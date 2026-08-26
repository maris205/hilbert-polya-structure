# Replacement Paper 15 Phase-2 control-design remediation gate v4

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v4 — C0/M2/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v4.0`  
Date: 2026-08-17 (Asia/Shanghai)

This is a design-remediation authorization, not a finding closure.  The two
major findings in the current final append-only review, `C-M1` and `C-M2`,
remain open.  This gate authorizes exactly one design-only amendment and,
only after that amendment is frozen and externally hashed, one fresh
independent append-only re-review.  It authorizes no generator, verifier,
test, wrapper, implementation, control execution, reproduction run, Route,
composition, manuscript, figure, release, archive, Git action, or public
synchronization.

## 1. Exact authority and current verdict

The following eight records were read on their complete current bytes and
independently re-hashed before this gate was written:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| design amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| remediation gate v2 | `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` |
| design amendment v2 | `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| remediation gate v3 | `notes/phase2_control_design_remediation_gate_v3.md` | 578 | 27299 | `e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac` |
| design amendment v3 | `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| current final append-only review | `notes/phase2_control_design_peer_review.md` | 1910 | 96524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |

The review's first 74,876 bytes independently hash to
`ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725`;
its first 49,358 bytes independently hash to
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`;
and its first 22,894 bytes independently hash to
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.
The complete current effective verdict is **REVISE — C0/M2/m0**.  No
amendment self-audit is evidence against it.

The current review contains exactly two effective-amendment blocks.  The
historical block remains exactly:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v1]
count=2
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

The current active block remains exactly:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v2]
count=3
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

Both blocks and all 96,524 current review bytes are immutable historical
prefix authority for the later append-only re-review.

The proof/source boundary is not reopened.  The theorem owner remains the
bare compact group `B_p`; universal recovery remains
`OPEN_NOT_AUTHORIZED`; Route B remains false.

## 2. Sole amendment target, precedence, and bounded supersession

The target was absent before this gate was created.  Exactly one new design
file may be created:

```text
notes/phase2_control_design_amendment_v4.md
```

After that file is frozen and externally hashed, the effective design is
exactly

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + amendment v2 c1d104d2...
  + amendment v3 f6a0af9c...
  + amendment v4 at its externally computed final digest.
