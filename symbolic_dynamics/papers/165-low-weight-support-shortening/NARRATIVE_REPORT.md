# P165 narrative report

The note begins with a conventional operation but asks a dynamical question.
At each step, the current code itself identifies every word below twice its
current minimum distance; the union of their supports is recomputed and the
code is shortened there, with ambient coordinates retained as zeros.

The one-step shortening mechanism is not the contribution.  Jibril et al.'s
hitting-set framework already owns the route from eliminating low-weight
words to increasing distance.  Once this is subtracted, the forward orbit
still carries a rigid dyadic geometry: purge supports from different times
are disjoint and their sizes grow at least as powers of two.  That yields the
sharp logarithmic height.

The inverse direction is the stronger residual.  A nonzero target is
reachable at time `t` exactly when it has both enough distance and enough
zero-coordinate capacity.  Dyadic full-support lines give a source whenever
those two conditions hold.  All sources satisfy matching dimension and new
support lower bounds.  If both bounds are tight, each purge quotient is
forced to be a pure one-dimensional line on a block of size `2^i`, which
classifies and counts the extremal layer.

The complete target fibre is not enumerated.  In particular, the zero target
is isolated: its whole time-`t` fibre includes every code absorbed by time
`t`, whereas the block formula counts only simultaneous minimizers in an
exact-depth shell.  The manuscript remains owner-thin and externally held.
