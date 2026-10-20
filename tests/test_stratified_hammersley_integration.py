"""Registration and display-title checks for the stratified Hammersley manuscript."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StratifiedHammersleyIntegrationTests(unittest.TestCase):
    def test_catalog_entry_and_source(self):
        docs = json.loads((ROOT/"papers.json").read_text())["documents"]
        record = next(d for d in docs if d["id"] == "stratified-hammersley-lis")
        self.assertEqual(record["status"], "current-research")
        self.assertEqual(record["dependencies"], [])
        text = (ROOT/record["source"]).read_text()
        for needle in ("\\\\label{thm:stratified-shape}", "\\\\label{thm:endpoint-luce}", "3.0602"):
            self.assertIn(needle.replace("\\\\","\\"), text)
        self.assertIn("Christopher D. Long", text)

    def test_display_titles_are_unicode(self):
        docs = json.loads((ROOT/"papers.json").read_text())["documents"]
        self.assertTrue(all("--" not in d["title"] for d in docs))
        readme = (ROOT/"README.md").read_text()
        for phrase in ("Erdős–Turán", "Berry–Esseen", "Poisson–Dirichlet", "Stratified Hammersley Laws for Luce Permutations"):
            self.assertIn(phrase, readme)
        self.assertNotIn("the cataloged manuscripts above do not claim a general solution", readme)

if __name__ == "__main__":
    unittest.main()
