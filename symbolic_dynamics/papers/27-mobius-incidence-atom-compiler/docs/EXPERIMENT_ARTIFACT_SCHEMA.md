# Experiment Artifact Schema — SD-C29

## Deterministic CSV ledgers

| Artifact | Rows | Purpose |
|---|---:|---|
| incidence_inverse_ledger.csv | 4 | two-sided inverse at four cutoffs |
| primitive_idempotent_ledger.csv | 30 | rank, trace, formula, similarity |
| pair_relation_ledger.csv | 900 | every \(q_nq_m\) relation |
| cover_atom_ledger.csv | 256 | source covers versus evaluator |
| necklace_ledger.csv | 1016 | every cyclic class through length six |
| digit_marker_ledger.csv | 80 | ten atoms through eight repetitions |
| power_trace_ledger.csv | 8 | exact marked power traces |
| fredholm_de_rham_ledger.csv | 4 | finite and degreewise determinants |
| weighted_hilbert_ledger.csv | 24 | trace-norm formula displays |
| bounded_similarity_ledger.csv | 3 | \(\eta>1\) similarity certificates |
| source_mutation_controls.csv | 2 | standard and promoted-six sources |
| stability_equivariance_ledger.csv | 30 | cutoff and relabeling checks |
| ablation_controls.csv | 13 | scalar, zeta-only, unfiltered failures |
| route_gate_summary.csv | 5 | frozen Route-A tuple |
| analysis_comparison_table.csv | 9 | raw comparison table for analysis |

CSV requirements are UTF-8, LF-only, one header row, deterministic row order,
and no floating-point value in a claim-bearing equality.

## JSON certificates

- source_oracle_certificate.json records candidate/evaluator separation.
- run_parameters.json freezes all cutoffs and exact weights.
- environment_lock.json records interpreter and library versions.
- theorem_ledger.json maps claims to evidence.
- summary.json contains primary pass/fail predicates.
- analysis_summary.json records observations, interpretations, implications,
  and next tests.
- test_summary.json records the exact regression result.
- double_run_certificate.json records both byte-hash maps.
- integrity_audit.json validates schema, route, source, science, LF, and caches.

## Provenance

The Route-A YAML intentionally uses the same
PENDING_FIRST_ARTIFACT_COMMIT value for source_commit, code_commit, and
source_lock.code_commit. This is a strict two-stage pre-commit freeze, not an
unknown or mixed provenance state. This integrator performs no Git operation.
