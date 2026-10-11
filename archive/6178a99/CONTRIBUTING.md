# Working on the manuscripts

1. Create a feature branch from `main`.
2. Edit the appropriate current manuscript in `papers/`, or place exploratory work under `notes/working/`.
3. Run `make test`, `make pdf`, and `make check`.
4. Inspect changed PDF pages visually; successful compilation is not a proof audit or visual review.
5. Commit the source, corresponding PDFs, and `output/pdf/manifest.json` together.
6. Open a pull request and review the `Build and check manuscripts` job before merging.

Use stable filenames. Keep mathematical changes separate from editorial, build, and file-organization changes. Historical audit material under `notes/provenance/` should be preserved as a record rather than rewritten to match later conclusions.

README mathematics is part of the website interface. Use `$...$` for inline mathematics and `$$...$$` for display mathematics. Do not use `\\(...\\)`, `\\[...\\]`, manuscript-only macros, or definitions such as `\\newcommand` in README.

Third-party files under `third_party/` retain their original license and attribution. Do not edit them except to update to a deliberately selected upstream version with a corresponding provenance change.
