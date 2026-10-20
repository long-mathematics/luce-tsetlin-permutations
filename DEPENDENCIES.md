# Mathematical dependency map

This is the canonical dependency map for the active Luce/Tsetlin manuscript series. The machine-readable document graph is `papers.json`; this file explains the exact theorem/module edges and the review boundary behind those graph entries.

## Dependency semantics

A document-level edge A → B means that active manuscript A imports a named mathematical result or interface from active manuscript B. Citations for historical context, standard external literature, later applications, or duplicated self-contained preliminaries are **not** document dependency edges.

The five newly extracted endpoint/boundary papers intentionally have no active-paper edges: each standalone source contains the complete archived framework it needs. This duplicates some preliminary machinery across papers, but avoids making a mechanical extraction silently depend on another edited active copy.

The frozen monolith and historical rejected candidates are provenance, never active dependencies.

## Canonical document graph

The rows are in exactly the `papers.json` order.

| ID | Active-paper dependencies |
| --- | --- |
| `mesoscopic-switching` | None |
| `erdos-turan-order` | `mesoscopic-switching` |
| `sharp-order-edgeworth` | `mesoscopic-switching`, `erdos-turan-order` |
| `functional-erdos-turan` | `mesoscopic-switching`, `erdos-turan-order` |
| `total-cycle-edgeworth` | `mesoscopic-switching`, `erdos-turan-order`, `sharp-order-edgeworth` |
| `mod-poisson` | `mesoscopic-switching`, `regular-profile-cycles`, `macroscopic-pd` |
| `independence-peeling` | `mesoscopic-switching`, `regular-profile-cycles`, `macroscopic-pd`, `sharp-order-edgeworth` |
| `boundary-laws` | None |
| `bottom-window-universality` | None |
| `sukhatme-fixed-points` | None |
| `endpoint-regular-universality` | None |
| `global-endpoint-poisson` | None |
| `endpoint-short-cycles` | None |
| `regular-profile-cycles` | None |
| `macroscopic-pd` | None |

| `stratified-hammersley-lis` | None |

The graph is acyclic. Repository tests reject unknown document IDs and dependency cycles.

## Module-level dependency register

### `mesoscopic-switching`

No active-paper dependency. The paper proves internally the exact marked swap, selected-factor moment/tail bounds, the short-root estimate, and the free-depth finite-endpoint comparison used later.

Downstream reviewed interfaces include `prop:master-switch` (exact marked switch), `cor:selected-moments` (selected p>1 factor control), `cor:root-crude` (short-root bound), `prop:endpoint-mixing` (fixed one-/two-root endpoint mixing in mean conditional total variation), and `cor:quantitative-truncation-interface` (truncation-uniform consequences). These named modules have scoped review coverage; this does not constitute a full-paper audit.

### `erdos-turan-order` → `mesoscopic-switching`

The scalar logarithmic-order paper imports the marked switching and quantitative finite-endpoint interfaces from the switching manuscript. Its rate-oriented three-clock identity, pair domination, and product--LCM/von-Mangoldt arithmetic reduction are proved in the scalar paper.

The downstream module used by the functional order coordinate is the scalar paper's product--LCM comparison. The pair bound is also a permitted input to the first quantitative total-cycle transfer.

### `sharp-order-edgeworth` → `mesoscopic-switching`, `erdos-turan-order`

The sharp logarithmic-order supplement imports the switching/free-depth endpoint machinery and scalar-order framework. It proves the stronger quantitative modules reused by the total-cycle paper: polynomial block/intensity control, passive-mark Campbell--Stein/product-Poisson approximation, the fixed-order rate-oriented multi-clock identity, and fixed-order factorial domination.

The total-cycle paper does **not** import the sharp-order paper's prime-power linearization, high-frequency arithmetic analysis, nonlinear product--LCM remainder analysis, or final logarithmic-order Edgeworth conclusion.

### `functional-erdos-turan` → `mesoscopic-switching`, `erdos-turan-order`

The count-only functional branch uses switching/free-depth endpoint control, Campbell--Stein, the independent-Poisson functional CLT, and uniform restoration of omitted cycles. It does not need the scalar product--LCM theorem.

The joint logarithmic-order coordinate additionally imports the scalar paper's product--LCM comparison. The total-count mean estimate comes from the exact mean-switch identity rather than from total-variation moment transfer.

### `total-cycle-edgeworth` → `mesoscopic-switching`, `erdos-turan-order`, `sharp-order-edgeworth`

The precise active inputs are:

