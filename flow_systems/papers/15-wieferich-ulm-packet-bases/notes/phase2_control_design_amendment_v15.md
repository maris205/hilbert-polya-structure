# Replacement Paper 15 control-design amendment v15

Status: AUTHOR-COMPLETE CANDIDATE; EXTERNAL STABLE RECEIPT AND ONE FRESH
INDEPENDENT APPEND-ONLY COMPLETE REREVIEW REQUIRED
Current historical design-review verdict: PASS_C0_M0_m0 under the unchanged
v14 conditional deployment-model ceiling
Reopened v15 design gap: OPEN_PENDING_FRESH_REREVIEW
Controlling implementation-gate verdict: STOP_DESIGN_REOPEN_REQUIRED
Source, implementation, implementation-review, platform-preflight,
execution, generated-artifact, result, proof, Route, manuscript, release,
archive, and Git authority: none

This amendment is the sole notes-only design delta authorized by
phase2_control_design_remediation_gate_v15.md. It supplies the missing
G-side stable P-lifetime capability using exactly FD12, validation-only
FD13, and immutable fork/COW identity lineage. It makes no PASS claim,
closes no finding by author assertion, accepts no source or platform, and
does not revive implementation gate v4 or ATTEMPT_4.

## Material Passport

- Material type: one versioned static control-design amendment.
- Sole path:
  notes/phase2_control_design_amendment_v15.md.
- Governing gate: regular mode 0644, nlink 1, 1085 lines, 48390 bytes,
  SHA-256
  c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a.
- Exact design start: base plus amendments v1 through v11, v13, and v14;
  v5 remains blocked/no-op provenance and v12 remains absent/skipped.
- Current review: regular mode 0644, nlink 1, 6431 lines, 346453 bytes,
  SHA-256
  2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19.
- Controlling STOP: implementation remediation gate v5, SHA-256
  411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7,
  verdict STOP_DESIGN_REOPEN_REQUIRED.
- Exact delta: P acquires its own pidfd and its initial-proc PID directory
  before L exists, installs them collision-safely at 12 and 13, and passes
  the same open file descriptions plus an immutable identity receipt to L
  and G only through ordinary fork/COW inheritance.
- Minimal lifetime: FD13 is closed and proved absent before PID1_READY;
  FD12 alone remains with G until the normal or P_CRASH terminal.
- No public delta: no new wire form, field, ancillary item, endpoint,
  public coordinate, classifier bit, result, path, service, persistence
  mechanism, schema item, authority binding, DAG node, or DAG edge.
- Finding posture: DESIGN_REOPEN_GAP_STATUS remains
  OPEN_PENDING_FRESH_REREVIEW. Only a later fresh independent zero-finding
  review of externally frozen bytes may decide closure.
- Author-side execution posture: no project source was imported, sourced,
  parsed as executable project code, syntax-checked, probed, or run; no
  generated, cache, temporary, result, lock, manifest, or Git object was
  created.

## 1. Exact authority and unchanged intake

### 1.1 Governing method records

The complete ARS-Codex academic-research-suite skill and routed experiment
workflow were freshly read in full before this sole write. Their
independent-oracle, fixed-observation, hostile-counterexample,
exact-evidence, no-fabrication, fail-closed, and no-run limits govern this
amendment.

| Complete ARS record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | 14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b |
| experiment-agent/WORKFLOW.md | 215 | 11555 | c89cb26ec05ed9facf80301df04ec1d892d74b5c7c68d42afbb2511a7c3268ef |

No method record supplies runtime evidence, finding closure, source
authority, or a review verdict.

### 1.2 Exact active design chain

The base and all thirteen active amendment records were completely read and
re-hashed. These are the exact authoring inputs:

| Record | Lines | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d | effective base |
| amendment v1 | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe | active |
| amendment v2 | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea | active |
| amendment v3 | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b | active |
| amendment v4 | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 | active |
| amendment v5 | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 | active blocked/no-op provenance |
| amendment v6 | 1498 | 80822 | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 | active |
| amendment v7 | 1199 | 60145 | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 | active |
| amendment v8 | 884 | 45610 | e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 | active |
| amendment v9 | 870 | 40366 | 0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829 | active |
| amendment v10 | 1133 | 50487 | d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f | active |
| amendment v11 | 1072 | 49086 | 7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269 | active |
| amendment v13 | 1057 | 48820 | 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27 | active |
| amendment v14 | 1414 | 65752 | b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c | active |

The v14 remediation gate is regular mode 0644, nlink 1, 1665 lines,
84029 bytes, SHA-256
cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292.
It is consumed v14 authority and supplies no v15 write authority.

The current design review's authentic historical verdict is
PASS_C0_M0_m0 for base + v1--v11 + v13 + v14 only. It did not review FD12,
FD13, the P identity receipt, or P_LIFETIME_LEDGER. This author neither
extends that PASS nor predicts the result of the required v15 rereview.

### 1.3 Controlling implementation STOP

The complete controlling implementation records were freshly read:

| Record | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| ATTEMPT_3 implementation peer review | 643 | 37947 | 637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88 | REVISE_C0_M12_m0 |
| implementation remediation gate v4 | 1311 | 62273 | b70dc8d42fbec891dba645160bade6effd177b0118db717de12dba403bddd912 | suspended provenance |
| implementation remediation gate v5 | 733 | 31304 | 411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7 | STOP_DESIGN_REOPEN_REQUIRED |

ATTEMPT_3 M12 requires a surviving G to prove P exit/no-future-producer,
drain P-to-G, reconcile G-to-P outbound receipts, and finalize the existing
v14 terminal classifier. Gate v5 correctly found that the active design
authorized no G-side stable P-lifetime capability:

~~~text
CURRENT_DESIGN_G_SIDE_P_LIFETIME_CAPABILITY=false
CURRENT_DESIGN_FD12_FD13_AUTHORIZED=false
M12_IMPLEMENTATION_ONLY_REPAIR_AUTHORIZED=false
DESIGN_REOPEN_REQUIRED=true
~~~

This amendment answers only that design gap. Gate v5 remains controlling;
ATTEMPT_4 remains unconsumed, suspended, and unavailable. All twelve
implementation findings remain open and no implementation-only repair is
performed here.

### 1.4 Exact six-source quarantine

The six source receipts were rechecked read-only and remain immutable
quarantine, not design evidence:

| Frozen path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| code/generate_controls.py | 1133 | 60497 | 4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020 |
| code/test_controls.py | 1655 | 129574 | c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac |
| code/README.md | 95 | 5267 | 96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee |
| experiments/reproduce.sh | 6270 | 469357 | dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59 |
| experiments/README.md | 226 | 14697 | ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6 |
| results/README.md | 76 | 3221 | 03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c |

