# Paper improvement log

## Round 0 -> Round 1

Replaced the initial scaffold with the exponential rise law, transformed
event coordinates, pulse clipping rule, and a precise same-time avalanche
definition.  The first revision adds the exact rational event-map theorem.

## Round 1 -> Round 2

Added the equality-partition coarsening proof, the absorbing all-equal cluster,
the primitive event word `[N]`, and the finite (N\leq8) receipt.  The
Mirollo--Strogatz statement is explicitly kept as cited almost-everywhere
context rather than a claim of exhaustive continuous-state enumeration.

## Release-integrity correction

Route-A was fixed to `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
event words are source-local and no target determinant is implied.  The source,
evaluator, epoch, scope, mutation, and byte-replay locks are all recorded.
