# Staged migration

Status date: 12 October 2026.

## Initial reviewed stages

1. **Foundation.** Establish the manuscript catalog, theorem-status and dependency maps, deterministic builds, CI, preservation rules, and audit conventions.
2. **Preservation import.** Pin upstream commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`; preserve the original Luce sources, PDFs, and historical audits byte-for-byte; create active focused copies without changing the frozen archive.
3. **Total-cycle integration.** Make the quantitative switching interface explicit, incorporate the functional audit clarifications, and integrate the total-cycle Poisson, Berry--Esseen, and lattice-Edgeworth work while preserving the source proof notes and finite checks.
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
| Poisson--Dirichlet Universality for Luce Permutations | Yes | Yes | Passed; no fatal gap | Six localized clarifications were applied and regression-checked | Audited current manuscript | None | None |

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
