#!/usr/bin/env python3
"""Apply one hash-pinned mechanical extraction, then restore migration tooling."""
from __future__ import annotations
import base64
import hashlib
import json
import lzma
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STAGE = 'macroscopic-pd-extraction'
BASELINE = 'c796e177fbf961bffe710ac8a1db30a6320e3f75'
PAYLOAD_SHA256 = 'ee42171ae2c942cefa59dbeef55ab6a8b3beded550da07119a1c48a6e350d521'
PARTS = 6
ARCHIVE_SOURCE = 'archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex'
ARCHIVE_SOURCE_SHA256 = 'c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe(rel: str) -> Path:
    parts = Path(rel).parts
    if Path(rel).is_absolute() or '..' in parts or '.git' in parts or '.github' in parts or '.migration' in parts:
        raise ValueError('Unsafe extraction payload path: ' + rel)
    dest = (ROOT / rel).resolve()
    if not dest.is_relative_to(ROOT.resolve()):
        raise ValueError('Payload path escapes checkout: ' + rel)
    return dest


def restore_tooling() -> None:
    prepare = base64.b64decode((ROOT/'.migration/prepare-baseline.b64').read_text())
    workflow = base64.b64decode((ROOT/'.migration/workflow-baseline.b64').read_text())
    (ROOT/'.migration/prepare.py').write_bytes(prepare)
    (ROOT/'.github/workflows/prepare-migration.yml').write_bytes(workflow)
    for path in list((ROOT/'.migration').glob('extraction-payload-part-*.b64')) + [
        ROOT/'.migration/prepare-baseline.b64', ROOT/'.migration/workflow-baseline.b64'
    ]:
        path.unlink()


request = json.loads((ROOT/'.migration/request.json').read_text())
if request.get('stage') != STAGE or request.get('baseline_commit') != BASELINE:
    raise SystemExit('Unexpected extraction request')
if not os.environ.get('GITHUB_REF_NAME', '').startswith('migration/'):
    raise SystemExit('Preparation requires an explicit migration branch')
headers = subprocess.check_output(['git', 'cat-file', '-p', 'HEAD'], cwd=ROOT, text=True).split('\n\n', 1)[0].splitlines()
if 'parent ' + BASELINE not in headers:
    raise ValueError('Extraction request must directly follow the pinned baseline')
if sha(ROOT/ARCHIVE_SOURCE) != ARCHIVE_SOURCE_SHA256:
    raise ValueError('Pinned monolith source hash mismatch')

parts = [(ROOT/f'.migration/extraction-payload-part-{j}.b64').read_text() for j in range(1, PARTS+1)]
compressed = base64.b64decode(''.join(parts))
if hashlib.sha256(compressed).hexdigest() != PAYLOAD_SHA256:
    raise ValueError('Composite extraction payload hash mismatch')
payload = json.loads(lzma.decompress(compressed))
if payload.get('schema_version') != 1 or payload.get('stage') != STAGE or payload.get('baseline_commit') != BASELINE:
    raise ValueError('Unexpected extraction payload schema or baseline')
if payload.get('archive_source_sha256') != ARCHIVE_SOURCE_SHA256:
    raise ValueError('Extraction payload archive pin mismatch')

archive = json.loads((ROOT/'archive/manifest.json').read_text())['files']
archive_before = {rec['path']: sha(ROOT/rec['path']) for rec in archive}
record = []
for operation in payload['operations']:
    kind = operation['operation']
    rel = operation['path']
    path = safe(rel)
    print(f'{kind}: {rel}', flush=True)
    if kind == 'create':
        if path.exists():
            raise ValueError('Refusing to overwrite create target: ' + rel)
        path.parent.mkdir(parents=True, exist_ok=True)
    elif kind == 'replace':
        if not path.is_file():
            raise ValueError('Missing replace target: ' + rel)
    else:
        raise ValueError('Unexpected extraction operation: ' + kind)
    path.write_text(operation['content'], encoding='utf-8')
    if sha(path) != operation['after_sha256']:
        raise ValueError('Output hash mismatch: ' + rel)
    record.append({k: v for k, v in operation.items() if k != 'content'})

for rec in archive:
    if sha(ROOT/rec['path']) != archive_before[rec['path']] or sha(ROOT/rec['path']) != rec['sha256']:
        raise ValueError('Frozen archive changed: ' + rec['path'])

(ROOT/'notes/macroscopic-pd-extraction-record.json').write_text(json.dumps({
    'schema_version': 1,
    'stage': STAGE,
    'baseline_commit': BASELINE,
    'reviewed_payload_sha256': PAYLOAD_SHA256,
    'archive_source_sha256': ARCHIVE_SOURCE_SHA256,
    'operations': record,
    'preserved_archive_files': len(archive),
    'proof_status': 'mechanical extraction; audit pending'
}, indent=2) + '\n')
restore_tooling()
print(f'Applied and hash-verified {len(record)} extraction operations; preserved {len(archive)} archive files; restored migration tooling.')
