#!/usr/bin/env python3
"""Rollback-atomic fixed nine-target promotion for HCS-C57 PREFREEZE results."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import fcntl
import hashlib
import os
from pathlib import Path
import stat
import sys
import uuid
from typing import Sequence

from c57_exact import (
    StrictDataError,
    canonical_json_bytes,
    deep_exact,
    reject_optimized_python,
    require_exact_keys,
    strict_json_loads,
)


EXPECTED_TARGET_NAMES = (
    "a12_crt_transcript.json.gz",
    "a12_table.json.gz",
    "delta_crt.json.gz",
    "incidence_char0_witness.json.gz",
    "theta_crt.json.gz",
    "c57_schema.json",
    "c57_certificate.json",
    "c57_check_report.json",
    "scoped_hash_manifest.json",
)
LOCK_NAME = ".c57-promotion.lock"


class PromotionError(StrictDataError):
    """The requested transaction violates the fixed C57 promotion contract."""


class RollbackError(RuntimeError):
    """Rollback could not restore an exact preimage."""


class PostCommitError(RuntimeError):
    """The live nine-file commit is durable, but postcommit cleanup failed."""


class RolledBackVerifiedError(RuntimeError):
    """A precommit/commit-path error ended with exact live preimages restored."""


ROLLED_BACK_EXIT_CODE = 74
POSTCOMMIT_EXIT_CODE = 75


@dataclass(frozen=True)
class Fingerprint:
    sha256: str
    size_bytes: int
    mode: int
    mtime_ns: int
    device: int
    inode: int

    def restored_fields(self) -> tuple[str, int, int, int]:
        return self.sha256, self.size_bytes, self.mode, self.mtime_ns


@dataclass
class Entry:
    source: Path
    target: Path
    staged: Path
    backup: Path
    source_fingerprint: Fingerprint
    preimage: Fingerprint | None
    staged_fingerprint: Fingerprint | None = None
    backup_fingerprint: Fingerprint | None = None
    placed_fingerprint: Fingerprint | None = None
    staged_resident: bool = False
    backup_resident: bool = False


@dataclass
class LockHandle:
    path: Path
    descriptor: int
    token: bytes
    device: int
    inode: int


def _lexists(path: Path) -> bool:
    return os.path.lexists(os.fspath(path))


def _lstat_regular(path: Path, label: str, *, single_link: bool = True) -> os.stat_result:
    try:
        metadata = path.lstat()
    except FileNotFoundError as exc:
        raise PromotionError(f"missing {label}: {path}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise PromotionError(f"{label} must be a non-symlink regular file: {path}")
    if single_link and metadata.st_nlink != 1:
        raise PromotionError(f"hardlinked {label} is forbidden: {path}")
    return metadata


def fingerprint(path: Path, label: str = "file") -> Fingerprint:
    pathname_before = _lstat_regular(path, label)
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise PromotionError(f"opened {label} is not a single-link regular file")
        if (pathname_before.st_dev, pathname_before.st_ino) != (before.st_dev, before.st_ino):
            raise PromotionError(f"{label} pathname changed before open")
        digest = hashlib.sha256()
        size = 0
        while True:
            block = os.read(descriptor, 1 << 20)
            if not block:
                break
            digest.update(block)
            size += len(block)
        after = os.fstat(descriptor)
        pathname_after = path.lstat()
        stable = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mode,
            before.st_mtime_ns,
            before.st_ctime_ns,
            before.st_nlink,
        ) == (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mode,
            after.st_mtime_ns,
            after.st_ctime_ns,
            after.st_nlink,
        )
        pathname_same = (pathname_after.st_dev, pathname_after.st_ino) == (
            after.st_dev,
            after.st_ino,
        )
        if not stable or not pathname_same or pathname_after.st_nlink != 1:
            raise PromotionError(f"{label} changed while fingerprinting")
    finally:
        os.close(descriptor)
    if size != after.st_size:
        raise PromotionError(f"{label} size changed while reading")
    return Fingerprint(
        digest.hexdigest(),
        size,
        stat.S_IMODE(after.st_mode),
        after.st_mtime_ns,
        after.st_dev,
        after.st_ino,
    )


def _copy_stable(source: Path, destination: Path, expected: Fingerprint) -> Fingerprint:
    source_flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    destination_flags = (
        os.O_WRONLY
        | os.O_CREAT
        | os.O_EXCL
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
    )
    source_fd = os.open(source, source_flags)
    destination_fd = -1
    destination_identity: tuple[int, int] | None = None
    try:
        before = os.fstat(source_fd)
        pathname = source.lstat()
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_nlink != 1
            or (before.st_dev, before.st_ino) != (expected.device, expected.inode)
            or (pathname.st_dev, pathname.st_ino) != (before.st_dev, before.st_ino)
        ):
            raise PromotionError("source identity changed before transaction copy")
        destination_fd = os.open(destination, destination_flags, 0o600)
        opened_destination = os.fstat(destination_fd)
        destination_identity = (opened_destination.st_dev, opened_destination.st_ino)
        digest = hashlib.sha256()
        size = 0
        while True:
            block = os.read(source_fd, 1 << 20)
            if not block:
                break
            digest.update(block)
            size += len(block)
            view = memoryview(block)
            while view:
                written = os.write(destination_fd, view)
                if written <= 0:
                    raise OSError("short transaction copy write")
                view = view[written:]
        after = os.fstat(source_fd)
        pathname_after = source.lstat()
        if (
            (after.st_dev, after.st_ino, after.st_size, after.st_mode, after.st_mtime_ns)
            != (before.st_dev, before.st_ino, before.st_size, before.st_mode, before.st_mtime_ns)
            or (pathname_after.st_dev, pathname_after.st_ino) != (after.st_dev, after.st_ino)
            or digest.hexdigest() != expected.sha256
            or size != expected.size_bytes
        ):
            raise PromotionError("source changed during transaction copy")
        os.fchmod(destination_fd, expected.mode)
        os.utime(destination_fd, ns=(expected.mtime_ns, expected.mtime_ns))
        os.fsync(destination_fd)
        final_destination = os.fstat(destination_fd)
        pathname_destination = destination.lstat()
        if (
            (pathname_destination.st_dev, pathname_destination.st_ino)
            != (final_destination.st_dev, final_destination.st_ino)
            or final_destination.st_size != expected.size_bytes
            or stat.S_IMODE(final_destination.st_mode) != expected.mode
            or final_destination.st_mtime_ns != expected.mtime_ns
            or final_destination.st_nlink != 1
        ):
            raise PromotionError("transaction copy metadata/identity mismatch")
        copied = Fingerprint(
            expected.sha256,
            final_destination.st_size,
            stat.S_IMODE(final_destination.st_mode),
            final_destination.st_mtime_ns,
            final_destination.st_dev,
            final_destination.st_ino,
        )
    except BaseException:
        if destination_fd >= 0:
            os.close(destination_fd)
            destination_fd = -1
        os.close(source_fd)
        source_fd = -1
        if destination_identity is not None and _lexists(destination):
            pathname = destination.lstat()
            if (pathname.st_dev, pathname.st_ino) == destination_identity:
                destination.unlink()
        raise
    finally:
        if destination_fd >= 0:
            os.close(destination_fd)
        if source_fd >= 0:
            os.close(source_fd)
    return copied


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _fsync_bound_directory(path: Path, expected_identity: tuple[int, int]) -> None:
    """Fsync only the directory still named by the recorded device/inode."""
    before = path.lstat()
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISDIR(before.st_mode):
        raise PromotionError("bound transaction directory became non-directory")
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_DIRECTORY", 0)
    )
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        if (opened.st_dev, opened.st_ino) != expected_identity or (
            before.st_dev,
            before.st_ino,
        ) != expected_identity:
            raise PromotionError("bound transaction directory identity changed")
        os.fsync(descriptor)
        after = path.lstat()
        if (after.st_dev, after.st_ino) != expected_identity:
            raise PromotionError("bound transaction directory pathname changed")
    finally:
        os.close(descriptor)


def _stage_directory(
    result_dir: Path,
    stage: Path,
    *,
    expected_device: int,
    expected_inode: int,
) -> tuple[Path, Path, tuple[int, int]]:
    if result_dir.is_symlink() or not result_dir.is_dir():
        raise PromotionError("stage result directory is not real")
    result_dir = result_dir.resolve(strict=True)
    if stage.is_symlink() or not stage.is_dir():
        raise PromotionError("active stage is not a real directory")
    stage = stage.resolve(strict=True)
    if stage.parent != result_dir or not stage.name.startswith(".c57-stage-"):
        raise PromotionError("active stage is outside the fixed result directory")
    metadata = stage.lstat()
    identity = (metadata.st_dev, metadata.st_ino)
    if identity != (expected_device, expected_inode):
        raise PromotionError("active stage directory identity changed")
    return result_dir, stage, identity


def _fingerprint_object(value: Fingerprint) -> dict[str, int | str]:
    return {
        "sha256": value.sha256,
        "size_bytes": value.size_bytes,
        "mode": value.mode,
        "mtime_ns": value.mtime_ns,
        "device": value.device,
        "inode": value.inode,
    }


def stage_snapshot(
    result_dir: Path,
    stage: Path,
    *,
    expected_device: int,
    expected_inode: int,
) -> dict[str, object]:
    """Bind an allowed active-stage subset before any later cleanup."""
    _, stage, identity = _stage_directory(
        result_dir,
        stage,
        expected_device=expected_device,
        expected_inode=expected_inode,
    )
    children = list(stage.iterdir())
    names = {child.name for child in children}
    if len(names) != len(children) or not names.issubset(set(EXPECTED_TARGET_NAMES)):
        raise PromotionError("active stage contains a foreign or duplicate entry")
    ordered = sorted(children, key=lambda child: EXPECTED_TARGET_NAMES.index(child.name))
    entries = [
        {"name": child.name, "fingerprint": _fingerprint_object(fingerprint(child, "active stage entry"))}
        for child in ordered
    ]
    metadata = stage.lstat()
    if (metadata.st_dev, metadata.st_ino) != identity:
        raise PromotionError("active stage changed during snapshot")
    if {child.name for child in stage.iterdir()} != names:
        raise PromotionError("active stage inventory changed during snapshot")
    return {
        "schema_id": "hcs-c57-owned-stage-snapshot-v1",
        "stage_device": identity[0],
        "stage_inode": identity[1],
        "entries": entries,
    }


def _parse_stage_snapshot(raw_argument: str) -> dict[str, object]:
    raw = raw_argument.encode("utf-8")
    if len(raw) > 20_000:
        raise PromotionError("stage snapshot argument exceeds byte ceiling")
    value = strict_json_loads(raw, max_bytes=20_000)
    if raw + b"\n" != canonical_json_bytes(value):
        raise PromotionError("stage snapshot argument is not canonical compact JSON")
    require_exact_keys(
        value,
        {"schema_id", "stage_device", "stage_inode", "entries"},
        "stage snapshot",
    )
    if value["schema_id"] != "hcs-c57-owned-stage-snapshot-v1":
        raise PromotionError("wrong stage snapshot schema")
    if type(value["stage_device"]) is not int or type(value["stage_inode"]) is not int:
        raise PromotionError("stage snapshot identity must be exact integers")
    entries = value["entries"]
    if not isinstance(entries, list) or len(entries) > len(EXPECTED_TARGET_NAMES):
        raise PromotionError("stage snapshot entries must be a bounded list")
    expected_names = []
    for entry in entries:
        require_exact_keys(entry, {"name", "fingerprint"}, "stage snapshot entry")
        name = entry["name"]
        if type(name) is not str or name not in EXPECTED_TARGET_NAMES:
            raise PromotionError("stage snapshot contains a foreign name")
        expected_names.append(name)
        fp = entry["fingerprint"]
        require_exact_keys(
            fp,
            {"sha256", "size_bytes", "mode", "mtime_ns", "device", "inode"},
            "stage snapshot fingerprint",
        )
        if (
            type(fp["sha256"]) is not str
            or len(fp["sha256"]) != 64
            or any(character not in "0123456789abcdef" for character in fp["sha256"])
        ):
            raise PromotionError("bad stage snapshot SHA-256")
        if any(type(fp[key]) is not int for key in ("size_bytes", "mode", "mtime_ns", "device", "inode")):
            raise PromotionError("stage snapshot fingerprint values must be exact integers")
    canonical_names = [name for name in EXPECTED_TARGET_NAMES if name in set(expected_names)]
    if expected_names != canonical_names or len(expected_names) != len(set(expected_names)):
        raise PromotionError("stage snapshot entries are not the canonical distinct subsequence")
    return value


def verify_stage_extension(
    prior: dict[str, object], current: dict[str, object]
) -> None:
    """Require the final snapshot to add only the manifest to checker-owned bytes."""
    if (
        prior["schema_id"] != current["schema_id"]
        or prior["stage_device"] != current["stage_device"]
        or prior["stage_inode"] != current["stage_inode"]
    ):
        raise PromotionError("stage identity changed between checker and manifest")
    prior_entries = prior["entries"]
    current_entries = current["entries"]
    expected_prior_names = list(EXPECTED_TARGET_NAMES[:-1])
    if [entry["name"] for entry in prior_entries] != expected_prior_names:
        raise PromotionError("checker-owned snapshot must contain the first eight targets")
    if [entry["name"] for entry in current_entries] != list(EXPECTED_TARGET_NAMES):
        raise PromotionError("final snapshot must contain all nine targets")
    if not deep_exact(prior_entries, current_entries[:-1]):
        raise PromotionError("a checker-owned stage byte changed before final manifest")


def acquire_lock(result_dir: Path) -> LockHandle:
    path = result_dir / LOCK_NAME
    token = uuid.uuid4().hex.encode("ascii") + b"\n"
    flags = os.O_RDWR | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0)
    try:
        descriptor = os.open(path, flags, 0o600)
    except FileExistsError as exc:
        raise PromotionError("another or stale C57 promotion lock exists") from exc
    held_identity: tuple[int, int] | None = None
    try:
        opened = os.fstat(descriptor)
        held_identity = (opened.st_dev, opened.st_ino)
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if os.write(descriptor, token) != len(token):
            raise PromotionError("short promotion lock-token write")
        os.fsync(descriptor)
        metadata = os.fstat(descriptor)
        pathname = path.lstat()
        if (metadata.st_dev, metadata.st_ino) != (pathname.st_dev, pathname.st_ino):
            raise PromotionError("new lock pathname does not name the held descriptor")
        _fsync_directory(result_dir)
        return LockHandle(path, descriptor, token, metadata.st_dev, metadata.st_ino)
    except BaseException:
        os.close(descriptor)
        if _lexists(path) and held_identity is not None:
            pathname = path.lstat()
            if (pathname.st_dev, pathname.st_ino) == held_identity:
                path.unlink()
        raise


def release_lock(lock: LockHandle) -> None:
    error: BaseException | None = None
    try:
        descriptor_metadata = os.fstat(lock.descriptor)
        pathname_metadata = lock.path.lstat()
        if (
            (descriptor_metadata.st_dev, descriptor_metadata.st_ino)
            != (lock.device, lock.inode)
            or (pathname_metadata.st_dev, pathname_metadata.st_ino)
            != (lock.device, lock.inode)
        ):
            raise PromotionError("promotion lock pathname was replaced; foreign lock retained")
        os.lseek(lock.descriptor, 0, os.SEEK_SET)
        if os.read(lock.descriptor, len(lock.token) + 1) != lock.token:
            raise PromotionError("promotion lock token changed; lock retained")
        lock.path.unlink()
        _fsync_directory(lock.path.parent)
    except BaseException as exc:
        error = exc
    finally:
        os.close(lock.descriptor)
    if error is not None:
        raise error


def _validate_request(
    pairs: Sequence[tuple[Path, str]],
    result_dir: Path,
    fail_after: int | None,
    expected_stage_snapshot: dict[str, object],
) -> tuple[Path, list[tuple[Path, Path, Fingerprint, Fingerprint | None]]]:
    reject_optimized_python()
    if len(pairs) != 9 or tuple(target for _, target in pairs) != EXPECTED_TARGET_NAMES:
        raise PromotionError("the nine targets and their order are fixed")
    if fail_after is not None and fail_after not in range(1, 10):
        raise PromotionError("--fail-after must be in 1..9")
    if result_dir.is_symlink() or not result_dir.is_dir():
        raise PromotionError("result directory must be an existing non-symlink directory")
    result_dir = result_dir.resolve(strict=True)
    result_metadata = result_dir.stat()
    require_exact_keys(
        expected_stage_snapshot,
        {"schema_id", "stage_device", "stage_inode", "entries"},
        "promotion stage snapshot",
    )
    snapshot_entries = expected_stage_snapshot["entries"]
    if [entry["name"] for entry in snapshot_entries] != list(EXPECTED_TARGET_NAMES):
        raise PromotionError("promotion requires an exact nine-entry final stage snapshot")
    snapshot_by_name = {entry["name"]: entry["fingerprint"] for entry in snapshot_entries}

    stage_parents = set()
    source_inodes = set()
    target_inodes = set()
    validated = []
    for source_argument, target_name in pairs:
        source = source_argument.absolute()
        if source.parent.is_symlink():
            raise PromotionError("stage parent symlink is forbidden")
        stage_parent = source.parent.resolve(strict=True)
        stage_parents.add(stage_parent)
        if stage_parent.parent != result_dir or not stage_parent.name.startswith(".c57-stage-"):
            raise PromotionError("sources must be in one named active stage under results")
        source_fingerprint = fingerprint(source, "promotion source")
        if not deep_exact(_fingerprint_object(source_fingerprint), snapshot_by_name[target_name]):
            raise PromotionError("promotion source differs from the final owned stage snapshot")
        if source_fingerprint.device != result_metadata.st_dev:
            raise PromotionError("cross-filesystem promotion is forbidden")
        source_inode = (source_fingerprint.device, source_fingerprint.inode)
        if source_inode in source_inodes:
            raise PromotionError("promotion sources must not hardlink each other")
        source_inodes.add(source_inode)
        target = result_dir / target_name
        preimage = None
        if _lexists(target):
            preimage = fingerprint(target, "promotion target")
            target_inode = (preimage.device, preimage.inode)
            if target_inode in target_inodes or target_inode in source_inodes:
                raise PromotionError("target hardlink alias is forbidden")
            target_inodes.add(target_inode)
        validated.append((source, target, source_fingerprint, preimage))
    if len(stage_parents) != 1:
        raise PromotionError("all nine sources must share one active stage")
    stage = next(iter(stage_parents))
    stage_metadata = stage.lstat()
    if (stage_metadata.st_dev, stage_metadata.st_ino) != (
        expected_stage_snapshot["stage_device"],
        expected_stage_snapshot["stage_inode"],
    ):
        raise PromotionError("promotion stage differs from the final owned snapshot")
    if source_inodes & target_inodes:
        raise PromotionError("a promotion source aliases an existing target")
    observed = set()
    for child in stage.iterdir():
        _lstat_regular(child, "active stage entry")
        observed.add(child.name)
    if observed != set(EXPECTED_TARGET_NAMES):
        raise PromotionError("active stage must contain exactly the nine promotion sources")
    allowed_live = set(EXPECTED_TARGET_NAMES) | {"RESULTS.md", "TEST_REPORT.md"}
    for child in result_dir.iterdir():
        if child.resolve(strict=False) == stage:
            if child.is_symlink() or not child.is_dir():
                raise PromotionError("active stage pathname changed")
            continue
        metadata = child.lstat()
        if child.name not in allowed_live:
            raise PromotionError(f"foreign result debris blocks promotion: {child.name}")
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise PromotionError(f"nonregular live result blocks promotion: {child.name}")
    return result_dir, validated


def _verify_preimages(entries: Sequence[Entry]) -> None:
    failures = []
    for entry in entries:
        if entry.preimage is None:
            if _lexists(entry.target):
                failures.append(f"expected absent target: {entry.target.name}")
        else:
            try:
                restored = fingerprint(entry.target, "restored target")
            except BaseException as exc:
                failures.append(f"unreadable {entry.target.name}: {exc}")
            else:
                if restored.restored_fields() != entry.preimage.restored_fields():
                    failures.append(f"metadata/content mismatch: {entry.target.name}")
    if failures:
        raise RollbackError("; ".join(failures))


def _verify_precommit_preimages(entries: Sequence[Entry]) -> None:
    for entry in entries:
        if entry.staged_fingerprint is None or fingerprint(
            entry.staged, "precommit staged copy"
        ) != entry.staged_fingerprint:
            raise PromotionError("a staged transaction copy changed before commit")
        if entry.preimage is not None and (
            entry.backup_fingerprint is None
            or fingerprint(entry.backup, "precommit backup") != entry.backup_fingerprint
        ):
            raise PromotionError("a transaction backup changed before commit")
        if entry.preimage is None:
            if _lexists(entry.target):
                raise PromotionError("an absent preimage appeared before commit")
        elif fingerprint(entry.target, "precommit target") != entry.preimage:
            raise PromotionError("a target changed before commit")


def _cleanup_transaction(
    entries: Sequence[Entry],
    transaction: Path,
    transaction_identity: tuple[int, int],
    result_dir: Path,
) -> None:
    # Phase one is read-only: reject missing, substituted, or extra entries before
    # deleting any evidence owned by this transaction.
    if not _lexists(transaction):
        raise PromotionError("transaction directory disappeared; no cleanup attempted")
    metadata = transaction.lstat()
    if (
        stat.S_ISLNK(metadata.st_mode)
        or not stat.S_ISDIR(metadata.st_mode)
        or (metadata.st_dev, metadata.st_ino) != transaction_identity
    ):
        raise PromotionError("transaction directory pathname was replaced")
    expected_resident: dict[Path, Fingerprint] = {}
    expected_absent: set[Path] = set()
    for entry in entries:
        for path, expected, resident in (
            (entry.staged, entry.staged_fingerprint, entry.staged_resident),
            (entry.backup, entry.backup_fingerprint, entry.backup_resident),
        ):
            if resident:
                if expected is None:
                    raise PromotionError("resident transaction entry lacks a fingerprint")
                expected_resident[path] = expected
            else:
                expected_absent.add(path)
    observed_paths = set(transaction.iterdir())
    if observed_paths != set(expected_resident):
        raise PromotionError("transaction inventory differs from recorded resident state")
    for path in expected_absent:
        if _lexists(path):
            raise PromotionError("nonresident transaction path reappeared")
    for path, expected in expected_resident.items():
        if fingerprint(path, "owned transaction entry") != expected:
            raise PromotionError("foreign/replaced transaction entry retained")
    _fsync_bound_directory(transaction, transaction_identity)

    # Phase two deletes only entries whose identity was already bound above and
    # rechecks each identity immediately before unlink.
    for path, expected in expected_resident.items():
        _fsync_bound_directory(transaction, transaction_identity)
        if fingerprint(path, "owned transaction entry") != expected:
            raise PromotionError("transaction entry changed during cleanup; retaining remainder")
        path.unlink()
        _fsync_bound_directory(transaction, transaction_identity)
    metadata = transaction.lstat()
    if (
        (metadata.st_dev, metadata.st_ino) != transaction_identity
        or any(transaction.iterdir())
    ):
        raise PromotionError("transaction final identity/inventory changed")
    transaction.rmdir()
    _fsync_directory(result_dir)


def promote(
    pairs: Sequence[tuple[Path, str]],
    result_dir: Path,
    *,
    expected_stage_snapshot: dict[str, object],
    fail_after: int | None = None,
) -> None:
    result_dir, validated = _validate_request(
        pairs, result_dir, fail_after, expected_stage_snapshot
    )
    lock = acquire_lock(result_dir)
    transaction = result_dir / f".c57-transaction-{uuid.uuid4().hex}"
    transaction_identity: tuple[int, int] | None = None
    entries: list[Entry] = []
    replaced = 0
    primary_error: BaseException | None = None
    rollback_failed = False
    committed = False
    try:
        transaction.mkdir(mode=0o700)
        transaction_metadata = transaction.lstat()
        transaction_identity = (transaction_metadata.st_dev, transaction_metadata.st_ino)
        for index, (source, target, source_fingerprint, preimage) in enumerate(validated):
            entry = Entry(
                source,
                target,
                transaction / f"new-{index:02d}",
                transaction / f"old-{index:02d}",
                source_fingerprint,
                preimage,
            )
            entries.append(entry)
            entry.staged_fingerprint = _copy_stable(
                source, entry.staged, source_fingerprint
            )
            entry.staged_resident = True
            if preimage is not None:
                entry.backup_fingerprint = _copy_stable(
                    target, entry.backup, preimage
                )
                entry.backup_resident = True
        _fsync_bound_directory(transaction, transaction_identity)

        # Rebind every original source pathname after all transaction copies,
        # before the first live target is touched.
        for entry in entries:
            if fingerprint(entry.source, "promotion source") != entry.source_fingerprint:
                raise PromotionError("promotion source changed before commit")
        _verify_precommit_preimages(entries)

        for entry in entries:
            if entry.staged_fingerprint is None:
                raise PromotionError("missing staged copy fingerprint")
            if fingerprint(entry.source, "per-replacement source") != entry.source_fingerprint:
                raise PromotionError("promotion source changed before replacement")
            if fingerprint(entry.staged, "per-replacement staged copy") != entry.staged_fingerprint:
                raise PromotionError("staged copy changed before replacement")
            if entry.preimage is not None and (
                entry.backup_fingerprint is None
                or fingerprint(entry.backup, "per-replacement backup")
                != entry.backup_fingerprint
            ):
                raise PromotionError("backup changed before replacement")
            os.replace(entry.staged, entry.target)
            replaced += 1
            entry.staged_resident = False
            _fsync_bound_directory(transaction, transaction_identity)
            _fsync_directory(result_dir)
            entry.placed_fingerprint = fingerprint(entry.target, "placed target")
            if entry.placed_fingerprint != entry.staged_fingerprint:
                raise PromotionError("placed target differs from staged copy identity")
            if fingerprint(entry.source, "post-replacement source") != entry.source_fingerprint:
                raise PromotionError("promotion source changed during replacement")
            if entry.preimage is not None and fingerprint(
                entry.backup, "post-replacement backup"
            ) != entry.backup_fingerprint:
                raise PromotionError("backup changed during replacement")
            if fail_after == replaced:
                raise RuntimeError(f"test-injected failure after replacement {replaced}")
        for entry in entries:
            if entry.placed_fingerprint is None or fingerprint(
                entry.target, "final placed target"
            ) != entry.placed_fingerprint:
                raise PromotionError("a placed target changed before transaction completion")
            if fingerprint(entry.source, "final promotion source") != entry.source_fingerprint:
                raise PromotionError("a promotion source changed before transaction completion")
        _fsync_bound_directory(transaction, transaction_identity)
        _fsync_directory(result_dir)
        committed = True
    except BaseException as exc:
        primary_error = exc
        try:
            for entry in reversed(entries[:replaced]):
                expected_placed = entry.placed_fingerprint or entry.staged_fingerprint
                if expected_placed is None:
                    raise RollbackError("missing placed/staged fingerprint")
                current = fingerprint(entry.target, "rollback target")
                if current != expected_placed:
                    raise RollbackError("foreign target replacement detected during rollback")
                if entry.preimage is None:
                    entry.target.unlink()
                    _fsync_directory(result_dir)
                else:
                    if entry.backup_fingerprint is None or fingerprint(
                        entry.backup, "rollback backup"
                    ) != entry.backup_fingerprint:
                        raise RollbackError("backup changed before rollback")
                    os.replace(entry.backup, entry.target)
                    entry.backup_resident = False
                    if transaction_identity is None:
                        raise RollbackError("missing transaction identity during rollback")
                    _fsync_bound_directory(transaction, transaction_identity)
                    _fsync_directory(result_dir)
            _verify_preimages(entries)
        except BaseException as rollback_exc:
            rollback_failed = True
            raise RollbackError(f"rollback after {primary_error!r} failed: {rollback_exc}") from rollback_exc
        raise RolledBackVerifiedError(
            f"ROLLED_BACK_VERIFIED: exact live preimages restored after {exc!r}"
        ) from exc
    finally:
        cleanup_error: BaseException | None = None
        if not rollback_failed:
            try:
                if transaction_identity is not None:
                    _cleanup_transaction(entries, transaction, transaction_identity, result_dir)
            except BaseException as exc:
                cleanup_error = exc
        try:
            release_lock(lock)
        except BaseException as exc:
            if cleanup_error is None:
                cleanup_error = exc
        if cleanup_error is not None and primary_error is None:
            if committed:
                raise PostCommitError(
                    "COMMITTED_WITH_DEBRIS: live nine-target commit is durable; "
                    "postcommit cleanup/lock release failed; DO NOT RETRY"
                ) from cleanup_error
            raise cleanup_error
        if cleanup_error is not None and primary_error is not None and not rollback_failed:
            raise RolledBackVerifiedError(
                "ROLLED_BACK_VERIFIED_WITH_DEBRIS: exact live preimages restored; "
                "transaction/lock cleanup incomplete"
            ) from cleanup_error


def cleanup_active_stage(
    result_dir: Path,
    stage: Path,
    *,
    expected_snapshot: dict[str, object],
) -> None:
    """Remove only the exact stage/inodes bound by an earlier owned snapshot."""
    require_exact_keys(
        expected_snapshot,
        {"schema_id", "stage_device", "stage_inode", "entries"},
        "stage cleanup snapshot",
    )
    result_dir, stage, identity = _stage_directory(
        result_dir,
        stage,
        expected_device=expected_snapshot["stage_device"],
        expected_inode=expected_snapshot["stage_inode"],
    )
    children = list(stage.iterdir())
    expected_entries = expected_snapshot["entries"]
    expected_names = [entry["name"] for entry in expected_entries]
    if {child.name for child in children} != set(expected_names):
        raise PromotionError("cleanup stage inventory changed; retaining it")
    expected_by_name = {entry["name"]: entry["fingerprint"] for entry in expected_entries}
    for child in sorted(children, key=lambda value: EXPECTED_TARGET_NAMES.index(value.name)):
        actual = _fingerprint_object(fingerprint(child, "cleanup stage file"))
        if not deep_exact(actual, expected_by_name[child.name]):
            raise PromotionError("cleanup stage file identity changed; retaining it")
    for child in sorted(children, key=lambda value: EXPECTED_TARGET_NAMES.index(value.name)):
        current_directory = stage.lstat()
        if (current_directory.st_dev, current_directory.st_ino) != identity:
            raise PromotionError("cleanup stage directory was replaced; retaining it")
        actual = _fingerprint_object(fingerprint(child, "cleanup stage file"))
        if not deep_exact(actual, expected_by_name[child.name]):
            raise PromotionError("cleanup stage file was replaced; retaining it")
        child.unlink()
        _fsync_directory(stage)
    metadata = stage.lstat()
    if (metadata.st_dev, metadata.st_ino) != identity or any(stage.iterdir()):
        raise PromotionError("cleanup stage final identity/inventory changed; retaining it")
    stage.rmdir()
    _fsync_directory(result_dir)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", type=Path, required=True)
    parser.add_argument("--source", type=Path, action="append")
    parser.add_argument("--target", action="append")
    parser.add_argument("--fail-after", type=int)
    parser.add_argument("--cleanup-stage", type=Path)
    parser.add_argument("--snapshot-stage", type=Path)
    parser.add_argument("--expected-stage-device", type=int)
    parser.add_argument("--expected-stage-inode", type=int)
    parser.add_argument("--expected-stage-snapshot")
    parser.add_argument("--verify-stage-extension", action="store_true")
    parser.add_argument("--prior-stage-snapshot")
    arguments = parser.parse_args()
    reject_optimized_python()
    if arguments.verify_stage_extension:
        if (
            arguments.source
            or arguments.target
            or arguments.fail_after is not None
            or arguments.cleanup_stage is not None
            or arguments.snapshot_stage is not None
            or arguments.expected_stage_device is not None
            or arguments.expected_stage_inode is not None
            or arguments.expected_stage_snapshot is None
            or arguments.prior_stage_snapshot is None
        ):
            parser.error("verify-stage-extension accepts exactly two snapshots")
        verify_stage_extension(
            _parse_stage_snapshot(arguments.prior_stage_snapshot),
            _parse_stage_snapshot(arguments.expected_stage_snapshot),
        )
        print("C57 checker-to-manifest stage extension PASS")
        return 0
    if arguments.snapshot_stage is not None:
        if (
            arguments.source
            or arguments.target
            or arguments.fail_after is not None
            or arguments.cleanup_stage is not None
            or arguments.expected_stage_snapshot is not None
            or arguments.verify_stage_extension
            or arguments.prior_stage_snapshot is not None
            or arguments.expected_stage_device is None
            or arguments.expected_stage_inode is None
        ):
            parser.error("snapshot-stage accepts only its expected directory identity")
        sys.stdout.buffer.write(
            canonical_json_bytes(
                stage_snapshot(
                    arguments.result_dir,
                    arguments.snapshot_stage,
                    expected_device=arguments.expected_stage_device,
                    expected_inode=arguments.expected_stage_inode,
                )
            )
        )
        return 0
    if arguments.cleanup_stage is not None:
        if (
            arguments.source
            or arguments.target
            or arguments.fail_after is not None
            or arguments.snapshot_stage is not None
            or arguments.expected_stage_device is not None
            or arguments.expected_stage_inode is not None
            or arguments.expected_stage_snapshot is None
            or arguments.verify_stage_extension
            or arguments.prior_stage_snapshot is not None
        ):
            parser.error("cleanup-stage accepts only one exact prior stage snapshot")
        cleanup_active_stage(
            arguments.result_dir,
            arguments.cleanup_stage,
            expected_snapshot=_parse_stage_snapshot(arguments.expected_stage_snapshot),
        )
        print("C57 active stage identity-bound cleanup PASS")
        return 0
    if not arguments.source or not arguments.target:
        parser.error("promotion requires nine --source/--target pairs")
    if len(arguments.source) != len(arguments.target):
        parser.error("every --source requires one --target")
    if arguments.expected_stage_snapshot is None or arguments.prior_stage_snapshot is not None:
        parser.error("promotion requires exactly one final owned stage snapshot")
    try:
        promote(
            list(zip(arguments.source, arguments.target)),
            arguments.result_dir,
            expected_stage_snapshot=_parse_stage_snapshot(arguments.expected_stage_snapshot),
            fail_after=arguments.fail_after,
        )
    except PostCommitError as exc:
        print(str(exc), file=sys.stderr)
        return POSTCOMMIT_EXIT_CODE
    except RolledBackVerifiedError as exc:
        print(str(exc), file=sys.stderr)
        return ROLLED_BACK_EXIT_CODE
    except PromotionError as exc:
        print(f"PRECOMMIT_REJECTED: {exc}", file=sys.stderr)
        return ROLLED_BACK_EXIT_CODE
    print("C57 rollback-atomic nine-target promotion PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
