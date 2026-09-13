# Paper 27 probe-recovery E001 noncircular first-copy control

## 1. Authority, status, and narrow precedence

This is the sole supplemental control authorized by
`B07-E0312-P27-PROBE-RECOVERY-E001-PLAN-DUAL-FAILURE-AND-NONCIRCULAR-FIRST-COPY-CONTROL-AUTHORIZATION`.
At its authoring boundary, `BATCH_07_STATUS.md` is 1,646,790 bytes, 19,229
LF bytes, regular mode 0644, link one, SHA-256
`5cfbfb59a26a654b6c094c3eece778ac192b7b7ab45b1c173650e499f324cf4d`,
and ends in
`BATCH07_P27_PROBE_RECOVERY_E001_PLAN_FAILURE_RECORDED_AND_FIRST_COPY_CONTROL_AUTHORIZED`.
This file is strict UTF-8/LF, has no BOM, CR, or NUL, has exactly one
terminal LF, and must remain regular mode 0644 and link one.

This control is authoritative only for one future recovery `E001` first-copy
transaction.  It narrowly supersedes only the impossible recovery-E001
requirement that an already-installed evidence validator authenticate its own
creation, the ordinary `/usr/bin/install` E001 payload, the ordinary Section
3 E001 receipt-redirection capsule, and the ordinary provenance of the E001
receipt triple.  It does not supersede the E0311 evidence-directory binding,
the validator source/lock/review bytes, the required copy or receipt bytes,
any E010-or-later profile/validator/lock clause, any validator predicate, any
evidence name frame, first-failure preservation, or build ordering.

The notes validator source is immutable payload only.  The harness neither
imports nor executes it.  `/usr/bin/install` is not invoked.  This
supplemental control is not a validator runtime input.  After the one attempt
is physically bound, this file becomes immutable historical control and the
supplemental precedence expires permanently.

This authoring event grants no execution or build-path access.  Only a later
ledger event that binds this exact file and two separated all-zero W1/W2
reviews may authorize the exact process below once.  E010, A000, validator
execution, stage/root access, PDF work, release, Paper 28, cleanup, repair,
and retry remain closed.

## 2. Frozen inputs, process, and trust boundary

The immutable source is exactly
`/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/BUILD_VALIDATOR_RECOVERY.py`:

```text
dev=2431
ino=5913826453
type=regular
mode=0644
nlink=1
uid=0
gid=0
bytes=398310
LF=9366
sha256=6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817
terminal=# BATCH07_P27_BUILD_VALIDATOR_RECOVERY_AUTHOR_STOP
```

The opening evidence directory is inherited without an authoring-time
reprobe from E0311 and must be exactly:

```text
dev=2431
ino=14502900794
type=directory
mode=0700
nlink=2
uid=0
gid=0
bytes=6
entries=0
```

The size-six predicate applies only before the first mutation.  Directory
size is never required after any child is created.  Device, inode, type/mode,
link count, and ownership remain required throughout.

The future execution preflight must bind, without build-path access, this
control and its W1/W2 reviews; the E0312 ledger; the recovery profile/profile
review; validator source/lock/review; inherited dependency and static-source
controls; and these exact process tools:

```text
/usr/bin/env regular 43976 0755 nlink=1 sha256=85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0
/usr/bin/bash regular 1396520 0755 nlink=1 sha256=59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4
/root/miniconda3/bin/python3 symlink bytes=10 mode=0777 nlink=1 raw=python3.12
/root/miniconda3/bin/python3.12 regular 30626264 0755 nlink=1 sha256=9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101
```

From that final preflight through the physical success or failure ledger
binding, one explicit single-writer interval governs the supplemental
control, validator source, process tools, every source/evidence ancestor, the
evidence directory, and its four candidate children.  Only the governed
harness may mutate the evidence entry set, and only by the four exclusive
creates below.  Rename, unlink, mount-over, bind-mount, replacement, hard-link
addition, source mutation, and outside evidence mutation invalidate the run.
Held descriptors and full rewalks detect changes through the last physical
check; the single-writer premise governs the unavoidable interval through
ledger binding.

The exact E0280 launcher argv is:

```text
/usr/bin/env
-i
/usr/bin/bash
--noprofile
--norc
-c
LITERAL_E0280_LAUNCHER
batch07-p27-successor-liveness-fd-scrub-launcher
LITERAL_E001_INNER
```

`LITERAL_E0280_LAUNCHER` is exactly:

```text
[ "$#" -eq 1 ] || exit 127
batch07_p27_inner=$1
[[ -e /proc/self/fd/0 && -e /proc/self/fd/1 && -e /proc/self/fd/2 ]] || exit 127
for batch07_p27_fd_path in /proc/self/fd/*; do
  batch07_p27_fd=${batch07_p27_fd_path##*/}
  case $batch07_p27_fd in
    0|1|2) ;;
    ''|*[!0-9]*) exit 127 ;;
    *) exec {batch07_p27_fd}>&- || exit 127 ;;
  esac
done
ulimit -Sn 4096 || exit 127
exec /usr/bin/env -i /usr/bin/bash --noprofile --norc -c "$batch07_p27_inner"
```

