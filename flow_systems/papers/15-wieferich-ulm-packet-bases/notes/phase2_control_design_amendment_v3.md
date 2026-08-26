# Replacement Paper 15 deterministic-control design amendment v3

Status: **FROZEN AMENDMENT CANDIDATE — B-M1--B-M3 CLOSED BY DESIGN / FRESH INDEPENDENT EXACT-BYTE RE-REVIEW REQUIRED**  
Version: `P15R-CONTROLS-AMENDMENT-v3.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Amendment self-audit: **C0/M0/m0 against B-M1--B-M3; not an independent PASS**  
Control implementation or execution performed here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS experiment-agent, integrity and reproducibility protocols,
  plus academic-paper authoring discipline
- Origin Mode: plan / deterministic exact-arithmetic control-design amendment
- Origin Date: 2026-08-17
- Verification Status: UNVERIFIED_PENDING_FRESH_INDEPENDENT_REREVIEW
- Version Label: `p15r_control_design_amendment_v3`
- Scope: only the three final-review findings `B-M1`, `B-M2`, and `B-M3`,
  plus the append-only successor receipt needed to bind this amendment; no
  generator, verifier, test, result, theorem, Route, manuscript, release, or
  publication claim

## 1. Exact authority, precedence, and bounded supersession

### 1.1 Complete current-byte authority

The complete bytes of all seven records below were read and independently
re-hashed before this amendment was written:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| design amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| remediation gate v2 | `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` |
| design amendment v2 | `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| current final append-only review | `notes/phase2_control_design_peer_review.md` | 1524 | 74876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |
| remediation gate v3 | `notes/phase2_control_design_remediation_gate_v3.md` | 578 | 27299 | `e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac` |

The review's first 49,358 bytes remain exactly
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`,
and its first 22,894 bytes remain exactly
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.
Its complete current effective verdict is `REVISE_C0_M3_m0`.  This
amendment's self-audit is not evidence against that verdict.

After this file is externally hashed, the effective design is exactly

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + amendment v2 c1d104d2...
  + this amendment v3 at its externally computed final digest.
```

This amendment does not embed, predict, or self-authenticate its own digest.

### 1.2 Exact supersessions

This amendment supersedes only the following v2 clauses:

1. for `B-M1`, amendment-v2 Section 5.3's `OWNER` rule and the exact
   `CHILD_REGISTERED` / `CHILD_ADMITTED` payloads, directions, cardinalities,
   and release meaning, plus the corresponding pre-suite child ownership in
   Sections 5.2, 5.5, and 5.9;
2. for `B-M2`, amendment-v2 Section 5.5's four undefined `FDSET` values,
   role-whitelist prose, one-use-barrier release, and child-descriptor
   lifetime prose, plus the matching `SPAWN` admission transition in Section
   5.9 and Section 5.3's closed P--G enum only to add `SOURCE_READY` and
   `START`;
3. for `B-M3`, amendment-v2 Section 5.5's unconditional statement that every
   `OBJECT_REGISTERED` precedes every child access, and only the creation,
   registration, acknowledgment, and post-creator-ledger ordering clauses in
   Sections 5.6--5.9 which depend on it, plus Section 5.3's closed P--G enum
   only to add the six B-M3 acknowledgment/authorization/ledger records
   listed below; and
4. for the v3 successor receipt, amendment-v2 Sections 6.1--6.2 only as to
   the count-two block being the active grammar and the internal resolved
   list ending at v2.

The exact operational changes are exhausted by:

```text
OWNER additions:
  BOOTSTRAP_G
  REPRO_COORDINATOR

ADMISSION additions:
  six literal pre-suite/top-runner values in Section 3
  one exact post-suite method-child production in Section 3

FDSET replacement enum:
  STDIO_BARRIER
  STDIO_SOURCE_BARRIER
  STDIO_SOURCE_ROOT_BARRIER
  STDIO_SOURCE_RPC_BARRIER

modified records:
  CHILD_REGISTERED
  CHILD_ADMITTED

new P--G records:
  SOURCE_READY
  START
  CHILD_REAPED_ACK
  OBJECT_REGISTERED_ACK
  MEMBER_CREATE_AUTHORIZED
  MEMBER_CREATE_ACK
  MEMBER_LEDGER_CLOSED
  MEMBER_LEDGER_ACK

new child-barrier frames:
  SANITIZED
  ADMIT
  SOURCE_READY
  START

review-node grammar:
  historical effective-amendment block v1 remains count two
  active effective-amendment block v2 has count three
```

No other `ROLE`, `TARGET`, `KIND`, generation `PURPOSE`, `TRIGGER`,
`DETECTOR`, `OUTCOME`, public exit class, detector, generated field, or
serialized enum changes.  Every omitted base/v1/v2 clause remains binding.

## 2. Frozen invariants retained exactly

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

The six implementation paths, eight CSV paths and headers, all 120 body
rows and their order, all 35 semantic-negative rows, all 35 `S` methods,
all 28 `P` methods, all 173 method names, all nine generated paths, all
fourteen authority paths, the manifest key set and schema, and the lifecycle
order `A,D,R,G,I,C,M,V` with its twelve distinct edges remain unchanged.
Every record introduced below is operational, in-memory, and nonserialized.

## 3. B-M1 — closed owner, role, and admission protocol

### 3.1 Exact `OWNER` domain and cardinalities

The amended closed `OWNER` domain is exactly:

```text
BOOTSTRAP_G
REPRO_COORDINATOR
SUITE_173
each exact one of the already frozen 173 unittest method names
```

`BOOTSTRAP_G` owns exactly two G-created children: the cgroup preflight
micro-stubs for epochs 1 and 2.  `REPRO_COORDINATOR` owns exactly three
G-created children: checked-in verify-only and canonical generations A and
B.  `SUITE_173` owns exactly one G-created child, the actual top-level
`test_controls` runner.  None of these three operational tokens is a method
name.  No operational token owns a later method child, and no method name
owns a bootstrap, pre-suite, or top-runner child.

L, G itself, and P's initial-user-namespace privilege probe are not G
children and consume no `OWNER`, admission token, or child sequence row in
this section.  There is no other G child before `TOP_TEST_CONTROLS`.

### 3.2 Exact `ADMISSION` domain

For the six session-zero rows in Section 3.3, `ADMISSION` is exactly one of
these six literal values:

```text
BOOTSTRAP_FREEZE_THAW_E1
BOOTSTRAP_KILL_E2
PRE_SUITE_VERIFY_ONLY
PRE_SUITE_CANONICAL_A
PRE_SUITE_CANONICAL_B
SUITE_173_TOP_RUNNER
```

After `SUITE_ENTRY`, a method-owned child has exactly one single-use value
with this canonical ASCII grammar:

```text
METHOD_V1:<METHOD>:S<SESSION_DEC>:R<REQUEST_DEC>:C<CHILD_DEC>
```

`METHOD` is exactly one of the frozen 173 names.  `SESSION_DEC`,
`REQUEST_DEC`, and `CHILD_DEC` are the already registered canonical
nonnegative-decimal session, endpoint request, and G-child identifiers; no
leading zero is legal except the number `0`.  G constructs the value only by
the printed deterministic production from its authenticated per-endpoint RPC
mapping and exact accepted request; it does not choose or propose an
alternative.  P independently derives the expected bytes instead of trusting
G's copy in `CHILD_REGISTERED`.  The method token is valid only when:

```text
registered OWNER = METHOD
registered session = SESSION_DEC
registered child = CHILD_DEC
the accepted request id = REQUEST_DEC
the request's target, purpose, trigger, role, and session are all authorized
```

P records every admission value before sending it and rejects reuse across
children, sessions, requests, phases, or owners.  This production does not
add a method or widen the exact 173-name set.  There is no `current_method`,
wildcard, inherited default, reusable bearer, random nonce, or caller-chosen
admission value.

### 3.3 Complete G-child sequence through suite entry

| Order / phase | Exact target identity | Session | `OWNER` | `ROLE` | `PURPOSE` | Exact admission | Cardinality |
|---:|---|---:|---|---|---|---|---:|
| 1, `CGROUP_PREFLIGHT_E1` | `CGROUP_PROBE_CHILD epoch=1` | `0` | `BOOTSTRAP_G` | `PROBE` | `NONE` | `BOOTSTRAP_FREEZE_THAW_E1` | 1 |
| 2, `CGROUP_PREFLIGHT_E2` | `CGROUP_PROBE_CHILD epoch=2` | `0` | `BOOTSTRAP_G` | `PROBE` | `NONE` | `BOOTSTRAP_KILL_E2` | 1 |
| 3, `PRE_SUITE_VERIFY` | `VERIFY_ONLY_GENERATOR` | `0` | `REPRO_COORDINATOR` | `GENERATOR` | `NONE` | `PRE_SUITE_VERIFY_ONLY` | 1 |
| 4, `PRE_SUITE_A` | `GENERATE_CANONICAL_A` | `0` | `REPRO_COORDINATOR` | `GENERATOR` | `CANONICAL_A` | `PRE_SUITE_CANONICAL_A` | 1 |
| 5, `PRE_SUITE_B` | `GENERATE_CANONICAL_B` | `0` | `REPRO_COORDINATOR` | `GENERATOR` | `CANONICAL_B` | `PRE_SUITE_CANONICAL_B` | 1 |
| 6, `SUITE_ENTRY` | `TOP_TEST_CONTROLS` | `0` | `SUITE_173` | `TOP_TEST_RUNNER` | `NONE` | `SUITE_173_TOP_RUNNER` | 1 |

All six use the already reserved session `0`.  No method-session handle may
be allocated or used before `SUITE_ENTRY`.  The epoch-one and epoch-two
cgroup probes retain their exact freeze/thaw and kill meanings, but each is
first sanitized, registered, independently verified, and admitted under its
printed row.  Only after that admission may its existing
`CGROUP_PROBE_CHILD` and epoch-specific records proceed.  Admission does not
bypass B-M2: the freeze/thaw or kill control action begins only after that
probe has also completed its no-source `SOURCE_READY`, P's second audit,
`START`, and the running-column check.

### 3.4 Exact child-registration records and guards

The canonical records superseding the two v2 payloads are exactly:

```text
CHILD_REGISTERED session=DEC child=DEC inner_pid=DEC role=ROLE owner=OWNER purpose=PURPOSE admission=ADMISSION fdset=FDSET cwd_dev=DEC cwd_ino=DEC
CHILD_ADMITTED session=DEC child=DEC admission=ADMISSION
```

`CHILD_REGISTERED` is G-to-P exactly once per G child after G receives that
child's `SANITIZED` frame, after clone3 has returned the PID and pidfd, and
before any target or loader instruction.  `CHILD_ADMITTED` is P-to-G exactly
once only after P's first independent actual-descriptor and membership audit
passes and, for a creation-capable generator target as defined in Section
5.3, after Section 5's creation authorization has also been acknowledged.
Both records repeat the identical admission bytes.

