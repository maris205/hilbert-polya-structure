# Theorem package: complete Hénon isochrone action–frequency atlas

## Claim

**Status: PROVABLE_AS_STATED.** Fix \(\mu,b>0\), put \(\ell=|L|\), and define

\[
A=\sqrt{\ell^2+4\mu b},\qquad B=\ell+A.
\]

For the effective radial Hamiltonian

\[
H_\ell=\frac{p_r^2}{2}+U_\ell(r),\qquad
U_\ell(r)=\frac{\ell^2}{2r^2}
-\frac{\mu}{b+\sqrt{b^2+r^2}},
\]

the circular/central minimum is

\[
s_c=\sqrt{b^2+r_c^2}=\frac{B^2}{4\mu},qquad
r_c^2=s_c^2-b^2,qquad
E_c=-\frac{\mu}{2s_c}=-\frac{2\mu^2}{B^2}.
\]

Bound motion exists exactly for \(E_c\leq E<0\).  On that interval, with
\(J_r=\pi^{-1}\int_{r_p}^{r_a}p_r\,dr\),

\[
J_r=\frac{\mu}{\sqrt{-2E}}-\frac B2,qquad
H(J_r,\ell)=-\frac{\mu^2}{2(J_r+B/2)^2},
\]

and therefore

\[
T_r=\frac{2\pi\mu}{(-2E)^{3/2}},\qquad
\Omega_r=\frac{(-2E)^{3/2}}\mu.
\]

For \(L\geq0\) and \(\ell>0\),

\[
\beta:=\frac{\Omega_\phi}{\Omega_r}
=\frac12\left(1+\frac{\ell}{A}\right),qquad
\Delta\phi=2\pi\beta
=\pi\left(1+\frac{\ell}{A}\right).
\]

A noncircular bound orbit with \(\ell>0\) is periodic in phase space if and only if \(\beta\in\mathbb Q\).  If \(\beta=p/q\) in lowest terms, its primitive period is \(qT_r\).

## Assumptions and conventions

- Unit mass and physical Hamiltonian time are used.
- The geometry depends on \(\ell=|L|\).  The displayed positive azimuthal frequency uses \(L\geq0\); for \(L<0\), canonical \(\Omega_\phi\) changes sign.
- At \(\ell=0\), the polar chart is singular but the Cartesian potential is smooth because \(b>0\).  The radial action formula is its continuous half-line limit.
- “Closed” means return of the full phase-space point.  Circular and center-crossing degeneracies are handled separately below.

## Proof dependency map

1. The effective-potential minimum fixes the admissible energy interval and the normalization \(J_r(E_c)=0\).
2. The substitution \(x=b+\sqrt{b^2+r^2}\) turns the radial equation into a quadratic.
3. Vieta identities plus an arcsine integral give \(T_r\).
4. \(\partial_EJ_r=T_r/(2\pi)\) and the circular normalization give \(J_r\).
5. Partial fractions and two root products give the apsidal angle.
6. Two-torus return gives the rational closure criterion.

## Proof

### 1. Circular minimum and allowed energies

Write \(s=\sqrt{b^2+r^2}\geq b\).  Then

\[
U_\ell(s)=-\frac{\mu}{b+s}
+\frac{\ell^2}{2(s^2-b^2)}.
\]

For \(\ell>0\), differentiation gives a unique critical point through

\[
\mu(s-b)^2=\ell^2s.
\]

Its positive solution is \(s=s_c=B^2/(4\mu)\), and substitution yields
\(U_\ell(s_c)=E_c=-\mu/(2s_c)\).  Since \(U_\ell\to+\infty\) at \(r\downarrow0\), \(U_\ell\to0^-\) at infinity, and the critical point is unique, it is the global minimum.  When \(\ell=0\), \(U_0\) increases from \(-\mu/(2b)\) to zero, so the same formulas give the central equilibrium \(s_c=b\) and \(E_c=-\mu/(2b)\).  Hence \(E<E_c\) is forbidden, \(E_c\leq E<0\) is bound, \(E=0\) is marginal escape, and \(E>0\) is unbound.

### 2. Quadratic reduction and period

Set

\[
x=b+s,\qquad r^2=x(x-2b),\qquad
Q(x)=2Ex^2+(2\mu-4bE)x-(4\mu b+\ell^2).
\]

On a noncircular bound segment, \(Q(x)=(-2E)(x_a-x)(x-x_p)\), and direct differentiation of \(r^2=x(x-2b)\) gives

\[
dt=\frac{x-b}{\sqrt{Q(x)}}\,dx.
\]

With \(q=-2E>0\), Vieta's formulas are

\[
x_p+x_a=2b+\frac{2\mu}{q},\qquad
x_px_a=\frac{A^2}{q}.
\]

The standard substitution from \([x_p,x_a]\) to \([0,\pi]\) yields

\[
\int_{x_p}^{x_a}\frac{x-b}{\sqrt{Q(x)}}\,dx
=\frac{\pi\mu}{q^{3/2}}.
\]

Doubling the periapsis-to-apoapsis time proves
\(T_r=2\pi\mu/q^{3/2}\), including the circular value by continuity.

### 3. Radial action

