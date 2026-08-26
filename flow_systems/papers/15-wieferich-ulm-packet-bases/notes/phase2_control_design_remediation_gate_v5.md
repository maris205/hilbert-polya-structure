# Replacement Paper 15 Phase-2 control-design remediation gate v5

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v5 — C0/M2/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v5.0`  
Date: 2026-08-17 (Asia/Shanghai)

This is a bounded design-remediation authorization, not a finding closure.
The current final append-only review's two major findings, `D-M1` and
`D-M2`, remain open.  This gate authorizes exactly one design-only amendment
and, only after that amendment is frozen and externally hashed, one fresh
independent append-only re-review.  It authorizes no generator, verifier,
test, wrapper, implementation, control execution, reproduction run, Route,
composition, manuscript, figure, release, archive, Git action, or public
synchronization.

## 1. Exact authority and current verdict

The complete current bytes of all ten records below were read and
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
| remediation gate v4 | `notes/phase2_control_design_remediation_gate_v4.md` | 645 | 30174 | `df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647` |
| design amendment v4 | `notes/phase2_control_design_amendment_v4.md` | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| current final append-only review | `notes/phase2_control_design_peer_review.md` | 2308 | 119250 | `cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab` |

The review's exact nested prefixes remain:

| Prefix lines | Prefix bytes | Independently recomputed SHA-256 |
|---:|---:|---|
| 1910 | 96524 | `ce39778a5cff3a9a6cbfc79e7141877fae26ec0106c38e5979a1d6b02e6eff41` |
| 1524 | 74876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| 1017 | 49358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| 488 | 22894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |

The complete effective verdict is **REVISE — C0/M2/m0**.  `D-M1` is the
absence of a P-visible, pre-receipt dynamic binding from an opaque top-runner
session to its method, trigger, and owner.  `D-M2` is the absence of a frozen
operation by which P obtains and `fstat`s the child's actual numbered socket
descriptor.  No amendment self-audit, gate, proposed frame, syscall name, or
fail-closed assertion is evidence against either finding.

The current review contains exactly three effective-amendment blocks.  The
historical `v1` count-two and `v2` count-three blocks are immutable inside
the preserved prefix.  Its sole current active successor is exactly:

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
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

All 119,250 review bytes, all four nested prefix receipts, and all three
existing blocks are immutable historical authority for the later append.
The theorem owner remains the bare compact group `B_p`; universal recovery
remains `OPEN_NOT_AUTHORIZED`; Route B remains false.

## 2. Sole amendment target, precedence, and bounded supersession

The target was absent before this gate was created.  Exactly one new design
file may be created:

```text
notes/phase2_control_design_amendment_v5.md
```

After that file is frozen and externally hashed, the effective design is
exactly:

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + amendment v2 c1d104d2...
  + amendment v3 f6a0af9c...
  + amendment v4 f5547926...
  + amendment v5 at its externally computed final digest.
```

Amendment v5 may supersede only:

1. amendment-v2's top-runner `SESSION_CREATE` request shape, opaque-session
   allocation/commit/close lifecycle, and amendment-v4 Section 3.3 only
   where P was required to consult an unregistered dynamic method/session
   binding, to add Section 3's direct session-authorization ledger and four
   exact P--G commit records;
2. amendment-v4 Section 4.5's contradictory phrase “no-follow actual-
   descriptor fstat,” and the v2 frozen x86_64 syscall/preflight inventory,
   only to add Section 4's exact `pidfd_open`/`pidfd_getfd` acquisition;
3. the P-only bootstrap/pre-suite state sequence only to add the exact
   actual-FD availability preflight below; and
4. amendment-v4 Section 7 only as to the current active count-four block
   being historical and the later active successor ending at v5.

The amendment must list every changed FD-5 frame, auth-ledger field, state
edge, syscall constant, per-process descriptor holder, local duplicate,
close edge, error branch, and verifier rule.  No optional frame, wildcard
owner, inferred syscall, alternate acquisition method, or unstated fallback
is permitted.  Every omitted base/v1/v2/v3/v4 clause remains binding.  The
amendment must not embed its own digest, claim independent closure, or
authorize implementation or execution.

## 3. D-M1 repair — direct single-use session authorization visible to P

### 3.1 Exact scope and authority source

The repair applies only to nonzero opaque method sessions created by the
already registered `TOP_TEST_CONTROLS` child on its unique FD-5
`REQUEST_AUDIT` endpoint.  `session=0` remains the fixed
`owner=SUITE_173` endpoint tuple and is never registered as a method
session.  `COPIED_REPRODUCE` does not create a session; its audit endpoint
may be allocated only from an already active registered method session.

