#!/usr/bin/env python3
"""Mechanically extract the regular-profile microscopic-cycle paper."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "fab8f0150e81ade0458bebed442f044141c2d2eb"
ARCHIVE_REL = "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
ARCHIVE_SHA256 = "c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028"
ACTIVE_REL = "papers/regular-profile-cycles/regular-profile-cycles.tex"
PDF_REL = "output/pdf/regular-profile-cycles.pdf"

START_PRELIM_A = r"\subsection{The exponential race}"
END_PRELIM_A = r"\begin{remark}[Hyperplane-walk priorities]"
START_PRELIM_B = r"\subsection{Analytic input}"
END_PRELIM_B = r"\subsection{A permuton-level obstruction}"
START_REGULAR = r"\section{Regular positive profiles: fixed points and short cycles}\label{sec:regular}"
END_REGULAR = r"\section{Macroscopic cycles under uniformly comparable weights}"

MARK_PRELIM_A_START = "% BEGIN ARCHIVED BLOCK: exponential-race-and-gumbel-input"
MARK_PRELIM_A_END = "% END ARCHIVED BLOCK: exponential-race-and-gumbel-input"
MARK_PRELIM_B_START = "% BEGIN ARCHIVED BLOCK: analytic-input"
MARK_PRELIM_B_END = "% END ARCHIVED BLOCK: analytic-input"
MARK_REGULAR_START = "% BEGIN ARCHIVED BLOCK: regular-positive-profile-theory"
MARK_REGULAR_END = "% END ARCHIVED BLOCK: regular-positive-profile-theory"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def block(text: str, start: str, end: str) -> tuple[str, int, int]:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j], line_number(text, i), line_number(text, j)


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def replace_once(text: str, old: str, new: str, name: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected one {name} anchor, found {text.count(old)}")
    return text.replace(old, new, 1)


request = json.loads((ROOT / ".migration/request.json").read_text(encoding="utf-8"))
if request.get("stage") != "integration" or request.get("task") != "regular-profile-extraction":
    raise SystemExit("Unexpected migration request")
if request.get("baseline_commit") != BASELINE:
    raise ValueError("Unexpected extraction baseline")
if not os.environ.get("GITHUB_REF_NAME", "").startswith("migration/"):
    raise SystemExit("Preparation requires an explicit migration branch")
REQUEST_PARENT = "264386c18d0b9f9aefbf882b214fe02d5ad86f24"
headers = subprocess.check_output(["git", "cat-file", "-p", "HEAD"], cwd=ROOT, text=True).split("\n\n", 1)[0].splitlines()
if "parent " + REQUEST_PARENT not in headers:
    raise ValueError("Unexpected extraction request parent")

archive_path = ROOT / ARCHIVE_REL
if sha(archive_path) != ARCHIVE_SHA256:
    raise ValueError("Frozen monolith source hash mismatch")
source = archive_path.read_text(encoding="utf-8")

prelim_a, prelim_a_first, prelim_a_after = block(source, START_PRELIM_A, END_PRELIM_A)
prelim_b, prelim_b_first, prelim_b_after = block(source, START_PRELIM_B, END_PRELIM_B)
regular, regular_first, regular_after = block(source, START_REGULAR, END_REGULAR)

# The source line ranges are pinned as a second defense against marker drift.
if (prelim_a_first, prelim_b_first, regular_first, regular_after) != (224, 353, 865, 2199):
    raise ValueError(
        "Unexpected source ranges: "
        + repr((prelim_a_first, prelim_b_first, regular_first, regular_after))
    )

selected = prelim_a + prelim_b + regular
labels = set(re.findall(r"\\label\{([^}]+)\}", selected))
refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", selected))
missing_refs = sorted(refs - labels)
if missing_refs:
    raise ValueError("Extraction has external label dependencies: " + ", ".join(missing_refs))

citation_keys: list[str] = []
for match in re.finditer(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", selected):
    for key in match.group(1).split(","):
        key = key.strip()
        if key and key not in citation_keys:
            citation_keys.append(key)

bib_start = source.index(r"\begin{thebibliography}")
bib_end = source.index(r"\end{thebibliography}", bib_start)
bib_body = source[bib_start:bib_end]
bib_matches = list(
    re.finditer(r"(?m)^\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bib_body)
)
bib_entries: dict[str, str] = {}
bib_order: list[str] = []
for pos, match in enumerate(bib_matches):
    stop = bib_matches[pos + 1].start() if pos + 1 < len(bib_matches) else len(bib_body)
    key = match.group(1)
    bib_entries[key] = bib_body[match.start():stop].rstrip() + "\n"
    bib_order.append(key)
missing_bib = [key for key in citation_keys if key not in bib_entries]
if missing_bib:
    raise ValueError("Missing bibliography entries: " + ", ".join(missing_bib))
selected_bibliography = "\n".join(
    bib_entries[key].rstrip() for key in bib_order if key in citation_keys
)

preamble = r"""\documentclass[11pt]{article}