Its frozen transport identities are raw 454 bytes, 13 LF, SHA-256
`f003386d98e60443011e85204651a44c99a9dc7c41aba4989b9e4f619fa40a09`
and normalized 453 bytes, 12 LF, SHA-256
`72927f87bb6fa18ce0afc7edf28f2cc81e4b370fb6d007ab485856d294752dcd`.

`LITERAL_E001_INNER` is exactly the following four lines, with the normalized
marker-delimited harness substituted literally for the final token and
enclosed by the displayed single quotes:

```text
set -C
umask 077
cd -- /root/autodl-tmp/symplectic_map || exit 125
exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -S -B -P -c 'LITERAL_E001_FIRST_COPY_HARNESS'
```

There is no argument after the `-c` source.  The harness requires exact
`sys.argv`, cwd, ten-key environment, interpreter/flags, euid/egid zero,
umask 077, live standard descriptors, and soft `RLIMIT_NOFILE` 4096.

## 3. Exact literal harness

The normalized harness is exactly the byte substring after the BEGIN line's
LF and before the LF immediately preceding the END line.  The delimiter LF
is not passed to Python.  Static marker extraction must freeze the raw and
normalized byte/LF/SHA identities before W1/W2 review.  No reviewer may
import, parse, compile, or execute it.

BATCH07_P27_RECOVERY_E001_FIRST_COPY_HARNESS_BEGIN
import errno
import hashlib
import os
import resource
import stat
import sys

SOURCE_COMPONENTS = (
    b"root",
    b"autodl-tmp",
    b"symplectic_map",
    b"papers",
    b"27-positive-newton-translation-reciprocity",
    b"notes",
)
EVIDENCE_COMPONENTS = (
    b"root",
    b"autodl-tmp",
    b"symplectic_map",
    b"papers",
    b"27-positive-newton-translation-reciprocity",
    b"build",
    b"recovery-6103a9df0c3d-evidence",
)
SOURCE_NAME = b"BUILD_VALIDATOR_RECOVERY.py"
COPY_NAME = b"BUILD_VALIDATOR_RECOVERY.py"
STDOUT_NAME = b"E001.stdout"
STDERR_NAME = b"E001.stderr"
STATUS_NAME = b"E001.status"
CREATE_ORDER = (STDOUT_NAME, STDERR_NAME, COPY_NAME, STATUS_NAME)
FINAL_NAMES = (
    COPY_NAME,
    STATUS_NAME,
    STDERR_NAME,
    STDOUT_NAME,
)
FINAL_FRAME = (
    b"BUILD_VALIDATOR_RECOVERY.py\n"
    b"E001.status\n"
    b"E001.stderr\n"
    b"E001.stdout\n"
)
EXPECTED_CWD = b"/root/autodl-tmp/symplectic_map"
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
SOURCE_DEV = 2431
SOURCE_INO = 5913826453
SOURCE_BYTES = 398310
SOURCE_LF = 9366
SOURCE_SHA256 = "6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817"
SOURCE_TERMINAL = b"# BATCH07_P27_BUILD_VALIDATOR_RECOVERY_AUTHOR_STOP\n"
EVIDENCE_DEV = 2431
EVIDENCE_INO = 14502900794
EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
STATUS_SHA256 = "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"
FRAME_SHA256 = "7aeb029ca886a47abeb0bd05a4f941c820983dc6e90925880ff7e297f92dbcde"
PASS_SHA256 = "b149a22827939aff6a6875a4797076a7e32f8ada246dee0e2f3a7aa490247c5b"
PASS_LINE = (
    b"PASS E001_FIRST_COPY_RECOVERY evidence_dev=2431 evidence_ino=14502900794 "
    b"copy_bytes=398310 copy_LF=9366 "
    b"copy_sha256=6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817 "
    b"inventory_items=4 inventory_framing_bytes=64 "
    b"inventory_sha256=7aeb029ca886a47abeb0bd05a4f941c820983dc6e90925880ff7e297f92dbcde\n"
)
CHUNK = 65536
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC
CREATE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC
OPEN_FDS = []

class Stop(Exception):
    pass

def stop(tag):
    raise Stop(tag)

def open_tracked(path, flags, dir_fd=None, mode=None):
    try:
        if mode is None:
            fd = os.open(path, flags, dir_fd=dir_fd)
        else:
            fd = os.open(path, flags, mode, dir_fd=dir_fd)
    except OSError:
        stop("OPEN")
    if fd < 3 or fd in OPEN_FDS:
        try:
            os.close(fd)
        except OSError:
            pass
        stop("OPEN_FD")
    OPEN_FDS.append(fd)
    return fd

def close_all():
    passed = True
    while OPEN_FDS:
        fd = OPEN_FDS.pop()
        try:
            os.close(fd)
        except OSError:
            passed = False
    return passed

def fstat_checked(fd):
    try:
        return os.fstat(fd)
    except OSError:
        stop("FSTAT")

def stat_at(parent_fd, name):
    try:
        return os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError:
        stop("STATAT")

def require_absent(parent_fd, name):
    try:
        os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as error:
        if error.errno != errno.ENOENT:
            stop("ABSENCE_ERRNO")
    else:
        stop("PRESENT")

def fsync_checked(fd):
    try:
        os.fsync(fd)
    except OSError:
        stop("FSYNC")

def directory_key(info):
    return (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_uid,
        info.st_gid,
    )

