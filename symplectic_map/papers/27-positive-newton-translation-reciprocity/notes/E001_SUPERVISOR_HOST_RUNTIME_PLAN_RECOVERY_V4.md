# Paper 27 E001 supervisor Host runtime plan recovery V4

Status: E0367-authorized inert Runner V4 author control. This file grants no
prebind PASS, formal-review, manifest, premise-certificate, issuer, gate,
test, microtest, execution, payload, build, evidence-root, PDF, release, or
publication authority.

All source records in this file are inert 7-bit ASCII/LF literals. V4
authorship never imports, tokenizes as a language, AST-parses, compiles,
evaluates, executes, launches, microtests, or submits any embedded byte to a
validator.

## 1. Sole authority and immutable identities

The sole authorizing record is exact E0367:

ledger_path=/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md
bytes=2319277
LF=23776
SHA256=8a072ddc741294f2322cc3a0a2f1f32ed07ea822f9bb93a0f4272497b4c0cf50
terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V3_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V4_AUTHOR_OPEN_NO_EXECUTION

A current mutable ledger is never a runtime identity. The only permitted
runtime ledger carrier is the separately constructed, anonymous, sealed
historical E0366 snapshot:

snapshot_name=B07_E0366_AUTHOR_OPEN
bytes=2303269
LF=23672
SHA256=0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92
terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V2_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V3_AUTHOR_OPEN_NO_EXECUTION

That carrier must be a regular memfd, nlink zero, uid/gid zero, open
read-write only for seal verification, and have exactly F_SEAL_WRITE,
F_SEAL_GROW, F_SEAL_SHRINK, and F_SEAL_SEAL. A and B bind its bytes, LF,
SHA, unique terminal, nlink, ownership, access mode, and seals. Neither may
stat or compare the current ledger. Exact snapshot construction remains an
external prerequisite; this file neither creates nor authorizes it.

The frozen Host inputs are:

Host_V15_path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15.md
Host_V15_dev=2431
Host_V15_ino=5916064615
Host_V15_mode=0100644
Host_V15_nlink=1
Host_V15_uid=0
Host_V15_gid=0
Host_V15_bytes=228310
Host_V15_LF=4622
Host_V15_SHA256=a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845
Host_V15_terminal=BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15_AUTHOR_STOP
Host_V8_SHA256=72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf

The five Host V15 raw spans remain:

source   bytes  LF    SHA256
OUTER    87151  1840  cfa1d88b312b7f4425778018be39cf7628568c9ddb39c697ff12b8b0f1c8be1a
KEEPER    4216   128  e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716
LAUNCHER  4218   128  e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5
MARKER   75094  1479  b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d
CHILD    19746   452  1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf

MARKER's embedded CHILD must equal the standalone CHILD byte-for-byte.

Frozen failed Runner V3 is immutable history, not execution authority:

V3_path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V3.md
V3_bytes=189292
V3_LF=2896
V3_SHA256=5552a25f953e13cd01fd467e79cf506fe0149a0b32d1c793c33dc14bce924dfa
V3_A=76971/1113/3a56c438fae58ecbb48bff7c19f61b682cc778d7456988dd33904ca93e0e4b2e
V3_C=9943/98/c3662ab9e09c133b79f80ca914e0650479d9d8c3a28b3f32da2520b0cb552190
V3_B=75004/1009/71647ce39758f59aef8eb3df2d1b5351ecf03437fa2138eedc557d5e980311d7

No V1, V2, V3, Host, Binder, actor, derivation, validator, manifest, paper,
or build/evidence/root byte gains authority from this document.

## 2. Hard non-executable prerequisites

The following independently frozen prerequisites are absent. Every one is a
launch blocker even if both V4 static reviews later PASS:

1. exact clone3 plus CPython post-clone continuation evidence;
2. exact deleted-cgroup held-dirfd and held-cgroup.events semantics;
3. exact construction and delivery procedure for the sealed E0366 snapshot;
4. exact external B survival and frozen terminal-owner transfer procedure;
5. exact outer reconciliation and no-replay receipt procedure;
6. exact issuer signature preimage, key identity, serial reservation,
   consumption, monotone receipt tokens, replay exclusion, and expiry policy.

Certificate PASS fields and 64-hex gate IDs are references to those future
artifacts, never self-certification. The certificate, issuer envelope, and
all gate artifacts require later exact identities, separated authority, and
their own review. Until then V4 is non-executable and manifest-ineligible.

## 3. Future outer-launcher obligation

Only a later ledger event may authorize one no-build launch. Its launcher
must authenticate the issuer and every gate before creating any process,
reserve exactly one serial, and create all sealed carriers without
normalization. It launches exactly one A with:

interpreter=/root/miniconda3/bin/python3
flags=-I -S -B -P -X utf8
source=/proc/self/fd/100
argv=[/proc/self/fd/100,RUN_V4,AUTH_ID]
cwd=certificate-bound safe-bind base
umask=0077
stdin=authenticated empty read pipe
stdout=dedicated raw result pipe
stderr=separate raw diagnostic pipe

The environment has exactly ten keys and no others:

LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
PYTHONIOENCODING=UTF-8:strict
PYTHONNOUSERSITE=1
PYTHONSAFEPATH=1
PYTHONUTF8=1
TZ=UTC

A receives exactly fd0, fd1, fd2, and:

fd100 sealed V4 A source
fd101 sealed exact E0366 snapshot
fd102 exact Host V15 regular file, read-only
fd103 sealed complete V4 plan
fd104 sealed premise certificate
fd105 sealed issuer envelope
fd106 sealed V4 B source

A closes 3..99 and 107..UINT_MAX and proves the exact remaining set.
Its launcher retains an A pidfd, concurrently drains A stdout and stderr to
EOF with separately authorized finite caps, rejects truncation or missing
EOF, and directly consumes A status once. It must keep stdin authentication
and all source/carrier identities stable through exec.

A parent watchdog must never treat killing only A as cleanup. Before BEGIN,
an exact refusal permits normal closure. Once BEGIN delivery may have
occurred, loss is unknown unless the exact state-bound refusal ACK proves
unconsumed. After COMMIT may have occurred, the parent must preserve B and
the frozen transfer owner, must not replay or retry, and must reconcile the
monotone issuer receipt. It may not close B's survival carrier, kill only the
top process, or infer descendant absence from A exit. Any external hard
deadline must enter the separately certified terminal-owner transfer; it
cannot invent a new local timeout or success.

## 4. Exact certificate, issuer, mount, and dependency law

AUTH_ID is exactly SHA256("P27E001V4" || NUL || certificate || NUL ||
issuer-envelope), represented by 64 lowercase hex. A and B parse the same
ordered certificate and issuer-envelope grammars. They independently bind
plan, A, B, snapshot, V15/V8, all Host source triples, all singleton
dependencies, every gate, every cap, all credentials, all bases and mounts,
all timing constants, and the complete DEP census. Duplicate, missing,
unknown, noncanonical, out-of-order, or trailing fields fail closed.

The issuer grammar binds ISSUER_ID=P27_HOST_PREMISE_ISSUER_V4, key ID,
authorization serial, certificate/plan/A/B hashes, exact E0366 snapshot
identity, V15 hash, absolute not-before/not-after, reserved and consumed
one-shot fields, signature algorithm, signature, and ENVELOPE_END=1.
Cryptographic verification and serial-state transition remain external.

The certificate binds realtime and monotonic samples with at most 1000000
ns drift and a 360000000000 ns absolute lifetime. Every boundary samples
monotonic-before, realtime, monotonic-after, checks absolute expiry and the
active absolute monotonic deadline, and preserves the typed causal fault.
An expiry checkpoint never converts an uncertain effect into refusal.

The runtime root is a separately bound, immutable read-only dependency
closure with exact dev/ino/mode/nlink/uid/gid, mount ID, mountinfo hash, and
filesystem type. Each required component is opened beneath a held root
through no-follow components; the six singleton roles and every canonical
DEP row are rehashed. The Python image and libc are bound by full identity;
LIBC_UID and LIBC_GID are both checked. No writable workspace, build,
evidence, user-site, cache, or unbound interpreter path is reachable.

The attempt base is separately bound read-write, root-owned mode 0700 and
has its exact mount identity. The safe-bind base is separately bound
root-owned mode 0700, read-write, nosuid,nodev,noexec, and has exactly one
authorized writable descendant. The cgroup2 mount/base is separately bound
by magic, mount graph, dev/ino/mode/nlink/uid/gid, type, controllers,
subtree_control, and no-external-mutator premise. Runtime root, attempt
base, safe bind, cgroup base, and child cgroup identities may not be
substituted or inferred from one another.

## 5. B bootstrap and exact authority split

A creates exactly one persistent B before BEGIN. It parks all source FDs at
distinct numbers >=200 before any dup2, maps only parked copies, closes the
parking bank, and closes every other FD. B receives exactly:

fd0 authenticated empty pipe, read-only
fd1 closed
fd2 closed
fd3 A/B SOCK_SEQPACKET
fd4 exact A pidfd
fd5 held attempt base
fd6 held cgroup base
fd7 sealed certificate
fd8 sealed issuer envelope
fd9 sealed E0366 snapshot
fd100 sealed V4 B source

B independently verifies all carrier bytes/seals/access, A pidfd identity,
peer credentials, exact FD set, limits/signals/credentials, full
certificate/envelope/dependency census, mount graph, attempt base, cgroup
base, and E0366 snapshot before READY. B does not trust A-provided hashes
for held stage or child-cgroup capabilities; each received capability is
checked against its named entry, held base, certificate, mount, owner, mode,
nlink, access mode, and exact control packet.

A alone authenticates and extracts Host V15, stages four leaves, creates the
child cgroup, performs raw clone3, observes the direct stopped child,
transfers the pidfd, sends SIGCONT, directly waits OUTER, and runs inert C
only in a future authorized process. B alone creates the attempt namespace
and records, binds all transferred capabilities, drains output, monitors
containment and pidfds, authorizes release, owns cleanup and the sole kill
effect, commits terminal records, and owns terminal closure. B has no
source extraction, staging creation, fork, clone, exec, SIGCONT, transcript
semantic validator, or direct wait authority. A has no attempt writer,
report writer, cgroup.kill writer, or descendant-cleanup substitute.

## 6. Consumption and attempt nonreuse state machine

A sets BEGIN_SEND_EFFECT_UNKNOWN and begin_effect_possible before the first
BEGIN send entry. A cannot infer unconsumed from send error, timeout, HUP,
or absence of ARMED. After any possible BEGIN effect, only an exact
version/auth/sequence/sender/current-state/current-ordinal/current-probe
REFUSE_ACK that echoes A's begin and arm states, B's state, the same consume
deadline, and disposition UNCONSUMED proves nonconsumption.

B sets ARM_SEND_EFFECT_UNKNOWN and armed_possible before the ARMED send.
After possible ARMED delivery, every loss other than the exact state-bound
REFUSE_PRECOMMIT/REFUSE_ACK exchange becomes CONSUME_EDGE_UNKNOWN. A sets
COMMIT_SEND_EFFECT_UNKNOWN, consumed=true, and PREFLIGHT=false before COMMIT
send entry. No later REFUSE, replay, replacement, second attempt, or serial
reuse exists.

A originates one consume_origin and consume_deadline. That exact
100000000 ns horizon is carried without restart through BEGIN, ARMED,
COMMIT, B's mkdir, immediate no-follow open, full local verification,
publication, base fsync, intent write/fsync/reread/dir-fsync, CONSUMED
message, and A receipt. A helper, EINTR, or lost control message cannot
refresh it.

The attempt-FD state is exactly LOCAL_UNVERIFIED -> LOCAL_VERIFIED ->
PUBLISHED. Publication occurs only after the held FD and named entry match
by dev/ino/mode/nlink/uid/gid, access is read-only, and the directory is
root-owned mode 0700. A closes its own mutation-capable attempt-base handle
before READY. On mkdir collision B closes fd5 before any collision stat or
filesystem report; it announces only through the independent control and
survival capability. Neither side can inspect or mutate that namespace.
Every partial durable effect retains state/digest; no filename is retried.

## 7. Staging, capability transfer, and payload containment

A uniquely extracts OUTER, KEEPER, LAUNCHER, MARKER, and CHILD by raw
delimiters and exact bytes/LF/SHA. It proves MARKER's CHILD equals the
standalone CHILD. It creates exactly stage/AUTH_ID and four mode-0400
O_EXCL|O_NOFOLLOW leaves, rereads each held FD, checks its exact triple,
fsyncs each leaf and the directory, then transfers one held stage dirfd.
No normalized or reconstructed Host source is staged.

Every recvmsg places all SCM_RIGHTS integers immediately in an exhaustive
owner scope. Each local FD progresses through unverified, verified, and
individually published ownership; all untransferred integers close on every
return, exception, truncation, malformed ancillary, wrong count, or
deadline. stream_arm includes stdout, stderr, cgroup.events, and
cgroup.kill; pidfd_arm includes exactly one OUTER pidfd; stage and
containment transfers each include exactly one dirfd. Local cgroup.type,
controllers, subtree_control, root events, root kill, stage-leaf, mount, and
dependency FDs are all covered by immediate cleanup.

Per ordinal A creates one direct OUTER with
CLONE_INTO_CGROUP|CLONE_PIDFD. The child performs SIGSTOP before context
mutation. A directly observes the stopped status and child-cgroup
membership. B binds the pidfd before release by fdinfo Pid, /proc starttime,
stopped status, cgroup.procs membership, and readiness false; it repeats the
identity checks around the observations. It records
pidfd_exit_ready_observed separately and cannot confuse PID reuse with the
held pidfd.

If any payload may have been released, the first failure reserves and
consumes the sole safe kill authority even when population is None or late.
The kill ticket, cgroup.kill write-call entry, return, and postcheck all
remain inside the one inherited cleanup deadline. There is no second write
or new cleanup cap. Unobservable or nonempty containment after that cap
requires frozen external ownership, never success. B keeps draining both
streams through EOF while discarding beyond each 3145728-byte cap.

## 8. Suite and complete transcript validator

The suite and order are exact:

P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
slot_count=15
authorized_invocation_count=15

Each slot has one A-origin absolute release horizon. It covers arm, clone,
stopped observation, pidfd transfer/binding, durable release record,
SIGCONT, direct final wait, concurrent stdout/stderr drain through EOF,
cgroup-empty observation, exact RESULT plus frames, complete transcript
validation, validated record, ACK-intent record, ACK, and A receipt.
host_complete-to-ACK is at most 500000000 ns; the validated and ACK-intent
durable records both fit inside that same bound. A or B loss never opens a
replacement slot.

RESULT is one exact packet, bound to ordinal/probe, outer PID, pidfd binding
and exit-ready bits, lengths, hashes, EOF/overflow bits, cgroup empty,
release/return/host-complete/capture times, direct wait, raw status, parser
states, candidate/terminal states, and certificate expiry. It carries no
rights. Frames are exactly increasing STDOUT frames, then increasing STDERR
frames, then RESULT_END; every byte count and SHA is exact. Missing,
duplicate, reordered, over-cap, trailing, truncated, or ancillary-bearing
input fails closed.

C separates three layers: allowed transcript byte language, complete
structural grammar/cardinality/order, and semantic validation. An accepted
candidate requires all three ACCEPTED; prose meaning cannot broaden the
literal grammar.

P00 rebuilds the exact 251414-byte synthetic source as authenticated CHILD
plus LF, '#', and the exact x padding, then compares the reported SHA.
P01D-to-P01C appends exactly these 13 values in order:

libc_path_hex, libc_dev, libc_ino, libc_mode, libc_nlink, libc_uid,
libc_gid, libc_bytes, libc_sha256, libc_confstr_hex, python_image_dev,
python_image_ino, python_image_sha256

Index 9 is exactly libc_confstr_hex; indexes 5 and 6 equal the certified
LIBC_UID and LIBC_GID. P05 permits sequential PID reuse and binds its two
observations by order, status, raw child lines, held process observations,
and the containing transcript. It does not assert uniqueness. P08/P10
topology fields are accepted only as literal transcript claims checked by C;
the final report does not elevate them into host-global topology proof.

## 9. Exact control grammar and parser separation

SOCK_SEQPACKET packets have one LF and this ordered common header:

kind|version=4|auth_id=AUTH_ID|sequence=UDEC|sender=A-or-B|
current_state=STATE|current_ordinal=ORDINAL|current_probe=PROBE

The sequence is exactly previous+1 in each direction. The common current
fields must equal the packet-specific state/ordinal/probe fields. Every kind
has a literal ordered key tuple; unknown, duplicate, missing, empty,
noncanonical, reordered, trailing, wrong-sender, wrong-state, wrong-slot,
wrong-probe, wrong-sequence, or wrong-deadline input fails closed.

ABORT is an exact packet with sender, state, ordinal, probe, effect_state,
stage_present, release_disabled, terminal_deadline_ns, and canonical ordered
nonempty fault_set. Its byte language and ordered structure are checked
before semantic effect-state checks. Malformed ancillary is closed before
classification. A PASS_COMMITTED or ACK_SEND_EFFECT_UNKNOWN state cannot be
downgraded by a conflicting ABORT. Remote faults remain sticky and retain
their typed causal precedence.

All zero-rights and nonzero-rights receives use recvmsg. The ancillary
buffer covers MAX_RIGHTS; MSG_TRUNC, MSG_CTRUNC, malformed or duplicate
SCM_RIGHTS, unexpected rights, and wrong cardinality are distinct faults.
On POLLIN plus HUP/ERR, queued POLLIN is drained and parsed before loss is
classified. Both control endpoints are nonblocking and every send first
polls POLLOUT under the same absolute deadline, preventing control deadlock.

## 10. Integrated deadlines and exact arithmetic

Literal caps are:

PRECONSUMPTION_CAP_NS=10000000000
CONSUMPTION_AND_ATTEMPT_HORIZON_NS=100000000
STAGING_CAP_NS=10000000000
CONTAINMENT_BIND_CAP_NS=500000000
SLOT_TOTAL_NS=18164800000
SLOT_COUNT=15
FINAL_REMOVAL_REPORT_CAP_NS=1000000000
FINAL_CANDIDATE_RECORD_NS=100000000
TERMINAL_SEEN_RECORD_NS=100000000
FINAL_PASS_COMMIT_NS=100000000
FINAL_PASS_MARGIN_NS=10000000
TERMINAL_ACK_NS=500000000
A_RECEIPT_RECORD_NS=100000000
B_OWNER_CLOSURE_NS=500000000
FINAL_TERMINAL_TOTAL_NS=1410000000
CLEANUP_CAP_NS=2000000000

15 * 18164800000 = 272472000000.
100000000 + 100000000 + 100000000 + 10000000 + 500000000 +
100000000 + 500000000 = 1410000000.

The required certificate remainders are:

ENTRY_MIN_REMAINING_NS=295482000000
CONSUMPTION_MIN_REMAINING_NS=285482000000
PRE_STAGE_MIN_REMAINING_NS=285382000000
POST_STAGE_MIN_REMAINING_NS=275382000000
POST_CONTAIN_MIN_REMAINING_NS=274882000000

These include all 15 slots, the separate 1000000000 ns removal/report cap,
and the later 1410000000 ns terminal cap. Every pre-entry and post-return
boundary resamples both clocks. A typed deadline fault remains typed even if
a later generic exception occurs. No helper, syscall retry, cleanup,
terminal transfer, or certificate refresh restarts an origin.

## 11. Durable records and coherent final tuples

B's durable_once state is monotone:

ABSENT_KNOWN -> OPEN_EFFECT_UNKNOWN -> FD_HELD -> WRITE_EFFECT_UNKNOWN ->
FILE_FSYNC_EFFECT_UNKNOWN -> SAME_FD_REREAD_VERIFIED ->
DIR_FSYNC_EFFECT_UNKNOWN -> DURABLE_VERIFIED

Each object records its partial state, computed digest when available,
typed causal faults, predecessor, monotone sequence, absolute deadline, and
one-shot name. The chain covers intent, release, validated receipt,
ACK-intent receipt, optional kill ticket, recovery/retained state, terminal
candidate, terminal-seen record, PASS or failure report, reconciliation, and
owner closure. A record effect unknown never becomes absence or retry.

Success and failure reports are a discriminated union. Each exact grammar
requires coherent consumption, stage, attempt, containment, entered,
committed, stopped, direct-reap, population, removed, kill-count, kill-state,
ACK, receipt, disposition, and retry tuples. Success alone requires 15/15,
direct reap COMPLETE, streams EOF without overflow, empty and removed
cgroup, kill count 0/NOT_RESERVED, no fault, retained stage/attempt, live
certificate, positive PASS margin, and retry_allowed=0. Candidate claims are
copied from and cross-checked against those literal fields; they are not
prose inferences.

Failure begins one cleanup origin and one cleanup deadline. Resource
acquisition is inside an immediate owner-stack cleanup before any fallible
check. Stage presence is recovered only through the independently certified
safe base and exact four leaves. The first possible kill consumes the one
ticket/call capability. A durable failure cannot claim cgroup removal,
direct reap, or stage presence unless the corresponding exact observation
exists.

## 12. Removal and common terminal handshake

After all 15 ACK receipts, A opens one 1000000000 ns removal deadline. A and
B bind the chain head, independently observe empty, exchange EMPTY_FINAL,
A removes only the named child cgroup through its held base, B proves named
absence through its held base, and they exchange REMOVED/REMOVE_ACK before
that deadline. This phase cannot spend terminal time.

Only after REMOVE_ACK does A establish one terminal_origin and one
terminal_deadline=origin+1410000000. FINALIZE carries both. The same absolute
deadline covers:

1. B durable terminal candidate;
2. candidate notice and A terminal-seen packet;
3. B durable terminal-seen record;
4. B durable PASS commit;
5. the strict 10000000 ns margin;
6. B terminal ACK delivery;
7. A exact ACK recognition;
8. A no-replay receipt delivery;
9. B durable reconciliation receipt;
10. B OWNER_CLOSED packet and safe owner release.

B's terminal_owner_loop continuously polls A pidfd, control, containment,
root/child cgroup observations, and any remaining stream FDs. It drains
POLLIN before HUP. It exits ownership only after the exact successful
handshake plus safe containment, after actor loss plus a durable outcome and
safe containment, or after a separately frozen external transfer. Generic
finally cleanup may not release owner FDs early.

Immediately before PASS, B performs the terminal prepass check. Once PASS
may be committed, missing ACK, send return loss, A receipt loss, conflicting
ABORT, timeout, or HUP is authoritative PASS/ACK effect unknown. It never
downgrades to failure and never permits replay. The outer reconciler must use
the exact monotonically chained report, reconciliation token, receipt, and
owner-closure records. Uncertainty freezes transfer; it is not a retry.

A emits its one success line only after exact OWNER_CLOSED and direct B
status zero. Exit 80 also requires exact refusal ACK and direct B status zero;
81 is consumed durable failure, 82 is effect unknown/no replay, and 83 is
invariant/input failure. B uses zero only after exact closure; unexpected B
termination is never success.

## 13. Exhaustive future effect boundary

A later authorized run may affect only:

1. attempts/AUTH_ID and the exact V4 durable leaf set;
2. stage/AUTH_ID and exactly keeper.py, launcher.py, marker.py, child.py,
   plus the frozen V15 target/a/b safe-bind effects;
3. cgroup/AUTH_ID membership metadata and at most one two-byte cgroup.kill
   write;
4. anonymous sealed memfds, pipes, pidfds, and SOCK_SEQPACKET traffic.

No source, dependency, cwd, base, record name, or capability can name or
reach a build/evidence/root. No other regular file, temporary, cache, log,
backup, lock, swap, symlink, pathname socket, FIFO, redirected capture, tee,
manifest, workspace, build, evidence, paper, PDF, or release write is
permitted. Authorship performs none of these future effects.

## 14. Inert literal source records

The following records use fresh V4 domains. The embedded validator is one
uniquely delimited contiguous raw subspan of A. Delimiter lines are excluded
from source hashes; each source's final LF is included. Any normalization,
comment removal, formatting, or regeneration is INPUT_AUTH.

P27 RUNNER V4 ACTOR SOURCE BEGIN A4C8E712
import array
import ctypes
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import socket
import stat
import sys
import time

TAG=b"P27E001V15"
PYTHON=b"/root/miniconda3/bin/python3"
PYIMAGE=b"/root/miniconda3/bin/python3.12"
RUNTIME_ROOT=b"/var/lib/p27-e001-host-v15/runtime-root"
ATTEMPT_BASE=b"/var/lib/p27-e001-host-v15/attempts"
STAGE_BASE=b"/tmp/p27-e001-host-v15"
CGROUP_BASE=b"/sys/fs/cgroup/p27-e001-host-v15"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
SUITE=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
SOURCE_NAMES=(b"keeper.py",b"launcher.py",b"marker.py",b"child.py")
SOURCE_META=((87151,1840,b"cfa1d88b312b7f4425778018be39cf7628568c9ddb39c697ff12b8b0f1c8be1a"),(4216,128,b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716"),(4218,128,b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5"),(75094,1479,b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d"),(19746,452,b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf"))
SNAPSHOT_EXPECT=(2303269,23672,b"0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92")
SNAPSHOT_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V2_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V3_AUTHOR_OPEN_NO_EXECUTION"
SNAPSHOT_TERMINAL_HEX=SNAPSHOT_TERMINAL.hex().encode("ascii")
WHOLE_V15=(2431,5916064615,0o100644,1,0,0,228310,4622,b"a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845")
V15_TERMINAL=b"BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15_AUTHOR_STOP"
V8_SHA=b"72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf"
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
EMPTY_SHA=b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
OP_NS=15000000000
LAUNCH_NS=1000000000
POST_NS=1664800000
ACK_NS=500000000
HOST_NS=17664800000
TOTAL_NS=18164800000
CLEANUP_NS=2000000000
SIGCONT_NS=5000000
PRECONSUME_NS=10000000000
CONSUMPTION_NS=100000000
ATTEMPT_DIRFD_NS=100000000
STAGE_NS=10000000000
REPORT_NS=1000000000
RECORD_NS=100000000
PASS_COMMIT_NS=100000000
PASS_MARGIN_NS=10000000
TERMINAL_NS=500000000
A_RECEIPT_NS=100000000
B_CLOSURE_NS=500000000
FINAL_TOTAL_NS=1410000000
ACTOR_DISABLE_NS=500000000
CERT_LIFE_NS=360000000000
ENTRY_REMAIN_NS=295482000000
CONSUME_REMAIN_NS=285482000000
PRE_STAGE_REMAIN_NS=285382000000
POST_STAGE_REMAIN_NS=275382000000
POST_CONTAIN_REMAIN_NS=274882000000
STREAM_CAP=3145728
MAX_FILE=16777216
MAX_U63=(1<<63)-1
UINT_MAX=(1<<32)-1
MAX_RIGHTS=4
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
O_DIR=os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW
LIBC=ctypes.CDLL(None,use_errno=True)
LIBC.syscall.restype=ctypes.c_long
SYS_CLONE3=435
CLONE_PIDFD=0x00001000
CLONE_INTO_CGROUP=0x200000000
CGROUP2_MAGIC=0x63677270
PREFLIGHT=True
STAGE_PRESENT=False
CONTROL_SEND_SEQ=0
CONTROL_RECV_SEQ=0

FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"CONSUME_EDGE_UNKNOWN",b"ATTEMPT_COLLISION",b"ATTEMPT_NAMESPACE_UNKNOWN",b"ATTEMPT_DIRFD_UNKNOWN",b"ATTEMPT_BASE_DURABILITY_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"CONTROL_MALFORMED",b"CONTROL_TIMEOUT",b"CONTROL_TRUNCATION",b"FD_TRANSFER",b"STOP_WAIT_UNKNOWN",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_TICKET_DURABILITY_UNKNOWN",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_IO",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"DIRECT_WAIT_UNKNOWN",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_STRUCTURE",b"TRANSCRIPT_SEMANTICS",b"VALIDATED_DURABILITY_UNKNOWN",b"ACK_DURABILITY_UNKNOWN",b"CONTAINMENT_OBSERVATION_UNKNOWN",b"CONTAINMENT_NOT_EMPTY",b"RECOVERY_DURABILITY_UNKNOWN",b"RETAINED_DURABILITY_UNKNOWN",b"REPORT_CANDIDATE_DURABILITY_UNKNOWN",b"TERMINAL_SEEN_DURABILITY_UNKNOWN",b"REPORT_DURABILITY_UNKNOWN",b"ACK_EFFECT_UNKNOWN",b"RECONCILIATION_UNKNOWN",b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED",b"INTERNAL_INVARIANT")

class Refuse(Exception):
 pass

class ConsumedFail(Exception):
 pass

class ConsumedIndeterminate(Exception):
 pass

class CertificateExpired(ConsumedIndeterminate):
 pass

class FaultSet(ConsumedIndeterminate):
 def __init__(self,faults):
  self.faults=set(faults)
  super().__init__("fault-set")

class RemoteAbort(FaultSet):
 pass

def need(value,kind=None):
 if not value:
  selected=(Refuse if PREFLIGHT else ConsumedFail) if kind is None else kind
  raise selected("closed")

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw)
 return value

def sdec(raw,low=-MAX_U63,high=MAX_U63):
 need(type(raw)is bytes and raw)
 if raw.startswith(b"-"):need(len(raw)>1 and raw[1:].isdigit() and raw[1]!=48)
 else:need(raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw)
 return value

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(x in b"0123456789abcdef" for x in raw))
 return raw

def even_hex(raw,cap=MAX_FILE):
 need(type(raw)is bytes and len(raw)%2==0 and len(raw)<=2*cap)
 need(all(x in b"0123456789abcdef" for x in raw))
 result=bytes.fromhex(raw.decode("ascii"))
 need(result.hex().encode()==raw)
 return result

def octal(raw):
 need(raw and all(x in b"01234567" for x in raw))
 value=int(raw,8);need(format(value,"o").encode()==raw)
 return value

def ascii_file(raw,cap=MAX_FILE):
 need(type(raw)is bytes and 0<len(raw)<=cap and raw.endswith(b"\n"))
 need(all(x==10 or 32<=x<=126 for x in raw))
 return raw

def sha(raw):
 return hashlib.sha256(raw).hexdigest().encode("ascii")

def read_all(number,cap=MAX_FILE):
 os.lseek(number,0,os.SEEK_SET);parts=[];total=0
 while True:
  chunk=os.read(number,min(1048576,cap-total+1))
  if not chunk:break
  total+=len(chunk);need(total<=cap);parts.append(chunk)
 return b"".join(parts)

