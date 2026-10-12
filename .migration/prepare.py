#!/usr/bin/env python3
"""Finalize documentation after the five-paper monolith decomposition."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PARENT = "654a25c0ed0abfa267aee2970fd311544be39866"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, heading: str, next_heading: str, body: str) -> str:
    start = text.index(heading)
    end = text.index(next_heading, start + len(heading))
    return text[:start] + heading + "\n\n" + body.rstrip() + "\n\n" + text[end:]


request_path = ROOT / ".migration/request.json"
request = json.loads(request_path.read_text(encoding="utf-8"))
expected_request = {
    "stage": "integration",
    "task": "monolith-decomposition-status",
    "baseline_commit": PARENT,
}
if request != expected_request:
    raise ValueError("Unexpected decomposition-status request")
if not os.environ.get("GITHUB_REF_NAME", "").startswith("migration/"):
    raise SystemExit("Preparation requires an explicit migration branch")
headers = subprocess.check_output(
    ["git", "cat-file", "-p", "HEAD"], cwd=ROOT, text=True
).split("\n\n", 1)[0].splitlines()
if "parent " + PARENT not in headers:
    raise ValueError("Status request must directly follow the pinned main commit")

# README status reconciliation.
readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
rows = {
    "Boundary Laws for Luce Rankings": ("output/pdf/boundary-laws.pdf", "papers/boundary-laws/boundary-laws.tex"),
    "Sukhatme Fixed Points and the Terminal Poisson Process": ("output/pdf/sukhatme-fixed-points.pdf", "papers/sukhatme-fixed-points/sukhatme-fixed-points.tex"),
    "Endpoint-Regular Fixed-Point Universality": ("output/pdf/endpoint-regular-universality.pdf", "papers/endpoint-regular-universality/endpoint-regular-universality.tex"),
    "Global Endpoint Poisson Approximation": ("output/pdf/global-endpoint-poisson.pdf", "papers/global-endpoint-poisson/global-endpoint-poisson.tex"),
    "Endpoint Short Cycles": ("output/pdf/endpoint-short-cycles.pdf", "papers/endpoint-short-cycles/endpoint-short-cycles.tex"),
}
for title, (pdf, source) in rows.items():
    old = f"| {title} | [PDF]({pdf}) | [Source]({source}) | mechanical extraction; proof audit pending |"
    new = f"| {title} | [PDF]({pdf}) | [Source]({source}) | mechanical extraction; audit passed; repairs pending |"
    readme = replace_once(readme, old, new, f"README row {title}")

monolith_start = readme.index("The **139-page original research draft**")
monolith_end = readme.index("\n\n## Paper summaries", monolith_start)
monolith_text = """The **139-page original research draft** is preserved as [PDF](archive/6178a99/output/pdf/luce-boundary-cycle-laws.pdf) and [LaTeX](archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex). It is an immutable provenance source, not an active monolithic editing target. Every principal theorem-and-proof package has now been assigned to a standalone paper. The regular-profile and PD/GEM papers completed extraction, adversarial audit, and localized repair and are audited current manuscripts. The five remaining thematic papers completed mechanical extraction and independent adversarial audit; every audit found no fatal gap, but each records six localized clarifications that remain deliberately deferred. See the [consolidated migration table](notes/migration-plan.md), theorem-specific audit files under [`audits/`](audits/), and old-label/new-label maps under the corresponding paper directories. No principal theorem remains only in the monolith."""
readme = readme[:monolith_start] + monolith_text + readme[monolith_end:]

status_replacements = {
    "**Status:** working mechanical extraction. Source coverage and reference closure are checked; a separate proof audit is pending.": "**Status:** working mechanical extraction; the adversarial audit found no fatal gap. Six localized clarifications are recorded in the [proof audit](audits/boundary-laws-proof-audit.md) and remain deferred.",
    "**Status:** working mechanical extraction. Source coverage and dependency closure are checked; a separate proof audit is pending.": None,
}
readme = replace_once(
    readme,
    "**Status:** working mechanical extraction. Source coverage and reference closure are checked; a separate proof audit is pending.",
    "**Status:** working mechanical extraction; the adversarial audit found no fatal gap. Six localized clarifications are recorded in the [proof audit](audits/boundary-laws-proof-audit.md) and remain deferred.",
    "boundary summary status",
)
# The remaining four paragraphs share the old wording, so replace them in order.
for audit_file, label in [
    ("sukhatme-fixed-points-proof-audit.md", "Sukhatme"),
    ("endpoint-regular-universality-proof-audit.md", "endpoint regular"),
    ("global-endpoint-poisson-proof-audit.md", "global endpoint"),
    ("endpoint-short-cycles-proof-audit.md", "endpoint short cycles"),
]:
    readme = replace_once(
        readme,
        "**Status:** working mechanical extraction. Source coverage and dependency closure are checked; a separate proof audit is pending.",
        f"**Status:** working mechanical extraction; the adversarial audit found no fatal gap. Six localized clarifications are recorded in the [proof audit](audits/{audit_file}) and remain deferred.",
        f"{label} summary status",
    )
readme_path.write_text(readme, encoding="utf-8")

# Theorem-status reconciliation.
status_path = ROOT / "THEOREM_STATUS.md"
status = status_path.read_text(encoding="utf-8")
status = replace_once(status, "Status date: 11 October 2026.", "Status date: 12 October 2026.", "status date")
status = replace_once(
    status,
    "**Working mechanical extraction** means the archived theorem and proof have been moved into a standalone source with extraction coverage checks, but no new correctness claim is made.",
    "**Working mechanical extraction** means the archived theorem and proof have been moved into a standalone source with extraction coverage checks. A paper may additionally have an audit-passed/repairs-pending status; it is not promoted to audited-current status until those repairs are applied and checked.",
    "status vocabulary",
)
row_map = {
    "| Boundary laws |": "| Boundary laws | **Working mechanical extraction; audit passed, repairs pending** in `papers/boundary-laws/`. The adversarial audit found no fatal gap in the vanishing-block obstruction, exact top-window identities, bottom-window convergence, terminal leakage, or log-log phase diagram. Six localized clarifications are recorded in `audits/boundary-laws-proof-audit.md`; none is applied here. |",
    "| Sukhatme fixed points and terminal Poisson process |": "| Sukhatme fixed points and terminal Poisson process | **Working mechanical extraction; audit passed, repairs pending** in `papers/sukhatme-fixed-points/`. The adversarial audit found no fatal gap in the death-process envelope, one- and multipoint terminal saddles, anisotropic localization, local terminal Poisson process, or fixed factorial moments. Six localized clarifications are recorded and deferred. |",
    "| Endpoint-Regular Fixed-Point Universality |": "| Endpoint-Regular Fixed-Point Universality | **Working mechanical extraction; audit passed, repairs pending** in `papers/endpoint-regular-universality/`. The endpoint fixed-point Poisson process, factorial moments, displacement and tangent laws, multiplicative kernel, and microscopic endpoint permutation all passed the independent audit within their archived scope. Six localized clarifications are recorded and deferred. |",
    "| Global Endpoint Poisson Approximation |": "| Global Endpoint Poisson Approximation | **Working mechanical extraction; audit passed, repairs pending** in `papers/global-endpoint-poisson/`. The independent audit found no fatal gap in the endpoint framework, approximate-Palm Stein argument, rank transposition, quantitative saddle, swap--Palm comparison, two-cycle correction, explicit total-variation rate, or normal corollary. Six localized clarifications are recorded and deferred. |",
    "| Endpoint Short Cycles |": "| Endpoint Short Cycles | **Working mechanical extraction; audit passed, repairs pending** in `papers/endpoint-short-cycles/`. The independent audit found no fatal gap in the source-to-target saddle, anisotropic LLT, global cycle envelope, logarithmic traces, negligible-configuration bounds, mixed factorial moments, or fixed-`L^p` law of large numbers. Six localized clarifications are recorded and deferred. |",
    "| Singular endpoint results in the 139-page draft |": "| Remaining monolith-only material | No principal theorem-and-proof package remains only in the frozen monolith. The remaining monolith-only text is introductory, transitional, concluding, or conjectural exposition; see `notes/migration-plan.md`. |",
}
status_lines = status.splitlines()
seen = set()
for i, line in enumerate(status_lines):
    for prefix, replacement in row_map.items():
        if line.startswith(prefix):
            status_lines[i] = replacement
            seen.add(prefix)
if seen != set(row_map):
    raise ValueError("Missing theorem-status table row(s): " + repr(set(row_map) - seen))
status = "\n".join(status_lines) + ("\n" if status.endswith("\n") else "")

status = replace_section(
    status,
    "## Boundary-laws extraction boundary",
    "## Sukhatme extraction boundary",
    "The selected blocks are byte-preserved, all internal references close, and no active paper is a proof dependency. The adversarial audit checked the exact finite identities, infinite-product limit, terminal leakage, phase diagram, and all endpoint cases and found no fatal gap. Six localized clarification repairs are specified in `audits/boundary-laws-proof-audit.md` and remain deliberately unapplied.",
)
status = replace_section(
    status,
    "## Sukhatme extraction boundary",
    "## Endpoint-Regular Fixed-Point Universality extraction boundary",
    "The exponential/Gumbel input, analytic LLT input, death-process envelope, anisotropic terminal saddle package, local Poisson process, and factorial-moment theorem are byte-preserved and dependency-closed. The independent audit found no fatal gap and records six localized clarifications. The manuscript remains a working extraction until those repairs are applied in a separate focused PR.",
)
status = replace_section(
    status,
    "## Endpoint-Regular Fixed-Point Universality extraction boundary",
    "## Global Endpoint Poisson Approximation extraction boundary",
    "The selected mathematical blocks are byte-preserved and dependency-closed. The adversarial audit checked endpoint regular variation, anisotropic localization, fixed-point factorial moments, displacement and tangent laws, the multiplicative semigroup, and the microscopic endpoint permutation, and found no fatal gap. Six localized clarifications are recorded and deferred.",
)
status = replace_section(
    status,
    "## Global Endpoint Poisson Approximation extraction boundary",
    "## Endpoint Short Cycles extraction boundary",
    "The selected mathematical blocks are byte-preserved and dependency-closed. The adversarial audit checked the Stein normalization, endpoint package, swap likelihood ratio and Palm comparison, two-cycle correction, weighted summation, and final total-variation/normal limits, and found no fatal gap. Six localized clarifications are recorded and deferred.",
)
status = replace_section(
    status,
    "## Endpoint Short Cycles extraction boundary",
    "## Regular-profile audit and repair boundary",
    "The selected mathematical blocks are byte-preserved and dependency-closed. The adversarial audit checked endpoint regularity, source-to-target local limits, mixed localization, forced-deletion envelopes, logarithmic traces, negligible configurations, mixed factorial moments, and fixed-`L^p` convergence, and found no fatal gap. Six localized clarifications are recorded and deferred.",
)
review_start = status.index("## Review records")
formal_start = status.index("Formalization status:", review_start)
review_text = """## Review records

