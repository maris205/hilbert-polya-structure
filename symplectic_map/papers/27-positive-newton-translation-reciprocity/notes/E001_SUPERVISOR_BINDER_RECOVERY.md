# E001 posix-spawn supervisor and failure binder

## 1. Authority, precedence, and inertness

This append-only control is the sole notes artifact authorized by
B07-E0315-P27-PROBE-RECOVERY-E001-SUPERVISOR-BINDER-POSIX-SPAWN-
ARCHITECTURE-CORRECTION-AUTHORIZATION.  Its authoring input is the exact
E0315 physical ledger prefix:

- bytes 1676581;
- LF 19438;
- SHA-256
  85cbc12527320c918a6dd00b9e7d6992ed0672710130ec6d9936352933d09ca9;
- terminal
  BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_POSIX_SPAWN_ARCHITECTURE_CORRECTION_AUTHORIZED.

E0315 explicitly supersedes only E0314's rejected Python-after-fork and
prctl architecture.  E0314's W2 failure, conservative durability phases,
complete candidate schema, no-retry rule, and all no-execution boundaries
remain normative.  E001_FIRST_COPY_RECOVERY.md remains byte-immutable.
Its marker-delimited payload is copied without changing one byte.

This file grants no execution authority.  The program below is inert text.
Authoring, extraction, hashing, and review may not import, parse, compile,
or execute it.  No build path may be named, opened, listed, stated, or
probed during authoring or static review.

The program has exactly three modes: supervisor, watchdog, and
recovery-binder.  It contains no fork, subprocess, preexec_fn, ctypes,
prctl, eval, compile, dynamic import, temporary file, PTY, tee, shell
substitution, cleanup, repair, backfill, or retry path.  Both child
transitions use os.posix_spawn with an empty exec environment.  The
watchdog transition directly execs the frozen Python tool with explicit
-I -S -B -P -X utf8 flags.  Its exec environment and resulting runtime
environment are both empty; hash randomization remains enabled, and every
serialization that could otherwise depend on hash order is explicitly
sorted or emitted in fixed literal order.

## 2. Frozen inputs and process boundary

Before any payload spawn, both supervisor and watchdog verify the E0315
ledger prefix, the exact supplemental control, its raw and normalized
payload transports, the exact recovery controls and source, the exact
E0280 raw and normalized transports, the exact fully substituted inner,
and the frozen env, Bash, and Python tool identities.  The E0315 prefix is
verified as a prefix because the required durable pending-attempt event is
an append to the same ledger after the watchdog becomes ready.

The frozen payload identities are raw
22671/714/02834994db821c0dcf9b6c06e58511686d0786b9012c68ce89af6de52806bbcb
and normalized
22670/713/6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0.
The exact E0280 identities are raw
454/13/f003386d98e60443011e85204651a44c99a9dc7c41aba4989b9e4f619fa40a09
and normalized
453/12/72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd.
The fully substituted four-line inner has 22965 bytes, 716 LF, no terminal
LF, final bytes 29,27, and SHA-256
e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f.

Every mode starts in the exact workspace, as euid and egid zero, with
umask 077, soft and hard RLIMIT_NOFILE 4096 and 1048576, exact Python
3.12 flags, and separate live non-PTY binary pipes at fd0, fd1, and fd2.
Supervisor and recovery-binder use the exact ten-key environment.
Watchdog uses the exact empty environment and isolated flags above.  A
two-pass fcntl F_GETFD scan over
0 through 4095 accepts exactly 0/1/2 in supervisor and recovery-binder
mode and exactly 0/1/2/10/11 in watchdog mode.  No procfs enumeration is
used.  Every mode binds an empty signal mask.  Both posix_spawn calls pass
an empty mask and reset every catchable inherited disposition, explicitly
including SIGPIPE and SIGCHLD, before exec.

The supervisor creates only two pipe2 O_CLOEXEC pairs.  It maps the
lifeline/start read end to watchdog fd10 and the ready write end to
watchdog fd11, starts the watchdog with setsid, and checks that watchdog
PID, session ID, and process-group ID are equal.  The watchdog and the
payload remain in that one dedicated process group.  The frozen payload
does not fork, setsid, or change process group.

The handshake is exact.  The watchdog writes one byte R and closes fd11.
The supervisor accepts R followed by EOF, emits the canonical BEGIN line,
and reads exactly one byte A from inherited fd0.  It then closes only its
own fd0; the watchdog already inherited a separate live reference, and
the payload never reads it.  The external executor
must first validate BEGIN and durably append a pending-attempt ledger
event containing the supervisor PID, watchdog session PGID, and
attempt_consumed=0.  Only after that durable append may it write A.  The
supervisor then writes one byte S while retaining the lifeline writer.
Receipt of S is the unique attempt-consumption point.  The payload later
inherits the still-live fd0.

## 3. Exact literal three-mode program

The normalized program is the exact byte substring after the BEGIN
marker's LF and before the LF immediately preceding the END marker.  The
delimiter LF is not passed to Python.  The normalized program has zero
single-quote, dollar, and backtick bytes.  The markers occur exactly once.
Static delimiter-only extraction at author stop gives raw bytes 60797,
raw LF 1788, and raw SHA-256
b79615b4dfe407006e829b553547b030735446a737a6e78200da997c9604794c.
Removing exactly the final delimiter LF gives normalized bytes 60796,
normalized LF 1787, 1788 physical lines, final byte 41, and SHA-256
b077e3bb0fca88f065311558d30d74c044c6929624e78257c64721bff9c86f2e.
The normalized byte census is single-quote 0, dollar 0, and backtick 0.

BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_PROGRAM_BEGIN
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import stat
import sys
import time

WORK = b"/root/autodl-tmp/symplectic_map"
PYTHON = b"/root/miniconda3/bin/python3"
ENV_TOOL = b"/usr/bin/env"
BASH_TOOL = b"/usr/bin/bash"
STATUS_NAME = b"BATCH_07_STATUS.md"
SELF_NAME = b"E001_SUPERVISOR_BINDER_RECOVERY.md"
PAYLOAD_CONTROL_NAME = b"E001_FIRST_COPY_RECOVERY.md"
SOURCE_NAME = b"BUILD_VALIDATOR_RECOVERY.py"
COPY_NAME = b"BUILD_VALIDATOR_RECOVERY.py"
STATUS_RECEIPT_NAME = b"E001.status"
STDERR_RECEIPT_NAME = b"E001.stderr"
STDOUT_RECEIPT_NAME = b"E001.stdout"
CANDIDATE_NAMES = (
    COPY_NAME,
    STATUS_RECEIPT_NAME,
    STDERR_RECEIPT_NAME,
    STDOUT_RECEIPT_NAME,
)
WORK_COMPONENTS = (
    b"root",
    b"autodl-tmp",
    b"symplectic_map",
)
NOTES_COMPONENTS = WORK_COMPONENTS + (
    b"papers",
    b"27-positive-newton-translation-reciprocity",
    b"notes",
)
EVIDENCE_COMPONENTS = WORK_COMPONENTS + (
    b"papers",
    b"27-positive-newton-translation-reciprocity",
    b"build",
    b"recovery-6103a9df0c3d-evidence",
)
USR_BIN_COMPONENTS = (
    b"usr",
    b"bin",
)
PYTHON_BIN_COMPONENTS = (
    b"root",
    b"miniconda3",
    b"bin",
)
EXPECTED_ENV = {
    b"LANG": b"C",
    b"LC_ALL": b"C",
    b"PATH": b"/usr/bin:/bin",
    b"PYTHONDONTWRITEBYTECODE": b"1",
    b"PYTHONHASHSEED": b"0",
    b"PYTHONIOENCODING": b"UTF-8:strict",
    b"PYTHONNOUSERSITE": b"1",
    b"PYTHONSAFEPATH": b"1",
    b"PYTHONUTF8": b"1",
    b"TZ": b"UTC",
}
STATUS_PREFIX_BYTES = 1676581
STATUS_PREFIX_LF = 19438
STATUS_PREFIX_SHA256 = "85cbc12527320c918a6dd00b9e7d6992ed0672710130ec6d9936352933d09ca9"
STATUS_PREFIX_TERMINAL = (
    b"BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_POSIX_SPAWN_"
    b"ARCHITECTURE_CORRECTION_AUTHORIZED\n"
)
SOURCE_DEV = 2431
SOURCE_INO = 5913826453
SOURCE_BYTES = 398310
SOURCE_LF = 9366
SOURCE_SHA256 = "6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817"
SOURCE_TERMINAL = b"# BATCH07_P27_BUILD_VALIDATOR_RECOVERY_AUTHOR_STOP\n"
EVIDENCE_DEV = 2431
EVIDENCE_INO = 14502900794
EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
STATUS_RECEIPT_SHA256 = "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"
PASS_SHA256 = "b149a22827939aff6a6875a4797076a7e32f8ada246dee0e2f3a7aa490247c5b"
PASS_LINE = (
    b"PASS E001_FIRST_COPY_RECOVERY evidence_dev=2431 evidence_ino=14502900794 "
    b"copy_bytes=398310 copy_LF=9366 "
    b"copy_sha256=6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817 "
    b"inventory_items=4 inventory_framing_bytes=64 "
    b"inventory_sha256=7aeb029ca886a47abeb0bd05a4f941c820983dc6e90925880ff7e297f92dbcde\n"
)
FIXED_NOTE_SPECS = (
    (
        PAYLOAD_CONTROL_NAME,
        40449,
        1103,
        "bb652a6a17e08a668795a23a7e16fa15be1c93e17923b76edf2f2e2e0d0152da",
        b"BATCH07_P27_E001_FIRST_COPY_RECOVERY_AUTHOR_STOP\n",
        None,
        None,
    ),
    (
        b"BUILD_PROFILE_RECOVERY.md",
        62863,
        1181,
        "ac1651c8ef5522f76f52b98a9deb300d5409c489d6e3ae4fa58e9d6e3fc4c985",
        b"BATCH07_P27_BUILD_PROFILE_RECOVERY_AUTHOR_STOP\n",
        None,
        None,
    ),
    (
        b"INDEPENDENT_BUILD_PROFILE_RECOVERY_REVIEW.md",
        15279,
        306,
        "c39970d11af0d0a7b0e46dde61485eb6629bb0d560541989a984b4982d597202",
        b"BATCH07_P27_INDEPENDENT_BUILD_PROFILE_RECOVERY_REVIEW_PASS\n",
        None,
        None,
    ),
    (
        SOURCE_NAME,
        SOURCE_BYTES,
        SOURCE_LF,
        SOURCE_SHA256,
        SOURCE_TERMINAL,
        SOURCE_DEV,
        SOURCE_INO,
    ),
    (
        b"VALIDATOR_LOCK_RECOVERY.md",
        64169,
        1173,
        "5601233185ca0d880f8e38a8b9ec2fdd174d95aebceb692d3c020d29f5c5f1be",
        b"BATCH07_P27_VALIDATOR_LOCK_RECOVERY_AUTHOR_STOP\n",
        None,
        None,
    ),
    (
        b"INDEPENDENT_VALIDATOR_RECOVERY_REVIEW.md",
        17140,
        346,
        "49669351a3a92ef2aea3303dfde64b71d1dde7b43eb0e29293506d7f6da7d9f9",
        b"BATCH07_P27_VALIDATOR_RECOVERY_REVIEW_PASS\n",
        None,
        None,
    ),
)
NOATIME = os.O_NOATIME
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC | NOATIME
READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | NOATIME
PATH_FLAGS = os.O_PATH | os.O_NOFOLLOW | os.O_CLOEXEC | NOATIME
CHUNK = 65536
STDOUT_CAP = 4096
STDERR_CAP = 65536
CANDIDATE_CAP = 1048576
INVENTORY_ITEMS_CAP = 64
INVENTORY_RAW_CAP = 16384
BINDER_CAP = 131072
RESULT_CAP = 524288
READY_DEADLINE_NS = 30000000000
ACK_DEADLINE_NS = 300000000000
PAYLOAD_DEADLINE_NS = 30000000000
KILL_REAP_GRACE_NS = 5000000000
PIPE_EOF_GRACE_NS = 1000000000
WATCHDOG_DEADLINE_NS = 60000000000
POLL_SLICE_MS = 100
QUOTE = bytes((39,))
DOLLAR = bytes((36,))
TICK = bytes((96,))
CODE_TEXT = (
    sys.orig_argv[sys.orig_argv.index("-c") + 1]
    if "-c" in sys.orig_argv and sys.orig_argv.index("-c") + 1 < len(sys.orig_argv)
    else ""
)
CODE_BYTES = CODE_TEXT.encode("ascii", "strict")
OPEN_FDS = set()
WATCHDOG_PID = 0

