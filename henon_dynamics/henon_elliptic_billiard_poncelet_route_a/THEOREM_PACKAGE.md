# Proof package

## Claim

For `0<f<e<1`, define the confocal ellipses

\[
 E(\varepsilon)=\left\{(x,y):\varepsilon^2x^2+
 \frac{\varepsilon^2}{1-\varepsilon^2}y^2=1\right\}.
\]

Let `B_e^f` be the positive-orientation Poncelet/billiard map on the outer
ellipse `E(f)` whose chords are tangent to `E(e)`.  With Jacobi modulus `e`,

\[
 \pi_e^f(\theta)=\frac1f\left(-\operatorname{sn}(4K(e)\theta,e),
 \sqrt{1-f^2}\operatorname{cn}(4K(e)\theta,e)\right)
\]

is a period-one covering and

\[
 B_e^f\circ\pi_e^f=\pi_e^f\circ R_{\rho(e,f)},\qquad
 R_\rho(\theta)=\theta+\rho,
\]

where

\[
 \rho(e,f)=\frac{F(\omega(e,f),e)}{2K(e)},\qquad
 \omega(e,f)=\arcsin\sqrt{\frac{e^2-f^2}{e^2(1-f^2)}}.
\]

On the open triangle, `partial_e rho>0` and `partial_f rho<0`.  The two
rotation endpoints are `0` and `1/2`:

\[
 \lim_{f\to e^-}\rho=\lim_{e\to f^+}\rho=0,
 \qquad
 \lim_{f\to0^+}\rho=\lim_{e\to1^-}\rho=\frac12.
\]

If `rho=p/q` in lowest terms, every point on this invariant curve has minimal
period `q`.  The restricted `q`-th return is the identity and its tangent
derivative is one.  The periodic points form a one-parameter family, so an
ordinary isolated-orbit Euler product is not defined by this rational caustic.
No ambient Jordan or unipotent conclusion is part of the claim.

## Status

**PROVABLE AS STATED** in the positive-orientation elliptic-caustic sector.

## Assumptions

- The common foci are `(+-1,0)` and eccentricity is the numerical
  eccentricity in the displayed normalization.
- `F(phi,e)` uses Jacobi modulus `e`, not parameter `e^2`; software calls use
  parameter `m=e^2` explicitly.
- The clock is one billiard reflection and orientation is fixed positive.
- Hyperbolic caustics are excluded.

## Notation

- `K(e)=F(pi/2,e)`.
- `sn`, `cn`, `dn`, `am`, and `cd=cn/dn` are Jacobi functions with modulus
  `e`.
- Circle coordinates are read modulo one.

## Proof strategy

Use the explicit Jacobi covering to turn the restricted billiard map into a
translation.  Use the inverse formula `f=e cd(2K(e)rho,e)` for strict
derivative signs.  Rational-translation arithmetic then proves the complete
porism and clean-family statement.

## Dependency map

1. Covering and chord tangency imply the rigid-rotation formula.
2. The inverse formula plus two signed Jacobi derivatives implies strict
   parameter monotonicity.
3. The formula and one logarithmic elliptic-integral estimate imply all four
   boundary paths.
4. Coprimality of `p,q` implies common minimal period `q`.
5. The translation model implies the identity restricted return and the A2
   obstruction.

## Proof

### 1. Covering and rotation

Put `u=4K(e)theta`.  The identity `sn^2(u,e)+cn^2(u,e)=1` shows directly that
`pi_e^f(theta)` lies on `E(f)`.  Period `4K(e)` of `sn` and `cn` makes the deck
group `theta -> theta+1`.

Let `v=2F(omega,e)`.  The Jacobi addition formulas for `sn(u+v,e)` and
`cn(u+v,e)`, together with

\[
 \sin^2\omega=\frac{e^2-f^2}{e^2(1-f^2)},
\]

show that the line through `pi_e^f(theta)` and
`pi_e^f(theta+v/(4K(e)))` satisfies the dual tangency equation

\[
 C^2=\frac{A^2}{e^2}+\frac{1-e^2}{e^2}B^2
\]

for a line `Ax+By+C=0`.  Hence it is tangent to `E(e)`.  Positive orientation
selects the next intersection, so
`B_e^f pi_e^f(theta)=pi_e^f(theta+v/(4K(e)))`.  Since
`v/(4K(e))=F(omega,e)/(2K(e))`, the claimed conjugacy and rotation formula
follow.  This is also the confocal covering theorem of Lomelí–Meiss, whose
hypotheses are exactly `0<f<e<1`.

