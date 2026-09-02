# Deterministic control results

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

Verifier: verify.py
Canonical transcript: CANONICAL.txt
Randomness: none
External packages: none

## Coverage

The exact replay audits the 25 odd primes from 3 through 101 listed in the
canonical transcript. Total audited states: 75,993. Total assertions:
18,942,551.

A fresh Round-2 scrubbed-process replay is byte-identical to both
`CANONICAL.txt` and `verification_output.txt`; transcript SHA-256 is
`fd900d9d0c1233a265834ce7efc25c43e2c9360a5cb3bbb5eaef4d125f67d6f9`.

## Independent lanes

1. Literal one-step trajectories versus the closed product formula.
2. First-repetition orbit discovery versus the predicted cycle and tails.
3. Literal indegrees and separately parametrized labelled arms.
4. Every literal target fibre for every time from 0 through p+3.
5. Fixed sets for every time from 1 through 3p.
6. Target-partition and source-mass conservation.

Terminal profile:

    PROFILE_SHA256 b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810
    TOTAL boxes=25 states=75993 assertions=18942551
    VERDICT PASS_EXACT_REPLAY

## Limits

The replay does not establish an infinite parameter quantifier and does not
establish source ownership. Those obligations are handled by the symbolic
proof and SOURCE_VERIFICATION.md.