class Stop(BaseException):
    def __init__(self, code):
        self.code = code

def stop(code):
    raise Stop(code)

def need(value, code):
    if not value:
        stop(code)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def node_key(value):
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_nlink,
        value.st_uid,
        value.st_gid,
        value.st_rdev,
        value.st_size,
    )

def dir_key(value):
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_nlink,
        value.st_uid,
        value.st_gid,
        value.st_rdev,
    )

def track(fd):
    need(fd >= 0 and fd not in OPEN_FDS, "fd-track")
    OPEN_FDS.add(fd)
    return fd

def close_fd(fd):
    if fd in OPEN_FDS:
        OPEN_FDS.remove(fd)
    try:
        os.close(fd)
        return True
    except BaseException:
        return False

def close_all():
    good = True
    for fd in sorted(tuple(OPEN_FDS), reverse=True):
        if not close_fd(fd):
            good = False
    return good

def pread_exact(fd, size):
    need(size >= 0, "read-size")
    parts = []
    offset = 0
    while offset < size:
        amount = min(CHUNK, size - offset)
        piece = os.pread(fd, amount, offset)
        need(len(piece) == amount, "read-short")
        parts.append(piece)
        offset += amount
    return b"".join(parts)

def pread_complete(fd, size):
    data = pread_exact(fd, size)
    need(os.pread(fd, 1, size) == b"", "read-eof")
    return data

def write_all(fd, data):
    offset = 0
    while offset < len(data):
        try:
            amount = os.write(fd, data[offset:])
        except InterruptedError:
            continue
        need(amount > 0, "write-zero")
        offset += amount

def fd_census():
    found = []
    flags = {}
    for fd in range(4096):
        try:
            value = fcntl.fcntl(fd, fcntl.F_GETFD)
        except OSError as error:
            if error.errno == errno.EBADF:
                continue
            stop("fd-census")
        found.append(fd)
        flags[fd] = value
    return tuple(found), flags

def runtime(mode, expected_fds):
    if mode == "supervisor":
        need(sys.argv == ["-c", mode], "argv")
        expected_orig = [
            PYTHON.decode("ascii"),
            "-S",
            "-B",
            "-P",
            "-c",
            CODE_TEXT,
            mode,
        ]
        expected_environment = EXPECTED_ENV
        expected_isolated = 0
        expected_ignore_environment = 0
        expected_hash_randomization = 0
    elif mode == "watchdog":
        need(sys.argv == ["-c", mode], "argv")
        expected_orig = [
            PYTHON.decode("ascii"),
            "-I",
            "-S",
            "-B",
            "-P",
            "-X",
            "utf8",
            "-c",
            CODE_TEXT,
            mode,
        ]
        expected_environment = {}
        expected_isolated = 1
        expected_ignore_environment = 1
        expected_hash_randomization = 1
    else:
        need(
            len(sys.argv) == 4
            and sys.argv[0] == "-c"
            and sys.argv[1] == mode,
            "argv",
        )
        expected_orig = [
            PYTHON.decode("ascii"),
            "-S",
            "-B",
            "-P",
            "-c",
            CODE_TEXT,
            mode,
            sys.argv[2],
            sys.argv[3],
        ]
        expected_environment = EXPECTED_ENV
        expected_isolated = 0
        expected_ignore_environment = 0
        expected_hash_randomization = 0
    need(sys.orig_argv == expected_orig, "orig-argv")
    need(sys.implementation.name == "cpython", "implementation")
    need(sys.version_info[:2] == (3, 12), "version")
    need(sys.flags.no_site == 1, "flag-site")
    need(sys.flags.dont_write_bytecode == 1, "flag-bytecode")
    need(sys.flags.safe_path, "flag-safe-path")
    need(
        sys.flags.isolated == expected_isolated
        and sys.flags.ignore_environment == expected_ignore_environment,
        "flag-env",
    )
    need(sys.flags.utf8_mode == 1, "flag-utf8")
    need(sys.flags.hash_randomization == expected_hash_randomization, "flag-hash")
    need(dict(os.environb) == expected_environment, "environment")
    need(os.getcwdb() == WORK, "cwd")
    need(os.geteuid() == 0 and os.getegid() == 0, "identity")
    old_mask = os.umask(0o077)
    os.umask(old_mask)
    need(old_mask == 0o077, "umask")
    need(resource.getrlimit(resource.RLIMIT_NOFILE) == (4096, 1048576), "nofile")
    blocked = signal.pthread_sigmask(signal.SIG_BLOCK, set())
    need(len(blocked) == 0, "signal-mask")
    first, first_flags = fd_census()
    second, second_flags = fd_census()
    need(first == expected_fds and second == expected_fds, "fd-set")
    need(first_flags == second_flags, "fd-flags-drift")
    for fd in expected_fds:
        need(first_flags[fd] == 0, "fd-cloexec")
    base = []
    for fd in (0, 1, 2):
        value = os.fstat(fd)
        need(stat.S_ISFIFO(value.st_mode), "standard-not-pipe")
        base.append((value.st_dev, value.st_ino))
    need(len(set(base)) == 3, "standard-alias")
    need(CODE_BYTES.decode("ascii", "strict").encode("ascii") == CODE_BYTES, "code-ascii")
    need(
        CODE_BYTES.count(QUOTE) == 0
        and CODE_BYTES.count(DOLLAR) == 0
        and CODE_BYTES.count(TICK) == 0,
        "code-census",
    )

class Chain:
    def __init__(self, components):
        self.components = components
        self.fds = []
        self.keys = []
        fd = track(os.open(b"/", DIR_FLAGS))
        self.fds.append(fd)
        self.keys.append(dir_key(os.fstat(fd)))
        for component in components:
            fd = track(os.open(component, DIR_FLAGS, dir_fd=fd))
            self.fds.append(fd)
            self.keys.append(dir_key(os.fstat(fd)))

    def leaf(self):
        return self.fds[-1]

    def rewalk(self):
        fresh = Chain(self.components)
        good = fresh.keys == self.keys
        closed = fresh.close()
        need(good and closed, "chain-drift")

    def close(self):
        good = True
        for fd in reversed(self.fds):
            if fd in OPEN_FDS and not close_fd(fd):
                good = False
        self.fds = []
        return good