\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{mathrsfs}

\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  citecolor=blue,
  urlcolor=blue,
  hypertexnames=false,
  pdftitle={Microscopic Cycles and Sparse Entries for Regular Luce Profiles},
  pdfauthor={Christopher D. Long}
}

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

\title{Microscopic Cycles and Sparse Entries for Regular Luce Profiles}
\author{Christopher D. Long}
\date{Mechanical extraction --- proof audit pending}

\begin{document}
\maketitle

\begin{abstract}
Let a Luce permutation be generated by independent exponential clocks with
rates
\[
 \theta_{n,i}=a_n\{f(i/n)+\varepsilon_{n,i}\},
 \qquad \max_i|\varepsilon_{n,i}|\longrightarrow0,
\]
where \(f\) is continuous and bounded above and below by positive constants.
This manuscript proves joint independent Poisson limits for every fixed vector
of cycle counts, identifies their means as traces of the microscopic Luce
kernel, and proves exponential convergence of those means to the uniform
values \(1/r\).  The same local-entry theory yields fixed-width diagonal-band
laws, sparse-entry Poisson limits, thin-graph laws, and overlap limits with
deterministic permutations.  The proof includes the separated bulk estimate
and the endpoint, collision, and target-crowding envelopes needed to sum fixed
factorial moments globally.
\end{abstract}

\tableofcontents

\section{Status and provenance}

This standalone source is a mechanical extraction from the frozen
139-page manuscript at repository commit
\texttt{6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0}.  The mathematical text
between the archival sentinels below is copied byte-for-byte from the frozen
source.  Only the standalone preamble, abstract, this provenance notice,
section wrapper, and selected bibliography have been added.

The extraction preserves the profile hypothesis, all equality and limit
statements, every endpoint and collision envelope used by the factorial-moment
arguments, and all internal labels and references.  It does not audit,
strengthen, or otherwise change the proof.  Its mathematical status remains
that of the archived draft until a separate adversarial audit is completed.

\section{Preliminaries}

