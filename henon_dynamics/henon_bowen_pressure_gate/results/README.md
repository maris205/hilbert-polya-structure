# HCS-C31 results

The exact certificate proves that the unique zero \(h_*\) of the H6
adapted-roof Bowen pressure satisfies

\[
0.277980<h_*<0.277987.
\]

The proof covers all 1156 length-13 cylinders of the genuine chronological
four-state shift. It does not infer a full-word result from isolated periodic
orbits and does not average transition matrices.

- `c31_certificate.json`: exhaustive cylinder intervals and rational Collatz
  witnesses;
- `c31_independent_check.json`: six-gate independent verification record;
- `RESULTS.md`: mathematical result and scope;
- `VALIDATION_REPORT.md`: checker contract;
- `TEST_REPORT.md`: regression and mutation coverage;
- `ARTIFACT_HASHES.sha256`: frozen hashes for all 40 authored release files.

Reproduce from the project directory with `./code/run_c31.sh`.
