# Theorem status

Status date: 11 October 2026. This register distinguishes mathematical assertions, scoped proof reviews, mechanical extraction, and open questions. It is not an independent referee report or a formal proof certificate.

## Status vocabulary

**Imported** means byte-preserved source provenance, not new mathematical review. **Current research manuscript** means the integrated proof and named dependencies are documented. **Audited current manuscript** means an internal adversarial audit found no fatal gap, every recommended localized repair was applied, and the exact review boundary is recorded; it is not formal verification or independent external refereeing. **Working mechanical extraction** means the archived theorem and proof have been moved into a standalone source with extraction coverage checks, but no new correctness claim is made. **Working** means an exploratory candidate. **Reviewed dependency** means only the named module was covered by a scoped audit. **Historical rejected candidate** means immutable provenance, excluded from dependencies. **Open** means no proof is promoted here.

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
| Macroscopic PD/GEM theorem | **Audited current manuscript** in `papers/macroscopic-pd/`. The exact comparability hypothesis, PD(1) and GEM(1) conclusions, independently resampled uniform-root construction, uniform-root conclusion, and `ell^1` topologies are unchanged. The adversarial audit found no fatal gap in conditioning, adaptive exposure, rooted closure, deletion stability, regeneration, GEM induction, residual-mass control, or the `ell^1` passage. Six localized clarification repairs were applied; no quantitative, quenched, endpoint-singular, mesoscopic, or total-cycle strengthening is claimed. |
| Singular endpoint results in the 139-page draft | Frozen archive. Dedicated thematic extraction and proof audits are still required. |

The original total-cycle/Conjecture 13.2 candidate remains a **Historical rejected candidate**. The newer Campbell–Stein proof does not reinstate its proposed profile expectation expansion.

## Macroscopic audit and repair boundary

The PD/GEM paper does not import the later total-cycle results. All model-specific lemmas used by the macroscopic proof remain internal. The adversarial audit covers reduced slab conditioning, residual permanental factorization, predictable adaptive exposure, the relative-prefix theorem, scale-sensitive rooted closure, exclusion of premature auxiliary termination, deletion stability on a joint event, the noncircular GEM hierarchy, and the bounded-Lipschitz `ell^1` restoration. The six applied repairs make those points explicit and add textbook references for the standard external inputs. The review does not establish a convergence rate, arbitrary-history quenched uniformity, endpoint-singular universality, formal verification, novelty certification, or independent peer review.

## Proven precision boundaries

The quantitative count theorems use the exact mean. The available general estimate is mean = log n + O(log log n); this does not give the same sharp bound with center log n. The second-order expansion retains the exact variance-minus-mean coefficient, bounded by O((log log n)^2), not a conjectured limiting constant. Signed approximants are not asserted positive. The first lattice phase at an integer is +1/2.

## Open questions

The sampled-profile mean constant, a uniformly bounded mean shift for arbitrary comparable arrays, convergence of higher factorial cumulants, and a locally uniform complex Luce mod-Poisson residue remain open in this repository. See [profile-limit note](notes/working/profile-mod-poisson.md).

## Review records

[Total-cycle integration audit](audits/total-cycle-integration.md), [PD/GEM extraction record](audits/macroscopic-pd-extraction.md), [PD/GEM proof audit](audits/macroscopic-pd-proof-audit.md), [PD/GEM repair record](audits/macroscopic-pd-repair-record.md), [PD/GEM old-label/new-label map](papers/macroscopic-pd/EXTRACTION_MAP.md), [dependency register](DEPENDENCIES.md), and [preserved scoped audit and proof notes](archive/total-cycle-source-notes/README.md). Original finite result records are provenance; current checks are rerun in CI.

Formalization status: **not started in this repository**. Finite exact identities, numerical checks, and token-preserving extraction tests do not constitute Lean verification or proofs of asymptotic estimates. No independent novelty certification or peer review is claimed.
