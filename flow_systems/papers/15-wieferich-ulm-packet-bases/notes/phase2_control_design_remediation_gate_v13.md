# Replacement Paper 15 control-design remediation gate v13

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v13 ONLY — CURRENT REVIEW REMAINS REVISE C0/M1/m0**  
Date: 2026-08-17 (Asia/Shanghai)  
Gate class: exact-byte design-remediation and crash-surviving seal governance  
Sole repository write in this gate-authoring step: `notes/phase2_control_design_remediation_gate_v13.md`  
Current open findings: `P15R-REOPEN-M1`, `P15R-V9-M1`,
`P15R-V9-m1`, `P15R-V10-M1`, `P15R-V10-m1`, and
`P15R-V11-M1`  
Source, implementation, execution, precheck, generated-artifact, Route,
manuscript, release, archive, and Git authority: **none**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**

## Material Passport

- **Material type:** one bounded design-remediation governance gate.
- **Question:** can `P15R-V11-M1` be repaired by exactly one authenticated
  G-to-P `BOOTSTRAP_SEALED` record, with no durable/shared log and no
  acknowledgment of that record?
- **Determination:** **PASS TO ONE VERSIONED DESIGN AMENDMENT v13 ONLY.**
  Under the already frozen Linux AF_UNIX `SOCK_SEQPACKET` ceiling, one
  complete canonical send atomically queues one packet on P's retained sole
  endpoint; last-close/G death cannot retract that queued packet.  Therefore
  G's complete canonical `BOOTSTRAP_SEALED` send can be the sole positive
  linearization point and can leave crash-surviving evidence at P even if G
  dies before P executes its later receive.
- **Essential state repair:** ACK parse, validation, digest recomputation,
  and seal staging at G are private ephemeral work.  They create no public,
  terminal, serialized, tombstoned, or otherwise auditable `AV` state.  The
  v11 stable state `GUARDIAN_READY_ACK_VALIDATED` is superseded and the v11
  `AV` lifecycle coordinate is replaced, not supplemented, by `SS`, the
  externally committed complete-canonical-seal-send bit.
- **Positive boundary:** G's exact full send of the canonical seal frame is
  simultaneously (i) the `SS:0->1` transition, (ii) the global bootstrap
  success boundary, (iii) the publication of the immutable seal receipt,
  and (iv) the first release of governed-write authority.  No governed write
  is legal before that full send completes.
- **Failure boundary:** any failure, crash, timeout, partial result, errno,
  or transport loss before a full canonical seal send retains `SS=0` and
  claims neither stable ACK validation nor a seal.  It is classified from
  exact available evidence; no vanished G-local fact is reconstructed.
- **No infinite handshake:** P's later exact receive and validation is audit
  confirmation of an already committed boundary.  It is not a prerequisite
  for G's first write, is not an ACK of the seal, and sends no response.
- **Platform stop rule:** the amendment must extend the existing disposable
  AF_UNIX preflight with the exact sender-full-send, sole-holder last-close,
  receiver-exact-frame, then EOF sequence below.  Failure is
  `E_POSSESSION_UNAVAILABLE` before any governed write.  If the invariant
  cannot be established without a new registered child, changed count, new
  path, or fallback, amendment v13 is BLOCKED and stops.
- **Finding posture:** this gate closes, downgrades, or pre-judges no
  finding.  `P15R-V11-M1` remains OPEN and the current result remains
  `REVISE_C0_M1_m0` until one fresh independent append-only review returns
  an evidence-backed verdict on the complete successor tuple.
- **Version posture:** v12 remains a blocking governance record and
  `notes/phase2_control_design_amendment_v12.md` remains absent.  A valid
  successor is base plus active amendments v1--v11 and v13: twelve active
  amendment records, with the v12 amendment path explicitly skipped.
- **Evidence ceiling:** no source conformance, platform availability,
  runtime behavior, deterministic replay, theorem recovery, or publication
  readiness is claimed by this static gate.

## 1. Exact authority, complete intake, and unchanged byte state

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

This was static design/governance intake.  No project path was imported,
sourced, compiled, parsed as project code, syntax-checked, or executed.  No
platform probe, preflight, generator, verifier, unittest, wrapper,
reproduction, cache, temporary, lock, result, manifest, or generated member
was created or run.

### 1.2 Complete current review and preserved prefixes

The complete current append-only review was freshly byte-read and re-hashed:

| Record | Lines | Bytes | SHA-256 | Current result |
|---|---:|---:|---|---|
| `notes/phase2_control_design_peer_review.md` | 5527 | 296651 | `0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c` | `REVISE_C0_M1_m0` |

Its current and nested historical boundaries remain:

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

The 296,651-byte record is the sole current adjudicative result.  Every
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
| remediation gate v12 | 789 | 37732 | `ac5e997419f1123218c662ab579e42274ad8774faf3634db1d7b6c51e8ccc999` | BLOCKED; zero amendment/review authority |

V12 correctly proves that a no-new-wire local `AV=1,BS=0` state is not
crash-surviving.  It authorized no amendment v12, and that amendment path is
absent.  V13 does not reinterpret v12 as approval; it supplies the separate
future carrier v12 required.

The current effective tuple remains base plus v1--v11, with v5 retained as
blocked/no-op provenance.  Its current active amendment-record count is
eleven.  This governance record itself adds no amendment and no semantic
design clause.  Only a conforming externally frozen v13 amendment would
make the active successor count twelve.

### 1.4 Historical implementation gates and unchanged six-path quarantine

The historical implementation gates were freshly byte-read and re-hashed:

| Historical nonauthorizing record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_implementation_gate.md` | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` |
| `notes/phase2_control_implementation_remediation_gate_v1.md` | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` |

Both are consumed provenance and nonauthorizing.  Neither this gate, a v13
amendment, nor a later design PASS silently revives them.

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

At gate-authoring start, all three paths below were absent under ordinary
existence and lstat-path reasoning:

```text
notes/phase2_control_design_remediation_gate_v13.md
notes/phase2_control_design_amendment_v12.md
notes/phase2_control_design_amendment_v13.md
```

No same-named path existed elsewhere in the workspace.  This gate target is
the sole write.  No amendment, review append, source, implementation,
precheck, cache, temporary, lock, receipt, result, manifest, generated,
Route, manuscript, release, archive, or Git path was created or changed.

## 2. Current finding and exact v13 remediation budget

### 2.1 `P15R-V11-M1` remains OPEN

The current review identifies one Major, high-confidence defect.  V11 made
`GUARDIAN_READY_ACK_VALIDATED` and
`BOOTSTRAP_BOUNDARY_SUCCESS_SEALED` successive G-local stable states.  A G
crash between them leaves true `AV=1` history that P cannot distinguish from
a crash before validation.  V12 proves that adding a second local bit cannot
repair the missing cross-owner carrier.

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

This gate is governance, not an independent review, and has no finding-
closure authority.

### 2.2 Sole authorized semantic delta

Exactly one later authoring attempt may create:

```text
notes/phase2_control_design_amendment_v13.md
```

Its complete permitted delta is:

1. add exactly one authenticated global G-to-P form named
   `BOOTSTRAP_SEALED` on the existing connected P--G `SOCK_SEQPACKET`
   control, after the exact v11 ACK and before every lock, child, object,
   transaction, or governed-write form;
2. supersede the stable/public v11 state
   `GUARDIAN_READY_ACK_VALIDATED`; ACK parse, validation, recomputation, and
   staging become private ephemeral work with no public state transition;
3. replace v11 lifecycle coordinate `AV` with `SS`, the complete canonical
   `BOOTSTRAP_SEALED` send/queue commit; do not retain both coordinates and
   do not introduce a renamed hidden validation bit;
4. make G's one complete canonical seal send the sole linearization for
   global success, immutable seal publication, and first governed-write
   release;
5. make P's later exact receipt/validation an audit confirmation only, with
   no response form and no influence on G's first-write authorization;
6. extend the existing P-only AF_UNIX disposable-pair preflight exactly as
   Section 3 requires, without a new registered child, method, count, path,
   or fallback; and
7. preserve every other v11/v10/v9 and base/v1--v8 clause, including v5's
   blocked/no-op provenance, except where this gate expressly supersedes the
   ACK-to-seal cut and global form count.

### 2.3 No broader repair and mandatory BLOCK rule

The amendment may not add a seal ACK, ACK-of-ACK, challenge, nonce exchange,
retry, fallback, reconnect, correction form, compatibility parse, alternate
endpoint, new descriptor, durable/shared log, shared-memory commit, new
syscall dependency, repository receipt, schema field, generated member,
authority binding, DAG node, or edge.

It may not preserve `GUARDIAN_READY_ACK_VALIDATED` under another name,
serialize ACK validation, put `AV` beside `SS`, or classify a pre-send G
crash from a local fact that died with G.  It may not infer success from
silence, timeout, EOF, poll readiness, expected behavior, queue inspection,
or ACK complete-send alone.

If one G-to-P seal cannot supply crash-surviving evidence under the exact
Section-3 transport/preflight contract without another ACK or shared
persistence, amendment v13 is **BLOCKED**.  The author stops and creates no
alternate amendment/design path.

## 3. Exact crash-surviving transport and availability contract

### 3.1 Frozen AF_UNIX `SOCK_SEQPACKET` invariant

The one-form proof is bounded to Linux AF_UNIX `SOCK_SEQPACKET` and these
exact facts:

1. the global P--G control is one already authenticated connected
   `SOCK_SEQPACKET` pair;
2. G owns the sole G endpoint and P owns the sole peer endpoint at the seal
   cut; no launcher, child, worker, helper, or other process retains or can
   read either description;
3. a complete send of exact frame length atomically enqueues exactly one
   record with the same bytes on the peer receive queue; there is no partial
   successful record;
4. after that enqueue, close of G's sole endpoint, G exit, or G death cannot
   retract or mutate the queued record;
5. P retains its endpoint and does not half-close, close, duplicate, pass,
   or let another consumer drain it before the one seal audit slot is
   resolved;
6. after G's sole endpoint closes, P receives already queued records in G's
   send order before it receives zero-byte EOF; and
7. an exact valid seal packet is evidence, while readiness, queue length,
   silence, time, EOF alone, or inferred packet presence is not.

This is crash-surviving with respect to loss of G because the immutable
record is receiver-queued.  It is not a claim of durable disk persistence
or universal recovery after destruction of both authenticated owners and
both endpoint descriptions.  `UNIVERSAL_RECOVER_P` remains open and
unauthorized.

### 3.2 Exact extension of the existing disposable-pair preflight

The amendment must extend, not replace, v4 Section 4.2's existing P-only
pair-A/pair-B preflight.  After the four reciprocal true-pair queries and
both crossed-pair rejections succeed, and before A1 is closed, P performs
this exact additional subtest on pair A:

```text
queue_preflight_payload = ASCII("P15R-SEAL-QUEUE-RETENTION-PREFLIGHT-v13")
queue_preflight_frame = U32BE(byte_length(queue_preflight_payload)) ||
                        queue_preflight_payload

1. A0 is the sole holder of the sender file description and A1 is the sole
   holder of its peer; neither endpoint was duped, inherited, or passed.
2. P performs exactly one zero-ancillary send of queue_preflight_frame on A0.
3. Success requires return == byte_length(queue_preflight_frame).
4. P closes A0 immediately; sole-holder last-close is the exact operational
   surrogate for all G sender descriptions closing on G death.
5. P performs one recvmsg on A1 with a buffer larger than the frame and
   requires exactly queue_preflight_frame, no ancillary item, no
   MSG_TRUNC/MSG_CTRUNC, and no trailing byte.
6. P performs the next receive on A1 and requires exact zero-byte EOF with
   no ancillary item or residual record.
7. P closes A1, re-queries still-live pair B in both directions exactly as
   v4 already requires, and then closes B0 and B1.
