# Replacement Paper 15 control-design amendment v11

Status: AUTHOR-SIDE CANDIDATE COMPLETE — CURRENT REVIEW REMAINS REVISE C0/M1/m1  
Date: 2026-08-17 (Asia/Shanghai)  
Amendment class: exact-byte design-only repair; no implementation or execution  
Sole authoring gate: notes/phase2_control_design_remediation_gate_v11.md  
Sole new wire form: GUARDIAN_READY_ACK, P to G  
Current open findings: P15R-REOPEN-M1, P15R-V9-M1, P15R-V9-m1,
P15R-V10-M1, and P15R-V10-m1  
Source, review, gate, implementation, run, precheck, generated-artifact,
Route, manuscript, release, archive, and Git authority: none  
Universal prime recovery: OPEN_NOT_AUTHORIZED

## Material Passport

- Material type: one bounded author-side control-design amendment.
- Question: can the v10 positive-close and raw-bitmap defects be repaired by
  exactly one authenticated P-to-G ACK, without a second acknowledgment or a
  weakened pre-write fence?
- Determination: yes, within only the inherited authenticated, trusted,
  non-Byzantine P/G ceiling and ordered existing SOCK_SEQPACKET endpoint. G
  alone validates the ACK, owns the unique positive success seal, and owns
  the first governed-write authorization. P remains pending after its sole
  complete ACK send, so an ACK-of-ACK would add no prerequisite to G's first
  governed write.
- Scope: this amendment changes only the exact boundary protocol, lifecycle
  algebra, classifier construction, and fence clauses stated below.
- Finding posture: this author-side candidate closes, downgrades, predicts,
  or adjudicates no finding. REVISE_C0_M1_m1 and all five named findings
  remain current after author-side completion pending a fresh independent
  append-only review of the complete base-plus-v1-through-v11 tuple.
- Evidence ceiling: no claim of Byzantine-owner resistance, runtime or
  platform availability, source conformance, theorem recovery,
  reproducibility execution, or deterministic replay is made.

## 1. Exact authority, intake, and frozen byte state

### 1.1 Sole gate and absent target

The author freshly byte-read and re-hashed the complete sole gate immediately
before this write. Its stable authority receipt was:

| Field | Exact value |
|---|---|
| path | notes/phase2_control_design_remediation_gate_v11.md |
| type | regular |
| mode | 0644 |
| nlink | 1 |
| lines | 1221 |
| bytes | 54839 |
| SHA-256 | d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e |

At intake and at the immediate pre-write check,
notes/phase2_control_design_amendment_v11.md was absent. This path is the
sole write of this authoring step. No source, review, gate, implementation,
run, precheck, cache, temporary, lock, receipt, result, manifest, generated,
Route, manuscript, release, archive, or Git path was created or changed.

### 1.2 Applicable complete ARS rules

The complete applicable ARS-Codex 0.1.25 experiment, integrity,
reproducibility, review, and authoring rules were freshly read and re-hashed.
Their independent-oracle, evidence-gap, hostile-counterexample, exact-byte,
no-fabricated-evidence, fail-closed, reproducibility, and bounded-authoring
rules govern this amendment.

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
| academic-paper/WORKFLOW.md | 542 | 47450 | 41a20e2a343236fb21983030dcacdb1f8014dbf3fed3b1ec84a6b31f68ed49dd |
| draft_writer_agent.md | 656 | 52379 | 029d71add0836bc03a55d324098c8e2d55e242c48a2d39539d34ef8c84c331cf |
| study_manager_agent.md | 392 | 19231 | 0416767252da10adcb5c35c2fa2ccea905f51d39a24d4b296db270df72eaf635 |
| academic_writing_style.md | 188 | 7741 | b47ee76b9c7490f0a34c74e0340f643ed27959d140af24e1adcad21c20f6d05b |

This was a static design-authoring intake. No project path was imported,
sourced, compiled, parsed as project code, syntax-checked, or executed. No
platform probe, preflight, generator, verifier, unittest, wrapper,
reproduction, cache, temporary, lock, result, manifest, or generated member
was created or run.

### 1.3 Current review and exact nested prefixes

The complete current append-only review was freshly byte-read and re-hashed:

| Record | Lines | Bytes | SHA-256 | Current result |
|---|---:|---:|---|---|
| notes/phase2_control_design_peer_review.md | 5080 | 270649 | 764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07 | REVISE_C0_M1_m1 |

Its exact nested append boundaries remain:

    CURRENT_REVIEW_LINES=5080
    CURRENT_REVIEW_BYTES=270649
    CURRENT_REVIEW_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
    PRESERVED_V10_INPUT_PREFIX_LINES=4634
    PRESERVED_V10_INPUT_PREFIX_BYTES=245023
    PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
    PRESERVED_V9_INPUT_PREFIX_LINES=4236
    PRESERVED_V9_INPUT_PREFIX_BYTES=223999
    PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
    PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
    PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
    PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

The full 270,649-byte result supersedes the nested historical PASS as the
current adjudicative record. No prefix is rewritten, normalized, truncated,
or reclassified.

### 1.4 Complete design and governance chain

Every input below was completely byte-read and re-hashed. The v11 gate is
the sole authoring authority; every earlier gate is provenance only.

