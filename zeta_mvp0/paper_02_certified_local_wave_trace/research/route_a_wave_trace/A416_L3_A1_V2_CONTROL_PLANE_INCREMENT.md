# A4.16 L3-A1 V2 control-plane increment

Scientific protocol identifier: `R401-VAL-L3-A1`

Control generation name: `A416_L3_A1_CONTROL_V2`

Prepared: 2026-08-11 UTC

Status: **UNBOUND ENGINEERING RECORD / NON_LICENSING**

## Purpose

This increment records the decision to repair the A4.16 L3-A1 control plane
without changing its scientific protocol.  It is intentionally not a member
of the 53-role input map, is not hashed by a future main freeze, and conveys
no review, freeze, initialization, result, theorem, release, promotion, or
dispatch authority.

Attempt 1 reached published roles 10--13 but a later independent review found
two P1 gaps: no formal role-54/formal 68-role production validator in old
role 24, and no formal three-checker plus three-postcheck publication chain
in old roles 20--22.  Write-once history makes in-place repair invalid.
Attempt-1 bytes and Git history are retained unchanged; role 5 will later
record their formal `WITHDRAWN_NON_LICENSING` disposition if and only if an
independent reviewer accepts the completed V2 implementation.

V2 uses no new scientific protocol identifier and adds no generation field
to artifacts.  Its namespace is defined solely by the fixed map below.  The
unchanged scientific evaluator, CAPD source/binary, branch runtime, static
evaluator test, and accepted upstream result roles remain direct inputs.

## Exact V2 53-role control map appendix

## Normative exact role-5 literals

This marker-delimited block is repeated byte-for-byte across the V2
documents.  Quoted values are exact UTF-8/ASCII JSON string values; integers
and Booleans are JSON values, not strings.  Every independent role-5
validator carries and compares these literals independently.

<!-- BEGIN A416_L3_A1_CONTROL_V2_ROLE5_LITERALS -->
```text
schema_version = 1
protocol_id = "R401-VAL-L3-A1"
artifact_role = "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL"
status = "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1"
authority = "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY"
scientific_licensing_enabled = false
production_authorized = false
legacy_attempt.attempt_id = "A416_L3_A1_CONTROL_ATTEMPT_1"
legacy_attempt.status = "WITHDRAWN_NON_LICENSING"
legacy_attempt.terminal_commit = "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0"
legacy_attempt.published_artifacts.role_json_type = integer
legacy_attempt.published_artifacts.role_order = [10,11,12,13]
legacy_attempt.published_artifacts[0].path = "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
legacy_attempt.published_artifacts[0].sha256 = "0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e"
legacy_attempt.published_artifacts[0].publication_commit = "5086e33c7c66f33785338e90b340347e086d9941"
legacy_attempt.published_artifacts[1].path = "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json"
legacy_attempt.published_artifacts[1].sha256 = "08ffeb5e7f5d681567bd7a81335585d1b8697040a28d91584b09fdc4304a379a"
legacy_attempt.published_artifacts[1].publication_commit = "201758031a7784a68ab66d37094c25135de52646"
legacy_attempt.published_artifacts[2].path = "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md"
legacy_attempt.published_artifacts[2].sha256 = "af38e899f9dad9abacadbdaa27f12833d5ea423a9896ee089fb8a4d90b55477c"
legacy_attempt.published_artifacts[2].publication_commit = "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0"
legacy_attempt.published_artifacts[3].path = "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
legacy_attempt.published_artifacts[3].sha256 = "d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30"
legacy_attempt.published_artifacts[3].publication_commit = "be2a732625d9cab97879539873a756e1eabd366d"
legacy_attempt.defects[0].severity = "P1"
legacy_attempt.defects[0].code = "ROLE24_MOCK_ONLY_NO_FORMAL_54_OR_68_VALIDATION"
legacy_attempt.defects[0].finding = "legacy role 24 implements mock release and machine verification only; it does not implement formal role-54 validation or publication or formal 68-role release validation or publication"
legacy_attempt.defects[1].severity = "P1"
legacy_attempt.defects[1].code = "ROLES20_22_NO_FORMAL_THREE_CHECKER_THREE_POSTCHECK_CHAIN"
legacy_attempt.defects[1].finding = "legacy roles 20 through 22 do not implement the required formal static, branch, and composite checker plus postcheck publication chain"
legacy_attempt.supersession_rule = "legacy attempt-1 bytes remain immutable audit evidence, are not V2 inputs, and confer no freeze, initialization, scientific licensing, promotion, or dispatch authority"
reviewed_v2_inputs.role_json_type = string
reviewed_v2_inputs.role_order = ["prefreeze_design","formal_protocol","scheduler_contract","checker_contract","release_contract","scheduler","static_checker_source","branch_checker_source","composite_checker_source","s0_adapter","release_builder","test_static_scheduler","test_static_checker","test_branch_scheduler","test_branch_checker","test_s0_compatibility","test_composite","test_adversarial","test_release"]
review.reviewer_independent_of_attempt1_author = true
review.verdict = "ACCEPT_CONTROL_PLANE_V2_DESIGN"
review.p0_count = 0
review.p1_count = 0
review.p2_count = 0
review.reviewed_commit = LOWERCASE_GIT_COMMIT_40_HEX
review.map_matches_contract = true
review.legacy_bytes_unchanged = true
review.scientific_protocol_unchanged = true
claim_boundary = "independent withdrawal of control attempt 1 and acceptance of the reviewed V2 control implementation only; no machine, main freeze, result, theorem, release, initialization, promotion, or dispatch acceptance"
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```
<!-- END A416_L3_A1_CONTROL_V2_ROLE5_LITERALS -->

The four exact Boolean review gates are
`reviewer_independent_of_attempt1_author`, `map_matches_contract`,
`legacy_bytes_unchanged`, and `scientific_protocol_unchanged`; each must
be JSON `true`.  `reviewed_commit` is the one intentionally variable
value and must match `^[0-9a-f]{40}$`.  The 19 reviewed-role strings are
exact role names from the ordered 53-role map, not row numbers.

Every `publication_commit` and `reviewed_commit` must name an exact Git
`commit` object.  The `reviewed_commit` tree must bind the exact regular Git
blob, mode, recorded digest, and live bytes for all 19 reviewed V2 paths.
It is also the historical upper bound for the four legacy publication
proofs: the fixed legacy terminal commit must be reachable on its
first-parent chain; each fixed publication commit must be reachable on that
chain, be an ordinary single-parent introduction commit whose child tree has
the exact fixed regular blob/mode and whose unique parent has the path
absent; every newer tree through `reviewed_commit` must retain that exact
blob/mode; and every older first-parent tree through the root must keep the
path absent.  Root introductions, merges, cycles, orphan commits, deletion,
replacement, and delete-then-readd histories are hard rejection.  All Git
proofs use bounded pure object/index readers with no Git subprocess or
fallback; a coherent-looking 40-hex OID alone is never evidence.

<!-- BEGIN A416_L3_A1_CONTROL_V2_ROLE5_LIFECYCLE -->
## Normative implemented V2 role-5 lifecycle

The role-5 lifecycle tooling is implemented and covered by non-scientific
tests.  The repository contains no role-5 builder: one fresh independent
reviewer outside these tools must author the complete candidate.  Neither
role 19 nor role 24 may synthesize, fill, repair, or infer the verdict,
finding counts, independence gate, reviewed commit, or any of the 19
reviewed-input rows.

