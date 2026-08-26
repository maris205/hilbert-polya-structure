# Replacement Paper 15 Phase-2 control-design remediation gate v7

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v7 — C0/M1/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v7.0`  
Date: 2026-08-17 (Asia/Shanghai)

This is a bounded design-remediation authorization, not a finding closure.
The current independent review's sole Major finding, `D-M1` as refined by
`F-M1.a` and `F-M1.b`, remains open.  `D-M2` is independently closed and is
frozen against regression.  This gate authorizes exactly one design-only
amendment and, only after that amendment is frozen and externally hashed,
one fresh independent append-only re-review.  It authorizes no generator,
verifier, test, wrapper, implementation, control execution, reproduction
run, Route, composition, manuscript, figure, release, archive, Git action,
or public synchronization.

## 1. Exact authority and retained verdict

The complete current bytes of all fourteen records below were freshly read
and independently re-hashed before this gate was written:

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
| current append-only review | `notes/phase2_control_design_peer_review.md` | 3149 | 165177 | `075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c` |

The corrected v6 gate preserves an exact 58,261-byte / 1,140-line prefix at
SHA-256
`81d5543fdd0acc72122cd9a2171a7354a7d51d7d4a2f2c8f6a78fb12b3af7dcc`.
The review is one append-only byte string.  Its exact nested prefixes are:

| Prefix lines | Prefix bytes | SHA-256 |
|---:|---:|---|
| 2746 | 143812 | `30aff47781dc182d15978d831e89ae720b5f34518b58173401b62adc6fec8ceb` |
| 2308 | 119250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` |
| 1910 | 96524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1524 | 74876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1017 | 49358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

The current effective verdict is exactly **REVISE — C0/M1/m0**.  V6 closes
the early predictable-queue worlds and closes `D-M2`, but `D-M1` remains
open because:

1. G receives raw `create_cap` and the complete future create bytes before
   the alleged actual FD-4 receipt, so its accepted record is synthesizable
   from the grant; and
2. P has no observation after its close ACK which distinguishes a complete
   terminal FD-4 reply send from an incomplete or failed send.

No gate, amendment self-audit, commitment name, G-only send result, copied
digest, or fail-closed assertion is evidence against this finding.  The
theorem owner remains the bare compact group `B_p`; universal recovery
remains `OPEN_NOT_AUTHORIZED`; Route B remains false.

The current review contains exactly five effective-amendment blocks.  Its
historical `v1` through `v4` blocks and its active `v5` count-six block are
immutable prefix authority.

## 2. Sole target, precedence, and exact supersession budget

The target was absent before this gate was created.  Exactly one new design
file may be created:

```text
notes/phase2_control_design_amendment_v7.md
```

After that file is frozen and externally hashed, the versioned chain is
exactly base + amendments v1--v4 + blocked/no-op v5 + v6 + v7.  Amendment
v7 may supersede only these surfaces:

1. amendment-v6 `SESSION_AUTH_CREATE_GRANTED` and
   `SESSION_AUTH_CREATE_ACCEPTED` fields, the FD-5
   `SESSION_AUTH_RECEIPT.create` byte interpretation, and create-state edges,
   solely to replace pre-receipt disclosure to G with Section 3's
   commitment/template arming and exact full-frame first-receive raw return;
2. amendment-v6 `SESSION_AUTH_ACTIVE` and `SESSION_AUTH_ACTIVE_ACK` fields
   and ACTIVE edge, solely to replace raw pre-operation disclosure to G with
   the bounded active commitment in Section 4;
3. amendment-v6 `SESSION_AUTH_SESSION_CLOSED` and
   `SESSION_AUTH_CLOSE_ACK`, the corresponding close states and failure
   rows, and the v2 terminal `SESSION_CLOSED` reply shape, solely to install
   Section 5's terminal preparation, fresh capability, requester-direct
   observation, finalization, and receipt sequence;
4. amendment-v6's exactly-three D-M1 capability-kind inventory, solely to
   add the fourth kind `terminal_cap` under the same exact entropy and
   collision rules;
5. amendment-v4 Section 3.3 and corrected-gate-v6 Section C1's exact-ten
   FD-5 enum, solely to replace it with Section 5's exact-twelve enum;