```

EINTR may retry only the same incomplete syscall against the existing
absolute preflight deadline.  A short positive return, wrong bytes, early
EOF, extra packet, ancillary data, truncation, errno, timeout, nonunique
holder, failed close, or changed B reciprocal result is
`E_POSSESSION_UNAVAILABLE`.  P closes disposable endpoints and the Netlink
FD and follows inherited bootstrap containment before U1 mapping resumes.

This adds no registered child, target, method, CSV row, public detector,
serialized record, manifest member, path, or count.  If sole-holder
last-close cannot mechanically stand for sender death on the frozen
platform, or the exact sequence cannot pass, no source implementation may
continue to release/READY/ACK/seal or perform any governed write.  There is
no fake receipt and no fallback.

### 3.3 Exact global endpoint holder and audit lifetime

The v13 amendment must state these live-system obligations:

- all transient launcher/setup copies of the global endpoint are closed and
  proven absent before G sends READY;
- no possible child exists before the seal because the fail-before-write
  fence also forbids child admission/creation;
- G's endpoint is never duplicated or passed after READY emission freeze;
- P's endpoint remains in a sole-reader audit state from its complete ACK
  send through exact seal receipt/validation or terminal drain/EOF;
- P performs no speculative receive, queue query, alternate-reader handoff,
  half-close, or endpoint close in that interval; and
- on G death, P first drains the exact expected record slot, retaining full
  bytes and digest if present, and only then accepts EOF as secondary
  containment evidence.

A conforming full canonical seal packet before G death therefore remains
available to P after death.  If no valid packet exists, G death/EOF proves
only failure; it never synthesizes `SS=1`.

## 4. Exact `BOOTSTRAP_SEALED` form

### 4.1 Canonical payload, framing, direction, and cardinality

The sole v13 payload is exactly one canonical ASCII payload without LF,
NUL, or trailing byte:

```text
BOOTSTRAP_SEALED session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC release_frame_sha256=LOWERHEX64 release_attestation_sha256=LOWERHEX64 ready_frame_sha256=LOWERHEX64 ack_frame_sha256=LOWERHEX64 p_seal_sha256=LOWERHEX64 x_p=0 x_g=0 p_freeze_receipt_sha256=LOWERHEX64 g_freeze_receipt_sha256=LOWERHEX64 bootstrap_seal_sha256=LOWERHEX64
```

Every field occurs exactly once and in exactly that order.  `DEC` and
`LOWERHEX64` retain the inherited canonical unsigned-decimal and exact
64-lowercase-hex grammar.  The record inherits the existing four-byte
unsigned big-endian payload-length prefix, 4096-byte ceiling, exact-length,
canonical-ASCII, authenticated-peer, complete-send/receive, and closed-state
rules.  It has zero ancillary items.

The form is G-to-P only.  G has exactly one authorized send attempt after
the complete private staging in Section 5.  P has exactly one expected
receive/validation slot after its complete v11 ACK send.  There is no retry,
correction, reconnect, fallback, response, ACK-of-seal, or record reuse.

On a successful bootstrap the exact boundary traffic is:

```text
P -> G: LAUNCHER_REAPED                 exactly once
P -> G: PRIVILEGE_DROP_RELEASE          exactly once
G -> P: GUARDIAN_READY                  exactly once
P -> G: GUARDIAN_READY_ACK              exactly once
G -> P: BOOTSTRAP_SEALED                exactly once
```

`BOOTSTRAP_SEALED` is inserted immediately after `GUARDIAN_READY_ACK` in
the global closed enum and before every lock/child/object/transaction form.
It is not a D-M1, D-M2, or requester form.

### 4.2 Exact identity and frame bindings

The first six fields bind the same bootstrap/global session, surviving G
outer PID, literal G inner PID 1, exact G starttime, and guardian cgroup
device/inode used by v9--v11.  All inherited L/G inequalities and
pidfd/proc/cgroup joins remain exact.

For v13 only, retain the inherited mathematical byte functions:

```text
FRAME(payload) = U32BE(byte_length(payload)) || payload
FRAME_SHA256(payload) = SHA256(FRAME(payload))
ITEM(tag,value) = U16BE(tag) || U64BE(byte_length(value)) || value
```

The four frame/digest joins are:

```text
release_frame_sha256 = SHA256(exact framed PRIVILEGE_DROP_RELEASE bytes)
release_attestation_sha256 = exact v9 attestation field from that release
ready_frame_sha256 = SHA256(exact framed GUARDIAN_READY bytes)
ack_frame_sha256 = SHA256(exact framed GUARDIAN_READY_ACK bytes)
p_seal_sha256 = exact v11 P seal, independently recomputed by G
```

P sent the release and ACK and received READY; G received the release and
ACK and sent READY.  Both can therefore retain the exact raw frames and
recompute every digest without normalized text, inferred packets, or peer-
reported bytes.  A digest is a receipt, not a secret or capability.

### 4.3 Exact P owner-freeze receipt

V13 retains v11's exact `ack_binding_ascii`, `p_counts_ascii`,
`p_freeze_ascii`, exact P ledgers, and nine-item P seal preimage without
changing one byte.  Define:

```text
p_freeze_receipt_ascii =
owner=P state=P_OLD_BOUNDARY_LEDGER_FROZEN old_form_emit_frozen=1 old_form_observe_frozen=1 x_p=0 p_seal_sha256=LOWERHEX64

p_freeze_receipt_preimage =
ASCII("P15R-P-OWNER-FREEZE-RECEIPT-v13") ||
U32BE(3) ||
ITEM(1,ack_binding_ascii) ||
ITEM(2,p_freeze_receipt_ascii) ||
ITEM(3,exact_v11_p_seal_preimage)

p_freeze_receipt_sha256 = SHA256(p_freeze_receipt_preimage)
```

The `LOWERHEX64` inside `p_freeze_receipt_ascii` is the same concrete
`p_seal_sha256` carried by the ACK and seal payload.  No placeholder enters
the hashed runtime bytes.  Both P and G reconstruct the complete value from
the exact retained v11 inputs.

### 4.4 Exact G owner-freeze receipt

V13 reuses v11's `LEDGER` and `ENTRY` encodings.  Define the exact G ledgers:

```text
g_old_emit_ledger_binary = LEDGER(
  ENTRY(1,3,exact framed GUARDIAN_READY bytes)
)

g_old_observe_ledger_binary = LEDGER(
  ENTRY(2,1,exact framed LAUNCHER_REAPED bytes),
  ENTRY(2,2,exact framed PRIVILEGE_DROP_RELEASE bytes)
)
```

The action/form codes retain v11's meanings.  ACK is not added to the old-
form ledger; its exact frame is a separate preimage item.

The fixed ASCII values are:

```text
g_counts_ascii =
g_launcher_complete_receive_count=1 g_release_complete_receive_count=1 g_release_validated_receive_count=1 g_ready_send_attempt_count=1 g_ready_complete_send_count=1 g_ack_complete_receive_count=1 x_g=0

g_freeze_ascii =
owner=G state=G_OLD_BOUNDARY_EMISSION_FROZEN old_form_emit_frozen=1 old_form_observe_frozen=1 x_g=0