class Record:
    def __init__(self, chain, name, value, data):
        self.chain = chain
        self.name = name
        self.fd = value
        self.key = node_key(os.fstat(value))
        self.data = data

    def verify(self):
        need(node_key(os.fstat(self.fd)) == self.key, "held-file-drift")
        need(pread_complete(self.fd, len(self.data)) == self.data, "held-file-content")
        before = os.stat(self.name, dir_fd=self.chain.leaf(), follow_symlinks=False)
        need(node_key(before) == self.key, "path-file-drift")
        fresh = track(os.open(self.name, READ_FLAGS, dir_fd=self.chain.leaf()))
        try:
            need(node_key(os.fstat(fresh)) == self.key, "fresh-file-drift")
            need(pread_complete(fresh, len(self.data)) == self.data, "fresh-file-content")
        finally:
            need(close_fd(fresh), "fresh-file-close")

    def close(self):
        if self.fd in OPEN_FDS:
            return close_fd(self.fd)
        return True

def open_fixed(chain, spec):
    name, size, lf, digest, terminal, dev, ino = spec
    before = os.stat(name, dir_fd=chain.leaf(), follow_symlinks=False)
    need(stat.S_ISREG(before.st_mode), "fixed-type")
    need(stat.S_IMODE(before.st_mode) == 0o644, "fixed-mode")
    need(before.st_nlink == 1 and before.st_uid == 0 and before.st_gid == 0, "fixed-owner")
    need(before.st_size == size, "fixed-size")
    if dev is not None:
        need(before.st_dev == dev and before.st_ino == ino, "fixed-node")
    fd = track(os.open(name, READ_FLAGS, dir_fd=chain.leaf()))
    after = os.fstat(fd)
    need(node_key(after) == node_key(before), "fixed-open-race")
    data = pread_complete(fd, size)
    need(data.count(b"\n") == lf and sha(data) == digest, "fixed-content")
    need(data.endswith(terminal), "fixed-terminal")
    return Record(chain, name, fd, data)

def open_dynamic(chain, name, cap):
    before = os.stat(name, dir_fd=chain.leaf(), follow_symlinks=False)
    need(stat.S_ISREG(before.st_mode), "dynamic-type")
    need(stat.S_IMODE(before.st_mode) == 0o644, "dynamic-mode")
    need(before.st_nlink == 1 and before.st_uid == 0 and before.st_gid == 0, "dynamic-owner")
    need(0 <= before.st_size <= cap, "dynamic-size")
    fd = track(os.open(name, READ_FLAGS, dir_fd=chain.leaf()))
    need(node_key(os.fstat(fd)) == node_key(before), "dynamic-open-race")
    data = pread_complete(fd, before.st_size)
    return Record(chain, name, fd, data)

def open_tool(chain, name, size, digest):
    before = os.stat(name, dir_fd=chain.leaf(), follow_symlinks=False)
    need(stat.S_ISREG(before.st_mode), "tool-type")
    need(stat.S_IMODE(before.st_mode) == 0o755, "tool-mode")
    need(before.st_nlink == 1 and before.st_uid == 0 and before.st_gid == 0, "tool-owner")
    need(before.st_size == size, "tool-size")
    fd = track(os.open(name, READ_FLAGS, dir_fd=chain.leaf()))
    need(node_key(os.fstat(fd)) == node_key(before), "tool-open-race")
    data = pread_complete(fd, size)
    need(sha(data) == digest, "tool-content")
    return Record(chain, name, fd, data)

def extract_between(data, begin, end, code):
    need(data.count(begin) == 1 and data.count(end) == 1, code)
    left = data.index(begin) + len(begin)
    right = data.index(end, left)
    need(right > left, code)
    return data[left:right]

def extract_payload(data):
    begin = (
        b"BATCH07_P27_RECOVERY_E001_FIRST_"
        b"COPY_HARNESS_BEGIN\n"
    )
    end = (
        b"BATCH07_P27_RECOVERY_E001_FIRST_"
        b"COPY_HARNESS_END\n"
    )
    raw = extract_between(data, begin, end, "payload-markers")
    need(
        len(raw) == 22671
        and raw.count(b"\n") == 714
        and sha(raw) == "02834994db821c0dcf9b6c06e58511686d0786b9012c68ce89af6de52806bbcb",
        "payload-raw",
    )
    need(raw.endswith(b"\n"), "payload-delimiter")
    normalized = raw[:-1]
    need(
        len(normalized) == 22670
        and normalized.count(b"\n") == 713
        and sha(normalized) == "6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0"
        and normalized[-1:] == b")",
        "payload-normalized",
    )
    need(
        normalized.count(QUOTE) == 0
        and normalized.count(DOLLAR) == 0
        and normalized.count(TICK) == 0,
        "payload-census",
    )
    return normalized

def extract_self(data):
    begin = (
        b"BATCH07_P27_RECOVERY_E001_SUPERVISOR_"
        b"BINDER_PROGRAM_BEGIN\n"
    )
    end = (
        b"BATCH07_P27_RECOVERY_E001_SUPERVISOR_"
        b"BINDER_PROGRAM_END\n"
    )
    raw = extract_between(data, begin, end, "self-markers")
    need(raw.endswith(b"\n") and raw[:-1] == CODE_BYTES, "self-transport")
    need(
        CODE_BYTES.count(QUOTE) == 0
        and CODE_BYTES.count(DOLLAR) == 0
        and CODE_BYTES.count(TICK) == 0,
        "self-census",
    )

def extract_launcher(status_data):
    prefix = (
        b"liveness_corrected_launcher_script_exact_"
        b"lines:\n"
        + TICK * 3
        + b"text\n"
    )
    suffix = TICK * 3 + b"\nliveness_guard_rule:"
    raw = extract_between(status_data, prefix, suffix, "launcher-markers")
    need(
        len(raw) == 454
        and raw.count(b"\n") == 13
        and sha(raw) == "f003386d98e60443011e85204651a44c99a9dc7c41aba4989b9e4f619fa40a09"
        and raw.endswith(b"\n"),
        "launcher-raw",
    )
    normalized = raw[:-1]
    need(
        len(normalized) == 453
        and normalized.count(b"\n") == 12
        and sha(normalized) == "72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd"
        and normalized[-1:] == b"\x22",
        "launcher-normalized",
    )
    return normalized

def build_inner(payload):
    inner = (
        b"set -C\n"
        b"umask 077\n"
        b"cd -- /root/autodl-tmp/symplectic_map || exit 125\n"
        b"exec /usr/bin/env -i "
        b"LANG=C LC_ALL=C PATH=/usr/bin:/bin "
        b"PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 "
        b"PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 "
        b"PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC "
        b"/root/miniconda3/bin/python3 -S -B -P -c "
        + QUOTE
        + payload
        + QUOTE
    )
    need(
        len(inner) == 22965
        and inner.count(b"\n") == 716
        and sha(inner) == "e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f"
        and inner[-2:] == b")" + QUOTE,
        "inner",
    )
    return inner

def verify_status_prefix():
    chain = Chain(WORK_COMPONENTS)
    try:
        before = os.stat(STATUS_NAME, dir_fd=chain.leaf(), follow_symlinks=False)
        need(stat.S_ISREG(before.st_mode), "status-type")
        need(stat.S_IMODE(before.st_mode) == 0o644, "status-mode")
        need(before.st_nlink == 1 and before.st_uid == 0 and before.st_gid == 0, "status-owner")
        need(before.st_size >= STATUS_PREFIX_BYTES, "status-size")
        fd = track(os.open(STATUS_NAME, READ_FLAGS, dir_fd=chain.leaf()))
        try:
            after = os.fstat(fd)
            need(
                after.st_dev == before.st_dev
                and after.st_ino == before.st_ino
                and after.st_mode == before.st_mode
                and after.st_nlink == before.st_nlink
                and after.st_uid == before.st_uid
                and after.st_gid == before.st_gid
                and after.st_size >= STATUS_PREFIX_BYTES,
                "status-open-race",
            )
            data = pread_exact(fd, STATUS_PREFIX_BYTES)
            need(
                len(data) == STATUS_PREFIX_BYTES
                and data.count(b"\n") == STATUS_PREFIX_LF
                and sha(data) == STATUS_PREFIX_SHA256
                and data.endswith(STATUS_PREFIX_TERMINAL),
                "status-prefix",
            )
            launcher = extract_launcher(data)
        finally:
            need(close_fd(fd), "status-close")
        chain.rewalk()
        return launcher
    finally:
        need(chain.close(), "status-chain-close")

class ToolLink:
    def __init__(self, chain, name, target):
        self.chain = chain
        self.name = name
        self.target = target
        self.key = node_key(os.stat(name, dir_fd=chain.leaf(), follow_symlinks=False))
        self.verify()

    def verify(self):
        value = os.stat(self.name, dir_fd=self.chain.leaf(), follow_symlinks=False)
        need(node_key(value) == self.key, "tool-link-drift")
        need(stat.S_ISLNK(value.st_mode), "tool-link-type")
        need(stat.S_IMODE(value.st_mode) == 0o777 and value.st_nlink == 1, "tool-link-mode")
        need(value.st_uid == 0 and value.st_gid == 0 and value.st_size == len(self.target), "tool-link-owner")
        need(os.readlink(self.name, dir_fd=self.chain.leaf()) == self.target, "tool-link-target")
        need(
            node_key(os.stat(self.name, dir_fd=self.chain.leaf(), follow_symlinks=False))
            == self.key,
            "tool-link-race",
        )

