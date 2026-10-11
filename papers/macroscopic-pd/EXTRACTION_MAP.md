# Macroscopic PD/GEM extraction map

This register covers the mechanical extraction from `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`, archived lines 2199--3565, into `papers/macroscopic-pd/poisson-dirichlet-luce.tex`. The archive is pinned at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

The complete macroscopic section is preserved in the standalone source up to whitespace: the repository regression test compares the non-whitespace TeX token stream between the archived section and the extracted section. All `\label` keys and the bibliography key are retained verbatim. The added abstract and model/status section are editorial wrappers; no proof statement or proof step inside the extracted section is changed.

## Theorem environments

| Kind | Archived number | Standalone number | Archived label | Standalone label | Archived line | Standalone line |
| --- | ---: | ---: | --- | --- | ---: | ---: |
| theorem | 6.1 | 2.1 | `thm:macroscopic-pd` | `thm:macroscopic-pd` | 2221 | 105 |
| lemma | 6.2 | 2.2 | `lem:pd-kernel-contraction` | `lem:pd-kernel-contraction` | 2296 | 180 |
| lemma | 6.3 | 2.3 | `lem:pd-slab-law` | `lem:pd-slab-law` | 2404 | 288 |
| lemma | 6.4 | 2.4 | `lem:pd-residual-factorization` | `lem:pd-residual-factorization` | 2529 | 413 |
| lemma | 6.5 | 2.5 | `lem:pd-hereditary-flatness` | `lem:pd-hereditary-flatness` | 2545 | 429 |
| lemma | 6.6 | 2.6 | `lem:pd-predictable-exposure` | `lem:pd-predictable-exposure` | 2586 | 470 |
| lemma | 6.7 | 2.7 | `lem:pd-relative-prefix` | `lem:pd-relative-prefix` | 2626 | 510 |
| lemma | 6.8 | 2.8 | `lem:pd-two-scale-balance` | `lem:pd-two-scale-balance` | 2821 | 705 |
| lemma | 6.9 | 2.9 | `lem:pd-root-avoiding` | `lem:pd-root-avoiding` | 2995 | 879 |
| lemma | 6.10 | 2.10 | `lem:pd-harmonic-product` | `lem:pd-harmonic-product` | 3033 | 917 |
| proposition | 6.11 | 2.11 | `prop:pd-uniform-residual-fraction` | `prop:pd-uniform-residual-fraction` | 3060 | 944 |
| lemma | 6.12 | 2.12 | `lem:pd-deletion-stability` | `lem:pd-deletion-stability` | 3190 | 1074 |
| lemma | 6.13 | 2.13 | `lem:pd-cdf-test` | `lem:pd-cdf-test` | 3293 | 1177 |
| proposition | 6.14 | 2.14 | `prop:pd-residual-uniforms` | `prop:pd-residual-uniforms` | 3330 | 1214 |
| corollary | 6.15 | 2.15 | `cor:pd-power-sums` | `cor:pd-power-sums` | 3535 | 1419 |

## Structural and equation labels

