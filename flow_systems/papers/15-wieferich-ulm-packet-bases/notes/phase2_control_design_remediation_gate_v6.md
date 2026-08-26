# Replacement Paper 15 Phase-2 control-design remediation gate v6

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v6 — C0/M2/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v6.0`  
Date: 2026-08-17 (Asia/Shanghai)

This is a bounded design-remediation authorization, not a finding closure.
The current independent review's two Major findings, `D-M1` and `D-M2`,
remain open.  This gate authorizes exactly one design-only amendment and,
only after that amendment is frozen and externally hashed, one fresh
independent append-only re-review.  It authorizes no generator, verifier,
test, wrapper, implementation, control execution, reproduction run, Route,
composition, manuscript, figure, release, archive, Git action, or public
synchronization.

## 1. Exact authority and retained independent verdict

The complete current bytes of all twelve records below were read and
independently re-hashed before this gate was frozen:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| design amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| remediation gate v2 | `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` |
| design amendment v2 | `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| remediation gate v3 | `notes/phase2_control_design_remediation_gate_v3.md` | 578 | 27299 | `e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac` |
| design amendment v3 | `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| remediation gate v4 | `notes/phase2_control_design_remediation_gate_v4.md` | 645 | 30174 | `df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647` |
| design amendment v4 | `notes/phase2_control_design_amendment_v4.md` | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| remediation gate v5 | `notes/phase2_control_design_remediation_gate_v5.md` | 839 | 41734 | `55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7` |
| blocked design amendment v5 | `notes/phase2_control_design_amendment_v5.md` | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` |
| current final append-only review | `notes/phase2_control_design_peer_review.md` | 2746 | 143812 | `30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb` |

The complete current review is an append-only chain.  Its independently
recomputed nested prefix receipts are:

| Prefix lines | Prefix bytes | SHA-256 |
|---:|---:|---|
| 2308 | 119250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` |
| 1910 | 96524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1524 | 74876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1017 | 49358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

The operative repair clauses remain base plus v1 through v4.  Amendment v5
is an exact blocked/no-op provenance member and installs no operational
repair.  Its presence in the versioned chain is not evidence against either
finding.  The current independent verdict is exactly **REVISE — C0/M2/m0**:

1. `D-M1` remains open because predictable registration and reply bytes do
   not causally prove the requester received the predecessor message, and G
   has no P-owned ACTIVE gate before later FD-4 operations.
2. `D-M2` remains open because actual-FD acquisition conflicts with the v4
   FD-5 no-duplicate authority and lacks total acquisition unwind, exact
   proc capabilities, and G descriptor-table quiescence.

No gate, amendment self-audit, random-value name, syscall name, queued
message, G self-report, or fail-closed assertion closes either finding.
The theorem owner remains the bare compact group `B_p`; universal recovery
remains `OPEN_NOT_AUTHORIZED`; Route B remains false.

The current review contains four immutable effective-amendment blocks.  Its
sole current active block is exactly:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v4]
count=5
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
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

## 2. Sole target, precedence, and exact supersession budget

The target was absent before this gate was created.  Exactly one new design
file may be created:

```text
notes/phase2_control_design_amendment_v6.md
```

After that file is frozen and externally hashed, the versioned design chain
is exactly:

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + amendment v2 c1d104d2...
  + amendment v3 f6a0af9c...
  + amendment v4 f5547926...
  + blocked/no-op amendment v5 2204471c...
  + amendment v6 at its externally computed final digest.
```

Amendment v6 may supersede only the following exact surfaces:

1. the v2 `SESSION_CREATE` and `SESSION_CREATED` request/reply shapes and
   opaque-session state edges, plus the v4 direct audit's dynamic-session
   lookup, only to install Section 3's P-owned causal capabilities, raw
   transcript joins, inactive/active split, and exact P--G records;
2. the eight creator-endpoint, post-create, non-child FD-4 request shapes
   named in Section 3.6, only to append their exact active capability;
3. the v2 native x86_64 syscall inventory, only to add `getrandom=318`,
   `pidfd_open=434`, and `pidfd_getfd=438` with the exact zero-flag and
   failure contracts below;
4. v4 Section 3.1's absolute statement that requester FD 5 is never
   duplicated and the corresponding exclusive-holder rows in v4 Sections
   4.5--4.6, only for the single bounded P audit duplicate while the exact
   Section 4 audit interval is open;
5. the P--G closed control enum and P-only pre-suite state sequence, only to
   add the exact session ACTIVE/abort and FD-audit quiescence records and
   preflights frozen below; and
6. v4's review-node successor grammar, only so the existing active count-five
   block becomes historical and one later count-six v5 block ends at v6.

The v4 requester FD-5 terminal lifetime is not superseded: no new requester
FD-5 frame is legal after the requester receives its terminal FD-4 reply,
and the requester still closes FD 5 at that exact retained edge.  Amendment
v6 must not recreate the blocked v5 post-reply close-handshake contradiction.

Every changed wire form, field, state, capability holder, disclosure edge,
syscall, proc FD, pidfd, local duplicate, close edge, failure edge, and
verifier obligation must be listed.  Every omitted base/v1/v2/v3/v4 clause
remains binding.  Blocked amendment v5 contributes no clause to supersede.
No optional frame, wildcard owner/slot/phase, inferred primitive, fallback,
alternate ABI, or unstated error branch is permitted.  Amendment v6 must
not embed its own digest, claim independent closure, or authorize
implementation or execution.

## 3. D-M1 minimum causal-capability contract

### 3.1 Capability source and threat boundary

P is the sole issuer of all three D-M1 values.  The only entropy primitive
is native Linux x86_64

```text
getrandom(buffer, 32, flags=0), syscall number 318
```

under the already frozen native x86_64 little-endian LP64 ABI.  P obtains
exactly 32 bytes.  A positive short return continues only for the remaining
suffix; `EINTR` retries only the unchanged suffix; a zero return, any other
errno, more than 32 aggregate bytes, or incomplete fill is terminal.  There
is no timestamp, PID, counter, deterministic digest, G/requester randomness,
`/dev/urandom`, header-derived call, libc fallback, redraw-after-collision,
or alternate source.  A pre-suite call under the final nested security
context must succeed before any subject/package/result/root/member write;
its 32 bytes are immediately tombstoned and never used as a capability.
Every later causal call must also succeed at its specified state edge.

Each 32-byte value is encoded as exactly 64 lowercase hexadecimal digits.
P compares a new value with every live and tombstoned value of every D-M1
kind.  Equality is a terminal collision, not permission to redraw.  The raw
values are operational, in-memory, nonserialized secrets.  Before their
specified first-disclosure edge they may not appear in a CSV, manifest,
result, log, diagnostic, environment, argv, pathname, G-to-requester reply,
or any requester-readable field.

