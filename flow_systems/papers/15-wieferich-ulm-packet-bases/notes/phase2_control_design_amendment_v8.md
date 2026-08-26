# Replacement Paper 15 deterministic-control design amendment v8

Status: **FROZEN DESIGN AMENDMENT v8 — G-M1 REMAINS OPEN PENDING FRESH INDEPENDENT REREVIEW**  
Version: `P15R-CONTROLS-AMENDMENT-v8.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Current independent verdict retained: **REVISE — C0/M1/m0**  
Control implementation or execution performed here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS experiment-agent reproducibility protocol and
  academic-pipeline integrity discipline
- Origin Mode: deterministic exact-byte control-design amendment
- Origin Date: 2026-08-17
- Verification Status: UNVERIFIED_PENDING_FRESH_INDEPENDENT_REREVIEW
- Version Label: `p15r_control_design_amendment_v8`
- Scope: only the post-`FINALIZED_ACK` global P--G control, requester reap,
  inherited `CHILD_REAPED`/`CHILD_REAPED_ACK`, retained global `FINAL`
  protocol, endpoint-exit, failure, and tombstone lifecycle, plus the
  append-only successor needed to bind this amendment; no
  implementation, run, result, theorem, Route, manuscript, release, or
  publication claim

## 1. Exact authority, precedence, and complete delta

### 1.1 Complete current-byte authority

The sole authorized target was confirmed absent before its first write.
Before this amendment was drafted, the complete authority chain was freshly
read and every record was independently re-hashed.  The exact receipts are:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| remediation gate v2 | `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` |
| amendment v2 | `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| remediation gate v3 | `notes/phase2_control_design_remediation_gate_v3.md` | 578 | 27299 | `e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac` |
| amendment v3 | `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| remediation gate v4 | `notes/phase2_control_design_remediation_gate_v4.md` | 645 | 30174 | `df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647` |
| amendment v4 | `notes/phase2_control_design_amendment_v4.md` | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| remediation gate v5 | `notes/phase2_control_design_remediation_gate_v5.md` | 839 | 41734 | `55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7` |
| blocked/no-op amendment v5 | `notes/phase2_control_design_amendment_v5.md` | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` |
| corrected remediation gate v6 | `notes/phase2_control_design_remediation_gate_v6.md` | 1252 | 62896 | `a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00` |
| amendment v6 | `notes/phase2_control_design_amendment_v6.md` | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` |
| remediation gate v7 | `notes/phase2_control_design_remediation_gate_v7.md` | 776 | 38865 | `a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576` |
| amendment v7 | `notes/phase2_control_design_amendment_v7.md` | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` |
| current append-only review | `notes/phase2_control_design_peer_review.md` | 3567 | 187634 | `cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73` |
| corrected remediation gate v8 | `notes/phase2_control_design_remediation_gate_v8.md` | 852 | 43684 | `342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8` |

The corrected v6 gate retains its exact 58,261-byte / 1,140-line prefix at
SHA-256
`81d5543fdd0acc72122cd9a2171a7354a7d51d7d4a2f2c8f6a78fb12b3af7dcc`.
The corrected v8 gate retains its exact 31,194-byte / 599-line prefix at
SHA-256
`f8397076858012c13c657108cf7903f674d4bb0e880b127d477b2af7c8c3976d`.
The review is one append-only byte string.  Its exact nested prefixes are:

~~~text
prefix_lines=3149 prefix_bytes=165177 sha256=075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c
prefix_lines=2746 prefix_bytes=143812 sha256=30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb
prefix_lines=2308 prefix_bytes=119250 sha256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
prefix_lines=1910 prefix_bytes=96524 sha256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
prefix_lines=1524 prefix_bytes=74876 sha256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
prefix_lines=1017 prefix_bytes=49358 sha256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
prefix_lines=488 prefix_bytes=22894 sha256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec
~~~

The operative design is the base plus amendments v1--v4, blocked/no-op v5,
v6, v7, and this amendment.  The independent verdict remains
`REVISE C0/M1/m0`; G-M1 remains open.  D-M2 is closed and frozen against
regression.  This author record is not independent closure evidence and
does not embed or self-authenticate its own digest.

### 1.2 Exact bounded supersessions

This amendment supersedes only:

1. amendment-v7 Section 9.1's G edge from complete
   `SESSION_AUTH_FINALIZED_ACK` send directly to `CLOSED_TOMBSTONE`, solely
   with Sections 3--5 below;
2. amendment-v7 Section 9.1's permission for orderly global P--G control
   close after ACK validation and its categorical no-post-ACK-P--G-message
   sentence, solely by distinguishing no later D-M1 session form from the
   retained inherited `CHILD_REAPED`/`CHILD_REAPED_ACK` and global `FINAL`
   control protocol;
3. amendment-v7 Sections 6.3, 9.1--9.2, and 10 only where their post-ACK
   state, duplicate, EOF/crash, reap, close, or tombstone wording conflicts
   with Sections 3--5; and
4. amendment-v7 Section 13's successor grammar, solely so the current active
   count-seven block becomes historical and a future active count-eight
   block ends at v8.

Every supersession is semantic and line-bounded.  It changes no
pre-`FINALIZED_ACK` capability, commitment, frame, transcript, send,
receive, comparison, state, outcome, or failure fact.  Complete `FINALIZE`
and complete `FINALIZED_ACK` remain immutable facts on every later branch.
A later error never retroactively describes either one as unsent.

