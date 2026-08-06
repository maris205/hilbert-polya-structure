# R300 Protocol: Relative Heat-Trace Activity Carrier

**Frozen:** 2026-08-06, before execution  
**Compute:** CPU only, expected below five minutes  
**Forbidden inputs:** prime tables, Riemann-zero ordinates, fitted spectral
parameters, archived R108 eigenvalues

## 1. Fixed object

For fixed \(h>0\), define on \(L^2(\mathbb R^2)\)

\[
H_{a,h}=-\frac{h^2}{2}\Delta+V_a,
\qquad
V_a(q)=2\pi e^{\pi|\Psi_a(q)|^2},
\]

with

\[
\Psi_a(x,y)=(-2ar_ax-ax^2-y,x),
\qquad
r_a=\frac1{1+\sqrt{1+a}},
\qquad
a=\frac{51}{50}.
\]

The control is \(H_{0,h}=-h^2\Delta/2+2\pi e^{\pi|q|^2}\).  The map,
centering, normalization, and parameter are not varied in R300.

## 2. Exact classical cancellation

Since \(\det D\Psi_a=1\),

\[
\int e^{-tV_a(q)}dq
=\int e^{-2\pi t e^{\pi|z|^2}}dz.
\]

Thus the full classical heat integral cancels in the relative trace.  R300
does not numerically retest this change-of-variables identity.

## 3. Frozen analytic carrier

Let

\[
I_a(t)=\int e^{-tV_a}|\nabla V_a|^2dq,
\qquad
\lambda=2\pi t,
\qquad
L=\log\frac1\lambda,
\]

and

\[
A_k(\lambda)=\int_\lambda^\infty
w e^{-w}(L+\log w)^k\,dw.
\]

The identity to be checked by independent quadratures is

\[
\boxed{
I_a(t)-I_0(t)
=\frac{2a^2}{t^2}
\left[A_2(\lambda)+4\pi r_a^2A_1(\lambda)\right].}
\]

The integrated Wigner--Kirkwood carrier for
\(H=-h^2\Delta/2+V\) is

\[
\Theta_a(t)-\Theta_0(t)
=-\frac{t^2}{48\pi}\bigl(I_a-I_0\bigr)
+R_{a,h}(t).
\]

Consequently the *formal carrier*, not yet the full heat-trace theorem, is

\[
Q_a(t)=-\frac{a^2}{24\pi}
\left[A_2(\lambda)+4\pi r_a^2A_1(\lambda)\right].
\]

Its predicted asymptotic polynomial is

\[
Q_a(t)=-\frac{a^2}{24\pi}
\left[L^2+\beta_aL+\kappa_a\right]+o(1),
\]

where

\[
\beta_a=2(1-\gamma)+4\pi r_a^2,
\]

\[
\kappa_a=\frac{\pi^2}{6}-2\gamma+\gamma^2
+4\pi r_a^2(1-\gamma).
\]

## 4. Numerical definitions

The frozen grid is

\[
t\in\{10^{-2},3\cdot10^{-3},10^{-3},3\cdot10^{-4},10^{-4},
3\cdot10^{-5},10^{-5}\}.
\]

Two implementations are required:

1. one-dimensional adaptive quadrature of \(A_1,A_2\) in the variable \(w\);
2. raw polar quadrature of
   \(e^{-tW}|\nabla W|^2\) with the full matrix \(D\Psi_a\), before angular
   cancellation is imposed.

An independent checker must not import the production module and must use
arbitrary precision for the one-dimensional identity.

## 5. Frozen gates

### R300-A: identity gate

- \(I_a-I_0>0\) at every grid point;
- maximum relative discrepancy between the two quadratures
  \(\le10^{-9}\);
- independent-checker discrepancy \(\le10^{-20}\) for its high-precision
  algebraic reconstruction.

### R300-B: coefficient gate

- the stored constants agree with direct high-precision evaluation to
  \(10^{-12}\);
- \(Q_a(t)<0\) on the full grid;
- the exact bracket divided by \(L^2\) approaches one monotonically on the
  last four grid points.  This is a diagnostic, not an inferential p-value.

### R300-C: proof gate

The following are paper-proof obligations and cannot be passed by quadrature:

1. a uniform resummed/Feynman--Kac remainder
   \(R_{a,h}(t)=o(L^2)\), preferably \(O_{a,h}(tL^4)\);
2. all integration-by-parts boundary terms vanish;
3. the trace expansion is valid for the noncompact exponential Hénon
   potential.

R300-C is `OPEN` unless a complete written proof and independent review are
present.  A/B passing does not silently pass C.

## 6. Decision table

| Outcome | Overall status | Allowed statement |
|---|---|---|
| A and B pass, C open | `PARTIAL_PASS` | exact nonzero WK carrier; promote uniform remainder to the next proof task |
| A/B fail | `KILLED_OR_REVISE` | constants/identity invalid; do not use the heat asymptotic |
| A/B/C pass | `PASS` | relative heat-trace asymptotic proves analytic spectral activity |

Independently of C, a separate symmetric-rearrangement proof may establish
\(\lambda_1(H_{a,h})>\lambda_1(H_{0,h})\) for \(a\ne0\).  That theorem is a
proof-review task, not a numerical R300 gate.

## 7. Claim boundary

Even a full R300 pass upgrades only S (and strengthens the relative spectral
container).  It does not produce rational-prime periods, von Mangoldt
amplitudes, an explicit-formula divisor, individual zeta zeros, or RH.

