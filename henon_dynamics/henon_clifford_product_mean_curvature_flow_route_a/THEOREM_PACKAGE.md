# Proof package

## Claim

Let `p,q>=1`, `n=p+q`, and

`Sigma_theta=S^p(cos(theta)) x S^q(sin(theta))` in the unit `S^(n+1)`.

Under mean-curvature-vector flow, with the mean-curvature vector defined as
the negative area gradient, the family is invariant.  Writing
`y=sin(theta)^2`, the complete regular solution is

`y(t)=q/n+(y0-q/n) exp(2nt)`.

The minimal leaf `y=q/n` is stationary.  Every other leaf is ancient and
collapses in finite forward time to one focal submanifold, with the exact
times and tangent cylinders stated below.  Area decreases strictly off the
minimal leaf.  On the minimal leaf, with the second-variation convention
`Q(f,f)=-integral(f J f)`, the Jacobi operator has index `n+3` and nullity
`(p+1)(q+1)`.

## Status

PROVABLE AS STATED.

## Assumptions and notation

Both dimensions are positive.  Endpoints `y=0,1` are focal submanifolds and
not regular product hypersurfaces.  Put

`F_theta(x,z)=(cos(theta)x,sin(theta)z)` and choose
`nu=(-sin(theta)x,cos(theta)z)`.

The Laplacian has nonpositive spectrum.

## Dependency map

1. Principal curvatures give the scalar flow.
2. The scalar solution gives the maximal interval and backward limit.
3. Endpoint expansions give Type-I residues and tangent cylinders.
4. The product-area derivative gives strict dissipation.
5. The round-sphere product spectrum gives index and nullity.

## Proof

### 1. Reduction and lifespan

For a tangent vector to the first sphere, `-d nu` has eigenvalue
`tan(theta)`; on the second it has eigenvalue `-cot(theta)`.  Hence the scalar
mean curvature is

`H=p tan(theta)-q cot(theta)`.

Because `partial_theta F=nu`, mean-curvature-vector flow is
`theta'=H`.  Therefore

`y'=2 sin(theta)cos(theta) theta'=2(ny-q)`.

Solving the affine equation gives the claimed formula.  The unique stationary
leaf is `y*=q/n`.  If `y0<y*`, the first endpoint is `y=0`, at

`T0=(2n)^(-1) log(q/(q-ny0))`.

If `y0>y*`, the first endpoint is `y=1`, at

`T1=(2n)^(-1) log(p/(ny0-q))`.

Both logarithm arguments exceed one.  In either case the solution exists for
all earlier times and tends exponentially to `y*` as `t` tends to minus
infinity.  This proves the complete regular lifespan and both ancient
branches.

### 2. Focal singularities

The squared second fundamental form is

`|A|^2=p y/(1-y)+q(1-y)/y`.

On the left branch, `y=2q(T0-t)+O((T0-t)^2)`.  Thus
`(T0-t)|A|^2 -> 1/2`, and after scaling by `(T0-t)^(-1/2)` the collapsing
second sphere has radius `sqrt(2q)` while the first factor becomes flat.  The
tangent flow is `R^p x S^q(sqrt(2q))`.  On the right branch,
`1-y=2p(T1-t)+O((T1-t)^2)`, yielding the same residue and
`S^p(sqrt(2p)) x R^q`.  Both singularities are Type I.

### 3. Area law

Up to the fixed factor `|S^p||S^q|`,

`A(y)=(1-y)^(p/2)y^(q/2)`.

Direct differentiation with `y'=2(ny-q)` gives

`d/dt log A=-(ny-q)^2/[y(1-y)]=-H^2`.

It vanishes exactly on the minimal leaf and is negative elsewhere.

### 4. Minimal Jacobi spectrum

At `y*=q/n` the radii are `sqrt(p/n)` and `sqrt(q/n)`.  The principal
curvature squares sum to `|A|^2=n`; the ambient normal Ricci curvature is
also `n`.  Thus the Jacobi operator is `J=Delta+2n`.

Degree `(ell,m)` product harmonics have minus-Laplacian eigenvalue

`lambda_(ell,m)=n ell(ell+p-1)/p+n m(m+q-1)/q`.

The values below `2n` are only `(0,0)`, `(1,0)`, and `(0,1)`, with total
multiplicity `1+(p+1)+(q+1)=n+3`.  Equality occurs only at `(1,1)`, with
multiplicity `(p+1)(q+1)`.  Indeed, every degree at least two already exceeds
`2n` on its factor, and adding a nonzero degree cannot decrease an
eigenvalue.  This proves the index and nullity.

## Corrections and boundaries

No full classification of spherical MCF is claimed.  The cases `p=0` or
`q=0` change the geometry and are excluded.  The focal endpoints and the
backward limit are limiting objects rather than additional regular leaves.
The natural Jacobi operator is not a target arithmetic operator.

## Open risks

None inside the stated smooth two-factor family.  Stability beyond the
second-variation count and perturbations leaving the isoparametric family are
outside scope.
