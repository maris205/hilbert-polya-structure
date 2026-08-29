# Lorenz-63 dissipativity and stability theorem package

## Frozen model

Let \(\sigma,\beta>0\), \(\rho\in\mathbb R\), and

\[
\dot x=\sigma(y-x),\quad \dot y=x(\rho-z)-y,\quad
\dot z=xy-\beta z. \tag{1}
\]

The clock is physical continuous time.  The involution
\((x,y,z)\mapsto(-x,-y,z)\) is retained.

## Main theorem

Put \(c=\rho+\sigma\),
\(V=x^2+y^2+(z-c)^2\), and
\(\kappa=\min\{2\sigma,2,\beta\}\).  Every solution of (1) is global
forward and

\[
\dot V=-2\sigma x^2-2y^2-\beta z^2-\beta(z-c)^2+\beta c^2
       \le -\kappa V+\beta c^2. \tag{2}
\]

Consequently

\[
V(t)\le e^{-\kappa t}V(0)+\frac{\beta c^2}{\kappa}
(1-e^{-\kappa t}), \tag{3}
\]

and every sublevel \(V\le R\) with
\(R>\beta c^2/\kappa\) is an absorbing ellipsoid.  Polynomial local
existence plus (3) excludes finite-time escape.

The origin exists for every \(\rho\), with

\[
\chi_O(\ell)=(\ell+\beta)
[\ell^2+(\sigma+1)\ell+\sigma(1-\rho)]. \tag{4}
\]

It is asymptotically stable for \(\rho<1\), nonhyperbolic at \(\rho=1\),
and a saddle for \(\rho>1\).  Exactly when \(\rho>1\), symmetry creates

\[
E_\pm=(\pm\sqrt{\beta(\rho-1)},
       \pm\sqrt{\beta(\rho-1)},\rho-1), \tag{5}
\]

and both have

\[
\chi_E(\ell)=\ell^3+(\sigma+\beta+1)\ell^2
+\beta(\sigma+\rho)\ell+2\sigma\beta(\rho-1). \tag{6}
\]

The only nontrivial cubic Hurwitz margin is

\[
D=\sigma(\sigma+\beta+3)+(\beta+1-\sigma)\rho. \tag{7}
\]

If \(\sigma\le\beta+1\), the wings are stable for every \(\rho>1\).  If
\(\sigma>\beta+1\), put

\[
\rho_H=\frac{\sigma(\sigma+\beta+3)}{\sigma-\beta-1}>1. \tag{8}
\]

The wings are stable for \(1<\rho<\rho_H\), lie on a linear Hopf boundary
at \(\rho_H\), and are unstable for \(\rho>\rho_H\).  At equality,

\[
\chi_E=(\ell+\sigma+\beta+1)
[\ell^2+\beta(\sigma+\rho_H)]. \tag{9}
\]

Thus the imaginary pair is exactly
\(\ell=\pm i\sqrt{\beta(\sigma+\rho_H)}\).  Equation (9) is a linear
spectral statement; nonlinear Hopf direction is outside this package.

## Degenerate faces

- If \(\sigma=0,\beta>0\), \(x=s\) is conserved and the equilibrium curve is
  \(E_s=(s,\beta\rho s/(\beta+s^2),\rho s^2/(\beta+s^2))\).  Its tangent
  root is zero and the transverse factor is
  \(\ell^2+(1+\beta)\ell+\beta+s^2\).
- If \(\beta=0,\sigma>0\), the equilibria are \((0,0,z_0)\), with a zero
  tangent root and transverse factor
  \(\ell^2+(\sigma+1)\ell+\sigma(1-\rho+z_0)\).
- If \(\sigma=\beta=0\), the equilibrium set is the union of the lines
  \((0,0,z)\) and \((x,0,\rho)\).

These faces do not inherit the positive-parameter absorbing theorem.

## Route-A verdict

The locked tuple is
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`, with
`overall=ROUTE_A_REJECTED` and
`route_b_invocation_allowed=false`.  The source supplies neither a rational-
prime owner nor a complete primitive-orbit ledger, a target determinant,
target analytic structure, or a natural unitary lift.
