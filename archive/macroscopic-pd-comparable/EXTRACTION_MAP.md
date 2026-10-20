# Macroscopic PD/GEM extraction map

This register covers the mechanical extraction from `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`, archived lines 2199--3565, into `papers/macroscopic-pd/poisson-dirichlet-luce.tex`. The archive is pinned at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

The initial mechanical extraction preserved the complete macroscopic section up to whitespace. After the separate adversarial audit, the active source received exactly six localized clarification repairs: an explicit reduced-conditioning derivation, expanded post-stopping cases and a small-`beta` choice, a GEM stage table, an explicit bounded-Lipschitz `ell^1` truncation estimate with independent residual-root wording, a power-sum wording correction, and textbook references for standard imports. All original theorem and equation labels remain unchanged. The repair checker verifies theorem scope, labels, references, and the presence of every audited clarification; the frozen archive remains byte-identical.

## Theorem environments

| Kind | Archived number | Standalone number | Archived label | Standalone label | Archived line | Standalone line |
| --- | ---: | ---: | --- | --- | ---: | ---: |
| theorem | 6.1 | 2.1 | `thm:macroscopic-pd` | `thm:macroscopic-pd` | 2221 | 112 |
| lemma | 6.2 | 2.2 | `lem:pd-kernel-contraction` | `lem:pd-kernel-contraction` | 2296 | 188 |
| lemma | 6.3 | 2.3 | `lem:pd-slab-law` | `lem:pd-slab-law` | 2404 | 296 |
| lemma | 6.4 | 2.4 | `lem:pd-residual-factorization` | `lem:pd-residual-factorization` | 2529 | 432 |
| lemma | 6.5 | 2.5 | `lem:pd-hereditary-flatness` | `lem:pd-hereditary-flatness` | 2545 | 448 |
| lemma | 6.6 | 2.6 | `lem:pd-predictable-exposure` | `lem:pd-predictable-exposure` | 2586 | 489 |
| lemma | 6.7 | 2.7 | `lem:pd-relative-prefix` | `lem:pd-relative-prefix` | 2626 | 529 |
| lemma | 6.8 | 2.8 | `lem:pd-two-scale-balance` | `lem:pd-two-scale-balance` | 2821 | 746 |
| lemma | 6.9 | 2.9 | `lem:pd-root-avoiding` | `lem:pd-root-avoiding` | 2995 | 920 |
| lemma | 6.10 | 2.10 | `lem:pd-harmonic-product` | `lem:pd-harmonic-product` | 3033 | 958 |
| proposition | 6.11 | 2.11 | `prop:pd-uniform-residual-fraction` | `prop:pd-uniform-residual-fraction` | 3060 | 985 |
| lemma | 6.12 | 2.12 | `lem:pd-deletion-stability` | `lem:pd-deletion-stability` | 3190 | 1115 |
| lemma | 6.13 | 2.13 | `lem:pd-cdf-test` | `lem:pd-cdf-test` | 3293 | 1219 |
| proposition | 6.14 | 2.14 | `prop:pd-residual-uniforms` | `prop:pd-residual-uniforms` | 3330 | 1256 |
| corollary | 6.15 | 2.15 | `cor:pd-power-sums` | `cor:pd-power-sums` | 3535 | 1496 |

## Structural and equation labels

