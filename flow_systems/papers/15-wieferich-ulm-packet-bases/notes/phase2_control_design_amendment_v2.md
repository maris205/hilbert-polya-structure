# Replacement Paper 15 deterministic-control design amendment v2

Status: **FROZEN AMENDMENT CANDIDATE — A-M1--A-M4 CLOSED BY DESIGN / INDEPENDENT EXACT-BYTE RE-REVIEW REQUIRED**  
Version: `P15R-CONTROLS-AMENDMENT-v2.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Amendment self-audit: **C0/M0/m0 against the four remanded findings; not an independent PASS**  
Control implementation or execution performed here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS experiment-agent, reproducibility and integrity protocols,
  plus academic-paper-reviewer methodology, domain, and devil's-advocate roles
- Origin Mode: plan / deterministic exact-arithmetic control-design amendment
- Origin Date: 2026-08-16
- Verification Status: UNVERIFIED_PENDING_INDEPENDENT_REREVIEW
- Version Label: `p15r_control_design_amendment_v2`
- Scope: only the four final-review findings `A-M1`, `A-M2`, `A-M3`, and
  `A-M4`; no generator, verifier, test, result, theorem, Route, manuscript,
  release, or publication claim

## 1. Exact authority, precedence, and bounded supersession

### 1.1 Complete current-byte authority

The complete bytes of all five design records below were read and
independently re-hashed before this amendment was written:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| remediation gate v1 | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |
| design amendment v1 | `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| final append-only review through v1 closure | `notes/phase2_control_design_peer_review.md` | 1017 | 49358 | `b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3` |
| remediation gate v2 | `notes/phase2_control_design_remediation_gate_v2.md` | 405 | 20113 | `00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705` |

The review's original 22,894-byte / 488-line prefix remains exactly
`3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec`.
Its current effective final verdict is `REVISE_C0_M4_m0`.  Neither the v1
amendment self-audit nor this amendment's self-audit is evidence against that
verdict.

The proof/source ceiling remains byte-bound, not reopened:

| Boundary authority | Package-relative path | SHA-256 | State |
|---|---|---|---|
| Phase-1 source/precedent audit | `notes/phase1_source_precedent_audit.md` | `287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97` | final source closure `PASS C0/M0/m0` |
| integrated Phase-1 proof gate | `notes/phase1_final_gate.md` | `949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd` | proof authorization only |
| Phase-2 symbolic proof | `notes/phase2_wieferich_ulm_proofs.md` | `7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355` | proof self-verdict `PASS C0/M0/m0` |
| independent proof review | `notes/phase2_wieferich_ulm_peer_review.md` | `2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7` | `PASS C0/M0/m0`; Full Paper plausible |
| post-proof control-design gate | `notes/phase2_control_design_gate.md` | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | design authority only |

The theorem owner is still the bare compact group `B_p`; universal prime
recovery is still `OPEN_NOT_AUTHORIZED`; Route B is still false.

### 1.2 Effective tuple and exact supersessions

After this file is externally hashed, the effective design is exactly

```text
base design db590ae2...
  + amendment v1 cd0b4ab2...
  + this amendment v2 at its externally computed final digest.
```

This amendment does not embed or predict its own digest.  It supersedes only:

1. for `A-M1`, amendment-v1 Section 4.5's ambiguous callable interface and
   the predicate cells for `S14..S17` in amendment-v1 Section 6; the remaining
   35-chain protocol and every other registry entry remain binding;
2. for `A-M2`, only the claim in amendment-v1 Section 8.2 that the live
   mode/mtime filesystem actions independently falsify omitted comparison of
   those coordinates; all receipt collection and all five live variants
   remain binding;
3. for `A-M3`, amendment-v1 Sections 9.1--9.3 only as to capability creator,
   retained lifetime, and cleanup, and Sections 10--11 as to pathname lock,
   candidate directory, acquisition helper, trap, deletion, and replacement
   injections, plus amendment-v1 Section 12 items 1, 3, 4, and 6 only as to
   their creator/trap/cleanup actor; the unchanged ten-step lifecycle order,
   Section-12 items 2 and 5, generator CLI, purpose grammar, validation-before-
   emptiness rule, descriptor-relative writes, P25 content, and canonical/
   mutation separation remain binding except where explicitly restated below;
4. for `A-M4`, amendment-v1 Section 1's unsupported transitive-authentication
   assertion; it is replaced by the mandatory dereference in Section 6 below.

Every omitted base-design and amendment-v1 clause remains binding.  No row,
CSV cell, schema, generated path, implementation path, authority path,
method name, registered S/P detector, theorem owner, Route boundary, or
printed graph edge is otherwise changed.

## 2. Frozen invariants retained exactly

```text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
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
TOLERANCE_POLICY=EXACT_ZERO
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
CONCURRENT_PROOF_HASH_CYCLE=false
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
```

The eight CSV paths and headers, all 120 body rows and their order, all 35
negative rows, all 35 `S` methods, all 28 `P` methods, all 173 method names,
the nine generated paths, the six implementation paths, the fourteen
authority paths, the manifest key set and schema, and the exact lifecycle
order `A,D,R,G,I,C,M,V` remain unchanged.

## 3. A-M1 — exact unparameterized `SG_SCOPE`

### 3.1 Callable identity and forbidden inputs

For all four existing methods `S14`, `S15`, `S16`, and `S17`, the complete
predicate symbol and dispatch identity is exactly

```text
SG_SCOPE
```

There is no class parameter, supplied-class argument, dispatch suffix,
closure variable, registry-selected branch, method annotation, or metadata
field.  In particular, the four amendment-v1 spellings beginning
`SG_SCOPE(` are invalid and are superseded.

`SG_SCOPE` receives one independently reparsed typed projection.  These
values are forbidden as decision inputs: `row_id`, `row_kind`, `case_kind`,
`mutation_id`, `negative_reason`, `oracle`, `status`, `scope_ceiling`, the
method-owned expected class, the method-owned expected detector, every prior
receipt, and every persisted PASS/rejection value.  Persisted
`kappa_prefix_p`, `kappa_prefix_q`, and a persisted witness are assertions to
be checked after primitive recomputation, never roots of trust.

### 3.2 Exact primitive projections

The decision projection for each existing method is frozen as follows:

| Method | Typed primitive decision projection | Post-recompute assertions excluded from the decision |
|---|---|---|
| `S14` | `PAIR{p:prime,q:prime,coordinates:ordered_distinct_prime_vector,proposed_conclusion:opaque_ascii_bytes}` | the two persisted prefix vectors, empty persisted coordinate, expected class/detector |
| `S15` | `PAIR_WITNESS{p:prime,q:prime,coordinates:ordered_distinct_prime_vector,distinguishing_coordinate:prime,proposed_conclusion:opaque_ascii_bytes}` | the two persisted prefix vectors, expected class/detector |
| `S16` | `FINITE_REGISTRY{registry:ordered_distinct_prime_vector,proposed_conclusion:opaque_ascii_bytes}` | any persisted matrix/range receipt and expected class/detector |
| `S17` | `OPEN_REGISTRY{registry:ordered_distinct_prime_vector,typed_infinite_witness:ABSENT_BY_SCHEMA,proposed_conclusion:opaque_ascii_bytes}` | expected class/detector and every open-state receipt |

For these four frozen seeds the vectors are respectively the existing
`[2;3;5;7;11;13]`, `[2;3;5;7;11;13]`,
`[2;3;5;7;11;13]`, and `[]`.  The CSV header and bytes do not change:
`prime_prefix` supplies `coordinates` or `registry`; the persisted prefix
columns remain receipt columns; the schema has no infinite-witness field, so
`ABSENT_BY_SCHEMA` is a parser fact and not method metadata.

For every primitive prime `p` and coordinate prime `r`, `SG_SCOPE`
independently computes

```text
r=p:          kappa_r(p)=0
r odd, r!=p:  kappa_r(p)=v_r(p^(r-1)-1)-1
r=2, p odd:   kappa_2(p)=v_2(p^2-1)-3.
```

Valuation is repeated exact integer division.  No `VC` row, saved prefix,
summary, or generator helper supplies a value.

### 3.3 Single ordered algorithm and derived-class rules

Each call performs exactly this order:

1. parse only the projection container and its primitive prime, vector,
   coordinate, and `ABSENT_BY_SCHEMA` fields; reject a composite/nonprime,
   duplicate coordinate, malformed vector, or noncanonical primitive scalar,
   but retain `proposed_conclusion` as opaque ASCII bytes and neither parse
   nor validate its grammar yet;
2. recompute every required `kappa_r(p)` from the primitive primes and the
   three formulas above;
3. for a pair, construct both recomputed prefixes in coordinate order;
4. for `PAIR_WITNESS`, require the claimed coordinate to occur exactly once
   and require the two recomputed values there to differ; an invalid claimed
   coordinate rejects before any expected-class comparison;
5. derive exactly one class by the four rules below;
6. only now parse the opaque proposed-conclusion bytes into its scope, named
   primes, coordinate, and quantifier; reject a malformed/noncanonical AST,
   otherwise decide whether the already derived class licenses it;
7. on a substantive conclusion rejection, return the typed failure derived
   from the parsed conclusion and recomputed class;
8. return the class, conclusion verdict, typed failure or acceptance, and
   the independently recomputed receipt values to the method without reading
   any expected value;
9. only after steps 1--8 may the method compare any persisted prefix/witness
   receipt with the returned recomputation; a stale receipt is a
   post-computation assertion failure and cannot select or alter the class;
10. only after those computations may the method compare the returned class
   with its method-owned expected-class assertion; and
11. only after substantive rejection may it translate the typed failure to
    the existing detector and compare that detector with the method-owned
    expected detector.

The class rules are exactly

```text
recomputed equal prefixes for one named pair         -> FINITE_COLLISION
recomputed unequal prefixes with a valid coordinate  -> FINITE_PAIR_SEPARATION
recomputed finite matrix over a nonempty registry    -> FINITE_RANGE
empty finite registry and no typed infinite witness  -> NO_INFINITE_EVIDENCE
```

The `FINITE_REGISTRY` matrix uses the same registry for its ordered `p` rows
and `r` columns and recomputes every entry.  None of the four classes is a
global injectivity or universal-recovery result.

The conclusion license remains exact: `FINITE_COLLISION` licenses only
`NO_GLOBAL_CONCLUSION`; `FINITE_PAIR_SEPARATION` licenses only its named
`r=<coordinate>;B_<p>_NOT_ISOMORPHIC_B_<q>` statement;
`FINITE_RANGE` licenses only `FINITE_RANGE_ONLY`; and
`NO_INFINITE_EVIDENCE` licenses only `OPEN_NOT_AUTHORIZED`.

### 3.4 Four same-method primitive counterfactuals

After each ordinary seed -> mutation -> rejection -> detector -> inverse ->
accept chain, the same existing method canonically serializes and
independently reparses one serial counterfactual.  Its expected-class,
expected-detector, persisted prefix/witness receipts, prior receipt bytes,
and all method metadata remain byte-identical.  The method requires the
following causal observation before it may inspect that unchanged metadata:

| Method | Sole primitive change | Mandatory recomputation and observation |
|---|---|---|
| `S14` | pair member `q:5 -> 3` | recompute both prefixes on `[2;3;5;7;11;13]`; derive `FINITE_PAIR_SEPARATION` at 11, so the old collision conclusion rejects; the deliberately stale saved `q=5` prefix is detected only after that recomputation |
| `S15` | distinguishing coordinate `11 -> 13` with `p=2,q=3` unchanged | recompute both prefixes; coordinate 13 has equal values and the seed rejects as an invalid witness before any expected-class comparison |
| `S16` | finite registry `[2;3;5;7;11;13] -> []` | the finite matrix cannot remain `FINITE_RANGE`; derive `NO_INFINITE_EVIDENCE` and reject the old `FINITE_RANGE_ONLY` conclusion |
| `S17` | empty registry `[] -> [2]` | recompute the one-by-one finite matrix, derive `FINITE_RANGE`, and reject the old `OPEN_NOT_AUTHORIZED` conclusion |

