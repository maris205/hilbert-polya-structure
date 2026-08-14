# HCS-C55 test report

The test suite contains 15 test methods and includes:

- a full valid producer/checker replay with exact executed-gate equality;
- exhaustive same-type mutation of all 292 central semantic scalar leaves
  while both payload and schema digests are rebound;
- the exact `1589 = 292 + 1296 + 1` disjoint scalar classification;
- explicit negative mutations for motive, honest-CY3, fixed-Hilbert,
  literal-family, contracted-class multiplication, `Q(2)`, all-24-rational,
  and the erroneous `D(z)=rho^2 z` overclaims;
- mutations of redundant committed provenance, the complete tangent-operator
  subtree, direct-cube metadata, common top scale, and producer smoothness;
- duplicate-key, unknown-key, exact-type, optimized-Python, and stale-output
  fail-closed controls;
- eight generic grouped-promotion rollback injections (existing or initially
  absent targets crossed with failures after each of moves 1, 2, 3, and 4),
  zero `.new`/`.bak` residue checks, and a successful four-target control;
- runner guards requiring `--refresh-manifest` with `--refresh-results`, plus
  a live default replay after every refresh.

The release runner executes the producer, checker, and all tests from a
temporary directory before certificate, check, and persistent scoped manifest
are atomically replaced.  The default runner verifies that persistent scoped
identity; the already-current full manifest is verified separately with
`c55_hash_manifest.py --full-only`.
