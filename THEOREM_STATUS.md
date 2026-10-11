# Theorem status

Status date: 11 October 2026. This register distinguishes mathematical assertions, scoped proof reviews, and open questions. It is not an independent referee report or a formal proof certificate.

## Status vocabulary

**Imported** means byte-preserved source provenance, not new mathematical review. **Current research manuscript** means the integrated proof and named dependencies are documented. **Working** means an exploratory candidate. **Reviewed dependency** means only the named module was covered by a scoped audit. **Historical rejected candidate** means immutable provenance, excluded from dependencies. **Open** means no proof is promoted here.

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
| Macroscopic PD/GEM and singular endpoint results in the 139-page draft | Frozen archive. Dedicated thematic extraction and proof audits are still required; this migration is not such an audit. |

The original total-cycle/Conjecture 13.2 candidate remains a **Historical rejected candidate**. The newer Campbell–Stein proof does not reinstate its proposed profile expectation expansion.

## Proven precision boundaries

The quantitative count theorems use the exact mean. The available general estimate is mean = log n + O(log log n); this does not give the same sharp bound with center log n. The second-order expansion retains the exact variance-minus-mean coefficient, bounded by O((log log n)^2), not a conjectured limiting constant. Signed approximants are not asserted positive. The first lattice phase at an integer is +1/2.

## Open questions

The sampled-profile mean constant, a uniformly bounded mean shift for arbitrary comparable arrays, convergence of higher factorial cumulants, and a locally uniform complex Luce mod-Poisson residue remain open in this repository. See [profile-limit note](notes/working/profile-mod-poisson.md).

## Review records

[Integration audit](audits/total-cycle-integration.md), [dependency register](DEPENDENCIES.md), and [preserved scoped audit and proof notes](archive/total-cycle-source-notes/README.md). Original finite result records are provenance; current checks are rerun in CI.

Formalization status: **not started in this repository**. Finite exact identities and numerical checks do not constitute Lean verification or proofs of asymptotic estimates. No independent novelty certification or peer review is claimed.
