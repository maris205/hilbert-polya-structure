# Exact-U_c physical ACIP endpoint-density theorem

- Stage ID: `P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY`
- Candidate ID: `P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`
- Formal candidate: `false`
- Archive status: `GO_WITH_LIMITATIONS`
- Paper status: `planned`

## Purpose

Identifies the exact endpoint density relation and the physical branch-mass ratio for the U_c absolutely continuous invariant probability measure.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
Riemann-target tuple: not separately recorded
overall:              ROUTE_A_EXPLORATORY
recommended verdict: REVISE
Route B authorized:   false
```

## Strongest failure / limitation

The theorem fixes a physical normalization but supplies neither an arithmetic primitive-orbit law nor a dynamical determinant.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml`
- Main Route-A evaluation: `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`
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
PYTHONPATH=. python3 -m unittest -v tests/test_p4_logistic_uc_acip_endpoint_density.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Use the endpoint identity only inside the validated cone and polar constructions with the same physical measure.
