# Mathematical dependency map

The catalog records document-level input edges and tests reject cycles. References for historical context or later applications are not proof dependencies. The precise modules below determine the review boundary.

## Macroscopic PD/GEM extraction

The standalone paper `papers/macroscopic-pd/poisson-dirichlet-luce.tex` is mechanically extracted from archived lines 2199--3565. It has no proof dependency on another active manuscript in `papers.json` and does not use the mesoscopic-cycle theorem, scalar or functional Erdős--Turán laws, total-cycle CLT, or quantitative total-cycle results.

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

All ten components are stated and proved in the standalone source. The external inputs are standard compactness and disintegration on compact standard Borel spaces, Kolmogorov's maximal inequality, Doob's `L^2` maximal inequality, the continuous mapping theorem, and the standard relation between GEM(1) and PD(1), cited to Pitman. The [extraction map](papers/macroscopic-pd/EXTRACTION_MAP.md) records every moved label and reference. The regression test compares the archived and standalone macroscopic-section TeX token streams up to whitespace.

This dependency closure is an extraction statement, not a proof-audit verdict. In particular, it does not certify the conditioning sigma-field, uniformity over adaptive histories, rooted closure estimate, deletion/regeneration induction, or `ell^1` passage.

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
