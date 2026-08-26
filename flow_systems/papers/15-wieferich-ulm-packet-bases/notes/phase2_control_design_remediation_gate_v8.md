# Replacement Paper 15 Phase-2 control-design remediation gate v8

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v8 — C0/M1/m0 OPEN**  
Version: P15R-CONTROL-DESIGN-REMEDIATION-GATE-v8.0  
Date: 2026-08-17 (Asia/Shanghai)

This is one narrow design-remediation authorization, not a finding closure.
The current independent review's sole Major finding, G-M1, remains OPEN.
The v7 create-capability, active-capability, and terminal-send joins remain
closed within their stated byte-bound trusted-G ceiling, and D-M2 remains
closed and frozen against regression.  This gate authorizes exactly one
design-only amendment and, only after that amendment is frozen and externally
hashed, one fresh independent append-only re-review.  It authorizes no
implementation, generator, verifier, test, wrapper, control execution,
reproduction run, Route, composition, manuscript, figure, release, archive,
Git action, or public synchronization.

## 1. Exact authority and retained independent verdict

The complete current bytes of all sixteen records below were freshly read
and independently re-hashed before this gate was written:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | notes/phase2_control_design_lock.md | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d |
| remediation gate v1 | notes/phase2_control_design_remediation_gate.md | 188 | 7023 | 98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16 |
| amendment v1 | notes/phase2_control_design_amendment_v1.md | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe |
| remediation gate v2 | notes/phase2_control_design_remediation_gate_v2.md | 405 | 20113 | 00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705 |
| amendment v2 | notes/phase2_control_design_amendment_v2.md | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea |
| remediation gate v3 | notes/phase2_control_design_remediation_gate_v3.md | 578 | 27299 | e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac |
| amendment v3 | notes/phase2_control_design_amendment_v3.md | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b |
| remediation gate v4 | notes/phase2_control_design_remediation_gate_v4.md | 645 | 30174 | df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647 |
| amendment v4 | notes/phase2_control_design_amendment_v4.md | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 |
| remediation gate v5 | notes/phase2_control_design_remediation_gate_v5.md | 839 | 41734 | 55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7 |
| blocked/no-op amendment v5 | notes/phase2_control_design_amendment_v5.md | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 |
| corrected remediation gate v6 | notes/phase2_control_design_remediation_gate_v6.md | 1252 | 62896 | a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00 |
| amendment v6 | notes/phase2_control_design_amendment_v6.md | 1498 | 80822 | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 |
| remediation gate v7 | notes/phase2_control_design_remediation_gate_v7.md | 776 | 38865 | a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576 |
| amendment v7 | notes/phase2_control_design_amendment_v7.md | 1199 | 60145 | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 |
| current append-only review | notes/phase2_control_design_peer_review.md | 3567 | 187634 | cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73 |

The corrected v6 gate retains its exact 58,261-byte / 1,140-line prefix at
SHA-256
81d5543fdd0acc72122cd9a2171a7354a7d51d7d4a2f2c8f6a78fb12b3af7dcc.
The review is one append-only byte string.  Its exact nested prefixes are:

| Prefix lines | Prefix bytes | SHA-256 |
|---:|---:|---|
| 3149 | 165177 | 075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c |
| 2746 | 143812 | 30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb |
| 2308 | 119250 | cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab |
| 1910 | 96524 | ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41 |
| 1524 | 74876 | ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725 |
| 1017 | 49358 | b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3 |
| 488 | 22894 | 3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec |

The current independent verdict is exactly **REVISE — C0/M1/m0**.  The
sole open finding is:

- G-M1: amendment v7 lets G enter final CLOSED and close the global P--G
  control connection after FINALIZED_ACK, although requester receipt,
  FD-5 EOF, requester exit/reap, and the inherited G-to-P CHILD_REAPED
  reconciliation necessarily occur later.

The review independently closed the v7 commitment-only create join,
wrong-first terminalization, active-cap evidence ceiling, direct terminal
observation/finalization join, and exact twelve-form enums.  It also retained
D-M2 and every earlier semantic, metadata, possession, descriptor,
object-ledger, effective-amendment, count, and DAG closure.  This gate does
not re-review, close, downgrade, or predict closure of G-M1.

The current review contains exactly six effective-amendment blocks.  The
historical v1 through v5 blocks and active v6 count-seven block are immutable
prefix authority.  The theorem owner remains the bare compact group B_p;
universal recovery remains OPEN_NOT_AUTHORIZED; Route B remains false.

## 2. Sole target, precedence, and exact supersession budget

The target was absent before this gate was created.  Exactly one new design
file may be created:

~~~text
notes/phase2_control_design_amendment_v8.md
~~~

After that file is frozen and externally hashed, the versioned chain is
exactly base + amendments v1--v4 + blocked/no-op v5 + v6 + v7 + v8.

Amendment v8 may supersede only these amendment-v7 surfaces:

1. Section 9.1's G transition from complete FINALIZED_ACK send directly to
   CLOSED_TOMBSTONE, replacing it only with the post-ACK states and ordering
   in Section 3 below;
