# C153 hostile audit

The mutation suite repairs the canonical payload hash before testing 52
semantic changes, so rejection cannot be attributed merely to stale integrity
metadata.  It mutates the source commit, gate, clock, normalization, one-site
polynomial receipts, rank rows, alpha rows, gcd clusters, normalized limit,
period-two witness, controls, Route-A tuple, Route-B flag, and forbidden claim
flags.  A separate 53rd case intentionally leaves the payload hash stale.

The final internal hostile review also checks the following theorem risks:

- one-step rank is not substituted for power rank;
- `n=0` and `alpha=0` remain explicit identity boundaries;
- divisor classes are distinguished from equality-merged cluster values;
- fixed-period normalization is not promoted to a full secular limit;
- the moved-hole control uses its characteristic polynomial, not rank alone;
- finite ledgers are not described as proofs of all-parameter statements;
- the unitary parent does not imply self-adjointness, antiunitary symmetry,
  target matching, or Route-B readiness.

All listed risks are either proved, tested, or retained as explicit nonclaims.