`CHILD_ADMITTED` does **not** authorize target execution.  It authorizes G
only to send the child-barrier frame `ADMIT`; the child remains blocked for
source handling and the second audit in Section 4.  A missing, unknown,
noncanonical, duplicate, reused, wrong-direction, wrong-owner,
wrong-session, wrong-request, phase-inconsistent, or cross-child admission
value is fail-closed before either `ADMIT` or target action.

## 4. B-M2 — exact descriptor, barrier, and phase contract

### 4.1 Exact child descriptor slots

`dup3` or an equivalent exact-FD operation places every present child
descriptor at the printed number.  Every present child descriptor has
`FD_CLOEXEC`; every unlisted number is closed before `SANITIZED`.

| Child FD | Slot | Exact object and lifetime |
|---:|---|---|
| 0 | `STDIN_EOF` | read end of a child-unique anonymous pipe; G closes the only writer before registration and retains its pre-close pipe device/inode receipt; the child observes EOF and closes FD 0 at target return |
| 1 | `STDOUT` | write end of a child-unique anonymous pipe; G alone holds the read end until both exact EOF drain and child reap complete, then closes it |
| 2 | `STDERR` | write end of a second child-unique anonymous pipe; G alone holds the read end until both exact EOF drain and child reap complete, then closes it |
| 3 | `SOURCE` | read-only regular-file FD for the exact byte-bound target source; the trusted loader reads and independently hashes all bytes, compiles only those bytes in memory, closes FD 3, and then emits `SOURCE_READY` |
| 4 | `RPC` | child endpoint of its unique `AF_UNIX SOCK_SEQPACKET` pair; G holds the sole peer from registration through terminal reply; the child closes FD 4 after that reply and before exit |
| 8 | `ADMISSION_BARRIER` | child endpoint of a child-unique `SOCK_SEQPACKET` pair; G holds the sole peer from first-instruction sanitization through `START`; the child end closes before the first target instruction, and G closes its peer when that closure is observed and before any later audit |
| 9 | `GENERATION_ROOT` | duplicate of the existing descriptor-relative generation-root capability; G retains the original; the child duplicate lives from registration through its last generator operation and closes before return |

The workers-cgroup placement FD is a trusted-stub transient.  The stub
closes it before `SANITIZED` and before `CHILD_REGISTERED`; it is forbidden
from every `FDSET`.  Pidfds, parent/root originals, stdout/stderr read ends,
RPC and barrier peers, namespace/cgroup FDs, package-lock sockets, lock
capabilities, and setup source FDs are G/P-held and forbidden in a child.

For FD 0, P validates the child's pipe against G's immutable receipt taken
before G closed the writer; no text claims that a closed writer remains
held.  For FDs 1, 2, 4, 8, and 9, P also validates the corresponding live
G-held peer or original.  A receipt cannot substitute for a peer/original
where the table requires one.

### 4.2 Exact source identities

The `SOURCE` slot maps only as follows:

| Exact target | Exact byte-bound source |
|---|---|
| `VERIFY_ONLY_GENERATOR` | registered `code/generate_controls.py` |
| `GENERATE_CANONICAL_A` | registered `code/generate_controls.py` |
| `GENERATE_CANONICAL_B` | registered `code/generate_controls.py` |
| `GENERATE_MUTATION` | registered `code/generate_controls.py` |
| `TOP_TEST_CONTROLS` | registered `code/test_controls.py` |
| `COPIED_REPRODUCE` | the copied package's `experiments/reproduce.sh`, after exact byte identity with the registered implementation source and marker-block validation |

No other target carries FD 3.  A path string is never source identity.  The
loader's complete-read SHA-256 must equal the already authenticated
implementation digest before compilation.  Failure closes the child and is
never permission to run remembered or path-reopened code.

### 4.3 Exact phase-indexed `FDSET` matrix

The amended closed `FDSET` enum is exactly:

```text
STDIO_BARRIER
STDIO_SOURCE_BARRIER
STDIO_SOURCE_ROOT_BARRIER
STDIO_SOURCE_RPC_BARRIER
```

| Exact `FDSET` | Exact targets | Registered / pre-admission | `SOURCE_READY` | Target running |
|---|---|---|---|---|
| `STDIO_BARRIER` | `CGROUP_PROBE_CHILD epoch=1`, `CGROUP_PROBE_CHILD epoch=2`, `LOCK_HOLDER`, `LOCK_CONTENDER`, `REPLACEMENT_ACTOR` | `{0,1,2,8}` | `{0,1,2,8}` | `{0,1,2}` |
| `STDIO_SOURCE_BARRIER` | `VERIFY_ONLY_GENERATOR` | `{0,1,2,3,8}` | `{0,1,2,8}` | `{0,1,2}` |
| `STDIO_SOURCE_ROOT_BARRIER` | `GENERATE_CANONICAL_A`, `GENERATE_CANONICAL_B`, `GENERATE_MUTATION` | `{0,1,2,3,8,9}` | `{0,1,2,8,9}` | `{0,1,2,9}` |
| `STDIO_SOURCE_RPC_BARRIER` | `TOP_TEST_CONTROLS`, `COPIED_REPRODUCE` | `{0,1,2,3,4,8}` | `{0,1,2,4,8}` | `{0,1,2,4}` |