2. Section 9.1's permission for orderly P--G control close after P validates
   FINALIZED_ACK and its categorical “no post-ACK P--G message” statement,
   replacing it only with “no post-ACK D-M1 session form” while retaining
   inherited global control records;
3. Sections 6.3, 9.1--9.2, and 10 only where their terminal path, EOF/crash
   boundary, duplicate row, or tombstone wording conflicts with the exact
   post-ACK receipt/EOF/reap/reconciliation path below; and
4. Section 13's review-node successor grammar, solely so the current active
   count-seven block becomes historical and one later active count-eight
   block ends at amendment v8.

The supersession is semantic and line-bounded.  It does not change any
pre-FINALIZED_ACK send, receive, capability, commitment, transcript, frame,
state, outcome, or failure fact.  In particular, a complete FINALIZE and a
complete FINALIZED_ACK remain immutable facts on every later branch; a later
error may not retroactively call either unsent.

No requester--P FD-5 form changes.  Its enum remains exactly twelve.  No
D-M1 P--G session form changes.  Its enum remains exactly twelve.
CHILD_REAPED is the inherited amendment-v2 global G-to-P control record

~~~text
CHILD_REAPED session=DEC child=DEC status=DEC
~~~

under the existing four-byte big-endian length, canonical-ASCII,
4096-byte, direction, credential, state, cardinality, and complete-send
contract.  It is explicitly outside the twelve D-M1 session forms and is
not a thirteenth form.  Its session field is the registered direct-child
session coordinate from the inherited child ledger, not an inferred alias
for the v7 opaque D-M1 auth-session coordinate; P joins the two only through
their already frozen child/auth mapping.

This gate neither adds nor suppresses amendment-v3 CHILD_REAPED_ACK.  Where
the inherited creator-ledger contract already requires that ACK, it retains
its old fields, applicability, and order before any P control close.  V8
does not generalize it to the terminal requester and does not use it as a
new D-M1 record.

Every omitted base/v1--v7 clause remains binding.  Blocked v5 remains a
no-op provenance member.  No optional form, compatibility parser, wildcard,
new target, method, path, detector, exit class, syscall, descriptor,
authority binding, graph item, Route, or fallback is authorized.

## 3. G-M1 minimum post-FINALIZED_ACK lifecycle contract

### 3.1 Authentication finalization is not global-control completion

Complete FINALIZED_ACK send finalizes the v7 D-M1 authentication transcript
only.  It does not reap the requester, reconcile the direct-child ledger,
close the global P--G connection, or prove P's later receipt/EOF path.

On the complete ACK send, G must enter exactly:

~~~text
FINALIZED_AWAITING_REAP
~~~

It must not enter final CLOSED_TOMBSTONE, close or half-close the P--G
control endpoint, discard the requester pidfd/identity/child ledger, discard
its waitid/reap authority, or treat later P--G EOF as already observed.
The control connection remains live for inherited global lifecycle records.

In FINALIZED_AWAITING_REAP, the D-M1 auth session is sealed.  No further
D-M1 success form is legal in either direction, and no FD-4/FD-5/requester
operation may mutate session, root, lock, object, result, or generated
state.  This sealing does not remove CHILD_REAPED or another independently
applicable inherited global control record from the full P--G enum.

### 3.2 Exact successful state paths

The affected suffixes must be exactly:

~~~text
P:
FINALIZE_SENT
  -> FINALIZED_ACKED
  -> TERMINAL_RECEIPT_SENT
  -> FD5_EOF_OBSERVED
  -> CHILD_REAPED_RECONCILED
  -> CLOSED_TOMBSTONE

G:
FINALIZE_RECEIVED
  -> FINALIZED_AWAITING_REAP
  -> REQUESTER_REAPED
  -> CHILD_REAPED_SENT
  -> CONTROL_EOF_OBSERVED
  -> CLOSED_TOMBSTONE

either side in any nonfinal suffix state
  -> POST_FINALIZE_FAILED
  -> FAILED_TOMBSTONE
~~~

These states are operational and nonserialized.  The sole successful order
is:

1. G completely sends the exact v7 FINALIZED_ACK, fixes that immutable
   transcript fact, and enters FINALIZED_AWAITING_REAP while retaining the
   global control endpoint and direct-child ledger.
2. P receives and validates that complete ACK and enters FINALIZED_ACKED.
   Only then does it attempt the exact v7 TERMINAL_RECEIPT once.  Only a
   complete FD-5 datagram-length send enters TERMINAL_RECEIPT_SENT.
3. The requester closes original FD 5 only after its retained v7 receipt
   condition.  P accepts FD-5 EOF only after the complete receipt send, with
   no open auth/audit/terminal frame, no queued extra datagram, the same
   registered endpoint identity, and no truncation or ancillary defect.
   That exact observation enters FD5_EOF_OBSERVED.  As in v7, this proves
   P's complete send plus later peer closure; it does not claim an
   independently observed application-level read.
4. The unchanged v7 FD-4 order remains mandatory: after the requester has
   completely received/validated the one terminal reply and sent the one
   TERMINAL_OBSERVED, it closes original FD 4 before exit; G drains and
   observes clean EOF, closes its peer, and removes both holder identities.
   No post-terminal FD-4 datagram is accepted.