```

Amendment v4 may supersede only the clauses needed to close `C-M1` and
`C-M2`, plus the mechanical successor-receipt grammar in Section 7.  It must
explicitly enumerate every changed descriptor slot, `FDSET`, RPC payload,
P--G record, ancillary-bearing record, child-registration variant, state
edge, holder, close event, and verifier rule.  Every omitted base/v1/v2/v3
clause remains binding.  It must not embed its own digest, claim independent
closure, or authorize implementation or execution.

## 3. C-M1 repair — P-direct requester witness and two-channel acceptance

### 3.1 Exact requester and descriptor scope

The repair applies to every child-creating RPC `SPAWN` accepted after suite
entry.  The only RPC-capable requester targets remain exactly:

```text
TOP_TEST_CONTROLS
COPIED_REPRODUCE
```

Each such requester receives one child-unique audit endpoint at exact child
FD 5.  FD 5 is named `REQUEST_AUDIT`; it is one endpoint of a P-created
`AF_UNIX SOCK_SEQPACKET|SOCK_CLOEXEC` socketpair.  P retains the sole peer and
sets `SO_PASSCRED=1` on that retained endpoint before the child endpoint
leaves P.  G never receives P's retained peer.  No generator, probe, holder,
contender, replacement actor, or non-RPC child receives FD 5.

The v3 `STDIO_SOURCE_RPC_BARRIER` token is replaced by exactly
`STDIO_SOURCE_RPC_AUDIT_BARRIER`; the closed enum still has four values:

```text
STDIO_BARRIER
STDIO_SOURCE_BARRIER
STDIO_SOURCE_ROOT_BARRIER
STDIO_SOURCE_RPC_AUDIT_BARRIER
```

The complete phase matrix remains the following, with only the printed FD 5
addition and token replacement in the fourth row:

| Exact `FDSET` | Exact targets | Registered / pre-admission | `SOURCE_READY` | Target running |
|---|---|---|---|---|
| `STDIO_BARRIER` | `CGROUP_PROBE_CHILD epoch=1`, `CGROUP_PROBE_CHILD epoch=2`, `LOCK_HOLDER`, `LOCK_CONTENDER`, `REPLACEMENT_ACTOR` | `{0,1,2,8}` | `{0,1,2,8}` | `{0,1,2}` |
| `STDIO_SOURCE_BARRIER` | `VERIFY_ONLY_GENERATOR` | `{0,1,2,3,8}` | `{0,1,2,8}` | `{0,1,2}` |
| `STDIO_SOURCE_ROOT_BARRIER` | `GENERATE_CANONICAL_A`, `GENERATE_CANONICAL_B`, `GENERATE_MUTATION` | `{0,1,2,3,8,9}` | `{0,1,2,8,9}` | `{0,1,2,9}` |
| `STDIO_SOURCE_RPC_AUDIT_BARRIER` | `TOP_TEST_CONTROLS`, `COPIED_REPRODUCE` | `{0,1,2,3,4,5,8}` | `{0,1,2,4,5,8}` | `{0,1,2,4,5}` |

There is no optional audit FD, alternate slot, wildcard requester, inherited
shared endpoint, pathname socket, or listener fallback.

### 3.2 Exact pair allocation and ownership transfer

The v4 amendment must add exactly these allocation records to the existing
four-byte-big-endian, 4096-byte P--G control protocol:

```text
AUDIT_FD_REQUEST session=DEC child=DEC target=TARGET role=ROLE owner=OWNER purpose=PURPOSE
AUDIT_FD_GRANTED session=DEC child=DEC audit=DEC
```

`AUDIT_FD_REQUEST` is G-to-P exactly once for an exact requester target,
after the child identifier is reserved and before clone3.  For a
`COPIED_REPRODUCE` child it is legal only after the parent request reaches
`AUDITED_RPC_CONFIRMED`; for the fixed top runner it is legal only in its
existing session-zero row.  P rejects every other target/role/owner/purpose
combination.

P creates a fresh pair, assigns a globally monotone canonical `AUDIT_DEC`
never reused in the control lifetime, retains one endpoint, and sends the
other in `AUDIT_FD_GRANTED`.  That P-to-G record carries exactly one
untruncated `SCM_RIGHTS` item containing exactly one endpoint and no other
ancillary item.  G receives with `recvmsg(MSG_CMSG_CLOEXEC)`, requires
`FD_CLOEXEC`, installs that endpoint at child FD 5, and closes every transit
copy before the child sends `SANITIZED`.  P's pre-admission audit must prove
the child holds exactly the granted endpoint at FD 5 and G holds no copy.

This explicitly supersedes the v2/v3 statement that `WORKERS_CGROUP_FD` is
the sole ancillary-bearing P--G record.  The complete allowed set becomes
exactly `WORKERS_CGROUP_FD` and `AUDIT_FD_GRANTED`; their states and payloads
are disjoint.  No audit endpoint can be delivered in an RPC, reused for a
second child, retained by G after sanitization, or substituted for FD 4 or
FD 8.

### 3.3 Exact requester--P frames and canonical audited RPC

On FD 5 the complete payload enum is exactly:

```text
requester -> P: AUDIT_OPEN audit=DEC serial=DEC
P -> requester: AUDIT_CHALLENGE audit=DEC serial=DEC nonce=LOWERHEX64
requester -> P: AUDITED_SPAWN audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64 trigger=TRIGGER core=LOWERHEX
P -> requester: AUDIT_RECEIPT audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64
```

Each item is one complete seqpacket containing exactly the shown canonical
ASCII payload, at most 4096 bytes, with no NUL, LF, separate length prefix,
rights, explicit credentials, or trailing byte.  `DEC` is canonical
nonnegative decimal.  `serial` starts at zero per audit endpoint and rises
by exactly one for each child-creating request; at most one serial is open.
The decoded `core` is nonempty and at most 512 bytes, and the complete
`AUDITED_SPAWN` payload is at most 1280 bytes; therefore its later lowercase-
hex transcript plus fixed fields remains below the unchanged 4096-byte P--G
ceiling.  Exceeding either bound is malformed, not a framing extension.

The requester uses plain `send` for both requester-to-P packets.  P uses
`recvmsg` and requires exactly one kernel-supplied `SCM_CREDENTIALS`, no
other cmsg, and no truncation.  In P's initial namespaces that credential
must be the requester's registered outer PID and outer uid/gid 65534/65534;
P's retained uid/gid maps and stable `NSpid` chain must independently
normalize it to the same registered inner PID and inner uid/gid 0/0 that G
observes.  A zero, invisible, or differently translated credential is not a
match.  `sendmsg` and `sendmmsg` remain denied to the requester.  P's two
replies contain no ancillary item.

For each accepted `AUDIT_OPEN`, P issues the unique one-use nonce

```text
lowerhex(sha256(
  "P15R-AUDIT-NONCE-v1 audit=<AUDIT_DEC> requester_session=<SESSION_DEC> requester_child=<CHILD_DEC> serial=<SERIAL_DEC>"
))
```

where the quoted ASCII bytes contain the canonical decimal substitutions
and no NUL or LF.  Uniqueness comes from P's never-reused audit handle and
strict serial state; a nonce is consumed by either one receipt or one
failure and is never reissued.

`core` decodes to exactly one unchanged v2 canonical payload, without its
four-byte length prefix:

```text
SPAWN request=DEC session=DEC target=TARGET method=METHOD purpose=PURPOSE handle=DEC
```

`digest` is lowercase SHA-256 of those decoded `core` bytes.  P independently
decodes and hashes `core`, parses the exact request id, session, target,
method, purpose, and handle, takes `trigger` from the same requester-authored
outer payload, and checks all of them against the requester's independently
registered endpoint role/owner and the existing closed method/session/
purpose/trigger authorization.  Expected values are never parsed from G's
later report.  Only that complete validation permits `AUDIT_RECEIPT` and an
immutable P pending-request record.

After receipt, the requester sends on FD 4, under the existing four-byte
length framing, the **same `AUDITED_SPAWN ...` payload bytes** it sent to P.
A bare child-creating `SPAWN`, a changed outer byte, or a second payload for
the same nonce is illegal.  Thus the actual G RPC carries the same P-issued
nonce and digest while preserving the exact inner v2 `SPAWN` semantics.

### 3.4 Exact G acceptance join and future admission

G receives the FD-4 frame with its existing `SO_PASSCRED`/`recvmsg`
credential check, validates the outer grammar, independently decodes and
hashes `core`, and holds the request without cloning or other target action.
It then sends exactly one:

```text
AUDITED_RPC_ACCEPTED requester_session=DEC requester_child=DEC audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64 rpc_inner_pid=DEC rpc_inner_uid=0 rpc_inner_gid=0 payload=LOWERHEX
```

The record is G-to-P.  `payload` is lowercase hex of the complete accepted
`AUDITED_SPAWN ...` payload bytes, not a reserialization.  P decodes it and
requires byte-for-byte equality with its requester-direct pending record,
plus equality of nonce, digest, audit, serial, endpoint child, session, and
the credential tuple after the exact outer-to-inner normalization above.
Only then does P send exactly one:

```text
AUDITED_RPC_CONFIRMED requester_session=DEC requester_child=DEC audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64
```

Only `AUDITED_RPC_CONFIRMED` makes the held G request accepted and permits G
to clone the requested child.  G's report is not the independent fact; it is
the value compared against P's separately kernel-authenticated requester
observation.

The existing v3 `CHILD_REGISTERED` payload remains exact for the six fixed
session-zero children and every non-audited child.  It is forbidden for a
child produced by `AUDITED_SPAWN`.  For every such produced child, v4 adds
exactly this distinct G-to-P record and no optional registration fields:

```text
CHILD_REGISTERED_AUDITED session=DEC child=DEC inner_pid=DEC role=ROLE owner=OWNER purpose=PURPOSE admission=ADMISSION fdset=FDSET cwd_dev=DEC cwd_ino=DEC target=TARGET trigger=TRIGGER request=DEC requester_child=DEC audit=DEC serial=DEC nonce=LOWERHEX64 digest=LOWERHEX64
```

It occurs exactly once in the same state where v3 would have emitted
`CHILD_REGISTERED`, and is added to the closed P--G enum.  P joins its fields
to the sole consumed confirmed request and to its independent
pidfd, `/proc`, cgroup, credential, and descriptor observations.  P then
derives, without reading expected fields back from G,

```text
METHOD_V1:<METHOD>:S<SESSION_DEC>:R<REQUEST_DEC>:C<CHILD_DEC>
```

and compares those bytes with G's `admission` before `CHILD_ADMITTED`.
Exactly one confirmed request may authorize exactly one registered child;
the audit tuple is carried into no other admission and cannot authorize a
retry after a failed clone.

### 3.5 Lifetime, close, and fail-closed behavior

P retains its audit peer from pair creation through requester reap.  The
requester holds FD 5 through all its child-creating RPCs, closes it after its
terminal endpoint reply and before exit, and never transfers or duplicates
it.  P accepts EOF only with no open challenge, pending request, or
unconsumed confirmation, then retains the closed-end identity until reap and
closes its peer.  G's transit endpoint is absent throughout requester target
execution.

A missing, duplicate, reused, reordered, cross-child, cross-session,
wrong-direction, wrong-credential, truncated, oversized, malformed,
digest-mismatched, nonce-mismatched, payload-mismatched, prematurely closed,
or post-terminal frame prevents confirmation and child action.  Before
target action this is `E_POSSESSION_UNAVAILABLE`; after an already confirmed
child exists, the existing containment, kill, reap, and cleanup rules apply.
No new public detector or exit class is added.

The amendment and fresh review must include at least these hostile pairs:
same G report with two requester-direct request ids; same method metadata
with changed primitive target or trigger; direct payload A but actual FD-4
payload B; nonce replay; audit endpoints exchanged between two requesters;
and a fabricated G accepted report with no requester packet.  Every pair
must be distinguishable by P before child action.

## 4. C-M2 repair — exact Linux Unix-diag reciprocal peer oracle

### 4.1 Sole primitive and availability preflight

The sole peer-correlation primitive is the Linux UAPI
`NETLINK_SOCK_DIAG` / `SOCK_DIAG_BY_FAMILY` exact-inode query with
`unix_diag_req.udiag_show=UDIAG_SHOW_PEER`.  P owns one
`socket(AF_NETLINK, SOCK_RAW|SOCK_CLOEXEC, NETLINK_SOCK_DIAG)` in the same
network namespace as all relevant anonymous Unix pairs.  The existing design
creates no new network namespace.  P binds
`sockaddr_nl{AF_NETLINK,0,0,0}`, reads its assigned nonzero `P_PORTID` with
`getsockname`, and sends only to kernel `sockaddr_nl` pid/groups zero.

Before any package, result, lock, or generation-root write, P must create two
disposable connected `AF_UNIX SOCK_SEQPACKET|SOCK_CLOEXEC` pairs, perform all
queries and reciprocal checks below, require each true pair to pass, require
both crossed expected mappings to fail, close/requery as required by the
preflight, and remove every disposable descriptor.  An unavailable module,
permission, namespace, UAPI, inode, attribute, or unique mapping is
`E_POSSESSION_UNAVAILABLE` before start.  There is no fallback.

### 4.2 Exact request and response ABI

The supported ABI remains the base design's sole x86_64 little-endian Linux
ABI.  For each nonzero endpoint inode `I <= 0xffffffff`, P uses a fresh
strictly increasing nonzero 32-bit `SEQ` and sends exactly 40 bytes:

```text
struct nlmsghdr
  nlmsg_len   = 40
  nlmsg_type  = SOCK_DIAG_BY_FAMILY = 20
  nlmsg_flags = NLM_F_REQUEST = 1
  nlmsg_seq   = SEQ
  nlmsg_pid   = P_PORTID
