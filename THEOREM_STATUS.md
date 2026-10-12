# Theorem status

Status date: 12 October 2026. This register distinguishes mathematical assertions, scoped proof reviews, mechanical extraction, and open questions. It is not an independent referee report or a formal proof certificate.

## Status vocabulary

**Imported** means byte-preserved source provenance, not new mathematical review. **Current research manuscript** means the integrated proof and named dependencies are documented. **Audited current manuscript** means an internal adversarial audit found no fatal gap, every recommended localized repair was applied, and the exact review boundary is recorded; it is not formal verification or independent external refereeing. **Working mechanical extraction** means the archived theorem and proof have been moved into a standalone source with extraction coverage checks. A paper may additionally have an audit-passed/repairs-pending status; it is not promoted to audited-current status until those repairs are applied and checked. **Working** means an exploratory candidate. **Reviewed dependency** means only the named module was covered by a scoped audit. **Historical rejected candidate** means immutable provenance, excluded from dependencies. **Open** means no proof is promoted here.

## Result-level status

| Result | Current location and scope |
| --- | --- |
| Comparable-rate mesoscopic cycles | Imported switching manuscript, now with an explicit truncation-uniform one-/two-root interface. The previously scoped endpoint audit applies to the named modules; no new full-series audit is asserted. |
| Scalar logarithmic-order CLT | Imported scalar paper, source unchanged by integration. |
| Sharp logarithmic-order Berry–Esseen/Edgeworth | Imported quantitative-order paper retains its result assertions. This integration narrows the wording of its endpoint interface to the source's mean conditional/annealed statement; it does not re-audit the nonlinear arithmetic proof. |
| Total-cycle CLT and joint functional count/order law | Current functional paper incorporates the scoped audit's explicit total-count, mean-centering, bounded-weight, tightness, and path-domain clarifications. |
| Exact-mean total-cycle Poisson approximation and sharp Berry–Esseen | Current quantitative total-cycle paper; the independent copied omitted count and mean-matched smoothing proof are explicit. Only the named switching modules, not the log-order Edgeworth theorem, are inputs. |
| First lattice Edgeworth expansion and exact leading Kolmogorov constant | Current total-cycle paper, with the right-continuous integer phase. |
| Variance asymptotic, second signed/lattice expansion, fixed-order Poisson–Charlier hierarchy | Current total-cycle paper, using fixed-order factorial domination and explicit moment transfer. Expansion order is fixed; no analytic residue convergence is inferred. |
| Boundary laws | **Working mechanical extraction; audit passed, repairs pending** in `papers/boundary-laws/`. The adversarial audit found no fatal gap in the vanishing-block obstruction, exact top-window identities, bottom-window convergence, terminal leakage, or log-log phase diagram. Six localized clarifications are recorded in `audits/boundary-laws-proof-audit.md`; none is applied here. |
| Sukhatme fixed points and terminal Poisson process | **Working mechanical extraction; audit passed, repairs pending** in `papers/sukhatme-fixed-points/`. The adversarial audit found no fatal gap in the death-process envelope, one- and multipoint terminal saddles, anisotropic localization, local terminal Poisson process, or fixed factorial moments. Six localized clarifications are recorded and deferred. |
| Endpoint-Regular Fixed-Point Universality | **Working mechanical extraction; audit passed, repairs pending** in `papers/endpoint-regular-universality/`. The endpoint fixed-point Poisson process, factorial moments, displacement and tangent laws, multiplicative kernel, and microscopic endpoint permutation all passed the independent audit within their archived scope. Six localized clarifications are recorded and deferred. |
| Global Endpoint Poisson Approximation | **Working mechanical extraction; audit passed, repairs pending** in `papers/global-endpoint-poisson/`. The independent audit found no fatal gap in the endpoint framework, approximate-Palm Stein argument, rank transposition, quantitative saddle, swap--Palm comparison, two-cycle correction, explicit total-variation rate, or normal corollary. Six localized clarifications are recorded and deferred. |
| Endpoint Short Cycles | **Working mechanical extraction; audit passed, repairs pending** in `papers/endpoint-short-cycles/`. The independent audit found no fatal gap in the source-to-target saddle, anisotropic LLT, global cycle envelope, logarithmic traces, negligible-configuration bounds, mixed factorial moments, or fixed-`L^p` law of large numbers. Six localized clarifications are recorded and deferred. |
| Regular positive-profile microscopic cycles and sparse entries | **Audited current manuscript** in `papers/regular-profile-cycles/`. The exact sampled-profile hypothesis, fixed-vector independent Poisson limits, trace means, long-trace asymptotic, diagonal-band laws, sparse-entry theorem, thin-graph laws, deterministic-overlap conclusion, and transverse-curve corollary are unchanged. The adversarial audit found no fatal gap in the local saddle/LLT argument, endpoint and collision domination, improper integrability, factorial-moment summation, total-variation upgrade, spectral trace argument, or sparse-entry applications. Six localized clarification sets were applied; no arbitrary-comparable-array, growing-cycle, endpoint-singular, or quantitative-TV strengthening is claimed. |
| Macroscopic PD/GEM theorem | **Audited current manuscript** in `papers/macroscopic-pd/`. The exact comparability hypothesis, PD(1) and GEM(1) conclusions, independently resampled uniform-root construction, uniform-root conclusion, and `ell^1` topologies are unchanged. The adversarial audit found no fatal gap in conditioning, adaptive exposure, rooted closure, deletion stability, regeneration, GEM induction, residual-mass control, or the `ell^1` passage. Six localized clarification repairs were applied; no quantitative, quenched, endpoint-singular, mesoscopic, or total-cycle strengthening is claimed. |
| Remaining monolith-only material | No principal theorem-and-proof package remains only in the frozen monolith. The remaining monolith-only text is introductory, transitional, concluding, or conjectural exposition; see `notes/migration-plan.md`. |

