# SS-0002 commutator-cover Mayer operator

- Stage ID: `SS-0002-COMMUTATOR-MAYER`
- Candidate ID: `SS-0002`
- Formal candidate: `true`
- Archive status: `STOP_SCOPED`
- Paper status: `planned`

## Purpose

Constructs a genuine countable-branch nuclear Mayer operator with intrinsic C6 holonomy and a natural modular Laplacian quantization.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED
Route B authorized:   false
```

## Strongest failure / limitation

Its same-object Selberg divisor contains Omega(T^2) spectral zeros, so it cannot equal the completed-xi Theta(T log T) divisor.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/SS-0002.yaml`
- Main Route-A evaluation: `evaluations/route_a/SS-0002/20260803T012711Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_ss_0002_commutator_mayer.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Keep under OBR-006; do not glue the separate scattering determinant.
