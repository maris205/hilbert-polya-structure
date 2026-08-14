# SD-C20 Experiment Artifact Schema

All paths below are relative to the Paper 18 project root.

| artifact | content | exactness |
|---|---|---|
| `results/incidence_orbits.csv` | `(u,v,w)` orbit rows through four atoms | integer exhaustive |
| `results/group_enumeration_summary.csv` | headline `S3,D4,Q8` counts | exhaustive |
| `results/group_exact_certificates.json` | grids, CRT bounds, survivors, rejection witnesses | exact finite-field plus CRT |
| `results/s3_exact_certificate.json` | character determinants, trace-log leaks, commutator gap | `Z[x,y]` / integer group arithmetic |
| `results/primitive_holonomy_ledger.csv` | frozen two- and four-cycle witnesses | exact |
| `results/transition_controls.csv` | identity, counting, gauge, and nongauge candidate | exact |
| `results/inventory_controls.csv` | six matched inventories over five seeds | rational/formal exact |
| `results/trace_class_gates.csv` | honest nuclear half-plane thresholds | analytic theorem ledger |
| `results/run_summary.json` | preregistered gates and claim boundaries | deterministic JSON |
| `results/analysis_summary.json` | result interpretation and Route tuple | deterministic JSON |
| `results/test_summary.json` | fourteen-test certificate | deterministic JSON |
| `results/integrity_audit.json` | parse, LF, YAML schema, cache, and scope audit | deterministic JSON |
| `results/SHA256SUMS.txt` | all code/result hashes except itself | SHA-256 |

Every CSV is UTF-8 with LF line endings.  Every JSON is UTF-8, sorted by key,
and ends in one LF.  Result metadata exclude wall time and timestamps.  The
Route-A YAML uses source/code commit placeholders pending the authority
two-stage commit protocol; this integration performs no Git operation.