Every omitted base/v1--v7 clause remains binding.  Blocked v5 remains a
no-op provenance member.  No new syscall, descriptor, channel, frame,
target, method, path, detector, exit class, authority binding, graph item,
Route, fallback, or compatibility parser is introduced.

### 1.3 Complete v8 operational delta

The entire v8 operational delta is:

~~~text
new G in-memory states after complete FINALIZED_ACK:
  FINALIZED_AWAITING_REAP
  REQUESTER_REAPED
  CHILD_REAPED_SENT
  CHILD_REAPED_ACKED
  AUTH_REAP_RECONCILED

new P in-memory state after FD5_EOF_OBSERVED:
  CHILD_REAPED_VALIDATED
  CHILD_REAPED_ACK_SENT
  AUTH_REAP_ACK_SENT

new auth-reap non-success suffix:
  POST_FINALIZE_FAILED -> AUTH_REAP_FAILED_TOMBSTONE

post-ACK inherited global records made reachable:
  G -> P: CHILD_REAPED session=DEC child=DEC status=DEC
  P -> G: CHILD_REAPED_ACK session=DEC child=DEC status=DEC

retained global sequence after auth-reap ACK:
  FREEZE_REQUEST -> FROZEN_FINAL -> KILL_REQUEST -> KILL_ISSUED
  -> REAPED -> CGROUP_EMPTY -> CLEANUP_RESULT*
  -> optional inherited SIGNAL_CLEANED -> EXIT -> G exit -> P reaps G

successful P--G EOF state:
  NONE

new requester--P FD-5 form:
  NONE

new D-M1 P--G session form:
  NONE

new requester--G FD-4 form:
  NONE

review grammar:
  six existing blocks historical
  one future active v7 count-eight block, appended only by a fresh reviewer
~~~

All states, failure causes, ledgers, send results, EOF facts, and close
receipts below are operational, in-memory, and nonserialized.

## 2. Unchanged wire grammars and coordinate ownership

### 2.1 Exact-twelve enums remain exact

Amendment-v7 Sections 7 and 8 remain byte-exact.  The requester--P FD-5
enum still contains exactly twelve forms, and the D-M1 P--G session enum
still contains exactly twelve forms.  There is no thirteenth form, read ACK,
post-ACK abort, close alias, or compatibility action.

The post-ACK global record used here is the inherited amendment-v2 record:

~~~text
G -> P:
CHILD_REAPED session=DEC child=DEC status=DEC
~~~

It retains the inherited four-byte unsigned big-endian payload length,
canonical ASCII, 4096-byte ceiling, exact field order and direction, one
complete-send requirement, authenticated P--G endpoint, state guard,
credential/identity contract, and once-per-registered-child cardinality.
It is outside the twelve D-M1 P--G session forms.  It is neither a thirteenth
form nor a replacement for `FINALIZED_ACK`.

### 2.2 Direct-child and auth-session coordinates are not aliases

`CHILD_REAPED.session` is the registered direct-child session coordinate in
the inherited child ledger.  The v7 D-M1 `auth/session/request/close` tuple
retains its own opaque auth-session coordinate.  P joins them only through
the already frozen direct child/auth mapping established by registration,
admission, pidfd, endpoint, and owner records.  It never copies one decimal
into the other by convention or infers equality from a record under review.

The required join is:

~~~text
registered direct-child session/child/status
+ immutable child-to-auth mapping
+ v7 auth/session/request/close tuple
+ exact requester pidfd/start-time/NSpid/cgroup/credential identity
+ exact FD4 and FD5 terminal ledgers
~~~

Any missing, multiple, stale, cross-child, cross-session, or inconsistent
mapping is terminal before reconciliation.

### 2.3 Exact inherited `CHILD_REAPED_ACK` state guard

The corrected v8 gate makes the already inherited amendment-v3 global ACK
mandatory for this one terminal-requester reap.  Its wire bytes are exactly:

~~~text
P -> G:
CHILD_REAPED_ACK session=DEC child=DEC status=DEC
~~~

It retains the inherited framing, canonical-ASCII grammar, 4096-byte limit,
authenticated endpoint, direction, credential, complete-send, and
single-attempt rules.  Its three values repeat byte-for-byte the fields of
the one accepted `CHILD_REAPED`.  It is outside the exact twelve D-M1 P--G
session forms, is not a thirteenth form, and adds no serialized field,
channel, or count.

The only new applicability is the exact terminal-requester state guard in
Section 3.5.  It does not widen creator enumeration, child admission,
method, target, object, cleanup, result, Route, or publication authority.
Its completion reconciles only the auth-session reap.  It does not close
the global P--G endpoint, authorize a result, or replace the inherited
global `FINAL` protocol.

## 3. Exact post-`FINALIZED_ACK` successful lifecycle

### 3.1 Authentication finalization is not global-control completion

Complete `SESSION_AUTH_FINALIZED_ACK` send finalizes only the v7 D-M1
authentication transcript.  On that complete send G enters exactly:

~~~text
FINALIZED_AWAITING_REAP
~~~

It does not enter `CLOSED_TOMBSTONE`; close or half-close the P--G control
endpoint; discard the requester pidfd, endpoint identities, direct-child or
guardian ledger; discard waitid/reap authority; or treat P--G EOF as already
observed.  G retains those live authorities until their exact release edges
below.  The control connection remains live for inherited global lifecycle
records.

In `FINALIZED_AWAITING_REAP`, the D-M1 auth session is sealed.  Neither side
may send or accept a later D-M1 success form.  No FD-4, FD-5, or requester
operation may mutate a session, root, lock, object, generated member,
result, or cleanup decision.  Sealing D-M1 does not suppress the inherited
global `CHILD_REAPED`, `CHILD_REAPED_ACK`, or later global `FINAL` records.

