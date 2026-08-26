# Replacement Paper 15 control-design remediation gate v10

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v10 ONLY — CURRENT REVIEW REMAINS REVISE C0/M1/m1**  
Date: 2026-08-17 (Asia/Shanghai)  
Gate class: design-remediation governance; exact-byte static review only  
Sole authorized future write: `notes/phase2_control_design_amendment_v10.md`  
Current open findings: `P15R-REOPEN-M1`, `P15R-V9-M1`, `P15R-V9-m1`  
Source, implementation, execution, generated-artifact, Route, manuscript, release, archive, and Git authority: **none**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**

## Material Passport

- **Material type:** bounded design-remediation gate.
- **Question:** can the two exact v9 review findings be repaired without a
  second wire form, a changed seven-item attestation preimage, a weakened
  fail-before-write fence, or any downstream authority?
- **Determination:** yes, but only through the exact non-wire lifecycle,
  cardinality, classification, and identity-binding repair frozen below.
- **Current adjudicative evidence:** the complete 245,023-byte design review
  at SHA-256
  `baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c`.
- **Finding posture:** this gate does not close, downgrade, or pre-judge
  `P15R-REOPEN-M1`, `P15R-V9-M1`, or `P15R-V9-m1`.  All three remain OPEN
  until one later fresh independent append-only design re-review returns an
  evidence-backed zero-finding verdict.
- **Form budget:** the v9 `PRIVILEGE_DROP_RELEASE` remains the sole global
  bootstrap form added by the effective design chain.  Amendment v10 may add
  no record, field, descriptor, ancillary item, channel, preimage item, or
  serialized receipt.
- **Write posture:** this gate file is the sole repository write in this
  gate-authoring step.  The authorized amendment is a later, separate write.
- **Evidence ceiling:** trusted, non-Byzantine P and the exact inherited v9
  boundary.  Nothing here claims Byzantine-P resistance, platform success,
  source conformance, or theorem recovery.

## 1. Exact authority and current byte state

### 1.1 Applicable ARS rules were freshly read in full

Before this gate was written, the applicable complete ARS-Codex 0.1.25
academic-research-suite root and its experiment, code-runner, study-manager,
academic-paper-reviewer, methodology-reviewer, devil's-advocate,
integrity-verification, integrity-review, reproducibility-audit, and shared
artifact-reproducibility instructions were freshly read in full.  Their
independent-oracle, exact-byte provenance, no-fabricated-evidence,
fail-closed execution, reviewer-independence, and reproducibility rules govern
this gate.

This was a static design/governance read.  No project code was imported,
sourced, compiled, syntax-checked, parsed as an AST, or executed.  No platform
preflight, runtime probe, generator, verifier, unittest, wrapper, reproduction,
or generated-artifact operation occurred.

### 1.2 Current append-only review and nested prefixes

The complete current adjudicative review was freshly read and re-hashed:

| Record | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| `notes/phase2_control_design_peer_review.md` | 4634 | 245023 | `baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c` | MATCH |

Its two required historical prefixes were independently re-derived from the
current bytes:

```text
CURRENT_REVIEW_LINES=4634
CURRENT_REVIEW_BYTES=245023
CURRENT_REVIEW_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_V9_INPUT_PREFIX_LINES=4236
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_NESTED_PASS_PREFIX_LINES=3961
PRESERVED_NESTED_PASS_PREFIX_BYTES=209656
PRESERVED_NESTED_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
```

The 245,023-byte review supersedes the historical PASS as the current
adjudicative result.  Its exact verdict is `REVISE_C0_M1_m1`.  Historical
prefix text remains evidence and may not be rewritten, normalized, truncated,
or reclassified.

### 1.3 Exact design and governance chain

Every design/governance input below was freshly read in full and re-hashed
immediately before authoring:

| Record | Lines | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` | effective base |
| amendment v1 | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` | effective |
| amendment v2 | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` | effective |
| amendment v3 | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` | effective |
| amendment v4 | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` | effective |
| blocked/no-op amendment v5 | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` | provenance only; no semantic delta |
| amendment v6 | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` | effective |
| amendment v7 | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` | effective |
| amendment v8 | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` | effective |
| frozen amendment v9 | 870 | 40366 | `0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829` | effective, under REVISE |
| original design gate | 272 | 10820 | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | historical governance |
| design-reopen gate v1 | 434 | 21256 | `8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973` | reopen authority |
| remediation gate v9 | 1060 | 48563 | `c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90` | exact v9 authoring authority |

The active design tuple at gate start is base plus v1--v9, with v5 retained
as blocked/no-op provenance.  Its effective amendment count is nine.  This
gate is governance, not an amendment, and does not itself change that count.

### 1.4 Historical implementation gates do not authorize this repair

| Historical record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_implementation_gate.md` | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` |
| `notes/phase2_control_implementation_remediation_gate_v1.md` | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` |

