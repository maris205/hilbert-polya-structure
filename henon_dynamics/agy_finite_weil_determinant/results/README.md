# HCS-C27 results

- `c27_certificate.json` — complete producer output, including exact
  `(1,G_p)` characters, six local polynomials, the power scan, the complete
  p=43 fibre-polynomial collision, the integral conjugacy, and all 150
  arithmetic rows.
- `c27_independent_check.json` — independent replay that does not import the
  producer.
- `RESULTS.md` — mathematical result summary.
- `VALIDATION_REPORT.md` — independent and theorem/finite-scan boundaries.
- `TEST_REPORT.md` — regression and mutation-test inventory.
- `MATERIAL_PASSPORTS.md` — source and artifact provenance.
- `ARTIFACT_HASHES.sha256` — frozen integrity manifest covering 40 project
  artifacts, including theorem/source documents, code, certificates, Route-A
  records, paper source, and the compiled PDF.

All exact character pairs are stored in the basis `(1,G_p)`, with
`G_p² = Legendre(-1,p) p`. The finite bridge scan is explicitly marked as
finite evidence; the fixed-prime Fredholm theorem and integral symplectic
conjugacy are exact results.

`code/run_c27.sh` checks regenerated output against the frozen manifest. It
does not silently refresh expected hashes.
