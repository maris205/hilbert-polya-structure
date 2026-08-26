# Replacement Paper 15 deterministic-control design amendment v6

Status: **FROZEN DESIGN AMENDMENT v6 — D-M1 AND D-M2 REMAIN OPEN PENDING FRESH INDEPENDENT REREVIEW**  
Version: P15R-CONTROLS-AMENDMENT-v6.0  
Date: 2026-08-17 (Asia/Shanghai)  
Current independent verdict retained: **REVISE — C0/M2/m0**  
Control implementation or execution performed here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS experiment-agent reproducibility protocol and
  academic-pipeline integrity discipline
- Origin Mode: deterministic exact-byte control-design amendment
- Origin Date: 2026-08-17
- Verification Status: UNVERIFIED_PENDING_FRESH_INDEPENDENT_REREVIEW
- Version Label: p15r_control_design_amendment_v6
- Scope: only D-M1 causal capabilities, D-M2 actual-FD/quiescence/unwind,
  their exact bounded supersessions, and the append-only successor needed to
  bind this amendment; no implementation, run, result, theorem, Route,
  manuscript, release, or publication claim

## 1. Exact authority, precedence, and complete delta

### 1.1 Complete current-byte authority

Before freezing this amendment, the complete bytes of all thirteen records
below were read and independently re-hashed:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | notes/phase2_control_design_lock.md | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d |
| remediation gate v1 | notes/phase2_control_design_remediation_gate.md | 188 | 7023 | 98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16 |
| design amendment v1 | notes/phase2_control_design_amendment_v1.md | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe |
| remediation gate v2 | notes/phase2_control_design_remediation_gate_v2.md | 405 | 20113 | 00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705 |
| design amendment v2 | notes/phase2_control_design_amendment_v2.md | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea |
| remediation gate v3 | notes/phase2_control_design_remediation_gate_v3.md | 578 | 27299 | e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac |
| design amendment v3 | notes/phase2_control_design_amendment_v3.md | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b |
| remediation gate v4 | notes/phase2_control_design_remediation_gate_v4.md | 645 | 30174 | df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647 |
| design amendment v4 | notes/phase2_control_design_amendment_v4.md | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 |
| remediation gate v5 | notes/phase2_control_design_remediation_gate_v5.md | 839 | 41734 | 55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7 |
| blocked/no-op design amendment v5 | notes/phase2_control_design_amendment_v5.md | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 |
| current final append-only review | notes/phase2_control_design_peer_review.md | 2746 | 143812 | 30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb |
| corrected remediation gate v6 | notes/phase2_control_design_remediation_gate_v6.md | 1252 | 62896 | a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00 |

The review is one append-only byte string.  Its independently recomputed
nested-prefix receipts remain:

~~~text
prefix_lines=2308 prefix_bytes=119250 sha256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
prefix_lines=1910 prefix_bytes=96524 sha256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
prefix_lines=1524 prefix_bytes=74876 sha256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
prefix_lines=1017 prefix_bytes=49358 sha256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
prefix_lines=488 prefix_bytes=22894 sha256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec
~~~

The corrected gate's first 58,261 bytes / 1,140 lines were independently
re-hashed as
`81d5543fdd0acc72122cd9a2171a7354a7d51d7d4a2f2c8f6a78fb12b3af7dcc`.
Its append-only correction adds solely the v4 Section 3.3 FD-5 enum surface:
four exact inherited forms become the ten exact gate-v6 Section 3.2 forms;
there is no eleventh form, FD-5 lifetime change, or other authority change.

The operative repair clauses before this file are base + v1 + v2 + v3 +
v4.  V5 remains a blocked/no-op provenance member.  It contributes no wire
form, state, supersession, or repair.  D-M1 and D-M2 remain open; nothing in
this author document is independent evidence against that verdict.

After this exact file is externally hashed, the versioned design chain is
base + v1 + v2 + v3 + v4 + blocked-v5 + v6.  This file does not embed,
predict, or self-authenticate its own digest.

### 1.2 Exact bounded supersessions

This amendment supersedes only:

1. v2 SESSION_CREATE/SESSION_CREATED shapes and opaque-session state edges,
   plus v4's dynamic-session lookup, to install Section 3's P-issued causal
   capabilities, raw joins, INACTIVE/ACTIVE split, and exact P--G protocol;
2. the exact eight TOP_TEST_CONTROLS post-create non-child FD-4 request
   shapes in Section 3.7, only by appending active_cap as their final field;
3. v2's native x86_64 syscall and P-only pre-suite inventory, only by adding
   getrandom=318, pidfd_open=434, pidfd_getfd=438, and the preflights below;
4. v4 Section 3.1's absolute no-duplicate sentence and the corresponding
   affected exclusive-holder rows in v4 Sections 4.5--4.6, only inside one
   exact quiesced P audit interval and only for the listed child FD4/FD5/FD8
   and proc-selected G-candidate P-local audit duplicates;
5. the closed P--G enum and P-only pre-suite state sequence, only by adding
   the ten session records and four FD-audit records printed below; and
6. v4's review-node successor grammar, only so its active count-five block
   becomes historical and the later active v5 count-six block ends at v6;
   and
7. under the corrected gate addendum, v4 Section 3.3's closed four-form
   FD-5 enum, solely to replace it with the six new Section 3.2 forms plus
   the four byte-identical inherited forms: complete enum ten, never eleven.

The v4 requester FD-5 terminal lifetime is not superseded.  No new FD-5
frame follows the terminal FD-4 reply, and the requester closes original FD
5 at the exact retained edge.  Every omitted base/v1/v2/v3/v4 clause remains
binding; blocked v5 supplies no clause.  No wildcard, optional record,
alternate ABI, fallback, unstated error path, or inferred primitive exists.

### 1.3 Exhaustive operational delta

The complete v6 delta is exhausted by:

~~~text
requester--P FD-5 additions, exactly six:
  SESSION_AUTH_OPEN
  SESSION_AUTH_CHALLENGE
  SESSION_AUTH_REGISTERED
  SESSION_AUTH_RECEIPT
  SESSION_AUTH_ACTIVATED
  SESSION_AUTH_ACTIVE_RECEIPT

P--G session additions, exactly ten:
  SESSION_AUTH_CREATE_GRANTED
  SESSION_AUTH_CREATE_ACCEPTED
  SESSION_AUTH_COMMIT
  SESSION_AUTH_COMMITTED
  SESSION_AUTH_ACTIVE
  SESSION_AUTH_ACTIVE_ACK
  SESSION_AUTH_ABORT
  SESSION_AUTH_ABORTED
  SESSION_AUTH_SESSION_CLOSED
  SESSION_AUTH_CLOSE_ACK

P--G FD-audit additions, exactly four:
  FD_AUDIT_QUIESCE_ENTER
  FD_AUDIT_QUIESCE_ACK
  FD_AUDIT_QUIESCE_EXIT
  FD_AUDIT_QUIESCE_EXIT_ACK

P-issued unpredictable values, exactly three semantic kinds:
  create_cap
  reply_nonce
  active_cap

native x86_64 syscall additions:
  getrandom=318 flags=0
  pidfd_open=434 flags=0
  pidfd_getfd=438 flags=0

P descriptor additions:
  one shared held proc-root FD
  one retained audit pidfd per live child
  four fresh per-row proc directory FDs
  one short-lived child socket duplicate per row
  one short-lived duplicate per selected G socket candidate

state additions:
  P and G auth ledgers printed in Section 3.4
  G_FD_QUIESCED and P FD_AUDIT_ALLOCATION_BARRIER
  monotone audit_epoch, acquisition_serial, pidfd_serial, g_fd_generation

review grammar:
  four existing blocks historical
  one future active v5 count-six block, appended only by fresh reviewer
~~~

No other FD-5/FD-4/P--G form, field, OWNER, ROLE, TARGET, PURPOSE, METHOD,
TRIGGER, DETECTOR, OUTCOME, public exit class, CSV byte, schema, generated
byte, repository path, authority binding, graph node, or edge changes.

## 2. Frozen invariants retained exactly

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

All eight CSV paths and headers, 120 rows and order, 35 explicit negatives,
35 S methods, 28 P methods, 173 method names, nine generated paths, fourteen
authority bindings, manifest keys/schema, and A,D,R,G,I,C,M,V graph with
twelve distinct edges remain exact.  Every v6 capability, nonce, digest,
state, pidfd, proc FD, duplicate, transcript, and receipt is operational,
in-memory, and nonserialized.

## 3. D-M1 — P-issued causal capabilities and ACTIVE gate

### 3.1 Sole entropy source, exact fill, and secret boundary

The sole entropy primitive is the byte-bound native Linux x86_64 call:

~~~text
getrandom(buffer,32,flags=0), syscall number 318
ABI=native x86_64 little-endian LP64
~~~

P owns the buffer and issuer.  L, G, requester, worker, libc, runtime header,
helper, service, timestamp, PID, counter, deterministic digest,
/dev/urandom, alternate architecture, x32 branch, and fallback never supply
entropy.  The x32 dispatch bit remains killed.

P fills offsets [0,32) exactly.  A positive return r with
0<r<=remaining advances only by r and calls the same syscall on the unchanged
suffix.  EINTR retries only that suffix.  Zero, a return greater than the
remaining length, any other errno, or incomplete aggregate fill is terminal.
No draw is retried as a new value.

Before any package, result, package-lock, private generation-root,
generated-member, or subject write, P performs one call sequence under the
final nested-security runtime state.  Its exact 32 bytes are entered only in
a PREFLIGHT_ONLY tombstone namespace, retained as raw P-only tombstone bytes
through complete P teardown, and never used as a capability.  Failure is
E_POSSESSION_UNAVAILABLE under retained bootstrap containment.  It creates
no child, target, method, or serialized record.

