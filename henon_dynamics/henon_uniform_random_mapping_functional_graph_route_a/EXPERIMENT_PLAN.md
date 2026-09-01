# Exact-computation plan

## Claims under test

1. The cycle–component count agrees with exhaustive functional-graph
   decomposition, including `n=1` and the pure-permutation face `k=n`.
2. Summing the component refinement yields the exact cyclic-vertex law, and
   direct cycle counting yields every expected cycle count.
3. The marked tail/cycle formula agrees cellwise with enumeration and its
   collision-length marginal equals the cyclic-vertex marginal.
4. Collision-product samples approach the proposed one- and two-dimensional
   square-root limits.

## Evidence design

- Enumerate every one of `n^n` labelled maps for `1<=n<=7`: 873,612 maps.
- Record all 84 admissible `(C_n,K_n)` cells, all 84 marked `(mu,lambda)`
  cells, and 28 aggregate cycle-length cells.
- Generate exact formula atlases for `1<=n<=32`: 528 cyclic probabilities,
  560 collision-survival probabilities, and 528 cycle-expectation values.
- Record 16 one-dimensional and 12 joint high-precision scaling receipts.

## Independence and hostility

The checker traces every starting orbit and canonicalizes cycles, whereas the
producer uses a color walk; it does not import the producer.  SymPy verifies
normalizations, determinants, and cycle expectations independently.  Replay
requires a fresh producer to reproduce the evidence byte for byte.  Every
hostile mutation repairs `payload_sha256` before the checker is invoked, so a
stale digest cannot be the rejection mechanism.

## Evidence boundary

Finite enumeration does not prove a theorem for arbitrary `n` or a scaling
limit.  The analytic owners are the functional-graph decomposition, the rooted
forest determinant, ordered-prefix counting, and the collision-product limit.