5. The requester exits.  G performs the inherited waitid reap of that exact
   registered direct child, requires the retained pidfd/start-time/NSpid/
   cgroup/credential identity, exact expected exit status, process gone,
   empty post-reap descriptor set, clean FD-4 terminal state, and no
   duplicate reap.  Only that complete join enters REQUESTER_REAPED.
6. From REQUESTER_REAPED, G sends exactly one inherited CHILD_REAPED with
   the exact registered direct-child session, child, and status.  Only a
   complete framed-record send enters CHILD_REAPED_SENT.  There is no suffix
   retry, second record, alias, or D-M1 replacement.
7. P accepts that record only in FD5_EOF_OBSERVED for the one unreconciled
   registered child.  It independently joins its terminal/auth tuple,
   requester pidfd/start-time/NSpid/cgroup/credential identity, expected
   status, FD-5 EOF, FD-4 terminal ledger, no-open-frame condition, and the
   inherited process-gone/reap evidence.  It then performs the retained
   post-reap child-pidfd close/EBADF proof and retained FD-5 peer close/
   absence proof.  Only the complete join and proofs enter
   CHILD_REAPED_RECONCILED.
8. Only from CHILD_REAPED_RECONCILED may P enter CLOSED_TOMBSTONE and close
   its P--G control endpoint exactly once.  No success result may be exposed
   before the reconciliation and retained endpoint-absence proofs.
9. G may enter CONTROL_EOF_OBSERVED only after CHILD_REAPED_SENT and only
   on an orderly clean peer EOF with no incomplete length/payload, queued
   record, or prior post-finalization failure.  That observation permits
   G's local CLOSED_TOMBSTONE and its normal control-endpoint disposal.

G's local CONTROL_EOF_OBSERVED proves peer closure, not an independent
application-level proof that P parsed the preceding record.  Conversely,
P does not claim to observe G's later local CLOSED transition.  Neither
local state alone authorizes an overall result: every inherited final
guardian, cgroup, manifest, result, and lifecycle predicate remains
mandatory.

### 3.3 Closed post-finalization admission and duplicate handling

The amendment must freeze one closed post-finalization admission rule:

~~~text
allowed successful traffic after FINALIZED_ACK:
  P -> requester: the already defined TERMINAL_RECEIPT
  G -> P: the inherited CHILD_REAPED
  any independently applicable inherited global control acknowledgment

new D-M1 P--G session form:
  NONE

new requester--P FD-5 form:
  NONE

new requester--G FD-4 operation:
  NONE
~~~

The optional-looking third line is not a wildcard.  It means only a record
whose pre-v8 role-specific inherited contract already makes it mandatory;
v8 creates no applicability.  For the terminal requester path at issue, the
sole new-after-ACK P--G success traffic is the already inherited
CHILD_REAPED.

Any queued or later duplicate FD-5 TERMINAL_OBSERVED, other FD-5 auth/audit
datagram, FD-4 SESSION_CLOSE, capability-bearing operation, D-M1 P--G form,
CHILD_REAPED, or other record outside its exact inherited state guard is
terminal.  The side first observing it:

1. fixes the exact duplicate endpoint, frame hash, state, and order;
2. enters POST_FINALIZE_FAILED before any new operation or reply;
3. performs no second FINALIZE, FINALIZED_ACK, terminal reply, receipt,
   cleanup mutation, or D-M1 abort exchange;
4. retains already completed FINALIZE/ACK/receipt facts without rewriting
   history; and
5. uses only the still-live control/reap path or existing crash containment
   to make the child and descriptors terminal.

A failure-marked CHILD_REAPED may be consumed only as cleanup/reap evidence;
it cannot change the auth result back to success.  Clean EOF following a
duplicate does not erase the failure.

### 3.4 Total failure and tombstone table

The amendment must freeze at least this complete post-ACK table:

| First failing edge | Required result |
|---|---|
| FINALIZED_ACK incomplete, invalid, or mismatched | retained v7 pre-ACK failure; P sends no terminal receipt; no v8 success suffix begins |
| TERMINAL_RECEIPT incomplete, zero, short, errno, or ambiguous | P enters POST_FINALIZE_FAILED; no retry or suffix send; requester is contained; G remains live only for terminal reap/containment |
| requester FD-5 EOF before a complete receipt | failure, never FD5_EOF_OBSERVED and never P success |
| requester remains live without FD-5 EOF or exit | no progress and no timeout-derived success |
| queued/late extra FD-5 datagram | exact duplicate failure; prior FINALIZE/ACK/receipt facts stay true; no retroactive “send no FINALIZE” claim |
| queued/late extra FD-4 datagram or non-child operation | G performs no mutation/reply, enters failure, closes admission, and contains/reaps the requester |
| duplicate/late D-M1 P--G form | receiving side fails; no thirteenth form, compatibility action, or abort retry is generated |
| requester exit status mismatch, PID/start-time drift, waitid error, wrong child, duplicate reap, process still present, or nonempty post-reap descriptor state | G cannot enter REQUESTER_REAPED or send a successful CHILD_REAPED; retained containment only |
| G crash or P observes P--G EOF before complete CHILD_REAPED | P enters failure, invokes retained cgroup kill/reap/populated-zero and guardian containment, and emits no successful close or ABSENT |
| P crash or G observes P--G EOF before complete CHILD_REAPED send | G enters failure, closes admission, locally kills/reaps what remains, performs no pathname deletion by reason of EOF, and cannot claim overall success |
| CHILD_REAPED send is zero, short, partial, errno, or ambiguous | G enters failure, never retries a suffix or second record, closes/contains control; P treats any partial frame or EOF as failure |
| CHILD_REAPED missing, malformed, duplicate, wrong-session, wrong-child, wrong-status, premature, or cross-bound | P enters failure; it cannot reconcile or enter successful CLOSED |
| P control close/EOF before CHILD_REAPED_RECONCILED | P cannot claim success; if G has not completed CHILD_REAPED it is a G failure; no EOF receipt synthesis |
| G clean EOF after complete CHILD_REAPED but P crashed before publishing any final result | G may finish local resource closure only; the missing P-owned result/guardian predicates forbid overall PASS |
| G crash after complete CHILD_REAPED but before local EOF observation | surviving P retains the exact record and crash fact; existing guardian teardown decides failure, never a synthesized G local success |
| close, endpoint-absence, pidfd-absence, or inherited final-ledger proof fails | failure tombstone and existing containment; no PASS, successful CLOSED, or false ABSENT |

Every send remains one attempt and succeeds only at the complete required
length.  There is no suffix retry.  A live but silent peer causes
nonprogress, not invented timeout success.  A physical cleanup that already
completed does not convert an auth/control failure into successful CLOSED.
No failure authorizes deletion of a foreign replacement or an unregistered
object.

Each post-finalization live and terminal ledger must retain at least:

~~~text
auth/session/request/close tuple
registered direct-child session/child/status tuple
requester endpoint, pidfd, start-time, NSpid, credentials, and cgroup
FINALIZE and FINALIZED_ACK exact bytes/hashes and complete-send facts
TERMINAL_RECEIPT exact bytes/hash and send result
FD4 and FD5 EOF/open-frame/duplicate observations
waitid result, process-gone and descriptor-empty observations
CHILD_REAPED exact bytes/hash and complete-send result
P--G EOF/close stage and first terminal cause
all v7 raw-value digests, commitments, reply bytes, and inherited OUTCOME
~~~

Live and failed tombstones are never recycled.  EOF, process death,
duplicate drain, or G local close never erases the first failure or upgrades
the inherited OUTCOME.  ABSENT remains legal only under its complete
preexisting owned-object-gone and foreign-preservation proof.

### 3.5 Mandatory hostile pairs

The later independent reviewer must be able to distinguish at least:

1. G retaining control in FINALIZED_AWAITING_REAP versus closing it
   immediately after FINALIZED_ACK;
2. the same finalized auth transcript with and without a later exact
   CHILD_REAPED record;
3. clean FD-5 EOF versus one queued duplicate TERMINAL_OBSERVED before EOF;
4. exact requester exit/reap/status versus a crash, wrong status, wrong
   child, duplicate reap, or still-live process;
5. complete CHILD_REAPED send versus partial/error send followed by EOF;
6. P control close after reconciliation versus EOF before reconciliation;
7. G local EOF closure after CHILD_REAPED versus a post-ACK crash before
   reap; and
8. an already finalized but later failed auth/control lifecycle versus a
   successful CLOSED result.

The required predicate must differ in each pair without adding a frame,
treating EOF as a missing receipt, trusting a copied success flag, erasing an
already-sent fact, or promoting local G closure to a P-observed result.

## 4. Exact preservation of v7, D-M2, and all prior closures

Amendment v8 must retain without weakening:

1. the v7 create commitment/template, non-disclosure, exact immutable first
   FD-4 receive-buffer provenance, raw-cap/frame P comparison, wrong-first
   consumption, trusted-byte-bound/non-Byzantine evidence ceiling, and all
   create abort/tombstone rules;
2. the v7 active commitment, first legal raw use before mutation,
   session-scoped capability, and explicit prohibition on per-operation
   requester-provenance overclaim;
3. the v7 fourth terminal capability, exact terminal frame, direct
   same-buffer FD-5 TERMINAL_OBSERVED, G full-send flag, FINALIZE/ACK join,
   exact twelve FD-5 forms, exact twelve D-M1 P--G forms, and no receipt-read
   claim;
4. D-M2's native x86_64 syscalls 434/438 with flags zero and runtime
   permission; exact slot/kind rows; pidfd/proc identity and lifetime;
   quiesce; two snapshots; every actual duplicate/fstat/proc/reciprocal-diag
   comparison; common reverse unwind; immediate EBADF; restored holders; and
   both ABA exclusions;
5. C-M1/C-M2's child-unique P-created FD 5, requester-direct child request,
   actual FD-4 byte join, audited child admission, and exact reciprocal
   Unix-diag ABI with no fallback;
6. B-M1..B-M3's six pre-suite rows, closed owner/admission grammar and
   173-method boundary; phase-indexed FD sets/barriers/lifetimes; and
   pre-access/post-creator object registration, ACK, ledger, P25-zero, and
   unexpected-object nondeletion rules;
