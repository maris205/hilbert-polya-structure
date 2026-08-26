# Replacement Paper 15 control-design remediation gate v17

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v17 ONLY, FOLLOWED BY
ONE FRESH INDEPENDENT APPEND-ONLY COMPLETE DESIGN REREVIEW**
Date: 2026-08-18 (Asia/Shanghai)
Gate class: notes-only v16-authority recovery and v15 dependent-corrigendum
governance
Current effective design verdict: PASS_C0_M0_m0 for
base + v1--v11 + v13 + v14 only
Candidate-v15 review verdict: REVISE_C0_M5_m1
Controlling implementation-gate verdict: STOP_DESIGN_REOPEN_REQUIRED
Current effective-amendment count: 13
Source, implementation, implementation-review, platform-preflight,
execution, generated-artifact, result, proof, Route, manuscript, release,
archive, and Git authority: **none**
Universal prime recovery: **OPEN_NOT_AUTHORIZED**

This gate has global precedence over the unconsumed amendment authority in
the immutable defective v16 gate. It tombstones that authority before use:
amendment v16 must remain absent and skipped. It authorizes only one later
notes-only amendment v17 and, after that file has an external stable receipt,
one fresh independent append-only complete design rereview.

V17 is a dependent corrigendum to non-effective candidate v15. Only a later
PASS_C0_M0_m0 review of the exact base + active-thirteen + candidate-v15 +
candidate-v17 tuple may activate v15 and v17 jointly and publish count 15.
Candidate v16 is not in that tuple. Any other review result leaves the active
tuple and count exactly unchanged.

## Material Passport

- **Material type:** one bounded design-remediation governance gate.
- **Sole gate-author write:** this v17 gate path.
- **Frozen adverse design review:** REVISE_C0_M5_m1 for candidate v15.
- **Frozen v16 governance record:** immutable defective provenance at exact
  SHA-256
  063d86fc87118547d2c77544d8b4b20a40dd63d1d41fab6647113767387d5f6c.
- **Combined independent v16-gate audit set:** exactly F1 and F2, with no
  other finding. F1 is the success/failure-unwind contradiction in v16
  Section 4.4. F2 is the R10/R11 acquisition-order regression in v16
  Section 3.
- **Authority recovery:** the v16 amendment attempt was never consumed;
  amendment v16 is absent; its creation authority is tombstoned, unavailable,
  and skipped rather than reused.
- **Exact v17 repair surface:** candidate-v15 findings P15R-V15-M1 through
  M5 and P15R-V15-m1 under the scope-corrected v16 mechanism, plus exact F1
  success/failure semantics and exact F2 active-v2 acquisition order.
- **Preserved mechanism:** fixed FD12 P self-pidfd; validation-only FD13
  initial-proc P directory; four-object high staging; immutable fork/COW
  receipt; Linux-5.15 POLLIN whole-thread-group-exit semantics; the complete
  v14 P_CRASH guard; G-child close-only transient; and the existing bootstrap
  B-side shared-OFD marker plus local SHUT_RD barrier.
- **No new public surface:** no new actor, endpoint, FD slot, wire form,
  field, ancillary item, shared persistence, classifier coordinate, HC item,
  schema member, artifact, manifest member, DAG node, or DAG edge.
- **Finding posture:** this gate closes no design or implementation finding
  and predicts no review verdict.
- **Downstream posture:** implementation gate v5 remains controlling;
  ATTEMPT_4 remains unconsumed, suspended, and unavailable.

## 1. Exact method, authority, and frozen intake

### 1.1 ARS-Codex integrity boundary

The gate author completely read the governing ARS-Codex router, academic
pipeline workflow, and reviewer workflow. Their read-only-review,
independent-oracle, evidence-before-persuasion, fixed-observation,
hostile-counterexample, no-fabrication, and no-silent-closure rules govern
this one notes-only action.

| Complete ARS record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | 14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b |
| academic-pipeline/WORKFLOW.md | 708 | 48531 | f67d9dea20974328044c503809ffd9bdb27392dc9da2d496c8cf0f1a26806073 |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | 01422d386ac9a42cbc7a938b2ce9c461c571cebe38cc1fb74a4893c9bb2e800 |

No project source was imported, sourced, parsed as executable project code,
syntax-checked, probed, or run. No generated, result, cache, temporary, lock,
manifest, or Git object was created.

### 1.2 Effective design chain and candidate records

The currently effective tuple remains the base plus thirteen active
amendments. Amendment v5 is active no-op provenance. Amendment v12 remains
absent and skipped. Candidate v15 remains non-effective. Amendment v16 is
absent and is now skipped by this gate.

| Record | Lines | Bytes | SHA-256 | Present role |
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
| v15 remediation gate | 1085 | 48390 | c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a | consumed candidate authority |
| amendment v15 | 1132 | 52502 | 158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239 | rejected candidate; not effective |
| v16 remediation gate | 1007 | 44574 | 063d86fc87118547d2c77544d8b4b20a40dd63d1d41fab6647113767387d5f6c | immutable defective governance provenance |

The active v2, v6, and v14 remediation gates remain consumed provenance at,
respectively:

~~~text
v2_gate_sha256=00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705
v6_gate_sha256=a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00
v14_gate_sha256=cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292
~~~

They supply no v17 write authority.

### 1.3 Current complete review and exact v15 findings

The current design review is a regular mode-0644, nlink-one file:

~~~text
path=notes/phase2_control_design_peer_review.md
lines=6965
bytes=375778
sha256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5
~~~

Its v14 PASS remains historical evidence for the active-thirteen tuple. Its
final v15 block has exact verdict REVISE_C0_M5_m1:

| Finding | Exact open cause |
|---|---|
| P15R-V15-M1 | destructive dup3 can silently remove an unrelated target-10--13 occupant |
| P15R-V15-M2 | the closed ledger cannot name all four object kinds, reference roles, or displacement |
| P15R-V15-M3 | transaction and distinct per-reference serials collapse into one ambiguous receipt scalar |
| P15R-V15-M4 | singleton anon-inode pidfd fstat is overstated as exact target/OFD identity |
| P15R-V15-M5 | local closes do not establish P--L--G global holder happens-before |
| P15R-V15-m1 | the P/G parent-child direction is reversed |