These are the complete target/source/root/RPC combinations.  The mapping
does not vary by method metadata.  There is no optional descriptor,
role-union, wildcard, inherited fallback, or target identity beyond the
literal names above.

### 4.4 Exact child-barrier bytes

FD 8 carries exactly four possible seqpacket payloads:

```text
child -> G: SANITIZED
G -> child: ADMIT
child -> G: SOURCE_READY
G -> child: START
```

They are respectively the exact 9, 5, 12, and 5 ASCII bytes shown, with no
NUL, LF, length prefix, credential, rights, or other ancillary item.  Each
appears exactly once in printed order for every child.  A short, truncated,
extra, repeated, wrong-direction, or reordered packet is fatal.  The P--G
control connection remains separately length-framed; same-spelled record
types on the two channels are distinguished by channel and may not be
forwarded as raw packets.

### 4.5 Exact P--G source/start records

The P--G closed enum in amendment-v2 Section 5.3 is extended by these exact
records:

```text
SOURCE_READY session=DEC child=DEC admission=ADMISSION fdset=FDSET
START session=DEC child=DEC admission=ADMISSION
```

`SOURCE_READY` is G-to-P exactly once after G receives the child's fixed
`SOURCE_READY` packet and verifies the child remains blocked.  For a
source-bearing child it additionally requires FD 3 closed; for a no-source
child the trusted loader sends the packet without reading a source.  The
record repeats the registered session, child, admission, and `FDSET`.

`START` is P-to-G exactly once only after P's second independent actual
descriptor audit matches the `SOURCE_READY` column and all registered
identity, membership, cwd, credential, and thread facts still match.  It
repeats the registered session, child, and admission.  Only after receiving
this record may G send the child-barrier packet `START`.

### 4.6 Exact state and close transitions

Every orderly child follows exactly:

```text
CLONED_AT_BARRIER
  -> SANITIZED_REPORTED
  -> REGISTERED
  -> ADMITTED
  -> SOURCE_READY_REPORTED
  -> START_AUTHORIZED
  -> RUNNING
  -> TARGET_RETURNED
  -> REAPED
```

The expected epoch-two probe kill and every already frozen fatal/containment
termination instead take the existing v2 terminal edge

```text
any non-REAPED child state -- expected probe kill or fatal containment --> REAPED
```

That edge authorizes no target success or cleanup shortcut; kernel exit closes
the child's remaining FDs, and the same drain/reap/empty-process proof below
is still mandatory.

The transition actions are:

1. the first-instruction stub closes the workers-cgroup FD and every
   descriptor outside the registered row, establishes exact slots, sends
   `SANITIZED`, and waits;
2. G sends `CHILD_REGISTERED` and, for a creation-capable generator target,
   immediately sends Section 5's authorization while the child remains
   blocked; P performs its first audit, ACKs that authorization only after a
   pass, and sends `CHILD_ADMITTED`; G sends `ADMIT` only;
3. the loader reads/hashes/compiles the exact source if present, closes FD 3,
   sends `SOURCE_READY`, and waits without executing the target;
4. G sends the P--G `SOURCE_READY`; P performs its second audit and sends the
   P--G `START`; G sends the child `START`;
5. the child receives `START`, closes FD 8 before its first target
   instruction, and may then run the target; G observes that peer closure and
   closes its barrier peer, which must be gone before any later audit;
6. while the target runs, every later freeze/reference audit requires the
   exact running-column set; on an orderly path a creation-capable generator
   closes FD 9 after its final generator operation, and an RPC child closes
   FD 4 after its terminal reply; G services both nonblocking output-pipe
   read ends throughout target life so pipe capacity cannot become a return
   barrier;
7. on orderly target return the child closes 0, 1, and 2; on the already
   frozen fatal/kill path, process exit closes every surviving child FD
   instead.  G drains both pipes to EOF, reaps the child, verifies the process
   is gone and its descriptor set therefore exactly empty, then closes its
   read ends; and
8. only after both drain and reap may G send the existing
   `CHILD_REAPED` record.

An error before `START` executes no target.  An error after `START` follows
the already frozen cgroup containment and cleanup rules; it cannot skip a
descriptor or object-ledger barrier.

### 4.7 Independent P descriptor verification

At pre-admission, `SOURCE_READY`, and every later running/freeze reference
audit, P independently enumerates the exact initial-PID-namespace
`/proc/PID/fd` and `fdinfo` entries for the registered child.  It checks:

```text
exact descriptor-number set
object type and access mode
FD_CLOEXEC
device/inode for regular files, directories, and pipes
socket family/type and exact peer identity
cwd device/inode
the corresponding G-held peer/original or the exact FD-0 pre-close receipt
pidfd/start-time identity, credentials, one-thread status, and workers membership
```

P compares actual observations with the applicable literal matrix column,
not with G's assertion that an `FDSET` token is correct.  An inability to
inspect any required coordinate, `fdinfo` bit, peer, receipt, or original is
`E_POSSESSION_UNAVAILABLE` before target action or a fatal containment
failure afterward.  It is never permission to trust G, `FDSET`, or a copied
receipt.

## 5. B-M3 — creator-specific object-ledger ordering

### 5.1 Exact object state and acknowledgment

`OBJECT_REGISTERED` always names an object that already exists and whose
actual device/inode was obtained through a retained capability.  It is never
a promise about a future inode.  The six unchanged kinds are exactly:

```text
ROOT_PARENT
ROOT
ROOT_MEMBER
LOCK_PARENT
LOCK
LOCK_MEMBER
```

For each actual object, P's mirrored state is exactly:

```text
UNSEEN -> REGISTERED_PENDING_ACK -> ACKED -> RELEASED_TOMBSTONE
```

`ACKED` is exactly the v3 acknowledged form of the v2 LIVE registry state;
it is not a release or a new terminal outcome.

G-to-P registration retains its v2 payload:

```text
OBJECT_REGISTERED session=DEC handle=DEC kind=KIND dev=DEC ino=DEC
```

The new P-to-G acknowledgment is exactly:

```text
OBJECT_REGISTERED_ACK session=DEC handle=DEC kind=KIND dev=DEC ino=DEC
```

It occurs exactly once after, and repeats every field of, the matching
registration.  It cannot acknowledge an unseen, future, duplicate,
released, wrong-kind, wrong-session, wrong-handle, or mismatched identity.

For independent validation, G retains exactly one no-follow validation FD
for the object until acknowledgment.  P, using its already authenticated G
pidfd/start-time identity and initial-root proc authority, enumerates G's
actual descriptor table and requires exactly one such retained descriptor
with the reported type/device/inode and the registered handle/kind state.
For a member, G opens it only relative to the already retained parent/root
FD; for a directory, the retained operational directory FD is the validation
FD.  P does not open a private-mount pathname and does not merely echo G's
numbers.  Failure to inspect or uniquely match that FD is fatal.  G closes a
short-lived member validation FD only after ACK; long-lived parent/root/lock
FDs retain their existing v2 lifetime.

Every actual object retains one matching v2 `OBJECT_RELEASED` transition.
A parent/root release cannot release a member; one handle cannot release a
different `KIND`.  Released identities remain tombstones through the exact
v2 freeze/cleanup epoch.  Closing the short-lived validation FD after ACK
does not release the object or remove its LIVE registry entry.  That entry
persists through the later reference/cleanup proof; release occurs only
after the object's final cleanup validation FD is closed following unlink,
under the retained v2 owned-object-gone order.

### 5.2 G-created objects: mandatory pre-access order

For every G-created object, including each P25 `occupied`, lock `.owner`,
post-cache member, and controlled-foreign fixture represented by one of the
six kinds, the exact order is:

```text
create relative to a retained parent capability
-> fstat/fstatat the actual no-follow object
-> retain one validation FD
-> OBJECT_REGISTERED G-to-P
-> independent P validation
-> OBJECT_REGISTERED_ACK P-to-G
-> close a short-lived validation FD if applicable
-> permit first child access
```

`ROOT_PARENT` and `ROOT` are both ACKED before a generation authorization or
generator admission.  `LOCK_PARENT`, `LOCK`, and `LOCK_MEMBER` are ACKED
before `LOCK_BOUND`, `OWNED`, or any holder/contender access.  The direct
`.owner` FD remains open through ACK and then closes before the retained v2
`CREATED` receipt.  A G-created `ROOT_MEMBER` is separately ACKED before any
child sees its root.  There is no parent-wide implied member registration.

### 5.3 Generator creation authorization without a future inode

In Sections 5.3--5.6, a **creation-capable generator target** means exactly
`GENERATE_CANONICAL_A`, `GENERATE_CANONICAL_B`, or `GENERATE_MUTATION`.
`VERIFY_ONLY_GENERATOR` retains role `GENERATOR` for the B-M1 row but is a
noncreator: it has no FD 9, no member-creation authorization, and no
post-creator ledger.

For a creation-capable generator target, immediately after
`CHILD_REGISTERED` and while the child remains blocked, G sends exactly one:

```text
MEMBER_CREATE_AUTHORIZED session=DEC child=DEC root=DEC target=TARGET purpose=PURPOSE basename_set=GENERATED_NINE_V1 primitive=DIRFD_O_CREAT_O_EXCL_O_NOFOLLOW
```

P may receive that record while performing its first descriptor audit, but
cannot acknowledge it unless that audit has passed.  P then verifies that
the child, root handle, target, purpose, admission, FD 9, and already ACKED
`ROOT` identity are one exact authorized tuple and sends exactly one:

```text
MEMBER_CREATE_ACK session=DEC child=DEC root=DEC purpose=PURPOSE basename_set=GENERATED_NINE_V1
```

The first record is G-to-P and the second P-to-G.  Neither contains a member
device/inode, and neither is an `OBJECT_REGISTERED`.  A missing, duplicate,
future-child, post-admission, wrong-root, wrong-target, wrong-purpose,
wrong-basename-set, or wrong-primitive record prevents `CHILD_ADMITTED`.

`GENERATED_NINE_V1` expands only to this ordered list:

```text
valuation_normalization_controls.csv
exponent_order_branch_controls.csv
finite_kernel_truncation_controls.csv
torsion_closure_type_controls.csv
signature_nonpromotion_controls.csv
owner_firewall_controls.csv
proof_ceiling_controls.csv
target_summary.csv
manifest.json
```

The exact authorized target/purpose pairs are:

```text
GENERATE_CANONICAL_A / CANONICAL_A
GENERATE_CANONICAL_B / CANONICAL_B
GENERATE_MUTATION / MUTATION_P01_V1
GENERATE_MUTATION / MUTATION_P02_V1
GENERATE_MUTATION / MUTATION_P03_V1
GENERATE_MUTATION / MUTATION_P04_V1
GENERATE_MUTATION / MUTATION_P05_V1
GENERATE_MUTATION / MUTATION_P06_V1
GENERATE_MUTATION / MUTATION_P07_V1
GENERATE_MUTATION / MUTATION_P08_V1
GENERATE_MUTATION / MUTATION_P09_V1
GENERATE_MUTATION / MUTATION_P10_V1
GENERATE_MUTATION / MUTATION_P11_V1
GENERATE_MUTATION / MUTATION_P12_V1
GENERATE_MUTATION / MUTATION_P13_V1
GENERATE_MUTATION / MUTATION_P14_V1
GENERATE_MUTATION / MUTATION_P15_V1
GENERATE_MUTATION / MUTATION_P16_V1
GENERATE_MUTATION / MUTATION_P17_V1
GENERATE_MUTATION / MUTATION_P18_V1
GENERATE_MUTATION / MUTATION_P19_V1
GENERATE_MUTATION / MUTATION_P20_V1
GENERATE_MUTATION / MUTATION_P21_V1
GENERATE_MUTATION / MUTATION_P22_V1
GENERATE_MUTATION / MUTATION_P23_V1
GENERATE_MUTATION / MUTATION_P24_V1
GENERATE_MUTATION / MUTATION_P25_V1
GENERATE_MUTATION / MUTATION_P26_V1
GENERATE_MUTATION / MUTATION_P27_V1
GENERATE_MUTATION / MUTATION_P27_V2
GENERATE_MUTATION / MUTATION_P27_V3
GENERATE_MUTATION / MUTATION_P27_V4
GENERATE_MUTATION / MUTATION_P27_V5
GENERATE_MUTATION / MUTATION_P28_V1
GENERATE_MUTATION / MUTATION_P28_V2
```

This is a literal closed list, not a regular expression, range, future
purpose, or wildcard.  `VERIFY_ONLY_GENERATOR`, `TOP_TEST_CONTROLS`,
`COPIED_REPRODUCE`, a probe, holder, contender, or replacement actor receives
no member-creation authorization and may create none of the nine through a
generation-root FD.

The base generator creation semantics remain exactly descriptor-relative
`O_CREAT|O_EXCL|O_NOFOLLOW`.  The nine outputs are not precreated, their
source bytes and CLI semantics do not change, and authorization does not
assert that any future inode exists.

### 5.4 Exact post-creator ledger barrier

For every creation-capable generator child, the state is exactly:

```text
AUTH_ACKED
  -> CREATOR_RUNNING
  -> CREATOR_REAPED
  -> REAP_ACKED
  -> ENUMERATING
  -> ACTUAL_MEMBERS_ACKED
  -> LEDGER_CLOSE_PENDING
  -> LEDGER_ACKED
```

The mandatory order is:

1. G waitid-reaps the generator and sends the existing `CHILD_REAPED`.
   After accepting that exact record, P sends exactly one:

   ```text
   CHILD_REAPED_ACK session=DEC child=DEC status=DEC
   ```

   It is P-to-G and repeats every field of the matching reap record.  G
   performs no root enumeration until it receives this ACK.  A missing,
   duplicate, premature, wrong-status, wrong-child, or wrong-session ACK is
   fatal.
2. G enumerates only through its held root FD, with no pathname reopen or
   symlink following.  Filesystem enumeration order has no authority.  It
   first revalidates and partitions out the exact pre-creator, already ACKED
   G-created `ROOT_MEMBER` set by basename, kind, device/inode, and handle.
   That set is empty for canonical A/B and every mutation call except the
   exact nonempty P25 call; for that one call it is exactly the sole
   `occupied` receipt.  The empty P25 replacement subfixture also has an
   empty set.  Drift, absence, or any additional pre-creator member is
   containment failure.  G then calls the remaining typed map the
   creator-produced set,
   compares that set with the acknowledged purpose authorization and child
   status, and only then iterates the printed `GENERATED_NINE_V1` order.
3. For every actual authorized regular member in that canonical order, G
   obtains no-follow type/device/inode relative to root FD, opens and retains
   one validation FD, sends one `OBJECT_REGISTERED` with `kind=ROOT_MEMBER`,
   receives the matching `OBJECT_REGISTERED_ACK`, and then closes the
   validation FD.
4. After every actual authorized generated member is ACKED, G sends exactly
   one:

   ```text
   MEMBER_LEDGER_CLOSED session=DEC child=DEC root=DEC count=DEC
   ```

5. P compares `count` with its exact ACKED generated-member handles for that
   child/root and the accepted child status.  G's canonical set comparison,
   not a fabricated inode or a count-only success inference, determines and
   retains any missing authorized subset as failure.  P then sends exactly
   one:

   ```text
   MEMBER_LEDGER_ACK session=DEC child=DEC root=DEC count=DEC
   ```

`MEMBER_LEDGER_CLOSED` is G-to-P and `MEMBER_LEDGER_ACK` is P-to-G.  Both
repeat the same canonical fields.  Each occurs once after
`CHILD_REAPED_ACK` and all member ACKs, never before.  Only the ledger ACK
changes state to `LEDGER_ACKED`.

Before `LEDGER_ACKED`, no later child admission, replacement exchange,
cleanup request, no-reference/reference audit, member release, fixed-entry
check, or fixed-entry deletion is legal for that root.  This is a state
barrier, not an implementation note.

### 5.5 Success, P25, partial, and unexpected-member cases

