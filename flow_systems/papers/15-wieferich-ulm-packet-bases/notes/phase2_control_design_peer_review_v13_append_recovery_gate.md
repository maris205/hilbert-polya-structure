# Replacement Paper 15 v13 peer-review append-order recovery gate

Status: **PASS TO ONE BYTE-PRESERVING APPEND-ORDER RECOVERY TRANSACTION ONLY**
Date: 2026-08-17 (Asia/Shanghai)
Gate class: exact-byte review-record ordering recovery
Sole repository write in this gate-authoring step:
notes/phase2_control_design_peer_review_v13_append_recovery_gate.md
Review, design-amendment, source, implementation, execution, generated-artifact,
proof, Route, manuscript, release, archive, and Git authority: **none**

## Material Passport

- Material type: one bounded governance gate for a misplaced already-authored
  peer-review block.
- Error being governed: the sole v13 review append used apply_patch context at
  the historical line-5080 boundary, so the complete v13 block was inserted
  before the already-existing v11 review block instead of at EOF.
- Current review receipt: regular file, mode 0644, nlink 1, 5,962 lines,
  321,362 bytes, SHA-256
  22fa89d53a9a6a4dae707b360a6bc12b6cc330d7be3add6055a2958ed7193a75.
- Exact movable block: current lines 5,081--5,515 inclusive, 435 lines,
  24,711 bytes, SHA-256
  fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1.
- Determination: **PASS TO ONE BYTE-PRESERVING APPEND-ORDER RECOVERY
  TRANSACTION ONLY.**
- Permitted transformation: delete that exact block from its current
  misplaced interval and append the same exact bytes once at EOF.
- Semantic posture: the transformation is a positional correction only.
  It neither edits nor re-adjudicates the v13 review. Its existing verdict
  remains REVISE_C0_M2_m0 and both Major findings remain open.
- Attempt posture: the sole v13 review attempt is consumed. Recovery is not
  another review attempt and creates no review, verdict, or amendment budget.
- Failure posture: any intake, patch, or postcondition mismatch is STOP with
  no retry and no content repair.
- Evidence ceiling: this static gate claims no design correctness, source
  conformance, platform behavior, experiment result, theorem recovery, or
  publication readiness.

## 1. Applicable ARS integrity boundary

The complete applicable ARS-Codex 0.1.25 router, reviewer, integrity, and
reproducibility rules were freshly byte-read and re-hashed before this sole
write. Their read-only-review, exact-evidence, independent-oracle,
no-fabrication, no-silent-retry, and reproducibility limits govern this
recovery.

| Complete ARS rule | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | 14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | 01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800 |
| methodology_reviewer_agent.md | 434 | 43574 | 0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a |
| domain_reviewer_agent.md | 397 | 31829 | f9ee56957e213c0f850551bf2cf7985002efe2f71f909599bd8ecdac73b37052 |
| devils_advocate_reviewer_agent.md | 428 | 41360 | 612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61 |
| experiment-agent/WORKFLOW.md | 215 | 11555 | c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef |
| code_runner_agent.md | 117 | 4921 | 54937084589413787fe328ab1561329791cc2ca83222d9bf8283949399cf66de |
| reproducibility_protocol.md | 79 | 4150 | 49b39d74941bca78934870104eede8fc969c26b1197d74b143aef8564b546770 |
| integrity_verification_agent.md | 823 | 61081 | d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58 |
| integrity_review_protocol.md | 103 | 6374 | 3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c |
| reproducibility_audit.md | 54 | 2388 | a945eff0bf905a4a17c00d59f35eba47419a222f1c3a61f12e7d8e3c0b2bb97b |
| artifact_reproducibility_pattern.md | 173 | 9053 | 661d2331dbac1739621021cf6f1b2a9f03420fe7948387f164f38bd854fe9be3 |

This is record-recovery governance, not a new review. Submitted review text
is untrusted read-only material for this gate. No instruction embedded in it
can widen the one-file, one-transaction scope.