| Input | Source | Scope actually used |
| --- | --- | --- |
| Exact marked swap and selected tails | `mesoscopic-switching`: `prop:master-switch`, `cor:selected-moments` | Permutation-measurable tests; selected p>1 control depends only on the rate ratio. |
| Internal short-root bound | `mesoscopic-switching`: `cor:root-crude` | No macroscopic PD/GEM input. |
| Free-depth endpoint estimate | `mesoscopic-switching`: `prop:endpoint-mixing` | Fixed one/two roots; mean conditional TV relative to the coarse environment. |
| Uniform truncations | `mesoscopic-switching`: `cor:quantitative-truncation-interface` | One factor costs A times the endpoint error and two factors A-squared; shared-clock fresh second moments are treated as second moments. |
| Pair domination | `erdos-turan-order`: pair corollary | Total prescribed length at most n/2; enough for the first Poisson/Berry–Esseen transfer. |
| Polynomial intensity | `sharp-order-edgeworth`: polynomial block proposition | Linear logarithmic terminal depth; arbitrary fixed logarithmic accuracy. |
| Passive-mark Campbell--Stein | `sharp-order-edgeworth`: passive Stein / polynomial product-Poisson modules | Entire growing core plus an unchanged permutation-measurable mark; no quenched conditioning on that mark. The omitted-count specialization is re-derived in the total-cycle paper. |
| Fixed-order domination | `sharp-order-edgeworth`: multi-clock theorem and factorial-domination corollary | Fixed order q only, total prescribed length at most n/2; used for higher moments and fixed-order expansions. |
| Discrete smoothing | internal to `total-cycle-edgeworth` | Taylor, Charlier, and smoothing lemmas are proved in the total-cycle paper and are not a Luce-model dependency. |

The total-cycle proof does not use the active macroscopic PD/GEM paper, regular-profile paper, or any endpoint-singular extraction.

### `mod-poisson` → `mesoscopic-switching`, `regular-profile-cycles`, `macroscopic-pd`

The exact marked clock-swap identity is cited from `mesoscopic-switching` (`prop:master-switch`); the new manuscript independently proves its real-fugacity estimates, conditional uniform-component decomposition, and complex generating-function bound. The only imported asymptotic theorems are:

- `regular-profile-cycles`: `prop:bulk-local-final` (separated bulk estimates for **targets**, uniform in source labels), `lem:endpoint-dom`, `lem:collision-dom`, and `cor:endpoint-tightness`. Their envelopes control the marked microscopic factorial-moment sums.
- `macroscopic-pd`: `thm:main-spectral`, `eq:uniform-root-main`, and `cor:comparable`, used only for the original-measure uniform-root cycle-length limit. The comparable-rate corollary covers arrays without an empirical-law limit. No tilted or finite-deletion version is assumed.

The new proof derives the profile mean shift, marked residual Poisson cloud, rank-one Fredholm determinant correction, and locally uniform analytic mod-Poisson limit. Its higher-factorial-cumulant corollary does not import the separate unpublished profile mean-shift/cumulant manuscript. Internal proof checks and finite numerical tests are not independent external refereeing.

### `independence-peeling` → `mesoscopic-switching`, `regular-profile-cycles`, `macroscopic-pd`, `sharp-order-edgeworth`

The principal result is microscopic–macroscopic independence, not another scalar total-cycle theorem. The two proof branches use different upstream interfaces:

| Result in this manuscript | Exact input | Scope |
| --- | --- | --- |
| Joint short-cycle/partition independence | `regular-profile-cycles`: `thm:regular-cycles`, `prop:regular-cycle-factorial` | Fixed vectors and all fixed mixed factorial moments under a positive continuous profile. |
| Finite-deletion uniformity | `macroscopic-pd`: `lem:residual-factorization`, `prop:uniform-root-fraction`, `lem:deletion-stability`; equations `eq:root-cdf`, `eq:deletion-error`, `eq:deletion-joint` | Under the existing positive-profile hypothesis, conditional uniformity over regular histories on good slab data; the initial bounded-deletion error is propagated explicitly. Unconditional PD/GEM convergence alone is not sufficient. |
| Finite annular passive-mark comparison | `mesoscopic-switching`: `prop:master-switch`, `cor:selected-moments`, `prop:endpoint-mixing`, `cor:quantitative-truncation-interface` | One- and two-root truncated moments, with a finite numerical depth range; absolute switching-intensity error and constants uniform in the truncation level. |
| Iterated fixed-moment/cumulant comparison | `sharp-order-edgeworth`: `cor:factorial-domination`, following `thm:multiclock` | Only fixed-order distinct-cycle domination for total prescribed length at most n/2; no arithmetic order theorem or Edgeworth conclusion is used. |