def object_key(info):
    return (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_uid,
        info.st_gid,
        info.st_rdev,
    )

def regular_key(info):
    return object_key(info) + (
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )

def fd_pair(fd):
    info = fstat_checked(fd)
    return (info.st_dev, info.st_ino)

def open_chain(components):
    fds = []
    root_fd = open_tracked(b"/", DIR_FLAGS)
    root_info = fstat_checked(root_fd)
    if not stat.S_ISDIR(root_info.st_mode):
        stop("ROOT_TYPE")
    fds.append(root_fd)
    for component in components:
        before = stat_at(fds[-1], component)
        if not stat.S_ISDIR(before.st_mode):
            stop("ANCESTOR_TYPE")
        child_fd = open_tracked(component, DIR_FLAGS, dir_fd=fds[-1])
        inside = fstat_checked(child_fd)
        if directory_key(before) != directory_key(inside):
            stop("ANCESTOR_REBIND")
        fds.append(child_fd)
    return tuple(fds)

def rewalk_chain(components, held):
    fresh = open_chain(components)
    if len(fresh) != len(held):
        stop("REWALK_LENGTH")
    for fresh_fd, held_fd in zip(fresh, held):
        if directory_key(fstat_checked(fresh_fd)) != directory_key(fstat_checked(held_fd)):
            stop("REWALK_IDENTITY")
    return fresh

def require_evidence(info, opening):
    if (
        not stat.S_ISDIR(info.st_mode)
        or info.st_dev != EVIDENCE_DEV
        or info.st_ino != EVIDENCE_INO
        or stat.S_IMODE(info.st_mode) != 0o700
        or info.st_nlink != 2
        or info.st_uid != 0
        or info.st_gid != 0
        or info.st_rdev != 0
    ):
        stop("EVIDENCE_IDENTITY")
    if opening and info.st_size != 6:
        stop("EVIDENCE_OPENING_SIZE")

def inventory_names(fd):
    try:
        if os.lseek(fd, 0, os.SEEK_SET) != 0:
            stop("INVENTORY_REWIND")
        listed = os.listdir(fd)
    except OSError:
        stop("INVENTORY_LIST")
    names = []
    for name in listed:
        if not isinstance(name, str):
            stop("INVENTORY_NAME_TYPE")
        raw = os.fsencode(name)
        try:
            raw.decode("ascii", "strict")
        except UnicodeDecodeError:
            stop("INVENTORY_NAME_ASCII")
        if b"/" in raw or b"\x00" in raw or b"\n" in raw or b"\r" in raw:
            stop("INVENTORY_NAME_BYTES")
        names.append(raw)
    if len(names) != len(set(names)):
        stop("INVENTORY_DUPLICATE")
    return tuple(sorted(names))

def require_inventory(fd, expected):
    before = fstat_checked(fd)
    names = inventory_names(fd)
    after = fstat_checked(fd)
    if directory_key(before) != directory_key(after):
        stop("INVENTORY_DIRECTORY_DRIFT")
    if names != expected:
        stop("INVENTORY_NAMES")
    frame = b"".join(name + b"\n" for name in names)
    if expected == FINAL_NAMES:
        if (
            frame != FINAL_FRAME
            or len(frame) != 64
            or frame.count(b"\n") != 4
            or hashlib.sha256(frame).hexdigest() != FRAME_SHA256
        ):
            stop("INVENTORY_FRAME")
    return frame

def require_source_stat(info):
    if (
        not stat.S_ISREG(info.st_mode)
        or info.st_dev != SOURCE_DEV
        or info.st_ino != SOURCE_INO
        or stat.S_IMODE(info.st_mode) != 0o644
        or info.st_nlink != 1
        or info.st_uid != 0
        or info.st_gid != 0
        or info.st_rdev != 0
        or info.st_size != SOURCE_BYTES
    ):
        stop("SOURCE_STAT")

def verify_source_payload(data):
    if (
        len(data) != SOURCE_BYTES
        or data.count(b"\n") != SOURCE_LF
        or hashlib.sha256(data).hexdigest() != SOURCE_SHA256
        or not data.endswith(SOURCE_TERMINAL)
        or data.count(SOURCE_TERMINAL) != 1
        or data.startswith(b"\xef\xbb\xbf")
        or b"\r" in data
        or b"\x00" in data
    ):
        stop("SOURCE_PAYLOAD")
    try:
        data.decode("utf-8", "strict")
    except UnicodeDecodeError:
        stop("SOURCE_UTF8")

def read_exact(fd, size):
    if size < 0:
        stop("READ_SIZE")
    chunks = []
    offset = 0
    while offset < size:
        amount = min(CHUNK, size - offset)
        try:
            part = os.pread(fd, amount, offset)
        except OSError:
            stop("PREAD")
        if len(part) != amount:
            stop("PREAD_SHORT")
        chunks.append(part)
        offset += amount
    try:
        tail = os.pread(fd, 1, size)
    except OSError:
        stop("PREAD_EOF")
    if tail != b"":
        stop("PREAD_EXTRA")
    data = b"".join(chunks)
    if len(data) != size:
        stop("PREAD_LENGTH")
    return data

