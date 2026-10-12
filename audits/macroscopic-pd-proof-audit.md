# Adversarial audit of the macroscopic PD/GEM manuscript

Audit date: 11 October 2026  
Audited branch: `migration/macroscopic-pd-extraction`  
Audited head: `025fbbc2ad072aad0577a2fdd5aec5edd640b748`  
Audited source: `papers/macroscopic-pd/poisson-dirichlet-luce.tex`  
Audited source SHA-256: `a14de186ecc0fdb48763bebf260ca56755bc6670570c31bfbce6c419c2f9f73e`  
Frozen source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`, archived lines 2199--3565  
Frozen commit: `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`

This is a mathematical proof audit, not an extraction check. The extraction-preservation review is recorded separately in `audits/macroscopic-pd-extraction.md`. No manuscript file was edited during this audit.

## 1. Executive verdict

### Main conclusion

I found **no fatal mathematical gap** in the extracted proof. The manuscript supports the stated theorem under the exact hypothesis

$$
\sup_n \frac{\max_i\theta_{n,i}}{\min_i\theta_{n,i}}<\infty.
$$

In particular, the proof supports:

1. convergence of the ranked normalized cycle lengths to `PD(1)` in the decreasing `ell^1` simplex;
2. convergence of the successive uniform-root deletion order to `GEM(1)` in `ell^1`;
3. convergence of the normalized cycle length of a uniform label to `Unif(0,1)`;
4. the stated convergence of power sums for every fixed exponent greater than one.

The argument now explicitly supplies the ingredients missing from earlier provisional versions: reduced slab conditioning, hereditary residual matching structure, predictable adaptive exposure, a scale-sensitive orbit-balance estimate, a root-avoiding likelihood-ratio identity, exclusion of premature auxiliary termination, a joint-event deletion-stability lemma, a noncircular cutoff hierarchy, and residual-mass control for the `ell^1` upgrade.

### Promotion recommendation

The theorem may be treated as **mathematically established within the present manuscript dependency boundary**, subject to the localized clarifications in Section 9 below. Those repairs do not alter the theorem hypothesis, conclusion, topology, or proof strategy. They are needed for publication-level transparency and eventual formalization, not to replace a missing argument.

### Scope boundary

This verdict does **not** assert:

- a quantitative rate of convergence to `PD(1)` or `GEM(1)`;
- a quenched theorem uniform over arbitrary deletion histories;
- endpoint-singular macroscopic universality without the fixed rate-ratio bound;
- mesoscopic cycle laws, total-cycle laws, or any result imported from another manuscript;
- formal verification or independent human refereeing.

The proof is subsequential and qualitative: for each comparable-rate triangular array, an arbitrary subsequence is refined to a marked-profile limit, the universal limit is identified, and the subsequence principle returns full convergence.

## 2. Verdict table

| Result | Verdict | Comments |
| --- | --- | --- |
| Theorem `thm:macroscopic-pd` | **Pass** | Both `GEM(1)` and ranked `PD(1)` limits, including the stated `ell^1` topologies, follow from the audited chain. |
| Lemma `lem:pd-kernel-contraction` | **Pass** | The common-component decomposition gives the claimed `L^2_0` contraction; the compression argument is sound. |
| Lemma `lem:pd-slab-law` | **Pass** | Fixed-partition empirical convergence, finite-state spectral transfer, inner-column control, Hilbert--Schmidt control, and aggregated tail control are valid. |
| Lemma `lem:pd-residual-factorization` | **Pass** | Conditioning on predictable exposed edges leaves independent permanental laws on the residual row submatrices. |
| Lemma `lem:pd-hereditary-flatness` | **Pass** | The permanent-minor bijection gives the required pairwise marginal ratio, stable under arbitrary partial matching. |
| Lemma `lem:pd-predictable-exposure` | **Pass** | The filtration condition is exactly what prevents adaptive source selection from revealing additional residual-matching information. |
| Lemma `lem:pd-relative-prefix` | **Pass with clarification** | The stopped logarithmic martingale argument is correct; the post-stopping two-case argument should be written out explicitly. |
| Lemma `lem:pd-two-scale-balance` | **Pass** | The rowwise prefix law, deterministic flow identity, tail-row Hilbert--Schmidt bound, and resolvent estimate fit together correctly. |
| Lemma `lem:pd-root-avoiding` | **Pass** | The sequential Radon--Nikodym product is exact, and only the root can be the first repeated target. |
| Lemma `lem:pd-harmonic-product` | **Pass** | The uniform harmonic expansion is valid in the stated interior range. |
| Proposition `prop:pd-uniform-residual-fraction` | **Pass** | The closure row is sampled with the correct residual mass; scale-sensitive balance excludes premature termination and yields an asymptotically uniform residual fraction. |
| Lemma `lem:pd-deletion-stability` | **Pass** | The simultaneous-prefix event may be evaluated at the random closing time; the result is correctly stated as a joint-event estimate rather than conditioning on the exact length. |
| Lemma `lem:pd-cdf-test` | **Pass** | Standard conditional integration by parts; endpoint control is correct. |
| Proposition `prop:pd-residual-uniforms` | **Pass with clarification** | The cutoff hierarchy is noncircular and the conditional induction is valid; a stage-by-stage parameter table would make this substantially easier to audit. |
| `ell^1` upgrade in the proof of the main theorem | **Pass with clarification** | Finite-dimensional convergence plus expected residual mass gives bounded-Lipschitz convergence in `ell^1`; the truncation inequality should be displayed explicitly. |
| Corollary `cor:pd-power-sums` | **Pass with wording correction** | The functional is bounded and continuous. “Bounded convergence” should be replaced by convergence of expectations for bounded continuous test functions under weak convergence. |

## 3. Conditioning and residual matching structure

### 3.1 The slab sigma-field is not overinformative

The manuscript conditions on:

- the label sets `H_{n,a}` belonging to each clock slab;
- the rank intervals `Q_{n,a}`, which are determined by the slab sizes;
- the **unlabeled ordered clock values** inside each slab.

It does **not** condition on which label receives which ordered time. Therefore the residual permutation is not determined. Given these data, assigning labels in `H_{n,a}` to ordered positions in `Q_{n,a}` has density proportional to

$$
\prod_{i\in H_{n,a}} e^{-\theta_{n,i}s_{a,\phi(i)}},
$$

because the factors `theta_{n,i}` are independent of the assignment and cancel from the conditional normalization. The normalizing sum is the permanent. Different slabs factor because the original exponential density is a product and the slab assignment partitions the labels.

This is the correct reduced conditioning. It avoids the earlier defect in which the conditioning sigma-field included enough information to determine the whole ranking.

### 3.2 Residual factorization survives adaptive exposure

Once a compatible collection of edges is fixed, deleting its source rows and target columns leaves the same product-of-edges density on each residual submatrix, with permanent normalization. Thus `lem:pd-residual-factorization` is exact.

The predictable-exposure condition is essential and is used correctly. Before the next edge is exposed, its source is measurable with respect to the current filtration. The fact that this source may have been chosen adaptively from all previous edges causes no extra conditioning on the unexposed submatrix. Consequently the next target has the residual one-edge marginal.

The root-avoiding exploration also fits this framework. Conditioning the current target not to be the distinguished root merely renormalizes the remaining one-edge marginal. After a non-root target is selected, conditioning on that edge again leaves a residual permanental matching.

### 3.3 Tail rows are never assigned false flatness

The proof uses one fixed finite partition of `[0,T]` and aggregates all clocks after `T` into one tail row. Hereditary flatness is invoked only in finite-width rows below a chosen cutoff. Tail rows are handled by deterministic occupancy bounds and the block Hilbert--Schmidt estimate. Thus the proof does not require positive lower cell sizes or a quenched flatness estimate in arbitrarily late clock slabs.

This point is decisive: the finite-state spectral gap belongs to the deterministic compressed kernel `P_n`, while the discrepancy between actual exploration and `P_n` in the aggregated tail is charged as a small-mass error.

## 4. Adaptive relative-prefix control

### 4.1 Rowwise martingale argument

For one row, let `N_r` be the number of remaining targets in one category and `s_r` the total number of remaining targets. Hereditary flatness gives

$$
\mathbb E(Y_{r+1}\mid\mathscr F_r)
\in
\left[e^{-\beta}\frac{N_r}{s_r},
      e^{\beta}\frac{N_r}{s_r}\right].
$$

The stopped process `log(N_r/s_r)` then has:

- drift of order `beta/s_r + 1/s_r^2 + 1/(s_rN_r)`;
- conditional variance of order `1/(s_rN_r)`.

Stopping when either remaining count falls below `m_b^{2/3}` yields total quadratic variation `o(1)`. Doob's `L^2` maximal inequality gives simultaneous control of every prefix. The accumulated `beta/s_r` drift produces a power `u^{1+O(beta)}`, and the elementary bound

$$
\sup_{0\le u\le1}|u^{1+a}-u|=O(|a|)
$$

removes the apparent logarithmic loss.

### 4.2 Post-stopping regime

The proof's conclusion after the stopping time is correct, but compressed. There are two cases:

1. If `s_tau < m_b^{2/3}`, then `s_tau/m=o(1)`, and the upper power bound forces `N_tau/m_b=o(1)`.
2. If `N_tau < m_b^{2/3}`, then `N_tau/m_b=o(1)`, and the lower power bound forces `s_tau/m=o(1)`.

In either case both normalized remaining counts are small at `tau`; both are nonincreasing afterward, so their difference stays small. This is the missing explicit sentence needed to make the stopping argument transparent.

### 4.3 Uniformity over adaptive histories

The rowwise estimate is not claimed on one event simultaneously for all counterfactual histories. Instead, for each regular history and each predictable exploration rule, the conditional failure probability is bounded by the same deterministic `pi_n`. This is the correct uniformity notion and is exactly what the regeneration induction later uses.

## 5. Two-scale orbit balance and rooted closure

### 5.1 Deterministic flow and resolvent

The row-prefix estimate controls the discrepancy

$$
E_{ab}=R_{ab}-R_aP_{ab}
$$

for rows below the outer cutoff. Outer rows are controlled only by injectivity and their small total mass. The deterministic orbit-flow identity gives

$$
q-qP=e,
$$

where `q_a=R_a/ell`. Writing `u=q/p-1` gives

$$
u-P^*u=e/p.
$$

The finite-state spectral gap therefore controls the global `L^2(p)` deviation. The inner-column bound then converts this global estimate into a pointwise estimate for a selected inner state. This is the required bridge from averaged orbit balance to the dependently selected closure row.

The tail-row calculation is also correct. Weighted Cauchy--Schwarz gives

$$
\sum_b \frac{H_b^2}{m_{n,b}}
\le Cm_{n,D(U)},
$$

using the block Hilbert--Schmidt estimate. Since `m_{n,D(U)}/n` is `O(e^{-U}+epsilon_n^2)`, its contribution is of order

$$
\frac n\ell(e^{-U/2}+\epsilon_n).
$$

### 5.2 Root-avoiding likelihood ratio

At each opportunity to close at the root, the original transition law is an atom at the root plus the conditional avoid-root law. Multiplying the sequential factors `1-lambda_j` gives the exact survival probability under the auxiliary law.

No non-root visited vertex can be the first repeat: its target column was already consumed by the edge that first entered it. Hence the only possible first repeat is the root. If the closure row initially contains `m` targets and `j` non-root targets have already been consumed, exactly `m-j` targets remain in that row, so hereditary flatness gives the stated hazard interval.

Exact finite checks were also performed on arbitrary positive rational permanental laws for sizes up to five. Across 540 matrix/length instances, the original survival probability and the root-avoiding Radon--Nikodym expression agreed exactly. These checks support the indexing and change-of-measure formula but are not part of the proof.

### 5.3 Premature termination is genuinely excluded

The auxiliary path can be forced to stop if only the forbidden root remains in the closure row. The scale-sensitive factor `n/ell` is indispensable here.

If forced termination occurs after `r` completed edges, then the path has used `m-1` closure-row targets. Applying the orbit-balance estimate at this random prefix and multiplying by `r/N` gives

$$
\left|\frac{m-1}{Np_C}-\frac rN\right|
\le C\Delta_n+O(n^{-1}).
$$

Regularity gives `m/(Np_C)=1+O(delta)`, so `r/N` must be close to one. Therefore the auxiliary exploration cannot terminate before `(1-zeta)N` edges when the deterministic error is small. This closes the central scale-sensitive gap present in earlier versions.

### 5.4 Uniform residual fraction

For `k=floor(xN)`, the number of closure opportunities is the number of visits to the closure source row. Two-scale balance gives `S(k)/m=x+o(1)` uniformly for `x` in a compact subinterval of `(0,1)`. The hazard product is squeezed between two harmonic products with exponents `e^{plus/minus beta}`. The harmonic-product lemma and `beta -> 0` then give

$$
\mathbb P(L/N\le x\mid\mathcal H)=x+o(1)
$$

uniformly over regular histories and interior `x`.

The selected closure row is not assumed deterministic. A uniform residual root lands in closure row `a` with probability `m_a^R/N`, and complete-cycle deletion gives the identity `|Q_{n,a} intersect R|=m_a^R`. The probability that the selected closure row lies beyond the inner cutoff is bounded by the aggregated tail mass.

## 6. Deletion stability and regeneration

The deletion lemma is stated in the correct joint-event form:

$$
\mathbb P(\text{interior cycle and bad post-deletion history}\mid\mathcal H)
\le\pi_n.
$$

It does not condition on the exact value of the random cycle length.

The simultaneous-prefix event from the orbit-balance lemma may be evaluated at the random closing time. On an interior macroscopic cycle, the closing time is at least a fixed positive fraction of `n`, so scale-sensitive balance gives the correct fraction of removed vertices in every inner row. The row-prefix estimate gives the corresponding fraction in every inner row/category cell. Because a directed edge from source row `a` to target category `b` removes exactly one target from `Q_{n,a} intersect H_{n,b}`, these are exactly the counts needed for the next residual matrix.

If `x=L/N`, then

$$
m_a^{R'}=(1-x)m_a^R+O(\Delta m_a^R),
\qquad
N_{ab}^{R'}=(1-x)N_{ab}^R+O(\Delta N_{ab}^R).
$$

The interior upper bound `x<=1-zeta` keeps the denominator away from zero. Division by the new residual fraction therefore preserves regularity at the smaller cutoff. Residual permanental factorization survives because the newly exposed cycle consists only of fixed matching edges.

This is enough for regeneration. No assertion is made for arbitrary histories; the induction remains inside the explicitly defined class of regular histories.

## 7. GEM induction

### 7.1 Noncircular parameter order

For a fixed number of deletions `k` and endpoint truncation `zeta`, the proof chooses:

1. an innermost cutoff `T_0` large enough to control the root-row tail;
2. successively larger outer cutoffs `T_1,...,T_k`, each chosen after the constants at the previous inner level are fixed;
3. one finite master partition containing all cutoffs;
4. a sufficiently small mesh, after every cutoff-dependent coefficient is known;
5. finally `n` sufficiently large for the fixed partition.

This order prevents constants depending on the inner cutoff or the mesh from entering a circular choice.

At stage `r`, the current history is regular at outer cutoff `T_{k-r+1}`. The root law uses inner cutoff `T_{k-r}`; after an interior deletion, the next history is regular at exactly that inner cutoff. The residual size remains at least `zeta^{r-1}n` on the interior event.

### 7.2 Conditional-to-joint passage

The conditional CDF estimate is converted to conditional expectations of test functions supported away from the endpoints. The joint-event deletion lemma permits insertion of the next regular-history indicator without conditioning on the exact residual fraction. Iterating conditional expectations gives factorization of products of test functions.

Endpoint mass is then controlled by evaluating the conditional CDF bound at `2zeta` and `1-2zeta`. Letting first `n` tend to infinity, then the target error tend to zero, and finally `zeta` tend to zero yields convergence against products of bounded Lipschitz functions. Such products form a convergence-determining class on the compact cube `[0,1]^k`.

The convention that later residual fractions are zero after exhaustion is harmless, since exhaustion before stage `k` forces one of the first `k` fractions into the endpoint event.

### 7.3 Clarification recommended

The hierarchy is correct, but the notation `R_j`, `D_j`, `A_j`, and the forward deletion recursion is difficult to verify on first reading. A small table listing, for each stage, the current regularity cutoff, the root-law inner/outer cutoffs, and the next cutoff would materially improve auditability without changing the proof.

## 8. Residual mass and the `ell^1` passage

Set

$$
X_{n,j}=V_{n,j}\prod_{i<j}(1-V_{n,i}),
\qquad
R_{n,k}=\prod_{i=1}^k(1-V_{n,i}).
$$

Finite-dimensional convergence of the residual fractions gives convergence of `(X_{n,1},...,X_{n,k},R_{n,k})`. Since `R_{n,k}` is bounded,

$$
\mathbb E R_{n,k}\longrightarrow 2^{-k}.
$$

For a bounded Lipschitz functional `F` on `ell^1`, let `x^{(k)}` denote truncation after `k` coordinates. Then

$$
|F(x)-F(x^{(k)})|
\le \mathrm{Lip}(F)\sum_{j>k}x_j.
$$

For the finite permutation sequence, the right side is `Lip(F) R_{n,k}`; for the limiting GEM sequence it is `Lip(F) R_k`. Thus

$$
|\mathbb EF(X_n)-\mathbb EF(X)|
\le \mathrm{Lip}(F)(\mathbb ER_{n,k}+\mathbb ER_k)
+|\mathbb EF(X_n^{(k)})-\mathbb EF(X^{(k)})|.
$$

For fixed `k`, the final term tends to zero; then `k` tends to infinity. This proves weak convergence in `ell^1`. The manuscript's shorter argument is valid, but displaying this inequality would make the topological step fully explicit.

For nonnegative `ell^1` sequences, decreasing rearrangement is a contraction in `ell^1`; the manuscript sketches the standard finite uncrossing proof and passes to truncations. Therefore the continuous mapping theorem gives the ranked `PD(1)` conclusion.

The subsequence argument is also sound. Every original subsequence has a further subsequence on which the marked empirical measures converge. The limiting cycle law is independent of the marked-profile limit, so every subsequence has a further subsequence with the same universal law.

## 9. Necessary localized repairs

The following repairs should be applied before changing the manuscript status from “mechanical extraction—audit pending” to an audited active paper. None requires changing a principal statement.

### R1. Make the reduced slab conditioning derivation explicit

Immediately before the permanental-row formula, add a short proof that the joint exponential density conditioned on slab memberships and unlabeled within-slab order statistics is proportional to the displayed product, and that row assignments factor. Explicitly say that the label-to-order assignments are **not** included in the conditioning sigma-field.

Reason: this is elementary, but it is the exact point at which an earlier proof version became overconditioned. It should not be left as an unsupported displayed formula.

### R2. Expand the post-stopping part of the relative-prefix proof

Replace the sentence after the stopping time by the two cases in Section 4.2 of this audit. Also choose the smallness constant so that, in later harmonic-product applications, `beta_0 <= log 2`; then `e^{plus/minus beta}` lies in `[1/2,2]`.

Reason: the argument is correct, but the present sentence “both normalized remaining counts are nonincreasing” is not by itself enough; the proof also uses that both are already small at the stopping time.

### R3. Add an explicit stage table or recursion lemma for the GEM hierarchy

Record the stage mapping

| Stage | Current history regular at | Root-law inner cutoff | Root-law outer cutoff | Post-deletion regular at |
| --- | --- | --- | --- | --- |
| `r` | `T_{k-r+1}` | `T_{k-r}` | `T_{k-r+1}` | `T_{k-r}` |

and state once how the deterministic regularity errors propagate.

Reason: the hierarchy is noncircular, but its indexing is currently harder to audit than the underlying argument.

### R4. Expand the `ell^1` truncation step and clarify root selection

Display the bounded-Lipschitz truncation inequality from Section 8. In the theorem statement, say that at each deletion stage the new root is sampled independently and uniformly from the current residual set.

Reason: these are the precise ingredients behind the size-biased ordering and the topology upgrade.

### R5. Correct the power-sum expectation wording

Replace “bounded convergence transfers the expectation limit” by “weak convergence and bounded continuity of the power-sum functional transfer the expectation limit.”

### R6. Add precise references for the genuinely imported standard facts

The manuscript already identifies its external inputs. The bibliography should include a standard source for compactness/disintegration and the maximal inequalities, or the text should state that these are textbook inputs. Pitman, Chapter 3, is the correct source for the `GEM(1)`/`PD(1)` size-biased-order relation; the author's Berkeley technical-report version is publicly available at `https://www.stat.berkeley.edu/~pitman/621.pdf`.

