# Narrative report

C301 advances the dynamics roadmap by changing subtype rather than subdividing
an earlier paper.  The state is an entire labelled set partition, and one time
step fragments all blocks simultaneously.  This makes the Bell-number matrix
look forbidding, but the correct state variable is each label's accumulated
binary word.  After `t` rounds, equality of words is exactly membership in the
same terminal block.  That observation solves the full transition semigroup in
one line.

The same coupling makes three formerly separate questions identical to finite
occupancy.  A particular `k`-block partition is realized by injectively
assigning `k` binary words; the number of blocks is the number of occupied word
boxes; absorption is the birthday event that all `n` words are distinct.  This
produces complete finite-time distributions, not only expectations or bounds.

The spectral result required a separate idea.  Refinement orders the transition
matrix triangularly, revealing eigenvalues and algebraic multiplicities, but
that alone cannot rule out Jordan blocks.  The rank filtration has scalar
successive quotients with distinct scalars.  Each matching factor lowers the
filtration, so their product annihilates the matrix.  The resulting squarefree
polynomial proves diagonalizability over the rationals.

At the scale `2^t` comparable with `n^2`, the absorption law converges to the
birthday probability `exp(-lambda/2)`.  Integer time leaves a dyadic phase, so
the theorem is stated along sequences where `n^2/2^t` converges.  This avoids a
false phase-free continuous limit.

The research result is mathematically complete but Route-A negative.  The
chain is absorbing and has no nonconstant recurrent cycles.  Its determinant
is finite and source-local, with no arithmetic local carrier, prime clock,
target functional equation, divisor law, or self-adjoint zero lift.  This
negative evaluation is part of the result rather than an omitted ambition.
