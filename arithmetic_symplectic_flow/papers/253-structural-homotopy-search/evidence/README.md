## Material Passport

- Origin Skill: experiment-agent (ARS-Codex)
- Origin Mode: run
- Origin Date: 2026-09-19 (supplied research date)
- Verification Status: UNVERIFIED (formal ARS rerun not invoked)
- Version Label: cs03_result_v1

## Executed constructive search

- Scope ID: `ASFS-DISCOVERY-20260919-CS03`
- Status/type: COMPLETED / bounded supervised structural construction search
- Exit0; no observed failure, traceback, timeout, retry, GPU, installation or upload
- PID48044; timeout parent48043
- Actual UTC manifest start2026-09-18T18:44:06.020991
- Actual UTC completion2026-09-18T18:46:44.225406
- Internal duration158.215738844seconds, before final serialization
- Initial/peak maxRSS78312/108380KiB
- Process observations: elapsed8s RSS90440KiB NLWP1;32s93616KiB NLWP1;
  113s94468KiB NLWP1. Events grew normally; process exited normally afterward.
- Monitoring target was approximately30seconds, but the32s→113s interval
  exceeded it during documentation work; no continuous30-second coverage is
  claimed. Process-alive checks and the600-second hard timeout were present.

Executed once from arithmetic_symplectic_flow root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/253-structural-homotopy-search/run_search.py
```

[Manifest](run-1/manifest.json) records9input locks, the lock-file hash, script,
Python3.12.3/NumPy2.4.4/SciPy1.16.1 and resources. The research date above is
not substituted for the observed UTC process date.
Script SHA256 `3b7dcc9ab4b3c5a22ecdb7a1b6a5cbd7cc17c90e5133d32a46607e0b63e0e054`.
Input-locks SHA256 `d11beba9e8b04ba3ab9194301338a6f3c07edfb4c1a5f4b1bcb2c6270bdb6f31`.

## Preflight and independent formula/implementation checks

[Formula review](form-review.md) checked all five equations, R monotonicity,
J jet/seam distinction and each H_ref. A separate read-only implementation
review checked current script against both frozen cards, seeds, budgets,
ownership, caching and freeze-before-reference order. An initial broader
cross-form lambda0 cache was narrowed before execution to the exact shared
default only; other points cache by form. No faulty version was run.

Import-free compile plus import/parameter-roundtrip checks confirmed all five
default normalized points reproduce the exact stored(hbar,a_start,0); no
forward/eigensolve was performed in those preflights. Nine input locks passed
before launch and remained unchanged afterward. The new first full forward
then passed[regression control](run-1/regression-control.json): zero first100
prediction discrepancy and zero MAPE discrepancy against252fixed-alpha output.
These are internal same-family checks, not external peer review.

## Counts, outputs and selection order

[Calls](run-1/calls.json):285calls,276new training forwards,9cache hits.
[Seed design](run-1/seed-design.json):17points×5forms, shared seeded perturbations.
[Evaluation directory](run-1/evaluations/):276NPZ/JSON pairs, with all spectra,
phases, expectations, branches and200predictions retained, not just winners.
All five optimizers hit40calls; success=False preserved.
Five complete winner NPZs include U/H_ref/H_end/eigenvectors and schedules.

[Winners frozen](run-1/winners-frozen.json) SHA256
`cce41b1691852ac3d4d6502ef83b7d5e9982092972c961cf80116b0ddb94d7d3`.
[Events](run-1/events.jsonl) record training_frozen18:46:29.998845UTC,
postfreeze_reference_start18:46:29.998901, then development_reference_read
18:46:42.527880. No optimization occurs after the freeze.
[151–200reference](run-1/reference-151-200.json):mpmath1.3.0,40decimal working
precision; not interval-certified, not historically blind.
[Winner points](run-1/winner-points.csv):1000rows, five×200; windows explicitly
train/development/postfreeze-evaluation. Baseline future predictions use saved
252energies, not a new baseline forward.
[Result](run-1/result.json):all five training/postfreeze metrics, optimizer
states, old baseline and two adverse N260/280 diagnostics; new grid forwards2.

The global winner arose inS but haslambda0. This is old-subfamily parameter
retuning, not evidence that the sextic term improved the fit.

## Independent saved-result review and final consistency

A separate same-family agent recomputed all276evaluation NPZ/JSON pairs,
all five winners, both grids and1000CSV rows. Parameters, alpha, targets,
branch/raw-energy/sort/shift/scale/200predictions, six metrics and full-winner/
grid matrix diagnostics agreed exactly: maximum discrepancy0.0. No forward,
eigensolve, new reference generation or file write was performed by reviewer.
This is an ANALYZED saved-evidence check, not a formal reproducibility rerun;
it does not change the Passport's UNVERIFIED run-certificate label.

The285calls split57per form(17seeds+40NM); actual forwards Q56 and S/J/K/R55each.
All9cache calls correctly cite the shared default. All576events have monotone
UTC ordering; all9input hashes plus script/lock-file hashes agree, and every
execution input predates launch. There were178nonzero-lambda actual training
forwards; none beats the old default on primary MAPE. Other metric tradeoffs
remain reported in the paper. Cached records inherit source seconds: summing
those per-call fields is not a valid process-runtime estimate.

Main integration checked9Markdown files,528local link targets,5current ID/status
pairs, the immutable card ID,15SHA256 locks and1000CSV rows: zero errors.
Protected plan/Route mirrors/243paper and original solver hashes remain equal;
both upstream snapshots are Git-clean. Root index whitespace checks passed.
The operating-system exit0 and the process/RSS/thread observations above come
from the main execution tool, not an inference from the manifest command text.
