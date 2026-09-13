# Paper 27 E001 supervisor Host runtime plan recovery V1

Status: E0364-authorized inert runner-plan author control; execution count is
zero.

This control closes all six E0364 preconditions. It freezes one external
one-shot actor, one recovery-only watchdog/reporter, and a structurally
delimited complete transcript validator inside the actor. All literal source
records are inert bytes. This authorship does not import, tokenize as a
language, AST-parse, compile, evaluate, execute, launch, microtest, or
validator-process any literal.

## 1. Frozen authority and immutable inputs

The only authorizing ledger entry is E0364 in the exact regular file
/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md:

dev=2431
ino=12439253869
mode=0644
nlink=1
uid=0
gid=0
bytes=2275332
LF=23473
SHA256=5b5d8b8f6ded4b20cfd06aeac42df4a41b72a0d7e53dfbd24b9a2bf805575efb
terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNTIME_PLAN_PRECONDITION_FAIL_AND_RUNNER_V1_AUTHOR_OPEN_NO_EXECUTION

The exact frozen Host V15 is:

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

Host V8 was consulted only for exact row order and value semantics:

path=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V8.md
bytes=74973
LF=1071
SHA256=72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf

The five V15 source spans, defined as the bytes strictly between their unique
BEGIN and END delimiter lines, including the last source LF, are immutable:

source  bytes  LF    SHA256
OUTER   87151  1840  cfa1d88b312b7f4425778018be39cf7628568c9ddb39c697ff12b8b0f1c8be1a
KEEPER   4216   128  e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716
LAUNCHER 4218   128  e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5
MARKER  75094  1479  b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d
CHILD   19746   452  1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf

The embedded CHILD bytes inside MARKER must be raw-equal to the standalone
CHILD span. Actor V3 and derivation V6 were not accessed for this authorship,
are negative historical controls only, and supply no execution authority.
The ledger, V15, V8, actor V3, derivation V6, manifest, Binder, validator,
fixture, all build/evidence roots, and every paper or release object are
immutable.

## 2. Authority result and six precondition closures

This is a plan, not an execution grant. A later event requires both fresh
formal static reviews, supervisor prebinding, a separately issued premise
certificate, and a new explicit execution authorization.

E0364 blocker                                                   V1 closure
NO_FROZEN_EXTERNAL_CALLER_OR_TRANSCRIPT_VALIDATOR               literal A fixes raw extraction, staging, launch, capture, direct wait, validation, ACK, and receipts; its separately delimited C span is the complete validator
TOP_PID_OR_OUTER_PROCESS_GROUP_TIMEOUT_CAN_STRAND_GROUP_G        one exclusive cgroup-v2 subtree contains OUTER and all descendants before release; literal B is outside and owns the only ticketed cgroup.kill lane; no PID or PGID fallback exists
AUTHENTICATED_V15_EXECUTION_DOMAIN_PREMISES_UNBOUND              the independent sealed certificate grammar in section 6 binds every 5m/2m/20m/100m/100m/no-async/owner-survival/500m premise to the exact attempt
EXTERNAL_EXECUTABLE_AND_LAUNCH_CONTEXT_PINNING_UNBOUND           certificate dependency closure plus exact flags, environment, cwd, descriptors, close_range scrub, signals, timers, hooks, rlimits, credentials, capabilities, runtime root, and no-mutator lifetime are mandatory
DURABLE_ONE_SHOT_ATTEMPT_AND_UNKNOWN_EFFECT_STATE_UNBOUND        an exclusive consumed=1 intent and directory fsync precede staging and every release; an unknown effect is permanently CONSUMED_INDETERMINATE
ZERO_WRITE_SCOPE_AMBIGUITY                                      authoring and reviews are zero-write; section 14 enumerates the exact later non-build write set

No observation during a run may manufacture or refresh a premise. No one of
text PASS, exit zero, EOF, ESRCH, elapsed time, signal return, physical exit,
pidfd readiness, cgroup emptiness, or ACK is sufficient by itself.

## 3. Exact suite, budgets, and stopping rule

SUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
SUITE_CARDINALITY=15
AUTHORIZED_INVOCATION_SLOTS=15
OPERATIONAL_BUDGET_NS=15000000000
ACTOR_LAUNCH_PROGRESS_NS=1000000000
POST_OPERATION_HOST_BOUND_NS=1664800000
ACTOR_ACK_PROGRESS_NS=500000000
RELEASE_THROUGH_ACK_CAP_NS=18164800000
CONTAINMENT_CLEANUP_CAP_NS=2000000000
STDOUT_CAP_BYTES=3145728
STDERR_CAP_BYTES=3145728

Exactly one serial pass through SUITE is possible. A slot is entered once.
The first FAIL or INDETERMINATE permanently stops the suite. There is no
retry, resume, continue, repair, skip, replacement slot, second suite, or
cleanup-to-PASS transition. The separately timed 2000000000-ns containment
cleanup begins only after a sticky failure selection and cannot restore PASS.

For an entered probe, release_origin is sampled before literal B arms its
watchdog and before SIGCONT. The actor requires:

release_origin < release_return <= release_origin+1000000000
host_complete <= release_origin+17664800000
ack_durable <= release_origin+18164800000
ack_durable-host_complete <= 500000000

The 17664800000 host cap is 1000000000+15000000000+1664800000. The final cap
adds exactly 500000000. A late sample or arithmetic ambiguity is sticky; no
horizon is restarted or extended.

## 4. AUTH_ID, nonce, durable one-shot, and retained disposition

The later execution event supplies exactly one AUTH_ID consisting of 64
lowercase hexadecimal digits. AUTH_ID is the SHA-256 of the complete sealed
premise-certificate bytes. This content-addressed rule is the stronger
one-to-one derivation selected here. NONCE is exactly AUTH_ID, with no hash,
prefix, truncation, random supplement, or alternate representation.

Before attempt consumption, literal A authenticates every input, the
certificate, current boot/platform, service-base and mount identities,
cgroup-v2 availability, complete dependency closure, no-mutator lifetime,
runtime-root bindings, absence of every AUTH_ID child, and its own launch
context. Per-attempt target/a/b checks necessarily follow exclusive safe
directory creation and therefore follow consumption. Failure before the
first exclusive attempt-directory creation is REFUSED_NOT_CONSUMED and makes
no stage, containment, or attempt leaf.

The preexisting durable base is /var/lib/p27-e001-host-v15/attempts, a
root-owned uid/gid 0 mode 0700 directory whose parent chain is root-owned and
not group/world writable. Literal A creates exactly one
AUTH_ID child with mkdirat mode 0700 and O_NOFOLLOW held-component
verification. EEXIST is permanent refusal; the directory is never reused. It
then creates intent.v1 with O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, mode 0400,
writes the exact grammar below, fsyncs the leaf, verifies
regular/root-owned/link1/mode0400, fsyncs the AUTH_ID directory, and fsyncs
the attempts base. Only after all three fsyncs is consumed=1 committed.

P27E001_ATTEMPT_INTENT_V1
AUTH_ID=H64
CERT_SHA256=H64
PLAN_SHA256=H64
RUNNER_SHA256=H64
RECOVERY_SHA256=H64
E0364_SHA256=5b5d8b8f6ded4b20cfd06aeac42df4a41b72a0d7e53dfbd24b9a2bf805575efb
V15_SHA256=a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845
V8_SHA256=72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf
SUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
NONCE=H64
CGROUP_PATH_HEX=LOWER_EVEN_HEX
SAFE_PATH_HEX=LOWER_EVEN_HEX
CONSUMED=1
RETRY_ALLOWED=0
RELEASE_COUNT_AT_INTENT=0
INTENT_END=1

Every line is strict ASCII and LF, values are canonical, the order is exact,
and the file ends after INTENT_END=1 LF. H64 at AUTH_ID, CERT_SHA256, and
NONCE is the same value.

For each probe, membership proof and a durable exclusive release-PROBE.v1
record precede SIGCONT. That record binds AUTH_ID, probe ordinal, OUTER PID,
cgroup dev/ino, safe dev/ino, all source identities through the canonical
argv SHA-256, the environment SHA-256, and RELEASE_AUTHORIZED=1. It does not
claim release occurred. After
it is fsynced with the attempt directory, any lost SIGCONT return or actor
loss is an unknown effect and therefore CONSUMED_INDETERMINATE.

Its exact grammar is:

P27E001_RELEASE_V1
AUTH_ID=H64
ORDINAL=UDEC
PROBE=Q
OUTER_PID=UDEC
CGROUP_DEV=UDEC
CGROUP_INO=UDEC
SAFE_DEV=UDEC
SAFE_INO=UDEC
ARGV_SHA256=H64
ENV_SHA256=H64
RELEASE_AUTHORIZED=1
RELEASE_END=1

No consumed path deletes, truncates, renames, replaces, clears, or reuses the
attempt directory, stage directory, intent, release records, receipts,
report, kill ticket, or recovery report. Success removes only the empty
cgroup directory; FAIL or INDETERMINATE retains it. On PASS the empty cgroup
is removed and ENOENT is proved before the final PASS report is committed.
The stage and durable records remain.

## 5. Concrete cgroup-v2 whole-tree containment

The selected mechanism is Linux cgroup v2. No bare-PID, PID-list, session,
process-group, guessed-PGID, killpg, or ancestor-group fallback exists.

Preexisting base:
/sys/fs/cgroup/p27-e001-host-v15

Exclusive attempt subtree:
/sys/fs/cgroup/p27-e001-host-v15/AUTH_ID

The independent certificate binds one unified cgroup2 mount, mount ID,
filesystem magic 0x63677270, base dev/ino/uid/gid/mode, cgroup.type=domain,
cgroup.controllers bytes, writable cgroup.procs, readable cgroup.events, and
writable cgroup.kill. It attests no delegator or mutator can add, move, fork,
freeze, remove, or alter membership or files from preflight through final
ACK. Availability is a separately bound pre-execution premise and is not
tested during this authorship.

Literal A creates the AUTH_ID subtree exclusively, opens it by held dirfd,
and requires cgroup.events exactly contain populated 0 before the first
release and between probes. It creates no descendant cgroup. The actor and B
must both be outside this subtree. For each probe A invokes the x86_64 clone3
syscall once with exactly CLONE_INTO_CGROUP|CLONE_PIDFD, SIGCHLD, and the held
attempt cgroup FD. The resulting OUTER is A's direct child, is born inside the
attempt cgroup, and yields an exact pidfd atomically; there is no fork-to-move
window. Before normalization or exec, the child executes its only
pre-release action: SIGSTOP to itself. A arms B with that pidfd and the fixed
launch origin, bounded-waits with waitpid(child,WNOHANG|WUNTRACED), requires
the exact stopped status, rereads cgroup.procs as exactly canonical PID LF,
requires cgroup.events populated 1, durably commits the release record, and
only then performs the sole SIGCONT release. There is no child-created
descendant before atomic membership. Any pre-release fault closes control;
B then owns the same one kill-to-empty lane, while A bounded-direct-waits.

A remains the direct OUTER parent. In the ordinary lane only A calls exact
waitpid(OUTER_PID,0), retains the raw status, and requires exit zero. B is a
non-parent. It never calls waitpid or waitid and never claims physical reap.
It uses pidfd readiness only as a liveness observation and cgroup.events
populated 0 only as the whole-tree empty proof.

B owns the only cgroup-wide kill authority. Before its one possible write it
durably creates kill-ticket.v1 with O_EXCL and fsyncs it and the attempt
directory. Only the process that successfully creates the ticket may write
exactly 1 LF to cgroup.kill, exactly once. An existing ticket prohibits a
second write. Crash after ticket commit but before or during the kill write
is an unknown effect; recovery must not issue another kill and reports
CONSUMED_INDETERMINATE. After a kill selection B continues concurrent stream
drain, pidfd observation, and cgroup.events polling until populated 0 or the
independent 2000000000-ns cleanup deadline. Empty proof or cleanup cannot
erase the original failure.

The ticket is exactly:

P27E001_KILL_TICKET_V1
AUTH_ID=H64
PROBE=Q
PRIMARY=TOKEN
KILL_AUTHORITY=1
KILL_COUNT_BEFORE=0
TICKET_END=1

If A is alive, PASS requires its direct exact wait plus B's timely empty
proof. If A is lost, B may drain, use its one ticketed kill lane, observe
pidfd readiness, and prove cgroup empty, but direct reap is unavailable.
Every such path is permanently CONSUMED_INDETERMINATE. B writes
DIRECT_REAP=UNAVAILABLE and never PASS. On full suite PASS A closes cgroup
FDs, rmdirats the exact empty AUTH_ID subtree, verifies ENOENT, and only then
commits the final PASS report. On any
other outcome it retains the subtree for recovery/audit.

## 6. Exact independent premise-certificate grammar

The certificate is created and authorized by the separately designated
P27_HOST_PREMISE_ISSUER_V1. That issuer must be independent of the runner,
recovery reporter, plan author, H41, and H42. The supervisor verifies the
issuer's authorization envelope before sealing the exact certificate bytes
into actor fd104 with exactly F_SEAL_WRITE, F_SEAL_GROW, F_SEAL_SHRINK, and
F_SEAL_SEAL. Neither literal contains a certificate-generation, signing, or
self-approval path.

The certificate is strict 7-bit ASCII/LF with no blank line. Fixed fields
occur exactly in the following order. DEP_COUNT is canonical decimal in
1..256 and is followed by exactly that many DEP rows with contiguous
zero-padded four-digit indices. Each path is lowercase even hex decoding to
an absolute NUL-free byte path. Identity is canonical
dev,ino,mode,nlink,uid,gid,bytes,sha256. MODE is full canonical octal.