def write_all(number,raw,kind=ConsumedIndeterminate):
 offset=0
 while offset<len(raw):
  try:count=os.write(number,raw[offset:])
  except InterruptedError:continue
  need(count>0,kind);offset+=count

def fd_tuple(number,body):
 held=os.fstat(number)
 return (held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,body.count(b"\n"),sha(body))

def exact_whole(number,expected,terminal):
 raw=read_all(number,expected[6]);need(fd_tuple(number,raw)==expected,Refuse)
 lines=raw[:-1].split(b"\n");need(lines and lines[-1]==terminal and lines.count(terminal)==1,Refuse)
 return raw

def exact_snapshot(number):
 seals(number);fd_access(number,os.O_RDWR)
 raw=read_all(number,SNAPSHOT_EXPECT[0]);held=os.fstat(number)
 need(stat.S_ISREG(held.st_mode) and held.st_nlink==0 and held.st_uid==held.st_gid==0,Refuse)
 need((held.st_size,raw.count(b"\n"),sha(raw))==SNAPSHOT_EXPECT and raw.endswith(b"\n"),Refuse)
 lines=raw[:-1].split(b"\n")
 need(lines and lines[-1]==SNAPSHOT_TERMINAL and lines.count(SNAPSHOT_TERMINAL)==1,Refuse)
 return raw

def seals(number):
 need(fcntl.fcntl(number,fcntl.F_GET_SEALS)==EXACT_SEALS,Refuse)

def extract_one(raw,begin,end):
 lead=begin+b"\n";tail=end+b"\n"
 need(raw.count(lead)==1 and raw.count(tail)==1)
 start=raw.index(lead)+len(lead);stop=raw.index(tail,start)
 return raw[start:stop]

def meta(raw):
 return (len(raw),raw.count(b"\n"),sha(raw))

def open_dir(path):
 need(type(path)is bytes and path.startswith(b"/") and b"\x00" not in path)
 current=following=-1
 try:
  current=os.open(b"/",O_DIR)
  for part in path.split(b"/")[1:]:
   need(part not in (b"",b".",b".."))
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  held=os.fstat(current)
  need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and held.st_mode&0o022==0)
  result=current;current=-1;return result
 finally:close_numbers(tuple(x for x in (following,current) if x>=0))

def open_under(rootfd,path):
 need(path.startswith(b"/") and b"\x00" not in path)
 parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts))
 current=following=-1
 try:
  current=os.dup(rootfd)
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  return os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
 finally:close_numbers(tuple(x for x in (following,current) if x>=0))

def mount_id(number):
 info=-1
 try:
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=read_all(info,4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")]
 need(len(values)==1);return udec(values[0],1)

def mount_line(number):
 wanted=mount_id(number);info=-1
 try:
  info=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,1048576),1048576)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 matches=[]
 for line in raw.splitlines():
  parts=line.split(b" ")
  if parts and parts[0]==str(wanted).encode():matches.append(line+b"\n")
 need(len(matches)==1);return wanted,matches[0]

class StatFS(ctypes.Structure):
 _fields_=(("f_type",ctypes.c_long),("f_bsize",ctypes.c_long),("rest",ctypes.c_byte*240))

def statfs_magic(number):
 cell=StatFS();need(LIBC.fstatfs(number,ctypes.byref(cell))==0)
 return cell.f_type&0xffffffff

def absent(directory,name,kind=ConsumedFail):
 try:os.stat(name,dir_fd=directory,follow_symlinks=False)
 except FileNotFoundError:return
 raise kind("present")

def durable_leaf(directory,name,raw,deadline,kind=ConsumedIndeterminate):
 number=-1
 try:
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)
  number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=directory)
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind);write_all(number,raw,kind);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)
  os.fsync(number);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind);held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw),kind)
  need(read_all(number,len(raw))==raw,kind);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 os.fsync(directory);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)

def stage_leaf(directory,name,raw,identity,deadline):
 number=-1
 try:
  durable_leaf(directory,name,raw,deadline)
  number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory)
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS));held=os.fstat(number);again=read_all(number,identity[0])
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_nlink==1 and held.st_uid==held.st_gid==0)
  need(meta(again)==identity);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS))
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def memfd(raw,label):
 number=-1
 try:
  number=os.memfd_create(label,os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)
  write_all(number,raw);os.lseek(number,0,os.SEEK_SET)
  fcntl.fcntl(number,fcntl.F_ADD_SEALS,EXACT_SEALS);seals(number)
  need(read_all(number,len(raw))==raw);os.lseek(number,0,os.SEEK_SET)
  result=number;number=-1;return result
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def close_range(first,last):
 need(0<=first<=last<=UINT_MAX)
 need(LIBC.close_range(ctypes.c_uint(first),ctypes.c_uint(last),ctypes.c_uint(0))==0)

def parse_fixed(raw,header,keys,end):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(len(lines)==len(keys)+2 and lines[0]==header and lines[-1]==end)
 result={}
 for key,line in zip(keys,lines[1:-1]):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result)
  result[key]=parts[1]
 return result

ENVELOPE_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX")

CERT_KEYS=(b"ISSUER_ID",b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"HISTORICAL_SNAPSHOT_SEALED",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"CGROUP_CHILD_MODE",b"CGROUP_CHILD_UID",b"CGROUP_CHILD_GID",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"ATTEMPT_DIRFD_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"FINAL_PASS_COMMIT_PROGRESS_NS",b"FINAL_PASS_MARGIN_NS",b"TERMINAL_HANDSHAKE_PROGRESS_NS",b"A_RECEIPT_PROGRESS_NS",b"B_CLOSURE_PROGRESS_NS",b"FINAL_TERMINAL_TOTAL_NS",b"ENTRY_MIN_REMAINING_NS",b"CONSUMPTION_MIN_REMAINING_NS",b"PRE_STAGE_MIN_REMAINING_NS",b"POST_STAGE_MIN_REMAINING_NS",b"POST_CONTAIN_MIN_REMAINING_NS",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DELETED_CGROUP_FD_GATE_ID",b"DELETED_CGROUP_FD_GATE_PASS",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS",b"EXTERNAL_SURVIVAL_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_PASS",b"OUTER_RECONCILER_GATE_ID",b"OUTER_RECONCILER_GATE_PASS",b"DEP_COUNT")

def parse_envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V4",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V4",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":WHOLE_V15[8],b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"EXTERNALLY_VERIFIED_ED25519"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig),Refuse)
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"])
 need(before<after,Refuse)
 return values

def parse_cert(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V4" and lines[-1]==b"CERTIFICATE_END=1",Refuse)
 fixed=lines[1:1+len(CERT_KEYS)];need(len(fixed)==len(CERT_KEYS),Refuse);values={}
 for key,line in zip(CERT_KEYS,fixed):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in values,Refuse);values[key]=parts[1]
 count=udec(values[b"DEP_COUNT"],1,256);dep_lines=lines[1+len(CERT_KEYS):-1];need(len(dep_lines)==count,Refuse)
 roles={b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC",b"PYTHON_STDLIB",b"PYTHON_EXTENSION",b"NSS_DEPENDENCY",b"RUNTIME_DEPENDENCY"}
 deps=[]
 for index,line in enumerate(dep_lines):
  prefix=b"DEP[%04d]="%index;need(line.startswith(prefix),Refuse);fields=line[len(prefix):].split(b",")
  need(len(fields)==10 and fields[0] in roles,Refuse);path=even_hex(fields[1]);need(path.startswith(b"/") and b"\x00" not in path,Refuse)
  ident=(udec(fields[2],1),udec(fields[3],1),octal(fields[4]),udec(fields[5],1),udec(fields[6]),udec(fields[7]),udec(fields[8]),h64(fields[9]))
  deps.append((fields[0],path,ident))
 need(len(set((x[0],x[1]) for x in deps))==len(deps),Refuse)
 for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC"):need(sum(x[0]==role for x in deps)==1,Refuse)
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V4",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":WHOLE_V15[8],b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"KEEPER_BYTES":b"4216",b"KEEPER_LF":b"128",b"KEEPER_SHA256":b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716",b"LAUNCHER_BYTES":b"4218",b"LAUNCHER_LF":b"128",b"LAUNCHER_SHA256":b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5",b"MARKER_BYTES":b"75094",b"MARKER_LF":b"1479",b"MARKER_SHA256":b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d",b"CHILD_BYTES":b"19746",b"CHILD_LF":b"452",b"CHILD_SHA256":b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"100000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"A_RECEIPT_PROGRESS_NS":b"100000000",b"B_CLOSURE_PROGRESS_NS":b"500000000",b"FINAL_TERMINAL_TOTAL_NS":b"1410000000",b"ENTRY_MIN_REMAINING_NS":b"295482000000",b"CONSUMPTION_MIN_REMAINING_NS":b"285482000000",b"PRE_STAGE_MIN_REMAINING_NS":b"285382000000",b"POST_STAGE_MIN_REMAINING_NS":b"275382000000",b"POST_CONTAIN_MIN_REMAINING_NS":b"274882000000",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS":b"500000000",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS":b"1",b"EXTERNAL_SURVIVAL_GATE_PASS":b"1",b"OUTER_RECONCILER_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_MOUNTINFO_SHA256",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"SAFE_BIND_MOUNTINFO_SHA256",b"KEEPER_SHA256",b"LAUNCHER_SHA256",b"MARKER_SHA256",b"CHILD_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"CLONE3_CPYTHON_GATE_ID",b"DELETED_CGROUP_FD_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_ID",b"OUTER_RECONCILER_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64 and values[b"DELETED_CGROUP_FD_GATE_ID"]!=b"0"*64 and values[b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID"]!=b"0"*64 and values[b"EXTERNAL_SURVIVAL_GATE_ID"]!=b"0"*64 and values[b"OUTER_RECONCILER_GATE_ID"]!=b"0"*64,Refuse)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1",Refuse)
 for key in (b"KERNEL_RELEASE_HEX",b"E0366_SNAPSHOT_TERMINAL_HEX",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"CGROUP_CHILD_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"LIBC_MODE"):octal(values[key])
 for key in (b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_MOUNT_ID",b"CGROUP2_MOUNT_ID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_NLINK",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_MOUNT_ID",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_NLINK",b"SAFE_BIND_MOUNT_ID",b"KEEPER_BYTES",b"KEEPER_LF",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"MARKER_BYTES",b"MARKER_LF",b"CHILD_BYTES",b"CHILD_LF",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT"):udec(values[key])
 by_role={role:next(x for x in deps if x[0]==role) for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC")}
 need(by_role[b"PYTHON_LINK"][1]==PYTHON and by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"ENV_EXEC"][1]==b"/usr/bin/env" and by_role[b"BASH_EXEC"][1]==b"/usr/bin/bash",Refuse)
 libc=(udec(values[b"LIBC_DEV"],1),udec(values[b"LIBC_INO"],1),octal(values[b"LIBC_MODE"]),udec(values[b"LIBC_NLINK"],1),0,0,udec(values[b"LIBC_BYTES"],1),values[b"LIBC_SHA256"])
 need(by_role[b"LIBC"][1]==even_hex(values[b"LIBC_PATH_HEX"]) and by_role[b"LIBC"][2]==libc,Refuse)
 return values,tuple(deps)

def checkpoint(cert,needed,kind=ConsumedIndeterminate,deadline=None):
 m0=time.monotonic_ns();real=time.time_ns();m1=time.monotonic_ns()
 before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 if not (before<=real<expiry and expiry-real>=needed):
  if kind is Refuse:raise Refuse("certificate-life")
  raise CertificateExpired("certificate-life")
 base_r=udec(cert[b"REALTIME_BIND_NS"]);base_m=udec(cert[b"MONOTONIC_BIND_NS"])
 need(base_m<=m0<=m1,kind);drift=udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"])
 low=base_r+(m0-base_m);high=base_r+(m1-base_m)
 need(low-drift<=real<=high+drift,kind)
 if deadline is not None:need(m1<=deadline,kind)
 return real,m1

def cert_live(cert,needed,kind=ConsumedIndeterminate):
 return checkpoint(cert,needed,kind)

def verify_platform(cert):
 boot=-1
 try:
  boot=os.open(b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);boot_raw=read_all(boot,128)
 finally:close_numbers(tuple(x for x in (boot,) if x>=0))
 need(boot_raw.endswith(b"\n") and sha(boot_raw)==cert[b"BOOT_ID_SHA256"],Refuse)
 u=os.uname();parts=(u.sysname,u.release,u.version,u.machine)
 encoded=tuple(x.encode("ascii","strict") for x in parts)
 raw=b"SYSNAME="+encoded[0]+b"\nRELEASE="+encoded[1]+b"\nVERSION="+encoded[2]+b"\nMACHINE="+encoded[3]+b"\n"
 need(encoded[3]==b"x86_64" and encoded[1].hex().encode()==cert[b"KERNEL_RELEASE_HEX"] and sha(raw)==cert[b"PLATFORM_ID_SHA256"],Refuse)

def verify_dependency(rootfd,entry):
 role,path,identity=entry;parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts),Refuse)
 current=number=following=-1
 try:
  current=os.dup(rootfd)
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode),Refuse)
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
   held=os.fstat(number);body=read_all(number,identity[6]);size=len(body);digest=sha(body)
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,size,digest)==identity,Refuse)
 finally:close_numbers(tuple(x for x in (number,following,current) if x>=0))

def verify_mount(number,cert,prefix,want_magic=None):
 held=os.fstat(number);mode=octal(cert[prefix+b"_MODE"])
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),mode,udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"])),Refuse)
 mid,line=mount_line(number);need(mid==udec(cert[prefix+b"_MOUNT_ID"],1) and sha(line)==cert[prefix+b"_MOUNTINFO_SHA256"],Refuse)
 if want_magic is not None:need(statfs_magic(number)==want_magic,Refuse)
 return line

def v15_sources(raw):
 result=[]
 for label,expected in zip((b"OUTER",b"KEEPER",b"LAUNCHER",b"MARKER",b"CHILD"),SOURCE_META):
  begin=(b"UNIFIED "+label+b" V15 SOURCE BEGIN") if label!=b"CHILD" else b"NESTED CHILD V15 SOURCE BEGIN"
  end=(b"UNIFIED "+label+b" V15 SOURCE END") if label!=b"CHILD" else b"NESTED CHILD V15 SOURCE END"
  span=extract_one(raw,begin,end);need(meta(span)==expected,Refuse);result.append(span)
 need(extract_one(result[3],b"CHILD_SOURCE=b'''\\",b"'''")==result[4],Refuse)
 return tuple(result)

def clock_binding(cert,kind=ConsumedIndeterminate):
 checkpoint(cert,0,kind)

def progress(cert,deadline,needed=0,kind=ConsumedIndeterminate):
 need(time.monotonic_ns()<=deadline,kind)
 return checkpoint(cert,needed,kind,deadline)


def horizon_needed(deadline,tail):
 return tail+max(0,deadline-time.monotonic_ns())

def certificate_mono_expiry(cert):
 return udec(cert[b"MONOTONIC_BIND_NS"],1)+udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])-udec(cert[b"REALTIME_BIND_NS"])-udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"])

def cap_status():
 number=-1
 try:
  number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,65536),65536)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 keys=(b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs")
 values={}
 for line in raw.splitlines():
  for key in keys:
   prefix=key+b":"
   if line.startswith(prefix):
    need(key not in values);values[key]=line[len(prefix):].strip()
 need(set(values)==set(keys))
 return values

def securebits():
 result=LIBC.prctl(27,0,0,0,0);need(result>=0)
 return result

def verify_creds(final):
 values=cap_status();zero=b"0000000000000000"
 need(os.getresuid()==(0,0,0) and os.getresgid()==(0,0,0) and os.getgroups()==[])
 if final:
  need(all(values[x]==zero for x in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb")))
  need(values[b"NoNewPrivs"]==b"1" and securebits()==15)
 else:
  need(values[b"CapInh"]==zero and values[b"CapAmb"]==zero)
  need(all(values[x]==b"00000000000401c0" for x in (b"CapPrm",b"CapEff",b"CapBnd")))
  need(values[b"NoNewPrivs"]==b"0" and securebits()==12,Refuse)

def normalize_limits():
 inf=resource.RLIM_INFINITY
 fixed=((resource.RLIMIT_AS,(inf,inf)),(resource.RLIMIT_CORE,(0,0)),(resource.RLIMIT_CPU,(inf,inf)),(resource.RLIMIT_DATA,(inf,inf)),(resource.RLIMIT_FSIZE,(inf,inf)),(resource.RLIMIT_MEMLOCK,(8388608,8388608)),(resource.RLIMIT_MSGQUEUE,(819200,819200)),(resource.RLIMIT_NICE,(0,0)),(resource.RLIMIT_NOFILE,(1048576,1048576)),(resource.RLIMIT_NPROC,(1048576,1048576)),(resource.RLIMIT_RSS,(inf,inf)),(resource.RLIMIT_RTPRIO,(0,0)),(resource.RLIMIT_RTTIME,(inf,inf)),(resource.RLIMIT_SIGPENDING,(515199,515199)),(resource.RLIMIT_STACK,(8388608,inf)))
 for key,value in fixed:resource.setrlimit(key,value)
 for key,value in fixed:need(resource.getrlimit(key)==value)

def normalize_signals():
 for which in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF):signal.setitimer(which,0.0,0.0)
 valid=signal.valid_signals();catchable=tuple(sorted(int(x) for x in valid if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))
 signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in catchable:signal.signal(number,signal.SIG_DFL)
 need(signal.sigpending()==set())

class CapHeader(ctypes.Structure):
 _fields_=(("version",ctypes.c_uint32),("pid",ctypes.c_int))

class CapData(ctypes.Structure):
 _fields_=(("effective",ctypes.c_uint32),("permitted",ctypes.c_uint32),("inheritable",ctypes.c_uint32))

class CloneArgs(ctypes.Structure):
 _fields_=(("flags",ctypes.c_uint64),("pidfd",ctypes.c_uint64),("child_tid",ctypes.c_uint64),("parent_tid",ctypes.c_uint64),("exit_signal",ctypes.c_uint64),("stack",ctypes.c_uint64),("stack_size",ctypes.c_uint64),("tls",ctypes.c_uint64),("set_tid",ctypes.c_uint64),("set_tid_size",ctypes.c_uint64),("cgroup",ctypes.c_uint64))

def final_drop():
 need(LIBC.prctl(28,15,0,0,0)==0)
 for bit in range(64):
  result=LIBC.prctl(24,bit,0,0,0)
  if result!=0:need(ctypes.get_errno()==errno.EINVAL)
 header=CapHeader(0x20080522,0);data=(CapData*2)()
 need(LIBC.capset(ctypes.byref(header),ctypes.byref(data))==0)
 need(LIBC.prctl(47,4,0,0,0)==0 and LIBC.prctl(38,1,0,0,0)==0)

def child_context(cwd_name,safe_dev,safe_ino):
 root=-1;os.chroot(RUNTIME_ROOT)
 try:
  root=os.open(b"/",O_DIR)
  tmp=os.open(b"tmp",O_DIR,dir_fd=root);base=os.open(b"p27-e001-host-v15",O_DIR,dir_fd=tmp)
  cwd=os.dup(base) if cwd_name is None else os.open(cwd_name,O_DIR,dir_fd=base)
  held=os.fstat(cwd);need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
  os.fchdir(cwd)
 finally:
  for number in (locals().get("cwd",-1),locals().get("base",-1),locals().get("tmp",-1),root):
   if number>=0:
    try:os.close(number)
    except OSError:pass
 os.setgroups([]);os.setresgid(0,0,0);os.setresuid(0,0,0);os.umask(0o077)
 normalize_limits();normalize_signals();final_drop();verify_creds(True)

def fd_access(number,mode):
 need(fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE==mode)

def scrub_exact(expected):
 seen=set()
 for item in os.listdir(b"/proc/self/fd"):
  if item.isdigit():
   number=int(item)
   try:os.fstat(number)
   except OSError as error:
    need(error.errno==errno.EBADF);continue
   seen.add(number)
 need(seen==expected)

def preserved_map(mapping):
 parked=[];number=-1;targets={target for source,target in mapping}
 try:
  for source,target in mapping:
   number=fcntl.fcntl(source,fcntl.F_DUPFD_CLOEXEC,200)
   need(number>=200 and number not in targets and number not in [x[0] for x in parked])
   parked.append((number,target));number=-1
  for held,target in parked:os.dup2(held,target,inheritable=True)
 finally:
  close_numbers(tuple(x for x in (number,) if x>=0))
  for held,target in parked:
   try:os.close(held)
   except OSError:pass

# P27 RUNNER V4 EMBEDDED VALIDATOR BEGIN B7D3F209
COMMON=(b"marker_image_dev",b"marker_image_ino",b"marker_image_sha256",b"probe_start_ns",b"probe_finish_ns",b"probe_elapsed_ns",b"probe_bound_ns",b"primary_failure",b"cleanup_failure",b"result")
PREFIX={b"P00":(b"source_item_bytes",b"source_item_accounted_bytes",b"broker_spawned",b"broker_payload_hex"),b"P01D":(b"python_image_dev",b"python_image_ino",b"python_image_bytes",b"python_image_sha256",b"libc_confstr_hex",b"libc_path_hex",b"libc_bytes",b"libc_sha256",b"backend_surface",b"spawn_premise_satisfied"),b"P01C":(b"libc_path_hex",b"libc_sha256",b"libc_confstr_hex",b"child_pids",b"child_statuses",b"child_raw_hex",b"spawn_premise_satisfied"),b"P02":(b"fds",b"environment_count",b"cwd_hex",b"flags"),b"P03":(b"soft_before",b"hard_before",b"soft_test",b"opened_fds",b"emfile"),b"P04":(b"valid_signal_count",b"default_signal_count",b"defaults_sha256",b"mask_empty"),b"P05":(b"wnohang_zero",b"eintr",b"echild",b"child_pids",b"raw_statuses",b"term_signal",b"broker_payload_hex"),b"P06":(b"monotonic",b"observed_min_delta_ns",b"start_ns",b"end_ns",b"deadline_checked"),b"P07":(b"empty_eagain",b"eof_before_last_writer",b"eof_after_last_writer"),b"P08":(b"child_pids",b"raw_statuses",b"same_session_group",b"post_pid_esrch",b"broker_payload_hex"),b"P09":(b"child_pids",b"raw_statuses",b"signal",b"reap_start_ns",b"reap_end_ns",b"reaped"),b"P10":(b"sample_count",b"pids",b"statuses",b"pid_duplicates",b"group_is_single_owned_launcher_group",b"reuse_proof"),b"P11":(b"open_result",b"atime_unchanged",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"scope_single_inode"),b"P12":(b"child_pids",b"raw_statuses",b"environment_count",b"underscore_absent",b"real_payload_invoked",b"broker_payload_hex"),b"P13":(b"file_fsync_returned",b"hardlink_noreplace_returned",b"inode_preserved",b"dir_fsync_returned",b"post_unlink_absent",b"cleanup_unlinked",b"durability_proof",b"rename_atomicity_proof")}

def csv_values(raw,signed=False,count=None):
 parts=raw.split(b",");need(parts and (count is None or len(parts)==count))
 return tuple(sdec(x) if signed else udec(x,1) for x in parts)

def child_observation(raw,mode,pid,source_sha,cwd_hex,phase):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|");need(len(fields)==11 and fields[0]==TAG and fields[1]==b"child=observation")
 need(fields[2]==b"mode="+mode and fields[3]==b"pid="+str(pid).encode())
 need(fields[4].startswith(b"sid=") and udec(fields[4][4:],1)>0)
 need(fields[5].startswith(b"pgid=") and udec(fields[5][5:],1)>0)
 need(tuple(fields[6:])==(b"image_sha="+PY_SHA,b"source_sha="+source_sha,b"cwd_hex="+cwd_hex,b"phase="+phase,b"result=PASS"))

def payload_item(raw,prefix):
 lead=prefix+b":";need(raw.startswith(lead));return even_hex(raw[len(lead):])

def parse_outer(line,probe,terminal):
 fields=line.split(b"|")
 if terminal:need(len(fields)==8 and fields[0]==TAG and fields[1]==b"outer=terminal" and fields[2]==b"probe="+probe and fields[3]==b"all_reaped=1" and fields[5]==b"frame_complete=1" and fields[6]==b"fatal=0" and fields[7]==b"result=PASS")
 else:need(len(fields)==8 and fields[0]==TAG and fields[1]==b"outer=candidate" and fields[2]==b"probe="+probe and fields[3]==b"slots=4" and fields[4]==b"all_reaped=1" and fields[6]==b"fatal=0" and fields[7]==b"result=PASS")
 role_field=fields[4] if terminal else fields[5];need(role_field.startswith(b"role_statuses="))
 roles=role_field[14:].split(b",");need(len(roles)==4);result={}
 for expected,item in zip((b"launcher",b"keeper",b"marker",b"child"),roles):
  pieces=item.split(b":",1);need(len(pieces)==2 and pieces[0]==expected);result[expected]=sdec(pieces[1])
 return result

def validate_probe(rows,probe,ctx):
 if probe==b"P00":
  need(rows[b"source_item_bytes"]==b"251414" and rows[b"source_item_accounted_bytes"]==b"251415")
  child=ctx[b"child_source"];need((len(child),child.count(b"\n"),sha(child))==SOURCE_META[4])
  padding=251414-len(child)-2;need(padding>=0)
  synthetic=child+b"\n#"+b"x"*padding
  need(len(synthetic)==251414 and synthetic[:len(child)]==child and synthetic[len(child):len(child)+2]==b"\n#");synthetic_sha=sha(synthetic)
  spawned=udec(rows[b"broker_spawned"],0,1);items=even_hex(rows[b"broker_payload_hex"]).split(b";")
  if spawned==0:
   need(len(items)==1 and items[0]==b"source_bytes=251414,returned=0,e2big=1,sha="+synthetic_sha)
  else:
   need(len(items)==2 and items[1]==b"source_bytes=251414,returned=1,e2big=0,sha="+synthetic_sha)
   observation=payload_item(items[0],b"INFO");fields=observation.split(b"|");need(len(fields)==11 and fields[3].startswith(b"pid="))
   child_observation(observation,b"INFO",udec(fields[3][4:],1),synthetic_sha,ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P01D":
  need(udec(rows[b"python_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"python_image_ino"],1)==ctx[b"python_ino"])
  need(rows[b"python_image_bytes"]==b"30626264" and rows[b"python_image_sha256"]==PY_SHA)
  need(rows[b"libc_path_hex"]==ctx[b"libc_path_hex"] and rows[b"libc_confstr_hex"]==ctx[b"libc_confstr_hex"])
  need(udec(rows[b"libc_bytes"],1)==ctx[b"libc_bytes"] and rows[b"libc_sha256"]==ctx[b"libc_sha"])
  need(rows[b"backend_surface"]==b"posix-posix_spawn" and rows[b"spawn_premise_satisfied"]==b"0")
 elif probe==b"P01C":
  prior=ctx[b"p01d"];need(rows[b"libc_path_hex"]==prior[b"libc_path_hex"] and rows[b"libc_sha256"]==prior[b"libc_sha256"] and rows[b"libc_confstr_hex"]==prior[b"libc_confstr_hex"] and rows[b"spawn_premise_satisfied"]==b"1")
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"child_statuses"],True,1)==(0,))
  child_observation(payload_item(even_hex(rows[b"child_raw_hex"]),b"INFO"),b"INFO",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P02":need(tuple(rows[x] for x in PREFIX[probe])==(b"0,1,2,5,6",b"10",ctx[b"cwd_hex"],b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1"))
 elif probe==b"P03":need(tuple(rows[x] for x in PREFIX[probe])==(b"4096",b"1048576",b"64",b"59",b"1"))
 elif probe==b"P04":need(udec(rows[b"valid_signal_count"])==ctx[b"valid_signals"] and udec(rows[b"default_signal_count"])==ctx[b"default_signals"] and rows[b"defaults_sha256"]==ctx[b"defaults_sha"] and rows[b"mask_empty"]==b"1")
 elif probe==b"P05":
  need(rows[b"wnohang_zero"]==rows[b"eintr"]==rows[b"echild"]==b"1" and rows[b"term_signal"]==b"15")
  pids=csv_values(rows[b"child_pids"],False,2);statuses=csv_values(rows[b"raw_statuses"],True,2);need(statuses==(23<<8,15))
  parts=payload_item(even_hex(rows[b"broker_payload_hex"]),b"P05").splitlines(True);need(len(parts)==2)
  child_observation(parts[0],b"EXIT23",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
  child_observation(parts[1],b"TERM",pids[1],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
 elif probe==b"P06":need(rows[b"monotonic"]==b"1" and udec(rows[b"observed_min_delta_ns"],1)>0 and udec(rows[b"start_ns"])<=udec(rows[b"end_ns"]) and rows[b"deadline_checked"]==b"1")
 elif probe==b"P07":need(tuple(rows[x] for x in PREFIX[probe])==(b"1",b"0",b"1"))
 elif probe==b"P08":
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(0,) and rows[b"same_session_group"]==rows[b"post_pid_esrch"]==b"1")
  child_observation(payload_item(even_hex(rows[b"broker_payload_hex"]),b"P08"),b"BLOCK0",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
 elif probe==b"P09":
  csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(9,) and rows[b"signal"]==b"9" and rows[b"reaped"]==b"1")
  start=udec(rows[b"reap_start_ns"]);finish=udec(rows[b"reap_end_ns"]);need(start<=finish and finish-start<=100000000)
 elif probe==b"P10":
  pids=csv_values(rows[b"pids"],False,16);need(rows[b"sample_count"]==b"16" and csv_values(rows[b"statuses"],True,16)==(0,)*16)
  need(udec(rows[b"pid_duplicates"])==16-len(set(pids)) and rows[b"group_is_single_owned_launcher_group"]==b"1" and rows[b"reuse_proof"]==b"0")
 elif probe==b"P11":need(tuple(rows[x] for x in PREFIX[probe])==(b"OK",b"1",b"1",b"1",b"0",b"1"))
 elif probe==b"P12":
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(0,) and rows[b"environment_count"]==b"10" and rows[b"underscore_absent"]==b"1" and rows[b"real_payload_invoked"]==b"0")
  child_observation(payload_item(even_hex(rows[b"broker_payload_hex"]),b"CHAIN"),b"CHAIN",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P13":need(tuple(rows[x] for x in PREFIX[probe])==(b"1",b"1",b"1",b"1",b"1",b"1",b"0",b"0"))
 else:need(False)

def transcript_structure(raw,probe):
 ascii_file(raw,STREAM_CAP);lines=raw[:-1].split(b"\n")
 need(lines and all(lines) and lines[0]==TAG+b"|marker=report|schema=15|probe="+probe)
 keys=PREFIX[probe]+COMMON;need(len(lines)==len(keys)+4);rows={}
 for key,line in zip(keys,lines[1:1+len(keys)]):
  prefix=TAG+b"|probe="+probe+b"|"+key+b"=";need(line.startswith(prefix) and key not in rows)
  value=line[len(prefix):];need(value and b"|" not in value and b"=" not in value);rows[key]=value
 need(lines[1+len(keys)]==TAG+b"|probe="+probe+b"|result=PASS")
 candidate=parse_outer(lines[2+len(keys)],probe,False);terminal=parse_outer(lines[3+len(keys)],probe,True)
 need(candidate==terminal);return rows,candidate

def transcript_semantics(rows,candidate,probe,ctx):
 need(candidate[b"launcher"]==15 and candidate[b"keeper"]==15 and candidate[b"marker"]==0)
 start=udec(rows[b"probe_start_ns"]);finish=udec(rows[b"probe_finish_ns"]);elapsed=udec(rows[b"probe_elapsed_ns"])
 need(start<=finish and finish-start==elapsed and elapsed<=OP_NS and rows[b"probe_bound_ns"]==b"15000000000")
 need(rows[b"primary_failure"]==b"none" and rows[b"cleanup_failure"]==b"none" and rows[b"result"]==b"PASS")
 need(udec(rows[b"marker_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"marker_image_ino"],1)==ctx[b"python_ino"] and rows[b"marker_image_sha256"]==PY_SHA)
 validate_probe(rows,probe,ctx);expected=-1
 if probe==b"P00":expected=-1 if rows[b"broker_spawned"]==b"0" else 0
 elif probe in (b"P01C",b"P08",b"P10",b"P12"):expected=0
 elif probe==b"P05":expected=15
 elif probe==b"P09":expected=9
 need(candidate[b"child"]==expected);return rows
# P27 RUNNER V4 EMBEDDED VALIDATOR END B7D3F209

def packet(kind,pairs):
 global CONTROL_SEND_SEQ
 need(kind.startswith(b"V4_") and b"|" not in kind and b"\n" not in kind)
 provided={}
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value and key not in provided)
  provided[key]=value
 state=provided.get(b"state",kind[3:]);ordinal=provided.get(b"ordinal",b"NONE");probe=provided.get(b"probe",b"NONE")
 CONTROL_SEND_SEQ+=1
 body=kind+b"|version=4|auth_id="+AUTH_ID+b"|sequence="+str(CONTROL_SEND_SEQ).encode()+b"|sender="+b"A"+b"|current_state="+state+b"|current_ordinal="+ordinal+b"|current_probe="+probe
 for key,value in pairs:body+=b"|"+key+b"="+value
 return body+b"\n"

def parse_packet(raw,kind,keys):
 global CONTROL_RECV_SEQ
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|");common_keys=(b"version",b"auth_id",b"sequence",b"sender",b"current_state",b"current_ordinal",b"current_probe")
 need(fields[0]==kind and len(fields)==len(keys)+1+len(common_keys))
 common={}
 for key,item in zip(common_keys,fields[1:1+len(common_keys)]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in common);common[key]=parts[1]
 result={}
 for key,item in zip(keys,fields[1+len(common_keys):]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result and parts[1]);result[key]=parts[1]
 need(common[b"version"]==b"4" and common[b"auth_id"]==AUTH_ID and common[b"sender"]==b"B")
 sequence=udec(common[b"sequence"],1);need(sequence==CONTROL_RECV_SEQ+1)
 need(common[b"current_state"]==result.get(b"state",kind[3:]))
 need(common[b"current_ordinal"]==result.get(b"ordinal",b"NONE"))
 need(common[b"current_probe"]==result.get(b"probe",b"NONE"))
 CONTROL_RECV_SEQ=sequence
 return result

def fault_csv(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults)
 need(len(ordered)==len(faults))
 return b"NONE" if not ordered else b",".join(ordered)

def parse_fault_csv(raw,allow_none):
 if raw==b"NONE":
  need(allow_none);return set()
 parts=raw.split(b",");need(parts and all(x in FAULT_ORDER for x in parts))
 need(len(parts)==len(set(parts)) and tuple(x for x in FAULT_ORDER if x in set(parts))==tuple(parts))
 return set(parts)

def parse_abort(raw,want_sender):
 keys=(b"sender",b"state",b"ordinal",b"probe",b"effect_state",b"stage_present",b"release_disabled",b"terminal_deadline_ns",b"fault_set")
 values=parse_packet(raw,b"V4_ABORT",keys)
 need(values[b"sender"]==want_sender and values[b"state"] and values[b"ordinal"] and values[b"probe"])
 effects=(b"PREBEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"ARM_SEND_EFFECT_UNKNOWN",b"COMMIT_SEND_EFFECT_UNKNOWN",b"CONSUMED",b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED")
 need(values[b"effect_state"] in effects and values[b"stage_present"] in (b"0",b"1") and values[b"release_disabled"] in (b"0",b"1"))
 if want_sender==b"A":need(values[b"release_disabled"]==b"1")
 if want_sender==b"B" and values[b"state"]==b"CLEANUP_RELEASE_DISABLE":need(values[b"release_disabled"]==b"0")
 deadline=udec(values[b"terminal_deadline_ns"])
 if values[b"effect_state"] in (b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED"):need(deadline>0)
 faults=parse_fault_csv(values[b"fault_set"],False);return values,faults

def close_numbers(numbers):
 for number in numbers:
  try:os.close(number)
  except OSError:pass

def wait_sendable(control,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  mask=0
  for number,event in events:
   if number==control.fileno():mask|=event
  if mask&select.POLLOUT:return
  if mask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"ACTOR_LOST"})

def send_plain(control,raw,deadline):
 while True:
  wait_sendable(control,deadline)
  try:count=control.send(raw)
  except BlockingIOError:continue
  except BaseException as error:raise FaultSet({b"CONTROL_MALFORMED"}) from error
  if count!=len(raw):raise FaultSet({b"CONTROL_MALFORMED"})
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);need(time.monotonic_ns()<=deadline,ConsumedIndeterminate);return

def send_rights(control,raw,numbers,deadline):
 cells=array.array("i",numbers)
 while True:
  wait_sendable(control,deadline)
  try:count=control.sendmsg([raw],[(socket.SOL_SOCKET,socket.SCM_RIGHTS,cells.tobytes())])
  except BlockingIOError:continue
  except BaseException as error:raise FaultSet({b"FD_TRANSFER"}) from error
  if count!=len(raw):raise FaultSet({b"FD_TRANSFER"})
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);need(time.monotonic_ns()<=deadline,ConsumedIndeterminate);return

def recv_control(control,deadline,cap=65536):
 checkpoint(CERT,0,ConsumedIndeterminate,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  mask=0
  for number,event in events:
   if number==control.fileno():mask|=event
  if mask&select.POLLIN:
   installed=[];bad=False
   try:
    raw,ancillary,flags,address=control.recvmsg(cap,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize))
    for level,kind,data in ancillary:
     if level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS:
      cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
      if whole:cells.frombytes(data[:whole]);installed.extend(cells)
      if whole!=len(data):bad=True
     else:bad=True
    checkpoint(CERT,0,ConsumedIndeterminate,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if bad or installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    if address is not None or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    if raw.startswith(b"V4_ABORT|"):
     values,faults=parse_abort(raw,b"B");error=RemoteAbort(faults);error.values=values;raise error
    return raw
   except BlockingIOError:
    close_numbers(installed);continue
   except BaseException:
    close_numbers(installed);raise
  if mask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"ACTOR_LOST"})

def wait_exact(control,deadline,expected):
 raw=recv_control(control,deadline)
 if raw!=expected:raise FaultSet({b"CONTROL_MALFORMED"})

def cgroup_populated(number):
 os.lseek(number,0,os.SEEK_SET);raw=os.read(number,4096)
 matches=[line for line in raw.splitlines() if line.startswith(b"populated ")]
 need(len(matches)==1 and matches[0] in (b"populated 0",b"populated 1"),ConsumedIndeterminate)
 return matches[0]==b"populated 1"

def cgroup_empty(cgfd):
 number=-1
 try:
  number=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd);return not cgroup_populated(number)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def exact_child_cgroup(cgfd,pid):
 number=-1
 try:
  number=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd);need(read_all(number,64)==str(pid).encode()+b"\n",ConsumedIndeterminate)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def wait_status(pid,flags,deadline,unknown_fault):
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline)
  if time.monotonic_ns()>deadline:raise FaultSet({unknown_fault})
  try:waited,raw=os.waitpid(pid,flags|os.WNOHANG)
  except InterruptedError:
   checkpoint(CERT,0,ConsumedIndeterminate,deadline);continue
  except BaseException as error:raise FaultSet({unknown_fault}) from error
  checkpoint(CERT,0,ConsumedIndeterminate,deadline)
  if time.monotonic_ns()>deadline:raise FaultSet({unknown_fault})
  if waited not in (0,pid):raise FaultSet({unknown_fault})
  if waited==pid:return raw
  try:select.poll().poll(1)
  except InterruptedError:pass

