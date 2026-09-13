# E001 supervisor host probe recovery V9

Status: inert author control; no embedded material was executed.

## 1. Authority and frozen inputs

This V9 control is authorized only by ledger entry E0349.  The parent ledger is
bound as dev 2431, ino 12439253869, mode 0644, nlink 1, uid 0, gid 0,
2078115 bytes, 22241 LF, and SHA-256
b2fd36caf5414f41f57e6ffb000df36978ef2159529d87a3d67e8cfde659e3ea.  Its
unique final terminal is
BATCH07_P27_PROBE_RECOVERY_E001_HOST_V9_PREAUTHOR_SPECIFICATION_CORRECTED_AND_CONTROL_REAUTHORIZED.

The qualified manifest remains frozen at 135 rows, 21715 bytes, 135 LF, and
SHA-256 7b315ceae9d93c29877a02f5e50eccfcdf1ce95d50341617c94e3cb0dd9e50b7.
This author does not extend it.  Host V8 remains frozen at 74973 bytes, 1071
LF, and SHA-256
72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf.

All five source regions below are inert ASCII text.  They are neither imported
nor parsed as a programming language, compiled, evaluated, executed, or
launched during authorship.  Runtime words in the source specify the future
controlled probe; they are not execution claims.

## 2. E0349 progress contract and finite arithmetic

The future actor must bind all of the following positive finite constants
before launch.  V9 fixes their accepted values, rather than inferring them from
POSIX, a successful signal call, an observation, EOF, ESRCH, or physical reap.

| name | nanoseconds | scope |
| --- | ---: | --- |
| OWNER_CONTROL_PROGRESS_NS | 20000000 | one owner control transition while any reservation, live slot, framing obligation, or exit-entry obligation exists |
| PRE_SIGNAL_CONTROL_NS | 20000000 | selection, fixed census, and exact-PID pre-signal work |
| TERM_ALLOWANCE_NS | 40000000 | cooperative exact-PID TERM observation window |
| EINTR_SYSCALL_NS | 20000000 | all bounded EINTR retries in one forced-cleanup selection |
| EXACT_KILL_WAIT_NS | 80000000 | exact-PID SIGKILL plus exact direct-parent wait return |
| RESCUE_ACCOUNT_NS | 10000000 | state/error rescue transitions after kill/wait |
| KILL_REAP_PROGRESS_NS | 170000000 | starts when OUTER selects a live/unknown PID; sum of the five preceding forced-cleanup sub-bounds |
| ORDER_GATE_NS | 20000000 | one role-order gate and status classification |
| CENSUS_ADMISSION_NS | 20000000 | admission latch plus one complete fixed census |
| TERMINAL_FRAMING_PROGRESS_NS | 80000000 | all bounded result and terminal write-all transitions and their postchecks |
| EXIT_ENTRY_PROGRESS_NS | 20000000 | final status latch through entry to the host exit syscall |
| ACTOR_ACK_PROGRESS_NS | 500000000 | future actor-only observation/ACK interval after host exit; not a host completion premise |

The registry has MAX_LIVE_SLOTS = 4.  Three non-keeper role gates and the
keeper gate each cost at most OWNER_CONTROL_PROGRESS_NS +
KILL_REAP_PROGRESS_NS + ORDER_GATE_NS = 210000000 ns.  Thus the separately
armed cleanup guard is exactly

    20000000 + 3 * 210000000 + 210000000 = 860000000 ns.

The host post-operational completion bound is

    HOST_COMPLETION_AFTER_OPERATION_NS
      = 860000000 + 80000000 + 20000000
      = 960000000 ns.

The future actor ACK bound is separate:

    ACTOR_ACK_AFTER_OPERATION_NS
      = HOST_COMPLETION_AFTER_OPERATION_NS + ACTOR_ACK_PROGRESS_NS
      = 1460000000 ns.

Every addition and multiplication is checked against signed 63-bit nanosecond
range before the first descriptor is opened or slot is reserved.  The owner
progress lease begins before the first reservation and remains in force until
complete result write-all, complete terminal write-all, every immediate
postcheck, final framing-state commit, and entry to the host exit syscall.  It
does not end when the last child slot clears.  The return-to-commit part of the
lease excludes asynchronous fatal injection only between a successful spawn
return and its first three fixed-slot assignments, and between an exact
waitpid return and its fixed-slot raw-status/reaped assignments.  This is an
explicit environmental premise, not a claim about Python or POSIX.  Scheduler
starvation, freezer/ptrace suspension, SIGSTOP, unbounded kernel blocking,
owner hard/default-fatal death, permanent EPERM, and failure to enter exit
within the bounds are out of the accepted domain and may never be reported as
a completed PASS.

## 3. Flattened OUTER sole-owner source

UNIFIED OUTER V9 SOURCE BEGIN
#!/usr/bin/env python3
import errno
import hashlib
import os
import resource
import signal
import stat
import sys
import time

SCHEMA = b"P27E001-HOST-V9"
MAX_LIVE_SLOTS = 4
MAX_FD_SLOTS = 24
MAX_FD_NUMBER = 1048575
NS_MAX = 0x7fffffffffffffff
SOURCE_EXEC_FD = 100
SOURCE_EXEC_PATH = "/proc/self/fd/100"
PYTHON_IMAGE_PATH = "/proc/self/exe"

OWNER_CONTROL_PROGRESS_NS = 20000000
PRE_SIGNAL_CONTROL_NS = 20000000
TERM_ALLOWANCE_NS = 40000000
EINTR_SYSCALL_NS = 20000000
EXACT_KILL_WAIT_NS = 80000000
RESCUE_ACCOUNT_NS = 10000000
KILL_REAP_PROGRESS_NS = 170000000
ORDER_GATE_NS = 20000000
CENSUS_ADMISSION_NS = 20000000
TERMINAL_FRAMING_PROGRESS_NS = 80000000
EXIT_ENTRY_PROGRESS_NS = 20000000
EXIT_ENTRY_MAX_TRANSITIONS = 3
ACTOR_ACK_PROGRESS_NS = 500000000
PER_ROLE_NS = 210000000
DERIVED_CLEANUP_GUARD_NS = 860000000
HOST_COMPLETION_AFTER_OPERATION_NS = 960000000
ACTOR_ACK_AFTER_OPERATION_NS = 1460000000

S_FREE = 0
S_RESERVED = 1
S_LIVE = 2
S_REAPED = 3
F_STATE = 0
F_PID = 1
F_STATUS = 2
F_ROLE = 3
F_FLAGS = 4
R_NONE = 0
R_CHILD = 1
R_MARKER = 2
R_LAUNCHER = 3
R_KEEPER = 4
CENSUS = (0, 1, 2, 3)
CLEAN_ORDER = (R_CHILD, R_MARKER, R_LAUNCHER, R_KEEPER)
CLEAN_RETRY_STEPS = tuple(range(64))

D_FREE = 0
D_RESERVED = 1
D_OWNED = 2
D_CLOSED = 3
D_STATE = 0
D_FD = 1
D_ROLE = 2
FD_CENSUS = tuple(range(MAX_FD_SLOTS))

PROBES = (
    b"P00", b"P01C", b"P01D", b"P02", b"P03",
    b"P04", b"P05", b"P06", b"P07", b"P08",
    b"P09", b"P10", b"P11", b"P12", b"P13",
)
BROKER_OPS = (
    b"E2BIG", b"INFO", b"", b"", b"",
    b"", b"EXIT23", b"", b"", b"TERM",
    b"KILL", b"CHAIN16", b"", b"BLOCK0", b"",
)
LOCAL_PROBES = (
    b"P01D", b"P02", b"P03", b"P04",
    b"P06", b"P07", b"P11", b"P13",
)
BROKER_PROBES = (b"P00", b"P01C", b"P05", b"P08", b"P09", b"P10", b"P12")
CHILD_MODES = (b"INFO", b"EXIT23", b"TERM", b"KILL", b"BLOCK0")
EXTRA = (
    b"E00", b"E01", b"E02", b"E03", b"E04",
    b"E05", b"E06", b"E07", b"E08", b"EXTRA[9]",
)

CHILD_SOURCE_SHA = b"12a81663e633c7cab5cb03da666aa5262ba0f9afa840076e80cf52d2bf8d7ba5"
MARKER_SOURCE_SHA = b"b165a0a62f11def502c80d595d2eb30ecc0813c5fa8578b8ec9c2e78a85cea70"
LAUNCHER_SOURCE_SHA = b"031cf45a7e8ea1c17336fd22d6ba6b83902c72cde8783964d7297bb372d9e35f"
KEEPER_SOURCE_SHA = b"1a4433f4f2f282790852357b2fabd753da4ef75c52504c5d270b7ac0483fc2df"
CHILD_SOURCE_BYTES = 5225
CHILD_SOURCE_LF = 186
MARKER_SOURCE_BYTES = 18864
MARKER_SOURCE_LF = 616
LAUNCHER_SOURCE_BYTES = 1022
LAUNCHER_SOURCE_LF = 43
KEEPER_SOURCE_BYTES = 1007
KEEPER_SOURCE_LF = 38

# These objects are allocated before every pipe and every spawn.  They are the
# sole ownership censuses.  No dict, append, sort, role list, or telemetry
# object has ownership authority.
slots = [[S_FREE, -1, -1, R_NONE, 0] for unused in CENSUS]
fdslots = [[D_FREE, -1, R_NONE] for unused in FD_CENSUS]
cleanup_fault = [0] * 64
semantic_fault = [0] * 64
frame_state = [0, 0, 0, 0, 0, 0]
p10_seen = [0] * 16
p10_pid_observation = [-1] * 16
operational_overrun = [0]
admission_closed = [0]
phase = [0]
fd_fault_latched = [0]
role_actual_status = [-1] * 5
role_status_seen = [0] * 5


class HostFailure(Exception):
    pass


def mark_semantic(code):
    if 0 <= code < 64:
        semantic_fault[code] = 1


def mark_cleanup(code):
    try:
        if 0 <= code < 64:
            cleanup_fault[code] = 1
    except BaseException:
        pass


def checked_add(a, b):
    if a < 0 or b < 0 or a > NS_MAX - b:
        raise HostFailure("nanosecond-overflow")
    return a + b


