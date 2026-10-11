# Luce/Tsetlin Permutations

Limit laws and cycle statistics for Luce/Tsetlin permutations, including Poisson–Dirichlet universality, switching methods, and Erdős–Turán theorems.

Manuscript author: **Christopher D. Long**.

## Current manuscripts

| Manuscript | PDF | LaTeX | Status |
| --- | --- | --- | --- |
| Mesoscopic cycles of comparable-rate Luce permutations | [PDF](output/pdf/mesoscopic-luce-cycles.pdf) | [Source](papers/mesoscopic-switching/mesoscopic-luce-cycles.tex) | imported |
| An Erdos--Turan Law for Comparable-Rate Luce Permutations | [PDF](output/pdf/luce-erdos-turan.pdf) | [Source](papers/erdos-turan-order/luce-erdos-turan.tex) | imported |
| A Sharp Berry--Esseen Theorem and First Edgeworth Expansion for Logarithmic Luce Order | [PDF](output/pdf/luce-edgeworth.pdf) | [Source](papers/sharp-order-edgeworth/luce-edgeworth.tex) | imported |
| Functional Erdos--Turan and Total-Cycle Laws for Luce Permutations | [PDF](output/pdf/functional-luce-erdos-turan.pdf) | [Source](papers/functional-erdos-turan/functional-luce-erdos-turan.tex) | current-research |
| Poisson Approximation and Lattice Edgeworth Expansions for Total Luce Cycles | [PDF](output/pdf/total-cycle-edgeworth.pdf) | [Source](papers/total-cycle-edgeworth/total-cycle-edgeworth.tex) | current-research |
| Microscopic Cycles and Sparse Entries for Regular Luce Profiles | [PDF](output/pdf/regular-profile-cycles.pdf) | [Source](papers/regular-profile-cycles/regular-profile-cycles.tex) | mechanical extraction; proof audit pending |
| Poisson--Dirichlet Universality for Luce Permutations | [PDF](output/pdf/poisson-dirichlet-luce.pdf) | [Source](papers/macroscopic-pd/poisson-dirichlet-luce.tex) | audited current manuscript |

The **139-page original research draft** is preserved as [PDF](archive/6178a99/output/pdf/luce-boundary-cycle-laws.pdf) and [LaTeX](archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex). It is not an active monolithic editing target. The regular positive-profile microscopic-cycle and sparse-entry theory is now available as a byte-preserving standalone working extraction, with its [provenance map](papers/regular-profile-cycles/EXTRACTION_MAP.md) and [extraction record](audits/regular-profile-extraction.md); its proof status has not been upgraded and a dedicated audit remains pending. The standalone PD/GEM manuscript was mechanically extracted, checked for completeness, adversarially audited, and revised only by the six localized clarifications recorded in the [proof audit](audits/macroscopic-pd-proof-audit.md) and [repair record](audits/macroscopic-pd-repair-record.md). The [label map](papers/macroscopic-pd/EXTRACTION_MAP.md) and regression checks preserve the theorem scope and document the exact departure from the frozen token stream.

## Total-cycle results

For positive rates with a fixed largest-to-smallest ratio, write $K_n$ for the total cycle count, $\mu_n=\mathbb E K_n$, and $L=\log n$. The functional manuscript gives the count CLT and its joint functional law with logarithmic permutation order. The new quantitative manuscript gives

$$
\mathrm{d}_{\mathrm{TV}}(\mathcal L(K_n),\mathrm{Pois}(\mu_n))
= O_\kappa((\log L)^2/L),
$$

and the exact leading normal-approximation constant

$$
\sqrt L\,\mathrm{d}_{\mathrm K}((K_n-\mu_n)/\sqrt L,N(0,1))
\longrightarrow \frac{2}{3\sqrt{2\pi}}.
$$

It also proves first and second lattice Edgeworth expansions and signed Poisson–Charlier approximations at each fixed order. The second expansion retains the exact variance-minus-mean correction; it does not identify a limiting profile constant. Exact mean, lattice phase, and fixed-order quantifiers are essential. See [theorem status](THEOREM_STATUS.md) and [dependencies](DEPENDENCIES.md).

## Preservation and review

The initial import pins the original collection at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`. Original sources, PDFs, licenses, and historical audits are immutable hash-checked archival records. The invalid historical total-cycle candidate remains separate from the later functional and quantitative proofs.

The PD/GEM paper adds an active standalone copy without changing any archived byte. The extraction check certifies coverage and cross-reference closure; the later adversarial audit separately checks the clock-slab conditioning, adaptive prefix law, rooted closure, deletion stability, regeneration, GEM induction, residual-mass control, and $\ell^1$ passage. The audit found no fatal gap and recommended six publication-level clarifications, all of which are recorded and regression-checked. This remains an internal review, not formal verification or independent external refereeing.

[Preservation manifest](archive/manifest.json) · [Import mapping](notes/import-record.json) · [Source proof notes](archive/total-cycle-source-notes/README.md) · [Total-cycle integration audit](audits/total-cycle-integration.md) · [PD/GEM extraction record](audits/macroscopic-pd-extraction.md) · [PD/GEM proof audit](audits/macroscopic-pd-proof-audit.md) · [PD/GEM repair record](audits/macroscopic-pd-repair-record.md) · [Migration plan](notes/migration-plan.md)

Compilation, finite computations, extraction regression checks, and CI are not independent refereeing, novelty certification, or formal verification. Formalization has not started in this repository.

## Related collection

The original [Nonuniform Random Permutations](https://github.com/long-mathematics/nonuniform-random-permutations) repository retains the historical snapshots and now points here as the canonical editing destination for the migrated Luce series. Riffle, shelf, Thorp, and caching manuscripts remain there. Preserved copies are not independent editing targets.

## Build and checks

On Debian/Ubuntu install `latexmk`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-science`, `lmodern`, `poppler-utils`, `python3`, `python3-numpy`, `python3-scipy`, `python3-sympy`, and `make`.

```sh
make test       # catalog, dependency, status, links, extraction, and regression checks
make pdf        # refresh deterministic active PDF snapshots
make check      # frozen hashes and byte-identical active PDF rebuilds
make verify     # exact finite and numerical consistency programs
```

Every active source and PDF is recorded in [the PDF manifest](output/pdf/manifest.json). Review logs are uploaded as CI artifacts. The catalog is [papers.json](papers.json). See [contribution rules](CONTRIBUTING.md) and [license scope](LICENSE.md).
