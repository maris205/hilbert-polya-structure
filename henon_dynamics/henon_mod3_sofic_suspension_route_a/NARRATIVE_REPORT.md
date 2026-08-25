# C140 narrative report

## Outcome

C140 moves the Route-A source class from full shifts to a strictly sofic
system.  The mod-three zero-gap shift has a minimal three-state residue cover,
but its all-zero label point has three cover lifts.  Classifying that one
exception gives an exact correction at every period and a closed intrinsic
rational zeta.

## Structural progress

The progress is the separation of two owners.  `1-u-v^3` is the finite cover
determinant.  It is not, by itself, the intrinsic label inverse zeta.  Replacing
the cover's three period-three phases of the all-zero point by the single label
fixed point contributes `log(1+v+v^2)`, yielding
`Z_140=(1+v+v^2)/(1-u-v^3)`.

## Exact limits

The rational correction is not promoted to the determinant of a newly
constructed natural Fredholm operator on label space.  Nor is the dynamical
primitive product called arithmetic.  There is no target divisor or global
target structure.

## Evidence and boundary

Through period fifteen, independent enumeration finds 969 intrinsic rooted
points, 74 primitive label cycles, 60 rooted label-count cells, and 32
primitive cells.  The cover and label fixed-count sequences differ exactly as
the theorem predicts.  These are sentinels for implementation, not the basis
of the all-period proof.  Verdict:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`.
