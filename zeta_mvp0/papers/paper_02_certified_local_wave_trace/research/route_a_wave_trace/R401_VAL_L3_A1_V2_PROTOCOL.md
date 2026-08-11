# R401-VAL-L3-A1 V2 scientific protocol and control overlay

Scientific protocol identifier: `R401-VAL-L3-A1`

Control generation name: `A416_L3_A1_CONTROL_V2`

Prepared: 2026-08-11 UTC

Status: **SCIENTIFIC SEMANTICS UNCHANGED / CONTROL CANDIDATE NON_LICENSING**

## 1. Identity and non-change rule

The scientific protocol remains `R401-VAL-L3-A1`.  V2 repairs its control
plane; it does not create `R401-VAL-L3-A1-V2` and does not add a serialized
generation field.  The fixed V2 paths and ordered maps in sections 5 and 6
are the only control-generation discriminator.

The immutable attempt-1 protocol document at
`research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md` has SHA-256
`518a76aa31e96c79eb2d5b81b00d690975f77dc12741a853de596d530de08618`.
That digest is an audit anchor, not a hidden runtime input.  This V2 document
restates the authority-bearing scientific invariants below.  Where a
scientific clause is not concerned with control paths, its meaning is
unchanged from that audit anchor.  If a proposed implementation changes a
matrix cell, evaluator, arithmetic model, threshold, accepted upstream
chain, or claim boundary, it is not this V2 control repair and requires a new
scientific protocol review.

The current document authorizes neither initialization nor evaluator
execution.  V2 roles 5 and 10--13, role 54, the result root, and the release
are separate future write-once edges.

## 2. Exact scientific matrix and inherited inputs

The slab order is exactly `S000, S001, ..., S050`.  The production order is
all 51 slabs at 128 bits followed by all 51 slabs at 256 bits.  There are
exactly 102 composite cells and 204 component evaluations.  The canonical
matrix is the ordered array of exact objects
`{precision_bits,slab_id}`; no subset, third precision, duplicate,
reordering, replacement box, or command-line matrix override is allowed.

The exact epsilon intervals and accepted primary boxes are taken from role
34, `R401_VAL_L1_FINAL_PLAN_V2.json`, and must replay through roles 35--39.
The A4.15 chain is roles 40--44.  The sealed S0 static, branch, and composite
chains are roles 45--53.  The V2 S0 compatibility object is role 13.  All
these paths and hashes are direct members of the ordered main-freeze input
array; no unbound helper may replace one.

The scientific code is deliberately reused unchanged:

- role 15:
  `scripts/evaluate_r401_val_l3_a1_static_cell.py`;
- roles 16 and 17:
  `validated/capd_r401_phase_branch_tube_mp_a1.cpp` and its persistent
  binary;
- role 18: `scripts/r401_val_l3_a1_branch_runtime.py`; and
- role 25: the unchanged static-evaluator test.

V2 checkers must bind and replay those exact roles.  Copying an evaluator to
a V2 name or silently rebuilding role 17 changes the protocol boundary and
is rejected.

## 3. Scientific predicates retained unchanged

With `a=51/50` and `c=2*(sqrt(1+a)-1)`, the algebraic orthogonal normal
basis and the two frequencies are reconstructed exactly as in the accepted
implementation.  Rounded eigenvectors are display-only.  With `q=OQ` and
`p=OP`,

```text
W_epsilon(q) = (-c*q1-q2-a*epsilon*q1^2, q1)
R = |W_epsilon(q)|^2
K_epsilon = (P_minus^2+P_plus^2)/2
            + 2*pi^2*R*exprel(pi*epsilon^2*R).
```

The theorem domain retains the premise that a candidate orbit remains in
`r_minus < 0.06` over its full period.  The intended local conclusion
remains uniqueness modulo time translation of the already accepted fast
branch, with that distinguished branch proving `r_minus < 0.04` throughout
its period.  Nothing in this control repair supplies a global-candidate
premise or a global-orbit, trace-formula, Hilbert--Polya, zeta-zero, or RH
claim.