6. amendment-v4 Sections 3.6 and 4.6, corrected-gate-v6 Sections 2/C2, and
   amendment-v6 Sections 1.2, 3.2, 3.4--3.6, 4.1, 4.6, and 5 only where
   they require no post-terminal FD-5 frame or immediate close after the
   terminal FD-4 reply; the only permitted lifetime extension is through
   `SESSION_AUTH_TERMINAL_OBSERVED`, finalization,
   `SESSION_AUTH_TERMINAL_RECEIPT`, and clean FD-5 EOF; and
7. amendment-v6 Section 6's review-node successor grammar, solely so the
   current active count-six block becomes historical and a later active
   count-seven block ends at v7.

The four D-M2 FD-audit records and every D-M2 syscall, permission, pidfd,
proc-capability, identity, quiescence, snapshot, acquisition, actual-fstat,
Unix-diag, transcript, common-unwind, EBADF, holder-restoration, and ABA
clause are not superseded.  References to the old FD-5 close edge are
mechanically redirected to the new terminal-receipt/EOF edge only; no
D-M2 observation or lifetime is weakened.

Every changed form, field, direction, state, disclosure, complete-send edge,
failure edge, and close edge must be exhaustive in amendment v7.  Every
omitted base/v1--v6 clause remains binding; blocked v5 still contributes no
operational clause.  No optional form, thirteenth FD-5 form, thirteenth D-M1
P--G form, wildcard, alternate entropy source, fallback, public detector,
or unstated retry is permitted.

## 3. F-M1.a repair — commitment-only create arming

### 3.1 Exact commitment grammar

Define `U32BE(n)` and `U64BE(n)` as the exact four- and eight-byte unsigned
big-endian encodings.  For byte strings `identity` and `payload`, define:

```text
P15R_V7_BIND(domain,identity,payload) =
  SHA256(ASCII(domain) || 0x00 ||
         U64BE(len(identity)) || identity ||
         U64BE(len(payload)) || payload)
```

There is no trailing byte or alternate framing.  `create_identity` is one
canonical ASCII line, fields in exactly this order:

```text
requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC method=METHOD trigger=TRIGGER owner=OWNER fd4_endpoint_inode=DEC rpc_inner_pid=DEC rpc_inner_uid=0 rpc_inner_gid=0
```

The exact final create payload remains:

```text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC create_cap=LOWERHEX64
```

Let `create_payload` be those exact canonical ASCII bytes.  The exact raw
FD-4 create request is one seqpacket datagram:

```text
create_frame = U32BE(len(create_payload)) || create_payload
```

The four-byte value is the inherited RPC payload length and counts only
`create_payload`.  There is no second frame, trailing byte, or alternate
framing.

The exact redacted template replaces only its capability value with the
literal fourteen ASCII bytes `{CREATE_CAP64}`:

```text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC create_cap={CREATE_CAP64}
```

`{CREATE_CAP64}` is not `LOWERHEX64` and can never be accepted as a packet
value.  It occurs exactly once.  The exact commitment is:

```text
create_commitment =
  P15R_V7_BIND("P15R-CREATE-COMMITMENT-v7",
                create_identity,
                create_frame)
```

### 3.2 Exact create records and non-disclosure

The first two v6 P--G session records retain their names but replace their
payloads exactly:

```text
P -> G:
SESSION_AUTH_CREATE_GRANTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC registration_digest=LOWERHEX64 create_commitment=LOWERHEX64 template=LOWERHEX fd4_endpoint_inode=DEC rpc_inner_pid=DEC rpc_inner_uid=0 rpc_inner_gid=0

G -> P:
SESSION_AUTH_CREATE_ACCEPTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC registration_digest=LOWERHEX64 create_commitment=LOWERHEX64 create_cap=LOWERHEX64 payload=LOWERHEX fd4_endpoint_inode=DEC rpc_inner_pid=DEC rpc_inner_uid=0 rpc_inner_gid=0
```

`template` is lowercase hex of the exact redacted template.  The grant
contains neither raw `create_cap`, the final capability-bearing frame, a
reversible encryption of either, nor any equivalent preimage.  A capability
digest which permits dictionary recovery from a smaller domain is forbidden;
the raw capability remains a uniformly drawn 256-bit value under the exact
v6 `getrandom=318`, fill, P-only retention, collision-with-all-live-and-
tombstoned-values, no-redraw, and no-early-surface rules.

