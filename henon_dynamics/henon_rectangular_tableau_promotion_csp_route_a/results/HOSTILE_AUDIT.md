# C187 hostile audit

This is an internal artifact-bound audit, not external peer review and not an
independent error process.

The suite repairs the canonical payload hash after each semantic attack.  It
rejects 107 repaired-hash mutations covering identity, date, source commit,
scope, evaluator provenance, every source-lock and attribution field, the
unshifted q-hook convention, every theorem and stopping sentence, finite
cutoffs and row counts, hook/coefficient/root/period/cycle/spectrum data, every
Route-A verdict and qualification, all scope flags, both source records, and
the nonclaims.  One additional stale-hash mutation is rejected.

High-risk rejected attacks include:

- `attribution.status=NEW_THEOREM_CLAIMED`;
- adding a q-shift to Rhoades's standard-tableau polynomial;
- replacing `j^N=id` by uniform exact order `N`;
- labeling finite enumeration as the all-rectangle proof;
- changing the `2 x 2` actual order from two to four;
- promoting A0/A2/A3 or claiming a target operator;
- enabling Route B or any forbidden target-data flag.

The direct checker is algorithmically independent of the producer on small
rectangles.  SymPy supplies a third exact polynomial/cyclotomic path.  These
checks strengthen implementation confidence without becoming a new proof or
novelty certificate for the classical CSP.
