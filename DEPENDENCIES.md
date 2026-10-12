# Mathematical dependency map

The catalog records document-level input edges and tests reject cycles. References for historical context or later applications are not proof dependencies. The precise modules below determine the review boundary.

## Boundary-laws extraction

The standalone boundary paper has no proof dependency on another active manuscript. Its internal chain consists of the exponential-race identity, vanishing-block construction, exact top-window likelihood comparison, finite-volume bottom-window convergence, and Borel--Cantelli/infinite-product leakage argument. The extraction is byte-preserving. The adversarial audit found no fatal gap and records six localized clarifications; those repairs remain deferred, so the paper stays a working mechanical extraction.

## Sukhatme fixed-point extraction

The standalone Sukhatme paper has no active-paper dependency. Its internal chain consists of exponential/Gumbel identities, the fixed-dimensional tilted LLT, death-process product bound, one- and multipoint terminal saddles, anisotropic localization, the separated joint estimate, and factorial-moment summation. The extraction is byte-preserving. The adversarial audit found no fatal gap and records six localized clarifications; repairs remain deferred.

## Endpoint-Regular Fixed-Point Universality extraction

The standalone endpoint-universality paper is self-contained: exponential/Gumbel and lattice-LLT inputs, the shared anisotropic Fourier/tilting toolkit, regularly varying endpoint sums, endpoint saddle/localization, factorial moments, tangent measure, kernel semigroup, and microscopic limit are internal. The extraction is byte-preserving. The independent audit found no fatal gap and records six localized clarifications; repairs remain deferred.

## Global Endpoint Poisson Approximation extraction

The standalone global endpoint paper includes the complete endpoint-regular framework and then the approximate-Palm Stein argument, exact swap likelihood ratio, quantitative one-dimensional saddle, swap--Palm comparison, and two-cycle summability. It has no active-paper dependency and is byte-preserving. The independent audit found no fatal gap and records six localized clarifications; repairs remain deferred.

## Endpoint Short Cycles extraction

The standalone endpoint-short-cycle paper includes the endpoint-regular framework and the full source-to-target saddle, scheduled-deletion envelope, multiplicative trace, and factorial-moment machinery. It has no active-paper dependency and is byte-preserving. The independent audit found no fatal gap and records six localized clarifications; repairs remain deferred.

## Regular-profile microscopic-cycle manuscript

The standalone paper `papers/regular-profile-cycles/regular-profile-cycles.tex`
has no proof dependency on another active manuscript in `papers.json` and does
not use the macroscopic, mesoscopic, order, or total-cycle theorems.

Its internal model-specific proof chain is:

1. exponential-race and Gumbel threshold identities;
2. Bernoulli point-probability/Bernstein bounds and the fixed-dimensional
   tilted lattice local limit theorem;
3. uniform sampled-profile approximation, regular saddle geometry, cumulative
   count local limits, and off-saddle exclusion;
4. the integrated lattice saddle and separated bulk multipoint estimate;
5. gap, endpoint, collision, and target-crowding envelopes;
6. fixed-order factorial-moment summation and fixed-vector total variation;
7. bistochasticity, Hilbert--Schmidt compactness, the cyclic trace formula, and
   exponential long-trace universality;
8. diagonal-band, sparse-entry, thin-graph, deterministic-overlap, and
   transverse-curve consequences.

The external inputs are the identified Luce permuton density of
Borga--Chatterjee--Diaconis, standard Bernoulli/local-limit background from
Petrov, trace-ideal results from Simon, and standard method-of-moments,
Scheffe, and converging-together criteria now cited to Billingsley. Every
model-specific estimate used in a theorem statement remains in the standalone
source.

The adversarial audit in `audits/regular-profile-proof-audit.md` found no fatal
gap. The six localized clarification sets in
`audits/regular-profile-repair-record.md` do not alter theorem scope. The
repair regression check removes the marked clarification blocks and recovers
the original three archived mathematical blocks byte-for-byte, while separately
checking that all repair markers and principal theorem statements remain
present.

## Macroscopic PD/GEM extraction

The standalone paper `papers/macroscopic-pd/poisson-dirichlet-luce.tex` was mechanically extracted from archived lines 2199--3565 and then revised only by the six localized clarifications listed in `audits/macroscopic-pd-repair-record.md`. It has no proof dependency on another active manuscript in `papers.json` and does not use the mesoscopic-cycle theorem, scalar or functional Erdős--Turán laws, total-cycle CLT, or quantitative total-cycle results.

