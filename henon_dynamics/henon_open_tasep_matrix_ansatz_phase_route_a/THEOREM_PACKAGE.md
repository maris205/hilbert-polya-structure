# HCS-C220 theorem package — open TASEP matrix-Ansatz phase atlas

## 1. Finite generator

For \(\eta=(\eta_1,\ldots,\eta_L)\in\{0,1\}^L\), let
\(\eta^{1+}\) fill site one, \(\eta^{L-}\) empty the last site, and
\(\eta^{i,i+1}\) move a particle from \(i\) to \(i+1\).  The row generator is
\[
\begin{aligned}
(\mathcal Lf)(\eta)={}&\alpha(1-\eta_1)
 [f(\eta^{1+})-f(\eta)]\\
&+\sum_{i=1}^{L-1}\eta_i(1-\eta_{i+1})
 [f(\eta^{i,i+1})-f(\eta)]\\
&+\beta\eta_L[f(\eta^{L-})-f(\eta)].
\end{aligned}
\]
For \(L=0\) this is the one-state zero generator.  If
\(\alpha,\beta>0\), every finite chain is irreducible and hence has a unique
stationary law.

## 2. DEHP stationary law

Let \(D,E\) obey the quadratic relation \(DE=D+E\), and let boundary vectors
satisfy
\[
\langle W|E=\alpha^{-1}\langle W|,\qquad
D|V\rangle=\beta^{-1}|V\rangle .
\]
Writing \(D\) for an occupied site and \(E\) for an empty site, define
\[
w(\eta)=\langle W|\prod_{i=1}^{L}
[\eta_iD+(1-\eta_i)E]|V\rangle,\quad
Z_L=\sum_{\eta}w(\eta).
\]
The local relation and the three generator moves give
\(\pi(\eta)=w(\eta)/Z_L\) and equal current through every bond.

The words are finite, so \(w(\eta)\) can be evaluated without choosing an
infinite matrix representation: strip a left \(E\), a right \(D\), or replace
the first \(DE\) by \(D+E\).  This is an exact algebraic realization of the
matrix Ansatz, not a numerical approximation.

## 3. Closed normalization and current

With \(x=\beta^{-1}\), \(y=\alpha^{-1}\), the finite normalization is
\[
Z_0=1,\qquad
Z_N=\sum_{p=1}^{N}
\frac{p(2N-1-p)!}{N!(N-p)!}\,
\frac{x^{p+1}-y^{p+1}}{x-y}\quad(N\ge1).
\]
The displayed quotient is a divided difference.  At \(x=y\)
(equivalently \(\alpha=\beta\)) it is \((p+1)x^p\), the continuous
equal-rate limit.  Consequently, for \(L\ge1\),
\[
J_L=\frac{Z_{L-1}}{Z_L};
\]
the injection, all bulk, and extraction currents computed from \(\pi\) equal
this value.  In particular \(J_1=\alpha\beta/(\alpha+\beta)\).

## 4. Thermodynamic atlas

For the normalized bulk rate, the analytic \(L\to\infty\) phase law is
\[
J=\begin{cases}
\alpha(1-\alpha),&\alpha<\min(\beta,\tfrac12)\quad(\mathrm{LD}),\\
\beta(1-\beta),&\beta<\min(\alpha,\tfrac12)\quad(\mathrm{HD}),\\
\tfrac14,&\alpha>\tfrac12,\ \beta>\tfrac12\quad(\mathrm{MC}).
\end{cases}
\]
The line \(0<\alpha=\beta<1/2\) is coexistence/shock in the positive-rate
interior, with the same current and no single selected bulk density.  Its
endpoint \((\alpha,\beta)=(0,0)\) is excluded from coexistence and is handled
by the zero-rate boundary theorem below.  The faces
\(\alpha=1/2,\beta>1/2\) and \(\beta=1/2,\alpha>1/2\) are critical and retain
their finite-size corrections; their intersection is the multicritical
corner \(\alpha=\beta=1/2\).  These are analytic source theorems; the finite
ledger only checks their formulas at sentinels.

## 5. Zero-rate and small-size boundaries

If \(\alpha=0,\beta>0\), the empty state is the unique closed class.  If
\(\beta=0,\alpha>0\), the full state is the unique closed class.  If
\(\alpha=\beta=0\), particle number is conserved and the right-packed state
\(0^{L-k}1^k\) is absorbing for each \(k=0,\ldots,L\).  There are L+1
absorbing extreme points.  The normalized stationary set is the simplex on
these absorbers, of affine dimension L (the unnormalized linear nullspace has
one basis direction per absorber).  At L=0 there is one state and affine
dimension zero.

## 6. Route-A boundary

The exact finite non-equilibrium theorem is source-local.  The strict tuple is
\[
(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).
\]
The matrix Ansatz is a formal non-self-adjoint algebraic hint only; no target
divisor, arithmetic local datum, Euler factor, root number, automorphy claim,
or Hilbert--Polya operator is made.
