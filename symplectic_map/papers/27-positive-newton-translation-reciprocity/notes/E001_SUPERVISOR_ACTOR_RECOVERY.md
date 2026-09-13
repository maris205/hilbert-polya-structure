# E001 supervisor actor and one-shot recovery control

## 1. Authority, scope, and inertness

This file is an inert control specification. It creates no execution authority.
It does not run, import, parse, compile, evaluate, or otherwise activate the V8
marker program, the payload marker program, the launcher, the inner command, a
supervisor, a watchdog, a recovery binder, a fixture, a probe, or any build
operation. It performs no credential access, network access, temporary-file
operation, PTY operation, shell operation, or repository mutation. All process
and append verbs below are requirements on a later separately authorized actor,
not actions performed by this author stop.

The sole authoring authority is E0331 of BATCH_07_STATUS.md. The exact E0331
whole-ledger anchor is:

- path: /root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md;
- device 2431, inode 12439253869, mode 0644, link count 1, uid 0, gid 0;
- 1848081 bytes, 20661 LF bytes;
- SHA-256 72d732c9834c7670f22160e73c0391c668f40d271e4fdf1aba986b24217c6b30;
- terminal bytes, including LF, are
  BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V8_DUAL_STATIC_PASS_CONSUMED_AND_ACTOR_DERIVATION_HOST_CONTROL_AUTHORIZED\n;
- terminal hex is
  424154434830375f5032375f50524f42455f5245434f564552595f453030315f53555045525649534f525f42494e4445525f56385f4455414c5f5354415449435f504153535f434f4e53554d45445f414e445f4143544f525f44455249564154494f4e5f484f53545f434f4e54524f4c5f415554484f52495a45440a.

The E0331 terminal authority is exactly
BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V8_DUAL_STATIC_PASS_CONSUMED_AND_ACTOR_DERIVATION_HOST_CONTROL_AUTHORIZED.
E0331 grants only this inert actor control and later manifest binding and
separated static review. Actor execution, recovery-binder execution, host
probing, fixtures, microtests, build access, evidence access, validator
execution, PDF production, release, and retry remain unauthorized.

This control consumes no authority from a visible result line, a process exit
code, a payload PASS line, or the V8 static PASS. Every acceptance below is a
conjunction. Every failure is sticky and can only reduce authority.

## 2. Frozen inputs and minimum binding

The only supervisor/binder is the frozen V8 whole file:

- path:
  /root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_BINDER_RECOVERY_V8.md;
- device 2431, inode 5917339790, mode 0644, link count 1, uid 0, gid 0;
- 279288 bytes, 7303 LF bytes;
- SHA-256 3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4;
- terminal bytes BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V8_AUTHOR_STOP\n.

Its unique marker transport is frozen without executing it:

- begin marker:
  BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V8_PROGRAM_BEGIN\n;
- end marker:
  BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V8_PROGRAM_END\n;
- raw transport is the byte substring after the unique begin-marker LF through
  the delimiter LF immediately before the unique end marker;
- raw identity: 251415 bytes, 6840 LF bytes, SHA-256
  6d512ac7480a521029203bfcf62a33600c3842eca0b422bf9fea1e577c75a74d;
- normalized transport is raw with its single final LF removed;
- normalized identity: 251414 bytes, 6839 LF bytes, 6840 physical lines,
  SHA-256 34449280b51dae17eeb5eb841296e99d25512867185525fec39dc73a39dfc076;
- normalized final byte decimal 41;
- normalized apostrophe, dollar, and backtick census 0, 0, and 0.

The frozen V7 predecessor remains an input to V8 and is not superseded:

- path:
  /root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_BINDER_RECOVERY_V7.md;
- device 2431, inode 5913770328, mode 0644, link count 1, uid 0, gid 0;
- 275366 bytes, 7207 LF bytes;
- SHA-256 0cf0749145ebb4f87d949f6ea787a47494876d8303ab2f09369a164dc3d115e3;
- terminal bytes BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V7_AUTHOR_STOP\n.

The later actor MUST first bind a complete current ledger prefix C0 on the
same E0331 device and inode. C0 may be a strict append-only extension of E0331
created by later authorized control binding and reviews. C0 MUST satisfy all
of the following:

1. regular file, mode 0644, link count 1, uid 0, gid 0, device 2431, inode
   12439253869;
2. canonical supplied C0 byte count in [1848081, 16777216], LF count in
   [20661, 200000], 64-lowercase-hex SHA-256, and even lowercase terminal hex
   decoding to 1 through 512 bytes ending in exactly one LF and containing no
   NUL;
3. a complete read of exactly C0 bytes has the supplied LF count, hash, and
   terminal;
4. its first 1848081 bytes have the exact E0331 LF count, hash, and terminal;
5. repeated held-fd, path, and fresh-fd metadata and byte checks agree before
   spawn; no suffix beyond C0 exists at the start of a new attempt;
6. a single-writer exclusive ledger lease is held until the final append has
   been reread and made durable.

The exact eleven-field V8 Binding, in argv order, is:

1. 2431
2. 5917339790
3. 279288
4. 7303
5. 3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4
6. 2431
7. 12439253869
8. C0_BYTES
9. C0_LF
10. C0_SHA256
11. C0_TERMINAL_HEX

The last four symbolic values are the canonical C0 values just independently
validated. The V8 E0329 minimum anchor is therefore retained internally, and
this actor adds the stronger E0331 minimum anchor. No later ledger suffix can
weaken either prefix.

## 3. Later host premises and actor implementation boundary

Execution remains closed until a later ledger event separately establishes
all of these premises without using a production payload:

- exact CPython 3.12 and the frozen Python executable chain;
- the exact libc posix_spawn file-action and setsid behavior used below;
- RLIMIT_NOFILE soft 4096 and hard 1048576 and a complete high-FD census;
- empty signal mask and default dispositions for every valid catchable signal;
- O_NOFOLLOW, O_CLOEXEC, O_NOATIME, O_APPEND, fsync, held-inode, and
  append-only durability behavior on this filesystem;
- a non-PTY actor stdin, stdout, and stderr, each a distinct binary pipe;
- timely SIGKILL and waitpid outside uninterruptible kernel sleep;
- no adversarial PID or PGID reuse from supervisor spawn through the final
  fourth absence check;
- single-writer ledger exclusion and crash recovery able to read the durable
  actor journal;
- no actor crash while it owns direct-child wait authority, except a complete
  host restart that destroys the process group and leaves the durable journal
  available.

The later actor implementation MUST be a literal, separately frozen CPython
program whose only imports are errno, fcntl, hashlib, os, resource, select,
signal, stat, sys, and time. Its API allowlist is:

- bytes and ASCII conversion, bounded bytearray, tuple, list, dict, set, int,
  len, range, min, max, sorted, and deterministic exception handling;
- hashlib.sha256;
- os.open, close, read, write, pread, fstat, stat, fsync, pipe2, dup, killpg,
  getsid, getpgid, getpid, getpgrp, waitpid, posix_spawn, set_blocking,
  getcwd/getcwdb, geteuid, getegid, umask, and _exit;
- os.POSIX_SPAWN_DUP2 and os.POSIX_SPAWN_CLOSE file actions;
- fcntl.fcntl for F_GETFD and F_DUPFD_CLOEXEC and fcntl.flock for a nonblocking
  exclusive ledger lease;
- resource.getrlimit;
- select.poll;
- signal.valid_signals, pthread_sigmask, signal, SIG_DFL, SIG_BLOCK,
  SIG_SETMASK, SIGKILL, and SIGSTOP;
- stat predicates and mode extraction;
- sys.argv, sys.orig_argv, sys.flags, sys.implementation, and sys.version_info;
- time.monotonic_ns only.

Everything not listed is forbidden. In particular there is no fork, vfork,
subprocess, preexec hook, ctypes, prctl, dynamic import, eval, exec, compile,
marshal, pickle, temporary file, rename, unlink, truncate, repair, shell,
PTY, terminal, tee, socket, credential, network, environment inheritance,
glob, directory walk, build-path open, evidence-path open, payload parse,
second supervisor, second payload, or retry API. Safe continuation of an
interrupted read, write, poll, or wait syscall is not an attempt retry.

The actor normalizes and verifies the exact ten-key environment:

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

It also verifies cwd /root/autodl-tmp/symplectic_map, euid and egid zero,
umask 077, CPython 3.12, flags -S -B -P, no site, no bytecode, safe path,
UTF-8 mode, non-isolated exact-environment behavior, the declared rlimits,
and exactly fds 0, 1, and 2 at entry. Those fds are three distinct FIFOs with
FD_CLOEXEC clear. The actor never reads external instructions after entry.

## 4. Exact actor invocation and frozen supervisor invocation

The later actor invocation is one exact argv vector:

/root/miniconda3/bin/python3
-S
-B
-P
-c
ACTOR_NORMALIZED_PROGRAM_BYTES
start
ACTOR_NORMALIZED_PROGRAM_SHA256
C0_BYTES
C0_LF
C0_SHA256
C0_TERMINAL_HEX

ACTOR_NORMALIZED_PROGRAM_BYTES is passed as one argv element, not through a
shell, file, environment variable, or temporary object. The program compares
its ASCII bytes, SHA-256, apostrophe/dollar/backtick census, sys.argv, and
sys.orig_argv to this vector before opening the ledger. The four C0 fields use
the grammar in section 2. A later separately frozen crash-recovery entry may
replace start by recover but MUST use the same actor bytes and the C0 identity
recorded in the durable journal. Recover can never enter the spawn state.

The exact direct supervisor argv is:

/root/miniconda3/bin/python3
-S
-B
-P
-c
V8_NORMALIZED_PROGRAM_BYTES
supervisor
2431
5917339790
279288
7303
3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4
2431
12439253869
C0_BYTES
C0_LF
C0_SHA256
C0_TERMINAL_HEX

