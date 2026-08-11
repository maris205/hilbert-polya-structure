# Validated sharp exact-U_c polar-cone enclosure

- Stage ID: `P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE`
- Candidate ID: `P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`
- Formal candidate: `false`
- Archive status: `GO_WITH_LIMITATIONS`
- Paper status: `planned`

## Purpose

Sharpens the physical ACIP cone using interval validation and freezes a reproducible endpoint/branch-mass certificate.

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

Sharp physical weights still do not generate log-prime periods, von-Mangoldt amplitudes, analytic continuation, or quantization.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml`
- Main Route-A evaluation: `evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml`
- `results/`: formal result notes copied from the main research repository.
- `obstructions/`: scoped obstruction notes, when applicable.
- `experiments/`, `tests/`, and `artifacts/`: repository-compatible
  reproduction snapshot.
- `SOURCE_PROVENANCE.yaml`: source commit, paths, and hashes.

## Dependencies

- None beyond files mirrored in this project.

## Reproduction

Run from the `hilbert-polya-structure` repository root.

This historical regression is source-bound because it verifies the original `riemann_dyna` Git commit or an artifact containing frozen absolute source paths. The wrapper runs the original test at the manifest-bound source commit; mirror bytes remain checked independently.

```bash
python3 logistic_dynamics/tools/test_all_projects.py --project exact_uc_acip_sharp_cone_enclosure
cd logistic_dynamics/projects/exact_uc_acip_sharp_cone_enclosure
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Use only as an input to the quantitative branch-mass and polar-roof theorem chain.
