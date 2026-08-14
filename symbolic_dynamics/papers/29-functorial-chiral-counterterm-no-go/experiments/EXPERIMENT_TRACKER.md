# Experiment Tracker — SD-C31

| Block | Canonical status | Evidence |
|---|---|---|
| preregistration | frozen before canonical run | top-level `PREREGISTRATION.md`, `experiments/EXPERIMENT_PLAN.md` |
| compiler/naturality | PASS | `results/incidence_checks.json` |
| baseline decomposition | PASS | 76 exact rows in `results/baseline_pair_ledger.csv` |
| finite-scheme ambiguity | PASS | 15 rows in `results/scheme_shift_ledger.csv` |
| controls | PROVES_TOO_MUCH | 47 rows in `results/control_pair_ledger.csv` |
| local coefficient no-go | PASS | 49 rows, zero solutions in `results/coefficient_grid_ledger.csv` |
| determinant ownership | PASS | `results/determinant_power_ledger.csv` |
| independent evaluator | PASS | 602/602 checks in `results/evaluation.json` |
| unit tests | PASS | 23/23 in `results/test_report.json` |
| fresh double run | PASS | `results/double_run_certificate.json` |
| integrity/SHA | PASS | `results/integrity_audit.json`, `results/SHA256SUMS.txt` |

The final row/hash values are owned by the authority canonical suite, not the
earlier `/tmp` prototype.
