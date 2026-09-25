## Material Passport

- Origin Skill: experiment-agent (ARS-Codex)
- Origin Mode: run
- Origin Date: 2026-09-19 (research date supplied by environment)
- Verification Status: UNVERIFIED (formal ARS reproducibility rerun not invoked)
- Version Label: ds05_result_v1

## Experiment Result

- ID: `ASFS-DISCOVERY-20260919-DS05`
- Type/status: saved-array analysis / COMPLETED
- Exit code: 0; one execution, no failure/retry/timeout/stderr
- Process PID: 44072
- Internal duration before final JSON: 0.06682681665 seconds
- Tool-observed wall duration: 0.105457137 seconds
- Initial/peak reported max RSS: 36448 / 36448 KiB
- Actual UTC: manifest start 2026-09-18T17:32:29.308516; completed
  2026-09-18T17:32:29.334866. This differs from the supplied research date;
  both are preserved, not silently equated.

Command, cwd = arithmetic_symplectic_flow root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/248-anchor-shape-decomposition/analyze_saved.py
```

The hard timeout was armed. Start/PID and normal process completion were
observed in one tool call; the run finished before a 30-second monitoring
interval. No separate periodic RSS/process snapshot was needed or claimed.
No GPU, installation, new forward, eigensolve or historical-file change.

[Manifest](run-1/manifest.json) owns four exact NPZ path/hash locks, Python
3.12.3, NumPy2.4.4, script hash and the immutable pre-analysis card hash.
Script SHA256: `616319d9ac7ec4a541cccfde7bdd97218a074bd982c779cef20af3cf80c3518c`.
Card SHA256: `63ec481460f32e1a6ac2167cc189c5d2749628dfa21ebba2d9110e3092ef4e0c`.

[Result](run-1/result.json): 4 cases, 4 fixed anchors each, all inputs unchanged.
[All points](run-1/all-points.csv): 1600 data rows, no omitted adverse grids.
Existing-output refusal prevents silent overwrite or automatic repeat.
Outputs are finite descriptive evidence, not statistical population inference.

## Independent saved-array check

A separate same-family agent read the four original NPZ files and recomputed
all 1600 CSV rows and JSON metrics without propagation or eigensolving.
Maximum field/metric difference was 0; the identity residual remained
4.4408920985e−16. All target and 300-step schedule arrays agreed elementwise.
This is a saved-array consistency check, not a new forward reproduction,
external peer review or the formal ARS verification rerun.
