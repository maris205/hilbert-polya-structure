# SD-C38 experiment artifact schema

## Scientific payloads

The fresh A/B/cold-C pipeline emits exactly 19 deterministic payloads.

| Family | Artifacts | Meaning |
|---|---|---|
| locks | `environment_lock.json`, `dependency_lock.json`, `run_parameters.json` | exact execution and dependency roles |
| source | `source_raw.json`, `source_summary.json`, `source_test_report.json` | neutral source construction and self-checks |
| firewall | `source_separation_certificate.json` | AST import/oracle separation and prototype core hashes |
| evaluator | `trace_audit.csv`, `marker_audit.csv`, `operator_cycle_audit.csv`, `finite_chain_audit.csv`, `graded_control.json`, `control_summary.json`, `evaluation.json`, `prototype_bridge_certificate.json` | independent exact reconstruction and controls |
| tests | `test_report.json` | authority integration gates |
| analysis | `raw_data_table.csv`, `analysis.json`, `ANALYSIS_REPORT.md` | raw comparison table and numbered findings |

## Reproducibility metadata

`double_run_certificate.json` binds fresh A/B hashes and stage stdout.
`cold_start_certificate.json` binds the cache-free cold C run.
`research_lock.json` hashes seven frozen authority research documents and the
external research package. `artifact_inventory.json` declares the exact final
result set and the authority scientific aggregate.

## Integrity metadata

`SHA256SUMS.txt` is a sorted relative-path ledger over experiment-owned code,
plans, docs, Route card, report, and non-self-referential results.
`aggregate_sha256.txt` is the SHA-256 of that ledger. The idempotence and
integrity payloads are excluded from the ledger to avoid recursion and are
bound by the later paper manifest.

All canonical text must be UTF-8, LF-only, exactly one terminal LF, free of
trailing whitespace and forbidden control bytes, and accompanied by no Python
or test cache.

## Route-A v0.2

The strict YAML contains all required input fields, allowed evidence enums,
the nine A2 metrics, the paired pending provenance triple, the frozen tuple,
`ROUTE_A_REJECTED`, and `route_b_invocation_allowed: false`.