def write_payload(fd, payload):
    view = memoryview(payload)
    chunk_start = 0
    while chunk_start < len(view):
        chunk_end = min(chunk_start + CHUNK, len(view))
        offset = chunk_start
        while offset < chunk_end:
            try:
                written = os.write(fd, view[offset:chunk_end])
            except OSError:
                stop("WRITE")
            if written <= 0 or written > chunk_end - offset:
                stop("WRITE_PROGRESS")
            offset += written
        chunk_start = chunk_end

def require_equal_chunks(left, right):
    if len(left) != len(right):
        stop("EQUALITY_LENGTH")
    offset = 0
    while offset < len(left):
        end = min(offset + CHUNK, len(left))
        if left[offset:end] != right[offset:end]:
            stop("EQUALITY_BYTES")
        offset = end

def read_source_at(parent_fd, expected_identity=None):
    before = stat_at(parent_fd, SOURCE_NAME)
    require_source_stat(before)
    if expected_identity is not None and regular_key(before) != expected_identity:
        stop("SOURCE_EXPECTED_IDENTITY")
    fd = open_tracked(SOURCE_NAME, READ_FLAGS, dir_fd=parent_fd)
    inside = fstat_checked(fd)
    if regular_key(before) != regular_key(inside):
        stop("SOURCE_OPEN_REBIND")
    data = read_exact(fd, SOURCE_BYTES)
    last = fstat_checked(fd)
    after = stat_at(parent_fd, SOURCE_NAME)
    if regular_key(before) != regular_key(last) or regular_key(last) != regular_key(after):
        stop("SOURCE_READ_DRIFT")
    verify_source_payload(data)
    return fd, regular_key(before), data

def reread_source(fd, parent_fd, expected_identity):
    before = fstat_checked(fd)
    path_before = stat_at(parent_fd, SOURCE_NAME)
    if regular_key(before) != expected_identity or regular_key(path_before) != expected_identity:
        stop("SOURCE_REREAD_PRE")
    data = read_exact(fd, SOURCE_BYTES)
    after = fstat_checked(fd)
    path_after = stat_at(parent_fd, SOURCE_NAME)
    if regular_key(after) != expected_identity or regular_key(path_after) != expected_identity:
        stop("SOURCE_REREAD_POST")
    verify_source_payload(data)
    return data

def require_created_stat(info, mode, size):
    if (
        not stat.S_ISREG(info.st_mode)
        or info.st_dev != EVIDENCE_DEV
        or info.st_ino <= 0
        or stat.S_IMODE(info.st_mode) != mode
        or info.st_nlink != 1
        or info.st_uid != 0
        or info.st_gid != 0
        or info.st_rdev != 0
        or info.st_size != size
    ):
        stop("CREATED_STAT")

def create_payload(parent_fd, name, mode, payload, used_pairs):
    fd = open_tracked(name, CREATE_FLAGS, dir_fd=parent_fd, mode=mode)
    birth_open = fstat_checked(fd)
    birth_path = stat_at(parent_fd, name)
    require_created_stat(birth_open, mode, 0)
    require_created_stat(birth_path, mode, 0)
    if object_key(birth_open) != object_key(birth_path):
        stop("CREATE_REBIND")
    pair = (birth_open.st_dev, birth_open.st_ino)
    if pair in used_pairs or pair == (SOURCE_DEV, SOURCE_INO):
        stop("CREATE_INODE_ALIAS")
    used_pairs.add(pair)
    write_payload(fd, payload)
    fsync_checked(fd)
    final_open = fstat_checked(fd)
    final_path = stat_at(parent_fd, name)
    require_created_stat(final_open, mode, len(payload))
    require_created_stat(final_path, mode, len(payload))
    if object_key(birth_open) != object_key(final_open) or regular_key(final_open) != regular_key(final_path):
        stop("CREATE_DRIFT")
    fsync_checked(parent_fd)
    return fd, regular_key(final_open), pair

def read_created_at(parent_fd, name, mode, payload, expected_lf, expected_digest, expected_identity):
    before = stat_at(parent_fd, name)
    require_created_stat(before, mode, len(payload))
    if regular_key(before) != expected_identity:
        stop("CREATED_EXPECTED_IDENTITY")
    fd = open_tracked(name, READ_FLAGS, dir_fd=parent_fd)
    inside = fstat_checked(fd)
    if regular_key(inside) != expected_identity:
        stop("CREATED_OPEN_REBIND")
    data = read_exact(fd, len(payload))
    last = fstat_checked(fd)
    after = stat_at(parent_fd, name)
    if regular_key(last) != expected_identity or regular_key(after) != expected_identity:
        stop("CREATED_READ_DRIFT")
    if (
        data != payload
        or data.count(b"\n") != expected_lf
        or hashlib.sha256(data).hexdigest() != expected_digest
    ):
        stop("CREATED_PAYLOAD")
    return fd, data

def emit_stdout(data):
    view = memoryview(data)
    chunk_start = 0
    try:
        while chunk_start < len(view):
            chunk_end = min(chunk_start + CHUNK, len(view))
            offset = chunk_start
            while offset < chunk_end:
                written = os.write(1, view[offset:chunk_end])
                if written <= 0 or written > chunk_end - offset:
                    return False
                offset += written
            chunk_start = chunk_end
    except OSError:
        return False
    return True

