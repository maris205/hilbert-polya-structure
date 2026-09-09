# NL424-3: integrated rational native-periodic atlas

2026-09-08 UTC. Coordinator integration of the original full question,
**under final cross-review and source/substance adjudication**. This is
not a new candidate, manuscript, formal Route-A grade or admission. The
[frozen contract](FROZEN_SCOUTS.md) is unchanged. Every parameter and
ordinary input point is rational. No mathematical program was used.

## 1. The theorem and its precise meaning

For every ordered triple `beta in Q³`, use the original site-fixed
`T=R13 after R12`, with an equal-parameter two-site map extended to the
global swap and every other two-site denominator required nonzero.
One whole transfer is one tick. On its factorwise two-sided regular
domain, the following cases classify every rational periodic point,
including all ordinary singular points and component intersections.

The possible native least periods, over all parameters and all rational
points in that domain, are exactly

`{1,2,3,4,5,6,7,8,9,10,12}`.

The bound 12 is sharp already on an explicitly described reducible level.
It is not a bound on the period of a changed/root clock, on geometric
points over larger fields, or on all rational birational maps.

For smooth fibres, “classification” means a precise rational elliptic
curve and torsion-translation criterion with all native pole orbits
removed. It does not assert an unconditional algorithm producing
Mordell--Weil generators for every elliptic curve. Nevertheless membership
of **any given rational point** in the periodic locus has the uniform
finite decision test in Section 6, independently of rank computation.

## 2. Exact invariant fibres and exhaustive case routing

The invariant map is `(S,H_beta)` from the original contract. Put

`u=x1+x2`, `v=x2+x3`, `w=x3+x1`, `t=2S`,
`a=beta3-beta2`, `b=beta1-beta2`, `c=beta2*t-h`.

The full affine level is

`uv(t-u-v)+a*u+b*v+c=0`, with `w=t-u-v`.

Both factors preserve it, including their allowed cancellations. The
inverse linear change is
`(x1,x2,x3)=((u+w-v)/2,(u+v-w)/2,(v+w-u)/2)`.
Every projective level is geometrically reduced, with three distinct
smooth rational infinity points and no infinity component. Every
geometric component is defined over `Q`.

The [reducibility proof](ADLER_REDUCIBLE_PROOF.md) and independently
derived [singular package, Steps 1–2](adler_singular_review/PROOF_PACKAGE.md)
give the exact iff: a fibre is geometrically reducible precisely when

`b=c=0`, or `a=c=0`, or `a=b and c=-b*t`.

The respective factors are `u(vw+a)`, `v(uw+b)`, `w(uv-b)`.
Thus a coincident parameter pair is necessary but not sufficient:
its corresponding level equality is essential. With exactly two equal
parameters there is one line and one smooth conic. With all three equal,
the reducible level consists of the three distinct lines `uvw=0`.
Every other fibre is geometrically irreducible and either smooth or
has exactly one singular point. This leaves no omitted nonreduced,
Galois-permuted-component, or additional infinity-singularity branch.

When all three parameters are equal, shortcut every fibre case:
`T(x1,x2,x3)=(x3,x1,x2)` everywhere, so diagonal points have period 1
and every other point period 3. This shortcut agrees with the other
descriptions wherever they apply.

## 3. Smooth fibres: nonzero translation, exact native holes

Use original plane coordinates `x=x1`, `y=x2`, `x3=S-x-y`.
The projective completion of the affine cubic

`(x+y)(S-x)(S-y)+beta1*(S-x)+beta2*(S-y)+beta3*(x+y)-h=0`

has infinity points `O=[1:0:0]`, `Q=[0:1:0]`, `R=[1:-1:0]`.
Equip the smooth fibre `E` with the rational origin `O`. Let `K` be
the line-section class minus `3O`. Chord involutions through `R` and
`O` act as `P -> K-R-P` and `P -> K-P`, respectively, so in the
frozen order

`T(P)=P+R`.

The full [smooth proof and origin correction](adler_followup_review/REVIEW.md)
identify these with the two original factors, not an arbitrary pair of
involutions. An arbitrary origin is not automatically a flex; `Q+R=K`
does not imply `Q=-R`. Since `R!=O`, no smooth point is fixed.