def checked_mul(a, b):
    if a < 0 or b < 0 or (a != 0 and b > NS_MAX // a):
        raise HostFailure("nanosecond-overflow")
    return a * b


def verify_bound_constants():
    positive = (
        OWNER_CONTROL_PROGRESS_NS, PRE_SIGNAL_CONTROL_NS,
        TERM_ALLOWANCE_NS, EINTR_SYSCALL_NS, EXACT_KILL_WAIT_NS,
        RESCUE_ACCOUNT_NS, KILL_REAP_PROGRESS_NS, ORDER_GATE_NS,
        CENSUS_ADMISSION_NS, TERMINAL_FRAMING_PROGRESS_NS,
        EXIT_ENTRY_PROGRESS_NS, ACTOR_ACK_PROGRESS_NS,
    )
    for value in positive:
        if value <= 0:
            raise HostFailure("nonpositive-progress-bound")
    forced = checked_add(PRE_SIGNAL_CONTROL_NS, TERM_ALLOWANCE_NS)
    forced = checked_add(forced, EINTR_SYSCALL_NS)
    forced = checked_add(forced, EXACT_KILL_WAIT_NS)
    forced = checked_add(forced, RESCUE_ACCOUNT_NS)
    if forced != KILL_REAP_PROGRESS_NS:
        raise HostFailure("kill-reap-arithmetic")
    per_role = checked_add(OWNER_CONTROL_PROGRESS_NS, KILL_REAP_PROGRESS_NS)
    per_role = checked_add(per_role, ORDER_GATE_NS)
    if per_role != PER_ROLE_NS:
        raise HostFailure("role-arithmetic")
    cleanup = checked_add(CENSUS_ADMISSION_NS, checked_mul(3, PER_ROLE_NS))
    cleanup = checked_add(cleanup, PER_ROLE_NS)
    if cleanup != DERIVED_CLEANUP_GUARD_NS:
        raise HostFailure("cleanup-arithmetic")
    host = checked_add(cleanup, TERMINAL_FRAMING_PROGRESS_NS)
    host = checked_add(host, EXIT_ENTRY_PROGRESS_NS)
    if host != HOST_COMPLETION_AFTER_OPERATION_NS:
        raise HostFailure("host-bound-arithmetic")
    actor = checked_add(host, ACTOR_ACK_PROGRESS_NS)
    if actor != ACTOR_ACK_AFTER_OPERATION_NS:
        raise HostFailure("actor-bound-arithmetic")
    if EXIT_ENTRY_MAX_TRANSITIONS != 3:
        raise HostFailure("exit-transition-count")


def close_inherited_fd_surface(deadline):
    # This one preownership admission call closes every legal nonstandard fd.
    # The bound platform requires RLIMIT_NOFILE not exceed MAX_FD_NUMBER + 1;
    # afterward the fixed fdslots table is the sole nonstandard FD census.
    before(deadline)
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    after(deadline)
    if soft == resource.RLIM_INFINITY or hard == resource.RLIM_INFINITY:
        raise HostFailure("unbounded-inherited-fd-surface")
    if soft > MAX_FD_NUMBER + 1 or hard > MAX_FD_NUMBER + 1:
        raise HostFailure("inherited-fd-ceiling")
    before(deadline)
    os.closerange(3, MAX_FD_NUMBER + 1)
    after(deadline)
    before(deadline)
    try:
        os.fstat(SOURCE_EXEC_FD)
    except OSError as exc:
        if exc.errno != errno.EBADF:
            after(deadline)
            raise
    else:
        after(deadline)
        raise HostFailure("source-exec-fd-inherited")
    after(deadline)


def mono():
    return time.monotonic_ns()


def before(deadline):
    now = mono()
    if now > deadline:
        operational_overrun[0] = 1
        raise HostFailure("operational-deadline-before-call")
    return now


def after(deadline):
    now = mono()
    if now > deadline:
        operational_overrun[0] = 1
        raise HostFailure("operational-deadline-after-call")
    return now


def edge(deadline):
    return after(deadline)


def reserve_fd(role):
    for index in FD_CENSUS:
        if fdslots[index][D_STATE] == D_FREE:
            fdslots[index][D_ROLE] = role
            fdslots[index][D_FD] = -1
            fdslots[index][D_STATE] = D_RESERVED
            return index
    raise HostFailure("fd-registry-full")


def release_fd_noncreation(index):
    fdslots[index][D_FD] = -1
    fdslots[index][D_ROLE] = R_NONE
    fdslots[index][D_STATE] = D_FREE


def owned_pipe(role, deadline):
    if fd_fault_latched[0] != 0:
        raise HostFailure("fd-fault-latched")
    before(deadline)
    left = reserve_fd(role)
    try:
        right = reserve_fd(role)
    except BaseException:
        release_fd_noncreation(left)
        raise
    try:
        before(deadline)
    except BaseException:
        release_fd_noncreation(left)
        release_fd_noncreation(right)
        raise
    try:
        rfd, wfd = os.pipe2(os.O_CLOEXEC | os.O_NONBLOCK)
    except OSError:
        release_fd_noncreation(left)
        release_fd_noncreation(right)
        after(deadline)
        raise
    fdslots[left][D_FD] = rfd
    fdslots[left][D_STATE] = D_OWNED
    fdslots[right][D_FD] = wfd
    fdslots[right][D_STATE] = D_OWNED
    after(deadline)
    return left, right


def owned_open_readonly(path, role, deadline):
    if fd_fault_latched[0] != 0:
        raise HostFailure("fd-fault-latched")
    before(deadline)
    index = reserve_fd(role)
    try:
        before(deadline)
    except BaseException:
        release_fd_noncreation(index)
        raise
    try:
        fd = os.open(path, os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW)
    except OSError:
        release_fd_noncreation(index)
        after(deadline)
        raise
    fdslots[index][D_FD] = fd
    fdslots[index][D_STATE] = D_OWNED
    after(deadline)
    return index


def fd_number(index):
    if index < 0 or index >= MAX_FD_SLOTS:
        raise HostFailure("bad-fd-slot")
    if fdslots[index][D_STATE] != D_OWNED:
        raise HostFailure("fd-not-owned")
    return fdslots[index][D_FD]


def close_fd_nonthrowing(index, code, deadline):
    try:
        if 0 <= index < MAX_FD_SLOTS and fdslots[index][D_STATE] == D_OWNED:
            fd = fdslots[index][D_FD]
            try:
                os.close(fd)
            except OSError as exc:
                if exc.errno == errno.EBADF:
                    # Registry/physical ownership disagreement is permanent
                    # failure evidence.  EBADF is never clean-close proof.
                    fd_fault_latched[0] = 1
                    mark_cleanup(code)
                    fdslots[index][D_FD] = -1
                    fdslots[index][D_ROLE] = R_NONE
                    fdslots[index][D_STATE] = D_FREE
                else:
                    fd_fault_latched[0] = 1
                    mark_cleanup(code)
            except BaseException:
                fd_fault_latched[0] = 1
                mark_cleanup(code)
            else:
                fdslots[index][D_FD] = -1
                fdslots[index][D_ROLE] = R_NONE
                fdslots[index][D_STATE] = D_FREE
            if cleanup_now(deadline) > deadline:
                mark_cleanup(code)
    except BaseException:
        fd_fault_latched[0] = 1
        mark_cleanup(code)


def close_all_fds_nonthrowing(deadline):
    # Fixed rescue passes; no descriptor list is allocated and no exception
    # prevents a later descriptor from being attempted.
    for attempt in (0, 1, 2, 3):
        for index in FD_CENSUS:
            close_fd_nonthrowing(index, 1, deadline)


def verify_source_file(path, expected_sha, expected_bytes, expected_lf,
                       deadline):
    index = owned_open_readonly(path, R_NONE, deadline)
    fd = fd_number(index)
    if fd == SOURCE_EXEC_FD:
        close_fd_nonthrowing(index, 32, deadline)
        raise HostFailure("source-oldfd-equals-exec-fd")
    before(deadline)
    info = os.fstat(fd)
    after(deadline)
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        close_fd_nonthrowing(index, 30, deadline)
        raise HostFailure("source-file-type")
    digest = hashlib.sha256()
    total = 0
    lf = 0
    while True:
        part = checked_read(fd, 1048576, deadline)
        if part is None:
            edge(deadline)
            continue
        if part == b"":
            edge(deadline)
            break
        digest.update(part)
        total += len(part)
        lf += part.count(b"\n")
        edge(deadline)
    if total != expected_bytes or lf != expected_lf:
        close_fd_nonthrowing(index, 31, deadline)
        raise HostFailure("source-size-or-lf")
    if digest.hexdigest().encode("ascii") != expected_sha:
        close_fd_nonthrowing(index, 31, deadline)
        raise HostFailure("source-sha")
    edge(deadline)
    # Keep the verified open-file description in the fixed FD census.  Every
    # future interpreter receives only a dup of this descriptor at fd 100 and
    # opens /proc/self/fd/100; no verified source is reopened by pathname.
    return index


def rewind_verified_source(index, deadline):
    fd = fd_number(index)
    before(deadline)
    position = os.lseek(fd, 0, os.SEEK_SET)
    after(deadline)
    if position != 0:
        raise HostFailure("source-rewind")
    return fd


def reserve_slot(role):
    if admission_closed[0] != 0:
        raise HostFailure("spawn-admission-closed")
    for index in CENSUS:
        if slots[index][F_STATE] == S_FREE:
            slots[index][F_PID] = -1
            slots[index][F_STATUS] = -1
            slots[index][F_ROLE] = role
            slots[index][F_FLAGS] = 0
            slots[index][F_STATE] = S_RESERVED
            return index
    raise HostFailure("live-slot-registry-full")


def release_slot_noncreation(index):
    # This transition is legal only in the OSError branch of posix_spawn,
    # where no successful PID return occurred.
    slots[index][F_PID] = -1
    slots[index][F_STATUS] = -1
    slots[index][F_ROLE] = R_NONE
    slots[index][F_FLAGS] = 0
    slots[index][F_STATE] = S_FREE


def spawn_owned(role, path, argv, env, file_actions, setpgroup, deadline):
    # argv, env, actions, path, role, and the stable registry slot all exist
    # before this call.  The successful return-to-commit lease excludes an
    # asynchronous fatal injection in the following three assignments.
    if fd_fault_latched[0] != 0:
        raise HostFailure("fd-fault-before-spawn")
    before(deadline)
    index = reserve_slot(role)
    try:
        before(deadline)
    except BaseException:
        release_slot_noncreation(index)
        raise
    try:
        pid = os.posix_spawn(path, argv, env, file_actions=file_actions,
                             setpgroup=setpgroup)
    except OSError:
        release_slot_noncreation(index)
        after(deadline)
        raise
    slots[index][F_PID] = pid
    slots[index][F_STATUS] = -1
    slots[index][F_STATE] = S_LIVE
    after(deadline)
    return index


def wait_owned(index, options, deadline):
    if slots[index][F_STATE] != S_LIVE:
        raise HostFailure("wait-nonlive-slot")
    pid = slots[index][F_PID]
    before(deadline)
    got, raw = os.waitpid(pid, options)
    if got == pid:
        slots[index][F_STATUS] = raw
        slots[index][F_STATE] = S_REAPED
    after(deadline)
    if got not in (0, pid):
        raise HostFailure("wait-wrong-pid")
    return got, raw


def exact_exit(raw, code):
    return os.WIFEXITED(raw) and os.WEXITSTATUS(raw) == code


def exact_signal(raw, sig):
    return os.WIFSIGNALED(raw) and os.WTERMSIG(raw) == sig


def retire_reaped_child(index):
    if slots[index][F_ROLE] != R_CHILD or slots[index][F_STATE] != S_REAPED:
        raise HostFailure("retire-unreaped-child")
    raw = slots[index][F_STATUS]
    pid = slots[index][F_PID]
    role_actual_status[R_CHILD] = raw
    role_status_seen[R_CHILD] = 1
    slots[index][F_PID] = -1
    slots[index][F_STATUS] = -1
    slots[index][F_ROLE] = R_NONE
    slots[index][F_FLAGS] = 0
    slots[index][F_STATE] = S_FREE
    return raw, pid


def checked_read(fd, count, deadline):
    before(deadline)
    try:
        data = os.read(fd, count)
    except BlockingIOError:
        after(deadline)
        return None
    except InterruptedError:
        after(deadline)
        return None
    after(deadline)
    return data


def checked_write(fd, data, deadline):
    before(deadline)
    try:
        count = os.write(fd, data)
    except (BlockingIOError, InterruptedError):
        after(deadline)
        return -1
    except BrokenPipeError:
        after(deadline)
        return -2
    after(deadline)
    return count


def write_all(fd, payload, deadline, state_index):
    frame_state[state_index] = 1
    offset = 0
    while offset < len(payload):
        count = checked_write(fd, payload[offset:], deadline)
        if count == -2:
            frame_state[state_index] = 4
            edge(deadline)
            return False
        if count < 0:
            edge(deadline)
            continue
        if count == 0 or count > len(payload) - offset:
            frame_state[state_index] = 4
            edge(deadline)
            return False
        offset += count
        frame_state[state_index] = 2
        edge(deadline)
    frame_state[state_index] = 3
    edge(deadline)
    return True


def read_exact_line(fd, limit, deadline):
    data = bytearray()
    while True:
        part = checked_read(fd, 4096, deadline)
        if part is None:
            edge(deadline)
            continue
        if part == b"":
            edge(deadline)
            break
        data.extend(part)
        if len(data) > limit:
            raise HostFailure("line-limit")
        if b"\n" in part:
            edge(deadline)
            break
        edge(deadline)
    raw = bytes(data)
    if raw.count(b"\n") != 1 or not raw.endswith(b"\n"):
        raise HostFailure("noncanonical-line")
    return raw


def drain_to_eof(fd, limit, deadline):
    data = bytearray()
    while True:
        part = checked_read(fd, 4096, deadline)
        if part is None:
            edge(deadline)
            continue
        if part == b"":
            edge(deadline)
            break
        data.extend(part)
        if len(data) > limit:
            raise HostFailure("drain-limit")
        edge(deadline)
    edge(deadline)
    return bytes(data)


def canonical_env(base, probe, mode, ordinal, child_source_sha, image_sha,
                  safe_hex, operational_deadline):
    # The closed environment has no inherited entries.  Sorted ASCII records
    # define the exact environment semantic hash seen by the child.
    pairs = (
        (b"LANG", b"C"),
        (b"LC_ALL", b"C"),
        (b"P27_CHILD_DEADLINE_NS", str(operational_deadline).encode("ascii")),
        (b"P27_CHILD_SOURCE_SHA", child_source_sha),
        (b"P27_EXTRA_09", EXTRA[9]),
        (b"P27_IMAGE_SHA", image_sha),
        (b"P27_INSTANCE", str(ordinal).encode("ascii")),
        (b"P27_MODE", mode),
        (b"P27_PROBE", probe),
        (b"P27_SAFE_HEX", safe_hex),
        (b"PYTHONHASHSEED", b"0"),
    )
    raw = b"".join(key + b"=" + value + b"\x00" for key, value in pairs)
    result = {}
    for key, value in pairs:
        result[key.decode("ascii")] = value.decode("ascii")
    return result, hashlib.sha256(raw).hexdigest().encode("ascii")


def expected_child_line(probe, mode, ordinal, pid, ppid, sid, pgid,
                        image_sha, source_sha, safe_hex, env_sha):
    # Exactly thirteen pipe-separated fields.  Field 13 carries EXTRA[9].
    fields = (
        SCHEMA,
        b"probe=" + probe,
        b"mode=" + mode,
        b"instance=" + str(ordinal).encode("ascii"),
        b"pid=" + str(pid).encode("ascii"),
        b"ppid=" + str(ppid).encode("ascii"),
        b"sid=" + str(sid).encode("ascii"),
        b"pgid=" + str(pgid).encode("ascii"),
        b"image_sha=" + image_sha,
        b"source_sha=" + source_sha,
        b"cwd_hex=" + safe_hex,
        b"env_sha=" + env_sha,
        b"extra9=" + EXTRA[9].hex().encode("ascii"),
    )
    if len(fields) != 13:
        raise HostFailure("p01c-field-count")
    return b"|".join(fields) + b"\n"


def no_live_child_slot():
    for index in CENSUS:
        if slots[index][F_ROLE] == R_CHILD and slots[index][F_STATE] in (S_RESERVED, S_LIVE):
            return False
    return True


def reap_child_exact(index, expected_kind, deadline):
    got, raw = wait_owned(index, 0, deadline)
    edge(deadline)
    if got != slots[index][F_PID]:
        raise HostFailure("child-not-exactly-reaped")
    if expected_kind == b"EXIT0" and not exact_exit(raw, 0):
        raise HostFailure("child-status-not-exit0")
    if expected_kind == b"EXIT23" and not exact_exit(raw, 23):
        raise HostFailure("child-status-not-exit23")
    if expected_kind == b"TERM" and not exact_signal(raw, signal.SIGTERM):
        raise HostFailure("child-status-not-term")
    if expected_kind == b"KILL" and not exact_signal(raw, signal.SIGKILL):
        raise HostFailure("child-status-not-kill")
    edge(deadline)
    return raw


def child_file_actions(out_write, gate_read, source_fd):
    actions = [
        (os.POSIX_SPAWN_DUP2, source_fd, SOURCE_EXEC_FD),
        (os.POSIX_SPAWN_DUP2, out_write, 1),
        (os.POSIX_SPAWN_DUP2, gate_read, 3),
    ]
    return actions


def spawn_one_child(child_source_fd, probe, mode, ordinal, leader_pid, outer_sid,
                    image_sha, safe_hex, operational_deadline):
    if not no_live_child_slot():
        raise HostFailure("simultaneous-child-slot")
    out_r_slot, out_w_slot = owned_pipe(R_CHILD, operational_deadline)
    gate_r_slot, gate_w_slot = owned_pipe(R_CHILD, operational_deadline)
    out_r = fd_number(out_r_slot)
    out_w = fd_number(out_w_slot)
    gate_r = fd_number(gate_r_slot)
    gate_w = fd_number(gate_w_slot)
    env, env_sha = canonical_env({}, probe, mode, ordinal, CHILD_SOURCE_SHA,
                                 image_sha, safe_hex, operational_deadline)
    before(operational_deadline)
    position = os.lseek(child_source_fd, 0, os.SEEK_SET)
    after(operational_deadline)
    if position != 0:
        raise HostFailure("child-source-rewind")
    actions = child_file_actions(out_w, gate_r, child_source_fd)
    index = spawn_owned(R_CHILD, PYTHON_IMAGE_PATH,
                        (PYTHON_IMAGE_PATH, SOURCE_EXEC_PATH, mode.decode("ascii")),
                        env, actions, leader_pid, operational_deadline)
    close_fd_nonthrowing(out_w_slot, 2, operational_deadline)
    close_fd_nonthrowing(gate_r_slot, 3, operational_deadline)
    pid = slots[index][F_PID]
    before(operational_deadline)
    outer_pid = os.getpid()
    after(operational_deadline)
    expected = expected_child_line(probe, mode, ordinal, pid, outer_pid,
                                   outer_sid, leader_pid, image_sha,
                                   CHILD_SOURCE_SHA, safe_hex, env_sha)
    observed = read_exact_line(out_r, 8192, operational_deadline)
    if observed != expected:
        raise HostFailure("child-output-byte-mismatch")
    close_fd_nonthrowing(out_r_slot, 4, operational_deadline)
    if mode in (b"TERM", b"KILL", b"BLOCK0"):
        token = b"G"
        if not write_all(gate_w, token, operational_deadline, 4):
            raise HostFailure("child-gate-write")
    close_fd_nonthrowing(gate_w_slot, 5, operational_deadline)
    if mode == b"TERM":
        before(operational_deadline)
        os.kill(pid, signal.SIGTERM)
        after(operational_deadline)
        raw = reap_child_exact(index, b"TERM", operational_deadline)
    elif mode == b"KILL":
        before(operational_deadline)
        os.kill(pid, signal.SIGKILL)
        after(operational_deadline)
        raw = reap_child_exact(index, b"KILL", operational_deadline)
    elif mode == b"EXIT23":
        raw = reap_child_exact(index, b"EXIT23", operational_deadline)
    else:
        raw = reap_child_exact(index, b"EXIT0", operational_deadline)
    edge(operational_deadline)
    committed_raw, committed_pid = retire_reaped_child(index)
    if committed_raw != raw or committed_pid != pid:
        raise HostFailure("child-retirement-commit")
    edge(operational_deadline)
    return observed, raw, pid


def e2big_noncreation(child_source_fd, leader_pid, operational_deadline):
    # Constructed before reservation.  E2BIG must raise from posix_spawn; only
    # that proven noncreation branch releases the reservation.
    huge = "X" * 8388608
    argv = (PYTHON_IMAGE_PATH, SOURCE_EXEC_PATH, "INFO", huge)
    env = {"LANG": "C", "LC_ALL": "C"}
    before(operational_deadline)
    position = os.lseek(child_source_fd, 0, os.SEEK_SET)
    after(operational_deadline)
    if position != 0:
        raise HostFailure("e2big-source-rewind")
    actions = ((os.POSIX_SPAWN_DUP2, child_source_fd, SOURCE_EXEC_FD),)
    before_count = 0
    for index in CENSUS:
        if slots[index][F_STATE] in (S_RESERVED, S_LIVE):
            before_count += 1
    try:
        spawn_owned(R_CHILD, PYTHON_IMAGE_PATH, argv, env, actions, leader_pid,
                    operational_deadline)
    except OSError as exc:
        if exc.errno != errno.E2BIG:
            raise HostFailure("wrong-e2big-error")
    else:
        raise HostFailure("e2big-unexpected-child")
    after_count = 0
    for index in CENSUS:
        if slots[index][F_STATE] in (S_RESERVED, S_LIVE):
            after_count += 1
    if before_count != after_count:
        raise HostFailure("e2big-reservation-leak")
    edge(operational_deadline)
    return b"E2BIG|noncreation=proved\n"


def run_broker_operation(op, child_source_fd, probe, leader_pid, outer_sid,
                         image_sha, safe_hex, operational_deadline):
    if op == b"E2BIG":
        return e2big_noncreation(child_source_fd, leader_pid, operational_deadline)
    if op == b"INFO":
        line, raw, pid = spawn_one_child(child_source_fd, probe, b"INFO", 0,
                                         leader_pid, outer_sid, image_sha,
                                         safe_hex, operational_deadline)
        return b"INFO|raw=" + str(raw).encode("ascii") + b"|" + line
    if op == b"EXIT23":
        line, raw, pid = spawn_one_child(child_source_fd, probe, b"EXIT23", 0,
                                         leader_pid, outer_sid, image_sha,
                                         safe_hex, operational_deadline)
        return b"EXIT23|raw=" + str(raw).encode("ascii") + b"|" + line
    if op == b"TERM":
        line, raw, pid = spawn_one_child(child_source_fd, probe, b"TERM", 0,
                                         leader_pid, outer_sid, image_sha,
                                         safe_hex, operational_deadline)
        return b"TERM|raw=" + str(raw).encode("ascii") + b"|" + line
    if op == b"KILL":
        line, raw, pid = spawn_one_child(child_source_fd, probe, b"KILL", 0,
                                         leader_pid, outer_sid, image_sha,
                                         safe_hex, operational_deadline)
        if not exact_signal(raw, signal.SIGKILL):
            raise HostFailure("p09-not-actual-sigkill")
        return b"KILL|raw=" + str(raw).encode("ascii") + b"|" + line
    if op == b"BLOCK0":
        line, raw, pid = spawn_one_child(child_source_fd, probe, b"BLOCK0", 0,
                                         leader_pid, outer_sid, image_sha,
                                         safe_hex, operational_deadline)
        return b"BLOCK0|raw=" + str(raw).encode("ascii") + b"|" + line
    if op == b"CHAIN16":
        result = bytearray(b"CHAIN16|count=16\n")
        ordinal = 0
        while ordinal < 16:
            if p10_seen[ordinal] != 0:
                raise HostFailure("p10-duplicate-ordinal-observation")
            line, raw, pid = spawn_one_child(child_source_fd, probe, b"INFO", ordinal,
                                             leader_pid, outer_sid, image_sha,
                                             safe_hex, operational_deadline)
            p10_seen[ordinal] = 1
            p10_pid_observation[ordinal] = pid
            # Numeric PID reuse is accepted.  Ordering and one observation for
            # each ordinal, not PID inequality, prove sixteen spawn instances.
            result.extend(b"ordinal=" + str(ordinal).encode("ascii") +
                          b"|raw=" + str(raw).encode("ascii") + b"|" + line)
            ordinal += 1
            edge(operational_deadline)
        for ordinal in range(16):
            if p10_seen[ordinal] != 1:
                raise HostFailure("p10-missing-ordinal")
        return bytes(result)
    raise HostFailure("closed-broker-op")


def probe_index(probe):
    found = -1
    for index in range(15):
        if PROBES[index] == probe:
            if found != -1:
                raise HostFailure("duplicate-probe-name")
            found = index
    if found < 0:
        raise HostFailure("unknown-probe")
    return found


def read_one_broker_request(fd, expected_probe, expected_op, expected_nonce,
                            deadline):
    raw = read_exact_line(fd, 256, deadline)
    expected = (b"REQ|probe=" + expected_probe + b"|op=" + expected_op +
                b"|nonce=" + expected_nonce + b"\n")
    if raw != expected:
        raise HostFailure("wrong-partial-malformed-broker-request")
    edge(deadline)
    return raw


def no_surplus_after_marker(fd, deadline):
    surplus = drain_to_eof(fd, 256, deadline)
    if surplus != b"":
        raise HostFailure("duplicate-late-surplus-broker-request")
    edge(deadline)


def cleanup_now(fallback):
    try:
        return time.monotonic_ns()
    except BaseException:
        mark_cleanup(2)
        return fallback


def cleanup_pause(deadline, code):
    try:
        if cleanup_now(deadline) > deadline:
            mark_cleanup(code)
            return
        time.sleep(0.001)
        if cleanup_now(deadline) > deadline:
            mark_cleanup(code)
    except BaseException:
        mark_cleanup(code)


def cleanup_clamped_deadline(start, duration, cap, code):
    try:
        if start < 0 or duration <= 0 or start > NS_MAX - duration:
            mark_cleanup(code)
            return cap
        value = start + duration
        if value > cap:
            mark_cleanup(code)
            return cap
        return value
    except BaseException:
        mark_cleanup(code)
        return cap


def cleanup_wait_once(index, options, code, deadline):
    # This routine never throws.  Exact-return commit precedes all validation,
    # deadlines, status classification, or error recording.
    try:
        if slots[index][F_STATE] != S_LIVE:
            return slots[index][F_STATE]
        pid = slots[index][F_PID]
        if cleanup_now(deadline) > deadline:
            mark_cleanup(code)
        try:
            got, raw = os.waitpid(pid, options)
        except InterruptedError:
            mark_cleanup(code)
            return S_LIVE
        except BaseException:
            mark_cleanup(code)
            return S_LIVE
        if got == pid:
            slots[index][F_STATUS] = raw
            slots[index][F_STATE] = S_REAPED
        if cleanup_now(deadline) > deadline:
            mark_cleanup(code)
        if got not in (0, pid):
            mark_cleanup(code)
        return slots[index][F_STATE]
    except BaseException:
        mark_cleanup(code)
        return S_LIVE


def cleanup_signal_exact(index, sig, code, deadline):
    sent = False
    try:
        if slots[index][F_STATE] == S_LIVE:
            pid = slots[index][F_PID]
            if cleanup_now(deadline) > deadline:
                mark_cleanup(code)
            try:
                os.kill(pid, sig)
                sent = True
            except ProcessLookupError:
                # ESRCH is not a reap.  The exact wait loop remains mandatory.
                mark_cleanup(code)
            except BaseException:
                mark_cleanup(code)
            if cleanup_now(deadline) > deadline:
                mark_cleanup(code)
    except BaseException:
        mark_cleanup(code)
    return sent


def cleanup_slot(index, role, pass_candidate, cleanup_deadline,
                 shared_selection):
    # Selection starts KILL_REAP_PROGRESS_NS.  TERM is a bounded subwindow of
    # that same horizon; it is not added in front of the kill/reap premise.
    try:
        if slots[index][F_ROLE] != role:
            return pass_candidate
        state = slots[index][F_STATE]
        if state == S_FREE:
            return pass_candidate
        if state == S_RESERVED:
            mark_cleanup(3)
            return False
        # All retry/rescue passes for this role use the one selection instant
        # armed by cleanup_registry; no retry can mint a fresh horizon.
        selection = shared_selection
        if selection < 0 or selection > NS_MAX - KILL_REAP_PROGRESS_NS:
            mark_cleanup(4)
            forced_end = cleanup_deadline
            pass_candidate = False
        else:
            forced_end = selection + KILL_REAP_PROGRESS_NS
        if forced_end > cleanup_deadline:
            mark_cleanup(4)
            forced_end = cleanup_deadline
        pre_signal_end = cleanup_clamped_deadline(
            selection, PRE_SIGNAL_CONTROL_NS, forced_end, 28)
        rescue_end = forced_end

        # PASS freezes launcher and keeper as live until their own turns.
        if role in (R_LAUNCHER, R_KEEPER) and pass_candidate:
            cleanup_wait_once(index, os.WNOHANG, 5, pre_signal_end)
            if slots[index][F_STATE] != S_LIVE:
                mark_cleanup(6)
                pass_candidate = False

        # A marker already reaped with exit 0 is the only PASS marker matrix.
        # Any live child on entry or any live marker after its output/EOF phase
        # demotes, even though cleanup remains exhaustive.
        if role == R_CHILD and slots[index][F_STATE] == S_LIVE:
            mark_cleanup(7)
            pass_candidate = False
        if role == R_MARKER and slots[index][F_STATE] == S_LIVE:
            mark_cleanup(8)
            pass_candidate = False

        if slots[index][F_STATE] == S_LIVE:
            term_sent = cleanup_signal_exact(index, signal.SIGTERM, 9,
                                             pre_signal_end)
            term_return = cleanup_now(pre_signal_end)
            if term_return > pre_signal_end or not term_sent:
                mark_cleanup(33)
                pass_candidate = False
            term_end = cleanup_clamped_deadline(
                term_return, TERM_ALLOWANCE_NS, forced_end, 34)
            for attempt in CLEAN_RETRY_STEPS:
                if slots[index][F_STATE] != S_LIVE:
                    break
                if cleanup_now(term_end) > term_end:
                    break
                cleanup_wait_once(index, os.WNOHANG, 10, term_end)
                if slots[index][F_STATE] == S_LIVE:
                    cleanup_pause(term_end, 25)

        rescued = False
        if slots[index][F_STATE] == S_LIVE:
            rescued = True
            pass_candidate = False
            eintr_start = cleanup_now(forced_end)
            eintr_end = cleanup_clamped_deadline(
                eintr_start, EINTR_SYSCALL_NS, forced_end, 35)
            kill_sent = False
            for attempt in CLEAN_RETRY_STEPS:
                if cleanup_now(eintr_end) > eintr_end:
                    break
                kill_sent = cleanup_signal_exact(index, signal.SIGKILL, 11,
                                                 eintr_end)
                if kill_sent:
                    break
                cleanup_pause(eintr_end, 30)
            if not kill_sent:
                mark_cleanup(31)
            kill_return = cleanup_now(eintr_end)
            if kill_return > eintr_end:
                mark_cleanup(36)
            exact_kill_wait_end = cleanup_clamped_deadline(
                kill_return, EXACT_KILL_WAIT_NS, forced_end, 37)
            for attempt in CLEAN_RETRY_STEPS:
                if slots[index][F_STATE] != S_LIVE:
                    break
                if cleanup_now(exact_kill_wait_end) > exact_kill_wait_end:
                    break
                options = 0 if kill_sent else os.WNOHANG
                cleanup_wait_once(index, options, 12, exact_kill_wait_end)
                if not kill_sent and slots[index][F_STATE] == S_LIVE:
                    cleanup_pause(exact_kill_wait_end, 38)
            wait_return = cleanup_now(exact_kill_wait_end)
            rescue_end = cleanup_clamped_deadline(
                wait_return, RESCUE_ACCOUNT_NS, forced_end, 39)

        # The E0349 premise makes this state unreachable in-domain.  It is
        # nevertheless recorded without throwing, and all later slots run.
        if slots[index][F_STATE] != S_REAPED:
            mark_cleanup(13)
            pass_candidate = False
            return pass_candidate

        raw = slots[index][F_STATUS]
        role_actual_status[role] = raw
        role_status_seen[role] = 1
        if cleanup_now(rescue_end) > rescue_end:
            mark_cleanup(29)
            pass_candidate = False
        if rescued:
            if not exact_signal(raw, signal.SIGKILL):
                mark_cleanup(14)
            # Rescue permanently demotes regardless of the observed status.
            pass_candidate = False
        elif role in (R_LAUNCHER, R_KEEPER):
            if not exact_signal(raw, signal.SIGTERM):
                mark_cleanup(15)
                pass_candidate = False
        elif role == R_MARKER:
            if not exact_exit(raw, 0):
                mark_cleanup(16)
                pass_candidate = False
        # A child status was already classified at the transaction boundary.
        return pass_candidate
    except BaseException:
        mark_cleanup(17)
        return False


def cleanup_registry(pass_candidate, launcher_hold_w_slot,
                     keeper_hold_w_slot, cleanup_start):
    # Nonthrowing, fixed-census, exhaustive state machine.  It never sorts,
    # allocates an ownership list, or consults telemetry/PID/mode side maps.
    if cleanup_start < 0 or cleanup_start > NS_MAX - DERIVED_CLEANUP_GUARD_NS:
        mark_cleanup(21)
        cleanup_deadline = NS_MAX
        pass_candidate = False
    else:
        cleanup_deadline = cleanup_start + DERIVED_CLEANUP_GUARD_NS
    admission_closed[0] = 1
    census_deadline = cleanup_start + CENSUS_ADMISSION_NS
    # Complete fixed census before the first signal.  The census itself owns
    # no allocation and validates every pre-reserved/live/unknown state.
    for index in CENSUS:
        state = slots[index][F_STATE]
        if state not in (S_FREE, S_RESERVED, S_LIVE, S_REAPED):
            mark_cleanup(22)
            pass_candidate = False
        if state in (S_RESERVED, S_LIVE) and slots[index][F_PID] <= 0:
            mark_cleanup(23)
            pass_candidate = False
    if cleanup_now(census_deadline) > census_deadline:
        mark_cleanup(24)
        pass_candidate = False
    for role in CLEAN_ORDER:
        role_start = cleanup_now(cleanup_deadline)
        if role_start <= NS_MAX - PER_ROLE_NS:
            role_deadline = role_start + PER_ROLE_NS
        else:
            role_deadline = cleanup_deadline
            mark_cleanup(26)
            pass_candidate = False
        if role_deadline > cleanup_deadline:
            role_deadline = cleanup_deadline
        for index in CENSUS:
            if slots[index][F_ROLE] == role and slots[index][F_STATE] != S_FREE:
                for rescue_pass in (0, 1, 2, 3):
                    pass_candidate = cleanup_slot(index, role, pass_candidate,
                                                  role_deadline, role_start)
                    if slots[index][F_STATE] in (S_FREE, S_REAPED):
                        break
        # Hold writers remain open through exact SIGTERM and reap at their role
        # turn, then close.  They cannot create a premature EOF/exit0 matrix.
        if role == R_LAUNCHER:
            close_fd_nonthrowing(launcher_hold_w_slot, 18, role_deadline)
        if role == R_KEEPER:
            close_fd_nonthrowing(keeper_hold_w_slot, 19, role_deadline)
        if cleanup_now(role_deadline) > role_deadline:
            mark_cleanup(27)
            pass_candidate = False
    for index in CENSUS:
        if slots[index][F_STATE] in (S_RESERVED, S_LIVE):
            mark_cleanup(20)
            pass_candidate = False
    return pass_candidate


def validate_ascii_token(raw, minimum, maximum, label):
    if len(raw) < minimum or len(raw) > maximum:
        raise HostFailure(label + "-length")
    for byte in raw:
        if byte < 0x21 or byte > 0x7e or byte in (0x2f, 0x5c):
            raise HostFailure(label + "-alphabet")
    return raw


def main():
    verify_bound_constants()
    if len(sys.argv) != 11:
        raise HostFailure("outer-argv-count")
    probe = validate_ascii_token(sys.argv[1].encode("ascii"), 3, 4, "probe")
    total_ns = int(sys.argv[2], 10)
    if total_ns < 2000000000 or total_ns > 15000000000:
        raise HostFailure("total-ns-range")
    launcher_path = os.fsencode(sys.argv[3])
    keeper_path = os.fsencode(sys.argv[4])
    marker_path = os.fsencode(sys.argv[5])
    child_path = os.fsencode(sys.argv[6])
    safe_path = os.fsencode(sys.argv[7])
    image_sha = validate_ascii_token(sys.argv[8].encode("ascii"), 64, 64, "image-sha")
    expected_safe_hex = validate_ascii_token(sys.argv[9].encode("ascii"), 2, 4096, "safe-hex")
    actor_nonce = validate_ascii_token(sys.argv[10].encode("ascii"), 32, 128, "actor-nonce")
    index_probe = probe_index(probe)
    expected_op = BROKER_OPS[index_probe]
    if (expected_op == b"") != (probe in LOCAL_PROBES):
        raise HostFailure("probe-operation-matrix")
    if (expected_op != b"") != (probe in BROKER_PROBES):
        raise HostFailure("broker-operation-matrix")
    if safe_path.hex().encode("ascii") != expected_safe_hex:
        raise HostFailure("safe-path-canonicality")
    if not safe_path.startswith(b"/tmp/p27-e001-host-v9/"):
        raise HostFailure("safe-path-containment")
    if safe_path.endswith(b"/") or b".." in safe_path.split(b"/") or b"\x00" in safe_path:
        raise HostFailure("safe-path-component")
    for source_path in (launcher_path, keeper_path, marker_path, child_path):
        if not source_path.startswith(safe_path + b"/"):
            raise HostFailure("source-path-containment")
        if b".." in source_path.split(b"/") or b"\x00" in source_path:
            raise HostFailure("source-path-component")

    start = mono()
    operational_deadline = checked_add(start, total_ns)
    checked_add(operational_deadline, HOST_COMPLETION_AFTER_OPERATION_NS)
    close_inherited_fd_surface(operational_deadline)
    before(operational_deadline)
    outer_sid = os.getsid(0)
    after(operational_deadline)
    before(operational_deadline)
    outer_pgid = os.getpgrp()
    after(operational_deadline)

    launcher_hold_r_slot = launcher_hold_w_slot = -1
    keeper_hold_r_slot = keeper_hold_w_slot = -1
    marker_req_r_slot = marker_req_w_slot = -1
    marker_resp_r_slot = marker_resp_w_slot = -1
    marker_out_r_slot = marker_out_w_slot = -1
    launcher_source_slot = keeper_source_slot = -1
    marker_source_slot = child_source_slot = -1
    launcher_slot = keeper_slot = marker_slot = -1
    marker_bytes = b""
    failure_text = b""
    pass_candidate = False
    cleanup_started = False
    phase[0] = 1

    try:
        phase[0] = 2
        before(operational_deadline)
        os.chdir(os.fsdecode(safe_path))
        after(operational_deadline)
        launcher_source_slot = verify_source_file(
            launcher_path, LAUNCHER_SOURCE_SHA, LAUNCHER_SOURCE_BYTES,
            LAUNCHER_SOURCE_LF, operational_deadline)
        keeper_source_slot = verify_source_file(
            keeper_path, KEEPER_SOURCE_SHA, KEEPER_SOURCE_BYTES,
            KEEPER_SOURCE_LF, operational_deadline)
        marker_source_slot = verify_source_file(
            marker_path, MARKER_SOURCE_SHA, MARKER_SOURCE_BYTES,
            MARKER_SOURCE_LF, operational_deadline)
        child_source_slot = verify_source_file(
            child_path, CHILD_SOURCE_SHA, CHILD_SOURCE_BYTES,
            CHILD_SOURCE_LF, operational_deadline)
        launcher_hold_r_slot, launcher_hold_w_slot = owned_pipe(R_LAUNCHER, operational_deadline)
        keeper_hold_r_slot, keeper_hold_w_slot = owned_pipe(R_KEEPER, operational_deadline)
        marker_req_r_slot, marker_req_w_slot = owned_pipe(R_MARKER, operational_deadline)
        marker_resp_r_slot, marker_resp_w_slot = owned_pipe(R_MARKER, operational_deadline)
        marker_out_r_slot, marker_out_w_slot = owned_pipe(R_MARKER, operational_deadline)

        launcher_actions = [
            (os.POSIX_SPAWN_DUP2, rewind_verified_source(launcher_source_slot,
                                                        operational_deadline),
             SOURCE_EXEC_FD),
            (os.POSIX_SPAWN_DUP2, fd_number(launcher_hold_r_slot), 3),
        ]
        leaf_hold_deadline = checked_add(operational_deadline,
                                         DERIVED_CLEANUP_GUARD_NS)
        launcher_env = {"LANG": "C", "LC_ALL": "C", "P27_ROLE": "launcher-v9",
                        "P27_LEAF_HOLD_DEADLINE_NS": str(leaf_hold_deadline)}
        launcher_slot = spawn_owned(
            R_LAUNCHER, PYTHON_IMAGE_PATH,
            (PYTHON_IMAGE_PATH, SOURCE_EXEC_PATH), launcher_env,
            launcher_actions, 0, operational_deadline)
        leader_pid = slots[launcher_slot][F_PID]
        close_fd_nonthrowing(launcher_hold_r_slot, 21, operational_deadline)
        if leader_pid == outer_pgid:
            raise HostFailure("outer-inside-owned-group")

        keeper_actions = [
            (os.POSIX_SPAWN_DUP2, rewind_verified_source(keeper_source_slot,
                                                        operational_deadline),
             SOURCE_EXEC_FD),
            (os.POSIX_SPAWN_DUP2, fd_number(keeper_hold_r_slot), 3),
        ]
        keeper_env = {"LANG": "C", "LC_ALL": "C", "P27_ROLE": "keeper-v9",
                      "P27_LEAF_HOLD_DEADLINE_NS": str(leaf_hold_deadline)}
        keeper_slot = spawn_owned(
            R_KEEPER, PYTHON_IMAGE_PATH,
            (PYTHON_IMAGE_PATH, SOURCE_EXEC_PATH), keeper_env,
            keeper_actions, leader_pid, operational_deadline)
        close_fd_nonthrowing(keeper_hold_r_slot, 22, operational_deadline)

        marker_actions = [
            (os.POSIX_SPAWN_DUP2, rewind_verified_source(marker_source_slot,
                                                        operational_deadline),
             SOURCE_EXEC_FD),
            (os.POSIX_SPAWN_DUP2, fd_number(marker_req_w_slot), 5),
            (os.POSIX_SPAWN_DUP2, fd_number(marker_resp_r_slot), 6),
            (os.POSIX_SPAWN_DUP2, fd_number(marker_out_w_slot), 1),
        ]
        marker_env = {
            "LANG": "C", "LC_ALL": "C", "P27_ACTOR_NONCE": actor_nonce.decode("ascii"),
            "P27_EXPECTED_OP": expected_op.decode("ascii"),
            "P27_MARKER_SOURCE_SHA": MARKER_SOURCE_SHA.decode("ascii"),
            "P27_OPERATIONAL_DEADLINE_NS": str(operational_deadline),
            "P27_PROBE": probe.decode("ascii"),
        }
        marker_slot = spawn_owned(
            R_MARKER, PYTHON_IMAGE_PATH,
            (PYTHON_IMAGE_PATH, SOURCE_EXEC_PATH, probe.decode("ascii")),
            marker_env, marker_actions, leader_pid, operational_deadline)
        close_fd_nonthrowing(marker_req_w_slot, 23, operational_deadline)
        close_fd_nonthrowing(marker_resp_r_slot, 24, operational_deadline)
        close_fd_nonthrowing(marker_out_w_slot, 25, operational_deadline)

        if expected_op != b"":
            request = read_one_broker_request(fd_number(marker_req_r_slot),
                                              probe, expected_op, actor_nonce,
                                              operational_deadline)
            response = run_broker_operation(expected_op, fd_number(child_source_slot),
                                            probe, leader_pid, outer_sid,
                                            image_sha, expected_safe_hex,
                                            operational_deadline)
            response_frame = (b"RESP|probe=" + probe + b"|op=" + expected_op +
                              b"|bytes=" + str(len(response)).encode("ascii") + b"\n" +
                              response + b"RESP-END\n")
            if not write_all(fd_number(marker_resp_w_slot), response_frame,
                             operational_deadline, 0):
                raise HostFailure("broker-response-short-or-epipe")
            close_fd_nonthrowing(marker_resp_w_slot, 26, operational_deadline)
        else:
            # Eight local probes make no broker request.  In particular OUTER
            # performs no request read here; EOF/no-surplus is proved only after
            # the marker has been physically reaped.
            close_fd_nonthrowing(marker_resp_w_slot, 27, operational_deadline)

        marker_bytes = drain_to_eof(fd_number(marker_out_r_slot), 1048576,
                                    operational_deadline)
        close_fd_nonthrowing(marker_out_r_slot, 28, operational_deadline)
        if not marker_bytes.endswith(b"P27E001_HOST_V9_MARKER_PASS\n"):
            raise HostFailure("marker-terminal-bytes")
        if marker_bytes.count(b"P27E001_HOST_V9_MARKER_PASS\n") != 1:
            raise HostFailure("marker-terminal-count")

        got, marker_raw = wait_owned(marker_slot, 0, operational_deadline)
        edge(operational_deadline)
        if got != slots[marker_slot][F_PID] or not exact_exit(marker_raw, 0):
            raise HostFailure("marker-exact-status")

        # This is deliberately after exact marker reap.  It proves no wrong,
        # partial, malformed, duplicate, late, or surplus request remained.
        no_surplus_after_marker(fd_number(marker_req_r_slot), operational_deadline)
        close_fd_nonthrowing(marker_req_r_slot, 29, operational_deadline)
        edge(operational_deadline)

        if not no_live_child_slot():
            raise HostFailure("child-slot-after-broker")
        if operational_overrun[0] != 0:
            raise HostFailure("latched-operational-overrun")
        pass_candidate = True
        edge(operational_deadline)
    except BaseException as exc:
        pass_candidate = False
        try:
            failure_text = (type(exc).__name__ + ":" + str(exc)).encode("ascii", "backslashreplace")[:512]
        except BaseException:
            failure_text = b"unprintable-host-failure"
    finally:
        cleanup_start = cleanup_now(0)
        cleanup_started = True
        pass_candidate = cleanup_registry(pass_candidate,
                                          launcher_hold_w_slot,
                                          keeper_hold_w_slot,
                                          cleanup_start)
        if cleanup_start <= NS_MAX - DERIVED_CLEANUP_GUARD_NS:
            cleanup_close_deadline = cleanup_start + DERIVED_CLEANUP_GUARD_NS
        else:
            cleanup_close_deadline = NS_MAX
            pass_candidate = False
        close_all_fds_nonthrowing(cleanup_close_deadline)
        phase[0] = 3

    if operational_overrun[0] != 0:
        pass_candidate = False
    for code in range(64):
        if cleanup_fault[code] != 0 or semantic_fault[code] != 0:
            pass_candidate = False
    for index in CENSUS:
        if slots[index][F_STATE] in (S_RESERVED, S_LIVE):
            pass_candidate = False
    for index in FD_CENSUS:
        if fdslots[index][D_STATE] in (D_RESERVED, D_OWNED):
            pass_candidate = False
    if not cleanup_started:
        pass_candidate = False

    phase[0] = 4
    framing_start = cleanup_now(0)
    if framing_start > NS_MAX - TERMINAL_FRAMING_PROGRESS_NS:
        pass_candidate = False
        framing_deadline = NS_MAX
    else:
        framing_deadline = framing_start + TERMINAL_FRAMING_PROGRESS_NS
    if framing_deadline > NS_MAX - EXIT_ENTRY_PROGRESS_NS:
        pass_candidate = False
        exit_deadline = NS_MAX
    else:
        exit_deadline = framing_deadline + EXIT_ENTRY_PROGRESS_NS
    result = b"HOST-V9|candidate=" + (b"PASS" if pass_candidate else b"FAIL")
    result += b"|probe=" + probe + b"|marker_bytes=" + str(len(marker_bytes)).encode("ascii")
    result += b"|failure=" + failure_text.hex().encode("ascii")
    result += (b"|actual_child=" + str(role_actual_status[R_CHILD]).encode("ascii") +
               b"|actual_marker=" + str(role_actual_status[R_MARKER]).encode("ascii") +
               b"|actual_launcher=" + str(role_actual_status[R_LAUNCHER]).encode("ascii") +
               b"|actual_keeper=" + str(role_actual_status[R_KEEPER]).encode("ascii") + b"\n")

    result_ok = write_all(1, result, framing_deadline, 1)
    marker_ok = False
    if result_ok:
        marker_ok = write_all(1, marker_bytes, framing_deadline, 2)
    edge(framing_deadline)
    if not result_ok or not marker_ok:
        pass_candidate = False
    if frame_state[1] != 3 or frame_state[2] != 3:
        pass_candidate = False
    edge(framing_deadline)

    # This is explicitly an actor-ACK-precondition candidate, never a final
    # PASS conclusion.  The future actor accepts it only with exact host exit 0
    # and its separately bounded ACK.  No host check after this frame can
    # rewrite the bytes into a stronger conclusion.
    terminal = (b"P27E001_HOST_V9_CANDIDATE_PASS\n" if pass_candidate else
                b"P27E001_HOST_V9_FAIL\n")
    terminal_ok = write_all(1, terminal, framing_deadline, 3)
    edge(framing_deadline)
    if not terminal_ok or frame_state[3] != 3:
        pass_candidate = False

    # The owner progress lease still applies here.  It ends only upon entry to
    # os._exit.  ACTOR_ACK_PROGRESS_NS starts later and is a separate actor
    # premise; this host neither waits for nor claims the ACK.
    # Exactly three nonblocking source transitions remain: choose the already
    # determined code, evaluate the direct call argument, and enter os._exit.
    # There is no pre-syscall flag pretending to observe entry.  E0349 binds
    # these three transitions by EXIT_ENTRY_PROGRESS_NS; failure to make them
    # yields no exit-0/actor-ACK acceptance.
    code = 0 if pass_candidate else 90
    os._exit(code)


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        # The phase is reported as observed; this fallback never labels a
        # post-ownership fault as preownership.  In-domain, phase 2 exceptions
        # were already caught and exhaustively cleaned by main.
        fallback_phase = phase[0]
        bootstrap_start = cleanup_now(0)
        entry_active = 0
        for index in CENSUS:
            if slots[index][F_STATE] in (S_RESERVED, S_LIVE):
                entry_active += 1
        entry_fd_active = 0
        for index in FD_CENSUS:
            if fdslots[index][D_STATE] in (D_RESERVED, D_OWNED):
                entry_fd_active += 1
        if entry_active != 0 or entry_fd_active != 0:
            if entry_active != 0:
                cleanup_registry(False, -1, -1, bootstrap_start)
            if bootstrap_start <= NS_MAX - DERIVED_CLEANUP_GUARD_NS:
                fallback_close_deadline = bootstrap_start + DERIVED_CLEANUP_GUARD_NS
            else:
                fallback_close_deadline = NS_MAX
            close_all_fds_nonthrowing(fallback_close_deadline)
            phase[0] = 5
        if bootstrap_start <= NS_MAX - TERMINAL_FRAMING_PROGRESS_NS:
            cleanup_offset = (DERIVED_CLEANUP_GUARD_NS
                              if entry_active != 0 or entry_fd_active != 0 else 0)
            if bootstrap_start <= NS_MAX - cleanup_offset - TERMINAL_FRAMING_PROGRESS_NS:
                bootstrap_deadline = (bootstrap_start + cleanup_offset +
                                      TERMINAL_FRAMING_PROGRESS_NS)
            else:
                bootstrap_deadline = NS_MAX
        else:
            bootstrap_deadline = NS_MAX
        active = 0
        for index in CENSUS:
            if slots[index][F_STATE] in (S_RESERVED, S_LIVE):
                active += 1
        try:
            fallback = (b"HOST-V9|candidate=FAIL|fallback=1|phase=" +
                        str(fallback_phase).encode("ascii") + b"|entry_active=" +
                        str(entry_active).encode("ascii") + b"|entry_fds=" +
                        str(entry_fd_active).encode("ascii") + b"|active_slots=" +
                        str(active).encode("ascii") + b"\nP27E001_HOST_V9_FAIL\n")
            write_all(1, fallback,
                      bootstrap_deadline, 5)
            edge(bootstrap_deadline)
        except BaseException:
            frame_state[5] = 4
        os._exit(90)
UNIFIED OUTER V9 SOURCE END

V9 STAGE 1 OUTER SOURCE COMPLETE

## 4. Childless keeper leaf source

UNIFIED KEEPER V9 SOURCE BEGIN
#!/usr/bin/env python3
import os
import signal
import time

# KEEPER owns no child, opens no path, and calls neither posix_spawn nor
# waitpid.  FD 3 is the OUTER-owned hold pipe.  Default SIGTERM disposition is
# deliberately preserved, so PASS requires OUTER's exact direct wait status to
# be SIGTERM.  EOF or data is a premature/different termination matrix.
deadline_raw = os.environ["P27_LEAF_HOLD_DEADLINE_NS"]
if not deadline_raw.isdigit():
    os._exit(70)
deadline = int(deadline_raw, 10)
def postcheck():
    if time.monotonic_ns() > deadline:
        os._exit(70)
signal.signal(signal.SIGPIPE, signal.SIG_IGN)
postcheck()
try:
    os.close(100)
except BaseException:
    os._exit(70)
postcheck()
while True:
    postcheck()
    try:
        token = os.read(3, 1)
    except BlockingIOError:
        time.sleep(0.002)
        postcheck()
        continue
    except InterruptedError:
        postcheck()
        continue
    postcheck()
    if token == b"":
        os._exit(71)
    os._exit(72)
UNIFIED KEEPER V9 SOURCE END

## 5. Childless launcher leaf source

UNIFIED LAUNCHER V9 SOURCE BEGIN
#!/usr/bin/env python3
import os
import signal
import time

# LAUNCHER is the process-group leader but not an owner.  It has no spawn,
# wait, broker, cleanup, or delegation surface.  OUTER retains the hold writer
# until LAUNCHER's role turn and requires exact SIGTERM wait status.
deadline_raw = os.environ["P27_LEAF_HOLD_DEADLINE_NS"]
if not deadline_raw.isdigit():
    os._exit(70)
deadline = int(deadline_raw, 10)
def postcheck():
    if time.monotonic_ns() > deadline:
        os._exit(70)
signal.signal(signal.SIGPIPE, signal.SIG_IGN)
postcheck()
try:
    os.close(100)
except BaseException:
    os._exit(70)
postcheck()
pgid = os.getpgrp()
postcheck()
pid = os.getpid()
postcheck()
if pgid != pid:
    os._exit(73)
while True:
    postcheck()
    try:
        token = os.read(3, 1)
    except BlockingIOError:
        time.sleep(0.002)
        postcheck()
        continue
    except InterruptedError:
        postcheck()
        continue
    postcheck()
    if token == b"":
        os._exit(74)
    os._exit(75)
UNIFIED LAUNCHER V9 SOURCE END

## 6. Childless marker and closed broker client source

UNIFIED MARKER V9 SOURCE BEGIN
#!/usr/bin/env python3
import errno
import hashlib
import os
import signal
import sys
import time

SCHEMA = b"P27E001-HOST-V9"
PROBES = (
    b"P00", b"P01C", b"P01D", b"P02", b"P03",
    b"P04", b"P05", b"P06", b"P07", b"P08",
    b"P09", b"P10", b"P11", b"P12", b"P13",
)
OPS = (
    b"E2BIG", b"INFO", b"", b"", b"",
    b"", b"EXIT23", b"", b"", b"TERM",
    b"KILL", b"CHAIN16", b"", b"BLOCK0", b"",
)
LOCAL = (b"P01D", b"P02", b"P03", b"P04", b"P06", b"P07", b"P11", b"P13")
BROKER = (b"P00", b"P01C", b"P05", b"P08", b"P09", b"P10", b"P12")
EXTRA9_HEX = b"45585452415b395d"
MAX_RESPONSE = 1048576
FRAME_NS = 1000000000
frame_state = [0, 0, 0, 0]


class MarkerFailure(Exception):
    pass


def mono():
    return time.monotonic_ns()


def before(deadline):
    now = mono()
    if now > deadline:
        raise MarkerFailure("deadline-before")


def after(deadline):
    now = mono()
    if now > deadline:
        raise MarkerFailure("deadline-after")


def checked_read(fd, count, deadline):
    before(deadline)
    try:
        data = os.read(fd, count)
    except (BlockingIOError, InterruptedError):
        after(deadline)
        return None
    after(deadline)
    return data


def checked_write(fd, data, deadline):
    before(deadline)
    try:
        count = os.write(fd, data)
    except (BlockingIOError, InterruptedError):
        after(deadline)
        return -1
    except BrokenPipeError:
        after(deadline)
        return -2
    after(deadline)
    return count


def write_all(fd, data, deadline, state):
    frame_state[state] = 1
    offset = 0
    while offset < len(data):
        count = checked_write(fd, data[offset:], deadline)
        if count == -1:
            after(deadline)
            continue
        if count <= 0 or count > len(data) - offset:
            frame_state[state] = 4
            after(deadline)
            return False
        offset += count
        frame_state[state] = 2
        after(deadline)
    frame_state[state] = 3
    after(deadline)
    return True


def read_line(fd, limit, deadline):
    data = bytearray()
    while True:
        part = checked_read(fd, 4096, deadline)
        if part is None:
            after(deadline)
            continue
        if part == b"":
            after(deadline)
            break
        data.extend(part)
        if len(data) > limit:
            raise MarkerFailure("line-limit")
        if b"\n" in part:
            after(deadline)
            break
        after(deadline)
    raw = bytes(data)
    if raw.count(b"\n") != 1 or not raw.endswith(b"\n"):
        raise MarkerFailure("line-framing")
    return raw


def read_count(fd, count, deadline):
    data = bytearray()
    while len(data) < count:
        part = checked_read(fd, count - len(data), deadline)
        if part is None:
            after(deadline)
            continue
        if part == b"":
            after(deadline)
            raise MarkerFailure("early-response-eof")
        data.extend(part)
        after(deadline)
    return bytes(data)


def close_nonthrowing(fd, deadline):
    ok = True
    try:
        os.close(fd)
    except BaseException:
        ok = False
    after(deadline)
    return ok


def drain_response(fd, deadline):
    data = bytearray()
    while True:
        part = checked_read(fd, 4096, deadline)
        if part is None:
            after(deadline)
            continue
        if part == b"":
            after(deadline)
            break
        data.extend(part)
        if len(data) > MAX_RESPONSE + 512:
            raise MarkerFailure("response-limit")
        after(deadline)
    after(deadline)
    return bytes(data)


def parse_header(raw, probe, op):
    prefix = b"RESP|probe=" + probe + b"|op=" + op + b"|bytes="
    if not raw.startswith(prefix) or not raw.endswith(b"\n"):
        raise MarkerFailure("response-header")
    count_raw = raw[len(prefix):-1]
    if len(count_raw) < 1 or len(count_raw) > 7 or not count_raw.isdigit():
        raise MarkerFailure("response-count")
    count = int(count_raw, 10)
    if count < 1 or count > MAX_RESPONSE:
        raise MarkerFailure("response-count-range")
    return count


def verify_child_line(line, probe, mode, ordinal):
    if not line.endswith(b"\n") or line.count(b"\n") != 1:
        raise MarkerFailure("child-line-framing")
    fields = line[:-1].split(b"|")
    if len(fields) != 13:
        raise MarkerFailure("p01c-thirteen-fields")
    expected_prefixes = (
        SCHEMA,
        b"probe=" + probe,
        b"mode=" + mode,
        b"instance=" + str(ordinal).encode("ascii"),
    )
    if tuple(fields[:4]) != expected_prefixes:
        raise MarkerFailure("child-prefix-semantics")
    for position, name in ((4, b"pid="), (5, b"ppid="),
                           (6, b"sid="), (7, b"pgid=")):
        if not fields[position].startswith(name):
            raise MarkerFailure("child-process-field")
        number = fields[position][len(name):]
        if not number.isdigit() or int(number, 10) <= 0:
            raise MarkerFailure("child-process-number")
    for position, name in ((8, b"image_sha="), (9, b"source_sha="),
                           (11, b"env_sha=")):
        if not fields[position].startswith(name):
            raise MarkerFailure("child-hash-field")
        value = fields[position][len(name):]
        if len(value) != 64 or any(c not in b"0123456789abcdef" for c in value):
            raise MarkerFailure("child-hash-value")
    if not fields[10].startswith(b"cwd_hex="):
        raise MarkerFailure("child-cwd-field")
    cwd_hex = fields[10][8:]
    if len(cwd_hex) < 2 or len(cwd_hex) % 2 != 0:
        raise MarkerFailure("child-cwd-value")
    if fields[12] != b"extra9=" + EXTRA9_HEX:
        raise MarkerFailure("child-extra9")


def verify_payload(probe, op, payload):
    if op == b"E2BIG":
        if payload != b"E2BIG|noncreation=proved\n":
            raise MarkerFailure("e2big-payload")
        return b"e2big-noncreation"
    if op in (b"INFO", b"EXIT23", b"TERM", b"KILL", b"BLOCK0"):
        expected_raw = {
            b"INFO": b"0", b"EXIT23": b"5888", b"TERM": b"15",
            b"KILL": b"9", b"BLOCK0": b"0",
        }[op]
        prefix = op + b"|raw=" + expected_raw + b"|"
        if not payload.startswith(prefix):
            raise MarkerFailure("child-raw-status")
        mode = op
        verify_child_line(payload[len(prefix):], probe, mode, 0)
        if op == b"KILL" and expected_raw != b"9":
            raise MarkerFailure("p09-sigkill")
        return b"one-exact-child"
    if op == b"CHAIN16":
        lines = payload.splitlines(keepends=True)
        if len(lines) != 17 or lines[0] != b"CHAIN16|count=16\n":
            raise MarkerFailure("p10-count")
        observed = [0] * 16
        for ordinal in range(16):
            prefix = (b"ordinal=" + str(ordinal).encode("ascii") +
                      b"|raw=0|")
            if not lines[ordinal + 1].startswith(prefix):
                raise MarkerFailure("p10-order-or-status")
            if observed[ordinal] != 0:
                raise MarkerFailure("p10-duplicate-observation")
            verify_child_line(lines[ordinal + 1][len(prefix):], probe,
                              b"INFO", ordinal)
            observed[ordinal] = 1
        if observed != [1] * 16:
            raise MarkerFailure("p10-missing-observation")
        # No comparison of numeric PID fields is made.  PID reuse is allowed;
        # the sixteen ordered ordinals identify sixteen spawn instances.
        return b"sixteen-ordered-observations"
    raise MarkerFailure("closed-response-op")


def broker_once(probe, op, nonce, deadline):
    request = (b"REQ|probe=" + probe + b"|op=" + op +
               b"|nonce=" + nonce + b"\n")
    if not write_all(5, request, deadline, 0):
        raise MarkerFailure("request-write-all")
    frame = drain_response(6, deadline)
    newline = frame.find(b"\n")
    if newline < 0 or newline > 255:
        raise MarkerFailure("response-header-boundary")
    header = frame[:newline + 1]
    count = parse_header(header, probe, op)
    payload_start = newline + 1
    payload_end = payload_start + count
    if payload_end < payload_start or payload_end + len(b"RESP-END\n") != len(frame):
        raise MarkerFailure("response-length-or-surplus")
    payload = frame[payload_start:payload_end]
    if frame[payload_end:] != b"RESP-END\n":
        raise MarkerFailure("response-trailer")
    after(deadline)
    semantic = verify_payload(probe, op, payload)
    after(deadline)
    return hashlib.sha256(payload).hexdigest().encode("ascii"), semantic


def local_p01d(deadline):
    keys = tuple(sorted(os.environ.keys()))
    if keys != ("LANG", "LC_ALL", "P27_ACTOR_NONCE", "P27_EXPECTED_OP",
                "P27_MARKER_SOURCE_SHA", "P27_OPERATIONAL_DEADLINE_NS",
                "P27_PROBE"):
        raise MarkerFailure("p01d-closed-environment")
    after(deadline)
    return b"closed-environment"


def local_p02(deadline):
    pid = os.getpid()
    after(deadline)
    sid = os.getsid(0)
    after(deadline)
    pgid = os.getpgrp()
    after(deadline)
    if pid <= 1 or sid <= 1 or pgid <= 1:
        raise MarkerFailure("p02-process-topology")
    return b"topology-observed"


def local_p03(deadline):
    os.fstat(1)
    after(deadline)
    os.fstat(5)
    after(deadline)
    os.fstat(6)
    after(deadline)
    return b"fixed-fd-contract"


def local_p04(deadline):
    first = mono()
    after(deadline)
    second = mono()
    after(deadline)
    if second < first:
        raise MarkerFailure("p04-clock-regression")
    return b"monotonic-clock"


def local_p06(deadline):
    cwd = os.getcwd().encode("utf-8", "strict")
    after(deadline)
    if not cwd.startswith(b"/tmp/p27-e001-host-v9/"):
        raise MarkerFailure("p06-cwd-containment")
    return b"contained-cwd"


def local_p07(deadline):
    # No filesystem mutation: this checks only already-open descriptor identity.
    one = os.fstat(1)
    after(deadline)
    if not one:
        raise MarkerFailure("p07-fstat")
    return b"closed-filesystem-api"


def local_p11(deadline):
    blocked = signal.pthread_sigmask(signal.SIG_BLOCK, set())
    after(deadline)
    if signal.SIGKILL in blocked or signal.SIGSTOP in blocked:
        raise MarkerFailure("p11-impossible-mask")
    return b"signal-mask-observed"


def local_p13(deadline):
    if SCHEMA != b"P27E001-HOST-V9" or len(PROBES) != 15:
        raise MarkerFailure("p13-schema")
    after(deadline)
    return b"terminal-framing-ready"


def run_local(probe, deadline):
    if probe == b"P01D":
        return local_p01d(deadline)
    if probe == b"P02":
        return local_p02(deadline)
    if probe == b"P03":
        return local_p03(deadline)
    if probe == b"P04":
        return local_p04(deadline)
    if probe == b"P06":
        return local_p06(deadline)
    if probe == b"P07":
        return local_p07(deadline)
    if probe == b"P11":
        return local_p11(deadline)
    if probe == b"P13":
        return local_p13(deadline)
    raise MarkerFailure("closed-local-probe")


# The bytes between EMBEDDED CHILD V9 RAW OPEN and CLOSE are an author copy of
# the standalone child region.  They are compared as raw bytes at author stop.
EMBEDDED_CHILD_SOURCE = r'''#!/usr/bin/env python3
import hashlib
import os
import signal
import sys
import time

SCHEMA = b"P27E001-HOST-V9"
MODES = (b"INFO", b"EXIT23", b"TERM", b"KILL", b"BLOCK0")
ENV_KEYS = (
    b"LANG", b"LC_ALL", b"P27_CHILD_DEADLINE_NS", b"P27_CHILD_SOURCE_SHA", b"P27_EXTRA_09",
    b"P27_IMAGE_SHA", b"P27_INSTANCE", b"P27_MODE", b"P27_PROBE",
    b"P27_SAFE_HEX", b"PYTHONHASHSEED",
)
image_fd_state = [0, -1]


class ChildFailure(Exception):
    pass


def mono():
    return time.monotonic_ns()


def after(deadline):
    if mono() > deadline:
        raise ChildFailure("deadline")


def write_all(fd, payload, deadline):
    offset = 0
    while offset < len(payload):
        after(deadline)
        try:
            count = os.write(fd, payload[offset:])
        except (BlockingIOError, InterruptedError):
            after(deadline)
            continue
        except BrokenPipeError:
            after(deadline)
            return False
        after(deadline)
        if count <= 0 or count > len(payload) - offset:
            return False
        offset += count
        after(deadline)
    return True


def image_sha(deadline):
    digest = hashlib.sha256()
    after(deadline)
    try:
        fd = os.open("/proc/self/exe", os.O_RDONLY | os.O_CLOEXEC)
    except BaseException:
        after(deadline)
        raise
    image_fd_state[1] = fd
    image_fd_state[0] = 1
    after(deadline)
    try:
        while True:
            after(deadline)
            part = os.read(fd, 1048576)
            after(deadline)
            if part == b"":
                break
            digest.update(part)
    finally:
        try:
            os.close(fd)
        finally:
            image_fd_state[1] = -1
            image_fd_state[0] = 0
            after(deadline)
    return digest.hexdigest().encode("ascii")


def environment_sha():
    if tuple(sorted(key.encode("ascii") for key in os.environ.keys())) != ENV_KEYS:
        raise ChildFailure("environment-key-set")
    raw = bytearray()
    for key in ENV_KEYS:
        raw.extend(key + b"=" + os.environ[key.decode("ascii")].encode("ascii") + b"\x00")
    return hashlib.sha256(bytes(raw)).hexdigest().encode("ascii")


def read_gate(deadline):
    while True:
        after(deadline)
        try:
            token = os.read(3, 1)
        except (BlockingIOError, InterruptedError):
            after(deadline)
            continue
        after(deadline)
        if token == b"G":
            return
        if token == b"":
            raise ChildFailure("gate-eof")
        raise ChildFailure("gate-byte")


def main():
    deadline_raw = os.environ["P27_CHILD_DEADLINE_NS"].encode("ascii")
    if not deadline_raw.isdigit():
        raise ChildFailure("deadline-value")
    deadline = int(deadline_raw, 10)
    after(deadline)
    try:
        os.close(100)
    except BaseException:
        after(deadline)
        raise ChildFailure("source-fd-close")
    after(deadline)
    if len(sys.argv) != 2:
        raise ChildFailure("argv-count")
    mode = sys.argv[1].encode("ascii")
    if mode not in MODES or os.environ["P27_MODE"].encode("ascii") != mode:
        raise ChildFailure("mode")
    probe = os.environ["P27_PROBE"].encode("ascii")
    ordinal_raw = os.environ["P27_INSTANCE"].encode("ascii")
    if not ordinal_raw.isdigit():
        raise ChildFailure("ordinal")
    ordinal = int(ordinal_raw, 10)
    source_sha = os.environ["P27_CHILD_SOURCE_SHA"].encode("ascii")
    expected_image = os.environ["P27_IMAGE_SHA"].encode("ascii")
    safe_hex = os.environ["P27_SAFE_HEX"].encode("ascii")
    actual_image = image_sha(deadline)
    after(deadline)
    if actual_image != expected_image:
        raise ChildFailure("image-sha")
    cwd = os.getcwd().encode("utf-8", "strict")
    after(deadline)
    if cwd.hex().encode("ascii") != safe_hex:
        raise ChildFailure("cwd")
    after(deadline)
    env_sha = environment_sha()
    after(deadline)
    pid = os.getpid()
    after(deadline)
    ppid = os.getppid()
    after(deadline)
    sid = os.getsid(0)
    after(deadline)
    pgid = os.getpgrp()
    after(deadline)
    fields = (
        SCHEMA,
        b"probe=" + probe,
        b"mode=" + mode,
        b"instance=" + str(ordinal).encode("ascii"),
        b"pid=" + str(pid).encode("ascii"),
        b"ppid=" + str(ppid).encode("ascii"),
        b"sid=" + str(sid).encode("ascii"),
        b"pgid=" + str(pgid).encode("ascii"),
        b"image_sha=" + actual_image,
        b"source_sha=" + source_sha,
        b"cwd_hex=" + safe_hex,
        b"env_sha=" + env_sha,
        b"extra9=" + os.environ["P27_EXTRA_09"].encode("ascii").hex().encode("ascii"),
    )
    if len(fields) != 13:
        raise ChildFailure("field-count")
    line = b"|".join(fields) + b"\n"
    if not write_all(1, line, deadline):
        raise ChildFailure("output-write-all")
    after(deadline)
    if mode == b"EXIT23":
        os._exit(23)
    if mode in (b"TERM", b"KILL"):
        read_gate(deadline)
        while True:
            time.sleep(0.01)
            after(deadline)
    if mode == b"BLOCK0":
        read_gate(deadline)
    os._exit(0)


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        os._exit(91)
'''


def main():
    deadline_raw = os.environ["P27_OPERATIONAL_DEADLINE_NS"].encode("ascii")
    if not deadline_raw.isdigit():
        raise MarkerFailure("operational-deadline")
    deadline = int(deadline_raw, 10)
    before(deadline)
    if not close_nonthrowing(100, deadline):
        raise MarkerFailure("source-fd-close")
    if len(sys.argv) != 2:
        raise MarkerFailure("argv-count")
    probe = sys.argv[1].encode("ascii")
    if probe not in PROBES or os.environ["P27_PROBE"].encode("ascii") != probe:
        raise MarkerFailure("probe")
    index = PROBES.index(probe)
    op = OPS[index]
    if os.environ["P27_EXPECTED_OP"].encode("ascii") != op:
        raise MarkerFailure("operation-binding")
    nonce = os.environ["P27_ACTOR_NONCE"].encode("ascii")
    if len(nonce) < 32 or len(nonce) > 128:
        raise MarkerFailure("nonce")
    if op == b"":
        if probe not in LOCAL:
            raise MarkerFailure("local-matrix")
        semantic = run_local(probe, deadline)
        payload_sha = hashlib.sha256(b"").hexdigest().encode("ascii")
    else:
        if probe not in BROKER:
            raise MarkerFailure("broker-matrix")
        payload_sha, semantic = broker_once(probe, op, nonce, deadline)
    if not close_nonthrowing(5, deadline):
        raise MarkerFailure("request-close")
    if not close_nonthrowing(6, deadline):
        raise MarkerFailure("response-close")
    marker_line = (SCHEMA + b"|marker=PASS|probe=" + probe + b"|op=" +
                   (op if op else b"LOCAL") + b"|semantic=" + semantic +
                   b"|payload_sha=" + payload_sha + b"|source_sha=" +
                   os.environ["P27_MARKER_SOURCE_SHA"].encode("ascii") + b"\n")
    output = marker_line + b"P27E001_HOST_V9_MARKER_PASS\n"
    if not write_all(1, output, deadline, 1):
        os._exit(92)
    after(deadline)
    if frame_state[1] != 3:
        os._exit(93)
    os._exit(0)


if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        deadline = mono() + FRAME_NS
        try:
            detail = (type(exc).__name__ + ":" + str(exc)).encode("ascii", "backslashreplace")[:256]
            write_all(1, b"P27E001-HOST-V9|marker=FAIL|detail=" + detail.hex().encode("ascii") + b"\n",
                      deadline, 2)
        except BaseException:
            pass
        os._exit(90)
UNIFIED MARKER V9 SOURCE END

## 7. Standalone nested child leaf source

NESTED CHILD V9 SOURCE BEGIN
#!/usr/bin/env python3
import hashlib
import os
import signal
import sys
import time

SCHEMA = b"P27E001-HOST-V9"
MODES = (b"INFO", b"EXIT23", b"TERM", b"KILL", b"BLOCK0")
ENV_KEYS = (
    b"LANG", b"LC_ALL", b"P27_CHILD_DEADLINE_NS", b"P27_CHILD_SOURCE_SHA", b"P27_EXTRA_09",
    b"P27_IMAGE_SHA", b"P27_INSTANCE", b"P27_MODE", b"P27_PROBE",
    b"P27_SAFE_HEX", b"PYTHONHASHSEED",
)
image_fd_state = [0, -1]


class ChildFailure(Exception):
    pass


def mono():
    return time.monotonic_ns()


def after(deadline):
    if mono() > deadline:
        raise ChildFailure("deadline")


def write_all(fd, payload, deadline):
    offset = 0
    while offset < len(payload):
        after(deadline)
        try:
            count = os.write(fd, payload[offset:])
        except (BlockingIOError, InterruptedError):
            after(deadline)
            continue
        except BrokenPipeError:
            after(deadline)
            return False
        after(deadline)
        if count <= 0 or count > len(payload) - offset:
            return False
        offset += count
        after(deadline)
    return True


def image_sha(deadline):
    digest = hashlib.sha256()
    after(deadline)
    try:
        fd = os.open("/proc/self/exe", os.O_RDONLY | os.O_CLOEXEC)
    except BaseException:
        after(deadline)
        raise
    image_fd_state[1] = fd
    image_fd_state[0] = 1
    after(deadline)
    try:
        while True:
            after(deadline)
            part = os.read(fd, 1048576)
            after(deadline)
            if part == b"":
                break
            digest.update(part)
    finally:
        try:
            os.close(fd)
        finally:
            image_fd_state[1] = -1
            image_fd_state[0] = 0
            after(deadline)
    return digest.hexdigest().encode("ascii")


def environment_sha():
    if tuple(sorted(key.encode("ascii") for key in os.environ.keys())) != ENV_KEYS:
        raise ChildFailure("environment-key-set")
    raw = bytearray()
    for key in ENV_KEYS:
        raw.extend(key + b"=" + os.environ[key.decode("ascii")].encode("ascii") + b"\x00")
    return hashlib.sha256(bytes(raw)).hexdigest().encode("ascii")


def read_gate(deadline):
    while True:
        after(deadline)
        try:
            token = os.read(3, 1)
        except (BlockingIOError, InterruptedError):
            after(deadline)
            continue
        after(deadline)
        if token == b"G":
            return
        if token == b"":
            raise ChildFailure("gate-eof")
        raise ChildFailure("gate-byte")


def main():
    deadline_raw = os.environ["P27_CHILD_DEADLINE_NS"].encode("ascii")
    if not deadline_raw.isdigit():
        raise ChildFailure("deadline-value")
    deadline = int(deadline_raw, 10)
    after(deadline)
    try:
        os.close(100)
    except BaseException:
        after(deadline)
        raise ChildFailure("source-fd-close")
    after(deadline)
    if len(sys.argv) != 2:
        raise ChildFailure("argv-count")
    mode = sys.argv[1].encode("ascii")
    if mode not in MODES or os.environ["P27_MODE"].encode("ascii") != mode:
        raise ChildFailure("mode")
    probe = os.environ["P27_PROBE"].encode("ascii")
    ordinal_raw = os.environ["P27_INSTANCE"].encode("ascii")
    if not ordinal_raw.isdigit():
        raise ChildFailure("ordinal")
    ordinal = int(ordinal_raw, 10)
    source_sha = os.environ["P27_CHILD_SOURCE_SHA"].encode("ascii")
    expected_image = os.environ["P27_IMAGE_SHA"].encode("ascii")
    safe_hex = os.environ["P27_SAFE_HEX"].encode("ascii")
    actual_image = image_sha(deadline)
    after(deadline)
    if actual_image != expected_image:
        raise ChildFailure("image-sha")
    cwd = os.getcwd().encode("utf-8", "strict")
    after(deadline)
    if cwd.hex().encode("ascii") != safe_hex:
        raise ChildFailure("cwd")
    after(deadline)
    env_sha = environment_sha()
    after(deadline)
    pid = os.getpid()
    after(deadline)
    ppid = os.getppid()
    after(deadline)
    sid = os.getsid(0)
    after(deadline)
    pgid = os.getpgrp()
    after(deadline)
    fields = (
        SCHEMA,
        b"probe=" + probe,
        b"mode=" + mode,
        b"instance=" + str(ordinal).encode("ascii"),
        b"pid=" + str(pid).encode("ascii"),
        b"ppid=" + str(ppid).encode("ascii"),
        b"sid=" + str(sid).encode("ascii"),
        b"pgid=" + str(pgid).encode("ascii"),
        b"image_sha=" + actual_image,
        b"source_sha=" + source_sha,
        b"cwd_hex=" + safe_hex,
        b"env_sha=" + env_sha,
        b"extra9=" + os.environ["P27_EXTRA_09"].encode("ascii").hex().encode("ascii"),
    )
    if len(fields) != 13:
        raise ChildFailure("field-count")
    line = b"|".join(fields) + b"\n"
    if not write_all(1, line, deadline):
        raise ChildFailure("output-write-all")
    after(deadline)
    if mode == b"EXIT23":
        os._exit(23)
    if mode in (b"TERM", b"KILL"):
        read_gate(deadline)
        while True:
            time.sleep(0.01)
            after(deadline)
    if mode == b"BLOCK0":
        read_gate(deadline)
    os._exit(0)


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        os._exit(91)
NESTED CHILD V9 SOURCE END

V9 STAGE 2 ALL FIVE SOURCE REGIONS CLOSED

## 8. Exact probe preservation matrix

The order below is the only accepted order.  There are exactly fifteen probe
IDs because P01 has the two frozen variants P01C and P01D.  A broker row emits
exactly one authenticated request; a local row emits zero request bytes.

| ordinal | probe | locus | sole broker op | child instances | exact child status or local semantic |
| ---: | --- | --- | --- | ---: | --- |
| 0 | P00 | broker | E2BIG | 0 | OSError E2BIG and proven noncreation reservation release |
| 1 | P01C | broker | INFO | 1 | exit 0; exact 13-field bytes including EXTRA[9] |
| 2 | P01D | local | none | 0 | exact seven-key marker environment |
| 3 | P02 | local | none | 0 | positive PID/SID/PGID topology observation |
| 4 | P03 | local | none | 0 | fixed descriptors 1, 5, and 6 are fstat-able |
| 5 | P04 | local | none | 0 | nonregressing monotonic clock |
| 6 | P05 | broker | EXIT23 | 1 | exact normal exit 23, raw wait status 5888 |
| 7 | P06 | local | none | 0 | canonical contained working directory |
| 8 | P07 | local | none | 0 | already-open descriptor-only filesystem observation |
| 9 | P08 | broker | TERM | 1 | exact SIGTERM, raw wait status 15 |
| 10 | P09 | broker | KILL | 1 | actual exact SIGKILL, raw wait status 9 |
| 11 | P10 | broker | CHAIN16 | 16 | sixteen ordered INFO spawn instances, each exit 0 |
| 12 | P11 | local | none | 0 | signal-mask observation with SIGKILL/SIGSTOP absent |
| 13 | P12 | broker | BLOCK0 | 1 | exact gate byte followed by exit 0 |
| 14 | P13 | local | none | 0 | schema and terminal-framing readiness |

The seven broker probes are exactly P00, P01C, P05, P08, P09, P10, and P12.
Their ops are exactly E2BIG, INFO, EXIT23, TERM, KILL, CHAIN16, and BLOCK0 in
that order.  The eight local probes are exactly P01D, P02, P03, P04, P06,
P07, P11, and P13.  OUTER does not read a request for a local probe.  For a
broker probe it accepts only the one nonce-bound canonical request, writes one
length-bound canonical response, and closes admission.  Only after the marker
has been exactly reaped does OUTER drain the request descriptor to exact EOF
and require zero surplus bytes.  Wrong, partial, malformed, duplicate, late,
or surplus requests therefore demote the candidate.

P10 is one CHAIN16 request, not sixteen requests.  It performs exactly sixteen
serial calls through the sole OUTER spawn wrapper.  Ordinals 0 through 15 are
preallocated observations and each must transition zero to one once.  Numeric
PID equality between two ordinals is expressly allowed; no PID nonreuse
premise exists.  An ordinal duplicate, missing ordinal, wrong order, wrong
bytes, or nonzero raw status demotes.

## 9. P01C canonical fields and five child modes

Every successful child observation is one LF-terminated line with exactly
thirteen pipe-separated fields in this order:

| field | exact key/semantic |
| ---: | --- |
| 1 | P27E001-HOST-V9 schema literal |
| 2 | probe= and the mapped probe ID |
| 3 | mode= and one of the five closed modes |
| 4 | instance= and the expected decimal ordinal |
| 5 | pid= and the observed positive child PID |
| 6 | ppid= and exact OUTER PID |
| 7 | sid= and exact OUTER session ID |
| 8 | pgid= and exact launcher group ID |
| 9 | image_sha= and the exact current interpreter-image SHA-256 |
| 10 | source_sha= and the bound standalone child-source SHA-256 |
| 11 | cwd_hex= and the canonical safe-directory bytes |
| 12 | env_sha= and SHA-256 of the exact sorted closed environment records |
| 13 | extra9=45585452415b395d, the canonical bytes of EXTRA[9] |

The five and only five modes are INFO, EXIT23, TERM, KILL, and BLOCK0.  P10
uses INFO with distinct ordinals rather than adding a sixth mode.  OUTER builds
the expected line from committed PID, known direct parent/session/group,
verified source, verified image, canonical cwd, and closed environment; it
requires byte equality, not merely a parseable or nonempty observation.
Marker independently checks the thirteen-field shape and mapped raw status.
P09 cannot pass on physical reap alone: WIFSIGNALED and WTERMSIG == SIGKILL are
mandatory.  The same exact-status rule applies to all other modes.

## 10. Ownership, FD, and cleanup proof

The only process owner is OUTER, which remains outside the launcher group.
Launcher L, keeper K, marker M, and the at-most-one concurrent child C are all
direct children of OUTER and are leaves.  L, K, M, and C contain zero
posix_spawn call sites and zero waitpid call sites.  Neither marker nor a leaf
can orphan cleanup-sensitive ownership.

MAX_LIVE_SLOTS is exactly four.  The sole process census is the fixed
preallocated slots array.  Before each spawn, a stable cell becomes RESERVED.
All argv, environment, file actions, source FD, role, and deadline objects
already exist.  On a successful posix_spawn return the first caller-visible
mutations are PID, raw-status sentinel, and LIVE in that same cell; they
allocate no registry object.  No validation, telemetry, map insertion,
deadline postcheck, or role lookup intervenes.  An OSError or pre-call deadline
failure releases the reservation only on the proven no-call/no-success-return
path.  The E0349 return-to-commit nonfatal-injection premise covers the exact
successful-return window.  Exact waitpid(pid) similarly commits raw status and
REAPED in the same fixed cell before any postcheck or semantic validation.
Only after exact child status and exact bytes are classified may a REAPED child
cell be cleared to FREE for the next serial P10 instance.

MAX_FD_SLOTS is exactly twenty-four.  Before ownership, the source requires a
finite RLIMIT_NOFILE no greater than 1048576, performs one bounded closerange
over every legal nonstandard descriptor, and proves fd 100 is EBADF.  Thus no
actor-supplied non-CLOEXEC descriptor survives admission.  Each later pipe,
open, and duplicate-source description is immediately committed into a stable
pre-reserved FD cell; two-cell pipe reservation rolls its first cell back if
the second cannot be reserved.  Pre-call deadline failure releases only a
proven noncreation reservation.  A successful close returns the cell to FREE;
EBADF or any other close error permanently latches failure.  EBADF is never
clean-close evidence.  Four fixed close-rescue passes cover all cells, and a
candidate is impossible while any FD cell remains RESERVED or OWNED.

Each of the four leaf source paths is opened O_NOFOLLOW, fstat-checked as a
single-link regular file, hashed and counted through its retained registered
open-file description, and kept open until all process slots are reaped.  The
description is rewound before every spawn and file actions first duplicate it
to fixed fd 100, before any action can overwrite low-number source FDs.  The
interpreter is the bound current Linux image at /proc/self/exe and reads only
/proc/self/fd/100.  The old source FD is explicitly rejected if it equals 100.
The future platform contract binds ordered POSIX_SPAWN_DUP2 semantics, target
CLOEXEC clearing, and Linux /proc/self/fd readability across exec.  Each leaf
closes fd 100 immediately after its interpreter has loaded the source.  This
is an explicit platform premise; neither POSIX, EOF, successful observation,
nor pathname stability is asserted to prove it.  No source pathname is
reopened for execution, so replacement of the original pathname cannot select
different bytes.

Cleanup first latches admission closed, performs a complete fixed census, and
only then signals.  It uses exactly this order:

    child -> marker -> launcher -> keeper.

No group TERM or KILL exists.  Every signal targets the committed exact PID.
Every reap is an exact direct-parent waitpid for that PID.  ESRCH, EOF,
telemetry, a status line, and group disappearance are never reap proof.  The
launcher and keeper hold writers stay open through their own role turns.  A
PASS candidate requires launcher alive at its turn and exact SIGTERM reap,
then keeper alive at its later turn and exact SIGTERM reap.  Premature exit,
normal exit, another signal, or SIGKILL demotes.  On failure, the actual raw
status is committed and reported while later roles still run.  Rescue is an
exact-PID SIGKILL followed by exact direct wait; it must observe SIGKILL and
permanently demotes regardless of later evidence.  Keeper is exact-PID last.

The cleanup implementation is nonthrowing at its boundary.  Close, signal,
wait, deadline, state, and classification errors set preallocated fault cells
and later fixed-census work continues.  A role has one selection instant and
one shared role deadline; retries cannot mint a new horizon.  The operational
deadline is permanently latched before cleanup and cannot be erased by the
separate cleanup guard.

## 11. Progress horizons and framing closure

The five forced-cleanup subhorizons are separately armed and all clamp to the
one selection-based KILL_REAP_PROGRESS_NS and the shared role/global guard:

1. selection to exact pre-signal return: PRE_SIGNAL_CONTROL_NS;
2. actual successful TERM return to cooperative reap: TERM_ALLOWANCE_NS;
3. actual TERM-window completion to SIGKILL retry return: EINTR_SYSCALL_NS;
4. actual successful SIGKILL return to exact waitpid commit:
   EXACT_KILL_WAIT_NS;
5. actual exact-wait return to status/error accounting: RESCUE_ACCOUNT_NS.

The worst-case sum is exactly 170000000 ns.  A late substep latches failure;
it cannot borrow unused time by changing the named duration.  Three ordinary
roles plus keeper, the census gate, terminal framing, and exit entry match the
overflow-checked 960000000 ns host-after-operation bound.  The OWNER progress
lease covers source/FD admission, every ownership transition, cleanup, all
result/marker/terminal write-all transitions and immediate postchecks, and the
three direct source transitions into os._exit.  It does not stop when the last
slot becomes REAPED.

Result, marker bytes, and candidate terminal use bounded write-all loops.
Every short write, zero write, EPIPE, EOF, EINTR retry, read/drain break, wait
return, and framing transition has an immediate deadline postcheck.  A
candidate terminal is not selected until the complete result and marker bytes
and their postchecks succeed.  The only positive terminal emitted by HOST is
P27E001_HOST_V9_CANDIDATE_PASS: it is explicitly not a completed PASS.  No
host check after that frame rewrites its textual strength.  The future actor
accepts it only together with exact host exit status 0 and the separate
ACTOR_ACK_PROGRESS_NS observation/ACK.  A nonzero exit, missing exit, timeout,
partial frame, missing ACK, or wrong ACK rejects it.  Host completion and actor
ACK completion are therefore distinct bounds.

Neither the progress lease nor SIGKILL completion is inferred from POSIX.
E0349 explicitly excludes starvation, freezer/ptrace suspension, SIGSTOP,
unbounded I/O/kernel sleep, owner fatal injection, and permanent signaling
failure during accepted operation.  The Linux RLIMIT/closerange bound,
ordered DUP2/fd100 behavior, timely signal/wait return, and three-transition
exit entry are positive future-run premises.  If any premise is not bound, the
candidate is unavailable; the author does not reinterpret an observation as
proof of the premise.

## 12. Closed path, API, and safety surface

The four source paths and safe directory arrive as fixed actor arguments.
Every source path must be a child of the canonical safe directory; NUL,
parent traversal, trailing-slash ambiguity, symlink source open, nonregular
source, and multi-link source are rejected.  OUTER changes cwd once to that
safe directory.  Child cwd bytes must equal its canonical hex.  The only
special read-only image paths are /proc/self/exe and the inherited
/proc/self/fd/100.  No build, evidence, repository-root, network, device,
shell, or user-selected path is in the runtime surface.

The closed process API is posix_spawn in OUTER only; fork, clone, subprocess,
shell, eval, exec-from-path-search, pidfd, subreaper, prctl, and daemonization
are absent.  The closed ownership API is the fixed slot arrays, exact-PID kill,
and exact-PID waitpid.  Group signaling, signal.pause, ancestor reap claims,
pipe-EOF reap claims, PID-only side maps, and dynamically sorted cleanup lists
are absent.  The closed FD API is preownership closerange, fixed-cell pipe/open
ownership, fstat/read/write/lseek/close, and ordered spawn DUP2 actions.  Hash
operations consume only bytes already read from those fixed descriptions.

Framing is strict ASCII with LF only.  Nonce, probe, operation, byte count,
response trailer, child line, marker terminal, host candidate terminal, and
exit status must all agree.  Status text and physical reap are necessary but
never alone sufficient semantic evidence.

## 13. Thirty-two V9 correction classes

V9 has exactly thirty-two correction classes:

1. flattened OUTER sole process ownership;
2. four-cell preallocated process registry;
3. stable pre-spawn reservation and proven-noncreation release;
4. immediate nonallocating successful-spawn commit;
5. immediate nonallocating exact-wait commit;
6. twenty-four-cell preallocated FD registry;
7. inherited-FD admission close and fd100 rejection;
8. partial two-FD reservation rollback;
9. EBADF-as-failure and successful-close recycling;
10. retained verified-source open-file descriptions;
11. ordered fd100 source installation before low-FD overwrite;
12. actor-independent flattened launcher/keeper/marker/child leaves;
13. admission latch plus complete pre-signal census;
14. nonthrowing exhaustive cleanup fault accumulation;
15. one shared role selection and global cleanup clamp;
16. independently armed PRE_SIGNAL duration;
17. actual-TERM-return TERM duration;
18. independently armed EINTR retry duration;
19. actual-SIGKILL-return exact-wait duration;
20. actual-wait-return rescue accounting;
21. child-to-marker-to-launcher-to-keeper physical order;
22. hold-writer preservation through launcher/keeper turns;
23. exact launcher then keeper SIGTERM PASS matrices;
24. exact SIGKILL rescue status with permanent demotion;
25. exact seven-broker/eight-local probe split;
26. one authenticated request plus post-marker EOF/no-surplus;
27. exact five child modes and per-mode raw statuses;
28. P09 actual SIGKILL and P10 sixteen ordered PID-reuse-tolerant instances;
29. P01C thirteen-field/EXTRA[9] byte equality;
30. exact source/image/cwd/environment semantics;
31. bounded result/marker/candidate write-all and immediate edge postchecks;
32. lease-through-exit candidate semantics with separate future actor ACK.

## 14. Raw lexical call map and staged author assertions

Raw lexical inspection of the five source regions gives this ownership map:

| source | os.posix_spawn call sites | os.waitpid call sites | os.kill call sites | killpg | signal.pause |
| --- | ---: | ---: | ---: | ---: | ---: |
| OUTER | 1 | 2 | 3 | 0 | 0 |
| KEEPER | 0 | 0 | 0 | 0 | 0 |
| LAUNCHER | 0 | 0 | 0 | 0 | 0 |
| MARKER, including its inert embedded child copy | 0 | 0 | 0 | 0 | 0 |
| standalone CHILD | 0 | 0 | 0 | 0 | 0 |

The one OUTER spawn site is the immediate fixed-slot wrapper used for L, K,
M, and serial C instances.  The two OUTER wait sites are the operational exact
wait wrapper and the nonthrowing cleanup exact-wait wrapper.  The three kill
sites are operational child TERM, operational child KILL, and cleanup exact
PID signaling.  No side source owns or reaps a process.

At this staged boundary, authoring execution counts are all zero: embedded
source imports 0, language/AST parses 0, compiles 0, evaluations 0, launches 0,
fixture/marker/payload executions 0, and build/evidence/root accesses 0.  Only
inert raw-byte/text reads and apply_patch writes to this exact V9 path occurred.

V9 STAGED PRESERVATION PROOF AND CENSUS COMPLETE

## 15. Author identity and inert closure

Raw extraction between the ten unique source delimiter lines, excluding the
delimiter lines themselves and retaining each final LF, gives:

| V9 source | bytes | LF | SHA-256 |
| --- | ---: | ---: | --- |
| OUTER | 55645 | 1454 | 100e14f6c6f21cf3ba8dedf39adee92adc7c5b583f14fdd03b8ec72cf4784268 |
| KEEPER | 1007 | 38 | 1a4433f4f2f282790852357b2fabd753da4ef75c52504c5d270b7ac0483fc2df |
| LAUNCHER | 1022 | 43 | 031cf45a7e8ea1c17336fd22d6ba6b83902c72cde8783964d7297bb372d9e35f |
| MARKER, including its inert embedded child copy | 18864 | 616 | b165a0a62f11def502c80d595d2eb30ecc0813c5fa8578b8ec9c2e78a85cea70 |
| standalone CHILD | 5225 | 186 | 12a81663e633c7cab5cb03da666aa5262ba0f9afa840076e80cf52d2bf8d7ba5 |

The raw embedded child body is independently 5225 bytes, 186 LF, SHA-256
12a81663e633c7cab5cb03da666aa5262ba0f9afa840076e80cf52d2bf8d7ba5,
exactly equal to the standalone CHILD region.  The four leaf hashes and
byte/LF counts embedded in OUTER agree with this table.

Raw lexical call counts agree with Section 14.  The process ownership census
is one OUTER posix_spawn call site and two OUTER waitpid call sites; all four
non-OUTER sources have zero of both.  Group kill and signal.pause counts are
zero.  The source delimiters occur once each.  Before this closure append, the
file was strict ASCII with CR 0, NUL 0, HT 0, high-byte 0, disallowed-control
0, final byte LF, and no author-stop occurrence; the final raw check below is
required to reproduce those properties for the completed file.

The E0349 parent ledger was re-read only as inert bytes and remains dev 2431,
ino 12439253869, mode 0644, nlink 1, uid/gid 0, 2078115 bytes, 22241 LF,
SHA-256 b2fd36caf5414f41f57e6ffb000df36978ef2159529d87a3d67e8cfde659e3ea,
with unique final terminal
BATCH07_P27_PROBE_RECOVERY_E001_HOST_V9_PREAUTHOR_SPECIFICATION_CORRECTED_AND_CONTROL_REAUTHORIZED.
The qualified manifest remains frozen at 135 rows, 21715 bytes, 135 LF, and
SHA-256 7b315ceae9d93c29877a02f5e50eccfcdf1ce95d50341617c94e3cb0dd9e50b7.

Host V8 was re-read only as inert bytes and remains dev 2431, ino 5916180464,
mode 0644, nlink 1, uid/gid 0, 74973 bytes, 1071 LF, SHA-256
72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf.
Its five frozen source identities also remain:

| V8 source | bytes | LF | SHA-256 |
| --- | ---: | ---: | --- |
| OUTER | 23612 | 285 | e8c18c6385124e5e61ff86fec3fdf4464f1034c7ee278dd2a3e17b638480bcec |
| KEEPER | 1243 | 23 | 8bdd1f75edc7c85296e4790a866be1a413452bad05984c06b40518b81278ec9d |
| LAUNCHER | 1159 | 24 | 8f6ab849192ac9865eacc8b60adcca71172f81e292dafa1860787093b43825b2 |
| MARKER | 20735 | 201 | 29368b0df7e005f4f182f097d61ece17aedebded47037568fe3bdda36a2fe36f |
| CHILD | 2827 | 42 | 0e48b1ad9511470c37268dd79fb41a098afb2baa60a8ea604780bc349c760d78 |

No predecessor, ledger, manifest, Binder, actor, derivation, build, evidence,
or root artifact was written.  This exact V9 note is the sole authored path.
Execution remained zero: no embedded import, language/AST parse, compile,
evaluation, launch, marker run, payload run, fixture run, or probe run occurred.
This is an inert author stop, not a claim of future execution success or a
formal reviewer approval.

BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V9_AUTHOR_STOP
