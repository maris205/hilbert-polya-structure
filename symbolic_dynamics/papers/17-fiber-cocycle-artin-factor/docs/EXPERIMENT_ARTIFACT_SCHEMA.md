# SD-C19 Experiment Artifact Schema

All CSV files use LF line endings. All JSON files are UTF-8, sorted-key, and
newline-terminated. Results contain no timestamps or elapsed-time values.

| Artifact | Rows / role |
|---|---|
| `formal_c2_factorization.csv` | 10 formal determinant certificates |
| `repetition_trace_ledger.csv` | 300 exact trace/repetition coefficients |
| `c2_transitivity.csv` | 10 exact two-fiber adjacency certificates |
| `cm_character_certificates.csv` | 350 exact coefficient/phase certificates |
| `cm_regular_local_determinants.csv` | seven regular local determinants |
| `primitive_lift_census.csv` | 350 base/lift census rows |
| `primitive_degree_distributions.json` | exact degree distributions |
| `naturality_tables.csv` | all 72,079 cardinality tables |
| `naturality_summary.csv` | 35 cutoff cells |
| `coboundary_controls.csv` | 63 gauge and 21 negative controls |
| `transition_countercontrols.csv` | four exact transition determinants |
| `inventory_controls.csv` | 64 exact inventory controls |
| `inventory_comparison_table.csv` | four pass-rate comparisons |
| `analysis_summary.json` | claim-facing aggregate |
| `test_summary.json` | deterministic 14-test certificate |
| `integrity_audit.json` | parse/LF/cache/prototype-diff certificate |
| `SHA256SUMS.txt` | code/result integrity ledger |

`base_necklace_q_distribution_json` counts base primitive necklaces grouped by
lift multiplier. `lifted_primitive_cycles_total` is the separate lifted-cycle
multiplicity field.

`identity_pass_rate_margin` compares exact identity pass rates, not numerical
determinant values.
