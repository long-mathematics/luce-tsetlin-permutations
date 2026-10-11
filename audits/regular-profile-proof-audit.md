# Adversarial proof audit: regular positive-profile cycles and sparse entries

Date: 11 October 2026.

Audited source:
`papers/regular-profile-cycles/regular-profile-cycles.tex` on
`migration/regular-profile-extraction` at commit
`f1287dd4b1598f260b2c98406dafddebcb579b9e`.

Frozen source used for scope comparison:
`archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`
at archived commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## Scope and review boundary

This audit reviews the complete standalone manuscript, with special attention
to the separated multipoint local estimate, endpoint and collision domination,
summability of the gap envelope, fixed-cycle factorial moments, improper trace
integrals, fixed-vector total variation, long-trace spectral theory, sparse
entry sets, deterministic overlaps, and the exact meaning of uniformity under
profile perturbations.

The review is adversarial but internal. It is not formal verification,
independent peer review, or novelty certification. The audit branch changes
only this report; it does not edit the manuscript, PDF, catalog, theorem-status
register, dependency map, or frozen archive.

## Executive verdict

**No fatal mathematical gap was found.** The proofs support the principal
results under the exact sampled-profile hypothesis

\[
 \theta_{n,i}=a_n\{f(i/n)+\varepsilon_{n,i}\},\qquad
 \max_i|\varepsilon_{n,i}|\longrightarrow0,
\]

where `f` is continuous and bounded above and below by positive constants.
The common factor `a_n` is immaterial after positive rescaling.

The following principal claims pass this audit:

1. the uniform separated bulk multipoint estimate;
2. endpoint and collision domination at every fixed order;
3. existence and finiteness of the improper fixed-point and cyclic trace
   integrals;
4. joint independent Poisson limits for every fixed cycle-count vector;
5. total-variation convergence for every fixed cycle-count vector;
6. exponential long-trace convergence to the uniform values `1/r`;
7. fixed-width diagonal-band Poisson laws;
8. sparse-entry and thin-graph Poisson laws;
9. overlap laws for deterministic permutations;
10. the transverse thin-curve corollary.

The proofs are mathematically sound within the stated scope. Before promotion
from a working extraction to an audited current manuscript, I recommend six
localized clarification repairs. None changes a principal hypothesis,
conclusion, limiting mean, mode of convergence, or proof strategy.

## Exact comparison with the archived source

The extraction regression test compares the three selected mathematical blocks
byte-for-byte with the frozen source. The audit independently checked every
principal statement against the provenance map. No theorem lost a hypothesis,
changed a limit, enlarged a uniformity class, or altered a mode of convergence.

| Result | Archived scope comparison | Audit verdict |
| --- | --- | --- |
| Gumbel threshold identities | Exact statement and proof retained | Pass |
| Point-probability and Bernstein bounds | Exact statement and proof retained | Pass |
| Uniform lattice LLT with tilted local bound | Exact statement and proof retained | Pass; clarify the uniform family bookkeeping |
| Regular-profile fixed points and short cycles | Exact sampled-profile hypothesis and fixed-`R` conclusion retained | Pass |
| Uniform saddle geometry | Exact fixed-order, separated-bulk scope retained | Pass |
| Uniform LLT for Luce cumulative counts | Exact compact-time and fixed-separation scope retained | Pass |
| Off-saddle exclusion | Exact fixed-order uniformity retained | Pass |
| Gaussian-scale saddle tail | Exact window and exponent restriction retained | Pass |
| Uniform integrated lattice saddle | Exact hypotheses and asymptotic retained | Pass; list the application checks explicitly |
| Separated bulk local estimate | Exact labels/positions and uniform error retained | Pass |
| One-point rank envelope | Exact bounded-rate scope retained | Pass |
| Gap envelope | Exact fixed-order conditional product bound retained | Pass |
| Gap-envelope summability | Exact `beta<alpha` conclusion retained | Pass; clean one off-by-one explanation |
| Endpoint domination | Exact order of limits and exponent retained | Pass |
| Bulk collision domination | Exact bulk and close-target scope retained | Pass |
| Endpoint tightness and improper integrability | Exact nonnegative improper limits retained | Pass |
| Fixed-point factorial moments | Exact fixed-`k` limit retained | Pass |
| Mixed short-cycle factorial moments | Exact fixed-vector limit retained | Pass; expand the combinatorial normalization |
| Fixed-vector total variation | Exact conclusion retained | Pass |
| Bistochastic Hilbert--Schmidt kernel | Exact kernel and bound retained | Pass |
| Cyclic trace formula | Exact `r>=2` trace statement retained | Pass |
| Long trace universality | Exact limiting-kernel statement retained | Pass |
| Fixed-width diagonal bands | Exact fixed-`h` Poisson law retained | Pass |
| Sparse bulk entry sets | Exact row-degree, no-crowding, and weak-measure hypotheses retained | Pass |
| General thin-graph law | Exact no-crowding and graph-measure hypotheses retained | Pass |
| Deterministic-permutation overlaps | Exact permuton hypothesis and improper mean retained | Pass |
| Transverse thin-curve law | Exact `C^1`, interior, nonvanishing-derivative scope retained | Pass |

