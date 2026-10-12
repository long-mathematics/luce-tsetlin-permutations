# Adversarial proof audit: global endpoint Poisson approximation

Date: 12 October 2026.

Audited source: `papers/global-endpoint-poisson/global-endpoint-poisson.tex` on the mechanical extraction branch. Frozen comparison source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex` at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## Scope and review boundary

This audit covers the endpoint-regular preliminary theory imported into the standalone source, the approximate-Palm Stein bound, the terminal-rank transposition and exact likelihood ratio, the uniform endpoint package, quantitative one-dimensional saddle, likelihood-ratio tails, swap--Palm approximation, exact rank-swap effect, two-cycle transition bounds, weighted two-cycle summability, the final total-variation estimate, and the normal limit. Every principal theorem is compared with the frozen source. The audit changes no manuscript text or theorem status.

## Executive verdict

**No fatal mathematical gap was found.** Under the archived uniformly endpoint-regularly varying hypotheses, the proof establishes

`d_TV(L(F_n), Pois(E F_n)) = O((log log n)/sqrt(log n))`

and hence the exact-mean central limit theorem. The Sukhatme specialization with mean asymptotic `e^{-1} log n` follows. The approximate-Palm coupling is correctly normalized, the rank transposition is an exact measurable map, and the only count discrepancy is the explicitly controlled two-cycle term.

Six localized clarifications are recommended before later promotion; none changes a hypothesis, rate, conclusion, or proof strategy.

## Result-by-result verdict

| Component | Verdict |
| --- | --- |
| Approximate-Palm Stein bound | Pass; state TV convention and Stein factors |
| Exact terminal-rank transposition likelihood ratio | Pass; make the chamber bijection explicit |
| Uniform endpoint package | Pass |
| Likelihood-ratio tail sum | Pass |
| Quantitative one-dimensional saddle | Pass; collect the uniform local-CLT checklist |
| Logarithmic order of the mean | Pass |
| Quantitative swap--Palm approximation | Pass; display normalization once |
| Exact count effect of rank swap | Pass |
| Two-cycle transition bound | Pass |
| Weighted two-cycle summability | Pass |
| Global Poisson approximation and CLT | Pass; expand the final rate arithmetic/reference |

## Detailed audit

### 1. Approximate-Palm Stein lemma

For `W=sum X_a`, the Poisson Stein equation is applied with parameter `lambda=E W`. Under the exact Palm law for `X_a=1`, the standard identity

`E[X_a f(W)] = p_a E[f(W^a)]`

is valid. Replacing the exact Palm variable by `Y^(a)` creates a total-variation error bounded by the first Stein difference. The other error is the coupling discrepancy `E|W+1-Y^(a)|`. The displayed coefficients are the standard Poisson Stein factors `(1-e^{-lambda})/lambda` and `(1-e^{-lambda})/sqrt(lambda)`. The lemma is correct; the manuscript should state its TV normalization and cite the chosen Stein-factor convention.

### 2. Terminal-rank transposition

For a no-tie clock vector, let `b` be the coordinate occupying terminal rank `a`. Swapping the clocks of `a` and `b` is an involution between the original chamber and the chamber where `a` is fixed. The exponential density ratio is the stated likelihood ratio. Summing over the disjoint possible values of `b` proves that the pushforward law is absolutely continuous with the exact displayed Radon--Nikodym derivative. No Jacobian appears because the map is a coordinate transposition.

The conditional Palm law is therefore compared to a fully explicit pushforward of the original clock law, not to an informal conditioning operation. The argument passes; the partition of clock space into rank chambers should be stated more explicitly.

### 3. Uniform endpoint package and likelihood tails

The cutoffs `U_n` and `V_n` leave a polylogarithmic separation from the macroscopic endpoint. Potter bounds give two-sided power envelopes for all rate ratios below `V_n`; monotonicity then controls the remaining tail. The saddle is bracketed between fixed scaled constants because a fixed multiple of `a` contributes order `a` mass at the lower bracket, while dyadic/Potter summation and the far-tail exponential bound make the upper bracket mass smaller than `a-1`.

The weighted moment sums through order four are `O(a)`, and fixed subintervals of `[a,2a]` give matching lower bounds through order two. This yields uniform variance and derivative nondegeneracy and a block of `ca` Bernoulli parameters bounded away from zero and one.

The likelihood-tail lemma follows from

`kappa x + log(M)/(x-1) >= kappa x/2 + c sqrt(log M)`

and the weighted first-moment estimate. It is uniform over the full rate range. These modules pass.

### 4. Quantitative endpoint saddle

The Bernoulli sum has variance of order `a`, derivative of order `a lambda_a`, and at least `ca` nondegenerate summands. Fourier inversion gives a uniform local expansion with absolute error `O(a^{-1})`; on the polylogarithmic saddle window this is a polynomially small relative error. Deleting one Bernoulli summand changes the mean and variance by `O(1)`, so the deleted/full local-probability ratio is `1+O(a^{-rho})`.

Taylor expansion in the scaled coordinate `u=lambda_a sqrt(a)(t-t_a^*)`, together with the Gaussian local upper bound, controls the central integral and shows exponentially small Palm mass outside `|u| <= (log(a+2))^{1/4}`. The prefactor is exactly

`lambda_a exp(-lambda_a t_a^*)/D_a(t_a^*)`.

The proof is quantitatively consistent. The local-CLT, derivative, variance, and tail hypotheses should be listed in one checklist.

### 5. Swap--Palm approximation

On the high-probability central saddle event, the exact likelihood ratio factors over the clock occupying rank `a`. The deleted-summand ratio from the preceding lemma controls the local part. For a much faster coordinate, the likelihood-ratio tail is bounded by the tail-sum lemma; slower coordinates and the complement of the central event are controlled by the uniform endpoint package and Palm concentration.

The final identity

`p_a E[R_a 1_C | I_a=1] = nu_a(C)`

correctly normalizes the pushed-forward law. Integrating `|p_a R_a-1|` under the Palm law is equivalent to twice the total-variation distance under the manuscript's convention. The resulting error is summable with weight `1/a` over the main endpoint range.

### 6. Exact count effect and two-cycle control

If `a` is fixed, the transposition is the identity. Otherwise the coordinate at rank `a` is swapped with `a`, fixing `a` and changing no other ranks except the partner's. The partner becomes fixed exactly when the old pair was a two-cycle. This gives the signed identity

`F(T_a T)=F+1-I_a+J_a`

and the absolute discrepancy `I_a+J_a` because those indicators are mutually exclusive.

For a two-cycle `a<b`, the death process must delete `a` at level `b` and later `b` at level `a`. The partial-sum bound gives the two conditional factors and their product

`C min{1/(ab), lambda_a/(b lambda_b)}`.

The weighted sum is finite on `a<=U_n`: below `V_n`, Potter bounds and a split at `b=a^{1+1/beta}` give a summable series; above `V_n`, the polylogarithmic gap makes the contribution `o(1)`. The remaining `a>U_n` range has only `O(log log n)` harmonic mass. The calculation passes.

### 7. Final Stein estimate

The first Stein term is

`lambda^{-1} sum p_a(p_a+q_a)`

up to the bounded Stein factor. Here `sum p_a^2=O(1)` and `sum p_a q_a=O(log log n)`, while `lambda=m_n asymp log n`; hence it is `O(log log n/log n)`.

For the approximate-Palm term, data processing contracts total variation from clocks to the fixed-point count. The main range contributes `O(1)` after weighting the summable swap--Palm errors by `p_a<=C/a`; the tail contributes `O(log log n)`. Multiplication by the second Stein factor `O(m_n^{-1/2})` gives the dominant rate `O(log log n/sqrt(log n))`.

The endpoint fixed-point theorem supplies `m_n~c_gamma log n`. A Poisson variable with this mean satisfies the ordinary centered CLT, and total variation transfers it to `F_n`. The rate arithmetic and centering are correct.

## Uniformity and scope

All quantitative estimates are uniform for `A_0<=a<=U_n` under a fixed endpoint-regular family with fixed index and regular-variation constants. The proof treats the remaining indices by global `C/a` bounds. It does not claim a sharper Poisson error, a profile-uniform constant over unconstrained regular-variation families, or joint Poisson approximation of a growing collection of endpoint indicators.

## Imported results

The external inputs are Potter bounds and the uniform convergence theorem for slowly varying functions; standard Poisson Stein-equation bounds; Fourier inversion, exponential tilting and concentration for Bernoulli sums; data processing for total variation; and the ordinary Poisson central limit theorem. Every model-specific transposition, likelihood-ratio, saddle, Palm, two-cycle, and summability estimate is proved internally.

## Localized repairs recommended before promotion

1. State the total-variation normalization and the precise Poisson Stein factors used in the approximate-Palm lemma.
2. Expand the terminal-rank transposition proof into an explicit partition by rank chambers and note the unit Jacobian.
3. Collect the uniform endpoint-package consequences actually used in the saddle and Palm proofs into a dependency checklist.
4. State once that the swap density integrates to one and display the identity relating its Palm expectation to the pushforward law before the error decomposition.
5. In the weighted two-cycle proof, display the two summation ranges and the split-point calculation in a compact standalone estimate.
6. In the final theorem, display the two Stein contributions and cite the Poisson CLT/total-variation transfer explicitly.

## Final status recommendation

The theorem package passes this internal adversarial audit. Repairs are deliberately deferred by the decomposition prompt, so the paper should remain a **working mechanical extraction with audit passed and repairs pending**. This review is not formal verification, novelty certification, or independent external refereeing.