def runtime_check():
    if tuple(sys.argv) != ("-c",):
        stop("ARGV")
    if (
        len(sys.orig_argv) != 6
        or tuple(sys.orig_argv[:5])
        != ("/root/miniconda3/bin/python3", "-S", "-B", "-P", "-c")
        or not isinstance(sys.orig_argv[5], str)
        or not sys.orig_argv[5].startswith("import errno\n")
        or not sys.orig_argv[5].endswith("os._exit(0)")
    ):
        stop("ORIG_ARGV")
    if (
        __name__ != "__main__"
        or __spec__ is not None
        or __package__ is not None
        or globals().get("__file__") is not None
        or sys.executable != "/root/miniconda3/bin/python3"
    ):
        stop("DISPATCH")
    if (
        sys.version_info[:2] != (3, 12)
        or not sys.dont_write_bytecode
        or sys.flags.no_site != 1
        or sys.flags.no_user_site != 1
        or sys.flags.safe_path != 1
        or sys.flags.utf8_mode != 1
        or sys.flags.hash_randomization != 0
    ):
        stop("FLAGS")
    if os.getcwdb() != EXPECTED_CWD:
        stop("CWD")
    if dict(os.environb) != EXPECTED_ENV:
        stop("ENV")
    if os.geteuid() != 0 or os.getegid() != 0:
        stop("EFFECTIVE_OWNER")
    if os.umask(0o077) != 0o077:
        stop("UMASK")
    for standard_fd in (0, 1, 2):
        try:
            os.fstat(standard_fd)
        except OSError:
            stop("STANDARD_FD")
    soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft_limit != 4096 or (hard_limit != resource.RLIM_INFINITY and hard_limit < 4096):
        stop("RLIMIT")
    if (
        len(PASS_LINE) != 308
        or PASS_LINE.count(b"\n") != 1
        or not PASS_LINE.endswith(b"\n")
        or b"\r" in PASS_LINE
        or b"\x00" in PASS_LINE
        or hashlib.sha256(PASS_LINE).hexdigest() != PASS_SHA256
    ):
        stop("PASS_FRAME")

def prepare_transaction():
    runtime_check()
    source_chain = open_chain(SOURCE_COMPONENTS)
    source_fd, source_identity, source_data = read_source_at(source_chain[-1])
    evidence_chain = open_chain(EVIDENCE_COMPONENTS)
    evidence_fd = evidence_chain[-1]
    evidence_info = fstat_checked(evidence_fd)
    require_evidence(evidence_info, True)
    evidence_identity = directory_key(evidence_info)
    require_inventory(evidence_fd, ())

    opening_source_chain = rewalk_chain(SOURCE_COMPONENTS, source_chain)
    opening_source_fd, opening_source_identity, opening_source_data = read_source_at(
        opening_source_chain[-1], source_identity
    )
    if opening_source_identity != source_identity:
        stop("OPENING_SOURCE_IDENTITY")
    require_equal_chunks(source_data, opening_source_data)
    opening_evidence_chain = rewalk_chain(EVIDENCE_COMPONENTS, evidence_chain)
    opening_evidence_fd = opening_evidence_chain[-1]
    opening_evidence_info = fstat_checked(opening_evidence_fd)
    require_evidence(opening_evidence_info, True)
    if directory_key(opening_evidence_info) != evidence_identity:
        stop("OPENING_EVIDENCE_IDENTITY")
    require_inventory(opening_evidence_fd, ())
    for name in CREATE_ORDER:
        require_absent(opening_evidence_fd, name)
    reread_source(source_fd, source_chain[-1], source_identity)

    used_pairs = {(SOURCE_DEV, SOURCE_INO)}
    stdout_fd, stdout_identity, stdout_pair = create_payload(
        evidence_fd, STDOUT_NAME, 0o600, b"", used_pairs
    )
    require_inventory(evidence_fd, (STDOUT_NAME,))
    stderr_fd, stderr_identity, stderr_pair = create_payload(
        evidence_fd, STDERR_NAME, 0o600, b"", used_pairs
    )
    require_inventory(evidence_fd, (STDERR_NAME, STDOUT_NAME))
    copy_fd, copy_identity, copy_pair = create_payload(
        evidence_fd, COPY_NAME, 0o500, source_data, used_pairs
    )
    require_inventory(evidence_fd, (COPY_NAME, STDERR_NAME, STDOUT_NAME))

    read_created_at(
        evidence_fd, STDOUT_NAME, 0o600, b"", 0, EMPTY_SHA256, stdout_identity
    )
    read_created_at(
        evidence_fd, STDERR_NAME, 0o600, b"", 0, EMPTY_SHA256, stderr_identity
    )
    copy_probe_fd, copy_probe = read_created_at(
        evidence_fd, COPY_NAME, 0o500, source_data, SOURCE_LF, SOURCE_SHA256, copy_identity
    )
    source_before_status = reread_source(source_fd, source_chain[-1], source_identity)
    require_equal_chunks(source_before_status, copy_probe)

    status_fd, status_identity, status_pair = create_payload(
        evidence_fd, STATUS_NAME, 0o600, b"0\n", used_pairs
    )
    if len({stdout_pair, stderr_pair, copy_pair, status_pair}) != 4:
        stop("CREATED_PAIR_SET")
    require_inventory(evidence_fd, FINAL_NAMES)
    return (
        source_chain,
        source_fd,
        source_identity,
        source_data,
        evidence_chain,
        evidence_fd,
        evidence_identity,
        opening_source_chain,
        opening_source_fd,
        opening_evidence_chain,
        opening_evidence_fd,
        stdout_fd,
        stdout_identity,
        stdout_pair,
        stderr_fd,
        stderr_identity,
        stderr_pair,
        copy_fd,
        copy_identity,
        copy_pair,
        status_fd,
        status_identity,
        status_pair,
    )

