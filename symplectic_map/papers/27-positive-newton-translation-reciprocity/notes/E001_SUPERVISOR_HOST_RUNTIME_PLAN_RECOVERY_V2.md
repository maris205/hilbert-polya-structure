# Paper 27 E001 supervisor Host runtime plan recovery V2

Status: E0365-authorized inert V2 author control. Execution, microtest,
prebind, manifest, formal-review, build, evidence-root, and release authority
are all zero.

This file is a strict 7-bit ASCII/LF normative plan. Its literal program
records are inert byte strings. Authorship does not import, tokenize as a
language, AST-parse, compile, evaluate, execute, launch, microtest, or send a
literal to any validator process.

## 1. Authority, immutable history, and exact inputs

The sole V2 authorizing event is E0365 in the exact ledger:

path=/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md
dev=2431
ino=12439253869
mode=0644
nlink=1
uid=0
gid=0
bytes=2288019
LF=23569
SHA256=fe04c56e704d99bab1c3182cad4811f7c585838f7d5dc2ebb1e42f8c3922e349
terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V1_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V2_AUTHOR_OPEN_NO_EXECUTION

The exact Host V15 remains:

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

V8 is normative only for exact transcript row semantics:

path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V8.md
bytes=74973
LF=1071
SHA256=72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf

Frozen failed V1 is immutable history, not execution authority:

path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V1.md
dev=2431
ino=5916180461
mode=0644
nlink=1
uid=0
gid=0
bytes=107536
LF=2060
SHA256=0d8d0b8ba5135b4df8d94615188d220f47bdabb84b06f5d43c628dd3d5b97e4a
terminal=BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V1_AUTHOR_STOP

V1 actor, recovery, and embedded-validator identities are respectively
49843/814/4fed500d3396a551680f941ccbe9fc910e40ff38db33e6d648473fe44c224650,
10774/225/0fb76bf24a8b930b161a826123bfe9d41496577ce52481f7f1c96176524ff07c,
and 10184/120/7488271ad85f0428b2b7e7ac27e966abcf246e099f3dd36b834deb780692eecd.
V1 is never copied as authority and is never modified.

The five exact V15 source spans are:

source   bytes  LF    SHA256
OUTER    87151  1840  cfa1d88b312b7f4425778018be39cf7628568c9ddb39c697ff12b8b0f1c8be1a
KEEPER    4216   128  e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716
LAUNCHER  4218   128  e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5
MARKER   75094  1479  b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d
CHILD    19746   452  1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf

MARKER's embedded CHILD bytes must be raw-equal to standalone CHILD. The
ledger, Host V15, Host V8, V1, manifest, Binder, actor V3, derivation V6,
validator, every paper, and every build/evidence root are immutable.

## 2. Exact closure of E0365 correction rules 1 through 12

Rule 1: V1 remains byte-for-byte unchanged. This fresh file contains newly
delimited V2 A, B, and embedded C records and a new identity census.

Rule 2: section 4 separates a capability-bearing actor-entry vector from the
post-chroot payload-final CAPS_EMPTY/NNP1 vector. Literal A freshly verifies
entry, applies the transition only in children, and freshly verifies final
state before either execve.

Rule 3: A first duplicates every B source descriptor to a disjoint high-FD
bank, maps only preserved copies, and closes the bank. Before READY, B checks
fd3..9 and fd100 for exact type, access direction, seals or whole identity,
peer or pidfd binding, and checks the complete close_range scrub.

Rule 4: one B starts before CONSUME_BEGIN and remains the authenticated
recovery owner until the one durable terminal report. It is not per-probe.
B exclusively owns consumption mkdir/intent, every attempt durable record,
capture, actor-loss handling, the kill call, and final report. A exclusively
owns source extraction/staging, clone3, SIGCONT, direct wait, and C parsing.
B has no source extraction, staging, payload release, fork, exec, SIGCONT,
semantic transcript parser, retry, resume, or repair path.

Rule 5: the certificate has one fixed 360000000000-ns absolute realtime
lifetime. Preflight and staging have independent monotonic caps. Literal A
and B recheck the same absolute expiry before consumption, before every
release, after every durable ACK, and before terminal report. Expiry is
sticky and closes every later slot.

Rule 6: B owns one direct os.write(cgroup.kill,b"1 LF") callsite. It never
uses write-all, EINTR retry, short-write retry, a second ticket, PID, PGID, or
any fallback. The certificate binds B survival and kill-return-to-empty
progress. Unknown effect is permanent CONSUMED_INDETERMINATE. If populated
remains 1 after the cleanup cap, B commits an indeterminate report and stays
alive in passive empty observation until populated 0; it never regains PASS.

Rule 7: immediately before SIGCONT, A checks certificate life and reserves
the exact 5000000-ns SIGCONT call/return premise inside the fixed launch
horizon. No release syscall begins if call_entry+5000000 exceeds the
horizon. Return is checked without extending the horizon.

Rule 8: attempts-base identity is certificate-bound and freshly held. B is
READY before CONSUME_BEGIN. Issuer one-shot consumption is already durable
and B observes the transition before A's first mkdirat. On actor loss B
creates or opens the exact AUTH_ID attempt directory and records every
pre-intent state; no observed consume transition can become reusable or be
called unconsumed.

Rule 9: certificate, envelope, signal mask, capability phases, cgroup2
filesystem/type/controllers, exact mount lines, runtime-root read-only mount,
separate writable safe bind, dependency identities, and all fresh checks are
aligned one-for-one with source.

Rule 10: no probe file contains PASS. VALIDATED_CANDIDATE and
ACK_COMMIT_INTENT are separate B-owned exclusive monotone records; only
after their full durable chain may B set an in-memory COMMITTED bit. Only B may create the
terminal PASS report, after every timing check and all durable ACK states.
The complete fault tuple and precedence are fixed in section 12 and both
literals.

Rule 11: C recomputes P00 synthetic SHA from authenticated CHILD bytes;
permits sequential P05 numeric PID reuse; makes no SID/PGID claim beyond
canonical fields and marker-attested rows; A and B enforce ordered packets,
current probe, and fdinfo PID binding; LIBC uid/gid are exactly zero.

Rule 12: raw clone3 continuation through CPython remains explicitly
unresolved. The certificate must bind a separately frozen synthetic gate.
No such gate is created here. Until a later no-build synthetic test is
separately authored, authorized, run, frozen, and reviewed, V2 is not
executable even if every static review passes.

## 3. Suite, budgets, absolute lifetime, and stop law

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
STAGING_CAP_NS=10000000000
FINAL_REPORT_CAP_NS=1000000000
CERTIFICATE_ABSOLUTE_LIFETIME_NS=360000000000
ENTRY_MIN_REMAINING_NS=293472000000
CONSUMPTION_MIN_REMAINING_NS=283472000000
STDOUT_CAP_BYTES=3145728
STDERR_CAP_BYTES=3145728

Fifteen times 18164800000 is 272472000000. At actor entry, fixed remaining
life covers preconsumption, staging, all slots, and final report. Immediately
before release ordinal q, required remaining life is
(15-q)*18164800000+1000000000. After its durable ACK it is
(14-q)*18164800000+1000000000. Before final report it is 1000000000.

Exactly one ordered loop exists. A slot is entered at most once. First sticky
FAIL or INDETERMINATE closes every later slot. No retry, resume, continue,
repair, skip, replacement slot, second suite, certificate refresh, clock
restart, or cleanup-to-PASS transition exists.

For a released probe:

release_origin < release_return <= release_origin+1000000000
host_complete <= release_origin+17664800000
ack_commit <= release_origin+18164800000
ack_commit-host_complete <= 500000000

The cleanup cap is separate and cannot restore PASS.

## 4. Exact two-phase credentials, signals, and descriptors

Actor entry is exactly:

uid=euid=suid=0
gid=egid=sgid=0
supplementary_groups=empty
umask=0077
CapInh=0000000000000000
CapPrm=00000000000401c0
CapEff=00000000000401c0
CapBnd=00000000000401c0
CapAmb=0000000000000000
NoNewPrivs=0
SecureBits=12

Bits 6, 7, 8, and 18 are exactly CAP_SETGID, CAP_SETUID, CAP_SETPCAP, and
CAP_SYS_CHROOT. Every other capability is denied. A reads canonical
/proc/self/status capability fields and PR_GET_SECUREBITS before any effect.

Each B or OUTER child chroots to the pinned runtime root, reopens and fchdirs
to a certificate-bound safe dev/ino, fixes ids/groups/umask/rlimits/signals, sets locked
NOROOT and NO_SETUID_FIXUP securebits, drops every bounding bit, clears all
effective/permitted/inheritable/ambient capabilities, sets no_new_privs=1,
and freshly requires:

uid/euid/suid/gid/egid/sgid=0
groups=empty
umask=0077
CapInh=CapPrm=CapEff=CapBnd=CapAmb=0000000000000000
NoNewPrivs=1
SecureBits=15

Before consumption B uses the safe-bind base itself; after staging OUTER uses
the exclusive stage/AUTH_ID child. Both identities are passed and freshly
checked, and B never changes cwd to the later child. Only after the final
credential equality may execve occur. All catchable signals are default,
the mask and pending set are empty, and all three interval timers are zero at
actor entry and final child state. No prose-blocked critical mask exists.
The certificate instead binds NO_SIGNAL_DELIVERY and NO_ASYNC_TRANSFER for
the entire protected lifetime. Trace/profile/audit hooks are absent by the
independent premise; a run cannot infer this from its own observations.

A is launched with exact Python flags -I -S -B -P -X utf8, exact ten-key
environment, authenticated empty fd0, distinct raw fd1/fd2 pipes, and:

fd100 sealed V2 A source
fd101 exact E0365 ledger
fd102 exact Host V15
fd103 exact complete V2 plan
fd104 sealed premise certificate
fd105 sealed issuer envelope
fd106 sealed V2 B source

No other descriptor exists after close_range(3,99) and
close_range(107,UINT_MAX). A's sys.argv is exactly
/proc/self/fd/100,RUN,AUTH_ID.

## 5. Independent certificate and issuer envelope

AUTH_ID is exactly 64 lowercase hex and equals
SHA256("P27E001V2 NUL" || certificate || NUL || issuer-envelope). NONCE is
exactly AUTH_ID. Neither source can create, sign, refresh, or approve either
input.

The supervisor independently authenticates the issuer envelope before actor
launch. Literal A still strictly parses, hashes, lifetime-checks, and binds
it. Signature validity is an external trust boundary, not self-certification.
The exact envelope grammar is:

P27E001_ISSUER_ENVELOPE_V2
ISSUER_ID=P27_HOST_PREMISE_ISSUER_V2
ISSUER_KEY_ID=H64
AUTHORIZATION_SERIAL=H64
CERTIFICATE_SHA256=H64
PLAN_SHA256=H64
RUNNER_SHA256=H64
RECOVERY_SHA256=H64
E0365_SHA256=fe04c56e704d99bab1c3182cad4811f7c585838f7d5dc2ebb1e42f8c3922e349
V15_SHA256=a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845
NOT_BEFORE_REALTIME_NS=UDEC
NOT_AFTER_REALTIME_NS=UDEC
ONE_SHOT_CONSUMED_BY_ISSUER=1
SIGNATURE_ALGORITHM=EXTERNALLY_VERIFIED_ED25519
SIGNATURE_HEX=LOWER_HEX_128
ENVELOPE_END=1

The strict certificate begins and ends as follows; every field is present
once in this exact order, followed by contiguous DEP rows:

P27E001_PREMISE_CERTIFICATE_V2
ISSUER_ID=P27_HOST_PREMISE_ISSUER_V2
ISSUER_ENVELOPE_SHA256=H64
BOOT_ID_SHA256=H64
PLATFORM_ID_SHA256=H64
ARCH=x86_64
KERNEL_RELEASE_HEX=LOWER_EVEN_HEX
NOT_BEFORE_REALTIME_NS=UDEC
ABSOLUTE_EXPIRY_REALTIME_NS=UDEC
ABSOLUTE_LIFETIME_NS=360000000000
REALTIME_BIND_NS=UDEC
MONOTONIC_BIND_NS=UDEC
REALTIME_MONOTONIC_MAX_DRIFT_NS=1000000
PLAN_SHA256=H64
RUNNER_SHA256=H64
RECOVERY_SHA256=H64
E0365_SHA256=fe04c56e704d99bab1c3182cad4811f7c585838f7d5dc2ebb1e42f8c3922e349
V15_SHA256=a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845
V8_SHA256=72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf
ACTOR_ENTRY_CAPS=00000000000401c0
ACTOR_ENTRY_NNP=0
ACTOR_ENTRY_SECUREBITS=12
PAYLOAD_FINAL_CAPS=0000000000000000
PAYLOAD_FINAL_NNP=1
PAYLOAD_FINAL_SECUREBITS=15
ATTEMPT_BASE_DEV=UDEC
ATTEMPT_BASE_INO=UDEC
ATTEMPT_BASE_MODE=40700
ATTEMPT_BASE_NLINK=UDEC
ATTEMPT_BASE_UID=0
ATTEMPT_BASE_GID=0
ATTEMPT_BASE_MOUNT_ID=UDEC
ATTEMPT_BASE_MOUNTINFO_SHA256=H64
CGROUP2_FS_MAGIC=63677270
CGROUP2_MOUNT_ID=UDEC
CGROUP2_MOUNTINFO_SHA256=H64
CGROUP_BASE_DEV=UDEC
CGROUP_BASE_INO=UDEC
CGROUP_BASE_MODE=OCTAL
CGROUP_BASE_NLINK=UDEC
CGROUP_BASE_UID=0
CGROUP_BASE_GID=0
CGROUP_TYPE_HEX=646f6d61696e0a
CGROUP_CONTROLLERS_HEX=LOWER_EVEN_HEX
CGROUP_SUBTREE_CONTROL_HEX=LOWER_EVEN_HEX
CGROUP_NO_EXTERNAL_MUTATOR=1
RUNTIME_ROOT_DEV=UDEC
RUNTIME_ROOT_INO=UDEC
RUNTIME_ROOT_MODE=OCTAL
RUNTIME_ROOT_NLINK=UDEC
RUNTIME_ROOT_UID=0
RUNTIME_ROOT_GID=0
RUNTIME_ROOT_MOUNT_ID=UDEC
RUNTIME_ROOT_MOUNTINFO_SHA256=H64
RUNTIME_ROOT_FSTYPE_HEX=LOWER_EVEN_HEX
SAFE_BIND_DEV=UDEC
SAFE_BIND_INO=UDEC
SAFE_BIND_MODE=OCTAL
SAFE_BIND_NLINK=UDEC
SAFE_BIND_UID=0
SAFE_BIND_GID=0
SAFE_BIND_MOUNT_ID=UDEC
SAFE_BIND_MOUNTINFO_SHA256=H64
SAFE_BIND_FSTYPE_HEX=LOWER_EVEN_HEX
SAFE_BIND_NOEXEC=1
SAFE_BIND_WRITABLE_DESCENDANT_COUNT=1
PYTHON_IMAGE_SHA256=9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101
PYTHON_IMAGE_BYTES=30626264
PYTHON_IMAGE_DEV=UDEC
PYTHON_IMAGE_INO=UDEC
LIBC_PATH_HEX=LOWER_EVEN_HEX
LIBC_DEV=UDEC
LIBC_INO=UDEC
LIBC_MODE=OCTAL
LIBC_NLINK=UDEC
LIBC_UID=0
LIBC_GID=0
LIBC_BYTES=UDEC
LIBC_SHA256=H64
LIBC_CONFSTR_HEX=LOWER_EVEN_HEX
VALID_SIGNAL_COUNT=UDEC
DEFAULT_SIGNAL_COUNT=UDEC
DEFAULTS_SHA256=H64
PRECONSUMPTION_CAP_NS=10000000000
CONSUMPTION_PROGRESS_NS=100000000
STAGING_CAP_NS=10000000000
RELEASE_PROGRESS_NS=1000000000
SIGCONT_CALL_RETURN_NS=5000000
DURABLE_RECORD_PROGRESS_NS=100000000
WATCHDOG_ARM_PROGRESS_NS=1000000000
WATCHDOG_ACK_PROGRESS_NS=500000000
WATCHDOG_SURVIVES_CONSUME_TO_REPORT=1
WATCHDOG_SURVIVES_KILL_TO_EMPTY=1
CGROUP_KILL_WRITE_RETURN_NS=5000000
CGROUP_KILL_TO_EMPTY_NS=2000000000
FINAL_REPORT_PROGRESS_NS=1000000000
NO_ASYNC_TRANSFER=1
NO_SIGNAL_DELIVERY=1
NO_TIMER_DELIVERY=1
NO_TRACE_PROFILE_AUDIT_HOOK=1
NO_CONCURRENT_MUTATOR=1
DEPENDENCY_CLOSURE_COMPLETE=1
RUNTIME_ROOT_WORKSPACE_ABSENT=1
BUILD_EVIDENCE_ROOT_UNREACHABLE=1
CLOSE_RANGE_COMPLETE=1
FSYNC_DURABILITY_PREMISE=1
CLONE3_CPYTHON_GATE_ID=H64
CLONE3_CPYTHON_GATE_PASS=1
DEP_COUNT=UDEC
DEP[0000]=ROLE,PATH_HEX,DEV,INO,MODE,NLINK,UID,GID,BYTES,SHA256
...
DEP[NNNN]=ROLE,PATH_HEX,DEV,INO,MODE,NLINK,UID,GID,BYTES,SHA256
CERTIFICATE_END=1