g_owner_use_ascii =
owner=G one_use=1 entropy=NONE ack_validation_publication=NONE
```

Each displayed value is one ASCII line without LF, NUL, leading/trailing
space, alternate spelling, or normalization.  Define:

```text
g_freeze_receipt_preimage =
ASCII("P15R-G-OWNER-FREEZE-RECEIPT-v13") ||
U32BE(10) ||
ITEM(1,ack_binding_ascii) ||
ITEM(2,exact framed LAUNCHER_REAPED bytes) ||
ITEM(3,exact framed PRIVILEGE_DROP_RELEASE bytes) ||
ITEM(4,exact framed GUARDIAN_READY bytes) ||
ITEM(5,exact framed GUARDIAN_READY_ACK bytes) ||
ITEM(6,g_counts_ascii) ||
ITEM(7,g_old_emit_ledger_binary) ||
ITEM(8,g_old_observe_ledger_binary) ||
ITEM(9,g_freeze_ascii) ||
ITEM(10,g_owner_use_ascii)

g_freeze_receipt_sha256 = SHA256(g_freeze_receipt_preimage)
```

`g_ack_complete_receive_count=1` records exact complete frame receipt, not a
stable validation state.  Complete semantic validation is a precondition
for constructing the canonical seal but has no independent public bit.

### 4.5 Exact bootstrap-seal receipt digest

Define:

```text
seal_binding_ascii =
session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC

seal_commit_ascii =
owner=G form=BOOTSTRAP_SEALED direction=G_TO_P channel=GLOBAL_CONTROL one_use=1 entropy=NONE x_p=0 x_g=0 ack_validation_publication=NONE linearization=COMPLETE_CANONICAL_FRAME_SEND

bootstrap_seal_preimage =
ASCII("P15R-BOOTSTRAP-SEALED-RECEIPT-v13") ||
U32BE(8) ||
ITEM(1,seal_binding_ascii) ||
ITEM(2,exact framed PRIVILEGE_DROP_RELEASE bytes) ||
ITEM(3,ASCII(release_attestation_sha256)) ||
ITEM(4,exact framed GUARDIAN_READY bytes) ||
ITEM(5,exact framed GUARDIAN_READY_ACK bytes) ||
ITEM(6,p_freeze_receipt_preimage) ||
ITEM(7,g_freeze_receipt_preimage) ||
ITEM(8,seal_commit_ascii)

bootstrap_seal_sha256 = SHA256(bootstrap_seal_preimage)
```

All dynamic `DEC` and digest tokens in the displayed ASCII templates are
replaced by their one canonical concrete values before hashing.  No random
entropy, nonce, clock, PID alias, native-endian field, separator ambiguity,
omitted item, duplicate item, normalization, or trailing byte exists.

Only G constructs the receipt after completely validating the ACK and every
raw-frame/freeze join.  P independently recomputes it from its exact
retained frames and the received canonical fields.  Hashing the final
payload including its own digest is forbidden; the eight-item preimage is
the only seal-receipt authority.

## 5. Ephemeral staging, sole linearization, and later audit

### 5.1 ACK validation and staging are not lifecycle state

After G's sole complete ACK-slot receive, G privately performs all parsing,
canonicality, session/G/cgroup identity, raw-frame digest, v9 attestation,
v11 P-seal, `X_P=0`, `X_G=0`, owner-freeze, one-use, and replay checks.  It
preallocates and fills the complete seal preimages, hashes, payload, length
prefix, and send buffer.

This work is **ephemeral and unpublished**:

- there is no `GUARDIAN_READY_ACK_VALIDATED` state;
- there is no stable `AV`, validation receipt, tombstone coordinate,
  repository artifact, shared-memory flag, or peer-visible transition;
- no failure record claims that validation completed;
- no governed write, child, lock, object, transaction, or generated member
  is admitted; and
- a crash or timeout at any point before full canonical seal send retains
  the last externally evidenced predecessor with `SS=0`.

The private staging buffer can be discarded on failure.  Discarding it does
not roll back history because it was never published as history.

### 5.2 Complete send is the one positive commit

G performs exactly one zero-ancillary send of the complete framed canonical
`BOOTSTRAP_SEALED` record.  Only the atomic complete-record enqueue and exact
full-length success constitute `SS:0->1`.  At that same linearization point:

```text
bootstrap_outcome = SUCCESS
G state = BOOTSTRAP_BOUNDARY_SUCCESS_SEALED
immutable bootstrap seal receipt = published
first governed-write authority = released to G
```

The complete-send event is the one kernel atomic-enqueue event, not a second
userspace state after it.  If G remains live, return of the exact frame
length is G's receipt of that event and is mandatory before G may exercise
the released write authority.  If G dies before it can retain that return,
P's later exact canonical packet is the crash-surviving receipt of the same
already completed event; P does not create a later `SS` transition.  Under
the frozen platform contract, a partial return or terminal errno does not
coexist with a complete queued record.  If a platform cannot preserve that
disjointness, Section 3 fails with `E_POSSESSION_UNAVAILABLE`.

There is no stable intermediate among those four facts.  No syscall,
allocation, parse, hash, copy, lock operation, or governed write occurs
inside an abstract split commit; the send/enqueue itself is the commit.

Before the complete canonical send, governed write authority is false.
After it, G may proceed without waiting for P.  A later G crash, P audit,
EOF, timeout, cleanup failure, child failure, or downstream protocol event
cannot flow backward across the already committed boundary.

### 5.3 Exact precommit failure cases

The following all retain `SS=0` and authorize no first write:

| Exact event before full canonical seal enqueue | Retained boundary consequence |
|---|---|
| ACK missing, partial, malformed, wrong-first, duplicate, replay, wrong session/identity/cgroup/attestation/state/direction/order | existing exact raw bits; no stable validation claim |
| owner freeze or X join fails | failure with exact available ledger/receipt; no seal |
| staging allocation/hash/construction fails | local operation evidence if retained; no published validation or seal |
| seal send returns positive short/partial | `PARTIAL`, `SS=0`, no retry |
| seal send returns terminal errno with no complete record | `TRANSPORT_ERROR`, `SS=0`, no retry |
| P endpoint is gone before enqueue | transport/P-crash evidence, `SS=0` |
| G crashes or is killed before complete enqueue | `G_CRASH`, `SS=0`; P drains exact slot then EOF |
| deadline fires before complete enqueue | `TIMEOUT` plus applicable losing bits, `SS=0` |
| no canonical seal at deterministic terminal checkpoint | `MISSING`, `SS=0` |

A send attempt has no lifecycle coordinate.  If an exact local attempt
receipt survives it may be retained as secondary evidence, but its absence
after G death is never guessed.  A form-shaped but noncanonical full packet
is not a canonical `BOOTSTRAP_SEALED` commit and cannot set `SS`.

### 5.4 P's later audit is confirmation, never an ACK

P has one expected seal slot after complete ACK send.  It receives at most
one complete record for that slot and validates exact framing, authenticated
G direction, field order/grammar, identity/cgroup bindings, raw-frame
digests, both freeze receipts, both X zeros, and the eight-item seal digest.

An exact valid record yields local audit state
`P_BOOTSTRAP_SEAL_AUDIT_CONFIRMED` and retains the complete frame and its
SHA-256.  That state confirms a boundary already linearized at G's complete
send; it does not set `SS`, authorize G, or send any record.

A malformed, partial, extra, wrong-bound, or wrong-digest packet is
fail-closed and retains exact raw evidence.  It cannot create `SS` after the
fact.  Under the trusted non-Byzantine and byte-preserving transport ceiling,
such a mismatch means no canonical seal commit occurred; this is absence of
the success predicate, not rollback of a prior valid success.  EOF without
a valid queued packet is failure evidence only.  EOF after an exact valid
packet is a later G-close consequence and does not revoke success.

## 6. Externally committed lifecycle algebra and all 33 vectors

### 6.1 Exact v13 tuple and projections

The v13 tuple is, in this exact order:

```text
C13 = (SA,SC,VA,X_P,X_G,RA,RC,RV,AA,AC,SS)