| Record | Lines | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| base design, notes/phase2_control_design_lock.md | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d | effective base |
| amendment v1 | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe | effective |
| amendment v2 | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea | effective |
| amendment v3 | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b | effective |
| amendment v4 | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 | effective |
| blocked/no-op amendment v5 | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 | provenance only; zero semantic delta |
| amendment v6 | 1498 | 80822 | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 | effective |
| amendment v7 | 1199 | 60145 | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 | effective |
| amendment v8 | 884 | 45610 | e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 | effective |
| amendment v9 | 870 | 40366 | 0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829 | effective |
| amendment v10 | 1133 | 50487 | d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f | effective under REVISE |
| design-reopen gate v1 | 434 | 21256 | 8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973 | reopen provenance |
| remediation gate v9 | 1060 | 48563 | c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90 | v9 authority provenance |
| remediation gate v10 | 1002 | 45658 | 48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5 | v10 authority provenance |
| remediation gate v11 | 1221 | 54839 | d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e | sole v11 authority |

The gate-start effective tuple is base plus v1 through v10, with v5 retained
as blocked/no-op provenance and zero semantic delta. The current effective
amendment count at authoring start is ten.

### 1.5 Historical implementation gates and six-path quarantine

The historical implementation gates were fully read and re-hashed:

| Historical nonauthorizing record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| notes/phase2_control_implementation_gate.md | 735 | 35164 | e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8 |
| notes/phase2_control_implementation_remediation_gate_v1.md | 660 | 32800 | 52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f |

Both are consumed provenance and remain nonauthorizing. Neither this
amendment nor a later design PASS revives either gate.

The six provisional source paths were byte-read only to freeze quarantine:

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
    SOURCE_USED_AS_DESIGN_AUTHORITY=false
    SOURCE_ACCEPTED_AS_IMPLEMENTATION_EVIDENCE=false

No source name, behavior, or apparent convention supplies design meaning.

## 2. Exact supersession and one-form budget

### 2.1 Sole semantic delta

The complete permitted wire and suffix-state delta is exactly:

    new global bootstrap P--G form, exactly one:
      GUARDIAN_READY_ACK

    new P suffix states:
      P_OLD_BOUNDARY_LEDGER_FROZEN
      GUARDIAN_READY_ACK_SENT_PENDING_G_SEAL

    new G suffix states:
      G_OLD_BOUNDARY_EMISSION_FROZEN
      GUARDIAN_READY_ACK_VALIDATED
      BOOTSTRAP_BOUNDARY_SUCCESS_SEALED

The state names, local ledgers, counter extension, seal digest, and tombstone
classes are operational and nonserialized except for the one ACK payload.
They add no second channel, descriptor, ancillary item, repository artifact,
log, schema field, manifest key, generated member, authority binding, DAG
node, or edge.

The old boundary form set remains exactly LAUNCHER_REAPED,
PRIVILEGE_DROP_RELEASE, and GUARDIAN_READY. The only new form is
GUARDIAN_READY_ACK on the existing authenticated global P--G control.
Together with v9's PRIVILEGE_DROP_RELEASE, the v2-derived global bootstrap
enum has exactly a plus-two delta.

### 2.2 One-ACK challenge and mandatory stop rule

A hostile one-ACK sufficiency challenge was resolved before authoring. Under
the exact trusted, authenticated, non-Byzantine P/G and ordered-record
ceiling, P never claims positive global success or governed-write authority;
P only binds and sends its frozen-ledger receipt, then remains pending. G
knows its own frozen ledger, independently validates P's exact ledger seal
and cross-owner joins, and alone seals success immediately before its first
governed write. Therefore a second form cannot add a missing prerequisite
at G. Exact one-ACK closure is sufficient and this amendment is not blocked.

No ACK-of-ACK, challenge, nonce exchange, retry, fallback, reconnect,
correction form, compatibility parse, alternate endpoint, new descriptor,
new syscall dependency, or third global bootstrap form is authorized. No
success may be inferred from silence, timeout, EOF, queue inspection, poll
readiness, scheduler order, or absence. If any clause below required a
second new form, this amendment would be BLOCKED and would stop rather than
invent one.

### 2.3 Exact finding scope

This amendment repairs only the candidate design clauses implicated by
P15R-V10-M1 and P15R-V10-m1 and the inherited entry/fence clauses necessary
to extend the boundary through ACK validation. It retains v10's monotone
history, corrected release cardinality, L/G PID binder, and already closed
rows, and retains v9's release bytes, seven-item preimage, and strict fence
intent. It supplies an author-side candidate only; all findings remain OPEN.
## 3. One-ACK sufficiency and exact positive cut

### 3.1 Frozen trust and transport ceiling

The sufficiency proof is limited to:

1. P and G are the already authenticated, trusted, non-Byzantine owners;
2. the global control remains the same connected `SOCK_SEQPACKET` endpoint;
3. a complete send enqueues one complete framed record, and records sent by
   one owner are received by the peer in that owner's send order;
4. wrong, partial, duplicate, replayed, reordered, extra, or post-freeze
   behavior is fail-closed; and
5. G alone owns the first positive bootstrap-success seal and the first
   governed-write authorization.

No claim extends to a Byzantine owner that lies about its local ledger,
continues sending after an irreversible freeze, or forges retained state.

### 3.2 Exact old-boundary scope and owner-local X bits

The old boundary form set is exactly:

```text
LAUNCHER_REAPED
PRIVILEGE_DROP_RELEASE
GUARDIAN_READY
```

`GUARDIAN_READY_ACK` is not an old form.  Each owner retains exact framed
bytes, operation result, direction, expected slot, and causal predecessor
for every emission or observation of an old form.

`X_P` and `X_G` are binary owner-local facts:

- `X_P=1` iff P's pre-freeze ledger contains an actual old-form emission or
  observation outside its sole authorized expected slot;
- `X_G=1` iff G's pre-success ledger contains either (a) an actual G
  old-form emission outside its sole authorized slot or (b) an actual old
  form from P observed outside P's sole authorized slot; and
- `X = X_P | X_G` is the only global X value.

An actual partial or complete frame/event sets the applicable owner bit.
Silence, timeout, EOF, crash, errno without bytes, poll readiness, inferred
queue state, or merely expected behavior does not set either bit.

### 3.3 G emission freeze

After G's sole authorized `GUARDIAN_READY` send returns the exact complete
framed length, and before G attempts any ACK receive or any lock/governed
write, G irreversibly freezes its old-form emission ledger in state
`G_OLD_BOUNDARY_EMISSION_FROZEN`.

The success-shaped G emission ledger contains exactly one complete READY
frame and no other old-boundary emission at or after the release transition.
G retains its prior exact release and launcher observations separately.  An
extra G old-form emission already present makes `X_G=1` and forbids success.

G's old-form observation ledger remains open only for the next expected ACK
slot.  If the next P-to-G record is an old form, ordering makes G observe it
before any later ACK from P; G sets `X_G=1`, seals failure, and performs no
second receive for correction.

### 3.4 P complete READY validation and freeze

P may freeze only after it has completely received, parsed, validated, and
G-identity-joined the sole exact READY.  It then verifies its local
expected-slot counts, requires `X_P=0`, and irreversibly freezes both its
old-form emission and observation ledgers in
`P_OLD_BOUNDARY_LEDGER_FROZEN`.

The success-shaped P ledgers are exact:

```text
P old-form emissions, in local causal order:
  one complete LAUNCHER_REAPED frame
  one complete PRIVILEGE_DROP_RELEASE frame

P old-form observations:
  one complete GUARDIAN_READY frame

all other old-form emission/observation counts:
  zero
```

Only after that freeze may P construct or attempt the ACK.  P performs one
ACK send attempt.  P never enters global success: a complete send enters
only `GUARDIAN_READY_ACK_SENT_PENDING_G_SEAL`, after which P waits.  P may
respond to a later valid downstream G record, but that record only carries
the fact of a seal G already owns; it cannot authorize G's first write or
participate in bootstrap closure.

### 3.5 G's unique positive success seal

G makes one receive in the ACK expected slot.  It validates the complete ACK
exactly as Section 5 requires, freezes its old-form observation ledger at
that receipt, requires `X_G=0`, reads the ACK's bound `X_P=0`, and computes:

```text
X = X_P | X_G = 0 | 0 = 0
```

Only complete ACK validation enters `GUARDIAN_READY_ACK_VALIDATED` and then
the one immutable `BOOTSTRAP_BOUNDARY_SUCCESS_SEALED` receipt.  G is the
sole owner of that transition.  No P-side success assertion, silence,
timeout, queue-empty check, or later message is part of the positive cut.

This closes the v10 two-implementation counterexample: an implementation
cannot seal on first READY receipt, and it cannot leave success open
indefinitely.  Every conforming implementation uses complete ACK validation
as the same finite positive cut.

### 3.6 Why no ACK-of-ACK is needed

P does not need to learn that G validated the ACK before G's first governed
write, because P does not own that authorization.  G knows its own frozen
READY emission ledger and `X_G`; same-direction ordering makes every earlier
P old form precede P's ACK at G; the ACK binds P's frozen ledgers and
`X_P=0`; and G itself validates the exact cross-owner frame joins.  Those
facts are complete at G without another message.

An ACK-of-ACK would inform P of an already sealed G fact but would not add a
prerequisite to G's first write.  It is therefore unnecessary and forbidden.

### 3.7 Post-freeze violations are not retroactive silence

Each local freeze is an irreversible positive state transition, not an
inference that no future frame exists.  Under the trusted-owner ceiling, a
conforming owner emits no old form after its freeze.

If an owner nevertheless attempts such an emission:

- the frozen ledger is never reopened or rewritten;
- if the peer observes the old form before ACK validation, the peer's still
  open observation bit becomes one and bootstrap fails;
- if it is ordered after the validated ACK, it is a later protocol
  violation and triggers inherited downstream containment; and
- it never retroactively changes the sealed bootstrap tuple, converts
  success to a pre-ACK tombstone, or supplies evidence that an earlier
  silence was clean.

## 4. Exact `GUARDIAN_READY_ACK` form

### 4.1 Canonical payload, framing, direction, and cardinality

The sole v11 payload is exactly one canonical ASCII payload without LF,
NUL, or trailing byte:

```text
GUARDIAN_READY_ACK session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC release_frame_sha256=LOWERHEX64 release_attestation_sha256=LOWERHEX64 ready_frame_sha256=LOWERHEX64 p_release_send_attempt_count=1 p_release_complete_send_count=1 p_ready_complete_receive_count=1 p_ready_validated_receive_count=1 x_p=0 p_seal_sha256=LOWERHEX64
```

