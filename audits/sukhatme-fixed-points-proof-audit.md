# Adversarial proof audit: Sukhatme fixed points and the terminal Poisson process

Date: 12 October 2026.

Audited source: `papers/sukhatme-fixed-points/sukhatme-fixed-points.tex` on the mechanical extraction branch. Frozen comparison source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex` at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## Scope and review boundary

This audit covers the death-process product envelope, finite-tail estimates, the one-point terminal saddle and fixed-point mean, the complete anisotropic Fourier/tilting package, the separated terminal joint estimate, the logarithmic terminal Poisson point process, and fixed-order factorial moments. It checks every extracted theorem against the frozen source, traces the external inputs, and changes no manuscript text or theorem status.

## Executive verdict

**No fatal mathematical gap was found.** The extracted proofs support the archived conclusions for the Sukhatme rates `n,n-1,...,1`:

- `E F_n ~ e^{-1} log n`;
- the fixed-point process on logarithmic terminal coordinates converges locally to a Poisson point process of intensity `e^{-1} dx`;
- for every fixed `r`, `E(F_n)_r ~ (e^{-1} log n)^r`, hence `F_n/(e^{-1}log n) -> 1` in probability.

The separated joint estimate and all anisotropic local-limit inputs also pass. Six localized clarifications are recommended before later promotion; none changes a hypothesis, limiting constant, topology, or proof strategy.

## Result-by-result verdict

| Component | Verdict |
| --- | --- |
| Death-process product bound | Pass; expand the tower/conditioning order |
| Finite-tail geometric estimates | Pass |
| One-point saddle geometry | Pass |
| Sukhatme one-point estimate | Pass; state the full uniform range precisely |
| Fixed-point mean | Pass |
| Joint terminal saddle geometry | Pass |
| Coordinate and edge Fourier concentration | Pass |
| Weighted/truncated chain comparison lemmas | Pass |
| Mixed cumulative--interval localization | Pass |
| Anisotropic tilted local upper bound and terminal LLT | Pass |
| Product-scale localization and covariance stability | Pass |
| Terminal integrated saddle | Pass; list the application checklist |
| Separated terminal joint estimate | Pass |
| Local terminal Poisson point process | Pass; cite the point-process criterion |
| Fixed factorial moments and law of large numbers | Pass |

## Detailed audit

### 1. Death-process envelope

In terminal rate coordinates the independent clocks have rates `1,...,n`. Exposing them by increasing clock time is a pure-death chain: conditional on the alive set `S`, the next deleted rate is `b` with probability `b/sum_{c in S}c`. The event `I_{n,a}=1` is exactly deletion of rate `a` when the alive-set cardinality is `a`. If `a` is then alive, the total rate is at least `1+...+a`, so the conditional deletion probability is at most `2/(a+1)`.

For a finite set `A`, ordering its elements decreasingly matches the temporal order of their possible death levels. Iterated conditioning on the sigma-fields just before those levels gives the product bound. Earlier required events may already have failed, in which case the conditional probability is zero; otherwise the same one-step bound applies. No independence between the events is assumed.

### 2. Finite tails and one-point saddle

The finite geometric sums are compared to their infinite counterparts at time `x/a`. Uniformly when `a->infinity` and `a=o(n)`, the omitted tail is exponentially small relative to the main scale because `exp[-(n/a)x]` decays uniformly on compact positive `x`-ranges. The mean rank function is strictly monotone, and its rescaled limit has a unique saddle at `x=1`. Its derivative and variance are of orders `a` and `a`, uniformly in the admissible range.

Conditioning on `T_a=t`, the fixed-point event is an exact Bernoulli-sum point event. Compact saddle localization, the one-dimensional local CLT, and the derivative cancellation give

`P(I_{n,a}=1) = e^{-1}/a + o(1/a)`

uniformly on every range in which both `a->infinity` and `a/n->0`. Outside the central logarithmic range the death-process envelope gives a summable bound. Splitting the mean at `ceil(log n)` and `floor(n/log n)` therefore gives `E F_n ~ e^{-1} log n`.

### 3. Anisotropic local-limit toolkit

For several terminal clocks the cumulative-count vector has strongly unequal coordinate scales. The manuscript handles this rather than applying an isotropic LLT blindly.

- Coordinatewise Fourier concentration follows by multiplying characteristic functions of independent interval indicators and using the available variance in each cumulative direction.
- The weighted-chain comparison converts lower bounds on adjacent interval masses into a coercive quadratic form for cumulative coordinates.
- Truncation and boundary-aware comparison preserve coercivity after small edge blocks are removed.
- Forward-edge projection controls directions invisible to a naive cumulative estimate.
- Actual-mean Chernoff bounds and mixed cumulative--interval localization exclude noncompact regions under one common tilt.
- The anisotropic tilted local upper bound uses the diagonal scale matrix and uniform tilted covariance bounds; the determinant scale matches the product of terminal rates.

The support contains adjacent lattice increments generating the full lattice, so there is no hidden periodicity. The bounded tilts used in the saddle window preserve covariance nondegeneracy and Fourier decay.

### 4. Joint saddle and separated estimate

For logarithmically separated terminal rates, the joint saddle coordinates are ordered and lie in disjoint multiplicative windows. The ordered integration chamber therefore contains the entire product saddle neighborhood. Taylor expansion of the mean map has a triangular leading Jacobian with diagonal terms of order `a_j`; the covariance determinant and Gaussian integration factors cancel in the integrated saddle exactly as claimed.

Product-scale localization removes points outside the anisotropic window. Covariance stability shows that replacing the moving covariance by its saddle value creates a uniform `o(1)` relative error. The specified-clock densities then contribute one factor `e^{-1}/a_j` per coordinate, proving

`P(I_{n,a_j}=1 for all j) ~ e^{-r}/(a_1...a_r)`

uniformly over multiplicatively separated admissible tuples.

### 5. Poisson point-process limit

On a bounded logarithmic interval, admissible rates lie in one bounded multiplicative window, and the harmonic Riemann sum converges to interval length. Mixed factorial moments are first restricted to tuples separated by logarithmic distance `eta`; the separated joint estimate gives the product intensity. The excluded logarithmic diagonals have weighted harmonic mass `O(eta)` by the death-process product envelope. Letting `eta` decrease to zero gives the mixed factorial moments of independent Poisson counts.

The manuscript then upgrades interval-count convergence to vague convergence by approximating nonnegative compactly supported continuous test functions by step functions and using the uniform first-moment bound. The resulting Laplace functional convergence identifies the Poisson point process.

### 6. Full factorial moments

The central rate window from `log n` to `n/log n` contributes the full leading harmonic mass `log n+O(log log n)`. Separation on logarithmic scale and the preceding joint estimate give the main term. Non-separated tuples are negligible by the death-process envelope, and tuples outside the central window carry only `O(log log n)` harmonic mass. Hence every fixed factorial moment has the asserted leading asymptotic.

For `r=1,2`, the factorial moment asymptotics imply the stated law of large numbers by the variance identity. No unproved moment transfer from distributional convergence is used.

## Uniformity and scope

All uniform estimates are for fixed tuple size. The local asymptotics require `min a_j -> infinity`, `max a_j=o(n)`, and fixed multiplicative separation. The global factorial-moment theorem removes those restrictions by envelopes and summation. The paper does not claim uniformity for tuple size growing with `n`, a quantitative point-process rate, or arbitrary endpoint-regular profiles.

## Imported results

The only external inputs are standard Fourier inversion and exponential tilting for lattice sums, Bernstein/Chernoff concentration, convergence of mixed factorial moments for integer-valued vectors, and the Laplace-functional criterion for vague convergence of locally finite point processes. The historical Sukhatme and Renyi citations identify the rate pattern but are not used as proof inputs. All model-specific saddle, localization, covariance, and domination estimates are internal.

## Localized repairs recommended before promotion

1. State the one-point estimate's uniform range in one displayed sentence: `a->infinity` and `a=o(n)`, uniformly on compact auxiliary saddle ranges.
2. In the death-process lemma, identify the pre-death sigma-fields and write the tower-product argument explicitly.
3. Collect the tilted-LLT hypotheses actually verified by the interval-block and chain-comparison lemmas into one checklist before the terminal LLT.
4. In the integrated saddle, say explicitly why multiplicative separation places the whole product neighborhood inside the ordered chamber.
5. Display the weighted logarithmic-diagonal estimate used when `eta` tends to zero in the Poisson and factorial-moment arguments.
6. Add precise references for the multivariate factorial-moment criterion and the Laplace-functional characterization of vague point-process convergence.

## Final status recommendation

The theorem package passes this internal adversarial audit. Because repairs are deliberately deferred by the decomposition prompt, the paper should remain a **working mechanical extraction with audit passed and repairs pending**. This is not formal verification, novelty certification, or independent external refereeing.