P27E001_PREMISE_CERTIFICATE_V1
ISSUER_ID=P27_HOST_PREMISE_ISSUER_V1
ISSUER_AUTHORIZATION_SHA256=H64
BOOT_ID_SHA256=H64
PLATFORM_ID_SHA256=H64
ARCH=x86_64
KERNEL_RELEASE_HEX=LOWER_EVEN_HEX
CGROUP2_MOUNT_ID=UDEC
RUNTIME_ROOT_MOUNT_ID=UDEC
NOT_BEFORE_REALTIME_NS=UDEC
NOT_AFTER_REALTIME_NS=UDEC
MIN_REMAINING_AT_CONSUMPTION_NS=283472000000
AUTH_BINDING=SHA256_OF_COMPLETE_CERTIFICATE_BYTES
PLAN_SHA256=H64
RUNNER_SHA256=H64
RECOVERY_SHA256=H64
E0364_SHA256=5b5d8b8f6ded4b20cfd06aeac42df4a41b72a0d7e53dfbd24b9a2bf805575efb
V15_SHA256=a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845
V8_SHA256=72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf
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
RUNTIME_ROOT_DEV=UDEC
RUNTIME_ROOT_INO=UDEC
SAFE_BIND_DEV=UDEC
SAFE_BIND_INO=UDEC
CGROUP_BASE_DEV=UDEC
CGROUP_BASE_INO=UDEC
RLIMIT_AS=INFINITY,INFINITY
RLIMIT_CORE=0,0
RLIMIT_CPU=INFINITY,INFINITY
RLIMIT_DATA=INFINITY,INFINITY
RLIMIT_FSIZE=INFINITY,INFINITY
RLIMIT_MEMLOCK=8388608,8388608
RLIMIT_MSGQUEUE=819200,819200
RLIMIT_NICE=0,0
RLIMIT_NOFILE=1048576,1048576
RLIMIT_NPROC=1048576,1048576
RLIMIT_RSS=INFINITY,INFINITY
RLIMIT_RTPRIO=0,0
RLIMIT_RTTIME=INFINITY,INFINITY
RLIMIT_SIGPENDING=515199,515199
RLIMIT_STACK=8388608,INFINITY
CREDENTIAL_VECTOR=UID0_GID0_RESUID0_RESGID0_GROUPS_EMPTY_UMASK0077_CAPS_EMPTY_NNP1
FD_RETURN_COMMIT_PROGRESS_NS=5000000
CLOSE_RETURN_COMMIT_PROGRESS_NS=2000000
OWNER_CONTROL_PROGRESS_NS=20000000
KILL_REAP_PROGRESS_NS=100000000
TERMINAL_FRAMING_PROGRESS_NS=100000000
ACTOR_LAUNCH_PROGRESS_NS=1000000000
POST_OPERATION_HOST_BOUND_NS=1664800000
ACTOR_ACK_PROGRESS_NS=500000000
OPERATIONAL_BUDGET_NS=15000000000
CONTAINMENT_CLEANUP_CAP_NS=2000000000
COMMIT_WINDOW_TOKEN=NO_ASYNC_TRANSFER_THROUGH_FIXED_FD_PROCESS_WAIT_AND_CLOSE_COMMIT_V15
OWNER_SURVIVAL_TOKEN=OWNER_SURVIVAL_PROGRESS_SINGLE_FRAME_V15
NO_MUTATOR_TOKEN=ROOT_OWNED_0700_STABLE_NONCE_NO_CONCURRENT_MUTATOR_V15
NO_ASYNC_TRANSFER=1
NO_SIGNAL_DELIVERY=1
NO_TIMER_DELIVERY=1
NO_TRACE_PROFILE_AUDIT_HOOK=1
OWNER_SURVIVES_THROUGH_ACK=1
NO_CONCURRENT_MUTATOR=1
DEPENDENCY_CLOSURE_COMPLETE=1
RUNTIME_ROOT_WORKSPACE_ABSENT=1
BUILD_EVIDENCE_ROOT_UNREACHABLE=1
CGROUP_MEMBERSHIP_EXCLUSIVE=1
CLONE3_INTO_CGROUP_AVAILABLE=1
CGROUP_KILL_AVAILABLE=1
CGROUP_EVENTS_RELIABLE=1
CLOSE_RANGE_COMPLETE=1
FSYNC_DURABILITY_PREMISE=1
DEP_COUNT=UDEC
DEP[0000]=ROLE,PATH_HEX,DEV,INO,MODE,NLINK,UID,GID,BYTES,SHA256
...
DEP[NNNN]=ROLE,PATH_HEX,DEV,INO,MODE,NLINK,UID,GID,BYTES,SHA256
CERTIFICATE_END=1

ROLE is one of PYTHON_LINK, PYTHON_IMAGE, ENV_EXEC, BASH_EXEC,
DYNAMIC_LOADER, LIBC, PYTHON_STDLIB, PYTHON_EXTENSION, NSS_DEPENDENCY, or
RUNTIME_DEPENDENCY. Exactly one PYTHON_LINK, PYTHON_IMAGE, ENV_EXEC,
BASH_EXEC, DYNAMIC_LOADER, and LIBC row is required. All executable and
mapped dependency bytes reachable in actor, B, OUTER, KEEPER, LAUNCHER,
MARKER, CHILD, and the P12 env/bash/Python chain must appear. The issuer
attests closure completeness; the run may only open and rehash listed rows,
not discover or enlarge the closure.

The certificate binds successful FD return through fixed-cell commit within
5000000 ns; close entry through exact state commit within 2000000 ns; spawn
and exact-wait return through first mutation and all final
scans/framing/exit-entry owner control within 20000000 ns; selected live PID
through KILL/reap/raw commit within 100000000 ns; terminal framing within
100000000 ns; actor launch within 1000000000 ns; owner survival and ACK within
500000000 ns; and no asynchronous transfer, callback, signal-language
handler, KeyboardInterrupt, trace, profile, audit, timer, or mutator in any
protected window. It also binds cgroup, close_range, chroot, capability drop,
pidfd, pipe, poll, fsync, clock, fork, clone3 with CLONE_INTO_CGROUP and
CLONE_PIDFD, execve, and direct-wait semantics.

BOOT_ID_SHA256 hashes the exact current
/proc/sys/kernel/random/boot_id bytes including its LF. PLATFORM_ID_SHA256
hashes exactly `SYSNAME=... LF RELEASE=... LF VERSION=... LF MACHINE=... LF`
from uname, and KERNEL_RELEASE_HEX is the lowercase byte hex of the same
RELEASE value. CGROUP2_MOUNT_ID and RUNTIME_ROOT_MOUNT_ID are exact decimal
`mnt_id` values read through /proc/self/fdinfo for the already held base FDs.

Before consumption A requires certificate SHA equal AUTH_ID, exact four
seals, issuer envelope already authenticated by the supervisor, current
boot/platform equality, not-before satisfied, at least 283472000000 ns
remaining, every fixed field exact, and every dependency freshly held and
hashed under the certified no-mutator premise. Absence, staleness,
contradiction, duplicate key, unlisted dependency, incomplete closure,
changed byte, or lifetime shortfall is REFUSED_NOT_CONSUMED. Runtime
observations cannot cure it.

## 7. Exact launch context, runtime root, and descriptor transport

The execution event raw-extracts literal A and B from this exact plan using
their unique delimiter lines only. It does not import, tokenize, compile, or
evaluate them during extraction. It copies each raw span to a distinct
anonymous memfd created with MFD_CLOEXEC|MFD_ALLOW_SEALING, adds exactly the
four seals, verifies F_GET_SEALS equality, and rehashes from offset zero. It
supplies:

fd0 authenticated empty pipe read end, writer already closed
fd1 distinct raw actor status pipe
fd2 distinct raw actor diagnostic pipe
fd100 sealed literal A source
fd101 exact E0364 ledger file
fd102 exact V15 file
fd103 exact complete V1 plan file
fd104 sealed independent premise certificate
fd105 sealed literal B source

No other descriptor exists. Before its first effect A applies close_range to
3..99 and 106..UINT_MAX, preserving exactly 0,1,2,100,101,102,103,104,105.
The launch argv is exactly:

/root/miniconda3/bin/python3
-I
-S
-B
-P
-X
utf8
/proc/self/fd/100
RUN
AUTH_ID

Thus actor sys.argv is exactly three entries. Its environment is exactly the
same ten-key V15 environment and has no underscore or extra key:

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

The actor starts in a fresh session as its session and process-group leader,
outside the payload cgroup, with uid/gid/resuid/resgid 0, empty supplementary
groups, umask 077, no pending signals, all catchable signals default and
blocked during actor critical sections, all three interval timers zero, no
trace/profile/audit hook, and the exact certificate rlimit vector. Its
private mount namespace exposes only pinned service roots and opened input
FDs. The workspace hierarchy is absent.

The pinned full runtime root is
/var/lib/p27-e001-host-v15/runtime-root. It is a read-only, no-suid,
no-device mount snapshot containing the exact certificate dependency closure,
a read-only proc mount, and a bind of /tmp/p27-e001-host-v15 at the same
absolute path. It preserves:

/root/miniconda3/bin/python3
/root/miniconda3/bin/python3.12
/usr/bin/env
/usr/bin/bash
/proc/self/fd
/proc/self/exe
/proc/self/maps
/tmp/p27-e001-host-v15

It does not contain /root/autodl-tmp/symplectic_map or any build/evidence
root. A's B-child and OUTER-child chroot to this full root, reopen the safe
directory through held no-follow components, verify the same safe dev/ino,
fchdir there, set securebits NOROOT and NO_SETUID_FIXUP with both locks, drop
all capability sets, set no_new_privs, normalize context, map only fixed
descriptors, and close_range every other descriptor. These steps occur after
OUTER's SIGSTOP membership barrier and before exec. The full root preserves
all V15 absolute executable paths.

For OUTER, A creates one authenticated empty fd0 pipe, two distinct
O_CLOEXEC|O_NONBLOCK raw stdout/stderr pipes, and one anonymous OUTER memfd.
It writes exact OUTER bytes, adds exactly four seals, verifies seals and
identity, then maps input to fd0, stdout to fd1, stderr to fd2, and OUTER to
fd100. It executes fixed Python with -I -S -B -P -X utf8 and
/proc/self/fd/100. Complete close_range calls cover 3..99 and
101..UINT_MAX. OUTER receives fd100 and no other inherited descriptor.

OUTER sys.argv is the exact V15 canonical 20-entry vector, or 33 only for
P01C:

0 /proc/self/fd/100
1 PROBE
2 AUTH_ID
3 15000000000
4 5000000
5 2000000
6 20000000
7 100000000
8 100000000
9 500000000
10 NO_ASYNC_TRANSFER_THROUGH_FIXED_FD_PROCESS_WAIT_AND_CLOSE_COMMIT_V15
11 OWNER_SURVIVAL_PROGRESS_SINGLE_FRAME_V15
12 ROOT_OWNED_0700_STABLE_NONCE_NO_CONCURRENT_MUTATOR_V15
13 SAFE_DEV
14 SAFE_INO
15 OUTER_BYTES,OUTER_LF,OUTER_SHA256
16 KEEPER_BYTES,KEEPER_LF,KEEPER_SHA256
17 LAUNCHER_BYTES,LAUNCHER_LF,LAUNCHER_SHA256
18 MARKER_BYTES,MARKER_LF,MARKER_SHA256
19 CHILD_BYTES,CHILD_LF,CHILD_SHA256
20..32 exact P01C fields only for P01C

The environment is exactly the ten entries above. The held safe cwd is exact.
Signals, timers, hooks, rlimits, credentials, capabilities, and umask are
certificate-bound. A fresh empty pipe is used for every probe.

## 8. Raw extraction and exact staging

A authenticates E0364 and V15 as whole byte strings from offset zero,
including fstat, byte count, LF count, SHA-256, terminal LF, and unique final
nonempty terminal. It authenticates the plan against the certificate,
raw-extracts A and B by unique delimiters, and compares them to sealed fd100
and fd105. It performs no language operation on extracted source.

For each V15 source it requires exactly one BEGIN and END delimiter, correct
order, and extracts only intervening bytes. It verifies all five triples. It
raw-extracts CHILD_SOURCE from MARKER using unique byte delimiters and
requires raw equality with standalone CHILD.

The preexisting /tmp/p27-e001-host-v15 base is root-owned uid/gid 0 and not
group/world writable, opened through held no-follow component FDs. After
durable consumption A creates exactly its AUTH_ID child with mkdirat mode
0700, exclusively and without reuse. It verifies stable held dev/ino.
target, a, and b must initially be absent.

Exactly four staged leaf writes are possible: keeper.py, launcher.py,
marker.py, child.py. Each is a held-dirfd
O_RDWR|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC write with mode0400, exact
write-all, fsync, same-FD rewind/read, fstat regular/root-owned/link1/mode0400,
rewind/read/hash/count equality, and final directory fsync. No outer.py
pathname exists. OUTER is only a sealed anonymous memfd. No enumeration,
absolute source reopen, actor cleanup, reuse, or repair exists.

## 9. P01D to P01C provenance

P01C is unreachable until same-suite P01D passes the complete validator and
its durable receipt ACK commits. A retains only that accepted row map.
Immediately before P01C it decodes accepted libc path/confstr with canonical
round trips, freshly opens exact libc and Python through held runtime-root
no-follow paths, fstats and hashes them, and checks accepted P01D and
certificate equality under the no-mutator premise.

The exact 13 fields are:

0 accepted libc_path_hex after fresh equality
1 fresh held libc st_dev
2 fresh held libc st_ino
3 fresh held libc full st_mode canonical octal
4 fresh held libc st_nlink
5 fresh held libc st_uid
6 fresh held libc st_gid
7 fresh held libc st_size
8 accepted libc_sha256 after fresh equality
9 accepted libc_confstr_hex after fresh equality
10 accepted python_image_dev after fresh equality
11 accepted python_image_ino after fresh equality
12 accepted python_image_sha256 after fresh equality

No prose literal, certificate-only substitute, prior suite, prior attempt,
guess, pathname stat, or unheld observation supplies a field.

## 10. Capture, watchdog, direct wait, and ACK

For each probe A launches a fresh B outside the cgroup. B's fixed FDs are:

fd0 empty input
fd1 and fd2 closed diagnostic sinks
fd3 OUTER stdout read
fd4 OUTER stderr read
fd5 cgroup.events read
fd6 cgroup.kill write
fd7 A/B SOCK_SEQPACKET control
fd8 held attempt directory
fd9 actor pidfd
fd100 sealed literal B

B's sys.argv entries are exactly /proc/self/fd/100,WATCH,AUTH_ID,PROBE,
18164800000,2000000000,3145728,3145728,ORDINAL,RECOVERY_SHA256,
RELEASE_ORIGIN_NS. It uses fixed flags and the ten-key environment. B applies
the independent RELEASE_ORIGIN_NS+1000000000 arm deadline even if A remains
alive but never supplies a complete ARM packet.

B sends READY. A atomically clone3-creates stopped OUTER in the cgroup,
passes the returned OUTER pidfd over fd7, sends ARM with PID/release_origin,
receives ARMED, proves stop and membership, commits release, and only then
SIGCONT releases. B concurrently nonblockingly drains
distinct fd3/fd4 through EOF while polling actor pidfd, OUTER pidfd, control,
cgroup.events, and deadline. There is no PTY, shell, merge, tee, temp output,
cache, log, or redirected capture.

Stdout retains 3145728 bytes; overflow is sticky and remaining bytes are
discarded while drain continues. Stderr has the same cap and successful
stderr is exactly empty. Overflow, actor loss, parser impossibility, exit, or
kill never stops drain.

A is the sole direct waiter. B returns a length-framed in-memory receipt only
after both EOFs and terminal cgroup empty or a sticky cleanup result. A parses
stdout only after complete capture. Host completion is the later of direct
wait and B completion. PASS stays provisional until receipt-PROBE.v1 and the
attempt directory are fsynced within both ACK bounds. Actor loss always
produces CONSUMED_INDETERMINATE; B cannot direct-wait or PASS.

## 11. Complete transcript language

The validator consumes complete stdout once from offset zero. It requires
1..3145728 bytes, strict bytes 0x20..0x7e plus LF only, no CR/NUL/HT/high
byte, final LF, no empty line, canonical encodings, and no unknown, duplicate,
missing, reordered, or malformed field.

For probe Q, line order is marker header, exact Q rows, marker footer, exactly
one candidate, and one unique terminal final line. Every row is
P27E001V15|probe=Q|KEY=VALUE. The common suffix keys are:

marker_image_dev,marker_image_ino,marker_image_sha256,probe_start_ns,probe_finish_ns,probe_elapsed_ns,probe_bound_ns,primary_failure,cleanup_failure,result

Probe prefixes are:

P00 source_item_bytes,source_item_accounted_bytes,broker_spawned,broker_payload_hex
P01D python_image_dev,python_image_ino,python_image_bytes,python_image_sha256,libc_confstr_hex,libc_path_hex,libc_bytes,libc_sha256,backend_surface,spawn_premise_satisfied
P01C libc_path_hex,libc_sha256,libc_confstr_hex,child_pids,child_statuses,child_raw_hex,spawn_premise_satisfied
P02 fds,environment_count,cwd_hex,flags
P03 soft_before,hard_before,soft_test,opened_fds,emfile
P04 valid_signal_count,default_signal_count,defaults_sha256,mask_empty
P05 wnohang_zero,eintr,echild,child_pids,raw_statuses,term_signal,broker_payload_hex
P06 monotonic,observed_min_delta_ns,start_ns,end_ns,deadline_checked
P07 empty_eagain,eof_before_last_writer,eof_after_last_writer
P08 child_pids,raw_statuses,same_session_group,post_pid_esrch,broker_payload_hex
P09 child_pids,raw_statuses,signal,reap_start_ns,reap_end_ns,reaped
P10 sample_count,pids,statuses,pid_duplicates,group_is_single_owned_launcher_group,reuse_proof
P11 open_result,atime_unchanged,cleanup_unlinked,cleanup_identity_observed,atomic_unlink_proof,scope_single_inode
P12 child_pids,raw_statuses,environment_count,underscore_absent,real_payload_invoked,broker_payload_hex
P13 file_fsync_returned,hardlink_noreplace_returned,inode_preserved,dir_fsync_returned,post_unlink_absent,cleanup_unlinked,durability_proof,rename_atomicity_proof

