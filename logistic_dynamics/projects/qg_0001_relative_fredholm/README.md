# QG-0001 same-operator relative Fredholm determinant

- Stage ID: `QG-0001-RELATIVE-FREDHOLM`
- Candidate ID: `QG-0001`
- Formal candidate: `true`
- Archive status: `STOP_SCOPED`
- Paper status: `planned`

## Purpose

Proves that the inverse tower operator is trace class and identifies the exact relative Fredholm product and divisor with multiplicity.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_UNITARY_OR_SCATTERING_CANDIDATE)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED
Route B authorized:   false
```

## Strongest failure / limitation

The immutable total-length coefficient is about 12.7647 times the target coefficient, so the frozen divisor has the wrong asymptotic density.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml`
- Main Route-A evaluation: `evaluations/route_a/QG-0001/20260806T123946Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_qg_0001_relative_fredholm.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Keep under OBR-013; reopen only with a new intrinsic tower law and source lock, not a post-hoc scaling.