```text
implementation_status = "ROLE5_LIFECYCLE_TOOLING_IMPLEMENTED_AND_NONSCIENTIFICALLY_TESTED"
candidate.origin = "EXTERNAL_INDEPENDENT_REVIEWER_ONLY"
candidate.repository_builder_present = false
candidate.path = "/tmp/a416-v2-role5-review.<32lowerhex>/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"
candidate.parent.basename_regex = "^a416-v2-role5-review\\.[0-9a-f]{32}$"
candidate.parent.parent = "/tmp"
candidate.parent.owner = "EFFECTIVE_UID"
candidate.parent.mode = "0700"
candidate.parent.nlink = 2
candidate.parent.namespace = ["R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"]
candidate.file.type = "REGULAR"
candidate.file.mode = "0600"
candidate.file.nlink = 1
candidate.file.size_bytes.range = [1,1048576]
candidate.serializer = "CJ_COMPACT_V1"
candidate.payload.top_level_key_count = 15
candidate.payload.contract = "A416_L3_A1_CONTROL_V2_ROLE5_LITERALS"

role24.api = "verify_v2_role5_candidate(project_root,candidate_path)"
role24.cli = ["--verify-role5-candidate","<ABSOLUTE_CANDIDATE_PATH>"]
role24.child_processes_started = 0
role24.artifacts_written = false
role24.verify_receipt.key_count = 7
role24.verify_receipt.key_order = ["verification_status","authority","candidate_sha256","input_map_sha256","size_bytes","promotion_authorized","artifacts_written"]
role24.verify_receipt.verification_status = "PASS_V2_DESIGN_REVIEW_WITHDRAWAL_VERIFY_ONLY"
role24.verify_receipt.authority = "NON_AUTHORITATIVE_VERIFY_ONLY"
role24.verify_receipt.candidate_sha256 = <SHA256_OF_EXACT_CANDIDATE_BYTES>
role24.verify_receipt.input_map_sha256 = <SHA256_OF_CJ_COMPACT_V1_ORDERED_19_REVIEWED_ROWS>
role24.verify_receipt.size_bytes = <EXACT_CANDIDATE_SIZE>
role24.verify_receipt.promotion_authorized = false
role24.verify_receipt.artifacts_written = false
role24.input_map_sha256.domain = "SHA256(CJ_COMPACT_V1(exact ordered reviewed_v2_inputs array of 19 objects with keys role,path,sha256), including its one terminal LF)"
role24.stdout = "CJ_COMPACT_V1(EXACT7_VERIFY_RECEIPT)_WITH_ONE_TERMINAL_LF"

verify_receipt.external_capture_path = "/tmp/a416-v2-role5-verify.<32lowerhex>/ROLE24_ROLE5_VERIFY_RECEIPT.json"
verify_receipt.parent.basename_regex = "^a416-v2-role5-verify\\.[0-9a-f]{32}$"
verify_receipt.parent.parent = "/tmp"
verify_receipt.parent.owner = "EFFECTIVE_UID"
verify_receipt.parent.mode = "0700"
verify_receipt.parent.nlink = 2
verify_receipt.parent.namespace = ["ROLE24_ROLE5_VERIFY_RECEIPT.json"]
verify_receipt.file.type = "REGULAR"
verify_receipt.file.mode = "0600"
verify_receipt.file.nlink = 1
verify_receipt.file.size_bytes.range = [1,4096]
verify_receipt.serializer = "CJ_COMPACT_V1"

role19.api = "publish_v2_role5(candidate_value,role24_receipt_value,expected_sha256,expected_reviewed_commit,publication_authority,authority_root_value)"
role19.cli.required_only = ["--publish-role5","--candidate","<ABSOLUTE_CANDIDATE_PATH>","--role24-receipt","<ABSOLUTE_ROLE24_RECEIPT_PATH>","--expected-sha256","<LOWERCASE_SHA256>","--expected-reviewed-commit","<LOWERCASE_GIT_COMMIT_40_HEX>","--publication-authority","ROLE19_DESIGN_REVIEW_PUBLICATION_ONLY","--authority-root","<ROLE10_FILESYSTEM_PROJECT_ROOT>"]
publication.intent.key_order = ["reviewed_commit","candidate_sha256","canonical_path","publication_authority"]
publication.intent.reviewed_commit = <EXPLICIT_EXPECTED_REVIEWED_COMMIT>
publication.intent.candidate_sha256 = <EXPLICIT_EXPECTED_CANDIDATE_SHA256>
publication.intent.canonical_path = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"
publication.intent.publication_authority = "ROLE19_DESIGN_REVIEW_PUBLICATION_ONLY"
publication.intent.source = "FRESH_EXPLICIT_USER_AUTHORIZATION"
publication.reviewed_commit_bindings = ["candidate.review.reviewed_commit","explicit_expected_reviewed_commit","refs/heads/main","refs/remotes/origin/main","live_remote_main"]
publication.reviewed_tree = "EXACT_CLEAN_INDEX_AND_ORDERED_19_COMMITTED_AND_LIVE_BYTE_MODE_BINDINGS"
publication.pre_stage_worktree = "EXACTLY_CLEAN"
publication.pre_rename_worktree = "EXACTLY_ONE_OWNED_UNTRACKED_STAGE"
publication.post_rename_worktree = "EXACTLY_ONE_CANONICAL_ROLE5_UNTRACKED_LEAF"

publication_receipt.key_count = 24
publication_receipt.key_order = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate_path","canonical_path","design_review_sha256","reviewed_commit","size_bytes","mode","nlink","serializer","publication_method","verify_receipt_sha256","input_map_sha256","independent_verification_receipt_validated","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","component_status","milestone_status","theorem_status","final_status"]
publication_receipt.schema_version = 1
publication_receipt.protocol_id = "R401-VAL-L3-A1"
publication_receipt.artifact_role = "DESIGN_REVIEW_AND_WITHDRAWAL_PUBLICATION_RECEIPT"
publication_receipt.artifact_status = "PUBLISHED_WRITE_ONCE_NON_LICENSING"
publication_receipt.authority = "ROLE19_DESIGN_REVIEW_PUBLICATION_ONLY"
publication_receipt.candidate_path = <EXACT_ABSOLUTE_CANDIDATE_PATH>
publication_receipt.canonical_path = "<ROLE10_FILESYSTEM_PROJECT_ROOT>/research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"
publication_receipt.design_review_sha256 = <EXPLICIT_EXPECTED_CANDIDATE_SHA256>
publication_receipt.reviewed_commit = <EXPLICIT_EXPECTED_REVIEWED_COMMIT>
publication_receipt.size_bytes = <EXACT_CANDIDATE_SIZE>
publication_receipt.mode = "0644"
publication_receipt.nlink = 1
publication_receipt.serializer = "CJ_COMPACT_V1"
publication_receipt.publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
publication_receipt.verify_receipt_sha256 = <SHA256_OF_EXACT_ROLE24_RECEIPT_BYTES_INCLUDING_ONE_TERMINAL_LF>
publication_receipt.input_map_sha256 = <SHA256_OF_CJ_COMPACT_V1_ORDERED_19_REVIEWED_ROWS>
publication_receipt.independent_verification_receipt_validated = true
publication_receipt.scientific_licensing_enabled = false
publication_receipt.production_authorized = false
publication_receipt.scientific_dispatch_performed = false
publication_receipt.component_status = null
publication_receipt.milestone_status = null
publication_receipt.theorem_status = null
publication_receipt.final_status = null

publication.phase_count = 9
publication.phase_order = ["AFTER_STAGE_WRITE","AFTER_STAGE_FILE_FSYNC","AFTER_STAGING_PARENT_FSYNC","BEFORE_TERMINAL_REPLAY","BEFORE_RENAME","AFTER_RENAME","AFTER_DESTINATION_FSYNC","AFTER_PUBLICATION_PARENT_FSYNC","AFTER_ULTIMATE_REPLAY"]
publication.method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
publication.stage.basename_regex = "^\\.R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL\\.json\\.publish-[0-9a-f]{32}$"
publication.stage.final_mode = "0644"
publication.stage.nlink = 1
publication.before_rename_hook_followed_by_full_replay = true
publication.full_replay_inputs = ["candidate_bytes_inode_parent_namespace","role24_receipt_bytes_inode_parent_namespace","exact15_role5_semantics","ordered19_live_and_reviewed_tree_bindings","legacy_four_publication_histories","clean_head_origin_live_remote_and_index","canonical_absence","authority_root_and_publication_parent_chains","owned_stage_bytes_inode_and_namespace"]
publication.rename_flags = "RENAME_NOREPLACE"
publication.file_fsync_before_rename = true
publication.parent_fsync_before_rename = true
publication.destination_fsync_after_rename = true
publication.parent_fsync_after_rename = true
publication.existing_destination_is_success = false
publication.portable_fallback_present = false
publication.pre_rename_cleanup = "OWNED_STAGE_ONLY"
publication.post_rename_rollback = false
publication.post_rename_unlink = false
publication.post_rename_overwrite = false
```

A role-24 `PASS` receipt proves only that the mechanical schema, live bytes,
Git history, and closed authority boundary were replayed for the exact
candidate.  It is not the independent review decision, is not publication
authorization, and cannot be promoted into either.  Likewise, possession of
the role-19 authority literal is not authorization.  Canonical publication
still requires a fresh explicit user authorization binding the exact
four-tuple `(reviewed_commit, candidate_sha256, fixed canonical path,
publication authority)`.

The publication receipt is transient transport evidence only.  Candidate
verification and role-5 publication authorize no role 10, 11, 12, 13, or 54,
no result-root initialization, evaluator dispatch, checker or postcheck
publication, release, scientific licensing, production, component,
milestone, theorem, final, promotion, or implication-toward-RH claim.
<!-- END A416_L3_A1_CONTROL_V2_ROLE5_LIFECYCLE -->

## Normative V2 role-11 ownership and schema

Role 11 stays inside the existing 53-role map and reuses the final attempt-1
22-key evidence envelope.  No unbound producer, checker, or focused-test tool
is permitted.  Role 19 owns candidate capture and write-once publication;
role 24 owns zero-subprocess independent verification; role 32 is the focused
test binding.  Role 24 verification reopens and reconstructs the recorded
evidence but never starts pytest, Git, a compiler, an evaluator, or any other
child process.

