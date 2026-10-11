# Repository instructions

- Treat `papers/` as the current Long manuscript sources. `notes/working/` contains active strengthenings; `notes/provenance/` is historical and must not be silently promoted.
- Keep the eight numbered paper directories and stable filenames. Do not encode dates or draft numbers into canonical names.
- For source changes, run `make test`, `make pdf`, and `make check`. Inspect changed PDF pages visually. Commit updated PDFs and `output/pdf/manifest.json` with the corresponding sources.
- Never silently change theorem hypotheses, author attribution, proof status, or the distinction between current, working, historical, and third-party material.
- README mathematics must use `$...$` and `$$...$$` only. Do not introduce custom macros in README math; spell them out with standard commands such as `\\mathbb`, `\\mathrm`, and `\\operatorname`.
- `third_party/openai-thorp/` is third-party Apache-2.0 material pinned to an upstream commit. Preserve attribution and license text.
- Use feature branches and pull requests. Do not bypass checks or change visibility/licensing without an explicit request.