Within this control threat model, “unforgeable” means an independently
generated 256-bit P value unavailable on every permitted requester input
channel before its first-disclosure edge and accepted only by exact equality
at its bound endpoint/state.  A public SHA-256 of predictable tuple fields
is a transcript digest, not an unforgeable capability.  Guessing is not an
authorized transition; a guessed or wrong value consumes the attempt and
terminates the authorization.

The three values have distinct semantics:

1. `create_cap` is a fresh, one-use capability first disclosed inside the
   post-grant `SESSION_AUTH_RECEIPT`.  A correct actual `SESSION_CREATE`
   carrying it is the causal witness that the requester received that
   receipt.  Its value is unavailable before the actual receipt.
2. `reply_nonce` is a fresh, one-use reply challenge given only to G in the
   commit and first disclosed to the requester only inside G's actual
   `SESSION_CREATED` reply.  The requester must return the exact raw reply
   and nonce directly to P.
3. `active_cap` is generated only after P joins the actual-reply witness to
   G's committed transcript.  It is a session-scoped operation capability,
   not falsely labelled one-use.  Its endpoint/request-number binding and
   terminal tombstone prevent replay; the separate create and reply values
   remain the two one-use causal capabilities.

### 3.2 Exact requester--P frames and raw registration

The amendment must add exactly six session-auth payload forms on the already
child-unique, P-created FD-5 `REQUEST_AUDIT` endpoint.  Together with the
four unchanged v4 child-request-audit forms, the complete FD-5 payload enum
is exactly these ten forms:

```text
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

requester -> P:
AUDIT_OPEN audit=DEC serial=DEC

P -> requester:
AUDIT_CHALLENGE audit=DEC serial=DEC nonce=LOWERHEX64

requester -> P:
AUDITED_SPAWN audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64 trigger=TRIGGER core=LOWERHEX

P -> requester:
AUDIT_RECEIPT audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64
```

The last four forms are the byte-identical v4 child-request-audit grammar;
they do not become session-auth substitutes.  There is no session-auth close
frame after `SESSION_CLOSED` and no eleventh FD-5 payload form.

Every form is one complete canonical ASCII seqpacket, at most 4096 bytes,
with no NUL, LF, length prefix, rights, explicit credentials, extra cmsg, or
trailing byte.  Requester sends use plain `send`; P receives with `recvmsg`
and requires exactly one kernel-supplied `SCM_CREDENTIALS`, the registered
outer PID and uid/gid 65534/65534, normalized inner PID and uid/gid 0/0,
the retained pidfd/start-time/NSpid/cgroup identity, exact child role and
audit endpoint, no other cmsg, and no `MSG_TRUNC`/`MSG_CTRUNC`.  P replies
use plain `send` and no ancillary item.  A send succeeds only when its return
equals the complete payload length.

`auth_serial`, `auth`, and nonzero `session` remain P-owned, monotone, and
never reused.  P derives `OWNER` from the frozen 173-method ownership table
and requires the exact method/trigger/owner/request/creator tuple.  No G
table or current child request supplies an expected coordinate.

`registration` is lowercase hex of exactly these canonical ASCII bytes:

```text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC
```

Its `digest` is SHA-256 of the exact registration bytes under the literal
domain prefix `P15R-SESSION-REGISTERED-v6` followed by one ASCII space and
then the exact registration, with no NUL or LF.  P canonical-decodes the raw
bytes, recomputes the digest, and binds the exact packet hash plus requester
identity, audit, auth serial, auth, session, request, method, trigger, and
owner before generating `create_cap`.

P then constructs the sole exact actual create bytes:

```text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC create_cap=LOWERHEX64
```

It sends the complete P--G create grant in Section 3.3 before disclosing
those bytes and `create_cap` in `SESSION_AUTH_RECEIPT`.  A requester cannot
know the correct capability before its actual receipt of that seqpacket.
The capability-bearing actual FD-4 request is therefore not byte-identical
to any packet queued before the predecessor receipt.  `create_cap` is
consumed by the first FD-4 create attempt for the bound endpoint/auth/session/
request, whether that attempt succeeds, is malformed, has a wrong byte or
capability, is duplicated, or is cross-bound.  It is never retried.

### 3.3 Exact P--G create, commit, ACTIVE, close, and abort records

The amendment must add exactly these ten payload forms to the closed P--G
control protocol:

```text
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
```

Each is one canonical payload under the unchanged four-byte big-endian
length prefix and 4096-byte payload ceiling, with no ancillary item and
exactly the shown direction and fields.  Every exact record occurs at most
once.  A missing, duplicate, stale, reordered, malformed, wrong-direction,
wrong-endpoint, wrong-identity, wrong-transcript, or wrong-state record is a
terminal protocol failure, never an alternate path.

`payload` is lowercase hex of the complete actual create bytes, never a
reserialization.  `create_cap_sha256` is SHA-256 of the 32 raw capability
bytes under domain `P15R-CREATE-CAP-v6`; it is a binding/tombstone digest,
not the capability.  `created` is lowercase hex of the sole future actual
reply:

```text
SESSION_CREATED request=DEC session=DEC reply_nonce=LOWERHEX64
```

After G receives `SESSION_AUTH_CREATE_GRANTED`, it consumes no FD-4 create
packet until the grant is installed.  This rule avoids treating readiness
order across two sockets as send order.  G then receives exactly the first
create packet, applies the retained credential/endpoint/pidfd/request checks,
consumes the one-use capability, requires complete raw equality with the
grant, and holds the request without private construction.  It reports the
actual bytes in `SESSION_AUTH_CREATE_ACCEPTED`.  P joins those bytes to its
direct registration and grant before generating `reply_nonce` and sending
`SESSION_AUTH_COMMIT`.

Only the commit permits G to create the exact bounded private copied-package
and lock-parent objects needed for an **INACTIVE** session.  G sends the
exact `SESSION_CREATED` bytes on the actual requester FD 4.  Only after that
complete send succeeds does it send `SESSION_AUTH_COMMITTED` with those
same raw bytes.  If the two independently scheduled observations arrive at
P in the opposite order, P may hold exactly one valid activation packet
until the committed record arrives; it may not infer order from poll order.

The requester learns `reply_nonce` only by actually receiving
`SESSION_CREATED`, then sends `SESSION_AUTH_ACTIVATED` with the nonce and
hex of the complete raw reply.  P parses and requires exact equality with
the commit and committed bytes and every immutable requester/session field.
Only after both observations match may P generate `active_cap`.

P first sends `SESSION_AUTH_ACTIVE_RECEIPT`, which is the sole first
requester disclosure of `active_cap`.  Only after that complete seqpacket
send succeeds may P send `SESSION_AUTH_ACTIVE` to G.  G validates the full
binding, sends `SESSION_AUTH_ACTIVE_ACK`, and changes the session to ACTIVE
only after the complete ACK send succeeds.  Before that transition G must
not receive, dequeue, parse, reserve, execute, mutate for, or reply to any
post-create FD-4 request.  Kernel queue readiness is not acceptance and
cannot bypass the gate.

