"""Structural guards for spectral PD replacement; not proof verification."""
import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex"
PREDECESSOR = "archive/macroscopic-pd-comparable"


def declaration(text: str, label: str) -> tuple[str, str]:
    pattern = (
        r"\\begin\{(theorem|corollary|lemma|proposition|question|conjecture)\}"
        r"(?:\[[^]]*\])?\s*\\label\{" + re.escape(label) + r"\}"
    )
    match = re.search(pattern, text)
    if match is None:
        raise AssertionError("Missing labeled declaration: " + label)
    kind = match.group(1)
    end = text.index(r"\end{" + kind + "}", match.end())
    return kind, text[match.end():end]


class SpectralPDIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.documents = json.loads((ROOT / "papers.json").read_text())["documents"]
        cls.text = (ROOT / SOURCE).read_text()

    def test_one_canonical_macroscopic_source(self):
        entries = [d for d in self.documents if d["id"] == "macroscopic-pd"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["source"], SOURCE)
        self.assertEqual(entries[0]["pdf"], "output/pdf/spectral-poisson-dirichlet-luce.pdf")
        self.assertEqual(entries[0]["dependencies"], [])
        self.assertEqual(list((ROOT / "papers/macroscopic-pd").glob("*.tex")), [ROOT / SOURCE])
        self.assertFalse((ROOT / "output/pdf/poisson-dirichlet-luce.pdf").exists())

    def test_predecessor_remains_hash_preserved(self):
        records = {
            r["path"]: r["sha256"]
            for r in json.loads((ROOT / "archive/manifest.json").read_text())["files"]
        }
        expected = {
            "poisson-dirichlet-luce.tex": "0fdde5028985c4b639c7679e4f59256fb23e4983119a22bf60ea9d55bfbccdaa",
            "poisson-dirichlet-luce.pdf": "1e1da609aeb2abcb07a264c585165a5c0bd248d4bffb49ae0fab4a44eaa8c03e",
            "EXTRACTION_MAP.md": "15593a1473bb28f1b4f69b806924fbbf4c616ac07795d7a2b50346df6a551533",
        }
        for name, digest in expected.items():
            path = PREDECESSOR + "/" + name
            with self.subTest(path=path):
                self.assertEqual(records[path], digest)
                self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest)
        self.assertTrue(all(not d["source"].startswith(PREDECESSOR) for d in self.documents))

    def test_full_spectral_criterion_and_subsequence_extension(self):
        kind, theorem = declaration(self.text, "thm:main-spectral")
        self.assertEqual(kind, "theorem")
        theorem = " ".join(theorem.split())
        for fragment in (
            r"\nu_n\Rightarrow\nu",
            r"\nu(\{0\})=0",
            r"q(\nu)<1",
            r"\Rightarrow \GEM(1)",
            r"\Rightarrow \PD(1)",
            r"\ell^1",
            r"\Rightarrow\Unif(0,1)",
            "no regularity assumption is imposed on the assignment of rates to labels",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, theorem)
        self.assertEqual(declaration(self.text, "cor:subsequential-spectral")[0], "corollary")
        self.assertEqual(declaration(self.text, "cor:comparable")[0], "corollary")

    def test_proved_boundary_results_and_remaining_question(self):
        for label in ("thm:rv-gap", "thm:dyadic-doubling", "thm:slow-boundary"):
            with self.subTest(label=label):
                self.assertEqual(declaration(self.text, label)[0], "theorem")
        self.assertEqual(declaration(self.text, "q:sharpness")[0], "question")

    def test_conditional_interfaces_and_internal_reference_closure(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.text)
        self.assertEqual(len(labels), len(set(labels)))
        required = {
            "lem:residual-factorization", "prop:uniform-root-fraction",
            "lem:deletion-stability", "eq:root-cdf", "eq:deletion-error",
            "eq:deletion-joint", "eq:uniform-root-main", "cor:comparable",
        }
        self.assertLessEqual(required, set(labels))
        refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", self.text))
        self.assertLessEqual(refs, set(labels))


if __name__ == "__main__":
    unittest.main()
