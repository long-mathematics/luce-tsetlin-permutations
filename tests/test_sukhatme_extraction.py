from pathlib import Path
import json,re,unittest
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex'
ACTIVE=ROOT/'papers/sukhatme-fixed-points/sukhatme-fixed-points.tex'
BLOCKS=[('\\subsection{The exponential race}', '\\subsection{Gumbel priorities}', '% BEGIN ARCHIVED BLOCK: exponential-race-input', '% END ARCHIVED BLOCK: exponential-race-input'), ('\\subsection{Gumbel priorities}', '\\begin{remark}[The derivative cancellation]', '% BEGIN ARCHIVED BLOCK: gumbel-threshold-input', '% END ARCHIVED BLOCK: gumbel-threshold-input'), ('\\subsection{Analytic input}', '\\subsection{A permuton-level obstruction}', '% BEGIN ARCHIVED BLOCK: analytic-input', '% END ARCHIVED BLOCK: analytic-input'), ('\\section{Sukhatme fixed points}', 'Theorem \\ref{thm:suk-fact} proves the fixed-order factorial moments', '% BEGIN ARCHIVED BLOCK: sukhatme-fixed-point-theory', '% END ARCHIVED BLOCK: sukhatme-fixed-point-theory')]
class ExtractionTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.archive=ARCHIVE.read_text();cls.active=ACTIVE.read_text()
 def test_blocks_byte_preserved(self):
  for ss,se,am,bm in BLOCKS:self.assertEqual(self.active.split(am+'\n',1)[1].split(bm,1)[0],self.archive[self.archive.index(ss):self.archive.index(se,self.archive.index(ss))])
 def test_reference_and_citation_closure(self):
  labs=set(re.findall(r'\\label\{([^}]+)\}',self.active));refs=set(re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',self.active));self.assertFalse(refs-labs)
  cites=set();[cites.update(k.strip() for k in m.group(1).split(',')) for m in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}',self.active)];bib=set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',self.active));self.assertFalse(cites-bib)
 def test_scope_and_status(self):
  [self.assertIn(t,self.active) for t in ['\\begin{theorem}[Sukhatme fixed-point mean]', '\\begin{proposition}[Separated terminal joint estimate]', '\\begin{theorem}[Local terminal Poisson point process]', '\\begin{theorem}[Sukhatme fixed factorial moments]']]
  d=next(x for x in json.loads((ROOT/'papers.json').read_text())['documents'] if x['id']=='sukhatme-fixed-points');self.assertEqual(d['status'],'working');self.assertEqual(d.get('dependencies',[]),[])
if __name__=='__main__':unittest.main()