Candidate is exactly:
P27E001V15|outer=candidate|probe=Q|slots=4|all_reaped=1|role_statuses=launcher:S,keeper:S,marker:S,child:S|fatal=0|result=PASS

Terminal is exactly:
P27E001V15|outer=terminal|probe=Q|all_reaped=1|role_statuses=launcher:S,keeper:S,marker:S,child:S|frame_complete=1|fatal=0|result=PASS

Status strings are equal. Launcher/keeper are exact SIGTERM, marker exit zero,
and child is probe-specific last status or -1 where no child returned.

Common semantics require marker image identity equal certificate and constant
across suite; start<=finish; difference=elapsed; elapsed<=15000000000;
bound=15000000000; failures none; result PASS. P00 is 251414/251415 and exact
E2BIG-zero or INFO-one partition. P01D matches fresh Python/libc and
posix-posix_spawn/premise0. P01C matches same-suite P01D and one INFO
exit-zero/premise1. P02 has fds 0,1,2,5,6, env10, exact cwd and flags. P03 is
4096/1048576/64/59/1. P04 matches fresh counts/hash/mask1. P05 is 1/1/1, two
PIDs, exit23 then SIGTERM, signal15 and two ready observations. P06 has
monotonic1, positive delta, ordered times, deadline1. P07 is 1/0/1. P08 is
one zero BLOCK0, group1, ESRCH1. P09 is one SIGKILL, signal9, timestamps
within 100000000, reaped1. P10 has 16 PIDs, 16 zeros,
duplicates=16-cardinality(set), group1,reuse0. P11 is OK/1/1/1/0/1. P12 is
one zero CHAIN, env10, underscore1, payload0. P13 is 1/1/1/1/1/1/0/0.
Embedded child observations are fully decoded and cross-checked.

Validator PASS is one conjunct; final PASS additionally requires no sticky
fault, both EOFs, empty stderr, no overflow, direct OUTER exit0, exact
candidate/terminal, timely cgroup empty, and durable ACK.

## 12. Failure precedence and complete state machines

REFUSED_NOT_CONSUMED is unconsumed. CONSUMED_INDETERMINATE dominates
CONSUMED_FAIL. PASS is separate. Primary precedence is:

CERTIFICATE_OR_INPUT,INTENT_DURABILITY,RELEASE_EFFECT_UNKNOWN,ACTOR_LOST_OR_DIRECT_REAP_UNAVAILABLE,CONTAINMENT_NOT_EMPTY,WATCHDOG_DEADLINE,CAPTURE_OVERFLOW,STDERR_NONEMPTY,OUTER_STATUS,TRANSCRIPT_LANGUAGE,TRANSCRIPT_SEMANTICS,ACK_DURABILITY,REPORT_DURABILITY

Actor transitions:

A00_ENTRY->A01_PREFLIGHT or R00_REFUSED
A01_PREFLIGHT->A02_CONSUME or R00_REFUSED
A02_CONSUME->A03_STAGE or I00_INDETERMINATE
A03_STAGE->A04_CGROUP_EMPTY or F00_FAIL or I00_INDETERMINATE
A04_CGROUP_EMPTY->A05_PROBE_PREPARE
A05_PROBE_PREPARE->A06_B_READY or F00_FAIL or I00_INDETERMINATE
A06_B_READY->A07_ATOMIC_MEMBER_AND_PIDFD or F00_FAIL or I00_INDETERMINATE
A07_ATOMIC_MEMBER_AND_PIDFD->A08_B_ARMED or I00_INDETERMINATE
A08_B_ARMED->A09_STOP_AND_MEMBER_PROVED or I00_INDETERMINATE
A09_STOP_AND_MEMBER_PROVED->A10_RELEASE_RECORD or I00_INDETERMINATE
A10_RELEASE_RECORD->A11_RELEASED or I00_INDETERMINATE
A11_RELEASED->A12_DRAIN_AND_DIRECT_WAIT or F00_FAIL or I00_INDETERMINATE
A12_DRAIN_AND_DIRECT_WAIT->A13_VALIDATE or F00_FAIL or I00_INDETERMINATE
A13_VALIDATE->A14_ACK or F00_FAIL
A14_ACK->A15_NEXT or A16_REMOVE_EMPTY_CGROUP
A15_NEXT->A05_PROBE_PREPARE
A16_REMOVE_EMPTY_CGROUP->A17_FINAL_REPORT->P00_PASS

R00 is terminal. F00 and I00 go once through containment cleanup then failure
report and stop. No terminal reaches prepare, release, exec, or PASS.

B transitions:

B00_ENTRY->B01_CONTEXT->B02_READY->B03_ARMED->B04_DRAIN_MONITOR
B02_READY->B07_ACTOR_LOST on ARM deadline, EOF, or malformed control
B04_DRAIN_MONITOR->B05_ORDINARY_COMPLETE
B04_DRAIN_MONITOR->B06_STICKY_FAILURE or B07_ACTOR_LOST
B06_STICKY_FAILURE->B08_TICKET
B07_ACTOR_LOST->B08_TICKET
B08_TICKET->B09_KILL_ONCE if ticket created
B08_TICKET->B10_UNKNOWN_KILL_EFFECT if ticket exists
B09_KILL_ONCE->B11_DRAIN_EMPTY
B10_UNKNOWN_KILL_EFFECT->B11_DRAIN_EMPTY
B11_DRAIN_EMPTY->B12_RECOVERY_REPORT->B15_STOP
B05_ORDINARY_COMPLETE->B13_MEMORY_RECEIPT->B14_WAIT_DURABLE_ACK
B14_WAIT_DURABLE_ACK->B15_STOP on ACKED
B14_WAIT_DURABLE_ACK->B12_RECOVERY_REPORT on actor loss or ACK deadline
B14_WAIT_DURABLE_ACK->B15_STOP on explicit FAIL

B has no extraction, staging, safe mkdir, SIGCONT, release, fork, exec, retry,
resume, repair, semantic PASS, or suite continuation state.

## 13. Receipt and final report grammars

B memory packet has this strict line, exactly stdout bytes, exactly stderr
bytes, then P27B1_END LF:

P27B1|probe=Q|fault=TOKEN|stdout_len=UDEC|stderr_len=UDEC|stdout_eof=B|stderr_eof=B|cgroup_empty=B|kill_issued=B|pidfd_ready=B|done_ns=UDEC

TOKEN is NONE, DEADLINE, ACTOR_LOST, CONTROL_FAULT, CAPTURE_OVERFLOW,
CGROUP_FAULT, or KILL_UNKNOWN.

receipt-Q.v1 is exact:

P27E001_PROBE_RECEIPT_V1
AUTH_ID=H64
ORDINAL=UDEC
PROBE=Q
RELEASE_ORIGIN_NS=UDEC
RELEASE_RETURN_NS=UDEC
HOST_COMPLETE_NS=UDEC
ACK_RECORD_SAMPLE_NS=UDEC
STDOUT_BYTES=UDEC
STDOUT_SHA256=H64
STDERR_BYTES=0
STDERR_SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
OUTER_PID=UDEC
OUTER_RAW_STATUS=0
DIRECT_WAIT=1
STDOUT_EOF=1
STDERR_EOF=1
CGROUP_EMPTY=1
KILL_ISSUED=0
PARSER_PASS=1
CANDIDATE_PASS=1
TERMINAL_PASS=1
ACK=PASS
RECEIPT_END=1

It is O_EXCL mode0400, fsynced, verified, and followed by attempt-dir fsync.
ACK_RECORD_SAMPLE_NS is sampled immediately before construction. A separate
commit sample is retained in memory after both fsync returns and is used for
both bounds. The record plus those completed fsyncs is the durable ACK; the
prewrite sample does not claim durability. A late commit is evidence only
and FAIL.

recovery-Q.v1 is exact:

P27E001_RECOVERY_RECEIPT_V1
AUTH_ID=H64
PROBE=Q
PRIMARY=TOKEN
DIRECT_REAP=UNAVAILABLE
PIDFD_READY=B
STDOUT_BYTES=UDEC
STDOUT_SHA256=H64
STDOUT_EOF=B
STDERR_BYTES=UDEC
STDERR_SHA256=H64
STDERR_EOF=B
KILL_TICKET=B
KILL_WRITE_RETURNED=B
CGROUP_EMPTY=B
DISPOSITION=CONSUMED_INDETERMINATE
RECOVERY_END=1

B never writes PASS. report.v1 is exact:

P27E001_FINAL_REPORT_V1
AUTH_ID=H64
SUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13
ENTERED_COUNT=UDEC
PASS_COUNT=UDEC
STOP_PROBE=Q_OR_NONE
PRIMARY=TOKEN_OR_NONE
FAULT_SET=COMMA_LIST_OR_NONE
DIRECT_REAP_COMPLETE=B
CGROUP_EMPTY=B
CGROUP_REMOVED=B
STAGE_RETAINED=1
ATTEMPT_RETAINED=1
RETRY_ALLOWED=0
DISPOSITION=PASS_OR_CONSUMED_FAIL_OR_CONSUMED_INDETERMINATE
REPORT_END=1

It is exclusive mode0400, fsynced, reread, then followed by attempt-dir
fsync. The attempts base was already fsynced when the durable AUTH_ID intent
was committed; no base-directory entry changes at report time. Failure to
record cannot improve disposition.

## 14. Exact future effects, APIs, and denial

Authoring and H41/H42 are zero-write. A later separately authorized real run
has only:

1 one durable AUTH_ID attempt directory;
2 intent.v1, <=15 release records, <=15 receipts, <=1 kill ticket, <=1
  recovery record, and one report;
3 one /tmp/p27-e001-host-v15/AUTH_ID directory and exactly four source leaves;
4 V15 P11 target and P13 a/b including V15 unlink attempts;
5 one cgroup AUTH_ID directory, one atomic clone3 membership per entered
  probe, read-only cgroup.procs proofs, and <=1 cgroup.kill write.

The complete volatile write set is the execution event's sealed A, B, and
certificate memfds; A's at most fifteen fresh sealed OUTER memfds; the authenticated
empty-input pipe setup; actor status/diagnostic pipes; at most fifteen distinct
OUTER stdout/stderr pipe pairs; A/B control socket packets and at most one pidfd
SCM_RIGHTS transfer per entered probe; V15's already-frozen internal pipes;
and the kernel cgroup membership/event updates above. These are anonymous or
pseudofilesystem effects and create no additional pathname.

No other regular file, symlink, pathname socket, FIFO, temporary, cache, log,
backup, swap, lock, redirected output, tee, manifest, build, evidence,
workspace, PDF, paper, or release write exists.

A may read only fd100..105, certificate-listed runtime dependencies through
held root FDs, exact service components, cgroup fixed files, the boot-id
file, uname values, proc self fdinfo, and four leaves through held safe FD. B
reads only fixed FDs.
OUTER/descendants see only V15 sources, pinned runtime closure, proc self, and
safe directory.

A's API allowlist is raw read/write/lseek/fstat/statx/SHA-256/fcntl seals,
held openat/openat2, mkdirat, fsync/fchmod, pipe2, socketpair/SCM_RIGHTS,
memfd_create, close/dup2/close_range, one B fork, clone3 with
CLONE_INTO_CGROUP|CLONE_PIDFD, bounded stopped/direct waitpid, pidfd_open,
poll, clocks, chroot/fchdir, rlimits, signal/timer normalization,
credentials, prctl/capset, execve, SIGCONT, and exact cgroup/rmdir. B's subset
is raw IO/fstat/fsync/openat exclusive records, poll/clocks, socket messages,
close_range, pidfd readiness, cgroup.events, and one ticketed cgroup.kill. B
has no fork, exec, SIGCONT, waitpid, waitid, stage, extraction, or parser API.

The actor namespace and runtime root lack the workspace. No process has a
preopened workspace directory. Every build/evidence/root is OS-unreachable.
Neither literal names, lists, stats, opens, traverses, or tests the forbidden
build/evidence root.

## 15. Literal source records

The spans below are inert. Identities are frozen after raw measurement in
section 16. Delimiter strings are assembled from fragments inside A so each
delimiter line remains unique.

P27 RUNNER V1 ACTOR SOURCE BEGIN 7E3A2C61
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
WHOLE_LEDGER=(2431,12439253869,0o100644,1,0,0,2275332,23473,b"5b5d8b8f6ded4b20cfd06aeac42df4a41b72a0d7e53dfbd24b9a2bf805575efb")
WHOLE_V15=(2431,5916064615,0o100644,1,0,0,228310,4622,b"a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845")
LEDGER_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNTIME_PLAN_PRECONDITION_FAIL_AND_RUNNER_V1_AUTHOR_OPEN_NO_EXECUTION"
V15_TERMINAL=b"BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15_AUTHOR_STOP"
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
EMPTY_SHA=b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
OP_NS=15000000000
LAUNCH_NS=1000000000
POST_NS=1664800000
ACK_NS=500000000
HOST_NS=17664800000
TOTAL_NS=18164800000
CLEANUP_NS=2000000000
STREAM_CAP=3145728
MAX_FILE=8388608
MAX_U63=(1<<63)-1
UINT_MAX=(1<<32)-1
PREFLIGHT=True
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
O_DIR=os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW
LIBC=ctypes.CDLL(None,use_errno=True)
LIBC.syscall.restype=ctypes.c_long
SYS_CLONE3=435
CLONE_PIDFD=0x00001000
CLONE_INTO_CGROUP=0x200000000

class Refuse(Exception):
 pass

class ConsumedFail(Exception):
 pass

class ConsumedIndeterminate(Exception):
 pass

def need(value,kind=None):
 if not value:
  selected=(Refuse if PREFLIGHT else ConsumedFail) if kind is None else kind
  raise selected("closed")

def ascii_raw(raw,cap=MAX_FILE):
 need(type(raw)is bytes and 0<len(raw)<=cap and raw.endswith(b"\n"))
 need(all(value==10 or 32<=value<=126 for value in raw))
 return raw

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(value in b"0123456789abcdef" for value in raw))
 return raw

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw)
 need(low<=value<=high and str(value).encode()==raw)
 return value

def sdec(raw,low=-MAX_U63,high=MAX_U63):
 need(type(raw)is bytes and raw)
 if raw.startswith(b"-"):
  need(len(raw)>1 and raw[1:].isdigit() and raw[1]!=48)
 else:need(raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw)
 need(low<=value<=high and str(value).encode()==raw)
 return value

def even_hex(raw,cap=MAX_FILE):
 need(type(raw)is bytes and len(raw)<=cap*2 and len(raw)%2==0)
 need(all(value in b"0123456789abcdef" for value in raw))
 value=bytes.fromhex(raw.decode("ascii"))
 need(value.hex().encode()==raw and len(value)<=cap)
 return value

def sha(raw):
 return hashlib.sha256(raw).hexdigest().encode("ascii")

