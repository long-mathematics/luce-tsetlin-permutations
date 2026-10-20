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
| `boundary-laws` | None |
| `sukhatme-fixed-points` | None |
| `endpoint-regular-universality` | None |
| `global-endpoint-poisson` | None |
| `endpoint-short-cycles` | None |
| `regular-profile-cycles` | None |
| `macroscopic-pd` | None |

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
| Pair domination | `erdos-turan-order`: pair corollary | Total prescribed length at most n/2; enough for the first Poisson/Berry--Esseen transfer. |
| Polynomial intensity | `sharp-order-edgeworth`: polynomial block proposition | Linear logarithmic terminal depth; arbitrary fixed logarithmic accuracy. |
| Passive-mark Campbell--Stein | `sharp-order-edgeworth`: passive Stein / polynomial product-Poisson modules | Entire growing core plus an unchanged permutation-measurable mark; no quenched conditioning on that mark. The omitted-count specialization is re-derived in the total-cycle paper. |
| Fixed-order domination | `sharp-order-edgeworth`: multi-clock theorem and factorial-domination corollary | Fixed order q only, total prescribed length at most n/2; used for higher moments and fixed-order expansions. |
| Discrete smoothing | internal to `total-cycle-edgeworth` | Taylor, Charlier, and smoothing lemmas are proved in the total-cycle paper and are not a Luce-model dependency. |

The total-cycle proof does not use the active macroscopic PD/GEM paper, regular-profile paper, or any endpoint-singular extraction.

### `mod-poisson` → `mesoscopic-switching`, `regular-profile-cycles`, `macroscopic-pd`

The exact marked clock-swap identity is cited from `mesoscopic-switching` (`prop:master-switch`); the new manuscript independently proves its real-fugacity estimates, conditional uniform-component decomposition, and complex generating-function bound. The only imported asymptotic theorems are:

- `regular-profile-cycles`: `prop:bulk-local-final` (separated bulk estimates for **targets**, uniform in source labels), `lem:endpoint-dom`, `lem:collision-dom`, and `cor:endpoint-tightness`. Their envelopes control the marked microscopic factorial-moment sums.
- `macroscopic-pd`: `thm:macroscopic-pd`, used only for the original-measure uniform-root cycle-length limit. No tilted or finite-deletion version is assumed.

The new proof derives the profile mean shift, marked residual Poisson cloud, rank-one Fredholm determinant correction, and locally uniform analytic mod-Poisson limit. Its higher-factorial-cumulant corollary does not import the separate unpublished profile mean-shift/cumulant manuscript. Internal proof checks and finite numerical tests are not independent external refereeing.

### `boundary-laws`

No active-paper dependency. The standalone extraction includes the exponential-race identity, vanishing-block implantation, exact top-window likelihood comparison, finite-volume bottom-window convergence, infinite-product criterion, Borel--Cantelli leakage argument, and phase diagram.

Its adversarial audit found no fatal gap and records six localized clarifications. Until those are applied, the paper remains `working`.

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

No active-paper dependency. Its internal proof chain is: subsequential marked-profile kernel and common L2 contraction; slab law and conditional permanental factorization; hereditary flatness and predictable adaptive exposure; relative-prefix control; two-scale orbit balance; root-avoiding change of measure; conditional residual-fraction uniformity; deletion stability; finite-dimensional independent residual fractions; and ell-one tail restoration/rearrangement to GEM(1)/PD(1).

External standard inputs are weak compactness/disintegration, maximal inequalities, weak convergence and continuous mapping, the bounded-Lipschitz criterion, and the standard GEM/PD relation. Its adversarial audit found no fatal gap and all six localized repairs have been applied and regression-checked.

## External literature and provenance

Standard external references are not represented as document edges in `papers.json`. Each manuscript is responsible for citing the external probability, analysis, operator-theoretic, or permutation-limit input it actually uses.

The frozen 139-page source under `archive/6178a99/` is an immutable provenance source, not a proof dependency. No active proof may import the historical rejected total-cycle candidate. The five final thematic papers are self-contained extractions even where that means duplicating archived preliminaries.

No growing-number-of-roots theorem, arbitrary-deletion quenched theorem, profile smoothness assumption for the comparable-rate papers, endpoint-singular input for the regular-profile paper, or mod-Poisson convergence hypothesis has been silently added.

## Open dependency-sensitive targets

The active `mod-poisson` manuscript establishes the sampled positive continuous-profile mean constant, universal fixed higher factorial-cumulant limits, and locally uniform analytic mod-Poisson convergence near z = 1. For arbitrary comparable-rate arrays, it gives a uniform mean-shift bound and local analytic bound without identifying a limiting residue. Open extensions include more general rate-array limits, endpoint-singular profiles, and larger complex domains or full-axis convergence. The new theorem is not an imported premise of its own proof; its actual upstream inputs are recorded above.

The next controlled edits to the five audit-passed working extractions are their focused audit-repair PRs. Those repairs must not create new active-paper dependency edges unless such an edge is explicitly justified, documented here, and added to `papers.json`.