def validate_state(context):
    (
        source_chain,
        source_fd,
        source_identity,
        source_data,
        evidence_chain,
        evidence_fd,
        evidence_identity,
        opening_source_chain,
        opening_source_fd,
        opening_evidence_chain,
        opening_evidence_fd,
        stdout_fd,
        stdout_identity,
        stdout_pair,
        stderr_fd,
        stderr_identity,
        stderr_pair,
        copy_fd,
        copy_identity,
        copy_pair,
        status_fd,
        status_identity,
        status_pair,
    ) = context
    require_evidence(fstat_checked(evidence_fd), False)
    require_evidence(fstat_checked(opening_evidence_fd), False)
    if (
        directory_key(fstat_checked(evidence_fd)) != evidence_identity
        or directory_key(fstat_checked(opening_evidence_fd)) != evidence_identity
    ):
        stop("HELD_EVIDENCE_DRIFT")
    require_inventory(evidence_fd, FINAL_NAMES)
    require_inventory(opening_evidence_fd, FINAL_NAMES)
    retained_source = reread_source(source_fd, source_chain[-1], source_identity)
    opening_source = reread_source(
        opening_source_fd, opening_source_chain[-1], source_identity
    )
    require_equal_chunks(retained_source, source_data)
    require_equal_chunks(opening_source, source_data)
    for fd, expected_identity in (
        (stdout_fd, stdout_identity),
        (stderr_fd, stderr_identity),
        (copy_fd, copy_identity),
        (status_fd, status_identity),
    ):
        if regular_key(fstat_checked(fd)) != expected_identity:
            stop("CREATED_FD_DRIFT")

    terminal_source_chain = rewalk_chain(SOURCE_COMPONENTS, source_chain)
    terminal_source_fd, terminal_source_identity, terminal_source_data = read_source_at(
        terminal_source_chain[-1], source_identity
    )
    if terminal_source_identity != source_identity:
        stop("TERMINAL_SOURCE_IDENTITY")
    terminal_evidence_chain = rewalk_chain(EVIDENCE_COMPONENTS, evidence_chain)
    terminal_evidence_fd = terminal_evidence_chain[-1]
    terminal_evidence_info = fstat_checked(terminal_evidence_fd)
    require_evidence(terminal_evidence_info, False)
    if directory_key(terminal_evidence_info) != evidence_identity:
        stop("TERMINAL_EVIDENCE_IDENTITY")
    require_inventory(terminal_evidence_fd, FINAL_NAMES)

    terminal_copy_fd, terminal_copy = read_created_at(
        terminal_evidence_fd,
        COPY_NAME,
        0o500,
        source_data,
        SOURCE_LF,
        SOURCE_SHA256,
        copy_identity,
    )
    terminal_status_fd, terminal_status = read_created_at(
        terminal_evidence_fd,
        STATUS_NAME,
        0o600,
        b"0\n",
        1,
        STATUS_SHA256,
        status_identity,
    )
    terminal_stderr_fd, terminal_stderr = read_created_at(
        terminal_evidence_fd,
        STDERR_NAME,
        0o600,
        b"",
        0,
        EMPTY_SHA256,
        stderr_identity,
    )
    terminal_stdout_fd, terminal_stdout = read_created_at(
        terminal_evidence_fd,
        STDOUT_NAME,
        0o600,
        b"",
        0,
        EMPTY_SHA256,
        stdout_identity,
    )
    require_equal_chunks(terminal_source_data, terminal_copy)
    require_equal_chunks(source_data, terminal_copy)
    if terminal_status != b"0\n" or terminal_stderr != b"" or terminal_stdout != b"":
        stop("TERMINAL_RECEIPTS")
    pairs = {
        fd_pair(terminal_copy_fd),
        fd_pair(terminal_status_fd),
        fd_pair(terminal_stderr_fd),
        fd_pair(terminal_stdout_fd),
    }
    if pairs != {copy_pair, status_pair, stderr_pair, stdout_pair}:
        stop("TERMINAL_PAIR_SET")

try:
    transaction = prepare_transaction()
    validate_state(transaction)
    if not emit_stdout(PASS_LINE):
        stop("STDOUT")
    validate_state(transaction)
except BaseException:
    close_all()
    os._exit(1)

if not close_all():
    os._exit(1)
os._exit(0)
BATCH07_P27_RECOVERY_E001_FIRST_COPY_HARNESS_END

Static delimiter-only extraction at author stop gives these exact identities:

```text
raw_record_bytes=22671
raw_record_LF=714
raw_record_sha256=02834994db821c0dcf9b6c06e58511686d0786b9012c68ce89af6de52806bbcb
raw_record_final_bytes=29,0a
normalized_bytes=22670
normalized_LF=713
normalized_physical_lines=714
normalized_sha256=6a07c364878cce79a6166cd16e9f941f402569dae9802b671c2998ee49e48ea0
normalized_final_byte=29
normalized_single_quote_count=0
normalized_dollar_count=0
normalized_backtick_count=0
```

