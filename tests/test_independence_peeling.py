from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'papers/independence-peeling/luce_independence_peeling.tex'


class IndependencePeelingTests(unittest.TestCase):
    def test_catalog_and_exact_dependencies(self):
        documents = json.loads((ROOT / 'papers.json').read_text())['documents']
        document = next(d for d in documents if d['id'] == 'independence-peeling')
        self.assertEqual(document['status'], 'current-research')
        self.assertEqual(set(document['dependencies']), {
            'regular-profile-cycles', 'macroscopic-pd',
            'mesoscopic-switching', 'sharp-order-edgeworth'})
        self.assertNotIn('mod-poisson', document['dependencies'])
        self.assertNotIn('total-cycle-edgeworth', document['dependencies'])
        self.assertTrue((ROOT / 'audits/independence-peeling-proof-audit.md').exists())

    def test_conditional_interfaces_are_explicit(self):
        text = SOURCE.read_text()
        for label in ('eq:imported-root-error', 'eq:imported-deletion-error',
                      'eq:finite-deletion-recursion', 'eq:weighted-good-slab'):
            self.assertIn(r'\label{' + label + '}', text)
        for name in ('eq:root-cdf', 'eq:deletion-joint',
                     'lem:residual-factorization', 'cor:factorial-domination'):
            self.assertIn(name, text)
        spectral = (ROOT / 'papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex').read_text()
        imported = ('thm:main-spectral', 'cor:comparable',
                    'lem:residual-factorization', 'prop:uniform-root-fraction',
                    'lem:deletion-stability', 'prop:residual-uniforms',
                    'eq:root-cdf', 'eq:deletion-error', 'eq:deletion-joint')
        for name in imported:
            self.assertIn(r'\label{' + name + '}', spectral)
        self.assertIn('not inferred from unconditional', text)
        self.assertIn('no additional information about unexposed edges', ' '.join(text.split()))

    def test_joint_annular_scope(self):
        text = SOURCE.read_text()
        self.assertIn(r"\cL(J^-,J^+,D_n(b',U'))", text)
        self.assertIn(r"\cup(U',U'+r]", text)
        self.assertIn('does not assert simultaneous independence', text)
        self.assertIn(r'\E|S_{n,r}/n-1|', text)

    def test_leading_theorem_and_appendix(self):
        text = SOURCE.read_text()
        self.assertEqual(text.count(r'\appendix'), 1)
        self.assertLess(text.index(r'\label{prop:micro-macro}'), text.index(r'\appendix'))
        self.assertLess(text.index(r'\section{Scope and further questions}'), text.index(r'\appendix'))
        self.assertLess(text.index(r'\appendix'), text.index(r'\begin{theorem}[Analytic cutoff'))
        for label in ('thm:mean-shift', 'thm:nuclear', 'thm:cumulants', 'conj:mod-poisson'):
            self.assertNotIn(r'\label{' + label + '}', text)

    def test_reference_closure(self):
        text = SOURCE.read_text()
        labels = re.findall(r'\\label\{([^}]+)\}', text)
        refs = [x for group in re.findall(r'\\(?:c|C|eq)?ref\{([^}]+)\}', text) for x in group.split(',')]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(set(refs).issubset(labels))
        citations = [x for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', text) for x in group.split(',')]
        self.assertTrue(set(citations).issubset(re.findall(r'\\bibitem\{([^}]+)\}', text)))


if __name__ == '__main__':
    unittest.main()
