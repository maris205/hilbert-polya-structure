# SD-C21 Experiment Artifact Schema

All paths are relative to the Paper 19 project root.

| artifact | content | exactness |
|---|---|---|
| `results/support_certificates.csv` | prime support at five frozen cutoffs | exact integer validation |
| `results/power_trace_ledger.csv` | rational traces through repetition order twelve | exact rational |
| `results/bounded_depth_controls.csv` | incomplete-verifier false positives | exact integer |
| `results/random_accept_controls.csv` | 32 matched random-support overlaps | seeded deterministic |
| `results/universal_decider_controls.csv` | square, power-of-two, Fibonacci, and hash wrappers | exact SCC plus rational determinant |
| `results/trace_class_entry_sums.csv` | finite absolute-entry regression sums | deterministic float display; theorem is analytic |
| `results/route_gate_summary.csv` | strict frozen A0--A4 tuple | deterministic CSV |
| `results/control_comparison_table.csv` | control outcomes and stopping interpretations | deterministic CSV |
| `results/run_summary.json` | complete primary graph, controls, and verdict ledger | deterministic JSON |
| `results/source_oracle_certificate.json` | AST and materialized Q-state audit | deterministic JSON |
| `results/analysis_summary.json` | strict Route decision and claim boundary | deterministic JSON |
| `results/test_summary.json` | thirteen-test certificate | deterministic JSON |
| `results/integrity_audit.json` | parse, LF, schema, cache, scope, and provenance-mode audit | deterministic JSON |
| `results/SHA256SUMS.txt` | every code/result artifact except itself | SHA-256 |

Expected CSV data-row counts are respectively `5,12,5,32,4,20,5,7` in the
table order above.  CSV is UTF-8 with LF line endings.  JSON is UTF-8, sorted
by key, and ends in one LF.  Runtime/timestamp metadata are forbidden.

The Route-A YAML initially uses `PENDING_FIRST_ARTIFACT_COMMIT` for source and
code.  The integrity audit accepts that exact paired placeholder before the
first artifact commit and accepts a matching 40-character lowercase Git hash
after sealing.  Mixed or malformed provenance is rejected.

All six zero/root metrics in the Route-A A2 block are strings beginning with
`not_applicable;` because this project performs no target-zero evaluation.
