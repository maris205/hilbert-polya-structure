# Results: HCS-C360

- Canonical evidence SHA-256:
  `58508bebd3abefb35192569cb7dab4c2a2e0fe71ac842f4a8351192c3bd26376`.
- Canonical payload SHA-256:
  `61ad52105de3ee33b0bd97c7c3c57b974a95b3e310450ba7f6a68571c410c751`.
- Evidence size: 20,314 bytes.
- Exact receipts: 12 curvature rows, 14 anisotropy-chart rows, 18 lifespan
  rows, 12 normalized-flow rows, and seven boundary rows.
- Independent checker: PASS, 95 checks.
- SymPy: PASS, 26 exact identities.
- Isolated replay: PASS, two byte-identical copies.
- Hostile audit: PASS, 60 of 60 attacks rejected.
- Route-A tuple:
  `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

The receipts audit equations and serialization.  The paper's maximal-interval,
Type-I, and convergence statements rest on analytic proof, not enumeration;
the symbolic lane independently verifies both nonzero scaled-curvature limits.
