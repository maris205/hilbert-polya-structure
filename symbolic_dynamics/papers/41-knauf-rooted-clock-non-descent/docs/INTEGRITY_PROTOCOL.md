# Paper 41 integration integrity protocol

The auditor and orchestrator own only the paths declared in
`code/contracts/INTEGRATION_CONTRACT.json`. Immutable research, external DA,
writer prose, manuscript sources, figures, compilation products, the paper
manifest, Git, registries, the umbrella README, and mirrors are outside that
set.

The local source snapshot preserves the exact 20 `repo:` bytes named by the
portable source manifest in one base64 container per source. The two typed dependencies are separately vendored
under `docs/inputs/dependencies/`. Canonical evaluation resolves the same 22
IDs against those portable local roots. Canonical materialization never reads
an external historical repository tree: it emits one fixed declaration that
the external tree was not queried. A separately requested diagnostic may
compare live repository paths outside the sealed pipeline, but it cannot enter
canonical results, reports, ledgers, Route bytes, or science bytes.

The fixed Route-A v0.2.0 skill is stored as base64 only to preserve exact
bytes safely. Every loader must decode it and verify SHA-256 before accepting
the schema fixture.

`code/audit_integrity.py` is read only. It accepts the actual Stage-1 state
or an isolated hypothetical Stage-2 state. It rejects every mixed state and
prints the same sorted check ledger for both legal states. The orchestrator,
not the auditor, prepares disposable copies for cold and Stage-2 checks.

The machine-controlled CLI policy is
`CANONICAL_PARENT_AND_EMITTER_REQUIRE_EXTERNAL_PYTHON_I_B__NAIVE_HOSTILE_FORBIDDEN`.
The only canonical parent command is
`python3 -I -B code/run_exact_integration.py`; the independent stdout command
is `python3 -I -B code/source/emit_packet.py`. Their in-script self-restart is
only an ordinary-misuse mitigation, not a security boundary: Python may run
`sitecustomize` before line 1. The packet/Route evaluators, independent
evaluator, read-only auditor, and mutation harness are child-only; the parent
invokes them with `python3 -I -B`, and every evidence command must do the same.
Naive hostile-environment invocation is forbidden.

The parent alone may invoke the isolated internal stage as
`python3 -I -B code/run_exact_integration.py --build-validated-stage` with its
private stage environment. The transaction negative is
`python3 -I -B code/run_exact_integration.py --force-late-transaction-failure`;
on an empty-output clone it must return rc 2 with exactly
`FAIL: FORCED_LATE_PREINSTALL_FAILURE`, leave the complete input map unchanged,
and create no output, cache, or external-sentinel change.

`results/SHA256SUMS.txt` is sorted, unique, exact-set, and self-excluding. It
also excludes the Route YAML and the forbidden paper manifest; those are
validated through their own contracts. No cache, bytecode, auxiliary,
symlink, control-character, carriage-return, missing-final-linefeed, or
trailing-whitespace artifact is permitted in integrator-owned text.

## Corrective-reseal chronology

The exact machine-controlled chronology payload is:

```json
{
  "blind": false,
  "cards_science_witnesses_da_known_before_original_docs": true,
  "fully_prospective": false,
  "known_corrections": [
    "unsorted_result_contract_and_raw_snapshot_hygiene_corrections_known",
    "direct_write_changed_accounting_and_idempotence_defect_known",
    "post_seal_evaluator_byte_drift_known",
    "route_semantic_survivors_and_mutation_coverage_gaps_known",
    "superseded_1c38_static_seal_and_clone_evidence_known",
    "parent_prebootstrap_module_shadow_and_cache_gap_known",
    "direct_emitter_bytecode_cache_gap_known",
    "mandatory_external_tree_portability_gap_known",
    "cross_evaluator_python_equality_type_gap_known",
    "cli_role_and_python_minimum_contract_gaps_known",
    "python_startup_sitecustomize_preexec_gap_known",
    "packet_selection_numeric_equivalent_type_gap_known",
    "coordinated_auditor_json_type_gap_known",
    "globally_sorted_mutation_id_ledger_and_report_audit_gap_known",
    "evaluator_direct_read_and_dynamic_import_boundary_gap_known",
    "hostile_parent_environment_negative_control_gap_known",
    "critical_result_semantic_auditor_closure_gap_known",
    "immutable_ledger_mutation_coverage_gap_known",
    "ast_role_allowlist_and_dynamic_read_gap_known",
    "source_resolver_structural_mutation_coverage_gap_known",
    "selection_and_route_safe_existing_ordered_mutation_gap_known",
    "nontransactional_failed_clone_contamination_gap_known"
  ],
  "novelty_credit": false,
  "original_experiment_docs_pre_initial_code_and_outputs": true,
  "priority_credit": false,
  "replacement_static_frozen_before_replacement_canonical_rerun": true,
  "results_unseen": false,
  "route_survivors_seen_before_replacement_seal": true,
  "status": "RETROSPECTIVE_CORRECTIVE_RESEAL_AFTER_FAILED_OUTPUTS_AND_AUDIT_FINDINGS",
  "superseded_output_materialization_seen_before_replacement_seal": true,
  "write_and_idempotence_defects_seen_before_replacement_seal": true
}
```

The machine-controlled integration status is
`RETROSPECTIVE_CORRECTIVE_RESEAL_AFTER_FAILED_OUTPUTS_AND_AUDIT_FINDINGS`.
The original two experiment documents were frozen before the initial
authority code and outputs, while all six cards, the science, witnesses, and
devil's-advocate result were already known. This narrower fact does not make
the replacement implementation blind or prospective.

Before the replacement static seal, superseded materialization bytes and all
of these corrections were known:

- `unsorted_result_contract_and_raw_snapshot_hygiene_corrections_known`;
- `direct_write_changed_accounting_and_idempotence_defect_known`;
- `post_seal_evaluator_byte_drift_known`;
- `route_semantic_survivors_and_mutation_coverage_gaps_known`;
- `superseded_1c38_static_seal_and_clone_evidence_known`;
- `parent_prebootstrap_module_shadow_and_cache_gap_known`;
- `direct_emitter_bytecode_cache_gap_known`;
- `mandatory_external_tree_portability_gap_known`;
- `cross_evaluator_python_equality_type_gap_known`;
- `cli_role_and_python_minimum_contract_gaps_known`;
- `python_startup_sitecustomize_preexec_gap_known`;
- `packet_selection_numeric_equivalent_type_gap_known`;
- `coordinated_auditor_json_type_gap_known`;
- `globally_sorted_mutation_id_ledger_and_report_audit_gap_known`;
- `evaluator_direct_read_and_dynamic_import_boundary_gap_known`;
- `hostile_parent_environment_negative_control_gap_known`;
- `critical_result_semantic_auditor_closure_gap_known`;
- `immutable_ledger_mutation_coverage_gap_known`;
- `ast_role_allowlist_and_dynamic_read_gap_known`;
- `source_resolver_structural_mutation_coverage_gap_known`;
- `selection_and_route_safe_existing_ordered_mutation_gap_known`;
- `nontransactional_failed_clone_contamination_gap_known`.

Only the final replacement static bytes are frozen before the replacement
canonical rerun. Therefore `blind=false`, `fully_prospective=false`, and
`results_unseen=false`; no novelty or priority credit is claimed.

No post-result scientific/model repair is used. The corrective post-output
integration-engineering and static repairs are disclosed above; the exact
rejection envelopes, isolated-interpreter/cache controls, and independent
Route-auditor closure are part of that corrective reseal. The final static
bytes are frozen only before the final replacement canonical rerun; none of
these corrected implementation bytes or their prior clone results is claimed
unseen, blind, or fully prospective.

The failed full-replay clone also exposed that the superseded runner installed
42 candidate outputs before its late mutation/audit gate completed. The
replacement runner therefore builds and validates the complete output set in
an isolated staging tree and reaches a forced late-failure control before any
target write. Only a fully accepted stage may be installed.