Let `B` be the rational points at infinity together with all affine
points at which either of the two successive native factor operations
is forbidden. Zero parameter differences create no forbidden denominator.
This is an explicitly defined finite subset of `E(Q)`. The exact
two-sided domain on this fibre is

`E(Q) \ union_(j in Z) T^(-j)(B)`.

If `R` has infinite order, there are no periodic points. If its order is
`n`, all points of the complement have least period `n`, and the deleted
union is just `j=0,...,n-1`. Thus projective periodicity alone does not
count a point that crosses an intermediate pole. Mazur's theorem bounds
the nonzero rational point order to `2,...,10,12`; this external classical
input is fully deducted.

The list is sharp on smooth fibres. The native two-cycle for
`beta=(0,4,1), S=h=0` is `(1,1,-2) <-> (-1,-1,2)`; its intermediate
denominators are `2,1,-2,-1`. For each other listed order, the smooth
report gives a rational coordinate normalization of an elliptic curve
with a torsion point of that order to this exact Adler family. Published
positive-rank examples ensure infinitely many rational points; removing
the finite torsion saturation of `B` leaves a native orbit. This imports
the source's existence result, not a new positive-rank construction.

## 4. Geometrically irreducible singular fibres

The complete [normalization proof](adler_singular_review/PROOF_PACKAGE.md)
is a dependency of this theorem, not a generic-elliptic extrapolation.
The unique singular point `(r,s,k)` in pair-sum coordinates is rational,
with `r*s*k!=0`, and is fixed by both native factors. Its relations are

`t=r+s+k`, `a=s*(r-k)`, `b=r*(s-k)`, `c=r*s*(k-r-s)`.

It is always one ordinary native fixed point, even for a nonsplit node.
Its normalization by a rational slope `z` is

`u=((k-s)*z-s)/(z*(z+1))`,
`v=z*(k-r-r*z)/(z+1)`,
`w=(z+1)*(r*z+s)/z`.

Let `q(z)=-s+(k-r-s)*z-r*z²` and `H0={0,-1,infinity}`.
The first and second factors on the normalization are

`M12(z)=s*(z+1)/((k-s)*z-s)`, `M13(z)=s/(r*z)`,

so one native tick induces

`M(z)=((k-s)*z-s)/(r*(z+1))`.

The singular preimages are exactly `q=0`, the fixed points of `M`.
The exact smooth native rational locus is the image of

`P¹(Q) \ ({q=0} union union_(j in Z) M^j(H0))`.

The one-tick extra poles are `M^-1(0)` and `M^-1(-1)`; when a
parameter difference vanishes its corresponding point is already in
`H0`, so the formula does not impose a cancelled pole.

Set `eta=(r+k-s)²/(r*k)`. For `eta=0,1,2,3`, respectively, `M` has
order `m=2,3,4,6`. Every smooth native point has least period `m`,
and the deleted orbit union is finite, `j=0,...,m-1`. Otherwise the
only periodic point on this fibre is its singular fixed point. This
includes cusps (`eta=4`, nonidentity parabolic map) and split/nonsplit
nodes. The finite-order criterion follows by elementary projective
linear algebra, not by applying elliptic torsion theory to a singular
curve. The sharp six-orbit is hand-verified in the proof package.

## 5. Reducible fibres: all components, intersections and domains

The [complete direct factor calculation](ADLER_REDUCIBLE_PROOF.md)
supplies the following atlas. For `d!=0`, set `M_(t,d)(z)=t+d/z`.
Write `D_infty(M)={M^j(infinity): j in Z}`, whether this orbit is
finite or infinite. In every line/conic chart below, the entire native
two-sided parameter set is `P¹(Q) \ D_infty(M)`. At an ordinary
component intersection use the separate action specified below; do
not count its two component labels as two different points.