SA = release send-attempt count at P
SC = release complete-send count at P
VA = release validated-accept count at G
X_P = P owner-local out-of-slot old-form bit
X_G = G owner-local out-of-slot old-form bit
RA = READY send-attempt count at G
RC = READY complete-send count at G
RV = READY validated-receive count at P
AA = ACK send-attempt count at P
AC = ACK complete-send count at P
SS = canonical BOOTSTRAP_SEALED complete-send/queue commit bit

X = X_P | X_G
C10 = (SA,SC,VA,X,RA,RC,RV)
```

Every coordinate is binary.  `SS` replaces v11 `AV`; there is no twelfth
coordinate, hidden validation bit, or stable validated-only state.  P's
later audit confirmation is outside C13 because it is downstream of the
positive boundary.

### 6.2 Complete invariants

```text
SC <= SA
VA <= SC
RA <= VA
RC <= RA
RV <= RC
AA <= RV
AC <= AA
SS <= AC

if VA == 0 then (RA,RC,RV,AA,AC,SS) == (0,0,0,0,0,0)
if RV == 0 then (AA,AC,SS) == (0,0,0)
if AA == 1 then X_P == 0 and P_OLD_BOUNDARY_LEDGER_FROZEN == true
if SS == 1 then (SA,SC,VA,RA,RC,RV,AA,AC) == (1,1,1,1,1,1,1,1)
if SS == 1 then X_P == 0 and X_G == 0
if SS == 1 then both exact owner-freeze receipts are bound
if SS == 1 then exact bootstrap_seal_sha256 is bound
if SS == 1 then G state == BOOTSTRAP_BOUNDARY_SUCCESS_SEALED
if X == 1 then bootstrap_outcome == FAILURE

bootstrap_outcome == SUCCESS iff
  C13 == (1,1,1,0,0,1,1,1,1,1,1)
  and one complete canonical BOOTSTRAP_SEALED frame was atomically queued
  and the immutable eight-item seal receipt was thereby published
```

The `11` local-X combination remains feasible only at causally incomparable
pre-freeze failure cuts.  Once P freezes with `X_P=0`, no ACK-stage vector
with `X_P=1` is legal.  `SS=1` admits no nonzero X bit.

### 6.3 Exhaustive mutually exclusive table

The table below is complete.  Rows 1--30 preserve v11 predecessor
cardinalities with `SS=0`.  Rows 31--32 collect every exact post-complete-ACK,
pre-complete-seal failure without claiming whether private validation or
staging occurred.  Row 33 is the only success.

| # | SA | SC | VA | X_P | X_G | RA | RC | RV | AA | AC | SS | Exact lifecycle class | Outcome |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `PRE_SEND_FAILURE` | FAILURE |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 6 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 8 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `PARTIAL_SEND_FAILURE` | FAILURE |
| 9 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 10 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 11 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 12 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 13 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 14 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 15 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 16 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| 17 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 18 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 19 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 20 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| 21 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 22 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 23 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 25 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | `POST_READY_PRE_ACK_FAILURE` | FAILURE |
| 26 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| 27 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| 28 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| 29 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | `ACK_PARTIAL_SEND_FAILURE` | FAILURE |
| 30 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | `ACK_PARTIAL_SEND_FAILURE` | FAILURE |
| 31 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | `ACK_COMPLETE_PRE_SEAL_COMMIT_FAILURE` | FAILURE |
| 32 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | `ACK_COMPLETE_PRE_SEAL_COMMIT_FAILURE` | FAILURE |
| 33 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | `BOOTSTRAP_SEALED_COMMIT` | SUCCESS |

```text
V13_VECTOR_COUNT=33
V13_FAILURE_VECTOR_COUNT=32
V13_SUCCESS_VECTOR_COUNT=1
V13_STABLE_ACK_VALIDATED_COORDINATE_COUNT=0
```

No omitted tuple satisfies the prefix constraints.  The former v11
validated-but-unsealed counterexample is not a distinct row because its
private validation step is not a committed lifecycle transition.  A crash
there is exactly row 31, and P never has to choose between two unobservable
values.  A full canonical seal send is row 33, and its queued packet survives
G death for P's audit.

### 6.4 Monotone history and tombstones

Every published transition is monotone.  A failure tombstone copies C13,
all exact externally retained predecessors, raw frames/digests, available
operation receipts, identities, owner freezes, classifier receipt, and
secondary evidence.  It never resets one to zero and never inserts private
validation/staging work as a completed predecessor.

In particular:

```text
ACK completely sent; G fails before canonical seal complete send:
  retain row 31 or 32 and SS=0
  retain no AV and no claimed ACK-validation receipt

seal send partial/errno/crash before complete enqueue:
  retain row 31, SS=0, and exact available cause evidence

canonical seal completely enqueued; G then crashes:
  retain row 33
  P receives the queued exact frame before EOF and confirms the receipt

