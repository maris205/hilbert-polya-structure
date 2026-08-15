#!/usr/bin/env python3
"""Rollback-atomic grouped promotion for the four HCS-C56 JSON results.

This is deliberately not described as multi-file filesystem atomicity.  It
stages and validates the complete group before touching a target, replaces the
four targets one at a time, and restores the exact pre-image if any move (or a
test-injected failure after a move) fails.
"""

from __future__ import annotations

import argparse
import errno
import hashlib
import os
import stat
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn, Sequence


EXPECTED_TARGET_NAMES: tuple[str, ...] = (
    "c56_certificate.json",
    "c56_schema.json",
    "c56_check_report.json",
    "scoped_hash_manifest.json",
)

_FSYNC_UNAVAILABLE = {
    errno.EBADF,
    errno.EINVAL,
    errno.ENOSYS,
    errno.EROFS,
}
if hasattr(errno, "ENOTSUP"):
    _FSYNC_UNAVAILABLE.add(errno.ENOTSUP)


class PromotionValidationError(ValueError):
    """The requested transaction is outside the fixed C56 result scope."""


class PromotionRollbackError(RuntimeError):
    """Rollback or its exact post-rollback verification failed."""


@dataclass(frozen=True)
class _Fingerprint:
    sha256: str
    size: int
    mode: int


@dataclass
class _Entry:
    source: Path
    target: Path
    staged: Path
    backup: Path
    source_fingerprint: _Fingerprint
    preimage: _Fingerprint | None


def _reject_optimized_python() -> None:
    if not __debug__ or "PYTHONOPTIMIZE" in os.environ:
        raise PromotionValidationError(
            "optimized Python and the PYTHONOPTIMIZE environment variable are forbidden"
        )


def _lexists(path: Path) -> bool:
    return os.path.lexists(os.fspath(path))


def _regular_lstat(path: Path, description: str) -> os.stat_result:
    try:
        metadata = path.lstat()
    except FileNotFoundError as exc:
        raise PromotionValidationError(f"missing {description}: {path}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise PromotionValidationError(
            f"{description} must be a non-symlink regular file: {path}"
        )
    return metadata


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    flags = os.O_RDONLY
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(path, flags)
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise PromotionValidationError(f"not a regular file: {path}")
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
        after = os.fstat(descriptor)
        stable_fields = (
            "st_dev",
            "st_ino",
            "st_size",
            "st_mtime_ns",
            "st_ctime_ns",
            "st_mode",
        )
        if any(getattr(before, key) != getattr(after, key) for key in stable_fields):
            raise PromotionValidationError(f"file changed while being read: {path}")
    finally:
        os.close(descriptor)
    return digest.hexdigest()


def _fingerprint(path: Path) -> _Fingerprint:
    metadata = _regular_lstat(path, "file")
    digest = _sha256(path)
    current = _regular_lstat(path, "file")
    if (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
        metadata.st_mode,
    ) != (
        current.st_dev,
        current.st_ino,
        current.st_size,
        current.st_mtime_ns,
        current.st_ctime_ns,
        current.st_mode,
    ):
        raise PromotionValidationError(f"file changed while fingerprinting: {path}")
    return _Fingerprint(
        sha256=digest,
        size=current.st_size,
        mode=stat.S_IMODE(current.st_mode),
    )


def _fsync_descriptor(descriptor: int) -> None:
    try:
        os.fsync(descriptor)
    except OSError as exc:
        if exc.errno not in _FSYNC_UNAVAILABLE:
            raise


def _fsync_file(path: Path) -> None:
    flags = os.O_RDONLY
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(path, flags)
    try:
        _fsync_descriptor(descriptor)
    finally:
        os.close(descriptor)


def _fsync_directory(path: Path) -> None:
    flags = os.O_RDONLY
    if hasattr(os, "O_DIRECTORY"):
        flags |= os.O_DIRECTORY
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    descriptor = os.open(path, flags)
    try:
        _fsync_descriptor(descriptor)
    finally:
        os.close(descriptor)


