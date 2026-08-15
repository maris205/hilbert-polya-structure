# HCS-C56 prefreeze test report

The final replay is performed by `code/run_all.sh`.  Its cold checker rebuilds
ten semantic gates independently and mutates every scalar leaf of the payload,
schema, and two envelope digests after rebinding exposed hashes.

The hostile suite covers strict JSON/schema failures, boolean-for-integer
forgeries, the complete standard-monomial box, one cold rebound mutation in
each of the eight semantic subtrees, all targeted leaf families, hostile
Singular diagnostics, optimized-Python stale-output cleanup, live and dangling
output symlinks, scoped-manifest inventory/path/self-exclusion, and the full
eight-case rollback matrix (existing/absent targets crossed with failures after
moves 1--4).  It also checks malformed promotion order/scope, symlinked
sources, foreign locks, source nonmutation, exact permission restoration, and
zero transaction debris.

Final artifact hashes and test counts are recorded in the generated checker
report and self-excluding scoped manifest; those machine files remain at
`PREFREEZE_CODE_RESULTS_PASS` until a later authorized release phase.