Every field occurs exactly once and in exactly that order.  `DEC` and
`LOWERHEX64` retain the inherited canonical decimal and exact 64-lowercase-
hex grammar.  The record inherits the existing four-byte unsigned
big-endian payload-length prefix, 4096-byte ceiling, exact-length,
canonical-ASCII, authenticated-peer, complete-send/receive, and closed-state
rules.  It has zero ancillary items.

The ACK is P-to-G only.  P has one authorized send attempt after its freeze;
G has one authorized receive/validation slot after its emission freeze.  A
partial, malformed, wrong-first, duplicate, replayed, wrong-session,
wrong-identity, wrong-cgroup, wrong-digest, wrong-state, or wrong-direction
record terminalizes.  There is no retry, correction, reconnect, or fallback.

On a successful bootstrap the exact boundary traffic is:

```text
P -> G: LAUNCHER_REAPED                 exactly once
P -> G: PRIVILEGE_DROP_RELEASE          exactly once
G -> P: GUARDIAN_READY                  exactly once
P -> G: GUARDIAN_READY_ACK              exactly once
```

Failure cardinalities are the retained counter values in Section 6; a form
already attempted or completely sent is never rewritten to zero.

### 4.2 Exact identity and frame bindings

The first six ACK fields bind the same exact bootstrap/global session,
surviving G outer PID, literal inner PID 1, G starttime, and guardian
device/inode already bound by v9/v10.  The v10 L/G correction remains exact:

```text
LAUNCHER_REAPED.outer_pid == launcher_outer_pid
PID1_READY.outer_pid == g_outer_pid
GUARDIAN_READY.outer_pid == g_outer_pid
PRIVILEGE_DROP_RELEASE.g_outer_pid == g_outer_pid
GUARDIAN_READY_ACK.g_outer_pid == g_outer_pid
launcher_outer_pid != g_outer_pid
```

`launcher_outer_pid` remains excluded from v9's `binding_ascii` and exact
seven-item attestation preimage.  V11 changes no v9 preimage byte.

Define, only for the v11 ACK contract:

```text
FRAME(payload) = U32BE(byte_length(payload)) || payload
FRAME_SHA256(payload) = SHA256(FRAME(payload))
```

The release digest is over the exact framed
`PRIVILEGE_DROP_RELEASE` bytes sent by P and received by G.  The separate
`release_attestation_sha256` field repeats exactly the release payload's v9
attestation field.  The READY digest is over the exact framed
`GUARDIAN_READY` bytes sent by G and received by P.  Hashing a normalized
payload, parsed fields, Markdown, an inferred frame, or a prior session is
invalid.

### 4.3 Exact P local count fields

The four count fields are P's success projection and are literal one only
when the corresponding retained operation is complete:

1. `p_release_send_attempt_count=1` means P began the sole authorized
   release send;
2. `p_release_complete_send_count=1` means that send returned the exact
   complete framed length;
3. `p_ready_complete_receive_count=1` means P received the exact complete
   READY frame; and
4. `p_ready_validated_receive_count=1` means P parsed, validated, and joined
   that READY to the retained G identity.

`x_p=0` is legal in an ACK only after P freezes its exact old-form ledgers.
No boolean is inferred from time or absence.

## 5. Exact P seal, owner, one-use, and replay rules

### 5.1 Binary grammar and scoped ledger encoding

V11 reuses the already defined `U16BE`, `U32BE`, `U64BE`, and `ITEM`
encodings as mathematical byte functions but uses a new domain and does not
alter v9's preimage.  Define the ACK-seal ledger encoding:

```text
LEDGER(entries) = U32BE(entry_count) || entry[0] || ... || entry[n-1]

ENTRY(action,form,frame) =
  U16BE(action) || U16BE(form) || U64BE(byte_length(frame)) || frame

action:
  1 = EMIT
  2 = OBSERVE

form:
  1 = LAUNCHER_REAPED
  2 = PRIVILEGE_DROP_RELEASE
  3 = GUARDIAN_READY
```

No owner code is serialized in an entry because the item name and seal owner
fix P.  The entry order is P's local causal order.  Partial or failed events
cannot appear in a success-shaped seal ledger; they remain in the failure
tombstone with their exact operation receipts.

The P success ledgers are exactly:

```text
p_old_emit_ledger_binary = LEDGER(
  ENTRY(1,1,exact framed LAUNCHER_REAPED bytes),
  ENTRY(1,2,exact framed PRIVILEGE_DROP_RELEASE bytes)
)

p_old_observe_ledger_binary = LEDGER(
  ENTRY(2,3,exact framed GUARDIAN_READY bytes)
)
```

### 5.2 Exact seal preimage

The fixed ASCII values are:

```text
ack_binding_ascii =
session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC

p_counts_ascii =
p_release_send_attempt_count=1 p_release_complete_send_count=1 p_ready_complete_receive_count=1 p_ready_validated_receive_count=1 x_p=0

p_freeze_ascii =
owner=P old_form_emit_frozen=1 old_form_observe_frozen=1 state=P_OLD_BOUNDARY_LEDGER_FROZEN

p_owner_use_ascii =
owner=P one_use=1 entropy=NONE
```