struct unix_diag_req
  sdiag_family  = AF_UNIX = 1
  sdiag_protocol= 0
  pad           = 0
  udiag_states  = 0xffffffff
  udiag_ino     = I
  udiag_show    = UDIAG_SHOW_PEER = 4
  udiag_cookie  = {0xffffffff,0xffffffff}
```

All multibyte fields are little-endian at their UAPI offsets.  No
`NLM_F_DUMP`, `NLM_F_ACK`, `NLM_F_MULTI`, request attribute, or trailing byte
is legal.  One request is outstanding at a time.

The only successful reply is one 48-byte datagram from a `recvmsg` source
`sockaddr_nl` with kernel pid/groups zero and no truncation.  It contains
exactly one `nlmsghdr`, one `unix_diag_msg`, and the following two aligned
attributes in this order:

```text
nlmsghdr:
  nlmsg_len=48, nlmsg_type=20, nlmsg_flags=0,
  nlmsg_seq=SEQ, nlmsg_pid=P_PORTID
unix_diag_msg:
  udiag_family=AF_UNIX=1
  udiag_type=SOCK_SEQPACKET=5
  udiag_state=TCP_ESTABLISHED=1
  pad=0
  udiag_ino=I
  udiag_cookie[2]=kernel-returned opaque receipt only
