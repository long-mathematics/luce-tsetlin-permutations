# Adversarial proof audit: endpoint-regular fixed-point universality

Date: 12 October 2026.

Audited source: `papers/endpoint-regular-universality/endpoint-regular-universality.tex` on the mechanical extraction branch. Frozen comparison source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex` at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## Scope and review boundary

This audit covers uniform endpoint regular variation, the automatic partial-sum bound, weighted regularly varying sums and product envelopes, the endpoint Gumbel saddle and anisotropic local-limit package, the separated fixed-point estimate, the logarithmic fixed-point Poisson process and factorial moments, the displacement law, mesoscopic tangent measure, multiplicative endpoint kernel, and microscopic endpoint permutation. It compares every extracted theorem with the frozen source, traces all external inputs, and edits no manuscript text or theorem status.

## Executive verdict

**No fatal mathematical gap was found.** The manuscript supports all archived conclusions under Definition `def:endpoint-rv`. In particular:

- the fixed-point process on logarithmic terminal coordinates converges locally to a Poisson process of intensity `c_gamma dx`;
- `E(F_n)_r ~ (c_gamma log n)^r` for every fixed `r`, hence `E C_1 ~ c_gamma log n` and `F_n/(c_gamma log n) -> 1` in probability;
- the endpoint displacement law, mesoscopic tangent-measure law, multiplicative-kernel semigroup identity, and microscopic endpoint permutation limit all hold in the stated modes of convergence.

The proof architecture is coherent and self-contained. Six localized clarifications are recommended before later promotion; none changes a hypothesis, constant, topology, quantifier, or proof strategy.

## Result-by-result verdict

| Component | Verdict |
| --- | --- |
| Uniform endpoint regular variation definition and sampled-profile example | Pass |
| Automatic endpoint partial-sum bound | Pass |
| Weighted regularly varying terminal sums | Pass; collect the Potter-uniformity bookkeeping |
| Endpoint product envelope | Pass |
| Endpoint Gumbel saddle geometry | Pass |
| Endpoint interval blocks and anisotropic LLT | Pass |
| Mixed localization, product localization, covariance stability | Pass |
| Separated endpoint local estimate | Pass; list the integrated-saddle checklist |
| Endpoint fixed-point universality and factorial moments | Pass |
| Endpoint displacement law | Pass |
| Uniform mesoscopic Laplace sums | Pass |
| Conditional rank self-averaging | Pass |
| Mesoscopic endpoint tangent measure and rectangle law | Pass; state the convergence-determining class precisely |
| Multiplicative semigroup and diagonal traces | Pass |
| Microscopic endpoint permutation | Pass; expand the tail/bijection argument |

## Detailed audit

### 1. Uniform endpoint regular variation

The normalization by `s_n` is harmless because a common rate multiplier does not alter the Luce order. Conditions (ER1)--(ER3) give exactly the three controls used later: uniform regular variation on every sublinear terminal window, nondegeneracy in the macroscopic bulk, and global monotonicity.

The sampled-profile example satisfies the definition: the uniform convergence theorem for slowly varying functions gives (ER1) on arbitrary sublinear windows; compact positivity gives (ER2); and the stated global monotonicity gives (ER3). The manuscript correctly warns that eventual endpoint monotonicity alone is insufficient for the full triangular array.

### 2. Partial sums and weighted endpoint sums

For sublinear `a`, the normalized partial sum is a Riemann sum for `int_0^1 x^gamma dx`; Potter bounds control the small-`b` tail. For `a` of macroscopic order, monotonicity plus (ER2) gives a positive lower bound from the interval `[a/2,a]`. This proves the uniform partial-sum inequality.

For the weighted sums, the proof separates `b/a` into a compact multiplicative window, a small lower tail, a Potter-controlled upper tail, and the far tail beyond `B_n=a R_n`. On the compact window the uniform convergence theorem yields the desired Riemann integral. The small tail has only `O(epsilon a)` terms; the medium tail is dominated by an integrable stretched exponential; and the far tail is killed by the logarithmic choice of `R_n`. These estimates are uniform for `kappa` in compact subsets of `(0,infinity)` and survive deletion of finitely many summands.

The three special sums and the variance identity follow algebraically. The proof is correct; its repeated Potter choices should be summarized in one explicit uniform-envelope statement.

### 3. Endpoint product envelope

The Luce order in terminal coordinates is a size-biased deletion chain. Conditional on the residual set when coordinate `a` can be fixed, the partial-sum lemma bounds the total residual rate below by a constant multiple of `a lambda_{n,a}`. Thus the conditional chance of deleting `a` at its required rank is `O(1/a)`. Ordering a finite prescribed set by decreasing terminal level and iterating conditional expectations gives the product bound. No independence of the fixed-point indicators is assumed.

This envelope is strong enough to dominate all fixed factorial moments and logarithmic diagonal errors.

### 4. Endpoint saddle and anisotropic local limits

Under the Gumbel representation, conditional on a specified priority, the fixed-point event is a Bernoulli cumulative-count point event. The weighted regular-variation sums determine the limiting mean, derivative, and covariance on the natural `1/a` terminal scale. The saddle equation has a unique solution and converges to `K_gamma`; its derivative is of order `a` and the variance is of order `a`.

For several multiplicatively separated coordinates, the saddle vector is ordered and its coordinates lie in separated scale windows. The endpoint interval-block lemmas verify the adjacent-mass conditions required by the shared anisotropic Fourier and chain-comparison toolkit. Bounded exponential tilts preserve covariance nondegeneracy and lattice aperiodicity. The mixed localization lemmas remove noncompact regions, while product localization and covariance stability justify freezing the covariance at the saddle.

The integrated Gaussian determinant cancels the Jacobian determinant. Each specified density/derivative ratio tends to `c_gamma/a_j`, producing the separated joint estimate

`P(I_{n,a_j}=1 for all j) ~ c_gamma^r/(a_1...a_r)`.

No missing determinant or cyclic factor was found.

### 5. Fixed-point point process and factorial moments

On a bounded logarithmic interval, terminal coordinates lie in one bounded multiplicative window and the harmonic sum converges to interval length. Restricting to logarithmically separated tuples allows the separated joint estimate; the product envelope shows that the weighted mass of excluded logarithmic diagonals is `O(eta)`. Letting `eta` decrease yields the mixed factorial moments of independent Poisson counts.

The passage from interval counts to the vague point-process limit is valid: the product envelope gives uniform expected mass on compact logarithmic intervals, and step-function approximation transfers the count-vector convergence to Laplace-functional convergence for compactly supported continuous tests.

For full factorial moments, the central range carries harmonic mass `log n+O(log log n)`, while the lower and upper endpoint ranges carry only `O(log log n)`. The product envelope removes all non-separated configurations. Thus the factorial asymptotics and law of large numbers follow.

### 6. Displacement law

Conditional on `E_{n,a}=lambda_{n,a}T_{n,a}=u`, the terminal rank is a sum of independent Bernoulli indicators with mean asymptotic to `a A_gamma u^{-1/gamma}` and variance `O(a)`. For `a->infinity`, `a=o(n)`, conditional concentration makes the normalized rank converge to that deterministic function of `u`. Since `E_{n,a}` is standard exponential, the displayed displacement distribution follows by continuous mapping. The endpoint and compact-`u` truncations are controlled by exponential tails and the uniform Laplace-sum estimates.

### 7. Mesoscopic tangent measure

For `a` in a compact multiple of `b_n`, uniform mesoscopic Laplace sums identify the conditional mean rank at scale `b_n`. Conditional variance is at most the mean, so Chebyshev gives uniform self-averaging outside an event `E_{n,a}<epsilon`; the latter has probability at most `epsilon`.

Replacing the actual ranks by their conditional means costs `o(1)` in expected test-function error. The replacements are independent functions of the independent exponentials, so their empirical variance is `O(1/b_n)`. The expectation is an ordinary Riemann sum, followed by the change of variables from the exponential mark to the second coordinate. This yields the density `K_gamma(x,y)` and convergence in `L^1` for every compactly supported continuous test function, hence vague convergence in probability.

The two marginal calculations show bistochasticity. The rectangle corollary follows because rectangle boundaries have zero mass under the continuous density.

### 8. Multiplicative kernel and microscopic endpoint permutation

Writing the kernel in logarithmic ratio coordinates turns composition into additive convolution, giving the semigroup and diagonal trace formulas exactly.

For the microscopic limit, finite-dimensional rate ratios converge to `b^gamma`. Coupling through the same independent exponentials gives almost-sure convergence on every fixed finite set. The tail comparison uses Potter lower bounds and summability of `exp[-c b^gamma]` after conditioning away from zero values of the finitely many marked exponentials. Thus, with high probability, no distant coordinate changes the first `m` ranks. This proves finite-dimensional convergence in the product topology.

The limiting random map is injective because the continuous clock values are almost surely distinct. It is surjective because every finite rank is attained by one of the countably ordered clock values and the clock set is locally finite above each positive threshold; equivalently, the rank construction is the order-isomorphism induced by the distinct values `E_b/b^gamma`. The theorem is correct, though this final bijection argument should be expanded.

## Uniformity and scope

All local joint estimates are for fixed tuple size and fixed multiplicative separation. Endpoint regular variation is uniform on arbitrary sublinear windows as stated in (ER1), while macroscopic control comes separately from (ER2) and monotonicity. The manuscript does not claim quantitative rates, growing tuple size, arbitrary nonmonotone endpoint arrays, or global Poisson approximation for the total fixed-point count.

## Imported results

The external inputs are the uniform convergence theorem and Potter bounds for slowly varying functions from Bingham--Goldie--Teugels; standard Fourier inversion, exponential tilting, Bernstein/Chernoff and Chebyshev inequalities; mixed factorial-moment and Laplace-functional criteria for Poisson processes; and standard vague-convergence/continuous-mapping facts. Every model-specific endpoint sum, saddle, localization, covariance, and tail estimate is internal.

## Localized repairs recommended before promotion

1. State one uniform Potter envelope that is subsequently reused in all endpoint sum and tail estimates.
2. Collect the consequences of (ER1)--(ER3), including the automatic partial-sum and far-tail bounds, into a short reusable paragraph.
3. Before the separated local estimate, list explicitly the anisotropic LLT, mixed localization, covariance stability, ordered-chamber, and equicontinuity inputs to the integrated saddle.
4. In the fixed-point factorial-moment proof, display the weighted logarithmic-diagonal estimate and the order in which `n`, separation, and endpoint cutoffs are taken.
5. In the tangent-measure theorem, name a countable convergence-determining subclass of `C_c((0,infinity)^2)` and cite the vague-convergence criterion.
6. In the microscopic endpoint theorem, expand the uniform tail removal and the almost-sure surjectivity argument for the limiting random permutation.

## Final status recommendation

The theorem package passes this internal adversarial audit. Repairs are deliberately deferred by the decomposition prompt, so the paper should remain a **working mechanical extraction with audit passed and repairs pending**. This review is not formal verification, novelty certification, or independent external refereeing.
