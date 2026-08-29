# C237 hostile audit

The mutation harness creates 32 independent deep-copy mutants and repairs the
payload hash where appropriate.  Every mutant is rejected by the independent
checker:

- stale hash, unknown top-level/regression/row keys;
- source, evaluator, scope and Route-A/Route-B lock drift;
- matrix theorem, \(L^2\) boundary, identity, citation and nonclaim drift;
- altered matrix, covariance, correlation, rate, critical flag, Kalman and
  Gibbs values;
- altered all five boundary rows (classification, stationarity, mixing,
  parameters, case identity and variance) and truncated transition ledger.

Result: `C237 hostile mutation rejection: PASS 32/32`.  This is an internal
schema and numerical audit, not external peer review.
