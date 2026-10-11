from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]

class IntegrationTests(unittest.TestCase):
    def test_one_canonical_functional_source(self):
        self.assertFalse((ROOT/'notes/working/functional-luce-erdos-turan.tex').exists())
        self.assertTrue((ROOT/'papers/functional-erdos-turan/functional-luce-erdos-turan.tex').exists())
    def test_expected_statement_labels(self):
        text=(ROOT/'papers/total-cycle-edgeworth/total-cycle-edgeworth.tex').read_text()
        for label in ('thm:poisson-be','thm:first','thm:signed','thm:second','thm:fixed-order','eq:mean-error','eq:moment-transfer'):
            self.assertIn('label{'+label+'}',text)
        self.assertIn('positivity is not asserted',text)
        self.assertIn('no growing-order uniformity',text)
    def test_explicit_truncation_and_mean_interfaces(self):
        text=(ROOT/'papers/mesoscopic-switching/mesoscopic-luce-cycles.tex').read_text()
        self.assertIn('cor:quantitative-truncation-interface',text)
        text=(ROOT/'papers/functional-erdos-turan/functional-luce-erdos-turan.tex').read_text()
        self.assertIn('cor:total-cycle-clt',text)
        self.assertNotIn('switching proof under submacroscopic root-cycle escape',text)
    def test_renewed_checks_are_not_archive_scripts(self):
        checks=json.loads((ROOT/'verification.json').read_text())['checks']
        self.assertEqual(len(checks),3)
        for c in checks:
            self.assertTrue(c['script'].startswith('scripts/total-cycles/'))
    def test_profile_limits_remain_open(self):
        text=(ROOT/'THEOREM_STATUS.md').read_text()
        self.assertIn('## Open questions',text)
        self.assertIn('locally uniform complex Luce mod-Poisson residue remain open',text)

if __name__=='__main__': unittest.main()
