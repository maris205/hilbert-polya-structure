# Theorem package

Let `rho>0`, `R0>0`, and `Pi in R`.  On the positive-radius half-plane define

\[
 R\ddot R+\frac32\dot R^2=-\frac{\Pi}{\rho},
 \qquad R(0)=R_0,\quad \dot R(0)=0. \tag{1}
\]

For the physical three-dimensional radial-flow normalization, the Lagrangian
and energy are

\[
 L=2\pi\rho R^3\dot R^2-\frac{4\pi}{3}\Pi R^3,
 \qquad E=2\pi\rho R^3\dot R^2+\frac{4\pi}{3}\Pi R^3.
 \tag{2}
\]

## Main theorem (all pressure signs)

Every positive-radius solution of (1) obeys the exact first integral

\[
 R^3\dot R^2+\frac{2\Pi}{3\rho}R^3
 =\frac{2\Pi}{3\rho}R_0^3. \tag{3}
\]

If `Pi>0`, put `a=sqrt(2 Pi/(3 rho))`.  The unique forward branch is strictly
decreasing on `[0,Tc)`, where

\[
 \dot R=-a\sqrt{(R_0/R)^3-1},\qquad
 T_c=\frac{R_0}{a}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx
 =\frac{R_0}{3a}B\!\left(\frac56,\frac12\right). \tag{4}
\]

Numerically,
`Tc=0.914681356501962... R0 sqrt(rho/Pi)`.  For `delta=Tc-t`,

\[
 R(t)=C\,\delta^{2/5}\bigl(1+O(\delta^{6/5})\bigr),\quad
 C=R_0^{3/5}(5a/2)^{2/5}, \tag{5}
\]

and therefore

\[
 \dot R(t)=-\frac25C\delta^{-3/5}(1+O(\delta^{6/5})),\qquad
 \ddot R(t)=-\frac6{25}C\delta^{-8/5}(1+O(\delta^{6/5})). \tag{6}
\]

The dimensionless radius is determined exactly by an inverse incomplete-Beta
relation.  This is source-local explicit solvability only: the source Beta
clock is not target continuation/divisor/counting law and is not an A3
analytic-structure match.  In particular, if `x=R/R0`, then
\[
 \frac{at}{R_0}=\int_x^1\frac{u^{3/2}}{\sqrt{1-u^3}}du,
\]
and the endpoint expansion is
\[
 \int_0^x\frac{u^{3/2}}{\sqrt{1-u^3}}du
 =\frac25x^{5/2}+\frac1{11}x^{11/2}+O(x^{17/2}). \tag{7}
\]

If `Pi=0`, the rest solution is the global equilibrium `R(t)=R0`.  If
`Pi<0`, put `a=sqrt(2|Pi|/(3 rho))`; the unique forward branch is strictly
increasing and satisfies
\[
 \frac{at}{R_0}=\int_1^{R/R_0}\frac{u^{3/2}}{\sqrt{u^3-1}}du,
 \qquad R(t)\sim at\quad(t\to\infty). \tag{8}
\]

For the collapse sign, the liquid kinetic, pressure-potential, and total
energy pieces are
\[
 K=2\pi\rho R^3\dot R^2=\frac{4\pi}{3}\Pi(R_0^3-R^3),\quad
 U=\frac{4\pi}{3}\Pi R^3,\quad E=\frac{4\pi}{3}\Pi R_0^3. \tag{9}
\]
With `V=(4 pi/3)R^3`, (5) gives
`V~(4 pi/3)C^3 delta^(6/5)` and `V_dot=O(delta^(1/5))`.  The endpoint
integrability thresholds are
\[
 \dot R\in L^p(T_c-\varepsilon,T_c)\iff p<\frac53,qquad
 \ddot R\in L^p(T_c-\varepsilon,T_c)\iff p<\frac58. \tag{10}
\]

The face `R0=0` is not a positive-radius classical initial state.  An
absorbing value `R=0` may be adjoined for bookkeeping, but it is not a
continuation theorem for (1).

## Proof ledger

Multiplying (1) by `2 R^2 dot R` gives the derivative of (3).  Separation of
the monotone branch gives (4) and (8); the substitution `y=x^3` gives the
Beta parameters `(5/6,1/2)`.  Expanding `(1-x^3)^(-1/2)` proves (7), and
inverting its leading term gives (5)--(6).  The same exponents give (10).
The Euler--Lagrange residual of (2) is
`4 pi rho R^2 [R R_ddot+(3/2)R_dot^2+Pi/rho]`, proving the Lagrangian claim.
Substitution of (3) into (2) proves (9), and the volume statements follow by
one differentiation.  Positivity and strict monotonicity follow from the
chosen square-root branch; the sign-zero and radius-zero faces are handled
separately as stated.

The finite JSON ledger is a regression certificate for these formulas.  It is
not a numerical substitute for the universal quantifiers in the theorem.