They are provenance only here.  Neither is revived, amended, or made current
by this gate, the future amendment, or a later design PASS.  Any source work
after design closure requires a new successor implementation-governance gate
bound to the final reviewed base-plus-v1-through-v10 design tuple.

### 1.5 Six-path source quarantine

The six provisional implementation paths were freshly read in full and
re-hashed only to prove that the quarantine boundary had not drifted:

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

No source convention is used to fill a design gap.  In particular, source
names and behavior are not authority for the lifecycle algebra, first-cause
classifier, or L/G PID join below.

### 1.6 Start-state and sole-write receipt

At gate-authoring start,
`notes/phase2_control_design_remediation_gate_v10.md` did not exist.  No
amendment-v10 path, cache, temporary file, result, lock, receipt, manifest,
or generated artifact was created.  This gate path is the sole write.

## 2. Governance determination and exact supersession budget

### 2.1 Verdict and findings which remain open

This gate authorizes exactly one later attempt to write:

```text
notes/phase2_control_design_amendment_v10.md
```

The target may repair only:

1. `P15R-V9-M1`, by replacing v9's unqualified failure cardinality ZERO
   with the total binary lifecycle/cardinality algebra in Section 4;
2. `P15R-V9-m1`, by adding the total deterministic first-cause classifier
   and immutable nonserialized tombstone receipt in Section 5; and
3. the v9 identity sentence that equated the L-bearing
   `LAUNCHER_REAPED outer_pid` with G-bearing records, by applying the exact
   non-wire PID binder in Section 3.4.

The current review remains `REVISE_C0_M1_m1`.  The amendment author may not
claim reviewer independence, close a finding, downgrade severity, predict a
later verdict, or treat author-side consistency checks as acceptance.

### 2.2 Sole semantic delta

Amendment v10 may supersede only these v9 surfaces:

- the sentence in amendment-v9 Section 3.5 that says the release occurs zero
  times on every failure path;
- the matching v9-gate authorization value
  `AUTHORIZED_FORM_CARDINALITY_FAILURE=ZERO`;
- any v9 language that would erase a complete send, validation, READY send,
  or READY validation when a later boundary failure is retained;
- the absence of a deterministic precedence/tie-break rule for the exact
  seventeen existing nonserialized labels; and
- amendment-v9 Section 3.2 item 2 and related joins only to the extent they
  equate `LAUNCHER_REAPED outer_pid` with G's outer PID.

The supersession must be surgical.  Every omitted base/v1--v9 clause remains
binding.  V5 remains a blocked/no-op record.  No other identity, state,
message, counter, form, enum member, operation, path, package count, or
scientific ceiling changes.

### 2.3 No broader repair

The authorized repair may not add or change a wire payload, record name,
record field, framing byte, descriptor, ancillary item, channel, socket,
preimage item, preimage tag, digest domain, governed write, retry, fallback,
reconnect, compatibility parse, helper, method, detector, result, source
path, schema field, authority binding, generated byte, DAG node, DAG edge,
proof, Route, manuscript, or trust claim.

If the exact repair cannot be expressed with the existing v9 wire form,
seven-item preimage, retained in-memory facts, and fence, the amendment step
is **BLOCKED**.  The author must stop rather than invent another form or
broader relaxation.  A need for a second form is a new design finding, not
permission to spend another form.

## 3. Frozen v9 envelope and exact PID binder

### 3.1 Sole wire form remains byte-for-byte unchanged

The only v9-added bootstrap payload remains:

```text
PRIVILEGE_DROP_RELEASE session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC attestation_sha256=LOWERHEX64
```

It remains one canonical ASCII payload without LF, NUL, or trailing byte,
with fields exactly once and in that order.  It retains the inherited
four-byte unsigned big-endian payload length, 4096-byte ceiling, exact length,
canonical decimal and lowercase-hex grammar, authenticated P--G
`SOCK_SEQPACKET` endpoint, P-to-G direction, complete-send/receive rules,
closed-state rules, and zero ancillary items.

Amendment v10 adds no form.  It only makes the operational accounting of this
existing form and the inherited `GUARDIAN_READY` transition total.

### 3.2 Exact seven-item preimage remains byte-for-byte unchanged

The binary definitions remain:

```text
U16BE(n) = unsigned n encoded as exactly 2 big-endian bytes
U32BE(n) = unsigned n encoded as exactly 4 big-endian bytes
U64BE(n) = unsigned n encoded as exactly 8 big-endian bytes
ITEM(tag,value) = U16BE(tag) || U64BE(byte_length(value)) || value
```

The complete preimage remains exactly:

```text
ASCII("P15R-PRIVILEGE-DROP-ATTESTATION-v9") ||
U32BE(7) ||
ITEM(1,binding_ascii) ||
ITEM(2,probe_identity_ascii) ||
ITEM(3,denial_ledger_binary) ||
ITEM(4,probe_reap_ascii) ||
ITEM(5,status_raw) ||
ITEM(6,cgroup_raw) ||
ITEM(7,pass_vector_ascii)
```

`binding_ascii` remains exactly the first six release fields, without the
record name and digest:

```text
session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC
```

The exact v9 definitions of `probe_identity_ascii`,
`denial_ledger_binary`, `probe_reap_ascii`, `status_raw`, `cgroup_raw`, and
`pass_vector_ascii`, including all byte lengths, tags, order, raw-read
boundaries, natural final LF handling, no normalization, and predicate
requirements, remain binding without abbreviation or reinterpretation.

There is no eighth item, new tag, launcher field, counter field, classifier
field, receipt field, alternate digest domain, or trailing byte.

### 3.3 Exact causal fence remains unchanged

The release remains after complete `LAUNCHER_REAPED`, G local drop, and P's
independent complete attestation, and before any authorized
`GUARDIAN_READY` attempt.  G may enter
`PRIVILEGE_DROP_RELEASE_VALIDATED` only after complete exact record
validation.  Only that state permits the unique expected-slot READY send.

Before `PRIVILEGE_DROP_RELEASE_VALIDATED`, the exact v9 fence continues to
forbid every lock candidate or `.owner`, `ACQUIRING`, package-lock bind,
lock-possession claim, generation/method/subject root, package copy, result,
generated or manifest member, publication staging object, subject or worker
admission/start, session/root/spawn/audit/object/cleanup/exchange operation,
and every subject, package, result, lock, object, generation, manifest, or
repository write.  The inherited setup/cgroup/private-mount containment
exception remains setup and failure containment only.

No cardinality or classifier clause may weaken this fence.  A failure at the
release/READY boundary enters the existing
`PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE -> BOOTSTRAP_FAILED` path before a
prohibited write.

### 3.4 Exact L/G PID disambiguation

The existing records have two distinct outer-PID owners:

| Existing record or retained value | Exact semantic owner |
|---|---|
| P's clone3 result and launcher pidfd | L, named `launcher_outer_pid` in retained state |
| `LAUNCHER_REAPED outer_pid=DEC` | L; its wire field remains literally `outer_pid` |
| accepted guardian control peer, guardian pidfd, stable proc identity | G, named `g_outer_pid` |
| `PID1_READY outer_pid=DEC inner_pid=1` | G |
| `GUARDIAN_READY outer_pid=DEC inner_pid=1` | G |
| `PRIVILEGE_DROP_RELEASE ... g_outer_pid=DEC ...` | G |

The joins are therefore exact:

```text
LAUNCHER_REAPED.outer_pid == launcher_outer_pid
PID1_READY.outer_pid == g_outer_pid
GUARDIAN_READY.outer_pid == g_outer_pid
PRIVILEGE_DROP_RELEASE.g_outer_pid == g_outer_pid
launcher_outer_pid != g_outer_pid
```

L is the pidfd-reaped launcher predecessor; G is the surviving accepted
inner-PID-1 guardian.  The two values must never be equated, substituted, or
used as aliases.  The correction changes no wire spelling and adds no field.

Under the exact v9 schema, `launcher_outer_pid` is excluded as a named value
from `binding_ascii` and from the seven-item preimage.  It must not be added
to an item or digest.  It is separately retained as the authenticated,
pidfd-bound, exact-reap predecessor and copied into success history or the
failure tombstone.  Raw kernel bytes remain raw bytes under their existing
v9 definitions; an incidental decimal byte sequence in a raw item does not
create a launcher-PID binding.

Release validation requires both predecessor branches: the retained
launcher-reap fact for L and the independently retained G identity/drop fact.
Their distinct values strengthen the existing causal join without expanding
the payload or preimage.

## 4. Total lifecycle and cardinality algebra for `P15R-V9-M1`

### 4.1 Exact binary counters

Amendment v10 must define the boundary counter tuple, in this exact order:

```text
C = (SA, SC, VA, X, RA, RC, RV)

SA = send_attempt_count
SC = complete_send_count
VA = validated_accept_count
X  = extra_or_out_of_slot_observation_count
RA = ready_send_attempt_count
RC = ready_complete_send_count
RV = ready_validated_receive_count
```

Every coordinate is binary: it is exactly 0 or 1.

`SA`, `SC`, and `VA` count only the one authorized expected-slot
`PRIVILEGE_DROP_RELEASE` transition.  `RA`, `RC`, and `RV` count only the one
authorized expected-slot inherited `GUARDIAN_READY` transition.  They do not
count datagrams, receive attempts, attacker observations, retries, duplicate
records, replays, compatibility parses, or kernel-queued packets.  A second,
out-of-slot, wrong-direction, duplicate, or replayed boundary datagram never
increments any of those six counters to two.

The meanings are exact:

1. `SA=1` only when P begins its sole authorized release send attempt after
   every prerequisite and canonical reparse succeeds.
2. `SC=1` only when that exact attempt returns the complete exact framed
   byte length.  A zero, short, interrupted, errored, or ambiguous result
   leaves `SC=0`.
3. `VA=1` only when G completely receives and validates that exact expected
   release and enters `PRIVILEGE_DROP_RELEASE_VALIDATED`.
