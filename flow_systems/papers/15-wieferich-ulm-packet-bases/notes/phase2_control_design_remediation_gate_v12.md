# Replacement Paper 15 control-design remediation gate v12

Status: **BLOCKED — NO AMENDMENT v12, REVIEW, SOURCE, IMPLEMENTATION, OR EXECUTION AUTHORITY; CURRENT REVIEW REMAINS REVISE C0/M1/m0**  
Date: 2026-08-17 (Asia/Shanghai)  
Gate class: exact-byte design-remediation feasibility and crash-retention audit  
Sole repository write in this gate-authoring step: `notes/phase2_control_design_remediation_gate_v12.md`  
Current open findings: `P15R-REOPEN-M1`, `P15R-V9-M1`,
`P15R-V9-m1`, `P15R-V10-M1`, `P15R-V10-m1`, and
`P15R-V11-M1`  
Source, design-amendment, review-append, implementation, execution,
precheck, generated-artifact, Route, manuscript, release, archive, and Git
authority: **none**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**

## Material Passport

- **Material type:** one bounded design-remediation feasibility gate.
- **Question:** can `P15R-V11-M1` be repaired without a new wire form by
  extending `C11` with one binary bootstrap-success-seal commit bit `BS`,
  retaining an exact `AV=1,BS=0` preseal failure, and making one local G
  commit atomically publish the immutable success seal, `BS=1`, and G's
  success state?
- **Algebraic candidate:** the proposed local extension is finite and
  internally expressible: the 32 existing failures acquire `BS=0`; former
  row 33 splits into one `AV=1,BS=0` preseal failure and one `AV=1,BS=1`
  success, giving 33 failures plus one success.  A preallocated, fully
  validated G-local aggregate can also have one abstract linearization
  point with no syscall, allocation, or stable intermediate inside it.
- **Determination:** **BLOCKED.**  The algebra and local linearization do not
  supply crash-surviving evidence for the new failure row.  If G validates
  the ACK, retains `AV=1`, and crashes before the local success commit, the
  only evidence distinguishing that execution from a crash before ACK
  receipt/validation dies with G.  P's complete ACK send proves `AC=1`, not
  G's `AV=1`; P's pidfd/wait receipt proves G death, not G's last local
  validation state.  The frozen model has no shared durable receipt and no
  G-to-P bootstrap-seal form.  Silence, EOF, time, queue state, and inferred
  delivery are expressly inadmissible.
- **Integrity consequence:** classifying the crash as `AV=1,BS=0` would
  fabricate unavailable evidence; classifying it as `AV=0,BS=0` would erase
  a completed monotone predecessor in executions where validation did occur.
  Either choice violates the frozen exact-evidence and tombstone contracts.
- **Finding posture:** this gate closes, downgrades, or pre-judges no
  finding.  `P15R-V11-M1` remains OPEN and the complete current result stays
  `REVISE_C0_M1_m0`.  The five inherited findings remain open because their
  required zero-finding closure has not occurred.
- **Future-governance ceiling:** a separate future gate may evaluate and,
  if justified, authorize one exact G-to-P seal/validation receipt or
  another crash-surviving carrier.  This gate does not authorize that form,
  its fields, an amendment, a review, or any implementation action.
- **Evidence ceiling:** no claim of source conformance, runtime/platform
  availability, deterministic replay, theorem recovery, or publication
  readiness is made.

## 1. Exact authority, full intake, and unchanged byte state

### 1.1 Applicable complete ARS rules

Before this sole write, the applicable complete ARS-Codex 0.1.25 root,
academic-paper-review workflow, methodology reviewer, domain reviewer,
devil's-advocate reviewer, experiment workflow, code-runner agent,
reproducibility protocol, integrity-verification agent, integrity-review
protocol, reproducibility audit, and artifact-reproducibility pattern were
freshly byte-read and re-hashed.  Their independent-oracle,
hostile-counterexample, exact-evidence, no-fabrication, fail-closed,
read-only-review, experiment-integrity, and reproducibility limits govern
this gate.