<!-- BEGIN A416_L3_A1_CONTROL_V2_ROLE11_CONTRACT -->
```text
canonical_path = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json"
top_level_key_count = 22
top_level_keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","recorded_at_utc","repository_snapshot","evidence_tool_bindings","pre_review_input_roles","prerequisite_bindings","command_results","test_totals","covered_gates","held_out_policy","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","claim_boundary","component_status","milestone_status","theorem_status","final_status"]
schema_version = 1
protocol_id = "R401-VAL-L3-A1-PREFREEZE-TESTS"
artifact_role = "PREFREEZE_TEST_RECORD"
artifact_status = "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW"
authority = "PREFREEZE_TEST_EVIDENCE_ONLY"
scientific_licensing_enabled = false
production_authorized = false
scientific_dispatch_performed = false
claim_boundary = "pre-freeze engineering test evidence only; no held-out or all-slab L3 result was read and no scientific evaluator was dispatched; no L3-A1 component, milestone, theorem, final, global tube-routing, trace-formula, Hilbert-Polya, zeta-zero, RH, or implication-toward-RH claim"
component_status = null
milestone_status = null
theorem_status = null
final_status = null
evidence_tool_bindings.key_order = ["producer","independent_checker","focused_test"]
evidence_tool_bindings.producer.path = "scripts/run_r401_val_l3_a1_v2_all_slabs.py"
evidence_tool_bindings.producer.sha256 = "3fbad3d7c67dafb32e27daa2c666c60ececc9494e3cff9fe5c1a951effc1757b"
evidence_tool_bindings.producer.size_bytes = 774502
evidence_tool_bindings.producer.mode = "0644"
evidence_tool_bindings.producer.nlink = 1
evidence_tool_bindings.independent_checker.path = "scripts/build_r401_val_l3_a1_v2_release_provenance.py"
evidence_tool_bindings.independent_checker.sha256 = "9fd662d2035434263e13dc71500e7157164fa771d9b94cf2c33c9352724b2bb1"
evidence_tool_bindings.independent_checker.size_bytes = 384529
evidence_tool_bindings.independent_checker.mode = "0644"
evidence_tool_bindings.independent_checker.nlink = 1
evidence_tool_bindings.focused_test.path = "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py"
evidence_tool_bindings.focused_test.sha256 = "01e34e6699965335f20794a3d4fe50386f2ad5a37852c09ea4c891e5bdde1c70"
evidence_tool_bindings.focused_test.size_bytes = 70561
evidence_tool_bindings.focused_test.mode = "0644"
evidence_tool_bindings.focused_test.nlink = 1
evidence_tool_binding.keys = ["path","sha256","size_bytes","mode","nlink"]
pre_review_input_roles.count = 51
pre_review_input_roles.excluded_role_order = ["prefreeze_tests","prefreeze_review"]
pre_review_input_roles.role_order = ["a416_derivation","s0_protocol","s0_report","prefreeze_design","implementation_design_review","formal_protocol","scheduler_contract","checker_contract","release_contract","machine_freeze","s0_compatibility","capd_dependency","static_evaluator","branch_evaluator_source","branch_evaluator_binary","branch_runtime","scheduler","static_checker_source","branch_checker_source","composite_checker_source","s0_adapter","release_builder","test_static_evaluator","test_static_scheduler","test_static_checker","test_branch_scheduler","test_branch_checker","test_s0_compatibility","test_composite","test_adversarial","test_release","l1_final_plan","l1_summary","l1_manifest","l1_checker","l1_postcheck","l1_release","a415_summary","a415_manifest","a415_checker","a415_postcheck","a415_release","s0_static_summary","s0_static_manifest","s0_static_checker","s0_branch_summary","s0_branch_manifest","s0_branch_checker","s0_composite_summary","s0_composite_manifest","s0_composite_checker"]
pre_review_input_role.keys = ["role","path","sha256","size_bytes","mode","nlink"]
command_results.count = 7
command_results.name_order = ["role24_machine_verify","role13_compatibility_verify","prefreeze_focused_pytest","l3_a1_modules_pytest","paper02_full_pytest","git_diff_check","second_fresh_rebuild"]
command_results.kind_order = ["VERIFY_MACHINE_FREEZE","VERIFY_S0_COMPATIBILITY","PYTEST_FOCUSED","PYTEST_L3_A1","PYTEST_PAPER02","GIT_DIFF_CHECK","SECOND_FRESH_REBUILD"]
command_result.keys = ["name","kind","argv","cwd","environment","return_code","started_at_utc","wall_duration_ms","stdout_utf8","stdout_sha256","stdout_size_bytes","stderr_utf8","stderr_sha256","stderr_size_bytes","pytest_counts","semantic_receipt"]
test_totals.keys = ["prefreeze_focused","l3_a1_modules","paper02_full"]
test_total.keys = ["passed","failed","skipped","xfailed","xpassed","wall_duration_ms"]
test_totals.prefreeze_focused.passed = 23
test_totals.l3_a1_modules.passed = 972
test_totals.paper02_full.passed = 1951
held_out_policy.held_out_l3_scientific_outputs_read = false
held_out_policy.held_out_l3_evaluator_dispatched = false
held_out_policy.scientific_evaluator_dispatch_count = 0
held_out_policy.new_archive_scope = "TEMPORARY_MOCK_ONLY"
held_out_policy.s0_archive_access = "READ_ONLY_SEALED_PUBLIC_SIX_CELL"
held_out_policy.canonical_result_created = false
recorded_at_utc.regex = "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
repository_snapshot.keys = ["authority_root","branch","capture_commit_oid","capture_tree_oid","origin_url","origin_main_oid","live_remote_main_oid","head_equals_origin_main","head_equals_live_remote_main","ahead","behind","worktree_clean_before","worktree_clean_after"]
repository_snapshot.authority_root = <ROLE10_FILESYSTEM_PROJECT_ROOT>
repository_snapshot.branch = "main"
repository_snapshot.origin_url = "git@github.com:maris205/hilbert-polya-structure.git"
repository_snapshot.capture_commit_oid = LOWERCASE_GIT_COMMIT_40_HEX
repository_snapshot.capture_tree_oid = LOWERCASE_GIT_TREE_40_HEX
repository_snapshot.origin_main_oid = <CAPTURE_COMMIT_OID>
repository_snapshot.live_remote_main_oid = <CAPTURE_COMMIT_OID>
repository_snapshot.head_equals_origin_main = true
repository_snapshot.head_equals_live_remote_main = true
repository_snapshot.ahead = 0
repository_snapshot.behind = 0
repository_snapshot.worktree_clean_before = true
repository_snapshot.worktree_clean_after = true
prerequisite_bindings.keys = ["machine_role10","s0_compatibility_role13","second_fresh_rebuild_replay","canonical_absence"]
prerequisite_bindings.machine_role10.keys = ["role","path","sha256","size_bytes","mode","nlink","publication_commit_oid","producer_path","producer_sha256","verifier_path","verifier_sha256","verify_receipt","promotion_authorized"]
prerequisite_bindings.machine_role10.role = "machine_freeze"
prerequisite_bindings.machine_role10.path = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"
prerequisite_bindings.machine_role10.mode = "0644"
prerequisite_bindings.machine_role10.nlink = 1
prerequisite_bindings.machine_role10.producer_path = "scripts/run_r401_val_l3_a1_v2_all_slabs.py"
prerequisite_bindings.machine_role10.verifier_path = "scripts/build_r401_val_l3_a1_v2_release_provenance.py"
prerequisite_bindings.machine_role10.promotion_authorized = false
prerequisite_bindings.s0_compatibility_role13.keys = ["role","path","sha256","size_bytes","mode","nlink","publication_commit_oid","producer_path","producer_sha256","verify_receipt","promotion_authorized"]
prerequisite_bindings.s0_compatibility_role13.role = "s0_compatibility"
prerequisite_bindings.s0_compatibility_role13.path = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"
prerequisite_bindings.s0_compatibility_role13.mode = "0644"
prerequisite_bindings.s0_compatibility_role13.nlink = 1
prerequisite_bindings.s0_compatibility_role13.producer_path = "scripts/replay_r401_val_l3_s0_through_a1_v2_checkers.py"
prerequisite_bindings.s0_compatibility_role13.promotion_authorized = false
prerequisite_bindings.verify_receipt.keys = ["verification_status","authority","candidate_sha256","size_bytes","promotion_authorized"]
prerequisite_bindings.machine_role10.verify_receipt.verification_status = "PASS_MACHINE_FREEZE_VERIFY_ONLY"
prerequisite_bindings.s0_compatibility_role13.verify_receipt.verification_status = "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
prerequisite_bindings.verify_receipt.authority = "NON_AUTHORITATIVE_VERIFY_ONLY"
prerequisite_bindings.verify_receipt.promotion_authorized = false
prerequisite_bindings.second_fresh_rebuild_replay.keys = ["command_result_name","command_result_sha256","semantic_receipt"]
prerequisite_bindings.second_fresh_rebuild_replay.command_result_name = "second_fresh_rebuild"
prerequisite_bindings.second_fresh_rebuild_replay.command_result_sha256 = <CJ_COMPACT_V1_SHA256_OF_COMMAND_RESULT_6>
prerequisite_bindings.second_fresh_rebuild_replay.semantic_receipt = <COMMAND_RESULT_6_SEMANTIC_RECEIPT>
prerequisite_bindings.canonical_absence.keys = ["prefreeze_review_role12_exists","main_freeze_role54_exists","canonical_result_root_exists","canonical_operational_root_exists"]
prerequisite_bindings.canonical_absence.prefreeze_review_role12_path = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md"
prerequisite_bindings.canonical_absence.main_freeze_role54_path = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json"
prerequisite_bindings.canonical_absence.canonical_result_root = "results/r401_val_l3_a1_v2_all_slabs"
prerequisite_bindings.canonical_absence.canonical_operational_root = "results/r401_val_l3_a1_v2_all_slabs.operational"
prerequisite_bindings.canonical_absence.all_values = false
pytest_counts.keys = ["passed","failed","skipped","xfailed","xpassed"]
pytest_counts.prefreeze_focused = {"passed":23,"failed":0,"skipped":0,"xfailed":0,"xpassed":0}
pytest_counts.l3_a1_modules = {"passed":972,"failed":0,"skipped":0,"xfailed":0,"xpassed":0}
pytest_counts.paper02_full = {"passed":1951,"failed":0,"skipped":0,"xfailed":0,"xpassed":0}
command_result.pytest_counts_by_kind = {"VERIFY_MACHINE_FREEZE":null,"VERIFY_S0_COMPATIBILITY":null,"PYTEST_FOCUSED":{"passed":23,"failed":0,"skipped":0,"xfailed":0,"xpassed":0},"PYTEST_L3_A1":{"passed":972,"failed":0,"skipped":0,"xfailed":0,"xpassed":0},"PYTEST_PAPER02":{"passed":1951,"failed":0,"skipped":0,"xfailed":0,"xpassed":0},"GIT_DIFF_CHECK":null,"SECOND_FRESH_REBUILD":null}
command_result.semantic_receipt_by_kind = {"VERIFY_MACHINE_FREEZE":<EXACT_VERIFY_RECEIPT>,"VERIFY_S0_COMPATIBILITY":<EXACT_VERIFY_RECEIPT>,"PYTEST_FOCUSED":null,"PYTEST_L3_A1":null,"PYTEST_PAPER02":null,"GIT_DIFF_CHECK":null,"SECOND_FRESH_REBUILD":<EXACT_SECOND_REBUILD_RECEIPT>}
second_fresh_rebuild_receipt.keys = ["verification_status","authority","source_path","source_sha256","persistent_binary_path","persistent_before_sha256","persistent_after_sha256","persistent_before_device_id","persistent_before_inode","persistent_after_device_id","persistent_after_inode","persistent_identity_unchanged","persistent_overwrite_performed","staging_output_sha256","staging_output_size_bytes","staging_output_mode","staging_output_removed","byte_for_byte_equal","scientific_evaluator_dispatched"]
second_fresh_rebuild_receipt.verification_status = "PASS_SECOND_FRESH_REBUILD"
second_fresh_rebuild_receipt.authority = "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY"
second_fresh_rebuild_receipt.source_path = "validated/capd_r401_phase_branch_tube_mp_a1.cpp"
second_fresh_rebuild_receipt.persistent_binary_path = "validated/bin/capd_r401_phase_branch_tube_mp_a1"
second_fresh_rebuild_receipt.persistent_identity_unchanged = true
second_fresh_rebuild_receipt.persistent_overwrite_performed = false
second_fresh_rebuild_receipt.staging_output_mode = "0755"
second_fresh_rebuild_receipt.staging_output_removed = true
second_fresh_rebuild_receipt.byte_for_byte_equal = true
second_fresh_rebuild_receipt.scientific_evaluator_dispatched = false
command.cwd = <ROLE10_FILESYSTEM_PROJECT_ROOT>
command.environment = {"PATH":"/root/miniconda3/bin:/usr/bin:/bin","LANG":"C.UTF-8","LC_ALL":"C.UTF-8","TZ":"UTC","PYTHONHASHSEED":"0","PYTHONNOUSERSITE":"1","PYTHONDONTWRITEBYTECODE":"1","PYTEST_DISABLE_PLUGIN_AUTOLOAD":"1","OMP_NUM_THREADS":"1","OPENBLAS_NUM_THREADS":"1","MKL_NUM_THREADS":"1","NUMEXPR_NUM_THREADS":"1","GIT_CONFIG_NOSYSTEM":"1","GIT_CONFIG_GLOBAL":"/dev/null"}
command.return_code = 0
command.wall_duration_ms.range = [1,603000]
command.stdout_utf8.max_bytes = 1048576
command.stderr_utf8.max_bytes = 1048576
command.stderr_utf8 = ""
command_argv_templates[0] = ["<PYTHON>","<AUTHORITY_ROOT>/scripts/build_r401_val_l3_a1_v2_release_provenance.py","--verify-machine-freeze","<AUTHORITY_ROOT>/research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"]
command_argv_templates[1] = ["<PYTHON>","<AUTHORITY_ROOT>/scripts/build_r401_val_l3_a1_v2_release_provenance.py","--verify-s0-compatibility","<AUTHORITY_ROOT>/research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"]
command_argv_templates[2] = ["<PYTHON>","-m","pytest","-q","-p","no:cacheprovider","--color=no","tests/test_r401_val_l3_a1_v2_adversarial_e2e.py"]
command_argv_templates[3] = ["<PYTHON>","-m","pytest","-q","-p","no:cacheprovider","--color=no","tests/test_r401_val_l3_a1_static_cell.py","tests/test_r401_val_l3_a1_v2_static_scheduler.py","tests/test_r401_val_l3_a1_v2_static_checker.py","tests/test_r401_val_l3_a1_v2_branch_scheduler.py","tests/test_r401_val_l3_a1_v2_branch_checker.py","tests/test_r401_val_l3_a1_v2_s0_compatibility.py","tests/test_r401_val_l3_a1_v2_composite_contract.py","tests/test_r401_val_l3_a1_v2_adversarial_e2e.py","tests/test_r401_val_l3_a1_v2_release_provenance.py"]
command_argv_templates[4] = ["<PYTHON>","-m","pytest","-q","-p","no:cacheprovider","--color=no"]
command_argv_templates[5] = ["/usr/bin/git","diff","--check","HEAD","--"]
command_argv_templates[6] = ["<PYTHON>","<AUTHORITY_ROOT>/scripts/run_r401_val_l3_a1_v2_all_slabs.py","--second-fresh-rebuild-only","--output","<OWNED_TMP_REBUILD_OUTPUT>"]
python_token = <ROLE10_PYTHON_EXECUTABLE_PATH>
owned_tmp_rebuild_output.regex = "^/tmp/a416-l3a1-v2-role11-rebuild\\.[0-9A-Za-z]{6,}/capd_r401_phase_branch_tube_mp_a1$"
implementation_only_runner.shell_used = false
implementation_only_runner.umask = "0022"
implementation_only_runner.timeout_seconds = 600
implementation_only_runner.term_grace_seconds = 2
implementation_only_runner.pipe_close_grace_seconds = 1
candidate.max_bytes = 4194304
candidate.path_shape = "/tmp/<EMPTY_OWNED_MODE_0700_DIRECTORY>/<BASENAME>"
candidate.file_mode = "0600"
candidate.nlink = 1
canonical.file_mode = "0644"
canonical.nlink = 1
publication.method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
final_mechanical_lock.required_before_capture_verify_publish = true
final_mechanical_lock.state = "LOCKED"
final_mechanical_lock.role19_final_command_locked = true
final_mechanical_lock.expected_test_passed = {"prefreeze_focused":23,"l3_a1_modules":972,"paper02_full":1951}
final_mechanical_lock.literals = ["seven_command_argv_templates","command_environment","producer_sha256_size_mode_nlink","independent_checker_sha256_size_mode_nlink","focused_test_sha256_size_mode_nlink","prefreeze_focused_passed","l3_a1_modules_passed","paper02_full_passed"]
covered_gates = ["EXACT_51_ROLE_ORDER_AND_SAME_BYTE_SNAPSHOTS","CANONICAL_ROLE10_AND_ROLE13_REPLAY","SEVEN_FIXED_COMMAND_IDENTITIES","BOUNDED_RAW_UTF8_TRANSCRIPT_REHASH","PYTEST_SUMMARY_REPARSE_AND_ZERO_NONPASS_COUNTS","CLEAN_REPOSITORY_AND_FIXED_ENVIRONMENT","PROCESS_GROUP_TIMEOUT_AND_DESCENDANT_CLEANUP","SECOND_REBUILD_NO_OVERWRITE_BYTE_EQUALITY","STRICT_SCHEMA_TYPES_PATHS_LINKS_AND_TOCTOU_REPLAY","INDEPENDENT_CHECKER_SOURCE_SEPARATION","WRITE_ONCE_FIXED_DESTINATION_NOREPLACE_PUBLICATION"]
```
<!-- END A416_L3_A1_CONTROL_V2_ROLE11_CONTRACT -->