Roles and complete dependency closure are as in V1 but are newly bound to
V2. Exactly one PYTHON_LINK, PYTHON_IMAGE, ENV_EXEC, BASH_EXEC,
DYNAMIC_LOADER, and LIBC row is required. Every dependency row is freshly
opened through held no-follow components and fully rehashed. The unique LIBC
row must equal every certificate field including uid=gid=0.

BOOT_ID_SHA256 hashes exact boot-id bytes including LF. PLATFORM_ID_SHA256
hashes exact `SYSNAME`, `RELEASE`, `VERSION`, and `MACHINE` LF records. Each
mount-info hash covers the unique complete /proc/self/mountinfo line plus LF.
Fresh parsing requires cgroup fstype cgroup2 and rw; runtime root ro,nosuid,
nodev; safe bind rw,nosuid,nodev,noexec; and distinct runtime-root/safe-bind mount
IDs. This makes the read-only snapshot and writable P11/P13 bind compatible.
The unique cgroup base is root-owned at its exact mode, its type,
controllers, and subtree-control bytes are frozen, and its explicit
no-external-mutator premise is fresh. The safe bind is mode0700 and the
mount graph exposes exactly one writable descendant below the read-only
runtime root: that safe bind.
Both programs freshly bracket realtime and monotonic samples and require the
certificate pair to remain within 1000000 ns after elapsed-time adjustment.
The same absolute expiry is checked at B READY, before and after consumption,
before and after staging, before every release, immediately before SIGCONT
entry and after return, after each receipt, before the next probe, before
cgroup removal, and before and after the final report durability sequence.
Every check reserves all remaining work, not merely its local call.

## 6. One-shot namespace and exact staging

Preexisting held bases are:

attempts=/var/lib/p27-e001-host-v15/attempts
stage=/tmp/p27-e001-host-v15
cgroup=/sys/fs/cgroup/p27-e001-host-v15
runtime-root=/var/lib/p27-e001-host-v15/runtime-root

B is READY before A sends CONSUME_BEGIN and before either process performs
mkdir, O_CREAT, staging, cgroup, or payload effect. B validates current
certificate life and replies CONSUME_ARMED. On CONSUME_COMMIT, B exclusively
mkdirats attempts/AUTH_ID mode0700, holds it no-follow, fsyncs the attempts
base, creates intent.v2 O_EXCL mode0400, file-fsyncs, same-FD rereads, and
attempt-dir-fsyncs it. Only then B sends CONSUMED_DURABLE. The transition is
also backed by the issuer's already durable one-shot serial. A performs no
later effect before that message. Thereafter actor loss is consumed even at
every boundary before or during the first mkdirat.

If B observes CONSUME_COMMIT but mkdir return is unavailable, it classifies
the attempt namespace as unknown, never sends CONSUMED_DURABLE, and performs
recovery observation. Existing AUTH_ID always means consumed; it is never
reused. Absence before CONSUME_COMMIT is REFUSED_NOT_CONSUMED; any unknown
effect at or after that call is never called unconsumed.

The B-authored intent binds AUTH_ID, envelope/certificate/plan/A/B/E0365/V15 hashes,
suite, cgroup/stage paths, credential phases, absolute expiry,
CONSUMED=1,RETRY_ALLOWED=0. File and both directories are fsynced before
staging or containment creation.

Within the fixed staging cap A exclusively creates stage/AUTH_ID mode0700,
requires target,a,b absent, and writes exactly keeper.py, launcher.py,
marker.py,child.py through its held dirfd with O_EXCL|O_NOFOLLOW, mode0400,
same-FD reread, exact triple verification, file fsync and directory fsync.
OUTER has no pathname and is sealed into an anonymous memfd with exactly
F_SEAL_WRITE|F_SEAL_GROW|F_SEAL_SHRINK|F_SEAL_SEAL.

P01C remains unreachable until same-suite P01D has complete C acceptance and
a B in-memory COMMITTED bit backed by both durable records. Its thirteen
fields, in V15 order, derive only from that row
map plus fresh held-component libc and Python observations. LIBC uid/gid must
both be zero. No certificate-only substitute, prose value, old attempt, or
pathname-only stat is accepted.

## 7. Continuous B bootstrap and collision-safe FD mapping

One B is forked before CONSUME_BEGIN. For each source descriptor A first uses
F_DUPFD_CLOEXEC with minimum 200, requires all preserved FDs distinct and
outside every target, and only then dup2s preserved copies. It closes every
preserved copy and calls close_range over all non-target ranges. Sequential
source destruction is impossible.

B receives exactly:

fd0 authenticated empty pipe, read-only
fd1 closed
fd2 closed
fd3 A/B SOCK_SEQPACKET, read/write, peer actor PID uid/gid0
fd4 actor pidfd, poll-only, fdinfo Pid equals actor PID
fd5 held attempts base, read-only directory, exact certificate identity
fd6 held cgroup base, read-only directory, exact certificate identity
fd7 sealed certificate, read/write memfd, SHA bound to AUTH_ID
fd8 sealed issuer envelope, read/write memfd, SHA bound to AUTH_ID
fd9 exact E0365 ledger, read-only regular file, whole identity
fd100 sealed B source, read/write memfd, certificate SHA

Before READY B validates every target's type, F_GETFL access direction,
seals where applicable, fstat identity, fdinfo pid binding, socket type and
peer credentials, empty fd0, closed fd1/fd2, and successful complete
close_range scrub. No other inherited descriptor exists.

B recomputes AUTH_ID from fd7/fd8, authenticates fd9 as the exact E0365
whole file and terminal, and requires fd100 SHA equal RECOVERY_SHA256. Its
fixed argv also carries PLAN_SHA256 solely as an equality check against fd7;
B has no plan parser and no source-extraction authority.

B uses fixed Python flags and the exact V15 ten-key environment. Its final
credential vector is freshly checked before READY. B never receives the
stage base.

## 8. Dynamic protocol, atomic containment, and one kill

All SOCK_SEQPACKET messages are strict ASCII/LF, one complete record, exact
ordered fields, no unknown key, and current ordinal/probe. Ancillary data is
accepted only with flags=0, one SCM_RIGHTS item, and the exact expected FD
count.

CONSUMED_DURABLE already proves B holds the attempt directory; A never
receives that FD. After exclusive cgroup creation A sends CONTAINMENT with
the held cgroup-directory FD. B verifies exact child identity,
cgroup.type=domain LF, controllers, and events populated 0, and returns
CONTAINMENT_ACK.

Before clone3, A sends STREAM_ARM with four SCM_RIGHTS descriptors in order:
stdout-read, stderr-read, cgroup.events-read, and cgroup.kill-write. The
packet binds each fstat tuple, access direction, ordinal, probe, release
origin, and launch deadline. B validates pipe distinction and nonblocking
read direction plus cgroup file identities/directions before STREAMS_ARMED.
Thus actor death during clone or before pidfd handoff is already covered by
events and the sole kill authority.

Raw clone3 with CLONE_INTO_CGROUP|CLONE_PIDFD atomically creates each direct
OUTER child inside that cgroup. The child performs SIGSTOP as its sole
pre-exec action. A first directly accepts the exact stopped wait status and
exact cgroup.procs member, then sends PIDFD_ARM with exactly one SCM_RIGHTS
OUTER pidfd, the bound OUTER PID, stopped status, and member fact. B requires
current ordinal/probe, live fdinfo Pid equality, independently observed
stopped state, and exact cgroup.procs membership before PIDFD_ARMED. Unknown
clone return or handoff effect is
permanent CONSUMED_INDETERMINATE; no clone is repeated.

A proves exact stopped status, cgroup.procs exactly PID LF, populated 1, and
durable release record. Immediately before SIGCONT it performs the section 3
absolute-life check, samples call_entry, and requires
call_entry+5000000<=launch_deadline. Only then may its sole SIGCONT callsite
begin. Return must be within both bounds. A is the only direct OUTER waiter;
B never calls waitpid or waitid.

B concurrently drains both raw nonblocking streams through EOF, caps each at
3145728 while continuing discard on overflow, polls actor/OUTER pidfds and
cgroup.events, and enforces the absolute deadline. It sends one exact RESULT
packet with this fixed ordered ten-key vector:
ordinal,probe,outer_pid,pidfd_ready,stdout_len,stderr_len,stdout_eof,
stderr_eof,fault_set,done_ns. Captured bytes follow as separately framed raw
streams. Overflow, cgroup, kill, and packet faults are sticky members of
fault_set rather than optional header keys. A accepts no packet for another
probe, requires pidfd_ready=1 and result OUTER PID equal its direct child,
rehashes both raw streams, and freshly confirms cgroup empty.

On the first sticky failure while populated, B durably creates one
kill-ticket.v2, then executes exactly one direct
os.write(kill_fd,b"1\n"). It never retries on EINTR, short return, exception,
actor loss, ticket presence, or timeout. A return other than exactly 2, or
any lost return, is KILL_EFFECT_UNKNOWN. B continues drain and populated
observation. At cleanup cap with populated 1 it commits retained terminal
INDETERMINATE and remains in RETAINED_POPULATED_MONITOR until populated 0.

## 9. Exact launch, argv, environment, and P01C

OUTER gets only fd0 authenticated empty, distinct raw fd1/fd2 pipes, and
sealed OUTER fd100. Complete close_range covers every other number. It uses:

/root/miniconda3/bin/python3 -I -S -B -P -X utf8 /proc/self/fd/100

Its sys.argv is exactly V15 canonical 20 entries, or 33 only for P01C. The
budget/tokens, safe dev/ino, five source triples, and thirteen P01C fields are
unchanged from E0364/V15. Environment is exactly:

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

The full chroot preserves absolute Python, Python image, /usr/bin/env,
/usr/bin/bash, dynamic loader/libc/dependencies, proc self paths, and the
separate writable /tmp/p27-e001-host-v15 bind. The workspace and every
build/evidence root are absent and no process has a preopened workspace FD.

## 10. Complete C transcript semantics

C consumes complete stdout from offset zero. It requires 1..3145728 bytes,
only 0x20..0x7e or LF, final LF, no empty line, exact marker header, exact
probe-specific ordered row vector, exact footer, exactly one candidate, and
the unique terminal as final line. Unknown, duplicate, missing, reordered,
noncanonical, CR, HT, NUL, high-byte, partial, or trailing input fails.

The exact prefix vectors and ten common suffix fields remain those frozen in
V15 and V1. C implements all fifteen peer branches. Candidate and terminal
must be byte-grammar exact, equal in all role statuses, all_reaped1,
fatal0,resultPASS, and terminal frame_complete1. Launcher/keeper are SIGTERM,
marker is zero, and child status is probe-specific.

P00 reconstructs authenticated synthetic bytes exactly as
CHILD || LF || "#" || enough "x" bytes to total 251414, computes SHA256, and
requires the payload metadata and any INFO child source_sha equal that value.
P05 accepts equal numeric values for its two sequential PID fields; it binds
each ordered observation/status without claiming simultaneous identity.
SID is only canonical positive because the transcript exposes no reference
SID. PGID is only canonical positive except where a marker-attested row
explicitly states topology. Every accepted receipt records
V15_INTERNAL_VALIDATION_REPORTED_BY_COMPLETE_TRANSCRIPT and
EXTERNAL_TOPOLOGY_RECONSTRUCTION=UNAVAILABLE. No host topology is inferred
from positivity and no child SID or launcher group is externally rebuilt.
P10 continues to permit and count numeric reuse exactly.

P01D/P01C, image/libc/cwd, all P00-P13 values, child observations, dynamic
PIDs/statuses, timing and source identities are fully checked. C returns only
an in-memory row map or a closed fault; it has no authority.

## 11. Monotone receipt and terminal report grammars

