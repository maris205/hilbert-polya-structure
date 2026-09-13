# E001 posix-spawn supervisor and failure binder V4

## 1. Authority, precedence, and inertness

This append-only V4 control is the sole notes artifact authorized by the exact
E0321 ledger terminal quoted below.  Its authoring input is the exact E0321
physical ledger prefix:

- bytes 1736809;
- LF 19884;
- SHA-256
  00096a2f1b8ff42fffa463ed6709e71cd35adf9c3dace25859745ea8c772316f;
- terminal
  BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V3_STATIC_REVIEW_FAILURE_RECORDED_AND_V4_CONTROL_AUTHORIZED.

The failed V1, V2 and V3 controls and every review remain byte-immutable.
This file supersedes only their failed deadline, capture, evidence-bracket and
recovery-schema design.  The frozen
E001_FIRST_COPY_RECOVERY.md payload is copied without changing one byte.
Every earlier failure, durability phase, no-retry rule, build boundary and
downstream gate remains normative.

This file grants no execution or microtest authority.  Its program is inert
text.  Authoring and review may not import, parse, compile, or execute the
program or payload and may not name, list, open, or probe a build path.

The program has supervisor, watchdog, and recovery-binder modes.  It has no
fork, subprocess, preexec_fn, ctypes, prctl, eval, compile, dynamic import,
temporary file, PTY, tee, cleanup mutation, repair, backfill, retry, or
second-payload path.  Children use only os.posix_spawn.  Safe byte-write
loops may repeat only an interrupted write syscall; that is not an attempt
retry.

## 2. V4 trust boundary and lifecycle

The executable marker bytes bind themselves through CODE_BYTES.  They do
not claim to self-certify this whole Markdown file.  A separately frozen
later actor supplies canonical whole-V4 and appendable-ledger-prefix identity
tuples after V4 author stop and ledger binding.  Every mode checks those
tuples, the marker transport, and the E0321 minimum ledger anchor.  The later
actor independently checks the whole control and complete current ledger.
This is the noncircular whole-control trust boundary.

The actor supplies five separate live binary pipes: supervisor fd0 is ACK
input, fd1 is stdout, fd2 is stderr, fd3 is payload stdin, and fd4 is launch
release.  It posix-spawns the supervisor with setsid=True, binds the returned
direct PID as SID and PGID, durably records that containment identity, then
writes exact L and closes fd4.  The supervisor cannot spawn a descendant
before L plus EOF.  The actor later durably appends
and rebinds a pending event before writing exact A and closing ACK.  It never
writes payload stdin and retains that pipe writer until containment is
complete.  The watchdog maps fd3 to its fd0.  Exact A followed by EOF is
required; extra data, live ACK after A, or premature EOF fails.

There is no normal supervisor watchdog-completion deadline and no grace that
can return to success.  Ready is bounded by 30 seconds, ACK by 300 seconds,
the payload wait by 30 seconds, kill/reap by 5 seconds, and post-reap stream
EOF by 1 second.  ready_deadline is frozen immediately before watchdog
posix_spawn.  ack_deadline is frozen immediately before BEGIN construction and
guards construction, write and ACK acceptance.  A preallocated capture state
receives one payload_deadline frozen immediately before payload posix_spawn;
the same absolute value governs return, topology, writer closes, wait, poll,
stream reads and lifeline reads.  Each observation checks strictly before and
immediately after its syscall, and equality is late.  The later actor owns a
sticky 420-second overall deadline and a separate 60-second recovery deadline.
Once any deadline fires, success is impossible.

The direct-report order is actor-known P equals SID equals PGID, durable
launch binding, L plus EOF, R plus EOF, BEGIN, durable pending ledger event,
A plus EOF, S, payload wait and stream EOF, terminal verification or binder,
watchdog RESULT write and fd1 close, watchdog exit, supervisor waitpid,
supervisor fd closes and exit, actor EOF/status acceptance, process-group
absence, and final ledger result append.  A visible RESULT is provisional
until stdout EOF, empty stderr EOF, watchdog status as attested by supervisor
zero exit, and supervisor zero exit all hold.

The watchdog and payload inherit the supervisor's actor-known session and
process group and never create another.  All modes normalize and verify every catchable signal disposition and the
empty mask before governed work.  They scan the complete frozen descriptor
domain 0 through 1048575 twice.  The watchdog receives the deterministic
ten-key environment, not an empty mapping.  Activation remains conditional
on a separately frozen no-build host probe proving that 1048576 is the
maximum possible live-fd boundary and reproducing the exact signal and
CPython/libc environment behavior.

## 3. Exact literal V4 program

The normalized program is the byte substring after the BEGIN marker LF and
before the LF immediately preceding the END marker.  The delimiter LF is not
passed to Python.  At author stop its raw and normalized identities are:

- raw bytes 140375, LF 3849, SHA-256
  c80f02abe599dbd8e7c3f8394c8b79eeb55281ba9543ceb98b39ee01fb84e666;
- normalized bytes 140374, LF 3848, physical lines 3849, final byte 41,
  SHA-256 8a16dd06b952a4d226fac87c853b50076f78adc0e0f22287aaeb2604178f7357;
- normalized single-quote, dollar, and backtick census 0/0/0.

BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V4_PROGRAM_BEGIN
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
SELF_NAME = b"E001_SUPERVISOR_BINDER_RECOVERY_V4.md"
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
EVIDENCE_PARENT_COMPONENTS = WORK_COMPONENTS + (
    b"papers",
    b"27-positive-newton-translation-reciprocity",
    b"build",
)
EVIDENCE_NAME = b"recovery-6103a9df0c3d-evidence"
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
E0321_BYTES = 1736809
E0321_LF = 19884
E0321_SHA256 = "00096a2f1b8ff42fffa463ed6709e71cd35adf9c3dace25859745ea8c772316f"
E0321_TERMINAL = (
    b"BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V3_STATIC_REVIEW_"
    b"FAILURE_RECORDED_AND_V4_CONTROL_AUTHORIZED\n"
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
COMMON_NOTE_SPECS = (
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
SOURCE_STRICT_SPEC = (
    SOURCE_NAME,
    SOURCE_BYTES,
    SOURCE_LF,
    SOURCE_SHA256,
    SOURCE_TERMINAL,
    SOURCE_DEV,
    SOURCE_INO,
)
NOATIME = os.O_NOATIME
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC | NOATIME
READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | NOATIME
PATH_FLAGS = os.O_PATH | os.O_NOFOLLOW | os.O_CLOEXEC | NOATIME
CHUNK = 65536
HARD_NOFILE = 1048576
STDOUT_CAP = 4096
STDERR_CAP = 65536
CANDIDATE_CAP = 1048576
SOURCE_OBSERVE_CAP = 1048576
INVENTORY_ITEMS_CAP = 64
INVENTORY_RAW_CAP = 16384
UNKNOWN_RECORD_CAP = 64
BINDER_WORST = 516096
BINDER_CAP = 524288
RESULT_WORST = 1263616
RESULT_CAP = 1310720
BEGIN_CAP = 4096
LAUNCH_RELEASE_DEADLINE_NS = 30000000000
READY_DEADLINE_NS = 30000000000
ACK_DEADLINE_NS = 300000000000
PAYLOAD_DEADLINE_NS = 30000000000
KILL_REAP_GRACE_NS = 5000000000
PIPE_EOF_GRACE_NS = 1000000000
ACTOR_OVERALL_DEADLINE_NS = 420000000000
ACTOR_RECOVERY_DEADLINE_NS = 60000000000
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
CLOSE_FAILED = 0
CLOSE_FAILURE_SITES = []
CLOSE_FAILURE_SITES_TRUNCATED = 0
CLOSE_FAILURE_SITES_CAP = 32
INVENTORY_REASON_ORDER = (
    "evidence-unavailable",
    "open-error",
    "identity-open",
    "name-invalid",
    "item-cap",
    "raw-cap",
    "scan-error",
    "duplicate",
    "frame-cap",
    "identity-final",
    "iterator-close",
    "fd-close",
    "unexpected",
)
WATCHDOG_PID = 0
CLOSE_SITE_TOKENS = (
    "ack-close",
    "candidate-close",
    "chain-close",
    "cleanup-close",
    "control-input-close",
    "evidence-close",
    "fresh-close",
    "inventory-fd-close",
    "inventory-iterator-close",
    "launch-close",
    "life-close",
    "payload-err-close",
    "payload-out-close",
    "payload-writer-close",
    "preflight-close",
    "ready-close",
    "record-close",
    "self-close",
    "stderr-close",
    "stdin-close",
    "source-close",
    "source-initial-close",
    "source-terminal-close",
    "stdout-close",
    "tool-close",
    "unknown-close-site",
)

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

def stable_file_key(value):
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_nlink,
        value.st_uid,
        value.st_gid,
        value.st_rdev,
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

def note_close_failure(site):
    global CLOSE_FAILED
    global CLOSE_FAILURE_SITES_TRUNCATED
    CLOSE_FAILED = 1
    token = site if site in CLOSE_SITE_TOKENS else "unknown-close-site"
    if len(CLOSE_FAILURE_SITES) < CLOSE_FAILURE_SITES_CAP:
        CLOSE_FAILURE_SITES.append(token)
    else:
        CLOSE_FAILURE_SITES_TRUNCATED = 1

def track(fd):
    need(fd >= 0 and fd not in OPEN_FDS, "fd-track")
    OPEN_FDS.add(fd)
    return fd

def close_fd(fd, site):
    if fd not in OPEN_FDS:
        return True
    OPEN_FDS.remove(fd)
    try:
        os.close(fd)
        return True
    except BaseException:
        note_close_failure(site)
        return False

def close_owned(fd, site):
    try:
        os.close(fd)
        return True
    except BaseException:
        note_close_failure(site)
        return False

def close_all():
    for fd in sorted(tuple(OPEN_FDS), reverse=True):
        close_fd(fd, "cleanup-close")
    return CLOSE_FAILED == 0

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

def canonical_decimal(text, minimum, maximum, code):
    need(text.isascii() and text.isdecimal(), code)
    value = int(text)
    need(minimum <= value <= maximum and str(value) == text, code)
    return value

def canonical_hex(text, size, code):
    need(len(text) == size and text == text.lower(), code)
    need(all(item in "0123456789abcdef" for item in text), code)
    return text

def signal_defaults():
    values = []
    for value in signal.valid_signals():
        number = int(value)
        if number not in (int(signal.SIGKILL), int(signal.SIGSTOP)):
            values.append(number)
    return tuple(sorted(values))

SIGNAL_DEFAULTS = signal_defaults()

def normalize_signals():
    signal.pthread_sigmask(signal.SIG_SETMASK, set())
    for number in SIGNAL_DEFAULTS:
        signal.signal(number, signal.SIG_DFL)
    blocked = signal.pthread_sigmask(signal.SIG_BLOCK, set())
    need(len(blocked) == 0, "signal-mask")
    for number in SIGNAL_DEFAULTS:
        need(signal.getsignal(number) == signal.SIG_DFL, "signal-disposition")

def fd_census():
    found = []
    flags = {}
    for fd in range(HARD_NOFILE):
        try:
            value = fcntl.fcntl(fd, fcntl.F_GETFD)
        except OSError as error:
            if error.errno == errno.EBADF:
                continue
            stop("fd-census")
        found.append(fd)
        flags[fd] = value
    return tuple(found), flags

class Binding:
    def __init__(self, values):
        need(len(values) == 11, "binding-count")
        self.text = tuple(values)
        self.self_dev = canonical_decimal(values[0], 1, 9223372036854775807, "binding-self-dev")
        self.self_ino = canonical_decimal(values[1], 1, 9223372036854775807, "binding-self-ino")
        self.self_bytes = canonical_decimal(values[2], 1, 2097152, "binding-self-bytes")
        self.self_lf = canonical_decimal(values[3], 1, 100000, "binding-self-lf")
        self.self_sha = canonical_hex(values[4], 64, "binding-self-sha")
        self.ledger_dev = canonical_decimal(values[5], 1, 9223372036854775807, "binding-ledger-dev")
        self.ledger_ino = canonical_decimal(values[6], 1, 9223372036854775807, "binding-ledger-ino")
        self.ledger_bytes = canonical_decimal(values[7], E0321_BYTES, 16777216, "binding-ledger-bytes")
        self.ledger_lf = canonical_decimal(values[8], E0321_LF, 200000, "binding-ledger-lf")
        self.ledger_sha = canonical_hex(values[9], 64, "binding-ledger-sha")
        terminal_text = values[10]
        need(len(terminal_text) >= 2 and len(terminal_text) <= 1024, "binding-ledger-terminal")
        need(len(terminal_text) % 2 == 0 and terminal_text == terminal_text.lower(), "binding-ledger-terminal")
        need(all(item in "0123456789abcdef" for item in terminal_text), "binding-ledger-terminal")
        self.ledger_terminal = bytes.fromhex(terminal_text)
        need(self.ledger_terminal.endswith(b"\n"), "binding-ledger-terminal")
        need(b"\x00" not in self.ledger_terminal, "binding-ledger-terminal")

def runtime(mode, expected_fds, binding):
    if mode == "supervisor":
        need(len(sys.argv) == 13 and sys.argv[0] == "-c" and sys.argv[1] == mode, "argv")
        flags = ["-S", "-B", "-P"]
        expected_environment = EXPECTED_ENV
        isolated = 0
        ignored = 0
        randomized = 0
    elif mode == "watchdog":
        need(len(sys.argv) == 14 and sys.argv[0] == "-c" and sys.argv[1] == mode, "argv")
        flags = ["-I", "-S", "-B", "-P", "-X", "utf8"]
        expected_environment = EXPECTED_ENV
        isolated = 1
        ignored = 1
        randomized = 1
    else:
        need(len(sys.argv) == 15 and sys.argv[0] == "-c" and sys.argv[1] == mode, "argv")
        flags = ["-S", "-B", "-P"]
        expected_environment = EXPECTED_ENV
        isolated = 0
        ignored = 0
        randomized = 0
    expected_orig = [PYTHON.decode("ascii")] + flags + ["-c", CODE_TEXT, mode] + list(sys.argv[2:])
    need(sys.orig_argv == expected_orig, "orig-argv")
    need(tuple(sys.argv[2:13]) == binding.text, "binding-argv")
    need(sys.implementation.name == "cpython", "implementation")
    need(sys.version_info[:2] == (3, 12), "version")
    need(sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1, "flags-basic")
    need(sys.flags.safe_path and sys.flags.utf8_mode == 1, "flags-safe")
    need(sys.flags.isolated == isolated and sys.flags.ignore_environment == ignored, "flags-env")
    need(sys.flags.hash_randomization == randomized, "flags-hash")
    need(dict(os.environb) == expected_environment, "environment")
    need(os.getcwdb() == WORK, "cwd")
    need(os.geteuid() == 0 and os.getegid() == 0, "identity")
    old_mask = os.umask(0o077)
    os.umask(old_mask)
    need(old_mask == 0o077, "umask")
    need(resource.getrlimit(resource.RLIMIT_NOFILE) == (4096, HARD_NOFILE), "nofile")
    normalize_signals()
    first, first_flags = fd_census()
    second, second_flags = fd_census()
    need(first == expected_fds and second == expected_fds, "fd-set")
    need(first_flags == second_flags, "fd-flags-drift")
    for fd in expected_fds:
        need(first_flags[fd] == 0, "fd-cloexec")
    keys = []
    for fd in expected_fds:
        value = os.fstat(fd)
        need(stat.S_ISFIFO(value.st_mode), "entry-not-pipe")
        keys.append((value.st_dev, value.st_ino))
    need(len(keys) == len(set(keys)), "entry-pipe-alias")
    need(CODE_BYTES.decode("ascii", "strict").encode("ascii") == CODE_BYTES, "code-ascii")
    need(CODE_BYTES.count(QUOTE) == 0 and CODE_BYTES.count(DOLLAR) == 0 and CODE_BYTES.count(TICK) == 0, "code-census")

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
        fresh.close()
        need(good and CLOSE_FAILED == 0, "chain-drift")

    def close(self):
        for fd in reversed(self.fds):
            close_fd(fd, "chain-close")
        self.fds = []
        return CLOSE_FAILED == 0

class Record:
    def __init__(self, chain, name, fd, data):
        self.chain = chain
        self.name = name
        self.fd = fd
        self.key = node_key(os.fstat(fd))
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
            need(node_key(os.fstat(fresh)) == self.key, "fresh-file-final-fstat")
            after = os.stat(self.name, dir_fd=self.chain.leaf(), follow_symlinks=False)
            need(node_key(after) == self.key, "fresh-file-final-path")
        finally:
            close_fd(fresh, "fresh-close")
        need(CLOSE_FAILED == 0, "fresh-file-close")

    def close(self):
        close_fd(self.fd, "record-close")
        return CLOSE_FAILED == 0

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
    need(node_key(os.fstat(fd)) == node_key(before), "fixed-open-race")
    data = pread_complete(fd, size)
    need(data.count(b"\n") == lf and sha(data) == digest, "fixed-content")
    need(data.endswith(terminal), "fixed-terminal")
    return Record(chain, name, fd, data)

def open_actor_self(chain, binding):
    before = os.stat(SELF_NAME, dir_fd=chain.leaf(), follow_symlinks=False)
    need(stat.S_ISREG(before.st_mode), "self-type")
    need(stat.S_IMODE(before.st_mode) == 0o644, "self-mode")
    need(before.st_nlink == 1 and before.st_uid == 0 and before.st_gid == 0, "self-owner")
    need(before.st_dev == binding.self_dev and before.st_ino == binding.self_ino, "self-node")
    need(before.st_size == binding.self_bytes, "self-size")
    fd = track(os.open(SELF_NAME, READ_FLAGS, dir_fd=chain.leaf()))
    need(node_key(os.fstat(fd)) == node_key(before), "self-open-race")
    data = pread_complete(fd, binding.self_bytes)
    need(data.count(b"\n") == binding.self_lf and sha(data) == binding.self_sha, "self-content")
    terminal = (
        b"BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_"
        b"V4_AUTHOR_STOP\n"
    )
    need(data.endswith(terminal), "self-terminal")
    return Record(chain, SELF_NAME, fd, data)

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
    begin = b"BATCH07_P27_RECOVERY_E001_FIRST_" + b"COPY_HARNESS_BEGIN\n"
    end = b"BATCH07_P27_RECOVERY_E001_FIRST_" + b"COPY_HARNESS_END\n"
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
        b"BINDER_V4_PROGRAM_BEGIN\n"
    )
    end = (
        b"BATCH07_P27_RECOVERY_E001_SUPERVISOR_"
        b"BINDER_V4_PROGRAM_END\n"
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
    prefix = b"liveness_corrected_launcher_script_exact_" + b"lines:\n" + TICK * 3 + b"text\n"
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

class StatusPrefixRecord:
    def __init__(self, binding):
        self.binding = binding
        self.chain = Chain(WORK_COMPONENTS)
        before = os.stat(STATUS_NAME, dir_fd=self.chain.leaf(), follow_symlinks=False)
        self.check_metadata(before)
        self.fd = track(os.open(STATUS_NAME, READ_FLAGS, dir_fd=self.chain.leaf()))
        need(stable_file_key(os.fstat(self.fd)) == stable_file_key(before), "ledger-open-race")
        self.data = pread_exact(self.fd, binding.ledger_bytes)
        self.check_data(self.data)
        self.launcher = extract_launcher(self.data[:E0321_BYTES])

    def check_metadata(self, value):
        need(stat.S_ISREG(value.st_mode), "ledger-type")
        need(stat.S_IMODE(value.st_mode) == 0o644, "ledger-mode")
        need(value.st_nlink == 1 and value.st_uid == 0 and value.st_gid == 0, "ledger-owner")
        need(value.st_dev == self.binding.ledger_dev and value.st_ino == self.binding.ledger_ino, "ledger-node")
        need(value.st_size >= self.binding.ledger_bytes, "ledger-size")

    def check_data(self, data):
        need(len(data) == self.binding.ledger_bytes, "ledger-prefix-size")
        need(data.count(b"\n") == self.binding.ledger_lf, "ledger-prefix-lf")
        need(sha(data) == self.binding.ledger_sha, "ledger-prefix-sha")
        need(data.endswith(self.binding.ledger_terminal), "ledger-prefix-terminal")
        anchor = data[:E0321_BYTES]
        need(
            anchor.count(b"\n") == E0321_LF
            and sha(anchor) == E0321_SHA256
            and anchor.endswith(E0321_TERMINAL),
            "ledger-E0321-anchor",
        )

    def verify(self):
        self.chain.rewalk()
        held = os.fstat(self.fd)
        self.check_metadata(held)
        self.check_data(pread_exact(self.fd, self.binding.ledger_bytes))
        before = os.stat(STATUS_NAME, dir_fd=self.chain.leaf(), follow_symlinks=False)
        self.check_metadata(before)
        need(stable_file_key(before) == stable_file_key(held), "ledger-path-drift")
        fresh = track(os.open(STATUS_NAME, READ_FLAGS, dir_fd=self.chain.leaf()))
        try:
            opened = os.fstat(fresh)
            self.check_metadata(opened)
            need(stable_file_key(opened) == stable_file_key(held), "ledger-fresh-drift")
            self.check_data(pread_exact(fresh, self.binding.ledger_bytes))
            final_fd = os.fstat(fresh)
            final_path = os.stat(STATUS_NAME, dir_fd=self.chain.leaf(), follow_symlinks=False)
            self.check_metadata(final_fd)
            self.check_metadata(final_path)
            need(stable_file_key(final_fd) == stable_file_key(held), "ledger-final-fstat")
            need(stable_file_key(final_path) == stable_file_key(held), "ledger-final-path")
        finally:
            close_fd(fresh, "fresh-close")
        need(CLOSE_FAILED == 0, "ledger-fresh-close")

    def close(self):
        close_fd(self.fd, "record-close")
        self.chain.close()
        return CLOSE_FAILED == 0

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
        need(node_key(os.stat(self.name, dir_fd=self.chain.leaf(), follow_symlinks=False)) == self.key, "tool-link-race")

class ControlInputs:
    def __init__(self, binding):
        self.binding = binding
        self.status = StatusPrefixRecord(binding)
        self.notes = Chain(NOTES_COMPONENTS)
        self.records = [open_fixed(self.notes, spec) for spec in COMMON_NOTE_SPECS]
        self.self_record = open_actor_self(self.notes, binding)
        extract_self(self.self_record.data)
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

    def verify(self):
        self.status.verify()
        self.notes.rewalk()
        for record in self.records:
            record.verify()
        self.self_record.verify()
        extract_self(self.self_record.data)
        self.usr_bin.rewalk()
        self.env_record.verify()
        self.bash_record.verify()
        self.python_bin.rewalk()
        self.python_link.verify()
        self.python_record.verify()
        self.status.verify()

    def verify_complete(self):
        good = True
        actions = [
            self.status.verify,
            self.notes.rewalk,
        ]
        actions.extend(record.verify for record in self.records)
        actions.extend(
            [
                self.self_record.verify,
                self.usr_bin.rewalk,
                self.env_record.verify,
                self.bash_record.verify,
                self.python_bin.rewalk,
                self.python_link.verify,
                self.python_record.verify,
                self.status.verify,
            ]
        )
        for action in actions:
            try:
                action()
            except BaseException:
                good = False
        try:
            extract_self(self.self_record.data)
        except BaseException:
            good = False
        return good and not CLOSE_FAILED

    def close(self):
        for record in self.records:
            record.close()
        self.self_record.close()
        self.env_record.close()
        self.bash_record.close()
        self.python_record.close()
        self.notes.close()
        self.usr_bin.close()
        self.python_bin.close()
        self.status.close()
        return CLOSE_FAILED == 0

LAUNCH_TOKEN = object()

class StrictPreflight:
    def __init__(self, binding):
        self.control = ControlInputs(binding)
        self.source = open_fixed(self.control.notes, SOURCE_STRICT_SPEC)
        self.payload = extract_payload(self.control.records[0].data)
        self.inner = build_inner(self.payload)
        self.payload_argv = (
            ENV_TOOL,
            b"-i",
            BASH_TOOL,
            b"--noprofile",
            b"--norc",
            b"-c",
            self.control.status.launcher,
            b"batch07-p27-successor-liveness-fd-scrub-launcher",
            self.inner,
        )
        need(len(self.payload_argv) == 9, "payload-argv")
        self.launch_token = LAUNCH_TOKEN

    def verify(self):
        self.control.verify()
        self.source.verify()
        need(extract_payload(self.control.records[0].data) == self.payload, "payload-drift")
        need(build_inner(self.payload) == self.inner, "inner-drift")

    def close(self):
        self.source.close()
        self.control.close()
        return CLOSE_FAILED == 0

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

def empty_observation(name):
    return {
        "name": name,
        "state": "unavailable",
        "absence": "none",
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
        "terminal": 0,
        "content": "unavailable",
        "exact": 0,
        "exact_absent": 0,
        "stable": 0,
        "path_fd_opened": 0,
        "directory_fd_opened": 0,
        "path_finalized_after_bracket": 0,
        "error": "none",
        "key": None,
        "final_state": "unavailable",
        "final_absence": "none",
        "final_error": "none",
        "final_key": None,
        "final_type": "none",
        "final_dev": "none",
        "final_ino": "none",
        "final_mode": "none",
        "final_nlink": "none",
        "final_uid": "none",
        "final_gid": "none",
        "final_rdev": "none",
        "final_bytes": "none",
        "path_fd": None,
        "dir_fd": None,
        "dir_key": None,
        "fds": [],
    }

def fill_metadata(record, value):
    record["state"] = "present"
    record["type"] = type_name(value.st_mode)
    record["dev"] = str(value.st_dev)
    record["ino"] = str(value.st_ino)
    record["mode"] = format(value.st_mode, "07o")
    record["nlink"] = str(value.st_nlink)
    record["uid"] = str(value.st_uid)
    record["gid"] = str(value.st_gid)
    record["rdev"] = str(value.st_rdev)
    record["key"] = node_key(value)

def finalize_observation_path(record, dir_fd):
    try:
        value = os.stat(record["name"], dir_fd=dir_fd, follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            record["final_state"] = "absent"
            record["final_absence"] = "ENOENT"
        else:
            record["final_state"] = "error"
            record["final_error"] = "final-lstat"
    except BaseException:
        record["final_state"] = "error"
        record["final_error"] = "final-unexpected"
    else:
        record["final_state"] = "present"
        record["final_key"] = node_key(value)
        record["final_type"] = type_name(value.st_mode)
        record["final_dev"] = str(value.st_dev)
        record["final_ino"] = str(value.st_ino)
        record["final_mode"] = format(value.st_mode, "07o")
        record["final_nlink"] = str(value.st_nlink)
        record["final_uid"] = str(value.st_uid)
        record["final_gid"] = str(value.st_gid)
        record["final_rdev"] = str(value.st_rdev)
        record["final_bytes"] = str(value.st_size)
    if record["state"] == "absent" and record["absence"] == "ENOENT":
        record["stable"] = int(
            record["final_state"] == "absent"
            and record["final_absence"] == "ENOENT"
            and record["error"] == "none"
            and record["final_error"] == "none"
        )
    elif record["state"] == "present" and record["key"] is not None:
        record["stable"] = int(
            record["final_state"] == "present"
            and record["final_key"] == record["key"]
            and record["final_error"] == "none"
        )
    else:
        record["stable"] = 0
    record["exact_absent"] = int(
        record["state"] == "absent"
        and record["absence"] == "ENOENT"
        and record["final_state"] == "absent"
        and record["final_absence"] == "ENOENT"
        and record["stable"] == 1
        and record["error"] == "none"
        and record["final_error"] == "none"
    )

def close_observation(record, site="candidate-close"):
    for fd in reversed(record["fds"]):
        close_fd(fd, site)
    record["fds"] = []

def observation_signature(record):
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
        record["terminal"],
        record["content"],
        record["exact"],
        record["exact_absent"],
        record["stable"],
        record["path_fd_opened"],
        record["directory_fd_opened"],
        record["path_finalized_after_bracket"],
        record["error"],
        record["key"],
        record["final_state"],
        record["final_absence"],
        record["final_error"],
        record["final_key"],
        record["final_type"],
        record["final_dev"],
        record["final_ino"],
        record["final_mode"],
        record["final_nlink"],
        record["final_uid"],
        record["final_gid"],
        record["final_rdev"],
        record["final_bytes"],
    )

def observation_line(kind, tag, record):
    return (
        kind
        + " tag="
        + tag
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
        + " terminal="
        + str(record["terminal"])
        + " content_state="
        + record["content"]
        + " stable="
        + str(record["stable"])
        + " exact_expected="
        + str(record["exact"])
        + " exact_absent="
        + str(record["exact_absent"])
        + " path_fd_opened="
        + str(record["path_fd_opened"])
        + " directory_fd_opened="
        + str(record["directory_fd_opened"])
        + " path_finalized_after_bracket="
        + str(record["path_finalized_after_bracket"])
        + " error="
        + record["error"]
        + " final_state="
        + record["final_state"]
        + " final_absence="
        + record["final_absence"]
        + " final_error="
        + record["final_error"]
        + " final_type="
        + record["final_type"]
        + " final_dev="
        + record["final_dev"]
        + " final_ino="
        + record["final_ino"]
        + " final_mode="
        + record["final_mode"]
        + " final_nlink="
        + record["final_nlink"]
        + " final_uid="
        + record["final_uid"]
        + " final_gid="
        + record["final_gid"]
        + " final_rdev="
        + record["final_rdev"]
        + " final_bytes="
        + record["final_bytes"]
        + "\n"
    ).encode("ascii")

def observe_source(notes):
    record = empty_observation(SOURCE_NAME)
    before = None
    data = None
    try:
        before = os.stat(SOURCE_NAME, dir_fd=notes.leaf(), follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            record["state"] = "absent"
            record["absence"] = "ENOENT"
            record["content"] = "absent"
        else:
            record["state"] = "error"
            record["error"] = "source-lstat"
    except BaseException:
        record["state"] = "error"
        record["error"] = "source-lstat-unexpected"
    if before is not None:
        fill_metadata(record, before)
        record["bytes"] = str(before.st_size)
        try:
            path_fd = track(os.open(SOURCE_NAME, PATH_FLAGS, dir_fd=notes.leaf()))
            record["fds"].append(path_fd)
            if node_key(os.fstat(path_fd)) != node_key(before):
                record["error"] = "source-path-race"
        except BaseException:
            record["error"] = "source-path-open"
        if not stat.S_ISREG(before.st_mode):
            record["content"] = "unavailable-nonregular"
        elif before.st_size > SOURCE_OBSERVE_CAP:
            record["content"] = "unavailable-size-cap"
        elif record["error"] == "none":
            try:
                read_fd = track(os.open(SOURCE_NAME, READ_FLAGS, dir_fd=notes.leaf()))
                record["fds"].append(read_fd)
                opened = os.fstat(read_fd)
                if node_key(opened) != node_key(before):
                    record["error"] = "source-read-race"
                else:
                    data = pread_complete(read_fd, before.st_size)
                    record["bytes"] = str(len(data))
                    record["lf"] = str(data.count(b"\n"))
                    record["sha"] = sha(data)
                    record["terminal"] = int(data.endswith(SOURCE_TERMINAL))
                    record["content"] = "complete"
                    if node_key(os.fstat(read_fd)) != node_key(before):
                        record["error"] = "source-read-final"
            except BaseException:
                record["error"] = "source-read"
                record["content"] = "read-error"
    finalize_observation_path(record, notes.leaf())
    record["exact"] = int(
        before is not None
        and data is not None
        and record["stable"] == 1
        and record["error"] == "none"
        and record["final_error"] == "none"
        and stat.S_ISREG(before.st_mode)
        and before.st_dev == SOURCE_DEV
        and before.st_ino == SOURCE_INO
        and stat.S_IMODE(before.st_mode) == 0o644
        and before.st_nlink == 1
        and before.st_uid == 0
        and before.st_gid == 0
        and before.st_rdev == 0
        and len(data) == SOURCE_BYTES
        and data.count(b"\n") == SOURCE_LF
        and sha(data) == SOURCE_SHA256
        and record["terminal"] == 1
    )
    return record

def candidate_expected(name):
    if name == COPY_NAME:
        return 0o500, SOURCE_BYTES, SOURCE_LF, SOURCE_SHA256, None
    if name == STATUS_RECEIPT_NAME:
        return 0o600, 2, 1, STATUS_RECEIPT_SHA256, b"0\n"
    if name in (STDERR_RECEIPT_NAME, STDOUT_RECEIPT_NAME):
        return 0o600, 0, 0, EMPTY_SHA256, b""
    return None

def observe_candidate(dir_fd, evidence_dev, name):
    record = empty_observation(name)
    before = None
    data = None
    try:
        before = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            record["state"] = "absent"
            record["absence"] = "ENOENT"
            record["content"] = "absent"
        else:
            record["state"] = "error"
            record["error"] = "candidate-lstat"
    except BaseException:
        record["state"] = "error"
        record["error"] = "candidate-lstat-unexpected"
    if before is not None:
        fill_metadata(record, before)
        record["bytes"] = str(before.st_size)
        record["content"] = "unavailable-nonregular"
        try:
            path_fd = track(os.open(name, PATH_FLAGS, dir_fd=dir_fd))
            record["fds"].append(path_fd)
            if node_key(os.fstat(path_fd)) != node_key(before):
                record["error"] = "candidate-path-race"
        except BaseException:
            record["error"] = "candidate-path-open"
        if stat.S_ISREG(before.st_mode):
            if before.st_size > CANDIDATE_CAP:
                record["content"] = "unavailable-size-cap"
            elif record["error"] == "none":
                try:
                    read_fd = track(os.open(name, READ_FLAGS, dir_fd=dir_fd))
                    record["fds"].append(read_fd)
                    if node_key(os.fstat(read_fd)) != node_key(before):
                        record["error"] = "candidate-read-race"
                    else:
                        data = pread_complete(read_fd, before.st_size)
                        record["bytes"] = str(len(data))
                        record["lf"] = str(data.count(b"\n"))
                        record["sha"] = sha(data)
                        record["content"] = "complete"
                        if node_key(os.fstat(read_fd)) != node_key(before):
                            record["error"] = "candidate-read-final"
                except BaseException:
                    record["error"] = "candidate-read"
                    record["content"] = "read-error"
    finalize_observation_path(record, dir_fd)
    expected = candidate_expected(name)
    if before is not None and data is not None and expected is not None:
        expected_mode, expected_size, expected_lf, expected_sha, expected_data = expected
        record["exact"] = int(
            record["stable"] == 1
            and record["error"] == "none"
            and record["final_error"] == "none"
            and stat.S_ISREG(before.st_mode)
            and before.st_dev == evidence_dev
            and stat.S_IMODE(before.st_mode) == expected_mode
            and before.st_nlink == 1
            and before.st_uid == 0
            and before.st_gid == 0
            and before.st_rdev == 0
            and len(data) == expected_size
            and data.count(b"\n") == expected_lf
            and sha(data) == expected_sha
            and (expected_data is None or data == expected_data)
        )
    return record

def observation_error(record, value):
    if record["error"] == "none":
        record["error"] = value

def begin_evidence(parent):
    record = empty_observation(EVIDENCE_NAME)
    before = None
    try:
        before = os.stat(EVIDENCE_NAME, dir_fd=parent.leaf(), follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            record["state"] = "absent"
            record["absence"] = "ENOENT"
            record["content"] = "absent"
        else:
            record["state"] = "error"
            observation_error(record, "evidence-lstat")
    except BaseException:
        record["state"] = "error"
        observation_error(record, "evidence-lstat-unexpected")
    if before is not None:
        fill_metadata(record, before)
        record["content"] = "metadata-only"
        try:
            path_fd = track(os.open(EVIDENCE_NAME, PATH_FLAGS, dir_fd=parent.leaf()))
            record["path_fd"] = path_fd
            record["path_fd_opened"] = 1
            record["fds"].append(path_fd)
            if node_key(os.fstat(path_fd)) != node_key(before):
                observation_error(record, "evidence-path-race")
        except BaseException:
            observation_error(record, "evidence-path-open")
        if stat.S_ISDIR(before.st_mode):
            try:
                directory_fd = track(os.open(EVIDENCE_NAME, DIR_FLAGS, dir_fd=parent.leaf()))
                record["dir_fd"] = directory_fd
                record["directory_fd_opened"] = 1
                record["fds"].append(directory_fd)
                opened = os.fstat(directory_fd)
                if node_key(opened) != node_key(before):
                    observation_error(record, "evidence-directory-race")
                else:
                    record["dir_key"] = dir_key(opened)
                    record["content"] = "directory-observed"
            except BaseException:
                observation_error(record, "evidence-directory-open")
        elif not stat.S_ISDIR(before.st_mode):
            record["content"] = "unavailable-nondirectory"
    return record

def finish_evidence(record, parent):
    path_fd = record["path_fd"]
    directory_fd = record["dir_fd"]
    if path_fd is not None:
        try:
            if node_key(os.fstat(path_fd)) != record["key"]:
                observation_error(record, "evidence-path-final")
        except BaseException:
            observation_error(record, "evidence-path-final-error")
    if directory_fd is not None:
        try:
            opened = os.fstat(directory_fd)
            if node_key(opened) != record["key"] or dir_key(opened) != record["dir_key"]:
                observation_error(record, "evidence-directory-final")
        except BaseException:
            observation_error(record, "evidence-directory-final-error")
    try:
        finalize_observation_path(record, parent.leaf())
    except BaseException:
        record["final_state"] = "error"
        record["final_error"] = "evidence-finalizer-unexpected"
        record["stable"] = 0
    finally:
        record["path_finalized_after_bracket"] = 1
    record["exact"] = int(
        record["state"] == "present"
        and record["type"] == "directory"
        and record["path_fd_opened"] == 1
        and record["directory_fd_opened"] == 1
        and record["dir_fd"] is not None
        and record["path_finalized_after_bracket"] == 1
        and record["stable"] == 1
        and record["error"] == "none"
        and record["final_error"] == "none"
        and record["dev"] == str(EVIDENCE_DEV)
        and record["ino"] == str(EVIDENCE_INO)
        and record["mode"] == format(stat.S_IFDIR | 0o700, "07o")
        and record["nlink"] == "2"
        and record["uid"] == "0"
        and record["gid"] == "0"
        and record["rdev"] == "0"
    )
    return record

def close_evidence(record):
    for fd in reversed(record["fds"]):
        close_fd(fd, "evidence-close")
    record["fds"] = []
    record["path_fd"] = None
    record["dir_fd"] = None
    record["dir_key"] = None

def new_inventory(reason=None):
    result = {
        "names": (),
        "frame": b"",
        "complete": 1,
        "reason_bits": {item: 0 for item in INVENTORY_REASON_ORDER},
        "reason_truncated": 0,
        "overflow_bytes": "none",
        "overflow_sha": "none",
    }
    if reason is not None:
        add_inventory_reason(result, reason)
    return result

def add_inventory_reason(result, reason):
    if reason in result["reason_bits"]:
        result["reason_bits"][reason] = 1
    else:
        result["reason_bits"]["unexpected"] = 1
        result["reason_truncated"] = 1
    result["complete"] = 0

def inventory_reason_text(inventory):
    values = [item for item in INVENTORY_REASON_ORDER if inventory["reason_bits"][item]]
    return ",".join(values) if values else "none"

def inventory_fresh(anchor_fd, expected_key):
    result = new_inventory()
    raw = []
    raw_bytes = 0
    scan_fd = None
    iterator = None
    try:
        scan_fd = track(os.open(b".", DIR_FLAGS, dir_fd=anchor_fd))
        if dir_key(os.fstat(scan_fd)) != expected_key:
            add_inventory_reason(result, "identity-open")
        else:
            try:
                iterator = os.scandir(scan_fd)
                for entry in iterator:
                    item = os.fsencode(entry.name)
                    roundtrip = os.fsdecode(item).encode(sys.getfilesystemencoding(), "surrogateescape")
                    if roundtrip != item or item in (b".", b"..") or b"/" in item or b"\x00" in item:
                        add_inventory_reason(result, "name-invalid")
                        result["overflow_bytes"] = str(len(item))
                        result["overflow_sha"] = sha(item)
                        break
                    if len(raw) >= INVENTORY_ITEMS_CAP:
                        add_inventory_reason(result, "item-cap")
                        result["overflow_bytes"] = str(len(item))
                        result["overflow_sha"] = sha(item)
                        break
                    if raw_bytes + len(item) > INVENTORY_RAW_CAP:
                        add_inventory_reason(result, "raw-cap")
                        result["overflow_bytes"] = str(len(item))
                        result["overflow_sha"] = sha(item)
                        break
                    raw.append(item)
                    raw_bytes += len(item)
            except BaseException:
                add_inventory_reason(result, "scan-error")
            raw.sort()
            if len(raw) != len(set(raw)):
                add_inventory_reason(result, "duplicate")
            frame = b"".join(
                str(len(item)).encode("ascii") + b":" + item.hex().encode("ascii") + b"\n"
                for item in raw
            )
            if len(frame) > BINDER_CAP:
                add_inventory_reason(result, "frame-cap")
            result["names"] = tuple(raw)
            result["frame"] = frame
        if dir_key(os.fstat(scan_fd)) != expected_key:
            add_inventory_reason(result, "identity-final")
    except OSError:
        add_inventory_reason(result, "open-error")
    except BaseException:
        add_inventory_reason(result, "unexpected")
    finally:
        if iterator is not None:
            try:
                iterator.close()
            except BaseException:
                note_close_failure("inventory-iterator-close")
                add_inventory_reason(result, "iterator-close")
        if scan_fd is not None:
            if not close_fd(scan_fd, "inventory-fd-close"):
                add_inventory_reason(result, "fd-close")
    result["complete"] = int(
        not result["reason_truncated"]
        and not any(result["reason_bits"].values())
    )
    return result

def unavailable_candidate(name, reason):
    record = empty_observation(name)
    record["error"] = reason
    record["final_error"] = reason
    return record

def unavailable_snapshot(index, reason):
    return {
        "index": index,
        "inventory": new_inventory(reason),
        "records": [unavailable_candidate(name, reason) for name in CANDIDATE_NAMES],
        "unknown_names": (),
        "duplicates": (),
        "aliases": (),
        "anomalies": (),
    }

def take_snapshot(index, evidence_fd, evidence_key, evidence_dev, target):
    target["index"] = index
    target["inventory"] = inventory_fresh(evidence_fd, evidence_key)
    target["unknown_names"] = tuple(
        name for name in target["inventory"]["names"] if name not in CANDIDATE_NAMES
    )
    for candidate_index, name in enumerate(CANDIDATE_NAMES):
        target["records"][candidate_index] = observe_candidate(evidence_fd, evidence_dev, name)
    return target

def close_snapshot(snapshot):
    for record in snapshot["records"]:
        try:
            close_observation(record)
        except BaseException:
            note_close_failure("candidate-close")

def snapshot_signature(snapshot):
    inventory = snapshot["inventory"]
    return (
        inventory["names"],
        inventory["frame"],
        inventory["complete"],
        tuple(inventory["reason_bits"][item] for item in INVENTORY_REASON_ORDER),
        inventory["reason_truncated"],
        inventory["overflow_bytes"],
        inventory["overflow_sha"],
        tuple(observation_signature(record) for record in snapshot["records"]),
        snapshot["unknown_names"],
        snapshot["duplicates"],
        snapshot["aliases"],
        snapshot["anomalies"],
    )

def relation_lists(records, source):
    duplicate_pairs = []
    source_aliases = []
    for left in range(len(records)):
        record = records[left]
        if record["state"] != "present" or record["key"] is None:
            continue
        pair = (record["key"][0], record["key"][1])
        if source["key"] is not None and pair == (source["key"][0], source["key"][1]):
            source_aliases.append(str(left))
        for right in range(left + 1, len(records)):
            other = records[right]
            if other["state"] == "present" and other["key"] is not None:
                other_pair = (other["key"][0], other["key"][1])
                if pair == other_pair:
                    duplicate_pairs.append(str(left) + "-" + str(right))
    return tuple(duplicate_pairs), tuple(source_aliases)

def candidate_is_valid(record):
    return (
        record["exact_absent"] == 1
        or (
            record["state"] == "present"
            and record["type"] == "regular"
            and record["content"] == "complete"
            and record["stable"] == 1
            and record["exact"] == 1
            and record["error"] == "none"
            and record["final_error"] == "none"
        )
    )

def snapshot_anomalies(snapshot):
    values = []
    inventory = snapshot["inventory"]
    for reason in INVENTORY_REASON_ORDER:
        if inventory["reason_bits"][reason]:
            values.append("inventory-" + reason)
    if inventory["reason_truncated"]:
        values.append("inventory-reason-truncated")
    for index, record in enumerate(snapshot["records"]):
        if not candidate_is_valid(record):
            values.append("candidate-" + str(index) + "-" + record["state"] + "-" + record["error"])
        if record["state"] == "present" and record["type"] == "directory":
            values.append("candidate-" + str(index) + "-directory")
        elif record["state"] == "present" and record["type"] != "regular":
            values.append("candidate-" + str(index) + "-nonregular-" + record["type"])
        if record["content"] == "unavailable-size-cap":
            values.append("candidate-" + str(index) + "-size-cap")
    for name in snapshot["unknown_names"]:
        values.append("unknown-" + name.hex())
    for pair in snapshot["duplicates"]:
        values.append("duplicate-" + pair)
    for index in snapshot["aliases"]:
        values.append("source-alias-" + index)
    return tuple(values)

def new_audit_schema(mode):
    return {
        "mode": mode,
        "source_initial": empty_observation(SOURCE_NAME),
        "source_terminal": empty_observation(SOURCE_NAME),
        "evidence_initial": empty_observation(EVIDENCE_NAME),
        "evidence_terminal": empty_observation(EVIDENCE_NAME),
        "snapshots": [
            unavailable_snapshot(1, "evidence-unavailable"),
            unavailable_snapshot(2, "evidence-unavailable"),
            unavailable_snapshot(3, "evidence-unavailable"),
        ],
        "source_equal": 0,
        "evidence_equal": 0,
        "snapshots_equal": 0,
        "inventories_complete": 0,
        "post_inputs_reverified": 0,
        "snapshot_1_attempt_complete": 0,
        "snapshot_2_attempt_complete": 0,
        "snapshot_3_attempt_complete": 0,
        "evidence_initial_path_finalized_after_bracket": 0,
        "evidence_terminal_path_finalized_after_bracket": 0,
        "recovery_first_esrch": "na",
        "recovery_second_esrch": "na",
        "recovery_third_esrch": "na",
        "base_status": "error",
        "proposed_phase": "unknown-mismatch",
        "errors": [],
        "errors_truncated": 0,
        "unknown_union": (),
        "duplicate_union": (),
        "alias_union": (),
        "global_anomalies": (),
        "anomaly_union": (),
    }

def schema_error(meta, value):
    if value not in meta["errors"]:
        if len(meta["errors"]) < 32:
            meta["errors"].append(value)
        else:
            meta["errors_truncated"] = 1
    meta["base_status"] = "error"
    meta["proposed_phase"] = "unknown-mismatch"

class FailureBinderInputs:
    def __init__(self, binding, meta):
        self.meta = meta
        self.control = None
        self.source_initial = empty_observation(SOURCE_NAME)
        self.source_terminal = empty_observation(SOURCE_NAME)
        self.input_construction_complete = 0
        self.constructor_error = "none"
        self.post_inputs_reverified = 0
        self.verify_error = "none"
        try:
            self.control = ControlInputs(binding)
        except BaseException:
            self.constructor_error = "input-construction"
            schema_error(self.meta, self.constructor_error)
        if self.control is not None:
            try:
                self.source_initial = observe_source(self.control.notes)
                self.input_construction_complete = 1
            except BaseException:
                self.constructor_error = "source-initial-observation"
                schema_error(self.meta, self.constructor_error)
        self.meta["source_initial"] = self.source_initial

    def verify_after(self):
        control_good = False
        source_good = False
        if self.control is None:
            self.verify_error = "input-terminal-control-unavailable"
        else:
            try:
                control_good = self.control.verify_complete()
            except BaseException:
                control_good = False
                self.verify_error = "input-terminal-control"
        try:
            if self.control is None:
                raise Stop("input-terminal-source-unavailable")
            self.source_terminal = observe_source(self.control.notes)
            source_good = (
                observation_signature(self.source_terminal)
                == observation_signature(self.source_initial)
            )
        except BaseException:
            source_good = False
            if self.verify_error == "none":
                self.verify_error = "input-terminal-source"
        self.meta["source_terminal"] = self.source_terminal
        self.post_inputs_reverified = int(
            self.input_construction_complete == 1
            and control_good
            and source_good
        )
        if self.post_inputs_reverified != 1 and self.verify_error == "none":
            self.verify_error = "input-terminal-drift"
        if CLOSE_FAILED:
            self.post_inputs_reverified = 0
            self.verify_error = "input-close"
        self.meta["post_inputs_reverified"] = self.post_inputs_reverified
        return self.post_inputs_reverified == 1

    def close(self):
        try:
            close_observation(self.source_terminal, "source-terminal-close")
        except BaseException:
            note_close_failure("source-terminal-close")
        try:
            close_observation(self.source_initial, "source-initial-close")
        except BaseException:
            note_close_failure("source-initial-close")
        if self.control is not None:
            actions = [record.close for record in self.control.records]
            actions.extend(
                (
                    self.control.self_record.close,
                    self.control.env_record.close,
                    self.control.bash_record.close,
                    self.control.python_record.close,
                    self.control.notes.close,
                    self.control.usr_bin.close,
                    self.control.python_bin.close,
                    self.control.status.close,
                )
            )
            for action in actions:
                try:
                    action()
                except BaseException:
                    note_close_failure("control-input-close")
        return CLOSE_FAILED == 0

class UnavailableBinderInputs:
    def __init__(self, meta, reason):
        self.meta = meta
        self.verify_error = reason
        schema_error(self.meta, reason)

    def verify_after(self):
        self.meta["source_terminal"] = empty_observation(SOURCE_NAME)
        self.meta["post_inputs_reverified"] = 0
        return False

    def close(self):
        return close_all()

def inventory_line(snapshot):
    inventory = snapshot["inventory"]
    return (
        "INVENTORY snapshot="
        + str(snapshot["index"])
        + " items="
        + str(len(inventory["names"]))
        + " complete="
        + str(inventory["complete"])
        + " reason_bits="
        + inventory_reason_text(inventory)
        + " reason_truncated="
        + str(inventory["reason_truncated"])
        + " framing_kind=full"
        + " framing_bytes="
        + str(len(inventory["frame"]))
        + " framing_LF="
        + str(inventory["frame"].count(b"\n"))
        + " sha256="
        + sha(inventory["frame"])
        + " overflow_name_bytes="
        + inventory["overflow_bytes"]
        + " overflow_name_sha256="
        + inventory["overflow_sha"]
        + " frame_hex="
        + (inventory["frame"].hex() if inventory["frame"] else "none")
        + "\n"
    ).encode("ascii")

def relation_line(snapshot):
    return (
        "RELATIONS snapshot="
        + str(snapshot["index"])
        + " duplicate_pairs="
        + (",".join(snapshot["duplicates"]) if snapshot["duplicates"] else "none")
        + " source_aliases="
        + (",".join(snapshot["aliases"]) if snapshot["aliases"] else "none")
        + " unknown_count="
        + str(len(snapshot["unknown_names"]))
        + " anomaly_count="
        + str(len(snapshot["anomalies"]))
        + "\n"
    ).encode("ascii")

def classify_phase(meta, recovery, pass_seen):
    if recovery:
        return "unknown-mismatch"
    if (
        meta["source_initial"]["exact"] != 1
        or meta["source_equal"] != 1
        or meta["evidence_initial"]["exact"] != 1
        or meta["evidence_equal"] != 1
        or meta["snapshot_1_attempt_complete"] != 1
        or meta["snapshot_2_attempt_complete"] != 1
        or meta["snapshot_3_attempt_complete"] != 1
        or meta["evidence_initial_path_finalized_after_bracket"] != 1
        or meta["evidence_terminal_path_finalized_after_bracket"] != 1
        or meta["inventories_complete"] != 1
        or meta["snapshots_equal"] != 1
        or meta["post_inputs_reverified"] != 1
        or CLOSE_FAILED
        or meta["unknown_union"]
        or meta["duplicate_union"]
        or meta["alias_union"]
        or meta["anomaly_union"]
    ):
        return "unknown-mismatch"
    for snapshot in meta["snapshots"]:
        if not all(candidate_is_valid(record) for record in snapshot["records"]):
            return "unknown-mismatch"
        present_names = tuple(sorted(
            record["name"]
            for record in snapshot["records"]
            if record["state"] == "present"
        ))
        if snapshot["inventory"]["names"] != present_names:
            return "unknown-mismatch"
    records = meta["snapshots"][0]["records"]
    mapping = {record["name"]: record for record in records}
    order = (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME, COPY_NAME, STATUS_RECEIPT_NAME)
    present = tuple(name for name in order if mapping[name]["state"] == "present")
    if present == ():
        return "pre-create"
    if present == (STDOUT_RECEIPT_NAME,):
        return "stdout-present-last-durability-unproven"
    if present == (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME):
        return "stdout-durable-and-stderr-present-last-durability-unproven"
    if present == (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME, COPY_NAME):
        return "stdout-stderr-durable-and-copy-present-last-durability-unproven"
    if present == order:
        if pass_seen:
            return "all-four-durable-post-emission-failure"
        return "first-three-durable-and-status-present-last-durability-unproven"
    return "unknown-mismatch"

def derive_schema(meta, recovery, pass_seen):
    source = meta["source_initial"]
    for snapshot in meta["snapshots"]:
        duplicates, aliases = relation_lists(snapshot["records"], source)
        snapshot["duplicates"] = duplicates
        snapshot["aliases"] = aliases
        snapshot["anomalies"] = snapshot_anomalies(snapshot)
    meta["source_equal"] = int(
        observation_signature(meta["source_initial"])
        == observation_signature(meta["source_terminal"])
    )
    meta["evidence_equal"] = int(
        meta["evidence_initial_path_finalized_after_bracket"] == 1
        and meta["evidence_terminal_path_finalized_after_bracket"] == 1
        and observation_signature(meta["evidence_initial"])
        == observation_signature(meta["evidence_terminal"])
    )
    meta["snapshots_equal"] = int(
        snapshot_signature(meta["snapshots"][0])
        == snapshot_signature(meta["snapshots"][1])
        == snapshot_signature(meta["snapshots"][2])
    )
    meta["inventories_complete"] = int(
        all(snapshot["inventory"]["complete"] == 1 for snapshot in meta["snapshots"])
    )
    meta["unknown_union"] = tuple(sorted(set(
        name for snapshot in meta["snapshots"] for name in snapshot["unknown_names"]
    )))
    meta["duplicate_union"] = tuple(sorted(set(
        value for snapshot in meta["snapshots"] for value in snapshot["duplicates"]
    )))
    meta["alias_union"] = tuple(sorted(set(
        value for snapshot in meta["snapshots"] for value in snapshot["aliases"]
    )))
    global_anomalies = []
    for tag, record in (
        ("source-initial", meta["source_initial"]),
        ("source-terminal", meta["source_terminal"]),
        ("evidence-initial", meta["evidence_initial"]),
        ("evidence-terminal", meta["evidence_terminal"]),
    ):
        if record["exact"] != 1:
            global_anomalies.append(tag + "-not-exact")
        if record["stable"] != 1:
            global_anomalies.append(tag + "-unstable")
        if record["error"] != "none" or record["final_error"] != "none":
            global_anomalies.append(tag + "-error")
        if tag.startswith("source-") and record["state"] == "present" and record["nlink"] != "1":
            global_anomalies.append(tag + "-nlink-" + record["nlink"])
        if tag.startswith("evidence-") and record["state"] == "present" and record["nlink"] != "2":
            global_anomalies.append(tag + "-nlink-" + record["nlink"])
        if tag.startswith("source-") and record["state"] == "present" and record["type"] != "regular":
            global_anomalies.append(tag + "-nonregular-" + record["type"])
        if tag.startswith("evidence-") and record["state"] == "present" and record["type"] != "directory":
            global_anomalies.append(tag + "-nondirectory-" + record["type"])
        if record["content"] == "unavailable-size-cap":
            global_anomalies.append(tag + "-size-cap")
    if meta["source_equal"] != 1:
        global_anomalies.append("source-cross-drift")
    if meta["evidence_equal"] != 1:
        global_anomalies.append("evidence-cross-drift")
    if meta["snapshot_1_attempt_complete"] != 1:
        global_anomalies.append("snapshot-1-attempt-incomplete")
    if meta["snapshot_2_attempt_complete"] != 1:
        global_anomalies.append("snapshot-2-attempt-incomplete")
    if meta["snapshot_3_attempt_complete"] != 1:
        global_anomalies.append("snapshot-3-attempt-incomplete")
    if meta["evidence_initial_path_finalized_after_bracket"] != 1:
        global_anomalies.append("evidence-initial-finalizer-incomplete")
    if meta["evidence_terminal_path_finalized_after_bracket"] != 1:
        global_anomalies.append("evidence-terminal-finalizer-incomplete")
    if meta["snapshots_equal"] != 1:
        global_anomalies.append("snapshot-cross-drift")
    meta["global_anomalies"] = tuple(sorted(set(global_anomalies)))
    meta["anomaly_union"] = tuple(sorted(set(
        list(meta["global_anomalies"])
        + [
            "snapshot-" + str(snapshot["index"]) + "-" + value
            for snapshot in meta["snapshots"]
            for value in snapshot["anomalies"]
        ]
    )))
    meta["proposed_phase"] = classify_phase(meta, recovery, pass_seen)
    infrastructure_good = (
        meta["post_inputs_reverified"] == 1
        and not CLOSE_FAILED
        and not meta["errors"]
        and not meta["errors_truncated"]
    )
    meta["base_status"] = "ok" if infrastructure_good else "error"

def bounded_ascii(value, cap):
    if not isinstance(value, str) or len(value) > cap:
        return False
    try:
        value.encode("ascii")
    except BaseException:
        return False
    return True

def observation_shape_good(record, expected_name):
    template = empty_observation(expected_name)
    if not isinstance(record, dict) or set(record) != set(template):
        return False
    if record["name"] != expected_name or record["fds"] != []:
        return False
    if record["path_fd"] is not None or record["dir_fd"] is not None or record["dir_key"] is not None:
        return False
    for key in ("terminal", "exact", "exact_absent", "stable", "path_fd_opened", "directory_fd_opened", "path_finalized_after_bracket"):
        if record[key] not in (0, 1):
            return False
    for key, value in record.items():
        if isinstance(template[key], str) and not bounded_ascii(value, 256):
            return False
    for key in ("key", "final_key"):
        value = record[key]
        if value is not None and (not isinstance(value, tuple) or len(value) != 7):
            return False
    return True

def inventory_shape_good(inventory):
    template = new_inventory()
    if not isinstance(inventory, dict) or set(inventory) != set(template):
        return False
    if not isinstance(inventory["names"], tuple) or len(inventory["names"]) > INVENTORY_ITEMS_CAP:
        return False
    if any(not isinstance(name, bytes) for name in inventory["names"]):
        return False
    if sum(len(name) for name in inventory["names"]) > INVENTORY_RAW_CAP:
        return False
    if not isinstance(inventory["frame"], bytes) or len(inventory["frame"]) > BINDER_CAP:
        return False
    if inventory["complete"] not in (0, 1) or inventory["reason_truncated"] not in (0, 1):
        return False
    bits = inventory["reason_bits"]
    if not isinstance(bits, dict) or tuple(bits) != INVENTORY_REASON_ORDER:
        return False
    if any(bits[key] not in (0, 1) for key in INVENTORY_REASON_ORDER):
        return False
    return bounded_ascii(inventory["overflow_bytes"], 256) and bounded_ascii(inventory["overflow_sha"], 256)

def bounded_tuple(value, item_kind, count_cap, byte_cap):
    if not isinstance(value, tuple) or len(value) > count_cap:
        return False
    total = 0
    for item in value:
        if item_kind == "bytes":
            if not isinstance(item, bytes):
                return False
            total += len(item)
        else:
            if not bounded_ascii(item, 256):
                return False
            total += len(item)
    return total <= byte_cap

def validate_schema_shape(meta):
    if not isinstance(meta, dict):
        return False
    mode = meta.get("mode")
    if mode not in ("normal", "watchdog", "recovery", "recovery-binder"):
        return False
    template = new_audit_schema(mode)
    if set(meta) != set(template):
        return False
    if not observation_shape_good(meta["source_initial"], SOURCE_NAME):
        return False
    if not observation_shape_good(meta["source_terminal"], SOURCE_NAME):
        return False
    if not observation_shape_good(meta["evidence_initial"], EVIDENCE_NAME):
        return False
    if not observation_shape_good(meta["evidence_terminal"], EVIDENCE_NAME):
        return False
    snapshots = meta["snapshots"]
    if not isinstance(snapshots, list) or len(snapshots) != 3:
        return False
    for offset, snapshot in enumerate(snapshots):
        expected = unavailable_snapshot(offset + 1, "unexpected")
        if not isinstance(snapshot, dict) or set(snapshot) != set(expected):
            return False
        if snapshot["index"] != offset + 1 or not inventory_shape_good(snapshot["inventory"]):
            return False
        records = snapshot["records"]
        if not isinstance(records, list) or len(records) != 4:
            return False
        for index, name in enumerate(CANDIDATE_NAMES):
            if not observation_shape_good(records[index], name):
                return False
        if not bounded_tuple(snapshot["unknown_names"], "bytes", UNKNOWN_RECORD_CAP, INVENTORY_RAW_CAP):
            return False
        for key in ("duplicates", "aliases", "anomalies"):
            if not bounded_tuple(snapshot[key], "str", 256, 65536):
                return False
    for key in (
        "source_equal",
        "evidence_equal",
        "snapshots_equal",
        "inventories_complete",
        "post_inputs_reverified",
        "snapshot_1_attempt_complete",
        "snapshot_2_attempt_complete",
        "snapshot_3_attempt_complete",
        "evidence_initial_path_finalized_after_bracket",
        "evidence_terminal_path_finalized_after_bracket",
        "errors_truncated",
    ):
        if meta[key] not in (0, 1):
            return False
    for key in ("recovery_first_esrch", "recovery_second_esrch", "recovery_third_esrch"):
        if meta[key] not in ("na", "0", "1"):
            return False
    if meta["base_status"] not in ("ok", "error"):
        return False
    if not bounded_ascii(meta["proposed_phase"], 256):
        return False
    if not isinstance(meta["errors"], list) or len(meta["errors"]) > 32:
        return False
    if any(not bounded_ascii(value, 256) for value in meta["errors"]):
        return False
    return (
        bounded_tuple(meta["unknown_union"], "bytes", UNKNOWN_RECORD_CAP, INVENTORY_RAW_CAP)
        and bounded_tuple(meta["duplicate_union"], "str", 256, 65536)
        and bounded_tuple(meta["alias_union"], "str", 256, 65536)
        and bounded_tuple(meta["global_anomalies"], "str", 256, 65536)
        and bounded_tuple(meta["anomaly_union"], "str", 768, 196608)
    )

def sanitize_schema(meta):
    mode = meta.get("mode") if isinstance(meta, dict) else "recovery"
    if mode not in ("normal", "watchdog", "recovery", "recovery-binder"):
        mode = "recovery-binder"
    template = new_audit_schema(mode)
    for key in tuple(meta):
        if key not in template:
            del meta[key]
    for key, value in template.items():
        if key not in meta:
            meta[key] = value
    meta["mode"] = mode
    for key, name in (
        ("source_initial", SOURCE_NAME),
        ("source_terminal", SOURCE_NAME),
        ("evidence_initial", EVIDENCE_NAME),
        ("evidence_terminal", EVIDENCE_NAME),
    ):
        if not observation_shape_good(meta[key], name):
            meta[key] = unavailable_candidate(name, "schema-malformed")
    snapshots = meta["snapshots"]
    if not isinstance(snapshots, list) or len(snapshots) != 3:
        meta["snapshots"] = [unavailable_snapshot(index, "unexpected") for index in (1, 2, 3)]
    else:
        for offset in range(3):
            snapshot = snapshots[offset]
            good = isinstance(snapshot, dict) and snapshot.get("index") == offset + 1
            good = good and inventory_shape_good(snapshot.get("inventory"))
            records = snapshot.get("records") if good else None
            good = good and isinstance(records, list) and len(records) == 4
            if good:
                good = all(observation_shape_good(records[index], name) for index, name in enumerate(CANDIDATE_NAMES))
            if not good:
                snapshots[offset] = unavailable_snapshot(offset + 1, "unexpected")
    for key in (
        "source_equal",
        "evidence_equal",
        "snapshots_equal",
        "inventories_complete",
        "post_inputs_reverified",
        "snapshot_1_attempt_complete",
        "snapshot_2_attempt_complete",
        "snapshot_3_attempt_complete",
        "evidence_initial_path_finalized_after_bracket",
        "evidence_terminal_path_finalized_after_bracket",
        "errors_truncated",
    ):
        meta[key] = int(meta[key] == 1)
    for key in ("recovery_first_esrch", "recovery_second_esrch", "recovery_third_esrch"):
        if meta[key] not in ("na", "0", "1"):
            meta[key] = "0"
    meta["base_status"] = "error"
    meta["proposed_phase"] = "unknown-mismatch"
    if not isinstance(meta["errors"], list):
        meta["errors"] = []
    meta["errors"] = [value for value in meta["errors"][:31] if bounded_ascii(value, 256)]
    if "schema-malformed" not in meta["errors"]:
        meta["errors"].append("schema-malformed")
    for key, kind, count_cap, byte_cap in (
        ("unknown_union", "bytes", UNKNOWN_RECORD_CAP, INVENTORY_RAW_CAP),
        ("duplicate_union", "str", 256, 65536),
        ("alias_union", "str", 256, 65536),
        ("global_anomalies", "str", 256, 65536),
        ("anomaly_union", "str", 768, 196608),
    ):
        if not bounded_tuple(meta[key], kind, count_cap, byte_cap):
            meta[key] = ()
    if not validate_schema_shape(meta):
        meta["snapshots"] = [unavailable_snapshot(index, "unexpected") for index in (1, 2, 3)]
        meta["unknown_union"] = ()
        meta["duplicate_union"] = ()
        meta["alias_union"] = ()
        meta["global_anomalies"] = ()
        meta["anomaly_union"] = ()
    return meta

def serialize_schema(meta):
    unknown_union_frame = b"".join(
        str(len(name)).encode("ascii") + b":" + name.hex().encode("ascii") + b"\n"
        for name in meta["unknown_union"]
    )
    anomaly_union_frame = b"".join(
        value.encode("ascii") + b"\n" for value in meta["anomaly_union"]
    )
    parts = [
        b"AUDIT_SCHEMA version=4 layout=fixed source_records=2 evidence_records=2 inventories=3 candidates=12\n",
        observation_line("SOURCE", "initial", meta["source_initial"]),
        observation_line("SOURCE", "terminal", meta["source_terminal"]),
        observation_line("EVIDENCE", "initial", meta["evidence_initial"]),
        observation_line("EVIDENCE", "terminal", meta["evidence_terminal"]),
    ]
    for snapshot in meta["snapshots"]:
        parts.append(inventory_line(snapshot))
        for name_index, name in enumerate(snapshot["unknown_names"]):
            parts.append(
                (
                    "UNKNOWN_CHILD snapshot="
                    + str(snapshot["index"])
                    + " index="
                    + str(name_index)
                    + " name_hex="
                    + name.hex()
                    + " observation=name-only opened=0\n"
                ).encode("ascii")
            )
        for candidate_index, record in enumerate(snapshot["records"]):
            parts.append(
                observation_line(
                    "CANDIDATE",
                    str(snapshot["index"]) + "-" + str(candidate_index),
                    record,
                )
            )
        parts.append(relation_line(snapshot))
        for anomaly_index, value in enumerate(snapshot["anomalies"]):
            parts.append(
                (
                    "ANOMALY snapshot="
                    + str(snapshot["index"])
                    + " index="
                    + str(anomaly_index)
                    + " token="
                    + value
                    + "\n"
                ).encode("ascii")
            )
    parts.append(
        (
            "CROSS source_equal="
            + str(meta["source_equal"])
            + " evidence_equal="
            + str(meta["evidence_equal"])
            + " snapshots_equal="
            + str(meta["snapshots_equal"])
            + " inventories_complete="
            + str(meta["inventories_complete"])
            + " snapshot_1_attempt_complete="
            + str(meta["snapshot_1_attempt_complete"])
            + " snapshot_2_attempt_complete="
            + str(meta["snapshot_2_attempt_complete"])
            + " snapshot_3_attempt_complete="
            + str(meta["snapshot_3_attempt_complete"])
            + " evidence_initial_path_finalized_after_bracket="
            + str(meta["evidence_initial_path_finalized_after_bracket"])
            + " evidence_terminal_path_finalized_after_bracket="
            + str(meta["evidence_terminal_path_finalized_after_bracket"])
            + "\n"
        ).encode("ascii")
    )
    for anomaly_index, value in enumerate(meta["global_anomalies"]):
        parts.append(
            (
                "GLOBAL_ANOMALY index="
                + str(anomaly_index)
                + " token="
                + value
                + "\n"
            ).encode("ascii")
        )
    parts.append(
        (
            "UNION unknown_count="
            + str(len(meta["unknown_union"]))
            + " unknown_framing_bytes="
            + str(len(unknown_union_frame))
            + " unknown_sha256="
            + sha(unknown_union_frame)
            + " duplicate_pairs="
            + (",".join(meta["duplicate_union"]) if meta["duplicate_union"] else "none")
            + " source_aliases="
            + (",".join(meta["alias_union"]) if meta["alias_union"] else "none")
            + " anomaly_count="
            + str(len(meta["anomaly_union"]))
            + " anomaly_framing_bytes="
            + str(len(anomaly_union_frame))
            + " anomaly_sha256="
            + sha(anomaly_union_frame)
            + "\n"
        ).encode("ascii")
    )
    parts.append(
        (
            "REVERIFY post_inputs_reverified="
            + str(meta["post_inputs_reverified"])
            + " recovery_first_esrch="
            + meta["recovery_first_esrch"]
            + " recovery_second_esrch="
            + meta["recovery_second_esrch"]
            + " recovery_third_esrch="
            + meta["recovery_third_esrch"]
            + " internal_close_error="
            + str(int(CLOSE_FAILED))
            + " errors="
            + (",".join(meta["errors"]) if meta["errors"] else "none")
            + " errors_truncated="
            + str(meta["errors_truncated"])
            + "\n"
        ).encode("ascii")
    )
    return b"".join(parts)

def binder_observe(inputs, meta, recovery, pass_seen, evidence_allowed):
    parent = None
    terminal_parent = None
    evidence_initial = None
    evidence_terminal = None
    snapshots = meta["snapshots"]
    if evidence_allowed:
        try:
            parent = Chain(EVIDENCE_PARENT_COMPONENTS)
            evidence_initial = begin_evidence(parent)
            meta["evidence_initial"] = evidence_initial
        except BaseException as error:
            schema_error(meta, error.code if isinstance(error, Stop) else "evidence-initial-begin")
    else:
        schema_error(meta, "evidence-gate-unavailable")
    try:
        if evidence_initial is None or evidence_initial["dir_fd"] is None:
            schema_error(meta, "snapshot-1-evidence-unavailable")
        else:
            snapshots[0] = take_snapshot(
                1,
                evidence_initial["dir_fd"],
                evidence_initial["dir_key"],
                int(evidence_initial["dev"]),
                snapshots[0],
            )
    except BaseException as error:
        schema_error(meta, error.code if isinstance(error, Stop) else "snapshot-1-unexpected")
    finally:
        meta["snapshot_1_attempt_complete"] = 1
    try:
        if evidence_initial is None or evidence_initial["dir_fd"] is None:
            schema_error(meta, "snapshot-2-evidence-unavailable")
        else:
            snapshots[1] = take_snapshot(
                2,
                evidence_initial["dir_fd"],
                evidence_initial["dir_key"],
                int(evidence_initial["dev"]),
                snapshots[1],
            )
    except BaseException as error:
        schema_error(meta, error.code if isinstance(error, Stop) else "snapshot-2-unexpected")
    finally:
        meta["snapshot_2_attempt_complete"] = 1
    if evidence_initial is not None and parent is not None:
        try:
            finish_evidence(evidence_initial, parent)
        except BaseException:
            schema_error(meta, "evidence-initial-finish")
        finally:
            meta["evidence_initial_path_finalized_after_bracket"] = evidence_initial[
                "path_finalized_after_bracket"
            ]
    if evidence_allowed:
        try:
            terminal_parent = Chain(EVIDENCE_PARENT_COMPONENTS)
            evidence_terminal = begin_evidence(terminal_parent)
            meta["evidence_terminal"] = evidence_terminal
        except BaseException as error:
            schema_error(meta, error.code if isinstance(error, Stop) else "evidence-terminal-begin")
    try:
        if evidence_terminal is None or evidence_terminal["dir_fd"] is None:
            schema_error(meta, "snapshot-3-evidence-unavailable")
        else:
            snapshots[2] = take_snapshot(
                3,
                evidence_terminal["dir_fd"],
                evidence_terminal["dir_key"],
                int(evidence_terminal["dev"]),
                snapshots[2],
            )
    except BaseException as error:
        schema_error(meta, error.code if isinstance(error, Stop) else "snapshot-3-unexpected")
    finally:
        meta["snapshot_3_attempt_complete"] = 1
    if evidence_terminal is not None and terminal_parent is not None:
        try:
            finish_evidence(evidence_terminal, terminal_parent)
        except BaseException:
            schema_error(meta, "evidence-terminal-finish")
        finally:
            meta["evidence_terminal_path_finalized_after_bracket"] = evidence_terminal[
                "path_finalized_after_bracket"
            ]
    for snapshot in reversed(snapshots):
        try:
            close_snapshot(snapshot)
        except BaseException:
            schema_error(meta, "snapshot-close")
    if evidence_terminal is not None:
        try:
            close_evidence(evidence_terminal)
        except BaseException:
            schema_error(meta, "evidence-terminal-close")
    if evidence_initial is not None:
        try:
            close_evidence(evidence_initial)
        except BaseException:
            schema_error(meta, "evidence-initial-close")
    if terminal_parent is not None:
        try:
            terminal_parent.close()
        except BaseException:
            schema_error(meta, "evidence-terminal-parent-close")
    if parent is not None:
        try:
            parent.close()
        except BaseException:
            schema_error(meta, "evidence-initial-parent-close")
    try:
        inputs.verify_after()
    except BaseException:
        schema_error(meta, "input-terminal-drift")
    try:
        if not inputs.close():
            schema_error(meta, "input-close")
    except BaseException:
        schema_error(meta, "input-close-unexpected")
    if inputs.verify_error != "none":
        schema_error(meta, inputs.verify_error)
    try:
        if not close_all():
            schema_error(meta, "final-close-sweep")
    except BaseException:
        schema_error(meta, "final-close-sweep-unexpected")
    try:
        derive_schema(meta, recovery, pass_seen)
    except BaseException:
        schema_error(meta, "schema-derive")
    return meta

def binder_header(meta, status, phase):
    sites = ",".join(CLOSE_FAILURE_SITES) if CLOSE_FAILURE_SITES else "none"
    return (
        "BINDER version=4 schema-layout=full status="
        + status
        + " mode="
        + meta["mode"]
        + " durability_phase="
        + phase
        + " inventory_complete="
        + str(meta["inventories_complete"])
        + " snapshots_stable="
        + str(meta["snapshots_equal"])
        + " source_stable="
        + str(meta["source_equal"])
        + " evidence_stable="
        + str(meta["evidence_equal"])
        + " post_inputs_reverified="
        + str(meta["post_inputs_reverified"])
        + " recovery_first_esrch="
        + meta["recovery_first_esrch"]
        + " recovery_second_esrch="
        + meta["recovery_second_esrch"]
        + " recovery_third_esrch="
        + meta["recovery_third_esrch"]
        + " internal_close_error="
        + str(int(CLOSE_FAILED))
        + " close_failure_sites="
        + sites
        + " close_failure_sites_truncated="
        + str(CLOSE_FAILURE_SITES_TRUNCATED)
        + " errors="
        + (",".join(meta["errors"]) if meta["errors"] else "none")
        + " errors_truncated="
        + str(meta["errors_truncated"])
        + "\n"
    ).encode("ascii")

def schema_overflow(kind, value):
    return (
        "SCHEMA_OVERFLOW schema-layout=overflow status=PERMANENT_FAILURE kind="
        + kind
        + " observed_bytes="
        + str(len(value))
        + " sha256="
        + sha(value)
        + "\n"
    ).encode("ascii")

def render_binder(meta, recovery):
    if not validate_schema_shape(meta):
        schema_error(meta, "schema-shape")
        sanitize_schema(meta)
    try:
        body = serialize_schema(meta)
    except BaseException:
        schema_error(meta, "schema-serialize")
        sanitize_schema(meta)
        need(validate_schema_shape(meta), "schema-layout-sanitize")
        body = serialize_schema(meta)
    status = meta["base_status"]
    phase = meta["proposed_phase"]
    if (
        status == "error"
        or meta["inventories_complete"] != 1
        or meta["snapshots_equal"] != 1
        or meta["source_equal"] != 1
        or meta["evidence_equal"] != 1
        or meta["post_inputs_reverified"] != 1
        or CLOSE_FAILED
    ):
        status = "error"
        phase = "unknown-mismatch"
    if recovery:
        status = "error"
        phase = "unknown-mismatch"
    if recovery:
        provenance = (
            b"PROVENANCE status_receipt=payload-created-synthetic-nonauthoritative "
            b"wait_provenance=unavailable-recovery "
            b"stream_provenance=unavailable-recovery\n"
        )
    else:
        provenance = (
            b"PROVENANCE status_receipt=payload-created-synthetic-nonauthoritative "
            b"wait_provenance=watchdog-waitpid-authoritative "
            b"stream_provenance=watchdog-separate-raw-pipes\n"
        )
    report = binder_header(meta, status, phase) + body + provenance + b"BINDER_END\n"
    if len(report) > BINDER_WORST:
        overflow = schema_overflow("binder", report)
        schema_error(meta, "schema-overflow")
        status = "error"
        phase = "unknown-mismatch"
        report = (
            b"BINDER version=4 schema-layout=overflow status=error mode="
            + meta["mode"].encode("ascii")
            + b" durability_phase=unknown-mismatch\n"
            + overflow
            + provenance
            + b"BINDER_END\n"
        )
    need(len(report) <= BINDER_WORST and len(report) <= BINDER_CAP, "binder-cap")
    return report, status, phase
def wait_deadline(pid, deadline):
    while True:
        if time.monotonic_ns() >= deadline:
            return False, False, None
        try:
            got, status_value = os.waitpid(pid, os.WNOHANG)
        except InterruptedError:
            if time.monotonic_ns() >= deadline:
                return False, False, None
            continue
        observed = time.monotonic_ns()
        timely = observed < deadline
        if got == pid:
            return True, timely, status_value
        if not timely:
            return False, False, None
        need(got == 0, "waitpid-other")
        remaining = deadline - observed
        time.sleep(min(0.01, remaining / 1000000000))

def wait_blocking(pid):
    while True:
        try:
            got, status_value = os.waitpid(pid, 0)
        except InterruptedError:
            continue
        need(got == pid, "waitpid-other")
        return status_value

def remaining_poll_ms(deadline, code):
    now = time.monotonic_ns()
    need(now < deadline, code + "-timeout")
    remaining = deadline - now
    return min(POLL_SLICE_MS, max(1, (remaining + 999999) // 1000000))

def require_before(deadline, code):
    need(time.monotonic_ns() < deadline, code + "-timeout")

def read_token_eof(fd, token, deadline, code):
    os.set_blocking(fd, False)
    poller = select.poll()
    poller.register(fd, select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL)
    data = bytearray()
    eof = False
    while not eof:
        events = poller.poll(remaining_poll_ms(deadline, code))
        require_before(deadline, code)
        for current, mask in events:
            need(current == fd and not mask & select.POLLNVAL, code + "-poll")
            while True:
                require_before(deadline, code)
                try:
                    piece = os.read(fd, len(token) + 1)
                except BlockingIOError:
                    break
                require_before(deadline, code)
                if piece == b"":
                    eof = True
                    break
                data.extend(piece)
                need(len(data) <= len(token) and bytes(data) == token[:len(data)], code + "-byte")
    require_before(deadline, code)
    need(bytes(data) == token, code + "-framing")
    return bytes(data)

def wait_start(fd):
    os.set_blocking(fd, False)
    poller = select.poll()
    poller.register(fd, select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL)
    while True:
        events = poller.poll(POLL_SLICE_MS)
        for current, mask in events:
            need(current == fd and not mask & select.POLLNVAL, "start-poll")
            try:
                piece = os.read(fd, 2)
            except BlockingIOError:
                continue
            need(piece == b"S", "start-byte")
            try:
                extra = os.read(fd, 1)
            except BlockingIOError:
                return
            need(extra is None, "start-extra")

def prove_payload_input_live(fd):
    os.set_blocking(fd, False)
    try:
        piece = os.read(fd, 1)
    except BlockingIOError:
        piece = None
    need(piece is None, "payload-stdin-not-empty-live")
    os.set_blocking(fd, True)

def probe_lifeline(fd):
    os.set_blocking(fd, False)
    try:
        piece = os.read(fd, 1)
    except BlockingIOError:
        return True
    except OSError:
        return False
    return False if piece == b"" else False

def begin_line(watchdog_pid, binding):
    supervisor_pid = os.getpid()
    need(supervisor_pid > 1 and watchdog_pid > 1, "pid")
    value = (
        "BEGIN E001_SUPERVISOR_BINDER_RECOVERY version=4 supervisor_pid="
        + str(supervisor_pid)
        + " watchdog_pid="
        + str(watchdog_pid)
        + " session_sid="
        + str(supervisor_pid)
        + " session_pgid="
        + str(supervisor_pid)
        + " watchdog_pgid="
        + str(supervisor_pid)
        + " program_bytes="
        + str(len(CODE_BYTES))
        + " program_LF="
        + str(CODE_BYTES.count(b"\n"))
        + " program_sha256="
        + sha(CODE_BYTES)
        + " whole_control_binding=actor-attested"
        + " self_dev="
        + binding.text[0]
        + " self_ino="
        + binding.text[1]
        + " self_bytes="
        + binding.text[2]
        + " self_LF="
        + binding.text[3]
        + " self_sha256="
        + binding.text[4]
        + " ledger_dev="
        + binding.text[5]
        + " ledger_ino="
        + binding.text[6]
        + " ledger_prefix_bytes="
        + binding.text[7]
        + " ledger_prefix_LF="
        + binding.text[8]
        + " ledger_prefix_sha256="
        + binding.text[9]
        + " ledger_prefix_terminal_hex="
        + binding.text[10]
        + " payload_sha256=6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0"
        + " launcher_sha256=72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd"
        + " inner_sha256=e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f"
        + " actor_overall_deadline_ns="
        + str(ACTOR_OVERALL_DEADLINE_NS)
        + " actor_deadline_semantics=sticky-external"
        + " attempt_consumed=0\n"
    ).encode("ascii")
    need(len(value) <= BEGIN_CAP, "begin-cap")
    return value

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
        "out_close_error": 0,
        "err_close_error": 0,
        "life_close_error": 0,
        "timeout": 0,
        "supervisor_lost": 0,
        "capture_error": "none",
        "wait_raw": None,
        "wait_kind": "none",
        "exit_code": None,
        "signal": None,
        "core": 0,
        "payload_spawned": 0,
        "capture_state": "PAYLOAD_WAIT",
        "payload_deadline_fired": 0,
        "kill_reap_deadline_fired": 0,
        "stream_eof_deadline_fired": 0,
        "payload_wait_observed": 0,
        "payload_wait_timely": 0,
        "kill_reap_wait_observed": 0,
        "kill_reap_wait_timely": 0,
        "stdout_eof_observed": 0,
        "stdout_eof_timely": 0,
        "stderr_eof_observed": 0,
        "stderr_eof_timely": 0,
        "child_reaped": 0,
        "kill_sent": 0,
        "capture_complete": 0,
        "recovery_pgid": "none",
        "wait_provenance": "watchdog-waitpid-authoritative",
        "stream_provenance": "watchdog-separate-raw-pipes",
        "streams_available": 1,
        "wait_available": 1,
        "recovery_esrch_initial": "na",
        "recovery_esrch_pre_evidence": "na",
        "recovery_esrch_terminal": "na",
    }

def recovery_capture(pgid):
    return {
        "out": bytearray(),
        "err": bytearray(),
        "out_total": "unavailable",
        "err_total": "unavailable",
        "out_lf": "unavailable",
        "err_lf": "unavailable",
        "out_hash": None,
        "err_hash": None,
        "out_overflow": "unavailable",
        "err_overflow": "unavailable",
        "out_eof": "unavailable",
        "err_eof": "unavailable",
        "out_close_error": "unavailable",
        "err_close_error": "unavailable",
        "life_close_error": "unavailable",
        "timeout": "unavailable",
        "supervisor_lost": 1,
        "capture_error": "watchdog-report-lost",
        "wait_raw": None,
        "wait_kind": "unavailable",
        "exit_code": None,
        "signal": None,
        "core": "unavailable",
        "payload_spawned": "unavailable",
        "capture_state": "unavailable",
        "payload_deadline_fired": "unavailable",
        "kill_reap_deadline_fired": "unavailable",
        "stream_eof_deadline_fired": "unavailable",
        "payload_wait_observed": "unavailable",
        "payload_wait_timely": "unavailable",
        "kill_reap_wait_observed": "unavailable",
        "kill_reap_wait_timely": "unavailable",
        "stdout_eof_observed": "unavailable",
        "stdout_eof_timely": "unavailable",
        "stderr_eof_observed": "unavailable",
        "stderr_eof_timely": "unavailable",
        "child_reaped": "unavailable",
        "kill_sent": "unavailable",
        "capture_complete": "unavailable",
        "recovery_pgid": str(pgid),
        "wait_provenance": "unavailable-recovery",
        "stream_provenance": "unavailable-recovery",
        "streams_available": 0,
        "wait_available": 0,
        "recovery_esrch_initial": "1",
        "recovery_esrch_pre_evidence": "1",
        "recovery_esrch_terminal": "1",
    }

def mark_capture_error(state, value):
    if state["capture_error"] == "none":
        state["capture_error"] = value

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

def close_stream(state, key, fd, poller, open_streams):
    try:
        poller.unregister(fd)
    except BaseException:
        mark_capture_error(state, key + "-unregister")
    site = "payload-out-close" if key == "out" else "payload-err-close"
    closed = close_fd(fd, site)
    state[key + "_close_error"] |= int(not closed)
    if not closed:
        mark_capture_error(state, key + "-close")
    if fd in open_streams:
        del open_streams[fd]

def latch_capture_deadline(state, bit, code):
    state[bit] = 1
    state["timeout"] = 1
    mark_capture_error(state, code)

def capture_guard(state, deadline, bit, code):
    if time.monotonic_ns() >= deadline:
        latch_capture_deadline(state, bit, code)
        return False
    return True

def capture_poll_ms(state, deadline, bit, code):
    if not capture_guard(state, deadline, bit, code):
        return 0
    remaining = deadline - time.monotonic_ns()
    if remaining <= 0:
        latch_capture_deadline(state, bit, code)
        return 0
    return min(POLL_SLICE_MS, max(1, (remaining + 999999) // 1000000))

def capture_wait_once(pid, state, deadline, bit, code, observed_key, timely_key):
    if not capture_guard(state, deadline, bit, code):
        return False
    try:
        got, status_value = os.waitpid(pid, os.WNOHANG)
    except InterruptedError:
        capture_guard(state, deadline, bit, code)
        return False
    except BaseException:
        capture_guard(state, deadline, bit, code)
        mark_capture_error(state, code + "-error")
        return False
    timely = capture_guard(state, deadline, bit, code)
    if got == pid:
        state["child_reaped"] = 1
        state[observed_key] = 1
        state[timely_key] = int(timely)
        state["wait_raw"] = status_value
        if not timely:
            state["wait_kind"] = "late-physical"
        return timely
    if got != 0:
        mark_capture_error(state, code + "-other")
    return False

def capture_read_once(state, key, fd, poller, open_streams, deadline, bit, code):
    if not capture_guard(state, deadline, bit, code):
        return
    try:
        piece = os.read(fd, CHUNK)
    except BlockingIOError:
        capture_guard(state, deadline, bit, code)
        return
    except BaseException:
        capture_guard(state, deadline, bit, code)
        mark_capture_error(state, key + "-read")
        close_stream(state, key, fd, poller, open_streams)
        return
    timely = capture_guard(state, deadline, bit, code)
    if piece == b"":
        state[key + "_eof"] = 1
        state[("stdout" if key == "out" else "stderr") + "_eof_observed"] = 1
        state[("stdout" if key == "out" else "stderr") + "_eof_timely"] = int(timely)
        close_stream(state, key, fd, poller, open_streams)
    elif timely:
        capture_piece(state, key, piece, STDOUT_CAP if key == "out" else STDERR_CAP)

def capture_lifeline_once(state, fd, poller, deadline, bit, code):
    if not capture_guard(state, deadline, bit, code):
        return
    try:
        piece = os.read(fd, CHUNK)
    except BlockingIOError:
        capture_guard(state, deadline, bit, code)
        return
    except BaseException:
        capture_guard(state, deadline, bit, code)
        mark_capture_error(state, "lifeline-read")
        return
    timely = capture_guard(state, deadline, bit, code)
    if not timely:
        return
    if piece == b"":
        state["supervisor_lost"] = 1
        try:
            poller.unregister(fd)
        except BaseException:
            mark_capture_error(state, "lifeline-unregister")
    else:
        mark_capture_error(state, "lifeline-data")

def classify_capture_wait(state):
    value = state["wait_raw"]
    if value is None or state["payload_wait_timely"] != 1:
        return
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

def capture_complete_good(state, open_streams):
    return (
        state["payload_wait_observed"] == 1
        and state["payload_wait_timely"] == 1
        and state["stdout_eof_observed"] == 1
        and state["stdout_eof_timely"] == 1
        and state["stderr_eof_observed"] == 1
        and state["stderr_eof_timely"] == 1
        and state["payload_deadline_fired"] == 0
        and state["kill_reap_deadline_fired"] == 0
        and state["stream_eof_deadline_fired"] == 0
        and state["kill_sent"] == 0
        and state["child_reaped"] == 1
        and state["out_close_error"] == 0
        and state["err_close_error"] == 0
        and state["capture_error"] == "none"
        and not open_streams
        and not CLOSE_FAILED
    )

def capture_payload(state, pid, out_fd, err_fd, life_fd, payload_deadline, forced_error):
    os.set_blocking(out_fd, False)
    os.set_blocking(err_fd, False)
    os.set_blocking(life_fd, False)
    poller = select.poll()
    masks = select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL
    poller.register(out_fd, masks)
    poller.register(err_fd, masks)
    poller.register(life_fd, masks)
    open_streams = {out_fd: "out", err_fd: "err"}
    kill_reap_deadline = None
    stream_eof_deadline = None
    if forced_error != "none":
        mark_capture_error(state, forced_error)
    while True:
        current = state["capture_state"]
        if current == "PAYLOAD_WAIT":
            capture_wait_once(
                pid,
                state,
                payload_deadline,
                "payload_deadline_fired",
                "payload-wait",
                "payload_wait_observed",
                "payload_wait_timely",
            )
            if state["payload_wait_timely"] == 1:
                state["capture_state"] = "STREAM_EOF"
                stream_eof_deadline = time.monotonic_ns() + PIPE_EOF_GRACE_NS
            failed = (
                forced_error != "none"
                or state["out_overflow"]
                or state["err_overflow"]
                or state["payload_deadline_fired"]
                or state["supervisor_lost"]
                or state["capture_error"] != "none"
                or CLOSE_FAILED
            )
            if failed and state["capture_state"] == "PAYLOAD_WAIT":
                state["capture_state"] = "KILL_REAP"
                if state["child_reaped"] == 1:
                    state["capture_state"] = "UNSAFE"
                else:
                    kill_reap_deadline = time.monotonic_ns() + KILL_REAP_GRACE_NS
                    if capture_guard(
                        state,
                        kill_reap_deadline,
                        "kill_reap_deadline_fired",
                        "kill-reap",
                    ):
                        state["kill_sent"] = 1
                        try:
                            os.kill(pid, signal.SIGKILL)
                        except OSError as error:
                            if error.errno != errno.ESRCH:
                                mark_capture_error(state, "payload-kill")
                        except BaseException:
                            mark_capture_error(state, "payload-kill-unexpected")
        elif current == "KILL_REAP":
            capture_wait_once(
                pid,
                state,
                kill_reap_deadline,
                "kill_reap_deadline_fired",
                "kill-reap",
                "kill_reap_wait_observed",
                "kill_reap_wait_timely",
            )
            if state["kill_reap_wait_observed"] == 1:
                if state["kill_reap_wait_timely"] == 1:
                    state["capture_state"] = "STREAM_EOF"
                    stream_eof_deadline = time.monotonic_ns() + PIPE_EOF_GRACE_NS
                else:
                    state["capture_state"] = "UNSAFE"
            elif state["kill_reap_deadline_fired"] == 1:
                state["capture_state"] = "UNSAFE"
        elif current == "STREAM_EOF":
            if capture_complete_good(state, open_streams):
                state["capture_state"] = "COMPLETE"
                state["capture_complete"] = 1
            elif not open_streams:
                state["capture_state"] = "UNSAFE"
            elif not capture_guard(
                state,
                stream_eof_deadline,
                "stream_eof_deadline_fired",
                "stream-eof",
            ):
                state["capture_state"] = "UNSAFE"
        if state["capture_state"] in ("COMPLETE", "UNSAFE"):
            break
        current = state["capture_state"]
        if current == "PAYLOAD_WAIT":
            deadline = payload_deadline
            bit = "payload_deadline_fired"
            code = "payload-wait"
        elif current == "KILL_REAP":
            deadline = kill_reap_deadline
            bit = "kill_reap_deadline_fired"
            code = "kill-reap"
        else:
            deadline = stream_eof_deadline
            bit = "stream_eof_deadline_fired"
            code = "stream-eof"
        poll_ms = capture_poll_ms(state, deadline, bit, code)
        if poll_ms == 0:
            continue
        try:
            events = poller.poll(poll_ms)
        except BaseException:
            capture_guard(state, deadline, bit, code)
            mark_capture_error(state, "capture-poll")
            continue
        if not capture_guard(state, deadline, bit, code):
            continue
        handled_streams = set()
        for fd, mask in events:
            if mask & select.POLLNVAL:
                mark_capture_error(state, "pollnval")
                continue
            if fd == life_fd:
                capture_lifeline_once(state, life_fd, poller, deadline, bit, code)
                continue
            if fd in open_streams and fd not in handled_streams:
                handled_streams.add(fd)
                key = open_streams[fd]
                capture_read_once(state, key, fd, poller, open_streams, deadline, bit, code)
    if state["capture_state"] == "UNSAFE":
        for fd in tuple(open_streams):
            close_stream(state, open_streams[fd], fd, poller, open_streams)
    classify_capture_wait(state)
    safe = state["capture_state"] == "COMPLETE" and state["capture_complete"] == 1
    return state, safe

def optional(value):
    return "none" if value is None else str(value)

def hash_field(value):
    return "unavailable" if value is None else value.hexdigest()

def stored_hex(state, key):
    if state["streams_available"] == 0:
        return "unavailable"
    return bytes(state[key]).hex() if state[key] else "none"

def stored_bytes(state, key):
    if state["streams_available"] == 0:
        return "unavailable"
    return str(len(state[key]))

def hex_kind(state, key):
    if state["streams_available"] == 0:
        return "unavailable"
    return "prefix" if state[key + "_overflow"] else "full"

def validate_result_capture(mode, state, disposition):
    names = (
        "payload_deadline_fired",
        "kill_reap_deadline_fired",
        "stream_eof_deadline_fired",
        "payload_wait_observed",
        "payload_wait_timely",
        "kill_reap_wait_observed",
        "kill_reap_wait_timely",
        "stdout_eof_observed",
        "stdout_eof_timely",
        "stderr_eof_observed",
        "stderr_eof_timely",
        "child_reaped",
        "kill_sent",
        "capture_complete",
    )
    if mode == "watchdog":
        need(state["capture_state"] in ("PAYLOAD_WAIT", "COMPLETE"), "result-capture-state")
        need(all(state[name] in (0, 1) for name in names), "result-capture-fields")
        if disposition == "SUCCESS":
            need(
                state["capture_state"] == "COMPLETE"
                and state["capture_complete"] == 1
                and state["payload_deadline_fired"] == 0
                and state["kill_reap_deadline_fired"] == 0
                and state["stream_eof_deadline_fired"] == 0
                and state["payload_wait_observed"] == 1
                and state["payload_wait_timely"] == 1
                and state["stdout_eof_observed"] == 1
                and state["stdout_eof_timely"] == 1
                and state["stderr_eof_observed"] == 1
                and state["stderr_eof_timely"] == 1
                and state["child_reaped"] == 1
                and state["kill_sent"] == 0,
                "result-success-capture",
            )
    else:
        need(all(state[name] == "unavailable" for name in names), "result-recovery-capture")

def result_line(mode, state, binder, binder_status, phase, disposition):
    validate_result_capture(mode, state, disposition)
    sites = ",".join(CLOSE_FAILURE_SITES) if CLOSE_FAILURE_SITES else "none"
    fields = (
        "RESULT E001_SUPERVISOR_BINDER_RECOVERY"
        + " version=4"
        + " mode="
        + mode
        + " recovery_pgid="
        + state["recovery_pgid"]
        + " attempt_consumed=1"
        + " payload_spawned="
        + str(state["payload_spawned"])
        + " capture_state="
        + state["capture_state"]
        + " capture_complete="
        + str(state["capture_complete"])
        + " payload_deadline_fired="
        + str(state["payload_deadline_fired"])
        + " kill_reap_deadline_fired="
        + str(state["kill_reap_deadline_fired"])
        + " stream_eof_deadline_fired="
        + str(state["stream_eof_deadline_fired"])
        + " payload_wait_observed="
        + str(state["payload_wait_observed"])
        + " payload_wait_timely="
        + str(state["payload_wait_timely"])
        + " kill_reap_wait_observed="
        + str(state["kill_reap_wait_observed"])
        + " kill_reap_wait_timely="
        + str(state["kill_reap_wait_timely"])
        + " stdout_eof_observed="
        + str(state["stdout_eof_observed"])
        + " stdout_eof_timely="
        + str(state["stdout_eof_timely"])
        + " stderr_eof_observed="
        + str(state["stderr_eof_observed"])
        + " stderr_eof_timely="
        + str(state["stderr_eof_timely"])
        + " child_reaped="
        + str(state["child_reaped"])
        + " kill_sent="
        + str(state["kill_sent"])
        + " payload_success="
        + str(int(disposition == "SUCCESS"))
        + " supervisor_lost="
        + str(state["supervisor_lost"])
        + " timeout="
        + str(state["timeout"])
        + " wait_provenance="
        + state["wait_provenance"]
        + " stream_provenance="
        + state["stream_provenance"]
        + " wait_available="
        + str(state["wait_available"])
        + " streams_available="
        + str(state["streams_available"])
        + " stdout_overflow="
        + str(state["out_overflow"])
        + " stderr_overflow="
        + str(state["err_overflow"])
        + " stdout_close_error="
        + str(state["out_close_error"])
        + " stderr_close_error="
        + str(state["err_close_error"])
        + " lifeline_close_error="
        + str(state["life_close_error"])
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
        + stored_bytes(state, "out")
        + " stdout_LF="
        + str(state["out_lf"])
        + " stdout_sha256="
        + hash_field(state["out_hash"])
        + " stdout_hex_kind="
        + hex_kind(state, "out")
        + " stdout_hex="
        + stored_hex(state, "out")
        + " stderr_bytes="
        + str(state["err_total"])
        + " stderr_stored_bytes="
        + stored_bytes(state, "err")
        + " stderr_LF="
        + str(state["err_lf"])
        + " stderr_sha256="
        + hash_field(state["err_hash"])
        + " stderr_hex_kind="
        + hex_kind(state, "err")
        + " stderr_hex="
        + stored_hex(state, "err")
        + " recovery_esrch_initial="
        + state["recovery_esrch_initial"]
        + " recovery_esrch_pre_evidence="
        + state["recovery_esrch_pre_evidence"]
        + " recovery_esrch_terminal="
        + state["recovery_esrch_terminal"]
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
        + str(int(CLOSE_FAILED))
        + " close_failure_sites="
        + sites
        + " close_failure_sites_truncated="
        + str(CLOSE_FAILURE_SITES_TRUNCATED)
        + " whole_control_binding=actor-attested"
        + " executable_binding=marker-self-bound"
        + " actor_deadline_ns="
        + str(ACTOR_RECOVERY_DEADLINE_NS if mode == "recovery-binder" else ACTOR_OVERALL_DEADLINE_NS)
        + " actor_deadline_semantics=sticky-external"
        + " disposition="
        + disposition
        + "\n"
    )
    value = fields.encode("ascii")
    if len(value) > RESULT_WORST:
        observed_bytes = len(value)
        observed_sha = sha(value)
        value = (
            "RESULT E001_SUPERVISOR_BINDER_RECOVERY version=4 mode="
            + mode
            + " attempt_consumed=1 payload_success=0"
            + " schema-layout=overflow disposition=PERMANENT_FAILURE"
            + " observed_bytes="
            + str(observed_bytes)
            + " observed_sha256="
            + observed_sha
            + "\n"
        ).encode("ascii")
    need(len(value) <= RESULT_WORST and len(value) <= RESULT_CAP, "result-cap")
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

def binding_argv_bytes(binding):
    return tuple(item.encode("ascii") for item in binding.text)

def spawn_payload(strict, state, out_read, out_write, err_read, err_write):
    need(type(strict) is StrictPreflight and strict.launch_token is LAUNCH_TOKEN, "strict-launch-token")
    actions = (
        (os.POSIX_SPAWN_DUP2, out_write, 1),
        (os.POSIX_SPAWN_DUP2, err_write, 2),
        (os.POSIX_SPAWN_CLOSE, 10),
        (os.POSIX_SPAWN_CLOSE, out_read),
        (os.POSIX_SPAWN_CLOSE, out_write),
        (os.POSIX_SPAWN_CLOSE, err_read),
        (os.POSIX_SPAWN_CLOSE, err_write),
    )
    normalize_signals()
    payload_deadline = time.monotonic_ns() + PAYLOAD_DEADLINE_NS
    pid = os.posix_spawn(
        ENV_TOOL,
        strict.payload_argv,
        {},
        file_actions=actions,
        setsigmask=(),
        setsigdef=SIGNAL_DEFAULTS,
    )
    state["payload_spawned"] = 1
    if not capture_guard(
        state,
        payload_deadline,
        "payload_deadline_fired",
        "payload-spawn",
    ):
        mark_capture_error(state, "payload-spawn-late")
    return pid, payload_deadline

def payload_topology(pid, supervisor_group, state, payload_deadline):
    if not capture_guard(state, payload_deadline, "payload_deadline_fired", "payload-topology"):
        return False
    try:
        pgid = os.getpgid(pid)
    except BaseException:
        capture_guard(state, payload_deadline, "payload_deadline_fired", "payload-topology")
        mark_capture_error(state, "payload-pgid")
        return False
    if not capture_guard(state, payload_deadline, "payload_deadline_fired", "payload-topology"):
        return False
    try:
        sid = os.getsid(pid)
    except BaseException:
        capture_guard(state, payload_deadline, "payload_deadline_fired", "payload-topology")
        mark_capture_error(state, "payload-sid")
        return False
    timely = capture_guard(state, payload_deadline, "payload_deadline_fired", "payload-topology")
    good = timely and pid > 1 and pgid == supervisor_group and sid == supervisor_group
    if not good:
        mark_capture_error(state, "payload-topology")
    return good

def payload_writer_close(state, fd, payload_deadline):
    before = capture_guard(
        state,
        payload_deadline,
        "payload_deadline_fired",
        "payload-writer-close",
    )
    closed = close_fd(fd, "payload-writer-close")
    after = capture_guard(
        state,
        payload_deadline,
        "payload_deadline_fired",
        "payload-writer-close",
    )
    if not before or not after or not closed:
        mark_capture_error(state, "payload-writer-close")
        return False
    return True

def governed_payload_abort(state, pid, payload_deadline, owned_fds, code):
    mark_capture_error(state, code)
    if payload_deadline is not None and state["child_reaped"] == 0:
        capture_wait_once(
            pid,
            state,
            payload_deadline,
            "payload_deadline_fired",
            "payload-wait",
            "payload_wait_observed",
            "payload_wait_timely",
        )
    if state["child_reaped"] == 0:
        state["capture_state"] = "KILL_REAP"
        kill_reap_deadline = time.monotonic_ns() + KILL_REAP_GRACE_NS
        state["kill_sent"] = 1
        try:
            os.kill(pid, signal.SIGKILL)
        except OSError as error:
            if error.errno != errno.ESRCH:
                mark_capture_error(state, "payload-kill")
        except BaseException:
            mark_capture_error(state, "payload-kill-unexpected")
        reaped, timely, status_value = wait_deadline(pid, kill_reap_deadline)
        if reaped:
            state["child_reaped"] = 1
            state["kill_reap_wait_observed"] = 1
            state["kill_reap_wait_timely"] = int(timely)
            state["wait_raw"] = status_value
        if not timely:
            state["kill_reap_deadline_fired"] = 1
            state["timeout"] = 1
    for fd, site in owned_fds:
        if fd is not None:
            close_fd(fd, site)
    state["capture_state"] = "UNSAFE"
    state["capture_complete"] = 0
    return state, False

def finalize_watchdog(strict, state, safe, forced_error):
    if forced_error != "none":
        mark_capture_error(state, forced_error)
    if not safe:
        if strict is not None:
            strict.close()
        close_all()
        close_owned(0, "stdin-close")
        close_owned(2, "stderr-close")
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)
    pass_seen = (
        state["capture_complete"] == 1
        and state["capture_state"] == "COMPLETE"
        and state["payload_deadline_fired"] == 0
        and state["kill_reap_deadline_fired"] == 0
        and state["stream_eof_deadline_fired"] == 0
        and state["payload_wait_observed"] == 1
        and state["payload_wait_timely"] == 1
        and state["stdout_eof_observed"] == 1
        and state["stdout_eof_timely"] == 1
        and state["stderr_eof_observed"] == 1
        and state["stderr_eof_timely"] == 1
        and state["child_reaped"] == 1
        and state["kill_sent"] == 0
        and state["out_eof"] == 1
        and state["err_eof"] == 1
        and state["out_overflow"] == 0
        and state["err_overflow"] == 0
        and state["out_close_error"] == 0
        and state["err_close_error"] == 0
        and bytes(state["out"]) == PASS_LINE
        and state["out_total"] == 308
        and state["out_lf"] == 1
        and state["out_hash"].hexdigest() == PASS_SHA256
        and state["err_total"] == 0
        and state["err_lf"] == 0
        and state["err_hash"].hexdigest() == EMPTY_SHA256
    )
    success = (
        pass_seen
        and state["payload_spawned"] == 1
        and state["capture_complete"] == 1
        and state["wait_kind"] == "exit"
        and state["exit_code"] == 0
        and state["timeout"] == 0
        and state["supervisor_lost"] == 0
        and state["capture_error"] == "none"
        and not CLOSE_FAILED
    )
    try:
        strict.verify()
    except BaseException:
        success = False
        mark_capture_error(state, "input-drift")
    binding = strict.control.binding
    strict.close()
    if CLOSE_FAILED:
        success = False
        mark_capture_error(state, "strict-close")
    if 10 in OPEN_FDS:
        closed_life = close_fd(10, "life-close")
        state["life_close_error"] |= int(not closed_life)
    if state["life_close_error"]:
        success = False
        mark_capture_error(state, "life-close")
    meta = None
    if not success:
        meta = new_audit_schema("watchdog")
        failure_inputs = None
        try:
            failure_inputs = FailureBinderInputs(binding, meta)
        except BaseException:
            failure_inputs = UnavailableBinderInputs(meta, "binder-input-construction")
        try:
            meta = binder_observe(failure_inputs, meta, False, pass_seen, True)
        except BaseException:
            schema_error(meta, "binder-observe")
            try:
                failure_inputs.verify_after()
            except BaseException:
                schema_error(meta, "input-terminal-drift")
            try:
                failure_inputs.close()
            except BaseException:
                schema_error(meta, "input-close-unexpected")
            close_all()
            try:
                derive_schema(meta, False, pass_seen)
            except BaseException:
                schema_error(meta, "schema-derive")
    else:
        close_all()
    close_owned(0, "stdin-close")
    close_owned(2, "stderr-close")
    if CLOSE_FAILED:
        success = False
        mark_capture_error(state, "internal-close")
        if meta is None:
            meta = new_audit_schema("watchdog")
        schema_error(meta, "pre-emission-close")
    if success:
        binder = b""
        binder_status = "not-run"
        phase = "not-applicable"
        disposition = "SUCCESS"
    else:
        binder, binder_status, phase = render_binder(meta, False)
        disposition = "PERMANENT_FAILURE"
    value = result_line("watchdog", state, binder, binder_status, phase, disposition)
    emit_and_exit(value, 1 if CLOSE_FAILED else 0)

def supervisor_mode(binding):
    global WATCHDOG_PID
    stdin_open = True
    runtime("supervisor", (0, 1, 2, 3, 4), binding)
    track(3)
    track(4)
    try:
        supervisor_pid = os.getpid()
        need(supervisor_pid == os.getsid(0) == os.getpgrp(), "supervisor-session-self")
        release = read_token_eof(
            4,
            b"L",
            time.monotonic_ns() + LAUNCH_RELEASE_DEADLINE_NS,
            "launch-release",
        )
        need(release == b"L", "launch-release-byte")
        close_fd(4, "launch-close")
        need(not CLOSE_FAILED, "launch-release-close")
        preflight = StrictPreflight(binding)
        preflight.verify()
        preflight.close()
        need(not CLOSE_FAILED and OPEN_FDS == {3}, "supervisor-preflight-close")
        life_read, life_write = os.pipe2(os.O_CLOEXEC)
        ready_read, ready_write = os.pipe2(os.O_CLOEXEC)
        for fd in (life_read, life_write, ready_read, ready_write):
            track(fd)
        need(
            len({life_read, life_write, ready_read, ready_write, 0, 1, 2, 3, 10, 11}) == 10,
            "supervisor-fd-collision",
        )
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
        ) + binding_argv_bytes(binding) + (str(supervisor_pid).encode("ascii"),)
        actions = (
            (os.POSIX_SPAWN_DUP2, 3, 0),
            (os.POSIX_SPAWN_DUP2, life_read, 10),
            (os.POSIX_SPAWN_DUP2, ready_write, 11),
            (os.POSIX_SPAWN_CLOSE, 3),
            (os.POSIX_SPAWN_CLOSE, life_read),
            (os.POSIX_SPAWN_CLOSE, life_write),
            (os.POSIX_SPAWN_CLOSE, ready_read),
            (os.POSIX_SPAWN_CLOSE, ready_write),
        )
        normalize_signals()
        ready_deadline = time.monotonic_ns() + READY_DEADLINE_NS
        pid = os.posix_spawn(
            PYTHON,
            watchdog_argv,
            EXPECTED_ENV,
            file_actions=actions,
            setsigmask=(),
            setsigdef=SIGNAL_DEFAULTS,
        )
        WATCHDOG_PID = pid
        require_before(ready_deadline, "ready-spawn")
        need(pid > 1, "watchdog-pid")
        require_before(ready_deadline, "ready-spawn")
        close_fd(3, "stdin-close")
        require_before(ready_deadline, "ready-close")
        close_fd(life_read, "life-close")
        require_before(ready_deadline, "ready-close")
        close_fd(ready_write, "ready-close")
        require_before(ready_deadline, "ready-close")
        need(not CLOSE_FAILED, "supervisor-opposite-close")
        ready = read_token_eof(
            ready_read,
            b"R",
            ready_deadline,
            "ready",
        )
        need(ready == b"R", "ready-byte")
        require_before(ready_deadline, "ready-close")
        close_fd(ready_read, "ready-close")
        require_before(ready_deadline, "ready-close")
        need(not CLOSE_FAILED, "supervisor-ready-close")
        require_before(ready_deadline, "ready-topology")
        watchdog_sid = os.getsid(pid)
        require_before(ready_deadline, "ready-topology")
        watchdog_pgid = os.getpgid(pid)
        require_before(ready_deadline, "ready-topology")
        need(pid != supervisor_pid and watchdog_sid == supervisor_pid and watchdog_pgid == supervisor_pid, "watchdog-session")
        ack_deadline = time.monotonic_ns() + ACK_DEADLINE_NS
        require_before(ack_deadline, "ack-begin")
        begin = begin_line(pid, binding)
        require_before(ack_deadline, "ack-begin")
        write_all(1, begin)
        require_before(ack_deadline, "ack-begin")
        ack = read_token_eof(
            0,
            b"A",
            ack_deadline,
            "ack",
        )
        need(ack == b"A", "ack-byte")
        require_before(ack_deadline, "ack-close")
        close_owned(0, "ack-close")
        require_before(ack_deadline, "ack-close")
        stdin_open = False
        need(not CLOSE_FAILED, "ack-close")
        write_all(life_write, b"S")
        status_value = wait_blocking(pid)
        WATCHDOG_PID = 0
        close_fd(life_write, "life-close")
        close_all()
        good = (
            os.WIFEXITED(status_value)
            and os.WEXITSTATUS(status_value) == 0
            and not CLOSE_FAILED
        )
        close_owned(2, "stderr-close")
        close_owned(1, "stdout-close")
        good = good and not CLOSE_FAILED
        os._exit(0 if good else 1)
    except BaseException:
        close_all()
        if stdin_open:
            close_owned(0, "stdin-close")
            stdin_open = False
        if WATCHDOG_PID > 1:
            reaped, timely, status_value = wait_deadline(
                WATCHDOG_PID,
                time.monotonic_ns() + KILL_REAP_GRACE_NS,
            )
            if not reaped:
                try:
                    os.kill(WATCHDOG_PID, signal.SIGKILL)
                except OSError as error:
                    if error.errno != errno.ESRCH:
                        pass
                try:
                    reaped, timely, status_value = wait_deadline(
                        WATCHDOG_PID,
                        time.monotonic_ns() + KILL_REAP_GRACE_NS,
                    )
                except BaseException:
                    pass
            WATCHDOG_PID = 0
        close_owned(2, "stderr-close")
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)

def watchdog_mode(binding):
    runtime("watchdog", (0, 1, 2, 10, 11), binding)
    track(10)
    track(11)
    strict = None
    started = False
    state = empty_capture()
    pid = 0
    payload_deadline = None
    out_read = None
    out_write = None
    err_read = None
    err_write = None
    try:
        supervisor_group = canonical_decimal(
            sys.argv[13],
            2,
            2147483647,
            "watchdog-supervisor-pid",
        )
        need(os.getppid() == supervisor_group, "watchdog-parent")
        need(os.getsid(0) == supervisor_group, "watchdog-session-self")
        need(os.getpgrp() == supervisor_group, "watchdog-pgid-self")
        need(os.getpid() != supervisor_group, "watchdog-not-leader")
        prove_payload_input_live(0)
        strict = StrictPreflight(binding)
        strict.verify()
        write_all(11, b"R")
        close_fd(11, "ready-close")
        need(not CLOSE_FAILED, "watchdog-ready-close")
        wait_start(10)
        started = True
        strict.verify()
        if not probe_lifeline(10):
            state["supervisor_lost"] = 1
            finalize_watchdog(strict, state, True, "supervisor-lost-before-spawn")
        out_read, out_write = os.pipe2(os.O_CLOEXEC)
        err_read, err_write = os.pipe2(os.O_CLOEXEC)
        for fd in (out_read, out_write, err_read, err_write):
            track(fd)
        need(
            len({out_read, out_write, err_read, err_write, 0, 1, 2, 10}) == 8,
            "payload-fd-collision",
        )
        pid, payload_deadline = spawn_payload(
            strict,
            state,
            out_read,
            out_write,
            err_read,
            err_write,
        )
        forced_error = "none"
        if not payload_topology(pid, supervisor_group, state, payload_deadline):
            forced_error = "payload-topology"
        if not payload_writer_close(state, out_write, payload_deadline):
            forced_error = "payload-writer-close"
        out_write = None
        if not payload_writer_close(state, err_write, payload_deadline):
            forced_error = "payload-writer-close"
        err_write = None
        state, safe = capture_payload(
            state,
            pid,
            out_read,
            err_read,
            10,
            payload_deadline,
            forced_error,
        )
        out_read = None
        err_read = None
        finalize_watchdog(strict, state, safe, "none")
    except BaseException as error:
        code = error.code if isinstance(error, Stop) else "unexpected"
        if pid > 1 and state["child_reaped"] == 0:
            state, safe = governed_payload_abort(
                state,
                pid,
                payload_deadline,
                (
                    (out_read, "payload-out-close"),
                    (out_write, "payload-writer-close"),
                    (err_read, "payload-err-close"),
                    (err_write, "payload-writer-close"),
                ),
                code,
            )
            finalize_watchdog(strict, state, False, code)
        if started and strict is not None:
            finalize_watchdog(strict, state, state["payload_spawned"] == 0, code)
        if strict is not None:
            strict.close()
        close_all()
        close_owned(0, "stdin-close")
        close_owned(2, "stderr-close")
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)

def require_group_absent(pgid):
    try:
        os.killpg(pgid, 0)
    except OSError as error:
        need(error.errno == errno.ESRCH, "recovery-pgid-check")
        return
    stop("recovery-pgid-live")

def recovery_mode(binding):
    runtime("recovery-binder", (0, 1, 2), binding)
    text_pgid = sys.argv[13]
    pgid = canonical_decimal(text_pgid, 2, 2147483647, "recovery-pgid-grammar")
    need(sys.argv[14] == "consumed", "recovery-consumed-token")
    meta = new_audit_schema("recovery-binder")
    inputs = None
    binder = None
    value = None
    try:
        require_group_absent(pgid)
    except BaseException:
        close_all()
        close_owned(0, "stdin-close")
        close_owned(2, "stderr-close")
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)
    meta["recovery_first_esrch"] = "1"
    try:
        inputs = FailureBinderInputs(binding, meta)
    except BaseException:
        inputs = UnavailableBinderInputs(meta, "binder-input-construction")
    evidence_allowed = False
    try:
        require_group_absent(pgid)
        meta["recovery_second_esrch"] = "1"
        evidence_allowed = True
    except BaseException:
        meta["recovery_second_esrch"] = "0"
        schema_error(meta, "recovery-second-esrch")
    try:
        meta = binder_observe(inputs, meta, True, False, evidence_allowed)
    except BaseException:
        schema_error(meta, "binder-observe")
        try:
            inputs.verify_after()
        except BaseException:
            schema_error(meta, "input-terminal-drift")
        try:
            inputs.close()
        except BaseException:
            schema_error(meta, "input-close-unexpected")
        close_all()
        try:
            derive_schema(meta, True, False)
        except BaseException:
            schema_error(meta, "schema-derive")
    close_owned(0, "stdin-close")
    close_owned(2, "stderr-close")
    meta["recovery_third_esrch"] = "1"
    binder, binder_status, phase = render_binder(meta, True)
    state = recovery_capture(pgid)
    state["recovery_esrch_initial"] = meta["recovery_first_esrch"]
    state["recovery_esrch_pre_evidence"] = meta["recovery_second_esrch"]
    state["recovery_esrch_terminal"] = meta["recovery_third_esrch"]
    if meta["post_inputs_reverified"] != 1:
        state["capture_error"] = "input-terminal-drift"
    value = result_line(
        "recovery-binder",
        state,
        binder,
        binder_status,
        "unknown-mismatch",
        "PERMANENT_FAILURE",
    )
    if not (
        meta["recovery_first_esrch"] == "1"
        and meta["recovery_second_esrch"] == "1"
        and meta["recovery_third_esrch"] == "1"
    ):
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)
    require_group_absent(pgid)
    emit_and_exit(value, 1 if CLOSE_FAILED else 0)

try:
    normalize_signals()
    need(len(sys.argv) >= 2, "mode-argv")
    if sys.argv[1] in ("supervisor", "watchdog"):
        binding = Binding(sys.argv[2:13])
        if sys.argv[1] == "supervisor":
            supervisor_mode(binding)
        else:
            watchdog_mode(binding)
    elif sys.argv[1] == "recovery-binder":
        binding = Binding(sys.argv[2:13])
        recovery_mode(binding)
    else:
        stop("mode")
except BaseException:
    close_all()
    os._exit(1)
BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V4_PROGRAM_END

## 4. Canonical transports and external actor

The launch-release, ready, ACK, and start tokens are exact one-byte L, R, A,
and S.  Launch release, ready, and ACK must each be followed by EOF.  Every
token deadline is sticky and tested before and immediately after poll, read,
and any governed write; an event observed at or after its deadline is loss
even if it may have been queued earlier.  Ready uses the one deadline frozen
before watchdog spawn.  ACK uses the one deadline frozen before BEGIN
construction.  The start/lifeline writer remains open until watchdog reap.

The later actor must itself be frozen and independently reviewed.  It creates
five independent binary pipes, normalizes its signals and FD set, and invokes
os.posix_spawn for the supervisor with setsid=True.  The returned direct PID P
is the containment identity.  Before releasing fd4 the actor proves
getsid(P)=P and getpgid(P)=P, durably appends and rebinds a launch record with
attempt_consumed=0, writes exact L, and closes the release writer.  Thus actor
knowledge of P happens before the supervisor may create a descendant.

The supervisor verifies pid=sid=pgid=P at entry.  It passes canonical P as the
watchdog-only argv tail, spawns the watchdog without setsid or setpgroup, and
accepts R only after the watchdog has proved ppid=sid=pgid=P.  The payload is
also spawned without a session/group action and is checked in group P.  BEGIN
reports supervisor_pid=P, session_sid=P, session_pgid=P, watchdog_pgid=P and
the direct watchdog PID.

BEGIN then emits the eleven actor-passed Binding fields contiguously in this
fixed order: self_dev, self_ino, self_bytes, self_LF, self_sha256, ledger_dev,
ledger_ino, ledger_prefix_bytes, ledger_prefix_LF, ledger_prefix_sha256 and
ledger_prefix_terminal_hex.  The terminal is the exact canonical lowercase
hex argv field.  BEGIN_CAP is 4096.  The actor compares all eleven texts
byte-for-byte with its frozen launch tuple before any ACK write.

After canonical BEGIN, the actor durably appends the pending attempt with P,
the watchdog PID, every Binding value and attempt_consumed=0; fsyncs the ledger
and parent; and freshly rebinds the complete ledger before writing A and
closing ACK.  Any ambiguity after the first A write is permanently possibly
consumed.  Payload stdin is independent, stays unwritten, and its writer is
retained through containment.

The capture transition graph is one-way: PAYLOAD_WAIT goes only to STREAM_EOF
or KILL_REAP; KILL_REAP goes only to STREAM_EOF or UNSAFE; STREAM_EOF goes only
to COMPLETE or UNSAFE.  Each loop offers WNOHANG wait before handling at most
one bounded chunk from each ready stream.  PAYLOAD_WAIT, KILL_REAP and
STREAM_EOF each have one immutable absolute guard.  Every waitpid, poll,
stdout read, stderr read and lifeline read checks its current guard before the
syscall and immediately after it, latching equality as late before examining
status, events, data or EOF.  A kill path freezes a fresh kill/reap guard
immediately before its sole SIGKILL attempt and continues WNOHANG reap under
that guard even though the payload guard already fired.  A physically late
reap prevents any later signal but is failure evidence, never authority.

The actor owns a monotone 420-second overall deadline.  Any deadline or other
loss sets an irreversible loss latch before later bytes are examined.  It
closes its launch, ACK and payload-stdin writers, sends SIGKILL to negative P
with only ESRCH accepted as an alternative, reaps direct P, repeats the
negative-P probe until killpg(P,0) returns ESRCH, and invokes recovery exactly
once only if S may have been consumed.  The supervisor never signals negative
P because that is its own group; its local exception cleanup may wait for and
SIGKILL only the direct watchdog PID before exiting nonzero.

A direct RESULT is provisional.  Physical success is exactly the conjunction
of: actor deadline never fired; loss never latched; one canonical BEGIN and
one canonical SUCCESS RESULT; all topology and eleven Binding fields match;
pending durability preceded A; exact A plus EOF; payload stdin remained live
and unused; capture_state is COMPLETE and capture_complete is one;
payload_deadline_fired, kill_reap_deadline_fired and
stream_eof_deadline_fired are zero; payload_wait_observed and
payload_wait_timely are one; both EOF observed/timely pairs are one;
child_reaped is one and kill_sent is zero; timeout, overflow, capture,
lifeline and close bits are all zero; exact PASS and empty payload stderr
identities hold; raw supervisor stdout reaches EOF; external stderr is empty
and reaches EOF; supervisor exits zero, thereby attesting watchdog exit zero;
killpg(P,0) proves ESRCH; every control, tool, source, whole V4 and complete
current ledger reverify; and the final ledger append, file/parent fsync and
exact rebind succeed.  A killed, late or expired capture is UNSAFE, emits no
authoritative direct RESULT, and can never satisfy a later actor.  Failure of
any conjunct is loss, never success.

The containment schedule is exhaustive.  Spawn failure before P creates no
accepted child.  Before L, fd4 EOF stops P before a descendant.  After L and
before BEGIN, every possible watchdog is already in known group P.  Before an
A write, S is impossible and recovery is not used.  From the first possibly
written A byte onward, S is conservatively possible, so loss kills/proves P
and then uses one recovery.  Watchdog death, payload death, supervisor death,
partial RESULT, RESULT without EOF/status, zero supervisor status with a
residual group, and actor deadline during terminal work all fail the same
sticky conjunction.  No visible line or late zero status can reverse loss.
Before watchdog spawn failure there is no watchdog.  From returned watchdog
PID through ready topology and closes, the direct PID is known and supervisor
cleanup waits, never signals a reaped PID, and sends at most one direct-PID
SIGKILL.  From returned payload PID through topology and writer closes, every
failure enters governed payload cleanup.  The supervisor never calls killpg
on its own group; only the actor kills and proves absence of negative P.

## 5. Fixed binder, close, and recovery contract

One complete fixed audit schema is allocated before FailureBinderInputs or any
binder observation.  It always contains scalar slots for source initial and
terminal, evidence initial and terminal, three inventories, twelve candidates,
three relation sets, per-snapshot anomalies, cross-snapshot and union summaries,
five bracket-completion flags, three recovery ESRCH proofs, post-input
revalidation, provenance and end.  Inputs, parents, evidence records, binder
bytes and RESULT bytes are optional locals; the caller-owned meta object is
never replaced or discarded.  Exceptions fill preallocated unavailable/error
slots and later attempts and finalizers continue.  Serialization occurs only
after snapshot, evidence, parent, source and control closes, terminal
verification, input close and the final tracked-FD close sweep have all
contributed to the monotone CLOSE_FAILED latch.

Every source and candidate observation performs an initial no-follow stat and
a fresh final no-follow stat in all branches, including ENOENT, non-ENOENT
error, nonregular, over-cap, path-open error, read-open error and complete
read.  Evidence uses nonthrowing begin_evidence and finish_evidence.  Begin
retains explicit O_PATH and directory FDs, initial scalars, exact zero and a
zero finalized flag.  Finish checks both retained identities, then attempts a
fresh parent-relative no-follow pathname stat and only afterward sets the
finalized flag and derives exact.  Held FDs close before rendering, while all
scalar initial/final states remain.  Stable absence means exact ENOENT at both
stats with no error.  Stable presence means exact node-key equality at both
stats.  No other state is stable or exact.

The evidence bracket order is fixed: initial parent and begin; separately
guarded snapshots one and two; finish initial evidence; fresh terminal parent
and begin; separately guarded snapshot three; finish terminal evidence; close
all snapshots, evidence records and parents; terminal control and source
verification; input close; final close sweep; then derive, classify and
render.  A snapshot exception leaves its preallocated slot unavailable,
records an error, sets only its attempt-complete flag, and cannot suppress a
later snapshot or either evidence finalizer.  Close failure latches but cannot
suppress another close or finalizer.

Every inventory fresh-opens dot relative to the held evidence directory.
Its fixed-order monotone reason_bits are evidence-unavailable, open-error,
identity-open, name-invalid, item-cap, raw-cap, scan-error, duplicate,
frame-cap, identity-final, iterator-close, fd-close and unexpected, plus a
truncation bit.  Later observations cannot erase an earlier bit.  Any bit or
truncation makes the inventory incomplete and the phase unknown-mismatch.

A named durability phase is possible only when all three full snapshot
signatures are identical, both source records match and are exact, both
evidence records match and are exact, all inventories are complete, terminal
input revalidation passed, all three snapshot-attempt flags and both
evidence-finalized-after-bracket flags are one, CLOSE_FAILED is zero, every one of twelve candidate
records is either exact stable double-ENOENT absence or exact stable regular
complete presence, each inventory names tuple exactly equals its sorted
present-candidate tuple, and no unknown child, duplicate, source alias or
anomaly exists.  Every unavailable, error, malformed, capped, nonregular or
unstable record forces unknown-mismatch.

Evidence equality itself requires both finalized flags.  The fixed report renders both source records, both evidence records, all three
complete inventory frames, every unknown child, all twelve candidate records,
relations, duplicates, aliases and anomalies tagged by snapshot, cross and
union summaries, revalidation, provenance and BINDER_END.  Later snapshots
never collapse into a generic drift token.

BINDER_CAP is 524288 and the mechanically allocated full-schema worst case is
516096 bytes: 201600 for three inventory records with full frame hex, 120000
for bounded unknown-child sections, 132000 for anomaly sections, 20480 for
sixteen source/evidence/candidate scalar records, and 42016 for headers,
attempt/finalizer/proof fields, relations, cross/union summaries, revalidation,
provenance and end.  RESULT_CAP is 1310720 and the full RESULT worst case is
1263616 bytes: 1032192 for hex of the maximum binder, 139264 for captured
stdout/stderr hex, and 92160 for capture state, deadline, wait, EOF, proof,
identity, decimal, hash and framing fields.  Both derived bounds are below
their caps.  Full schema shape is validated before serialization.  Malformed
bounded fields are sanitized in place in the same caller-owned meta and the
same full layout is retried exactly once after a primary serializer failure.
Only a mechanically impossible size violation may emit a small record clearly
tagged schema-layout=overflow with observed byte count and SHA-256; it forces
PERMANENT_FAILURE and never truncates or masquerades as a full report.

Recovery allocates meta before FailureBinderInputs.  Its first ESRCH proof
precedes every input and evidence open; failure closes transport and emits
nothing.  After guarded partial input construction it makes and records a
second ESRCH proof immediately before any evidence Chain.  It then follows the
same observation, verification, close, derive and full-layout rendering path,
even for ordinary unavailable or construction failures.  The candidate report
contains a conditional third-proof value of one, but no byte is written unless
a fresh third ESRCH succeeds immediately before emit; failure discards the
candidate.  Thus every visible recovery report truthfully has all three proofs
equal to one.  Recovery retains unavailable wait/stream/capture provenance and
can emit only PERMANENT_FAILURE with unknown-mismatch.  It never authorizes a
retry or consumes new attempt authority.

## 6. Mechanically derived no-build fixture specification

No fixture or microtest is authorized here.  A later control may derive a
fixture only from the exact normalized V4 program by ordered unique-anchor
replacement.  Each record is class, identifier, old hex, new hex, old offset,
old SHA-256 and new SHA-256.  The only classes remain fixture labels and
self/status names; isolated non-build workspace/input/tool identities; complete
payload, launcher, PASS and identity stubs; timeout/cap decimals; and
actor-passed fixture whole-self and ledger tuples.

Replacing every changed span by its class/identifier token must give the same
production and fixture skeleton SHA-256.  No function or control-flow byte may
differ.  Production contains no test branch, environment switch, monkeypatch,
fault hook, production build/evidence fixture literal or second payload path.
No test may claim equivalence beyond its exact reviewed branch map.

## 7. Remaining host premises and author stop

Activation still trusts the frozen CPython 3.12 and libc posix_spawn/file-
action and setsid implementation, the host-wide 1048576 FD ceiling, timely
SIGKILL and reap outside uninterruptible kernel sleep, no adversarial PID/PGID
reuse over the checked interval, the statically proved direct exec chain with
no process-group escape, root CAP_FOWNER for O_NOATIME, filesystem fsync
durability, and pathname/tool immutability during declared single-writer
intervals.

This author stop creates no actor, E001, recovery-binder, fixture, host-probe,
microtest, E010, A000, stage, root, PDF, release or Paper28 execution authority.

BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V4_AUTHOR_STOP