class Preflight:
    def __init__(self):
        self.launcher = verify_status_prefix()
        self.notes = Chain(NOTES_COMPONENTS)
        self.records = []
        for spec in FIXED_NOTE_SPECS:
            self.records.append(open_fixed(self.notes, spec))
        self.self_record = open_dynamic(self.notes, SELF_NAME, 1048576)
        need(
            self.self_record.data.endswith(
                b"BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_AUTHOR_STOP\n"
            ),
            "self-terminal",
        )
        extract_self(self.self_record.data)
        payload_record = self.records[0]
        self.payload = extract_payload(payload_record.data)
        self.inner = build_inner(self.payload)
        self.source = self.records[3]
        self.usr_bin = Chain(USR_BIN_COMPONENTS)
        self.env_record = open_tool(
            self.usr_bin,
            b"env",
            43976,
            "85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0",
        )
        self.bash_record = open_tool(
            self.usr_bin,
            b"bash",
            1396520,
            "59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4",
        )
        self.python_bin = Chain(PYTHON_BIN_COMPONENTS)
        self.python_link = ToolLink(self.python_bin, b"python3", b"python3.12")
        self.python_record = open_tool(
            self.python_bin,
            b"python3.12",
            30626264,
            "9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101",
        )
        self.payload_argv = (
            ENV_TOOL,
            b"-i",
            BASH_TOOL,
            b"--noprofile",
            b"--norc",
            b"-c",
            self.launcher,
            b"batch07-p27-successor-liveness-fd-scrub-launcher",
            self.inner,
        )
        need(len(self.payload_argv) == 9, "payload-argv")

    def verify(self):
        self.notes.rewalk()
        for record in self.records:
            record.verify()
        self.self_record.verify()
        extract_self(self.self_record.data)
        need(extract_payload(self.records[0].data) == self.payload, "payload-drift")
        need(build_inner(self.payload) == self.inner, "inner-drift")
        self.usr_bin.rewalk()
        self.env_record.verify()
        self.bash_record.verify()
        self.python_bin.rewalk()
        self.python_link.verify()
        self.python_record.verify()

    def close(self):
        good = True
        for record in self.records:
            if not record.close():
                good = False
        if not self.self_record.close():
            good = False
        if not self.env_record.close():
            good = False
        if not self.bash_record.close():
            good = False
        if not self.python_record.close():
            good = False
        if not self.notes.close():
            good = False
        if not self.usr_bin.close():
            good = False
        if not self.python_bin.close():
            good = False
        return good

def signal_defaults():
    values = []
    for value in signal.valid_signals():
        number = int(value)
        if number not in (int(signal.SIGKILL), int(signal.SIGSTOP)):
            values.append(number)
    return tuple(sorted(values))

SIGNAL_DEFAULTS = signal_defaults()

def wait_deadline(pid, deadline):
    while True:
        got, status_value = os.waitpid(pid, os.WNOHANG)
        if got == pid:
            return status_value
        need(got == 0, "waitpid-other")
        if time.monotonic_ns() >= deadline:
            return None
        time.sleep(0.01)

