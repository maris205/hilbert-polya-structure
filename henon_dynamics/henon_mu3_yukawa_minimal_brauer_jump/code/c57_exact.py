#!/usr/bin/env python3
"""Small, producer-neutral exact-I/O primitives for HCS-C57.

The checker may import this module.  It deliberately contains no C57 witness
construction and no expected mathematical answers.
"""

from __future__ import annotations

from dataclasses import dataclass
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys
from typing import Any, Iterable, NoReturn


# Every caller supplies a byte ceiling before parsing.  The exact transcripts
# legitimately contain a 100609-digit CRT modulus, so Python's unrelated
# decimal-display guard cannot be the size authority.
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


class StrictDataError(ValueError):
    """A byte-level or structural certificate firewall rejected input."""


def reject_optimized_python() -> None:
    if not __debug__ or sys.flags.optimize or "PYTHONOPTIMIZE" in os.environ:
        raise StrictDataError(
            "optimized Python and the PYTHONOPTIMIZE environment variable are forbidden"
        )


def _reject_float(_: str) -> NoReturn:
    raise StrictDataError("JSON floating-point literals are forbidden")


def _reject_constant(_: str) -> NoReturn:
    raise StrictDataError("non-finite JSON constants are forbidden")


def _canonical_integer(token: str) -> int:
    # RFC 8259 permits -0, but C57 has one byte-level representation for every
    # integer.  json.loads otherwise silently maps both 0 and -0 to int(0).
    if token == "0":
        return 0
    negative = token.startswith("-")
    digits = token[1:] if negative else token
    if not digits or digits[0] == "0" or not digits.isascii() or not digits.isdigit():
        raise StrictDataError("noncanonical JSON integer token")
    return int(token)


