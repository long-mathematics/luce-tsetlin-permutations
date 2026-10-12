#!/usr/bin/env python3
"""Generate one mechanically extracted manuscript from the frozen Luce monolith."""
from __future__ import annotations
import hashlib,json,re,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE_REL='archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex'
ARCHIVE_SHA='c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def line(t,o):return t.count('\n',0,o)+1
def once(t,a,b,name):
 if t.count(a)!=1: raise ValueError(f'{name}: expected one anchor, found {t.count(a)}')
 return t.replace(a,b,1)
def write(rel,text):
 p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

def main(cfg_path):
 cfg=json.loads(Path(cfg_path).read_text())
 ar=ROOT/ARCHIVE_REL
 if sha(ar)!=ARCHIVE_SHA: raise ValueError('Frozen source hash mismatch')
 arc=ar.read_text()
 blocks=[]; selected=''
 for b in cfg['blocks']:
  i=arc.index(b['start']);j=arc.index(b['end'],i);txt=arc[i:j];first=line(arc,i);last=line(arc,j)-1
  if 'first_line' in b and [first,last]!=[b['first_line'],b['last_line']]: raise ValueError(f"Range drift {b['name']}: {(first,last)}")
  blocks.append((b,txt,first,last));selected+=txt
 labels=set(re.findall(r'\\label\{([^}]+)\}',selected));refs=set(re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',selected))
 if refs-labels: raise ValueError('Unresolved references: '+', '.join(sorted(refs-labels)))
 cites=[]
 for m in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}',selected):
  for k in m.group(1).split(','):
   k=k.strip()
   if k and k not in cites:cites.append(k)
 bib={}
 if cites:
  a=arc.index(r'\begin{thebibliography}');z=arc.index(r'\end{thebibliography}',a);body=arc[a:z];ms=list(re.finditer(r'(?m)^\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',body))
  for n,m in enumerate(ms):bib[m.group(1)]=body[m.start():(ms[n+1].start() if n+1<len(ms) else len(body))].rstrip()+'\n'
  miss=[k for k in cites if k not in bib]
  if miss:raise ValueError('Missing bibliography: '+', '.join(miss))
 pre=r'''\documentclass[11pt]{article}
\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{mathrsfs}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue,hypertexnames=false,pdftitle={TITLE},pdfauthor={Christopher D. Long}}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{warning}[theorem]{Warning}
\newtheorem{definition}[theorem]{Definition}
\newcommand{\Pp}{\mathbb P}
\newcommand{\Ee}{\mathbb E}
\newcommand{\Rr}{\mathbb R}
\newcommand{\Nn}{\mathbb N}
\newcommand{\Zz}{\mathbb Z}
\newcommand{\one}{\mathbf 1}
\newcommand{\TV}{\mathrm{TV}}
\newcommand{\Pois}{\operatorname{Pois}}
\newcommand{\Exp}{\operatorname{Exp}}
\newcommand{\PPP}{\operatorname{PPP}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\Cov}{\operatorname{Cov}}
\newcommand{\diag}{\operatorname{diag}}
\newcommand{\dd}{\,d}
\newcommand{\eps}{\varepsilon}
\newcommand{\calD}{\mathcal D}
\newcommand{\calC}{\mathcal C}
\newcommand{\calE}{\mathcal E}
\newcommand{\calG}{\mathcal G}
\title{TITLE}
\author{Christopher D. Long}
\date{Mechanical extraction --- proof audit pending}
\begin{document}\maketitle
\begin{abstract}
ABSTRACT
\end{abstract}
\tableofcontents
\section{Status and provenance}
This source is a mechanical extraction from the frozen 139-page Luce manuscript at repository commit \texttt{6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0}. The mathematical blocks between the archival sentinels below are copied byte-for-byte from the frozen source. Only the standalone preamble, abstract, section wrappers, provenance notice, and cited bibliography entries have been added.

The extraction preserves every theorem hypothesis, identity, limiting statement, topology, quantifier, and proof step in the selected theorem package. It does not audit, repair, strengthen, weaken, or modernize the mathematics. Its status remains a working mechanical extraction until a separate adversarial audit is completed.
'''.replace('TITLE',cfg['title']).replace('ABSTRACT',cfg['abstract'])
 parts=[pre]
 for b,txt,first,last in blocks:
  if b.get('wrapper'):parts.append('\n\\section{'+b['wrapper']+'}\n\n')
  parts += [b['begin_marker']+'\n',txt,b['end_marker']+'\n']
 if cites:
  parts.append('\n\\begin{thebibliography}{99}\n\n')
  for k in cites:parts.append(bib[k]+'\n')
  parts.append('\\end{thebibliography}\n')
 parts.append('\n\\end{document}\n');active=''.join(parts);write(cfg['source'],active)
 for b,txt,first,last in blocks:
  obs=active.split(b['begin_marker']+'\n',1)[1].split(b['end_marker'],1)[0]
  if obs!=txt:raise ValueError('Block not preserved: '+b['name'])
 envre=re.compile(r'\\begin\{(theorem|proposition|lemma|corollary)\}(?:\[([^\]]+)\])?');rows=[]
 for m in envre.finditer(selected):
  env=m.group(1);stop=selected.find('\\end{'+env+'}',m.end());seg=selected[m.start():stop];lm=re.search(r'\\label\{([^}]+)\}',seg);lab=lm.group(1) if lm else '(unlabeled)';sig=('\\label{'+lab+'}') if lm else m.group(0);rows.append((env.title(),m.group(2) or '—',lab,line(arc,arc.index(sig)),line(active,active.index(sig))))
 ml=['# '+cfg['map_title'],'','Frozen source:',f'`{ARCHIVE_REL}`','',f'Frozen source SHA-256: `{ARCHIVE_SHA}`.','','The mathematical blocks are copied byte-for-byte. The active paper adds only the standalone wrapper and cited bibliography entries.','','## Source ranges','','| Block | Archived lines | Active sentinel |','| --- | ---: | --- |']
 for b,txt,first,last in blocks:ml.append(f"| {b['name']} | {first}--{last} | `{b['begin_marker']}` |")
 ml += ['','## Theorem and lemma provenance','','Labels are unchanged, so every old label is also the new label.','','| Environment | Title | Old label = new label | Archived line | Active line |','| --- | --- | --- | ---: | ---: |']
 for r in rows:ml.append(f'| {r[0]} | {r[1]} | `{r[2]}` | {r[3]} | {r[4]} |')
 ml += ['','## Closure checks','',f'- theorem/proposition/lemma/corollary environments: **{len(rows)}**;',f'- labels: **{len(labels)}**;',f'- distinct internal reference targets: **{len(refs)}**;',f'- cited bibliography keys: **{len(cites)}**;','- unresolved internal references: **0**;',f"- declared active-paper proof dependencies: **{len(cfg.get('dependencies',[]))}**.",'','This is an extraction and provenance map, not a correctness audit.']
 write(cfg['map'], '\n'.join(ml)+'\n')
 rec={'schema_version':1,'stage':cfg['id']+'-extraction','archive_source':ARCHIVE_REL,'archive_source_sha256':ARCHIVE_SHA,'active_source':cfg['source'],'active_source_sha256':sha(ROOT/cfg['source']),'source_ranges':[{'name':b['name'],'first_line':first,'last_line':last,'sentinel':b['begin_marker']} for b,txt,first,last in blocks],'theorem_environments':len(rows),'labels':len(labels),'reference_targets':len(refs),'citation_keys':cites,'proof_status':'mechanical extraction; adversarial audit pending'};write(cfg['record'],json.dumps(rec,indent=2)+'\n')
 write(cfg['extraction_audit'],cfg['extraction_note'].replace('{THEOREMS}',str(len(rows))).replace('{LABELS}',str(len(labels))).replace('{REFS}',str(len(refs))))
 # generic regression test
 block_repr=repr([(b['start'],b['end'],b['begin_marker'],b['end_marker']) for b,txt,first,last in blocks])
 tokens=repr(cfg['scope_tokens'])
 test=f'''from pathlib import Path\nimport json,re,unittest\nROOT=Path(__file__).resolve().parents[1]\nARCHIVE=ROOT/{ARCHIVE_REL!r}\nACTIVE=ROOT/{cfg['source']!r}\nBLOCKS={block_repr}\nclass ExtractionTests(unittest.TestCase):\n @classmethod\n def setUpClass(cls):cls.archive=ARCHIVE.read_text();cls.active=ACTIVE.read_text()\n def test_blocks_byte_preserved(self):\n  for ss,se,am,bm in BLOCKS:self.assertEqual(self.active.split(am+'\\n',1)[1].split(bm,1)[0],self.archive[self.archive.index(ss):self.archive.index(se,self.archive.index(ss))])\n def test_reference_and_citation_closure(self):\n  labs=set(re.findall(r'\\\\label\\{{([^}}]+)\\}}',self.active));refs=set(re.findall(r'\\\\(?:ref|eqref|autoref)\\{{([^}}]+)\\}}',self.active));self.assertFalse(refs-labs)\n  cites=set();[cites.update(k.strip() for k in m.group(1).split(',')) for m in re.finditer(r'\\\\cite(?:\\[[^\\]]*\\])*\\{{([^}}]+)\\}}',self.active)];bib=set(re.findall(r'\\\\bibitem(?:\\[[^\\]]*\\])?\\{{([^}}]+)\\}}',self.active));self.assertFalse(cites-bib)\n def test_scope_and_status(self):\n  [self.assertIn(t,self.active) for t in {tokens}]\n  d=next(x for x in json.loads((ROOT/'papers.json').read_text())['documents'] if x['id']=={cfg['id']!r});self.assertEqual(d['status'],'working');self.assertEqual(d.get('dependencies',[]),{cfg.get('dependencies',[])!r})\nif __name__=='__main__':unittest.main()\n''';write(cfg['test'],test)
 # catalog
 cp=ROOT/'papers.json';cat=json.loads(cp.read_text());new={'id':cfg['id'],'title':cfg['title'],'source':cfg['source'],'pdf':cfg['pdf'],'status':'working','dependencies':cfg.get('dependencies',[])};idx=next(i for i,d in enumerate(cat['documents']) if d['id']==cfg['catalog_before']);cat['documents'].insert(idx,new);cp.write_text(json.dumps(cat,indent=2)+'\n')
 # docs exact replacements supplied in config
 for rel,key in [('README.md','readme'),('THEOREM_STATUS.md','status'),('DEPENDENCIES.md','dependencies_doc'),('notes/migration-plan.md','migration')]:
  p=ROOT/rel;t=p.read_text()
  for edit in cfg.get(key,[]):t=once(t,edit['anchor'],edit['replacement'],rel)
  p.write_text(t)
 # archive invariant
 for r in json.loads((ROOT/'archive/manifest.json').read_text())['files']:
  if sha(ROOT/r['path'])!=r['sha256']:raise ValueError('Frozen archive changed: '+r['path'])
 print(cfg['id'],len(rows),len(labels),len(refs),len(cites))
if __name__=='__main__':main(sys.argv[1])
