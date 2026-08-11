# Strict-monotone autonomous Logistic clock-lift obstruction

- Stage ID: `P4-LOGISTIC-MONOTONE-CLOCK-LIFT`
- Candidate ID: `P4-LOGISTIC-MONOTONE-CLOCK-LIFT`
- Formal candidate: `false`
- Archive status: `STOP_SCOPED`
- Paper status: `planned`

## Purpose

Proves that the exact autonomous lift of the frozen logarithmic aging schedule has all full-state periodic orbits on the static U_c boundary.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED
Route B authorized:   false
```

## Strongest failure / limitation

The strict Lyapunov clock creates no recurrent aging orbits and adds a neutral clock multiplier, so occupation-matrix cycles cannot be used as chronological UPOs.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`
- Main Route-A evaluation: `evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml`
- `results/`: formal result notes copied from the main research repository.
- `obstructions/`: scoped obstruction notes, when applicable.
- `experiments/`, `tests/`, and `artifacts/`: repository-compatible
  reproduction snapshot.
- `SOURCE_PROVENANCE.yaml`: source commit, paths, and hashes.

## Dependencies

- None beyond files mirrored in this project.

## Reproduction

Run from this project directory.

This regression is portable inside the mirrored project snapshot.

```bash
PYTHONPATH=. python3 -m unittest -v tests/test_p4_logistic_monotone_clock_lift.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Reopen only with an intrinsically recurrent base and a source-locked same-object determinant; otherwise keep this subclass closed.
