# C191 test report

## Exact executable checks

- Producer: PASS — 272 zero-pattern rows, four positive cases, four boundary
  cases, 40 iteration rows and 28 cross-ratios.
- Independent checker: PASS — 2,411 assertions and no producer import.
- SymPy cross-check: PASS — 951 exact checks.
- Canonical replay: PASS — 154,517 bytes and exact SHA-256 match.
- Mutation suite: PASS — 242 semantic repaired-hash rejections plus one
  stale-hash rejection.

## Independence and coverage

The producer detects positive diagonals through permutation enumeration and
constructs exact rational normalization orbits.  The checker independently
uses dynamic-programming matching counts, rebuilds support/total-support/full-
indecomposability predicates, recomputes every declared scaling identity,
cross-ratio, projective coefficient, iteration error and local Gram spectrum,
and includes an asymmetric sentinel separating `S^T S` from `S^2`.

The SymPy path supplies a third implementation.  It uses Ryser permanents for
the pattern census, differentiates the logarithmic full-cycle map directly,
reconstructs the characteristic polynomials of `S^T S`, and checks all stored
exact iterations and cross-ratio invariants.

The four positive cases test exact finite scaling, Hilbert contraction data and
local singular-value rates.  The four boundary cases separately test support
without total support, total support without full indecomposability, a fully
indecomposable zero pattern, and Hall failure despite nonzero rows and columns.
None of these finite tests is used as a proof of the classical all-matrix
theorems.

Publication checks and 27-payload hash closure are recorded in
`paper/COMPILE_REPORT.md` and `C191_RELEASE_MANIFEST.json`.