Each static cell retains the four canonical trees, in order:
`ANGLE`, `SECTION_LOW`, `SECTION_HIGH`, and `SECTION_WINDOW`.
It retains the exact domains and gates `r_minus <= 0.06`,
`|Q_minus| < 0.015`, `|P_minus| <= 0.06`, `|P_plus| < 1.415`,
`|Q_plus| < 0.18`, the strict angle conditions
`D_plus > 0`, `N_plus > 0`, `theta_dot < 18`, and
`18*0.69 < 4*pi`.  The landing window remains
`0.12 < Q_plus < 0.17`, `|Q_minus| < 0.02`,
`|P_minus| < 0.08`.  Terminal classifications and their proof semantics
are unchanged.

Each branch cell embeds the accepted L1 primary box at `P_plus=0`, treats
epsilon and period as interval constants, and integrates normalized time on
the exact 64 closed phase cells `[k/64,(k+1)/64]`.  The CAPD method remains
`SolutionCurve`, Taylor order 24, with precision-dependent absolute and
relative tolerances `1e-30` at 128 bits and `1e-60` at 256 bits.  All
transcript, tube, return, phase-cover, resource, and cross-precision gates
remain unchanged.

A scientific component, milestone, or theorem status can arise only from
the complete frozen 102-cell archive after both independent component
checkers and the composite checker pass and their three postchecks reopen
the published checker objects.  Producer summaries, mock statuses, role-5
acceptance, role-12 acceptance, or role-54 publication alone cannot assign a
scientific status.

## 4. Immutable legacy and V2 isolation

The old role-10/11/12/13 objects and all old role-19--24 and role-26--33
sources remain immutable attempt-1 evidence.  They are not aliases or
fallbacks for V2.  Role 5 must record
`WITHDRAWN_NON_LICENSING` for attempt 1 and bind the exact old publication
hashes and commits specified by the V2 pre-freeze design.  Its acceptance is
limited to the V2 control implementation.

Every V2 main freeze, run configuration, per-cell record, aggregate,
checker, postcheck, report, and release uses scientific
`protocol_id = R401-VAL-L3-A1`.  The fixed V2 main-freeze path and result
root prevent collision.  Validators reject either a V2 path in an old map or
an old path in the V2 map before comparing hashes.

## 5. Exact ordered 53-role input map

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

The JSON representation is exactly 53 ordered objects with keys
`{role,path,sha256}`.  The row numbers above are documentation order only.
A role or path may occur exactly once.

## 6. Exact roles 54--68 and result namespace

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
sibling is `results/r401_val_l3_a1_v2_all_slabs.operational`.  Release
provenance is written at
`results/r401_val_l3_a1_v2_all_slabs/RELEASE_PROVENANCE.json` only after
all 68 roles pass.  It is not in its own map.

## 7. Freeze and dispatch boundary

Role 54 is generated only after the 53 byte images are final and the V2
review file is exactly `Verdict: ACCEPT_FOR_FREEZE\n`.  Its construction
does not initialize the result root or run either evaluator.  Role 54 may be
published only after the three role-20--22 validators and role 24
independently accept the same candidate bytes and after separate publication
authorization.

Initialization, scientific dispatch, checker publication, postcheck
publication, and release publication remain distinct authorization edges.
The present document supplies none of them.  Before those edges, all
component, milestone, theorem, and final statuses remain null and every
engineering artifact remains non-licensing.

The role-5 verify-only and write-once lifecycle tooling is implemented and
non-scientifically tested, but no repository tool may author the candidate.
No role-5 candidate or canonical role-5 object is accepted by this protocol
boundary.  Canonical publication remains forbidden pending a fresh
independent review and fresh explicit user authorization of the exact
`(reviewed_commit, candidate_sha256, fixed canonical path, publication
authority)` tuple; even a successful role-24 receipt grants no downstream
authority.
