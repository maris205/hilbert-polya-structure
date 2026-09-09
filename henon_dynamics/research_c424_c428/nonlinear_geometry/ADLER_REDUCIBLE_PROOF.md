# NL424-3: complete reduced-fibre test and reducible native dynamics

2026-09-08 UTC. Coordinator hand-proof draft for nonauthor review. This
does not by itself solve the complete Adler question or make an admission.
All parameters and ordinary input points below are rational. No program ran.

## 1. Pair-sum coordinates and exact native factors

Set

`u=x_1+x_2`, `v=x_2+x_3`, `w=x_3+x_1`, `t=u+v+w=2S`,
`a=beta_3-beta_2`, `b=beta_1-beta_2`, `c=beta_2*t-h`.

This is an invertible rational linear change, with
`x_1=(u+w-v)/2`, `x_2=(u+v-w)/2`, `x_3=(v+w-u)/2`.
The full affine invariant level is

`F(u,v)=uv(t-u-v)+a*u+b*v+c=0`, `w=t-u-v`.

Writing `e=b-a=beta_1-beta_3`, the two native factors are

`A=R12: (u,v,w) -> (u,w+b/u,v-b/u)`,
`B=R13: (u,v,w) -> (v-e/w,u+e/w,w)`,
`T=B after A`.

For `b=0`, `A` is the globally regular swap of `v,w`, including `u=0`.
For `e=0`, `B` is the globally regular swap of `u,v`, including `w=0`.
Otherwise their written denominators must be nonzero. Each factor is an
involution on its declared regular domain. Consequently a finite closed
forward word with all intermediate factors regular has the same valid
inverse word, and is in the two-sided native domain. No simplified whole-map
formula enlarges this domain.

## 2. Every fibre is reduced; all reducible fibres are explicit

The homogeneous cubic is

`Fbar(U,V,W)=UV(tW-U-V)+a*UW²+b*VW²+c*W³`.

Its intersection with the line at infinity has the three distinct points
`[1:0:0]`, `[0:1:0]`, `[1:-1:0]`. At each, at least one of the `U,V`
partial derivatives of `-UV(U+V)` is nonzero, so the curve is smooth there
for every parameter. It has no component equal to the line at infinity.

If a geometric irreducible factor occurred with multiplicity at least
two, its highest homogeneous part would give a repeated factor of
`-UV(U+V)`, which is squarefree. The highest part is nonconstant for a
nonconstant affine factor. Thus every fibre is geometrically reduced.

A reducible geometric cubic has a linear component. The highest part of
such a line is proportional to `u`, `v` or `u+v`. Substituting a general
line in each direction into `F` gives the entire list:

| Line | Necessary and sufficient condition | Full factorization |
| --- | --- | --- |
| `u=0` | `b=c=0` | `u(vw+a)` |
| `v=0` | `a=c=0` | `v(uw+b)` |
| `w=0` | `a=b`, `c=-bt` | `w(uv-b)` |

For example, substituting `u=r` gives a quadratic in `v` with coefficient
`-r`, so `r=0`, followed by `b=c=0`. The `v` case is identical. Substituting
`u+v=r` forces `r=t` from the quadratic coefficient, then `a=b,c=-bt`.
This reasoning works over the algebraic closure; the displayed factors
are therefore all the geometric possibilities, not merely rational factors.

In the original parameters, reducibility requires a coincident pair and
the corresponding level `h=2S` times that pair's common parameter. If
exactly two parameters agree, the remaining quadratic factor is a smooth
conic: its nonzero product constant forbids an affine singularity, and
its infinity points are already smooth. If all three agree, the reducible
level has the three distinct lines `u v w=0`, including the concurrent
case `t=0`. There is no double line, hidden geometric factor, or omitted
nonreduced level.

## 3. Rational Möbius classification used below

For `d!=0`, let `M_(t,d)(r)=t+d/r` on the full projective line and
`A_(t,d)=[[t,d],[1,0]]`. Its determinant is `-d`, so it is invertible
and is never the identity. Its finite-order cases over the rationals are

| Projective order `m` | Exact condition |
| --- | --- |
| 2 | `t=0` |
| 3 | `t!=0`, `t²=-d` |
| 4 | `t!=0`, `t²=-2d` |
| 6 | `t!=0`, `t²=-3d` |

Here is a complete elementary justification, with no assumed period cutoff.
For distinct eigenvalues the eigenvalue ratio is a root of unity precisely
when the projective matrix has finite order. The rational number
`(tr A)²/det A` then equals `2+zeta+zeta^(-1)`, a rational algebraic integer
in `[0,4]`. The distinct-eigenvalue case excludes value 4; the remaining
values `0,1,2,3` give orders `2,3,4,6`. Conversely each value gives the
stated eigenvalue ratio and exact order. A repeated eigenvalue would give
a nonidentity unipotent projective matrix, of infinite order in
characteristic zero.

For a nonidentity rational Möbius map, a nonfixed periodic point exists
only when the map has finite order, and its least period equals that order.
Over the algebraic closure, diagonal coordinates give `z -> lambda*z` in
the two-eigenline case and a translation in the repeated-eigenvalue case;
the assertion follows directly. Thus an infinite-order map has only its
rational fixed points as rational periodic points. This is classical
projective linear algebra, not a claimed new mechanism.