For a counterfactual, mismatch with the deliberately unchanged expected
class is a required post-computation observation, not a way to choose a
branch and not a new detector class.  Changing only an expected class can
satisfy none of the four subfixtures.  These are serial subfixtures inside
the existing four methods: no row, mutation class, detector, method, CSV,
schema, or generated byte is added.

## 4. A-M2 — exact-one-coordinate comparator probes

All amendment-v1 Section-8 receipt collection remains binding: valid and
malformed `--verify-only` calls; recursive `lstat` from `.`; complete path
inventory; every directory; type, mode, size, regular-file SHA-256,
`mtime_ns`, `ctime_ns`, link count, device, and inode; uid-0 operation;
relative-only diagnostics; and the live mode, mtime, ctime, transient-sidecar,
and root variants.

Within the existing `test_rep_010`, immediately after one actually collected
valid before-receipt has compared equal to its after-receipt, the method
selects the actual regular-file record at

```text
papers/15-wieferich-ulm-packet-bases/results/valuation_normalization_controls.csv
```

relative to the synthetic repository root.  Absence, duplication, nonregular
type, or a captured mode other than the frozen valid-baseline `0444` fails
closed.  The method then performs two independent pure probes from the same
captured receipt `Q`:

1. deep-clone the complete object as `Q_mode`; set only that record's `mode`
   from `0444` to `0644`; leave path, type, size, digest, mtime, ctime,
   nlink, device, inode, all other records, record order, and inventory
   bit-for-bit identical; require the receipt comparator to reject with
   `E_VERIFY_ONLY_METADATA`;
2. separately deep-clone `Q` as `Q_mtime`; add exactly `1000000000` to only
   that record's integer `mtime_ns`; leave its `ctime_ns`, mode, type, size,
   digest, nlink, device, inode, all other records, record order, and
   inventory bit-for-bit identical; require the comparator to reject with
   `E_VERIFY_ONLY_METADATA`.

Before calling the subject comparator, an independent tuple-difference
routine which does not call that comparator enumerates every
`(relative_path,coordinate,before,after)` difference.  It requires the exact
singleton sets

```text
{(selected_path,mode,0444,0644)}
{(selected_path,mtime_ns,t,t+1000000000)}.
```

The probe objects exist only in method memory.  Neither probe mutates a
filesystem, changes `ctime_ns`, consults an expected detector, or reuses the
other probe's clone.  Thus a comparator omitting either `mode` or `mtime_ns`
fails even if it compares `ctime_ns`.  `test_rep_010` remains one method and
one metadata-integrity class; no schema, path, artifact, generated byte, or
method count changes.

## 5. A-M3 — byte-bound Linux atomic possession

### 5.1 Impossibility result and exact replacement

Linux has no conditional remove-directory-by-held-directory-FD operation.
unlinkat accepts a retained parent FD plus a replaceable basename;
openat2 makes resolution safe but does not make a later unlink conditional
on an already held child inode; renameat2 cannot condition an exchange on a
held inode; and O_PATH, file handles, flock/advisory locks, inotify, and fanotify do
not prevent a noncooperating same-uid process from renaming a parent entry.
The v1 sequence of checking a fixed name and later deleting that name is
therefore not repairable as an ordinary shared-mount pathname protocol.

The sole replacement primitive is

    P15R_REPRODUCE_EMBEDDED_POSSESSION_V2

It combines two indivisible authorities:

1. package-lock ownership is one successful abstract AF_UNIX bind whose
   socket remains open; and
2. every filesystem deletion occurs relative to retained capabilities in a
   private mount namespace after the guardian has proved that no other task
   in that namespace can mutate a path.

The only source of the host coordinator, namespace launcher, PID-1 guardian,
RPC decoder, replacement actor, signal relay, and cleanup state machine is
one literal embedded Python-standard-library block between the fixed markers
P15R_POSSESSION_PY_V2_BEGIN and P15R_POSSESSION_PY_V2_END inside the already
frozen implementation path experiments/reproduce.sh.  The POSIX-shell prefix
performs the unchanged entry-script and physical-root checks and then uses
python3 -B with that in-file block; it does not create or import a separate
launcher service.  The future manifest's existing implementation digest for
experiments/reproduce.sh byte-binds the complete creator and protocol source.
There is no seventh repository path, separately supplied service or binary,
additional digest, authority binding, or dynamically downloaded component.
Python stdlib plus direct libc/Linux syscall bindings are the only facilities
used, as already permitted for the six implementation paths.

### 5.2 Exact supported platform and trusted boundary

The supported platform is deliberately narrow and fail-closed:

    operating system and syscall ABI     Linux x86_64, little-endian LP64
    launcher user namespace              the initial user namespace
    launcher r/e/s/fs uid and gid        0/0/0/0
    frozen logical UID_DEC               0
    guardian outer uid and gid           GUARDIAN_OUTER_UID/GID=65534
    network concurrency domain           one designated inherited netns
    quiescence primitive                 one root-owned cgroup-v2 subtree
    project source                       the two preopened exact root FDs
    writable project tree                none
    writable operational filesystem      one unexported private tmpfs

Every supported invocation of this repository must start in the same
designated network namespace and must not call CLONE_NEWNET.  An invocation
from another network namespace or a platform on which the repository can be
entered concurrently from another network namespace is unsupported and
stops before a project write.  The abstract lock is package-wide within this
explicit concurrency domain; this amendment makes no broader concurrency
claim.

Initial-user-namespace uid 0 and any process holding CAP_SYS_ADMIN,
CAP_SYS_PTRACE, CAP_SETUID, CAP_SETGID, or an equivalent ancestor capability
are the trusted platform-administrator boundary.  The design does not claim
to resist a hostile initial-user-namespace root, a hostile kernel, an LSM
administrator, or an administrator that deliberately enters or destroys the
private namespaces.  If any of those actors must be adversarial, A-M3 has no
Linux solution under the frozen six-path surface and implementation must
stop.

No reservation of uid 65534, account exclusivity, process census, or
administrator promise is a premise of cleanup correctness.  An
initial-namespace process
with outer uid 65534 can signal an inner-uid-0 worker because both map to the
same kernel uid; dumpable=0 does not change kill permission.  Quiescence is
instead the kernel cgroup-v2 frozen state described below.  SIGCONT cannot
make a task in a frozen cgroup runnable, and a worker has neither a path nor
an FD with which to move itself out.  The two-user-namespace construction
remains mandatory for setns, capability, ptrace, and proc-root isolation.

P resolves its own exact unified-cgroup-v2 directory from the sole canonical
0::/path line of /proc/self/cgroup, starting at a preopened cgroup2 mount FD
and using openat2 BENEATH/NO_SYMLINKS/NO_MAGICLINKS.  PID_DEC is P's canonical
base-ten PID in the initial PID namespace.  Before L exists, P creates one
root-owned session directory with basename

    p15r-possession-v2-PID_DEC

and exact children guardian and workers.  Each mkdirat name insertion is
atomic; the three creations are not represented as one atomic transaction.
On a partial failure P unwinds only names whose creation and identity it has
proved through retained FDs.  It never opens, removes, or reuses a stale or
pre-existing name.  P enables no controller and requires `cgroup.type` to
read exactly `domain` and `cgroup.subtree_control` to be empty for session,
guardian, and workers.  It retains
directory FDs and exact device/inode receipts for the current parent, session,
guardian, and workers until final removal.  An existing name, changed parent,
wrong cgroup2 statfs type, missing delegation, or unremovable probe subtree is
E_POSSESSION_UNAVAILABLE; P never opens or removes a pre-existing name.

P retains root-only O_CLOEXEC FDs for workers/cgroup.freeze,
workers/cgroup.events, workers/cgroup.kill, session/cgroup.events,
session/cgroup.kill, and the three cgroup.procs files.
P creates session/guardian/workers with mode 0700, uid/gid 0, and no
intermediate permissive mode.  It changes only session/cgroup.procs and
workers/cgroup.procs to uid/gid 65534 and mode 0600; guardian/cgroup.procs,
workers/cgroup.freeze, workers/cgroup.kill, every cgroup.events file, all
directories, and the current-parent capability remain uid/gid 0, with write
permission only for initial root.  Those two delegated cgroup.procs inodes
are exactly the common-ancestor and destination write authorities required
by clone3 placement; no directory creation or freeze/kill authority is
delegated.

Before G exists, P creates L directly in guardian with
`clone3(CLONE_INTO_CGROUP|CLONE_PIDFD)`, `cgroup=guardian_fd`, and
`exit_signal=SIGCHLD`; ordinary fork-then-move is forbidden.  G is L's sole
later child and inherits guardian membership.  P verifies both memberships
through its retained cgroup and proc capabilities.

After authenticating G, P passes it one
O_PATH|O_DIRECTORY|O_CLOEXEC workers-cgroup FD in the one declared control
SCM_RIGHTS record.  G uses it only as clone_args.cgroup.  Every clone child
enters workers before its first instruction; the fixed trusted child stub
closes that FD and all nonwhitelisted descriptors before target-source or fixture
action.  G never passes the FD through exec, an RPC, or another socket.
Before READY, G hides every cgroup2 mount in its private mount namespace and
has dumpable zero before the descriptor exists in G.  The inherited trusted
child micro-stub is part of the same byte-bound reproduce.sh source; it closes
the workers-cgroup FD before invoking any subject source or fixture
code.  No subject worker ever holds that FD.  P rejects any
unexpected descriptor, SCM_RIGHTS record, `/proc/G/fd` accessibility, or
worker descriptor table.  Thus workers, although outer uid 65534, cannot
reopen cgroup.procs,
cgroup.freeze, or any ancestor and cannot migrate or thaw themselves.

The following are runtime preconditions, not conclusions from a kernel
version or sysctl:

    CLONE_NEWUSER, CLONE_NEWNS, and CLONE_NEWPID
    one-line uid_map/gid_map writes and setgroups=deny
    recursive private mount propagation and private tmpfs/proc mounts
    fchdir/openat/openat2 plus post-drop DAC/ACL read/write probes
    openat2, fstatat, unlinkat, and renameat2(RENAME_EXCHANGE)
    AF_UNIX abstract SOCK_SEQPACKET, SO_PEERCRED, SO_PASSCRED/SCM_CREDENTIALS
    signalfd, pidfd_open, pidfd_send_signal, waitid, and prctl
    unified cgroup v2, cgroup.freeze/events/kill, and cgroup FD delegation
    clone3(CLONE_INTO_CGROUP|CLONE_PIDFD) atomic worker placement
    securebits, capability bounding-set drop, no_new_privs, and seccomp-BPF

The embedded source owns its syscall ABI rather than consulting an external
header or helper: on the sole supported x86_64 ABI, `SYS_clone3=435`,
`SYS_openat2=437`, `SYS_pidfd_send_signal=424`, `SYS_pidfd_open=434`, and
`SYS_close_range=436`.  Its versioned `struct clone_args` is 88 zeroed bytes
with eleven little-endian unsigned-64 fields at offsets 0, 8, ..., 80 in the
kernel order flags, pidfd, child_tid, parent_tid, exit_signal, stack,
stack_size, tls, set_tid, set_tid_size, cgroup.  A worker creation changes
only `flags=CLONE_INTO_CGROUP|CLONE_PIDFD`, `pidfd` to the trusted output
address, `exit_signal=SIGCHLD`, and `cgroup` to the retained workers FD;
launcher creation uses the same record with the guardian FD.  Every other
field and reserved byte is zero.  A size, constant, endianness, returned PID,
pidfd, or first-instruction placement mismatch fails the disposable probe;
there is no architecture fallback.

