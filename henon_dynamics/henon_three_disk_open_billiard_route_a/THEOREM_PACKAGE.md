# Theorem package — HCS-C294

Status: **PROVABLE AS STATED** in the strict chamber `r>0` and
`d>4r/sqrt(3)`.  Obstruction record: `HEN-O278`.

Let `K_0,K_1,K_2` be the closed radius-`r` disks whose centers form an
equilateral triangle of side `d`.  An admissible cyclic word
`w=(i_0,...,i_{n-1})` has `i_j != i_{j+1}` with indices modulo `n`.
Write its cyclic class uniquely as `[w]=[u^m]`, with `[u]` primitive and
`m>=1`.  A **periodic-ray iterate** means a primitive oriented geometric ray
together with its positive traversal multiplicity `m`.

## Headline theorem

Modulo cyclic shift, admissible words are in bijection with periodic-ray
iterates.  If `[w]=[u^m]`, its image is the `m`-fold traversal of the unique
primitive oriented ray coded by `[u]`; in particular, primitive cyclic words
are in bijection with primitive oriented rays.  The geometric support is
non-grazing, isolated, and hyperbolic.  Reversal sends `[w]` to
`[reverse(w)]`; it is an involution and is not silently divided out.  Thus
`[01]` and `[0101]` represent the same geometric ray with traversal
multiplicities one and two, not two different primitive rays.

For a word `w`, minimize

`L(q_0,...,q_{n-1})=sum_j |q_{j+1}-q_j|`

on the compact convex product `prod_j K_{i_j}`.  A minimizer exists.  If a
minimizing coordinate were interior, the equality case of the triangle
inequality would put it on the segment between its two neighbors.  That
segment lies in the convex hull of one or two other disks and is excluded by
no-eclipse.  Thus every coordinate lies on its circle.  If two minimizers
existed, convexity would make their midpoint a minimizer; strict convexity of
each disk would put every differing midpoint coordinate in an interior,
which has just been excluded.  Hence the minimizer is unique.

The constrained first variation has zero tangential component.  Its normal
multiplier is strict because the zero-multiplier case would again put the
vertex between its neighbors.  Therefore incoming and outgoing tangential
components agree, normal components are opposite and nonzero: this is the
specular, non-grazing law.  Convexity and no-eclipse keep every open flight
segment outside all obstacles.  Conversely, the reflection law gives the
convex first-order optimality condition, so every ray iterate with the
itinerary is that unique minimizer.  If `w=u^m`, shifting the minimizing tuple
by `|u|` coordinates preserves the constraint set and length; uniqueness
forces this shift to fix the tuple.  Hence the polygon is exactly the
`m`-fold traversal of the primitive polygon for `u`.  Conversely, a smaller
geometric collision period forces the word to be a proper power.  This
proves the primitive/iterate statement rather than incorrectly identifying
different traversal multiplicities.

The convex hull of two disks is the radius-`r` capsule around their center
segment.  Its gap from the third disk is
`sqrt(3)d/2-2r`; this proves the stated chamber exactly.

In transverse optical coordinates a flight/reflection block is

`B_j=[[1,ell_j],[a_j,1+a_j ell_j]]`,

where `ell_j>0` and `a_j=2/(r cos(phi_j))>0`.  It has determinant one and
positive entries.  Any periodic product has trace greater than two and hence
real reciprocal multipliers `Lambda,Lambda^{-1}` with `Lambda>1`.

## Exact ledgers

With `A=J_3-I_3`,

- collision-marked `n`-bounce return records (including iterates whose
  primitive period divides `n`): `F_n=tr(A^n)=2^n+2(-1)^n`;
- exact-period rooted words:
  `P_n=sum_(e|n) mu(e) F_(n/e)`;
- primitive oriented geometric rays of collision period `n`: `O_n=P_n/n`;
- collision-code zeta:
  `exp(sum_(n>=1)F_n z^n/n)=det(I-zA)^(-1)
   =1/((1-2z)(1+z)^2)`;
- ray length: `n(d-2r)<=L_w<=n(d+2r)`.

At equality `d=4r/sqrt(3)` a capsule touches the third disk, so the strict
full-shift theorem is not asserted.  The ranges `2r<d<=4r/sqrt(3)`, `d=2r`,
`d<2r`, `r=0`, nonreduced words, and grazing trajectories are recorded as
separate boundary failures.

Finite evidence is regression evidence only; it does not prove geometric
coding.  The rational zeta is source-local.  No target Euler data,
root number, arithmetic clock, target functional equation, target zero
match, or Hilbert--Pólya construction is claimed.
