# Audit: functional Luce Erdős–Turán theorem and the total-cycle CLT

Audit date: 11 October 2026.

Repository: `long-mathematics/nonuniform-random-permutations`.

Frozen commit: `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`.

## 1. Verdict and scope

**The total-cycle central limit theorem passes this audit.** The newer functional working manuscript supplies a valid route from the comparable-rate switching theory to

\[
\frac{K_n-\log n}{\sqrt{\log n}}\Rightarrow N(0,1),
\qquad K_n=\sum_{r=1}^n C_{n,r}.
\]

The audited hypothesis is the full triangular-array hypothesis

\[
\sup_n\frac{\max_i\theta_{n,i}}{\min_i\theta_{n,i}}<\infty.
\]

There is no sampled-profile hypothesis, no smoothness hypothesis, and no macroscopic Poisson–Dirichlet input in the relevant proof chain. After rescaling, fix \(1\le\theta_{n,i}\le\kappa\).

The count-process functional CLT and the stated joint functional limit with logarithmic permutation order also pass the audit. The arithmetic step for the latter was checked separately; it is not needed for the count-only theorem.

The conclusion is a mathematical assessment of the written proofs, not a formal proof verification or an independent novelty assessment. No new review of Paper I or of Paper IV's sharp normal approximation was performed. No repository files were changed, and no new compilation or PDF-layout check is claimed.

### Audited sources

All source references below are to the frozen commit above. Line ranges are TeX source lines, not PDF page numbers.

| Code | Path | Git blob SHA |
|---|---|---|
| F | `notes/working/functional-luce-erdos-turan.tex` | `bc3769c671dcb77657871b6d3fafc8879075d079` |
| II | `papers/02-mesoscopic-luce-cycles/mesoscopic-luce-cycles.tex` | `cb8e806ee252e329a221ba126b998a69bef263c4` |
| III | `papers/03-luce-erdos-turan/luce-erdos-turan.tex` | `b5ca7fd1ccfd4a8102c756056446a76553abd9de` |

F was read through its main arguments, appendices, and bibliography. The relevant upstream arguments in II and III were traced rather than merely accepted because they were labeled as inputs.

## 2. Dependency map

The count theorem uses the following chain:

\[
\begin{gathered}
\text{exact marked clock swap + selected-factor tails}
\\\Downarrow\\
\text{crude cycle/root bounds + fixed-two-root endpoint comparison}
\\\Downarrow\\
\text{quantitative }L^1\text{ concentration of }S_{n,r}/n
\\\Downarrow\\
\text{summable Campbell error on a growing window}
\\\Downarrow\\
\text{dimension-free product-Poisson approximation}
\\\Downarrow\\
\text{Poisson CLT + }L^1\text{ restoration of omitted cycles}.
\end{gathered}
\]

The precise high-dimensional transfer is the new part of F. It does **not** require an endpoint theorem with a growing number of roots. One- and two-root comparisons suffice to control a scalar switching intensity. Arbitrary bounded tests of the entire growing vector are then handled by the exact marked identity and the dimension-free Stein factor.

The joint order theorem additionally uses III's rate-oriented three-clock identity and product-to-LCM estimate. Those steps are downstream of, and logically separate from, the count CLT.

## 3. Exact switching identity and selected-factor bounds

**Sources:** II, `prop:master-switch`, `cor:selected-moments`, `cor:root-crude`; III, lines 150–256; F, lines 325–396.

For distinct labels define

\[
R_{ij}=\exp\{-(\theta_i-\theta_j)(X_j-X_i)\},
\qquad R_{ii}=1,
\]

and

\[
S_{n,r}=\sum_{i:L_n(i)>r}R_{i,\sigma_n^r(i)}.
\]

Swapping \(X_i,X_j\) right-composes the rank permutation by \((i\ j)\). The density ratio is exactly \(R_{ij}\). For any bounded test \(\Phi\),

\[
r(n-r)\mathbb E[C_{n,r}\Phi(\sigma_n)]
=
\mathbb E\sum_{i:L_n(i)>r}R_{i,\sigma_n^r(i)}
\Phi(\sigma_n\circ(i\ \sigma_n^r(i))).
\tag{3.1}
\]

