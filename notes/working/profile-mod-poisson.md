# Profile mod-Poisson theorem: scope and remaining questions

The former conjecture in this note is **proved in the active, internally audited research manuscript** [*An Exact Uniform Component and Analytic Mod-Poisson Convergence for Luce Permutations*](../../papers/mod-poisson/luce_mod_poisson.tex) ([PDF](../../output/pdf/luce-mod-poisson.pdf)), subject to its explicit companion-paper inputs. This note is historical context and a register of extensions, **not** a proof input or an external refereeing certificate.

## Established statements and precise scope

For rate arrays sampled uniformly from a positive continuous profile, the manuscript proves, locally uniformly on a fixed complex neighborhood of $z=1$,

$$
n^{1-z}\mathbb E z^{K_n}
\longrightarrow \frac{e^{A_f(z-1)}}{\Gamma(z)},
\qquad A_f=\sum_{r\ge1}\left(\lambda_r(f)-\frac1r\right).
$$

It also proves the profile-dependent mean expansion $\mathbb E K_n=H_n+A_f+o(1)$ and the universal limits of all fixed higher factorial cumulants. For arbitrary comparable-rate triangular arrays, with **no** limiting profile required, it proves a uniform local complex bound and $\mathbb E K_n-H_n=O(1)$, but does not identify a limiting residue.

The earlier historical candidate for the mean-shift formula was invalidated; that obsolete proof is **not** reinstated. The present result has a different proof using real-fugacity switching, common-rate thinning, and marked residual cycles. The finite-order Edgeworth paper remains valid on its own narrower proof scope; it did not independently establish this profile-dependent analytic result.

## Open extensions

- Identify residues for broader marked, discontinuous, or singular profile classes, or for other well-controlled rate-array limits.
- Investigate convergence on larger complex domains; the current local theorem near $z=1$ does **not** assert full imaginary-axis mod-Poisson convergence.
- Determine higher-order asymptotic corrections and quantitative convergence rates under additional regularity.
- Extend Poisson–Dirichlet macroscopic universality to endpoint-singular arrays where uniform rate comparability fails.

For precise theorem hypotheses and the two imported asymptotic input interfaces, see the [manuscript](../../papers/mod-poisson/luce_mod_poisson.tex), [dependency map](../../DEPENDENCIES.md), and [internal audit](../../audits/mod-poisson-proof-audit.md).

Approximate deterministic centers must still respect lattice thresholds: replacing an exact mean inside a fractional-part function can change jump phases, even when the centering error is small.
