# Mathematical dependency map

This is the canonical dependency map for the active Luce/Tsetlin manuscript series. The machine-readable document graph is `papers.json`; this file explains the exact theorem/module edges and the review boundary behind those graph entries.

## Dependency semantics

A document-level edge (A	o B) means that active manuscript (A) imports a named mathematical result or interface from active manuscript (B). Citations for historical context, standard external literature, later applications, or duplicated self-contained preliminaries are **not** document dependency edges.

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

Downstream reviewed interfaces include:

- `prop:master-switch`: exact marked switch for permutation-measurable tests;
- `cor:selected-moments`: selected (p>1) factor control depending only on the rate ratio;
- `cor:root-crude`: internal short-root bound;
- `prop:endpoint-mixing`: fixed one-/two-root endpoint mixing in mean conditional total variation relative to the coarse environment;
- `cor:quantitative-truncation-interface`: truncation-uniform one-/two-factor consequences.

These named modules have scoped review coverage; this does not constitute a full-paper audit.

### `erdos-turan-order` → `mesoscopic-switching`

The scalar logarithmic-order paper imports the marked switching and quantitative finite-endpoint interfaces from the switching manuscript. Its rate-oriented three-clock identity, pair domination, and product--LCM/von-Mangoldt arithmetic reduction are proved in the scalar paper.

The downstream module used by the functional order coordinate is the paper's product--LCM comparison. The pair bound is also a permitted input to the first quantitative total-cycle transfer.

### `sharp-order-edgeworth` → `mesoscopic-switching`, `erdos-turan-order`

The sharp logarithmic-order supplement imports the switching/free-depth endpoint machinery and the scalar order framework. It proves the stronger quantitative modules reused by the total-cycle paper, including:

- polynomial block/intensity control on the logarithmic core;
- passive-mark Campbell--Stein/product-Poisson approximation;
- the fixed-order rate-oriented multi-clock identity;
- fixed-order factorial domination.

The total-cycle paper does **not** import this paper's prime-power linearization, high-frequency arithmetic analysis, nonlinear product--LCM remainder analysis, or final logarithmic-order Edgeworth conclusion.

### `functional-erdos-turan` → `mesoscopic-switching`, `erdos-turan-order`

The count-only functional branch uses switching/free-depth endpoint control, Campbell--Stein, the independent-Poisson functional CLT, and uniform restoration of omitted cycles. It does not need the scalar product--LCM theorem.

The joint logarithmic-order coordinate additionally imports the scalar paper's product--LCM comparison. The total-count mean estimate comes from the exact mean-switch identity rather than from total-variation moment transfer.

### `total-cycle-edgeworth` → `mesoscopic-switching`, `erdos-turan-order`, `sharp-order-edgeworth`

The precise active inputs are:

| Input | Source | Scope actually used |
| --- | --- | --- |
| Exact marked swap and selected tails | `mesoscopic-switching`: `prop:master-switch`, `cor:selected-moments` | Permutation-measurable tests; selected (p>1) depends only on the rate ratio. |
| Internal short-root bound | `mesoscopic-switching`: `cor:root-crude` | No macroscopic PD/GEM input. |
| Free-depth endpoint estimate | `mesoscopic-switching`: `prop:endpoint-mixing` | Fixed one/two roots; mean conditional TV relative to the coarse environment. |
| Uniform truncations | `mesoscopic-switching`: `cor:quantitative-truncation-interface` | One factor costs (A) times the endpoint error and two factors (A^2); the shared-clock fresh second moment is the second moment, not the square of the first. |
| Pair domination | `erdos-turan-order`: pair corollary | Total prescribed length at most (n/2); enough for the first Poisson/Berry--Esseen transfer. |
| Polynomial intensity | `sharp-order-edgeworth`: polynomial block proposition | Linear logarithmic terminal depth; arbitrary fixed logarithmic accuracy. |
| Passive-mark Campbell--Stein | `sharp-order-edgeworth`: passive Stein / polynomial product-Poisson modules | Entire growing core plus an unchanged permutation-measurable mark; no quenched conditioning on that mark. The omitted-count specialization is re-derived in the total-cycle paper. |
| Fixed-order domination | `sharp-order-edgeworth`: multi-clock theorem and factorial-domination corollary | Fixed order (q) only, total prescribed length at most (n/2); used for higher moments and fixed-order expansions. |
| Discrete smoothing | internal to `total-cycle-edgeworth` | Taylor, Charlier, and smoothing lemmas are proved in the total-cycle paper and are not a Luce-model dependency. |

The total-cycle proof does not use the active macroscopic PD/GEM paper, regular-profile paper, or any endpoint-singular extraction.

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

No active-paper dependency. Its internal proof chain is:

1. exponential-race and Gumbel threshold identities;
2. Bernoulli concentration and the fixed-dimensional tilted lattice LLT;
3. uniform sampled-profile approximation and regular saddle geometry;
4. cumulative-count LLT, off-saddle exclusion, and integrated lattice saddle;
5. separated bulk multipoint estimate;
6. gap, endpoint, collision, and target-crowding envelopes;
7. fixed and mixed factorial moments plus the discrete total-variation upgrade;
8. bistochastic Hilbert--Schmidt kernel, cyclic trace formula, and exponential long-trace universality;
9. diagonal-band, sparse-entry, thin-graph, deterministic-overlap, and transverse-curve consequences.

External standard inputs include the identified Luce permuton density, standard Bernoulli/local-limit background, trace-ideal results, the multivariate method of moments, Scheffé's lemma, and a converging-together criterion. The manuscript supplies references. Its adversarial audit found no fatal gap and all six localized repairs have been applied and regression-checked.

### `macroscopic-pd`

No active-paper dependency. Its model-specific proof chain is internal:

1. subsequential marked-profile kernel and common (L^2) contraction;
2. slab law, deterministic good events, and conditional permanental factorization;
3. hereditary flatness and predictable adaptive exposure;
4. relative-prefix control;
5. scale-sensitive two-scale orbit balance;
6. root-avoiding change of measure and harmonic-product approximation;
7. conditional residual-fraction uniformity;
8. deletion stability for an interior macroscopic cycle;
9. finite-dimensional independent residual fractions;
10. (ell^1) tail restoration and decreasing rearrangement to GEM(1)/PD(1).

External standard inputs are weak compactness/disintegration, maximal inequalities, weak convergence and continuous mapping, the bounded-Lipschitz criterion, and the standard GEM/PD relation. Its adversarial audit found no fatal gap and all six localized repairs have been applied and regression-checked.

## External literature and provenance

Standard external references are not represented as document edges in `papers.json`. Each manuscript is responsible for citing the external probability, analysis, operator-theoretic, or permutation-limit input it actually uses.

The frozen 139-page source under `archive/6178a99/` is an immutable provenance source, not a proof dependency. No active proof may import the historical rejected total-cycle candidate. The five final thematic papers are self-contained extractions even where that means duplicating archived preliminaries.

No growing-number-of-roots theorem, arbitrary-deletion quenched theorem, profile smoothness assumption for the comparable-rate papers, endpoint-singular input for the regular-profile paper, or mod-Poisson convergence hypothesis has been silently added.

## Open dependency-sensitive targets

The sampled-profile mean constant, uniformly bounded arbitrary-array mean shift, higher factorial-cumulant limits, and locally uniform complex mod-Poisson residue remain open. None is an input to a current theorem.

The next controlled edits to the five audit-passed working extractions are their focused audit-repair PRs. Those repairs must not create new active-paper dependency edges unless such an edge is explicitly justified, documented here, and added to `papers.json`.
