#!/usr/bin/env python3
"""Apply reviewed manuscript changes without modifying workflow configuration."""
from __future__ import annotations
import hashlib
import json
import lzma
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '1524e027382e2d6f10a392790d00075717d752ef'
PREVIOUS_REQUEST = 'f61c91a2b3a2c3d0f77ad9e966c042f2598ddd16'
PAYLOAD_SHA256 = 'a6a7d71ff87930d084ff0e278fe932962594ed9316c9d3b0e98a39659880ea3c'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe(rel: str) -> Path:
    parts = Path(rel).parts
    if Path(rel).is_absolute() or '..' in parts or '.git' in parts or '.github' in parts:
        raise ValueError('Unsafe or workflow payload path: '+rel)
    dest = (ROOT/rel).resolve()
    if not dest.is_relative_to(ROOT.resolve()):
        raise ValueError('Payload path escapes checkout')
    return dest


def require_hash(path: Path, expected: str) -> None:
    if not path.is_file() or sha(path) != expected:
        raise ValueError('Content hash mismatch: '+str(path.relative_to(ROOT)))


request = json.loads((ROOT/'.migration/request.json').read_text())
if request.get('stage') != 'integration':
    raise SystemExit('This preparation script handles integration only')
if not os.environ.get('GITHUB_REF_NAME', '').startswith('migration/'):
    raise SystemExit('Preparation requires an explicit migration branch')
headers = subprocess.check_output(['git', 'cat-file', '-p', 'HEAD'], cwd=ROOT, text=True).split('\n\n', 1)[0].splitlines()
if 'parent '+PREVIOUS_REQUEST not in headers:
    raise ValueError('Publication repair must directly follow the pinned integration request')
chunks = [ROOT/f'.migration/payload-part-{j}.bin' for j in range(1, 6)]
data = b''.join(path.read_bytes() for path in chunks)
if hashlib.sha256(data).hexdigest() != PAYLOAD_SHA256:
    raise ValueError('Composite integration payload hash mismatch')
payload = json.loads(lzma.decompress(data))
if payload.get('schema_version') != 1 or payload.get('baseline_commit') != BASELINE:
    raise ValueError('Unexpected integration payload schema or baseline')
original_archive = json.loads((ROOT/'archive/manifest.json').read_text())['files']
record = []
for operation in payload['operations']:
    kind = operation['operation']
    path = safe(operation['path'])
    print(f'{kind}: {operation["path"]}', flush=True)
    if kind in ('patch', 'delete'):
        require_hash(path, operation['before_sha256'])
    if kind == 'patch':
        patch = operation['patch'].encode('utf-8')
        expected_headers = f'--- a/{operation["path"]}\n+++ b/{operation["path"]}\n'
        if not operation['patch'].startswith(expected_headers):
            raise ValueError('Unexpected patch headers')
        subprocess.run(['git', 'apply', '--check', '-'], input=patch, cwd=ROOT, check=True)
        subprocess.run(['git', 'apply', '-'], input=patch, cwd=ROOT, check=True)
    elif kind == 'create':
        if path.exists():
            raise ValueError('Refusing to overwrite existing create target')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(operation['content'], encoding='utf-8')
    elif kind == 'copy':
        source = safe(operation['source'])
        require_hash(source, operation['before_sha256'])
        if path.exists():
            raise ValueError('Refusing to overwrite existing copy target')
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, path)
    elif kind == 'delete':
        path.unlink()
    else:
        raise ValueError('Unexpected integration operation: '+kind)
    if 'after_sha256' in operation:
        require_hash(path, operation['after_sha256'])
    record.append({k: v for k, v in operation.items() if k not in ('content', 'patch')})
for archived in original_archive:
    archived_path = (ROOT/archived['path']).resolve()
    if not archived_path.is_relative_to((ROOT/'archive').resolve()):
        raise ValueError('Unexpected preservation manifest path')
    require_hash(archived_path, archived['sha256'])
subprocess.run(['git', 'diff', '--exit-code', '--', '.github/'], cwd=ROOT, check=True)
(ROOT/'notes/integration-record.json').write_text(json.dumps({'schema_version': 1, 'baseline_commit': BASELINE, 'reviewed_payload_sha256': PAYLOAD_SHA256, 'operations': record, 'workflow_configuration': 'Artifact export paths were committed through the repository connector before preparation; the preparation job never edits workflow files.', 'preserved_original_archive_files': len(original_archive)}, indent=2)+'\n')
for path in chunks:
    path.unlink()
print(f'Applied and hash-verified {len(record)} operations; original {len(original_archive)} archive files unchanged; workflow files unchanged by preparation.')