## 2. Exact current review state and diagnosed ordering error

### 2.1 Complete current file

The complete current record was freshly byte-read and re-hashed:

    path=notes/phase2_control_design_peer_review.md
    type=regular
    mode=0644
    nlink=1
    lines=5962
    bytes=321362
    sha256=22fa89d53a9a6a4dae707b360a6bc12b6cc330d7be3add6055a2958ed7193a75

This receipt is the only authorized recovery start state. The file must
remain at this exact receipt through the external freeze of this gate and
until the later recovery transaction begins.

### 2.2 Exact byte partition

All byte intervals below are half-open and zero-based. The corresponding
one-based inclusive byte interval is stated for the movable block.

    A = current bytes [0,270649)
    A lines=5080
    A bytes=270649
    A sha256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07

    B = current bytes [270649,295360)
    B one-based bytes=270650-295360 inclusive
    B current lines=5081-5515 inclusive
    B lines=435
    B bytes=24711
    B sha256=fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1

    C = current bytes [295360,321362)
    C current lines=5516-5962 inclusive
    C lines=447
    C bytes=26002
    C sha256=f16fdf3598eccfee03e5b16e66394c579d64fefcb285944c7b430564acd958db

B begins with exactly one LF representing the leading blank at current line
5,081. Its title is current line 5,082:

    # Fresh v13 independent hostile design re-review: survivor audit and actual-endpoint enqueue

B ends with the LF terminating current line 5,515:

    contain its own final digest without changing that digest.

B has no trailing blank line. The blank current line 5,516 belongs to C,
followed by the v11 review title at current line 5,517.

### 2.3 Exact reconstruction proof

Deleting B in memory and concatenating A || C reconstructs the exact review
that existed before the v13 append:

    reconstructed_pre_v13_review_lines=5527
    reconstructed_pre_v13_review_bytes=296651
    reconstructed_pre_v13_review_sha256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c

Appending the same unmodified B bytes to A || C yields the only authorized
final file:

    final_bytes=(A || C) || B
    final_lines=5962
    final_bytes_count=321362
    final_sha256=3a17a681b880d4f99bc41aabe2dcde3a29ec6117dc896de14991a73547fdb40f

The unchanged final head and tail receipts are:

    final_head_interval=[0,296651)
    final_head_lines=5527
    final_head_bytes=296651
    final_head_sha256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c

    final_tail_interval=[296651,321362)
    final_tail_lines=435
    final_tail_bytes=24711
    final_tail_sha256=fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1

No decoding, newline conversion, rewrapping, normalization, copy edit,
heading edit, verdict edit, hash edit, or regenerated review prose is
permitted.

### 2.4 Nested historical prefixes

The current file and the authorized final file preserve all historical
prefixes byte-for-byte:

    PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
    PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
    PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

    PRESERVED_V9_INPUT_PREFIX_LINES=4236
    PRESERVED_V9_INPUT_PREFIX_BYTES=223999
    PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1

    PRESERVED_V10_INPUT_PREFIX_LINES=4634
    PRESERVED_V10_INPUT_PREFIX_BYTES=245023
    PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c

    PRESERVED_V11_INPUT_PREFIX_LINES=5080
    PRESERVED_V11_INPUT_PREFIX_BYTES=270649
    PRESERVED_V11_INPUT_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07

The recovery is invalid if any nested prefix differs, even if the full final
digest accidentally matches a separately constructed file.

## 3. Frozen design, governance, and quarantine authority

Every record below was freshly byte-read and re-hashed. These receipts bind
the recovery intake; they supply no new design or implementation verdict.