P's authority source for the dynamic tuple is one direct seqpacket sent by
the top runner with plain `send` and received by P with `recvmsg`.  P must
require exactly one kernel-supplied `SCM_CREDENTIALS`, no requester-supplied
ancillary item, no other cmsg, and neither `MSG_TRUNC` nor `MSG_CTRUNC`.
The credential, outer PID, uid/gid 65534/65534, retained pidfd/start time,
stable `NSpid`, cgroup membership, inner PID, inner uid/gid 0/0, child role,
audit handle, and audit endpoint must equal the existing registered top-
runner identity.  A G-forwarded copy, P--G record, G session table, later G
accepted transcript, or a value copied from `AUDITED_SPAWN` is not this
independent authority.

### 3.2 Exact FD-5 session-auth frames

P, not G, becomes the sole allocator of nonzero opaque session decimals.
`session=0` stays reserved.  A P-allocated decimal is operational and
nonserialized, globally monotone, and never reused in the control lifetime.
G may create the private copied-package/lock state and install a session
record only through the exact P-owned grant and commit in Section 3.3; it no
longer chooses a method-session handle or independently supplies the tuple.

The amendment must add exactly these eight payload forms to the existing
closed FD-5 frame enum; the four v4 child-request audit frames remain exact:

```text
requester -> P:
SESSION_AUTH_OPEN audit=DEC auth_serial=DEC request=DEC method=METHOD trigger=TRIGGER owner=OWNER

P -> requester:
SESSION_AUTH_CHALLENGE audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64

requester -> P:
SESSION_AUTH_REGISTERED audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64 request=DEC method=METHOD trigger=TRIGGER owner=OWNER digest=LOWERHEX64 create=LOWERHEX

P -> requester:
SESSION_AUTH_RECEIPT audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64 request=DEC digest=LOWERHEX64

requester -> P:
SESSION_AUTH_ACTIVATED audit=DEC auth=DEC session=DEC request=DEC created=LOWERHEX

P -> requester:
SESSION_AUTH_ACTIVE_RECEIPT audit=DEC auth=DEC session=DEC request=DEC

requester -> P:
SESSION_AUTH_CLOSED audit=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME closed=LOWERHEX

P -> requester:
SESSION_AUTH_CLOSE_RECEIPT audit=DEC auth=DEC session=DEC close_request=DEC outcome=OUTCOME
```

Each payload is one complete canonical ASCII seqpacket, at most 4096 bytes,
with no NUL, LF, rights, explicit credentials, separate length prefix, or
trailing byte.  `DEC`, `LOWERHEX`, `LOWERHEX64`, `METHOD`, `TRIGGER`,
`OWNER`, and `OUTCOME` retain their existing closed grammars.  Continuation
above is presentational only.  The requester sends its four outbound forms
with plain `send`; P receives each with the exact kernel-credential check in
Section 3.1.  P's four replies use plain `send` and contain no ancillary
item.

`auth_serial` is a new P-owned per-audit-endpoint counter, initially zero,
increased by exactly one after each terminal registration attempt, with at
most one open value.  It is distinct from v4 child-request `serial`; neither
counter can advance or satisfy the other.  `auth` is a globally monotone
nonnegative P handle, never reused during the control lifetime.  P assigns
one fresh nonzero session together with `auth` and computes the sole
challenge nonce as lowercase SHA-256 of these exact ASCII bytes, with
canonical substitutions and no NUL or LF:

```text
P15R-SESSION-AUTH-NONCE-v1 audit=<AUDIT_DEC> requester_child=<CHILD_DEC> auth_serial=<AUTH_SERIAL_DEC> auth=<AUTH_DEC> session=<SESSION_DEC> request=<REQUEST_DEC> method=<METHOD> trigger=<TRIGGER> owner=<OWNER>
```

A challenge nonce and its assigned session are consumed by exactly one
successful registration or one failure and are never reissued.

`SESSION_AUTH_OPEN` is legal only immediately before the same endpoint's
method-session creation request.  P must derive the one legal `OWNER` from
the frozen method-ownership table; for an opaque method session it is
exactly that one frozen `METHOD`, not `SUITE_173` and not a caller-selected
alias.  P must also require the exact method/trigger ownership pair, the
endpoint's next RPC request number, and one of the unchanged 173 method
names.  Merely checking membership in the broad `TRIGGER` enum is
insufficient.

The P-issued binding digest is lowercase SHA-256 of exactly these canonical
ASCII bytes, with no NUL or LF:

```text
P15R-SESSION-AUTH-BINDING-v1 audit=<AUDIT_DEC> requester_child=<CHILD_DEC> auth_serial=<AUTH_SERIAL_DEC> auth=<AUTH_DEC> session=<SESSION_DEC> nonce=<NONCE> request=<REQUEST_DEC> method=<METHOD> trigger=<TRIGGER> owner=<OWNER>
```

