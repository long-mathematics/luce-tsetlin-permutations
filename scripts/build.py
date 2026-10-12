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


def frozen_archive_paths() -> set[Path]:
    manifest = ROOT/'archive/manifest.json'
    if not manifest.exists():
        return set()
    return {safe_path(rec['path']) for rec in json.loads(manifest.read_text())['files']}


def _strip_inline_code(line: str) -> str:
    out = []
    in_code = False
    for ch in line:
        if ch == chr(96):
            in_code = not in_code
            continue
        if not in_code:
            out.append(ch)
    return ''.join(out)


def _markdown_math_fragments(line: str) -> list[str]:
    plain = _strip_inline_code(line)
    fragments = []
    start = None
    i = 0
    backslash = chr(92)
    while i < len(plain):
        if plain[i] != '$':
            i += 1
            continue
        if i + 1 < len(plain) and plain[i + 1] == '$':
            i += 2
            continue
        if i and plain[i - 1] == backslash:
            i += 1
            continue
        if start is None:
            start = i + 1
        else:
            fragments.append(plain[start:i])
            start = None
        i += 1
    if start is not None:
        raise ValueError('Unclosed inline math delimiter')
    return fragments


def check_markdown_math(text: str, label: str = '<markdown>') -> None:
    # GitHub parses Markdown before MathJax. Keep editable Markdown to a
    # conservative subset that cannot lose backslashes to Markdown escaping.
    allowed_commands = {
        'Delta', 'Gamma', 'Phi', 'Rightarrow',
        'beta', 'bigl', 'bigr', 'epsilon', 'ell', 'frac', 'ge',
        'in', 'infty', 'int', 'kappa', 'lambda', 'lbrace', 'le',
        'left', 'log', 'longrightarrow', 'mathbb', 'mathcal', 'mathscr',
        'max', 'mid', 'min', 'mu', 'phi', 'pi', 'prod', 'qquad',
        'rbrace', 'right', 'sigma', 'sim', 'sqrt', 'sum', 'sup',
        'text', 'theta', 'to', 'varepsilon', 'varphi', 'zeta', 'mathrm',
    }
    lines = text.splitlines()
    in_code = False
    display = False
    fence = chr(96) * 3
    backslash = chr(92)
    display_token = '
    def inspect(expr: str, lineno: int) -> None:
        i = 0
        while i < len(expr):
            if expr[i] != backslash:
                i += 1
                continue
            if i + 1 >= len(expr):
                raise ValueError(f'Dangling backslash in {label}:{lineno}')
            nxt = expr[i + 1]
            if nxt == backslash:
                raise ValueError(f'TeX line-break escape in {label}:{lineno}')
            if not nxt.isalpha():
                raise ValueError(f'Backslash-plus-punctuation in {label}:{lineno}')
            j = i + 1
            while j < len(expr) and expr[j].isalpha():
                j += 1
            command = expr[i + 1:j]
            if command not in allowed_commands:
                raise ValueError(f'Unreviewed TeX command in {label}:{lineno}: {command}')
            i = j

    for i, line in enumerate(lines):
        lineno = i + 1
        stripped = line.strip()

        if stripped.startswith(fence):
            if stripped == fence + 'math':
                raise ValueError(f'Use double-dollar display math rather than fenced math in {label}:{lineno}')
            in_code = not in_code
            continue
        if in_code:
            continue

        plain_line = _strip_inline_code(line)
        plain = plain_line.strip()
        for legacy in (backslash + '(', backslash + ')', backslash + '[', backslash + ']'):
            if legacy in plain_line:
                raise ValueError(f'Unsupported math delimiter in {label}:{lineno}')

        if display_token in plain:
            if plain != display_token:
                raise ValueError(f'Display delimiter must occupy its own line in {label}:{lineno}')
            if not display:
                if i and lines[i - 1].strip():
                    raise ValueError(f'Missing blank line before display in {label}:{lineno}')
                display = True
            else:
                if i + 1 < len(lines) and lines[i + 1].strip():
                    raise ValueError(f'Missing blank line after display in {label}:{lineno}')
                display = False
            continue

        if display:
            if stripped in {'=', '-', '---', '***', '___'} or (
                len(stripped) > 1 and stripped[0] in '*+-' and stripped[1].isspace()
            ):
                raise ValueError(f'Markdown structure inside math display in {label}:{lineno}')
            inspect(line, lineno)
        else:
            for expr in _markdown_math_fragments(line):
                inspect(expr, lineno)

    if display:
        raise ValueError(f'Unclosed math display in {label}')