| Parameter equality and level | Components and parameters | Native component maps | Intersection action |
| --- | --- | --- | --- |
| `beta1=beta2!=beta3`, `b=c=0` | `L(r)=(0,r,t-r)`; `C(z)=(t-z+a/z,z,-a/z)` | `L(r)->C(-a/r)`, `C(z)->L(t-z)`; `T²` is `M_(t,a)` on L and its inverse on C | Roots of `r²-tr-a=0`: two distinct rational roots exchanged; double root fixed |
| `beta1=beta3!=beta2`, `a=b!=0,c=-bt` | `L(r)=(r,t-r,0)`; `C(z)=(z,b/z,t-z-b/z)` | `L(r)->C(b/r)`, `C(z)->L(t-z)`; `T²` is `M_(t,-b)` on L and its inverse on C | Roots of `r²-tr+b=0`: two distinct rational roots exchanged; double root fixed |
| `beta2=beta3!=beta1`, `a=c=0,b!=0` | `L(r)=(r,0,t-r)`; `C(z)=(z,t-z+b/z,-b/z)` | L preserved by `M_(t,b)`; C preserved by its inverse | Each rational root of `r²-tr-b=0` fixed individually |

To verify the full domain statement rather than just its finite-period
part, the initial chart and factor restrictions remove `0,infinity,t`
as they arise in the line/conic transition formulas. These all belong
to `D_infty(M)` because `infinity -> t`, `0 -> infinity`. Saturating
under both return directions deletes exactly that one orbit. The
transition between L and C conjugates the two inverse return actions
and maps this same infinity orbit to itself. No other native hole is
present in the displayed exact factors. Rational intersections are
nonzero fixed points of `M`, so never lie in its infinity orbit.

The finite projective orders of `M_(t,d)` are exactly 2 if `t=0`,
3 if `t!=0,t²=-d`, 4 if `t!=0,t²=-2d`, and 6 if
`t!=0,t²=-3d`. For such an order `m`, every nonintersection native
point in either of the first two rows has **least period `2m`**, and
in the third row **least period `m`**. Infinite-order cases have no
nonintersection periodic points. The intersection action in the last
column supplies all remaining periods 1 or 2. Irrational intersections
are not ordinary rational states; a tangency is one ordinary point.

For all three equal parameters use the global period-1-or-3 swap rule
of Section 2, including the three-line level and its concurrent case.
Thus the complete reducible contribution lies in `{1,2,3,4,6,8,12}`.
At `beta=(0,0,-1/3), S=1/2,h=0`, the point
`(-3/2,3/2,1/2)` has native least period 12. Its line parameter 2 is
outside the order-six infinity orbit of `M(z)=1-1/(3z)` and is not
an intersection. This follows from the exact matrix criterion, not
from a guessed numerical period.

## 6. Uniform finite membership test and global sharpness

Given any rational `beta` and `P in Q³`, perform the original factors
with their declared cancellations, stopping if a noncancelled zero
denominator is encountered. After each full tick `j=1,...,12`, test
whether the current point equals `P`. The first equality returns its
exact least period. If a factor fails first, or if no equality has
occurred after tick 12, return “not a native periodic point”.

This is an exact rational-arithmetic decision procedure, not a
height/period search conjecture. If it returns a cycle, all its factor
steps are regular and reversing those involutions makes the cycle
two-sided native. Conversely any native periodic input belongs to one
of the exhaustive cases above, hence has period at most 12 and must
be found. A negative result does **not** assert that a nonperiodic
input fails to have a full native two-sided orbit. The test decides
periodic membership only and terminates without computing a rank.

Combining the three cases excludes 11 and every period above 12.
All periods 2 through 10 and 12 are realized on smooth fibres as
proved in Section 3; period 1 occurs in the all-swap family, and the
explicit reducible example independently makes 12 sharp. Hence the
global period set in Section 1 is exact.

## 7. Source, review and admission boundaries

The original Adler transfer, invariants and integrability are source-owned.
The [smooth review's source audit](adler_followup_review/REVIEW.md)
deducts the two-involution mechanism, Mazur's restriction, arbitrary-origin
Picard arithmetic and positive-rank torsion examples. The explicit
singular and reducible formulas close the boundary omitted by a
smooth-only argument; their existence does not automatically establish
a paper-level new mechanism or result increment.

The coordinator has read both complete branch reports and the complete
reducible proof and integrated the exact cases here. Branch checks and
final source/substance review are recorded separately when actually
completed. This file presently does not assert their future outcome,
global priority, journal readiness, a formal Route-A evaluation, target
Euler factors, root numbers, automorphy, a zero/divisor correspondence
or a Hilbert–Pólya realization. No mathematical program has run for this
Adler follow-up, and the finite membership test is proved but not
implemented or represented as an executed certificate.