The extraction selected the unique BEGIN-through-END region, deleted only
the two marker lines, and removed exactly the raw record's final delimiter LF
for the normalized identity.  It did not parse, compile, import, or execute
Python.  The final byte `0x29` is `)`.  The three zero censuses make the
displayed single-quoted transport literal and non-interpolating.  W1/W2 must
bind these exact identities, not a pattern or prefix.

## 4. Exclusive creation, durability, and synthetic receipts

Before the first create, the harness no-follow stats all four literal names
relative to the freshly rewalked evidence FD and accepts only `ENOENT` for
each.  The empty opening inventory separately proves there is no unknown
entry.  Absence preflight does not replace exclusive creation.

The only creation flags are
`O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC`, relative to the retained
evidence FD.  The exact order is:

1. `E001.stdout`, mode 0600, empty;
2. `E001.stderr`, mode 0600, empty;
3. `BUILD_VALIDATOR_RECOVERY.py`, mode 0500, exact source bytes;
4. `E001.status`, mode 0600, exact `0` plus LF.

Each new file is immediately fstat/lstat-bound, must be regular on device
2431 with exact mode, nlink one, uid/gid zero, and is fsynced.  The retained
evidence directory is fsynced after every individual create.  All four
`(dev,ino)` pairs must be distinct and none may equal source
`(2431,5913826453)`.  There is no truncate, chmod/fchmod repair, chown,
temporary destination, rename, fallback name, second write-open, or cleanup.

Each positional read requests at most 65,536 bytes.  It must return exactly
the requested amount; a zero or positive short pread fails without retry,
followed by a one-byte EOF probe at the exact frozen length.  A positive
short write may continue only within the same fixed chunk on the same FD; it
is I/O completion, not a transaction retry.  Source and copy are directly
compared chunk by chunk; equal hashes alone are insufficient.

The receipt triple is synthetic canonical provenance for the internal
first-copy suboperation.  It is not fd1/fd2/status capture from
`/usr/bin/install`, which does not run.  Outer harness stdout, stderr, and wait
status are separate out-of-band results.  Redirecting outer output into an
E001 receipt, or later backfilling a receipt, is forbidden.

`E001.status` is created last only after the two empty receipts and copy have
been fsynced, reopened, reread, and validated.  It is not a commit record.
Terminal checks, PASS emission, post-emission checks, descriptor closes, raw
capture, and ledger binding can still fail.  A full four-file set containing
`0` plus LF is non-authoritative unless the complete outer success
conjunction and immediate physical ledger binding pass.

## 5. Exact poststate and inventory

The only accepted four files are:

| Name | Type | Mode | nlink | uid/gid | Bytes | LF | SHA-256 |
|---|---|---:|---:|---:|---:|---:|---|
| `BUILD_VALIDATOR_RECOVERY.py` | regular | 0500 | 1 | 0/0 | 398310 | 9366 | `6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817` |
| `E001.status` | regular | 0600 | 1 | 0/0 | 2 | 1 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `E001.stderr` | regular | 0600 | 1 | 0/0 | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `E001.stdout` | regular | 0600 | 1 | 0/0 | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The exact byte-sorted name frame is:

```text
BUILD_VALIDATOR_RECOVERY.py
E001.status
E001.stderr
E001.stdout
```

It is the 64-byte preimage
`BUILD_VALIDATOR_RECOVERY.py\nE001.status\nE001.stderr\nE001.stdout\n`,
with four items, four LF bytes, and SHA-256
`7aeb029ca886a47abeb0bd05a4f941c820983dc6e90925880ff7e297f92dbcde`.
Enumeration is from held directory FDs, rejects unknown, non-ASCII,
surrogate, malformed, or duplicate names, and never constructs a path from an
enumerated name.  Every leaf operation uses one of the four frozen literals.

The first `validate_state` performs the complete pre-emission terminal
source/evidence rewalk, fresh no-follow source/evidence opens, four fresh leaf
opens, inventory, content, inode, link, and direct equality checks.  All held
and fresh descriptors remain live through the direct write-all PASS emission.
The second `validate_state` repeats fstat, inventory, source/content equality,
and a new complete terminal-chain rewalk after emission.  Only then are all
nonstandard descriptors closed.  Close continues over every descriptor after
one close error, remembers failure, never retries an interrupted close, and
forces process status one.  Thus complete PASS bytes followed by any
post-emission or close failure are rejected.

## 6. Exact outer transcript and capture

The only accepted stdout bytes are this line with exactly one terminal LF:

```text
PASS E001_FIRST_COPY_RECOVERY evidence_dev=2431 evidence_ino=14502900794 copy_bytes=398310 copy_LF=9366 copy_sha256=6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817 inventory_items=4 inventory_framing_bytes=64 inventory_sha256=7aeb029ca886a47abeb0bd05a4f941c820983dc6e90925880ff7e297f92dbcde
```

