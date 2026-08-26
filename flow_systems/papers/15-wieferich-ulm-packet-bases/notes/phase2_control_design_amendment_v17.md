# Replacement Paper 15 control-design amendment v17

Status: **FROZEN CANDIDATE DESIGN AMENDMENT v17 — ALL DESIGN FINDINGS
REMAIN OPEN PENDING ONE FRESH INDEPENDENT COMPLETE REREVIEW**
Date: 2026-08-18 (Asia/Shanghai)
Amendment class: v15 dependent corrigendum under v17 authority recovery
Governing gate:
phase2_control_design_remediation_gate_v17.md at SHA-256
1b51406bd9e66fdac1ffc36deab9ecbbbd8dc0c8595a3566f20f60347d57e4be
Current effective design: base + v1--v11 + v13 + v14 only
Current effective-amendment count: 13
Current candidate-v15 verdict: REVISE_C0_M5_m1
Controlling implementation verdict: STOP_DESIGN_REOPEN_REQUIRED
Source, implementation, review-append, execution, generated-artifact,
result, proof, Route, manuscript, release, archive, and Git authority:
**none**
Universal prime recovery: **OPEN_NOT_AUTHORIZED**

This candidate implements the bounded v17 gate contract. It restores the
active-v2 acquisition cut, gives the four-object transaction a closed
reference algebra, separates successful cleanup from failure unwind,
reduces pidfd fstat to class evidence, and establishes the P--L--G holder
happens-before edges through the existing bootstrap channel and B open file
description. It adds no public wire form, coordinate, schema member,
artifact, manifest member, or DAG edge.

This author makes no PASS claim and closes no finding. Amendment v16 remains
absent and skipped. Only a later reviewer independent of the v15, v16, and
v17 gate/amendment authors may decide whether the exact active-thirteen +
candidate-v15 + candidate-v17 tuple satisfies PASS_C0_M0_m0.

## Material Passport

- **Material type:** one notes-only versioned candidate design amendment.
- **Sole author write:** this amendment-v17 path.
- **Exact formal repair surface:** P15R-V15-M1 through M5 and
  P15R-V15-m1.
- **Exact governance corrections carried:** v16-gate F1
  success-versus-failure semantics and F2 active-v2 R10/R11 acquisition
  order.
- **Preserved mechanism:** fixed FD10/11 source roots, fixed FD12 P
  self-pidfd, validation-only FD13 initial-proc P directory, one
  four-object high-stage transaction, immutable fork/COW receipts, the
  existing five-form inherited bootstrap channel, B-side O_NONBLOCK marker
  plus local SHUT_RD, Linux-5.15 pidfd POLLIN semantics, the complete v14
  P_CRASH guard, and the trusted G-child close-only transient.
- **Private-only additions:** reference/transaction entries and the
  BOOTSTRAP_L_PROC_AUDIT_LEDGER are in-memory, nonserialized,
  nonpersistent, nonendpoint, and outside public DESIGN_SCHEMA,
  MANIFEST_SCHEMA, D-M2 tags, HC, artifacts, and authority bindings.
- **No new public surface:** no new actor, process, endpoint, FD ABI slot,
  wire form, wire field, ancillary item, classifier coordinate, HC item,
  result, public path, persisted file, package/manifest schema member,
  artifact, DAG node, or DAG edge.
- **Review posture:** author-side checks are not independent evidence and
  predict no verdict.
- **Downstream posture:** implementation gate v5 remains controlling;
  ATTEMPT_4 remains unconsumed, suspended, and unavailable.

## 1. Exact authority and unchanged intake

### 1.1 Governing method records

The complete applicable ARS-Codex records were read under their read-only,
independent-oracle, evidence-before-persuasion, hostile-counterexample,
no-fabrication, and no-silent-closure rules:

| Complete record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | 14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b |
| academic-pipeline/WORKFLOW.md | 708 | 48531 | f67d9dea20974328044c503809ffd9bdb27392dc9da2d496c8cf0f1a26806073 |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | 01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800 |

No project source was imported, sourced, parsed as executable project code,
syntax-checked, probed, or run. No generated, result, cache, temporary,
lock, manifest, receipt-file, or Git object was created.

### 1.2 Frozen design and governance chain

The effective predecessor remains the base plus thirteen active amendment
records. Amendment v5 remains active no-op provenance. Amendment v12 is
absent and skipped. Candidate v15 remains non-effective. The immutable v16
gate is defective governance provenance; amendment v16 is absent and
skipped.

| Record | Lines | Bytes | SHA-256 | Role |
|---|---:|---:|---|---|
| base design | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d | effective base |
| amendment v1 | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe | active |
| amendment v2 | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea | active |
| amendment v3 | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b | active |
| amendment v4 | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 | active |
| amendment v5 | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 | active no-op provenance |
| amendment v6 | 1498 | 80822 | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 | active |
| amendment v7 | 1199 | 60145 | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 | active |
| amendment v8 | 884 | 45610 | e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 | active |
| amendment v9 | 870 | 40366 | 0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829 | active |
| amendment v10 | 1133 | 50487 | d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f | active |
| amendment v11 | 1072 | 49086 | 7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269 | active |
| amendment v13 | 1057 | 48820 | 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27 | active |
| amendment v14 | 1414 | 65752 | b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c | active |
| v15 gate | 1085 | 48390 | c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a | consumed candidate authority |
| amendment v15 | 1132 | 52502 | 158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239 | rejected candidate |
| v16 gate | 1007 | 44574 | 063d86fc87118547d2c77544d8b4b20a40dd63d1d41fab6647113767387d5f6c | defective governance provenance |
| v17 gate | 1209 | 51632 | 1b51406bd9e66fdac1ffc36deab9ecbbbd8dc0c8595a3566f20f60347d57e4be | sole current authoring authority |

The active v2, v6, and v14 remediation-gate receipts are:

~~~text
v2_gate_sha256=00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705
v6_gate_sha256=a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00
v14_gate_sha256=cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292
~~~

They are consumed provenance, not amendment-v17 write authority.

### 1.3 Current review and exact open findings

The complete current design review was frozen as:

~~~text
path=notes/phase2_control_design_peer_review.md
type=regular
mode=0644
nlink=1
lines=6965
bytes=375778
sha256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5
~~~

Its final candidate-v15 verdict is REVISE_C0_M5_m1:

| Finding | Open cause this candidate addresses without self-closing |
|---|---|
| P15R-V15-M1 | target 10--13 can contain an unrelated object before destructive dup3 |
| P15R-V15-M2 | the ledger cannot name all objects, roles, or displacement |
| P15R-V15-M3 | transaction and distinct per-reference serials have no unique receipt grammar |
| P15R-V15-M4 | singleton pidfd anon-inode fstat is overstated as target/OFD identity |
| P15R-V15-M5 | local close order lacks a global P--L--G happens-before |
| P15R-V15-m1 | the P/G parent-child direction is reversed |

The combined independent audit of the immutable v16 gate found exactly F1
and F2 and no other defect in the scope-corrected mechanism:

~~~text
F1=SUCCESS_AND_FAILURE_UNWIND_CONTRADICTION
F2=R10_R11_ACQUISITION_ORDER_REGRESSION
V16_GATE_OTHER_FINDING_COUNT=0
~~~

That audit bounds this candidate's authority; it is not a design PASS.

### 1.4 Controlling implementation STOP and source quarantine

