# E001 posix-spawn supervisor and failure binder V5

## 1. Exact authority and frozen inputs

This V5 control is inert authoring text. It grants no execution, host-probe,
fixture, microtest, build, evidence, root, release, or retry authority. The
sole ledger authority is the exact E0323 prefix of BATCH_07_STATUS.md:

- device 2431, inode 12439253869, mode 0644, link count 1, uid 0, gid 0;
- 1757838 bytes and 20037 LF bytes;
- SHA-256 bf9db8399a5e5baf25599b88f657076680497a920e7be36ee4515ef9d444c1eb;
- exact terminal BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V4_STATIC_REVIEW_FAILURE_RECORDED_AND_V5_CONTROL_AUTHORIZED.

The sole predecessor binder bound by this program is the frozen
E001_SUPERVISOR_BINDER_RECOVERY_V4.md:

- device 2431, inode 5913750730, mode 0644, link count 1, uid 0, gid 0;
- 159710 bytes and 4163 LF bytes;
- SHA-256 9acf33952e81197b4cff8c714bc6484bacd976f88f186f6b4946e37277cd6da0;
- exact terminal BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V4_AUTHOR_STOP.

The status anchor and V4 identity are hard-coded as well as checked through
the actor-supplied eleven-field Binding. A later appendable ledger binding may
extend E0323 only on the same bound status inode. V1 through V3, every review,
the 114-row manifest, the payload control, build/evidence material, and every
other repository object remain byte-immutable and are neither superseded nor
granted new authority here. The frozen payload extraction identities,
launcher, inner command, eleven-field Binding, ACK protocol, high-FD census,
signal and environment normalization, group containment, close latches,
candidate rules, no-retry rule, and exact PASS identity remain unchanged.

The marker program is static text during authoring and review. It may not be
imported, parsed, compiled, evaluated, or executed. It contains no fork API,
subprocess module, preexec hook, ctypes, prctl, dynamic import, evaluator,
compiler, temporary-file, PTY, tee, cleanup mutation, repair, backfill,
second payload, or second-attempt path. Child creation is only through
os.posix_spawn. A safe write loop may repeat an interrupted write syscall;
that is not an attempt retry.

## 2. Trust boundary and causal lifecycle

The normalized marker bytes bind themselves through CODE_BYTES; they do not
claim to self-certify this Markdown container. A separately frozen actor must
supply and independently revalidate the whole V5 file identity and the
appendable ledger-prefix identity. The program binds the exact E0323 physical
anchor, frozen V4, fixed controls, tools, source, payload, marker transport,
and actor tuple before governed work. This separates executable self-binding
from whole-control attestation without a circular claim.

The actor owns five independent binary pipes. Supervisor fd0 is ACK input,
fd1 and fd2 are raw result streams, fd3 is payload stdin, and fd4 is launch
release. It spawns the supervisor with setsid true, binds the direct PID as
SID and PGID, durably records containment, then writes exact L plus EOF. The
supervisor cannot create the watchdog before release. The actor appends and
rebinds the pending event before exact A plus EOF. Payload stdin remains
unwritten and live until containment is resolved. The watchdog receives the
deterministic ten-key environment and stays in the actor-known group.

Ready has one 30-second absolute guard frozen immediately before watchdog
spawn. ACK has one 300-second guard frozen immediately before BEGIN
construction. Payload capture has one 30-second guard frozen immediately
before payload spawn. Kill/reap has a fresh 5-second cleanup-only guard.
Every physical capture reap creates an immutable WaitObservation containing
outcome, origin, governing deadline, wait-called bit, the exact first
post-wait timestamp, physical-reap bit, timely bit, raw status, derived stream
deadline, and finite error token. Its stream deadline is checked unsigned
addition of exactly one second to that single timestamp; no caller resamples
time for it.

Reduction is monotone. A late physical reap retains status, origin and both
timestamps, latches its governing deadline, transitions UNSAFE, and forbids a
later PID signal. A timely payload or kill reap freezes origin, T and S before
caller work. Kill-origin is cleanup-only. Each EOF has one immutable stream,
causal phase, guard, exact first post-read timestamp and timely bit. Pre-reap
EOF remains PAYLOAD_WAIT or KILL_REAP; post-reap EOF is STREAM_EOF. No record
is relabeled. Completion requires timely payload-origin reap, S equal to T
plus one second, coherent ordering for both EOF records, exact exit zero,
zero deadline and kill bits, no open stream, no capture or close error, and
no overflow. A killed, late, uncertain or unsafe path emits no authoritative
direct result. Wait ownership errors suppress numeric-PID signaling.

The RESULT carries every payload, kill, stream and EOF deadline, observation
timestamp, origin, phase, raw status and error token in bounded canonical
fields. A future actor must repeat the T/S arithmetic and EOF ordering checks,
then require raw stdout EOF, empty external stderr EOF, watchdog attestation
through supervisor zero exit, process-group ESRCH, terminal whole-control and
ledger revalidation, and durable final append. Actor ready/ACK origins,
deadlines, every pre/post guard, and the sticky 420-second overall deadline
remain externally retained. No visible line alone is authoritative.

## 3. Exact literal V5 program

The raw program is the byte substring after the unique BEGIN marker LF and
through the delimiter LF immediately before the unique END marker. The
normalized program removes that single final LF. At this author stop:

- raw identity: 220606 bytes, 5880 LF bytes, SHA-256
  8c7f124e41f166f8dc2aed6501532e9ba186f2078ad54c3126d5fb8bfa7a0e92;
- normalized identity: 220605 bytes, 5879 LF bytes, 5880 physical lines,
  SHA-256 63b7e7d73c04a79953101a959e3e4aac44b1c22bddc49a8594506b355fb99454;
- normalized final byte decimal 41;
- normalized apostrophe byte 0x27, dollar byte 0x24, and backtick byte 0x60
  census 0/0/0.
BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V5_PROGRAM_BEGIN
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
SELF_NAME = b"E001_SUPERVISOR_BINDER_RECOVERY_V5.md"
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
E0323_BYTES = 1757838
E0323_LF = 20037
E0323_DEV = 2431
E0323_INO = 12439253869
E0323_SHA256 = "bf9db8399a5e5baf25599b88f657076680497a920e7be36ee4515ef9d444c1eb"
E0323_TERMINAL = (
    b"BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V4_STATIC_REVIEW_"
    b"FAILURE_RECORDED_AND_V5_CONTROL_AUTHORIZED\n"
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
    (
        b"E001_SUPERVISOR_BINDER_RECOVERY_V4.md",
        159710,
        4163,
        "9acf33952e81197b4cff8c714bc6484bacd976f88f186f6b4946e37277cd6da0",
        b"BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V4_AUTHOR_STOP\n",
        2431,
        5913750730,
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
INVENTORY_NAME_CAP = 255
INVENTORY_RAW_CAP = 16384
INVENTORY_FRAME_CAP = 33216
UNKNOWN_RECORD_CAP = 64
UNKNOWN_UNION_COUNT_CAP = 192
UNKNOWN_UNION_RAW_CAP = 49152
DUPLICATE_CAP = 6
ALIAS_CAP = 4
SNAPSHOT_ANOMALY_CAP = 96
SNAPSHOT_ANOMALY_TOKEN_CAP = 518
GLOBAL_ANOMALY_CAP = 32
GLOBAL_ANOMALY_TOKEN_CAP = 64
ANOMALY_UNION_CAP = 320
ANOMALY_UNION_TOKEN_CAP = 529
INVENTORY_LINE_CAP = 67072
OBSERVATION_LINE_CAP = 2048
CHAIN_COMPONENT_LINE_CAP = 384
UNKNOWN_LINE_CAP = 640
RELATION_LINE_CAP = 256
SNAPSHOT_ANOMALY_LINE_CAP = 576
GLOBAL_ANOMALY_LINE_CAP = 128
CROSS_LINE_CAP = 1024
UNION_LINE_CAP = 512
REVERIFY_LINE_CAP = 3072
BINDER_HEADER_CAP = 4096
SCHEMA_HEADER_CAP = 128
PROVENANCE_CAP = 256
BINDER_END_CAP = 16
BINDER_WORST = 547472
BINDER_CAP = 589824
RESULT_FIXED_CAP = 12288
RESULT_WORST = 1246496
RESULT_CAP = 1310720
BEGIN_CAP = 4096
UINT64_MAX = 18446744073709551615
NODE_KEY_ARITY = 8
CHAIN_COMPONENT_COUNT = 7
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
CAPTURE_ERROR_ORDER = (
    "capture-poll",
    "counter-overflow",
    "input-drift",
    "input-terminal-drift",
    "internal-close",
    "kill-reap",
    "kill-reap-error",
    "kill-reap-other",
    "life-close",
    "lifeline-data",
    "lifeline-read",
    "lifeline-unregister",
    "out-close",
    "out-counter-overflow",
    "out-read",
    "out-unregister",
    "payload-kill",
    "payload-kill-unexpected",
    "payload-pgid",
    "payload-sid",
    "payload-spawn",
    "payload-spawn-late",
    "payload-topology",
    "payload-wait",
    "payload-wait-error",
    "payload-wait-other",
    "payload-writer-close",
    "pollnval",
    "stream-eof",
    "strict-close",
    "supervisor-lost-before-spawn",
    "unexpected",
    "watchdog-report-lost",
    "err-close",
    "err-counter-overflow",
    "err-read",
    "err-unregister",
)
OBSERVATION_STATES = ("unavailable", "present", "absent", "error")
ABSENCE_STATES = ("none", "ENOENT")
TYPE_STATES = ("none", "regular", "directory", "symlink", "fifo", "socket", "char", "block", "unknown")
CONTENT_STATES = (
    "unavailable",
    "absent",
    "metadata-only",
    "directory-observed",
    "unavailable-nondirectory",
    "unavailable-nonregular",
    "unavailable-size-cap",
    "complete",
    "read-error",
)
MODE_STATES = ("normal", "watchdog", "recovery", "recovery-binder")
BASE_STATUS_STATES = ("ok", "error")
PHASE_STATES = (
    "unknown-mismatch",
    "pre-create",
    "stdout-present-last-durability-unproven",
    "stdout-durable-and-stderr-present-last-durability-unproven",
    "stdout-stderr-durable-and-copy-present-last-durability-unproven",
    "first-three-durable-and-status-present-last-durability-unproven",
    "all-four-durable-post-emission-failure",
)
ESRCH_STATES = ("na", "0", "1")

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

def node_key_good(value):
    return (
        isinstance(value, tuple)
        and len(value) == NODE_KEY_ARITY
        and all(type(item) is int and 0 <= item <= UINT64_MAX for item in value)
    )

def ledger_stable_key(value):
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
        need(
            self.ledger_dev == E0323_DEV and self.ledger_ino == E0323_INO,
            "binding-ledger-node",
        )
        self.ledger_bytes = canonical_decimal(values[7], E0323_BYTES, 16777216, "binding-ledger-bytes")
        self.ledger_lf = canonical_decimal(values[8], E0323_LF, 200000, "binding-ledger-lf")
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
        self.keys.append(node_key(os.fstat(fd)))
        for component in components:
            fd = track(os.open(component, DIR_FLAGS, dir_fd=fd))
            self.fds.append(fd)
            self.keys.append(node_key(os.fstat(fd)))

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

class ObservedChain:
    def __init__(self, components):
        self.components = components
        self.fds = []
        self.keys = [None] * (len(components) + 1)
        self.complete = 0
        self.error = "none"
        fd = None
        try:
            fd = track(os.open(b"/", DIR_FLAGS))
            self.fds.append(fd)
            self.keys[0] = node_key(os.fstat(fd))
            for index, component in enumerate(components, 1):
                fd = track(os.open(component, DIR_FLAGS, dir_fd=fd))
                self.fds.append(fd)
                self.keys[index] = node_key(os.fstat(fd))
            self.complete = 1
        except BaseException:
            self.error = "chain-open"

    def leaf(self):
        return self.fds[-1] if self.complete and self.fds else None

    def signature(self):
        return tuple(self.keys)

    def close(self):
        good = True
        for fd in reversed(self.fds):
            good = close_fd(fd, "chain-close") and good
        self.fds = []
        return good

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
        b"V5_AUTHOR_STOP\n"
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
        b"BINDER_V5_PROGRAM_BEGIN\n"
    )
    end = (
        b"BATCH07_P27_RECOVERY_E001_SUPERVISOR_"
        b"BINDER_V5_PROGRAM_END\n"
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
        need(ledger_stable_key(os.fstat(self.fd)) == ledger_stable_key(before), "ledger-open-race")
        self.data = pread_exact(self.fd, binding.ledger_bytes)
        self.check_data(self.data)
        self.launcher = extract_launcher(self.data[:E0323_BYTES])

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
        anchor = data[:E0323_BYTES]
        need(
            anchor.count(b"\n") == E0323_LF
            and sha(anchor) == E0323_SHA256
            and anchor.endswith(E0323_TERMINAL),
            "ledger-E0323-anchor",
        )

    def verify(self):
        self.chain.rewalk()
        held = os.fstat(self.fd)
        self.check_metadata(held)
        self.check_data(pread_exact(self.fd, self.binding.ledger_bytes))
        before = os.stat(STATUS_NAME, dir_fd=self.chain.leaf(), follow_symlinks=False)
        self.check_metadata(before)
        need(ledger_stable_key(before) == ledger_stable_key(held), "ledger-path-drift")
        fresh = track(os.open(STATUS_NAME, READ_FLAGS, dir_fd=self.chain.leaf()))
        try:
            opened = os.fstat(fresh)
            self.check_metadata(opened)
            need(ledger_stable_key(opened) == ledger_stable_key(held), "ledger-fresh-drift")
            self.check_data(pread_exact(fresh, self.binding.ledger_bytes))
            final_fd = os.fstat(fresh)
            final_path = os.stat(STATUS_NAME, dir_fd=self.chain.leaf(), follow_symlinks=False)
            self.check_metadata(final_fd)
            self.check_metadata(final_path)
            need(ledger_stable_key(final_fd) == ledger_stable_key(held), "ledger-final-fstat")
            need(ledger_stable_key(final_path) == ledger_stable_key(held), "ledger-final-path")
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
        "fresh_chain_attempt_complete": 0,
        "fresh_chain_open_complete": 0,
        "fresh_chain_equal": 0,
        "fresh_path_stat_complete": 0,
        "fresh_path_fd_opened": 0,
        "fresh_path_fd_equal": 0,
        "fresh_directory_fd_opened": 0,
        "fresh_directory_fd_equal": 0,
        "fresh_final_stat_complete": 0,
        "fresh_identity_equal": 0,
        "fresh_chain_close_complete": 0,
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
        "directory_key": None,
        "opening_chain_signature": (None,) * CHAIN_COMPONENT_COUNT,
        "fresh_chain_signature": (None,) * CHAIN_COMPONENT_COUNT,
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
    record["bytes"] = str(value.st_size)
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
    good = True
    for fd in reversed(record["fds"]):
        good = close_fd(fd, site) and good
    record["fds"] = []
    return good

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
        record["fresh_chain_attempt_complete"],
        record["fresh_chain_open_complete"],
        record["fresh_chain_equal"],
        record["fresh_path_stat_complete"],
        record["fresh_path_fd_opened"],
        record["fresh_path_fd_equal"],
        record["fresh_directory_fd_opened"],
        record["fresh_directory_fd_equal"],
        record["fresh_final_stat_complete"],
        record["fresh_identity_equal"],
        record["fresh_chain_close_complete"],
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
        record["opening_chain_signature"],
        record["fresh_chain_signature"],
    )

def observation_line(kind, tag, record):
    need(kind in ("SOURCE", "EVIDENCE", "CANDIDATE"), "observation-kind")
    need(
        tag in ("initial", "terminal") or safe_token(tag, 3),
        "observation-tag",
    )
    value = (
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
        + " fresh_chain_attempt_complete="
        + str(record["fresh_chain_attempt_complete"])
        + " fresh_chain_open_complete="
        + str(record["fresh_chain_open_complete"])
        + " fresh_chain_equal="
        + str(record["fresh_chain_equal"])
        + " fresh_path_stat_complete="
        + str(record["fresh_path_stat_complete"])
        + " fresh_path_fd_opened="
        + str(record["fresh_path_fd_opened"])
        + " fresh_path_fd_equal="
        + str(record["fresh_path_fd_equal"])
        + " fresh_directory_fd_opened="
        + str(record["fresh_directory_fd_opened"])
        + " fresh_directory_fd_equal="
        + str(record["fresh_directory_fd_equal"])
        + " fresh_final_stat_complete="
        + str(record["fresh_final_stat_complete"])
        + " fresh_identity_equal="
        + str(record["fresh_identity_equal"])
        + " fresh_chain_close_complete="
        + str(record["fresh_chain_close_complete"])
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
    need(len(value) <= OBSERVATION_LINE_CAP, "observation-line-cap")
    return value

def chain_component_line(bracket, generation, index, key):
    need(
        bracket in ("initial", "terminal")
        and generation in ("opening", "fresh")
        and type(index) is int
        and 0 <= index < CHAIN_COMPONENT_COUNT,
        "chain-component-fields",
    )
    if key is None:
        fields = ("none",) * NODE_KEY_ARITY
        state_value = "unavailable"
    else:
        need(node_key_good(key), "chain-component-key")
        fields = tuple(str(item) for item in key)
        state_value = "present"
    value = (
        "CHAIN_COMPONENT bracket="
        + bracket
        + " generation="
        + generation
        + " component="
        + str(index)
        + " state="
        + state_value
        + " dev="
        + fields[0]
        + " ino="
        + fields[1]
        + " mode="
        + fields[2]
        + " nlink="
        + fields[3]
        + " uid="
        + fields[4]
        + " gid="
        + fields[5]
        + " rdev="
        + fields[6]
        + " size="
        + fields[7]
        + "\n"
    ).encode("ascii")
    need(len(value) <= CHAIN_COMPONENT_LINE_CAP, "chain-component-line-cap")
    return value

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
            record["path_fd_opened"] = 1
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
            record["path_fd_opened"] = 1
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
    record["opening_chain_signature"] = parent.signature()
    before = None
    if parent.complete != 1 or parent.leaf() is None:
        record["state"] = "error"
        observation_error(record, "evidence-parent-open")
        return record
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
                    record["directory_key"] = node_key(opened)
                    record["content"] = "directory-observed"
            except BaseException:
                observation_error(record, "evidence-directory-open")
        elif not stat.S_ISDIR(before.st_mode):
            record["content"] = "unavailable-nondirectory"
    return record

def fill_final_metadata(record, value):
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

def finish_evidence(record):
    path_fd = record["path_fd"]
    directory_fd = record["dir_fd"]
    fresh_path_fd = None
    fresh_directory_fd = None
    fresh = ObservedChain(EVIDENCE_PARENT_COMPONENTS)
    record["fresh_chain_signature"] = fresh.signature()
    record["fresh_chain_open_complete"] = fresh.complete
    record["fresh_chain_equal"] = int(
        fresh.complete == 1
        and len(record["opening_chain_signature"]) == CHAIN_COMPONENT_COUNT
        and all(node_key_good(value) for value in record["opening_chain_signature"])
        and record["fresh_chain_signature"] == record["opening_chain_signature"]
    )
    retained_path_key = None
    retained_directory_key = None
    first_key = None
    fresh_path_key = None
    fresh_directory_key = None
    final_key = None
    try:
        if path_fd is not None:
            try:
                retained_path_key = node_key(os.fstat(path_fd))
            except BaseException:
                observation_error(record, "evidence-path-final-error")
        if directory_fd is not None:
            try:
                retained_directory_key = node_key(os.fstat(directory_fd))
            except BaseException:
                observation_error(record, "evidence-directory-final-error")
        leaf = fresh.leaf()
        if leaf is None:
            record["final_state"] = "error"
            record["final_error"] = "evidence-fresh-chain"
        else:
            try:
                first = os.stat(EVIDENCE_NAME, dir_fd=leaf, follow_symlinks=False)
            except OSError as error:
                if error.errno == errno.ENOENT:
                    record["fresh_path_stat_complete"] = 1
                    record["final_state"] = "absent"
                    record["final_absence"] = "ENOENT"
                else:
                    record["final_state"] = "error"
                    record["final_error"] = "evidence-fresh-lstat"
            except BaseException:
                record["final_state"] = "error"
                record["final_error"] = "evidence-fresh-lstat-unexpected"
            else:
                record["fresh_path_stat_complete"] = 1
                first_key = node_key(first)
                fill_final_metadata(record, first)
                try:
                    fresh_path_fd = track(os.open(EVIDENCE_NAME, PATH_FLAGS, dir_fd=leaf))
                    record["fresh_path_fd_opened"] = 1
                    fresh_path_key = node_key(os.fstat(fresh_path_fd))
                    record["fresh_path_fd_equal"] = int(fresh_path_key == first_key)
                except BaseException:
                    observation_error(record, "evidence-fresh-path-open")
                if stat.S_ISDIR(first.st_mode):
                    try:
                        fresh_directory_fd = track(os.open(EVIDENCE_NAME, DIR_FLAGS, dir_fd=leaf))
                        record["fresh_directory_fd_opened"] = 1
                        fresh_directory_key = node_key(os.fstat(fresh_directory_fd))
                        record["fresh_directory_fd_equal"] = int(
                            fresh_directory_key == first_key
                        )
                    except BaseException:
                        observation_error(record, "evidence-fresh-directory-open")
            try:
                final = os.stat(EVIDENCE_NAME, dir_fd=leaf, follow_symlinks=False)
            except OSError as error:
                if error.errno == errno.ENOENT:
                    record["fresh_final_stat_complete"] = 1
                    if record["state"] == "absent":
                        record["final_state"] = "absent"
                        record["final_absence"] = "ENOENT"
                else:
                    record["final_error"] = "evidence-fresh-final-lstat"
            except BaseException:
                record["final_error"] = "evidence-fresh-final-unexpected"
            else:
                record["fresh_final_stat_complete"] = 1
                final_key = node_key(final)
                fill_final_metadata(record, final)
        if record["state"] == "absent":
            record["fresh_identity_equal"] = int(
                record["absence"] == "ENOENT"
                and record["fresh_path_stat_complete"] == 1
                and record["fresh_final_stat_complete"] == 1
                and record["final_state"] == "absent"
                and record["final_absence"] == "ENOENT"
                and path_fd is None
                and directory_fd is None
                and fresh_path_fd is None
                and fresh_directory_fd is None
            )
        elif record["state"] == "present":
            record["fresh_identity_equal"] = int(
                node_key_good(record["key"])
                and retained_path_key == record["key"]
                and retained_directory_key == record["key"]
                and first_key == record["key"]
                and fresh_path_key == record["key"]
                and fresh_directory_key == record["key"]
                and final_key == record["key"]
                and record["fresh_path_fd_opened"] == 1
                and record["fresh_path_fd_equal"] == 1
                and record["fresh_directory_fd_opened"] == 1
                and record["fresh_directory_fd_equal"] == 1
            )
    except BaseException:
        record["final_state"] = "error"
        record["final_error"] = "evidence-finalizer-unexpected"
    finally:
        close_good = True
        if fresh_directory_fd is not None:
            close_good = close_fd(fresh_directory_fd, "fresh-close") and close_good
        if fresh_path_fd is not None:
            close_good = close_fd(fresh_path_fd, "fresh-close") and close_good
        close_good = fresh.close() and close_good
        record["fresh_chain_close_complete"] = int(close_good)
        record["fresh_chain_attempt_complete"] = 1
    record["path_finalized_after_bracket"] = int(
        record["fresh_chain_attempt_complete"] == 1
        and record["fresh_chain_open_complete"] == 1
        and record["fresh_chain_equal"] == 1
        and record["fresh_path_stat_complete"] == 1
        and record["fresh_final_stat_complete"] == 1
        and record["fresh_identity_equal"] == 1
        and record["fresh_chain_close_complete"] == 1
        and record["final_error"] == "none"
    )
    record["stable"] = record["path_finalized_after_bracket"]
    record["exact_absent"] = int(
        record["state"] == "absent"
        and record["absence"] == "ENOENT"
        and record["final_state"] == "absent"
        and record["final_absence"] == "ENOENT"
        and record["stable"] == 1
        and record["error"] == "none"
        and record["final_error"] == "none"
    )
    record["exact"] = int(
        record["state"] == "present"
        and record["type"] == "directory"
        and record["path_fd_opened"] == 1
        and record["directory_fd_opened"] == 1
        and record["dir_fd"] is not None
        and record["path_finalized_after_bracket"] == 1
        and record["fresh_chain_equal"] == 1
        and record["fresh_identity_equal"] == 1
        and record["fresh_chain_close_complete"] == 1
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
    good = True
    for fd in reversed(record["fds"]):
        good = close_fd(fd, "evidence-close") and good
    record["fds"] = []
    record["path_fd"] = None
    record["dir_fd"] = None
    record["directory_key"] = None
    return good

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
        if node_key(os.fstat(scan_fd)) != expected_key:
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
                    if not 1 <= len(item) <= INVENTORY_NAME_CAP:
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
            if len(frame) > INVENTORY_FRAME_CAP:
                add_inventory_reason(result, "frame-cap")
            result["names"] = tuple(raw)
            result["frame"] = frame
        if node_key(os.fstat(scan_fd)) != expected_key:
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
    good = True
    for record in snapshot["records"]:
        try:
            good = close_observation(record) and good
        except BaseException:
            note_close_failure("candidate-close")
            good = False
    return good

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
        "snapshot_1_success": 0,
        "snapshot_2_success": 0,
        "snapshot_3_success": 0,
        "snapshot_1_close_complete": 0,
        "snapshot_2_close_complete": 0,
        "snapshot_3_close_complete": 0,
        "evidence_initial_close_complete": 0,
        "evidence_terminal_close_complete": 0,
        "evidence_initial_path_finalized_after_bracket": 0,
        "evidence_terminal_path_finalized_after_bracket": 0,
        "pass_seen": 0,
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
    value = normalize_schema_error(value)
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
    value = (
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
    need(len(value) <= INVENTORY_LINE_CAP, "inventory-line-cap")
    return value

def relation_line(snapshot):
    value = (
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
    need(len(value) <= RELATION_LINE_CAP, "relation-line-cap")
    return value

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
        or meta["snapshot_1_success"] != 1
        or meta["snapshot_2_success"] != 1
        or meta["snapshot_3_success"] != 1
        or meta["snapshot_1_close_complete"] != 1
        or meta["snapshot_2_close_complete"] != 1
        or meta["snapshot_3_close_complete"] != 1
        or meta["evidence_initial_close_complete"] != 1
        or meta["evidence_terminal_close_complete"] != 1
        or meta["evidence_initial_path_finalized_after_bracket"] != 1
        or meta["evidence_terminal_path_finalized_after_bracket"] != 1
        or meta["inventories_complete"] != 1
        or meta["snapshots_equal"] != 1
        or meta["post_inputs_reverified"] != 1
        or meta["errors"]
        or meta["errors_truncated"]
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
    meta["pass_seen"] = int(pass_seen)
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
    meta["global_anomalies"] = construct_global_anomalies(meta)
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

OBSERVATION_ERROR_TOKENS = (
    "none",
    "schema-malformed",
    "final-lstat",
    "final-unexpected",
    "source-lstat",
    "source-lstat-unexpected",
    "source-path-race",
    "source-path-open",
    "source-read-race",
    "source-read-final",
    "source-read",
    "candidate-lstat",
    "candidate-lstat-unexpected",
    "candidate-path-race",
    "candidate-path-open",
    "candidate-read-race",
    "candidate-read-final",
    "candidate-read",
    "evidence-parent-open",
    "evidence-lstat",
    "evidence-lstat-unexpected",
    "evidence-path-race",
    "evidence-path-open",
    "evidence-directory-race",
    "evidence-directory-open",
    "evidence-path-final",
    "evidence-path-final-error",
    "evidence-directory-final",
    "evidence-directory-final-error",
    "evidence-fresh-chain",
    "evidence-fresh-lstat",
    "evidence-fresh-lstat-unexpected",
    "evidence-fresh-path-open",
    "evidence-fresh-directory-open",
    "evidence-fresh-final-lstat",
    "evidence-fresh-final-unexpected",
    "evidence-finalizer-unexpected",
    "evidence-unavailable",
    "unexpected",
)
SCHEMA_ERROR_TOKENS = (
    "binder-input-construction",
    "binder-observe",
    "evidence-gate-unavailable",
    "evidence-initial-begin",
    "evidence-initial-close",
    "evidence-initial-finish",
    "evidence-initial-parent-close",
    "evidence-terminal-begin",
    "evidence-terminal-close",
    "evidence-terminal-finish",
    "evidence-terminal-parent-close",
    "final-close-sweep",
    "final-close-sweep-unexpected",
    "input-close",
    "input-close-unexpected",
    "input-terminal-control",
    "input-terminal-control-unavailable",
    "input-terminal-drift",
    "input-terminal-source",
    "input-terminal-source-unavailable",
    "pre-emission-close",
    "recovery-second-esrch",
    "schema-derive",
    "schema-malformed",
    "schema-overflow",
    "schema-serialize",
    "schema-shape",
    "snapshot-1-evidence-unavailable",
    "snapshot-1-unexpected",
    "snapshot-2-evidence-unavailable",
    "snapshot-2-unexpected",
    "snapshot-3-evidence-unavailable",
    "snapshot-3-unexpected",
    "snapshot-close",
    "source-initial-observation",
    "unexpected",
)

def safe_token(value, cap):
    return (
        isinstance(value, str)
        and 1 <= len(value) <= cap
        and all(
            ord("a") <= ord(item) <= ord("z")
            or ord("0") <= ord(item) <= ord("9")
            or item == "-"
            for item in value
        )
    )

def normalize_schema_error(value):
    return value if value in SCHEMA_ERROR_TOKENS else "unexpected"

def canonical_u64_text(value, sentinels=("none",)):
    if value in sentinels:
        return True
    if not isinstance(value, str) or not value:
        return False
    if value == "0":
        return True
    if value[0] == "0" or any(item < "0" or item > "9" for item in value):
        return False
    if len(value) > 20:
        return False
    return int(value) <= UINT64_MAX

def canonical_mode_text(value):
    return (
        value == "none"
        or (
            isinstance(value, str)
            and len(value) == 7
            and all("0" <= item <= "7" for item in value)
        )
    )

def canonical_hash_text(value, sentinels=("none",)):
    return (
        value in sentinels
        or (
            isinstance(value, str)
            and len(value) == 64
            and all(item in "0123456789abcdef" for item in value)
        )
    )

def canonical_inventory_frame(names):
    return b"".join(
        str(len(name)).encode("ascii") + b":" + name.hex().encode("ascii") + b"\n"
        for name in names
    )

def basename_good(value):
    return (
        isinstance(value, bytes)
        and 1 <= len(value) <= INVENTORY_NAME_CAP
        and value not in (b".", b"..")
        and b"/" not in value
        and b"\x00" not in value
    )

def chain_signature_good(value):
    return (
        isinstance(value, tuple)
        and len(value) == CHAIN_COMPONENT_COUNT
        and all(item is None or node_key_good(item) for item in value)
    )

def key_matches_scalars(record, prefix):
    key_name = "key" if prefix == "" else "final_key"
    value = record[key_name]
    state = record["state"] if prefix == "" else record["final_state"]
    names = (
        prefix + "dev",
        prefix + "ino",
        prefix + "mode",
        prefix + "nlink",
        prefix + "uid",
        prefix + "gid",
        prefix + "rdev",
        prefix + "bytes",
    )
    scalars = tuple(record[name] for name in names)
    if state == "present":
        if not node_key_good(value):
            return False
        if not all(canonical_u64_text(item, ()) for index, item in enumerate(scalars) if index != 2):
            return False
        if not canonical_mode_text(scalars[2]) or scalars[2] == "none":
            return False
        parsed = (
            int(scalars[0]),
            int(scalars[1]),
            int(scalars[2], 8),
            int(scalars[3]),
            int(scalars[4]),
            int(scalars[5]),
            int(scalars[6]),
            int(scalars[7]),
        )
        return parsed == value
    return value is None and all(item == "none" for item in scalars)

def stable_claim_good(record):
    if record["stable"] == 0:
        return True
    if record["error"] != "none" or record["final_error"] != "none":
        return False
    if record["state"] == "absent":
        return (
            record["absence"] == "ENOENT"
            and record["final_state"] == "absent"
            and record["final_absence"] == "ENOENT"
        )
    return (
        record["state"] == "present"
        and record["final_state"] == "present"
        and node_key_good(record["key"])
        and record["final_key"] == record["key"]
    )

def exact_claim_good(record, expected_name):
    if record["exact_absent"] == 1:
        if not (
            record["state"] == "absent"
            and record["absence"] == "ENOENT"
            and record["content"] == "absent"
            and record["final_state"] == "absent"
            and record["final_absence"] == "ENOENT"
            and record["stable"] == 1
            and record["error"] == "none"
            and record["final_error"] == "none"
            and record["path_fd_opened"] == 0
        ):
            return False
        if expected_name == EVIDENCE_NAME and not (
            record["path_finalized_after_bracket"] == 1
            and record["fresh_chain_attempt_complete"] == 1
            and record["fresh_chain_open_complete"] == 1
            and record["fresh_chain_equal"] == 1
            and record["fresh_path_stat_complete"] == 1
            and record["fresh_path_fd_opened"] == 0
            and record["fresh_directory_fd_opened"] == 0
            and record["fresh_final_stat_complete"] == 1
            and record["fresh_identity_equal"] == 1
            and record["fresh_chain_close_complete"] == 1
        ):
            return False
    if record["exact"] == 0:
        return True
    if not (
        record["state"] == "present"
        and record["final_state"] == "present"
        and record["stable"] == 1
        and record["error"] == "none"
        and record["final_error"] == "none"
        and record["path_fd_opened"] == 1
        and record["key"] == record["final_key"]
    ):
        return False
    if expected_name == SOURCE_NAME:
        return (
            record["type"] == "regular"
            and record["content"] == "complete"
            and record["dev"] == str(SOURCE_DEV)
            and record["ino"] == str(SOURCE_INO)
            and record["mode"] == format(stat.S_IFREG | 0o644, "07o")
            and record["nlink"] == "1"
            and record["uid"] == "0"
            and record["gid"] == "0"
            and record["rdev"] == "0"
            and record["bytes"] == str(SOURCE_BYTES)
            and record["lf"] == str(SOURCE_LF)
            and record["sha"] == SOURCE_SHA256
            and record["terminal"] == 1
        )
    if expected_name == EVIDENCE_NAME:
        return (
            record["type"] == "directory"
            and record["content"] == "directory-observed"
            and record["dev"] == str(EVIDENCE_DEV)
            and record["ino"] == str(EVIDENCE_INO)
            and record["mode"] == format(stat.S_IFDIR | 0o700, "07o")
            and record["nlink"] == "2"
            and record["uid"] == "0"
            and record["gid"] == "0"
            and record["rdev"] == "0"
            and record["directory_fd_opened"] == 1
            and record["path_finalized_after_bracket"] == 1
            and record["fresh_chain_attempt_complete"] == 1
            and record["fresh_chain_open_complete"] == 1
            and record["fresh_chain_equal"] == 1
            and record["fresh_path_stat_complete"] == 1
            and record["fresh_path_fd_opened"] == 1
            and record["fresh_path_fd_equal"] == 1
            and record["fresh_directory_fd_opened"] == 1
            and record["fresh_directory_fd_equal"] == 1
            and record["fresh_final_stat_complete"] == 1
            and record["fresh_identity_equal"] == 1
            and record["fresh_chain_close_complete"] == 1
            and record["opening_chain_signature"] == record["fresh_chain_signature"]
        )
    expected = candidate_expected(expected_name)
    if expected is None:
        return False
    expected_mode, expected_size, expected_lf, expected_sha, expected_data = expected
    return (
        record["type"] == "regular"
        and record["content"] == "complete"
        and record["mode"] == format(stat.S_IFREG | expected_mode, "07o")
        and record["nlink"] == "1"
        and record["uid"] == "0"
        and record["gid"] == "0"
        and record["rdev"] == "0"
        and record["bytes"] == str(expected_size)
        and record["lf"] == str(expected_lf)
        and record["sha"] == expected_sha
        and record["terminal"] == 0
        and (expected_data is None or record["sha"] == sha(expected_data))
    )

def observation_semantics_good(record, expected_name):
    if expected_name != SOURCE_NAME and record["terminal"] != 0:
        return False
    if record["state"] == "absent":
        if (
            record["absence"] != "ENOENT"
            or record["type"] != "none"
            or record["content"] != "absent"
        ):
            return False
    elif record["state"] == "present":
        if record["absence"] != "none" or record["type"] == "none":
            return False
        if expected_name == EVIDENCE_NAME:
            if record["type"] == "directory":
                if record["content"] not in ("metadata-only", "directory-observed"):
                    return False
            elif record["content"] not in ("metadata-only", "unavailable-nondirectory"):
                return False
        elif record["type"] == "regular":
            if record["content"] not in (
                "unavailable",
                "unavailable-size-cap",
                "complete",
                "read-error",
            ):
                return False
        elif record["content"] != "unavailable-nonregular":
            return False
    elif (
        record["absence"] != "none"
        or record["type"] != "none"
        or record["content"] != "unavailable"
    ):
        return False
    if record["final_state"] == "absent":
        if record["final_absence"] != "ENOENT" or record["final_type"] != "none":
            return False
    elif record["final_state"] == "present":
        if record["final_absence"] != "none" or record["final_type"] == "none":
            return False
    elif record["final_absence"] != "none" or record["final_type"] != "none":
        return False
    if record["content"] == "complete":
        if record["lf"] == "none" or record["sha"] == "none":
            return False
        if int(record["lf"]) > int(record["bytes"]):
            return False
    elif record["lf"] != "none" or record["sha"] != "none" or record["terminal"] != 0:
        return False
    return stable_claim_good(record) and exact_claim_good(record, expected_name)

def observation_shape_good(record, expected_name):
    template = empty_observation(expected_name)
    if not isinstance(record, dict) or set(record) != set(template):
        return False
    if record["name"] != expected_name or record["fds"] != []:
        return False
    if record["path_fd"] is not None or record["dir_fd"] is not None or record["directory_key"] is not None:
        return False
    flag_names = (
        "terminal",
        "exact",
        "exact_absent",
        "stable",
        "path_fd_opened",
        "directory_fd_opened",
        "path_finalized_after_bracket",
        "fresh_chain_attempt_complete",
        "fresh_chain_open_complete",
        "fresh_chain_equal",
        "fresh_path_stat_complete",
        "fresh_path_fd_opened",
        "fresh_path_fd_equal",
        "fresh_directory_fd_opened",
        "fresh_directory_fd_equal",
        "fresh_final_stat_complete",
        "fresh_identity_equal",
        "fresh_chain_close_complete",
    )
    if any(record[name] not in (0, 1) for name in flag_names):
        return False
    if record["state"] not in OBSERVATION_STATES or record["final_state"] not in OBSERVATION_STATES:
        return False
    if record["absence"] not in ABSENCE_STATES or record["final_absence"] not in ABSENCE_STATES:
        return False
    if record["type"] not in TYPE_STATES or record["final_type"] not in TYPE_STATES:
        return False
    if record["content"] not in CONTENT_STATES:
        return False
    if record["error"] not in OBSERVATION_ERROR_TOKENS or record["final_error"] not in OBSERVATION_ERROR_TOKENS:
        return False
    for name in ("dev", "ino", "nlink", "uid", "gid", "rdev", "bytes", "lf"):
        if not canonical_u64_text(record[name]):
            return False
    for name in ("final_dev", "final_ino", "final_nlink", "final_uid", "final_gid", "final_rdev", "final_bytes"):
        if not canonical_u64_text(record[name]):
            return False
    if not canonical_mode_text(record["mode"]) or not canonical_mode_text(record["final_mode"]):
        return False
    if not canonical_hash_text(record["sha"]):
        return False
    if not key_matches_scalars(record, "") or not key_matches_scalars(record, "final_"):
        return False
    if not chain_signature_good(record["opening_chain_signature"]):
        return False
    if not chain_signature_good(record["fresh_chain_signature"]):
        return False
    schema_marked = (
        record["error"] == "schema-malformed"
        or record["final_error"] == "schema-malformed"
    )
    if (
        record["state"] != "present"
        and record["path_fd_opened"] != 0
        and not schema_marked
    ):
        return False
    if record["directory_fd_opened"] == 1 and not (
        expected_name == EVIDENCE_NAME
        and record["state"] == "present"
        and record["type"] == "directory"
    ) and not schema_marked:
        return False
    if record["fresh_chain_attempt_complete"] == 0:
        if any(
            record[name] != 0
            for name in (
                "fresh_chain_open_complete", "fresh_chain_equal",
                "fresh_path_stat_complete", "fresh_path_fd_opened",
                "fresh_path_fd_equal", "fresh_directory_fd_opened",
                "fresh_directory_fd_equal", "fresh_final_stat_complete",
                "fresh_identity_equal", "fresh_chain_close_complete",
            )
        ) or any(item is not None for item in record["fresh_chain_signature"]):
            if schema_marked:
                pass
            else:
                return False
    if record["fresh_chain_open_complete"] == 1 and record["fresh_chain_attempt_complete"] != 1 and not schema_marked:
        return False
    if record["fresh_chain_equal"] == 1 and not (
        record["fresh_chain_open_complete"] == 1
        and all(node_key_good(item) for item in record["opening_chain_signature"])
        and record["opening_chain_signature"] == record["fresh_chain_signature"]
    ) and not schema_marked:
        return False
    if record["fresh_path_fd_equal"] == 1 and not (
        record["fresh_path_stat_complete"] == 1
        and record["fresh_path_fd_opened"] == 1
    ) and not schema_marked:
        return False
    if record["fresh_directory_fd_equal"] == 1 and not (
        record["fresh_path_stat_complete"] == 1
        and record["fresh_directory_fd_opened"] == 1
    ) and not schema_marked:
        return False
    if record["fresh_chain_close_complete"] == 1 and record["fresh_chain_attempt_complete"] != 1 and not schema_marked:
        return False
    if record["fresh_path_stat_complete"] == 1 and record["fresh_chain_open_complete"] != 1 and not schema_marked:
        return False
    if record["fresh_final_stat_complete"] == 1 and record["fresh_chain_open_complete"] != 1 and not schema_marked:
        return False
    if record["fresh_path_fd_opened"] == 1 and record["fresh_path_stat_complete"] != 1 and not schema_marked:
        return False
    if record["fresh_directory_fd_opened"] == 1 and record["fresh_path_stat_complete"] != 1 and not schema_marked:
        return False
    if record["fresh_identity_equal"] == 1 and not schema_marked:
        if not (
            record["fresh_chain_attempt_complete"] == 1
            and record["fresh_chain_open_complete"] == 1
            and record["fresh_chain_equal"] == 1
            and record["fresh_path_stat_complete"] == 1
            and record["fresh_final_stat_complete"] == 1
        ):
            return False
        if record["state"] == "absent":
            if not (
                record["absence"] == "ENOENT"
                and record["final_state"] == "absent"
                and record["final_absence"] == "ENOENT"
                and record["fresh_path_fd_opened"] == 0
                and record["fresh_directory_fd_opened"] == 0
            ):
                return False
        elif record["state"] == "present":
            if not (
                record["key"] == record["final_key"]
                and record["fresh_path_fd_opened"] == 1
                and record["fresh_path_fd_equal"] == 1
                and record["fresh_directory_fd_opened"] == 1
                and record["fresh_directory_fd_equal"] == 1
            ):
                return False
        else:
            return False
    if expected_name != EVIDENCE_NAME:
        if record["directory_fd_opened"] != 0 or record["path_finalized_after_bracket"] != 0:
            return False
        if any(record[name] != 0 for name in flag_names[7:]):
            return False
        if any(item is not None for item in record["opening_chain_signature"]):
            return False
        if any(item is not None for item in record["fresh_chain_signature"]):
            return False
    elif record["stable"] != record["path_finalized_after_bracket"]:
        return False
    if record["path_finalized_after_bracket"] == 1:
        if not all(
            record[name] == 1
            for name in (
                "fresh_chain_attempt_complete",
                "fresh_chain_open_complete",
                "fresh_chain_equal",
                "fresh_path_stat_complete",
                "fresh_final_stat_complete",
                "fresh_identity_equal",
                "fresh_chain_close_complete",
            )
        ):
            return False
    return observation_semantics_good(record, expected_name)

def inventory_shape_good(inventory):
    template = new_inventory()
    if not isinstance(inventory, dict) or set(inventory) != set(template):
        return False
    names = inventory["names"]
    if not isinstance(names, tuple) or len(names) > INVENTORY_ITEMS_CAP:
        return False
    if any(not basename_good(name) for name in names):
        return False
    if tuple(sorted(set(names))) != names:
        return False
    if sum(len(name) for name in names) > INVENTORY_RAW_CAP:
        return False
    frame = canonical_inventory_frame(names)
    if inventory["frame"] != frame or len(frame) > INVENTORY_FRAME_CAP:
        return False
    if inventory["complete"] not in (0, 1) or inventory["reason_truncated"] not in (0, 1):
        return False
    bits = inventory["reason_bits"]
    if not isinstance(bits, dict) or tuple(bits) != INVENTORY_REASON_ORDER:
        return False
    if any(bits[key] not in (0, 1) for key in INVENTORY_REASON_ORDER):
        return False
    if inventory["complete"] != int(
        inventory["reason_truncated"] == 0 and not any(bits.values())
    ):
        return False
    return (
        canonical_u64_text(inventory["overflow_bytes"])
        and canonical_hash_text(inventory["overflow_sha"])
        and (
            (inventory["overflow_bytes"] == "none" and inventory["overflow_sha"] == "none")
            or (
                inventory["overflow_bytes"] != "none"
                and inventory["overflow_sha"] != "none"
                and int(inventory["overflow_bytes"]) >= 1
            )
        )
    )

def bounded_bytes_tuple(value, count_cap, byte_cap):
    return (
        isinstance(value, tuple)
        and len(value) <= count_cap
        and all(basename_good(item) for item in value)
        and len(set(value)) == len(value)
        and sum(len(item) for item in value) <= byte_cap
    )

def bounded_token_tuple(value, count_cap, token_cap):
    return (
        isinstance(value, tuple)
        and len(value) <= count_cap
        and len(set(value)) == len(value)
        and all(safe_token(item, token_cap) for item in value)
    )

def construct_global_anomalies(meta):
    values = []
    for tag, record in (
        ("source-initial", meta["source_initial"]),
        ("source-terminal", meta["source_terminal"]),
        ("evidence-initial", meta["evidence_initial"]),
        ("evidence-terminal", meta["evidence_terminal"]),
    ):
        if record["exact"] != 1:
            values.append(tag + "-not-exact")
        if record["stable"] != 1:
            values.append(tag + "-unstable")
        if record["error"] != "none" or record["final_error"] != "none":
            values.append(tag + "-error")
        if tag.startswith("source-") and record["state"] == "present" and record["nlink"] != "1":
            values.append(tag + "-nlink-" + record["nlink"])
        if tag.startswith("evidence-") and record["state"] == "present" and record["nlink"] != "2":
            values.append(tag + "-nlink-" + record["nlink"])
        if tag.startswith("source-") and record["state"] == "present" and record["type"] != "regular":
            values.append(tag + "-nonregular-" + record["type"])
        if tag.startswith("evidence-") and record["state"] == "present" and record["type"] != "directory":
            values.append(tag + "-nondirectory-" + record["type"])
        if record["content"] == "unavailable-size-cap":
            values.append(tag + "-size-cap")
    if meta["source_equal"] != 1:
        values.append("source-cross-drift")
    if meta["evidence_equal"] != 1:
        values.append("evidence-cross-drift")
    for index in (1, 2, 3):
        if meta["snapshot_" + str(index) + "_success"] != 1:
            values.append("snapshot-" + str(index) + "-unsuccessful")
        if meta["snapshot_" + str(index) + "_close_complete"] != 1:
            values.append("snapshot-" + str(index) + "-close-incomplete")
    if meta["evidence_initial_path_finalized_after_bracket"] != 1:
        values.append("evidence-initial-finalizer-incomplete")
    if meta["evidence_terminal_path_finalized_after_bracket"] != 1:
        values.append("evidence-terminal-finalizer-incomplete")
    if meta["snapshots_equal"] != 1:
        values.append("snapshot-cross-drift")
    return tuple(sorted(set(values)))

def validate_schema_shape(meta):
    if not isinstance(meta, dict):
        return False
    mode = meta.get("mode")
    if mode not in MODE_STATES:
        return False
    template = new_audit_schema(mode)
    if set(meta) != set(template):
        return False
    for key, name in (
        ("source_initial", SOURCE_NAME),
        ("source_terminal", SOURCE_NAME),
        ("evidence_initial", EVIDENCE_NAME),
        ("evidence_terminal", EVIDENCE_NAME),
    ):
        if not observation_shape_good(meta[key], name):
            return False
    snapshots = meta["snapshots"]
    if not isinstance(snapshots, list) or len(snapshots) != 3:
        return False
    source = meta["source_initial"]
    for offset, snapshot in enumerate(snapshots):
        expected = unavailable_snapshot(offset + 1, "unexpected")
        if not isinstance(snapshot, dict) or set(snapshot) != set(expected):
            return False
        if snapshot["index"] != offset + 1 or not inventory_shape_good(snapshot["inventory"]):
            return False
        records = snapshot["records"]
        if not isinstance(records, list) or len(records) != 4:
            return False
        if any(
            not observation_shape_good(records[index], name)
            for index, name in enumerate(CANDIDATE_NAMES)
        ):
            return False
        evidence_record = meta["evidence_initial"] if offset < 2 else meta["evidence_terminal"]
        if any(
            record["exact"] == 1
            and (
                evidence_record["state"] != "present"
                or record["dev"] != evidence_record["dev"]
            )
            for record in records
        ):
            return False
        unknown = tuple(
            name for name in snapshot["inventory"]["names"] if name not in CANDIDATE_NAMES
        )
        duplicates, aliases = relation_lists(records, source)
        anomalies = snapshot_anomalies(snapshot)
        if snapshot["unknown_names"] != unknown:
            return False
        if snapshot["duplicates"] != duplicates or len(duplicates) > DUPLICATE_CAP:
            return False
        if snapshot["aliases"] != aliases or len(aliases) > ALIAS_CAP:
            return False
        if snapshot["anomalies"] != anomalies:
            return False
        if not bounded_bytes_tuple(unknown, UNKNOWN_RECORD_CAP, INVENTORY_RAW_CAP):
            return False
        if not bounded_token_tuple(anomalies, SNAPSHOT_ANOMALY_CAP, SNAPSHOT_ANOMALY_TOKEN_CAP):
            return False
    bit_names = (
        "source_equal",
        "evidence_equal",
        "snapshots_equal",
        "inventories_complete",
        "post_inputs_reverified",
        "snapshot_1_attempt_complete",
        "snapshot_2_attempt_complete",
        "snapshot_3_attempt_complete",
        "snapshot_1_success",
        "snapshot_2_success",
        "snapshot_3_success",
        "snapshot_1_close_complete",
        "snapshot_2_close_complete",
        "snapshot_3_close_complete",
        "evidence_initial_close_complete",
        "evidence_terminal_close_complete",
        "evidence_initial_path_finalized_after_bracket",
        "evidence_terminal_path_finalized_after_bracket",
        "pass_seen",
        "errors_truncated",
    )
    if any(meta[key] not in (0, 1) for key in bit_names):
        return False
    if mode in ("recovery", "recovery-binder") and meta["pass_seen"] != 0:
        return False
    if any(meta[key] not in ESRCH_STATES for key in ("recovery_first_esrch", "recovery_second_esrch", "recovery_third_esrch")):
        return False
    if meta["base_status"] not in BASE_STATUS_STATES or meta["proposed_phase"] not in PHASE_STATES:
        return False
    if not isinstance(meta["errors"], list) or len(meta["errors"]) > 32:
        return False
    if (
        len(set(meta["errors"])) != len(meta["errors"])
        or any(value not in SCHEMA_ERROR_TOKENS for value in meta["errors"])
    ):
        return False
    expected_unknown = tuple(sorted(set(
        name for snapshot in snapshots for name in snapshot["unknown_names"]
    )))
    expected_duplicate = tuple(sorted(set(
        value for snapshot in snapshots for value in snapshot["duplicates"]
    )))
    expected_alias = tuple(sorted(set(
        value for snapshot in snapshots for value in snapshot["aliases"]
    )))
    expected_global = construct_global_anomalies(meta)
    expected_anomaly = tuple(sorted(set(
        list(expected_global)
        + [
            "snapshot-" + str(snapshot["index"]) + "-" + value
            for snapshot in snapshots
            for value in snapshot["anomalies"]
        ]
    )))
    expected_source_equal = int(
        observation_signature(meta["source_initial"])
        == observation_signature(meta["source_terminal"])
    )
    expected_evidence_equal = int(
        meta["evidence_initial_path_finalized_after_bracket"] == 1
        and meta["evidence_terminal_path_finalized_after_bracket"] == 1
        and observation_signature(meta["evidence_initial"])
        == observation_signature(meta["evidence_terminal"])
    )
    expected_snapshots_equal = int(
        snapshot_signature(snapshots[0])
        == snapshot_signature(snapshots[1])
        == snapshot_signature(snapshots[2])
    )
    expected_inventories_complete = int(
        all(snapshot["inventory"]["complete"] == 1 for snapshot in snapshots)
    )
    expected_base_status = (
        "ok"
        if (
            meta["post_inputs_reverified"] == 1
            and not CLOSE_FAILED
            and not meta["errors"]
            and not meta["errors_truncated"]
        )
        else "error"
    )
    expected_phase = classify_phase(
        meta,
        meta["mode"] in ("recovery", "recovery-binder"),
        meta["pass_seen"] == 1,
    )
    return (
        meta["source_equal"] == expected_source_equal
        and meta["evidence_equal"] == expected_evidence_equal
        and meta["snapshots_equal"] == expected_snapshots_equal
        and meta["inventories_complete"] == expected_inventories_complete
        and meta["evidence_initial_path_finalized_after_bracket"]
        == meta["evidence_initial"]["path_finalized_after_bracket"]
        and meta["evidence_terminal_path_finalized_after_bracket"]
        == meta["evidence_terminal"]["path_finalized_after_bracket"]
        and meta["base_status"] == expected_base_status
        and meta["proposed_phase"] == expected_phase
        and meta["unknown_union"] == expected_unknown
        and bounded_bytes_tuple(expected_unknown, UNKNOWN_UNION_COUNT_CAP, UNKNOWN_UNION_RAW_CAP)
        and meta["duplicate_union"] == expected_duplicate
        and bounded_token_tuple(expected_duplicate, DUPLICATE_CAP, 3)
        and meta["alias_union"] == expected_alias
        and bounded_token_tuple(expected_alias, ALIAS_CAP, 1)
        and meta["global_anomalies"] == expected_global
        and bounded_token_tuple(expected_global, GLOBAL_ANOMALY_CAP, GLOBAL_ANOMALY_TOKEN_CAP)
        and meta["anomaly_union"] == expected_anomaly
        and bounded_token_tuple(expected_anomaly, ANOMALY_UNION_CAP, ANOMALY_UNION_TOKEN_CAP)
    )

def sanitize_observation(record, expected_name, meta):
    template = empty_observation(expected_name)
    if not isinstance(record, dict) or set(record) != set(template):
        return False
    original_signature = observation_signature(record)
    malformed = False
    if record["name"] != expected_name:
        record["name"] = expected_name
        malformed = True
    flag_names = (
        "terminal", "exact", "exact_absent", "stable", "path_fd_opened",
        "directory_fd_opened", "path_finalized_after_bracket",
        "fresh_chain_attempt_complete", "fresh_chain_open_complete",
        "fresh_chain_equal", "fresh_path_stat_complete", "fresh_path_fd_opened",
        "fresh_path_fd_equal", "fresh_directory_fd_opened",
        "fresh_directory_fd_equal", "fresh_final_stat_complete",
        "fresh_identity_equal", "fresh_chain_close_complete",
    )
    for name in flag_names:
        if record[name] not in (0, 1):
            record[name] = 0
            malformed = True
    for name, allowed, sentinel in (
        ("state", OBSERVATION_STATES, "error"),
        ("final_state", OBSERVATION_STATES, "error"),
        ("absence", ABSENCE_STATES, "none"),
        ("final_absence", ABSENCE_STATES, "none"),
        ("type", TYPE_STATES, "none"),
        ("final_type", TYPE_STATES, "none"),
        ("content", CONTENT_STATES, "unavailable"),
    ):
        if record[name] not in allowed:
            record[name] = sentinel
            malformed = True
    for name in ("error", "final_error"):
        if record[name] not in OBSERVATION_ERROR_TOKENS:
            record[name] = "schema-malformed"
            malformed = True
    for name in ("dev", "ino", "nlink", "uid", "gid", "rdev", "bytes", "lf", "final_dev", "final_ino", "final_nlink", "final_uid", "final_gid", "final_rdev", "final_bytes"):
        if not canonical_u64_text(record[name]):
            record[name] = "none"
            malformed = True
    for name in ("mode", "final_mode"):
        if not canonical_mode_text(record[name]):
            record[name] = "none"
            malformed = True
    if not canonical_hash_text(record["sha"]):
        record["sha"] = "none"
        malformed = True
    if not node_key_good(record["key"]) and record["key"] is not None:
        record["key"] = None
        malformed = True
    if not node_key_good(record["final_key"]) and record["final_key"] is not None:
        record["final_key"] = None
        malformed = True
    if record["state"] == "present" and not key_matches_scalars(record, ""):
        values = (
            record["dev"], record["ino"], record["mode"], record["nlink"],
            record["uid"], record["gid"], record["rdev"], record["bytes"],
        )
        if (
            all(canonical_u64_text(item, ()) for index, item in enumerate(values) if index != 2)
            and canonical_mode_text(values[2])
            and values[2] != "none"
        ):
            record["key"] = (
                int(values[0]), int(values[1]), int(values[2], 8), int(values[3]),
                int(values[4]), int(values[5]), int(values[6]), int(values[7]),
            )
        else:
            record["state"] = "error"
            record["type"] = "none"
            record["content"] = "unavailable"
            record["absence"] = "none"
            record["key"] = None
            for name in ("dev", "ino", "mode", "nlink", "uid", "gid", "rdev", "bytes"):
                record[name] = "none"
        malformed = True
    if record["final_state"] == "present" and not key_matches_scalars(record, "final_"):
        values = (
            record["final_dev"], record["final_ino"], record["final_mode"],
            record["final_nlink"], record["final_uid"], record["final_gid"],
            record["final_rdev"], record["final_bytes"],
        )
        if (
            all(canonical_u64_text(item, ()) for index, item in enumerate(values) if index != 2)
            and canonical_mode_text(values[2])
            and values[2] != "none"
        ):
            record["final_key"] = (
                int(values[0]), int(values[1]), int(values[2], 8), int(values[3]),
                int(values[4]), int(values[5]), int(values[6]), int(values[7]),
            )
        else:
            record["final_state"] = "error"
            record["final_type"] = "none"
            record["final_absence"] = "none"
            record["final_key"] = None
            for name in (
                "final_dev", "final_ino", "final_mode", "final_nlink",
                "final_uid", "final_gid", "final_rdev", "final_bytes",
            ):
                record[name] = "none"
        malformed = True
    for name in ("opening_chain_signature", "fresh_chain_signature"):
        value = record[name]
        if not isinstance(value, tuple) or len(value) != CHAIN_COMPONENT_COUNT:
            record[name] = (None,) * CHAIN_COMPONENT_COUNT
            malformed = True
        else:
            cleaned = tuple(item if node_key_good(item) else None for item in value)
            malformed = malformed or cleaned != value
            record[name] = cleaned
    owned = record["fds"] if isinstance(record["fds"], list) else []
    extra_owned = [record["path_fd"], record["dir_fd"]]
    if (
        not isinstance(record["fds"], list)
        or owned
        or any(value is not None for value in extra_owned)
        or record["directory_key"] is not None
    ):
        malformed = True
    closed_once = set()
    for value in reversed(owned + extra_owned):
        if type(value) is int and value in OPEN_FDS and value not in closed_once:
            close_fd(value, "candidate-close")
            closed_once.add(value)
    record["path_fd"] = None
    record["dir_fd"] = None
    record["directory_key"] = None
    record["fds"] = []
    if record["state"] == "absent":
        record["absence"] = "ENOENT"
        record["type"] = "none"
        record["content"] = "absent"
        record["key"] = None
        record["lf"] = "none"
        record["sha"] = "none"
        record["terminal"] = 0
        for name in ("dev", "ino", "mode", "nlink", "uid", "gid", "rdev", "bytes"):
            record[name] = "none"
    elif record["state"] in ("error", "unavailable"):
        record["absence"] = "none"
        record["type"] = "none"
        record["content"] = "unavailable"
        record["key"] = None
        record["lf"] = "none"
        record["sha"] = "none"
        record["terminal"] = 0
        for name in ("dev", "ino", "mode", "nlink", "uid", "gid", "rdev", "bytes"):
            record[name] = "none"
    elif record["type"] == "none":
        record["state"] = "error"
        record["content"] = "unavailable"
        record["key"] = None
        record["lf"] = "none"
        record["sha"] = "none"
        record["terminal"] = 0
        for name in ("dev", "ino", "mode", "nlink", "uid", "gid", "rdev", "bytes"):
            record[name] = "none"
        malformed = True
    elif expected_name == EVIDENCE_NAME:
        if record["type"] == "directory":
            if record["content"] not in ("metadata-only", "directory-observed"):
                record["content"] = "directory-observed"
        elif record["content"] not in ("metadata-only", "unavailable-nondirectory"):
            record["content"] = "unavailable-nondirectory"
    elif record["type"] == "regular":
        if record["content"] not in (
            "unavailable", "unavailable-size-cap", "complete", "read-error"
        ):
            record["content"] = "unavailable"
    else:
        record["content"] = "unavailable-nonregular"
    if record["content"] != "complete":
        record["lf"] = "none"
        record["sha"] = "none"
        record["terminal"] = 0
    elif (
        record["lf"] == "none"
        or record["sha"] == "none"
        or record["bytes"] == "none"
        or int(record["lf"]) > int(record["bytes"])
    ):
        record["content"] = "read-error"
        record["lf"] = "none"
        record["sha"] = "none"
        record["terminal"] = 0
        malformed = True
    if expected_name != SOURCE_NAME and record["terminal"] != 0:
        record["terminal"] = 0
        malformed = True
    if record["final_state"] == "absent":
        record["final_absence"] = "ENOENT"
        record["final_type"] = "none"
        record["final_key"] = None
        for name in (
            "final_dev", "final_ino", "final_mode", "final_nlink",
            "final_uid", "final_gid", "final_rdev", "final_bytes",
        ):
            record[name] = "none"
    elif record["final_state"] in ("error", "unavailable"):
        record["final_absence"] = "none"
        record["final_type"] = "none"
        record["final_key"] = None
        for name in (
            "final_dev", "final_ino", "final_mode", "final_nlink",
            "final_uid", "final_gid", "final_rdev", "final_bytes",
        ):
            record[name] = "none"
    elif record["final_type"] == "none":
        record["final_state"] = "error"
        record["final_key"] = None
        for name in (
            "final_dev", "final_ino", "final_mode", "final_nlink",
            "final_uid", "final_gid", "final_rdev", "final_bytes",
        ):
            record[name] = "none"
        malformed = True
    if expected_name != EVIDENCE_NAME:
        for name in (
            "directory_fd_opened", "path_finalized_after_bracket",
            "fresh_chain_attempt_complete", "fresh_chain_open_complete",
            "fresh_chain_equal", "fresh_path_stat_complete",
            "fresh_path_fd_opened", "fresh_path_fd_equal",
            "fresh_directory_fd_opened", "fresh_directory_fd_equal",
            "fresh_final_stat_complete", "fresh_identity_equal",
            "fresh_chain_close_complete",
        ):
            if record[name] != 0:
                record[name] = 0
                malformed = True
        if any(item is not None for item in record["opening_chain_signature"]):
            record["opening_chain_signature"] = (None,) * CHAIN_COMPONENT_COUNT
            malformed = True
        if any(item is not None for item in record["fresh_chain_signature"]):
            record["fresh_chain_signature"] = (None,) * CHAIN_COMPONENT_COUNT
            malformed = True
    if record["state"] != "present" and record["path_fd_opened"] != 0:
        malformed = True
    if record["directory_fd_opened"] == 1 and not (
        expected_name == EVIDENCE_NAME
        and record["state"] == "present"
        and record["type"] == "directory"
    ):
        malformed = True
    fresh_dependents = (
        "fresh_chain_open_complete", "fresh_chain_equal",
        "fresh_path_stat_complete", "fresh_path_fd_opened",
        "fresh_path_fd_equal", "fresh_directory_fd_opened",
        "fresh_directory_fd_equal", "fresh_final_stat_complete",
        "fresh_identity_equal", "fresh_chain_close_complete",
    )
    if record["fresh_chain_attempt_complete"] == 0:
        if any(record[name] != 0 for name in fresh_dependents):
            malformed = True
        if any(item is not None for item in record["fresh_chain_signature"]):
            malformed = True
    if record["fresh_chain_equal"] == 1 and not (
        record["fresh_chain_open_complete"] == 1
        and all(node_key_good(item) for item in record["opening_chain_signature"])
        and record["opening_chain_signature"] == record["fresh_chain_signature"]
    ):
        record["fresh_chain_equal"] = 0
        malformed = True
    if record["fresh_path_fd_equal"] == 1 and not (
        record["fresh_path_stat_complete"] == 1
        and record["fresh_path_fd_opened"] == 1
    ):
        record["fresh_path_fd_equal"] = 0
        malformed = True
    if record["fresh_directory_fd_equal"] == 1 and not (
        record["fresh_path_stat_complete"] == 1
        and record["fresh_directory_fd_opened"] == 1
    ):
        record["fresh_directory_fd_equal"] = 0
        malformed = True
    malformed = malformed or observation_signature(record) != original_signature
    if malformed or not observation_semantics_good(record, expected_name):
        record["exact"] = 0
        record["exact_absent"] = 0
        record["stable"] = 0
        record["path_finalized_after_bracket"] = 0
        record["fresh_chain_equal"] = 0
        record["fresh_identity_equal"] = 0
        record["error"] = "schema-malformed"
        record["final_error"] = "schema-malformed"
        schema_error(meta, "schema-malformed")
    return True

def sanitize_schema(meta):
    if validate_schema_shape(meta):
        return True
    if not isinstance(meta, dict):
        return False
    mode = meta.get("mode")
    if mode not in MODE_STATES:
        mode = "recovery-binder"
    template = new_audit_schema(mode)
    if set(meta) != set(template):
        return False
    meta["mode"] = mode
    incoming_errors = meta["errors"] if isinstance(meta["errors"], list) else []
    incoming_error_problem = (
        not isinstance(meta["errors"], list)
        or len(incoming_errors) > 32
        or len(set(
            value if value in SCHEMA_ERROR_TOKENS else "unexpected"
            for value in incoming_errors[:32]
        )) != len(incoming_errors[:32])
        or any(value not in SCHEMA_ERROR_TOKENS for value in incoming_errors[:32])
        or meta["errors_truncated"] not in (0, 1)
    )
    meta["errors"] = []
    meta["errors_truncated"] = int(
        meta["errors_truncated"] == 1 or len(incoming_errors) > 32
    )
    for value in incoming_errors[:32]:
        schema_error(meta, value)
    if incoming_error_problem:
        schema_error(meta, "schema-malformed")
    for key, name in (
        ("source_initial", SOURCE_NAME),
        ("source_terminal", SOURCE_NAME),
        ("evidence_initial", EVIDENCE_NAME),
        ("evidence_terminal", EVIDENCE_NAME),
    ):
        if not sanitize_observation(meta[key], name, meta):
            return False
    snapshots = meta["snapshots"]
    if not isinstance(snapshots, list) or len(snapshots) != 3:
        return False
    for offset, snapshot in enumerate(snapshots):
        expected = unavailable_snapshot(offset + 1, "unexpected")
        if not isinstance(snapshot, dict) or set(snapshot) != set(expected):
            return False
        snapshot["index"] = offset + 1
        inventory = snapshot["inventory"]
        if not isinstance(inventory, dict) or set(inventory) != set(new_inventory()):
            return False
        if not isinstance(inventory["reason_bits"], dict) or tuple(inventory["reason_bits"]) != INVENTORY_REASON_ORDER:
            return False
        inventory_was_good = inventory_shape_good(inventory)
        names = inventory["names"] if isinstance(inventory["names"], tuple) else ()
        if len(names) > INVENTORY_ITEMS_CAP + 1:
            names = names[:INVENTORY_ITEMS_CAP + 1]
            inventory["reason_bits"]["item-cap"] = 1
            inventory["reason_truncated"] = 1
            inventory["complete"] = 0
            schema_error(meta, "schema-malformed")
        cleaned = tuple(sorted(set(name for name in names if basename_good(name))))
        if cleaned != names or sum(len(name) for name in cleaned) > INVENTORY_RAW_CAP:
            inventory["reason_bits"]["name-invalid"] = 1
            inventory["complete"] = 0
            schema_error(meta, "schema-malformed")
            rejected = next(
                (
                    name for name in names
                    if isinstance(name, bytes) and (
                        not basename_good(name) or names.count(name) > 1
                    )
                ),
                None,
            )
            if rejected is not None:
                inventory["overflow_bytes"] = str(len(rejected))
                inventory["overflow_sha"] = sha(rejected)
            else:
                inventory["reason_truncated"] = 1
            while sum(len(name) for name in cleaned) > INVENTORY_RAW_CAP:
                rejected = cleaned[-1]
                inventory["overflow_bytes"] = str(len(rejected))
                inventory["overflow_sha"] = sha(rejected)
                cleaned = cleaned[:-1]
        if len(cleaned) > INVENTORY_ITEMS_CAP:
            inventory["reason_bits"]["item-cap"] = 1
            inventory["complete"] = 0
            schema_error(meta, "schema-malformed")
            inventory["overflow_bytes"] = str(len(cleaned[INVENTORY_ITEMS_CAP]))
            inventory["overflow_sha"] = sha(cleaned[INVENTORY_ITEMS_CAP])
            cleaned = cleaned[:INVENTORY_ITEMS_CAP]
        inventory["names"] = cleaned[:INVENTORY_ITEMS_CAP]
        inventory["frame"] = canonical_inventory_frame(inventory["names"])
        for reason in INVENTORY_REASON_ORDER:
            inventory["reason_bits"][reason] = int(inventory["reason_bits"][reason] == 1)
        inventory["reason_truncated"] = int(inventory["reason_truncated"] == 1)
        inventory["complete"] = int(
            inventory["reason_truncated"] == 0
            and not any(inventory["reason_bits"].values())
        )
        if not canonical_u64_text(inventory["overflow_bytes"]):
            inventory["overflow_bytes"] = "none"
        if not canonical_hash_text(inventory["overflow_sha"]):
            inventory["overflow_sha"] = "none"
        if not (
            inventory["overflow_bytes"] == "none"
            and inventory["overflow_sha"] == "none"
            or inventory["overflow_bytes"] != "none"
            and inventory["overflow_sha"] != "none"
            and int(inventory["overflow_bytes"]) >= 1
        ):
            inventory["overflow_bytes"] = "none"
            inventory["overflow_sha"] = "none"
            inventory["reason_truncated"] = 1
        if not inventory_was_good:
            inventory["reason_bits"]["unexpected"] = 1
            inventory["complete"] = 0
            meta["snapshot_" + str(offset + 1) + "_success"] = 0
            schema_error(meta, "schema-malformed")
        records = snapshot["records"]
        if not isinstance(records, list) or len(records) != 4:
            return False
        records_were_good = all(
            observation_shape_good(records[index], name)
            for index, name in enumerate(CANDIDATE_NAMES)
        )
        for index, name in enumerate(CANDIDATE_NAMES):
            if not sanitize_observation(records[index], name, meta):
                return False
        evidence_record = meta["evidence_initial"] if offset < 2 else meta["evidence_terminal"]
        for record in records:
            if record["exact"] == 1 and (
                evidence_record["state"] != "present"
                or record["dev"] != evidence_record["dev"]
            ):
                record["exact"] = 0
                record["exact_absent"] = 0
                record["stable"] = 0
                record["error"] = "schema-malformed"
                record["final_error"] = "schema-malformed"
                records_were_good = False
                schema_error(meta, "schema-malformed")
        if not records_were_good:
            meta["snapshot_" + str(offset + 1) + "_success"] = 0
        snapshot["unknown_names"] = tuple(
            name for name in inventory["names"] if name not in CANDIDATE_NAMES
        )
        snapshot["duplicates"], snapshot["aliases"] = relation_lists(
            records, meta["source_initial"]
        )
        snapshot["anomalies"] = snapshot_anomalies(snapshot)
    for name in (
        "source_equal", "evidence_equal", "snapshots_equal", "inventories_complete",
        "post_inputs_reverified", "snapshot_1_attempt_complete",
        "snapshot_2_attempt_complete", "snapshot_3_attempt_complete",
        "snapshot_1_success", "snapshot_2_success", "snapshot_3_success",
        "snapshot_1_close_complete", "snapshot_2_close_complete",
        "snapshot_3_close_complete", "evidence_initial_close_complete",
        "evidence_terminal_close_complete",
        "evidence_initial_path_finalized_after_bracket",
        "evidence_terminal_path_finalized_after_bracket", "errors_truncated",
        "pass_seen",
    ):
        meta[name] = int(meta[name] == 1)
    if meta["mode"] in ("recovery", "recovery-binder") and meta["pass_seen"] != 0:
        meta["pass_seen"] = 0
        schema_error(meta, "schema-malformed")
    for name in ("recovery_first_esrch", "recovery_second_esrch", "recovery_third_esrch"):
        if meta[name] not in ESRCH_STATES:
            meta[name] = "0"
    schema_error(meta, "schema-malformed")
    meta["base_status"] = "error"
    meta["proposed_phase"] = "unknown-mismatch"
    derive_schema(
        meta,
        meta["mode"] in ("recovery", "recovery-binder"),
        meta["pass_seen"] == 1,
    )
    meta["base_status"] = "error"
    meta["proposed_phase"] = "unknown-mismatch"
    return validate_schema_shape(meta)

def serialize_schema(meta):
    need(validate_schema_shape(meta), "schema-shape")
    unknown_union_frame = canonical_inventory_frame(meta["unknown_union"])
    anomaly_union_frame = b"".join(
        value.encode("ascii") + b"\n" for value in meta["anomaly_union"]
    )
    schema_header = (
        b"AUDIT_SCHEMA version=5 layout=fixed source=2 evidence=2 "
        b"inventory=3 candidate=12 chain=28\n"
    )
    need(len(schema_header) <= SCHEMA_HEADER_CAP, "schema-header-cap")
    parts = [
        schema_header,
        observation_line("SOURCE", "initial", meta["source_initial"]),
        observation_line("SOURCE", "terminal", meta["source_terminal"]),
        observation_line("EVIDENCE", "initial", meta["evidence_initial"]),
        observation_line("EVIDENCE", "terminal", meta["evidence_terminal"]),
    ]
    chain_count = 0
    for bracket, record in (
        ("initial", meta["evidence_initial"]),
        ("terminal", meta["evidence_terminal"]),
    ):
        for generation, signature in (
            ("opening", record["opening_chain_signature"]),
            ("fresh", record["fresh_chain_signature"]),
        ):
            need(chain_signature_good(signature), "chain-signature-shape")
            for index, key in enumerate(signature):
                parts.append(chain_component_line(bracket, generation, index, key))
                chain_count += 1
    need(chain_count == 28, "chain-component-count")
    for snapshot in meta["snapshots"]:
        parts.append(inventory_line(snapshot))
        for name_index, name in enumerate(snapshot["unknown_names"]):
            line = (
                "UNKNOWN_CHILD snapshot="
                + str(snapshot["index"])
                + " index="
                + str(name_index)
                + " name_hex="
                + name.hex()
                + " observation=name-only opened=0\n"
            ).encode("ascii")
            need(len(line) <= UNKNOWN_LINE_CAP, "unknown-line-cap")
            parts.append(line)
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
            line = (
                "ANOMALY snapshot="
                + str(snapshot["index"])
                + " index="
                + str(anomaly_index)
                + " token="
                + value
                + "\n"
            ).encode("ascii")
            need(len(line) <= SNAPSHOT_ANOMALY_LINE_CAP, "snapshot-anomaly-line-cap")
            parts.append(line)
    cross = (
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
        + " snapshot_1_success="
        + str(meta["snapshot_1_success"])
        + " snapshot_2_success="
        + str(meta["snapshot_2_success"])
        + " snapshot_3_success="
        + str(meta["snapshot_3_success"])
        + " snapshot_1_close_complete="
        + str(meta["snapshot_1_close_complete"])
        + " snapshot_2_close_complete="
        + str(meta["snapshot_2_close_complete"])
        + " snapshot_3_close_complete="
        + str(meta["snapshot_3_close_complete"])
        + " evidence_initial_close_complete="
        + str(meta["evidence_initial_close_complete"])
        + " evidence_terminal_close_complete="
        + str(meta["evidence_terminal_close_complete"])
        + " pass_seen="
        + str(meta["pass_seen"])
        + " evidence_initial_path_finalized_after_bracket="
        + str(meta["evidence_initial_path_finalized_after_bracket"])
        + " evidence_terminal_path_finalized_after_bracket="
        + str(meta["evidence_terminal_path_finalized_after_bracket"])
        + "\n"
    ).encode("ascii")
    need(len(cross) <= CROSS_LINE_CAP, "cross-line-cap")
    parts.append(cross)
    for anomaly_index, value in enumerate(meta["global_anomalies"]):
        line = (
            "GLOBAL_ANOMALY index="
            + str(anomaly_index)
            + " token="
            + value
            + "\n"
        ).encode("ascii")
        need(len(line) <= GLOBAL_ANOMALY_LINE_CAP, "global-anomaly-line-cap")
        parts.append(line)
    union = (
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
    need(len(union) <= UNION_LINE_CAP, "union-line-cap")
    parts.append(union)
    reverify = (
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
    need(len(reverify) <= REVERIFY_LINE_CAP, "reverify-line-cap")
    parts.append(reverify)
    return b"".join(parts)

def binder_observe(inputs, meta, recovery, pass_seen, evidence_allowed):
    parent = None
    terminal_parent = None
    evidence_initial = None
    evidence_terminal = None
    snapshots = meta["snapshots"]
    if evidence_allowed:
        try:
            parent = ObservedChain(EVIDENCE_PARENT_COMPONENTS)
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
                evidence_initial["directory_key"],
                int(evidence_initial["dev"]),
                snapshots[0],
            )
            meta["snapshot_1_success"] = 1
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
                evidence_initial["directory_key"],
                int(evidence_initial["dev"]),
                snapshots[1],
            )
            meta["snapshot_2_success"] = 1
    except BaseException as error:
        schema_error(meta, error.code if isinstance(error, Stop) else "snapshot-2-unexpected")
    finally:
        meta["snapshot_2_attempt_complete"] = 1
    if evidence_initial is not None and parent is not None:
        try:
            finish_evidence(evidence_initial)
        except BaseException:
            schema_error(meta, "evidence-initial-finish")
        finally:
            meta["evidence_initial_path_finalized_after_bracket"] = evidence_initial[
                "path_finalized_after_bracket"
            ]
    if evidence_allowed:
        try:
            terminal_parent = ObservedChain(EVIDENCE_PARENT_COMPONENTS)
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
                evidence_terminal["directory_key"],
                int(evidence_terminal["dev"]),
                snapshots[2],
            )
            meta["snapshot_3_success"] = 1
    except BaseException as error:
        schema_error(meta, error.code if isinstance(error, Stop) else "snapshot-3-unexpected")
    finally:
        meta["snapshot_3_attempt_complete"] = 1
    if evidence_terminal is not None and terminal_parent is not None:
        try:
            finish_evidence(evidence_terminal)
        except BaseException:
            schema_error(meta, "evidence-terminal-finish")
        finally:
            meta["evidence_terminal_path_finalized_after_bracket"] = evidence_terminal[
                "path_finalized_after_bracket"
            ]
    for snapshot in reversed(snapshots):
        try:
            meta["snapshot_" + str(snapshot["index"]) + "_close_complete"] = int(
                close_snapshot(snapshot)
            )
        except BaseException:
            schema_error(meta, "snapshot-close")
    if evidence_terminal is not None:
        try:
            meta["evidence_terminal_close_complete"] = int(
                close_evidence(evidence_terminal)
            )
        except BaseException:
            schema_error(meta, "evidence-terminal-close")
    if evidence_initial is not None:
        try:
            meta["evidence_initial_close_complete"] = int(
                close_evidence(evidence_initial)
            )
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
    need(
        validate_schema_shape(meta)
        and status in BASE_STATUS_STATES
        and phase in PHASE_STATES,
        "binder-header-fields",
    )
    sites = ",".join(CLOSE_FAILURE_SITES) if CLOSE_FAILURE_SITES else "none"
    value = (
        "BINDER version=5 schema-layout=full status="
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
    need(len(value) <= BINDER_HEADER_CAP, "binder-header-cap")
    return value

def schema_layout_failure(kind, recovery):
    need(kind in ("outer-layout", "leaf-layout", "serializer", "impossible-overflow"), "layout-kind")
    mode = "recovery-binder" if recovery else "watchdog"
    value = (
        "BINDER version=5 schema-layout=failure status=error mode="
        + mode
        + " durability_phase=unknown-mismatch failure="
        + kind
        + "\nSCHEMA_LAYOUT_FAILURE status=PERMANENT_FAILURE\n"
        + "PROVENANCE status_receipt=payload-created-synthetic-nonauthoritative "
        + ("wait_provenance=unavailable-recovery stream_provenance=unavailable-recovery\n" if recovery else "wait_provenance=watchdog-waitpid-authoritative stream_provenance=watchdog-separate-raw-pipes\n")
        + "BINDER_END\n"
    ).encode("ascii")
    need(len(value) <= BINDER_WORST and len(value) <= BINDER_CAP, "layout-failure-cap")
    return value, "error", "unknown-mismatch"

def render_binder(meta, recovery):
    if not validate_schema_shape(meta):
        try:
            sanitized = sanitize_schema(meta)
        except BaseException:
            sanitized = False
        if not sanitized:
            return schema_layout_failure("outer-layout", recovery)
    if not validate_schema_shape(meta):
        return schema_layout_failure("leaf-layout", recovery)
    try:
        body = serialize_schema(meta)
    except BaseException:
        return schema_layout_failure("serializer", recovery)
    status = meta["base_status"]
    phase = meta["proposed_phase"]
    if (
        status == "error"
        or meta["inventories_complete"] != 1
        or meta["snapshots_equal"] != 1
        or meta["source_equal"] != 1
        or meta["evidence_equal"] != 1
        or meta["post_inputs_reverified"] != 1
        or any(
            meta[name] != 1
            for name in (
                "snapshot_1_attempt_complete", "snapshot_2_attempt_complete",
                "snapshot_3_attempt_complete", "snapshot_1_success",
                "snapshot_2_success", "snapshot_3_success",
                "snapshot_1_close_complete", "snapshot_2_close_complete",
                "snapshot_3_close_complete", "evidence_initial_close_complete",
                "evidence_terminal_close_complete",
                "evidence_initial_path_finalized_after_bracket",
                "evidence_terminal_path_finalized_after_bracket",
            )
        )
        or CLOSE_FAILED
        or recovery
    ):
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
    need(len(provenance) <= PROVENANCE_CAP, "provenance-cap")
    end = b"BINDER_END\n"
    need(len(end) <= BINDER_END_CAP, "binder-end-cap")
    report = binder_header(meta, status, phase) + body + provenance + end
    if len(report) > BINDER_WORST:
        return schema_layout_failure("impossible-overflow", recovery)
    need(len(report) <= BINDER_CAP, "binder-cap")
    return report, status, phase

def checked_u64_add(left, right, code):
    need(type(left) is int and type(right) is int, code)
    need(0 <= left <= UINT64_MAX and 0 <= right <= UINT64_MAX, code)
    need(left <= UINT64_MAX - right, code)
    return left + right

class WaitObservation(tuple):
    __slots__ = ()

    def __new__(
        cls,
        outcome,
        origin,
        guard_deadline_ns,
        wait_called,
        observed_ns,
        physical_reap,
        timely,
        raw_status,
        error_token,
    ):
        need(
            type(guard_deadline_ns) is int
            and type(observed_ns) is int
            and 0 <= guard_deadline_ns <= UINT64_MAX
            and 0 <= observed_ns <= UINT64_MAX,
            "wait-observation-u64",
        )
        need(wait_called in (0, 1) and physical_reap in (0, 1) and timely in (0, 1), "wait-observation-bits")
        need(
            raw_status is None
            or (type(raw_status) is int and 0 <= raw_status <= UINT64_MAX),
            "wait-observation-status",
        )
        need(
            outcome in ("guard-expired", "interrupted", "error", "reaped", "empty", "other")
            and origin in ("payload-wait", "kill-reap", "cleanup")
            and error_token in (
                "none", "payload-wait-error", "payload-wait-other",
                "kill-reap-error", "kill-reap-other",
                "cleanup-error", "cleanup-other",
            ),
            "wait-observation-enum",
        )
        stream_deadline_ns = None
        if physical_reap:
            stream_deadline_ns = checked_u64_add(
                observed_ns,
                PIPE_EOF_GRACE_NS,
                "stream-eof-deadline-overflow",
            )
        return tuple.__new__(
            cls,
            (
                outcome,
                origin,
                guard_deadline_ns,
                wait_called,
                observed_ns,
                physical_reap,
                timely,
                raw_status,
                stream_deadline_ns,
                error_token,
            ),
        )

    outcome = property(lambda value: value[0])
    origin = property(lambda value: value[1])
    guard_deadline_ns = property(lambda value: value[2])
    wait_called = property(lambda value: value[3])
    observed_ns = property(lambda value: value[4])
    physical_reap = property(lambda value: value[5])
    timely = property(lambda value: value[6])
    raw_status = property(lambda value: value[7])
    stream_eof_deadline_ns = property(lambda value: value[8])
    error_token = property(lambda value: value[9])

def guarded_wait_once(pid, deadline, origin):
    before = time.monotonic_ns()
    if before >= deadline:
        return WaitObservation(
            "guard-expired", origin, deadline, 0, before, 0, 0, None, "none"
        )
    try:
        got, status_value = os.waitpid(pid, os.WNOHANG)
        observed = time.monotonic_ns()
    except InterruptedError:
        observed = time.monotonic_ns()
        return WaitObservation(
            "interrupted",
            origin,
            deadline,
            1,
            observed,
            0,
            int(observed < deadline),
            None,
            "none",
        )
    except BaseException:
        observed = time.monotonic_ns()
        return WaitObservation(
            "error",
            origin,
            deadline,
            1,
            observed,
            0,
            int(observed < deadline),
            None,
            origin + "-error",
        )
    timely = int(observed < deadline)
    if got == pid:
        return WaitObservation(
            "reaped",
            origin,
            deadline,
            1,
            observed,
            1,
            timely,
            status_value,
            "none",
        )
    if got == 0:
        return WaitObservation(
            "empty", origin, deadline, 1, observed, 0, timely, None, "none"
        )
    return WaitObservation(
        "other",
        origin,
        deadline,
        1,
        observed,
        0,
        timely,
        None,
        origin + "-other",
    )

def wait_deadline(pid, deadline, origin="cleanup"):
    while True:
        observation = guarded_wait_once(pid, deadline, origin)
        if observation.physical_reap or observation.outcome in (
            "guard-expired",
            "error",
            "other",
        ):
            return observation
        if not observation.timely:
            return observation
        remaining = deadline - observation.observed_ns
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

def begin_line(watchdog_pid, binding, ready_deadline, ack_deadline):
    supervisor_pid = os.getpid()
    need(supervisor_pid > 1 and watchdog_pid > 1, "pid")
    value = (
        "BEGIN E001_SUPERVISOR_BINDER_RECOVERY version=5 supervisor_pid="
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
        + " ready_guard_origin=immediately-before-watchdog-spawn"
        + " ready_deadline_ns="
        + str(ready_deadline)
        + " ack_guard_origin=immediately-before-begin"
        + " ack_deadline_ns="
        + str(ack_deadline)
        + " actor_deadline_semantics=sticky-external"
        + " attempt_consumed=0\n"
    ).encode("ascii")
    need(len(value) <= BEGIN_CAP, "begin-cap")
    return value

class EOFObservation(tuple):
    __slots__ = ()

    def __new__(cls, stream, phase, guard_deadline_ns, observed_ns, timely):
        need(
            type(guard_deadline_ns) is int
            and type(observed_ns) is int
            and 0 <= guard_deadline_ns <= UINT64_MAX
            and 0 <= observed_ns <= UINT64_MAX
            and timely in (0, 1),
            "eof-observation-shape",
        )
        need(
            stream in ("stdout", "stderr")
            and phase in ("PAYLOAD_WAIT", "KILL_REAP", "STREAM_EOF"),
            "eof-observation-enum",
        )
        return tuple.__new__(
            cls,
            (stream, phase, guard_deadline_ns, observed_ns, timely),
        )

    stream = property(lambda value: value[0])
    phase = property(lambda value: value[1])
    guard_deadline_ns = property(lambda value: value[2])
    observed_ns = property(lambda value: value[3])
    timely = property(lambda value: value[4])

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
        "capture_error_bits": {item: 0 for item in CAPTURE_ERROR_ORDER},
        "capture_errors_truncated": 0,
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
        "payload_deadline_ns": None,
        "kill_reap_deadline_ns": None,
        "stream_eof_deadline_ns": None,
        "payload_wait_observation": None,
        "kill_reap_wait_observation": None,
        "stdout_eof_observation": None,
        "stderr_eof_observation": None,
        "reap_origin": "none",
    }

def recovery_capture(pgid):
    state = empty_capture()
    for name in (
        "out_total", "err_total", "out_lf", "err_lf", "out_overflow",
        "err_overflow", "out_eof", "err_eof", "out_close_error",
        "err_close_error", "life_close_error", "timeout", "payload_spawned",
        "capture_state", "payload_deadline_fired", "kill_reap_deadline_fired",
        "stream_eof_deadline_fired", "payload_wait_observed",
        "payload_wait_timely", "kill_reap_wait_observed",
        "kill_reap_wait_timely", "stdout_eof_observed",
        "stdout_eof_timely", "stderr_eof_observed", "stderr_eof_timely",
        "child_reaped", "kill_sent", "capture_complete",
    ):
        state[name] = "unavailable"
    state["out_hash"] = None
    state["err_hash"] = None
    state["supervisor_lost"] = 1
    state["wait_raw"] = None
    state["wait_kind"] = "unavailable"
    state["exit_code"] = None
    state["signal"] = None
    state["core"] = "unavailable"
    state["recovery_pgid"] = str(pgid)
    state["wait_provenance"] = "unavailable-recovery"
    state["stream_provenance"] = "unavailable-recovery"
    state["streams_available"] = 0
    state["wait_available"] = 0
    state["recovery_esrch_initial"] = "1"
    state["recovery_esrch_pre_evidence"] = "1"
    state["recovery_esrch_terminal"] = "1"
    state["payload_deadline_ns"] = "unavailable"
    state["kill_reap_deadline_ns"] = "unavailable"
    state["stream_eof_deadline_ns"] = "unavailable"
    state["reap_origin"] = "unavailable"
    mark_capture_error(state, "watchdog-report-lost")
    return state

def mark_capture_error(state, value):
    if value in state["capture_error_bits"]:
        state["capture_error_bits"][value] = 1
    else:
        state["capture_error_bits"]["unexpected"] = 1
        state["capture_errors_truncated"] = 1

def capture_errors_text(state):
    values = [
        item for item in CAPTURE_ERROR_ORDER if state["capture_error_bits"][item]
    ]
    return ",".join(values) if values else "none"

def capture_error_any(state):
    return state["capture_errors_truncated"] == 1 or any(
        state["capture_error_bits"].values()
    )

def u64_accumulate(state, name, amount, error_token):
    current = state[name]
    if current > UINT64_MAX - amount:
        state[name] = UINT64_MAX
        mark_capture_error(state, error_token)
        return False
    state[name] = current + amount
    return True

def capture_piece(state, key, piece, cap):
    u64_accumulate(state, key + "_total", len(piece), key + "-counter-overflow")
    u64_accumulate(state, key + "_lf", piece.count(b"\n"), key + "-counter-overflow")
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
    if deadline is None or time.monotonic_ns() >= deadline:
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

def reduce_wait_observation(state, observation):
    need(type(observation) is WaitObservation, "wait-observation-type")
    if observation.error_token != "none":
        mark_capture_error(state, observation.error_token)
    if observation.origin == "payload-wait":
        state["payload_wait_observation"] = observation
    elif observation.origin == "kill-reap":
        state["kill_reap_wait_observation"] = observation
    if observation.physical_reap:
        state["child_reaped"] = 1
        state["wait_raw"] = observation.raw_status
        state["reap_origin"] = observation.origin
        state["stream_eof_deadline_ns"] = observation.stream_eof_deadline_ns
        if observation.origin == "payload-wait":
            state["payload_wait_observed"] = 1
            state["payload_wait_timely"] = observation.timely
        else:
            state["kill_reap_wait_observed"] = 1
            state["kill_reap_wait_timely"] = observation.timely
        if observation.timely:
            state["capture_state"] = "STREAM_EOF"
        else:
            bit = (
                "payload_deadline_fired"
                if observation.origin == "payload-wait"
                else "kill_reap_deadline_fired"
            )
            latch_capture_deadline(state, bit, observation.origin)
            state["capture_state"] = "UNSAFE"
    elif not observation.timely or observation.outcome == "guard-expired":
        bit = (
            "payload_deadline_fired"
            if observation.origin == "payload-wait"
            else "kill_reap_deadline_fired"
        )
        latch_capture_deadline(state, bit, observation.origin)
    elif observation.outcome in ("error", "other"):
        state["capture_state"] = "UNSAFE"

def capture_wait_once(pid, state, deadline, origin):
    observation = guarded_wait_once(pid, deadline, origin)
    reduce_wait_observation(state, observation)
    return observation

def capture_read_once(state, key, fd, poller, open_streams, phase, deadline, bit, code):
    if not capture_guard(state, deadline, bit, code):
        return
    try:
        piece = os.read(fd, CHUNK)
        observed = time.monotonic_ns()
    except BlockingIOError:
        observed = time.monotonic_ns()
        if observed >= deadline:
            latch_capture_deadline(state, bit, code)
        return
    except BaseException:
        observed = time.monotonic_ns()
        if observed >= deadline:
            latch_capture_deadline(state, bit, code)
        mark_capture_error(state, key + "-read")
        close_stream(state, key, fd, poller, open_streams)
        return
    timely = int(observed < deadline)
    if not timely:
        latch_capture_deadline(state, bit, code)
    if piece == b"":
        stream = "stdout" if key == "out" else "stderr"
        observation = EOFObservation(stream, phase, deadline, observed, timely)
        slot = stream + "_eof_observation"
        if state[slot] is None:
            state[slot] = observation
        else:
            mark_capture_error(state, "unexpected")
        state[key + "_eof"] = 1
        state[stream + "_eof_observed"] = 1
        state[stream + "_eof_timely"] = timely
        close_stream(state, key, fd, poller, open_streams)
    else:
        capture_piece(state, key, piece, STDOUT_CAP if key == "out" else STDERR_CAP)

def capture_lifeline_once(state, fd, poller, deadline, bit, code):
    if not capture_guard(state, deadline, bit, code):
        return
    try:
        piece = os.read(fd, CHUNK)
        observed = time.monotonic_ns()
    except BlockingIOError:
        observed = time.monotonic_ns()
        if observed >= deadline:
            latch_capture_deadline(state, bit, code)
        return
    except BaseException:
        observed = time.monotonic_ns()
        if observed >= deadline:
            latch_capture_deadline(state, bit, code)
        mark_capture_error(state, "lifeline-read")
        return
    if observed >= deadline:
        latch_capture_deadline(state, bit, code)
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
    if value is None:
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

def eof_observation_good(state, observation, expected_stream):
    reap = state["payload_wait_observation"]
    if type(observation) is not EOFObservation or type(reap) is not WaitObservation:
        return False
    if observation.stream != expected_stream or observation.timely != 1:
        return False
    if observation.phase == "PAYLOAD_WAIT":
        return (
            observation.guard_deadline_ns == state["payload_deadline_ns"]
            and observation.observed_ns <= reap.observed_ns
        )
    if observation.phase == "STREAM_EOF":
        return (
            observation.guard_deadline_ns == reap.stream_eof_deadline_ns
            and reap.observed_ns <= observation.observed_ns
            and observation.observed_ns < reap.stream_eof_deadline_ns
        )
    return False

def capture_complete_good(state, open_streams):
    reap = state["payload_wait_observation"]
    return (
        type(reap) is WaitObservation
        and reap.origin == "payload-wait"
        and reap.physical_reap == 1
        and reap.timely == 1
        and reap.stream_eof_deadline_ns
        == checked_u64_add(reap.observed_ns, PIPE_EOF_GRACE_NS, "stream-eof-arithmetic")
        and state["stream_eof_deadline_ns"] == reap.stream_eof_deadline_ns
        and eof_observation_good(state, state["stdout_eof_observation"], "stdout")
        and eof_observation_good(state, state["stderr_eof_observation"], "stderr")
        and state["payload_deadline_fired"] == 0
        and state["kill_reap_deadline_fired"] == 0
        and state["stream_eof_deadline_fired"] == 0
        and state["kill_sent"] == 0
        and state["child_reaped"] == 1
        and state["out_close_error"] == 0
        and state["err_close_error"] == 0
        and not capture_error_any(state)
        and not open_streams
        and not CLOSE_FAILED
        and os.WIFEXITED(reap.raw_status)
        and os.WEXITSTATUS(reap.raw_status) == 0
    )

def enter_kill_reap(state, pid):
    if state["child_reaped"] == 1:
        state["capture_state"] = "UNSAFE"
        return
    state["capture_state"] = "KILL_REAP"
    now = time.monotonic_ns()
    deadline = checked_u64_add(now, KILL_REAP_GRACE_NS, "kill-deadline-overflow")
    state["kill_reap_deadline_ns"] = deadline
    state["kill_sent"] = 1
    try:
        os.kill(pid, signal.SIGKILL)
    except OSError as error:
        if error.errno != errno.ESRCH:
            mark_capture_error(state, "payload-kill")
    except BaseException:
        mark_capture_error(state, "payload-kill-unexpected")

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
    state["payload_deadline_ns"] = payload_deadline
    if forced_error != "none":
        mark_capture_error(state, forced_error)
    while True:
        current = state["capture_state"]
        if current == "PAYLOAD_WAIT":
            observation = capture_wait_once(
                pid, state, payload_deadline, "payload-wait"
            )
            if state["capture_state"] == "PAYLOAD_WAIT" and (
                forced_error != "none"
                or state["out_overflow"]
                or state["err_overflow"]
                or state["payload_deadline_fired"]
                or state["supervisor_lost"]
                or capture_error_any(state)
                or CLOSE_FAILED
            ):
                enter_kill_reap(state, pid)
        elif current == "KILL_REAP":
            deadline = state["kill_reap_deadline_ns"]
            capture_wait_once(pid, state, deadline, "kill-reap")
            if state["kill_reap_deadline_fired"] == 1 and state["child_reaped"] == 0:
                state["capture_state"] = "UNSAFE"
        elif current == "STREAM_EOF":
            classify_capture_wait(state)
            if capture_complete_good(state, open_streams):
                state["capture_state"] = "COMPLETE"
                state["capture_complete"] = 1
            elif (
                state["reap_origin"] != "payload-wait"
                or state["kill_sent"] != 0
                or capture_error_any(state)
                or not open_streams
            ):
                state["capture_state"] = "UNSAFE"
            elif not capture_guard(
                state,
                state["stream_eof_deadline_ns"],
                "stream_eof_deadline_fired",
                "stream-eof",
            ):
                state["capture_state"] = "UNSAFE"
        if state["capture_state"] in ("COMPLETE", "UNSAFE"):
            break
        phase = state["capture_state"]
        if phase == "PAYLOAD_WAIT":
            deadline = payload_deadline
            bit = "payload_deadline_fired"
            code = "payload-wait"
        elif phase == "KILL_REAP":
            deadline = state["kill_reap_deadline_ns"]
            bit = "kill_reap_deadline_fired"
            code = "kill-reap"
        else:
            deadline = state["stream_eof_deadline_ns"]
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
                capture_read_once(
                    state,
                    key,
                    fd,
                    poller,
                    open_streams,
                    phase,
                    deadline,
                    bit,
                    code,
                )
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

def wait_value(observation, name, unavailable=False):
    if observation is None:
        return "unavailable" if unavailable else "none"
    value = getattr(observation, name)
    return "none" if value is None else str(value)

def eof_value(observation, name, unavailable=False):
    if observation is None:
        return "unavailable" if unavailable else "none"
    return str(getattr(observation, name))

def u64_int_good(value):
    return type(value) is int and 0 <= value <= UINT64_MAX

def hash_object_good(value):
    try:
        text = value.hexdigest()
    except BaseException:
        return False
    return canonical_hash_text(text, ())

def validate_result_capture(mode, state, disposition):
    need(
        isinstance(state, dict)
        and tuple(state) == tuple(empty_capture())
        and mode in ("watchdog", "recovery-binder")
        and disposition in ("SUCCESS", "PERMANENT_FAILURE")
        and isinstance(state["capture_error_bits"], dict)
        and tuple(state["capture_error_bits"]) == CAPTURE_ERROR_ORDER
        and all(value in (0, 1) for value in state["capture_error_bits"].values())
        and state["capture_errors_truncated"] in (0, 1),
        "result-capture-errors",
    )
    need(
        all(site in CLOSE_SITE_TOKENS for site in CLOSE_FAILURE_SITES)
        and len(CLOSE_FAILURE_SITES) <= CLOSE_FAILURE_SITES_CAP
        and CLOSE_FAILURE_SITES_TRUNCATED in (0, 1),
        "result-close-sites",
    )
    if mode == "watchdog":
        names = (
            "payload_deadline_fired", "kill_reap_deadline_fired",
            "stream_eof_deadline_fired", "payload_wait_observed",
            "payload_wait_timely", "kill_reap_wait_observed",
            "kill_reap_wait_timely", "stdout_eof_observed",
            "stdout_eof_timely", "stderr_eof_observed",
            "stderr_eof_timely", "child_reaped", "kill_sent",
            "capture_complete",
        )
        need(all(state[name] in (0, 1) for name in names), "result-capture-fields")
        need(
            isinstance(state["out"], bytearray)
            and isinstance(state["err"], bytearray)
            and len(state["out"]) <= STDOUT_CAP
            and len(state["err"]) <= STDERR_CAP
            and all(
                u64_int_good(state[name])
                for name in ("out_total", "err_total", "out_lf", "err_lf")
            )
            and state["out_lf"] <= state["out_total"]
            and state["err_lf"] <= state["err_total"]
            and state["out_total"] >= len(state["out"])
            and state["err_total"] >= len(state["err"])
            and state["out_overflow"] in (0, 1)
            and state["err_overflow"] in (0, 1)
            and (
                state["out_total"] == len(state["out"])
                if state["out_overflow"] == 0
                else state["out_total"] > len(state["out"]) and len(state["out"]) == STDOUT_CAP
            )
            and (
                state["err_total"] == len(state["err"])
                if state["err_overflow"] == 0
                else state["err_total"] > len(state["err"]) and len(state["err"]) == STDERR_CAP
            )
            and hash_object_good(state["out_hash"])
            and hash_object_good(state["err_hash"]),
            "result-stream-fields",
        )
        need(
            state["out_eof"] in (0, 1)
            and state["err_eof"] in (0, 1)
            and state["out_close_error"] in (0, 1)
            and state["err_close_error"] in (0, 1)
            and state["life_close_error"] in (0, 1)
            and state["timeout"] in (0, 1)
            and state["supervisor_lost"] in (0, 1)
            and state["payload_spawned"] in (0, 1)
            and state["wait_kind"] in ("none", "exit", "signal", "other")
            and state["exit_code"] is not None
            and u64_int_good(state["exit_code"])
            and (state["signal"] is None or u64_int_good(state["signal"]))
            and state["core"] in (0, 1)
            and state["recovery_pgid"] == "none"
            and state["wait_provenance"] == "watchdog-waitpid-authoritative"
            and state["stream_provenance"] == "watchdog-separate-raw-pipes"
            and state["streams_available"] == 1
            and state["wait_available"] == 1
            and state["recovery_esrch_initial"] == "na"
            and state["recovery_esrch_pre_evidence"] == "na"
            and state["recovery_esrch_terminal"] == "na"
            and state["out_eof"] == 1
            and state["err_eof"] == 1
            and state["out_close_error"] == 0
            and state["err_close_error"] == 0
            and state["life_close_error"] == 0
            and state["timeout"] == 0
            and state["supervisor_lost"] == 0
            and state["payload_spawned"] == 1,
            "result-watchdog-enums",
        )
        need(
            u64_int_good(state["payload_deadline_ns"])
            and state["kill_reap_deadline_ns"] is None
            and u64_int_good(state["stream_eof_deadline_ns"]),
            "result-watchdog-deadlines",
        )
        need(state["capture_state"] == "COMPLETE", "result-capture-state")
        need(state["capture_complete"] == 1, "result-capture-complete")
        need(capture_complete_good(state, set()), "result-causal-capture")
        need(
            type(state["payload_wait_observation"]) is WaitObservation
            and state["kill_reap_wait_observation"] is None
            and type(state["stdout_eof_observation"]) is EOFObservation
            and type(state["stderr_eof_observation"]) is EOFObservation,
            "result-observation-shape",
        )
        need(
            state["reap_origin"] == "payload-wait"
            and state["payload_wait_observation"].error_token == "none",
            "result-watchdog-origin",
        )
    else:
        names = (
            "payload_deadline_fired", "kill_reap_deadline_fired",
            "stream_eof_deadline_fired", "payload_wait_observed",
            "payload_wait_timely", "kill_reap_wait_observed",
            "kill_reap_wait_timely", "stdout_eof_observed",
            "stdout_eof_timely", "stderr_eof_observed",
            "stderr_eof_timely", "child_reaped", "kill_sent",
            "capture_complete",
        )
        need(all(state[name] == "unavailable" for name in names), "result-recovery-capture")
        need(
            disposition == "PERMANENT_FAILURE"
            and state["out"] == bytearray()
            and state["err"] == bytearray()
            and state["out_hash"] is None
            and state["err_hash"] is None
            and all(
                state[name] == "unavailable"
                for name in (
                    "out_total", "err_total", "out_lf", "err_lf",
                    "out_overflow", "err_overflow", "out_eof", "err_eof",
                    "out_close_error", "err_close_error", "life_close_error",
                    "timeout", "payload_spawned", "capture_state", "core",
                )
            )
            and state["supervisor_lost"] == 1
            and state["wait_raw"] is None
            and state["wait_kind"] == "unavailable"
            and state["exit_code"] is None
            and state["signal"] is None
            and canonical_u64_text(state["recovery_pgid"], ())
            and state["wait_provenance"] == "unavailable-recovery"
            and state["stream_provenance"] == "unavailable-recovery"
            and state["streams_available"] == 0
            and state["wait_available"] == 0
            and state["recovery_esrch_initial"] == "1"
            and state["recovery_esrch_pre_evidence"] == "1"
            and state["recovery_esrch_terminal"] == "1"
            and state["payload_deadline_ns"] == "unavailable"
            and state["kill_reap_deadline_ns"] == "unavailable"
            and state["stream_eof_deadline_ns"] == "unavailable"
            and state["payload_wait_observation"] is None
            and state["kill_reap_wait_observation"] is None
            and state["stdout_eof_observation"] is None
            and state["stderr_eof_observation"] is None
            and state["reap_origin"] == "unavailable"
            and state["capture_error_bits"]["watchdog-report-lost"] == 1,
            "result-recovery-disposition",
        )

def result_layout_failure(mode, observed_bytes, observed_sha):
    need(
        mode in ("watchdog", "recovery-binder")
        and u64_int_good(observed_bytes)
        and canonical_hash_text(observed_sha, ()),
        "result-layout-fields",
    )
    value = (
        "RESULT E001_SUPERVISOR_BINDER_RECOVERY version=5 mode="
        + mode
        + " attempt_consumed=1 payload_success=0"
        + " schema-layout=overflow disposition=PERMANENT_FAILURE"
        + " observed_bytes="
        + str(observed_bytes)
        + " observed_sha256="
        + observed_sha
        + "\n"
    ).encode("ascii")
    need(
        len(value) <= RESULT_FIXED_CAP and len(value) <= RESULT_CAP,
        "result-layout-failure-cap",
    )
    return value

def result_line(mode, state, binder, binder_status, phase, disposition):
    validate_result_capture(mode, state, disposition)
    need(
        isinstance(binder, bytes)
        and len(binder) <= BINDER_CAP
        and binder_status in ("not-run", "ok", "error")
        and phase in PHASE_STATES + ("not-applicable",)
        and (
            disposition == "SUCCESS"
            and mode == "watchdog"
            and binder == b""
            and binder_status == "not-run"
            and phase == "not-applicable"
            or disposition == "PERMANENT_FAILURE"
            and binder != b""
            and binder_status in ("ok", "error")
            and phase in PHASE_STATES
        ),
        "result-arguments",
    )
    sites = ",".join(CLOSE_FAILURE_SITES) if CLOSE_FAILURE_SITES else "none"
    unavailable = mode == "recovery-binder"
    payload_wait = state["payload_wait_observation"]
    kill_wait = state["kill_reap_wait_observation"]
    stdout_eof = state["stdout_eof_observation"]
    stderr_eof = state["stderr_eof_observation"]
    fields = (
        "RESULT E001_SUPERVISOR_BINDER_RECOVERY"
        + " version=5"
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
        + " payload_deadline_ns="
        + optional(state["payload_deadline_ns"])
        + " payload_deadline_origin=immediately-before-payload-spawn"
        + " kill_reap_deadline_ns="
        + optional(state["kill_reap_deadline_ns"])
        + " kill_reap_deadline_origin=immediately-before-sigkill"
        + " stream_eof_deadline_ns="
        + optional(state["stream_eof_deadline_ns"])
        + " stream_eof_deadline_origin=single-first-post-wait-observation"
        + " payload_wait_outcome="
        + wait_value(payload_wait, "outcome", unavailable)
        + " payload_wait_origin="
        + wait_value(payload_wait, "origin", unavailable)
        + " payload_wait_guard_deadline_ns="
        + wait_value(payload_wait, "guard_deadline_ns", unavailable)
        + " payload_wait_called="
        + wait_value(payload_wait, "wait_called", unavailable)
        + " payload_wait_observed_ns="
        + wait_value(payload_wait, "observed_ns", unavailable)
        + " payload_wait_physical_reap="
        + wait_value(payload_wait, "physical_reap", unavailable)
        + " payload_wait_timely="
        + wait_value(payload_wait, "timely", unavailable)
        + " payload_wait_raw_status="
        + wait_value(payload_wait, "raw_status", unavailable)
        + " payload_wait_stream_eof_deadline_ns="
        + wait_value(payload_wait, "stream_eof_deadline_ns", unavailable)
        + " payload_wait_error_token="
        + wait_value(payload_wait, "error_token", unavailable)
        + " kill_wait_outcome="
        + wait_value(kill_wait, "outcome", unavailable)
        + " kill_wait_origin="
        + wait_value(kill_wait, "origin", unavailable)
        + " kill_wait_guard_deadline_ns="
        + wait_value(kill_wait, "guard_deadline_ns", unavailable)
        + " kill_wait_called="
        + wait_value(kill_wait, "wait_called", unavailable)
        + " kill_wait_observed_ns="
        + wait_value(kill_wait, "observed_ns", unavailable)
        + " kill_wait_physical_reap="
        + wait_value(kill_wait, "physical_reap", unavailable)
        + " kill_wait_timely="
        + wait_value(kill_wait, "timely", unavailable)
        + " kill_wait_raw_status="
        + wait_value(kill_wait, "raw_status", unavailable)
        + " kill_wait_stream_eof_deadline_ns="
        + wait_value(kill_wait, "stream_eof_deadline_ns", unavailable)
        + " kill_wait_error_token="
        + wait_value(kill_wait, "error_token", unavailable)
        + " reap_origin="
        + state["reap_origin"]
        + " stdout_eof_stream="
        + eof_value(stdout_eof, "stream", unavailable)
        + " stdout_eof_phase="
        + eof_value(stdout_eof, "phase", unavailable)
        + " stdout_eof_guard_deadline_ns="
        + eof_value(stdout_eof, "guard_deadline_ns", unavailable)
        + " stdout_eof_observed_ns="
        + eof_value(stdout_eof, "observed_ns", unavailable)
        + " stdout_eof_timely="
        + eof_value(stdout_eof, "timely", unavailable)
        + " stderr_eof_stream="
        + eof_value(stderr_eof, "stream", unavailable)
        + " stderr_eof_phase="
        + eof_value(stderr_eof, "phase", unavailable)
        + " stderr_eof_guard_deadline_ns="
        + eof_value(stderr_eof, "guard_deadline_ns", unavailable)
        + " stderr_eof_observed_ns="
        + eof_value(stderr_eof, "observed_ns", unavailable)
        + " stderr_eof_timely="
        + eof_value(stderr_eof, "timely", unavailable)
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
        + " stderr_eof_observed="
        + str(state["stderr_eof_observed"])
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
        + " capture_errors="
        + capture_errors_text(state)
        + " capture_errors_truncated="
        + str(state["capture_errors_truncated"])
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
    stream_blob = 0
    if state["streams_available"] == 1:
        stream_blob = 2 * (len(state["out"]) + len(state["err"]))
    if len(value) > RESULT_FIXED_CAP + 2 * len(binder) + stream_blob:
        return result_layout_failure(mode, len(value), sha(value))
    if len(value) > RESULT_WORST:
        return result_layout_failure(mode, len(value), sha(value))
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
    payload_deadline = checked_u64_add(
        time.monotonic_ns(),
        PAYLOAD_DEADLINE_NS,
        "payload-deadline-overflow",
    )
    state["payload_deadline_ns"] = payload_deadline
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
        capture_wait_once(pid, state, payload_deadline, "payload-wait")
    if state["child_reaped"] == 0 and state["capture_state"] != "UNSAFE":
        enter_kill_reap(state, pid)
        if state["capture_state"] == "KILL_REAP":
            observation = wait_deadline(
                pid,
                state["kill_reap_deadline_ns"],
                "kill-reap",
            )
            reduce_wait_observation(state, observation)
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
        and not capture_error_any(state)
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
    if (
        state["capture_state"] != "COMPLETE"
        or state["capture_complete"] != 1
        or capture_error_any(state)
        or state["life_close_error"] != 0
        or CLOSE_FAILED
    ):
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)
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
            checked_u64_add(
                time.monotonic_ns(),
                LAUNCH_RELEASE_DEADLINE_NS,
                "launch-release-deadline-overflow",
            ),
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
        ready_deadline = checked_u64_add(
            time.monotonic_ns(),
            READY_DEADLINE_NS,
            "ready-deadline-overflow",
        )
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
        ack_deadline = checked_u64_add(
            time.monotonic_ns(),
            ACK_DEADLINE_NS,
            "ack-deadline-overflow",
        )
        require_before(ack_deadline, "ack-begin")
        begin = begin_line(pid, binding, ready_deadline, ack_deadline)
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
        require_before(ack_deadline, "ack-start")
        write_all(life_write, b"S")
        require_before(ack_deadline, "ack-start")
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
            cleanup_deadline = checked_u64_add(
                time.monotonic_ns(),
                KILL_REAP_GRACE_NS,
                "cleanup-deadline-overflow",
            )
            observation = wait_deadline(
                WATCHDOG_PID,
                cleanup_deadline,
                "cleanup",
            )
            if (
                not observation.physical_reap
                and observation.outcome not in ("error", "other")
            ):
                try:
                    os.kill(WATCHDOG_PID, signal.SIGKILL)
                except OSError as error:
                    if error.errno != errno.ESRCH:
                        pass
                try:
                    cleanup_deadline = checked_u64_add(
                        time.monotonic_ns(),
                        KILL_REAP_GRACE_NS,
                        "cleanup-deadline-overflow",
                    )
                    observation = wait_deadline(
                        WATCHDOG_PID,
                        cleanup_deadline,
                        "cleanup",
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
    try:
        require_group_absent(pgid)
        meta["recovery_third_esrch"] = "1"
    except BaseException:
        try:
            os.close(1)
        except BaseException:
            pass
        os._exit(1)
    binder, binder_status, phase = render_binder(meta, True)
    state = recovery_capture(pgid)
    state["recovery_esrch_initial"] = meta["recovery_first_esrch"]
    state["recovery_esrch_pre_evidence"] = meta["recovery_second_esrch"]
    state["recovery_esrch_terminal"] = meta["recovery_third_esrch"]
    if meta["post_inputs_reverified"] != 1:
        mark_capture_error(state, "input-terminal-drift")
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
BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V5_PROGRAM_END

## 4. Uniform observation schema and non-destructive validation

NODE_KEY_ARITY is exactly eight everywhere in the audit schema:
(dev, ino, mode, nlink, uid, gid, rdev, size). Observation key and final_key,
evidence keys, inventory anchor keys, candidate keys, and all opening and
fresh Chain component signatures use that tuple. Every present scalar set
must canonically match its key, including the size field and seven-octal-digit
mode. Absent, unavailable and error states carry no key and all associated
identity scalars are none. The separately named ledger_stable_key deliberately
omits only the growing status file size and is not an audit node key or hidden
directory key.

The audit object has one preallocated exact outer layout: two source
observations, two evidence observations, three snapshots, twelve named
candidate observations, three inventories, fixed relation and anomaly
containers, independent attempt/success/close/reachability bits, three ESRCH
bits, terminal revalidation, errors, unions, status and phase. A valid object
passes validation and rendering without mutation. Every enum, scalar, key,
tuple length, cap, canonical frame, exact derived cache and exact-success
claim is checked before serialization.

If a leaf is malformed, sanitation changes only that leaf and dependent
claims. It retains every valid neighboring source, evidence, candidate,
snapshot and inventory observation; preserves historical open flags; closes
any still-owned tracked descriptor; clears exact, stable and reachability
claims that depended on the malformed leaf; adds schema-malformed and finite
reason bits; and then recomputes frames, unknowns, relations, anomalies,
unions, equality, status and phase from retained observations. Invalid names
are represented by bounded length and SHA-256 overflow evidence when bytes
are available. Valid data is idempotent. An impossible outer key set, wrong
record count, wrong fixed reason-bit layout or still-invalid sanitized leaf
uses a separately labeled SCHEMA_LAYOUT_FAILURE envelope. Such an envelope
never claims schema-layout full.

Successful source and candidate O_PATH opens set path_fd_opened immediately.
That bit is historical and never cleared by later read, stat, validation,
close or sanitation failure. Attempt, successful return, close completion,
fresh-chain attempt, fresh-chain open, component equality, fresh path stat,
fresh O_PATH, fresh directory open, second final stat, identity equality and
fresh-chain close are separate monotone fields. Classification requires the
true success and close fields, not merely an attempted operation.

## 5. Fresh absolute reachability and evidence brackets

The initial bracket constructs one opening seven-component absolute Chain
from slash, begins the evidence observation, and independently attempts
snapshot one and snapshot two. After the bracket, finish_evidence constructs
a wholly new absolute Chain from slash; it never finalizes through the held
opening parent. The terminal bracket independently repeats that sequence for
snapshot three. Partial opening and fresh Chains retain each successfully
observed component key and unavailable slots for the remainder, and every
owned component FD is closed under a distinct latch.

The full report renders fourteen Chain components for the initial bracket and
fourteen for the terminal bracket: seven opening plus seven fresh each,
exactly twenty-eight CHAIN_COMPONENT lines. Reachability succeeds only if
each fresh Chain is complete and all seven eight-field keys equal the opening
signature componentwise.

For an initially present evidence node, finalization relative to the fresh
leaf performs a first no-follow stat, a fresh O_PATH open and fstat, a fresh
directory open and fstat, and a second no-follow final stat. Those values are
compared with the opening no-follow stat, retained opening O_PATH fstat,
retained opening directory fstat, one another, and the second final stat.
Every comparison includes size. For initial absence, both fresh no-follow
stats must independently return ENOENT and no evidence FD may exist. Partial
or non-directory presence is retained but never exact. Fresh-chain close and
later retained-evidence close are independent gates. Snapshot one, two and
three each have distinct attempt, success and close fields; only success plus
close can contribute to a named phase.

Each source and candidate observation likewise retains initial and final
no-follow path states, full eight-field keys, content disposition, exact
bounded content identity when available, errors, historical opens and close
outcomes. A present exact claim is re-derived against its fixed expected
mode, ownership, link count, device relationship, size, LF count and hash.
Stable absence is double ENOENT. No sanitizer may promote an observation.

## 6. Exact constructor caps and canonical rendering

Inventory basenames are one through 255 bytes. Each snapshot retains at most
64 sorted unique names with at most 16384 raw name bytes. The true constructor
raw maximum is 64 times 255, or 16320. A maximum canonical row is four length
and colon bytes, 510 lowercase hex bytes and one LF, or 515 bytes; therefore
the true 64-row frame maximum is 32960, below the exact frame cap 33216.
Validation requires byte-for-byte equality with that canonical frame.

Each snapshot retains at most 64 unknown names and 16384 unknown raw bytes.
The three-snapshot unknown union retains at most 192 names and 49152 raw
bytes; its constructor maximum is 48960. Four candidates give exactly at most
six unordered duplicate pairs and four source aliases. Snapshot anomalies
have cap 96 and token cap 518. Their constructor maximum is exactly
13 inventory reasons plus one reason-truncation token, at most eight
candidate-state/type/size tokens, 64 unknown-name tokens, six duplicates and
four aliases: 96. Global anomalies have cap 32 and token cap 64; this
constructor emits at most 31. The anomaly union has cap 320 and token cap
529; its constructor emits at most three times 96 plus 31, or 319. The
529-byte token bound is the 11-byte snapshot prefix plus a maximum 518-byte
unknown anomaly.

Names, inventory data and captured stream data render only as lowercase hex.
Unsigned integers use canonical decimal without a leading zero except zero.
Modes are exactly seven octal digits. Hashes are exactly 64 lowercase hex
digits or a field-specific finite sentinel. All other strings are fixed enums,
finite relation tokens, or lowercase alphanumeric-hyphen safe tokens under a
field-specific cap. Whitespace, controls, equals, comma and record-delimiter
injection are rejected as value data. Commas appear only between already
validated finite tokens. Serialization consumes validated values only.

Every builder asserts its local serialized bound:

- header 4096 and schema header 128;
- sixteen observation lines at 2048 each;
- twenty-eight Chain lines at 384 each;
- three inventory lines at 67072 each;
- 192 unknown lines at 640 each;
- three relation lines at 256 each;
- 288 snapshot-anomaly lines at 576 each;
- cross line 1024, 32 global-anomaly lines at 128 each, and union line 512;
- revalidation 3072, provenance 256, and end 16.

The complete arithmetic is

4096 + 128 + 16*2048 + 28*384 + 3*67072 + 192*640
+ 3*256 + 288*576 + 1024 + 32*128 + 512 + 3072 + 256 + 16
= 547472.

Thus BINDER_WORST is exactly 547472 and BINDER_CAP is 589824. Variable line
counts can only reduce the result. The impossible-layout and
impossible-overflow envelopes are bounded permanent failures and never a
truncated full schema.

RESULT_FIXED_CAP is 12288. It includes every fixed label, finite enum, bounded
decimal, hash, capture-error set, close set, deadline, wait and EOF field, plus
the constant framing overhead when a binder or stream is empty. Binder hex
costs at most twice BINDER_WORST. Stored stdout and stderr hex cost at most
twice 4096 plus 65536. Therefore

RESULT_WORST
= 12288 + 2*547472 + 2*(4096 + 65536)
= 1246496,

strictly below RESULT_CAP 1310720. The RESULT builder checks both the
instance-specific decomposition and RESULT_WORST before the final cap.
Unsigned counters saturate at UINT64_MAX only while latching a permanent
counter-overflow error. All deadline additions are checked unsigned
additions. Any mechanically impossible size violation emits only the small,
bounded, clearly labeled permanent-failure envelope.

## 7. Immutable wait, EOF and completion contract

Every guarded wait returns exactly one immutable WaitObservation even for
pre-guard expiry, interruption, empty WNOHANG, wait error, unexpected return,
timely reap or late reap. The observation contains its exact origin and guard,
whether waitpid was called, the first timestamp sampled immediately after
waitpid, physical ownership outcome, timeliness, raw status, derived EOF
deadline and finite error token. Generic cleanup returns that same evidence.
A wait error or unexpected ownership result moves capture to UNSAFE; neither
payload cleanup nor supervisor cleanup then sends a numeric-PID signal.
Known direct-child cleanup may signal only after a non-error empty or expired
wait, and never after physical reap.

Stream reads sample exactly once immediately after read. Nonempty late data is
still retained in bounded counters, hash and prefix before permanent failure
is decided. The first EOF per stream creates one immutable EOFObservation.
Duplicate EOF evidence is an error. PAYLOAD_WAIT EOF must precede or equal T
and use the payload guard. STREAM_EOF EOF must follow or equal T, precede S,
and use S as its guard. KILL_REAP EOF is retained but cannot validate
completion. The stdout and stderr record stream tags must match their slots.

The only authoritative direct completion has payload origin, timely physical
reap, no kill observation, no kill attempt, raw exit zero, S equal to T plus
1000000000 nanoseconds, two coherent EOF records, zero deadline bits, zero
capture errors and truncation, zero stream and lifeline close errors, no open
stream, exact bounded counters and hashes, and no global close failure.
Kill-origin, signaled, nonzero, late, uncertain, overflowed or close-failed
capture cannot produce an authoritative RESULT. A clean exit-zero capture
whose payload bytes do not match the exact PASS line may produce only a
PERMANENT_FAILURE binder result.

Capture errors are a fixed-order monotone bit set plus a truncation bit.
Unknown error input maps to unexpected and latches truncation; no later event
can overwrite an earlier error. RESULT validation checks the complete
preallocated capture layout and every field grammar before encoding. Recovery
uses the same layout with explicit unavailable values and retains
watchdog-report-lost together with input-terminal-drift whenever terminal
inputs fail; the latter never replaces the former.

## 8. Full binder recovery and permanent-failure rules

The caller allocates the complete audit schema before constructing
FailureBinderInputs. Inputs, ControlInputs, source observations, partial
absolute Chains, evidence records, snapshots, verify outcomes, close outcomes,
derived caches, binder bytes and RESULT bytes remain caller-owned optional
locals. Construction, observation, fresh-chain, inventory, candidate,
verification, close, derivation, sanitation, serialization and rendering
exceptions can only add finite errors, clear dependent success claims, close
owned FDs and continue the bounded fail-closed sequence. They cannot replace
the schema with an apparently complete default.

The observation order is fixed: opening initial evidence; independent
snapshots one and two; fresh initial finalization; opening terminal evidence;
independent snapshot three; fresh terminal finalization; snapshot closes;
retained evidence closes; opening-parent closes; complete terminal control
and source verification; input close; final tracked-FD sweep; exact derivation;
validation; and rendering. All close sites feed the monotone global latch and
bounded fixed-token close set. A close failure cannot suppress a later close,
verification or finalizer, but it permanently forbids success.

Recovery accepts only a canonical already-consumed PGID. Its first killpg
zero ESRCH proof precedes input construction. Its second independent ESRCH
proof immediately precedes any evidence Chain; failure prevents evidence
access and forbids output. After complete terminal verification and closure,
a third ESRCH proof precedes rendering. A fourth emission-adjacent absence
check occurs after candidate RESULT construction and immediately before the
write. Any non-ESRCH result suppresses all bytes. Recovery never signals a
numeric PID, never starts payload work, never claims authoritative wait or
stream provenance, and can emit only PERMANENT_FAILURE with
unknown-mismatch. It grants no retry.

The direct and recovery reports retain provenance explicitly. A payload-created
status receipt is synthetic and nonauthoritative. Direct wait provenance is
the watchdog waitpid observation and direct streams are distinct raw pipes.
Recovery wait and stream provenance are unavailable. Future acceptance must
bind these labels to external pipe EOF, status and process-group evidence;
no provenance token upgrades missing evidence.

## 9. Retained actor, fixture and host premises

The V4 group and release protocol remains: one actor-known supervisor session
and process group, exact L/R/A/S tokens, durable pending record before ACK,
watchdog and payload without group escape, payload stdin held live, one
attempt, and negative-group cleanup owned only by the actor. The supervisor
never calls killpg on its own group. The actor must treat ambiguity at the
first possibly written ACK byte as consumed and may invoke the recovery binder
once only after killing, reaping the direct supervisor and proving the group
absent.

The exact eleven Binding fields remain self device, inode, bytes, LF and hash;
ledger device, inode, prefix bytes, LF and hash; and ledger terminal hex.
BEGIN retains ready and ACK origins and deadlines plus the payload, launcher
and inner identities. A later actor must compare every field byte-for-byte,
retain all guard outcomes, and revalidate whole V5 plus the complete current
ledger at terminal acceptance.

No fixture is authorized here. A later fixture control, if separately
authorized, must derive only from the exact normalized program with a reviewed
ordered replacement table and identical control-flow skeleton. Production has
no test branch, environment switch, monkeypatch, fault hook, production
build/evidence fixture literal or alternative payload route.

Activation still depends on separately frozen no-build proof of CPython 3.12,
libc posix_spawn and file actions, setsid behavior, the host-wide 1048576 FD
ceiling, complete signal normalization, O_NOATIME authority, timely SIGKILL
outside uninterruptible kernel sleep, no adversarial PID/PGID reuse during the
checked interval, the statically proved exec chain without group escape,
filesystem durability, and declared single-writer immutability.

This author stop creates no actor, payload, recovery-binder, fixture, probe,
microtest, build, evidence, E010, A000, stage, root, PDF, release or Paper28
execution authority.

BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V5_AUTHOR_STOP