P completely sends CREATE_GRANTED before completely sending the existing
FD-5 `SESSION_AUTH_RECEIPT`, which remains the sole first disclosure of raw
`create_cap` to the requester and whose `create=LOWERHEX` is hex of the exact
`create_frame`.  G cannot reconstruct a valid final create frame from its
grant.

### 3.3 Actual first receive, same-buffer return, and P join

After installing the grant, G enables exactly one FD-4 receive attempt for
the bound requester endpoint.  The first complete seqpacket datagram is
immutably captured before parsing and permanently consumes the attempt.  G
uses `recvmsg` under the retained `SO_PASSCRED` contract and requires exactly
one kernel-supplied credential, no rights or other cmsg, and neither
`MSG_TRUNC` nor `MSG_CTRUNC`.  The endpoint inode and credential tuple must
equal the D-M2-verified registered endpoint and `create_identity`.

G first requires the first four bytes of that same immutable receive buffer
to equal the exact length of all remaining bytes.  It then canonical-parses
that same immutable full `create_frame`, obtains raw `create_cap`, recomputes
`create_commitment`, and requires exact equality.  Only then may it construct
CREATE_ACCEPTED, whose `payload` is hex of that same immutable full-frame
first-receive buffer and whose raw `create_cap` is the value parsed from that
buffer.  It may not reconstruct, normalize, replace, or
reserialize either field.  The byte-bound G implementation must preserve a
single data-flow object from `recvmsg` return through the accepted record;
a copied grant, synthetic buffer, or later packet is not a source.

P receives CREATE_ACCEPTED and, before drawing or disclosing `reply_nonce`,
sending COMMIT, constructing private state, or advancing another success
edge, independently requires:

```text
returned raw create_cap = P's undisclosed-then-receipted raw secret
returned payload = P's stored exact create_frame
returned commitment = P's stored commitment
returned identity/endpoint/credentials = the immutable registered tuple
recomputed commitment over those exact bytes = returned commitment
state = exactly one unconsumed CREATE_GRANTED attempt
```

Expected values come from P's direct registration and secret ledger, never
from G's record.  This is the sole new information in G's success report:
before an actual requester-to-G disclosure, G lacks the raw preimage needed
to make the equality true.

A malformed, empty, truncated, wrong-capability, wrong-byte, wrong-endpoint,
wrong-credential, duplicate, replayed, cross-session, or prematurely queued
first datagram consumes the attempt and enters ABORTING.  There is no second
receive, reconstruction, retry, or later success for that auth/session.
Raw values and all commitment/transcript digests enter the retained terminal
tombstone.

The exact threat boundary remains the byte-bound, single-threaded trusted G
program already frozen by the possession design; G is not an unbounded
Byzantine party allowed to forge arbitrary records after learning a secret
from a rejected packet.  The amendment must state this boundary and the
same-buffer audit obligation explicitly.  If the intended theorem instead
requires Byzantine-G resistance, this commitment protocol is insufficient:
the amendment must stop with `D-M1` open because a P- or kernel-direct actual-
buffer observation would require authority not granted here.

## 4. Active-cap non-disclosure and exact evidence ceiling

Raw `active_cap` remains first disclosed only to the requester in the
complete FD-5 `SESSION_AUTH_ACTIVE_RECEIPT`.  Define `active_identity` as:

```text
requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER fd4_endpoint_inode=DEC
```

and define:

```text
active_cap_commitment =
  P15R_V7_BIND("P15R-ACTIVE-COMMITMENT-v7",
                active_identity,
                raw_active_cap_32_bytes)
```

The v6 ACTIVE pair is replaced only in these fields:

```text
P -> G:
SESSION_AUTH_ACTIVE requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC active_cap_commitment=LOWERHEX64 created_digest=LOWERHEX64

G -> P:
SESSION_AUTH_ACTIVE_ACK requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC request=DEC active_cap_commitment=LOWERHEX64 created_digest=LOWERHEX64
```

Neither record carries raw `active_cap`.  A complete ACK authorizes the
session and the already direct-audited `AUDITED_SPAWN` lane, but G learns raw
`active_cap` only from the first later capability-bearing non-child FD-4
packet.  For each of the eight unchanged v6 capability-bearing forms, G
recomputes the commitment over the parsed raw value and exact bound identity
before any mutation.  A wrong first active-cap use consumes that operation
attempt and aborts before mutation.

