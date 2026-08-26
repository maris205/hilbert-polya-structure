# C188 hostile audit

This is an internal artifact-bound adversarial test, not external peer review
and not an independent error process.

The suite changes a semantic field, repairs the canonical payload hash, and
requires the independent checker to reject the result.  All 137 repaired-hash
attacks are rejected, together with one stale-hash control.

Attacked surfaces include:

- identity, date, source commit, evaluator authority and scope;
- every source-lock and attribution field, including the max-times/max-plus
  logarithmic convention bridge;
- both source records and their ownership roles;
- every theorem, boundary, Route-A qualification and nonclaim;
- matrix IDs, tags, dimensions, supports, weights and normalizations;
- cycle means, critical edges/SCCs, cyclicity and exact transients;
- `C,S,R`, periodic powers, vector/projective periods and attraction divisors;
- the fixed-support unbounded-transient family;
- the reducible multirate witness and all population counts.

The first hostile run exposed that `dimension` and related row metadata were
derivable but not exact-matched.  The checker contract was strengthened before
release; the complete suite then passed.  This is recorded as an internal
repair, not concealed as a first-pass success.