| Complete ARS rule | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| methodology_reviewer_agent.md | 434 | 43574 | `0a056ab04963b4ccb1af050b3e40390da2f675a6fa723f0df44674551e83838a` |
| domain_reviewer_agent.md | 397 | 31829 | `f9ee56957e213c0f850551bf2cf7985002efe2f71f909599bd8ecdac73b37052` |
| devils_advocate_reviewer_agent.md | 428 | 41360 | `612ea6371ba3107524c72a21cfb1966e196eb0512c9072b18af83caa6005be61` |
| experiment-agent/WORKFLOW.md | 215 | 11555 | `c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef` |
| code_runner_agent.md | 117 | 4921 | `54937084589413787fe328ab1561329791cc2ca83222d9bf8283949399cf66de` |
| reproducibility_protocol.md | 79 | 4150 | `49b39d74941bca78934870104eede8fc969c26b1197d74b143aef8564b546770` |
| integrity_verification_agent.md | 823 | 61081 | `d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58` |
| integrity_review_protocol.md | 103 | 6374 | `3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c` |
| reproducibility_audit.md | 54 | 2388 | `a945eff0bf905a4a17c00d59f35eba47419a222f1c3a61f12e7d8e3c0b2bb97b` |
| artifact_reproducibility_pattern.md | 173 | 9053 | `661d2331dbac1739621021cf6f1b2a9f03420fe7948387f164f38bd854fe9be3` |

This was a static design/governance intake.  No project path was imported,
sourced, compiled, parsed as project code, syntax-checked, or executed.  No
platform probe, preflight, generator, verifier, unittest, wrapper,
reproduction, cache, temporary, lock, result, manifest, or generated member
was created or run.

### 1.2 Complete current review and every preserved prefix

The complete current append-only review was freshly byte-read and re-hashed:

| Record | Lines | Bytes | SHA-256 | Current result |
|---|---:|---:|---|---|
| `notes/phase2_control_design_peer_review.md` | 5527 | 296651 | `0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c` | `REVISE_C0_M1_m0` |

Its exact current and nested historical append boundaries were independently
recomputed from the same bytes:

```text
CURRENT_REVIEW_LINES=5527
CURRENT_REVIEW_BYTES=296651
CURRENT_REVIEW_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c

PRESERVED_V11_INPUT_PREFIX_LINES=5080
PRESERVED_V11_INPUT_PREFIX_BYTES=270649
PRESERVED_V11_INPUT_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07

PRESERVED_V10_INPUT_PREFIX_LINES=4634
PRESERVED_V10_INPUT_PREFIX_BYTES=245023
PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c

PRESERVED_V9_INPUT_PREFIX_LINES=4236
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1

PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
```

The 296,651-byte result is the sole current adjudicative record.  Every
older PASS or REVISE block remains evidence in original order; no prefix is
rewritten, normalized, truncated, or reclassified.

### 1.3 Exact design and governance chain

Every design/governance input below was completely byte-read and re-hashed:

| Record | Lines | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | provenance |
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | effective base |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | effective |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | effective |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | effective |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | effective |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | provenance only; zero semantic delta |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | effective |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | effective |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` | effective |
| amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` | effective |
| amendment v10 | 1133 | 50487 | `d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f` | effective under REVISE |
| amendment v11, recovered correct target | 1072 | 49086 | `7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269` | effective under REVISE |
| design-reopen gate v1 | 434 | 21256 | `8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973` | reopen provenance |
| remediation gate v9 | 1060 | 48563 | `c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90` | v9 authority provenance |
| remediation gate v10 | 1002 | 45658 | `48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5` | v10 authority provenance |
| remediation gate v11 | 1221 | 54839 | `d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e` | consumed v11 authority |
| amendment-v11 path-recovery gate | 528 | 21386 | `41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888` | consumed path-only authority |

The effective tuple remains base plus v1 through v11, with v5 retained only
as blocked/no-op provenance.  Its effective amendment count remains eleven.
This blocking gate adds no amendment and no semantic design clause.