`active_cap` remains session-scoped.  After one valid capability-bearing
packet, G necessarily knows its raw value.  Therefore v7 must not claim that
this value independently proves requester authorship of every later packet.
The existing requester-direct `AUDITED_SPAWN` join remains the independent
child-request evidence; Section 5's fresh terminal direct observation is the
independent terminal-send evidence.  No later G-only operation report may be
promoted to independent requester provenance merely because it repeats
`active_cap`.  Per-operation provenance would require fresh per-request
one-use capabilities or a P-direct request witness and is outside this gate;
amendment v7 must stop rather than add such a protocol.

## 5. F-M1.b repair — P-observable terminal completion

### 5.1 Fourth capability kind

`terminal_cap` is the fourth and final D-M1 capability kind.  P draws it
only after accepting `SESSION_AUTH_TERMINAL_PREPARED`.  It uses the exact
v6 native x86_64 `getrandom(buffer,32,flags=0)` syscall 318, suffix/EINTR
fill, exact-32-byte, raw-collision, no-redraw, secret-retention, encoding,
and tombstone rules.  The collision set now contains every live and
tombstoned raw value of:

```text
PREFLIGHT_ONLY | create_cap | reply_nonce | active_cap | terminal_cap
```

Raw `terminal_cap` is P-only before the complete P-to-G terminal grant.  It
must not occur in an earlier requester field, G record, log, exception,
digest preimage exposed to the requester, environment, argv, pathname,
result, or serialized artifact.  The requester first learns it only by
receiving the actual terminal FD-4 reply.

### 5.2 Exact terminal reply and P--G sequence

The v2/v6 terminal reply payload is superseded only by appending one final
field:

```text
SESSION_CLOSED request=DEC session=DEC outcome=OUTCOME terminal_cap=LOWERHEX64
```

Let `terminal_payload` be those exact canonical ASCII bytes and let the sole
raw terminal FD-4 datagram be:

```text
terminal_frame = U32BE(len(terminal_payload)) || terminal_payload
```

The inherited four-byte prefix counts only `terminal_payload`; no trailing
byte, second datagram, or alternate frame is legal.

The v6 `SESSION_AUTH_SESSION_CLOSED` / `SESSION_AUTH_CLOSE_ACK` pair is
removed.  Its replacement is exactly:

```text
G -> P:
SESSION_AUTH_TERMINAL_PREPARED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME terminal_template=LOWERHEX

P -> G:
SESSION_AUTH_TERMINAL_GRANTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME terminal_cap=LOWERHEX64 reply_digest=LOWERHEX64 reply=LOWERHEX

P -> G:
SESSION_AUTH_FINALIZE requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME terminal_cap_sha256=LOWERHEX64 reply_digest=LOWERHEX64

G -> P:
SESSION_AUTH_FINALIZED_ACK requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME terminal_cap_sha256=LOWERHEX64 reply_digest=LOWERHEX64
```

`terminal_template` is hex of the exact terminal payload with its sole
capability value replaced by literal `{TERMINAL_CAP64}`, which is not legal
`LOWERHEX64`.  `reply` is hex of the exact final `terminal_frame`.
`reply_digest` is:

```text
SHA256(ASCII("P15R-TERMINAL-REPLY-v7") || ASCII(" ") || terminal_frame)
```

`terminal_cap_sha256` is:

```text
SHA256(ASCII("P15R-TERMINAL-CAP-v7") || ASCII(" ") || raw_terminal_cap_32_bytes)
```

G may send TERMINAL_PREPARED only after accepting the one legal ACTIVE
`SESSION_CLOSE`, closing admission, reaching `CLOSING`, reaping every child,
and completing every inherited root/lock/object/foreign-preservation and
terminal cleanup proof.  P independently validates that state and template,
draws `terminal_cap`, constructs the sole exact `terminal_frame`, and
completely sends TERMINAL_GRANTED.  This is the first disclosure of raw
`terminal_cap` to G.

G requires exact raw bytes/digests and performs exactly one FD-4 seqpacket
send of the decoded `terminal_frame`.  It records a success flag only if the
return equals the complete datagram length.  `terminal_frame` must be at most
4096 bytes and is one message on the inherited connected Linux
`SOCK_SEQPACKET` endpoint: a complete send enqueues exactly one whole
datagram, never a stream prefix.  Any positive short return, errno, or
ambiguous result leaves the full-send flag false.  G does not retry a suffix,
send a second terminal reply, or treat readiness/EOF as success.  A G-only
success flag or record is not P's evidence.

