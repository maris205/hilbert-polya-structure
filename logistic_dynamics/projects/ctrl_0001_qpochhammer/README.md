# Four-channel q-Pochhammer Fredholm evaluator control

- Stage ID: `CTRL-0001-QPOCHHAMMER`
- Candidate ID: `none (audit/archive)`
- Formal candidate: `false`
- Archive status: `STOP_SCOPED_CONTROL`
- Paper status: `not_opened`

## Purpose

Provides a deterministic positive control for signed complex Fredholm ledgers, winding counts, cutoff drift, missing/extra roots, and balanced corruption tests.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED_CONTROL
Route B authorized:   false
```

## Strongest failure / limitation

The four channels are engineered evaluator infrastructure with no natural primitive dynamics, prime law, completed-xi structure, or quantization.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/CTRL-0001.yaml`
- Main Route-A evaluation: `evaluations/route_a/CTRL-0001/20260803T171847Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_ctrl_0001_qpochhammer.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Reuse as a regression control for new determinants; never promote it to a Riemann candidate.