`create` is lowercase hex of exactly this amended FD-4 RPC payload:

```text
SESSION_CREATE request=DEC session=DEC method=METHOD trigger=TRIGGER owner=OWNER auth=DEC nonce=LOWERHEX64 digest=LOWERHEX64
```

P decodes `create`, requires byte-for-byte canonical form, recomputes the
binding digest, and requires every explicit and decoded field to equal its
unconsumed challenge and independently derived owner.  Only then may P
store the immutable mapping

```text
session -> (method, trigger, owner, creator child, creator audit,
            creation request, auth, auth_serial, nonce, digest,
            exact SESSION_CREATE bytes)
```

and send `SESSION_AUTH_GRANTED` to G.  Only after that complete control-
channel send succeeds may P send `SESSION_AUTH_RECEIPT` to the requester;
the receipt therefore orders the P--G grant before the requester can send
the FD-4 payload.  `SESSION_AUTH_REGISTERED` occurs before the actual
`SESSION_CREATE`, before `SESSION_CREATED`, and necessarily before any v4
`AUDIT_RECEIPT` for that session.  Exactly one successful registration
exists for a nonzero session; its tuple and exact create bytes can never be
revised.

### 3.3 Exact P--G grant, accepted-byte join, and commit

The amendment must add exactly these four records to the closed P--G
protocol:

```text
P -> G:
SESSION_AUTH_GRANTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64 digest=LOWERHEX64 method=METHOD trigger=TRIGGER owner=OWNER payload=LOWERHEX

G -> P:
SESSION_AUTH_ACCEPTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64 digest=LOWERHEX64 payload=LOWERHEX

P -> G:
SESSION_AUTH_COMMIT requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64 digest=LOWERHEX64

G -> P:
SESSION_AUTH_COMMITTED requester_session=0 requester_child=DEC audit=DEC auth_serial=DEC auth=DEC session=DEC nonce=LOWERHEX64 digest=LOWERHEX64 method=METHOD trigger=TRIGGER owner=OWNER
```

Each is one canonical P--G control payload under the unchanged four-byte
big-endian length and 4096-byte ceiling, carries no ancillary item, and has
exactly the printed direction and fields.  `payload` is lowercase hex of
the complete registered `SESSION_CREATE` bytes, not a reserialization.
Every record occurs exactly once or the auth enters a failed tombstone.

P sends `SESSION_AUTH_GRANTED` only after the direct registration and before
the requester receipt.  The requester then sends on FD 4 the exact same
decoded `create` payload bytes.  G applies the existing endpoint, kernel-credential, pidfd,
request-number, role, and session-zero top-runner checks, compares the
complete actual FD-4 bytes with the one unconsumed P grant, and holds the
request without allocating a different handle, creating the copy/lock
state, or installing a session.  G reports the actual received bytes in
`SESSION_AUTH_ACCEPTED`.

P decodes that report and requires exact byte equality with its immutable
direct requester registration, plus equality of every credential-bound
requester, audit, auth, session, method, trigger, owner, nonce, and digest
coordinate.  G's report supplies none of P's expected values.  Only this
complete two-channel join permits `SESSION_AUTH_COMMIT`.

After commit, G constructs the sole session record by copying the immutable
P-granted session, method, trigger, and owner fields; there is no second G
binding input or private allocator.  It creates the unchanged private copy
and isolated lock parent, sends `SESSION_AUTH_COMMITTED` with the copied
tuple, and only then replies on FD 4 with the unchanged exact
`SESSION_CREATED request=DEC session=DEC`.  The reply session must equal the
P-assigned session.  A different private G tuple is not a second operational
world: it is an unreachable, noncommitted protocol violation that cannot
produce `SESSION_CREATED` or child action.

The requester then sends kernel-authenticated `SESSION_AUTH_ACTIVATED`, with
`created` equal to lowercase hex of the exact complete `SESSION_CREATED`
reply.  P decodes it, requires the request and session to match the direct
registration, commit, and G committed record, and only then sends
`SESSION_AUTH_ACTIVE_RECEIPT`.

### 3.4 Mandatory pre-receipt join, close, and lifecycle

The exact P ledger is:

```text
UNSEEN
  -> CHALLENGE_ISSUED
  -> REGISTERED_PENDING_G
  -> G_BYTES_MATCHED
  -> COMMIT_SENT
  -> G_COMMITTED_AWAITING_ACTIVATION
  -> REGISTERED_ACTIVE
  -> CLOSE_PENDING
  -> CLOSED_TOMBSTONE

any nonterminal state -> FAILED_TOMBSTONE
```

