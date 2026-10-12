# Adversarial proof audit: boundary laws for Luce rankings

Date: 12 October 2026.

Audited source: `papers/boundary-laws/boundary-laws.tex` on the mechanical extraction branch. Frozen comparison source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex` at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## Scope and review boundary

This audit covers the exponential-race identity, the vanishing-block implantation proposition, the exact top-window total-variation identity, the exact one-sided relative defect, the birthday transfer, finite bottom-window convergence, terminal leakage, and the logarithmic phase diagram. It compares every extracted statement with the frozen source and checks all external inputs. The audit branch changes only this report; it does not edit the manuscript or alter theorem status.

## Executive verdict

**No fatal mathematical gap was found.** Every principal statement follows under its archived hypotheses. The extraction preserves all hypotheses, identities, quantifiers, and limiting conclusions. Six localized clarifications are recommended before later promotion, but none changes a theorem statement or proof strategy.

## Result-by-result verdict

| Result | Verdict |
| --- | --- |
| Exponential-race representation | Pass |
| Vanishing-block implantation | Pass; quantify the final permuton comparison explicitly |
| Exact top-window total variation | Pass; state the total-variation normalization |
| Exact one-sided relative defect | Pass; expand the simultaneous prefix-maximization sentence |
| Birthday transfer | Pass |
| Finite bottom-window convergence | Pass |
| Terminal leakage | Pass; invoke Tonelli explicitly and separate endpoint cases |
| Log-log phase diagram | Pass; cite the logarithmic series test |

## Detailed audit

### 1. Exponential-race representation

For independent clocks `X_i` of rates `theta_i`, the probability of a prescribed increasing order is obtained by exposing the minimum recursively. The minimum label has probability `theta_i/sum theta`, and exponential memorylessness leaves independent residual clocks with the same rates. Iterating gives exactly the Plackett--Luce product. No normalization or conditioning issue is hidden.

### 2. Vanishing-block implantation

Let `tau_r=pi_n^{-1}(r)` and assign rates `R_n^{m_n-r+1}` to the implanted labels, with all other rates one and `R_n/n -> infinity`. For adjacent implanted clocks,

`P(X_{tau_r} >= X_{tau_{r+1}})=1/(R_n+1)`;

for the final implanted clock and the minimum background clock,

`P(X_{tau_{m_n}} >= Y_n)=(n-m_n)/(R_n+n-m_n)`.

The union bound tends to zero because `m_n/R_n=(m_n/n)(n/R_n)->0` and `n/R_n->0`. On the complementary event the first `m_n` labels in draw order are `tau_1,...,tau_{m_n}`, so `sigma_n(tau_r)=r=pi_n(tau_r)`.

The step profile converges pointwise almost everywhere to one because `m_n/n->0`. Conditional on the successful implanted block, the remaining equal-rate labels are uniformly ordered. Removing the first `m_n` rows and positions changes empirical permuton mass by at most `m_n/n`, while the rescaled uniform permutation on the remaining labels converges to Lebesgue measure. Hence the full permuton is uniform. The argument is correct; the last comparison should be written quantitatively rather than only narratively.

### 3. Exact top-window total variation

On the distinct-tuple set `D_k`,

`P_k(i)=Q_k(i) prod_{r=1}^{k-1}(1-prefix_r)^{-1} >= Q_k(i)`,

while `P_k` vanishes on the complement. Therefore the positive and negative parts of `P_k-Q_k` have equal mass `Q_k(D_k^c)`, giving the displayed identity under the convention `||P-Q||_TV=(1/2)sum |P-Q|`. Finally `Q_k(D_k)=k! e_k(theta)`. The proof is exact.

### 4. One-sided relative defect

For a distinct tuple,

`Q_k(i)/P_k(i)=prod_{r=1}^{k-1}(1-sum_{j<=r} theta_{i_j})`.

Every prefix sum is at most the sum of the `r` largest weights. Ordering those largest weights first realizes equality simultaneously for every prefix, so it minimizes the product. The formula follows. The archived proof is correct; it would benefit from saying explicitly that one ordering realizes all prefix maxima at once.

### 5. Birthday transfer

Under the product measure, `W_k=0` is exactly the distinct-tuple event. The result is an immediate reformulation of the exact total-variation identity.

### 6. Finite bottom-window convergence

For fixed labels, the finite-volume probability has the stated integral representation. As `N` grows, the finite product over unspecified clocks decreases pointwise to the infinite product and remains between zero and one. The remaining factor is the integrable joint density of the specified clocks restricted to the chamber. Dominated convergence therefore proves coordinatewise convergence. No exchange of an infinite sum is used at this stage.

### 7. Terminal leakage

For every `x>x_0`, the tail probabilities are summable, so Borel--Cantelli gives local finiteness of clock values above `x`. Applying this to a sequence decreasing to `x_0` shows that ordered points above the endpoint exist whenever `N_0>=k`.

For each ordered distinct label tuple, the displayed density describes exactly the event that those labels are the largest `k` clocks above the endpoint. These events are disjoint and their union is `{N_0>=k}`. Since all integrands are nonnegative, Tonelli justifies summing the integrals and yields the mass identity.

If `f(x_0)=infinity`, independence and the second Borel--Cantelli lemma give infinitely many clocks above `x_0`. If `f(x_0)<infinity`, then `x_0>0`, the Bernoulli parameters have finite sum and lie strictly below one, and the infinite product for `P(N_0=0)` is positive; hence the limiting law is defective. If `x_0=infinity`, every finite integration point lies below the convergence boundary and the infinite product vanishes, giving complete leakage. All cases are correct.

### 8. Log-log phase diagram

The assumption gives

`exp(-theta_i x) asymp i^{-beta x}(log i)^{-alpha x}`

for fixed `x`. The convergence abscissa is `x_0=1/beta`; at the boundary the series is `sum 1/[i(log i)^{alpha/beta}]`, which diverges exactly when `alpha/beta <= 1`. Combining this with terminal leakage gives the stated criterion.

## Imported results

The only external inputs are standard: exponential memorylessness; dominated and monotone convergence; Tonelli for nonnegative sums/integrals; the first and second Borel--Cantelli lemmas; the criterion for positivity of an infinite product; convergence of uniform-permutation permutons; and the logarithmic integral/series test. No result from another active manuscript is used.

## Localized repairs recommended before promotion

1. State the convention `||P-Q||_TV=(1/2)sum |P-Q|` before the exact top-window theorem.
2. In the relative-defect theorem, say explicitly that decreasing order of the largest `k-1` weights realizes every prefix maximum simultaneously.
3. Quantify the permuton conclusion in the implantation proof by bounding the exceptional mass by `m_n/n` and identifying the affine rescaling of the remaining uniform block.
4. In terminal leakage, invoke Tonelli explicitly when summing the nonnegative tuple densities.
5. Separate the cases `x_0=0`, finite positive `x_0`, and `x_0=infinity` in one short summary paragraph.
6. Add precise textbook citations for Borel--Cantelli, the infinite-product criterion, and the logarithmic series test.

## Final status recommendation

The theorem package passes this internal adversarial audit. Because the requested workflow defers repairs, the paper should remain a **working mechanical extraction with audit passed and repairs pending**. It should not yet be promoted to audited-current status. This review is not formal verification, novelty certification, or independent refereeing.