| Record | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| ATTEMPT_3 implementation review | 643 | 37947 | 637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88 | REVISE_C0_M12_m0 |
| implementation remediation gate v5 | 733 | 31304 | 411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7 | STOP_DESIGN_REOPEN_REQUIRED |

All twelve implementation findings remain open. ATTEMPT_4 remains
unconsumed, suspended, and unavailable.

| Frozen path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| code/generate_controls.py | 1133 | 60497 | 4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020 |
| code/test_controls.py | 1655 | 129574 | c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac |
| code/README.md | 95 | 5267 | 96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee |
| experiments/reproduce.sh | 6270 | 469357 | dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59 |
| experiments/README.md | 226 | 14697 | ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6 |
| results/README.md | 76 | 3221 | 03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c |

They total 9455 lines and 682613 bytes. Each is regular mode 0644, nlink
one. They remain quarantine, never design evidence.

### 1.5 V16 tombstone and sole target

The v17 gate has global precedence over the unused authority in v16:

~~~text
V16_GATE_ROLE=IMMUTABLE_DEFECTIVE_GOVERNANCE_PROVENANCE
V16_AMENDMENT_ATTEMPT_CONSUMED=false
V16_AMENDMENT_AUTHORITY_TOMBSTONED_BEFORE_CONSUMPTION=true
V16_AMENDMENT_AUTHORITY_AVAILABLE=false
V16_AMENDMENT_PATH_PRESENT=false
V16_AMENDMENT_SKIPPED=true
AMENDMENT_V16_CREATION_AUTHORIZED=false
~~~

Amendment v16 is not deleted, rewritten, revived, or adopted; it never
existed. Its later appearance is STOP. At this author's write boundary,
amendment-v16 and amendment-v17 targets were absent under ordinary and
symlink-aware checks. This amendment-v17 Add-File was the only authorized
write.

## 2. Exact semantic delta and non-scope

This candidate does only the following:

1. restores R10/R11 source-capability acquisition before the root probe and
   leaves only R12/R13 acquisition plus the combined install after complete
   probe removal;
2. preclassifies targets 10--13 before staging and rejects every unrelated
   occupant before destructive action;
3. supplies four object kinds, separate phase/role/disposition/lifetime
   algebras, and distinct transaction/reference identities;
4. separates successful cleanup, which retains T10--T13, from failure
   unwind, which closes the installed prefix;
5. reduces pidfd fstat to class evidence and binds authority through the
   exact P-side receipt and trusted no-replacement lineage;
6. orders P's closes before U1 ACK and orders L's closes before G progresses
   through the already-inherited B OFD marker plus local SHUT_RD;
7. makes P independently audit the parked live L before accept or
   PID1_READY acceptance;
8. corrects the parent-child sentence; and
9. restates only coupled holder, D-M2, HC, P_CRASH, count, and predecessor
   consequences.

No new public actor, process, endpoint, FD slot, wire form, wire field,
ancillary item, pipe, eventfd, socket, shared mapping, memfd, service,
environment bearer, reconnect, retry, fallback, persistence object,
classifier coordinate, result, package schema item, manifest member,
artifact, or DAG edge is added.

For that public-surface prohibition, the exact private transaction entries,
reference fields, immutable fork/COW receipt fields, and
BOOTSTRAP_L_PROC_AUDIT_LEDGER below are expressly authorized. They exist
only in process memory, are never serialized, persisted, sent, placed in
env/argv, written to a repository path, or counted as DESIGN_SCHEMA,
MANIFEST_SCHEMA, D-M2, HC, artifact, authority-binding, or DAG members.
Transient reads beneath the existing trusted outer proc-root create no
public or persistent path.

## 3. F2 normative order: source acquisition and root probe

The exact pre-L order is:

~~~text
P blocks HUP,INT,QUIT,PIPE,ALRM,TERM,USR1,USR2
-> P calls PR_SET_CHILD_SUBREAPER
-> acquire, validate, and retain active-v2 R10
   REPOSITORY_SOURCE_ROOT
-> acquire, validate, and retain active-v2 R11
   PACKAGE_SOURCE_ROOT
-> freeze their exact active-v2 type, mode, uid, device, inode,
   FD_CLOEXEC, status flags, and OFD/object receipts
-> preserve both references without close, replacement, reopen,
   reacquisition, or receipt substitution
-> create the existing cgroup tree
-> create the one existing root-owned root probe
-> perform its exact clone-into/delegation/freeze/thaw/kill checks
-> fully kill and reap it
-> complete duplicate-wait/process-gone proof
-> require its cgroup populated=0
-> remove the exact empty probe cgroup
-> prove no probe or other pre-L child remains
-> revalidate the same retained R10/R11 objects and receipts
-> acquire and ledger R12=P_SELF_PIDFD
-> acquire and ledger R13=P_INITIAL_PROC_PID_DIR
-> enter the one combined R10--R13 transaction in Sections 4--5
-> reach SLOTS_INSTALLED
-> bind the existing abstract control listener
-> create the existing CLOEXEC bootstrap SOCK_SEQPACKET socketpair
-> clone L with the existing exact clone3 record
~~~

The probe cannot inherit FD12 or FD13 because those references do not yet
exist. R10/R11 acquisition is not moved. Only their fixed-target install is
part of the post-probe combined transaction. The active-v2 source receipts
remain the same receipts on both sides of the probe. An equivalent reopen
is not continuity.

The P-only LONG_LIVED_PROC_ROOT may remain open. If it or any unrelated
descriptor occupies 10--13, Section 4 stops before the first staging
duplicate. No alternate target, remap, temporary child, or retry exists.

## 4. M1--M3 closed target and reference algebra

### 4.1 Exact fixed registry

| Fixed FD | Object kind | Exact lifetime |
|---:|---|---|
| 10 | REPOSITORY_SOURCE_ROOT | unchanged active-v2 inherited source lifetime |
| 11 | PACKAGE_SOURCE_ROOT | unchanged active-v2 inherited source lifetime |
| 12 | P_SELF_PIDFD | P installs; L/G inherit; G retains through terminal |
| 13 | P_INITIAL_PROC_PID_DIR | P installs; L/G inherit; G validates then closes pre-PID1_READY |

FD6 and FD7 receive no persistent role. FD10/11 are not renamed,
repurposed, shortened, or widened. FD12 is not a worker FD, endpoint,
source root, cgroup FD, D-M2 row duplicate, guardian pidfd, socket
candidate, or pidfd_getfd target. FD13 is not terminal retained. There is
no FD14 role or third new persistent capability.

The closed object-kind enum is:

~~~text
REPOSITORY_SOURCE_ROOT
PACKAGE_SOURCE_ROOT
P_SELF_PIDFD
P_INITIAL_PROC_PID_DIR
~~~

R10, R11, R12, and R13 name the raw references for those four objects.
Their raw integers are not prescribed by those names.

### 4.2 Acquisition barrier and exact new capability calls

The combined transaction runs only while P is single-threaded, has initial
user/mount/PID visibility, holds the trusted outer proc root, has no L, has
blocked the handled signal set, has no asynchronous allocation path, and
will clone L without CLONE_FILES or exec. PIDFD_NONBLOCK is forbidden.

After the root-probe cut, P performs:

~~~text
P_PID_DEC = canonical initial-namespace getpid()
raw_pidfd = pidfd_open(P_PID_DEC,0)
raw_procdir = openat(trusted_outer_proc_root,ASCII(P_PID_DEC),
                     O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
~~~

Every successful FD return enters a preallocated raw-reference slot before
any validation that can fail. Returned integers alone are never authority.

### 4.3 Target preclassification

After all four raw references and distinct reference IDs are bound, but
before the first F_DUPFD_CLOEXEC, P classifies each current target 10--13
as exactly:

~~~text
VACANT_EBADF
TRANSACTION_RAW_REFERENCE
FORBIDDEN_THIRD_PARTY
~~~

VACANT_EBADF requires F_GETFD=-1 and errno EBADF.
TRANSACTION_RAW_REFERENCE requires the target integer to equal the current
exact_local_fd of one R10--R13 entry and requires exact flags, class, object
kind, and object receipt equality with that entry. Every other open target
is FORBIDDEN_THIRD_PARTY.

LONG_LIVED_PROC_ROOT, listener, bootstrap/control endpoint, signalfd,
cgroup/namespace FD, unrelated pidfd, or any unclassified object at 10--13
causes E_POSSESSION_UNAVAILABLE before staging. It is not overwritten and
is not widened into the transaction. Immediately before each dup3, P
rechecks the target against its frozen applicable classification. Drift
stops before the destructive syscall.

### 4.4 Independent algebras

The closed reference-role enum is:

~~~text
RAW
HIGH_STAGE
FIXED_TARGET
INHERITED_ACTOR_COPY
~~~

The closed reference-disposition enum is:

~~~text
LIVE_UNVALIDATED
LIVE_VALIDATED
DISPLACED_BY_TARGET
CLOSED_PROVED
OWNER_DIED_RELEASED
AMBIGUOUS_CRASH_ONLY
~~~

The closed transaction-phase enum is:

~~~text
OPEN
RAW_SET_BOUND
TARGETS_CLASSIFIED
STAGES_COMPLETE
INSTALLING
TARGETS_VALIDATED
CLEANING
SLOTS_INSTALLED
UNWINDING
ABORT_CLOSED
ABORT_AMBIGUOUS
~~~

The closed P-lifetime phase enum is:

~~~text
P_INSTALLED
L_INHERITED
P_RELEASE_HB_FIXED
G_INHERITED
L_RELEASE_HB_FIXED
G_IDENTITY_VALIDATED
G_PIDFD_ARMED_PROC_CLOSED
P_EXIT_OBSERVED
TERMINAL_CLOSED
~~~

Transaction phase, reference role/disposition, and lifetime phase are
separate fields. DISPLACED_BY_TARGET is a terminal reference disposition,
not a close, transaction phase, or owner-death result. CLOSED_PROVED
requires close return 0 and, with no intervening allocation, immediate
F_GETFD=-1/EBADF.

### 4.5 Exact reference identity

Every raw, high-stage, fixed-target, and inherited-copy entry is:

~~~text
(transaction_serial,
 issuer_actor,
 reference_serial,
 parent_reference_id,
 object_kind,
 reference_role,
 exact_local_fd,
 fd_flags,
 status_flags,
 object_class_receipt,
 object_receipt,
 reference_disposition)
~~~

Its identity is:

~~~text
reference_id=(transaction_serial,issuer_actor,reference_serial)
~~~

transaction_serial is P-owned, monotone, nonzero, and never reused.
reference_serial is nonzero, monotone, and never reused in its actor domain.
parent_reference_id=NONE is legal only for RAW. HIGH_STAGE points to its
RAW; FIXED_TARGET points to its HIGH_STAGE; INHERITED_ACTOR_COPY points to
its actual parent copy.

P pre-reserves deterministic P-to-L and L-to-G copy IDs before the
applicable fork. Each trusted G-child transient uses its existing unique
child-creation serial. Wrap, duplicate, missing parent, actor mismatch, or
cross-object parentage is ABORT_AMBIGUOUS.

The immutable P identity receipt contains, at minimum:

~~~text
receipt_domain=P15R-P-LIFETIME-IDENTITY-v17
transaction_serial
pidfd_raw_reference_id
pidfd_stage_reference_id
pidfd_target_reference_id
procdir_raw_reference_id
procdir_stage_reference_id
procdir_target_reference_id
canonical_outer_pid
outer_pid_starttime_field22
procdir_object_receipt
pidfd_class_fstat_receipt
pidfd_initial_fdinfo_pid
ordinary_fork_no_clone_files=true
exec_occurred=false
~~~

G joins inherited slot 12 separately to pidfd_target_reference_id and slot
13 separately to procdir_target_reference_id. No scalar simultaneously
stands for transaction, pidfd, and procdir identity.

## 5. F1 normative transaction: success is not unwind

### 5.1 Common staging/install prefix

The only transaction prefix is:

1. allocate one transaction_serial and distinct R10--R13 reference IDs;
2. ledger all four raw references and enter RAW_SET_BOUND;
3. classify all targets and enter TARGETS_CLASSIFIED;
4. create H10, H11, H12, H13 in that target order with
   F_DUPFD_CLOEXEC lower 64;
5. ledger each returned stage before validation, require a distinct integer
   at least 64, FD_CLOEXEC, expected flags/class, and exact raw-to-stage
   object join;
6. install no low target until all four stages exist and all four joins
   validate; then enter STAGES_COMPLETE;
7. enter INSTALLING and, after rechecking each target, call
   dup3(H10,10,O_CLOEXEC), dup3(H11,11,O_CLOEXEC),
   dup3(H12,12,O_CLOEXEC), dup3(H13,13,O_CLOEXEC);
8. after each successful dup3, create one FIXED_TARGET reference with a new
   reference ID and parent equal to its stage;
9. if the syscall displaced a TRANSACTION_RAW_REFERENCE at that integer,
   mark that raw DISPLACED_BY_TARGET with target-reference ID and syscall
   serial; and
10. validate all four target numbers, FD_CLOEXEC, flags, class, object
    receipt, and parent joins, then enter TARGETS_VALIDATED.

A failed dup3 does not displace its old target occupant. A
DISPLACED_BY_TARGET raw integer is stale and must never be closed as a raw
reference. Sequential low install before every high stage exists is
forbidden.

### 5.2 Successful cleanup

**SUCCESS IS NOT UNWIND.** Only after all four targets validate:

1. set transaction_phase=CLEANING;
2. reverse-close live H13, H12, H11, H10 by reference identity;
3. reverse-close every still-live nondisplaced raw in reverse acquisition
   order;
4. after each actual close require return 0, no intervening allocation,
   F_GETFD=-1 and errno EBADF, then set that entry CLOSED_PROVED;
5. require each raw exactly CLOSED_PROVED or DISPLACED_BY_TARGET;
6. require each high stage CLOSED_PROVED;
7. require T10, T11, T12, T13 still open, role FIXED_TARGET,
   disposition LIVE_VALIDATED, and joined to their exact stage/object
   receipts; and
8. only then set transaction_phase=SLOTS_INSTALLED and permit clone L.

SLOTS_INSTALLED terminates transaction setup while all four target
references remain live. It does not require every reference to have a
terminal disposition. Successful cleanup never closes an installed target.

### 5.3 Failure unwind

Any failure before SLOTS_INSTALLED enters UNWINDING and permanently forbids
clone L. The sole serial-driven unwind:

1. reverse-closes the actually installed target prefix;
2. reverse-closes every still-live high stage;
3. reverse-closes every still-live nondisplaced raw;
4. never closes a DISPLACED_BY_TARGET stale integer;
5. applies the exact close/immediate-EBADF proof to every actual live close;
   and
6. preserves every reference, completed prefix, classification,
   displacement, syscall serial/result, close result, and ambiguity in the
   failure tombstone.

A clean, complete, unambiguous unwind ends ABORT_CLOSED. Any close, EBADF,
reference, order, target, or liveness ambiguity ends ABORT_AMBIGUOUS and
invokes crash-only containment. Neither terminal permits a design row,
retry, fallback, alternate slot, partial success, or second transaction.

## 6. Immutable P identity, M4 evidence ceiling, and lifetime ledger

### 6.1 P-side authoritative acquisition

While P is alive and initially visible, P binds:

1. pidfd_open(canonical getpid(),0);
2. pidfd fdinfo Pid equal to P_PID_DEC in the initial PID namespace;
3. the trusted initial-proc PID directory;
4. canonical field-22 starttime read through that directory;
5. the exact transaction/reference chains; and
6. the class/type/flags receipts.

R13 must be O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC and join its directory
device/inode/mode receipt. The field-22 parser requires one complete,
canonical, stable record and the same canonical P PID at both bracketing
cuts.

For R12:

~~~text
pidfd_class_fstat_receipt
pidfd_fstat_is_unique_identity=false
pidfd_fstat_is_target_identity=false
pidfd_fstat_is_same_ofd_proof=false
~~~

On Linux 5.15 ordinary pidfds share the singleton anonymous inode. Fstat
supports class/type and flags sanity only. It does not distinguish pidfds,
prove target P, or prove same open file description.

### 6.2 Trusted authoritative lineage

The authoritative P binding is the conjunction of:

1. P-side pidfd_open of canonical P_PID_DEC;
2. P-side fdinfo Pid equality in the initial namespace;
3. initial-proc object plus field-22 starttime;
4. exact transaction and per-reference IDs;
5. raw-to-stage-to-target parent chains;
6. ordinary fork with no CLONE_FILES and no exec;
7. P's U1 close-before-ACK happens-before;
8. L's B marker plus local-SHUT_RD happens-before;
9. P's independent live-L audit;
10. gapless no-close/no-dup/no-replace FD12 policy;
11. close-only disposal of every trusted G-child transient; and
12. terminal polling of that exact lineage-bound FD12.

G has no independent exact OFD comparator. Same-OFD is a static
trusted-program lineage invariant under the existing conditional,
unverified deployment-model ceiling. A wrong live pidfd with the same
anon-inode fstat, G-side fdinfo Pid:0, and initial nonreadiness is not
excluded by those observations alone.

### 6.3 G validation and FD13 disposal

After consuming and closing B but before mount/connect/PID1_READY, G:

1. authenticates the immutable fork/COW receipt and reference chains;
2. requires slots 12 and 13 present at their exact fixed integers with
   FD_CLOEXEC and expected non-socket classes;
3. uses FD13 only for the exact pre-death procdir fstat and field-22
   starttime/object join;
4. treats FD12 fstat only as class evidence and permits G fdinfo Pid:0 from
   PID-namespace visibility;
5. polls exact FD12 with zero timeout and requires return 0 with no
   readiness, error, or ambiguity;
6. enters G_IDENTITY_VALIDATED only after all joins; and
7. closes FD13, performs no intervening FD allocation, requires
   F_GETFD(13)=-1/EBADF, and enters
   G_PIDFD_ARMED_PROC_CLOSED.

FD13 never traverses fd, fdinfo, root, namespace, or another proc subtree.
It never crosses PID1_READY, carrier scope, holder freeze, or a terminal.

### 6.4 Private P_LIFETIME_LEDGER

The P-lifetime ledger is separate from every D-M2 row ledger, endpoint
holder ledger, bootstrap-L-proc ledger, C14/raw17 record, artifact, and
manifest. Its entry algebra is the Section-4 reference tuple plus exact
lifetime_phase for P_SELF_PIDFD and P_INITIAL_PROC_PID_DIR only.

Every transition records actor, reference ID, parent, syscall/event serial,
prior phase, next phase, and evidence receipt. Impossible skips, duplicate
transitions, or missing owners are AMBIGUOUS_CRASH_ONLY. Inherited actor
copies join their exact parent IDs. P and L live closes require close return
0 and immediate EBADF; process death alone may use OWNER_DIED_RELEASED only
when exact owner-death evidence exists.

FD13's G-side normal endpoint is CLOSED_PROVED before PID1_READY. FD12
remains at G_PIDFD_ARMED_PROC_CLOSED until the exact terminal predicate
enters P_EXIT_OBSERVED and terminal disposal enters TERMINAL_CLOSED.

## 7. M5 global holder happens-before through existing bootstrap B

### 7.1 A/B baseline and immutable receipt

The existing bootstrap SOCK_SEQPACKET pair is named:

~~~text
A=P-side endpoint/open-file-description
B=L-to-G inherited endpoint/open-file-description
~~~

This adds no endpoint or form. Bfd is its existing receipt-bound integer and
must not equal 10--13. Before clone L, P freezes:

~~~text
B0=fcntl(B,F_GETFL)
(B0 & O_NONBLOCK)==0
fcntl(B,F_GETFD)==FD_CLOEXEC
B is expected SOCK_SEQPACKET sockfs class
A and B are distinct endpoints/open-file-descriptions
~~~

The immutable B receipt includes B0, Bfd, socket inode/mount lineage,
endpoint role, and CLOEXEC. It passes to L/G only through fork/COW.

P closes its B alias and proves EBADF before processing U1_CREATED. L closes
its A alias and proves EBADF before sending its first U1 record. Thereafter
P alone owns A. After L forks G, L and G have separate FD-table references
to the same B open file description.

Only L's one F_SETFL and one SHUT_RD below may mutate B. P cannot mutate B
through peer A. G and every other actor are forbidden from F_SETFL, FIONBIO,
shutdown, dup, SCM_RIGHTS, replacement, exec, registration, or transfer of
B.

### 7.2 P-to-L release through existing U1 ACK

After successful clone3 parent return, P performs:

~~~text
close P's B alias -> immediate F_GETFD(Bfd)=-1/EBADF
-> close(13)=0 -> immediate F_GETFD(13)=-1/EBADF
-> close(12)=0 -> immediate F_GETFD(12)=-1/EBADF
-> only then process already-queued U1_CREATED
-> write and byte-re-read exact U1 uid_map,setgroups,gid_map
-> send existing exact U1_MAPS_COMMITTED once
~~~

L stays blocked after U1_CREATED until receiving that ACK. Thus:

~~~text
P B/13/12 close receipts
-> U1_MAPS_COMMITTED enqueue and receive
-> all later L U2 actions
-> L fork of G
~~~

Any P close, EBADF, map, re-read, or send failure forbids the ACK and enters
bootstrap containment. The ACK gains no field or form.

### 7.3 Retimed fifth form and L release

L completes the exact U2 uid/gid map writes, re-reads, inner-id checks,
empty-groups check, and U2_ROOT0_MAPPED local state before fork G. It does
not send U2_MAPS_COMMITTED yet. It performs the existing
unshare(CLONE_NEWNS|CLONE_NEWPID) and sole fork of G.

After fork, L parent performs:

~~~text
close(13)=0
-> immediate F_GETFD(13)=-1/EBADF
-> close(12)=0
-> immediate F_GETFD(12)=-1/EBADF
-> fcntl(B,F_GETFL)==B0
-> fcntl(B,F_SETFL,B0|O_NONBLOCK)==0
-> fcntl(B,F_GETFL)==B1
   where (B1 xor B0)==O_NONBLOCK
-> one sendmsg containing the existing exact framed
   U2_MAPS_COMMITTED length prefix and payload
-> return equals the exact full framed length
-> shutdown(B,SHUT_RD)==0
~~~

The marker makes the U2 send nonblocking. EAGAIN, EWOULDBLOCK, EINTR, zero,
short return, or any error is fatal with no retry. U2_MAPS_COMMITTED remains
the fifth and final inherited-bootstrap form, occurs exactly once, remains
L-to-P, and retains its exact payload, fields, framing, and bytes.

O_NONBLOCK alone is not release authority. SHUT_RD alone is not release
authority. Their conjunction after L's close receipts and exact full U2
send is the sole L-origin release. Successful local SHUT_RD is the
wake/release linearization.

If marker publication is followed by U2, SHUT_RD, or validation failure, L
enters fatal containment so G observes HUP. HUP always defeats the normal
branch. Normal release never uses SHUT_RDWR.

### 7.4 G release consumer

Immediately after fork, G may perform only the governed ppoll, F_GETFL,
recvmsg(MSG_DONTWAIT), and final B close/EBADF. It may not validate 12/13,
mount private proc state, connect, send PID1_READY, allocate or close
another FD, mutate B, or perform other work before release.

G blocks with the existing bootstrap deadline:

~~~text
ppoll(B,events=POLLIN|POLLRDHUP)
~~~

Normal release requires all:

~~~text
poll return identifies only B
(revents & POLLIN)!=0
(revents & POLLRDHUP)!=0
(revents & (POLLHUP|POLLERR|POLLNVAL))==0
fcntl(B,F_GETFL)==B1
recvmsg(B,one-byte nonzero buffer,MSG_DONTWAIT)==0
payload_bytes_consumed=0
ancillary_count=0
MSG_TRUNC=false
MSG_CTRUNC=false
~~~

Additional nonfatal bits do not require exact revents equality. POLLHUP
always wins, including when IN/RDHUP/B1 coexist. Timeout, EINTR, error,
positive data, cmsg, truncation, flag drift, or ambiguity is bootstrap
failure, never release or life/death evidence.

After the predicate, G closes B, performs no intervening allocation, and
requires F_GETFD(Bfd)=-1/EBADF. Only then may it validate 12/13, require
FD12 initially nonready, close FD13, mount private state, connect once, or
send PID1_READY.

Peer EOF/close, P death, zero-time FD12 poll, marker alone, SHUT_RD alone,
or an F_GETFL busy loop is never G release authority.

### 7.5 P's independent parked-live-L audit

P receives and validates the exact post-close U2 frame before accept. Before
accept or PID1_READY acceptance, P enters a single-threaded,
signal-controlled allocation barrier, preallocates exactly four private
audit slots, and performs no accept, SCM_RIGHTS receive, signalfd read, or
unlisted allocation.

Using only LONG_LIVED_PROC_ROOT and the receipt-bound L outer PID, P opens
and immediately ledgers:

~~~text
L_PROC_PID_DIR
L_PROC_STAT
L_PROC_FD_DIR
L_PROC_B_FDINFO
~~~

Each private BOOTSTRAP_L_PROC_AUDIT_LEDGER entry is:

~~~text
(audit_epoch,
 acquisition_serial,
 local_fd,
 kind,
 launcher_pidfd_serial,
 l_outer_pid,
 l_starttime_field22,
 fd_flags,
 object_receipt,
 state)
~~~

kind is exactly the four tokens above. state is exactly:

~~~text
RETURNED
VALIDATED
CLOSED_PROVED
AMBIGUOUS_CRASH_ONLY
~~~

Every successful FD return is recorded as RETURNED before validation.
acquisition_serial is P-owned, monotone, nonzero, and never reused. The
ledger is in-memory, nonserialized, pre-accept, P-local, noninherited,
nonendpoint, and outside D-M2's four proc slots and 21 tags.

P first requires launcher pidfd nonready. It brackets two complete canonical
L FD-number snapshots with exact launcher pidfd, outer PID, field-22
starttime, NSpid, credentials, and guardian-cgroup identity checks. The two
complete snapshots must be byte- and set-equal. Parked live L's exact
allowlist is:

~~~text
FD10
FD11
bootstrap Bfd
~~~

FD12/13 must be absent; no extra integer or alias is legal. Bfd must join
the frozen B socket/inode/mount receipt. P parses proc fdinfo descriptor and
file-status flag domains separately: descriptor CLOEXEC must be set, and
the status-flag projection must equal B1. It does not naively compare the
complete proc numeric flags with F_GETFL. It never follows or reopens
/proc/L/fd/Bfd and never duplicates B.

The four transient references remain open through both snapshots and all
bracketing checks, then reverse-close in exact order
L_PROC_B_FDINFO, L_PROC_FD_DIR, L_PROC_STAT, L_PROC_PID_DIR. Each close
requires return 0 and immediate same-number F_GETFD=-1/EBADF without an
intervening allocation. A clean entry becomes CLOSED_PROVED.

L death, pidfd readiness, identity/snapshot drift, missing B, present
12/13, extra FD, lineage/flag mismatch, partial read, close ambiguity, or
an unvisited entry forbids accept and invokes guardian/bootstrap
containment. An ambiguous local reference never yields a normal audit.

### 7.6 L park and final bootstrap disposal

After normal SHUT_RD, L retains B, performs no FD allocation, duplication,
replacement, marker clear, process creation, or normal SHUT_RDWR, and parks
with:

~~~text
poll(B,events=0)
~~~

G never reads bootstrap peer EOF. L may not close B before P's live-L
audit. P retains A through CONTROL_AUTHENTICATED and CGROUP_PREFLIGHTED and
closes A at the original launcher-exit cut. Full peer shutdown gives parked
L POLLHUP. L requires HUP, closes B with immediate EBADF, completes its
unchanged exit duties, and exits. P pidfd-reaps L before LAUNCHER_REAPED.

P may not close A early. On every failure HUP precedence prevents a visible
marker from becoming false normal release.

## 8. Exact holder matrix, inherited copies, and child cut

| Cut | FD12 holders | FD13 holders | Required proof |
|---|---|---|---|
| post-install, pre-clone | P | P | transaction/receipt complete |
| clone-L kernel window | P,L | P,L | no CLONE_FILES; no exec |
| post-U1 ACK receive | L | L | P B/13/12 closes precede ACK |
| fork-G kernel window | L,G | L,G | separate FD tables; shared B OFD |
| B release observed by G | G | G | L closes precede marker, U2, SHUT_RD |
| G identity validated | G | G | class and trusted-lineage joins |
| pre-PID1_READY | G | none | G FD13 close/EBADF |
| steady carrier | G only | none | fixed nonreplaceable FD12 |
| trusted G-child fork instant | G plus child transient | none | unavoidable ordinary-fork copy |
| child SANITIZED/registered | G only | none | close-only stub removed child FD12 |
| terminal after endpoint duties | none | none | G closes FD12 last/EBADF |

P's live-L audit independently verifies L's holder absence before accept; it
does not replace G's B-visible release. The B transition is pre-auth
bootstrap state, not endpoint custody.

P closes its 13/12 copies before U1 ACK. L closes its 13/12 copies before
marker/U2/SHUT_RD. G closes 13 before PID1_READY and retains 12.

Every later trusted G child transiently inherits FD12 under ordinary fork.
Its exact first-instruction close-only order is:

~~~text
close EP_G alias first when applicable -> immediate EBADF
close FD12 next -> immediate EBADF
close every already-authorized setup transient
only then SANITIZED, register, allocate, perform I/O, or run subject work
~~~

The child may not poll, read, duplicate, transfer, register, send through,
pidfd_getfd, or retain FD12. FD13 is already absent. The v14 P denial child
occurs only after P has closed both 12 and 13 and inherits neither.

## 9. D-M2 and endpoint-custody ceiling

### 9.1 D-M2 observable claim

Every complete steady G snapshot after PID1_READY:

- contains fixed FD12;
- requires FD13 absent and preserves its separate prior close receipt;
- requires FD12 FD_CLOEXEC and non-socket pidfd class;
- excludes local/target 12 from socket candidates and pidfd_getfd;
- keeps FD12 out of row ownership, tag-18 unwind, and temporary duplicate
  slots; and
- joins set stability and G fd_generation without calling fstat unique
  identity.

D-M2 may claim:

~~~text
D_M2_PROVES_FD12_SLOT_PRESENT=true
D_M2_PROVES_FD12_CLOEXEC_AND_CLASS=true
D_M2_PROVES_FD12_NONSOCKET=true
D_M2_PROVES_SNAPSHOT_SET_STABILITY=true
D_M2_PROVES_G_FD_GENERATION_STABILITY=true
~~~

It may not claim:

~~~text
D_M2_PROVES_PIDFD_TARGET_P=false
D_M2_PROVES_UNIQUE_PIDFD_OFD_BY_FSTAT=false
D_M2_PROVES_SAME_OFD_BY_FSTAT=false
D_M2_PROVES_INDEPENDENT_LINEAGE=false
~~~

The bootstrap B receipt and private BOOTSTRAP_L_PROC_AUDIT_LEDGER never
enter D-M2.

Exact D-M2/FDSET counts remain:

~~~text
D_M2_FIXED_TAG_COUNT=21
D_M2_CONTROL_FORM_COUNT=4
D_M2_FRESH_PROC_LEDGER_SLOTS=4
D_M2_CHILD_DUPLICATE_SLOTS=1
WORKER_FDSET_VALUE_COUNT=4
~~~

### 9.2 HC noninteraction

B closes in G before the actual P--G control connection and in P/L before
LAUNCHER_REAPED. It is not EP_P, EP_G, endpoint alias, holder-freeze
member, or D-M2 candidate. FD12 is nonendpoint. FD13 is pre-carrier gone.

Therefore the existing static profile remains exactly:

~~~text
HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
PROFILE_HASH_IS_EVIDENCE=false
CURRENT_RUN_PROFILE_ACCEPTED=false
CURRENT_EXECUTION_AUTHORITY=false
~~~

Any B survival into the actual control holder window, FD13 survival past
PID1_READY, FD12 endpoint I/O/duplication/registration/transfer,
pidfd_getfd target 12, new synchronization object, or changed holder set
reopens HC and is outside this amendment. HC is not recomputed here.

## 10. Exact terminal P lifetime and parent-child correction

### 10.1 FD12 terminal poll

G polls one direct target, the exact lineage-bound FD12:

~~~text
pollfd.fd=12
pollfd.events=POLLIN
poll_return=1
(pollfd.revents & POLLIN)!=0
(pollfd.revents & POLLNVAL)==0
(pollfd.revents & POLLERR)==0
~~~

Exact revents equality is forbidden. POLLHUP is not required. Additional
nonfatal readiness such as POLLRDNORM may coexist. Timeout, EINTR, return
zero, POLLNVAL, POLLERR, syscall failure, or ambiguity is not P-exit
evidence.

On Linux 5.15 readiness starts only after the target whole thread group
exits and remains through reap. It proves no signal, exit status, core
status, first failing thread, wait result, reap result, or cause.

### 10.2 Forbidden substitute evidence and correct direction

The normative sentence is:

~~~text
P is not G's child. After L is reaped, G is normally P's
descendant/adopted child in the outer PID namespace because P is the
child subreaper.
~~~

G cannot wait or reap P. It must not use waitid, waitpid, ECHILD, WNOHANG,
wait error, pidfd_send_signal/signal 0, EINVAL, EPERM, signal success,
FD12 read, G fdinfo Pid equality, post-close FD13, reopened /proc/P, a new
pidfd_open, pathname/proc status, EOF alone, successful old-procdir fstat,
or numeric PID as substitute P life/death evidence. P may reap adopted G in
the lawful direction. Pidfd polling itself neither waits nor reaps.

### 10.3 Complete twelve-part P_CRASH guard

FD12 readiness is necessary but insufficient. G may classify P_CRASH only
after retaining all twelve facts in order:

1. v14 carrier scope has begun;
2. normal terminal is incomplete and no finalized C14 success may change;
3. authenticated P--G transport has in-scope EOF or loss;
4. P_LIFETIME_LEDGER is G_PIDFD_ARMED_PROC_CLOSED;
5. exact FD12 poll enters P_EXIT_OBSERVED;
6. G permanently stops every future in-scope enqueue;
7. v14 holder/profile ceiling proves no alternate reader or producer, and
   inherited LAUNCHER_REAPED excludes L;
8. G is the one authenticated survivor with actual EP_G;
9. G drains P-to-G inbound records one record at a time through exact EOF;
10. G reconciles all G-to-P endpoint-bound full-return receipts, including
    form, direction, complete frame bytes, and one-use identity;
11. existing C14, raw17, winner, all true losing bits, owner evidence,
    P-before-G same-label tie, and tombstone rules run without a new
    coordinate; and
12. G completes endpoint close/absence and holder teardown, then closes
    FD12 last and immediately proves EBADF before exit.

B release, B HUP, U2, P's L audit, initial FD12 nonreadiness, or EOF is not
a C14 coordinate, raw17 bit, P-exit proof, or terminal success. EOF with
FD12 nonready is transport/bootstrap failure or unreconciled state, never
P_CRASH. Readiness after finalized row-15 success cannot backflow.
Readiness without holder ceiling, exact drain, or reconciliation proves
exit only. P death before carrier scope is bootstrap failure, not a C14 row.

### 10.4 Normal terminal

Normal success retains v14 row-15 and endpoint disposal order. G completes
all drain, reconciliation, freeze, close, and holder-teardown duties, then
closes FD12 last with immediate EBADF. Later or already-visible readiness is
only the expected consequence of P exit. FD13 is already absent. No normal
or P_CRASH terminal leaves a P-lifetime descriptor in G.

## 11. Frozen public algebra, forms, and package vector

~~~text
C14_COORDINATES=RE,YE,AE,SS,E_PG,E_GP
C14_VECTOR_COUNT=15
C14_FAILURE_VECTOR_COUNT=14
C14_SUCCESS_VECTOR_COUNT=1
C14_SUCCESS_VECTOR=111100
RAW_CLASSIFIER_PREDICATE_COUNT=17
RAW_BITS_COMPUTED_BEFORE_WINNER=true
ALL_TRUE_LOSER_BITS_RETAINED=true

INHERITED_BOOTSTRAP_FORM_COUNT=5
V17_NEW_WIRE_FORM_COUNT=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
ADMIT_FORM_COUNT=1
~~~

The inherited bootstrap forms remain exactly, in printed order and
cardinality one:

~~~text
L->P U1_CREATED
P->L U1_MAPS_COMMITTED
L->P OUTER_IDS_READY
P->L OUTER_IDS_ATTESTED
L->P U2_MAPS_COMMITTED
~~~

Only the fifth form's send cut moves. B marker and local SHUT_RD are private
kernel/OFD transitions, not records or forms.

The scientific/package vector remains:

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
~~~

AUTHORITY_BINDINGS=14 is a package binding count, not an amendment count.

## 12. Exact narrow supersessions

This amendment supersedes or clarifies only:

1. v15 Sections 3 and 6 for target preclassification, object kinds,
   reference roles/dispositions, transaction/lifetime phases, and serial
   grammar;
2. v15 identity fields by separating transaction, pidfd, and procdir
   reference IDs;
3. v15 pidfd fstat language by limiting it to class sanity;
4. v15 holder matrix/local-order inference with the U1 and B-OFD
   happens-before edges plus P's parked-live-L audit;
5. v15 wait rationale with the correct P-is-not-G's-child sentence;
6. active-v2 step 1 by preserving R10/R11 acquisition before root probe and
   moving only R12/R13 acquisition plus the combined fixed install after
   complete probe removal;
7. active-v2 step 2 with exact A/B alias closure and P B/13/12-before-U1;
8. active-v2 step 5 by retaining U2 map work pre-fork while moving the sole
   U2 send post-fork/post-L-close;
9. active-v2 steps 6--7 by making B release consumption G's first work,
   closing G B before identity/connect/ready, and requiring P audit before
   accept;
10. active-v2 bootstrap close by retaining L B under local SHUT_RD until
    P's original post-auth/preflight A close;
11. active-v2 step 10 with L final B close/EBADF, exit, and P reap before
    LAUNCHER_REAPED;
12. active-v6 D-M2 with FD12 class/set/generation ceiling and separate
    private ledgers;
13. active-v14 terminal/HC only at the exact pre-carrier cuts above;
14. active-v14 count governance so only a joint v15+v17 zero-finding review
    can publish count 15;
15. defective-v16 Section 3 with the Section-3 acquisition order here; and
16. defective-v16 Section 4.4 with the Section-5 success/failure split here.

There is no blanket supersession of v2, v6, v14, v15, or v16. V16 is
defective governance provenance, not a candidate. Every unmentioned active
obligation remains exact.

## 13. Fifty-five mandatory hostile cases

The later fresh reviewer must independently attack at least every case. The
author-side disposition below is a normative candidate rule, never a review
result.

| # | Hostile case | Normative candidate disposition |
|---:|---|---|
| 1 | root probe begins before R10/R11 acquisition | active-v2 order violation; STOP |
| 2 | R10/R11 is reopened or reacquired after probe | receipt-continuity failure; STOP |
| 3 | R12 or R13 exists while root probe is live | holder-contract failure |
| 4 | combined transaction begins while probe/pre-L child survives | STOP before staging |
| 5 | v17 blanket-supersedes v2 step 1 | authority excess |
| 6 | target 12 is LONG_LIVED_PROC_ROOT | STOP before staging; never overwrite |
| 7 | target 13 is listener/bootstrap/signalfd | same STOP |
| 8 | target classified then drifts | recheck fails before dup3 |
| 9 | target is exact R12/R13 raw | high stage protects it; successful dup3 records displacement |
| 10 | dup3 fails | old occupant remains; no displacement claim |
| 11 | code closes a displaced stale integer | forbidden; it could close the new target |
| 12 | R10/R11 lacks object kind | schema failure |
| 13 | stage/target/inherited copy lacks role | schema failure |
| 14 | transaction and two capabilities share one serial | receipt ambiguity |
| 15 | post-fork actor IDs collide | actor-qualified identity failure |
| 16 | success cleanup closes any T10--T13 | nonaccepting |
| 17 | SLOTS_INSTALLED has fixed target CLOSED_PROVED | nonaccepting |
| 18 | SLOTS_INSTALLED has live raw or stage | incomplete success cleanup |
| 19 | partial failure leaves installed target open | incomplete failure unwind |
| 20 | failure cleanup closes DISPLACED_BY_TARGET stale integer | forbidden |
| 21 | success enters UNWINDING | phase contradiction |
| 22 | P sends U1 ACK before closing B/13/12 | ACK-guard failure |
| 23 | G runs before L parent | G remains blocked in ppoll |
| 24 | B initially has O_NONBLOCK | baseline failure before clone |
| 25 | Bfd equals 10--13 | registry-collision STOP |
| 26 | actor other than L mutates B flags or shutdown | forbidden mutation |
| 27 | L sets marker before closing 13/12 | release-state violation |
| 28 | marker alone is release | reject; marker+SHUT_RD/no-HUP conjunction required |
| 29 | L sends U2 before marker or retries | state/cardinality failure |
| 30 | nonblocking U2 send is short/EAGAIN/EINTR | fatal; no retry |
| 31 | L uses normal-path SHUT_RDWR | HUP/failure, never normal release |
| 32 | P dies before marker | HUP precedence; no normal release |
| 33 | P dies after marker before SHUT_RD | HUP precedence; no normal release |
| 34 | HUP appears with IN/RDHUP and B1 | HUP wins |
| 35 | G uses F_GETFL spin or peer EOF as authority | forbidden |
| 36 | G writes/clears marker or calls shutdown | forbidden |
| 37 | recvmsg yields data/cmsg/truncation | bootstrap failure |
| 38 | G validates/connects before B close/EBADF | state violation |
| 39 | P accepts before U2/live-L audit | authentication-guard failure |
| 40 | L fdinfo flags compare naively to F_GETFL | reject mixed flag domains |
| 41 | live L snapshot contains 12 or 13 | no accept; containment |
| 42 | live L snapshot has extra alias | no accept; containment |
| 43 | L dies or identity drifts during audit | no accept |
| 44 | L closes B before P audit | allowlist failure |
| 45 | wrong pidfd shares anon-inode fstat | fstat cannot prove target |
| 46 | wrong live pidfd also shows Pid:0 and nonready | only trusted lineage may exclude it |
| 47 | D-M2 says fstat proves P/same OFD | overclaim; nonaccepting |
| 48 | G waits P and uses ECHILD as death | forbidden |
| 49 | FD13 survives PID1_READY in any actor | HC-reopening STOP |
| 50 | FD12 ready after finalized row-15 success | no classifier backflow |
| 51 | FD12 ready without holder/EOF/drain/reconciliation | exit-only evidence |
| 52 | B enters EP_P/EP_G, D-M2, or HC | scope violation |
| 53 | form count, C14/raw17, package vector, or DAG changes | separate authority required |
| 54 | amendment v16 appears or enters candidate tuple | tombstone violation; STOP |
| 55 | v15 or v17 activates alone | partial activation forbidden |

Missing a case, weakening HUP precedence, closing a successful fixed target,
moving R10/R11 acquisition, accepting a public/private scope leak, or using
a timeout, plausible schedule, comment, hash, or self-authored constant
instead of exact evidence is nonaccepting.

## 14. Author status, joint marker contract, and authority stop

### 14.1 No author-side closure

Creating this file closes no finding:

~~~text
CURRENT_DESIGN_REVIEW_VERDICT=REVISE_C0_M5_m1
P15R_V15_M1_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
P15R_V15_M2_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
P15R_V15_M3_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
P15R_V15_M4_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
P15R_V15_M5_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
P15R_V15_m1_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
V16_F1_STATUS=CANDIDATE_CORRECTION_PENDING_REREVIEW
V16_F2_STATUS=CANDIDATE_CORRECTION_PENDING_REREVIEW
AUTHOR_SELF_CLOSURE_AUTHORIZED=false
REVIEW_VERDICT_PREJUDGED=false
~~~

This amendment is not an independent review and does not authorize a review
append. The frozen v17 gate alone governs whether one later fresh reviewer
may append after an external stable receipt for this file.

### 14.2 Joint-activation marker contract

Neither this amendment nor its gate makes v15 or v17 effective. Only a later
PASS_C0_M0_m0 reviewer may publish:

~~~text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v13]
count=15
entries 1..11 = amendments v1..v11 at frozen hashes
entry 12 = amendment v13 at 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27
entry 13 = amendment v14 at b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c
entry 14 = amendment v15 at 158865dfe0235f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c
entry 15 = amendment v17 at its external stable SHA-256
amendment v12 = absent and skipped
amendment v16 = absent and skipped
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
~~~

