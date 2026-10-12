# Adversarial proof audit: endpoint short cycles

Date: 12 October 2026.

Audited source:
`papers/endpoint-short-cycles/endpoint-short-cycles.tex` on
`migration/endpoint-short-cycles` at commit
`fe7d8e759cb9fd38a506e3f929c05abc1e1a5857`.

Frozen comparison source:
`archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`
at archived commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## Scope and review boundary

This report is the independent Stage B audit of the mechanical extraction.  It
checks the complete source-to-target endpoint local estimate, the global cycle
envelope, the continuum and discrete logarithmic traces, negligible-configuration
summation, the mixed factorial-moment theorem, the joint law of large numbers,
and all endpoint-regular and anisotropic local-limit inputs copied into the
standalone paper.

The audit branch changes only this report.  It does not edit the manuscript,
compiled PDF, extraction map, theorem-status register, catalog, dependency
map, build scripts, or frozen archive.  It is an internal adversarial review,
not formal verification, independent external refereeing, or novelty
certification.

## Executive verdict

**No fatal mathematical gap was found.**  The proof supports the endpoint
short-cycle theorem under exactly Definition `def:endpoint-rv`: the normalized
terminal rates are uniformly endpoint regularly varying with index
`gamma>0`, are uniformly bounded above and below in every macroscopic terminal
strip, and are nondecreasing on the full triangular array.

For every fixed `R` and fixed nonnegative integers `m_1,...,m_R`, the audited
argument proves

```math
E prod_{r=1}^R (C_r)_{m_r}
~ prod_{r=1}^R (alpha_{gamma,r} log n)^{m_r},
qquad
alpha_{gamma,r}=k_gamma^{*r}(0)/r.
```

It also proves, jointly for fixed `R`, convergence of the normalized fixed
cycle counts to `(1,...,1)` in probability and in every fixed `L^p`.

The proof is mathematically sound within this scope.  Six localized
clarifications are recommended before eventual promotion beyond “working
mechanical extraction; audit passed, repairs pending.”  None changes a
hypothesis, coefficient, quantifier, mode of convergence, or proof strategy.

## Frozen-source comparison

The extraction regression test compares six selected mathematical blocks
byte-for-byte with the frozen source.  The audit independently checked the
statement of every theorem-like environment against the provenance map.  No
hypothesis, rate, topology, quantifier, or limiting constant was lost or
expanded.

The active paper preserves:

- the exponential-race and Gumbel identities;
- the fixed-dimensional lattice LLT and tilted local upper bound;
- the full shared anisotropic Fourier/tilting toolkit;
- the entire endpoint-regular framework, including Definition
  `def:endpoint-rv`, weighted terminal sums, fixed-point universality,
  displacement and tangent laws, the multiplicative kernel, and the
  microscopic endpoint permutation;
- the complete endpoint short-cycle section, including all point-constraint,
  survival-envelope, trace, and factorial-moment arguments.

The extraction map records 47 theorem/proposition/lemma/corollary
environments, 167 labels, 117 internal reference targets, and two bibliography
keys, with no unresolved reference.  No active manuscript is a proof
dependency.

## Result-by-result verdicts

| Component | Verdict |
| --- | --- |
| Exponential/Gumbel and analytic inputs | Pass |
| Shared anisotropic Fourier and tilted-local-bound toolkit | Pass; inherited interface rechecked |
| Endpoint partial-sum lower bound | Pass |
| Weighted regularly varying terminal sums | Pass |
| Endpoint product envelope | Pass |
| Endpoint fixed-point universality package | Pass; source-identical to separately audited package |
| Endpoint displacement and tangent-measure laws | Pass; source-identical to separately audited package |
| Multiplicative semigroup and diagonal traces | Pass |
| Microscopic endpoint permutation | Pass |
| Source-to-target endpoint saddle geometry | Pass |
| Source-to-target anisotropic local CLT | Pass, with one checklist clarification recommended |
| Mixed noncompact localization | Pass, with one chain-comparison clarification recommended |
| Covariance stability on the point saddle scale | Pass |
| Integrated point-constraint saddle | Pass |
| Separated endpoint entry estimate | Pass |
| Scheduled-deletion survival | Pass, with adaptive-schedule induction to be stated more formally |
| Forced-deletion bound | Pass, with history-summation bookkeeping to be expanded |
| Endpoint survival tail | Pass |
| Capped path drop | Pass |
| Global cycle envelope | Pass |
| Continuum multiplicative trace | Pass |
| Discrete endpoint trace | Pass, with Riemann/tail estimates to be expanded |
| Negligible endpoint cycle configurations | Pass |
| Mixed factorial-moment theorem | Pass |
| Joint probability and fixed-`L^p` law of large numbers | Pass |