The later authorized implementation must, before package, result, lock, or
generation-root writes, create and remove a disposable non-root child cgroup
and probe the exact clone-into, delegation, freeze-to-events,
thaw-to-events, kill, populated-to-zero, and removal operations.  Absence of
freeze/kill on the cgroup-v2 root itself is neither probed nor treated as an
error because those controls exist only on non-root cgroups.  Kernel
configuration files,
sysctls, uname, and a zero-hit /proc census establish necessary facts only;
seccomp, LSM, mount policy, uid-map policy, and syscall availability must be
tested.  Any denied, missing, semantically different, or unobservable
operation is E_POSSESSION_UNAVAILABLE before lock acquisition and project
writes, with no fallback to v1 pathname deletion.  This amendment performs
none of those probes and makes no current-runtime availability claim.

### 5.3 Closed bootstrap, placement, and record protocol

Bootstrap state is separate from lock and cleanup state and is exactly

    HOST_INIT
    CGROUP_READY
    LAUNCHER_ATOMICALLY_PLACED
    U1_CREATED_UNMAPPED
    U1_MAPPED
    U1_OUTER65534_ATTESTED
    U2_CREATED_UNMAPPED
    U2_ROOT0_MAPPED
    PRIVATE_MOUNT_READY
    PID1_FORKED
    CONTROL_AUTHENTICATED
    WORKER_CAPABILITY_DELIVERED
    CGROUP_PREFLIGHTED
    LAUNCHER_REAPED
    PRIVILEGE_DROP_ATTESTED
    GUARDIAN_READY
    BOOTSTRAP_FAILED

Only GUARDIAN_READY may enter lock state.  Every unexpected syscall result,
message, state, credential, map byte, descriptor, cgroup member, process, or
transition goes once to BOOTSTRAP_FAILED and E_POSSESSION_UNAVAILABLE.  No
bootstrap retry is legal after any package, result, lock, or generation-root
write.

The exact creation order is:

1. The single-threaded host coordinator P, still r/e/s/fs uid/gid 0 in the
   initial user, mount, PID, and cgroup namespaces, captures UID_DEC=0 and
   PID_DEC; blocks HUP, INT, QUIT, PIPE, ALRM, TERM, USR1, and USR2 before
   process creation; calls PR_SET_CHILD_SUBREAPER; opens the exact source
   capabilities; creates the cgroup tree of Section 5.2; then creates one
   root-owned transient child named `probe`, retains its identity, atomically
   places a no-filesystem micro-stub there, proves freeze/events, thaw/events,
   cgroup.kill, waitid/ECHILD, populated 0, and exact empty removal, and never
   reuses that name.  Only after the proved probe removal does P bind the
   control listener and create one CLOEXEC inherited bootstrap
   SOCK_SEQPACKET socketpair.  This is CGROUP_READY.
2. P creates L with exactly the 88-byte clone_args record frozen above,
   targeting guardian and requesting a pidfd.  No ordinary fork, clone,
   posix_spawn, vfork, subprocess helper, shell helper, or later cgroup move
   may replace this operation.  Before any namespace call, L verifies from
   /proc/self/cgroup that it was born in the retained guardian identity,
   retains only its bootstrap endpoint plus fixed read-only source slots 10
   and 11 for G, closes every other P descriptor, calls setsid, and clears
   supplementary groups.  P binds clone3's returned canonical outer PID to
   the returned launcher pidfd and guardian receipt; U1_CREATED later repeats
   that PID as a checked field.  This is
   LAUNCHER_ATOMICALLY_PLACED.
3. L verifies initial-user-namespace uid/gid 0 and calls
   unshare(CLONE_NEWUSER) while still uid 0.  U1's kernel owner is therefore
   initial uid 0, never uid 65534.  L sends U1_CREATED and blocks.  P writes
   and byte-re-reads each U1 file exactly once in this order:

       /proc/L/uid_map       "65534 65534 1\n"
       /proc/L/setgroups     "deny\n"
       /proc/L/gid_map       "65534 65534 1\n"

   U1 intentionally has no mapping for uid or gid 0.  P sends the sole
   U1_MAPS_COMMITTED acknowledgment.
4. L calls setresgid(65534,65534,65534) before
   setresuid(65534,65534,65534), requires empty supplementary groups, resets
   PR_SET_DUMPABLE to 0, clears its U1 effective, permitted, inheritable, and
   ambient capabilities, and sends OUTER_IDS_READY.  L's displayed uid is not
   evidence because an unmapped id can display the overflow value 65534.  P
   instead reads L's status from the initial PID namespace and requires all
   four Uid and Gid columns to be 65534, Groups empty, and all live capability
   sets zero.  P then sends OUTER_IDS_ATTESTED.
5. Still single-threaded and capability-empty in U1, L calls
   unshare(CLONE_NEWUSER).  U2's owner is uid 65534 in its direct parent U1;
   an initial-namespace uid-65534 process is not in U1 and gains no owner
   capability in U2.  L requires setgroups to read deny and writes and
   byte-re-reads exactly

       /proc/self/uid_map    "0 65534 1\n"
       /proc/self/gid_map    "0 65534 1\n"

   L sends U2_MAPS_COMMITTED and requires inner r/e/s/fs uid/gid all 0, empty
   groups, the exact maps, and dumpable zero.  UID_DEC and every later owned
   temporary object remain inner uid 0.
6. Using only creator capabilities in U2, L calls
   unshare(CLONE_NEWNS|CLONE_NEWPID).  CLONE_NEWPID does not move L.  Between
   that return and guardian creation no thread or process creation is legal.
   L's first and only later process creation is one fork whose child G must
   observe getpid()==1 in the new PID namespace; G inherits guardian cgroup
   membership and observes inner PID 1.  It does not claim to possess a G
   pidfd yet.  This is PID1_FORKED.
7. G becomes the isolated session leader, sets PR_SET_CHILD_SUBREAPER, makes
   mount propagation recursively private, mounts a private tmpfs over /tmp,
   mounts procfs for its PID namespace, validates the source capabilities,
   and reaches PRIVATE_MOUNT_READY before connecting exactly once to P's
   already-bound abstract control listener.
   P accepts one peer with uid/gid 65534, immediately pidfd_open's the
   SO_PEERCRED outer PID, and proves from stable proc status, parentage,
   NSpid ending in 1, start time, and retained guardian membership that this
   is L's sole G child.  It then accepts exactly one PID1_READY record and
   binds the peer, pidfd, outer PID, and inner PID 1.  An early, extra, reused,
   or mismatched peer is fatal.  The address is one leading NUL followed by
   the ASCII bytes
   p15r-possession-control-v2:PID_DEC, with exact sockaddr length and no
   trailing NUL.  It is carried to G only by the inherited bootstrap record,
   never as a pathname or reconnectable secret.  This is
   CONTROL_AUTHENTICATED.
8. P sends one WORKERS_CGROUP_FD record on the authenticated connection with
   exactly one untruncated SCM_RIGHTS item containing exactly one
   O_PATH|O_DIRECTORY|O_CLOEXEC FD.  G fstats it against P's workers
   device/inode receipt, receives with recvmsg(MSG_CMSG_CLOEXEC), verifies
   FD_CLOEXEC on the new descriptor and no second ancillary item, and acknowledges
   it once.  The record is the only cgroup descriptor handoff.  G never sends
   it, duplicates it, or exposes it through an RPC.  This is
   WORKER_CAPABILITY_DELIVERED.
9. Before a subject is admitted, G creates two disposable trusted micro-stubs,
   one at a time, with the exact clone3 worker record.  Each child is in
   workers before its first instruction, closes the cgroup FD, reports at its
   inherited barrier, and performs no filesystem operation.  G sends
   `CGROUP_PROBE_CHILD epoch=1 inner_pid=DEC`; P verifies that first child in
   workers, writes exact bytes "1\n" to the retained freeze FD,
   and sends `CGROUP_PROBE_FROZEN epoch=1` only after a fresh parse of the
   retained events FD yields frozen 1; it writes "0\n" and sends
   `CGROUP_PROBE_THAWED epoch=1` only after frozen 0.  The child exits, G reaps
   it, and sends `CGROUP_PROBE_REAPED epoch=1`.  G sends
   `CGROUP_PROBE_CHILD epoch=2 inner_pid=DEC`; P verifies that second child and
   writes exact bytes "1\n" to workers/cgroup.kill, then sends
   `CGROUP_PROBE_KILLED epoch=2`.  G reaps it and sends
   `CGROUP_PROBE_REAPED epoch=2`; only then may P accept a fresh events parse
   yielding populated 0.  Both clone pidfds, exact membership, delegation,
   freeze, thaw, kill, wait, and events parsing, together with P's earlier
   separate-probe removal, must succeed under the real
   seccomp/LSM/mount/permission policy.
   A denied operation or timeout is BOOTSTRAP_FAILED, with no weaker fallback.
   Completion is CGROUP_PREFLIGHTED; it asserts no current-runtime
   availability until an authorized implementation actually performs it.
10. L closes every source, namespace, cgroup, private-root, parent, lock,
    control, and listener duplicate and exits.  P waitid-reaps L through its
    pidfd, verifies guardian now contains exactly G, and sends
    LAUNCHER_REAPED.  G may not bind a package lock, create a generation root,
    or advertise READY before this record.
11. G hides every cgroup2 mount, closes setup-only descriptors, drops every
    capability bounding-set bit while CAP_SETPCAP remains effective, clears
    ambient capabilities, locks SECBIT_NOROOT, SECBIT_NO_SETUID_FIXUP, and
    disabled SECBIT_KEEP_CAPS, clears effective/permitted/inheritable sets,
    and sets PR_SET_NO_NEW_PRIVS=1 and PR_SET_DUMPABLE=0.  It revalidates the
    source read/write boundary in Section 5.4.  P then creates one disposable
    initial-user-namespace probe child, drops that child irreversibly to all
    r/e/s/fs uid/gid 65534 with empty groups/capabilities, and requires its
    attempts to open G's proc fd/root/namespace entries to be denied; the
    child receives no cgroup or namespace FD and is pidfd-killed/reaped before
    READY.  A denial caused only by a transient pathname error is not proof.
    Every worker inherits and verifies the
    same securebits, empty capability sets and bounding set, no_new_privs,
    dumpable zero, inner uid/gid 0, and empty groups.  A setuid, setgid, or
    file-capability executable is forbidden.  P independently re-reads G's
    status and cgroup membership.  This is PRIVILEGE_DROP_ATTESTED; only then
    may G send GUARDIAN_READY.

The inherited bootstrap channel carries only this closed sequence and closes
after CONTROL_AUTHENTICATED:

    U1_CREATED outer_pid=DEC
    U1_MAPS_COMMITTED outer_pid=DEC
    OUTER_IDS_READY outer_pid=DEC
    OUTER_IDS_ATTESTED outer_pid=DEC
    U2_MAPS_COMMITTED outer_pid=DEC

Directions alternate L-to-P, P-to-L, L-to-P, P-to-L, and L-to-P.
Each occurs exactly once in printed order; the PID field is checked against
the retained launcher pidfd before a transition.  No descriptor
or ancillary item is legal on this inherited channel.

The authenticated P--G control connection then carries only the closed enum

    PID1_READY
    WORKERS_CGROUP_FD
    WORKERS_CGROUP_FD_ACK
    CGROUP_PROBE_CHILD
    CGROUP_PROBE_FROZEN
    CGROUP_PROBE_THAWED
    CGROUP_PROBE_REAPED
    CGROUP_PROBE_KILLED
    LAUNCHER_REAPED
    GUARDIAN_READY
    CHILD_REGISTERED
    CHILD_ADMITTED
    CHILD_REAPED
    OBJECT_REGISTERED
    OBJECT_RELEASED
    LOCK_BOUND
    FREEZE_REQUEST
    FROZEN_NOREFS
    FROZEN_FINAL
    CLEANUP_COMMITTED
    THAWED
    KILL_REQUEST
    KILL_ISSUED
    REAPED
    CGROUP_EMPTY
    CLEANUP_RESULT
    SIGNAL_PENDING
    SIGNAL_CLEANED
    EXIT