`SESSION_AUTH_RECEIPT` enters `REGISTERED_PENDING_G`;
`SESSION_AUTH_COMMIT` enters `COMMIT_SENT`; and
`SESSION_AUTH_ACTIVE_RECEIPT` is the sole transition to
`REGISTERED_ACTIVE`.  Before P sends any v4 `AUDIT_RECEIPT`, it must require
exactly one active mapping for the direct `AUDITED_SPAWN` session and exact
equality of method, trigger, owner, creator, purpose ownership, and all
unchanged static request coordinates.  The expected tuple comes from P's
stored registration, never from the current `AUDITED_SPAWN` fields or G's
report.  A copied requester inherits the one mapping only after its parent
audited spawn has been bound to that active session.  One active
registration may authorize the session's existing sequence of distinct
requests, but the auth is not a transferable bearer token.

The retained ordering is exactly:

```text
SESSION_AUTH_OPEN / SESSION_AUTH_CHALLENGE
  -> SESSION_AUTH_REGISTERED
  -> SESSION_AUTH_GRANTED / SESSION_AUTH_RECEIPT
  -> amended SESSION_CREATE actual FD-4 bytes
  -> SESSION_AUTH_ACCEPTED / SESSION_AUTH_COMMIT
  -> SESSION_AUTH_COMMITTED / existing SESSION_CREATED
  -> SESSION_AUTH_ACTIVATED / SESSION_AUTH_ACTIVE_RECEIPT
  -> zero or more existing authorized session operations and audited spawns
  -> all spawned children terminal and all session roots/lock state terminal
  -> existing SESSION_CLOSE / SESSION_CLOSED
  -> SESSION_AUTH_CLOSED / SESSION_AUTH_CLOSE_RECEIPT
  -> CLOSED_TOMBSTONE
```

After the existing `SESSION_CLOSE` reply, `SESSION_AUTH_CLOSED.closed` is
lowercase hex of the exact complete
`SESSION_CLOSED request=DEC session=DEC outcome=OUTCOME` reply.  P decodes
and parses it and requires equality with the explicit session,
`close_request`, and `outcome`, the active mapping, and the existing closed
session terminal predicate before it sends the close receipt.  Tombstones
persist through complete P teardown and make every replay, reuse, delayed
packet, or second close distinguishable.

A missing, duplicate, wrong-direction, wrong-credential, wrong-owner,
cross-session, cross-method, cross-trigger, reused-nonce, changed-byte,
malformed, premature-close, post-close, or EOF transition fails before the
next child action.  An endpoint crash or EOF with an open challenge or live
session goes to `FAILED_TOMBSTONE`, closes admission, and invokes the
existing containment/cleanup path; it never silently closes the session or
permits reuse.  An auth/session consumed by any failed G match, commit,
session creation, activation, or close has no retry path.  No G-supplied
assertion can repair a missing direct record.  No CSV value, method, target,
public detector, result field, or exit class is added.

### 3.5 Mandatory hostile pairs

The amendment must preserve enough exact state for the later independent
reviewer to attack at least:

1. an attempt to install or commit a private G tuple different from the
   P-granted tuple before the same later direct `AUDITED_SPAWN`;
2. the same session decimal with registered method or trigger changed;
3. a valid G session table but no direct `SESSION_AUTH_REGISTERED`;
4. a registration copied from another top-runner audit endpoint;
5. one nonce, auth, session, or raw create/created transcript replayed;
6. an `AUDIT_RECEIPT` attempted in `CHALLENGE_ISSUED`, `CLOSE_PENDING`, or a
   tombstone state; and
7. a copied requester bound to a different active method session.

The required predicate must differ in each hostile pair.  P's direct
kernel-authenticated registration plus the grant/actual-byte/commit
production chain must either distinguish the worlds before the child-request
receipt or make the mismatched world unreachable before `SESSION_CREATED`.
Looking the tuple up in the same current request is tautological and does
not satisfy this contract.

## 4. D-M2 repair — exact actual-FD acquisition and fstat

### 4.1 Sole native x86_64 primitive

The sole actual-foreign-descriptor acquisition mechanism is the Linux
x86_64 native syscall pair:

```text
pidfd_open:
  x86_64 syscall number = 434
  arguments             = (outer_pid, flags=0)

pidfd_getfd:
  x86_64 syscall number = 438
  arguments             = (pidfd, targetfd, flags=0)
```

Both calls are made through the amendment's byte-bound in-source syscall
binding on the already frozen native x86_64, little-endian LP64 ABI.  The
x32 table remains killed before dispatch.  Runtime headers, libc feature
detection, a helper process, `/proc/PID/fd` pathname following, `SCM_RIGHTS`,
`kcmp`, ptrace attachment, a service, or another architecture is not an
alternate mechanism.