Each later causal draw yields exactly 32 bytes and is encoded as exactly 64
lowercase hexadecimal digits.  Before disclosure, P compares the complete
32 raw bytes with every still-retained live or tombstoned 32-byte value of
every D-M1 namespace: PREFLIGHT_ONLY, create_cap, reply_nonce, and
active_cap.  This is raw equality, never digest equality.  Every raw value
therefore remains in P-only memory until complete P teardown; equality is a
terminal collision and there is no redraw.  The three capability kinds
remain exactly create_cap, reply_nonce, and active_cap; PREFLIGHT_ONLY is an
availability receipt, not a fourth capability.

The raw bytes are requester-inaccessible before their stated edge.  They
may not appear early in a CSV, manifest, result, log, diagnostic, exception,
environment, argv, pathname, G reply, requester-readable record, or public
field.  “Unforgeable” means a P-generated 256-bit value unavailable on every
permitted requester input before disclosure and accepted only by exact raw
equality in its bound endpoint/state.  A predictable public digest is never
a capability.  A guessed or wrong value consumes the relevant attempt and
aborts; guessing is not a transition.

The semantic roles are exact:

1. create_cap is one-use, first disclosed only in the complete
   SESSION_AUTH_RECEIPT, and required in the first actual SESSION_CREATE;
2. reply_nonce is one-use, given only to G in SESSION_AUTH_COMMIT and first
   requester-disclosed only by the actual SESSION_CREATED reply; and
3. active_cap is minted only after P joins the actual reply echo to G's
   committed transcript, is first requester-disclosed in
   SESSION_AUTH_ACTIVE_RECEIPT, and is a session-scoped operation capability,
   not falsely labelled one-use.

### 3.2 Complete requester--P FD-5 grammar

The complete FD-5 payload enum is exactly ten forms.  The six additions are:

~~~text
requester -> P:
SESSION_AUTH_OPEN audit=DEC auth_serial=DEC request=DEC method=METHOD trigger=TRIGGER owner=OWNER

P -> requester:
SESSION_AUTH_CHALLENGE audit=DEC auth_serial=DEC auth=DEC session=DEC

requester -> P:
SESSION_AUTH_REGISTERED audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC method=METHOD trigger=TRIGGER owner=OWNER registration=LOWERHEX digest=LOWERHEX64

P -> requester:
SESSION_AUTH_RECEIPT audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC digest=LOWERHEX64 create_cap=LOWERHEX64 create=LOWERHEX

requester -> P:
SESSION_AUTH_ACTIVATED audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC reply_nonce=LOWERHEX64 created=LOWERHEX

P -> requester:
SESSION_AUTH_ACTIVE_RECEIPT audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC active_cap=LOWERHEX64 created_digest=LOWERHEX64
~~~

The four byte-identical v4 child-request forms remain:

~~~text
requester -> P:
AUDIT_OPEN audit=DEC serial=DEC

P -> requester:
AUDIT_CHALLENGE audit=DEC serial=DEC nonce=LOWERHEX64

requester -> P:
AUDITED_SPAWN audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64 trigger=TRIGGER core=LOWERHEX

P -> requester:
AUDIT_RECEIPT audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64
~~~

There is no eleventh form and no post-SESSION_CLOSED FD-5 auth exchange.
Each payload is one complete canonical ASCII seqpacket of at most 4096
bytes, with no NUL, LF, separate length, rights, explicit credentials,
other cmsg, or trailing byte.  Requester uses plain send; success is exactly
the complete byte length.  P uses recvmsg and requires exactly one kernel-
supplied SCM_CREDENTIALS; registered outer PID and uid/gid 65534/65534;
normalized inner PID and uid/gid 0/0; retained pidfd, start time, full NSpid,
cgroup, role, child, audit, and endpoint identity; no other cmsg; and neither
MSG_TRUNC nor MSG_CTRUNC.  P replies use plain send and no ancillary item.

DEC, LOWERHEX, LOWERHEX64, METHOD, TRIGGER, OWNER, and the unchanged child-
audit grammars retain their exact closed definitions.  auth_serial is
P-owned per audit endpoint, starts at zero, advances exactly once after each
terminal registration attempt, and has one open value.  auth and nonzero
session are P-owned globally monotone values and are never reused.  P derives
OWNER from the exact 173-method table and requires the exact next request,
method/trigger/owner/creator tuple.  G and the current child request never
supply an expected coordinate.

registration decodes to exactly:

~~~text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC
~~~

registration_digest is exactly:

~~~text
SHA256(ASCII("P15R-SESSION-REGISTERED-v6") || ASCII(" ") || exact_registration_bytes)
~~~

P canonical-decodes registration, recomputes the digest, and binds the
complete direct packet hash, credentials/endpoint, audit, auth_serial, auth,
session, request, method, trigger, owner, and exact registration bytes.  It
then draws create_cap and constructs exactly:

~~~text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC create_cap=LOWERHEX64
~~~

Only after the complete CREATE_GRANTED send succeeds does P disclose
create_cap and the exact final create bytes in SESSION_AUTH_RECEIPT.  A
pre-receipt queued request cannot contain that value.  The first actual
FD-4 create attempt for the bound endpoint/auth/session/request consumes
create_cap whether correct, malformed, wrong, duplicate, or cross-bound; it
has no retry.

### 3.3 Complete P--G session grammar and digest definitions

The closed P--G protocol adds exactly these ten session records:

~~~text
P -> G:
SESSION_AUTH_CREATE_GRANTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC registration_digest=LOWERHEX64 create_cap=LOWERHEX64 payload=LOWERHEX

G -> P:
SESSION_AUTH_CREATE_ACCEPTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC registration_digest=LOWERHEX64 create_cap_sha256=LOWERHEX64 payload=LOWERHEX

P -> G:
SESSION_AUTH_COMMIT requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC reply_nonce=LOWERHEX64 created=LOWERHEX

G -> P:
SESSION_AUTH_COMMITTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC reply_nonce=LOWERHEX64 created=LOWERHEX

P -> G:
SESSION_AUTH_ACTIVE requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC active_cap=LOWERHEX64 created_digest=LOWERHEX64

G -> P:
SESSION_AUTH_ACTIVE_ACK requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC active_cap_sha256=LOWERHEX64 created_digest=LOWERHEX64

P -> G:
SESSION_AUTH_ABORT requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC phase=AUTH_PHASE reason=AUTH_REASON

G -> P:
SESSION_AUTH_ABORTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC phase=AUTH_PHASE reason=AUTH_REASON outcome=OUTCOME

G -> P:
SESSION_AUTH_SESSION_CLOSED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME

P -> G:
SESSION_AUTH_CLOSE_ACK requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME
~~~

Each record has exactly the printed direction and fields and is one
canonical payload under the unchanged four-byte unsigned big-endian length
and 4096-byte payload ceiling.  It has no ancillary item or trailing byte;
complete send means exactly prefix plus payload was sent under the retained
control-channel contract.  Each exact record occurs at most once.  Missing,
duplicate, stale, reordered, malformed, wrong-direction, cross-endpoint,
wrong-identity, wrong-transcript, or wrong-state input is terminal.

payload is lowercase hex of the complete actual capability-bearing create
bytes.  created is lowercase hex of exactly:

~~~text
SESSION_CREATED request=DEC session=DEC reply_nonce=LOWERHEX64
~~~

The domain-separated digests are exactly:

~~~text
registration_digest = SHA256(ASCII("P15R-SESSION-REGISTERED-v6") || ASCII(" ") || exact_registration_bytes)
create_cap_sha256    = SHA256(ASCII("P15R-CREATE-CAP-v6") || ASCII(" ") || raw_create_cap_32_bytes)
reply_nonce_sha256   = SHA256(ASCII("P15R-REPLY-NONCE-v6") || ASCII(" ") || raw_reply_nonce_32_bytes)
created_digest       = SHA256(ASCII("P15R-SESSION-CREATED-v6") || ASCII(" ") || exact_created_bytes)
activation_digest    = SHA256(ASCII("P15R-SESSION-ACTIVATED-v6") || ASCII(" ") || exact_SESSION_AUTH_ACTIVATED_bytes)
active_cap_sha256    = SHA256(ASCII("P15R-ACTIVE-CAP-v6") || ASCII(" ") || raw_active_cap_32_bytes)
~~~

Here `||` is byte concatenation; ASCII literals contain no NUL or LF.  The
hashes bind or tombstone values but never substitute for raw capability
equality.  The raw-value ledger also compares a new 32-byte value against
all live and raw-tombstoned values before complete teardown; digest
comparison never authorizes a value.

AUTH_PHASE is exactly:

~~~text
REGISTERED | CREATE_GRANTED | CREATE_ACCEPTED | INACTIVE_COMMITTED |
ACTIVATION_JOINED | ACTIVE_RECEIPT_SENT | ACTIVE_PENDING | ACTIVE | CLOSING
~~~

AUTH_REASON is exactly:

~~~text
RECEIPT_SEND | REQUESTER_EOF | CREATE_MISMATCH | CREATE_ACCEPTED_SEND |
COMMIT_SEND | PRIVATE_CONSTRUCTION | CREATED_SEND | COMMITTED_SEND |
ACTIVATION_MISMATCH | ACTIVE_RECEIPT_SEND | ACTIVE_SEND |
ACTIVE_ACK_SEND | PREACTIVE_OPERATION | ACTIVE_OPERATION_MISMATCH |
SESSION_CLOSE_FAILURE | CONTROL_EOF
~~~

The continuation lines above are presentational; each enum is the literal
closed set.  These operational tokens add no public detector or exit class.

### 3.4 Exact causal production and ACTIVE sequence

The sole successful sequence is:

1. P validates the direct SESSION_AUTH_REGISTERED bytes, draws create_cap,
   stores their immutable binding, and completely sends
   SESSION_AUTH_CREATE_GRANTED to G.
2. Only after that send succeeds does P completely send
   SESSION_AUTH_RECEIPT.  Before receiving that exact packet the requester
   cannot know create_cap or construct the accepted final create bytes.
3. G installs the grant before dequeuing any FD-4 create.  It then receives
   exactly the first create packet, applies the retained endpoint,
   credential, pidfd, request-number, role, and session-zero checks, consumes
   the one-use create_cap, requires raw equality with the grant, creates no
   private object, and completely sends SESSION_AUTH_CREATE_ACCEPTED.
4. P compares the actual payload bytes and create-cap digest with its direct
   registration, grant, and raw capability; joins every immutable coordinate;
   draws reply_nonce; constructs the sole exact created bytes; and completely
   sends SESSION_AUTH_COMMIT.
5. Only that commit permits G to create the bounded copied-package and lock-
   parent objects for an INACTIVE session.  Every actual G-created object
   still completes the v3 pre-access OBJECT_REGISTERED, independent P
   validation, and ACK barrier.  G then completely sends the actual
   SESSION_CREATED reply to the requester; only after that send succeeds does
   it completely send SESSION_AUTH_COMMITTED with the identical raw created
   bytes and tuple.
6. The requester learns reply_nonce only from that actual reply and sends
   SESSION_AUTH_ACTIVATED containing the exact nonce and raw reply hex.  P
   requires its direct credential/endpoint, parses the raw reply, and joins
   it to the commit and committed record.  Because G sends the actual reply
   before COMMITTED, P may retain exactly one otherwise valid activation
   packet in its bounded `activation_hold=HELD` slot until the already causal
   committed record arrives.  This does not add a state: P remains exactly
   CREATE_ACCEPTED and stores the packet in one separate bounded
   `activation_hold` slot.  The slot is initially EMPTY, can become HELD
   exactly once, and is cleared only by the matching COMMITTED join or
   abort.  On the matching record P takes the exact consecutive transitions
   CREATE_ACCEPTED -> INACTIVE_COMMITTED -> ACTIVATION_JOINED.  It performs
   no authorization, mint, or other action while held; an extra packet,
   replacement, mismatch, EOF, or terminal transition aborts and clears the
   slot without minting.
7. Only the completed two-input join permits P to draw active_cap.  P first
   completely sends SESSION_AUTH_ACTIVE_RECEIPT, the sole first requester
   disclosure.  Only after that send succeeds does P completely send
   SESSION_AUTH_ACTIVE to G and enter ACTIVE_PENDING.
8. G validates the complete binding, completely sends
   SESSION_AUTH_ACTIVE_ACK, and changes its own session to ACTIVE only after
   the ACK send succeeds.  P remains ACTIVE_PENDING until it receives and
   validates that exact ACK, then enters its own ACTIVE state.  G's
   acceptance gate is its completed ACK send and its own ACTIVE state; it
   does not and cannot infer whether P has already dequeued the ACK, and no
   eleventh acknowledgement is added.  Before G's own transition it does not
   receive, dequeue, parse, reserve, execute, mutate for, or reply to any
   post-create FD-4 operation.

Queue readiness is never acceptance.  A capability-bearing operation may be
queued after the requester receives the active receipt while G is still
ACTIVE_PENDING; G leaves it queued until the ACTIVE/ACK transition completes.
An older packet cannot gain a missing capability by waiting.

Normal close remains on FD 4.  In ACTIVE, G validates the capability-bearing
SESSION_CLOSE, enters CLOSING, closes admission, completes the retained
child/root/lock terminal proofs, and completely sends
SESSION_AUTH_SESSION_CLOSED to P before the requester reply.  P validates the
exact active mapping, close request, outcome, object ledger, and terminal
proof, then completely sends SESSION_AUTH_CLOSE_ACK.  Only after that ACK
succeeds may G completely send the unchanged terminal
`SESSION_CLOSED request=DEC session=DEC outcome=OUTCOME`.  P and G then enter
CLOSED_TOMBSTONE, and the requester closes FD 5 at the unchanged v4 post-
terminal-reply edge.  No post-reply FD-5 packet exists.

### 3.5 Exact P/G ledgers, binding, erasure, and tombstones

P's state is exactly:

~~~text
UNSEEN
  -> CHALLENGE_ISSUED
  -> REGISTERED
  -> CREATE_GRANTED
  -> CREATE_ACCEPTED
  -> INACTIVE_COMMITTED
  -> ACTIVATION_JOINED
  -> ACTIVE_RECEIPT_SENT
  -> ACTIVE_PENDING
  -> ACTIVE
  -> CLOSING
  -> CLOSED_TOMBSTONE

any nonterminal state -> ABORTING -> FAILED_TOMBSTONE
~~~

G's state is exactly:

~~~text
NO_SESSION
  -> CREATE_ARMED
  -> CREATE_HELD
  -> INACTIVE
  -> ACTIVE_PENDING
  -> ACTIVE
  -> CLOSING
  -> CLOSED_TOMBSTONE

any nonterminal state -> ABORTING -> FAILED_TOMBSTONE
~~~

P's successful edges are challenge send, direct registration validation,
complete grant send, exact CREATE_ACCEPTED join, complete COMMIT send, valid
COMMITTED plus direct activation join, complete ACTIVE_RECEIPT send, complete
ACTIVE send, valid ACTIVE_ACK, valid close report, and complete CLOSE_ACK.
If COMMITTED arrives with an EMPTY activation_hold, P moves from
CREATE_ACCEPTED to INACTIVE_COMMITTED and waits; the one valid later direct
activation moves it to ACTIVATION_JOINED.  If the valid activation arrives
first, P remains CREATE_ACCEPTED with the sole HELD slot; matching COMMITTED
then causes the two consecutive transitions printed in Section 3.4.  No
other state, flag, or readiness order advances either path.
G's successful edges are grant install, exact first-create consumption,
complete accepted report, valid commit plus bounded construction, complete
created and committed sends, valid ACTIVE plus complete ACK, exact active
operations, and close report/ACK/reply.  No receive timeout, EOF, queue
readiness, or G assertion advances a success edge.

Both ledgers bind requester child, audit endpoint, outer/inner credentials,
pidfd/start-time/NSpid/cgroup identity; auth_serial, auth, session, request;
method, trigger, P-derived owner; exact direct registration, actual create,
created, and activation packet hashes; all six domain-separated digests;
and the private object/session handles.  Expected coordinates always come
from P's immutable direct record.  A G record supplies actual values only.

create_cap and reply_nonce each have one legal consumption.  Wrong,
premature, cross-bound, duplicate, delayed, guessed, or replayed use consumes
the attempt and aborts.  active_cap is bound to one ACTIVE session, creator
endpoint, and immutable tuple.  It may authorize that session's distinct
strictly increasing request numbers, never another endpoint/session/method/
trigger/owner or a post-close request.  It is not transferable.

On close or abort, each side retains at least

~~~text
auth, session, creation request, endpoint identity, terminal cause,
registration_digest, create_cap_sha256, reply_nonce_sha256,
created_digest, activation_digest, active_cap_sha256
~~~

through complete P/G teardown.  P retains the raw PREFLIGHT_ONLY,
create_cap, reply_nonce, and active_cap bytes in P-only live/tombstone memory
until complete P teardown so every later draw can be compared by exact raw
equality.  G retains only the raw values disclosed to it by the legal grant,
commit, and ACTIVE edges and keeps them through complete G teardown.  After
terminal state and every required digest are fixed, complete teardown
overwrites each retained raw buffer exactly once; no earlier erase is legal.
No auth, session, request, nonce, capability, raw value, or tombstoned tuple
is recycled.  EOF never synthesizes a receipt, ACK, close, or tombstone
erasure.

`OUTCOME` remains exactly the complete inherited enum, including UNSET, and
retains every inherited state-dependent meaning; v6 adds, removes, or
reinterprets no token and defines no narrower subset.  Each auth record must
carry the exact already-computed inherited outcome for that session/object
state.  Thus an honest no-lock/no-root close or pre-construction abort may
remain UNSET where the inherited machine yields UNSET; ABSENT is legal only
after the complete inherited owned-object-gone proof; and a foreign object
is never deleted or relabelled absent.  SESSION_AUTH_CLOSE_ACK echoes the
exact accepted close OUTCOME.  ABORT binds only its printed tuple, phase, and
reason before cleanup; ABORTED alone reports the exact later reachable
OUTCOME.  No auth record chooses, upgrades, normalizes, or turns an error or
crash receipt into success.

### 3.6 Total send-failure, abort, and cleanup table

The exact failure transitions are:

| First failing edge | Mandatory transition before later action |
|---|---|
| PREFLIGHT_ONLY fill/collision | before any auth child or write, P retains the exact partial-fill failure receipt or complete colliding raw value P-only through teardown, invokes bootstrap containment, and returns E_POSSESSION_UNAVAILABLE; no auth record exists |
| SESSION_AUTH_CHALLENGE incomplete send | P has not completed the UNSEEN -> CHALLENGE_ISSUED success edge; it instead takes UNSEEN -> ABORTING -> FAILED_TOMBSTONE locally, tombstones the allocated auth/session coordinates, closes this FD5 authorization admission and contains the requester, sends no P--G ABORT because G has no auth state, and never retries |
| create_cap fill/collision after registration | P takes REGISTERED -> ABORTING -> FAILED_TOMBSTONE locally, retains the exact partial-fill failure receipt or complete colliding raw value plus registration tuple, sends neither CREATE_GRANTED nor requester receipt nor ABORT because G has no auth state, closes this authorization admission, and never retries |
| create grant incomplete | P takes its nonterminal state -> ABORTING -> FAILED_TOMBSTONE, closes the failed control admission, sends no requester receipt or retry, and relies on control-EOF containment rather than a second frame on the failed send edge |
| grant complete, requester receipt incomplete | P enters ABORTING and sends ABORT; G discards grant or held packet; both tombstone; no construction |
| requester EOF after receipt | P sends ABORT; any held create is discarded and cannot commit |
| requester remains live but sends nothing | state makes no progress; no liveness success and no invented timeout |
| first actual create malformed/wrong/duplicate | G consumes the attempt, creates no object, enters ABORTING, and reports CREATE_MISMATCH in ABORTED |
| CREATE_ACCEPTED send incomplete | G creates no object, takes CREATE_HELD -> ABORTING -> FAILED_TOMBSTONE locally, closes admission/control, and invokes containment |
| reply_nonce fill/collision after CREATE_ACCEPTED | P retains the exact partial-fill failure receipt or complete colliding raw value, enters ABORTING at phase CREATE_ACCEPTED, and sends ABORT with reason COMMIT_SEND; G discards the held create, constructs nothing, terminally reports ABORTED if control remains usable, and neither side retries or sends COMMIT |
| COMMIT send/validation fails | held create is discarded; no construction; P/G abort without retry |
| private construction or required object registration fails | G enters ABORTING, closes admission, unconditionally removes every object it created, then may send ABORTED |
| actual SESSION_CREATED send incomplete | session remains INACTIVE, G aborts and cleans; requester does not receive a valid reply nonce; P mints no active_cap |
| COMMITTED send incomplete after reply | requester may know reply_nonce, but P cannot complete the two-input join; G aborts INACTIVE state; no active_cap is minted |
| activation missing | state makes no progress and creates no success; EOF invokes abort |
| activation premature/malformed/duplicate/wrong | P enters ABORTING; G stays INACTIVE and processes no later request |
| active_cap fill/collision after ACTIVATION_JOINED | P retains the exact partial-fill failure receipt or complete colliding raw value, enters ABORTING at phase ACTIVATION_JOINED, and sends ABORT with reason ACTIVE_RECEIPT_SEND; G remains INACTIVE, admits no operation, performs retained private-object cleanup, and neither receipt nor ACTIVE is sent |
| ACTIVE_RECEIPT send incomplete | active_cap never becomes operational; P sends no ACTIVE and aborts |
| ACTIVE send incomplete/invalid | G remains INACTIVE or ACTIVE_PENDING, processes no later request, and P aborts |
| ACTIVE_ACK send incomplete | G does not enter ACTIVE, aborts and cleans; P cannot treat timeout/EOF as ACK |
| non-create FD-4 readiness before ACTIVE | G leaves endpoint unpolled; a forced receive is PREACTIVE_OPERATION failure before any mutation |
| active_cap/endpoint/request binding fails | no requested mutation occurs; G aborts with ACTIVE_OPERATION_MISMATCH; request cannot retry |
| close report, CLOSE_ACK, or terminal reply fails | cleanup still completes; both use failed tombstones, not successful close; no capability is reused |
| ABORT or ABORTED send incomplete | each side completes locally possible cleanup, closes control, and invokes retained freeze/kill/reap/cgroup containment; missing record is never success evidence |
| P--G control EOF in any nonterminal state | each side fixes CONTROL_EOF failure and closes admission; G seeing P EOF performs no pathname deletion and exits CRASH_TEARDOWN; P seeing G EOF uses retained cgroup kill/reap/populated-zero containment; neither emits PASS or ABSENT |

Every send accepts only a complete payload-length return and is attempted at
most once.  A P-detected failure uses P-to-G SESSION_AUTH_ABORT only when G
has already installed the matching auth state and the control channel
remains usable.  Incomplete CHALLENGE, pre-grant create_cap failure, and
incomplete CREATE_GRANTED have no such G state and take only their exact
local/control-EOF rows above; they never fabricate ABORT.  G-detected failure
enters ABORTING locally,
completes all reachable cleanup, and sends SESSION_AUTH_ABORTED with the
actual phase/reason; it need not fabricate a preceding P ABORT.  In the
P-initiated case ABORTED is the single response after reachable private state
is terminal.  Duplicate ABORT/ABORTED or a reason/phase mismatch is fatal.
The two entropy-to-abort mappings above consume existing closed AUTH_REASON
tokens by their next impossible send edge; they add no entropy reason.  Every
complete colliding raw draw remains in P's raw-
tombstone set through teardown; every incomplete fill retains its exact
partial length/bytes and errno coordinate P-only through teardown.  Neither
path permits redraw or reuse.

Before cleanup G enters ABORTING, closes admission, rejects queued frames,
starts no operation, kills/reaps controlled children where applicable, and
uses only retained capability-relative root/lock cleanup.  ABORTED is legal
only after reachable private state is terminal.  If its delivery fails,
crash-containment evidence substitutes for no missing receipt and cannot
yield PASS, ABSENT, or successful close.

### 3.7 Exact active capability on later operations

SESSION_CREATE is the sole creator request permitted before ACTIVE; its only
pre-ACTIVE effect is bounded INACTIVE construction.  On the
TOP_TEST_CONTROLS creator endpoint the eight changed request forms are
exactly:

~~~text
LOCK_ACQUIRE request=DEC session=DEC active_cap=LOWERHEX64
LOCK_RELEASE request=DEC session=DEC lock=DEC active_cap=LOWERHEX64
ROOT_CREATE request=DEC session=DEC purpose=PURPOSE active_cap=LOWERHEX64
ROOT_VALIDATE request=DEC session=DEC handle=DEC active_cap=LOWERHEX64
INJECT_EXCHANGE request=DEC session=DEC handle=DEC trigger=TRIGGER active_cap=LOWERHEX64
CLEAN request=DEC session=DEC handle=DEC active_cap=LOWERHEX64
FOREIGN_AUDIT request=DEC session=DEC handle=DEC active_cap=LOWERHEX64
SESSION_CLOSE request=DEC session=DEC active_cap=LOWERHEX64
~~~

The appended field is last.  Replies remain byte-identical.  No other
creator non-child request exists or changes.  G requires exact raw
active_cap equality, ACTIVE state, creator endpoint, immutable method/
trigger/owner/session mapping, exact next request number, and the retained
per-operation predicates before it accepts or mutates.  A pre-created packet
cannot contain active_cap; waiting cannot change its bytes.

AUDITED_SPAWN remains the sole child-creating form and retains v4's P nonce,
direct raw bytes, G actual bytes, exact P join, confirmation, and admission.
P issues AUDIT_RECEIPT only for an ACTIVE parent mapping.  A delegated
requester endpoint cannot be allocated, transferred, or bound before that
parent is ACTIVE.  Its immutable mapping carries the same active session;
its existing request shapes remain unchanged, but G rechecks that parent
ACTIVE state before every delegated non-child request.  There is no hostile
pre-ACTIVE delegated endpoint and no wildcard exemption.

### 3.8 Mandatory D-M1 hostile pairs

The frozen receipts preserve distinct predicates for later attack of at
least:

1. identical public registration with create queued before versus after
   receipt of create_cap;
2. predictable request/session decimals with activation queued before versus
   after receipt of actual SESSION_CREATED(reply_nonce);
3. an early creator operation without active_cap versus the post-ACTIVE
   capability-bearing operation;
4. a byte-correct G table with no direct requester registration;
5. a changed method, trigger, owner, endpoint, session, transcript, or private
   G tuple under the same later child request;
6. create_cap, reply_nonce, active_cap, or request number replayed across a
   session or after close; and
7. each receipt/accepted/commit/reply/ACTIVE/ACK/abort send failure in the
   total table.

The predicate must differ without requester obedience, G trust, queue/poll
order, public digest, current child-request tautology, or an unperformed
operation.

## 4. D-M2 — actual-FD acquisition, G quiescence, and total unwind

### 4.1 Sole syscall ABI and bounded temporary-holder exception

The sole foreign-descriptor acquisition calls are the byte-bound native
Linux x86_64 little-endian LP64 syscalls:

~~~text
pidfd_open(outer_pid,flags=0), syscall number 434
pidfd_getfd(pidfd,targetfd,flags=0), syscall number 438
~~~

Every argument is exactly as printed.  The x32 dispatch bit remains killed.
No libc/header-selected number, other architecture, helper, service,
SCM_RIGHTS, kcmp, ptrace attachment, pathname-following stat, or alternate
primitive exists.  A successful call returns a nonnegative P-local FD and P
immediately requires `fcntl(fd,F_GETFD)=FD_CLOEXEC` exactly.  Extra flag
bits, a missing CLOEXEC bit, a short/ambiguous binding, or any errno is
fatal.  Actual successful `pidfd_getfd` under the kernel's
`PTRACE_MODE_ATTACH_REALCREDS` check is the permission preflight; uid,
capability, kernel version, proc readability, LSM text, and ptrace_scope do
not infer permission.  There is no fallback.

The inherited permanent holder matrix is superseded only during the exact
interval below for the exact P-local socket duplicates listed in the row.
For requester FD 5 that interval is:

~~~text
FD_AUDIT_QUIESCED
  -> pidfd_getfd(exact_child_pidfd,5,0)
  -> F_GETFD/fstat/proc/reciprocal-diag comparison
  -> close(the exact P-local duplicate)
  -> immediate fcntl(the same number,F_GETFD)=-1/EBADF
  -> FD_AUDIT_EXIT_ACKED
~~~

Throughout it the child retains original FD 5, P retains the sole opposite
audit peer, and P holds at most one additional audit duplicate of that child
endpoint.  The duplicate is used only for F_GETFD, fstat, nonmutating type/
inode comparison, and derivation of its diag query inode.  It is never read,
written, sent, received, polled for payload, transferred, re-duplicated, or
retained across EXIT_ACK or the original close.  The requester still closes
original FD 5 only after its retained terminal FD-4 reply.

