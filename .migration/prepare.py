#!/usr/bin/env python3
"""Mechanically extract the boundary-law theorem package from the frozen monolith."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "e950728f28b1aa3933b092a68a6b78bae328ac97"
ARCHIVE_REL = "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
ARCHIVE_SHA256 = "c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028"
PAPER_ID = "boundary-laws"
PAPER_TITLE = "Boundary Laws for Luce Rankings"
ACTIVE_REL = "papers/boundary-laws/boundary-laws.tex"
PDF_REL = "output/pdf/boundary-laws.pdf"

BLOCKS = [
    ("Exponential-race input", r"\subsection{The exponential race}", r"\subsection{Gumbel priorities}", "% BEGIN ARCHIVED BLOCK: exponential-race-input", "% END ARCHIVED BLOCK: exponential-race-input", 224, 233),
    ("Vanishing-block obstruction", r"\begin{proposition}[Vanishing-block implantation]\label{prop:implantation}", r"\begin{remark}\label{rem:implantation-consequences}", "% BEGIN ARCHIVED BLOCK: vanishing-block-obstruction", "% END ARCHIVED BLOCK: vanishing-block-obstruction", 539, 598),
    ("Top and bottom boundary laws", r"\section{Top windows: exact boundary identities}", r"\section{Regular positive profiles: fixed points and short cycles}\label{sec:regular}", "% BEGIN ARCHIVED BLOCK: top-bottom-boundary-laws", "% END ARCHIVED BLOCK: top-bottom-boundary-laws", 611, 864),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


request = json.loads((ROOT / ".migration/request.json").read_text(encoding="utf-8"))
expected_request = {"stage": "integration", "task": "boundary-laws-extraction", "baseline_commit": BASE}
if request != expected_request:
    raise ValueError("Unexpected boundary extraction request")
if not os.environ.get("GITHUB_REF_NAME", "").startswith("migration/"):
    raise SystemExit("Extraction requires an explicit migration branch")
headers = subprocess.check_output(["git", "cat-file", "-p", "HEAD"], cwd=ROOT, text=True).split("\n\n", 1)[0].splitlines()
if "parent " + BASE not in headers:
    raise ValueError("Boundary extraction request must directly follow the pinned main head")

archive_path = ROOT / ARCHIVE_REL
if sha(archive_path) != ARCHIVE_SHA256:
    raise ValueError("Frozen monolith source hash mismatch")
archive = archive_path.read_text(encoding="utf-8")

selected_blocks = []
selected_math = ""
for name, start, end, begin_marker, end_marker, expected_first, expected_last in BLOCKS:
    i = archive.index(start)
    j = archive.index(end, i)
    block = archive[i:j]
    first = line_number(archive, i)
    last = line_number(archive, j) - 1
    if (first, last) != (expected_first, expected_last):
        raise ValueError(f"Unexpected archived range for {name}: {(first, last)}")
    selected_blocks.append((name, block, begin_marker, end_marker, first, last))
    selected_math += block

labels = set(re.findall(r"\\label\{([^}]+)\}", selected_math))
refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", selected_math))
if refs - labels:
    raise ValueError("Unresolved internal references: " + ", ".join(sorted(refs - labels)))

citation_keys = []
for match in re.finditer(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", selected_math):
    for key in match.group(1).split(","):
        key = key.strip()
        if key and key not in citation_keys:
            citation_keys.append(key)

bib_entries = {}
if citation_keys:
    bib_start = archive.index(r"\begin{thebibliography}")
    bib_end = archive.index(r"\end{thebibliography}", bib_start)
    bib_body = archive[bib_start:bib_end]
    matches = list(re.finditer(r"(?m)^\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bib_body))
    for idx, match in enumerate(matches):
        stop = matches[idx + 1].start() if idx + 1 < len(matches) else len(bib_body)
        bib_entries[match.group(1)] = bib_body[match.start():stop].rstrip() + "\n"
    missing = [key for key in citation_keys if key not in bib_entries]
    if missing:
        raise ValueError("Missing bibliography entries: " + ", ".join(missing))

preamble = r"""\documentclass[11pt]{article}
\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{mathrsfs}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue,hypertexnames=false,pdftitle={Boundary Laws for Luce Rankings},pdfauthor={Christopher D. Long}}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{warning}[theorem]{Warning}
\newtheorem{definition}[theorem]{Definition}
\newcommand{\Pp}{\mathbb P}
\newcommand{\Ee}{\mathbb E}
\newcommand{\Rr}{\mathbb R}
\newcommand{\Nn}{\mathbb N}
\newcommand{\Zz}{\mathbb Z}
\newcommand{\one}{\mathbf 1}
\newcommand{\TV}{\mathrm{TV}}
\newcommand{\Pois}{\operatorname{Pois}}
\newcommand{\Exp}{\operatorname{Exp}}
\newcommand{\PPP}{\operatorname{PPP}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\Cov}{\operatorname{Cov}}
\newcommand{\diag}{\operatorname{diag}}
\newcommand{\dd}{\,d}
\newcommand{\eps}{\varepsilon}
\newcommand{\calD}{\mathcal D}
\newcommand{\calC}{\mathcal C}
\newcommand{\calE}{\mathcal E}
\newcommand{\calG}{\mathcal G}
\title{Boundary Laws for Luce Rankings}
\author{Christopher D. Long}
\date{Mechanical extraction --- proof audit pending}
\begin{document}
\maketitle
\begin{abstract}
A Luce ranking is generated by ordering independent exponential clocks with prescribed positive rates. This paper gives exact finite identities for the top of the ranking and sharp limiting laws for the bottom. The top-window law has an exact total-variation formula equal to the collision probability of an associated product sample, together with an exact one-sided relative defect. For countably many clocks, the paper identifies the coordinatewise limiting bottom-window subprobability law and computes its missing mass exactly as a terminal leakage event. A vanishing-block construction also shows why permuton convergence alone cannot control microscopic cycle statistics.
\end{abstract}
\tableofcontents
\section{Status and provenance}
This source is a mechanical extraction from the frozen 139-page Luce manuscript at repository commit \texttt{6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0}. The mathematical blocks between the archival sentinels below are copied byte-for-byte from the frozen source. Only the standalone preamble, abstract, section wrappers, provenance notice, and any cited bibliography entries have been added.