"""

active = (
    preamble
    + MARK_PRELIM_A_START + "\n"
    + prelim_a
    + MARK_PRELIM_A_END + "\n\n"
    + MARK_PRELIM_B_START + "\n"
    + prelim_b
    + MARK_PRELIM_B_END + "\n\n"
    + MARK_REGULAR_START + "\n"
    + regular
    + MARK_REGULAR_END + "\n\n"
    + "\\begin{thebibliography}{99}\n\n"
    + selected_bibliography
    + "\n\n\\end{thebibliography}\n\n\\end{document}\n"
)

active_path = ROOT / ACTIVE_REL
if active_path.exists():
    raise ValueError("Active extraction target already exists")
write(ACTIVE_REL, active)

# Recheck exact byte preservation of the three archived blocks.
active_text = active_path.read_text(encoding="utf-8")
for start_mark, end_mark, expected in [
    (MARK_PRELIM_A_START, MARK_PRELIM_A_END, prelim_a),
    (MARK_PRELIM_B_START, MARK_PRELIM_B_END, prelim_b),
    (MARK_REGULAR_START, MARK_REGULAR_END, regular),
]:
    observed = active_text.split(start_mark + "\n", 1)[1].split(end_mark, 1)[0]
    if observed != expected:
        raise ValueError("Active extraction is not byte-preserving: " + start_mark)

# Build a theorem/lemma provenance map.
theorem_rows: list[tuple[str, str, str, int, int]] = []
env_pattern = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary)\}"
    r"(?:\[([^\]]+)\])?"
)
for match in env_pattern.finditer(selected):
    env = match.group(1)
    title = (match.group(2) or "").replace("|", r"\|")
    end_marker = "\\end{" + env + "}"
    end = selected.find(end_marker, match.end())
    if end < 0:
        raise ValueError("Unclosed theorem environment")
    segment = selected[match.start():end]
    label_match = re.search(r"\\label\{([^}]+)\}", segment)
    label = label_match.group(1) if label_match else "(unlabeled)"
    signature = match.group(0)
    if label != "(unlabeled)":
        source_offset = source.index(r"\label{" + label + "}")
        active_offset = active.index(r"\label{" + label + "}")
    else:
        source_offset = source.index(signature)
        active_offset = active.index(signature)
    theorem_rows.append(
        (
            env.title(),
            title or "—",
            label,
            line_number(source, source_offset),
            line_number(active, active_offset),
        )
    )

range_rows = [
    ("Exponential race and Gumbel input", prelim_a_first, prelim_a_after - 1, MARK_PRELIM_A_START),
    ("Analytic input", prelim_b_first, prelim_b_after - 1, MARK_PRELIM_B_START),
    ("Regular-profile theory", regular_first, regular_after - 1, MARK_REGULAR_START),
]

map_lines = [
    "# Regular-profile extraction map",
    "",
    "Frozen source:",
    f"`{ARCHIVE_REL}`",
    "",
    f"Frozen source SHA-256: `{ARCHIVE_SHA256}`.",
    "",
    "The three mathematical blocks are copied byte-for-byte. The active paper adds only a standalone preamble, abstract, provenance notice, section wrapper, and the bibliography entries actually cited by the extracted blocks.",
    "",
    "## Source ranges",
    "",
    "| Block | Archived lines | Active sentinel |",
    "| --- | ---: | --- |",
]
for name, first, last, marker in range_rows:
    map_lines.append(f"| {name} | {first}--{last} | `{marker}` |")
map_lines += [
    "",
    "## Theorem and lemma provenance",
    "",
    "Labels are intentionally unchanged, so every old label is also the new label.",
    "",
    "| Environment | Title | Old label = new label | Archived line | Active line |",
    "| --- | --- | --- | ---: | ---: |",
]
for env, title, label, old_line, new_line in theorem_rows:
    map_lines.append(f"| {env} | {title} | `{label}` | {old_line} | {new_line} |")
map_lines += [
    "",
    "## Closure checks",
    "",
    f"- theorem/proposition/lemma/corollary environments: **{len(theorem_rows)}**;",
    f"- labels: **{len(labels)}**;",
    f"- distinct internal reference targets: **{len(refs)}**;",
    f"- cited bibliography keys: **{len(citation_keys)}**;",
    "- unresolved internal references: **0**;",
    "- omitted proof dependencies on the top-window, bottom-window, macroscopic, mesoscopic, order, or total-cycle papers: **0**.",
    "",
    "This is a provenance and completeness map, not a correctness audit.",
]
write("papers/regular-profile-cycles/EXTRACTION_MAP.md", "\n".join(map_lines) + "\n")

active_hash = sha(active_path)
record = {
    "schema_version": 1,
    "stage": "regular-profile-extraction",
    "baseline_commit": BASELINE,
    "archive_source": ARCHIVE_REL,
    "archive_source_sha256": ARCHIVE_SHA256,
    "active_source": ACTIVE_REL,
    "active_source_sha256": active_hash,
    "source_ranges": [
        {"name": name, "first_line": first, "last_line": last, "sentinel": marker}
        for name, first, last, marker in range_rows
    ],
    "theorem_environments": len(theorem_rows),
    "labels": len(labels),
    "reference_targets": len(refs),
    "citation_keys": citation_keys,
    "proof_status": "mechanical extraction; adversarial audit pending",
}
write("notes/regular-profile-extraction-record.json", json.dumps(record, indent=2) + "\n")

audit = f"""# Mechanical extraction record: regular-profile microscopic cycles

Date: 11 October 2026.

## Scope

This record covers only the mechanical extraction of the regular positive-profile
microscopic-cycle and sparse-entry theory from the frozen 139-page manuscript.
It is not a mathematical proof audit, novelty review, or formal verification.

## Frozen source

- source: `{ARCHIVE_REL}`;
- pinned repository commit: `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`;
- source SHA-256: `{ARCHIVE_SHA256}`.

The active source is `{ACTIVE_REL}` with SHA-256 `{active_hash}` before PDF
generation.

## Extracted material

The extraction contains three byte-preserved blocks:

1. exponential-race and Gumbel threshold input, archived lines
   {prelim_a_first}--{prelim_a_after - 1};
2. Bernoulli concentration and the uniform tilted lattice local limit theorem,
   archived lines {prelim_b_first}--{prelim_b_after - 1};
