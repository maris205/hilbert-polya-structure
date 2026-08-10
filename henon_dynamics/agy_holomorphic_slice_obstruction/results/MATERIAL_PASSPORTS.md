# HCS-C26 material passports

## `c26_certificate.json`

- Origin: `code/c26_producer.py`
- Origin Mode: exact producer
- Date: 2026-08-10
- Evidence Status: `NUMERICALLY_CERTIFIED` for the finite exact arithmetic;
  `CONDITIONAL_THEOREM` for the point-evaluation conclusion; `PROVED`
  theorem metadata with exact inputs for the positive-prefix complex-cone
  and Perron/characteristic identities
- Verification: independently replayed
- Version: `c26_exact_certificate_v1`

The JSON contains exact integer matrices and rational numbers.  Its
`UNVERIFIED_UNTIL_INDEPENDENT_CHECK` producer label is intentional; release
verification is carried by the separate checker artifact.

## `c26_independent_check.json`

- Origin: `code/c26_independent_check.py`
- Origin Mode: independent validation
- Date: 2026-08-10
- Evidence Status: `NUMERICALLY_CERTIFIED`
- Verification Status: `VERIFIED`
- Version: `c26_independent_check_v1`

The checker shares no producer import.  It reconstructs the mathematical
object from literal constants and separately verifies all exact outputs.
Its projective trace check uses a centered high-precision finite difference,
not the producer's analytic derivative implementation.

## C26 theorem bases

- Positive-prefix complex-cone lemma: the exact strictly positive matrix
  `P`, normalized-column margin, and Birkhoff coefficient are verified in
  both implementations.  The common-domain conclusion is theorem-based;
  no sampled complex points are used as proof.
- Perron/characteristic projective trace identity: proved by the Perron
  eigenline splitting in complex projective dimension three.  Three exact
  word examples validate formulas.  The two-return pair is explicitly
  limited to matrix-order bookkeeping because AB/BA have the same
  characteristic polynomial; the three-return noncyclic reversal is the
  spectral chronology sentinel.  Neither finite check is the general proof.

## External theorem dependencies

- C24 discrete-metaplectic-atom essential-norm theorem:
  `PROVED` in `../rauzy_metaplectic_obstruction/THEOREM_PACKAGE.md`, not
  reproved here.
- C25 AGY absolute branch summability and fixed-start all-length decoder:
  `PROVED` in `../agy_metaplectic_transfer_obstruction/THEOREM_PACKAGE.md`,
  not reproved here.
- Generic bounded literal transfer, constant embedding, and evaluation:
  explicit hypotheses of the point-evaluative theorem, not automatic for an
  arbitrary anisotropic space.
- Concrete vector Bergman realization
  `A^2(Omega;L^2(R^2))`: `PROVED` bounded by the common compact branch image
  and the summable complex weights; constants and interior evaluation are
  bounded.  The resulting operator is noncompact by the C24/C25 slice.
- Concrete scalar Bergman realization: `PROVED` trace class by the verified
  Bandtlow--Jenkinson hypotheses, with trace-norm word expansion and an
  ordinary Fredholm determinant.

## Human-readable reports

- `RESULTS.md`: interpretation and theorem boundary
- `VALIDATION_REPORT.md`: independent replay
- `TEST_REPORT.md`: mutation coverage
- `README.md`: bundle index

These reports do not upgrade conditional or external inputs to newly proved
claims.