### 3.2 Exact auth-reap state suffixes

The successful auth-reap suffixes are exactly:

~~~text
P:
FINALIZE_SENT
  -> FINALIZED_ACKED
  -> TERMINAL_RECEIPT_SENT
  -> FD5_EOF_OBSERVED
  -> CHILD_REAPED_VALIDATED
  -> CHILD_REAPED_ACK_SENT
  -> AUTH_REAP_ACK_SENT

G:
FINALIZE_RECEIVED
  -> FINALIZED_AWAITING_REAP
  -> REQUESTER_REAPED
  -> CHILD_REAPED_SENT
  -> CHILD_REAPED_ACKED
  -> AUTH_REAP_RECONCILED

either side before auth-reap reconciliation:
  -> POST_FINALIZE_FAILED
  -> AUTH_REAP_FAILED_TOMBSTONE
~~~

The transition owner table is exact:

| Side/from | Sole success event | To |
|---|---|---|
| G `FINALIZE_RECEIVED` | complete exact `FINALIZED_ACK` send | `FINALIZED_AWAITING_REAP` |
| P `FINALIZE_SENT` | receive and validate that complete exact ACK | `FINALIZED_ACKED` |
| P `FINALIZED_ACKED` | complete exact `TERMINAL_RECEIPT` FD-5 send | `TERMINAL_RECEIPT_SENT` |
| P `TERMINAL_RECEIPT_SENT` | identity-valid clean FD-5 EOF under Section 3.3 | `FD5_EOF_OBSERVED` |
| G `FINALIZED_AWAITING_REAP` | exact requester waitid/reap join under Section 3.4 | `REQUESTER_REAPED` |
| G `REQUESTER_REAPED` | complete exact inherited `CHILD_REAPED` send | `CHILD_REAPED_SENT` |
| P `FD5_EOF_OBSERVED` | exact `CHILD_REAPED` join plus child-pidfd and FD-5-peer close/absence proofs | `CHILD_REAPED_VALIDATED` |
| P `CHILD_REAPED_VALIDATED` | complete exact inherited `CHILD_REAPED_ACK` send | `CHILD_REAPED_ACK_SENT`, then the immutable local `AUTH_REAP_ACK_SENT` fact |
| G `CHILD_REAPED_SENT` | receive and validate that one exact ACK | `CHILD_REAPED_ACKED`, then `AUTH_REAP_RECONCILED` |

No attempted send, readiness event, copied flag, EOF, reap notification, or
close attempt advances a state before its exact success predicate.
`AUTH_REAP_ACK_SENT` and `AUTH_REAP_RECONCILED` close only the auth-session
reap join.  They are not global `CLOSED`, result, cleanup, or endpoint-close
states.  The same live P--G control immediately remains subject to Section
3.6.

### 3.3 Terminal receipt and FD-5 EOF

P attempts the exact v7 `SESSION_AUTH_TERMINAL_RECEIPT` once only after it
validates the complete ACK.  Only a return equal to the complete datagram
length enters `TERMINAL_RECEIPT_SENT`; zero, short, errno, or ambiguous
return is failure with no retry.

The requester closes original FD 5 only after its retained v7 complete-
receipt condition.  P accepts EOF only after its complete receipt send and
only when all of the following are true:

~~~text
same registered child-unique endpoint and credential identity
no open auth, child-audit, or terminal frame
no queued duplicate or extra datagram
no MSG_TRUNC or MSG_CTRUNC observation
no ancillary item or endpoint substitution
no prior post-finalization failure
~~~

The observation enters `FD5_EOF_OBSERVED`.  It proves P's complete receipt
send followed by peer closure; it does not claim an independently observed
requester application-level read.  EOF before complete receipt is failure,
not a receipt or success substitute.

### 3.4 FD-4 anomaly-free close, requester exit, and exact reap

The v7 FD-4 order is unchanged.  After one complete exact terminal reply
receive and one complete `TERMINAL_OBSERVED` send, the requester closes its
original FD 4 before exit.  Before a success-valid requester reap, G must
drain the retained exact FD-4 peer to clean EOF, prove there is no queued
datagram, partial/truncated frame, ancillary item, duplicate close,
capability-bearing operation, or other post-terminal byte, close its peer,
and prove both holder identities absent.  It permanently fixes this
anomaly-free drain fact together with the immutable terminal-reply and
full-send receipts.  An extra FD-4 datagram is never accepted.

The requester then exits.  G's exact successful reap join requires:

~~~text
one waitid reap of the exact registered direct child
retained pidfd, start-time, NSpid, cgroup, credential, role, owner identity
exact expected exit status
process-gone proof
empty post-reap descriptor/process set
clean terminal FD4 holder/EOF ledger
no wrong child, duplicate reap, identity drift, or earlier suffix failure
~~~

Only this conjunction enters `REQUESTER_REAPED`.  G retains the live pidfd
through waitid and process-gone proof.  After the exact reap it closes that
pidfd at its inherited edge, proves immediate absence/EBADF as already
required, and retains the pidfd identity and close receipt in the child
ledger through auth-reap ACK and the inherited global `FINAL` sequence.  It
does not discard the ledger itself.

If any late, queued, malformed, truncated, or ancillary FD-4 input or drain
defect exists, G enters fail-closed containment before `REQUESTER_REAPED`.
It must not construct or completely send `CHILD_REAPED` for success
reconciliation.  The canonical reap bytes have no hidden failure bit and
may not be reused as a same-byte “failure-marked” record.