V15 is not effective. No effective marker was appended for it. The active
count is still 13.

### 1.4 Exact v16-gate audit and recovery decision

Two fresh independent read-only hostile audits authenticated the exact v16
gate and amendment-v16 absence. Their combined finding set is exactly:

| Audit finding | Exact defect | Recovery requirement |
|---|---|---|
| F1 | v16 Section 4.4 lines 359--369 says both that targets survive success and that success uses an unwind which closes installed targets; it also requires every reference to have a terminal success disposition although fixed targets must remain live | separate successful cleanup from failure unwind; keep T10--T13 LIVE_VALIDATED on success |
| F2 | v16 Section 3 lines 189--198 moves acquisition of all four objects after root-probe removal, contradicting active v2's pre-probe R10/R11 acquisition; v16's own supersession scope moved only FD12/13 | restore R10/R11 acquisition before the probe; acquire R12/R13 only after complete probe removal; then run one combined four-object transaction |

Both audits found no separate defect in the scope-corrected M1--M5/m1
mechanism, the B-side O_NONBLOCK plus local-SHUT_RD release, HUP precedence,
live-L audit, pidfd evidence ceiling, counts, HC boundary, or downstream
authority. That bounded no-additional-finding result is recovery-scope
evidence, not a design PASS.

Immediately before this gate's sole write:

~~~text
notes/phase2_control_design_amendment_v16.md=ABSENT_ORDINARY_AND_SYMLINK_AWARE
notes/phase2_control_design_remediation_gate_v17.md=ABSENT_ORDINARY_AND_SYMLINK_AWARE
notes/phase2_control_design_amendment_v17.md=ABSENT_ORDINARY_AND_SYMLINK_AWARE
V16_AMENDMENT_ATTEMPT_CONSUMED=false
~~~

### 1.5 Controlling implementation STOP and exact quarantine

| Record | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| ATTEMPT_3 implementation peer review | 643 | 37947 | 637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88 | REVISE_C0_M12_m0 |
| implementation remediation gate v5 | 733 | 31304 | 411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7 | STOP_DESIGN_REOPEN_REQUIRED |

All twelve implementation findings remain open. ATTEMPT_4 remains
unconsumed only because its plan was rejected before admission and its
source-mutation count is zero. It is suspended and unavailable.

| Frozen path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| code/generate_controls.py | 1133 | 60497 | 4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020 |
| code/test_controls.py | 1655 | 129574 | c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac |
| code/README.md | 95 | 5267 | 96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee |
| experiments/reproduce.sh | 6270 | 469357 | dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59 |
| experiments/README.md | 226 | 14697 | ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6 |
| results/README.md | 76 | 3221 | 03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c |

They total 9455 lines and 682613 bytes. Each is regular mode 0644, nlink 1.
They are immutable quarantine, not design authority or conformance evidence.

## 2. Global v16-authority tombstone and exact v17 scope

### 2.1 V16 authority is unavailable before consumption

The following recovery decision has global precedence over v16 Sections 15
and 17 and every dependent v16 amendment-authority statement:

~~~text
V16_GATE_ROLE=IMMUTABLE_DEFECTIVE_GOVERNANCE_PROVENANCE
V16_GATE_BYTES_MUTABLE=false
V16_AMENDMENT_ATTEMPT_CONSUMED=false
V16_AMENDMENT_AUTHORITY_TOMBSTONED_BEFORE_CONSUMPTION=true
V16_AMENDMENT_AUTHORITY_EFFECTIVE=false
V16_AMENDMENT_AUTHORITY_AVAILABLE=false
V16_AMENDMENT_PATH_PRESENT=false
V16_AMENDMENT_SKIPPED=true
AMENDMENT_V16_CREATION_AUTHORIZED=false
~~~

The v16 gate is neither deleted nor rewritten. Its correct analysis remains
bounded evidence, but it cannot authorize amendment v16, a rereview, a
marker, source work, or a run. Appearance of amendment v16 at any later cut
is a STOP; it is never adopted into the v17 tuple.

### 2.2 Sole v17 dependent-corrigendum scope

The one future amendment v17 may only:

1. correct v15 M1--M3 with target preclassification, a closed four-object
   reference algebra, and distinct transaction/per-reference identity;
2. correct v15 M4 by reducing pidfd fstat to class evidence and freezing the
   trusted authoritative lineage;
3. correct v15 M5 with the exact U1 and shared-bootstrap-B happens-before
   edges plus P's live-L audit;
4. correct v15 m1's parent-child sentence;
5. correct F1 by keeping fixed targets live on successful cleanup and
   reserving UNWINDING for failure;
6. correct F2 by restoring R10/R11 pre-probe acquisition and placing only
   R12/R13 acquisition plus the combined install after probe removal; and
7. restate only the mechanically coupled holder, D-M2, HC, P_CRASH, count,
   and narrow-predecessor consequences.

V17 may not add an actor, process, endpoint, wire form, field, ancillary
item, FD slot, pipe, eventfd, socket, path, service, shared mapping, memfd,
file, environment bearer, reconnect, retry, fallback, persistence object,
classifier coordinate, result, schema item, manifest member, or DAG edge.

The v15 choices retained as candidate inputs are FD12, FD13, the immutable
identity receipt, ordinary fork/COW lineage, exact terminal poll, complete
P_CRASH guard, G-child transient close order, and unchanged public counts.
V17 must explicitly supersede defective v15 clauses and the two defective
v16 instructions. It may not call v15 effective, call v16 a candidate, or
silently inherit a contradicted statement.

## 3. F2 closure: exact acquisition and root-probe order

The exact order is:

~~~text
P blocks the inherited handled-signal set and becomes child subreaper
-> acquire, validate, and retain exact active-v2 R10
   REPOSITORY_SOURCE_ROOT
-> acquire, validate, and retain exact active-v2 R11
   PACKAGE_SOURCE_ROOT
-> preserve both active-v2 receipts and OFD lifetimes without
   close, replacement, reopen, or reacquisition
