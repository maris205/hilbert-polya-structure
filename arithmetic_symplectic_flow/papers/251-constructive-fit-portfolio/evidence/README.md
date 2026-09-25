## Material Passport

- Origin Skill: experiment-agent (ARS-Codex)
- Origin Mode: run
- Origin Date: 2026-09-19 (supplied research date)
- Verification Status: UNVERIFIED (formal ARS rerun not invoked)
- Version Label: cs01_result_v1

## Executed constructive search

- ID: `ASFS-DISCOVERY-20260919-CS01`
- Status/type: COMPLETED / bounded supervised numerical construction search
- Exit: 0; no stderr/failure/retry/timeout
- PID 45948; timeout parent45947
- Actual UTC start: 2026-09-18T18:08:43.350178
- Actual UTC completion: 2026-09-18T18:15:14 (separate from supplied research date)
- Internal duration before final serialization: 390.6742045 seconds
- Initial/peak maxRSS: 78616 / 114468 KiB
- Process checks: elapsed17s RSS102080 KiB NLWP1; elapsed78s RSS103664 KiB
  NLWP1; elapsed123s RSS103928 KiB NLWP1. Events continued growing normally.
- No GPU, installation, external upload/publication or original source changes.

Executed once, cwd=arithmetic_symplectic_flow root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/251-constructive-fit-portfolio/run_search.py
```

[Manifest](run-1/manifest.json) records five exact input locks, script,
Python3.12.3/NumPy2.4.4/SciPy1.16.1, command and initial resource state.
Script SHA256 `317fc87e033f9e3bea7ba5dc8c35096f9bf1a9ce1bf0b2e218a98f358e366fe4`.
[Execution card](../execution-card.md) distinguishes fixed extrapolation scale
from per-grid application of the fixed first-anchor rule.

## Outputs and ordering

[Events](run-1/events.jsonl): 285 start/complete pairs, 5 cached calls,
5 training-complete events, one training freeze and one completion; no failures.
[Seed design](run-1/seed-design.json) contains18 normalized points shared by all forms.
[Evaluations](run-1/evaluations/) contains285 NPZ+JSON pairs, all sorted energies
and predictions retained, not just winning points.
[Regression control](run-1/regression-control.json) passed with6.20e−12 max
prediction difference. The extra form D transform-identity preflight does not
compute a model spectrum or consume optimization data.

[Winners frozen](run-1/winners-frozen.json) was written at18:14:58.938962 UTC,
SHA256 `9ce81c2106000c412c1a4a76a48432d633e93402daafe805882be5e21bd00759`.
Five complete winner NPZ files were then saved; event training_frozen occurred
18:14:59.682013, before reference generation started18:14:59.682056.
[Reference101–150](run-1/reference-101-150.json) was generated with mpmath1.3.0
at40 decimal working precision; no interval certification claimed.
[Winner points](run-1/winner-points.csv):750 rows, five forms×150 indices.
[Result](run-1/result.json) includes all training/extrapolation metrics and
two adverse resolution diagnostics. All five NM optimizers hit their40-call
limit; their success=false is preserved, not treated as convergence.

[Formula review](form-review.md) plus a separate read-only implementation
preflight checked DST complex handling, kinetic axes, split order and data
access ordering. These were same-model-family internal checks, not peer review.

## Independent saved-result check

A separate same-family agent recomputed metrics from all285evaluation NPZ/JSON
pairs, all five winner arrays,750final point rows and both resolution arrays.
Maximum metric discrepancy was0; all source hashes, budgets and event ordering
matched the frozen contract. This check performed no new forward, eigensolve
or reference generation. It is not external peer review or a formal ARS rerun.
