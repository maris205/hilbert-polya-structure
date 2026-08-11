# HCS-C29 results

The Phase-2 release is anchored by two machine-readable artifacts:

- `c29_certificate.json`: deterministic exact producer certificate;
- `c29_independent_check.json`: separate fail-closed reconstruction and audit.

Human-readable result files:

- `RESULTS.md`: mathematical findings and interpretation;
- `VALIDATION_REPORT.md`: checker gates and independence boundary;
- `TEST_REPORT.md`: regression, mutation and fuzz coverage;
- `MATERIAL_PASSPORTS.md`: sources, software and disclosure metadata;
- `ARTIFACT_HASHES.sha256`: read-only release integrity manifest;
- `PRELIMINARY_WITNESS.md`: retained Phase-1 feasibility artifact.

The formal Route-A record is `../route_a_evaluation.yaml`.

Run the whole release from any working directory with

```bash
/absolute/path/to/rauzy_groupoid_identity_determinant/code/run_c29.sh
```

The default command never refreshes the manifest.  Only an intentional release
update may use `--refresh-manifest`.
