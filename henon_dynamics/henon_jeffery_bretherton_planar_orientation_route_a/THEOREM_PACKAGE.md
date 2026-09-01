# Exact theorem package — HCS-C280

## 1. Frozen owner

Let

`L=diag(L2,0)`, `L2=[[a,b],[c,-a]]`,

and put `E=(L+L^T)/2`, `W=(L-L^T)/2`.  A passive axisymmetric spheroid of
finite aspect ratio `r>0` has shape parameter

`lambda=(r^2-1)/(r^2+1) in (-1,1)`.

For `r!=1`, its intrinsic head–tail director is `[p] in RP2`; a unit
representative obeys

`p'=Wp+lambda(Ep-(p^T E p)p)`.

An unmarked sphere (`r=1`) has no intrinsic shape director.  Every `r=1` row
below retains `RP2` only for a marked material director carried by the sphere.

The clock is physical time.  There is no particle inertia, Brownian rotation,
spatial transport, hydrodynamic interaction, or fluid feedback.

## 2. Projective lift

Set `B=W+lambda E`.  Since `p^T Wp=0`, the equation is

`p'=Bp-(p^T Bp)p`.

If `q'=Bq` and `p=q/||q||`, differentiation gives exactly this equation.
Conversely, multiplying a director solution by the scalar integrating factor
`exp(int p^T Bp dt)` lifts it to `q'=Bq`.  Therefore

`[p(t)]=[exp(tB)q0]`

globally.  The normalization never vanishes because a matrix exponential is
invertible.

## 3. Scalar discriminant

Writing

`k=(b-c)/2`, `s=(b+c)/2`,

the active block is

`B2=[[lambda a,k+lambda s],[-k+lambda s,-lambda a]]`.

It is traceless and direct multiplication gives

`B2^2=delta I`,

`delta=lambda^2(a^2+s^2)-k^2=-det B2`.

Thus, with `rho=sqrt(delta)` or `omega=sqrt(-delta)`,

- `delta>0`: `exp(tB2)=cosh(rho t)I+sinh(rho t)B2/rho`;
- `delta<0`: `exp(tB2)=cos(omega t)I+sin(omega t)B2/omega`;
- `delta=0`: `exp(tB2)=I+tB2`.

These formulas meet continuously at the discriminant wall.

## 4. Complete classification theorem

### Elliptic chamber

If `delta<0`, `B2` has no real eigenline.  The vertical director is the only
fixed point.  On the equator `exp(pi B2/omega)=-I`, so every equatorial
head–tail director has least period `pi/omega`.  A director with both vertical
and horizontal components is not returned by this sign change, but is returned
by `exp(2pi B2/omega)=I`; its least period is `2pi/omega`.

For a strobe time `tau>0`:

- if `omega tau` is not an integer multiple of `pi`, only the vertical point
  is fixed;
- if it is an odd multiple of `pi`, the fixed set is the equatorial `RP1`
  together with the vertical point;
- if it is an even multiple, all of `RP2` is fixed.

### Hyperbolic chamber

If `delta>0`, choose horizontal eigenvectors `v_+`, `v_-` for eigenvalues
`rho`, `-rho`, and let `e0` be vertical.  The three eigen-directors are exactly
the fixed set.  For

`q=q_+v_+ + q_0e0 + q_-v_-`,

the forward limit is `[v_+]` if `q_+!=0`, `[e0]` if `q_+=0,q_0!=0`, and
`[v_-]` otherwise.  The backward statement reverses `+` and `-`.  Hence
`[v_+]` is the sink, `[v_-]` the source, and `[e0]` the saddle.  Precisely,

`W^s([e0])=P(span(e0,v_-))\{[v_-]}`,

`W^u([e0])=P(span(e0,v_+))\{[v_+]}`.

Their closures are the two invariant `RP1` projective lines.  Coordinate
ratios give exponential gaps `rho` or `2rho`, so no unstated recurrence
remains.

### Nilpotent and identity faces

If `delta=0` but `B2!=0`, then `B2` has rank one and
`im B2=ker B2`.  Since `exp(tB)=I+tB`, the full fixed set is the projective
line `P(ker B)`.  For every point outside it,

`[q+tBq] -> [Bq]`

as `t->+/- infinity`; both time directions approach the unique horizontal
image/kernel director, at algebraic rate `1/|t|`.  If `B2=0`, `B=0` and the
flow is the identity on all of `RP2`.

## 5. Simple-shear corollary and boundaries

For `L2=[[0,gamma],[0,0]]` with `gamma!=0`,

`delta=-gamma^2 r^2/(r^2+1)^2`,

so `omega=|gamma|r/(r^2+1)`.  The equatorial head–tail director period is

`T_RP1=pi(r+r^(-1))/|gamma|`.

Every nonvertical oriented vector, or a mixed `RP2` director, needs

`T=2pi(r+r^(-1))/|gamma|`.

The vertical oriented vector is fixed.  At `r=1`, strain drops out: a marked
material director follows vorticity, while an unmarked sphere has no intrinsic
orientation state.  As `r->infinity`
or `r->0`, `lambda->+/-1`, `omega->0`, the period diverges, and the limiting
simple-shear generator is nilpotent.  At `gamma=0`, every director is fixed.
These singular rod/disk limits are not silently included among finite
aspect-ratio periodic orbits.

## 6. Evidence theorem boundary

The deterministic receipt contains 625 exact rational parameter cells, 320
90-digit projective orbit reconstructions, 10 exact shear-period cells, five
strobe cells, and six named boundaries.  The independent checker passes 8,328
assertions, SymPy passes 39 identities, fresh replay is byte-exact, and 25/25
hostile mutations are rejected.  This evidence detects convention and code
regressions; it does not replace the arbitrary-parameter proof above.

## 7. Route-A theorem

The tuple is

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.

There is no arithmetic origin, rational-prime carrier, logarithmic prime
clock, target divisor, target determinant, or target zero match.  The only
nontrivial periodic chamber is a clean continuum of projective orbits whose
period varies with continuous fluid and shape parameters.  Hyperbolic and
nilpotent chambers align rather than recur.  Therefore the ordinary isolated
primitive-orbit gate fails and the result is `ROUTE_A_REJECTED`; Route B is
not authorized.
