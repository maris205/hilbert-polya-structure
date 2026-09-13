# Paper 27 E001 supervisor Host runtime plan recovery V3

Status: E0366-authorized inert Runner V3 author control. This document grants
zero prebind, formal-review, manifest, microtest, execution, build,
evidence-root, payload, PDF, release, or publication authority.

All literal source records below are inert 7-bit ASCII/LF bytes. During V3
authorship they are never imported, tokenized as a language, AST-parsed,
compiled, evaluated, executed, launched, microtested, or sent to a validator.

## 1. Sole authority and immutable inputs

The sole authorizing record is the exact author-stopped E0366 historical
snapshot:

snapshot_name=B07_E0366_AUTHOR_OPEN
bytes=2303269
LF=23672
SHA256=0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92
terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V2_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V3_AUTHOR_OPEN_NO_EXECUTION

The mutable current ledger pathname is not a runtime identity. A later
append necessarily changes that regular file. Future prebind and execution
may therefore use E0366 only through an anonymous sealed historical-snapshot
carrier. That carrier must contain exactly the bytes above, have exactly the
LF count and unique terminal above, be a regular memfd with nlink zero and
exact seals F_SEAL_WRITE, F_SEAL_GROW, F_SEAL_SHRINK, and F_SEAL_SEAL, and
be bound by both the premise certificate and issuer envelope. A current
ledger dev, ino, size, or hash comparison is forbidden. Creation of the
carrier is not authorized here; a later ledger event must explicitly
authorize its exact construction and independently reproduce its raw
identity before launch.

The frozen Host V15 input remains:

path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15.md
dev=2431
ino=5916064615
mode=0644
nlink=1
uid=0
gid=0
bytes=228310
LF=4622
SHA256=a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845
terminal=BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15_AUTHOR_STOP

The exact V8 transcript semantics hash is
72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf.
Frozen failed Runner V1 and Runner V2 are immutable history. Runner V2 is:

path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V2.md
dev=2431
ino=5916064581
mode=0644
nlink=1
uid=0
gid=0
bytes=148074
LF=2600
SHA256=cb68357d1765723607187b057214832b53eb98d3d959aeace6570d9ebf530620
terminal=BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V2_AUTHOR_STOP

No V1 or V2 byte is execution authority. The ledger, manifest, V1, V2,
Host V15, Host V8, Binder, validator, actor V3, derivation V6, every paper,
and every build/evidence/root are immutable and inaccessible to this
authorship except the exact reads expressly allowed by E0366.

The five Host V15 raw source identities are:

source   bytes  LF    SHA256
OUTER    87151  1840  cfa1d88b312b7f4425778018be39cf7628568c9ddb39c697ff12b8b0f1c8be1a
KEEPER    4216   128  e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716
LAUNCHER  4218   128  e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5
MARKER   75094  1479  b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d
CHILD    19746   452  1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf

MARKER's embedded CHILD span must be byte-equal to standalone CHILD.

## 2. Non-executable unresolved gates

Three matters remain explicitly unresolved and prevent launch even after a
future static PASS:

1. raw clone3 continuation through CPython;
2. issuer signature-preimage, key, serial reservation, replay, and exact
   reserved-versus-consumed state semantics;
3. deleted-cgroup open-directory and open-cgroup.events observation
   semantics.

The premise certificate contains separate nonzero gate IDs and PASS=1 fields
for the clone3/CPython and deleted-cgroup gates, but those fields are only
references. They are not self-certification. No gate artifact exists or is
authorized by this file. Each needs separately authorized, no-build,
synthetic evidence with an exact identity and separated review. Static V3
authorship grants no test or execution.

## 3. Exact future supervisor entry contract

A later separately authorized supervisor may launch exactly one A process
and no payload directly. It must authenticate the issuer envelope
externally, construct sealed A, B, plan, certificate, envelope, and E0366
snapshot memfds, pin the exact Host V15 regular file, and then exec:

interpreter=/root/miniconda3/bin/python3
interpreter_flags=-I -S -B -P -X utf8
source=/proc/self/fd/100
sys.argv=[/proc/self/fd/100,RUN_V3,AUTH_ID]
cwd=certificate-bound safe-bind base
umask=0077
stdin=authenticated empty pipe
stdout=distinct raw result pipe
stderr=distinct raw diagnostic pipe

The exact environment has ten keys and no others:

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

A receives only:

fd100 sealed V3 A source
fd101 sealed exact E0366 historical snapshot carrier
fd102 exact Host V15 regular file
fd103 sealed complete V3 plan
fd104 sealed premise certificate
fd105 sealed issuer envelope
fd106 sealed V3 B source

Descriptors 3 through 99 and 107 through UINT_MAX are closed. A freshly
requires exact equality of the expected open-FD set, not merely absence of
extras. Its parent retains a pidfd, directly waits A exactly once, never
releases a payload, and on its separately authorized hard deadline may
signal only A through that pidfd. B, not the parent, remains the containment
and terminal owner after consumption.

A entry credentials are exactly uid/euid/suid and gid/egid/sgid zero,
empty supplementary groups, umask 0077, CapInh and CapAmb zero,
CapPrm=CapEff=CapBnd=00000000000401c0, NoNewPrivs=0, and SecureBits=12.
The four set bits are CAP_SETGID, CAP_SETUID, CAP_SETPCAP, and
CAP_SYS_CHROOT. Each B or OUTER child chroots first, fixes cwd, ids, groups,
umask, rlimits, signals and timers, locks securebits, drops every bounding
capability, clears every capability set, sets NoNewPrivs=1, and freshly
requires CAPS_EMPTY and SecureBits=15 before execve.

The fixed rlimit vector is the literal normalize_limits vector in A. All
catchable dispositions are SIG_DFL, the signal mask and pending set are
empty, and the three interval timers are zero. The certificate separately
binds no signal delivery, no asynchronous transfer, no timer delivery, no
trace/profile/audit hook, and no concurrent mutator.

## 4. Suite, caps, and integrated clock law

SUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
SUITE_CARDINALITY=15
AUTHORIZED_INVOCATION_SLOTS=15
OPERATIONAL_BUDGET_NS=15000000000
ACTOR_LAUNCH_PROGRESS_NS=1000000000
POST_OPERATION_HOST_BOUND_NS=1664800000
ACTOR_ACK_PROGRESS_NS=500000000
RELEASE_THROUGH_ACK_CAP_NS=18164800000
CONTAINMENT_CLEANUP_CAP_NS=2000000000
SIGCONT_CALL_RETURN_NS=5000000
PRECONSUMPTION_CAP_NS=10000000000
CONSUMPTION_PROGRESS_NS=100000000
ATTEMPT_DIRFD_PROGRESS_NS=100000000
STAGING_CAP_NS=10000000000
DURABLE_RECORD_PROGRESS_NS=100000000
WATCHDOG_ARM_PROGRESS_NS=1000000000
WATCHDOG_ACK_PROGRESS_NS=500000000
FINAL_REPORT_PROGRESS_NS=1000000000
FINAL_PASS_COMMIT_PROGRESS_NS=100000000
FINAL_PASS_MARGIN_NS=10000000
TERMINAL_HANDSHAKE_PROGRESS_NS=500000000
CERTIFICATE_ABSOLUTE_LIFETIME_NS=360000000000
ENTRY_MIN_REMAINING_NS=293472000000
CONSUMPTION_MIN_REMAINING_NS=283472000000
STDOUT_CAP_BYTES=3145728
STDERR_CAP_BYTES=3145728

Fifteen times 18164800000 is 272472000000. Every A and B certificate
checkpoint takes monotonic-before, realtime, monotonic-after, validates the
certificate's realtime/monotonic binding with at most 1000000 ns drift,
validates absolute life and the required remaining work, and validates any
active monotonic deadline. No realtime-only checkpoint exists.

Every certified progress operation has a literal pre-entry reservation and
a literal post-return monotonic plus integrated-clock check. This includes
consumption preparation and commit, immediate attempt-dirfd acquisition,
staging mkdir/open/write/fsync, every recvmsg and ACK, durable records,
watchdog arm, release record, SIGCONT entry and return, capture completion,
cleanup, terminal candidate, terminal-seen receipt, final report commit, and
terminal ACK. A receive or syscall return after its horizon is a fault even
when the underlying call returned success.

No slot, cleanup cap, certificate, or clock origin restarts. First sticky
failure closes all later slots. There is no retry, resume, repair, skip,
replacement slot, second suite, certificate refresh, or cleanup-to-success
transition.

## 5. Sealed certificate and issuer envelope

AUTH_ID is 64 lowercase hex and equals
SHA256("P27E001V3 NUL" || certificate || NUL || issuer-envelope).
AUTH_ID is also the collision-safe static leaf name below each fixed base.
No process creates, signs, refreshes, or approves the certificate or
envelope.

Both A and B parse the full exact ordered certificate grammar and every DEP
row. B does not accept a subset. Both require exact values, canonical
decimal/octal/hex, unique ordered keys, contiguous DEP indexes, unique
role/path pairs, the six mandatory singleton roles, the complete dependency
closure, exact E0366 snapshot fields, exact V15/V8 fields, both capability
phases, all progress constants, distinct cgroup-base and cgroup-child facts,
and both unresolved gate references. A additionally reopens and rehashes
every dependency through held no-follow components.

The envelope header is P27E001_ISSUER_ENVELOPE_V3 and its exact ordered keys
are ISSUER_ID, ISSUER_KEY_ID, AUTHORIZATION_SERIAL,
CERTIFICATE_SHA256, PLAN_SHA256, RUNNER_SHA256, RECOVERY_SHA256,
E0366_SNAPSHOT_BYTES, E0366_SNAPSHOT_LF, E0366_SNAPSHOT_SHA256,
E0366_SNAPSHOT_TERMINAL_HEX, V15_SHA256, NOT_BEFORE_REALTIME_NS,
NOT_AFTER_REALTIME_NS, ONE_SHOT_RESERVED_BY_ISSUER,
ONE_SHOT_CONSUMED_BY_ISSUER, SIGNATURE_ALGORITHM, SIGNATURE_HEX,
followed by ENVELOPE_END=1.

The certificate header is P27E001_PREMISE_CERTIFICATE_V3 and exact
CERTIFICATE_END=1 terminates it. The literal CERT_KEYS tuples in A and B are
the complete authoritative field order. Important distinct fields include:

E0366_SNAPSHOT_BYTES=2303269
E0366_SNAPSHOT_LF=23672
E0366_SNAPSHOT_SHA256=0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92
HISTORICAL_SNAPSHOT_SEALED=1
CGROUP_BASE_TYPE_HEX
CGROUP_BASE_CONTROLLERS_HEX
CGROUP_BASE_SUBTREE_CONTROL_HEX
CGROUP_CHILD_MODE=40700
CGROUP_CHILD_UID=0
CGROUP_CHILD_GID=0
CGROUP_CHILD_TYPE_HEX=646f6d61696e0a
CGROUP_CHILD_CONTROLLERS_HEX
CGROUP_CHILD_SUBTREE_CONTROL_HEX
CLONE3_CPYTHON_GATE_ID=H64_NONZERO
CLONE3_CPYTHON_GATE_PASS=1
DELETED_CGROUP_FD_GATE_ID=H64_NONZERO
DELETED_CGROUP_FD_GATE_PASS=1

Issuer authenticity, replay exclusion, and the meaning of the two one-shot
fields remain external trust boundaries. A and B only parse and bind bytes.

## 6. Persistent B and collision-safe bootstrap

A forks exactly one B before CONSUME_BEGIN. A first parks every B source FD
with F_DUPFD_CLOEXEC at or above 200, proves all parked FDs distinct from
every target, maps only parked copies, closes the parking bank, and performs
complete close_range scrubbing. Sequential dup2 source destruction is
impossible.

B receives exactly:

fd0 authenticated empty pipe, read-only
fd1 closed
fd2 closed
fd3 A/B SOCK_SEQPACKET, read/write, exact peer credentials
fd4 actor pidfd, poll-only, exact fdinfo Pid binding
fd5 held attempts base, read-only directory, exact certificate identity
fd6 held cgroup base, read-only directory, exact certificate identity
fd7 sealed certificate memfd
fd8 sealed issuer-envelope memfd
fd9 sealed exact E0366 historical-snapshot memfd
fd100 sealed V3 B source memfd

B uses the same interpreter flags and environment, argv0
/proc/self/fd/100, action RECOVER_V3, and the safe-bind base cwd. Before
V3_READY it reparses every certificate and dependency field, checks the
envelope and AUTH_ID, checks the snapshot by bytes/LF/SHA/terminal without
dev/ino, verifies exact FDs, credentials, rlimits, signals, bases,
cgroup-base type/controllers/subtree-control, and all seals. It then remains
one persistent process until clean refusal or its unique durable terminal
report plus terminal closure. It has no source extraction, staging, fork,
clone, exec, SIGCONT, semantic transcript parser, waitpid/waitid, retry,
resume, repair, or release path.

## 7. Consumption edge and attempt FSM

Before any namespace or payload effect, B sends V3_READY. A sends
V3_CONSUME_BEGIN; B checks the integrated clock and replies
V3_CONSUME_ARMED. A may still refuse only by sending
V3_REFUSE_PRECOMMIT and receiving V3_REFUSE_ACK.

Immediately before the first sendmsg/send call that may deliver
V3_CONSUME_COMMIT, A irreversibly sets its local state to
CONSUME_EFFECT_UNKNOWN, consumed=true, and PREFLIGHT=false. From that
instruction onward A has no REFUSE branch. Send failure, ACK loss, HUP,
timeout, or actor exception is consumed indeterminate unless B proves the
exact durable successor.

After B has sent V3_CONSUME_ARMED, clean V3_REFUSE_PRECOMMIT is the only
nonconsuming terminal. COMMIT receipt starts consumption. Actor loss,
timeout, malformed control, or ambiguous HUP before a clean refusal also
moves B to CONSUME_EDGE_UNKNOWN and the issuer serial becomes permanently
nonreusable. B may then establish the attempt namespace solely to preserve a
durable recovery owner; it can never release or exec.

The attempt FSM is monotone:

ARMED
-> MKDIR_CALL_ENTERED
-> MKDIR_RETURNED_CREATED or MKDIR_EFFECT_UNKNOWN or COLLISION
-> IMMEDIATE_DIRFD_CALL_ENTERED
-> DIRFD_PUBLISHED or DIRFD_EFFECT_UNKNOWN
-> BASE_FSYNC_EFFECT_UNKNOWN
-> BASE_DURABLE
-> INTENT_RECORD_PARTIAL
-> INTENT_DURABLE

After successful mkdir return, the very next fallible operation is the
no-follow open of AUTH_ID. On return B publishes that dirfd in the shared
context before base fsync or any record operation. If the immediate open is
unknown, B never repeats mkdir; it remains the nonreusable owner and performs
only no-follow observation/open of the already named directory until it can
publish a verified dirfd or the separately frozen B-survival premise fails.
Every mkdir, collision, fsync, open, and intent partial-effect branch has an
explicit retained state. No branch calls the authorization reusable.

## 8. Staging, cgroup, clone, and release

Only A extracts V15 spans by unique raw delimiters and exact triples. Within
one nonrestarting staging deadline it creates stage/AUTH_ID mode0700 and
exactly keeper.py, launcher.py, marker.py, and child.py with
O_EXCL|O_NOFOLLOW mode0400, same-FD reread, exact raw identity, file fsync,
and directory fsync. OUTER is a sealed anonymous memfd. No source is
normalized.

A creates cgroup/AUTH_ID once, holds it no-follow, and requires root/root,
octal 040000 directory type plus 0700 permissions (certificate octal
40700), the exact distinct child type/controllers/subtree-control bytes, and
populated zero. B independently compares the SCM_RIGHTS dirfd, the named
child, exact dev/ino/mode/nlink/uid/gid, exact child files, and its separately
checked base facts before V3_CONTAINMENT_ACK.

For every ordinal, A first transfers stdout-read, stderr-read,
cgroup.events-read, and cgroup.kill-write in one exact four-rights
V3_STREAM_ARM packet. B validates each installed FD and acknowledges before
clone3. A then performs its sole raw clone3 call with
CLONE_INTO_CGROUP|CLONE_PIDFD. The direct OUTER child performs SIGSTOP as
its only pre-context action. A directly observes exact stopped status and
exact cgroup.procs membership, then transfers the OUTER pidfd. B sets
pidfd_bound=1 only after fdinfo Pid, stopped state, and membership checks.
pidfd_exit_ready_observed remains a separate false state until poll reports
exit readiness; it is never inferred from binding.

