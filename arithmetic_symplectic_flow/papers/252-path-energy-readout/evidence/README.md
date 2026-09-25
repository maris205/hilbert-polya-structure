## Material Passport

- Origin Skill: experiment-agent (ARS-Codex)
- Origin Mode: run
- Origin Date: 2026-09-19 (supplied research date)
- Verification Status: UNVERIFIED (formal ARS rerun not invoked)
- Version Label: cs02_result_v1

## Executed readout construction

- ID: `ASFS-DISCOVERY-20260919-CS02`
- Status/type: COMPLETED / saved-state supervised scan
- Exit0; no failure, stderr, retry, timeout, GPU, installation or upload
- PID46409; actual UTC start2026-09-18T18:17:12.009424
- Completed UTC2026-09-18T18:17:13.489346; internal time1.498797249seconds
- Peak maxRSS89388KiB; exact initial RSS and environment in manifest
- No new evolution or eigensolve; source arrays unchanged

Executed once, cwd=arithmetic_symplectic_flow root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/252-path-energy-readout/scan_readout.py
```

Start/PID observed before process yielded; completion before30-second periodic
monitor interval, hard timeout armed. No periodic RSS observation claimed.
[Manifest](run-1/manifest.json) records all [input locks](../input-locks.json),
script hash and execution environment; source winner/reference hashes were
checked before execution without parsing future numeric values.
Script SHA256 `fef6e535a2d06cf04d67609c6bc6a1cd1d21cb171977dcaf216514dec655bf52`.

## Selection order and outputs

[Events](run-1/events.jsonl): training_frozen18:17:13.396462,
extrapolation_reference_read18:17:13.396499 UTC; no training after that read.
[Frozen winners](run-1/winners-frozen.json) SHA256
`f2525caf3818d0783b4bfcf1e9406d9b141a4e1b05afda39ba3ccbce6e3fe7cb`.
[Search CSV](run-1/search.csv):10035rows, five×(2006training+1diagnostic),
8790uniquealpha evaluations including five diagnostics; cached calls retained.
[Winner points](run-1/winner-points.csv):750rows, five×150indices.
[Result](run-1/result.json): all five training/extrapolation results, time-mean
controls, exact source IDs and both reused-resolution diagnostics.

## Independent saved-array check

A separate same-family agent checked every10035scanrow, all five sources and
winnerNPZs,750pointrows, five coarse grids/25refinements and both resolution
NPZs. Recomputed arrays/metrics agreed exactly; direct H_ref quadratic forms
differed from the affine formula by at most2.48690e−14 with identical integer
branches. Maximum eigenvector column norm error≤1.33227e−15.
No evolution/eigenvalue solve/reference generation was performed by reviewer.
This is internal evidence checking, not external peer review or a formal ARS
reproducibility-run certificate.

## Final package consistency check

Root integration checked16Markdown files,551local link targets,10current
ID/status fields,23SHA256 locks, both750-row winner tables and the10035-row
scan table: zero errors. Locks include the frozen cards/scripts, source arrays,
original solver, plan, both Route mirrors and the unchanged243method paper.
Both upstream snapshots remain Git-clean; root index diff-whitespace checks
passed. A separate read-only prose review found no substantive inconsistency;
its one wording correction distinguishes a quadratic-form discrepancy from
a matrix-norm discrepancy. No experiment was repeated for documentation QA.