### 5.3 Complete FD-5 enum and direct terminal frames

The complete requester--P FD-5 enum becomes exactly twelve forms:

```text
requester -> P: SESSION_AUTH_OPEN
P -> requester: SESSION_AUTH_CHALLENGE
requester -> P: SESSION_AUTH_REGISTERED
P -> requester: SESSION_AUTH_RECEIPT
requester -> P: SESSION_AUTH_ACTIVATED
P -> requester: SESSION_AUTH_ACTIVE_RECEIPT
requester -> P: SESSION_AUTH_TERMINAL_OBSERVED
P -> requester: SESSION_AUTH_TERMINAL_RECEIPT
requester -> P: AUDIT_OPEN
P -> requester: AUDIT_CHALLENGE
requester -> P: AUDITED_SPAWN
P -> requester: AUDIT_RECEIPT
```

The first six and last four retain their v6/v4 exact byte grammar.  The two
new forms are exactly:

```text
requester -> P:
SESSION_AUTH_TERMINAL_OBSERVED audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME terminal_cap=LOWERHEX64 reply_digest=LOWERHEX64 reply=LOWERHEX

P -> requester:
SESSION_AUTH_TERMINAL_RECEIPT audit=DEC auth_serial=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME terminal_cap_sha256=LOWERHEX64 reply_digest=LOWERHEX64
```

Each is one canonical ASCII `SOCK_SEQPACKET` datagram no larger than 4096
bytes, with no NUL, LF, separate length, rights, explicit credential, other
cmsg, or trailing byte.  The requester uses plain `send` and P receives with
`recvmsg`, requiring the registered endpoint and exactly one kernel-supplied
`SCM_CREDENTIALS`, no other cmsg, and no `MSG_TRUNC`/`MSG_CTRUNC`.  P replies
with plain `send` and no ancillary item.  Complete send means the exact full
datagram length.

The requester may emit TERMINAL_OBSERVED exactly once only after one exact,
complete, nontruncated FD-4 seqpacket receive of `terminal_frame`, including
validation of its U32BE length and canonical `SESSION_CLOSED` payload.  It
sends the raw capability and hex of that same immutable receive buffer.  P requires
exact equality with its secret, exact expected reply bytes, both digests,
the close tuple, endpoint, credentials, and the one open terminal attempt.
The direct FD-5 endpoint remains child-unique and, by frozen D-M2 evidence,
G holds no endpoint or peer copy.  Therefore G's local send assertion cannot
satisfy this requester-direct observation.

A wrong, premature, malformed, duplicate, replayed, truncated, cross-session,
or cross-endpoint TERMINAL_OBSERVED consumes the attempt and fails.  A direct
observation alone cannot cure an anomalous wrong/partial terminal send: even
if such a defect exposed the raw capability and the requester synthesized
the expected bytes, G's full-send flag would be false and G is forbidden to
send FINALIZED_ACK.  Conversely, G's flag alone cannot replace the direct
observation.  P requires both joins, and there is no second terminal send or
observation attempt.  This combined rule uses the same byte-bound trusted-G,
non-Byzantine boundary frozen in Section 3.3.

Only after that direct join may P completely send SESSION_AUTH_FINALIZE.  G
requires its exact local full-terminal-send flag and tuple before completely
sending SESSION_AUTH_FINALIZED_ACK.  Only after P validates that ACK may P
completely send SESSION_AUTH_TERMINAL_RECEIPT.  The requester closes FD 5
only after receiving the complete receipt.  P accepts clean EOF only with no
open audit/auth/terminal frame and retains the existing peer-identity and
requester-reap order before closing its peer.

There is no thirteenth FD-5 form.  The design proves P's complete receipt
send plus later peer closure; it does not claim that P independently observes
the requester's application-level read of TERMINAL_RECEIPT.  If such a read
is made a success predicate, amendment v7 must stop because an acknowledgment
would be a forbidden thirteenth form.

### 5.4 Complete D-M1 P--G enum

The D-M1 P--G session enum is exactly twelve forms:

