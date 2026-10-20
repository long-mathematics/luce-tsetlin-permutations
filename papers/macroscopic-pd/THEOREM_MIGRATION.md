# Comparable-rate PD/GEM to the spectral manuscript

Integration date: 20 October 2026.

The stable catalog ID is `macroscopic-pd`. Its sole active manuscript is now [Spectral Poisson–Dirichlet Universality for Luce Permutations under Arbitrary Rate Arrangements](spectral-poisson-dirichlet-luce.tex), with [PDF](../../output/pdf/spectral-poisson-dirichlet-luce.pdf). It strictly extends the comparable-rate theorem and reproduces the proof framework needed for its conditional interfaces.

The predecessor is preserved as [source](../../archive/macroscopic-pd-comparable/poisson-dirichlet-luce.tex), [PDF](../../archive/macroscopic-pd-comparable/poisson-dirichlet-luce.pdf), and [original extraction map](../../archive/macroscopic-pd-comparable/EXTRACTION_MAP.md). Its [extraction](../../audits/macroscopic-pd-extraction.md), [proof audit](../../audits/macroscopic-pd-proof-audit.md), and [repair record](../../audits/macroscopic-pd-repair-record.md) describe that historical version. They do not certify the additional spectral theorems. The [spectral audit](../../audits/spectral-pd-proof-audit.md) records the new proof scope and repairs.

## Theorem and interface map

| Comparable-rate label | Active spectral label | Meaning of the migration |
| --- | --- | --- |
| `thm:macroscopic-pd` | `thm:main-spectral` and `cor:comparable` | Theorem 1.1 gives the full spectral criterion; Corollary 8.1 recovers every comparable-rate array, including arrays without an empirical-law limit. |
| `lem:pd-kernel-contraction` | `lem:channel-domination` and `cor:comparable` | Channel factorization controls arbitrary label–rate couplings; the comparable-support common component verifies the channel gap in the old regime. |
| `lem:pd-slab-law` | `lem:slab-law` | Slab convergence and compression transfer the channel gap to the finite stochastic matrix. |
| `lem:pd-residual-factorization` | `lem:residual-factorization` | The exact conditional residual permanental factorization is retained. |
| `lem:pd-hereditary-flatness` | `lem:flatness` | Hereditary flatness is used in finite clock slabs. |
| `lem:pd-predictable-exposure` | `lem:predictable-exposure` | Predictable adaptive exposure preserves the conditional matching law. |
| `lem:pd-relative-prefix` | `lem:relative-prefix` | Relative prefix estimates remain uniform for the specified predictable explorations. |
| `lem:pd-two-scale-balance` | `lem:orbit-balance` | The new `lem:row-block-contraction` supplies late-row control without a Hilbert–Schmidt assumption. |
| `lem:pd-root-avoiding` | `lem:root-avoiding` | The stopped auxiliary survival weight is explicit; the hazard estimate assumes a finite closure slab. |
| `lem:pd-harmonic-product` | `lem:harmonic-product` | The interior harmonic-product estimate is retained. |
| `prop:pd-uniform-residual-fraction` | `prop:uniform-root-fraction` | Conditional residual-root uniformity holds on good slab data and regular histories. |
| `eq:pd-root-cdf` | `eq:root-cdf` | Conditional CDF error, with principal and fixed-partition errors separated. |
| `lem:pd-deletion-stability` | `lem:deletion-stability` | Joint-event deletion stability, explicitly on good slab data. |
| `eq:pd-deletion-error` | `eq:deletion-error` | The propagated regularity error retains a partition-independent principal coefficient. |
| `eq:pd-deletion-joint` | `eq:deletion-joint` | The bad-deletion probability is a joint-event bound, not conditioning on an exact cycle length. |
| `lem:pd-cdf-test` | `lem:cdf-test` | Conditional CDF testing is retained. |
| `prop:pd-residual-uniforms` | `prop:residual-uniforms` | Finite-dimensional independent residual fractions use the repaired cutoff budget. |
| `cor:pd-power-sums` | `cor:power-sums` | Power-sum convergence holds under the spectral criterion. |

## Downstream use

`mod-poisson` uses only the original-measure uniform-root limit from `thm:main-spectral`, specialized through `cor:comparable`. `independence-peeling` uses the stronger conditional factorization, root-CDF, and deletion interfaces named above. Their good-data and regular-history hypotheses remain part of those imports. The spectral extension does not change either downstream manuscript's profile or rate hypotheses.

## Added scope and remaining questions

`cor:subsequential-spectral` allows every empirical limit point to satisfy the criterion without requiring a single limiting law. `thm:rv-gap`, `cor:power-law-spectra`, and `cor:regularly-varying` cover positive-index regularly varying spectra and all deterministic rearrangements of Sukhatme rates. `cor:random-environment` gives the stated conditional-in-probability extension for random rates independent of the exponential variables, and `cor:longest-cycle` gives the longest-cycle law and all positive moments.

The proved promotions are `thm:dyadic-doubling` (Theorem 9.1) and `thm:slow-boundary` (Theorem 9.2). The latter establishes channel norm one for slowly varying lower tails; it does not establish failure of PD(1).

The remaining labels are `q:sharpness` (Question 9.3, gap necessity), `q:log-linear-growth` (Question 9.5), `conj:multiscale` (Conjecture 9.6), `q:quantitative` (Question 9.7), and `q:exact-gap` (Question 9.8). These are not promoted by this integration.