7. A-M1's unparameterized SG_SCOPE, primitive-only evidence-class
   recomputation, post-recomputation expected class, and four primitive
   counterfactuals;
8. A-M2's recursive real-filesystem receipts, valid/malformed roots, five
   live falsifiers, and exact-one-coordinate mode/mtime probes without ctime
   masking;
9. A-M3's private namespace/cgroup possession, retained parent/root/lock
   capabilities, capability-relative cleanup, replacement fixtures, foreign
   preservation, and no false ABSENT;
10. A-M4's manifest-first complete-review authentication, unique ordered
    effective-amendment blocks, independent capability-relative amendment
    reads/hashes, and dereference before lifecycle adjacency; and
11. blocked v5's no-op provenance and every prior clause not expressly
    superseded in Section 2.

A v8 clause that weakens any item creates a new open finding.  It cannot
trade a prior closure for G-M1 or declare a conditional PASS.

## 5. Frozen schemas, paths, counts, and DAG

The exact invariant vector remains:

~~~text
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
~~~

All six implementation paths, eight CSV paths and literal headers, 120 rows
and order, 35 explicit negatives, 35 semantic methods, 28 package methods,
173 method names, nine generated paths, fourteen authority paths, manifest
keys/schema, and graph A,D,R,G,I,C,M,V with twelve distinct edges remain
unchanged.  V8 states, ledgers, EOF facts, and inherited reap reconciliation
are operational, in-memory, and nonserialized.

If the repair requires a thirteenth form, new syscall/FD/channel, changed
CSV/schema/generated byte, seventh implementation path, new method/target/
mutation/detector/exit, authority binding, manifest node/edge, theorem
owner, Route, or publication surface, amendment v8 must stop and record a
new design finding rather than silently widen this gate.

## 6. Append-only count-eight successor

After amendment v8 is frozen and externally hashed, the fresh independent
reviewer must preserve all six existing blocks and append exactly one sole
active successor, with no blank or commentary line inside it:

~~~text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v7]
count=8
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
8.sha256=<exact externally computed final v8 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
~~~

The final verifier must authenticate the complete post-v8 review through
the manifest-bound review FD before parsing, require exactly one
byte-identical historical block for each version v1 through v6, exactly one
active v7 count-eight block above, and no other begin/end tag.  It rejects
missing, duplicate, reordered, nested, malformed, prefix-drifted, wrong-
version/count/index/path/digest, extra-key, blank, or commentary-bearing
blocks.

It then independently capability-opens amendments v1 through v8 in active
order beneath the same held package-root FD with the retained beneath/no-
link rules, reads every byte, and recomputes all eight hashes.  Only after
every match may it set
R.effective_amendments=[v1,v2,v3,v4,v5,v6,v7,v8] before lifecycle
adjacency.  This changes no manifest key, authority binding, artifact,
graph node, edge, self-hash, future-result edge, or proof cycle.

## 7. Sole later fresh independent re-review

Only after amendment v8 is frozen and externally hashed may one fresh
independent reviewer append to:

~~~text
notes/phase2_control_design_peer_review.md
~~~

The current 187,634-byte / 3,567-line file at SHA-256
cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73
must remain its exact prefix, preserving every nested prefix and all six
existing effective-amendment blocks.

The reviewer must independently read and hash the complete base + v1--v8
tuple and attack, rather than restate:

1. FINALIZED_ACK as D-M1 finalization but not global-control completion;
2. exact G/P suffix states and the requirement that G retain its control,
   requester identity, pidfd/ledger, FD-4 closure evidence, and reap
   authority through CHILD_REAPED;
3. exact FD-5 receipt/clean-EOF and FD-4 close/drain/EOF joins before
   requester exit and reap;
4. CHILD_REAPED's inherited bytes, direct-child versus auth-session
   coordinate join, direction, cardinality, complete send, P reconciliation,
   pidfd/peer close proofs, and its explicit exclusion from the twelve D-M1
   forms;
5. queued duplicate FD-5/FD-4/P--G records, partial CHILD_REAPED, post-ACK
   P/G/requester crash or EOF, wrong exit/reap, live silence, and every
   successful and failed tombstone;
6. the evidence ceiling on G's final EOF state and the prohibition on
   promoting local close, EOF, or already-completed ACK into a missing
   receipt or overall PASS;
7. regression of every v7 create/active/terminal join, D-M2 clause, prior
   closure, count, schema, path, authority, and DAG invariant; and
8. six immutable historical blocks, one active count-eight block, eight
   independent amendment reads/hashes, fourteen bindings, and unchanged
   eight-node/twelve-edge DAG.

The reviewer may close G-M1 only from its own evidence.  This gate does not
predict that result.  Only a later independent PASS C0/M0/m0 could support
consideration of a separate implementation gate.

## 8. Authorization matrix

~~~text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V8=PASS_TO_ONE_AMENDMENT_V8
CURRENT_OPEN_FINDINGS=C0_M1_m0
G_M1_STATUS=OPEN
D_M2_STATUS=CLOSED_FROZEN_NO_REGRESSION
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v8.md
AMENDMENT_V8_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V8_FROZEN_AND_EXTERNALLY_HASHED=true
CURRENT_REVIEW_PREFIX_SHA256=cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73
CURRENT_REVIEW_PREFIX_LINES=3567
CURRENT_REVIEW_PREFIX_BYTES=187634

