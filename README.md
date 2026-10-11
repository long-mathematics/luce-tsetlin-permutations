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
| Microscopic Cycles and Sparse Entries for Regular Luce Profiles | [PDF](output/pdf/regular-profile-cycles.pdf) | [Source](papers/regular-profile-cycles/regular-profile-cycles.tex) | audited current manuscript |
| Poisson--Dirichlet Universality for Luce Permutations | [PDF](output/pdf/poisson-dirichlet-luce.pdf) | [Source](papers/macroscopic-pd/poisson-dirichlet-luce.tex) | audited current manuscript |

The **139-page original research draft** is preserved as [PDF](archive/6178a99/output/pdf/luce-boundary-cycle-laws.pdf) and [LaTeX](archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex). It is not an active monolithic editing target. The regular positive-profile microscopic-cycle and sparse-entry theory is now an audited standalone manuscript. The initial extraction is documented by its [provenance map](papers/regular-profile-cycles/EXTRACTION_MAP.md) and [extraction record](audits/regular-profile-extraction.md); the later [proof audit](audits/regular-profile-proof-audit.md) found no fatal gap, and the six localized clarification sets are recorded in the [repair record](audits/regular-profile-repair-record.md). The standalone PD/GEM manuscript was mechanically extracted, checked for completeness, adversarially audited, and revised only by the six localized clarifications recorded in the [proof audit](audits/macroscopic-pd-proof-audit.md) and [repair record](audits/macroscopic-pd-repair-record.md). The [label map](papers/macroscopic-pd/EXTRACTION_MAP.md) and regression checks preserve the theorem scope and document the exact departure from the frozen token stream.


## Paper summaries

### Mesoscopic cycles of comparable-rate Luce permutations

[PDF](output/pdf/mesoscopic-luce-cycles.pdf) · [LaTeX](papers/mesoscopic-switching/mesoscopic-luce-cycles.tex)

For arbitrary triangular arrays of positive rates with a fixed largest-to-smallest ratio, this paper proves the mesoscopic uniform-permutation law
$$
\mathbb E C_{n,r}\sim \frac1r
$$
uniformly whenever the cycle length tends to infinity but remains $o(n)$. More generally, if $a_n\to\infty$ and $a_n=o(n)$, the point process of cycle lengths divided by $a_n$ converges vaguely to the scale-invariant Poisson process with intensity $dx/x$.

The proof develops the switching calculus used throughout the later series: a marked involutive clock-swap identity, selected-factor moment bounds, and a finite-endpoint mixing theorem in mean conditional total variation. It proves the short-root estimate internally and therefore does not depend on the macroscopic Poisson--Dirichlet theorem.

**Status:** imported manuscript. The named endpoint modules have scoped review records; this README does not promote the paper to a separately re-audited status.

### An Erdős--Turán law for comparable-rate Luce permutations

[PDF](output/pdf/luce-erdos-turan.pdf) · [LaTeX](papers/erdos-turan-order/luce-erdos-turan.tex)

This paper proves that the classical Erdős--Turán central limit theorem for permutation order survives throughout the comparable-rate Luce class, with no limiting rate profile:
$$
\frac{\log\operatorname{ord}(\sigma_n)-\frac12(\log n)^2}
{\sqrt{\frac13(\log n)^3}}
\Rightarrow N(0,1).
$$
The additive cycle-product statistic is handled by the marked switching theory, while an exact rate-oriented three-clock identity controls the arithmetic difference between the product and least common multiple of the cycle lengths through a uniform two-cycle factorial-moment estimate.

**Status:** imported manuscript. Its switching dependencies are explicit; the source is unchanged by the later total-cycle integration.

### A sharp Berry--Esseen theorem and first Edgeworth expansion for logarithmic Luce order

[PDF](output/pdf/luce-edgeworth.pdf) · [LaTeX](papers/sharp-order-edgeworth/luce-edgeworth.tex)

This quantitative supplement strengthens the scalar Erdős--Turán law. Writing $O_n=\operatorname{ord}(\sigma_n)$, $m_n=\mathbb E\log O_n$, and $L=\log n$, it states
$$
d_{\mathrm K}\!\left(
\frac{\log O_n-m_n}{\sqrt{L^3/3}},N(0,1)
\right)
\le \frac{C_\kappa}{\sqrt L},
$$
together with the first Edgeworth correction
$$
\mathbb P\!\left\{
\frac{\log O_n-m_n}{\sqrt{L^3/3}}\le x
\right\}
=
\Phi(x)-\frac{\sqrt3}{8}(x^2-1)\varphi(x)L^{-1/2}
+o_\kappa(L^{-1/2}).
$$
The proof combines polynomial endpoint control, prime-power linearization, compound-Poisson approximation, an extended Fourier window, and bounds for the nonlinear arithmetic remainder.

**Status:** imported quantitative manuscript. The later repository integration reviewed the switching interfaces used elsewhere, but did not constitute a fresh audit of this paper's full nonlinear arithmetic argument.

### Functional Erdős--Turán and total-cycle laws

[PDF](output/pdf/functional-luce-erdos-turan.pdf) · [LaTeX](papers/functional-erdos-turan/functional-luce-erdos-turan.tex)

