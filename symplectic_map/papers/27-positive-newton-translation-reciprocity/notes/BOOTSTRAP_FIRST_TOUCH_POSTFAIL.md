# Paper 27 post-failure evidence first-touch control

This append-only supplemental control resolves only the bootstrap circularity recorded by Batch 07 E0296. It does not edit the frozen profile, validator, lock, reviews, old evidence, or old roots.

## Narrow precedence

For exactly one operation—the first creation of build/postfail-d60ec6611683-evidence—this control supersedes only BUILD_PROFILE_POSTFAIL Sections 3 and 10 where they require an on-disk three-receipt row and evidence-validator no-follow checks before the evidence directory or validator copy exists. Section 4 direct physical-ledger capture governs this one operation.

This exception ends permanently when the physical bootstrap result is ledger-bound. E001 and every later operation immediately return to the complete frozen profile: E0280 wrapper, three exclusive mode-0600 receipts, exact environments, validator lock, first-failure preservation, and no retry.

This control grants no E001, E010, A000, certified-root, root-1, cross-root, PDF, build-evidence, release, Paper-28, cleanup, rollback, rename, fallback, or external authority.

The only runtime leaf is:
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/postfail-d60ec6611683-evidence

The harness contains no predecessor namespace and no new r0, r1, evidence/r0, evidence/r1, or cross-root path.

## Opening identities

A later execution authorizer must rebind before any build-path touch:

- E0296 BATCH_07_STATUS.md: 1517548 bytes; 17995 LF; 0644; nlink 1; SHA-256 ed269b8d7f503fa90fe340432d4aabc87989ea84549fcc7bfbacfc6da4975ad6; terminal BATCH07_P27_POSTFAIL_BOOTSTRAP_PLAN_FAILURE_RECORDED_AND_FIRST_TOUCH_CONTROL_AUTHORIZED.
- BUILD_PROFILE_POSTFAIL.md: 53878 bytes; 963 LF; SHA-256 f4829e21e4626b372a05e646f34d29f0ea306b653d23d6dd924d1fc54161687e.
- INDEPENDENT_BUILD_PROFILE_POSTFAIL_REVIEW.md: 13492 bytes; 248 LF; SHA-256 b1bbdf96dc68ae1ee4e6ce984616c106931c5f2d462117808f8747f6496d887b.
- BUILD_VALIDATOR_POSTFAIL.py: 398307 bytes; 9366 LF; SHA-256 6103a9df0c3d3fec652b9b39e0407b6a35eb369a7950d1b1724c8918fbe57693.
- VALIDATOR_LOCK_POSTFAIL.md: 63861 bytes; 1168 LF; SHA-256 72d3bf2175c983f91b2cbe39c05271638bbcc23409dd7ed42a0acc6133501d63.
- INDEPENDENT_VALIDATOR_POSTFAIL_REVIEW.md: 11954 bytes; 246 LF; SHA-256 b248796cde7a5f68d4c532bf62c8162b2ab8a4ec8962357b317ab768d7254b09.

The next authorizer also rebinds this control and its two all-zero reviews, E0295 physical parser-microtest PASS, /usr/bin/env, /usr/bin/bash, and /root/miniconda3/bin/python3 plus its python3.12 target. Source/control/tool checks touch no build path.

Frozen executable identities are:

- /usr/bin/env: 43976 bytes; 0755; nlink 1; SHA-256 85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0.
- /usr/bin/bash: 1396520 bytes; 0755; nlink 1; SHA-256 59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4.
- /root/miniconda3/bin/python3: ten-byte symlink to python3.12; target /root/miniconda3/bin/python3.12 is 30626264 bytes, 0755, nlink 1, SHA-256 9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101.

## Exact launcher and inner process

The one process chain uses exact argv:
/usr/bin/env -i /usr/bin/bash --noprofile --norc -c LITERAL_E0280_LAUNCHER batch07-p27-successor-liveness-fd-scrub-launcher LITERAL_INNER

BATCH07_P27_BOOTSTRAP_E0280_BEGIN
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
BATCH07_P27_BOOTSTRAP_E0280_END

The exact inner script is:
set -C
umask 077
cd -- /root/autodl-tmp/symplectic_map || exit 125
exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -S -B -P -c LITERAL_HARNESS

LITERAL_HARNESS is exactly the byte substring after the following BEGIN LF and before the LF preceding END. Two independent static reviewers and the later authorizer must bind its bytes, LF count, SHA-256, terminal byte, and shell-sensitive-character census.

BATCH07_P27_BOOTSTRAP_HARNESS_BEGIN
import errno
import os
import stat
import sys

COMPONENTS = (
    "root",
    "autodl-tmp",
    "symplectic_map",
    "papers",
    "27-positive-newton-translation-reciprocity",
    "build",
)
LEAF = "postfail-d60ec6611683-evidence"
EXPECTED_CWD = "/root/autodl-tmp/symplectic_map"
EXPECTED_ENV = {
    "LANG": "C",
    "LC_ALL": "C",
    "PATH": "/usr/bin:/bin",
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
    "PYTHONIOENCODING": "UTF-8:strict",
    "PYTHONNOUSERSITE": "1",
    "PYTHONSAFEPATH": "1",
    "PYTHONUTF8": "1",
    "TZ": "UTC",
}

