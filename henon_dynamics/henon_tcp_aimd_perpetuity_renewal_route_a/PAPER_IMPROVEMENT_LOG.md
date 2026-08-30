# Paper improvement log

## Round 0 -> Round 1

Replaced the initial scaffold with the linear-rate AIMD
generator, pre-jump hazard equation, and the square-affine recurrence carrying
the explicit (2a/\rho) factor.

## Round 1 -> Round 2

Added contractive uniqueness/convergence, q-product and all-order squared
moments, generator recurrence, and the stationary Markov-renewal/Palm reward
formula.  The text now explicitly says that positive-beta jump cycles are not
iid regenerative; beta=0 is the sole reset face.

## Release-integrity correction

Route-A is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, the q-product is
source-local probability data rather than an Euler factor, and all source,
evaluator, epoch, scope, replay, and mutation locks are closed.