The extraction preserves every theorem hypothesis, identity, limiting statement, quantifier, and proof step in the selected boundary package. It does not audit, repair, strengthen, weaken, or modernize the mathematics. Its status remains a working mechanical extraction until a separate adversarial audit is completed.
\section{Exponential-race input}
"""

parts = [preamble]
for idx, (name, block, begin_marker, end_marker, first, last) in enumerate(selected_blocks):
    if idx == 1:
        parts.append("\n\\section{A microscopic obstruction}\n\n")
    parts.extend([begin_marker + "\n", block, end_marker + "\n"])
if citation_keys:
    parts.append("\n\\begin{thebibliography}{99}\n\n")
    for key in citation_keys:
        parts.append(bib_entries[key] + "\n")
    parts.append("\\end{thebibliography}\n")
parts.append("\n\\end{document}\n")
active = "".join(parts)
write(ACTIVE_REL, active)

active_text = (ROOT / ACTIVE_REL).read_text(encoding="utf-8")
for name, block, begin_marker, end_marker, first, last in selected_blocks:
    observed = active_text.split(begin_marker + "\n", 1)[1].split(end_marker, 1)[0]
    if observed != block:
        raise ValueError("Active extraction is not byte-preserving: " + name)

env_pattern = re.compile(r"\\begin\{(theorem|proposition|lemma|corollary)\}(?:\[([^\]]+)\])?")
rows = []
for match in env_pattern.finditer(selected_math):
    env = match.group(1)
    title = (match.group(2) or "—").replace("|", r"\|")
    stop = selected_math.find("\\end{" + env + "}", match.end())
    segment = selected_math[match.start():stop]
    label_match = re.search(r"\\label\{([^}]+)\}", segment)
    label = label_match.group(1) if label_match else "(unlabeled)"
    if label == "(unlabeled)":
        archived_offset = archive.index(match.group(0)); active_offset = active.index(match.group(0))
    else:
        archived_offset = archive.index(r"\label{" + label + "}"); active_offset = active.index(r"\label{" + label + "}")
    rows.append((env.title(), title, label, line_number(archive, archived_offset), line_number(active, active_offset)))

map_lines = ["# Boundary-laws extraction map", "", "Frozen source:", f"`{ARCHIVE_REL}`", "", f"Frozen source SHA-256: `{ARCHIVE_SHA256}`.", "", "The mathematical blocks are copied byte-for-byte. The active paper adds only the standalone wrapper and bibliography entries actually cited by the selected blocks.", "", "## Source ranges", "", "| Block | Archived lines | Active sentinel |", "| --- | ---: | --- |"]
for name, block, begin_marker, end_marker, first, last in selected_blocks:
    map_lines.append(f"| {name} | {first}--{last} | `{begin_marker}` |")
map_lines += ["", "## Theorem and lemma provenance", "", "Labels are unchanged, so every old label is also the new label.", "", "| Environment | Title | Old label = new label | Archived line | Active line |", "| --- | --- | --- | ---: | ---: |"]
for env, title, label, old_line, new_line in rows:
    map_lines.append(f"| {env} | {title} | `{label}` | {old_line} | {new_line} |")
map_lines += ["", "## Closure checks", "", f"- theorem/proposition/lemma/corollary environments: **{len(rows)}**;", f"- labels: **{len(labels)}**;", f"- distinct internal reference targets: **{len(refs)}**;", f"- cited bibliography keys: **{len(citation_keys)}**;", "- unresolved internal references: **0**;", "- active-paper proof dependencies: **0**.", "", "This is an extraction and provenance map, not a correctness audit."]
write("papers/boundary-laws/EXTRACTION_MAP.md", "\n".join(map_lines) + "\n")

record = {"schema_version": 1, "stage": "boundary-laws-extraction", "baseline_commit": BASE, "archive_source": ARCHIVE_REL, "archive_source_sha256": ARCHIVE_SHA256, "active_source": ACTIVE_REL, "active_source_sha256": sha(ROOT / ACTIVE_REL), "source_ranges": [{"name": name, "first_line": first, "last_line": last, "sentinel": begin_marker} for name, block, begin_marker, end_marker, first, last in selected_blocks], "theorem_environments": len(rows), "labels": len(labels), "reference_targets": len(refs), "citation_keys": citation_keys, "proof_status": "mechanical extraction; adversarial audit pending"}
write("notes/boundary-laws-extraction-record.json", json.dumps(record, indent=2) + "\n")
write("audits/boundary-laws-extraction.md", f"""# Mechanical extraction record: boundary laws