def source_argv(probe,safe,p01c):
 app=[b"/proc/self/fd/100",probe,AUTH_ID,b"15000000000",b"5000000",b"2000000",b"20000000",b"100000000",b"100000000",b"500000000",b"NO_ASYNC_TRANSFER_THROUGH_FIXED_FD_PROCESS_WAIT_AND_CLOSE_COMMIT_V15",b"OWNER_SURVIVAL_PROGRESS_SINGLE_FRAME_V15",b"ROOT_OWNED_0700_STABLE_NONCE_NO_CONCURRENT_MUTATOR_V15",str(safe.st_dev).encode(),str(safe.st_ino).encode()]
 for identity in SOURCE_META:app.append(str(identity[0]).encode()+b","+str(identity[1]).encode()+b","+identity[2])
 app.extend(p01c);need(len(app)==20 or (probe==b"P01C" and len(app)==33))
 return [PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8"]+app

def derive_p01c(prior,cert):
 need(prior is not None)
 path=even_hex(prior[b"libc_path_hex"]);conf_bytes=even_hex(prior[b"libc_confstr_hex"])
 conf_text=conf_bytes.decode("ascii","strict");need(conf_text.encode("ascii","strict")==conf_bytes and conf_bytes.hex().encode()==prior[b"libc_confstr_hex"])
 need(prior[b"libc_path_hex"]==cert[b"LIBC_PATH_HEX"] and prior[b"libc_confstr_hex"]==cert[b"LIBC_CONFSTR_HEX"] and prior[b"libc_sha256"]==cert[b"LIBC_SHA256"])
 rootfd=number=py=-1
 try:
  rootfd=open_dir(RUNTIME_ROOT);number=open_under(rootfd,path);held=os.fstat(number);raw=read_all(number,held.st_size);os.close(number);number=-1
  py=open_under(rootfd,PYIMAGE);pyheld=os.fstat(py);pyraw=read_all(py,30626264);os.close(py);py=-1
 finally:close_numbers(tuple(x for x in (number,py,rootfd) if x>=0))
 observed=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,sha(raw))
 certified=(udec(cert[b"LIBC_DEV"],1),udec(cert[b"LIBC_INO"],1),octal(cert[b"LIBC_MODE"]),udec(cert[b"LIBC_NLINK"],1),udec(cert[b"LIBC_UID"]),udec(cert[b"LIBC_GID"]),udec(cert[b"LIBC_BYTES"],1),cert[b"LIBC_SHA256"])
 need(observed==certified and held.st_size==udec(prior[b"libc_bytes"]) and sha(raw)==prior[b"libc_sha256"])
 need(sha(pyraw)==PY_SHA and str(pyheld.st_dev).encode()==prior[b"python_image_dev"] and str(pyheld.st_ino).encode()==prior[b"python_image_ino"])
 result=(prior[b"libc_path_hex"],str(held.st_dev).encode(),str(held.st_ino).encode(),format(held.st_mode,"o").encode(),str(held.st_nlink).encode(),str(held.st_uid).encode(),str(held.st_gid).encode(),str(held.st_size).encode(),prior[b"libc_sha256"],prior[b"libc_confstr_hex"],prior[b"python_image_dev"],prior[b"python_image_ino"],prior[b"python_image_sha256"])
 need(len(result)==13 and result[9]==prior[b"libc_confstr_hex"] and result[5]==cert[b"LIBC_UID"] and result[6]==cert[b"LIBC_GID"]);return result

def launch_b(cert,base_stats):
 empty_r=empty_w=actor_pidfd=-1;left=right=None;pid=-1
 try:
  empty_r,empty_w=os.pipe2(os.O_CLOEXEC);os.close(empty_w);empty_w=-1
  left,right=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC|socket.SOCK_NONBLOCK)
  actor_pid=os.getpid();actor_pidfd=os.pidfd_open(actor_pid,0);pid=os.fork()
  if pid==0:
   try:
    left.close();left=None
    mapping=((empty_r,0),(right.fileno(),3),(actor_pidfd,4),(base_stats[b"attempt_fd"],5),(base_stats[b"cgroup_fd"],6),(104,7),(105,8),(101,9),(106,100))
    preserved_map(mapping);os.close(1);os.close(2)
    close_range(10,99);close_range(101,UINT_MAX)
    child_context(None,base_stats[b"safe"].st_dev,base_stats[b"safe"].st_ino);scrub_exact({0,3,4,5,6,7,8,9,100})
    argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",b"RECOVER_V4",AUTH_ID,str(actor_pid).encode(),cert[b"PLAN_SHA256"],cert[b"RECOVERY_SHA256"],str(base_stats[b"safe"].st_dev).encode(),str(base_stats[b"safe"].st_ino).encode())
    os.execve(PYTHON,argv,ENV)
   except BaseException:os._exit(97)
  right.close();right=None;os.close(empty_r);empty_r=-1;os.close(actor_pidfd);actor_pidfd=-1
  result=left;left=None;return pid,result
 finally:
  close_numbers(tuple(x for x in (empty_r,empty_w,actor_pidfd) if x>=0))
  for endpoint in (left,right):
   if endpoint is not None:
    try:endpoint.close()
    except BaseException:pass

def launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd):
 pidfd_cell=ctypes.c_int(-1);args=CloneArgs();args.flags=CLONE_PIDFD|CLONE_INTO_CGROUP
 args.pidfd=ctypes.addressof(pidfd_cell);args.exit_signal=int(signal.SIGCHLD);args.cgroup=cgfd
 pid=LIBC.syscall(SYS_CLONE3,ctypes.byref(args),ctypes.sizeof(args))
 if pid<0:raise ConsumedIndeterminate("clone-return")
 if pid==0:
  try:
   os.kill(os.getpid(),signal.SIGSTOP)
   preserved_map(((in_r,0),(out_w,1),(err_w,2),(outer_fd,100)))
   close_range(3,99);close_range(101,UINT_MAX)
   child_context(AUTH_ID,safe.st_dev,safe.st_ino);scrub_exact({0,1,2,100})
   os.execve(PYTHON,tuple(argv),ENV)
  except BaseException:os._exit(98)
 need(pid>=2 and pidfd_cell.value>=0,ConsumedIndeterminate)
 return pid,pidfd_cell.value

def recv_result(control,deadline,ordinal,probe,pid):
 raw=recv_control(control,deadline)
 keys=(b"ordinal",b"probe",b"outer_pid",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_frames",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_frames",b"cgroup_empty",b"fault_set",b"capture_done_ns")
 values=parse_packet(raw,b"V4_RESULT",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==pid)
 out_need=udec(values[b"stdout_len"],0,STREAM_CAP);err_need=udec(values[b"stderr_len"],0,STREAM_CAP)
 out_frames=udec(values[b"stdout_frames"],0,49);err_frames=udec(values[b"stderr_frames"],0,49)
 need(out_frames==(out_need+64999)//65000 and err_frames==(err_need+64999)//65000)
 h64(values[b"stdout_sha256"]);h64(values[b"stderr_sha256"]);parse_fault_csv(values[b"fault_set"],True)
 out=bytearray();err=bytearray()
 for stream,total,target in ((b"STDOUT",out_frames,out),(b"STDERR",err_frames,err)):
  for index in range(total):
   frame=recv_control(control,deadline,65536)
   cut=frame.find(b"\n");need(cut>0)
   header=frame[:cut+1];payload=frame[cut+1:]
   fields=parse_packet(header,b"V4_RESULT_FRAME",(b"ordinal",b"probe",b"stream",b"index",b"bytes",b"sha256"))
   need(udec(fields[b"ordinal"],0,14)==ordinal and fields[b"probe"]==probe and fields[b"stream"]==stream)
   need(udec(fields[b"index"])==index and udec(fields[b"bytes"],1,65000)==len(payload) and sha(payload)==fields[b"sha256"])
   target.extend(payload)
 end=parse_packet(recv_control(control,deadline),b"V4_RESULT_END",(b"state",b"ordinal",b"probe"))
 need(end[b"state"]==b"RESULT_END" and udec(end[b"ordinal"],0,14)==ordinal and end[b"probe"]==probe)
 need(len(out)==out_need and len(err)==err_need and sha(out)==values[b"stdout_sha256"] and sha(err)==values[b"stderr_sha256"])
 return values,bytes(out),bytes(err)

def transcript_language(raw):
 if not (type(raw)is bytes and 0<len(raw)<=STREAM_CAP and raw.endswith(b"\n")):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})
 if not all(x==10 or 32<=x<=126 for x in raw):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})
 lines=raw[:-1].split(b"\n")
 if not lines or not all(lines):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})

PHASE_FAULT={b"STAGE":b"STAGING_FAULT",b"CONTAIN":b"CONTAINMENT_FAULT",b"STREAM_ARM":b"FD_TRANSFER",b"CLONE":b"RELEASE_EFFECT_UNKNOWN",b"STOP":b"STOP_WAIT_UNKNOWN",b"PIDFD_ARM":b"PIDFD_BINDING",b"RELEASE_RECORD":b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"SIGCONT":b"RELEASE_EFFECT_UNKNOWN",b"WAIT":b"DIRECT_WAIT_UNKNOWN",b"RESULT":b"CAPTURE_IO",b"LANGUAGE":b"TRANSCRIPT_LANGUAGE",b"STRUCTURE":b"TRANSCRIPT_STRUCTURE",b"SEMANTICS":b"TRANSCRIPT_SEMANTICS",b"RECEIPT":b"ACK_DURABILITY_UNKNOWN",b"REMOVE":b"CONTAINMENT_NOT_EMPTY",b"FINAL":b"REPORT_DURABILITY_UNKNOWN"}

def error_faults(error,phase):
 if isinstance(error,FaultSet):return set(error.faults)
 if isinstance(error,CertificateExpired):return {b"CERTIFICATE_EXPIRED"}
 if isinstance(error,(ConsumedFail,ConsumedIndeterminate)) and phase in PHASE_FAULT:return {PHASE_FAULT[phase]}
 return {b"INTERNAL_INVARIANT"}

def send_abort(control,state,ordinal,probe,faults,deadline,terminal_deadline=0):
 effect=b"PREBEGIN" if PREFLIGHT else b"CONSUMED"
 raw=packet(b"V4_ABORT",((b"sender",b"A"),(b"state",state),(b"ordinal",b"NONE" if ordinal is None else str(ordinal).encode()),(b"probe",probe),(b"effect_state",effect),(b"stage_present",b"1" if STAGE_PRESENT else b"0"),(b"release_disabled",b"1"),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"fault_set",fault_csv(faults))))
 send_plain(control,raw,deadline)

def run_probe(control,ordinal,probe,cgfd,safefd,safe,outer_source,ctx,p01c,cert):
 phase=b"STREAM_ARM";release_origin=time.monotonic_ns();launch_deadline=release_origin+LAUNCH_NS
 in_r=in_w=out_r=out_w=err_r=err_w=outer_fd=events=kill=pidfd=-1;pid=-1;direct_wait_entered=False
 try:
  checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  in_r,in_w=os.pipe2(os.O_CLOEXEC);os.close(in_w);in_w=-1;need(os.read(in_r,1)==b"")
  out_r,out_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK);err_r,err_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
  need(os.fstat(out_r).st_ino!=os.fstat(err_r).st_ino);outer_fd=memfd(outer_source,"p27-v15-outer-v4")
  events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  stream=packet(b"V4_STREAM_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode()),(b"stdout_dev",str(os.fstat(out_r).st_dev).encode()),(b"stdout_ino",str(os.fstat(out_r).st_ino).encode()),(b"stderr_dev",str(os.fstat(err_r).st_dev).encode()),(b"stderr_ino",str(os.fstat(err_r).st_ino).encode()),(b"events_dev",str(os.fstat(events).st_dev).encode()),(b"events_ino",str(os.fstat(events).st_ino).encode()),(b"kill_dev",str(os.fstat(kill).st_dev).encode()),(b"kill_ino",str(os.fstat(kill).st_ino).encode())))
  send_rights(control,stream,(out_r,err_r,events,kill),launch_deadline)
  close_numbers((out_r,err_r,events,kill));out_r=err_r=events=kill=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V4_STREAMS_ARMED",(b"ordinal",b"probe"))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe);progress(cert,launch_deadline,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS))
  phase=b"CLONE";argv=source_argv(probe,safe,p01c);pid,pidfd=launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd)
  close_numbers((in_r,out_w,err_w,outer_fd));in_r=out_w=err_w=outer_fd=-1
  phase=b"STOP";stopped=wait_status(pid,os.WUNTRACED,launch_deadline,b"STOP_WAIT_UNKNOWN")
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP,ConsumedIndeterminate)
  exact_child_cgroup(cgfd,pid);need(not cgroup_empty(cgfd),ConsumedIndeterminate)
  phase=b"PIDFD_ARM";arm=packet(b"V4_PIDFD_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"pidfd_bound",b"1")))
  send_rights(control,arm,(pidfd,),launch_deadline);os.close(pidfd);pidfd=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V4_PIDFD_ARMED",(b"ordinal",b"probe",b"pidfd_bound"))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe and armed[b"pidfd_bound"]==b"1")
  outer_pid=pid;cg=os.fstat(cgfd)
  phase=b"RELEASE_RECORD";release=packet(b"V4_RELEASE_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_bound",b"1"),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"cgroup_dev",str(cg.st_dev).encode()),(b"cgroup_ino",str(cg.st_ino).encode()),(b"cgroup_mode",format(cg.st_mode,"o").encode()),(b"cgroup_nlink",str(cg.st_nlink).encode()),(b"cgroup_uid",str(cg.st_uid).encode()),(b"cgroup_gid",str(cg.st_gid).encode()),(b"argv_sha256",sha(b"\x00".join(argv))),(b"env_sha256",sha(b"\x00".join(x+b"="+ENV[x] for x in sorted(ENV)))),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode())))
  send_plain(control,release,launch_deadline)
  released=parse_packet(recv_control(control,launch_deadline),b"V4_RELEASE_DURABLE",(b"ordinal",b"probe",b"release_sha256"))
  need(udec(released[b"ordinal"],0,14)==ordinal and released[b"probe"]==probe);release_sha=h64(released[b"release_sha256"])
  phase=b"SIGCONT";checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  call_entry=time.monotonic_ns();need(call_entry+SIGCONT_NS<=launch_deadline,ConsumedIndeterminate)
  os.kill(pid,signal.SIGCONT);release_return=time.monotonic_ns()
  need(release_return<=call_entry+SIGCONT_NS and release_return<=launch_deadline,ConsumedIndeterminate)
  checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  phase=b"WAIT";direct_wait_entered=True
  raw=wait_status(pid,0,release_origin+HOST_NS,b"DIRECT_WAIT_UNKNOWN");pid=-1;direct_done=time.monotonic_ns()
  phase=b"RESULT";values,stdout,stderr=recv_result(control,release_origin+HOST_NS,ordinal,probe,outer_pid)
  done=udec(values[b"capture_done_ns"]);host_complete=max(direct_done,done);ack_deadline=min(release_origin+TOTAL_NS,host_complete+ACK_NS)
  need(time.monotonic_ns()<=ack_deadline and ack_deadline-host_complete<=ACK_NS,ConsumedIndeterminate)
  faults=parse_fault_csv(values[b"fault_set"],True)
  if values[b"pidfd_bound"]!=b"1" or values[b"pidfd_exit_ready_observed"]!=b"1":faults.add(b"PIDFD_BINDING")
  if values[b"stdout_eof"]!=b"1" or values[b"stderr_eof"]!=b"1":faults.add(b"CAPTURE_IO")
  if values[b"cgroup_empty"]!=b"1":faults.add(b"CONTAINMENT_NOT_EMPTY")
  if stderr:faults.add(b"STDERR_NONEMPTY")
  if raw!=0:faults.add(b"OUTER_STATUS")
  if host_complete>release_origin+HOST_NS:faults.add(b"WATCHDOG_DEADLINE")
  if faults:raise FaultSet(faults)
  try:
   if not cgroup_empty(cgfd):raise FaultSet({b"CONTAINMENT_NOT_EMPTY"})
  except FaultSet:raise
  except BaseException as error:raise FaultSet({b"CONTAINMENT_OBSERVATION_UNKNOWN"}) from error
  phase=b"LANGUAGE";transcript_language(stdout)
  phase=b"STRUCTURE"
  try:rows,outer_claims=transcript_structure(stdout,probe)
  except BaseException as error:raise FaultSet({b"TRANSCRIPT_STRUCTURE"}) from error
  phase=b"SEMANTICS"
  try:rows=transcript_semantics(rows,outer_claims,probe,ctx)
  except FaultSet:raise
  except BaseException as error:raise FaultSet({b"TRANSCRIPT_SEMANTICS"}) from error
  phase=b"RECEIPT";candidate=packet(b"V4_VALIDATED_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_record_sha256",release_sha),(b"release_origin_ns",str(release_origin).encode()),(b"release_return_ns",str(release_return).encode()),(b"host_complete_ns",str(host_complete).encode()),(b"capture_done_ns",str(done).encode()),(b"direct_wait_state",b"COMPLETE"),(b"outer_raw_status",str(raw).encode()),(b"pidfd_bound",b"1"),(b"pidfd_exit_ready_observed",b"1"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1"),(b"stdout_overflow",b"0"),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",EMPTY_SHA),(b"stderr_eof",b"1"),(b"stderr_overflow",b"0"),(b"cgroup_empty",b"1"),(b"parser_language",b"ACCEPTED"),(b"parser_structure",b"ACCEPTED"),(b"parser_semantics",b"ACCEPTED"),(b"candidate",b"ACCEPTED"),(b"terminal",b"ACCEPTED"),(b"certificate_expiry_realtime_ns",cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])))
  send_plain(control,candidate,ack_deadline)
  validated=parse_packet(recv_control(control,ack_deadline),b"V4_VALIDATED_DURABLE",(b"ordinal",b"probe",b"validated_sha256"))
  need(udec(validated[b"ordinal"],0,14)==ordinal and validated[b"probe"]==probe);validated_sha=h64(validated[b"validated_sha256"])
  checkpoint(cert,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,ack_deadline)
  actor_ack=time.monotonic_ns();need(actor_ack-host_complete<=ACK_NS,ConsumedIndeterminate)
  intent=packet(b"V4_ACK_COMMIT_INTENT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha),(b"host_complete_ns",str(host_complete).encode()),(b"ack_deadline_ns",str(ack_deadline).encode()),(b"actor_ack_intent_ns",str(actor_ack).encode())))
  send_plain(control,intent,ack_deadline)
  committed=parse_packet(recv_control(control,ack_deadline),b"V4_COMMITTED",(b"ordinal",b"probe",b"ack_sha256"))
  need(udec(committed[b"ordinal"],0,14)==ordinal and committed[b"probe"]==probe);ack_sha=h64(committed[b"ack_sha256"])
  checkpoint(cert,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,ack_deadline)
  seen=packet(b"V4_COMMITTED_SEEN",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha),(b"host_complete_ns",str(host_complete).encode()),(b"ack_deadline_ns",str(ack_deadline).encode())))
  send_plain(control,seen,ack_deadline);need(time.monotonic_ns()-host_complete<=ACK_NS,ConsumedIndeterminate);return rows,ack_sha
 except BaseException as error:
  faults=error_faults(error,phase)
  try:send_abort(control,phase,ordinal,probe,faults,min(release_origin+TOTAL_NS,time.monotonic_ns()+ACK_NS))
  except BaseException as send_error:faults.update(error_faults(send_error,phase))
  if pid>=0 and not direct_wait_entered:
   direct_wait_entered=True
   try:wait_status(pid,0,release_origin+TOTAL_NS,b"DIRECT_WAIT_UNKNOWN");pid=-1
   except FaultSet as wait_error:faults.update(wait_error.faults)
  raised=FaultSet(faults);setattr(raised,"p27_abort_sent",True);setattr(raised,"p27_phase",phase);raise raised
 finally:
  close_numbers(tuple(number for number in (in_r,in_w,out_r,out_w,err_r,err_w,outer_fd,events,kill,pidfd) if number>=0))

def mount_semantics(line,fstype,required,forbidden):
 pieces=line[:-1].split(b" - ");need(len(pieces)==2)
 left=pieces[0].split(b" ");right=pieces[1].split(b" ");need(len(left)>=6 and len(right)>=3 and right[0]==fstype)
 options=set(left[5].split(b","))|set(right[2].split(b","))
 need(required<=options and not (forbidden&options),Refuse)