-> create the existing cgroup tree
-> create the one existing root probe
-> fully kill and reap the root probe
-> complete duplicate-wait/process-gone proof
-> require probe cgroup populated=0
-> remove the exact empty probe cgroup
-> prove no probe or other pre-L child remains
-> revalidate the same retained R10/R11 receipts
-> acquire and ledger R12=P_SELF_PIDFD
-> acquire and ledger R13=P_INITIAL_PROC_PID_DIR
-> enter the one combined R10--R13 target-preclassification,
   high-stage, install, validation, and successful-cleanup transaction
-> reach SLOTS_INSTALLED
-> bind the existing listener
-> create the existing bootstrap SOCK_SEQPACKET socketpair
-> clone L
~~~

The root probe may not inherit FD12 or FD13 because neither exists while it
is live. R10/R11 acquisition is not moved; only their fixed-target install
participates in the post-probe combined transaction. Reopening or
reacquiring a supposedly equivalent R10/R11 after the probe is forbidden;
the exact retained active-v2 object receipts must survive.

The P-only LONG_LIVED_PROC_ROOT may remain open. If it or any unrelated
descriptor occupies target 10--13, Section 4 requires STOP before staging.
No alternate slot or remap is authorized.

## 4. M1--M3 closure: target and reference algebra

### 4.1 Closed object and target domains

The complete object-kind enum is:

~~~text
REPOSITORY_SOURCE_ROOT
PACKAGE_SOURCE_ROOT
P_SELF_PIDFD
P_INITIAL_PROC_PID_DIR
~~~

The bindings are T10/R10 repository root, T11/R11 package root, T12/R12 P
self-pidfd, and T13/R13 initial-proc P directory.

After all four raw references and their distinct IDs are ledgered, and
before the first F_DUPFD_CLOEXEC, P enters one single-threaded,
signal-controlled, no-allocation barrier and classifies each current target
10--13 as exactly one of:

~~~text
VACANT_EBADF
TRANSACTION_RAW_REFERENCE
FORBIDDEN_THIRD_PARTY
~~~

VACANT_EBADF requires F_GETFD=-1 and errno EBADF. A
TRANSACTION_RAW_REFERENCE requires that the target integer equal the exact
current local_fd of one ledgered R10--R13 and that flags, type, object kind,
and object receipt match that entry. Every other open occupant is
FORBIDDEN_THIRD_PARTY.

LONG_LIVED_PROC_ROOT, listener, bootstrap endpoint, control endpoint,
signalfd, cgroup/namespace FD, unrelated pidfd, or any unclassified occupant
at 10--13 yields E_POSSESSION_UNAVAILABLE before the first staging
duplicate. It is neither overwritten nor added to the transaction.
Immediately before each dup3, P rechecks the still-applicable frozen target
classification. Any drift stops before that destructive syscall.

### 4.2 Separate phase, role, disposition, and lifetime algebras

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

The closed lifetime-phase enum for only the P-lifetime objects is:

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

Transaction phase, reference disposition, and lifetime phase are distinct.
DISPLACED_BY_TARGET is a terminal reference disposition, not a close,
transaction phase, or owner-death result. CLOSED_PROVED requires close
return 0 followed immediately, with no allocation between, by
F_GETFD=-1/EBADF.

### 4.3 Exact reference identity grammar

Every raw, stage, target, and inherited reference entry binds:

~~~text
transaction_serial
issuer_actor
reference_serial
parent_reference_id
object_kind
reference_role
exact_local_fd
fd_flags
status_flags
object_class_receipt
object_receipt
reference_disposition
~~~

The identity is:

~~~text
reference_id=(transaction_serial,issuer_actor,reference_serial)
~~~

transaction_serial is P-owned, monotone, nonzero, and never reused.
reference_serial is nonzero, monotone, and never reused within its actor
domain. parent_reference_id=NONE is legal only for a raw. A high stage
points to its raw; a fixed target points to its high stage; an inherited
copy points to its actual parent copy. P pre-reserves deterministic L/G copy
IDs before fork; each G-child copy uses the already-governed unique child
creation serial. Wrap, duplicate, missing parent, actor mismatch, or
cross-object parentage yields ABORT_AMBIGUOUS.

The immutable P identity receipt contains at least:

~~~text
transaction_serial
pidfd_raw_reference_id
pidfd_stage_reference_id
pidfd_target_reference_id
procdir_raw_reference_id
procdir_stage_reference_id
procdir_target_reference_id
~~~

G joins inherited slot 12 separately to pidfd_target_reference_id and slot
13 separately to procdir_target_reference_id. No scalar may stand for the
transaction, pidfd reference, and procdir reference simultaneously.

## 5. F1 closure: successful cleanup is not failure unwind

### 5.1 Common staging and install prefix

The transaction prefix is exact:

1. ledger R10--R13 and their distinct reference IDs;
2. classify all target occupants;
3. create H10--H13 in target order with F_DUPFD_CLOEXEC lower 64;
4. validate all four raw-to-stage joins before any low install;
5. dup3 H10--H13 to targets 10--13 in ascending order with O_CLOEXEC;
6. after each successful dup3 create one new FIXED_TARGET reference;
7. if that dup3 displaced a transaction raw occupant, mark that raw
   DISPLACED_BY_TARGET with target-reference and syscall serial; and
8. validate all four target references before selecting success.

A failed dup3 does not displace its old target occupant. A displaced raw
integer is stale and must never be closed.

### 5.2 Exact successful cleanup

**SUCCESS IS NOT UNWIND.** After all four target references validate:

1. set transaction_phase=CLEANING;
2. reverse-close every live H10--H13 stage in reverse acquisition order;
3. reverse-close every still-live nondisplaced R10--R13 raw reference in
   reverse acquisition order;
4. after every actual close require return 0, no intervening allocation,
   F_GETFD=-1, errno EBADF, then set that reference CLOSED_PROVED;
5. require every raw to be exactly CLOSED_PROVED or DISPLACED_BY_TARGET;
6. require every stage to be CLOSED_PROVED;
7. require T10, T11, T12, and T13 to remain open, role FIXED_TARGET,
   disposition LIVE_VALIDATED, with their exact target joins; and
