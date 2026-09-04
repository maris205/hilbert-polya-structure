# Proof package

## Claim

Let `N>=2`, `d>=1`, `K>0`, `beta>=0`, and let

$$
\dot x_i=v_i,\qquad
\dot v_i=\frac K N\sum_{j=1}^N\psi(|x_j-x_i|)(v_j-v_i),
\qquad \psi(r)=(1+r^2)^{-\beta}.
$$

Write `bar v=N^{-1} sum_i v_i`,
`X=max_{i,j}|x_i-x_j|`, and `V=max_{i,j}|v_i-v_j|`.
Then the flow is global, `bar v` is conserved, and

$$
\frac d{dt}\frac1N\sum_i|v_i-\bar v|^2
=-\frac K{N^2}\sum_{i,j}\psi(|x_i-x_j|)|v_i-v_j|^2.
$$

The upper Dini derivatives obey

$$D^+X\le V,\qquad D^+V\le-K\psi(X)V.$$

If

$$
V_0<K\int_{X_0}^{\infty}\psi(s)\,ds,
$$

there is a unique `R>=X0` with
`K integral_[X0,R] psi=V0`; moreover `X(t)<=R` and
`V(t)<=V0 exp(-K psi(R)t)`.  Hence relative positions converge and all
velocities converge to `bar v`.  Since the tail diverges exactly when
`0<=beta<=1/2`, flocking is unconditional throughout that chamber, endpoint
included.

For `N=2`, `d=1`, outward initial data `r(0)=r0>=0` and
`u(0)=u0>=0` satisfy

$$r'=u,\qquad u'=-K\psi(r)u,qquad
u(r)=u_0-K\int_{r_0}^{r}\psi(s)\,ds.$$

When `beta>1/2`, put `A=K integral_[r0,infinity] psi`.  If `u0<A`, the
separation converges to the unique finite zero of the displayed first
integral.  If `u0=A`, then `r(t)` tends to infinity while `u(t)` tends to zero.
If `u0>A`, then `u(t)` tends to `u0-A>0` and `r(t)/t` has the same limit.

## Status

PROVABLE AS STATED.

## Dependency map and proof

### 1. Global flow

The vector field is locally Lipschitz.  For every unit vector `e`, a velocity
projection attaining its maximum has nonpositive derivative and one attaining
its minimum has nonnegative derivative.  Thus the velocity convex hull is
forward invariant.  Velocities remain bounded and positions grow at most
linearly, excluding finite-time escape and extending the local solution
globally.

### 2. Conservation and dissipation

Pair symmetry cancels the double sum in `sum_i dot v_i`, proving conservation
of `bar v`.  Pairing `(i,j)` with `(j,i)` in
`2 N^{-1} sum_i (v_i-bar v) dot dot v_i` gives the displayed exact negative
sum.  No missing factor of two remains because the ledger sum is ordered.

### 3. Diameter lemma

If `V=0`, every velocity is identical, every alignment acceleration vanishes,
and the second Dini inequality is immediate.  Otherwise, at a differentiability
time choose a velocity-diameter pair `(p,q)`, put `e=(v_p-v_q)/V`, and write
`z_j=e dot v_j`.  Then
`z_q<=z_j<=z_p`.  Since every communication weight is at least `psi(X)`,
replacing the weights in the negative terms of `dot z_p` and the positive
terms of `dot z_q` yields

$$
\dot z_p-\dot z_q\le
\frac{K\psi(X)}N\sum_j[(z_j-z_p)-(z_j-z_q)]
=-K\psi(X)V.
$$

Taking the maximum over active pairs proves the Dini inequality.  The same
active-pair argument for the spatial diameter gives `D+X<=V`.

### 4. Tail barrier

Where ordinary derivatives exist,

$$
D^+\left[V+K\int_{X_0}^{X}\psi(s)\,ds\right]\le0.
$$

The strict tail condition defines a finite `R`.  A first-crossing argument
prevents `X` from exceeding `R`; at a putative first hit the barrier forces
`V=0`, hence `D+X<=0`.  Monotonicity of `psi` then gives
`D+V<=-K psi(R)V` and the exponential bound.  Its integrability makes every
relative position Cauchy.  The conserved mean identifies the common velocity.

The primitive

$$
\Phi_\beta(r)=\int_0^r(1+s^2)^{-\beta}ds
=r\,{}_2F_1(1/2,\beta;3/2;-r^2)
$$

makes `R=Phi_beta^{-1}(Phi_beta(X0)+V0/K)`.  Comparison with `s^{-2beta}`
shows that `Phi_beta(infinity)` diverges exactly for `beta<=1/2`.

### 5. Exact two-body sharpness

Subtracting the two velocity equations gives the scalar system in the claim.
On every interval with `u>0`, division gives `du/dr=-K psi(r)`; continuity
extends its first integral through the limiting endpoint.  A finite zero gives
the subthreshold limit.  At equality the tail integral is positive at every
finite `r`, so `r` cannot stop finitely; its divergence forces `u` to zero.  In
the superthreshold case the first integral tends to `u0-A>0`, and Cesaro
averaging of `r'=u` gives `r(t)/t` with the same limit.

### 6. Degenerate faces

For `N=1`, both diameters vanish.  For `K=0`, velocities are constant and
flocking occurs exactly when `V0=0`.  If `V0=0` with `K>=0`, relative positions
are fixed.  Coincident positions cause no singularity because `psi(0)=1`.
The strict many-body tail inequality is not asserted necessary; equality and
failure are classified only in the stated scalar outward subfamily.

## Open risks

None inside the frozen theorem.  Singular kernels, normalized-neighbour
weights, noise, delay, collision avoidance, and mean-field limits are outside
scope.
