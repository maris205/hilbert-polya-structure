# SS-0001 finite-state mod-6 Cayley suspension

- Stage ID: `SS-0001-MOD6-CAYLEY`
- Candidate ID: `SS-0001`
- Formal candidate: `true`
- Archive status: `STOP_SCOPED`
- Paper status: `planned`

## Purpose

Gives an exact residue-memory symbolic suspension with nontrivial mod-3 modes, complete primitive-cycle census, and a closed determinant.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_REJECTED
recommended verdict: STOP_SCOPED
Route B authorized:   false
```

## Strongest failure / limitation

Every finite-state finite-roof determinant has only O(T) zeros in a fixed vertical strip, not the completed-xi Theta(T log T) divisor.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/SS-0001.yaml`
- Main Route-A evaluation: `evaluations/route_a/SS-0001/20260802T163302Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_ss_0001_mod6_cayley.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Keep under OBR-005; finite residue decoration cannot reopen this class.