The newly added abstract accurately summarizes the archived theorems. Its phrase
“exponential convergence of those means” refers to the limiting means
`lambda_r`, not to a uniform-in-`r` finite-`n` estimate.

## Imported results and their sources

No active manuscript in the repository is a proof dependency. All
model-specific estimates are internal to the standalone paper.

The external inputs are:

1. **Luce permuton density.** Borga--Chatterjee--Diaconis,
   *Permuton and local limits for the Luce model*, Proposition 2.2 and its
   explicit density formula. The current arXiv version retains the same
   density used here.
2. **Bernoulli concentration and local-limit background.** Petrov,
   *Sums of Independent Random Variables*, Chapter VII. The manuscript gives
   the Fourier proof of the concentration bound and proves the
   fixed-dimensional tilted LLT in the form actually used; Petrov is a source
   and comparison reference rather than an unproved model-specific lemma.
   Bernstein's inequality is used in its standard bounded-summand form.
3. **Trace ideals.** Simon, *Trace Ideals and Their Applications*, second
   edition: the Schatten ideal inequality, Weyl's eigenvalue inequality, and
   Lidskii's trace theorem are used in the long-trace section.
4. **Standard probability and functional analysis.** The multivariate method
   of moments, weak convergence on a countable discrete space, the
   converging-together lemma, compact-operator spectral theory, and equality
   in Jensen/Cauchy--Schwarz are used in standard forms. These are valid but
   should receive precise references in the promoted version.

## Detailed audit

### 1. Analytic input and the tilted lattice LLT

The general LLT is adequate for the later saddle calculation.

- Bounded increments give the uniform third-cumulant expansion
  `log Psi(u)=-u^T Sigma u/2+O(s|u|^3)`.
- The covariance lower bound gives Gaussian damping on the intermediate
  Fourier region.
- The stated tilted aperiodicity removes the remaining torus frequencies.
- The error is uniform in the lattice point because the oscillatory factor has
  modulus one and the Fourier errors are controlled in `L^1`.
- For displacements `o(s)`, uniform strong convexity produces the exponential
  tilt with mean equal to the desired lattice point. The tilted concentration
  bound then yields the Gaussian local upper estimate.

For cumulative exponential-clock counts, each increment has all adjacent
cumulative atoms with probability uniformly bounded below: the first interval,
all interior time intervals, and the terminal interval are uniformly nonempty
because times stay in a compact subset of `(0,infinity)` and are separated.
The adjacent support differences are the coordinate vectors. This gives both
uniform covariance nondegeneracy and strong aperiodicity, before and after all
bounded tilts.

**Verdict:** pass. The only recommended change is an explicit sentence that the
covariance functions and their first derivatives are uniformly continuous in
the time vector; this is immediate from bounded rates and is later used by the
integrated-saddle lemma.

### 2. Profile perturbations and saddle geometry

The perturbation hypothesis is used correctly. After rescaling by the positive
common factor `a_n`, the rates satisfy uniform positive upper and lower bounds.
For every fixed number of removed labels and every compact time interval,
Riemann summation plus `max_i|epsilon_{n,i}| -> 0` gives, uniformly,

