import importlib.util
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build', ROOT/'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class RepositoryTests(unittest.TestCase):
    def test_catalog_and_dependencies(self):
        build.check_catalog()
    def test_archive_preservation(self):
        build.check_archive()
    def test_links_and_readme(self):
        build.check_markdown()
    def test_bad_math_rejected(self):
        bad = [
            r'\[x\]',
            '$\n',
            '$$\nx\n=\ny\n$$\n',
            '$$\n- x\n$$\n',
            '$$\nx\n',
            r'$\Ee X$',
            r'$\operatorname{ord}(\sigma)$',
            r'$\newcommand{\foo}{x}\foo$',
            r'$$\n\begin{aligned}x&=y\end{aligned}\n$$\n',
            r'$\href{https://example.com}{x}$',
            r'$\foo{x}$',
        ]
        for text in bad:
            with self.subTest(text=text), self.assertRaises(ValueError):
                build.check_readme_math(text)
    def test_good_math(self):
        build.check_readme_math('$$\nx\n= y\n$$\n')
    def test_monolith_decomposition_status(self):
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

    def test_normalized_theorem_and_dependency_maps_match_catalog(self):
        docs = build.catalog()
        ids = [d['id'] for d in docs]
        status = (ROOT/'THEOREM_STATUS.md').read_text()
        deps = (ROOT/'DEPENDENCIES.md').read_text()

        status_rows = [line for line in status.splitlines() if line.startswith('| `')]
        status_ids = [line.split('`')[1] for line in status_rows[:len(ids)]]
        self.assertEqual(status_ids, ids)

        dep_section = deps.split('## Canonical document graph', 1)[1].split('## Module-level dependency register', 1)[0]
        dep_rows = [line for line in dep_section.splitlines() if line.startswith('| `')]
        dep_ids = [line.split('`')[1] for line in dep_rows]
        self.assertEqual(dep_ids, ids)

        for d in docs:
            dep_cell = ', '.join('`'+x+'`' for x in d.get('dependencies', [])) or 'None'
            self.assertIn('| `'+d['id']+'` | '+dep_cell+' |', dep_section)
            catalog_fragment = '| `'+d['id']+'` |'
            self.assertIn(catalog_fragment, status)
            self.assertIn('| `'+d['status']+'` |', status)

        self.assertEqual(status.count('audit passed, repairs pending'), 5)

    def test_historical_candidate_is_not_dependency(self):
        for d in build.catalog():
            self.assertNotIn('resolution-candidate', d['source'])
            self.assertNotIn('historical-total-cycle', d.get('dependencies', []))
    def test_status_distinctions(self):
        text = (ROOT/'THEOREM_STATUS.md').read_text()
        self.assertIn('Historical rejected candidate', text)
        self.assertIn('Formalization status', text)
        self.assertIn('not started', text)
    def test_no_imported_thorp_material(self):
        self.assertFalse((ROOT/'third_party/openai-thorp').exists())

if __name__ == '__main__':
    unittest.main()