Each role-11 `publication_commit_oid` for roles 10 and 13 is the exact
historical introduction commit, not merely a later commit that contains the
same bytes.  Starting at `repository_snapshot.capture_commit_oid`, a bounded
pure-Git first-parent walk must reach the recorded introduction; every tree
from capture through that introduction must retain the exact regular
blob/mode/digest bound by role 11; the introduction must be an ordinary
single-parent commit whose unique parent has the path absent; and every
still-older first-parent tree through the root must keep the path absent.
Merge/root introductions, cycles, unreachable orphans, intervening drift or
deletion, and delete-then-readd histories are rejected.  Capture discovers
and proves this history from Git objects; independent verification repeats
it without a subprocess.

The three tool hash/size/mode/nlink items in the final mechanical lock are
captured evidence facts, not literals embedded in roles 19 or 24.  Each must
equal both its live `pre_review_input_roles` entry and the corresponding
canonical role-5 `reviewed_v2_inputs` entry for roles 19, 24, and 32.  This
three-way cross-binding is mandatory and avoids an impossible source
self-hash.  Source literals lock only the seven argv/environment identities
and the three final positive pytest passed totals.

The role-54 temporary candidate is exactly
`/tmp/<owned-mode-0700-singleton>/<leaf>`: its parent is an otherwise empty
direct child of `/tmp` owned by the invoking uid, and the candidate is a
regular `0600`, `nlink=1` file of at most 1048576 bytes.  A future role-24
same-parent publication stage and fixed destination are instead regular
`0644`, `nlink=1`; candidate mode is never reused as canonical mode.