Every displayed line is exactly one argv byte string in that order.
V8_NORMALIZED_PROGRAM_BYTES is obtained only by the unique delimiter
extraction and identity checks in section 2. It is never shell-quoted or
written to a file. The executable is passed as both posix_spawn path and
argv[0]. The environment is exactly the ten-key map above. posix_spawn uses
setsid=true, setsigmask=(), and setsigdef equal to the ascending tuple of all
valid signals other than SIGKILL and SIGSTOP.

The one permitted recovery-binder argv replaces supervisor by
recovery-binder and appends exactly two elements after the Binding:

KNOWN_PGID
consumed

It uses the same exact V8 normalized bytes, executable, Binding, environment,
signal tuple, and no shell. It is not a payload and has no path to spawn one.

## 5. Five actor-owned pipes and file actions

Before direct spawn the actor creates exactly five independent binary pipes
with pipe2(O_CLOEXEC | O_NONBLOCK). It relocates every end with
F_DUPFD_CLOEXEC to a distinct fd at or above 20, closes the originals, and
proves all ten pipe node identities are pairwise distinct. No pipe is a PTY,
socket, regular file, or alias. The roles are:

| Role | Actor-retained end | Supervisor end |
| --- | --- | --- |
| ACK input | write | fd 0 read |
| result stdout | read | fd 1 write |
| external stderr | read | fd 2 write |
| live-empty payload stdin | write | fd 3 read |
| launch release | write | fd 4 read |

The child file actions first DUP2 the five supervisor ends to 0, 1, 2, 3,
and 4 in that order, then CLOSE every one of the ten relocated source fds.
The child therefore enters with exactly fds 0 through 4, each FD_CLOEXEC
clear and each a different pipe. The actor closes all five child ends
immediately after posix_spawn returns and retains exactly the five ends in the
table. The result and stderr readers are registered independently with poll
before any release byte is written. The ACK and release writers are blocking
only for their single-byte writes. Payload stdin is never written.

The recovery binder uses three new independent pipes. Its stdin read end is
fd 0 and its actor writer is closed without a write before spawn returns to
the drain loop; result stdout is fd 1 and external stderr is fd 2. File
actions and closure rules are the same. The recovery binder is a direct actor
child, is independently waited, and cannot inherit any direct-attempt pipe.

## 6. Checked clocks, caps, and sticky observations

All times are monotonic unsigned 64-bit nanoseconds. checked_add(a,b) first
requires 0 <= a <= 2^64-1 and 0 <= b <= 2^64-1-a. Overflow is permanent
failure; there is no saturated success interpretation.

The actor samples A0 exactly once immediately before direct posix_spawn and
freezes AEND = checked_add(A0, 420000000000). It never moves or recomputes
AEND. It samples L0 immediately after verified SID/PGID topology and freezes
LEND = min(AEND, checked_add(L0, 30000000000)). Exact L and its EOF must be
completed before LEND. The BEGIN-provided ACK deadline is immutable and A
plus EOF must complete before both that deadline and AEND. No timeout bit can
be cleared.

On a failure requiring cleanup, K0 is sampled once immediately before the
first SIGKILL attempt and KEND = min(AEND, checked_add(K0,5000000000)). The
direct supervisor wait and first group-absence proof must complete before
KEND. The one recovery entry samples Q0 immediately before its posix_spawn
and freezes QEND = checked_add(Q0,60000000000). Recovery wait, both EOFs,
validation, and its terminal group-absence proof must complete before QEND.

Every read samples time once immediately after the syscall. Every waitpid
samples time once immediately after waitpid. Records are immutable. EINTR,
EAGAIN, poll errors, read errors, wait errors, late observations, impossible
ownership, duplicate EOF, and counter overflow latch failure. A physical reap
is retained even when late. No late record is relabeled timely.

The exact caps are:

- BEGIN line: 4096 bytes including LF;
- V8 RESULT line: 1310720 bytes including LF;
- total direct stdout: 1314816 bytes and exactly two LF bytes;
- direct external stderr: 65536 bytes; direct success requires zero;
- recovery stdout: 1310720 bytes and exactly one LF;
- recovery external stderr: 65536 bytes; valid recovery requires zero;
- each actor journal record: 4096 bytes and exactly one LF;
- total actor journal suffix: 16384 bytes and at most four records;
- actor final stdout line: 4096 bytes and exactly one LF;
- actor stderr: zero bytes for every classified exit.

Reads continue after any failure until EOF, cap, or the applicable sticky
deadline so pipe pressure cannot hide causality. Once a cap would be exceeded,
the actor latches overflow, retains byte count, LF count, SHA-256, and the
bounded prefix, closes no read end early, and continues count/hash draining
through EOF. A cap violation permanently forbids direct or recovery validity.

## 7. Durable state machine and ACK ambiguity

The attempt identifier is the lowercase SHA-256 of the exact ASCII framing

E001-SUPERVISOR-ACTOR-V1\n
C0_SHA256\n
V8_WHOLE_SHA256\n
V8_NORMALIZED_SHA256\n

where the symbolic hashes are replaced by their 64 ASCII hex bytes. It is
deterministic for the sole C0/V8 attempt and is not a credential or nonce.