8. only then set transaction_phase=SLOTS_INSTALLED.

SLOTS_INSTALLED therefore requires terminal setup-only raw/stage
dispositions while all four installed fixed targets remain LIVE_VALIDATED.
It does not require every reference to have a terminal disposition, and it
never closes a successful installed target.

### 5.3 Exact failure unwind

Only a failure before SLOTS_INSTALLED enters transaction_phase=UNWINDING.
The single serial-driven failure unwind:

1. reverse-closes the actually installed target prefix;
2. reverse-closes every still-live stage;
3. reverse-closes every still-live nondisplaced raw;
4. never closes a DISPLACED_BY_TARGET stale integer;
5. applies the exact close/EBADF proof to each actual live close; and
6. retains every reference, completed prefix, displacement, syscall serial,
   close result, and ambiguity in the failure tombstone.

A clean, complete, unambiguous unwind ends ABORT_CLOSED. Any close, EBADF,
reference, order, or liveness ambiguity ends ABORT_AMBIGUOUS. Both forbid
clone L. There is no retry, fallback, alternate slot, partial design state,
or second transaction.

## 6. M5 baseline: existing bootstrap A/B identity

The existing inherited bootstrap socketpair is named only for this
corrigendum:

~~~text
A = P-side peer endpoint/OFD
B = L-to-G inherited endpoint/OFD
~~~

This naming adds no endpoint or record. Bfd is the existing receipt-bound
integer and must not equal 10--13. Before clone L, P freezes:

~~~text
B0=fcntl(B,F_GETFL)
(B0 & O_NONBLOCK)==0
B has FD_CLOEXEC
B is the expected SOCK_SEQPACKET sockfs object
A and B are distinct endpoint/open-file descriptions
~~~

The immutable B receipt, including B0, Bfd, socket identity, endpoint role,
and CLOEXEC, passes to L and G only through existing fork/COW memory.

P closes its B alias and proves EBADF before processing U1_CREATED. L closes
its A alias and proves EBADF before its first U1 record. Then P alone owns A;
L later forks G, so L and G hold separate FD-table references to the same B
open file description.

Only L's one Section-8 F_SETFL and one Section-8 SHUT_RD may mutate B. P
cannot mutate B through A. G and every other actor are forbidden from
F_SETFL, FIONBIO, shutdown, dup, SCM_RIGHTS, replacement, exec,
registration, or transfer of B.

## 7. P-to-L release through the existing U1 ACK

After successful clone3 parent return, P performs exactly:

~~~text
close P's B alias -> immediate EBADF
-> close(13)=0 -> immediate F_GETFD(13)=-1/EBADF
-> close(12)=0 -> immediate F_GETFD(12)=-1/EBADF
-> only then process already-queued U1_CREATED
-> write and re-read exact U1 maps
-> send existing U1_MAPS_COMMITTED
~~~

L remains blocked after U1_CREATED until receiving that ACK. Therefore:

~~~text
P FD13/12 close receipts
happens-before U1_MAPS_COMMITTED enqueue/receive
happens-before every later L U2 action
happens-before L forks G
~~~

Any P close, EBADF, U1 map, or send failure forbids the ACK and enters
bootstrap containment. The existing ACK gains no field or form.

## 8. L-to-G release through the shared B OFD

### 8.1 Retimed fifth bootstrap form and L release

L completes the exact U2 uid/gid map writes, re-reads, inner-id checks,
empty-groups check, and U2_ROOT0_MAPPED local state before fork G. It does
not yet send U2_MAPS_COMMITTED. It then performs the existing
unshare(CLONE_NEWNS|CLONE_NEWPID) and sole fork of G.

After fork, the L parent performs exactly:

~~~text
close(13)=0
-> immediate F_GETFD(13)=-1/EBADF
-> close(12)=0
-> immediate F_GETFD(12)=-1/EBADF
-> fcntl(B,F_GETFL)==B0
-> fcntl(B,F_SETFL,B0|O_NONBLOCK)==0
-> fcntl(B,F_GETFL)==B1 where (B1 xor B0)==O_NONBLOCK
-> one sendmsg of the existing exact framed U2_MAPS_COMMITTED
-> exact full framed-length return
-> shutdown(B,SHUT_RD)==0
~~~

The marker makes the send nonblocking. Length prefix and payload use one
exact sendmsg. EAGAIN, EWOULDBLOCK, EINTR, short return, zero, or any other
error is fatal, with no retry. U2_MAPS_COMMITTED remains the fifth and final
inherited bootstrap form, exactly once, L-to-P, with unchanged fields and
bytes.

The marker alone is not release authority. SHUT_RD alone is not release
authority. Their conjunction after both close receipts and exact full U2
send is the one L-origin release transition. The successful local SHUT_RD
is the wake/release linearization. If marker publication is followed by U2,
SHUT_RD, or validation failure, fatal containment must make G observe HUP;
the normal path never uses SHUT_RDWR.

### 8.2 G's sole pre-release action and exact predicate

Immediately after fork, G may perform only the governed B-barrier ppoll,
F_GETFL, recvmsg(MSG_DONTWAIT), and final close/EBADF. Before release it may
not validate FD12/13, mount private proc state, connect, send PID1_READY,
allocate or close another FD, mutate B, or perform other work.

G blocks on:

~~~text
ppoll(B,events=POLLIN|POLLRDHUP,existing bootstrap deadline)
~~~

A normal release requires all of:

~~~text
poll return identifies only B
(revents & POLLIN) != 0
(revents & POLLRDHUP) != 0
(revents & (POLLHUP|POLLERR|POLLNVAL)) == 0
fcntl(B,F_GETFL) == B1
recvmsg(B,one-byte nonzero buffer,MSG_DONTWAIT) == 0
payload bytes consumed = 0
ancillary count = 0
MSG_TRUNC and MSG_CTRUNC absent
~~~

Additional nonfatal readiness bits do not require exact revents equality.
POLLHUP always wins and forbids normal release even if all other bits and B1
are visible. Timeout, EINTR, error, positive data, cmsg, truncation, flag
drift, or ambiguity is bootstrap failure, never success or life/death
evidence.

