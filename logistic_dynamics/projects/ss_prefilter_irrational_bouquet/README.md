# Irrational-roof countable bouquet prefilter

- Stage ID: `SS-PREFILTER-IRRATIONAL-BOUQUET`
- Candidate ID: `none (audit/archive)`
- Formal candidate: `false`
- Archive status: `STOP_SCOPED`
- Paper status: `planned`

## Purpose

Gives an explicit entire countable Fredholm product with incommensurate primitive lengths and a closed-form divisor.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED
Route B authorized:   false
```

## Strongest failure / limitation

The disconnected cycle actions escape every bounded real strip, leaving only O(T) zeros in each fixed vertical strip despite countability and non-lattice periods.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml`
- Main Route-A evaluation: `evaluations/route_a/SS-PREFILTER-IRRATIONAL-BOUQUET/20260810T162243Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_ss_prefilter_irrational_bouquet.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Keep under OBR-016; connectivity and a new divisor mechanism are required.