The unconditional comparable-array input uses `thm:main-spectral` and `cor:comparable`. The conditional proof now uses maximum-normalized clocks and the exact spectral error `delta + 2h + chi_n + sqrt(p_n(D(U)))`. Its empirical clock-tail envelope is `exp(-U/kappa) + epsilon_n^2`. The full product of previously fixed root and deletion coefficients controls propagation through a fixed number of deletions; cutoffs control tails, the mesh controls `2h`, and n is chosen last. These inputs are pinned to spectral-source commit `81462993a7400f972a3d75583d447fbeccf1e7b3`. No endpoint-singular independence or uniformity over varying profiles is added.

The PD(1) cutoff appendix uses only the standard size-biased representation and the Dickman density cited there. `total-cycle-edgeworth` is cited for marked-Stein provenance and scalar comparisons; `mod-poisson` is cited only to delimit nonoverlap. Neither is an active dependency. The finite-deletion lemma does not assume uniform good-event probabilities after conditioning on a rare prescribed cycle, and the iterated scalar convolution comparison does not assert simultaneous independence of all actual annular counts.

### `boundary-laws`

No active-paper dependency. The standalone extraction includes the exponential-race identity, vanishing-block implantation, exact top-window likelihood comparison, finite-volume bottom-window convergence, infinite-product criterion, Borel--Cantelli leakage argument, and phase diagram.

Its adversarial audit found no fatal gap and records six localized clarifications. Until those are applied, the paper remains `working`.

### `bottom-window-universality`

No active-paper dependency. The paper supplies the Poisson-spacings coupling, regularly varying endpoint and interior tail bounds, almost-sure c-zero and ell-p convergence, continuity of fixed-window ranking, quenched and annealed total-variation passage, last-label integral and tail analysis, exact-grid comparison, and the logarithmic critical-scale argument.

Its external inputs are the Borga--Chatterjee--Diaconis permuton-sampling representation, Rényi's uniform order-statistic representation, regular-variation uniform convergence and Potter bounds, standard Poisson marking/mapping and iid extreme-value results, and the stable-jump Poisson–Dirichlet identification. Pitman--Tran's last-pick/rank-permutation results are cited for their substantive overlap, including the linear last-label constant; the Arendarczyk--Dębicki Weibull-product lemma supplies the scalar-tail precedent in the critical example. The standalone proofs do not import the boundary extraction or any cycle-limit manuscript. Its Poisson–Dirichlet corollary describes clock shares rather than cycle lengths.

### `sukhatme-fixed-points`

No active-paper dependency. The standalone extraction contains the exponential/Gumbel representation, fixed-dimensional tilted lattice LLT, death-process product envelope, terminal saddle geometry, anisotropic Fourier/tilting package, separated terminal joint estimate, local terminal Poisson process, and fixed-factorial-moment summation.

Its adversarial audit found no fatal gap and records six localized clarifications. Until those are applied, the paper remains `working`.

### `endpoint-regular-universality`

No active-paper dependency. The standalone extraction includes the exponential/Gumbel and tilted-LLT preliminaries, shared anisotropic Fourier/tilting toolkit, endpoint regular-variation hypotheses and weighted sum asymptotics, endpoint saddle/localization, fixed-point factorial moments, displacement and tangent limits, multiplicative semigroup/kernel traces, and microscopic endpoint permutation.

Its adversarial audit found no fatal gap and records six localized clarifications. Until those are applied, the paper remains `working`.

### `global-endpoint-poisson`

No active-paper dependency. The standalone extraction deliberately contains the complete endpoint-regular framework it needs, followed by the approximate-Palm Stein bound, terminal-rank transposition, exact likelihood ratio, quantitative one-dimensional saddle, swap--Palm comparison, two-cycle transition bound, weighted two-cycle summability, and the final global Poisson/normal theorem.

Its adversarial audit found no fatal gap and records six localized clarifications. Until those are applied, the paper remains `working`.

### `endpoint-short-cycles`

No active-paper dependency. The standalone extraction deliberately contains the endpoint-regular framework and the source-to-target saddle/LLT/localization package, scheduled/forced-deletion envelope, endpoint survival tail, continuum and discrete multiplicative traces, negligible-configuration estimates, and mixed factorial-moment summation.

Its adversarial audit found no fatal gap and records six localized clarifications. Until those are applied, the paper remains `working`.

### `regular-profile-cycles`

No active-paper dependency. Its internal proof chain is: exponential-race/Gumbel identities; Bernoulli concentration and tilted lattice LLT; sampled-profile approximation and regular saddle geometry; cumulative-count LLT, off-saddle exclusion, and integrated saddle; separated bulk multipoint estimate; endpoint/collision/gap/crowding envelopes; fixed and mixed factorial moments with total-variation upgrade; Hilbert--Schmidt kernel and cyclic traces; and diagonal-band, sparse-entry, thin-graph, deterministic-overlap, and transverse-curve applications.