Normal close uses the retained actual `SESSION_CLOSE`/`SESSION_CLOSED` FD-4
exchange.  G reports terminal cleanup to P with
`SESSION_AUTH_SESSION_CLOSED` before sending the terminal requester reply;
P validates and returns `SESSION_AUTH_CLOSE_ACK`.  Only after that ACK send
succeeds may G send `SESSION_CLOSED`.  The requester then closes FD 5 under
the unchanged v4 lifetime.  Thus no new post-reply FD-5 exchange is needed.

`AUTH_PHASE` is exactly

```text
REGISTERED | CREATE_GRANTED | CREATE_ACCEPTED | INACTIVE_COMMITTED |
ACTIVATION_JOINED | ACTIVE_RECEIPT_SENT | ACTIVE_PENDING | ACTIVE | CLOSING
```

and `AUTH_REASON` is exactly

```text
RECEIPT_SEND | REQUESTER_EOF | CREATE_MISMATCH | CREATE_ACCEPTED_SEND |
COMMIT_SEND | PRIVATE_CONSTRUCTION | CREATED_SEND | COMMITTED_SEND |
ACTIVATION_MISMATCH | ACTIVE_RECEIPT_SEND | ACTIVE_SEND |
ACTIVE_ACK_SEND | PREACTIVE_OPERATION | ACTIVE_OPERATION_MISMATCH |
SESSION_CLOSE_FAILURE | CONTROL_EOF
```

These are in-memory control tokens and add no public detector or exit class.

### 3.4 Exact ledger, binding, one-use, and tombstones

P's exact auth state is:

```text
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
```

G's exact session state is:

```text
NO_SESSION
  -> CREATE_ARMED
  -> CREATE_HELD
  -> INACTIVE
  -> ACTIVE_PENDING
  -> ACTIVE
  -> CLOSING
  -> CLOSED_TOMBSTONE

any nonterminal state -> ABORTING -> FAILED_TOMBSTONE
```

The ledgers bind every value to the requester child and unique audit
endpoint; kernel credentials and retained pidfd/start-time/NSpid/cgroup
identity; auth serial, auth, session, and request; method, trigger, and
P-derived owner; exact `SESSION_AUTH_REGISTERED`, final `SESSION_CREATE`,
and `SESSION_CREATED` byte hashes; and distinct domain-tagged registration,
create, reply, and activation transcript hashes.  Expected coordinates come
from P's immutable direct record.  G reports provide actual values only.

The `create_cap` and `reply_nonce` each have one legal consumption.  A wrong,
premature, cross-bound, duplicate, delayed, or replayed use consumes the
corresponding state and aborts it.  `active_cap` is a bound bearer only for
the one ACTIVE session and one creator endpoint; existing strict monotone
request numbers make a request replay illegal.  It cannot authorize another
endpoint, child, session, method, trigger, owner, or post-close request.

On close or abort, P and G retain at least

```text
(auth, session, request, endpoint identity, terminal cause,
 registration digest, create-cap digest, reply digest, active-cap digest)
```

through complete P/G teardown.  Raw secret bytes are erased only after their
digest and terminal state are fixed.  No auth, session, request capability,
nonce, value, or tombstoned tuple is recycled.  EOF never synthesizes a
success receipt or removes a tombstone.

### 3.5 Total send-failure, abort, and cleanup table

The amendment must freeze at least the following exact total transitions:

| Failure edge | Required transition before any later operation |
|---|---|
| create grant cannot be completely sent | P tombstones the undisclosed create capability; no requester receipt and no retry |
| grant succeeds but requester receipt send fails | P enters ABORTING; G discards grant/held packet; both tombstone the capability |
| requester EOF after receipt | P aborts; any held create cannot commit |
| requester remains live but sends nothing | the state makes no progress and no liveness success or invented timeout is claimed |
| first actual create is wrong or duplicated | G consumes the attempt, creates no private object, enters ABORTING, and reports the exact reason |
| create-accepted report cannot be sent | G creates no private object, locally tombstones, closes admission, and forces control containment |
| commit cannot be sent or validated | held create is discarded; no construction and no retry |
| private construction fails | G closes admission and unconditionally removes every object it created before `ABORTED` |
| actual `SESSION_CREATED` send fails | session stays INACTIVE, G cleans it, requester never learns reply nonce, and no active capability is minted |
| committed report fails after reply send | requester may know reply nonce, but P never reaches the two-input join or mints active capability; INACTIVE session is aborted |
| activation is missing, malformed, premature, duplicated, or wrong | P aborts; G remains INACTIVE and processes no later request |
| ACTIVE receipt send fails | active capability is not operational; P aborts before sending ACTIVE |
| ACTIVE send fails | G remains INACTIVE/ACTIVE_PENDING; no later request is processed; P aborts |
| ACTIVE ACK send fails | G does not enter ACTIVE, aborts and cleans the session; P cannot treat timeout/EOF as ACK |
| non-create FD-4 readiness before ACTIVE | G leaves the endpoint unpolled and performs no operation; after ACTIVE the first received packet must carry the exact capability, while a forced pre-ACTIVE receive is a protocol failure before mutation |
| active capability or request binding fails | no requested mutation occurs; the session enters ABORTING and cannot retry that request |
| close report/ACK/terminal reply fails | cleanup still completes, the state is a failed tombstone rather than successful close, and no capability is reused |
| ABORT or ABORTED itself cannot be sent | each side performs its locally possible cleanup, closes the control channel, and invokes the retained freeze/kill/reap/cgroup containment; missing delivery is never a success receipt |

Every send accepts only the complete payload-length return.  There is no
retry with the same capability.  G enters ABORTING before cleanup, closes
admission, rejects queued frames, starts no new session operation, kills and
reaps controlled children where applicable, and applies the retained
capability-relative root/lock cleanup.  `SESSION_AUTH_ABORTED` is legal only
after the reachable private state is terminal.  If a control-channel failure
prevents that record, the existing crash-containment evidence replaces no
missing receipt and cannot yield PASS or ABSENT.

### 3.6 Exact ACTIVE gate for every later FD-4 operation

`SESSION_CREATE` is the sole creator FD-4 request permitted before ACTIVE,
and its only pre-ACTIVE effect is the bounded INACTIVE construction needed
to produce `SESSION_CREATED`.  On the `TOP_TEST_CONTROLS` creator endpoint,
the following eight post-create non-child request forms must append exactly
one final field `active_cap=LOWERHEX64`:

```text
LOCK_ACQUIRE
LOCK_RELEASE
ROOT_CREATE
ROOT_VALIDATE
INJECT_EXCHANGE
CLEAN
FOREIGN_AUDIT
SESSION_CLOSE
```