canonical seal confirmed; later P/G/child/cleanup failure:
  append secondary/downstream evidence only
  never rewrite SS or flow backward across bootstrap success
```

This preserves all real committed history while avoiding both v12 forbidden
choices: fabricating `AV=1` and rolling a real stable `AV=1` back to zero.
There is no stable AV to fabricate or erase.

## 7. Classifier, fence, form counts, and prior preservation

### 7.1 Exact raw predicates and winner remain frozen

The exact seventeen independent raw predicates remain:

```text
MISSING MALFORMED DUPLICATE REPLAY WRONG_SESSION WRONG_G_IDENTITY
WRONG_CGROUP WRONG_ATTESTATION WRONG_DIRECTION WRONG_STATE REORDERED
PARTIAL EOF TIMEOUT P_CRASH G_CRASH TRANSPORT_ERROR
```

They are computed from admissible evidence before priority.  The winner
permutation remains:

```text
PARTIAL > DUPLICATE > REPLAY > WRONG_DIRECTION > REORDERED > WRONG_STATE
> MALFORMED > WRONG_SESSION > WRONG_G_IDENTITY > WRONG_CGROUP
> WRONG_ATTESTATION > TRANSPORT_ERROR > EOF > P_CRASH > G_CRASH
> TIMEOUT > MISSING
```

All true losing bits, P-before-G same-label owner tie, earliest causally
closed failure phase, and immutable classification receipt remain frozen.
V13 extends the phase vocabulary only with
`POST_ACK_COMPLETE_PRE_SEAL_COMMIT` and `SEAL_SEND`; these are
nonserialized classifier phases, not wire forms or lifecycle coordinates.

An invalid complete seal packet may set MALFORMED, WRONG_SESSION,
WRONG_G_IDENTITY, WRONG_CGROUP, WRONG_ATTESTATION, WRONG_DIRECTION,
WRONG_STATE, REORDERED, DUPLICATE, or REPLAY as independently warranted.
A partial seal send sets PARTIAL.  An errno, EOF, crash, or deadline uses
the existing corresponding bits.  No new raw label is authorized.

### 7.2 Exact fail-before-write fence

Before G's complete canonical `BOOTSTRAP_SEALED` send commits `SS=1`, neither
G nor any possible child may:

- create a lock candidate or `.owner`;
- enter `ACQUIRING`, call bind, or claim lock possession;
- create a generation root, method root, subject root, package copy, result,
  generated member, manifest member, or publication staging object;
- admit, start, or expose a subject, runner, wrapper, generator, verifier,
  test, mutation worker, replacement actor, holder, or contender;
- accept or execute a session, lock, root, spawn, audit, object, cleanup,
  exchange, foreign-audit, or other transaction operation; or
- perform any subject, package, result, lock, object, generation, manifest,
  repository, or governed write.

The inherited setup/cgroup/private-mount and exact preflight exceptions
remain setup/availability/containment only.  ACK receipt, private validation,
private staging, seal send attempt, poll readiness, or P's later audit state
is not write authority.  The v11 fence sentence is superseded to:

```text
Only G's complete canonical BOOTSTRAP_SEALED send may enter lock state or
release the first governed write.
```

### 7.3 Exact global and scoped form counts

```text
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
V9_NEW_WIRE_FORM=PRIVILEGE_DROP_RELEASE
V11_NEW_WIRE_FORM=GUARDIAN_READY_ACK
V13_NEW_WIRE_FORM=BOOTSTRAP_SEALED
V13_NEW_WIRE_FORM_COUNT=1
V13_FORM_DIRECTION=G_TO_P
V13_FORM_CHANNEL=EXISTING_AUTHENTICATED_GLOBAL_P_G_CONTROL
V13_FORM_ANCILLARY_ITEMS=0

