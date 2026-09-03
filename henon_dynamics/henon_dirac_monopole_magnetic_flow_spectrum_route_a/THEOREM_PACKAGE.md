# Proof Package

## Claim

Let `S^2` be the oriented unit sphere. Let `L_q -> S^2` be a Hermitian line bundle with `q in Z` and a unitary connection whose curvature is `F=i(q/2)dA`. Put `b=q/2`.

For the magnetic equation

`nabla_t xdot = b J xdot`, with `|xdot|^2=2E`,

the vector `K=x cross xdot+b x` is conserved and obeys `K dot x=b` and `|K|^2=2E+b^2`. If `E>0`, the trajectory is a nonconstant oriented small circle and its least period is

`T(E,q)=2 pi/sqrt(2E+q^2/4)`.

If `E=0`, every solution is stationary. At `q=0`, the positive-energy circles are great circles.

Every unitary connection in the claim is unitary-gauge equivalent to the standard homogeneous degree-`q` monopole connection: degree classifies the line bundle, equal curvature makes the connection difference closed, and `H^1_dR(S^2)=0` makes it exact.

On `C^infty(S^2,L_q)=C_c^infty(S^2,L_q)`, close the nonnegative form

`Q_q(s)=integral_(S^2) |nabla s|^2 dA`,

and let `Delta_q` be its Friedrichs operator. The differential expression `nabla^*nabla` is essentially self-adjoint on the closed sphere, so this is also its unique self-adjoint closure. Its complete spectrum is

`lambda_(n,q)=n(n+|q|+1)+|q|/2`, `n=0,1,...`,

with multiplicity `2n+|q|+1`. Consequently, for every `t>0`,

`Tr exp(-t Delta_q)=sum_(n>=0) (2n+|q|+1) exp(-t lambda_(n,q))`.

If `x_q(t)` is a charge-`q` solution, then `x_q(-t)` with initial velocity reversed is a charge-`-q` solution: this time-reversal pairing traverses the same geometric circle oppositely. Replacing `L_q` by its conjugate preserves the quantum spectrum. Nonintegral `q` does not define the frozen global line bundle.

## Status

PROVABLE AS STATED

## Assumptions

- The sphere has radius one and its standard orientation and metric.
- `J v=x cross v` is rotation by positive ninety degrees in `T_x S^2`.
- The magnetic charge is `b=q/2` with `q in Z`.
- `Delta_q` is the Friedrichs realization of the positive covariant Laplacian on smooth sections.
- “Primitive” means least positive period of the source-local nonconstant orbit, not an isolated hyperbolic orbit.

## Notation

- `dA` is the sphere area form, with integral `4 pi`.
- `E=|xdot|^2/2` is the conserved kinetic energy.
- `ell` denotes an `SU(2)` angular-momentum label.
- `n=ell-|q|/2` is the nonnegative radial/representation index.

## Proof Strategy

Use an ambient three-dimensional conserved vector to solve the classical flow as a rigid rotation. Use Chern--Weil integrality to lock the charge. Classify the degree-`q` bundle, use `H^1_dR(S^2)=0` to gauge every connection with the frozen curvature to the standard homogeneous monopole connection, and fix the operator through its Friedrichs form. Only then identify the standard covariant Laplacian with the `SU(2)` Casimir minus the fixed vertical Casimir and decompose the induced representation into irreducibles.

## Dependency Map

1. The classical orbit theorem depends on the ambient acceleration identity and conservation of `K`.
2. The least-period statement depends on the positive radius when `E>0`.
3. The global quantum model depends on the first Chern number computation.
4. The passage to homogeneous sections depends on line-bundle classification and `H^1_dR(S^2)=0`, not merely on equality of curvature forms.
5. The operator statement depends on the Friedrichs closure of the smooth-section energy form and essential self-adjointness on a compact manifold without boundary.
6. The spectrum depends on the multiplicity-one `SU(2)` decomposition of degree-`q` equivariant functions.
7. The heat trace depends on compact elliptic self-adjointness and the quadratic growth of the displayed eigenvalues.

## Proof

### Step 1: energy and ambient acceleration

Metric compatibility and skew-symmetry of `J` give

`d|xdot|^2/dt=2 <nabla_t xdot,xdot>=2b<J xdot,xdot>=0`.

Thus `E` is constant. For a unit-sphere curve, the ambient derivative satisfies

`xddot=nabla_t xdot-|xdot|^2 x=b x cross xdot-2E x`.

### Step 2: conservation of the Poincare vector

Differentiate `K=x cross xdot+b x` in ambient space. Since `xdot cross xdot=0`,

`Kdot=x cross xddot+b xdot`.

The radial term in `xddot` has zero cross product with `x`, while

`x cross (x cross xdot)=-xdot`.

Therefore `Kdot=-b xdot+b xdot=0`. Orthogonality gives

`K dot x=b`,

and

`|K|^2=|x cross xdot|^2+b^2=2E+b^2`.

