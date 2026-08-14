# SD-C22 Experiment Artifact Schema

All paths are relative to the Paper 20 project root.

| artifact | content | exactness |
|---|---|---|
| results/cycle_clock_ledger.csv | exact length, spectral witnesses, and source-clock distortion for 564 primes | exact integers plus deterministic float displays |
| results/cutoff_compactness_witnesses.csv | five frozen tail compactness witnesses | deterministic float displays; theorem is analytic |
| results/power_trace_certificates.csv | first four nonzero traces for eleven small prime blocks | exact rational |
| results/marker_firewall.csv | raw versus induced products at \(z=1,1/3\) | exact rational |
| results/padded_decider_controls.csv | four generic total-decider controls | deterministic finite certificates |
| results/route_gate_summary.csv | strict A0--A4 tuple | deterministic CSV |
| results/summary.json | primary ledger, exact products, controls, and verdict | deterministic JSON |
| results/source_oracle_certificate.json | endpoint, Q-state, and allowed-instruction audit | deterministic JSON |
| results/analysis_summary.json | strict Route decision and claim boundary | deterministic JSON |
| results/test_summary.json | exact-test certificate | deterministic JSON |
| results/integrity_audit.json | parse, LF, schema, cache, scope, and provenance audit | deterministic JSON |
| results/SHA256SUMS.txt | every code/result artifact except itself | SHA-256 |

Expected CSV data-row counts in table order are 564, 5, 44, 2, 4, and 5.
CSV is UTF-8 with LF line endings. JSON is UTF-8, sorted by key, and ends in
one LF. Runtime and timestamp metadata are forbidden.

The Route-A YAML initially uses PENDING_FIRST_ARTIFACT_COMMIT for source and
code. The integrity audit accepts that exact paired placeholder before the
first authority commit and accepts a matching 40-character lowercase Git hash
after sealing. Mixed or malformed provenance is rejected.

All six target-zero/root metrics in the Route-A A2 block are strings beginning
with "not_applicable;" because this project performs no target-zero evaluation.