Every record is one four-byte unsigned big-endian payload length at most
4096, followed by exactly that many canonical ASCII bytes and no trailing
byte.  Its payload is the exact type followed, where specified below, by one
ASCII space between ordered key=value fields:

    PID1_READY outer_pid=DEC inner_pid=1
    WORKERS_CGROUP_FD session=DEC
    WORKERS_CGROUP_FD_ACK session=DEC
    CGROUP_PROBE_CHILD epoch=DEC inner_pid=DEC
    CGROUP_PROBE_FROZEN epoch=DEC
    CGROUP_PROBE_THAWED epoch=DEC
    CGROUP_PROBE_REAPED epoch=DEC
    CGROUP_PROBE_KILLED epoch=DEC
    LAUNCHER_REAPED outer_pid=DEC
    GUARDIAN_READY outer_pid=DEC inner_pid=1
    CHILD_REGISTERED session=DEC child=DEC inner_pid=DEC
        role=ROLE owner=OWNER purpose=PURPOSE fdset=FDSET
        cwd_dev=DEC cwd_ino=DEC
    CHILD_ADMITTED session=DEC child=DEC
    CHILD_REAPED session=DEC child=DEC status=DEC
    OBJECT_REGISTERED session=DEC handle=DEC kind=KIND dev=DEC ino=DEC
    OBJECT_RELEASED session=DEC handle=DEC kind=KIND dev=DEC ino=DEC
    LOCK_BOUND session=DEC lock=DEC
    FREEZE_REQUEST session=DEC handle=DEC phase=METHOD|FINAL
    FROZEN_NOREFS session=DEC handle=DEC phase=METHOD epoch=DEC
    FROZEN_FINAL session=DEC handle=0 phase=FINAL epoch=DEC
    CLEANUP_COMMITTED session=DEC handle=DEC epoch=DEC
    THAWED session=DEC handle=DEC epoch=DEC
    KILL_REQUEST session=DEC epoch=DEC
    KILL_ISSUED session=DEC epoch=DEC
    REAPED session=DEC epoch=DEC
    CGROUP_EMPTY session=DEC epoch=DEC
    CLEANUP_RESULT session=DEC handle=DEC outcome=OUTCOME
    SIGNAL_PENDING signo=DEC
    SIGNAL_CLEANED signo=DEC outcome=OUTCOME
    EXIT status=DEC outcome=OUTCOME

Continuation indentation above is presentational only: every payload is one
line with those fields in exactly that order.  DEC is the base canonical
nonnegative-decimal grammar; handle zero is reserved for FINAL.  ROLE,
OWNER, PURPOSE, FDSET, KIND, and OUTCOME are members of their already closed or
clause-closed enums, never arbitrary strings.
OWNER is exactly `SUITE_173` for the one top-level test runner or one of the
173 frozen method names for every other child; the token does not add a
unittest method.

PID1_READY is G-to-P and occurs exactly once immediately after connection
authentication.  WORKERS_CGROUP_FD is P-to-G and is the only record with
ancillary data; WORKERS_CGROUP_FD_ACK is G-to-P, and the single FD/ACK pair
occurs exactly once before the probe.  For each probe
epoch, CGROUP_PROBE_CHILD and CGROUP_PROBE_REAPED are G-to-P; the other probe
records are P-to-G.  Epoch 1 has CHILD, FROZEN, THAWED, REAPED and epoch 2
has CHILD, KILLED, REAPED in exactly those orders.  CHILD_REGISTERED is G-to-P after
clone3 returns both PID and pidfd but before G releases the trusted child
barrier; P must verify the child in workers before returning the one
P-to-G CHILD_ADMITTED record that releases it.  OBJECT_REGISTERED,
OBJECT_RELEASED, and CHILD_REAPED are G-to-P and occur only under their
Section 5.5 registry transitions; CHILD_REAPED can occur once for each
registered child.  FREEZE_REQUEST, CLEANUP_COMMITTED,
KILL_REQUEST, REAPED, CLEANUP_RESULT, SIGNAL_CLEANED, and EXIT are G-to-P;
FROZEN_NOREFS, FROZEN_FINAL, THAWED, KILL_ISSUED, and CGROUP_EMPTY are P-to-G.  The exact
transaction cardinalities and state guards are frozen in Section 5.5.
LAUNCHER_REAPED is P-to-G and GUARDIAN_READY is G-to-P; they occur once in
that order after the probe.
LOCK_BOUND is G-to-P exactly once after each successful bind plus complete
CREATED receipt and before that lock can enter OWNED.  CLEANUP_RESULT occurs
once per registered handle after its terminal proof.  SIGNAL_PENDING is
P-to-G at most once and only from signalfd; it closes admission.  If present,
SIGNAL_CLEANED with the same signal precedes the sole terminal EXIT.  Without
a signal, EXIT still occurs exactly once on an orderly terminal path.

An unknown, duplicate, reordered, oversized, non-ASCII, partial,
post-terminal, wrong-direction, wrong-state, or cross-session record,
unexpected ancillary item, ancillary truncation, credential mismatch, pidfd
drift, or EOF is fail-closed.  No record is persisted or serialized.  The
RPC protocol uses the same length framing but a separate per-requester
endpoint and the SCM_CREDENTIALS authority frozen in Section 5.9; it never
shares this P--G connection.
### 5.4 Repository/package capabilities and write boundary

Before L is forked, P opens the already derived physical repository and
package roots with O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC and records
type, mode, uid, device, and inode.  Their inherited descriptor numbers are
fixed setup ABI slots 10 and 11.  A preopened FD bypasses lookup of the
mode-0700 /root ancestor; it does not bypass DAC from that FD onward.
Therefore preflight must prove that outer uid 65534 can search every required
subdirectory and read every registered implementation, authority, and
lifecycle input.  Any required post-drop absolute reopen or unreadable
component is E_POSSESSION_UNAVAILABLE.

After becoming outer uid 65534 and before project reads, G opens every
registered directory and file from those two starting FDs without following
symlinks.  Using its real post-drop credentials, it requires search access on
every traversed directory, read access on every required input, and denial of
write access on every repository/package directory and file, including ACL,
idmapped-mount, and filesystem policy effects.  A mode-bit inference alone
is not enough.  It also requires that set-user-ID, set-group-ID, and file
capabilities cannot change a worker credential.  Failure of any read or
write-denial probe is E_POSSESSION_UNAVAILABLE.

All project reads are openat/openat2 relative to the held source FDs, or
relative paths after G fchdir-spawns a worker at the exact package FD and the
worker derives the repository as the package root's second parent.  Every
worker closes inherited source descriptors before subject code begins.  No
process reopens /root or any ambient absolute project path.  The exact
device/inode receipts remain live through the run, and all six implementation
and fourteen authority paths retain their existing serialized names.

P closes its source-FD copies after GUARDIAN_READY; G retains the source
capabilities solely to set a worker's cwd and closes them after the last
worker.  Neither P nor G uses them in unlinkat, renameat, mkdirat, chmod, or
any other write operation.  P never receives a private-tmpfs, namespace,
generation-
parent, generation-root, lock-parent, lock-directory, or package-lock socket
FD.  A worker never receives a parent, lock, namespace, setup, or package-
lock descriptor.  The only writable filesystem visible to the workflow is
the private tmpfs: copied packages, canonical A/B, mutation roots, P25, and
lock receipts live there.  No repository write is required or allowed.

The only worker descriptor exceptions are the existing single-call
P15R_GENERATION_ROOT_FD and, for the test workflow only, the new RPC endpoint
below.  Canonical A/B are exposed to comparisons and the test suite only for
the already frozen read-only operations; mutation writes remain confined to
the named method-owned root.  If future implementation requires a write to
the root-owned checked-in repository rather than a private copy, this design
is blocked rather than widened.

### 5.5 Cgroup membership, freeze, kill, and reap proof

G is single-threaded PID 1 and a subreaper in the private PID namespace.  It
is the only process outside workers that can mutate the private tmpfs.  Every
subject, requester, generator, copied wrapper, replacement actor, lock
holder, and contender is a direct child created by G with exactly
CLONE_INTO_CGROUP|CLONE_PIDFD, exit_signal=SIGCHLD, and all other clone_args
fields as frozen in Section 5.2.  Ordinary fork-then-move is forbidden.  A
child or subject may not call clone, clone3, fork, vfork, posix_spawn,
unshare, or setns; daemonize; create a thread; use CLONE_PARENT; or export a
namespace or cgroup FD.  Any workflow subprocess is instead a separately
registered direct G child.

The trusted first-instruction micro-stub closes the workers-cgroup FD and
every descriptor outside its role whitelist, installs no_new_privs and the
byte-bound x86_64 seccomp filter, and blocks at a one-use barrier.  Its first
branch requires `seccomp_data.arch == AUDIT_ARCH_X86_64 (0xc000003e)` and
kills the process otherwise; its second kills any syscall number carrying
`__X32_SYSCALL_BIT (0x40000000)`.  Only after those gates does the native
x86_64 table deny clone, clone3, fork, vfork, execve, execveat, unshare,
setns, io_setup, io_submit,
io_cancel, io_destroy, io_getevents, io_pgetevents, io_uring_setup,
io_uring_enter, io_uring_register, sendmsg, and sendmmsg with
SECCOMP_RET_ERRNO|EPERM; the arch/x32 branches use SECCOMP_RET_KILL_PROCESS
and the sole final branch allows other native calls.  RPC requesters use
plain send/write, so SO_PASSCRED supplies credentials without giving a worker
an ancillary-data send primitive.  POSIX-AIO helper threads are excluded
by the same no-thread rule.  Therefore no worker can originate a descendant,
namespace escape, queued asynchronous filesystem operation, or migration.
A filter install, architecture, syscall-number, or denial-probe mismatch is
E_POSSESSION_UNAVAILABLE before a subject write.  This is a platform
precondition to be runtime-tested, not a claim about the present host.

After clone3 returns, G records the PID, pidfd, start time, session, owner,
purpose, role, expected cwd, and exact descriptor whitelist, sends
CHILD_REGISTERED, and waits.  P independently verifies the PID/pidfd,
workers membership, one thread, dumpable zero, credentials, cwd, and
descriptor set through initial-namespace procfs before authorizing G to
release the barrier.  Only then can subject code execute.  G waitid-reaps
each direct child and sends CHILD_REAPED.  P mirrors the closed ledger.
The only live roles are

    TOP_TEST_RUNNER | REQUESTER | GENERATOR | REPLACEMENT_ACTOR | LOCK_HOLDER |
    CONTENDER | PROBE | EXITED_UNREAPED

and the only FDSET values are

    STDIO | STDIO_RPC | STDIO_SOURCE_RPC | STDIO_GENERATION_ROOT

A GENERATOR may have STDIO_GENERATION_ROOT only for its single call and must
be reaped before cleanup.  A live TOP_TEST_RUNNER or REQUESTER may have STDIO_RPC or
STDIO_SOURCE_RPC but never a generation-parent, generation-root, root-member,
lock-parent, lock, lock-member, cgroup, namespace, or package-lock socket FD.
The other mutating roles must exit and be reaped before a cleanup request.
A task, thread, role, FD, or cgroup member absent from the two ledgers is an
error, never presumed harmless.

G reports each live owned filesystem identity to P when created and again
when released, using the internal kinds ROOT_PARENT, ROOT, ROOT_MEMBER,
LOCK_PARENT, LOCK, and LOCK_MEMBER with session, handle, device, and inode.
P retains only these numeric receipts, never a private-mount FD.  Receipt
records use the same closed channel and are not result artifacts.  The
corresponding exact payloads are

    OBJECT_REGISTERED session=DEC handle=DEC kind=KIND dev=DEC ino=DEC
    OBJECT_RELEASED session=DEC handle=DEC kind=KIND dev=DEC ino=DEC

OBJECT_REGISTERED precedes any child access; OBJECT_RELEASED follows the
last G close.  Release changes P's entry to RELEASED_TOMBSTONE rather than
deleting it.  P includes LIVE and tombstone identities in every reference
audit through the matching freeze epoch and prunes them only after the
matching CLEANUP_RESULT plus THAWED, or after final CGROUP_EMPTY.  A duplicate
identity, mismatched release, premature prune, or live member not in the
registry is fatal.

