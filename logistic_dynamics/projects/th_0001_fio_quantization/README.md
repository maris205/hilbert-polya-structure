# TH-0001 same-order Fourier-integral quantization

- Stage ID: `TH-0001-FIO-QUANTIZATION`
- Candidate ID: `TH-0001`
- Formal candidate: `true`
- Archive status: `GO_WITH_LIMITATIONS`
- Paper status: `planned`

## Purpose

Constructs the natural same-order unitary FIO on L2(R), proves the exact generating-function relation, and audits the inherited antiunitary class.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_EXPLORATORY
recommended verdict: GO_WITH_LIMITATIONS
Route B authorized:   false
```

## Strongest failure / limitation

A natural unitary lift does not supply a determinant, discrete target spectrum, self-adjoint generator, or prime-power trace formula.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/TH-0001-FIO.yaml`
- Main Route-A evaluation: `evaluations/route_a/TH-0001/20260806T045554Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_th_0001_fio_quantization.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

The single-phase caustic audit is the only scoped continuation; Route B remains closed.