B durably writes a release record chained to the intent or preceding ACK
record. A receives its SHA. Immediately before SIGCONT, A performs an
integrated certificate/deadline checkpoint and requires
call_entry+5000000<=launch_deadline. It performs one SIGCONT call and checks
both call return and a new integrated checkpoint before any direct wait.
Unknown release effect is permanent indeterminate.

A alone performs the one direct OUTER final wait. Before its first waitpid
call entry it sets DIRECT_REAP=UNKNOWN. Only the exact successful return
changes it to COMPLETE. EINTR may repeat the same in-progress wait operation,
but exception, deadline, lost return, or unavailable status stays
DIRECT_WAIT_UNKNOWN and is never mapped to OUTER_STATUS. A known nonzero raw
status is separately OUTER_STATUS. B never claims reaping.

## 9. Seqpacket, dynamic rights, and capture law

Every SOCK_SEQPACKET receive in A and B, including expected-zero-rights
messages, uses recvmsg. The ancillary buffer is large enough to receive and
close every permitted maximum FD. MSG_TRUNC, MSG_CTRUNC, malformed ancillary,
unexpected ancillary, multiple rights items, wrong rights count, wrong
packet order, and post-return deadline failure are distinct closed faults.
Every installed FD is closed on every exceptional path.

V3_ABORT is accepted in every protocol receive state before the expected
packet is interpreted. It carries sender, state, ordinal, probe, and the
complete ordered sticky fault set. An ABORT with rights is rejected after all
installed FDs are closed. Receivers preserve every received sticky fault and
never replace it with a generic higher-priority phase label.

On a poll result containing both POLLIN and POLLHUP/POLLERR, the receiver
first performs exactly one recvmsg and processes that queued packet. HUP or
ERR is classified only afterward when no exact queued packet was returned.
This rule applies to terminal messages as well as ordinary ACKs.

B concurrently drains stdout and stderr through EOF, retains at most
3145728 bytes per stream while continuing discard after overflow, observes
cgroup.events, actor pidfd, and OUTER pidfd, and uses one host deadline.
V3_RESULT contains separate pidfd_bound and pidfd_exit_ready_observed,
lengths, hashes, EOF bits, exact frame counts, the ordered fault set, and
capture completion time. Frames are exactly all STDOUT frames by increasing
index, then all STDERR frames by increasing index, then V3_RESULT_END.
Each frame carries stream, index, byte count, and frame SHA before its raw
payload. A rejects any missing, duplicate, reordered, over-cap, or trailing
frame.

C first checks the complete transcript byte language, then its exact
semantics. TRANSCRIPT_LANGUAGE and TRANSCRIPT_SEMANTICS are separate sticky
faults. C uses the frozen Host V15 tag and rows, reconstructs P00 synthetic
SHA from authenticated CHILD, permits the specified sequential numeric PID
reuse in P05 and P10, and makes no unsupported SID/PGID topology claim.
The corrected embedded C return indentation is part of the fresh V3 bytes.

## 10. Monotone durable objects and receipt chain

For every exclusive object B records this in-memory partial-durability FSM:

ABSENT_KNOWN
-> OPEN_EFFECT_UNKNOWN
-> FD_HELD
-> WRITE_EFFECT_UNKNOWN
-> FILE_FSYNC_EFFECT_UNKNOWN
-> SAME_FD_REREAD_VERIFIED
-> DIR_FSYNC_EFFECT_UNKNOWN
-> DURABLE_VERIFIED

The state is published before each fallible effect and advances only after
the exact return and post-return deadline check. A basename is attempted at
most once. A partial object is never replay permission. Record errors are
sticky but cannot terminate B before containment ownership is closed.

The chain starts at intent.v3. Each release record names the predecessor SHA.
The validated receipt names the release SHA and contains AUTH_ID, record
sequence, ordinal/probe, all release/capture/direct-wait/raw-status,
pidfd-bound/pidfd-exit-ready, stdout/stderr length/hash/EOF/overflow,
cgroup-empty, parser-language, parser-semantics, candidate/terminal,
certificate-expiry, and actor/B timestamp fields. The ACK-intent receipt
names the validated SHA and repeats the complete forensic binding plus actor
ACK-intent time, B receive time, record origin/deadline, and certificate
sample. Its exact durable SHA is the next predecessor. No in-memory
COMMITTED bit is set before both receipts are DURABLE_VERIFIED and a fresh
integrated checkpoint passes. Loss after that bit stops the suite but cannot
erase or replay the slot.

No per-probe object contains DISPOSITION=PASS. Probe state names are
VALIDATED_CANDIDATE and ACK_COMMIT_INTENT only.

## 11. One cleanup origin, one kill, and retained ownership

The first sticky fault stores cleanup_origin exactly once and derives
cleanup_deadline=cleanup_origin+2000000000. Every later failure path reuses
those values. No monitor, terminal function, or exception handler restarts
the cap.

If populated, B reserves one kill permission in memory, begins
kill-ticket.v3 once, records its partial durability state, and proceeds even
if ticket durability is unknown. Ticket presence is never replay authority.
Immediately before the only direct os.write(cgroup.kill,"1 LF") call B sets
KILL_CALL_COUNT=1 and KILL_STATE=CALL_ENTERED. The call-entry reservation and
return are bounded by CGROUP_KILL_WRITE_RETURN_NS=5000000 and a post-return
integrated checkpoint. It never retries EINTR, short return, exception, lost
return, missing FD, ticket collision, actor loss, or timeout. No PID, PGID,
process-tree, second ticket, or fallback signal exists.

At the cleanup cap B records RETAINED_INDETERMINATE if possible and remains
the owner. Recoverable cgroup.events or record errors add sticky faults and
do not make it exit. It continues drain and observation without another
kill until populated zero. If final-report durability is partial or unknown,
B remains alive even after empty; only an explicitly frozen external
B-survival-premise failure can explain loss of that owner.

DIRECT_REAP is COMPLETE only from A's exact receipt, UNKNOWN after a direct
wait call with unavailable result, and UNAVAILABLE_ACTOR_LOST when A died
before providing the fact. A physical empty cgroup never upgrades UNKNOWN or
UNAVAILABLE to COMPLETE.

## 12. Final candidate, exact reports, and terminal handshake

Failure and success grammars are disjoint. A failure report requires a
nonempty ordered FAULT_SET, PRIMARY equal to its highest-precedence member,
and DISPOSITION equal to CONSUMED_FAIL or CONSUMED_INDETERMINATE. PRIMARY=NONE
is forbidden.

A success path first writes final-candidate.v3 with ELIGIBLE=1 and no PASS
disposition. It binds all fifteen durable ACK receipt hashes, the chain head,
direct reap complete, cgroup empty and removed, zero kill calls, live
certificate, timing samples, and all gates. B sends
V3_TERMINAL_CANDIDATE_DURABLE with its hash. A checks it and sends
V3_TERMINAL_SEEN. B drains that packet before HUP and durably writes the
terminal-seen receipt chained to the candidate.

Only after every terminal precondition above does B enter the final PASS
commit. Immediately beforehand it requires remaining certificate life of
FINAL_PASS_COMMIT_PROGRESS_NS+FINAL_PASS_MARGIN_NS and establishes a
monotonic commit deadline. The final O_EXCL report.v3 operation is covered
by the externally certified progress premise, checks every syscall return,
and performs file fsync, same-FD reread, attempt-dir fsync, and a post-return
integrated checkpoint with the strict positive margin. This is the sole
immutable PASS creation.

The exact PASS grammar is:

P27E001_FINAL_REPORT_V3
AUTH_ID=H64
SUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
ENTERED_COUNT=15
COMMITTED_COUNT=15
STOP_PROBE=NONE
PRIMARY=NONE
FAULT_SET=NONE
CHAIN_HEAD_SHA256=H64
TERMINAL_SEEN_SHA256=H64
DIRECT_REAP=COMPLETE
CGROUP_EMPTY=1
CGROUP_REMOVED=1
KILL_CALL_COUNT=0
KILL_STATE=NOT_RESERVED
CERTIFICATE_LIVE_AT_COMMIT=1
PASS_COMMIT_ORIGIN_MONOTONIC_NS=UDEC
PASS_COMMIT_DEADLINE_MONOTONIC_NS=UDEC
FINAL_PASS_MARGIN_NS=10000000
STAGE_RETAINED=1
ATTEMPT_RETAINED=1
RETRY_ALLOWED=0
DISPOSITION=PASS
REPORT_END=1

PRIMARY=NONE is admitted only by this complete conjunction. All failure
forms use a separate exact constructor and parser branch.

After report.v3 reaches DURABLE_VERIFIED, B sends
V3_TERMINAL_ACK with the candidate, terminal-seen, and report hashes. A
processes queued POLLIN before HUP and does not close fd3 until that exact
ACK. B remains terminal owner until the ACK send returns or actor-loss
closure is established. A then directly waits B and emits its one raw
success line. No PASS can be created after any sticky fault.

## 13. Fault order, crash partitions, and STOP law

The exact highest-first fault order is the literal FAULT_ORDER tuple in both
sources. It separately names input, entry, certificate, preconsumption,
consume-edge, attempt collision/namespace/dirfd/base/intent, actor loss,
expiry, staging, containment, malformed/timeout/truncated control,
FD transfer, stop-wait, pidfd binding, launch, release-record and release
effect, watchdog, kill-ticket and kill effect, capture I/O and overflow,
stderr, direct-wait, known outer status, transcript language and semantics,
validated and ACK durability, cgroup observation/nonempty, final-candidate,
terminal-seen, report durability, and internal invariant faults. Generic
exception handling may add INTERNAL_INVARIANT only when no typed sticky
fault exists; it may not replace or outrank a known set.

Crash partitions are exhaustive:

1. Before B sends V3_CONSUME_ARMED, either actor may close with no write.
2. After armed but before A's commit edge, only the exact refusal/ACK pair is
   unconsumed. Loss without that pair is CONSUME_EDGE_UNKNOWN.
3. From A's local commit edge onward REFUSE is absent. B consumes or retains
   unknown, establishes/pursues the attempt dirfd, and never releases on
   ambiguity.
4. At every attempt partial state B owns nonreuse and recovery. A loss cannot
   interrupt B.
5. Before STREAM_ARM no payload exists. After STREAM_ARM, B owns events and
   kill even if clone or pidfd handoff loses its return.
6. Clone return unknown, stopped wait unknown, pidfd transfer unknown,
   release record unknown, SIGCONT unknown, direct wait unknown, capture,
   parser, either receipt, cgroup removal, candidate, terminal-seen, and
   final commit each have a distinct sticky terminal partition.
7. B or kernel loss violates the external survival premise and is never
   locally reclassified reusable.
8. No terminal state returns to staging, clone, release, exec, another slot,
   kill, or PASS.

B alone creates attempt intent, release/receipt/recovery/ticket/candidate,
terminal-seen, and final-report objects. A alone stages, clones, SIGCONTs,
directly waits OUTER, and runs C. B cannot release or exec; A cannot write
the attempt directory or kill the cgroup.

## 14. Future effect and access boundary

A later explicitly authorized run may affect only:

1. attempts/AUTH_ID and the exact V3 intent, release, validated, ACK-intent,
   recovery, kill-ticket, retained, final-candidate, terminal-seen, report,
   and optional post-empty leaves;
2. stage/AUTH_ID and exactly keeper.py, launcher.py, marker.py, child.py plus
   the frozen V15 target/a/b safe-bind effects;
3. cgroup/AUTH_ID membership metadata and at most one two-byte cgroup.kill
   write;
4. anonymous sealed memfds, pipes, pidfds, and SOCK_SEQPACKET traffic.

No other regular file, temporary, cache, log, backup, lock, swap, symlink,
pathname socket, FIFO, redirected capture, tee, manifest, workspace, build,
evidence, paper, PDF, or release write is permitted. No source names or can
reach a build/evidence/root. This authoring performs none of those future
effects.

## 15. Inert literal source records

The following three records use fresh V3 domains and delimiters. C is a
uniquely delimited contiguous subspan of A. Source identities are frozen in
the post-source census after the final byte content is complete.

P27 RUNNER V3 ACTOR SOURCE BEGIN 91C4B7E3
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
CERT_LIFE_NS=360000000000
ENTRY_REMAIN_NS=293472000000
CONSUME_REMAIN_NS=283472000000
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

FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"CONSUME_EDGE_UNKNOWN",b"ATTEMPT_COLLISION",b"ATTEMPT_NAMESPACE_UNKNOWN",b"ATTEMPT_DIRFD_UNKNOWN",b"ATTEMPT_BASE_DURABILITY_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"CONTROL_MALFORMED",b"CONTROL_TIMEOUT",b"CONTROL_TRUNCATION",b"FD_TRANSFER",b"STOP_WAIT_UNKNOWN",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_TICKET_DURABILITY_UNKNOWN",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_IO",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"DIRECT_WAIT_UNKNOWN",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_SEMANTICS",b"VALIDATED_DURABILITY_UNKNOWN",b"ACK_DURABILITY_UNKNOWN",b"CONTAINMENT_OBSERVATION_UNKNOWN",b"CONTAINMENT_NOT_EMPTY",b"RECOVERY_DURABILITY_UNKNOWN",b"RETAINED_DURABILITY_UNKNOWN",b"REPORT_CANDIDATE_DURABILITY_UNKNOWN",b"TERMINAL_SEEN_DURABILITY_UNKNOWN",b"REPORT_DURABILITY_UNKNOWN",b"INTERNAL_INVARIANT")

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
 current=os.open(b"/",O_DIR)
 try:
  for part in path.split(b"/")[1:]:
   need(part not in (b"",b".",b".."))
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following
  held=os.fstat(current)
  need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and held.st_mode&0o022==0)
  return current
 except BaseException:
  os.close(current);raise

def open_under(rootfd,path):
 need(path.startswith(b"/") and b"\x00" not in path)
 parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts))
 current=os.dup(rootfd)
 try:
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following
  return os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
 finally:os.close(current)

def mount_id(number):
 info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=read_all(info,4096)
 finally:os.close(info)
 values=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")]
 need(len(values)==1);return udec(values[0],1)

def mount_line(number):
 wanted=mount_id(number);info=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(info,1048576),1048576)
 finally:os.close(info)
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
 progress(CERT,deadline,0,kind)
 number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=directory)
 try:
  progress(CERT,deadline,0,kind);write_all(number,raw,kind);progress(CERT,deadline,0,kind)
  os.fsync(number);progress(CERT,deadline,0,kind);held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw),kind)
  need(read_all(number,len(raw))==raw,kind);progress(CERT,deadline,0,kind)
 finally:os.close(number)
 os.fsync(directory);progress(CERT,deadline,0,kind)

def stage_leaf(directory,name,raw,identity,deadline):
 durable_leaf(directory,name,raw,deadline)
 number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory)
 try:
  progress(CERT,deadline);held=os.fstat(number);again=read_all(number,identity[0])
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_nlink==1 and held.st_uid==held.st_gid==0)
  need(meta(again)==identity);progress(CERT,deadline)
 finally:os.close(number)

def memfd(raw,label):
 number=os.memfd_create(label,os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)
 write_all(number,raw);os.lseek(number,0,os.SEEK_SET)
 fcntl.fcntl(number,fcntl.F_ADD_SEALS,EXACT_SEALS);seals(number)
 need(read_all(number,len(raw))==raw);os.lseek(number,0,os.SEEK_SET)
 return number

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

CERT_KEYS=(b"ISSUER_ID",b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"HISTORICAL_SNAPSHOT_SEALED",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"CGROUP_CHILD_MODE",b"CGROUP_CHILD_UID",b"CGROUP_CHILD_GID",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"ATTEMPT_DIRFD_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"FINAL_PASS_COMMIT_PROGRESS_NS",b"FINAL_PASS_MARGIN_NS",b"TERMINAL_HANDSHAKE_PROGRESS_NS",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DELETED_CGROUP_FD_GATE_ID",b"DELETED_CGROUP_FD_GATE_PASS",b"DEP_COUNT")

def parse_envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V3",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V3",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":WHOLE_V15[8],b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"EXTERNALLY_VERIFIED_ED25519"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig),Refuse)
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"])
 need(before<after,Refuse)
 return values

