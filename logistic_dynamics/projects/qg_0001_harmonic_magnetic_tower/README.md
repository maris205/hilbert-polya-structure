# QG-0001 harmonic magnetic graph-tower prefilter

- Stage ID: `QG-0001-HARMONIC-MAGNETIC-TOWER`
- Candidate ID: `QG-0001`
- Formal candidate: `true`
- Archive status: `GO_WITH_LIMITATIONS`
- Paper status: `planned`

## Purpose

Freezes a low-complexity magnetic lollipop-theta graph tower with exact orbit/scattering data and a natural magnetic-Laplacian lift.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_EXPLORATORY
recommended verdict: GO_WITH_LIMITATIONS
Route B authorized:   false
```

## Strongest failure / limitation

The naive infinite product is not an ordinary determinant, and no arithmetic primitive-orbit or completed-xi trace law is present.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/QG-0001.yaml`
- Main Route-A evaluation: `evaluations/route_a/QG-0001/20260806T090351Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_qg_0001_harmonic_magnetic_tower.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Read through the base-characteristic and relative-Fredholm repairs; do not use the naive determinant.
