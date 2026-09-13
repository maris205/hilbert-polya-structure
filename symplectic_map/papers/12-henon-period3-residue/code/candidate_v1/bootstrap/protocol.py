"""Strict exact I/O primitives used only outside the scientific engines."""

from __future__ import annotations

import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


class DuplicateJSONKeyError(ValueError):
    """A supposedly exact JSON object repeated a key."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError("duplicate JSON key: " + key)
        result[key] = value
    return result


def strict_json_loads(text: str) -> Any:
    def reject_constant(value: str) -> None:
        raise ValueError("non-finite JSON value: " + value)

    def reject_float(value: str) -> None:
        raise ValueError("floating JSON value: " + value)

    return json.loads(
        text,
        object_pairs_hook=_unique_object,
        parse_constant=reject_constant,
        parse_float=reject_float,
    )


def strict_source_json_loads(text: str) -> Any:
    """Parse immutable hash-bound source metadata, preserving decimals as opaque tokens."""

    def reject_constant(value: str) -> None:
        raise ValueError("non-finite source JSON value: " + value)

    return json.loads(
        text,
        object_pairs_hook=_unique_object,
        parse_constant=reject_constant,
        parse_float=lambda value: value,
    )


def exact_json(value: Any) -> Any:
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is tuple:
        return [exact_json(item) for item in value]
    if type(value) is list:
        return [exact_json(item) for item in value]
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, item in value.items():
            if type(key) is not str or key in result:
                raise TypeError("exact JSON requires unique string keys")
            result[key] = exact_json(item)
        return result
    raise TypeError("non-exact evidence type: " + type(value).__name__)


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        exact_json(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def pretty_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(exact_json(value), sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def reject_symlink_components(path: Path) -> None:
    absolute = lexical_absolute(path)
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        if current.exists() and stat.S_ISLNK(current.lstat().st_mode):
            raise RuntimeError("symlink component forbidden: " + os.fspath(current))


def regular_file(path: Path) -> bool:
    try:
        absolute = lexical_absolute(path)
        reject_symlink_components(absolute)
        return stat.S_ISREG(absolute.lstat().st_mode)
    except (OSError, RuntimeError):
        return False


def regular_directory(path: Path) -> bool:
    try:
        absolute = lexical_absolute(path)
        reject_symlink_components(absolute)
        return stat.S_ISDIR(absolute.lstat().st_mode)
    except (OSError, RuntimeError):
        return False


def _identity(metadata: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def stable_file_bytes(path: Path) -> bytes:
    absolute = lexical_absolute(path)
    reject_symlink_components(absolute)
    before = absolute.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise RuntimeError("stable read requires a regular file")
    descriptor = os.open(os.fspath(absolute), os.O_RDONLY | os.O_NOFOLLOW)
    try:
        opened = os.fstat(descriptor)
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    final = absolute.lstat()
    if _identity(before) != _identity(opened) or _identity(opened) != _identity(after):
        raise RuntimeError("file changed during stable read")
    if _identity(after) != _identity(final):
        raise RuntimeError("path changed during stable read")
    data = b"".join(chunks)
    if len(data) != before.st_size:
        raise RuntimeError("stable read size mismatch")
    return data


def sha256_file(path: Path) -> str:
    return hashlib.sha256(stable_file_bytes(path)).hexdigest()


def load_exact_json(path: Path) -> Any:
    return strict_json_loads(stable_file_bytes(path).decode("utf-8"))


def load_source_json(path: Path) -> Any:
    return strict_source_json_loads(stable_file_bytes(path).decode("utf-8"))


def fsync_directory(path: Path) -> None:
    absolute = lexical_absolute(path)
    reject_symlink_components(absolute)
    descriptor = os.open(os.fspath(absolute), os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_bytes_exclusive(path: Path, data: bytes) -> None:
    absolute = lexical_absolute(path)
    reject_symlink_components(absolute.parent)
    if not regular_directory(absolute.parent):
        raise RuntimeError("exclusive evidence parent is unsafe")
    descriptor = os.open(
        os.fspath(absolute),
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
        0o600,
    )
    try:
        offset = 0
        while offset < len(data):
            written = os.write(descriptor, data[offset:])
            if written < 1:
                raise OSError("short evidence write")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    fsync_directory(absolute.parent)


def write_json_exclusive(path: Path, value: Any, *, pretty: bool = False) -> None:
    data = pretty_json_bytes(value) if pretty else canonical_json_bytes(value)
    write_bytes_exclusive(path, data)


def mkdir_durable(path: Path) -> None:
    absolute = lexical_absolute(path)
    reject_symlink_components(absolute.parent)
    os.mkdir(os.fspath(absolute), 0o700)
    fsync_directory(absolute.parent)


def exact_same(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(exact_same(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(
            exact_same(left[index], right[index]) for index in range(len(left))
        )
    return left == right


def validate_canonical_json_file(path: Path) -> Any:
    data = stable_file_bytes(path)
    value = strict_json_loads(data.decode("utf-8"))
    if data != canonical_json_bytes(value):
        raise ValueError("JSON file is not canonical: " + os.fspath(path))
    return value
