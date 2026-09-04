# Proof Package — HCS-C354

## Claim

Fix \(A,C,\gamma>0\). In regular \(z\)-\(y\)-\(z\) Euler coordinates
\((\phi,\theta,\psi)\), put \(u=\cos\theta\), and let \(L=p_\phi\) and
\(G=p_\psi\). The Lagrange top has Hamiltonian

$$
H={p_\theta^2\over2A}+{(L-Gu)^2\over2A(1-u^2)}
  +{G^2\over2C}+\gamma u. \tag{1}
$$

Its flow on \(T^*SO(3)\) is complete. On every nonsteady trajectory contained
in \(-1<u<1\),

$$
A^2\dot u^2=P(u):=2A\left(E-{G^2\over2C}-\gamma u\right)(1-u^2)
 -(L-Gu)^2. \tag{2}
$$

A finite-period regular nutation exists exactly on a positive component of
\(P\) bounded by two simple roots in \((-1,1)\). In the generic
pole-incompatible chamber \(L\ne\pm G\), the roots can be labelled

$$-1<r_1<r_2<1<r_3,\qquad
P(u)=2A\gamma(u-r_1)(u-r_2)(u-r_3).$$

Writing

$$
d=r_2-r_1,\quad R=r_3-r_1,\quad k^2={d\over R},\quad
\nu^2={\gamma R\over2A},\quad Q=\sqrt{2A\gamma R},
$$

the inclination and its least state-return period are

$$
u(t)=r_1+d\,\operatorname{sn}^2(\nu(t-t_0),k),\qquad
T={4A\over Q}K(k). \tag{3}
$$

Define

$$
I_N={2\over Q(1-r_1)}
 \Pi\!\left({d\over1-r_1},k\right),\qquad
I_S={2\over Q(1+r_1)}
 \Pi\!\left(-{d\over1+r_1},k\right). \tag{4}
$$

The two phase increments in one nutation are

$$
\Delta\phi=(L-G)I_N+(L+G)I_S, \tag{5}
$$

$$
\Delta\psi=G\left({1\over C}-{1\over A}\right)T
 +(G-L)I_N+(G+L)I_S. \tag{6}
$$

The full regular \(SO(3)\) trajectory is closed if and only if

$$ {\Delta\phi\over2\pi}\in\mathbb Q,\qquad
   {\Delta\psi\over2\pi}\in\mathbb Q. \tag{7}$$

If the reduced fractions have denominators \(q_\phi,q_\psi\), the least number
of nutations returning the full state is \(\operatorname{lcm}(q_\phi,q_\psi)\).
The convention excludes accidental lower return by requiring \(T\) to be the
least return time of \((u,\dot u)\).

At an interior double root, the constant solution is steady precession and a
nonconstant solution approaching that root is a separatrix of infinite time.
The pole conditions are \(L=G\) at \(u=1\) and \(L=-G\) at \(u=-1\); pole
motions are interpreted on \(SO(3)\), not by dividing by \(1-u^2\). The
\(\gamma=0\), \(A=C\), \(G=0\), sleeping and triple-root cases are separate
boundaries. The natural compact quantum Hamiltonian is self-adjoint with
compact resolvent, but no closed spectrum is asserted.

## Status

PROVABLE AS STATED.

## Assumptions

- \(A,C,\gamma>0\) in the cubic theorem.
- Equations (3)--(7) are stated first in the generic chamber \(L\ne\pm G\).
  Pole-compatible limits are boundary statements.
- The closure iff is restricted to a trajectory with \(-1<u(t)<1\) for all
  \(t\), two simple turning roots, and the regular Euler chart.
- \(K\) and \(\Pi\) are Legendre complete elliptic integrals, with
  \(0<k^2<1\). The characteristics in (4) are below one, so the displayed
  real integrals are finite.
- Statements at poles and repeated roots use their separately declared
  coordinates and do not substitute singular Euler rates.

## Notation

The configuration is
\(R=R_z(\phi)R_y(\theta)R_z(\psi)\). The first circle is spatial rotation
about the vertical; the second is body rotation about the symmetry axis.
Thus \(L\) and \(G\) are distinct momentum-map components.

## Proof Strategy

Use coercive energy for completeness, Routh reduction for (2), one-dimensional
energy topology for the root chambers, a direct Jacobi substitution for (3),
partial fractions for (5)--(6), and uniqueness of regular Euler coordinates
for (7). Degenerate roots and poles are taken before any division by a
vanishing factor.

## Dependency Map

1. Completeness depends on compactness of \(SO(3)\) and kinetic coercivity.
2. Root exhaustiveness depends on (2) and the endpoint squares.
3. Elliptic inversion depends only on the ordered three-root factorization.
4. Reconstruction depends on Hamilton's equations and two partial fractions.
5. Full closure depends on the least return of \((u,\dot u)\) and regular Euler
   coordinate uniqueness.
6. Boundary claims depend on local orders of zeros of \(P\), not on finite
   evidence.

## Proof

### Step 1: completeness and momenta

The Lagrangian kinetic metric determined by \(A,A,C>0\) is positive definite.
The potential \(\gamma u\) is bounded on compact \(SO(3)\). Therefore every
energy sublevel in \(T^*SO(3)\) has bounded momentum and compact base, hence is
compact. A maximal Hamiltonian integral curve stays in its compact energy
level. Smooth-ODE continuation extends it for every real time.

The Hamiltonian is invariant under the spatial-vertical and body-axis circle
actions. Hamilton's equations give \(\dot p_\phi=\dot p_\psi=0\), so write their
values as \(L,G\).

### Step 2: reduced equation and endpoint ownership