def parse_cert(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V3" and lines[-1]==b"CERTIFICATE_END=1",Refuse)
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
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V3",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":WHOLE_V15[8],b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"100000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_MOUNTINFO_SHA256",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"SAFE_BIND_MOUNTINFO_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"CLONE3_CPYTHON_GATE_ID",b"DELETED_CGROUP_FD_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64 and values[b"DELETED_CGROUP_FD_GATE_ID"]!=b"0"*64,Refuse)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1",Refuse)
 for key in (b"KERNEL_RELEASE_HEX",b"E0366_SNAPSHOT_TERMINAL_HEX",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"CGROUP_CHILD_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"LIBC_MODE"):octal(values[key])
 for key in (b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_MOUNT_ID",b"CGROUP2_MOUNT_ID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_NLINK",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_MOUNT_ID",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_NLINK",b"SAFE_BIND_MOUNT_ID",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT"):udec(values[key])
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
 boot=os.open(b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:boot_raw=read_all(boot,128)
 finally:os.close(boot)
 need(boot_raw.endswith(b"\n") and sha(boot_raw)==cert[b"BOOT_ID_SHA256"],Refuse)
 u=os.uname();parts=(u.sysname,u.release,u.version,u.machine)
 encoded=tuple(x.encode("ascii","strict") for x in parts)
 raw=b"SYSNAME="+encoded[0]+b"\nRELEASE="+encoded[1]+b"\nVERSION="+encoded[2]+b"\nMACHINE="+encoded[3]+b"\n"
 need(encoded[3]==b"x86_64" and encoded[1].hex().encode()==cert[b"KERNEL_RELEASE_HEX"] and sha(raw)==cert[b"PLATFORM_ID_SHA256"],Refuse)

def verify_dependency(rootfd,entry):
 role,path,identity=entry;parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts),Refuse)
 current=os.dup(rootfd)
 try:
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode),Refuse)
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
   try:held=os.fstat(number);body=read_all(number,identity[6]);size=len(body);digest=sha(body)
   finally:os.close(number)
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,size,digest)==identity,Refuse)
 finally:os.close(current)

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

def cap_status():
 number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(number,65536),65536)
 finally:os.close(number)
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
 os.chroot(RUNTIME_ROOT);root=os.open(b"/",O_DIR)
 try:
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
 parked=[];targets={target for source,target in mapping}
 try:
  for source,target in mapping:
   number=fcntl.fcntl(source,fcntl.F_DUPFD_CLOEXEC,200)
   need(number>=200 and number not in targets and number not in [x[0] for x in parked])
   parked.append((number,target))
  for number,target in parked:os.dup2(number,target,inheritable=True)
 finally:
  for number,target in parked:
   try:os.close(number)
   except OSError:pass

# P27 RUNNER V3 EMBEDDED VALIDATOR BEGIN 4F2A9D68
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
  synthetic=ctx[b"child_source"]+b"\n#"+b"x"*(251414-len(ctx[b"child_source"])-2)
  need(len(synthetic)==251414);synthetic_sha=sha(synthetic)
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

def validate_transcript(raw,probe,ctx):
 ascii_file(raw,STREAM_CAP);lines=raw[:-1].split(b"\n")
 need(lines and all(lines) and lines[0]==TAG+b"|marker=report|schema=15|probe="+probe)
 keys=PREFIX[probe]+COMMON;need(len(lines)==len(keys)+4);rows={}
 for key,line in zip(keys,lines[1:1+len(keys)]):
  prefix=TAG+b"|probe="+probe+b"|"+key+b"=";need(line.startswith(prefix) and key not in rows)
  value=line[len(prefix):];need(value and b"|" not in value and b"=" not in value);rows[key]=value
 need(lines[1+len(keys)]==TAG+b"|probe="+probe+b"|result=PASS")
 candidate=parse_outer(lines[2+len(keys)],probe,False);terminal=parse_outer(lines[3+len(keys)],probe,True)
 need(candidate==terminal and candidate[b"launcher"]==15 and candidate[b"keeper"]==15 and candidate[b"marker"]==0)
 start=udec(rows[b"probe_start_ns"]);finish=udec(rows[b"probe_finish_ns"]);elapsed=udec(rows[b"probe_elapsed_ns"])
 need(start<=finish and finish-start==elapsed and elapsed<=OP_NS and rows[b"probe_bound_ns"]==b"15000000000")
 need(rows[b"primary_failure"]==b"none" and rows[b"cleanup_failure"]==b"none" and rows[b"result"]==b"PASS")
 need(udec(rows[b"marker_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"marker_image_ino"],1)==ctx[b"python_ino"] and rows[b"marker_image_sha256"]==PY_SHA)
 validate_probe(rows,probe,ctx);expected=-1
 if probe==b"P00":expected=-1 if rows[b"broker_spawned"]==b"0" else 0
 elif probe in (b"P01C",b"P08",b"P10",b"P12"):expected=0
 elif probe==b"P05":expected=15
 elif probe==b"P09":expected=9
 need(candidate[b"child"]==expected)
 return rows
# P27 RUNNER V3 EMBEDDED VALIDATOR END 4F2A9D68

def packet(kind,pairs):
 need(kind and b"|" not in kind and b"\n" not in kind)
 body=kind
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value)
  body+=b"|"+key+b"="+value
 return body+b"\n"

def parse_packet(raw,kind,keys):
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|");need(fields[0]==kind and len(fields)==len(keys)+1);result={}
 for key,item in zip(keys,fields[1:]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result and parts[1]);result[key]=parts[1]
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
 values=parse_packet(raw,b"V3_ABORT",(b"sender",b"state",b"ordinal",b"probe",b"fault_set"))
 need(values[b"sender"]==want_sender and values[b"state"] and values[b"ordinal"] and values[b"probe"])
 faults=parse_fault_csv(values[b"fault_set"],False)
 return values,faults

def close_numbers(numbers):
 for number in numbers:
  try:os.close(number)
  except OSError:pass

def send_plain(control,raw,deadline):
 need(time.monotonic_ns()<=deadline,ConsumedIndeterminate)
 try:count=control.send(raw)
 except BaseException as error:raise FaultSet({b"CONTROL_MALFORMED"}) from error
 if count!=len(raw):raise FaultSet({b"CONTROL_MALFORMED"})
 if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})

def send_rights(control,raw,numbers,deadline):
 need(time.monotonic_ns()<=deadline,ConsumedIndeterminate)
 cells=array.array("i",numbers)
 try:count=control.sendmsg([raw],[(socket.SOL_SOCKET,socket.SCM_RIGHTS,cells.tobytes())])
 except BaseException as error:raise FaultSet({b"FD_TRANSFER"}) from error
 if count!=len(raw):raise FaultSet({b"FD_TRANSFER"})
 if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})

def recv_control(control,deadline,cap=65536):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  remaining=deadline-time.monotonic_ns()
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
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if bad or installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    if address is not None or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    if raw.startswith(b"V3_ABORT|"):
     values,faults=parse_abort(raw,b"B");raise RemoteAbort(faults)
    return raw
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
 number=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
 try:return not cgroup_populated(number)
 finally:os.close(number)

def exact_child_cgroup(cgfd,pid):
 number=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
 try:need(read_all(number,64)==str(pid).encode()+b"\n",ConsumedIndeterminate)
 finally:os.close(number)

def wait_status(pid,flags,deadline,unknown_fault):
 while True:
  if time.monotonic_ns()>deadline:raise FaultSet({unknown_fault})
  try:waited,raw=os.waitpid(pid,flags|os.WNOHANG)
  except InterruptedError:
   if time.monotonic_ns()>deadline:raise FaultSet({unknown_fault})
   continue
  except BaseException as error:raise FaultSet({unknown_fault}) from error
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
 path=even_hex(prior[b"libc_path_hex"])
 conf_bytes=even_hex(prior[b"libc_confstr_hex"])
 conf_text=conf_bytes.decode("ascii","strict")
 need(conf_text.encode("ascii","strict")==conf_bytes and conf_bytes.hex().encode()==prior[b"libc_confstr_hex"])
 need(prior[b"libc_path_hex"]==cert[b"LIBC_PATH_HEX"] and prior[b"libc_confstr_hex"]==cert[b"LIBC_CONFSTR_HEX"] and prior[b"libc_sha256"]==cert[b"LIBC_SHA256"])
 rootfd=open_dir(RUNTIME_ROOT)
 try:
  number=open_under(rootfd,path)
  try:held=os.fstat(number);raw=read_all(number,held.st_size)
  finally:os.close(number)
  py=open_under(rootfd,PYIMAGE)
  try:pyheld=os.fstat(py);pyraw=read_all(py,30626264)
  finally:os.close(py)
 finally:os.close(rootfd)
 observed=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,sha(raw))
 certified=(udec(cert[b"LIBC_DEV"],1),udec(cert[b"LIBC_INO"],1),octal(cert[b"LIBC_MODE"]),udec(cert[b"LIBC_NLINK"],1),0,0,udec(cert[b"LIBC_BYTES"],1),cert[b"LIBC_SHA256"])
 need(observed==certified and held.st_size==udec(prior[b"libc_bytes"]) and sha(raw)==prior[b"libc_sha256"])
 need(sha(pyraw)==PY_SHA and str(pyheld.st_dev).encode()==prior[b"python_image_dev"] and str(pyheld.st_ino).encode()==prior[b"python_image_ino"])
 return (prior[b"libc_path_hex"],str(held.st_dev).encode(),str(held.st_ino).encode(),format(held.st_mode,"o").encode(),str(held.st_nlink).encode(),b"0",b"0",str(held.st_size).encode(),prior[b"libc_sha256"],conf_text.encode("ascii").hex().encode(),prior[b"python_image_dev"],prior[b"python_image_ino"],prior[b"python_image_sha256"])

def launch_b(cert,base_stats):
 empty_r,empty_w=os.pipe2(os.O_CLOEXEC);os.close(empty_w)
 left,right=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
 actor_pid=os.getpid();actor_pidfd=os.pidfd_open(actor_pid,0);pid=os.fork()
 if pid==0:
  try:
   left.close()
   mapping=((empty_r,0),(right.fileno(),3),(actor_pidfd,4),(base_stats[b"attempt_fd"],5),(base_stats[b"cgroup_fd"],6),(104,7),(105,8),(101,9),(106,100))
   preserved_map(mapping);os.close(1);os.close(2)
   close_range(10,99);close_range(101,UINT_MAX)
   child_context(None,base_stats[b"safe"].st_dev,base_stats[b"safe"].st_ino)
   scrub_exact({0,3,4,5,6,7,8,9,100})
   argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",b"RECOVER_V3",AUTH_ID,str(actor_pid).encode(),cert[b"PLAN_SHA256"],cert[b"RECOVERY_SHA256"],str(base_stats[b"safe"].st_dev).encode(),str(base_stats[b"safe"].st_ino).encode())
   os.execve(PYTHON,argv,ENV)
  except BaseException:os._exit(97)
 right.close();os.close(empty_r);os.close(actor_pidfd)
 return pid,left

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
 values=parse_packet(raw,b"V3_RESULT",keys)
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
   fields=parse_packet(header,b"V3_RESULT_FRAME",(b"ordinal",b"probe",b"stream",b"index",b"bytes",b"sha256"))
   need(udec(fields[b"ordinal"],0,14)==ordinal and fields[b"probe"]==probe and fields[b"stream"]==stream)
   need(udec(fields[b"index"])==index and udec(fields[b"bytes"],1,65000)==len(payload) and sha(payload)==fields[b"sha256"])
   target.extend(payload)
 need(recv_control(control,deadline)==b"V3_RESULT_END\n")
 need(len(out)==out_need and len(err)==err_need and sha(out)==values[b"stdout_sha256"] and sha(err)==values[b"stderr_sha256"])
 return values,bytes(out),bytes(err)

def transcript_language(raw):
 if not (type(raw)is bytes and 0<len(raw)<=STREAM_CAP and raw.endswith(b"\n")):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})
 if not all(x==10 or 32<=x<=126 for x in raw):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})
 lines=raw[:-1].split(b"\n")
 if not lines or not all(lines):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})

PHASE_FAULT={b"STAGE":b"STAGING_FAULT",b"CONTAIN":b"CONTAINMENT_FAULT",b"STREAM_ARM":b"FD_TRANSFER",b"CLONE":b"RELEASE_EFFECT_UNKNOWN",b"STOP":b"STOP_WAIT_UNKNOWN",b"PIDFD_ARM":b"PIDFD_BINDING",b"RELEASE_RECORD":b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"SIGCONT":b"RELEASE_EFFECT_UNKNOWN",b"WAIT":b"DIRECT_WAIT_UNKNOWN",b"RESULT":b"CAPTURE_IO",b"LANGUAGE":b"TRANSCRIPT_LANGUAGE",b"SEMANTICS":b"TRANSCRIPT_SEMANTICS",b"RECEIPT":b"ACK_DURABILITY_UNKNOWN",b"REMOVE":b"CONTAINMENT_NOT_EMPTY",b"FINAL":b"REPORT_DURABILITY_UNKNOWN"}

def error_faults(error,phase):
 if isinstance(error,FaultSet):return set(error.faults)
 if isinstance(error,CertificateExpired):return {b"CERTIFICATE_EXPIRED"}
 if isinstance(error,(ConsumedFail,ConsumedIndeterminate)) and phase in PHASE_FAULT:return {PHASE_FAULT[phase]}
 return {b"INTERNAL_INVARIANT"}

def send_abort(control,state,ordinal,probe,faults,deadline):
 raw=packet(b"V3_ABORT",((b"sender",b"A"),(b"state",state),(b"ordinal",b"NONE" if ordinal is None else str(ordinal).encode()),(b"probe",probe),(b"fault_set",fault_csv(faults))))
 send_plain(control,raw,deadline)