## Detailed audit

### 1. Endpoint regular variation and uniformity

The short-cycle argument uses the endpoint-regular framework exactly in the
range for which it was proved.  All source and target terminal coordinates in
the local estimate satisfy

```math
N <= p_j,q_j <= n/N,
```

with source-to-target ratios in a fixed compact multiplicative interval and
with target ratios separated by `exp(eta)`.  The final summation uses
`L_n=ceil(log n)` and `U_n=floor(n/(log n)^2)`, so these local uniformity
conditions hold after `N` tends to infinity.

The weighted-sum lemma is applicable after deletion of the fixed set of
specified sources.  Potter bounds and monotonicity control indices beyond the
uniform regular-variation window.  The endpoint partial-sum lower bound is
uniform over every possible alive set of a given cardinality and is therefore
strong enough for the later death-chain envelope.

**Verdict:** pass.  The promoted version should state in one place that all
uniformity is sequential in fixed `R,L,eta,M` and then `N -> infinity`; it is
not a quantitative assertion uniform over an unbounded family of endpoint
indices or cycle lengths.

### 2. Source-to-target saddle geometry

For the constraint `tau_n(p_j)=q_j`, the centered threshold is

```math
y_j(h_j)=log lambda_{n,q_j}+h_j,
```

and the specified centered Gumbel has density `varphi_{R_{n,j}}`, where
`R_{n,j}=lambda_{n,p_j}/lambda_{n,q_j}`.  Uniform regular variation gives
`R_{n,j}=(p_j/q_j)^gamma(1+o(1))` on the admissible family.

The mean cumulative lower-priority count satisfies

```math
M_j(h)=q_j A_gamma exp(h/gamma)(1+o(1)),
```

uniformly on compact `h`-sets after finitely many sources are deleted.  Hence
the exact equation `M_j(h_j^*)=q_j-j` has a unique solution,
`h_j^* -> -log K_gamma`, and derivative `d_{n,j}~q_j/gamma`.  The target
multiplicative separation, Potter lower bound, and common saddle limit give a
fixed positive gap between adjacent priority thresholds.  Thus the saddle
neighborhood lies strictly inside the required ordering chamber.

**Verdict:** pass.  The finite `j` correction in `q_j-j`, and the fact that it
is uniform because the number of constraints is fixed, should be mentioned
explicitly in a later clarification.

### 3. Anisotropic point-constraint LLT

The cumulative categorical vectors have adjacent support differences equal to
the coordinate vectors.  Disjoint multiplicative blocks around the separated
target scales `q_j` contain order `q_j` summands for which the two categories
adjacent to threshold `j` both have probability bounded below.  These blocks
survive deletion of the fixed source set and every bounded exponential tilt.
They imply the quadratic-form lower bound

```math
c D_q <= Sigma(h) <= C D_q.
```

The upper bound follows from the endpoint weighted-sum estimates and Cauchy--
Schwarz.  The same disjoint blocks give the anisotropic Fourier damping away
from the origin.  On the box `|u_j|=O(q_j^{-1/2})`, the third-cumulant error is
`O(q_1^{-1/2})`, hence uniformly negligible because `q_1>=N`.  Fourier
inversion yields the local Gaussian formula.  The tilted local upper bound
uses precisely the bounded-tilt covariance and projected-edge hypotheses of
the included anisotropic lemma.

**Verdict:** pass.  A later repair should display the assignment of a disjoint
edge block to each coordinate, including the first and last cumulative
categories, and explicitly note why bounded tilts preserve the lower atom
probabilities.

