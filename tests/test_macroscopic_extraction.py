from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex"
ACTIVE = ROOT / "papers/macroscopic-pd/poisson-dirichlet-luce.tex"
MAP = ROOT / "papers/macroscopic-pd/EXTRACTION_MAP.md"
START = r"\section{Macroscopic cycles under uniformly comparable weights}"
ARCHIVE_END = r"\section{Sukhatme fixed points}"
ACTIVE_END = r"\begin{thebibliography}{9}"


def between(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j].rstrip()


def tex_tokens(text: str) -> str:
    """Ignore extraction-only whitespace while preserving every TeX token."""
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    return re.sub(r"\s+", "", text)


def labels(text: str) -> set[str]:
    return set(re.findall(r"\\label\{([^}]+)\}", text))


def refs(text: str) -> set[str]:
    return set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text))


def cites(text: str) -> set[str]:
    return set(re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text))


class MacroscopicExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.old = between(ARCHIVE.read_text(), START, ARCHIVE_END)
        cls.new = between(ACTIVE.read_text(), START, ACTIVE_END)

    def test_complete_section_token_stream_is_preserved(self):
        self.assertEqual(tex_tokens(self.old), tex_tokens(self.new))

    def test_labels_references_and_citations_are_preserved(self):
        self.assertEqual(labels(self.old), labels(self.new))
        self.assertEqual(refs(self.old), refs(self.new))
        self.assertEqual(cites(self.old), cites(self.new))
        self.assertLessEqual(refs(self.new), labels(self.new))
        self.assertEqual(cites(self.new), {"Pitman2006"})

    def test_map_covers_every_label(self):
        mapping = MAP.read_text()
        for label in labels(self.old):
            with self.subTest(label=label):
                self.assertIn(f"`{label}`", mapping)

    def test_status_is_extraction_not_audit(self):
        text = ACTIVE.read_text()
        self.assertIn("Mechanical extraction --- audit pending", text)
        self.assertIn("does not constitute a new proof audit", text)
        self.assertNotIn("total-cycle CLT", self.new)


if __name__ == "__main__":
    unittest.main()