| Record | Lines | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| phase2_control_design_gate.md | 272 | 10820 | 0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3 | provenance |
| phase2_control_design_lock.md | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d | effective base |
| phase2_control_design_amendment_v1.md | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe | effective |
| phase2_control_design_amendment_v2.md | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea | effective |
| phase2_control_design_amendment_v3.md | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b | effective |
| phase2_control_design_amendment_v4.md | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 | effective |
| phase2_control_design_amendment_v5.md | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 | blocked/no-op provenance |
| phase2_control_design_amendment_v6.md | 1498 | 80822 | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 | effective |
| phase2_control_design_amendment_v7.md | 1199 | 60145 | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 | effective |
| phase2_control_design_amendment_v8.md | 884 | 45610 | e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 | effective |
| phase2_control_design_amendment_v9.md | 870 | 40366 | 0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829 | effective |
| phase2_control_design_amendment_v10.md | 1133 | 50487 | d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f | effective under REVISE |
| phase2_control_design_amendment_v11.md | 1072 | 49086 | 7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269 | effective under REVISE |
| phase2_control_design_amendment_v13.md | 1057 | 48820 | 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27 | reviewed successor |
| phase2_control_design_reopen_gate_v1.md | 434 | 21256 | 8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973 | provenance |
| phase2_control_design_remediation_gate_v9.md | 1060 | 48563 | c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90 | provenance |
| phase2_control_design_remediation_gate_v10.md | 1002 | 45658 | 48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5 | provenance |
| phase2_control_design_remediation_gate_v11.md | 1221 | 54839 | d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e | consumed |
| phase2_control_design_amendment_v11_path_recovery_gate.md | 528 | 21386 | 41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888 | consumed path-only |
| phase2_control_design_remediation_gate_v12.md | 789 | 37732 | ac5e997419f1123218c662ab579e42274ad8774faf3634db1d7b6c51e8ccc999 | BLOCKED |
| phase2_control_design_remediation_gate_v13.md | 1324 | 61873 | 5253cebde296df494aee9d63bdc275f7622e79182c61732715bbaf94bd8e2dca | consumed review authority |
| phase2_control_implementation_gate.md | 735 | 35164 | e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8 | historical nonauthorizing |
| phase2_control_implementation_remediation_gate_v1.md | 660 | 32800 | 52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f | historical nonauthorizing |

The path notes/phase2_control_design_amendment_v12.md is absent and must
remain absent. V12 authorized no amendment and no review. The v13 gate and
amendment are immutable inputs to this positional recovery.

The six provisional implementation paths remain quarantine only:

| Quarantined path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| code/generate_controls.py | 1086 | 56136 | d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc |
| code/test_controls.py | 1239 | 98421 | d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756 |
| code/README.md | 75 | 3722 | 6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb |
| experiments/reproduce.sh | 4452 | 316515 | 930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66 |
| experiments/README.md | 94 | 5419 | 266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959 |
| results/README.md | 55 | 2342 | b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028 |

    QUARANTINED_SOURCE_PATHS=6
    QUARANTINED_SOURCE_LINES=7001
    QUARANTINED_SOURCE_BYTES=482555
    SOURCE_USED_AS_RECOVERY_AUTHORITY=false
    SOURCE_ACCEPTED_AS_IMPLEMENTATION_EVIDENCE=false

No project code was imported, sourced, compiled, syntax-checked, parsed as
project code, or executed while authoring this gate. No platform probe,
preflight, generator, verifier, unittest, wrapper, reproduction, cache,
temporary, lock, result, receipt, manifest, or generated member was created
or run.

## 4. Exactly one authorized later recovery transaction

### 4.1 External gate receipt is mandatory first

This gate contains no prediction of its own digest. After gate authoring, an
external coordinator must compute and freeze:

    path=notes/phase2_control_design_peer_review_v13_append_recovery_gate.md
    type=regular
    mode=<actual>
    nlink=1
    lines=<actual>
    bytes=<actual>
    sha256=<actual 64-lowercase-hex digest>

