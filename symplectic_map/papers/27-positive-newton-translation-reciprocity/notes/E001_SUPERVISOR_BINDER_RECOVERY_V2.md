# E001 posix-spawn supervisor and failure binder V2

## 1. Authority, precedence, and inertness

This append-only V2 control is the sole notes artifact authorized by
B07-E0317-P27-PROBE-RECOVERY-E001-SUPERVISOR-BINDER-STATIC-REVIEW-
FAILURE-AND-V2-CONTROL-AUTHORIZATION.  Its authoring input is the exact
E0317 physical ledger:

- bytes 1696061;
- LF 19585;
- SHA-256
  5fa5d1417c5e2bc8b0cf417161f8b23e771c5323043ac21ea585094fe3b0f5ea;
- terminal
  BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_STATIC_REVIEW_FAILURE_RECORDED_AND_V2_CONTROL_AUTHORIZED.

The failed V1 control remains byte-immutable at 75678 bytes, 2053 LF and
SHA-256 e93dabf09038b9112ab4fa2912f03d34407f1598962abe934d18cc1b85bbb3f4.
This file supersedes only its failed lifecycle, binder, close, inventory,
binding, recovery-provenance, and test-equivalence design.  The frozen
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

## 2. V2 trust boundary and lifecycle

The executable marker bytes bind themselves through CODE_BYTES.  They do
not claim to self-certify this whole Markdown file.  A separately frozen
later actor supplies canonical whole-V2 and appendable-ledger-prefix identity
tuples after V2 author stop and ledger binding.  Every mode checks those
tuples, the marker transport, and the E0317 minimum ledger anchor.  The later
actor independently checks the whole control and complete current ledger.
This is the noncircular whole-control trust boundary.

The actor supplies separate live binary pipes: supervisor fd0 is ACK input,
fd1 is stdout, fd2 is stderr, and fd3 is payload stdin.  It durably appends
and rebinds a pending event before writing exact A and closing ACK.  It never
writes payload stdin and retains that pipe writer until containment is
complete.  The watchdog maps fd3 to its fd0.  Exact A followed by EOF is
required; extra data, live ACK after A, or premature EOF fails.

There is no normal supervisor watchdog-completion deadline and no grace
that can return to success.  Ready is bounded by 30 seconds, ACK by 300
seconds, the payload by 30 seconds, kill/reap cleanup by 5 seconds, and
post-reap stream EOF by 1 second.  The later actor owns a sticky 420-second
overall deadline and a separate 60-second recovery deadline.  Once any
deadline fires, success is impossible.

The direct-report order is R plus EOF, BEGIN, durable pending ledger event,
A plus EOF, S, payload wait and stream EOF, terminal verification or binder,
watchdog RESULT write and fd1 close, watchdog exit, supervisor waitpid,
supervisor fd closes and exit, actor EOF/status acceptance, process-group
absence, and final ledger result append.  A visible RESULT is provisional
until stdout EOF, empty stderr EOF, watchdog status as attested by supervisor
zero exit, and supervisor zero exit all hold.

All modes normalize and verify every catchable signal disposition and the
empty mask before governed work.  They scan the complete frozen descriptor
domain 0 through 1048575 twice.  The watchdog receives the deterministic
ten-key environment, not an empty mapping.  Activation remains conditional
on a separately frozen no-build host probe proving that 1048576 is the
maximum possible live-fd boundary and reproducing the exact signal and
CPython/libc environment behavior.

## 3. Exact literal V2 program

The normalized program is the byte substring after the BEGIN marker LF and
before the LF immediately preceding the END marker.  The delimiter LF is not
passed to Python.  At author stop its raw and normalized identities are:

- raw bytes 89799, LF 2572, SHA-256
  dde0a5d2b4a51fc6e750af4cd5ab890e590e764ea3ca21ee9357cbed7cf70108;
- normalized bytes 89798, LF 2571, physical lines 2572, final byte 41,
  SHA-256 12205ffbcd39981d5840e940eefb7868d1a6e08836c3733470595ccfb707cc9c;
- normalized single-quote, dollar, and backtick census 0/0/0.

BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V2_PROGRAM_BEGIN
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
SELF_NAME = b"E001_SUPERVISOR_BINDER_RECOVERY_V2.md"
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
E0317_BYTES = 1696061
E0317_LF = 19585
E0317_SHA256 = "5fa5d1417c5e2bc8b0cf417161f8b23e771c5323043ac21ea585094fe3b0f5ea"
E0317_TERMINAL = (
    b"BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_STATIC_REVIEW_"
    b"FAILURE_RECORDED_AND_V2_CONTROL_AUTHORIZED\n"
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
BINDER_CAP = 262144
RESULT_CAP = 786432
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
WATCHDOG_PID = 0
CLOSE_SITE_TOKENS = (
    "ack-close",
    "candidate-close",
    "chain-close",
    "cleanup-close",
    "evidence-close",
    "fresh-close",
    "inventory-fd-close",
    "inventory-iterator-close",
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
        self.ledger_bytes = canonical_decimal(values[7], E0317_BYTES, 16777216, "binding-ledger-bytes")
        self.ledger_lf = canonical_decimal(values[8], E0317_LF, 200000, "binding-ledger-lf")
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
        need(len(sys.argv) == 13 and sys.argv[0] == "-c" and sys.argv[1] == mode, "argv")
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
        b"V2_AUTHOR_STOP\n"
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
        b"BINDER_V2_PROGRAM_BEGIN\n"
    )
    end = (
        b"BATCH07_P27_RECOVERY_E001_SUPERVISOR_"
        b"BINDER_V2_PROGRAM_END\n"
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
        self.launcher = extract_launcher(self.data[:E0317_BYTES])

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
        anchor = data[:E0317_BYTES]
        need(
            anchor.count(b"\n") == E0317_LF
            and sha(anchor) == E0317_SHA256
            and anchor.endswith(E0317_TERMINAL),
            "ledger-E0317-anchor",
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
        "stable": 0,
        "error": "none",
        "key": None,
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

def close_observation(record):
    for fd in reversed(record["fds"]):
        close_fd(fd, "candidate-close")
    record["fds"] = []

def observe_source(notes):
    record = empty_observation(SOURCE_NAME)
    try:
        before = os.stat(SOURCE_NAME, dir_fd=notes.leaf(), follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            record["state"] = "absent"
            record["absence"] = "ENOENT"
            record["content"] = "absent"
            return record
        record["state"] = "error"
        record["error"] = "source-lstat"
        return record
    fill_metadata(record, before)
    try:
        path_fd = track(os.open(SOURCE_NAME, PATH_FLAGS, dir_fd=notes.leaf()))
        record["fds"].append(path_fd)
        if node_key(os.fstat(path_fd)) != node_key(before):
            record["error"] = "source-path-race"
            return record
    except BaseException:
        record["error"] = "source-path-open"
        return record
    if not stat.S_ISREG(before.st_mode):
        record["content"] = "unavailable-nonregular"
        record["stable"] = 1
        return record
    record["bytes"] = str(before.st_size)
    if before.st_size > SOURCE_OBSERVE_CAP:
        record["content"] = "unavailable-size-cap"
        record["stable"] = 1
        return record
    try:
        read_fd = track(os.open(SOURCE_NAME, READ_FLAGS, dir_fd=notes.leaf()))
        record["fds"].append(read_fd)
        opened = os.fstat(read_fd)
        if node_key(opened) != node_key(before):
            record["error"] = "source-read-race"
            return record
        data = pread_complete(read_fd, before.st_size)
        record["bytes"] = str(len(data))
        record["lf"] = str(data.count(b"\n"))
        record["sha"] = sha(data)
        record["terminal"] = int(data.endswith(SOURCE_TERMINAL))
        record["content"] = "complete"
        final_fd = os.fstat(read_fd)
        final_path = os.stat(SOURCE_NAME, dir_fd=notes.leaf(), follow_symlinks=False)
        record["stable"] = int(node_key(final_fd) == node_key(before) and node_key(final_path) == node_key(before))
    except BaseException:
        record["error"] = "source-read"
        record["content"] = "read-error"
        record["stable"] = 0
    record["exact"] = int(
        record["stable"] == 1
        and stat.S_ISREG(before.st_mode)
        and before.st_dev == SOURCE_DEV
        and before.st_ino == SOURCE_INO
        and stat.S_IMODE(before.st_mode) == 0o644
        and before.st_nlink == 1
        and before.st_uid == 0
        and before.st_gid == 0
        and before.st_rdev == 0
        and record["bytes"] == str(SOURCE_BYTES)
        and record["lf"] == str(SOURCE_LF)
        and record["sha"] == SOURCE_SHA256
        and record["terminal"] == 1
        and record["error"] == "none"
    )
    return record

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
        record["stable"],
        record["error"],
        record["key"],
    )

def source_line(record):
    return (
        "SOURCE state="
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
        + " error="
        + record["error"]
        + "\n"
    ).encode("ascii")

class FailureBinderInputs:
    def __init__(self, binding):
        self.control = ControlInputs(binding)
        self.source = observe_source(self.control.notes)
        self.initial_source_signature = observation_signature(self.source)
        self.post_inputs_reverified = 0
        self.verify_error = "none"

    def verify_after(self):
        fresh_source = None
        try:
            control_good = self.control.verify_complete()
            fresh_source = observe_source(self.control.notes)
            source_good = observation_signature(fresh_source) == self.initial_source_signature
            self.post_inputs_reverified = int(control_good and source_good)
            if self.post_inputs_reverified != 1:
                self.verify_error = "input-terminal-drift"
        except BaseException:
            self.post_inputs_reverified = 0
            self.verify_error = "input-terminal-drift"
        finally:
            if fresh_source is not None:
                close_observation(fresh_source)
        if CLOSE_FAILED:
            self.post_inputs_reverified = 0
            self.verify_error = "input-close"
        return self.post_inputs_reverified == 1

    def close(self):
        close_observation(self.source)
        self.control.close()
        return CLOSE_FAILED == 0

def inventory_fresh(anchor_fd, expected_key):
    result = {
        "names": (),
        "frame": b"",
        "complete": 1,
        "stop_reason": "none",
        "overflow_bytes": "none",
        "overflow_sha": "none",
    }
    raw = []
    raw_bytes = 0
    scan_fd = None
    iterator = None
    try:
        scan_fd = track(os.open(b".", DIR_FLAGS, dir_fd=anchor_fd))
        if dir_key(os.fstat(scan_fd)) != expected_key:
            result["complete"] = 0
            result["stop_reason"] = "identity"
            return result
        iterator = os.scandir(scan_fd)
        try:
            for entry in iterator:
                item = os.fsencode(entry.name)
                roundtrip = os.fsdecode(item).encode(sys.getfilesystemencoding(), "surrogateescape")
                if roundtrip != item or item in (b".", b"..") or b"/" in item or b"\x00" in item:
                    result["complete"] = 0
                    result["stop_reason"] = "name-invalid"
                    result["overflow_bytes"] = str(len(item))
                    result["overflow_sha"] = sha(item)
                    break
                if len(raw) >= INVENTORY_ITEMS_CAP:
                    result["complete"] = 0
                    result["stop_reason"] = "item-cap"
                    result["overflow_bytes"] = str(len(item))
                    result["overflow_sha"] = sha(item)
                    break
                if raw_bytes + len(item) > INVENTORY_RAW_CAP:
                    result["complete"] = 0
                    result["stop_reason"] = "raw-cap"
                    result["overflow_bytes"] = str(len(item))
                    result["overflow_sha"] = sha(item)
                    break
                raw.append(item)
                raw_bytes += len(item)
        except BaseException:
            result["complete"] = 0
            result["stop_reason"] = "scan-error"
        raw.sort()
        if len(raw) != len(set(raw)):
            result["complete"] = 0
            result["stop_reason"] = "duplicate"
        frame = b"".join(
            str(len(item)).encode("ascii") + b":" + item.hex().encode("ascii") + b"\n"
            for item in raw
        )
        if len(frame) > BINDER_CAP:
            result["complete"] = 0
            result["stop_reason"] = "frame-cap"
            frame = frame[:BINDER_CAP]
        result["names"] = tuple(raw)
        result["frame"] = frame
        if dir_key(os.fstat(scan_fd)) != expected_key:
            result["complete"] = 0
            result["stop_reason"] = "identity-drift"
    except BaseException:
        result["complete"] = 0
        result["stop_reason"] = "open-error"
    finally:
        if iterator is not None:
            try:
                iterator.close()
            except BaseException:
                note_close_failure("inventory-iterator-close")
        if scan_fd is not None:
            close_fd(scan_fd, "inventory-fd-close")
    return result

def absent_candidate(name):
    record = empty_observation(name)
    record["state"] = "absent"
    record["absence"] = "ENOENT"
    record["content"] = "absent"
    return record

def unavailable_candidate(name, reason):
    record = empty_observation(name)
    record["error"] = reason
    return record

def observe_candidate(dir_fd, evidence_dev, name):
    try:
        before = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            return absent_candidate(name)
        return unavailable_candidate(name, "candidate-lstat")
    record = empty_observation(name)
    fill_metadata(record, before)
    record["content"] = "unavailable-nonregular"
    try:
        path_fd = track(os.open(name, PATH_FLAGS, dir_fd=dir_fd))
        record["fds"].append(path_fd)
        if node_key(os.fstat(path_fd)) != node_key(before):
            record["error"] = "candidate-path-race"
            return record
    except BaseException:
        record["error"] = "candidate-path-open"
        return record
    data = None
    if stat.S_ISREG(before.st_mode):
        record["bytes"] = str(before.st_size)
        if before.st_size > CANDIDATE_CAP:
            record["content"] = "unavailable-size-cap"
            record["stable"] = 1
        else:
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
                    final_fd = os.fstat(read_fd)
                    final_path = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
                    record["stable"] = int(node_key(final_fd) == node_key(before) and node_key(final_path) == node_key(before))
            except BaseException:
                record["error"] = "candidate-read"
                record["content"] = "read-error"
                record["stable"] = 0
    else:
        record["stable"] = 1
    expected = None
    if name == COPY_NAME:
        expected = (0o500, SOURCE_BYTES, SOURCE_LF, SOURCE_SHA256)
    elif name == STATUS_RECEIPT_NAME:
        expected = (0o600, 2, 1, STATUS_RECEIPT_SHA256)
    elif name in (STDERR_RECEIPT_NAME, STDOUT_RECEIPT_NAME):
        expected = (0o600, 0, 0, EMPTY_SHA256)
    if expected is not None and data is not None:
        expected_mode, expected_size, expected_lf, expected_sha = expected
        record["exact"] = int(
            record["stable"] == 1
            and record["error"] == "none"
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
            and (name != STATUS_RECEIPT_NAME or data == b"0\n")
        )
    return record

def candidate_signature(record):
    return observation_signature(record)

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
        + " stable="
        + str(record["stable"])
        + " exact_expected="
        + str(record["exact"])
        + " error="
        + record["error"]
        + "\n"
    ).encode("ascii")

def take_snapshot(evidence_fd, evidence_key, evidence_dev):
    inventory = inventory_fresh(evidence_fd, evidence_key)
    records = [observe_candidate(evidence_fd, evidence_dev, name) for name in CANDIDATE_NAMES]
    return {
        "inventory": inventory,
        "records": records,
    }

def close_snapshot(snapshot):
    for record in snapshot["records"]:
        close_observation(record)

def snapshot_signature(snapshot):
    inventory = snapshot["inventory"]
    return (
        inventory["names"],
        inventory["frame"],
        inventory["complete"],
        inventory["stop_reason"],
        inventory["overflow_bytes"],
        inventory["overflow_sha"],
        tuple(candidate_signature(record) for record in snapshot["records"]),
    )

def open_evidence(parent):
    record = empty_observation(EVIDENCE_NAME)
    record["dir_fd"] = None
    record["dir_key"] = None
    try:
        before = os.stat(EVIDENCE_NAME, dir_fd=parent.leaf(), follow_symlinks=False)
    except OSError as error:
        if error.errno == errno.ENOENT:
            record["state"] = "absent"
            record["absence"] = "ENOENT"
            record["content"] = "absent"
            return record
        record["state"] = "error"
        record["error"] = "evidence-lstat"
        return record
    fill_metadata(record, before)
    record["content"] = "metadata-only"
    try:
        path_fd = track(os.open(EVIDENCE_NAME, PATH_FLAGS, dir_fd=parent.leaf()))
        record["fds"].append(path_fd)
        if node_key(os.fstat(path_fd)) != node_key(before):
            record["error"] = "evidence-path-race"
            return record
    except BaseException:
        record["error"] = "evidence-path-open"
        return record
    if stat.S_ISDIR(before.st_mode):
        try:
            directory_fd = track(os.open(EVIDENCE_NAME, DIR_FLAGS, dir_fd=parent.leaf()))
            record["fds"].append(directory_fd)
            opened = os.fstat(directory_fd)
            if node_key(opened) != node_key(before):
                record["error"] = "evidence-directory-race"
            else:
                record["dir_fd"] = directory_fd
                record["dir_key"] = dir_key(opened)
                final_path = os.stat(EVIDENCE_NAME, dir_fd=parent.leaf(), follow_symlinks=False)
                record["stable"] = int(node_key(final_path) == node_key(before))
                record["content"] = "directory-observed"
        except BaseException:
            record["error"] = "evidence-directory-open"
    else:
        record["content"] = "unavailable-nondirectory"
        record["stable"] = 1
    record["exact"] = int(
        record["stable"] == 1
        and record["error"] == "none"
        and stat.S_ISDIR(before.st_mode)
        and before.st_dev == EVIDENCE_DEV
        and before.st_ino == EVIDENCE_INO
        and stat.S_IMODE(before.st_mode) == 0o700
        and before.st_nlink == 2
        and before.st_uid == 0
        and before.st_gid == 0
        and before.st_rdev == 0
    )
    return record

def close_evidence(record):
    for fd in reversed(record["fds"]):
        close_fd(fd, "evidence-close")
    record["fds"] = []
    record["dir_fd"] = None

def evidence_signature(record):
    return observation_signature(record)

def evidence_line(record):
    return (
        "EVIDENCE state="
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
        + " content_state="
        + record["content"]
        + " stable="
        + str(record["stable"])
        + " exact_expected="
        + str(record["exact"])
        + " error="
        + record["error"]
        + "\n"
    ).encode("ascii")

def inventory_line(index, inventory):
    return (
        "INVENTORY snapshot="
        + str(index)
        + " items="
        + str(len(inventory["names"]))
        + " complete="
        + str(inventory["complete"])
        + " stop_reason="
        + inventory["stop_reason"]
        + " framing_kind="
        + ("full" if inventory["complete"] == 1 else "capped-prefix")
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

def unavailable_snapshot(reason):
    return {
        "inventory": {
            "names": (),
            "frame": b"",
            "complete": 0,
            "stop_reason": reason,
            "overflow_bytes": "none",
            "overflow_sha": "none",
        },
        "records": [unavailable_candidate(name, reason) for name in CANDIDATE_NAMES],
    }

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
    return duplicate_pairs, source_aliases

def classify_phase(
    records,
    names,
    recovery,
    pass_seen,
    source_exact,
    evidence_exact,
    inventories_complete,
    snapshots_stable,
    unknown_names,
    duplicate_pairs,
    source_aliases,
):
    if recovery or source_exact != 1 or evidence_exact != 1:
        return "unknown-mismatch"
    if inventories_complete != 1 or snapshots_stable != 1:
        return "unknown-mismatch"
    if unknown_names or duplicate_pairs or source_aliases:
        return "unknown-mismatch"
    mapping = {record["name"]: record for record in records}
    order = (STDOUT_RECEIPT_NAME, STDERR_RECEIPT_NAME, COPY_NAME, STATUS_RECEIPT_NAME)
    present = tuple(name for name in order if mapping[name]["state"] == "present")
    if any(mapping[name]["exact"] != 1 for name in present):
        return "unknown-mismatch"
    if any(
        record["state"] == "present"
        and (record["type"] != "regular" or record["content"] != "complete" or record["stable"] != 1)
        for record in records
    ):
        return "unknown-mismatch"
    inventory_exact = set(names) == set(present) and len(names) == len(present)
    if not inventory_exact:
        return "unknown-mismatch"
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

def anomaly_lines(source, evidence, records, unknown_names, duplicate_pairs, source_aliases, stable):
    lines = []
    if source["state"] != "present" or source["exact"] != 1:
        lines.append(b"ANOMALY kind=source-not-exact\n")
    if source["state"] == "present" and source["nlink"] != "1":
        lines.append(("ANOMALY kind=source-nlink observed=" + source["nlink"] + "\n").encode("ascii"))
    if evidence["state"] != "present" or evidence["exact"] != 1:
        lines.append(b"ANOMALY kind=evidence-not-exact\n")
    if evidence["state"] == "present" and evidence["type"] == "directory" and evidence["nlink"] != "2":
        lines.append(("ANOMALY kind=evidence-nlink observed=" + evidence["nlink"] + "\n").encode("ascii"))
    for index, record in enumerate(records):
        if record["state"] == "present" and record["type"] == "directory":
            lines.append(("ANOMALY kind=candidate-directory candidate_index=" + str(index) + "\n").encode("ascii"))
        elif record["state"] == "present" and record["type"] != "regular":
            lines.append(("ANOMALY kind=candidate-nonregular candidate_index=" + str(index) + " type=" + record["type"] + "\n").encode("ascii"))
        if record["state"] == "present" and record["content"] == "unavailable-size-cap":
            lines.append(("ANOMALY kind=candidate-size-cap candidate_index=" + str(index) + "\n").encode("ascii"))
        if record["state"] == "present" and record["stable"] != 1:
            lines.append(("ANOMALY kind=candidate-unstable candidate_index=" + str(index) + "\n").encode("ascii"))
    for index, name in enumerate(unknown_names[:UNKNOWN_RECORD_CAP]):
        lines.append(
            (
                "UNKNOWN_CHILD index="
                + str(index)
                + " name_hex="
                + name.hex()
                + " observation=name-only opened=0\n"
            ).encode("ascii")
        )
    if len(unknown_names) > UNKNOWN_RECORD_CAP:
        lines.append(b"ANOMALY kind=unknown-record-overcap\n")
    for pair in duplicate_pairs:
        lines.append(("ANOMALY kind=candidate-duplicate pair=" + pair + "\n").encode("ascii"))
    for index in source_aliases:
        lines.append(("ANOMALY kind=source-hardlink candidate_index=" + index + "\n").encode("ascii"))
    if stable != 1:
        lines.append(b"ANOMALY kind=snapshot-drift\n")
    return lines

def empty_binder_meta(mode):
    return {
        "mode": mode,
        "body": b"INFRASTRUCTURE state=unavailable error=bounded-audit-failure\n",
        "base_status": "error",
        "proposed_phase": "unknown-mismatch",
        "inventory_complete": 0,
        "snapshots_stable": 0,
        "post_inputs_reverified": 0,
        "recovery_pre_evidence_esrch": "na",
        "error": "bounded-audit-failure",
    }

def binder_observe(inputs, recovery, pass_seen, pre_evidence):
    mode = "recovery-binder" if recovery else "watchdog"
    meta = empty_binder_meta(mode)
    parent = None
    evidence = empty_observation(EVIDENCE_NAME)
    evidence["dir_fd"] = None
    evidence["dir_key"] = None
    terminal_parent = None
    terminal_evidence = None
    first = unavailable_snapshot("evidence-unavailable")
    second = unavailable_snapshot("evidence-unavailable")
    third = unavailable_snapshot("evidence-unavailable")
    try:
        if pre_evidence is not None:
            parent = pre_evidence()
            meta["recovery_pre_evidence_esrch"] = "1"
        else:
            parent = Chain(EVIDENCE_PARENT_COMPONENTS)
        evidence = open_evidence(parent)
        if evidence["dir_fd"] is not None:
            first = take_snapshot(evidence["dir_fd"], evidence["dir_key"], int(evidence["dev"]))
            second = take_snapshot(evidence["dir_fd"], evidence["dir_key"], int(evidence["dev"]))
            terminal_parent = Chain(EVIDENCE_PARENT_COMPONENTS)
            terminal_evidence = open_evidence(terminal_parent)
            if terminal_evidence["dir_fd"] is not None:
                third = take_snapshot(
                    terminal_evidence["dir_fd"],
                    terminal_evidence["dir_key"],
                    int(terminal_evidence["dev"]),
                )
        parent_stable = int(
            terminal_parent is not None
            and parent.keys == terminal_parent.keys
            and terminal_evidence is not None
            and evidence_signature(evidence) == evidence_signature(terminal_evidence)
        )
        snapshot_stable = int(
            parent_stable == 1
            and snapshot_signature(first) == snapshot_signature(second)
            and snapshot_signature(first) == snapshot_signature(third)
        )
        inventories_complete = int(
            first["inventory"]["complete"] == 1
            and second["inventory"]["complete"] == 1
            and third["inventory"]["complete"] == 1
        )
        names = first["inventory"]["names"]
        unknown_names = tuple(name for name in names if name not in CANDIDATE_NAMES)
        duplicate_pairs, source_aliases = relation_lists(first["records"], inputs.source)
        proposed_phase = classify_phase(
            first["records"],
            names,
            recovery,
            pass_seen,
            inputs.source["exact"],
            evidence["exact"],
            inventories_complete,
            snapshot_stable,
            unknown_names,
            duplicate_pairs,
            source_aliases,
        )
        lines = [source_line(inputs.source), evidence_line(evidence)]
        lines.append(inventory_line(1, first["inventory"]))
        lines.append(inventory_line(2, second["inventory"]))
        lines.append(inventory_line(3, third["inventory"]))
        for index, record in enumerate(first["records"]):
            lines.append(candidate_line(index, record))
        lines.append(
            (
                "RELATIONS duplicate_pairs="
                + (",".join(duplicate_pairs) if duplicate_pairs else "none")
                + " source_aliases="
                + (",".join(source_aliases) if source_aliases else "none")
                + " snapshots_stable="
                + str(snapshot_stable)
                + " parent_chain_stable="
                + str(parent_stable)
                + "\n"
            ).encode("ascii")
        )
        lines.extend(
            anomaly_lines(
                inputs.source,
                evidence,
                first["records"],
                unknown_names,
                duplicate_pairs,
                source_aliases,
                snapshot_stable,
            )
        )
        body = b"".join(lines)
        need(len(body) <= BINDER_CAP, "binder-body-cap")
        meta["body"] = body
        meta["base_status"] = "ok"
        meta["proposed_phase"] = proposed_phase
        meta["inventory_complete"] = inventories_complete
        meta["snapshots_stable"] = snapshot_stable
        meta["error"] = "none"
    except BaseException as error:
        if isinstance(error, Stop):
            meta["error"] = error.code
        else:
            meta["error"] = "unexpected-binder"
    finally:
        close_snapshot(third)
        close_snapshot(second)
        close_snapshot(first)
        if terminal_evidence is not None:
            close_evidence(terminal_evidence)
        if terminal_parent is not None:
            terminal_parent.close()
        close_evidence(evidence)
        if parent is not None:
            parent.close()
        inputs.verify_after()
        meta["post_inputs_reverified"] = inputs.post_inputs_reverified
        if not inputs.close():
            meta["base_status"] = "error"
        if inputs.verify_error != "none":
            meta["error"] = inputs.verify_error
    if meta["post_inputs_reverified"] != 1 or CLOSE_FAILED:
        meta["base_status"] = "error"
        meta["proposed_phase"] = "unknown-mismatch"
    return meta

def render_binder(meta, recovery):
    if meta is None:
        meta = empty_binder_meta("recovery-binder" if recovery else "watchdog")
        meta["error"] = "pre-emission-close"
    final_error = int(CLOSE_FAILED)
    status = meta["base_status"]
    phase = meta["proposed_phase"]
    if (
        status == "error"
        or meta["inventory_complete"] != 1
        or meta["snapshots_stable"] != 1
        or meta["post_inputs_reverified"] != 1
        or final_error
    ):
        status = "error"
        phase = "unknown-mismatch"
    sites = ",".join(CLOSE_FAILURE_SITES) if CLOSE_FAILURE_SITES else "none"
    header = (
        "BINDER version=2 status="
        + status
        + " mode="
        + meta["mode"]
        + " durability_phase="
        + phase
        + " inventory_complete="
        + str(meta["inventory_complete"])
        + " snapshots_stable="
        + str(meta["snapshots_stable"])
        + " post_inputs_reverified="
        + str(meta["post_inputs_reverified"])
        + " recovery_pre_evidence_esrch="
        + meta["recovery_pre_evidence_esrch"]
        + " internal_close_error="
        + str(final_error)
        + " close_failure_sites="
        + sites
        + " close_failure_sites_truncated="
        + str(CLOSE_FAILURE_SITES_TRUNCATED)
        + " error="
        + meta["error"]
        + "\n"
    ).encode("ascii")
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
    report = header + meta["body"] + provenance + b"BINDER_END\n"
    need(len(report) <= BINDER_CAP, "binder-cap")
    return report, status, phase

def wait_deadline(pid, deadline):
    while True:
        try:
            got, status_value = os.waitpid(pid, os.WNOHANG)
        except InterruptedError:
            continue
        if got == pid:
            return status_value
        need(got == 0, "waitpid-other")
        if time.monotonic_ns() >= deadline:
            return None
        time.sleep(0.01)

def wait_blocking(pid):
    while True:
        try:
            got, status_value = os.waitpid(pid, 0)
        except InterruptedError:
            continue
        need(got == pid, "waitpid-other")
        return status_value

def read_token_eof(fd, token, deadline, code):
    os.set_blocking(fd, False)
    poller = select.poll()
    poller.register(fd, select.POLLIN | select.POLLHUP | select.POLLERR | select.POLLNVAL)
    data = bytearray()
    eof = False
    while not eof:
        remaining = deadline - time.monotonic_ns()
        need(remaining > 0, code + "-timeout")
        events = poller.poll(min(POLL_SLICE_MS, max(1, (remaining + 999999) // 1000000)))
        for current, mask in events:
            need(current == fd and not mask & select.POLLNVAL, code + "-poll")
            while True:
                try:
                    piece = os.read(fd, 2)
                except BlockingIOError:
                    break
                if piece == b"":
                    eof = True
                    break
                data.extend(piece)
                need(len(data) <= len(token) and bytes(data) == token[:len(data)], code + "-byte")
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
        "BEGIN E001_SUPERVISOR_BINDER_RECOVERY version=2 supervisor_pid="
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
        + " whole_control_binding=actor-attested"
        + " self_bytes="
        + str(binding.self_bytes)
        + " self_LF="
        + str(binding.self_lf)
        + " self_sha256="
        + binding.self_sha
        + " ledger_prefix_bytes="
        + str(binding.ledger_bytes)
        + " ledger_prefix_LF="
        + str(binding.ledger_lf)
        + " ledger_prefix_sha256="
        + binding.ledger_sha
        + " payload_sha256=6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0"
        + " launcher_sha256=72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd"
        + " inner_sha256=e556f5dc1b9bf31bcc3640000db29ee842048a643094ceca2083eb883ef4565f"
        + " actor_overall_deadline_ns="
        + str(ACTOR_OVERALL_DEADLINE_NS)
        + " actor_deadline_semantics=sticky-external"
        + " attempt_consumed=0\n"
    ).encode("ascii")
    need(len(value) < 2048, "begin-cap")
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

def kill_payload(pid):
    try:
        os.kill(pid, signal.SIGKILL)
    except OSError as error:
        if error.errno != errno.ESRCH:
            stop("payload-kill")

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
            try:
                got, wait_value = os.waitpid(pid, os.WNOHANG)
            except InterruptedError:
                got = 0
                wait_value = 0
            if got == pid:
                state["wait_raw"] = wait_value
                reaped_time = now
            elif got != 0:
                stop("payload-wait")
        if state["wait_raw"] is None and now >= deadline:
            state["timeout"] = 1
        failed = (
            state["out_overflow"]
            or state["err_overflow"]
            or state["timeout"]
            or state["supervisor_lost"]
            or state["capture_error"] != "none"
            or CLOSE_FAILED
        )
        if failed and not killed and state["wait_raw"] is None:
            kill_payload(pid)
            killed = True
            kill_time = now
        if kill_time is not None and state["wait_raw"] is None and now - kill_time >= KILL_REAP_GRACE_NS:
            mark_capture_error(state, "reap-grace")
            return state, False
        if state["wait_raw"] is not None and not open_streams:
            break
        if reaped_time is not None and open_streams and now - reaped_time >= PIPE_EOF_GRACE_NS:
            mark_capture_error(state, "eof-grace")
            return state, False
        events = poller.poll(POLL_SLICE_MS)
        for fd, mask in events:
            if mask & select.POLLNVAL:
                mark_capture_error(state, "pollnval")
                continue
            if fd == life_fd:
                while True:
                    try:
                        piece = os.read(life_fd, CHUNK)
                    except BlockingIOError:
                        break
                    except OSError:
                        mark_capture_error(state, "lifeline-read")
                        break
                    if piece == b"":
                        state["supervisor_lost"] = 1
                        try:
                            poller.unregister(life_fd)
                        except BaseException:
                            mark_capture_error(state, "lifeline-unregister")
                        break
                    mark_capture_error(state, "lifeline-data")
                continue
            if fd in open_streams:
                key = open_streams[fd]
                while True:
                    try:
                        piece = os.read(fd, CHUNK)
                    except BlockingIOError:
                        break
                    except OSError:
                        mark_capture_error(state, key + "-read")
                        close_stream(state, key, fd, poller, open_streams)
                        break
                    if piece == b"":
                        state[key + "_eof"] = 1
                        close_stream(state, key, fd, poller, open_streams)
                        break
                    capture_piece(state, key, piece, STDOUT_CAP if key == "out" else STDERR_CAP)
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
    safe = state["out_eof"] == 1 and state["err_eof"] == 1
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

def result_line(mode, state, binder, binder_status, phase, disposition):
    sites = ",".join(CLOSE_FAILURE_SITES) if CLOSE_FAILURE_SITES else "none"
    fields = (
        "RESULT E001_SUPERVISOR_BINDER_RECOVERY"
        + " version=2"
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

def binding_argv_bytes(binding):
    return tuple(item.encode("ascii") for item in binding.text)

def spawn_payload(strict, out_read, out_write, err_read, err_write):
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
    return os.posix_spawn(
        ENV_TOOL,
        strict.payload_argv,
        {},
        file_actions=actions,
        setsigmask=(),
        setsigdef=SIGNAL_DEFAULTS,
    )

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
    if 10 in OPEN_FDS and not probe_lifeline(10):
        state["supervisor_lost"] = 1
        mark_capture_error(state, "final-lifeline")
    pass_seen = (
        state["out_eof"] == 1
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
    meta = None
    if not success:
        try:
            failure_inputs = FailureBinderInputs(strict.control.binding)
            meta = binder_observe(failure_inputs, False, pass_seen, None)
        except BaseException:
            meta = empty_binder_meta("watchdog")
            meta["error"] = "binder-input-open"
    try:
        strict.verify()
    except BaseException:
        success = False
        mark_capture_error(state, "input-terminal-drift")
        if meta is None:
            meta = empty_binder_meta("watchdog")
        meta["base_status"] = "error"
        meta["proposed_phase"] = "unknown-mismatch"
        meta["post_inputs_reverified"] = 0
        meta["error"] = "input-terminal-drift"
    strict.close()
    if 10 in OPEN_FDS:
        closed_life = close_fd(10, "life-close")
        state["life_close_error"] |= int(not closed_life)
    close_all()
    close_owned(0, "stdin-close")
    close_owned(2, "stderr-close")
    if CLOSE_FAILED:
        success = False
        mark_capture_error(state, "internal-close")
        if meta is None:
            meta = empty_binder_meta("watchdog")
            meta["error"] = "pre-emission-close"
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
    runtime("supervisor", (0, 1, 2, 3), binding)
    track(3)
    try:
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
        ) + binding_argv_bytes(binding)
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
        pid = os.posix_spawn(
            PYTHON,
            watchdog_argv,
            EXPECTED_ENV,
            file_actions=actions,
            setsigmask=(),
            setsigdef=SIGNAL_DEFAULTS,
            setsid=True,
        )
        need(pid > 1, "watchdog-pid")
        WATCHDOG_PID = pid
        close_fd(3, "stdin-close")
        close_fd(life_read, "life-close")
        close_fd(ready_write, "ready-close")
        need(not CLOSE_FAILED, "supervisor-opposite-close")
        ready = read_token_eof(
            ready_read,
            b"R",
            time.monotonic_ns() + READY_DEADLINE_NS,
            "ready",
        )
        need(ready == b"R", "ready-byte")
        close_fd(ready_read, "ready-close")
        need(not CLOSE_FAILED, "supervisor-ready-close")
        need(os.getsid(pid) == pid and os.getpgid(pid) == pid, "watchdog-session")
        write_all(1, begin_line(pid, binding))
        ack = read_token_eof(
            0,
            b"A",
            time.monotonic_ns() + ACK_DEADLINE_NS,
            "ack",
        )
        need(ack == b"A", "ack-byte")
        close_owned(0, "ack-close")
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
    try:
        need(os.getpid() == os.getsid(0) == os.getpgrp(), "watchdog-session-self")
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
        pid = spawn_payload(strict, out_read, out_write, err_read, err_write)
        state["payload_spawned"] = 1
        need(
            pid > 1
            and os.getpgid(pid) == os.getpgrp()
            and os.getsid(pid) == os.getsid(0),
            "payload-pgid",
        )
        close_fd(out_write, "payload-writer-close")
        close_fd(err_write, "payload-writer-close")
        state, safe = capture_payload(pid, out_read, err_read, 10)
        finalize_watchdog(strict, state, safe, "none")
    except BaseException as error:
        code = error.code if isinstance(error, Stop) else "unexpected"
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
    require_group_absent(pgid)
    inputs = FailureBinderInputs(binding)
    def pre_evidence_check():
        require_group_absent(pgid)
        return Chain(EVIDENCE_PARENT_COMPONENTS)
    meta = binder_observe(inputs, True, False, pre_evidence_check)
    need(meta["recovery_pre_evidence_esrch"] == "1", "recovery-pre-evidence-proof")
    close_all()
    close_owned(0, "stdin-close")
    close_owned(2, "stderr-close")
    binder, binder_status, phase = render_binder(meta, True)
    state = recovery_capture(pgid)
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
BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V2_PROGRAM_END

## 4. Canonical transports and external actor

The ready, ACK, and start tokens are exact one-byte R, A, and S.  Ready and
ACK must each be followed by EOF.  The start/lifeline writer remains open
until watchdog reap.  BEGIN and RESULT use version=2 and the literal field
orders in the program.  BEGIN binds the actor-attested whole-control and
ledger-prefix values, exact marker program, unchanged payload, launcher and
fully substituted inner.  RESULT distinguishes executable marker binding
from actor-attested whole-control binding.

The later actor must itself be frozen and independently reviewed.  It must:

1. verify the execution-authorizing complete ledger prefix, whole V2 file,
   exact marker program, all frozen controls and tools, and the unchanged
   payload, launcher and inner;
2. launch supervisor under the exact ten-key environment, workspace, umask,
   signal defaults/mask, hard FD premise, and four independent binary pipes;
3. concurrently drain stdout and stderr with no normalization, merging,
   command capture or truncation;
4. accept one canonical BEGIN and verify the direct PID, watchdog session
   PID/PGID, binding tuple, and every frozen transport identity;
5. durably append a pending event with attempt_consumed=0, supervisor PID,
   watchdog PID/PGID and all binding identities, fsync the ledger and parent,
   and freshly rebind the complete result before writing A and closing ACK;
6. retain the independent payload-stdin writer, write it no bytes, and treat
   any ambiguity after beginning the A write as permanently possibly
   consumed and never retryable;
7. enforce a monotone 420-second overall deadline.  On any loss, kill the
   direct supervisor and negative watchdog PGID, reap the supervisor, prove
   the full group absent, and invoke recovery-binder exactly once only when
   S may have been consumed;
8. accept a direct result only after exact BEGIN plus one RESULT, stdout EOF,
   empty stderr EOF, supervisor exit zero, and absent watchdog PGID;
9. declare physical success only for the complete RESULT success conjunction
   and only if its own deadline never fired and payload stdin stayed live and
   unused; and
10. terminally reverify whole V2, all inputs, tools and the entire current
    ledger, append the complete physical outcome while the single-writer
    interval remains held, fsync file and parent, and freshly rebind exact
    bytes, LF, SHA-256 and terminal.

Any complete result paired with missing EOF, nonempty external stderr,
nonzero or missing supervisor status, deadline, PGID presence, identity
drift, or ledger-order failure is loss, never success.  The program cannot
attest its future fd1 close; complete report, EOF and both process statuses
form the later attestation.

## 5. Binder and recovery contract

CLOSE_FAILED is process-global, monotone and never cleared.  Each attempted
internal close owns its descriptor exactly once, records a bounded fixed
site token before any later rendering can claim success, and is never retried
after an ambiguous close error.  Candidate, directory, inventory, stream,
preflight, fd0 and fd2 closes all participate.  Binder header, final phase,
RESULT close bit and disposition are rendered only after every pre-emission
close.  The sole later fd1-close epistemic boundary is covered by external
EOF and exit status.

Every inventory pass opens dot relative to the identity-checked evidence fd,
thereby obtaining an independent open-file description at offset zero.  Its
iterator and scan fd close explicitly.  Initial, repeated and fresh-terminal
snapshots must agree.  Incomplete/capped scans retain bounded triggering-name
fingerprints and never claim unseen entries absent.  Unknown children are
name-only and unopened.

StrictPreflight alone owns payload_argv and the unforgeable launch token.
FailureBinderInputs owns no payload, inner, argv or launch method.  It observes
source metadata before exactness predicates and observes anomalous evidence
metadata before directory predicates.  A regular source hardlink remains
boundedly readable for observation but can never launch.  Directory
candidates, other nonregular candidates, size caps, unknown children,
candidate aliases, source aliases, evidence nlink anomalies and all drift are
explicit records and conservatively force unknown-mismatch.

Recovery verifies old-PGID ESRCH initially, immediately before the first
evidence-parent open, and immediately before RESULT emission.  It performs
complete post-binder control, self, ledger, source and tool reverification,
uses unavailable-recovery wait and stream provenance, and always reports
PERMANENT_FAILURE with unknown-mismatch.  Any infrastructure, close, cap,
containment or terminal-input problem is permanent failure/unknown; collected
records are not erased to manufacture a stronger phase.

## 6. Mechanically derived no-build fixture specification

No fixture or microtest is authorized here.  A later control may derive a
fixture only from the exact normalized V2 program by ordered unique-anchor
replacement.  Each replacement record is class, identifier, old hex, new
hex, old offset, old SHA-256 and new SHA-256.  The only classes are:

- C1: fixture-only labels and self/status names;
- C2: workspace, input and tool identities redirected to one isolated
  non-build tree;
- C3: the complete payload, launcher, PASS bytes and their identities
  replaced with no-fork synthetic stubs;
- C4: timeout and cap decimal literals; and
- C5: actor-passed fixture whole-self and ledger tuples.

Replacing every changed span by its class/identifier token must give the
same production and fixture skeleton SHA-256.  No function or control-flow
byte may differ.  Production contains no test branch, environment switch,
monkeypatch, fault hook, production build/evidence fixture literal, or second
payload path.

Normal channels cover ACK A-plus-EOF, live-after-A, premature EOF, wrong or
extra bytes and timeout; payload pass, stdout/stderr, exit, signal, timeout
and overflow; supervisor/lifeline/report loss; and synthetic inventory,
alias, nonregular, cap and drift states.  Separate exact-snippet host probes
cover deterministic watchdog environment, inherited blocked/ignored signal
normalization, and rejection of inherited descriptors 4096 and 1048575.
Close-syscall failure and impossible malformed-watchdog-only paths remain
honestly static-only unless a separately derived and reviewed helper receives
authority.  No test may claim production equivalence beyond its exact branch
map.

## 7. Remaining host premises and author stop

Activation still trusts the frozen CPython 3.12 and libc posix_spawn/file-
action implementation, the host-wide 1048576 FD ceiling, timely SIGKILL and
reap outside uninterruptible kernel sleep, no adversarial PID/PGID reuse over
the checked interval, the statically proved direct exec chain with no process-
group escape, root CAP_FOWNER for O_NOATIME, filesystem fsync durability, and
pathname/tool immutability during the declared single-writer intervals.

This author stop creates no E001, recovery-binder, microtest, E010, A000,
stage, root, PDF, release or Paper28 execution authority.

BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V2_AUTHOR_STOP