V8_SCOPE=POST_FINALIZED_ACK_GLOBAL_CONTROL_AND_REAP_ONLY
FINALIZED_ACK_CLOSES_D_M1_AUTH=true
FINALIZED_ACK_CLOSES_GLOBAL_P_G_CONTROL=false
G_POST_ACK_STATE=FINALIZED_AWAITING_REAP
G_CONTROL_RETAINED_THROUGH_CHILD_REAPED=true
INHERITED_CHILD_REAPED_REQUIRED=true
CHILD_REAPED_IS_D_M1_SESSION_FORM=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M1_THIRTEENTH_FORM_AUTHORIZED=false
POST_ACK_D_M1_SESSION_FORM_AUTHORIZED=false
P_SUCCESS_BEFORE_CHILD_REAPED_RECONCILIATION=false
G_LOCAL_CLOSED_BEFORE_CONTROL_EOF=false
EOF_SYNTHESIZES_RECEIPT=false
POST_ACK_DUPLICATE_RETROACTIVELY_UNSENDS_FINALIZE_OR_ACK=false
POST_ACK_CRASH_OR_PARTIAL_REAP_CAN_YIELD_SUCCESS=false

V7_CREATE_JOIN_RETAINED=true
V7_ACTIVE_EVIDENCE_CEILING_RETAINED=true
V7_TERMINAL_DIRECT_JOIN_RETAINED=true
D_M2_CLOSURE_RETAINED=true
ALL_PRIOR_CLOSURES_MUST_NOT_REGRESS=true

BASE_COUNTS_MUST_REMAIN_UNCHANGED=true
SIX_IMPLEMENTATION_PATHS_MUST_REMAIN_UNCHANGED=true
EIGHT_CSV_PATHS_MUST_REMAIN_UNCHANGED=true
MANIFEST_SCHEMA_MUST_REMAIN_UNCHANGED=true
AUTHORITY_BINDING_COUNT_MUST_REMAIN_14=true
PRINTED_DAG_MUST_REMAIN_8_NODES_12_EDGES=true
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
~~~

This gate does not embed its own SHA-256.  Amendment v8 and the sole later
fresh independent append-only re-review must bind this file's externally
computed final digest.  G-M1 remains open, D-M2 remains closed, and no
implementation or execution is authorized by these design-only bytes.

## 9. Append-only correction: auth-reap ACK before inherited global final

Status: **NARROW SUPERSEDING ADDENDUM — C0/M1/m0 REMAIN OPEN**  
Date: 2026-08-17 (Asia/Shanghai)

This addendum preserves the complete original v8 gate as its exact prefix:

~~~text
PRESERVED_GATE_V8_PREFIX_LINES=599
PRESERVED_GATE_V8_PREFIX_BYTES=31194
PRESERVED_GATE_V8_PREFIX_SHA256=f8397076858012c13c657108cf7903f674d4bb0e880b127d477b2af7c8c3976d
~~~

The prefix incorrectly made one terminal-requester `CHILD_REAPED` sufficient
for reconciliation, let P close the global P--G control connection at that
point, and made G's `CONTROL_EOF_OBSERVED` a successful local terminal state.
Those three consequences omit the inherited v3 acknowledgment and truncate
the inherited v2/v3 global FINAL protocol.  Only the conflicting sentences,
state suffixes, table rows, review duties, and authorization-matrix values in
prefix Sections 2, 3, 7, and 8 are superseded by this Section 9.  Every other
prefix byte and every base/v1--v7 clause remains binding.

In particular, prefix Section 2's statement that v8 does not generalize
`CHILD_REAPED_ACK` to the terminal requester is superseded.  The sole corrected
state applicability below is mandatory.  This does not add a record, payload,
direction, enum member, channel, or serialized field.

### 9.1 Exact existing ACK and auth-session-only reconciliation

After the exact requester exit/reap/identity/FD-4/FD-5 join already required
by prefix Section 3.2, the successful auth-reap suffix is exactly:

~~~text
G: REQUESTER_REAPED
   -> CHILD_REAPED_SENT
   -> CHILD_REAPED_ACKED
   -> AUTH_REAP_RECONCILED

P: FD5_EOF_OBSERVED
   -> CHILD_REAPED_VALIDATED
   -> CHILD_REAPED_ACK_SENT
   -> AUTH_REAP_ACK_SENT
~~~

The two wire records are the already inherited global control records:

~~~text
G -> P: CHILD_REAPED session=DEC child=DEC status=DEC
P -> G: CHILD_REAPED_ACK session=DEC child=DEC status=DEC
~~~

