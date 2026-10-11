# Nonuniform Random Permutations

Research manuscripts on Luce/Tsetlin permutations, move-to-front/LRU orderings, and nonuniform card shuffles, including boundary and cycle laws, Poisson--Dirichlet universality, mesoscopic cycles, permutation order, riffle and shelf shuffles, and related Thorp-shuffle calculations.

Author of the manuscripts in `papers/`: **Christopher D. Long**.

The repository separates current manuscripts, working branches, historical audit material, and third-party material. Compilation and finite computations are checks of the written arguments; they are not independent peer review or formal verification.

## Read the papers

| Paper | Manuscript | PDF | LaTeX |
| --- | --- | --- | --- |
| I | Boundary, Terminal, Diagonal, and Cycle Limit Laws for Luce Permutations | [Read PDF](output/pdf/luce-boundary-cycle-laws.pdf) | [Source](papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex) |
| II | Mesoscopic cycles of comparable-rate Luce permutations: a switching proof of Conjecture 13.1 | [Read PDF](output/pdf/mesoscopic-luce-cycles.pdf) | [Source](papers/02-mesoscopic-luce-cycles/mesoscopic-luce-cycles.tex) |
| III | An Erdős--Turán Law for Comparable-Rate Luce Permutations | [Read PDF](output/pdf/luce-erdos-turan.pdf) | [Source](papers/03-luce-erdos-turan/luce-erdos-turan.tex) |
| IV | A Sharp Berry--Esseen Theorem and First Edgeworth Expansion for the Erdős--Turán Law of Comparable-Rate Luce Permutations | [Read PDF](output/pdf/luce-edgeworth.pdf) | [Source](papers/04-luce-edgeworth/luce-edgeworth.tex) |
| V | Erdős--Turán Universality after One Shuffle | [Read PDF](output/pdf/one-shuffle-universality.pdf) | [Source](papers/05-one-shuffle-universality/one-shuffle-universality.tex) |
| VI | Radial Extremality for LRU Caching and the Fill--Holst Conjecture ([arXiv:2605.26107](https://arxiv.org/abs/2605.26107)) | [Read PDF](output/pdf/radial-lru-extremality.pdf) | [Source](papers/06-radial-lru-extremality/radial-lru-extremality.tex) |
| VII | Residual-Mass Transform Order for LRU Caching and the Coupon Collector | [Read PDF](output/pdf/residual-mass-transform-order.pdf) | [Source](papers/07-residual-mass-transform-order/residual-mass-transform-order.tex) |
| VIII | Cycle Universality for a Single Thorp Shuffle | [Read PDF](output/pdf/thorp-cycle-universality.pdf) | [Source](papers/08-thorp-cycle-universality/thorp-cycle-universality.tex) |

The PDFs are committed deterministic snapshots compiled from the linked sources. CI rebuilds every document from a clean checkout and requires the rebuilt PDF to be byte-for-byte identical to the committed snapshot. Intermediate files are kept out of the repository.

## Theorem map

### I. Luce/Tsetlin boundary, microscopic, endpoint, and macroscopic laws

The stationary distribution of the Tsetlin library is the Luce distribution, equivalently the ranking induced by independent exponential clocks. The comprehensive manuscript develops four complementary regimes.

For uniformly positive continuous profiles it proves joint Poisson limits for every fixed cycle-count vector and an exponentially small correction to the uniform trace law:

$$
\lambda_r=\frac1r+O_f\left(\frac{q^r}{r}\right),\qquad 0<q<1.
$$

Under uniformly comparable positive weights, the ranked macroscopic cycle lengths converge to $\mathrm{PD}(1)$ and the size-biased deletion order converges to $\mathrm{GEM}(1)$.

For the Sukhatme profile and more general endpoint-regular profiles, the manuscript proves logarithmic fixed-point means, local terminal Poisson point processes, a global Poisson approximation for the fixed-point count, fixed-length endpoint-cycle asymptotics, and microscopic and mesoscopic endpoint limits. It also contains the exact top-window comparison identities and the bottom-window leakage theorem.

The manuscript's original open-problem section predates Paper II below; the mesoscopic conjecture recorded there is superseded by the later switching paper.

### II. Mesoscopic Luce cycles

For rates with a uniformly bounded largest-to-smallest ratio, Paper II proves

$$
\mathbb{E}C_{n,r_n}\sim\frac1{r_n}
\qquad
\text{whenever }r_n\to\infty\text{ and }r_n=o(n),
$$

and, for every $a_n\to\infty$ with $a_n=o(n)$, convergence of the rescaled cycle-length point process to the scale-invariant Poisson point process with intensity

$$
\frac{\mathrm{d}x}{x}.
$$

The final free-depth version proves its short-root estimate internally and does not import the macroscopic $\mathrm{PD}(1)$ or $\mathrm{GEM}(1)$ theorem. Its endpoint-mixing theorem is fixed-dimensional and annealed relative to a coarse clock environment; it does not claim a fully quenched arbitrary-deletion local law.

### III. Erdős--Turán universality for comparable-rate Luce permutations

For arbitrary comparable-rate triangular arrays, with no limiting profile assumption,

$$
\frac{\log\mathrm{ord}(\sigma_n)-\frac12(\log n)^2}
{\sqrt{\frac13(\log n)^3}}
\Rightarrow N(0,1).
$$

The proof combines the switching theory with an arithmetic product-to-least-common-multiple comparison.

### IV. Sharp normal approximation and first Edgeworth term

Writing $O_n=\mathrm{ord}(\sigma_n)$, $m_n=\mathbb{E}\log O_n$, and $L=\log n$, the quantitative supplement proves

$$
\mathrm{d}_{\mathrm K}\left(
\frac{\log O_n-m_n}{\sqrt{L^3/3}},N(0,1)
\right)
\le \frac{C_\kappa}{\sqrt L},
$$

and, uniformly in $x$,

$$
\mathbb{P}\left(
\frac{\log O_n-m_n}{\sqrt{L^3/3}}\le x
\right)
= \Phi(x)-\frac{\sqrt3}{8}(x^2-1)\varphi(x)L^{-1/2}
+o_\kappa(L^{-1/2}).
$$

Thus the $L^{-1/2}$ Kolmogorov order is optimal. The theorem uses the exact mean at this precision; an explicit deterministic center accurate to $o(L)$ is a separate problem.

### V. One-shuffle universality: riffle and shelf shuffles

Paper V proves a functional Erdős--Turán universality theorem for several nonexchangeable models after a single shuffle. In particular, if $\rho_n$ is obtained from the identity by one ordinary Gilbert--Shannon--Reeds $2$-riffle shuffle, then

$$
\frac{\log\mathrm{ord}(\rho_n)-\frac12(\log n)^2}
{\sqrt{\frac13(\log n)^3}}
\Rightarrow N(0,1),
$$

even though

$$
\mathrm{d}_{\mathrm{TV}}\left(
\mathcal{L}(\rho_n),\mathrm{Unif}(S_n)
\right)\longrightarrow1.
$$

The same cycle-index mechanism treats biased riffle shuffles under the stated nonconcentration hypothesis, major-index-biased permutations in the manuscript's parameter range, and asymmetric shelf shuffles under the stated uniformity assumptions.

A later Edgeworth/optimality strengthening is retained as a working branch below rather than silently replacing this stable manuscript.

### VI. Radial LRU extremality and move-to-front tails

[arXiv:2605.26107](https://arxiv.org/abs/2605.26107) proves that, for every nontrivial cache capacity, uniform popularity is the unique global minimizer of the exact stationary LRU hit rate. More sharply, every nonconstant straight-line ray away from the uniform popularity vector strictly increases the hit rate. In move-to-front language, the entire stationary search-cost distribution improves strictly in the usual stochastic order along such rays.

The proof uses the exponential-age representation of the stationary LRU stack and gives an explicit positive pair-square formula for the radial derivative. The conclusion is deliberately radial: the full Fill--Holst Schur-concavity/majorization principle is false, while this raywise positivity survives.

### VII. Residual-mass transform order

For the size-biased prefix $S_C(p)$, put $Q_C(p)=1-p(S_C(p))$. This sequel strengthens Paper VI from the mean hit rate to a transform order for the full residual miss mass, and connects that same random variable to coupon-collector discovery time:

$$
\mathrm{MR}_{\mathrm{LRU}}(C;p)=\mathbb{E}Q_C(p),
\qquad
\mathbb{E}_p[T_{C+1}-T_C]=\mathbb{E}Q_C(p)^{-1}.
$$

This paper is adjacent to the permutation-cycle program but uses the same Plackett--Luce/Gumbel size-biased ordering mechanism.

### VIII. Cycle universality for one physical Thorp shuffle

Paper VIII studies one random binary feedback-shift-register permutation, with the feedback function sampled **once and reused**. It obtains uniform joint cycle factorial-moment estimates for every fixed number of cycles, allowing arbitrary ratios of their lengths when their total length is below any fixed exponent less than two thirds of the dyadic state-space size. The two-sided estimate assumes each prescribed length is at least four times the register width.

The consequences include a truncated functional Erdős--Turán Gaussian law, independent Poisson limits on sets of bounded harmonic mass, a scale-invariant Poisson cycle process, a Dickman law for truncated cycle mass, and the uniform limit for the largest cycle below a cutoff. A separate quantitative full-vector Poisson theorem applies below the birthday scale. Exact short-cycle binomial laws and lower bounds for the full order and cycle count are also recorded.

**Scope:** The full one-shuffle Erdős--Turán conjecture, the exponent endpoint two thirds, and a full initial-vector Poisson approximation above the birthday range remain open. Paper VIII is an authored single-permutation cycle-statistics paper; the external OpenAI paper below studies mixing after multiple independent physical shuffles. [Scope, finite checks, and validation](papers/08-thorp-cycle-universality/README.md).

## Working branches

| Document | Status | PDF | LaTeX |
| --- | --- | --- | --- | --- |
| Functional Erdős--Turán Universality for Comparable-Rate Luce Permutations | Working functional/multivariate strengthening | [Read PDF](output/pdf/functional-luce-erdos-turan.pdf) | [Source](notes/working/functional-luce-erdos-turan.tex) |
| Erdős--Turán, Berry--Esseen, and Edgeworth Universality after One Shuffle | Working Edgeworth/optimality strengthening | [Read PDF](output/pdf/one-shuffle-edgeworth-optimality.pdf) | [Source](notes/working/one-shuffle-edgeworth-optimality.tex) |

These files are deliberately separated from the eight main manuscripts so that exploratory strengthenings are not presented as settled replacements.

## Mesoscopic total-cycle branch: audit status

A July candidate attempted to resolve both the mesoscopic cycle process and the total number of cycles. An adversarial audit found structural defects in that version, including the slab good event, adaptive-history treatment, and the factorial-moment-to-CLT step. The later free-depth switching manuscript gives a separate proof of the mesoscopic result, but this repository does **not** promote the total-cycle expectation/CLT claim to the established theorem list.

The historical sources are preserved for provenance:

- [resolution candidate](notes/provenance/mesoscopic-total-cycle-resolution-candidate.tex)
- [audit and repair note](notes/provenance/mesoscopic-audit-and-repair.tex)
- [free-depth endpoint audit](notes/provenance/free-depth-endpoint-audit.md)

See [repository status](notes/repository-status.md) for the dependency and review boundary.

## Thorp shuffle

The optimal-order Thorp mixing theorem below is an **external OpenAI result**, not a Long-authored manuscript. The distinct Long-authored one-physical-shuffle cycle theorem is Paper VIII above. A pinned copy of its LaTeX source is kept under `third_party/openai-thorp/` with the original Apache-2.0 license and provenance.

For $n=2^d$, its main theorem states

$$
\left\|q_d^{*(1600d)}-U_{2^d}\right\|_{\mathrm{TV}}\longrightarrow0,
\qquad
t_{\mathrm{mix}}(d)=\Theta(d).
$$

- [Read PDF](output/pdf/openai-thorp-mixing.pdf)
- [Source](third_party/openai-thorp/main.tex)
- [Conditional-flow source](third_party/openai-thorp/conditional-flow.tex)
- [References source](third_party/openai-thorp/references.tex)
- [Provenance and attribution](third_party/openai-thorp/README.md)
- [Apache-2.0 license](third_party/openai-thorp/LICENSE)

The repository also contains an [exact finite audit program](scripts/thorp_moment_audit.cpp) for a rooted cyclic-word factorial-moment identity associated with one physical Thorp shuffle. It verifies 156 identities for dimensions $d=2,3,4,5$ using exact integer arithmetic. These finite checks do not prove the asymptotic mixing theorem.

## Build and verification

On Debian/Ubuntu:

```sh
sudo apt-get install latexmk texlive-latex-extra texlive-fonts-recommended texlive-science lmodern poppler-utils python3 g++ make
```

From the repository root:

```sh
make pdf     # compile the eight papers, two working notes, and the pinned external Thorp paper
make check   # verify hashes, rebuild PDFs byte-for-byte, and check README links/math syntax
make test    # repository unit tests
make verify  # run exact finite Thorp and Paper VIII reproducibility checks
```

All canonical LaTeX sources are standalone except the pinned Thorp source, which includes its companion file. PDFs are committed under `output/pdf/`; intermediates stay in `.build/`. The [manifest](output/pdf/manifest.json) records source hashes, PDF hashes, and page counts.

The README intentionally uses GitHub's dollar-delimited inline math and double-dollar display blocks. It defines no custom LaTeX macros. The repository linter uses an explicit allowlist for the TeX commands appearing here, so manuscript-only or unsupported commands cannot silently break GitHub rendering.

## Scripts

| Script | Purpose |
| --- | --- |
| [Build and snapshot checker](scripts/build.py) | Compile manuscripts, refresh the PDF manifest, verify deterministic PDF bytes and hashes, and lint README links and math syntax |
| [Thorp exact finite audit](scripts/thorp_moment_audit.cpp) | Exact integer check of 156 rooted cyclic-word factorial-moment identities in dimensions $d=2,3,4,5$ |
| [Paper VIII reproducibility](scripts/thorp-cycle-universality/reproduce.py) | Re-run preserved multiscale finite checks and the additions audit; optionally rebuild Paper VIII and compare deterministic snapshots |

The repository tests are in [`tests/test_repository.py`](tests/test_repository.py).

## Repository layout

```text
papers/                     eight current Long manuscripts
notes/working/              active strengthenings
notes/provenance/           historical candidates and audits
third_party/openai-thorp/   pinned external source and license
scripts/                    build checks and finite computations
output/pdf/                 committed PDF snapshots and manifest
tests/                      repository regression tests
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Mathematical changes should be separated from editorial/build changes. Do not infer proof status from a filename or chronology alone; update the status note when a theorem is promoted, weakened, or withdrawn.

## License

Repository-authored code and documentation are available under the [MIT License](LICENSE). Individual manuscript copyright remains with the author. The pinned OpenAI Thorp source is redistributed under its [Apache-2.0 license](third_party/openai-thorp/LICENSE).
