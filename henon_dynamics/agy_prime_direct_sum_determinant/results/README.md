# HCS-C28 result artifacts

- `c28_certificate.json` — source-locked exact producer certificate;
- `c28_independent_check.json` — implementation-independent replay;
- `RESULTS.md` — mathematical result and claim boundary;
- `VALIDATION_REPORT.md` — theorem/computation separation and independent gates;
- `TEST_REPORT.md` — regression, mutation, and portability tests;
- `MATERIAL_PASSPORTS.md` — origin and verification status of every input;
- `ARTIFACT_HASHES.sha256` — frozen release manifest.

All arithmetic decisions are exact.  The code performs no floating-point
eigenvalue computation, Riemann-zero fit, new prime-window scan, or fitted
normalization.
