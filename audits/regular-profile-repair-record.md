# Regular-profile audit repair record

Date: 11 October 2026.

Source audit: `audits/regular-profile-proof-audit.md`.

## Verdict inherited from the audit

The adversarial audit found no fatal gap in the regular positive-profile
microscopic-cycle and sparse-entry manuscript. The repair stage therefore
applies clarification edits only. No principal theorem is weakened or
strengthened.

## Resolved findings

1. **Uniform profile approximation.** Added compact-uniform convergence of
   `A_{n,P}` through second derivatives and of the covariance kernels and
   their first derivatives, uniformly over bounded-size removed sets. The text
   now states explicitly that uniformity is for the fixed triangular array
   satisfying `max|epsilon| -> 0`, not for an unquantified class of arrays.
2. **Integrated-saddle checklist.** The separated bulk proof now lists the
   `C^2`, nonsingularity, covariance-continuity/nondegeneracy, LLT,
   off-saddle/Gaussian-tail, and equicontinuity inputs used by the abstract
   integrated-saddle lemma.
3. **Summability and order of limits.** Expanded the single endpoint value in
   the base case of the gap-envelope induction and stated the limit order
   `n -> infinity`, then collision cutoff to zero, then endpoint cutoff to
   zero.
4. **Cycle combinatorics.** Displayed the exact cyclic-rotation normalization
   `prod_r r^{-k_r}` and explained why no `k_r!` factor appears.
5. **Standard convergence tools.** Added book references for the multivariate
   method of moments, the discrete Scheffe argument, and the
   converging-together lemma.
6. **Spectral and sparse bookkeeping.** Made the complex equality case in
   Jensen/Cauchy--Schwarz explicit, derived `E C_r -> lambda_r` from the
   first mixed factorial moment before the long-trace iterated limit, and
   recorded the repeated-edge contribution in the sparse deterministic
   product sum.

## Scope preservation

The repaired manuscript still assumes exactly the sampled positive-profile
hypothesis from the archive. It does not claim arbitrary comparable arrays,
growing cycle lengths, endpoint-singular profiles, a quantitative
total-variation rate, or a finite-`n` uniform-in-cycle-length trace theorem.

All original labels remain present. The frozen archive is unchanged. The CI
repair checker strips the marked clarification blocks from the active
mathematical sections and verifies byte-for-byte recovery of the initial
mechanical extraction.

This remains an internal adversarial audit and localized repair, not formal
verification, novelty certification, or independent peer review.
