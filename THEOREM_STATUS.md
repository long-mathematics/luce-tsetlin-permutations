# Theorem status

Status date: 20 October 2026.

This is the canonical theorem/review map for the active Luce/Tsetlin manuscript series. It separates **catalog status** (the machine-readable state in `papers.json`) from **mathematical review state**. Neither an internal audit nor CI is independent external refereeing or formal verification.

## Status vocabulary

The catalog uses exactly three active-document states:

- **`imported`**: provenance-preserved active source; no new full-paper review is implied.
- **`current-research`**: an active integrated research manuscript whose proof dependencies and review boundary are documented.
- **`working`**: an active manuscript that has not yet been promoted to current-research status.

The human review state is more precise:

- **Scoped review only**: named modules or interfaces have been checked, but no full-paper audit is claimed.
- **Current research / integrated review**: the active proof and named dependency interfaces are documented, but no end-to-end adversarial audit is claimed.
- **Audit passed, repairs pending**: an adversarial audit found no fatal gap, but its localized clarifications have deliberately not yet been applied; the catalog therefore remains `working`.
- **Audited current manuscript**: an adversarial audit found no fatal gap, all approved localized repairs were applied, and regression checks preserve theorem scope.
- **Historical rejected candidate**: preserved provenance that is explicitly excluded from active dependency chains.
- **Open**: a conjecture or research target not promoted as a theorem.

## Canonical manuscript-level map

The rows below are in the same order as `papers.json`. Every active manuscript appears exactly once.

