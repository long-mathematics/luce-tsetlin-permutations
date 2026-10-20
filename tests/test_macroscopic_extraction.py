"""Historical extraction checks for the preserved comparable-rate predecessor."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
PRESERVED = ROOT / "archive/macroscopic-pd-comparable/poisson-dirichlet-luce.tex"
MAP = ROOT / "archive/macroscopic-pd-comparable/EXTRACTION_MAP.md"
AUDIT = ROOT / "audits/macroscopic-pd-proof-audit.md"
REPAIRS = ROOT / "audits/macroscopic-pd-repair-record.md"
START = r"\section{Macroscopic cycles under uniformly comparable weights}"
ARCHIVE_END = r"\section{Sukhatme fixed points}"
PRESERVED_END = r"\begin{thebibliography}{99}"


def between(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j].rstrip()


def labels(text: str) -> set[str]:
    return set(re.findall(r"\\label\{([^}]+)\}", text))


def refs(text: str) -> set[str]:
    return set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text))


def cites(text: str) -> set[str]:
    return set(re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text))


def environment_with_label(text: str, kind: str, label: str) -> str:
    start = text.rfind(rf"\begin{{{kind}}}", 0, text.index(rf"\label{{{label}}}"))
    end = text.index(rf"\end{{{kind}}}", start) + len(rf"\end{{{kind}}}")
    return text[start:end]


class MacroscopicExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.archive_text = ARCHIVE.read_text()
        cls.preserved_text = PRESERVED.read_text()
        cls.old = between(cls.archive_text, START, ARCHIVE_END)
        cls.new = between(cls.preserved_text, START, PRESERVED_END)

    def test_original_labels_and_internal_references_are_preserved(self):
        self.assertEqual(labels(self.old), labels(self.new))
        self.assertEqual(refs(self.old), refs(self.new))
        self.assertLessEqual(refs(self.new), labels(self.new))

    def test_bibliography_extensions_are_only_standard_imports(self):
        self.assertEqual(cites(self.old), {"Pitman2006"})
        self.assertEqual(
            cites(self.preserved_text),
            {"Pitman2006", "Kallenberg2002", "Durrett2019", "Billingsley1999", "Dudley2002"},
        )

    def test_map_covers_every_original_label(self):
        mapping = MAP.read_text()
        for label in labels(self.old):
            with self.subTest(label=label):
                self.assertIn(f"`{label}`", mapping)

    def test_main_theorem_scope_is_preserved(self):
        theorem = environment_with_label(self.preserved_text, "theorem", "thm:macroscopic-pd")
        for fragment in (
            r"\sup_n\frac{\max_i\theta_{n,i}}{\min_i\theta_{n,i}}<\infty",
            r"\Rightarrow\operatorname{PD}(1)",
            r"in $\mathcal S^\downarrow$",
            r"\Rightarrow\operatorname{GEM}(1)",
            r"in $\ell^1$",
            r"\frac{\mathscr L_n(I_n)}n\Rightarrow\operatorname{Unif}(0,1)",
        ):
            self.assertIn(fragment, theorem)
        self.assertIn("independently and uniformly from the current residual", theorem)
        for forbidden in ("rate of convergence", "quenched", "endpoint-singular", "mesoscopic"):
            self.assertNotIn(forbidden, theorem)

    def test_six_audit_repairs_are_present(self):
        required = (
            "The ordered list is \\emph{unlabeled}",
            "C_2\\beta_0\\le\\frac12",
            "At the stopping time there are two cases",
            "the cutoff used at each deletion stage is summarized",
            "If $F:\\ell^1\\to\\mathbb R$ is bounded and Lipschitz",
            "Weak convergence and bounded continuity of the power-sum functional",
            "Kallenberg2002",
            "Durrett2019",
            "Billingsley1999",
            "Dudley2002",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.preserved_text)

    def test_preserved_revision_is_audited_and_records_exist(self):
        self.assertIn("Audited revision --- 11 October 2026", self.preserved_text)
        self.assertNotIn("Mechanical extraction --- audit pending", self.preserved_text)
        self.assertTrue(AUDIT.is_file())
        self.assertTrue(REPAIRS.is_file())
        repairs = REPAIRS.read_text()
        self.assertEqual(repairs.count("**Resolved.**"), 6)

    def test_prohibited_dependencies_are_absent(self):
        section = self.new
        self.assertNotIn("total-cycle CLT", section)
        self.assertNotIn("mesoscopic-cycle theorem", section)


if __name__ == "__main__":
    unittest.main()