def _copy_regular_file(source: Path, destination: Path, mode: int) -> None:
    """Copy a stable source without following symlinks, then fsync the copy."""
    read_flags = os.O_RDONLY
    if hasattr(os, "O_CLOEXEC"):
        read_flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        read_flags |= os.O_NOFOLLOW
    write_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        write_flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        write_flags |= os.O_NOFOLLOW

    source_fd = os.open(source, read_flags)
    destination_fd = -1
    try:
        before = os.fstat(source_fd)
        if not stat.S_ISREG(before.st_mode):
            raise PromotionValidationError(f"source is not regular: {source}")
        destination_fd = os.open(destination, write_flags, 0o600)
        while True:
            chunk = os.read(source_fd, 1024 * 1024)
            if not chunk:
                break
            view = memoryview(chunk)
            while view:
                written = os.write(destination_fd, view)
                if written <= 0:
                    raise OSError("short write while staging promotion input")
                view = view[written:]
        after = os.fstat(source_fd)
        stable_fields = (
            "st_dev",
            "st_ino",
            "st_size",
            "st_mtime_ns",
            "st_ctime_ns",
            "st_mode",
        )
        if any(getattr(before, key) != getattr(after, key) for key in stable_fields):
            raise PromotionValidationError(f"source changed while staging: {source}")
        os.fchmod(destination_fd, mode)
        _fsync_descriptor(destination_fd)
    finally:
        if destination_fd >= 0:
            os.close(destination_fd)
        os.close(source_fd)


def _validate_request(
    pairs: Sequence[tuple[Path, Path]], result_dir: Path, fail_after: int | None
) -> tuple[Path, list[tuple[Path, Path, _Fingerprint, _Fingerprint | None]]]:
    _reject_optimized_python()
    if len(pairs) != 4:
        raise PromotionValidationError("exactly four source/target pairs are required")
    if fail_after is not None and fail_after not in range(1, 5):
        raise PromotionValidationError("--fail-after must be one of 1, 2, 3, or 4")

    if result_dir.is_symlink():
        raise PromotionValidationError("result directory must not be a symlink")
    try:
        result_metadata = result_dir.stat()
    except FileNotFoundError as exc:
        raise PromotionValidationError(
            f"result directory must already exist: {result_dir}"
        ) from exc
    if not stat.S_ISDIR(result_metadata.st_mode):
        raise PromotionValidationError(f"result directory is not a directory: {result_dir}")
    result_dir = result_dir.resolve(strict=True)

    target_names = tuple(target.name for _, target in pairs)
    if target_names != EXPECTED_TARGET_NAMES:
        raise PromotionValidationError(
            "targets must occur exactly in this order: "
            + ", ".join(EXPECTED_TARGET_NAMES)
        )

    validated: list[tuple[Path, Path, _Fingerprint, _Fingerprint | None]] = []
    source_paths: set[Path] = set()
    source_inodes: set[tuple[int, int]] = set()
    for source_argument, target_argument in pairs:
        source = Path(source_argument)
        target = Path(target_argument)
        source_metadata = _regular_lstat(source, "staged source")
        source = source.resolve(strict=True)
        source_metadata = _regular_lstat(source, "staged source")
        if source_metadata.st_dev != result_metadata.st_dev:
            raise PromotionValidationError(
                f"staged source and result directory are on different filesystems: {source}"
            )
        inode = (source_metadata.st_dev, source_metadata.st_ino)
        if source in source_paths or inode in source_inodes:
            raise PromotionValidationError("the four staged sources must be distinct files")
        source_paths.add(source)
        source_inodes.add(inode)

        if target.parent.resolve(strict=True) != result_dir:
            raise PromotionValidationError(f"target is outside the result directory: {target}")
        target = result_dir / target.name
        if target.is_symlink():
            raise PromotionValidationError(f"target must not be a symlink: {target}")
        if source == target:
            raise PromotionValidationError(f"source and target must differ: {target}")

        source_fingerprint = _fingerprint(source)
        preimage: _Fingerprint | None
        if _lexists(target):
            preimage = _fingerprint(target)
        else:
            preimage = None
        validated.append((source, target, source_fingerprint, preimage))
    return result_dir, validated


