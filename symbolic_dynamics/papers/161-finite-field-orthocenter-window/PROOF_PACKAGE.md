# Proof package — P161

## Claim

For every prime `p=3 mod 4`, the totalized orthocenter window on all ordered
noncollinear triangles in `F_p^2` plus a sink has the period, oriented-depth,
target-fibre, image, zeta, and `p=3` boundary formulas in Theorem 1 of
`main.tex`.

## Status

**PROVABLE AS STATED.**  The all-prime theorem survives unchanged.  The
orthocentric quartet and finite-field metric geometry remain zero-credit
background.

## Assumptions and notation

- `p` is prime and `p=3 mod 4`.
- `V=F_p^2` has dot product `(x,y) dot (u,v)=xu+yv`.
- A carrier triangle is ordered and noncollinear.
- `H(A,B,C)` is the unique common point of the altitudes.
- A degenerate successor window goes to the fixed sink `dagger`.
- `T`, `R`, and `Q` have the meanings in the frozen contract.

## Dependency map

1. Anisotropy gives the perpendicular-line count and prevents overlapping
   right-angle classes.
2. Altitude symmetry gives the classical orthocentric quartet and the unique
   reverse candidate.
3. Direct substitution of `H=A,B,C` gives the three oriented depth strata.
4. Reverse-candidate validity gives every triangle fibre; degenerating source
   classes give the sink fibre.
5. The image tower, CDF, zeta, and `p=3` boundary follow by exact counting.

## Proof

### 1. Anisotropy, existence, and counts

Since `-1` is not a square modulo a prime `p=3 mod 4`,
`x^2+y^2=0` forces `(x,y)=0`.  Thus every nonzero vector `u=(x,y)` has the
one-dimensional perpendicular space spanned by `(-y,x)`, and `u` is not
parallel to any nonzero member of this space.

Choose `A` in `p^2` ways, `B-A` in `p^2-1` ways, and `C` off the `p`-point
line `AB` in `p^2-p` ways.  This gives `T`.  For a right angle at a specified
coordinate, choose the vertex, a nonzero first side, and one of `p-1`
nonzero vectors on its perpendicular line.  This gives `R` and always yields
a noncollinear triangle.

For disjointness, write `u=B-A`, `v=C-A`.  If a triangle were right at both
`A` and `B`, then

~~~text
u dot v=0,
(-u) dot (v-u)=0,
~~~

so `u dot u=0`, contradicting anisotropy.  Relabeling handles the other
pairs.  Hence the nonright count is `Q=T-3R`.

The coefficient vectors in the two altitude equations are independent for a
noncollinear triangle.  Nondegeneracy of the dot pairing therefore gives a
unique orthocenter.  Subtracting the first two scalar-product equations also
gives the third altitude equation.

### 2. Orthocentric quartet and exact periods

Let `H=H(A,B,C)`.  The three altitude perpendicularities for `H` become the
altitude perpendicularities for `A` with respect to `(B,C,H)`.  Uniqueness
therefore gives `H(B,C,H)=A`; cyclic relabeling yields the four windows

~~~text
(A,B,C), (B,C,H), (C,H,A), (H,A,B), (A,B,C).
~~~

This is the classical orthocentric identity, reproduced only to close the
finite-field proof.

The equality `H=A` is equivalent to a right angle at `A`: one implication is
read from the altitude through `B`, and the other follows because `A`
satisfies both altitude equations.  The same holds at `B,C`.  Thus for a
nonright triangle the four points are distinct.

No three are collinear.  For example, suppose `H=A+lambda(B-A)` lies on
`AB` with `lambda` distinct from zero and one.  Put `u=B-A`.  The altitude
through `A` and the third altitude imply respectively

~~~text
u dot (B-C)=0,
(A-C+lambda u) dot u=0.
~~~

The first equation gives `u dot (A-C)=-u dot u`; the second then gives
`(lambda-1)u dot u=0`.  Anisotropy forces `lambda=1`, a contradiction.
The other triples follow by relabeling.  Hence every displayed window is a
carrier triangle.  Equality of the ordered tuple at time one, two, or three
would force two of `A,B,C` to coincide.  The exact period is four.

### 3. Oriented singular depths

For a triangle right at its first coordinate `A`, `H=A`; hence its successor
is the valid cyclic rotation `(B,C,A)`, now right at coordinate three.  The
next window repeats `A` and reaches the sink.  Its depth is two.

If the triangle is right at the second coordinate, `H=B`, and `(B,C,B)` is
degenerate.  If it is right at the third, `H=C`, and `(B,C,C)` is
degenerate.  Both depths are one.  The sink is fixed.  Since `R>0`, the
height two is sharp.  These counts immediately give the three CDF values.
The recurrent set is the sink plus `Q` states in `Q/4` four-cycles, giving
the zeta product.

### 4. Unique reverse window and fibres

Suppose a nonsink predecessor maps to target `(A,B,C)`.  It must be
`(D,A,B)` and must have orthocenter `C`.  Applying the orthocentric identity
to this predecessor forces `D=H(A,B,C)`.  There is at most one candidate:

~~~text
(H(A,B,C),A,B).
~~~

If the target is right at `A` or `B`, the candidate repeats that vertex and
is not a triangle.  If it is right at `C`, the candidate is `(C,A,B)`, a
cyclic rotation of the target, and is valid.  If the target is nonright, the
no-three-collinear result makes it valid.  Orthocentric symmetry proves that
each valid candidate maps back to the target.  Thus target fibres are zero
for right-at-first/second targets and one for right-at-third/nonright targets.

The sink predecessors are the sink itself and exactly the sources right at
their second or third coordinate, totaling `1+2R`.  Reading the positive
fibres gives the one-step image.  The right-at-third part maps to the sink,
while the nonright core permutes, so the second image is stable and has size
`1+Q`.

### 5. Boundary prime

At `p=3`, the factor `p-3` gives `Q=0`, but `R=144>0`.  Substitution gives
`T=432`, one-step image size `145`, stable image size one, sink fibre `289`,
and depth counts `1,288,144`.  Therefore the periodic triangle core is empty
without collapsing the height-two shell.

## Corrections or missing assumptions

None.  The restriction `p=3 mod 4` is essential; the proof does not extend
silently to isotropic planes.

## Open risks

- The classical quartet and finite-field setting must continue to receive
  zero contribution credit.
- Guy's trisequence is an iterative neighbor but not the literal map; the
  distinction must remain explicit.
- A direct owner of the singular/fibre conjunction would trigger further
  subtraction or kill.