| Kind | Archived label | Standalone label | Archived line | Standalone line |
| --- | --- | --- | ---: | ---: |
| section | `sec:macroscopic-cycles` | `sec:macroscopic-cycles` | 2200 | 84 |
| equation | `eq:pd-normalized-rates` | `eq:pd-normalized-rates` | 2264 | 148 |
| equation | `eq:pd-permanental-row` | `eq:pd-permanental-row` | 2523 | 407 |
| equation | `eq:pd-relative-prefix` | `eq:pd-relative-prefix` | 2647 | 531 |
| equation | `eq:pd-prefix-pi` | `eq:pd-prefix-pi` | 2668 | 552 |
| equation | `eq:pd-prefix-drift` | `eq:pd-prefix-drift` | 2685 | 569 |
| equation | `eq:pd-prefix-qv` | `eq:pd-prefix-qv` | 2693 | 577 |
| equation | `eq:pd-prefix-doob` | `eq:pd-prefix-doob` | 2703 | 587 |
| equation | `eq:pd-prefix-log` | `eq:pd-prefix-log` | 2709 | 593 |
| equation | `eq:pd-prefix-power` | `eq:pd-prefix-power` | 2717 | 601 |
| equation | `eq:pd-prefix-before-stop` | `eq:pd-prefix-before-stop` | 2728 | 612 |
| equation | `eq:pd-cycle-block-equality` | `eq:pd-cycle-block-equality` | 2771 | 655 |
| equation | `eq:pd-regular-history` | `eq:pd-regular-history` | 2783 | 667 |
| equation | `eq:pd-flow` | `eq:pd-flow` | 2817 | 701 |
| equation | `eq:pd-row-prefix` | `eq:pd-row-prefix` | 2836 | 720 |
| equation | `eq:pd-scale-sensitive-balance` | `eq:pd-scale-sensitive-balance` | 2849 | 733 |
| equation | `eq:pd-good-row-error` | `eq:pd-good-row-error` | 2891 | 775 |
| equation | `eq:pd-bad-row-error` | `eq:pd-bad-row-error` | 2900 | 784 |
| equation | `eq:pd-good-L2` | `eq:pd-good-L2` | 2913 | 797 |
| equation | `eq:pd-bad-L2-raw` | `eq:pd-bad-L2-raw` | 2924 | 808 |
| equation | `eq:pd-bad-L2` | `eq:pd-bad-L2` | 2931 | 815 |
| equation | `eq:pd-g-L2-scale` | `eq:pd-g-L2-scale` | 2946 | 830 |
| equation | `eq:pd-u-L2-scale` | `eq:pd-u-L2-scale` | 2956 | 840 |
| equation | `eq:pd-root-rn` | `eq:pd-root-rn` | 3006 | 890 |
| equation | `eq:pd-root-hazard` | `eq:pd-root-hazard` | 3015 | 899 |
| equation | `eq:pd-root-cdf` | `eq:pd-root-cdf` | 3076 | 960 |
| equation | `eq:pd-closure-tail` | `eq:pd-closure-tail` | 3092 | 976 |
| equation | `eq:pd-closure-size` | `eq:pd-closure-size` | 3098 | 982 |
| equation | `eq:pd-no-premature` | `eq:pd-no-premature` | 3130 | 1014 |
| equation | `eq:pd-closure-opportunities` | `eq:pd-closure-opportunities` | 3155 | 1039 |
| equation | `eq:pd-deletion-joint` | `eq:pd-deletion-joint` | 3204 | 1088 |
| equation | `eq:pd-deletion-error` | `eq:pd-deletion-error` | 3211 | 1095 |
| equation | `eq:pd-deleted-row-fraction` | `eq:pd-deleted-row-fraction` | 3240 | 1124 |
| equation | `eq:pd-deleted-cell-fraction` | `eq:pd-deleted-cell-fraction` | 3258 | 1142 |
| equation | `eq:pd-interior-history` | `eq:pd-interior-history` | 3391 | 1275 |
| equation | `eq:pd-stage-cdf` | `eq:pd-stage-cdf` | 3404 | 1288 |
| equation | `eq:pd-truncated-product` | `eq:pd-truncated-product` | 3450 | 1334 |
| equation | `eq:pd-actual-endpoints` | `eq:pd-actual-endpoints` | 3461 | 1345 |
| equation | `eq:pd-finite-gem` | `eq:pd-finite-gem` | 3496 | 1380 |
| equation | `eq:pd-tail-mass` | `eq:pd-tail-mass` | 3506 | 1390 |

## Explicit equation tags without `\label`

| Archived tag | Standalone tag | Content location |
| --- | --- | --- |
| `(6.1)` | `(6.1)` | Inner-column slab bound in Lemma `lem:pd-slab-law` |
| `(6.2)` | `(6.2)` | Hilbert--Schmidt block estimate in Lemma `lem:pd-slab-law` |
| `(6.3)` | `(6.3)` | Tail slab-mass estimate in Lemma `lem:pd-slab-law` |
| `(6.4)` | `(6.4)` | Definition `beta = 2 kappa h` in Lemma `lem:pd-hereditary-flatness` |

## Cross-references and bibliography

- Internal `\ref`/`\eqref` targets: 43 distinct keys; every target is present in the extracted section.
- Missing internal targets: `[]`.
- Bibliographic key `Pitman2006` is retained and is the only citation in the extracted section.
- No active manuscript in `papers.json` is imported by the proof. Standard probabilistic and measure-theoretic inputs are listed explicitly in Section 1 of the standalone manuscript.

## Status boundary

This map certifies extraction coverage only. It is not a mathematical audit of the clock-slab conditioning, rooted closure argument, deletion stability, regeneration, GEM induction, or `ell^1` tail restoration. Those questions remain assigned to the separate audit stage recorded in Issue #4.