`pidfd_open` flags are exactly zero.  Its successful result must be a
nonnegative P-local pidfd with `FD_CLOEXEC` set.  `pidfd_getfd` flags are
exactly zero.  Its successful result must be a nonnegative P-local duplicate
of the target process's exact numbered descriptor, referring to the same
open file description, with `FD_CLOEXEC` set.  P must verify each returned
descriptor with `fcntl(F_GETFD)`; any bit result other than exactly
`FD_CLOEXEC` is failure.  Neither call's pidfd or duplicate number, by
itself, is a socket identity.

Every required live-pidfd check is exactly one
`poll([{fd=PIDFD,events=POLLIN}],1,0)` returning zero, with no returned
event.  A positive return, `POLLIN`, `POLLHUP`, `POLLERR`, `POLLNVAL`, any
other `revents` bit, or a negative return is not live identity.

The kernel's successful `pidfd_getfd` is the mandatory runtime permission
test under `PTRACE_MODE_ATTACH_REALCREDS`.  P must not infer permission from
uid zero, namespace ancestry, `CAP_SYS_PTRACE`, kernel version,
`ptrace_scope`, an LSM file, or a successful `/proc` read.  `ENOSYS`,
`EINVAL`, `EPERM`, `EBADF`, `ESRCH`, `EMFILE`, `ENFILE`, any other errno,
LSM denial, or an ambiguous success is fail-closed.  There is no fallback.

### 4.2 Fail-before-write availability preflight

The v4 `PEER_ORACLE_PREFLIGHTED` two-pair Unix-diag test remains unchanged.
The v5 acquisition preflight occurs under the actual nested uid/gid maps,
dumpable-zero rule, cgroup placement, and process credentials, using the
already required first `CGROUP_PROBE_CHILD epoch=1` while that existing
probe child is blocked with its exact FD 8 barrier.  It creates no seventh
session-zero child, target, method, or probe epoch.

Before any package, result, package-lock, private generation-root,
generated-member, or subject write, P must:

1. independently identify the probe child's unique outer PID from the
   existing pid-namespace, `NSpid`, cgroup, credential, one-thread, and
   start-time receipts;
2. invoke native `pidfd_open(outer_pid,0)`, require `FD_CLOEXEC`, require the
   exact zero-timeout live-pidfd poll above, and re-read the same start time, `NSpid`,
   credentials, and cgroup membership without drift;
3. invoke native `pidfd_getfd(child_pidfd,8,0)`, require `FD_CLOEXEC`, and
   `fstat` that obtained duplicate as `S_IFSOCK` with a nonzero inode no
   larger than `0xffffffff`;
4. require the existing canonical
   `/proc/<outer-pid>/fd/8 -> socket:[INODE_DEC]` text to name exactly that
   `fstat` inode, while treating the text only as a comparison receipt;
5. query the unchanged v4 Unix-diag oracle for that inode, independently
   find exactly one matching G-held barrier peer as in Section 4.4, and
   require the two reciprocal queries;
6. close every P-local obtained duplicate as in Section 4.5, prove each
   exact local FD number returns `EBADF` to immediate `fcntl(F_GETFD)`, and
   then re-query the still-live original child/G
   pair in both directions to prove that acquisition and close did not
   consume or substitute either original; and
7. only after all of those checks permit the existing epoch-1 probe to
   continue.

The preflight is a runtime operation, not a claim about the present host.
Failure follows the existing bootstrap/pre-suite kill, reap, populated-zero,
and cleanup path and returns `E_POSSESSION_UNAVAILABLE` before any write
listed above.  No platform-specific error may select another primitive.

### 4.3 Exact process identity and pidfd lifetime

For each runtime G child, P opens exactly one audit pidfd with
`pidfd_open(outer_pid,0)` after the child has supplied its frozen
first-instruction identity and while it remains blocked, and before P's
first descriptor audit.  P joins the outer PID to the existing unique
child/session/role/owner record, stable start time, complete `NSpid` chain,
credentials, one-thread state, and workers-cgroup membership both before and
after opening.  Any exit indication, PID disappearance, start-time drift,
PID reuse, namespace mismatch, or cgroup mismatch invalidates the pidfd.

That exact pidfd, not a newly looked-up PID, is used for every later
`pidfd_getfd` acquisition for the child.  P retains it through the child's
existing close, exit, wait/reap, and `CHILD_REAPED` reconciliation, then
closes it exactly once and, without an intervening allocation, requires
immediate `fcntl(F_GETFD)` on that number to return `-1` with `EBADF`.  It is never
sent, duplicated to a worker, serialized, or used as a socket FD.

For G-held peer acquisition, P uses only the existing authenticated guardian
pidfd opened during the v2 guardian handshake, with its retained guardian
outer PID, start time, one-thread, credentials, namespace, and guardian-
cgroup identity rechecked at each acquisition.  That pidfd retains its
existing lifetime through G reap.  No child pidfd may name G and no guardian
pidfd may name a child.

