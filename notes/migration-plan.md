# Staged migration

## Initial reviewed stages

1. Foundation: catalog, status/dependency maps, build checks, CI, and preservation conventions.
2. Preservation import: pin upstream commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`; preserve the original five Luce source/PDF pairs and historical audits byte-for-byte. Create active copies of the switching, scalar order, quantitative order, and functional manuscripts without changing their source bytes. The monolith stays archived.
3. Total-cycle integration: make the quantitative truncation interface explicit, incorporate the functional audit clarifications, and integrate the new total-cycle Poisson/Berry–Esseen/lattice Edgeworth argument. Preserve the uploaded proof notes and test programs with hashes. Any new mathematical limitation discovered during integration must be reported rather than hidden.
4. Macroscopic PD/GEM extraction: mechanically extract the archived macroscopic-cycle section and every model-specific lemma used by it into a standalone source. Preserve the exact hypothesis, PD(1)/GEM(1) conclusions, uniform-root conclusion, `ell^1` topologies, labels, and proof token stream. Register the paper as working and audit pending. This stage is extraction only.

The original repository has now been reconciled by a separate documentation-only PR and points here as the canonical editing location for the migrated Luce series.

## Current PD/GEM extraction stage

The extraction branch adds `papers/macroscopic-pd/poisson-dirichlet-luce.tex`, a compiled deterministic PDF, a complete old-label/new-label map, and a regression test comparing the archived and standalone section token streams up to whitespace. The archived source and PDF remain unchanged.

The extraction pull request must not be merged until its completeness checks have been reviewed. Passing compilation, token comparison, label/reference closure, and visual inspection is a preservation verdict, not a mathematical proof verdict. The separate audit must examine the clock-slab conditioning, relative-prefix estimate, rooted smoothing, compatible residual histories, deletion stability, GEM induction, and `ell^1` tail restoration.

## Subsequent decomposition of the 139-page draft

After the PD/GEM extraction is checked and its mathematical audit is completed separately, the regular-profile microscopic-cycle/sparse-entry paper is next.

The remaining planned thematic destinations are boundary laws; Sukhatme fixed points; endpoint universality; global endpoint fixed-point Poisson approximation; and singular-profile short cycles. These are proposed boundaries, not a promise that every extraction already fits a particular page count. Do not change hypotheses or upgrade proof status during mechanical extraction.

Do not maintain two independently editable copies. Active thematic papers live under `papers/`; the frozen monolith remains the provenance source under `archive/6178a99/`.

## Initial integration record

The foundation and preservation-import stages passed their separate PR checks. The total-cycle integration consolidated the two quantitative proof notes, updated the functional source and truncation interface, and registered three finite consistency programs. It did not split or certify the monolith. The macroscopic extraction begins that split while explicitly deferring the proof audit.
