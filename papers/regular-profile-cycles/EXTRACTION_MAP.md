# Regular-profile extraction map

Frozen source:
`archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`

Frozen source SHA-256: `c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028`.

The three mathematical blocks were initially copied byte-for-byte. Following the adversarial audit, the active source differs only by the marked clarification blocks documented in `audits/regular-profile-repair-record.md`. Removing those marked blocks recovers the original archived mathematical blocks byte-for-byte; labels are unchanged.

## Source ranges

| Block | Archived lines | Active sentinel |
| --- | ---: | --- |
| Exponential race and Gumbel input | 224--336 | `% BEGIN ARCHIVED BLOCK: exponential-race-and-gumbel-input` |
| Analytic input | 353--531 | `% BEGIN ARCHIVED BLOCK: analytic-input` |
| Regular-profile theory | 865--2198 | `% BEGIN ARCHIVED BLOCK: regular-positive-profile-theory` |

## Theorem and lemma provenance

Labels are unchanged, so every old label is also the current label.

| Environment | Title | Old label = current label | Archived line | Current active line |
| --- | --- | --- | ---: | ---: |
| Lemma | Gumbel threshold identities | `lem:gumbel-threshold-identities` | 260 | 135 |
| Lemma | Point probability and Bernstein bounds | `lem:bernstein-point` | 356 | 218 |
| Lemma | Uniform lattice local CLT with a tilted local bound | `lem:llt` | 378 | 240 |
| Theorem | Regular-profile fixed points and short cycles | `thm:regular-cycles` | 925 | 457 |
| Lemma | Uniform saddle geometry | `lem:regular-saddle-geometry` | 952 | 510 |
| Lemma | Uniform LLT for Luce cumulative counts | `lem:luce-cumulative-llt` | 1010 | 568 |
| Lemma | Off-saddle exclusion | `lem:regular-off-saddle` | 1096 | 654 |
| Lemma | Gaussian-scale saddle tail | `lem:regular-gaussian-tail` | 1124 | 682 |
| Lemma | Uniform integrated lattice saddle | `lem:integrated-lattice-saddle` | 1178 | 736 |
| Proposition | Separated bulk local estimate | `prop:bulk-local-final` | 1252 | 810 |
| Lemma | One-point rank envelope | `lem:one-rank-envelope` | 1348 | 922 |
| Lemma | Gap envelope | `lem:gap-envelope` | 1395 | 969 |
| Lemma | Summability of the gap envelope | `lem:gap-sum` | 1418 | 992 |
| Lemma | Endpoint domination | `lem:endpoint-dom` | 1494 | 1079 |
| Lemma | Bulk collision domination | `lem:collision-dom` | 1523 | 1108 |
| Corollary | Endpoint tightness and improper integrability | `cor:endpoint-tightness` | 1552 | 1137 |
| Proposition | Fixed-point factorial moments | `prop:regular-fixed-factorial` | 1600 | 1191 |
| Proposition | Mixed short-cycle factorial moments | `prop:regular-cycle-factorial` | 1633 | 1224 |
| Corollary | Total-variation convergence for fixed cycle vectors | `cor:regular-cycles-tv` | 1697 | 1307 |
| Lemma | Bistochastic Hilbert--Schmidt kernel | `lem:bistochastic-hs` | 1734 | 1349 |
| Lemma | Cyclic trace formula | `lem:cyclic-trace-formula` | 1791 | 1406 |
| Theorem | Long trace universality | `thm:long-trace` | 1817 | 1432 |
| Theorem | Fixed-width diagonal bands | `thm:diagonal-band` | 1904 | 1538 |
| Theorem | Sparse bulk entry sets | `thm:sparse-entry` | 1976 | 1610 |
| Corollary | General thin-graph Poisson law | `cor:thin-graph-general` | 2075 | 1717 |
| Corollary | Overlaps with deterministic permutations | `cor:overlap-permutation` | 2111 | 1753 |
| Theorem | Transverse thin-curve Poisson law | `thm:thin-curve-transverse` | 2167 | 1815 |

## Closure and repair checks

- original theorem/proposition/lemma/corollary environments: **27**;
- original labels: **33**;
- original distinct internal reference targets: **21**;
- original cited bibliography keys: **3**;
- unresolved internal references in the active source: **0**;
- active-paper proof dependencies: **0**;
- audit-approved repair sets: **6**, represented by marked passages and checked in CI;
- removing the marked repair passages restores the original three mathematical blocks byte-for-byte.

This map records provenance and scope preservation. The mathematical verdict is in `audits/regular-profile-proof-audit.md`.
