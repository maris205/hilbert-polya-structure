# C135 narrative report

C130 used a nonlattice roof with one value per symbol.  Its determinant was
exact and all-period, but every orbit with the same symbol population shared a
clock sector.  C135 asks for the smallest exact refinement that can see how
symbols transition.

The roof assigns `1,sqrt(2),sqrt(3),sqrt(6)` to the four directed binary
edges.  These numbers form a rational basis, so suspension time uniquely
determines the complete directed-edge-count vector.  The formal two-state
matrix retains an explicit determinant and its logarithmic trace expansion
gives the primitive product at every period.

The requested period-six control is decisive.  `000111` has edge vector
`(2,1,1,2)`, whereas `001011` has `(1,2,2,1)`.  Their exact length difference
is `1-sqrt(2)-sqrt(3)+sqrt(6)`, which is nonzero.  The corresponding rooted
trace coefficients are six and twelve.

The refinement does not recover individual orbits.  `001011` and `001101`
are distinct primitive necklaces with the same vector `(1,2,2,1)`.  This is
not an incidental prefix defect: every binary closed word has `N01=N10`, so
periodic data can see only the sum of the two off-diagonal roof values.

The evidence enumerates 2,046 rooted words and 226 primitive cycles through
period ten.  It includes 2,121 independent checker assertions, 37 SymPy
checks, byte replay, and 43 hostile mutations: 42 repaired semantic hashes
plus one stale-hash case.  The theorems themselves have no cutoff.

The result is a sharper internal clock, not a target-facing or arithmetic
determinant.  It supplies no natural self-adjoint lift or Route-B authorization.