def fail(predicate):
    print("FAIL BOOTSTRAP predicate=" + predicate)
    raise SystemExit(1)

if sys.argv != ["-c"]:
    fail("ARGV")
if os.getcwd() != EXPECTED_CWD:
    fail("CWD")
if dict(os.environ) != EXPECTED_ENV:
    fail("ENV")
old_umask = os.umask(0o077)
if old_umask != 0o077:
    fail("UMASK")

flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
parent_fd = os.open("/", flags)
try:
    for component in COMPONENTS:
        next_fd = os.open(component, flags, dir_fd=parent_fd)
        os.close(parent_fd)
        parent_fd = next_fd
    parent_before = os.fstat(parent_fd)
    if not stat.S_ISDIR(parent_before.st_mode):
        fail("PARENT_TYPE")
    try:
        os.stat(LEAF, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError as error:
        if error.errno != errno.ENOENT:
            fail("LEAF_ABSENCE_ERRNO")
    else:
        fail("LEAF_PRESENT")
    os.mkdir(LEAF, 0o700, dir_fd=parent_fd)
    child_fd = os.open(LEAF, flags, dir_fd=parent_fd)
    try:
        child_info = os.fstat(child_fd)
        leaf_info = os.stat(LEAF, dir_fd=parent_fd, follow_symlinks=False)
        fields = ("st_dev", "st_ino", "st_mode", "st_nlink", "st_uid", "st_gid")
        if any(getattr(child_info, name) != getattr(leaf_info, name) for name in fields):
            fail("LEAF_REBIND")
        if not stat.S_ISDIR(child_info.st_mode):
            fail("LEAF_TYPE")
        if stat.S_IMODE(child_info.st_mode) != 0o700:
            fail("LEAF_MODE")
        if child_info.st_nlink != 2:
            fail("LEAF_NLINK")
        if child_info.st_uid != os.geteuid() or child_info.st_gid != os.getegid():
            fail("LEAF_OWNER")
        if os.listdir(child_fd) != []:
            fail("LEAF_NONEMPTY")
        os.fsync(child_fd)
        os.fsync(parent_fd)
        child_after = os.fstat(child_fd)
        parent_after = os.fstat(parent_fd)
        if any(getattr(child_info, name) != getattr(child_after, name) for name in fields):
            fail("LEAF_DRIFT")
        if (parent_before.st_dev != parent_after.st_dev or
                parent_before.st_ino != parent_after.st_ino or
                parent_before.st_mode != parent_after.st_mode or
                parent_before.st_uid != parent_after.st_uid or
                parent_before.st_gid != parent_after.st_gid):
            fail("PARENT_DRIFT")
        if os.listdir(child_fd) != []:
            fail("LEAF_POSTSYNC_NONEMPTY")
        print(
            "PASS BOOTSTRAP"
            + " parent_dev=" + str(parent_after.st_dev)
            + " parent_ino=" + str(parent_after.st_ino)
            + " evidence=" + LEAF
            + " dev=" + str(child_after.st_dev)
            + " ino=" + str(child_after.st_ino)
            + " bytes=" + str(child_after.st_size)
            + " mode=0700 nlink=2"
            + " uid=" + str(child_after.st_uid)
            + " gid=" + str(child_after.st_gid)
            + " entries=0"
        )
    finally:
        os.close(child_fd)
finally:
    os.close(parent_fd)
BATCH07_P27_BOOTSTRAP_HARNESS_END

The harness has no cleanup branch. Its finally blocks close process-local descriptors only. Any failure after os.mkdir preserves the new directory and permanently stops.

## Capture and grammar

Success is one printable-ASCII LF-terminated line with this exact positional grammar:
PASS BOOTSTRAP parent_dev=D parent_ino=I evidence=postfail-d60ec6611683-evidence dev=D ino=I bytes=B mode=0700 nlink=2 uid=U gid=G entries=0

Each D, I, B, U, and G is one canonical decimal 0|[1-9][0-9]*; repeated letters are explanatory, except the two device values must compare equal. Status must be zero and stderr empty.

One in-memory command-substitution capture appends a non-newline status sentinel. It opens no temporary file and creates no receipt. Child stderr remains externally visible. Only after status and full grammar pass does the supervisor re-emit the exact child stdout. The physical ledger binds exact stdout bytes/LF/SHA-256, parent and child metadata, opening authorizer, all controls/tools, argv/environment/cwd, empty stderr, and empty inventory. No later receipt backfills this action.

A controlled failure may print one FAIL BOOTSTRAP predicate=NAME line and return one. An unexpected exception may write stderr. Every non-success is permanent; no second absence check, mkdir, process chain, retry, cleanup, deletion, chmod, rename, fallback, or repair is allowed.

## Post-bootstrap handoff

Only a later physical PASS-binding event may authorize a separately reviewed E001 plan. E001 installs the exact frozen validator source once as mode 0500 with E001.stdout, E001.stderr, and E001.status inside the existing evidence directory. E010 then creates only evidence/r0 with receipts. A000 and the r0 certified root remain unauthorized until E001 and E010 are physically bound PASS. Root 1 and cross-root remain unopened.

BATCH07_P27_BOOTSTRAP_FIRST_TOUCH_POSTFAIL_AUTHOR_STOP