The recovered v11 target is a regular mode-0644, nlink-one file at the
correct paper-package path.  The former workspace-root stray
`/root/rh_dyna/flow_systems/notes/phase2_control_design_amendment_v11.md`
was absent under ordinary-existence and lstat-path reasoning.  Workspace
inventory contained no second v11 amendment-named path.

### 1.4 Historical implementation gates and unchanged six-path quarantine

The historical implementation gates were freshly byte-read and re-hashed:

| Historical nonauthorizing record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_implementation_gate.md` | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` |
| `notes/phase2_control_implementation_remediation_gate_v1.md` | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` |

Both are consumed provenance and remain nonauthorizing.  Neither this gate
nor any future design action silently revives them.

The six provisional implementation paths were completely byte-read and
re-hashed only to freeze their quarantine boundary:

| Quarantined path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `code/generate_controls.py` | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

```text
QUARANTINED_SOURCE_PATHS=6
QUARANTINED_SOURCE_LINES=7001
QUARANTINED_SOURCE_BYTES=482555
SOURCE_USED_AS_DESIGN_AUTHORITY=false
SOURCE_ACCEPTED_AS_IMPLEMENTATION_EVIDENCE=false
```

No source name, behavior, count, or apparent implementation convention
supplies design meaning.

### 1.5 Start state and sole write

At gate-authoring start,
`notes/phase2_control_design_remediation_gate_v12.md` was absent under both
ordinary-existence and lstat-path checks.  The workspace-root v11 stray was
also absent.  This gate target is the sole write.  No amendment, review,
source, implementation, precheck, cache, temporary, lock, receipt, result,
manifest, generated, Route, manuscript, release, archive, or Git path was
created or changed.

## 2. Current finding and exact remediation question

### 2.1 `P15R-V11-M1` remains OPEN

The current review identifies one Major, high-confidence defect.  V11 makes
`GUARDIAN_READY_ACK_VALIDATED` and
`BOOTSTRAP_BOUNDARY_SUCCESS_SEALED` successive G-local states.  `AV` records
ACK validated acceptance, but no indivisible transition binds `AV:0->1` to
the immutable success seal.  A G crash after validation and before sealing
therefore has former row-33 coordinates without success.  That contradicts
v11's exact 32-failure/one-success totality.

The exact current adjudication remains:

```text
CURRENT_REVIEW_VERDICT=REVISE_C0_M1_m0
P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V9_m1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V10_M1_STATUS=OPEN_REMEDIATION_INCOMPLETE
P15R_V10_m1_STATUS=OPEN_ZERO_FINDING_CLOSURE_NOT_MET
P15R_V11_M1_STATUS=OPEN
```

This gate is not an independent review and has no finding-closure authority.

### 2.2 Candidate repair budget subjected to hostile audit

The proposed minimal repair admitted for feasibility analysis, but not for
authoring, was exactly:

1. add no wire form, channel, descriptor, ancillary item, syscall
   dependency, repository artifact, schema field, generated member,
   authority binding, DAG node, or edge;
2. extend `C11` with one binary G-local bit `BS`;
3. require `BS<=AV` and require `BS=1` to imply every unique-success
   predecessor, `X_P=X_G=0`, both old-boundary freeze receipts, exact ACK
   validation, one immutable G success seal, and G's success state;
4. append `BS=0` to the 32 existing failure vectors;
5. split former row 33 into an `AV=1,BS=0` preseal failure and an
   `AV=1,BS=1` unique success, for 33 failures plus one success;
6. prepare, validate, and stage every seal byte before one G-local commit;
7. make that commit one indivisible linearization point that publishes the
   immutable seal receipt, `BS=1`, and G success state together, with no
   syscall, allocation, hash, parse, copy, governed write, or observable
   stable intermediate inside the commit; and
8. retain `AV=1` in a precommit crash/timeout tombstone rather than rolling
   it back.

The proposed local atomic transition is expressible inside an abstract
state machine.  The blocker arises from evidence retention after G death,
not from an inability to write the transition relation.

## 3. Rejected candidate algebra, frozen only as the attacked object

Nothing in this section is an effective amendment.  It freezes the exact
candidate that was attacked so a future gate cannot misdescribe this
BLOCKED decision as approval.

### 3.1 Exact rejected tuple and invariants

```text
C12 = (SA,SC,VA,X_P,X_G,RA,RC,RV,AA,AC,AV,BS)

