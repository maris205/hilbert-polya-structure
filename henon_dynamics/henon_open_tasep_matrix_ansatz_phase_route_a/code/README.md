# C220 code contract

The producer and checker are intentionally separate implementations.

* c220_tasep_producer.py evaluates finite DEHP words by exact rewrite and
  serializes rational rows.
* c220_tasep_checker.py rebuilds the same objects with reverse stripping
  order, exact generator residuals, and SymPy nullspaces on small sentinels.
* c220_tasep_sympy_crosscheck.py verifies the quadratic algebra, closed
  normalization, equal-rate divided difference, stationarity, and current
  identities symbolically.
* c220_tasep_replay.py checks clean-process byte identity.
* c220_tasep_mutation.py exercises repaired/stale hashes and hostile
  overclaim/schema mutations.
* c220_release_manifest.py closes the 27-payload/self-excluded-manifest
  contract and the fixed-epoch PDF checks.

The phase ledger treats coexistence as the positive-rate line
`0<alpha=beta<1/2`; `(0,0)` is checked only as a zero-rate boundary.

No script imports target arithmetic data or writes outside this package.
