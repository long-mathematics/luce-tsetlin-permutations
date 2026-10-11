# Macroscopic PD/GEM audit-repair record

Repair date: 11 October 2026  
Audit source: `audits/macroscopic-pd-proof-audit.md`  
Audited manuscript head: `025fbbc2ad072aad0577a2fdd5aec5edd640b748`  
Audit commit: `e71bfa3fa32c8095ce78e5d039006215386db82e`  
Audit merge on extraction branch: `f7eb751eb6d5a7afd21e2139f0d17176557120b4`  
Pre-repair source SHA-256: `a14de186ecc0fdb48763bebf260ca56755bc6670570c31bfbce6c419c2f9f73e`  
Post-repair source SHA-256: `0fdde5028985c4b639c7679e4f59256fb23e4983119a22bf60ea9d55bfbccdaa`

This record maps each localized recommendation in Section 9 of the adversarial audit to the exact correction applied in `papers/macroscopic-pd/poisson-dirichlet-luce.tex`. The frozen source under `archive/6178a99/` is unchanged. No correction below changes the comparable-rate hypothesis, the `PD(1)` or `GEM(1)` conclusions, the uniform-root conclusion, the `ell^1` topology, or the qualitative proof strategy.

## 1. Reduced slab conditioning and permanental law

**Resolved.** The manuscript now states explicitly that the ordered clock values inside each slab are *unlabeled*: the conditioning sigma-field does not record the label-to-order-statistic assignment and therefore does not determine the ranking within the slab. It writes the full assignment density

\[
\prod_{i\in H_{n,a}}\theta_{n,i}e^{-\theta_{n,i}s_{a,\phi(i)}},
\]

explains cancellation of the assignment-independent factor `prod_i theta_{n,i}`, identifies the permanent as the normalizing sum, and derives conditional independence across slabs from the product clock density and disjoint slab label sets.

Location: immediately before equation `eq:pd-permanental-row` and Lemma `lem:pd-residual-factorization`.

## 2. Post-stopping relative-prefix argument and small-beta choice

**Resolved.** The proof of Lemma `lem:pd-relative-prefix` now separates the two stopping cases:

1. `s_tau < a_m`, where the upper power bound at time `tau-1` forces `N_tau/m_b = o(1)`;
2. `N_tau < a_m`, where the lower power bound at time `tau-1` forces `s_tau/m = o(1)`.

It records the integer-safe estimates `s_{tau-1}<a_m+1` and `N_{tau-1}<a_m+1`, then explains why both normalized remaining counts stay small after stopping. The choice of `beta_0` now also imposes `beta_0 <= log 2`, so the harmonic-product exponents `e^{+/- beta}` used later lie in `[1/2,2]`.

Location: equations `eq:pd-prefix-log` through `eq:pd-prefix-before-stop`.

## 3. Noncircular GEM cutoff hierarchy

**Resolved.** The proof of Proposition `prop:pd-residual-uniforms` now displays a stage table. At deletion stage `r`, it records:

- current regularity at `T_{k-r+1}`;
- root-law inner cutoff `T_{k-r}`;
- root-law outer cutoff `T_{k-r+1}`;
- post-deletion regularity at `T_{k-r}`.

The text explicitly notes that every inner cutoff is fixed before its corresponding outer cutoff and that a successful deletion moves one level inward through the already chosen hierarchy.

Location: between the deterministic error recursion and event `eq:pd-interior-history`.

## 4. Independent residual roots and the `ell^1` upgrade

**Resolved.** The main theorem and the size-biased deletion subsection now specify that a new root is sampled independently and uniformly from the current residual set at every stage. The proof of Theorem `thm:macroscopic-pd` now displays the bounded-Lipschitz truncation estimate

\[
\begin{aligned}
|E F(X_n)-E F(X)|
&\le \operatorname{Lip}(F)(E R_{n,k}+E R_k)\\
&\quad+|E F(X_n^{(k)})-E F(X^{(k)})|,
\end{aligned}
\]

and takes first `n -> infinity` and then `k -> infinity`. It cites the bounded-Lipschitz criterion on the separable metric space `ell^1` rather than leaving the topology upgrade implicit.

Location: Theorem `thm:macroscopic-pd`, the opening paragraph of “Independent residual fractions,” and the proof of the main theorem after `eq:pd-tail-mass`.

## 5. Power-sum expectation wording

**Resolved.** The final sentence of Corollary `cor:pd-power-sums` now invokes weak convergence plus bounded continuity of the power-sum functional. It no longer calls this step “bounded convergence,” which was formally imprecise.

Location: final sentence of the proof of Corollary `cor:pd-power-sums`.

## 6. Textbook references for standard imports

**Resolved.** The model/dependency section and bibliography now give explicit references for:

- weak compactness and disintegration on standard Borel spaces: Kallenberg, Chapters 4 and 6;
- Kolmogorov and Doob maximal inequalities: Durrett, Chapters 2 and 4;
- bounded-continuous expectation convergence and continuous mapping: Billingsley, Theorems 2.1 and 2.7;
- the bounded-Lipschitz criterion: Dudley, Section 11.3;
- the `GEM(1)`/`PD(1)` relation: Pitman, Chapter 3.

Location: Section 1 and the bibliography.

## Scope retained

The repaired manuscript does **not** assert any of the following:

- a quantitative rate of convergence;
- a quenched theorem uniform over arbitrary deletion histories;
- endpoint-singular macroscopic universality without the fixed rate-ratio bound;
- a mesoscopic or total-cycle result;
- formal verification, novelty certification, or independent external refereeing.

## Regression and build checks

The structural checker `scripts/macroscopic-pd/check_audit_repairs.py` verifies archive immutability, preservation of all original labels and internal references, the count of theorem environments, the unchanged main-theorem scope, absence of the prohibited strengthenings above, and the presence of all six repair classes. `tests/test_macroscopic_extraction.py` independently checks theorem scope, citation additions, repair records, and dependency exclusions.

The repaired manuscript compiles to 21 pages. Its deterministic PDF SHA-256 is `ee6ae8cdca53859c43ffbbfa54b402811821f1213c8add1eaa62313eebc8f3d4`. All 21 pages were rendered and inspected, including every page containing new clarification text; no clipping, overlap, missing glyph, broken display, or evident layout defect was found. The repository passed `make test`, byte-identical `make check`, and every registered finite consistency program under `make verify`.