The twelve fixed publisher-routing authority literals are
`ROLE19_MACHINE_FREEZE_PUBLICATION_ONLY`,
`ROLE19_PREFREEZE_TESTS_PUBLICATION_ONLY`,
`ROLE19_RUN_CONFIG_PUBLICATION_ONLY`,
`ROLE19_COMPONENT_AGGREGATES_PUBLICATION_ONLY`,
`ROLE19_COMPOSITE_PRODUCER_PUBLICATION_ONLY`,
`ROLE20_STATIC_CHECKER_PUBLICATION_ONLY`,
`ROLE21_BRANCH_CHECKER_PUBLICATION_ONLY`,
`ROLE22_COMPOSITE_CHECKER_PUBLICATION_ONLY`,
`ROLE23_ADAPTER_PUBLICATION_ONLY`,
`ROLE24_MAIN_FREEZE_PUBLICATION_ONLY`,
`ROLE24_REPORT_PUBLICATION_ONLY`, and
`ROLE24_RELEASE_PROVENANCE_PUBLICATION_ONLY`.  They are final CLI routing
literals, not upgradeable authorization slots and not automatic permission.
Roles 20, 21, and 22 use their one purpose-separated literal for their fixed
checker and matching postcheck destinations only.  Each write-once edge
still requires its explicit publish mode, absolute private candidate path,
and caller-supplied expected SHA-256.  The three formal role-19 publishers
and all three role-24 publishers additionally require the matching
`--publication-authority` literal.  Role 23 instead fixes its token inside
the source and requires the exact publish mode, expected SHA-256, and live
authority root without any override flag.  No such mode is invoked by this
implementation checkpoint.

Role 11 serializes exactly seven evidence command results.  Separately, each
pre-command, post-command, and post-candidate terminal repository snapshot
runs two fixed, nonserialized plumbing probes:
`["/usr/bin/git","-C","<REPOSITORY_ROOT>","ls-remote","--heads","origin","refs/heads/main"]`
and
`["/usr/bin/git","-C","<REPOSITORY_ROOT>","status","--porcelain=v1","--untracked-files=all"]`.
Both use the exact 14-key clean environment, `shell=false`, a 60-second
timeout, 1 MiB stream caps, and process-group/subreaper termination with the
original subreaper state restored.  Each requires return code zero and empty
stderr; status stdout is empty, while ls-remote stdout is exactly
`<40-lowercase-hex>\trefs/heads/main\n`.  All three live OIDs equal the
captured commit and origin/main OID.  `origin_url` is independently parsed
as the unique exact origin URL from the pinned `.git/config`; global and
system configuration are disabled, and any `include`, `includeIf`, `url.*`
rewrite section, `insteadOf`, or `pushInsteadOf` directive is fatal.  Role 24 historical verification replays the
recorded commit/tree/index and local remote-tracking ref with zero
subprocesses; it never represents that local ref as a current network
observation, and its independent preflight performs any new live probe.

The empty-status rule above governs role-11 candidate capture.  The separate
role-11 publisher has an exact transient status state machine under a
nonblocking destination-parent flock: pre-stage status is empty; immediately
before rename it is exactly one porcelain line for this call's owned hidden
stage and that leaf still has the pinned stage inode; after rename it is
exactly one porcelain line for the fixed V2 role-11 canonical path and that
leaf has the published inode.  Cached changes, quoting ambiguity, any second
line, or any other tracked or untracked path reported by that exact porcelain
command are rejected.  Ordinary ignored cache paths are outside this Git-clean
signal; fixed forbidden authority, result, and operational namespaces are
independently checked by no-follow namespace replay, so ignored entries there
remain fatal.  The live-remote
probe is repeated at every publication replay.  Exactly one concurrent
publisher can win; pre-rename failure removes only the pinned owned stage,
whereas every post-rename failure is reported without rollback.

The focused command runs role 32.  The nine-module command runs role 25 and
V2 roles 26--33 in exact role order.  The full command runs the complete
Paper02 suite.  The two verify commands execute role 24's machine and S0
verify-only modes; the rebuild command executes role 19's no-overwrite
second-rebuild mode.  None may dispatch roles 15 or 17 as a scientific
evaluator; import-only unit tests of role-15 helpers and synthetic executable
fixtures remain non-dispatching.

The final three passing pytest counts and the role-19, role-24, and role-32
file facts are now mechanically locked in the shared contract block above.
The earlier unset expected-count/command-lock gate was the historical
development boundary: while either role 19 or role 24 was unset, role-11
capture, verification, and publication failed closed.  The stable sources now
independently lock passed totals 23, 972, and 1951, and role 19 has its final
command lock set true.  Only argv/environment identities and passed totals are
source literals.  Tool facts remain evidence cross-bindings checked four ways:
the three tool bindings, their 51-role snapshots, canonical role-5 reviewed
bindings, and live pinned bytes/stat.  No placeholder or unset registry value
is serialized into role 11.  Any development-stage statement elsewhere that
the registries remain unset records only that completed historical boundary;
the permanent role-23 None sentinel remains separate and prevents a
role-13-to-role-11 cycle.

Role 19 may execute the seven bounded non-scientific evidence commands only
during an explicitly selected role-11 capture.  It writes a private
temporary `0600` candidate, replays the live probes, pure-Git history, all 51
roles, three tool bindings, downstream-absence namespace, and the full pinned
candidate file and `/tmp` lexical parent chain as the final operation, and
does not publish implicitly.  Publication is a separate authorized Linux
same-parent `renameat2(..., RENAME_NOREPLACE)` edge to explicit `0644`, with
no fallback, identical-existing success, rollback, repair, or overwrite.
Role 24 verifies the candidate independently before publication.  Role 19's
publisher pins and replays every lexical directory component from the
authority root through the destination parent and from `/tmp` through the
candidate parent before rename, after rename, and again after its final fault
hook; its last operation is a full canonical/candidate/input/Git/namespace
replay, with no later hook before returning its transient receipt.  Role 11
remains non-licensing and cannot authorize role 12, role 54, initialization,
or dispatch by itself.

<!-- BEGIN A416_L3_A1_CONTROL_V2_PUBLICATION_RECEIPTS -->

Normative transient role-24 publication receipts:

Role 24's three publisher APIs return a strict receipt mapping, and their CLI
modes write exactly its CJ-COMPACT-V1 bytes (including one terminal LF) to
stdout.  No receipt is written to a canonical path, retained as an artifact,
or inserted into the 53-role or 68-role map.  The exact schemas are:

