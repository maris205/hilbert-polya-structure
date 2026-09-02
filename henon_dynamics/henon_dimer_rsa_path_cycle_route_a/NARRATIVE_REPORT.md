# Narrative report

The cleanest finite description of one-dimensional dimer RSA is not a time
simulation.  It is a uniformly random order of the edges.  The first path edge
must be accepted; after its endpoints are blocked, the two surviving pieces
inherit independent uniform relative orders.  That observation closes an
exact convolution for the whole probability generating polynomial.

Summing the convolution yields a Riccati OGF.  Its specialization at `z=1` is
the geometric series, and differentiating at arbitrary order produces a
triangular hierarchy for all falling-factorial moments.  The first derivative
gives an exact alternating truncated-exponential formula for the mean.  The
second gives a closed `H_2`; its pole part at `x=1` leaves the variance slope
`e^{-4}` and constant `2e^{-4}` after the squared mean cancels.

The support has an equally finite explanation.  A maximal matching on a path
with `k` dimers has `k+1` intervening/end gaps, each containing zero or one
unmatched vertex.  Hence `2k<=n<=3k+1`, and every allowed gap word is a
construction.  On a cycle there are `k` cyclic gaps, yielding `2k<=n<=3k`.
Putting the chosen matching edges first in the scan proves that every such
maximal matching occurs with positive probability.  Nothing here says that a
greedy output is always maximum.

The first cycle edge leaves a path on `n-2` vertices, so `G_n=zF_{n-2}` exactly.
This removes the path's `-e^{-2}` mean boundary term: a same-size cycle has
`e^{-2}+o(1)` more dimers in expectation, while both geometries share occupied
fraction `1-e^{-2}` and variance density `e^{-4}`.

The executable package has separate trust lanes.  The producer uses the
convolution; the checker enumerates all edge-order prefixes through bitmasks
and separately rebuilds every factorial-moment cell.  SymPy verifies the ODE
and pole algebra, replay checks bytes in fresh paths, hostile mutations repair
hashes before trying to falsify semantics, and the manifest rebuilds all three
PDF rounds twice.  These computations audit the proof; they do not replace it.

The result is classical in ownership and non-arithmetic in Route-A content.
It supplies no prime labels, repetition law, logarithmic clock, target bridge,
or quantization.  The correct disposition is a complete standalone stochastic
theorem with Route A rejected.