Date: 12 October 2026.

This record covers only the mechanical extraction of the boundary-law theorem package from the frozen 139-page manuscript. It is not a mathematical audit, novelty review, or formal verification.

The active paper contains the exact archived exponential-race identity, the vanishing-block obstruction, the top-window total-variation and relative-defect identities, the birthday transfer, finite bottom-window convergence, terminal leakage, and the log-log phase diagram. The selected mathematical blocks are byte-for-byte identical to archived lines 224--233, 539--598, and 611--864.

All {len(rows)} theorem-like environments, all {len(labels)} labels, all {len(refs)} internal reference targets, and every cited bibliography entry are present. No active manuscript is imported as a proof dependency. The detailed old-label/new-label map is `papers/boundary-laws/EXTRACTION_MAP.md`.

The extraction does not assess the correctness of the exact top-window identities, infinite-product limiting law, Borel--Cantelli leakage argument, or phase diagram. A separate adversarial audit is required before any status promotion.
""")

write("tests/test_boundary_extraction.py", r'''from pathlib import Path
import json
import re
import unittest
ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
ACTIVE = ROOT / "papers/boundary-laws/boundary-laws.tex"
BLOCKS = [
    (r"\subsection{The exponential race}", r"\subsection{Gumbel priorities}", "% BEGIN ARCHIVED BLOCK: exponential-race-input", "% END ARCHIVED BLOCK: exponential-race-input"),
    (r"\begin{proposition}[Vanishing-block implantation]\label{prop:implantation}", r"\begin{remark}\label{rem:implantation-consequences}", "% BEGIN ARCHIVED BLOCK: vanishing-block-obstruction", "% END ARCHIVED BLOCK: vanishing-block-obstruction"),
    (r"\section{Top windows: exact boundary identities}", r"\section{Regular positive profiles: fixed points and short cycles}\label{sec:regular}", "% BEGIN ARCHIVED BLOCK: top-bottom-boundary-laws", "% END ARCHIVED BLOCK: top-bottom-boundary-laws"),
]
class BoundaryExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archive = ARCHIVE.read_text(encoding="utf-8"); cls.active = ACTIVE.read_text(encoding="utf-8")
    def test_blocks_are_byte_preserved(self):
        for source_start, source_end, active_start, active_end in BLOCKS:
            expected = self.archive[self.archive.index(source_start):self.archive.index(source_end, self.archive.index(source_start))]
            observed = self.active.split(active_start + "\n", 1)[1].split(active_end, 1)[0]
            self.assertEqual(observed, expected)
    def test_reference_and_citation_closure(self):
        labels = set(re.findall(r"\\label\{([^}]+)\}", self.active)); refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", self.active)); self.assertFalse(refs - labels)
        cites = set()
        for match in re.finditer(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", self.active): cites.update(key.strip() for key in match.group(1).split(","))
        bibitems = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", self.active)); self.assertFalse(cites - bibitems)
    def test_scope_and_working_status(self):
        for token in [r"\|P_k-Q_k\|_{\TV}=Q_k(\calD_k^c)", r"d_\infty^+(P_k,Q_k)", r"\sum_{a_1,\ldots,a_k}^{*}\mu_k(a_1,\ldots,a_k)", r"\Pp(N_0\ge k)", r"\theta_i=\beta\log i+\alpha\log\log i+O(1)"]: self.assertIn(token, self.active)
        catalog = json.loads((ROOT / "papers.json").read_text())["documents"]; doc = next(d for d in catalog if d["id"] == "boundary-laws"); self.assertEqual(doc["status"], "working"); self.assertEqual(doc.get("dependencies", []), [])
        status = (ROOT / "THEOREM_STATUS.md").read_text(); self.assertIn("Boundary laws", status); self.assertIn("Working mechanical extraction", status); self.assertIn("proof audit pending", status)
if __name__ == "__main__": unittest.main()
''')

catalog_path = ROOT / "papers.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
if any(doc["id"] == PAPER_ID for doc in catalog["documents"]): raise ValueError("boundary-laws already registered")
new_doc = {"id": PAPER_ID, "title": PAPER_TITLE, "source": ACTIVE_REL, "pdf": PDF_REL, "status": "working", "dependencies": []}
insert_at = next(i for i, doc in enumerate(catalog["documents"]) if doc["id"] == "regular-profile-cycles")
catalog["documents"].insert(insert_at, new_doc)
catalog_path.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")

readme_path = ROOT / "README.md"; readme = readme_path.read_text(encoding="utf-8")
row_anchor = "| Microscopic Cycles and Sparse Entries for Regular Luce Profiles |"
new_row = "| Boundary Laws for Luce Rankings | [PDF](output/pdf/boundary-laws.pdf) | [Source](papers/boundary-laws/boundary-laws.tex) | mechanical extraction; proof audit pending |\n"
readme = replace_once(readme, row_anchor, new_row + row_anchor, "README table row")
summary_anchor = "### Microscopic cycles and sparse entries for regular Luce profiles"
new_summary = """### Boundary laws for Luce rankings

