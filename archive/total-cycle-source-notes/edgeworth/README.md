# Total-cycle lattice Edgeworth proof note

Author: Christopher D. Long. Research note, 11 October 2026.

Read `luce-total-cycle-edgeworth.pdf` for the typeset proof or the matching
Markdown/LaTeX source. The note proves first and second lattice Edgeworth
expansions, the exact leading Kolmogorov constant, and a fixed-order signed
Poisson--Charlier hierarchy from the named comparable-rate switching inputs.
Profile limits are explicitly separated as unproved targets.

## Reproduce checks

```sh
python check_edgeworth.py --output edgeworth_checks.json
pdflatex -interaction=nonstopmode -halt-on-error luce-total-cycle-edgeworth.tex
pdflatex -interaction=nonstopmode -halt-on-error luce-total-cycle-edgeworth.tex
```

Python requirements: numpy, scipy, sympy. LaTeX requirements: a normal article
installation with amsmath, amssymb, mathtools, microtype, needspace, hyperref,
and the standard packages included by Pandoc.

The JSON records numerical values and exact algebra checks. These are not
an independent verification of the upstream Luce endpoint theorem.
`source-manifest.json` records the exact source dependency boundary.
No repository file was changed.