| ID | Manuscript | Catalog status | Review state | Principal theorem package and scope |
| --- | --- | --- | --- | --- |
| `mesoscopic-switching` | Mesoscopic cycles of comparable-rate Luce permutations | `imported` | Scoped review only | For arbitrary comparable-rate triangular arrays, mesoscopic first moments are asymptotic to 1/r uniformly for r→∞ with r=o(n), and rescaled mesoscopic cycle lengths converge to the scale-invariant Poisson process. The marked switch, selected-factor estimates, and finite-endpoint interface are the reviewed modules used downstream. |
| `erdos-turan-order` | An Erdős–Turán Law for Comparable-Rate Luce Permutations | `imported` | Imported; no full-paper audit | The classical logarithmic-order CLT holds for arbitrary comparable-rate triangular arrays. The source is unchanged by later integration; downstream use is restricted to the named arithmetic/product--LCM modules recorded in `DEPENDENCIES.md`. |
| `sharp-order-edgeworth` | A Sharp Berry–Esseen Theorem and First Edgeworth Expansion for Logarithmic Luce Order | `imported` | Imported; nonlinear arithmetic not re-audited | Retains the sharp order Berry–Esseen and first Edgeworth assertions under comparable rates. Later work reuses named switching, intensity, and factorial-domination modules only; it does not certify the full nonlinear prime-power/arithmetic remainder argument. |
| `functional-erdos-turan` | Functional Erdős–Turán and Total-Cycle Laws for Luce Permutations | `current-research` | Current research / integrated review | Gives the bivariate functional count/order limit, total-cycle CLT, bounded logarithmic-scale Gaussian field, and joint endpoint law. The count-only branch and arithmetic order branch have distinct dependency boundaries. |
| `total-cycle-edgeworth` | Poisson Approximation and Lattice Edgeworth Expansions for Total Luce Cycles | `current-research` | Current research / integrated review | Gives exact-mean Poisson approximation, sharp normal approximation, first and second lattice Edgeworth expansions, variance control, and the fixed-order signed Poisson--Charlier hierarchy. Expansion order is fixed; no analytic mod-Poisson residue or limiting profile mean constant is inferred. |
| `mod-poisson` | An Exact Uniform Component and Analytic Mod-Poisson Convergence for Luce Permutations | `current-research` | Internally audited draft, with exact companion inputs and remaining external-review boundary recorded | Uniform local complex bound for arbitrary comparable rates; analytic mod-Poisson convergence for positive continuous profiles; exact-mean universal residue and universal fixed higher factorial cumulants. |
| `independence-peeling` | Microscopic–Macroscopic Independence and Poisson Peeling for Luce Permutations | `current-research` | Internally audited; targeted conditional-interface and switching review recorded | Under regular positive profiles, fixed short-cycle vectors and the entire ranked PD(1) partition converge jointly and independently, with mixed factorial moments. Comparable rates suffice for the finite two-annulus passive-mark comparison and fixed-order scalar peeling. The analytic PD cutoff law is in an independent appendix. |
| `boundary-laws` | Boundary Laws for Luce Rankings | `working` | **Working mechanical extraction; audit passed, repairs pending** | The vanishing-block obstruction, exact top-window total variation and relative defect, birthday transfer, finite bottom-window convergence, terminal leakage, and log-log phase diagram all passed adversarial audit within the archived scope. Audit-recorded clarifications remain deferred. |
| `bottom-window-universality` | Bottom-Window Universality for Permuton-Sampled Luce Permutations | `current-research` | Internally audited; prior-work and proof-scope review recorded | At an isolated regularly varying vanishing endpoint, the normalized clock sequence converges almost surely in c-zero and in the sharp summable ell-p range. Fixed bottom windows stabilize under the Poisson-spacings coupling and converge in quenched and annealed total variation. The paper also gives last-label laws and tails, a clock-value Poisson–Dirichlet corollary, exact-profile comparison, and a critical logarithmic extreme-value and label-scale theorem. |
| `sukhatme-fixed-points` | Sukhatme Fixed Points and the Terminal Poisson Process | `working` | **Working mechanical extraction; audit passed, repairs pending** | The death-process envelope, one- and multipoint terminal saddles, anisotropic local-limit/localization package, local terminal Poisson process, mean asymptotic, and fixed factorial moments passed adversarial audit. Audit-recorded clarifications remain deferred. |
| `endpoint-regular-universality` | Endpoint-Regular Fixed-Point Universality | `working` | **Working mechanical extraction; audit passed, repairs pending** | Endpoint fixed-point Poisson universality, factorial moments, displacement law, tangent measure, multiplicative endpoint kernel, diagonal traces, and microscopic endpoint-permutation limit passed adversarial audit. Audit-recorded clarifications remain deferred. |
| `global-endpoint-poisson` | Global Endpoint Poisson Approximation | `working` | **Working mechanical extraction; audit passed, repairs pending** | The endpoint framework, approximate-Palm Stein bound, exact rank-transposition likelihood ratio, quantitative saddle, swap--Palm comparison, two-cycle correction, explicit total-variation rate, and exact-mean normal corollary passed adversarial audit. Audit-recorded clarifications remain deferred. |
| `endpoint-short-cycles` | Endpoint Short Cycles | `working` | **Working mechanical extraction; audit passed, repairs pending** | The source-to-target endpoint saddle, anisotropic LLT/localization, global cycle envelope, logarithmic trace, negligible-configuration bounds, mixed factorial moments, and fixed-Lp law of large numbers passed adversarial audit. Audit-recorded clarifications remain deferred. |
| `regular-profile-cycles` | Microscopic Cycles and Sparse Entries for Regular Luce Profiles | `current-research` | **Audited current manuscript** | Under the exact sampled positive continuous-profile hypothesis, fixed cycle vectors converge to independent Poisson laws with cyclic-trace means; the means approach 1/r exponentially. The same paper gives diagonal-band, sparse-entry, thin-graph, deterministic-overlap, and transverse-curve laws. Audit-approved clarifications were applied and regression-checked. |
| `macroscopic-pd` | Spectral Poisson–Dirichlet Universality for Luce Permutations under Arbitrary Rate Arrangements | `current-research` | **Audited current manuscript** | The full mean-zero channel criterion gives GEM(1) and PD(1) convergence in ell-one and a uniform-root Uniform(0,1) limit for arbitrary deterministic rate assignments. Its subsequential form recovers all comparable arrays. Positive-index regularly varying spectra, including every Sukhatme rearrangement, satisfy the criterion. The dyadic-gap and slowly varying no-gap results are proved theorems. |

