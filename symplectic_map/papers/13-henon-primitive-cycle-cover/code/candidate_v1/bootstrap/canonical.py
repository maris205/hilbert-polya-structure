"""Strict canonical JSON, hashes, and durable exclusive writes."""

import hashlib
import json
import os
from pathlib import Path


def _reject_constant(value: str):
    raise ValueError("nonfinite JSON constant: " + value)


def _reject_float(value: str):
    raise ValueError("floating JSON number forbidden: " + value)


def _pairs_no_duplicates(pairs):
    output = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate JSON key: " + key)
        output[key] = value
    return output


def strict_load_bytes(payload: bytes):
    if type(payload) is not bytes:
        raise TypeError("JSON payload must be bytes")
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("JSON is not UTF-8") from exc
    return json.loads(
        text,
        object_pairs_hook=_pairs_no_duplicates,
        parse_constant=_reject_constant,
        parse_float=_reject_float,
    )


def canonical_bytes(value) -> bytes:
    pending = [value]
    while pending:
        item = pending.pop()
        if type(item) not in (dict, list, str, int, bool, type(None)):
            raise TypeError("non-JSON value is forbidden in canonical JSON")
        if type(item) is dict:
            if any(type(key) is not str for key in item):
                raise TypeError("canonical JSON object keys must be strings")
            pending.extend(item.keys())
            pending.extend(item.values())
        elif type(item) is list:
            pending.extend(item)
    return (
        json.dumps(
            value,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("ascii")


def strict_canonical_load(payload: bytes):
    value = strict_load_bytes(payload)
    if canonical_bytes(value) != payload:
        raise ValueError("JSON bytes are not canonical")
    return value


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    _assert_no_symlink_ancestor(path)
    with path.open("rb") as handle:
        digest = hashlib.sha256()
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def read_regular_bytes(path: Path) -> bytes:
    _assert_no_symlink_ancestor(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError("regular non-symlink file required: " + path.as_posix())
    return path.read_bytes()


def fsync_directory(directory: Path) -> None:
    _assert_no_symlink_ancestor(directory)
    descriptor = os.open(directory, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_bytes_exclusive(path: Path, payload: bytes) -> None:
    _assert_no_symlink_ancestor(path)
    if path.exists() or path.is_symlink():
        raise FileExistsError(path)
    _ensure_directory_chain(path.parent)
    _assert_no_symlink_ancestor(path)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    descriptor = os.open(path, flags, 0o600)
    try:
        offset = 0
        while offset < len(payload):
            written = os.write(descriptor, payload[offset:])
            if written <= 0:
                raise OSError("short durable write")
            offset += written
        os.fsync(descriptor)
    except BaseException:
        try:
            os.close(descriptor)
        finally:
            if path.exists() and not path.is_symlink():
                path.unlink()
                fsync_directory(path.parent)
        raise
    else:
        os.close(descriptor)
    fsync_directory(path.parent)


def _ensure_directory_chain(directory: Path) -> None:
    absolute = directory.absolute()
    missing = []
    cursor = absolute
    while True:
        if cursor.is_symlink():
            raise ValueError("symlink directory component forbidden: " + cursor.as_posix())
        if cursor.exists():
            if not cursor.is_dir():
                raise ValueError("directory component is not a directory: " + cursor.as_posix())
            break
        missing.append(cursor)
        parent = cursor.parent
        if parent == cursor:
            raise ValueError("no existing directory ancestor")
        cursor = parent
    for target in reversed(missing):
        parent = target.parent
        _assert_no_symlink_ancestor(parent)
        try:
            os.mkdir(target, 0o700)
        except FileExistsError:
            if target.is_symlink() or not target.is_dir():
                raise ValueError("raced directory component is not regular: " + target.as_posix())
        else:
            fsync_directory(parent)
        if target.is_symlink() or not target.is_dir():
            raise ValueError("created directory component drift: " + target.as_posix())


def _assert_no_symlink_ancestor(path: Path) -> None:
    absolute = path.absolute()
    for ancestor in (absolute, *absolute.parents):
        if ancestor.is_symlink():
            raise ValueError("symlink path component forbidden: " + ancestor.as_posix())


def write_json_exclusive(path: Path, value) -> str:
    payload = canonical_bytes(value)
    write_bytes_exclusive(path, payload)
    return sha256_bytes(payload)