### 4.4 Exact child and G-peer acquisition at every live audit

For each v4 live-matrix audit of a child socket slot 8, 4, or 5, P performs
this order while the child is blocked at the already frozen registration,
`SOURCE_READY`, or freeze/reference barrier:

```text
child duplicate = pidfd_getfd(exact child audit pidfd, exact child slot, 0)
  -> require FD_CLOEXEC
  -> fstat duplicate
  -> require S_IFSOCK and record (st_dev, st_ino)
  -> compare st_ino with the canonical proc socket text
  -> query diag(st_ino)
```

For slots 8 and 4, the Unix-diag peer inode returned from the child inode is
located at G without trusting a G FD number.  While single-threaded G is in
the corresponding frozen control state, P enumerates G's complete canonical
numeric descriptor set immediately before acquisition and again after all
candidate fstats, requiring byte-for-byte equal ordered decimal sets.
Canonical proc link text
may select entries whose object type is socket, but cannot establish their
identity.  For every selected numeric `targetfd`, P invokes
`pidfd_getfd(guardian_pidfd,targetfd,0)`, requires `FD_CLOEXEC`, and `fstat`s
the obtained duplicate.  Exactly one live G duplicate must be `S_IFSOCK`
with the returned peer inode and the existing registered holder role; zero,
two, a disappearing entry, a changed numeric set, or an acquisition failure
is fatal.  P then requires:

```text
diag(child_fstat_inode) = G_peer_fstat_inode
diag(G_peer_fstat_inode) = child_fstat_inode
```

For slot 5, P obtains and `fstat`s the child FD 5 through
`pidfd_getfd` in the same order, directly `fstat`s its sole retained local
audit peer, and requires the same reciprocal equality.  G must contain zero
FD-5 endpoint or peer copies as already frozen.  P's local peer does not use
`pidfd_getfd`.

The v4 canonical proc symlink check remains a second comparison coordinate,
but the phrase “no-follow actual-descriptor fstat” is replaced only by
`pidfd_getfd` followed by `fstat` on the returned local duplicate.  `fstat`
of a pidfd, `fstatat(...,AT_SYMLINK_NOFOLLOW)` of a proc magic link, following
that link with `stat`/`fstatat`, and relabeling readlink text as an `fstat`
result are all forbidden.

P uses an obtained duplicate only for `fcntl(F_GETFD)`, `fstat`, the existing
nonmutating type checks, and derivation of the inode supplied to the
Unix-diag query.  It never reads, writes, sends, receives, polls for payload,
binds, connects, accepts, shuts down, changes file status flags, changes an
offset, or transfers an obtained duplicate.  The original endpoint remains
owned by the target process throughout the audit.

### 4.5 Exact local-duplicate close discipline

Every `pidfd_getfd` result is P-local and short-lived.  P is single-threaded
and allocates no other FD between obtaining and disposing of it.  After the
two `fstat` inode values and both reciprocal Unix-diag results are fixed, P
closes every obtained child and G duplicate exactly once, accepts only a
zero return, and never retries a failed close.  Without any intervening FD
allocation, it then calls `fcntl(F_GETFD)` on each exact closed number and
requires `-1` with `EBADF`.  Only after every such absence check may P send
`ADMIT`, `SOURCE_READY` acknowledgment, `START`, thaw, or another action that
permits an original endpoint to close.

An obtained duplicate must never cross the child's original close edge:
retaining it would keep the Unix socket endpoint alive and invalidate EOF,
shutdown, peer-close, and reap evidence.  A close error, lingering local FD,
FD-number reuse, or reciprocal requery drift is a containment failure, not a
receipt.  Child audit pidfds and the guardian pidfd follow their distinct
longer lifetimes in Section 4.3; closing a short-lived socket duplicate never
closes the process's original descriptor.

Before target action, any unavailable or nonunique pidfd, target slot,
duplicate, fstat, proc comparison, G holder, reciprocal relation, or close
is `E_POSSESSION_UNAVAILABLE`.  After `START`, the same defect invokes the
existing fatal freeze/kill/reap/cleanup path and cannot produce `PASS` or
`ABSENT`.  No public detector or exit class is added.

### 4.6 Mandatory hostile pairs

The later reviewer must be able to distinguish at least:

1. a child pidfd and the child's slot FD with the same numeric value but
   different underlying objects;
2. one outer PID reused across two start times;
3. canonical proc text naming inode A while `fstat` of the obtained duplicate
   yields inode B;
4. a true child endpoint paired with the wrong one of two simultaneous G
   peers while local FD numbers, types, credentials, and CLOEXEC bits match;