No other creator-side non-child operation exists.  G requires exact equality
with the active ledger and ACTIVE state before it receives or acts on any of
them.  A packet queued before actual `SESSION_CREATED` cannot contain the
not-yet-generated value; waiting for another queue cannot make its bytes
equal.  A requester that has received `SESSION_AUTH_ACTIVE_RECEIPT` may
enqueue a capability-bearing request while G is still `ACTIVE_PENDING`; G
leaves it queued until the P-to-G ACTIVE/ACK transition completes.  The
contract orders G's receipt/acceptance/mutation, not an unobservable
cross-socket enqueue timestamp.

`AUDITED_SPAWN` remains the sole child-creating request and retains the v4
FD-5 random nonce, direct raw bytes, P confirmation, and admission gate.  P
may issue its audit receipt only for an ACTIVE parent mapping.  A delegated
requester endpoint cannot be allocated, transferred, or bound until the
parent is ACTIVE; G binds its immutable endpoint mapping to the same ACTIVE
session and checks ACTIVE before each unchanged delegated non-child request.
Thus no delegated endpoint exists in the hostile pre-ACTIVE world and no
wildcard endpoint exemption is introduced.

The later independent reviewer must attack at least these pairs:

1. the same public registration tuple with an early FD-4 create queued
   before versus after actual receipt of `create_cap`;
2. predictable request/session decimals with activation queued before versus
   after actual receipt of `SESSION_CREATED(reply_nonce)`;
3. an early creator operation without the later `active_cap` versus the
   exact post-ACTIVE operation;
4. a byte-correct G table with no direct requester registration;
5. a changed method, trigger, owner, endpoint, session, transcript, or
   private G tuple under the same later audit request;
6. one create capability, reply nonce, active capability, or request number
   replayed cross-session or post-close; and
7. every receipt/commit/reply/ACTIVE/ACK/abort send failure above.

The required predicates must differ without trusting requester obedience,
G self-report, queue readiness order, a public digest, or an unperformed
operation.

## 4. D-M2 minimum actual-FD, quiescence, unwind, and ABA contract

### 4.1 Exact primitive and narrow v4 FD-5 supersession

The sole foreign-FD acquisition primitives are native Linux x86_64:

```text
pidfd_open(outer_pid, flags=0), syscall number 434
pidfd_getfd(pidfd, targetfd, flags=0), syscall number 438
```

They use the byte-bound native x86_64 little-endian LP64 binding.  The x32
table remains killed.  There is no libc/header-selected alternate, helper,
pathname-following `stat`, `SCM_RIGHTS`, `kcmp`, ptrace attachment, service,
other architecture, or fallback.  Success must produce a nonnegative
P-local FD with exactly `FD_CLOEXEC` under `fcntl(F_GETFD)`.  The exact
runtime `pidfd_getfd` success under the kernel's
`PTRACE_MODE_ATTACH_REALCREDS` check is the permission preflight; permission
is not inferred from uid, capability, kernel version, proc access, LSM text,
or `ptrace_scope`.  Every errno or ambiguous result is fail-closed.

The v4 FD-5 rule is superseded only inside one exact interval:

```text
FD_AUDIT_QUIESCED
  -> successful pidfd_getfd(exact child pidfd, targetfd=5, flags=0)
  -> fstat/compare/reciprocal-diag
  -> close exact P-local duplicate
  -> immediate F_GETFD=-1/EBADF
  -> FD_AUDIT_EXIT_ACKED
```

During that interval the child retains its original FD 5, P retains the one
opposite audit peer, and P may hold exactly one additional duplicate of the
child endpoint returned by that one call.  It may perform only `F_GETFD`,
`fstat`, nonmutating type/inode comparison, and derivation of the diag query
inode.  It is never read, written, sent, received, polled for payload,
transferred, duplicated again, or retained across interval exit or original
close.  Outside the interval the absolute v4 no-duplicate and holder matrix
remain exact.  The requester still closes original FD 5 only at the retained
post-terminal-reply edge.

The same audit-only temporary P holder rule applies to actual child slots 4
and 8 and each exact G candidate acquired below.  It changes no permanent
owner, FDSET row, admission token, or serialized count.

### 4.2 Per-slot pidfd and proc-capability table

`SLOT` is the closed enum `FD4|FD5|FD8`.  `AUDIT_KIND` is exactly
`PREFLIGHT_PROBE|RUNTIME_CHILD`.  Every audit binds one fresh monotone
`audit_epoch`, one registered child, one exact numeric target slot, and the
following capability row; no wildcard row is legal:

| AUDIT_KIND | SLOT | retained child pidfd | retained guardian pidfd | fresh child proc PID dir / fd dir | fresh G proc PID dir / fd dir | P retained opposite peer |
|---|---|---:|---:|---:|---:|---:|
| PREFLIGHT_PROBE | FD8 | 1 | 1 | 1 / 1 | 1 / 1 | 0 |
| RUNTIME_CHILD | FD8 | 1 | 1 | 1 / 1 | 1 / 1 | 0 |
| RUNTIME_CHILD | FD4 | 1 | 1 | 1 / 1 | 1 / 1 | 0 |
| RUNTIME_CHILD | FD5 | 1 | 1 | 1 / 1 | 1 / 1 | 1 |

The preflight row uses only the already frozen epoch-1
`CGROUP_PROBE_CHILD` while blocked at its FD-8 barrier.  It creates no new
child, target, method, probe epoch, or session-zero row.

That complete row, including quiesce, both proc snapshots, actual child/G
acquisitions, fstats, reciprocal diag, unconditional unwind, EBADF proofs,
and EXIT_ACK, must pass under the actual nested uid/gid maps, dumpable-zero
rule, cgroup placement, and process credentials before any package, result,
package-lock, private generation-root, generated-member, or subject write.
Failure invokes the retained bootstrap kill/reap/populated-zero cleanup and
returns `E_POSSESSION_UNAVAILABLE`; it cannot select a fallback.

P opens exactly one child pidfd after the child's first-instruction identity
and while it remains blocked.  Before and after opening it joins outer PID,
start time, full `NSpid`, uid/gid, one-thread state, child/session/role/owner,
and workers-cgroup membership.  The pidfd is retained through every audit,
exit, wait/reap, and `CHILD_REAPED` reconciliation.  It is then closed once
and immediately proved `F_GETFD=-1/EBADF` without intervening allocation.
A pidfd returned before any failed post-open validation is entered in the
pidfd ledger, closed once, and proved absent on that same failure path.

The guardian pidfd is exactly the one existing authenticated P-held
guardian capability; it is never re-opened per slot.  Its outer PID, start
time, `NSpid`, credentials, one-thread state, and guardian-cgroup identity
are revalidated at each row.  No child pidfd names G and no guardian pidfd
names a child.

P also owns exactly one shared proc-root capability for all rows.  Before
the preflight child exists, P opens literal `/proc` exactly once with
`O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC`, requires directory type and
exact `FD_CLOEXEC`, and prevents inheritance by L, G, or any child.  It is
never duplicated, serialized, or used to open anything except the exact
per-row PID directories below.  P retains it through the final endpoint
audit, then closes it exactly once on orderly teardown (or bootstrap failure)
and immediately requires `F_GETFD=-1/EBADF` without intervening allocation.

