# Proof Package: precise rejection mechanisms

## Claim

1. For $k=\overline{\mathbb F}_2$, the rational map
   $f_2(x)=x+x^{-2}$ on $\mathbb P^1(k)$ is a separable Lattès map.
   Consequently its geometric Artin–Mazur zeta lies within the existing
   dynamically affine theory, and it does not qualify as a new non-affine
   contract in this lane.
2. Derivative one does not force all nonzero geometric fixed points of
   $f_1^{\circ n}$, for $f_1=x+x^6$ over $\mathbb F_3$, to have displacement
   multiplicity three. The first exhibited failure is a true period-four
   factor of multiplicity six, with an independent period-five failure.
3. The fixed finite critical portrait of $f_3=x^3+x^2$ over $\mathbb F_2$
   does not confine all multiple-root defects to fixed points and their
   repetition towers. True period-five and period-seven factors occur.

## Status

PROVABLE AS STATED for claims 1–3, with claims 2–3 supported by the explicitly
bounded polynomial identities and their executable exact verifier.

The requested all-period count/rationality theorem for $f_1$ or $f_3$ is
**NOT CURRENTLY JUSTIFIED**. These finite counterexamples do not establish
any global analytic type and are not being promoted to a paper contract.

## Assumptions and notation

$\mathbb F_p$ denotes the field of $p$ elements and $\overline{\mathbb F}_p$
its algebraic closure. $f^{\circ n}$ denotes $n$ compositions. Multiplicity
always means the local order of the fixed-point displacement, whereas
$N_n$ counts distinct geometric roots. For $f_2$, the poles and infinity
are part of the projective dynamical domain, not deleted physical points.

## Strategy and dependency map

1. Construct an elliptic-curve lift of $f_2$ by a direct function-field
   identity. Extend it to the smooth projective curve, verify that it fixes
   the origin, and compute its degree using the quotient coordinate.
2. Invoke the named elliptic-curve fact that a morphism of elliptic curves
   preserving their origins is a group homomorphism. Its nonconstant,
   degree-three form is an isogeny; the degree is prime to the characteristic,
   so it is separable.
3. Use square-free polynomial divisibility and proper-divisor coprimality
   to certify the primitive-period witnesses for $f_1$ and $f_3$.
4. Separate a failure of the proposed proof route from a proof of a global
   impossibility or a zeta analytic classification.

## Proof

### Step 1. An explicit elliptic lift

Let $E$ be the smooth projective completion of

$$E:\quad y^2+y=x^3,$$

with origin $O$ at infinity. The affine model is nonsingular since its
partial derivative with respect to $y$ is one. Its homogeneous cubic has
the unique point $O=[0:1:0]$ at infinity, also nonsingular. Thus it is an
elliptic curve.

Choose $\alpha\in\mathbb F_4$ satisfying $\alpha^2+\alpha=1$ and set

$$X=x+x^{-2},\qquad Y=y+x^{-3}+\alpha.$$

In its function field, characteristic two gives

$$Y^2+Y=x^3+x^{-6}+x^{-3}+1
=(x+x^{-2})^3=X^3.$$

Therefore $(X,Y)$ defines a nonconstant rational map $\psi:E\dashrightarrow
E$. A rational map from a smooth projective curve to a projective curve
extends over each missing point: the source local ring is a discrete
valuation ring and the target is proper, so the valuative criterion of
properness applies. Hence $\psi$ is a morphism on all of $E$.

At $O$, the functions $x$ and $y$ have pole orders two and three,
respectively. The summands $x^{-2}$ and $x^{-3}$ vanish there, so $X$ has
a pole and $\psi(O)=O$ (the only point at which the target $x$-coordinate
has a pole). The stated origin-preserving morphism theorem makes $\psi$
a group endomorphism.

### Step 2. Degree and quotient

Let $\pi:E\to\mathbb P^1$ be the $x$-coordinate. Its degree is two and
it is separable, since $y$ satisfies $y^2+y=x^3$. The elliptic involution
$P\mapsto-P$ sends $(x,y)$ to $(x,y+1)$, so $\pi$ is the quotient by
$\Gamma=\{1,[-1]\}$, including in characteristic two.

By construction,

$$\pi\circ\psi=f_2\circ\pi.$$

The rational map $f_2=(x^3+1)/x^2$ has coprime numerator and denominator,
so its degree is three. Degree multiplicativity gives

