# Theorem status

Status date: 11 October 2026. This is a result/dependency register, not a referee report or formal verification certificate.

## Status vocabulary

- **Imported:** a byte-preserved source was copied; no new proof review follows from importing it.
- **Working:** a proof candidate is retained separately from the current manuscript series.
- **Reviewed dependency:** the named proof module has an accompanying scoped audit. This does not certify the rest of its manuscript.
- **Current research manuscript:** the integrated argument and its named dependencies are documented; external refereeing and formalization are not claimed.
- **Historical rejected candidate:** preserved for provenance and forbidden as a theorem dependency.
- **Open:** neither an integration nor a successful build changes this status.

## Preservation import state

Four editable manuscript copies and the archived original have been imported without source changes. No theorem is promoted by the import. The preserved upstream snapshot pins `long-mathematics/nonuniform-random-permutations` at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

The historical total-cycle/Conjecture 13.2 candidate remains a historical rejected candidate. A later functional proof and total-cycle quantitative notes must be distinguished from it at integration. In particular, a new total-cycle CLT must not silently reinstate the historical profile-dependent expectation proof.

## Questions that remain separate

The sampled-profile mean constant, an O(1) correction uniformly over arbitrary comparable arrays, convergence of higher factorial cumulants, and an analytic Luce mod-Poisson residue are not established by migration. Macroscopic PD/GEM and singular endpoint arguments in the large research draft retain their existing proof-review boundaries until dedicated audits.

Formalization status: **not started in this repository**. Executable exact identities are finite consistency checks, not formal asymptotic proofs.