The workers-cgroup state is exactly

    THAWED -> FREEZING -> FROZEN -> THAWING -> THAWED
    THAWED -> FREEZING -> FROZEN -> KILLING -> EMPTY
    any nonterminal state -> CGROUP_ERROR

Only P writes cgroup.freeze or cgroup.kill.  Before every such write and
events read it fstats the retained FD, cgroup directory, and cgroup2
filesystem against their creation receipts.  For each events read P seeks
the retained FD to offset zero, reads to EOF with a 4096-byte ceiling, and
parses LF-terminated ASCII records of exactly KEY, one space, and one
canonical decimal value.  Required keys populated and frozen must each occur
exactly once; other distinct syntactically valid keys may occur in any order
and are ignored.  poll is notification only.  A transition is proved only by
a fresh full parse with the requested exact key value.

The immutable in-source transition deadline is

    P15R_CGROUP_TRANSITION_TIMEOUT_NS=30000000000

measured with CLOCK_MONOTONIC; it is neither an environment field nor a
serialized value.  EINTR restarts against the original deadline.  Timeout,
short/partial control write, malformed events bytes, wrong identity, D-state
noncompletion, or state drift enters CGROUP_ERROR.  If this occurs before a
destructive private-path syscall, none is attempted.  If it occurs later,
the transaction cannot report PASS or ABSENT and no further pathname
mutation is attempted; P may still use cgroup.kill for crash containment.

For one method-level cleanup, the exact protocol is:

1. G closes admission for the session, finishes every synchronous
   filesystem syscall, reaps any generator and controlled replacement actor,
   and requires that the only workers remaining are the authenticated
   TOP_TEST_RUNNER/REQUESTER records that will receive or relay the immutable
   result.  No SCM_RIGHTS
   item, kernel worker, queued asynchronous I/O, or non-G path mutator may be
   outstanding.  Because worker sendmsg/sendmmsg are denied and G never sends
   an RPC FD, an RPC socket cannot contain SCM_RIGHTS.  G nevertheless drains
   each requester endpoint with nonblocking recvmsg(MSG_CMSG_CLOEXEC) to
   EAGAIN after consuming the exact pending request, rejects every extra
   frame and every ancillary item other than that request's sole required
   SCM_CREDENTIALS, and records the request before asking P to freeze.
2. G sends FREEZE_REQUEST with phase=METHOD.  P requires workers state
   THAWED, closes its corresponding child-admission gate, reconciles the
   complete G/P ledgers with workers/cgroup.procs and every task directory,
   writes exact bytes "1\n" once to workers/cgroup.freeze, and enters
   FREEZING.
3. P loops only until a fresh retained-events parse yields frozen 1.  It then
   enters FROZEN and repeats the complete cgroup/task inventory.  Frozen
   state alone does not close membership: closure is separately proved by
   the root-owned tree and control files, absence of a cgroup mount or
   cgroup/procs FD in every worker, G's inaccessible dumpable-zero descriptor
   table, the no-clone seccomp contract, and exact ledger membership.  Any
   administrator able to migrate a task is already inside the trusted
   boundary of Section 5.2.
4. While workers remain frozen, P uses its initial-root proc authority,
   without opening or retaining a target FD, to stat every /proc/PID/fd
   target and cwd/root/exe target and to parse every maps entry for every
   thread.  It compares the results with the registered owned-object set and
   each role's exact FDSET/cwd receipt.  No worker may reference any
   ROOT_PARENT, ROOT, ROOT_MEMBER, LOCK_PARENT, LOCK, or LOCK_MEMBER identity;
   no unregistered descriptor, cwd, root, executable, mapping, SCM_RIGHTS
   queue, kernel AIO context, or live child is permitted.  P re-reads
   cgroup.events frozen 1 and the same membership after this audit.
5. Only after all four proofs does P increment the session freeze epoch and
   send FROZEN_NOREFS.  Until that exact record G may not fstatat, renameat,
   unlinkat, rmdir, or otherwise begin cleanup.  After it, G is the sole
   runnable process with a private-mount pathname capability, so an external
   uid-65534 SIGCONT cannot create a check/use path actor.
6. G performs the one retained-capability cleanup transaction, completes the
   foreign audit if applicable, closes the released owned descriptors, and
   queues the immutable RPC result without sending it.  G sends
   CLEANUP_COMMITTED with the same epoch.  P writes exact bytes "0\n" once,
   enters THAWING, and waits for a fresh events parse yielding frozen 0.
   P then enters THAWED, reopens the admission gate, and sends THAWED.
   Only after THAWED may G send the queued RPC result or start another child.

Method-level freeze does not SIGSTOP, SIGCONT, kill, or retain an assumed
cooperative waiter.  The kernel freezer is the only quiescence fact.  A
method error before FROZEN_NOREFS goes to terminal final kill with no
pathname deletion.  An error after cleanup begins is visible E_CLEANUP and
cannot produce a successful ABSENT/PASS receipt.  A controlled displacement
may still complete its owned-object and foreign-object audit while frozen,
but its specified result remains DISPLACED_CLEANED/E_CLEANUP.

Final cleanup is used for ordinary success, ordinary failure, P24, a handled
signal, or any state that cannot safely resume.  Its exact protocol is:

1. G permanently closes every RPC and child-admission gate and sends
   FREEZE_REQUEST with phase=FINAL and reserved handle 0.  From THAWED P
   writes freeze=1; from FREEZING it finishes that pending transition; from
   an already proved FROZEN METHOD epoch it does not rewrite the control.  In
   every case it requires a fresh events parse with
   frozen 1 and the same root-owned
   cgroup identity.  Unlike METHOD, FINAL permits registered generators,
   requesters, their legitimate owned-object references, an inconsistent
   ledger, or an unknown workers member: those facts require killing and may
   not make terminal containment depend on a no-reference receipt.  Because
   the root-owned controls and no-migration boundary remain intact, P sends
   FROZEN_FINAL, not FROZEN_NOREFS.  No private-path cleanup occurs yet.
2. Only after FROZEN_FINAL G sends KILL_REQUEST.  P verifies the epoch and writes exact bytes "1\n"
   once to the retained workers/cgroup.kill FD, enters KILLING, and sends
   KILL_ISSUED.  This kernel operation, rather than frozen state, supplies
   concurrent-fork handling and migration protection.
3. G loops waitid/waitpid over every direct child and reparented descendant
   until ECHILD, closes every pidfd, and proves its ledger empty; it sends
   REAPED.  P independently requires workers/cgroup.procs empty, enumerates
   no task/thread, and only after REAPED obtains a fresh retained-events parse
   with populated 0.  Both independent receipts are mandatory; neither
   populated 0 nor an empty directory substitutes for reaping.  P enters
   EMPTY and sends CGROUP_EMPTY.
4. Only after CGROUP_EMPTY, which proves all worker references are gone, may
   G perform generation-root, P25, lock, and
   foreign-fixture cleanup through retained capabilities.  It closes the
   workers-cgroup FD before its last CLEANUP_RESULT, then sends EXIT and
   exits.  P reaps G through the retained pidfd, requires guardian and session
   to yield populated 0, and removes the exact empty cgroups in order workers,
   guardian, session.  Before each rmdir it compares the held directory and
   parent/name device/inode receipts; it never opens or removes a
   pre-existing, replaced, nonempty, populated, or foreign cgroup name.

The cgroup directories and controls are operational containment state, not
project artifacts or an additional implementation path.  Normal removal is
by P's retained root-owned capabilities.  If G dies, P writes session
cgroup.kill, treats events poll only as notification, loops waitid over G and
every direct or reparented descendant to ECHILD while closing all pidfds, and
then requires a fresh session-events parse with populated 0.  Only both reap
and populated receipts permit removal of the proved session tree, and P
records only CRASH_TEARDOWN; it performs no private-mount pathname
cleanup and cannot assert ABSENT.  If P dies or its control connection reaches
G as EOF, G performs no pathname deletion, closes its descriptors, and exits
PID 1 so the private PID/mount namespace tears down; stale host cgroups may
require the trusted administrator and are never a success receipt.  If P is
stopped, progress may stop.  If G or a worker is stopped or continued by an
outer uid-65534 peer, freeze/kill and cgroup membership remain controlled by
P; availability may be denied but foreign pathname integrity is unchanged.
An uncatchable kill at any point is CRASH_TEARDOWN, not CLEANING, ABSENT, or
PASS.

A FINAL freeze timeout or control-identity failure permits P to attempt
cgroup.kill only as crash containment; it forbids every private-path cleanup
and every ABSENT/PASS receipt.  Thus a METHOD failure before
FROZEN_NOREFS reaches a killable FINAL path without recursively requiring
METHOD's no-reference audit.

### 5.6 Generation-root possession and cleanup

For every canonical or mutation root, G retains from mkdirat creation through
the final cleanup decision:

    parent_fd
    parent_container_fd and parent basename
    root_fd
    fixed basename
    opaque base-ten handle
    purpose, inner uid, device, inode, mode
    state

The root state is the closed enum

    LIVE | CLEANING | ABSENT | DISPLACED_OWNED |
    DISPLACED_CLEANED | ERROR

The only successful transition is LIVE -> CLEANING -> ABSENT.  Detection of
an uncontrolled fixed-entry drift before or during CLEANING goes to
DISPLACED_OWNED; the exact controlled exchange goes from LIVE or CLEANING to
DISPLACED_CLEANED after owned-object removal; a proved intact foreign fixture
adds terminal FOREIGN_RETAINED to the method receipt without changing either
displaced state; and every other failed proof goes to ERROR.  No displaced,
foreign, or error state transitions to ABSENT.

The fixed parent and child are nonsymlink mode-0700 directories owned by
inner uid 0.  G creates them relative to retained private-tmpfs
capabilities and keeps independent parent_fd and root_fd references.  It
passes a duplicate root_fd for exactly one generator call and retains its
own root_fd after the duplicate closes.  The five v1 variables remain exact:

    P15R_GENERATION_ROOT_FD
    P15R_GENERATION_PURPOSE
    P15R_GENERATION_UID
    P15R_GENERATION_DEV
    P15R_GENERATION_INO

Generator CLI, purpose grammar, steps 1--9, validation-before-emptiness,
descriptor-relative member creation, E_OUTPUT_CAPABILITY, and canonical
A/B versus MUTATION purpose separation remain binding.  Canonical A/B remain
the only two fresh generations and their three byte comparisons remain the
only copies.  The v1 instruction to close the creator's root FD after the
generator returns is superseded: only the child duplicate closes.

After Section 5.5 quiescence, ordinary cleanup:

1. enumerates and validates every member through root_fd;
2. deletes each owned regular member with
   unlinkat(root_fd,basename,0), never through a joined path;
3. for P25 specifically requires the sole exact occupied receipt and deletes
   occupied through the still-held P25 root_fd before releasing it;
4. proves the held root empty and requires the fixed entry, resolved only by
   fstatat(parent_fd,fixed,AT_SYMLINK_NOFOLLOW), to be the retained root
   device/inode;
5. while the exclusive receipt remains true, calls
   unlinkat(parent_fd,fixed,AT_REMOVEDIR);
6. proves fixed is ENOENT, the held directory is empty with st_nlink zero,
   and no foreign object was touched.  These link facts are not by themselves
   an owned-object-gone proof.  The same freeze epoch must already prove that
   no worker FD, cwd, root, executable, mapping, queued message, async I/O, or
   kernel worker refers to the root or a member; every generator duplicate is
   reaped; G's root_fd is the sole remaining user-space reference; and every
   member FD is closed.  G then closes that final root_fd, sends the matching
   OBJECT_RELEASED receipt, and P retains its tombstone.  Only the conjunction
   of fixed ENOENT, empty/st_nlink-zero, the frozen no-reference receipt, and
   closure of the sole final FD is `OWNED_OBJECT_GONE`; only then may G record
   ABSENT; and