Inside the audit allocation barrier and after G's quiesce ACK, P opens each
fresh proc capability exactly as:

```text
proc_pid_dirfd = openat(held_proc_root_fd, canonical_outer_pid_decimal,
                        O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
proc_fd_dirfd  = openat(proc_pid_dirfd, "fd",
                        O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
```

Each must be a directory, have exactly `FD_CLOEXEC`, and join to the same
live pidfd/start-time/NSpid/credential/cgroup identity before the first
snapshot and after the second.  The fd-directory offset is reset only with
`lseek(fd,0,SEEK_SET)` returning zero before each exact `getdents64` pass.
Only canonical decimal entries, `getdents64`, and bounded `readlinkat` of an
exact entry are permitted.  A proc link is comparison text only; it is never
followed or relabelled as actual-descriptor `fstat` evidence.

Every fresh proc PID and fd directory is entered in the audit ledger and
remains open through both snapshots, all acquisitions, all fstats, and all
reciprocal diag comparisons.  Both are unconditionally closed and
immediately proved `EBADF` on success and every error path before the
quiesce exit.  A partial open closes and proves every earlier proc FD.  No
proc capability escapes its exact row.

### 4.3 Exact G-quiescence protocol and prohibited interval

The amendment must add exactly these four P--G payload forms:

```text
P -> G:
FD_AUDIT_QUIESCE_ENTER audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT child_pidfd_serial=DEC guardian_pidfd_serial=DEC

G -> P:
FD_AUDIT_QUIESCE_ACK audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT g_fd_generation=DEC

P -> G:
FD_AUDIT_QUIESCE_EXIT audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT g_fd_generation=DEC outcome=AUDIT_OUTCOME transcript=LOWERHEX64

G -> P:
FD_AUDIT_QUIESCE_EXIT_ACK audit_epoch=DEC kind=AUDIT_KIND session=DEC child=DEC slot=SLOT g_fd_generation=DEC outcome=AUDIT_OUTCOME transcript=LOWERHEX64
```

`AUDIT_OUTCOME` is exactly `PASS|ABORT`.  `g_fd_generation` is a G-owned
monotone nonzero operational counter bound to the exact quiesce interval;
it is not P's evidence for descriptor identity.  `transcript` is P's
domain-tagged SHA-256 binding.  For PASS it covers, in exact execution order,
both complete snapshots; every obtained-FD fstat; the two pre-unwind
reciprocal diag responses; the complete close/EBADF ledger; the two
post-unwind reciprocal diag responses; and the final restored permanent-
holder matrix, including FD5's current zero-G-holder result.  Thus all four
diag responses are distinct transcript entries.  For ABORT it covers the
exact successfully observed prefix, the first failing stage/errno or
mismatch, explicit `MISSING` tokens for every later unperformed stage, and
the complete unwind ledger.  It is not a replacement for any primitive
observation and never asserts an unperformed observation.

For `PREFLIGHT_PROBE`, `session=0`; for every `RUNTIME_CHILD` row it is the
child's exact registered session.  `child_pidfd_serial` is always that
child's nonzero retained serial.  `guardian_pidfd_serial` is the exact
nonzero retained guardian serial for every row, including FD5's current
zero-holder audit.  No sentinel or omitted field is legal.

G accepts ENTER only in the exact corresponding frozen child barrier with
no earlier quiesce open.  It first completes or rejects every already-started
FD-mutating action, drains no new requester operation, increments the
generation, enters `G_FD_QUIESCED`, and then sends ACK.  ACK is valid only
if its complete send succeeds.  From before ACK through complete EXIT_ACK,
G may use only its already-held P control FD to receive the matching EXIT
and send the ACK.  It may not call or perform any descriptor-table mutation,
including `open*`, `creat`, `close`, `close_range`, `dup*`, `fcntl` duplicate,
`socket*`, `socketpair`, `accept*`, `pipe*`, `eventfd*`, `signalfd*`,
`timerfd*`, `inotify*`, pidfd creation, `SCM_RIGHTS` receipt/installation,
`fork`, `clone`, `exec`, signal-handler allocation, library lazy-open, or
another operation that can allocate, install, replace, or close an FD.

The interval spans, without a gap:

```text
G quiesce ACK
  -> child and G proc capability opens/identity joins
  -> first exact descriptor snapshots
  -> every child and G pidfd_getfd acquisition
  -> every F_GETFD/fstat/proc comparison
  -> every reciprocal Unix-diag request/response
  -> second exact descriptor snapshots and equality checks
  -> every acquired duplicate and proc-FD close/EBADF proof
  -> reciprocal re-query of the still-live original endpoint pair
  -> restored-holder proof
  -> EXIT / EXIT_ACK
```

The child is independently blocked at its already frozen barrier for this
same complete interval and may not mutate its FD table.  G single-threaded
status alone is not quiescence.  P's observation of equal snapshots alone
is not quiescence.  Only the closed state plus the independent snapshots and
actual acquisitions supplies the join.

On `PASS`, G resumes FD-mutating work only after the complete EXIT_ACK send
succeeds.  On `ABORT`, G sends EXIT_ACK but does not reopen admission or
resume the failed session; it proceeds to retained containment.  ENTER send
or ACK failure, wrong generation, replay, control EOF, or EXIT/EXIT_ACK
failure is whole-control containment with no thaw or original close inferred.

### 4.4 Allocation barrier, acquisition ledger, and actual comparison

P is single-threaded and enters one P-local `FD_AUDIT_ALLOCATION_BARRIER`
before opening the fresh proc capabilities.  The sole already-open Netlink
Unix-diag socket remains the exact v4 oracle.  No P code outside the audit
may open, accept, duplicate, receive, or close an FD until every audit-owned
FD is closed and proved absent.  The retained handled signal set
`HUP,INT,QUIT,PIPE,ALRM,TERM,USR1,USR2` remains blocked process-wide and its
already-held signalfd is not read during the barrier.  P has no asynchronous
user handler for any signal; every other catchable signal retains a default
disposition that invokes no P code, while uncatchable `SIGKILL`/`SIGSTOP`
cannot invoke P code; their stop/death yields no successful audit and enters
the retained external crash containment.  Any default stop/termination has
the same no-success disposition.  P verifies the same mask/dispositions at
barrier entry and after EXIT_ACK.  Therefore no handler, second thread,
callback, or signal-time library action can intervene in a continuing audit
between a successful FD-returning syscall and its ledger insertion, or
between `close` and the immediate `F_GETFD` proof.

Before the first proc open, P preallocates fixed ledger slots for every
row's exact four proc FDs plus one child
duplicate.  After those proc FDs are recorded and the first snapshot fixes
the exact G socket-candidate count, but before any `pidfd_getfd`, P
preallocates exactly that many additional G-candidate slots.  Failure of
either memory allocation runs the same common unwind; therefore no returned
proc FD or duplicate can exist without an already reserved ledger slot.

