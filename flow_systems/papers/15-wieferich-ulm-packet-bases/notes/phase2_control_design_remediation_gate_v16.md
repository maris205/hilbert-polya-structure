# Replacement Paper 15 control-design remediation gate v16

Status: **PASS TO ONE VERSIONED DESIGN AMENDMENT v16 ONLY, FOLLOWED BY
ONE FRESH INDEPENDENT APPEND-ONLY COMPLETE DESIGN REREVIEW**
Date: 2026-08-18 (Asia/Shanghai)
Gate class: notes-only dependent corrigendum governance for candidate v15
Current effective design verdict: PASS_C0_M0_m0 for
base + v1--v11 + v13 + v14 only
Candidate-v15 review verdict: REVISE_C0_M5_m1
Controlling implementation-gate verdict: STOP_DESIGN_REOPEN_REQUIRED
Current effective-amendment count: 13
Source, implementation, implementation-review, platform-preflight,
execution, generated-artifact, result, proof, Route, manuscript, release,
archive, and Git authority: **none**
Universal prime recovery: **OPEN_NOT_AUTHORIZED**

This gate authorizes one later notes-only v16 amendment and, only after its
external stable freeze, one fresh independent append-only complete design
rereview. It does not make candidate v15 effective. Candidate v16 is a
dependent corrigendum: only a later PASS_C0_M0_m0 review of the exact
base + active-thirteen + candidate-v15 + candidate-v16 tuple may activate
v15 and v16 jointly and publish count 15. Any other result leaves the active
tuple and count exactly unchanged.

## Material Passport

- **Material type:** one bounded design-remediation governance gate.
- **Sole gate-author write:** this v16 gate path.
- **Frozen adverse finding:** the current complete design review ends in
  REVISE_C0_M5_m1 for candidate v15.
- **Exact repair surface:** P15R-V15-M1 through M5 and P15R-V15-m1 only.
- **Preserved v15 core:** fixed FD12 P self-pidfd; validation-only FD13
  initial-proc P directory; immutable fork/COW receipt; Linux-5.15 POLLIN
  whole-thread-group-exit semantics; the complete v14 P_CRASH guard; and
  the G-child close-only transient.
- **Closed M1--M3 repair:** preclassify every target 10--13 before staging;
  separate transaction phase, reference role/disposition, and lifetime
  phase; and bind transaction and per-reference identities without scalar
  ambiguity.
- **Closed M4 ceiling:** pidfd fstat is class/type sanity only. Target/OFD
  authority comes from P-side identity plus the complete trusted lineage,
  never singleton-anon-inode fstat.
- **Closed M5 candidate:** root probe precedes capability acquisition; P
  closes its B-side alias and its own FD13/12 copies before U1 ACK; L
  publishes a one-use release through the already-inherited bootstrap
  B-side OFD by an O_NONBLOCK marker plus local SHUT_RD; G consumes that
  exact no-HUP transition before identity, connect, or PID1_READY; P
  independently audits parked live L before accepting PID1_READY.
- **No new form:** the inherited bootstrap sequence remains the same five
  forms, directions, payloads, byte grammar, and cardinalities. Only the
  fifth form's send cut moves.
- **Finding posture:** this gate closes no finding and predicts no review
  verdict.
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
syntax-checked, probed, or run. No generated, result, cache, temporary,
lock, manifest, or Git object was created.

### 1.2 Effective design chain and candidate records

The currently effective tuple remains the base plus thirteen active
amendments. Amendment v5 is active no-op provenance. Amendment v12 remains
absent and skipped.

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

The v14 remediation gate remains consumed evidence at 1665 lines, 84029
bytes, SHA-256
cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292.
It supplies no v16 write authority.

### 1.3 Current complete review and exact v15 findings

The current design review is a regular mode-0644, nlink-one file:

    path=notes/phase2_control_design_peer_review.md
    lines=6965
    bytes=375778
    sha256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5

Its preserved v14 PASS remains historical evidence for the active-thirteen
tuple. Its final v15 block has exact verdict REVISE_C0_M5_m1:

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

### 1.4 Controlling implementation STOP

| Record | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| ATTEMPT_3 implementation peer review | 643 | 37947 | 637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88 | REVISE_C0_M12_m0 |
| implementation remediation gate v5 | 733 | 31304 | 411d33fba7fe9aa50965c7e3e293a4994b27f386b4b61afcb8745e2fe0db01f7 | STOP_DESIGN_REOPEN_REQUIRED |

All twelve implementation findings remain open. ATTEMPT_4 remains
unconsumed only because its plan was rejected before admission and its
source-mutation count is zero. It is suspended and unavailable throughout
this gate, amendment, and rereview sequence.

### 1.5 Exact six-source immutable quarantine