~~~text
common_top_level_key_count = 17
common_top_level_keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate","canonical","publication_method","independent_postpublication_verification_performed","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","claim_boundary","component_status","milestone_status","theorem_status","final_status"]
main_receipt_top_level_key_count = 20
main_receipt_top_level_keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate","canonical","publication_method","independent_postpublication_verification_performed","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","claim_boundary","component_status","milestone_status","theorem_status","final_status","input_role_count","ordered_input_roles_sha256","checker_receipt_sha256"]
report_receipt_top_level_key_count = 20
report_receipt_top_level_keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate","canonical","publication_method","independent_postpublication_verification_performed","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","claim_boundary","component_status","milestone_status","theorem_status","final_status","upstream_role_count","ordered_upstream_roles_sha256","archive_generation_sha256"]
release_receipt_top_level_key_count = 21
release_receipt_top_level_keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate","canonical","publication_method","independent_postpublication_verification_performed","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","claim_boundary","component_status","milestone_status","theorem_status","final_status","role_count","ordered_roles_sha256","main_freeze_sha256","archive_generation_sha256"]
candidate.keys = ["path","sha256","size_bytes","mode","nlink","fingerprint"]
canonical.keys = ["path","sha256","size_bytes","mode","nlink","fingerprint"]
fingerprint.keys = ["device_id","inode","size_bytes","mtime_ns","ctime_ns","mode","nlink"]
schema_version = 1
protocol_id = "R401-VAL-L3-A1"
artifact_status = "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY"
publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
independent_postpublication_verification_performed = false
scientific_licensing_enabled = false
production_authorized = false
scientific_dispatch_performed = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
candidate.mode = "0600"
candidate.nlink = 1
canonical.mode = "0644"
canonical.nlink = 1
main.artifact_role = "MAIN_FREEZE_PUBLICATION_RECEIPT"
main.authority = "ROLE24_MAIN_FREEZE_PUBLICATION_ONLY"
main.input_role_count = 53
main.checker_receipt_sha256.keys = ["static","branch","composite"]
main.claim_boundary = "role-24 write-once transport evidence for the exact role-54 main freeze only; no independent postpublication verification, scientific licensing, production authorization, promotion, or dispatch authority"
report.artifact_role = "PRODUCTION_REPORT_PUBLICATION_RECEIPT"
report.authority = "ROLE24_REPORT_PUBLICATION_ONLY"
report.upstream_role_count = 14
report.claim_boundary = "role-24 write-once transport evidence for the exact role-68 five-line report only; no independent postpublication verification, scientific licensing, production authorization, promotion, or dispatch authority"
release.artifact_role = "RELEASE_PROVENANCE_PUBLICATION_RECEIPT"
release.authority = "ROLE24_RELEASE_PROVENANCE_PUBLICATION_ONLY"
release.role_count = 68
release.claim_boundary = "role-24 write-once transport evidence for the exact 68-role release provenance only; no independent postpublication verification, scientific licensing, production authorization, promotion, or dispatch authority"
~~~

Each path, digest, and outer mode is a JSON string.  Each size_bytes, nlink,
and all seven fingerprint values are strict JSON integers with Booleans
rejected.  In particular, outer candidate.mode and canonical.mode are the
four-character permission strings above, while nested fingerprint.mode is
the full integer st_mode; it must describe a regular file and its permission
bits must equal the outer mode.  Fingerprint nlink is one, positive inode and
nonnegative device/size/time values are required, and repeated
size/mode/nlink values must agree.  Candidate and canonical bindings have
identical raw bytes, digest, and size; the candidate path is exact
/tmp/<owned-0700-nlink2-singleton>/<leaf>, and the canonical path is the
applicable fixed role-54, role-68 report, or release destination.

For the main receipt,
ordered_input_roles_sha256 = SHA256(CJ_COMPACT_V1(input_roles)), including
the serializer's one terminal LF, over the exact ordered 53 role-54 inputs.
checker_receipt_sha256 has exactly the ordered names static, branch,
composite; each value is the SHA-256 of that checker's actual raw seven-key
CJ-COMPACT-V1 verify-only receipt, including its LF.  The three receipts are
supplied only with --publish-main-freeze through exact CLI options
--role20-receipt, --role21-receipt, and --role22-receipt.  Each is a distinct
regular 0600, nlink=1, at-most-1048576-byte file in its own
otherwise-singleton euid-owned 0700, nlink=2 direct child of /tmp; their paths
and inodes are pairwise distinct and are replayed through the ultimate
post-rename check.  Each receipt has exactly:

~~~text
checker_verify_receipt.keys = ["verification_status","authority","candidate_sha256","input_map_sha256","size_bytes","promotion_authorized","artifacts_written"]
checker_verify_receipt.verification_status = "PASS_MAIN_FREEZE_VERIFY_ONLY"
checker_verify_receipt.authority = "NON_AUTHORITATIVE_VERIFY_ONLY"
checker_verify_receipt.promotion_authorized = false
checker_verify_receipt.artifacts_written = false
checker_verify_receipt.candidate_sha256 = <ROLE54_CANDIDATE_RAW_SHA256>
checker_verify_receipt.input_map_sha256 = <ORDERED_53_INPUT_ROLES_CJ_COMPACT_V1_SHA256>
checker_verify_receipt.size_bytes = <ROLE54_CANDIDATE_RAW_SIZE>
~~~

For the report receipt,
ordered_upstream_roles_sha256 = SHA256(CJ_COMPACT_V1(upstream_roles)), including
one LF, over the exact ordered 14 rows for role 54 and roles 55--67, each row
having exactly `role`, `path`, and `sha256`.  `archive_generation_sha256`
equals the independently replayed composite generation.  Role 24 alone owns
`build_report_candidate`, `verify_report_candidate`, and `publish_report` and
the exact CLI XOR modes `--build-report-candidate ABSOLUTE_MD_PATH`,
`--verify-report ABSOLUTE_MD_PATH`, and `--publish-report ABSOLUTE_MD_PATH`.
Publication additionally requires `--expected-candidate-sha256` and
`--publication-authority ROLE24_REPORT_PUBLICATION_ONLY`; checker-receipt CLI
options are forbidden.  The private candidate is exactly
`/tmp/<euid-owned-0700-nlink2-singleton>/R401_VAL_L3_A1_REPORT.md`, regular
0600, nlink one, and at most 4096 bytes; the canonical is the fixed role-68
path, regular 0644 and nlink one.  Its bytes are exactly these five ASCII
lines with one final LF and no other bytes:

~~~text
Status: PASS_LOCAL_PHASE_TUBE_ALL_SLABS
milestone_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
theorem_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
final_status = null
Claim boundary: complete-period local-tube candidate uniqueness modulo time translation and distinguished-branch tube membership only; no global routing, trace-formula, Hilbert-Polya, zeta-zero, or RH promotion
~~~

Report verify returns this transient exact seven-key mapping and writes no
artifact:

~~~text
report_verify_receipt.keys = ["verification_status","authority","candidate_sha256","ordered_upstream_roles_sha256","size_bytes","promotion_authorized","artifacts_written"]
report_verify_receipt.verification_status = "PASS_PRODUCTION_REPORT_VERIFY_ONLY"
report_verify_receipt.authority = "NON_AUTHORITATIVE_VERIFY_ONLY"
report_verify_receipt.promotion_authorized = false
report_verify_receipt.artifacts_written = false
~~~

For the release receipt,
ordered_roles_sha256 = SHA256(CJ_COMPACT_V1(roles)), including one LF, over
the exact ordered 68-role array.  Its main_freeze_sha256 and
archive_generation_sha256 equal the independently rebuilt release envelope.
All three transport receipts deliberately keep all licensing, production,
dispatch, verification, and scientific status fields false or null; a true
licensing field in the underlying role-54 or release artifact never
propagates into its transport receipt.

<!-- END A416_L3_A1_CONTROL_V2_PUBLICATION_RECEIPTS -->

<!-- BEGIN A416_L3_A1_CONTROL_V2_FORMAL_PRODUCER_PUBLICATION -->

Normative transient role-19 formal-producer publication receipts:

Role 19 owns exactly these three source literals; possessing a literal never
authorizes publication, and every publisher also requires the exact explicit
CLI mode, private candidate, expected digest or digest pair, and live V2
authority replay:

~~~text
role55.publication_authority = "ROLE19_RUN_CONFIG_PUBLICATION_ONLY"
component_pair.publication_authority = "ROLE19_COMPONENT_AGGREGATES_PUBLICATION_ONLY"
composite_pair.publication_authority = "ROLE19_COMPOSITE_PRODUCER_PUBLICATION_ONLY"
publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
~~~

The role-55 candidate is one regular 0600, nlink-one, at-most-4194304-byte
CJ-COMPACT-V1 file in an otherwise-singleton, euid-owned 0700, nlink-two
direct child of /tmp.  Publication creates a fresh hidden directory under
'results', pins and explicitly chmods that directory to 0755, writes its
sole 'run_config.json' as regular 0644/nlink one, fsyncs file and directories,
and makes the fixed
'results/r401_val_l3_a1_v2_all_slabs' directory visible only through Linux
same-parent renameat2(..., RENAME_NOREPLACE).  Existing identical content is
fatal and there is no rename, replace, link, or portable fallback.  The
transient role-55 receipt has exactly ten top-level keys:

~~~text
role55_receipt.key_count = 10
role55_receipt.keys = ["publication_status","authority","artifact_role","candidate_sha256","canonical_path","canonical_sha256","publication_method","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed"]
role55_receipt.publication_status = "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY"
role55_receipt.authority = "ROLE19_RUN_CONFIG_PUBLICATION_ONLY"
role55_receipt.artifact_role = "RUN_CONFIG_PUBLICATION_RECEIPT"
role55_receipt.canonical_path = "results/r401_val_l3_a1_v2_all_slabs/run_config.json"
role55_receipt.publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
role55_receipt.scientific_licensing_enabled = false
role55_receipt.production_authorized = false
role55_receipt.scientific_dispatch_performed = false
~~~

