# SS-0003 connected integer-renewal Dirichlet transfer

- Stage ID: `SS-0003-CONNECTED-RENEWAL`
- Candidate ID: `SS-0003`
- Formal candidate: `true`
- Archive status: `STOP_SCOPED`
- Paper status: `planned`

## Purpose

Constructs a connected countable renewal graph whose rank-two Fredholm determinant is exactly 2-zeta(s) on Re(s)>1 and whose scalar a-points have the correct Theta(T log T) fixed-strip order.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)
Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED
Route B authorized:   false
```

## Strongest failure / limitation

Positivity forces a unique forbidden real determinant zero in (1,2), and the all-integer primitive alphabet has no prime/von-Mangoldt law.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/SS-0003-CONNECTED-RENEWAL.yaml`
- Main Route-A evaluation: `evaluations/route_a/SS-0003/20260811T112250Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_ss_0003_connected_renewal.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Keep under OBR-017; only a structurally new intrinsic signed/complex grammar can reopen the clue.