### 4. Mixed noncompact localization

The proof separates right offenders, left offenders, and locally regular
coordinates.  The single interval-coordinate tilt

```math
Theta=T alpha^- + T alpha^+ + lambda
```

is valid, and generalized Hölder separates its cumulant into three costs.  The
actual-mean cumulative Chernoff estimates give exponential penalties for both
offender classes.  The local interval tilt gives the quadratic/linear cost on
the regular coordinates.  Projected forward-edge concentration supplies every
available product-scale local factor; any omitted factor is absorbed by a
fixed exponential loss of order `q_j`.

The boundary-aware truncated-chain lemma is used with the correct orientation:
right `h`-offenders have large mean and negative cumulative residual, while
left offenders have small mean and positive residual.  The hypotheses
`|d_j|=O_L(q_j)` on the good set and `|H_j|<=q_j` on the left-offender set are
sufficient.  Monotonicity and the derivative lower bound convert residual cost
to distance from the saddle.  Finally the Gumbel density tails and the
superlinear offender penalties make the integrated noncompact contribution
`o(prod q_j^{-1})`.

**Verdict:** pass.  The later clarification should state the chain-lemma
substitution in a small table and show explicitly how one offender penalty
absorbs its missing `q_j^{-1/2}` local factor.

### 5. Covariance stability and integrated saddle

For `j<=k`, the covariance entry has the nested-event formula

```math
Sigma_{jk}(h)=sum_b p_{b,j}(h_j)(1-p_{b,k}(h_k)).
```

Endpoint weighted sums give derivative bounds of orders `q_j` and `q_k`.
Moving `h_j` on its `q_j^{-1/2}` scale therefore changes the normalized
covariance entry by `O(q_j^{-1/2}+q_k^{-1/2})`, uniformly tending to zero.
The normalized covariance matrices remain in a compact positive-definite set,
so determinant and inverse stability follow.

Taylor expansion of the mean on the saddle scale gives

```math
M(h)-z=D_n H_q u+o(D_q^{1/2}).
```

The local LLT and covariance stability identify the Gaussian integrand.  The
Jacobian and covariance determinant cancel exactly, leaving
`|det D_n|^{-1}`.  Compact Gaussian localization supplies domination, while
the preceding noncompact estimate removes the outer region.

**Verdict:** pass.  No hidden determinant or lattice factor is missing.

### 6. Separated endpoint entry estimate

Conditioning on the specified centered Gumbels gives an exact integral over
the priority-order chamber.  With sorted distinct targets, exactly `j-1`
specified priorities lie below the `j`-th threshold, so the residual count is
`q_j-j`; this matches the saddle target.  The integrated saddle then gives the
product of `varphi_{R_{n,j}}(h_j^*)/d_{n,j}`.  Using
`R_{n,j}~(p_j/q_j)^gamma` and `exp(-h_j^*) -> K_gamma` yields

```math
q_j^{-1} k_gamma(log(q_j/p_j))
```

for every factor.  The sign in the logarithm and all normalizing constants are
correct.

**Verdict:** pass.

### 7. Scheduled and forced deletion bounds

For an ordinary exponential race, `H_m(S,p)` satisfies the displayed first-
step recursion.  It is monotone under addition of competitors.  Induction on
the remaining schedule therefore handles arbitrary predictable forced
removals of competitors: a forced removal can only reduce the survival
probability, while an ordinary deletion is exactly averaged by the recursion.

For compatible point constraints, the conditional probability of deleting
source `p_i` at the prescribed level `q_i` is at most

```math
C lambda_{n,p_i}/(q_i lambda_{n,q_i}),
```

because every alive set of size `q_i` has total rate at least the sum of the
smallest `q_i` rates.  Pulling out these factors and summing the remaining
compatible transition weights gives total mass at most one.  If one edge is
distinguished, at most `L-1` other prescribed deletions occur before its level,
so at least `n-q_*-L` ordinary deletions must be survived.  The terminal-rank
identity converts this to the stated factor
`P(tau_n(p_*)<=q_*+L)`.

**Verdict:** pass.  A later repair should formulate the induction with an
explicit state `(S,m,schedule)` and show the compatible-history summation in
one displayed line; this would remove the most compressed conditioning step.