```text
P -> G: SESSION_AUTH_CREATE_GRANTED
G -> P: SESSION_AUTH_CREATE_ACCEPTED
P -> G: SESSION_AUTH_COMMIT
G -> P: SESSION_AUTH_COMMITTED
P -> G: SESSION_AUTH_ACTIVE
G -> P: SESSION_AUTH_ACTIVE_ACK
P -> G: SESSION_AUTH_ABORT
G -> P: SESSION_AUTH_ABORTED
G -> P: SESSION_AUTH_TERMINAL_PREPARED
P -> G: SESSION_AUTH_TERMINAL_GRANTED
P -> G: SESSION_AUTH_FINALIZE
G -> P: SESSION_AUTH_FINALIZED_ACK
```

There is no thirteenth D-M1 session form.  The four separate D-M2
`FD_AUDIT_QUIESCE_ENTER/ACK/EXIT/EXIT_ACK` forms remain byte-exact and are
not counted as D-M1 session forms.  Every D-M1 P--G form uses the inherited
four-byte big-endian length prefix, 4096-byte ceiling, canonical ASCII,
exact direction and field order, no ancillary item, and complete-send rule.

## 6. Exact states, failures, and terminal ownership

Amendment v7 must replace only the affected D-M1 states with these complete
successful paths:

```text
P:
UNSEEN -> CHALLENGE_ISSUED -> REGISTERED -> CREATE_GRANTED
-> CREATE_ACCEPTED -> INACTIVE_COMMITTED -> ACTIVATION_JOINED
-> ACTIVE_RECEIPT_SENT -> ACTIVE_PENDING -> ACTIVE_AUTHORIZED
-> CLOSING -> TERMINAL_PREPARED -> TERMINAL_GRANTED
-> TERMINAL_OBSERVED -> FINALIZE_SENT -> FINALIZED_ACKED
-> TERMINAL_RECEIPT_SENT -> FD5_EOF_OBSERVED -> CLOSED_TOMBSTONE

G:
NO_SESSION -> CREATE_ARMED -> CREATE_HELD -> INACTIVE
-> ACTIVE_ARMED -> ACTIVE_AUTHORIZED -> CLOSING
-> TERMINAL_PREPARED -> TERMINAL_GRANTED -> TERMINAL_REPLY_SENT
-> FINALIZE_RECEIVED -> CLOSED_TOMBSTONE

any nonterminal state -> ABORTING -> FAILED_TOMBSTONE
```

G's ACTIVE_ACK authorizes the direct-audited child-request lane and arms the
active commitment.  Its first correct active-cap-bearing non-child packet
supplies raw equality before that packet's mutation; this does not create an
additional P-visible state or a per-operation provenance claim.

At minimum the total failure table must freeze these rows:

| First failing edge | Required result before any later operation |
|---|---|
| create/active/terminal entropy fill or raw collision | retain exact partial/colliding P-only receipt; no redraw, disclosure, or success; abort/contain according to whether G has state |
| CREATE_GRANTED incomplete | disclose no raw create cap; no requester receipt; tombstone locally; no retry |
| grant succeeds but requester receipt fails | P aborts; G discards arm/held frame; raw cap remains unknown to G; no commit |
| requester is live but sends no create | no progress and no invented timeout success |
| first create datagram is wrong in any coordinate | consume attempt; no second receive; no construction; abort and tombstone |
| CREATE_ACCEPTED incomplete or P comparison fails | no COMMIT, reply nonce, or private construction; abort/contain |
| COMMIT through ACTIVATION join fails | retain the exact v6 no-retry INACTIVE cleanup; no active cap |
| ACTIVE_RECEIPT incomplete | raw active cap is not operational; send no ACTIVE; abort |
| ACTIVE or ACTIVE_ACK incomplete | G remains nonmutating for non-child operations; abort and clean |
| first active-cap-bearing packet is wrong | no requested mutation; consume attempt; abort |
| SESSION_CLOSE or inherited cleanup fails | no TERMINAL_PREPARED; retained containment/foreign-preservation; failed tombstone |
| TERMINAL_PREPARED incomplete | P draws/discloses no terminal cap; failed tombstone |
| terminal-cap fill/collision | send no TERMINAL_GRANTED; failed tombstone and retained cleanup state |
| TERMINAL_GRANTED incomplete/invalid | G sends no terminal reply; failed tombstone; no retry |
| terminal FD-4 send is incomplete or errors | G never sets full-send flag; P receives no valid direct observation; abort/contain; no second reply |
| requester remains live but sends no TERMINAL_OBSERVED | no progress and no invented success or timeout |
| TERMINAL_OBSERVED wrong, duplicate, malformed, or premature | consume terminal attempt; send no FINALIZE; failed tombstone |
| requester FD-5 EOF before terminal receipt | failed tombstone; never clean close |
| FINALIZE incomplete/invalid | no FINALIZED_ACK success; failed tombstone |
| FINALIZED_ACK incomplete/invalid | P never sends terminal receipt; failed tombstone |
| TERMINAL_RECEIPT incomplete | P does not enter success tombstone; requester endpoint is contained; G's completed cleanup is not relabelled P-observed success |
| clean FD-5 EOF absent after complete receipt | P does not enter CLOSED_TOMBSTONE; no EOF synthesis |
| P--G control EOF or crash before final ACK | retained whole-control freeze/kill/reap containment; no terminal success or ABSENT |