After the predicate, G closes B and, without intervening allocation, proves
Bfd F_GETFD=-1/EBADF. Only then may G validate FD12/13, require FD12 initial
nonreadiness, close FD13/EBADF, prepare its private mount, connect to the
existing listener, and send PID1_READY.

Peer EOF, peer close, P death, zero-time FD12 poll, marker alone, or F_GETFL
busy-loop visibility is not release authority.

### 8.3 P's independent live-L holder audit

P receives and validates the exact post-close U2 frame before accepting G.
Before accept() and before accepting PID1_READY, P enters one
single-threaded, signal-controlled allocation barrier. It does not accept,
receive an FD, read signalfd, or perform another allocation during the
audit.

P requires launcher pidfd nonready and uses only the existing trusted outer
proc root and bound L outer PID. Every returned transient L PID-directory,
stat, fd-directory, and fdinfo-for-Bfd reference is entered immediately with
an acquisition serial in a separate BOOTSTRAP_L_PROC_AUDIT_LEDGER before
validation.

P brackets two complete canonical L FD-number snapshots with exact launcher
pidfd, outer PID, field-22 starttime, NSpid, credentials, and guardian
identity checks. Both snapshots must be byte/set equal. Parked live L's
exact allowlist is:

~~~text
FD10
FD11
bootstrap Bfd
~~~

FD12 and FD13 must be absent. No extra integer or alias is legal. P requires
Bfd's frozen socket/inode/mount lineage, descriptor CLOEXEC, and file-status
flags corresponding to B1. Proc fdinfo's descriptor and status-flag domains
must be parsed separately; its numeric flags are not naively compared with
F_GETFL B1. P never follows or reopens /proc/L/fd/Bfd and never duplicates B.

All transient audit references are reverse-closed with immediate EBADF.
They are P-local, pre-accept, noninherited, nonendpoint, and outside D-M2's
21 tags. L death, identity drift, snapshot drift, missing B, present 12/13,
extra FD, flag mismatch, partial read, or unwind ambiguity forbids accept and
enters containment.

### 8.4 L park and final bootstrap disposal

After normal SHUT_RD, L retains B, performs no FD allocation, duplication,
replacement, marker clear, or process creation, and parks with
poll(B,events=0) awaiting the existing P-side final close.

G never reads bootstrap peer EOF. P retains A through
CONTROL_AUTHENTICATED and CGROUP_PREFLIGHTED, then performs the original
final A close at the launcher-exit cut. Full peer shutdown produces POLLHUP
for parked L. L requires HUP, closes B with immediate EBADF, completes its
unchanged exit duties, and exits; P pidfd-reaps L before LAUNCHER_REAPED.

L may not close B before P's audit. P may not close A early. On every
failure, HUP precedence prevents an already-visible marker from becoming a
false normal release.

## 9. Exact holder matrix

| Cut | P-lifetime FD12 holders | P-procdir FD13 holders | Required proof |
|---|---|---|---|
| post-install, pre-clone | P | P | successful transaction and receipt complete |
| clone-L kernel window | P,L | P,L | no CLONE_FILES; no exec |
| post-U1 ACK receive | L | L | P B/13/12 closes precede ACK |
| fork-G kernel window | L,G | L,G | shared B OFD; separate FD tables |
| B release observed by G | G | G | L closes precede marker, U2, SHUT_RD |
| G identity validated | G | G | lineage and class checks complete |
| pre-PID1_READY | G | none | G closes FD13 and proves EBADF |
| steady carrier | G only | none | FD12 fixed and nonreplaceable |
| trusted G-child fork instant | G plus child transient | none | EP_G-first then FD12 close-only stub |
| child SANITIZED/registered | G only | none | child has no 12/13 |
| terminal after endpoint duties | none | none | G closes FD12 last and proves EBADF |

P's audit independently confirms L's absence before accept. It does not
replace G's B release. B marker/SHUT_RD are pre-auth bootstrap facts, not
endpoint custody.

## 10. M4 evidence ceiling, D-M2, and HC

### 10.1 Pidfd class receipt and trusted lineage

V17 must replace pidfd_type_and_fstat_identity with class-only evidence:

~~~text
pidfd_class_fstat_receipt
pidfd_fstat_is_unique_identity=false
pidfd_fstat_is_target_identity=false
pidfd_fstat_is_same_ofd_proof=false
~~~

Linux 5.15 ordinary pidfds use the shared singleton anonymous inode.
st_dev/st_ino/st_mode support class/type and flags sanity only; they cannot
distinguish pidfds, prove target P, or prove same OFD.

The authoritative P binding is the conjunction of:

1. P-side pidfd_open(canonical getpid(),0);
2. P-side fdinfo Pid equality in the initial PID namespace;
3. initial-proc directory object and field-22 starttime;
4. exact transaction and per-reference IDs;
5. raw-to-stage-to-target parent-reference chains;
6. ordinary fork with no CLONE_FILES and no exec;
7. P's U1 happens-before;
8. L's B marker plus local-SHUT_RD happens-before;
9. P's independent live-L FD audit;
10. a gapless no-close/no-dup/no-replace FD12 invariant;
11. close-only handling of every G-child transient; and
12. terminal poll on that lineage-bound fixed FD12.

G has no independent exact OFD comparator. Same-OFD is a static
trusted-program lineage invariant under the unchanged conditional,
unverified deployment-model ceiling. A wrong live pidfd with the same
anon-inode fstat, G fdinfo Pid:0, and initial nonreadiness is not excluded by
those observations alone.

### 10.2 D-M2 claim ceiling and exact counts

Every steady complete G snapshot after PID1_READY requires FD12 present and
FD13 absent. D-M2 may claim slot presence, CLOEXEC/class/non-socket status,
snapshot-set stability, and G FD-generation stability. It may not claim that
fstat proves target P, unique pidfd OFD, same OFD, or an independently
observed lineage.

FD12 remains excluded from the socket-candidate selector, pidfd_getfd target
set, row ledger, and tag-18 unwind. FD13 remains absent. Bootstrap B and the
transient L-proc audit ledger do not enter D-M2.

