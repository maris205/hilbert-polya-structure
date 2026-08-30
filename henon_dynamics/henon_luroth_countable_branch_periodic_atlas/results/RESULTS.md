# C241 results

The exact receipt covers 11 branch rows, 780 finite-word rows, 30 necklace
rows, 88 weighted rows, 3 convergence-limit rows, and 2 finite primitive-factor
rows.  Word fractions, itineraries, least periods, and multiplier products are
recomputed independently.  The branch image is recorded as \((0,1]\); the
excluded left endpoint explains why 0 is not counted as a branch image.

The full weight sum converges absolutely for \(\Re(s)>1/2\).  Rows at
\(s=1/2\) mark divergence.  The absolute primitive product/log domain is the
strict intersection \(\Re(s)>1/2\) and \(|z|A(\Re(s))<1\), while
\(1/(1-zA(s))\) is only a meromorphic continuation away from denominator
zeros in that half-plane.  At \(s=1\), \(A(1)=1\), \(z=1\) is a pole, and
the exact tail beyond cutoff \(M\) is \(1/M\).

Route-A: `A0_FAIL`, `A1_PASS_ANALYTIC`, `A2_FAIL`, `A3_FAIL`,
`A4_FORMAL_HINT`; overall `ROUTE_A_REJECTED`.  This source-local result does
not claim target prime/zero data or any arithmetic correspondence.