## 10. Import trace

No theorem from another active manuscript is imported. The model-specific dependency chain is entirely internal to the extracted paper.

| Standalone result | Frozen source | Depends on |
| --- | --- | --- |
| `lem:pd-kernel-contraction` | archived Lemma 6.2, line 2296 | compactness/disintegration; elementary conditional-expectation contraction |
| `lem:pd-slab-law` | archived Lemma 6.3, line 2404 | marked empirical convergence along the chosen subsequence; Kolmogorov maximal inequality; `lem:pd-kernel-contraction` |
| permanental-row formula | archived display at line 2523 | conditional density of independent exponentials given unlabeled order statistics |
| `lem:pd-residual-factorization` | archived Lemma 6.4, line 2529 | permanental-row formula |
| `lem:pd-hereditary-flatness` | archived Lemma 6.5, line 2545 | permanent-minor term bijection |
| `lem:pd-predictable-exposure` | archived Lemma 6.6, line 2586 | residual factorization; hereditary flatness |
| `lem:pd-relative-prefix` | archived Lemma 6.7, line 2626 | Doob `L^2` maximal inequality; elementary Taylor estimates |
| `lem:pd-two-scale-balance` | archived Lemma 6.8, line 2821 | predictable exposure; relative-prefix law; slab spectral/tail estimates; deterministic flow identity |
| `lem:pd-root-avoiding` | archived Lemma 6.9, line 2995 | predictable exposure; sequential change of measure |
| `lem:pd-harmonic-product` | archived Lemma 6.10, line 3033 | harmonic-sum expansion |
| `prop:pd-uniform-residual-fraction` | archived Proposition 6.11, line 3060 | two-scale balance; root-avoiding identity; harmonic product |
| `lem:pd-deletion-stability` | archived Lemma 6.12, line 3190 | simultaneous-prefix form of two-scale balance; residual factorization |
| `lem:pd-cdf-test` | archived Lemma 6.13, line 3293 | conditional Stieltjes integration by parts |
| `prop:pd-residual-uniforms` | archived Proposition 6.14, line 3330 | uniform residual-fraction law; deletion stability; CDF test |
| `thm:macroscopic-pd` | archived Theorem 6.1, line 2221; proof near line 3485 | finite-dimensional residual uniforms; continuous mapping; residual-mass truncation; rearrangement contraction |
| `cor:pd-power-sums` | archived Corollary 6.15, line 3535 | main theorem; standard `GEM(1)`/`PD(1)` size-biased-order relation from Pitman |