A live requester which has not produced EOF or exit causes nonprogress, not
timeout-derived success.  No new timeout is introduced.

### 3.5 Exact inherited reap record, ACK, and auth reconciliation

From `REQUESTER_REAPED`, G constructs exactly one inherited record from its
registered direct-child ledger and actual waitid status.  Only one complete
framed-record send enters `CHILD_REAPED_SENT`.  There is no retry, second
record, D-M1 alias, or substitute.

P does not dequeue a candidate `CHILD_REAPED` for success before
`FD5_EOF_OBSERVED`.  Queue readiness is not acceptance.  A correct record
may wait on the authenticated control queue while P completes the FD-5 EOF
observation; P then receives exactly one record and independently requires:

~~~text
exact registered direct-child session, child, and expected status
unique immutable child-to-auth mapping
exact v7 auth/session/request/close/outcome tuple
requester pidfd/start-time/NSpid/cgroup/credential identity
P's retained FD5_EOF_OBSERVED fact
G's retained clean FD4 terminal ledger as joined by inherited receipts
no open frame, duplicate, prior failure, or unreconciled child
inherited process-gone/reap evidence
~~~

After this join P performs the retained post-reap child-pidfd close and
immediate EBADF proof, closes its retained FD-5 peer exactly once, and proves
the expected endpoint/holder absence without intervening allocation.  Only
the complete join and both close/absence proofs enter
`CHILD_REAPED_VALIDATED`.

From `CHILD_REAPED_VALIDATED`, P constructs exactly one inherited
`CHILD_REAPED_ACK` by repeating the accepted record's `session`, `child`,
and `status` fields byte-for-byte.  It attempts the canonical framed send
exactly once.  Only a complete send enters `CHILD_REAPED_ACK_SENT` and fixes
the local `AUTH_REAP_ACK_SENT` fact.  Zero, short, partial, errno, or
ambiguous send is terminal; it is never retried and cannot be inferred from
later traffic.

G accepts exactly one ACK only in `CHILD_REAPED_SENT`, only on the same
authenticated control endpoint, and only if all three canonical fields
equal the sent reap record byte-for-byte.  A complete valid receive enters
`CHILD_REAPED_ACKED` and then `AUTH_REAP_RECONCILED`.  Missing, malformed,
premature, duplicate, wrong-direction, wrong-coordinate, cross-bound,
truncated, ancillary-bearing, or trailing-byte ACK is terminal.  No later
`FREEZE_REQUEST`, EOF, or cleanup record synthesizes the missing join.

An early queued correct record is not processed as success until this state
guard is true.  A record actually received in the wrong state, or any
missing, malformed, duplicate, wrong-session, wrong-child, wrong-status,
cross-bound, or extra record, is terminal.

### 3.6 Exact retained global `FINAL` protocol on the same control

Only after G reaches `AUTH_REAP_RECONCILED` does it permanently close every
remaining RPC and child-admission gate.  Both P--G endpoints and all
inherited guardian, cgroup, ledger, signal, cleanup, and reap authorities
remain live.  The same authenticated connection then carries the retained
successful global sequence in exactly this order:

~~~text
G -> P: FREEZE_REQUEST session=DEC handle=0 phase=FINAL
P -> G: FROZEN_FINAL session=DEC handle=0 phase=FINAL epoch=DEC
G -> P: KILL_REQUEST session=DEC epoch=DEC
P -> G: KILL_ISSUED session=DEC epoch=DEC
G -> P: REAPED session=DEC epoch=DEC
P -> G: CGROUP_EMPTY session=DEC epoch=DEC
G: retained capability-relative cleanup and every retained cleanup proof
G -> P: each inherited CLEANUP_RESULT; the last follows closure of the
        workers-cgroup FD
G -> P: SIGNAL_CLEANED signo=DEC outcome=OUTCOME, exactly when the inherited
        handled-signal state requires it
G -> P: EXIT status=DEC outcome=OUTCOME, exactly once and terminal
G: exit
P: retained-pidfd reap of G; guardian/session populated-zero proofs; exact
   retained-capability removal of empty workers, guardian, session cgroups
~~~

The `SIGNAL_CLEANED` line is present only when the inherited
`SIGNAL_PENDING` state exists; otherwise it is absent and `EXIT` remains
exactly once.  Every compactly omitted `CLEANUP_RESULT`, object-ledger,
foreign-preservation, signal, capability-relative cleanup, and cardinality
guard remains binding.

`REAPED` covers every remaining direct or reparented descendant through
`ECHILD` and G's empty ledger.  It never reaps the already reaped terminal
requester twice and never substitutes for its separately ACKed
`CHILD_REAPED`.  P sends `CGROUP_EMPTY` only after its independent
workers-empty, task-empty, and freshly read `populated 0` proof.  No private
pathname cleanup begins before that record.  G sends the last
`CLEANUP_RESULT` only after every applicable cleanup proof and closure of the
workers-cgroup FD, then sends the conditional signal record and the one
terminal `EXIT` in inherited order.

P must not close or half-close the control endpoint after
`AUTH_REAP_ACK_SENT`; it retains it through complete receipt and validation
of `EXIT`.  G must not close or half-close after
`AUTH_REAP_RECONCILED`; it retains the endpoint through the complete `EXIT`
send and closes it only by its inherited orderly exit.  P then reaps the
exact G through its retained pidfd, proves guardian/session populated zero,
and removes the empty cgroups in workers, guardian, session order.

### 3.7 EOF and success evidence ceiling