No probe record contains the token PASS. A never writes the attempt
directory. After complete direct wait and C acceptance A sends B one strict
VALIDATED_CANDIDATE packet containing capture/direct-wait/parser/timing
facts. B exclusively creates and durably verifies:

receipt-Q-validated.v2: STATE=VALIDATED_CANDIDATE
receipt-Q-ack-intent.v2: STATE=ACK_COMMIT_INTENT

Before the second creation B reserves DURABLE_RECORD_PROGRESS_NS inside both
ACK horizons. After file fsync, same-FD reread, attempt-dir fsync, and current
certificate-life check, B changes only its in-memory slot to COMMITTED and
sends COMMITTED. It will not admit the next ordinal before A sends
COMMITTED_SEEN. A late, lost, or malformed exchange leaves only non-PASS
durable states and permanently stops.

Each record begins with P27E001_PROBE_STATE_V2 and contains AUTH_ID, ORDINAL,
PROBE, STATE, release/capture/ACK times, stdout/stderr hashes and lengths,
OUTER PID/raw status, direct-wait, EOF, cgroup, parser, candidate, terminal,
certificate-expiry, and RECORD_END=1 in a fixed order frozen in A/B.

B alone creates report.v2. The fixed grammar is:

Every failure first gets one B-owned recovery.v2; if the intent did not
become durably known, the basename is preintent.v2 instead. Its exact grammar
is:

P27E001_RECOVERY_STATE_V2
AUTH_ID=H64
STOP_PROBE=Q_OR_NONE
PRIMARY=FAULT
FAULT_SET=ORDERED_CSV
INTENT_DURABLE=B
DIRECT_REAP=COMPLETE_OR_UNAVAILABLE
STDOUT_EOF=B
STDERR_EOF=B
KILL_CALL_COUNT=0_OR_1
KILL_WRITE_RETURNED=B
CGROUP_EMPTY=B
RETRY_ALLOWED=0
DISPOSITION=CONSUMED_FAIL_OR_CONSUMED_INDETERMINATE
RECOVERY_END=1

On A loss B is not OUTER's parent and writes DIRECT_REAP=UNAVAILABLE; it
never claims waitid(P_PIDFD) reaping. Physical completion is established
only by cgroup.events populated 0, while lack of A's direct wait remains an
indeterminate disposition. No recovery receipt contains PASS.

P27E001_FINAL_REPORT_V2
AUTH_ID=H64
SUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
ENTERED_COUNT=UDEC
COMMITTED_COUNT=UDEC
STOP_PROBE=Q_OR_NONE
PRIMARY=FAULT
FAULT_SET=ORDERED_CSV_OR_NONE
DIRECT_REAP_COMPLETE=B
CGROUP_EMPTY=B
CGROUP_REMOVED=B
KILL_CALL_COUNT=0_OR_1
KILL_WRITE_RETURNED=B
CERTIFICATE_LIVE_AT_REPORT=B
STAGE_RETAINED=1
ATTEMPT_RETAINED=1
RETRY_ALLOWED=0
DISPOSITION=PASS_OR_CONSUMED_FAIL_OR_CONSUMED_INDETERMINATE
REPORT_END=1

PASS requires all fifteen in-memory COMMITTED slots backed by both exact
durable receipt objects, live certificate, no fault,
direct reap complete, cgroup empty and removed, kill count zero, and every
prior conjunction. B reserves report durability within expiry, writes and
fsyncs report, fsyncs attempt dir, rereads exact bytes, performs the
post-report expiry sample, then sends
TERMINAL_DURABLE. It remains alive until A sends TERMINAL_SEEN and A directly
reaps it. An actor-loss report is never PASS.

## 12. Complete fault set, precedence, and disposition

The exact primary precedence, highest first, is:

INPUT_AUTH
ENTRY_CONTEXT
CERTIFICATE_INVALID
PRECONSUMPTION_DEADLINE
ATTEMPT_NAMESPACE_UNKNOWN
INTENT_DURABILITY_UNKNOWN
ACTOR_LOST
CERTIFICATE_EXPIRED
STAGING_FAULT
STAGING_DEADLINE
CONTAINMENT_FAULT
CONTROL_PACKET
PIDFD_BINDING
LAUNCH_DEADLINE
RELEASE_EFFECT_UNKNOWN
WATCHDOG_DEADLINE
KILL_EFFECT_UNKNOWN
CAPTURE_OVERFLOW
STDERR_NONEMPTY
OUTER_STATUS
TRANSCRIPT_LANGUAGE
TRANSCRIPT_SEMANTICS
ACK_DURABILITY
CONTAINMENT_NOT_EMPTY
REPORT_DURABILITY

The sticky set is the ordered subset of this complete tuple. Unknown attempt,
release, kill, direct-reap, containment, ACK, or report effect makes
CONSUMED_INDETERMINATE, which dominates CONSUMED_FAIL. Known closed semantic
or status failure is CONSUMED_FAIL. REFUSED_NOT_CONSUMED is possible only
before CONSUME_COMMIT. PASS is the complete conjunction and never follows a
fault.

Crash ownership is exhaustive:

1. Before CONSUME_COMMIT, input, context, certificate, B boot, READY, or
   CONSUME_ARMED loss is REFUSED_NOT_CONSUMED and permits no write.
2. At the single consumption mkdir/intent sequence, B is the effecting
   process. A loss cannot interrupt B. An unavailable mkdir/intent result is
   ATTEMPT_NAMESPACE_UNKNOWN or INTENT_DURABILITY_UNKNOWN. If the safe
   attempt dirfd exists, B writes preintent.v2 and report.v2; otherwise the
   issuer's durable consumed serial is the external terminal fact and no
   retry is possible.
3. B or kernel loss after CONSUME_COMMIT violates the independently
   certified survival premise and is permanently CONSUMED_INDETERMINATE,
   even if no local report survived. It is never reclassified reusable.
4. A loss after CONSUMED_DURABLE is ACTOR_LOST at the exact current state:
   before/during staging, before/during containment, before STREAM_ARM,
   after STREAM_ARM but before clone, after clone but before pidfd handoff,
   before release record, immediately before/during/after SIGCONT, during
   direct wait/drain, parser, either receipt, cgroup removal, or finalization.
   B owns the same one-kill/empty/report transition at every such point.
5. A live-process exception uses the literal CRASH_FAULT map for INPUT,
   ENTRY, CERT, B_BOOT, CONSUME, STAGE, CONTAIN, STREAM_ARM, CLONE,
   PIDFD_ARM, STOP, RELEASE_RECORD, SIGCONT, WAIT, RESULT, PARSER, RECEIPT,
   REMOVE, and FINAL. CertificateExpired overrides phase mapping and remains
   sticky. There is no generic unclassified post-consumption branch.

## 13. Complete state machines and authority census

Actor FSM:

A00_ENTRY -> A01_INPUT_AUTH -> A02_ENTRY_CONTEXT -> A03_CERT_LIVE
A03 -> A04_WATCHDOG_BOOT -> A05_WATCHDOG_READY
A05 -> R00_REFUSED before CONSUME_COMMIT on any fault
A05 -> A06_CONSUME_BEGIN -> A07_CONSUME_ARMED -> A08_CONSUME_COMMIT
A08 -> A09_B_CONSUMED_DURABLE -> A10_STAGE -> A11_CONTAINMENT
A11 -> A12_B_CONTAINMENT_ACK
A12 -> A13_PREPARE_Q -> A14_STREAMS_ARMED_Q -> A15_ATOMIC_CLONE_Q
A15 -> A16_STOP_MEMBER_Q -> A17_PIDFD_ARMED_Q
A17 -> A18_RELEASE_RECORD_Q -> A19_RELEASE_AUTHORITY_Q
A19 -> A20_SIGCONT_Q -> A21_DIRECT_WAIT_AND_DRAIN_Q
A21 -> A22_VALIDATE_Q -> A23_VALIDATED_CANDIDATE_Q
A23 -> A24_B_ACK_COMMIT_INTENT_DURABLE_Q -> A25_B_MEMORY_COMMITTED_Q
A25 -> A26_CERT_LIVE_AFTER_ACK_Q
A26 -> A13_PREPARE_NEXT or A27_REMOVE_EMPTY_CGROUP
A27 -> A28_FINALIZE -> A29_TERMINAL_DURABLE -> A30_TERMINAL_SEEN
A30 -> A31_DIRECT_WAIT_B -> T00_TERMINAL

Every post-CONSUME_COMMIT fault goes to B-owned terminal failure. No terminal returns
to prepare, release, exec, or PASS.

Watchdog FSM:

B00_ENTRY -> B01_FD_VERIFY -> B02_FINAL_CREDENTIAL_VERIFY -> B03_READY
B03 -> B04_CONSUME_ARMED or B90_REFUSED_OWNER
B04 -> B05_CONSUME_COMMIT -> B06_ATTEMPT_INTENT_DURABLE
B06 -> B07_CONTAINMENT_BOUND
B07 -> B08_STREAMS_ARMED_Q -> B09_WAIT_PIDFD_WITH_ACTOR_MONITOR_Q
B09 -> B10_PIDFD_ARMED_Q -> B11_RELEASE_DURABLE_Q
B11 -> B12_DRAIN_RESULT_Q -> B13_VALIDATED_RECEIPT_Q
B13 -> B14_ACK_INTENT_DURABLE_Q -> B07_IDLE_NEXT
B07 after ordinal14 -> B15_FINALIZE
any post-CONSUME fault/actor loss -> B80_FAILURE_SELECT
B80 -> B81_TICKET_OPTION -> B82_ONE_KILL_CALL_OPTION
B82 -> B83_DRAIN_EMPTY_UNTIL_CAP
B83 empty -> B84_TERMINAL_REPORT
B83 populated-at-cap -> B84_TERMINAL_REPORT -> B85_RETAINED_POPULATED_MONITOR
B85 -> B86_EMPTY_OBSERVED with no second kill and no PASS
B15 -> B84_TERMINAL_REPORT
B84 -> B87_TERMINAL_DURABLE -> B88_WAIT_TERMINAL_SEEN -> B89_STOP

B has no fork, clone, exec, SIGCONT, source extraction, staging, semantic
parser, retry, resume, repair, or suite-selection transition. It alone can
create consumption/intent, release, candidate/ACK-intent, recovery, ticket,
terminal report, and optional post-report empty-observation records.

## 14. Future effects, access denial, and later gates

Authoring, supervisor prebind, and both future formal reviews are zero-write.
A later explicitly authorized run may write only:

1 attempts/AUTH_ID and intent/preintent/release/validated/ack-intent/recovery,
  kill-ticket, report, and optional post-report-empty leaves;
2 stage/AUTH_ID with exactly keeper.py,launcher.py,marker.py,child.py and V15
  target/a/b effects;
3 cgroup/AUTH_ID membership metadata and at most one exact cgroup.kill write;
4 anonymous sealed A/B/certificate/envelope/OUTER memfds, pipes, pidfds and
  SOCK_SEQPACKET traffic.

No other regular file, temporary, cache, log, backup, lock, swap, symlink,
pathname socket, FIFO, redirected capture, tee, manifest, workspace, build,
evidence, paper, PDF, or release write exists. A reads only fixed fd100..106,
held service/mount components, certificate dependencies, exact proc boot,
self status/fdinfo/mountinfo, cgroup fixed files, and four safe leaves. B
reads only fixed fd0,3..9,100, exact attempt/cgroup children, dynamic probe
FDs, and its own proc status/fdinfo. Neither literal names or can reach a
workspace build/evidence root.

The raw clone3/CPython gate remains absent now. A later synthetic gate may be
opened only after separate supervisor authorization and review. It must be a
no-build, no-V15, no-stage synthetic test limited to atomic cgroup birth,
immediate SIGSTOP, CPython post-clone state, collision-safe FD mapping,
capability transition, one-kill empty observation, and report truncation.
Even a frozen synthetic PASS cannot authorize the real suite; V2 still needs
fresh separated formal H41 lifecycle/containment and H42 source/parser review
and a later explicit execution event.

The V2 author and all E0365 prebind advisors are permanently disqualified
from H41/H42. This file grants no prebind, manifest, formal review, microtest,
execution, build, evidence-root, payload, PDF, or release authority.

## 15. Literal source records

The following source records are inert raw bytes. Each identity is measured
only after its source is complete. Delimiters are unique literal lines.

P27 RUNNER V2 ACTOR SOURCE BEGIN 6A91D4E2
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
WHOLE_LEDGER=(2431,12439253869,0o100644,1,0,0,2288019,23569,b"fe04c56e704d99bab1c3182cad4811f7c585838f7d5dc2ebb1e42f8c3922e349")
WHOLE_V15=(2431,5916064615,0o100644,1,0,0,228310,4622,b"a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845")
LEDGER_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V1_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V2_AUTHOR_OPEN_NO_EXECUTION"
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
STAGE_NS=10000000000
REPORT_NS=1000000000
CERT_LIFE_NS=360000000000
ENTRY_REMAIN_NS=293472000000
CONSUME_REMAIN_NS=283472000000
RECORD_NS=100000000
STREAM_CAP=3145728
MAX_FILE=16777216
MAX_U63=(1<<63)-1
UINT_MAX=(1<<32)-1
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
O_DIR=os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW
LIBC=ctypes.CDLL(None,use_errno=True)
LIBC.syscall.restype=ctypes.c_long
SYS_CLONE3=435
CLONE_PIDFD=0x00001000
CLONE_INTO_CGROUP=0x200000000
CGROUP2_MAGIC=0x63677270
PREFLIGHT=True

FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"ATTEMPT_NAMESPACE_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"CONTROL_PACKET",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_SEMANTICS",b"ACK_DURABILITY",b"CONTAINMENT_NOT_EMPTY",b"REPORT_DURABILITY")

class Refuse(Exception):
 pass

class ConsumedFail(Exception):
 pass

class ConsumedIndeterminate(Exception):
 pass

class CertificateExpired(ConsumedIndeterminate):
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

def durable_leaf(directory,name,raw,kind=ConsumedIndeterminate):
 number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=directory)
 try:
  write_all(number,raw,kind);os.fsync(number);held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw),kind)
  need(read_all(number,len(raw))==raw,kind)
 finally:os.close(number)
 os.fsync(directory)

def stage_leaf(directory,name,raw,identity):
 durable_leaf(directory,name,raw)
 number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory)
 try:
  held=os.fstat(number);again=read_all(number,identity[0])
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_nlink==1 and held.st_uid==held.st_gid==0)
  need(meta(again)==identity)
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

ENVELOPE_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0365_SHA256",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX")