### 8. Endpoint survival tail and capped path drop

For `q<=U_n`, the proof chooses a lower block of size
`s=floor(m d^delta)`, with `m=q+L`, `d=(p wedge V_n)/m`, and
`delta=beta/(1+beta)`.  In the nontrivial range this block excludes `p` and
has size at least a fixed multiple of `m`.  Every block clock survives time
`1/lambda_{n,s}` with probability at least `e^{-1}`, so a binomial Chernoff
bound applies.  Potter's lower bound gives the same power `d^delta` in the
source-clock tail because `beta(1-delta)=delta`.  For `p>V_n`, monotonicity
reduces the comparison to `V_n`, which remains in the endpoint regime.

Following a directed cycle from the largest capped logarithm to the smallest,
the product of downward capped ratios is at least the total capped range.
Thus one downward edge realizes at least the geometric-average drop.  The
zero-oscillation case is also correct: distinctness plus the presence of a
vertex at or below `U_n` forces an entrance from above `U_n` into the vertex
`U_n`.

**Verdict:** pass.  The constants comparing `q+L` with `q` in the final
superexponential envelope should be made explicit in a later repair.

### 9. Cycle envelope

Multiplying the forced-deletion factors around a directed cycle cancels every
rate:

```math
prod_{a->b} lambda_{n,a}/(b lambda_{n,b})
=1/prod_{a in cycle} a.
```

This proves the basic harmonic envelope.  Choosing the capped-drop edge as the
distinguished constraint and using the survival tail gives a superexponential
penalty in the component's capped logarithmic oscillation.  Selecting the
component of maximal oscillation gives the collection-level envelope.

**Verdict:** pass.

### 10. Continuum and discrete logarithmic traces

After changing to cycle increments, the continuum trace has one free
translation coordinate.  Its available interval length is
`[T-R(z)]_+`, and the increment product integrates to
`k_gamma^{*r}(0)`.  Since `k_gamma` has an exponential right tail, a
superexponential left tail, and a finite first absolute moment, the range
correction is uniformly integrable and contributes `O_r(1)`.

The discrete trace is the corresponding Riemann sum in logarithmic cells.
On bounded oscillation sets, the kernel product and its first derivatives are
bounded; replacing harmonic weights by cell lengths costs `O(T_n/L_n)`.  A
local-supremum majorant with the same integrable tails controls the unbounded
oscillation uniformly.  Equality diagonals replace a harmonic factor by a
square, producing `O(1/L_n)` after the remaining relative sums are bounded by
the convolution majorant.  Letting the oscillation cutoff tend to infinity
gives

```math
k_gamma^{*r}(0) T_n+o(T_n).
```

**Verdict:** pass.  The construction of the local-supremum majorant and the
cell-error summation are correct but terse; both should be written out in a
few lines in a later clarification.

### 11. Negligible configurations

The harmonic-coordinate volume estimate assigns one logarithmic translation
to each component and bounded relative coordinates to the other vertices.
Combined with the superexponential cycle envelope, it gives a summable tail in
the maximum component oscillation.

For bounded oscillation, a close pair inside one component cuts out an
`O(eta)` band in relative-coordinate space.  A close pair in different
components links two translation coordinates and removes one free `T_n`
factor.  Low-endpoint components replace one `T_n` translation by
`O(log L_n+oscillation)`, which is negligible.  A wholly upper component has
harmonic mass `O((log log n)^r)=o(T_n)` for fixed length.  A crossing component
has no free `T_n` translation, while its finitely many upper vertices
contribute powers of `log log n`; the superexponential oscillation factor makes
the remaining sum finite.  These bounds cover fixed points separately where
no nontrivial-component oscillation exists.

**Verdict:** pass.  The later repair should separate the wholly upper, crossing,
and all-fixed-point subcases in a short summary table and state where fixed
`L` is essential.

### 12. Factorial-moment summation

Expanding the mixed falling factorial selects ordered collections of distinct
cycles.  Intersecting cycles are incompatible.  For a good collection, all
source-to-target ratios are bounded and all sorted targets are multiplicatively
separated, so the uniform entry estimate applies.  The accumulated relative
error is `o(T_n^m)` because the total leading kernel mass is `O(T_n^m)`.

