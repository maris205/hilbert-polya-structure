# Theorem package: planar Kepler conics, collision, and configuration regularization

## Theorem (all-parameter statement)

Let \(\mu>0\), \(q\in\mathbb R^2\setminus\{0\}\), and \(p\in\mathbb R^2\).  Set

\[
 H(q,p)=\frac{|p|^2}{2}-\frac{\mu}{r},\qquad r=|q|,
\]

and let \(\Phi_t\) be the Hamiltonian flow.  Write

\[
 E=H,\qquad L=q_1p_2-q_2p_1,
\qquad A=(|p|^2-\mu/r)q-(q\!\cdot\!p)p.
\]

Then, along every collision-free trajectory,

\[
 \dot q=p,\qquad \dot p=-\mu q/r^3,
\]

and \(E,L,A\) are constant.  The Runge–Lenz identities are

\[
 A\!\cdot q=L^2-\mu r,
 \qquad |A|^2=\mu^2+2EL^2. \tag{1}
\]

If \(L\ne0\), choose polar angle \(\theta\) from the direction of \(A\) (with the circular case \(A=0\) understood by continuity), put \(e=|A|/\mu\), and obtain

\[
 r(\theta)=\frac{L^2/\mu}{1+e\cos\theta}. \tag{2}
\]

Thus \(E<0\) gives an ellipse (including a circle), \(E=0\) a parabola, and \(E>0\) a hyperbola.  For \(E<0\),

\[
 P(E)=2\pi\mu(-2E)^{-3/2},\qquad
 J_r=\frac1{2\pi}\oint p_r\,dr
 =\frac1\pi\int_{r_-}^{r_+}p_r\,dr
 =\frac{\mu}{\sqrt{-2E}}-|L|, \tag{3}
\]

where \(p_r^2=2(E+\mu/r)-L^2/r^2\) and \(r_\pm=a(1\pm e)\), \(a=-\mu/(2E)\).  For \(E>0\) and \(L\ne0\), the unsigned hyperbolic deflection is

\[
 \chi=2\arcsin(1/e). \tag{4}
\]

For \(L=0\), the inward radial branch satisfies

\[
 t_{\rm coll}(r_0)=\int_0^{r_0}\frac{dr}{\sqrt{2(E+\mu/r)}}<\infty
\]

whenever the branch is physically admissible.  Since \(r=0\) is removed from phase space, the physical flow is incomplete.  In particular, with \(\alpha=-E>0\), the bound apocentre formula is

\[
 t_{\rm coll}=\frac{\mu}{\sqrt2\,\alpha^{3/2}}
 \bigl(u-\sin u\cos u\bigr),\quad
 u=\arcsin\sqrt{\alpha r_0/\mu},
\]

while the parabolic and positive-energy formulas are respectively

\[
 \frac{2r_0^{3/2}}{3\sqrt{2\mu}},\qquad
 \frac{\mu}{\sqrt2 E^{3/2}}\bigl(\sinh u\cosh u-u\bigr),\quad
 u=\operatorname{arsinh}\sqrt{Er_0/\mu}. \tag{5}
\]

Identify the plane with \(\mathbb C\), write \(q=u^2\), and change time by \(dt=|u|^2d\tau\).  On a fixed energy level the Levi–Civita equations reduce to

\[
 u''=\frac E2u,\qquad
 2|u'|^2-E|u|^2=\mu,\qquad
 L=2\operatorname{Im}(\bar u u'). \tag{6}
\]

Equation (6) is smooth through \(u=0\), and therefore gives a configuration-level continuation of a collision.  It does not assert a global symplectomorphism, a full Ligon–Schaaf reconstruction, or a three-dimensional regularization statement.

Finally, for each \(E<0\), every collision-free Kepler orbit has period \(P(E)\).  Hence a time-\(T\) map has the positive-dimensional fixed set \(\{H=E,L\ne0\}\) whenever

\[
 T=mP(E),\qquad m\in\mathbb N, \tag{7}
\]

so ordinary isolated primitive-orbit Artin–Mazur counting is not defined on these resonant shells.  For \(E\ge0\), noncollision trajectories are nonperiodic (parabolic/hyperbolic escape).

## Proof ledger

Hamilton's equations give the first line.  Differentiating \(L=q\wedge p\) and \(A\), or using the central-force identity, gives constancy.  Taking scalar products and norms of \(A\) yields (1); solving the first identity in polar coordinates gives (2).  The sign of \(E\) is equivalent to \(e^2-1=2EL^2/\mu^2\), which proves the conic trichotomy.

For \(E<0\), the radial polynomial has roots \(r_\pm\).  The eccentric-anomaly substitution gives Kepler's period in (3).  Separating radial and angular motion and evaluating the same substitution gives the action in (3); differentiating it gives \(\partial_EJ_r=P(E)/(2\pi)\).  The asymptotic directions of (2) satisfy \(\cos\theta_\infty=-1/e\), yielding (4).

For \(L=0\), the radial energy equation is \(\dot r^2=2(E+\mu/r)\); the substitutions \(r=(\mu/\alpha)\sin^2u\), \(r=(\mu/E)\sinh^2u\), and the direct parabolic integral give (5), proving finite collision time and incompleteness.  Substitution of \(q=u^2\) and the stated time change into the complex equation gives (6); the constraint is the transformed energy equation.  Kepler's period depends only on \(E\), proving (7) and the fixed-set boundary.

## Evidence map

`results/c216_kepler_evidence.json` stores 10 orbit rows, 4 radial rows, 12 Levi–Civita rows, and 5 fixed-set rows.  The checker independently verifies 260 assertions; SymPy verifies 17 identities.  These rows are regression tests only.  They do not turn the finite ledger into a proof of the quantified theorem.
