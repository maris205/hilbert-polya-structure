# Phragmen-Lindelof lower bound for the LOG-0001 order

- Stage ID: `LOG-0001-ORDER-LOWER`
- Candidate ID: `LOG-0001`
- Formal candidate: `true`
- Archive status: `ANALYTIC_REVIEW`
- Paper status: `planned`

## Purpose

Combines the same-determinant half-plane bound and nonconstancy witness to prove the sharp interval 1<=ord(D_pol)<=2.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall:              ROUTE_A_EXPLORATORY
recommended verdict: GO_WITH_LIMITATIONS
Route B authorized:   false
```

## Strongest failure / limitation

The interval does not distinguish order one from two and gives no target divisor asymptotic, prime weights, or quantization.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/LOG-0001-ORDER-LOWER.yaml`
- Main Route-A evaluation: `evaluations/route_a/LOG-0001/20260809T110000Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_log_0001_order_lower.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Park LOG-0001 at this theorem boundary and pursue structurally different candidates rather than additional local estimates.