7. removes the now-empty private parent by its basename relative to retained
   parent_container_fd, proves it gone, closes parent_fd, sends the exact
   ROOT_PARENT OBJECT_RELEASED record, and only then closes the unowned
   parent_container_fd.  Each ROOT_MEMBER likewise gets its own matching
   OBJECT_RELEASED after unlink and final member-FD close; one handle-wide
   release cannot cover another KIND.

There is no path join, external reopen, recursive deletion, glob, chmod,
truncate, or close-before-member-delete.  An unexpected disappearance,
replacement, device/inode drift, token drift, member, or cgroup-quiescence
failure performs no fixed-name deletion, records DISPLACED_OWNED or ERROR,
emits E_CLEANUP, and fails.  Namespace teardown is then crash containment,
not an ABSENT proof.

For the exact controlled exchange only, G already owns and retains the
foreign fixture FD and its internal exchange basename.  After the independent
same-uid actor exits and is reaped, the fixed entry points to the foreign
object and the internal basename points to the owned root.  Subject cleanup
never opens or mutates the foreign fixed entry.  It deletes owned members
through root_fd, requires the internal entry to equal root_fd while the
namespace is exclusively possessed, removes that internal owned entry,
proves fixed still foreign, closes the sole final root_fd under the same
frozen no-reference receipt, and sends OBJECT_RELEASED.  Only that complete
owned-object-gone proof records DISPLACED_CLEANED plus E_CLEANUP, never
ABSENT.  The method separately
proves the foreign bytes/device/inode unchanged before its own fixture
teardown.  FOREIGN_RETAINED is this pre-teardown receipt; destruction of the
private tmpfs later is not represented as subject deletion or ABSENT.

### 5.7 Atomic package lock and retained private receipt

The logical identifiers remain exactly

    /tmp/p15r-wieferich-ulm-controls-UID_DEC.lock

and the already validated isolated P15R_TEST_LOCK_DIR values in test context.
For either identifier G constructs the abstract address as one leading NUL
byte followed by the exact identifier's ASCII bytes.  It uses
AF_UNIX SOCK_SEQPACKET|SOCK_CLOEXEC and sockaddr length
offsetof(sockaddr_un,sun_path)+1+identifier_length, with no trailing NUL,
truncation, or hash.  The complete identifier must fit sun_path; otherwise
preflight is E_POSSESSION_UNAVAILABLE, never truncation.  A foreign holder
of that exact address is the P22
contender.  bind EADDRINUSE creates/touches no filesystem object, changes
ACQUIRING to UNOWNED, and returns the unchanged concurrent exit class 74.
Successful bind is the sole atomic lock-possession event.

The v1 candidate tuple, token grammar, and owner bytes are retained, but the
candidate is created only inside G's private tmpfs and is not lock authority.
Before ACQUIRING, G creates a candidate via retained tmp_fd, retains its FD,
and derives the unchanged 64-lowercase-hex token from the exact
length-delimited tuple

    P15R-LOCK-OWNER-v1, UID_DEC,
    candidate st_dev, candidate st_ino, candidate basename

It creates through candidate_fd exactly one .owner, mode 0600, nlink 1,
inner uid 0, with unchanged bytes

    P15R-LOCK-OWNER-v1 <64-lowercase-hex-token>\n

and fsyncs/re-reads it.  It closes the direct .owner member FD before CREATED;
later access is only relative to retained lock_fd, and the LOCK_MEMBER
identity remains registered until final unlink/release.  With handled
signals blocked, G changes
UNOWNED to ACQUIRING and calls bind.  On success it holds the socket
exclusively, installs the complete candidate with one
renameat2(lock_parent_fd,candidate_basename,lock_parent_fd,fixed_basename,
RENAME_NOREPLACE), retains lock_parent_fd and lock_fd, and records exactly

    CREATED(lock_dev,lock_ino,owner_dev,owner_ino)

before ACQUIRING can become OWNED.  A failure after bind but before CREATED
uses retained capabilities to remove only the private candidate, closes the
socket, and enters CLEANING then ABSENT; it cannot delete a shared host path.

The ordinary lock state remains

    UNOWNED -> ACQUIRING -> OWNED -> CLEANING -> ABSENT

with UNOWNED -> ABSENT on a no-lock exit, ACQUIRING -> UNOWNED on
EADDRINUSE, and ACQUIRING -> CLEANING -> ABSENT on a post-bind acquisition
failure.  Replacement terminal results are DISPLACED_OWNED,
DISPLACED_CLEANED, or FOREIGN_RETAINED and never masquerade as ABSENT.
The separate nonserialized lock cleanup outcome is exactly

    UNSET | ABSENT | DISPLACED_OWNED | DISPLACED_CLEANED |
    FOREIGN_RETAINED | ERROR | CRASH_TEARDOWN

Only state ABSENT with outcome ABSENT is ordinary success.  A displaced
outcome leaves the operational lock state at CLEANING; foreign audit or
namespace teardown does not advance it to ABSENT.

The package lock remains bound through every canonical/mutation/P25 cleanup
and its final receipt; nested copied-wrapper lock sessions remain bound
through every root owned by that session.  After Section 5.5 quiescence,
lock cleanup first relies on the same frozen no-worker-reference or final
CGROUP_EMPTY receipt as root cleanup.  It unlinks .owner only with
unlinkat(lock_fd,".owner",0), proves no direct member FD survives, sends the
exact LOCK_MEMBER OBJECT_RELEASED record, proves lock_fd empty, requires the fixed entry
through lock_parent_fd to equal lock_fd, removes it with
unlinkat(lock_parent_fd,fixed_basename,AT_REMOVEDIR), proves fixed ENOENT and
held st_nlink zero, closes the sole lock_fd, and sends the exact LOCK
OBJECT_RELEASED record.  The conjunction of fixed ENOENT, empty/st_nlink-zero,
the no-worker-reference receipt, member release, and final lock-FD close is
LOCK_OWNED_OBJECT_GONE; nlink/path facts alone are not.  G then closes and
releases LOCK_PARENT when the session no longer needs it and closes the bound
abstract socket last.  Only after all proofs and the final socket close may
state become ABSENT.
An unexpected fixed entry is foreign: it is never opened, unlinked, removed,
rewritten, truncated, or chmodded.  The bound socket, not the private
.owner/token/path, remains possession authority through the final decision.

For a controlled lock exchange, fixed_basename is therefore never a deletion
target.  After the actor is reaped and quiescence is proved, G deletes the
owned .owner only through lock_fd, proves that the known internal exchange
basename is the held owned lock, removes that internal basename relative to
lock_parent_fd, closes the sole lock_fd, sends matching LOCK_MEMBER and LOCK
release records, and records DISPLACED_CLEANED/E_CLEANUP only after the same
owned-object-gone conjunction.  It re-reads the
foreign fixed directory and .owner through the retained foreign FD, requires
their complete receipt unchanged, and closes the bound socket only after that
audit.  State never becomes ABSENT.  Method-owned fixture teardown may later
remove the foreign directory; subject cleanup may not.

### 5.8 Exact same-uid replacement falsifiers

The replacement actor is code in the same embedded reproduce.sh block.  It
runs as inner uid 0 with the worker's empty capability sets and independently
opens the exact private parent by path; it inherits no parent/root/lock/socket
FD.  At a guardian barrier it performs exactly one
renameat2(RENAME_EXCHANGE), reports completion, closes every FD, and exits.
G waitid-reaps it before subject cleanup.  This is the same-uid competing
pathname actor; G itself does not perform the injected exchange.

G creates and retains each foreign fixture before releasing the actor.
Generation-root foreign content is exactly one regular foreign file, mode
0600, nlink 1, inner uid 0, bytes P15R-FOREIGN-ROOT-v1 followed by LF.
Lock foreign content is exactly one regular .owner with those same metadata
and bytes P15R-FOREIGN-LOCK-v1 followed by LF.  Complete before/after
directory and member type/mode/uid/device/inode/nlink/size/bytes receipts
must match.

The five serial subfixtures are assigned without a new method or class:

| Existing method | Exact subfixture and required result |
|---|---|
| test_rep_009 | in its existing copied-package serial lifecycle fixture, after that copied wrapper's test-only canonical-A capability validation and immediately before its cleanup, exchange the canonical fixed root; foreign is identical, owned members are cleaned only through root_fd, result DISPLACED_CLEANED/E_CLEANUP and never ABSENT; this fixture root is excluded from the top-level two-generation/three-copy aggregate exactly like the existing copied-wrapper subruns |
| test_package_p25_nonempty_generation_root | first create one separate empty authorized MUTATION_P25_V1 root, exchange after validation and before cleanup, preserve the foreign object, and require DISPLACED_CLEANED/E_CLEANUP; this is the mutation-root falsifier and is not a canonical generation |
| test_package_p25_nonempty_generation_root | in a second serial root, retain exact purpose MUTATION_P25_V1 and sole occupied member; after E_NONEMPTY_OUTPUT, exchange immediately before cleanup, delete occupied only through the held P25 FD, preserve foreign, and require displaced cleanup failure in addition to the P25 detector |
| test_rep_009, ACQUIRING | exchange the private lock fixed entry immediately after token-complete CREATED while state remains ACQUIRING; the actor exits/reaps, cleanup deletes only owned .owner through lock_fd, foreign remains identical, and state never says ABSENT |
| test_rep_009, CLEANING | change OWNED to CLEANING, exchange before the first member deletion, reap the actor, delete only the owned .owner/root through held capabilities, preserve foreign, and require displaced visible failure |

The existing test_rep_009 signal-after-CREATED and pre-existing-lock
subfixtures remain.  The latter now has a peer bind and hold the same exact
abstract address while its existing different-token foreign directory and
.owner remain a method-owned observation fixture; the contender receives
exit 74, touches no member, and the complete foreign bytes/inodes remain
identical.  Neither party obtains filesystem deletion authority from the
filesystem receipt.  P24 retains its existing forced-failure
purpose and timing, but its root/lock cleanup uses G; it gains no replacement
purpose.  Thus a P-purpose is not reassigned and canonical A/B remain
separate from mutation roots.

The five new exact operational triggers are

    P15R_TEST_REPLACE_CANONICAL_ROOT=1
    P15R_TEST_REPLACE_MUTATION_ROOT=1
    P15R_TEST_REPLACE_P25_ROOT=1
    P15R_TEST_REPLACE_LOCK_ACQUIRING=1
    P15R_TEST_REPLACE_LOCK_CLEANING=1

Each requires P15R_TEST_CONTEXT=1, its owning method, its exact purpose, and
literal 1.  They are pairwise exclusive per child run and exclusive with
P15R_TEST_CREATE_POST_CACHE, P15R_TEST_ABORT_AFTER_FRESH_A, and
P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN.  Unknown values, combinations, owners,
or ordinary-run use are unchanged exit class 2.  These are serial
subfixtures only: package classes remain 28 and methods remain 173.

The copied-wrapper controller, not its canonical generator child, owns
P15R_TEST_REPLACE_CANONICAL_ROOT.  G consumes that trigger into private
session state before spawning the generator; the CANONICAL_A child receives
P15R_REPRO_ACTIVE=1 and the five ordinary generation fields, but receives
neither P15R_TEST_CONTEXT nor any replacement trigger.  Mutation/P25
generator children retain P15R_TEST_CONTEXT=1 and their exact MUTATION
purpose.  Thus the v1 ordinary/test-context purpose relationship is not
weakened to make the replacement fixtures pass.

### 5.9 Per-worker RPC, delegated subprocesses, signals, and terminal states

The only new ordinary child fields are

    P15R_POSSESSION_RPC_FD=<inherited SOCK_SEQPACKET endpoint>
    P15R_POSSESSION_ROOT_HANDLE=<canonical base-ten handle>

For each RPC-capable worker, G creates a fresh
AF_UNIX SOCK_SEQPACKET|SOCK_CLOEXEC socketpair immediately before that
worker's clone3.  G sets SO_PASSCRED on its endpoint and stores the immutable
mapping

    endpoint -> session, child, pidfd, inner PID, role, authorization, purpose

