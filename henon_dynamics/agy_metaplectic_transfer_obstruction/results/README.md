# HCS-C25 exact results

The result bundle is intentionally split into a producer artifact and an
independent replay:

- `c25_certificate.json` -- seven-state graph, every elementary edge,
  deterministic state-4 symplectic frames, all fourteen fixed-fiber edge
  matrices, source-locked AGY section witness, 128-step decoder trace,
  exact projective data, all-length theorem metadata, and the non-proof
  stress sentinel;
- `c25_independent_check.json` -- independent graph/matrix/Jacobian/decoder
  reconstruction; all registered checks must be true;
- `RESULTS.md` -- mathematical findings and scope;
- `VALIDATION_REPORT.md` -- exact independent checks;
- `TEST_REPORT.md` -- regression and mutation suite;
- `MATERIAL_PASSPORTS.md` -- artifact lineage and epistemic status;
- `ARTIFACT_HASHES.sha256` -- integrity manifest for code and released
  results.

Regenerate the bundle with:

```bash
./code/run_c25.sh
```

The length-22 replay is not a periodic-orbit ledger and is not the proof of
injectivity.  Its sole role is to detect implementation mutations in the
all-length decoder.