At that freeze the coordinator must also re-hash the complete current review,
all Section-1 ARS rules, all Section-3 authority, and the six quarantined
paths; confirm the absent v12 amendment; and confirm that the review is still
the exact 22fa89d5... start state. Any drift stops. No recovery begins from
an unreceipted or mutable gate.

### 4.2 T0 mandatory preflight

One later recovery actor may perform read-only T0. T0 must:

1. fresh-read and re-hash this complete gate and every Section-1 and
   Section-3 input;
2. require the review to be regular mode 0644, nlink 1, exactly
   5,962/321,362/22fa89d53a9a6a4dae707b360a6bc12b6cc330d7be3add6055a2958ed7193a75;
3. require the exact A/B/C byte partition, line boundaries, component
   counts, and all three component hashes in Section 2.2;
4. reconstruct A || C and (A || C) || B in memory only and require every
   Section-2.3 receipt before writing;
5. require the four nested prefix receipts in Section 2.4;
6. require the exact v13 title once at current line 5,082 and require no
   second copy elsewhere;
7. require the sole active v13 count-twelve block inside B exactly as
   Section 5 specifies;
8. require amendment v12 absent and every frozen authority unchanged; and
9. confirm that no other path is about to be written.

If any item differs, the actor stops before write. T0 grants no opportunity
to search for a similar block, infer replacement coordinates, normalize
bytes, or choose a nearby context.

### 4.3 Sole write transaction

After T0 passes, exactly one apply_patch transaction may modify only:

    notes/phase2_control_design_peer_review.md

That single transaction contains exactly two coupled hunks:

1. Delete B at its exact current position, including its one leading blank
   byte and its final line terminator, and excluding C's leading blank.
2. Add the same exact B bytes once after the current EOF of C, preserving
   every byte and the one leading blank.

The Delete and Add represent one move. The actor may not use two separate
patch invocations, an intermediate file, a temporary copy, a script rewrite,
an editor normalization, or a regenerated review block. It may not alter A,
C, or any byte of B.

The sole apply_patch invocation consumes the recovery attempt. If the patch
rejects, applies unexpectedly, or cannot express the exact move, STOP. There
is no retry, fallback, second patch, manual repair, alternate context, or
content edit.

## 5. Mandatory post-transaction proof

### 5.1 Exact final receipt

Immediately after the sole patch, the actor must fully re-read and double-
hash the review. The only passing receipt is:

    path=notes/phase2_control_design_peer_review.md
    type=regular
    mode=0644
    nlink=1
    lines=5962
    bytes=321362
    sha256=3a17a681b880d4f99bc41aabe2dcde3a29ec6117dc896de14991a73547fdb40f

The first 296,651 bytes must be exactly 5,527 lines with SHA-256
0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c.
The final 24,711 bytes must be exactly 435 lines with SHA-256
fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1.
All four nested prefixes must still match Section 2.4.

The actor must compute the full, head, tail, and nested-prefix receipts
twice from fresh reads. One matching pass followed by a different pass is
failure.

### 5.2 Exact order and uniqueness

The final record must satisfy all of these:

- lines 1--5,527 are the exact pre-v13 review;
- no v13 review title occurs in the first 296,651 bytes;
- final line 5,528 is B's one leading blank;
- the exact v13 title occurs once in the complete file, at line 5,529;
- the exact heading
  ## L6. Exact active count-twelve successor authentication
  occurs once, at line 5,828;
- the exact active marker
  [P15R-EFFECTIVE-DESIGN-AMENDMENTS v11]
  occurs once, at line 5,835;
- its matching close occurs at line 5,861;
- the exact heading
  ## L7. Verdict and authorization consequence
  occurs at line 5,867;
- B occupies the complete EOF interval [296651,321362);
- B occurs once, as proven by its unique title and exact EOF-tail hash; and
- final line 5,962 is exactly:
  contain its own final digest without changing that digest.

The active v13 amendment block must retain exactly:

- one count=12 line;
- twelve dense path rows numbered 1 through 12;
- twelve corresponding SHA-256 rows numbered 1 through 12;
- paths v1 through v11 followed by v13;
- no amendment-v12 path;
- the frozen v13 digest
  4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27;
  and
- no blank or commentary line inside the marker pair.

These are structural checks on the unchanged B bytes, not permission to
edit the block into conformance.

### 5.3 Failure and stop

If any postcondition fails, the actor stops immediately and reports the
actual receipt. It must not attempt to fix, undo, reapply, append again,
delete again, or manufacture a passing hash. A mismatching post-state is
not authority for another write.

If every postcondition passes, the external recovery receipt authenticates
only the corrected append order. It does not convert REVISE to PASS, close
a finding, authorize a v14 amendment, revive implementation authority, or
admit any source or execution step.

## 6. Verdict and finding preservation

The moved v13 review block is immutable adjudicative content. Its exact
verdict and findings remain:

    REVIEW_ID=P15R-P2-CONTROL-DESIGN-PEER-REVIEW-v13.0
    OVERALL_CLOSURE_VERDICT=REVISE_C0_M2_m0
    CRITICAL_FINDINGS=0
    MAJOR_FINDINGS=2
    MINOR_FINDINGS=0
    P15R_V13_M1_STATUS=OPEN_REQUIRES_REMEDIATION_AUTHORITY
    P15R_V13_M2_STATUS=OPEN_REQUIRES_REMEDIATION_AUTHORITY
    P15R_V11_M1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
    ALL_INHERITED_FINDINGS_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET

Recovery changes only physical block order so the consumed v13 append is at
the EOF boundary it claimed. It does not reassess the Linux source evidence,
the VA/RA survivor-audit finding, the actual-endpoint enqueue finding, the
33-vector algebra, or any no-additional-finding statement.

The active successor remains base plus amendments v1--v11 and v13, with v5
blocked/no-op and v12 skipped. Its count is twelve. The design remains
REVISE, and the six provisional implementation paths remain quarantined.

