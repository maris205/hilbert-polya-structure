# Legacy Logistic numerical baselines and leakage audit

- Stage ID: `LEGACY-LOGISTIC-NUMERIC-BASELINES`
- Candidate ID: `none (audit/archive)`
- Formal candidate: `false`
- Archive status: `ARCHIVED`
- Paper status: `not_opened`

## Purpose

Preserves the legacy non-autonomous Logistic notebooks, deterministic eigensolver smoke test, and physical-epsilon robustness audit as historical evidence, including their explicit fitting and data-leakage boundaries.

This directory is a source-locked shareable snapshot of the corresponding
HP-Dynamics checkpoint.  It does not replace or rewrite the versioned evidence
in `riemann_dyna`; copied evidence is verified byte-for-byte by
`SOURCE_PROVENANCE.yaml` and `results/SOURCE_HASHES.sha256`.

## Route-A checkpoint

```text
analytic tuple:       not separately recorded
Riemann-target tuple: not separately recorded
overall:              NOT_FORMALLY_EVALUATED
recommended verdict: ARCHIVED
Route B authorized:   false
```

## Strongest failure / limitation

The legacy construction used fitted zero targets, USTC data, partition and smoothing choices, and no frozen primitive-orbit/Fredholm determinant object; it is not a Route-A candidate.

## Claim boundary

Established only within the frozen object and data boundary described by
`source_lock.yaml` and `route_a_evaluation.yaml`.  No project in this stream
claims a completed-xi identity, a Hilbert--Pólya realization, the Riemann
Hypothesis, or permission to mix determinant conventions.

## Canonical records

- Main source lock: `configs/source_locks/P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON.yaml`
- Main Route-A evaluation: `none`
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
PYTHONPATH=. python3 -m unittest -v tests/test_p4_logistic_legacy_audit.py
PYTHONPATH=. python3 -m unittest -v tests/test_p4_logistic_deterministic_smoke.py
PYTHONPATH=. python3 -m unittest -v tests/test_p4_logistic_medium_branch_audit.py
sha256sum -c results/SOURCE_HASHES.sha256
```

## Next smallest task

Keep as an archive and regression baseline only; do not reopen target-zero fitting or promote saved numerical matches.