The trusted child stub retains exactly its own endpoint in the first field
above.  Both ends remain FD_CLOEXEC because no worker calls execve or
execveat: the single-threaded Python process cloned from G executes the exact
target source in-process after resetting argv/environment/cwd as specified
below.  Thus no CLOEXEC exception or pre/post-exec dumpable window exists.
A generator or non-RPC actor closes the child endpoint instead.  Every other
worker and every later G child gets a different socketpair.
The top-level test_controls process, a copied reproduce wrapper, and a
method-owned requester never inherit or reuse one another's endpoint.
Neither endpoint is sent with SCM_RIGHTS or discoverable through a shared
listener.  The top-level runner mapping is exactly
`role=TOP_TEST_RUNNER,authorization=SUITE_173,purpose=NONE`; it may name any
of the already frozen 173 methods only in the request shapes authorized
below.  Every copied/delegated requester instead has one exact owning method
and purpose.  Possession of this one-worker endpoint plus G's immutable mapping
is request authority; SCM_CREDENTIALS is only a mandatory consistency check,
not the sole authority.

A requester sends frames with plain send/write; its seccomp filter denies
sendmsg/sendmmsg.  G receives each complete frame with
recvmsg(MSG_CMSG_CLOEXEC) on the mapped endpoint and requires exactly one
kernel-supplied SCM_CREDENTIALS and no other cmsg.  The translated inner
pid/uid/gid must be the registered PID and 0/0, and the pidfd, start time,
workers membership, session, role, authorization, and purpose must still
match.
Missing, duplicate, explicit/forged, truncated, or extra credentials; any
SCM_RIGHTS; an endpoint mismatch; PID reuse; or a frame from an unregistered
descendant fails closed.  G responses contain no ancillary item.  No worker
receives P's coordinator channel or a cgroup descriptor.

RPC uses the four-byte length and canonical-ASCII rules of Section 5.3.  The
closed request/reply payloads are exactly

    ENDPOINT_BIND session=DEC owner=OWNER purpose=PURPOSE
    SESSION_CREATE request=DEC method=METHOD trigger=TRIGGER
    SESSION_CREATED request=DEC session=DEC
    LOCK_ACQUIRE request=DEC session=DEC
    LOCK_ACQUIRED request=DEC session=DEC lock=DEC state=OWNED
    LOCK_REJECTED request=DEC session=DEC status=74
        outcome=UNSET|FOREIGN_RETAINED
    LOCK_RELEASE request=DEC session=DEC lock=DEC
    LOCK_RELEASED request=DEC session=DEC lock=DEC outcome=OUTCOME
    ROOT_CREATE request=DEC session=DEC purpose=PURPOSE
    ROOT_CREATED request=DEC session=DEC handle=DEC
    ROOT_VALIDATE request=DEC session=DEC handle=DEC
    ROOT_VALIDATED request=DEC session=DEC handle=DEC
    SPAWN request=DEC session=DEC target=TARGET method=METHOD
        purpose=PURPOSE handle=DEC
    SPAWN_STDOUT request=DEC seq=DEC hex=LOWERHEX
    SPAWN_STDERR request=DEC seq=DEC hex=LOWERHEX
    SPAWN_RESULT request=DEC child=DEC status=DEC
        stdout_sha256=LOWERHEX64 stderr_sha256=LOWERHEX64
    INJECT_EXCHANGE request=DEC session=DEC handle=DEC trigger=TRIGGER
    INJECTED request=DEC session=DEC handle=DEC outcome=OUTCOME
    CLEAN request=DEC session=DEC handle=DEC
    CLEANED request=DEC session=DEC handle=DEC
        outcome=OUTCOME detector=DETECTOR
    FOREIGN_AUDIT request=DEC session=DEC handle=DEC
    FOREIGN_AUDITED request=DEC session=DEC handle=DEC outcome=OUTCOME
    SESSION_CLOSE request=DEC session=DEC
    SESSION_CLOSED request=DEC session=DEC outcome=OUTCOME

ENDPOINT_BIND is G's sole first frame after CHILD_ADMITTED and before target
source begins; it contains the immutable
mapping already attested by CHILD_ADMITTED.  A delegated requester must echo
that session in every request; the SUITE_173 runner is bound to session 0 and
may additionally use only opaque session handles returned on its own
SESSION_CREATE requests.  Continuation
indentation is presentational; each record is one frame with
fields in exactly the printed order.  Requests are monotonically increasing
per endpoint.  A request gets only its named reply sequence.  LOWERHEX chunks
have even length at most 2048 hexadecimal digits, sequence starts at zero,
and concatenation is capped at 16777216 decoded bytes per stream.  G reads
the child's stdout and stderr through separate nonblocking pipes, emits each
stream's chunks in its read order, and terminates with SPAWN_RESULT whose
digests cover the exact reconstructed byte strings.  The requester verifies
both lengths/digests and therefore receives the same separate stdout, stderr,
and exit status that its former local subprocess call observed.  Overflow,
pipe error, missing terminal result, interleaved request ID, or digest
mismatch is infrastructure failure, never a detector rewrite.

TARGET is the closed enum

    TOP_TEST_CONTROLS | VERIFY_ONLY_GENERATOR |
    GENERATE_CANONICAL_A | GENERATE_CANONICAL_B |
    GENERATE_MUTATION | COPIED_REPRODUCE |
    LOCK_HOLDER | LOCK_CONTENDER | REPLACEMENT_ACTOR

TOP_TEST_CONTROLS is used once by G before the runner endpoint exists and is
never legal in an RPC SPAWN; every other target is legal only in its frozen
owner/session role.

The remaining RPC tokens are closed here.  TRIGGER is exactly

    NONE | P15R_TEST_CREATE_POST_CACHE |
    P15R_TEST_ABORT_AFTER_FRESH_A | P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN |
    P15R_TEST_REPLACE_CANONICAL_ROOT |
    P15R_TEST_REPLACE_MUTATION_ROOT | P15R_TEST_REPLACE_P25_ROOT |
    P15R_TEST_REPLACE_LOCK_ACQUIRING |
    P15R_TEST_REPLACE_LOCK_CLEANING

DETECTOR is exactly

    NONE | E_CLEANUP | E_SIGNAL_ACQUIRE | E_POSSESSION_UNAVAILABLE

OUTCOME is exactly the Section-5.7 nonserialized outcome enum.  PURPOSE is
the unchanged generation-purpose enum plus `NONE`, with `NONE` legal only
for a target that receives no generation root.  METHOD in a request is one
of the exact 173 frozen names; SUITE_173 is an endpoint authorization token,
not a method.  Any other token is malformed before an operation.

A client never supplies argv, environment, cwd, path, FD number, lock
identifier, copied-package identity, or output basename.  TARGET selects one
byte-bound template owned by the embedded reproduce.sh block.  The templates
for test_controls and the two generator modes set sys.argv to exactly the
base-design argv, including the frozen option order, and use runpy on the
independently opened registered source; the surrounding interpreter already
runs with `-B`.  The selected session
supplies checked-in/A/B or the one output-dir value.  A generate target also
receives exactly descriptor 9 and the five unchanged P15R_GENERATION_*
fields from G's retained root record.  COPIED_REPRODUCE independently opens
the copied package's own experiments/reproduce.sh, proves its entry-script,
marker-block, copied-root, and source bytes against the registered source,
performs the unchanged POSIX-prefix checks in the byte-identical in-block
implementation, and then runs that delegated implementation in-process with
cwd at G's retained copied-package FD and only the frozen
active-marker/test-context/isolated-lock/trigger fields.  It does not exec a
shell or a copied program.  LOCK_HOLDER, LOCK_CONTENDER, and
REPLACEMENT_ACTOR are fixed in-block micro-stubs.  Every template closes all
nonwhitelisted FDs before its first subject instruction.  A need for any
exec, other argv, executable, env field, cwd source, pass_fds item, or target
is a design blocker.

G owns a session record containing session handle, owning method and trigger,
source/copy parent FD, copied-package FD and identity, exact derived copied
cwd, lock-parent FD, exact lock identifier, all root handles, and each child
pidfd.  SESSION_CREATE is accepted only from the top-level test process for
an already frozen copied-package method; G creates the copy and isolated
lock parent inside private tmpfs and returns only the opaque session handle.
It never returns a pathname.  Session state is exactly
`CREATED -> LOCKED -> CLEANING -> CLOSED`: after SESSION_CREATED the copied
wrapper must issue LOCK_ACQUIRE; G alone derives and binds the abstract
address, installs and retains the filesystem receipt, socket, and lock
handle, and returns LOCK_ACQUIRED.  A worker receives none of those
capabilities.  Exact bind EADDRINUSE instead returns LOCK_REJECTED, leaves
state CREATED with no lock handle or filesystem touch, and preserves class
74; that session may only audit/close.  LOCK_RELEASE enters Section 5.5 cleanup and returns only after
the exact owned/displaced proof; SESSION_CLOSE is legal only after
LOCK_RELEASED and all roots are terminal, or after LOCK_REJECTED with no root
or lock handle ever created.  Each later delegated requester is
G-spawned from that record with a fresh endpoint.  Its P15R_TEST_LOCK_DIR, where required,
is G's exact derived private value rather than client input.
P15R_POSSESSION_ROOT_HANDLE is legal only for a method-owned child and its
registered purpose.  Handle zero means no root for a SPAWN template.

The SUITE_173 endpoint may issue SESSION_CREATE, ROOT_CREATE/VALIDATE,
SPAWN, INJECT_EXCHANGE, CLEAN, FOREIGN_AUDIT, LOCK_ACQUIRE/RELEASE, and
SESSION_CLOSE only with an exact existing method and that method's frozen
purpose/trigger ownership; it cannot invent a method or transfer authority.
A delegated endpoint may issue only the subset fixed in its immutable
one-method session.  All subprocess semantics formerly initiated by test_controls or a copied
wrapper use SPAWN.  G alone performs clone3 and binds the new per-worker
endpoint/pidfd/role before CHILD_ADMITTED; the requester blocks on its own
endpoint while G multiplexes the child endpoint and pipes.  Thus a copied
wrapper never creates a descendant and never shares the top-level endpoint.
A generator child receives no RPC endpoint.  A copied wrapper requests its
canonical/mutation generator, contender, or replacement actor only through
the corresponding closed TARGET; target/method/purpose/trigger ownership is
checked before clone3.  Unknown, repeated, cross-purpose, post-clean,
post-session, extra-frame, or malformed requests are exit-class-2 input
failures when they are subject misuse and E_POSSESSION_UNAVAILABLE/E_CLEANUP
when containment state failed; neither can create a new public exit class.

There is one bootstrap creator only.  A copied experiments/reproduce.sh
never creates U1/U2, a cgroup, or a second guardian.  After its unchanged
active-marker, entry-script, copied-package, and isolated-lock checks, it may
enter DELEGATED_TEST_SESSION only with P15R_TEST_CONTEXT=1, its own endpoint
mapped by G to the exact owning method/trigger, and its cwd identity equal to
the retained copied-package record.  It delegates root/lock creation,
generator/contender spawn, exchange, validation, foreign audit, and cleanup
to G.  P21 retains P15R_REPRO_ACTIVE and is rejected before delegated
selection.  P20 and P24 omit that marker only in their frozen copied
sessions.  P22 removes only that marker and asks G for LOCK_CONTENDER against
the already-held ordinary abstract address; EADDRINUSE remains exit 74.
test_rep_009's isolated holder/contender uses the analogous exact targets.
No nested session changes the top-level two-generation or three-copy
aggregate.
P and G retain the exact handled set HUP, INT, QUIT, PIPE, ALRM, TERM, USR1,
and USR2 blocked process-wide and consume it synchronously with signalfd.
No asynchronous handler and no POSIX-shell trap performs unlink, rmdir,
rename, chmod, or truncation.  P forwards one authenticated signal record to
G; G records it pending, closes admission, obtains FROZEN_FINAL followed by
KILL_ISSUED, REAPED, and CGROUP_EMPTY, and only then performs the
state-appropriate retained-capability cleanup.
Signal delivery cannot interrupt bind, CREATED, an exchange, the
quiescence proof, or a destructive sequence.