SA = release send-attempt count
SC = release complete-send count
VA = release validated-accept count at G
X_P = P owner-local out-of-slot old-form bit
X_G = G owner-local out-of-slot old-form bit
RA = READY send-attempt count
RC = READY complete-send count
RV = READY validated-receive count at P
AA = ACK send-attempt count
AC = ACK complete-send count
AV = ACK validated-accept count at G
BS = G bootstrap-success-seal commit bit

X = X_P | X_G
C11 = (SA,SC,VA,X_P,X_G,RA,RC,RV,AA,AC,AV)
C10 = (SA,SC,VA,X,RA,RC,RV)
```

Every coordinate is binary.  The rejected candidate would retain every v11
constraint and add:

```text
SC <= SA
VA <= SC
RA <= VA
RC <= RA
RV <= RC
AA <= RV
AC <= AA
AV <= AC
BS <= AV

if VA == 0 then (RA,RC,RV,AA,AC,AV,BS) == (0,0,0,0,0,0,0)
if RV == 0 then (AA,AC,AV,BS) == (0,0,0,0)
if AA == 1 then X_P == 0 and P_OLD_BOUNDARY_LEDGER_FROZEN == true
if AV == 1 then X_P == 0 and X_G == 0
if AV == 1 then G_OLD_BOUNDARY_EMISSION_FROZEN == true
if BS == 1 then AV == 1
if BS == 1 then (SA,SC,VA,RA,RC,RV,AA,AC,AV) == (1,1,1,1,1,1,1,1,1)
if BS == 1 then X_P == 0 and X_G == 0
if BS == 1 then both exact freeze receipts are retained
if BS == 1 then immutable G success-seal receipt is published
if BS == 1 then G state == BOOTSTRAP_BOUNDARY_SUCCESS_SEALED
if X == 1 then bootstrap_outcome == FAILURE

bootstrap_outcome == SUCCESS iff
  C12 == (1,1,1,0,0,1,1,1,1,1,1,1)
  and the one atomic G success aggregate is published