Each displayed value is one ASCII line without LF, NUL, leading/trailing
space, or alternate spelling.  The complete P seal preimage is exactly:

```text
ASCII("P15R-GUARDIAN-READY-ACK-SEAL-v11") ||
U32BE(9) ||
ITEM(1,ack_binding_ascii) ||
ITEM(2,exact_release_frame_bytes) ||
ITEM(3,ASCII(release_attestation_sha256)) ||
ITEM(4,exact_ready_frame_bytes) ||
ITEM(5,p_counts_ascii) ||
ITEM(6,p_old_emit_ledger_binary) ||
ITEM(7,p_old_observe_ledger_binary) ||
ITEM(8,p_freeze_ascii) ||
ITEM(9,p_owner_use_ascii)
```

`p_seal_sha256` is SHA-256 of exactly that preimage, encoded as 64 lowercase
hex characters.  There is no random entropy, nonce, clock, PID alias,
separator, padding, native-endian field, omitted item, duplicated item,
reordered item, normalization, or trailing byte.  Session/G/cgroup identity
and the exact two cross-owner frame joins supply the replay boundary; the
digest is a receipt, not a secret or capability.

### 5.3 Mint, recomputation, one-use, and replay

Only P mints the seal, after the P freeze and canonical reparse of every ACK
field.  G independently reconstructs the same P success ledgers from the
exact launcher/release frames it received and exact READY frame it sent,
recomputes the nine-item preimage, and requires equality with the ACK's seal.

G accepts the ACK only in one-use state `ACK_UNSEEN` and changes that state
irreversibly to `ACK_CONSUMED` on the first complete ACK-slot observation,
whether valid or invalid.  A wrong first record fails; no corrected second
record is read.  A repeated same-session ACK is `DUPLICATE`; an ACK whose
session/G/cgroup/frame bindings belong to an earlier bootstrap is `REPLAY`.
Neither can validate.  No ACK or seal is recycled into another bootstrap.

## 6. Extended lifecycle algebra and all 33 feasible vectors

### 6.1 Exact extended tuple and v10 projection

The v11 tuple is, in this exact order:

```text
C11 = (SA,SC,VA,X_P,X_G,RA,RC,RV,AA,AC,AV)

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

X = X_P | X_G
C10 = (SA,SC,VA,X,RA,RC,RV)
```

Every coordinate is binary.  The v10 projection preserves every completed
release/READY predecessor and derives its scalar X from the two owner bits.

### 6.2 Complete invariants

```text
SC <= SA
VA <= SC
RA <= VA
RC <= RA
RV <= RC
AA <= RV
AC <= AA
AV <= AC

if VA == 0 then (RA,RC,RV,AA,AC,AV) == (0,0,0,0,0,0)
if RV == 0 then (AA,AC,AV) == (0,0,0)
if AA == 1 then X_P == 0 and P_OLD_BOUNDARY_LEDGER_FROZEN == true
if AV == 1 then X_P == 0 and X_G == 0
if AV == 1 then G_OLD_BOUNDARY_EMISSION_FROZEN == true
if X == 1 then bootstrap_outcome == FAILURE

bootstrap_outcome == SUCCESS iff
  C11 == (1,1,1,0,0,1,1,1,1,1,1)
  and both exact freeze receipts are retained
  and G owns BOOTSTRAP_BOUNDARY_SUCCESS_SEALED
```

The `11` local-X combination is feasible only when causally incomparable
owner-local offending facts belong to the same minimal sealed failure cut;
serial processing stops at the first offending observation.  Once P has
frozen with `X_P=0`, no ACK-stage vector with `X_P=1` is legal.  Complete ACK
validation admits no nonzero X bit.

### 6.3 Exhaustive vector table

The following table is complete.  Every row is mutually exclusive by its
exact eleven coordinates.  Every listed failure vector is operationally
feasible under its retained causal evidence; no omitted tuple satisfies the
prefix constraints.

| # | SA | SC | VA | X_P | X_G | RA | RC | RV | AA | AC | AV | Exact lifecycle class | Outcome |
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
| 31 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | `ACK_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 32 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | `ACK_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| 33 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | `BOOTSTRAP_BOUNDARY_SUCCESS` | SUCCESS |

There are exactly 32 failure vectors and one success vector.  Rows 1--24
retain v10's six incomplete release/READY prefixes while decomposing X by
owner.  Rows 26--28 retain v10's post-READY-extra class.  Rows 25 and 29--32
are the finite ACK extension.  Row 33 is the only success.

### 6.4 Monotone history and tombstones

Every transition is monotone.  A failure tombstone copies the complete C11
tuple, exact local ledgers, completed release/READY/ACK predecessors, frame
bytes/digests, operation receipts, identities, freeze receipts, and
classifier receipt.  It never resets a one to zero.

The existing nonserialized
`PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE` is extended by these exact
lifecycle classes; it is not a new wire form or file.  In particular:

```text
validated READY, then P fails before ACK attempt:
  retain (1,1,1,0,0,1,1,1,0,0,0)

validated READY, then actual old-form extra before ACK:
  retain one of rows 26--28; do not erase RV

ACK attempted but incomplete:
  retain row 29 or 30; AA remains 1

ACK completely sent but not validated:
  retain row 31 or 32; AC remains 1

ACK fully validated with both X bits zero:
  retain row 33 and G's immutable success seal
```