The identical audit-only temporary-holder rule applies to the selected child
slot 4 or 8 and to each proc-selected G socket candidate.  It changes no
permanent holder, FDSET, child admission, endpoint ownership, terminal
lifetime, or serialized count.  Outside one open audit interval every
inherited sole-holder and no-duplicate predicate is exact again.

### 4.2 Closed row table and descriptor-lifetime ledgers

`SLOT` is exactly `FD4|FD5|FD8`; `AUDIT_KIND` is exactly
`PREFLIGHT_PROBE|RUNTIME_CHILD`.  One fresh monotone nonzero `audit_epoch`
selects exactly one row and one registered child; no wildcard or union row
exists:

| AUDIT_KIND | SLOT | retained child pidfd | retained guardian pidfd | fresh child PID/fd proc dirs | fresh G PID/fd proc dirs | P opposite peer |
|---|---|---:|---:|---:|---:|---:|
| PREFLIGHT_PROBE | FD8 | 1 | 1 | 1 / 1 | 1 / 1 | 0 |
| RUNTIME_CHILD | FD8 | 1 | 1 | 1 / 1 | 1 / 1 | 0 |
| RUNTIME_CHILD | FD4 | 1 | 1 | 1 / 1 | 1 / 1 | 0 |
| RUNTIME_CHILD | FD5 | 1 | 1 | 1 / 1 | 1 / 1 | 1 |

The PREFLIGHT_PROBE row uses only the existing epoch-1
CGROUP_PROBE_CHILD, already blocked at FD 8.  It adds no child, target,
method, probe epoch, session-zero row, or public result.  Its complete
quiesce, two snapshots, acquisitions, fstats, reciprocal diag, total unwind,
EBADF proofs, holder restoration, and EXIT_ACK must succeed under the final
nested uid/gid maps, credentials, dumpable-zero setting, and cgroup state
before any package, result, package-lock, private generation-root,
generated-member, or subject write.  Failure uses retained bootstrap
kill/reap/populated-zero containment and returns
E_POSSESSION_UNAVAILABLE; no downgrade is legal.

The rows occur at every inherited v4 live-pair audit, not merely once per
child.  PREFLIGHT_PROBE/FD8 is used only for the epoch-1 probe and includes
its first pre-write availability row.  RUNTIME_CHILD/FD8 is used for every
other child at each registered and SOURCE_READY audit while FD8 is live.
RUNTIME_CHILD/FD4 and RUNTIME_CHILD/FD5 are used only for TOP_TEST_CONTROLS
and COPIED_REPRODUCE at registered, SOURCE_READY, and every later running or
frozen reference audit while that exact endpoint remains live.  When more
than one slot is live at one phase, the rows are complete and sequential in
the exact order FD8, FD4, FD5; after FD8's authorized close only FD4 then
FD5 remain.  No row is run for an absent or already-authorized-closed slot,
and every row receives a fresh audit_epoch.

P opens exactly one child pidfd with `pidfd_open(exact_outer_pid,0)` after
the child's first-instruction identity receipt and while the child remains
blocked.  Immediately before and after the call it joins the canonical outer
PID, start time, full NSpid vector, real/effective/saved/filesystem uid/gid,
one-thread state, exact child/session/role/owner, and workers-cgroup
membership.  A returned pidfd is inserted immediately in the distinct
`PIDFD_LIFETIME_LEDGER` before any validation that can fail.  A validated
child pidfd is retained through every row, EXIT_ACK, child exit, wait/reap,
and CHILD_REAPED reconciliation; it is then closed exactly once and, without
an intervening FD allocation, proved absent by exact F_GETFD=-1/EBADF.  A
returned pidfd followed by any failed validation is closed and proved absent
on that same failure path.  The ledger states are exactly
`RETURNED|VALIDATED|CLOSED_PROVED` plus terminal `AMBIGUOUS_CRASH_ONLY`.

The guardian pidfd is the one already authenticated P-held guardian
capability.  It is never re-opened per row and retains its existing lifetime
through G reap.  At each row P revalidates its outer PID, start time, full
NSpid, credentials, one-thread state, and guardian-cgroup membership.  A
child pidfd never names G and a guardian pidfd never names a child.

Each `PIDFD_LIFETIME_LEDGER` entry is exactly

~~~text
(pidfd_serial,local_fd,subject,outer_pid,start_time,nspid_sha256,
 credential_sha256,cgroup_dev,cgroup_ino,state)
~~~

where `subject` is exactly `CHILD|GUARDIAN`; CHILD is one entry per live
registered child and GUARDIAN is the single inherited entry.  Identity bytes
have two exact kind-specific one-line ASCII preimages.  Every field is
`name=value`, fields are joined by one ASCII space, there is no NUL/LF or
trailing byte, every decimal is canonical unsigned decimal, and the order is
exactly:

~~~text
CHILD:
subject=CHILD outer_pid=DEC start_time=DEC nspid=VECTOR outer_ruid=DEC outer_euid=DEC outer_suid=DEC outer_fsuid=DEC outer_rgid=DEC outer_egid=DEC outer_sgid=DEC outer_fsgid=DEC inner_ruid=DEC inner_euid=DEC inner_suid=DEC inner_fsuid=DEC inner_rgid=DEC inner_egid=DEC inner_sgid=DEC inner_fsgid=DEC outer_groups=GROUPS inner_groups=GROUPS threads=1 session=DEC child=DEC role=ROLE owner=OWNER cgroup_dev=DEC cgroup_ino=DEC

GUARDIAN:
subject=GUARDIAN outer_pid=DEC start_time=DEC nspid=VECTOR outer_ruid=DEC outer_euid=DEC outer_suid=DEC outer_fsuid=DEC outer_rgid=DEC outer_egid=DEC outer_sgid=DEC outer_fsgid=DEC inner_ruid=DEC inner_euid=DEC inner_suid=DEC inner_fsuid=DEC inner_rgid=DEC inner_egid=DEC inner_sgid=DEC inner_fsgid=DEC outer_groups=GROUPS inner_groups=GROUPS threads=1 guardian_pidfd_serial=DEC cgroup_dev=DEC cgroup_ino=DEC
~~~

`VECTOR` is the nonempty full NSpid sequence in kernel-printed outer-to-inner
order, with canonical decimals joined by one ASCII comma and no space.
`GROUPS` is exactly the literal `NONE` because the frozen supplementary set
is empty; no alternate list or wildcard is legal.
All outer values are P's initial-namespace observations; all inner values are
the independently map-normalized values.  `start_time` is the retained
canonical `/proc/PID/stat` clock-tick integer.  The child cgroup is the exact
workers cgroup; the guardian cgroup is the exact guardian cgroup.  ROLE and
OWNER are the already closed tokens and session/child are the registered
values, including zero where exact.

For either kind let `identity_bytes` be its complete line above and
`nspid_bytes` be exactly `subject=CHILD|GUARDIAN nspid=VECTOR` with the
applicable literal subject.  The ledger digests are exactly:

~~~text
nspid_sha256 = SHA256(ASCII("P15R-PIDFD-NSPID-v6") || ASCII(" ") || nspid_bytes)
credential_sha256 = SHA256(ASCII("P15R-PIDFD-CREDENTIAL-v6") || ASCII(" ") || identity_bytes)
identity_sha256 = SHA256(ASCII("P15R-PROC-IDENTITY-v6") || ASCII(" ") || identity_bytes)
~~~

Tag 3/4 uses the CHILD identity_sha256; tag 5/6 uses the GUARDIAN
identity_sha256; tag 17 recomputes those same two preimages after snapshot 2
and requires byte equality.  No alternate digest preimage exists.  These
digests are bindings, never identity substitutes; P still performs every
actual value join before hashing.

P separately owns exactly one `LONG_LIVED_PROC_ROOT` descriptor.  Before
the preflight child exists it opens literal `/proc` once with exactly
`O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC`, fstats directory type, requires
exact FD_CLOEXEC, records its device/inode identity, and prevents its
inheritance by L, G, or any child.  It is never duplicated, serialized, or
used except as the starting dirfd for the per-row PID-directory opens below.
It is not one of the four fresh per-row proc FDs, never enters the audit-
owned acquisition ledger, and is explicitly excluded from the common row
unwind and from every rule saying a per-row proc FD may not cross EXIT_ACK.
It remains live through the final endpoint audit.  Only on orderly P
teardown, or bootstrap failure after closing every row-owned FD, P closes it
once and immediately requires F_GETFD=-1/EBADF with no intervening
allocation.  If that proof fails, teardown is crash-only and cannot yield a
success receipt.

After a valid quiesce ACK and inside the P allocation barrier, the exact four
fresh row-owned proc FDs are opened in this order:

~~~text
child_pid_dirfd = openat(LONG_LIVED_PROC_ROOT,
                         canonical_child_outer_pid_decimal,
                         O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
child_fd_dirfd  = openat(child_pid_dirfd,"fd",
                         O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
g_pid_dirfd     = openat(LONG_LIVED_PROC_ROOT,
                         canonical_G_outer_pid_decimal,
                         O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
g_fd_dirfd      = openat(g_pid_dirfd,"fd",
                         O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
~~~

Each is immediately ledgered, must be a directory with exactly FD_CLOEXEC,
and must join the same live pidfd/start-time/NSpid/credential/cgroup identity
before snapshot 1 and after snapshot 2.  Before each complete enumeration P
requires `lseek(fd_dirfd,0,SEEK_SET)=0`, then uses only exact getdents64,
canonical nonnegative decimal entries without leading zero except `0`, and
bounded readlinkat on an exact entry.  Proc link text is comparison evidence
only: it is never followed and never substitutes for fstat of an acquired
descriptor.

All four fresh proc FDs remain open through both snapshots, every
pidfd_getfd/fstat comparison, and both pre-unwind reciprocal diag responses.
They are row-owned and are unconditionally reverse-closed and proved EBADF
on success and every error before EXIT.  A partial open disposes every
earlier returned row FD.  No fresh row proc FD crosses EXIT, EXIT_ACK,
original endpoint close, thaw, child start, kill, or reap.  These statements
do not close or shorten the separately named LONG_LIVED_PROC_ROOT lifetime.

### 4.3 Exact four-record quiescence protocol

The closed P--G protocol adds exactly these four records:

~~~text
P -> G:
FD_AUDIT_QUIESCE_ENTER audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT child_pidfd_serial=DEC guardian_pidfd_serial=DEC

G -> P:
FD_AUDIT_QUIESCE_ACK audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT g_fd_generation=DEC

P -> G:
FD_AUDIT_QUIESCE_EXIT audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT g_fd_generation=DEC outcome=AUDIT_OUTCOME transcript=LOWERHEX64

G -> P:
FD_AUDIT_QUIESCE_EXIT_ACK audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT g_fd_generation=DEC outcome=AUDIT_OUTCOME transcript=LOWERHEX64
~~~

Each uses the unchanged four-byte big-endian length prefix, canonical ASCII,
4096-byte ceiling, exact field order/direction, no ancillary item, and exact
complete-send rule.  It occurs once for the row.  `AUDIT_OUTCOME` is exactly
`PASS|ABORT`.  `audit_epoch`, child_pidfd_serial, and guardian_pidfd_serial
are P-owned monotone nonzero values.  PREFLIGHT_PROBE has session=0;
RUNTIME_CHILD has the child's exact registered session, including an exact
session-zero bootstrap row where the inherited registration says zero.  No
sentinel substitution,
omission, replay, row substitution, or cross-child record is legal.

`g_fd_generation` is G-owned, monotone, nonzero, incremented exactly once
for the accepted ENTER, and bound through EXIT_ACK.  It is an operational
anti-replay coordinate, never P's identity evidence.  G accepts ENTER only
while the exact child is in its frozen pre-START or method-specific barrier
and no quiesce is open.  It first completes or rejects every already-started
FD-mutating action, closes admission to new work, drains no requester
operation, increments the generation, enters `G_FD_QUIESCED`, and only then
completely sends ACK.

From immediately before ACK through complete EXIT_ACK, G may use only its
already-held P-control FD to receive the exact EXIT and send the exact ACK.
It may not call or cause `open*`, `creat`, `close`, `close_range`, `dup*`,
fcntl duplication, `socket*`, `socketpair`, `accept*`, `pipe*`, `eventfd*`,
`signalfd*`, `timerfd*`, `inotify*`, pidfd creation, SCM_RIGHTS receipt or
installation, fork, clone, exec, signal-handler allocation, library lazy-
open, or any descriptor allocation/install/replacement/close.  It has one
thread; nevertheless, the prohibited state rather than thread count is the
quiescence premise.  The child independently stays blocked for the same
whole interval and cannot mutate its descriptor table.

The gapless interval is exactly:

~~~text
complete QUIESCE_ACK send / G_FD_QUIESCED
  -> four row proc opens and identity joins
  -> complete child snapshot 1, then complete G snapshot 1
  -> every child and G pidfd_getfd acquisition in Section 4.5 order
  -> every F_GETFD/fstat/proc comparison
  -> two pre-unwind reciprocal Unix-diag responses
  -> complete child snapshot 2, then complete G snapshot 2
  -> identity, snapshot, and generation equality
  -> reverse close plus immediate EBADF for every row-owned entry
  -> two post-unwind reciprocal Unix-diag responses on originals
  -> restored permanent-holder matrix
  -> complete EXIT send
  -> complete EXIT_ACK send
~~~

On PASS, G may reopen admission and resume FD-mutating work only after its
complete EXIT_ACK send.  P releases its allocation barrier only after it
receives and validates the matching ACK.  On ABORT, G completely sends the
ACK but never reopens admission or resumes the failed session; it proceeds
to retained containment.  ENTER/ACK/EXIT/EXIT_ACK send failure, control EOF,
wrong generation, replay, or mismatch invokes whole-control containment; it
never infers thaw, original close, audit success, ABSENT, or PASS.

### 4.4 P allocation barrier and exact ledger grammar

P is single-threaded and enters exactly one
`FD_AUDIT_ALLOCATION_BARRIER` before the first fresh proc open.  Its existing
Netlink Unix-diag socket, P-control channel, signalfd, LONG_LIVED_PROC_ROOT,
guardian/child pidfds, and any FD5 opposite peer are permanent pre-existing
capabilities, not row-owned allocations.  Except for the exact whitelisted
row opens and pidfd_getfd calls, no P code opens, accepts, receives an FD,
duplicates, or closes a descriptor until row unwind finishes.  The retained
handled set `HUP,INT,QUIT,PIPE,ALRM,TERM,USR1,USR2` remains blocked process-
wide and the already-open signalfd is not read during the barrier.  P has no
asynchronous user handler; every other catchable signal retains a default
disposition that invokes no P code.  SIGKILL/SIGSTOP and default stop/death
produce no successful audit and enter retained external crash containment.
P validates mask/dispositions at entry and again after EXIT_ACK.

Before the first row open, P preallocates exactly four proc-ledger slots plus
one child-duplicate slot.  After all four proc FDs are ledgered and snapshot
1 fixes the complete G socket-candidate count, but before the first
pidfd_getfd, P preallocates exactly that many G-candidate slots.  Allocation
failure before any FD exists creates an ABORT transcript and leaves G
contained; allocation failure after a row FD exists enters the common
unwind.  No successful FD-returning syscall occurs without a reserved slot.

The audit ledger tuple is exactly:

~~~text
(audit_epoch, acquisition_serial, local_fd, kind,
 target_pidfd_serial, targetfd, state)
~~~

`acquisition_serial` is P-owned monotone nonzero and never reused.  `state`
is exactly `OPEN|CLOSED_PROVED|AMBIGUOUS_CRASH_ONLY`.  `kind` and its exact
`target_pidfd_serial,targetfd` applicability are:

| kind | target_pidfd_serial | targetfd |
|---|---|---|
| CHILD_PROC_PID_DIR | exact child pidfd serial | literal `PROC_PID_DIR` |
| CHILD_PROC_FD_DIR | exact child pidfd serial | literal `PROC_FD_DIR` |
| GUARDIAN_PROC_PID_DIR | exact guardian pidfd serial | literal `PROC_PID_DIR` |
| GUARDIAN_PROC_FD_DIR | exact guardian pidfd serial | literal `PROC_FD_DIR` |
| CHILD_SOCKET_DUP | exact child pidfd serial | exact decimal 4, 5, or 8 selected by SLOT |
| GUARDIAN_SOCKET_DUP | exact guardian pidfd serial | canonical decimal G candidate FD from snapshot 1 |

Thus `targetfd` has the closed kind-indexed grammar
`PROC_PID_DIR|PROC_FD_DIR|DEC`; the two tokens are legal only on their
matching proc kinds and DEC is legal only on a socket-duplicate kind.  There
is no null, minus-one, wildcard, inferred coordinate, or inapplicable field.
The proc rows record the process capability against which their identity is
joined even though openat, not pidfd_getfd, created them.

Every successful row FD return is written immediately into the next slot
before any other fallible operation.  All acquired duplicates, including
nonmatching G candidates, remain OPEN until the common unwind, so the kernel
cannot reuse their local numeric FD.  A local number equal to any earlier
OPEN entry is terminal.  Numeric equality never proves object identity.
The long-lived descriptor/pidfd ledgers are distinct and cannot be smuggled
into or disposed by this row ledger.

### 4.5 Exact snapshots, acquisitions, comparisons, and transcript

For one row P performs this fixed acquisition order after snapshot 1:

1. `pidfd_getfd(exact_child_pidfd,slot_decimal,0)` into
   CHILD_SOCKET_DUP;
2. `fcntl(F_GETFD)=FD_CLOEXEC`, then fstat the obtained child duplicate;
3. for every canonical G numeric socket candidate from complete snapshot 1,
   in increasing numeric order, one
   `pidfd_getfd(exact_guardian_pidfd,candidate_decimal,0)` into
   GUARDIAN_SOCKET_DUP, immediately followed by exact CLOEXEC and fstat; and
4. no other acquisition.

P performs exactly one bounded readlinkat on every canonical numeric G
snapshot entry and requires one complete, nonempty, nontruncated result; any
errno, disappearance, truncation, or ambiguous result is terminal.  An entry
is a socket candidate if and only if those complete bytes are exactly
`socket:[DEC]`, where DEC is nonzero, has no leading zero, and is at most
0xffffffff, with no trailing byte.  Every and only such entry is acquired in
step 3.  Any other complete text is a noncandidate, but text beginning
`socket:[` that is not the exact grammar is a terminal PROC mismatch rather
than an ignored entry.

The obtained child FD must be S_IFSOCK with nonzero st_ino no greater than
0xffffffff.  Its canonical proc text must name the same inode; the actual
fstat, not proc text, fixes the query inode.  Every selected G candidate must
also be S_IFSOCK with such an inode and its proc text must match that actual
fstat.  A failed acquisition or validation is terminal but does not skip
later unwind.

For FD4 and FD8, P obtains and fstats every proc-selected G socket candidate.
Exactly one must have the registered holder role and the inode returned as
the child endpoint's UNIX_DIAG_PEER.  Zero or two matches is terminal.  Both
directions must be unique and reciprocal:

~~~text
diag(child_actual_fstat_inode) = selected_G_actual_fstat_inode
diag(selected_G_actual_fstat_inode) = child_actual_fstat_inode
~~~

For FD5, P fstats the one retained P-side opposite peer directly; it is not
newly opened, duplicated, or entered in the row ledger.  P still acquires and
fstats every proc-selected G socket candidate.  Exactly zero candidate
inodes may equal either child FD5's actual inode or the P-peer actual inode.
The child/P original pair must be uniquely reciprocal before unwind.  This
current quiesced result, not a historical table, proves G holds neither FD5
endpoint.  All v4 40-byte request, 48-byte response, sequence, port, source,
cardinality, NLA, cookie, two-pair crossed-preflight, and no-fallback rules
remain byte-exact.

Through the same still-open proc FD directories P next takes child snapshot
2 then G snapshot 2.  Each complete canonical numeric set must be byte-equal
to its snapshot 1 set; both process identities and g_fd_generation must be
unchanged.  Equal numbers become meaningful only because the child barrier
and G_FD_QUIESCED prohibit close/replacement.  Actual acquired-fd fstat plus
reciprocal diag, not equal numbers or proc strings, proves object identity.

The transcript preimage has one exact binary grammar.  Define `U16BE(n)`,
`U32BE(n)`, and `U64BE(n)` as unsigned big-endian integers of 2, 4, and 8
bytes.  An item is

~~~text
U16BE(tag) || U64BE(value_byte_count) || exact_value_bytes
~~~

and the complete preimage is

~~~text
ASCII("P15R-FD-AUDIT-TRANSCRIPT-v6") ||
U32BE(item_count) || item[0] || ... || item[item_count-1]
~~~

with no NUL, LF, padding, omitted item, alternate encoding, or trailing
byte.  `transcript` is lowercase hex of SHA-256 over that preimage.  The
exact successful schedule is:

| tag | value bytes | cardinality/order |
|---:|---|---|
| 1 | canonical ENTER tuple plus exact ACK generation | once |
| 2 | canonical base-ledger-allocation receipt | once, before any row FD |
| 3 | canonical CHILD_PROC_PID_DIR F_GETFD/fstat/identity receipt | once |
| 4 | canonical CHILD_PROC_FD_DIR F_GETFD/fstat/identity receipt | once |
| 5 | canonical GUARDIAN_PROC_PID_DIR F_GETFD/fstat/identity receipt | once |
| 6 | canonical GUARDIAN_PROC_FD_DIR F_GETFD/fstat/identity receipt | once |
| 7 | exact child snapshot-1 canonical bytes | once |
| 8 | exact G snapshot-1 canonical bytes | once |
| 9 | canonical G-candidate-slot-allocation receipt | once |
| 10 | canonical child-duplicate F_GETFD/fstat/proc receipt | once |
| 11 | canonical G-candidate F_GETFD/fstat/proc receipt | once per candidate, increasing candidate decimal |
| 12 | canonical P-peer fstat receipt | exactly once for FD5; absent for FD4/FD8 |
| 13 | exact raw v4 diag response child-to-peer | once |
| 14 | exact raw v4 diag response peer-to-child | once |
| 15 | exact child snapshot-2 canonical bytes | once |
| 16 | exact G snapshot-2 canonical bytes | once |
| 17 | canonical identity/snapshot/generation equality receipt | once |
| 18 | canonical complete reverse close/EBADF ledger bytes | once |
| 19 | exact raw v4 post-unwind diag response child-to-peer | once |
| 20 | exact raw v4 post-unwind diag response peer-to-child | once |
| 21 | canonical final permanent-holder matrix including FD5 zero-G result | once |

Every canonical ASCII receipt is a sequence of `name=value` fields in the
exact listed order, joined by one ASCII space, with canonical unsigned
decimals or lowercase hex as specified and no optional field, NUL, or LF.
Its fixed field lists are:

~~~text
tag1: audit_epoch kind session child slot child_pidfd_serial guardian_pidfd_serial g_fd_generation
tag2: reserved_proc_slots reserved_child_duplicate_slots
tag3..6: acquisition_serial local_fd kind target_pidfd_serial targetfd fd_flags st_mode st_dev st_ino identity_sha256
tag9: reserved_g_candidate_slots
tag10: acquisition_serial local_fd target_pidfd_serial targetfd fd_flags st_mode st_dev st_ino proc_inode
tag11: acquisition_serial local_fd target_pidfd_serial targetfd fd_flags st_mode st_dev st_ino proc_inode
tag12: local_fd fd_flags st_mode st_dev st_ino
tag17: child_identity_sha256 guardian_identity_sha256 child_snapshot_equal g_snapshot_equal g_fd_generation
tag21: slot child_original_holders peer_original_holders p_audit_duplicates g_matching_holders restored
~~~

Tag 2 is exactly
`reserved_proc_slots=4 reserved_child_duplicate_slots=1`; tag 9's value is
`reserved_g_candidate_slots=DEC` with DEC equal to the exact candidate count
fixed by snapshot 1.  The four proc receipt fstats require directory
type, exact FD_CLOEXEC, actual device/inode, and the exact joined child or
guardian identity digest.  They are “obtained-FD fstat” transcript entries;
no proc-open or proc-validation result is implicit.

The snapshot canonical bytes are the increasing canonical-decimal FD entries
joined by one ASCII comma, or the empty byte string for an empty set; no
spaces or final comma occur.  `st_mode` and `fd_flags` are unsigned decimal;
device and inode are unsigned decimal; boolean/equality/holder fields are
canonical unsigned decimals.  Every identity digest is exactly the
Section 4.2 `identity_sha256` over the applicable complete `identity_bytes`;
tag 3/4, tag 5/6, and tag 17 use no alternate preimage.

Tag 18 is binary even though its rows are canonical ASCII.  Its exact value
is `U32BE(close_row_count)` followed by, for each actual OPEN entry in reverse
acquisition order, `U64BE(row_byte_count)||row_bytes`.  Each row is exactly:

~~~text
acquisition_serial=DEC local_fd=DEC close_return=SIGNEDDEC close_errno=DEC f_getfd_return=-1 f_getfd_errno=9 final_state=CLOSED_PROVED
~~~

Here SIGNEDDEC is exactly `0|-1`; close_errno is 0 after return 0 and the
actual positive x86_64 errno after return -1.  The fixed F_GETFD result and
errno are the required EBADF proof.  The row count is zero when no audit-
owned FD was returned.  Reserved but
never-opened slots have no acquisition_serial and no close row; their
unperformed acquisition is instead a MISSING stage.  Tag 18 includes every
actual returned one of the four proc FDs, child duplicate, and G candidates,
and no long-lived descriptor.

For PASS tags 1 through 10 occur once in order, tag 11 repeats exactly the
snapshot-fixed candidate count, tag 12 occurs iff SLOT=FD5, and tags 13
through 21 then occur once in order.  For ABORT, tag 65533 is inserted at
the actual first-failure point.  Its exact value uses one and only one of
these kind-indexed forms:

~~~text
non-FD stage:
stage=DEC errno=DEC mismatch=TOKEN

FD stage before a descriptor return:
stage=DEC errno=DEC mismatch=TOKEN targetfd=TARGET

FD stage after a descriptor return, including close stage 18:
stage=DEC errno=DEC mismatch=TOKEN acquisition_serial=DEC local_fd=DEC targetfd=TARGET
~~~

TARGET is the exact `PROC_PID_DIR|PROC_FD_DIR|DEC` coordinate from the
ledger grammar.  The second form is mandatory when stages 3--6, 10, or 11
fail before returning a descriptor; for repeated tag 11 its DEC is the exact
snapshot candidate.  The third is mandatory once that stage has a ledgered
return and for a stage-18 close/EBADF failure.  All other stages use the
first form.  `stage` is the ordinary tag whose action failed, and errno is
the actual nonnegative errno or 0 for a predicate mismatch.  Successfully
completed earlier stages are the exact observed prefix; a partially
completed failing stage is not relabelled successful, while any FD it
returned is independently fixed by its acquisition and close-ledger tuple.
TOKEN is exactly
`NONE|MEMORY|OPEN|RETURN|CLOEXEC|TYPE|INODE|PROC|DIAG|CARDINALITY|IDENTITY|SNAPSHOT|GENERATION|CLOSE|EBADF|HOLDER|CONTROL`.
Thus ENOMEM in either fixed allocation has stage 2 or 9/MEMORY, and every
proc open, CLOEXEC, fstat, or identity failure has exact stage 3, 4, 5, or 6
and exact target coordinate.

Tag 18 is inserted after the actual unwind completes and is never declared
missing.  If the first failure occurs during unwind, its stage-18 failure
marker is inserted immediately when observed; P then continues the required
reverse unwind, and the complete proved tag-18 ledger follows the marker.
Every other later unperformed ordinary position is represented in schedule
order after unwind by tag 65534 and value `missing_tag=DEC`.  A missing
repeated tag 11 is
`missing_tag=11 candidate=DEC` for every snapshot-fixed unperformed
candidate; if snapshot 1 never fixed the candidate set, exactly one token is
`missing_tag=11 candidate_set=UNFIXED`.  The FD5-only tag 12 is a schedule
position only for FD5.  If close absence cannot be proved, the observed
prefix and crash ledger remain internal but no EXIT/transcript is sent.  An
ABORT digest never claims an unperformed allocation, open, fstat, diag,
snapshot, close proof, or holder restoration.

### 4.6 One common reverse unwind, exit, and ABA exclusion

After the first row-owned FD opens, success and every later error enter one
finally-equivalent common unwind.  It visits every OPEN entry exactly once
in reverse acquisition order.  For each entry it performs, without retry:

1. `close(exact_local_fd)` exactly once and records the exact return;
2. with no intervening P allocation, immediately
   `fcntl(exact_local_fd,F_GETFD)`; and
3. requires exactly -1 with errno EBADF before changing that exact
   `(audit_epoch,acquisition_serial,local_fd)` to CLOSED_PROVED.

A close error does not prevent attempts on the remaining OPEN entries.  A
nonzero close return, non-EBADF observation, unvisited OPEN entry, duplicate
close, intervening allocation, or wrong reverse order is terminal.  If all
row-owned FDs are proved absent but another predicate failed, P constructs
the exact ABORT transcript, sends EXIT outcome=ABORT, and G remains
contained.  If any absence is ambiguous, P attempts every other close but
does not send normal EXIT, release the child, thaw, close an original
endpoint, or emit PASS/ABSENT/success; it invokes crash-only containment so
process teardown, not a false receipt, removes the ambiguous P reference.

After a clean unwind, P re-queries the still-live original pair in both
directions using the retained v4 Netlink socket.  It requires the same unique
reciprocal mapping, then recomputes the permanent-holder matrix: original
child and opposite endpoint remain, every audit-ledger entry is
CLOSED_PROVED, and FD5 has zero matching G holder.  Only then does it fix the
PASS transcript and completely send EXIT.  The row allocation barrier is
released only after matching EXIT_ACK; no temporary duplicate or fresh row
proc FD crosses original close, G resume, child START, kill, reap, or
terminal reply.  LONG_LIVED_PROC_ROOT remains intentionally live and is not
a temporary/proc-row residue.

All returned pidfds use their separate total unwind: failed post-open
validation closes/proves immediately; a valid child pidfd closes/proves only
after exit/reap/CHILD_REAPED; the guardian pidfd retains its inherited
lifetime through G reap.  Every close has the same immediate EBADF rule.  A
numeric local FD can be reused only after its prior ledger entry is
CLOSED_PROVED and its allocation barrier has ended; its new monotone
acquisition or pidfd serial cannot satisfy the old tombstone.  Retaining all
duplicates until reverse unwind plus G/child quiescence excludes both a
target-table same-number close/reopen and a P-local same-number reuse.

### 4.7 Mandatory D-M2 hostile pairs

The frozen actual observations permit a later reviewer to distinguish at
least:

1. identical pidfd and target decimals naming different objects;
2. one outer PID at two start times;
3. proc text naming inode A while acquired-descriptor fstat gives B;
4. the real child endpoint paired with the wrong one of two live G peers;
5. G closing FD N and installing another socket at N between superficially
   equal snapshots;
6. first duplicate success followed by CLOEXEC, fstat, proc, later-
   acquisition, diag, snapshot, uniqueness, or holder failure;
7. pidfd_open success followed by failed identity validation;
8. a temporary socket duplicate or fresh per-row proc FD crossing original
   close, EXIT_ACK, thaw, START, kill, or reap;
9. a P-local FD decimal reused under a different acquisition generation;
10. actual pidfd_getfd denial while proc and Unix-diag remain readable; and
11. a clean row ledger while the deliberately distinct long-lived proc-root
    capability remains present through the final audit.

Trust in G, equal descriptor numbers, copied proc inode text, inferred
permission, an unversioned helper, a generic cleanup sentence, or another
kernel primitive cannot distinguish the pairs and is not an alternate path.

## 5. Non-regression and frozen external invariants

The following prior closures remain binding without weakening:

1. **C-M1:** the child-unique P-created FD 5; exact FDSET; kernel credential,
   pidfd, role, and endpoint binding; P-issued one-use child-request nonce;
   requester-direct raw request; actual FD-4 bytes; exact comparison; G
   confirmation; registered child; and P-derived admission.  Section 3 only
   expands the closed FD-5 enum from the four v4 forms to the exact ten forms
   authorized by the corrected gate; it adds no post-terminal form.
2. **C-M2:** the exact 40-byte Netlink request and 48-byte response, native
   x86_64 ABI, sequence/port/source/cardinality/NLA/cookie checks, two
   simultaneous preflight pairs, reciprocal UNIX_DIAG_PEER, crossed-pair
   rejection, holder matrix, and no fallback.  Section 4 invokes that oracle;
   it does not replace or weaken it.
3. **B-M1:** the exact two operational OWNER additions, six ordered session-
   zero rows, closed post-suite owner/admission grammar, and exactly 173
   methods.  Neither preflight adds a method or child row.
4. **B-M2:** the phase-specific FDSET table, FD3 source-close and FD8 START
   barriers, FD4/FD5/FD9 lifetimes, stdout/stderr drain, EOF, close, and reap
   order.  Section 4 adds a bounded quiesced observation before a barrier
   release; it changes no target byte or permanent descriptor set.
5. **B-M3:** G-created pre-access OBJECT_REGISTERED/ACK, generator
   authorized basename/purpose creation, post-reap held-dirfd enumerate/
   fstat/register/ACK and MEMBER_LEDGER_CLOSED before exchange, cleanup, or
   reference audit; P25 generated count zero; and unexpected-object
   containment/nondeletion.
6. **A-M1:** exact unparameterized SG_SCOPE; four primitive-only
   counterfactuals; primitive evidence-class recomputation before proposed
   conclusion; all S01--S35 typed substantive predicates; and unchanged
   accept/reject/detector/inverse registry.
7. **A-M2:** real-filesystem recursive lstat receipts, valid/malformed
   variants, five live metadata falsifiers, and exact-one-coordinate mode and
   mtime clones without ctime masking, including root/transient sidecar.
8. **A-M3:** private namespace/cgroup possession, atomic birth placement,
   root-owned control capabilities, freeze/membership/kill/reap proofs,
   retained parent/root/lock dirfds, capability-relative cleanup, generation/
   P25/ACQUIRING/OWNED-to-CLEANING replacement fixtures, foreign
   preservation, and no false ABSENT.
9. **A-M4:** manifest-first complete-review authentication, canonical unique
   effective-amendment blocks, capability-relative independent amendment
   opens and hashes, and full dereference before lifecycle adjacency.
10. **blocked v5:** its exact digest remains a provenance member, but none of
    its discarded protocol, descriptor, or review claims becomes operative.

The following values remain exact and are not reinterpretations:

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

The six implementation paths, eight CSV paths and literal headers, all 120
rows and order, 35 semantic and 28 package mutation methods, all 173 method
names, nine generated paths, fourteen authority paths, manifest keys, and
graph nodes A,D,R,G,I,C,M,V with twelve distinct edges remain byte-
definition invariant.  Every v6 secret, digest, session state, pidfd, proc
FD, quiesce record, transcript, ledger, and close proof is operational and
nonserialized.  No seventh path, new test, new target/purpose/owner, public
detector/exit, schema field, generated byte, authority binding, node, edge,
theorem owner, Route, or manuscript surface is introduced.

## 6. Append-only successor and later independent review

The current review at SHA-256
`30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb`
remains unchanged.  Its historical v1 count-two, v2 count-three, v3 count-
four, and v4 count-five blocks remain byte-identical and ordered.  Only after
this amendment is frozen and externally hashed may a fresh independent
reviewer append one active block with exactly these lines and no blank or
commentary line inside it:

~~~text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v5]
count=6
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
6.sha256=<exact externally computed final v6 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
~~~

The verifier first capability-opens the unchanged manifest-bound review path
once, applies the retained regular/nlink-one/no-link rules, reads and hashes
the complete post-v6 review from that one FD, and matches the manifest-bound
complete digest before parsing.  From those authenticated bytes it requires
exactly one byte-identical historical v1, v2, v3, and v4 block, exactly one
active v5 block in the count-six form above, and no other begin/end tag.  It
rejects missing, duplicate, reordered, nested, malformed, prefix-drifted,
wrong-version/count/index/path/digest, extra-key, blank, or commentary-
bearing blocks.

It then independently capability-opens amendments v1 through v6 in active
order beneath the same held package-root FD with the retained beneath/no-link
rules, reads every byte, and recomputes every hash.  The v6 digest comes only
from the externally frozen file and is not predicted in this file.  Only
after all six independent dereferences match does R set the nonserialized
obligation `R.effective_amendments=[v1,v2,v3,v4,v5,v6]` and evaluate
lifecycle adjacency.  This changes no manifest key, binding count, generated
artifact, node, edge, self-hash, future-result edge, or proof cycle.

The later reviewer must independently read and hash base, v1--v4, blocked
v5, v6, the corrected gate v6, and the complete review prefix.  It must
attack all D-M1 early-queue, first-disclosure, replay, ACTIVE/ACK, send-
failure, and cleanup worlds and all D-M2 syscall-permission, pidfd/proc
identity, quiescence, two-snapshot, actual-fstat/diag, reverse-unwind,
EBADF, holder-restoration, and dual-ABA worlds.  This author document and its
self-audit are not independent evidence.  D-M1 and D-M2 remain OPEN until
that fresh append-only review makes its own exact finding.

## 7. Frozen lifecycle and author-side audit

No generator, verifier, test, wrapper, implementation, control execution,
reproduction run, Route, composition, manuscript, figure, release, archive,
Git operation, or public synchronization was authorized or performed by
this amendment.  No CSV, schema, generated artifact, review byte, gate byte,
base design, earlier amendment, Route record, or manuscript was changed.

The author-side closure audit is limited to contract presence:

| Gate obligation | Frozen design surface | Independent finding |
|---|---|---|
| D-M1 P-only causal values and exact ACTIVE gate | Sections 3.1--3.8 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| D-M2 actual-FD/quiescence/unwind/ABA contract | Sections 4.1--4.7 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| all retained counts, paths, schemas, closures, and DAG | Sections 2 and 5 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| count-six append-only successor and six dereferences | Section 6 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |

The lifecycle matrix is:

~~~text
CURRENT_INDEPENDENT_VERDICT=REVISE_C0_M2_m0
D_M1_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
D_M2_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
AMENDMENT_V6_DESIGN_BYTES=FROZEN_DESIGN_ONLY_PENDING_FRESH_INDEPENDENT_REREVIEW
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