nlattr 1:
  nla_len=8, nla_type=UNIX_DIAG_PEER=2,
  payload=one little-endian u32 peer inode J
nlattr 2:
  nla_len=5, nla_type=UNIX_DIAG_SHUTDOWN=6,
  payload=one u8 value 0, followed only by alignment padding
```

The alignment padding carries no authority.  A zero or out-of-range inode,
missing or duplicate peer, extra or reordered attribute, wrong family/type/
state/shutdown, sequence or port mismatch, multipart reply, trailing message
or byte, `NLMSG_ERROR`, `NLMSG_DONE`, `NLMSG_OVERRUN`, timeout, truncation,
EOF, or unknown ABI is failure.  Cookie bytes are retained with the query
receipt but never substitute for the reciprocal peer relation.

### 4.3 Independent inode sources and reciprocal ownership matrix

For a child endpoint, P independently reads the exact
`/proc/<child-PID>/fd/<slot>` symlink, requires canonical
`socket:[INODE_DEC]`, and requires its no-follow `fstat` socket inode to equal
the same value.  For a G-held endpoint, P performs the corresponding
enumeration beneath its authenticated G pidfd/start-time proc identity and
requires exactly one live G descriptor with that inode and the registered
holder state.  For P's audit peer, P uses its own retained FD and `fstat`.
G-reported inode numbers, FD numbers, or endpoint maps are never the sole
inode source.

At every applicable pre-admission and `SOURCE_READY` audit, and at every
later audit while the pair remains live, P requires both exact queries

```text
diag(endpoint_inode) = expected_peer_inode
diag(expected_peer_inode) = endpoint_inode
```

and one-to-one ownership under this closed matrix:

| Child slot | Child targets | Required peer holder | Required live phases |
|---:|---|---|---|
| 8, `ADMISSION_BARRIER` | every G child | G, exactly one barrier-peer FD | registered and `SOURCE_READY`; both endpoints close at existing `START` transition |
| 4, `RPC` | `TOP_TEST_CONTROLS`, `COPIED_REPRODUCE` | G, exactly one RPC-peer FD | registered, `SOURCE_READY`, and target running through terminal reply |
| 5, `REQUEST_AUDIT` | `TOP_TEST_CONTROLS`, `COPIED_REPRODUCE` | P, exactly one retained audit-peer FD | registered, `SOURCE_READY`, and target running through terminal audit close/reap |

No endpoint may appear in two rows, map to itself, have two live holder FDs,
or have a reciprocal peer outside the expected holder.  The FD-5 P peer is
not a G endpoint.  The G transit copy of FD 5 must already be absent before
the first matrix check.

### 4.4 No substitute oracle

`SO_PEERCRED`, `SCM_CREDENTIALS`, equal uid/pid, local FD numbers, copied
inode text, packet delivery, G's table, or fixed barrier bytes do not prove
which of two anonymous endpoints are peers.  None is an allowed fallback or
tie-breaker.  The fresh review must create at least two simultaneous pairs,
hold all local number/type/CLOEXEC/credential facts fixed, cross-associate
the expected G endpoints, and require reciprocal Unix-diag comparison to
reject both crossed rows before `START`.

If exact querying is unsupported or does not yield a unique reciprocal
mapping on the actual platform, the design stops at
`E_POSSESSION_UNAVAILABLE`.  Amendment v4 may not replace this with an
opaque helper, external authority, best-effort `/proc/net/unix` scan, or
trust in G.

## 5. Required preservation of prior closures

Amendment v4 must retain, without weakening:

1. v3 `B-M1`: the exact operational owners, six session-zero rows, closed
   post-suite method owner grammar, and no widening of 173 methods;
2. v3 `B-M3`: actual-object pre-access acknowledgment, exact generator
   basename/purpose authorization without a future inode, reap/enumerate/
   register/ledger barriers, P25 count-zero behavior, and unexpected-object
   nondeletion;
3. `A-M1`: unparameterized `SG_SCOPE`, primitive-only class derivation,
   expected class only after recomputation, and all four primitive
   counterfactuals;
4. `A-M2`: real-filesystem receipt variants and actual-receipt exact-one-
   coordinate mode/mtime comparator clones;
5. `A-M3`: private possession, atomic cgroup placement, freeze/kill/reap,
   retained parent/root/lock capabilities, capability-relative deletion,
   five controlled replacements, foreign preservation, and no false
   `ABSENT`; and
6. `A-M4`: manifest-first complete-review authentication followed by
   independent capability-relative reads and hashes of every active
   amendment before lifecycle adjacency.

The exact v3 descriptor/barrier/source/close matrix remains binding except
for the explicit FD 5 and reciprocal-peer additions above.  A v4 repair that
regresses any retained closure creates a new open finding; it does not trade
one finding for another.

## 6. Frozen invariants

Amendment v4 and its re-review must preserve exactly:

```text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
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

