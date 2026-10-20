# Stratified Hammersley / LIS proof and integration record

Status: internally audited and repaired 20 October 2026. This records an AI-assisted adversarial proof audit, not independent external refereeing or formal verification.

## Provenance and choice of version

The active source `papers/stratified-hammersley-lis/stratified-hammersley-laws-luce.tex` retains the stronger 13 October 2026 draft. The earlier 12 October `stratified-hammersley-luce.tex` supplied the regular-profile development but is not an additional active paper. The 13 October manuscript extends the foundation to independent-score rankings, path localization, endpoint-degenerate dyadic rates, and both Sukhatme rate orientations. The revised manuscript further corrects the proof and clarifies external input.

## Proof scope and confirmed modules

- **Row-stratified theorem.** Independent vertical-fibre points with densities uniformly approximating a bounded continuous row density admit a common-core/residual decomposition. Core heights are identically distributed within each strip, giving exact uniform-permutation ranks; residual points are dominated by a Bernoulli-uniform proposal cloud. Mesh rounding of random strip-exit heights and the exact finite-block formula yield the full `sqrt(n)` shape field, fixed-deviation `exp(-c sqrt(n))` tails, uniform field convergence, all finite moments, and almost-sure convergence under arbitrary couplings.
- **Localization.** Compactness and upper semicontinuity of the Hammersley action give an action gap. The repaired restricted upper bound applies to **every monotone interpolation** through a chain, not just its polygon. This permits a valid score-to-rank transfer under nonlinear monotone homeomorphisms, using ideal rank polygons and a deterministic `2 delta` comparison.
- **Regular-score and Luce transfer.** Uniform empirical CDF concentration and monotone score transformations yield the independent-score ranking theorem, including Gaussian Thurstone–Mosteller scores. Regular positive Luce profiles have the identified Luce permuton density and a complete two-parameter shape field. Sparse exceptional rows with globally comparable rates contribute `o_P(sqrt(n))`.
- **Endpoint theorem.** Dyadic terminal-block comparability gives exponential moments for the LIS and LDS supported on a terminal block. Prefix limits and correctly rounded terminal-label counts yield terminal subsequence limits for endpoint-degenerate profiles, all finite moments, fixed-deviation concentration and almost-sure convergence. Regular variation and both Sukhatme rate orientations are special cases. The theorem does **not** establish a complete singular two-parameter shape field.
- **Additional bounds.** A common-subdensity argument improves the comparable-rate lower bound to `2/sqrt(kappa)`. Self-similarity of terminal Sukhatme rates yields `ell(δ) <= L <= ell(δ)/(1-sqrt(δ))` separately for LIS and LDS. An explicit admissible trial curve establishes a rigorous decreasing-rate LIS lower bound `L_Suk > 3.0602`. No numerical equality at two-decimal precision is certified.

## Repairs included in active source

1. Independence added explicitly to the first-moment chain lemma.
2. Boundary-truncated score-to-rank variational invariance, with full path-localization repair.
3. Restored definition of the decreasing-subsequence constant.
4. Correct count `ceil(delta n)` for discarded endpoint labels and partial dyadic-block intersections.
5. Precise distinction of decreasing and increasing Sukhatme rate conventions; endpoint LDS included.
6. Explicit terminal-block exponential-moment calculation and quantitative prefix truncation.
7. Hamilton–Jacobi uniqueness restricted to continuous coordinatewise nondecreasing viscosity solutions; zero-boundary specification and comparison included.
8. Correct attribution of CDK's introductory LIS question and BCD §5.3; context from Mueller–Starr and Bhatnagar–Peled; explicit warning on exponentially unlikely one-per-strip conditioning; accurate uniform-permutation tail citation; consistent vertical-fibre terminology.
9. Exact rational certificate of the `3.0602` lower bound. Claimed decimal approximations around `3.05` were excluded because they contradict this certified lower bound.

## Dependency and review boundary

No active-paper dependencies. Standard external inputs are cited in the source; no PD(1) cycle theorem is used. Build, source checks, PDF snapshots and numerical experiments are reproducibility aids, not mathematical or novelty certification. KPZ/Tracy–Widom fluctuations, full RSK surfaces, and unrestricted positive-rate arrays remain open.

The archived monolith and all existing active papers are unchanged by this integration.