def check_readme_math(text: str) -> None:
    check_markdown_math(text, 'README.md')


def check_markdown(allow_pending: bool = False) -> None:
    # Link checking remains scoped to canonical navigation documents.
    for file in [ROOT/'README.md', ROOT/'THEOREM_STATUS.md', ROOT/'DEPENDENCIES.md', ROOT/'CONTRIBUTING.md', ROOT/'notes/migration-plan.md']:
        text = file.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            dest = (file.parent / target.split('#', 1)[0]).resolve()
            if not dest.exists() and not (allow_pending and dest in {safe_path(d['pdf']) for d in catalog()}):
                raise ValueError(f'Broken link in {file.name}: {target}')

    # Rendering checks apply to every editable Markdown file. Exact files in
    # archive/manifest.json remain byte-preserved provenance and are exempt.
    frozen = frozen_archive_paths()
    for file in sorted(ROOT.rglob('*.md')):
        if file in frozen:
            continue
        check_markdown_math(file.read_text(), str(file.relative_to(ROOT)))

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
 * 2

    def inspect(expr: str, lineno: int) -> None:
        i = 0
        while i < len(expr):
            if expr[i] != backslash:
                i += 1
                continue
            if i + 1 >= len(expr):
                raise ValueError(f'Dangling backslash in {label}:{lineno}')
            nxt = expr[i + 1]
            if nxt == backslash:
                raise ValueError(f'TeX line-break escape in {label}:{lineno}')
            if not nxt.isalpha():
                raise ValueError(f'Backslash-plus-punctuation in {label}:{lineno}')
            j = i + 1
            while j < len(expr) and expr[j].isalpha():
                j += 1
            command = expr[i + 1:j]
            if command not in allowed_commands:
                raise ValueError(f'Unreviewed TeX command in {label}:{lineno}: {command}')
            i = j

    for i, line in enumerate(lines):
        lineno = i + 1
        stripped = line.strip()

        if stripped.startswith(fence):
            if stripped == fence + 'math':
                raise ValueError(f'Use $ rather than fenced math in {label}:{lineno}')
            in_code = not in_code
            continue
        if in_code:
            continue

        plain_line = _strip_inline_code(line)
        plain = plain_line.strip()
        for legacy in (backslash + '(', backslash + ')', backslash + '[', backslash + ']'):
            if legacy in plain_line:
                raise ValueError(f'Unsupported math delimiter in {label}:{lineno}')

        if '$' in plain:
            if plain != '$':
                raise ValueError(f'Display delimiter must occupy its own line in {label}:{lineno}')
            if not display:
                if i and lines[i - 1].strip():
                    raise ValueError(f'Missing blank line before display in {label}:{lineno}')
                display = True
            else:
                if i + 1 < len(lines) and lines[i + 1].strip():
                    raise ValueError(f'Missing blank line after display in {label}:{lineno}')
                display = False
            continue

        if display:
            if stripped in {'=', '-', '---', '***', '___'} or (
                len(stripped) > 1 and stripped[0] in '*+-' and stripped[1].isspace()
            ):
                raise ValueError(f'Markdown structure inside math display in {label}:{lineno}')
            inspect(line, lineno)
        else:
            for expr in _markdown_math_fragments(line):
                inspect(expr, lineno)

    if display:
        raise ValueError(f'Unclosed math display in {label}')


def check_readme_math(text: str) -> None:
    check_markdown_math(text, 'README.md')


def check_markdown(allow_pending: bool = False) -> None:
    # Link checking remains scoped to canonical navigation documents.
    for file in [ROOT/'README.md', ROOT/'THEOREM_STATUS.md', ROOT/'DEPENDENCIES.md', ROOT/'CONTRIBUTING.md', ROOT/'notes/migration-plan.md']:
        text = file.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            dest = (file.parent / target.split('#', 1)[0]).resolve()
            if not dest.exists() and not (allow_pending and dest in {safe_path(d['pdf']) for d in catalog()}):
                raise ValueError(f'Broken link in {file.name}: {target}')

    # Rendering checks apply to every editable Markdown file. Exact files in
    # archive/manifest.json remain byte-preserved provenance and are exempt.
    frozen = frozen_archive_paths()
    for file in sorted(ROOT.rglob('*.md')):
        if file in frozen:
            continue
        check_markdown_math(file.read_text(), str(file.relative_to(ROOT)))

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
