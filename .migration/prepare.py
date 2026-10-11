#!/usr/bin/env python3
"""One-shot, pinned preservation import; never edits the upstream repository."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SHA = '6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0'
UPSTREAM = 'long-mathematics/nonuniform-random-permutations'
BASE = f'https://raw.githubusercontent.com/{UPSTREAM}/{SHA}/'
ARCHIVE = ROOT/'archive'/SHA[:7]
request = json.loads((ROOT/'.migration/request.json').read_text())
if request['stage'] != 'import':
    raise SystemExit('This script implements the preservation import only')
if (ROOT/'archive/manifest.json').exists():
    raise SystemExit('Preservation import already exists; refusing to overwrite it')


def fetch(path: str) -> bytes:
    for attempt in range(4):
        try:
            req = urllib.request.Request(BASE+path, headers={'User-Agent': 'luce-tsetlin-preservation-import'})
            with urllib.request.urlopen(req, timeout=90) as response:
                return response.read()
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2**attempt)


def write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


manifest_bytes = fetch('output/pdf/manifest.json')
upstream_manifest = json.loads(manifest_bytes)
records = {r['source']: r for r in upstream_manifest['documents']}
items = [
 ('archive-monolith', 'papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex', None, 'Boundary, Terminal, Diagonal, and Cycle Limit Laws for Luce Permutations', []),
 ('mesoscopic-switching', 'papers/02-mesoscopic-luce-cycles/mesoscopic-luce-cycles.tex', 'papers/mesoscopic-switching/mesoscopic-luce-cycles.tex', 'Mesoscopic cycles of comparable-rate Luce permutations', []),
 ('erdos-turan-order', 'papers/03-luce-erdos-turan/luce-erdos-turan.tex', 'papers/erdos-turan-order/luce-erdos-turan.tex', 'An Erdos--Turan Law for Comparable-Rate Luce Permutations', ['mesoscopic-switching']),
 ('sharp-order-edgeworth', 'papers/04-luce-edgeworth/luce-edgeworth.tex', 'papers/sharp-order-edgeworth/luce-edgeworth.tex', 'A Sharp Berry--Esseen Theorem and First Edgeworth Expansion for Logarithmic Luce Order', ['mesoscopic-switching', 'erdos-turan-order']),
 ('functional-erdos-turan', 'notes/working/functional-luce-erdos-turan.tex', 'notes/working/functional-luce-erdos-turan.tex', 'Functional Erdos--Turan Universality for Comparable-Rate Luce Permutations', ['mesoscopic-switching', 'erdos-turan-order']),
]
expected_sources = {
 'archive-monolith': 'c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028',
 'mesoscopic-switching': '30bb9a373aa8d83e37dc96f425417fa35d343aba44504d5f2a5e9314ac6ccaed',
 'erdos-turan-order': 'cf628b24b6ef70b1b54ce91b849096562091b406ee05525156e016c2787f50a3',
 'sharp-order-edgeworth': 'dfe6a24f7002eaa2c732e2448c290f416cc72a62bdf8dbda47228fe07daeba80',
 'functional-erdos-turan': 'bae8958e825dc3f3d8bd4290ae4715f9d6fbce1d1eb17ca101699c9ba8e5bffa',
}
frozen = []
docs = []
imports = []


def preserve(path: str, data: bytes) -> None:
    dest = ARCHIVE/path
    write(dest, data)
    frozen.append({'path': str(dest.relative_to(ROOT)), 'upstream_path': path, 'sha256': hashlib.sha256(data).hexdigest(), 'upstream_url': BASE+path})


preserve('output/pdf/manifest.json', manifest_bytes)
for ident, source, target, title, dependencies in items:
    record = records[source]
    data = fetch(source)
    source_hash = hashlib.sha256(data).hexdigest()
    if source_hash != expected_sources[ident] or source_hash != record['source_sha256']:
        raise ValueError('Pinned source hash mismatch: '+source)
    pdf_data = fetch(record['pdf'])
    if hashlib.sha256(pdf_data).hexdigest() != record['pdf_sha256']:
        raise ValueError('Pinned PDF hash mismatch: '+record['pdf'])
    preserve(source, data)
    preserve(record['pdf'], pdf_data)
    if target is not None:
        write(ROOT/target, data)
        pdf = 'output/pdf/'+Path(record['pdf']).name
        write(ROOT/pdf, pdf_data)
        docs.append(dict(id=ident, title=title, source=target, pdf=pdf, status='working' if ident == 'functional-erdos-turan' else 'imported', dependencies=dependencies))
        imports.append(dict(id=ident, upstream_source=source, active_source=target, imported_sha256=source_hash, original_pdf_sha256=record['pdf_sha256'], original_pages=record['pages']))
for source in ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'AGENTS.md', 'notes/repository-status.md', 'notes/provenance/mesoscopic-total-cycle-resolution-candidate.tex', 'notes/provenance/mesoscopic-audit-and-repair.tex', 'notes/provenance/free-depth-endpoint-audit.md', 'scripts/build.py', 'tests/test_repository.py', '.github/workflows/latex.yml']:
    preserve(source, fetch(source))
write(ROOT/'archive/manifest.json', (json.dumps({'schema_version': 1, 'upstream_repository': UPSTREAM, 'upstream_commit': SHA, 'files': frozen}, indent=2)+'\n').encode())
write(ROOT/'notes/import-record.json', (json.dumps({'upstream_repository': UPSTREAM, 'upstream_commit': SHA, 'active_imports': imports}, indent=2)+'\n').encode())
write(ROOT/'papers.json', (json.dumps({'schema_version': 1, 'documents': docs}, indent=2)+'\n').encode())
write(ROOT/'archive/README.md', f'''# Frozen preservation archive

The directory `{SHA[:7]}/` preserves five Luce source/PDF pairs and the supporting status, audit, license, and build records from `{UPSTREAM}` at commit `{SHA}`. Every preserved file is checked against `manifest.json`.

The 139-page original is here, not an active editing target. The historical total-cycle resolution candidate remains rejected and is not an input to the newer functional proof. No theorem is re-audited or promoted by this import.

Active source copies initially match their imported source bytes. Active PDFs are rebuilt deterministically in the new repository; these may have different binary metadata from the preserved original PDFs, whose bytes remain unchanged here.
'''.encode())
readme = (ROOT/'README.md').read_text()
start = readme.index('## Migration status')
end = readme.index('## Reading and status')
rows = ['## Manuscripts', '', '| Manuscript | PDF | LaTeX | Import status |', '| --- | --- | --- | --- |']
for d in docs:
    rows.append(f"| {d['title']} | [PDF]({d['pdf']}) | [Source]({d['source']}) | {d['status']} |")
rows.extend(['', f"The **139-page original research draft** is preserved as [PDF](archive/{SHA[:7]}/output/pdf/luce-boundary-cycle-laws.pdf) and [LaTeX](archive/{SHA[:7]}/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex). It has not yet been split or newly audited.", '', '## Migration status', '', 'The preservation import is pinned and byte-checked. Importing a source does not upgrade its proof status. Total-cycle integration is the next separate PR; the functional manuscript remains a working branch until that integration.', '', 'The original [Nonuniform Random Permutations](https://github.com/long-mathematics/nonuniform-random-permutations) repository remains unchanged. Riffle, shelf, Thorp, and caching manuscripts remain there. This repository will be the canonical editing destination for the migrated Luce series; preserved copies are archival.', '', '[Preservation manifest](archive/manifest.json) · [Import mapping](notes/import-record.json)', ''])
(ROOT/'README.md').write_text(readme[:start]+'\n'.join(rows)+'\n'+readme[end:])
status = (ROOT/'THEOREM_STATUS.md').read_text()
status = status.replace('## Foundation state', '## Preservation import state')
status = status.replace('No manuscript is imported or promoted by the foundation PR. The coming import pins', 'Four editable manuscript copies and the archived original have been imported without source changes. No theorem is promoted by the import. The preserved upstream snapshot pins')
(ROOT/'THEOREM_STATUS.md').write_text(status)
print(f'Preserved {len(frozen)} files; registered {len(docs)} editable manuscripts without mathematical changes.')