| Frozen path | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| code/generate_controls.py | 1133 | 60497 | 4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020 |
| code/test_controls.py | 1655 | 129574 | c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac |
| code/README.md | 95 | 5267 | 96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee |
| experiments/reproduce.sh | 6270 | 469357 | dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59 |
| experiments/README.md | 226 | 14697 | ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6 |
| results/README.md | 76 | 3221 | 03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c |

They total 9455 lines and 682613 bytes. Each is regular mode 0644, nlink 1.
They are quarantine, not design authority or conformance evidence.

Immediately before this gate's sole Add-File write, the v16 gate target was
absent under ordinary and symlink-aware checks. Any pre-existing, symlink,
hardlink, nonregular, or drifted target was a mandatory pre-write STOP.

## 2. Exact dependent-corrigendum scope

The one future v16 amendment may do only the following:

1. correct v15 M1--M3 with a mechanically closed four-object staging and
   reference algebra;
2. correct v15 M4 by reducing pidfd fstat to class evidence and freezing the
   authoritative lineage;
3. correct v15 M5 with the exact root-probe, U1, B-OFD release, G-consume,
   and P live-L audit cuts in this gate;
4. correct v15 m1's parent-child sentence;
5. restate only the mechanically coupled holder, D-M2, HC, P_CRASH, count,
   and narrow-predecessor consequences; and
6. prove that all unmentioned active obligations remain exact.

V16 may not add an actor, process, endpoint, wire form, field, ancillary
item, FD slot, pipe, eventfd, socket, path, service, shared mapping, memfd,
file, environment bearer, reconnect, retry, fallback, persistence object,
classifier coordinate, result, schema item, manifest member, or DAG edge.

The v15 choices that remain candidate inputs are FD12, FD13, the immutable
identity receipt, ordinary fork/COW lineage, exact terminal poll, the
complete P_CRASH guard, G-child transient close order, and unchanged public
counts. V16 must explicitly supersede the defective v15 clauses; it may not
call v15 effective or silently inherit a contradicted statement.

## 3. Root-probe and acquisition placement

The active v2 root probe must not inherit FD12 or FD13. The exact order is:

    root probe fully killed and reaped
    -> duplicate-wait/process-gone proof
    -> probe cgroup populated=0 and exact removal
    -> no probe or other pre-L child remains
    -> acquire and install the four setup/control objects
    -> bind the existing listener
    -> create the existing bootstrap SOCK_SEQPACKET socketpair
    -> clone L

The already-authorized P-only LONG_LIVED_PROC_ROOT may remain open. If it
or any other unrelated descriptor occupies target 10--13, Section 4
requires STOP before destructive staging. No alternate slot or remap is
authorized.

## 4. Target preclassification and four-object transaction

### 4.1 Closed object, target, and reference domains

The complete object-kind enum is:

    REPOSITORY_SOURCE_ROOT
    PACKAGE_SOURCE_ROOT
    P_SELF_PIDFD
    P_INITIAL_PROC_PID_DIR

The four target bindings remain exact:

| Target | Object kind |
|---:|---|
| 10 | REPOSITORY_SOURCE_ROOT |
| 11 | PACKAGE_SOURCE_ROOT |
| 12 | P_SELF_PIDFD |
| 13 | P_INITIAL_PROC_PID_DIR |

The complete target-occupant classification is:

    VACANT_EBADF
    TRANSACTION_RAW_REFERENCE
    FORBIDDEN_THIRD_PARTY

Inside one single-threaded, signal-controlled, no-allocation barrier, after
all four raw references are ledgered and before the first
F_DUPFD_CLOEXEC, P classifies each target 10--13.

VACANT_EBADF requires F_GETFD=-1 and errno EBADF. A
TRANSACTION_RAW_REFERENCE requires the target integer to equal the exact
current local_fd of one ledgered R10--R13 reference and requires its flags,
type, object kind, and object receipt to match that reference. Every other
open occupant is FORBIDDEN_THIRD_PARTY.

LONG_LIVED_PROC_ROOT, listener, bootstrap endpoint, control endpoint,
signalfd, cgroup/namespace FD, unrelated pidfd, or any unclassified object
at 10--13 causes E_POSSESSION_UNAVAILABLE before the first staging
duplicate. It is neither overwritten nor added to the four-source
transaction. Immediately before each dup3, the still-applicable target
occupant must be rechecked against its frozen classification. Drift stops
before that destructive syscall.

### 4.2 Separate phase, role, and disposition algebras

V16 must not use one state enum for transaction progress, reference
liveness, and P-lifetime progress.

The closed reference-role enum is:

    RAW
    HIGH_STAGE
    FIXED_TARGET
    INHERITED_ACTOR_COPY

The closed reference-disposition enum is:

    LIVE_UNVALIDATED
    LIVE_VALIDATED
    DISPLACED_BY_TARGET
    CLOSED_PROVED
    OWNER_DIED_RELEASED
    AMBIGUOUS_CRASH_ONLY

