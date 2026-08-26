# Replacement Paper 15 Phase-2 control-design remediation gate v3

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v3 — C0/M3/m0 OPEN**  
Version: `P15R-CONTROL-DESIGN-REMEDIATION-GATE-v3.0`  
Date: 2026-08-17 (Asia/Shanghai)

This is a design-remediation authorization, not a finding closure.  The three
major findings in the current final append-only review remain open.  This gate
authorizes exactly one design-only amendment and, only after that amendment is
frozen and externally hashed, one fresh independent append-only re-review.  It
authorizes no generator, verifier, test suite, README, CSV, manifest,
implementation, reproduction run, Route, composition, manuscript, figure,
release, archive, Git action, or public synchronization.

## 1. Exact authority and current verdict

The following six records were read on their complete current bytes and
independently re-hashed before this gate was written:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| design amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| remediation gate v2 | `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` |
| design amendment v2 | `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| current final append-only review | `notes/phase2_control_design_peer_review.md` | 1524 | 74876 | `ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725` |

The review's first 49,358 bytes independently hash to
`b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3`;
its first 22,894 bytes independently hash to
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.
The complete current effective verdict is **REVISE — C0/M3/m0**, with the
three open findings `B-M1`, `B-M2`, and `B-M3`.  No self-audit is evidence
against them.

The current review contains exactly one historical effective-amendment block,
at lines 1400--1406, with these exact bytes:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v1]
count=2
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

That block and all 74,876 current review bytes are immutable historical
prefix authority for the later append-only re-review.

The proof/source boundary is not reopened.  The theorem owner remains the
bare compact group `B_p`; universal recovery remains
`OPEN_NOT_AUTHORIZED`; Route B remains false.  This gate does not authorize a
theorem, source, owner, or publication-state change.

## 2. Sole amendment target, precedence, and bounded supersession

The target was absent before this gate was created.  Exactly one new design
file may be created:

```text
notes/phase2_control_design_amendment_v3.md
```

After that file is frozen and externally hashed, the effective design is
exactly

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + amendment v2 c1d104d2...
  + amendment v3 at its externally computed final digest.
```

Amendment v3 may supersede only the v2 clauses needed to close `B-M1`,
`B-M2`, and `B-M3`, plus the mechanical successor-receipt rule in Section 7
needed to byte-bind v3 without rewriting the append-only review.  Every
omitted base/v1/v2 clause remains binding.  The amendment must identify each
superseded clause and every operational record or enum change explicitly.
It must not embed its own digest, claim an independent closure, or authorize
implementation or execution.

## 3. B-M1 repair — closed pre-suite owner, role, and admission matrix

### 3.1 Exact operational owner additions

Amendment v3 must add exactly these two operational-only `OWNER` tokens:

```text
BOOTSTRAP_G
REPRO_COORDINATOR
```

They do not name unittest methods.  `BOOTSTRAP_G` owns exactly the two
G-created cgroup-preflight micro-stubs below.  `REPRO_COORDINATOR` owns
exactly the checked-in verify-only generator and canonical A/B generators.
The existing `SUITE_173` token remains reserved for exactly one actual
`TOP_TEST_CONTROLS` child.  Every later method-owned child remains owned by
the exact one of the already frozen 173 method names that authorized its
session/request.  Neither new token may own a method child, and no method
token may own a bootstrap, ordinary pre-suite, or top-runner child.

### 3.2 Exact target/phase table

The complete G-child sequence through creation of the suite runner is:

| Order/phase | Exact target identity | Session | `OWNER` | `ROLE` | `PURPOSE` | Exact admission token | Cardinality |
|---:|---|---:|---|---|---|---|---:|
| 1, `CGROUP_PREFLIGHT_E1` | `CGROUP_PROBE_CHILD epoch=1` | `0` | `BOOTSTRAP_G` | `PROBE` | `NONE` | `BOOTSTRAP_FREEZE_THAW_E1` | 1 |
| 2, `CGROUP_PREFLIGHT_E2` | `CGROUP_PROBE_CHILD epoch=2` | `0` | `BOOTSTRAP_G` | `PROBE` | `NONE` | `BOOTSTRAP_KILL_E2` | 1 |
| 3, `PRE_SUITE_VERIFY` | `VERIFY_ONLY_GENERATOR` | `0` | `REPRO_COORDINATOR` | `GENERATOR` | `NONE` | `PRE_SUITE_VERIFY_ONLY` | 1 |
| 4, `PRE_SUITE_A` | `GENERATE_CANONICAL_A` | `0` | `REPRO_COORDINATOR` | `GENERATOR` | `CANONICAL_A` | `PRE_SUITE_CANONICAL_A` | 1 |
| 5, `PRE_SUITE_B` | `GENERATE_CANONICAL_B` | `0` | `REPRO_COORDINATOR` | `GENERATOR` | `CANONICAL_B` | `PRE_SUITE_CANONICAL_B` | 1 |
| 6, `SUITE_ENTRY` | `TOP_TEST_CONTROLS` | `0` | `SUITE_173` | `TOP_TEST_RUNNER` | `NONE` | `SUITE_173_TOP_RUNNER` | 1 |

There is no other G child before `TOP_TEST_CONTROLS`.  L, G itself, and P's
initial-namespace privilege probe are not G children and retain their exact
v2 bootstrap records; they may not consume any token in this table.  All six
bootstrap/pre-suite/top-runner rows use the already reserved top-level
session `0`; no row may allocate a method-session handle before
`SUITE_ENTRY`.  The two cgroup probes retain their exact epoch-specific
freeze/thaw and kill
semantics.  Each probe must additionally use the same exact
`CHILD_REGISTERED -> CHILD_ADMITTED` framing below before its barrier is
released; its epoch-specific `CGROUP_PROBE_*` records follow that admission
and remain distinct.  No alternative bootstrap-only implicit registration is
legal.

Every registered child must bind the admission value in both directions.
The amended canonical record shapes must be exactly

```text
CHILD_REGISTERED session=DEC child=DEC inner_pid=DEC
    role=ROLE owner=OWNER purpose=PURPOSE admission=ADMISSION fdset=FDSET
    cwd_dev=DEC cwd_ino=DEC
CHILD_ADMITTED session=DEC child=DEC admission=ADMISSION
```

Continuation indentation is presentational only; each payload remains one
canonical ASCII line.  The field order above is mandatory.  A missing,
unknown, repeated, phase-inconsistent, wrong-direction, or cross-child
admission token is fail-closed before the child barrier is released.

After `SUITE_ENTRY`, the existing method/session rules remain exact: an RPC
request names one of the frozen 173 methods, the registered child's `OWNER`
must equal that same method name, and its target/purpose must be authorized by
that method's existing closed session.  There is no wildcard owner, no
"current method" default, and no widening of the 173-method ownership set.

## 4. B-M2 repair — exact admission barrier and descriptor tables

### 4.1 Descriptor slots and owners

Amendment v3 must supersede the four undefined v2 `FDSET` tokens with the
following exact semantic slots.  `dup3` or an equivalent exact-FD operation
must place each child descriptor at its printed number; every present child
descriptor has `FD_CLOEXEC`, and every unlisted number is closed before the
child announces that it is sanitized.

| Child FD | Slot | Exact object and holder/lifetime contract |
|---:|---|---|
| 0 | `STDIN_EOF` | read end of a private anonymous pipe whose writer G closes before registration; child observes EOF; child closes it at target return |
| 1 | `STDOUT` | write end of a child-unique anonymous pipe; G alone holds the read end through drain and reap; child closes on target return |
| 2 | `STDERR` | write end of a second child-unique anonymous pipe; G alone holds the read end through drain and reap; child closes on target return |
| 3 | `SOURCE` | read-only regular-file FD for the exact byte-bound target source; the trusted loader reads, independently hashes, and compiles those exact bytes to the in-memory target before closing it and before `SOURCE_READY`; G/P never treat its path string as identity |
| 4 | `RPC` | child endpoint of its unique `AF_UNIX SOCK_SEQPACKET` pair; G holds the sole peer; it lives from registration through the terminal reply and closes before child exit |
| 8 | `ADMISSION_BARRIER` | child endpoint of a child-unique `SOCK_SEQPACKET` pair; G holds the sole peer; it exists only from first-instruction sanitization through the exact `START` transition, then both ends close |
| 9 | `GENERATION_ROOT` | the existing descriptor-relative generation-root duplicate; G retains the original root capability; the child duplicate lives from registration through generator return and closes before exit |

