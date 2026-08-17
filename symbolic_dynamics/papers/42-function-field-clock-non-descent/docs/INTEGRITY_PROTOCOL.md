# Paper 42 portable integration integrity protocol

This protocol governs only the disposable static candidate rooted at the
directory containing this file. It grants no authority-tree, Git, mirror,
root-README, registry, writer, or paper-manifest mutation authority.

## Frozen and excluded inputs

The 17-file `preauthority/` package, the two-file `independent_da/` release,
the writer files bound by `WRITER_SHA256SUMS.txt`, and the exact experiment
blueprint are read only. Integration owns only the C-sorted paths in
`code/contracts/INTEGRATION_CONTRACT.json`. Writer paths are deliberately
excluded from both the static managed set and every result declaration.

The portable source resolver consumes exactly 29 typed IDs from the frozen
`SOURCE_HASHES.sha256`: 21 `repo:` IDs and eight `dependency:` IDs. Each is
represented by one local base64 container and verified after decoding. A
canonical run never consults a live or historical repository tree; the
external-tree comparison result is a fixed declaration that no such tree was
queried. The Route-A v0.2 skill is likewise vendored as exact encoded bytes
and verified after decoding.

## Process and evaluator boundary

The only canonical parent and packet-emitter commands are:

```text
python3 -I -B code/run_exact_integration.py
python3 -I -B code/source/emit_packet.py
```

Python startup hooks can execute before line 1, so naive hostile-environment
invocation is forbidden; an in-script restart is convenience, not the
security boundary. Every evaluator, Route checker, mutation harness, and
auditor is child-only and is invoked by the parent with `-I -B`, a scrubbed
`PYTHONPATH`/`PYTHONHOME`, and disabled user site.

The source emits one canonical raw packet. Neither evaluator imports or reads
source implementation bytes. The enumeration/trial-division evaluator and
the recurrence/Rabin evaluator parse the packet independently and must emit
byte-identical canonical science projections. JSON equality is recursive and
type strict: booleans, integers, and floats are never interchangeable. The
independent Route checker does not import or read the renderer; it binds the
full normalized Route digest, legal paired-state raw bytes, safe artifact
paths, and current science hash independently.

## Route and paired states

The Stage-A Route is strict live Route v0.2 at
`evaluations/route_a/SD-C44/2026-08-17.yaml`. Every mapping key, scalar type
and value, list member and order, artifact path, terminal, tuple component,
verdict, metric, evidence status, claim boundary, chronology field, Route-B
field, and integration seal is renderer-owned. Stage A has the same pending
sentinel in all three provenance fields and no paper manifest. Stage B is a
read-only hypothetical metadata transformation: one lowercase nonzero
40-hex commit replaces the triple, the exact sealed note is installed, and a
C-sorted self-excluding manifest appears. Mixed states are rejected.

## Generated adversarial closure

The registry mechanically enumerates the entire canonical packet and Route:
every mapping key is deleted, one extra key is inserted in every mapping,
every nonempty list loses and duplicates a member, every non-palindromic list
is reversed, and every scalar receives same-type and numeric-equivalent or
cross-type drift. The embedded six-card selector is a separately counted
group. Raw duplicate/noncanonical bytes, every static-path deletion,
namespace extras, every output deletion, coordinated payload-plus-ledger
tampering, immutable/DA/writer/dependency drift, Route drift, ledger drift,
and symlink controls are also executed. Each row freezes the responsible
main, independent, or complete sorted auditor rejection envelope. The result
publishes the globally C-sorted ID list and its SHA-256 plus per-group counts
and ID hashes; survivors must be the exact empty list.

## Transaction and audit

The parent first copies the complete input tree, excluding only managed
outputs, caches, auxiliaries, and the forbidden manifest, into an isolated
P42-only stage. It builds all 49 candidate outputs, runs the full mutation
registry, A/B/cold-C byte comparisons, Stage-A/Stage-B read-only audits, Route
checks, exact-set checks, and hygiene checks there. No target write occurs
until every gate passes. Installation uses atomic write-if-changed for every
output. An actual-parent forced late failure must return rc 2 with exactly:

```text
FAIL: FORCED_LATE_PREINSTALL_FAILURE
```

and leave the complete target input/output map unchanged with outputs and
caches absent. On a fresh clone the first accepted install must report 49
changed paths; an immediate second top-level replay must make zero physical
writes and change zero hashes. Extra-only, partial, dangling-symlink, and
symlinked-parent output namespaces are rejected before staging or install.

