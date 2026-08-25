# C146 paper improvement log

No external or cross-model reviewer was available or claimed.  Both rounds
below are genuine internal theorem/scope audits; no numerical score is used.

## Round 0 to round 1

The first draft correctly exhibited the central circle and singular
derivative, but its description of the horizontal control could be read as a
nilmanifold component count.  The audit replayed the quotient fixed equation
and found the period-two class `(1/5,2/5)` with central obstruction `-4/5`.

**Fix:** explicitly separate the exact toral count from the nilmanifold fixed
set, add the counterexample, downgrade the proof status to "after weakening",
and state that the full nilmanifold component count is not asserted.

## Round 1 to round 2

The second audit found that "Lefschetz cancellation" needed an explicit
cohomology basis and that lattice preservation should include bijectivity, not
only forward integrality.

**Fix:** add the Heisenberg forms and alternating trace calculation; add the
integral inverse argument; explain why horizontal hyperbolicity makes the
central circle a connected component rather than merely a fixed subset.

## Final format and integrity audit

The final artifact is checked against the evidence hashes, scope flags, strict
Route-A tuple, fixed-epoch double compilation, embedded fonts, warning-free
logs, extracted text, and every rendered page.  Remaining limitation: no full
fixed-component enumeration and no clean-family trace regularization.