CERT_KEYS=(b"ISSUER_ID",b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0365_SHA256",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_TYPE_HEX",b"CGROUP_CONTROLLERS_HEX",b"CGROUP_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DEP_COUNT")

def parse_envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V2",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V2",b"E0365_SHA256":WHOLE_LEDGER[8],b"V15_SHA256":WHOLE_V15[8],b"ONE_SHOT_CONSUMED_BY_ISSUER":b"1",b"SIGNATURE_ALGORITHM":b"EXTERNALLY_VERIFIED_ED25519"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig),Refuse)
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"])
 need(before<after,Refuse)
 return values

def parse_cert(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V2" and lines[-1]==b"CERTIFICATE_END=1",Refuse)
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
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V2",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0365_SHA256":WHOLE_LEDGER[8],b"V15_SHA256":WHOLE_V15[8],b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"CLONE3_CPYTHON_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_ENVELOPE_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"CLONE3_CPYTHON_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64,Refuse)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1",Refuse)
 for key in (b"KERNEL_RELEASE_HEX",b"CGROUP_TYPE_HEX",b"CGROUP_CONTROLLERS_HEX",b"CGROUP_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"LIBC_MODE"):octal(values[key])
 for key in CERT_KEYS:
  if key.endswith((b"_DEV",b"_INO",b"_NLINK",b"_UID",b"_GID",b"_BYTES",b"_COUNT",b"_MOUNT_ID",b"_REALTIME_NS")) or key==b"ABSOLUTE_EXPIRY_REALTIME_NS":udec(values[key])
 by_role={role:next(x for x in deps if x[0]==role) for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC")}
 need(by_role[b"PYTHON_LINK"][1]==PYTHON and by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"ENV_EXEC"][1]==b"/usr/bin/env" and by_role[b"BASH_EXEC"][1]==b"/usr/bin/bash",Refuse)
 libc=(udec(values[b"LIBC_DEV"],1),udec(values[b"LIBC_INO"],1),octal(values[b"LIBC_MODE"]),udec(values[b"LIBC_NLINK"],1),0,0,udec(values[b"LIBC_BYTES"],1),values[b"LIBC_SHA256"])
 need(by_role[b"LIBC"][1]==even_hex(values[b"LIBC_PATH_HEX"]) and by_role[b"LIBC"][2]==libc,Refuse)
 return values,tuple(deps)

def cert_live(cert,needed,kind=ConsumedIndeterminate):
 now=time.time_ns();before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 if not (before<=now<expiry and expiry-now>=needed):
  if kind is Refuse:raise Refuse("certificate-life")
  raise CertificateExpired("certificate-life")
 return now

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
 m0=time.monotonic_ns();real=time.time_ns();m1=time.monotonic_ns()
 base_r=udec(cert[b"REALTIME_BIND_NS"]);base_m=udec(cert[b"MONOTONIC_BIND_NS"])
 need(base_m<=m1 and m0<=m1,kind)
 low=base_r+(m0-base_m);high=base_r+(m1-base_m)
 drift=udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"])
 need(low-drift<=real<=high+drift,kind)

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
 need(seen-expected==set())

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

# P27 RUNNER V2 EMBEDDED VALIDATOR BEGIN D27C8B41
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
# P27 RUNNER V2 EMBEDDED VALIDATOR END D27C8B41

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

def send_rights(control,raw,numbers):
 cells=array.array("i",numbers)
 count=control.sendmsg([raw],[(socket.SOL_SOCKET,socket.SCM_RIGHTS,cells.tobytes())])
 need(count==len(raw),ConsumedIndeterminate)

def recv_control(control,deadline,cap=65536):
 remaining=deadline-time.monotonic_ns();need(remaining>0,ConsumedIndeterminate)
 control.settimeout(max(0.001,remaining/1000000000))
 raw=control.recv(cap);need(raw,ConsumedIndeterminate);return raw

def wait_exact(control,deadline,expected):
 need(recv_control(control,deadline)==expected,ConsumedIndeterminate)

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

def wait_status(pid,flags,deadline):
 while True:
  try:waited,raw=os.waitpid(pid,flags|os.WNOHANG)
  except InterruptedError:continue
  need(waited in (0,pid),ConsumedIndeterminate)
  if waited==pid:return raw
  need(time.monotonic_ns()<=deadline,ConsumedIndeterminate)
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
   argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",b"WATCH",AUTH_ID,str(actor_pid).encode(),cert[b"PLAN_SHA256"],cert[b"RECOVERY_SHA256"],str(base_stats[b"safe"].st_dev).encode(),str(base_stats[b"safe"].st_ino).encode())
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
 keys=(b"ordinal",b"probe",b"outer_pid",b"pidfd_ready",b"stdout_len",b"stderr_len",b"stdout_eof",b"stderr_eof",b"fault_set",b"done_ns")
 values=parse_packet(raw,b"RESULT",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==pid and values[b"pidfd_ready"]==b"1",ConsumedIndeterminate)
 out_need=udec(values[b"stdout_len"],0,STREAM_CAP);err_need=udec(values[b"stderr_len"],0,STREAM_CAP);out=bytearray();err=bytearray()
 while True:
  frame=recv_control(control,deadline,65536)
  if frame==b"RESULT_END\n":break
  need(frame[:1] in (b"O",b"E"),ConsumedIndeterminate);target=out if frame[:1]==b"O" else err
  target.extend(frame[1:]);need(len(target)<=STREAM_CAP,ConsumedIndeterminate)
 need(len(out)==out_need and len(err)==err_need,ConsumedIndeterminate)
 return values,bytes(out),bytes(err)

CRASH_FAULT={b"INPUT":b"INPUT_AUTH",b"ENTRY":b"ENTRY_CONTEXT",b"CERT":b"CERTIFICATE_INVALID",b"B_BOOT":b"ACTOR_LOST",b"CONSUME":b"ATTEMPT_NAMESPACE_UNKNOWN",b"STAGE":b"STAGING_FAULT",b"CONTAIN":b"CONTAINMENT_FAULT",b"STREAM_ARM":b"CONTROL_PACKET",b"CLONE":b"RELEASE_EFFECT_UNKNOWN",b"PIDFD_ARM":b"PIDFD_BINDING",b"STOP":b"LAUNCH_DEADLINE",b"RELEASE_RECORD":b"ACK_DURABILITY",b"SIGCONT":b"RELEASE_EFFECT_UNKNOWN",b"WAIT":b"OUTER_STATUS",b"RESULT":b"WATCHDOG_DEADLINE",b"PARSER":b"TRANSCRIPT_SEMANTICS",b"RECEIPT":b"ACK_DURABILITY",b"REMOVE":b"CONTAINMENT_NOT_EMPTY",b"FINAL":b"REPORT_DURABILITY"}

def run_probe(control,ordinal,probe,cgfd,safefd,safe,outer_source,ctx,p01c,cert):
 phase=b"STREAM_ARM";release_origin=time.monotonic_ns();launch_deadline=release_origin+LAUNCH_NS
 cert_live(cert,(15-ordinal)*TOTAL_NS+REPORT_NS)
 in_r,in_w=os.pipe2(os.O_CLOEXEC);os.close(in_w);need(os.read(in_r,1)==b"")
 out_r,out_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK);err_r,err_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
 need(os.fstat(out_r).st_ino!=os.fstat(err_r).st_ino)
 outer_fd=memfd(outer_source,"p27-v15-outer")
 events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
 kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
 pid=pidfd=-1
 try:
  stream=packet(b"STREAM_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode()),(b"stdout_dev",str(os.fstat(out_r).st_dev).encode()),(b"stdout_ino",str(os.fstat(out_r).st_ino).encode()),(b"stderr_dev",str(os.fstat(err_r).st_dev).encode()),(b"stderr_ino",str(os.fstat(err_r).st_ino).encode()),(b"events_dev",str(os.fstat(events).st_dev).encode()),(b"events_ino",str(os.fstat(events).st_ino).encode()),(b"kill_dev",str(os.fstat(kill).st_dev).encode()),(b"kill_ino",str(os.fstat(kill).st_ino).encode())))
  send_rights(control,stream,(out_r,err_r,events,kill))
  for number in (out_r,err_r,events,kill):os.close(number)
  out_r=err_r=events=kill=-1;wait_exact(control,launch_deadline,b"STREAMS_ARMED\n")
  phase=b"CLONE";argv=source_argv(probe,safe,p01c);pid,pidfd=launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd)
  for number in (in_r,out_w,err_w,outer_fd):os.close(number)
  in_r=out_w=err_w=outer_fd=-1
  phase=b"STOP";stopped=wait_status(pid,os.WUNTRACED,launch_deadline);need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP,ConsumedIndeterminate)
  exact_child_cgroup(cgfd,pid);need(not cgroup_empty(cgfd),ConsumedIndeterminate)
  phase=b"PIDFD_ARM";arm=packet(b"PIDFD_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1")))
  send_rights(control,arm,(pidfd,));os.close(pidfd);pidfd=-1;wait_exact(control,launch_deadline,b"PIDFD_ARMED\n")
  outer_pid=pid
  phase=b"RELEASE_RECORD";release=packet(b"RELEASE_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"argv_sha256",sha(b"\x00".join(argv))),(b"env_sha256",sha(b"\x00".join(x+b"="+ENV[x] for x in sorted(ENV)))),(b"launch_deadline_ns",str(launch_deadline).encode())))
  need(control.send(release)==len(release),ConsumedIndeterminate);wait_exact(control,launch_deadline,b"RELEASE_DURABLE\n")
  phase=b"SIGCONT";cert_live(cert,(15-ordinal)*TOTAL_NS+REPORT_NS)
  call_entry=time.monotonic_ns();need(call_entry+SIGCONT_NS<=launch_deadline,ConsumedIndeterminate)
  os.kill(pid,signal.SIGCONT);release_return=time.monotonic_ns();need(release_return<=call_entry+SIGCONT_NS and release_return<=launch_deadline,ConsumedIndeterminate)
  cert_live(cert,(15-ordinal)*TOTAL_NS+REPORT_NS)
  phase=b"WAIT";raw=wait_status(pid,0,release_origin+TOTAL_NS+CLEANUP_NS);pid=-1;direct_done=time.monotonic_ns()
  phase=b"RESULT";values,stdout,stderr=recv_result(control,release_origin+TOTAL_NS+CLEANUP_NS,ordinal,probe,outer_pid)
  done=udec(values[b"done_ns"]);host_complete=max(direct_done,done)
  known=values[b"fault_set"]==b"NONE" and values[b"stdout_eof"]==values[b"stderr_eof"]==b"1" and cgroup_empty(cgfd)
  need(known and stderr==b"" and raw==0 and host_complete<=release_origin+HOST_NS,ConsumedFail)
  phase=b"PARSER";rows=validate_transcript(stdout,probe,ctx)
  phase=b"RECEIPT";candidate=packet(b"VALIDATED_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_origin_ns",str(release_origin).encode()),(b"release_return_ns",str(release_return).encode()),(b"host_complete_ns",str(host_complete).encode()),(b"outer_raw_status",str(raw).encode()),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stderr_len",b"0"),(b"stderr_sha256",EMPTY_SHA),(b"parser",b"ACCEPTED")))
  need(control.send(candidate)==len(candidate),ConsumedIndeterminate);wait_exact(control,release_origin+TOTAL_NS,b"VALIDATED_DURABLE\n")
  intent=packet(b"ACK_COMMIT_INTENT",((b"ordinal",str(ordinal).encode()),(b"probe",probe)))
  need(control.send(intent)==len(intent),ConsumedIndeterminate);wait_exact(control,release_origin+TOTAL_NS,b"COMMITTED\n")
  cert_live(cert,(14-ordinal)*TOTAL_NS+REPORT_NS);seen=packet(b"COMMITTED_SEEN",((b"ordinal",str(ordinal).encode()),(b"probe",probe)))
  need(control.send(seen)==len(seen),ConsumedIndeterminate)
  return rows
 except BaseException as error:
  fault=b"CERTIFICATE_EXPIRED" if isinstance(error,CertificateExpired) else CRASH_FAULT[phase]
  try:
   abort=packet(b"ABORT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"fault",fault)))
   control.send(abort)
   setattr(error,"p27_abort_sent",True)
  except BaseException:pass
  if pid>=0:
   try:wait_status(pid,0,time.monotonic_ns()+CLEANUP_NS+ACK_NS)
   except BaseException:pass
  setattr(error,"p27_phase",phase);raise
 finally:
  for number in (in_r,out_r,out_w,err_r,err_w,outer_fd,events,kill,pidfd):
   if number>=0:
    try:os.close(number)
    except OSError:pass

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

def b_send(control,raw):
 need(control.send(raw)==len(raw),ConsumedIndeterminate)

def main():
 global AUTH_ID,PREFLIGHT
 entry_mono=time.monotonic_ns();state=b"INPUT";consumed=False;bpid=-1;control=None
 need(type(sys.argv)is list and len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RUN",Refuse)
 supplied=h64(sys.argv[2].encode("ascii"))
 need(os.environb==ENV and os.read(0,1)==b"" and sys.gettrace() is None and sys.getprofile() is None,Refuse)
 verify_creds(False);need(os.umask(0o077)==0o077,Refuse)
 fd0=os.fstat(0);fd1=os.fstat(1);fd2=os.fstat(2)
 need(stat.S_ISFIFO(fd0.st_mode) and stat.S_ISFIFO(fd1.st_mode) and stat.S_ISFIFO(fd2.st_mode),Refuse)
 fd_access(0,os.O_RDONLY);fd_access(1,os.O_WRONLY);fd_access(2,os.O_WRONLY)
 need((fd1.st_dev,fd1.st_ino)!=(fd2.st_dev,fd2.st_ino),Refuse)
 close_range(3,99);close_range(107,UINT_MAX);scrub_exact({0,1,2,100,101,102,103,104,105,106})
 for number in (100,104,105,106):seals(number)
 actor_raw=read_all(100);ledger=exact_whole(101,WHOLE_LEDGER,LEDGER_TERMINAL)
 v15=exact_whole(102,WHOLE_V15,V15_TERMINAL);plan=read_all(103,MAX_FILE)
 cert_raw=read_all(104);envelope_raw=read_all(105);b_raw=read_all(106)
 AUTH_ID=sha(b"P27E001V2\x00"+cert_raw+b"\x00"+envelope_raw);need(AUTH_ID==supplied,Refuse)
 state=b"CERT";envelope=parse_envelope(envelope_raw);cert,deps=parse_cert(cert_raw)
 need(sha(cert_raw)==envelope[b"CERTIFICATE_SHA256"] and sha(envelope_raw)==cert[b"ISSUER_ENVELOPE_SHA256"],Refuse)
 need(envelope[b"PLAN_SHA256"]==cert[b"PLAN_SHA256"] and envelope[b"RUNNER_SHA256"]==cert[b"RUNNER_SHA256"] and envelope[b"RECOVERY_SHA256"]==cert[b"RECOVERY_SHA256"],Refuse)
 need(sha(plan)==cert[b"PLAN_SHA256"] and sha(actor_raw)==cert[b"RUNNER_SHA256"] and sha(b_raw)==cert[b"RECOVERY_SHA256"],Refuse)
 not_before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(envelope[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(envelope[b"NOT_AFTER_REALTIME_NS"]),Refuse)
 cert_live(cert,ENTRY_REMAIN_NS,Refuse);clock_binding(cert,Refuse);verify_platform(cert);signal_snapshot(cert)
 ab=b"P27 RUNNER V2 ACTOR SOURCE "+b"BEGIN 6A91D4E2";ae=b"P27 RUNNER V2 ACTOR SOURCE "+b"END 6A91D4E2"
 bb=b"P27 RUNNER V2 WATCHDOG SOURCE "+b"BEGIN F53E709A";be=b"P27 RUNNER V2 WATCHDOG SOURCE "+b"END F53E709A"
 need(extract_one(plan,ab,ae)==actor_raw and extract_one(plan,bb,be)==b_raw,Refuse)
 sources=v15_sources(v15)
 state=b"ENTRY";runtime=open_dir(RUNTIME_ROOT);attempt_base=open_dir(ATTEMPT_BASE);stage_base=open_dir(STAGE_BASE);cgroup_base=open_dir(CGROUP_BASE)
 try:
  runtime_stat=base_identity(runtime,cert,b"RUNTIME_ROOT");runtime_mid,runtime_line=mount_line(runtime)
  need(runtime_mid==udec(cert[b"RUNTIME_ROOT_MOUNT_ID"],1) and sha(runtime_line)==cert[b"RUNTIME_ROOT_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(runtime_line,even_hex(cert[b"RUNTIME_ROOT_FSTYPE_HEX"]),{b"ro",b"nosuid",b"nodev"},{b"rw"})
  for entry in deps:verify_dependency(runtime,entry)
  attempt_stat=base_identity(attempt_base,cert,b"ATTEMPT_BASE");attempt_mid,attempt_line=mount_line(attempt_base)
  need(attempt_mid==udec(cert[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==cert[b"ATTEMPT_BASE_MOUNTINFO_SHA256"],Refuse)
  stage_stat=base_identity(stage_base,cert,b"SAFE_BIND");stage_mid,stage_line=mount_line(stage_base)
  need(stage_mid==udec(cert[b"SAFE_BIND_MOUNT_ID"],1) and sha(stage_line)==cert[b"SAFE_BIND_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(stage_line,even_hex(cert[b"SAFE_BIND_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev",b"noexec"},{b"ro"})
  cgroup_stat=base_identity(cgroup_base,cert,b"CGROUP_BASE");cg_mid,cg_line=mount_line(cgroup_base)
  need(statfs_magic(cgroup_base)==CGROUP2_MAGIC and cg_mid==udec(cert[b"CGROUP2_MOUNT_ID"],1) and sha(cg_line)==cert[b"CGROUP2_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(cg_line,b"cgroup2",{b"rw"},{b"ro"})
  need(runtime_mid!=stage_mid,Refuse)
  mount_graph(cert)
  absent(attempt_base,AUTH_ID,Refuse);absent(stage_base,AUTH_ID,Refuse);absent(cgroup_base,AUTH_ID,Refuse)
  need(time.monotonic_ns()-entry_mono<=PRECONSUME_NS,Refuse)
  bases={b"attempt_fd":attempt_base,b"cgroup_fd":cgroup_base,b"safe":stage_stat}
  state=b"B_BOOT";bpid,control=launch_b(cert,bases)
  ready_deadline=entry_mono+PRECONSUME_NS;wait_exact(control,ready_deadline,b"READY\n")
  clock_binding(cert,Refuse);cert_live(cert,CONSUME_REMAIN_NS,Refuse)
  state=b"CONSUME";b_send(control,b"CONSUME_BEGIN\n");wait_exact(control,ready_deadline,b"CONSUME_ARMED\n")
  b_send(control,b"CONSUME_COMMIT\n");wait_exact(control,ready_deadline,b"CONSUMED_DURABLE\n");consumed=True;PREFLIGHT=False
  clock_binding(cert);cert_live(cert,CONSUME_REMAIN_NS)
  state=b"STAGE";stage_origin=time.monotonic_ns();os.mkdir(AUTH_ID,0o700,dir_fd=stage_base);os.fsync(stage_base)
  safefd=os.open(AUTH_ID,O_DIR,dir_fd=stage_base);safe=os.fstat(safefd)
  need((safe.st_uid,safe.st_gid,stat.S_IMODE(safe.st_mode),safe.st_nlink)==(0,0,0o700,2),ConsumedIndeterminate)
  for name in (b"target",b"a",b"b"):absent(safefd,name)
  for name,body,identity in zip(SOURCE_NAMES,sources[1:],SOURCE_META[1:]):stage_leaf(safefd,name,body,identity)
  os.fsync(safefd);need(time.monotonic_ns()-stage_origin<=STAGE_NS,ConsumedIndeterminate)
  cert_live(cert,15*TOTAL_NS+REPORT_NS)
  staged=packet(b"STAGE_DURABLE",((b"safe_dev",str(safe.st_dev).encode()),(b"safe_ino",str(safe.st_ino).encode())))
  b_send(control,staged);wait_exact(control,time.monotonic_ns()+ACK_NS,b"STAGE_ACK\n")
  state=b"CONTAIN";os.mkdir(AUTH_ID,0o700,dir_fd=cgroup_base);cgfd=os.open(AUTH_ID,O_DIR,dir_fd=cgroup_base)
  cgchild=os.fstat(cgfd);need(cgroup_empty(cgfd),ConsumedIndeterminate)
  ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  try:
   need(read_all(ctype,128)==even_hex(cert[b"CGROUP_TYPE_HEX"]) and read_all(controllers,4096)==even_hex(cert[b"CGROUP_CONTROLLERS_HEX"]) and read_all(subtree,4096)==even_hex(cert[b"CGROUP_SUBTREE_CONTROL_HEX"]),ConsumedIndeterminate)
  finally:os.close(ctype);os.close(controllers);os.close(subtree)
  containment=packet(b"CONTAINMENT",((b"dev",str(cgchild.st_dev).encode()),(b"ino",str(cgchild.st_ino).encode()),(b"mode",format(cgchild.st_mode,"o").encode()),(b"uid",str(cgchild.st_uid).encode()),(b"gid",str(cgchild.st_gid).encode())))
  send_rights(control,containment,(cgfd,));wait_exact(control,time.monotonic_ns()+ACK_NS,b"CONTAINMENT_ACK\n")
  safe_path=STAGE_BASE+b"/"+AUTH_ID
  ctx={b"cwd_hex":safe_path.hex().encode(),b"python_dev":udec(cert[b"PYTHON_IMAGE_DEV"],1),b"python_ino":udec(cert[b"PYTHON_IMAGE_INO"],1),b"libc_path_hex":cert[b"LIBC_PATH_HEX"],b"libc_confstr_hex":cert[b"LIBC_CONFSTR_HEX"],b"libc_bytes":udec(cert[b"LIBC_BYTES"],1),b"libc_sha":cert[b"LIBC_SHA256"],b"valid_signals":udec(cert[b"VALID_SIGNAL_COUNT"]),b"default_signals":udec(cert[b"DEFAULT_SIGNAL_COUNT"]),b"defaults_sha":cert[b"DEFAULTS_SHA256"],b"child_source":sources[4]}
  prior=None
  for ordinal,probe in enumerate(SUITE):
   cert_live(cert,(15-ordinal)*TOTAL_NS+REPORT_NS);clock_binding(cert)
   p01c=derive_p01c(prior,cert) if probe==b"P01C" else ()
   rows=run_probe(control,ordinal,probe,cgfd,safefd,safe,sources[0],ctx,p01c,cert)
   if probe==b"P01D":prior=rows;ctx[b"p01d"]=rows
  state=b"REMOVE";cert_live(cert,REPORT_NS);need(cgroup_empty(cgfd),ConsumedIndeterminate)
  b_send(control,b"EMPTY_FINAL_QUERY\n");wait_exact(control,time.monotonic_ns()+ACK_NS,b"EMPTY_FINAL_CONFIRMED\n")
  os.close(cgfd);cgfd=-1;os.rmdir(AUTH_ID,dir_fd=cgroup_base)
  try:os.stat(AUTH_ID,dir_fd=cgroup_base,follow_symlinks=False);need(False,ConsumedIndeterminate)
  except FileNotFoundError:pass
  state=b"FINAL";cert_live(cert,REPORT_NS);clock_binding(cert)
  b_send(control,b"CGROUP_REMOVED\n");wait_exact(control,time.monotonic_ns()+ACK_NS,b"REMOVE_ACK\n")
  b_send(control,b"FINALIZE_PASS\n");wait_exact(control,time.monotonic_ns()+REPORT_NS,b"TERMINAL_DURABLE\n")
  b_send(control,b"TERMINAL_SEEN\n");control.close();control=None
  braw=wait_status(bpid,0,time.monotonic_ns()+ACK_NS);bpid=-1
  need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
  write_all(1,b"P27E001_RUNNER_V2|AUTH_ID="+AUTH_ID+b"|entered=15|committed=15|terminal_durable=1\n")
 except BaseException as error:
  phase=getattr(error,"p27_phase",state);fault=b"CERTIFICATE_EXPIRED" if isinstance(error,CertificateExpired) else CRASH_FAULT.get(phase,b"REPORT_DURABILITY")
  if control is not None:
   try:
    if consumed:
     stop=locals().get("probe",b"NONE");ordinal_value=locals().get("ordinal",0)
     if not getattr(error,"p27_abort_sent",False):
      abort=packet(b"ABORT",((b"ordinal",str(ordinal_value).encode()),(b"probe",stop),(b"fault",fault)))
      control.send(abort)
     wait_exact(control,time.monotonic_ns()+CLEANUP_NS+REPORT_NS,b"TERMINAL_DURABLE\n")
     control.send(b"TERMINAL_SEEN\n")
    else:control.send(b"REFUSE\n")
   except BaseException:pass
   try:control.close()
   except BaseException:pass
  if bpid>=0:
   try:wait_status(bpid,0,time.monotonic_ns()+CLEANUP_NS+REPORT_NS)
   except BaseException:pass
  if not consumed:raise Refuse("preconsume") from error
  if isinstance(error,ConsumedFail):raise
  raise ConsumedIndeterminate("postconsume") from error
 finally:
  for number in (locals().get("cgfd",-1),locals().get("safefd",-1),runtime,attempt_base,stage_base,cgroup_base):
   if number>=0:
    try:os.close(number)
    except OSError:pass

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
P27 RUNNER V2 ACTOR SOURCE END 6A91D4E2

P27 RUNNER V2 WATCHDOG SOURCE BEGIN F53E709A
import array
import ctypes
import errno
import fcntl
import hashlib
import os
import select
import signal
import socket
import stat
import struct
import sys
import time

PROBES=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"ATTEMPT_NAMESPACE_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"CONTROL_PACKET",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_SEMANTICS",b"ACK_DURABILITY",b"CONTAINMENT_NOT_EMPTY",b"REPORT_DURABILITY")
INDETERMINATE={b"ATTEMPT_NAMESPACE_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"ACTOR_LOST",b"CERTIFICATE_EXPIRED",b"CONTAINMENT_FAULT",b"CONTROL_PACKET",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_EFFECT_UNKNOWN",b"ACK_DURABILITY",b"CONTAINMENT_NOT_EMPTY",b"REPORT_DURABILITY"}
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
LEDGER_EXPECT=(2431,12439253869,0o100644,1,0,0,2288019,23569,b"fe04c56e704d99bab1c3182cad4811f7c585838f7d5dc2ebb1e42f8c3922e349")
LEDGER_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V1_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V2_AUTHOR_OPEN_NO_EXECUTION"
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
MAX_U63=(1<<63)-1
STREAM_CAP=3145728
TOTAL_NS=18164800000
HOST_NS=17664800000
CLEANUP_NS=2000000000
ACK_NS=500000000
REPORT_NS=1000000000
UINT_MAX=(1<<32)-1

class Closed(Exception):
 pass

class ActorLost(Exception):
 pass

class CertificateExpired(Closed):
 pass

def need(value):
 if not value:raise Closed("closed")

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw);return value

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(x in b"0123456789abcdef" for x in raw));return raw

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
 body=kind
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value)
  body+=b"|"+key+b"="+value
 return body+b"\n"

def parse_packet(raw,kind,keys):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1);fields=raw[:-1].split(b"|")
 need(fields[0]==kind and len(fields)==len(keys)+1);result={}
 for key,item in zip(keys,fields[1:]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result and parts[1]);result[key]=parts[1]
 return result

def contract(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines[0]==b"P27E001_PREMISE_CERTIFICATE_V2" and lines[-1]==b"CERTIFICATE_END=1")
 fixed=[];deps=[];in_deps=False
 for line in lines[1:-1]:
  if line.startswith(b"DEP["):in_deps=True;deps.append(line);continue
  need(not in_deps);parts=line.split(b"=",1);need(len(parts)==2);fixed.append(parts)
 keys=[x[0] for x in fixed];need(len(keys)==len(set(keys)));values=dict(fixed)
 required=(b"ISSUER_ID",b"ISSUER_ENVELOPE_SHA256",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0365_SHA256",b"V15_SHA256",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_TYPE_HEX",b"CGROUP_CONTROLLERS_HEX",b"CGROUP_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"FSYNC_DURABILITY_PREMISE",b"DEP_COUNT")
 need(all(x in values for x in required) and [keys.index(x) for x in required]==sorted(keys.index(x) for x in required))
 need(values[b"ISSUER_ID"]==b"P27_HOST_PREMISE_ISSUER_V2" and values[b"E0365_SHA256"]==LEDGER_EXPECT[8])
 need(values[b"ABSOLUTE_LIFETIME_NS"]==b"360000000000" and values[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"]==b"1000000")
 for key in (b"CGROUP_NO_EXTERNAL_MUTATOR",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1")
 count=udec(values[b"DEP_COUNT"],1,256);need(len(deps)==count)
 for index,line in enumerate(deps):need(line.startswith(b"DEP[%04d]="%index))
 return values

def envelope(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 keys=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0365_SHA256",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX")
 need(len(lines)==len(keys)+2 and lines[0]==b"P27E001_ISSUER_ENVELOPE_V2" and lines[-1]==b"ENVELOPE_END=1");values={}
 for key,line in zip(keys,lines[1:-1]):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key);values[key]=parts[1]
 need(values[b"ISSUER_ID"]==b"P27_HOST_PREMISE_ISSUER_V2" and values[b"E0365_SHA256"]==LEDGER_EXPECT[8] and values[b"ONE_SHOT_CONSUMED_BY_ISSUER"]==b"1" and values[b"SIGNATURE_ALGORITHM"]==b"EXTERNALLY_VERIFIED_ED25519")
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):h64(values[key])
 need(len(values[b"SIGNATURE_HEX"])==128 and all(x in b"0123456789abcdef" for x in values[b"SIGNATURE_HEX"]))
 return values

def cert_live(cert,needed=0):
 m0=time.monotonic_ns();real=time.time_ns();m1=time.monotonic_ns()
 before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 if not (before<=real<expiry and expiry-real>=needed):raise CertificateExpired("certificate-life")
 base_r=udec(cert[b"REALTIME_BIND_NS"]);base_m=udec(cert[b"MONOTONIC_BIND_NS"]);need(base_m<=m1)
 drift=udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"]);low=base_r+(m0-base_m);high=base_r+(m1-base_m)
 need(low-drift<=real<=high+drift)

def cap_status():
 number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=ascii_file(read_all(number,65536),65536)
 finally:os.close(number)
 values={}
 for line in raw.splitlines():
  for key in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs"):
   if line.startswith(key+b":"):need(key not in values);values[key]=line.split(b":",1)[1].strip()
 need(set(values)=={b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs"});return values

def final_context(safe_dev,safe_ino):
 values=cap_status();zero=b"0000000000000000"
 need(os.getresuid()==(0,0,0) and os.getresgid()==(0,0,0) and os.getgroups()==[])
 need(all(values[x]==zero for x in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb")) and values[b"NoNewPrivs"]==b"1")
 libc=ctypes.CDLL(None,use_errno=True);need(libc.prctl(27,0,0,0,0)==15)
 held=os.stat(b".",follow_symlinks=False);need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
 need(os.umask(0o077)==0o077 and all(signal.getitimer(x)==(0.0,0.0) for x in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF)))
 need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set() and all(signal.getsignal(x)==signal.SIG_DFL for x in signal.valid_signals() if x not in (signal.SIGKILL,signal.SIGSTOP)))
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

def whole_ledger():
 raw=read_all(9,LEDGER_EXPECT[6]);held=os.fstat(9)
 observed=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,raw.count(b"\n"),sha(raw))
 need(observed==LEDGER_EXPECT and raw.endswith(b"\n"))
 lines=raw[:-1].split(b"\n");need(lines[-1]==LEDGER_TERMINAL and lines.count(LEDGER_TERMINAL)==1)

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

def durable(directory,name,raw):
 number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=directory)
 try:
  write_all(number,raw);os.fsync(number);held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw))
  need(read_all(number,len(raw))==raw)
 finally:os.close(number)
 os.fsync(directory)

def primary(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults);need(len(ordered)==len(faults))
 return ordered[0] if ordered else b"NONE"

def disposition(faults):
 return b"CONSUMED_INDETERMINATE" if any(x in INDETERMINATE for x in faults) else b"CONSUMED_FAIL"

def recovery_record(context,stop,faults,empty):
 chosen=primary(faults);fault_csv=b",".join(x for x in FAULT_ORDER if x in faults);disp=disposition(faults)
 direct=b"COMPLETE" if context[b"direct_reaps"]==context[b"entered"] and b"ACTOR_LOST" not in faults else b"UNAVAILABLE"
 body=(b"P27E001_RECOVERY_STATE_V2\nAUTH_ID="+AUTH+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+chosen+b"\nFAULT_SET="+fault_csv+b"\nINTENT_DURABLE="+(b"1" if context[b"intent_durable"] else b"0")+b"\nDIRECT_REAP="+direct+b"\nSTDOUT_EOF="+(b"1" if context.get(b"last_out_eof",False) else b"0")+b"\nSTDERR_EOF="+(b"1" if context.get(b"last_err_eof",False) else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_count"]).encode()+b"\nKILL_WRITE_RETURNED="+(b"1" if context[b"kill_returned"] else b"0")+b"\nCGROUP_EMPTY="+(b"1" if empty else b"0")+b"\nRETRY_ALLOWED=0\nDISPOSITION="+disp+b"\nRECOVERY_END=1\n")
 name=b"recovery.v2" if context[b"intent_durable"] else b"preintent.v2"
 durable(context[b"attempt"],name,body)

def populated(number):
 os.lseek(number,0,os.SEEK_SET);raw=os.read(number,4096)
 values=[x for x in raw.splitlines() if x.startswith(b"populated ")]
 need(len(values)==1 and values[0] in (b"populated 0",b"populated 1"));return values[0]==b"populated 1"

def drain(number,target):
 overflow=False;eof=False
 while True:
  try:chunk=os.read(number,65536)
  except BlockingIOError:break
  except InterruptedError:continue
  if chunk==b"":eof=True;break
  room=STREAM_CAP-len(target)
  if room>0:target.extend(chunk[:room])
  if len(chunk)>room:overflow=True
 return overflow,eof

def recv_monitored(control,actor_pidfd,deadline,rights):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(actor_pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  remaining=deadline-time.monotonic_ns();need(remaining>0)
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  if any(number==actor_pidfd for number,event in events):raise ActorLost("actor")
  if any(number==control.fileno() and event&(select.POLLHUP|select.POLLERR) for number,event in events):raise ActorLost("control")
  if any(number==control.fileno() and event&select.POLLIN for number,event in events):
   if rights==0:
    raw=control.recv(65536);need(raw);return raw,()
   raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(rights*array.array("i").itemsize))
   need(raw and flags==0 and address is None and len(ancillary)==1)
   level,kind,data=ancillary[0];need(level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS)
   cells=array.array("i");need(len(data)==rights*cells.itemsize);cells.frombytes(data)
   need(len(cells)==rights);return raw,tuple(cells)

def send_exact(control,raw):
 need(control.send(raw)==len(raw))

def attempt_intent(auth,cert,cert_raw,envelope_raw,source_raw):
 return (b"P27E001_ATTEMPT_INTENT_V2\nAUTH_ID="+auth+b"\nNONCE="+auth+b"\nISSUER_ENVELOPE_SHA256="+sha(envelope_raw)+b"\nCERTIFICATE_SHA256="+sha(cert_raw)+b"\nPLAN_SHA256="+cert[b"PLAN_SHA256"]+b"\nRUNNER_SHA256="+cert[b"RUNNER_SHA256"]+b"\nRECOVERY_SHA256="+sha(source_raw)+b"\nE0365_SHA256="+LEDGER_EXPECT[8]+b"\nV15_SHA256="+cert[b"V15_SHA256"]+b"\nSUITE="+b",".join(PROBES)+b"\nATTEMPT_PATH_HEX="+(b"/var/lib/p27-e001-host-v15/attempts/"+auth).hex().encode()+b"\nSTAGE_PATH_HEX="+(b"/tmp/p27-e001-host-v15/"+auth).hex().encode()+b"\nCGROUP_PATH_HEX="+(b"/sys/fs/cgroup/p27-e001-host-v15/"+auth).hex().encode()+b"\nACTOR_ENTRY_CAPS=00000000000401c0\nPAYLOAD_FINAL_CAPS=0000000000000000\nABSOLUTE_EXPIRY_REALTIME_NS="+cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCONSUMED=1\nRETRY_ALLOWED=0\nINTENT_END=1\n")

def consume_attempt(auth,cert,cert_raw,envelope_raw,source_raw):
 global RECOVERY_ATTEMPT
 try:os.mkdir(auth,0o700,dir_fd=5)
 except BaseException as error:
  try:
   held=os.open(auth,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
   RECOVERY_ATTEMPT=held
   observed=os.fstat(held);need(stat.S_ISDIR(observed.st_mode) and observed.st_uid==observed.st_gid==0 and stat.S_IMODE(observed.st_mode)==0o700)
  except BaseException:raise Closed("attempt-unknown") from error
  raise Closed("attempt-existed") from error
 os.fsync(5);attempt=os.open(auth,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
 RECOVERY_ATTEMPT=attempt
 held=os.fstat(attempt);need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and stat.S_IMODE(held.st_mode)==0o700 and held.st_nlink==2)
 durable(attempt,b"intent.v2",attempt_intent(auth,cert,cert_raw,envelope_raw,source_raw))
 return attempt

def release_record(attempt,values):
 body=(b"P27E001_RELEASE_V2\nAUTH_ID="+AUTH+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nOUTER_PID="+values[b"outer_pid"]+b"\nARGV_SHA256="+values[b"argv_sha256"]+b"\nENV_SHA256="+values[b"env_sha256"]+b"\nLAUNCH_DEADLINE_NS="+values[b"launch_deadline_ns"]+b"\nSTATE=RELEASE_AUTHORIZED\nRELEASE_END=1\n")
 durable(attempt,b"release-"+values[b"probe"]+b".v2",body)

def validated_record(attempt,values):
 body=(b"P27E001_PROBE_STATE_V2\nAUTH_ID="+AUTH+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nSTATE=VALIDATED_CANDIDATE\nRELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nRELEASE_RETURN_NS="+values[b"release_return_ns"]+b"\nHOST_COMPLETE_NS="+values[b"host_complete_ns"]+b"\nOUTER_RAW_STATUS="+values[b"outer_raw_status"]+b"\nDIRECT_WAIT=1\nSTDOUT_BYTES="+values[b"stdout_len"]+b"\nSTDOUT_SHA256="+values[b"stdout_sha256"]+b"\nSTDERR_BYTES="+values[b"stderr_len"]+b"\nSTDERR_SHA256="+values[b"stderr_sha256"]+b"\nSTDOUT_EOF=1\nSTDERR_EOF=1\nCGROUP_EMPTY=1\nPARSER=ACCEPTED\nCANDIDATE=ACCEPTED\nTERMINAL=ACCEPTED\nTOPOLOGY=V15_INTERNAL_VALIDATION_REPORTED_BY_COMPLETE_TRANSCRIPT\nEXTERNAL_TOPOLOGY_RECONSTRUCTION=UNAVAILABLE\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nRECORD_END=1\n")
 durable(attempt,b"receipt-"+values[b"probe"]+b"-validated.v2",body)

def ack_intent_record(attempt,ordinal,probe):
 body=(b"P27E001_PROBE_STATE_V2\nAUTH_ID="+AUTH+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=ACK_COMMIT_INTENT\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nRECORD_END=1\n")
 durable(attempt,b"receipt-"+probe+b"-ack-intent.v2",body)

def kill_once(context,reason):
 if context[b"kill_count"]!=0:return
 ticket=(b"P27E001_KILL_TICKET_V2\nAUTH_ID="+AUTH+b"\nPRIMARY="+reason+b"\nKILL_CALL_COUNT_BEFORE=0\nWRITE_BYTES_HEX=310a\nRETRY_ALLOWED=0\nTICKET_END=1\n")
 durable(context[b"attempt"],b"kill-ticket.v2",ticket);context[b"kill_count"]=1
 number=context.get(b"kill_fd",-1)
 if number<0:number=context.get(b"root_kill_fd",-1)
 if number<0:
  context[b"kill_unknown"]=True;return
 try:
  returned=os.write(number,b"1\n")
 except BaseException:
  context[b"kill_unknown"]=True;return
 if returned!=2:context[b"kill_unknown"]=True
 else:context[b"kill_returned"]=True

def report(context,stop,faults,removed):
 try:
  cert_live(CERT,REPORT_NS);live=True
 except BaseException:
  live=False
  if b"CERTIFICATE_EXPIRED" not in faults:faults.add(b"CERTIFICATE_EXPIRED")
  ordered=tuple(x for x in FAULT_ORDER if x in faults);chosen=primary(set(ordered))
 empty=False
 events_number=context.get(b"events_fd",-1)
 if events_number<0:events_number=context.get(b"root_events_fd",-1)
 if events_number>=0:
  try:empty=not populated(events_number)
  except BaseException:faults.add(b"CONTAINMENT_NOT_EMPTY")
 ordered=tuple(x for x in FAULT_ORDER if x in faults);chosen=primary(set(ordered))
 complete=len(context[b"committed"])==15 and all(context[b"committed"]) and not faults and empty and removed and context[b"kill_count"]==0 and live and context[b"direct_reaps"]==15
 disp=b"PASS" if complete else disposition(faults)
 fault_csv=b"NONE" if not faults else b",".join(x for x in FAULT_ORDER if x in faults)
 body=(b"P27E001_FINAL_REPORT_V2\nAUTH_ID="+AUTH+b"\nSUITE="+b",".join(PROBES)+b"\nENTERED_COUNT="+str(context[b"entered"]).encode()+b"\nCOMMITTED_COUNT="+str(sum(context[b"committed"])).encode()+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+chosen+b"\nFAULT_SET="+fault_csv+b"\nDIRECT_REAP_COMPLETE="+(b"1" if context[b"direct_reaps"]==context[b"entered"] else b"0")+b"\nCGROUP_EMPTY="+(b"1" if empty else b"0")+b"\nCGROUP_REMOVED="+(b"1" if removed else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_count"]).encode()+b"\nKILL_WRITE_RETURNED="+(b"1" if context[b"kill_returned"] else b"0")+b"\nCERTIFICATE_LIVE_AT_REPORT="+(b"1" if live else b"0")+b"\nSTAGE_RETAINED=1\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION="+disp+b"\nREPORT_END=1\n")
 durable(context[b"attempt"],b"report.v2",body)
 try:cert_live(CERT,0);post_live=True
 except CertificateExpired:post_live=False
 if disp==b"PASS":need(post_live)
 return empty,disp

def send_result(control,ordinal,probe,pid,context,stdout,stderr,out_eof,err_eof,out_over,err_over,empty,faults,done):
 fault_csv=b"NONE" if not faults else b",".join(x for x in FAULT_ORDER if x in faults)
 header=packet(b"RESULT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_ready",b"1" if context[b"pidfd_ready"] else b"0"),(b"stdout_len",str(len(stdout)).encode()),(b"stderr_len",str(len(stderr)).encode()),(b"stdout_eof",b"1" if out_eof else b"0"),(b"stderr_eof",b"1" if err_eof else b"0"),(b"fault_set",fault_csv),(b"done_ns",str(done).encode())))
 send_exact(control,header)
 for start in range(0,len(stdout),65535):send_exact(control,b"O"+stdout[start:start+65535])
 for start in range(0,len(stderr),65535):send_exact(control,b"E"+stderr[start:start+65535])
 send_exact(control,b"RESULT_END\n")

def stream_arm(control,context,ordinal,probe):
 keys=(b"ordinal",b"probe",b"release_origin_ns",b"launch_deadline_ns",b"stdout_dev",b"stdout_ino",b"stderr_dev",b"stderr_ino",b"events_dev",b"events_ino",b"kill_dev",b"kill_ino")
 raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,4);values=parse_packet(raw,b"STREAM_ARM",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 origin=udec(values[b"release_origin_ns"],1);launch=udec(values[b"launch_deadline_ns"],1);need(origin<launch==origin+1000000000)
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
  finally:os.close(own_events);os.close(own_kill)
 except BaseException:
  for number in fds:
   try:os.close(number)
   except OSError:pass
  raise
 context.update({b"out_fd":out,b"err_fd":err,b"events_fd":events,b"kill_fd":kill,b"origin":origin,b"launch":launch,b"pidfd_ready":False})
 send_exact(control,b"STREAMS_ARMED\n")

def pidfd_arm(control,context,ordinal,probe):
 raw,fds=recv_monitored(control,4,context[b"launch"],1)
 values=parse_packet(raw,b"PIDFD_ARM",(b"ordinal",b"probe",b"outer_pid",b"stopped_raw_status",b"cgroup_member"))
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 pid=udec(values[b"outer_pid"],2);number=fds[0]
 stopped=udec(values[b"stopped_raw_status"],1);need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and values[b"cgroup_member"]==b"1")
 try:
  fd_access(number,os.O_RDWR);need(pidfd_pid(number)==pid)
  procs=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  status=os.open(b"/proc/"+str(pid).encode()+b"/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  try:
   need(read_all(procs,64)==str(pid).encode()+b"\n")
   state=[x for x in ascii_file(read_all(status,65536),65536).splitlines() if x.startswith(b"State:\t")]
   need(len(state)==1 and state[0].startswith(b"State:\tT"))
  finally:os.close(procs);os.close(status)
 except BaseException:
  os.close(number);raise
 context[b"outer_pidfd"]=number;context[b"outer_pid"]=pid;context[b"pidfd_ready"]=True
 send_exact(control,b"PIDFD_ARMED\n")

def release_phase(control,context,ordinal,probe):
 raw,fds=recv_monitored(control,4,context[b"launch"],0);need(fds==())
 keys=(b"ordinal",b"probe",b"outer_pid",b"argv_sha256",b"env_sha256",b"launch_deadline_ns")
 values=parse_packet(raw,b"RELEASE_CANDIDATE",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==context[b"outer_pid"])
 h64(values[b"argv_sha256"]);h64(values[b"env_sha256"]);need(udec(values[b"launch_deadline_ns"])==context[b"launch"])
 cert_live(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS);release_record(context[b"attempt"],values)
 send_exact(control,b"RELEASE_DURABLE\n")

def monitor_probe(control,context,ordinal,probe):
 stdout=bytearray();stderr=bytearray();out_eof=err_eof=out_over=err_over=False;faults=set();actor_lost=False
 context[b"abort_received"]=False
 deadline=context[b"origin"]+HOST_NS;cleanup_deadline=0
 poller=select.poll()
 for number in (context[b"out_fd"],context[b"err_fd"],context[b"events_fd"],context[b"outer_pidfd"],4,control.fileno()):poller.register(number,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  now=time.monotonic_ns()
  try:events=poller.poll(10)
  except InterruptedError:events=[]
  if any(number==4 for number,event in events):
   faults.add(b"ACTOR_LOST");actor_lost=True
  for number,event in events:
   if number==context[b"out_fd"]:
    overflow,eof=drain(number,stdout);out_over|=overflow;out_eof|=eof
   elif number==context[b"err_fd"]:
    overflow,eof=drain(number,stderr);err_over|=overflow;err_eof|=eof
   elif number==context[b"outer_pidfd"]:context[b"pidfd_ready"]=True
   elif number==control.fileno() and event&select.POLLIN:
    message=control.recv(65536)
    context[b"abort_received"]=True
    if not message:faults.add(b"ACTOR_LOST");actor_lost=True
    elif message.startswith(b"ABORT|"):
     values=parse_packet(message,b"ABORT",(b"ordinal",b"probe",b"fault"))
     need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and values[b"fault"] in FAULT_ORDER)
     faults.add(values[b"fault"])
    else:faults.add(b"CONTROL_PACKET")
   elif number==control.fileno() and event&(select.POLLHUP|select.POLLERR):
    faults.add(b"ACTOR_LOST");actor_lost=True
  if not out_eof:
   overflow,eof=drain(context[b"out_fd"],stdout);out_over|=overflow;out_eof|=eof
  if not err_eof:
   overflow,eof=drain(context[b"err_fd"],stderr);err_over|=overflow;err_eof|=eof
  if out_over or err_over:faults.add(b"CAPTURE_OVERFLOW")
  if stderr:faults.add(b"STDERR_NONEMPTY")
  try:empty=not populated(context[b"events_fd"])
  except BaseException:empty=False;faults.add(b"CONTAINMENT_FAULT")
  if not faults and now>deadline:faults.add(b"WATCHDOG_DEADLINE")
  if faults and cleanup_deadline==0:
   cleanup_deadline=now+CLEANUP_NS
   if not empty:kill_once(context,primary(faults))
  if context[b"kill_unknown"]:faults.add(b"KILL_EFFECT_UNKNOWN")
  if not faults and out_eof and err_eof and empty and context[b"pidfd_ready"]:break
  if faults and out_eof and err_eof and empty:break
  if cleanup_deadline and now>cleanup_deadline:break
 done=time.monotonic_ns()
 try:empty=not populated(context[b"events_fd"])
 except BaseException:empty=False;faults.add(b"CONTAINMENT_FAULT")
 context[b"last_out_eof"]=out_eof;context[b"last_err_eof"]=err_eof
 if not actor_lost:send_result(control,ordinal,probe,context[b"outer_pid"],context,bytes(stdout),bytes(stderr),out_eof,err_eof,out_over,err_over,empty,faults,done)
 return actor_lost,faults,empty,bytes(stdout),bytes(stderr),out_eof,err_eof

def close_probe(context):
 for key in (b"out_fd",b"err_fd",b"events_fd",b"kill_fd",b"outer_pidfd"):
  number=context.get(key,-1)
  if number>=0:
   try:os.close(number)
   except OSError:pass
  context[key]=-1

def passive_until_empty(context):
 number=context.get(b"events_fd",-1)
 if number<0:number=context.get(b"root_events_fd",-1)
 if number<0:return
 while True:
  try:
   if not populated(number):return
  except BaseException:return
  for key in (b"out_fd",b"err_fd"):
   stream=context.get(key,-1)
   if stream>=0:
    try:drain(stream,bytearray())
    except BaseException:pass
  try:select.poll().poll(50)
  except InterruptedError:pass

def terminal_failure(control,context,stop,faults,actor_lost):
 events_number=context.get(b"events_fd",-1)
 if events_number<0:events_number=context.get(b"root_events_fd",-1)
 if events_number>=0:
  try:empty=not populated(events_number)
  except BaseException:empty=False;faults.add(b"CONTAINMENT_FAULT")
  if not empty and context[b"kill_count"]==0:kill_once(context,primary(faults))
  deadline=time.monotonic_ns()+CLEANUP_NS
  while time.monotonic_ns()<=deadline:
   try:
    if not populated(events_number):break
   except BaseException:faults.add(b"CONTAINMENT_FAULT");break
   for key in (b"out_fd",b"err_fd"):
    if context.get(key,-1)>=0:
     try:drain(context[key],bytearray())
     except BaseException:pass
   try:select.poll().poll(10)
   except InterruptedError:pass
 if context[b"kill_unknown"]:faults.add(b"KILL_EFFECT_UNKNOWN")
 try:final_empty=events_number>=0 and not populated(events_number)
 except BaseException:final_empty=False;faults.add(b"CONTAINMENT_FAULT")
 recovery_record(context,stop,faults,final_empty)
 empty,disp=report(context,stop,faults,False)
 if not actor_lost:
  try:
   send_exact(control,b"TERMINAL_DURABLE\n")
   raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0);need(fds==() and raw==b"TERMINAL_SEEN\n")
  except BaseException:actor_lost=True
 if not empty:passive_until_empty(context)
 return disp

def validated_exchange(control,context,ordinal,probe,stdout,stderr):
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 if raw.startswith(b"ABORT|"):
  values=parse_packet(raw,b"ABORT",(b"ordinal",b"probe",b"fault"))
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and values[b"fault"] in FAULT_ORDER)
  return {values[b"fault"]},False
 keys=(b"ordinal",b"probe",b"release_origin_ns",b"release_return_ns",b"host_complete_ns",b"outer_raw_status",b"stdout_len",b"stdout_sha256",b"stderr_len",b"stderr_sha256",b"parser")
 values=parse_packet(raw,b"VALIDATED_CANDIDATE",keys)
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"release_origin_ns"])==context[b"origin"])
 release_return=udec(values[b"release_return_ns"]);host_complete=udec(values[b"host_complete_ns"])
 need(context[b"origin"]<release_return<=context[b"launch"] and host_complete<=context[b"origin"]+HOST_NS)
 need(values[b"outer_raw_status"]==b"0" and values[b"parser"]==b"ACCEPTED")
 need(udec(values[b"stdout_len"])==len(stdout) and values[b"stdout_sha256"]==sha(stdout))
 need(udec(values[b"stderr_len"])==len(stderr)==0 and values[b"stderr_sha256"]==sha(stderr))
 h64(values[b"stdout_sha256"]);h64(values[b"stderr_sha256"])
 cert_live(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS);validated_record(context[b"attempt"],values)
 send_exact(control,b"VALIDATED_DURABLE\n")
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 intent=parse_packet(raw,b"ACK_COMMIT_INTENT",(b"ordinal",b"probe"))
 need(udec(intent[b"ordinal"],0,14)==ordinal and intent[b"probe"]==probe)
 need(time.monotonic_ns()+100000000<=context[b"origin"]+TOTAL_NS)
 ack_intent_record(context[b"attempt"],ordinal,probe);ack_now=time.monotonic_ns()
 need(ack_now-host_complete<=ACK_NS and ack_now-context[b"origin"]<=TOTAL_NS)
 cert_live(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS)
 context[b"committed"][ordinal]=True;context[b"direct_reaps"]+=1
 send_exact(control,b"COMMITTED\n")
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0);need(fds==())
 seen=parse_packet(raw,b"COMMITTED_SEEN",(b"ordinal",b"probe"))
 need(udec(seen[b"ordinal"],0,14)==ordinal and seen[b"probe"]==probe)
 return set(),True

def containment_bind(control,context):
 raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,1)
 values=parse_packet(raw,b"CONTAINMENT",(b"dev",b"ino",b"mode",b"uid",b"gid"));number=fds[0]
 try:
  held=os.fstat(number);need(stat.S_ISDIR(held.st_mode))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_uid,held.st_gid)==(udec(values[b"dev"],1),udec(values[b"ino"],1),octal(values[b"mode"]),udec(values[b"uid"]),udec(values[b"gid"])))
  named=os.stat(AUTH,dir_fd=6,follow_symlinks=False);need((named.st_dev,named.st_ino)==(held.st_dev,held.st_ino))
  ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  try:
   need(read_all(ctype,128).hex().encode()==CERT[b"CGROUP_TYPE_HEX"] and read_all(controllers,4096).hex().encode()==CERT[b"CGROUP_CONTROLLERS_HEX"] and read_all(subtree,4096).hex().encode()==CERT[b"CGROUP_SUBTREE_CONTROL_HEX"])
   need(not populated(root_events))
  finally:os.close(ctype);os.close(controllers);os.close(subtree)
 except BaseException:
  os.close(number);raise
 context[b"cgfd"]=number;context[b"root_events_fd"]=root_events;context[b"root_kill_fd"]=root_kill
 send_exact(control,b"CONTAINMENT_ACK\n")

def static_inputs():
 global AUTH,CERT,RECOVERY_ATTEMPT
 RECOVERY_ATTEMPT=-1
 need(type(sys.argv)is list and len(sys.argv)==8 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="WATCH")
 supplied=h64(sys.argv[2].encode("ascii"));actor_pid=udec(sys.argv[3].encode("ascii"),2)
 plan_sha=h64(sys.argv[4].encode("ascii"));source_sha=h64(sys.argv[5].encode("ascii"))
 safe_dev=udec(sys.argv[6].encode("ascii"),1);safe_ino=udec(sys.argv[7].encode("ascii"),1)
 need(os.read(0,1)==b"");fd_access(0,os.O_RDONLY);need(stat.S_ISFIFO(os.fstat(0).st_mode));closed(1);closed(2)
 control=socket.socket(fileno=3);need(control.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET);fd_access(3,os.O_RDWR)
 peer=struct.unpack("3i",control.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(actor_pid,0,0))
 fd_access(4,os.O_RDWR);need(pidfd_pid(4)==actor_pid)
 for number in (7,8,100):seals(number);fd_access(number,os.O_RDWR)
 fd_access(9,os.O_RDONLY);whole_ledger()
 cert_raw=read_all(7);envelope_raw=read_all(8);source_raw=read_all(100)
 CERT=contract(cert_raw);issued=envelope(envelope_raw)
 need(sha(cert_raw)==issued[b"CERTIFICATE_SHA256"] and sha(envelope_raw)==CERT[b"ISSUER_ENVELOPE_SHA256"])
 AUTH=sha(b"P27E001V2\x00"+cert_raw+b"\x00"+envelope_raw);need(AUTH==supplied)
 need(plan_sha==CERT[b"PLAN_SHA256"]==issued[b"PLAN_SHA256"])
 need(source_sha==sha(source_raw)==CERT[b"RECOVERY_SHA256"]==issued[b"RECOVERY_SHA256"])
 need(issued[b"E0365_SHA256"]==CERT[b"E0365_SHA256"]==LEDGER_EXPECT[8])
 base_check(5,CERT,b"ATTEMPT_BASE");base_check(6,CERT,b"CGROUP_BASE")
 need((safe_dev,safe_ino)==(udec(CERT[b"SAFE_BIND_DEV"],1),udec(CERT[b"SAFE_BIND_INO"],1)))
 final_context(safe_dev,safe_ino);scrub_exact({0,3,4,5,6,7,8,9,100})
 cert_live(CERT,283472000000)
 return control,cert_raw,envelope_raw,source_raw

def minimal_context(attempt):
 return {b"attempt":attempt,b"intent_durable":False,b"committed":[False]*15,b"entered":0,b"direct_reaps":0,b"kill_count":0,b"kill_returned":False,b"kill_unknown":False,b"last_out_eof":False,b"last_err_eof":False,b"cgfd":-1,b"root_events_fd":-1,b"root_kill_fd":-1,b"events_fd":-1,b"kill_fd":-1,b"out_fd":-1,b"err_fd":-1,b"outer_pidfd":-1}

def main():
 control,cert_raw,envelope_raw,source_raw=static_inputs();consumed=False;context=None
 try:
  send_exact(control,b"READY\n")
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+10000000000,0);need(fds==())
  if raw==b"REFUSE\n":return
  need(raw==b"CONSUME_BEGIN\n");cert_live(CERT,283472000000);send_exact(control,b"CONSUME_ARMED\n")
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+100000000,0);need(fds==() and raw==b"CONSUME_COMMIT\n")
  consumed=True;attempt=consume_attempt(AUTH,CERT,cert_raw,envelope_raw,source_raw);cert_live(CERT,283472000000)
  context={b"attempt":attempt,b"intent_durable":True,b"committed":[False]*15,b"entered":0,b"direct_reaps":0,b"kill_count":0,b"kill_returned":False,b"kill_unknown":False,b"last_out_eof":False,b"last_err_eof":False,b"cgfd":-1,b"root_events_fd":-1,b"root_kill_fd":-1,b"events_fd":-1,b"kill_fd":-1,b"out_fd":-1,b"err_fd":-1,b"outer_pidfd":-1}
  send_exact(control,b"CONSUMED_DURABLE\n")
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+10000000000,0);need(fds==())
  stage=parse_packet(raw,b"STAGE_DURABLE",(b"safe_dev",b"safe_ino"))
  need(udec(stage[b"safe_dev"],1)>0 and udec(stage[b"safe_ino"],1)>0);cert_live(CERT,15*TOTAL_NS+REPORT_NS);send_exact(control,b"STAGE_ACK\n")
  containment_bind(control,context)
  for ordinal,probe in enumerate(PROBES):
   context[b"entered"]=ordinal+1;cert_live(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS)
   try:
    stream_arm(control,context,ordinal,probe)
    pidfd_arm(control,context,ordinal,probe)
    release_phase(control,context,ordinal,probe)
    actor_lost,faults,empty,stdout,stderr,out_eof,err_eof=monitor_probe(control,context,ordinal,probe)
    if actor_lost:
     faults.add(b"ACTOR_LOST");terminal_failure(control,context,probe,faults,True);return
    if faults:
     if not context[b"abort_received"]:
      try:
       raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0);need(fds==())
       abort=parse_packet(raw,b"ABORT",(b"ordinal",b"probe",b"fault"));need(udec(abort[b"ordinal"],0,14)==ordinal and abort[b"probe"]==probe and abort[b"fault"] in FAULT_ORDER);faults.add(abort[b"fault"])
      except ActorLost:faults.add(b"ACTOR_LOST")
     terminal_failure(control,context,probe,faults,b"ACTOR_LOST" in faults);return
    new_faults,committed=validated_exchange(control,context,ordinal,probe,stdout,stderr)
    if not committed:
     terminal_failure(control,context,probe,new_faults,False);return
    close_probe(context);cert_live(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS)
   except ActorLost:
    terminal_failure(control,context,probe,{b"ACTOR_LOST"},True);return
   except CertificateExpired:
    terminal_failure(control,context,probe,{b"CERTIFICATE_EXPIRED"},False);return
   except BaseException:
    terminal_failure(control,context,probe,{b"CONTROL_PACKET"},False);return
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0);need(fds==() and raw==b"EMPTY_FINAL_QUERY\n")
  cert_live(CERT,REPORT_NS);need(not populated(context[b"root_events_fd"]));send_exact(control,b"EMPTY_FINAL_CONFIRMED\n")
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0);need(fds==() and raw==b"CGROUP_REMOVED\n")
  try:os.stat(AUTH,dir_fd=6,follow_symlinks=False);need(False)
  except FileNotFoundError:pass
  cert_live(CERT,REPORT_NS);send_exact(control,b"REMOVE_ACK\n")
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0);need(fds==() and raw==b"FINALIZE_PASS\n")
  empty,disp=report(context,b"NONE",set(),True);need(empty and disp==b"PASS")
  send_exact(control,b"TERMINAL_DURABLE\n")
  raw,fds=recv_monitored(control,4,time.monotonic_ns()+ACK_NS,0);need(fds==() and raw==b"TERMINAL_SEEN\n")
 except ActorLost:
  if consumed and context is None and RECOVERY_ATTEMPT>=0:context=minimal_context(RECOVERY_ATTEMPT)
  if consumed and context is not None:terminal_failure(control,context,b"NONE",{b"ACTOR_LOST"},True)
 except CertificateExpired:
  if consumed and context is None and RECOVERY_ATTEMPT>=0:context=minimal_context(RECOVERY_ATTEMPT)
  if consumed and context is not None:
   try:terminal_failure(control,context,b"NONE",{b"CERTIFICATE_EXPIRED"},False)
   except BaseException:pass
 except BaseException:
  if consumed and context is None and RECOVERY_ATTEMPT>=0:context=minimal_context(RECOVERY_ATTEMPT)
  if consumed and context is not None:
   fault=b"INTENT_DURABILITY_UNKNOWN" if not context[b"intent_durable"] else b"CONTROL_PACKET"
   try:terminal_failure(control,context,b"NONE",{fault},False)
   except BaseException:pass
 finally:
  if context is not None:
   close_probe(context)
   for key in (b"root_events_fd",b"root_kill_fd",b"cgfd",b"attempt"):
    number=context.get(key,-1)
    if number>=0:
     try:os.close(number)
     except OSError:pass
  try:control.close()
  except BaseException:pass