\[
 A_{n,P}^{(j)}(t)\longrightarrow A^{(j)}(t)
\]

for the derivatives needed in the proof, and similarly for the covariance
entries. This yields compact saddle localization, uniform derivative lower
bounds, convergence of the saddle locations, and separation of saddle
coordinates whenever the target ranks are separated by a positive fraction of
`n`.

The theorem is uniform in the labels and separated target positions for a
fixed triangular array satisfying the displayed perturbation condition. It is
**not** a quantitative theorem uniform over all perturbation arrays with no
specified modulus of convergence; the manuscript does not claim such a
stronger statement.

**Verdict:** pass. This exact interpretation of uniformity should be stated in
one place, and the uniform derivative/Riemann-sum consequences should be
collected into a short lemma or paragraph.

### 3. Off-saddle control and integrated saddle evaluation

Outside a fixed compact saddle region, at least one cumulative count has mean a
linear distance from its target; Bernstein gives an exponentially small
contribution. Inside the compact region but outside the
`n^{-1/2+gamma}` saddle window, the derivative lower bound gives a mean
separation of order `n^{1/2+gamma}`, again yielding an exponentially small
bound.

Within the saddle window, Taylor expansion gives a mean displacement
`sqrt(n) D h+O(|h|^2)`. Since the diagonal derivative matrix is uniformly
nonsingular and `gamma<1/6`, the Gaussian local upper bound supplies an
integrable `exp(-c|h|^2)` majorant. The local Gaussian determinant cancels
against the Gaussian integral, leaving exactly `|det D|^{-1}`. Multiplication
by the specified-clock densities therefore gives the product of microscopic
kernel factors.

All hypotheses of the abstract integrated-saddle lemma hold in the application:

- uniform `C^2` bounds for `A_{n,P}`;
- diagonal derivatives bounded above and below;
- covariance matrices uniformly positive definite and uniformly continuous;
- the cumulative-count LLT;
- off-saddle exclusion and the Gaussian tail;
- bounded equicontinuous specified-clock densities.

**Verdict:** pass. The proposition currently says these hypotheses are
satisfied but does not enumerate the covariance-continuity and `C^2` checks;
they should be displayed in the repair PR.

### 4. Separated bulk local estimate

After sorting the target positions, the event is represented by cumulative
counts with exact targets `q_a-a`. The saddle solves the corresponding exact
finite-`n` mean equation. The ordered integration chamber contains a fixed
neighborhood of the separated saddle. The integrated saddle result yields

\[
 n^{-ell}\prod_a
 \frac{\theta_{n,p_a}e^{-\theta_{n,p_a}t_{n,a}^*}}
 {B_{n,P}(t_{n,a}^*)}+o(n^{-ell}),
\]

and uniform profile convergence identifies each ratio with
`rho(p_a/n,q_a/n)`.

There is no missing factor from the lattice covariance: it cancels in the
integrated Gaussian calculation. The sources need only be distinct; metric
separation is required only for target ranks. This is exactly what is needed
for cycles and sparse-entry applications.

**Verdict:** pass.

### 5. One-rank, gap, endpoint, and collision envelopes

The one-rank envelope correctly treats the two rank regimes.

- In the first half, the next-draw probability is `O(1/N)`.
- In the second half, survival from `N` to `s` labels is at most
  `C(s/N)^alpha`, followed by a next-draw factor `O(1/s)`.

Conditioning successively at specified target ranks is legitimate because the
unrevealed tail of a Plackett--Luce order is again a Plackett--Luce order on the
remaining labels. Iteration produces the product gap envelope.

The summability induction is correct for every `beta<alpha`. The terminal
part is summable with exponent `alpha`, the middle range loses an arbitrarily
small exponent to `beta`, and the bulk range contributes uniformly bounded
mass. Endpoint domination follows from a small first gap or small final
residual mass. Collision domination follows because a close pair creates a
small interior gap while the residual deck remains of order `n`.

**Verdict:** pass. The base case of the gap-sum induction uses
`r>N-h-1`; the phrase “with a harmless endpoint term” is correct but should be
expanded by one line to eliminate an avoidable off-by-one ambiguity.

