# Results

The raw and derived artifacts for the frozen experiment live here.

## Primary artifacts

- catalog_robustness.json and CSV: all 2,170 primitive cycles through period 20
- roots_robustness.json and CSV: both orientation sectors and all tested cutoffs
- controls.json: random, constant-roof, shuffle, and neighbor controls
- analysis_summary.json: strict machine-readable aggregate
- ANALYSIS.md: evidence-labelled interpretation and next tests
- control_summary.csv: compact control table
- independent_check.json: standalone 38-check reconstruction
- manifest.json: repository handoff hashes

All JSON artifacts are emitted in strict RFC 8259 form; an unmatched-root
drift is represented by JSON null, never a bare non-finite token.

Development, validation, and sealed-test catalog/root files are retained
separately so the source split can be audited rather than reconstructed from
the period-20 output. The frozen protocol is
../refine-logs/R000_FROZEN_PROTOCOL.json. The Route-A evaluation is under
../evaluations/route_a/.