The workers-cgroup placement FD is a trusted-stub transient.  The stub must
close it before announcing sanitization and before `CHILD_REGISTERED`; it is
therefore forbidden from every table below.  Pidfds, parent/root originals,
pipe read ends, RPC peers, namespace/cgroup FDs, package-lock sockets, and
lock capabilities are G/P-held objects and are forbidden in the child table.

### 4.2 Exact phase-indexed `FDSET` matrix

The amended closed `FDSET` enum is exactly

```text
STDIO_BARRIER
STDIO_SOURCE_BARRIER
STDIO_SOURCE_ROOT_BARRIER
STDIO_SOURCE_RPC_BARRIER
```

The complete mapping is:

| Exact `FDSET` | Exact target(s) | Registered/pre-admission FDs | `SOURCE_READY` FDs | Target-running FDs |
|---|---|---|---|---|
| `STDIO_BARRIER` | `CGROUP_PROBE_CHILD epoch=1`, `CGROUP_PROBE_CHILD epoch=2`, `LOCK_HOLDER`, `LOCK_CONTENDER`, `REPLACEMENT_ACTOR` | `{0,1,2,8}` | `{0,1,2,8}` | `{0,1,2}` |
| `STDIO_SOURCE_BARRIER` | `VERIFY_ONLY_GENERATOR` | `{0,1,2,3,8}` | `{0,1,2,8}` | `{0,1,2}` |
| `STDIO_SOURCE_ROOT_BARRIER` | `GENERATE_CANONICAL_A`, `GENERATE_CANONICAL_B`, `GENERATE_MUTATION` | `{0,1,2,3,8,9}` | `{0,1,2,8,9}` | `{0,1,2,9}` |
| `STDIO_SOURCE_RPC_BARRIER` | `TOP_TEST_CONTROLS`, `COPIED_REPRODUCE` | `{0,1,2,3,4,8}` | `{0,1,2,4,8}` | `{0,1,2,4}` |

These are the complete source/root/RPC combinations; there is no wildcard,
implicit auxiliary FD, optional descriptor, inherited fallback, or
role-based union.  One token maps to exactly one printed row, and the mapping
may not vary by method metadata.  No target identity other than the exact
names in this table is legal.

### 4.3 Two-stage admission and independent P verification

The barrier protocol is exactly:

1. The first-instruction stub closes the workers-cgroup FD and every
   descriptor outside its registered-row set, establishes the exact numeric
   slots, sends the fixed barrier frame `SANITIZED`, and waits on FD 8.
2. G sends `CHILD_REGISTERED` only after `SANITIZED`.  P independently
   enumerates the child's actual `/proc/PID/fd` and `fdinfo` table, checks
   each number, object type, access mode, `FD_CLOEXEC`, device/inode or socket
   identity, cwd, and the corresponding G-held peer/original, and compares
   the result with the exact pre-admission row rather than trusting `FDSET`.
3. Only a match permits P to send `CHILD_ADMITTED` with the same admission
   token.  G sends the fixed barrier frame `ADMIT`.
4. A source-bearing child's trusted loader reads and independently hashes all
   source bytes, compiles only those exact bytes to its in-memory target,
   closes FD 3, and sends `SOURCE_READY`; a no-source child sends
   `SOURCE_READY` without a source read.  No compiled target instruction has
   run yet, and the child remains blocked on FD 8.
5. G reports that phase to P.  P independently enumerates the actual table
   again and requires the exact middle-column set.  Only that match permits
   the fixed `START` record.  The child receives `START`, closes FD 8 before
   the first target instruction, and only then performs target action.
6. G observes closure of the barrier peer and closes its end.  During target
   life, P's later freeze/reference audits require exactly the running-column
   set for the registered target.  A generator closes FD 9 after its last
   generator operation; an RPC child closes FD 4 after its terminal reply;
   every child closes 0/1/2 before exit.  G drains/closes its peers and pipes,
   reaps the child, and only then may send `CHILD_REAPED`.  The post-reap
   child descriptor set is exactly empty because the process no longer
   exists.