~~~text
D_M2_FIXED_TAG_COUNT=21
D_M2_CONTROL_FORM_COUNT=4
D_M2_FRESH_PROC_LEDGER_SLOTS=4
D_M2_CHILD_DUPLICATE_SLOTS=1
WORKER_FDSET_VALUE_COUNT=4
~~~

B closes in G before the actual P--G control connection and in P/L before
LAUNCHER_REAPED. It is not EP_P, EP_G, an endpoint alias, or holder-freeze
member. FD12 remains nonendpoint and FD13 is pre-carrier gone. Therefore:

~~~text
HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
~~~

Any B survival into the control holder window, FD13 survival past
PID1_READY, FD12 endpoint operation, duplicate/registration/transfer, or new
synchronization object reopens HC and is outside this gate.

## 11. P_CRASH and parent-child correction

The exact FD12 terminal predicate and complete twelve-part P_CRASH guard
from candidate v15 remain candidate obligations. B release, HUP, U2, P's
L-audit, initial nonreadiness, or EOF is not a C14 coordinate, raw17 bit,
P-exit proof, or terminal success.

The exact sentence is:

~~~text
P is not G's child. After L is reaped, G is normally P's
descendant/adopted child in the outer PID namespace because P is the
child subreaper.
~~~

Therefore G cannot wait or reap P, and ECHILD is not P-death evidence. P may
reap adopted G in the lawful direction. Pidfd polling neither waits nor
reaps.

## 12. Frozen public algebra and package vector

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

AUTHORITY_BINDINGS=14 is a package binding count, not the amendment count.

## 13. Exact narrow supersessions required in v17

The future amendment must explicitly supersede or clarify only:

1. v15 Sections 3 and 6: target preclassification, reference algebra,
   phases, dispositions, and serial grammar;
2. v15 identity-receipt fields: separate transaction/pidfd/procdir IDs;
3. v15 pidfd fstat language: class sanity only;
4. v15 holder matrix: replace local-order inference with exact U1 and B-OFD
   happens-before edges plus P's live-L audit;
5. v15 wait rationale: P is not G's child;
6. active v2 step 1: preserve R10/R11 acquisition before root probe, while
   moving only R12/R13 acquisition and combined fixed install after complete
   probe removal;
7. active v2 step 2: exact A/B alias closure and P B/13/12-before-U1 order;
8. active v2 step 5: U2 map work remains pre-fork, while the sole U2 send
   moves post-fork and post-L-close;
9. active v2 steps 6--7: G's first work is B release consume; G closes B
   before identity/connect/ready; P audits live L before accept;
10. active v2 bootstrap close: G B closes pre-connect; L B survives local
    SHUT_RD through P's original post-auth/preflight A close;
11. active v2 step 10: L final B close/EBADF, exit, and P reap precede
    LAUNCHER_REAPED;
12. v6 D-M2: FD12 class/set/generation ceiling and separate ledgers;
13. v14 terminal/HC: unchanged only under the exact pre-carrier cuts here;
14. v14 effective-count governance: only joint v15+v17 zero-finding review
    may publish count 15;
15. v16 Section 3: replace its all-four-post-probe acquisition statement
    with Section 3 of this gate; and
16. v16 Section 4.4: replace its success/unwind and all-terminal-reference
    statements with Section 5 of this gate.

There is no blanket supersession of v2, v6, v14, v15, or v16. V16 remains
defective provenance, not a candidate. Every unmentioned active obligation
remains exact.

## 14. Mandatory hostile counterexamples

The amendment author must state, and the fresh reviewer must independently
attack, at least all of these fixed cases:

| # | Hostile case | Required disposition |
|---:|---|---|
| 1 | root probe begins before R10/R11 acquisition | active-v2 order violation; STOP |
| 2 | R10/R11 is reopened or reacquired after the probe | receipt-continuity failure; STOP |
| 3 | R12 or R13 exists while root probe is live | holder-contract failure |
| 4 | combined transaction begins while probe/pre-L child survives | STOP before staging |
| 5 | v17 blanket-supersedes v2 step 1 | authority excess |
| 6 | target 12 is LONG_LIVED_PROC_ROOT | STOP before staging; never overwrite |
| 7 | target 13 is listener/bootstrap/signalfd | same STOP |
| 8 | target classified then drifts | recheck fails before dup3 |
| 9 | target is exact R12/R13 raw | stage protects it; successful dup3 records displacement |
| 10 | dup3 fails | old occupant remains; no displacement claim |
| 11 | code closes a displaced stale integer | forbidden; it could close the new target |
| 12 | R10/R11 lacks object kind | schema failure |
| 13 | stage/target/inherited copy lacks role | schema failure |
| 14 | transaction and two capabilities share one serial | receipt ambiguity |
| 15 | post-fork actor IDs collide | actor-qualified identity failure |
| 16 | success cleanup closes any T10--T13 | nonaccepting |
| 17 | SLOTS_INSTALLED has a fixed target CLOSED_PROVED | nonaccepting |
| 18 | SLOTS_INSTALLED has a live raw or stage | incomplete successful cleanup |
| 19 | partial failure leaves installed target open | incomplete failure unwind |
| 20 | failure cleanup closes DISPLACED_BY_TARGET stale integer | forbidden |
| 21 | success enters UNWINDING | phase contradiction |
| 22 | P sends U1 ACK before closing B/13/12 | ACK-guard failure |
| 23 | G runs before L parent | it remains blocked in ppoll |
| 24 | B initially has O_NONBLOCK | baseline failure before clone |
| 25 | Bfd equals 10--13 | registry-collision STOP |
| 26 | actor other than L mutates B flags or shutdown | forbidden mutation |
| 27 | L sets marker before closing 13/12 | release-state violation |
| 28 | marker alone is release | reject; SHUT_RD/no-HUP conjunction required |
| 29 | L sends U2 before marker or retries | state/cardinality failure |
| 30 | nonblocking U2 send is short/EAGAIN/EINTR | fatal, no retry |
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
| 54 | amendment v16 appears or is included in candidate tuple | tombstone violation; STOP |
| 55 | v15 or v17 activates alone | partial activation forbidden |

