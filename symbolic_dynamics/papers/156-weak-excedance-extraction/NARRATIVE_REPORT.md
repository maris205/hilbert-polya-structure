# P156 narrative report

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

Independent Hostile Reviews A and B are complete with zero unresolved
Critical, Major, or Minor findings.  Review B's sole Minor corrected a stale
font-row count in two author ledgers; the mathematics, source, executable
control, transcript, and four-page PDF did not change in Round 2.

## Reframed progress

The original scouting signal mixed a strong inverse theory with an appealing
but false pointwise maximum-drop clock.  Exact pressure at rank eleven found a
counterexample.  P156 therefore does not repair the clock by weakening its
wording; it removes it and reorganizes the paper around a different temporal
axis that is fully provable.

The exact image theorem is target-resolved.  A target `sigma in S_m` requires
exactly `d(sigma)` extra source coordinates, where
`d=max_i(i-sigma_i)`.  The necessity is a short but sharp chain linking the
order of selected positions to the order of selected values.  The matching
right section shifts the target above the diagonal and appends a deficient low
tail.

The every-target fibre theorem expands that section geometry.  Choosing the
selected position and value sets forces the target assignment.  What remains
is a Ferrers matching of complement values strictly below complement
positions.  Processing positions increasingly gives a closed product for
each board, and summing resolves every target and every rank, including zero
fibres.

The temporal replacement is a canonical backward system.  For a nonidentity
target of resources `(m,d)`, take its minimum-rank section.  Its high entries
have nonpositive drop, while every low-tail entry has drop exactly `m`; hence

```text
(m,d) -> (m+d,m).
```

Iteration produces an inverse ray of arbitrary depth and exact Fibonacci
matrix powers.  Every edge is minimum rank among one-step preimages, and each
lift adds exactly one forward hitting-time step.  This is substantial
temporal structure without pretending to solve the global optimization over
all forward orbits or all multi-step preimages.

## Ownership subtraction

Weak-excedance and maximum-drop statistics, bounded-drop enumeration,
permutation-tableau and Bruhat structures, generic Ferrers matching, and the
Bell enumeration of the increasing weak-excedance-letter subword all receive
zero credit.  The Bell owner is cited at theorem level.  The carrier-level
overlap with other subsequence-standardization maps is also subtracted; the
residual uses the diagonal predicate, maxdrop obstruction, deficient board,
and explicit backward resource dynamics.

## Computational role

The verifier executes 3,689,489 exact assertions.  It independently checks
literal images and fibres, the `n<m` zero-fibre and identity-only same-rank
boundaries, the Bell aggregate as a zero-credit consistency control, six
inverse levels for every nonidentity target through rank eight, and the exact
counterexample to the deleted clock. None of this finite work substitutes for
the all-parameter proofs.
