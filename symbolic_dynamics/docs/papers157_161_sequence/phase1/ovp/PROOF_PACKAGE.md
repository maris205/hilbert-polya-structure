# Proof package — parallel odd-vertex pruning

## Lemma A: parity deletion and recurrence

The odd-degree set of a finite graph has even cardinality.  A nonfixed step
therefore removes at least two vertices, whereas an all-even graph is fixed.
Strict vertex loss rules out every nontrivial cycle.  This proves recurrence,
the upper clock bound, and—using the endpoint peeling of `P_n`—sharpness.

Boundary controls: the empty graph and every singleton are fixed; the formula
`floor(n/2)` is zero for `n=0,1`.

## Lemma B: strict predecessor count

For a target on `S` and a deleted set `D`, retain the target edges on `S` and
write one binary variable for every edge meeting `D`.  The conditions “`S`
even, `D` odd” are the incidence equations displayed in
`DERIVATION_PACKAGE.md`.  The variable graph is connected for `d>0`, so its
incidence rank over `F_2` is `s+d-1`.  The only consistency condition is that
the right-side sum vanish, equivalent to `d` even.  Rank-nullity proves the
fixed-`D` power of two; choosing `D` proves `B_n(s,m)`.

The `s=0,d=2` boundary has one variable and one independent equation, hence
one predecessor, agreeing with the exponent zero.  There is no strict
predecessor for odd `d`.

## Lemma C: transfer powers

A strict predecessor is non-even because its deleted set is nonempty and
odd-degree.  Thus every reverse strict chain corresponds to exactly one
forward active orbit segment.  Induct on chain length: after conditioning on
the first source rank `m`, Lemma B supplies `B_n(s,m)` choices independent of
the target edges, and the induction hypothesis supplies the next matrix
factor.  This proves `B_n^t`.

For an even target, the unique orbit can reach it after `k<=t` active steps
and then remain there; the disjoint cases sum to `I+B_n+...+B_n^t`.  For a
non-even target, early arrival is impossible, so only `k=t` occurs.

## Corollaries

- `B_n` is strictly upper triangular and nilpotent.
- The exact image test follows from positive even rank increments.
- The phase, fixed, image, CDF, and shell formulas follow by summing over
  target ranks and using the cycle-space count of even labelled graphs.
- All periodic points are fixed and the Artin--Mazur zeta function is
  `(1-z)^(-|Fix F|)` if retained in the manuscript; this is bookkeeping, not
  a contribution axis.

## Computational falsification boundary

`verify_ovp_focused.py` constructs all 41,658 states through ambient order
six (40,069 at order six alone).  It compares literal iterates with every
target transfer formula at every relevant time, checks images, fixed counts,
the CDF, and the path witness.  Its 1,350,807 passing assertions are evidence
against small counterexamples, not a proof or owner certificate.
