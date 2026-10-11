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
            r'\\[x\\]',
            '$\\n',
            '$$\\nx\\n=\\ny\\n$$\\n',
            '$$\\n- x\\n$$\\n',
            '$$\\nx\\n',
            r'$\\Ee X$',
            r'$\\operatorname{ord}(\\sigma)$',
            r'$\\newcommand{\\foo}{x}\\foo$',
            r'$$\\n\\begin{aligned}x&=y\\end{aligned}\\n$$\\n',
            r'$\\href{https://example.com}{x}$',
        ]
        for text in bad:
            with self.subTest(text=text), self.assertRaises(ValueError):
                build.check_readme_math(text)
    def test_good_math(self):
        build.check_readme_math('$$\nx\n= y\n$$\n')
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