External standard inputs include the identified Luce permuton density, Bernoulli/local-limit background, trace-ideal results, the multivariate method of moments, Scheffé's lemma, and a converging-together criterion. The manuscript supplies references. Its adversarial audit found no fatal gap and all six localized repairs have been applied and regression-checked.

### `macroscopic-pd`

The sole active source is [Spectral Poisson–Dirichlet Universality under Arbitrary Rate Arrangements](papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex). There is no active-paper dependency. The manuscript cites the comparable-rate predecessor for provenance and reproduces the slab, flatness, and regeneration framework it needs.

Its internal proof chain is: the exponential observation channel; factorization through arbitrary rate-to-label couplings; spectral compression to finite slab matrices; conditional permanental factorization and hereditary flatness; predictable exposure and relative-prefix control; a late-row contraction controlled by total row mass; two-scale orbit balance; stopped root avoidance and the harmonic product; conditional root fractions and deletion stability on good slab data; and a full-budget cutoff induction with residual-mass restoration to GEM(1)/PD(1) in ell-one. No Hilbert–Schmidt assumption is used.

The regularly varying gap proof combines its explicit rate-chain kernel, Abelian asymptotics, dyadic lower bounds, and a geometric Poincaré argument. The dyadic-doubling theorem and slowly varying no-gap theorem are proved within the manuscript. The subsequential criterion recovers arbitrary comparable arrays through the common-component bound.

External standard inputs are weak compactness/disintegration, maximal inequalities, weak convergence and continuous mapping, the bounded-Lipschitz criterion, the GEM/PD relation, and regular-variation background. The five repaired proof points, two theorem promotions, and editorial corrections are recorded in [the spectral audit](audits/spectral-pd-proof-audit.md). The [theorem migration map](papers/macroscopic-pd/THEOREM_MIGRATION.md) identifies every reused conditional interface. The preserved predecessor and original monolith remain provenance, not active dependencies.

### `stratified-hammersley-lis`

No active-paper dependency. The independent-clock representation reduces Luce LIS to a deterministic-fibre point cloud. The manuscript proves the row-stratified shape theorem through a common-core/residual decomposition, uniform-permutation LIS bounds, mesh-based random-exit control, and exact block variational equality. Conditional path localization and independent-score rank transfer are proved internally. The regular-profile Luce shape and robust sparse-error results use that theorem, while the endpoint-degenerate LIS/LDS argument instead adds a dyadic terminal-block exponential-moment estimate and prefix truncation. The self-similar Sukhatme estimate and certified decreasing-rate LIS lower bound are internal additions.

External standard inputs include Logan–Shepp/Vershik–Kerov and uniform-permutation fixed-deviation bounds (Deuschel–Zeitouni, or Talagrand plus first-order LIS); standard compactness, concentration, regular variation, and deterministic Hamilton–Jacobi comparison. Mallows-permutation LIS literature is background only. No theorem from `macroscopic-pd`, `regular-profile-cycles`, or `independence-peeling` is imported.

**Review boundary:** the October 13 expanded manuscript received a targeted adversarial audit, its score-to-rank path-localization transfer was repaired using arbitrary monotone interpolants, and the endpoint orientation, ceiling convention, bounded-density independence, and regular-Hamilton–Jacobi specification were clarified. See [the audit record](audits/stratified-hammersley-proof-audit.md). Numerical simulations are not proof; no KPZ/Tracy–Widom assertion is promoted.

## External literature and provenance

Standard external references are not represented as document edges in `papers.json`. Each manuscript is responsible for citing the external probability, analysis, operator-theoretic, or permutation-limit input it actually uses.

The frozen 139-page source under `archive/6178a99/` is an immutable provenance source, not a proof dependency. No active proof may import the historical rejected total-cycle candidate. The five final thematic papers are self-contained extractions even where that means duplicating archived preliminaries.

No growing-number-of-roots theorem, arbitrary-deletion quenched theorem, profile smoothness assumption for the comparable-rate papers, endpoint-singular input for the regular-profile paper, or mod-Poisson convergence hypothesis has been silently added.

## Open dependency-sensitive targets

The active `mod-poisson` manuscript establishes the sampled positive continuous-profile mean constant, universal fixed higher factorial-cumulant limits, and locally uniform analytic mod-Poisson convergence near z = 1. For arbitrary comparable-rate arrays, it gives a uniform mean-shift bound and local analytic bound without identifying a limiting residue. Open extensions include more general rate-array limits, endpoint-singular profiles, and larger complex domains or full-axis convergence. The new theorem is not an imported premise of its own proof; its actual upstream inputs are recorded above.

The next controlled edits to the five audit-passed working extractions are their focused audit-repair PRs. Those repairs must not create new active-paper dependency edges unless such an edge is explicitly justified, documented here, and added to `papers.json`.
