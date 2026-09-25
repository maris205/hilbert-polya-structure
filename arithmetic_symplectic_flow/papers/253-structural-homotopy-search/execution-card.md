# CS03 execution card v1 — frozen before execution

Scope: `ASFS-DISCOVERY-20260919-CS03`. The current user continuation and
existing automatic local-work authorization cover this bounded wrapper/run.
The candidate card owns every mathematical choice and data-use rule.

Working directory: arithmetic_symplectic_flow repository root.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/253-structural-homotopy-search/run_search.py
```

Only output/monitor scope: this package's evidence/run-1 directory, event log
and launched process. Initial PID/RSS plus process-alive/output-growth checks
approximately every30seconds, no blocking wait over60seconds. Hard timeout is
armed before execution; anomalies otherwise advisory. No retry after crash.
No writes to old packages/sources; no installation/GPU/network upload.

Inputs are locked before the numerical run in input-locks.json; the manifest
locks that file and the executed script. Required inputs: this frozen card,
candidate card, immutable251helper (metrics and periodic potential only),
old252A full readout arrays/frozen identity, old251development reference,
old252fixed-alpha grid readouts descended from251,
and the unchanged original source solver. No execution of old main functions.
New151–200 numeric reference is generated only after selection is written.

Known windows:1–100training;101–150development;151–200this-run untrained
postfreeze evaluation, not historically blind. Per-grid first-anchor rule may
produce a different numerical scale; postfreeze windows keep the training
grid's scale. No re-selection or extra optimization after reference generation.

Collect exit status, elapsed timing, resource state and every output. Numerical
results are finite floating-point observations, not interval certifications.
Formal ARS reproducibility rerun is not part of this run; its Passport remains
UNVERIFIED even when execution and independent saved-array checks succeed.