### Step 3: complete classical orbit and least period

The triple-product identity gives

`K cross x=(x cross xdot) cross x=xdot`.

Hence `x` solves the constant-coefficient rotation equation `xdot=K cross x`. It lies simultaneously on the unit sphere and the plane `K dot x=b`; this is a circle. If `E>0`, its squared radius is

`1-b^2/|K|^2=2E/(2E+b^2)>0`.

Rodrigues' formula rotates this nonzero-radius circle through angle `|K|t`. A nonconstant circle has no smaller positive rotation returning every point and tangent than angle `2 pi`. Its least period is therefore

`2 pi/|K|=2 pi/sqrt(2E+q^2/4)`.

If `E=0`, then `xdot=0`; these are stationary points and have no primitive period. If `q=0`, the plane passes through the origin, so every positive-energy orbit is a great circle.

### Step 4: Chern boundary

The frozen curvature has

`(1/(2 pi i)) integral_(S^2) F=(1/(2 pi i)) i(q/2) 4 pi=q`.

Thus it is the curvature of a degree-`q` Hermitian line bundle. Conversely, the left side must be integral for any global Hermitian line bundle. This proves that nonintegral `q` is outside the frozen global quantum model even though the local classical equation can still be written.

### Step 5: bundle, connection, and operator bridges

Complex line bundles over `S^2` are classified up to isomorphism by their first Chern class in `H^2(S^2;Z)=Z`. Thus `L_q` is isomorphic to the standard degree-`q` homogeneous monopole bundle. Choose a unitary bundle isomorphism and transport both connections to that bundle. Two unitary connections there differ by `i alpha` for a real one-form `alpha`; equality of their curvature gives `d alpha=0`. Since `H^1_dR(S^2)=0`, there is a real smooth function `f` with `alpha=df`. In the convention `nabla=nabla_hom+i df`, the unitary gauge `g=e^{if}` satisfies `g^{-1} nabla_hom g=nabla`. Hence every connection in the claim is unitarily gauge equivalent to the standard homogeneous connection, and their covariant Laplacians are unitarily conjugate.

On the compact sphere, `C_c^infty(S^2,L_q)=C^infty(S^2,L_q)`. The densely defined nonnegative form

`Q_q(s)=integral_(S^2) |nabla s|^2 dA`

is closable, and its closed form defines the Friedrichs realization `Delta_q`. The symmetric Laplace-type operator `nabla^*nabla` on smooth sections of a Hermitian bundle over a compact manifold without boundary is essentially self-adjoint. Its unique self-adjoint closure therefore equals this Friedrichs realization. It is nonnegative and has compact resolvent. These facts fix both the gauge class and the operator domain before any representation-theoretic calculation.

### Step 6: complete covariant-Laplacian spectrum

By Step 5 it suffices to use the standard homogeneous bundle and connection. Realize its sections as functions on `SU(2)` equivariant under the right `U(1)` action with weight `q`. Peter--Weyl decomposition says that the spin-`ell` irreducible occurs exactly once whenever

`ell=|q|/2+n`, `n=0,1,...`.

Its dimension is `2ell+1`. With the unit-sphere normalization, the horizontal covariant Laplacian is the total Casimir minus the fixed vertical weight square. Hence on this summand,

`Delta_q=ell(ell+1)-q^2/4`.

Substitution of `ell=|q|/2+n` gives

`lambda_(n,q)=n(n+|q|+1)+|q|/2`,

and the dimension gives multiplicity

`2ell+1=2n+|q|+1`.

Peter--Weyl completeness proves that no further eigenvalues or eigensections occur.

### Step 7: heat trace and sign involution

The eigenvalues grow quadratically in `n` and the multiplicities grow linearly. Thus the displayed exponential series converges absolutely for every `t>0` and the spectral theorem gives the heat trace formula.

If `x_q(t)` solves the charge-`q` equation, set `y(t)=x_q(-t)`. Then `ydot(t)=-xdot_q(-t)` while its covariant acceleration equals the acceleration of `x_q` at `-t`. The charge-`-q` right side is `(-b)Jydot=bJxdot_q(-t)`, so `y` is a charge-`-q` solution with reversed initial velocity. This pairs the same geometric circle with the opposite traversal; it does not identify solutions having the same initial velocity. Complex conjugation sends the degree-`q` connection to degree `-q`; the formula depends only on `|q|`, so eigenvalues and multiplicities agree.

Therefore every part of the claim follows. ∎

## Corrections or Missing Assumptions

- None. The charge convention `b=q/2`, sphere radius, curvature, and positive-Laplacian sign are essential and explicitly frozen.

## Open Risks

- The result is a source-local reconstruction, not a priority claim.
- Chern integrality supplies only a weak arithmetic relation; it does not identify rational primes.
- The classical periodic circles form clean families rather than isolated hyperbolic cycles.
- The Friedrichs/essentially-self-adjoint covariant Laplacian is natural, but no target-zero or Hilbert--Polya claim follows.