The ledger is an append-only crash journal. Each record is one canonical
ASCII line with exactly these space-separated fields and no extra field:

ACTOR_JOURNAL E001_SUPERVISOR_ACTOR_RECOVERY version=1 state=STATE attempt_id=HEX64 parent_bytes=U64 parent_LF=U64 parent_sha256=HEX64 base_bytes=C0_BYTES base_LF=C0_LF base_sha256=C0_SHA256 pgid=PGID consumed=BIT ack_state=ACK_STATE direct_state=DIRECT_STATE recovery_state=RECOVERY_STATE outcome=OUTCOME detail=TOKEN\n

STATE is one of SPAWNED, PENDING_ACK, ACK_CLOSED, FINAL_SUCCESS, or
FINAL_FAILURE. ACK_STATE is not-armed, armed-ambiguous, or closed. The state
and permitted values are:

| State | consumed | ack_state | Required meaning |
| --- | --- | --- | --- |
| SPAWNED | 0 | not-armed | PID, SID, and PGID equal PGID; no L byte yet |
| PENDING_ACK | 1 | armed-ambiguous | exact BEGIN valid; no ACK write call yet |
| ACK_CLOSED | 1 | closed | exact A write returned one and actor closed writer |
| FINAL_SUCCESS | 1 | closed | complete success conjunction and durable terminal state |
| FINAL_FAILURE | 1 | armed-ambiguous or closed | permanent failure; never retry |

Every record carries the byte count, LF count, and SHA-256 of the complete
ledger immediately before that record. The actor performs one O_APPEND write,
requires its exact full length, fsyncs the held ledger fd, rereads the complete
expected prefix, verifies the appended bytes and final metadata by held fd,
path, and fresh fd, and only then changes in-memory state. A partial write,
fsync error, metadata drift, interleaving, or reread mismatch is not repaired
or truncated. It stops authority.

After posix_spawn returns, the actor proves direct PID > 1 and exact
getsid(PID) = getpgid(PID) = PID before release. It durably appends SPAWNED
with that PGID before any L byte. It then writes exactly L and closes the
release writer, drains R-derived BEGIN as specified below, and durably appends
PENDING_ACK with consumed=1 and ack_state=armed-ambiguous. Only after the
PENDING_ACK fsync and complete reread may the actor enter the ACK write call.
Thus the consumed bit and known PGID are durable before the first ACK byte can
possibly be written.

The first entry to the one-byte ACK write call is the ambiguity boundary.
Return one followed by successful close permits ACK_CLOSED to be appended.
EINTR may repeat a safe one-byte syscall, but the durable state remains
armed-ambiguous until close is proved. Short write, error, close error, crash,
or missing ACK_CLOSED is permanently consumed. No path returns to SPAWNED or
PENDING_ACK and no path creates a second supervisor or payload.

A later recover entry reads C0 plus the complete journal. FINAL_SUCCESS and
FINAL_FAILURE are terminal and cause no action. SPAWNED, PENDING_ACK, or
ACK_CLOSED can only enter recovery. A malformed or partial journal suppresses
all retry; if a complete SPAWNED prefix exposes the canonical PGID, that PGID
is killed and absence-proved. PENDING_ACK and ACK_CLOSED conclusively prove
consumption. A host restart makes any missing direct wait/status permanently
invalid; it never fabricates a status. The exact V8 recovery binder is invoked
once only after group absence, and FINAL_FAILURE is then appended if the
journal remains appendable. No journal byte is rewritten.

## 8. Exact release, ready, BEGIN, ACK, and internal start order

The causal order is strict:

1. direct posix_spawn with setsid=true returns PID;
2. actor verifies PID = SID = PGID and durably appends SPAWNED;
3. actor writes exact byte L and closes the release pipe, proving EOF;
4. supervisor consumes L plus EOF, performs preflight, and spawns watchdog;
5. watchdog writes internal exact R and EOF to the supervisor;
6. supervisor validates R, topology, and emits one exact BEGIN line on fd 1;
7. actor continuously drains both fd 1 and fd 2, validates the entire BEGIN,
   and durably appends PENDING_ACK;
8. actor writes exact byte A and closes ACK, proving EOF;
9. supervisor consumes A plus EOF and writes internal exact S to watchdog;
10. watchdog may then enter payload work once; no earlier step can spawn it.

R and S are internal V8 pipe tokens. The actor never claims to observe either
directly. A valid entire BEGIN is the only external evidence that the
supervisor accepted R. A valid final V8 RESULT plus supervisor zero exit is
the only external evidence that the supervisor completed its S/watchdog
lifecycle. The actor does not invent separate R or S observations.

The BEGIN must be the first direct stdout line and match this exact field
order, with one ASCII space between tokens and one terminal LF:

BEGIN E001_SUPERVISOR_BINDER_RECOVERY version=8 supervisor_pid=PID watchdog_pid=WATCHDOG session_sid=PID session_pgid=PID watchdog_pgid=PID program_bytes=251414 program_LF=6839 program_sha256=34449280b51dae17eeb5eb841296e99d25512867185525fec39dc73a39dfc076 whole_control_binding=actor-attested self_dev=2431 self_ino=5917339790 self_bytes=279288 self_LF=7303 self_sha256=3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4 ledger_dev=2431 ledger_ino=12439253869 ledger_prefix_bytes=C0_BYTES ledger_prefix_LF=C0_LF ledger_prefix_sha256=C0_SHA256 ledger_prefix_terminal_hex=C0_TERMINAL_HEX payload_sha256=6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0 launcher_sha256=72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd inner_sha256=e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f actor_overall_deadline_ns=420000000000 ready_guard_origin=immediately-before-watchdog-spawn ready_deadline_ns=READY_ACK_U64 ack_guard_origin=immediately-before-begin ack_deadline_ns=ACK_U64 actor_deadline_semantics=sticky-external attempt_consumed=0\n

PID and WATCHDOG are canonical decimal integers in [2,2147483647], distinct
from each other. PID is the direct posix_spawn return. The actor repeats
getsid(WATCHDOG) = getpgid(WATCHDOG) = PID before ACK. READY_ACK_U64 and
ACK_U64 are canonical unsigned decimals, READY_ACK_U64 < ACK_U64,
monotonic_ns() < ACK_U64, and ACK_U64 <= AEND. Every fixed, Binding, payload,
launcher, inner, origin, and semantic value is byte-equal to the line above.
No duplicate key, extra key, blank value, CR, NUL, non-ASCII byte, extra LF,
or prefix-only match is valid.

## 9. Independent draining, direct wait, and containment

The result and stderr pipes are independently nonblocking and registered from
before L until their own first EOF. Every poll cycle services all ready fds
before a WNOHANG wait observation; every loop also performs a wait observation
when no fd is ready. A busy stdout cannot starve stderr, a busy stderr cannot
starve stdout, and an early direct wait cannot stop either drain. The first
zero-length read freezes an EOF record with stream, governing deadline,
post-read time, and timeliness. Duplicate EOF or bytes after a recorded EOF
are impossible states and permanent failure.

The actor alone calls waitpid on the direct supervisor PID. It retains the
raw wait status and first post-wait time. ECHILD, another PID, interruption
not safely resumed, wait error, late status, signaled status, stopped status,
continued status, or nonzero exit is invalid. Draining continues through both
EOFs even after a valid wait. Direct completion requires status and both EOFs
before AEND.

Payload stdin remains live and empty from pipe creation until containment is
resolved. It is never polled for readability and never receives a byte. On a
candidate direct completion the actor checks killpg(PID,0) exactly once and
requires errno ESRCH. It then closes the payload-stdin writer, checks ESRCH a
second independent time, and only then may validate terminal inputs. A live
or uncertain group enters cleanup, not success.

Cleanup sends at most one SIGKILL to the exact known PGID, never to an
unbound numeric PID. Success or ESRCH is retained. The actor continuously
drains both streams while it directly waitpid-reaps the supervisor before
KEND. It closes payload stdin only after the group is absent. It then requires
two independent killpg(PGID,0) calls to return ESRCH. No signal is sent after
an uncertain ownership observation. The no-PID-reuse host premise covers the
entire interval.

## 10. Frozen V8 RESULT grammar

After the BEGIN line, direct stdout must contain exactly one V8 RESULT line
and EOF. Recovery stdout must contain exactly one V8 RESULT line and EOF. A
full-layout RESULT has the exact prefix

RESULT E001_SUPERVISOR_BINDER_RECOVERY version=8

and then exactly these keys in this order:

mode, recovery_pgid, attempt_consumed, payload_spawned, payload_pid,
capture_state, capture_complete, payload_deadline_ns,
payload_deadline_origin, kill_reap_deadline_ns,
kill_reap_deadline_origin, stream_eof_deadline_ns,
stream_eof_deadline_origin, payload_wait_outcome, payload_wait_origin,
payload_wait_guard_deadline_ns, payload_wait_called,
payload_wait_observed_ns, payload_wait_physical_reap,
payload_wait_timely, payload_wait_raw_status,
payload_wait_stream_eof_deadline_ns, payload_wait_error_token,
kill_wait_outcome, kill_wait_origin, kill_wait_guard_deadline_ns,
kill_wait_called, kill_wait_observed_ns, kill_wait_physical_reap,
kill_wait_timely, kill_wait_raw_status, kill_wait_stream_eof_deadline_ns,
kill_wait_error_token, reap_origin, stdout_eof_stream, stdout_eof_phase,
stdout_eof_guard_deadline_ns, stdout_eof_observed_ns, stdout_eof_timely,
stderr_eof_stream, stderr_eof_phase, stderr_eof_guard_deadline_ns,
stderr_eof_observed_ns, stderr_eof_timely, payload_deadline_fired,
kill_reap_deadline_fired, stream_eof_deadline_fired,
payload_wait_observed, payload_wait_timely, kill_reap_wait_observed,
kill_reap_wait_timely, stdout_eof_observed, stderr_eof_observed,
child_reaped, kill_sent, payload_success, supervisor_lost, timeout,
wait_provenance, stream_provenance, wait_available, streams_available,
stdout_overflow, stderr_overflow, stdout_close_error, stderr_close_error,
lifeline_close_error, capture_errors, capture_errors_truncated, wait_raw,
wait_kind, exit_code, signal, core, stdout_eof, stderr_eof, stdout_bytes,
stdout_stored_bytes, stdout_LF, stdout_sha256, stdout_hex_kind, stdout_hex,
stderr_bytes, stderr_stored_bytes, stderr_LF, stderr_sha256,
stderr_hex_kind, stderr_hex, recovery_esrch_initial,
recovery_esrch_pre_evidence, recovery_esrch_terminal, binder_status,
durability_phase, binder_bytes, binder_LF, binder_sha256, binder_hex,
internal_close_error, close_failure_sites, close_failure_sites_truncated,
whole_control_binding, executable_binding, actor_deadline_ns,
actor_deadline_semantics, disposition.

