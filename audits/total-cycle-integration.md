# Total-cycle integration audit

Date: 11 October 2026. Scope: reconcile the uploaded scoped functional audit, Berry–Esseen note, and lattice Edgeworth note with the pinned repository sources. This is an AI-assisted mathematical integration review, not independent refereeing, novelty certification, or formal verification.

## Preservation boundary

Upstream commit: `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`. The first import preserved 22 files including all five source/PDF pairs. Integration keeps every existing frozen byte unchanged. The uploaded audit/proof-note text, sources, scripts, and original result JSON are separately preserved. Original conversation PDFs are fingerprinted but not duplicated in the source-note archive.

## Changes to existing mathematics

The switching paper gains a named truncation-uniform observable corollary. Its proof tracks the bounded norm and Lipschitz norm of exp(z) truncated at A: errors scale as A and A squared, uniformly even for growing A. The second comparison keeps shared-clock E[D squared]. This exposes the existing estimate used downstream; it is not an untruncated second-moment or arbitrary-deletion hypothesis.

The functional paper is promoted with its explicit total-cycle CLT, direct mean estimate, and exact-mean corollary. Its p parameter is tied to the rate ratio. The bounded Riemann-integrable test-function argument is justified by weak convergence of the harmonic measures. Tightness retains both covariance control and Lindeberg, not merely vanishing jumps. The abstract appendix now specifies t in [0,1] and cadlag paths. Obsolete future merge instructions and root-escape wording are replaced by current scoped dependencies. The scalar proof remains separate and unchanged.

The quantitative-order paper has only an interface wording clarification: the source theorem controls mean conditional TV relative to the coarse environment, not every arbitrary deletion history. The stopped-history comparisons remain internal to that proof. Its prime-power and nonlinear arithmetic arguments are not re-audited or imported by the new count theorem.

## New focused quantitative paper

The canonical source consolidates, rather than simply appends, both proof notes. It states the exact imported modules and proves the passive omitted-count construction, dimension-free Stein transfer, direct mean bookkeeping, fixed-order moment bounds, discrete Taylor/Charlier smoothing, and the signed expansions.

Checks during integration include the strict good-split inequality; both omitted cycle ranges as one passive mark; avoiding pair/fixed-order bounds outside total prescribed length <= n/2; deriving mean control separately from TV; using 2jth moments to transfer jth moments; matching mark means before Poisson smoothing; the negative sign of the variance-minus-mean CDF term; the midpoint correction y/24; the right-continuous phase +1/2 at integers; and the exact constant 2/(3 sqrt(2 pi)).

The Poisson mass remainder is controlled in l1 using Fourier inversion with two derivatives; the phase products at the two lattice interval endpoints cancel before integration by parts. Midpoint Euler–Maclaurin then gives a uniform CDF expansion. Fixed-order coefficient replacement is justified by the moment estimate and an accuracy exponent chosen after the order is fixed. No locally uniform analytic residue follows.

The expected-mean and factorial-cumulant limiting profile constants remain open. The macroscopic and singular-profile portions of the monolith retain their prior audit boundaries.

## Verification protocol

Three registered programs rerun the exact switch/residual identities, mean-matched Poisson smoothing, and lattice/Charlier formulas. Active programs write fresh results under `.build/verification/`; archived original results are not overwritten. Numerical agreement is a consistency check, not an asymptotic proof. All active PDFs must compile without undefined references/citations or overfull boxes and rebuild byte-for-byte in CI. New/changed pages are rendered for visual review. The final PR review records the actual completed checks and page counts at the tested head.

## Remaining decomposition

The 139-page draft is not split in this integration. The next mechanical PR should extract the PD/GEM theorem with all relevant preliminary lemmas, an old-label/new-label map, and an explicit list of retained external assumptions, followed by a separate mathematical audit. The regular-profile microscopic paper follows. Moving a theorem out of the archive alone does not improve its proof status.