Each successful syscall result is written immediately into the next ledger
slot before any other fallible action:

```text
(audit_epoch, acquisition_serial, local_fd, kind,
 target_pidfd_serial, targetfd, state=OPEN)
```

`acquisition_serial` is monotone and never reused.  All acquired duplicates,
including nonmatching G candidates, remain open until the common unwind, so
the kernel cannot reuse a local numeric FD inside the interval.  A duplicate
local number while an earlier ledger entry is OPEN is terminal.  Numeric FD
equality never establishes object identity.

For the exact child slot P performs

```text
pidfd_getfd(exact retained child pidfd, exact targetfd 4|5|8, flags=0)
  -> exact FD_CLOEXEC
  -> fstat obtained duplicate
  -> S_IFSOCK and nonzero st_ino <= 0xffffffff
  -> compare canonical proc text to that actual fstat inode
  -> diag(actual child fstat inode)
```

For FD4 and FD8, P enumerates the complete canonical G numeric set in the
first snapshot, obtains and fstats every proc-selected socket candidate via
`pidfd_getfd(exact guardian pidfd, exact targetfd,0)`, and retains each
duplicate in the ledger.  Exactly one candidate must have the diag-returned
peer inode and registered holder role.  Zero, two, a failed acquisition, or
another selected candidate state is terminal.  It then requires:

```text
diag(child_actual_fstat_inode) = G_peer_actual_fstat_inode
diag(G_peer_actual_fstat_inode) = child_actual_fstat_inode
```

For FD5, P uses the actual child duplicate and directly fstats its one
retained local audit peer.  It also enumerates the complete canonical G
numeric set and, exactly as for FD4/FD8, acquires and fstats every
proc-selected G socket candidate through the retained guardian pidfd.  Zero
G candidate fstat inodes may equal either the actual child-FD5 endpoint inode
or the actual P-peer inode; every candidate remains in the common ledger.
This current quiesced acquisition, not the historical holder matrix, proves
that G has zero FD-5 endpoint or peer copies.  The child/P-peer reciprocal
equality is required before unwind and again after unwind.  All Unix-diag
request/response bytes, sequence/port/source/cardinality rules, crossed-pair
preflight, and no-fallback ABI from v4 remain exact.

P then takes the complete second child/G numeric snapshots through the same
held proc FDs and requires byte equality with the first snapshots, stable
pidfd/process identity, and unchanged G generation.  Quiescence makes an
equal numeric set meaningful: G and the child were forbidden to close and
replace a same-number entry.  The actual duplicate fstats and reciprocal
diag mapping, not the numbers or proc strings, establish socket identity.

### 4.5 One unconditional success/error unwind and EBADF proof

The amendment must implement one `finally`-equivalent unwind entered after
the first audit-owned FD is opened, on success and after every later error.
It walks every OPEN ledger entry exactly once in reverse acquisition order.
For each entry it:

1. calls `close(exact local_fd)` exactly once and never retries;
2. records whether the return was exactly zero;
3. with no intervening P allocation, immediately calls
   `fcntl(exact local_fd,F_GETFD)`; and
4. requires exactly `-1` with `errno=EBADF`, then marks that exact
   `(audit_epoch,acquisition_serial,local_fd)` entry `CLOSED_PROVED`.

A close error does not short-circuit disposal of later ledger entries.  A
nonzero close return, a non-EBADF result, an unvisited entry, a duplicate
close, or an allocation between close and proof is terminal.  If every FD
is absent but another audit predicate failed, P sends EXIT with `ABORT` and
G remains contained.  If any FD absence cannot be proved, P never sends a
normal EXIT, never thaws/releases a barrier, and never closes an original
endpoint; after attempting every other ledger close it invokes the existing
crash-only containment so process teardown, not a false receipt, removes the
ambiguous local reference.  That path cannot emit PASS, ABSENT, successful
cleanup, or a new public result.

On a clean unwind, after all temporary duplicates are absent P re-queries
the still-live original pair in both directions through the retained v4
Netlink socket.  It requires the same reciprocal inode mapping and the
retained permanent holder matrix.  All proc FDs are then already absent,
the local allocation barrier is released only after EXIT_ACK, and no audit
duplicate can cross an original endpoint close, thaw, child start, kill,
reap, or requester terminal reply.

The distinct long-lived pidfd ledger is total too: every pidfd returned
before failed validation is closed/proved on that failure path; every valid
child pidfd remains through exit/reap/reconciliation and is then
closed/proved; the guardian pidfd keeps its existing lifetime through G
reap.  A local numeric FD reused only after a prior `CLOSED_PROVED` entry and
after the audit barrier ends belongs to a new acquisition generation and
cannot satisfy the tombstoned tuple.  These rules close both target-table
and P-local FD-number ABA worlds.

### 4.6 Mandatory D-M2 hostile pairs

The later reviewer must be able to distinguish at least:

1. a pidfd and target slot with the same decimal but different objects;
2. an outer PID reused at a different start time;
3. canonical proc text naming inode A while actual duplicate `fstat` gives B;
4. true child endpoint paired with the wrong one of two simultaneous G peers;
5. G closing FD N and opening a different socket at N between superficially
   equal snapshots;
6. a first successful duplicate followed by failure of CLOEXEC, fstat, proc
   comparison, a later acquisition, diag, second snapshot, or uniqueness;
7. a returned pidfd followed by failed post-open validation;
8. one temporary duplicate or proc FD retained across original close,
   barrier release, thaw, kill, or reap;
9. a local FD number reused under a different acquisition generation; and
10. actual `pidfd_getfd` denial while proc and Unix-diag remain readable.

Trust in G, equal numbers, a copied inode, inferred privilege, a generic
cleanup sentence, or a different kernel primitive cannot distinguish these
pairs and is not a repair.

## 5. Required preservation of prior closures

Amendment v6 must retain without weakening:

1. v4 `C-M1`: child-unique P-created FD 5, exact FDSET row, kernel
   credentials, P-issued one-use child-request nonce, requester-direct bytes,
   actual FD-4 bytes, exact comparison, G confirmation, audited registration,
   and P-derived admission;
2. v4 `C-M2`: exact 40-byte request and 48-byte response, sequence/port/
   source/cardinality rules, two simultaneous preflight pairs, reciprocal
   `UNIX_DIAG_PEER`, crossed-pair rejection, owner matrix, and no fallback;
3. v3 `B-M1`: two operational owners, six exact session-zero rows, closed
   post-suite owner grammar, and exact 173-method boundary;
4. v3 `B-M2`: phase-indexed descriptor sets, admission barrier, source/root/
   RPC lifetimes, drain, EOF, close, and reap order, strengthened only by
   Section 4's explicit quiesced audit interval;
