# Analytic mod-Poisson manuscript: proof and integration audit

## Scope

Source: `papers/mod-poisson/luce_mod_poisson.tex`. Status: **internally audited current research** (20 October 2026); not an independent external referee report and not formal verification.

The manuscript proves local complex normal-family bounds for arbitrary comparable-rate arrays and the analytic mod-Poisson generating-function limit under positive continuous profiles. Its exact-mean residue and higher factorial-cumulant limits are corollaries.

## Dependency boundary

The exact marked switch is referenced to the mesoscopic switching paper (`prop:master-switch`) and restated with a proof. The *two* imported asymptotic theorems are (i) the separated target-bulk local estimate and the endpoint/collision envelopes in `regular-profile-cycles`, and (ii) the original-measure uniform-root consequence of `macroscopic-pd`. Their exact interfaces are restated in the manuscript. In particular, source labels in the local-entry estimate are arbitrary distinct labels; bulk and separation restrictions apply only to the target ranks.

The analytic mod-Poisson proof does **not** assume the unpublished profile mean-shift/higher-cumulant paper, a complex-fugacity switching theorem, finite-deletion independence, or a tilted Poisson–Dirichlet limit. Its real-fugacity endpoint argument is developed internally.

## Internal review

The internal line-by-line review and an independent focused AI-assisted review found no fatal gap in the new chain of arguments. The latest revision specifically tightened (a) source citations and supremum-over-label envelope phrasing; (b) conditional sigma-fields in single-row insertion; (c) symbol collisions; (d) explicit large-n qualifications, parameter absorption, and terminal-depth bounds; and (e) distinctions between conditional results and unweighted asymptotic imports.

The exact common-rate thinning identity, finite insertion bijections, selected-factor bounds, trace-class estimates, and rank-one determinant relation underwent finite or numerical consistency checks in the draft's companion audit materials. Such tests cannot verify asymptotic theorems.

The remaining independent-verification boundary is end-to-end scrutiny of the two upstream asymptotic theorems, especially the uniform target-envelope estimates and regular-history arguments in the macroscopic theorem.

## Repository reproducibility

The LaTeX source and compiled PDF are registered in `papers.json`; the deterministic build and SHA-256 PDF manifest are maintained by `scripts/build.py`. Run `make pdf`, `make test`, `make check`, and `make verify` following `CONTRIBUTING.md`. At the original integration, the companion citations were pinned to repository revision `01f99e121c4ea497e3c9e9bcfa83d027c5833742`. The later spectral migration below updates only the macroscopic input citation.

## Spectral PD dependency migration — 20 October 2026

The macroscopic citation now points to the approved spectral source at revision `81462993a7400f972a3d75583d447fbeccf1e7b3`. The imported conclusion remains the original-measure uniform-root law under comparable rates: Theorem 1.1, equation `eq:uniform-root-main`, specialized by Corollary 8.1. That corollary includes arrays without an empirical rate-law limit. No tilted, residual-history, or finite-deletion input is added.

A focused interface review checked the replacement against the active spectral source. Every labelled theorem, corollary, lemma, proposition, and input-theorem statement in this manuscript is unchanged. The bibliography and explanatory citation paragraph are the only mathematical-source edits. See the [spectral integration record](spectral-pd-proof-audit.md) and [theorem migration map](../papers/macroscopic-pd/THEOREM_MIGRATION.md). The earlier audit remains a record of its originally pinned companions.