There is no successful `CONTROL_EOF_OBSERVED` state.  Before P completely
receives and validates `EXIT`, any P--G EOF, half-close, incomplete/corrupt
record, endpoint drift, or peer crash is failure.  P's earlier terminal
receipt or auth-reap ACK cannot upgrade it.  G's observation of P EOF at any
stage is the inherited failure edge: G closes admission, performs no
pathname deletion, closes descriptors, exits PID 1 for namespace teardown,
and records no successful cleanup or result.

After validated `EXIT`, G's exit and resulting endpoint EOF are consequences,
not a record, receipt, ACK, or success proof.  P still must reap the exact G,
verify identity and fresh populated-zero state, and complete the inherited
cgroup-removal proofs.  It disposes its endpoint only after the validated
`EXIT` and G-reap path.  Failure of the G reap, cgroup proof, or removal is
terminal despite a complete `EXIT`.  No G-local state is inferred from P's
later endpoint disposal, and no successful result is exposed before every
inherited final predicate holds.

## 4. Closed post-finalization admission and duplicate rule

The complete successful post-ACK traffic rule is:

~~~text
auth-reap suffix:
  P -> requester: SESSION_AUTH_TERMINAL_RECEIPT
  G -> P: CHILD_REAPED session=DEC child=DEC status=DEC
  P -> G: CHILD_REAPED_ACK session=DEC child=DEC status=DEC

after AUTH_REAP_RECONCILED on the same live global control:
  exact Section 3.6 inherited FINAL records through EXIT

new D-M1 P--G session form:
  NONE

new requester--P FD-5 form:
  NONE

new requester--G FD-4 operation:
  NONE
~~~

`CHILD_REAPED` and `CHILD_REAPED_ACK` are inherited global forms outside
the exact twelve D-M1 session forms.  The global `FINAL` records likewise
retain their own inherited enum, byte grammar, directions, state guards, and
cardinality.  This list is a chronology, not a new union enum or wildcard.

Any queued or later duplicate `TERMINAL_OBSERVED`, other FD-5 auth/audit
datagram, FD-4 `SESSION_CLOSE`, capability-bearing operation, D-M1 P--G
form, `CHILD_REAPED`, `CHILD_REAPED_ACK`, global `FINAL` record, or record
outside its inherited state guard is terminal.  The first observer
atomically:

1. fixes the endpoint, complete immutable frame or available partial bytes,
   frame hash, current state, and order coordinate;
2. before G reaches `AUTH_REAP_RECONCILED`, enters
   `POST_FINALIZE_FAILED`; after that state, enters the inherited global
   failed-terminal/`CRASH_TEARDOWN` state, always before any new operation
   or reply;
3. closes admission and performs no second `FINALIZE`, `FINALIZED_ACK`,
   terminal reply, receipt, auth-reap record, cleanup mutation, or D-M1
   abort exchange;
4. retains every already completed send/receive fact without rewriting
   history; and
5. uses only the still-live reap/control path or retained crash containment
   to make the requester and descriptors terminal.

G completes the anomaly-free FD-4 drain and fixes all G-side requester
success guards before it enters `REQUESTER_REAPED` or constructs a
success-valid `CHILD_REAPED`.  A late FD-4 anomaly, wrong status, identity
defect, or other G-only failure therefore prevents that record.  P sends no
ACK.  The same canonical `CHILD_REAPED` bytes are never emitted as
“failure-marked cleanup evidence” and can never mean both success and
failure.

Failure containment may use the retained `FINAL` freeze/kill/reap/empty
path only under its inherited failure guards.  It retains the first anomaly
and cannot enter the successful auth-reap states, synthesize the missing ACK,
authorize private-path deletion forbidden on the failure branch, assert
`ABSENT`, or yield PASS.  Clean EOF after a duplicate does not restore
success.

## 5. Total post-finalization failures and tombstones

### 5.1 Closed first-cause enum

The exact post-ACK in-memory first-cause enum is:

~~~text
TERMINAL_RECEIPT_SEND |
FD5_EARLY_EOF | FD5_EXTRA_DATAGRAM |
FD4_EXTRA_DATAGRAM | POST_ACK_D_M1_RECORD |
REQUESTER_IDENTITY | REQUESTER_EXIT_STATUS | REQUESTER_WAITID |
REQUESTER_WRONG_CHILD | REQUESTER_DUPLICATE_REAP |
REQUESTER_PROCESS_PRESENT | REQUESTER_FDSET_NONEMPTY |
CHILD_REAPED_SEND | CHILD_REAPED_RECORD |
CHILD_REAPED_ACK_SEND | CHILD_REAPED_ACK_RECORD |
GLOBAL_FINAL_RECORD | GLOBAL_FINAL_PROOF | EXIT_RECORD |
CONTROL_EOF_EARLY | P_CRASH | G_CRASH |
CONTROL_DISPOSAL | PIDFD_ABSENCE | FD5_PEER_ABSENCE |
G_REAP | CGROUP_FINAL | FINAL_LEDGER
~~~

Continuation is presentational.  The value is not a wire field, detector,
public exit class, serialized artifact, or replacement for inherited
`OUTCOME`.  The exact failed syscall/record, endpoint, return, errno,
available bytes, expected length, state, and identity remain separate ledger
coordinates.  The first cause is immutable and later cleanup cannot replace
it.

`FINALIZED_ACK` incomplete, invalid, or mismatched remains the exact v7
pre-ACK failure and begins no v8 success suffix.  The enum above applies only
after a complete ACK send exists.

### 5.2 Exact failure table