def _unique_pairs(pairs: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictDataError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(raw: bytes, *, max_bytes: int) -> Any:
    if type(raw) is not bytes:
        raise StrictDataError("JSON input must be bytes")
    if len(raw) > max_bytes:
        raise StrictDataError("JSON input exceeds size limit")
    if raw.startswith(b"\xef\xbb\xbf"):
        raise StrictDataError("UTF-8 BOM is forbidden")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise StrictDataError("JSON input is not strict UTF-8") from exc
    try:
        return json.loads(
            text,
            object_pairs_hook=_unique_pairs,
            parse_int=_canonical_integer,
            parse_float=_reject_float,
            parse_constant=_reject_constant,
        )
    except StrictDataError:
        raise
    except (json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise StrictDataError("invalid JSON") from exc


def canonical_json_bytes(value: Any, *, pretty: bool = False) -> bytes:
    options: dict[str, Any] = {
        "sort_keys": True,
        "ensure_ascii": False,
        "allow_nan": False,
    }
    if pretty:
        options["indent"] = 2
    else:
        options["separators"] = (",", ":")
    return json.dumps(value, **options).encode("utf-8") + b"\n"


def canonical_leaf_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def require_canonical_compact_json(raw: bytes) -> None:
    """Verify compact sorted-key JSON lexically, without reprinting huge ints."""
    if type(raw) is not bytes or not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise StrictDataError("canonical compact JSON requires one terminal newline")
    try:
        text = raw[:-1].decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise StrictDataError("canonical JSON is not UTF-8") from exc
    position = 0

    def parse_string() -> str:
        nonlocal position
        if position >= len(text) or text[position] != '"':
            raise StrictDataError("canonical JSON string expected")
        start = position
        position += 1
        while position < len(text):
            character = text[position]
            if character == '"':
                position += 1
                token = text[start:position]
                try:
                    value = json.loads(token)
                except json.JSONDecodeError as exc:
                    raise StrictDataError("invalid JSON string token") from exc
                canonical = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
                if token != canonical:
                    raise StrictDataError("noncanonical JSON string escaping")
                return value
            if character == "\\":
                position += 2
                continue
            if ord(character) < 0x20:
                raise StrictDataError("unescaped JSON control character")
            position += 1
        raise StrictDataError("unterminated JSON string")

    def parse_value() -> None:
        nonlocal position
        if position >= len(text):
            raise StrictDataError("unexpected end of canonical JSON")
        character = text[position]
        if character == "{":
            position += 1
            prior_key = None
            if position < len(text) and text[position] == "}":
                position += 1
                return
            while True:
                key = parse_string()
                if prior_key is not None and not prior_key < key:
                    raise StrictDataError("JSON object keys are not strictly sorted")
                prior_key = key
                if position >= len(text) or text[position] != ":":
                    raise StrictDataError("noncompact/missing JSON colon")
                position += 1
                parse_value()
                if position >= len(text):
                    raise StrictDataError("unterminated JSON object")
                if text[position] == "}":
                    position += 1
                    return
                if text[position] != ",":
                    raise StrictDataError("noncompact/missing JSON object comma")
                position += 1
        elif character == "[":
            position += 1
            if position < len(text) and text[position] == "]":
                position += 1
                return
            while True:
                parse_value()
                if position >= len(text):
                    raise StrictDataError("unterminated JSON array")
                if text[position] == "]":
                    position += 1
                    return
                if text[position] != ",":
                    raise StrictDataError("noncompact/missing JSON array comma")
                position += 1
        elif character == '"':
            parse_string()
        elif text.startswith("true", position):
            position += 4
        elif text.startswith("false", position):
            position += 5
        elif text.startswith("null", position):
            position += 4
        else:
            start = position
            if text[position] == "-":
                position += 1
            digit_start = position
            while position < len(text) and "0" <= text[position] <= "9":
                position += 1
            token = text[start:position]
            if (
                digit_start == position
                or token == "-0"
                or (token.startswith("0") and token != "0")
                or (token.startswith("-0"))
            ):
                raise StrictDataError("noncanonical JSON integer")
        # Whitespace, floats, and unexpected punctuation are rejected by the
        # exact delimiter checks in the caller or at the root boundary.

    parse_value()
    if position != len(text):
        raise StrictDataError("trailing or noncompact JSON bytes")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe_relative_path(value: str) -> bool:
    if type(value) is not str or "\\" in value:
        return False
    path = PurePosixPath(value)
    return (
        not path.is_absolute()
        and str(path) == value
        and all(part not in ("", ".", "..") for part in path.parts)
    )


def regular_file(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISREG(metadata.st_mode) and not path.is_symlink()


@dataclass(frozen=True)
class Fingerprint:
    sha256: str
    size_bytes: int
    mode: int
    mtime_ns: int


def read_stable(path: Path, *, max_bytes: int | None = None) -> tuple[bytes, Fingerprint]:
    if not regular_file(path):
        raise StrictDataError(f"required non-symlink regular file missing: {path}")
    flags = os.O_RDONLY
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(path, flags)
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise StrictDataError(f"not a regular file: {path}")
        chunks: list[bytes] = []
        size = 0
        while True:
            block = os.read(descriptor, 1 << 20)
            if not block:
                break
            size += len(block)
            if max_bytes is not None and size > max_bytes:
                raise StrictDataError(f"file exceeds size limit: {path}")
            chunks.append(block)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    stable = (
        before.st_dev,
        before.st_ino,
        before.st_size,
        before.st_mode,
        before.st_mtime_ns,
        before.st_ctime_ns,
    ) == (
        after.st_dev,
        after.st_ino,
        after.st_size,
        after.st_mode,
        after.st_mtime_ns,
        after.st_ctime_ns,
    )
    if not stable:
        raise StrictDataError(f"file changed while being read: {path}")
    raw = b"".join(chunks)
    return raw, Fingerprint(
        sha256=sha256_bytes(raw),
        size_bytes=len(raw),
        mode=stat.S_IMODE(after.st_mode),
        mtime_ns=after.st_mtime_ns,
    )


def sha256_file(path: Path) -> str:
    return read_stable(path)[1].sha256


def deterministic_gzip(raw: bytes, *, level: int = 9) -> bytes:
    destination = io.BytesIO()
    with gzip.GzipFile(
        filename="", mode="wb", fileobj=destination, compresslevel=level, mtime=0
    ) as stream:
        stream.write(raw)
    return destination.getvalue()


def strict_gzip_json(
    path: Path, *, max_compressed_bytes: int, max_decompressed_bytes: int
) -> tuple[Any, bytes, Fingerprint]:
    compressed, fingerprint = read_stable(path, max_bytes=max_compressed_bytes)
    if len(compressed) < 10 or compressed[:2] != b"\x1f\x8b":
        raise StrictDataError(f"not a gzip artifact: {path}")
    if int.from_bytes(compressed[4:8], "little") != 0:
        raise StrictDataError(f"gzip mtime must be zero: {path}")
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(compressed), mode="rb") as stream:
            raw = stream.read(max_decompressed_bytes + 1)
            trailing = stream.read(1)
    except (OSError, EOFError) as exc:
        raise StrictDataError(f"invalid gzip artifact: {path}") from exc
    if len(raw) > max_decompressed_bytes or trailing:
        raise StrictDataError(f"decompressed artifact exceeds size limit: {path}")
    value = strict_json_loads(raw, max_bytes=max_decompressed_bytes)
    return value, raw, fingerprint


def atomic_write(path: Path, raw: bytes, *, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.parent.is_symlink() or path.is_symlink():
        raise StrictDataError(f"symlink output forbidden: {path}")
    temporary = path.with_name(f".{path.name}.{os.getpid()}.new")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = -1
    try:
        descriptor = os.open(temporary, flags, 0o600)
        view = memoryview(raw)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short write")
            view = view[written:]
        os.fchmod(descriptor, mode)
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = -1
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        temporary.unlink(missing_ok=True)


def require_exact_keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict:
        raise StrictDataError(f"{label} must be an object")
    observed = set(value)
    if observed != expected:
        raise StrictDataError(
            f"{label} key mismatch; missing={sorted(expected-observed)}; "
            f"extra={sorted(observed-expected)}"
        )
    return value


def require_int(value: Any, label: str) -> int:
    if type(value) is not int:
        raise StrictDataError(f"{label} must be an integer (booleans forbidden)")
    return value


def require_bool(value: Any, label: str) -> bool:
    if type(value) is not bool:
        raise StrictDataError(f"{label} must be a boolean")
    return value


def deep_exact(left: Any, right: Any) -> bool:
    """Recursive equality with exact Python types (so True never equals 1)."""
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            deep_exact(left[key], right[key]) for key in left
        )
    if type(left) is list:
        return len(left) == len(right) and all(
            deep_exact(a, b) for a, b in zip(left, right)
        )
    if left is None or type(left) in (bool, int, str):
        return left == right
    return False


def prepare_output_targets(
    outputs: Iterable[Path], *, protected: Iterable[Path]
) -> tuple[Path, ...]:
    """Validate output aliases/inodes completely, then remove stale regular files."""
    output_paths = tuple(path.absolute() for path in outputs)
    if not output_paths:
        raise StrictDataError("at least one output target is required")
    resolved_outputs: list[Path] = []
    for output in output_paths:
        parent = output.parent
        if (
            not parent.exists()
            or parent.is_symlink()
            or not parent.is_dir()
            or parent.resolve(strict=True) != parent
        ):
            raise StrictDataError("output parent must be an existing real directory")
        resolved_outputs.append(parent / output.name)
    if len(set(resolved_outputs)) != len(resolved_outputs):
        raise StrictDataError("output targets alias after path resolution")

    protected_paths = []
    protected_inodes = set()
    for path in protected:
        absolute = path.absolute()
        resolved = absolute.resolve(strict=False)
        protected_paths.append(resolved)
        if regular_file(path):
            metadata = path.stat()
            protected_inodes.add((metadata.st_dev, metadata.st_ino))

    output_inodes = set()
    for output in resolved_outputs:
        if output in protected_paths:
            raise StrictDataError("output target aliases a protected input path")
        if os.path.lexists(output):
            metadata = output.lstat()
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
                raise StrictDataError("output must be absent or a regular non-symlink file")
            inode = (metadata.st_dev, metadata.st_ino)
            if inode in protected_inodes:
                raise StrictDataError("output target hardlinks a protected input")
            if inode in output_inodes:
                raise StrictDataError("output targets hardlink each other")
            output_inodes.add(inode)

    # No target is removed until every target and every protected source has
    # passed path and inode validation.
    for output in resolved_outputs:
        if os.path.lexists(output):
            output.unlink()
    return tuple(resolved_outputs)


def require_sha256(value: Any, label: str) -> str:
    if (
        type(value) is not str
        or len(value) != 64
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise StrictDataError(f"{label} must be a lowercase SHA-256 digest")
    return value