The closed transaction-phase enum is:

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

The closed lifetime-phase enum for only the P-lifetime objects is:

    P_INSTALLED
    L_INHERITED
    P_RELEASE_HB_FIXED
    G_INHERITED
    L_RELEASE_HB_FIXED
    G_IDENTITY_VALIDATED
    G_PIDFD_ARMED_PROC_CLOSED
    P_EXIT_OBSERVED
    TERMINAL_CLOSED

DISPLACED_BY_TARGET is a terminal reference disposition. It is not a
transaction phase, not a live close, and not an owner-death result.
CLOSED_PROVED requires an actual close return 0 followed immediately by
F_GETFD=-1/EBADF with no allocation in between.

### 4.3 Exact reference identity grammar

Every raw, stage, target, and inherited reference entry binds:

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

The exact reference identity is:

    reference_id=(transaction_serial,issuer_actor,reference_serial)

transaction_serial is P-owned, monotone, nonzero, and never reused.
reference_serial is nonzero, monotone, and never reused in its actor domain.
parent_reference_id=NONE is legal only for raw references. A high stage
points to its raw; a fixed target points to its high stage; an inherited
copy points to its actual parent copy. Fork/COW must not create ambiguous
equal IDs: P pre-reserves the deterministic L/G copy identities before
fork, and each G-child copy uses the already-governed unique child-creation
serial. Wrap, duplicate, missing parent, actor mismatch, or cross-object
parentage yields ABORT_AMBIGUOUS.

The immutable P identity receipt replaces v15's single ambiguous scalar
with at least:

    transaction_serial
    pidfd_raw_reference_id
    pidfd_stage_reference_id
    pidfd_target_reference_id
    procdir_raw_reference_id
    procdir_stage_reference_id
    procdir_target_reference_id

G joins inherited slot 12 separately to pidfd_target_reference_id and
inherited slot 13 separately to procdir_target_reference_id. No scalar may
stand simultaneously for transaction, pidfd, and procdir identity.

### 4.4 Stage, install, cleanup, and unwind

The transaction order is:

1. ledger R10--R13 and their distinct reference IDs;
2. classify all target occupants;
3. create H10--H13 in target order with F_DUPFD_CLOEXEC lower 64;
4. validate all four raw-to-stage joins before any low install;
5. dup3 H10--H13 to 10--13 in ascending order with O_CLOEXEC;
6. after each successful dup3, create a new FIXED_TARGET reference;
7. if that dup3 displaced a transaction raw occupant, mark that raw
   DISPLACED_BY_TARGET with the target reference and syscall serial;
8. validate all four target references;
9. reverse-close all stages and every still-live nondisplaced raw; and
10. enter SLOTS_INSTALLED only when every reference has a legal terminal
    success disposition.

A failed dup3 does not displace its old target occupant. A displaced raw
integer is stale and must never be closed. Success and every partial failure
use one serial-driven reverse unwind: installed targets in reverse order,
live stages in reverse order, then live nondisplaced raws in reverse order.
Displaced references are recorded but not closed again. An ambiguous close
enters ABORT_AMBIGUOUS and forbids clone L.

## 5. Bootstrap A/B identity and baseline

The existing inherited bootstrap socketpair is named only for this
corrigendum:

    A = P-side peer endpoint/OFD
    B = L-to-G inherited endpoint/OFD

This naming adds no endpoint or record. Bfd is the existing receipt-bound
local integer and must not equal 10, 11, 12, or 13. Before clone L, P
freezes:

    B0=fcntl(B,F_GETFL)
    (B0 & O_NONBLOCK)==0
    B has FD_CLOEXEC
    B is the expected SOCK_SEQPACKET sockfs object
    A and B are distinct endpoint/open-file descriptions

The immutable B receipt, including B0, Bfd, socket identity, endpoint role,
and CLOEXEC, passes to L and G only through existing fork/COW memory.

P must close its B alias and prove EBADF before processing U1_CREATED. L
must close its A alias and prove EBADF before its first U1 record. After
those cuts only P owns A; L later forks G so L and G hold distinct local
FD-table references to the same B open file description.

Only L's one Section-7 F_SETFL and one Section-7 SHUT_RD are authorized to
mutate B. P cannot mutate B through A. G and every other actor are forbidden
from F_SETFL, FIONBIO, shutdown, dup, SCM_RIGHTS, replacement, exec,
registration, or transfer of B.

## 6. P-to-L release through the existing U1 ACK

The exact P sequence after successful clone3 parent return is:

    close P's B alias -> immediate EBADF
    -> close(13)=0 -> immediate F_GETFD(13)=-1/EBADF
    -> close(12)=0 -> immediate F_GETFD(12)=-1/EBADF
    -> only then process the already-queued U1_CREATED
    -> write and re-read the exact U1 maps
    -> send existing U1_MAPS_COMMITTED