The normalization and orientation are correct. The split creates an \(r\)-cycle containing the endpoint \(j=\sigma_n^r(i)\); the residual cycle contains \(i\). Reversing the construction gives \(r\) choices for the mark on each target \(r\)-cycle and \(n-r\) choices for the external mark. The case in which the other split cycle also has length \(r\) is counted correctly.

The selected-factor moment bound is not an unjustified replacement of an adaptively selected endpoint by an independent label. If \(\theta_i>\theta_j\) and \(\log R_{ij}>u\), then

\[
X_i>u/(\theta_i-1).
\]

The other rate ordering gives the corresponding bound for \(X_j\). The map \(i\mapsto\sigma_n^r(i)\) is a bijection on the invariant set \(\{i:L_n(i)>r\}\). Reindexing by the endpoint therefore gives, for \(\kappa>1\),

\[
\frac1n\mathbb E\sum_{i:L_n(i)>r}
\mathbf1_{\{\log R_{i,\sigma_n^r(i)}>u\}}
\le 2e^{-\lambda_\kappa u},
\qquad \lambda_\kappa=\frac\kappa{\kappa-1}.
\tag{3.2}
\]

Layer-cake integration proves the selected \(p\)-moment bound for every \(1<p<\lambda_\kappa\), and the first-moment truncation tail is \(O_\kappa(A^{-1/(\kappa-1)})\). Equal rates cause no difficulty: all swap factors are one.

Setting \(\Phi=1\) in (3.1) gives

\[
\mathbb EC_{n,r}\le \frac{C_\kappa n}{r(n-r)},\qquad r<n.
\tag{3.3}
\]

Consequently, for an independent uniform root \(I\),

\[
\mathbb P(L_n(I)\le a)\le C_\kappa a/n,\qquad a\le n/2.
\tag{3.4}
\]

This establishes root escape internally. It avoids a circular appeal to a macroscopic cycle theorem. The singular denominator at \(r=n\) is never used: the large-cycle restoration treats cycles longer than \(n/2\) by their deterministic count bound of one.

## 4. Audit of the finite-endpoint input

**Sources:** II, lines 505–1660, especially `lem:permanental-rows`, `lem:good-environment`, `lem:depletion-stopping`, `lem:reset-mixing`, `lem:terminal-uniform`, `prop:endpoint-mixing`, and the exact-clock observable corollaries.

The important conditioning distinctions are respected in the newer proof.

1. The environment records the label sets in each block and ordered **unlabeled** clock values. It does not record their full assignment to labels. Conditional residual matching randomness remains.
2. Hereditary flatness is proved by a swap of two target assignments. In a block of width at most \(h\), its multiplicative error is \(e^{\pm\kappa h}\), uniformly after compatible exposures.
3. The terminal tail is not assumed to have uniformly dense cells. The proof separates a finite core from a small tail and resets the tail row of the comparison kernel.
4. Prefix depletion is controlled along the realized random-root exploration. It is not claimed to hold simultaneously over all counterfactual histories. The relevant good event is measurable at the frozen-prefix stage.
5. The adaptive terminal process is compared to a **fixed** frozen reset kernel using conditional one-step error bounds. It is not incorrectly treated as a product of path-dependent transition matrices.

### Core and tail scales

For fixed \(q\), write

\[
K=qr_+,\quad \delta=K/n,\quad h=\delta^{1/4},
\quad \rho=\delta^{1/(4\kappa)},\quad M=\sqrt{nK}.
\]

Finite rows have size at least a constant times \(M\). Early cells have size at least a constant times \(hM\). The interval-uniform Bernoulli estimates are taken over all deterministic integer intervals, so they legitimately apply afterward to the random rank intervals.

The frozen-prefix depletion bounds follow from uniformity of \(\sigma^t(I)\) conditional on the full permutation, followed by Markov's inequality and a union bound. Their total error is

\[
O_q(\delta^{3/4}\log(1/\delta)+\delta^{1/2}\log(1/\delta)).
\]

The orbit-intersection bound is linear, not quadratic, in the exposed lengths: two orbit segments on one permutation can intersect only when their starting roots lie in a single enlarged arc. This gives the required \(O_q(r_+/n)\) bound.

### Residual bookkeeping and fixed reset kernel

