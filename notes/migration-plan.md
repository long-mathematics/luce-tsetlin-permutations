# Staged migration

## Initial reviewed stages

1. Foundation: catalog, status/dependency maps, build checks, CI, and preservation conventions.
2. Preservation import: pin upstream commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`; preserve the original five Luce source/PDF pairs and historical audits byte-for-byte. Create active copies of the switching, scalar order, quantitative order, and functional manuscripts without changing their source bytes. The monolith stays archived.
3. Total-cycle integration: make the quantitative truncation interface explicit, incorporate the functional audit clarifications, and integrate the new total-cycle Poisson/Berry–Esseen/lattice Edgeworth argument. Preserve the uploaded proof notes and test programs with hashes. Any new mathematical limitation discovered during integration must be reported rather than hidden.

The old repository is not edited during these three stages.

## Subsequent decomposition of the 139-page draft

Priority: extract the macroscopic PD/GEM proof with all actual dependencies and an old-label/new-label map, then audit it as a separate unit. The regular-profile microscopic paper is next.

The planned thematic destinations are boundary laws; regular-profile cycles and sparse entries; macroscopic PD/GEM; Sukhatme fixed points; endpoint universality; global endpoint fixed-point Poisson approximation; and singular-profile short cycles. These are proposed boundaries, not a promise that every extraction already fits a particular page count. Do not change hypotheses or upgrade proof status during mechanical extraction.

Cross-reference the old README only after verified canonical versions are in place. Do not maintain two independently editable copies.

## Initial integration record

The foundation and preservation-import stages have passed their separate PR checks. The total-cycle integration consolidates the two quantitative proof notes, updates the functional source and truncation interface, and registers three finite consistency programs. It does not split or certify the monolith. The original repository remains unchanged until a later explicit cross-reference reconciliation.