Amendment v3 must freeze the exact P--G record names, directions, field order,
and state transitions needed for `SOURCE_READY` and `START`; it may not leave
them as an implementation note.  Any inability to independently inspect a
descriptor coordinate or peer identity is `E_POSSESSION_UNAVAILABLE` before
target action, not permission to trust G or the FDSET token.

## 5. B-M3 repair — creator-specific object-ledger ordering

### 5.1 Existing-object registration rule

`OBJECT_REGISTERED` always means an object already exists and its actual
device/inode receipt was obtained through a retained capability.  It must
never be used as a promise about an inode that does not yet exist.

For every G-created object of the six existing kinds

```text
ROOT_PARENT ROOT ROOT_MEMBER LOCK_PARENT LOCK LOCK_MEMBER
```

the exact order is: G creates the object relative to its retained parent
capability; G `fstat`/`fstatat`s the actual object; G sends one
`OBJECT_REGISTERED`; P independently validates and acknowledges that exact
kind/handle/device/inode; only then may any child be admitted to access that
object.  This covers the P25 `occupied` member, lock `.owner`, post-cache and
controlled-foreign fixtures whenever they use one of the six kinds.  Each
actual member retains one matching `OBJECT_RELEASED`; a parent/root receipt
cannot release a member.

P's acknowledgment is a new internal record with exactly the existing
registration identity, in this order:

```text
OBJECT_REGISTERED_ACK session=DEC handle=DEC kind=KIND dev=DEC ino=DEC
```

It is P-to-G, occurs exactly once after the matching G-to-P
`OBJECT_REGISTERED`, and cannot acknowledge a future, duplicate, or
mismatched identity.

### 5.2 Generator creation authorization is not inode registration

Before admitting a generator, G must send and P must acknowledge one
operational-only creation authorization binding

```text
session, child, root handle, exact target, exact purpose,
ordered authorized basenames,
required creation primitive=dirfd-relative O_CREAT|O_EXCL|O_NOFOLLOW.
```

The wire form is exactly

```text
MEMBER_CREATE_AUTHORIZED session=DEC child=DEC root=DEC target=TARGET
    purpose=PURPOSE basename_set=GENERATED_NINE_V1
    primitive=DIRFD_O_CREAT_O_EXCL_O_NOFOLLOW
MEMBER_CREATE_ACK session=DEC child=DEC root=DEC purpose=PURPOSE
    basename_set=GENERATED_NINE_V1
```

Continuation indentation is presentational only.  The authorization is
G-to-P and its acknowledgment P-to-G; each occurs exactly once before the
matching generator's `CHILD_ADMITTED`.  `GENERATED_NINE_V1` expands only to
the ordered list printed below.

This authorization contains no member device or inode and is never called
`OBJECT_REGISTERED`.  For `GENERATE_CANONICAL_A`,
`GENERATE_CANONICAL_B`, and every enumerated `GENERATE_MUTATION` purpose, the
ordered authorized basename list is exactly:

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

The purpose domain remains the exact finite v1/v2 domain:

```text
CANONICAL_A
CANONICAL_B
MUTATION_P01_V1
MUTATION_P02_V1
MUTATION_P03_V1
MUTATION_P04_V1
MUTATION_P05_V1
MUTATION_P06_V1
MUTATION_P07_V1
MUTATION_P08_V1
MUTATION_P09_V1
MUTATION_P10_V1
MUTATION_P11_V1
MUTATION_P12_V1
MUTATION_P13_V1
MUTATION_P14_V1
MUTATION_P15_V1
MUTATION_P16_V1
MUTATION_P17_V1
MUTATION_P18_V1
MUTATION_P19_V1
MUTATION_P20_V1
MUTATION_P21_V1
MUTATION_P22_V1
MUTATION_P23_V1
MUTATION_P24_V1
MUTATION_P25_V1
MUTATION_P26_V1
MUTATION_P27_V1
MUTATION_P27_V2
MUTATION_P27_V3
MUTATION_P27_V4
MUTATION_P27_V5
MUTATION_P28_V1
MUTATION_P28_V2
```