[PDF](output/pdf/boundary-laws.pdf) · [LaTeX](papers/boundary-laws/boundary-laws.tex)

This paper isolates the finite top-window identities and infinite bottom-window leakage theory from the archived monolith. It proves that the exact top-window total-variation distance equals the collision probability of the corresponding product sample, gives the exact one-sided relative defect, and identifies the total mass lost by a limiting bottom-window law. A vanishing-block construction records why permuton convergence alone cannot control microscopic statistics.

**Status:** working mechanical extraction. Source coverage and reference closure are checked; a separate proof audit is pending.

"""
readme = replace_once(readme, summary_anchor, new_summary + summary_anchor, "README summary")
readme_path.write_text(readme, encoding="utf-8")

status_path = ROOT / "THEOREM_STATUS.md"; status = status_path.read_text(encoding="utf-8")
status_anchor = "| Regular positive-profile microscopic cycles and sparse entries |"
status_row = "| Boundary laws | **Working mechanical extraction** in `papers/boundary-laws/`. The vanishing-block obstruction, exact top-window total-variation identity, exact one-sided relative defect, birthday transfer, finite bottom-window convergence, terminal leakage theorem, and log-log phase diagram are preserved from the archive. Source coverage and closure pass; a dedicated proof audit is pending. |\n"
status = replace_once(status, status_anchor, status_row + status_anchor, "status table row")
review_anchor = "## Regular-profile audit and repair boundary"
status_section = """## Boundary-laws extraction boundary