The auditor is read only. It independently verifies exact path sets,
immutable package and DA seals, writer exclusion, dependency snapshots,
canonical critical-result objects and A/B/C relations, Route normalization
and raw state, ledger/manifest state, AST role boundaries, chronology, and
text hygiene. `results/SHA256SUMS.txt` is C-sorted, unique, exact-set, and
self-excluding; it also excludes the Route and forbidden manifest, which have
their own exact gates.

The result-free writer seal is preserved as the immutable canonical
`docs/inputs/WRITER_BASELINE_SNAPSHOT.json` integration input. The canonical
integration command requires the current writer to equal that baseline and
never writes a writer-owned path. After output materialization, writer sync is
a separate authorized lane: the read-only auditor accepts either the exact
18-entry baseline writer map or an exact 20-entry post-sync map containing the
same 18 logical writer paths plus `COMPILATION_REPORT.md` and `main.pdf`.
Every mapped byte is hash-bound. Text paths retain text hygiene; the sole
binary path must have a PDF header and terminal EOF marker. Scientific prose,
layout, and compile acceptance remain the responsibility of the separate root
writer audit. Unlisted writer, root, immutable, or integration paths fail the
recursive whole-tree exact-set gate.

## Exact retrospective chronology

The theorem, six-card outcomes, witnesses, independent DA, and initial
substantive blueprint design predate integration implementation. The final
writer and blueprint bytes were repaired and frozen only after disposable
implementation smoke and therefore do not predate implementation. The work
is retrospective: `blind=false`, `fully_prospective=false`,
`results_unseen=false`, and there is no novelty, priority, preregistration,
outcome-independent, ranking, or authorization credit. The final static
candidate is frozen only after disposable smoke output bytes were known and
before a final disposable full replay. The exact correction tokens are:

```text
p41_transaction_architecture_adapted_after_p41_outputs_known
paper42_disposable_scratch_smoke_outputs_known_before_static_seal
stale_p41_mutation_harness_replaced_after_disposable_scratch_smoke
route_paired_state_exact_rejection_class_repaired_after_disposable_scratch_smoke
auditor_canonical_json_order_and_critical_result_semantic_closure_repaired_after_disposable_scratch_smoke
first_transactional_stage_smoke_failed_before_mutation_completion
nested_evaluations_snapshot_static_clone_exclusion_gap_repaired_after_disposable_scratch_smoke
final_writer_numbered_reference_portability_and_chronology_reseal_d930_ingested_before_final_static_seal
blueprint_rebound_to_final_writer_d930_before_final_static_seal
final_blueprint_writer_timing_overclaim_repaired_after_p39_static_hold_and_interrupted_disposable_replay
host_temporary_path_vocabulary_and_boundary_scanner_gap_repaired_before_replacement_static_seal
post_materialization_chronology_present_tense_gap_repaired_before_replacement_static_seal
writer_baseline_provenance_and_post_output_sync_lane_gap_repaired_before_replacement_static_seal
whole_tree_exact_set_and_packet_registry_partition_gaps_repaired_before_replacement_static_seal
evaluator_check_set_and_hostile_parent_evidence_gaps_repaired_before_replacement_static_seal
authority_governance_lock_and_fresh_input_map_gate_added_before_replacement_static_seal
packet_semantic_reanchor_lane_gap_repaired_before_final_replacement_static_seal
static_mutation_actual_auditor_envelope_gap_repaired_before_final_replacement_static_seal
coordinated_run_route_projection_closure_gap_repaired_before_final_replacement_static_seal
unsafe_path_pre_io_containment_gap_repaired_before_final_replacement_static_seal
cli_argument_contract_gap_repaired_before_final_replacement_static_seal
terminal_contract_block_anchor_gap_repaired_before_final_replacement_static_seal
json_container_and_nested_duplicate_mutation_gap_repaired_before_final_replacement_static_seal
expected_output_rename_and_symlink_replacement_gap_repaired_before_final_replacement_static_seal
external_frozen_auditor_exception_totality_gap_repaired_before_final_replacement_static_seal
route_artifact_precanonical_path_classification_gap_repaired_before_final_replacement_static_seal
semantic_fixture_hash_collision_reuse_gap_repaired_after_full_mutation_replay
route_raw_order_and_artifact_structure_exact_rejection_envelope_gaps_repaired_after_full_mutation_replay
```

These are integration-engineering/static corrections, not changes to the
scientific model, theorem, exact witnesses, selector, or frozen Route outcome.
No post-result scientific/model repair is claimed or performed.