D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
```

The global plus-three change is express and does not alter the exact 12/12/4
scoped enums.  `BOOTSTRAP_SEALED` is not counted in any of them.

### 7.4 Frozen prior closures and scientific/package vector

V13 retains without weakening:

1. v11's exact ACK bytes, P seal, owner-local X definitions, P full freeze,
   G READY emission freeze, one-use/replay rules, raw bitmap, and all
   clauses not expressly superseded by the ephemeral-validation and seal-
   send commit;
2. v10's nonzero cardinality, PID binder, monotone committed history,
   seventeen-label construction, and launcher exclusion;
3. v9's release payload, seven-item preimage, exact P/G/cgroup bindings,
   no retry/fallback/reuse, and fail-before-write intent;
4. base plus v1--v8, including v5's blocked/no-op provenance, all namespace,
   cgroup, private-mount, capability, FD, requester, quiescence, object,
   signal/crash, cleanup, foreign-preservation, and global-final clauses;
5. v4/v6's peer-oracle ABI, holder matrix, and no-fallback rules, with only
   the exact additive preflight subtest in Section 3.2; and
6. every prior closure not expressly superseded above.

The frozen package/scientific vector remains:

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

## 8. One amendment-v13 authoring attempt and external freeze

### 8.1 Required amendment contents

The sole v13 amendment must:

1. bind this gate's externally computed path/type/mode/nlink/line/byte/
   SHA-256 receipt;
2. bind the exact current review and all nested prefixes, the v12 BLOCKED
   gate and absent v12 amendment path, v11 gate/recovery/amendment,
   v10/v9/reopen chain, base plus v1--v8, both implementation gates, and the
   unchanged six-source quarantine;
3. state that all six named findings and `REVISE_C0_M1_m0` remain current
   at authoring start and after author-side completion;
4. reproduce the exact Section-3 platform invariant, preflight bytes/order,
   holder/lifetime/no-drain rules, `E_POSSESSION_UNAVAILABLE` behavior, and
   no-child/no-count/no-fallback ceiling;
5. reproduce the complete seal payload, field order, framing, direction,
   channel, cardinality, every identity/frame/digest join, both owner-freeze
   preimages, and the eight-item seal preimage without abbreviation;
6. expressly remove the stable v11 ACK_VALIDATED state and `AV`, make all
   parse/validation/staging private and unpublished, and prohibit any hidden
   replacement bit;
7. reproduce the sole-send linearization, precommit failure matrix, later P
   audit, no ACK-of-seal, no-backflow, and fail-before-write fence;
8. reproduce C13, every invariant, all 33 rows, exact lifecycle classes,
   monotone committed history, and tombstone retention;
9. preserve all seventeen raw predicates, declaration-order bitmap,
   separate winner permutation, all-loser retention, and totality;
10. freeze global plus-three, exact 12/12/4 counts, all scientific/package
    counts, and the eight-node/twelve-edge DAG; and
11. authorize nothing downstream and predict neither its own digest nor the
    independent verdict.

Omission, abbreviation, a second form, a shared carrier, a persistent AV,
an unverifiable sender-death assumption, or any weakened fence is outside
this gate.  The author then stops.

### 8.2 Exact path skip and external stable receipt

The only authorized amendment path is:

```text
notes/phase2_control_design_amendment_v13.md
```

The following path remains absent and forbidden:

```text
notes/phase2_control_design_amendment_v12.md
```

After the v13 author completes the sole file, an external coordinator
computes:

```text
path=notes/phase2_control_design_amendment_v13.md
type=regular
mode=<actual>
nlink=1
lines=<actual>
bytes=<actual>
sha256=<actual 64-lowercase-hex digest>
```

The coordinator re-hashes this gate and every Section-1 authority.  Any
drift, v12 amendment, extra amendment/design path, symlink, hardlink,
nonregular target, predicted digest, or post-receipt edit stops.  No review
begins on a partial, self-reported, or mutable amendment.

## 9. Sole fresh append-only review after stable v13

### 9.1 Exact prefix and independence

Only after the complete external v13 receipt may one fresh independent
reviewer append exactly one addendum to:

```text
notes/phase2_control_design_peer_review.md
```

The complete current review must remain the exact prefix:

```text
PRESERVED_PREFIX_LINES=5527
PRESERVED_PREFIX_BYTES=296651
PRESERVED_PREFIX_SHA256=0321b1234f7d931f0daefc6dec67bef322cf5324d04c7f120ac3d9442ed34a6c
PRESERVED_V11_INPUT_PREFIX_LINES=5080
PRESERVED_V11_INPUT_PREFIX_BYTES=270649
PRESERVED_V11_INPUT_PREFIX_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
PRESERVED_V10_INPUT_PREFIX_LINES=4634
PRESERVED_V10_INPUT_PREFIX_BYTES=245023
PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_V9_INPUT_PREFIX_LINES=4236
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_PASS_PREFIX_LINES=3961
PRESERVED_PASS_PREFIX_BYTES=209656
PRESERVED_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
```

The reviewer must be independent of this gate author, the v13 amendment
author, every source author, and prior verdicts.  The reviewer fresh-reads
and re-hashes the complete applicable ARS rules, this gate, v12, the complete
review prefix, v11/v10/v9/reopen governance, base plus active amendments
v1--v11 and v13, both historical implementation gates, and the then-current
six-path quarantine.  Source remains quarantine only.

The review is static exact-byte design review.  Its sole write is the one
append.  It may not edit a gate, amendment, source, implementation review,
proof, Route, manuscript, or another path; import/execute project code;
perform a platform preflight/probe; or create a generated/cache/temp/result/
lock/receipt/manifest file.

### 9.2 Exact active count-twelve successor block

The append preserves every historical block and adds one sole active block,
with the externally computed v13 digest and no blank/commentary line inside:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v11]
count=12
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829
10.path=notes/phase2_control_design_amendment_v10.md
10.sha256=d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f
11.path=notes/phase2_control_design_amendment_v11.md
11.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
12.path=notes/phase2_control_design_amendment_v13.md
12.sha256=<exact externally computed final v13 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

No entry for amendment v12 is legal.  The reviewer independently reads and
hashes all twelve listed files in order.

### 9.3 Mandatory hostile attacks and verdict

The reviewer must independently attack at least:

1. whether the exact AF_UNIX preflight genuinely establishes the required
   full-send/sole-last-close/exact-frame/EOF invariant without a new child,
   count, method, path, or fallback;
2. every global endpoint holder/lifetime/no-drain fact and the fixed pair of
   G crash before versus after the seal enqueue;
3. every seal field, frame/digest join, owner-freeze byte, item count,
   preimage, direction, cardinality, wrong-first, duplicate, and replay rule;
4. proof that ACK parse/validation/staging is wholly ephemeral and that no
   public `AV`, renamed validation bit, stable state, or tombstone fact
   survives;
5. proof that complete canonical seal send is one indivisible success/write
   release and that partial/errno/crash/timeout cannot authorize a write;
6. P's later exact audit, queued-frame-before-EOF behavior, mismatch
   handling, no seal ACK, and no infinite handshake;
7. all 33 C13 vectors, feasibility, mutual exclusion, completeness, unique
   success, monotone committed history, and exact failure tombstones;
8. all seventeen raw predicates, all mandated overlaps, every true losing
   bit, separate permutation, owner tie, and receipt immutability;
9. preservation of v11 ACK/P seal/X/freezes, v10 cardinality/PID binder,
   v9 form/preimage/fence, global plus-three, exact 12/12/4 enums, all
   base/v1--v8 closures, and v5 no-op; and
10. every frozen path, schema, row, method, generated member, authority
    binding, and eight-node/twelve-edge DAG coordinate.

Only a fresh evidence-backed `PASS_C0_M0_m0` on the complete tuple may close
`P15R-V11-M1`, then v10/v9/reopen findings.  Any critical, major, or minor
defect returns REVISE with its exact vector.  This gate predicts neither
outcome.

## 10. Mandatory successor source/implementation governance

Even a later zero-finding design PASS grants no source edit, source
acceptance, implementation review, platform preflight, execution, or
generated artifact.  Before any such action, a separate successor source/
implementation-governance gate must bind:

- this gate's final external receipt;
- v12's blocking receipt and the absent v12 amendment path;
- the externally frozen v13 amendment receipt;
- the complete append-only zero-finding review receipt;
- the exact base-plus-v1--v11-plus-v13 tuple;
- both historical implementation gates as nonrevived provenance; and
- the then-current six-path source tuple as quarantine.

That successor gate must separately decide source attempt, path, freeze,
static review, platform-preflight, and execution budgets.  In particular it
must prove or execute the Section-3 preflight only under newly granted
authority; this design gate does not run it.  Nothing is reserved here.

## 11. External freeze of this sole gate

After this file is complete, its author stops.  An external coordinator
computes and freezes:

```text
path=notes/phase2_control_design_remediation_gate_v13.md
type=regular
mode=<actual>
nlink=1
lines=<actual>
bytes=<actual>
sha256=<actual 64-lowercase-hex digest>
```

The coordinator re-hashes the complete current review and every prefix,
v12, v11 gate/recovery/amendment, v10/v9/reopen governance, base/v1--v8,
historical implementation gates, and six quarantined paths.  Any drift,
extra v13/v12 amendment/design path, symlink, hardlink, nonregular target,
predicted self-digest, or post-receipt edit stops.  This gate cannot contain
its own final digest without changing that digest.

The external receipt authenticates only this governance record.  It does
not create amendment, review, source, or execution authority beyond the
conditional one-attempt sequencing expressly stated here.

## 12. Authorization matrix and stop

```text
GATE_KIND=DESIGN_REMEDIATION_ONLY
GATE_VERDICT=PASS_TO_ONE_VERSIONED_DESIGN_AMENDMENT_V13_ONLY
CURRENT_REVIEW_VERDICT=REVISE_C0_M1_m0