Since \(p_\theta=A\dot\theta\) and
\(\dot u=-\sin\theta\,\dot\theta\), multiplying \(H=E\) by
\(2A(1-u^2)\) gives (2). Expanding its endpoint values before division yields

$$P(1)=-(L-G)^2,\qquad P(-1)=-(L+G)^2. \tag{8}$$

Thus a regular trajectory can approach the north or south pole only under the
stated momentum compatibility.

On \((-1,1)\), allowed reduced positions are exactly \(P\ge0\). A nonsteady
bounded component has turning endpoints at zeros of \(P\). If both are simple,
the time integral behaves as \(\int_0^\epsilon s^{-1/2}ds\) and is finite. If an
endpoint is double, it behaves as \(\int_0^\epsilon s^{-1}ds\) and diverges.
This proves the finite-period iff.

In the generic pole-incompatible chamber, (8) is strict at both endpoints of
\([-1,1]\). Since
the leading coefficient of \(P\) is \(2A\gamma>0\), the sign pattern of a cubic
with two simple roots \(r_1<r_2\) enclosing a positive component forces the
third root to satisfy \(r_3>1\). This gives the announced ordering.

### Step 3: Jacobi inversion

Set \(z=(u-r_1)/d\). On the allowed component,

$$P=2A\gamma d^2R\,z(1-z)(1-k^2z).$$

If \(z=\operatorname{sn}^2(\nu(t-t_0),k)\), then

$$\dot z^2=4\nu^2z(1-z)(1-k^2z).$$

Substitution into \(A^2d^2\dot z^2=P\) gives
\(\nu^2=\gamma R/(2A)\). The least period of \(\operatorname{sn}^2\) is
\(2K(k)\), producing (3). This coefficient identity is also checked exactly
in the symbolic lane.

### Step 4: reconstruction quadratures

Hamilton's equations give

$$\dot\phi={L-Gu\over A(1-u^2)},\qquad
\dot\psi={G\over C}-u\dot\phi. \tag{9}$$

During a half-nutation \(dt=A\,du/\sqrt{P(u)}\). The identities

$$
{L-Gu\over1-u^2}={L-G\over2(1-u)}+{L+G\over2(1+u)},
$$

$$
\dot\psi={G\over C}-{G\over A}
 +{G-Lu\over A(1-u^2)},\qquad
{G-Lu\over1-u^2}={G-L\over2(1-u)}+{G+L\over2(1+u)}
$$

reduce the full out-and-back phase integrals to \(I_N,I_S\). With
\(u=r_1+d\sin^2\chi\), direct substitution gives (4), and the coefficients give
(5)--(6).

### Step 5: full \(SO(3)\) closure

After one least nutation, \((u,\dot u)\) returns and the two cyclic coordinates
advance by the same constants \(\Delta\phi,\Delta\psi\). Hence (7) is sufficient:
after the least common denominator number of nutations both rotations advance
by integer multiples of \(2\pi\).

For necessity, suppose the full phase state returns. Its reduced pair must
return, so the return time is an integer multiple \(nT\). For
\(0<\theta<\pi\), the decomposition
\(R_z(\phi)R_y(\theta)R_z(\psi)\) is unique modulo independent \(2\pi\) changes
of \(\phi,\psi\). Therefore \(n\Delta\phi,n\Delta\psi\in2\pi\mathbb Z\), proving
(7) and the least-denominator statement.

### Step 6: degenerations

If \(P(u_0)=P'(u_0)=0\) and the initial reduced velocity vanishes, uniqueness
for the regular reduced Hamiltonian system keeps \(u=u_0\); (9) then gives two
constant angular velocities. Its regular configuration closes exactly when
their ratio is rational, with the cases of one or both rates zero interpreted
directly. A nonconstant branch approaching the same double root has the
logarithmically divergent time integral from Step 2. A triple root is a further
critical degeneration and is not inserted into (3).

At \(u=\pm1\), (8) supplies the necessary momentum compatibility, but Euler
angles cease to be coordinates. The original smooth Hamiltonian vector field
on \(T^*SO(3)\) supplies existence and uniqueness there. Sleeping solutions are
relative equilibria on that smooth chart. If \(L=G\) but a selected oscillation
still has two interior simple turning roots, the same regular formulas have the
finite limiting root \(r_3=1\); any branch that actually reaches the pole is
excluded from (7) and reconstructed in a group chart. When \(\gamma=0\), \(P\) is at most
quadratic and the motion is the free symmetric-top boundary. Setting \(A=C\)
enhances the kinetic symmetry; setting \(G=0\) removes axial spin. Neither
operation licenses use of a singular pole formula.

### Step 7: natural quantization boundary

The positive rigid-body metric defines a symmetric positive elliptic kinetic
operator on \(C^\infty(SO(3))\).  On the closed manifold \(SO(3)\), the
standard elliptic completeness theorem makes this operator essentially
self-adjoint.  Adding bounded real multiplication by \(\gamma u\) preserves
essential self-adjointness.  Its unique closure equals the Friedrichs
operator, and elliptic compactness gives compact resolvent.  This establishes
only a natural source quantization. No formula for its spectrum and no target
spectral identification follows.

Therefore every part of the claim follows. \(\square\)

## Corrections or Missing Assumptions

The closure theorem is deliberately not extended through Euler poles. Such
motions require group reconstruction in a different chart and are retained as
a boundary rather than hidden in divergent third-kind integrals.

## Open Risks

- A future singular-fiber classification may refine the pole and critical-root
  topology; it is outside this theorem.
- The source-normalized phases must not be identified with arithmetic clocks.