try:
 main()
except BaseException:
 raise SystemExit(96)
raise SystemExit(0)
P27 RUNNER V2 WATCHDOG SOURCE END F53E709A

## 16. Frozen literal identities and delimiter census

A literal span is every byte after its BEGIN delimiter LF and before the
first byte of its END delimiter. Thus the final source LF is included and
neither delimiter is included. Raw line extraction, wc, and sha256sum only
gave:

record                 absolute lines  bytes  LF   SHA256
A actor including C    848-1761        61068  914  bd13e59aa41acba50792e9321399dab99d094b2f388371df9734e2d4013097b4
C embedded validator   1295-1392       9944   98   9acf06ee9e4594dd6d39223eb3e0e54a17ed0c569ebd646a168d5b82baf22462
B continuous watchdog  1765-2414       40827  650  2d2d232d34c62ee20701a9eee17a153d4553e8b927fef80c6e273c654d4f45fb

Each of the six exact delimiter lines occurs once: A BEGIN/END, embedded C
BEGIN/END, and B BEGIN/END. C is a uniquely delimited contiguous subspan of
A and is therefore separately identifiable without a fourth external
program. A reconstructs its A and B delimiter strings from fragments, so no
complete delimiter is duplicated inside a literal.

These identities are normative. Any byte, LF, delimiter, line location, or
hash mismatch closes preflight as INPUT_AUTH. No later process may normalize
line endings, strip comments, indent, format, patch, or regenerate a source.

