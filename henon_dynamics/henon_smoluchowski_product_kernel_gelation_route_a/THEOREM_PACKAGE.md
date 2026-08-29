# Product-kernel coagulation theorem package

## Frozen equations

For \(k\ge1\), let

\[
\dot c_k=\frac12\sum_{i+j=k}ijc_ic_j-kc_kM_1(t),\qquad
M_q=\sum_{k\ge1}k^q c_k,                              \tag{1}
\]

with \(c_1(0)=1\) and \(c_k(0)=0\) for \(k>1\).  This is the
Smoluchowski/Stockmayer loss convention.  The Flory convention replaces the
postgel loss mass \(M_1(t)\) by the initial total mass \(M_1(0)=1\), thereby
allowing finite clusters to react with the gel.

## Exact pregel theorem

Let

\[
T(u)=\sum_{k\ge1}\frac{k^{k-1}}{k!}u^k,qquad
U(u)=\sum_{k\ge1}\frac{k^{k-2}}{k!}u^k.
\]

Then \(T=ue^T\), \(U=T-T^2/2\), and for \(0\le t\le1\),

\[
c_k(t)=\frac{k^{k-2}}{k!}t^{k-1}e^{-kt}.              \tag{2}
\]

Indeed, the coefficients \(a_k=k^{k-2}/k!\) obey

\[
(k-1)a_k=\frac12\sum_{i+j=k}ij a_i a_j,               \tag{3}
\]

so (2) satisfies (1) while \(M_1=1\).  For \(u=tze^{-t}\),

\[
G(z,t)=\sum k c_kz^k=\frac{T(u)}t,qquad
C(z,t)=\sum c_kz^k=\frac{U(u)}t,                       \tag{4}
\]

as formal power series in \(z\), and analytically on the principal convergence
disk (in particular for \(0\le z\le1\)); the \(t=0\) values are continuous
limits.  Since the physical branch has
\(T(te^{-t})=t\) for \(t\le1\),

\[
M_0=1-\frac t2,\quad M_1=1,\quad
M_2=\frac1{1-t},\quad M_3=\frac1{(1-t)^3}.             \tag{5}
\]

The last two formulas hold for \(t<1\).  At \(t=1\), Stirling's formula gives

\[
c_k(1)\sim(2\pi)^{-1/2}k^{-5/2},                      \tag{6}
\]

so \(M_2\) diverges.  For fixed \(0<t<1\),

\[
c_k(t)\sim\frac{k^{-5/2}}{\sqrt{2\pi}\,t}
[t e^{1-t}]^k.                                        \tag{7}
\]

Thus \(t_g=1\) is the exact gel point.

## Two postgel closures

One explicit postgel solution of (1), often called the Stockmayer
continuation, is

\[
c_k^{\rm S}(t)=\frac{k^{k-2}}{k!}\frac{e^{-k}}t,qquad t\ge1. \tag{8}
\]

It has \(M_0=1/(2t)\), \(M_1=1/t\), and \(M_2=\infty\).  Equation (3)
gives gain \((k-1)c_k^{\rm S}/t\); loss is
\(kc_k^{\rm S}/t\); their difference equals
\(\dot c_k^{\rm S}=-c_k^{\rm S}/t\).

The gel-reactive Flory equation instead admits

\[
c_k^{\rm F}(t)=\frac{k^{k-2}}{k!}t^{k-1}e^{-kt}.       \tag{9}
\]

For \(t>1\), let

\[
r=-W_0(-te^{-t})\in(0,1),\qquad q=r/t.
\]

Then \(q=e^{-t(1-q)}\) is the finite-cluster mass and

\[
M_0=q-\frac t2q^2,\quad M_1=q,\quad
M_2=\frac q{1-r},\quad M_3=\frac q{(1-r)^3}.           \tag{10}
\]

Here gain is \((k-1)c_k^{\rm F}/t\), but the gel-reactive loss is
\(kc_k^{\rm F}\), exactly matching the derivative of (9).  Formulas (8) and
(9) coincide at \(t=1\) and immediately diverge afterward because they solve
different equations.  The package verifies both displayed solutions; it does
not assert uniqueness among every weak postgel solution.

## Route-A verdict

The locked tuple is
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`, overall
`ROUTE_A_REJECTED`, with `route_b_invocation_allowed=false`.  Tree functions
and cluster labels remain source-native analytic/combinatorial objects, not
arithmetic primitives, a target determinant, a target divisor or a natural
unitary spectral bridge.