The five final thematic extractions have paired extraction and audit records:

- [Boundary extraction](audits/boundary-laws-extraction.md), [boundary proof audit](audits/boundary-laws-proof-audit.md), and [boundary provenance map](papers/boundary-laws/EXTRACTION_MAP.md);
- [Sukhatme extraction](audits/sukhatme-fixed-points-extraction.md), [Sukhatme proof audit](audits/sukhatme-fixed-points-proof-audit.md), and [Sukhatme provenance map](papers/sukhatme-fixed-points/EXTRACTION_MAP.md);
- [Endpoint-regular extraction](audits/endpoint-regular-universality-extraction.md), [endpoint-regular proof audit](audits/endpoint-regular-universality-proof-audit.md), and [endpoint-regular provenance map](papers/endpoint-regular-universality/EXTRACTION_MAP.md);
- [Global endpoint extraction](audits/global-endpoint-poisson-extraction.md), [global endpoint proof audit](audits/global-endpoint-poisson-proof-audit.md), and [global endpoint provenance map](papers/global-endpoint-poisson/EXTRACTION_MAP.md);
- [Endpoint short-cycle extraction](audits/endpoint-short-cycles-extraction.md), [endpoint short-cycle proof audit](audits/endpoint-short-cycles-proof-audit.md), and [endpoint short-cycle provenance map](papers/endpoint-short-cycles/EXTRACTION_MAP.md).