| First failing edge | Cause | Required result |
|---|---|---|
| terminal receipt zero, short, errno, ambiguous, or incomplete | `TERMINAL_RECEIPT_SEND` | P enters failure, never retries or sends a suffix record; requester is contained; G stays live only for reap/containment |
| FD-5 EOF before complete receipt | `FD5_EARLY_EOF` | never `FD5_EOF_OBSERVED`; no success or EOF synthesis |
| requester remains live without FD-5 EOF or exit | none while live | nonprogress; no timeout-derived success |
| queued or late extra FD-5 datagram | `FD5_EXTRA_DATAGRAM` | exact duplicate failure; no second receipt/finalize and no historical rewrite |
| queued or late extra FD-4 datagram or non-child operation | `FD4_EXTRA_DATAGRAM` | G performs no mutation/reply, cannot enter `REQUESTER_REAPED`, sends no success-valid `CHILD_REAPED`, closes admission, and contains/reaps requester |
| duplicate or late D-M1 P--G form | `POST_ACK_D_M1_RECORD` | receiver fails; no thirteenth form, compatibility action, ABORT, or retry |
| pid/start-time/NSpid/cgroup/credential drift | `REQUESTER_IDENTITY` | G cannot enter `REQUESTER_REAPED`; retained containment only |
| exit status mismatch | `REQUESTER_EXIT_STATUS` | no success-valid `CHILD_REAPED`; actual status remains only in the failed local ledger |
| waitid error or ambiguous reap | `REQUESTER_WAITID` | no success reap or record; containment and failed tombstone |
| wrong child | `REQUESTER_WRONG_CHILD` | reject before ledger mutation; no success record |
| duplicate reap | `REQUESTER_DUPLICATE_REAP` | reject; never synthesize process-gone or a second record |
| process still present at the required proof | `REQUESTER_PROCESS_PRESENT` | no success and no false process absence |
| nonempty post-reap process/descriptor set | `REQUESTER_FDSET_NONEMPTY` | no success, close, PASS, or false absence |
| CHILD_REAPED zero, short, partial, errno, or ambiguous send | `CHILD_REAPED_SEND` | G fails, never retries; P treats partial frame or EOF as failure |
| CHILD_REAPED missing, malformed, duplicate, wrong-coordinate, premature, or cross-bound | `CHILD_REAPED_RECORD` | P cannot enter `CHILD_REAPED_VALIDATED`, sends no ACK, and cannot reconcile |
| CHILD_REAPED_ACK zero, short, partial, errno, or ambiguous send | `CHILD_REAPED_ACK_SEND` | P fails with no retry; G cannot enter `CHILD_REAPED_ACKED` or start a successful global `FINAL` |
| CHILD_REAPED_ACK missing, malformed, duplicate, wrong-coordinate, premature, or cross-bound | `CHILD_REAPED_ACK_RECORD` | G cannot enter `AUTH_REAP_RECONCILED`; no later record repairs the join |
| any global FINAL record is missing, malformed, partial, duplicate, wrong-direction, out of order, or cross-bound | `GLOBAL_FINAL_RECORD` | inherited failed terminal/containment ledger; no successful cleanup or result |
| freeze/kill/reap/empty/cleanup/signal proof fails | `GLOBAL_FINAL_PROOF` | first defect retained; no `EXIT`-based success, PASS, or false `ABSENT` |
| EXIT is missing, partial, malformed, duplicate, wrong-status/outcome, premature, or not validated | `EXIT_RECORD` | P treats any EOF as failure and invokes retained containment |
| G crash or P observes P--G EOF before validated EXIT | `G_CRASH` or `CONTROL_EOF_EARLY` | P invokes retained cgroup/guardian containment, records only `CRASH_TEARDOWN`, performs no private-mount pathname cleanup, and emits no success or ABSENT |
| P crash or G observes P--G EOF at any live-control stage | `P_CRASH` or `CONTROL_EOF_EARLY` | G closes admission, performs no pathname deletion, closes descriptors, exits PID 1 for namespace teardown, and cannot claim success |
| P closes or half-closes control before validated EXIT and G-reap disposal | `CONTROL_EOF_EARLY` | no auth/global success; EOF is not a receipt or record |
| post-EXIT endpoint disposal is zero, errno, ambiguous, or identity-drifted | `CONTROL_DISPOSAL` | retained failed terminal ledger; no retry-derived success |
| exact G pidfd reap/identity/process-gone proof fails after validated EXIT | `G_REAP` | no final success despite complete EXIT or EOF |
| guardian/session populated-zero or empty-cgroup removal proof fails | `CGROUP_FINAL` | no final success, PASS, or false absence |
| child-pidfd close/absence proof fails | `PIDFD_ABSENCE` | failure tombstone and containment; no PASS |
| retained FD-5 peer close/absence proof fails | `FD5_PEER_ABSENCE` | failure tombstone and containment; no PASS |
| any other inherited final guardian/object/result ledger proof fails | `FINAL_LEDGER` | no successful terminal result, PASS, or false `ABSENT` |

Every send is one attempt and succeeds only at the complete required length.
There is no suffix retry.  A physical cleanup already completed does not
convert an auth/control failure into successful `CLOSED_TOMBSTONE`.

### 5.3 Failure-state completion

A living side which detects failure before G's valid ACK acceptance and
`AUTH_REAP_RECONCILED` enters `POST_FINALIZE_FAILED`; after that state it
enters the inherited global
`CRASH_TEARDOWN` or failed terminal ledger.  Either branch closes all new
admission and retains only the already frozen control, cgroup, guardian,
pidfd, reap, descriptor, and capability-relative containment authorities.
The pre-ACK branch enters `AUTH_REAP_FAILED_TOMBSTONE` only after every
locally reachable containment receipt is fixed.  Neither branch ever enters
a later successful suffix state.

