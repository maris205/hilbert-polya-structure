# Hostile audit

The mutation suite changes source locks, evaluator authority, Route-A tuple,
Route-B permission, every forbidden-data flag, threshold signs, regime labels,
critical coefficients, spectra, row populations and metadata.  Each mutation
is rehashed before checking, so rejection cannot be attributed to a stale
payload checksum.  The final rejected/total count is recorded after release.
All 28 of 28 mutations are rejected.  In particular, changing a critical
coefficient after recomputing the payload hash fails the independent algebra,
and enabling any arithmetic/operator claim fails the scope gate.