### 6. Improper integrability

For fixed endpoint cutoff and collision scale, the separated local estimate
turns the finite sums into Riemann sums. Collision domination removes the
near-diagonal region, and bounded continuity of `rho` handles the same region
in the limiting integral. The gap envelope uniformly bounds the complete
finite-order sums, while endpoint domination makes the omitted endpoint mass
tend to zero. Since the integrands are nonnegative, the truncated integrals
increase as the endpoint cutoff is removed and remain uniformly bounded.

This proves existence and finiteness of the diagonal integral, every cyclic
trace integral, and the finite products appearing in mixed moments. For
`r>=2`, the later Hilbert--Schmidt trace argument independently confirms
finiteness of the full cyclic integral.

**Verdict:** pass. The order of limits `n -> infinity`, collision scale to
zero, endpoint cutoff to zero should be summarized explicitly once.

### 7. Fixed-point and mixed cycle factorial moments

For fixed points, source and target tuples coincide, so the endpoint and
collision envelopes apply directly. Uniform `o(n^{-k})` error over
`O(n^k)` separated configurations contributes `o(1)`, and the remaining
Riemann sum tends to the appropriate power of the diagonal integral.

For mixed cycles, expanding falling factorials gives ordered collections of
distinct cycles. Collections sharing a label are incompatible. Each disjoint
collection produces distinct sources and distinct targets; the target set is
the source set cyclically shifted inside each component. The only intrinsic
normalization for an `r`-cycle is the factor `1/r` for cyclic rotations, and
there is no additional `k_r!` because `(C_r)_{k_r}` orders the selected
cycles. Equality diagonals have `O(n^{L-1})` configurations and vanish after
multiplication by `n^{-L}`. The limiting integral factors over components.

The limiting mixed factorial moments are those of independent Poisson
variables. First moments give tightness, and the Poisson vector has finite
exponential moments, so the multivariate moment method applies.

**Verdict:** pass. The proof should display the exact factor
`prod_r r^{-k_r}` or state the encoding count explicitly; the current prose is
correct but compressed.

### 8. Fixed-vector total variation

Weak convergence on the countable discrete state space gives pointwise
convergence of all probability masses. The finite-set truncation argument is a
direct form of Scheffe's lemma and proves `l1`, hence total-variation,
convergence.

**Verdict:** pass. Add a citation to Scheffe's lemma or explicitly note that
finite subsets are continuity sets in the discrete topology.

### 9. Bistochasticity and long traces

The substitutions `y=A(t)` prove both marginal identities. Jensen then makes
`K` an `L^2` contraction. The Hilbert--Schmidt estimate

\[
 \|K\|_{HS}^2\le M_f\int_0^\infty B(2t)/B(t)\,dt
 \le M_f/m_f
\]

is correct. Approximation by nonnegative step kernels plus Schatten ideal
bounds gives the cyclic trace formula for every `r>=2`.

For a unit-modulus eigenvalue, equality in the `L^2` contraction forces
equality in Jensen for almost every row. Strict positivity of the kernel makes
each row measure equivalent to Lebesgue measure, so the eigenfunction is
constant and the eigenvalue is one. A generalized eigenvector would make
`K^n g` grow linearly, contradicting power boundedness, so the eigenvalue one
is algebraically simple. Compactness then places all remaining eigenvalues in
a disk of radius `q<1`. Lidskii and Weyl give

\[
 |\operatorname{Tr}(T^r)|
 \le q^{r-2}\sum_j|\zeta_j|^2
 \le q^{r-2}\|T\|_{HS}^2.
\]

This yields `r lambda_r=1+O(q^r)`. The first-factorial-moment result gives
`E C_r -> lambda_r` for each fixed `r`, justifying the iterated limit in the
theorem.

**Verdict:** pass. The complex-valued equality case in Jensen and the last
first-moment implication should be stated explicitly.

### 10. Fixed-width diagonal bands