5. a successful child duplicate with zero or two matching G-held peers;
6. a P-local duplicate retained across the original child close; and
7. `pidfd_getfd` denied by the actual ptrace/LSM policy while proc reads and
   Unix-diag queries remain available.

Trust in G, fail-closed prose, a copied inode, or success of another kernel
primitive cannot distinguish these pairs and is not a repair.

## 5. Required preservation of all prior closures

Amendment v5 must retain without weakening:

1. v4 `C-M1` closure: the child-unique P-created FD 5, exact FDSET row,
   kernel credentials, P-issued one-use child-request nonce, requester-direct
   bytes, actual FD-4 bytes, exact byte comparison, G confirmation, audited
   registration, and P-derived admission;
2. v4 `C-M2` closure: the exact 40-byte request, 48-byte response,
   sequence/port/source/cardinality rules, two simultaneous preflight pairs,
   reciprocal `UNIX_DIAG_PEER` mapping, crossed-pair rejection, owner matrix,
   and no fallback;
3. v3 `B-M1`: two operational owners, six exact session-zero rows, closed
   post-suite owner grammar, and the exact 173-method boundary;
4. v3 `B-M2`: exact phase-indexed descriptor sets, four-frame admission
   barrier, source/root/RPC lifetimes, drain, EOF, close, and reap order,
   strengthened only by Section 4's acquisition mechanism;
5. v3 `B-M3`: G-created pre-access registration/ACK, generator authorized-
   basename/purpose creation, post-reap enumerate/register/ACK before
   exchange/cleanup/reference audit, P25 count zero, and unexpected-object
   nondeletion;
6. `A-M1`: exact unparameterized `SG_SCOPE`, primitive-only evidence-class
   projection, post-recomputation expected class, and every primitive-prefix
   and witness counterfactual;
7. `A-M2`: real-filesystem recursive receipts, all valid and malformed
   variants, five live metadata falsifiers, and exact-one-coordinate actual-
   receipt mode/mtime comparator probes without ctime masking;
8. `A-M3`: private possession, two namespace layers, atomic cgroup
   placement, freeze/kill/reap/populated-zero proof, retained parent/root/
   lock capabilities, capability-relative cleanup, both replacement phases,
   five replacement fixtures, foreign preservation, and no false `ABSENT`;
   and
9. `A-M4`: complete-review authentication before parsing, unique canonical
   effective-amendment list, capability-relative independent amendment reads
   and hashes, and dereference before lifecycle adjacency.

A v5 repair that regresses any prior closure creates a new open finding.  It
cannot trade one finding for another or declare a conditional pass.

## 6. Frozen counts, paths, schemas, and DAG

Amendment v5 and its later re-review must preserve exactly:

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
rows and their order, all 35 negative rows, all 35 semantic methods, all 28
package methods, all 173 method names, all nine generated paths, all fourteen
authority paths, manifest key set and schema, and printed graph nodes
`A,D,R,G,I,C,M,V` with twelve distinct edges remain unchanged.  Session-auth
frames, auth ledgers, pidfds, obtained duplicates, fstat receipts, and close
receipts are operational, in-memory, and nonserialized.

If either repair requires a CSV/schema/generated-byte change, a seventh
implementation path, a new method, target, mutation class, public detector,
exit class, authority binding, manifest node/edge, theorem owner, Route, or
publication-boundary change, amendment v5 must stop and report a new design
finding rather than silently widen scope.

## 7. Append-only v5 successor receipt while preserving A-M4

The current review's historical `v1` count-two, `v2` count-three, and `v3`
count-four blocks cannot be edited, normalized, reordered, duplicated, or
treated as the new active list.  After amendment v5 is frozen and externally
hashed, the fresh independent reviewer must append exactly one active
successor block:

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
5.sha256=<exact externally computed final v5 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

There is no blank or commentary line inside an actual block.  Amendment v5
must version the internal review-node grammar so the final verifier:

1. capability-opens the unchanged manifest-bound review path once, checks
   the existing canonical regular/nlink-one/no-link rules, hashes the
   complete post-v5 review bytes from that FD, and matches the manifest's
   complete-review digest before parsing;
2. parses only those authenticated bytes and requires exactly one historical
   `v1` block byte-equal to its preserved current bytes, exactly one
   historical `v2` block byte-equal to its preserved current bytes, exactly
   one historical `v3` block byte-equal to Section 1, exactly one active
   `v4` block in the count-five form above, and no other effective-amendment
   begin/end tag;
3. rejects missing, duplicate, reordered, nested, malformed, prefix-drifted,
   wrong-count, wrong-index, wrong-path, wrong-digest, cross-version,
   extra-key, blank, or commentary-bearing blocks;
4. independently capability-opens v1, v2, v3, v4, and v5 in active order
   beneath the same held package-root FD with the existing no-link/beneath
   rules, reads every byte, and independently recomputes all five hashes;
   and
