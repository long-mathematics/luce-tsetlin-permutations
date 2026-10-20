# Macroscopic PD/GEM mechanical extraction record

**Supersession notice — 20 October 2026.** This historical record concerns the comparable-rate predecessor. Its repaired source, PDF, and extraction map are now [preserved byte-for-byte](../archive/macroscopic-pd-comparable/README.md). The active `macroscopic-pd` manuscript is the [spectral replacement](../papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex); see its [separate audit](spectral-pd-proof-audit.md) and [theorem migration map](../papers/macroscopic-pd/THEOREM_MIGRATION.md). The dated findings, hashes, and paths below describe the historical version.

Date: 11 October 2026.

This record documents extraction coverage and build integrity. It is **not** a mathematical audit, referee report, novelty certification, or formal proof verification.

## Source and destination

- Frozen source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`
- Frozen source commit: `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`
- Extracted archived range: lines 2199--3565, from `sec:macroscopic-cycles` through `cor:pd-power-sums`
- Active destination: `papers/macroscopic-pd/poisson-dirichlet-luce.tex`
- Old-label/new-label map: `papers/macroscopic-pd/EXTRACTION_MAP.md`

No file under `archive/` is changed by this extraction.

## Preserved mathematical scope

The standalone theorem retains exactly the archived hypotheses and conclusions:

- positive Luce rates with a uniformly bounded largest-to-smallest ratio;
- ranked normalized cycle lengths converging to `PD(1)` in the decreasing `ell^1` simplex;
- size-biased deletion-order normalized cycle lengths converging to `GEM(1)` in `ell^1`;
- the normalized cycle length of a uniform label converging to `Unif(0,1)`;
- the archived power-sum corollary for every fixed exponent greater than one.

The extraction does not replace any regeneration step by a total-cycle theorem, does not add a quenched arbitrary-deletion assertion, and does not strengthen the topology or uniformity.

## Completeness checks

The standalone source includes every model-specific theorem, proposition, and lemma used by the archived proof. The proof chain is internal: marked kernel contraction; slab law; residual permanental factorization; hereditary flatness; predictable exposure; relative-prefix law; two-scale balance; root-avoiding closure; conditional residual fraction; deletion stability; finite-dimensional residual uniforms; and `ell^1` restoration.

The regression test `tests/test_macroscopic_extraction.py` performs the following checks against the immutable archive on every CI run:

1. compares the complete non-whitespace TeX token stream of the archived and extracted macroscopic sections;
2. compares all `label`, `ref`/`eqref`, and citation-key sets;
3. checks that every internal cross-reference target is present;
4. checks that the extraction map contains every moved label;
5. checks that the active source remains explicitly marked `audit pending` and does not import the total-cycle CLT.

The extraction contains 55 retained labels, 43 distinct internal reference targets, and one retained bibliographic key, `Pitman2006`. Explicit unlabelled tags `(6.1)`--`(6.4)` are also recorded in the map.

## Local build and visual review

The standalone source was compiled from a clean directory with TeX Live 2025 using the repository's deterministic environment:

- `SOURCE_DATE_EPOCH=1791504000`
- `FORCE_SOURCE_DATE=1`
- `TZ=UTC`
- `latexmk -pdf -g -interaction=nonstopmode -halt-on-error -file-line-error -latexoption=-no-shell-escape`

Results:

- PDF pages: 20
- source SHA-256: `a14de186ecc0fdb48763bebf260ca56755bc6670570c31bfbce6c419c2f9f73e`
- PDF SHA-256: `c862c0f825a63233409bbd018c61d74fd32b061a1375573ab7790b8559235b56`
- deterministic clean rebuild: byte-identical
- undefined references/citations: none
- multiply defined labels: none
- overfull boxes: none

All 20 pages were rendered at 130 DPI and inspected as a contact sheet. The title page and representative proof pages were also inspected at full size. No clipping, overlap, missing glyph, broken display, or obvious layout failure was found.

## Deliberately deferred proof questions

The following are assigned to the separate adversarial audit and are not certified here:

- whether the conditioned slab data leave precisely the randomness later used;
- whether all adaptive explorations satisfy the claimed uniform relative-prefix event;
- whether the dependently selected closure row is controlled at the required scale;
- whether the residual-history regularity class is preserved under actual cycle deletion;
- whether the parameter hierarchy closes without circular uniformity;
- whether finite-dimensional residual fractions and residual-mass estimates give the stated `ell^1` convergence;
- whether every standard imported fact is invoked under its exact hypotheses.

The paper remains a **working mechanical extraction** until that separate audit and any resulting repair PR are completed.
