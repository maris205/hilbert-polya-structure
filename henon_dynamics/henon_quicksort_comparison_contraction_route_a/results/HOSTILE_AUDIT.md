# Hostile audit — HCS-C302

## Major proof attacks

**“A fixed-point contraction does not prove convergence of changing
subproblem sizes.”** Accepted and repaired.  The proof derives the exact
finite centered recurrence, couples the pivot grid to one uniform variable,
uses the closed variance formula for uniform `L2` boundedness, and splits the
limsup at a fixed subproblem cutoff.  Endpoint branch coefficients vanish and
the remaining term contracts by `sqrt(2/3)`, forcing the limsup to zero.

**“An `L2` fixed point cannot simply be cubed.”** Accepted and repaired.  The
binary-tree toll representation has bounded centered tolls.  Conditional
Rosenthal bounds, together with level weight sums `(2/3)^r` and `(1/2)^r`,
make the level increments summable in `L3`.  Uniqueness identifies this `L3`
law with the `L2` fixed point before its third moment is taken.

## Formula attacks

The independent integer-count lane agrees with exhaustive permutation
enumeration through `n=9`.  The SymPy lane verifies the unsimplified mean and
total-variance recurrences through `n=80`.  Beta differentiation gives
`integral C*(u^2+(1-u)^2)=1/18` and
`integral C^3=-32/3+pi^2/9+8*zeta(3)`, hence
`m3=16*zeta(3)-19`.  The first six terms of zeta already give the strict lower
bound `67/1500`.

## Machine-contract attacks

Repaired-payload attacks replaced integer coordinates/counts by JSON booleans
or integral-valued floats and appended a surplus centered group.  The checker
now requires `type(x) is int` for every archived count and coordinate, exact
keys for every row, and exact list lengths before indexed traversal.  Thus
Python's `False == 0` / `173.0 == 173` aliases and `zip` truncation cannot
hide a malformed certificate; all five attacks are retained as mutations.

## Model attacks

Empty branches and extreme pivots are retained.  Using swaps, assignments,
recursion depth, wall time, repeated keys, three-way partitions, or sampled
pivots changes the cost/model.  Dividing by `n` has the same limit away from
zero but is not the frozen finite recurrence, which divides by `n+1`.

## Collision and Route-A attacks

Hoare, Régnier, and Rösler are explicitly credited; no priority is claimed.
C291 concerns random greedy dimers, not recursive permutation splitting.  An
input-size recursion is neither recurrent dynamics nor a primitive orbit
ledger.  Its PGFs have no target arithmetic local carrier, determinant,
functional equation, divisor law, or self-adjoint zero lift.  All Route-A
rungs fail and Route B remains locked.
