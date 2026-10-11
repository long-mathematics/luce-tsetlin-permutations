# Mathematical dependency map

The catalog records document-level input edges and tests reject cycles. References for historical context or later applications are not proof dependencies. The precise modules below determine the review boundary.

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

The 139-page research draft is outside the total-cycle proof chain. The historical resolution candidate is never a dependency. No growing-number-of-roots, arbitrary-deletion quenched, profile smoothness, or mod-Poisson convergence hypothesis has been silently added. Distributional convergence alone does not imply unbounded moment convergence; the higher-order count theorem supplies the necessary moment estimates explicitly.
