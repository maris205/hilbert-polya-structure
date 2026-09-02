# Proof package — finite-field orthocenter sliding window

## Metric boundary and counts

Because `p=3 (mod 4)`, `-1` is not a square.  Hence
`x^2+y^2=0` only for the zero vector.  The dot product is anisotropic, and a
nonzero vector `(x,y)` has the perpendicular line spanned by `(-y,x)`; every
nonzero perpendicular vector is linearly independent from it.

There are `p^2` choices for the specified right-angle vertex, `p^2-1`
choices for the first side vector, and `p-1` nonzero choices on its
perpendicular line for the second side.  This gives `R` triangles right at
each ordered vertex.  A noncollinear triangle cannot have two right angles,
so the classes are disjoint.  The standard ordered-triangle count is `T`,
leaving `Q=T-3R` nonright states.

## Forward dynamics

For a nonright triangle, `A,B,C,H` are four distinct points in an
orthocentric system.  The consecutive windows are

```text
(A,B,C), (B,C,H), (C,H,A), (H,A,B), (A,B,C).
```

No shorter return is compatible with three distinct ordered vertices, so the
period is exactly four.  This identity is classical and is not claimed.

If the original triangle is right at `A`, then `H=A`; its first successor is
the valid rotation `(B,C,A)`, now right at the third coordinate, and the next
window is degenerate, so the depth is two.  If it is right at `B` or `C`,
then `H` equals that repeated coordinate in `(B,C,H)`, so it reaches the sink
in one step.  This proves the recurrent set, sharp height, depth CDF, and
stable image.  At `p=3`, the factor `p-3` makes `Q=0` without removing the
depth-two shell.

## Unique reverse window

For a target `(A,B,C)`, any nonsink predecessor must have the form

```text
(H(A,B,C),A,B).
```

The orthocentric identity proves that this candidate maps to the target.  It
is invalid precisely when the target is right at `A` or `B`, because then its
first coordinate equals `A` or `B` and the predecessor is degenerate.  It is
valid for a nonright target and for a target right at `C`.  This gives the
`0/1` target fibres directly rather than by orbit division.  Exactly the
right-at-second and right-at-third source classes map to the sink, so the
sink fibre has size `1+2R` after including the sink itself.

The combined replacement verifier checks all `433` states at `p=3` and all
`98,785` states at `p=7`; computation is bounded falsification pressure only.