def _verify_preimages(entries: Sequence[_Entry]) -> None:
    problems: list[str] = []
    for entry in entries:
        if entry.preimage is None:
            if _lexists(entry.target):
                problems.append(f"expected absent target: {entry.target}")
        else:
            try:
                actual = _fingerprint(entry.target)
            except Exception as exc:  # Verification must report the whole rollback failure.
                problems.append(f"unreadable restored target {entry.target}: {exc}")
            else:
                if actual != entry.preimage:
                    problems.append(f"restored target differs from pre-image: {entry.target}")
    if problems:
        raise PromotionRollbackError("; ".join(problems))


def _remove_if_present(path: Path) -> None:
    if _lexists(path):
        path.unlink()


def _cleanup_transaction(entries: Sequence[_Entry], transaction_dir: Path) -> None:
    for entry in entries:
        _remove_if_present(entry.staged)
        _remove_if_present(entry.backup)
    if _lexists(transaction_dir):
        _fsync_directory(transaction_dir)
        transaction_dir.rmdir()


def promote(
    pairs: Sequence[tuple[Path, Path]],
    fail_after: int | None = None,
    *,
    result_dir: Path | None = None,
) -> bool:
    """Promote the fixed four-file C56 group.

    Validation errors raise :class:`PromotionValidationError`.  A transactional
    failure returns ``False`` only after exact rollback and cleanup have been
    verified.  An unverifiable rollback raises :class:`PromotionRollbackError`.
    """
    path_pairs = [(Path(source), Path(target)) for source, target in pairs]
    if result_dir is None:
        if not path_pairs:
            raise PromotionValidationError("no promotion pairs supplied")
        parents = {target.parent.resolve(strict=True) for _, target in path_pairs}
        if len(parents) != 1:
            raise PromotionValidationError("all targets must have one result directory")
        result_dir = next(iter(parents))
    result_dir, validated = _validate_request(path_pairs, Path(result_dir), fail_after)

    transaction = uuid.uuid4().hex
    transaction_dir = result_dir / f".c56-promote-{transaction}"
    lock_path = result_dir / ".c56-atomic-promote.lock"
    lock_fd = -1
    entries: list[_Entry] = []
    transaction_failed = False
    rollback_error: BaseException | None = None
    lock_owned = False
    transaction_dir_owned = False

    lock_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        lock_flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        lock_flags |= os.O_NOFOLLOW
    try:
        lock_fd = os.open(lock_path, lock_flags, 0o600)
    except FileExistsError as exc:
        raise PromotionValidationError(
            f"another promotion may be active (lock exists): {lock_path}"
        ) from exc
    lock_owned = True
    try:
        os.write(lock_fd, (transaction + "\n").encode("ascii"))
        _fsync_descriptor(lock_fd)
        transaction_dir.mkdir(mode=0o700)
        transaction_dir_owned = True
        _fsync_directory(result_dir)

        for index, (source, target, source_fp, preimage) in enumerate(validated):
            staged = transaction_dir / f"{index:02d}-{target.name}.new"
            backup = transaction_dir / f"{index:02d}-{target.name}.bak"
            entry = _Entry(
                source=source,
                target=target,
                staged=staged,
                backup=backup,
                source_fingerprint=source_fp,
                preimage=preimage,
            )
            # Register paths before copying so a partial copy is cleaned on any
            # write/fsync failure.
            entries.append(entry)
            _copy_regular_file(source, staged, source_fp.mode)
            staged_fingerprint = _fingerprint(staged)
            if staged_fingerprint != source_fp:
                raise RuntimeError(f"staged copy does not match source: {source}")
        _fsync_directory(transaction_dir)

        # Recheck every live pre-image immediately before the first live move.
        _verify_preimages(entries)

        for move, entry in enumerate(entries, 1):
            if entry.preimage is not None:
                os.replace(entry.target, entry.backup)
                _fsync_file(entry.backup)
                _fsync_directory(transaction_dir)
                _fsync_directory(result_dir)
            os.replace(entry.staged, entry.target)
            _fsync_file(entry.target)
            _fsync_directory(transaction_dir)
            _fsync_directory(result_dir)
            if _fingerprint(entry.target) != entry.source_fingerprint:
                raise RuntimeError(f"promoted target does not match staged source: {entry.target}")
            if fail_after == move:
                raise RuntimeError(f"injected promotion failure after move {move}")

        # The live group is complete and verified before pre-image backups go.
        for entry in entries:
            if _fingerprint(entry.target) != entry.source_fingerprint:
                raise RuntimeError(f"live target verification failed: {entry.target}")
        _fsync_directory(result_dir)

    except (PromotionValidationError, PromotionRollbackError):
        # Pre-transaction validation is outside this block; failures here may
        # occur after live moves, so they must use the same rollback path.
        transaction_failed = True
    except BaseException:
        transaction_failed = True

    if transaction_failed:
        try:
            # Reverse order is important when a failure lands between a backup
            # move and installation of its replacement.
            for entry in reversed(entries):
                if _lexists(entry.backup):
                    os.replace(entry.backup, entry.target)
                    _fsync_file(entry.target)
                    _fsync_directory(transaction_dir)
                elif entry.preimage is None:
                    _remove_if_present(entry.target)
                # With a non-null pre-image and no backup, this entry was not
                # touched.  Exact verification below distinguishes that case
                # from missing/corrupt state.
                _fsync_directory(result_dir)
            _verify_preimages(entries)
            if transaction_dir_owned:
                _cleanup_transaction(entries, transaction_dir)
            _fsync_directory(result_dir)
        except BaseException as exc:
            rollback_error = exc
    else:
        try:
            if transaction_dir_owned:
                _cleanup_transaction(entries, transaction_dir)
            _fsync_directory(result_dir)
        except BaseException as exc:
            # The four live files are already a verified complete group.  A
            # cleanup failure is nevertheless fail-closed and cannot be called
            # a successful transaction.
            rollback_error = PromotionRollbackError(
                f"promotion completed but transaction debris cleanup failed: {exc}"
            )

    try:
        if lock_fd >= 0:
            os.close(lock_fd)
            lock_fd = -1
        if lock_owned:
            _remove_if_present(lock_path)
            _fsync_directory(result_dir)
    except BaseException as exc:
        if rollback_error is None:
            rollback_error = PromotionRollbackError(f"lock cleanup failed: {exc}")

    if rollback_error is not None:
        raise PromotionRollbackError(str(rollback_error)) from rollback_error
    return not transaction_failed