The six implementation paths, eight CSV paths and headers, all 120 rows and
their order, all 35 semantic-negative rows, all 35 `S` methods, all 28 `P`
methods, all 173 method names, all nine generated paths, all fourteen
authority paths, manifest key set/schema, and printed graph
`A,D,R,G,I,C,M,V` with twelve edges remain unchanged.  All v4 audit, nonce,
descriptor, Unix-diag, and receipt records are operational and
nonserialized.

If either repair requires a schema, generated byte, public detector/exit
class, method, path, binding, node, edge, theorem owner, Route, or
publication-boundary change, amendment v4 must stop and report a new design
finding rather than silently widen scope.

## 7. Append-only v4 successor receipt while preserving A-M4

The current historical `v1` count-two block and current `v2` count-three
block in Section 1 cannot be edited, normalized, reordered, or duplicated.
After amendment v4 is externally hashed, the fresh independent reviewer must
append exactly one active successor block:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v3]
count=4
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=<exact externally computed final v4 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

There is no blank or commentary line inside any block.  Amendment v4 must
version the internal review-node grammar so the final verifier first
authenticates the complete post-v4 review through the existing manifest-
bound review path, parses those same bytes, requires exactly one historical
`v1` block equal to Section 1, exactly one historical `v2` block equal to
Section 1, exactly one active `v3` block in the form above, and no other
effective-amendment begin/end tag.

