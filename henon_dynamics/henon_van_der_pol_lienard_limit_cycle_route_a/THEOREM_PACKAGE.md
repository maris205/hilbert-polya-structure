# C249 theorem package — Van der Pol/Liénard flow

## Frozen object

The phase space is \(\mathbb R^2\), with physical time \(t\), section
\(\Sigma=\{(x,y):x=0,y>0\}\), and parameter \(\mu\in\mathbb R\):
\[
 \dot x=y,\qquad \dot y=\mu(1-x^2)y-x.
\]
Equivalently, \(x\) solves
\[
 x''+\mu(x^2-1)x'+x=0.
\]
There is no arithmetic origin in this definition.  If a restoring frequency
\(\omega>0\) is inserted, the change \(\tau=\omega t\) reduces the equation
to the same normal form with effective damping \(\mu_0/\omega\).

## Analytic atlas

Set \(f(x)=\mu(x^2-1)\) and
\[
 F(x)=\int_0^x f(s)\,ds=\mu(x^3/3-x).
\]
For \(\mu>0\), \(F\) is negative on \((0,\sqrt3)\), has the unique
positive zero \(\sqrt3\), and is positive and increasing beyond that zero.
The standard Liénard existence/uniqueness hypotheses therefore give one
periodic orbit enclosing the origin.  The orbit is hyperbolic and attracting;
the Poincaré return map on \(\Sigma\) has exactly one fixed point and its
derivative is the transverse multiplier.  No second periodic orbit or
non-equilibrium recurrent component is assigned to the certificate.

For \(\mu<0\), the involution
\((t,x,y)\mapsto(-t,x,-y)\) maps the positive-\(\mu\) flow to the negative
one.  The unique cycle is consequently repelling.  At \(\mu=0\),
\[
 E(x,y)=\tfrac12(x^2+y^2),\qquad \dot E=0,
\]
and every level \(E=c>0\) is a harmonic oval of period \(2\pi\); this is a
continuum boundary, not an isolated cycle.

## Balance and Floquet identities

For all \(\mu\),
\[
 \dot E=\mu(1-x^2)y^2,qquad \operatorname{div}X=\mu(1-x^2).
\]
For a periodic orbit with \(\mu\ne0\), integrating the first identity gives
the exact balance \(\int_0^T(1-x^2)y^2\,dt=0\).  (At the \(\mu=0\) center
this divided balance is not asserted.)  In two dimensions the tangent Floquet
multiplier is one and the transverse multiplier is
\[
 \lambda_\perp=\exp\!\left(\int_0^T\operatorname{div}X\,dt\right)
 =\exp\!\left(\mu\int_0^T(1-x^2)\,dt\right).
\]
The analytic theorem supplies strict attraction/repulsion; the finite receipt
reports the corresponding numerical values for five positive parameters.

## Scope boundary

This is a smooth-flow theorem with a finite numerical regression receipt.  It
does not provide a target prime/zero table, arithmetic local data, Euler
factors, root numbers, automorphy, a target divisor or functional equation, a
zeta/Fredholm determinant, or a Hilbert--Pólya operator.  The Route-A tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and the overall
verdict is `ROUTE_A_REJECTED`.