| `stratified-hammersley-lis` | Stratified Hammersley Laws for Luce Permutations | `current-research` | Internally audited, localized repairs incorporated; no external refereeing | A row-stratified Hammersley full shape-field theorem (with fixed-deviation tails, all finite moments and localization) transfers to independent-score rankings and positive continuous-profile Luce arrays, with bounded-rate sparse-error robustness. A dyadic terminal-block comparison gives first-order endpoint LIS/LDS laws for both Sukhatme orientations, quantitative truncation bounds and the certified decreasing-rate lower bound >3.0602. No singular full-field or Tracy–Widom assertion. |

## Precision and non-claims

The new `mod-poisson` manuscript proves a uniform local analytic bound for arbitrary comparable arrays but identifies its limiting analytic residue only under the sampled positive continuous-profile hypothesis, locally uniformly for complex z near 1. It does not assert convergence on the entire imaginary axis or an identified residue without profile convergence. Its two imported asymptotic theorems are the local-entry/envelope result of `regular-profile-cycles` and the macroscopic uniform-root result of `macroscopic-pd`; the switching identity from `mesoscopic-switching` is a cited finite identity. A manuscript-level internal proof audit and a second focused review found no fatal gap, but neither amounts to independent external refereeing.



For the quantitative total-cycle results, exact-mean centering is essential at the stated precision. The newer `mod-poisson` theorem yields `E K_n = H_n + O(1)` and `Var K_n - E K_n = O(1)` uniformly over comparable-rate arrays. These bounds do not justify replacing the exact mean inside the sharp lattice formulas, because the lattice phase can jump under an arbitrarily small centering error. The second-order Edgeworth formula retains the exact variance-minus-mean coefficient; an arbitrary comparable-rate array need not have a convergent profile or limiting coefficient. Signed approximants are not asserted positive, and the right-continuous lattice phase equals +1/2 at integers.

The regular-profile extraction is not extended to arbitrary comparable arrays, growing cycle lengths, endpoint-singular profiles, or a quantitative total-variation rate. The spectral PD/GEM replacement permits endpoint-singular spectra under its stated channel criterion and recovers all comparable-rate arrays through its subsequential form. It does not supply a quantitative convergence rate or uniformity over arbitrary deletion histories. Its conditional root and deletion estimates apply to the specified regular histories and good slab data. The random-environment corollary concerns rates independent of the exponential variables whose empirical laws converge in probability to a deterministic qualifying limit; conditional convergence is in probability. Neither that corollary nor the broader marginal cycle theorem changes the hypotheses of the regular-profile, mod-Poisson, or independence-peeling manuscripts.

The five audit-passed working extractions remain below audited-current status until their recorded clarifications are applied in focused repair PRs and checked against the frozen-source theorem scope.

The `independence-peeling` manuscript imports conditional regular-history root and deletion estimates from `macroscopic-pd`, a stronger interface than the unweighted root law used in `mod-poisson`. Its finite-deletion argument is uniform only for a fixed number of prescribed vertices on suitable good slab data. Its two-root absolute switching-intensity estimate is not replaced by the weaker mean-defect estimate used for scalar mod-Poisson growth. The iterated peeling law is scalar; growing windows, simultaneous all-annulus independence, and complex-tilted joint transforms are not asserted. The appendix cutoff error belongs to the limiting PD partition, not to the finite-n Luce partition.

The `bottom-window-universality` theorem assumes a regularly varying profile with a positive index and an essential positive lower bound away from the endpoint. The deterministic grid theorem uses pointwise lower bounds; a separate almost-everywhere grid-profile approximation suffices to identify its permuton with the sampled model. The endpoint hypotheses alone do not guarantee that identification. The Poisson point-process and Poisson–Dirichlet distribution identities are annealed laws of clock values, and the eventual-equality assertion uses the stated Poisson-spacings coupling. The power-law rank-permutation limit and linear last-label constant overlap Pitman--Tran's published results; the logarithmic scalar tail is an instance of the Arendarczyk--Dębicki Weibull-product lemma. The multiple-zero direction requires convergent local scale ratios and marked local labels; the crossover, effective-rate, and general critical-scale questions remain open.

