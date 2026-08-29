# Hostile mutation audit

`c238_friction_mutation.py` constructs 28 stale or hash-repaired mutations.
They alter turning points, counts, energies, release regimes, harmonic values,
general centers/phases/partial-arc counts, source/evaluator/scope locks,
Route-A flags, schema keys, forward-only well-posedness, and the positive-
friction capture hypothesis.  Every mutant is rejected by the independent
checker: `PASS 28/28`.

In particular, changing the positive exterior-rest center from `+a_f` to
`-a_f`, changing the negative phase from `pi`, or relabeling a partial first
arc as a complete half-cycle is detected after repairing the payload digest.
The suite also rejects an artificial backward-uniqueness claim and any attempt
to apply the capture quotient at `c=0`.