The entry-14 digest must be the actual frozen amendment-v15 digest:

~~~text
158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239
~~~

The preceding displayed marker template's entry-14 line is nonauthoritative
if it differs from that exact digest; the later reviewer must use the exact
digest immediately above and the v17-gate contract. This amendment contains
no active marker delimiter and predicts no self digest.

Marker version v13 is next unused. Count 15 counts actual active amendment
records, not a contiguous version range. Partial activation, v15-only
activation, and v17-only activation are forbidden. A non-PASS review
publishes no marker and leaves count 13.

### 14.3 Final authorization matrix

~~~text
AMENDMENT_KIND=V15_DEPENDENT_CORRIGENDUM_V17
AMENDMENT_PATH=notes/phase2_control_design_amendment_v17.md
GOVERNING_GATE_SHA256=1b51406bd9e66fdac1ffc36deab9ecbbbd8dc0c8595a3566f20f60347d57e4be
V17_OWN_SHA256_PREDICTED=false
V17_EFFECTIVE=false
CURRENT_EFFECTIVE_AMENDMENT_COUNT=13
SUCCESSOR_EFFECTIVE_COUNT_ONLY_IF_JOINT_PASS=15
SUCCESSOR_EFFECTIVE_MARKER_VERSION=v13
PARTIAL_ACTIVATION_AUTHORIZED=false
V15_ONLY_ACTIVATION_AUTHORIZED=false
V17_ONLY_ACTIVATION_AUTHORIZED=false