Every item is exactly key=value, ASCII, nonempty, and separated by one space;
there are no duplicate or unknown keys. Decimal values are canonical and
within unsigned 64-bit range. Bits are exactly 0 or 1. SHA values are exactly
64 lowercase hex. A present hex blob is lowercase, even length, and decodes
to exactly its declared stored byte count. The actor recomputes byte count,
LF count, and SHA-256 from decoded stdout, stderr, and binder blobs. For
hex_kind=full, stored bytes equal total bytes; prefix is never accepted for
success. none and unavailable are accepted only in the exact context where
V8 defines them. capture_errors and close_failure_sites are finite canonical
comma lists or none. The whole line has exactly one LF and no CR or NUL.

The short schema-layout=overflow RESULT is valid only as a classified
PERMANENT_FAILURE. It has exact ordered fields mode, attempt_consumed,
payload_success, schema-layout, disposition, observed_bytes, and
observed_sha256. It can never validate direct success or recovery-binder
completeness.

## 11. Direct SUCCESS conjunction and T/S/EOF arithmetic

Direct SUCCESS requires every condition below. Missing one condition is
permanent failure.

- complete valid BEGIN, PENDING_ACK durable before A, ACK_CLOSED durable after
  A plus EOF, no actor error, and A completed before both sticky deadlines;
- direct stdout has exactly BEGIN plus one full-layout RESULT plus EOF within
  cap; external stderr has exactly zero bytes plus EOF; direct supervisor is
  directly reaped with WIFEXITED and WEXITSTATUS zero before AEND;
- RESULT mode=watchdog, recovery_pgid=none, attempt_consumed=1,
  payload_spawned=1, capture_state=COMPLETE, capture_complete=1,
  payload_success=1, disposition=SUCCESS;
- payload_pid is canonical and distinct from supervisor and watchdog;
- payload_wait_outcome=reaped, payload_wait_origin=payload-wait,
  payload_wait_called=1, payload_wait_physical_reap=1,
  payload_wait_timely=1, payload_wait_error_token=none;
- kill wait fields are none, kill_reap_deadline_ns=none,
  kill_reap_wait_observed=0, kill_reap_wait_timely=0, kill_sent=0;
- every deadline-fired bit, supervisor_lost, timeout, overflow, stream close,
  lifeline close, capture error, capture truncation, internal close, and close
  failure bit is zero; close_failure_sites=none;
- wait_provenance=watchdog-waitpid-authoritative,
  stream_provenance=watchdog-separate-raw-pipes, wait_available=1,
  streams_available=1;
- wait_raw=0, wait_kind=exit, exit_code=0, signal=none, core=0,
  child_reaped=1, reap_origin=payload-wait;
- stdout_eof=1, stderr_eof=1, stdout_eof_observed=1,
  stderr_eof_observed=1, and both EOF timely values are 1;
- binder_status=not-run, durability_phase=not-applicable, binder_bytes=0,
  binder_LF=0, binder_sha256 equals the SHA-256 of empty bytes,
  binder_hex=none;
- whole_control_binding=actor-attested,
  executable_binding=marker-self-bound,
  actor_deadline_ns=420000000000,
  actor_deadline_semantics=sticky-external;
- recovery_esrch_initial, recovery_esrch_pre_evidence, and
  recovery_esrch_terminal are all na.

Let T be payload_wait_observed_ns and let S be both
payload_wait_stream_eof_deadline_ns and stream_eof_deadline_ns. The actor
performs checked_add(T,1000000000) and requires exact equality to S. It does
not resample time for S. Each stream EOF independently satisfies exactly one
of these alternatives:

- phase PAYLOAD_WAIT, guard payload_deadline_ns, observed_ns <= T; or
- phase STREAM_EOF, guard S, T <= observed_ns < S.

KILL_REAP is never a success phase. Stream tags must be stdout and stderr in
their respective slots. All observation decimals are canonical u64.

The decoded internal payload stdout is exactly 308 bytes, one LF, SHA-256
b149a22827939aff6a6875a4797076a7e32f8ada246dee0e2f3a7aa490247c5b,
hex_kind=full, and byte-equal to:

PASS E001_FIRST_COPY_RECOVERY evidence_dev=2431 evidence_ino=14502900794 copy_bytes=398310 copy_LF=9366 copy_sha256=6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817 inventory_items=4 inventory_framing_bytes=64 inventory_sha256=7aeb029ca886a47abeb0bd05a4f941c820983dc6e90925880ff7e297f92dbcde\n

The decoded internal payload stderr is exactly zero bytes, zero LF,
hex_kind=full, SHA-256
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
and empty hex. These internal stream claims do not replace the independently
observed external stdout, external stderr, or direct wait.

## 12. Permanent failure and one recovery-binder invocation

A valid direct full-layout PERMANENT_FAILURE is itself the frozen V8 binder
result. The actor validates its full grammar, blob hashes, EOFs, direct status,
and group absence, then appends FINAL_FAILURE. It does not run a second binder
and never retries the payload.

For ACK ambiguity, invalid or missing BEGIN after a spawned supervisor,
invalid or missing RESULT, invalid status, missing EOF, nonempty external
stderr, deadline, overflow, close failure, or invalid containment, the actor
does all of the following exactly once:

1. latches consumed=1 and never clears it;
2. kills the exact known group if still present, directly reaps the supervisor
   while continuously draining, and proves the group absent twice;
3. closes live-empty payload stdin only after absence;
4. invokes the exact V8 recovery-binder argv once, with the known PGID and
   consumed token, under QEND;
5. independently drains recovery stdout and stderr through EOF, directly
   waits the recovery process, and validates its report;
6. proves the original known group absent again immediately before the final
   append;
7. appends FINAL_FAILURE and never enters spawn again.

If direct-child ownership cannot be affirmatively reaped, group absence cannot
be proved, or a safe signal predicate is unavailable, the actor does not send
an unbound signal and does not pretend cleanup succeeded. The attempt remains
permanently consumed. The later crash-recovery host must finish absence under
its separately proved restart premise before the one recovery binder. There
is still no second supervisor, payload, repair, evidence reuse, or retry.

A valid recovery report requires one full-layout RESULT and EOF, zero external
stderr and EOF, direct recovery-process WIFEXITED/WEXITSTATUS zero, and:

- mode=recovery-binder, recovery_pgid exactly KNOWN_PGID,
  attempt_consumed=1, disposition=PERMANENT_FAILURE, payload_success=0;
- payload_spawned, payload_pid, capture_state, capture_complete, all payload,
  kill, stream, wait, EOF, deadline, counter, hash, and hex capture fields are
  exactly the V8 recovery unavailable values;
- supervisor_lost=1, wait_provenance=unavailable-recovery,
  stream_provenance=unavailable-recovery, wait_available=0,
  streams_available=0;
- recovery_esrch_initial=1, recovery_esrch_pre_evidence=1, and
  recovery_esrch_terminal=1;
- capture_errors contains watchdog-report-lost and obeys the fixed V8 grammar;
- binder_status is ok or error, durability_phase=unknown-mismatch,
  binder_bytes in [1,589824], binder_LF consistent, binder_sha256 correct,
  binder_hex lowercase/even and exactly decodable to binder_bytes;
- decoded binder begins with the exact recovery-binder mode header, contains
  exactly one canonical PROVENANCE line with unavailable-recovery wait and
  stream provenance, and ends with exact BINDER_END\n;
- internal_close_error=0, close_failure_sites=none,
  close_failure_sites_truncated=0;
- whole_control_binding=actor-attested,
  executable_binding=marker-self-bound,
  actor_deadline_ns=60000000000,
  actor_deadline_semantics=sticky-external.

An invalid, absent, nonzero-status, non-EOF, nonempty-stderr, overflow, late,
or containment-invalid recovery is recorded as recovery_state=invalid. It is
never invoked again. A report cannot be repaired, concatenated, borrowed from
the direct run, or accepted from a prior attempt.

## 13. Terminal revalidation and durable final append

Immediately before any FINAL record, the actor reopens and revalidates the
entire V8 whole file and uniquely extracts and hashes its marker transport
again. It revalidates the held and path ledger as exactly C0 plus the actor
journal records already written, including every parent identity. It rereads
the first 1848081 bytes and repeats the E0331 anchor checks. It verifies the
current ledger has no foreign or partial suffix and that the exclusive lease
still belongs to this actor.

FINAL_SUCCESS is permitted only after the complete direct SUCCESS conjunction,
two group-absence proofs, payload-stdin closure, terminal V8 and ledger
revalidation, and no recovery invocation. Its fields use direct_state=valid,
recovery_state=not-run, outcome=SUCCESS, and detail=none.

FINAL_FAILURE is used for every consumed non-success after the strongest safe
cleanup available. It records direct_state as valid-failure, invalid, missing,
or unavailable; recovery_state as valid, invalid, blocked, or not-run; outcome
as PERMANENT_FAILURE; and one token from this frozen detail set:

begin, ack, deadline, direct-report, direct-status, direct-eof,
direct-stderr, direct-overflow, containment, cleanup, recovery-report,
recovery-status, recovery-eof, recovery-stderr, recovery-overflow,
terminal-drift, ledger-durability, crash-resume, or unexpected.

The final line is appended, fsynced, completely reread, and verified by held,
path, and fresh descriptors. The final current-ledger byte count, LF count,
SHA-256, and terminal line are then frozen for the actor output. A final append
failure cannot be called durable and cannot yield actor SUCCESS.

## 14. Exact actor output and status grammar

After a verified durable final append the actor writes exactly one line to its
own stdout and closes stdout. It writes no stderr. The exact field order is:

ACTOR_RESULT E001_SUPERVISOR_ACTOR_RECOVERY version=1 attempt_id=HEX64 state=FINAL_SUCCESS_OR_FINAL_FAILURE consumed=1 pgid=PGID direct_stdout_bytes=U64 direct_stdout_LF=U64 direct_stdout_sha256=HEX64 direct_stderr_bytes=U64 direct_stderr_LF=U64 direct_stderr_sha256=HEX64 direct_wait_raw=U64_OR_NONE direct_stdout_eof=BIT direct_stderr_eof=BIT group_absent=BIT recovery_invoked=BIT recovery_valid=BIT_OR_NA ledger_bytes=U64 ledger_LF=U64 ledger_sha256=HEX64 disposition=SUCCESS_OR_PERMANENT_FAILURE detail=TOKEN\n

All decimals and bits are canonical, hashes lowercase, tokens from the frozen
sets, and the line is at most 4096 bytes. No additional stdout or stderr byte
is permitted. Exit status is exactly 0 only for FINAL_SUCCESS with
disposition=SUCCESS and every success conjunction. Exit status is exactly 1
for a durable FINAL_FAILURE. Exit status 2 is reserved for a pre-spawn invalid
invocation or invalid C0 for which no journal record was appended; its stdout
is the same grammar with state=FINAL_FAILURE, consumed=0, pgid=none, unavailable
direct fields encoded as zero/none, recovery_invoked=0, recovery_valid=na,
disposition=PERMANENT_FAILURE, and detail=terminal-drift. A crash can have no
output and is resolved only from the journal.

No ACTOR_RESULT line, including a syntactically valid one, is authoritative
without independent confirmation of its exit status, stdout EOF, empty stderr
EOF, final ledger bytes, terminal V8 identity, and process-group absence.

## 15. Proof obligations and invariant ledger

The five-pipe proof is structural: ten unique pipe ends are relocated above
19, exactly five DUP2 destinations are installed, and every high source is
closed in the child. Therefore fd 0 is only ACK input, fd 1 only result
stdout, fd 2 only external stderr, fd 3 only live-empty payload stdin, and fd
4 only release. Separate node identities exclude aliasing and a PTY.

The no-early-payload proof is causal: the actor withholds L until known-group
durability; V8 withholds watchdog creation until L plus EOF; the supervisor
withholds BEGIN until internal R; the actor withholds A until PENDING_ACK is
durable; V8 withholds internal S until A plus EOF; the watchdog withholds
payload spawn until S. Consequently a possible payload implies a prior
durable consumed bit and known PGID.

The one-attempt proof is monotone: start is legal only with no actor suffix;
SPAWNED has no transition to start; PENDING_ACK latches consumed; ACK_CLOSED
cannot clear it; every error targets recovery or FINAL_FAILURE; recover has no
spawn edge; and both final states are absorbing. Syscall continuation cannot
reenter posix_spawn.

The output proof is conjunctive: internal payload bytes are nested inside a
V8 RESULT, but the actor separately requires exact BEGIN, RESULT grammar and
hashes, direct supervisor wait, both external EOFs, empty external stderr,
T/S/EOF arithmetic, group absence, whole-V8 identity, current-ledger identity,
and durable final append. No nested claim can substitute for its outer
observation.

The recovery proof is fail-closed: ambiguity first consumes; only the exact
known group may be killed; absence precedes recovery; recovery-binder mode is
fixed by argv and cannot spawn a payload; its report must independently prove
permanent failure and four V8 absence gates; and the invocation bit is sticky.
Thus failure cannot promote success or cause a second payload.

The persistence proof is order-based: SPAWNED durability precedes L;
PENDING_ACK durability precedes the first possibly written A byte; all journal
records contain parent identities; ACK_CLOSED is informational rather than a
condition for consumption; and final durability is independently reread.
Therefore any journal prefix that permits payload ambiguity already contains
the consumed bit and known PGID. An incomplete append before PENDING_ACK
cannot coexist with an attempted A by program order.

This control does not certify the later host premises, implement or execute an
actor, authorize an append, or validate a runtime result. Those remain closed
until this exact whole file is manifest-bound, Y1 lifecycle/transport and Y2
recovery/ledger reviews each return Blocker=0 Major=0 Minor=0 Ambiguity=0,
and a later ledger event grants the exact next action.

BATCH07_P27_E001_SUPERVISOR_ACTOR_RECOVERY_AUTHOR_STOP