Its model-specific dependency chain is internal:

1. subsequential marked-profile kernel and common `L^2` contraction;
2. slab law, deterministic good events, and conditional permanental row factorization;
3. hereditary flatness and predictable adaptive row exposure;
4. the quantitative relative-prefix law;
5. scale-sensitive two-scale orbit balance for regular residual histories;
6. root-avoiding change of measure and harmonic-product approximation;
7. uniform conditional residual-fraction law;
8. deletion stability for an interior macroscopic cycle;
9. finite-dimensional independent residual fractions;
10. `ell^1` tail restoration and decreasing rearrangement to GEM(1)/PD(1).

All ten components are stated and proved in the standalone source. The external inputs are weak compactness and disintegration on standard Borel spaces, Kolmogorov's and Doob's maximal inequalities, weak convergence and continuous mapping, the bounded-Lipschitz criterion, and the standard relation between GEM(1) and PD(1); the manuscript now gives textbook references for each. The [extraction map](papers/macroscopic-pd/EXTRACTION_MAP.md) records every moved label and reference, while the [repair record](audits/macroscopic-pd-repair-record.md) records every post-extraction clarification.

The adversarial audit found no fatal gap in this chain. Its verdict is internal and scoped: it does not assert a rate, arbitrary-history quenched uniformity, endpoint-singular macroscopic universality, or any theorem outside the displayed chain. The repair checker verifies that all original theorem labels and internal references remain present, the main theorem scope is unchanged, and all six audit findings are represented in the active source.

## Count proof

| Input | Source | Scope actually used |
| --- | --- | --- |
| Exact marked swap and selected tails | `mesoscopic-switching`: `prop:master-switch`, `cor:selected-moments` | Permutation-measurable tests; selected p>1 depends only on the rate ratio. |
| Internal short-root bound | `mesoscopic-switching`: `cor:root-crude` | No macroscopic PD/GEM input. |
| Free-depth endpoint estimate | `mesoscopic-switching`: `prop:endpoint-mixing` | Fixed one/two roots, mean conditional TV relative to the coarse environment. |
| Uniform truncations | `mesoscopic-switching`: `cor:quantitative-truncation-interface` | One factor costs A times the error, two factors A squared; shared-clock fresh second moment is E[D squared], not (ED) squared. |
| Polynomial intensity | `sharp-order-edgeworth`: `prop:poly-block` | Linear logarithmic terminal depth; arbitrary fixed logarithmic accuracy. |
| Passive-mark Campbell–Stein | `sharp-order-edgeworth`: `lem:passive-Stein`, `thm:poly-pp` | Entire growing core and an unchanged permutation-measurable mark; no quenched conditioning on that mark. Re-derived for the omitted count in the new paper. |
| Pair domination | `erdos-turan-order`: `cor:pair` | Total prescribed length at most n/2; enough for first Poisson/BE transfer. |
| Fixed-order domination | `sharp-order-edgeworth`: `thm:multiclock`, `cor:factorial-domination` | Fixed q only, total length at most n/2; needed for higher moments/expansions. |
| Discrete smoothing | `total-cycle-edgeworth`: `lem:taylor`, `lem:charlier`, `lem:smooth2` | Full proofs in the new paper; independent of the Luce model. |

The new count manuscript depends on these modules of the quantitative-order paper, **not** on its prime-power linearization, high-frequency arithmetic analysis, or nonlinear order-Edgeworth conclusions. Narrowing the endpoint-interface wording to its actually proved annealed scope does not change any estimate used in the count transfer.

## Functional proof

The qualitative functional manuscript uses square-root-depth unweighted dyadic summability, Campbell–Stein, the independent Poisson functional CLT, and uniform omitted-cycle restoration. Its count-only CLT is independent of the scalar arithmetic theorem. The joint logarithmic-order coordinate additionally imports `cor:product-lcm` from the scalar order paper. The explicit total-count mean estimate uses the exact mean-switch identity, not TV moment transfer.

## Archive and prohibited dependencies

The frozen 139-page source remains outside the total-cycle proof chain. The active macroscopic manuscript is an extraction from that archive, not an input to the count proof. The historical resolution candidate is never a dependency. No growing-number-of-roots, arbitrary-deletion quenched, profile smoothness, or mod-Poisson convergence hypothesis has been silently added. Distributional convergence alone does not imply unbounded moment convergence; the higher-order count theorem supplies the necessary moment estimates explicitly.
