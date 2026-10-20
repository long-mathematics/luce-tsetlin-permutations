# Spectral PD(1) / Sukhatme proof and integration record

Status date: 20 October 2026.

This records the internal AI-assisted proof review, five mathematical repairs, two proved theorem promotions, and subsequent editorial review of the spectral manuscript. Separate internal reviews examined the dependency boundary, regeneration argument, and spectral-gap proofs. These reviews are not independent external refereeing, formal verification, or novelty certification.

## Source and provenance

- Active source: [`papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex`](../papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex).
- Active PDF: [`output/pdf/spectral-poisson-dirichlet-luce.pdf`](../output/pdf/spectral-poisson-dirichlet-luce.pdf).
- Stable catalog ID: `macroscopic-pd`.
- Approved source integration commit: `81462993a7400f972a3d75583d447fbeccf1e7b3`; both downstream citations are pinned to this source.
- Approved revised source SHA-256: `06e4c2487c6b5af6ed89b55a58637ff87adf80a583e418dae2a07ab2b5170c49`.
- Preserved comparable-rate predecessor: [source](../archive/macroscopic-pd-comparable/poisson-dirichlet-luce.tex), [PDF](../archive/macroscopic-pd-comparable/poisson-dirichlet-luce.pdf), and [extraction map](../archive/macroscopic-pd-comparable/EXTRACTION_MAP.md).