def read_all(number,cap=MAX_FILE):
 os.lseek(number,0,os.SEEK_SET)
 parts=[]
 total=0
 while True:
  chunk=os.read(number,min(1048576,cap-total+1))
  if not chunk:break
  total+=len(chunk)
  need(total<=cap)
  parts.append(chunk)
 raw=b"".join(parts)
 need(len(raw)==total)
 return raw

def write_all(number,raw):
 offset=0
 while offset<len(raw):
  count=os.write(number,raw[offset:])
  need(count>0)
  offset+=count

def fd_identity(number,raw):
 held=os.fstat(number)
 return (held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,raw.count(b"\n"),sha(raw))

def exact_whole(number,expected,terminal):
 raw=read_all(number,expected[6])
 need(fd_identity(number,raw)==expected,Refuse)
 need(raw.endswith(b"\n"),Refuse)
 lines=raw[:-1].split(b"\n")
 need(lines and lines[-1]==terminal and sum(line==terminal for line in lines)==1,Refuse)
 return raw

def seals(number):
 need(fcntl.fcntl(number,fcntl.F_GET_SEALS)==EXACT_SEALS,Refuse)

def extract_one(raw,begin,end):
 begin_line=begin+b"\n"
 need(raw.count(begin_line)==1 and raw.count(end+b"\n")==1)
 start=raw.index(begin_line)+len(begin_line)
 stop=raw.index(end+b"\n",start)
 need(start<=stop)
 return raw[start:stop]

def meta(raw):
 return (len(raw),raw.count(b"\n"),sha(raw))

def open_dir(path):
 need(type(path)is bytes and path.startswith(b"/") and b"\x00" not in path)
 current=os.open(b"/",O_DIR)
 try:
  for part in path.split(b"/")[1:]:
   need(part not in (b"",b".",b".."))
   following=os.open(part,O_DIR,dir_fd=current)
   os.close(current)
   current=following
  held=os.fstat(current)
  need(stat.S_ISDIR(held.st_mode) and held.st_uid==0 and held.st_gid==0 and held.st_mode&0o022==0)
  return current
 except BaseException:
  os.close(current)
  raise

def open_under(rootfd,path):
 need(type(path)is bytes and path.startswith(b"/") and b"\x00" not in path,Refuse)
 parts=path.split(b"/")[1:]
 need(parts and all(part not in (b"",b".",b"..") for part in parts),Refuse)
 current=os.dup(rootfd)
 try:
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current)
   os.close(current);current=following
  return os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
 finally:os.close(current)

def mount_id(number):
 info=os.open((b"/proc/self/fdinfo/"+str(number).encode()),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:raw=read_all(info,4096)
 finally:os.close(info)
 matches=[line[7:] for line in raw.splitlines() if line.startswith(b"mnt_id:\t")]
 need(len(matches)==1,Refuse)
 return udec(matches[0],1)

def verify_platform(cert):
 boot=os.open(b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:boot_raw=read_all(boot,128)
 finally:os.close(boot)
 need(boot_raw.endswith(b"\n") and sha(boot_raw)==cert[b"BOOT_ID_SHA256"],Refuse)
 uname=os.uname()
 sysname=uname.sysname.encode("ascii","strict");release=uname.release.encode("ascii","strict");version=uname.version.encode("ascii","strict");machine=uname.machine.encode("ascii","strict")
 platform=b"SYSNAME="+sysname+b"\nRELEASE="+release+b"\nVERSION="+version+b"\nMACHINE="+machine+b"\n"
 need(machine==b"x86_64" and release.hex().encode()==cert[b"KERNEL_RELEASE_HEX"] and sha(platform)==cert[b"PLATFORM_ID_SHA256"],Refuse)

def absent(directory,name,kind=ConsumedFail):
 try:os.stat(name,dir_fd=directory,follow_symlinks=False)
 except FileNotFoundError:return
 raise kind("name-present")

def durable_leaf(directory,name,raw):
 number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=directory)
 try:
  write_all(number,raw)
  os.fsync(number)
  held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==0 and held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw),ConsumedIndeterminate)
  need(read_all(number,len(raw))==raw,ConsumedIndeterminate)
 finally:os.close(number)
 os.fsync(directory)

def stage_leaf(directory,name,raw,identity):
 durable_leaf(directory,name,raw)
 number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory)
 try:
  held=os.fstat(number)
  again=read_all(number,identity[0])
  need(stat.S_ISREG(held.st_mode) and held.st_nlink==1 and held.st_uid==0 and held.st_gid==0 and stat.S_IMODE(held.st_mode)==0o400)
  need(meta(again)==identity)
 finally:os.close(number)

def memfd(raw,label):
 number=os.memfd_create(label,os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)
 write_all(number,raw)
 os.lseek(number,0,os.SEEK_SET)
 fcntl.fcntl(number,fcntl.F_ADD_SEALS,EXACT_SEALS)
 need(fcntl.fcntl(number,fcntl.F_GET_SEALS)==EXACT_SEALS)
 need(read_all(number,len(raw))==raw)
 os.lseek(number,0,os.SEEK_SET)
 return number

def close_range(first,last):
 need(0<=first<=last<=UINT_MAX)
 result=LIBC.close_range(ctypes.c_uint(first),ctypes.c_uint(last),ctypes.c_uint(0))
 need(result==0)

def map_fd(source,target):
 if source!=target:os.dup2(source,target,inheritable=True)
 else:os.set_inheritable(target,True)

def normalize_limits():
 inf=resource.RLIM_INFINITY
 fixed=((resource.RLIMIT_AS,(inf,inf)),(resource.RLIMIT_CORE,(0,0)),(resource.RLIMIT_CPU,(inf,inf)),(resource.RLIMIT_DATA,(inf,inf)),(resource.RLIMIT_FSIZE,(inf,inf)),(resource.RLIMIT_MEMLOCK,(8388608,8388608)),(resource.RLIMIT_MSGQUEUE,(819200,819200)),(resource.RLIMIT_NICE,(0,0)),(resource.RLIMIT_NOFILE,(1048576,1048576)),(resource.RLIMIT_NPROC,(1048576,1048576)),(resource.RLIMIT_RSS,(inf,inf)),(resource.RLIMIT_RTPRIO,(0,0)),(resource.RLIMIT_RTTIME,(inf,inf)),(resource.RLIMIT_SIGPENDING,(515199,515199)),(resource.RLIMIT_STACK,(8388608,inf)))
 for key,value in fixed:resource.setrlimit(key,value)
 for key,value in fixed:need(resource.getrlimit(key)==value)

def normalize_signals():
 signal.setitimer(signal.ITIMER_REAL,0.0,0.0)
 signal.setitimer(signal.ITIMER_VIRTUAL,0.0,0.0)
 signal.setitimer(signal.ITIMER_PROF,0.0,0.0)
 valid=signal.valid_signals()
 catchable=tuple(sorted(int(x) for x in valid if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))
 signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in catchable:signal.signal(number,signal.SIG_DFL)

class CapHeader(ctypes.Structure):
 _fields_=(("version",ctypes.c_uint32),("pid",ctypes.c_int))

class CapData(ctypes.Structure):
 _fields_=(("effective",ctypes.c_uint32),("permitted",ctypes.c_uint32),("inheritable",ctypes.c_uint32))

class CloneArgs(ctypes.Structure):
 _fields_=(("flags",ctypes.c_uint64),("pidfd",ctypes.c_uint64),("child_tid",ctypes.c_uint64),("parent_tid",ctypes.c_uint64),("exit_signal",ctypes.c_uint64),("stack",ctypes.c_uint64),("stack_size",ctypes.c_uint64),("tls",ctypes.c_uint64),("set_tid",ctypes.c_uint64),("set_tid_size",ctypes.c_uint64),("cgroup",ctypes.c_uint64))

def drop_caps():
 PR_SET_SECUREBITS=28
 PR_CAPBSET_DROP=24
 PR_CAP_AMBIENT=47
 PR_CAP_AMBIENT_CLEAR_ALL=4
 PR_SET_NO_NEW_PRIVS=38
 secure=1|2|4|8
 need(LIBC.prctl(PR_SET_SECUREBITS,secure,0,0,0)==0)
 for number in range(64):
  result=LIBC.prctl(PR_CAPBSET_DROP,number,0,0,0)
  if result!=0:need(ctypes.get_errno()==errno.EINVAL)
 header=CapHeader(0x20080522,0)
 data=(CapData*2)()
 need(LIBC.capset(ctypes.byref(header),ctypes.byref(data))==0)
 need(LIBC.prctl(PR_CAP_AMBIENT,PR_CAP_AMBIENT_CLEAR_ALL,0,0,0)==0)
 need(LIBC.prctl(PR_SET_NO_NEW_PRIVS,1,0,0,0)==0)

def child_context(safe_dev,safe_ino,keep):
 os.chroot(RUNTIME_ROOT)
 root=os.open(b"/",O_DIR)
 try:
  tmp=os.open(b"tmp",O_DIR,dir_fd=root)
  base=os.open(b"p27-e001-host-v15",O_DIR,dir_fd=tmp)
  safe=os.open(AUTH_ID,O_DIR,dir_fd=base)
  held=os.fstat(safe)
  need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
  os.fchdir(safe)
 finally:
  for number in (locals().get("safe",-1),locals().get("base",-1),locals().get("tmp",-1),root):
   if number>=0 and number not in keep:
    try:os.close(number)
    except OSError:pass
 os.setgroups([])
 os.setresgid(0,0,0)
 os.setresuid(0,0,0)
 os.umask(0o077)
 normalize_limits()
 normalize_signals()
 drop_caps()

CERT_ORDER=(b"ISSUER_ID",b"ISSUER_AUTHORIZATION_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"CGROUP2_MOUNT_ID",b"RUNTIME_ROOT_MOUNT_ID",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"MIN_REMAINING_AT_CONSUMPTION_NS",b"AUTH_BINDING",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0364_SHA256",b"V15_SHA256",b"V8_SHA256",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"RLIMIT_AS",b"RLIMIT_CORE",b"RLIMIT_CPU",b"RLIMIT_DATA",b"RLIMIT_FSIZE",b"RLIMIT_MEMLOCK",b"RLIMIT_MSGQUEUE",b"RLIMIT_NICE",b"RLIMIT_NOFILE",b"RLIMIT_NPROC",b"RLIMIT_RSS",b"RLIMIT_RTPRIO",b"RLIMIT_RTTIME",b"RLIMIT_SIGPENDING",b"RLIMIT_STACK",b"CREDENTIAL_VECTOR",b"FD_RETURN_COMMIT_PROGRESS_NS",b"CLOSE_RETURN_COMMIT_PROGRESS_NS",b"OWNER_CONTROL_PROGRESS_NS",b"KILL_REAP_PROGRESS_NS",b"TERMINAL_FRAMING_PROGRESS_NS",b"ACTOR_LAUNCH_PROGRESS_NS",b"POST_OPERATION_HOST_BOUND_NS",b"ACTOR_ACK_PROGRESS_NS",b"OPERATIONAL_BUDGET_NS",b"CONTAINMENT_CLEANUP_CAP_NS",b"COMMIT_WINDOW_TOKEN",b"OWNER_SURVIVAL_TOKEN",b"NO_MUTATOR_TOKEN",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"OWNER_SURVIVES_THROUGH_ACK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CGROUP_MEMBERSHIP_EXCLUSIVE",b"CLONE3_INTO_CGROUP_AVAILABLE",b"CGROUP_KILL_AVAILABLE",b"CGROUP_EVENTS_RELIABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"DEP_COUNT")

def parse_cert(raw):
 ascii_raw(raw)
 lines=raw[:-1].split(b"\n")
 need(lines[0]==b"P27E001_PREMISE_CERTIFICATE_V1" and lines[-1]==b"CERTIFICATE_END=1",Refuse)
 fixed=lines[1:1+len(CERT_ORDER)]
 need(len(fixed)==len(CERT_ORDER),Refuse)
 values={}
 for expected,line in zip(CERT_ORDER,fixed):
  parts=line.split(b"=",1)
  need(len(parts)==2 and parts[0]==expected and expected not in values,Refuse)
  values[expected]=parts[1]
 count=udec(values[b"DEP_COUNT"],1,256)
 dep_lines=lines[1+len(CERT_ORDER):-1]
 need(len(dep_lines)==count,Refuse)
 deps=[]
 roles={b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC",b"PYTHON_STDLIB",b"PYTHON_EXTENSION",b"NSS_DEPENDENCY",b"RUNTIME_DEPENDENCY"}
 for index,line in enumerate(dep_lines):
  prefix=(b"DEP[%04d]="%index)
  need(line.startswith(prefix),Refuse)
  fields=line[len(prefix):].split(b",")
  need(len(fields)==10 and fields[0] in roles,Refuse)
  path=even_hex(fields[1])
  need(path.startswith(b"/") and b"\x00" not in path,Refuse)
  need(fields[4] and all(value in b"01234567" for value in fields[4]),Refuse)
  mode=int(fields[4],8);need(format(mode,"o").encode()==fields[4],Refuse)
  ident=(udec(fields[2],1),udec(fields[3],1),mode,udec(fields[5],1),udec(fields[6]),udec(fields[7]),udec(fields[8]),h64(fields[9]))
  deps.append((fields[0],path,ident))
 need(len(set((item[0],item[1]) for item in deps))==len(deps),Refuse)
 for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC"):
  need(sum(1 for item in deps if item[0]==role)==1,Refuse)
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V1",b"ARCH":b"x86_64",b"MIN_REMAINING_AT_CONSUMPTION_NS":b"283472000000",b"AUTH_BINDING":b"SHA256_OF_COMPLETE_CERTIFICATE_BYTES",b"E0364_SHA256":WHOLE_LEDGER[8],b"V15_SHA256":WHOLE_V15[8],b"V8_SHA256":b"72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"RLIMIT_AS":b"INFINITY,INFINITY",b"RLIMIT_CORE":b"0,0",b"RLIMIT_CPU":b"INFINITY,INFINITY",b"RLIMIT_DATA":b"INFINITY,INFINITY",b"RLIMIT_FSIZE":b"INFINITY,INFINITY",b"RLIMIT_MEMLOCK":b"8388608,8388608",b"RLIMIT_MSGQUEUE":b"819200,819200",b"RLIMIT_NICE":b"0,0",b"RLIMIT_NOFILE":b"1048576,1048576",b"RLIMIT_NPROC":b"1048576,1048576",b"RLIMIT_RSS":b"INFINITY,INFINITY",b"RLIMIT_RTPRIO":b"0,0",b"RLIMIT_RTTIME":b"INFINITY,INFINITY",b"RLIMIT_SIGPENDING":b"515199,515199",b"RLIMIT_STACK":b"8388608,INFINITY",b"CREDENTIAL_VECTOR":b"UID0_GID0_RESUID0_RESGID0_GROUPS_EMPTY_UMASK0077_CAPS_EMPTY_NNP1",b"FD_RETURN_COMMIT_PROGRESS_NS":b"5000000",b"CLOSE_RETURN_COMMIT_PROGRESS_NS":b"2000000",b"OWNER_CONTROL_PROGRESS_NS":b"20000000",b"KILL_REAP_PROGRESS_NS":b"100000000",b"TERMINAL_FRAMING_PROGRESS_NS":b"100000000",b"ACTOR_LAUNCH_PROGRESS_NS":b"1000000000",b"POST_OPERATION_HOST_BOUND_NS":b"1664800000",b"ACTOR_ACK_PROGRESS_NS":b"500000000",b"OPERATIONAL_BUDGET_NS":b"15000000000",b"CONTAINMENT_CLEANUP_CAP_NS":b"2000000000",b"COMMIT_WINDOW_TOKEN":b"NO_ASYNC_TRANSFER_THROUGH_FIXED_FD_PROCESS_WAIT_AND_CLOSE_COMMIT_V15",b"OWNER_SURVIVAL_TOKEN":b"OWNER_SURVIVAL_PROGRESS_SINGLE_FRAME_V15",b"NO_MUTATOR_TOKEN":b"ROOT_OWNED_0700_STABLE_NONCE_NO_CONCURRENT_MUTATOR_V15"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_AUTHORIZATION_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0364_SHA256",b"V15_SHA256",b"V8_SHA256",b"PYTHON_IMAGE_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256"):h64(values[key])
 for key in (b"KERNEL_RELEASE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"CGROUP2_MOUNT_ID",b"RUNTIME_ROOT_MOUNT_ID",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO"):udec(values[key])
 need(values[b"LIBC_MODE"] and all(value in b"01234567" for value in values[b"LIBC_MODE"]),Refuse)
 libc_mode=int(values[b"LIBC_MODE"],8);need(format(libc_mode,"o").encode()==values[b"LIBC_MODE"],Refuse)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"OWNER_SURVIVES_THROUGH_ACK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CGROUP_MEMBERSHIP_EXCLUSIVE",b"CLONE3_INTO_CGROUP_AVAILABLE",b"CGROUP_KILL_AVAILABLE",b"CGROUP_EVENTS_RELIABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1",Refuse)
 by_role={role:next(item for item in deps if item[0]==role) for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC")}
 need(by_role[b"PYTHON_LINK"][1]==PYTHON and by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"ENV_EXEC"][1]==b"/usr/bin/env" and by_role[b"BASH_EXEC"][1]==b"/usr/bin/bash",Refuse)
 pyident=by_role[b"PYTHON_IMAGE"][2]
 need((pyident[0],pyident[1],pyident[6],pyident[7])==(udec(values[b"PYTHON_IMAGE_DEV"],1),udec(values[b"PYTHON_IMAGE_INO"],1),udec(values[b"PYTHON_IMAGE_BYTES"],1),values[b"PYTHON_IMAGE_SHA256"]),Refuse)
 libc_path=even_hex(values[b"LIBC_PATH_HEX"]);libc_ident=by_role[b"LIBC"][2]
 need(by_role[b"LIBC"][1]==libc_path and libc_ident==(udec(values[b"LIBC_DEV"],1),udec(values[b"LIBC_INO"],1),libc_mode,udec(values[b"LIBC_NLINK"],1),udec(values[b"LIBC_UID"]),udec(values[b"LIBC_GID"]),udec(values[b"LIBC_BYTES"],1),values[b"LIBC_SHA256"]),Refuse)
 now=time.time_ns()
 need(udec(values[b"NOT_BEFORE_REALTIME_NS"])<=now and udec(values[b"NOT_AFTER_REALTIME_NS"])-now>=283472000000,Refuse)
 return values,tuple(deps)

def verify_dependency(rootfd,entry):
 role,path,identity=entry
 parts=path.split(b"/")[1:]
 need(parts and all(part not in (b"",b".",b"..") for part in parts),Refuse)
 current=os.dup(rootfd)
 try:
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current)
   os.close(current);current=following
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False)
   need(stat.S_ISLNK(held.st_mode),Refuse)
   target=os.readlink(parts[-1],dir_fd=current)
   digest=sha(target);size=len(target)
  else:
   number=os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
   try:
    held=os.fstat(number);body=read_all(number,identity[6])
    digest=sha(body);size=len(body)
   finally:os.close(number)
  observed=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,size,digest)
  need(observed==identity,Refuse)
 finally:os.close(current)