```

`BS` would be derived only from the published aggregate, never set or
cleared independently.  A failure tombstone would have to retain the entire
monotone C12 tuple and could never rewrite `AV=1` to zero.

### 3.2 Exact rejected 34-row terminal table

The proposed table below is internally finite.  Rows 1--32 are v11's exact
failures with `BS=0`; row 33 is the new preseal terminal failure; row 34 is
the sole success.

| # | SA | SC | VA | X_P | X_G | RA | RC | RV | AA | AC | AV | BS | Exact lifecycle class | Outcome |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 6 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 8 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 9 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 10 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 11 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 12 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 13 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 14 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 15 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 16 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 17 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 18 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 19 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 20 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 21 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 22 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 23 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 25 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | `POST_READY_PRE_ACK_FAILURE` | FAILURE |
| 26 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| 27 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| 28 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| 29 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | `ACK_PARTIAL_SEND_FAILURE` | FAILURE |
| 30 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | `ACK_PARTIAL_SEND_FAILURE` | FAILURE |
| 31 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | `ACK_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 32 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | `ACK_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 33 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | `ACK_VALIDATED_PRE_SEAL_COMMIT_FAILURE` | FAILURE |
| 34 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | `BOOTSTRAP_BOUNDARY_SUCCESS` | SUCCESS |

```text
REJECTED_CANDIDATE_VECTOR_COUNT=34
REJECTED_CANDIDATE_FAILURE_VECTOR_COUNT=33
REJECTED_CANDIDATE_SUCCESS_VECTOR_COUNT=1
REJECTED_CANDIDATE_EFFECTIVE=false
```

Row 33 would be a live G-local preseal state until a terminal cause seals it.
A proven G crash would set `G_CRASH`; an inherited deadline reached while
the commit remained absent would set `TIMEOUT` and the independent
`MISSING` bit, with `TIMEOUT` winning under the existing priority; a
deterministic terminal checkpoint with none of the first sixteen predicates
would use `MISSING`.  No new raw label is needed.  The defect is that the
survivor cannot prove row 33 rather than row 31/32 after G dies.

### 3.3 Rejected local preparation and commit construction

The attacked construction separated four concepts:

1. **Preparation:** before `AV=1`, G preallocates private staging storage and
   retains every exact frame, digest, identity, freeze, and ledger input.
2. **Validation/staging:** G completely validates the sole ACK, recomputes
   its exact joins, fills all success-seal bytes in private staging, and only
   then enters a local `AV=1,BS=0` preseal state.  Failure before that state
   remains an existing `AV=0` row.
3. **Commit:** one abstract local linearization publishes a single immutable
   aggregate containing the seal receipt, `BS=1`, and
   `BOOTSTRAP_BOUNDARY_SUCCESS_SEALED`.  The commit contains no syscall,
   allocation, hash, parse, copy, lock operation, governed write, or
   separately observable stable state.
4. **Postcommit:** any crash, timeout, peer fact, cleanup fact, or downstream
   failure ordered after the linearization point cannot flow backward
   through the sealed success boundary.

This construction closes the *local torn-state* counterexample: an
execution cannot expose only one of the aggregate's seal, `BS`, and success
state.  It does not close the *crash-surviving evidence* counterexample in
Section 4.

## 4. Fatal crash-retention counterexample to the no-new-wire candidate

### 4.1 Frozen retention ownership

The existing retained-evidence ownership is asymmetric and exact:

- P retains the bootstrap/global session, authenticated G PID/pidfd/proc and
  guardian identity, P-side preflight/attestation inputs, exact release and
  ACK send results, exact READY receive/validation facts, and later
  pidfd/wait/EOF containment evidence.
- G retains the exact release and ACK receive/validation facts, its local
  READY send result, its local ledgers, and its G-local state/tombstone.
- The exact global bootstrap wire forms through v11 are P-to-G
  `LAUNCHER_REAPED`, P-to-G `PRIVILEGE_DROP_RELEASE`, G-to-P
  `GUARDIAN_READY`, and P-to-G `GUARDIAN_READY_ACK`.
- There is no G-to-P record after G validates the ACK and before G's local
  success seal.  There is no frozen shared-memory, durable log, repository
  write, or other crash-surviving carrier for `AV` or `BS`.
- The inherited crash rule states that a dead process receives no
  fabricated local transition; the survivor records the exact last complete
  transcript/control fact and reachable containment receipts, while missing
  peer-local state remains missing.

The v11 generic sentence that a failure tombstone copies C11 does not create
a cross-owner storage mechanism.  A G-local tombstone in dead G memory is
not evidence available to P or to a later independent audit.

### 4.2 Fixed-observation pair

Let both executions share every retained predecessor through P's sole exact
complete ACK send:

```text
C common prefix at P:
  release and READY completed and validated
  P old-form ledgers frozen with X_P=0
  exact ACK constructed, attempted, and completely sent
  SA=SC=VA=RA=RC=RV=AA=AC=1
  P retains the same session, identities, frames, digests, and send receipt
```

Now compare:

```text
E0 — prevalidation crash
  G crashes after the ACK is completely sent by P but before G completes
  receive/validation
  true G-local suffix: AV=0, BS=0
  candidate row: 31 or 32 according to X_G

E1 — postvalidation/precommit crash
  G completely receives and validates the same ACK
  G completes private staging and enters AV=1, BS=0
  G crashes before the local aggregate commit
  true G-local suffix: AV=1, BS=0
  candidate row: 33
