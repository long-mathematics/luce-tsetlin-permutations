import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
ACTIVE = ROOT / "papers/regular-profile-cycles/regular-profile-cycles.tex"

START_PRELIM_A = r"\subsection{The exponential race}"
END_PRELIM_A = r"\begin{remark}[Hyperplane-walk priorities]"
START_PRELIM_B = r"\subsection{Analytic input}"
END_PRELIM_B = r"\subsection{A permuton-level obstruction}"
START_REGULAR = r"\section{Regular positive profiles: fixed points and short cycles}\label{sec:regular}"
END_REGULAR = r"\section{Macroscopic cycles under uniformly comparable weights}"

MARKERS = [
    ("% BEGIN ARCHIVED BLOCK: exponential-race-and-gumbel-input", "% END ARCHIVED BLOCK: exponential-race-and-gumbel-input", START_PRELIM_A, END_PRELIM_A),
    ("% BEGIN ARCHIVED BLOCK: analytic-input", "% END ARCHIVED BLOCK: analytic-input", START_PRELIM_B, END_PRELIM_B),
    ("% BEGIN ARCHIVED BLOCK: regular-positive-profile-theory", "% END ARCHIVED BLOCK: regular-positive-profile-theory", START_REGULAR, END_REGULAR),
]

def source_block(text, start, end):
    return text[text.index(start):text.index(end, text.index(start))]

def active_block(text, start_marker, end_marker):
    return text.split(start_marker + "\n", 1)[1].split(end_marker, 1)[0]

def strip_repairs(text):
    return re.sub(
        r"\n% BEGIN AUDIT REPAIR [^\n]+\n.*?% END AUDIT REPAIR [^\n]+\n",
        "",
        text,
        flags=re.S,
    )

class RegularProfileExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archive = ARCHIVE.read_text(encoding="utf-8")
        cls.active = ACTIVE.read_text(encoding="utf-8")

    def test_archived_blocks_recovered_after_stripping_repairs(self):
        for sm, em, ss, se in MARKERS:
            with self.subTest(marker=sm):
                self.assertEqual(
                    strip_repairs(active_block(self.active, sm, em)),
                    source_block(self.archive, ss, se),
                )

    def test_label_reference_and_citation_closure(self):
        labels = set(re.findall(r"\\label\{([^}]+)\}", self.active))
        refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", self.active))
        self.assertFalse(refs - labels)
        cites = set()
        for match in re.finditer(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", self.active):
            cites.update(k.strip() for k in match.group(1).split(","))
        bibitems = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", self.active))
        self.assertFalse(cites - bibitems)

    def test_principal_scope_is_unchanged(self):
        required = [
            r"\theta_{n,i}=a_n(f(i/n)+\eps_{n,i})",
            r"\max_{1\le i\le n}|\eps_{n,i}|\to0",
            r"f\in C[0,1]",
            r"0<m_f\le f(x)\le M_f<\infty",
            r"(C_1(\sigma_n),\ldots,C_R(\sigma_n))",
            r"\Rightarrow (Z_1,\ldots,Z_R)",
            r"\lambda_r=\frac1r+O\!\left(\frac{q^r}{r}\right)",
            r"\begin{theorem}[Sparse bulk entry sets]",
            r"\begin{corollary}[Overlaps with deterministic permutations]",
        ]
        for token in required:
            self.assertIn(token, self.active)

    def test_audit_repairs_are_all_present(self):
        for marker in ["1:", "2:", "3A:", "3B:", "4:", "5A:", "5B:", "5C:", "6A:", "6B:", "6C:"]:
            self.assertIn("% BEGIN AUDIT REPAIR " + marker, self.active)
        self.assertIn("Audited current manuscript", self.active)

    def test_catalog_and_status_promoted_without_dependencies(self):
        catalog = json.loads((ROOT / "papers.json").read_text())["documents"]
        doc = next(d for d in catalog if d["id"] == "regular-profile-cycles")
        self.assertEqual(doc["status"], "current-research")
        self.assertEqual(doc.get("dependencies", []), [])
        status = (ROOT / "THEOREM_STATUS.md").read_text()
        self.assertIn("Microscopic Cycles and Sparse Entries for Regular Luce Profiles", status)
        self.assertIn("**Audited current manuscript**", status)
        self.assertIn("regular-profile-repair-record.md", status)

    def test_scope_denials_are_recorded(self):
        status = (ROOT / "THEOREM_STATUS.md").read_text()
        for token in ("arbitrary comparable arrays", "growing cycle lengths", "endpoint-singular profiles", "quantitative total-variation rate"):
            self.assertIn(token, status)

if __name__ == "__main__":
    unittest.main()