Every send is attempted once and succeeds only at the complete byte count;
there is no suffix retry.  Every raw value, commitment, digest, endpoint,
request, and terminal cause persists in the live/terminal ledger through
complete teardown.  Neither clean EOF nor G-only send success substitutes
for a required direct record.  Cleanup may already be physically complete
on a terminal-protocol failure, but the auth outcome remains failed and
foreign preservation/no-false-`ABSENT` rules remain exact.

## 7. D-M2 and all prior closures: no regression

Amendment v7 must preserve without weakening:

1. `D-M2`: native x86_64 syscalls 434/438 with flags zero and actual runtime
   permission; four exact slot/kind rows; pidfd/proc identities and
   lifetimes; G quiesce; both snapshots; every actual duplicate/fstat/proc/
   reciprocal-diag comparison; common reverse unwind; immediate EBADF;
   restored holders; and both ABA exclusions.  Its only textual adjustment
   is the new FD-5 terminal close edge.
2. `C-M1/C-M2`: child-unique P-created FD 5, requester-direct child request,
   actual FD-4 byte join, audited child registration/admission, and exact
   Unix-diag ABI with no fallback.
3. `B-M1..B-M3`: six pre-suite rows, exact owner/admission grammar and 173-
   method boundary; phase-indexed descriptor sets and barriers; and
   pre-access/post-creator object ledger ordering.
4. `A-M1`: unparameterized `SG_SCOPE`, primitive-only evidence-class
   projection, expected class only after recomputation, and every primitive
   prefix/witness counterfactual.
5. `A-M2`: recursive real-filesystem receipts, all live variants, and the
   exact-one-coordinate mode/mtime comparator probes cloned from actual
   receipts without ctime masking.
6. `A-M3`: private possession, namespace/cgroup containment, retained
   parent/root/lock capabilities, capability-relative cleanup, both
   replacement phases, every replacement fixture, foreign preservation,
   and no false `ABSENT`.
7. `A-M4`: manifest-first complete-review authentication, canonical unique
   ordered effective-amendment blocks, independent capability-relative
   reads/hashes, and dereference before lifecycle adjacency.
8. blocked v5's no-op provenance and every v6 closure not expressly
   superseded above.

A v7 clause which weakens any item creates a new open finding.  It cannot
trade a prior closure for D-M1 or declare a conditional PASS.

## 8. Frozen counts, schemas, paths, and DAG

The following remain exact:

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

All six implementation paths, eight CSV paths and literal headers, 120 rows
and order, 35 explicit negatives, 35 semantic methods, 28 package methods,
173 method names, nine generated paths, fourteen authority paths, manifest
keys/schema, and graph `A,D,R,G,I,C,M,V` with twelve distinct edges remain
unchanged.  Commitments, capabilities, frames, ledgers, and terminal receipts
are operational, in-memory, and nonserialized.

## 9. Append-only count-seven successor

After amendment v7 is frozen and externally hashed, the fresh independent
reviewer must preserve all five existing blocks and append exactly one sole
active successor, with no blank or commentary line inside it:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v6]
count=7
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
7.sha256=<exact externally computed final v7 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

The final verifier must authenticate the complete post-v7 review through the
manifest-bound review FD before parsing, require exactly one byte-identical
historical block for each version `v1` through `v5`, exactly one active `v6`
block above, and no other begin/end tag.  It rejects missing, duplicate,
reordered, nested, malformed, prefix-drifted, wrong-version/count/index/path/
digest, extra-key, blank, or commentary-bearing blocks.