V16_GATE_SHA256=063d86fc87118547d2c77544d8b4b20a40dd63d1d41fab6647113767387d5f6c
V16_AMENDMENT_ATTEMPT_CONSUMED=false
V16_AMENDMENT_AUTHORITY_AVAILABLE=false
V16_AMENDMENT_PATH_PRESENT=false
V16_AMENDMENT_SKIPPED=true
AMENDMENT_V16_CREATION_AUTHORIZED=false

R10_R11_ACQUIRED_BEFORE_ROOT_PROBE=true
R10_R11_ACTIVE_V2_RECEIPTS_PRESERVED=true
R12_R13_ACQUIRED_BEFORE_ROOT_PROBE=false
ROOT_PROBE_INHERITS_FD12_FD13=false
FOUR_OBJECT_TRANSACTION_BEGINS_AFTER_ROOT_PROBE_REMOVAL=true
FD10_FD11_ACQUISITION_ORDER_MOVED=false

TARGET_PRECLASSIFICATION_REQUIRED=true
TARGET_PRECLASSIFICATION_TARGETS=10,11,12,13
THIRD_PARTY_TARGET_OVERWRITE_AUTHORIZED=false
TRANSACTION_OBJECT_KIND_COUNT=4
REFERENCE_ROLE_COUNT=4
REFERENCE_DISPOSITION_COUNT=6
TRANSACTION_AND_REFERENCE_SERIALS_DISTINCT=true