The original total-cycle/Conjecture 13.2 candidate remains a **Historical rejected candidate**. The newer Campbell–Stein proof does not reinstate its proposed profile expectation expansion.

## Boundary-laws extraction boundary

The selected blocks are byte-preserved, all internal references close, and no active paper is a proof dependency. The adversarial audit checked the exact finite identities, infinite-product limit, terminal leakage, phase diagram, and all endpoint cases and found no fatal gap. Six localized clarification repairs are specified in `audits/boundary-laws-proof-audit.md` and remain deliberately unapplied.

## Sukhatme extraction boundary

The exponential/Gumbel input, analytic LLT input, death-process envelope, anisotropic terminal saddle package, local Poisson process, and factorial-moment theorem are byte-preserved and dependency-closed. The independent audit found no fatal gap and records six localized clarifications. The manuscript remains a working extraction until those repairs are applied in a separate focused PR.

## Endpoint-Regular Fixed-Point Universality extraction boundary

The selected mathematical blocks are byte-preserved and dependency-closed. The adversarial audit checked endpoint regular variation, anisotropic localization, fixed-point factorial moments, displacement and tangent laws, the multiplicative semigroup, and the microscopic endpoint permutation, and found no fatal gap. Six localized clarifications are recorded and deferred.

## Global Endpoint Poisson Approximation extraction boundary

The selected mathematical blocks are byte-preserved and dependency-closed. The adversarial audit checked the Stein normalization, endpoint package, swap likelihood ratio and Palm comparison, two-cycle correction, weighted summation, and final total-variation/normal limits, and found no fatal gap. Six localized clarifications are recorded and deferred.

## Endpoint Short Cycles extraction boundary

The selected mathematical blocks are byte-preserved and dependency-closed. The adversarial audit checked endpoint regularity, source-to-target local limits, mixed localization, forced-deletion envelopes, logarithmic traces, negligible configurations, mixed factorial moments, and fixed-`L^p` convergence, and found no fatal gap. Six localized clarifications are recorded and deferred.

## Regular-profile audit and repair boundary

The standalone regular-profile paper was initially byte-preserving across the
exponential/Gumbel input, the analytic Bernoulli and lattice-LLT input, and the
complete regular positive-profile section. The adversarial audit then checked
the multivariate local limit and integrated saddle, uniform profile
perturbations, gap/endpoint/collision envelopes, improper trace passage,
fixed and mixed factorial moments, discrete total variation, compact spectral
trace argument, diagonal bands, sparse entries, thin graphs, deterministic
overlaps, and the transverse-curve application. It found no fatal gap.