L remains blocked after U1_CREATED until it receives that exact ACK.
Therefore:

    P FD13/12 close receipts
    happens-before U1_MAPS_COMMITTED enqueue/receive
    happens-before every later L U2 action
    happens-before L forks G

Any P close, EBADF, U1 map, or send failure forbids the ACK and enters
bootstrap containment. The existing ACK receives no new field or form.

## 7. L-to-G release through the shared B OFD

### 7.1 Retimed fifth bootstrap form

L still completes the exact U2 uid/gid map writes, re-reads, inner-id checks,
empty-groups check, and U2_ROOT0_MAPPED local state before fork G. It does
not yet send U2_MAPS_COMMITTED.

After the sole fork of G, the L parent performs:

    close(13)=0
    -> immediate F_GETFD(13)=-1/EBADF
    -> close(12)=0
    -> immediate F_GETFD(12)=-1/EBADF
    -> fcntl(B,F_GETFL)==B0
    -> fcntl(B,F_SETFL,B0|O_NONBLOCK)==0
    -> fcntl(B,F_GETFL)==B1
       where (B1 xor B0)==O_NONBLOCK
    -> one sendmsg of the existing exact framed U2_MAPS_COMMITTED
    -> exact full framed length return
    -> shutdown(B,SHUT_RD)==0

Because the marker precedes the send, the send is nonblocking. The complete
length prefix and payload must be one exact sendmsg operation. EAGAIN,
EWOULDBLOCK, EINTR, a short return, zero, or any other error is fatal. There
is no retry. U2_MAPS_COMMITTED remains the fifth and final inherited
bootstrap form, occurs exactly once, remains L-to-P, and retains its exact
payload, fields, and bytes.

The O_NONBLOCK marker alone is not release authority. SHUT_RD alone is not
release authority. Their exact conjunction after the close receipts and
full U2 send is the one governed L-origin release transition.

### 7.2 G's sole pre-release action and predicate

Immediately after fork, G may perform only the governed barrier operations
ppoll, F_GETFL, recvmsg(MSG_DONTWAIT), and the final close/EBADF on B.
Before release it may not validate FD12/13, mount proc/private state,
connect, send PID1_READY, allocate or close another FD, mutate B, or perform
other work.

G blocks on:

    ppoll(B,events=POLLIN|POLLRDHUP,existing bootstrap deadline)

A normal L release requires all of:

    poll return identifies only B
    (revents & POLLIN) != 0
    (revents & POLLRDHUP) != 0
    (revents & (POLLHUP|POLLERR|POLLNVAL)) == 0
    fcntl(B,F_GETFL) == B1
    recvmsg(B,one-byte nonzero buffer,MSG_DONTWAIT) == 0
    payload bytes consumed = 0
    ancillary count = 0
    MSG_TRUNC and MSG_CTRUNC absent

Additional nonfatal readiness bits do not require exact revents equality.
POLLHUP always has precedence and forbids the normal release branch even if
the marker and required bits are also visible. Timeout, EINTR, error,
partial/positive data, ancillary data, flag drift, or ambiguity is bootstrap
failure, never success or life/death evidence.

After the exact predicate, G closes B, performs no intervening allocation,
and proves Bfd F_GETFD=-1/EBADF. Only then may it validate FD12/13, perform
the initial FD12 nonready poll, close FD13/EBADF, prepare its private mount,
connect to the existing listener, and send PID1_READY.

Peer EOF, peer close, P death, a zero-time FD12 poll, marker visibility
alone, or a F_GETFL busy loop is not this release predicate.

### 7.3 P's independent live-L holder audit

P receives and validates the exact post-close U2 frame before accepting G.
Before accept() of the G connection and before accepting PID1_READY, P
enters one single-threaded, signal-controlled allocation barrier. It does
not accept, receive an FD, read signalfd, or perform another allocation
during the audit.

P requires the launcher pidfd nonready and uses only its existing trusted
outer proc root and bound L outer PID to obtain transient L PID/stat/fd
observation references. Each successful returned FD is immediately entered
with an acquisition serial in a separate private
BOOTSTRAP_L_PROC_AUDIT_LEDGER before validation.

P brackets two complete canonical L FD-number snapshots with exact launcher
pidfd, outer PID, field-22 starttime, NSpid, credential, and guardian
identity checks. Both snapshots must be byte/set equal. Parked live L's
exact allowlist is:

    FD10
    FD11
    bootstrap Bfd

FD12 and FD13 must be absent. No extra integer or alias is legal. P reads
L's fdinfo for Bfd and requires the frozen socket/inode/mount lineage,
descriptor CLOEXEC, and file-status flags corresponding to B1. Proc fdinfo
includes descriptor CLOEXEC in its printed flags, so its numeric value is
not compared naively with F_GETFL B1. P must parse the distinct flag
domains. P never follows or reopens /proc/L/fd/Bfd and never duplicates B.