Including that LF, it is 308 bytes, one LF, and SHA-256
`b149a22827939aff6a6875a4797076a7e32f8ada246dee0e2f3a7aa490247c5b`.
There is no CR, NUL, trailing space, prefix matching, extra line, or variable
field.  Success is only the conjunction:

```text
outer wait status = 0
outer stderr = empty
outer stdout = the exact 308 bytes above
both terminal physical validation passes completed
all descriptor closes completed
the physically next ledger event binds the exact outcome
```

The controller must use separate in-memory byte pipes for raw stdout and raw
stderr, retain the terminal LF, reap the process before classification, and
create no build-path capture, temporary, or receipt file.  `PASS ` text alone
has no authority.  `BaseException` is caught without a Python traceback; any
loader/Bash stderr byte or signal also rejects success.

## 7. Failure preservation and exact partial-state binder

The first launcher invocation consumes the one attempt whether it succeeds,
returns nonzero, is signaled, times out, emits malformed stdout, emits any
stderr, or fails a physical predicate.  Descriptor cleanup is the only
cleanup.  Every existing partial byte is preserved.  There is no delete,
truncate, rename, chmod, repair, backfill, second E001 payload process,
absence-check reuse, suffix fallback, or retry.  E010, A000, stages, roots,
validator execution, PDF work, and release remain closed after failure.

The later execution authorization must co-authorize exactly one immediate
read-only failure binder, which is not an E001 retry or payload process.  It
runs only after a failed first launch and remains within the same
single-writer interval.  Through complete retained no-follow source and
evidence chains, with no mutation, it records in the physically next ledger
event:

- raw outer stdout and stderr bytes, byte counts, LF counts, and SHA-256;
- numeric exit status, or exact terminating signal/timeout classification;
- evidence dev, ino, type/mode, nlink, uid, gid, and current entry count;
- the byte-sorted current inventory frame, its byte/LF count and SHA-256;
- every unexpected returned basename as raw-byte hex only, without using it
  to form or open a path;
- for each of the four frozen candidate literals, `absent`, or exact no-follow
  type, mode, nlink, uid, gid, bytes, LF, and SHA-256;
- source dev, ino, type/mode, nlink, uid, gid, bytes, LF, SHA-256, and terminal;
- whether `E001.status` exists, always labelled non-authoritative;
- the last safely inferable phase: `pre-create`, `stdout-durable`,
  `stderr-durable`, `copy-durable`, `status-durable-or-later`,
  `post-emission-failure`, or `unknown-mismatch`.

The prefix phase is inferred only when the exact inventory is respectively
empty; stdout only; stdout plus stderr; those two plus the copy; or all four
exact names with every preceding object valid.  Exact PASS stdout with a
nonzero/signal outcome is `post-emission-failure`.  Any other state is
`unknown-mismatch`.  The binder opens unknown names never, changes nothing,
and cannot authorize a second launch.  Failure before creation binds the
still-empty directory; failure after creation binds the exact preserved
prefix or mismatch.

## 8. Four-name handoff and unchanged A000 frame

Immediately after successful supplemental E001, evidence has nlink two and
exactly the four-name, 64-byte frame above.  This supplemental creates no
transcript, marker, control copy, temporary, or extra evidence entry.

Unchanged E010 later, only under separate authority, adds `r0` and the three
E010 receipts.  Root-0 A000 must then see exactly this byte-sorted eight-name
frame:

```text
BUILD_VALIDATOR_RECOVERY.py
E001.status
E001.stderr
E001.stdout
E010.status
E010.stderr
E010.stdout
r0
```

That frame has eight names, 103 bytes, eight LF bytes, and SHA-256
`72b0a3948e4c178327e5ce944f2e6887ce26b22a23d9a5a376d762719f8e4a8b`;
evidence then has nlink three.  The unchanged validator A000 predicate remains
authoritative.  This notes file enters the later canonical project
source/control manifest as immutable history but remains absent from the
validator's unchanged five-control runtime set.

## 9. Required separated reviews and activation gate

W1 is the invariant/lifecycle reviewer.  It must independently bind exact
control and marker identities; source/evidence/tool identities; E0280,
argv/cwd/environment/umask/FD/RLIMIT; no validator execution or install;
opening and both pre/post-emission terminal rewalks; exclusive order;
per-child file and directory fsync; strict pread/write semantics; direct
equality; ownership/link/inode separation; four/eight name frames; transcript;
synthetic provenance; failure binder; precedence; expiry; and zero later
authority.

W2 is the adversarial reviewer.  It must independently close circularity,
symlink/hard-link/overwrite, ancestor/evidence/source replacement, mount,
TOCTOU, short-I/O, fsync, status-as-false-commit, PASS-before-close,
post-emission failure, close-error, stderr/terminal-LF capture, partial-prefix,
unexpected-inventory, second-process/retry, control-runtime leakage, A000
compatibility, and single-writer counterexamples.

Each report must independently have
`Blocker=0; Major=0; Minor=0; Ambiguity=0`.  One report cannot waive, cure, or
outvote a finding in the other.  Only a later physical ledger event may bind
this author stop, both exact all-zero reviews, static harness transport
identities and censuses, current frozen inputs/tools, and then authorize the
one process plus its immediate result binder.  Until then, execution and all
build-path access remain none.

BATCH07_P27_E001_FIRST_COPY_RECOVERY_AUTHOR_STOP