def mount_graph(cert):
 number=-1
 try:
  number=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,1048576),1048576)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 rows={}
 for line in raw.splitlines():
  left,right=line.split(b" - ",1);fields=left.split(b" ");need(len(fields)>=6,Refuse)
  mid=udec(fields[0],1);parent=udec(fields[1],1);options=set(fields[5].split(b","))
  need(mid not in rows,Refuse);rows[mid]=(parent,options)
 runtime=udec(cert[b"RUNTIME_ROOT_MOUNT_ID"],1);safe=udec(cert[b"SAFE_BIND_MOUNT_ID"],1)
 need(runtime in rows and safe in rows and runtime!=safe,Refuse)
 def descends(mid,ancestor):
  seen=set()
  while mid in rows and mid not in seen:
   if mid==ancestor:return True
   seen.add(mid);mid=rows[mid][0]
  return False
 writable=[mid for mid,(parent,options) in rows.items() if mid!=runtime and descends(mid,runtime) and b"rw" in options]
 need(writable==[safe] and cert[b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT"]==b"1",Refuse)

def base_identity(number,cert,prefix):
 held=os.fstat(number)
 expected=(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),octal(cert[prefix+b"_MODE"]),udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"]))
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==expected,Refuse)
 return held

def signal_snapshot(cert):
 need(all(signal.getitimer(which)==(0.0,0.0) for which in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF)),Refuse)
 previous=signal.pthread_sigmask(signal.SIG_BLOCK,set());need(previous==set(),Refuse)
 valid=tuple(sorted(int(x) for x in signal.valid_signals()))
 catchable=tuple(x for x in valid if x not in (int(signal.SIGKILL),int(signal.SIGSTOP)))
 defaults=[]
 for number in catchable:
  need(signal.getsignal(number)==signal.SIG_DFL,Refuse);defaults.append(str(number).encode()+b":DFL\n")
 need(len(valid)==udec(cert[b"VALID_SIGNAL_COUNT"]) and len(defaults)==udec(cert[b"DEFAULT_SIGNAL_COUNT"]),Refuse)
 need(sha(b"".join(defaults))==cert[b"DEFAULTS_SHA256"],Refuse)

def b_send(control,raw,deadline):
 send_plain(control,raw,deadline)

def request_refusal(control,begin_state,arm_state,reason,deadline):
 raw=packet(b"V4_REFUSE_PRECOMMIT",((b"state",b"REFUSE_PRECOMMIT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"reason",reason),(b"consume_deadline_ns",str(deadline).encode())))
 send_plain(control,raw,deadline)
 ack=parse_packet(recv_control(control,deadline),b"V4_REFUSE_ACK",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"b_state",b"consume_deadline_ns",b"disposition"))
 need(ack[b"state"]==b"REFUSE_ACK" and ack[b"ordinal"]==ack[b"probe"]==b"NONE" and ack[b"auth_id"]==AUTH_ID)
 need(ack[b"a_begin_state"]==begin_state and ack[b"a_arm_state"]==arm_state and ack[b"disposition"]==b"UNCONSUMED")
 need(udec(ack[b"consume_deadline_ns"])==deadline and ack[b"b_state"] in (b"ARM_NOT_ENTERED",b"ARM_SENT"));return True

def failure_recv(control,deadline):
 while True:
  try:return recv_control(control,deadline)
  except RemoteAbort as error:
   values=error.values;need(values[b"sender"]==b"B" and values[b"state"]==b"CLEANUP_RELEASE_DISABLE")
   remote_deadline=udec(values[b"terminal_deadline_ns"],1);need(time.monotonic_ns()<=remote_deadline<=deadline)
   send_abort(control,b"CLEANUP_RELEASE_DISABLED",None,values[b"probe"],set(error.faults),remote_deadline,remote_deadline)

def await_failure_terminal(control,outer_deadline):
 raw=failure_recv(control,outer_deadline)
 values=parse_packet(raw,b"V4_TERMINAL_FAILURE_DURABLE",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"disposition",b"terminal_deadline_ns"))
 subject=h64(values[b"subject_sha256"]);deadline=udec(values[b"terminal_deadline_ns"],1)
 need(values[b"state"]==b"TERMINAL_FAILURE_DURABLE" and values[b"ordinal"]==values[b"probe"]==b"NONE")
 need(values[b"kind"] in (b"FAILURE",b"COLLISION_VOLATILE") and values[b"disposition"] in (b"CONSUMED_FAIL",b"CONSUMED_INDETERMINATE"))
 need(time.monotonic_ns()<=deadline<=outer_deadline)
 seen=packet(b"V4_TERMINAL_SEEN",((b"state",b"TERMINAL_SEEN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",values[b"kind"]),(b"subject_sha256",subject),(b"terminal_deadline_ns",str(deadline).encode())))
 send_plain(control,seen,deadline)
 ack=parse_packet(failure_recv(control,deadline),b"V4_TERMINAL_ACK",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_seen_sha256",b"report_sha256",b"reconciliation_token",b"ack_state",b"terminal_deadline_ns"))
 need(ack[b"state"]==b"TERMINAL_ACK" and ack[b"ordinal"]==ack[b"probe"]==b"NONE" and ack[b"kind"]==values[b"kind"] and ack[b"subject_sha256"]==subject)
 need(ack[b"report_sha256"]==subject and ack[b"reconciliation_token"]==b"NONE" and ack[b"ack_state"]==b"FAILURE_COMMITTED" and udec(ack[b"terminal_deadline_ns"])==deadline)
 receipt_ns=time.monotonic_ns();receipt=packet(b"V4_TERMINAL_ACK_RECEIPT",((b"state",b"ACK_RECEIVED_NO_REPLAY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",values[b"kind"]),(b"subject_sha256",subject),(b"report_sha256",subject),(b"reconciliation_token",b"NONE"),(b"actor_receipt_ns",str(receipt_ns).encode()),(b"terminal_deadline_ns",str(deadline).encode())))
 send_plain(control,receipt,deadline)
 closed=parse_packet(failure_recv(control,deadline),b"V4_TERMINAL_CLOSED",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"closure_sha256",b"owner",b"terminal_deadline_ns"))
 need(closed[b"state"]==b"OWNER_CLOSED" and closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"kind"]==values[b"kind"])
 need(closed[b"subject_sha256"]==subject and closed[b"closure_sha256"]==subject and closed[b"owner"]==b"B" and udec(closed[b"terminal_deadline_ns"])==deadline)
 return values[b"disposition"],deadline

