# Results and evidence levels

T1--T3 are released in this directory.

- [`RESULTS.md`](RESULTS.md) gives the concise mathematical result.
- `c22_certificate.json` is the deterministic exact-rational producer
  artifact.  It contains all 78 matched branch comparisons (156 local orbit
  enclosures), joint combinatorics through period ten, symmetry controls,
  and symbolic T3 checks.
- `c22_independent_check.json` is the hash-bound checker artifact.  Its checker
  imports no producer code.
- [`TEST_REPORT.md`](TEST_REPORT.md) records the clean commands and outcomes.
- [`ARTIFACT_HASHES.sha256`](ARTIFACT_HASHES.sha256) freezes the released
  producer, checker, tests, and result bytes.

Evidence labels:

- T1 common survivor: `PROVED`;
- T2 aggregate separation: `NUMERICALLY_CERTIFIED` by exact rational interval
  arithmetic and an independent implementation;
- T3 unit-numerator global residue collapse: `PROVED`;
- T4/T5 analytic operator: `OPEN`.

Every artifact distinguishes the local real survivor from the global complex
scheme and distinguishes signed, absolute, and instability weights.