### 2. Strict monotonicity

For `0<ell<1/2`, inversion of the formula gives

\[
 f=R(\ell,e):=e\operatorname{cd}(2K(e)\ell,e).
\]

Set `u=2K(e)ell`.  Differentiating the Jacobi functions gives

\[
 R_\ell=-\frac{2e(1-e^2)K(e)\operatorname{sn}(u,e)}
 {\operatorname{dn}^2(u,e)}<0.
\]

Writing `mathcal E(u,e)=int_0^u dn^2(t,e)dt`, the other derivative is

\[
 R_e=\operatorname{cd}(u,e)+
 \frac{\operatorname{sn}(u,e)}{\operatorname{dn}^2(u,e)}
 [\mathcal E(u,e)-2\ell\mathcal E(K(e),e)].
\]

On `(0,K(e))`, `dn^2` is strictly decreasing.  Therefore its average on
`[0,u]` exceeds its average on `[0,K(e)]`, so the bracket is positive.  Every
other factor is positive and hence `R_e>0`.  Implicit differentiation of
`f=R(rho,e)` now yields

\[
 \rho_f=1/R_\ell<0,\qquad \rho_e=-R_e/R_\ell>0.
\]

### 3. Endpoints

When `f->e-` or `e->f+`, `omega->0`, so `F(omega,e)->0` and `rho->0`.
For fixed `e`, `f->0+` gives `omega->pi/2`, hence `F->K` and `rho->1/2`.

For fixed `f` and `e->1-`, put `e'=sqrt(1-e^2)`.  Then
`cos(omega)=O(e')`.  Moreover,

\[
 0\le K(e)-F(\omega,e)
 =\int_\omega^{\pi/2}\frac{dt}{\sqrt{1-e^2\sin^2t}}=O(1),
\]

after the substitution `x=cos(t)`, while `K(e)~log(4/e')->infinity`.
Thus `F(omega,e)/K(e)->1`, proving the remaining half-rotation endpoint.

### 4. Rational porisms and least period

If `rho=p/q` with `gcd(p,q)=1`, then
`R_rho^q(theta)=theta+p`, which is the same circle point.  If a smaller
positive `k<q` returned, then `kp/q` would be an integer, forcing `q|k`, a
contradiction.  Every starting `theta` therefore has minimal period `q`.
Changing `theta` continuously changes the inscribed polygon while retaining
the same caustic, which is the Poncelet porism.

### 5. Restricted derivative and Route-A obstruction

On the invariant circle, the `q`-th lift is `theta -> theta+p`; its derivative
is exactly one and its quotient map is the identity.  Hence the fixed set is
the full circle rather than isolated points.  An ordinary product indexed by
isolated primitive orbits, or a nondegenerate isolated-fixed-point denominator,
cannot be extracted from this rational caustic.  This tangent computation says
nothing about the transverse derivative or ambient Jordan form.

Let `Omega_f` be the smooth bounded interior of `E(f)`.  The standard ambient
Dirichlet quantum billiard is `-Delta_D` on `L^2(Omega_f)`, with

\[
 \mathcal D(-\Delta_D)=H^2(\Omega_f)\cap H_0^1(\Omega_f).
\]

It is self-adjoint and has compact resolvent.  Its unitary group
`U(t)=exp(-it(-Delta_D))` uses continuous physical flight time, and complex
conjugation `C` is antiunitary with `C U(t) C=U(-t)`.  This is a coherent
ambient quantization, but it does not pass the evaluator's same-clock and
orbit-data gates: the frozen owner is the one-reflection Poincaré map, no
same-clock quantum return has been constructed, and no theorem shows that a
quantum return preserves the phases and weights of the fixed-caustic orbits.
Consequently the strict classification is `A4_FORMAL_HINT`, not
`A4_NATURAL_QUANTIZATION`.  No same-object target spectral identification
follows.

## Corrections or missing assumptions

- The theorem is restricted to elliptic caustics.  A full hyperbolic-caustic
  atlas would be a different theorem.
- “Unit derivative” means the derivative of the restricted circle return.
  Ambient unipotence was deliberately removed from the claim.
- The Dirichlet Laplacian is an ambient formal hint only; a same-clock quantum
  Poincaré return and a fixed-caustic phase/weight bridge remain unproved.

## Open risks

None inside the frozen sector.  Extending the determinant discussion to a
Morse–Bott or Berry–Tabor regularization would require a new convention and is
not part of this package.