def read_one_with_eof(fd, deadline):
    os.set_blocking(fd, False)
    poller = select.poll()
    poller.register(fd, select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL)
    data = bytearray()
    eof = False
    while not eof:
        remaining = deadline - time.monotonic_ns()
        need(remaining > 0, "ready-timeout")
        events = poller.poll(min(POLL_SLICE_MS, max(1, (remaining + 999999) // 1000000)))
        for current, mask in events:
            need(current == fd and not mask & select.POLLNVAL, "ready-poll")
            while True:
                try:
                    piece = os.read(fd, 2)
                except BlockingIOError:
                    break
                if piece == b"":
                    eof = True
                    break
                data.extend(piece)
                need(len(data) <= 1, "ready-extra")
    return bytes(data)

def read_ack(deadline):
    os.set_blocking(0, False)
    poller = select.poll()
    poller.register(0, select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL)
    while True:
        remaining = deadline - time.monotonic_ns()
        need(remaining > 0, "ack-timeout")
        events = poller.poll(min(POLL_SLICE_MS, max(1, (remaining + 999999) // 1000000)))
        for fd, mask in events:
            need(fd == 0 and not mask & select.POLLNVAL, "ack-poll")
            piece = os.read(0, 1)
            need(piece == b"A", "ack-byte")
            os.set_blocking(0, True)
            return

def begin_line(watchdog_pid):
    supervisor_pid = os.getpid()
    need(supervisor_pid > 1 and watchdog_pid > 1, "pid")
    value = (
        "BEGIN E001_SUPERVISOR_BINDER_RECOVERY version=1 supervisor_pid="
        + str(supervisor_pid)
        + " watchdog_pid="
        + str(watchdog_pid)
        + " session_pgid="
        + str(watchdog_pid)
        + " program_bytes="
        + str(len(CODE_BYTES))
        + " program_LF="
        + str(CODE_BYTES.count(b"\n"))
        + " program_sha256="
        + sha(CODE_BYTES)
        + " payload_sha256=6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0"
        + " launcher_sha256=72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd"
        + " inner_sha256=e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f"
        + " attempt_consumed=0\n"
    ).encode("ascii")
    need(len(value) < 1024, "begin-cap")
    return value

def type_name(mode):
    if stat.S_ISREG(mode):
        return "regular"
    if stat.S_ISDIR(mode):
        return "directory"
    if stat.S_ISLNK(mode):
        return "symlink"
    if stat.S_ISFIFO(mode):
        return "fifo"
    if stat.S_ISSOCK(mode):
        return "socket"
    if stat.S_ISCHR(mode):
        return "char"
    if stat.S_ISBLK(mode):
        return "block"
    return "unknown"

def inventory(fd):
    raw = []
    complete = 1
    raw_bytes = 0
    with os.scandir(fd) as iterator:
        for entry in iterator:
            item = os.fsencode(entry.name)
            need(os.fsdecode(item).encode(sys.getfilesystemencoding(), "surrogateescape") == item, "name-roundtrip")
            need(item not in (b".", b"..") and b"/" not in item and b"\x00" not in item, "name-invalid")
            if len(raw) >= INVENTORY_ITEMS_CAP or raw_bytes + len(item) > INVENTORY_RAW_CAP:
                complete = 0
                break
            raw.append(item)
            raw_bytes += len(item)
    raw.sort()
    need(len(raw) == len(set(raw)), "inventory-duplicate")
    frame = b"".join(
        str(len(item)).encode("ascii") + b":" + item.hex().encode("ascii") + b"\n"
        for item in raw
    )
    need(len(frame) <= BINDER_CAP, "inventory-frame-cap")
    return tuple(raw), frame, complete

def absent_record(name):
    return {
        "name": name,
        "state": "absent",
        "absence": "ENOENT",
        "type": "none",
        "dev": "none",
        "ino": "none",
        "mode": "none",
        "nlink": "none",
        "uid": "none",
        "gid": "none",
        "rdev": "none",
        "bytes": "none",
        "lf": "none",
        "sha": "none",
        "content": "absent",
        "valid": 0,
        "key": None,
        "fds": [],
    }

def observe_candidate(dir_fd, evidence_dev, name):
    try:
        before = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            return absent_record(name)
        stop("candidate-lstat")
    path_fd = track(os.open(name, PATH_FLAGS, dir_fd=dir_fd))
    need(node_key(os.fstat(path_fd)) == node_key(before), "candidate-path-race")
    record = {
        "name": name,
        "state": "present",
        "absence": "none",
        "type": type_name(before.st_mode),
        "dev": str(before.st_dev),
        "ino": str(before.st_ino),
        "mode": format(before.st_mode, "07o"),
        "nlink": str(before.st_nlink),
        "uid": str(before.st_uid),
        "gid": str(before.st_gid),
        "rdev": str(before.st_rdev),
        "bytes": "none",
        "lf": "none",
        "sha": "none",
        "content": "not-regular",
        "valid": 0,
        "key": node_key(before),
        "fds": [path_fd],
    }
    data = None
    if stat.S_ISREG(before.st_mode):
        if before.st_size <= CANDIDATE_CAP:
            read_fd = track(os.open(name, READ_FLAGS, dir_fd=dir_fd))
            need(
                os.fstat(read_fd).st_dev == before.st_dev
                and os.fstat(read_fd).st_ino == before.st_ino,
                "candidate-read-race",
            )
            data = pread_complete(read_fd, before.st_size)
            record["fds"].append(read_fd)
            record["bytes"] = str(len(data))
            record["lf"] = str(data.count(b"\n"))
            record["sha"] = sha(data)
            record["content"] = "complete"
        else:
            record["bytes"] = str(before.st_size)
            record["content"] = "unavailable-size-cap"
    expected = None
    if name == COPY_NAME:
        expected = (0o500, SOURCE_BYTES, SOURCE_LF, SOURCE_SHA256)
    elif name == STATUS_RECEIPT_NAME:
        expected = (0o600, 2, 1, STATUS_RECEIPT_SHA256)
    elif name in (STDERR_RECEIPT_NAME, STDOUT_RECEIPT_NAME):
        expected = (0o600, 0, 0, EMPTY_SHA256)
    if expected is not None and data is not None:
        mode, size, lf, digest = expected
        record["valid"] = int(
            stat.S_ISREG(before.st_mode)
            and before.st_dev == evidence_dev
            and stat.S_IMODE(before.st_mode) == mode
            and before.st_nlink == 1
            and before.st_uid == 0
            and before.st_gid == 0
            and before.st_rdev == 0
            and len(data) == size
            and data.count(b"\n") == lf
            and sha(data) == digest
            and (name != STATUS_RECEIPT_NAME or data == b"0\n")
        )
    return record

def close_candidate(record):
    good = True
    for fd in reversed(record["fds"]):
        if fd in OPEN_FDS and not close_fd(fd):
            good = False
    record["fds"] = []
    return good

def candidate_signature(record):
    return (
        record["name"],
        record["state"],
        record["absence"],
        record["type"],
        record["dev"],
        record["ino"],
        record["mode"],
        record["nlink"],
        record["uid"],
        record["gid"],
        record["rdev"],
        record["bytes"],
        record["lf"],
        record["sha"],
        record["content"],
        record["valid"],
        record["key"],
    )

def candidate_line(index, record):
    return (
        "CANDIDATE index="
        + str(index)
        + " name_hex="
        + record["name"].hex()
        + " state="
        + record["state"]
        + " absence="
        + record["absence"]
        + " type="
        + record["type"]
        + " dev="
        + record["dev"]
        + " ino="
        + record["ino"]
        + " mode="
        + record["mode"]
        + " nlink="
        + record["nlink"]
        + " uid="
        + record["uid"]
        + " gid="
        + record["gid"]
        + " rdev="
        + record["rdev"]
        + " bytes="
        + record["bytes"]
        + " LF="
        + record["lf"]
        + " sha256="
        + record["sha"]
        + " content_state="
        + record["content"]
        + " exact_expected="
        + str(record["valid"])
        + "\n"
    ).encode("ascii")

def classify_phase(records, names, inventory_complete, recovery, pass_seen, duplicate_pairs, source_aliases):
    if recovery:
        return "unknown-mismatch"
    if inventory_complete != 1:
        return "unknown-mismatch"
    mapping = {record["name"]: record for record in records}
    present = tuple(name for name in (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME, COPY_NAME, STATUS_RECEIPT_NAME) if mapping[name]["state"] == "present")
    exact = all(mapping[name]["valid"] == 1 for name in present)
    inventory_exact = set(names) == set(present) and len(names) == len(present)
    clean_relations = len(duplicate_pairs) == 0 and len(source_aliases) == 0
    if not exact or not inventory_exact or not clean_relations:
        return "unknown-mismatch"
    if present == ():
        return "pre-create"
    if present == (STDOUT_RECEIPT_NAME,):
        return "stdout-present-last-durability-unproven"
    if present == (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME):
        return "stdout-durable-and-stderr-present-last-durability-unproven"
    if present == (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME, COPY_NAME):
        return "stdout-stderr-durable-and-copy-present-last-durability-unproven"
    if present == (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME, COPY_NAME, STATUS_RECEIPT_NAME):
        if pass_seen:
            return "all-four-durable-post-emission-failure"
        return "first-three-durable-and-status-present-last-durability-unproven"
    return "unknown-mismatch"

def binder_core(source_record, recovery, pass_seen):
    chain = None
    first_records = []
    second_records = []
    try:
        source_value = os.fstat(source_record.fd)
        source_data = pread_complete(source_record.fd, SOURCE_BYTES)
        need(
            source_value.st_dev == SOURCE_DEV
            and source_value.st_ino == SOURCE_INO
            and stat.S_ISREG(source_value.st_mode)
            and stat.S_IMODE(source_value.st_mode) == 0o644
            and source_value.st_nlink == 1
            and source_value.st_uid == 0
            and source_value.st_gid == 0
            and source_value.st_rdev == 0
            and len(source_data) == SOURCE_BYTES
            and source_data.count(b"\n") == SOURCE_LF
            and sha(source_data) == SOURCE_SHA256
            and source_data.endswith(SOURCE_TERMINAL),
            "binder-source",
        )
        chain = Chain(EVIDENCE_COMPONENTS)
        evidence = os.fstat(chain.leaf())
        need(
            evidence.st_dev == EVIDENCE_DEV
            and evidence.st_ino == EVIDENCE_INO
            and stat.S_ISDIR(evidence.st_mode)
            and stat.S_IMODE(evidence.st_mode) == 0o700
            and evidence.st_nlink == 2
            and evidence.st_uid == 0
            and evidence.st_gid == 0
            and evidence.st_rdev == 0,
            "binder-evidence",
        )
        first_names, first_frame, first_complete = inventory(chain.leaf())
        for name in CANDIDATE_NAMES:
            first_records.append(observe_candidate(chain.leaf(), evidence.st_dev, name))
        repeated_names, repeated_frame, repeated_complete = inventory(chain.leaf())
        if first_complete == 1:
            need(
                repeated_complete == 1
                and first_names == repeated_names
                and first_frame == repeated_frame,
                "binder-inventory-drift",
            )
        duplicate_pairs = []
        source_aliases = []
        for left in range(len(first_records)):
            record = first_records[left]
            if record["state"] == "present":
                pair = (int(record["dev"]), int(record["ino"]))
                if pair == (SOURCE_DEV, SOURCE_INO):
                    source_aliases.append(str(left))
                for right in range(left + 1, len(first_records)):
                    other = first_records[right]
                    if other["state"] == "present" and pair == (int(other["dev"]), int(other["ino"])):
                        duplicate_pairs.append(str(left) + "-" + str(right))
        chain.rewalk()
        fresh = Chain(EVIDENCE_COMPONENTS)
        try:
            need(fresh.keys == chain.keys, "binder-terminal-chain")
            terminal_names, terminal_frame, terminal_complete = inventory(fresh.leaf())
            if first_complete == 1:
                need(
                    terminal_complete == 1
                    and terminal_names == first_names
                    and terminal_frame == first_frame,
                    "binder-terminal-inventory",
                )
            for name in CANDIDATE_NAMES:
                second_records.append(observe_candidate(fresh.leaf(), evidence.st_dev, name))
            need(
                tuple(candidate_signature(item) for item in second_records)
                == tuple(candidate_signature(item) for item in first_records),
                "binder-terminal-candidates",
            )
        finally:
            for record in second_records:
                need(close_candidate(record), "binder-terminal-candidate-close")
            second_records = []
            need(fresh.close(), "binder-terminal-chain-close")
        phase = classify_phase(
            first_records,
            first_names,
            int(first_complete == 1 and repeated_complete == 1 and terminal_complete == 1),
            recovery,
            pass_seen,
            duplicate_pairs,
            source_aliases,
        )
        mode = "recovery-binder" if recovery else "watchdog"
        lines = [
            (
                "BINDER version=1 status=ok mode="
                + mode
                + " durability_phase="
                + phase
                + "\n"
            ).encode("ascii"),
            (
                "SOURCE state=present type=regular dev="
                + str(source_value.st_dev)
                + " ino="
                + str(source_value.st_ino)
                + " mode="
                + format(source_value.st_mode, "07o")
                + " nlink="
                + str(source_value.st_nlink)
                + " uid="
                + str(source_value.st_uid)
                + " gid="
                + str(source_value.st_gid)
                + " rdev="
                + str(source_value.st_rdev)
                + " bytes="
                + str(len(source_data))
                + " LF="
                + str(source_data.count(b"\n"))
                + " sha256="
                + sha(source_data)
                + "\n"
            ).encode("ascii"),
            (
                "EVIDENCE state=present type=directory dev="
                + str(evidence.st_dev)
                + " ino="
                + str(evidence.st_ino)
                + " mode="
                + format(evidence.st_mode, "07o")
                + " nlink="
                + str(evidence.st_nlink)
                + " uid="
                + str(evidence.st_uid)
                + " gid="
                + str(evidence.st_gid)
                + " rdev="
                + str(evidence.st_rdev)
                + "\n"
            ).encode("ascii"),
            (
                "INVENTORY items="
                + str(len(first_names))
                + " complete="
                + str(int(first_complete == 1 and repeated_complete == 1 and terminal_complete == 1))
                + " framing_kind="
                + ("full" if first_complete == 1 else "capped-prefix")
                + " framing_bytes="
                + str(len(first_frame))
                + " framing_LF="
                + str(first_frame.count(b"\n"))
                + " sha256="
                + sha(first_frame)
                + " frame_hex="
                + first_frame.hex()
                + "\n"
            ).encode("ascii"),
        ]
        for index, record in enumerate(first_records):
            lines.append(candidate_line(index, record))
        lines.append(
            (
                "RELATIONS duplicate_pairs="
                + (",".join(duplicate_pairs) if duplicate_pairs else "none")
                + " source_aliases="
                + (",".join(source_aliases) if source_aliases else "none")
                + "\n"
            ).encode("ascii")
        )
        lines.append(
            b"PROVENANCE status_receipt=payload-created-synthetic-nonauthoritative "
            b"wait_status=watchdog-waitpid-authoritative "
            b"stream_capture=watchdog-separate-raw-pipes\n"
        )
        lines.append(b"BINDER_END\n")
        report = b"".join(lines)
        need(len(report) <= BINDER_CAP, "binder-cap")
        for record in first_records:
            need(close_candidate(record), "binder-candidate-close")
        first_records = []
        need(chain.close(), "binder-chain-close")
        chain = None
        return report, "ok", phase
    except BaseException:
        for record in second_records:
            close_candidate(record)
        for record in first_records:
            close_candidate(record)
        if chain is not None:
            chain.close()
        report = (
            b"BINDER version=1 status=error mode="
            + (b"recovery-binder" if recovery else b"watchdog")
            + b" durability_phase=unknown-mismatch error=bounded-audit-failure\n"
            + b"PROVENANCE status_receipt=payload-created-synthetic-nonauthoritative "
            + b"wait_status=watchdog-waitpid-authoritative "
            + b"stream_capture=watchdog-separate-raw-pipes\n"
            + b"BINDER_END\n"
        )
        return report, "error", "unknown-mismatch"

def empty_capture():
    return {
        "out": bytearray(),
        "err": bytearray(),
        "out_total": 0,
        "err_total": 0,
        "out_lf": 0,
        "err_lf": 0,
        "out_hash": hashlib.sha256(),
        "err_hash": hashlib.sha256(),
        "out_overflow": 0,
        "err_overflow": 0,
        "out_eof": 0,
        "err_eof": 0,
        "timeout": 0,
        "supervisor_lost": 0,
        "capture_error": "none",
        "wait_raw": None,
        "wait_kind": "none",
        "exit_code": None,
        "signal": None,
        "core": 0,
        "payload_spawned": 0,
        "recovery_pgid": "none",
    }

def capture_piece(state, key, piece, cap):
    state[key + "_total"] += len(piece)
    state[key + "_lf"] += piece.count(b"\n")
    state[key + "_hash"].update(piece)
    stored = state[key]
    available = cap - len(stored)
    if available > 0:
        stored.extend(piece[:available])
    if len(piece) > available:
        state[key + "_overflow"] = 1

def kill_payload(pid):
    try:
        os.kill(pid, signal.SIGKILL)
    except OSError as error:
        if error.errno != errno.ESRCH:
            stop("payload-kill")

def capture_payload(pid, out_fd, err_fd, life_fd):
    state = empty_capture()
    state["payload_spawned"] = 1
    os.set_blocking(out_fd, False)
    os.set_blocking(err_fd, False)
    os.set_blocking(life_fd, False)
    poller = select.poll()
    masks = select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL
    poller.register(out_fd, masks)
    poller.register(err_fd, masks)
    poller.register(life_fd, masks)
    open_streams = {out_fd: "out", err_fd: "err"}
    deadline = time.monotonic_ns() + PAYLOAD_DEADLINE_NS
    kill_time = None
    reaped_time = None
    killed = False
    while True:
        now = time.monotonic_ns()
        if state["wait_raw"] is None:
            got, wait_value = os.waitpid(pid, os.WNOHANG)
            if got == pid:
                state["wait_raw"] = wait_value
                reaped_time = now
            elif got != 0:
                stop("payload-wait")
        if state["wait_raw"] is None and now >= deadline:
            state["timeout"] = 1
        if state["out_overflow"] or state["err_overflow"] or state["timeout"] or state["supervisor_lost"] or state["capture_error"] != "none":
            if not killed and state["wait_raw"] is None:
                kill_payload(pid)
                killed = True
                kill_time = now
        if kill_time is not None and state["wait_raw"] is None and now - kill_time >= KILL_REAP_GRACE_NS:
            state["capture_error"] = "reap-grace"
            return state, False
        if state["wait_raw"] is not None and not open_streams:
            break
        if reaped_time is not None and open_streams and now - reaped_time >= PIPE_EOF_GRACE_NS:
            state["capture_error"] = "eof-grace"
            return state, False
        events = poller.poll(POLL_SLICE_MS)
        for fd, mask in events:
            if mask & select.POLLNVAL:
                state["capture_error"] = "pollnval"
                continue
            if fd == life_fd:
                while True:
                    try:
                        piece = os.read(life_fd, CHUNK)
                    except BlockingIOError:
                        break
                    except OSError:
                        state["capture_error"] = "lifeline-read"
                        break
                    if piece == b"":
                        state["supervisor_lost"] = 1
                        poller.unregister(life_fd)
                        break
                    state["capture_error"] = "lifeline-data"
                continue
            if fd in open_streams:
                key = open_streams[fd]
                while True:
                    try:
                        piece = os.read(fd, CHUNK)
                    except BlockingIOError:
                        break
                    except OSError:
                        state["capture_error"] = key + "-read"
                        poller.unregister(fd)
                        close_fd(fd)
                        del open_streams[fd]
                        break
                    if piece == b"":
                        state[key + "_eof"] = 1
                        poller.unregister(fd)
                        close_fd(fd)
                        del open_streams[fd]
                        break
                    capture_piece(
                        state,
                        key,
                        piece,
                        STDOUT_CAP if key == "out" else STDERR_CAP,
                    )
    value = state["wait_raw"]
    if os.WIFEXITED(value):
        state["wait_kind"] = "exit"
        state["exit_code"] = os.WEXITSTATUS(value)
    elif os.WIFSIGNALED(value):
        state["wait_kind"] = "signal"
        state["signal"] = os.WTERMSIG(value)
        if hasattr(os, "WCOREDUMP"):
            state["core"] = int(os.WCOREDUMP(value))
    else:
        state["wait_kind"] = "other"
    return state, state["out_eof"] == 1 and state["err_eof"] == 1

def probe_lifeline(fd):
    os.set_blocking(fd, False)
    try:
        piece = os.read(fd, 1)
    except BlockingIOError:
        return True
    except OSError:
        return False
    return False if piece == b"" else False

def result_line(mode, state, binder, binder_status, phase, disposition, close_error):
    def optional(value):
        return "none" if value is None else str(value)
    fields = (
        "RESULT E001_SUPERVISOR_BINDER_RECOVERY"
        + " version=1"
        + " mode="
        + mode
        + " recovery_pgid="
        + state["recovery_pgid"]
        + " attempt_consumed=1"
        + " payload_spawned="
        + str(state["payload_spawned"])
        + " payload_success="
        + str(int(disposition == "SUCCESS"))
        + " supervisor_lost="
        + str(state["supervisor_lost"])
        + " timeout="
        + str(state["timeout"])
        + " stdout_overflow="
        + str(state["out_overflow"])
        + " stderr_overflow="
        + str(state["err_overflow"])
        + " capture_error="
        + state["capture_error"]
        + " wait_raw="
        + optional(state["wait_raw"])
        + " wait_kind="
        + state["wait_kind"]
        + " exit_code="
        + optional(state["exit_code"])
        + " signal="
        + optional(state["signal"])
        + " core="
        + str(state["core"])
        + " stdout_eof="
        + str(state["out_eof"])
        + " stderr_eof="
        + str(state["err_eof"])
        + " stdout_bytes="
        + str(state["out_total"])
        + " stdout_stored_bytes="
        + str(len(state["out"]))
        + " stdout_LF="
        + str(state["out_lf"])
        + " stdout_sha256="
        + state["out_hash"].hexdigest()
        + " stdout_hex_kind="
        + ("prefix" if state["out_overflow"] else "full")
        + " stdout_hex="
        + (bytes(state["out"]).hex() if state["out"] else "none")
        + " stderr_bytes="
        + str(state["err_total"])
        + " stderr_stored_bytes="
        + str(len(state["err"]))
        + " stderr_LF="
        + str(state["err_lf"])
        + " stderr_sha256="
        + state["err_hash"].hexdigest()
        + " stderr_hex_kind="
        + ("prefix" if state["err_overflow"] else "full")
        + " stderr_hex="
        + (bytes(state["err"]).hex() if state["err"] else "none")
        + " binder_status="
        + binder_status
        + " durability_phase="
        + phase
        + " binder_bytes="
        + str(len(binder))
        + " binder_LF="
        + str(binder.count(b"\n"))
        + " binder_sha256="
        + sha(binder)
        + " binder_hex="
        + (binder.hex() if binder else "none")
        + " internal_close_error="
        + str(close_error)
        + " disposition="
        + disposition
        + "\n"
    )
    value = fields.encode("ascii")
    need(len(value) <= RESULT_CAP, "result-cap")
    return value

def emit_and_exit(value, code):
    try:
        write_all(1, value)
    except BaseException:
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)
    try:
        os.close(1)
    except BaseException:
        os._exit(1)
    os._exit(code)

def finalize_watchdog(preflight, state, safe, forced_error):
    if forced_error != "none" and state["capture_error"] == "none":
        state["capture_error"] = forced_error
    if not safe:
        preflight.close()
        close_all()
        os._exit(1)
    if 10 in OPEN_FDS and not probe_lifeline(10):
        state["supervisor_lost"] = 1
        if state["capture_error"] == "none":
            state["capture_error"] = "final-lifeline"
    pass_seen = (
        state["out_eof"] == 1
        and state["err_eof"] == 1
        and state["out_overflow"] == 0
        and state["err_overflow"] == 0
        and bytes(state["out"]) == PASS_LINE
        and state["out_total"] == 308
        and state["out_lf"] == 1
        and state["out_hash"].hexdigest() == PASS_SHA256
        and state["err_total"] == 0
        and state["err_hash"].hexdigest() == EMPTY_SHA256
    )
    success = (
        pass_seen
        and state["wait_kind"] == "exit"
        and state["exit_code"] == 0
        and state["timeout"] == 0
        and state["supervisor_lost"] == 0
        and state["capture_error"] == "none"
    )
    input_drift = False
    try:
        preflight.verify()
    except BaseException:
        input_drift = True
        state["capture_error"] = "input-drift"
        success = False
    binder = b""
    binder_status = "not-run"
    phase = "not-applicable"
    if not success:
        binder, binder_status, phase = binder_core(preflight.source, False, pass_seen)
        try:
            preflight.verify()
        except BaseException:
            prior_sha = sha(binder)
            prior_bytes = len(binder)
            binder = (
                b"BINDER version=1 status=error mode=watchdog "
                b"durability_phase=unknown-mismatch error=input-terminal-drift "
                b"prior_binder_bytes="
                + str(prior_bytes).encode("ascii")
                + b" prior_binder_sha256="
                + prior_sha.encode("ascii")
                + b"\nBINDER_END\n"
            )
            binder_status = "error"
            phase = "unknown-mismatch"
            input_drift = True
            state["capture_error"] = "input-terminal-drift"
    closed = preflight.close()
    closed = close_all() and closed
    for fd in (0, 2):
        try:
            os.close(fd)
        except BaseException:
            closed = False
    disposition = "SUCCESS" if success and closed and not input_drift else "PERMANENT_FAILURE"
    exit_code = 0
    if not closed:
        exit_code = 1
        if binder_status == "not-run":
            binder_status = "recovery-required"
            phase = "unknown-mismatch"
        state["capture_error"] = "internal-close"
    value = result_line(
        "watchdog",
        state,
        binder,
        binder_status,
        phase,
        disposition,
        int(not closed),
    )
    emit_and_exit(value, exit_code)

def supervisor_mode():
    global WATCHDOG_PID
    runtime("supervisor", (0, 1, 2))
    preflight = Preflight()
    preflight.verify()
    need(preflight.close() and close_all(), "supervisor-preflight-close")
    life_read, life_write = os.pipe2(os.O_CLOEXEC)
    ready_read, ready_write = os.pipe2(os.O_CLOEXEC)
    for fd in (life_read, life_write, ready_read, ready_write):
        track(fd)
    need(len({life_read, life_write, ready_read, ready_write, 0, 1, 2, 10, 11}) == 9, "supervisor-fd-collision")
    watchdog_argv = (
        PYTHON,
        b"-I",
        b"-S",
        b"-B",
        b"-P",
        b"-X",
        b"utf8",
        b"-c",
        CODE_BYTES,
        b"watchdog",
    )
    actions = (
        (os.POSIX_SPAWN_DUP2, life_read, 10),
        (os.POSIX_SPAWN_DUP2, ready_write, 11),
        (os.POSIX_SPAWN_CLOSE, life_read),
        (os.POSIX_SPAWN_CLOSE, life_write),
        (os.POSIX_SPAWN_CLOSE, ready_read),
        (os.POSIX_SPAWN_CLOSE, ready_write),
    )
    pid = os.posix_spawn(
        PYTHON,
        watchdog_argv,
        {},
        file_actions=actions,
        setsigmask=(),
        setsigdef=SIGNAL_DEFAULTS,
        setsid=True,
    )
    need(pid > 1, "watchdog-pid")
    WATCHDOG_PID = pid
    need(close_fd(life_read) and close_fd(ready_write), "supervisor-opposite-close")
    ready = read_one_with_eof(ready_read, time.monotonic_ns() + READY_DEADLINE_NS)
    need(close_fd(ready_read), "supervisor-ready-close")
    need(ready == b"R", "ready-byte")
    need(os.getsid(pid) == pid and os.getpgid(pid) == pid, "watchdog-session")
    write_all(1, begin_line(pid))
    read_ack(time.monotonic_ns() + ACK_DEADLINE_NS)
    need(close_fd(0), "supervisor-stdin-close")
    write_all(life_write, b"S")
    status_value = wait_deadline(pid, time.monotonic_ns() + WATCHDOG_DEADLINE_NS)
    if status_value is None:
        close_fd(life_write)
        status_value = wait_deadline(pid, time.monotonic_ns() + KILL_REAP_GRACE_NS)
        if status_value is None:
            try:
                os.killpg(pid, signal.SIGKILL)
            except OSError as error:
                if error.errno != errno.ESRCH:
                    stop("watchdog-killpg")
            status_value = wait_deadline(pid, time.monotonic_ns() + KILL_REAP_GRACE_NS)
    need(status_value is not None, "watchdog-reap")
    WATCHDOG_PID = 0
    if life_write in OPEN_FDS:
        need(close_fd(life_write), "supervisor-lifeline-close")
    need(close_all(), "supervisor-internal-close")
    good = os.WIFEXITED(status_value) and os.WEXITSTATUS(status_value) == 0
    close_good = True
    for fd in (2, 1):
        try:
            os.close(fd)
        except BaseException:
            close_good = False
    os._exit(0 if good and close_good else 1)

def watchdog_mode():
    runtime("watchdog", (0, 1, 2, 10, 11))
    track(10)
    track(11)
    need(os.getpid() == os.getsid(0) == os.getpgrp(), "watchdog-session-self")
    preflight = Preflight()
    preflight.verify()
    write_all(11, b"R")
    need(close_fd(11), "watchdog-ready-close")
    os.set_blocking(10, False)
    poller = select.poll()
    poller.register(10, select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL)
    deadline = time.monotonic_ns() + ACK_DEADLINE_NS
    start = None
    while start is None:
        remaining = deadline - time.monotonic_ns()
        need(remaining > 0, "start-timeout")
        for fd, mask in poller.poll(min(POLL_SLICE_MS, max(1, (remaining + 999999) // 1000000))):
            need(fd == 10 and not mask & select.POLLNVAL, "start-poll")
            piece = os.read(10, 1)
            need(piece == b"S", "start-byte")
            start = piece
            break
    state = empty_capture()
    try:
        preflight.verify()
        if not probe_lifeline(10):
            state["supervisor_lost"] = 1
            finalize_watchdog(preflight, state, True, "supervisor-lost-before-spawn")
        out_read, out_write = os.pipe2(os.O_CLOEXEC)
        err_read, err_write = os.pipe2(os.O_CLOEXEC)
        for fd in (out_read, out_write, err_read, err_write):
            track(fd)
        need(
            len({out_read, out_write, err_read, err_write, 0, 1, 2, 10}) == 8,
            "payload-fd-collision",
        )
        actions = (
            (os.POSIX_SPAWN_DUP2, out_write, 1),
            (os.POSIX_SPAWN_DUP2, err_write, 2),
            (os.POSIX_SPAWN_CLOSE, 10),
            (os.POSIX_SPAWN_CLOSE, out_read),
            (os.POSIX_SPAWN_CLOSE, out_write),
            (os.POSIX_SPAWN_CLOSE, err_read),
            (os.POSIX_SPAWN_CLOSE, err_write),
        )
        pid = os.posix_spawn(
            ENV_TOOL,
            preflight.payload_argv,
            {},
            file_actions=actions,
            setsigmask=(),
            setsigdef=SIGNAL_DEFAULTS,
        )
        state["payload_spawned"] = 1
        need(pid > 1 and os.getpgid(pid) == os.getpgrp(), "payload-pgid")
        need(close_fd(out_write) and close_fd(err_write), "payload-writer-close")
        state, safe = capture_payload(pid, out_read, err_read, 10)
        finalize_watchdog(preflight, state, safe, "none")
    except BaseException as error:
        code = error.code if isinstance(error, Stop) else "unexpected"
        finalize_watchdog(preflight, state, state["payload_spawned"] == 0, code)

def require_group_absent(pgid):
    try:
        os.killpg(pgid, 0)
    except OSError as error:
        need(error.errno == errno.ESRCH, "recovery-pgid-check")
        return
    stop("recovery-pgid-live")

def recovery_mode():
    runtime("recovery-binder", (0, 1, 2))
    text_pgid = sys.argv[2]
    need(text_pgid.isascii() and text_pgid.isdecimal(), "recovery-pgid-grammar")
    pgid = int(text_pgid)
    need(pgid > 1 and str(pgid) == text_pgid, "recovery-pgid-canonical")
    need(sys.argv[3] == "consumed", "recovery-consumed-token")
    require_group_absent(pgid)
    preflight = Preflight()
    preflight.verify()
    require_group_absent(pgid)
    binder, binder_status, phase = binder_core(preflight.source, True, False)
    need(phase == "unknown-mismatch", "recovery-phase")
    state = empty_capture()
    state["supervisor_lost"] = 1
    state["capture_error"] = "watchdog-report-lost"
    state["recovery_pgid"] = str(pgid)
    closed = preflight.close()
    closed = close_all() and closed
    for fd in (0, 2):
        try:
            os.close(fd)
        except BaseException:
            closed = False
    value = result_line(
        "recovery-binder",
        state,
        binder,
        binder_status,
        "unknown-mismatch",
        "PERMANENT_FAILURE",
        int(not closed),
    )
    emit_and_exit(value, 0 if closed else 1)

try:
    need(len(sys.argv) >= 2, "mode-argv")
    if len(sys.argv) == 2 and sys.argv[1] == "supervisor":
        supervisor_mode()
    elif len(sys.argv) == 2 and sys.argv[1] == "watchdog":
        watchdog_mode()
    elif len(sys.argv) == 4 and sys.argv[1] == "recovery-binder":
        recovery_mode()
    else:
        stop("mode")
except BaseException:
    close_all()
    if WATCHDOG_PID > 1:
        status_value = wait_deadline(
            WATCHDOG_PID,
            time.monotonic_ns() + KILL_REAP_GRACE_NS,
        )
        if status_value is None:
            try:
                os.killpg(WATCHDOG_PID, signal.SIGKILL)
            except OSError as error:
                if error.errno != errno.ESRCH:
                    pass
            try:
                wait_deadline(
                    WATCHDOG_PID,
                    time.monotonic_ns() + KILL_REAP_GRACE_NS,
                )
            except BaseException:
                pass
    os._exit(1)
BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_PROGRAM_END

## 4. Canonical transports

The ready, durable-ack, and start tokens are respectively the exact
one-byte strings R, A, and S.  The ready pipe must then reach EOF.  The
start pipe remains open as the supervisor lifeline until watchdog reap.
Any other byte, extra byte, premature EOF, timeout, poll error, close
error, or status inconsistency is failure.

BEGIN has exactly this ASCII grammar and one terminal LF:

    BEGIN E001_SUPERVISOR_BINDER_RECOVERY version=1 supervisor_pid=D watchdog_pid=D session_pgid=D program_bytes=D program_LF=D program_sha256=H payload_sha256=6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0 launcher_sha256=72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd inner_sha256=e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f attempt_consumed=0

Each D is canonical decimal, PID values are positive with no leading zero,
H is the exact lowercase 64-hex normalized-program hash frozen by this
control's static extraction, and watchdog_pid must byte-equal
session_pgid.  No watchdog output is possible before S, so BEGIN cannot
interleave with the later watchdog result.

The watchdog emits exactly one RESULT line in the literal field order used
by result_line.  The fixed success instance is obtained by substituting
payload_spawned=1, payload_success=1, supervisor_lost=0, timeout=0, both
overflow fields zero, capture_error=none, wait_raw=0, wait_kind=exit,
exit_code=0, signal=none, core=0, both EOF fields one, the exact 308-byte
PASS stream and its hex, empty stderr, binder_status=not-run,
durability_phase=not-applicable, zero binder bytes, no close error, and
disposition=SUCCESS.  That RESULT is distinct from the raw child PASS.
Every other complete result has disposition=PERMANENT_FAILURE.

The binder is canonical ASCII/LF.  Inventory names are recovered only by
a capped os.scandir iteration on the held directory fd followed by
os.fsencode surrogateescape roundtrip, raw-byte sorting, and
length-colon-hex-LF framing.  A valid inventory reaches iterator EOF and
has at most four entries.  An over-cap inventory reports complete=0,
framing_kind=capped-prefix, and forces unknown-mismatch without claiming
that all names were observed.  Unknown names occur only in inventory
frame_hex and are never
formed into a pathname or opened.  Only the four fixed literal candidates
are lstat'ed and opened with O_PATH/O_NOFOLLOW, with regular candidates
separately opened O_RDONLY/O_NOFOLLOW.

Each present candidate records type, dev, ino, full st_mode, nlink, uid,
gid, rdev, byte count, LF count, SHA-256, content state, and exact-expected
predicate.  Each absent candidate records exact ENOENT and every field as
none.  All duplicate candidate dev/ino pairs and all source-equal pairs
are explicit.  A regular candidate over 1048576 bytes is bound with its
stat byte count and content_state=unavailable-size-cap, maps to
unknown-mismatch, and makes success impossible.

Every source, control, tool, directory ancestor, evidence directory, and
regular candidate read is opened with O_NOATIME in addition to the
applicable O_NOFOLLOW and O_CLOEXEC flags.  Root with CAP_FOWNER is a
frozen premise.  There is no fallback without O_NOATIME; failure to obtain
such an fd stops before the corresponding read.

The payload-created E001.status is a synthetic receipt and is never
authoritative for process success.  Only watchdog waitpid plus complete
independent raw-stream EOF capture is process authority.  Recovery-binder
mode always emits durability_phase=unknown-mismatch and
PERMANENT_FAILURE, irrespective of the physical four-name state.  Only an
in-process watchdog binder with the exact complete child PASS may use
all-four-durable-post-emission-failure.

The watchdog runs a held-directory repeat inventory, a complete fresh
terminal no-follow rewalk, a second independent candidate snapshot, and
exact snapshot equality before constructing the binder.  It binds only
after the direct payload is reaped and both stream pipes reached EOF.  If
SIGKILL does not reap within five seconds or a stream does not reach EOF
within one second after reap, it emits no report and exits nonzero; the
external actor must use recovery-binder after containment is proven gone.

On stream overflow, the watchdog continues draining through EOF while
retaining total bytes, total LF, and SHA-256 over the complete stream.
Only the bounded stored prefix is hex encoded; the result explicitly says
hex_kind=prefix.  Non-overflow streams say hex_kind=full.

All internal descriptors are closed before the direct fd1 write-all.
Safe write loops preserve partial writes and retry only InterruptedError.
The watchdog then closes fd1 and calls os._exit.  Any pre-emission internal
close error converts success to failure and exits nonzero.  Any partial
emission or fd1 close error also exits nonzero.  Therefore the external
actor must require the complete line, terminal LF, fd1 EOF, empty external
stderr, watchdog exit zero, and supervisor exit zero.  A frame cannot
attest to its own future fd1 close or exit.

## 5. External durable executor and recovery trust boundary

A later separately frozen non-PTY executor is required.  It must:

1. launch the supervisor under exact E0280, exact ten-key environment,
   exact workspace, separate binary stdin/stdout/stderr pipes, and a
   durable overall deadline;
2. drain stdout and stderr concurrently without newline normalization,
   truncation, merging, shell substitution, or command capture;
3. accept exactly one BEGIN, validate canonical PIDs, and durably append a
   pending-attempt event containing the consumed bit zero and the known
   watchdog session PGID before writing the sole A byte;
4. after the sole A write, retain the external stdin channel without
   writing another byte; the supervisor closes its own fd0 while the
   watchdog-held fd0 remains live, and the actor remembers that S may have
   consumed the attempt;
5. accept exactly BEGIN plus one canonical watchdog RESULT, stdout EOF,
   empty stderr, and consistent direct-supervisor status;
6. treat any missing, partial, malformed, duplicated, overflowed, timed
   out, or status-inconsistent report as loss;
7. on loss after possible S, SIGKILL the direct supervisor PID and the
   negative watchdog session PGID, wait until the supervisor is reaped and
   the entire frozen watchdog process group is absent, and only then
   invoke this exact program once in recovery-binder mode with the
   canonical watchdog PGID and literal consumed token into a new, separate
   raw capture; recovery-binder itself requires killpg of that PGID with
   signal zero to return ESRCH both before preflight and immediately before
   its first build-path open;
8. append the complete physical result while the single-writer interval
   remains held, then permanently consume the attempt.

The frozen chain contains no process-group escape and no descendant other
than the direct exec chain.  If later review cannot prove that property
for every frozen byte, session-PGID kill is insufficient and activation
must stop.  CPython/libc posix_spawn correctness, pathname-exec immutability
between final tool rewalk and exec, and timely SIGKILL/reap outside
uninterruptible kernel sleep remain explicit host trust assumptions.

## 6. Failure preservation and later gates

Empty evidence is pre-create.  Exact stdout only is
stdout-present-last-durability-unproven.  Exact stdout plus stderr is
stdout-durable-and-stderr-present-last-durability-unproven.  Exact first
three is stdout-stderr-durable-and-copy-present-last-durability-unproven.
Exact all four without the in-process exact PASS proof is
first-three-durable-and-status-present-last-durability-unproven.  Exact all
four with that proof followed by a later failure is
all-four-durable-post-emission-failure.  Every corruption, alias,
unexpected or incomplete inventory, non-prefix presence pattern,
unavailable content,
recovery invocation, or unstable rewalk is unknown-mismatch.

No partial state is deleted, renamed, repaired, completed, backfilled, or
retried.  A canonical failure report is an observation binder, not
authority to resume.  A000 four-name and eight-frame rules, E010 and later
receipt rules, root and stage ordering, validator predicates, and every
downstream control remain unchanged and closed.

Before any real execution, two separated static reviewers must reproduce
the exact control and program transports and return all-zero findings.
Later isolated no-build microtests must use a separately derived and
separately reviewed synthetic non-build test double
and cover R/A/S ordering, durable pre-S barrier, FD collisions, signal
mask/defaults, dual-stream deadlock and terminal LF, exit, signal, timeout,
overflow, supervisor loss before and after spawn, watchdog/report loss,
session-PGID kill, truncation, close-after-report failure, and
recovery-binder dispatch.  Those microtests may not use this payload,
source execution, a validator import, or any build path.

This author stop creates no E001, recovery-binder, E010, A000, root, stage,
PDF, release, or Paper28 execution authority.

BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_AUTHOR_STOP