A later EOF, crash, cleanup, peer death, namespace teardown, or post-freeze
violation appends secondary evidence only.  It cannot erase a predecessor,
alter the frozen tuple, or flow backward across G's sealed success.

## 7. Total raw predicate bitmap for `P15R-V10-m1`

### 7.1 Exact raw-bit rule

For every terminal boundary failure, first seal the earliest causally closed
evidence cut under v10's six phases extended by:

```text
7 POST_READY_PRE_ACK
8 ACK_SEND
9 POST_ACK_SEND_PRE_VALIDATE
```

The phase uses retained send/receive, state, frame, validation, pidfd/reap,
deadline, and freeze receipts, never scheduler or wall-clock order.

On that sealed evidence, compute all seventeen raw predicates independently.
No raw predicate may mention priority, a higher-ranked label, exclusion of a
prior case, or the eventual winner:

1. `B[PARTIAL]` is true iff an authorized send or receive retains positive
   proper-prefix bytes, a short nonzero result, truncation, or an exact
   known-length frame that did not complete.
2. `B[DUPLICATE]` is true iff an actual complete observation is byte-
   identical to a current-bootstrap form whose first current-bootstrap
   predecessor is already retained.
3. `B[REPLAY]` is true iff an actual complete observation authenticates to a
   consumed earlier bootstrap, earlier boundary, or otherwise old one-use
   coordinate.
4. `B[WRONG_DIRECTION]` is true iff a recognizable form is emitted or
   observed from the owner opposite its sole authorized direction.
5. `B[REORDERED]` is true iff a recognizable form is emitted or observed
   without its required causal predecessor or with a skipped protocol edge.
6. `B[WRONG_STATE]` is true iff a recognizable form is emitted or observed
   while the exact current state has no expected slot for it.
7. `B[MALFORMED]` is true iff a complete observation fails framing, exact
   length, canonical ASCII, record name, field count/order, decimal/hex
   grammar, no-NUL/no-LF, or trailing-byte rules.
8. `B[WRONG_SESSION]` is true iff a canonical session field is parseable and
   differs from the retained bootstrap/global session.
9. `B[WRONG_G_IDENTITY]` is true iff canonical G PID/starttime/inner-PID or
   authenticated peer fields are parseable and differ from the retained G
   identity joins.
10. `B[WRONG_CGROUP]` is true iff canonical guardian device/inode fields are
    parseable and differ from the retained guardian identity or membership
    join.
11. `B[WRONG_ATTESTATION]` is true iff a canonical digest/seal field is
    parseable but its required preimage recomputation, frame binding, or
    retained digest equality fails.
12. `B[TRANSPORT_ERROR]` is true iff the exact operation returns a terminal
    transport error with no complete expected record.
13. `B[EOF]` is true iff the authenticated endpoint returns zero-byte EOF
    while an expected transition remains incomplete.
14. `B[P_CRASH]` is true iff retained pidfd/wait evidence proves P death in
    the sealed cut.
15. `B[G_CRASH]` is true iff retained pidfd/wait evidence proves G death in
    the sealed cut.
16. `B[TIMEOUT]` is true iff the exact inherited deadline event fires while
    the boundary transition remains incomplete.
17. `B[MISSING]` is true iff a required transition lacks a completed
    acceptance receipt at an inherited deterministic state checkpoint.

Field parseability is evidence-domain gating, not priority.  More than one
raw bit may be true.  For example EOF can coexist with PARTIAL, timeout with
MISSING, a wrong-direction early frame with REORDERED and WRONG_STATE, and a
duplicate with WRONG_STATE.

### 7.2 Immutable bitmap and separate winner permutation

Freeze every true raw bit into the immutable bitmap in the existing enum
declaration order:

```text
MISSING MALFORMED DUPLICATE REPLAY WRONG_SESSION WRONG_G_IDENTITY
WRONG_CGROUP WRONG_ATTESTATION WRONG_DIRECTION WRONG_STATE REORDERED
PARTIAL EOF TIMEOUT P_CRASH G_CRASH TRANSPORT_ERROR
```

The secondary-fact ledger may retain richer evidence, but it can never
substitute for or omit a true bitmap bit.

Only after all bits are frozen, select the first set bit under this separate
fixed permutation:

```text
PARTIAL > DUPLICATE > REPLAY > WRONG_DIRECTION > REORDERED > WRONG_STATE
> MALFORMED > WRONG_SESSION > WRONG_G_IDENTITY > WRONG_CGROUP
> WRONG_ATTESTATION > TRANSPORT_ERROR > EOF > P_CRASH > G_CRASH
> TIMEOUT > MISSING
```

All true losing bits remain set.  For an otherwise identical same-label
owner tie, primary owner is P before G; that owner rule does not alter bit
membership or label selection.  The phase, C11 tuple, complete bitmap,
winner, owner, evidence references, and first valid predecessor are immutable
after sealing.

### 7.3 Totality

Every failure has at least one raw bit: an actual frame yields a partial,
grammar, semantic, state, direction, order, duplicate, or replay fact; an
operation failure yields transport/EOF/crash/timeout evidence; and the
remaining deterministic absent transition yields MISSING.  The independent
bitmap is therefore total, the separate permutation has one winner, and
receipt bytes no longer depend on whether an implementation applies
precedence before or after recording losing facts.

## 8. Exact fail-before-write fence and preservation