~~~text
QUARANTINED_SOURCE_PATHS=6
QUARANTINED_SOURCE_LINES=9455
QUARANTINED_SOURCE_BYTES=682613
SOURCE_USED_AS_DESIGN_AUTHORITY=false
SOURCE_ACCEPTED_AS_IMPLEMENTATION_EVIDENCE=false
SOURCE_MUTATION_COUNT_AFTER_ATTEMPT3=0
ATTEMPT4_SOURCE_MUTATION_COUNT=0
~~~

Immediately before this one Add-File operation, this amendment target was
absent under both ordinary and symlink-aware checks. Amendment v12 was also
absent and remains forbidden/skipped. No review, gate, other amendment,
source, generated, result, cache, temporary, lock, manifest, or Git path is
created or changed by this amendment.

## 2. Exact v15 semantic delta and non-scope

The complete semantic delta is exactly:

1. reserve fixed FD12 as P_SELF_PIDFD and fixed FD13 as
   P_INITIAL_PROC_PID_DIR;
2. acquire both in single-threaded initial-namespace P before L exists;
3. stage the existing source roots and the two new capabilities as one
   collision-safe four-source transaction to targets 10, 11, 12, and 13;
4. cross-bind FD12, FD13, P outer PID, and P starttime in one immutable
   identity receipt inherited only through ordinary fork/COW memory;
5. close P's and L's copies at exact branch cuts, close G's FD13 before
   PID1_READY, and retain only G's FD12 through terminal reconciliation;
6. represent all references and transitions in one private
   P_LIFETIME_LEDGER separate from D-M2 and every existing ledger;
7. add FD12 as a permanent registered non-socket in complete steady-state G
   snapshots without changing any D-M2 tag, form, candidate, or acquisition
   count;
8. use exact FD12 POLLIN readiness only as whole-P-thread-group exit
   evidence and only inside the complete existing v14 P_CRASH guard; and
9. close FD12 last after endpoint duties on normal and P_CRASH terminals.

This amendment adds no actor, process, thread, endpoint, wire record, wire
field, ancillary item, shared persistence, service, path, file, memfd,
mapping, cgroup capability, FD6/7 role, FD10/11 repurpose, FD14 role, or
third persistent P-lifetime capability. It does not change C14 success,
raw17, HC, scientific controls, package controls, schemas, the manifest, or
the DAG.

## 3. Closed FD registry and collision-safe installation

### 3.1 Exact setup/control ABI

The fixed registry is:

| Fixed FD | Exact role | Exact lifetime |
|---:|---|---|
| 10 | existing repository source root | unchanged inherited source lifetime |
| 11 | existing package source root | unchanged inherited source lifetime |
| 12 | P_SELF_PIDFD | P pre-L acquisition; inherited P to L to G; G terminal retained |
| 13 | P_INITIAL_PROC_PID_DIR | P pre-L acquisition; inherited P to L to G; G validation-only and closed before PID1_READY |

FD6 and FD7 remain outside every closed worker FD enum and receive no
persistent role. FD10 and FD11 are not renamed, repurposed, shortened, or
widened. FD12 is not a worker FD, endpoint, source root, cgroup FD, D-M2 row
duplicate, guardian pidfd, or dynamic socket candidate. FD13 is never
terminal retained. There is no FD14 role and no third persistent
capability.

### 3.2 Exact acquisition barrier

P may acquire or stage the four source objects only while:

- P is single-threaded;
- P remains in its initial user, mount, and PID visibility;
- P still owns the trusted outer proc-root capability;
- L does not yet exist;
- no concurrent, signal-handler, lazy, or interleaved FD allocation is
  possible;
- the future clone of L omits CLONE_FILES;
- P-to-L and L-to-G execute no new program; and
- PIDFD_NONBLOCK is not used.

The exact new calls are:

~~~text
P_PID_DEC = canonical outer getpid()
raw_pidfd = pidfd_open(P_PID_DEC, 0)
raw_procdir = openat(trusted_outer_proc_root, ASCII(P_PID_DEC),
                     O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
~~~

Each returned reference is inserted in P_LIFETIME_LEDGER as RAW_ACQUIRED,
with a fresh acquisition serial, before any validation that can fail.
FD_CLOEXEC, exact type, and exact object identity are mandatory. A returned
number alone is never authority.

The four source objects are named R10, R11, R12, and R13 only for this
private staging description. R10 and R11 are the already acquired
repository/package source-root OFDs; R12 is raw_pidfd; R13 is raw_procdir.
The names do not prescribe their raw local FD numbers.

### 3.3 One all-source high-FD staging transaction

The only installation algorithm is:

1. Enter the single allocation barrier and bind one fresh transaction
   acquisition serial plus a distinct per-reference serial.
2. Record all four raw references, their current local integers, exact
   kinds, types, flags, and object identities.
3. In exact target order 10, 11, 12, 13, call
   fcntl(raw_fd,F_DUPFD_CLOEXEC,64). The lower bound is exactly
   max(64,max_target+1)=64. Each successful result is a distinct dynamic
   stage H10, H11, H12, or H13, is ledgered as STAGED before further
   validation, and is checked for FD_CLOEXEC and source identity.
4. Install no low target until all four stages exist and the four
   raw-to-stage identity joins are complete.
5. In exact ascending target order call
   dup3(H10,10,O_CLOEXEC), dup3(H11,11,O_CLOEXEC),
   dup3(H12,12,O_CLOEXEC), and dup3(H13,13,O_CLOEXEC).
6. Immediately record each installed target occupant by acquisition serial.
   If dup3 atomically displaced a raw reference using that same integer,
   mark that raw serial DISPLACED_BY_TARGET and never later close its stale
   integer as though it were still the raw object.
7. Validate each target's fixed number, FD_CLOEXEC, type, status flags, and
   exact object/identity equality with its stage.
8. On success, reverse-close every non-target stage and every still-live
   non-displaced raw reference. After each close, with no intervening FD
   allocation, require F_GETFD=-1 and errno EBADF. The four installed
   targets alone remain.
9. Only after all cleanup and target joins may the transaction enter
   SLOTS_INSTALLED and allow clone L.

Sequential low-number dup3 before all four stages exist is forbidden because
it can overwrite an unstaged source. Reusing a source integer as evidence of
object identity is forbidden.

### 3.4 Per-reference success and common unwind

| Reference/state | Success disposition | Failure/unwind disposition |
|---|---|---|
| R10/R11 raw source roots | stage first; close original if still live; targets 10/11 retain staged OFDs | reverse-close if live; never close a stale integer displaced by target install |
| R12 raw self pidfd | ledger before validation; stage; target 12 retains same OFD | close every actual live raw/stage/target reference by serial; no death claim follows |
| R13 raw procdir | ledger before validation; stage; target 13 retains same OFD | close every actual live raw/stage/target reference by serial; no proc identity claim follows |
| H10/H11/H12/H13 | remain until all targets validate; then reverse-close with immediate EBADF | reverse-close every created stage even if a later stage or install failed |
| installed T10--T13 | remain only after all four target validations and cleanup succeed | close installed targets in reverse installation order before leaving the barrier |
| raw integer equal to 12 or 13 | high stage protects the raw OFD before low install; dup3 displacement transfers the integer occupant to the target serial | mark the raw serial displaced; never issue a later close against its stale integer |
| raw integer at or above 64 | F_DUPFD_CLOEXEC still creates a different free FD at least 64; no numeric ordering inference is allowed | close by serial/liveness, not by comparison with 64 or the raw number |
| low-number ABA possibility | prohibited by the allocation barrier and serial-to-object map | any interleaved allocation, occupant drift, or uncertain identity is ambiguity and E_POSSESSION_UNAVAILABLE |

Every partial acquire, stage, install, target validation, cleanup close, or
EBADF failure enters one common reverse unwind. That unwind:

1. permanently prevents clone L;
2. closes every actually installed target in descending target order;
3. closes every still-live stage in reverse acquisition order;
4. closes every still-live, non-displaced raw reference in reverse
   acquisition order;
5. after each successful live close and with no allocation between calls,
   requires F_GETFD=-1/EBADF;
6. retains all acquisition serials, completed prefixes, displacements,
   actual returned references, close results, and ambiguities in a failure
   tombstone; and
7. ends with E_POSSESSION_UNAVAILABLE and no design row, retry, fallback,
   alternate slot, or second transaction.

An RLIMIT exhaustion or any F_DUPFD_CLOEXEC failure after earlier stages is
handled by this same unwind. A partial dup3 sequence does not become a
partial design state. A close or EBADF ambiguity causes best-effort
containment but never CLOSED_PROVED, SLOTS_INSTALLED, clone authority, or an
exact C14 row.

## 4. Immutable P lifetime identity receipt

### 4.1 Exact P-side fields and acquisition

Before L exists, P binds the two capabilities and P's identity in one
ordinary-memory receipt whose semantic fields are exactly:

~~~text
receipt_domain=P15R-P-LIFETIME-IDENTITY-v15
acquisition_serial
canonical_outer_pid
pidfd_fixed_slot=12
pidfd_FD_CLOEXEC
pidfd_type_and_fstat_identity
pidfd_fdinfo_Pid=canonical_outer_pid
procdir_fixed_slot=13
procdir_FD_CLOEXEC
procdir_st_mode
procdir_st_dev
procdir_st_ino
proc_stat_field22_starttime
~~~

While P is alive and visible in the initial PID namespace, P reads FD12
fdinfo and requires its Pid value to equal P's canonical outer getpid().
P fstats FD13 and requires the exact O_PATH directory identity. Through
that already-open directory it reads P's stat entry and canonically parses
field 22 starttime. The parser handles the parenthesized comm field without
naive whitespace splitting or an ambiguous field shift.

Before publishing the receipt to the future clone image, P revalidates
fixed slots 12/13, FD_CLOEXEC, types, fstat identities, canonical outer PID,
pidfd fdinfo identity, procdir identity, and field-22 starttime as one join.

Whole status or cgroup byte equality is excluded because those bytes can
depend on the reader's user, PID, mount, or cgroup namespace. A child-authored
constant, pathname spelling, stored expected string, or numeric PID without
starttime and capability identity is not P identity.

### 4.2 COW-only lineage

The complete receipt becomes immutable ordinary process memory before clone
L. L and G receive it only through ordinary fork/COW address-space
inheritance. It is not placed in:

- argv or environment;
- the bootstrap channel or authenticated P--G wire;
- SCM_RIGHTS or any ancillary data;
- a file, memfd, shared mapping, service, socket, pathname, or persistent
  store;
- a child registration, evidence record, result, manifest, or generated
  member; or
- an author-side or runtime out-of-band handoff.

L and G may compare their inherited observations with this predecessor
receipt but may not edit it in place, regenerate it from self-authored
expected values, or fill a missing field.

### 4.3 G pre-PID1_READY validation and FD13 disposal

Before PID1_READY, G must:

1. verify that fixed slot 12 is the inherited P_SELF_PIDFD OFD and fixed
   slot 13 is the inherited P_INITIAL_PROC_PID_DIR OFD;
2. verify both fixed numbers, FD_CLOEXEC flags, exact types, fstat
   identities, acquisition serials, and immutable receipt lineage;
3. use FD13 only for its exact pre-death procdir fstat and stat-field-22
   identity join;
4. accept that G's descendant PID-namespace view of FD12 fdinfo may show
   Pid:0; that value is neither mismatch nor life/death evidence;
5. poll exact FD12 with zero timeout and require return 0; any readiness,
   POLLNVAL, POLLERR, call error, ambiguity, or other nonzero result stops
   before PID1_READY; and
6. close FD13, perform no intervening FD allocation, then require
   fcntl(13,F_GETFD)=-1 with errno EBADF before PID1_READY.

FD13 may not traverse fd/, fdinfo/, root, namespace, or another proc subtree
to obtain an endpoint or authority. It may not survive PID1_READY, carrier
scope, a holder freeze, or terminal. A long-lived or traversable FD13 is an
HC-reopening STOP, not a fallback.

## 5. Exact holder, inheritance, and close matrix

### 5.1 Owner-by-phase matrix

| Phase | FD12 holders | FD13 holders | Mandatory transition |
|---|---|---|---|
| P install complete, before clone | P | P | acquisition, staging, and immutable receipt complete |
| short clone-L window | P and L | P and L | ordinary separate FD tables; no CLONE_FILES; no exec |
| P successful clone branch | L | L | P closes 13 then 12; each immediate EBADF |
| short L-fork-G window | L and G | L and G | ordinary non-CLONE_FILES fork; no exec |
| L successful fork branch | G | G | L closes 13 then 12; each immediate EBADF before later work |
| G before PID1_READY | G | G | exact identity validation and FD12 initial poll nonready |
| G identity bound | G | none | FD13 close and EBADF complete |
| carrier/runtime steady state | G only | none | FD12 fixed, nonduplicable, terminal retained |
| unavoidable G-child fork window | G and trusted child transiently | none | child close-only stub removes FD12 |
| child SANITIZED/registered/running | G only | none | child has neither 12 nor 13 |
| normal or P_CRASH terminal after endpoint teardown | none | none | G closes FD12 last and proves EBADF |

P closes its copies on the successful clone-L branch before it can create
the v14 denial child. The P denial child therefore inherits neither FD12 nor
FD13. Its existing first-instruction EP_P and global-endpoint-alias closes
remain exact and are not rewritten as P-lifetime closes.

L retains both descriptors only for its one ordinary fork of G. On the live
L parent branch after successful fork, L closes 13 then 12, proving each
absent before any later non-close action or bootstrap transition. No L retry,
second G, or later L child is authorized.

### 5.2 Exact live close and owner-death semantics

Every live-owner close proof is:

~~~text
close(local_fd) returns 0
no intervening FD allocation
fcntl(local_fd,F_GETFD) returns -1
errno is EBADF
~~~

If an owner actually dies before its close, no survivor may forge a close
return or EBADF receipt. P_LIFETIME_LEDGER records OWNER_DIED_RELEASED only
when appropriate death and holder evidence proves that the owner's
reference was released. A live close ambiguity yields
E_POSSESSION_UNAVAILABLE before an authorized action or terminal crash-only
containment after an action. It never yields CLOSED_PROVED, successful
absence, or an exact row.

### 5.3 G-child first-instruction close stub

Ordinary fork necessarily creates a short kernel-instant child copy of
FD12. FD_CLOEXEC does not prevent that copy, and v15 makes no false
zero-instantaneous-inheritance claim.

Every authorized G child follows this fixed first-instruction order:

1. when the v14 HC item-31 transient EP_G alias is present, close EP_G first
   and complete its existing absence proof;
2. close FD12 next and immediately prove F_GETFD=-1/EBADF;
3. close the already-authorized cgroup/setup transient descriptors; and
4. only then perform any report, barrier, registration, I/O, duplication,
   target, loader, or other non-close instruction.

No child may poll, read, fstat for authority, duplicate, transfer, register,
signal through, call pidfd_getfd on, or retain FD12. FD13 is already absent
before such a child exists. A child cannot reach SANITIZED, registration, or
running while holding 12 or 13.

The exact worker FDSET values are unchanged:

| FDSET | Registered/pre-admission | SOURCE_READY | Target running |
|---|---|---|---|
| STDIO_BARRIER | {0,1,2,8} | {0,1,2,8} | {0,1,2} |
| STDIO_SOURCE_BARRIER | {0,1,2,3,8} | {0,1,2,8} | {0,1,2} |
| STDIO_SOURCE_ROOT_BARRIER | {0,1,2,3,8,9} | {0,1,2,8,9} | {0,1,2,9} |
| STDIO_SOURCE_RPC_AUDIT_BARRIER | {0,1,2,3,4,5,8} | {0,1,2,4,5,8} | {0,1,2,4,5} |

Neither 12 nor 13 enters a token, payload, registered set, SOURCE_READY set,
or running set. FD6 and FD7 remain unlisted and closed.

## 6. Separate private P_LIFETIME_LEDGER

P_LIFETIME_LEDGER is private and nonserialized. It is distinct from:

- v6 PIDFD_LIFETIME_LEDGER, whose subject is exactly CHILD or GUARDIAN;
- every D-M2 row acquisition and unwind ledger;
- HP, HG, HM, MECH, H, and HC;
- C14 and raw17; and
- scientific, package, result, and manifest records.

Its closed monotone state enum is exactly:

~~~text
RAW_ACQUIRED
STAGED
SLOTS_INSTALLED
L_INHERITED
G_INHERITED
G_IDENTITY_VALIDATED
G_PIDFD_ARMED_PROC_CLOSED
P_EXIT_OBSERVED
CLOSED_PROVED
OWNER_DIED_RELEASED
AMBIGUOUS_CRASH_ONLY
~~~

Every entry binds:

~~~text
acquisition_serial
actor
exact_local_fd
kind=P_SELF_PIDFD|P_INITIAL_PROC_PID_DIR
object_identity
receipt_identity
state
~~~

State never moves backward. A local FD integer is never recycled as the
same entry after close or displacement. A failure tombstone retains every
completed prefix and every actual returned raw, staged, installed, inherited,
or close reference. Missing work is never reported complete.

The principal transitions are:

- P's two new returned references enter RAW_ACQUIRED before validation;
- every successful dynamic high duplicate enters STAGED;
- only the completely validated four-target transaction enters
  SLOTS_INSTALLED;
- successful ordinary inheritance records L_INHERITED and G_INHERITED
  separately for the local references actually held by those actors;
- complete G slot/receipt/object validation enters G_IDENTITY_VALIDATED;
- only after that validation, zero-time FD12 nonreadiness, FD13 live close,
  and FD13 EBADF may the joined transaction enter
  G_PIDFD_ARMED_PROC_CLOSED;
- only the exact terminal FD12 poll predicate may enter P_EXIT_OBSERVED;
- only an actual live close/EBADF sequence may enter CLOSED_PROVED;
- actual owner death with sufficient holder/death proof may enter
  OWNER_DIED_RELEASED; and
- uncertain close, identity, holder, or ABA state enters
  AMBIGUOUS_CRASH_ONLY.

For FD13, G's normal terminal ledger endpoint is its pre-ready
CLOSED_PROVED state. For FD12, G retains the armed state until terminal,
optionally records P_EXIT_OBSERVED on the P_CRASH branch, and closes/proves
the descriptor only after endpoint duties. P and L have their own local
close entries and cannot borrow G's result.

These states add no wire field, public lifecycle coordinate, classifier bit,
success predicate, result field, or generated evidence.

## 7. D-M2 and endpoint-custody coupling

### 7.1 Complete steady-state G snapshots

Every complete D-M2 steady-state G FD snapshot after PID1_READY must:

- contain fixed FD12;
- classify 12 as the registered permanent P_SELF_PIDFD non-socket;
- require FD13 absent and retain its separate prior close/EBADF receipt;
- preserve complete set equality between snapshots 1 and 2;
- reject any unregistered extra, replacement, type drift, identity drift,
  or generation drift; and
- permit the canonical raw snapshot bytes to differ from pre-v15 bytes
  because the complete set naturally now contains decimal 12.

The socket selector remains exactly the existing proc-link-text predicate
socket:[DEC]. FD12 is not a socket candidate. The local candidate number 12
is forbidden, and P must never call pidfd_getfd on guardian pidfd target 12.
FD13 is absent and is not a candidate.

FD12 is not inserted into D-M2 row ownership, tag-18 unwind,
CHILD|GUARDIAN PIDFD_LIFETIME_LEDGER, or a dynamically allocated candidate
slot. P_LIFETIME_LEDGER alone owns it. Complete-snapshot tag values may
change naturally, but tag numbers and grammars do not.

The exact counts remain:

~~~text
D_M2_FIXED_TAG_COUNT=21
D_M2_CONTROL_FORM_COUNT=4
D_M2_FRESH_PROC_LEDGER_SLOTS=4
D_M2_CHILD_DUPLICATE_SLOTS=1
D_M2_G_SOCKET_CANDIDATE_SLOTS=N_FROM_SNAPSHOT
D_M2_TAG18_GRAMMAR_CHANGED=false
D_M2_TAG21_ENDPOINT_HOLDER_MATRIX_CHANGED=false
P_SELF_PIDFD_IS_D_M2_ACQUISITION_CANDIDATE=false
~~~

No fifth control form, new tag, new targetfd grammar, permanent row slot, or
pidfd_getfd acquisition is introduced.

### 7.2 HC, endpoint identities, and counts remain exact

~~~text
HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
~~~

FD13 is gone before PID1_READY, carrier scope, and holder freeze. FD12
authorizes only identity checks, initial nonreadiness, terminal polling, and
close/absence. It is not an endpoint reference or alias and authorizes no
endpoint I/O, pidfd_getfd, duplication, SCM_RIGHTS, epoll registration,
io_uring registration, delayed endpoint release, or endpoint custody.
Neither FD enters HP, HG, HM, MECH, H, or HC.

The post-Seal child still closes EP_G before FD12, so HC item 31 is neither
reordered nor expanded. Any FD13 lifetime across PID1_READY or holder
freeze, traversal of its fd/ subtree, FD12 endpoint extraction, duplicate,
registration, transfer, or endpoint I/O invalidates the no-change proof and
is an immediate STOP requiring a fresh HC review. The existing 41/2928
digest may not be silently reused after such a change.

## 8. Linux 5.15 P lifetime and P_CRASH

### 8.1 Exact FD12 terminal poll predicate

G polls one direct target, the exact inherited and identity-bound FD12:

~~~text
pollfd.fd=12
pollfd.events=POLLIN
poll_return=1
(pollfd.revents & POLLIN)!=0
(pollfd.revents & POLLNVAL)==0
(pollfd.revents & POLLERR)==0
~~~

Exact revents equality is forbidden. POLLHUP is not required. Additional
nonfatal readiness, including POLLRDNORM, may coexist. Timeout, EINTR,
return 0, POLLNVAL, POLLERR, call failure, or ambiguity is not P-exit
evidence.

On Linux 5.15, pidfd poll readiness begins only when the target whole thread
group has exited and remains ready through later reap. It proves only whole
thread-group exit. It proves no signal, ordinary-exit distinction, exit
status, core status, first failing thread, wait result, reap result, or exit
cause.

P remains within the inherited single-threaded coordinator axiom. If that
axiom were widened, P_CRASH would still require whole-thread-group
termination. A leader exit with a residual live thread correctly leaves
FD12 nonready.

### 8.2 Forbidden substitute evidence

G is not P's child. G must not:

- call waitid on P or FD12;
- call waitpid or try to reap P;
- treat ECHILD, WNOHANG, or a wait error as P life/death evidence;
- call pidfd_send_signal with signal 0 or any other signal as a liveness
  probe;
- treat EINVAL, EPERM, or signal success as P death;
- read FD12;
- require G-side pidfd fdinfo Pid to equal the outer PID;
- read P task content through FD13 after its pre-ready close;
- reopen /proc/PID_DEC or call pidfd_open(PID_DEC) after the namespace
  transition; or
- use a pathname, status/cgroup byte replay, control EOF alone, proc failure,
  successful procdir fstat, or numeric PID as identity or death.

A live nonchild P can yield ECHILD. Descendant PID-namespace signal
direction can yield EINVAL before liveness is addressed. A dead/reaped P's
already-open procdir can still fstat, and a live P's proc read can fail from
hidepid or permission. None substitutes for FD12 POLLIN.

### 8.3 Exact P_CRASH guard and order

FD12 readiness is necessary but not sufficient. G may classify P_CRASH only
after retaining all twelve facts in this order:

1. the v14 carrier scope has begun;
2. the normal terminal remains incomplete and no already-finalized C14
   success may be revised;
3. the authenticated P--G transport has produced in-scope EOF or loss;
4. P_LIFETIME_LEDGER is at G_PIDFD_ARMED_PROC_CLOSED;
5. the exact FD12 poll predicate enters P_EXIT_OBSERVED;
6. G permanently stops every future in-scope enqueue;
7. the v14 holder/profile ceiling proves no alternate reader or producer,
   and inherited LAUNCHER_REAPED excludes L;
8. G remains the one authenticated survivor with its actual EP_G;
9. G drains P-to-G inbound records one record at a time through every
   queued record to exact EOF;
10. G reconciles all G-to-P endpoint-bound full-return receipts, including
    exact form, direction, complete frame bytes, and one-use identity;
11. existing C14, raw17, winner, all true losing bits, owner evidence,
    P-before-G same-label tie, and tombstone rules run without a new
    coordinate; and
12. G completes the existing endpoint close/absence and holder teardown,
    then closes FD12 last and immediately proves EBADF before exit.

Existing C14/raw17 rules include all queued records, old-form extra
direction bits, committed-carrier predecessor history, one-use identities,
and the same first-cause/tombstone semantics. FD12 contributes no new bit or
coordinate.

EOF while FD12 is nonready is EOF/transport failure or an unreconciled
state, never P_CRASH. Readiness after unique row-15 success is finalized
retains success with no classifier backflow. Readiness without the holder
ceiling, exact EOF drain, or outbound reconciliation proves exit only and
cannot freeze an exact row. P exit before v14 carrier scope is bootstrap
failure and is not forced into the fifteen C14 rows.

### 8.4 Normal terminal

The normal terminal retains v14 success and disposal order. G first
completes all existing endpoint drain, reconciliation, freeze, close, and
holder-teardown duties. It then closes FD12 last and immediately proves
EBADF. A later or already-present FD12 readiness is only the expected
consequence of P exit and has no classifier authority. FD13 is already
absent. No normal or P_CRASH terminal leaves a P-lifetime descriptor in G.

## 9. Frozen algebra, forms, HC, and scientific/package coordinates

### 9.1 C14 and raw17 remain unchanged

The coordinate order remains:

~~~text
C14=(RE,YE,AE,SS,E_PG,E_GP)
~~~

The exact vectors remain:

~~~text
000000 000010 000001 000011
100000 100010 100001 100011
110000 110010 110001 110011
111000 111001
111100
~~~

Rows 1--14 remain failures; row 15, 111100, remains the unique success.
Actual SS enqueue with E_PG=E_GP=0 remains the sole success cut. No initial
poll, terminal poll, procdir validation, close receipt, or private-ledger
state is a C14 coordinate.

The raw predicate declaration order remains exactly:

~~~text
MISSING
MALFORMED
DUPLICATE
REPLAY
WRONG_SESSION
WRONG_G_IDENTITY
WRONG_CGROUP
WRONG_ATTESTATION
WRONG_DIRECTION
WRONG_STATE
REORDERED
PARTIAL
EOF
TIMEOUT
P_CRASH
G_CRASH
TRANSPORT_ERROR
~~~

All seventeen bits are computed independently before winner selection, all
true losing bits remain, and the inherited separate priority permutation and
P-before-G same-label owner tie remain exact.

~~~text
C14_VECTOR_COUNT=15
C14_FAILURE_VECTOR_COUNT=14
C14_SUCCESS_VECTOR_COUNT=1
C14_SUCCESS_VECTOR=111100
C14_ROW14_VECTOR=111001
RAW_CLASSIFIER_PREDICATE_COUNT=17
RAW_BITS_COMPUTED_BEFORE_WINNER=true
ALL_TRUE_LOSER_BITS_RETAINED=true
~~~

### 9.2 Form and FDSET counts

~~~text
WORKER_FDSET_VALUE_COUNT=4
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
ADMIT_FORM_COUNT=1
V15_NEW_WIRE_FORM_COUNT=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
~~~

The plus-three forms remain v9 PRIVILEGE_DROP_RELEASE, v11
GUARDIAN_READY_ACK, and v13 BOOTSTRAP_SEALED. No ACK-of-Seal, ACK-of-ACK,
retry, reconnect, fallback, compatibility form, endpoint handoff, or shared
persistence is added.

### 9.3 Scientific, package, and DAG vector

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

The graph remains nodes A D R G I C M V; chain edges
A->D->R->G->I->C->M->V; and additional edges A->M, D->M, R->M, G->M,
and I->M: exactly eight nodes and twelve distinct edges.

AUTHORITY_BINDINGS=14 is the package binding count and does not become the
active-amendment count. No schema, manifest, proof, Route, or graph byte is
authorized to change here.

## 10. Exact narrow supersessions and clarifications

Only the following predecessor surfaces are superseded or clarified:

1. v2 Section 5.3 step 1 now includes pre-L P acquisition, immutable receipt,
   and the one four-source high-FD staging transaction.
2. v2 Section 5.3 step 2 gives L the bootstrap endpoint plus exact 10, 11,
   12, and 13, and no other retained P descriptor.
3. v2's L/G fork is clarified to omit CLONE_FILES and exec and to use the
   exact P/L close cuts in Section 5.
4. v2 step 7 now requires G receipt/slot validation, FD12 initial
   nonreadiness, FD13 close/EBADF, and the resulting PID1_READY guard.
5. v2 step 10 now requires L's exact 13-then-12 close/EBADF branch after
   forking G.
6. v2 step 11's setup-only-descriptor close sentence receives only the
   narrow terminal-FD12 exception; FD13 remains setup-only and pre-ready
   gone.
7. v3/v4 child FDSET and trusted-stub rules retain the same four FDSET
   values and add only EP_G-first where applicable, then FD12 close before
   non-close work.
8. v6 D-M2 complete G snapshots contain permanent FD12, require FD13 absent,
   exclude local/target 12 from candidate and pidfd_getfd acquisition, and
   use P_LIFETIME_LEDGER without tag/form expansion.
9. v14 terminal reconciliation gains exact G-survivor P-exit/no-future-
   producer evidence and the normal/P_CRASH FD12-last disposal order.
10. v14 endpoint custody treats FD12 as nonendpoint and FD13 as pre-carrier
    gone; HC remains exact only under the restrictions in Section 7.
11. v14 active-count governance permits only a later zero-finding review to
    publish the count-fourteen marker version v13, with amendment v12 still
    absent/skipped.

There is no blanket supersession of v2, v3, v4, v6, or v14. Every
unmentioned predecessor requirement remains exact.

## 11. Twenty-five mandatory hostile pairs and dispositions

| # | Hostile pair or counterexample | Normative v15 disposition |
|---:|---|---|
| 1 | FD6/7 is assigned, or 12/13 collides with a retained raw/source FD | STOP. Persistent roles remain only source 10/11 and P-lifetime 12/13; collision is handled only by the four-source stage transaction. |
| 2 | partial high-FD staging, RLIMIT exhaustion, or sequential dup3 overwrites an unstaged source | Enter the common reverse unwind; do not clone, claim a row, retry, or fall back. |
| 3 | CLONE_FILES or an intervening exec changes inheritance | STOP as outside the authorized P/L/G topology. |
| 4 | pidfd names P-A while procdir or receipt names P-B | Fail the complete identity join before PID1_READY. |
| 5 | the same outer PID has a different field-22 starttime after reuse | Reject; numeric PID alone is not identity. |
| 6 | G sees pidfd fdinfo Pid:0 while P remains alive | Do not reject and do not infer death; inherited lineage plus FD12 poll governs. |
| 7 | authenticated control EOF occurs while FD12 is nonready | Classify EOF/transport failure or retain unreconciled state; never P_CRASH. |
| 8 | FD12 becomes ready after normal row-15 success finalized | Retain success; no classifier backflow is allowed. |
| 9 | waiting on live nonchild P returns ECHILD | ECHILD is no life/death evidence and the wait itself is forbidden. |
| 10 | signal 0 returns EINVAL from PID-namespace direction or EPERM from permission | It is no life/death evidence; the signal probe is forbidden. |
| 11 | P is dead/reaped but the old FD13 still fstats | Fstat does not prove life; conforming FD13 was already closed before PID1_READY. |
| 12 | P is alive but proc reading fails from hidepid or permission | Proc failure does not prove death. |
| 13 | an implementation or review requires POLLHUP | Reject that requirement; POLLIN is the sole required readiness bit. |
| 14 | P's leader exits while another thread remains live | FD12 correctly remains nonready because the whole thread group is the subject. |
| 15 | a G child reaches SANITIZED or registration retaining FD12 | Fail closed; its first-instruction close/EBADF sequence was incomplete. |
| 16 | D-M2 selects FD12 as a socket candidate or adds a duplicate, tag, or form | STOP. FD12 is permanent non-socket state owned by the separate ledger. |
| 17 | FD13 crosses PID1_READY/holder freeze or can traverse fd/ | STOP and reopen HC; validation-only lifetime was violated. |
| 18 | a closed local number is ABA-reused without acquisition-serial identity | Retain ambiguity; claim neither CLOSED_PROVED nor an exact row. |
| 19 | FD12 is ready but the holder ceiling, exact EOF drain, or reconciliation is incomplete | Retain exit-only evidence; do not finalize exact P_CRASH. |
| 20 | P dies before the applicable C14 carrier scope and is forced into a C14 row | Reject that projection and retain bootstrap failure. |
| 21 | P_CRASH is required to state a signal, exit code, or core cause | Impossible from FD12 poll; STOP instead of inventing evidence. |
| 22 | zero instantaneous kernel inheritance is required for every G child | Impossible under ordinary fork; STOP instead of hiding the transient. |
| 23 | the identity receipt moves to env, argv, wire, ancillary data, shared memory/file/service, or persistence | STOP. Immutable ordinary fork/COW lineage is the only bearer. |
| 24 | a new wire form/field, SCM_RIGHTS item, endpoint handoff, reconnect, or second ancillary item appears | STOP as outside v15. |
| 25 | HC item/count/digest, C14 rows, raw17 count, scientific vector, authority bindings, or DAG changes | STOP; separate authority is mandatory and no silent reuse is allowed. |

Items 21 and 22 are explicit infeasibility tests, not implementation
preferences. Additional automatic stops are a third persistent slot,
repurposed 10/11, long-lived or traversable 13, pidfd_getfd target 12,
FD12 endpoint I/O/duplication/registration/transfer, a new shared
service/path, D-M2 tag grammar change, HC recomputation, source use as
design evidence, or project execution.

## 12. Author-side status and successor-marker contract

### 12.1 Findings remain open

Creating this file closes no design or implementation finding:

~~~text
CURRENT_HISTORICAL_DESIGN_REVIEW_VERDICT=PASS_C0_M0_m0
DESIGN_REOPEN_GAP=G_SURVIVOR_MISSING_STABLE_P_LIFETIME_EVIDENCE
DESIGN_REOPEN_GAP_STATUS=OPEN_PENDING_FRESH_REREVIEW
ATTEMPT3_IMPLEMENTATION_REVIEW_VERDICT=REVISE_C0_M12_m0
CONTROLLING_IMPLEMENTATION_GATE_VERDICT=STOP_DESIGN_REOPEN_REQUIRED
ALL_ATTEMPT3_IMPLEMENTATION_FINDINGS_STATUS=OPEN
AUTHOR_SELF_CLOSURE_AUTHORIZED=false
REVIEW_VERDICT_PREJUDGED=false
~~~

Only one fresh independent complete rereview, after an external stable
receipt for this file, may decide the reopened design finding. Its sole
accepting verdict is PASS_C0_M0_m0. This amendment author does not serve as
that reviewer.

### 12.2 Future count-fourteen marker contract

This amendment intentionally contains no active marker delimiter and no
self digest. Only a later zero-finding reviewer may publish the literal
effective-design marker. Its mandatory contract is:

~~~text
marker_version=v13
count=14
amendment_v12=absent_and_skipped
marker_owner=fresh_zero_finding_append_only_reviewer
v15_digest_source=external_stable_regular_file_receipt
~~~

| Marker entry | Required path | Required SHA-256 |
|---:|---|---|
| 1 | notes/phase2_control_design_amendment_v1.md | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe |
| 2 | notes/phase2_control_design_amendment_v2.md | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea |
| 3 | notes/phase2_control_design_amendment_v3.md | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b |
| 4 | notes/phase2_control_design_amendment_v4.md | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 |
| 5 | notes/phase2_control_design_amendment_v5.md | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 |
| 6 | notes/phase2_control_design_amendment_v6.md | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 |
| 7 | notes/phase2_control_design_amendment_v7.md | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 |
| 8 | notes/phase2_control_design_amendment_v8.md | e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 |
| 9 | notes/phase2_control_design_amendment_v9.md | 0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829 |
| 10 | notes/phase2_control_design_amendment_v10.md | d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f |
| 11 | notes/phase2_control_design_amendment_v11.md | 7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269 |
| 12 | notes/phase2_control_design_amendment_v13.md | 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27 |
| 13 | notes/phase2_control_design_amendment_v14.md | b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c |
| 14 | notes/phase2_control_design_amendment_v15.md | the actual external stable v15 SHA-256; never predicted here |

A review that is non-PASS, incomplete, missing a hostile pair, or unable to
authenticate any current byte may not publish that marker.

## 13. Exact authorization matrix

~~~text
AMENDMENT_KIND=VERSIONED_DESIGN_DELTA_V15
AMENDMENT_PATH=notes/phase2_control_design_amendment_v15.md
GOVERNING_GATE_SHA256=c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a
GOVERNING_GATE_KIND=NOTES_ONLY_G_SIDE_P_LIFETIME_DESIGN_REMEDIATION
OTHER_DESIGN_OR_AMENDMENT_PATH_AUTHORIZED=false
AMENDMENT_V12_PRESENT=false
AMENDMENT_V12_SKIPPED=true
V15_OWN_SHA256_PREDICTED=false

CURRENT_EFFECTIVE_AMENDMENT_COUNT_AT_AUTHORING_START=13
SUCCESSOR_EFFECTIVE_AMENDMENT_COUNT_IF_VALID_V15=14
SUCCESSOR_EFFECTIVE_MARKER_VERSION=v13
SUCCESSOR_ACTIVE_AMENDMENTS=v1-v11-plus-v13-plus-v14-plus-v15
SUCCESSOR_MARKER_AUTHORIZED_IN_THIS_AMENDMENT=false

P_SELF_PIDFD_FIXED_SLOT=12
P_INITIAL_PROC_PID_DIR_FIXED_SLOT=13
P_LIFETIME_FIXED_SLOT_COUNT=2
P_LIFETIME_THIRD_PERSISTENT_SLOT_AUTHORIZED=false
FD12_TERMINAL_RETAINED_BY_G=true
FD13_PRE_PID1_READY_ONLY=true
FD13_STEADY_STATE_PRESENT=false
FD13_TERMINAL_RETAINED=false
FD10_FD11_REPURPOSE_AUTHORIZED=false
FD6_FD7_ROLE_AUTHORIZED=false

HIGH_FD_STAGING_SOURCE_COUNT=4
HIGH_FD_STAGING_TARGETS=10,11,12,13
HIGH_FD_STAGING_COMMAND=F_DUPFD_CLOEXEC
HIGH_FD_STAGING_LOWER=64
FIXED_INSTALL_COMMAND=dup3_O_CLOEXEC
CLONE_FILES_AUTHORIZED=false
P_TO_L_TO_G_EXEC_AUTHORIZED=false
PIDFD_NONBLOCK_AUTHORIZED=false

P_IDENTITY_RECEIPT_DOMAIN=P15R-P-LIFETIME-IDENTITY-v15
P_IDENTITY_RECEIPT_TRANSPORT=IMMUTABLE_FORK_COW_MEMORY_ONLY
P_IDENTITY_RECEIPT_WIRE_AUTHORIZED=false
P_IDENTITY_RECEIPT_ENV_AUTHORIZED=false
P_IDENTITY_RECEIPT_SHARED_PERSISTENCE_AUTHORIZED=false
P_IDENTITY_STATUS_CGROUP_BYTE_EQUALITY_REQUIRED=false

P_LIFETIME_LEDGER_SEPARATE=true
P_LIFETIME_LEDGER_SERIALIZED=false
P_LIFETIME_LEDGER_IS_D_M2_ROW_LEDGER=false
P_LIFETIME_LEDGER_IS_CHILD_GUARDIAN_PIDFD_LEDGER=false
P_LIFETIME_LEDGER_IS_C14_COORDINATE=false

P_EXIT_POLL_FD=12
P_EXIT_POLL_RETURN=1
P_EXIT_POLL_REQUIRED_BIT=POLLIN
P_EXIT_POLL_REJECT_POLLNVAL=true
P_EXIT_POLL_REJECT_POLLERR=true
P_EXIT_POLL_REQUIRE_POLLHUP=false
P_EXIT_POLL_REQUIRE_EXACT_REVENTS_EQUALITY=false
P_EXIT_POLL_PROVES=WHOLE_THREAD_GROUP_EXIT_ONLY
P_EXIT_POLL_PROVES_EXIT_STATUS=false
P_EXIT_POLL_PROVES_SIGNAL=false
P_EXIT_POLL_REAPS_P=false
G_WAIT_OR_REAP_P_AUTHORIZED=false
G_ECHILD_AS_P_DEATH_EVIDENCE=false
G_SIGNAL_ZERO_AS_P_DEATH_EVIDENCE=false
G_POSTDEATH_PROC_READ_AUTHORIZED=false
G_NUMERIC_PROC_REOPEN_AUTHORIZED=false

P_CRASH_REQUIRES_NORMAL_TERMINAL_INCOMPLETE=true
P_CRASH_REQUIRES_CARRIER_SCOPE_STARTED=true
P_CRASH_REQUIRES_CONTROL_EOF_OR_LOSS=true
P_CRASH_REQUIRES_FD12_POLLIN=true
P_CRASH_REQUIRES_HOLDER_CEILING=true
P_CRASH_REQUIRES_INBOUND_DRAIN_TO_EXACT_EOF=true
P_CRASH_REQUIRES_OUTBOUND_FULL_RETURN_RECONCILIATION=true
P_CRASH_EOF_ALONE_SUFFICIENT=false
P_CRASH_PIDFD_READY_ALONE_SUFFICIENT=false

G_CHILD_ZERO_KERNEL_INHERITANCE_CLAIM=false
G_CHILD_TRUSTED_STUB_TRANSIENT_FD12=true
G_POST_SEAL_CHILD_CLOSE_ORDER=EP_G_THEN_FD12_THEN_EXISTING_TRANSIENTS
P_DENIAL_CHILD_INHERITS_FD12_FD13=false
WORKER_FDSET_VALUE_COUNT=4
WORKER_FDSET_CHANGE_AUTHORIZED=false

D_M2_STEADY_G_SNAPSHOT_REQUIRES_FD12=true
D_M2_STEADY_G_SNAPSHOT_REQUIRES_FD13_ABSENT=true
D_M2_FD12_SOCKET_CANDIDATE=false
D_M2_PIDFD_GETFD_TARGET12_AUTHORIZED=false
D_M2_FIXED_TAG_COUNT=21
D_M2_CONTROL_FORM_COUNT=4
D_M2_FRESH_PROC_LEDGER_SLOTS=4
D_M2_CHILD_DUPLICATE_SLOTS=1
D_M2_TAG_OR_FORM_CHANGE_AUTHORIZED=false

HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
FD12_IS_ENDPOINT_ALIAS=false
FD13_CROSSES_HOLDER_FREEZE=false
FD12_FD13_ENTER_HP_HG_HM_MECH_H_HC=false
HC_RECOMPUTATION_AUTHORIZED=false

C14_VECTOR_COUNT=15
C14_FAILURE_VECTOR_COUNT=14
C14_SUCCESS_VECTOR_COUNT=1
RAW_CLASSIFIER_PREDICATE_COUNT=17
V15_NEW_WIRE_FORM_COUNT=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4

FRESH_APPEND_ONLY_DESIGN_REREVIEW_AUTHORIZED_ONLY_AFTER_V15_FREEZE=true
FRESH_APPEND_ONLY_DESIGN_REREVIEW_ATTEMPTS_AUTHORIZED=1
DESIGN_REREVIEW_PATH=notes/phase2_control_design_peer_review.md
DESIGN_REREVIEW_REQUIRED_PREFIX_LINES=6431
DESIGN_REREVIEW_REQUIRED_PREFIX_BYTES=346453
DESIGN_REREVIEW_REQUIRED_PREFIX_SHA256=2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19
DESIGN_REREVIEW_PREFIX_REWRITE_AUTHORIZED=false
DESIGN_REREVIEW_ONLY_ACCEPTING_VERDICT=PASS_C0_M0_m0

IMPLEMENTATION_GATE_V5_REMAINS_STOP=true
ATTEMPT4_ADMISSION_AUTHORIZED=false
ATTEMPT4_SOURCE_MUTATION_AUTHORIZED=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
PROJECT_CODE_IMPORT_AUTHORIZED=false
PROJECT_CODE_EXECUTION_AUTHORIZED=false
SHELL_SOURCE_AUTHORIZED=false
PROJECT_AST_OR_SHELL_SYNTAX_CHECK_AUTHORIZED=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
RESULT_REGENERATION_AUTHORIZED=false
CSV_GENERATION_AUTHORIZED=false
MANIFEST_GENERATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
AUTHOR_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0
INDEPENDENT_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0

MANIFEST_SCHEMA_CHANGE_AUTHORIZED=false
DAG_CHANGE_AUTHORIZED=false
PROOF_MODIFICATION_AUTHORIZED=false
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

## 14. Author stop and required external receipt

This file intentionally predicts neither its own line count, byte count, nor
SHA-256. The author makes no independent PASS determination. The reopened
design finding and every ATTEMPT_3 implementation finding remain open until
the separately authorized fresh rereview acts on frozen bytes.

An external coordinator must now verify this exact path as a regular file,
mode, nlink 1, UTF-8/no-NUL, terminal LF, complete line and byte counts, and
SHA-256; make a second complete unchanged read; re-hash the governing v15
gate, base, all thirteen predecessor amendments, current review, ATTEMPT_3
review, implementation gates v4/v5, and all six quarantined source paths;
confirm amendment v12 remains absent/skipped and no extra successor path was
created; and issue the stable receipt outside this file.

No review may begin before that receipt. The sole next design action is the
gate-authorized one fresh independent append-only complete rereview against
the exact preserved 6431-line, 346453-byte,
2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19
prefix. No source, implementation, preflight, execution, generated
artifact, proof, Route, manuscript, release, archive, or Git authority flows
from this author-side candidate.