3. the complete regular positive-profile section, archived lines
   {regular_first}--{regular_after - 1}.

The third block contains the separated bulk local estimate, endpoint and
collision domination, target-crowding estimates, factorial-moment summation,
long-trace universality, diagonal-band laws, sparse-entry laws, thin-graph
corollaries, deterministic-permutation overlaps, and the transverse-curve
corollary.

## Completeness checks

- all {len(theorem_rows)} theorem-like environments in the selected blocks are
  present;
- all {len(labels)} labels and all {len(refs)} distinct reference targets are
  present;
- every cited key has its original bibliography entry;
- the three active mathematical blocks compare byte-for-byte with the frozen
  source;
- no active manuscript is imported as a proof dependency;
- no statement from the macroscopic, mesoscopic, order, or total-cycle papers
  is used.

The detailed old-label/new-label map is
`papers/regular-profile-cycles/EXTRACTION_MAP.md`.

## Status boundary

The extraction does not assess the correctness or optimality of the separated
local estimate, endpoint/collision envelopes, improper trace limits, factorial
moment argument, total-variation conclusion for fixed cycle vectors, sparse
entry theorem, or overlap laws. It does not alter a hypothesis, equality,
limit, topology, or proof step. A separate adversarial audit is required
before promotion from working mechanical extraction.
"""
write("audits/regular-profile-extraction.md", audit)

test_source = rf"""import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "{ARCHIVE_REL}"
ACTIVE = ROOT / "{ACTIVE_REL}"

START_PRELIM_A = r"{START_PRELIM_A}"
END_PRELIM_A = r"{END_PRELIM_A}"
START_PRELIM_B = r"{START_PRELIM_B}"
END_PRELIM_B = r"{END_PRELIM_B}"
START_REGULAR = r"{START_REGULAR}"
END_REGULAR = r"{END_REGULAR}"

MARKERS = [
    ("{MARK_PRELIM_A_START}", "{MARK_PRELIM_A_END}", START_PRELIM_A, END_PRELIM_A),
    ("{MARK_PRELIM_B_START}", "{MARK_PRELIM_B_END}", START_PRELIM_B, END_PRELIM_B),
    ("{MARK_REGULAR_START}", "{MARK_REGULAR_END}", START_REGULAR, END_REGULAR),
]


def source_block(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


def active_block(text: str, start_marker: str, end_marker: str) -> str:
    return text.split(start_marker + "\n", 1)[1].split(end_marker, 1)[0]


class RegularProfileExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archive = ARCHIVE.read_text(encoding="utf-8")
        cls.active = ACTIVE.read_text(encoding="utf-8")

    def test_mathematical_blocks_are_byte_preserved(self):
        for start_marker, end_marker, source_start, source_end in MARKERS:
            with self.subTest(start_marker=start_marker):
                self.assertEqual(
                    active_block(self.active, start_marker, end_marker),
                    source_block(self.archive, source_start, source_end),
                )

    def test_label_reference_and_citation_closure(self):
        labels = set(re.findall(r"\\label\{{([^}}]+)\}}", self.active))
        refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{{([^}}]+)\}}", self.active))
        self.assertFalse(refs - labels)
        cites = set()
        for match in re.finditer(r"\\cite(?:\[[^\]]*\])*\{{([^}}]+)\}}", self.active):
            cites.update(k.strip() for k in match.group(1).split(","))
        bibitems = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{{([^}}]+)\}}", self.active))
        self.assertFalse(cites - bibitems)

    def test_principal_scope_is_unchanged(self):
        required = [
            r"\theta_{{n,i}}=a_n(f(i/n)+\eps_{{n,i}})",
            r"\max_{{1\le i\le n}}|\eps_{{n,i}}|\to0",
            r"f\in C[0,1]",
            r"0<m_f\le f(x)\le M_f<\infty",
            r"(C_1(\sigma_n),\ldots,C_R(\sigma_n))",
            r"\Rightarrow (Z_1,\ldots,Z_R)",
            r"\lambda_r=\frac1r+O_f\!\left(\frac{{q^r}}r\right)",
            r"\begin{{theorem}}[Sparse bulk entry sets]",
            r"\begin{{corollary}}[Overlaps with deterministic permutations]",
        ]
        for token in required:
            self.assertIn(token, self.active)

    def test_catalog_and_status_keep_extraction_working(self):
        catalog = json.loads((ROOT / "papers.json").read_text())["documents"]
        doc = next(d for d in catalog if d["id"] == "regular-profile-cycles")
        self.assertEqual(doc["status"], "working")
        self.assertEqual(doc.get("dependencies", []), [])
        status = (ROOT / "THEOREM_STATUS.md").read_text()
        self.assertIn("Working mechanical extraction", status)
        self.assertIn("regular-profile-cycles", status)
        self.assertIn("proof audit pending", status)

    def test_no_unreviewed_strengthening_markers(self):
        provenance = self.active.split("{MARK_PRELIM_A_START}", 1)[0]
        self.assertIn("does not audit", provenance)
        self.assertNotIn("audited current manuscript", provenance.lower())
        prohibited = [
            "uniformly comparable triangular arrays",
            "growing cycle lengths",
            "quantitative total variation rate",
            "quenched arbitrary-deletion",
        ]
        for phrase in prohibited:
            self.assertNotIn(phrase, provenance.lower())