4. `RA=1` only when G, after `VA=1`, begins the sole authorized expected-slot
   READY send.
5. `RC=1` only when that READY send returns its exact complete framed length.
6. `RV=1` only when P completely receives, parses, validates, and joins that
   exact READY to retained G identity.
7. `X=1` only from retained evidence that one actual boundary frame was
   observed outside its one currently authorized expected slot.  This
   includes a second current-bootstrap record, same-bootstrap duplicate,
   cross-bootstrap replay, wrong-direction record, or reordered READY/release.
   A first invalid frame occupying the expected slot is not automatically an
   extra frame.  Timeout, silence, EOF, crash, errno, poll readiness, or an
   inferred queued packet can never set `X`.

The first actual out-of-slot frame sets `X:0 -> 1` and immediately
terminalizes the boundary.  No later frame is consumed for classification.
`X=1` is always failure.  It cannot coexist with a successful boundary
outcome, and it never erases or increments a valid predecessor.

### 4.2 Algebraic invariants

The complete constraints are:

```text
SA,SC,VA,X,RA,RC,RV in {0,1}
SC <= SA
VA <= SC
RC <= RA
RV <= RC
RA <= VA
if VA == 0 then (RA,RC,RV) == (0,0,0)
if X == 1 then boundary_outcome == FAILURE
if (SA,SC,VA,X,RA,RC,RV) == (1,1,1,0,1,1,1)
then boundary_outcome == SUCCESS
```

No retry, correction, fallback, or second expected slot exists.  Consequently
`(SA,SC,VA)` is one of `000`, `100`, `110`, `111`; the READY prefix is `000`
until `VA=1`, then one of `000`, `100`, `110`, `111`.

### 4.3 Exhaustive legal vectors and tombstone classes

The following table is exhaustive.  `x` means either 0 or 1, with `x=1`
legal only when the immutable cut contains the actual out-of-slot frame
evidence defined above.  Each row with outcome FAILURE is a subtype of the
existing nonserialized `PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE`, not a new
wire form or repository artifact.

| Release `(SA,SC,VA)` | `X` | READY `(RA,RC,RV)` | Exact class | Outcome |
|---|---:|---|---|---|
| `000` | `x` | `000` | `PRE_SEND_FAILURE` | FAILURE |
| `100` | `x` | `000` | `PARTIAL_SEND_FAILURE` | FAILURE |
| `110` | `x` | `000` | `POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| `111` | `x` | `000` | `POST_VALIDATE_PRE_READY_FAILURE` | FAILURE |
| `111` | `x` | `100` | `READY_PARTIAL_SEND_FAILURE` | FAILURE |
| `111` | `x` | `110` | `READY_POST_SEND_PRE_VALIDATE_FAILURE` | FAILURE |
| `111` | `1` | `111` | `POST_READY_BOUNDARY_EXTRA_FAILURE` | FAILURE |
| `111` | `0` | `111` | `BOOTSTRAP_BOUNDARY_SUCCESS` | SUCCESS |

Thus there are exactly thirteen legal failure vectors and one legal success
vector.  No other tuple is legal.  The table distinguishes, without erasure:

- failure before any release send attempt;
- partial/failed release send after the sole attempt begins;
- complete release send without validated acceptance;
- validated release followed by failure before READY attempt;
- partial READY send;
- complete READY send without P's validated receive;
- an actual extra/duplicate/replay at the boundary after all three READY
  coordinates have become one; and
- the sole exact success boundary.

READY fully validated with `X=0` is the bootstrap boundary success.  Any
ordinary transaction, method, cleanup, signal, or global-final failure after
that immutable success receipt belongs to its inherited downstream lifecycle;
it must not flow backward into a release tombstone or alter `C`.  The only
failure with `RV=1` is an actual extra/duplicate/replay whose retained receipt
belongs to the still-open boundary close and therefore sets `X=1` before the
boundary success receipt is sealed.

### 4.4 Monotone retained-history rule

Every transition is monotone.  A failure tombstone copies the entire prior
counter tuple and every completed predecessor receipt, then adds the failure
classification.  It never resets a one to zero.

In particular:

```text
complete release validation then G crash before READY:
  C retains (1,1,1,0,0,0,0)

complete release validation then partial READY send:
  C retains (1,1,1,0,1,0,0)

complete READY send then receive-side transport failure:
  C retains (1,1,1,0,1,1,0)

valid release predecessor then duplicate/replay before READY:
  C changes (1,1,1,0,0,0,0) -> (1,1,1,1,0,0,0)
  VA remains 1; no expected-slot counter becomes 2

fully validated READY plus boundary extra before success seal:
  C retains (1,1,1,1,1,1,1)
