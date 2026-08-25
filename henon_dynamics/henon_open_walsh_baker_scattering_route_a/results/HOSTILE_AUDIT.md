# C148 hostile and boundary audit

The mutation suite contains 40 registered semantic corruptions whose canonical
payload hash is repaired before checking, plus one stale-hash control.  It
covers the DFT/projector/order/shift locks, clock and determinant convention,
one-qutrit receipts, the rejected and corrected ranks, `B_k^k`, gcd traces,
polynomial coefficients and supports, primitive paths, defect ranks, all three
controls, symmetry restraint, Route-A tuple, Route-B flag, and forbidden claim
flags.  All 41 cases are rejected.

The suite is not claimed to enumerate every possible corruption.  It proves
that the registered semantic changes fail even when the outer hash is valid.

Failure-mode findings retained in the release:

- one-step rank is `2*3^(k-1)`, not `2^k`;
- the `2^k` escape rank occurs only after the full `k`-step factor cycle;
- the projector-order control is isospectral and cannot support a false
  geometry-sensitive spectral claim;
- a changed hole position really does change the linear secular coefficient;
- the primitive product is a complex-amplitude basis-path product, not an
  arithmetic factorization;
- the raw path product has only the stated local absolute domain;
- finite `k` gives neither self-adjointness nor semiclassical target matching;
- antiunitary symmetry, target structure, Hilbert--Polya, and Route B remain
  nonclaims.

Verdict: PASS within `NO_BAD_EULER_OR_ROOT_NUMBER`.