Earlier records include the [regular-profile extraction](audits/regular-profile-extraction.md), [proof audit](audits/regular-profile-proof-audit.md), and [repair record](audits/regular-profile-repair-record.md); the [PD/GEM extraction](audits/macroscopic-pd-extraction.md), [proof audit](audits/macroscopic-pd-proof-audit.md), and [repair record](audits/macroscopic-pd-repair-record.md); the [total-cycle integration audit](audits/total-cycle-integration.md); the [dependency register](DEPENDENCIES.md); and the [preserved total-cycle proof notes](archive/total-cycle-source-notes/README.md). Original finite result records are provenance; current checks are rerun in CI.

"""
status = status[:review_start] + review_text + status[formal_start:]
status_path.write_text(status, encoding="utf-8")

# Dependency-map reconciliation.
deps_path = ROOT / "DEPENDENCIES.md"
deps = deps_path.read_text(encoding="utf-8")
sections = [
    (
        "## Boundary-laws extraction",
        "## Sukhatme fixed-point extraction",
        "The standalone boundary paper has no proof dependency on another active manuscript. Its internal chain consists of the exponential-race identity, vanishing-block construction, exact top-window likelihood comparison, finite-volume bottom-window convergence, and Borel--Cantelli/infinite-product leakage argument. The extraction is byte-preserving. The adversarial audit found no fatal gap and records six localized clarifications; those repairs remain deferred, so the paper stays a working mechanical extraction.",
    ),
    (
        "## Sukhatme fixed-point extraction",
        "## Endpoint-Regular Fixed-Point Universality extraction",
        "The standalone Sukhatme paper has no active-paper dependency. Its internal chain consists of exponential/Gumbel identities, the fixed-dimensional tilted LLT, death-process product bound, one- and multipoint terminal saddles, anisotropic localization, the separated joint estimate, and factorial-moment summation. The extraction is byte-preserving. The adversarial audit found no fatal gap and records six localized clarifications; repairs remain deferred.",
    ),
    (
        "## Endpoint-Regular Fixed-Point Universality extraction",
        "## Global Endpoint Poisson Approximation extraction",
        "The standalone endpoint-universality paper is self-contained: exponential/Gumbel and lattice-LLT inputs, the shared anisotropic Fourier/tilting toolkit, regularly varying endpoint sums, endpoint saddle/localization, factorial moments, tangent measure, kernel semigroup, and microscopic limit are internal. The extraction is byte-preserving. The independent audit found no fatal gap and records six localized clarifications; repairs remain deferred.",
    ),
    (
        "## Global Endpoint Poisson Approximation extraction",
        "## Endpoint Short Cycles extraction",
        "The standalone global endpoint paper includes the complete endpoint-regular framework and then the approximate-Palm Stein argument, exact swap likelihood ratio, quantitative one-dimensional saddle, swap--Palm comparison, and two-cycle summability. It has no active-paper dependency and is byte-preserving. The independent audit found no fatal gap and records six localized clarifications; repairs remain deferred.",
    ),
    (
        "## Endpoint Short Cycles extraction",
        "## Regular-profile microscopic-cycle manuscript",
        "The standalone endpoint-short-cycle paper includes the endpoint-regular framework and the full source-to-target saddle, scheduled-deletion envelope, multiplicative trace, and factorial-moment machinery. It has no active-paper dependency and is byte-preserving. The independent audit found no fatal gap and records six localized clarifications; repairs remain deferred.",
    ),
]
for heading, next_heading, body in sections:
    deps = replace_section(deps, heading, next_heading, body)
deps_path.write_text(deps, encoding="utf-8")

# Consolidated migration plan.
plan_path = ROOT / "notes/migration-plan.md"
plan_path.write_text("""# Staged migration

