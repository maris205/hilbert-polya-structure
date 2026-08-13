# HCS-C44 — Hénon \(\mu_3\) Fixed-Coefficient-Field Obstruction

This project closes the first arithmetic descent gate left open by HCS-C43.
For every prime \(p\equiv1\pmod 3\), the conjugate-paired first chronological
Hénon moment generates the full maximal real cyclotomic field

\[
\mathbf Q(B_{p,1})=\mathbf Q(\zeta_p)^+,
\qquad
[\mathbf Q(B_{p,1}):\mathbf Q]=\frac{p-1}{2}.
\]

The result is an all-prime theorem, not a finite scan.  Since these degrees are
unbounded, the paired moments cannot be Frobenius traces of any compatible
system over one fixed number field that realizes these exact moments.  This
rejects the most natural self-dual arithmetic repair of the C43 Euler germ
before any rank, conductor, or functional-equation hypothesis is invoked.

## Main theorem

Let \(\rho\in\mathbf F_p\) have order three, put \(c=1+\rho\), and define

\[
f_p(x,y)=2x^3+2y^3+cxy,
\qquad
H_p(r)=\#\{f_p=r\}+\#\{f_p=-r\}.
\]

The paired C43 moment is

\[
B_{p,1}=\frac{2}{p}\sum_{r\in\mathbf F_p}H_p(r)\zeta_p^r.
\]

Its Galois stabilizer is exactly \(\{\pm1\}\).  The proof uses two explicit
finite-field power moments of \(H_p\), rather than computing a minimal
polynomial separately at every prime.

## Route-A decision

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_ANALYTIC\_DETERMINANT},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_REJECTED_FIXED_COEFFICIENT_FIELD`.

The conjugate-paired Euler germ and finite-place quantization are inherited
exactly from C43, but the new arithmetic theorem obstructs their promotion to
a fixed-field global object.  Route B is not authorized.

## Successor

Prime-dependent coefficient fields do not repair the compatible-system
claim.  The next canonical alternatives are Galois-invariant descents; trace
and norm are the two minimal tests, not an exhaustive classification.  The
first additive descent already collapses exactly:

\[
\operatorname{Tr}_{\mathbf Q(\zeta_p)^+/\mathbf Q}B_{p,1}=-6.
\]

HCS-C45 therefore tests the multiplicative norm of the full chronological
local determinant and asks whether rational descent produces a bounded local
object or a growing divisor obstruction.

## Reproduce

From this directory:

~~~bash
./code/run_c44.sh
~~~

The released runner regenerates the certificate in isolation, performs an
independent exact replay, runs fail-closed mutation tests, and verifies the
artifact manifest.