A component or composite candidate package is exactly one euid-owned 0700,
nlink-two directory directly below /tmp with exactly two regular 0600,
nlink-one, at-most-4194304-byte CJ-COMPACT-V1 leaves.  Component leaves are
'aggregate_summary.json' and 'aggregate_manifest.json'; composite leaves are
'composite_summary.json' and 'composite_manifest.json'.  Component publication
targets the fixed static or branch directory.  Composite publication targets
the fixed result root.  Both are same-parent write-once pair transactions:
summary is renamed first, manifest is the commit marker and is renamed last.
Any post-summary failure leaves summary in place, never rolls it back or
repairs it, permanently invalidates that result generation, and makes every
retry against the existing summary fatal; a retry requires a fresh result
generation.  Existing identical content is never success.  Each transient
pair receipt has exactly sixteen top-level keys, and each nested artifact
binding has exactly five:

~~~text
pair_receipt.key_count = 16
pair_receipt.keys = ["publication_status","authority","artifact_kind","candidate_package","summary","manifest","archive_generation_sha256","publication_method","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","independent_postpublication_verification_performed","component_status","milestone_status","theorem_status","final_status"]
pair_receipt.summary.keys = ["path","sha256","size_bytes","mode","nlink"]
pair_receipt.manifest.keys = ["path","sha256","size_bytes","mode","nlink"]
pair_receipt.publication_status = "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY"
pair_receipt.publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
pair_receipt.summary.mode = "0644"
pair_receipt.summary.nlink = 1
pair_receipt.manifest.mode = "0644"
pair_receipt.manifest.nlink = 1
pair_receipt.scientific_licensing_enabled = false
pair_receipt.production_authorized = false
pair_receipt.scientific_dispatch_performed = false
pair_receipt.independent_postpublication_verification_performed = false
pair_receipt.component_status = null
pair_receipt.milestone_status = null
pair_receipt.theorem_status = null
pair_receipt.final_status = null
static_pair.authority = "ROLE19_COMPONENT_AGGREGATES_PUBLICATION_ONLY"
static_pair.artifact_kind = "static_component_aggregate_pair"
branch_pair.authority = "ROLE19_COMPONENT_AGGREGATES_PUBLICATION_ONLY"
branch_pair.artifact_kind = "branch_component_aggregate_pair"
composite_pair.authority = "ROLE19_COMPOSITE_PRODUCER_PUBLICATION_ONLY"
composite_pair.artifact_kind = "composite_producer_pair"
~~~

The six formal producer CLI modes are an exact XOR and retain raw lexical path
spellings until the absolute-path gate:

~~~text
build_role55 = ["--build-formal-run-config-candidate","--authority-root","--output"]
publish_role55 = ["--publish-formal-run-config","--authority-root","--candidate","--expected-sha256","--publication-authority"]
build_component_pair = ["--build-formal-component-aggregate-candidates","--authority-root","--output","--component"]
publish_component_pair = ["--publish-formal-component-aggregates","--authority-root","--candidate","--expected-summary-sha256","--expected-manifest-sha256","--publication-authority","--component"]
build_composite_pair = ["--build-formal-composite-candidates","--authority-root","--output"]
publish_composite_pair = ["--publish-formal-composite-candidates","--authority-root","--candidate","--expected-summary-sha256","--expected-manifest-sha256","--publication-authority"]
component.values = ["STATIC","BRANCH"]
~~~

Any extra legacy, mock, prefreeze, initialization, production, evaluator, or
scientific-dispatch option is fatal even when its supplied numeric value is
zero.  CLI receipts are exact CJ-COMPACT-V1 plus one terminal LF.  Publication
receipts are transport-only, are never persisted or inserted into the 53/68
role maps, and confer no checker, postcheck, licensing, production, theorem,
promotion, or dispatch authority.  Every candidate and each hook boundary
replays the same full live generation: pinned role 54/55 inputs, exact 102-cell
namespace and raw producer ABI, component controls, operational absence,
candidate package, canonical namespace, modes, links, inodes, timestamps, and
ancestor chains.  During development the three entries of the pytest
passed-count registry were unset and every live capture/publication authority
path failed closed.  They are now mechanically locked to 23, 972, and 1951;
the role-11 authority path enforces those exact totals.  All scientific dispatch remains an
unconditional hard stop.

<!-- END A416_L3_A1_CONTROL_V2_FORMAL_PRODUCER_PUBLICATION -->

<!-- BEGIN A416_L3_A1_CONTROL_V2_ROLE23_RECEIPTS -->

Normative role-23 S0-adapter modes and transient receipts:

Role 23 alone captures, verifies, and publishes the fixed role-13 object at
'research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json'.
The three raw CLI modes are an exact XOR:

~~~text
capture_mode = ["--capture-s0-compatibility","--output"]
verify_mode = ["--verify-s0-compatibility","ABSOLUTE_JSON_PATH"]
publish_mode = ["--publish-s0-compatibility","--candidate","--expected-sha256","--authority-root"]
publication_authority = "ROLE23_ADAPTER_PUBLICATION_ONLY"
publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
~~~

Capture and publication candidates are absolute lexical descendants of
/tmp, outside the project tree, and are regular 0600/nlink-one
CJ-COMPACT-V1 files of at most 1048576 bytes.  Every ancestor is opened with
no symlink traversal and the pinned parent chain and file image are replayed;
role 23 does not require a singleton or fixed-mode immediate parent.
Publication uses only Linux
same-parent renameat2(..., RENAME_NOREPLACE), fsyncs the file and parent,
publishes the fixed canonical as regular 0644/nlink one, rejects existing
identical content, and has no overwrite, repair, link, rename, replace, or
portable fallback.  Each successful mode writes exactly its transient
CJ-COMPACT-V1 receipt with one terminal LF to stdout and writes no receipt
artifact.  The schemas and literals are exact:

~~~text
capture_receipt.key_count = 18
capture_receipt.keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate_path","candidate_sha256","size_bytes","mode","nlink","serializer","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","component_status","milestone_status","theorem_status","final_status"]
capture_receipt.schema_version = 1
capture_receipt.protocol_id = "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY"
capture_receipt.artifact_role = "TEMP_S0_COMPATIBILITY_CANDIDATE_RECEIPT"
capture_receipt.artifact_status = "CAPTURED_VALIDATED_TEMP_ONLY"
capture_receipt.authority = "NON_AUTHORITATIVE_CAPTURE_ONLY"
capture_receipt.mode = "0600"
capture_receipt.nlink = 1
capture_receipt.serializer = "CJ_COMPACT_V1"
verify_receipt.key_count = 5
verify_receipt.keys = ["verification_status","authority","candidate_sha256","size_bytes","promotion_authorized"]
verify_receipt.verification_status = "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
verify_receipt.authority = "NON_AUTHORITATIVE_VERIFY_ONLY"
verify_receipt.promotion_authorized = false
publication_receipt.key_count = 21
publication_receipt.keys = ["schema_version","protocol_id","artifact_role","artifact_status","authority","candidate_path","canonical_path","compatibility_sha256","size_bytes","mode","nlink","serializer","publication_method","independent_verification_performed","scientific_licensing_enabled","production_authorized","scientific_dispatch_performed","component_status","milestone_status","theorem_status","final_status"]
publication_receipt.schema_version = 1
publication_receipt.protocol_id = "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY"
publication_receipt.artifact_role = "S0_COMPATIBILITY_PUBLICATION_RECEIPT"
publication_receipt.artifact_status = "PUBLISHED_WRITE_ONCE_NON_LICENSING"
publication_receipt.authority = "ROLE23_ADAPTER_PUBLICATION_ONLY"
publication_receipt.mode = "0644"
publication_receipt.nlink = 1
publication_receipt.serializer = "CJ_COMPACT_V1"
publication_receipt.publication_method = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
publication_receipt.independent_verification_performed = false
~~~

For both 18- and 21-key receipts, scientific_licensing_enabled,
production_authorized, and scientific_dispatch_performed are false and all
four status fields are null.  Every digest, size, path, mode, and inode is
replayed through the final namespace observation.  These receipts are
non-licensing transport evidence only: they do not authorize role 12, role
54, initialization, evaluator execution, production, promotion, or dispatch,
and they never enter the 53/68 role maps.

Role 23's source constant EXPECTED_PREFREEZE_TEST_PASSED remains None as a
permanent upstream-S0 sentinel and must not be filled during the role-11
mechanical count lock; binding it to role-11 results would create a forbidden
role-13-to-role-11 cycle.  The later passed-count lock applies only to roles
19, 20, 21, 22, and 24.

<!-- END A416_L3_A1_CONTROL_V2_ROLE23_RECEIPTS -->