The standalone `stratified-hammersley-lis` paper is a first-order LIS/LDS result, not a cycle theorem, and does not import an active Luce manuscript. Its endpoint theorem provides terminal subsequence limits and concentration, not a uniform full shape field in the singular regime. The rigorous bound for the decreasing-rate Sukhatme LIS constant is strictly greater than 3.0602; the draft does not certify a two-decimal numerical limiting constant. Its internal audit and repaired localization proof are documented in [the focused record](audits/stratified-hammersley-proof-audit.md).

## Spectral PD/GEM theorem register

The active spectral source retains the full criterion and distinguishes its proved boundary results from its remaining questions:

| Result | Label | Status and scope |
| --- | --- | --- |
| Spectral criterion, Theorem 1.1 | `thm:main-spectral` | **Proved.** Weak convergence of maximum-normalized empirical laws to $ν$, no atom at zero, and $q(ν)<1$ imply the three cycle limits for every deterministic rate arrangement. |
| Subsequential criterion, Corollary 1.2 | `cor:subsequential-spectral` | **Proved.** Every weak subsequential limit must satisfy the criterion; a single limiting law and an extra uniform-gap assumption are unnecessary. |
| Independent random environments, Corollary 1.3 | `cor:random-environment` | **Proved.** Conditional bounded-Lipschitz convergence in probability when rates are independent of the exponential variables and their empirical laws converge in probability to a deterministic qualifying law. |
| Longest cycle, Corollary 1.4 | `cor:longest-cycle` | **Proved.** Convergence to the largest PD(1) part and convergence of every positive moment. |
| Regularly varying gap, Theorem 1.5 | `thm:rv-gap` | **Proved.** A lower tail regularly varying at zero with positive index has a spectral gap. Power and regularly varying rate spectra are covered by Corollaries 1.6–1.7. |
| Comparable arrays, Corollary 8.1 | `cor:comparable` | **Proved.** Recovers the predecessor's full theorem without empirical-law convergence. |
| Dyadic-doubling criterion, Theorem 9.1 | `thm:dyadic-doubling` | **Proved; promoted from conjecture.** Eventually positive shell masses with successive ratios between fixed positive constants strictly below one give a gap, including atomic or singular laws. |
| Slowly varying boundary, Theorem 9.2 | `thm:slow-boundary` | **Proved; promoted from conjecture.** An eventually positive, slowly varying lower tail tending to zero has $q(ν)=1$. This does not assert failure of PD(1). |

See the [spectral audit](audits/spectral-pd-proof-audit.md) for the five repaired proof points and the [migration map](papers/macroscopic-pd/THEOREM_MIGRATION.md) for the exact predecessor interfaces.

## Historical material

The original total-cycle / Conjecture 13.2 resolution candidate is a **Historical rejected candidate**. The later Campbell--Stein proof does not reinstate its proposed profile expectation expansion.

The comparable-rate PD/GEM paper is a **superseded, proved predecessor**, preserved with its PDF and extraction map in [the comparable-rate archive](archive/macroscopic-pd-comparable/README.md). It is no longer a separate active paper or an active dependency; its full theorem is recovered by the spectral manuscript. Its historical audit findings and hashes remain valid for that preserved version.

No principal theorem-and-proof package remains only in the frozen 139-page monolith. The monolith-only remainder is introductory, transitional, concluding, or conjectural exposition, as recorded in `notes/migration-plan.md`.

## Open questions