5. v3 `B-M3`: G-created pre-access register/ACK, authorized-basename/purpose
   generator creation, post-reap enumerate/register/ACK before exchange/
   cleanup/reference audit, P25 count zero, and unexpected-object
   nondeletion;
6. `A-M1`: exact unparameterized `SG_SCOPE`, primitive-only evidence-class
   projection, expected class only after recomputation, and all primitive-
   prefix/witness counterfactuals;
7. `A-M2`: real-filesystem recursive receipts, valid/malformed variants,
   five live metadata falsifiers, and exact-one-coordinate mode/mtime probes
   cloned from actual receipts without ctime masking;
8. `A-M3`: private possession, namespace/cgroup containment, retained parent/
   root/lock capabilities, capability-relative cleanup, both replacement
   phases, all replacement fixtures, foreign preservation, and no false
   `ABSENT`;
9. `A-M4`: complete-review authentication before parsing, canonical unique
   effective-amendment list, capability-relative independent reads/hashes,
   and dereference before lifecycle adjacency; and
10. the v5 blocked/no-op status: its hash remains provenance and none of its
    discarded attempted repair forms becomes effective by implication.

A v6 repair that regresses any retained closure creates a new open finding.
It cannot trade one finding for another or declare a conditional pass.

## 6. Frozen counts, paths, schemas, and DAG

Amendment v6 and its later re-review must preserve exactly:

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
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
```

The six implementation paths, eight CSV paths and literal headers, all 120
rows and order, 35 explicit negatives, 35 semantic methods, 28 package
methods, 173 method names, nine generated paths, fourteen authority paths,
manifest keys/schema, and graph nodes `A,D,R,G,I,C,M,V` with twelve distinct
edges remain unchanged.  Capabilities, transcript digests, session states,
pidfds, proc FDs, quiesce records, acquisition ledgers, and close receipts
are operational, in-memory, and nonserialized.

If either repair requires a CSV/schema/generated-byte change, seventh
implementation path, new method/target/mutation/public detector/exit class,
authority binding, manifest node/edge, theorem owner, Route, or publication
boundary, amendment v6 must stop and record a new design finding instead of
silently widening this gate.

## 7. Append-only count-six successor while preserving A-M4

The current review's historical `v1` count-two, `v2` count-three, `v3`
count-four, and `v4` count-five blocks cannot be edited, normalized,
reordered, duplicated, or treated as the new active list.  After amendment
v6 is frozen and externally hashed, the fresh independent reviewer must
append exactly one active successor block:

```text
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
```

There is no blank or commentary line inside an actual block.  Amendment v6
must version the internal review-node grammar so the final verifier:

1. capability-opens the unchanged manifest-bound review path once, applies
   the existing regular/nlink-one/no-link rules, hashes the complete post-v6
   review from that FD, and matches the manifest-bound complete digest before
   parsing;
2. requires exactly one byte-identical historical v1, v2, v3, and v4 block,
   exactly one active v5 block in the count-six form above, and no other
   effective-amendment begin/end tag;
3. rejects missing, duplicate, reordered, nested, malformed, prefix-drifted,
   wrong-count/index/path/digest/version, extra-key, blank, or commentary-
   bearing blocks;
4. independently capability-opens v1 through v6 in active order beneath the
   same held package-root FD with the retained beneath/no-link rules, reads
   every byte, and recomputes all six hashes; and
5. only after every match sets the nonserialized obligation
   `R.effective_amendments=[v1,v2,v3,v4,v5,v6]` before lifecycle adjacency.

This dereference changes no manifest key, binding count, generated artifact,
node, edge, review self-hash, future-result edge, or proof cycle.

## 8. Sole later append-only independent re-review

Only after amendment v6 is frozen and externally hashed may an independent
reviewer append once to:

```text
notes/phase2_control_design_peer_review.md
```

The complete current 143812-byte / 2746-line file at SHA-256
`30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb`
must remain its exact prefix, preserving every nested prefix and all four
existing blocks.

The reviewer must independently read and hash the complete
`base + v1 + v2 + v3 + v4 + blocked-v5 + v6` tuple and attack, rather than
restate:

1. entropy syscall 318, exact 32-byte fills, first-disclosure edges,
   collision policy, secret surfaces, and the distinction among one-use
   create capability, one-use reply nonce, and session operation capability;
2. direct registration, exact create/created bytes, P/G transcript joins,
   actual-reply witness, ACTIVE/ACK gate, all eight non-child creator forms,
   delegated endpoint birth, one-use/replay/tombstone rules, and every send-
   failure/abort/cleanup branch;
3. the D-M1 early-queue worlds with all public tuple fields fixed, proving a
   valid early create lacks `create_cap`, an early activation lacks
   `reply_nonce`, and an early operation lacks `active_cap`;
4. syscall numbers 434/438, zero flags, actual permission success, exact
   per-slot pidfd/proc table, identity joins, open flags, lifetimes, and no
   fallback;
5. exact G quiesce ENTER/ACK/EXIT/ACK, prohibited mutations, child barrier,
   two snapshots, every acquisition/fstat/diag comparison, restored-holder
   proof, and every success/error unwind;
6. bounded FD-5 temporary-holder supersession, allocation ledger, no local
   FD reuse while live, reverse close, immediate EBADF, pidfd normal/error
   close, and both G-table and P-local ABA hostile worlds;
7. every retained closure and every invariant in Sections 5--6; and
8. four immutable historical blocks, one unique active count-six successor,
   six independent amendment dereferences, fourteen bindings, and unchanged
   eight-node/twelve-edge DAG.

The reviewer may close `D-M1` or `D-M2` only from its own evidence.  This
gate does not predict that result.  Only a later independent effective
verdict `PASS C0/M0/m0` could support consideration of a separate
implementation gate.  Partial repair, author self-audit, predictable
digest, queued-message priority, G-only assertion, proc-text-only inode,
inferred permission, unproved local-FD lifetime, or fallback remains
`REVISE`.

## 9. Authorization matrix

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V6=PASS_TO_ONE_AMENDMENT_V6
CURRENT_OPEN_FINDINGS=C0_M2_m0
D_M1_STATUS=OPEN
D_M2_STATUS=OPEN
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v6.md
AMENDMENT_V6_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V6_FROZEN_AND_EXTERNALLY_HASHED=true
CURRENT_REVIEW_PREFIX_SHA256=30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb
CURRENT_REVIEW_PREFIX_LINES=2746
CURRENT_REVIEW_PREFIX_BYTES=143812

D_M1_CREATE_CAP_SOURCE=P_ONLY_GETRANDOM_32_FLAGS_0
D_M1_CREATE_CAP_FIRST_DISCLOSURE=SESSION_AUTH_RECEIPT
D_M1_CREATE_CAP_SINGLE_USE=true
D_M1_REPLY_NONCE_FIRST_DISCLOSURE=ACTUAL_SESSION_CREATED
D_M1_REPLY_NONCE_SINGLE_USE=true
D_M1_ACTIVE_CAP_MINTED_AFTER_ACTUAL_REPLY_JOIN=true
D_M1_ACTIVE_CAP_SESSION_SCOPED=true
D_M1_P_TO_G_ACTIVE_ACK_REQUIRED=true
D_M1_NONCHILD_FD4_BEFORE_ACTIVE_AUTHORIZED=false
D_M1_G_SELF_REPORT_IS_INDEPENDENT_EVIDENCE=false
D_M1_TOMBSTONE_REUSE_AUTHORIZED=false

D_M2_PIDFD_OPEN_X86_64_SYSCALL=434
D_M2_PIDFD_GETFD_X86_64_SYSCALL=438
D_M2_PIDFD_FLAGS=0
D_M2_PIDFD_GETFD_FLAGS=0
D_M2_FD5_DUPLICATE_ONLY_INSIDE_AUDIT_INTERVAL=true
D_M2_G_QUIESCE_ENTER_ACK_EXIT_ACK_REQUIRED=true
D_M2_UNCONDITIONAL_SUCCESS_ERROR_UNWIND=true
D_M2_IMMEDIATE_EBADF_PROOF_REQUIRED=true
D_M2_G_AND_P_ABA_PREVENTION_REQUIRED=true
D_M2_FALLBACK_AUTHORIZED=false

BASE_COUNTS_MUST_REMAIN_UNCHANGED=true
SIX_IMPLEMENTATION_PATHS_MUST_REMAIN_UNCHANGED=true
EIGHT_CSV_PATHS_MUST_REMAIN_UNCHANGED=true
MANIFEST_SCHEMA_MUST_REMAIN_UNCHANGED=true
AUTHORITY_BINDING_COUNT_MUST_REMAIN_14=true
PRINTED_DAG_MUST_REMAIN_8_NODES_12_EDGES=true
ALL_PRIOR_CLOSURES_MUST_NOT_REGRESS=true
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
```