def _die(message: str, status: int) -> NoReturn:
    print(f"c56_atomic_promote: {message}", file=sys.stderr)
    raise SystemExit(status)


def main(argv: Sequence[str] | None = None) -> int:
    try:
        _reject_optimized_python()
    except PromotionValidationError as exc:
        print(f"c56_atomic_promote: {exc}", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(
        description="rollback-atomically promote the fixed four-file C56 result group"
    )
    parser.add_argument("--result-dir", required=True, type=Path)
    parser.add_argument("--source", action="append", required=True, type=Path)
    parser.add_argument(
        "--target",
        action="append",
        required=True,
        type=Path,
        help="target path, or one of the four target basenames relative to --result-dir",
    )
    parser.add_argument("--fail-after", type=int, choices=range(1, 5))
    arguments = parser.parse_args(argv)
    if len(arguments.source) != 4 or len(arguments.target) != 4:
        parser.error("exactly four --source and four --target arguments are required")

    result_dir = arguments.result_dir
    targets: list[Path] = []
    for target in arguments.target:
        targets.append(result_dir / target if target.parent == Path(".") else target)
    try:
        success = promote(
            list(zip(arguments.source, targets)),
            arguments.fail_after,
            result_dir=result_dir,
        )
    except (PromotionValidationError, PromotionRollbackError, OSError) as exc:
        _die(str(exc), 2)
    print("promotion=" + ("COMMITTED" if success else "ROLLED_BACK"))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