## 17. Branch, callsite, FSM, and authority census

The actor FSM has exactly 34 named states: A00 through A31, R00_REFUSED, and
T00_TERMINAL. The watchdog FSM has exactly 27 named states: B00 through B15
and B80 through B90. The fault-precedence tuple has exactly 25 members. A's
explicit CRASH_FAULT map has exactly 19 phase keys; CertificateExpired is the
one typed override and is not a twentieth phase.

Raw callsite census inside A is:

operation                         callsites
fork B                            1
raw clone3 OUTER                  1
execve B/OUTER                    2
central direct waitpid            1
payload SIGCONT                   1
payload pre-exec SIGSTOP          1
stage/cgroup mkdir                2
SCM_RIGHTS send helper            1
SCM_RIGHTS sends                  3

Raw callsite census inside B is:

operation                         callsites
fork/clone/exec/wait/SIGCONT      0
consumption mkdir                 1
O_CREAT|O_EXCL durable helper     1
durable-helper callers            7
recvmsg ancillary intake          1
direct cgroup.kill os.write       1
kill retry or second kill         0

The seven B durable callers are recovery/preintent, intent, release,
validated receipt, ACK-intent receipt, kill ticket, and final report. The
one direct kill call is textually os.write(number,b"1\n"); no write_all
path reaches cgroup.kill. A has no attempt-directory FD and no attempt
durable writer. B has no stage-base FD, source extractor, transcript parser,
clone, release, or direct-wait authority.