def main():
 global AUTH_ID,PREFLIGHT,CERT,STAGE_PRESENT
 entry_mono=time.monotonic_ns();state=b"INPUT";consumed=False;commit_edge=False
 begin_effect_possible=False;begin_state=b"BEGIN_NOT_ENTERED";arm_state=b"ARM_NOT_OBSERVED";refusal_acked=False
 pass_may_be_committed=False;pass_authoritative=False;receipt_effect_unknown=False;terminal_deadline=0;failure_terminal_deadline=0
 bpid=-1;control=None;runtime=attempt_base=stage_base=cgroup_base=safefd=cgfd=-1
 need(type(sys.argv)is list and len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RUN_V4",Refuse)
 supplied=h64(sys.argv[2].encode("ascii"))
 need(os.environb==ENV and os.read(0,1)==b"" and sys.gettrace() is None and sys.getprofile() is None,Refuse)
 verify_creds(False);need(os.umask(0o077)==0o077,Refuse)
 fd0=os.fstat(0);fd1=os.fstat(1);fd2=os.fstat(2)
 need(stat.S_ISFIFO(fd0.st_mode) and stat.S_ISFIFO(fd1.st_mode) and stat.S_ISFIFO(fd2.st_mode),Refuse)
 fd_access(0,os.O_RDONLY);fd_access(1,os.O_WRONLY);fd_access(2,os.O_WRONLY)
 need((fd1.st_dev,fd1.st_ino)!=(fd2.st_dev,fd2.st_ino),Refuse)
 close_range(3,99);close_range(107,UINT_MAX);scrub_exact({0,1,2,100,101,102,103,104,105,106})
 for number in (100,101,103,104,105,106):seals(number);fd_access(number,os.O_RDWR)
 fd_access(102,os.O_RDONLY)
 actor_raw=read_all(100);snapshot=exact_snapshot(101)
 v15=exact_whole(102,WHOLE_V15,V15_TERMINAL);plan=read_all(103,MAX_FILE)
 cert_raw=read_all(104);envelope_raw=read_all(105);b_raw=read_all(106)
 AUTH_ID=sha(b"P27E001V4\x00"+cert_raw+b"\x00"+envelope_raw);need(AUTH_ID==supplied,Refuse)
 state=b"CERT";envelope=parse_envelope(envelope_raw);CERT,deps=parse_cert(cert_raw)
 need(sha(cert_raw)==envelope[b"CERTIFICATE_SHA256"] and sha(envelope_raw)==CERT[b"ISSUER_ENVELOPE_SHA256"],Refuse)
 need(envelope[b"PLAN_SHA256"]==CERT[b"PLAN_SHA256"] and envelope[b"RUNNER_SHA256"]==CERT[b"RUNNER_SHA256"] and envelope[b"RECOVERY_SHA256"]==CERT[b"RECOVERY_SHA256"],Refuse)
 need(sha(plan)==CERT[b"PLAN_SHA256"] and sha(actor_raw)==CERT[b"RUNNER_SHA256"] and sha(b_raw)==CERT[b"RECOVERY_SHA256"],Refuse)
 need(envelope[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot),Refuse)
 need(envelope[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and envelope[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672",Refuse)
 need(envelope[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX,Refuse)
 not_before=udec(CERT[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(envelope[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(envelope[b"NOT_AFTER_REALTIME_NS"]),Refuse)
 checkpoint(CERT,horizon_needed(entry_mono+PRECONSUME_NS,CONSUME_REMAIN_NS),Refuse,entry_mono+PRECONSUME_NS);verify_platform(CERT);signal_snapshot(CERT)
 ab=b"P27 RUNNER V4 ACTOR SOURCE "+b"BEGIN A4C8E712";ae=b"P27 RUNNER V4 ACTOR SOURCE "+b"END A4C8E712"
 bb=b"P27 RUNNER V4 WATCHDOG SOURCE "+b"BEGIN E6A1954C";be=b"P27 RUNNER V4 WATCHDOG SOURCE "+b"END E6A1954C"
 need(extract_one(plan,ab,ae)==actor_raw and extract_one(plan,bb,be)==b_raw,Refuse)
 sources=v15_sources(v15)
 state=b"ENTRY"
 try:
  runtime=open_dir(RUNTIME_ROOT);attempt_base=open_dir(ATTEMPT_BASE);stage_base=open_dir(STAGE_BASE);cgroup_base=open_dir(CGROUP_BASE)
  runtime_stat=base_identity(runtime,CERT,b"RUNTIME_ROOT");runtime_mid,runtime_line=mount_line(runtime)
  need(runtime_mid==udec(CERT[b"RUNTIME_ROOT_MOUNT_ID"],1) and sha(runtime_line)==CERT[b"RUNTIME_ROOT_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(runtime_line,even_hex(CERT[b"RUNTIME_ROOT_FSTYPE_HEX"]),{b"ro",b"nosuid",b"nodev"},{b"rw"})
  for entry in deps:verify_dependency(runtime,entry)
  attempt_stat=base_identity(attempt_base,CERT,b"ATTEMPT_BASE");attempt_mid,attempt_line=mount_line(attempt_base)
  need(attempt_mid==udec(CERT[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==CERT[b"ATTEMPT_BASE_MOUNTINFO_SHA256"],Refuse)
  stage_stat=base_identity(stage_base,CERT,b"SAFE_BIND");stage_mid,stage_line=mount_line(stage_base)
  need(stage_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(stage_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(stage_line,even_hex(CERT[b"SAFE_BIND_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev",b"noexec"},{b"ro"})
  cgroup_stat=base_identity(cgroup_base,CERT,b"CGROUP_BASE");cg_mid,cg_line=mount_line(cgroup_base)
  need(statfs_magic(cgroup_base)==CGROUP2_MAGIC and cg_mid==udec(CERT[b"CGROUP2_MOUNT_ID"],1) and sha(cg_line)==CERT[b"CGROUP2_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(cg_line,b"cgroup2",{b"rw"},{b"ro"})
  base_type=base_controllers=base_subtree=-1
  try:
   base_type=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   base_controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   base_subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"],Refuse)
   need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"],Refuse)
   need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"],Refuse)
  finally:close_numbers((base_type,base_controllers,base_subtree))
  need(runtime_mid!=stage_mid,Refuse);mount_graph(CERT)
  absent(attempt_base,AUTH_ID,Refuse);absent(stage_base,AUTH_ID,Refuse);absent(cgroup_base,AUTH_ID,Refuse)
  need(time.monotonic_ns()-entry_mono<=PRECONSUME_NS,Refuse)
  bases={b"attempt_fd":attempt_base,b"cgroup_fd":cgroup_base,b"safe":stage_stat}
  state=b"B_BOOT";bpid,control=launch_b(CERT,bases);need(fcntl.fcntl(control.fileno(),fcntl.F_GETFL)&os.O_NONBLOCK,Refuse)
  os.close(attempt_base);attempt_base=-1
  ready_deadline=entry_mono+PRECONSUME_NS
  ready=parse_packet(recv_control(control,ready_deadline),b"V4_READY",(b"state",b"ordinal",b"probe"))
  need(ready[b"state"]==b"READY" and ready[b"ordinal"]==ready[b"probe"]==b"NONE",Refuse)
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,ready_deadline)
  consume_origin=time.monotonic_ns();consume_deadline=consume_origin+CONSUMPTION_NS
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,consume_deadline)
  state=b"BEGIN_SEND_EFFECT_UNKNOWN";begin_state=b"BEGIN_SEND_EFFECT_UNKNOWN";begin_effect_possible=True
  begin=packet(b"V4_CONSUME_BEGIN",((b"state",b"CONSUME_BEGIN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"consume_origin_ns",str(consume_origin).encode()),(b"consume_deadline_ns",str(consume_deadline).encode())))
  b_send(control,begin,consume_deadline);begin_state=b"BEGIN_SENT";state=b"BEGIN_SENT"
  arm_state=b"ARM_RECEIVE_EFFECT_UNKNOWN";state=b"ARM_RECEIVE_EFFECT_UNKNOWN"
  armed=parse_packet(recv_control(control,consume_deadline),b"V4_CONSUME_ARMED",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"b_arm_state",b"consume_origin_ns",b"consume_deadline_ns"))
  need(armed[b"state"]==b"CONSUME_ARMED" and armed[b"ordinal"]==armed[b"probe"]==b"NONE" and armed[b"auth_id"]==AUTH_ID)
  need(armed[b"a_begin_state"]==b"BEGIN_SEND_EFFECT_UNKNOWN" and armed[b"b_arm_state"]==b"ARM_SEND_EFFECT_UNKNOWN")
  need(udec(armed[b"consume_origin_ns"])==consume_origin and udec(armed[b"consume_deadline_ns"])==consume_deadline)
  arm_state=b"ARMED_CONFIRMED";state=b"ARMED_CONFIRMED"
  commit_edge=True;consumed=True;PREFLIGHT=False;state=b"COMMIT_SEND_EFFECT_UNKNOWN"
  commit=packet(b"V4_CONSUME_COMMIT",((b"state",b"CONSUME_COMMIT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"a_commit_state",b"COMMIT_SEND_EFFECT_UNKNOWN"),(b"consume_origin_ns",str(consume_origin).encode()),(b"consume_deadline_ns",str(consume_deadline).encode())))
  b_send(control,commit,consume_deadline);state=b"COMMIT_SENT"
  consumed_msg=parse_packet(recv_control(control,consume_deadline),b"V4_CONSUMED_DURABLE",(b"state",b"ordinal",b"probe",b"auth_id",b"intent_sha256",b"consume_origin_ns",b"consume_deadline_ns",b"attempt_fd_state"))
  need(consumed_msg[b"state"]==b"CONSUMED_DURABLE" and consumed_msg[b"ordinal"]==consumed_msg[b"probe"]==b"NONE" and consumed_msg[b"auth_id"]==AUTH_ID)
  need(udec(consumed_msg[b"consume_origin_ns"])==consume_origin and udec(consumed_msg[b"consume_deadline_ns"])==consume_deadline and consumed_msg[b"attempt_fd_state"]==b"PUBLISHED")
  chain_sha=h64(consumed_msg[b"intent_sha256"]);checkpoint(CERT,PRE_STAGE_REMAIN_NS,ConsumedIndeterminate,consume_deadline)
  state=b"STAGE";stage_origin=time.monotonic_ns();stage_deadline=stage_origin+STAGE_NS
  checkpoint(CERT,PRE_STAGE_REMAIN_NS,ConsumedIndeterminate,stage_deadline)
  os.mkdir(AUTH_ID,0o700,dir_fd=stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS));os.fsync(stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS))
  safefd=os.open(AUTH_ID,O_DIR,dir_fd=stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS));safe=os.fstat(safefd)
  need((safe.st_uid,safe.st_gid,stat.S_IMODE(safe.st_mode),safe.st_nlink)==(0,0,0o700,2),ConsumedIndeterminate)
  named=os.stat(AUTH_ID,dir_fd=stage_base,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(safe.st_dev,safe.st_ino,safe.st_mode,safe.st_nlink,safe.st_uid,safe.st_gid),ConsumedIndeterminate)
  for name in (b"target",b"a",b"b"):absent(safefd,name)
  for name,body,identity in zip(SOURCE_NAMES,sources[1:],SOURCE_META[1:]):stage_leaf(safefd,name,body,identity,stage_deadline)
  os.fsync(safefd);progress(CERT,stage_deadline,POST_STAGE_REMAIN_NS)
  STAGE_PRESENT=True
  staged=packet(b"V4_STAGE_DURABLE",((b"state",b"STAGE_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"stage_origin_ns",str(stage_origin).encode()),(b"stage_deadline_ns",str(stage_deadline).encode()),(b"stage_return_ns",str(time.monotonic_ns()).encode()),(b"safe_dev",str(safe.st_dev).encode()),(b"safe_ino",str(safe.st_ino).encode()),(b"safe_mode",format(safe.st_mode,"o").encode()),(b"safe_nlink",str(safe.st_nlink).encode()),(b"safe_uid",str(safe.st_uid).encode()),(b"safe_gid",str(safe.st_gid).encode()),(b"keeper_sha256",CERT[b"KEEPER_SHA256"]),(b"launcher_sha256",CERT[b"LAUNCHER_SHA256"]),(b"marker_sha256",CERT[b"MARKER_SHA256"]),(b"child_sha256",CERT[b"CHILD_SHA256"])))
  send_rights(control,staged,(safefd,),stage_deadline)
  stage_ack=parse_packet(recv_control(control,stage_deadline),b"V4_STAGE_ACK",(b"state",b"ordinal",b"probe",b"stage_deadline_ns",b"safe_dev",b"safe_ino"))
  need(stage_ack[b"state"]==b"STAGE_BOUND" and stage_ack[b"ordinal"]==stage_ack[b"probe"]==b"NONE")
  need(udec(stage_ack[b"stage_deadline_ns"])==stage_deadline and (udec(stage_ack[b"safe_dev"]),udec(stage_ack[b"safe_ino"]))==(safe.st_dev,safe.st_ino))
  progress(CERT,stage_deadline,POST_STAGE_REMAIN_NS)
  state=b"CONTAIN";contain_origin=time.monotonic_ns();contain_deadline=contain_origin+ACK_NS
  os.mkdir(AUTH_ID,0o700,dir_fd=cgroup_base);progress(CERT,contain_deadline,horizon_needed(contain_deadline,POST_CONTAIN_REMAIN_NS))
  cgfd=os.open(AUTH_ID,O_DIR,dir_fd=cgroup_base);progress(CERT,contain_deadline,horizon_needed(contain_deadline,POST_CONTAIN_REMAIN_NS));cgchild=os.fstat(cgfd)
  need((format(cgchild.st_mode,"o").encode(),cgchild.st_uid,cgchild.st_gid,cgchild.st_nlink)==(CERT[b"CGROUP_CHILD_MODE"],0,0,2),ConsumedIndeterminate)
  need(cgroup_empty(cgfd),ConsumedIndeterminate)
  ctype=controllers=subtree=-1
  try:
   ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   type_raw=read_all(ctype,128);controllers_raw=read_all(controllers,4096);subtree_raw=read_all(subtree,4096)
   need(type_raw.hex().encode()==CERT[b"CGROUP_CHILD_TYPE_HEX"],ConsumedIndeterminate)
   need(controllers_raw.hex().encode()==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"],ConsumedIndeterminate)
   need(subtree_raw.hex().encode()==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"],ConsumedIndeterminate)
  finally:close_numbers(tuple(x for x in (ctype,controllers,subtree) if x>=0))
  cgbase=os.fstat(cgroup_base);cg_mid,cg_line=mount_line(cgfd)
  containment=packet(b"V4_CONTAINMENT",((b"state",b"CONTAINMENT_CANDIDATE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"contain_origin_ns",str(contain_origin).encode()),(b"contain_deadline_ns",str(contain_deadline).encode()),(b"dev",str(cgchild.st_dev).encode()),(b"ino",str(cgchild.st_ino).encode()),(b"mode",format(cgchild.st_mode,"o").encode()),(b"nlink",str(cgchild.st_nlink).encode()),(b"uid",str(cgchild.st_uid).encode()),(b"gid",str(cgchild.st_gid).encode()),(b"base_dev",str(cgbase.st_dev).encode()),(b"base_ino",str(cgbase.st_ino).encode()),(b"mount_id",str(cg_mid).encode()),(b"mountinfo_sha256",sha(cg_line)),(b"type_hex",type_raw.hex().encode()),(b"controllers_hex",controllers_raw.hex().encode()),(b"subtree_control_hex",subtree_raw.hex().encode())))
  send_rights(control,containment,(cgfd,),contain_deadline)
  contain_ack=parse_packet(recv_control(control,contain_deadline),b"V4_CONTAINMENT_ACK",(b"state",b"ordinal",b"probe",b"contain_deadline_ns",b"dev",b"ino"))
  need(contain_ack[b"state"]==b"CONTAINMENT_BOUND" and contain_ack[b"ordinal"]==contain_ack[b"probe"]==b"NONE")
  need(udec(contain_ack[b"contain_deadline_ns"])==contain_deadline and (udec(contain_ack[b"dev"]),udec(contain_ack[b"ino"]))==(cgchild.st_dev,cgchild.st_ino))
  progress(CERT,contain_deadline,POST_CONTAIN_REMAIN_NS)
  safe_path=STAGE_BASE+b"/"+AUTH_ID
  ctx={b"cwd_hex":safe_path.hex().encode(),b"python_dev":udec(CERT[b"PYTHON_IMAGE_DEV"],1),b"python_ino":udec(CERT[b"PYTHON_IMAGE_INO"],1),b"libc_path_hex":CERT[b"LIBC_PATH_HEX"],b"libc_confstr_hex":CERT[b"LIBC_CONFSTR_HEX"],b"libc_bytes":udec(CERT[b"LIBC_BYTES"],1),b"libc_sha":CERT[b"LIBC_SHA256"],b"valid_signals":udec(CERT[b"VALID_SIGNAL_COUNT"]),b"default_signals":udec(CERT[b"DEFAULT_SIGNAL_COUNT"]),b"defaults_sha":CERT[b"DEFAULTS_SHA256"],b"child_source":sources[4]}
  prior=None
  for ordinal,probe in enumerate(SUITE):
   checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS)
   p01c=derive_p01c(prior,CERT) if probe==b"P01C" else ()
   rows,chain_sha=run_probe(control,ordinal,probe,cgfd,safefd,safe,sources[0],ctx,p01c,CERT)
   if probe==b"P01D":prior=rows;ctx[b"p01d"]=rows
  state=b"REMOVE";remove_origin=time.monotonic_ns();remove_deadline=remove_origin+REPORT_NS
  checkpoint(CERT,REPORT_NS+FINAL_TOTAL_NS,ConsumedIndeterminate,remove_deadline);need(cgroup_empty(cgfd),ConsumedIndeterminate)
  query=packet(b"V4_EMPTY_FINAL_QUERY",((b"state",b"EMPTY_FINAL_QUERY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"remove_origin_ns",str(remove_origin).encode()),(b"remove_deadline_ns",str(remove_deadline).encode())))
  b_send(control,query,remove_deadline)
  confirmed=parse_packet(recv_control(control,remove_deadline),b"V4_EMPTY_FINAL_CONFIRMED",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"))
  need(confirmed[b"state"]==b"EMPTY_FINAL_CONFIRMED" and confirmed[b"ordinal"]==confirmed[b"probe"]==b"NONE" and confirmed[b"chain_head_sha256"]==chain_sha and udec(confirmed[b"remove_deadline_ns"])==remove_deadline)
  os.close(cgfd);cgfd=-1;os.rmdir(AUTH_ID,dir_fd=cgroup_base)
  try:os.stat(AUTH_ID,dir_fd=cgroup_base,follow_symlinks=False);need(False,ConsumedIndeterminate)
  except FileNotFoundError:pass
  progress(CERT,remove_deadline,FINAL_TOTAL_NS)
  removed=packet(b"V4_CGROUP_REMOVED",((b"state",b"CGROUP_REMOVED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"remove_deadline_ns",str(remove_deadline).encode())))
  b_send(control,removed,remove_deadline)
  removed_ack=parse_packet(recv_control(control,remove_deadline),b"V4_REMOVE_ACK",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"))
  need(removed_ack[b"state"]==b"REMOVE_ACK" and removed_ack[b"ordinal"]==removed_ack[b"probe"]==b"NONE" and removed_ack[b"chain_head_sha256"]==chain_sha and udec(removed_ack[b"remove_deadline_ns"])==remove_deadline)
  state=b"FINAL";terminal_origin=time.monotonic_ns();terminal_deadline=terminal_origin+FINAL_TOTAL_NS
  checkpoint(CERT,FINAL_TOTAL_NS,ConsumedIndeterminate,terminal_deadline)
  finalize=packet(b"V4_FINALIZE_CANDIDATE",((b"state",b"FINALIZE_CANDIDATE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode())))
  b_send(control,finalize,terminal_deadline)
  candidate=parse_packet(recv_control(control,terminal_deadline),b"V4_TERMINAL_CANDIDATE_DURABLE",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"chain_head_sha256",b"terminal_deadline_ns"))
  candidate_sha=h64(candidate[b"subject_sha256"])
  need(candidate[b"state"]==b"TERMINAL_CANDIDATE_DURABLE" and candidate[b"ordinal"]==candidate[b"probe"]==b"NONE" and candidate[b"kind"]==b"SUCCESS_CANDIDATE")
  need(candidate[b"chain_head_sha256"]==chain_sha and udec(candidate[b"terminal_deadline_ns"])==terminal_deadline)
  seen=packet(b"V4_TERMINAL_SEEN",((b"state",b"TERMINAL_SEEN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha),(b"terminal_deadline_ns",str(terminal_deadline).encode())))
  pass_may_be_committed=True;state=b"TERMINAL_SEEN_SEND_EFFECT_UNKNOWN";b_send(control,seen,terminal_deadline);state=b"TERMINAL_SEEN_SENT"
  terminal=parse_packet(recv_control(control,terminal_deadline),b"V4_TERMINAL_ACK",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_seen_sha256",b"report_sha256",b"reconciliation_token",b"ack_state",b"terminal_deadline_ns"))
  need(terminal[b"state"]==b"TERMINAL_ACK" and terminal[b"ordinal"]==terminal[b"probe"]==b"NONE" and terminal[b"kind"]==b"SUCCESS_CANDIDATE")
  need(terminal[b"subject_sha256"]==candidate_sha and terminal[b"ack_state"]==b"PASS_COMMITTED_RECONCILIATION_REQUIRED" and udec(terminal[b"terminal_deadline_ns"])==terminal_deadline)
  terminal_seen_sha=h64(terminal[b"terminal_seen_sha256"]);report_sha=h64(terminal[b"report_sha256"]);reconciliation_token=h64(terminal[b"reconciliation_token"])
  pass_authoritative=True;receipt_ns=time.monotonic_ns()
  receipt=packet(b"V4_TERMINAL_ACK_RECEIPT",((b"state",b"ACK_RECEIVED_NO_REPLAY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha),(b"report_sha256",report_sha),(b"reconciliation_token",reconciliation_token),(b"actor_receipt_ns",str(receipt_ns).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode())))
  receipt_effect_unknown=True;state=b"ACK_RECEIPT_SEND_EFFECT_UNKNOWN";b_send(control,receipt,terminal_deadline);receipt_effect_unknown=False;state=b"ACK_RECEIPT_SENT"
  closed=parse_packet(recv_control(control,terminal_deadline),b"V4_TERMINAL_CLOSED",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"closure_sha256",b"owner",b"terminal_deadline_ns"))
  need(closed[b"state"]==b"OWNER_CLOSED" and closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"kind"]==b"SUCCESS_CANDIDATE")
  need(closed[b"subject_sha256"]==candidate_sha and h64(closed[b"closure_sha256"])!=b"0"*64 and closed[b"owner"]==b"B" and udec(closed[b"terminal_deadline_ns"])==terminal_deadline)
  control.close();control=None
  braw=wait_status(bpid,0,terminal_deadline,b"ACTOR_LOST");bpid=-1
  need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
  result=(b"P27E001_RUNNER_V4|AUTH_ID="+AUTH_ID+b"|entered=15|committed=15|candidate_sha256="+candidate_sha+b"|terminal_seen_sha256="+terminal_seen_sha+b"|report_sha256="+report_sha+b"|reconciliation_token="+reconciliation_token+b"|owner_closed=1|retry_allowed=0\n")
  write_all(1,result)
 except BaseException as error:
  phase=getattr(error,"p27_phase",state);faults=error_faults(error,phase);disposition=None;clean_refusal=False
  if not begin_effect_possible:
   if control is None:clean_refusal=True
   else:
    try:
     deadline=locals().get("ready_deadline",entry_mono+PRECONSUME_NS)
     clean_refusal=request_refusal(control,b"BEGIN_NOT_ENTERED",b"ARM_NOT_OBSERVED",b"PREBEGIN_CLOSED",deadline)
    except BaseException:clean_refusal=False
  elif not commit_edge:
   try:
    refusal_acked=request_refusal(control,begin_state,arm_state,b"BEGIN_OR_ARM_CLOSED",consume_deadline);clean_refusal=refusal_acked
   except BaseException:clean_refusal=False
  elif pass_may_be_committed or pass_authoritative:
   disposition=None
  else:
   if control is not None:
    try:
     if not getattr(error,"p27_abort_sent",False):
      abort_deadline=terminal_deadline if terminal_deadline and time.monotonic_ns()<=terminal_deadline else time.monotonic_ns()+ACK_NS
      send_abort(control,phase,locals().get("ordinal",None),locals().get("probe",b"NONE"),faults,abort_deadline,terminal_deadline)
     outer_deadline=terminal_deadline if terminal_deadline else certificate_mono_expiry(CERT)
     disposition,failure_terminal_deadline=await_failure_terminal(control,outer_deadline)
    except BaseException:disposition=None
  if control is not None:
   try:control.close()
   except BaseException:pass
   control=None
  if bpid>=0 and (clean_refusal or disposition is not None):
   shutdown_deadline=failure_terminal_deadline if disposition is not None else locals().get("consume_deadline",locals().get("ready_deadline",entry_mono+PRECONSUME_NS))
   try:
    shutdown_raw=wait_status(bpid,0,shutdown_deadline,b"ACTOR_LOST");bpid=-1
    if not (os.WIFEXITED(shutdown_raw) and os.WEXITSTATUS(shutdown_raw)==0):clean_refusal=False;disposition=None
   except BaseException:
    clean_refusal=False;disposition=None
  if clean_refusal and (refusal_acked or not begin_effect_possible):raise Refuse("exact-refusal-ack") from error
  if disposition==b"CONSUMED_FAIL":raise ConsumedFail("reported-fail") from error
  raise ConsumedIndeterminate("consumed-or-effect-unknown-no-replay") from error
 finally:
  close_numbers(tuple(number for number in (cgfd,safefd,runtime,attempt_base,stage_base,cgroup_base) if number>=0))

try:
 main()
except Refuse:
 raise SystemExit(80)
except ConsumedFail:
 raise SystemExit(81)
except ConsumedIndeterminate:
 raise SystemExit(82)
except BaseException:
 raise SystemExit(83)
raise SystemExit(0)

P27 RUNNER V4 ACTOR SOURCE END A4C8E712

P27 RUNNER V4 WATCHDOG SOURCE BEGIN E6A1954C
import array
import ctypes
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import socket
import stat
import struct
import sys
import time

PROBES=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"CONSUME_EDGE_UNKNOWN",b"ATTEMPT_COLLISION",b"ATTEMPT_NAMESPACE_UNKNOWN",b"ATTEMPT_DIRFD_UNKNOWN",b"ATTEMPT_BASE_DURABILITY_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"CONTROL_MALFORMED",b"CONTROL_TIMEOUT",b"CONTROL_TRUNCATION",b"FD_TRANSFER",b"STOP_WAIT_UNKNOWN",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_TICKET_DURABILITY_UNKNOWN",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_IO",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"DIRECT_WAIT_UNKNOWN",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_STRUCTURE",b"TRANSCRIPT_SEMANTICS",b"VALIDATED_DURABILITY_UNKNOWN",b"ACK_DURABILITY_UNKNOWN",b"CONTAINMENT_OBSERVATION_UNKNOWN",b"CONTAINMENT_NOT_EMPTY",b"RECOVERY_DURABILITY_UNKNOWN",b"RETAINED_DURABILITY_UNKNOWN",b"REPORT_CANDIDATE_DURABILITY_UNKNOWN",b"TERMINAL_SEEN_DURABILITY_UNKNOWN",b"REPORT_DURABILITY_UNKNOWN",b"ACK_EFFECT_UNKNOWN",b"RECONCILIATION_UNKNOWN",b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED",b"INTERNAL_INVARIANT")
KNOWN_FAIL={b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_STRUCTURE",b"TRANSCRIPT_SEMANTICS"}
INDETERMINATE=set(FAULT_ORDER)-KNOWN_FAIL
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
PYTHON=b"/root/miniconda3/bin/python3"
PYIMAGE=b"/root/miniconda3/bin/python3.12"
SNAPSHOT_EXPECT=(2303269,23672,b"0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92")
SNAPSHOT_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V2_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V3_AUTHOR_OPEN_NO_EXECUTION"
SNAPSHOT_TERMINAL_HEX=SNAPSHOT_TERMINAL.hex().encode("ascii")
V15_SHA=b"a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845"
V8_SHA=b"72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf"
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
MAX_U63=(1<<63)-1
MAX_FILE=16777216
STREAM_CAP=3145728
TOTAL_NS=18164800000
HOST_NS=17664800000
CLEANUP_NS=2000000000
ACK_NS=500000000
REPORT_NS=1000000000
RECORD_NS=100000000
CONSUMPTION_NS=100000000
PASS_COMMIT_NS=100000000
PASS_MARGIN_NS=10000000
TERMINAL_NS=500000000
A_RECEIPT_NS=100000000
B_CLOSURE_NS=500000000
FINAL_TOTAL_NS=1410000000
ACTOR_DISABLE_NS=500000000
STAGE_NS=10000000000
CERT_LIFE_NS=360000000000
ENTRY_REMAIN_NS=295482000000
CONSUME_REMAIN_NS=285482000000
PRE_STAGE_REMAIN_NS=285382000000
POST_STAGE_REMAIN_NS=275382000000
POST_CONTAIN_REMAIN_NS=274882000000
KILL_RETURN_NS=5000000
MAX_RIGHTS=4
UINT_MAX=(1<<32)-1
DURABLE_VERIFIED=b"DURABLE_VERIFIED"
O_DIR=os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW
AUTH=b""
CERT={}
DEPS=()
CONTROL_SEND_SEQ=0
CONTROL_RECV_SEQ=0
ENVELOPE_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX")
CERT_KEYS=(b"ISSUER_ID",b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"HISTORICAL_SNAPSHOT_SEALED",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"CGROUP_CHILD_MODE",b"CGROUP_CHILD_UID",b"CGROUP_CHILD_GID",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"ATTEMPT_DIRFD_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"FINAL_PASS_COMMIT_PROGRESS_NS",b"FINAL_PASS_MARGIN_NS",b"TERMINAL_HANDSHAKE_PROGRESS_NS",b"A_RECEIPT_PROGRESS_NS",b"B_CLOSURE_PROGRESS_NS",b"FINAL_TERMINAL_TOTAL_NS",b"ENTRY_MIN_REMAINING_NS",b"CONSUMPTION_MIN_REMAINING_NS",b"PRE_STAGE_MIN_REMAINING_NS",b"POST_STAGE_MIN_REMAINING_NS",b"POST_CONTAIN_MIN_REMAINING_NS",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DELETED_CGROUP_FD_GATE_ID",b"DELETED_CGROUP_FD_GATE_PASS",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS",b"EXTERNAL_SURVIVAL_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_PASS",b"OUTER_RECONCILER_GATE_ID",b"OUTER_RECONCILER_GATE_PASS",b"DEP_COUNT")

class Closed(Exception):
 pass

class ActorLost(Exception):
 pass

class CertificateExpired(Closed):
 pass

class FaultSet(Closed):
 def __init__(self,faults):
  self.faults=set(faults)
  super().__init__("fault-set")

class RemoteAbort(FaultSet):
 pass

def need(value):
 if not value:raise Closed("closed")

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw);return value

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(x in b"0123456789abcdef" for x in raw));return raw

def even_hex(raw,cap=MAX_FILE):
 need(type(raw)is bytes and len(raw)%2==0 and len(raw)<=2*cap)
 need(all(x in b"0123456789abcdef" for x in raw))
 result=bytes.fromhex(raw.decode("ascii"));need(result.hex().encode()==raw);return result

def octal(raw):
 need(raw and all(x in b"01234567" for x in raw));value=int(raw,8);need(format(value,"o").encode()==raw);return value

def sha(raw):
 return hashlib.sha256(raw).hexdigest().encode("ascii")

def read_all(number,cap=16777216):
 os.lseek(number,0,os.SEEK_SET);parts=[];total=0
 while True:
  chunk=os.read(number,min(1048576,cap-total+1))
  if not chunk:break
  total+=len(chunk);need(total<=cap);parts.append(chunk)
 return b"".join(parts)

def ascii_file(raw,cap=16777216):
 need(type(raw)is bytes and 0<len(raw)<=cap and raw.endswith(b"\n"))
 need(all(x==10 or 32<=x<=126 for x in raw));return raw

def seals(number):
 need(fcntl.fcntl(number,fcntl.F_GET_SEALS)==EXACT_SEALS)

def fd_access(number,mode):
 need(fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE==mode)

def packet(kind,pairs):
 global CONTROL_SEND_SEQ
 need(kind.startswith(b"V4_") and b"|" not in kind and b"\n" not in kind)
 provided={}
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value and key not in provided)
  provided[key]=value
 state=provided.get(b"state",kind[3:]);ordinal=provided.get(b"ordinal",b"NONE");probe=provided.get(b"probe",b"NONE")
 CONTROL_SEND_SEQ+=1
 body=kind+b"|version=4|auth_id="+AUTH+b"|sequence="+str(CONTROL_SEND_SEQ).encode()+b"|sender="+b"B"+b"|current_state="+state+b"|current_ordinal="+ordinal+b"|current_probe="+probe
 for key,value in pairs:body+=b"|"+key+b"="+value
 return body+b"\n"

def parse_packet(raw,kind,keys):
 global CONTROL_RECV_SEQ
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|");common_keys=(b"version",b"auth_id",b"sequence",b"sender",b"current_state",b"current_ordinal",b"current_probe")
 need(fields[0]==kind and len(fields)==len(keys)+1+len(common_keys))
 common={}
 for key,item in zip(common_keys,fields[1:1+len(common_keys)]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in common);common[key]=parts[1]
 result={}
 for key,item in zip(keys,fields[1+len(common_keys):]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result and parts[1]);result[key]=parts[1]
 need(common[b"version"]==b"4" and common[b"auth_id"]==AUTH and common[b"sender"]==b"A")
 sequence=udec(common[b"sequence"],1);need(sequence==CONTROL_RECV_SEQ+1)
 need(common[b"current_state"]==result.get(b"state",kind[3:]))
 need(common[b"current_ordinal"]==result.get(b"ordinal",b"NONE"))
 need(common[b"current_probe"]==result.get(b"probe",b"NONE"))
 CONTROL_RECV_SEQ=sequence
 return result

def parse_fixed(raw,header,keys,end):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(len(lines)==len(keys)+2 and lines[0]==header and lines[-1]==end);result={}
 for key,line in zip(keys,lines[1:-1]):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result);result[key]=parts[1]
 return result

def fault_csv(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults);need(len(ordered)==len(faults))
 return b"NONE" if not ordered else b",".join(ordered)

def parse_fault_csv(raw,allow_none):
 if raw==b"NONE":need(allow_none);return set()
 parts=raw.split(b",");need(parts and all(x in FAULT_ORDER for x in parts))
 need(len(parts)==len(set(parts)) and tuple(x for x in FAULT_ORDER if x in set(parts))==tuple(parts))
 return set(parts)

def parse_abort(raw,want_sender=b"A"):
 keys=(b"sender",b"state",b"ordinal",b"probe",b"effect_state",b"stage_present",b"release_disabled",b"terminal_deadline_ns",b"fault_set")
 values=parse_packet(raw,b"V4_ABORT",keys)
 need(values[b"sender"]==want_sender and values[b"state"] and values[b"ordinal"] and values[b"probe"])
 effects=(b"PREBEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"ARM_SEND_EFFECT_UNKNOWN",b"COMMIT_SEND_EFFECT_UNKNOWN",b"CONSUMED",b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED")
 need(values[b"effect_state"] in effects and values[b"stage_present"] in (b"0",b"1") and values[b"release_disabled"] in (b"0",b"1"))
 if want_sender==b"A":need(values[b"release_disabled"]==b"1")
 if want_sender==b"B" and values[b"state"]==b"CLEANUP_RELEASE_DISABLE":need(values[b"release_disabled"]==b"0")
 deadline=udec(values[b"terminal_deadline_ns"])
 if values[b"effect_state"] in (b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED"):need(deadline>0)
 faults=parse_fault_csv(values[b"fault_set"],False);return values,faults

def envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V4",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V4",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":V15_SHA,b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"EXTERNALLY_VERIFIED_ED25519"}
 for key,value in exact.items():need(values[key]==value)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig))
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"])
 need(before<after)
 return values

def contract(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V4" and lines[-1]==b"CERTIFICATE_END=1")
 fixed=lines[1:1+len(CERT_KEYS)];need(len(fixed)==len(CERT_KEYS));values={}
 for key,line in zip(CERT_KEYS,fixed):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in values);values[key]=parts[1]
 count=udec(values[b"DEP_COUNT"],1,256);dep_lines=lines[1+len(CERT_KEYS):-1];need(len(dep_lines)==count)
 roles={b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC",b"PYTHON_STDLIB",b"PYTHON_EXTENSION",b"NSS_DEPENDENCY",b"RUNTIME_DEPENDENCY"}
 deps=[]
 for index,line in enumerate(dep_lines):
  prefix=b"DEP[%04d]="%index;need(line.startswith(prefix));fields=line[len(prefix):].split(b",")
  need(len(fields)==10 and fields[0] in roles);path=even_hex(fields[1]);need(path.startswith(b"/") and b"\x00" not in path)
  ident=(udec(fields[2],1),udec(fields[3],1),octal(fields[4]),udec(fields[5],1),udec(fields[6]),udec(fields[7]),udec(fields[8]),h64(fields[9]))
  deps.append((fields[0],path,ident))
 need(len(set((x[0],x[1]) for x in deps))==len(deps))
 for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC"):need(sum(x[0]==role for x in deps)==1)
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V4",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":V15_SHA,b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"KEEPER_BYTES":b"4216",b"KEEPER_LF":b"128",b"KEEPER_SHA256":b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716",b"LAUNCHER_BYTES":b"4218",b"LAUNCHER_LF":b"128",b"LAUNCHER_SHA256":b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5",b"MARKER_BYTES":b"75094",b"MARKER_LF":b"1479",b"MARKER_SHA256":b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d",b"CHILD_BYTES":b"19746",b"CHILD_LF":b"452",b"CHILD_SHA256":b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"100000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"A_RECEIPT_PROGRESS_NS":b"100000000",b"B_CLOSURE_PROGRESS_NS":b"500000000",b"FINAL_TERMINAL_TOTAL_NS":b"1410000000",b"ENTRY_MIN_REMAINING_NS":b"295482000000",b"CONSUMPTION_MIN_REMAINING_NS":b"285482000000",b"PRE_STAGE_MIN_REMAINING_NS":b"285382000000",b"POST_STAGE_MIN_REMAINING_NS":b"275382000000",b"POST_CONTAIN_MIN_REMAINING_NS":b"274882000000",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS":b"500000000",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS":b"1",b"EXTERNAL_SURVIVAL_GATE_PASS":b"1",b"OUTER_RECONCILER_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value)
 for key in (b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_MOUNTINFO_SHA256",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"SAFE_BIND_MOUNTINFO_SHA256",b"KEEPER_SHA256",b"LAUNCHER_SHA256",b"MARKER_SHA256",b"CHILD_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"CLONE3_CPYTHON_GATE_ID",b"DELETED_CGROUP_FD_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_ID",b"OUTER_RECONCILER_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64 and values[b"DELETED_CGROUP_FD_GATE_ID"]!=b"0"*64 and values[b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID"]!=b"0"*64 and values[b"EXTERNAL_SURVIVAL_GATE_ID"]!=b"0"*64 and values[b"OUTER_RECONCILER_GATE_ID"]!=b"0"*64)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1")
 for key in (b"KERNEL_RELEASE_HEX",b"E0366_SNAPSHOT_TERMINAL_HEX",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"CGROUP_CHILD_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"LIBC_MODE"):octal(values[key])
 for key in (b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_MOUNT_ID",b"CGROUP2_MOUNT_ID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_NLINK",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_MOUNT_ID",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_NLINK",b"SAFE_BIND_MOUNT_ID",b"KEEPER_BYTES",b"KEEPER_LF",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"MARKER_BYTES",b"MARKER_LF",b"CHILD_BYTES",b"CHILD_LF",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT"):udec(values[key])
 by_role={role:next(x for x in deps if x[0]==role) for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC")}
 need(by_role[b"PYTHON_LINK"][1]==PYTHON and by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"ENV_EXEC"][1]==b"/usr/bin/env" and by_role[b"BASH_EXEC"][1]==b"/usr/bin/bash")
 libc=(udec(values[b"LIBC_DEV"],1),udec(values[b"LIBC_INO"],1),octal(values[b"LIBC_MODE"]),udec(values[b"LIBC_NLINK"],1),0,0,udec(values[b"LIBC_BYTES"],1),values[b"LIBC_SHA256"])
 need(by_role[b"LIBC"][1]==even_hex(values[b"LIBC_PATH_HEX"]) and by_role[b"LIBC"][2]==libc)
 return values,tuple(deps)

def checkpoint(cert,needed=0,deadline=None):
 m0=time.monotonic_ns();real=time.time_ns();m1=time.monotonic_ns()
 before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 if not (before<=real<expiry and expiry-real>=needed):raise CertificateExpired("certificate-life")
 base_r=udec(cert[b"REALTIME_BIND_NS"]);base_m=udec(cert[b"MONOTONIC_BIND_NS"]);need(base_m<=m0<=m1)
 drift=udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"]);low=base_r+(m0-base_m);high=base_r+(m1-base_m)
 need(low-drift<=real<=high+drift)
 if deadline is not None:need(m1<=deadline)
 return real,m1


def horizon_needed(deadline,tail):
 return tail+max(0,deadline-time.monotonic_ns())

def cert_live(cert,needed=0):
 return checkpoint(cert,needed)

def cap_status():
 number=-1
 try:
  number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,65536),65536)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 values={}
 for line in raw.splitlines():
  for key in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs"):
   if line.startswith(key+b":"):need(key not in values);values[key]=line.split(b":",1)[1].strip()
 need(set(values)=={b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs"});return values

def limit_vector():
 inf=resource.RLIM_INFINITY
 return ((resource.RLIMIT_AS,(inf,inf)),(resource.RLIMIT_CORE,(0,0)),(resource.RLIMIT_CPU,(inf,inf)),(resource.RLIMIT_DATA,(inf,inf)),(resource.RLIMIT_FSIZE,(inf,inf)),(resource.RLIMIT_MEMLOCK,(8388608,8388608)),(resource.RLIMIT_MSGQUEUE,(819200,819200)),(resource.RLIMIT_NICE,(0,0)),(resource.RLIMIT_NOFILE,(1048576,1048576)),(resource.RLIMIT_NPROC,(1048576,1048576)),(resource.RLIMIT_RSS,(inf,inf)),(resource.RLIMIT_RTPRIO,(0,0)),(resource.RLIMIT_RTTIME,(inf,inf)),(resource.RLIMIT_SIGPENDING,(515199,515199)),(resource.RLIMIT_STACK,(8388608,inf)))

def final_context(safe_dev,safe_ino):
 values=cap_status();zero=b"0000000000000000"
 need(os.getresuid()==(0,0,0) and os.getresgid()==(0,0,0) and os.getgroups()==[])
 need(all(values[x]==zero for x in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb")) and values[b"NoNewPrivs"]==b"1")
 libc=ctypes.CDLL(None,use_errno=True);need(libc.prctl(27,0,0,0,0)==15)
 held=os.stat(b".",follow_symlinks=False);need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
 need(os.umask(0o077)==0o077 and all(signal.getitimer(x)==(0.0,0.0) for x in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF)))
 need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set() and all(signal.getsignal(x)==signal.SIG_DFL for x in signal.valid_signals() if x not in (signal.SIGKILL,signal.SIGSTOP)))
 for key,value in limit_vector():need(resource.getrlimit(key)==value)
 need(sys.gettrace() is None and sys.getprofile() is None and os.environb==ENV)

def scrub_exact(expected):
 seen=set()
 for item in os.listdir(b"/proc/self/fd"):
  if item.isdigit():
   number=int(item)
   try:os.fstat(number)
   except OSError as error:need(error.errno==errno.EBADF);continue
   seen.add(number)
 need(seen==expected)

def pidfd_pid(number):
 link=os.readlink(b"/proc/self/fd/"+str(number).encode());need(link==b"anon_inode:[pidfd]");info=-1
 try:
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[5:] for x in raw.splitlines() if x.startswith(b"Pid:\t")];need(len(values)==1)
 return udec(values[0],1)

def closed(number):
 try:os.fstat(number)
 except OSError as error:need(error.errno==errno.EBADF);return
 need(False)

def whole_snapshot():
 seals(9);fd_access(9,os.O_RDWR);raw=read_all(9,SNAPSHOT_EXPECT[0]);held=os.fstat(9)
 need(stat.S_ISREG(held.st_mode) and held.st_nlink==0 and held.st_uid==held.st_gid==0)
 need((held.st_size,raw.count(b"\n"),sha(raw))==SNAPSHOT_EXPECT and raw.endswith(b"\n"))
 lines=raw[:-1].split(b"\n");need(lines[-1]==SNAPSHOT_TERMINAL and lines.count(SNAPSHOT_TERMINAL)==1)
 return raw

class StatFS(ctypes.Structure):
 _fields_=(("f_type",ctypes.c_long),("f_bsize",ctypes.c_long),("rest",ctypes.c_byte*240))

def statfs_magic(number):
 cell=StatFS();libc=ctypes.CDLL(None,use_errno=True);need(libc.fstatfs(number,ctypes.byref(cell))==0)
 return cell.f_type&0xffffffff

def mount_binding(number):
 info=-1
 try:
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 mids=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")];need(len(mids)==1);mid=udec(mids[0],1);table=-1
 try:
  table=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);rows=ascii_file(read_all(table,1048576),1048576)
 finally:close_numbers(tuple(x for x in (table,) if x>=0))
 matches=[line+b"\n" for line in rows.splitlines() if line.split(b" ",1)[0]==str(mid).encode()]
 need(len(matches)==1);return mid,matches[0]

def base_check(number,cert,prefix):
 held=os.fstat(number);need(stat.S_ISDIR(held.st_mode));fd_access(number,os.O_RDONLY)
 expected=(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),octal(cert[prefix+b"_MODE"]),udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"]))
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==expected)
 return held

def verify_dependency(entry):
 role,path,identity=entry;parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts))
 rootfd=current=number=following=-1
 try:
  rootfd=os.open(b"/",O_DIR);current=os.dup(rootfd)
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode))
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
   held=os.fstat(number);body=read_all(number,identity[6]);size=len(body);digest=sha(body)
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,size,digest)==identity)
 finally:
  close_numbers(tuple(x for x in (number,following,current,rootfd) if x>=0))

def write_all(number,raw,context,deadline,require_live,needed):
 offset=0
 while offset<len(raw):
  record_boundary(context,deadline,require_live,needed)
  try:count=os.write(number,raw[offset:])
  except InterruptedError:
   record_boundary(context,deadline,require_live,needed);continue
  record_boundary(context,deadline,require_live,needed);need(count>0);offset+=count

def post_deadline(deadline):
 if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})

def record_boundary(context,deadline,require_live,needed):
 post_deadline(deadline)
 try:checkpoint(CERT,needed,deadline)
 except CertificateExpired:
  context[b"faults"].add(b"CERTIFICATE_EXPIRED")
  if require_live:raise
 except Closed:
  context[b"faults"].add(b"CERTIFICATE_INVALID")
  if require_live:raise

def durable_once(context,name,raw,deadline,require_live=True,needed_after=0):
 digest=sha(raw)
 if name in context[b"durability"]:
  if context[b"durability_digest"].get(name)!=digest:raise FaultSet({b"INTERNAL_INVARIANT"})
  return context[b"durability"][name],digest
 state=b"ABSENT_KNOWN";context[b"durability"][name]=state;context[b"durability_digest"][name]=digest;context[b"durability_faults"][name]=set();number=-1
 try:
  record_boundary(context,deadline,require_live,needed_after)
  state=b"OPEN_EFFECT_UNKNOWN";context[b"durability"][name]=state
  number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=context[b"attempt"])
  record_boundary(context,deadline,require_live,needed_after);state=b"FD_HELD";context[b"durability"][name]=state
  state=b"WRITE_EFFECT_UNKNOWN";context[b"durability"][name]=state
  write_all(number,raw,context,deadline,require_live,needed_after)
  state=b"FILE_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  record_boundary(context,deadline,require_live,needed_after);os.fsync(number);record_boundary(context,deadline,require_live,needed_after)
  held=os.fstat(number);record_boundary(context,deadline,require_live,needed_after)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw))
  need(read_all(number,len(raw))==raw);record_boundary(context,deadline,require_live,needed_after)
  state=b"SAME_FD_REREAD_VERIFIED";context[b"durability"][name]=state
  state=b"DIR_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  record_boundary(context,deadline,require_live,needed_after);os.fsync(context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
  state=DURABLE_VERIFIED;context[b"durability"][name]=state
 except CertificateExpired:
  context[b"faults"].add(b"CERTIFICATE_EXPIRED");context[b"durability_faults"][name].add(b"CERTIFICATE_EXPIRED");context[b"durability"][name]=state
 except FaultSet as error:
  context[b"faults"].update(error.faults);context[b"durability_faults"][name].update(error.faults);context[b"durability"][name]=state
 except Closed:
  context[b"faults"].add(b"CERTIFICATE_INVALID");context[b"durability_faults"][name].add(b"CERTIFICATE_INVALID");context[b"durability"][name]=state
 except BaseException:
  context[b"faults"].add(b"INTERNAL_INVARIANT");context[b"durability_faults"][name].add(b"INTERNAL_INVARIANT");context[b"durability"][name]=state
 finally:
  if number>=0:
   try:os.close(number)
   except OSError:pass
 return context[b"durability"][name],digest

def primary(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults);need(faults and len(ordered)==len(faults))
 return ordered[0]

def disposition(faults):
 need(faults)
 return b"CONSUMED_INDETERMINATE" if any(x in INDETERMINATE for x in faults) else b"CONSUMED_FAIL"

def close_numbers(numbers):
 for number in numbers:
  try:os.close(number)
  except OSError:pass

def next_record(context):
 context[b"record_seq"]+=1
 return str(context[b"record_seq"]).encode()

def attempt_intent(auth,cert,cert_raw,envelope_raw,source_raw):
 return (b"P27E001_ATTEMPT_INTENT_V4\nAUTH_ID="+auth+b"\nNONCE="+auth+b"\nRECORD_SEQ=1\nPREDECESSOR_SHA256=NONE\nISSUER_ENVELOPE_SHA256="+sha(envelope_raw)+b"\nCERTIFICATE_SHA256="+sha(cert_raw)+b"\nPLAN_SHA256="+cert[b"PLAN_SHA256"]+b"\nRUNNER_SHA256="+cert[b"RUNNER_SHA256"]+b"\nRECOVERY_SHA256="+sha(source_raw)+b"\nE0366_SNAPSHOT_BYTES=2303269\nE0366_SNAPSHOT_LF=23672\nE0366_SNAPSHOT_SHA256="+SNAPSHOT_EXPECT[2]+b"\nE0366_SNAPSHOT_TERMINAL_HEX="+SNAPSHOT_TERMINAL_HEX+b"\nV15_SHA256="+cert[b"V15_SHA256"]+b"\nSUITE="+b",".join(PROBES)+b"\nATTEMPT_PATH_HEX="+(b"/var/lib/p27-e001-host-v15/attempts/"+auth).hex().encode()+b"\nSTAGE_PATH_HEX="+(b"/tmp/p27-e001-host-v15/"+auth).hex().encode()+b"\nCGROUP_PATH_HEX="+(b"/sys/fs/cgroup/p27-e001-host-v15/"+auth).hex().encode()+b"\nACTOR_ENTRY_CAPS=00000000000401c0\nPAYLOAD_FINAL_CAPS=0000000000000000\nABSOLUTE_EXPIRY_REALTIME_NS="+cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCONSUMED_OR_EFFECT_UNKNOWN=1\nRETRY_ALLOWED=0\nINTENT_END=1\n")

def verify_attempt_fd(number):
 held=os.fstat(number);fd_access(number,os.O_RDONLY);named=os.stat(AUTH,dir_fd=5,follow_symlinks=False)
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid))
 need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and stat.S_IMODE(held.st_mode)==0o700 and held.st_nlink==2)
 base_check(5,CERT,b"ATTEMPT_BASE");return held

def retain_attempt_dirfd(context):
 context[b"faults"].update((b"ATTEMPT_DIRFD_UNKNOWN",b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED"))
 context[b"consumption_state"]=b"DIRFD_HORIZON_CLOSED_NO_REOPEN"
 return False

def consume_attempt(context,cert_raw,envelope_raw,source_raw,deadline):
 context[b"consume_deadline"]=deadline;context[b"consumption_state"]=b"MKDIR_CALL_ENTERED"
 try:
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  os.mkdir(AUTH,0o700,dir_fd=5)
  post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
 except FileExistsError as error:
  context[b"consumption_state"]=b"COLLISION";context[b"collision"]=True;context[b"faults"].add(b"ATTEMPT_COLLISION")
  context[b"collision_identity"]=(0,0,0,0,0,0)
  try:os.close(5);context[b"attempt_base_closed_on_collision"]=True
  except BaseException:context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 except CertificateExpired:
  context[b"consumption_state"]=b"MKDIR_EFFECT_UNKNOWN";context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_NAMESPACE_UNKNOWN"))
  raise
 except BaseException as error:
  context[b"consumption_state"]=b"MKDIR_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_NAMESPACE_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 context[b"consumption_state"]=b"MKDIR_RETURNED_CREATED";context[b"local_fd_state"]=b"LOCAL_UNVERIFIED";number=-1
 try:
  context[b"consumption_state"]=b"IMMEDIATE_DIRFD_CALL_ENTERED"
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  number=os.open(AUTH,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
  post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  verify_attempt_fd(number);context[b"local_fd_state"]=b"LOCAL_VERIFIED";checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  context[b"attempt"]=number;number=-1;context[b"local_fd_state"]=b"PUBLISHED";context[b"consumption_state"]=b"DIRFD_PUBLISHED_VERIFIED"
 except CertificateExpired:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_DIRFD_UNKNOWN"))
  raise
 except BaseException as error:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 finally:
  if number>=0:
   try:os.close(number)
   except OSError:pass
 context[b"consumption_state"]=b"BASE_FSYNC_EFFECT_UNKNOWN"
 try:
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline);os.fsync(5);post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
 except CertificateExpired:
  context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_BASE_DURABILITY_UNKNOWN"));raise
 except BaseException as error:
  context[b"faults"].add(b"ATTEMPT_BASE_DURABILITY_UNKNOWN");raise FaultSet(set(context[b"faults"])) from error
 context[b"consumption_state"]=b"BASE_DURABLE"
 body=attempt_intent(AUTH,CERT,cert_raw,envelope_raw,source_raw)
 state,digest=durable_once(context,b"intent.v4",body,deadline,True,PRE_STAGE_REMAIN_NS)
 if state!=DURABLE_VERIFIED:
  context[b"faults"].add(b"INTENT_DURABILITY_UNKNOWN");raise FaultSet(set(context[b"faults"]))
 context[b"intent_durable"]=True;context[b"chain_sha"]=digest;context[b"record_seq"]=1
 context[b"consumption_state"]=b"INTENT_DURABLE";return digest

def release_record(context,values):
 seq=next_record(context);predecessor=context[b"chain_sha"];origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_RELEASE_STATE_V4\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nOUTER_PID="+values[b"outer_pid"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED=0\nSTOPPED_RAW_STATUS="+values[b"stopped_raw_status"]+b"\nCGROUP_MEMBER="+values[b"cgroup_member"]+b"\nCGROUP_DEV="+values[b"cgroup_dev"]+b"\nCGROUP_INO="+values[b"cgroup_ino"]+b"\nCGROUP_MODE="+values[b"cgroup_mode"]+b"\nCGROUP_NLINK="+values[b"cgroup_nlink"]+b"\nCGROUP_UID="+values[b"cgroup_uid"]+b"\nCGROUP_GID="+values[b"cgroup_gid"]+b"\nARGV_SHA256="+values[b"argv_sha256"]+b"\nENV_SHA256="+values[b"env_sha256"]+b"\nRELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nLAUNCH_DEADLINE_NS="+values[b"launch_deadline_ns"]+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nSTATE=RELEASE_AUTHORIZED\nRELEASE_END=1\n")
 state,digest=durable_once(context,b"release-"+values[b"probe"]+b".v4",body,deadline,True)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"RELEASE_RECORD_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"release_sha"]=digest;return digest

CANDIDATE_KEYS=(b"ordinal",b"probe",b"release_record_sha256",b"release_origin_ns",b"release_return_ns",b"host_complete_ns",b"capture_done_ns",b"direct_wait_state",b"outer_raw_status",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_overflow",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_overflow",b"cgroup_empty",b"parser_language",b"parser_structure",b"parser_semantics",b"candidate",b"terminal",b"certificate_expiry_realtime_ns")
FINAL_REPORT_KEYS=(b"AUTH_ID",b"SUITE",b"ENTERED_COUNT",b"COMMITTED_COUNT",b"STAGE_PRESENT",b"CONTAINMENT_BOUND",b"STOPPED_COUNT",b"STOP_PROBE",b"PRIMARY",b"FAULT_SET",b"CHAIN_HEAD_SHA256",b"TERMINAL_SEEN_SHA256",b"ACK_STATE",b"RECONCILIATION_TOKEN",b"COMMON_TERMINAL_DEADLINE_NS",b"DIRECT_REAP",b"CGROUP_EMPTY",b"CGROUP_REMOVED",b"KILL_CALL_COUNT",b"KILL_STATE",b"CERTIFICATE_LIVE_AT_COMMIT",b"PASS_COMMIT_ORIGIN_MONOTONIC_NS",b"PASS_COMMIT_DEADLINE_MONOTONIC_NS",b"FINAL_PASS_MARGIN_NS",b"STAGE_RETAINED",b"ATTEMPT_RETAINED",b"RETRY_ALLOWED",b"DISPOSITION")

def forensic_body(values):
 return (b"RELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nRELEASE_RETURN_NS="+values[b"release_return_ns"]+b"\nHOST_COMPLETE_NS="+values[b"host_complete_ns"]+b"\nCAPTURE_DONE_NS="+values[b"capture_done_ns"]+b"\nDIRECT_WAIT="+values[b"direct_wait_state"]+b"\nOUTER_RAW_STATUS="+values[b"outer_raw_status"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED="+values[b"pidfd_exit_ready_observed"]+b"\nSTDOUT_BYTES="+values[b"stdout_len"]+b"\nSTDOUT_SHA256="+values[b"stdout_sha256"]+b"\nSTDOUT_EOF="+values[b"stdout_eof"]+b"\nSTDOUT_OVERFLOW="+values[b"stdout_overflow"]+b"\nSTDERR_BYTES="+values[b"stderr_len"]+b"\nSTDERR_SHA256="+values[b"stderr_sha256"]+b"\nSTDERR_EOF="+values[b"stderr_eof"]+b"\nSTDERR_OVERFLOW="+values[b"stderr_overflow"]+b"\nCGROUP_EMPTY="+values[b"cgroup_empty"]+b"\nPARSER_LANGUAGE="+values[b"parser_language"]+b"\nPARSER_STRUCTURE="+values[b"parser_structure"]+b"\nPARSER_SEMANTICS="+values[b"parser_semantics"]+b"\nCANDIDATE="+values[b"candidate"]+b"\nTERMINAL="+values[b"terminal"]+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+values[b"certificate_expiry_realtime_ns"]+b"\nTOPOLOGY=V15_INTERNAL_VALIDATION_REPORTED_BY_COMPLETE_TRANSCRIPT\nEXTERNAL_TOPOLOGY_RECONSTRUCTION=UNAVAILABLE\n")

def validated_record(context,values,ack_deadline):
 seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V4\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nSTATE=VALIDATED_CANDIDATE\n"+forensic_body(values)+b"B_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+values[b"probe"]+b"-validated.v4",body,deadline,True)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"VALIDATED_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"validated_sha"]=digest;context[b"validated_values"]=dict(values);return digest

def ack_intent_record(context,ordinal,probe,actor_ack,received,ack_deadline):
 values=context[b"validated_values"];seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V4\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=ACK_COMMIT_INTENT\n"+forensic_body(values)+b"ACTOR_ACK_INTENT_NS="+str(actor_ack).encode()+b"\nB_ACK_RECEIVED_NS="+str(received).encode()+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-ack-intent.v4",body,deadline,True)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"ACK_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;return digest

def populated(number):
 os.lseek(number,0,os.SEEK_SET);raw=os.read(number,4096)
 values=[x for x in raw.splitlines() if x.startswith(b"populated ")]
 need(len(values)==1 and values[0] in (b"populated 0",b"populated 1"));return values[0]==b"populated 1"

def observe_population(context):
 number=context.get(b"events_fd",-1)
 if number<0:number=context.get(b"root_events_fd",-1)
 if number<0:return False
 try:return populated(number)
 except BaseException:
  context[b"faults"].add(b"CONTAINMENT_OBSERVATION_UNKNOWN");return None

def drain(number,target):
 overflow=False;eof=False
 while True:
  try:chunk=os.read(number,65536)
  except BlockingIOError:break
  except InterruptedError:continue
  except BaseException as error:raise FaultSet({b"CAPTURE_IO"}) from error
  if chunk==b"":eof=True;break
  room=STREAM_CAP-len(target)
  if room>0:target.extend(chunk[:room])
  if len(chunk)>room:overflow=True
 return overflow,eof

def recv_monitored(control,actor_pidfd,deadline,rights):
 checkpoint(CERT,0,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(actor_pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  cmask=0;amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   if number==actor_pidfd:amask|=event
  if cmask&select.POLLIN:
   installed=[];bad=False
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize))
    for level,kind,data in ancillary:
     if level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS:
      cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
      if whole:cells.frombytes(data[:whole]);installed.extend(cells)
      if whole!=len(data):bad=True
     else:bad=True
    checkpoint(CERT,0,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if address is not None or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    if bad:raise FaultSet({b"FD_TRANSFER"})
    if raw.startswith(b"V4_ABORT|"):
     values,faults=parse_abort(raw)
     if installed or ancillary:faults.add(b"FD_TRANSFER")
     error=RemoteAbort(faults);error.values=values;raise error
    if rights==0:
     if installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    else:
     if len(ancillary)!=1 or len(installed)!=rights:raise FaultSet({b"FD_TRANSFER"})
    return raw,tuple(installed)
   except BlockingIOError:
    close_numbers(installed);continue
   except BaseException:
    close_numbers(installed);raise
  if amask:raise ActorLost("actor")
  if cmask&(select.POLLHUP|select.POLLERR):raise ActorLost("control")

def wait_sendable(control,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR);poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  cmask=amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==4:amask|=event
  if amask:raise ActorLost("actor")
  if cmask&select.POLLOUT:return
  if cmask&(select.POLLHUP|select.POLLERR):raise ActorLost("control")

def send_exact(control,raw,deadline):
 while True:
  wait_sendable(control,deadline)
  try:count=control.send(raw)
  except BlockingIOError:continue
  except BaseException as error:raise ActorLost("send") from error
  if count!=len(raw):raise FaultSet({b"CONTROL_MALFORMED"})
  checkpoint(CERT,0,deadline)
  if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
  return

def kill_once(context,reason):
 if context[b"kill_state"]!=b"NOT_RESERVED":return
 inherited=context[b"cleanup_deadline"];now=time.monotonic_ns()
 if inherited is None or now+RECORD_NS+KILL_RETURN_NS>inherited:
  context[b"kill_state"]=b"TRANSFER_REQUIRED";context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED");return
 context[b"kill_state"]=b"TICKET_COMMITTING"
 ticket=(b"P27E001_KILL_TICKET_V4\nAUTH_ID="+AUTH+b"\nPRIMARY="+reason+b"\nCLEANUP_DEADLINE_NS="+str(inherited).encode()+b"\nKILL_CALL_COUNT_BEFORE=0\nWRITE_BYTES_HEX=310a\nRETRY_ALLOWED=0\nTICKET_END=1\n")
 ticket_deadline=min(inherited,time.monotonic_ns()+RECORD_NS)
 state,digest=durable_once(context,b"kill-ticket.v4",ticket,ticket_deadline,False)
 context[b"kill_ticket_state"]=state
 if state!=DURABLE_VERIFIED:context[b"faults"].add(b"KILL_TICKET_DURABILITY_UNKNOWN")
 context[b"kill_state"]=b"CALL_RESERVED";number=context.get(b"kill_fd",-1)
 if number<0:number=context.get(b"root_kill_fd",-1)
 if number<0:
  context[b"kill_state"]=b"CALL_UNAVAILABLE";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 now=time.monotonic_ns()
 if now+KILL_RETURN_NS>inherited:
  context[b"kill_state"]=b"TRANSFER_REQUIRED";context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED");return
 context[b"kill_call_count"]=1;context[b"kill_state"]=b"CALL_ENTERED";call_deadline=min(inherited,now+KILL_RETURN_NS)
 try:
  record_boundary(context,call_deadline,False,0);returned=os.write(number,b"1\n");record_boundary(context,call_deadline,False,0)
 except BaseException:
  context[b"kill_state"]=b"RETURN_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 if returned!=2:
  context[b"kill_state"]=b"SHORT_OR_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN")
 else:context[b"kill_state"]=b"RETURNED_2"
 while time.monotonic_ns()<inherited:
  state=observe_population(context);context[b"last_population"]=state
  if state is False:
   context[b"kill_state"]=b"RETURNED_2_EMPTY_CONFIRMED" if returned==2 else context[b"kill_state"];return
  owner_poll(None,context,inherited)
 context[b"faults"].add(b"CONTAINMENT_OBSERVATION_UNKNOWN")
 if context[b"kill_state"]==b"RETURNED_2":context[b"kill_state"]=b"RETURNED_2_POSTCHECK_UNKNOWN"

def begin_cleanup(context):
 if context[b"cleanup_origin"] is None:
  context[b"cleanup_origin"]=time.monotonic_ns()
  inherited=context.get(b"terminal_deadline",0)
  context[b"cleanup_deadline"]=inherited if inherited else context[b"cleanup_origin"]+CLEANUP_NS
 state=observe_population(context);context[b"last_population"]=state
 if context[b"containment_bound"] and context[b"kill_state"]==b"NOT_RESERVED":
  kill_once(context,primary(context[b"faults"]))

def retained_record(context,stop):
 if context[b"attempt"]<0 or context[b"collision"]:return
 deadline=context[b"cleanup_deadline"]
 body=(b"P27E001_RETAINED_STATE_V4\nAUTH_ID="+AUTH+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nCLEANUP_ORIGIN_NS="+str(context[b"cleanup_origin"]).encode()+b"\nCLEANUP_DEADLINE_NS="+str(deadline).encode()+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nRETRY_ALLOWED=0\nRETAINED_END=1\n")
 state,digest=durable_once(context,b"retained.v4",body,deadline,False)
 context[b"retained_state"]=state
 if state!=DURABLE_VERIFIED:context[b"faults"].add(b"RETAINED_DURABILITY_UNKNOWN")

def owner_poll(control,context,until):
 poller=select.poll();poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 if control is not None:poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
 try:events=poller.poll(max(1,min(50,max(1,(until-time.monotonic_ns()+999999)//1000000))))
 except InterruptedError:return
 for number,event in events:
  if number==4:
   context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"ACTOR_LOST")
  elif control is not None and number==control.fileno():
   if event&select.POLLIN:
    try:
     raw,fds=recv_monitored(control,4,min(until,time.monotonic_ns()+ACK_NS),0);need(fds==())
     if raw.startswith(b"V4_ABORT|"):
      values,faults=parse_abort(raw,b"A");context[b"faults"].update(faults)
      context[b"release_disabled"]=values[b"release_disabled"]==b"1"
      context[b"stage_present"]=values[b"stage_present"]==b"1"
     else:context[b"faults"].add(b"CONTROL_MALFORMED")
    except RemoteAbort as error:
     context[b"faults"].update(error.faults);context[b"release_disabled"]=True
    except ActorLost:
     context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"ACTOR_LOST")
    except FaultSet as error:context[b"faults"].update(error.faults)
   elif event&(select.POLLHUP|select.POLLERR):
    context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"ACTOR_LOST")

def retained_until_empty(control,context,stop):
 retained_record(context,stop)
 while True:
  for key in (b"out_fd",b"err_fd"):
   number=context.get(key,-1)
   if number>=0:
    try:drain(number,bytearray())
    except FaultSet as error:context[b"faults"].update(error.faults)
  owner_poll(control,context,time.monotonic_ns()+50000000)
  state=observe_population(context);context[b"last_population"]=state
  if state is False:return
  if context[b"release_disabled"] and context[b"containment_bound"] and context[b"kill_state"]==b"NOT_RESERVED":
   kill_once(context,primary(context[b"faults"]))
  if state is True and context[b"kill_state"] in (b"TRANSFER_REQUIRED",b"CALL_UNAVAILABLE"):
   context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")

def direct_reap_value(context,actor_lost):
 if context[b"direct_reaps"]==context[b"entered"] and context[b"entered"]>0:return b"COMPLETE"
 if b"DIRECT_WAIT_UNKNOWN" in context[b"faults"]:return b"UNKNOWN"
 if actor_lost:return b"UNAVAILABLE_ACTOR_LOST"
 return b"UNKNOWN"

def recovery_record(context,stop,actor_lost):
 deadline=context[b"cleanup_deadline"];direct=direct_reap_value(context,actor_lost)
 body=(b"P27E001_RECOVERY_STATE_V4\nAUTH_ID="+AUTH+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nINTENT_DURABLE="+(b"1" if context[b"intent_durable"] else b"0")+b"\nCONSUMPTION_STATE="+context[b"consumption_state"]+b"\nSTAGE_PRESENT="+(b"1" if context[b"stage_present"] else b"0")+b"\nCONTAINMENT_BOUND="+(b"1" if context[b"containment_bound"] else b"0")+b"\nSTOPPED_COUNT="+str(context[b"stopped_count"]).encode()+b"\nDIRECT_REAP="+direct+b"\nSTDOUT_EOF="+(b"1" if context[b"last_out_eof"] else b"0")+b"\nSTDERR_EOF="+(b"1" if context[b"last_err_eof"] else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nKILL_TICKET_STATE="+context[b"kill_ticket_state"]+b"\nCGROUP_EMPTY=1\nCLEANUP_ORIGIN_NS="+str(context[b"cleanup_origin"]).encode()+b"\nCLEANUP_DEADLINE_NS="+str(deadline).encode()+b"\nRETRY_ALLOWED=0\nDISPOSITION="+disposition(context[b"faults"])+b"\nRECOVERY_END=1\n")
 name=b"recovery.v4" if context[b"intent_durable"] else b"preintent.v4"
 state,digest=durable_once(context,name,body,deadline,False)
 context[b"recovery_state"]=state
 if state==DURABLE_VERIFIED:context[b"chain_sha"]=digest
 else:context[b"faults"].add(b"RECOVERY_DURABILITY_UNKNOWN")
 return state,digest

def parse_final_report(raw):
 values=parse_fixed(raw,b"P27E001_FINAL_REPORT_V4",FINAL_REPORT_KEYS,b"REPORT_END=1")
 need(values[b"AUTH_ID"]==AUTH and values[b"SUITE"]==b",".join(PROBES))
 entered=udec(values[b"ENTERED_COUNT"],0,15);committed=udec(values[b"COMMITTED_COUNT"],0,15);stopped=udec(values[b"STOPPED_COUNT"],0,15)
 need(committed<=entered and stopped<=entered)
 need(values[b"STAGE_PRESENT"] in (b"0",b"1") and values[b"CONTAINMENT_BOUND"] in (b"0",b"1"))
 if entered:need(values[b"STAGE_PRESENT"]==values[b"CONTAINMENT_BOUND"]==b"1")
 h64(values[b"CHAIN_HEAD_SHA256"]);need(values[b"CGROUP_EMPTY"]==b"1" and values[b"CGROUP_REMOVED"] in (b"0",b"1"))
 need(values[b"FINAL_PASS_MARGIN_NS"]==str(PASS_MARGIN_NS).encode() and values[b"ATTEMPT_RETAINED"]==b"1" and values[b"RETRY_ALLOWED"]==b"0")
 kill_count=udec(values[b"KILL_CALL_COUNT"],0,1);kill_state=values[b"KILL_STATE"]
 if kill_count==0:need(kill_state in (b"NOT_RESERVED",b"TICKET_COMMITTING",b"CALL_RESERVED",b"CALL_UNAVAILABLE",b"TRANSFER_REQUIRED"))
 else:need(kill_state in (b"CALL_ENTERED",b"RETURN_UNKNOWN",b"SHORT_OR_UNKNOWN",b"RETURNED_2",b"RETURNED_2_EMPTY_CONFIRMED",b"RETURNED_2_POSTCHECK_UNKNOWN"))
 if values[b"DISPOSITION"]==b"PASS":
  need(entered==committed==stopped==15 and values[b"STAGE_PRESENT"]==values[b"CONTAINMENT_BOUND"]==b"1")
  need(values[b"STOP_PROBE"]==values[b"PRIMARY"]==values[b"FAULT_SET"]==b"NONE")
  h64(values[b"TERMINAL_SEEN_SHA256"]);h64(values[b"RECONCILIATION_TOKEN"])
  need(values[b"ACK_STATE"]==b"PASS_COMMITTED_RECONCILIATION_REQUIRED")
  udec(values[b"COMMON_TERMINAL_DEADLINE_NS"],1)
  need(values[b"DIRECT_REAP"]==b"COMPLETE" and values[b"CGROUP_REMOVED"]==b"1")
  need(kill_count==0 and kill_state==b"NOT_RESERVED" and values[b"CERTIFICATE_LIVE_AT_COMMIT"]==b"1")
  origin=udec(values[b"PASS_COMMIT_ORIGIN_MONOTONIC_NS"],1);deadline=udec(values[b"PASS_COMMIT_DEADLINE_MONOTONIC_NS"],1)
  need(deadline==origin+PASS_COMMIT_NS and values[b"STAGE_RETAINED"]==b"1");return values
 faults=parse_fault_csv(values[b"FAULT_SET"],False);need(values[b"PRIMARY"]==primary(faults) and values[b"DISPOSITION"]==disposition(faults))
 need(values[b"STOP_PROBE"]==b"NONE" or values[b"STOP_PROBE"] in PROBES)
 need(values[b"TERMINAL_SEEN_SHA256"]==b"NONE" and values[b"ACK_STATE"]==b"FAILURE_DURABLE_AWAITING_ACK" and values[b"RECONCILIATION_TOKEN"]==b"NONE")
 need(udec(values[b"COMMON_TERMINAL_DEADLINE_NS"],1)>0)
 need(values[b"DIRECT_REAP"] in (b"COMPLETE",b"UNKNOWN",b"UNAVAILABLE_ACTOR_LOST"))
 need(values[b"CERTIFICATE_LIVE_AT_COMMIT"]==b"0" and values[b"PASS_COMMIT_ORIGIN_MONOTONIC_NS"]==values[b"PASS_COMMIT_DEADLINE_MONOTONIC_NS"]==b"0")
 need(values[b"STAGE_RETAINED"]==values[b"STAGE_PRESENT"])
 need(values[b"DISPOSITION"] in (b"CONSUMED_FAIL",b"CONSUMED_INDETERMINATE"));return values

def failure_report(context,stop,actor_lost):
 deadline=context[b"cleanup_deadline"];direct=direct_reap_value(context,actor_lost);disp=disposition(context[b"faults"])
 body=(b"P27E001_FINAL_REPORT_V4\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT="+str(context[b"entered"]).encode()+b"\nCOMMITTED_COUNT="+str(sum(context[b"committed"])).encode()+b"\nSTAGE_PRESENT="+(b"1" if context[b"stage_present"] else b"0")+b"\nCONTAINMENT_BOUND="+(b"1" if context[b"containment_bound"] else b"0")+b"\nSTOPPED_COUNT="+str(context[b"stopped_count"]).encode()+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nCHAIN_HEAD_SHA256="+context[b"chain_sha"]+b"\nTERMINAL_SEEN_SHA256=NONE\nACK_STATE=FAILURE_DURABLE_AWAITING_ACK\nRECONCILIATION_TOKEN=NONE\nCOMMON_TERMINAL_DEADLINE_NS="+str(deadline).encode()+b"\nDIRECT_REAP="+direct+b"\nCGROUP_EMPTY=1\nCGROUP_REMOVED="+(b"1" if context[b"removed"] else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nCERTIFICATE_LIVE_AT_COMMIT=0\nPASS_COMMIT_ORIGIN_MONOTONIC_NS=0\nPASS_COMMIT_DEADLINE_MONOTONIC_NS=0\nFINAL_PASS_MARGIN_NS=10000000\nSTAGE_RETAINED="+(b"1" if context[b"stage_present"] else b"0")+b"\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION="+disp+b"\nREPORT_END=1\n")
 parse_final_report(body);state,digest=durable_once(context,b"report.v4",body,deadline,False)
 context[b"report_state"]=state;context[b"report_sha"]=digest
 if state!=DURABLE_VERIFIED:context[b"faults"].add(b"REPORT_DURABILITY_UNKNOWN")
 return state,digest,disp

def final_candidate(context,terminal_origin,terminal_deadline):
 need(terminal_deadline==terminal_origin+FINAL_TOTAL_NS)
 deadline=min(terminal_deadline,time.monotonic_ns()+RECORD_NS)
 body=(b"P27E001_FINAL_CANDIDATE_V4\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT=15\nCOMMITTED_COUNT=15\nSTAGE_PRESENT=1\nCONTAINMENT_BOUND=1\nSTOPPED_COUNT=15\nCHAIN_HEAD_SHA256="+context[b"chain_sha"]+b"\nTRANSITIVE_ACK_CHAIN=1\nDIRECT_REAP=COMPLETE\nCGROUP_EMPTY=1\nCGROUP_REMOVED=1\nKILL_CALL_COUNT=0\nKILL_STATE=NOT_RESERVED\nTERMINAL_ORIGIN_NS="+str(terminal_origin).encode()+b"\nTERMINAL_DEADLINE_NS="+str(terminal_deadline).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCLONE3_GATE_ID="+CERT[b"CLONE3_CPYTHON_GATE_ID"]+b"\nDELETED_CGROUP_GATE_ID="+CERT[b"DELETED_CGROUP_FD_GATE_ID"]+b"\nSNAPSHOT_CONSTRUCTION_GATE_ID="+CERT[b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID"]+b"\nEXTERNAL_SURVIVAL_GATE_ID="+CERT[b"EXTERNAL_SURVIVAL_GATE_ID"]+b"\nOUTER_RECONCILER_GATE_ID="+CERT[b"OUTER_RECONCILER_GATE_ID"]+b"\nELIGIBLE=1\nCANDIDATE_END=1\n")
 remain=RECORD_NS+PASS_COMMIT_NS+PASS_MARGIN_NS+TERMINAL_NS+A_RECEIPT_NS+B_CLOSURE_NS
 state,digest=durable_once(context,b"final-candidate.v4",body,deadline,True,remain)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"REPORT_CANDIDATE_DURABILITY_UNKNOWN"})
 context[b"candidate_sha"]=digest;return digest

def terminal_seen_record(context,candidate_sha,terminal_deadline):
 deadline=min(terminal_deadline,time.monotonic_ns()+RECORD_NS)
 body=(b"P27E001_TERMINAL_SEEN_V4\nAUTH_ID="+AUTH+b"\nPREDECESSOR_SHA256="+candidate_sha+b"\nCANDIDATE_SHA256="+candidate_sha+b"\nACTOR_SEEN=1\nCOMMON_TERMINAL_DEADLINE_NS="+str(terminal_deadline).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nSEEN_END=1\n")
 remain=PASS_COMMIT_NS+PASS_MARGIN_NS+TERMINAL_NS+A_RECEIPT_NS+B_CLOSURE_NS
 state,digest=durable_once(context,b"terminal-seen.v4",body,deadline,True,remain)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"TERMINAL_SEEN_DURABILITY_UNKNOWN"})
 context[b"terminal_seen_sha"]=digest;return digest

def pass_report(context,terminal_deadline):
 origin=time.monotonic_ns();deadline=origin+PASS_COMMIT_NS
 remain=PASS_COMMIT_NS+PASS_MARGIN_NS+TERMINAL_NS+A_RECEIPT_NS+B_CLOSURE_NS
 need(origin+remain<=terminal_deadline);checkpoint(CERT,remain,terminal_deadline)
 token=sha(b"P27E001V4_RECONCILE\x00"+AUTH+b"\x00"+context[b"chain_sha"]+b"\x00"+context[b"terminal_seen_sha"]+b"\x00"+str(terminal_deadline).encode())
 body=(b"P27E001_FINAL_REPORT_V4\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT=15\nCOMMITTED_COUNT=15\nSTAGE_PRESENT=1\nCONTAINMENT_BOUND=1\nSTOPPED_COUNT=15\nSTOP_PROBE=NONE\nPRIMARY=NONE\nFAULT_SET=NONE\nCHAIN_HEAD_SHA256="+context[b"chain_sha"]+b"\nTERMINAL_SEEN_SHA256="+context[b"terminal_seen_sha"]+b"\nACK_STATE=PASS_COMMITTED_RECONCILIATION_REQUIRED\nRECONCILIATION_TOKEN="+token+b"\nCOMMON_TERMINAL_DEADLINE_NS="+str(terminal_deadline).encode()+b"\nDIRECT_REAP=COMPLETE\nCGROUP_EMPTY=1\nCGROUP_REMOVED=1\nKILL_CALL_COUNT=0\nKILL_STATE=NOT_RESERVED\nCERTIFICATE_LIVE_AT_COMMIT=1\nPASS_COMMIT_ORIGIN_MONOTONIC_NS="+str(origin).encode()+b"\nPASS_COMMIT_DEADLINE_MONOTONIC_NS="+str(deadline).encode()+b"\nFINAL_PASS_MARGIN_NS=10000000\nSTAGE_RETAINED=1\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION=PASS\nREPORT_END=1\n")
 parse_final_report(body);context[b"pass_effect_possible"]=True
 state,digest=durable_once(context,b"report.v4",body,min(deadline,terminal_deadline),True,PASS_MARGIN_NS+TERMINAL_NS+A_RECEIPT_NS+B_CLOSURE_NS)
 context[b"report_state"]=state;context[b"report_sha"]=digest;context[b"reconciliation_token"]=token
 if state!=DURABLE_VERIFIED:raise FaultSet({b"REPORT_DURABILITY_UNKNOWN"})
 context[b"pass_committed"]=True;context[b"outcome_durable"]=True
 return digest,token

def reconciliation_record(context,report_sha,terminal_deadline,receipt_ns):
 deadline=min(terminal_deadline,time.monotonic_ns()+A_RECEIPT_NS)
 body=(b"P27E001_OUTER_RECONCILIATION_V4\nAUTH_ID="+AUTH+b"\nREPORT_SHA256="+report_sha+b"\nRECONCILIATION_TOKEN="+context[b"reconciliation_token"]+b"\nACTOR_RECEIPT_NS="+str(receipt_ns).encode()+b"\nCOMMON_TERMINAL_DEADLINE_NS="+str(terminal_deadline).encode()+b"\nNO_REPLAY=1\nRECONCILIATION_END=1\n")
 state,digest=durable_once(context,b"outer-reconciliation.v4",body,deadline,True,B_CLOSURE_NS)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"RECONCILIATION_UNKNOWN"})
 context[b"reconciliation_sha"]=digest;return digest

def send_result(control,ordinal,probe,pid,context,stdout,stderr,out_eof,err_eof,out_over,err_over,empty,faults,done):
 deadline=context[b"origin"]+HOST_NS;out_frames=(len(stdout)+64999)//65000;err_frames=(len(stderr)+64999)//65000
 header=packet(b"V4_RESULT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_bound",b"1" if context[b"pidfd_bound"] else b"0"),(b"pidfd_exit_ready_observed",b"1" if context[b"pidfd_exit_ready_observed"] else b"0"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1" if out_eof else b"0"),(b"stdout_frames",str(out_frames).encode()),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",sha(stderr)),(b"stderr_eof",b"1" if err_eof else b"0"),(b"stderr_frames",str(err_frames).encode()),(b"cgroup_empty",b"1" if empty else b"0"),(b"fault_set",fault_csv(faults)),(b"capture_done_ns",str(done).encode())))
 send_exact(control,header,deadline)
 for stream,raw in ((b"STDOUT",stdout),(b"STDERR",stderr)):
  for index,start in enumerate(range(0,len(raw),65000)):
   payload=raw[start:start+65000]
   frame=packet(b"V4_RESULT_FRAME",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"stream",stream),(b"index",str(index).encode()),(b"bytes",str(len(payload)).encode()),(b"sha256",sha(payload))))+payload
   send_exact(control,frame,deadline)
 end=packet(b"V4_RESULT_END",((b"state",b"RESULT_END"),(b"ordinal",str(ordinal).encode()),(b"probe",probe)));send_exact(control,end,deadline)

def stream_arm(control,context,ordinal,probe):
 keys=(b"ordinal",b"probe",b"release_origin_ns",b"launch_deadline_ns",b"stdout_dev",b"stdout_ino",b"stderr_dev",b"stderr_ino",b"events_dev",b"events_ino",b"kill_dev",b"kill_ino")
 fds=();out=err=events=kill=own_events=own_kill=-1
 try:
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,4);need(len(fds)==4)
  out,err,events,kill=fds;fds=()
  values=parse_packet(raw,b"V4_STREAM_ARM",keys)
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
  origin=udec(values[b"release_origin_ns"],1);launch=udec(values[b"launch_deadline_ns"],1);need(origin<launch==origin+1000000000)
  post_deadline(launch);checkpoint(CERT,horizon_needed(origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),launch)
  fd_access(out,os.O_RDONLY);fd_access(err,os.O_RDONLY);fd_access(events,os.O_RDONLY);fd_access(kill,os.O_WRONLY)
  need(fcntl.fcntl(out,fcntl.F_GETFL)&os.O_NONBLOCK and fcntl.fcntl(err,fcntl.F_GETFL)&os.O_NONBLOCK)
  outs=os.fstat(out);errs=os.fstat(err);eventss=os.fstat(events);kills=os.fstat(kill)
  need(stat.S_ISFIFO(outs.st_mode) and stat.S_ISFIFO(errs.st_mode) and (outs.st_dev,outs.st_ino)!=(errs.st_dev,errs.st_ino))
  need((outs.st_dev,outs.st_ino)==(udec(values[b"stdout_dev"],1),udec(values[b"stdout_ino"],1)))
  need((errs.st_dev,errs.st_ino)==(udec(values[b"stderr_dev"],1),udec(values[b"stderr_ino"],1)))
  need((eventss.st_dev,eventss.st_ino)==(udec(values[b"events_dev"],1),udec(values[b"events_ino"],1)))
  need((kills.st_dev,kills.st_ino)==(udec(values[b"kill_dev"],1),udec(values[b"kill_ino"],1)))
  own_events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  own_kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  fd_access(own_events,os.O_RDONLY);fd_access(own_kill,os.O_WRONLY)
  a=os.fstat(own_events);bb=os.fstat(own_kill)
  need((a.st_dev,a.st_ino)==(eventss.st_dev,eventss.st_ino) and (bb.st_dev,bb.st_ino)==(kills.st_dev,kills.st_ino))
  context.update({b"out_fd":out,b"err_fd":err,b"events_fd":events,b"kill_fd":kill,b"origin":origin,b"launch":launch,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False})
  out=err=events=kill=-1
  reply=packet(b"V4_STREAMS_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe)))
  send_exact(control,reply,launch);checkpoint(CERT,horizon_needed(origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),launch)
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (out,err,events,kill,own_events,own_kill) if x>=0))

def pidfd_arm(control,context,ordinal,probe):
 fds=();number=procs=status=-1
 try:
  raw,fds=recv_monitored(control,4,context[b"launch"],1);need(len(fds)==1)
  number=fds[0];fds=()
  values=parse_packet(raw,b"V4_PIDFD_ARM",(b"ordinal",b"probe",b"outer_pid",b"stopped_raw_status",b"cgroup_member",b"pidfd_bound"))
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
  pid=udec(values[b"outer_pid"],2);stopped=udec(values[b"stopped_raw_status"],1)
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and values[b"cgroup_member"]==values[b"pidfd_bound"]==b"1")
  fd_access(number,os.O_RDWR);need(pidfd_pid(number)==pid)
  watcher=select.poll();watcher.register(number,select.POLLIN|select.POLLHUP|select.POLLERR);need(watcher.poll(0)==[])
  procs=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  status=os.open(b"/proc/"+str(pid).encode()+b"/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  need(read_all(procs,64)==str(pid).encode()+b"\n")
  state=[x for x in ascii_file(read_all(status,65536),65536).splitlines() if x.startswith(b"State:\t")]
  need(len(state)==1 and state[0].startswith(b"State:\tT") and watcher.poll(0)==[])
  need(pidfd_pid(number)==pid and read_all(procs,64)==str(pid).encode()+b"\n")
  context[b"outer_pidfd"]=number;number=-1;context[b"outer_pid"]=pid
  context[b"pidfd_bound"]=True;context[b"pidfd_exit_ready_observed"]=False;context[b"stopped_count"]+=1
  reply=packet(b"V4_PIDFD_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"pidfd_bound",b"1")))
  send_exact(control,reply,context[b"launch"]);checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"])
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (number,procs,status) if x>=0))

def release_phase(control,context,ordinal,probe):
 raw,fds=recv_monitored(control,4,context[b"launch"],0);need(fds==())
 keys=(b"ordinal",b"probe",b"outer_pid",b"pidfd_bound",b"stopped_raw_status",b"cgroup_member",b"cgroup_dev",b"cgroup_ino",b"cgroup_mode",b"cgroup_nlink",b"cgroup_uid",b"cgroup_gid",b"argv_sha256",b"env_sha256",b"release_origin_ns",b"launch_deadline_ns")
 values=parse_packet(raw,b"V4_RELEASE_CANDIDATE",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==context[b"outer_pid"] and values[b"pidfd_bound"]==values[b"cgroup_member"]==b"1")
 h64(values[b"argv_sha256"]);h64(values[b"env_sha256"]);need(udec(values[b"release_origin_ns"])==context[b"origin"] and udec(values[b"launch_deadline_ns"])==context[b"launch"])
 cg=os.fstat(context[b"cgfd"]);observed=(cg.st_dev,cg.st_ino,format(cg.st_mode,"o").encode(),cg.st_nlink,cg.st_uid,cg.st_gid)
 supplied=(udec(values[b"cgroup_dev"],1),udec(values[b"cgroup_ino"],1),values[b"cgroup_mode"],udec(values[b"cgroup_nlink"],1),udec(values[b"cgroup_uid"]),udec(values[b"cgroup_gid"]))
 need(observed==supplied)
 checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"]);digest=release_record(context,values)
 reply=packet(b"V4_RELEASE_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_sha256",digest)))
 send_exact(control,reply,context[b"launch"]);checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"])

def monitor_probe(control,context,ordinal,probe):
 stdout=bytearray();stderr=bytearray();out_eof=err_eof=out_over=err_over=False;faults=set();actor_lost=False
 deadline=context[b"origin"]+HOST_NS;poller=select.poll()
 for number in (context[b"out_fd"],context[b"err_fd"],context[b"events_fd"],context[b"outer_pidfd"],4,control.fileno()):poller.register(number,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),deadline)
  now=time.monotonic_ns()
  try:events=poller.poll(10)
  except InterruptedError:events=[]
  cmask=0;amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   if number==4:amask|=event
  if cmask&select.POLLIN:
   try:
    raw,fds=recv_monitored(control,4,min(deadline,time.monotonic_ns()+ACK_NS),0)
    faults.add(b"CONTROL_MALFORMED")
   except RemoteAbort as error:faults.update(error.faults)
   except ActorLost:actor_lost=True;faults.add(b"ACTOR_LOST")
   except FaultSet as error:faults.update(error.faults)
  elif cmask&(select.POLLHUP|select.POLLERR):
   actor_lost=True;faults.add(b"ACTOR_LOST")
  if amask:
   actor_lost=True;faults.add(b"ACTOR_LOST")
  for number,event in events:
   if number==context[b"out_fd"]:
    try:
     overflow,eof=drain(number,stdout);out_over|=overflow;out_eof|=eof
    except FaultSet as error:faults.update(error.faults)
   elif number==context[b"err_fd"]:
    try:
     overflow,eof=drain(number,stderr);err_over|=overflow;err_eof|=eof
    except FaultSet as error:faults.update(error.faults)
   elif number==context[b"outer_pidfd"] and event&(select.POLLIN|select.POLLHUP|select.POLLERR):
    context[b"pidfd_exit_ready_observed"]=True
  if not out_eof:
   try:
    overflow,eof=drain(context[b"out_fd"],stdout);out_over|=overflow;out_eof|=eof
   except FaultSet as error:faults.update(error.faults)
  if not err_eof:
   try:
    overflow,eof=drain(context[b"err_fd"],stderr);err_over|=overflow;err_eof|=eof
   except FaultSet as error:faults.update(error.faults)
  if out_over or err_over:faults.add(b"CAPTURE_OVERFLOW")
  if stderr:faults.add(b"STDERR_NONEMPTY")
  empty_state=observe_population(context)
  if empty_state is None:faults.add(b"CONTAINMENT_OBSERVATION_UNKNOWN")
  if not faults and now>deadline:faults.add(b"WATCHDOG_DEADLINE")
  if faults:
   context[b"faults"].update(faults);begin_cleanup(context)
   if empty_state is True and context[b"kill_state"]==b"NOT_RESERVED" and now<context[b"cleanup_deadline"]:kill_once(context,primary(context[b"faults"]))
  if not faults and out_eof and err_eof and empty_state is False and context[b"pidfd_bound"] and context[b"pidfd_exit_ready_observed"]:break
  if faults and context[b"cleanup_deadline"] is not None and now>=context[b"cleanup_deadline"]:break
  if actor_lost and context[b"cleanup_deadline"] is not None and now>=context[b"cleanup_deadline"]:break
 checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),deadline)
 done=time.monotonic_ns();empty_state=observe_population(context);empty=empty_state is False
 context[b"last_out_eof"]=out_eof;context[b"last_err_eof"]=err_eof
 if not actor_lost:
  send_result(control,ordinal,probe,context[b"outer_pid"],context,bytes(stdout),bytes(stderr),out_eof,err_eof,out_over,err_over,empty,set(context[b"faults"]),done)
 return actor_lost,set(context[b"faults"]),empty,bytes(stdout),bytes(stderr)

def close_probe(context):
 for key in (b"out_fd",b"err_fd",b"events_fd",b"kill_fd",b"outer_pidfd"):
  number=context.get(key,-1)
  if number>=0:
   try:os.close(number)
   except OSError:pass
  context[key]=-1
 context[b"pidfd_bound"]=False;context[b"pidfd_exit_ready_observed"]=False

def request_release_disable(control,context,stop):
 if context[b"release_disabled"] or context[b"actor_lost"]:return
 deadline=min(context[b"cleanup_deadline"],time.monotonic_ns()+ACTOR_DISABLE_NS)
 notice=packet(b"V4_ABORT",((b"sender",b"B"),(b"state",b"CLEANUP_RELEASE_DISABLE"),(b"ordinal",b"NONE"),(b"probe",stop),(b"effect_state",b"CONSUMED"),(b"stage_present",b"1" if context[b"stage_present"] else b"0"),(b"release_disabled",b"0"),(b"terminal_deadline_ns",str(context[b"cleanup_deadline"]).encode()),(b"fault_set",fault_csv(context[b"faults"]))))
 try:
  send_exact(control,notice,deadline)
  raw,fds=recv_monitored(control,4,deadline,0);need(fds==())
  values,faults=parse_abort(raw,b"A");context[b"faults"].update(faults)
  need(values[b"release_disabled"]==b"1");context[b"release_disabled"]=True
 except RemoteAbort as error:
  context[b"faults"].update(error.faults);context[b"release_disabled"]=True
 except ActorLost:
  context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"ACTOR_LOST")
 except FaultSet as error:context[b"faults"].update(error.faults)
 except BaseException:context[b"faults"].add(b"CONTROL_MALFORMED")
 if not context[b"release_disabled"]:
  context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")

def pass_locked(context):
 return context[b"pass_effect_possible"] or context[b"pass_committed"]

def terminal_safe(context):
 state=observe_population(context);context[b"last_population"]=state
 if context[b"containment_bound"]:return state is False
 return context[b"stopped_count"]==0

def terminal_owner_loop(control,context,mode,kind,subject,disp,deadline):
 need(mode in (b"SUCCESS",b"FAILURE") and deadline==context[b"terminal_deadline"])
 context[b"terminal_mode"]=mode;context[b"terminal_kind"]=kind;context[b"terminal_subject"]=subject
 context[b"terminal_phase"]=b"NOTICE_SEND_EFFECT_UNKNOWN"
 if mode==b"SUCCESS":
  notice=packet(b"V4_TERMINAL_CANDIDATE_DURABLE",((b"state",b"TERMINAL_CANDIDATE_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"chain_head_sha256",context[b"chain_sha"]),(b"terminal_deadline_ns",str(deadline).encode())))
 else:
  notice=packet(b"V4_TERMINAL_FAILURE_DURABLE",((b"state",b"TERMINAL_FAILURE_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"disposition",disp),(b"terminal_deadline_ns",str(deadline).encode())))
 try:
  send_exact(control,notice,deadline);context[b"terminal_phase"]=b"WAIT_TERMINAL_SEEN"
 except BaseException:
  if not pass_locked(context):raise
  context[b"ack_effect_unknown"]=True;context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
 while True:
  for key in (b"out_fd",b"err_fd"):
   number=context.get(key,-1)
   if number>=0:
    try:drain(number,bytearray())
    except FaultSet as error:context[b"faults"].update(error.faults)
  safe=terminal_safe(context);now=time.monotonic_ns()
  if context[b"actor_lost"] and context[b"outcome_durable"] and safe:
   context[b"owner_released"]=True;context[b"terminal_phase"]=b"ACTOR_LOSS_SAFE_CLOSURE";return
  if now>=deadline:
   context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED");context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
   owner_poll(control,context,now+50000000);continue
  poller=select.poll();poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
  for key in (b"root_events_fd",b"events_fd",b"out_fd",b"err_fd"):
   number=context.get(key,-1)
   if number>=0:poller.register(number,select.POLLIN|select.POLLHUP|select.POLLERR)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==4:amask|=event
  if cmask&select.POLLIN:
   try:
    raw,fds=recv_monitored(control,4,deadline,0);need(fds==())
    phase=context[b"terminal_phase"]
    if phase==b"WAIT_TERMINAL_SEEN":
     values=parse_packet(raw,b"V4_TERMINAL_SEEN",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_deadline_ns"))
     need(values[b"state"]==b"TERMINAL_SEEN" and values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==kind and values[b"subject_sha256"]==subject and udec(values[b"terminal_deadline_ns"])==deadline)
     if mode==b"SUCCESS":
      context[b"terminal_seen_sha"]=terminal_seen_record(context,subject,deadline);terminal_prepass_guard(control,context,deadline)
      report_sha,token=pass_report(context,deadline);context[b"pass_committed"]=True;context[b"outcome_durable"]=True
      ack_state=b"PASS_COMMITTED_RECONCILIATION_REQUIRED"
     else:
      report_sha=subject;token=b"NONE";context[b"outcome_durable"]=True;ack_state=b"FAILURE_COMMITTED"
     ack=packet(b"V4_TERMINAL_ACK",((b"state",b"TERMINAL_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"terminal_seen_sha256",context.get(b"terminal_seen_sha",b"0"*64)),(b"report_sha256",report_sha),(b"reconciliation_token",token),(b"ack_state",ack_state),(b"terminal_deadline_ns",str(deadline).encode())))
     context[b"ack_state"]=b"ACK_SEND_EFFECT_UNKNOWN";context[b"terminal_phase"]=b"ACK_SEND_EFFECT_UNKNOWN"
     try:
      send_exact(control,ack,deadline);context[b"ack_state"]=b"ACK_SENT";context[b"terminal_phase"]=b"WAIT_ACK_RECEIPT"
     except BaseException:
      context[b"ack_effect_unknown"]=True;context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
    elif phase==b"WAIT_ACK_RECEIPT":
     values=parse_packet(raw,b"V4_TERMINAL_ACK_RECEIPT",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"report_sha256",b"reconciliation_token",b"actor_receipt_ns",b"terminal_deadline_ns"))
     need(values[b"state"]==b"ACK_RECEIVED_NO_REPLAY" and values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==kind and values[b"subject_sha256"]==subject and udec(values[b"terminal_deadline_ns"])==deadline)
     receipt_ns=udec(values[b"actor_receipt_ns"],1,deadline);need(receipt_ns<=time.monotonic_ns()<=deadline)
     if mode==b"SUCCESS":
      need(values[b"report_sha256"]==context[b"report_sha"] and values[b"reconciliation_token"]==context[b"reconciliation_token"])
      closure_sha=reconciliation_record(context,context[b"report_sha"],deadline,receipt_ns)
     else:
      need(values[b"report_sha256"]==subject and values[b"reconciliation_token"]==b"NONE");closure_sha=subject
     closed_packet=packet(b"V4_TERMINAL_CLOSED",((b"state",b"OWNER_CLOSED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"closure_sha256",closure_sha),(b"owner",b"B"),(b"terminal_deadline_ns",str(deadline).encode())))
     context[b"terminal_phase"]=b"OWNER_CLOSE_SEND_EFFECT_UNKNOWN"
     try:
      send_exact(control,closed_packet,deadline);context[b"terminal_phase"]=b"OWNER_CLOSED"
      if terminal_safe(context):context[b"owner_released"]=True;return
     except BaseException:
      context[b"ack_effect_unknown"]=True;context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
    elif pass_locked(context):
     if raw.startswith(b"V4_ABORT|"):
      values,faults=parse_abort(raw,b"A");context[b"faults"].add(b"ACK_EFFECT_UNKNOWN")
     else:context[b"faults"].add(b"CONTROL_MALFORMED")
     context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
    else:raise FaultSet({b"CONTROL_MALFORMED"})
   except RemoteAbort as error:
    if pass_locked(context):
     context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
    else:raise
   except ActorLost:
    context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"ACTOR_LOST")
   except FaultSet:
    if pass_locked(context):
     context[b"faults"].add(b"RECONCILIATION_UNKNOWN");context[b"terminal_phase"]=b"FROZEN_TRANSFER_REQUIRED"
    else:raise
  if amask or (cmask&(select.POLLHUP|select.POLLERR) and not cmask&select.POLLIN):
   context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"ACTOR_LOST")

def terminal_failure(control,context,stop,faults,actor_lost):
 need(not pass_locked(context));context[b"faults"].update(faults);context[b"actor_lost"]|=actor_lost
 if actor_lost:context[b"release_disabled"]=True
 if not context[b"faults"]:context[b"faults"].add(b"INTERNAL_INVARIANT")
 if b"DIRECT_WAIT_UNKNOWN" in context[b"faults"]:context[b"direct_reap_state"]=b"UNKNOWN"
 recover_stage_presence(context)
 begin_cleanup(context);context[b"terminal_origin"]=context[b"cleanup_origin"];context[b"terminal_deadline"]=context[b"cleanup_deadline"]
 request_release_disable(control,context,stop);begin_cleanup(context)
 if context[b"attempt"]<0 and not context[b"collision"]:
  retain_attempt_dirfd(context)
  while True:
   owner_poll(control,context,time.monotonic_ns()+50000000)
 while time.monotonic_ns()<context[b"cleanup_deadline"]:
  owner_poll(control,context,context[b"cleanup_deadline"])
  state=observe_population(context);context[b"last_population"]=state
  if context[b"containment_bound"] and context[b"kill_state"]==b"NOT_RESERVED":kill_once(context,primary(context[b"faults"]))
  if state is False:break
 state=observe_population(context)
 if state is not False:retained_until_empty(control,context,stop)
 disp=disposition(context[b"faults"])
 if context[b"collision"]:
  context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")
  while True:owner_poll(control,context,time.monotonic_ns()+50000000)
 recovery_record(context,stop,context[b"actor_lost"])
 report_state,report_sha,disp=failure_report(context,stop,context[b"actor_lost"])
 if report_state!=DURABLE_VERIFIED:
  context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")
  while not (context[b"actor_lost"] and context.get(b"outcome_durable",False) and terminal_safe(context)):
   owner_poll(control,context,time.monotonic_ns()+50000000)
  context[b"owner_released"]=True;return disp
 context[b"outcome_durable"]=True
 if context[b"actor_lost"] and terminal_safe(context):
  context[b"owner_released"]=True;context[b"terminal_phase"]=b"ACTOR_LOSS_SAFE_CLOSURE";return disp
 terminal_owner_loop(control,context,b"FAILURE",b"FAILURE",report_sha,disp,context[b"terminal_deadline"]);return disp

def validated_exchange(control,context,ordinal,probe,stdout,stderr):
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 values=parse_packet(raw,b"V4_VALIDATED_CANDIDATE",CANDIDATE_KEYS)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 need(values[b"release_record_sha256"]==context[b"release_sha"] and udec(values[b"release_origin_ns"])==context[b"origin"])
 release_return=udec(values[b"release_return_ns"]);host_complete=udec(values[b"host_complete_ns"]);capture_done=udec(values[b"capture_done_ns"])
 need(context[b"origin"]<release_return<=context[b"launch"] and capture_done<=host_complete<=context[b"origin"]+HOST_NS)
 need(values[b"direct_wait_state"]==b"COMPLETE" and values[b"outer_raw_status"]==b"0")
 need(values[b"pidfd_bound"]==values[b"pidfd_exit_ready_observed"]==b"1")
 need(udec(values[b"stdout_len"])==len(stdout) and values[b"stdout_sha256"]==sha(stdout) and values[b"stdout_eof"]==b"1" and values[b"stdout_overflow"]==b"0")
 need(udec(values[b"stderr_len"])==len(stderr)==0 and values[b"stderr_sha256"]==sha(stderr) and values[b"stderr_eof"]==b"1" and values[b"stderr_overflow"]==b"0")
 need(values[b"cgroup_empty"]==b"1" and values[b"parser_language"]==values[b"parser_structure"]==values[b"parser_semantics"]==values[b"candidate"]==values[b"terminal"]==b"ACCEPTED")
 need(values[b"certificate_expiry_realtime_ns"]==CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 h64(values[b"stdout_sha256"]);h64(values[b"stderr_sha256"])
 ack_deadline=min(context[b"origin"]+TOTAL_NS,host_complete+ACK_NS);need(time.monotonic_ns()+2*RECORD_NS<=ack_deadline)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline);validated_sha=validated_record(context,values,ack_deadline)
 reply=packet(b"V4_VALIDATED_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha)))
 send_exact(control,reply,ack_deadline)
 raw,fds=recv_monitored(control,4,ack_deadline,0);need(fds==())
 intent=parse_packet(raw,b"V4_ACK_COMMIT_INTENT",(b"ordinal",b"probe",b"validated_sha256",b"host_complete_ns",b"ack_deadline_ns",b"actor_ack_intent_ns"))
 need(udec(intent[b"ordinal"],0,14)==ordinal and intent[b"probe"]==probe and intent[b"validated_sha256"]==validated_sha)
 actor_ack=udec(intent[b"actor_ack_intent_ns"]);received=time.monotonic_ns();ack_deadline=udec(intent[b"ack_deadline_ns"],1)
 need(udec(intent[b"host_complete_ns"])==host_complete and ack_deadline==min(context[b"origin"]+TOTAL_NS,host_complete+ACK_NS))
 need(host_complete<=actor_ack<=received<=ack_deadline and actor_ack-host_complete<=ACK_NS)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline)
 ack_sha=ack_intent_record(context,ordinal,probe,actor_ack,received,ack_deadline)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline)
 context[b"committed"][ordinal]=True;context[b"direct_reaps"]+=1;context[b"direct_reap_state"]=b"COMPLETE"
 committed=packet(b"V4_COMMITTED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha)))
 send_exact(control,committed,ack_deadline)
 raw,fds=recv_monitored(control,4,ack_deadline,0);need(fds==())
 seen=parse_packet(raw,b"V4_COMMITTED_SEEN",(b"ordinal",b"probe",b"ack_sha256",b"host_complete_ns",b"ack_deadline_ns"))
 need(udec(seen[b"ordinal"],0,14)==ordinal and seen[b"probe"]==probe and seen[b"ack_sha256"]==ack_sha)
 need(udec(seen[b"host_complete_ns"])==host_complete and udec(seen[b"ack_deadline_ns"])==ack_deadline and time.monotonic_ns()-host_complete<=ACK_NS)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline);return ack_sha

def recover_stage_presence(context):
 if context[b"stage_present"]:return
 base=number=leaf=-1
 try:
  base=os.open(b".",O_DIR)
  named=os.stat(AUTH,dir_fd=base,follow_symlinks=False)
  number=os.open(AUTH,O_DIR,dir_fd=base);held=os.fstat(number)
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid))
  need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==held.st_gid==0)
  context[b"stage_present"]=True;context[b"stage_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  context[b"stage_fd"]=number;number=-1
  specs=((b"keeper.py",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256"),(b"launcher.py",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256"),(b"marker.py",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256"),(b"child.py",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256"))
  for name,bkey,lkey,hkey in specs:
   try:
    leaf=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"stage_fd"])
    body=read_all(leaf,udec(CERT[bkey],1));st=os.fstat(leaf)
    need(stat.S_ISREG(st.st_mode) and (st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode),st.st_nlink)==(0,0,0o400,1))
    need((len(body),body.count(b"\n"),sha(body))==(udec(CERT[bkey],1),udec(CERT[lkey]),CERT[hkey]))
   finally:close_numbers(tuple(x for x in (leaf,) if x>=0));leaf=-1
 except FileNotFoundError:return
 except BaseException:context[b"faults"].add(b"STAGING_FAULT")
 finally:close_numbers(tuple(x for x in (leaf,number,base) if x>=0))

def stage_bind(control,context):
 fds=();number=base=leaf=-1
 keys=(b"state",b"ordinal",b"probe",b"stage_origin_ns",b"stage_deadline_ns",b"stage_return_ns",b"safe_dev",b"safe_ino",b"safe_mode",b"safe_nlink",b"safe_uid",b"safe_gid",b"keeper_sha256",b"launcher_sha256",b"marker_sha256",b"child_sha256")
 try:
  boot=time.monotonic_ns()+STAGE_NS;raw,fds=recv_monitored(control,4,boot,1);need(len(fds)==1)
  number=fds[0];fds=()
  values=parse_packet(raw,b"V4_STAGE_DURABLE",keys)
  need(values[b"state"]==b"STAGE_DURABLE" and values[b"ordinal"]==values[b"probe"]==b"NONE")
  origin=udec(values[b"stage_origin_ns"],1);deadline=udec(values[b"stage_deadline_ns"],1)
  need(deadline==origin+STAGE_NS and udec(values[b"stage_return_ns"],origin,deadline)<=time.monotonic_ns()<=deadline)
  checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline);fd_access(number,os.O_RDONLY)
  held=os.fstat(number);supplied=(udec(values[b"safe_dev"],1),udec(values[b"safe_ino"],1),octal(values[b"safe_mode"]),udec(values[b"safe_nlink"],1),udec(values[b"safe_uid"]),udec(values[b"safe_gid"]))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==supplied)
  need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==held.st_gid==0 and held.st_nlink==2)
  base=os.open(b".",O_DIR);base_check(base,CERT,b"SAFE_BIND")
  named=os.stat(AUTH,dir_fd=base,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  specs=((b"keeper.py",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"keeper_sha256"),(b"launcher.py",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"launcher_sha256"),(b"marker.py",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"marker_sha256"),(b"child.py",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"child_sha256"))
  for name,bkey,lkey,hkey,pkey in specs:
   try:
    leaf=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number);fd_access(leaf,os.O_RDONLY)
    body=read_all(leaf,udec(CERT[bkey],1));st=os.fstat(leaf)
    need(stat.S_ISREG(st.st_mode) and (st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode),st.st_nlink)==(0,0,0o400,1))
    need((len(body),body.count(b"\n"),sha(body))==(udec(CERT[bkey],1),udec(CERT[lkey]),CERT[hkey]))
    need(values[pkey]==CERT[hkey])
   finally:close_numbers(tuple(x for x in (leaf,) if x>=0));leaf=-1
  checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline)
  context[b"stage_fd"]=number;number=-1;context[b"stage_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  context[b"stage_present"]=True;context[b"stage_deadline"]=deadline
  reply=packet(b"V4_STAGE_ACK",((b"state",b"STAGE_BOUND"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"stage_deadline_ns",str(deadline).encode()),(b"safe_dev",str(held.st_dev).encode()),(b"safe_ino",str(held.st_ino).encode())))
  send_exact(control,reply,deadline);checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline)
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (leaf,number,base) if x>=0))

def containment_bind(control,context):
 fds=();number=root_events=root_kill=ctype=controllers=subtree=-1
 try:
  boot=time.monotonic_ns()+ACK_NS;raw,fds=recv_monitored(control,4,boot,1);need(len(fds)==1)
  number=fds[0];fds=()
  keys=(b"state",b"ordinal",b"probe",b"contain_origin_ns",b"contain_deadline_ns",b"dev",b"ino",b"mode",b"nlink",b"uid",b"gid",b"base_dev",b"base_ino",b"mount_id",b"mountinfo_sha256",b"type_hex",b"controllers_hex",b"subtree_control_hex")
  values=parse_packet(raw,b"V4_CONTAINMENT",keys)
  need(values[b"state"]==b"CONTAINMENT_CANDIDATE" and values[b"ordinal"]==values[b"probe"]==b"NONE" and context[b"stage_present"])
  origin=udec(values[b"contain_origin_ns"],1);deadline=udec(values[b"contain_deadline_ns"],1);need(deadline==origin+ACK_NS and time.monotonic_ns()<=deadline)
  checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline);fd_access(number,os.O_RDONLY)
  held=os.fstat(number);need(stat.S_ISDIR(held.st_mode))
  supplied=(udec(values[b"dev"],1),udec(values[b"ino"],1),octal(values[b"mode"]),udec(values[b"nlink"],1),udec(values[b"uid"]),udec(values[b"gid"]))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==supplied)
  need(values[b"mode"]==CERT[b"CGROUP_CHILD_MODE"] and values[b"uid"]==CERT[b"CGROUP_CHILD_UID"] and values[b"gid"]==CERT[b"CGROUP_CHILD_GID"] and values[b"nlink"]==b"2")
  base_check(6,CERT,b"CGROUP_BASE");base=os.fstat(6)
  need((udec(values[b"base_dev"],1),udec(values[b"base_ino"],1))==(base.st_dev,base.st_ino))
  named=os.stat(AUTH,dir_fd=6,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  mid,line=mount_binding(number);need(mid==udec(values[b"mount_id"],1)==udec(CERT[b"CGROUP2_MOUNT_ID"],1))
  need(sha(line)==values[b"mountinfo_sha256"]==CERT[b"CGROUP2_MOUNTINFO_SHA256"] and statfs_magic(number)==int(CERT[b"CGROUP2_FS_MAGIC"],16))
  ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  fd_access(ctype,os.O_RDONLY);fd_access(controllers,os.O_RDONLY);fd_access(subtree,os.O_RDONLY);fd_access(root_events,os.O_RDONLY);fd_access(root_kill,os.O_WRONLY)
  type_raw=read_all(ctype,128);controllers_raw=read_all(controllers,4096);subtree_raw=read_all(subtree,4096)
  need(type_raw.hex().encode()==values[b"type_hex"]==CERT[b"CGROUP_CHILD_TYPE_HEX"])
  need(controllers_raw.hex().encode()==values[b"controllers_hex"]==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"])
  need(subtree_raw.hex().encode()==values[b"subtree_control_hex"]==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"])
  need(not populated(root_events));checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline)
  context[b"cgfd"]=number;number=-1;context[b"root_events_fd"]=root_events;root_events=-1
  context[b"root_kill_fd"]=root_kill;root_kill=-1;context[b"containment_bound"]=True;context[b"contain_deadline"]=deadline
  context[b"cgroup_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  reply=packet(b"V4_CONTAINMENT_ACK",((b"state",b"CONTAINMENT_BOUND"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"contain_deadline_ns",str(deadline).encode()),(b"dev",str(held.st_dev).encode()),(b"ino",str(held.st_ino).encode())))
  send_exact(control,reply,deadline);checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline)
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (number,root_events,root_kill,ctype,controllers,subtree) if x>=0))