### 8.1 Extended fence

The v9 fence is extended through complete ACK validation.  Before G enters
`BOOTSTRAP_BOUNDARY_SUCCESS_SEALED`, neither G nor any possible child may:

- create a lock candidate or `.owner`;
- enter `ACQUIRING`, call bind, or claim lock possession;
- create a generation root, method root, subject root, package copy, result,
  generated member, manifest member, or publication staging object;
- admit, start, or expose a subject, runner, wrapper, generator, verifier,
  test, mutation worker, replacement actor, holder, or contender;
- accept or execute a session, lock, root, spawn, audit, object, cleanup,
  exchange, foreign-audit, or other transaction operation; or
- perform any subject, package, result, lock, object, generation, manifest,
  or repository write.

The inherited setup/cgroup/private-mount exception remains setup and total
failure containment only.  It cannot be used for a governed object.
`GUARDIAN_READY`, release validation, P's ACK send, or P's pending state is
not lock-state authority.  Only G's validated ACK and success seal crosses
the fence.

The v2 sentence “Only GUARDIAN_READY may enter lock state” is superseded to
“Only BOOTSTRAP_BOUNDARY_SUCCESS_SEALED after GUARDIAN_READY_ACK validation
may enter lock state.”  The v2 P source-FD-close sentence is superseded only
as needed to move its post-READY action after P's ledger freeze and ACK send;
it creates no authorization at G.

### 8.2 Wire/form counts

```text
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_TWO
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=2
V9_NEW_WIRE_FORM=PRIVILEGE_DROP_RELEASE
V11_NEW_WIRE_FORM=GUARDIAN_READY_ACK
V11_NEW_WIRE_FORM_COUNT=1
THIRD_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
GUARDIAN_READY_ACK_IS_D_M1_FORM=false
GUARDIAN_READY_ACK_IS_D_M2_FORM=false
GUARDIAN_READY_ACK_IS_REQUESTER_FORM=false
```

The ACK is inserted immediately after `GUARDIAN_READY` in the v2-derived
global P--G closed enum and before every lock/child/object/transaction form.
The exact D-M1/D-M2 enums remain unchanged.

### 8.3 v9/v10 and base/v1--v10 preservation

V11 retains without weakening:

1. v9's exact `PRIVILEGE_DROP_RELEASE` payload, direction, framing,
   cardinality history, seven-item attestation preimage, raw-byte boundaries,
   trusted-P ceiling, causal two-branch join, no retry/fallback/reuse, and
   fail-before-write intent;
2. v10's corrected nonzero failure cardinalities, monotone predecessor
   history, L/G PID binder and preimage exclusion, causal phase discipline,
   seventeen-label set, and every vector prefix through RV=0;
3. v1 primitive-only causal controls and evidence ceiling;
4. v2 namespace/cgroup possession, atomic placement, private tmpfs, source
   capabilities, retained-capability cleanup, foreign preservation,
   signal/crash, and global-final semantics, subject only to this exact
   later success/fence cut;
5. v3 owner/admission/FDSET barriers, source/start joins, child/object
   registration and acknowledgments, member-ledger closure, and unexpected-
   object nondeletion;
6. v4 requester-direct FD 5, actual FD-4 join, audited admission, reciprocal
   Unix-diag ABI, and P-only peer-oracle preflight;
7. v5 blocked/no-op provenance and zero semantic delta;
8. v6 P-issued capabilities, D-M1/D-M2 evidence, native pidfds, proc
   identities, quiescence, snapshots, diagnostics, reverse unwind, EBADF,
   restoration, and ABA exclusions;
9. v7 commitment-only create, immutable first receive, wrong-first
   terminalization, active-cap ceilings, terminal observation, exact 12/12
   D-M1 forms, and partial/replay/tombstone rules;
10. v8 requester receipt, FD-4/FD-5 closure, exact reap, CHILD_REAPED/ACK,
    auth-reap reconciliation, live control through global FINAL, EXIT, G
    reap, populated-zero, and ordered cgroup removal; and
11. every v10 and earlier clause not expressly superseded in Sections 2--8.

No prior closure may be traded for the v11 repair.

### 8.4 Frozen scientific, package, count, and DAG vector

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

The graph remains nodes `A D R G I C M V`, chain edges `A->D->R->G->I->C->M->V`,
and the five additional edges `A->M`, `D->M`, `R->M`, `G->M`, and `I->M`.
V11 adds no path, schema, CSV, row, method, generated member, binding, node,
or edge.

## 9. Author-side completion, conditional count, and external freeze

### 9.1 Exact preservation receipt

This candidate preserves all base/v1-through-v10 provisions not expressly
superseded above, including v5's blocked/no-op status. It adds exactly one
effective amendment candidate and no implementation, schema, package,
scientific, count, or DAG change.

The count transition is conditional on an external stable receipt:

    CURRENT_EFFECTIVE_AMENDMENT_COUNT_AT_AUTHORING_START=10
    SUCCESSOR_EFFECTIVE_AMENDMENT_COUNT_IF_EXTERNALLY_FROZEN_VALID_V11=11
    BLOCKED_NO_OP_AMENDMENT_V5_RETAINED=true
    GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_TWO
    GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=2
    V11_NEW_WIRE_FORM_COUNT=1
    THIRD_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
    D_M1_FD5_FORM_COUNT=12
    D_M1_P_G_SESSION_FORM_COUNT=12
    D_M2_QUIESCENCE_FORM_COUNT=4