For disjoint open prefixes, the residual source and target sets satisfy

\[
T^0\setminus S^0=\{\text{roots}\},\qquad
S^0\setminus T^0=\{\text{current tips}\}.
\]

This identity persists through compatible terminal exposures. In particular, no currently available target that belongs to the original residual source set has already been used as a source. The completed reset kernel therefore has the asserted interpretation.

Before resetting the tail row, its stationarity defect is exactly

\[
(p^0\widehat P^0-p^0)_b=\frac{q\nu_b-e_b}{N_0},
\]

where \(e_b\) counts the missing-target tips in source row \(b\). Thus its total-variation defect is at most \(q/N_0\). Resetting the tail costs at most its mass \(O(\rho)\). The early-cell minorization yields a fixed positive Doeblin constant.

The terminal coupling costs

\[
O_q\left(mh+\frac{m^2}{M}+m\rho+\frac{m\log n}{M}\right),
\]

in addition to geometric mixing and residual-uniform comparison errors. Averaging from the prefix sigma-field down to the coarse environment is justified by convexity of conditional total variation. No conditioning on future successful terminal behavior is inserted.

**Finding:** no unresolved gap was found in the fixed-one/two-root endpoint argument needed here.

## 5. The important quantitative interface clarification

**Sources:** II, lines 1490–1635; III, lines 282–425; F, lines 420–467.

II states its truncated-factor decorrelation corollary for fixed truncation levels. III and F require a bound usable when the truncation level grows. Reading only the fixed-level statement would not justify that use. Reading the proof does: its dependence on the bound and Lipschitz constant is explicit.

Let \(F_A(i,j)=R_{ij}\wedge A\), and define

\[
S^{(A)}_{n,r}=\sum_{i:L_n(i)>r}F_A(i,\sigma_n^r(i)),
\quad
D_{n,A}=n^{-2}\sum_{i,j}F_A(i,j),
\quad \mu_{n,A}=\mathbb ED_{n,A}.
\]

The function \(z\mapsto e^z\wedge A\) is bounded by \(A\) and is \(A\)-Lipschitz. Coarsening a finite-block clock changes \(\log R_{ij}\) by at most \(2\kappa h\). A product of two truncated factors has sup norm \(A^2\) and telescoping coarsening cost \(O_\kappa(A^2h)\). Tail and short-root events cost the same sup norm times their probabilities.

Consequently the one/two-root estimate gives, uniformly for every \(A\ge1\),

\[
\left|\mathbb E[S^{(A)}_{n,r}/n]-\mu_{n,A}\right|
\le C_\kappa A\Gamma_{n,a},
\tag{5.1}
\]

\[
\left|\mathbb E[(S^{(A)}_{n,r}/n)^2]-\mathbb ED_{n,A}^2\right|
\le C_\kappa A^2\Gamma_{n,a}.
\tag{5.2}
\]

These are exactly the quantitative interface used in III. The constants do not acquire an additional uncontrolled dependence on \(A\).

Notice that the second fresh-pair expectation is \(\mathbb ED_{n,A}^2\), not \(\mu_{n,A}^2\). The proof correctly retains the dependence caused by shared clocks. Changing one clock changes \(D_{n,A}\) by at most \(2A/n\), so Efron–Stein gives

\[
\operatorname{Var}D_{n,A}\le 4A^2/n.
\]

The centered second-moment identity in III is correct. Combining it with (5.1)–(5.2), and then removing the truncation using (3.2), gives

\[
\Delta_{n,r}:=\mathbb E|S_{n,r}/n-1|
\le C_\kappa\left[A(\Gamma_{n,a}+n^{-1})^{1/2}
+A^{-1/(\kappa-1)}\right].
\]

Optimizing \(A\) gives

\[
\Delta_{n,r}\le C_\kappa(\Gamma_{n,a}+n^{-1})^{1/(2\kappa)}.
\tag{5.3}
\]

The equal-rate case follows without truncation. In particular, this argument does not assume a uniformly bounded **untruncated second moment** of a selected swap factor, which would exceed the available moment threshold for some \(\kappa\).

**Recommended source change:** promote (5.1)–(5.2) to an explicit quantitative corollary in II, or reproduce their short derivation at the import point. This closes a presentation/interface ambiguity, not a missing probabilistic estimate.