if __name__ == "__main__":
    unittest.main()
"""
write("tests/test_regular_profile_extraction.py", test_source)

# Update the document catalog.
catalog_path = ROOT / "papers.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
if any(doc["id"] == "regular-profile-cycles" for doc in catalog["documents"]):
    raise ValueError("regular-profile-cycles already registered")
new_doc = {
    "id": "regular-profile-cycles",
    "title": "Microscopic Cycles and Sparse Entries for Regular Luce Profiles",
    "source": ACTIVE_REL,
    "pdf": PDF_REL,
    "status": "working",
    "dependencies": [],
}
insert_at = next(
    (i for i, doc in enumerate(catalog["documents"]) if doc["id"] == "macroscopic-pd"),
    len(catalog["documents"]),
)
catalog["documents"].insert(insert_at, new_doc)
catalog_path.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")

# Update README.
readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
row_anchor = "| Poisson--Dirichlet Universality for Luce Permutations | [PDF](output/pdf/poisson-dirichlet-luce.pdf) | [Source](papers/macroscopic-pd/poisson-dirichlet-luce.tex) | audited current manuscript |"
new_row = "| Microscopic Cycles and Sparse Entries for Regular Luce Profiles | [PDF](output/pdf/regular-profile-cycles.pdf) | [Source](papers/regular-profile-cycles/regular-profile-cycles.tex) | mechanical extraction; proof audit pending |"
readme = replace_once(readme, row_anchor, new_row + "\n" + row_anchor, "README paper row")
paragraph_anchor = "The **139-page original research draft** is preserved as [PDF](archive/6178a99/output/pdf/luce-boundary-cycle-laws.pdf) and [LaTeX](archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex). It is not an active monolithic editing target."
paragraph_replacement = paragraph_anchor + " The regular positive-profile microscopic-cycle and sparse-entry theory is now available as a byte-preserving standalone working extraction, with its [provenance map](papers/regular-profile-cycles/EXTRACTION_MAP.md) and [extraction record](audits/regular-profile-extraction.md); its proof status has not been upgraded and a dedicated audit remains pending."
readme = replace_once(readme, paragraph_anchor, paragraph_replacement, "README monolith paragraph")
readme_path.write_text(readme, encoding="utf-8")

# Update theorem status.
status_path = ROOT / "THEOREM_STATUS.md"
status = status_path.read_text(encoding="utf-8")
status_anchor = "| Macroscopic PD/GEM theorem | **Audited current manuscript**"
new_status_row = "| Regular positive-profile microscopic cycles and sparse entries | **Working mechanical extraction** in `papers/regular-profile-cycles/`. The exact sampled-profile hypothesis, fixed-vector independent Poisson limits, trace means, long-trace asymptotic, diagonal-band laws, sparse-entry theorem, thin-graph laws, and deterministic-overlap conclusions are preserved from the archive. The separated bulk estimate and all endpoint, collision, and target-crowding envelopes used by the proof are internal. A dedicated proof audit is pending; no status upgrade is asserted. |\n"
if status.count(status_anchor) != 1:
    raise ValueError("THEOREM_STATUS row anchor not unique")
status = status.replace(status_anchor, new_status_row + status_anchor, 1)
section_anchor = "## Macroscopic audit and repair boundary"
new_section = """## Regular-profile extraction boundary