The exact active count-eleven tuple, if externally frozen and admitted for
review, consists in order of amendments v1 through v11. The first ten
digests are the frozen values in Section 1.4. The v11 digest is not stated,
predicted, or self-reported here; it must be computed externally from the
final stable regular file.

### 9.2 External stable receipt and independent review

After this sole file is written, the author stops. An external coordinator,
not this amendment, must determine and freeze:

    path=notes/phase2_control_design_amendment_v11.md
    type=regular
    mode=<actual>
    nlink=1
    lines=<actual>
    bytes=<actual>
    sha256=<externally computed actual 64-lowercase-hex digest>

Any input drift, extra design path, symlink, hardlink, nonregular target,
predicted digest, or post-receipt edit stops. Only after that stable receipt
may one fresh independent reviewer append one addendum to
notes/phase2_control_design_peer_review.md while retaining the exact
5080-line, 270649-byte, 764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
prefix and all nested prefixes in Section 1.3.

Only a fresh evidence-backed PASS_C0_M0_m0 on the complete base plus v1
through v11 tuple may close P15R-V10-M1, P15R-V10-m1, and then the inherited
v9/reopen findings. This amendment predicts no result. A later design PASS
still grants no source edit, implementation review, preflight, execution, or
generated artifact; a new successor implementation-governance gate is
mandatory.

### 9.3 Findings remain OPEN

At authoring start and after author-side completion the exact status is:

    CURRENT_REVIEW_VERDICT=REVISE_C0_M1_m1
    P15R_REOPEN_M1_STATUS=OPEN
    P15R_V9_M1_STATUS=OPEN
    P15R_V9_m1_STATUS=OPEN
    P15R_V10_M1_STATUS=OPEN
    P15R_V10_m1_STATUS=OPEN
    AUTHOR_SELF_CLOSURE_AUTHORIZED=false
    REVIEW_VERDICT_PREJUDGED=false

This candidate does not claim independent review, acceptance, source
conformance, runtime evidence, or scientific recovery.

## 10. Authorization matrix and stop

    AMENDMENT_KIND=DESIGN_REMEDIATION_ONLY
    AUTHORIZING_GATE=notes/phase2_control_design_remediation_gate_v11.md
    AUTHORIZING_GATE_SHA256=d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e
    AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v11.md
    AMENDMENT_V11_WRITE_CONSUMED=true
    OTHER_AMENDMENT_OR_DESIGN_PATH_AUTHORIZED=false

    AUTHORIZED_NEW_FORM=GUARDIAN_READY_ACK
    AUTHORIZED_NEW_FORM_COUNT=1
    AUTHORIZED_FORM_DIRECTION=P_TO_G
    AUTHORIZED_FORM_CHANNEL=EXISTING_AUTHENTICATED_GLOBAL_P_G_CONTROL
    AUTHORIZED_FORM_ANCILLARY_ITEMS=0
    ACK_OF_ACK_AUTHORIZED=false
    RETRY_AUTHORIZED=false
    FALLBACK_AUTHORIZED=false
    RECONNECT_AUTHORIZED=false
    RECORD_REUSE_AUTHORIZED=false
    BLOCK_IF_MORE_THAN_ONE_ACK_FORM_REQUIRED=true

    G_READY_EMISSION_FREEZE_AFTER_COMPLETE_SEND_REQUIRED=true
    G_READY_EMISSION_FREEZE_BEFORE_ACK_RECEIVE_REQUIRED=true
    P_FULL_FREEZE_AFTER_READY_VALIDATION_REQUIRED=true
    P_FULL_FREEZE_BEFORE_ACK_ATTEMPT_REQUIRED=true
    GLOBAL_X_EQUALS_XP_OR_XG=true
    G_OWNS_UNIQUE_SUCCESS_SEAL=true
    P_REMAINS_PENDING_AFTER_COMPLETE_ACK_SEND=true
    SUCCESS_FROM_SILENCE_AUTHORIZED=false
    FIRST_GOVERNED_WRITE_BEFORE_G_SEAL_AUTHORIZED=false

    EXTENDED_VECTOR_COUNT=33
    EXTENDED_FAILURE_VECTOR_COUNT=32
    EXTENDED_SUCCESS_VECTOR_COUNT=1
    RAW_CLASSIFIER_PREDICATE_COUNT=17
    RAW_BITS_COMPUTED_BEFORE_WINNER=true
    ALL_TRUE_LOSER_BITS_RETAINED=true

    CONTROL_SOURCE_EDIT_AUTHORIZED=false
    CONTROL_IMPLEMENTATION_AUTHORIZED=false
    INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
    PROJECT_CODE_IMPORT_AUTHORIZED=false
    PROJECT_CODE_EXECUTION_AUTHORIZED=false
    SHELL_SOURCE_AUTHORIZED=false
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

Final author-side determination: exactly one authenticated P-to-G
GUARDIAN_READY_ACK is sufficient under the frozen trusted-owner and ordered
endpoint ceiling because G alone owns the positive success cut. P remains
pending, G performs no governed write before full ACK validation and its
immutable success seal, no second handshake form is needed or authorized,
and every named finding remains OPEN pending fresh independent review.