- UNOWNED performs no lock deletion and finishes private-root cleanup.
- ACQUIRING before bind owns no lock; after bind it closes only the held
  socket and its retained private candidate/receipt.
- ACQUIRING after CREATED uses the same lock_fd cleanup and retains the
  displaced result if replacement occurred.
- OWNED changes once to CLEANING.
- CLEANING continues one idempotent transaction and never starts a second.
- ABSENT performs no deletion.
- DISPLACED_OWNED, DISPLACED_CLEANED, FOREIGN_RETAINED, and ERROR never
  transition to a user-space ABSENT receipt.

After a caught-signal cleanup, G sends SIGNAL_CLEANED and EXIT and exits.  P,
which remains the visible top-level process, reaps G, proves session
populated 0, removes the proved cgroup tree, restores the default action,
unblocks, and re-raises the signal only after all those receipts.  If G sees
P's control EOF it performs no pathname cleanup and exits for
CRASH_TEARDOWN.  If P sees G EOF, a corrupt record, or guardian death, P uses
session cgroup.kill, reaps all descendants, and records CRASH_TEARDOWN without
a private-path ABSENT proof.  P and G STOP merely pause.  KILL is uncatchable:
killing PID 1 destroys its PID-namespace descendants and eventually releases
the private mount; killing P may leave only trusted-administrator cgroup
recovery.  Neither outcome is CLEANING, successful cleanup, or ABSENT.  An
untrusted same-uid peer can therefore deny availability but cannot authorize
a foreign-path deletion.

P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN remains exact: after CREATED and before
OWNED, G queues TERM into the copied-wrapper logical session, runs the
ACQUIRING retained-capability path, preserves E_SIGNAL_ACQUIRE, and returns
the result to test_rep_009.  It does not depend on a shell assignment/helper
window.

### 5.10 Complete v1 operational delta and nonserialization

The following v1 operations are superseded completely:

1. shell mktemp/mkdir ownership of canonical/mutation parents and the
   close-after-generator creator lifetime;
2. P25's close-root-FD then unlink/rmdir sequence;
3. root cleanup by lstat path identity followed by pathname rm/rmdir;
4. host-visible candidate ownership, pathname mkdir lock acquisition, the
   standard-library acquisition helper, its pipe timing, and PREEXISTING
   mkdir authority;
5. cleanup authority inferred from .owner token/path lstat;
6. shell exit/signal traps which delete the lock or roots; and
7. a claim that a token check makes later pathname deletion conditional;
8. ordinary child-side subprocess creation, shared/inherited requester
   endpoints, and any fork-then-cgroup-move placement; all workflow children
   now use G's closed SPAWN templates and atomic placement;
9. cooperative SIGSTOP/SIGCONT or PID-census quiescence; METHOD now requires
   freeze/events plus the no-reference audit, whereas FINAL uses the distinct
   freeze, cgroup.kill, waitid/ECHILD, and populated-zero sequence;
10. v1 PREEXISTING/mkdir as possession authority; EADDRINUSE on the held
    abstract socket is the unchanged class-74 concurrency result and never
    grants filesystem authority; and
11. any cleanup on coordinator/guardian EOF or uncatchable death; those are
    CRASH_TEARDOWN with no private-path ABSENT receipt.

The v1 candidate token tuple and .owner bytes are retained only as a private
receipt; the generator's five capability variables, purpose enum, CLI,
detectors, validation order, and descriptor-relative writes remain.  The
three existing injection variables remain; the five replacement variables
and two RPC fields above are the complete additions.  Descriptor 9 remains
the single generator-call handoff; setup slots 10/11, bootstrap/control
descriptors, the one workers-cgroup handoff, per-worker RPC endpoints,
pidfds, handles, namespace IDs, abstract addresses, candidate/
foreign basenames, credentials, tokens, receipts, cgroup state/epochs, and
RPC request/child/session handles are
internal only.  None is printed, serialized, placed in a CSV/manifest, or
treated as a result artifact.

Public exit classes remain exactly 0, 1, 2, 73, and 74.  Every existing
public S/P detector remains unchanged.  E_POSSESSION_UNAVAILABLE is the sole
new pre-write infrastructure detector and uses class 1; replacement and
cleanup drift retain E_CLEANUP; the existing acquisition signal subfixture
retains E_SIGNAL_ACQUIRE.  CRASH_TEARDOWN is an internal nonserialized
outcome, not a detector or PASS.

The supported-platform limitation, source placement, creator identity,
two-level maps, peer credential check, capability lifetime/inheritance,
read-only project boundary, PID containment, quiescence/reap proof, root/P25
sequence, abstract bind, every lock state, signals, controlled replacements,
detector/exit behavior, operational fields, and final absence/displaced
proof are exhaustive.  Any implementation need for another service, path,
binary, digest, descriptor field, environment field, transition, detector,
or trusted actor is a new design finding and must stop rather than silently
widen this amendment.

## 6. A-M4 — manifest-bound effective-amendment dereference

### 6.1 Canonical final-review block

After this amendment is externally hashed, the fresh independent reviewer
must preserve the complete current review bytes as its prefix and append
exactly one canonical block, in its Section 6, with no blank or commentary
line inside it:

```text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v1]
count=2
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=<exact final v1 SHA-256>
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=<exact final v2 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
```

The v1 value must be
`cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe`.
The v2 value is this file's externally computed final digest; this amendment
does not supply it.

### 6.2 Exact verifier order

The final verifier performs these operations before accepting lifecycle
adjacency:

1. resolve the unchanged manifest `design_review.path` from the held package-
   root capability, require the canonical path
   `notes/phase2_control_design_peer_review.md`, open it once without symlink
   following, and require a regular, nlink-1 file;
2. hash the complete bytes from that same open FD and require the exact
   `design_review.sha256` recorded in the generated manifest for the complete
   post-v2 review; parse those same bytes only after the hash matches;
3. find byte lines exactly equal to the begin/end tags above and require
   exactly one begin, one end, correct nesting, and exactly the five interior
   assignment lines in the printed order;
4. require `count=2`, indices exactly `1,2`, paths exactly v1 then v2, each
   path once, lowercase 64-hex digests, and no malformed, duplicate, extra,
   or unknown key;
5. independently resolve each path relative to the same held package-root
   capability using Linux `openat2` with
   `RESOLVE_BENEATH|RESOLVE_NO_SYMLINKS|RESOLVE_NO_MAGICLINKS` and
   `O_RDONLY|O_CLOEXEC|O_NOFOLLOW`;
6. require each opened object to be the canonical regular nlink-1 file at
   its exact path, read every byte from that FD, independently compute
   SHA-256, and compare it with the block; and
7. only after both hashes match set the internal, nonserialized review-node
   obligation
   `R.effective_amendments=[v1,v2]` and continue adjacency validation.

A read error, path/canonicalization/link/type mismatch, replacement between
resolution and open, short read, hash mismatch, missing/second block,
wrong count/order/path/digest, or extra entry stops validation.  Parsing a
copied digest without opening and hashing both files is failure.

This obligation is internal to the existing review node `R`.  It adds no
manifest field, schema member, authority binding, artifact, lifecycle node,
or edge.  The authoritative manifest surface remains fourteen bindings,
eight nodes, twelve distinct edges, and topological order
`A,D,R,G,I,C,M,V`.

## 7. Effective reproduction and review obligations

The unchanged reproduction arithmetic remains two canonical generations
and three copies.  The only operational clarifications are:

1. entry checks precede the platform/namespace isolation probe;
2. the embedded guardian atomically binds the abstract lock before any
   project write and retains its socket through every root receipt and final
   lock cleanup;
3. all canonical and mutation roots are guardian-created inside the
   private namespace, but the generator CLI, serialized `results/...` paths,
   purpose grammar, and comparison roles remain unchanged;
4. every member deletion is capability-relative and every fixed-entry
   deletion follows the mandatory exclusive-namespace quiescence proof;
5. lifecycle adjacency cannot pass until the manifest-bound review FD has
   yielded the unique ordered v1/v2 block and both amendment files have been
   independently re-hashed; and
6. all coordinator/guardian descriptors, handles, socket names, tokens,
   namespace identifiers, replacement basenames, and receipts are closed or
   destroyed and are never generated bytes.

The mandatory fresh reviewer must independently attack all four primitive
counterfactuals, both exact-one-coordinate clones, every ordinary/failure/
signal/replacement transition, all five replacement subfixtures spanning
generation, P25, ACQUIRING, and OWNED-to-CLEANING,
foreign-object preservation, and the complete review-to-two-amendment
dereference.  Only its append-only `PASS C0/M0/m0` on the externally hashed
effective tuple could support later consideration of an implementation gate.

## 8. A-M1--A-M4 closure self-audit and authorization stop

| Finding | Design closure in this amendment | Frozen-surface effect | Self-result |
|---|---|---|---|
| `A-M1` | exact unparameterized `SG_SCOPE`; primitive-only projections; independent prefix/matrix derivation; expected-class comparison last; four fixed-metadata primitive counterfactuals | same four rows/methods, same 35/35/173 totals | CLOSED_BY_DESIGN |
| `A-M2` | two independent deep-cloned receipts differing in exactly mode or mtime, with singleton-difference preassertion and no ctime/filesystem cause | same `test_rep_010`, class, schema, paths, bytes, and 173 methods | CLOSED_BY_DESIGN |
| `A-M3` | byte-bound two-level-namespace guardian; root-owned cgroup-v2 control; atomic clone placement, freeze/events method gate, final kill/reap/populated proof; atomic abstract-socket possession in one designated netns; retained root/parent capabilities; exact generation, P25, ACQUIRING, and CLEANING replacements | existing reproduce.sh source plus operational-only fields/primitive; six paths, 28 classes, and 173 methods unchanged | CLOSED_BY_DESIGN |
| `A-M4` | manifest-bound final-review read/hash, unique canonical ordered v1/v2 block, independent open/hash of both amendment files, internal `R` obligation | 14 bindings, 8 nodes, 12 edges, schema/key set unchanged | CLOSED_BY_DESIGN |

```text
P15R_CONTROL_DESIGN_AMENDMENT_V2=FROZEN_CANDIDATE
BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
V1_REMEDIATION_GATE_SHA256=98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16
AMENDMENT_V1_SHA256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
FINAL_REVIEW_PREFIX_SHA256=b085df5444fa967056479574d8c75f55f978c7c2fe223c5587f049d36b52e0b3
V2_REMEDIATION_GATE_SHA256=00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705

A_M1_PREDICATE=SG_SCOPE
A_M1_SUPPLIED_CLASS_INPUT=false
A_M1_PRIMITIVE_COUNTERFACTUALS=4
A_M2_EXACT_ONE_COORDINATE_CLONES=2
A_M2_CTIME_CAUSAL_FOR_MODE_MTIME=false
A_M3_POSSESSION=P15R_REPRODUCE_EMBEDDED_POSSESSION_V2
A_M3_USER_NAMESPACE_LAYERS=2
A_M3_UID65534_EXCLUSIVITY=NOT_REQUIRED
A_M3_CLONE_INTO_CGROUP=REQUIRED
A_M3_METHOD_FREEZE_EVENTS=REQUIRED
A_M3_FINAL_KILL_REAP_POPULATED_ZERO=REQUIRED
A_M3_UNQUIESCED_PATH_CHECK_THEN_DELETE=false
A_M3_REPLACEMENT_SUBFIXTURES=5
A_M3_PUBLIC_EXIT_CLASSES_CHANGED=false
A_M4_EFFECTIVE_AMENDMENTS=2
A_M4_INDEPENDENT_AMENDMENT_REHASH=true

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

This self-audit is not the required fresh independent re-review.  No control
may be implemented or run, and no downstream authority changes, until a
separate reviewer reads and hashes the exact `base + v1 + v2` tuple, appends
the authorized canonical closure block and review, and independently reaches
`PASS C0/M0/m0`.