def v15_sources(raw):
 labels=(b"OUTER",b"KEEPER",b"LAUNCHER",b"MARKER",b"CHILD")
 result=[]
 for label,expected in zip(labels,SOURCE_META):
  begin=b"UNIFIED "+label+b" V15 SOURCE BEGIN" if label!=b"CHILD" else b"NESTED CHILD V15 SOURCE BEGIN"
  end=b"UNIFIED "+label+b" V15 SOURCE END" if label!=b"CHILD" else b"NESTED CHILD V15 SOURCE END"
  span=extract_one(raw,begin,end)
  need(meta(span)==expected,Refuse)
  result.append(span)
 marker=result[3]
 embedded=extract_one(marker,b"CHILD_SOURCE=b'''\\",b"'''")
 need(embedded==result[4],Refuse)
 return tuple(result)

# P27 RUNNER V1 EMBEDDED VALIDATOR BEGIN C18F5D73
COMMON=(b"marker_image_dev",b"marker_image_ino",b"marker_image_sha256",b"probe_start_ns",b"probe_finish_ns",b"probe_elapsed_ns",b"probe_bound_ns",b"primary_failure",b"cleanup_failure",b"result")
PREFIX={b"P00":(b"source_item_bytes",b"source_item_accounted_bytes",b"broker_spawned",b"broker_payload_hex"),b"P01D":(b"python_image_dev",b"python_image_ino",b"python_image_bytes",b"python_image_sha256",b"libc_confstr_hex",b"libc_path_hex",b"libc_bytes",b"libc_sha256",b"backend_surface",b"spawn_premise_satisfied"),b"P01C":(b"libc_path_hex",b"libc_sha256",b"libc_confstr_hex",b"child_pids",b"child_statuses",b"child_raw_hex",b"spawn_premise_satisfied"),b"P02":(b"fds",b"environment_count",b"cwd_hex",b"flags"),b"P03":(b"soft_before",b"hard_before",b"soft_test",b"opened_fds",b"emfile"),b"P04":(b"valid_signal_count",b"default_signal_count",b"defaults_sha256",b"mask_empty"),b"P05":(b"wnohang_zero",b"eintr",b"echild",b"child_pids",b"raw_statuses",b"term_signal",b"broker_payload_hex"),b"P06":(b"monotonic",b"observed_min_delta_ns",b"start_ns",b"end_ns",b"deadline_checked"),b"P07":(b"empty_eagain",b"eof_before_last_writer",b"eof_after_last_writer"),b"P08":(b"child_pids",b"raw_statuses",b"same_session_group",b"post_pid_esrch",b"broker_payload_hex"),b"P09":(b"child_pids",b"raw_statuses",b"signal",b"reap_start_ns",b"reap_end_ns",b"reaped"),b"P10":(b"sample_count",b"pids",b"statuses",b"pid_duplicates",b"group_is_single_owned_launcher_group",b"reuse_proof"),b"P11":(b"open_result",b"atime_unchanged",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"scope_single_inode"),b"P12":(b"child_pids",b"raw_statuses",b"environment_count",b"underscore_absent",b"real_payload_invoked",b"broker_payload_hex"),b"P13":(b"file_fsync_returned",b"hardlink_noreplace_returned",b"inode_preserved",b"dir_fsync_returned",b"post_unlink_absent",b"cleanup_unlinked",b"durability_proof",b"rename_atomicity_proof")}

def csv_values(raw,signed=False,count=None):
 parts=raw.split(b",")
 need(parts and (count is None or len(parts)==count))
 return tuple(sdec(item) if signed else udec(item,1) for item in parts)

def child_observation(raw,mode,pid,source_sha,cwd_hex,phase):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|")
 need(len(fields)==11 and fields[0]==TAG and fields[1]==b"child=observation")
 expected=(b"mode="+mode,b"pid="+str(pid).encode(),b"image_sha="+PY_SHA,b"source_sha="+source_sha,b"cwd_hex="+cwd_hex,b"phase="+phase,b"result=PASS")
 need(fields[2]==expected[0] and fields[3]==expected[1])
 need(fields[4].startswith(b"sid=") and udec(fields[4][4:],1)>0)
 need(fields[5].startswith(b"pgid=") and udec(fields[5][5:],1)>0)
 need(fields[6:]==expected[2:])

def payload_item(raw,prefix):
 lead=prefix+b":"
 need(raw.startswith(lead))
 return even_hex(raw[len(lead):])

def parse_outer(line,probe,terminal):
 fields=line.split(b"|")
 if terminal:
  need(len(fields)==8 and fields[0]==TAG and fields[1]==b"outer=terminal" and fields[2]==b"probe="+probe and fields[3]==b"all_reaped=1" and fields[5]==b"frame_complete=1" and fields[6]==b"fatal=0" and fields[7]==b"result=PASS")
 else:
  need(len(fields)==8 and fields[0]==TAG and fields[1]==b"outer=candidate" and fields[2]==b"probe="+probe and fields[3]==b"slots=4" and fields[4]==b"all_reaped=1" and fields[6]==b"fatal=0" and fields[7]==b"result=PASS")
 role_field=fields[4] if terminal else fields[5]
 need(role_field.startswith(b"role_statuses="))
 roles=role_field[len(b"role_statuses="):].split(b",")
 need(len(roles)==4)
 result={}
 for expected,item in zip((b"launcher",b"keeper",b"marker",b"child"),roles):
  pieces=item.split(b":",1)
  need(len(pieces)==2 and pieces[0]==expected)
  result[expected]=sdec(pieces[1])
 return result