All transient proc audit references are reverse-closed with immediate
EBADF. They are P-local, pre-accept, noninherited, nonendpoint, and outside
D-M2's 21 tags. L death, identity drift, snapshot drift, missing B, present
12/13, extra FD, flag mismatch, partial read, close ambiguity, or failed
unwind forbids accept and enters guardian/bootstrap containment.

### 7.4 L park, A close, and final bootstrap disposal

After normal SHUT_RD, L retains B and performs no FD allocation,
duplication, replacement, clear-marker action, or new process creation. It
parks using poll(B,events=0) for the existing P-side final close.

G never reads bootstrap EOF. Clean EOF is not G authority. P retains A
through the existing CONTROL_AUTHENTICATED and cgroup-preflight/launcher
exit cut, then performs the original final A close. This full peer shutdown
produces POLLHUP for parked L. L requires that HUP, closes B with immediate
EBADF, completes the unchanged launcher-exit duties, and exits; P then
pidfd-reaps L before LAUNCHER_REAPED.

On a normal release L must not use SHUT_RDWR. After marker publication, if
U2 send, SHUT_RD, or a validation fails, L uses fatal containment so G sees
HUP; HUP precedence prevents the marker from becoming a false normal
release.

## 8. Exact holder matrix

| Cut | P-lifetime FD12 holders | P-procdir FD13 holders | Required proof |
|---|---|---|---|
| post-install, pre-clone | P | P | transaction and receipt complete |
| clone-L kernel window | P,L | P,L | no CLONE_FILES; no exec |
| post-U1 ACK receive | L | L | P B/13/12 closes precede ACK |
| fork-G kernel window | L,G | L,G | same B OFD; separate FD tables |
| B release observed by G | G | G | L closes precede marker, U2, SHUT_RD |
| G identity validated | G | G | lineage and class checks complete |
| pre-PID1_READY | G | none | G closes FD13 and proves EBADF |
| steady carrier | G only | none | FD12 fixed and nonreplaceable |
| trusted G-child fork instant | G plus child transient | none | EP_G-first then FD12 close-only stub |
| child SANITIZED/registered | G only | none | child has no 12/13 |
| terminal after endpoint duties | none | none | G closes FD12 last and proves EBADF |

The P audit independently confirms L's absence before P accepts the G
connection. It does not replace the G-visible B release. The B marker and
local read shutdown are pre-auth bootstrap facts, not endpoint custody.

## 9. Pidfd evidence ceiling and trusted lineage

The v16 amendment must replace pidfd_type_and_fstat_identity with a
class-only receipt, for example:

    pidfd_class_fstat_receipt
    pidfd_fstat_is_unique_identity=false
    pidfd_fstat_is_target_identity=false
    pidfd_fstat_is_same_ofd_proof=false

Linux 5.15 ordinary pidfds use the shared singleton anonymous inode.
st_dev/st_ino/st_mode can reject a directory or socket class and support
flags/type sanity. They cannot distinguish two pidfds, prove target P, or
prove same open file description.

The authoritative P binding is the conjunction of:

1. P-side pidfd_open(canonical getpid(),0);
2. P-side fdinfo Pid equality in the initial PID namespace;
3. initial-proc directory object and field-22 starttime;
4. exact transaction and per-reference IDs;
5. raw-to-stage-to-target parent-reference chains;
6. ordinary fork with no CLONE_FILES and no exec;
7. P's U1 happens-before;
8. L's B marker plus local SHUT_RD happens-before;
9. P's independent live-L FD audit;
10. a gapless no-close/no-dup/no-replace FD12 invariant;
11. close-only handling of every G-child transient; and
12. terminal poll on that lineage-bound fixed FD12.

G has no independent exact OFD comparator. The same-OFD claim is a static
trusted-program lineage invariant under the unchanged conditional,
unverified deployment-model ceiling. A wrong live pidfd with the same
anon-inode fstat, G fdinfo Pid:0, and initial nonreadiness is not excluded by
those observations alone.

## 10. D-M2 and endpoint-custody claim ceiling

Every steady complete G snapshot after PID1_READY still requires FD12
present and FD13 absent. D-M2 may claim:

    D_M2_PROVES_FD12_SLOT_PRESENT=true
    D_M2_PROVES_FD12_CLOEXEC_AND_CLASS=true
    D_M2_PROVES_FD12_NONSOCKET=true
    D_M2_PROVES_SNAPSHOT_SET_STABILITY=true
    D_M2_PROVES_G_FD_GENERATION_STABILITY=true

It may not claim:

    D_M2_PROVES_PIDFD_TARGET_P=false
    D_M2_PROVES_UNIQUE_PIDFD_OFD_BY_FSTAT=false
    D_M2_PROVES_INDEPENDENT_LINEAGE=false

