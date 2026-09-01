# Theorem package

Let `H^1=R^3` carry

`X=d_x-(y/2)d_z`, `Y=d_y+(x/2)d_z`, `[X,Y]=d_z`,

with `X,Y` orthonormal, and let

`H=((p_x-y p_z/2)^2+(p_y+x p_z/2)^2)/2`.

All statements below concern this metric only.

## Main theorem

Put `lambda=p_z`.  Every unit-speed normal geodesic from the identity is,
for some angle `phi`,

```text
lambda=0:  (x,y,z)=(t cos(phi),t sin(phi),0),

lambda!=0:
x=(sin(phi+lambda t)-sin(phi))/lambda,
y=(cos(phi)-cos(phi+lambda t))/lambda,
z=(lambda t-sin(lambda t))/(2 lambda^2).
```

There are no nonconstant abnormal extremals.  For initial horizontal norm `r`,
the exponential-map Jacobian in parameters `(r,phi,lambda)` is

`r^3 t [2-2 cos(s)-s sin(s)]/lambda^4`, `s=lambda t`,

with zero-momentum limit `r^3 t^5/12`.  Its first positive zero along a
nonzero-`lambda` geodesic is `|s|=2*pi`; hence the first conjugate time is

`t_conj=2*pi/|lambda|`.

The first cut time is the same.  The cut locus from the identity, and also its
first conjugate locus, is exactly

`{(0,0,z): z!=0}`.

For `rho=sqrt(x^2+y^2)>0`, there is a unique `theta in (-pi,pi)` satisfying

`4z/rho^2=(theta-sin(theta)cos(theta))/sin(theta)^2`,

with the continuous convention `theta=0` at `z=0`, and

`d(0,(x,y,z))=rho*theta/sin(theta)`.

On the vertical axis,

`d(0,(0,0,z))=2 sqrt(pi |z|)`;

on the horizontal face, `d=rho`.

## Proof closure

Hamilton's equations give constant `lambda` and rotating controls
`h1=cos(phi+lambda t)`, `h2=sin(phi+lambda t)`, which integrate to the displayed
flow.  An abnormal covector must annihilate `X`, `Y`, and their bracket, hence
must vanish.

The Jacobian factorization is

`4 sin(s/2)[sin(s/2)-(s/2)cos(s/2)]`.

For `0<s<2*pi`, the first factor is positive.  With `u=s/2`, the second has
derivative `u sin(u)>0` on `(0,pi)` and vanishes at zero.  Thus `2*pi` is the
first positive conjugate phase.

Horizontal length equals planar length and `z` equals signed planar area.
Dido's variational problem makes every minimizer a line or circular arc.  The
unique sub-full-turn Dido arc has central angle
`2 theta in (-2*pi,2*pi)` and is unique for a nonvertical endpoint.  At
`theta=+/-pi` it becomes a full circle: the initial
angle is lost and a Maxwell family reaches the same vertical endpoint.  The
isoperimetric inequality proves minimality up to this merger and proves the
vertical distance law.  Finally,

`mu'(theta)=2(sin(theta)-theta cos(theta))/sin(theta)^3>0`

on `(-pi,pi)`, so the implicit angle is unique.  Left invariance transports
the result from the identity.

The horizontal controls are periodic when `lambda != 0`, but the complete
geodesic is not: after one horizontal period its `z` coordinate changes by
`sign(lambda)*pi/lambda^2`.  When `lambda=0` the complete geodesics are lines.
Thus there are no nontrivial closed complete geodesics, so Route-A axis A1 is
`A1_FAIL`, not a weak periodic-orbit signal.

Status: **PROVABLE AS STATED**.
