# HCS-C34 results

## Main theorem

Let \(L\) be the \(S_9\) splitting field of the C33 period-five Maxwell
collision polynomial, and let \(\beta_1,\ldots,\beta_9\) be the conjugates
of the intrinsic two-branch Hill product. Then

\[
\dim_{\mathbb F_2}\langle[\beta_1],\ldots,[\beta_9]\rangle=9.
\]

Therefore

\[
\operatorname{Gal}\left(
L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})/\mathbb Q
\right)
=C_2\wr S_9
\]

with exact order \(185794560\).

## Small exact certificate

The translated \(19\)-adic coefficient valuations are

\[
v_{19}(P_9(1802+T))=(5,3,0,0,0,0,0,0,0,0)
\]

and

\[
v_{19}(\operatorname{num}\beta(1802+T))
=(3,0,0,0,0,0,0,0,0).
\]

The Newton edge of slope \(-5/2\) isolates two roots, on which the
integer-normalized Hill valuation equals \(5\). The other seven conjugates
are units. This produces parity row \(e_1+e_2\); its full \(S_9\)-orbit
forces any square relation into the all-ones line.

The last relation fails because

\[
[N_{K/\mathbb Q}(\beta)]
=3\cdot13\cdot19\cdot41\cdot59
\]

while

\[
[\operatorname{Disc}(P_9)]
=13\cdot19\cdot41\cdot59.
\]

## Independent finite controls

The degree-eighteen polynomial

\[
F_{18}(U)=N_{K/\mathbb Q}(U^2-\beta)
\]

is independently proved irreducible modulo \(7\). A complete orbit-span
census over all \(512\) vectors in \(\mathbb F_2^9\) is

\[
\{0:1,\ 1:1,\ 8:255,\ 9:255\}.
\]

These are controls; the full-rank proof is the local valuation plus global
square-class argument.

## Route-A outcome

This is a positive, exact, fixed-period arithmetic theorem. It does not
construct an all-period dynamical zeta, prime law, analytic continuation, or
self-adjoint operator. The tuple is

\[
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{FORMAL\_HINT})
\]

and the decision is `ROUTE_A_REJECTED` with Route B unauthorized.