def acquire_control(actor_pid):
 control=None
 try:
  control=socket.socket(fileno=3)
  need(control.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET);fd_access(3,os.O_RDWR)
  need(fcntl.fcntl(3,fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",control.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(actor_pid,0,0))
  result=control;control=None;return result
 finally:
  if control is not None:
   try:control.close()
   except BaseException:pass

def static_inputs():
 global AUTH,CERT,DEPS
 need(type(sys.argv)is list and len(sys.argv)==8 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RECOVER_V4")
 supplied=h64(sys.argv[2].encode("ascii"));actor_pid=udec(sys.argv[3].encode("ascii"),2)
 plan_sha=h64(sys.argv[4].encode("ascii"));source_sha=h64(sys.argv[5].encode("ascii"))
 safe_dev=udec(sys.argv[6].encode("ascii"),1);safe_ino=udec(sys.argv[7].encode("ascii"),1)
 need(os.read(0,1)==b"");fd_access(0,os.O_RDONLY);need(stat.S_ISFIFO(os.fstat(0).st_mode));closed(1);closed(2)
 fd_access(4,os.O_RDWR);need(pidfd_pid(4)==actor_pid)
 for number in (7,8,9,100):seals(number);fd_access(number,os.O_RDWR)
 snapshot_raw=whole_snapshot();cert_raw=read_all(7);envelope_raw=read_all(8);source_raw=read_all(100)
 CERT,DEPS=contract(cert_raw);issued=envelope(envelope_raw)
 need(sha(cert_raw)==issued[b"CERTIFICATE_SHA256"] and sha(envelope_raw)==CERT[b"ISSUER_ENVELOPE_SHA256"])
 not_before=udec(CERT[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(issued[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(issued[b"NOT_AFTER_REALTIME_NS"]))
 for entry in DEPS:verify_dependency(entry)
 AUTH=sha(b"P27E001V4\x00"+cert_raw+b"\x00"+envelope_raw);need(AUTH==supplied)
 need(plan_sha==CERT[b"PLAN_SHA256"]==issued[b"PLAN_SHA256"])
 need(issued[b"RUNNER_SHA256"]==CERT[b"RUNNER_SHA256"])
 need(source_sha==sha(source_raw)==CERT[b"RECOVERY_SHA256"]==issued[b"RECOVERY_SHA256"])
 need(issued[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot_raw)==SNAPSHOT_EXPECT[2])
 need(issued[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and issued[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672")
 need(issued[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX)
 need(issued[b"V15_SHA256"]==CERT[b"V15_SHA256"]==V15_SHA)
 base_check(5,CERT,b"ATTEMPT_BASE");base_check(6,CERT,b"CGROUP_BASE")
 rootfd=safebase=-1
 try:
  rootfd=os.open(b"/",O_DIR);safebase=os.open(b".",O_DIR)
  base_check(rootfd,CERT,b"RUNTIME_ROOT");base_check(safebase,CERT,b"SAFE_BIND")
  root_mid,root_line=mount_binding(rootfd);safe_mid,safe_line=mount_binding(safebase)
  need(root_mid==udec(CERT[b"RUNTIME_ROOT_MOUNT_ID"],1) and sha(root_line)==CERT[b"RUNTIME_ROOT_MOUNTINFO_SHA256"])
  need(safe_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(safe_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"] and root_mid!=safe_mid)
 finally:close_numbers(tuple(x for x in (rootfd,safebase) if x>=0))
 attempt_mid,attempt_line=mount_binding(5)
 need(attempt_mid==udec(CERT[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==CERT[b"ATTEMPT_BASE_MOUNTINFO_SHA256"])
 cgroup_mid,cgroup_line=mount_binding(6)
 need(statfs_magic(6)==int(CERT[b"CGROUP2_FS_MAGIC"],16) and cgroup_mid==udec(CERT[b"CGROUP2_MOUNT_ID"],1) and sha(cgroup_line)==CERT[b"CGROUP2_MOUNTINFO_SHA256"])
 base_type=base_controllers=base_subtree=-1
 try:
  base_type=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  base_controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  base_subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"])
  need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"])
  need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"])
 finally:close_numbers((base_type,base_controllers,base_subtree))
 need((safe_dev,safe_ino)==(udec(CERT[b"SAFE_BIND_DEV"],1),udec(CERT[b"SAFE_BIND_INO"],1)))
 final_context(safe_dev,safe_ino);scrub_exact({0,3,4,5,6,7,8,9,100});checkpoint(CERT,ENTRY_REMAIN_NS)
 return acquire_control(actor_pid),cert_raw,envelope_raw,source_raw

def minimal_context():
 return {
  b"attempt":-1,b"local_fd_state":b"ABSENT",b"attempt_base_closed_on_collision":False,
  b"consumed":False,b"consumption_state":b"PREARMED",b"consume_origin":0,b"consume_deadline":0,b"arm_effect_possible":False,
  b"intent_durable":False,b"collision":False,b"collision_identity":(0,0,0,0,0,0),
  b"faults":set(),b"durability":{},b"durability_digest":{},b"durability_faults":{},b"record_seq":0,b"chain_sha":b"0"*64,b"committed":[False]*15,b"entered":0,b"stopped_count":0,
  b"direct_reaps":0,b"direct_reap_state":b"UNAVAILABLE",
  b"stage_present":False,b"stage_fd":-1,b"stage_identity":None,b"stage_deadline":0,
  b"containment_bound":False,b"contain_deadline":0,b"actor_lost":False,b"release_disabled":False,
  b"kill_call_count":0,b"kill_state":b"NOT_RESERVED",b"kill_ticket_state":b"ABSENT_KNOWN",
  b"cleanup_origin":None,b"cleanup_deadline":None,b"last_population":None,b"last_out_eof":False,b"last_err_eof":False,
  b"cgfd":-1,b"root_events_fd":-1,b"root_kill_fd":-1,b"events_fd":-1,b"kill_fd":-1,b"out_fd":-1,b"err_fd":-1,
  b"outer_pidfd":-1,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False,b"outer_pid":-1,b"removed":False,
  b"report_state":b"ABSENT_KNOWN",b"report_sha":b"0"*64,b"retained_state":b"ABSENT_KNOWN",
  b"candidate_sha":b"0"*64,b"terminal_seen_sha":b"0"*64,b"reconciliation_token":b"0"*64,b"reconciliation_sha":b"0"*64,
  b"terminal_origin":0,b"terminal_deadline":0,b"terminal_mode":b"NONE",b"terminal_kind":b"NONE",b"terminal_subject":b"0"*64,
  b"terminal_phase":b"NOT_STARTED",b"ack_state":b"NOT_SENT",b"ack_effect_unknown":False,b"pass_effect_possible":False,b"pass_committed":False,
  b"outcome_durable":False,b"owner_released":False
 }

def ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error):
 context[b"consumed"]=True;context[b"consumption_state"]=b"CONSUME_EDGE_UNKNOWN";context[b"faults"].add(b"CONSUME_EDGE_UNKNOWN")
 if isinstance(error,RemoteAbort):
  context[b"faults"].update(error.faults);context[b"release_disabled"]=True
 elif isinstance(error,FaultSet):context[b"faults"].update(error.faults)
 elif isinstance(error,ActorLost):
  context[b"faults"].add(b"ACTOR_LOST");context[b"actor_lost"]=True;context[b"release_disabled"]=True
 try:consume_attempt(context,cert_raw,envelope_raw,source_raw,context[b"consume_deadline"])
 except CertificateExpired:context[b"faults"].add(b"CERTIFICATE_EXPIRED")
 except FaultSet as attempt_error:context[b"faults"].update(attempt_error.faults)
 terminal_failure(control,context,b"NONE",set(context[b"faults"]),isinstance(error,ActorLost))

def refusal_values(raw):
 values=parse_packet(raw,b"V4_REFUSE_PRECOMMIT",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"reason",b"consume_deadline_ns"))
 need(values[b"state"]==b"REFUSE_PRECOMMIT" and values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"auth_id"]==AUTH)
 need(values[b"a_begin_state"] in (b"BEGIN_NOT_ENTERED",b"BEGIN_SEND_EFFECT_UNKNOWN",b"BEGIN_SENT"))
 need(values[b"a_arm_state"] in (b"ARM_NOT_OBSERVED",b"ARM_RECEIVE_EFFECT_UNKNOWN",b"ARMED_CONFIRMED"))
 udec(values[b"consume_deadline_ns"]);return values

def refusal_ack(control,values,b_state,deadline):
 need(udec(values[b"consume_deadline_ns"]) in (0,deadline))
 ack=packet(b"V4_REFUSE_ACK",((b"state",b"REFUSE_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"a_begin_state",values[b"a_begin_state"]),(b"a_arm_state",values[b"a_arm_state"]),(b"b_state",b_state),(b"consume_deadline_ns",values[b"consume_deadline_ns"]),(b"disposition",b"UNCONSUMED")))
 send_exact(control,ack,deadline)

def terminal_prepass_guard(control,context,deadline):
 checkpoint(CERT,PASS_COMMIT_NS+PASS_MARGIN_NS+TERMINAL_NS+A_RECEIPT_NS+B_CLOSURE_NS,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 events=poller.poll(0);cmask=amask=0
 for number,event in events:
  if number==control.fileno():cmask|=event
  if number==4:amask|=event
 if cmask&select.POLLIN:
  raw,fds=recv_monitored(control,4,deadline,0);close_numbers(fds)
  if raw.startswith(b"V4_ABORT|"):
   values,faults=parse_abort(raw,b"A");context[b"release_disabled"]=True;raise RemoteAbort(faults)
  raise FaultSet({b"CONTROL_MALFORMED"})
 if amask or cmask&(select.POLLHUP|select.POLLERR):raise ActorLost("terminal-guard")

def main():
 context=minimal_context();control=None
 try:
  control,cert_raw,envelope_raw,source_raw=static_inputs()
  ready_deadline=time.monotonic_ns()+10000000000
  ready=packet(b"V4_READY",((b"state",b"READY"),(b"ordinal",b"NONE"),(b"probe",b"NONE")))
  send_exact(control,ready,ready_deadline)
  raw,fds=recv_monitored(control,4,ready_deadline,0);need(fds==())
  if raw.startswith(b"V4_REFUSE_PRECOMMIT|"):
   values=refusal_values(raw);need(values[b"a_begin_state"]==b"BEGIN_NOT_ENTERED" and values[b"a_arm_state"]==b"ARM_NOT_OBSERVED")
   refusal_ack(control,values,b"ARM_NOT_ENTERED",ready_deadline);context[b"owner_released"]=True;return
  begin=parse_packet(raw,b"V4_CONSUME_BEGIN",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"consume_origin_ns",b"consume_deadline_ns"))
  need(begin[b"state"]==b"CONSUME_BEGIN" and begin[b"ordinal"]==begin[b"probe"]==b"NONE" and begin[b"auth_id"]==AUTH)
  need(begin[b"a_begin_state"]==b"BEGIN_SEND_EFFECT_UNKNOWN" and begin[b"a_arm_state"]==b"ARM_NOT_OBSERVED")
  origin=udec(begin[b"consume_origin_ns"],1);deadline=udec(begin[b"consume_deadline_ns"],1)
  need(deadline==origin+CONSUMPTION_NS and time.monotonic_ns()<=deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  context[b"begin_observed"]=True;context[b"consume_origin"]=origin;context[b"consume_deadline"]=deadline
  context[b"consumption_state"]=b"ARM_SEND_EFFECT_UNKNOWN";context[b"arm_effect_possible"]=True
  armed=packet(b"V4_CONSUME_ARMED",((b"state",b"CONSUME_ARMED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"a_begin_state",b"BEGIN_SEND_EFFECT_UNKNOWN"),(b"b_arm_state",b"ARM_SEND_EFFECT_UNKNOWN"),(b"consume_origin_ns",str(origin).encode()),(b"consume_deadline_ns",str(deadline).encode())))
  send_exact(control,armed,deadline);context[b"consumption_state"]=b"ARM_SENT"
  try:
   raw,fds=recv_monitored(control,4,deadline,0);need(fds==())
   if raw.startswith(b"V4_REFUSE_PRECOMMIT|"):
    values=refusal_values(raw);need(values[b"a_begin_state"]==b"BEGIN_SENT" and values[b"a_arm_state"]==b"ARMED_CONFIRMED")
    refusal_ack(control,values,b"ARM_SENT",deadline);context[b"owner_released"]=True;return
   commit=parse_packet(raw,b"V4_CONSUME_COMMIT",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"a_commit_state",b"consume_origin_ns",b"consume_deadline_ns"))
   need(commit[b"state"]==b"CONSUME_COMMIT" and commit[b"ordinal"]==commit[b"probe"]==b"NONE" and commit[b"auth_id"]==AUTH)
   need(commit[b"a_begin_state"]==b"BEGIN_SENT" and commit[b"a_arm_state"]==b"ARMED_CONFIRMED" and commit[b"a_commit_state"]==b"COMMIT_SEND_EFFECT_UNKNOWN")
   need(udec(commit[b"consume_origin_ns"])==origin and udec(commit[b"consume_deadline_ns"])==deadline)
  except (ActorLost,RemoteAbort,CertificateExpired,FaultSet) as error:
   ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error);return
  context[b"consumed"]=True;context[b"consumption_state"]=b"COMMIT_RECEIVED"
  try:intent_sha=consume_attempt(context,cert_raw,envelope_raw,source_raw,deadline)
  except (CertificateExpired,FaultSet) as error:
   context[b"faults"].update(error.faults if isinstance(error,FaultSet) else {b"CERTIFICATE_EXPIRED"})
   terminal_failure(control,context,b"NONE",set(context[b"faults"]),False);return
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  consumed=packet(b"V4_CONSUMED_DURABLE",((b"state",b"CONSUMED_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"intent_sha256",intent_sha),(b"consume_origin_ns",str(origin).encode()),(b"consume_deadline_ns",str(deadline).encode()),(b"attempt_fd_state",context[b"local_fd_state"])))
  send_exact(control,consumed,deadline)
  stage_bind(control,context);containment_bind(control,context)
  for ordinal,probe in enumerate(PROBES):
   context[b"entered"]=ordinal+1;checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS)
   try:
    stream_arm(control,context,ordinal,probe);pidfd_arm(control,context,ordinal,probe);release_phase(control,context,ordinal,probe)
    actor_lost,faults,empty,stdout,stderr=monitor_probe(control,context,ordinal,probe)
    if actor_lost:raise ActorLost("probe")
    if faults:raise FaultSet(faults)
    validated_exchange(control,context,ordinal,probe,stdout,stderr)
    close_probe(context);checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS)
   except RemoteAbort as error:
    context[b"faults"].update(error.faults);terminal_failure(control,context,probe,set(context[b"faults"]),False);return
   except ActorLost:
    context[b"faults"].add(b"ACTOR_LOST");terminal_failure(control,context,probe,set(context[b"faults"]),True);return
   except CertificateExpired:
    context[b"faults"].add(b"CERTIFICATE_EXPIRED");terminal_failure(control,context,probe,set(context[b"faults"]),False);return
   except FaultSet as error:
    context[b"faults"].update(error.faults);terminal_failure(control,context,probe,set(context[b"faults"]),False);return
  preterminal_arrival_deadline=context[b"origin"]+TOTAL_NS;raw,fds=recv_monitored(control,4,preterminal_arrival_deadline,0);need(fds==())
  query=parse_packet(raw,b"V4_EMPTY_FINAL_QUERY",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_origin_ns",b"remove_deadline_ns"))
  remove_origin=udec(query[b"remove_origin_ns"],1);remove_deadline=udec(query[b"remove_deadline_ns"],1)
  need(query[b"state"]==b"EMPTY_FINAL_QUERY" and query[b"ordinal"]==query[b"probe"]==b"NONE" and query[b"chain_head_sha256"]==context[b"chain_sha"])
  need(remove_deadline==remove_origin+REPORT_NS and remove_origin<=time.monotonic_ns()<=remove_deadline)
  checkpoint(CERT,horizon_needed(remove_deadline,FINAL_TOTAL_NS),remove_deadline);need(observe_population(context) is False)
  confirmed=packet(b"V4_EMPTY_FINAL_CONFIRMED",((b"state",b"EMPTY_FINAL_CONFIRMED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",context[b"chain_sha"]),(b"remove_deadline_ns",str(remove_deadline).encode())))
  send_exact(control,confirmed,remove_deadline)
  raw,fds=recv_monitored(control,4,remove_deadline,0);need(fds==())
  removed=parse_packet(raw,b"V4_CGROUP_REMOVED",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"))
  need(removed[b"state"]==b"CGROUP_REMOVED" and removed[b"ordinal"]==removed[b"probe"]==b"NONE" and removed[b"chain_head_sha256"]==context[b"chain_sha"] and udec(removed[b"remove_deadline_ns"])==remove_deadline)
  try:os.stat(AUTH,dir_fd=6,follow_symlinks=False);need(False)
  except FileNotFoundError:pass
  context[b"removed"]=True;checkpoint(CERT,horizon_needed(remove_deadline,FINAL_TOTAL_NS),remove_deadline)
  ack=packet(b"V4_REMOVE_ACK",((b"state",b"REMOVE_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",context[b"chain_sha"]),(b"remove_deadline_ns",str(remove_deadline).encode())))
  send_exact(control,ack,remove_deadline)
  raw,fds=recv_monitored(control,4,remove_deadline,0);need(fds==())
  finalize=parse_packet(raw,b"V4_FINALIZE_CANDIDATE",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns"))
  terminal_origin=udec(finalize[b"terminal_origin_ns"],1);terminal_deadline=udec(finalize[b"terminal_deadline_ns"],1)
  need(finalize[b"state"]==b"FINALIZE_CANDIDATE" and finalize[b"ordinal"]==finalize[b"probe"]==b"NONE" and finalize[b"chain_head_sha256"]==context[b"chain_sha"])
  need(terminal_deadline==terminal_origin+FINAL_TOTAL_NS and terminal_origin<=time.monotonic_ns()<=terminal_deadline)
  context[b"terminal_origin"]=terminal_origin;context[b"terminal_deadline"]=terminal_deadline
  checkpoint(CERT,horizon_needed(terminal_deadline,0),terminal_deadline)
  need(context[b"entered"]==sum(context[b"committed"])==context[b"direct_reaps"]==context[b"stopped_count"]==15)
  need(context[b"stage_present"] and context[b"containment_bound"] and context[b"removed"] and not context[b"faults"] and context[b"kill_call_count"]==0 and context[b"kill_state"]==b"NOT_RESERVED")
  candidate_sha=final_candidate(context,terminal_origin,terminal_deadline)
  terminal_owner_loop(control,context,b"SUCCESS",b"SUCCESS_CANDIDATE",candidate_sha,b"PASS",terminal_deadline)
 except RemoteAbort as error:
  if pass_locked(context):
   context[b"faults"].update(error.faults);context[b"faults"].add(b"ACK_EFFECT_UNKNOWN")
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:
   context[b"faults"].update(error.faults);terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 except ActorLost:
  context[b"actor_lost"]=True
  if pass_locked(context):context[b"faults"].update((b"ACTOR_LOST",b"ACK_EFFECT_UNKNOWN"))
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,ActorLost("actor"))
  elif context[b"consumed"]:
   context[b"faults"].add(b"ACTOR_LOST");terminal_failure(control,context,b"NONE",set(context[b"faults"]),True)
  else:raise
 except CertificateExpired:
  if pass_locked(context):context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ACK_EFFECT_UNKNOWN"))
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,CertificateExpired("consume"))
  elif context[b"consumed"]:
   context[b"faults"].add(b"CERTIFICATE_EXPIRED");terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 except FaultSet as error:
  if pass_locked(context):context[b"faults"].update(error.faults|{b"ACK_EFFECT_UNKNOWN"})
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:
   context[b"faults"].update(error.faults);terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 except BaseException:
  error=FaultSet({b"INTERNAL_INVARIANT"})
  if pass_locked(context):context[b"faults"].update((b"INTERNAL_INVARIANT",b"ACK_EFFECT_UNKNOWN"))
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:
   context[b"faults"].add(b"INTERNAL_INVARIANT");terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 finally:
  if (context.get(b"begin_observed",False) or context[b"consumed"]) and not context[b"owner_released"]:
   context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")
   while not (context[b"actor_lost"] and context[b"outcome_durable"] and terminal_safe(context)):
    owner_poll(control,context,time.monotonic_ns()+50000000)
   context[b"owner_released"]=True
  close_probe(context)
  close_numbers(tuple(context.get(key,-1) for key in (b"root_events_fd",b"root_kill_fd",b"cgfd",b"stage_fd",b"attempt") if context.get(key,-1)>=0))
  close_numbers(tuple(number for number in (5,6) if number>=0))
  try:control.close()
  except BaseException:pass

try:
 main()
except BaseException:
 raise SystemExit(96)
raise SystemExit(0)

P27 RUNNER V4 WATCHDOG SOURCE END E6A1954C

## 15. Frozen source identities and structural census

A raw span is every byte after its BEGIN delimiter LF and before the LF that
introduces its END delimiter. The source's final LF is included; the blank
separator and delimiters are excluded. Exact raw slicing, wc, and sha256sum
give:

record                 absolute raw lines  bytes   LF    SHA256
A actor including C    511-1786            98510   1276  98aca253e14db32eb09837f142663c1d046bb341245194e6ac21f14f4978857f
C embedded validator   1020-1121           10195    102  7414e09dcdd09463f900a24dc19af9d3ecc9528c44895541fba7739fd7af9a89
B persistent watchdog  1791-3258          115781   1468  ed759a87c4abae0bf51f8e779cc400a3a00b09e9f020d936f5578369e30a0cb9

Delimiter locations are A BEGIN 510, A END 1788, C BEGIN 1019, C END
1122, B BEGIN 1790, and B END 3260. Each exact delimiter line occurs once.
C is one contiguous raw subspan of A. A constructs plan delimiter searches
from fragments, so an exact delimiter line is not duplicated inside source.

Raw neighborhood inspection finds zero column-zero def/class/try transition
without a preceding empty LF-delimited line. This is a raw byte inspection,
not tokenization or language parsing. Source byte class is LF plus ASCII
0x20..0x7e only; there are no CR, tab, NUL, or non-ASCII bytes.

A and B contain byte-identical 151-field CERT_KEYS, byte-identical 18-field
ENVELOPE_KEYS, and byte-identical 48-member FAULT_ORDER literals. Important
raw callsite counts are:

operation                                      A   B
persistent os.fork call                        1   0
raw clone3 syscall call                        1   0
os.execve call                                 2   0
central os.waitpid call                        1   0
direct os.kill SIGSTOP call                    1   0
payload os.kill SIGCONT call                   1   0
os.mkdir call                                  2   1
recvmsg intake definition                      1   1
send_rights definition/calls                   1/4 0/0
durable_once definition/calls                  0/0 1/12
direct cgroup.kill os.write call               0   1
terminal_owner_loop definition/calls           0/0 1/2
parse_final_report definition/calls            0/0 1/2

The four A rights transfers are streams, OUTER pidfd, stage dirfd, and child
cgroup dirfd. The twelve B durable callsites are intent, release, validated
receipt, ACK-intent receipt, kill ticket, retained state, recovery/preintent,
failure report, final candidate, terminal-seen, PASS report, and outer
reconciliation. Failure and PASS both traverse the one exact report parser.
The one direct kill write is inside kill_once; all textual kill_once callsites
are guarded by the monotone NOT_RESERVED state.

Any mismatch in a source byte, LF, hash, delimiter, location, certificate
census, or callsite census is INPUT_AUTH. A future carrier must reproduce
the frozen raw spans exactly.

## 16. E0367 correction closure matrix

rule  exact V4 closure
1     Fresh V4 path, domains, delimiters, source identities, and author stop.
2     A marks BEGIN effect unknown before send; B marks ARM effect unknown
      before send; only an exact session/state/deadline refusal ACK is clean.
3     Attempt FD remains LOCAL_UNVERIFIED until named/held/access/identity
      checks, then LOCAL_VERIFIED, then atomically PUBLISHED.
4     Collision closes the mutation-capable attempt base and reports only
      through the separately certified control/survival capability.
5     Every SCM_RIGHTS integer and every local stage/cgroup/mount/dependency
      FD enters exhaustive immediate cleanup and transfers individually.
6     One A-origin consumption deadline covers BEGIN through intent and ACK;
      no helper, mkdir, open, fsync, durable record, or receive restarts it.
7     One inherited cleanup cap contains ticket creation, kill-call entry,
      write return, postcheck, population observation, and retained transfer.
8     Possible payload release consumes the sole kill authority on first
      failure even when population is unobservable; no second kill exists.
9     One fresh terminal deadline covers candidate, seen record, PASS,
      margin, ACK, A receipt, reconciliation, and B OWNER_CLOSED.
10    PASS or ACK effect unknown remains authoritative no-replay; conflicting
      ABORT cannot downgrade it, and missing ACK enters reconciliation.
11    B owns success, failure, actor-loss, and frozen-transfer terminal paths;
      terminal_owner_loop continuously polls control, pidfds, and containment.
12    Every certified boundary resamples realtime/monotonic clocks and active
      absolute deadline while retaining the original typed causal fault.
13    Each host-complete-to-ACK interval is at most 500000000 ns and contains
      both durable validated and ACK-intent receipts.
14    B mirrors A's full certificate/envelope/dependency/gate/credential
      relations and independently binds stage/cgroup bases and capabilities.
15    Common header, packet-specific tuples, ABORT, fault set, ancillary
      language, transcript language, structure, and semantics are disjoint.
16    Candidate, success, failure, kill, stage, attempt, containment, reap,
      receipt, ACK, disposition, and retry tuples are cross-consistent.
17    Each acquisition starts inside an owner cleanup scope; stage presence is
      asserted only after exact held-base and four-leaf verification.
18    All six missing external premises remain named launch blockers; static
      source authorship cannot make them executable or manifest-eligible.

## 17. Separated formal static review protocol

The V4 author and every E0367 prebind/advisory participant are permanently
disqualified from both formal reviews. The two reviewers must be fresh and
distinct. Neither reviewer may contact the other or inspect the other's
work product before both immutable review stops exist.

Formal Scope S is source/staging/parser/certificate only. It covers exact
V4/A/C/B extraction and identities, E0366 and V15 carriers, fd/seal/access
laws, four leaves, dependency/certificate/envelope/gate census, P00,
P01D-to-P01C index 9 and libc uid/gid, P05 reuse, transcript-only topology,
RESULT/frame/control/ABORT/SCM_RIGHTS/pidfd grammar, report union, and the
raw source/prose census. Its only permitted terminals are:

PASS=BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V4_SOURCE_STATIC_REVIEW_PASS_BOUND_NO_EXECUTION
FAIL=BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V4_SOURCE_STATIC_REVIEW_FAIL_NO_EXECUTION

Formal Scope L is lifecycle/containment/consumption/durability/clock/deadline
and outer-launcher only. It covers dual BEGIN/ARM ambiguity, refusal proof,
one consume horizon, FD ownership, parent/top-process watchdog, serial
nonreuse, cleanup/kill cap, actor/B survival, stream drainage, clock and
expiry arithmetic, removal deadline, common terminal deadline, PASS/ACK
unknown effects, reconciliation, OWNER_CLOSED, external transfer, exits, and
effect boundary. Its only permitted terminals are:

PASS=BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V4_LIFECYCLE_STATIC_REVIEW_PASS_BOUND_NO_EXECUTION
FAIL=BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V4_LIFECYCLE_STATIC_REVIEW_FAIL_NO_EXECUTION

A PASS is bound to the final whole-file identity and all three raw source
identities. Any mismatch is a formal FAIL, not a request to edit. Reviewers
have zero write, test, validator, execution, manifest, gate, premise, issuer,
or release authority.

Only two exact PASS stops may support a later ledger recommendation:

DUAL_PASS=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V4_DUAL_STATIC_REVIEW_PASS_BOUND_NO_EXECUTION

Either formal FAIL instead supports only:

DUAL_FAIL=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V4_STATIC_REVIEW_FAIL_NO_EXECUTION

Even dual PASS remains no-execution. Manifest eligibility additionally
requires all six exact external prerequisites, an authenticated unexpired
issuer reservation, exact sealed carriers, an authorized outer launcher and
survival transfer, independent gate reviews, and a later explicit ledger
event. No reviewer or manifest actor may infer any missing premise from
certificate PASS fields.

## 18. Author effects and stop boundary

During V4 authorship the only filesystem mutation was apply_patch creation
and update of this exact fresh V4 path. V1, V2, V3, the ledger, manifest,
Host, Binder, actor, derivation, validator, papers, and every other byte were
preserved. No temporary, cache, log, backup, lock, swap, redirect, generated
carrier, evidence leaf, or auxiliary file was created or modified.

No source literal was imported, tokenized, AST- or language-parsed,
compiled, evaluated, executed, launched, microtested, or passed to a
validator. Only exact-path raw reads, raw textual transforms, wc,
sha256sum, stat, byte-class inspection, and apply_patch on this target were
used. No build/evidence/root, including the prohibited recovery evidence
tree, was listed, stated, opened, traversed, or accessed.

This plan remains non-executable because its external prerequisites are
unresolved. Author stop grants no manifest, formal-review, test, premise,
issuer, gate, execution, payload, build, evidence-root, PDF, release, or
publication authority. The unique EOF token below declares inert V4
author-stop only.
BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V4_AUTHOR_STOP