def run_probe(control,ordinal,probe,cgfd,safefd,safe,outer_source,ctx,p01c,cert):
 phase=b"STREAM_ARM";release_origin=time.monotonic_ns();launch_deadline=release_origin+LAUNCH_NS
 checkpoint(cert,(15-ordinal)*TOTAL_NS+REPORT_NS,ConsumedIndeterminate,launch_deadline)
 in_r,in_w=os.pipe2(os.O_CLOEXEC);os.close(in_w);need(os.read(in_r,1)==b"")
 out_r,out_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK);err_r,err_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
 need(os.fstat(out_r).st_ino!=os.fstat(err_r).st_ino)
 outer_fd=memfd(outer_source,"p27-v15-outer-v3")
 events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
 kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
 pid=pidfd=-1;direct_wait_entered=False
 try:
  stream=packet(b"V3_STREAM_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode()),(b"stdout_dev",str(os.fstat(out_r).st_dev).encode()),(b"stdout_ino",str(os.fstat(out_r).st_ino).encode()),(b"stderr_dev",str(os.fstat(err_r).st_dev).encode()),(b"stderr_ino",str(os.fstat(err_r).st_ino).encode()),(b"events_dev",str(os.fstat(events).st_dev).encode()),(b"events_ino",str(os.fstat(events).st_ino).encode()),(b"kill_dev",str(os.fstat(kill).st_dev).encode()),(b"kill_ino",str(os.fstat(kill).st_ino).encode())))
  send_rights(control,stream,(out_r,err_r,events,kill),launch_deadline)
  close_numbers((out_r,err_r,events,kill));out_r=err_r=events=kill=-1
  wait_exact(control,launch_deadline,b"V3_STREAMS_ARMED\n");progress(cert,launch_deadline,(15-ordinal)*TOTAL_NS+REPORT_NS)
  phase=b"CLONE";argv=source_argv(probe,safe,p01c);pid,pidfd=launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd)
  close_numbers((in_r,out_w,err_w,outer_fd));in_r=out_w=err_w=outer_fd=-1
  phase=b"STOP";stopped=wait_status(pid,os.WUNTRACED,launch_deadline,b"STOP_WAIT_UNKNOWN")
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP,ConsumedIndeterminate)
  exact_child_cgroup(cgfd,pid);need(not cgroup_empty(cgfd),ConsumedIndeterminate)
  phase=b"PIDFD_ARM";arm=packet(b"V3_PIDFD_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"pidfd_bound",b"1")))
  send_rights(control,arm,(pidfd,),launch_deadline);os.close(pidfd);pidfd=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V3_PIDFD_ARMED",(b"ordinal",b"probe",b"pidfd_bound"))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe and armed[b"pidfd_bound"]==b"1")
  outer_pid=pid;cg=os.fstat(cgfd)
  phase=b"RELEASE_RECORD";release=packet(b"V3_RELEASE_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_bound",b"1"),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"cgroup_dev",str(cg.st_dev).encode()),(b"cgroup_ino",str(cg.st_ino).encode()),(b"cgroup_mode",format(cg.st_mode,"o").encode()),(b"cgroup_nlink",str(cg.st_nlink).encode()),(b"cgroup_uid",str(cg.st_uid).encode()),(b"cgroup_gid",str(cg.st_gid).encode()),(b"argv_sha256",sha(b"\x00".join(argv))),(b"env_sha256",sha(b"\x00".join(x+b"="+ENV[x] for x in sorted(ENV)))),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode())))
  send_plain(control,release,launch_deadline)
  released=parse_packet(recv_control(control,launch_deadline),b"V3_RELEASE_DURABLE",(b"ordinal",b"probe",b"release_sha256"))
  need(udec(released[b"ordinal"],0,14)==ordinal and released[b"probe"]==probe);release_sha=h64(released[b"release_sha256"])
  phase=b"SIGCONT";checkpoint(cert,(15-ordinal)*TOTAL_NS+REPORT_NS,ConsumedIndeterminate,launch_deadline)
  call_entry=time.monotonic_ns();need(call_entry+SIGCONT_NS<=launch_deadline,ConsumedIndeterminate)
  os.kill(pid,signal.SIGCONT);release_return=time.monotonic_ns()
  need(release_return<=call_entry+SIGCONT_NS and release_return<=launch_deadline,ConsumedIndeterminate)
  checkpoint(cert,(15-ordinal)*TOTAL_NS+REPORT_NS,ConsumedIndeterminate,launch_deadline)
  phase=b"WAIT";direct_wait_entered=True
  raw=wait_status(pid,0,release_origin+HOST_NS,b"DIRECT_WAIT_UNKNOWN");pid=-1;direct_done=time.monotonic_ns()
  phase=b"RESULT";values,stdout,stderr=recv_result(control,release_origin+HOST_NS,ordinal,probe,outer_pid)
  done=udec(values[b"capture_done_ns"]);host_complete=max(direct_done,done)
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
  phase=b"SEMANTICS"
  try:rows=validate_transcript(stdout,probe,ctx)
  except FaultSet:raise
  except BaseException as error:raise FaultSet({b"TRANSCRIPT_SEMANTICS"}) from error
  phase=b"RECEIPT";candidate=packet(b"V3_VALIDATED_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_record_sha256",release_sha),(b"release_origin_ns",str(release_origin).encode()),(b"release_return_ns",str(release_return).encode()),(b"host_complete_ns",str(host_complete).encode()),(b"capture_done_ns",str(done).encode()),(b"direct_wait_state",b"COMPLETE"),(b"outer_raw_status",str(raw).encode()),(b"pidfd_bound",b"1"),(b"pidfd_exit_ready_observed",b"1"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1"),(b"stdout_overflow",b"0"),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",EMPTY_SHA),(b"stderr_eof",b"1"),(b"stderr_overflow",b"0"),(b"cgroup_empty",b"1"),(b"parser_language",b"ACCEPTED"),(b"parser_semantics",b"ACCEPTED"),(b"candidate",b"ACCEPTED"),(b"terminal",b"ACCEPTED"),(b"certificate_expiry_realtime_ns",cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])))
  receipt_deadline=release_origin+TOTAL_NS;send_plain(control,candidate,receipt_deadline)
  validated=parse_packet(recv_control(control,receipt_deadline),b"V3_VALIDATED_DURABLE",(b"ordinal",b"probe",b"validated_sha256"))
  need(udec(validated[b"ordinal"],0,14)==ordinal and validated[b"probe"]==probe);validated_sha=h64(validated[b"validated_sha256"])
  checkpoint(cert,(14-ordinal)*TOTAL_NS+REPORT_NS,ConsumedIndeterminate,receipt_deadline)
  actor_ack=time.monotonic_ns();intent=packet(b"V3_ACK_COMMIT_INTENT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha),(b"actor_ack_intent_ns",str(actor_ack).encode())))
  send_plain(control,intent,receipt_deadline)
  committed=parse_packet(recv_control(control,receipt_deadline),b"V3_COMMITTED",(b"ordinal",b"probe",b"ack_sha256"))
  need(udec(committed[b"ordinal"],0,14)==ordinal and committed[b"probe"]==probe);ack_sha=h64(committed[b"ack_sha256"])
  checkpoint(cert,(14-ordinal)*TOTAL_NS+REPORT_NS,ConsumedIndeterminate,receipt_deadline)
  seen=packet(b"V3_COMMITTED_SEEN",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha)))
  send_plain(control,seen,receipt_deadline);return rows,ack_sha
 except BaseException as error:
  faults=error_faults(error,phase)
  try:send_abort(control,phase,ordinal,probe,faults,time.monotonic_ns()+ACK_NS)
  except BaseException as send_error:faults.update(error_faults(send_error,phase))
  if pid>=0 and not direct_wait_entered:
   direct_wait_entered=True
   try:wait_status(pid,0,time.monotonic_ns()+CLEANUP_NS,b"DIRECT_WAIT_UNKNOWN");pid=-1
   except FaultSet as wait_error:faults.update(wait_error.faults)
  raised=FaultSet(faults);setattr(raised,"p27_abort_sent",True);setattr(raised,"p27_phase",phase);raise raised
 finally:
  close_numbers(tuple(number for number in (in_r,out_r,out_w,err_r,err_w,outer_fd,events,kill,pidfd) if number>=0))

def mount_semantics(line,fstype,required,forbidden):
 pieces=line[:-1].split(b" - ");need(len(pieces)==2)
 left=pieces[0].split(b" ");right=pieces[1].split(b" ");need(len(left)>=6 and len(right)>=3 and right[0]==fstype)
 options=set(left[5].split(b","))|set(right[2].split(b","))
 need(required<=options and not (forbidden&options),Refuse)

def mount_graph(cert):
 number=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(number,1048576),1048576)
 finally:os.close(number)
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

def await_failure_terminal(control,deadline):
 raw=recv_control(control,deadline)
 values=parse_packet(raw,b"V3_TERMINAL_FAILURE_DURABLE",(b"report_sha256",b"disposition"))
 report_sha=h64(values[b"report_sha256"])
 need(values[b"disposition"] in (b"CONSUMED_FAIL",b"CONSUMED_INDETERMINATE"))
 seen=packet(b"V3_TERMINAL_SEEN",((b"kind",b"FAILURE"),(b"subject_sha256",report_sha)))
 send_plain(control,seen,deadline)
 ack=parse_packet(recv_control(control,deadline),b"V3_TERMINAL_ACK",(b"kind",b"subject_sha256",b"closure"))
 need(ack[b"kind"]==b"FAILURE" and ack[b"subject_sha256"]==report_sha and ack[b"closure"]==b"SEEN")
 return values[b"disposition"]

def main():
 global AUTH_ID,PREFLIGHT,CERT
 entry_mono=time.monotonic_ns();state=b"INPUT";consumed=False;commit_edge=False;armed=False
 bpid=-1;control=None;runtime=attempt_base=stage_base=cgroup_base=safefd=cgfd=-1
 need(type(sys.argv)is list and len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RUN_V3",Refuse)
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
 AUTH_ID=sha(b"P27E001V3\x00"+cert_raw+b"\x00"+envelope_raw);need(AUTH_ID==supplied,Refuse)
 state=b"CERT";envelope=parse_envelope(envelope_raw);CERT,deps=parse_cert(cert_raw)
 need(sha(cert_raw)==envelope[b"CERTIFICATE_SHA256"] and sha(envelope_raw)==CERT[b"ISSUER_ENVELOPE_SHA256"],Refuse)
 need(envelope[b"PLAN_SHA256"]==CERT[b"PLAN_SHA256"] and envelope[b"RUNNER_SHA256"]==CERT[b"RUNNER_SHA256"] and envelope[b"RECOVERY_SHA256"]==CERT[b"RECOVERY_SHA256"],Refuse)
 need(sha(plan)==CERT[b"PLAN_SHA256"] and sha(actor_raw)==CERT[b"RUNNER_SHA256"] and sha(b_raw)==CERT[b"RECOVERY_SHA256"],Refuse)
 need(envelope[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot),Refuse)
 need(envelope[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and envelope[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672",Refuse)
 need(envelope[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX,Refuse)
 not_before=udec(CERT[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(envelope[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(envelope[b"NOT_AFTER_REALTIME_NS"]),Refuse)
 checkpoint(CERT,ENTRY_REMAIN_NS,Refuse,entry_mono+PRECONSUME_NS);verify_platform(CERT);signal_snapshot(CERT)
 ab=b"P27 RUNNER V3 ACTOR SOURCE "+b"BEGIN 91C4B7E3";ae=b"P27 RUNNER V3 ACTOR SOURCE "+b"END 91C4B7E3"
 bb=b"P27 RUNNER V3 WATCHDOG SOURCE "+b"BEGIN D8E5A103";be=b"P27 RUNNER V3 WATCHDOG SOURCE "+b"END D8E5A103"
 need(extract_one(plan,ab,ae)==actor_raw and extract_one(plan,bb,be)==b_raw,Refuse)
 sources=v15_sources(v15)
 state=b"ENTRY";runtime=open_dir(RUNTIME_ROOT);attempt_base=open_dir(ATTEMPT_BASE);stage_base=open_dir(STAGE_BASE);cgroup_base=open_dir(CGROUP_BASE)
 try:
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
  base_type=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
  base_controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
  base_subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
  try:
   need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"],Refuse)
   need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"],Refuse)
   need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"],Refuse)
  finally:close_numbers((base_type,base_controllers,base_subtree))
  need(runtime_mid!=stage_mid,Refuse);mount_graph(CERT)
  absent(attempt_base,AUTH_ID,Refuse);absent(stage_base,AUTH_ID,Refuse);absent(cgroup_base,AUTH_ID,Refuse)
  need(time.monotonic_ns()-entry_mono<=PRECONSUME_NS,Refuse)
  bases={b"attempt_fd":attempt_base,b"cgroup_fd":cgroup_base,b"safe":stage_stat}
  state=b"B_BOOT";bpid,control=launch_b(CERT,bases)
  ready_deadline=entry_mono+PRECONSUME_NS;wait_exact(control,ready_deadline,b"V3_READY\n")
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,ready_deadline)
  state=b"CONSUME_PREPARE";b_send(control,b"V3_CONSUME_BEGIN\n",ready_deadline)
  wait_exact(control,ready_deadline,b"V3_CONSUME_ARMED\n");armed=True
  consume_deadline=time.monotonic_ns()+CONSUMPTION_NS
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,consume_deadline)
  state=b"CONSUME_EDGE_UNKNOWN";commit_edge=True;consumed=True;PREFLIGHT=False
  b_send(control,b"V3_CONSUME_COMMIT\n",consume_deadline)
  consumed_msg=parse_packet(recv_control(control,consume_deadline),b"V3_CONSUMED_DURABLE",(b"intent_sha256",))
  chain_sha=h64(consumed_msg[b"intent_sha256"])
  checkpoint(CERT,CONSUME_REMAIN_NS,ConsumedIndeterminate,consume_deadline)
  state=b"STAGE";stage_origin=time.monotonic_ns();stage_deadline=stage_origin+STAGE_NS
  checkpoint(CERT,15*TOTAL_NS+REPORT_NS,ConsumedIndeterminate,stage_deadline)
  os.mkdir(AUTH_ID,0o700,dir_fd=stage_base);progress(CERT,stage_deadline)
  os.fsync(stage_base);progress(CERT,stage_deadline)
  safefd=os.open(AUTH_ID,O_DIR,dir_fd=stage_base);progress(CERT,stage_deadline);safe=os.fstat(safefd)
  need((safe.st_uid,safe.st_gid,stat.S_IMODE(safe.st_mode),safe.st_nlink)==(0,0,0o700,2),ConsumedIndeterminate)
  for name in (b"target",b"a",b"b"):absent(safefd,name)
  for name,body,identity in zip(SOURCE_NAMES,sources[1:],SOURCE_META[1:]):stage_leaf(safefd,name,body,identity,stage_deadline)
  os.fsync(safefd);progress(CERT,stage_deadline,15*TOTAL_NS+REPORT_NS)
  staged=packet(b"V3_STAGE_DURABLE",((b"safe_dev",str(safe.st_dev).encode()),(b"safe_ino",str(safe.st_ino).encode()),(b"stage_return_ns",str(time.monotonic_ns()).encode())))
  b_send(control,staged,stage_deadline);wait_exact(control,stage_deadline,b"V3_STAGE_ACK\n")
  progress(CERT,stage_deadline,15*TOTAL_NS+REPORT_NS)
  state=b"CONTAIN";contain_deadline=time.monotonic_ns()+ACK_NS
  os.mkdir(AUTH_ID,0o700,dir_fd=cgroup_base);progress(CERT,contain_deadline)
  cgfd=os.open(AUTH_ID,O_DIR,dir_fd=cgroup_base);progress(CERT,contain_deadline);cgchild=os.fstat(cgfd)
  need((format(cgchild.st_mode,"o").encode(),cgchild.st_uid,cgchild.st_gid,cgchild.st_nlink)==(CERT[b"CGROUP_CHILD_MODE"],0,0,2),ConsumedIndeterminate)
  need(cgroup_empty(cgfd),ConsumedIndeterminate)
  ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  try:
   need(read_all(ctype,128).hex().encode()==CERT[b"CGROUP_CHILD_TYPE_HEX"],ConsumedIndeterminate)
   need(read_all(controllers,4096).hex().encode()==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"],ConsumedIndeterminate)
   need(read_all(subtree,4096).hex().encode()==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"],ConsumedIndeterminate)
  finally:close_numbers((ctype,controllers,subtree))
  containment=packet(b"V3_CONTAINMENT",((b"dev",str(cgchild.st_dev).encode()),(b"ino",str(cgchild.st_ino).encode()),(b"mode",format(cgchild.st_mode,"o").encode()),(b"nlink",str(cgchild.st_nlink).encode()),(b"uid",str(cgchild.st_uid).encode()),(b"gid",str(cgchild.st_gid).encode())))
  send_rights(control,containment,(cgfd,),contain_deadline);wait_exact(control,contain_deadline,b"V3_CONTAINMENT_ACK\n")
  progress(CERT,contain_deadline,15*TOTAL_NS+REPORT_NS)
  safe_path=STAGE_BASE+b"/"+AUTH_ID
  ctx={b"cwd_hex":safe_path.hex().encode(),b"python_dev":udec(CERT[b"PYTHON_IMAGE_DEV"],1),b"python_ino":udec(CERT[b"PYTHON_IMAGE_INO"],1),b"libc_path_hex":CERT[b"LIBC_PATH_HEX"],b"libc_confstr_hex":CERT[b"LIBC_CONFSTR_HEX"],b"libc_bytes":udec(CERT[b"LIBC_BYTES"],1),b"libc_sha":CERT[b"LIBC_SHA256"],b"valid_signals":udec(CERT[b"VALID_SIGNAL_COUNT"]),b"default_signals":udec(CERT[b"DEFAULT_SIGNAL_COUNT"]),b"defaults_sha":CERT[b"DEFAULTS_SHA256"],b"child_source":sources[4]}
  prior=None
  for ordinal,probe in enumerate(SUITE):
   checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS)
   p01c=derive_p01c(prior,CERT) if probe==b"P01C" else ()
   rows,chain_sha=run_probe(control,ordinal,probe,cgfd,safefd,safe,sources[0],ctx,p01c,CERT)
   if probe==b"P01D":prior=rows;ctx[b"p01d"]=rows
  state=b"REMOVE";final_deadline=time.monotonic_ns()+REPORT_NS
  checkpoint(CERT,REPORT_NS,ConsumedIndeterminate,final_deadline);need(cgroup_empty(cgfd),ConsumedIndeterminate)
  b_send(control,b"V3_EMPTY_FINAL_QUERY\n",final_deadline);wait_exact(control,final_deadline,b"V3_EMPTY_FINAL_CONFIRMED\n")
  os.close(cgfd);cgfd=-1;os.rmdir(AUTH_ID,dir_fd=cgroup_base)
  try:os.stat(AUTH_ID,dir_fd=cgroup_base,follow_symlinks=False);need(False,ConsumedIndeterminate)
  except FileNotFoundError:pass
  progress(CERT,final_deadline,REPORT_NS)
  removed=packet(b"V3_CGROUP_REMOVED",((b"chain_head_sha256",chain_sha),))
  b_send(control,removed,final_deadline)
  removed_ack=parse_packet(recv_control(control,final_deadline),b"V3_REMOVE_ACK",(b"chain_head_sha256",))
  need(removed_ack[b"chain_head_sha256"]==chain_sha)
  state=b"FINAL";checkpoint(CERT,REPORT_NS,ConsumedIndeterminate,final_deadline)
  finalize=packet(b"V3_FINALIZE_CANDIDATE",((b"chain_head_sha256",chain_sha),))
  b_send(control,finalize,final_deadline)
  candidate=parse_packet(recv_control(control,final_deadline),b"V3_TERMINAL_CANDIDATE_DURABLE",(b"candidate_sha256",b"chain_head_sha256"))
  candidate_sha=h64(candidate[b"candidate_sha256"]);need(candidate[b"chain_head_sha256"]==chain_sha)
  checkpoint(CERT,PASS_COMMIT_NS+PASS_MARGIN_NS+TERMINAL_NS,ConsumedIndeterminate,final_deadline)
  seen=packet(b"V3_TERMINAL_SEEN",((b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha)))
  b_send(control,seen,final_deadline)
  terminal=parse_packet(recv_control(control,final_deadline),b"V3_TERMINAL_ACK",(b"kind",b"candidate_sha256",b"terminal_seen_sha256",b"report_sha256"))
  need(terminal[b"kind"]==b"SUCCESS" and terminal[b"candidate_sha256"]==candidate_sha)
  h64(terminal[b"terminal_seen_sha256"]);h64(terminal[b"report_sha256"])
  control.close();control=None
  braw=wait_status(bpid,0,time.monotonic_ns()+TERMINAL_NS,b"ACTOR_LOST");bpid=-1
  need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
  write_all(1,b"P27E001_RUNNER_V3|AUTH_ID="+AUTH_ID+b"|entered=15|committed=15|terminal_ack=1\n")
 except BaseException as error:
  phase=getattr(error,"p27_phase",state);faults=error_faults(error,phase)
  disposition=None;clean_refusal=False
  if not commit_edge:
   if control is not None:
    try:
     refusal_deadline=time.monotonic_ns()+ACK_NS
     b_send(control,b"V3_REFUSE_PRECOMMIT\n",refusal_deadline)
     wait_exact(control,refusal_deadline,b"V3_REFUSE_ACK\n");clean_refusal=True
    except BaseException:clean_refusal=False
   elif not armed:clean_refusal=True
  else:
   if control is not None:
    try:
     if not getattr(error,"p27_abort_sent",False):
      send_abort(control,phase,locals().get("ordinal",None),locals().get("probe",b"NONE"),faults,time.monotonic_ns()+ACK_NS)
     disposition=await_failure_terminal(control,time.monotonic_ns()+CLEANUP_NS+REPORT_NS+TERMINAL_NS)
    except BaseException:disposition=None
  if control is not None:
   try:control.close()
   except BaseException:pass
   control=None
  if bpid>=0:
   try:wait_status(bpid,0,time.monotonic_ns()+CLEANUP_NS+REPORT_NS+TERMINAL_NS,b"ACTOR_LOST");bpid=-1
   except BaseException:pass
  if clean_refusal and not commit_edge:raise Refuse("clean-refusal") from error
  if not commit_edge and not armed:raise Refuse("prearmed-refusal") from error
  if disposition==b"CONSUMED_FAIL":raise ConsumedFail("reported-fail") from error
  raise ConsumedIndeterminate("consumed-or-effect-unknown") from error
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
P27 RUNNER V3 ACTOR SOURCE END 91C4B7E3

P27 RUNNER V3 WATCHDOG SOURCE BEGIN D8E5A103
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
FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"CONSUME_EDGE_UNKNOWN",b"ATTEMPT_COLLISION",b"ATTEMPT_NAMESPACE_UNKNOWN",b"ATTEMPT_DIRFD_UNKNOWN",b"ATTEMPT_BASE_DURABILITY_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"CONTROL_MALFORMED",b"CONTROL_TIMEOUT",b"CONTROL_TRUNCATION",b"FD_TRANSFER",b"STOP_WAIT_UNKNOWN",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_TICKET_DURABILITY_UNKNOWN",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_IO",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"DIRECT_WAIT_UNKNOWN",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_SEMANTICS",b"VALIDATED_DURABILITY_UNKNOWN",b"ACK_DURABILITY_UNKNOWN",b"CONTAINMENT_OBSERVATION_UNKNOWN",b"CONTAINMENT_NOT_EMPTY",b"RECOVERY_DURABILITY_UNKNOWN",b"RETAINED_DURABILITY_UNKNOWN",b"REPORT_CANDIDATE_DURABILITY_UNKNOWN",b"TERMINAL_SEEN_DURABILITY_UNKNOWN",b"REPORT_DURABILITY_UNKNOWN",b"INTERNAL_INVARIANT")
KNOWN_FAIL={b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_SEMANTICS"}
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
KILL_RETURN_NS=5000000
MAX_RIGHTS=4
UINT_MAX=(1<<32)-1
DURABLE_VERIFIED=b"DURABLE_VERIFIED"
ENVELOPE_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX")
CERT_KEYS=(b"ISSUER_ID",b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"HISTORICAL_SNAPSHOT_SEALED",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"CGROUP_CHILD_MODE",b"CGROUP_CHILD_UID",b"CGROUP_CHILD_GID",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"ATTEMPT_DIRFD_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"FINAL_PASS_COMMIT_PROGRESS_NS",b"FINAL_PASS_MARGIN_NS",b"TERMINAL_HANDSHAKE_PROGRESS_NS",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DELETED_CGROUP_FD_GATE_ID",b"DELETED_CGROUP_FD_GATE_PASS",b"DEP_COUNT")

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
 need(kind and b"|" not in kind and b"\n" not in kind)
 body=kind
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value)
  body+=b"|"+key+b"="+value
 return body+b"\n"

def parse_packet(raw,kind,keys):
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|");need(fields[0]==kind and len(fields)==len(keys)+1);result={}
 for key,item in zip(keys,fields[1:]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result and parts[1]);result[key]=parts[1]
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

def parse_abort(raw):
 values=parse_packet(raw,b"V3_ABORT",(b"sender",b"state",b"ordinal",b"probe",b"fault_set"))
 need(values[b"sender"]==b"A");return values,parse_fault_csv(values[b"fault_set"],False)

def envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V3",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V3",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":V15_SHA,b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"EXTERNALLY_VERIFIED_ED25519"}
 for key,value in exact.items():need(values[key]==value)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig))
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"])
 need(before<after)
 return values

def contract(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V3" and lines[-1]==b"CERTIFICATE_END=1")
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
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V3",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":V15_SHA,b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"100000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value)
 for key in (b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_MOUNTINFO_SHA256",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"SAFE_BIND_MOUNTINFO_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"CLONE3_CPYTHON_GATE_ID",b"DELETED_CGROUP_FD_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64 and values[b"DELETED_CGROUP_FD_GATE_ID"]!=b"0"*64)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1")
 for key in (b"KERNEL_RELEASE_HEX",b"E0366_SNAPSHOT_TERMINAL_HEX",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"CGROUP_CHILD_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"LIBC_MODE"):octal(values[key])
 for key in (b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_MOUNT_ID",b"CGROUP2_MOUNT_ID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_NLINK",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_MOUNT_ID",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_NLINK",b"SAFE_BIND_MOUNT_ID",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT"):udec(values[key])
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

def cert_live(cert,needed=0):
 return checkpoint(cert,needed)

def cap_status():
 number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(number,65536),65536)
 finally:os.close(number)
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
 link=os.readlink(b"/proc/self/fd/"+str(number).encode());need(link==b"anon_inode:[pidfd]")
 info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(info,4096),4096)
 finally:os.close(info)
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
 info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(info,4096),4096)
 finally:os.close(info)
 mids=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")];need(len(mids)==1);mid=udec(mids[0],1)
 table=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:rows=ascii_file(read_all(table,1048576),1048576)
 finally:os.close(table)
 matches=[line+b"\n" for line in rows.splitlines() if line.split(b" ",1)[0]==str(mid).encode()]
 need(len(matches)==1);return mid,matches[0]

def base_check(number,cert,prefix):
 held=os.fstat(number);need(stat.S_ISDIR(held.st_mode));fd_access(number,os.O_RDONLY)
 expected=(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),octal(cert[prefix+b"_MODE"]),udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"]))
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==expected)
 return held

def write_all(number,raw):
 offset=0
 while offset<len(raw):
  try:count=os.write(number,raw[offset:])
  except InterruptedError:continue
  need(count>0);offset+=count

def post_deadline(deadline):
 if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})