```

After G death, P's admissible surviving evidence is identical in E0 and E1:

```text
same exact complete ACK send receipt (AC=1)
same last P-visible bootstrap transcript
same authenticated G identity
same G pidfd/wait death receipt
same control EOF/peer-death containment facts
no G-to-P post-ACK receipt
no governed write and no P-visible success record
```

A complete `SOCK_SEQPACKET` send proves one complete framed record was
enqueued; it does not prove peer receive or validation.  Pidfd/wait proves
which G died and how, not which G-local instruction or state transition was
last complete.

### 4.3 Every proposed inference is forbidden or insufficient

The following cannot distinguish E0 from E1:

1. **G-local tombstone:** it dies with G and has no frozen cross-owner
   carrier.
2. **P's `AC=1`:** complete send is not G validated acceptance.
3. **EOF or G death:** both executions yield the same facts.
4. **silence, timeout, scheduler order, or elapsed time:** none proves ACK
   receipt or validation, and v9--v11 explicitly forbid success/fact
   inference from them.
5. **socket queue inspection or poll readiness:** the frozen design forbids
   inferred queue state, and no allowed stable receipt survives G death.
6. **trusted/non-Byzantine G:** trust does not imply crash-free execution,
   receipt persistence, or permanent scheduling; `G_CRASH` and `TIMEOUT`
   remain exact failure predicates.
7. **the local atomic commit:** it separates row 33 from row 34 inside live
   G, but says nothing about proving whether G had reached row 33 after G's
   volatile state is gone.

Therefore the proposed 34-row table is not mechanically auditable under the
frozen evidence model.  It is mathematically enumerated but not an admissible
exact-evidence terminal algebra.

### 4.4 Monotonicity makes silent collapse invalid

Mapping every E0/E1 survivor record to `AV=0,BS=0` would avoid fabricating
row 33, but it would erase the completed `AV=1` predecessor in E1.  V10 and
v11 require monotone history and prohibit resetting a one to zero.  Mapping
both to `AV=1,BS=0` would instead fabricate validation in E0.  Reporting an
unknown or probabilistic AV value would violate the proposed binary exact
row table and the no-gray-zone integrity rule.

There is no conforming classification choice.  This is the blocking proof.

## 5. Existing predicates, priorities, fence, and prior closures remain frozen

### 5.1 No classifier change

The exact seventeen raw predicates remain unchanged and independently
computed from admissible evidence:

```text
MISSING MALFORMED DUPLICATE REPLAY WRONG_SESSION WRONG_G_IDENTITY
WRONG_CGROUP WRONG_ATTESTATION WRONG_DIRECTION WRONG_STATE REORDERED
PARTIAL EOF TIMEOUT P_CRASH G_CRASH TRANSPORT_ERROR
```

The separate winner permutation remains:

```text
PARTIAL > DUPLICATE > REPLAY > WRONG_DIRECTION > REORDERED > WRONG_STATE
> MALFORMED > WRONG_SESSION > WRONG_G_IDENTITY > WRONG_CGROUP
> WRONG_ATTESTATION > TRANSPORT_ERROR > EOF > P_CRASH > G_CRASH
> TIMEOUT > MISSING
```

All true losing bits, P-before-G same-label owner tie, earliest causally
closed failure phase, and immutable classification receipt remain frozen.
The blocking problem is not a missing label; it is the absence of evidence
needed to select the correct C12 row before applying the existing label.

### 5.2 Fence and wire counts are not weakened

The v11 fence remains exact: before an actually sealed
`BOOTSTRAP_BOUNDARY_SUCCESS_SEALED`, neither G nor any possible child may
enter lock state, bind, create a candidate or `.owner`, admit a subject,
create a root/package/result/generated/manifest object, or perform any
governed/project write.  The setup/cgroup/private-mount exception remains
setup and containment only.

```text
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_TWO
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=2
V9_NEW_WIRE_FORM=PRIVILEGE_DROP_RELEASE
V11_NEW_WIRE_FORM=GUARDIAN_READY_ACK
V12_NEW_WIRE_FORM_COUNT=0
THIRD_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
```

This gate adds no `BS` field to any wire form and grants no permission to
cross the fence.

### 5.3 Base/v1--v11, counts, and DAG remain unchanged

No prior closure may be traded for this blocked repair.  Base/v1--v11 remain
exactly as currently adjudicated, including v5's blocked/no-op provenance;
v9's exact release bytes and seven-item preimage; v10's nonzero cardinality,
PID binder, monotone history, and classifier; and v11's one ACK, owner
freezes, cross-owner ledger seal, and independent raw bitmap except for its
still-open finding.

```text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
CSV_HEADER_WIDTHS=18,19,22,17,16,19,13,10
EXPLICIT_NEGATIVE_ROWS=35
SEMANTIC_MUTATION_CLASSES=35
PACKAGE_MUTATION_CLASSES=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
TOLERANCE_POLICY=EXACT_ZERO
NETWORK_USED=false
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
```

The graph remains nodes `A D R G I C M V`, chain edges
`A->D->R->G->I->C->M->V`, and additional edges `A->M`, `D->M`, `R->M`,
`G->M`, and `I->M`: exactly eight nodes and twelve distinct edges.

## 6. Mandatory future governance before any further repair

### 6.1 No amendment or review follows this gate

This BLOCKED gate authorizes zero amendment attempts and zero review
attempts.  In particular, it does not authorize creation of
`notes/phase2_control_design_amendment_v12.md`, an append to
`notes/phase2_control_design_peer_review.md`, or any alternate design path.

A fresh review cannot cure absent design evidence.  It may occur only after
a separate future remediation gate authorizes a bounded design carrier, a
separate author creates and externally freezes the exact amendment, and
that future gate's independent-review prerequisites are met.

### 6.2 Minimum question for a separate future gate

A future gate may examine an exact G-to-P seal/validation receipt or another
crash-surviving carrier.  Before it may authorize anything, it must at least:

1. bind this v12 gate's external final receipt and the unchanged complete
   authority tuple in Section 1;
2. state the exact new carrier, owner, direction, channel, canonical bytes,
   framing, field order, identity/session/frame bindings, cardinality,
   one-use state, and crash persistence;
3. prove which event makes `AV=1` independently auditable and how that fact
   survives G death without rollback or inference from send completion;
4. close every window before, during, and after any G-to-P send/receive or
   local seal commit, including G crash after local validation but before
   peer-visible receipt, P crash, partial send, EOF, timeout, duplicate,
   replay, wrong-first, and loss of either owner;
5. decide whether the new carrier requires additional counters, lifecycle
   phases, rows, raw evidence joins, or a change to the global plus-two form
   count, and freeze the complete resulting table rather than preserving a
   false count;
6. retain the strict fail-before-write fence until the new positive boundary
   is both exact and auditable;
7. preserve v9/v10/v11 bindings, exact 12/12/4 scoped enums, every prior
   closure, all scientific/package counts, and the eight-node/twelve-edge
   DAG; and
8. authorize one exact path and attempt only after the future gate itself
   receives an external stable receipt.

This list is a minimum governance question, not authorization or a selected
design.  The future gate may BLOCK again.  In particular:

```text
G_TO_P_SEAL_RECEIPT_AUTHORIZED=false
G_TO_P_VALIDATION_RECEIPT_AUTHORIZED=false
NEW_WIRE_FORM_AUTHORIZED=false
NEW_SHARED_CARRIER_AUTHORIZED=false
AMENDMENT_V12_AUTHORIZED=false
```

### 6.3 Implementation remains quarantined after any future design result

Even a future zero-finding design PASS would grant no source edit, source
acceptance, implementation review, platform preflight, execution, or
generated artifact.  A distinct successor implementation-governance gate
would remain mandatory and would have to bind the exact then-current design,
review, historical implementation gates, and six-path quarantine.

## 7. External freeze of this sole blocking gate

After this file is complete, its author stops.  An external coordinator
computes and freezes:

```text
path=notes/phase2_control_design_remediation_gate_v12.md
type=regular
mode=<actual>
nlink=1
lines=<actual>
bytes=<actual>
sha256=<actual 64-lowercase-hex digest>
```

The coordinator re-hashes the complete current review and every prefix,
base/v1--v11, v9/v10/v11 governance, recovery gate, historical
implementation gates, and six quarantined paths.  Any drift, extra v12
amendment/design path, symlink, hardlink, nonregular target, predicted
self-digest, or post-receipt edit stops.  This gate cannot contain its own
final digest without changing that digest.

The external receipt authenticates only this blocking governance record.  It
does not create amendment, review, source, or execution authority.

## 8. Authorization matrix and stop

```text
GATE_KIND=DESIGN_REMEDIATION_FEASIBILITY_AND_CRASH_RETENTION_AUDIT_ONLY
GATE_VERDICT=BLOCKED_NO_AMENDMENT_V12_AUTHORITY
BLOCKER=AV1_BS0_G_LOCAL_STATE_NOT_CRASH_SURVIVING_OR_INDEPENDENTLY_AUDITABLE
CURRENT_REVIEW_VERDICT=REVISE_C0_M1_m0