For arbitrary comparable-rate triangular arrays, define the cycle-count and truncated-order processes by
$$
K_n(t)=\sum_{r\le n^t}C_{n,r},
\qquad
\mathcal O_n(t)=\log\operatorname{lcm}\{r\le n^t:C_{n,r}>0\}.
$$
This paper proves their joint functional convergence to the common Brownian field
$$
\left(
\frac{K_n(t)-t\log n}{\sqrt{\log n}},
\frac{\mathcal O_n(t)-\frac12t^2(\log n)^2}
{\sqrt{\frac13(\log n)^3}}
\right)
\Rightarrow
\left(W(t),\sqrt3\int_0^t u\,dW(u)\right).
$$
In particular it gives the total-cycle CLT and the joint endpoint Gaussian law, whose cycle-count/order correlation is $\sqrt3/2$.

The main intermediate theorem is a growing-dimensional product-Poisson approximation for all cycle counts in a logarithmically truncated window. It is obtained from the marked switching identity by an approximate Campbell formula and configuration-space Poisson Stein method, after which short and long cycles are restored.

**Status:** current research manuscript. The total-cycle and functional-count proof chain has a scoped audit and explicit dependency record.

### Poisson approximation and lattice Edgeworth expansions for total Luce cycles

[PDF](output/pdf/total-cycle-edgeworth.pdf) · [LaTeX](papers/total-cycle-edgeworth/total-cycle-edgeworth.tex)

Let $K_n$ be the total number of cycles and $\mu_n=\mathbb E K_n$. For comparable-rate Luce permutations this paper proves the stronger exact-mean Poisson approximation
$$
d_{\mathrm{TV}}\!\left(\mathcal L(K_n),\operatorname{Pois}(\mu_n)\right)
=
O_\kappa\!\left(\frac{(\log\log n)^2}{\log n}\right),
$$
which yields the sharp Berry--Esseen order $(\log n)^{-1/2}$. Its first lattice Edgeworth expansion determines the exact leading Kolmogorov constant $2/(3\sqrt{2\pi})$.

The paper also gives the variance asymptotic, a continuity-corrected second-order lattice expansion retaining the exact coefficient $\operatorname{Var}K_n-\mu_n$, and signed Poisson--Charlier approximations at every fixed order. The proof uses a passive-mark Poisson core from the switching theory and discrete Poisson smoothing; it does not use the nonlinear arithmetic analysis required for logarithmic permutation order.

**Status:** current research manuscript. Exact-mean centering and the lattice phase are essential; profile-dependent limiting mean and higher-cumulant constants remain separate open questions.

### Microscopic cycles and sparse entries for regular Luce profiles

[PDF](output/pdf/regular-profile-cycles.pdf) · [LaTeX](papers/regular-profile-cycles/regular-profile-cycles.tex)

For sampled positive continuous profiles
$$
\theta_{n,i}=a_n\bigl(f(i/n)+\varepsilon_{n,i}\bigr),
\qquad
\max_i|\varepsilon_{n,i}|\to0,
$$
this paper proves joint independent Poisson limits for every fixed vector of cycle counts. Their means are cyclic traces of the microscopic Luce kernel, and those limiting means satisfy
$$
\lambda_r=\frac1r+O\!\left(\frac{q^r}{r}\right)
$$
for some $q<1$ depending on the limiting profile.

The same local-entry theory yields fixed-width diagonal-band Poisson laws, sparse-entry and thin-graph laws, deterministic-permutation overlap laws, and a transverse thin-curve theorem. The proof develops the separated bulk local estimate together with endpoint, collision, gap, and target-crowding envelopes sufficient to sum fixed factorial moments globally.

**Status:** audited current manuscript. The standalone extraction was checked against the frozen monolith, adversarially audited, and changed only by the localized clarifications recorded in its audit and repair files.

### Poisson--Dirichlet universality for Luce permutations

[PDF](output/pdf/poisson-dirichlet-luce.pdf) · [LaTeX](papers/macroscopic-pd/poisson-dirichlet-luce.tex)

Under only a fixed bound on the ratio of the largest to the smallest positive rate, the ranked normalized cycle lengths converge in $\ell^1$ to $\operatorname{PD}(1)$, while the size-biased deletion sequence converges in $\ell^1$ to $\operatorname{GEM}(1)$. Consequently, the normalized cycle length containing a uniformly chosen label converges to $\operatorname{Unif}(0,1)$.

The proof is independent of the mesoscopic and total-cycle theorems. Its main ingredients are the clock-slab permanental representation, hereditary flatness under predictable exploration, scale-sensitive rooted closure, deletion stability, and a regenerative GEM induction with residual-mass control.

**Status:** audited current manuscript. The standalone extraction and all localized post-audit clarifications are recorded in the repository provenance and repair files.

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

The regular-profile paper adds an active standalone copy without changing any archived byte. Its audit covers the separated local estimate, endpoint/collision envelopes, improper integrability, factorial moments, total variation, long traces, sparse entries, and deterministic overlaps; its six localized clarification sets are regression-checked. The PD/GEM paper adds an active standalone copy without changing any archived byte. The extraction check certifies coverage and cross-reference closure; the later adversarial audit separately checks the clock-slab conditioning, adaptive prefix law, rooted closure, deletion stability, regeneration, GEM induction, residual-mass control, and $\ell^1$ passage. The audit found no fatal gap and recommended six publication-level clarifications, all of which are recorded and regression-checked. This remains an internal review, not formal verification or independent external refereeing.

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
