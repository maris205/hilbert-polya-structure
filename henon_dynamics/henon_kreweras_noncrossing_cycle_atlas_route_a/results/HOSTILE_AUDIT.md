# Hostile audit

The payload hash is recomputed from canonical JSON bytes.  Mutations cover the
schema/identity lock, evaluator and scope lock, source-clock and attribution
claims, theorem strings, row coordinates, fixed values, period populations,
cycle/zeta/determinant factors, spectral multiplicities, rank counts, q
coefficients/hashes, and stale-hash tampering.  Every mutation is rejected by
the independent checker.  A mutation that changes a value without changing
the payload hash is also rejected.

The audit does not attempt to prove the imported all-(n) CSP; it tests that
the release does not silently alter the declared source theorem or its finite
consequences.