def validate_probe(rows,probe,ctx):
 one=lambda key:need(rows[key]==b"1")
 if probe==b"P00":
  need(rows[b"source_item_bytes"]==b"251414" and rows[b"source_item_accounted_bytes"]==b"251415")
  spawned=udec(rows[b"broker_spawned"],0,1);payload=even_hex(rows[b"broker_payload_hex"])
  items=payload.split(b";")
  if spawned==0:
   need(len(items)==1 and items[0].startswith(b"source_bytes=251414,returned=0,e2big=1,sha="));h64(items[0].rsplit(b"sha=",1)[1])
  else:
   need(len(items)==2 and items[1].startswith(b"source_bytes=251414,returned=1,e2big=0,sha="))
   synthetic=h64(items[1].rsplit(b"sha=",1)[1])
   observation=payload_item(items[0],b"INFO")
   child_fields=observation.split(b"|")
   need(len(child_fields)==11 and child_fields[3].startswith(b"pid="))
   child_observation(observation,b"INFO",udec(child_fields[3][4:],1),synthetic,ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P01D":
  need(udec(rows[b"python_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"python_image_ino"],1)==ctx[b"python_ino"] and rows[b"python_image_bytes"]==b"30626264" and rows[b"python_image_sha256"]==PY_SHA)
  need(rows[b"libc_path_hex"]==ctx[b"libc_path_hex"] and rows[b"libc_confstr_hex"]==ctx[b"libc_confstr_hex"] and udec(rows[b"libc_bytes"],1)==ctx[b"libc_bytes"] and rows[b"libc_sha256"]==ctx[b"libc_sha"])
  need(rows[b"backend_surface"]==b"posix-posix_spawn" and rows[b"spawn_premise_satisfied"]==b"0")
 elif probe==b"P01C":
  prior=ctx[b"p01d"]
  need(rows[b"libc_path_hex"]==prior[b"libc_path_hex"] and rows[b"libc_sha256"]==prior[b"libc_sha256"] and rows[b"libc_confstr_hex"]==prior[b"libc_confstr_hex"] and rows[b"spawn_premise_satisfied"]==b"1")
  pids=csv_values(rows[b"child_pids"],False,1);statuses=csv_values(rows[b"child_statuses"],True,1);need(statuses==(0,))
  child_observation(payload_item(even_hex(rows[b"child_raw_hex"]),b"INFO"),b"INFO",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P02":
  need(rows[b"fds"]==b"0,1,2,5,6" and rows[b"environment_count"]==b"10" and rows[b"cwd_hex"]==ctx[b"cwd_hex"] and rows[b"flags"]==b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1")
 elif probe==b"P03":need(tuple(rows[key] for key in PREFIX[probe])==(b"4096",b"1048576",b"64",b"59",b"1"))
 elif probe==b"P04":
  need(udec(rows[b"valid_signal_count"])==ctx[b"valid_signals"] and udec(rows[b"default_signal_count"])==ctx[b"default_signals"] and rows[b"defaults_sha256"]==ctx[b"defaults_sha"] and rows[b"mask_empty"]==b"1")
 elif probe==b"P05":
  need(rows[b"wnohang_zero"]==rows[b"eintr"]==rows[b"echild"]==b"1" and rows[b"term_signal"]==b"15")
  pids=csv_values(rows[b"child_pids"],False,2);statuses=csv_values(rows[b"raw_statuses"],True,2);need(pids[0]!=pids[1] and statuses==(23<<8,15))
  combined=payload_item(even_hex(rows[b"broker_payload_hex"]),b"P05");parts=combined.splitlines(True);need(len(parts)==2)
  child_observation(parts[0],b"EXIT23",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
  child_observation(parts[1],b"TERM",pids[1],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
 elif probe==b"P06":
  need(rows[b"monotonic"]==b"1" and udec(rows[b"observed_min_delta_ns"],1)>0 and udec(rows[b"start_ns"])<=udec(rows[b"end_ns"]) and rows[b"deadline_checked"]==b"1")
 elif probe==b"P07":need(tuple(rows[key] for key in PREFIX[probe])==(b"1",b"0",b"1"))
 elif probe==b"P08":
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(0,) and rows[b"same_session_group"]==rows[b"post_pid_esrch"]==b"1")
  child_observation(payload_item(even_hex(rows[b"broker_payload_hex"]),b"P08"),b"BLOCK0",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
 elif probe==b"P09":
  csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(9,) and rows[b"signal"]==b"9" and rows[b"reaped"]==b"1")
  start=udec(rows[b"reap_start_ns"]);finish=udec(rows[b"reap_end_ns"]);need(start<=finish and finish-start<=100000000)
 elif probe==b"P10":
  pids=csv_values(rows[b"pids"],False,16);need(rows[b"sample_count"]==b"16" and csv_values(rows[b"statuses"],True,16)==(0,)*16 and udec(rows[b"pid_duplicates"])==16-len(set(pids)) and rows[b"group_is_single_owned_launcher_group"]==b"1" and rows[b"reuse_proof"]==b"0")
 elif probe==b"P11":need(tuple(rows[key] for key in PREFIX[probe])==(b"OK",b"1",b"1",b"1",b"0",b"1"))
 elif probe==b"P12":
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(0,) and rows[b"environment_count"]==b"10" and rows[b"underscore_absent"]==b"1" and rows[b"real_payload_invoked"]==b"0")
  child_observation(payload_item(even_hex(rows[b"broker_payload_hex"]),b"CHAIN"),b"CHAIN",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P13":need(tuple(rows[key] for key in PREFIX[probe])==(b"1",b"1",b"1",b"1",b"1",b"1",b"0",b"0"))
 else:need(False)

def validate_transcript(raw,probe,ctx):
 ascii_raw(raw,STREAM_CAP)
 lines=raw[:-1].split(b"\n")
 need(lines and all(lines) and lines[0]==TAG+b"|marker=report|schema=15|probe="+probe)
 keys=PREFIX[probe]+COMMON
 need(len(lines)==len(keys)+4)
 rows={}
 for key,line in zip(keys,lines[1:1+len(keys)]):
  prefix=TAG+b"|probe="+probe+b"|"+key+b"="
  need(line.startswith(prefix) and key not in rows)
  value=line[len(prefix):];need(value and b"|" not in value and b"=" not in value)
  rows[key]=value
 footer=lines[1+len(keys)];need(footer==TAG+b"|probe="+probe+b"|result=PASS")
 candidate=parse_outer(lines[2+len(keys)],probe,False)
 terminal=parse_outer(lines[3+len(keys)],probe,True)
 need(candidate==terminal and candidate[b"launcher"]==15 and candidate[b"keeper"]==15 and candidate[b"marker"]==0)
 start=udec(rows[b"probe_start_ns"]);finish=udec(rows[b"probe_finish_ns"]);elapsed=udec(rows[b"probe_elapsed_ns"])
 need(start<=finish and finish-start==elapsed and elapsed<=OP_NS and rows[b"probe_bound_ns"]==b"15000000000" and rows[b"primary_failure"]==b"none" and rows[b"cleanup_failure"]==b"none" and rows[b"result"]==b"PASS")
 need(udec(rows[b"marker_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"marker_image_ino"],1)==ctx[b"python_ino"] and rows[b"marker_image_sha256"]==PY_SHA)
 validate_probe(rows,probe,ctx)
 expected=-1
 if probe==b"P00":expected=-1 if rows[b"broker_spawned"]==b"0" else 0
 elif probe in (b"P01C",b"P08",b"P10",b"P12"):expected=0
 elif probe==b"P05":expected=15
 elif probe==b"P09":expected=9
 need(candidate[b"child"]==expected)
 return rows
# P27 RUNNER V1 EMBEDDED VALIDATOR END C18F5D73

def cgroup_populated(events_fd):
 os.lseek(events_fd,0,os.SEEK_SET)
 raw=os.read(events_fd,4096)
 lines=raw.splitlines()
 matches=[line for line in lines if line.startswith(b"populated ")]
 need(len(matches)==1 and matches[0] in (b"populated 0",b"populated 1"),ConsumedIndeterminate)
 return matches[0]==b"populated 1"

def cgroup_state(cg_fd):
 events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC,dir_fd=cg_fd)
 try:return cgroup_populated(events)
 finally:os.close(events)

def source_argv(probe,safe_stat,p01c):
 items=[PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",probe,AUTH_ID,b"15000000000",b"5000000",b"2000000",b"20000000",b"100000000",b"100000000",b"500000000",b"NO_ASYNC_TRANSFER_THROUGH_FIXED_FD_PROCESS_WAIT_AND_CLOSE_COMMIT_V15",b"OWNER_SURVIVAL_PROGRESS_SINGLE_FRAME_V15",b"ROOT_OWNED_0700_STABLE_NONCE_NO_CONCURRENT_MUTATOR_V15",str(safe_stat.st_dev).encode(),str(safe_stat.st_ino).encode()]
 for identity in SOURCE_META:items.append(str(identity[0]).encode()+b","+str(identity[1]).encode()+b","+identity[2])
 items.extend(p01c)
 need(len(items)==27 or (probe==b"P01C" and len(items)==40))
 return items

def wait_ready(control,expected,deadline):
 control.settimeout(max(0.001,(deadline-time.monotonic_ns())/1000000000))
 raw=control.recv(4096)
 need(raw==expected,ConsumedIndeterminate)

def launch_b(out_r,err_r,events_fd,kill_fd,attempt_fd,safe_stat,recovery_sha,ordinal,release_origin):
 left,right=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
 actor_pidfd=os.pidfd_open(os.getpid(),0)
 pid=os.fork()
 if pid==0:
  try:
   left.close()
   for source,target in ((out_r,3),(err_r,4),(events_fd,5),(kill_fd,6),(right.fileno(),7),(attempt_fd,8),(actor_pidfd,9),(105,100)):map_fd(source,target)
   os.set_inheritable(0,True)
   os.close(1);os.close(2)
   child_context(safe_stat.st_dev,safe_stat.st_ino,set(range(3,10))|{100})
   close_range(10,99);close_range(101,UINT_MAX)
   argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",b"WATCH",AUTH_ID,CURRENT_PROBE,b"18164800000",b"2000000000",b"3145728",b"3145728",str(ordinal).encode(),recovery_sha,str(release_origin).encode())
   os.execve(PYTHON,argv,ENV)
  except BaseException:os._exit(97)
 right.close();os.close(actor_pidfd)
 return pid,left

def launch_outer(outer_fd,in_r,out_w,err_w,safe_stat,argv,cg_fd):
 pidfd_cell=ctypes.c_int(-1)
 args=CloneArgs()
 args.flags=CLONE_PIDFD|CLONE_INTO_CGROUP
 args.pidfd=ctypes.addressof(pidfd_cell)
 args.exit_signal=int(signal.SIGCHLD)
 args.cgroup=cg_fd
 pid=LIBC.syscall(SYS_CLONE3,ctypes.byref(args),ctypes.sizeof(args))
 if pid<0:raise OSError(ctypes.get_errno(),"clone3")
 if pid==0:
  try:
   os.kill(os.getpid(),signal.SIGSTOP)
   map_fd(in_r,0);map_fd(out_w,1);map_fd(err_w,2);map_fd(outer_fd,100)
   child_context(safe_stat.st_dev,safe_stat.st_ino,{0,1,2,100})
   close_range(3,99);close_range(101,UINT_MAX)
   os.execve(PYTHON,tuple(argv),ENV)
  except BaseException:os._exit(98)
 need(pid>=2 and pidfd_cell.value>=0,ConsumedIndeterminate)
 return pid,pidfd_cell.value

def recv_packet(control,deadline,size):
 remaining=deadline-time.monotonic_ns()
 need(remaining>0,ConsumedIndeterminate)
 control.settimeout(max(0.001,remaining/1000000000))
 return control.recv(size)

def recv_b(control,deadline):
 header=recv_packet(control,deadline,4096)
 need(header.endswith(b"\n") and header.startswith(b"P27B1|"),ConsumedIndeterminate)
 fields=header[:-1].split(b"|");need(len(fields)==11,ConsumedIndeterminate)
 values={}
 for item in fields[1:]:
  pieces=item.split(b"=",1);need(len(pieces)==2 and pieces[0] not in values,ConsumedIndeterminate);values[pieces[0]]=pieces[1]
 out_need=udec(values[b"stdout_len"],0,STREAM_CAP);err_need=udec(values[b"stderr_len"],0,STREAM_CAP)
 out=bytearray();err=bytearray()
 while True:
  packet=recv_packet(control,deadline,65536)
  need(packet,ConsumedIndeterminate)
  if packet==b"P27B1_END\n":break
  need(packet[:1] in (b"O",b"E"),ConsumedIndeterminate)
  target=out if packet[:1]==b"O" else err
  target.extend(packet[1:])
  need(len(target)<=STREAM_CAP,ConsumedIndeterminate)
 need(len(out)==out_need and len(err)==err_need,ConsumedIndeterminate)
 return values,bytes(out),bytes(err)

def wait_status(pid,flags,deadline):
 while True:
  try:waited,raw=os.waitpid(pid,flags|os.WNOHANG)
  except InterruptedError:continue
  need(waited in (0,pid),ConsumedIndeterminate)
  if waited==pid:return raw
  need(time.monotonic_ns()<=deadline,ConsumedIndeterminate)
  try:select.poll().poll(1)
  except InterruptedError:pass

def release_record(attempt_fd,ordinal,probe,pid,cg_stat,safe_stat,argv):
 body=(b"P27E001_RELEASE_V1\nAUTH_ID="+AUTH_ID+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nOUTER_PID="+str(pid).encode()+b"\nCGROUP_DEV="+str(cg_stat.st_dev).encode()+b"\nCGROUP_INO="+str(cg_stat.st_ino).encode()+b"\nSAFE_DEV="+str(safe_stat.st_dev).encode()+b"\nSAFE_INO="+str(safe_stat.st_ino).encode()+b"\nARGV_SHA256="+sha(b"\x00".join(argv))+b"\nENV_SHA256="+sha(b"\x00".join(key+b"="+ENV[key] for key in sorted(ENV)))+b"\nRELEASE_AUTHORIZED=1\nRELEASE_END=1\n")
 durable_leaf(attempt_fd,b"release-"+probe+b".v1",body)

def probe_receipt(attempt_fd,ordinal,probe,times,pid,stdout):
 release_origin,release_return,host_complete=times
 prepare=time.monotonic_ns()
 body=(b"P27E001_PROBE_RECEIPT_V1\nAUTH_ID="+AUTH_ID+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nRELEASE_ORIGIN_NS="+str(release_origin).encode()+b"\nRELEASE_RETURN_NS="+str(release_return).encode()+b"\nHOST_COMPLETE_NS="+str(host_complete).encode()+b"\nACK_RECORD_SAMPLE_NS="+str(prepare).encode()+b"\nSTDOUT_BYTES="+str(len(stdout)).encode()+b"\nSTDOUT_SHA256="+sha(stdout)+b"\nSTDERR_BYTES=0\nSTDERR_SHA256="+EMPTY_SHA+b"\nOUTER_PID="+str(pid).encode()+b"\nOUTER_RAW_STATUS=0\nDIRECT_WAIT=1\nSTDOUT_EOF=1\nSTDERR_EOF=1\nCGROUP_EMPTY=1\nKILL_ISSUED=0\nPARSER_PASS=1\nCANDIDATE_PASS=1\nTERMINAL_PASS=1\nACK=PASS\nRECEIPT_END=1\n")
 durable_leaf(attempt_fd,b"receipt-"+probe+b".v1",body)
 sample=time.monotonic_ns()
 need(sample-host_complete<=ACK_NS and sample-release_origin<=TOTAL_NS)
 return sample

def derive_p01c(prior,cert):
 path=even_hex(prior[b"libc_path_hex"])
 need(prior[b"libc_path_hex"]==cert[b"LIBC_PATH_HEX"] and prior[b"libc_confstr_hex"]==cert[b"LIBC_CONFSTR_HEX"] and prior[b"libc_sha256"]==cert[b"LIBC_SHA256"])
 rootfd=open_dir(RUNTIME_ROOT)
 try:
  number=open_under(rootfd,path)
  try:
   held=os.fstat(number);raw=read_all(number,held.st_size)
  finally:os.close(number)
  py=open_under(rootfd,PYIMAGE)
  try:
   pyheld=os.fstat(py);pyraw=read_all(py,30626264)
  finally:os.close(py)
 finally:os.close(rootfd)
 libc_identity=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,sha(raw))
 certified=(udec(cert[b"LIBC_DEV"],1),udec(cert[b"LIBC_INO"],1),int(cert[b"LIBC_MODE"],8),udec(cert[b"LIBC_NLINK"],1),udec(cert[b"LIBC_UID"]),udec(cert[b"LIBC_GID"]),udec(cert[b"LIBC_BYTES"],1),cert[b"LIBC_SHA256"])
 need(libc_identity==certified and sha(raw)==prior[b"libc_sha256"] and held.st_size==udec(prior[b"libc_bytes"]))
 need(sha(pyraw)==PY_SHA and str(pyheld.st_dev).encode()==prior[b"python_image_dev"] and str(pyheld.st_ino).encode()==prior[b"python_image_ino"])
 return (prior[b"libc_path_hex"],str(held.st_dev).encode(),str(held.st_ino).encode(),format(held.st_mode,"o").encode(),str(held.st_nlink).encode(),str(held.st_uid).encode(),str(held.st_gid).encode(),str(held.st_size).encode(),prior[b"libc_sha256"],prior[b"libc_confstr_hex"],prior[b"python_image_dev"],prior[b"python_image_ino"],prior[b"python_image_sha256"])

def run_probe(ordinal,probe,attempt_fd,cg_fd,safe_fd,safe_stat,outer_source,recovery_sha,ctx,p01c):
 global CURRENT_PROBE
 CURRENT_PROBE=probe
 need(not cgroup_state(cg_fd))
 in_r,in_w=os.pipe2(os.O_CLOEXEC);os.close(in_w);need(os.read(in_r,1)==b"")
 out_r,out_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK);err_r,err_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
 need(os.fstat(out_r).st_ino!=os.fstat(err_r).st_ino)
 outer_fd=memfd(outer_source,"p27-v15-outer")
 events_fd=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC,dir_fd=cg_fd)
 kill_fd=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC,dir_fd=cg_fd)
 release_origin=time.monotonic_ns()
 bpid=-1;control=None;pid=-1;outer_pid=-1;pidfd=-1
 try:
  bpid,control=launch_b(out_r,err_r,events_fd,kill_fd,attempt_fd,safe_stat,recovery_sha,ordinal,release_origin)
  for number in (out_r,err_r,events_fd,kill_fd):os.close(number)
  out_r=err_r=events_fd=kill_fd=-1
  wait_ready(control,b"READY\n",release_origin+LAUNCH_NS)
  argv=source_argv(probe,safe_stat,p01c)
  pid,pidfd=launch_outer(outer_fd,in_r,out_w,err_w,safe_stat,argv,cg_fd)
  for number in (in_r,out_w,err_w,outer_fd):os.close(number)
  in_r=out_w=err_w=outer_fd=-1
  arm=b"ARM|"+str(pid).encode()+b"|"+str(release_origin).encode()+b"|"+str(TOTAL_NS).encode()+b"\n"
  need(control.sendmsg([arm],[(socket.SOL_SOCKET,socket.SCM_RIGHTS,pidfd.to_bytes(4,sys.byteorder))])==len(arm),ConsumedIndeterminate)
  os.close(pidfd);pidfd=-1
  wait_ready(control,b"ARMED\n",release_origin+LAUNCH_NS)
  raw=wait_status(pid,os.WUNTRACED,release_origin+LAUNCH_NS)
  need(os.WIFSTOPPED(raw) and os.WSTOPSIG(raw)==signal.SIGSTOP,ConsumedIndeterminate)
  check=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC,dir_fd=cg_fd)
  try:need(read_all(check,64)==str(pid).encode()+b"\n",ConsumedIndeterminate)
  finally:os.close(check)
  need(cgroup_state(cg_fd),ConsumedIndeterminate)
  release_record(attempt_fd,ordinal,probe,pid,os.fstat(cg_fd),safe_stat,argv)
  os.kill(pid,signal.SIGCONT)
  release_return=time.monotonic_ns()
  need(release_origin<release_return<=release_origin+LAUNCH_NS,ConsumedIndeterminate)
  outer_pid=pid;raw=wait_status(pid,0,release_origin+TOTAL_NS+CLEANUP_NS);pid=-1
  direct_done=time.monotonic_ns()
  values,stdout,stderr=recv_b(control,release_origin+TOTAL_NS+CLEANUP_NS)
  done=udec(values[b"done_ns"]);host_complete=max(direct_done,done)
  need(host_complete<=release_origin+HOST_NS and raw==0 and values[b"fault"]==b"NONE" and values[b"stdout_eof"]==b"1" and values[b"stderr_eof"]==b"1" and values[b"cgroup_empty"]==b"1" and values[b"kill_issued"]==b"0" and stderr==b"",ConsumedFail)
  rows=validate_transcript(stdout,probe,ctx)
  probe_receipt(attempt_fd,ordinal,probe,(release_origin,release_return,host_complete),outer_pid,stdout)
  need(control.send(b"ACKED\n")==6,ConsumedIndeterminate)
  control.close();control=None
  braw=wait_status(bpid,0,release_origin+TOTAL_NS+CLEANUP_NS);bpid=-1
  need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
  return rows
 except BaseException as original:
  try:control.send(b"FAIL\n")
  except BaseException:pass
  try:control.close()
  except BaseException:pass
  control=None
  for number in (in_r,out_r,out_w,err_r,err_w,outer_fd,events_fd,kill_fd,pidfd):
   if number>=0:
    try:os.close(number)
    except OSError:pass
  in_r=out_r=out_w=err_r=err_w=outer_fd=events_fd=kill_fd=pidfd=-1
  uncertain=False
  if pid>=0:
   try:wait_status(pid,0,time.monotonic_ns()+CLEANUP_NS+ACK_NS);pid=-1
   except BaseException:uncertain=True
  if bpid>=0:
   try:
    braw=wait_status(bpid,0,time.monotonic_ns()+CLEANUP_NS+ACK_NS);bpid=-1
    need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
   except BaseException:uncertain=True
  if uncertain:raise ConsumedIndeterminate("cleanup-uncertain") from original
  raise
 finally:
  for number in (in_r,out_r,out_w,err_r,err_w,outer_fd,events_fd,kill_fd,pidfd):
   if number>=0:
    try:os.close(number)
    except OSError:pass

def final_report(attempt_fd,entered,passed,stop,primary,faults,disposition,empty,removed):
 direct=disposition==b"PASS" and entered==passed==15
 body=(b"P27E001_FINAL_REPORT_V1\nAUTH_ID="+AUTH_ID+b"\nSUITE="+b",".join(SUITE)+b"\nENTERED_COUNT="+str(entered).encode()+b"\nPASS_COUNT="+str(passed).encode()+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary+b"\nFAULT_SET="+faults+b"\nDIRECT_REAP_COMPLETE="+(b"1" if direct else b"0")+b"\nCGROUP_EMPTY="+(b"1" if empty else b"0")+b"\nCGROUP_REMOVED="+(b"1" if removed else b"0")+b"\nSTAGE_RETAINED=1\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION="+disposition+b"\nREPORT_END=1\n")
 durable_leaf(attempt_fd,b"report.v1",body)

def main():
 global AUTH_ID,PREFLIGHT
 need(type(sys.argv)is list and len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RUN",Refuse)
 AUTH_ID=sys.argv[2].encode("ascii")
 h64(AUTH_ID)
 need(os.environb==ENV and os.read(0,1)==b"" and sys.gettrace() is None and sys.getprofile() is None,Refuse)
 need(os.getresuid()==(0,0,0) and os.getresgid()==(0,0,0) and os.getgroups()==[] and os.getpid()==os.getpgrp()==os.getsid(0),Refuse)
 need(os.umask(0o077)==0o077,Refuse)
 normalize_limits();normalize_signals();need(signal.sigpending()==set(),Refuse)
 fd0=os.fstat(0);fd1=os.fstat(1);fd2=os.fstat(2)
 need(stat.S_ISFIFO(fd0.st_mode) and stat.S_ISFIFO(fd1.st_mode) and stat.S_ISFIFO(fd2.st_mode) and (fd1.st_dev,fd1.st_ino)!=(fd2.st_dev,fd2.st_ino),Refuse)
 close_range(3,99);close_range(106,UINT_MAX)
 for number in (100,104,105):seals(number)
 actor_raw=read_all(100);ledger=exact_whole(101,WHOLE_LEDGER,LEDGER_TERMINAL);v15=exact_whole(102,WHOLE_V15,V15_TERMINAL);plan=read_all(103);cert_raw=read_all(104);recovery_raw=read_all(105)
 need(sha(cert_raw)==AUTH_ID,Refuse)
 cert,deps=parse_cert(cert_raw)
 verify_platform(cert)
 need(sha(plan)==cert[b"PLAN_SHA256"] and sha(actor_raw)==cert[b"RUNNER_SHA256"] and sha(recovery_raw)==cert[b"RECOVERY_SHA256"],Refuse)
 ab=b"P27 RUNNER V1 ACTOR SOURCE "+b"BEGIN 7E3A2C61";ae=b"P27 RUNNER V1 ACTOR SOURCE "+b"END 7E3A2C61"
 rb=b"P27 RUNNER V1 RECOVERY SOURCE "+b"BEGIN 9B4D50F2";re=b"P27 RUNNER V1 RECOVERY SOURCE "+b"END 9B4D50F2"
 need(extract_one(plan,ab,ae)==actor_raw and extract_one(plan,rb,re)==recovery_raw,Refuse)
 sources=v15_sources(v15)
 runtime_fd=open_dir(RUNTIME_ROOT)
 try:
  runtime_stat=os.fstat(runtime_fd)
  need((runtime_stat.st_dev,runtime_stat.st_ino,mount_id(runtime_fd))==(udec(cert[b"RUNTIME_ROOT_DEV"],1),udec(cert[b"RUNTIME_ROOT_INO"],1),udec(cert[b"RUNTIME_ROOT_MOUNT_ID"],1)),Refuse)
  for entry in deps:verify_dependency(runtime_fd,entry)
 finally:os.close(runtime_fd)
 attempt_base=open_dir(ATTEMPT_BASE);stage_base=open_dir(STAGE_BASE);cgroup_base=open_dir(CGROUP_BASE)
 attempt_stat=os.fstat(attempt_base);stage_stat=os.fstat(stage_base);cgroup_stat=os.fstat(cgroup_base)
 need(stat.S_IMODE(attempt_stat.st_mode)==0o700,Refuse)
 need((stage_stat.st_dev,stage_stat.st_ino)==(udec(cert[b"SAFE_BIND_DEV"],1),udec(cert[b"SAFE_BIND_INO"],1)),Refuse)
 need((cgroup_stat.st_dev,cgroup_stat.st_ino,mount_id(cgroup_base))==(udec(cert[b"CGROUP_BASE_DEV"],1),udec(cert[b"CGROUP_BASE_INO"],1),udec(cert[b"CGROUP2_MOUNT_ID"],1)),Refuse)
 absent(attempt_base,AUTH_ID,Refuse);absent(stage_base,AUTH_ID,Refuse);absent(cgroup_base,AUTH_ID,Refuse)
 PREFLIGHT=False
 os.mkdir(AUTH_ID,0o700,dir_fd=attempt_base);attempt_fd=os.open(AUTH_ID,O_DIR,dir_fd=attempt_base)
 attempt_child=os.fstat(attempt_fd);need(stat.S_ISDIR(attempt_child.st_mode) and stat.S_IMODE(attempt_child.st_mode)==0o700 and attempt_child.st_uid==0 and attempt_child.st_gid==0,ConsumedIndeterminate)
 consumed=False
 try:
  cg_path=CGROUP_BASE+b"/"+AUTH_ID;safe_path=STAGE_BASE+b"/"+AUTH_ID
  intent=(b"P27E001_ATTEMPT_INTENT_V1\nAUTH_ID="+AUTH_ID+b"\nCERT_SHA256="+AUTH_ID+b"\nPLAN_SHA256="+cert[b"PLAN_SHA256"]+b"\nRUNNER_SHA256="+cert[b"RUNNER_SHA256"]+b"\nRECOVERY_SHA256="+cert[b"RECOVERY_SHA256"]+b"\nE0364_SHA256="+WHOLE_LEDGER[8]+b"\nV15_SHA256="+WHOLE_V15[8]+b"\nV8_SHA256="+cert[b"V8_SHA256"]+b"\nSUITE="+b",".join(SUITE)+b"\nNONCE="+AUTH_ID+b"\nCGROUP_PATH_HEX="+cg_path.hex().encode()+b"\nSAFE_PATH_HEX="+safe_path.hex().encode()+b"\nCONSUMED=1\nRETRY_ALLOWED=0\nRELEASE_COUNT_AT_INTENT=0\nINTENT_END=1\n")
  durable_leaf(attempt_fd,b"intent.v1",intent);os.fsync(attempt_base);consumed=True
  os.mkdir(AUTH_ID,0o700,dir_fd=stage_base);os.fsync(stage_base);safe_fd=os.open(AUTH_ID,O_DIR,dir_fd=stage_base);safe_stat=os.fstat(safe_fd)
  need((safe_stat.st_uid,safe_stat.st_gid,stat.S_IMODE(safe_stat.st_mode))==(0,0,0o700),ConsumedIndeterminate)
  for name in (b"target",b"a",b"b"):absent(safe_fd,name)
  for name,body,identity in zip(SOURCE_NAMES,sources[1:],SOURCE_META[1:]):stage_leaf(safe_fd,name,body,identity)
  os.fsync(safe_fd)
  os.mkdir(AUTH_ID,0o700,dir_fd=cgroup_base);cg_fd=os.open(AUTH_ID,O_DIR,dir_fd=cgroup_base)
  events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC,dir_fd=cg_fd)
  need(not cgroup_populated(events),ConsumedIndeterminate);os.close(events)
  ctx={b"cwd_hex":safe_path.hex().encode(),b"python_dev":udec(cert[b"PYTHON_IMAGE_DEV"],1),b"python_ino":udec(cert[b"PYTHON_IMAGE_INO"],1),b"libc_path_hex":cert[b"LIBC_PATH_HEX"],b"libc_confstr_hex":cert[b"LIBC_CONFSTR_HEX"],b"libc_bytes":udec(cert[b"LIBC_BYTES"],1),b"libc_sha":cert[b"LIBC_SHA256"],b"valid_signals":udec(cert[b"VALID_SIGNAL_COUNT"],1),b"default_signals":udec(cert[b"DEFAULT_SIGNAL_COUNT"],1),b"defaults_sha":cert[b"DEFAULTS_SHA256"]}
  passed=0;entered=0;prior=None
  for ordinal,probe in enumerate(SUITE):
   entered+=1
   p01c=derive_p01c(prior,cert) if probe==b"P01C" else ()
   rows=run_probe(ordinal,probe,attempt_fd,cg_fd,safe_fd,safe_stat,sources[0],cert[b"RECOVERY_SHA256"],ctx,p01c)
   passed+=1
   if probe==b"P01D":prior=rows;ctx[b"p01d"]=rows
  events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC,dir_fd=cg_fd);empty=not cgroup_populated(events);os.close(events);need(empty)
  os.close(cg_fd);cg_fd=-1
  os.rmdir(AUTH_ID,dir_fd=cgroup_base)
  try:os.stat(AUTH_ID,dir_fd=cgroup_base,follow_symlinks=False);need(False)
  except FileNotFoundError:pass
  final_report(attempt_fd,entered,passed,b"NONE",b"NONE",b"NONE",b"PASS",True,True)
  final_line=b"P27E001_RUNNER_V1|AUTH_ID="+AUTH_ID+b"|entered=15|passed=15|disposition=PASS\n"
  write_all(1,final_line)
 except BaseException as error:
  if consumed:
   disposition=b"CONSUMED_FAIL" if isinstance(error,ConsumedFail) else b"CONSUMED_INDETERMINATE"
   primary=b"TRANSCRIPT_OR_RUNTIME" if isinstance(error,ConsumedFail) else b"UNKNOWN_EFFECT"
   stop=locals().get("probe",b"NONE")
   try:final_report(attempt_fd,locals().get("entered",0),locals().get("passed",0),stop,primary,primary,disposition,False,False)
   except BaseException:pass
  raise
 finally:
  for number in (locals().get("cg_fd",-1),locals().get("safe_fd",-1),attempt_fd,attempt_base,stage_base,cgroup_base):
   if number>=0:
    try:os.close(number)
    except OSError:pass

try:
 main()
except Refuse:
 raise SystemExit(80)
except ConsumedIndeterminate:
 raise SystemExit(82)
except ConsumedFail:
 raise SystemExit(81)
except BaseException:
 raise SystemExit(83)
raise SystemExit(0)
P27 RUNNER V1 ACTOR SOURCE END 7E3A2C61

P27 RUNNER V1 RECOVERY SOURCE BEGIN 9B4D50F2
import errno
import fcntl
import hashlib
import os
import select
import socket
import stat
import sys
import time

EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
PROBES=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
TOKENS=(b"NONE",b"DEADLINE",b"ACTOR_LOST",b"CONTROL_FAULT",b"CAPTURE_OVERFLOW",b"CGROUP_FAULT",b"KILL_UNKNOWN")
MAX_U63=(1<<63)-1

class Closed(Exception):
 pass

def need(value):
 if not value:raise Closed("closed")

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(value in b"0123456789abcdef" for value in raw))
 return raw

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw)
 return value

def sha(raw):
 return hashlib.sha256(raw).hexdigest().encode("ascii")

def write_all(number,raw):
 offset=0
 while offset<len(raw):
  count=os.write(number,raw[offset:])
  need(count>0);offset+=count

def read_source():
 need(fcntl.fcntl(100,fcntl.F_GET_SEALS)==EXACT_SEALS)
 os.lseek(100,0,os.SEEK_SET);parts=[];total=0
 while True:
  chunk=os.read(100,1048576)
  if not chunk:break
  total+=len(chunk);need(total<=8388608);parts.append(chunk)
 raw=b"".join(parts);need(len(raw)==total)
 return raw

def durable(name,raw):
 number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=8)
 try:
  write_all(number,raw);os.fsync(number)
  held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==0 and held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw))
  os.lseek(number,0,os.SEEK_SET);parts=[];total=0
  while True:
   chunk=os.read(number,min(1048576,len(raw)-total+1))
   if not chunk:break
   total+=len(chunk);need(total<=len(raw));parts.append(chunk)
  need(b"".join(parts)==raw)
 finally:os.close(number)
 os.fsync(8)

def populated():
 os.lseek(5,0,os.SEEK_SET)
 raw=os.read(5,4096)
 matches=[line for line in raw.splitlines() if line.startswith(b"populated ")]
 need(len(matches)==1 and matches[0] in (b"populated 0",b"populated 1"))
 return matches[0]==b"populated 1"

def drain(number,target,cap):
 overflow=False;eof=False
 while True:
  try:chunk=os.read(number,65536)
  except BlockingIOError:break
  except InterruptedError:continue
  if chunk==b"":eof=True;break
  available=cap-len(target)
  if available>0:target.extend(chunk[:available])
  if len(chunk)>available:overflow=True
 return overflow,eof

def kill_once(auth,probe,reason):
 body=(b"P27E001_KILL_TICKET_V1\nAUTH_ID="+auth+b"\nPROBE="+probe+b"\nPRIMARY="+reason+b"\nKILL_AUTHORITY=1\nKILL_COUNT_BEFORE=0\nTICKET_END=1\n")
 try:durable(b"kill-ticket.v1",body)
 except FileExistsError:return False,False
 write_all(6,b"1\n")
 return True,True

def send_memory(control,probe,fault,stdout,stderr,out_eof,err_eof,empty,kill_issued,pid_ready,done):
 need(fault in TOKENS)
 header=(b"P27B1|probe="+probe+b"|fault="+fault+b"|stdout_len="+str(len(stdout)).encode()+b"|stderr_len="+str(len(stderr)).encode()+b"|stdout_eof="+(b"1" if out_eof else b"0")+b"|stderr_eof="+(b"1" if err_eof else b"0")+b"|cgroup_empty="+(b"1" if empty else b"0")+b"|kill_issued="+(b"1" if kill_issued else b"0")+b"|pidfd_ready="+(b"1" if pid_ready else b"0")+b"|done_ns="+str(done).encode()+b"\n")
 control.send(header)
 for start in range(0,len(stdout),65535):control.send(b"O"+stdout[start:start+65535])
 for start in range(0,len(stderr),65535):control.send(b"E"+stderr[start:start+65535])
 control.send(b"P27B1_END\n")

def recovery(auth,probe,ordinal,primary,stdout,stderr,out_eof,err_eof,ticket,kill_returned,empty,pid_ready):
 body=(b"P27E001_RECOVERY_RECEIPT_V1\nAUTH_ID="+auth+b"\nPROBE="+probe+b"\nPRIMARY="+primary+b"\nDIRECT_REAP=UNAVAILABLE\nPIDFD_READY="+(b"1" if pid_ready else b"0")+b"\nSTDOUT_BYTES="+str(len(stdout)).encode()+b"\nSTDOUT_SHA256="+sha(stdout)+b"\nSTDOUT_EOF="+(b"1" if out_eof else b"0")+b"\nSTDERR_BYTES="+str(len(stderr)).encode()+b"\nSTDERR_SHA256="+sha(stderr)+b"\nSTDERR_EOF="+(b"1" if err_eof else b"0")+b"\nKILL_TICKET="+(b"1" if ticket else b"0")+b"\nKILL_WRITE_RETURNED="+(b"1" if kill_returned else b"0")+b"\nCGROUP_EMPTY="+(b"1" if empty else b"0")+b"\nDISPOSITION=CONSUMED_INDETERMINATE\nRECOVERY_END=1\n")
 durable(b"recovery-"+probe+b".v1",body)
 report=(b"P27E001_FINAL_REPORT_V1\nAUTH_ID="+auth+b"\nSUITE=P00,P01D,P01C,P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13\nENTERED_COUNT="+str(ordinal+1).encode()+b"\nPASS_COUNT="+str(ordinal).encode()+b"\nSTOP_PROBE="+probe+b"\nPRIMARY="+primary+b"\nFAULT_SET="+primary+b"\nDIRECT_REAP_COMPLETE=0\nCGROUP_EMPTY="+(b"1" if empty else b"0")+b"\nCGROUP_REMOVED=0\nSTAGE_RETAINED=1\nATTEMPT_RETAINED=1\nRETRY_ALLOWED=0\nDISPOSITION=CONSUMED_INDETERMINATE\nREPORT_END=1\n")
 try:durable(b"report.v1",report)
 except FileExistsError:pass

def receive_arm(control):
 raw,ancillary,flags,address=control.recvmsg(4096,socket.CMSG_SPACE(4))
 need(flags==0 and raw.startswith(b"ARM|") and raw.endswith(b"\n"))
 parts=raw[:-1].split(b"|")
 need(len(parts)==4 and parts[0]==b"ARM")
 pid=udec(parts[1],2);origin=udec(parts[2],1);cap=udec(parts[3],1)
 received=[]
 for level,kind,data in ancillary:
  need(level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS and len(data)==4)
  received.append(int.from_bytes(data,sys.byteorder))
 need(len(received)==1)
 return pid,origin,cap,received[0]

def main():
 need(type(sys.argv)is list and len(sys.argv)==11 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="WATCH")
 auth=h64(sys.argv[2].encode("ascii"));probe=sys.argv[3].encode("ascii");need(probe in PROBES)
 total=udec(sys.argv[4].encode("ascii"),1);cleanup=udec(sys.argv[5].encode("ascii"),1)
 out_cap=udec(sys.argv[6].encode("ascii"),1);err_cap=udec(sys.argv[7].encode("ascii"),1);ordinal=udec(sys.argv[8].encode("ascii"),0,14);expected=h64(sys.argv[9].encode("ascii"));launch_origin=udec(sys.argv[10].encode("ascii"),1)
 need(PROBES[ordinal]==probe)
 need((total,cleanup,out_cap,err_cap)==(18164800000,2000000000,3145728,3145728))
 need(sha(read_source())==expected)
 for number in range(3,10):os.fstat(number)
 control=socket.socket(fileno=7);need(control.send(b"READY\n")==6)
 remaining=launch_origin+1000000000-time.monotonic_ns();need(remaining>0);control.settimeout(max(0.001,remaining/1000000000))
 actor_lost=False;fault=b"NONE";outer_pidfd=-1;origin=0;deadline=0
 try:
  pid,origin,total_again,outer_pidfd=receive_arm(control);need(total_again==total and origin==launch_origin);control.settimeout(None)
  deadline=origin+total;need(deadline<=MAX_U63)
  need(control.send(b"ARMED\n")==6)
 except BaseException:
  actor_lost=True;fault=b"CONTROL_FAULT";deadline=time.monotonic_ns()+cleanup
 stdout=bytearray();stderr=bytearray();out_eof=False;err_eof=False;pid_ready=False
 out_over=False;err_over=False;kill_ticket=False;kill_returned=False;kill_issued=False
 poller=select.poll()
 poller.register(3,select.POLLIN|select.POLLHUP|select.POLLERR)
 poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 poller.register(7,select.POLLIN|select.POLLHUP|select.POLLERR)
 poller.register(9,select.POLLIN|select.POLLHUP|select.POLLERR)
 if outer_pidfd>=0:poller.register(outer_pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
 cleanup_deadline=0
 while True:
  now=time.monotonic_ns()
  try:events=poller.poll(10)
  except InterruptedError:events=[]
  for number,event in events:
   if number==3:
    overflow,eof=drain(3,stdout,out_cap);out_over|=overflow;out_eof|=eof
   elif number==4:
    overflow,eof=drain(4,stderr,err_cap);err_over|=overflow;err_eof|=eof
   elif number==9:
    actor_lost=True
    if fault==b"NONE":fault=b"ACTOR_LOST"
   elif number==outer_pidfd:pid_ready=True
   elif number==7 and event&(select.POLLHUP|select.POLLERR):
    actor_lost=True
    if fault==b"NONE":fault=b"ACTOR_LOST"
   elif number==7 and event&select.POLLIN:
    message=control.recv(4096)
    if message not in (b"",b"FAIL\n"):
     fault=b"CONTROL_FAULT"
    if message==b"":
     actor_lost=True
     if fault==b"NONE":fault=b"ACTOR_LOST"
    elif message==b"FAIL\n" and fault==b"NONE":fault=b"CONTROL_FAULT"
  if not out_eof:
   overflow,eof=drain(3,stdout,out_cap);out_over|=overflow;out_eof|=eof
  if not err_eof:
   overflow,eof=drain(4,stderr,err_cap);err_over|=overflow;err_eof|=eof
  if (out_over or err_over) and fault==b"NONE":fault=b"CAPTURE_OVERFLOW"
  try:empty=not populated()
  except BaseException:
   empty=False
   if fault==b"NONE":fault=b"CGROUP_FAULT"
  if fault==b"NONE" and deadline and now>deadline:fault=b"DEADLINE"
  if fault!=b"NONE" and cleanup_deadline==0:
   cleanup_deadline=now+cleanup
   if not empty:
    kill_ticket,kill_returned=kill_once(auth,probe,fault)
    kill_issued=kill_ticket and kill_returned
    if not kill_ticket and fault!=b"ACTOR_LOST":fault=b"KILL_UNKNOWN"
  if fault==b"NONE" and out_eof and err_eof and empty and pid_ready:break
  if fault!=b"NONE" and out_eof and err_eof and empty:break
  if cleanup_deadline and now>cleanup_deadline:break
 done=time.monotonic_ns()
 try:empty=not populated()
 except BaseException:empty=False
 if actor_lost:
  primary=b"ACTOR_LOST" if fault in (b"NONE",b"ACTOR_LOST") else fault
  recovery(auth,probe,ordinal,primary,bytes(stdout),bytes(stderr),out_eof,err_eof,kill_ticket,kill_returned,empty,pid_ready)
 else:
  if fault==b"NONE" and not (out_eof and err_eof and empty and pid_ready):fault=b"CGROUP_FAULT"
  send_memory(control,probe,fault,bytes(stdout),bytes(stderr),out_eof,err_eof,empty,kill_issued,pid_ready,done)
  acknowledged=False;failed=False
  ack_deadline=min(origin+total,done+500000000) if origin else done+500000000
  while time.monotonic_ns()<=ack_deadline:
   watcher=select.poll();watcher.register(7,select.POLLIN|select.POLLHUP|select.POLLERR);watcher.register(9,select.POLLIN|select.POLLHUP|select.POLLERR)
   try:events=watcher.poll(10)
   except InterruptedError:events=[]
   for number,event in events:
    if number==9:
     actor_lost=True
    elif number==7 and event&select.POLLIN:
     message=control.recv(4096)
     if message==b"ACKED\n":acknowledged=True
     elif message==b"FAIL\n":failed=True
     elif message==b"":actor_lost=True
     else:actor_lost=True
    elif number==7 and event&(select.POLLHUP|select.POLLERR):actor_lost=True
   if acknowledged or failed or actor_lost:break
  if actor_lost or (not acknowledged and not failed):
   primary=b"ACTOR_LOST" if actor_lost else b"DEADLINE"
   recovery(auth,probe,ordinal,primary,bytes(stdout),bytes(stderr),out_eof,err_eof,kill_ticket,kill_returned,empty,pid_ready)
 control.close()
 if outer_pidfd>=0:os.close(outer_pidfd)

try:
 main()
except BaseException:
 raise SystemExit(96)
raise SystemExit(0)
P27 RUNNER V1 RECOVERY SOURCE END 9B4D50F2

## 16. Literal identities and delimiter census

Raw measurement after source completion freezes:

span                         bytes  LF  SHA256
ACTOR                        49843  814  4fed500d3396a551680f941ccbe9fc910e40ff38db33e6d648473fe44c224650
RECOVERY                     10774  225  0fb76bf24a8b930b161a826123bfe9d41496577ce52481f7f1c96176524ff07c
EMBEDDED_TRANSCRIPT_VALIDATOR 10184 120  7488271ad85f0428b2b7e7ac27e966abcf246e099f3dd36b834deb780692eecd

ACTOR BEGIN count=1
ACTOR END count=1
RECOVERY BEGIN count=1
RECOVERY END count=1
EMBEDDED VALIDATOR BEGIN count=1
EMBEDDED VALIDATOR END count=1

Every span is strict ASCII/LF and ends in LF. The extraction operation is a
raw first-byte search for the unique BEGIN line plus LF and the unique END
line, with all intervening bytes retained. No language parser is involved.

## 17. Branch, callsite, authority, and consistency census

Raw literal inspection fixes this semantic branch census:

actor entry modes=1 (RUN)
recovery entry modes=1 (WATCH)
suite ordinals=15
validator PREFIX vectors=15
validator common suffix keys=10
validate_probe peer branches=15
P01C derivation branches=1
ordinary versus actor-loss watchdog partitions=2
watchdog sticky-fault tokens=7
dispositions=4 (REFUSED_NOT_CONSUMED, CONSUMED_FAIL,
CONSUMED_INDETERMINATE, PASS)
containment kill-ticket outcomes=2 (created, already exists)
direct-reap authorities for OUTER=1 (A only)
recovery direct-reap authorities=0

The raw callsite census is:

literal A os.fork callsites=1, exactly B-child
literal A raw clone3 syscall callsites=1, exactly OUTER with
CLONE_INTO_CGROUP|CLONE_PIDFD
literal A os.execve callsites=2, exactly B and OUTER
literal A os.waitpid callsites=1, centralized in wait_status for bounded
stopped-OUTER, direct-OUTER, and direct-B waits
literal A os.kill callsites=2, exactly child self-SIGSTOP and parent SIGCONT
literal A os.pidfd_open callsites=1, exactly actor pidfd for B; clone3 returns
the OUTER pidfd atomically
literal A memfd_create callsites=1, exactly OUTER
literal B fork/execve/waitpid/waitid/SIGCONT callsites=0
literal B cgroup.kill write callsites=1
literal B durable helper callsites=3, exactly kill ticket, recovery receipt,
and recovery final report
literal B populated-observation callsites=2 plus one definition
literal C validate_transcript definitions=1 and actor callsites=1

The two A exec callsites are disjoint: B receives the authenticated B memfd
and no release authority; OUTER receives the authenticated OUTER memfd and is
the sole payload entry. A contains no V15 child ownership call: all
posix_spawn and V15 child wait ownership remains inside authenticated OUTER.
B contains none of the four stage basenames and none of the source, stage,
release, semantic-parser, fork, exec, or wait APIs.

Source-to-prose consistency is exact:

prose rule                         literal construction
suite once and ordered             SUITE is one 15-tuple and main has one enumerate(SUITE) loop; the first exception leaves it permanently
budget partition                   OP_NS, LAUNCH_NS, POST_NS, ACK_NS, HOST_NS, TOTAL_NS, CLEANUP_NS are exact literals and checked at receipt
five V15 identities                SOURCE_META is the exact five-tuple and v15_sources checks every raw span plus embedded CHILD equality
nonce binding                      AUTH_ID is exact certificate SHA and is passed unchanged as argv nonce and directory component
four staged leaves                 SOURCE_NAMES has exactly four basenames and the sole stage loop zips sources[1:] with those four identities
anonymous OUTER                    one memfd call receives sources[0], four seals, and maps only to fd100
exact environment                  ENV has ten byte keys and both execve callsites receive exactly ENV
OUTER argv 20/33                   source_argv has one fixed base and appends exactly zero or thirteen P01C fields
P01D to P01C                       derive_p01c accepts only validator-returned prior rows and fresh held libc/Python observations
whole-tree containment             clone3 creates OUTER atomically in the held cgroup and cgroup.procs plus populated=1 are proved before the single SIGCONT
concurrent dual drain              B polls distinct fd3/fd4, retains separate buffers, marks overflow sticky, and drains to EOF
direct wait                        only A calls waitpid on OUTER; B observes pidfds and cgroup.events without a reap claim
one kill lane                      only B's kill_once can create kill-ticket.v1 and write 1 LF to fd6 once
complete transcript                C consumes offset zero, exact header/vector/footer/candidate/terminal, all 15 semantic branches, and dynamic identities
durable ACK                        probe_receipt writes one exclusive receipt and checks a post-fsync in-memory commit sample against both bounds
recovery nonlaunch                 B has no fork, exec, release, process-wait, extraction, staging, or PASS callsite and writes INDETERMINATE only after actor/control loss or its ARM/ACK deadline
workspace denial                   input bytes arrive on fixed FDs; child_context enters the pinned full runtime root before either exec

Authority exclusions are complete. Neither literal contains Binder,
downstream validator, E010, A000, payload selection, paper build, evidence
collection, PDF, manifest mutation, release, or Paper 28 authority. Literal A
may execute only B and exact V15 OUTER after a later authorization. Literal B
may only contain, drain, observe, ticket one kill, and report. Literal C may
only return an in-memory accepted row map or raise a closed failure. No
literal can authorize itself, its certificate, a retry, a microtest, or a
real run.

## 18. Review and microtest gates

The author and both E0364 preauthor advisors are permanently disqualified
from formal V1 review. The supervisor must independently reproduce whole-file
and source identities, prebind exactly one manifest row, and open two fresh
separated zero-write reviewers.

H41 scope is durable one-shot state, full launch context, external
actor/watchdog liveness, release barrier, deadlines, dual streams, sticky
failure, direct wait, whole-tree kill-to-empty, ACK, recovery-only nonlaunch,
and no retry at unknown-effect boundaries.

H42 scope is raw extraction/identities, sealed fd100, exclusive staging,
dependency/no-mutator binding, P00-P13 and P01D/P01C provenance, complete
parser/semantics, caps, access denial, exact effects, and absence of
parser/recovery authority escalation.

Even later dual formal static PASS may open only separately authored and
reviewed synthetic no-build runner microtests for FD scrub, dual streams,
timeout, cgroup kill-to-empty, report truncation, actor loss, and B nonlaunch.
It cannot authorize literal A or B against real V15, any real suite slot,
payload, Binder, validator, E010, A000, stage/root, build/evidence, PDF, or
release.

## 19. Author-side zero-effect closure

During this authorship the only filesystem effect is apply_patch creation and
modification of this exact V1 path. No other path is written. No temporary,
cache, backup, log, lock, swap, redirected output, manifest, or generated
file exists. Forbidden build/evidence-root access is zero. Git, glob, find,
directory listing, and sibling discovery are zero.

Literal import, language tokenization, AST parsing, compilation, evaluation,
execution, launch, microtest, and validator-process counts are zero. No
cgroup, /tmp stage, durable attempt, authored-literal process, runtime signal,
pipe, memfd, mount, namespace, chroot, capability, receipt, report, ACK,
payload, paper, PDF, or release effect occurred.

This author-stop claims only an inert normative control. It does not claim
formal review PASS, runtime correctness, premise truth, microtest authority,
execution authority, or release authority.

BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V1_AUTHOR_STOP