```

A duplicate or replay cannot erase, replace, reinterpret, or demote the first
valid predecessor.  It is never a second acceptance.  It sets only `X` among
the counters and retains the predecessor payload, digest, acceptance state,
and causal receipts verbatim.

The no-retry, no-fallback, no-reuse, fail-before-write, and inherited
containment rules remain exact.  Physical cleanup or later peer death cannot
turn a failure vector into success or a success boundary into release failure.

## 5. Deterministic total first-cause classifier for `P15R-V9-m1`

### 5.1 Causal phase sealing without scheduler time

The classifier operates only on the exact retained P/G boundary facts already
required by v7--v9.  It introduces no message, clock, shared file, log, or
serialized receipt.

First, each side freezes its already retained local operation result, bytes,
state predecessor, endpoint identity, pidfd/wait evidence, and deadline event.
The classification cut is the smallest causally closed set of those retained
facts that proves boundary failure.  Causal closure follows the existing
send/receive, validation, state-predecessor, pidfd/reap, and retained-receipt
joins.  It never uses wall-clock order, scheduler order, poll-list order,
filesystem time, process enumeration order, or the order in which cleanup
later happens.

The earliest failing lifecycle phase is the first applicable member of this
fixed order:

```text
1 PRE_SEND
2 RELEASE_SEND
3 POST_SEND_PRE_VALIDATE
4 POST_VALIDATE_PRE_READY
5 READY_SEND
6 POST_READY_BOUNDARY
```

Only evidence in that phase's causally closed cut generates primary
candidates.  A later EOF, cleanup failure, process death, or timeout is
secondary evidence and cannot replace an earlier sealed cause.  If P and G
provide causally incomparable failure receipts in the same phase, the full
candidate union is retained; the label precedence below is applied to that
union.  For an otherwise identical same-label owner tie, P precedes G solely
for the retained primary-owner coordinate.  The label itself is unchanged.

### 5.2 Exact seventeen-label decision tree

The enum remains exactly the existing seventeen labels; none is added,
removed, renamed, serialized, or made successful:

```text
MISSING MALFORMED DUPLICATE REPLAY WRONG_SESSION WRONG_G_IDENTITY
WRONG_CGROUP WRONG_ATTESTATION WRONG_DIRECTION WRONG_STATE REORDERED
PARTIAL EOF TIMEOUT P_CRASH G_CRASH TRANSPORT_ERROR
```

Within the sealed earliest phase, evaluate the following predicates in the
printed order and choose the first true label:

1. **PARTIAL** — an authorized send or receive has retained positive proper
   prefix bytes, a short nonzero result, truncation, or an exact known-length
   frame that did not complete.  This wins over simultaneous EOF, transport,
   or crash evidence.
2. **DUPLICATE** — the actual complete observation is a second/out-of-slot
   byte-identical current-bootstrap boundary record whose first
   current-bootstrap predecessor is already retained.  This sets `X=1` and
   wins over wrong state.
3. **REPLAY** — the actual complete observation authenticates as a consumed
   earlier-bootstrap, earlier-boundary, or otherwise old record and is not
   the same-current-bootstrap duplicate above.  This sets `X=1` and wins over
   wrong session.
4. **WRONG_DIRECTION** — a recognizable boundary form is observed from the
   endpoint owner opposite its one authorized direction, after excluding
   duplicate/replay.  This is an actual out-of-slot observation and sets
   `X=1`.
5. **REORDERED** — a recognizable form is observed before its required
   predecessor or skips the lifecycle order, after excluding the cases
   above.  Early READY is here and sets `X=1`.
6. **WRONG_STATE** — form, direction, and relative order are otherwise
   recognizable, but the exact current state has no legal expected slot for
   it.  An actual out-of-slot frame sets `X=1`.
7. **MALFORMED** — a complete observation fails inherited framing, exact
   length, canonical ASCII, no-NUL/no-LF, record name, field count/order,
   canonical decimal, or lowercase-hex grammar.  Semantic field comparisons
   are not attempted through a grammar failure.
8. **WRONG_SESSION** — the fully parsed canonical session differs from the
   retained bootstrap/global-control session.
9. **WRONG_G_IDENTITY** — session matches, but canonical G outer PID, inner
   PID 1, starttime, authenticated peer, pidfd, or stable proc join differs.
10. **WRONG_CGROUP** — session and G identity match, but guardian device/inode
    or the required retained membership join differs.
11. **WRONG_ATTESTATION** — all prior syntax and semantic bindings match, but
    P's pre-send recomputation, exact preimage/digest join, or G's retained
    exact digest validation fails.
12. **TRANSPORT_ERROR** — the exact operation returns a terminal transport
    error with no partial bytes and no higher-ranked record evidence.
13. **EOF** — the expected boundary record is absent and the authenticated
    endpoint returns clean zero-byte EOF with no partial bytes or higher
    evidence.
14. **P_CRASH** — retained pidfd/wait evidence proves P death in the sealed
    phase and no higher-ranked cause exists.
15. **G_CRASH** — retained pidfd/wait evidence proves G death in the sealed
    phase and no higher-ranked cause exists.
16. **TIMEOUT** — the exact inherited deadline event fires while the expected
    boundary transition is incomplete, with no higher-ranked evidence.
17. **MISSING** — at an inherited deterministic state checkpoint the required
    transition has no retained record or completion receipt, and none of the
    sixteen predicates above applies.

This is a total classifier: every terminal boundary failure has a nonempty
candidate set and exactly one primary label.  Unknown complete bytes fall
under `MALFORMED`; an explicit no-byte transport error falls under
`TRANSPORT_ERROR`; clean close falls under `EOF`; proved process death falls
under its crash label; deadline expiry falls under `TIMEOUT`; only the
remaining deterministic absence is `MISSING`.

### 5.3 Mandatory overlap examples

The amendment must reproduce these exact outcomes and add no alternate tie
break:

| Same sealed evidence contains | Primary label | Required retained secondary facts |
|---|---|---|
| positive proper prefix, then EOF/transport error/peer death | `PARTIAL` | EOF/error/crash retained secondary |
| byte-identical second current-bootstrap record in terminal/wrong state | `DUPLICATE` | `WRONG_STATE` candidate retained; `X=1`; predecessor preserved |
| earlier-bootstrap record with a mismatching current session | `REPLAY` | `WRONG_SESSION` candidate retained; `X=1` |
| READY before release validation while state is also wrong | `REORDERED` | `WRONG_STATE` candidate retained; `X=1` |
| recognizable form from the wrong owner and too early | `WRONG_DIRECTION` | `REORDERED` candidate retained; `X=1` |
| malformed/noncanonical digest syntax and apparent digest mismatch | `MALFORMED` | no semantic `WRONG_ATTESTATION` through failed grammar |
| canonical 64-lowercase-hex digest with wrong recomputation | `WRONG_ATTESTATION` | exact parsed fields retained |
| no-byte transport errno followed by later EOF | `TRANSPORT_ERROR` | later EOF secondary only |
| P and G death proved in the same earliest phase | `P_CRASH` | G death retained secondary |
| deadline and deterministic absence at the same cut | `TIMEOUT` | missing fact retained secondary |

### 5.4 Immutable nonserialized classification receipt

The existing failure tombstone must retain an immutable classification
receipt containing at least:

```text
boundary bootstrap/global session
owner set and primary owner
earliest failing lifecycle phase
exact causal predecessor state/receipt identities already retained
C=(SA,SC,VA,X,RA,RC,RV)
expected record/form/direction and exact current state
actual complete or partial byte length and SHA-256, or explicit NONE
send/receive return and errno, or explicit NONE
authenticated endpoint identity
pidfd/wait status evidence, or explicit NONE
deadline event/serial, or explicit NONE
candidate-label bitmap in the exact seventeen-label enum order
primary label selected by Section 5.2
first valid predecessor identity/digest, or explicit NONE
```

Once sealed, the phase, counter tuple, candidate bitmap, primary label,
primary owner, actual-byte receipt, and valid-predecessor reference are
immutable.  Later EOF, crash containment, cleanup, namespace destruction, or
global-final facts append only as secondary evidence.  They cannot reclassify
the cause, erase a valid predecessor, reset a counter, or turn failure into
success.

This receipt is operational, in-memory, and nonserialized.  It adds no wire
payload, field, preimage item, CSV column, manifest key, generated member,
authority binding, path, log, DAG node, or DAG edge.

## 6. Mandatory non-regression vector

### 6.1 Form and closed-enum counts

V10 authoring adds no form.  The inherited v9 scoped plus-one remains the
only global bootstrap form delta:

```text
GLOBAL_BOOTSTRAP_FORM_DELTA=PLUS_ONE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=1
V10_NEW_WIRE_FORM_COUNT=0
SECOND_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
PRIVILEGE_DROP_RELEASE_IS_D_M1_FORM=false
PRIVILEGE_DROP_RELEASE_IS_D_M2_FORM=false
PRIVILEGE_DROP_RELEASE_IS_REQUESTER_FORM=false
```

The exact seventeen failure labels remain operational and nonserialized.  The
counter tuple and tombstone classes are also operational and nonserialized;
they are not forms.

### 6.2 Base and v1--v9 preservation

Amendment v10 must retain without weakening:

1. v1 primitive-only causal controls and evidence ceiling;
2. v2 two-level namespace/cgroup possession, atomic placement, private
   tmpfs, source capabilities, retained-capability cleanup, foreign
   preservation, signal/crash, and global-final semantics, subject only to
   the exact L/G PID disambiguation above;
3. v3 six pre-suite rows, owner/admission/FDSET barriers, source/start joins,
   child/object registration, acknowledgments, member-ledger closure, and
   unexpected-object nondeletion;
4. v4 requester-direct FD 5, actual FD-4 join, audited admission, reciprocal
   Unix-diag ABI, and P-only peer-oracle preflight;
5. v5's blocked/no-op provenance and zero semantic delta;
6. v6 P-issued capabilities, exact D-M1/D-M2 evidence, native pidfds,
   stable proc identities, quiescence, snapshots, diagnostics, reverse
   unwind, EBADF, restoration, and ABA exclusions;
7. v7 commitment-only create, immutable first receive, wrong-first
   terminalization, evidence ceilings, terminal observation, exact 12/12
   D-M1 forms, and partial/replay/tombstone rules;
8. v8 post-finalization requester receipt, FD-4/FD-5 closure, exact reap,
   child-reap acknowledgment, auth-reap reconciliation, live control through
   global FINAL, validated EXIT, G reap, populated-zero, and ordered cgroup
   removal; and
9. v9's sole release form, exact seven-item preimage, causal two-branch join,
   trusted-P ceiling, fail-before-write fence, no retry/fallback/reuse,
   seventeen-label set, hostile pairs, and every clause not expressly
   superseded by Sections 2--5 of this gate.

No earlier closure may be traded to repair the two v9 findings.

### 6.3 Frozen scientific, package, count, and DAG vector

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

The current count remains:

```text
CURRENT_EFFECTIVE_AMENDMENT_COUNT=9
```

Only after a conforming v10 amendment is externally frozen does its exact
successor tuple have:

```text
SUCCESSOR_EFFECTIVE_AMENDMENT_COUNT=10
```

That governance count changes no implementation path, schema, header, row,
method, generated member, authority binding, node, or edge.

## 7. Amendment-v10 authoring and external freeze

### 7.1 Required amendment contents

The one v10 amendment must:

1. bind this gate's externally computed final SHA-256, line count, and byte
   count;
2. bind the exact current 245,023-byte review and both nested prefixes, v9
   gate, v9 amendment, reopen gate, base, v1--v8, both historical
   implementation gates, and unchanged six-source quarantine tuple;
3. state that `P15R-REOPEN-M1`, `P15R-V9-M1`, `P15R-V9-m1`, and
   `REVISE_C0_M1_m1` were open/current at authoring start;
4. reproduce the exact seven-counter definitions, invariants, exhaustive
   vector table, success boundary, failure tombstones, and monotone history
   rules without semantic abbreviation;
5. reproduce the phase sealing, full seventeen-label decision tree, overlap
   examples, and immutable receipt without using scheduler time;
6. reproduce the L/G PID table, exact joins, inequality, preimage exclusion,
   and separate launcher-predecessor retention;
7. reproduce the unchanged wire form, exact seven-item preimage, fence,
   global plus-one, 12/12/4 counts, base/v1--v9 preservation, package vector,
   and 8-node/12-edge DAG; and
8. authorize nothing downstream and predict neither its own digest nor the
   later independent verdict.

A paraphrase that omits a counter coordinate, legal vector, success boundary,
failure class, overlap rule, causal-cut rule, retained predecessor, PID owner,
preimage exclusion, fence clause, or preservation obligation is outside this
gate.

### 7.2 External stable receipt

After the sole amendment file is complete, its author stops.  An external
coordinator then computes:

```text
path=notes/phase2_control_design_amendment_v10.md
type=regular
mode=<actual>
nlink=1
lines=<actual>
bytes=<actual>
sha256=<actual 64-lowercase-hex digest>
```

The coordinator re-hashes this gate and every Section-1 input.  Any drift,
extra amendment/design path, symlink, hardlink, nonregular target, predicted
digest, or post-receipt edit stops.  No reviewer may begin from a partial,
self-reported, or mutable amendment receipt.

## 8. Sole fresh append-only design re-review after stable v10

### 8.1 Exact review boundary and independence

Only after the complete externally stable v10 receipt may one fresh
independent reviewer append exactly one addendum to:

```text
notes/phase2_control_design_peer_review.md
```

The complete current review must remain a byte-identical prefix:

```text
PRESERVED_PREFIX_LINES=4634
PRESERVED_PREFIX_BYTES=245023
PRESERVED_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_NESTED_PREFIX_LINES=4236
PRESERVED_NESTED_PREFIX_BYTES=223999
PRESERVED_NESTED_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_OLDER_NESTED_PREFIX_LINES=3961
PRESERVED_OLDER_NESTED_PREFIX_BYTES=209656
PRESERVED_OLDER_NESTED_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
```

The reviewer must be independent of this gate author, the v10 amendment
author, every source author, and prior review conclusions.  The reviewer must
fresh-read and re-hash the applicable complete ARS rules, this gate, reopen
gate, v9 gate, complete current review prefix, base plus v1--v10, both
historical implementation gates, and the quarantined source tuple.  Source
remains quarantine only.

The re-review is static exact-byte design review.  It may write only the one
review addendum.  It may not edit an amendment, gate, source, implementation
review, proof, Route, manuscript, or any other path; import or execute project
code; perform a platform probe; or create a generated, cache, temporary,
result, lock, receipt, or manifest file.

### 8.2 Exact active count-ten successor block

The append preserves every prior block and adds one sole active successor,
with the externally computed v10 digest and no blank/commentary line inside:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v9]
count=10
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
10.sha256=<exact externally computed final v10 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

The reviewer independently reads and hashes all ten amendment files in that
order.  The block adds no manifest key, authority binding, implementation
path, generated member, DAG node, or edge.

### 8.3 Mandatory independent attacks and verdict

The re-review must independently attack at least:

1. all fourteen algebraically legal vectors, the unique success vector, all
   thirteen failure vectors, and exclusion of every other tuple;
2. complete-send, accepted-predecessor, READY-partial, READY-complete, G-crash,
   transport-error, duplicate, replay, and post-READY-boundary schedules;
3. proof that X is actual-frame-only, binary, always failing, and never a
   second acceptance or a way to erase the first predecessor;
4. proof that a later ordinary transaction failure cannot flow backward
   across the sealed successful bootstrap boundary;
5. causal phase sealing from retained P/G receipts without scheduler or wall
   time;
6. every one of the seventeen labels, their printed decision order, all
   overlap examples, owner tie, and receipt immutability;
7. L=`launcher_outer_pid`, G=`g_outer_pid`, their inequality, every existing
   record join, launcher exclusion from the preimage, and separate retained
   launcher-reap evidence;
8. byte-for-byte preservation of the sole wire form, seven-item preimage,
   fail-before-write fence, trusted-P ceiling, no retry/fallback/reuse, global
   plus-one, 12/12/4 enums, and every base/v1--v9 closure; and
9. every frozen path, count, schema, row, method, generated member, authority
   binding, and 8-node/12-edge DAG coordinate.

Only a fresh evidence-backed `PASS_C0_M0_m0` on the complete base-plus-v1-
through-v10 tuple may close `P15R-V9-M1`, `P15R-V9-m1`, and then
`P15R-REOPEN-M1`.  Any critical, major, or minor defect returns REVISE with
the exact finding vector.  This gate predicts neither outcome.

## 9. Mandatory successor implementation governance

Even a later design PASS authorizes no source change, implementation review,
preflight, execution, or generated artifact.  Before any of those actions, a
new successor implementation-governance gate must bind:

- the final externally frozen v10 amendment receipt;
- the final append-only zero-finding design review receipt;
- the exact complete base-plus-v1-through-v10 tuple;
- both historical implementation gates as nonrevived provenance; and
- the then-current complete six-path source tuple as quarantine.

That successor gate, not this design gate or amendment, must decide whether
source editing or review is admissible.  Execution, preflight, generation,
and reproduction remain separate later authorities even after implementation
governance.

## 10. Authorization matrix and stop

```text
GATE_KIND=DESIGN_REMEDIATION_ONLY
CURRENT_REVIEW_VERDICT=REVISE_C0_M1_m1
P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN
P15R_V9_m1_STATUS=OPEN

AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v10.md
AMENDMENT_V10_WRITE_AUTHORIZED=true
AMENDMENT_ATTEMPTS_AUTHORIZED=1
OTHER_AMENDMENT_OR_DESIGN_PATH_AUTHORIZED=false

V10_NEW_WIRE_FORM_AUTHORIZED=false
AUTHORIZED_EXISTING_FORM=PRIVILEGE_DROP_RELEASE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=1
SECOND_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
WIRE_FIELD_CHANGE_AUTHORIZED=false
PREIMAGE_ITEM_CHANGE_AUTHORIZED=false
FENCE_WEAKENING_AUTHORIZED=false
FAILURE_CARDINALITY_ZERO_RETAINED=false
TOTAL_LIFECYCLE_CARDINALITY_ALGEBRA_REQUIRED=true
TOTAL_FIRST_CAUSE_CLASSIFIER_REQUIRED=true
PID_BINDER_DISAMBIGUATION_REQUIRED=true
RETRY_AUTHORIZED=false
FALLBACK_AUTHORIZED=false
RECONNECT_AUTHORIZED=false
RECORD_REUSE_AUTHORIZED=false

D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
CURRENT_EFFECTIVE_AMENDMENT_COUNT=9
SUCCESSOR_EFFECTIVE_AMENDMENT_COUNT_IF_VALID_V10=10
BLOCK_IF_SECOND_FORM_REQUIRED=true

FRESH_APPEND_ONLY_REREVIEW_AUTHORIZED_ONLY_AFTER_V10_FREEZE=true
FRESH_APPEND_ONLY_REREVIEW_ATTEMPTS_AUTHORIZED=1
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_PREFIX_REWRITE_AUTHORIZED=false
AUTHOR_SELF_CLOSURE_AUTHORIZED=false
REVIEW_VERDICT_PREJUDGED=false

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
```

Final determination: **PASS TO ONE VERSIONED DESIGN AMENDMENT v10 ONLY**.
This gate finds that the two review defects can be repaired inside the sole
existing v9 form: by total monotone lifecycle accounting, deterministic
first-cause classification, and exact L/G identity disambiguation.  It does
not close the findings, accept source, revive implementation authority, or
authorize any execution or downstream research action.  If amendment v10
cannot meet every frozen clause without a new form, the authorized step is
blocked and must stop.