<!-- BEGIN A416_L3_A1_CONTROL_V2_ORDERED_53 -->
```text
01	a416_derivation	research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md
02	s0_protocol	research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md
03	s0_report	research/route_a_wave_trace/A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md
04	prefreeze_design	research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_DESIGN.md
05	implementation_design_review	research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json
06	formal_protocol	research/route_a_wave_trace/R401_VAL_L3_A1_V2_PROTOCOL.md
07	scheduler_contract	research/route_a_wave_trace/R401_VAL_L3_A1_V2_SCHEDULER_CONTRACT.md
08	checker_contract	research/route_a_wave_trace/R401_VAL_L3_A1_V2_CHECKER_CONTRACT.md
09	release_contract	research/route_a_wave_trace/R401_VAL_L3_A1_V2_RELEASE_PROVENANCE_CONTRACT.md
10	machine_freeze	research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json
11	prefreeze_tests	research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json
12	prefreeze_review	research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md
13	s0_compatibility	research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json
14	capd_dependency	validated/CAPD_DEPENDENCY.md
15	static_evaluator	scripts/evaluate_r401_val_l3_a1_static_cell.py
16	branch_evaluator_source	validated/capd_r401_phase_branch_tube_mp_a1.cpp
17	branch_evaluator_binary	validated/bin/capd_r401_phase_branch_tube_mp_a1
18	branch_runtime	scripts/r401_val_l3_a1_branch_runtime.py
19	scheduler	scripts/run_r401_val_l3_a1_v2_all_slabs.py
20	static_checker_source	scripts/check_r401_val_l3_a1_v2_static_independent.py
21	branch_checker_source	scripts/check_r401_val_l3_a1_v2_branch_independent.py
22	composite_checker_source	scripts/check_r401_val_l3_a1_v2_composite_independent.py
23	s0_adapter	scripts/replay_r401_val_l3_s0_through_a1_v2_checkers.py
24	release_builder	scripts/build_r401_val_l3_a1_v2_release_provenance.py
25	test_static_evaluator	tests/test_r401_val_l3_a1_static_cell.py
26	test_static_scheduler	tests/test_r401_val_l3_a1_v2_static_scheduler.py
27	test_static_checker	tests/test_r401_val_l3_a1_v2_static_checker.py
28	test_branch_scheduler	tests/test_r401_val_l3_a1_v2_branch_scheduler.py
29	test_branch_checker	tests/test_r401_val_l3_a1_v2_branch_checker.py
30	test_s0_compatibility	tests/test_r401_val_l3_a1_v2_s0_compatibility.py
31	test_composite	tests/test_r401_val_l3_a1_v2_composite_contract.py
32	test_adversarial	tests/test_r401_val_l3_a1_v2_adversarial_e2e.py
33	test_release	tests/test_r401_val_l3_a1_v2_release_provenance.py
34	l1_final_plan	research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json
35	l1_summary	results/r401_val_l1_branch/summary.json
36	l1_manifest	results/r401_val_l1_branch/manifest.json
37	l1_checker	results/r401_val_l1_branch/independent_checker.json
38	l1_postcheck	results/r401_val_l1_branch/POSTCHECK_STATUS.json
39	l1_release	results/r401_val_l1_branch/RELEASE_PROVENANCE.json
40	a415_summary	results/r401_val_l2_all_slabs/aggregate_summary.json
41	a415_manifest	results/r401_val_l2_all_slabs/aggregate_manifest.json
42	a415_checker	results/r401_val_l2_all_slabs/independent_checker.json
43	a415_postcheck	results/r401_val_l2_all_slabs/POSTCHECK_STATUS.json
44	a415_release	results/r401_val_l2_all_slabs/RELEASE_PROVENANCE.json
45	s0_static_summary	results/r401_val_l3_phase_tube_smoke/summary.json
46	s0_static_manifest	results/r401_val_l3_phase_tube_smoke/manifest.json
47	s0_static_checker	results/r401_val_l3_phase_tube_smoke/independent_checker.json
48	s0_branch_summary	results/r401_val_l3_branch_tube_smoke/summary.json
49	s0_branch_manifest	results/r401_val_l3_branch_tube_smoke/manifest.json
50	s0_branch_checker	results/r401_val_l3_branch_tube_smoke/independent_checker.json
51	s0_composite_summary	results/r401_val_l3_s0_composite/summary.json
52	s0_composite_manifest	results/r401_val_l3_s0_composite/manifest.json
53	s0_composite_checker	results/r401_val_l3_s0_composite/independent_checker.json
```
<!-- END A416_L3_A1_CONTROL_V2_ORDERED_53 -->

The replaced partition is exactly roles 4--13, 19--24, and 26--33.  The
retained partition is exactly roles 1--3, 14--18, 25, and 34--53.

## Exact V2 downstream map appendix

<!-- BEGIN A416_L3_A1_CONTROL_V2_ORDERED_54_68 -->
```text
54	main_freeze	research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json
55	run_config	results/r401_val_l3_a1_v2_all_slabs/run_config.json
56	static_aggregate_summary	results/r401_val_l3_a1_v2_all_slabs/static/aggregate_summary.json
57	static_aggregate_manifest	results/r401_val_l3_a1_v2_all_slabs/static/aggregate_manifest.json
58	static_checker_result	results/r401_val_l3_a1_v2_all_slabs/independent_static_checker.json
59	static_postcheck	results/r401_val_l3_a1_v2_all_slabs/STATIC_POSTCHECK_STATUS.json
60	branch_aggregate_summary	results/r401_val_l3_a1_v2_all_slabs/branch/aggregate_summary.json
61	branch_aggregate_manifest	results/r401_val_l3_a1_v2_all_slabs/branch/aggregate_manifest.json
62	branch_checker_result	results/r401_val_l3_a1_v2_all_slabs/independent_branch_checker.json
63	branch_postcheck	results/r401_val_l3_a1_v2_all_slabs/BRANCH_POSTCHECK_STATUS.json
64	composite_summary	results/r401_val_l3_a1_v2_all_slabs/composite_summary.json
65	composite_manifest	results/r401_val_l3_a1_v2_all_slabs/composite_manifest.json
66	composite_checker_result	results/r401_val_l3_a1_v2_all_slabs/independent_checker.json
67	composite_postcheck	results/r401_val_l3_a1_v2_all_slabs/POSTCHECK_STATUS.json
68	production_report	results/r401_val_l3_a1_v2_all_slabs/R401_VAL_L3_A1_REPORT.md
```
<!-- END A416_L3_A1_CONTROL_V2_ORDERED_54_68 -->

The canonical result root is
`results/r401_val_l3_a1_v2_all_slabs`; the non-authoritative operational
sibling is `results/r401_val_l3_a1_v2_all_slabs.operational`; and the
self-excluded release object is
`results/r401_val_l3_a1_v2_all_slabs/RELEASE_PROVENANCE.json`.

## Role-5 review boundary

The fixed canonical role-5 path is
`research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json`.
Its exact 15-key top-level schema, legacy four-object manifest, ordered two P1
codes, 19 reviewed-source bindings, and zero-finding acceptance gates are
normatively defined by
`R401_VAL_L3_A1_V2_PREFREEZE_DESIGN.md`.  This increment creates neither an
external-review candidate nor the canonical object.  Its implemented tools
only verify and transport reviewer-authored bytes under the exact lifecycle
contract above.  The V2 design author must not self-authorize role 5.

## Implemented control-plane increments

The completed non-scientific control repair includes:

- V2 role 19 with strict machine capture/publication, formal 53-input
  handshake, temporary main-freeze construction, exact initialization, and
  gated scheduler transactions;
- V2 roles 20--22 with independent role-54 validation and complete formal
  static, branch, and composite checker/postcheck chains;
- V2 role 23 with exact S0 replay and write-once V2 role-13 publication;
- V2 role 24 with formal main-freeze validation/publication and formal
  68-role release validation/publication, not only mock replay;
- V2 tests 26--33 covering exact schemas, every missing role, map ordering,
  old/V2 substitution, TOCTOU, namespace safety, formal checker/postcheck
  paths, and write-once refusal; and
- the externally authored role-5 candidate gate, role-24 exact-seven
  verify-only receipt, and role-19 exact-four-tuple write-once transport; and
- new capture/verification evidence at V2 roles 10, 11, and 13, followed by
  an independent role-12 decision and only then a possible role-54 candidate.

## Current stop line

The role-5 verify-only and write-once lifecycle tooling is implemented and
non-scientifically tested, but no repository tool may author its candidate.
Role-5 canonical creation/publication remains forbidden pending a fresh
independent review and fresh explicit user authorization of the exact
`(reviewed_commit, candidate_sha256, fixed canonical path, publication
authority)` tuple.  Machine capture, every later canonical V2 publication,
role-54 construction/publication, result initialization, roles 15/17
execution, held-out or all-slab computation, checker/postcheck publication,
release publication, and scientific dispatch remain forbidden until their
separate review and authorization edges.