## 7. Authorization matrix and final stop

    GATE_KIND=PEER_REVIEW_APPEND_ORDER_RECOVERY_ONLY
    GATE_VERDICT=PASS_TO_ONE_BYTE_PRESERVING_APPEND_ORDER_RECOVERY_TRANSACTION_ONLY

    CURRENT_REVIEW_TYPE=regular
    CURRENT_REVIEW_MODE=0644
    CURRENT_REVIEW_NLINK=1
    CURRENT_REVIEW_LINES=5962
    CURRENT_REVIEW_BYTES=321362
    CURRENT_REVIEW_SHA256=22fa89d53a9a6a4dae707b360a6bc12b6cc330d7be3add6055a2958ed7193a75

    MOVABLE_BLOCK_CURRENT_LINES=5081-5515
    MOVABLE_BLOCK_ZERO_BASED_BYTES=[270649,295360)
    MOVABLE_BLOCK_ONE_BASED_BYTES=270650-295360
    MOVABLE_BLOCK_LINES=435
    MOVABLE_BLOCK_BYTES=24711
    MOVABLE_BLOCK_SHA256=fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1
    MOVABLE_BLOCK_LEADING_BLANK_INCLUDED=true
    MOVABLE_BLOCK_TRAILING_BLANK_INCLUDED=false

    DELETE_RECONSTRUCTION_LINES=5527
    DELETE_RECONSTRUCTION_BYTES=296651
    DELETE_RECONSTRUCTION_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c

    AUTHORIZED_FINAL_LINES=5962
    AUTHORIZED_FINAL_BYTES=321362
    AUTHORIZED_FINAL_SHA256=3a17a681b880d4f99bc41aabe2dcde3a29ec6117dc896de14991a73547fdb40f
    AUTHORIZED_FINAL_HEAD_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c
    AUTHORIZED_FINAL_TAIL_SHA256=fd8580e789244c14c732235084a06aa8ed20c2014b655c854bd7fd96233128c1

    RECOVERY_TARGET=notes/phase2_control_design_peer_review.md
    RECOVERY_TRANSACTIONS_AUTHORIZED=1
    RECOVERY_APPLY_PATCH_INVOCATIONS_AUTHORIZED=1
    RECOVERY_COUPLED_HUNKS_REQUIRED=2
    RECOVERY_DELETE_EXACT_BLOCK_AUTHORIZED=true
    RECOVERY_ADD_SAME_EXACT_BLOCK_AT_EOF_AUTHORIZED=true
    RECOVERY_OTHER_PATH_WRITE_AUTHORIZED=false
    RECOVERY_RETRY_AUTHORIZED=false
    RECOVERY_FALLBACK_AUTHORIZED=false
    RECOVERY_UNDO_AUTHORIZED=false
    RECOVERY_CONTENT_EDIT_AUTHORIZED=false
    RECOVERY_SEMANTIC_CHANGE_AUTHORIZED=false

    V13_REVIEW_ATTEMPT_CONSUMED=true
    NEW_REVIEW_ATTEMPTS_AUTHORIZED=0
    REVIEW_VERDICT_CHANGE_AUTHORIZED=false
    FINDING_RECLASSIFICATION_AUTHORIZED=false
    FINDING_CLOSURE_AUTHORIZED=false
    NEW_REVIEW_TEXT_AUTHORIZED=false
    NEW_ACTIVE_AMENDMENT_BLOCK_AUTHORIZED=false

    AMENDMENT_V12_PATH_ABSENT=true
    AMENDMENT_WRITE_AUTHORIZED=false
    DESIGN_REMEDIATION_AUTHORIZED=false
    CONTROL_SOURCE_EDIT_AUTHORIZED=false
    CONTROL_IMPLEMENTATION_AUTHORIZED=false
    INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
    PROJECT_CODE_IMPORT_AUTHORIZED=false
    PROJECT_CODE_EXECUTION_AUTHORIZED=false
    SHELL_SOURCE_AUTHORIZED=false
    PROJECT_AST_OR_SHELL_SYNTAX_CHECK_AUTHORIZED=false
    PLATFORM_PREFLIGHT_AUTHORIZED=false
    PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
    GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
    RESULT_REGENERATION_AUTHORIZED=false
    GENERATOR_EXECUTION_AUTHORIZED=false
    VERIFY_ONLY_EXECUTION_AUTHORIZED=false
    UNITTEST_EXECUTION_AUTHORIZED=false
    TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
    REPRODUCTION_RUN_AUTHORIZED=false

    PROOF_MODIFICATION_AUTHORIZED=false
    ROUTE_A_AUTHORIZED=false
    ROUTE_B_AUTHORIZED=false
    COMPOSITION_AUTHORIZED=false
    MANUSCRIPT_AUTHORIZED=false
    FIGURE_WORK_AUTHORIZED=false
    RELEASE_AUTHORIZED=false
    ARCHIVE_AUTHORIZED=false
    GIT_OPERATION_AUTHORIZED=false
    GIT_PUBLIC_SYNC_AUTHORIZED=false
    UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED

Final determination: **PASS TO ONE BYTE-PRESERVING APPEND-ORDER RECOVERY
TRANSACTION ONLY.** The current 24,711-byte v13 review block is complete
and already adjudicative but physically misplaced. Exactly one later
apply_patch transaction may delete those exact bytes from current lines
5,081--5,515 and append the same bytes once at EOF. The sole valid result is
5,962 lines, 321,362 bytes, SHA-256
3a17a681b880d4f99bc41aabe2dcde3a29ec6117dc896de14991a73547fdb40f,
with the exact 0321b123... head and fd8580e7... tail. The recovery creates
no new review, does not change REVISE_C0_M2_m0, and authorizes no amendment,
source, implementation, run, proof, Route, manuscript, release, archive, or
Git action.