The active source now differs from the archive only through six marked
clarification sets: uniform profile-approximation bookkeeping, the
integrated-saddle checklist, two summability/limit-order clarifications, the
cycle combinatorial normalization, standard convergence references, and the
spectral/repeated-edge bookkeeping. These edits do not change a principal
hypothesis, conclusion, limiting constant, or convergence mode. All
model-specific lemmas remain internal and the catalog records no active-paper
dependency. The review is internal, not formal verification or independent
peer review.

## Macroscopic audit and repair boundary

The PD/GEM paper does not import the later total-cycle results. All model-specific lemmas used by the macroscopic proof remain internal. The adversarial audit covers reduced slab conditioning, residual permanental factorization, predictable adaptive exposure, the relative-prefix theorem, scale-sensitive rooted closure, exclusion of premature auxiliary termination, deletion stability on a joint event, the noncircular GEM hierarchy, and the bounded-Lipschitz `ell^1` restoration. The six applied repairs make those points explicit and add textbook references for the standard external inputs. The review does not establish a convergence rate, arbitrary-history quenched uniformity, endpoint-singular universality, formal verification, novelty certification, or independent peer review.

## Proven precision boundaries

The quantitative count theorems use the exact mean. The available general estimate is mean = log n + O(log log n); this does not give the same sharp bound with center log n. The second-order expansion retains the exact variance-minus-mean coefficient, bounded by O((log log n)^2), not a conjectured limiting constant. Signed approximants are not asserted positive. The first lattice phase at an integer is +1/2.

## Open questions

The sampled-profile mean constant, a uniformly bounded mean shift for arbitrary comparable arrays, convergence of higher factorial cumulants, and a locally uniform complex Luce mod-Poisson residue remain open in this repository. See [profile-limit note](notes/working/profile-mod-poisson.md).

## Review records

The five final thematic extractions have paired extraction and audit records:

- [Boundary extraction](audits/boundary-laws-extraction.md), [boundary proof audit](audits/boundary-laws-proof-audit.md), and [boundary provenance map](papers/boundary-laws/EXTRACTION_MAP.md);
- [Sukhatme extraction](audits/sukhatme-fixed-points-extraction.md), [Sukhatme proof audit](audits/sukhatme-fixed-points-proof-audit.md), and [Sukhatme provenance map](papers/sukhatme-fixed-points/EXTRACTION_MAP.md);
- [Endpoint-regular extraction](audits/endpoint-regular-universality-extraction.md), [endpoint-regular proof audit](audits/endpoint-regular-universality-proof-audit.md), and [endpoint-regular provenance map](papers/endpoint-regular-universality/EXTRACTION_MAP.md);
- [Global endpoint extraction](audits/global-endpoint-poisson-extraction.md), [global endpoint proof audit](audits/global-endpoint-poisson-proof-audit.md), and [global endpoint provenance map](papers/global-endpoint-poisson/EXTRACTION_MAP.md);
- [Endpoint short-cycle extraction](audits/endpoint-short-cycles-extraction.md), [endpoint short-cycle proof audit](audits/endpoint-short-cycles-proof-audit.md), and [endpoint short-cycle provenance map](papers/endpoint-short-cycles/EXTRACTION_MAP.md).

Earlier records include the [regular-profile extraction](audits/regular-profile-extraction.md), [proof audit](audits/regular-profile-proof-audit.md), and [repair record](audits/regular-profile-repair-record.md); the [PD/GEM extraction](audits/macroscopic-pd-extraction.md), [proof audit](audits/macroscopic-pd-proof-audit.md), and [repair record](audits/macroscopic-pd-repair-record.md); the [total-cycle integration audit](audits/total-cycle-integration.md); the [dependency register](DEPENDENCIES.md); and the [preserved total-cycle proof notes](archive/total-cycle-source-notes/README.md). Original finite result records are provenance; current checks are rerun in CI.

Formalization status: **not started in this repository**. Finite exact identities, numerical checks, and token-preserving extraction tests do not constitute Lean verification or proofs of asymptotic estimates. No independent novelty certification or peer review is claimed.