The exact authority partition is:

authority                       sole owner
E0365/V15/source authentication A, with independent B contract recheck
entry privilege observation     A
final child credential check    each child and B
one-shot consumption/intent     B
V15 extraction/staging          A
atomic clone3                   A
stopped/direct-member wait      A
dynamic FD/type/pidfd recheck   B
release record durability       B
SIGCONT                         A
raw capture/overflow/empty      B
OUTER direct wait               A
transcript C semantics          A
validated/ACK-intent receipts   B
one kill and retained monitor   B
terminal report                 B
B direct wait                   A

There is no shared or fallback authority. In particular, B cannot reap
OUTER after A loss, A cannot author a report, and neither process can
substitute a PID/PGID action for cgroup.kill.

## 18. Exact source-to-prose consistency matrix

requirement                 literal locus
whole input identities      A exact_whole/main; B whole_ledger/static_inputs
AUTH/envelope/certificate   A parse_envelope/parse_cert/main; B contract/envelope
fixed absolute lifetime     both cert_live and clock-binding paths
entry/final credentials     A verify_creds/child_context; B final_context
complete FD scrub           A/B scrub_exact after close_range mappings
collision-safe B mapping    A preserved_map and launch_b
B pre-effect READY          A main and B main consume handshake
B-owned intent              B consume_attempt/attempt_intent
raw V15 spans/equality      A v15_sources
four staged leaves          A stage_leaf and main staging block
P01C thirteen fields        A derive_p01c/source_argv
serial fifteen-slot loop    A main enumerate(SUITE); B main enumerate(PROBES)
preclone drain authority    A STREAM_ARM; B stream_arm
stopped/member/pidfd bind   A run_probe; B pidfd_arm
release deadline authority  A run_probe call_entry; B release_phase
direct wait                 A wait_status/run_probe only
concurrent bounded capture  B monitor_probe/drain
fixed ten-key result        A recv_result; B send_result
strict transcript grammar   embedded C validate_transcript
P00 exact SHA               embedded C validate_probe P00
P05 legal PID reuse         embedded C validate_probe P05
topology non-reconstruction embedded C child_observation and B receipt
monotone durable receipts   B validated_record/ack_intent_record
one nonretry kill           B kill_once
actor-loss containment      B terminal_failure/passive_until_empty
recovery grammar            B recovery_record
final report grammar        B report
no real clone3 test now     certificate gate plus section 14

