"""Exercise actual PDF builds across checkout paths, including source overrides."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('reproducibility_build', ROOT / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

TEX = r"""% Mentioning \pdftrailerid in a comment does not select an override.
\documentclass{article}
\begin{document}
Reproducible manuscript build.
\end{document}
"""


@unittest.skipUnless(shutil.which('latexmk') and shutil.which('pdflatex'), 'TeX build tools are unavailable')
class BuildReproducibilityTests(unittest.TestCase):
    def build_fixture(self, checkout: Path, text: str) -> bytes:
        relative_source = 'papers/reproducibility/probe.tex'
        source = checkout / relative_source
        source.parent.mkdir(parents=True)
        source.write_text(text)
        document = {'id': 'reproducibility', 'source': relative_source}
        with patch.object(build, 'ROOT', checkout), patch.object(build, 'BUILD', checkout / '.build'):
            pdf, pages = build.build_one(document)
        self.assertEqual(pages, 1)
        return pdf.read_bytes()

    def test_identical_pdf_bytes_across_checkout_and_output_paths(self):
        with tempfile.TemporaryDirectory(prefix='luce-build-paths-') as tmp:
            root = Path(tmp)
            first = self.build_fixture(root / 'first-checkout', TEX)
            second = self.build_fixture(root / 'different' / 'second-checkout', TEX)
        self.assertTrue(b'/ID [' in first, 'The default trailer ID is missing')
        self.assertTrue(first == second, 'PDF bytes differ between checkout paths')

    def test_source_can_keep_its_own_trailer_id_omission(self):
        # The bottom-window manuscript deliberately omits its trailer ID.
        source_choice = TEX.replace(r'\documentclass{article}', r'\pdftrailerid{}\documentclass{article}')
        with tempfile.TemporaryDirectory(prefix='luce-build-override-') as tmp:
            root = Path(tmp)
            first = self.build_fixture(root / 'first-checkout', source_choice)
            second = self.build_fixture(root / 'second-checkout', source_choice)
        self.assertTrue(b'/ID [' not in first, 'The source-selected trailer omission was overridden')
        self.assertTrue(first == second, 'PDF bytes differ between checkout paths')


if __name__ == '__main__':
    unittest.main()
