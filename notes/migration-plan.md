# Staged migration

Status date: 20 October 2026.

## Initial reviewed stages

1. **Foundation.** Establish the manuscript catalog, theorem-status and dependency maps, deterministic builds, CI, preservation rules, and audit conventions.
2. **Preservation import.** Pin upstream commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`; preserve the original Luce sources, PDFs, and historical audits byte-for-byte; create active focused copies without changing the frozen archive.
3. **Total-cycle integration.** Make the quantitative switching interface explicit, incorporate the functional audit clarifications, and integrate the total-cycle Poisson, Berry–Esseen, and lattice-Edgeworth work while preserving the source proof notes and finite checks.
4. **Macroscopic PD/GEM extraction, audit, and repair.** Mechanically extract the macroscopic theorem package, audit it independently, and apply only the six localized clarifications approved by that audit.
5. **Regular positive-profile extraction, audit, and repair.** Mechanically extract the microscopic-cycle, trace, sparse-entry, and overlap package, audit it independently, and apply only the six localized clarifications approved by that audit.
6. **Remaining five-paper decomposition.** Extract and independently audit Boundary Laws, Sukhatme Fixed Points, Endpoint-Regular Fixed-Point Universality, Global Endpoint Poisson Approximation, and Endpoint Short Cycles. In accordance with the requested workflow, record but do not apply the audit repairs in this stage.

The original `nonuniform-random-permutations` repository points here as the canonical editing location for the Luce/Tsetlin manuscript series.

## Consolidated monolith-decomposition status

| Paper | Extracted? | Completeness checked? | Audit verdict | Repairs required? | Promotion status | Active-paper dependencies | Remaining monolith-only theorem material? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Boundary Laws for Luce Rankings | Yes | Yes; selected blocks are byte-preserved, labels/references close, deterministic PDF and regression checks pass | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Sukhatme Fixed Points and the Terminal Poisson Process | Yes | Yes; complete saddle, localization, point-process, and factorial-moment package preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Endpoint-Regular Fixed-Point Universality | Yes | Yes; endpoint framework, fixed-point laws, tangent kernel, and microscopic limit preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Global Endpoint Poisson Approximation | Yes | Yes; endpoint framework, Palm/Stein coupling, swap law, quantitative saddle, and two-cycle package preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Endpoint Short Cycles | Yes | Yes; point-constraint saddle, global envelope, trace, and factorial-moment package preserved | Passed; no fatal gap | Yes; six localized clarifications recorded and deferred | Working mechanical extraction; audit passed, repairs pending | None | None |
| Microscopic Cycles and Sparse Entries for Regular Luce Profiles | Yes | Yes | Passed; no fatal gap | Six localized clarifications were applied and regression-checked | Audited current manuscript | None | None |
| Poisson–Dirichlet Universality for Luce Permutations | Yes | Yes | Passed; no fatal gap | Six localized clarifications were applied and regression-checked | Audited predecessor; now preserved and superseded by the spectral manuscript | None | None |

The five papers processed in the final decomposition stage deliberately remain below audited-current status because this orchestration prompt prohibited applying repairs. Their audit reports are the specifications for later focused repair PRs.

## Remaining material in the frozen monolith

No principal theorem-and-proof package now exists only in the 139-page source. The material intentionally retained only in the frozen monolith consists of:

- the original introduction, scope discussion, and conventions;
- the concluding theorem map and proof-mechanism overview;
- the historical open-problem and additional-conjecture sections;
- transitional or duplicated exposition connecting theorem packages that now live in separate papers.

These sections may later be distilled into repository documentation or updated open-problem notes, but they are not additional extraction targets. The frozen monolith remains the immutable provenance source under `archive/6178a99/`; active thematic papers live under `papers/` and must not be maintained in duplicate.

## Next controlled stage

Any further mathematical editing of the five newly extracted papers should occur one paper at a time through a focused repair PR that implements exactly the localized clarifications in its audit report. Such repair PRs must preserve the archived theorem scope and must not introduce an unreviewed strengthening.

## Integration record

The foundation, preservation import, total-cycle integration, PD/GEM extraction, and regular-profile extraction passed their separate validation workflows. Each of the five final thematic extractions has a standalone source, deterministic PDF, provenance map, extraction record, permanent archive-preservation test, and independent audit report. All audits found no fatal gap. No frozen archive byte was changed during the decomposition.

## Independent LIS/Hammersley addition (20 October 2026)

`stratified-hammersley-lis` is a standalone, independently developed paper (not an extraction from the archived 139-page source). The stronger 13 October draft was retained, audited, and updated: bounded-density stratified shape and localization; regular-profile and robust Luce/independent-score LIS and LDS laws; dyadic endpoint LIS/LDS for both Sukhatme orientations; self-similar truncation inequality; and the certified `>3.0602` decreasing-rate LIS lower bound. The October 12 regular-profile-only draft is historical research context and not a second active canonical manuscript. The active source, deterministic PDF, and hash manifest appear in the catalog and `output/pdf/manifest.json`. See [the LIS audit](../audits/stratified-hammersley-proof-audit.md) and [dependency map](../DEPENDENCIES.md).

## Spectral PD/GEM replacement (20 October 2026)

The stable catalog ID `macroscopic-pd` now identifies [Spectral Poisson–Dirichlet Universality for Luce Permutations under Arbitrary Rate Arrangements](../papers/macroscopic-pd/spectral-poisson-dirichlet-luce.tex). This is a substantive extension of the comparable-rate paper, with its own proof audit and five mathematical repairs; it is not a scope-preserving mechanical extraction. The full channel criterion, its subsequential form, and both proved boundary results are retained. The dyadic-doubling and slowly varying results are Theorems 9.1 and 9.2; gap necessity remains open.

The earlier source, PDF, and extraction map are preserved byte-for-byte under [`archive/macroscopic-pd-comparable/`](../archive/macroscopic-pd-comparable/README.md), with their hashes appended to the preservation manifest. No previously archived file or preservation record is changed. Historical extraction and six-repair regression checks now read this preserved predecessor. The active source and deterministic PDF use the spectral filename, leaving one canonical active macroscopic manuscript.

`mod-poisson` now imports the spectral theorem's comparable-rate uniform-root consequence. `independence-peeling` imports the precise conditional root/deletion interfaces with maximum-normalized clocks, good slab data, empirical tail bounds, and the full finite-deletion cutoff budget. Both papers retain their existing main theorem statements and rate hypotheses. The migration does not extend microscopic–macroscopic independence to endpoint-singular arrays.

See the [spectral proof and integration record](../audits/spectral-pd-proof-audit.md), [theorem migration map](../papers/macroscopic-pd/THEOREM_MIGRATION.md), and [current dependency map](../DEPENDENCIES.md). The latest LIS integration and standardized Unicode display titles are retained.