The verifier must reject missing, duplicate, reordered, malformed, nested,
prefix-drifted, wrong-count, wrong-path, wrong-digest, cross-version, or
commentary-bearing blocks.  It then independently capability-opens, reads,
and hashes all four active paths in order.  Only after all current-byte
hashes match may it set the internal nonserialized obligation
`R.effective_amendments=[v1,v2,v3,v4]` and permit lifecycle adjacency.

This changes no manifest key/schema, authority binding, generated artifact,
lifecycle node, edge, or topological order.

## 8. Mandatory fresh append-only independent re-review

Only after amendment v4 is frozen and externally hashed may an independent
reviewer append to:

```text
notes/phase2_control_design_peer_review.md
```

The complete current 96,524-byte / 1,910-line file at SHA-256
`ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41`
must remain the exact prefix, necessarily preserving all three nested prefix
receipts and both historical amendment blocks.

The reviewer must independently read and hash the complete
`base + v1 + v2 + v3 + v4` tuple and attack, rather than restate:

1. every requester audit-pair allocation, exact FD 5 slot, phase set,
   holder, credential, lifetime, EOF, and close rule;
2. every direct audit frame, P-issued one-use nonce, receipt, exact payload
   digest, actual FD-4 payload, G accepted transcript, byte comparison,
   confirmation, registration join, and admission production;
