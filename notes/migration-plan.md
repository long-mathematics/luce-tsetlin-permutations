# Staged migration

## Initial reviewed stages

1. Foundation: catalog, status/dependency maps, build checks, CI, and preservation conventions.
2. Preservation import: pin upstream commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`; preserve the original five Luce source/PDF pairs and historical audits byte-for-byte. Create active copies of the switching, scalar order, quantitative order, and functional manuscripts without changing their source bytes. The monolith stays archived.
3. Total-cycle integration: make the quantitative truncation interface explicit, incorporate the functional audit clarifications, and integrate the new total-cycle Poisson/Berry–Esseen/lattice Edgeworth argument. Preserve the uploaded proof notes and test programs with hashes. Any new mathematical limitation discovered during integration must be reported rather than hidden.
4. Macroscopic PD/GEM extraction and audit: mechanically extract the archived macroscopic-cycle section and every model-specific lemma used by it; preserve the exact hypothesis, PD(1)/GEM(1) conclusions, uniform-root conclusion, `ell^1` topologies, labels, and proof content; then audit the extracted argument in a separate stage. The audit found no fatal gap, and the six localized clarification repairs have been applied without changing the principal theorem.
5. Regular positive-profile extraction and audit: mechanically extract the complete microscopic-cycle, long-trace, diagonal-band, sparse-entry, thin-graph, and overlap theory together with its indispensable preliminary and endpoint/collision bounds; audit the extracted proof separately; then apply only the six localized clarification sets approved by that audit. The audit found no fatal gap and the repairs preserve theorem scope.

The original repository has now been reconciled by a separate documentation-only PR and points here as the canonical editing location for the migrated Luce series.

## Current PD/GEM stage

The standalone source, deterministic PDF, old-label/new-label map, extraction record, adversarial proof audit, and repair record are now present. The archived source and PDF remain unchanged. The initial extraction was token-preserving; the active source now differs from the archive only through the six localized, documented clarification repairs.

The audit examined the clock-slab conditioning, relative-prefix estimate, rooted smoothing, compatible residual histories, deletion stability, GEM induction, residual-mass control, and `ell^1` tail restoration, and found no fatal gap. Regression checks now enforce theorem-scope preservation, label/reference closure, the six repair markers, and archive immutability. The result is an audited current manuscript, subject to the explicit internal-review boundary in `THEOREM_STATUS.md`.

## Subsequent decomposition of the 139-page draft

The regular-profile microscopic-cycle/sparse-entry paper has now completed mechanical extraction, adversarial proof audit, and localized clarification repair. Its active source is an audited current manuscript; the frozen monolith remains unchanged.

The boundary-laws paper and the Sukhatme fixed-point paper are now present as working mechanical extractions with completeness checks; their adversarial audits are tracked separately. The remaining planned thematic destinations are endpoint universality; global endpoint fixed-point Poisson approximation; and singular-profile short cycles. These are proposed boundaries, not a promise that every extraction already fits a particular page count. Do not change hypotheses or upgrade proof status during mechanical extraction.

Do not maintain two independently editable copies. Active thematic papers live under `papers/`; the frozen monolith remains the provenance source under `archive/6178a99/`.

## Initial integration record

The foundation and preservation-import stages passed their separate PR checks. The total-cycle integration consolidated the two quantitative proof notes, updated the functional source and truncation interface, and registered three finite consistency programs. It did not certify the monolith. The macroscopic extraction began that split; its separate audit and localized repair stage are now recorded without altering the frozen archive.