For this boundary, “auth-reap ACK complete” means G has received, validated,
and accepted the exact ACK.  P's complete ACK send and
`AUTH_REAP_ACK_SENT` fact alone do not move either side into the global
success branch.

There is no post-ACK D-M1 `ABORT`/`ABORTED` exchange.  A still-live P--G
connection may carry only the inherited auth-reap or global containment
evidence exact for its state.  Failure of that send or connection is itself
fixed and cannot be retried on a new channel.

If P or G crashes, the dead process has no fabricated local transition.
The survivor's tombstone records `P_CRASH` or `G_CRASH`, the exact last
complete transcript/control fact, and every reachable containment receipt;
the missing peer state remains missing.  A clean-looking physical EOF does
not turn a crash into orderly success.

No failure authorizes deletion of a foreign replacement or unregistered
object.  `ABSENT` remains legal only under its complete inherited owned-
object-gone and foreign-preservation proof.

### 5.4 Mandatory live and tombstone ledger

Every post-finalization live, failed, and successful tombstone retains at
least:

~~~text
auth/session/request/close/outcome tuple
registered direct-child session/child/expected-status tuple
immutable child-to-auth mapping
requester endpoint, pidfd, start-time, NSpid, credentials, role, owner, cgroup
FINALIZE and FINALIZED_ACK exact bytes/hashes and complete-send facts
TERMINAL_RECEIPT exact bytes/hash and attempted/complete send result
FD4 and FD5 EOF, open-frame, queue, duplicate, truncation, ancillary facts
waitid result, actual status, process-gone and descriptor-empty observations
CHILD_REAPED exact bytes/hash and attempted/complete send result
CHILD_REAPED_ACK exact bytes/hash and attempted/complete send/receive result
child-pidfd and FD5-peer close/EBADF/absence receipts
every inherited global FINAL record, epoch, direction, bytes/hash, and result
EXIT exact bytes, complete-send, validation, G-exit, pidfd-reap, and cgroup proofs
P--G EOF and both endpoint close/disposal stages, never as success evidence
first post-finalization cause and exact failed edge
all v7 raw-value digests, commitments, reply bytes, direct joins, and OUTCOME
~~~

Live and terminal rows are never recycled.  EOF, process death, duplicate
drain, physical cleanup, or local close never erases the first failure,
upgrades `OUTCOME`, or changes a completed send fact.

## 6. Exact non-regression of v7, D-M2, and prior closures

Without weakening, v8 retains:

1. **V7 create join:** the exact commitment/template, prepacket raw-secret
   non-disclosure, immutable first FD-4 receive object, same-buffer returned
   cap/frame, P comparison, wrong-first consumption, no retry, and explicit
   trusted byte-bound non-Byzantine G ceiling;
2. **V7 active join:** commitment-only arming, first legal raw-cap use before
   mutation, session-scoped capability, and no per-operation requester-
   provenance overclaim;
3. **V7 terminal join:** fourth secret kind, exact terminal frame and
   digests, G full-send flag, requester-direct same-buffer
   `TERMINAL_OBSERVED`, `FINALIZE`/`FINALIZED_ACK`, exact twelve FD-5 forms,
   exact twelve D-M1 P--G forms, and no receipt-read claim;
4. **D-M2:** native x86_64 syscalls 434/438 with flags zero and actual
   permission; exact rows, pidfd/proc identity and lifetime; G quiescence;
   two snapshots; every duplicate/fstat/proc/reciprocal-diag comparison;
   common reverse unwind, immediate EBADF, restored holders, and both ABA
   exclusions.  V8 adds no audit trigger and no audit-local FD crosses its
   own `EXIT_ACK` or the validated-global-`EXIT`/G-exit disposal edge;
5. **C-M1/C-M2:** P-created child-unique FD 5, direct child request, actual
   FD-4 byte join, audited admission, and exact reciprocal Unix-diag ABI
   without fallback;
6. **B-M1..B-M3:** six pre-suite rows, closed owner/admission and 173-method
   boundary, phase-indexed descriptor/barrier lifetimes, and pre-access plus
   post-creator object registration/ACK/ledger ordering;
7. **A-M1:** unparameterized `SG_SCOPE`, primitive-only class recomputation,
   four primitive counterfactuals, and all 35 typed
   seed/mutation/reparse/reject/detector/inverse chains;
8. **A-M2:** recursive real-filesystem receipts, valid/malformed roots, five
   live falsifiers, and exact-one-coordinate mode/mtime probes without
   ctime masking;
9. **A-M3:** private namespace/cgroup possession, root-owned controls,
   retained parent/root/lock capabilities, capability-relative cleanup,
   replacement fixtures, foreign preservation, and no false `ABSENT`;
10. **A-M4:** manifest-first complete-review authentication, unique ordered
    amendment blocks, independent capability-relative amendment reads and
    hashes, and dereference before lifecycle adjacency; and
11. blocked v5's no-op provenance and every prior clause not expressly
    superseded in Section 1.2.

The only D-M2 reference change is the already authorized mechanical
recognition that FD 5 remains live until the terminal receipt/EOF/reap edge.
No D-M2 byte, call, observation, holder, or cardinality changes.

## 7. Frozen schemas, paths, counts, and DAG

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
keys/schema, and graph `A,D,R,G,I,C,M,V` with twelve distinct edges remain
unchanged.  V8 adds no manifest node, edge, self-hash, future-result edge,
or proof cycle.