$$2\deg\psi=\deg(\pi\circ\psi)
=\deg(f_2\circ\pi)=3\cdot2.$$

Thus $\deg\psi=3$. A nonconstant elliptic group endomorphism is surjective
with finite kernel. Its inseparable degree is a power of two dividing three,
so it is separable. These data satisfy the Lattès/dynamically affine
definition. The point $x=0$ is sent to infinity by $f_2$, and infinity is
fixed; this matches the projective convention in the exact probe.

This proof identifies an excluded classical mechanism. It does not claim
priority for this isogeny formula. Bridy's Theorem 1.2 gives the all-period
zeta transcendence of separable Lattès maps; Byszewski–Cornelissen–Houben's
Theorem A provides the broader non-holonomicity framework. Reapplying those
theorems to the displayed lift would not fill a new non-affine seat.

### Step 3. Why derivative one is not the missing theorem

For any perfect field of characteristic $p$ and polynomial
$f=x+g(x)^p$, telescoping yields the exact identity

$$f^{\circ n}(x)-x
=\sum_{j=0}^{n-1}g(f^{\circ j}(x))^p
=H_n(x)^p,\qquad
H_n=\sum_{j=0}^{n-1}g(f^{\circ j}(x)).$$

Since $(f^{\circ j})'=1$, differentiation gives

$$H_n'(x)=\sum_{j=0}^{n-1}g'(f^{\circ j}(x)).$$

The first identity forces displacement multiplicity at least $p$, but it
does not imply $H_n$ is square-free. For $f_1=x+x^6$ one has $g=x^2$,
$H_n=\sum(f_1^{\circ j})^2$ and $H_n'=2\sum f_1^{\circ j}$.
The simultaneous vanishing of these two orbit sums is a new global
condition; no nonvanishing theorem has been proved here.

The exact witnesses in `EXACT_EVIDENCE.md` satisfy

$$Q_4^6\mid f_1^{\circ4}-x,\qquad
\gcd\left(Q_4,(f_1^{\circ4}-x)/Q_4^6\right)=1,$$

and $Q_4$ is square-free and coprime to both proper-divisor displacement
polynomials. Thus every root of $Q_4$ has exact period four and exact
displacement multiplicity six. The same test for $Q_5$ gives exact period
five and multiplicity six. This refutes correction-by-the-origin alone.

For example, at $n=4$ the incorrect ansatz “origin has multiplicity six,
all other roots multiplicity three” would give

$$1+(6^4-6)/3=431,$$

whereas the exact geometric count is $411$. The twenty additional
multiplicity-six nonzero roots account for the difference. At $n=5$ the
same ansatz predicts $2591$, versus the exact count $2571$.

### Step 4. Why the fixed critical portrait is insufficient

For $f_3=x^3+x^2$, one has $f_3'=x^2$, so zero is the only finite
critical point and it is fixed. Infinity is fixed too. Nevertheless the
displayed square-free factors $R_5$ and $R_7$ have exact multiplicities
three and two in their respective displacements. Their coprimality to
$f_3-x$ and the primality of five and seven prove that their roots have
those exact periods. None belongs to a fixed-point repetition tower.

The period-three repeated factor is $x^2+x+1$, whose roots are fixed
points of $f_3$; their multipliers have order three. Treating this as a
primitive three-cycle would be an error. The period-five and period-seven
witnesses explicitly avoid that error.

More generally, every separable rational map defined over a finite field is
postcritically finite over its algebraic closure: its finitely many
critical points lie in one finite extension, and the map acts on the
finite projective line over that extension. Thus a PCF label alone adds
no all-period rigidity in this setting. A specific short portrait can
still be useful, but this example shows that the fixed portrait does
not eliminate multiplier resonances on unrelated cycles.

## Corrections and missing assumptions

The retained mathematical statements are the explicit Lattès reduction and
finite counterexamples, not an all-period theorem for a new object.
For either $f_1$ or $f_3$, a genuine survivor would need a theorem controlling
all primitive cycles' multiplicities, their repetitions, and the summed
effect on $N_n$ and $Z_f$. No such theorem is supplied by these checks.

## Open risks

- There is no process-separated review of this note yet.
- Finite witnesses rule out the stated simple ansätze, not every possible
  finite-state/global method.
- No inference of zeta irrationality or transcendence is made for $f_1$ or
  $f_3$. Search failure is not a certificate that their analytic types are
  globally open or novel.
- This lane has zero retained paper-level contracts and no target A2/A3
  increment.