Missing a case, weakening HUP precedence, closing a successful fixed target,
moving R10/R11 acquisition, or replacing exact evidence with a timeout,
plausible schedule, comment, hash, or self-authored constant is
nonaccepting.

## 15. One v17 amendment and one independent rereview

### 15.1 Amendment authority

Only after an external coordinator freezes this gate's actual regular-file
receipt may one design author create:

~~~text
notes/phase2_control_design_amendment_v17.md
~~~

Amendment v16 and v17 targets must still have their required absence states:
v16 absent/skipped; v17 absent before creation. The v17 author receives
exactly one notes-only Add-File apply_patch attempt. There is no draft path,
temporary path, overwrite, rename, second attempt, v16 reuse, or author
handoff.

The amendment author must full-read this gate; immutable v16 provenance;
candidate v15 gate/amendment; the complete current review; base and every
active amendment; active v2/v6/v14; v5 STOP; ATTEMPT_3 review; and exact
quarantine. It must implement Sections 3--14, retain actual input digests,
make no PASS claim, predict no self hash, and authorize no source, review
append, or run.

### 15.2 Fresh append-only complete rereview

Only after an external coordinator freezes actual amendment v17, while
amendment v16 remains absent, may one fresh reviewer independent of v15,
v16, and v17 gate/amendment authors append one block to:

~~~text
notes/phase2_control_design_peer_review.md
~~~

The required preserved prefix is:

~~~text
lines=6965
bytes=375778
sha256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5
~~~

Prefix rewrite, insertion, deletion, relocation, truncation, replacement,
or second review attempt is forbidden. The reviewer reads the complete base
+ active-thirteen + frozen-v15 + frozen-v17 tuple and every governing
record; attacks all hostile cases; and re-derives acquisition order,
transaction success/failure closure, target occupants, ledgers, serials,
Linux-5.15 B/pidfd semantics, holders, D-M2, HC, C14/raw17, forms, and
package/DAG counts.

The sole accepting verdict is:

~~~text
PASS_C0_M0_m0
~~~

Any finding, uncertainty affecting exact closure, missing hostile case,
authority mismatch, amendment-v16 appearance, prefix drift, conditional
waiver, REVISE, FAIL, STOP, or incomplete append is nonaccepting.

### 15.3 Joint-activation marker

Neither this gate nor amendment v17 makes v15 or v17 effective. Only the
later zero-finding reviewer may append:

~~~text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v13]
count=15
entries 1..11 = amendments v1..v11 at frozen hashes
entry 12 = amendment v13 at 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27
entry 13 = amendment v14 at b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c
entry 14 = amendment v15 at 158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239
entry 15 = amendment v17 at its external stable hash
amendment v12 = absent and skipped
amendment v16 = absent and skipped
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
~~~

Marker version v13 is the next unused effective-marker version. Count 15 is
the number of actually active amendment records, not a contiguous version
range. Partial activation, v15-only activation, and v17-only activation are
forbidden. A non-PASS review publishes no marker and leaves count 13.

## 16. Downstream nonauthority

This gate writes no amendment or review and authorizes no source edit,
implementation plan admission, implementation review, platform preflight,
runtime probe, generated member, result, proof, Route, composition,
manuscript, figure, release, archive, or Git action.

Even a future joint design PASS does not revive implementation gate v4 or
directly admit ATTEMPT_4. A separate owner decision and successor
implementation gate must bind the new complete design/review tuple, v5
STOP, all twelve implementation findings, rejected old plan, unconsumed
attempt state, and all six source hashes before deciding whether
implementation work exists.

## 17. External freeze and authorization matrix

An external coordinator, not this self-referential file, must compute and
freeze this gate's actual path, type, mode, nlink, lines, bytes, UTF-8,
terminal-LF, CR/NUL result, and SHA-256. It must perform two complete
unchanged reads; reauthenticate all Section-1 inputs and six source paths;
and confirm amendment v16 and amendment v17 absence at the applicable cuts.
Any drift, unexpected successor, symlink, hardlink, nonregular object,
predicted self digest, or post-receipt edit is STOP.

~~~text
P15R_CONTROL_DESIGN_REMEDIATION_GATE=P15R-P2-CONTROL-DESIGN-REMEDIATION-GATE-v17.0
GATE_KIND=NOTES_ONLY_V16_AUTHORITY_RECOVERY_AND_V15_DEPENDENT_CORRIGENDUM
GATE_VERDICT=PASS_TO_ONE_VERSIONED_DESIGN_AMENDMENT_V17_ONLY

CURRENT_DESIGN_REVIEW_SHA256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5
CURRENT_V15_REVIEW_VERDICT=REVISE_C0_M5_m1
V15_GATE_SHA256=c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a
V15_AMENDMENT_SHA256=158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239
V15_EFFECTIVE=false
V17_IS_V15_DEPENDENT_CORRIGENDUM=true

V16_GATE_SHA256=063d86fc87118547d2c77544d8b4b20a40dd63d1d41fab6647113767387d5f6c
V16_GATE_ROLE=IMMUTABLE_DEFECTIVE_GOVERNANCE_PROVENANCE
V16_GATE_COMBINED_FINDING_SET=F1,F2
V16_GATE_OTHER_FINDING_COUNT=0
V16_AMENDMENT_ATTEMPT_CONSUMED=false
V16_AMENDMENT_AUTHORITY_TOMBSTONED_BEFORE_CONSUMPTION=true
V16_AMENDMENT_AUTHORITY_AVAILABLE=false
V16_AMENDMENT_PATH_PRESENT=false
V16_AMENDMENT_SKIPPED=true
AMENDMENT_V16_CREATION_AUTHORIZED=false

CURRENT_EFFECTIVE_AMENDMENT_COUNT=13
SUCCESSOR_EFFECTIVE_COUNT_ONLY_IF_JOINT_PASS=15
SUCCESSOR_EFFECTIVE_MARKER_VERSION=v13
PARTIAL_ACTIVATION_AUTHORIZED=false
V15_ONLY_ACTIVATION_AUTHORIZED=false
V17_ONLY_ACTIVATION_AUTHORIZED=false
AMENDMENT_V12_PRESENT=false
AMENDMENT_V12_SKIPPED=true