This is a literal closed list, not a runtime regular expression, future
purpose, or wildcard.  A verify-only, top-runner, copied-wrapper, lock,
contender, replacement, or bootstrap target has no generation authorization
and may create none of the nine members through a generation-root FD.

For the nonempty P25 call, `occupied` is a G-created `ROOT_MEMBER`: it must
be actually registered and acknowledged before the generator is admitted.
The generator retains purpose `MUTATION_P25_V1`, observes nonemptiness before
any create, emits `E_NONEMPTY_OUTPUT`, and creates zero members.  The empty
P25 replacement subfixture likewise does not precreate any of the nine
generator outputs merely to obtain future inode receipts.

### 5.3 Post-creator registration barrier

After any generator child exits, the following order is mandatory:

1. G waitid-reaps it and P accepts the exact `CHILD_REAPED` receipt.
2. G enumerates the held root FD dirfd-relative, without a pathname reopen or
   symlink following, and compares the actual basename set with the
   acknowledged purpose authorization.
3. On generator success, the actual set must be exactly the nine names in the
   printed order.  On expected P25 nonempty rejection, the created set must
   be empty and the separately registered `occupied` must remain the sole
   member.  On any other failed/partial generation, G registers every actual
   authorized member it can validate, reports the missing subset as failure,
   and treats an unexpected name/type as containment failure; it does not
   invent an identity or delete an unregistered unexpected object.
4. For each actual generated member, G obtains type/device/inode through the
   retained root FD, sends one `OBJECT_REGISTERED` in canonical basename
   order, and receives P's independent acknowledgment.  Only after the full
   actual set is acknowledged may G send
   `MEMBER_LEDGER_CLOSED session=DEC child=DEC root=DEC count=DEC`; P checks
   the exact acknowledged identities and replies once with the same fields
   under `MEMBER_LEDGER_ACK`.  Only that reply closes the post-creator ledger.
5. No replacement exchange, cleanup request, no-reference/reference audit,
   later child admission, member release, or fixed-entry deletion may begin
   before that ledger-close point.  Thereafter every post-creator child
   access is subject to the ordinary pre-access registration rule.

The creating generator is the sole bounded exception to actual-inode
pre-registration, because its authorized inode does not exist until its
`O_CREAT|O_EXCL` succeeds.  This exception is authorization by exact
basename/purpose/parent capability, not a claim that the future inode was
registered.  Amendment v3 may add the required operational authorization and
acknowledgment records, but must freeze their exact payloads, directions,
cardinality, and state guards.  It may not precreate the nine outputs, change
their creation flags, alter generator bytes, or otherwise change the base
generator's byte semantics.

## 6. Required preservation of v2 closures

Amendment v3 must retain, without weakening:

1. `A-M1`: exact unparameterized `SG_SCOPE`, primitive-only class derivation,
   expected class after computation, and all four primitive counterfactuals;
2. `A-M2`: the real-filesystem receipt variants and the two actual-receipt
   exact-one-coordinate mode/mtime comparator clones;
3. the original `A-M3` closure: private possession, cgroup
   freeze/kill/reap/reference boundaries, retained parent/child capabilities,
   capability-relative member deletion, five controlled replacements,
   foreign-object preservation, and no false `ABSENT`; and
4. `A-M4`: manifest-bound final-review authentication followed by independent
   amendment-path reads and hashes before lifecycle adjacency.

The fresh re-review must regression-attack all four closures.  A v3 clause
which makes one of them ambiguous is a new open major finding, not an
acceptable trade for one of `B-M1..B-M3`.

## 7. Append-only v3 amendment receipt while preserving A-M4

The current count-two `v1` block in Section 1 cannot be edited and cannot be
duplicated.  To byte-bind amendment v3 without violating append-only history,
amendment v3 must minimally version the internal review-node dereference
grammar.  The later fresh review must append exactly one successor block:

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

The manifest-bound final verifier must authenticate the complete post-v3
review first.  From those same bytes it must require exactly one historical
`v1` block equal byte-for-byte to Section 1, exactly one active `v2` block in
the form above, and no other effective-amendment begin/end tag.  It must
reject a missing, duplicate, reordered, malformed, prefix-drifted, or
cross-version entry.  It then independently opens and hashes v1, v2, and v3
at the three active-block paths; only the active ordered list
`R.effective_amendments=[v1,v2,v3]` may satisfy lifecycle adjacency.

