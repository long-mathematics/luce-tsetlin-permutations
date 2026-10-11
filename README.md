# Luce/Tsetlin Permutations

Limit laws and cycle statistics for Luce/Tsetlin permutations, including Poisson–Dirichlet universality, switching methods, and Erdős–Turán theorems.

Manuscript author: **Christopher D. Long**.

## Migration status

This repository is being established in three separately reviewed stages: repository foundation, a byte-preserved import, and total-cycle integration. No manuscript has been promoted by this foundation commit. The 139-page research draft will be preserved as an archive, not enlarged or presented as a newly audited paper.

The original [Nonuniform Random Permutations](https://github.com/long-mathematics/nonuniform-random-permutations) repository remains unchanged during these stages. Riffle, shelf, Thorp, and caching manuscripts remain there. New canonical Luce sources will have descriptive, stable filenames here; archived copies are not independent editing targets.

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