## 8. Append-only count-eight successor

The current 187,634-byte / 3,567-line review at SHA-256
`cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73`
remains unchanged.  Its six effective-amendment blocks v1 through v6 are
immutable historical prefix authority.  Only after this amendment is frozen
and externally hashed may one fresh independent reviewer append this sole
active block, with no blank or commentary line inside it:

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

The final verifier first authenticates the complete post-v8 review through
the manifest-bound review FD.  From those same bytes it requires exactly one
byte-identical historical block for each version v1 through v6, exactly one
active v7 block above, and no other begin/end tag.  It rejects missing,
duplicate, reordered, nested, malformed, prefix-drifted, wrong-version,
wrong-count/index/path/digest, extra-key, blank, or commentary-bearing
blocks.

It then capability-opens amendments v1 through v8 independently in active
order beneath the same held package-root FD, using the retained beneath/no-
link rules, reads every byte, and recomputes all eight hashes.  Only after
every match may it set
`R.effective_amendments=[v1,v2,v3,v4,v5,v6,v7,v8]` before lifecycle
adjacency.  This changes no manifest key, binding, artifact, graph node,
edge, self-hash, future-result edge, or proof cycle.

## 9. Author-side contract audit and authorization stop

The author-side audit is limited to contract presence.  It cannot close the
independent finding:

| Gate obligation | Frozen v8 surface | Independent status |
|---|---|---|
| G retains global control and reap authority after ACK | Sections 3.1--3.7 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| exact FD-5 EOF, anomaly-free FD-4 close, reap, CHILD_REAPED/ACK, and auth reconciliation | Sections 3.3--3.5 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| same-control inherited FINAL sequence through validated EXIT, G exit, P reap, and cgroup proofs | Sections 3.6--3.7 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| duplicate, partial, EOF, crash, wrong-reap, ACK, and final-ledger totality | Sections 4--5 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| v7, D-M2, and all prior closure regression | Sections 6--7 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| active count-eight successor and eight dereferences | Section 8 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |

~~~text
P15R_CONTROL_DESIGN_AMENDMENT_V8=FROZEN_DESIGN_ONLY_PENDING_FRESH_INDEPENDENT_REREVIEW
BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
AMENDMENT_V7_SHA256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
CURRENT_REVIEW_SHA256=cb112e5eca0aee1d006fb2943bc805eb5a2cd8d27aa542c4812394b532602f73
REMEDIATION_GATE_V8_SHA256=342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8
REMEDIATION_GATE_V8_PREFIX_SHA256=f8397076858012c13c657108cf7903f674d4bb0e880b127d477b2af7c8c3976d

CURRENT_INDEPENDENT_VERDICT=REVISE_C0_M1_m0
G_M1_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
D_M2_STATUS=CLOSED_FROZEN_NO_REGRESSION
INDEPENDENT_FINDINGS_CLOSED_BY_AUTHOR=false
INDEPENDENT_PASS_CLAIMED=false
FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true

V8_SCOPE=POST_FINALIZED_ACK_GLOBAL_CONTROL_AND_REAP_ONLY
FINALIZED_ACK_CLOSES_D_M1_AUTH=true
FINALIZED_ACK_CLOSES_GLOBAL_P_G_CONTROL=false
G_POST_ACK_STATE=FINALIZED_AWAITING_REAP
G_CONTROL_RETAINED_THROUGH_AUTH_REAP_ACK=true
INHERITED_CHILD_REAPED_REQUIRED=true
INHERITED_CHILD_REAPED_ACK_REQUIRED=true
CHILD_REAPED_IS_D_M1_SESSION_FORM=false
CHILD_REAPED_ACK_IS_D_M1_SESSION_FORM=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M1_THIRTEENTH_FORM_AUTHORIZED=false
POST_ACK_D_M1_SESSION_FORM_AUTHORIZED=false
AUTH_REAP_RECONCILIATION_CLOSES_GLOBAL_CONTROL=false
GLOBAL_FINAL_SEQUENCE_RETAINED=true
P_G_CONTROL_RETAINED_THROUGH_VALIDATED_EXIT=true
CONTROL_EOF_OBSERVED_SUCCESS_STATE=false
CONTROL_EOF_BEFORE_VALIDATED_EXIT_IS_SUCCESS=false
EOF_SYNTHESIZES_RECEIPT=false
LATE_FD4_ANOMALY_CAN_YIELD_SUCCESS_CHILD_REAPED_OR_ACK=false
SAME_CHILD_REAPED_BYTES_CAN_MEAN_FAILURE_AND_SUCCESS=false
POST_ACK_DUPLICATE_RETROACTIVELY_UNSENDS_FINALIZE_OR_ACK=false
POST_ACK_CRASH_OR_PARTIAL_REAP_CAN_YIELD_SUCCESS=false

V7_CREATE_JOIN_RETAINED=true
V7_ACTIVE_EVIDENCE_CEILING_RETAINED=true
V7_TERMINAL_DIRECT_JOIN_RETAINED=true
D_M2_CLOSURE_RETAINED=true
ALL_PRIOR_CLOSURES_MUST_NOT_REGRESS=true

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
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
~~~

No generator, verifier, test, wrapper, implementation, control execution,
reproduction run, Route, composition, manuscript, figure, release, archive,
Git operation, or public synchronization was authorized or performed by
this amendment.  G-M1 remains open until the authorized fresh independent
append-only reviewer reads and attacks the final exact bytes and reaches an
independent verdict.