SUCCESS_IS_UNWIND=false
SUCCESS_CLEANUP_CLOSES_FIXED_TARGETS=false
SLOTS_INSTALLED_FIXED_TARGET_DISPOSITION=LIVE_VALIDATED
FAILURE_ONLY_ENTERS_UNWINDING=true
FAILURE_UNWIND_CLOSES_INSTALLED_PREFIX=true
FAILURE_UNWIND_CLOSES_DISPLACED_STALE_INTEGER=false

P_CLOSE_B_FD13_FD12_PRECEDES_U1_ACK=true
U2_MAPS_COMMITTED_CARDINALITY=1
U2_MAPS_COMMITTED_SEND_RETRY_AUTHORIZED=false
BOOTSTRAP_B_RELEASE_MARKER=O_NONBLOCK
BOOTSTRAP_B_RELEASE_WAKE=LOCAL_SHUT_RD
G_RELEASE_REJECTS_POLLHUP=true
P_LIVE_L_FDINFO_ALLOWLIST_AUDIT_REQUIRED=true
P_ACCEPT_BEFORE_L_AUDIT_AUTHORIZED=false

PIDFD_FSTAT_PROVES_CLASS_ONLY=true
PIDFD_FSTAT_PROVES_TARGET=false
PIDFD_FSTAT_PROVES_SAME_OFD=false
PARENT_CHILD_CORRECT_SENTENCE=P_IS_NOT_GS_CHILD