FD12 remains excluded from the socket candidate selector, pidfd_getfd
target set, row ledger, and tag-18 unwind. FD13 remains absent. The
bootstrap B release ledger and transient L-proc audit ledger do not enter
D-M2.

The exact counts remain:

    D_M2_FIXED_TAG_COUNT=21
    D_M2_CONTROL_FORM_COUNT=4
    D_M2_FRESH_PROC_LEDGER_SLOTS=4
    D_M2_CHILD_DUPLICATE_SLOTS=1
    WORKER_FDSET_VALUE_COUNT=4

B is closed in G before the actual P--G control connection and is fully
closed in P/L before LAUNCHER_REAPED. It is not EP_P, EP_G, an endpoint
alias, or a holder-freeze member. FD12 remains nonendpoint; FD13 remains
pre-carrier gone. Therefore the exact HC profile remains:

    HOOK_CUSTODY_PROFILE_ITEM_COUNT=41
    HOOK_CUSTODY_PROFILE_PREIMAGE_BYTES=2928
    HOOK_CUSTODY_PROFILE_SHA256=1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1

Any B survival into the actual control holder window, FD13 survival past
PID1_READY, FD12 endpoint operation, duplicate/registration/transfer, or
different synchronization object reopens HC and is outside this gate.

## 11. P_CRASH and parent-child correction

The exact FD12 terminal predicate and complete twelve-part P_CRASH guard
from candidate v15 remain candidate obligations. B release, bootstrap HUP,
U2, the P L-audit, initial nonreadiness, or EOF is not a C14 coordinate,
raw17 bit, P-exit proof, or terminal success.

The exact normative sentence is:

    P is not G's child. After L is reaped, G is normally P's
    descendant/adopted child in the outer PID namespace because P is the
    child subreaper.

Therefore G cannot wait or reap P, and ECHILD is not P-death evidence. P may
reap the adopted G in the lawful direction. Pidfd polling itself neither
waits nor reaps.

## 12. Frozen public algebra and package vector

The following remain exact:

    C14_COORDINATES=RE,YE,AE,SS,E_PG,E_GP
    C14_VECTOR_COUNT=15
    C14_FAILURE_VECTOR_COUNT=14
    C14_SUCCESS_VECTOR_COUNT=1
    C14_SUCCESS_VECTOR=111100
    RAW_CLASSIFIER_PREDICATE_COUNT=17
    RAW_BITS_COMPUTED_BEFORE_WINNER=true
    ALL_TRUE_LOSER_BITS_RETAINED=true

    INHERITED_BOOTSTRAP_FORM_COUNT=5
    V16_NEW_WIRE_FORM_COUNT=0
    GLOBAL_BOOTSTRAP_FORM_DELTA_VS_V2=PLUS_THREE
    GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=3
    D_M1_FD5_FORM_COUNT=12
    D_M1_P_G_SESSION_FORM_COUNT=12
    D_M2_QUIESCENCE_FORM_COUNT=4
    ADMIT_FORM_COUNT=1

The scientific/package vector remains:

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

AUTHORITY_BINDINGS=14 is a package binding count, not the design-amendment
count.

## 13. Exact narrow supersessions required in v16

The one future amendment must explicitly supersede or clarify:

1. v15 Sections 3 and 6: target preclassification, reference algebra,
   transaction phases, dispositions, and serial grammar.
2. v15 identity-receipt fields: separate transaction/pidfd/procdir
   reference identities.
3. v15 pidfd fstat language: class sanity only; no exact target/OFD claim.
4. v15 holder matrix and local-close prose: replace interpretation with the
   exact U1 and B-OFD happens-before edges.
5. v15 wait rationale: P is not G's child.
6. v2 step 1: root probe finishes before FD12/13 acquisition.
7. v2 step 2: exact A/B alias closure and P B/13/12 close-before-U1 order.
8. v2 step 5: U2 map work remains pre-fork, but the sole
   U2_MAPS_COMMITTED send moves post-fork and post-L-close.
9. v2 step 6: G's first work is the governed B release wait and consume.
10. v2 step 7: G closes B before identity/connect/PID1_READY; P audits live
    L before accept/ready acceptance.
11. v2 bootstrap-close sentence: G B closes pre-connect; L B retains local
    read shutdown until P's original post-auth/preflight A close.
12. v2 step 10: L's final B close/EBADF, exit, and P reap remain before
    LAUNCHER_REAPED.
13. v6 D-M2: FD12 class/set/generation claim ceiling and separate ledgers.
14. v14 terminal/HC: unchanged only under the exact pre-carrier cuts here.
15. v14 effective-count governance: only a joint v15+v16 zero-finding
    review may publish count 15.

No blanket supersession of v2, v6, v14, or v15 is authorized. Every
unmentioned predecessor obligation remains exact.

## 14. Mandatory hostile counterexamples

The amendment author must state, and the fresh reviewer must independently
attack, at least all of these fixed pairs:

| # | Hostile case | Required disposition |
|---:|---|---|
| 1 | target 12 is LONG_LIVED_PROC_ROOT | STOP before staging; never overwrite |
| 2 | target 13 is listener/bootstrap/signalfd | same STOP |
| 3 | target classified then drifts | recheck fails before dup3 |
| 4 | target is exact R12/R13 raw | stage protects it; successful dup3 records displacement |
| 5 | dup3 fails | old occupant stays live; no displacement claim |
| 6 | code closes a displaced stale integer | forbidden; it would close the new target |
| 7 | R10/R11 lacks object kind | schema failure |
| 8 | stage/target/inherited copy lacks role | schema failure |
| 9 | transaction and two capabilities share one serial | receipt ambiguity |
| 10 | post-fork actor IDs collide | actor-qualified identity failure |
| 11 | root probe exists after FD12/13 acquisition | holder-contract failure |
| 12 | P sends U1 ACK before closing B/13/12 | ACK guard failure |
| 13 | G runs before L parent | it remains blocked in ppoll |
| 14 | B initially has O_NONBLOCK | baseline failure before clone |
| 15 | Bfd equals 10--13 | registry collision STOP |
| 16 | actor other than L sets/clears B flags | forbidden mutation |
| 17 | L sets marker before closing 13/12 | release-state violation |
| 18 | marker alone is treated as release | reject; SHUT_RD/no-HUP conjunction required |
| 19 | L sends U2 before marker or retries | state/cardinality failure |
| 20 | nonblocking U2 send is short/EAGAIN/EINTR | fatal, no retry |
| 21 | L uses normal-path SHUT_RDWR | HUP/failure, never normal release |
| 22 | P dies before marker | HUP precedence; no normal release |
| 23 | P dies after marker before SHUT_RD | HUP precedence; no normal release |
| 24 | HUP appears with IN/RDHUP and B1 | HUP wins; no normal release |
| 25 | G uses F_GETFL spin or peer EOF as authority | forbidden |
| 26 | G writes/clears marker or calls shutdown | forbidden |
| 27 | recvmsg yields data/cmsg/truncation | bootstrap failure |
| 28 | G validates/connects before B close/EBADF | state violation |
| 29 | P accepts before U2/live-L audit | authentication guard failure |
| 30 | L fdinfo flags compare naively to F_GETFL | reject mixed descriptor/status domains |
| 31 | live L snapshot contains 12 or 13 | no accept; containment |
| 32 | live L snapshot has an extra alias | no accept; containment |
| 33 | L dies or identity drifts during audit | no accept |
| 34 | L closes B before P audit | allowlist failure |
| 35 | wrong pidfd shares anon-inode fstat | fstat cannot prove target |
| 36 | wrong live pidfd also shows Pid:0 and nonready | only trusted lineage may exclude it |
| 37 | D-M2 claims fstat proves P/same OFD | overclaim; nonaccepting |
| 38 | G waits P and uses ECHILD as death | forbidden |
| 39 | FD13 survives PID1_READY in any actor | HC-reopening STOP |
| 40 | FD12 ready after finalized row-15 success | no classifier backflow |
| 41 | FD12 ready without holder/EOF/drain/reconciliation | exit-only evidence |
| 42 | B enters EP_P/EP_G, D-M2, or HC | scope violation |
| 43 | form count, C14/raw17, package vector, or DAG changes | separate authority required |

Missing a pair, weakening HUP precedence, or replacing exact evidence with a
timeout, plausible schedule, comment, hash, or self-authored constant is
nonaccepting.

## 15. One v16 amendment and one independent rereview

### 15.1 Amendment authority

Only after an external coordinator freezes this gate's actual regular-file
receipt may one design author create:

    notes/phase2_control_design_amendment_v16.md

The target must still be absent under ordinary and symlink-aware checks.
The author receives exactly one notes-only Add-File apply_patch attempt.
There is no draft path, temporary path, overwrite, rename, second attempt,
or design-author handoff.

The amendment author must full-read this gate, candidate v15 gate/amendment,
the complete current review, base and every active amendment, v5 STOP,
ATTEMPT_3 review, and the exact quarantine. The amendment must implement
Sections 3--14, retain every actual input digest, make no PASS claim,
predict no self hash, and authorize no source, review append, or run.

### 15.2 Fresh append-only complete rereview

Only after an external coordinator freezes the actual v16 amendment may one
fresh reviewer independent of both authors append one block to:

    notes/phase2_control_design_peer_review.md

The required preserved prefix is:

    lines=6965
    bytes=375778
    sha256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5

Prefix rewrite, insertion, deletion, relocation, truncation, replacement,
or a second review attempt is forbidden. The reviewer reads the complete
base + active-thirteen + frozen-v15 + frozen-v16 tuple and every governing
record, independently attacks all hostile pairs, and re-derives target
closure, ledgers, serials, Linux-5.15 B/pidfd semantics, holder sets, D-M2,
HC, C14/raw17, forms, and package/DAG counts.