The boundary paper is a working mechanical extraction. The selected mathematical blocks are byte-preserved, all internal references close, and no active paper is a proof dependency. The extraction does not audit the exact finite identities, the infinite-product limit, terminal leakage, or the log-log phase diagram.

"""
status = replace_once(status, review_anchor, status_section + review_anchor, "status boundary section")
status_path.write_text(status, encoding="utf-8")

deps_path = ROOT / "DEPENDENCIES.md"; deps = deps_path.read_text(encoding="utf-8")
deps_anchor = "## Regular-profile microscopic-cycle manuscript"
deps_section = """## Boundary-laws extraction

The standalone boundary paper has no proof dependency on another active manuscript. Its internal chain consists of the exponential-race identity, the vanishing-block construction, exact top-window likelihood comparison, finite-volume bottom-window convergence, and the Borel--Cantelli/infinite-product leakage argument. The extraction is byte-preserving and has not yet received a correctness audit.

"""
deps = replace_once(deps, deps_anchor, deps_section + deps_anchor, "dependency section")
deps_path.write_text(deps, encoding="utf-8")

plan_path = ROOT / "notes/migration-plan.md"; plan = plan_path.read_text(encoding="utf-8")
remaining = "The remaining planned thematic destinations are boundary laws; Sukhatme fixed points; endpoint universality; global endpoint fixed-point Poisson approximation; and singular-profile short cycles."
replacement = "The boundary-laws paper is now present as a working mechanical extraction with completeness checks; its adversarial audit is pending. The remaining planned thematic destinations are Sukhatme fixed points; endpoint universality; global endpoint fixed-point Poisson approximation; and singular-profile short cycles."
plan = replace_once(plan, remaining, replacement, "migration remaining list")
plan_path.write_text(plan, encoding="utf-8")

manifest = json.loads((ROOT / "archive/manifest.json").read_text(encoding="utf-8"))["files"]
for rec in manifest:
    if sha(ROOT / rec["path"]) != rec["sha256"]: raise ValueError("Frozen archive changed: " + rec["path"])
subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", "main"], cwd=ROOT, check=True)
head = subprocess.check_output(["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True).strip()
if head != BASE: raise ValueError("Unexpected main head while restoring migration helper")
(ROOT / ".migration/prepare.py").write_bytes(subprocess.check_output(["git", "show", "FETCH_HEAD:.migration/prepare.py"], cwd=ROOT))
print(f"Prepared boundary-laws extraction with {len(rows)} theorem-like environments, {len(labels)} labels, and {len(refs)} reference targets.")
