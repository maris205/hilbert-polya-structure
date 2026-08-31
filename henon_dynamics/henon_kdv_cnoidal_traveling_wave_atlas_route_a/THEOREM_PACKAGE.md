# Theorem package

## Frozen equation and first integral

Let `u` be a real classical solution of

\[
u_t+6uu_x+u_{xxx}=0
\]

of traveling form `u(x,t)=U(x-ct)`, where `U` is bounded and defined on all
of `R`.  Two integrations give

\[
U''=cU-3U^2+A,
\qquad
(U')^2=-2U^3+cU^2+2AU+B.                 \tag{1}
\]

If the cubic has three real roots `r1<=r2<=r3`, write it as

\[
(U')^2=2(r_3-U)(U-r_2)(U-r_1).           \tag{2}
\]

Coefficient comparison yields

\[
c=2(r_1+r_2+r_3),\quad
A=-(r_1r_2+r_1r_3+r_2r_3),\quad
B=2r_1r_2r_3.                            \tag{3}
\]

## Root-complete bounded-profile theorem

A nonconstant bounded entire profile exists precisely in either of the
following cases.

1. If `r1<r2<r3`, it oscillates on `[r2,r3]` and, up to translation of `xi`,

   \[
   U(\xi)=r_2+(r_3-r_2)\operatorname{cn}^2(k\xi;m),
   \quad
   k=\sqrt{\frac{r_3-r_1}{2}},\quad
   m=\frac{r_3-r_2}{r_3-r_1}.             \tag{4}
   \]

2. If `r1=r2<r3`, the compact allowed interval becomes a homoclinic and

   \[
   U(\xi)=r_1+(r_3-r_1)
   \operatorname{sech}^2\!\left(\sqrt{\frac{r_3-r_1}{2}}\,\xi\right). \tag{5}
   \]

All other bounded entire profiles are constants.  Indeed, the leading
coefficient in (1) is negative.  Three simple roots give exactly one compact
positive interval, `[r2,r3]`; a lower double root gives the homoclinic compact
closure.  An upper double root, a triple root, or a cubic with only one real
root has no nonconstant compact allowed interval.  Separation of variables
also shows that the simple endpoints reflect in finite time, whereas the
lower double root is approached only at infinite time.  This exhausts the
root topologies.

To check (4) algebraically, put `q=cn^2(k xi;m)`.  Then

\[
q_\xi^2=4k^2q(1-q)(1-m+mq),
\]

which converts exactly to (2).  Differentiating the identity gives the
profile ODE in (1).  Formula (5) follows either from the same calculation or
from `cn(s;1)=sech(s)`.

## Period and moments

The fundamental spatial period is

\[
L=\frac{2K(m)}k
 =2\sqrt{\frac2{r_3-r_1}}K(m),             \tag{6}
\]

because `cn^2` has period `2K`, not `4K`.  Its mean is

\[
\langle U\rangle=r_1+(r_3-r_1)\frac{E(m)}{K(m)}.       \tag{7}
\]

For a second exact moment, define

\[
C_2=\frac{E-(1-m)K}{mK},\qquad
C_4=1-\frac{2(K-E)}{mK}
 +\frac{(2+m)K-2(1+m)E}{3m^2K}.
\]

Then

\[
\langle U^2\rangle=r_2^2+2r_2(r_3-r_2)C_2
 +(r_3-r_2)^2C_4.                         \tag{8}
\]

These formulas follow from the standard complete integrals of `sn^2` and
`sn^4`; the checker independently reconstructs them by a regularized root
quadrature.

## Degenerations, covariance, and clock

As `r2` decreases to `r1`, (4) tends to (5); its excess mass over the
background is `2 sqrt(2(r3-r1))`.  As `r2` increases to `r3` with `r1` fixed,
the amplitude vanishes and

\[
L\longrightarrow \frac{2\pi}{\sqrt{2(r_3-r_1)}}.
\]

The limiting constant profile itself does not select a traveling speed.

For every real `a`,

\[
u_a(x,t)=u(x-6at,t)+a
\]

again solves the frozen plus-sign equation.  It shifts every root by `a` and
the speed by `6a`, leaving `m`, amplitude, and `L` unchanged.  On the circle
of fundamental length `L`, a wave with `c!=0` is a periodic PDE orbit of
primitive physical-time period `L/|c|`; `c=0` is stationary.

## Scope and Route A

This theorem classifies bounded traveling profiles only.  It does not
classify arbitrary KdV solutions or assert spectral, orbital, or nonlinear
stability.  The source periods depend continuously on the roots and provide
no rational-prime carrier or logarithmic arithmetic clock.  The auxiliary
KdV Lax operator is retained only as a formal candidate-local hint.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