5. only after all five hashes match sets the internal nonserialized
   obligation `R.effective_amendments=[v1,v2,v3,v4,v5]` and permits
   lifecycle adjacency.

This dereference adds no manifest key, authority binding, generated artifact,
node, edge, review self-hash, future-result edge, or proof cycle.

## 8. Mandatory fresh append-only independent re-review

Only after amendment v5 is frozen and externally hashed may an independent
reviewer append to:

```text
notes/phase2_control_design_peer_review.md
```

The complete current 119,250-byte / 2,308-line file at SHA-256
`cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab`
must remain its exact prefix, necessarily preserving every nested prefix and
all three existing effective-amendment blocks.

The reviewer must independently read and hash the complete
`base + v1 + v2 + v3 + v4 + v5` tuple and attack, rather than restate:

1. every direct session-auth frame, credential, raw create/created transcript,
   digest, nonce, auth/session uniqueness rule, method/trigger/owner
   derivation, lifecycle, close, tombstone, replay, and failure branch;
2. the exact pre-`AUDIT_RECEIPT` join under the D-M1 two-world
   counterexample, including a changed private G binding and a missing direct
   registration;
3. syscall numbers 434/438, native ABI and zero flags, actual
   `PTRACE_MODE_ATTACH_REALCREDS` permission success, pidfd/process identity,
   target-slot selection, returned FD CLOEXEC, same-open-file-description
   semantics, fstat, and every local close;
4. the actual nested-security preflight before writes, plus every no-fallback
   failure including ENOSYS, EPERM, EBADF, ESRCH, LSM denial, process drift,
   and descriptor ambiguity;
5. child actual-FD fstat versus canonical proc text, independent G-peer
   acquisition, reciprocal Unix-diag comparison, simultaneous crossed pairs,
   and proof that no P duplicate crosses an original endpoint close;
6. regression of every closure in Section 5 and every invariant in Section
   6; and
7. the immutable v1/v2/v3 blocks, unique active v4 count-five block, five
   independent amendment reads/hashes, and unchanged fourteen-binding,
   eight-node, twelve-edge manifest ceiling.

The reviewer may close `D-M1` or `D-M2` only from its own evidence.  Only an
independent final effective verdict `PASS C0/M0/m0` can support later
consideration of an implementation gate.  A partial repair, amendment
self-audit, G-only session assertion, proc-link-only inode, permission
inference, unspecified local-FD lifetime, or fallback remains `REVISE`.

## 9. Authorization matrix

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V5=PASS_TO_ONE_AMENDMENT_V5
CURRENT_OPEN_FINDINGS=C0_M2_m0
D_M1_STATUS=OPEN
D_M2_STATUS=OPEN
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v5.md
AMENDMENT_V5_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V5_FROZEN_AND_EXTERNALLY_HASHED=true
CURRENT_REVIEW_PREFIX_SHA256=cdf9c168c0e5492e5c6e717d5bec897374abf065d3198d9f7a5d5ebc9ca403ab
CURRENT_REVIEW_PREFIX_LINES=2308
CURRENT_REVIEW_PREFIX_BYTES=119250

D_M1_DIRECT_SESSION_AUTH_REQUIRED=true
D_M1_SESSION_AUTH_REGISTERED_KERNEL_AUTHENTICATED=true
D_M1_SESSION_AUTH_REGISTERED_SINGLE_USE=true
D_M1_SESSION_AUTH_REQUIRED_BEFORE_AUDIT_RECEIPT=true
D_M1_G_SELF_REPORT_IS_INDEPENDENT_EVIDENCE=false
D_M1_SESSION_TUPLE=SESSION_METHOD_TRIGGER_OWNER
D_M1_TOMBSTONE_REUSE_AUTHORIZED=false

D_M2_PIDFD_OPEN_X86_64_SYSCALL=434
D_M2_PIDFD_GETFD_X86_64_SYSCALL=438
D_M2_PIDFD_FLAGS=0
D_M2_PIDFD_GETFD_FLAGS=0
D_M2_PERMISSION_CHECK=PTRACE_MODE_ATTACH_REALCREDS_RUNTIME_SUCCESS
D_M2_RETURNED_FD_CLOEXEC_REQUIRED=true
D_M2_FSTAT_OBTAINED_DUPLICATE_REQUIRED=true
D_M2_RECIPROCAL_UNIX_DIAG_REQUIRED=true
D_M2_DUPLICATE_MAY_CROSS_ORIGINAL_CLOSE=false
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

This gate does not embed its own SHA-256.  Amendment v5 and the later fresh
independent append-only re-review must bind this file's externally computed
final digest.  No finding is closed by this authorization.
