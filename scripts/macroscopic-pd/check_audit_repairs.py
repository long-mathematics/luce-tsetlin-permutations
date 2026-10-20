#!/usr/bin/env python3
"""Check the six audited clarifications in the preserved comparable-rate predecessor."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
PRESERVED = ROOT / "archive/macroscopic-pd-comparable/poisson-dirichlet-luce.tex"
RECORD = ROOT / "audits/macroscopic-pd-repair-record.md"
START = r"\section{Macroscopic cycles under uniformly comparable weights}"
ARCHIVE_END = r"\section{Sukhatme fixed points}"
PRESERVED_END = r"\begin{thebibliography}{99}"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def between(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


def labels(text: str) -> set[str]:
    return set(re.findall(r"\\label\{([^}]+)\}", text))


def refs(text: str) -> set[str]:
    return set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text))


def theorem_with_label(text: str, label: str) -> str:
    marker = rf"\label{{{label}}}"
    i = text.index(marker)
    start = text.rfind(r"\begin{theorem}", 0, i)
    end = text.index(r"\end{theorem}", i) + len(r"\end{theorem}")
    return text[start:end]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args()

    old_text = ARCHIVE.read_text()
    preserved_text = PRESERVED.read_text()
    old = between(old_text, START, ARCHIVE_END)
    preserved = between(preserved_text, START, PRESERVED_END)

    checks: dict[str, object] = {}
    checks["archive_sha256"] = sha(ARCHIVE)
    checks["preserved_sha256"] = sha(PRESERVED)
    checks["labels_preserved"] = labels(old) == labels(preserved)
    checks["references_preserved"] = refs(old) == refs(preserved)
    checks["reference_closure"] = refs(preserved) <= labels(preserved)
    checks["theorem_environment_count"] = len(re.findall(r"\\begin\{(?:theorem|proposition|lemma|corollary)\}", preserved))

    theorem = theorem_with_label(preserved_text, "thm:macroscopic-pd")
    theorem_fragments = [
        r"\sup_n\frac{\max_i\theta_{n,i}}{\min_i\theta_{n,i}}<\infty",
        r"\Rightarrow\operatorname{PD}(1)",
        r"in $\mathcal S^\downarrow$",
        r"\Rightarrow\operatorname{GEM}(1)",
        r"in $\ell^1$",
        r"\frac{\mathscr L_n(I_n)}n\Rightarrow\operatorname{Unif}(0,1)",
        "independently and uniformly from the current residual",
    ]
    checks["theorem_scope_preserved"] = all(x in theorem for x in theorem_fragments)
    checks["no_unreviewed_theorem_strengthening"] = not any(
        x in theorem for x in ("rate of convergence", "quenched", "endpoint-singular", "mesoscopic")
    )

    repairs = {
        "reduced_conditioning": "The ordered list is \\emph{unlabeled}",
        "post_stopping_and_beta": "At the stopping time there are two cases",
        "gem_stage_table": "the cutoff used at each deletion stage is summarized",
        "ell1_and_root_sampling": "If $F:\\ell^1\\to\\mathbb R$ is bounded and Lipschitz",
        "power_sum_wording": "Weak convergence and bounded continuity of the power-sum functional",
        "standard_references": "Kallenberg2002",
    }
    for name, phrase in repairs.items():
        checks[name] = phrase in preserved_text
    checks["all_six_repair_records"] = RECORD.read_text().count("**Resolved.**") == 6

    failed = [k for k, v in checks.items() if isinstance(v, bool) and not v]
    if checks["theorem_environment_count"] != 15:
        failed.append("theorem_environment_count")
    if checks["archive_sha256"] != "c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028":
        failed.append("archive_sha256")
    if failed:
        raise SystemExit("Preserved PD/GEM audit-repair check failed: " + ", ".join(failed))

    result = {
        "schema_version": 1,
        "check": "macroscopic-pd-audit-repairs",
        "checks": checks,
        "status": "pass",
        "scope": "historical predecessor structural consistency check; not formal proof verification",
    }
    if args.output:
        out = ROOT / args.output
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