On creation-capable generator success, the creator-produced set is exactly
`GENERATED_NINE_V1`, every member is ACKED in printed order, and the ledger
count is exactly `9`.

For the nonempty P25 call, G creates `occupied` first as an actual
`ROOT_MEMBER` with exact v1 metadata, registers it, and obtains
`OBJECT_REGISTERED_ACK` before admitting the `MUTATION_P25_V1` generator.
That generator still receives the exact nine-basename authorization so that
its permitted creation surface is closed, but it observes nonemptiness
before any create, returns `E_NONEMPTY_OUTPUT`, and creates zero generated
members.  After reap, the actual generated-member set is empty, the already
ACKED `occupied` is the sole root member, and the post-creator ledger count
is exactly `0`; `occupied` is not counted a second time.  The empty P25
replacement subfixture likewise precreates none of the nine outputs merely
to obtain an inode receipt.

On another failed or partial generation containing only validated authorized
regular members, G registers and obtains ACKs for every actual such member
in canonical order.  `count` is exactly that actual ACKED number; G's exact
set comparison retains any missing authorized subset, and P requires the
accepted non-success child status rather than inferring success from any
count or ACK ledger.  A nonempty missing subset necessarily has `count < 9`
and remains a failure; a failure after all nine exist likewise remains a
failure.  Ledger ACK permits only the already frozen failure/containment
cleanup path; it does not convert the generation to success.

An unexpected basename, unexpected type, symlink, special file, duplicate
identity, or object outside the authorization is containment failure.  It is
not registered, released, normalized, renamed, or deleted.  G sends no
`MEMBER_LEDGER_CLOSED`, P sends no ACK, ordinary reference audit and cleanup
remain prohibited, and the private namespace may only follow the existing
non-success containment/teardown path.  No unregistered object can be made
deletable by omitting it from a ledger.

### 5.6 Closed P--G enum and state guards

The v2 P--G closed record enum is amended only by adding:

```text
SOURCE_READY
START
CHILD_REAPED_ACK
OBJECT_REGISTERED_ACK
MEMBER_CREATE_AUTHORIZED
MEMBER_CREATE_ACK
MEMBER_LEDGER_CLOSED
MEMBER_LEDGER_ACK
```

The exact payloads, directions, cardinalities, and state guards are those in
Sections 4 and 5.  All retain the v2 four-byte big-endian length framing,
4096-byte ceiling, canonical ASCII, no trailing byte, and no ancillary item.
The sole ancillary-bearing P--G record remains `WORKERS_CGROUP_FD`.

The relevant exact ordering for a creation-capable generator is:

```text
SANITIZED child frame
CHILD_REGISTERED G-to-P
MEMBER_CREATE_AUTHORIZED G-to-P while child remains blocked
first P descriptor audit, with no audit-success message
MEMBER_CREATE_ACK P-to-G
CHILD_ADMITTED P-to-G
ADMIT child frame
source load and FD 3 close
SOURCE_READY child frame
SOURCE_READY G-to-P
second P descriptor audit
START P-to-G
START child frame and FD 8 close
generator O_CREAT|O_EXCL|O_NOFOLLOW operations
target return / descriptor closes / drain / reap
CHILD_REAPED G-to-P
CHILD_REAPED_ACK P-to-G
dirfd-relative set comparison and canonical registration/ACKs
MEMBER_LEDGER_CLOSED G-to-P
MEMBER_LEDGER_ACK P-to-G
later admission, audit, exchange, or cleanup
```

Any deviation is fatal.  The existing v2 cgroup freeze/kill/reap, foreign
preservation, retained-capability deletion, release-tombstone, no-false-
`ABSENT`, EOF, signal, and crash semantics remain binding after this added
ordering.

## 6. Required preservation of v2 closures

Nothing in Sections 3--5 changes or weakens:

1. `A-M1`: exact unparameterized `SG_SCOPE`, primitive-only class
   derivation, conclusion parsing after class derivation, expected class only
   after recomputation, and all four primitive counterfactuals;
2. `A-M2`: the recursive actual-filesystem receipt, all five live variants,
   and the two exact-one-coordinate mode/mtime comparator clones;
3. `A-M3`: the byte-bound embedded possession source, two namespace layers,
   atomic cgroup placement, root-owned freeze/kill controls, method
   freeze/no-reference and final kill/reap/populated-zero distinction,
   retained parent/root/lock capabilities, capability-relative member
   deletion, the seven old P19--P25 lifecycle classes, five controlled
   replacement subfixtures, foreign-object preservation, and the prohibition
   on false `ABSENT`; or
4. `A-M4`: manifest-first authentication of the complete review followed by
   independent capability-relative reads and hashes of every active
   amendment before lifecycle adjacency.

The new descriptor and object-ledger barriers strengthen the existing
freeze/reference proof; they do not replace cgroup quiescence, exclusive
private-mount possession, final reap, or release/owned-object-gone proofs.

## 7. Append-only v3 successor receipt while preserving A-M4

### 7.1 Historical and active block grammar

The complete current 74,876-byte review is immutable historical prefix
authority.  Its one existing block at lines 1400--1406 remains exactly:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v1]
count=2
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

It may not be edited, normalized, duplicated, or reinterpreted as the active
count-three list.  After this amendment is externally hashed, the fresh
independent reviewer must append exactly one successor block:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v2]
count=3
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=<exact externally computed final v3 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

There is no blank or commentary line inside either block.  The successor
tag version is exactly `v2`, not `v3`.

### 7.2 Exact verifier order

