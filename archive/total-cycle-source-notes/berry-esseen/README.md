# Total-cycle quantitative transfer

The proof note establishes, from the specified switching inputs, exact-mean Poisson approximation in total variation with error O((log log n)^2/log n) and the sharp O((log n)^(-1/2)) Berry–Esseen theorem for comparable-rate Luce total cycle counts.

Files:
- `luce-total-cycle-berry-esseen.pdf`: ten-page proof note.
- `luce-total-cycle-berry-esseen.tex`: standalone LaTeX source.
- `luce-total-cycle-berry-esseen.md`: Markdown source.
- `check_poisson_smoothing.py`: reproducible exact and numerical checks.
- `smoothing_checks.json`: executed check results.
- `source-manifest.json`: upstream source identifiers and scope.
- `SHA256SUMS`: hashes of these deliverables.

Run checks with Python 3.10+, NumPy, and SciPy:

```sh
python check_poisson_smoothing.py
```

Compile the supplied LaTeX source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error luce-total-cycle-berry-esseen.tex
```

The tests verify finite consistency, not the asymptotic theorem. The source manifest records dependencies; this bundle does not include full repository source copies and does not change the repository.
