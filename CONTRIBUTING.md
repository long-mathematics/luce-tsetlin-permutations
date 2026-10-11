# Contributing

Use a feature branch and a pull request. Separate preservation/file movement, mathematical changes, and proof-status changes. Merge only after reviewing the diff and successful checks for the current PR head.

Use descriptive stable paper directories and filenames; do not encode draft dates or version counters in canonical names. Every authored manuscript retains `Christopher D. Long` as its sole author unless the user expressly changes authorship.

Register papers in `papers.json`, record exact input labels in `DEPENDENCIES.md`, and update `THEOREM_STATUS.md` when a result is promoted, weakened, or withdrawn. Never use archived rejected candidates as theorem dependencies. Archived files are immutable and checked against a preservation manifest.

Run `make test`, `make pdf`, `make check`, and `make verify`. Review changed PDF pages visually; review all pages of a new short manuscript. Commit LaTeX, the corresponding PDF, and hashes together. The snapshot builder is a convenience, not mathematical approval.

README mathematics uses `$...$` and `$$...$$` with standard commands, no private macros. Display delimiters occupy their own lines. A line consisting only of `=` or hyphens is forbidden inside a display because Markdown can reinterpret it as a heading.

A successful finite test is not an asymptotic proof. A scoped AI-assisted audit is not independent refereeing. No Lean claims are permitted without executable formal sources and an actually passing formalization job.