P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN
P15R_V9_m1_STATUS=OPEN
P15R_V10_M1_STATUS=OPEN
P15R_V10_m1_STATUS=OPEN
P15R_V11_M1_STATUS=OPEN

V12_GATE_VERDICT=BLOCKED
AMENDMENT_V12_PATH_ABSENT=true
AMENDMENT_V12_WRITE_AUTHORIZED=false
AMENDMENT_V12_ATTEMPTS_AUTHORIZED=0

AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v13.md
AMENDMENT_V13_WRITE_AUTHORIZED=true
AMENDMENT_V13_ATTEMPTS_AUTHORIZED=1
OTHER_AMENDMENT_OR_DESIGN_PATH_AUTHORIZED=false
AUTHOR_SELF_CLOSURE_AUTHORIZED=false
REVIEW_VERDICT_PREJUDGED=false

AUTHORIZED_NEW_FORM=BOOTSTRAP_SEALED
AUTHORIZED_NEW_FORM_COUNT=1
AUTHORIZED_FORM_DIRECTION=G_TO_P
AUTHORIZED_FORM_CHANNEL=EXISTING_AUTHENTICATED_GLOBAL_P_G_CONTROL
AUTHORIZED_FORM_ANCILLARY_ITEMS=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
ACK_OF_SEAL_AUTHORIZED=false
ACK_OF_ACK_AUTHORIZED=false
RETRY_AUTHORIZED=false
FALLBACK_AUTHORIZED=false
RECONNECT_AUTHORIZED=false
RECORD_REUSE_AUTHORIZED=false
NEW_SHARED_PERSISTENCE_AUTHORIZED=false
BLOCK_IF_MORE_THAN_ONE_SEAL_FORM_REQUIRED=true

V11_STABLE_ACK_VALIDATED_STATE_SUPERSEDED=true
V11_AV_COORDINATE_SUPERSEDED=true
STABLE_ACK_VALIDATED_STATE_AUTHORIZED=false
HIDDEN_ACK_VALIDATED_BIT_AUTHORIZED=false
ACK_PARSE_VALIDATE_STAGE_EPHEMERAL=true
SS_REPLACES_AV=true
SS_AND_AV_COEXISTENCE_AUTHORIZED=false
COMPLETE_CANONICAL_SEAL_SEND_IS_SOLE_LINEARIZATION=true
FIRST_GOVERNED_WRITE_BEFORE_COMPLETE_SEAL_SEND_AUTHORIZED=false
P_SEAL_RECEIPT_IS_LATER_AUDIT_ONLY=true
P_SEAL_RECEIPT_REQUIRED_FOR_G_FIRST_WRITE=false
SUCCESS_FROM_SILENCE_AUTHORIZED=false
SUCCESS_FROM_ACK_COMPLETE_SEND_AUTHORIZED=false
SUCCESS_FROM_EOF_AUTHORIZED=false
QUEUE_STATE_INFERENCE_AUTHORIZED=false

AF_UNIX_QUEUE_RETENTION_PREFLIGHT_REQUIRED=true
AF_UNIX_PREFLIGHT_NEW_REGISTERED_CHILD_AUTHORIZED=false
AF_UNIX_PREFLIGHT_CHILD_COUNT_CHANGE_AUTHORIZED=false
AF_UNIX_PREFLIGHT_METHOD_COUNT_CHANGE_AUTHORIZED=false
AF_UNIX_PREFLIGHT_FALLBACK_AUTHORIZED=false
AF_UNIX_PREFLIGHT_FAILURE=E_POSSESSION_UNAVAILABLE
P_GLOBAL_ENDPOINT_RETAINED_THROUGH_SEAL_AUDIT=true
P_GLOBAL_ENDPOINT_ALTERNATE_READER_AUTHORIZED=false
G_GLOBAL_ENDPOINT_DUPLICATION_AFTER_FREEZE_AUTHORIZED=false

V13_VECTOR_COUNT=33
V13_FAILURE_VECTOR_COUNT=32
V13_SUCCESS_VECTOR_COUNT=1
RAW_CLASSIFIER_PREDICATE_COUNT=17
RAW_BITS_COMPUTED_BEFORE_WINNER=true
ALL_TRUE_LOSER_BITS_RETAINED=true

D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
CURRENT_EFFECTIVE_AMENDMENT_COUNT=11
SUCCESSOR_EFFECTIVE_AMENDMENT_COUNT_IF_VALID_V13=12
SUCCESSOR_ACTIVE_AMENDMENTS=v1-v11-plus-v13
SUCCESSOR_AMENDMENT_V12_SKIPPED=true

FRESH_APPEND_ONLY_REREVIEW_AUTHORIZED_ONLY_AFTER_V13_FREEZE=true
FRESH_APPEND_ONLY_REREVIEW_ATTEMPTS_AUTHORIZED=1
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
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

Final determination: **PASS TO ONE VERSIONED DESIGN AMENDMENT v13 ONLY**.
The one new authenticated G-to-P seal record is sufficient under the exact
receiver-queue, sole-holder, and preflight ceiling because a complete
canonical enqueue is both the success linearization and G-crash-surviving
evidence.  Private ACK validation/staging has no stable AV state; every
pre-send failure remains `SS=0`, and every complete canonical send is the
sole `SS=1` success.  P's later validation confirms but does not authorize
or acknowledge that boundary.  These bytes close no finding, accept no
source, revive no implementation authority, and authorize no execution,
precheck, generated artifact, proof, Route, manuscript, release, archive,
or Git action.  If the exact one-record or platform-preflight contract
cannot be met without another handshake/shared carrier or changed child/
count/path, the authorized amendment step is BLOCKED and stops.
