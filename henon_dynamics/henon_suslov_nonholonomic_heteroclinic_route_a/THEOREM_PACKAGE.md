# Theorem package

## Frozen body and constraint

Let the attitude be `Q in SO(3)`, let body angular velocity satisfy
`omega_3=0`, and, after an allowed in-plane rotation, write

```text
I = [[I1,0,a],[0,I2,b],[a,b,I3]],
I1,I2>0,  I3>a^2/I1+b^2/I2.
```

The Euler–Poincaré–Suslov equation is
`I omega_dot=(I omega) cross omega+lambda e3`, with physical time retained.

## Complete theorem

Put `ell=a omega1+b omega2` and
`H=(I1 omega1^2+I2 omega2^2)/2`.  Then

```text
I1 omega1_dot=-ell omega2,
I2 omega2_dot= ell omega1,
H_dot=0.
```

Let `u=sqrt(I1)omega1`, `v=sqrt(I2)omega2`, `R=sqrt(2H)`, and

```text
q^2=a^2/I1+b^2/I2,
cos(delta)=a/[sqrt(I1)q],
sin(delta)=b/[sqrt(I2)q],
kappa=Rq/sqrt(I1 I2).
```

If `q>0` and `H>0`, writing `(u,v)=R(cos phi,sin phi)` gives
`phi_dot=kappa cos(phi-delta)`.  Each energy ellipse contains the two
antipodal permanent rotations `ell=0`.  Its two complementary arcs are

```text
sin(phi-delta)=tanh(kappa(t-t0)),
cos(phi-delta)=sigma sech(kappa(t-t0)), sigma in {+1,-1}.
```

Both are complete heteroclinics from the same reduced-unstable endpoint to
the same reduced-stable endpoint; the nonzero exponents are `+kappa` and
`-kappa`.  The scaled ellipse angle changes by `pi`, independently of energy.

Every reduced permanent rotation has constant body angular velocity.  Its
full reconstruction is

```text
Q(t)=Q0 exp(t hat(omega)).
```

For `omega!=0` this is periodic with primitive attitude period
`2 pi/|omega|`.  For fixed `omega`, distinct circles are parameterized by the
right-coset space `SO(3)/SO(2)`, a clean two-dimensional family; varying
energy gives a continuum.  Thus the generic full system does possess periodic
rotations, but they are not isolated primitive objects.

The reduced Poisson bracket is

```text
{omega1,omega2}=-ell/(I1 I2).
```

On each open half-plane `ell>0` or `ell<0`, the density
`domega1 domega2/|ell|` is invariant.  It is singular on `ell=0`.
At a nonzero endpoint the vector-field divergence is nonzero, so the invariant
density equation forbids a positive `C^1` density extending across it.
The involution `(Q,omega)->(Q,-omega)` reverses the full flow.

If `a=b=0`, the reduced vector field vanishes identically: every nonzero state
reconstructs as a clean periodic rotation.  If only one of `a,b` vanishes,
the generic atlas remains valid.  At `H=0`, `omega=0` and `Q` is fixed.  Schur
equality makes the inertia singular and is excluded.

## Proof and evidence boundary

The first two components of `(I omega) cross omega` give the reduced equations;
their scalar product with `(omega1,omega2)` proves energy conservation.
The scaled equations are `u_dot=-ell v/sqrt(I1 I2)` and
`v_dot=ell u/sqrt(I1 I2)`, hence the scalar angle equation.  Direct
differentiation of the hyperbolic formulas proves both branches and their
limits.  Constant angular velocity integrates the attitude equation by the
matrix exponential.  The bracket generates the reduced vector field, and
division by `ell` leaves a divergence-free linear rotation field on each
half-plane.  The reversor follows because the reduced quadratic field is even.

Sixteen rational receipts check normalizations, not the continuous theorem.
The singular bracket is not a target quantization.  Therefore

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```
