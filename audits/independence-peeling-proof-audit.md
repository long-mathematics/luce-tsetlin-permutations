# Targeted proof audit: microscopic–macroscopic independence and Poisson peeling

Audited manuscript: `papers/independence-peeling/luce_independence_peeling.tex`.
Companion sources checked at revision `38f195dc5b30812ebbf084764016e857a68b9a1c`.
Review date: 20 October 2026.

## Assessment and verification boundary

The targeted audit found no unresolved internal gap in the revised argument relative to the named companion interfaces. The paper remains **internally audited current research**: this is not formal verification, independent human refereeing, or a new end-to-end audit of all companion proofs. The main theorem is joint short-cycle/macroscopic-partition independence under a positive continuous profile. The quantitative peeling results have the broader comparable-rate hypothesis. The independent PD cutoff result is placed in Appendix A.

## Conditional macroscopic inputs

The relevant premises are not merely unconditional PD/GEM convergence. The source's `lem:pd-residual-factorization` permits compatible exposed matching edges and proves independent permanental residual minors. Its `prop:pd-uniform-residual-fraction`, equation `eq:pd-root-cdf`, is uniform over regular residual histories with a fixed positive residual fraction. Its `lem:pd-deletion-stability`, equations `eq:pd-deletion-error` and `eq:pd-deletion-joint`, is a joint-event bound for an interior deletion and irregular post-history; it does not condition on an exact random cycle length.

The revised input statement displays both quantitative bounds. The unconditional statement of `prop:pd-residual-uniforms` is not cited as if it were a conditional theorem. Instead, the draft derives the needed uniform finite-dimensional induction, using the conditional modules and the cutoff order supplied by its proof.

## Finite prescribed-cycle deletion

For every complete prescribed cycle and clock row, the numbers of its vertices in the source block and target-rank block agree. Removing at most a fixed number of vertices therefore preserves square residual rows and changes each row and cell population by at most that fixed number. On good slab data, the relative initial error is bounded by a partition-dependent constant times that number divided by n.

The revision makes the subsequent error recursion explicit in `eq:finite-deletion-recursion`. Its initial value is the bounded-deletion error rather than zero. At each of a fixed number of stages the added perturbation is multiplied only by previously fixed constants, so it still tends to zero uniformly over compatible prescribed cycles. Inner cutoffs are chosen before the corresponding outer cutoffs; the mesh and n are chosen afterward. The conditional root-CDF and joint-event deletion bounds then give product-uniform residual fractions, including control of the omitted endpoint events. The expected leftover mass is bounded by the uniform residual product plus a chosen small error.

The final ranked-partition comparison uses the contraction of decreasing rearrangement and a restoration/renormalization error at most twice the deleted fraction. The factorial-moment weighted passage uses bounded second moments from the microscopic fixed-order moment theorem and Cauchy–Schwarz on bad slab data. It does not assume uniform control of a bad slab event conditional on a rare prescribed cycle.

## Joint annular switching

For cutoffs b' < b < U < U', a lower-annulus split at distance r uses the sufficient exceptional length set `(r,r+b]` union `(U,U+r]` union `(U',U'+r]`. The last interval is required because the upper-annulus count and final remainder are retained separately. The admissible witness b'=2, b=5, U=12, U'=20, r=3, source length 22 crosses the last boundary without crossing the first two.

The set has at most b+2r, hence at most 3b, integer lengths and lies below n/2. For an upper-annulus split the sufficient exceptional set `(r,r+U']` has at most U' lengths and also lies below n/2. Selected-factor Holder control applies to these sets. The passive-mark Stein comparison preserves the mark's original marginal; tensoring its two applications yields the stated vector approximation. All finite checks of these sufficient conditions passed.

The iteration uses independent comparison copies and contraction under convolution. It does not assert simultaneous independence of all original annular counts. Moment transfer explicitly requires a fixed higher-moment bound, and no total-variation estimate is applied directly to an unbounded test. Constants are uniform in the logarithmic stage index with the order fixed. The finite-n error is retained until it is absorbed uniformly over the stage range.

## Endpoint and fixed-order interfaces

The finite endpoint statement uses the bracket in `eq:free-depth-global-bound` and `cor:quantitative-truncation-interface` of the mesoscopic source. The finite conditions leave intact residual row/cell margins; asymptotic smallness conditions are used to make the bracket vanish, not to derive it. The second fresh-pair observable is an expectation of a square in the shared clock environment, not the square of an expectation. Truncation optimization uses a selected moment above one, not an untruncated selected second moment.

The higher-moment branch cites the exact `cor:factorial-domination` in the sharp order source, following `thm:multiclock`, only for fixed tuple size and total prescribed length at most n/2. No arithmetic-order theorem or Edgeworth conclusion is an input. The scalar mod-Poisson paper is contextual only and its weaker mean-defect bound is not substituted for the absolute intensity error needed by peeling.

## Appendix A

The appendix derives the ordered PD factorial measure from the size-biased representation and uses a cutoff recurrence. The normalized derivative bound is integrable on every closed disk strictly inside radius one half, proving analytic convergence with an explicit cutoff error. The constant is identified by Theorem 1.1 of Caravenna–Sun–Zygouras, *The Dickman subordinator, renewal theorems, and disordered systems* (2019), DOI `10.1214/19-EJP353`. Its density formula was checked in the primary paper. Differentiation for cumulants follows only after taking logarithms on a smaller zero-free disk.

The error is for a threshold tending to zero in the limiting PD partition. It is not a rate in the finite Luce size and does not permit exchanging a moving short-cycle cutoff with the size limit.

## Reproducible checks

Run `python3 scripts/independence-peeling/check_consistency.py --output .build/verification/independence_peeling.json` or the registered `make verify` target. The suite checks 5,912 exact complete-cycle deletion cases through n=6, 637,137 length-splitting cases over 1,641 cutoff configurations, and the additional upper-boundary witness. It also checks the PD recurrence at real and complex parameters, the second factorial cumulant by independent quadrature, source labels, citation closure, and the appendix placement. These are finite/floating-point consistency checks, not asymptotic or certified numerical proofs.

Repository regression tests separately preserve the exact dependency set, distinguish contextual citations from premises, require the explicit conditional recursion, and check the principal theorem and appendix placement. Existing manuscript mathematics, archived sources, and audit reports are unchanged by this integration.