P01C element index 9 is explicitly decoded hex-to-bytes, decoded as strict
ASCII, re-encoded to identical bytes, and re-encoded to identical lowercase
hex. P00's synthetic bytes are exactly authenticated CHILD plus "\n#" plus
the required x padding to 251414 bytes, and both possible metadata
partitions are compared with the recomputed SHA. P05 accepts numeric reuse
while requiring ordered statuses 5888 and 15 and their ordered child
observations.

The issuer's signature validity and complete envelope bytes are authenticated
by independent prebind authority. A and B only digest/reparse the supplied
sealed bytes; neither claims to establish issuer trust. The certificate is
an externally issued premise, never a self-certificate.

## 19. Immutable effects, formal review scopes, and author stop

The future non-build effect list in section 14 is exhaustive. B remains
outside cgroup/AUTH_ID from READY through report file fsync, same-FD reread,
attempt-dir fsync, post-report certificate sample, TERMINAL_DURABLE, and
TERMINAL_SEEN. On retained populated state it remains longer, observing
until empty without another kill. The certificate premise that B survives
both its own cgroup.kill call and kill-to-empty progress is mandatory.

The certificate subcaps are mechanical, not additive surprises:
CONSUMPTION_PROGRESS_NS=100000000 is contained within the
PRECONSUMPTION_CAP_NS=10000000000; RELEASE_PROGRESS_NS=1000000000 is the
fixed launch component of each slot; SIGCONT_CALL_RETURN_NS=5000000 and
DURABLE_RECORD_PROGRESS_NS=100000000 are reservations within that slot;
FINAL_REPORT_PROGRESS_NS=1000000000 is the final term. Therefore
15*18164800000+10000000000+1000000000 is exactly 283472000000 at
consumption, and adding the entry preconsumption cap gives exactly
293472000000 at actor entry.

H41 is a future independent static lifecycle/containment review. Its exact
scope is authority partition, one-shot boundary, capability transition,
static/dynamic FD graph, actor-loss coverage, cgroup2 mount/type/controllers/
subtree-control, stopped/member/pidfd binding, one-kill semantics, direct
wait limitations, deadlines/lifetime, durable ordering, effects/access
denial, crash matrix, FSM, and callsite census.

H42 is a different future independent static source/parser review. Its exact
scope is raw identities/delimiters, source-to-prose equality, certificate and
packet grammars, exact argv/environment, all transcript row vectors and
dynamic cross-checks, P00/P01C/P05 fixes, topology limitation, receipt/report
grammars, complete fault precedence, and forbidden branch absence.

The V2 author and every E0365 prebind advisor are disqualified from H41 and
H42. H41 and H42 must be performed by separated reviewers and both must
independently return formal static PASS. Even dual static PASS opens only a
separately reviewed synthetic no-build clone3/CPython gate. It does not open
the real V15 suite, create a manifest, authorize a microtest, or grant
execution, build, evidence, PDF, or release authority.

During this authorship the only write was this V2 path through apply_patch.
No literal was imported, tokenized as a language, AST-parsed, compiled,
evaluated, executed, launched, microtested, or sent to a validator process.
Only exact raw byte/line identity tools were used. V1, the ledger, V15, V8,
manifest, Binder, actor, derivation, every other paper/note, and all
build/evidence roots were not written. No build/evidence root was listed, stated, opened,
traversed, touched, or otherwise accessed. No temporary, cache, log,
redirect, or auxiliary file was made.

This terminal declares only completion of inert static authorship. It does
not declare prebind PASS, formal-review PASS, synthetic-gate PASS, runtime
correctness, execution readiness, or payload success.

BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V2_AUTHOR_STOP
