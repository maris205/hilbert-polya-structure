# Theorem package

Let
\[
 \Delta=\{(x,y,z)\in\mathbb R^3:x,y,z\ge0, x+y+z=1\}
\]
and let \(F_{a,\mu}\) be
\[
 \dot x=ax(y-z)+\mu(1/3-x),\quad
 \dot y=ay(z-x)+\mu(1/3-y),\quad
 \dot z=az(x-y)+\mu(1/3-z).
\]

## Theorem 1 — simplex and conservative atlas

For every \(a,\mu\ge0\), \(\Delta\) is forward invariant because
\(\dot x+\dot y+\dot z=0\).  If \(\mu>0\), a zero coordinate has derivative
\(\mu/3>0\), so a boundary trajectory enters the interior immediately.  If
\(\mu=0\), each coordinate face is invariant.  On the interior,
\[
 \frac{d}{dt}\log(xyz)=a[(y-z)+(z-x)+(x-y)]=0,
\]
so \(H=xyz\) is a first integral.  When \(a>0\), the barycenter is the unique
interior equilibrium.  For every \(0<h<1/27\), the regular level \(xyz=h\)
is a single simple closed curve carrying one periodic orbit; the limit
\(h\downarrow0\) is the three-edge cyclic heteroclinic network.  When \(a=0\)
as well as \(\mu=0\), the vector field vanishes instead, as recorded in
Theorem 4.

For \(a>0\), obtain the period by fixing \(x\).  Then \(y+z=1-x\),
\(yz=h/x\), and
\[
 (y-z)^2=(1-x)^2-4h/x.
\]
The two physical turning roots \(x_-<1/3<x_+\) solve
\(x(1-x)^2=4h\).  Traversing both signs of \(y-z\) gives
\[
 T(h)=\frac2a\int_{x_-}^{x_+}
 \frac{dx}{x\sqrt{(1-x)^2-4h/x}}. \tag{1}
\]
The third cubic root is \(x_3=2-x_--x_+>1\).  With
\(x=(x_-+x_+)/2+(x_+-x_-)sin\theta/2\), the endpoint factor cancels and
\[
 T(h)=\frac2a\int_{-\pi/2}^{\pi/2}
 \frac{d\theta}{\sqrt{x(\theta)(x_3-x(\theta))}}. \tag{2}
\]
This is the deterministic representation used in the receipt.

## Theorem 2 — center and boundary limits

For \(a>0\), as \(h\uparrow1/27\), the roots coalesce at \(1/3\), and (2)
converges to
\[
 \lim_{h\uparrow1/27}T(h)=\frac{2\pi\sqrt3}{a}.
\]
As \(h\downarrow0\), the lower root tends to zero and the integral diverges;
this is the slowing near the boundary heteroclinic network.  These are
physical-time statements, not a discrete zeta or a prime-power repetition
law.

## Theorem 3 — uniform mutation

For \(\mu>0\), every positive-time state is interior.  On the interior,
\[
 \frac{d}{dt}\log(xyz)=\frac\mu3\left(\frac1x+\frac1y+\frac1z-9\right)\ge0, \tag{3}
\]
because \(x+y+z=1\) and the reciprocal AM–HM inequality gives
\(1/x+1/y+1/z\ge9\).  Equality holds only at the barycenter.  Compactness of
\(\Delta\), continuity of \(H\), and LaSalle's invariance principle therefore
give \((x(t),y(t),z(t))\to(1/3,1/3,1/3)\) for every initial state.  There is no
nonconstant recurrent trajectory on this face.

At the barycenter the full Jacobian has characteristic polynomial
\[
 (\lambda+\mu)\left((\lambda+\mu)^2+\frac{a^2}{3}\right).
\]
The tangent eigenvalues are \(-\mu\pm ia/\sqrt3\), while the normal direction
has eigenvalue \(-\mu\) in the ambient coordinates.

## Theorem 4 — degenerate faces

If \(a=0\), each coordinate solves
\[
 x_i(t)=\frac13+\bigl(x_i(0)-\tfrac13\bigr)e^{-\mu t}.
\]
If \(a=\mu=0\), the vector field vanishes and every point of \(\Delta\) is
fixed.  If \(\mu=0,a>0\), boundary points remain on their invariant edges and
the interior product levels above apply.  No statement is made for a general
nonuniform mutation matrix or a stochastic perturbation.

## Route-A boundary

The model has no intrinsic arithmetic origin, no prime-power clock, no
primitive-orbit Euler product, and no target determinant.  The exact ODE
theorems are retained as a mathematically meaningful source-local result, but
the evaluator tuple is
\[
(\mathtt{A0\_FAIL},\mathtt{A1\_WEAK},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),
\]
with `ROUTE_A_REJECTED` and Route B disabled.