| Kind | Archived label | Standalone label | Archived line | Standalone line |
| --- | --- | --- | ---: | ---: |
| section | `sec:macroscopic-cycles` | `sec:macroscopic-cycles` | 2200 | 91 |
| equation | `eq:pd-normalized-rates` | `eq:pd-normalized-rates` | 2264 | 156 |
| equation | `eq:pd-permanental-row` | `eq:pd-permanental-row` | 2523 | 425 |
| equation | `eq:pd-relative-prefix` | `eq:pd-relative-prefix` | 2647 | 550 |
| equation | `eq:pd-prefix-pi` | `eq:pd-prefix-pi` | 2668 | 571 |
| equation | `eq:pd-prefix-drift` | `eq:pd-prefix-drift` | 2685 | 588 |
| equation | `eq:pd-prefix-qv` | `eq:pd-prefix-qv` | 2693 | 596 |
| equation | `eq:pd-prefix-doob` | `eq:pd-prefix-doob` | 2703 | 606 |
| equation | `eq:pd-prefix-log` | `eq:pd-prefix-log` | 2709 | 612 |
| equation | `eq:pd-prefix-power` | `eq:pd-prefix-power` | 2717 | 626 |
| equation | `eq:pd-prefix-before-stop` | `eq:pd-prefix-before-stop` | 2728 | 637 |
| equation | `eq:pd-cycle-block-equality` | `eq:pd-cycle-block-equality` | 2771 | 696 |
| equation | `eq:pd-regular-history` | `eq:pd-regular-history` | 2783 | 708 |
| equation | `eq:pd-flow` | `eq:pd-flow` | 2817 | 742 |
| equation | `eq:pd-row-prefix` | `eq:pd-row-prefix` | 2836 | 761 |
| equation | `eq:pd-scale-sensitive-balance` | `eq:pd-scale-sensitive-balance` | 2849 | 774 |
| equation | `eq:pd-good-row-error` | `eq:pd-good-row-error` | 2891 | 816 |
| equation | `eq:pd-bad-row-error` | `eq:pd-bad-row-error` | 2900 | 825 |
| equation | `eq:pd-good-L2` | `eq:pd-good-L2` | 2913 | 838 |
| equation | `eq:pd-bad-L2-raw` | `eq:pd-bad-L2-raw` | 2924 | 849 |
| equation | `eq:pd-bad-L2` | `eq:pd-bad-L2` | 2931 | 856 |
| equation | `eq:pd-g-L2-scale` | `eq:pd-g-L2-scale` | 2946 | 871 |
| equation | `eq:pd-u-L2-scale` | `eq:pd-u-L2-scale` | 2956 | 881 |
| equation | `eq:pd-root-rn` | `eq:pd-root-rn` | 3006 | 931 |
| equation | `eq:pd-root-hazard` | `eq:pd-root-hazard` | 3015 | 940 |
| equation | `eq:pd-root-cdf` | `eq:pd-root-cdf` | 3076 | 1001 |
| equation | `eq:pd-closure-tail` | `eq:pd-closure-tail` | 3092 | 1017 |
| equation | `eq:pd-closure-size` | `eq:pd-closure-size` | 3098 | 1023 |
| equation | `eq:pd-no-premature` | `eq:pd-no-premature` | 3130 | 1055 |
| equation | `eq:pd-closure-opportunities` | `eq:pd-closure-opportunities` | 3155 | 1080 |
| equation | `eq:pd-deletion-joint` | `eq:pd-deletion-joint` | 3204 | 1129 |
| equation | `eq:pd-deletion-error` | `eq:pd-deletion-error` | 3211 | 1136 |
| equation | `eq:pd-deleted-row-fraction` | `eq:pd-deleted-row-fraction` | 3240 | 1165 |
| equation | `eq:pd-deleted-cell-fraction` | `eq:pd-deleted-cell-fraction` | 3258 | 1183 |
| equation | `eq:pd-interior-history` | `eq:pd-interior-history` | 3391 | 1331 |
| equation | `eq:pd-stage-cdf` | `eq:pd-stage-cdf` | 3404 | 1344 |
| equation | `eq:pd-truncated-product` | `eq:pd-truncated-product` | 3450 | 1390 |
| equation | `eq:pd-actual-endpoints` | `eq:pd-actual-endpoints` | 3461 | 1401 |
| equation | `eq:pd-finite-gem` | `eq:pd-finite-gem` | 3496 | 1436 |
| equation | `eq:pd-tail-mass` | `eq:pd-tail-mass` | 3506 | 1446 |

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
- Bibliographic key `Pitman2006` is retained. The audited wrapper adds `Kallenberg2002`, `Durrett2019`, `Billingsley1999`, and `Dudley2002` for the standard external inputs.
- No active manuscript in `papers.json` is imported by the proof. Standard probabilistic and measure-theoretic inputs are listed explicitly in Section 1 of the standalone manuscript.

## Status boundary

This map certifies extraction coverage and records the boundary between the frozen source and the audited active paper. The separate [proof audit](../../audits/macroscopic-pd-proof-audit.md) gives the mathematical verdict, and the [repair record](../../audits/macroscopic-pd-repair-record.md) identifies how each localized finding was resolved. Neither document is formal verification or independent external refereeing.

