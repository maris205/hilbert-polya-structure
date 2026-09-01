# Narrative report — P147

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

## Outcome

The candidate crossed the paper threshold on two independent axes.  Its time
axis is not merely termination: the largest depth is exactly
`floor(log2 n)` for every total, and the proof identifies a weight-doubling
dependency chain.  Its inverse axis is complete and target resolved: every
predecessor of `(b_1,...,b_k)` corresponds uniquely to a path through the
divisor sets of the target parts, with adjacent divisor choices unequal.

## Why the signal survived subtraction

The fixed states are Carlitz compositions, and equal-run statistics are
classical.  Those facts were removed before scoring.  Ordinary run-length
encoding was also rejected as an ownership shortcut because it outputs
value/count pairs and changes representation, whereas the present map takes
their product, preserves total weight, and iterates on a fixed finite carrier.

The residual is the conjunction of:

- a literal simultaneous coarsening map on `Comp(n)`;
- a sharp every-size logarithmic clock with a constructive witness; and
- a complete length-refined one-step fibre atlas.

The closest internal composition paper refines balanced blocks and uses a
suffix decoder; neither its literal update nor its proof engine transfers.
The external ledger also subtracts the closest recent random weak-composition
evolution and static Arndt--Carlitz neighbours.  Neither owns the literal
iteration, sharp clock, or target-resolved fibre package.

## Proof status

The all-parameter claims have deductive proofs in `main.tex`.  Exact
enumeration is used only to pressure the map, clock, equality witness, fixed
criterion, and every target fibre in each exact-total layer through total 18.
The frozen cold replay passes 2,690,869 assertions.  Review B independently
replayed the witness through `n=100000`, rebuilt the current four-page PDF
byte for byte in isolation, and inspected all four pages without defect.

Hostile Review A's 0 Critical / 1 Major / 3 Minor findings were repaired;
Hostile Review B accepted with 0 / 0 / 0 surviving findings.

## External boundary

The primary-source search was bounded and terminology dependent.  No novelty,
priority, authorship, submission, or release claim is made.  The internal
paper decision is **ROUND-2 INTERNAL REVIEW ACCEPTED**, while external status
remains `HOLD_EXTERNAL`.