This gate does not embed its own SHA-256.  Amendment v6 and the one later
fresh independent append-only re-review must bind this file's externally
computed final digest.  No finding is closed by this authorization.

---

# Append-only v6 authority-surface correction

Status: **FROZEN NARROW CORRECTION — C0/M2/m0 OPEN**  
Correction ID: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v6.0-FD5-ENUM`  
Date: 2026-08-17 (Asia/Shanghai)

## C1. Preserved prefix and sole omission corrected

The complete gate before this addendum is preserved byte-for-byte as the
first 58,261 bytes and 1,140 lines of this file.  That exact prefix has
SHA-256
`81d5543fdd0acc72122cd9a2171a7354a7d51d7d4a2f2c8f6a78fb12b3af7dcc`.
Nothing in that prefix is rewritten, normalized, renumbered, or withdrawn.

Section 2 says that its supersession budget is exhaustive, while Section
3.2 requires six new requester--P FD-5 forms in addition to the four forms
closed by amendment v4 Section 3.3.  The original Section 2 list omitted the
corresponding authority surface.  This addendum corrects only that omission.
It does not re-review a finding, alter evidence, or assert closure.

The effective Section 2 supersession budget is the original six numbered
items plus exactly this one permitted surface:

> Amendment v4 Section 3.3's closed four-form FD-5 payload enum may be
> superseded solely to replace that enum with the exact ten-form FD-5
> payload enum already printed in this gate's Section 3.2.

The exact replacement enum, with no optional direction or form, is:

```text
requester -> P: SESSION_AUTH_OPEN
P -> requester: SESSION_AUTH_CHALLENGE
requester -> P: SESSION_AUTH_REGISTERED
P -> requester: SESSION_AUTH_RECEIPT
requester -> P: SESSION_AUTH_ACTIVATED
P -> requester: SESSION_AUTH_ACTIVE_RECEIPT
requester -> P: AUDIT_OPEN
P -> requester: AUDIT_CHALLENGE
requester -> P: AUDITED_SPAWN
P -> requester: AUDIT_RECEIPT
```

The complete field order and byte grammar for all ten forms are exactly the
forms printed in Section 3.2; this addendum does not redefine them.  The last
four remain byte-identical to amendment v4 Section 3.3.  The first six are
exactly the six session-auth forms already mandated by Section 3.2.  There
is no eleventh FD-5 payload form, wildcard form, optional form, alternate
direction, or implied close form.

## C2. No lifetime or collateral authority expansion

This correction changes enum membership only.  It does not supersede the
v4 requester FD-5 terminal lifetime, endpoint ownership, transport,
credential, EOF, or close rules except for admitting the six exact Section
3.2 payloads before the retained terminal edge.  In particular:

1. no requester FD-5 frame is legal after the requester receives its
   terminal FD-4 reply;
2. the requester still closes FD 5 at that retained v4 edge;
3. there is no post-`SESSION_CLOSED` session-auth frame or close handshake;
4. the retained peer and endpoint close/reap order is unchanged; and
5. no other amendment-v4 clause or original Section 2 authority surface is
   superseded by this correction.

If amendment v6 requires an eleventh form, any different field or direction,
an FD-5 lifetime extension, a changed terminal edge, or another authority
surface not already exhaustively permitted by Section 2 plus this correction,
it must stop rather than infer permission.

## C3. Unchanged verdict and sole downstream authorization

`D-M1` and `D-M2` remain open Major findings.  The effective gate verdict
remains **PASS TO ONE VERSIONED DESIGN AMENDMENT v6 — C0/M2/m0 OPEN**.
Exactly one design-only target remains authorized:

```text
notes/phase2_control_design_amendment_v6.md
```

Only after that amendment is frozen against the externally computed final
digest of this corrected complete gate may one fresh independent append-only
re-review be added to the existing peer-review file.  This correction itself
closes no finding and authorizes no implementation or execution.

```text
P15R_GATE_V6_AUTHORITY_CORRECTION=FD5_ENUM_4_TO_EXACT_10_ONLY
PRESERVED_GATE_PREFIX_SHA256=81d5543fdd0acc72122cd9a2171a7354a7d51d7d4a2f2c8f6a78fb12b3af7dcc
PRESERVED_GATE_PREFIX_LINES=1140
PRESERVED_GATE_PREFIX_BYTES=58261
V4_SECTION_3_3_FD5_ENUM_SUPERSESSION_AUTHORIZED=true
FD5_ENUM_CARDINALITY=10
FD5_ELEVENTH_FORM_AUTHORIZED=false
FD5_TERMINAL_LIFETIME_CHANGED=false
OTHER_AUTHORITY_EXPANSION_AUTHORIZED=false
CURRENT_OPEN_FINDINGS=C0_M2_m0
D_M1_STATUS=OPEN
D_M2_STATUS=OPEN
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v6.md
FRESH_APPEND_ONLY_REREVIEW_ONLY_AFTER_AMENDMENT_V6_FREEZE=true
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```