Before lifecycle adjacency, the final verifier must:

1. open the unchanged manifest-bound canonical review path once through the
   held package-root capability, require the same regular/nlink-one/no-link
   rules, hash the complete post-v3 review bytes from that FD, and require
   the manifest's exact complete-review digest;
2. parse only those same authenticated bytes and require exactly one
   historical `v1` begin/end pair whose complete block bytes equal Section
   7.1's first block, exactly one active `v2` begin/end pair with the second
   block's exact field grammar and order, and no other effective-amendment
   begin/end tag;
3. reject a missing, duplicate, reordered, malformed, nested,
   prefix-drifted, wrong-count, wrong-path, wrong-digest, unknown-index,
   extra-key, cross-version, or commentary-bearing block;
4. independently resolve the three active paths relative to the same held
   package-root capability with the existing v2 `openat2` beneath/no-link
   rules, require canonical regular nlink-one files, read every byte from
   each opened FD, and independently compute SHA-256; and
5. only after all three current-byte hashes match set the internal,
   nonserialized obligation
   `R.effective_amendments=[v1,v2,v3]` and permit lifecycle adjacency.

The historical v1 block is authenticated history but is not the active
dereference list.  The active ordered v2 block is the sole source of the
three paths and expected digests, never a digest oracle: every file is
opened and hashed independently.

This successor grammar remains internal to existing review node `R`.  It
adds no manifest key, authority binding, generated artifact, node, edge, or
topological-order change.

## 8. B-M1--B-M3 closure self-audit and authorization stop

| Finding | Design closure in this amendment | Frozen-surface effect | Self-result |
|---|---|---|---|
| `B-M1` | two exact operational owners; six single-cardinality session-zero target/role/purpose/admission rows; single-use method-child admission production bound to exact method/session/request/child; admission echoed both directions | no method, row, artifact, schema, or generated-byte change | CLOSED_BY_DESIGN |
| `B-M2` | exact slots 0/1/2/3/4/8/9; four literal FDSET rows; fixed SANITIZED/ADMIT/SOURCE_READY/START frames; separate P--G SOURCE_READY/START records; two independent P actual-table audits; exact close and post-reap rules | operational descriptors only; 173 methods and six paths unchanged | CLOSED_BY_DESIGN |
| `B-M3` | G-created pre-access registration plus P ACK; generator exact basename/purpose authorization without future inode; post-reap dirfd set comparison, canonical actual-member registration/ACK, and ledger-close ACK before any later access/audit/exchange/cleanup | generator bytes and O_CREAT/O_EXCL/O_NOFOLLOW semantics unchanged; P25 count zero excludes pre-ACKED occupied | CLOSED_BY_DESIGN |
| A-M4 successor | unique immutable historical v1 block plus unique active v2 count-three block; complete-review authentication and independent v1/v2/v3 reads/hashes before adjacency | 14 bindings, 8 nodes, 12 edges, schema/key set unchanged | CLOSED_BY_DESIGN |

```text
P15R_CONTROL_DESIGN_AMENDMENT_V3=FROZEN_CANDIDATE
BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
AMENDMENT_V2_SHA256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
CURRENT_FINAL_REVIEW_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
V3_REMEDIATION_GATE_SHA256=e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac

B_M1_OPERATIONAL_OWNER_ADDITIONS=2
B_M1_PRE_SUITE_AND_RUNNER_ROWS=6
B_M1_ADMISSION_REUSE_ALLOWED=false
B_M1_METHOD_OWNER_WILDCARD=false
B_M2_FDSET_VALUES=4
B_M2_CHILD_BARRIER_FRAMES=4
B_M2_P_DESCRIPTOR_AUDITS_BEFORE_START=2
B_M2_CHILD_ADMITTED_EXECUTES_TARGET=false
B_M2_POST_REAP_DESCRIPTOR_SET=EMPTY_PROCESS_GONE
B_M3_FUTURE_INODE_REGISTERED=false
B_M3_G_CREATED_PREACCESS_ACK=true
B_M3_GENERATOR_CREATE_AUTHORIZATION=true
B_M3_POST_CREATOR_REAP_ACK=true
B_M3_CANONICAL_SUCCESS_LEDGER_COUNT=9
B_M3_P25_GENERATED_LEDGER_COUNT=0
B_M3_UNEXPECTED_OBJECT_DELETION=false
A_M4_EFFECTIVE_AMENDMENTS=3
A_M4_INDEPENDENT_AMENDMENT_REHASH=true

A_M1_REGRESSION=RETAINED
A_M2_REGRESSION=RETAINED
A_M3_FOREIGN_DELETE_REGRESSION=RETAINED
A_M4_REGRESSION=RETAINED_WITH_VERSIONED_SUCCESSOR

IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS=9
CSV_BODY_ROWS=120
EXPLICIT_NEGATIVES=35
SEMANTIC_MUTATIONS=35
PACKAGE_MUTATIONS=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
MANIFEST_DAG_CHANGED=false

AMENDMENT_SELF_AUDIT=C0_M0_m0
INDEPENDENT_REREVIEW_REQUIRED=true
INDEPENDENT_PASS_CLAIMED=false

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

This self-audit is not the required fresh independent append-only re-review.
No control may be implemented or run, and no downstream authority changes,
until a separate reviewer reads and hashes the exact
`base + v1 + v2 + v3` tuple, regression-attacks all retained closures,
appends the authorized successor receipt and review, and independently
reaches `PASS C0/M0/m0`.