Both retain the inherited four-byte big-endian length, 4096-byte ceiling,
canonical ASCII, no-trailing-byte, no-ancillary-item, direction, endpoint,
credential, complete-send, and single-attempt rules.  The ACK repeats all
three fields byte-for-byte from the one accepted reap record.  P sends it
exactly once, only after independently validating the exact registered
terminal requester, direct-child/session join, status, process-gone proof,
FD-4 terminal ledger, FD-5 clean EOF, and no-open/no-extra-frame predicates.
Only a complete ACK send enters `CHILD_REAPED_ACK_SENT`.  G enters
`CHILD_REAPED_ACKED` and `AUTH_REAP_RECONCILED` only after it receives and
validates that exact ACK in `CHILD_REAPED_SENT`.

`CHILD_REAPED_ACK` remains an amendment-v3 inherited **global** P--G record.
It is outside the exact twelve D-M1 session-form enum, so there is no
thirteenth D-M1 form and no new wire-form count.  Applying its existing bytes
to this one terminal-requester reap is the sole corrected state guard; it
does not widen method, target, child-admission, object, cleanup, or Route
authority.

Complete ACK acceptance closes only the D-M1 auth-session reap
reconciliation.  `AUTH_REAP_RECONCILED` and `AUTH_REAP_ACK_SENT` are not
global `CLOSED`, do not authorize a result, do not close either P--G endpoint,
and do not replace any FINAL freeze/kill/reap/empty/cleanup/exit proof.

### 9.2 Exact retained global FINAL sequence on the same live control

After G accepts `CHILD_REAPED_ACK`, both endpoints and all inherited guardian,
cgroup, ledger, cleanup, signal, and reap authority remain live.  G then
permanently closes every remaining RPC and child-admission gate and the same
authenticated P--G connection carries the inherited successful FINAL sequence
in exactly this order:

~~~text
G -> P: FREEZE_REQUEST session=DEC handle=0 phase=FINAL
P -> G: FROZEN_FINAL session=DEC handle=0 phase=FINAL epoch=DEC
G -> P: KILL_REQUEST session=DEC epoch=DEC
P -> G: KILL_ISSUED session=DEC epoch=DEC
G -> P: REAPED session=DEC epoch=DEC
P -> G: CGROUP_EMPTY session=DEC epoch=DEC
G: retained capability-relative cleanup and every retained cleanup proof
G -> P: each inherited CLEANUP_RESULT; the last one occurs after closing
        the workers-cgroup FD
G -> P: SIGNAL_CLEANED signo=DEC outcome=OUTCOME, exactly when the inherited
        handled-signal path requires it
G -> P: EXIT status=DEC outcome=OUTCOME, exactly once and terminal
G: exit
P: retained-pidfd reap of G; guardian/session populated-zero proofs; exact
   retained-capability removal of empty cgroups in workers, guardian,
   session order
~~~

The displayed signal line is conditional only under the already closed
inherited signal state: if `SIGNAL_PENDING` exists, matching
`SIGNAL_CLEANED` follows all required cleanup and precedes `EXIT`; otherwise
there is no signal record and `EXIT` still occurs exactly once.  All other
retained cleanup, signal, object-ledger, foreign-preservation, and
`CLEANUP_RESULT` cardinality/state rules remain exact even though the compact
display does not repeat every intermediate operation.

`REAPED` covers every remaining direct or reparented descendant through
`ECHILD` and the empty G ledger.  It neither reaps the already reaped terminal
requester a second time nor substitutes for that requester's separately
ACKed `CHILD_REAPED`.  `CGROUP_EMPTY` still requires P's independent
workers-empty/task-empty/fresh-populated-zero evidence.  No private-path
cleanup begins before it.

P must not close or half-close the P--G endpoint after
`CHILD_REAPED_ACK_SENT`; it retains the endpoint through complete receipt and
validation of the sole `EXIT`.  G must not close or half-close its endpoint
after `CHILD_REAPED_ACKED`; it retains it through complete send of `EXIT` and
then closes it only by the inherited orderly exit.  P's subsequent pidfd reap
of G and populated-zero/cgroup-removal proofs remain mandatory.  No endpoint
EOF is a record, receipt, acknowledgment, or success state.

Accordingly, every prefix occurrence that permits P close after
`CHILD_REAPED`, names `CONTROL_EOF_OBSERVED` as a success edge, or lets G enter
local successful `CLOSED_TOMBSTONE` on that EOF is deleted semantically and
replaced by this sequence.  There is no `CONTROL_EOF_OBSERVED` success state.
An EOF caused by G's specified exit may occur only after P has completely
received and validated `EXIT`; it supplies no missing proof, and P still must
reap G and complete the inherited final cgroup proofs.

### 9.3 Late FD-4 anomaly and no same-byte success

Before G may enter `REQUESTER_REAPED` or construct `CHILD_REAPED`, it must
complete the inherited FD-4 terminal drain on the retained exact peer:

1. the exact terminal reply was the sole terminal send;
2. the requester then closed original FD 4 in the frozen order;
3. G drained to clean EOF with no queued datagram, partial/truncated frame,
   ancillary item, duplicate close, capability-bearing operation, or other
   post-terminal byte;
4. G closed its peer, proved both holder identities absent, and permanently
   fixed the anomaly-free drain fact before the child-reap success edge; and
5. the requester was then reaped with the exact retained identity and status.