def durable_once(context,name,raw,deadline,require_live=True,needed_after=0):
 digest=sha(raw)
 if name in context[b"durability"]:return context[b"durability"][name],digest
 state=b"ABSENT_KNOWN";context[b"durability"][name]=state;number=-1
 try:
  post_deadline(deadline)
  if require_live:checkpoint(CERT,needed_after,deadline)
  state=b"OPEN_EFFECT_UNKNOWN";context[b"durability"][name]=state
  number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=context[b"attempt"])
  post_deadline(deadline);state=b"FD_HELD";context[b"durability"][name]=state
  state=b"WRITE_EFFECT_UNKNOWN";context[b"durability"][name]=state
  write_all(number,raw);post_deadline(deadline)
  state=b"FILE_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  os.fsync(number);post_deadline(deadline)
  held=os.fstat(number);need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw))
  need(read_all(number,len(raw))==raw);post_deadline(deadline)
  state=b"SAME_FD_REREAD_VERIFIED";context[b"durability"][name]=state
  state=b"DIR_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  os.fsync(context[b"attempt"]);post_deadline(deadline)
  if require_live:checkpoint(CERT,needed_after,deadline)
  state=DURABLE_VERIFIED;context[b"durability"][name]=state
 except BaseException:
  context[b"durability"][name]=state
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
 return (b"P27E001_ATTEMPT_INTENT_V3\nAUTH_ID="+auth+b"\nNONCE="+auth+b"\nRECORD_SEQ=1\nPREDECESSOR_SHA256=NONE\nISSUER_ENVELOPE_SHA256="+sha(envelope_raw)+b"\nCERTIFICATE_SHA256="+sha(cert_raw)+b"\nPLAN_SHA256="+cert[b"PLAN_SHA256"]+b"\nRUNNER_SHA256="+cert[b"RUNNER_SHA256"]+b"\nRECOVERY_SHA256="+sha(source_raw)+b"\nE0366_SNAPSHOT_BYTES=2303269\nE0366_SNAPSHOT_LF=23672\nE0366_SNAPSHOT_SHA256="+SNAPSHOT_EXPECT[2]+b"\nE0366_SNAPSHOT_TERMINAL_HEX="+SNAPSHOT_TERMINAL_HEX+b"\nV15_SHA256="+cert[b"V15_SHA256"]+b"\nSUITE="+b",".join(PROBES)+b"\nATTEMPT_PATH_HEX="+(b"/var/lib/p27-e001-host-v15/attempts/"+auth).hex().encode()+b"\nSTAGE_PATH_HEX="+(b"/tmp/p27-e001-host-v15/"+auth).hex().encode()+b"\nCGROUP_PATH_HEX="+(b"/sys/fs/cgroup/p27-e001-host-v15/"+auth).hex().encode()+b"\nACTOR_ENTRY_CAPS=00000000000401c0\nPAYLOAD_FINAL_CAPS=0000000000000000\nABSOLUTE_EXPIRY_REALTIME_NS="+cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCONSUMED_OR_EFFECT_UNKNOWN=1\nRETRY_ALLOWED=0\nINTENT_END=1\n")

def verify_attempt_fd(number):
 held=os.fstat(number)
 need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and stat.S_IMODE(held.st_mode)==0o700 and held.st_nlink>=2)
 return held

