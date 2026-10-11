#!/usr/bin/env python3
"""Apply the audited macroscopic PD/GEM clarifications and restore request tooling."""
from __future__ import annotations
import base64
import hashlib
import json
import lzma
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STAGE = 'macroscopic-pd-audit-repair'
BASELINE = 'f7eb751eb6d5a7afd21e2139f0d17176557120b4'
REQUEST_PARENT = '10b4467619a9e985046987d0104141dba9c1fbb9'
PAYLOAD_SHA256 = '3ececa6ee8d054bc0066445c480a6308756c7540f584e85ef3059bd645815a65'
PAYLOAD_FILES = [ROOT/f'.migration/macroscopic-pd-repair-payload-part-{j}.b64' for j in range(1, 7)]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe(rel: str) -> Path:
    parts = Path(rel).parts
    if Path(rel).is_absolute() or '..' in parts or '.git' in parts or '.github' in parts or '.migration' in parts:
        raise ValueError('Unsafe repair payload path: '+rel)
    dest = (ROOT/rel).resolve()
    if not dest.is_relative_to(ROOT.resolve()):
        raise ValueError('Payload path escapes checkout: '+rel)
    return dest


def require_hash(path: Path, expected: str) -> None:
    if not path.is_file() or sha(path) != expected:
        raise ValueError('Content hash mismatch: '+str(path.relative_to(ROOT)))


request = json.loads((ROOT/'.migration/request.json').read_text())
if request.get('stage') != STAGE or request.get('baseline_commit') != BASELINE:
    raise SystemExit('Unexpected PD/GEM repair request')
if not os.environ.get('GITHUB_REF_NAME', '').startswith('migration/'):
    raise SystemExit('Preparation requires an explicit migration branch')
headers = subprocess.check_output(['git','cat-file','-p','HEAD'], cwd=ROOT, text=True).split('\n\n',1)[0].splitlines()
if 'parent '+REQUEST_PARENT not in headers:
    raise ValueError('Repair retry must directly follow the reviewed request commit')

compressed = base64.b64decode(''.join(path.read_text() for path in PAYLOAD_FILES))
if hashlib.sha256(compressed).hexdigest() != PAYLOAD_SHA256:
    raise ValueError('PD/GEM repair payload hash mismatch')
payload = json.loads(lzma.decompress(compressed))
if payload.get('schema_version') != 1 or payload.get('stage') != STAGE or payload.get('baseline_commit') != BASELINE:
    raise ValueError('Unexpected PD/GEM repair payload schema or baseline')

archive = json.loads((ROOT/'archive/manifest.json').read_text())['files']
archive_before = {rec['path']: sha(ROOT/rec['path']) for rec in archive}
record=[]
for operation in payload['operations']:
    kind=operation['operation']
    rel=operation['path']
    path=safe(rel)
    print(f'{kind}: {rel}', flush=True)
    if kind == 'replace':
        require_hash(path, operation['before_sha256'])
    elif kind == 'create':
        if path.exists():
            raise ValueError('Refusing to overwrite create target: '+rel)
        path.parent.mkdir(parents=True, exist_ok=True)
    else:
        raise ValueError('Unexpected repair operation: '+kind)
    path.write_text(operation['content'], encoding='utf-8')
    require_hash(path, operation['after_sha256'])
    record.append({k:v for k,v in operation.items() if k != 'content'})

for rec in archive:
    path=ROOT/rec['path']
    if sha(path) != archive_before[rec['path']] or sha(path) != rec['sha256']:
        raise ValueError('Frozen archive changed: '+rec['path'])

for rel in ('.migration/prepare.py', '.github/workflows/prepare-migration.yml'):
    baseline_bytes = subprocess.check_output(['git','show',f'{BASELINE}:{rel}'], cwd=ROOT)
    (ROOT/rel).write_bytes(baseline_bytes)
for path in PAYLOAD_FILES:
    path.unlink()
print(f'Applied and hash-verified {len(record)} audited repairs; preserved {len(archive)} frozen archive files; restored request tooling.')