For spectral PD/GEM, necessity of a channel gap for universality over all deterministic arrangements remains Question 9.3. The slowly varying no-gap theorem does not settle it. Growing log-linear spectra (Question 9.5), the multiscale endpoint phase (Conjecture 9.6), quantitative GEM/PD convergence (Question 9.7), and the exact power-law gap (Question 9.8) remain open. The former dyadic and slowly varying conjectures are now Theorems 9.1 and 9.2.

The active `mod-poisson` manuscript establishes the sampled positive continuous-profile mean constant, locally uniform analytic convergence near z = 1, and the limits of every fixed higher factorial cumulant. For arbitrary comparable-rate arrays, it proves uniform bounds on the mean shift and higher factorial cumulants, but not an identified analytic limiting residue. Open extensions include broader rate-array limits, endpoint-singular or discontinuous profiles, and convergence on larger complex domains (including the full imaginary axis in stronger formulations). See the [scope and remaining-questions note](notes/working/profile-mod-poisson.md).

## Review records

The five audit-passed working extractions have paired extraction, provenance, and proof-audit records:

| ID | Extraction record | Proof audit | Provenance map |
| --- | --- | --- | --- |
| `boundary-laws` | [record](audits/boundary-laws-extraction.md) | [audit](audits/boundary-laws-proof-audit.md) | [map](papers/boundary-laws/EXTRACTION_MAP.md) |
| `sukhatme-fixed-points` | [record](audits/sukhatme-fixed-points-extraction.md) | [audit](audits/sukhatme-fixed-points-proof-audit.md) | [map](papers/sukhatme-fixed-points/EXTRACTION_MAP.md) |
| `endpoint-regular-universality` | [record](audits/endpoint-regular-universality-extraction.md) | [audit](audits/endpoint-regular-universality-proof-audit.md) | [map](papers/endpoint-regular-universality/EXTRACTION_MAP.md) |
| `global-endpoint-poisson` | [record](audits/global-endpoint-poisson-extraction.md) | [audit](audits/global-endpoint-poisson-proof-audit.md) | [map](papers/global-endpoint-poisson/EXTRACTION_MAP.md) |
| `endpoint-short-cycles` | [record](audits/endpoint-short-cycles-extraction.md) | [audit](audits/endpoint-short-cycles-proof-audit.md) | [map](papers/endpoint-short-cycles/EXTRACTION_MAP.md) |

The regular-profile extraction and the now-preserved comparable-rate PD/GEM predecessor have full historical extraction/audit/repair chains:

| ID | Extraction | Audit | Repair |
| --- | --- | --- | --- |
| `regular-profile-cycles` | [record](audits/regular-profile-extraction.md) | [audit](audits/regular-profile-proof-audit.md) | [repair](audits/regular-profile-repair-record.md) |
| `macroscopic-pd` | [record](audits/macroscopic-pd-extraction.md) | [audit](audits/macroscopic-pd-proof-audit.md) | [repair](audits/macroscopic-pd-repair-record.md) |

The active spectral replacement has a separate [proof and integration audit](audits/spectral-pd-proof-audit.md) and [theorem migration map](papers/macroscopic-pd/THEOREM_MIGRATION.md). The two downstream papers now cite its exact inputs; their theorem hypotheses are unchanged.

The total-cycle integration boundary is recorded in [the integration audit](audits/total-cycle-integration.md), and the preserved source proof notes remain under [`archive/total-cycle-source-notes/`](archive/total-cycle-source-notes/README.md).

The [independence and peeling proof audit](audits/independence-peeling-proof-audit.md) records the conditional input checks, explicit initial-deletion recursion, exceptional splitting sets, and appendix scope.

The [bottom-window universality proof audit](audits/bottom-window-universality-proof-audit.md) records the functional coupling, fixed-window total-variation consequence, prior-work overlap, exact-grid interpretation, last-label tail proof, and critical-scale and conjectural-scope repairs.

Formalization status: **not started in this repository**. CI, deterministic builds, finite exact checks, numerical consistency checks, extraction regression tests, and internal adversarial audits are not Lean verification, novelty certification, or independent peer review.