The sole accepting verdict is:

    PASS_C0_M0_m0

Any finding, uncertainty affecting exact closure, missing pair, authority
mismatch, prefix drift, conditional waiver, REVISE, FAIL, STOP, or
incomplete append is nonaccepting.

### 15.3 Joint-activation marker

Neither this gate nor v16 may make v15 effective. Only the later
zero-finding reviewer may append:

    [P15R-EFFECTIVE-DESIGN-AMENDMENTS v13]
    count=15
    entries 1..11 = amendments v1..v11 at frozen hashes
    entry 12 = amendment v13 at 4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27
    entry 13 = amendment v14 at b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c
    entry 14 = amendment v15 at 158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239
    entry 15 = amendment v16 at its external stable hash
    amendment v12 = absent and skipped
    [/P15R-EFFECTIVE-DESIGN-AMENDMENTS]

Marker version v13 is the next unused effective-marker version; count 15 is
the joint active-amendment count. A non-PASS review publishes no marker and
leaves count 13.

## 16. Downstream nonauthority

This gate writes no amendment or review and authorizes no source edit,
implementation plan admission, implementation review, platform preflight,
runtime probe, generated member, result, proof, Route, composition,
manuscript, figure, release, archive, or Git action.

Even a future joint design PASS does not revive implementation gate v4 or
directly admit ATTEMPT_4. A separate owner decision and successor
implementation gate must bind the new complete design/review tuple, v5
STOP, all twelve implementation findings, the rejected old plan, the
unconsumed attempt state, and all six source hashes before deciding whether
implementation work exists.

## 17. External freeze and authorization matrix

An external coordinator, not this self-referential file, must compute and
freeze this gate's actual path, type, mode, nlink, lines, bytes, UTF-8,
terminal-LF, no-NUL result, and SHA-256. It must perform two complete
unchanged reads and reauthenticate the Section-1 inputs and six source
paths. Any drift, extra successor, symlink, hardlink, nonregular object,
predicted self digest, or post-receipt edit is STOP.

    P15R_CONTROL_DESIGN_REMEDIATION_GATE=P15R-P2-CONTROL-DESIGN-REMEDIATION-GATE-v16.0
    GATE_KIND=NOTES_ONLY_V15_DEPENDENT_CORRIGENDUM
    GATE_VERDICT=PASS_TO_ONE_VERSIONED_DESIGN_AMENDMENT_V16_ONLY

    CURRENT_DESIGN_REVIEW_SHA256=b7782bb497049540f5e31b3b8f332f3b92d80206f218f4b4000e05772fc655a5
    CURRENT_V15_REVIEW_VERDICT=REVISE_C0_M5_m1
    V15_GATE_SHA256=c067c23a4e807e121a849a1921eba2141499d7733666d1484f29332607c4180a
    V15_AMENDMENT_SHA256=158865dfe0235f4e959eaf697f0c09a605c02ae5abfa64dc62a78c32dc81c239
    V15_EFFECTIVE=false
    V16_IS_V15_DEPENDENT_CORRIGENDUM=true

    CURRENT_EFFECTIVE_AMENDMENT_COUNT=13
    SUCCESSOR_EFFECTIVE_COUNT_ONLY_IF_JOINT_PASS=15
    SUCCESSOR_EFFECTIVE_MARKER_VERSION=v13
    AMENDMENT_V12_PRESENT=false
    AMENDMENT_V12_SKIPPED=true

    TARGET_PRECLASSIFICATION_REQUIRED=true
    TARGET_PRECLASSIFICATION_TARGETS=10,11,12,13
    THIRD_PARTY_TARGET_OVERWRITE_AUTHORIZED=false
    TRANSACTION_OBJECT_KIND_COUNT=4
    REFERENCE_ROLE_COUNT=4
    REFERENCE_DISPOSITION_COUNT=6
    DISPLACED_BY_TARGET_IS_CLOSED_DISPOSITION=true
    TRANSACTION_AND_REFERENCE_SERIALS_DISTINCT=true

    ROOT_PROBE_PRECEDES_FD12_FD13_ACQUISITION=true
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
    V16_NEW_WIRE_FORM_COUNT=0
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

    AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v16.md
    AMENDMENT_V16_APPLY_PATCH_ATTEMPTS_AUTHORIZED=1
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

Final determination: **PASS TO ONE VERSIONED DESIGN AMENDMENT v16 ONLY,
FOLLOWED BY ONE FRESH INDEPENDENT APPEND-ONLY COMPLETE DESIGN REREVIEW.**
The authorized candidate is a dependent corrigendum to non-effective v15.
It closes no finding by author assertion, changes no public form/count/HC
coordinate, and grants no source or run authority. Only a later independent
PASS_C0_M0_m0 review may activate v15 and v16 jointly.