Status date: 12 October 2026.

## Initial reviewed stages

1. **Foundation.** Establish the manuscript catalog, theorem-status and dependency maps, deterministic builds, CI, preservation rules, and audit conventions.
2. **Preservation import.** Pin upstream commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`; preserve the original Luce sources, PDFs, and historical audits byte-for-byte; create active focused copies without changing the frozen archive.
3. **Total-cycle integration.** Make the quantitative switching interface explicit, incorporate the functional audit clarifications, and integrate the total-cycle Poisson, Berry--Esseen, and lattice-Edgeworth work while preserving the source proof notes and finite checks.
4. **Macroscopic PD/GEM extraction, audit, and repair.** Mechanically extract the macroscopic theorem package, audit it independently, and apply only the six localized clarifications approved by that audit.
5. **Regular positive-profile extraction, audit, and repair.** Mechanically extract the microscopic-cycle, trace, sparse-entry, and overlap package, audit it independently, and apply only the six localized clarifications approved by that audit.
6. **Remaining five-paper decomposition.** Extract and independently audit Boundary Laws, Sukhatme Fixed Points, Endpoint-Regular Fixed-Point Universality, Global Endpoint Poisson Approximation, and Endpoint Short Cycles. In accordance with the requested workflow, record but do not apply the audit repairs in this stage.

The original `nonuniform-random-permutations` repository points here as the canonical editing location for the Luce/Tsetlin manuscript series.

## Consolidated monolith-decomposition status

| Paper | Extracted? | Completeness checked? | Audit verdict | Repairs required? | Promotion status | Active-paper dependencies | Remaining monolith-only theorem material? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Boundary Laws for Luce Rankings | Yes | Yes; selected blocks are byte-preserved, labels/references close, deterministic PDF and regression checks pass | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Sukhatme Fixed Points and the Terminal Poisson Process | Yes | Yes; complete saddle, localization, point-process, and factorial-moment package preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Endpoint-Regular Fixed-Point Universality | Yes | Yes; endpoint framework, fixed-point laws, tangent kernel, and microscopic limit preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Global Endpoint Poisson Approximation | Yes | Yes; endpoint framework, Palm/Stein coupling, swap law, quantitative saddle, and two-cycle package preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Endpoint Short Cycles | Yes | Yes; point-constraint saddle, global envelope, trace, and factorial-moment package preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Microscopic Cycles and Sparse Entries for Regular Luce Profiles | Yes | Yes | Passed; no fatal gap | Six localized clarifications were applied and regression-checked | Audited current manuscript | None | None |
| Poisson--Dirichlet Universality for Luce Permutations | Yes | Yes | Passed; no fatal gap | Six localized clarifications were applied and regression-checked | Audited current manuscript | None | None |

The five papers processed in the final decomposition stage deliberately remain below audited-current status because this orchestration prompt prohibited applying repairs. Their audit reports are the specifications for later focused repair PRs.

## Remaining material in the frozen monolith

No principal theorem-and-proof package now exists only in the 139-page source. The material intentionally retained only in the frozen monolith consists of:

- the original introduction, scope discussion, and conventions;
- the concluding theorem map and proof-mechanism overview;
- the historical open-problem and additional-conjecture sections;
- transitional or duplicated exposition connecting theorem packages that now live in separate papers.

These sections may later be distilled into repository documentation or updated open-problem notes, but they are not additional extraction targets. The frozen monolith remains the immutable provenance source under `archive/6178a99/`; active thematic papers live under `papers/` and must not be maintained in duplicate.

## Next controlled stage

Any further mathematical editing of the five newly extracted papers should occur one paper at a time through a focused repair PR that implements exactly the localized clarifications in its audit report. Such repair PRs must preserve the archived theorem scope and must not introduce an unreviewed strengthening.

## Integration record

The foundation, preservation import, total-cycle integration, PD/GEM extraction, and regular-profile extraction passed their separate validation workflows. Each of the five final thematic extractions has a standalone source, deterministic PDF, provenance map, extraction record, permanent archive-preservation test, and independent audit report. All audits found no fatal gap. No frozen archive byte was changed during the decomposition.
""", encoding="utf-8")

# Add a regression test for the consolidated documentation state.
test_path = ROOT / "tests/test_repository.py"
test = test_path.read_text(encoding="utf-8")
anchor = "    def test_historical_candidate_is_not_dependency(self):\n"
method = """    def test_monolith_decomposition_status(self):
        plan = (ROOT/'notes/migration-plan.md').read_text()
        status = (ROOT/'THEOREM_STATUS.md').read_text()
        papers = [
            'Boundary Laws for Luce Rankings',
            'Sukhatme Fixed Points and the Terminal Poisson Process',
            'Endpoint-Regular Fixed-Point Universality',
            'Global Endpoint Poisson Approximation',
            'Endpoint Short Cycles',
        ]
        audits = [
            'boundary-laws-proof-audit.md',
            'sukhatme-fixed-points-proof-audit.md',
            'endpoint-regular-universality-proof-audit.md',
            'global-endpoint-poisson-proof-audit.md',
            'endpoint-short-cycles-proof-audit.md',
        ]
        for paper in papers:
            self.assertIn('| '+paper+' | Yes |', plan)
        for audit in audits:
            self.assertTrue((ROOT/'audits'/audit).is_file())
        self.assertIn('No principal theorem-and-proof package now exists only', plan)
        self.assertEqual(status.count('audit passed, repairs pending'), 5)

"""
test = replace_once(test, anchor, method + anchor, "repository test insertion")
test_path.write_text(test, encoding="utf-8")

# Preserve the frozen archive exactly.
manifest = json.loads((ROOT / "archive/manifest.json").read_text(encoding="utf-8"))["files"]
for rec in manifest:
    path = ROOT / rec["path"]
    if not path.is_file():
        raise ValueError("Missing frozen archive file: " + rec["path"])
    import hashlib
    if hashlib.sha256(path.read_bytes()).hexdigest() != rec["sha256"]:
        raise ValueError("Frozen archive changed: " + rec["path"])

# Restore the canonical migration helper and remove the one-time request.
baseline_prepare = subprocess.check_output(
    ["git", "show", f"{PARENT}:.migration/prepare.py"], cwd=ROOT
)
(ROOT / ".migration/prepare.py").write_bytes(baseline_prepare)
request_path.unlink()
print("Reconciled all five extraction/audit statuses; frozen archive unchanged.")
