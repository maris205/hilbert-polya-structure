# Results and evidence levels

T1--T4 and the orbitwise scalar-T5 gate are released in this directory.

- [`RESULTS.md`](RESULTS.md) gives the concise mathematical result.
- [`T4_T5_RESULTS.md`](T4_T5_RESULTS.md) gives the T4 convergence theorem,
  common complex/projective domains, and orbitwise scalar trace obstruction.
- `c22_certificate.json` is the deterministic exact-rational producer
  artifact.  It contains all 78 matched branch comparisons (156 local orbit
  enclosures), joint combinatorics through period ten, symmetry controls,
  and symbolic T3 checks.
- `c22_independent_check.json` is the hash-bound checker artifact.  Its checker
  imports no producer code.
- `c22_t4_certificate.json` and `c22_t4_independent_check.json` are the exact
  producer/checker artifacts for the T4 and orbitwise scalar-T5 round.
- [`TEST_REPORT.md`](TEST_REPORT.md) records the clean commands and outcomes.
- [`ARTIFACT_HASHES.sha256`](ARTIFACT_HASHES.sha256) freezes the released
  producer, checker, tests, and result bytes.

Evidence labels:

- T1 common survivor: `PROVED`;
- T2 aggregate separation: `NUMERICALLY_CERTIFIED` by exact rational interval
  arithmetic and an independent implementation;
- T3 unit-numerator global residue collapse: `PROVED`;
- T4 intrinsic Euler determinant: `PROVED` in an explicit nonzero domain;
- T5 common base/projective/log domains: `PROVED`;
- T5 orbitwise scalar denominator cancellation: `REFUTED` under the frozen
  convention; aggregate scalar compensation is not excluded;
- graded exterior nuclear complex: `OPEN`.

Every artifact distinguishes the local real survivor from the global complex
scheme and distinguishes signed, absolute, and instability weights.