In finite order `m`, denote the finite orbit of `infinity` by `D_M`.
It contains `0,infinity,t`. Its complement among rational parameters is
exactly the periodic part which never encounters a missing finite chart
or a pole in the formulas below. Fixed points of `M`, when rational,
never belong to `D_M`, since `0` and `infinity` are not fixed.

## 4. Case beta_1=beta_2 != beta_3

Here `b=0`, `a!=0`, `e=-a`, and the reducible level is
`u(vw+a)=0`. Denote its line by `L:u=0` and conic by `C:vw=-a`.
The exact transfer is

`T(u,v,w)=(w+a/v,u-a/v,v)`, with `v!=0`.

Parametrize both components by their `v` coordinate. On `L`, use
`(0,r,t-r)`. On `C`, use `(t-z+a/z,z,-a/z)`. In both affine charts the
parameter must be finite and nonzero. Direct substitution gives

`L(r) -> C(-a/r)`, `C(z) -> L(t-z)`.

Away from the intersections, components alternate and
`T²|L=M_(t,a)`, `T²|C=M_(t,a)^(-1)` in these parameters. If `M` has
finite order `m`, every nonintersection point whose parameter avoids
`D_M` is in a native orbit of **least length 2m**. The excluded orbit is
the same for the inverse map on the conic; `z=t` is included in it because
the next line parameter would be zero. In the infinite-order case there
are no nonintersection periodic points.

The intersections are the roots of `r²-tr-a=0`, represented by `L(r)`.
They are nonzero and hence native regular. At them `T` acts as
`r -> t-r`, so two distinct rational roots form one two-cycle. At a
double rational root `r=t/2`, the single ordinary intersection point is
fixed. If the two distinct roots are irrational, there is no ordinary
rational point on their intersection. Scheme multiplicity at tangency
does not count a second ordinary point. These cases include every point
on both components and avoid double counting the intersection.

## 5. Case beta_1=beta_3 != beta_2

Here `a=b!=0`, `e=0`, and the reducible level is `w(uv-b)=0`.
Take `L:w=0`, `C:uv=b`, and use `u` as the parameter on each component:

`L(r)=(r,t-r,0)`, `C(z)=(z,b/z,t-z-b/z)`.

Both finite parameters are nonzero. The exact native transfer is

`T(u,v,w)=(w+b/u,u,v-b/u)`, with `u!=0`,

and therefore `L(r)->C(b/r)`, `C(z)->L(t-z)`.
The preceding proof applies with `d=-b`: `T²|L=M_(t,-b)` and
`T²|C=M_(t,-b)^(-1)`. Nonintersection periodic orbits have least length
`2m` when that Möbius map has finite order `m`, subject to deletion of
its infinity orbit, and none exist otherwise. Intersections solve
`r²-tr+b=0`; `T` swaps the two distinct rational roots or fixes the
single double root. All these ordinary intersection points are regular.

## 6. Case beta_2=beta_3 != beta_1

Here `a=0`, `b=e!=0`, and the reducible level is `v(uw+b)=0`.
Take `L:v=0`, `C:uw=-b` and parametrize by `u`:

`L(r)=(r,0,t-r)`, `C(z)=(z,t-z+b/z,-b/z)`.

In contrast to Sections 4–5, the native transfer preserves each component.
Direct substitution into the ordered factors gives

`T L(r)=L(t+b/r)`,
`T C(z)=C(b/(z-t))`.

The line requires finite `r!=0`; on the conic finite `z!=0,t` is required
by the two factors. Thus the line and conic maps are `M_(t,b)` and its
inverse, respectively. Finite-order nonintersection orbits have least
length **m**, not `2m`, after deletion of the common infinity orbit;
the infinite-order case has no nonintersection periodic point.

Intersections solve `r²-tr-b=0`. Each distinct rational intersection is
now fixed by `T`, not exchanged. A double root is one ordinary fixed point.
The roots are nonzero and different from `t`, so these points are always
native regular. The inverse maps give the same two-sided-domain conclusion.

## 7. All three parameters equal

Both factors are swaps and `T(u,v,w)=(w,u,v)` everywhere. Every rational
point has least period three, except `u=v=w`, which has period one.
This applies to every invariant level, reducible or irreducible, and
includes all zero coordinates. The invariant description does not impose
artificial poles on this globally regular map.

## 8. Consequences and remaining proof boundary

Every rational periodic point on every reducible fibre has period in
`{1,2,3,4,6,8,12}`, with the exact parameter/component/pole criteria above.
The order-six condition in Section 4 gives actual native twelve-cycles:
take `beta=(0,0,-1/3)`, `S=1/2`, `h=0`, and the line parameter `r=2`.
Then `t=1,a=-1/3`, and the forbidden infinity orbit of
`M(r)=1-1/(3r)` is

`infinity -> 1 -> 2/3 -> 1/2 -> 1/3 -> 0 -> infinity`.

The rational value 2 is outside it and is not an intersection; hence
`(-3/2,3/2,1/2)` has native least period twelve by Section 4. This is an
exact hand consequence of the full matrix criterion, not a numerical
period guess or the result of a sample scan.

The original question additionally requires every smooth and irreducible
singular fibre, and a coherent all-parameter native-domain classification.
Those proofs and source/substance subtraction are separate gates. No
admission, formal Route-A grade, target Euler factor, root number,
automorphy or Hilbert–Pólya claim follows from this draft.