This is a versioned append-only extension of the already closed A-M4
dereference, not a new manifest surface.  It changes no manifest key/schema,
authority binding, generated artifact, lifecycle node, edge, or topological
order.

## 8. Frozen invariants

Amendment v3 and its re-review must preserve exactly:

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

The six implementation paths, eight CSV paths and headers, all row values
and row order, nine generated paths, fourteen authority paths, manifest key
set, all 35 S-method names, all 28 P-method names, all 173 method names, and
the printed graph `A,D,R,G,I,C,M,V` with twelve edges remain unchanged.
Operational owner/admission/FD/ledger records are nonserialized and add no
CSV, manifest member, method, binding, node, or edge.

If any repair requires a schema, count, generated byte, implementation path,
public detector/exit class, theorem owner, Route, or publication-boundary
change, amendment v3 must stop and report a new design finding rather than
silently widen scope.

## 9. Mandatory fresh append-only independent re-review

Only after amendment v3 is frozen and externally hashed may an independent
reviewer append to

```text
notes/phase2_control_design_peer_review.md
```

The complete current 74,876-byte / 1,524-line file at SHA-256
`ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725`
must remain the exact prefix.  This necessarily preserves the nested 49,358-
and 22,894-byte prefixes and the exact historical v1 amendment block.

The reviewer must independently read and hash the complete
`base + v1 + v2 + v3` tuple and attack, rather than restate:

1. every target/phase owner, role, admission value and its cardinality,
   including the two bootstrap probes, verify-only, canonical A/B, and the
   separately identifiable top test runner;
2. every exact pre-admission, source-ready, running, close, and post-reap
   descriptor set, including P's independent actual-table verification and
   all source/root/RPC combinations;
3. every G-created pre-access registration and every generator authorization,
   reap, dirfd-relative enumeration, actual-member registration/ack, later-
   admission, reference-audit, exchange, cleanup, and release ordering;
4. the P25 `occupied` exception and failed/partial generation behavior,
   including proof that no future inode is claimed before creation and no
   base generator byte semantics changed;
5. regression of all four v2 closures in Section 6; and
6. preservation of the exact old v1 block, unique active v2 count-three
   block, and independent current-byte reads/hashes of all three amendments.

The reviewer may close findings only from its own evidence.  Only a final
effective verdict `PASS C0/M0/m0` can support consideration of a later
implementation gate.  A partial repair, self-audit, copied enum, or unchanged
counterexample remains `REVISE`.

## 10. Authorization matrix

```text
P15R_CONTROL_DESIGN_REMEDIATION_GATE_V3=PASS_TO_ONE_AMENDMENT_V3
CURRENT_OPEN_FINDINGS=C0_M3_m0
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v3.md
AMENDMENT_V3_WRITE_AUTHORIZED=true

FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true
REREVIEW_PATH=notes/phase2_control_design_peer_review.md
REREVIEW_AUTHORIZED_ONLY_AFTER_AMENDMENT_V3_FROZEN=true
CURRENT_REVIEW_PREFIX_SHA256=ae201960c8994f935ab1347afc41f30066742cf65c4f605f4ddcf4d010446725
CURRENT_REVIEW_PREFIX_LINES=1524
CURRENT_REVIEW_PREFIX_BYTES=74876

BASE_COUNTS_MUST_REMAIN_UNCHANGED=true
SIX_IMPLEMENTATION_PATHS_MUST_REMAIN_UNCHANGED=true
MANIFEST_SCHEMA_MUST_REMAIN_UNCHANGED=true
AUTHORITY_BINDING_COUNT_MUST_REMAIN_14=true
PRINTED_DAG_MUST_REMAIN_8_NODES_12_EDGES=true
V2_CLOSURES_MUST_NOT_REGRESS=true
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

This gate does not embed its own SHA-256.  Amendment v3 and the later fresh
independent re-review must bind this file's externally computed final digest.
No finding is closed by this authorization.
