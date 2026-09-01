# Narrative report

The vertical momentum `lambda=p_z` turns the horizontal control vector at
constant angular speed.  This makes every nonzero-`lambda` geodesic a lifted
circle and every zero-`lambda` geodesic a horizontal line.  The exponential
Jacobian factors into two elementary terms.  Its first positive zero occurs at
`|lambda|t=2*pi`, exactly where every initial horizontal angle reaches the same
nonzero vertical endpoint.

The geometric reason is planar: horizontal length is Euclidean projected
length, while the vertical coordinate is signed projected area.  Dido's
problem therefore gives the unique sub-full-turn Dido arc for a nonvertical
endpoint and a full circle for a vertical endpoint.  This proves the cut
locus, not merely a candidate Maxwell set.  It also yields the exact distance
through a unique angle `theta in (-pi,pi)` and the vertical law
`d^2=4*pi*|z|`.

The result is source-local geometry.  The horizontal controls rotate when
`lambda!=0`, but the complete geodesic drifts vertically after each horizontal
period; for `lambda=0` it is a line.  Hence no nontrivial complete geodesic is
closed and A1 is `A1_FAIL`.  The model supplies no arithmetic owner and does
not extend by assertion to general Carnot groups.