3. swapped request id/method/target/trigger/session, nonce replay, direct-vs-
   actual byte drift, missing requester packet, and two-requester endpoint
   exchange counterexamples;
4. every exact Unix-diag request/response field, source port, sequence,
   inode source, family/type/state, peer/shutdown attribute, reciprocal
   query, owner cardinality, preflight, close, and no-fallback branch;
5. simultaneous two-pair cross-wiring for FD 8 and FD 4, plus the P-held FD
   5 reciprocal mapping; and
6. regression of every closure in Section 5, all frozen counts, both exact
   historical blocks, the unique active count-four block, four independent
   amendment reads/hashes, and the unchanged manifest/DAG ceiling.

The reviewer may close `C-M1` or `C-M2` only from its own evidence.  Only a
final effective verdict `PASS C0/M0/m0` can support consideration of a later
implementation gate.  A partial repair, self-audit, copied digest, G-only
assertion, or unspecified kernel primitive remains `REVISE`.

## 9. Authorization matrix

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V4=PASS_TO_ONE_AMENDMENT_V4
CURRENT_OPEN_FINDINGS=C0_M2_m0
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v4.md
AMENDMENT_V4_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V4_FROZEN=true
CURRENT_REVIEW_PREFIX_SHA256=ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41
CURRENT_REVIEW_PREFIX_LINES=1910
CURRENT_REVIEW_PREFIX_BYTES=96524

C_M1_P_DIRECT_REQUESTER_WITNESS_REQUIRED=true
C_M1_G_FORWARDING_IS_INDEPENDENT_EVIDENCE=false
C_M1_REQUEST_AUDIT_FD=5
C_M1_FDSET_VALUES_REMAIN=4
C_M1_ONE_USE_NONCE_AND_RECEIPT_REQUIRED=true
C_M1_DIRECT_AND_ACCEPTED_PAYLOAD_EXACT_COMPARE=true
C_M2_PEER_ORACLE=NETLINK_SOCK_DIAG_UNIX_DIAG_PEER
C_M2_RECIPROCAL_MAPPING_REQUIRED=true
C_M2_FALLBACK_AUTHORIZED=false

BASE_COUNTS_MUST_REMAIN_UNCHANGED=true
SIX_IMPLEMENTATION_PATHS_MUST_REMAIN_UNCHANGED=true
MANIFEST_SCHEMA_MUST_REMAIN_UNCHANGED=true
AUTHORITY_BINDING_COUNT_MUST_REMAIN_14=true
PRINTED_DAG_MUST_REMAIN_8_NODES_12_EDGES=true
V3_AND_A_M_CLOSURES_MUST_NOT_REGRESS=true
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

This gate does not embed its own SHA-256.  Amendment v4 and the later fresh
independent re-review must bind this file's externally computed final digest.
No finding is closed by this authorization.
