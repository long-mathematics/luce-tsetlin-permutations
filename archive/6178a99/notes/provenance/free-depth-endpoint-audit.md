# Independent audit of the free-depth finite-endpoint theorem

## Scope

This audit reviews the finite-endpoint section of
`Conjecture_13_1_switching_proof_strengthened.tex`, with special attention
to whether the terminal-window depth can be left free and specialized to
linear depth

\[
  m\asymp \log(1/\delta)
\]

on logarithmic Berry--Esseen windows.

## Verdict

The free-depth strengthening is valid.  No step of the endpoint proof
uses the former choice

\[
  m\asymp \sqrt{\log(1/\delta)}
\]

except to verify a collection of explicit asymptotic conditions.  Once
those conditions are stated directly, the proof is uniform over every
admissible depth.

The audit also found that the manuscript's external submacroscopic
root-cycle escape assumption is redundant.  The exact master switching
identity and the selected-factor first moment imply

\[
  \mathbb E C_{n,r}\le \frac{C_\kappa n}{r(n-r)},
  \qquad
  \mathbb P\{L_n(I_n)\le a\}\le C_\kappa a/n
  \quad(a\le n/2).
\]

Thus the mesoscopic theorem and the polynomial global endpoint estimate
are self-contained under uniform rate comparability.

## Audited free-depth theorem

For fixed \(q\), put

\[
  K=qr_+,
  \qquad \delta=K/n,
  \qquad h=\delta^{1/4},
  \qquad \rho=\delta^{1/(4\kappa)},
  \qquad M=\sqrt{nK}.
\]

A terminal depth \(m=m_n\) is admissible when

\[
  1\le m\le r_-/3,
\]

and

\[
  m\to\infty,
  \quad mh\to0,
  \quad m\rho\to0,
  \quad \frac{m^2}{M}\to0,
  \quad \frac{m\log n}{M}\to0,
  \quad \frac{m}{hM}\to0.
\]

For every such depth, the endpoint error satisfies

\[
\begin{aligned}
\Delta_{n,q}\le C_{\kappa,q}\bigg[&
 (1-\alpha)^{m-1}
 +mh+\frac{m^2}{M}
 +m\rho+\frac{m\log n}{M}
 +\rho+\delta+\delta^{1/2}\log(1/\delta)\\
&+h^{-1}\log(1/\delta)e^{-cM}
 +n^2h^{-1}e^{-chM}
 +n^{-2}
\bigg].
\end{aligned}
\]

This tends to zero for every admissible depth.

## Complete dependency map for \(m\)

The proof was checked from the frozen-prefix construction through the
sequential terminal coupling.

1. **Prefix definition.**  The condition \(m\le r_-/3\) ensures every
   prefix length \(r_\ell-m\) is nonnegative and at least two thirds of
   the observed orbit remains in the frozen prefix.

2. **Environment and prefix depletion.**  Their bounds are independent
   of \(m\).  Shorter prefixes can only reduce the depletion counts.

3. **Residual rows.**  At most \(qm\) targets are deleted during all
   terminal windows.  The condition \(m/(hM)\to0\) preserves both the
   row-size and early-cell margins.

4. **One-step adaptive comparison.**  Hereditary flatness contributes
   \(O(h)\); deletion of frozen targets contributes \(O(m/M)\).  Across
   \(m\) steps these become \(O(mh+m^2/M)\).

5. **Tail-row failures.**  The per-step tail probability is
   \(O(\rho+\log n/M)\); accumulation gives
   \(O(m\rho+m\log n/M)\).

6. **Reset mixing.**  The only role of \(m\to\infty\) is to force
   \((1-\alpha)^{m-1}\to0\).

7. **Final target and residual-uniform comparison.**  Their errors are
   \(O(h+m/M+\rho+K/n)\), already absorbed by the displayed bound for
   \(m\ge1\).

No hidden use of square-root depth was found.

## Linear-depth specialization

Let \(L=\log n\).  On a window

\[
  L^3\le r_-\le r_+\le n/L^A,
\]

choose

\[
  m=\lfloor\log(1/\delta)\rfloor.
\]

Then

\[
  m\le L+O_q(1)\ll r_-,
\]

and

\[
  \frac{m^2+m\log n}{M}
  \ll \frac{L^{1/2}}{\sqrt n},
  \qquad
  \frac{m}{hM}
  \ll \frac1{n^{1/4}L^{5/4}}.
\]

The reset and positive-power terms are bounded by a logarithmic factor
times a positive power of \(\delta\).  Therefore, for every fixed
\(Q>0\), choosing \(A=A(\kappa,q,Q)\) sufficiently large gives

\[
  \varepsilon_{n,q}=O_{\kappa,q,Q}(L^{-Q}),
  \qquad
  \Delta_{n,q}=O_{\kappa,q,Q}(L^{-Q}).
\]

The second estimate is genuinely global because the internally proved
root bound gives

\[
  \zeta_n=\mathbb P\{L_n(I_n)\le r_+\}
  \le C_\kappa r_+/n.
\]

## Additional proof corrections and clarifications

- The environment failure probability is now recorded explicitly:

  \[
    \mathbb P(\mathcal G_n^c)
    \le C\left[
      h^{-1}\log(1/\delta)e^{-cM}
      +n^2h^{-1}e^{-chM}
      +n^{-2}
    \right].
  \]

- The prefix-depletion probability is now recorded explicitly as
  \(O_q(\delta^{1/2}\log(1/\delta))\).

- The theorem remains fixed-\(q\).  No growing-\(q\), quenched, or
  arbitrary-deletion result is claimed.

- Untruncated products of multiple swap factors still require the
  existing moment threshold \(q<\lambda_\kappa\); the free-depth
  strengthening does not change that restriction.

## Build and visual checks

- The revised source compiles with `pdflatex` in three passes.
- All cross-references resolve.
- The log contains no undefined-reference, multiply-defined-label,
  overfull-box, or underfull-box warnings.
- The 27-page PDF was rendered and visually checked at the title page,
  crude root bound, free-depth theorem, linear-depth corollary, global
  endpoint assembly, and dependency audit.