For a directed `r`-cycle with a distinguished start, the discrete trace is
`k_gamma^{*r}(0)T_n+o(T_n)`; division by `r` removes cyclic rotations.  The
falling factorial already orders cycles of equal length, so no `m_r!` divisor
appears.  Removing equality constraints and cross-component close pairs costs
`O(T_n^{m-1})`; same-component close bands cost `O(eta T_n^m)`.  The global
envelope removes all remaining nongood collections.  Taking limits in the
order `n -> infinity`, `eta -> 0`, then `M -> infinity`, and using
`T_n~log n`, proves the displayed mixed factorial-moment asymptotic.

The constants `alpha_{gamma,r}` are finite and strictly positive because
`k_gamma` is a strictly positive probability density with the stated tails.
The first two factorial moments give normalized `L^2` convergence.  For fixed
`p`, a higher fixed integer factorial moment uniformly bounds an ordinary
moment of order greater than `p`, giving uniform integrability and hence
`L^p` convergence.  Finitely many coordinates give the joint vector
conclusion in any norm.

**Verdict:** pass.  A later repair should display the exact cycle-encoding
factor and state explicitly that the uniform ordinary-moment bound is asserted
for all sufficiently large `n`, which is all that the asymptotic argument
requires.

## External inputs

The extracted proof uses only two cited external sources.

1. **Petrov, _Sums of Independent Random Variables_ (1975), Chapter VII.**
   Used for standard Bernoulli concentration and local-limit background.  The
   fixed-dimensional and anisotropic LLT statements actually needed are proved
   in the manuscript.
2. **Bingham--Goldie--Teugels, _Regular Variation_ (1987), Theorems 1.2.1 and
   1.5.6.**  Used for the uniform convergence theorem and Potter bounds for
   slowly varying functions.

The remaining inputs—Chernoff's inequality, Fourier inversion, Hölder's
inequality, Gaussian integration, dominated convergence, and elementary
factorial/ordinary-moment identities—are standard and used in their usual
forms.  No theorem from another active repository paper is imported.

## Localized repairs recommended before promotion

1. **State the terminal-rank convention and chamber bookkeeping explicitly.**
   Record in one place why sorted targets force sorted priorities and why the
   residual cumulative target is exactly `q_j-j`; note that all finite
   corrections are uniform because the number of constraints is fixed.
2. **Add an anisotropic LLT and integrated-saddle checklist.**  Identify the
   disjoint edge block for each coordinate, the bounded-tilt persistence, the
   normalized covariance stability, and the determinant cancellation used by
   the point-constraint saddle.
3. **Expand the mixed-localization chain comparison.**  Give a small table
   matching right/left offenders to residual signs and chain-lemma sets, and
   state explicitly how offender penalties replace missing local factors.
4. **Formalize the scheduled/forced deletion bookkeeping.**  Write the
   induction state for adaptive forced schedules, the sum over compatible
   histories, the terminal-rank survival identity, and the harmless
   `q+L`-versus-`q` constant in the oscillation envelope.
5. **Expand the logarithmic trace approximation.**  Construct the integrable
   local-supremum majorant, show the `O(T_n/L_n)` cell error, and isolate the
   equality-diagonal estimate.
6. **Expose the final combinatorics and limit order.**  Display the division by
   cyclic rotations, absence of `m_r!`, the three boundary classes in the
   negligible-configuration lemma, positivity of `alpha_{gamma,r}`, and the
   fixed-higher-moment uniform-integrability step.

These are clarification and formalization repairs only.  They must not enlarge
the endpoint-regular class, permit growing cycle lengths, assert a Poisson
limit for the logarithmically diverging counts, add a convergence rate, or
change the fixed-`R`, fixed-`L^p` quantifiers.

## Final status recommendation

The endpoint short-cycle theorem package may be recorded as **audit passed; six
localized repairs pending**.  Under the user's requested workflow, the
manuscript itself remains unchanged and is not promoted beyond working
mechanical extraction in this prompt.