def retain_attempt_dirfd(context):
 while context[b"attempt"]<0:
  context[b"consumption_state"]=b"RETAINED_DIRFD_OBSERVATION"
  try:
   number=os.open(AUTH,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
   verify_attempt_fd(number);context[b"attempt"]=number;context[b"consumption_state"]=b"DIRFD_PUBLISHED_RETAINED"
   return
  except BaseException:
   try:
    if "number" in locals() and number>=0:os.close(number)
   except OSError:pass
   try:select.poll().poll(50)
   except InterruptedError:pass

def consume_attempt(context,cert_raw,envelope_raw,source_raw):
 deadline=time.monotonic_ns()+CONSUMPTION_NS
 context[b"consumption_state"]=b"MKDIR_CALL_ENTERED"
 try:
  os.mkdir(AUTH,0o700,dir_fd=5)
 except FileExistsError as error:
  context[b"consumption_state"]=b"COLLISION";context[b"faults"].add(b"ATTEMPT_COLLISION")
  try:
   number=os.open(AUTH,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
   verify_attempt_fd(number);context[b"attempt"]=number
  except BaseException:context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 except BaseException as error:
  context[b"consumption_state"]=b"MKDIR_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_NAMESPACE_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 context[b"consumption_state"]=b"MKDIR_RETURNED_CREATED"
 context[b"consumption_state"]=b"IMMEDIATE_DIRFD_CALL_ENTERED"
 try:number=os.open(AUTH,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
 except BaseException as error:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 context[b"attempt"]=number;context[b"consumption_state"]=b"DIRFD_PUBLISHED";verify_attempt_fd(number)
 post_deadline(deadline);checkpoint(CERT,15*TOTAL_NS+REPORT_NS,deadline)
 context[b"consumption_state"]=b"BASE_FSYNC_EFFECT_UNKNOWN"
 try:os.fsync(5);post_deadline(deadline)
 except BaseException as error:
  context[b"faults"].add(b"ATTEMPT_BASE_DURABILITY_UNKNOWN");raise FaultSet(set(context[b"faults"])) from error
 context[b"consumption_state"]=b"BASE_DURABLE"
 body=attempt_intent(AUTH,CERT,cert_raw,envelope_raw,source_raw)
 state,digest=durable_once(context,b"intent.v3",body,deadline,True,15*TOTAL_NS+REPORT_NS)
 if state!=DURABLE_VERIFIED:
  context[b"faults"].add(b"INTENT_DURABILITY_UNKNOWN");raise FaultSet(set(context[b"faults"]))
 context[b"intent_durable"]=True;context[b"chain_sha"]=digest;context[b"record_seq"]=1
 context[b"consumption_state"]=b"INTENT_DURABLE";return digest

def release_record(context,values):
 seq=next_record(context);predecessor=context[b"chain_sha"];origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_RELEASE_STATE_V3\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nOUTER_PID="+values[b"outer_pid"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED=0\nSTOPPED_RAW_STATUS="+values[b"stopped_raw_status"]+b"\nCGROUP_MEMBER="+values[b"cgroup_member"]+b"\nCGROUP_DEV="+values[b"cgroup_dev"]+b"\nCGROUP_INO="+values[b"cgroup_ino"]+b"\nCGROUP_MODE="+values[b"cgroup_mode"]+b"\nCGROUP_NLINK="+values[b"cgroup_nlink"]+b"\nCGROUP_UID="+values[b"cgroup_uid"]+b"\nCGROUP_GID="+values[b"cgroup_gid"]+b"\nARGV_SHA256="+values[b"argv_sha256"]+b"\nENV_SHA256="+values[b"env_sha256"]+b"\nRELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nLAUNCH_DEADLINE_NS="+values[b"launch_deadline_ns"]+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nSTATE=RELEASE_AUTHORIZED\nRELEASE_END=1\n")
 state,digest=durable_once(context,b"release-"+values[b"probe"]+b".v3",body,deadline,True)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"RELEASE_RECORD_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"release_sha"]=digest;return digest

CANDIDATE_KEYS=(b"ordinal",b"probe",b"release_record_sha256",b"release_origin_ns",b"release_return_ns",b"host_complete_ns",b"capture_done_ns",b"direct_wait_state",b"outer_raw_status",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_overflow",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_overflow",b"cgroup_empty",b"parser_language",b"parser_semantics",b"candidate",b"terminal",b"certificate_expiry_realtime_ns")
FINAL_REPORT_KEYS=(b"AUTH_ID",b"SUITE",b"ENTERED_COUNT",b"COMMITTED_COUNT",b"STOP_PROBE",b"PRIMARY",b"FAULT_SET",b"CHAIN_HEAD_SHA256",b"TERMINAL_SEEN_SHA256",b"DIRECT_REAP",b"CGROUP_EMPTY",b"CGROUP_REMOVED",b"KILL_CALL_COUNT",b"KILL_STATE",b"CERTIFICATE_LIVE_AT_COMMIT",b"PASS_COMMIT_ORIGIN_MONOTONIC_NS",b"PASS_COMMIT_DEADLINE_MONOTONIC_NS",b"FINAL_PASS_MARGIN_NS",b"STAGE_RETAINED",b"ATTEMPT_RETAINED",b"RETRY_ALLOWED",b"DISPOSITION")

def forensic_body(values):
 return (b"RELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nRELEASE_RETURN_NS="+values[b"release_return_ns"]+b"\nHOST_COMPLETE_NS="+values[b"host_complete_ns"]+b"\nCAPTURE_DONE_NS="+values[b"capture_done_ns"]+b"\nDIRECT_WAIT="+values[b"direct_wait_state"]+b"\nOUTER_RAW_STATUS="+values[b"outer_raw_status"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED="+values[b"pidfd_exit_ready_observed"]+b"\nSTDOUT_BYTES="+values[b"stdout_len"]+b"\nSTDOUT_SHA256="+values[b"stdout_sha256"]+b"\nSTDOUT_EOF="+values[b"stdout_eof"]+b"\nSTDOUT_OVERFLOW="+values[b"stdout_overflow"]+b"\nSTDERR_BYTES="+values[b"stderr_len"]+b"\nSTDERR_SHA256="+values[b"stderr_sha256"]+b"\nSTDERR_EOF="+values[b"stderr_eof"]+b"\nSTDERR_OVERFLOW="+values[b"stderr_overflow"]+b"\nCGROUP_EMPTY="+values[b"cgroup_empty"]+b"\nPARSER_LANGUAGE="+values[b"parser_language"]+b"\nPARSER_SEMANTICS="+values[b"parser_semantics"]+b"\nCANDIDATE="+values[b"candidate"]+b"\nTERMINAL="+values[b"terminal"]+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+values[b"certificate_expiry_realtime_ns"]+b"\nTOPOLOGY=V15_INTERNAL_VALIDATION_REPORTED_BY_COMPLETE_TRANSCRIPT\nEXTERNAL_TOPOLOGY_RECONSTRUCTION=UNAVAILABLE\n")

def validated_record(context,values):
 seq=next_record(context);origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_PROBE_STATE_V3\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nSTATE=VALIDATED_CANDIDATE\n"+forensic_body(values)+b"B_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+values[b"probe"]+b"-validated.v3",body,deadline,True)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"VALIDATED_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"validated_sha"]=digest;context[b"validated_values"]=dict(values);return digest

def ack_intent_record(context,ordinal,probe,actor_ack,received):
 values=context[b"validated_values"];seq=next_record(context);origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_PROBE_STATE_V3\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=ACK_COMMIT_INTENT\n"+forensic_body(values)+b"ACTOR_ACK_INTENT_NS="+str(actor_ack).encode()+b"\nB_ACK_RECEIVED_NS="+str(received).encode()+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-ack-intent.v3",body,deadline,True)
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
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(actor_pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  remaining=deadline-time.monotonic_ns()
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
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if address is not None or not raw or bad:raise FaultSet({b"CONTROL_MALFORMED"})
    if raw.startswith(b"V3_ABORT|"):
     values,faults=parse_abort(raw)
     if installed or ancillary:faults.add(b"FD_TRANSFER")
     raise RemoteAbort(faults)
    if rights==0:
     if installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    else:
     if len(ancillary)!=1 or len(installed)!=rights:raise FaultSet({b"FD_TRANSFER"})
    return raw,tuple(installed)
   except BaseException:
    close_numbers(installed);raise
  if amask:raise ActorLost("actor")
  if cmask&(select.POLLHUP|select.POLLERR):raise ActorLost("control")

def send_exact(control,raw,deadline):
 if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
 try:count=control.send(raw)
 except BaseException as error:raise ActorLost("send") from error
 if count!=len(raw):raise FaultSet({b"CONTROL_MALFORMED"})
 if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})

def kill_once(context,reason):
 if context[b"kill_state"]!=b"NOT_RESERVED":return
 context[b"kill_state"]=b"TICKET_COMMITTING"
 ticket=(b"P27E001_KILL_TICKET_V3\nAUTH_ID="+AUTH+b"\nPRIMARY="+reason+b"\nKILL_CALL_COUNT_BEFORE=0\nWRITE_BYTES_HEX=310a\nRETRY_ALLOWED=0\nTICKET_END=1\n")
 deadline=time.monotonic_ns()+RECORD_NS
 state,digest=durable_once(context,b"kill-ticket.v3",ticket,deadline,False)
 context[b"kill_ticket_state"]=state
 if state!=DURABLE_VERIFIED:context[b"faults"].add(b"KILL_TICKET_DURABILITY_UNKNOWN")
 context[b"kill_state"]=b"CALL_RESERVED"
 number=context.get(b"kill_fd",-1)
 if number<0:number=context.get(b"root_kill_fd",-1)
 if number<0:
  context[b"kill_state"]=b"CALL_UNAVAILABLE";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 context[b"kill_call_count"]=1;context[b"kill_state"]=b"CALL_ENTERED";call_deadline=time.monotonic_ns()+KILL_RETURN_NS
 try:returned=os.write(number,b"1\n")
 except BaseException:
  context[b"kill_state"]=b"RETURN_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 try:post_deadline(call_deadline);checkpoint(CERT,REPORT_NS,call_deadline)
 except BaseException:
  context[b"kill_state"]=b"RETURN_DEADLINE_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 if returned!=2:
  context[b"kill_state"]=b"SHORT_OR_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN")
 else:context[b"kill_state"]=b"RETURNED_2"

def begin_cleanup(context):
 if context[b"cleanup_origin"] is not None:return
 context[b"cleanup_origin"]=time.monotonic_ns();context[b"cleanup_deadline"]=context[b"cleanup_origin"]+CLEANUP_NS
 state=observe_population(context)
 if state is True:kill_once(context,primary(context[b"faults"]))

def retained_record(context,stop):
 if context[b"attempt"]<0:return
 origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_RETAINED_STATE_V3\nAUTH_ID="+AUTH+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nCLEANUP_ORIGIN_NS="+str(context[b"cleanup_origin"]).encode()+b"\nCLEANUP_DEADLINE_NS="+str(context[b"cleanup_deadline"]).encode()+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nRETRY_ALLOWED=0\nRETAINED_END=1\n")
 state,digest=durable_once(context,b"retained.v3",body,deadline,False)
 context[b"retained_state"]=state
 if state!=DURABLE_VERIFIED:context[b"faults"].add(b"RETAINED_DURABILITY_UNKNOWN")

def retained_until_empty(context,stop):
 retained_record(context,stop)
 while True:
  for key in (b"out_fd",b"err_fd"):
   number=context.get(key,-1)
   if number>=0:
    try:drain(number,bytearray())
    except FaultSet as error:context[b"faults"].update(error.faults)
  state=observe_population(context)
  if state is False:return
  try:select.poll().poll(50)
  except InterruptedError:pass

def direct_reap_value(context,actor_lost):
 if context[b"direct_reaps"]==context[b"entered"] and context[b"entered"]>0:return b"COMPLETE"
 if b"DIRECT_WAIT_UNKNOWN" in context[b"faults"]:return b"UNKNOWN"
 if actor_lost:return b"UNAVAILABLE_ACTOR_LOST"
 return b"UNKNOWN"

def recovery_record(context,stop,actor_lost):
 origin=time.monotonic_ns();deadline=origin+RECORD_NS;direct=direct_reap_value(context,actor_lost)
 body=(b"P27E001_RECOVERY_STATE_V3\nAUTH_ID="+AUTH+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nINTENT_DURABLE="+(b"1" if context[b"intent_durable"] else b"0")+b"\nCONSUMPTION_STATE="+context[b"consumption_state"]+b"\nDIRECT_REAP="+direct+b"\nSTDOUT_EOF="+(b"1" if context[b"last_out_eof"] else b"0")+b"\nSTDERR_EOF="+(b"1" if context[b"last_err_eof"] else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nKILL_TICKET_STATE="+context[b"kill_ticket_state"]+b"\nCGROUP_EMPTY=1\nCLEANUP_ORIGIN_NS="+str(context[b"cleanup_origin"]).encode()+b"\nCLEANUP_DEADLINE_NS="+str(context[b"cleanup_deadline"]).encode()+b"\nRETRY_ALLOWED=0\nDISPOSITION="+disposition(context[b"faults"])+b"\nRECOVERY_END=1\n")
 name=b"recovery.v3" if context[b"intent_durable"] else b"preintent.v3"
 state,digest=durable_once(context,name,body,deadline,False)
 context[b"recovery_state"]=state
 if state==DURABLE_VERIFIED:context[b"chain_sha"]=digest
 else:context[b"faults"].add(b"RECOVERY_DURABILITY_UNKNOWN")
 return state,digest

def parse_final_report(raw):
 values=parse_fixed(raw,b"P27E001_FINAL_REPORT_V3",FINAL_REPORT_KEYS,b"REPORT_END=1")
 need(values[b"AUTH_ID"]==AUTH and values[b"SUITE"]==b",".join(PROBES))
 entered=udec(values[b"ENTERED_COUNT"],0,15);committed=udec(values[b"COMMITTED_COUNT"],0,15);need(committed<=entered)
 h64(values[b"CHAIN_HEAD_SHA256"]);need(values[b"CGROUP_EMPTY"]==b"1" and values[b"CGROUP_REMOVED"] in (b"0",b"1"))
 need(values[b"FINAL_PASS_MARGIN_NS"]==str(PASS_MARGIN_NS).encode() and values[b"STAGE_RETAINED"]==values[b"ATTEMPT_RETAINED"]==b"1" and values[b"RETRY_ALLOWED"]==b"0")
 if values[b"DISPOSITION"]==b"PASS":
  need(entered==committed==15 and values[b"STOP_PROBE"]==values[b"PRIMARY"]==values[b"FAULT_SET"]==b"NONE")
  h64(values[b"TERMINAL_SEEN_SHA256"]);need(values[b"DIRECT_REAP"]==b"COMPLETE" and values[b"CGROUP_REMOVED"]==b"1")
  need(values[b"KILL_CALL_COUNT"]==b"0" and values[b"KILL_STATE"]==b"NOT_RESERVED" and values[b"CERTIFICATE_LIVE_AT_COMMIT"]==b"1")
  origin=udec(values[b"PASS_COMMIT_ORIGIN_MONOTONIC_NS"],1);deadline=udec(values[b"PASS_COMMIT_DEADLINE_MONOTONIC_NS"],1)
  need(deadline==origin+PASS_COMMIT_NS);return values
 faults=parse_fault_csv(values[b"FAULT_SET"],False);need(values[b"PRIMARY"]==primary(faults) and values[b"DISPOSITION"]==disposition(faults))
 need(values[b"STOP_PROBE"]==b"NONE" or values[b"STOP_PROBE"] in PROBES)
 need(values[b"TERMINAL_SEEN_SHA256"]==b"NONE" and values[b"DIRECT_REAP"] in (b"COMPLETE",b"UNKNOWN",b"UNAVAILABLE_ACTOR_LOST"))
 need(values[b"KILL_CALL_COUNT"] in (b"0",b"1") and values[b"KILL_STATE"] in (b"NOT_RESERVED",b"TICKET_COMMITTING",b"CALL_RESERVED",b"CALL_UNAVAILABLE",b"CALL_ENTERED",b"RETURN_UNKNOWN",b"RETURN_DEADLINE_UNKNOWN",b"SHORT_OR_UNKNOWN",b"RETURNED_2"))
 need(values[b"CERTIFICATE_LIVE_AT_COMMIT"]==b"0" and values[b"PASS_COMMIT_ORIGIN_MONOTONIC_NS"]==values[b"PASS_COMMIT_DEADLINE_MONOTONIC_NS"]==b"0")
 need(values[b"DISPOSITION"] in (b"CONSUMED_FAIL",b"CONSUMED_INDETERMINATE"));return values

def failure_report(context,stop,actor_lost):
 origin=time.monotonic_ns();deadline=origin+REPORT_NS;direct=direct_reap_value(context,actor_lost);disp=disposition(context[b"faults"])
 body=(b"P27E001_FINAL_REPORT_V3\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT="+str(context[b"entered"]).encode()+b"\nCOMMITTED_COUNT="+str(sum(context[b"committed"])).encode()+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nCHAIN_HEAD_SHA256="+context[b"chain_sha"]+b"\nTERMINAL_SEEN_SHA256=NONE\nDIRECT_REAP="+direct+b"\nCGROUP_EMPTY=1\nCGROUP_REMOVED="+(b"1" if context[b"removed"] else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nCERTIFICATE_LIVE_AT_COMMIT=0\nPASS_COMMIT_ORIGIN_MONOTONIC_NS=0\nPASS_COMMIT_DEADLINE_MONOTONIC_NS=0\nFINAL_PASS_MARGIN_NS=10000000\nSTAGE_RETAINED=1\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION="+disp+b"\nREPORT_END=1\n")
 parse_final_report(body)
 state,digest=durable_once(context,b"report.v3",body,deadline,False)
 context[b"report_state"]=state;context[b"report_sha"]=digest
 if state!=DURABLE_VERIFIED:context[b"faults"].add(b"REPORT_DURABILITY_UNKNOWN")
 return state,digest,disp

def final_candidate(context):
 origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_FINAL_CANDIDATE_V3\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT=15\nCOMMITTED_COUNT=15\nCHAIN_HEAD_SHA256="+context[b"chain_sha"]+b"\nDIRECT_REAP=COMPLETE\nCGROUP_EMPTY=1\nCGROUP_REMOVED=1\nKILL_CALL_COUNT=0\nKILL_STATE=NOT_RESERVED\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCLONE3_GATE_ID="+CERT[b"CLONE3_CPYTHON_GATE_ID"]+b"\nDELETED_CGROUP_GATE_ID="+CERT[b"DELETED_CGROUP_FD_GATE_ID"]+b"\nELIGIBLE=1\nCANDIDATE_END=1\n")
 state,digest=durable_once(context,b"final-candidate.v3",body,deadline,True,PASS_COMMIT_NS+PASS_MARGIN_NS+TERMINAL_NS)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"REPORT_CANDIDATE_DURABILITY_UNKNOWN"})
 context[b"candidate_sha"]=digest;return digest

def terminal_seen_record(context,candidate_sha):
 origin=time.monotonic_ns();deadline=origin+RECORD_NS
 body=(b"P27E001_TERMINAL_SEEN_V3\nAUTH_ID="+AUTH+b"\nPREDECESSOR_SHA256="+candidate_sha+b"\nCANDIDATE_SHA256="+candidate_sha+b"\nACTOR_SEEN=1\nB_RECEIVE_MONOTONIC_NS="+str(origin).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nSEEN_END=1\n")
 state,digest=durable_once(context,b"terminal-seen.v3",body,deadline,True,PASS_COMMIT_NS+PASS_MARGIN_NS)
 if state!=DURABLE_VERIFIED:raise FaultSet({b"TERMINAL_SEEN_DURABILITY_UNKNOWN"})
 context[b"terminal_seen_sha"]=digest;return digest

def pass_report(context):
 origin=time.monotonic_ns();deadline=origin+PASS_COMMIT_NS
 checkpoint(CERT,PASS_COMMIT_NS+PASS_MARGIN_NS,deadline)
 body=(b"P27E001_FINAL_REPORT_V3\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT=15\nCOMMITTED_COUNT=15\nSTOP_PROBE=NONE\nPRIMARY=NONE\nFAULT_SET=NONE\nCHAIN_HEAD_SHA256="+context[b"chain_sha"]+b"\nTERMINAL_SEEN_SHA256="+context[b"terminal_seen_sha"]+b"\nDIRECT_REAP=COMPLETE\nCGROUP_EMPTY=1\nCGROUP_REMOVED=1\nKILL_CALL_COUNT=0\nKILL_STATE=NOT_RESERVED\nCERTIFICATE_LIVE_AT_COMMIT=1\nPASS_COMMIT_ORIGIN_MONOTONIC_NS="+str(origin).encode()+b"\nPASS_COMMIT_DEADLINE_MONOTONIC_NS="+str(deadline).encode()+b"\nFINAL_PASS_MARGIN_NS=10000000\nSTAGE_RETAINED=1\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION=PASS\nREPORT_END=1\n")
 parse_final_report(body)
 state,digest=durable_once(context,b"report.v3",body,deadline,True,PASS_MARGIN_NS)
 context[b"report_state"]=state;context[b"report_sha"]=digest
 if state!=DURABLE_VERIFIED:raise FaultSet({b"REPORT_DURABILITY_UNKNOWN"})
 return digest

def send_result(control,ordinal,probe,pid,context,stdout,stderr,out_eof,err_eof,out_over,err_over,empty,faults,done):
 deadline=context[b"origin"]+HOST_NS;out_frames=(len(stdout)+64999)//65000;err_frames=(len(stderr)+64999)//65000
 header=packet(b"V3_RESULT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_bound",b"1" if context[b"pidfd_bound"] else b"0"),(b"pidfd_exit_ready_observed",b"1" if context[b"pidfd_exit_ready_observed"] else b"0"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1" if out_eof else b"0"),(b"stdout_frames",str(out_frames).encode()),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",sha(stderr)),(b"stderr_eof",b"1" if err_eof else b"0"),(b"stderr_frames",str(err_frames).encode()),(b"cgroup_empty",b"1" if empty else b"0"),(b"fault_set",fault_csv(faults)),(b"capture_done_ns",str(done).encode())))
 send_exact(control,header,deadline)
 for stream,raw in ((b"STDOUT",stdout),(b"STDERR",stderr)):
  for index,start in enumerate(range(0,len(raw),65000)):
   payload=raw[start:start+65000]
   frame=packet(b"V3_RESULT_FRAME",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"stream",stream),(b"index",str(index).encode()),(b"bytes",str(len(payload)).encode()),(b"sha256",sha(payload))))+payload
   send_exact(control,frame,deadline)
 send_exact(control,b"V3_RESULT_END\n",deadline)