### External standard facts

| Input | Where used | Source status |
| --- | --- | --- |
| sequential compactness of probability measures on a compact metric space | extraction of the marked-profile limit | standard Prokhorov compactness |
| disintegration on compact standard Borel spaces | definition of `eta_x` | standard regular conditional probability/disintegration theorem |
| Kolmogorov maximal inequality | uniform centered partial sums in the slab law | standard textbook inequality |
| Doob `L^2` maximal inequality | relative-prefix martingale | standard textbook inequality |
| continuous mapping theorem | finite GEM coordinates and decreasing rearrangement | standard weak-convergence theorem |
| bounded-Lipschitz convergence criterion | `ell^1` upgrade | standard metric-space weak convergence |
| `GEM(1)` as the size-biased order of `PD(1)` | naming the ranked law and the power-sum expectation | Pitman, *Combinatorial Stochastic Processes*, Chapter 3 |

## 11. Final theorem-by-theorem verdict

### Theorem `thm:macroscopic-pd`

**Verdict: proved.** The hypothesis, both topology statements, and the uniform-root conclusion are supported. No weakening or strengthening is required.

### Proposition `prop:pd-uniform-residual-fraction`

**Verdict: proved.** The dependently selected closure row is handled correctly, including the tail event and premature auxiliary termination.

### Lemma `lem:pd-deletion-stability`

**Verdict: proved.** The joint-event formulation is sufficient for regeneration and avoids illicit conditioning on an exact random cycle length.

### Proposition `prop:pd-residual-uniforms`

**Verdict: proved.** The parameter hierarchy is logically noncircular and the conditional induction yields independent uniforms for every fixed dimension.

### `ell^1` GEM and PD conclusions

**Verdict: proved.** Expected residual mass gives the needed tail tightness; decreasing rearrangement is continuous in `ell^1`.

### Corollary `cor:pd-power-sums`

**Verdict: proved.** Only the final description of the expectation-transfer theorem should be corrected.

## 12. Audit boundary

The audit was adversarial with respect to the previously identified failure modes: overconditioning, false late-slab flatness, adaptive-history quantifiers, averaged rather than rooted balance, premature root-avoiding termination, deletion conditioned on the exact length, circular cutoff selection, and finite-dimensional convergence without residual-mass control. The current proof contains an explicit valid mechanism for each point.

The finite checks mentioned above test only algebraic components of the proof. They do not substitute for the analytic argument. This report is not a claim of formal verification or external peer review.
