#!/usr/bin/env python3
"""Build active papers; verify immutable archive bytes and deterministic PDFs."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / '.build'
MANIFEST = ROOT / 'output/pdf/manifest.json'
STATUSES = {'imported', 'working', 'current-research'}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def catalog() -> list[dict]:
    data = json.loads((ROOT / 'papers.json').read_text())
    if data.get('schema_version') != 1:
        raise ValueError('Unsupported document catalog version')
    return data['documents']


def safe_path(rel: str) -> Path:
    path = (ROOT / rel).resolve()
    if not path.is_relative_to(ROOT.resolve()):
        raise ValueError('Path escapes repository: ' + rel)
    return path


def check_catalog() -> None:
    docs = catalog()
    for key in ('id', 'source', 'pdf'):
        vals = [d[key] for d in docs]
        if len(set(vals)) != len(vals):
            raise ValueError('Duplicate catalog ' + key)
    ids = {d['id'] for d in docs}
    graph = {d['id']: d.get('dependencies', []) for d in docs}
    for d in docs:
        if d['status'] not in STATUSES:
            raise ValueError('Unknown proof status: ' + d['status'])
        if not set(d.get('dependencies', [])) <= ids:
            raise ValueError('Unknown dependency: ' + d['id'])
        source = safe_path(d['source'])
        safe_path(d['pdf'])
        if not source.is_file():
            raise ValueError('Missing source: ' + d['source'])
        text = source.read_text()
        if 'Christopher D. Long' not in text:
            raise ValueError('Missing author: ' + d['source'])
        if d['source'].startswith('archive/') or 'resolution-candidate' in d['source']:
            raise ValueError('Historical source registered as active')
    visiting, done = set(), set()
    def visit(node: str) -> None:
        if node in visiting:
            raise ValueError('Cyclic document dependency at ' + node)
        if node in done:
            return
        visiting.add(node)
        for child in graph[node]:
            visit(child)
        visiting.remove(node)
        done.add(node)
    for node in graph:
        visit(node)


def check_markdown(allow_pending: bool = False) -> None:
    for file in [ROOT/'README.md', ROOT/'THEOREM_STATUS.md', ROOT/'DEPENDENCIES.md', ROOT/'CONTRIBUTING.md', ROOT/'notes/migration-plan.md']:
        text = file.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            dest = (file.parent / target.split('#', 1)[0]).resolve()
            if not dest.exists() and not (allow_pending and dest in {safe_path(d['pdf']) for d in catalog()}):
                raise ValueError(f'Broken link in {file.name}: {target}')
    check_readme_math((ROOT/'README.md').read_text())


def check_readme_math(text: str) -> None:
    # Keep README math to a conservative GitHub/MathJax subset. Use only
    # $...$ for inline math and $$...$$ for display math; avoid document-level
    # definitions/environments, repository-private aliases, and commands
    # rejected by GitHub's safe renderer (notably \\operatorname).
    forbidden_tokens = (
        r'\\(', r'\\)', r'\\[', r'\\]',
        r'\\newcommand', r'\\renewcommand', r'\\providecommand',
        r'\\def', r'\\gdef', r'\\xdef', r'\\let',
        r'\\DeclareMathOperator', r'\\operatorname',
        r'\\begin{', r'\\end{',
        r'\\input', r'\\include', r'\\require',
        r'\\href', r'\\url', r'\\htmlClass', r'\\htmlId',
        r'\\htmlStyle', r'\\class', r'\\style', r'\\cssId',
    )
    for token in forbidden_tokens:
        if token in text:
            raise ValueError('Unsupported README TeX command/delimiter: ' + token)
    if re.search(r'\\(?:Ee|Pp|TV|Kol|one|Pois|dd|cL)\\b', text):
        raise ValueError('Private manuscript macro in README')
    display = False
    for line in text.splitlines():
        s = line.strip()
        if s == '$':
            raise ValueError('Single-dollar display delimiter')
        if '$$' in s:
            if s != '$$':
                raise ValueError('Display delimiter must occupy its own line')
            display = not display
            continue
        if display and (re.fullmatch(r'=+|-+', s) or re.match(r'^[+*-]\\s+', s)):
            raise ValueError('Markdown structure inside mathematical display')
    if display:
        raise ValueError('Unclosed README display')

def check_archive() -> None:
    path = ROOT/'archive/manifest.json'
    if not path.exists():
        return
    for rec in json.loads(path.read_text())['files']:
        file = safe_path(rec['path'])
        if not file.is_file() or digest(file) != rec['sha256']:
            raise ValueError('Frozen archive changed: ' + rec['path'])


def build_one(doc: dict) -> tuple[Path, int]:
    source = safe_path(doc['source'])
    work = BUILD/doc['id']
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    env = dict(os.environ, SOURCE_DATE_EPOCH='1791504000', FORCE_SOURCE_DATE='1', TZ='UTC')
    cmd = ['latexmk', '-pdf', '-g', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-latexoption=-no-shell-escape', '-outdir='+str(work), source.name]
    result = subprocess.run(cmd, cwd=source.parent, env=env, capture_output=True, text=True, timeout=300)
    (work/'build-console.txt').write_text(result.stdout+result.stderr)
    if result.returncode:
        raise ValueError('LaTeX failed: ' + doc['id'])
    log = (work/(source.stem+'.log')).read_text(errors='replace')
    bad = [s for s in log.splitlines() if re.search(r'^!|LaTeX Warning:.*undefined|Citation .* undefined|Reference .* undefined|multiply defined|Overfull ', s)]
    if bad:
        raise ValueError('LaTeX diagnostics: '+doc['id']+'\n'+'\n'.join(bad[:30]))
    pdf = work/(source.stem+'.pdf')
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
    return pdf, pages


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    check_catalog(); check_markdown(allow_pending=not args.check); check_archive()
    docs = catalog()
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {'documents': []}
    records = {r['id']: r for r in old['documents']}
    if args.check and set(records) != {d['id'] for d in docs}:
        raise ValueError('Catalog and PDF manifest differ; run make pdf')
    new = []
    for doc in docs:
        target = safe_path(doc['pdf'])
        src_hash = digest(safe_path(doc['source']))
        if args.check:
            rec = records[doc['id']]
            if rec['source_sha256'] != src_hash or not target.exists() or digest(target) != rec['pdf_sha256']:
                raise ValueError('Stale snapshot: '+doc['id'])
        print('Building '+doc['id'], flush=True)
        built, pages = build_one(doc)
        if args.check and digest(built) != digest(target):
            raise ValueError('PDF bytes differ from snapshot: '+doc['id'])
        if not args.check:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(built, target)
        new.append(dict(id=doc['id'], source=doc['source'], source_sha256=src_hash, pdf=doc['pdf'], pdf_sha256=digest(built), pages=pages))
    if not args.check:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps({'schema_version': 1, 'documents': new}, indent=2)+'\n')
    check_markdown()
    print(f'Verified {len(docs)} active documents and frozen archives.')

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
