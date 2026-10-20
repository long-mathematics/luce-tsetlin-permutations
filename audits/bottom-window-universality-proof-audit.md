# Proof audit: bottom-window universality for permuton-sampled Luce permutations

Review date: 20 October 2026.

Canonical manuscript: `papers/bottom-window-universality/bottom_window_luce.tex`.
Reviewed starting manuscript: the October 13, 2026 source supplied for this audit.
Catalog ID: `bottom-window-universality`; status: `current-research`; active-paper dependencies: none.

## Assessment and review boundary

The internal audit found no fatal gap in the functional endpoint theorem or its fixed-window consequences. The revision retains their full strength and applies the approved proof, attribution, and scope repairs below. The paper is a standalone active manuscript, not an extraction from the frozen monolith. Its main comparison concerns bottom labels and exponential-clock values; its Poisson--Dirichlet corollary is not a theorem about permutation cycle lengths.

This record separates mathematical review from compilation and finite numerical checks. It is not formal verification, independent external refereeing, or novelty certification. The audit identified substantial published overlap that the manuscript now acknowledges explicitly.

## Prior work and external inputs

- Jim Pitman and Ngoc M. Tran, *Size-biased permutation of a finite sequence with independent and identically distributed terms*, Bernoulli 21(4) (2015), 2484–2512, [primary paper](https://arxiv.org/pdf/1210.7856). Theorem 25 and Propositions 26–27 describe the power-law last-pick and rank-permutation limit and its marginals. The linear last-label integral and its value near 0.555228458706 already appear there. The PDF theorem numbering is used; the arXiv HTML rendering has different numbering. General regularly varying profiles, the functional coupling, and the additional comparisons must be assessed relative to this precedent, not presented as a newly discovered power-law construction.
- Marek Arendarczyk and Krzysztof Dębicki, *Asymptotics of supremum distribution of a Gaussian process over a Weibullian time*, Bernoulli 17(1) (2011), 194–210, [DOI 10.3150/10-BEJ266](https://doi.org/10.3150/10-BEJ266). Lemma 2.1, page 196, gives the Weibull-product tail asymptotic underlying the logarithmic example's scalar clock tail. The manuscript gives the specialization and its extremal-location argument explicitly.
- Borga–Chatterjee–Diaconis, *Permuton and local limits for the Luce model*, [arXiv:2509.07729v3](https://arxiv.org/html/2509.07729v3), supplies the conditional permuton-sample representation. Its Section 2.4 motivates the exact-versus-sampled comparison. Under its stated convention, the decreasing-clock chamber describes bottom positions, which the revised source states explicitly.

Other external inputs are Rényi's order-statistic representation, uniform convergence and Potter bounds for regular variation, strong laws and Borel–Cantelli, standard Poisson marking and mapping, the iid extreme-value point-process criterion, and the stable-jump Poisson--Dirichlet identification. They are cited in the source. No active companion paper is used as a mathematical premise.

## Retained theorem scope

| Result | Reviewed scope |
| --- | --- |
| Functional endpoint limit | For a measurable positive profile regularly varying at zero with index gamma greater than zero, and an essential positive lower bound away from zero, the normalized clock sequence converges almost surely in c-zero. It converges in ell-p for p at least one exactly in the summable range p times gamma greater than one. |
| Bottom-window universality | Every fixed bottom tuple eventually equals the limiting tuple under the Poisson-spacings and common-clock coupling, for almost every environment and almost every set of marks. The limiting ordering enumerates every positive integer. |
| Total-variation consequence | Every fixed window converges in both quenched and annealed total variation by the coupling inequality and dominated convergence. No quantitative rate is claimed. |
| Last-label laws | The integral probability mass function, generating function, exact survival integral, stretched-exponential logarithmic tail, and finite moments of every order for the limiting last label are retained. |
| Clock-value process | The limiting unlabeled clocks form an annealed power-law Poisson process. For gamma greater than one, their normalized ranked values have the stated Poisson--Dirichlet law and converge almost surely in ell-one. |
| Exact deterministic profiles | The grid-clock endpoint theorem uses pointwise positive lower bounds away from zero. A separate almost-everywhere grid-profile convergence condition is sufficient to identify the exact grid model's limiting permuton with the sampled one; the endpoint hypotheses alone do not guarantee this identification. |
| Critical profiles | Slowly varying endpoints give escape from every fixed label set. The logarithmic family has the displayed Poisson--Gumbel clock limit and a logarithmic bottom-label exponent; the statement does not assert convergence after division of the label by that power of n. |

## Proof and scope repairs applied

The main c-zero proof already controlled both escaping endpoint labels and interior labels. Potter's lower bound, the strong-law comparison of Poisson arrival times with their indices, and the almost-sure logarithmic maximum of the exponential marks give the uniform tail estimate. The ell-p proof has a summable endpoint majorant and an interior term tending to zero. Pairwise distinct positive coordinates in c-zero then justify continuity of fixed-window ranking and eventual equality. The revision records the immediate total-variation consequence explicitly.

The exact-grid comparison now separates its valid local endpoint theorem from the additional hypothesis needed for a common macroscopic permuton. Mere measurability does not identify values on the deterministic rational grid with the almost-everywhere profile sampled by independent uniforms. The point-process and Poisson--Dirichlet law statements are explicitly annealed; the Poisson arrival times are described as dependent partial sums of iid increments.

The last-label tail proof now starts from an exact survival integral and supplies explicit compact and tail estimates for the Laplace argument. The large-exponent calculation includes the integrable domination at small and large integration parameters. These repairs make the stated asymptotics auditable without changing their constants or exponent ranges.

In the logarithmic critical proof, extending the transformed integration domain is an upper bound, rather than an equality. Coercivity supplies an integrable bound on the unbounded domain. Upper-tail tightness and the order of limits, first a fixed level cutoff and then its removal, justify selecting each fixed number of largest atoms. The label conclusion retains its precise logarithmic normalization.

The orientation discussion retains the distinction between increasing draw order and decreasing bottom order. It no longer treats the displayed finite value 0.5551 as an exact limiting decimal. The attribution to Pitman–Tran and the scalar-tail citation to Arendarczyk–Dębicki are included in the mathematical exposition.

The multiple-zero direction now requires convergent local scale ratios and labels marked by zero, side, and local rank. Equal regular-variation exponents alone are insufficient: oscillating slowly varying ratios can produce distinct subsequential probabilities for the origin of the last clock. The ineffective fixed-truncation rate conjecture has been replaced by a research direction requiring errors uniform in a growing truncation. The broad critical-scale conjecture has also been replaced by a research direction with explicit tail and location targets. Leading asymptotic equivalence of slowly varying profiles does not by itself determine precise extreme-value centering, and an extra log–log factor can change the leading clock normalization. The exact-versus-sampled crossover remains a conjecture; numerical values are not certified uniqueness results.

## Repository integration and validation

The canonical catalog, README, theorem-status map, and dependency map register this manuscript immediately after `boundary-laws`. Frozen archives, existing manuscript sources, and existing audit records are preserved. The catalog records no active-paper dependencies. Existing repository checks already test catalog uniqueness, matching map order, dependency acyclicity, archive preservation, and navigation links; no duplicate catalog tests are added.

The catalog check, the existing normalized theorem/dependency-map test, navigation and Markdown checks with pending PDF links permitted, and `git diff --check` passed during integration.

Final local validation completed on 20 October 2026:

- **Manuscript build and closure:** the revised paper compiles to 21 pages with no overfull boxes, undefined references or citations, or multiply defined labels. The original 14 theorem/proposition/corollary statement bodies retain their mathematical scope; the sole wording change inside an existing statement corrects the dependence of Poisson arrival times. The new statement is the total-variation corollary. The two removed conjecture labels correspond to the passages deliberately recast as research directions. The author and title are unchanged.
- **Repository gates:** all 48 unit tests and all five registered finite consistency programs pass. Catalog, navigation, dependency-map, reference/citation, whitespace, and frozen-archive checks pass. All 15 active sources compile successfully in the local TeX environment.
- **Snapshot reproducibility:** the new paper's automatic PDF trailer identifier is suppressed locally in its source. Its complete PDF bytes match a second build into a different output directory. Rebuilding the 14 baseline papers locally changes only their automatic trailer identifiers: all other bytes are identical to the repository snapshots. Their original PDFs and manifest records are retained. The strict full-repository byte-for-byte check is unchanged and remains the existing PR workflow's gate in its runner environment; local content equivalence is recorded separately from that gate.
- **Numerical consistency:** 60-decimal working-precision quadrature gives the linear sampled probability as 0.55522845870614357735426716102582958, confirming all 26 printed decimal digits. Independent direct and transformed binary64 quadratures give the exact linear probability near 0.5160943231508148, a crossing near 1.49826071665266, and common probability near 0.663859139921823. Doubling the product cutoffs preserves the displayed digits. Analytic-form product and integration-tail bounds are smaller than the numerical quadrature uncertainty. These are numerical checks, not certified interval enclosures or a proof of uniqueness.
- **Visual review:** all 21 rendered pages were inspected for layout, equation and citation rendering, clipping, and page transitions. The repaired tail proof, exact-grid remark, critical proof, research directions, and complete bibliography were also checked at full-page resolution. The bibliography starts on its own page.

The successful builds and numerical agreement do not substitute for the mathematical review recorded above. Full PR validation must succeed before merge.