def stream_arm(control,context,ordinal,probe):
 keys=(b"ordinal",b"probe",b"release_origin_ns",b"launch_deadline_ns",b"stdout_dev",b"stdout_ino",b"stderr_dev",b"stderr_ino",b"events_dev",b"events_ino",b"kill_dev",b"kill_ino")
 raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,4);values=parse_packet(raw,b"V3_STREAM_ARM",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 origin=udec(values[b"release_origin_ns"],1);launch=udec(values[b"launch_deadline_ns"],1);need(origin<launch==origin+1000000000)
 post_deadline(launch);checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS,launch)
 out,err,events,kill=fds
 try:
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
  try:
   a=os.fstat(own_events);b=os.fstat(own_kill)
   need((a.st_dev,a.st_ino)==(eventss.st_dev,eventss.st_ino) and (b.st_dev,b.st_ino)==(kills.st_dev,kills.st_ino))
  finally:close_numbers((own_events,own_kill))
 except BaseException:
  close_numbers(fds);raise
 context.update({b"out_fd":out,b"err_fd":err,b"events_fd":events,b"kill_fd":kill,b"origin":origin,b"launch":launch,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False})
 send_exact(control,b"V3_STREAMS_ARMED\n",launch);checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS,launch)

def pidfd_arm(control,context,ordinal,probe):
 raw,fds=recv_monitored(control,4,context[b"launch"],1)
 values=parse_packet(raw,b"V3_PIDFD_ARM",(b"ordinal",b"probe",b"outer_pid",b"stopped_raw_status",b"cgroup_member",b"pidfd_bound"))
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 pid=udec(values[b"outer_pid"],2);number=fds[0];stopped=udec(values[b"stopped_raw_status"],1)
 need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and values[b"cgroup_member"]==values[b"pidfd_bound"]==b"1")
 try:
  fd_access(number,os.O_RDWR);need(pidfd_pid(number)==pid)
  procs=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  status=os.open(b"/proc/"+str(pid).encode()+b"/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  try:
   need(read_all(procs,64)==str(pid).encode()+b"\n")
   state=[x for x in ascii_file(read_all(status,65536),65536).splitlines() if x.startswith(b"State:\t")]
   need(len(state)==1 and state[0].startswith(b"State:\tT"))
  finally:close_numbers((procs,status))
 except BaseException:
  os.close(number);raise
 context[b"outer_pidfd"]=number;context[b"outer_pid"]=pid;context[b"pidfd_bound"]=True;context[b"pidfd_exit_ready_observed"]=False
 reply=packet(b"V3_PIDFD_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"pidfd_bound",b"1")))
 send_exact(control,reply,context[b"launch"]);checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS,context[b"launch"])

def release_phase(control,context,ordinal,probe):
 raw,fds=recv_monitored(control,4,context[b"launch"],0);need(fds==())
 keys=(b"ordinal",b"probe",b"outer_pid",b"pidfd_bound",b"stopped_raw_status",b"cgroup_member",b"cgroup_dev",b"cgroup_ino",b"cgroup_mode",b"cgroup_nlink",b"cgroup_uid",b"cgroup_gid",b"argv_sha256",b"env_sha256",b"release_origin_ns",b"launch_deadline_ns")
 values=parse_packet(raw,b"V3_RELEASE_CANDIDATE",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==context[b"outer_pid"] and values[b"pidfd_bound"]==values[b"cgroup_member"]==b"1")
 h64(values[b"argv_sha256"]);h64(values[b"env_sha256"]);need(udec(values[b"release_origin_ns"])==context[b"origin"] and udec(values[b"launch_deadline_ns"])==context[b"launch"])
 cg=os.fstat(context[b"cgfd"]);observed=(cg.st_dev,cg.st_ino,format(cg.st_mode,"o").encode(),cg.st_nlink,cg.st_uid,cg.st_gid)
 supplied=(udec(values[b"cgroup_dev"],1),udec(values[b"cgroup_ino"],1),values[b"cgroup_mode"],udec(values[b"cgroup_nlink"],1),udec(values[b"cgroup_uid"]),udec(values[b"cgroup_gid"]))
 need(observed==supplied)
 checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS,context[b"launch"]);digest=release_record(context,values)
 reply=packet(b"V3_RELEASE_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_sha256",digest)))
 send_exact(control,reply,context[b"launch"]);checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS,context[b"launch"])

def monitor_probe(control,context,ordinal,probe):
 stdout=bytearray();stderr=bytearray();out_eof=err_eof=out_over=err_over=False;faults=set();actor_lost=False
 deadline=context[b"origin"]+HOST_NS;poller=select.poll()
 for number in (context[b"out_fd"],context[b"err_fd"],context[b"events_fd"],context[b"outer_pidfd"],4,control.fileno()):poller.register(number,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
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

def terminal_failure(control,context,stop,faults,actor_lost):
 context[b"faults"].update(faults)
 if not context[b"faults"]:context[b"faults"].add(b"INTERNAL_INVARIANT")
 if b"DIRECT_WAIT_UNKNOWN" in context[b"faults"]:context[b"direct_reap_state"]=b"UNKNOWN"
 if context[b"attempt"]<0:retain_attempt_dirfd(context)
 begin_cleanup(context)
 while time.monotonic_ns()<context[b"cleanup_deadline"]:
  for key in (b"out_fd",b"err_fd"):
   number=context.get(key,-1)
   if number>=0:
    try:drain(number,bytearray())
    except FaultSet as error:context[b"faults"].update(error.faults)
  state=observe_population(context)
  if state is True and context[b"kill_state"]==b"NOT_RESERVED" and time.monotonic_ns()<context[b"cleanup_deadline"]:kill_once(context,primary(context[b"faults"]))
  if state is False:break
  try:select.poll().poll(10)
  except InterruptedError:pass
 state=observe_population(context)
 if state is not False:retained_until_empty(context,stop)
 recovery_record(context,stop,actor_lost)
 report_state,report_sha,disp=failure_report(context,stop,actor_lost)
 if report_state!=DURABLE_VERIFIED:
  while True:
   for key in (b"out_fd",b"err_fd"):
    number=context.get(key,-1)
    if number>=0:
     try:drain(number,bytearray())
     except BaseException:pass
   try:select.poll().poll(50)
   except InterruptedError:pass
 if actor_lost:return disp
 try:
  notice=packet(b"V3_TERMINAL_FAILURE_DURABLE",((b"report_sha256",report_sha),(b"disposition",disp)))
  send_exact(control,notice,time.monotonic_ns()+TERMINAL_NS)
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+TERMINAL_NS,0);need(fds==())
  seen=parse_packet(raw,b"V3_TERMINAL_SEEN",(b"kind",b"subject_sha256"))
  need(seen[b"kind"]==b"FAILURE" and seen[b"subject_sha256"]==report_sha)
  ack=packet(b"V3_TERMINAL_ACK",((b"kind",b"FAILURE"),(b"subject_sha256",report_sha),(b"closure",b"SEEN")))
  send_exact(control,ack,time.monotonic_ns()+TERMINAL_NS)
 except (ActorLost,FaultSet,RemoteAbort):pass
 return disp

def validated_exchange(control,context,ordinal,probe,stdout,stderr):
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 values=parse_packet(raw,b"V3_VALIDATED_CANDIDATE",CANDIDATE_KEYS)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 need(values[b"release_record_sha256"]==context[b"release_sha"] and udec(values[b"release_origin_ns"])==context[b"origin"])
 release_return=udec(values[b"release_return_ns"]);host_complete=udec(values[b"host_complete_ns"]);capture_done=udec(values[b"capture_done_ns"])
 need(context[b"origin"]<release_return<=context[b"launch"] and capture_done<=host_complete<=context[b"origin"]+HOST_NS)
 need(values[b"direct_wait_state"]==b"COMPLETE" and values[b"outer_raw_status"]==b"0")
 need(values[b"pidfd_bound"]==values[b"pidfd_exit_ready_observed"]==b"1")
 need(udec(values[b"stdout_len"])==len(stdout) and values[b"stdout_sha256"]==sha(stdout) and values[b"stdout_eof"]==b"1" and values[b"stdout_overflow"]==b"0")
 need(udec(values[b"stderr_len"])==len(stderr)==0 and values[b"stderr_sha256"]==sha(stderr) and values[b"stderr_eof"]==b"1" and values[b"stderr_overflow"]==b"0")
 need(values[b"cgroup_empty"]==b"1" and values[b"parser_language"]==values[b"parser_semantics"]==values[b"candidate"]==values[b"terminal"]==b"ACCEPTED")
 need(values[b"certificate_expiry_realtime_ns"]==CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 h64(values[b"stdout_sha256"]);h64(values[b"stderr_sha256"]);checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS,context[b"origin"]+TOTAL_NS)
 validated_sha=validated_record(context,values)
 reply=packet(b"V3_VALIDATED_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha)))
 send_exact(control,reply,context[b"origin"]+TOTAL_NS)
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 intent=parse_packet(raw,b"V3_ACK_COMMIT_INTENT",(b"ordinal",b"probe",b"validated_sha256",b"actor_ack_intent_ns"))
 need(udec(intent[b"ordinal"],0,14)==ordinal and intent[b"probe"]==probe and intent[b"validated_sha256"]==validated_sha)
 actor_ack=udec(intent[b"actor_ack_intent_ns"]);received=time.monotonic_ns();need(actor_ack<=received)
 checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS,context[b"origin"]+TOTAL_NS)
 ack_sha=ack_intent_record(context,ordinal,probe,actor_ack,received)
 checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS,context[b"origin"]+TOTAL_NS)
 context[b"committed"][ordinal]=True;context[b"direct_reaps"]+=1;context[b"direct_reap_state"]=b"COMPLETE"
 committed=packet(b"V3_COMMITTED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha)))
 send_exact(control,committed,context[b"origin"]+TOTAL_NS)
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 seen=parse_packet(raw,b"V3_COMMITTED_SEEN",(b"ordinal",b"probe",b"ack_sha256"))
 need(udec(seen[b"ordinal"],0,14)==ordinal and seen[b"probe"]==probe and seen[b"ack_sha256"]==ack_sha)
 checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS,context[b"origin"]+TOTAL_NS);return ack_sha