The standalone regular-profile paper is byte-preserving across three source
blocks: the exponential/Gumbel input, the analytic Bernoulli and lattice-LLT
input, and the complete regular positive-profile section. All model-specific
lemmas used by the fixed-cycle and sparse-entry results are internal, and the
catalog records no active-paper dependency. The extraction checks coverage,
reference closure, theorem scope, and archive immutability only. It does not
audit the multivariate local limit argument, endpoint/collision domination,
improper trace passage, factorial-moment summation, or sparse-entry and overlap
applications.

"""
status = replace_once(status, section_anchor, new_section + section_anchor, "THEOREM_STATUS section")
review_anchor = "[Total-cycle integration audit](audits/total-cycle-integration.md),"
status = replace_once(
    status,
    review_anchor,
    "[Regular-profile extraction record](audits/regular-profile-extraction.md), [regular-profile provenance map](papers/regular-profile-cycles/EXTRACTION_MAP.md), "
    + review_anchor,
    "THEOREM_STATUS review records",
)
status_path.write_text(status, encoding="utf-8")

# Update dependencies.
deps_path = ROOT / "DEPENDENCIES.md"
deps = deps_path.read_text(encoding="utf-8")
deps_anchor = "## Macroscopic PD/GEM extraction"
deps_section = """## Regular-profile microscopic-cycle extraction

The standalone paper `papers/regular-profile-cycles/regular-profile-cycles.tex`
mechanically extracts the complete regular positive-profile theory together
with the two indispensable preliminary blocks. It has no proof dependency on
another active manuscript in `papers.json` and does not use the macroscopic,
mesoscopic, order, or total-cycle theorems.

Its internal proof chain, preserved from the archive, is:

1. exponential-race and Gumbel threshold identities;
2. Bernoulli point-probability/Bernstein bounds and the fixed-dimensional
   tilted lattice local limit theorem;
3. regular saddle geometry, cumulative-count local limits, and off-saddle
   exclusion;
4. the separated bulk multipoint estimate;
5. endpoint, collision, and target-crowding envelopes;
6. fixed-order factorial-moment summation for short cycles;
7. bistochasticity and exponential long-trace universality;
8. diagonal-band, sparse-entry, thin-graph, and deterministic-overlap
   consequences.

The cited external literature supplies the identified Luce permuton density,
standard Bernoulli concentration/local-limit estimates, and background
permutation-limit facts. Every model-specific estimate used in the theorem
statements is included in the standalone source. The extraction map records
all moved theorem and lemma labels. No correctness audit or strengthening is
part of this stage.

"""
deps = replace_once(deps, deps_anchor, deps_section + deps_anchor, "DEPENDENCIES section")
deps_path.write_text(deps, encoding="utf-8")

# Update migration plan.
plan_path = ROOT / "notes/migration-plan.md"
plan = plan_path.read_text(encoding="utf-8")
stage_anchor = "4. Macroscopic PD/GEM extraction and audit: mechanically extract"
stage_end = "The original repository has now been reconciled"
idx = plan.index(stage_anchor)
end = plan.index("\n\n" + stage_end, idx)
stages = plan[idx:end]
if "5. Regular positive-profile extraction" not in stages:
    stages += (
        "\n5. Regular positive-profile extraction: mechanically extract the complete "
        "microscopic-cycle, long-trace, diagonal-band, sparse-entry, thin-graph, and "
        "overlap theory together with its indispensable preliminary and endpoint/collision "
        "bounds. Preserve proof status pending a separate audit."
    )
plan = plan[:idx] + stages + plan[end:]
current = "With the PD/GEM extraction, audit, and localized repair stage complete, the regular-profile microscopic-cycle/sparse-entry paper is next."
replacement = "The regular-profile microscopic-cycle/sparse-entry paper is now present as a working mechanical extraction with byte-preserving coverage and provenance checks. Its separate adversarial proof audit is the next stage; no theorem has been promoted by the extraction."
plan = replace_once(plan, current, replacement, "migration current-stage sentence")
plan_path.write_text(plan, encoding="utf-8")

# Restore the baseline migration helper so it does not appear in the PR.
baseline_prepare = subprocess.check_output(
    ["git", "show", f"{BASELINE}:.migration/prepare.py"], cwd=ROOT
)
(ROOT / ".migration/prepare.py").write_bytes(baseline_prepare)

print(
    "Prepared regular-profile extraction: "
    f"{len(theorem_rows)} theorem environments, {len(labels)} labels, "
    f"{len(refs)} reference targets, {len(citation_keys)} bibliography keys."
)