For a one-degree-of-freedom oscillation, differentiation under the action integral gives

\[
\frac{\partial J_r}{\partial E}=\frac{T_r}{2\pi}
=\frac{\mu}{(-2E)^{3/2}}.
\]

Integration in \(E\) gives \(J_r=\mu/\sqrt{-2E}+C(\ell)\).  The collapsed circular cycle has \(J_r(E_c,\ell)=0\); since \(\mu/\sqrt{-2E_c}=B/2\), one obtains \(C=-B/2\).  Inversion gives the asserted action Hamiltonian.  In particular, \(J_r\geq0\) is equivalent to \(E\geq E_c\) inside \(E<0\), so the action domain and energy domain agree exactly.

### 4. Apsidal advance and frequencies

For \(\ell>0\), \(\dot\phi=\ell/r^2\).  The identity

\[
\frac{x-b}{{x(x-2b)}}
=\frac12\left(\frac1x+\frac1{x-2b}\right)
\]

and the shifted root product

\[
(x_p-2b)(x_a-2b)=\frac{\ell^2}{q}
\]

give the periapsis-to-apoapsis angle

\[
\frac{\ell}{2\sqrt q}\left(
\frac{\pi}{\sqrt{x_px_a}}+
\frac{\pi}{\sqrt{(x_p-2b)(x_a-2b)}}
\right)
=\frac\pi2\left(1+\frac\ell A\right).
\]

Doubling proves \(\Delta\phi=\pi(1+\ell/A)\).  Equivalently, differentiating
\(H(J_r,\ell)\) gives

\[
\Omega_r=\partial_{J_r}H,qquad
\Omega_\phi=\partial_\ell H
=\Omega_r\,\frac12\left(1+\frac\ell A\right)
\]

under the \(L\geq0\) convention.

### 5. Closure

For a noncircular bound orbit, the radial phase is nonconstant.  A phase-space return must therefore take an integer number \(q\) of radial cycles.  The azimuth then advances by \(2\pi q\beta\), which is an integer multiple of \(2\pi\) exactly when \(\beta\) is rational.  If \(\beta=p/q\) is reduced, no smaller positive number of radial cycles can return both phases, so the primitive period is \(qT_r\).

## Boundary atlas

- **Circular face \(E=E_c\), \(\ell>0\):** \(J_r=0\).  The orbit is a circle and is closed for every \(\beta\), including irrational \(\beta\); its actual period is \(2\pi/\Omega_\phi\).  Here \(T_r\) is the limiting epicyclic period, so applying the noncircular rationality test would be an error.
- **Central equilibrium \(E=E_c\), \(\ell=0\):** the particle remains at \(r=0\).
- **Center-crossing face \(E_c<E<0\), \(\ell=0\):** the Cartesian trajectory crosses the smooth center.  The half-line radius repeats after \(T_r\), but the velocity direction is reversed; the full Cartesian phase point returns after \(2T_r\).  The one-sided limiting ratio is \(1/2\).
- **Escape face:** as \(E\uparrow0\), both \(J_r\) and \(T_r\) diverge.  Thus \(E=0\) is not part of the finite action chart.
- **Signed angular momentum:** replacing \(L>0\) by \(L<0\) reverses angular orientation; \(\ell\) and the radial geometry remain unchanged.
- **Kepler face:** for fixed \(\ell>0\), \(b\downarrow0\) gives \(J_r\to\mu/\sqrt{-2E}-\ell\) and \(\beta\to1\).  The simultaneous \((b,\ell)\to(0,0)\) corner reaches the Kepler collision singularity and is not a smooth commuting limit.

## Natural quantization and Route-A consequence

The Cartesian potential

\[
V(x)=-\frac{\mu}{b+\sqrt{b^2+|x|^2}}
\]

is real and bounded between \(-\mu/(2b)\) and zero.  Therefore
\(-\hbar^2\Delta/2+V\) is self-adjoint on \(H^2(\mathbb R^2)\) and semibounded by the bounded-perturbation theorem.  This proves only `A4_NATURAL_QUANTIZATION`.  Its spectrum is not analyzed here and it is not identified with any target operator.

Resonant closed orbits exist intrinsically, but occur in continuous energy and rotational families rather than as an isolated primitive ledger.  This supports only `A1_WEAK`.  There is no arithmetic local carrier, determinant, target analytic bridge, or Route-B input, giving the frozen tuple

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.

## Proof risks and controls

1. **Using \(L\) instead of \(|L|\):** controlled by defining \(\ell=|L|\) before the action formula and separating the sign of \(\Omega_\phi\).
2. **Forgetting \(E_c\):** controlled by the effective-potential minimization and the equivalence \(J_r\geq0\iff E\geq E_c\).
3. **Applying the rationality test to a circle:** excluded explicitly because the radial phase is constant.
4. **Calling \(T_r\) the full \(L=0\) Cartesian period:** excluded; the full return is \(2T_r\).
5. **Treating finite cells as proof:** excluded; exact cells and quadratures are regression controls only.
6. **Claiming classical formulas as new:** excluded by the locked source audit.
7. **Upgrading natural quantization to Hilbert–Pólya:** explicitly forbidden by scope and frozen false flags.