R10_R11_ACQUIRED_BEFORE_ROOT_PROBE=true
R10_R11_ACTIVE_V2_RECEIPTS_PRESERVED=true
R12_R13_ACQUIRED_BEFORE_ROOT_PROBE=false
ROOT_PROBE_INHERITS_FD12_FD13=false
FOUR_OBJECT_TRANSACTION_BEGINS_AFTER_ROOT_PROBE_REMOVAL=true
TARGET_CLASSIFICATION_OCCURS_AFTER_ALL_FOUR_RAW_REFERENCES_ARE_BOUND=true
FD10_FD11_ACQUISITION_ORDER_MOVED=false

TARGET_PRECLASSIFICATION_REQUIRED=true
TARGET_PRECLASSIFICATION_TARGETS=10,11,12,13
THIRD_PARTY_TARGET_OVERWRITE_AUTHORIZED=false
TRANSACTION_OBJECT_KIND_COUNT=4
REFERENCE_ROLE_COUNT=4
REFERENCE_DISPOSITION_COUNT=6
DISPLACED_BY_TARGET_IS_CLOSED_DISPOSITION=true
TRANSACTION_AND_REFERENCE_SERIALS_DISTINCT=true

SUCCESS_IS_UNWIND=false
SUCCESS_CLEANUP_CLOSES_FIXED_TARGETS=false
SUCCESS_CLEANUP_CLOSES_STAGES=true
SUCCESS_CLEANUP_CLOSES_NONDISPLACED_RAWS=true
SLOTS_INSTALLED_FIXED_TARGET_DISPOSITION=LIVE_VALIDATED
FAILURE_ONLY_ENTERS_UNWINDING=true
FAILURE_UNWIND_CLOSES_INSTALLED_PREFIX=true
FAILURE_UNWIND_CLOSES_DISPLACED_STALE_INTEGER=false
CLEAN_FAILURE_UNWIND_TERMINAL=ABORT_CLOSED
AMBIGUOUS_FAILURE_UNWIND_TERMINAL=ABORT_AMBIGUOUS

P_CLOSE_B_FD13_FD12_PRECEDES_U1_ACK=true
U2_MAPS_COMMITTED_DIRECTION=L_TO_P
U2_MAPS_COMMITTED_CARDINALITY=1
U2_MAPS_COMMITTED_SEND_RETRY_AUTHORIZED=false
BOOTSTRAP_B_INITIAL_NONBLOCK=false
BOOTSTRAP_B_RELEASE_MARKER=O_NONBLOCK
BOOTSTRAP_B_RELEASE_WAKE=LOCAL_SHUT_RD
BOOTSTRAP_PEER_EOF_IS_G_RELEASE_AUTHORITY=false
F_GETFL_SPIN_IS_G_RELEASE_AUTHORITY=false
MARKER_ALONE_IS_G_RELEASE_AUTHORITY=false
G_RELEASE_REQUIRES_POLLIN=true
G_RELEASE_REQUIRES_POLLRDHUP=true
G_RELEASE_REJECTS_POLLHUP=true
G_RELEASE_REJECTS_POLLERR=true
G_RELEASE_REJECTS_POLLNVAL=true
G_RELEASE_REQUIRES_B1=true
G_RELEASE_REQUIRES_ZERO_DATA_NO_CMSG=true
P_LIVE_L_FDINFO_ALLOWLIST_AUDIT_REQUIRED=true
P_ACCEPT_BEFORE_L_AUDIT_AUTHORIZED=false

PIDFD_FSTAT_PROVES_CLASS_ONLY=true
PIDFD_FSTAT_PROVES_TARGET=false
PIDFD_FSTAT_PROVES_SAME_OFD=false
PARENT_CHILD_CORRECT_SENTENCE=P_IS_NOT_GS_CHILD

INHERITED_BOOTSTRAP_FORM_COUNT=5
V17_NEW_WIRE_FORM_COUNT=0
GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
D_M2_FIXED_TAG_COUNT=21
WORKER_FDSET_VALUE_COUNT=4

HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1
HC_RECOMPUTATION_AUTHORIZED=false

AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v17.md
AMENDMENT_V17_APPLY_PATCH_ATTEMPTS_AUTHORIZED=1
OTHER_DESIGN_OR_AMENDMENT_PATH_AUTHORIZED=false
FRESH_APPEND_ONLY_REREVIEW_ATTEMPTS_AUTHORIZED=1
DESIGN_REREVIEW_PATH=notes/phase2_control_design_peer_review.md
DESIGN_REREVIEW_PREFIX_LINES=6965
DESIGN_REREVIEW_PREFIX_BYTES=375778
DESIGN_REREVIEW_PREFIX_SHA256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5
DESIGN_REREVIEW_ONLY_ACCEPTING_VERDICT=PASS_C0_M0_m0

CONTROLLING_IMPLEMENTATION_GATE_VERDICT=STOP_DESIGN_REOPEN_REQUIRED
CONTROLLING_IMPLEMENTATION_GATE_V5_SHA256=411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7
ATTEMPT3_IMPLEMENTATION_REVIEW_SHA256=637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88
ATTEMPT4_UNCONSUMED=true
ATTEMPT4_SUSPENDED=true
ATTEMPT4_AVAILABLE=false

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

Final determination: **PASS TO ONE VERSIONED DESIGN AMENDMENT v17 ONLY,
FOLLOWED BY ONE FRESH INDEPENDENT APPEND-ONLY COMPLETE DESIGN REREVIEW.**
The unused v16 amendment authority is tombstoned and amendment v16 remains
absent/skipped. The sole candidate is v17, which restores active-v2
R10/R11 acquisition order, separates successful cleanup from failure
unwind, and otherwise carries the scope-corrected v15 M1--M5/m1 mechanism.
It changes no public form/count/HC coordinate and grants no source or run
authority. Only a later independent PASS_C0_M0_m0 may activate v15 and v17
jointly.
