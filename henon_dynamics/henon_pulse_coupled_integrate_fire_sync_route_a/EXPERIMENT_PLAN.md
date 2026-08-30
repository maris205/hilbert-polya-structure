# Deterministic experiment and audit plan

## Frozen event census

Use (r=1/2,2/3,3/4), (epsilon=1/5,1/4,1/3), and (N=2,ldots,8).
For each parameter tuple, enumerate seven fixed rational initial seeds and
iterate twelve event maps.  The transformed state is (u_i=e^{-aphi_i}),
with (u_iin[r,1]).  The next threshold uses the exact scale
(r/min_i u_i); each avalanche pulse subtracts
((1-r)epsilon) and clips at (r).  Queue order is index-canonical.

## Independent computation

`c245_pulse_if_checker.py` reimplements the state map, avalanche closure,
equality clusters, cycle detection, and all expected rows without importing
the producer.  `c245_pulse_if_sympy_crosscheck.py` checks the rise inverse,
threshold scaling, pulse algebra, and primitive one-event word.  The replay
script compares two fresh producer byte streams with the checked receipt.

## Adversarial controls

The mutation suite applies 41 repaired-hash or stale-hash edits to event states,
avalanche generations, cluster counts, cycle labels, metadata, identities,
citations, route tuple, scope flags, and unknown keys; every changed receipt
must be rejected.  No mutation is allowed to be a no-op.

The finite ledger establishes exact rational event progress and the stated
cluster/synchrony facts at the declared cutoff.  It does not turn a finite
probe set into a global continuous-state synchrony theorem.
