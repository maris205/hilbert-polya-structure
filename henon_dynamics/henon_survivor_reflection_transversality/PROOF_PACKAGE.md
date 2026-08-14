# Proof package

## 1. Geometry

Let

\[
H(q,p)=(1-6q^2-p,q),\quad R(q,p)=(p,q),\quad J=RH.
\]

Then `R` and `J` are involutions and `H=RJ`.  Parameterize `Fix(J)` by

\[
\gamma(X)=\left(X,\frac{1-6X^2}{2}\right).
\]

For odd `n=2m+1`, define `ell(q,p)=q-p`.  The mixed closure is exactly

\[
F_n(X)=\ell\!\left(H^{m+1}\gamma(X)\right)
      =q_{m+1}(X)-q_m(X).
\]

Therefore

\[
F_n'(X)=(1,-1)DH^{m+1}(\gamma(X))\gamma'(X).
\]

## 2. Tangency forces a neutral multiplier

Set

\[
K_m=H^{-(m+1)}RH^{m+1}.
\]

This is an involution.  At a closure root `X`, the point `z=gamma(X)` lies on
both `Fix(J)` and `Fix(K_m)`.  Direct use of `R H^k R=H^{-k}` gives

\[
J K_m=H^{2m+1}=H^n.
\]

If `F_n'(X)=0`, the image of `gamma'(X)` is tangent to `Fix(R)`.
Consequently `gamma'(X)` is tangent to `Fix(K_m)`.  It is already tangent to
`Fix(J)`, so

\[
DJ(z)\gamma'(X)=DK_m(z)\gamma'(X)=\gamma'(X).
\]

Differentiating `H^n=J K_m` yields

\[
DH^n(z)\gamma'(X)=\gamma'(X).
\]

Thus tangency implies the multiplier `+1`.

## 3. Physical transversality

The frozen H6 survivor is uniformly hyperbolic.  Every periodic monodromy on
it has a stable and an unstable multiplier with moduli respectively below and
above one.  The multiplier `+1` is impossible.  Hence every odd mixed-axis
closure root in the survivor satisfies `F_n'(X) != 0`.

This invokes hyperbolicity only for roots already known to lie in the
certified survivor.  It says nothing about ambient algebraic roots.

## 4. Exact physical incidence

The four state labels are the sign pairs `--,-+,+-,++`.  Coordinate swap
fixes the first/fourth and exchanges the middle two, exactly P59's
`rho=(0)(1 2)(3)`.  Applying a reversor to the unique signed-square-root
orbit therefore produces the unique orbit with the reversed `rho` itinerary;
the conjugacy is symmetry equivariant.  At odd period all reflection axes
are rotationally conjugate, and a primitive necklace has no two stabilizing
reflections.
Therefore every primitive reversible necklace has exactly one representative
on the chosen `Fix(J)` axis.  Since `X` parameterizes that axis injectively,
the number of distinct primitive physical roots is

\[
P_n=R_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2}.
\]

A primitive physical root is not a root of any proper-divisor closure.  Its
multiplicity in `F_n` is one by transversality, so its coefficient in the
formal P60 divisor is exactly `+1`.

## 5. Entropy comparison

P59 and P60 give

\[
P_n=\Theta(\varphi^{n/2}),\qquad
D_n=2^{(n+1)/2}+O(n2^{n/6+1/2}).
\]

Along odd periods,

\[
\frac{P_n}{D_n}=\Theta\!\left((\varphi/2)^{n/2}\right).
\]

The formal residual degree `D_n-P_n` has entropy `(1/2)log 2`; this is a
degree statement, not a count of distinct ambient roots.

## 6. Finite exact certificate

For odd `n<=11`, the primary checker reconstructs the primitive quotient,
isolates every root by a disjoint rational interval of width below `10^-40`,
and propagates each interval through the recurrence.  A root is certified in
the survivor band precisely when every coordinate interval lies strictly in

\[
\sqrt{17}/12<|q_j|<\sqrt{3/8}.
\]

Interval Horner evaluation excludes zero from `F_n'` on every physical
isolator.  The physical counts are `1,1,2,4,6,12`, exactly matching an
independent Cartesian symbolic enumeration.

## 7. Boundary

P61 proves all-period physical transversality and local effectivity.  It does
not prove that every ambient closure is reduced, that the formal divisor is
globally effective, or that residual degree is a root count.  It also proves
no Galois-height pressure, rational-prime trace or Hilbert--Pólya operator.
