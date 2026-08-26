# C179 exact code

- `c179_zsigmondy_return_producer.py` generates the content-addressed exact
  ledger from the frozen congruence dynamics and deterministic cutoffs.
- `c179_zsigmondy_return_checker.py` reconstructs metadata, factorization,
  primality, first returns, valuations, group orders, all finite orbits,
  global fixed ledgers, and Route-A boundaries without importing producer
  code.  Claim-bearing attribution, theorem, Route-A, scope, and integrity
  objects are frozen by exact-map equality; prefixes and appended claims are
  not accepted.
- `c179_sympy_crosscheck.py` separately verifies formal source-zeta algebra,
  homogeneous cyclotomic divisibility, every recorded prime-power order, and
  representative permutation determinant and reversor matrices.
- `c179_replay.py` regenerates evidence in a temporary directory and requires
  byte identity.
- `c179_mutation.py` changes semantic fields, repairs the payload hash, and
  requires the independent checker to reject every mutation; it also tests
  one stale-hash mutation.  Its mandatory contract attacks include novelty
  attribution, appended log-(p) clock and target-operator claims, and an
  absolutized enlarged-owner impossibility claim.
- `c179_release_manifest.py` closes the 27 payload files after the final PDF
  build and excludes its own content-addressed manifest.

Run the six commands from the package root in main-README order.  Finite rows
are regression sentinels; the Markdown and paper proofs carry all unbounded
claims.
