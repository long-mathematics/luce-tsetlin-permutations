# Luce/Tsetlin Permutations

Limit laws and cycle statistics for Luce/Tsetlin permutations, including Poisson–Dirichlet universality, switching methods, and Erdős–Turán theorems.

Manuscript author: **Christopher D. Long**.

## Manuscripts

| Manuscript | PDF | LaTeX | Import status |
| --- | --- | --- | --- |
| Mesoscopic cycles of comparable-rate Luce permutations | [PDF](output/pdf/mesoscopic-luce-cycles.pdf) | [Source](papers/mesoscopic-switching/mesoscopic-luce-cycles.tex) | imported |
| An Erdos--Turan Law for Comparable-Rate Luce Permutations | [PDF](output/pdf/luce-erdos-turan.pdf) | [Source](papers/erdos-turan-order/luce-erdos-turan.tex) | imported |
| A Sharp Berry--Esseen Theorem and First Edgeworth Expansion for Logarithmic Luce Order | [PDF](output/pdf/luce-edgeworth.pdf) | [Source](papers/sharp-order-edgeworth/luce-edgeworth.tex) | imported |
| Functional Erdos--Turan Universality for Comparable-Rate Luce Permutations | [PDF](output/pdf/functional-luce-erdos-turan.pdf) | [Source](notes/working/functional-luce-erdos-turan.tex) | working |

The **139-page original research draft** is preserved as [PDF](archive/6178a99/output/pdf/luce-boundary-cycle-laws.pdf) and [LaTeX](archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex). It has not yet been split or newly audited.

## Migration status

The preservation import is pinned and byte-checked. Importing a source does not upgrade its proof status. Total-cycle integration is the next separate PR; the functional manuscript remains a working branch until that integration.

The original [Nonuniform Random Permutations](https://github.com/long-mathematics/nonuniform-random-permutations) repository remains unchanged. Riffle, shelf, Thorp, and caching manuscripts remain there. This repository will be the canonical editing destination for the migrated Luce series; preserved copies are archival.

[Preservation manifest](archive/manifest.json) · [Import mapping](notes/import-record.json)

## Reading and status

The [document catalog](papers.json) is the build manifest's source of truth. [Theorem status](THEOREM_STATUS.md) distinguishes manuscript assertions, proof reviews, and unresolved questions. [Dependencies](DEPENDENCIES.md) records which mathematical modules are actually imported. [Migration plan](notes/migration-plan.md) records the preservation and splitting sequence.

Compilation, finite calculations, and CI do not constitute mathematical refereeing or Lean verification. No theorem is represented as formally verified.

## Build and checks

On Debian/Ubuntu, install `latexmk`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-science`, `lmodern`, `poppler-utils`, `python3`, `python3-numpy`, `python3-scipy`, `python3-sympy`, and `make`.

```sh
make test       # catalog, dependency, status, link, and README regressions
make pdf        # build active sources and refresh deterministic PDF snapshots
make check      # verify frozen hashes; rebuild active PDFs byte-for-byte
make verify     # run registered mathematical consistency checks
```

PDFs and their source/PDF hashes are committed together. Historical source and PDF bytes are verified separately from current deterministic builds. CI has read-only repository access. A separate migration-branch workflow can prepare imports and snapshots, but cannot merge a pull request or write to the original repository.

See [contribution rules](CONTRIBUTING.md), [repository instructions](AGENTS.md), and [license scope](LICENSE.md).
