#!/usr/bin/env python3
"""Rollback-atomic fixed six-target promotion for HCS-C60 PREFREEZE results."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import fcntl
import hashlib
import os
from pathlib import Path
import re
import stat
import sys
import uuid
from typing import Sequence

from c60_exact import (
    StrictDataError,
    canonical_json_bytes,
    deep_exact,
    reject_optimized_python,
    require_exact_keys,
    strict_json_loads,
)


EXPECTED_TARGET_NAMES = (
    "c60_group_evidence.json",
    "c60_resolvent_evidence.json",
    "c60_schema.json",
    "c60_certificate.json",
    "c60_check_report.json",
    "scoped_hash_manifest.json",
)
LOCK_NAME = ".c60-promotion.lock"
STAGE_NAME_PATTERN = re.compile(r"^\.c60-stage-[A-Za-z0-9]{8}$")


class PromotionError(StrictDataError):
    """The requested transaction violates the fixed C60 promotion contract."""


class DirectoryIdentityError(RuntimeError):
    """A directory pathname stopped naming its persistently bound directory FD."""


class RollbackError(RuntimeError):
    """Rollback could not restore an exact preimage."""


class PostCommitError(RuntimeError):
    """The live six-file commit is durable, but postcommit cleanup failed."""


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


@dataclass
class DirectoryBinding:
    path: Path
    descriptor: int
    device: int
    inode: int


def _directory_flags() -> int:
    return (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_DIRECTORY", 0)
    )


def _bind_directory(path: Path, label: str) -> DirectoryBinding:
    """Open and retain a directory capability after a three-way identity check."""
    absolute = path.absolute()
    try:
        pathname_before = absolute.lstat()
    except FileNotFoundError as exc:
        raise PromotionError(f"missing {label}: {absolute}") from exc
    if stat.S_ISLNK(pathname_before.st_mode) or not stat.S_ISDIR(pathname_before.st_mode):
        raise PromotionError(f"{label} must be a non-symlink directory")
    canonical = absolute.resolve(strict=True)
    if canonical != absolute:
        raise PromotionError(f"{label} must be supplied by its canonical absolute path")
    descriptor = os.open(canonical, _directory_flags())
    try:
        opened = os.fstat(descriptor)
        pathname_after = canonical.lstat()
        identity = (opened.st_dev, opened.st_ino)
        if (
            not stat.S_ISDIR(opened.st_mode)
            or (pathname_before.st_dev, pathname_before.st_ino) != identity
            or (pathname_after.st_dev, pathname_after.st_ino) != identity
            or stat.S_ISLNK(pathname_after.st_mode)
        ):
            raise PromotionError(f"{label} identity changed while binding")
        return DirectoryBinding(canonical, descriptor, opened.st_dev, opened.st_ino)
    except BaseException:
        os.close(descriptor)
        raise


def _bind_child_directory(
    parent: DirectoryBinding,
    name: str,
    path: Path,
    label: str,
    *,
    expected_identity: tuple[int, int] | None = None,
) -> DirectoryBinding:
    _verify_directory_binding(parent, f"{label} parent")
    descriptor = os.open(name, _directory_flags(), dir_fd=parent.descriptor)
    try:
        opened = os.fstat(descriptor)
        relative = os.stat(name, dir_fd=parent.descriptor, follow_symlinks=False)
        pathname = path.lstat()
        identity = (opened.st_dev, opened.st_ino)
        if (
            not stat.S_ISDIR(opened.st_mode)
            or stat.S_ISLNK(relative.st_mode)
            or not stat.S_ISDIR(relative.st_mode)
            or (relative.st_dev, relative.st_ino) != identity
            or (pathname.st_dev, pathname.st_ino) != identity
            or (expected_identity is not None and identity != expected_identity)
        ):
            raise DirectoryIdentityError(f"{label} identity changed while binding")
        _verify_directory_binding(parent, f"{label} parent")
        return DirectoryBinding(path, descriptor, opened.st_dev, opened.st_ino)
    except BaseException:
        os.close(descriptor)
        raise


def _verify_directory_binding(binding: DirectoryBinding, label: str) -> None:
    """Rebind both the persistent capability and its required pathname."""
    if binding.descriptor < 0:
        raise DirectoryIdentityError(f"{label} directory capability is closed")
    opened = os.fstat(binding.descriptor)
    expected = (binding.device, binding.inode)
    if not stat.S_ISDIR(opened.st_mode) or (opened.st_dev, opened.st_ino) != expected:
        raise DirectoryIdentityError(f"{label} directory descriptor identity changed")
    try:
        pathname = binding.path.lstat()
    except FileNotFoundError as exc:
        raise DirectoryIdentityError(f"{label} directory pathname disappeared") from exc
    if (
        stat.S_ISLNK(pathname.st_mode)
        or not stat.S_ISDIR(pathname.st_mode)
        or (pathname.st_dev, pathname.st_ino) != expected
    ):
        raise DirectoryIdentityError(f"{label} directory pathname identity changed")
    rebound = os.open(binding.path, _directory_flags())
    try:
        metadata = os.fstat(rebound)
        if (metadata.st_dev, metadata.st_ino) != expected:
            raise DirectoryIdentityError(f"{label} directory rebound identity changed")
    finally:
        os.close(rebound)


def _close_directory_binding(binding: DirectoryBinding) -> None:
    if binding.descriptor >= 0:
        os.close(binding.descriptor)
        binding.descriptor = -1


def _fsync_directory_binding(binding: DirectoryBinding, label: str) -> None:
    _verify_directory_binding(binding, label)
    os.fsync(binding.descriptor)
    _verify_directory_binding(binding, label)


def _lexists_at(binding: DirectoryBinding, name: str) -> bool:
    try:
        os.stat(name, dir_fd=binding.descriptor, follow_symlinks=False)
    except FileNotFoundError:
        return False
    return True


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


def _fingerprint_at(
    binding: DirectoryBinding,
    name: str,
    label: str = "file",
) -> Fingerprint:
    """Fingerprint a leaf relative to a persistently bound directory."""
    _verify_directory_binding(binding, f"{label} parent")
    try:
        pathname_before = os.stat(name, dir_fd=binding.descriptor, follow_symlinks=False)
    except FileNotFoundError as exc:
        raise PromotionError(f"missing {label}: {name}") from exc
    if (
        stat.S_ISLNK(pathname_before.st_mode)
        or not stat.S_ISREG(pathname_before.st_mode)
        or pathname_before.st_nlink != 1
    ):
        raise PromotionError(f"{label} must be a single-link non-symlink regular file")
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(name, flags, dir_fd=binding.descriptor)
    try:
        before = os.fstat(descriptor)
        if (before.st_dev, before.st_ino) != (
            pathname_before.st_dev,
            pathname_before.st_ino,
        ):
            raise PromotionError(f"{label} relative pathname changed before open")
        digest = hashlib.sha256()
        size = 0
        while True:
            block = os.read(descriptor, 1 << 20)
            if not block:
                break
            digest.update(block)
            size += len(block)
        after = os.fstat(descriptor)
        pathname_after = os.stat(name, dir_fd=binding.descriptor, follow_symlinks=False)
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
        if (
            not stable
            or (pathname_after.st_dev, pathname_after.st_ino)
            != (after.st_dev, after.st_ino)
            or pathname_after.st_nlink != 1
            or size != after.st_size
        ):
            raise PromotionError(f"{label} changed while fingerprinting")
    finally:
        os.close(descriptor)
    _verify_directory_binding(binding, f"{label} parent")
    return Fingerprint(
        digest.hexdigest(),
        size,
        stat.S_IMODE(after.st_mode),
        after.st_mtime_ns,
        after.st_dev,
        after.st_ino,
    )


def _copy_stable_bound(
    source: Path,
    expected: Fingerprint,
    destination_binding: DirectoryBinding,
    destination_name: str,
    *,
    source_binding: DirectoryBinding | None = None,
) -> Fingerprint:
    """Copy to a bound directory without authorizing any mutable parent pathname."""
    _verify_directory_binding(destination_binding, "transaction destination")
    if source_binding is not None:
        _verify_directory_binding(source_binding, "transaction source")
    source_flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    destination_flags = (
        os.O_WRONLY
        | os.O_CREAT
        | os.O_EXCL
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
    )
    if source_binding is None:
        source_fd = os.open(source, source_flags)
        source_before_path = source.lstat()
    else:
        source_fd = os.open(source.name, source_flags, dir_fd=source_binding.descriptor)
        source_before_path = os.stat(
            source.name, dir_fd=source_binding.descriptor, follow_symlinks=False
        )
    destination_fd = -1
    destination_identity: tuple[int, int] | None = None
    try:
        before = os.fstat(source_fd)
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_nlink != 1
            or (before.st_dev, before.st_ino) != (expected.device, expected.inode)
            or (source_before_path.st_dev, source_before_path.st_ino)
            != (before.st_dev, before.st_ino)
        ):
            raise PromotionError("source identity changed before bound transaction copy")
        destination_fd = os.open(
            destination_name,
            destination_flags,
            0o600,
            dir_fd=destination_binding.descriptor,
        )
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
                    raise OSError("short bound transaction copy write")
                view = view[written:]
        after = os.fstat(source_fd)
        if source_binding is None:
            source_after_path = source.lstat()
        else:
            source_after_path = os.stat(
                source.name, dir_fd=source_binding.descriptor, follow_symlinks=False
            )
        if (
            (after.st_dev, after.st_ino, after.st_size, after.st_mode, after.st_mtime_ns)
            != (before.st_dev, before.st_ino, before.st_size, before.st_mode, before.st_mtime_ns)
            or (source_after_path.st_dev, source_after_path.st_ino)
            != (after.st_dev, after.st_ino)
            or digest.hexdigest() != expected.sha256
            or size != expected.size_bytes
        ):
            raise PromotionError("source changed during bound transaction copy")
        os.fchmod(destination_fd, expected.mode)
        os.utime(destination_fd, ns=(expected.mtime_ns, expected.mtime_ns))
        os.fsync(destination_fd)
        final_destination = os.fstat(destination_fd)
        pathname_destination = os.stat(
            destination_name,
            dir_fd=destination_binding.descriptor,
            follow_symlinks=False,
        )
        if (
            (pathname_destination.st_dev, pathname_destination.st_ino)
            != (final_destination.st_dev, final_destination.st_ino)
            or final_destination.st_size != expected.size_bytes
            or stat.S_IMODE(final_destination.st_mode) != expected.mode
            or final_destination.st_mtime_ns != expected.mtime_ns
            or final_destination.st_nlink != 1
        ):
            raise PromotionError("bound transaction copy metadata/identity mismatch")
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
        if destination_identity is not None:
            try:
                pathname = os.stat(
                    destination_name,
                    dir_fd=destination_binding.descriptor,
                    follow_symlinks=False,
                )
            except FileNotFoundError:
                pass
            else:
                if (pathname.st_dev, pathname.st_ino) == destination_identity:
                    os.unlink(destination_name, dir_fd=destination_binding.descriptor)
        raise
    finally:
        if destination_fd >= 0:
            os.close(destination_fd)
        os.close(source_fd)
    _verify_directory_binding(destination_binding, "transaction destination")
    if source_binding is not None:
        _verify_directory_binding(source_binding, "transaction source")
    return copied


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


def _bind_stage_directories(
    result_dir: Path,
    stage: Path,
    *,
    expected_device: int,
    expected_inode: int,
) -> tuple[DirectoryBinding, DirectoryBinding]:
    result_binding = _bind_directory(result_dir, "stage result directory")
    try:
        stage_absolute = stage.absolute()
        if (
            stage_absolute.parent != result_binding.path
            or STAGE_NAME_PATTERN.fullmatch(stage_absolute.name) is None
        ):
            raise PromotionError("active stage is outside the fixed result directory")
        stage_binding = _bind_child_directory(
            result_binding,
            stage_absolute.name,
            stage_absolute,
            "active stage",
            expected_identity=(expected_device, expected_inode),
        )
        return result_binding, stage_binding
    except BaseException:
        _close_directory_binding(result_binding)
        raise


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
    result_binding, stage_binding = _bind_stage_directories(
        result_dir,
        stage,
        expected_device=expected_device,
        expected_inode=expected_inode,
    )
    try:
        names_list = os.listdir(stage_binding.descriptor)
        names = set(names_list)
        if len(names) != len(names_list) or not names.issubset(set(EXPECTED_TARGET_NAMES)):
            raise PromotionError("active stage contains a foreign or duplicate entry")
        ordered = sorted(names, key=EXPECTED_TARGET_NAMES.index)
        entries = [
            {
                "name": name,
                "fingerprint": _fingerprint_object(
                    _fingerprint_at(stage_binding, name, "active stage entry")
                ),
            }
            for name in ordered
        ]
        _verify_directory_binding(result_binding, "stage result directory")
        _verify_directory_binding(stage_binding, "active stage")
        if set(os.listdir(stage_binding.descriptor)) != names:
            raise PromotionError("active stage inventory changed during snapshot")
        return {
            "schema_id": "hcs-c60-owned-stage-snapshot-v1",
            "stage_device": stage_binding.device,
            "stage_inode": stage_binding.inode,
            "entries": entries,
        }
    finally:
        _close_directory_binding(stage_binding)
        _close_directory_binding(result_binding)


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
    if value["schema_id"] != "hcs-c60-owned-stage-snapshot-v1":
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
        raise PromotionError("checker-owned snapshot must contain the first five targets")
    if [entry["name"] for entry in current_entries] != list(EXPECTED_TARGET_NAMES):
        raise PromotionError("final snapshot must contain all six targets")
    if not deep_exact(prior_entries, current_entries[:-1]):
        raise PromotionError("a checker-owned stage byte changed before final manifest")


def acquire_lock(result_binding: DirectoryBinding) -> LockHandle:
    _verify_directory_binding(result_binding, "result directory at lock acquisition")
    path = result_binding.path / LOCK_NAME
    token = uuid.uuid4().hex.encode("ascii") + b"\n"
    flags = os.O_RDWR | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0)
    try:
        descriptor = os.open(LOCK_NAME, flags, 0o600, dir_fd=result_binding.descriptor)
    except FileExistsError as exc:
        raise PromotionError("another or stale C60 promotion lock exists") from exc
    held_identity: tuple[int, int] | None = None
    try:
        opened = os.fstat(descriptor)
        held_identity = (opened.st_dev, opened.st_ino)
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if os.write(descriptor, token) != len(token):
            raise PromotionError("short promotion lock-token write")
        os.fsync(descriptor)
        metadata = os.fstat(descriptor)
        pathname = os.stat(
            LOCK_NAME, dir_fd=result_binding.descriptor, follow_symlinks=False
        )
        if (metadata.st_dev, metadata.st_ino) != (pathname.st_dev, pathname.st_ino):
            raise PromotionError("new lock pathname does not name the held descriptor")
        _fsync_directory_binding(result_binding, "result directory after lock acquisition")
        return LockHandle(path, descriptor, token, metadata.st_dev, metadata.st_ino)
    except BaseException:
        os.close(descriptor)
        if held_identity is not None:
            try:
                pathname = os.stat(
                    LOCK_NAME, dir_fd=result_binding.descriptor, follow_symlinks=False
                )
            except FileNotFoundError:
                pass
            else:
                if (pathname.st_dev, pathname.st_ino) == held_identity:
                    os.unlink(LOCK_NAME, dir_fd=result_binding.descriptor)
        raise


def release_lock(lock: LockHandle, result_binding: DirectoryBinding) -> None:
    error: BaseException | None = None
    try:
        _verify_directory_binding(result_binding, "result directory at lock release")
        descriptor_metadata = os.fstat(lock.descriptor)
        pathname_metadata = os.stat(
            LOCK_NAME, dir_fd=result_binding.descriptor, follow_symlinks=False
        )
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
        _verify_directory_binding(result_binding, "result directory before lock unlink")
        os.unlink(LOCK_NAME, dir_fd=result_binding.descriptor)
        _fsync_directory_binding(result_binding, "result directory after lock unlink")
    except BaseException as exc:
        error = exc
    finally:
        os.close(lock.descriptor)
    if error is not None:
        raise error


def _validate_request(
    pairs: Sequence[tuple[Path, str]],
    result_binding: DirectoryBinding,
    fail_after: int | None,
    expected_stage_snapshot: dict[str, object],
) -> tuple[DirectoryBinding, list[tuple[Path, Path, Fingerprint, Fingerprint | None]]]:
    reject_optimized_python()
    if len(pairs) != 6 or tuple(target for _, target in pairs) != EXPECTED_TARGET_NAMES:
        raise PromotionError("the six targets and their order are fixed")
    if fail_after is not None and fail_after not in range(1, 7):
        raise PromotionError("--fail-after must be in 1..6")
    _verify_directory_binding(result_binding, "result directory during request validation")
    result_dir = result_binding.path
    result_metadata = os.fstat(result_binding.descriptor)
    require_exact_keys(
        expected_stage_snapshot,
        {"schema_id", "stage_device", "stage_inode", "entries"},
        "promotion stage snapshot",
    )
    snapshot_entries = expected_stage_snapshot["entries"]
    if [entry["name"] for entry in snapshot_entries] != list(EXPECTED_TARGET_NAMES):
        raise PromotionError("promotion requires an exact six-entry final stage snapshot")
    snapshot_by_name = {entry["name"]: entry["fingerprint"] for entry in snapshot_entries}

    stage_parents = {source.absolute().parent for source, _ in pairs}
    if len(stage_parents) != 1:
        raise PromotionError("all six sources must share one active stage")
    stage = next(iter(stage_parents))
    if (
        stage.parent != result_dir
        or STAGE_NAME_PATTERN.fullmatch(stage.name) is None
    ):
        raise PromotionError("sources must be in one named active stage under results")
    if any(source.absolute().name != target_name for source, target_name in pairs):
        raise PromotionError("source basenames must equal the fixed target basenames")
    stage_binding = _bind_child_directory(
        result_binding,
        stage.name,
        stage,
        "promotion stage",
        expected_identity=(
            expected_stage_snapshot["stage_device"],
            expected_stage_snapshot["stage_inode"],
        ),
    )
    source_inodes = set()
    target_inodes = set()
    validated = []
    try:
        for source_argument, target_name in pairs:
            source = source_argument.absolute()
            source_fingerprint = _fingerprint_at(
                stage_binding, source.name, "promotion source"
            )
            if not deep_exact(
                _fingerprint_object(source_fingerprint), snapshot_by_name[target_name]
            ):
                raise PromotionError(
                    "promotion source differs from the final owned stage snapshot"
                )
            if source_fingerprint.device != result_metadata.st_dev:
                raise PromotionError("cross-filesystem promotion is forbidden")
            source_inode = (source_fingerprint.device, source_fingerprint.inode)
            if source_inode in source_inodes:
                raise PromotionError("promotion sources must not hardlink each other")
            source_inodes.add(source_inode)
            target = result_dir / target_name
            preimage = None
            if _lexists_at(result_binding, target_name):
                preimage = _fingerprint_at(
                    result_binding, target_name, "promotion target"
                )
                target_inode = (preimage.device, preimage.inode)
                if target_inode in target_inodes or target_inode in source_inodes:
                    raise PromotionError("target hardlink alias is forbidden")
                target_inodes.add(target_inode)
            validated.append((source, target, source_fingerprint, preimage))
        if source_inodes & target_inodes:
            raise PromotionError("a promotion source aliases an existing target")
        observed_stage = set(os.listdir(stage_binding.descriptor))
        if observed_stage != set(EXPECTED_TARGET_NAMES):
            raise PromotionError("active stage must contain exactly the six promotion sources")
        allowed_live = set(EXPECTED_TARGET_NAMES) | {
            "RESULTS.md",
            "TEST_REPORT.md",
            stage.name,
        }
        observed_live = set(os.listdir(result_binding.descriptor))
        if not observed_live.issubset(allowed_live) or stage.name not in observed_live:
            extra = sorted(observed_live - allowed_live)
            raise PromotionError(f"foreign result debris blocks promotion: {extra}")
        for name in observed_live:
            metadata = os.stat(
                name, dir_fd=result_binding.descriptor, follow_symlinks=False
            )
            if name == stage.name:
                if (
                    stat.S_ISLNK(metadata.st_mode)
                    or not stat.S_ISDIR(metadata.st_mode)
                    or (metadata.st_dev, metadata.st_ino)
                    != (stage_binding.device, stage_binding.inode)
                ):
                    raise PromotionError("active stage pathname changed")
            elif stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
                raise PromotionError(f"nonregular live result blocks promotion: {name}")
        _verify_directory_binding(result_binding, "result directory after request validation")
        _verify_directory_binding(stage_binding, "promotion stage after request validation")
        return stage_binding, validated
    except BaseException:
        _close_directory_binding(stage_binding)
        raise


def _verify_preimages(
    entries: Sequence[Entry], result_binding: DirectoryBinding
) -> None:
    _verify_directory_binding(result_binding, "result directory during rollback verification")
    failures = []
    for entry in entries:
        if entry.preimage is None:
            if _lexists_at(result_binding, entry.target.name):
                failures.append(f"expected absent target: {entry.target.name}")
        else:
            try:
                restored = _fingerprint_at(
                    result_binding, entry.target.name, "restored target"
                )
            except BaseException as exc:
                failures.append(f"unreadable {entry.target.name}: {exc}")
            else:
                if restored.restored_fields() != entry.preimage.restored_fields():
                    failures.append(f"metadata/content mismatch: {entry.target.name}")
    if failures:
        raise RollbackError("; ".join(failures))
    _verify_directory_binding(result_binding, "result directory after rollback verification")


def _verify_precommit_preimages(
    entries: Sequence[Entry],
    result_binding: DirectoryBinding,
    transaction_binding: DirectoryBinding,
) -> None:
    _verify_directory_binding(result_binding, "result directory at precommit")
    _verify_directory_binding(transaction_binding, "transaction directory at precommit")
    for entry in entries:
        if entry.staged_fingerprint is None or _fingerprint_at(
            transaction_binding, entry.staged.name, "precommit staged copy"
        ) != entry.staged_fingerprint:
            raise PromotionError("a staged transaction copy changed before commit")
        if entry.preimage is not None and (
            entry.backup_fingerprint is None
            or _fingerprint_at(
                transaction_binding, entry.backup.name, "precommit backup"
            )
            != entry.backup_fingerprint
        ):
            raise PromotionError("a transaction backup changed before commit")
        if entry.preimage is None:
            if _lexists_at(result_binding, entry.target.name):
                raise PromotionError("an absent preimage appeared before commit")
        elif _fingerprint_at(
            result_binding, entry.target.name, "precommit target"
        ) != entry.preimage:
            raise PromotionError("a target changed before commit")
    _verify_directory_binding(result_binding, "result directory after precommit")
    _verify_directory_binding(transaction_binding, "transaction directory after precommit")


def _cleanup_transaction(
    entries: Sequence[Entry],
    transaction_binding: DirectoryBinding,
    result_binding: DirectoryBinding,
) -> None:
    # Phase one is read-only: reject missing, substituted, or extra entries before
    # deleting any evidence owned by this transaction.
    _verify_directory_binding(result_binding, "result directory at transaction cleanup")
    _verify_directory_binding(transaction_binding, "transaction directory at cleanup")
    expected_resident: dict[str, Fingerprint] = {}
    expected_absent: set[str] = set()
    for entry in entries:
        for path, expected, resident in (
            (entry.staged, entry.staged_fingerprint, entry.staged_resident),
            (entry.backup, entry.backup_fingerprint, entry.backup_resident),
        ):
            if resident:
                if expected is None:
                    raise PromotionError("resident transaction entry lacks a fingerprint")
                expected_resident[path.name] = expected
            else:
                expected_absent.add(path.name)
    observed_paths = set(os.listdir(transaction_binding.descriptor))
    if observed_paths != set(expected_resident):
        raise PromotionError("transaction inventory differs from recorded resident state")
    for name in expected_absent:
        if _lexists_at(transaction_binding, name):
            raise PromotionError("nonresident transaction path reappeared")
    for name, expected in expected_resident.items():
        if _fingerprint_at(transaction_binding, name, "owned transaction entry") != expected:
            raise PromotionError("foreign/replaced transaction entry retained")
    _fsync_directory_binding(transaction_binding, "transaction directory before cleanup")

    # Phase two deletes only entries whose identity was already bound above and
    # rechecks each identity immediately before unlink.
    for name, expected in expected_resident.items():
        _verify_directory_binding(result_binding, "result directory during transaction cleanup")
        _fsync_directory_binding(transaction_binding, "transaction directory during cleanup")
        if _fingerprint_at(transaction_binding, name, "owned transaction entry") != expected:
            raise PromotionError("transaction entry changed during cleanup; retaining remainder")
        os.unlink(name, dir_fd=transaction_binding.descriptor)
        _fsync_directory_binding(transaction_binding, "transaction directory after cleanup unlink")
        _verify_directory_binding(result_binding, "result directory after transaction cleanup unlink")
    if os.listdir(transaction_binding.descriptor):
        raise PromotionError("transaction final identity/inventory changed")
    _verify_directory_binding(transaction_binding, "transaction directory before removal")
    _verify_directory_binding(result_binding, "result directory before transaction removal")
    transaction_name = transaction_binding.path.name
    _close_directory_binding(transaction_binding)
    os.rmdir(transaction_name, dir_fd=result_binding.descriptor)
    _fsync_directory_binding(result_binding, "result directory after transaction removal")


def promote(
    pairs: Sequence[tuple[Path, str]],
    result_dir: Path,
    *,
    expected_stage_snapshot: dict[str, object],
    fail_after: int | None = None,
) -> None:
    result_binding = _bind_directory(result_dir, "result directory")
    stage_binding: DirectoryBinding | None = None
    transaction_binding: DirectoryBinding | None = None
    lock: LockHandle | None = None
    try:
        stage_binding, validated = _validate_request(
            pairs, result_binding, fail_after, expected_stage_snapshot
        )
        lock = acquire_lock(result_binding)
        transaction_name = f".c60-transaction-{uuid.uuid4().hex}"
        transaction = result_binding.path / transaction_name
        entries: list[Entry] = []
        replaced = 0
        primary_error: BaseException | None = None
        rollback_failed = False
        committed = False
        try:
            _verify_directory_binding(result_binding, "result directory before transaction mkdir")
            os.mkdir(transaction_name, 0o700, dir_fd=result_binding.descriptor)
            _verify_directory_binding(result_binding, "result directory after transaction mkdir")
            transaction_binding = _bind_child_directory(
                result_binding,
                transaction_name,
                transaction,
                "promotion transaction",
            )
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
                entry.staged_fingerprint = _copy_stable_bound(
                    source,
                    source_fingerprint,
                    transaction_binding,
                    entry.staged.name,
                    source_binding=stage_binding,
                )
                entry.staged_resident = True
                if preimage is not None:
                    entry.backup_fingerprint = _copy_stable_bound(
                        target,
                        preimage,
                        transaction_binding,
                        entry.backup.name,
                        source_binding=result_binding,
                    )
                    entry.backup_resident = True
            _fsync_directory_binding(transaction_binding, "transaction after copies")
            _verify_directory_binding(result_binding, "result directory before precommit")

            for entry in entries:
                if _fingerprint_at(
                    stage_binding, entry.source.name, "promotion source"
                ) != entry.source_fingerprint:
                    raise PromotionError("promotion source changed before commit")
            _verify_precommit_preimages(
                entries, result_binding, transaction_binding
            )

            for entry in entries:
                _verify_directory_binding(result_binding, "result directory before replacement")
                _verify_directory_binding(transaction_binding, "transaction before replacement")
                if entry.staged_fingerprint is None:
                    raise PromotionError("missing staged copy fingerprint")
                if _fingerprint_at(
                    stage_binding, entry.source.name, "per-replacement source"
                ) != entry.source_fingerprint:
                    raise PromotionError("promotion source changed before replacement")
                if _fingerprint_at(
                    transaction_binding, entry.staged.name, "per-replacement staged copy"
                ) != entry.staged_fingerprint:
                    raise PromotionError("staged copy changed before replacement")
                if entry.preimage is not None and (
                    entry.backup_fingerprint is None
                    or _fingerprint_at(
                        transaction_binding,
                        entry.backup.name,
                        "per-replacement backup",
                    )
                    != entry.backup_fingerprint
                ):
                    raise PromotionError("backup changed before replacement")
                _verify_directory_binding(result_binding, "result directory at replacement")
                _verify_directory_binding(transaction_binding, "transaction at replacement")
                os.replace(
                    entry.staged.name,
                    entry.target.name,
                    src_dir_fd=transaction_binding.descriptor,
                    dst_dir_fd=result_binding.descriptor,
                )
                replaced += 1
                entry.staged_resident = False
                _verify_directory_binding(result_binding, "result directory after replacement")
                _verify_directory_binding(transaction_binding, "transaction after replacement")
                _fsync_directory_binding(transaction_binding, "transaction after replacement")
                _fsync_directory_binding(result_binding, "result directory after replacement")
                entry.placed_fingerprint = _fingerprint_at(
                    result_binding, entry.target.name, "placed target"
                )
                if entry.placed_fingerprint != entry.staged_fingerprint:
                    raise PromotionError("placed target differs from staged copy identity")
                if _fingerprint_at(
                    stage_binding, entry.source.name, "post-replacement source"
                ) != entry.source_fingerprint:
                    raise PromotionError("promotion source changed during replacement")
                if entry.preimage is not None and _fingerprint_at(
                    transaction_binding, entry.backup.name, "post-replacement backup"
                ) != entry.backup_fingerprint:
                    raise PromotionError("backup changed during replacement")
                if fail_after == replaced:
                    raise RuntimeError(f"test-injected failure after replacement {replaced}")
            for entry in entries:
                _verify_directory_binding(result_binding, "result directory at final verification")
                if entry.placed_fingerprint is None or _fingerprint_at(
                    result_binding, entry.target.name, "final placed target"
                ) != entry.placed_fingerprint:
                    raise PromotionError("a placed target changed before transaction completion")
                if _fingerprint_at(
                    stage_binding, entry.source.name, "final promotion source"
                ) != entry.source_fingerprint:
                    raise PromotionError("a promotion source changed before transaction completion")
            _fsync_directory_binding(transaction_binding, "transaction at commit")
            _fsync_directory_binding(result_binding, "result directory at commit")
            committed = True
        except BaseException as exc:
            primary_error = exc
            try:
                if transaction_binding is None:
                    raise RollbackError("transaction capability unavailable")
                for entry in reversed(entries[:replaced]):
                    _verify_directory_binding(result_binding, "result directory before rollback")
                    _verify_directory_binding(transaction_binding, "transaction before rollback")
                    expected_placed = entry.placed_fingerprint or entry.staged_fingerprint
                    if expected_placed is None:
                        raise RollbackError("missing placed/staged fingerprint")
                    current = _fingerprint_at(
                        result_binding, entry.target.name, "rollback target"
                    )
                    if current != expected_placed:
                        raise RollbackError("foreign target replacement detected during rollback")
                    if entry.preimage is None:
                        os.unlink(entry.target.name, dir_fd=result_binding.descriptor)
                        _fsync_directory_binding(result_binding, "result directory after rollback unlink")
                    else:
                        if entry.backup_fingerprint is None or _fingerprint_at(
                            transaction_binding, entry.backup.name, "rollback backup"
                        ) != entry.backup_fingerprint:
                            raise RollbackError("backup changed before rollback")
                        os.replace(
                            entry.backup.name,
                            entry.target.name,
                            src_dir_fd=transaction_binding.descriptor,
                            dst_dir_fd=result_binding.descriptor,
                        )
                        entry.backup_resident = False
                        _fsync_directory_binding(transaction_binding, "transaction after rollback")
                        _fsync_directory_binding(result_binding, "result directory after rollback")
                _verify_preimages(entries, result_binding)
            except BaseException as rollback_exc:
                rollback_failed = True
                raise RollbackError(
                    f"rollback after {primary_error!r} failed: {rollback_exc}"
                ) from rollback_exc
            raise RolledBackVerifiedError(
                f"ROLLED_BACK_VERIFIED: exact live preimages restored after {exc!r}"
            ) from exc
        finally:
            cleanup_error: BaseException | None = None
            if not rollback_failed:
                try:
                    if transaction_binding is not None:
                        _cleanup_transaction(
                            entries, transaction_binding, result_binding
                        )
                except BaseException as exc:
                    cleanup_error = exc
            try:
                if lock is not None:
                    held_lock = lock
                    lock = None
                    release_lock(held_lock, result_binding)
            except BaseException as exc:
                if cleanup_error is None:
                    cleanup_error = exc
            if cleanup_error is not None and primary_error is None:
                if committed:
                    raise PostCommitError(
                        "COMMITTED_WITH_DEBRIS: live six-target commit is durable; "
                        "postcommit cleanup/lock release failed; DO NOT RETRY"
                    ) from cleanup_error
                raise cleanup_error
            if cleanup_error is not None and primary_error is not None and not rollback_failed:
                raise RolledBackVerifiedError(
                    "ROLLED_BACK_VERIFIED_WITH_DEBRIS: exact live preimages restored; "
                    "transaction/lock cleanup incomplete"
                ) from cleanup_error
    finally:
        if lock is not None:
            os.close(lock.descriptor)
        if transaction_binding is not None:
            _close_directory_binding(transaction_binding)
        if stage_binding is not None:
            _close_directory_binding(stage_binding)
        _close_directory_binding(result_binding)


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
    result_binding, stage_binding = _bind_stage_directories(
        result_dir,
        stage,
        expected_device=expected_snapshot["stage_device"],
        expected_inode=expected_snapshot["stage_inode"],
    )
    try:
        expected_entries = expected_snapshot["entries"]
        expected_names = [entry["name"] for entry in expected_entries]
        if set(os.listdir(stage_binding.descriptor)) != set(expected_names):
            raise PromotionError("cleanup stage inventory changed; retaining it")
        expected_by_name = {
            entry["name"]: entry["fingerprint"] for entry in expected_entries
        }
        ordered = sorted(expected_names, key=EXPECTED_TARGET_NAMES.index)
        for name in ordered:
            actual = _fingerprint_object(
                _fingerprint_at(stage_binding, name, "cleanup stage file")
            )
            if not deep_exact(actual, expected_by_name[name]):
                raise PromotionError("cleanup stage file identity changed; retaining it")
        for name in ordered:
            _verify_directory_binding(result_binding, "result directory during stage cleanup")
            _verify_directory_binding(stage_binding, "active stage during cleanup")
            actual = _fingerprint_object(
                _fingerprint_at(stage_binding, name, "cleanup stage file")
            )
            if not deep_exact(actual, expected_by_name[name]):
                raise PromotionError("cleanup stage file was replaced; retaining it")
            os.unlink(name, dir_fd=stage_binding.descriptor)
            _fsync_directory_binding(stage_binding, "active stage after cleanup unlink")
            _verify_directory_binding(result_binding, "result directory after stage cleanup unlink")
        if os.listdir(stage_binding.descriptor):
            raise PromotionError("cleanup stage final identity/inventory changed; retaining it")
        _verify_directory_binding(stage_binding, "active stage before removal")
        _verify_directory_binding(result_binding, "result directory before stage removal")
        stage_name = stage_binding.path.name
        _close_directory_binding(stage_binding)
        os.rmdir(stage_name, dir_fd=result_binding.descriptor)
        _fsync_directory_binding(result_binding, "result directory after stage removal")
    finally:
        _close_directory_binding(stage_binding)
        _close_directory_binding(result_binding)


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
        print("C60 checker-to-manifest stage extension PASS")
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
        print("C60 active stage identity-bound cleanup PASS")
        return 0
    if not arguments.source or not arguments.target:
        parser.error("promotion requires six --source/--target pairs")
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
    print("C60 rollback-atomic six-target promotion PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