INHERITED_BOOTSTRAP_FORM_COUNT=5
V17_NEW_WIRE_FORM_COUNT=0
D_M2_FIXED_TAG_COUNT=21
WORKER_FDSET_VALUE_COUNT=4
HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
HC_RECOMPUTATION_AUTHORIZED=false

CONTROLLING_IMPLEMENTATION_GATE_VERDICT=STOP_DESIGN_REOPEN_REQUIRED
ATTEMPT4_UNCONSUMED=true
ATTEMPT4_SUSPENDED=true
ATTEMPT4_AVAILABLE=false

DESIGN_REREVIEW_AUTHORIZED_BY_THIS_AMENDMENT=false
CONTROL_SOURCE_EDIT_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
PROJECT_CODE_IMPORT_AUTHORIZED=false
PROJECT_CODE_EXECUTION_AUTHORIZED=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
RESULT_REGENERATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false

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

This author stops after this one Add-File. An external coordinator, not this
self-referential file, must compute and freeze its actual regular-file type,
mode, nlink, lines, bytes, UTF-8, terminal-LF, CR/NUL result, and SHA-256;
perform two complete unchanged reads; reauthenticate the v17 gate, current
review, v15/v16 provenance, active chain, implementation STOP/review, and
six-source quarantine; and confirm amendment v16 remains absent. Any drift,
unexpected successor, symlink, hardlink, nonregular object, predicted self
digest, or post-receipt edit is STOP.