Because clean EOF plus requester reap makes later FD-4 input impossible, this
join is complete before any success-valid reap record can be sent.  If any
late/queued/malformed FD-4 input or drain defect exists, G enters inherited
fail-closed containment and **must not send a complete `CHILD_REAPED` for
success reconciliation**.  P therefore sends no `CHILD_REAPED_ACK`.  The
same canonical `CHILD_REAPED` bytes have no hidden failure bit and may not be
sent as “failure-marked cleanup evidence,” then accepted as success.  That
prefix Section 3.3 allowance is superseded.  Failure containment instead uses
the inherited FINAL freeze/kill/reap/empty path while retaining the first
anomaly; it never changes the anomaly to ABSENT or PASS.

If a transport failure occurs while sending `CHILD_REAPED`, the incomplete
attempt is terminal, never retried, and cannot be parsed or ACKed.  If P
rejects a complete record for wrong state/session/child/status/identity or a
duplicate, it sends no ACK and enters failure.  If the ACK send is zero,
short, partial, errno, ambiguous, missing, malformed, premature, duplicate,
or cross-bound, neither side enters auth-reap reconciliation.  No later
FREEZE_REQUEST can convert that failed auth-reap join to success.

### 9.4 Corrected EOF, crash, and tombstone boundary

Before P completely receives and validates the one inherited terminal
`EXIT`, any P--G EOF, half-close, corrupt/incomplete record, endpoint identity
drift, or peer crash is failure:

- if P observes G failure, P invokes the inherited session cgroup kill,
  waitid/reap-to-`ECHILD`, pidfd close, and fresh populated-zero containment,
  records only `CRASH_TEARDOWN`, performs no private-mount pathname cleanup,
  and never asserts successful `ABSENT` or PASS;
- if G observes P failure, G closes admission, performs no pathname deletion,
  closes its descriptors, exits PID 1 for namespace teardown, and records no
  successful cleanup or result; and
- a complete earlier FINALIZE, FINALIZED_ACK, terminal receipt,
  `CHILD_REAPED`, or `CHILD_REAPED_ACK` remains an immutable historical fact
  but cannot make the failed global FINAL lifecycle successful.

After P has validated `EXIT`, G's inherited exit and the resulting endpoint
closure are consequences, not evidence.  Failure to reap the exact G,
nonzero populated state, pidfd/identity drift, nonempty/replaced cgroups, or
any final removal-proof defect still yields the inherited failure tombstone
and no PASS.  P closes its own endpoint only as part of disposal after the
validated EXIT and G-reap path; G has no post-exit local state inferred from
P EOF.

Queued duplicates or wrong-direction records at any corrected suffix state
are fatal.  A failure before auth-reap ACK completes enters an
`AUTH_REAP_FAILED_TOMBSTONE`; a later failure enters the inherited global
`CRASH_TEARDOWN`/failed terminal ledger.  Neither tombstone is recycled, and
neither EOF nor later physical cleanup erases its first cause.  Live silence
is nonprogress, never timeout-derived success.  There is no control-close
race whose winning branch can produce the same successful bytes.

### 9.5 Narrow preservation and authorization restatement

This correction changes no D-M1 requester--P FD-5 form, no D-M1 P--G session
form, no v7 create/active/terminal capability or evidence ceiling, and no
D-M2 syscall, slot, quiescence, duplicate, diagnostic, lifetime, unwind, or
ABA clause.  It changes no base/v1--v7 method, target, outcome, schema, path,
CSV byte, 120/35/35/28/173 count, fourteen authority bindings, eight-node/
twelve-edge DAG, theorem owner, universal-recovery state, or Route state.
The prefix's count-eight effective-amendment grammar and all prior closures
remain unchanged.

The sole open design finding is still G-M1; this gate does not close it:

~~~text
CORRECTED_GATE_VERDICT=PASS_TO_ONE_AMENDMENT_V8
CURRENT_OPEN_FINDINGS=C0_M1_m0
G_M1_STATUS=OPEN
D_M2_STATUS=CLOSED_FROZEN_NO_REGRESSION

AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v8.md
AMENDMENT_V8_WRITE_AUTHORIZED=true
FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V8_FROZEN_AND_EXTERNALLY_HASHED=true

CHILD_REAPED_ACK_IS_EXISTING_V3_GLOBAL_FORM=true
CHILD_REAPED_ACK_IS_D_M1_SESSION_FORM=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
NEW_FORM_OR_COUNT_AUTHORIZED=false
AUTH_REAP_RECONCILIATION_CLOSES_GLOBAL_CONTROL=false
GLOBAL_FINAL_SEQUENCE_RETAINED=true
CONTROL_EOF_OBSERVED_SUCCESS_STATE=false
CONTROL_EOF_BEFORE_VALIDATED_EXIT_IS_SUCCESS=false
LATE_FD4_ANOMALY_CAN_YIELD_SUCCESS_CHILD_REAPED_OR_ACK=false
SAME_CHILD_REAPED_BYTES_CAN_MEAN_FAILURE_AND_SUCCESS=false

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
~~~

Amendment v8 remains provisional and is not authority until authored against
the final external SHA-256 of this corrected gate, frozen, and independently
hashed.  Only then is the already authorized one fresh append-only review
permitted.  No amendment or review byte is changed by this correction.