P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN
P15R_V9_m1_STATUS=OPEN
P15R_V10_M1_STATUS=OPEN
P15R_V10_m1_STATUS=OPEN
P15R_V11_M1_STATUS=OPEN

CURRENT_EFFECTIVE_AMENDMENT_COUNT=11
BLOCKED_NO_OP_AMENDMENT_V5_RETAINED=true
AMENDMENT_V12_WRITE_AUTHORIZED=false
AMENDMENT_V12_ATTEMPTS_AUTHORIZED=0
AUTHORIZED_AMENDMENT_PATH=NONE
OTHER_AMENDMENT_OR_DESIGN_PATH_AUTHORIZED=false
AUTHOR_SELF_CLOSURE_AUTHORIZED=false
REVIEW_VERDICT_PREJUDGED=false

PROPOSED_C12_EFFECTIVE=false
PROPOSED_BS_BIT_AUTHORIZED=false
PROPOSED_VECTOR_COUNT_EFFECTIVE=false
PROPOSED_ATOMIC_LOCAL_COMMIT_AUTHORIZED=false
AV1_BS0_ROLLBACK_AUTHORIZED=false
AV1_BS0_FABRICATED_RECEIPT_AUTHORIZED=false
SUCCESS_FROM_SILENCE_AUTHORIZED=false
SUCCESS_FROM_ACK_COMPLETE_SEND_AUTHORIZED=false
QUEUE_STATE_INFERENCE_AUTHORIZED=false

