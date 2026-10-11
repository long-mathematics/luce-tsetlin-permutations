# Repository instructions

Read `THEOREM_STATUS.md`, `DEPENDENCIES.md`, and the relevant audit before editing mathematics. Preserve precise rate hypotheses, exact-mean versus deterministic centering, right-continuous lattice conventions, fixed-order quantifiers, and error uniformity.

Do not edit frozen material under `archive/`. Keep the original nonuniform-random-permutations repository unchanged during initial migration. There must be one canonical active source for each paper.

Changes require a branch, a PR, successful tests/build checks, and visual PDF review. The catalog is `papers.json`; outputs are `output/pdf/`. Never equate compilation with proof verification. Keep historical rejected total-cycle candidates out of dependencies.

Prefer independently auditable proofs and explicitly stated interfaces. Split the 139-page draft by mathematical dependencies in later PRs, with theorem/label migration maps; do not manufacture short papers by concealing their proof in an unreviewed monolith.