It then independently capability-opens amendments v1 through v7 in active
order beneath the same held package-root FD with the retained beneath/no-link
rules, reads every byte, and recomputes all seven hashes.  Only after every
match may it set
`R.effective_amendments=[v1,v2,v3,v4,v5,v6,v7]` before lifecycle adjacency.
This changes no manifest key, authority binding, artifact, graph node, edge,
self-hash, future-result edge, or proof cycle.

## 10. Sole later independent re-review

Only after amendment v7 is frozen and externally hashed may one fresh
independent reviewer append to:

```text
notes/phase2_control_design_peer_review.md
```

The current 165,177-byte / 3,149-line file at SHA-256
`075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c`
must remain its exact prefix.  The reviewer must independently read and hash
the complete base + v1--v7 tuple and attack, rather than restate:

1. absence of raw/equivalent create-capability disclosure to G before the
   actual packet, exact commitment/template framing, first-attempt
   consumption, immutable receive-buffer provenance, endpoint credentials,
   wrong-first/replay/abort, and P's pre-COMMIT raw-byte join;
2. the explicit trusted-G/non-Byzantine boundary and whether any permitted
   alternate surface lets G learn the preimage without an actual FD-4
   datagram;
3. active commitment non-disclosure and the exact prohibition on promoting a
   session-scoped known-after-first-use cap to per-operation provenance;
4. terminal-cap entropy/collision/disclosure, exact reply packet, FD-4
   complete-send versus failure, requester-direct FD-5 observation,
   FINALIZE/ACK, terminal receipt, EOF, crash, and every failure row;
5. the exact twelve FD-5 and twelve D-M1 P--G forms with no hidden thirteenth
   form or post-receipt read claim;
6. complete regression of D-M2 and every earlier closure; and
7. five immutable historical blocks, one active count-seven block, seven
   independent amendment reads/hashes, fourteen bindings, and the unchanged
   eight-node/twelve-edge DAG.

The reviewer may close `D-M1` only from its own evidence.  This gate does not
predict that result.  Only a later independent `PASS C0/M0/m0` could support
consideration of a separate implementation gate.

## 11. Authorization matrix

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V7=PASS_TO_ONE_AMENDMENT_V7
CURRENT_OPEN_FINDINGS=C0_M1_m0
D_M1_STATUS=OPEN
D_M2_STATUS=CLOSED_FROZEN_NO_REGRESSION
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v7.md
AMENDMENT_V7_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V7_FROZEN_AND_EXTERNALLY_HASHED=true
CURRENT_REVIEW_PREFIX_SHA256=075749b3dc36aa1a58c65f7bb861c14071d5a6e66c23c8263c12086bc468e47c
CURRENT_REVIEW_PREFIX_LINES=3149
CURRENT_REVIEW_PREFIX_BYTES=165177

D_M1_CREATE_G_PREPACKET_RAW_DISCLOSURE=false
D_M1_CREATE_COMMITMENT_DOMAIN=P15R-CREATE-COMMITMENT-v7
D_M1_CREATE_ACCEPTED_RETURNS_RAW_CAP_AND_EXACT_FIRST_BUFFER=true
D_M1_P_COMPARE_BEFORE_COMMIT_AND_FUTURE_SECRET=true
D_M1_WRONG_FIRST_RETRY_AUTHORIZED=false
D_M1_ACTIVE_G_PREOP_RAW_DISCLOSURE=false
D_M1_ACTIVE_PER_OPERATION_PROVENANCE_CLAIMED=false
D_M1_TERMINAL_CAP_KIND=FOURTH
D_M1_TERMINAL_DIRECT_FD5_OBSERVATION_REQUIRED=true
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M1_THIRTEENTH_FORM_AUTHORIZED=false
D_M1_G_ONLY_TERMINAL_SEND_IS_INDEPENDENT_EVIDENCE=false
D_M1_FINDING_CLOSED_BY_THIS_GATE=false

D_M2_CLOSURE_RETAINED=true
D_M2_SYSCALLS_434_438_RETAINED=true
D_M2_QUIESCE_SNAPSHOT_UNWIND_EBADF_RETAINED=true
D_M2_ONLY_FD5_TERMINAL_CLOSE_EDGE_REDIRECTED=true

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

This gate does not embed its own SHA-256.  Amendment v7 and the sole later
fresh independent append-only re-review must bind this file's externally
computed final digest.  `D-M1` remains open, `D-M2` remains closed, and no
implementation or execution is authorized by these design-only bytes.