The factorial expansion excludes identical summands; different edges sharing
a row or column are incompatible. Endpoint and close-target terms are
controlled uniformly. On separated bulk tuples, fixed offsets change the
second kernel coordinate by `O(1/n)`, so continuity gives the same diagonal
factor for every offset. Summing over the `2h+1` fixed offsets yields the
correct mean.

**Verdict:** pass.

### 11. Sparse-entry and thin-graph laws

The hypotheses are exactly those needed for the factorial-moment proof.

- `|E_n|=O(n)` fixes the natural Poisson scale.
- Maximum row degree `o(n)` makes repeated-row tuples negligible.
- The no-crowding condition makes close-target tuples negligible.
- Targets stay in a fixed bulk strip, where the gap envelope gives a uniform
  `O(n^{-k})` bound and `rho` is bounded continuous.

On good tuples the separated local estimate applies. Removing repeated edges,
repeated rows, and close target columns changes both the probabilistic sum and
the deterministic product sum by `o(1)`. Weak convergence of the finite graph
measures then identifies the intensity.

The general thin-graph corollary is an immediate specialization with row degree
one.

**Verdict:** pass. Repeated edges are already contained in the repeated-row
count, but the deterministic-sum paragraph should say this explicitly.

### 12. Deterministic overlaps and transverse curves

For a deterministic permutation graph, row and column degrees are one and a
window of width `2 eta n` contains at most `2 eta n+2` target columns. Weak
convergence of graph permutons passes to every fixed bulk strip because a
permuton's second marginal is Lebesgue and the strip boundary has zero mass.
The endpoint rank envelope makes the omitted overlap count negligible.
Applying the sparse theorem to endpoint annuli shows that the truncated
intensities form a Cauchy family, proving finiteness of the improper mean. The
standard converging-together lemma then gives the full Poisson limit.

A continuously differentiable function with derivative bounded away from zero
has constant derivative sign and is bi-Lipschitz on its image. This yields the
required no-crowding estimate for the transverse curve.

**Verdict:** pass. The overlap proof should cite a converging-together lemma and
state the order of the two limits explicitly.

## Required localized repairs before promotion

The following changes are recommended. They are clarifications, not theorem
repairs or strengthenings.

1. **Collect the profile-approximation consequences.** Add a short lemma or
   paragraph proving uniform compact convergence of `A_{n,P}`, `B_{n,P}`, the
   derivatives used in Taylor expansion, and the covariance kernels, uniformly
   over bounded-size removed sets. State that uniformity is for the fixed
   triangular array satisfying `max|epsilon| -> 0`, not over an unquantified
   class of arrays.
2. **Make the integrated-saddle checklist explicit.** In the proof of the
   separated local estimate, list the `C^2`, covariance-continuity,
   nonsingularity, LLT, off-saddle, and equicontinuity inputs rather than saying
   only that the abstract lemma applies.
3. **Expand two compressed summability points.** Write the one-line
   off-by-one treatment in the base case of the gap-envelope induction and
   summarize the exact order `n`, collision cutoff, endpoint cutoff used for
   improper integrability.
4. **Expose the cycle combinatorics.** State the exact
   `prod_r r^{-k_r}` cyclic-rotation factor and explicitly note why target
   tuples determine source tuples up to a fixed combinatorial encoding.
5. **Cite the standard convergence tools.** Add references for the
   multivariate factorial-moment criterion, Scheffe/discrete weak-to-total-
   variation implication, and the converging-together lemma.
6. **Clarify the spectral endpoint.** State the complex Jensen equality case,
   and explicitly derive `E C_r -> lambda_r` from the first mixed factorial
   moment before asserting the iterated long-trace limit. In the sparse-entry
   proof, mention repeated edges explicitly in the negligible deterministic
   product-sum comparison.

An optional bibliography update may replace the cited arXiv v2 entry for the
Borga--Chatterjee--Diaconis paper by the current version. The density formula
used in the proof is unchanged.

## Final status recommendation

The mathematical results may be promoted after the six localized
clarifications above are applied in a focused repair PR and checked against
this audit. No theorem should be weakened or strengthened. In particular, the
repair must not extend the results to arbitrary comparable arrays, growing
cycle lengths, quantitative total-variation rates, or endpoint-singular
profiles.