## 6. Unweighted dyadic summability

**Source:** F, lines 496–592, `prop:unweighted`.

Set \(L=\log n\) and

\[
b_n=\lceil L^3\rceil,\qquad U_n=\lfloor n/L^{A_0}\rfloor,
\qquad \mathcal I_n=\{r:b_n<r\le U_n\}.
\]

Choose \(p\) once as a function of \(\kappa\), with \(1<p<\lambda_\kappa\), and put \(\beta=1-1/p\). The manuscript's cutoff requirement is more than sufficient; the exceptional-source summation needs \(A_0\beta>1\).

For \(a_j=2^jb_n\), put \(\delta_j=4a_j/n\) and \(L_j=\log(1/\delta_j)\). The terminal depth is eventually \(m_j\asymp\sqrt{L_j}\), uniformly over the blocks. Furthermore,

\[
L_j\ge A_0\log L-O(1).
\]

The values \(L_j\) lie on a lattice with spacing \(\log2\). This is important: one sums the decaying error over that lattice instead of multiplying its largest value by \(O(L)\).

The reset contribution is bounded by

\[
C\sum_{L_j\ge A_0\log L-O(1)}e^{-c\sqrt{L_j}}
\le C(1+\sqrt{\log L})e^{-c'\sqrt{\log L}}=o(1).
\]

After taking the power \(\eta=1/(2\kappa)\), the positive-power \(\delta_j\) contributions have the form \(CL_j^d e^{-\gamma L_j}\), with \(\gamma\ge1/(8\kappa^2)\). Their lattice sums also vanish.

The finite-size terms satisfy

\[
\frac{m_j^2+m_j\log n}{n\delta_j^{1/2}}
\le C\frac{L^{3/2}}{\sqrt{na_j}}\le Cn^{-1/2}.
\]

After raising to \(\eta\) and summing \(O(L)\) blocks, this contributes \(O(Ln^{-1/(4\kappa)})\). The exponential environment errors are negligible; the polynomial environment errors also sum to zero.

Therefore

\[
\varepsilon_n^{\rm sw}:=
\sum_{j:a_j\le U_n}\sup_{a_j\le r<2a_j}\Delta_{n,r}\longrightarrow0.
\tag{6.1}
\]

This is a genuinely re-derived estimate, not an invalid inference from the weaker weighted summation used for the scalar order theorem. The final partially intersected block causes no problem: the endpoint input applies throughout \(a\le r<2a\), even when only part of that block enters \(\mathcal I_n\).

## 7. Campbell identity and the dimension-free Stein transfer

**Source:** F, lines 596–838, `lem:good-split`, `lem:exceptional`, `prop:Campbell`, `lem:Stein`.

Write \(\xi_n=(C_{n,r})_{r\in\mathcal I_n}\) and

\[
a_{n,r}=\frac{n}{r(n-r)}=\frac1r+\frac1{n-r}.
\]

If \(L_n(i)>r+U_n\), the switch creates one \(r\)-cycle and leaves every other intermediate coordinate unchanged:

\[
\xi_n(\sigma_n\circ(i\ \sigma_n^r(i)))=\xi_n+e_r.
\tag{7.1}
\]

The strict inequality is correct. It ensures both the source cycle and the residual split cycle lie above \(U_n\).

The exceptional weighted source mass is

\[
B_{n,r}:=\frac1n\mathbb E\sum_{i:r<L_n(i)\le r+U_n}
R_{i,\sigma_n^r(i)}.
\]

Hölder's inequality, the selected \(p\)-moment estimate, and (3.4) give

\[
B_{n,r}\le C_\kappa(U_n/n)^\beta.
\tag{7.2}
\]

For arbitrary functions \(g_r:\mathbb Z_+^{\mathcal I_n}\to[-1,1]\), use the marked identity with the shifted vector test. On the good split, (7.1) gives exactly \(g_r(\xi_n)\). On a bad split the difference is at most two. Consequently,

\[
\left|\mathbb E[C_{n,r}g_r(\xi_n-e_r)]
-a_{n,r}\mathbb Eg_r(\xi_n)\right|
\le a_{n,r}\Delta_{n,r}+2a_{n,r}B_{n,r}.
\tag{7.3}
\]

The factor two and the normalization are correct. Since \(a_{n,r}\le2/r\) on the window, harmonic summation within each dyadic block and (6.1) yield

\[
\left|\mathbb E\sum_r C_{n,r}g_r(\xi_n-e_r)
-\sum_r a_{n,r}\mathbb Eg_r(\xi_n)\right|
\le C_\kappa\varepsilon_n^{\rm sw}
+C_\kappa L(U_n/n)^\beta=:\varepsilon_n=o(1).
\tag{7.4}
\]

This holds for tests of the full growing vector. There is no independence assumption between \(g_r(\xi_n)\) and the switching intensity: their product is bounded using \(|g_r|\le1\) and the \(L^1\) intensity error.

### Stein factor

For the product-Poisson immigration–death generator,

\[
\mathcal Ah(\eta)=\sum_r a_{n,r}[h(\eta+e_r)-h(\eta)]
+\sum_r\eta_r[h(\eta-e_r)-h(\eta)],
\]

the semigroup solution for an indicator test has

\[
\sup_{\eta,r}|h(\eta+e_r)-h(\eta)|\le\int_0^\infty e^{-t}\,dt=1.
\tag{7.5}
\]

The coupling consists of one extra initial particle, whose lifetime has mean one. Thus the constant is independent of the dimension and total intensity. The first-moment integrability required for the generator expectation is automatic here; in the abstract lemma it is also forced by taking all tests equal to one.

Equations (7.4)–(7.5) prove

\[
d_{\rm TV}\left(\mathcal L(\xi_n),\bigotimes_{r\in\mathcal I_n}
\operatorname{Pois}(a_{n,r})\right)\le\varepsilon_n.
\]

Replacing the intensities by \(1/r\) costs at most

\[
\sum_{r\in\mathcal I_n}\frac1{n-r}=O(U_n/n)=o(1).
\]

Hence the manuscript's growing-dimensional product-Poisson theorem is valid. The configuration-space immigration–death construction is standard Poisson-process Stein theory; the Luce-specific work is in establishing the summable Campbell error, not in inventing that generator.

## 8. Direct derivation of the total-cycle theorem

**Sources:** F, lines 1038–1154; additional expectation conclusion derived here from the exact one-switch identity.

Set

\[
K_n^\circ=\sum_{r\in\mathcal I_n}C_{n,r},\qquad
R_n=K_n-K_n^\circ\ge0.
\]

The sum of the independent Poisson reference coordinates is Poisson with parameter

\[
\mu_n=\sum_{r\in\mathcal I_n}\frac1r
=\log n-(A_0+3)\log\log n+o(1).
\tag{8.1}
\]

Thus \(\mu_n/\log n\to1\), and \((\mu_n-\log n)/\sqrt{\log n}\to0\). The ordinary Poisson CLT and total-variation contraction under summation give

\[
\frac{K_n^\circ-\log n}{\sqrt{\log n}}\Rightarrow N(0,1).
\]

The omitted ranges satisfy

\[
\mathbb ER_n
\le C_\kappa\{\log b_n+1+\log(n/U_n)\}
=O_\kappa(\log\log n).
\tag{8.2}
\]

For the upper tail, sum the crude \(C_\kappa/r\) bound only up to \(n/2\), then use the deterministic bound of one above \(n/2\). Therefore

\[
R_n/\sqrt{\log n}\to0\quad\text{in }L^1.
\]

Slutsky proves

\[
\boxed{\frac{K_n-\log n}{\sqrt{\log n}}\Rightarrow N(0,1).}
\tag{8.3}
\]

This last deduction is complete; there is no remaining cumulant-transfer hypothesis.

### Exact-mean centering

Do not infer convergence of an unbounded expectation from total variation alone. Instead, (3.1) gives directly

\[
\sum_{r\in\mathcal I_n}|\mathbb EC_{n,r}-a_{n,r}|
\le\sum_{r\in\mathcal I_n}a_{n,r}\Delta_{n,r}=o(1).
\]

Combining this with (8.1)–(8.2) proves

\[
\mathbb EK_n=\log n+O_\kappa(\log\log n).
\tag{8.4}
\]

In particular,

\[
\boxed{\frac{K_n-\mathbb EK_n}{\sqrt{\log n}}\Rightarrow N(0,1).}
\tag{8.5}
\]

The same reasoning gives a uniform-in-time expectation-centering error of order \(\log\log n\) for the count process.

## 9. Functional and multivariate assertions

**Sources:** F, lines 840–1318.

For the independent reference variables \(Z_{n,r}\sim\operatorname{Pois}(a_{n,r})\), define

\[
M_n(t)=\frac1{\sqrt L}\sum_{r\in\mathcal I_n,\,r\le n^t}
(Z_{n,r}-a_{n,r})\binom{1}{\sqrt3\log r/L}.
\]

The covariance partial sums converge uniformly to

\[
Q(t)=\begin{pmatrix}
t&\frac{\sqrt3}{2}t^2\\
\frac{\sqrt3}{2}t^2&t^3
\end{pmatrix}.
\]

The sum of fourth moments of its vector increments is \(O(1/L)\), using
\(\mathbb E(Z-\lambda)^4=\lambda+3\lambda^2\). This yields Lindeberg. Together with the covariance control, it justifies the independent-increment/martingale functional CLT and continuous-limit tightness. Vanishing maximum jumps alone would not imply tightness, so a final version should keep the covariance/tightness argument attached to the brief remark following this calculation.

Total variation transfers the entire path law. Restoring omitted lengths and deterministic centers is uniform in \(t\), because the omitted sums are nonnegative and their maximum occurs at the endpoint. Both cutoff transitions are covered: before the lower cutoff the omitted deterministic count center is at most \(\log b_n\); after the upper cutoff it is at most \(\log(n/U_n)\). Both are \(O(\log\log n)\).

For bounded Riemann-integrable weights, the needed harmonic measures converge weakly to Lebesgue measure, and the test discontinuity set has Lebesgue measure zero. This supplies the general weighted variance convergence used in F's Gaussian-field proposition, including degenerate linear combinations.

### An optional shorter verification of the common-noise limit

Let \(M_n^K\) be the first coordinate of the reference process and \(M_n^B\) its second coordinate. The exact finite-sum identity

\[
M_n^B(t)=\sqrt3\left[tM_n^K(t)-\int_0^tM_n^K(u)\,du\right]
\]

follows by integration by parts. Once \(M_n^K\Rightarrow W\), continuity of this map at continuous paths gives jointly

\[
(M_n^K,M_n^B)\Rightarrow
\left(W(t),\sqrt3\int_0^t u\,dW(u)\right).
\]

This is an independent check of the normalization and shared-noise covariance, and an optional simplification of the vector functional-CLT presentation.

## 10. Arithmetic transfer for the joint order theorem

**Sources:** III, lines 700–1022; F, lines 1157–1254 and Appendix A.

III's three-clock construction uses a rate-ordered cyclic orientation with one positive coefficient in the log density ratio. Reorganizing the target marks into the two possible source-arc patterns gives

\[
rs(n-r-s)\mathbb E[C_{n,r}(C_{n,s}-\mathbf1_{\{r=s\}})]
=\mathbb E\mathcal I_{n;r,s}.
\]

The orientation and multiplicity when \(r=s\) are correct. In each of six source/endpoint classes, the maximum-rate label is an injective image of the source under a fixed permutation power. Its exponential tail therefore proves \(\mathbb E\mathcal I_{n;r,s}\le C_\kappa n\), and hence the asserted factorial bound for \(r+s\le n/2\).

The von Mangoldt decomposition, split at \(y=(\log n)^2\), then gives

\[
\mathbb E[B_n(1)-\log\operatorname{ord}(\sigma_n)]
=O_\kappa(\log n\log\log n).
\]

For the process, each divisibility count is nondecreasing, so

\[
\sup_{0\le t\le1}[B_n(t)-\mathcal O_n(t)]
=B_n(1)-\log\operatorname{ord}(\sigma_n).
\]

Thus the endpoint estimate already gives the needed uniform-in-time perturbation bound. No extra joint arithmetic theorem is needed. This validates the stated joint functional theorem and its endpoint correlation \(\sqrt3/2\).

The abstract appendix should explicitly take \(t\in[0,1]\) and assume càdlàg cutoffs/processes (or otherwise state that both processes are random elements of \(D\)). The main cutoff \(\lfloor n^t\rfloor\) already has this property; this is only a scope clarification for the generalized appendix.

## 11. Exact finite checks performed

The companion script uses only exact integer and rational arithmetic, with no simulation and no third-party packages. It checks finite combinatorial identities, not the asymptotic probability estimates.

| Check | Range | Result |
|---|---|---|
| Two-clock marked coefficient identity | All permutations, \(2\le n\le8\) | 316,646 coefficient checks passed |
| Split orientation and marked cycle membership | Same range | 1,246,964 switches passed |
| Entire-vector effect at all admissible tested upper cutoffs | Same range | 1,492,038 cutoff checks passed |
| Rate-oriented three-clock coefficient identity, including equal lengths | All permutations, \(3\le n\le7\), two rate-order profiles | 167,196 coefficient checks passed |
| Three-clock selected split membership | Same range | 384,204 selected summands passed |
| Residual-set and completed-kernel stationarity-defect identities | All permutations, \(2\le n\le6\), all single-root open prefix lengths, a three-block partition | 12,164 histories and 36,492 coordinate identities passed |

The main asymptotic findings rest on the analytic derivations in Sections 3–10, not on these finite checks.

## 12. Changes recommended before promotion

### Mathematical exposition

- State the uniform-in-truncation estimates (5.1)–(5.2) explicitly at the II-to-III interface.
- Add an explicit total-cycle corollary containing (8.3), (8.4), and (8.5), rather than leaving the count CLT only as the first coordinate at \(t=1\).
- State the two tail-count estimates and the intermediate expectation calculation alongside that corollary. This makes clear why no unbounded-moment claim is inferred from total variation.
- For the general weighted field, add the harmonic-measure justification for bounded Riemann-integrable test functions.
- Tie \(p\) to \(\kappa\) when claiming constants depend only on \(\kappa\), and retain an explicit functional-CLT/tightness reference or the integration-by-parts verification above.

### Status and references

F's bibliography still calls II a proof “under submacroscopic root-cycle escape,” although the current II proves that estimate internally. Its reference to the Berry–Esseen supplement uses an older “checkpoints” title. The discussion of square-root-depth qualitative accuracy should distinguish this branch's chosen depth from the later linear-depth quantitative machinery. These are stale-reference/status issues, not defects in the count proof.

The repository's total-cycle status should distinguish the invalid historical candidate from the later Campbell–Stein proof. The appropriate result-level status after this audit is: **total-cycle and joint functional CLTs supported by the audited working-branch proof**, with the modest clarifications above incorporated on promotion.

## 13. What is not established by this audit

This audit does not establish the profile-dependent constant in

\[
\mathbb EK_n=\log n+\kappa_f+o(1),
\]

nor the bounds \(\kappa_j(K_n)=\log n+O_j(1)\). Those do not follow from the distributional CLT.

Likewise, \(\operatorname{Var}K_n\sim\log n\) is not asserted merely from weak convergence or total variation. Additional moment/uniform-integrability arguments are needed to certify that statement. Covariance formulas in the functional theorem describe its Gaussian limit; they must not be silently promoted to finite-\(n\) covariance asymptotics.

A sharp \(O_\kappa((\log n)^{-1/2})\) Berry–Esseen bound for total cycles is also outside this verdict. This version uses a square-root-depth error that vanishes too slowly for that rate, and the \(L^1\) restoration estimate alone does not provide optimal Kolmogorov precision. The later quantitative machinery is a possible input to the next task, not a result certified here.

## Standard references checked

A. D. Barbour and T. C. Brown, *Stein's method and point process approximation*, Stochastic Processes and their Applications 43 (1992), 9–31. DOI: `10.1016/0304-4149(92)90073-Y`.

W. Whitt, *Proofs of the martingale FCLT*, Probability Surveys 4 (2007), 268–302. DOI: `10.1214/07-PS122`; arXiv: `0712.1929v2`.

The proof of the particular dimension-free Stein estimate needed here was also reconstructed directly in Section 7. No general theorem about fixed-dimensional convergence was used to justify a growing-dimensional approximation.