def containment_bind(control,context):
 deadline=time.monotonic_ns()+ACK_NS;raw,fds=recv_monitored(control,4,deadline,1)
 values=parse_packet(raw,b"V3_CONTAINMENT",(b"dev",b"ino",b"mode",b"nlink",b"uid",b"gid"));number=fds[0]
 try:
  held=os.fstat(number);need(stat.S_ISDIR(held.st_mode))
  supplied=(udec(values[b"dev"],1),udec(values[b"ino"],1),octal(values[b"mode"]),udec(values[b"nlink"],1),udec(values[b"uid"]),udec(values[b"gid"]))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==supplied)
  need(values[b"mode"]==CERT[b"CGROUP_CHILD_MODE"] and values[b"uid"]==CERT[b"CGROUP_CHILD_UID"] and values[b"gid"]==CERT[b"CGROUP_CHILD_GID"] and values[b"nlink"]==b"2")
  named=os.stat(AUTH,dir_fd=6,follow_symlinks=False);need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  try:
   need(read_all(ctype,128).hex().encode()==CERT[b"CGROUP_CHILD_TYPE_HEX"])
   need(read_all(controllers,4096).hex().encode()==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"])
   need(read_all(subtree,4096).hex().encode()==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"])
   need(not populated(root_events))
  finally:close_numbers((ctype,controllers,subtree))
 except BaseException:
  try:os.close(number)
  except OSError:pass
  raise
 context[b"cgfd"]=number;context[b"root_events_fd"]=root_events;context[b"root_kill_fd"]=root_kill
 context[b"cgroup_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
 send_exact(control,b"V3_CONTAINMENT_ACK\n",deadline);checkpoint(CERT,15*TOTAL_NS+REPORT_NS,deadline)

def static_inputs():
 global AUTH,CERT,DEPS
 need(type(sys.argv)is list and len(sys.argv)==8 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RECOVER_V3")
 supplied=h64(sys.argv[2].encode("ascii"));actor_pid=udec(sys.argv[3].encode("ascii"),2)
 plan_sha=h64(sys.argv[4].encode("ascii"));source_sha=h64(sys.argv[5].encode("ascii"))
 safe_dev=udec(sys.argv[6].encode("ascii"),1);safe_ino=udec(sys.argv[7].encode("ascii"),1)
 need(os.read(0,1)==b"");fd_access(0,os.O_RDONLY);need(stat.S_ISFIFO(os.fstat(0).st_mode));closed(1);closed(2)
 control=socket.socket(fileno=3);need(control.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET);fd_access(3,os.O_RDWR)
 peer=struct.unpack("3i",control.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(actor_pid,0,0))
 fd_access(4,os.O_RDWR);need(pidfd_pid(4)==actor_pid)
 for number in (7,8,9,100):seals(number);fd_access(number,os.O_RDWR)
 snapshot_raw=whole_snapshot();cert_raw=read_all(7);envelope_raw=read_all(8);source_raw=read_all(100)
 CERT,DEPS=contract(cert_raw);issued=envelope(envelope_raw)
 need(sha(cert_raw)==issued[b"CERTIFICATE_SHA256"] and sha(envelope_raw)==CERT[b"ISSUER_ENVELOPE_SHA256"])
 AUTH=sha(b"P27E001V3\x00"+cert_raw+b"\x00"+envelope_raw);need(AUTH==supplied)
 need(plan_sha==CERT[b"PLAN_SHA256"]==issued[b"PLAN_SHA256"])
 need(issued[b"RUNNER_SHA256"]==CERT[b"RUNNER_SHA256"])
 need(source_sha==sha(source_raw)==CERT[b"RECOVERY_SHA256"]==issued[b"RECOVERY_SHA256"])
 need(issued[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot_raw)==SNAPSHOT_EXPECT[2])
 need(issued[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and issued[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672")
 need(issued[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX)
 need(issued[b"V15_SHA256"]==CERT[b"V15_SHA256"]==V15_SHA)
 base_check(5,CERT,b"ATTEMPT_BASE");base_check(6,CERT,b"CGROUP_BASE")
 attempt_mid,attempt_line=mount_binding(5)
 need(attempt_mid==udec(CERT[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==CERT[b"ATTEMPT_BASE_MOUNTINFO_SHA256"])
 cgroup_mid,cgroup_line=mount_binding(6)
 need(statfs_magic(6)==int(CERT[b"CGROUP2_FS_MAGIC"],16) and cgroup_mid==udec(CERT[b"CGROUP2_MOUNT_ID"],1) and sha(cgroup_line)==CERT[b"CGROUP2_MOUNTINFO_SHA256"])
 base_type=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
 base_controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
 base_subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
 try:
  need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"])
  need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"])
  need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"])
 finally:close_numbers((base_type,base_controllers,base_subtree))
 need((safe_dev,safe_ino)==(udec(CERT[b"SAFE_BIND_DEV"],1),udec(CERT[b"SAFE_BIND_INO"],1)))
 final_context(safe_dev,safe_ino);scrub_exact({0,3,4,5,6,7,8,9,100});checkpoint(CERT,283472000000)
 return control,cert_raw,envelope_raw,source_raw

def minimal_context():
 return {b"attempt":-1,b"consumed":False,b"consumption_state":b"PREARMED",b"intent_durable":False,b"faults":set(),b"durability":{},b"record_seq":0,b"chain_sha":b"0"*64,b"committed":[False]*15,b"entered":0,b"direct_reaps":0,b"direct_reap_state":b"UNAVAILABLE",b"kill_call_count":0,b"kill_state":b"NOT_RESERVED",b"kill_ticket_state":b"ABSENT_KNOWN",b"cleanup_origin":None,b"cleanup_deadline":None,b"last_out_eof":False,b"last_err_eof":False,b"cgfd":-1,b"root_events_fd":-1,b"root_kill_fd":-1,b"events_fd":-1,b"kill_fd":-1,b"out_fd":-1,b"err_fd":-1,b"outer_pidfd":-1,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False,b"outer_pid":-1,b"removed":False,b"report_state":b"ABSENT_KNOWN",b"report_sha":b"0"*64,b"retained_state":b"ABSENT_KNOWN"}

def ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error):
 context[b"consumed"]=True;context[b"consumption_state"]=b"CONSUME_EDGE_UNKNOWN";context[b"faults"].add(b"CONSUME_EDGE_UNKNOWN")
 if isinstance(error,RemoteAbort):context[b"faults"].update(error.faults)
 elif isinstance(error,FaultSet):context[b"faults"].update(error.faults)
 elif isinstance(error,ActorLost):context[b"faults"].add(b"ACTOR_LOST")
 try:consume_attempt(context,cert_raw,envelope_raw,source_raw)
 except FaultSet as attempt_error:context[b"faults"].update(attempt_error.faults)
 terminal_failure(control,context,b"NONE",set(context[b"faults"]),isinstance(error,ActorLost))

def wait_actor_loss():
 poller=select.poll();poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  try:events=poller.poll(50)
  except InterruptedError:continue
  if events:return

def main():
 control,cert_raw,envelope_raw,source_raw=static_inputs();context=minimal_context();armed=False
 try:
  boot_deadline=time.monotonic_ns()+10000000000;send_exact(control,b"V3_READY\n",boot_deadline)
  raw,fds=recv_monitored(control,4,boot_deadline,0);need(fds==())
  if raw==b"V3_REFUSE_PRECOMMIT\n":
   send_exact(control,b"V3_REFUSE_ACK\n",boot_deadline);return
  need(raw==b"V3_CONSUME_BEGIN\n");checkpoint(CERT,283472000000,boot_deadline)
  context[b"consumption_state"]=b"ARMED";send_exact(control,b"V3_CONSUME_ARMED\n",boot_deadline);armed=True
  consume_deadline=time.monotonic_ns()+CONSUMPTION_NS
  try:raw,fds=recv_monitored(control,4,consume_deadline,0);need(fds==())
  except (ActorLost,RemoteAbort,FaultSet) as error:
   ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error);return
  if raw==b"V3_REFUSE_PRECOMMIT\n":
   send_exact(control,b"V3_REFUSE_ACK\n",consume_deadline);return
  if raw!=b"V3_CONSUME_COMMIT\n":
   ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,FaultSet({b"CONTROL_MALFORMED"}));return
  context[b"consumed"]=True;context[b"consumption_state"]=b"COMMIT_RECEIVED"
  try:intent_sha=consume_attempt(context,cert_raw,envelope_raw,source_raw)
  except FaultSet as error:
   context[b"faults"].update(error.faults);terminal_failure(control,context,b"NONE",set(context[b"faults"]),False);return
  checkpoint(CERT,283472000000,consume_deadline)
  consumed=packet(b"V3_CONSUMED_DURABLE",((b"intent_sha256",intent_sha),));send_exact(control,consumed,consume_deadline)
  stage_deadline=time.monotonic_ns()+10000000000;raw,fds=recv_monitored(control,4,stage_deadline,0);need(fds==())
  stage=parse_packet(raw,b"V3_STAGE_DURABLE",(b"safe_dev",b"safe_ino",b"stage_return_ns"))
  need(udec(stage[b"safe_dev"],1)>0 and udec(stage[b"safe_ino"],1)>0 and udec(stage[b"stage_return_ns"])<=stage_deadline)
  checkpoint(CERT,15*TOTAL_NS+REPORT_NS,stage_deadline);send_exact(control,b"V3_STAGE_ACK\n",stage_deadline)
  containment_bind(control,context)
  for ordinal,probe in enumerate(PROBES):
   context[b"entered"]=ordinal+1;checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS)
   try:
    stream_arm(control,context,ordinal,probe)
    pidfd_arm(control,context,ordinal,probe)
    release_phase(control,context,ordinal,probe)
    actor_lost,faults,empty,stdout,stderr=monitor_probe(control,context,ordinal,probe)
    if actor_lost:
     terminal_failure(control,context,probe,faults|{b"ACTOR_LOST"},True);return
    if faults:
     try:
      raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0)
      context[b"faults"].add(b"CONTROL_MALFORMED")
     except RemoteAbort as error:context[b"faults"].update(error.faults)
     except ActorLost:
      context[b"faults"].add(b"ACTOR_LOST");actor_lost=True
     except FaultSet as error:context[b"faults"].update(error.faults)
     terminal_failure(control,context,probe,set(context[b"faults"]),actor_lost);return
    try:validated_exchange(control,context,ordinal,probe,stdout,stderr)
    except RemoteAbort as error:
     context[b"faults"].update(error.faults);terminal_failure(control,context,probe,set(context[b"faults"]),False);return
    except ActorLost:
     context[b"faults"].add(b"ACTOR_LOST");terminal_failure(control,context,probe,set(context[b"faults"]),True);return
    except FaultSet as error:
     context[b"faults"].update(error.faults);terminal_failure(control,context,probe,set(context[b"faults"]),False);return
    close_probe(context);checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS)
  final_deadline=time.monotonic_ns()+REPORT_NS
  raw,fds=recv_monitored(control,4,final_deadline,0);need(fds==() and raw==b"V3_EMPTY_FINAL_QUERY\n")
  checkpoint(CERT,REPORT_NS,final_deadline);need(observe_population(context) is False)
  send_exact(control,b"V3_EMPTY_FINAL_CONFIRMED\n",final_deadline)
  raw,fds=recv_monitored(control,4,final_deadline,0);need(fds==())
  removed=parse_packet(raw,b"V3_CGROUP_REMOVED",(b"chain_head_sha256",));need(removed[b"chain_head_sha256"]==context[b"chain_sha"])
  try:os.stat(AUTH,dir_fd=6,follow_symlinks=False);need(False)
  except FileNotFoundError:pass
  context[b"removed"]=True;checkpoint(CERT,REPORT_NS,final_deadline)
  ack=packet(b"V3_REMOVE_ACK",((b"chain_head_sha256",context[b"chain_sha"]),));send_exact(control,ack,final_deadline)
  raw,fds=recv_monitored(control,4,final_deadline,0);need(fds==())
  finalize=parse_packet(raw,b"V3_FINALIZE_CANDIDATE",(b"chain_head_sha256",));need(finalize[b"chain_head_sha256"]==context[b"chain_sha"])
  need(context[b"entered"]==sum(context[b"committed"])==context[b"direct_reaps"]==15 and not context[b"faults"] and context[b"kill_call_count"]==0 and context[b"kill_state"]==b"NOT_RESERVED")
  candidate_sha=final_candidate(context)
  notice=packet(b"V3_TERMINAL_CANDIDATE_DURABLE",((b"candidate_sha256",candidate_sha),(b"chain_head_sha256",context[b"chain_sha"])))
  send_exact(control,notice,final_deadline)
  raw,fds=recv_monitored(control,4,final_deadline,0);need(fds==())
  seen=parse_packet(raw,b"V3_TERMINAL_SEEN",(b"kind",b"subject_sha256"))
  need(seen[b"kind"]==b"SUCCESS_CANDIDATE" and seen[b"subject_sha256"]==candidate_sha)
  terminal_sha=terminal_seen_record(context,candidate_sha);report_sha=pass_report(context)
  terminal=packet(b"V3_TERMINAL_ACK",((b"kind",b"SUCCESS"),(b"candidate_sha256",candidate_sha),(b"terminal_seen_sha256",terminal_sha),(b"report_sha256",report_sha)))
  try:send_exact(control,terminal,time.monotonic_ns()+TERMINAL_NS)
  except BaseException:wait_actor_loss()
 except RemoteAbort as error:
  if context[b"consumed"]:
   context[b"faults"].update(error.faults);terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
 except ActorLost:
  if armed and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,ActorLost("actor"))
  elif context[b"consumed"]:
   context[b"faults"].add(b"ACTOR_LOST");terminal_failure(control,context,b"NONE",set(context[b"faults"]),True)
 except CertificateExpired:
  if context[b"consumed"]:
   context[b"faults"].add(b"CERTIFICATE_EXPIRED");terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
 except FaultSet as error:
  if armed and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:
   context[b"faults"].update(error.faults);terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
 except BaseException:
  if armed and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,FaultSet({b"INTERNAL_INVARIANT"}))
  elif context[b"consumed"]:
   context[b"faults"].add(b"INTERNAL_INVARIANT");terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
 finally:
  close_probe(context)
  close_numbers(tuple(context.get(key,-1) for key in (b"root_events_fd",b"root_kill_fd",b"cgfd",b"attempt") if context.get(key,-1)>=0))
  try:control.close()
  except BaseException:pass

try:
 main()
except BaseException:
 raise SystemExit(96)
raise SystemExit(0)
P27 RUNNER V3 WATCHDOG SOURCE END D8E5A103

## 16. Frozen literal identities and raw structural census

A literal span is every byte after its BEGIN delimiter LF and before the
first byte of its END delimiter. The final source LF is included; neither
delimiter is included. Raw line slicing, wc, and sha256sum give:

record                 absolute source lines  bytes  LF    SHA256
A actor including C    604-1716               76971  1113  3a56c438fae58ecbb48bff7c19f61b682cc778d7456988dd33904ca93e0e4b2e
C embedded validator   1084-1181               9943    98  c3662ab9e09c133b79f80ca914e0650479d9d8c3a28b3f32da2520b0cb552190
B persistent watchdog  1720-2728              75004  1009  71647ce39758f59aef8eb3df2d1b5351ecf03437fa2138eedc557d5e980311d7

The exact A BEGIN/END, C BEGIN/END, and B BEGIN/END delimiter lines each
occur once. C is one contiguous uniquely delimited subspan of A. A
constructs the delimiter search strings from fragments, so neither complete
delimiter line is duplicated inside a source span.

Raw neighborhood inspection covered every column-zero def/class transition
in A, C, and B. Every such transition is preceded by an empty LF-delimited
line; no definition, try, except, finally, return, or top-level main boundary
is concatenated with its neighbor. The corrected C line " return rows" has
exactly one leading ASCII space and is line 1181. This was raw text
inspection only, not language parsing or validation.

Any mismatch in these span bytes, LF counts, delimiters, absolute locations,
or hashes is INPUT_AUTH. A future carrier must preserve them byte-for-byte;
normalization, comment stripping, formatting, indentation repair, or source
regeneration is forbidden.

## 17. Exact raw callsite and authority census

The A and B FAULT_ORDER tuples are byte-identical and have 44 members. They
separately include direct-wait, recovery-durability, retained-durability,
candidate, terminal-seen, and report-durability unknown effects. B's
KNOWN_FAIL set contains only CAPTURE_OVERFLOW, STDERR_NONEMPTY, OUTER_STATUS,
TRANSCRIPT_LANGUAGE, and TRANSCRIPT_SEMANTICS; every other member is
indeterminate. The canonical tuple order alone chooses PRIMARY.

Raw callsites inside A:

operation                                      callsites
os.fork for the one persistent B               1
raw LIBC.syscall(SYS_CLONE3)                    1
os.execve for B and OUTER                       2
central os.waitpid text                         1
payload SIGCONT                                 1
payload pre-context SIGSTOP                     1
stage/cgroup os.mkdir                           2
recvmsg intake                                  1
SCM_RIGHTS helper definition                    1
SCM_RIGHTS transfers                            3

The three A rights transfers are, in order, four stream/containment FDs, one
OUTER pidfd, and one child-cgroup dirfd. The one os.waitpid text is the
central wait_status implementation used for direct stopped/final waits and
the direct B wait; no second wait implementation exists.

Raw callsites inside B:

operation                                      callsites
direct fork/clone/exec/wait/SIGCONT             0
attempt os.mkdir                                1
O_CREAT|O_EXCL durable helper definition        1
durable_once callsites                          11
recvmsg ancillary intake                        1
direct cgroup.kill os.write                      1
kill retry or second direct kill                0
parse_final_report definition/calls             1/2

The eleven durable callsites are intent, release, validated receipt,
ACK-intent receipt, kill ticket, retained state, recovery/preintent, failure
report, final candidate, terminal-seen receipt, and PASS report. Failure and
PASS report constructors both pass through the one exact report parser. The
only cgroup.kill effect text is os.write(number,b"1\n"); write_all never
targets cgroup.kill.

Exact sole ownership is:

authority                                      owner
sealed E0366/V15/plan/source authentication    A; B independently reparses its inputs
issuer authenticity and serial replay          future external issuer authority
one-shot attempt and durable intent             B
V15 extraction and four-leaf staging           A
raw clone3, stopped wait, and SIGCONT           A
dynamic streams/cgroup/pidfd recheck            B
release, validated, and ACK-intent records      B
direct OUTER final wait                         A
dual-stream drain, framing, caps, and empty     B
transcript language and C semantics             A
one kill, cleanup origin, retained ownership    B
candidate, terminal-seen, and final report      B
direct B wait                                   A

B has no release, source extraction, staging, fork, clone, exec, semantic
transcript parser, or wait authority. A has no attempt-directory writer,
report writer, cgroup.kill writer, or substitute PID/PGID cleanup path.

## 18. E0366 correction closure matrix

rule  literal/prose closure
1     fresh V3 domains/delimiters plus sections 16-19 identity closure
2     corrected C line 1181 and raw function-boundary review in section 16
3     A sets CONSUME_EDGE_UNKNOWN/consumed/PREFLIGHT before COMMIT send
4     B's post-mkdir next fallible call is no-follow open and dirfd publish
5     durable_once partial FSM; ticket/recovery/retained/report sticky states
6     DIRECT_WAIT_UNKNOWN is distinct from known OUTER_STATUS
7     integrated checkpoint plus literal consume/stage/release/ACK/kill/final caps
8     non-PASS final-candidate, terminal-seen receipt, then margin-bound PASS
9     POLLIN-before-HUP and TERMINAL_SEEN followed by B TERMINAL_ACK
10    fd101/fd9 exact sealed E0366 snapshot, with no current-ledger identity
11    FINAL_REPORT_KEYS and parse_final_report exact disjoint branches
12    global recv ABORT recognition and complete canonical sticky fault set
13    recvmsg at rights zero/nonzero, truncation rejection, and FD cleanup
14    one cleanup origin/cap, one kill reservation, retained-until-empty owner
15    split pidfd states, chained receipts, exact FDs/cgroup, full B cert parse
16    unresolved gate references remain non-self-certifying and non-executable

The consume edge uses a fresh 100000000 ns consume_deadline on both actors,
not the 10000000000 ns preconsumption horizon. Successful attempt mkdir is
followed by immediate no-follow dirfd acquisition and publication before
base fsync. durable_once publishes every partial effect before the call,
never retries a basename, closes its held FD, and returns the monotone state.
Unknown recovery, retained, and final-report durability is sticky; B cannot
exit through those paths.

recv_control and recv_monitored each have one recvmsg intake. Both process
queued POLLIN before HUP/ERR, reject MSG_TRUNC and MSG_CTRUNC, reject
unexpected ancillary even when zero rights were expected, and close every
installed integer FD on every exceptional path. A consumes STDOUT frames in
index order, then STDERR frames, then the exact end packet; B emits that
same order with 65000-byte maximum payloads and independent hashes.

The final-report parser has one ordered 22-key census plus REPORT_END=1.
PRIMARY=NONE is accepted only when all fifteen entered and committed,
FAULT_SET=NONE, STOP_PROBE=NONE, direct reap complete, cgroup empty and
removed, kill count zero, certificate live, positive exact commit interval,
positive margin, both retained bits, retry zero, and DISPOSITION=PASS.
Every failure requires a nonempty canonical fault set, PRIMARY equal to its
first precedence member, a typed direct-reap value, and the mechanically
derived consumed disposition.

## 19. Unresolved gates, effect denial, and author stop

The raw clone3/CPython continuation, issuer signature-preimage/key/serial
reservation/replay semantics, and deleted-cgroup open-FD observation
semantics remain unresolved. Certificate PASS fields merely name external
gate IDs. They do not supply evidence, do not authorize a synthetic test,
and do not authorize launch. Each gate still requires a separately frozen,
no-build artifact, exact authorization, and separated static review.

The future effect boundary in section 14 is exhaustive, but no future effect
is authorized here. This document grants no prebind PASS, formal review,
manifest change, microtest, execution, payload, build, evidence-root, PDF,
release, or publication authority. The V3 author and all E0366 prebind
advisors are permanently disqualified from formal V3 review.

During this authorship the only writes were apply_patch updates to this exact
fresh V3 path. No other file was created or modified. No temporary, cache,
log, backup, lock, swap, redirected capture, or auxiliary file was made. No
embedded literal was imported, tokenized, AST- or language-parsed, compiled,
evaluated, executed, launched, microtested, or passed to a validator
process. Raw reads and byte/line/hash/callsite inspections only were used.
No build/evidence/root was listed, stated, opened, traversed, or accessed.

This unique EOF terminal declares inert author-stop only.

BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V3_AUTHOR_STOP
