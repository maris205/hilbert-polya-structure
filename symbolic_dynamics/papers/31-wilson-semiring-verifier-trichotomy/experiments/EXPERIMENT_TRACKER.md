# SD-C33 experiment tracker

| Block | Status | Canonical evidence |
|---|---|---|
| authority experiment lock | complete | `experiments/EXPERIMENT_PLAN.md` |
| source/candidate oracle audit | complete | `results/source_oracle_certificate.json` |
| Wilson cutoff 4096 | complete | `results/wilson_ledger.csv` (4,095 rows; 564 accepts) |
| composite/pseudoprime evaluation | complete | `results/composite_controls.csv`, `results/fermat_pseudoprime_controls.csv` (3,531 + 13 rows) |
| bare/matched semiring clones | complete | `results/bare_ufd_addition_failure.csv`, `results/matched_semiring_clone.csv` (144 + 169 rows) |
| operation-table controls | complete | `results/semiring_controls.json`, `results/random_operation_controls.json` (7 + 33 rows) |
| recurrent dilution/formal traces | complete | `results/entropy_budget_dilution.csv`, `results/formal_trace_ledger.csv` (1,692 + 16 rows) |
| marker and universal wrappers | complete | `results/marker_change_certificate.json`, `results/universal_wrapper_controls.json` (2 + 5 rows) |
| independent evaluator | complete | `results/evaluation.json` (26,620/26,620 checks pass) |
| exact tests and analysis | complete | `results/test_report.json`, `results/analysis.json` (18/18 pass under direct pytest and isolated runner) |
| double-run/integrity/SHA | complete | `results/double_run_certificate.json`, `results/integrity_audit.json`, `results/SHA256SUMS.txt` (16 fresh artifacts; complete-tree audit exits 0; 31 hashes) |
| report | complete | `EXPERIMENT_REPORT.md` |
