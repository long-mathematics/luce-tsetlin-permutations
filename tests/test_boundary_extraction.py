from pathlib import Path
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
        for token in [r"\|P_k-Q_k\|_{\TV}", r"d_\infty^+(P_k,Q_k)", r"\sum_{a_1,\ldots,a_k}^{*}\mu_k(a_1,\ldots,a_k)", r"\Pp(N_0\ge k)", r"\theta_i=\beta\log i+\alpha\log\log i+O(1)"]: self.assertIn(token, self.active)
        catalog = json.loads((ROOT / "papers.json").read_text())["documents"]; doc = next(d for d in catalog if d["id"] == "boundary-laws"); self.assertEqual(doc["status"], "working"); self.assertEqual(doc.get("dependencies", []), [])
        status = (ROOT / "THEOREM_STATUS.md").read_text(); self.assertIn("Boundary laws", status); self.assertIn("Working mechanical extraction", status); self.assertIn("audit passed, repairs pending", status)
if __name__ == "__main__": unittest.main()