The spectral paper cites the earlier comparable-rate manuscript at a [pinned repository revision](https://github.com/long-mathematics/luce-tsetlin-permutations/blob/25b7e4490c32418b818b2356106228283986dd6c/papers/macroscopic-pd/poisson-dirichlet-luce.tex). Its introduction identifies the inherited clock-slab, residual permanental, adaptive-prefix, and regeneration arguments and reproduces their necessary proofs. Channel domination, late-row contraction without Hilbert–Schmidt control, and endpoint spectral-gap criteria are the additional ingredients. Corollary 8.1 recovers the predecessor's full comparable-array theorem.

The earlier [extraction](macroscopic-pd-extraction.md), [proof audit](macroscopic-pd-proof-audit.md), and [six-repair record](macroscopic-pd-repair-record.md) remain historical records of the predecessor. The five repairs below concern the spectral draft and are a separate review. Exact interface migration is recorded in [the theorem map](../papers/macroscopic-pd/THEOREM_MIGRATION.md).

## Full theorem scope retained

Theorem 1.1 (`thm:main-spectral`) assumes convergence of the empirical rates normalized by their maximum to a law with no atom at zero and strict mean-zero exponential-channel norm $q(ν)<1$. It gives GEM(1) and ranked PD(1) convergence in $\ell^1$, and a Uniform(0,1) limit for the normalized cycle length of a uniform label. It imposes no regularity on deterministic assignments of rates to labels.

Corollary 1.2 (`cor:subsequential-spectral`) requires the same properties for every empirical limit point; it does not require a single empirical-law limit. Corollaries 1.3 and 1.4 give the stated random-environment extension and longest-cycle convergence with all positive moments. Theorem 1.5 and Corollaries 1.6–1.7 cover positive-index regularly varying lower tails, power spectra, and regularly varying sequences under arbitrary deterministic rearrangements. In particular, every rearrangement of the Sukhatme rates is covered.

## Confirmed proof chain

| Module | Reviewed conclusion |
| --- | --- |
| Channel factorization | The bistochastic marked kernel factors through the rate-observation channel; label–rate coupling cannot increase its mean-zero norm. |
| Slab compression | Random slab endpoints are controlled by maximal empirical estimates. The finite matrix is stochastic, has the stated stationary law, and inherits the spectral gap by compression. |
| Flatness and late rows | Permanent-minor comparison gives exact hereditary flatness in finite slabs. The row-block contraction charges late rows by the square root of their total mass and uses no global Hilbert–Schmidt assumption. |
| Orbit balance | The deterministic flow identity, finite-state resolvent, and inner-column Cauchy–Schwarz estimate yield the required scale-sensitive closure control. |
| Root and deletion | The repaired stopped survival weight, harmonic product, conditional root CDF, and joint-event deletion estimate apply on the stated good data and regular histories. |
| Regeneration and topology | The repaired cutoff order gives independent residual fractions; expected residual-mass control supplies the $\ell^1$ GEM and PD conclusions. |
| Spectral sufficient conditions | The regularly varying kernel bound and geometric Poincaré argument give a strict gap. The same mechanism proves the broader dyadic shell criterion. |

## Five mathematical repairs incorporated

1. **Finite closure slab.** Lemma `lem:root-avoiding` now assumes that the closure row has finite width at most the mesh when invoking `eq:root-hazard`. The hazard comparison is not applied to the unbounded tail row.
2. **Stopped auxiliary survival weight.** Equation `eq:root-survival-weight` defines the product on paths that complete at least the requested number of nonclosing edges, including equality at the stopping boundary, and gives weight zero to paths stopped earlier. The exact survival identity therefore includes auxiliary termination correctly.
3. **Good slab data for deletion.** Lemma `lem:deletion-stability` explicitly assumes the good slab event. Its conclusion remains a joint-event probability bound and is not obtained by conditioning on an exact cycle length.
4. **Separated error constants.** The root and deletion estimates distinguish the principal error coefficient, depending on the inner cutoff and interior parameters, from the fixed-partition coefficient multiplying $1/n$. This prevents partition-dependent constants from entering the cutoff-selection recursion.
5. **Complete propagated cutoff budget.** Proposition `prop:residual-uniforms` uses $A_j=\prod_{i=0}^{j}(1+R_i+D_i)$. It controls every later regularity multiplier and every root-law multiplier, including those originating at earlier levels. The cutoffs control the square-root tail terms; only after fixing them does the mesh control its own contributions, followed by the limit in $n$.

These repairs retain the hypotheses and conclusions of the main spectral criterion. They do not replace it with a comparable-rate or density-only theorem.

## Proved promotions and open boundary

**Theorem 9.1 (`thm:dyadic-doubling`)** proves that eventually positive dyadic shell masses with successive ratios bounded between constants $0<a\le b<1$ yield $q(ν)<1$. Atomic and singular laws are permitted.

**Theorem 9.2 (`thm:slow-boundary`)** proves that an eventually positive slowly varying lower tail tending to zero yields $q(ν)=1$. Its proof constructs rate-tail and clock-tail events whose correlation tends to one, using the index-zero Abelian theorem and the truncated first-moment estimate.

Neither theorem settles gap necessity for arrangement-uniform PD(1): that remains `q:sharpness` (Question 9.3). The other remaining labels are `q:log-linear-growth`, `conj:multiscale`, `q:quantitative`, and `q:exact-gap`. A channel norm of one is not asserted to imply failure of PD(1).

## Editorial and bibliographic corrections

The source explicitly credits the comparable-rate predecessor. The CDK reference is the published *Journal of Algebra* 655 (2024), 139–162 article, with its DOI; BCD is cited as *Annals of Applied Probability*, to appear, with the specified arXiv v3. The longest-cycle attribution distinguishes CDK's general question from its singled-out Sukhatme example.

The redundant empirical error term was removed from the principal error definition. The logarithmic Hilbert–Schmidt remark is restricted to the ordered coupling and its stated time truncation. The log-uniform example gives the explicit upper bound $1-q(ν_\beta)\le\pi^2/\beta^2$ rather than an ambiguous assertion of an exact decay order. The unsupported description of the relative-prefix lemma as “standard” was removed.

## Dependency and review boundary

The spectral proof is self-contained relative to the active Luce papers. Its predecessor citation supplies provenance rather than an unproved imported step. `mod-poisson` uses the comparable specialization of the original-measure uniform-root limit; `independence-peeling` uses conditional regular-history root and deletion estimates. The migration does not extend those papers' rate hypotheses. A separate focused review checked the maximum-normalized conditional errors, the empirical tail bound, the good slab event, and the full propagated cutoff budget in `independence-peeling`. Every principal theorem in both dependent papers is unchanged; among their labelled theorem/lemma/proposition/input statements, only `input:PD` in the independence paper changes.

No quantitative finite-size PD/GEM rate, arbitrary-history quenched theorem, general positive-array theorem, or multiscale conclusion is established. The random-rate corollary assumes independence from the exponential variables and convergence in probability of the empirical laws to a deterministic qualifying limit. It does not require independence among the rates.

## Validation record

Before repository integration, the approved revised source compiled to a 26-page PDF without unresolved references or citations, and all pages were rendered and visually inspected. The source digest above identifies that reviewed draft.

Repository integration validation passed:

- `make test`: 57 tests, including the spectral scope/promotion guards, historical predecessor checks, exact dependency labels, navigation and Markdown rendering, and actual builds in distinct checkout directories.
- `make pdf` and `make check`: all 16 active manuscripts compile with resolved references and citations; clean rebuilds match the committed snapshots byte-for-byte.
- `make verify`: all five registered finite and numerical consistency programs pass.
- All 40 pre-existing archive records and their file hashes are unchanged; three predecessor files were added to preservation. All 13 unaffected active PDFs remain byte-identical to the pre-integration snapshots.
- All 26 spectral pages, all 21 mod-Poisson pages, and all 18 independence pages were visually reviewed. Enlarged review covered the new criterion and both promoted theorems, every repaired proof region, migrated conditional estimates and cutoff induction, and updated bibliography entries. No clipping, overlap, missing glyph, unresolved-reference marker, or layout defect was found.

The build review exposed path-dependent default PDF trailer identifiers. The builder now supplies a stable identifier seed that reproduces the historical CI snapshots and respects an explicit identifier choice in a manuscript. Strict source/PDF hash comparisons are unchanged. Cross-directory build tests pass; the final metadata adjustment was verified to leave all reviewed PDF content unchanged.

The active spectral PDF has 26 pages and SHA-256 `1201e63b6dbf4d628a2c1abfc40ca5be3835971e6b83146da7f3e926308e840f`. Exact source/PDF hashes and page counts are in [the PDF manifest](../output/pdf/manifest.json); the [integration record](../notes/spectral-pd-integration-record.json) records the baseline, approved source, preservation, and validation scope. Compilation and regression checks do not substitute for the proof review described above.