G_TO_P_SEAL_RECEIPT_AUTHORIZED=false
G_TO_P_VALIDATION_RECEIPT_AUTHORIZED=false
NEW_WIRE_FORM_AUTHORIZED=false
NEW_SHARED_CARRIER_AUTHORIZED=false
THIRD_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
ACK_OF_ACK_AUTHORIZED=false
RETRY_AUTHORIZED=false
FALLBACK_AUTHORIZED=false
RECONNECT_AUTHORIZED=false
RECORD_REUSE_AUTHORIZED=false

FRESH_APPEND_ONLY_REREVIEW_AUTHORIZED=false
FRESH_APPEND_ONLY_REREVIEW_ATTEMPTS_AUTHORIZED=0
REREVIEW_PATH_AUTHORIZED=NONE
REREVIEW_PREFIX_REWRITE_AUTHORIZED=false

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
CSV_GENERATION_AUTHORIZED=false
MANIFEST_GENERATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
AUTHOR_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0
INDEPENDENT_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0

MANIFEST_SCHEMA_CHANGE_AUTHORIZED=false
DAG_CHANGE_AUTHORIZED=false
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
```

Final determination: **BLOCKED**.  The no-new-wire `BS` extension can model
one local atomic commit and can enumerate 33 failure shapes plus one success,
but it cannot preserve and independently expose the decisive `AV=1,BS=0`
fact after a precommit G crash.  The fixed-observation E0/E1 pair has
different true rows and identical admissible surviving evidence.  Neither
fabrication nor monotone-history rollback is allowed.  Therefore no v12
amendment, review append, source action, implementation action, run,
precheck, generated artifact, proof, Route, manuscript, release, archive, or
Git action follows from these bytes.  Only a separate future governance gate
may decide whether to authorize an exact crash-surviving G-to-P receipt or
another bounded carrier.
