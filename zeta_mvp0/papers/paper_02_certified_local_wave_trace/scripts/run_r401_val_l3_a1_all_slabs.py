#!/usr/bin/env python3
"""Prospective L3-A1 scheduler framework.

This module implements strict matrix/run-binding and mock-only static cell
transactions.  It deliberately contains no production evaluator dispatcher.
Production and non-mock initialize modes fail closed until the separately
accepted machine/main freezes and pre-freeze review exist.
"""

from __future__ import annotations

import argparse
import ctypes
import errno
import hashlib
import json
import math
import os
import re
import shutil
import stat
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"
SCHEDULER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"
)
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
)
MACHINE_FREEZE = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
)
MAIN_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
PREFREEZE_REVIEW = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md"
)
CANONICAL_RESULT = ROOT / "results/r401_val_l3_all_slabs"
CANONICAL_OPERATIONAL = ROOT / "results/r401_val_l3_all_slabs.operational"

PROTOCOL_ID = "R401-VAL-L3-A1"
SCHEMA_VERSION = 1
PRECISIONS = (128, 256)
SLAB_IDS = tuple(f"S{index:03d}" for index in range(51))
COMPONENTS = ("STATIC", "BRANCH")
SCHEDULER_POLICY = "deterministic_component_barrier_batches_v1"
PREFREEZE_ACCEPT_LINE = "Verdict: ACCEPT_FOR_FREEZE"
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
GENERATION_STAGING_PATTERN = (
    r"^\.(S(?:00[0-9]|0[1-4][0-9]|050))\.tmp-([0-9a-f]{16})-"
    r"(0|[1-9][0-9]*)$"
)
STAGING_BASENAME = re.compile(GENERATION_STAGING_PATTERN)

MOCK_CLAIM_BOUNDARY = (
    "synthetic static scheduler transaction only; no Arb/CAPD scientific "
    "evaluation, no component or local theorem, no global routing, trace, "
    "Hilbert-Polya, zeta-zero, or RH claim"
)


class SchedulerContractError(RuntimeError):
    """Base fail-closed scheduler error."""


class StrictJSONError(SchedulerContractError):
    """Strict JSON or type contract failure."""


class PathContractError(SchedulerContractError):
    """Unsafe, aliased, linked, or off-filesystem path."""


class ProductionAuthorityError(SchedulerContractError):
    """Missing or invalid production authority."""


class RunBindingMismatch(SchedulerContractError):
    """Resume binding differs from the sealed run config."""


class CorruptGeneration(SchedulerContractError):
    """Published or staged generation bytes fail validation."""


class SyntheticCrash(RuntimeError):
    """Test-only crash injected after the canonical cell rename."""


class SyntheticQuarantineCrash(RuntimeError):
    """Test-only crash injected at a durable quarantine boundary."""


@dataclass(frozen=True, order=True)
class CellKey:
    precision_bits: int
    slab_id: str

    def __post_init__(self) -> None:
        if type(self.precision_bits) is not int or self.precision_bits not in PRECISIONS:
            raise SchedulerContractError("invalid precision")
        if type(self.slab_id) is not str or self.slab_id not in SLAB_IDS:
            raise SchedulerContractError("invalid slab id")

    @property
    def label(self) -> str:
        return f"{self.precision_bits}:{self.slab_id}"

    def payload(self) -> dict[str, Any]:
        return {
            "precision_bits": self.precision_bits,
            "slab_id": self.slab_id,
        }


def exact_matrix() -> tuple[CellKey, ...]:
    return tuple(CellKey(bits, slab) for bits in PRECISIONS for slab in SLAB_IDS)


def matrix_payload() -> list[dict[str, Any]]:
    return [cell.payload() for cell in exact_matrix()]


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJSONError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise StrictJSONError(f"nonfinite JSON constant: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise StrictJSONError(f"nonfinite JSON number: {value}")
    return parsed


def strict_json_loads(raw: str) -> Any:
    try:
        return json.loads(
            raw,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except StrictJSONError:
        raise
    except (ValueError, TypeError, json.JSONDecodeError) as error:
        raise StrictJSONError(f"invalid JSON: {error}") from error


def strict_json_load(
    path: Path,
    *,
    reject_hardlink: bool = True,
    require_canonical: bool = False,
) -> Any:
    return strict_json_image(
        path,
        reject_hardlink=reject_hardlink,
        require_canonical=require_canonical,
    )[0]


def strict_json_image(
    path: Path,
    *,
    reject_hardlink: bool = True,
    require_canonical: bool = False,
) -> tuple[Any, bytes, os.stat_result]:
    raw_bytes, info = read_pinned_regular_file(
        path,
        reject_hardlink=reject_hardlink,
    )
    try:
        raw = raw_bytes.decode("utf-8")
    except UnicodeError as error:
        raise StrictJSONError(f"non-UTF8 JSON: {path}") from error
    payload = strict_json_loads(raw)
    if require_canonical and raw_bytes != canonical_json_bytes(payload):
        raise StrictJSONError(f"noncanonical JSON bytes: {path}")
    return payload, raw_bytes, info


def canonical_json_bytes(payload: Any) -> bytes:
    try:
        return (
            json.dumps(
                payload,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise StrictJSONError(f"payload is not canonical JSON: {error}") from error


def exact_json_equal(actual: Any, expected: Any) -> bool:
    if type(actual) is not type(expected):
        return False
    if isinstance(actual, dict):
        return (
            set(actual) == set(expected)
            and all(exact_json_equal(actual[key], expected[key]) for key in actual)
        )
    if isinstance(actual, list):
        return len(actual) == len(expected) and all(
            exact_json_equal(left, right) for left, right in zip(actual, expected)
        )
    return actual == expected


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    raw, _ = read_pinned_regular_file(path, reject_hardlink=False)
    return hashlib.sha256(raw).hexdigest()


def canonical_matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(matrix_payload()))


def exact_int(value: Any, context: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise StrictJSONError(f"{context} must be an exact integer >= {minimum}")
    return value


def exact_keys(payload: Mapping[str, Any], expected: set[str], context: str) -> None:
    if type(payload) is not dict or set(payload) != expected:
        actual = set(payload) if isinstance(payload, dict) else type(payload).__name__
        raise StrictJSONError(f"{context} key set mismatch: {actual}")


def safe_relative_path(value: str) -> PurePosixPath:
    if type(value) is not str or not value:
        raise PathContractError("relative path must be a nonempty string")
    if "\\" in value or value.startswith("/") or "//" in value:
        raise PathContractError(f"unsafe path: {value}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise PathContractError(f"unsafe path: {value}")
    if path.as_posix() != value or value.endswith("/"):
        raise PathContractError(f"noncanonical path: {value}")
    return path


def safe_absolute_path(value: str, context: str) -> Path:
    if type(value) is not str or not value.startswith("/"):
        raise PathContractError(f"{context} must be an absolute POSIX path string")
    if "\\" in value or "//" in value or value.endswith("/"):
        raise PathContractError(f"noncanonical {context}: {value}")
    pure = PurePosixPath(value)
    if any(part in {"", ".", ".."} for part in pure.parts[1:]):
        raise PathContractError(f"unsafe {context}: {value}")
    if pure.as_posix() != value:
        raise PathContractError(f"noncanonical {context}: {value}")
    return Path(value)


def reject_symlink_components(path: Path, *, allow_missing_leaf: bool = True) -> None:
    candidate = path.absolute()
    parts = candidate.parts
    current = Path(parts[0])
    for part in parts[1:]:
        current = current / part
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            if allow_missing_leaf:
                return
            raise PathContractError(f"missing path component: {current}")
        if stat.S_ISLNK(mode):
            raise PathContractError(f"symlink path component: {current}")


def require_regular_file(path: Path, *, reject_hardlink: bool = True) -> None:
    reject_symlink_components(path, allow_missing_leaf=False)
    info = path.stat()
    if not stat.S_ISREG(info.st_mode):
        raise PathContractError(f"not a regular file: {path}")
    if reject_hardlink and info.st_nlink != 1:
        raise PathContractError(f"hard-link alias rejected: {path}")


def require_directory(path: Path) -> None:
    reject_symlink_components(path, allow_missing_leaf=False)
    if not path.is_dir():
        raise PathContractError(f"not a directory: {path}")


def _open_directory_fd(path: Path) -> int:
    canonical = safe_absolute_path(os.fspath(path), "directory path")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for component in canonical.parts[1:]:
            next_fd = os.open(component, flags | nofollow, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = next_fd
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def ensure_real_directory_tree(path: Path) -> None:
    canonical = safe_absolute_path(os.fspath(path), "directory path")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for component in canonical.parts[1:]:
            try:
                next_fd = os.open(
                    component, flags | nofollow, dir_fd=descriptor
                )
            except FileNotFoundError:
                os.mkdir(component, 0o755, dir_fd=descriptor)
                os.fsync(descriptor)
                next_fd = os.open(
                    component, flags | nofollow, dir_fd=descriptor
                )
            os.close(descriptor)
            descriptor = next_fd
    except Exception:
        os.close(descriptor)
        raise
    os.close(descriptor)


def read_pinned_regular_file(
    path: Path,
    *,
    reject_hardlink: bool = True,
) -> tuple[bytes, os.stat_result]:
    canonical = safe_absolute_path(os.fspath(path), "file path")
    try:
        parent_fd = _open_directory_fd(canonical.parent)
    except OSError as error:
        raise PathContractError(f"secure file parent failed for {canonical}: {error}") from error
    parent_before = os.fstat(parent_fd)
    descriptor: int | None = None
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(canonical.name, os.O_RDONLY | nofollow, dir_fd=parent_fd)
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise PathContractError(f"not a regular file: {canonical}")
        if reject_hardlink and before.st_nlink != 1:
            raise PathContractError(f"hard-link alias rejected: {canonical}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        metadata_before = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        metadata_after = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if metadata_before != metadata_after:
            raise PathContractError(f"file changed during pinned read: {canonical}")
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        replay_parent_fd = _open_directory_fd(canonical.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            lexical = os.stat(
                canonical.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
        finally:
            os.close(replay_parent_fd)
        if (
            (entry.st_dev, entry.st_ino) != (before.st_dev, before.st_ino)
            or (lexical.st_dev, lexical.st_ino) != (before.st_dev, before.st_ino)
            or (replay_parent.st_dev, replay_parent.st_ino)
            != (parent_before.st_dev, parent_before.st_ino)
        ):
            raise PathContractError(f"path changed during pinned read: {canonical}")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise PathContractError(f"short pinned read: {canonical}")
        return raw, before
    except OSError as error:
        raise PathContractError(f"secure file open failed for {canonical}: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def file_binding(path: Path, *, reject_hardlink: bool = True) -> dict[str, Any]:
    raw, info = read_pinned_regular_file(path, reject_hardlink=reject_hardlink)
    return {
        "sha256": sha256_bytes(raw),
        "size_bytes": info.st_size,
    }


def nearest_existing_parent(path: Path) -> Path:
    current = path.absolute()
    while not current.exists():
        if current.parent == current:
            raise PathContractError(f"no existing parent: {path}")
        current = current.parent
    reject_symlink_components(current, allow_missing_leaf=False)
    return current


def ensure_same_filesystem(left: Path, right: Path) -> None:
    if nearest_existing_parent(left).stat().st_dev != nearest_existing_parent(right).stat().st_dev:
        raise PathContractError("authoritative and operational roots differ in filesystem")


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.absolute().relative_to(parent.absolute())
        return True
    except ValueError:
        return False


def ensure_mock_output_allowed(output: Path) -> None:
    reject_symlink_components(output, allow_missing_leaf=True)
    if is_within(output, CANONICAL_RESULT) or is_within(output, CANONICAL_OPERATIONAL):
        raise PathContractError("mock output cannot use canonical production namespace")
    if output.absolute() in {CANONICAL_RESULT.absolute(), CANONICAL_OPERATIONAL.absolute()}:
        raise PathContractError("mock output cannot equal canonical production namespace")


def fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def rename_directory_noreplace(source: Path, destination: Path) -> None:
    """Atomically publish one directory without replacing any destination."""

    source = safe_absolute_path(os.fspath(source), "rename source")
    destination = safe_absolute_path(os.fspath(destination), "rename destination")
    source_parent_fd = _open_directory_fd(source.parent)
    destination_parent_fd = _open_directory_fd(destination.parent)
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        renameat2 = getattr(libc, "renameat2", None)
        if renameat2 is None:
            raise PathContractError("renameat2(RENAME_NOREPLACE) is unavailable")
        renameat2.argtypes = [
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]
        renameat2.restype = ctypes.c_int
        result = renameat2(
            source_parent_fd,
            os.fsencode(source.name),
            destination_parent_fd,
            os.fsencode(destination.name),
            1,
        )
        if result != 0:
            error_number = ctypes.get_errno()
            if error_number == errno.EEXIST:
                raise CorruptGeneration(
                    f"no-replace destination collision: {destination}"
                )
            raise PathContractError(
                f"renameat2 no-replace failed: {os.strerror(error_number)}"
            )
        try:
            os.stat(source.name, dir_fd=source_parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise CorruptGeneration("no-replace rename left source entry present")
        target_info = os.stat(
            destination.name,
            dir_fd=destination_parent_fd,
            follow_symlinks=False,
        )
        if not stat.S_ISDIR(target_info.st_mode):
            raise CorruptGeneration("no-replace rename published non-directory")
        os.fsync(source_parent_fd)
        if destination_parent_fd != source_parent_fd:
            os.fsync(destination_parent_fd)
    finally:
        os.close(source_parent_fd)
        os.close(destination_parent_fd)


def exclusive_write_bytes(path: Path, payload: bytes) -> None:
    canonical = safe_absolute_path(os.fspath(path), "exclusive output path")
    try:
        ensure_real_directory_tree(canonical.parent)
        parent_fd = _open_directory_fd(canonical.parent)
    except OSError as error:
        raise PathContractError(f"exclusive output parent failed: {error}") from error
    parent_before = os.fstat(parent_fd)
    descriptor: int | None = None
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(
            canonical.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | nofollow,
            0o644,
            dir_fd=parent_fd,
        )
        view = memoryview(payload)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short exclusive write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        if (
            not stat.S_ISREG(info.st_mode)
            or info.st_nlink != 1
            or info.st_size != len(payload)
        ):
            raise PathContractError("exclusive output publication mismatch")
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        if (entry.st_dev, entry.st_ino) != (info.st_dev, info.st_ino):
            raise PathContractError("exclusive output directory entry mismatch")
        replay_parent_fd = _open_directory_fd(canonical.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            replay_entry = os.stat(
                canonical.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
            if (
                (replay_parent.st_dev, replay_parent.st_ino)
                != (parent_before.st_dev, parent_before.st_ino)
                or (replay_entry.st_dev, replay_entry.st_ino)
                != (info.st_dev, info.st_ino)
            ):
                raise PathContractError("exclusive output lexical replay mismatch")
            os.fsync(replay_parent_fd)
        finally:
            os.close(replay_parent_fd)
        os.fsync(parent_fd)
    except FileExistsError:
        raise
    except OSError as error:
        raise PathContractError(f"exclusive output publication failed: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def exclusive_write_json(path: Path, payload: Any) -> None:
    exclusive_write_bytes(path, canonical_json_bytes(payload))


def load_plan(path: Path = PLAN) -> dict[str, Mapping[str, Any]]:
    payload = strict_json_load(path, reject_hardlink=False)
    if type(payload) is not dict or type(payload.get("slabs")) is not list:
        raise StrictJSONError("L1 plan must contain a slabs array")
    if payload.get("slab_count") != 51 or type(payload.get("slab_count")) is not int:
        raise StrictJSONError("L1 plan slab count mismatch")
    records: dict[str, Mapping[str, Any]] = {}
    for record in payload["slabs"]:
        if type(record) is not dict or type(record.get("slab_id")) is not str:
            raise StrictJSONError("invalid plan slab record")
        slab_id = record["slab_id"]
        if slab_id in records:
            raise StrictJSONError(f"duplicate plan slab: {slab_id}")
        for key in ("epsilon_lower", "epsilon_upper", "center", "root_radii"):
            if key not in record:
                raise StrictJSONError(f"plan slab missing {key}: {slab_id}")
        records[slab_id] = record
    if tuple(records) != SLAB_IDS:
        raise StrictJSONError("L1 plan slab order or identity mismatch")
    return records


def source_bindings() -> dict[str, str]:
    paths = (SCRIPT, PLAN, PROTOCOL, SCHEDULER_CONTRACT, CHECKER_CONTRACT, RELEASE_CONTRACT)
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths}


def candidate_limits() -> dict[str, Any]:
    return {
        "branch": {
            "record_bytes": 4 * 1024 * 1024,
            "stderr_bytes": 1 * 1024 * 1024,
            "stdout_bytes": 16 * 1024 * 1024,
            "timeout_seconds": 600,
            "total_cell_bytes": 32 * 1024 * 1024,
            "workers": 6,
        },
        "global_scientific_budget": None,
        "max_inflight_per_component_cell": 1,
        "static": {
            "max_depth_per_tree": 24,
            "max_nodes_per_cell": 1_000_000,
            "max_nodes_per_tree": 250_000,
            "timeout_seconds": 1800,
            "total_cell_bytes": 512 * 1024 * 1024,
            "workers": 8,
        },
    }


def build_mock_binding(output: Path, operational: Path) -> dict[str, Any]:
    ensure_mock_output_allowed(output)
    ensure_mock_output_allowed(operational)
    ensure_same_filesystem(output, operational)
    load_plan()
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "RUN_CONFIG",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "production_authorized": False,
        "scientific_licensing_enabled": False,
        "matrix": matrix_payload(),
        "matrix_id": canonical_matrix_id(),
        "scheduler_policy": SCHEDULER_POLICY,
        "limits": candidate_limits(),
        "paths": {
            "authoritative_root": str(output.absolute()),
            "operational_root": str(operational.absolute()),
        },
        "main_freeze": {"path": None, "sha256": None},
        "machine_freeze": {"path": None, "sha256": None},
        "prefreeze_review": {"path": None, "sha256": None, "accepted": False},
        "source_bindings": source_bindings(),
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


RUN_CONFIG_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "production_authorized",
    "scientific_licensing_enabled",
    "matrix",
    "matrix_id",
    "scheduler_policy",
    "limits",
    "paths",
    "main_freeze",
    "machine_freeze",
    "prefreeze_review",
    "source_bindings",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def validate_mock_binding(binding: Any) -> dict[str, Any]:
    exact_keys(binding, RUN_CONFIG_KEYS, "mock run binding")
    exact_int(binding["schema_version"], "schema_version", minimum=1)
    if binding["schema_version"] != SCHEMA_VERSION:
        raise StrictJSONError("schema version mismatch")
    if binding["protocol_id"] != PROTOCOL_ID or binding["artifact_role"] != "RUN_CONFIG":
        raise StrictJSONError("run binding identity mismatch")
    if (
        binding["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or binding["authority"] != "PRODUCER_ONLY"
    ):
        raise StrictJSONError("mock artifact status mismatch")
    for key, expected in {
        "mock_only": True,
        "production_authorized": False,
        "scientific_licensing_enabled": False,
    }.items():
        if binding[key] is not expected:
            raise StrictJSONError(f"mock binding {key} mismatch")
    if binding["matrix_id"] != canonical_matrix_id():
        raise StrictJSONError("matrix id mismatch")
    if not exact_json_equal(binding["matrix"], matrix_payload()):
        raise StrictJSONError("matrix payload mismatch")
    if binding["scheduler_policy"] != SCHEDULER_POLICY:
        raise StrictJSONError("scheduler policy mismatch")
    if not exact_json_equal(binding["limits"], candidate_limits()):
        raise StrictJSONError("candidate resource limits mismatch")
    if not exact_json_equal(
        binding["main_freeze"], {"path": None, "sha256": None}
    ):
        raise StrictJSONError("mock main-freeze binding mismatch")
    if not exact_json_equal(
        binding["machine_freeze"], {"path": None, "sha256": None}
    ):
        raise StrictJSONError("mock machine-freeze binding mismatch")
    if not exact_json_equal(
        binding["prefreeze_review"],
        {"path": None, "sha256": None, "accepted": False},
    ):
        raise StrictJSONError("mock review binding mismatch")
    if not exact_json_equal(binding["source_bindings"], source_bindings()):
        raise StrictJSONError("source bindings mismatch")
    if binding["claim_boundary"] != MOCK_CLAIM_BOUNDARY:
        raise StrictJSONError("mock claim boundary mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if binding[key] is not None:
            raise StrictJSONError(f"unauthorized mock status: {key}")
    exact_keys(
        binding["paths"],
        {"authoritative_root", "operational_root"},
        "mock run paths",
    )
    output = safe_absolute_path(
        binding["paths"]["authoritative_root"], "authoritative root"
    )
    operational = safe_absolute_path(
        binding["paths"]["operational_root"], "operational root"
    )
    if operational != operational_root_for(output):
        raise PathContractError("operational root is not the canonical sibling")
    ensure_mock_output_allowed(output)
    ensure_mock_output_allowed(operational)
    ensure_same_filesystem(output, operational)
    return dict(binding)


def run_config_path(output: Path) -> Path:
    return output / "run_config.json"


def ensure_run_config(
    output: Path, binding: Mapping[str, Any], *, resume: bool
) -> tuple[dict[str, Any], str]:
    validate_mock_binding(binding)
    target = run_config_path(output)
    if target.exists():
        stored, raw, _ = strict_json_image(target, require_canonical=True)
        validate_mock_binding(stored)
        if not exact_json_equal(stored, binding):
            raise RunBindingMismatch("stored run config differs from expected binding")
        if not resume:
            raise RunBindingMismatch("run config already exists; explicit resume required")
        return dict(stored), sha256_bytes(raw)
    if resume:
        raise RunBindingMismatch("resume requested but run config is missing")
    output.mkdir(parents=True, exist_ok=False)
    exclusive_write_json(target, binding)
    stored, raw, _ = strict_json_image(target, require_canonical=True)
    if not exact_json_equal(stored, binding):
        raise RunBindingMismatch("new run config publication mismatch")
    return dict(stored), sha256_bytes(raw)


def validate_prefreeze_review(path: Path) -> None:
    require_regular_file(path)
    declarations = [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip().startswith("Verdict:")
    ]
    if declarations != [PREFREEZE_ACCEPT_LINE]:
        raise ProductionAuthorityError("pre-freeze review is not the sole exact ACCEPT verdict")


def validate_production_authority() -> None:
    # Fail before touching any output path.  A future implementation will
    # tighten the complete 53-role freeze schema; this framework cannot turn a
    # nominal file into dispatch authority.
    for path, label in (
        (MACHINE_FREEZE, "machine freeze"),
        (MAIN_FREEZE, "main freeze"),
        (PREFREEZE_REVIEW, "pre-freeze review"),
    ):
        if not path.exists():
            raise ProductionAuthorityError(f"{label} is absent; production rejected")
        require_regular_file(path)
    main = strict_json_load(MAIN_FREEZE)
    if type(main) is not dict or main.get("status") != "FROZEN_FOR_PRODUCTION":
        raise ProductionAuthorityError("main freeze status is not accepted")
    if main.get("scientific_licensing_enabled") is not True:
        raise ProductionAuthorityError("main freeze does not enable licensing")
    validate_prefreeze_review(PREFREEZE_REVIEW)
    raise ProductionAuthorityError(
        "production dispatcher is intentionally unimplemented in this framework"
    )


def operational_root_for(output: Path) -> Path:
    return output.with_name(output.name + ".operational")


def staging_basename(
    cell: CellKey,
    run_config_sha256: str,
    attempt: int = 0,
) -> str:
    if (
        type(run_config_sha256) is not str
        or HEX_SHA256.fullmatch(run_config_sha256) is None
    ):
        raise PathContractError("run-config digest is not an exact SHA-256")
    exact_int(attempt, "staging attempt", minimum=0)
    name = f".{cell.slab_id}.tmp-{run_config_sha256[:16]}-{attempt}"
    if STAGING_BASENAME.fullmatch(name) is None:
        raise PathContractError(f"invalid staging basename: {name}")
    return name


def staging_path(
    operational: Path,
    cell: CellKey,
    run_config_sha256: str,
    attempt: int = 0,
) -> Path:
    return (
        operational
        / "staging"
        / "static"
        / str(cell.precision_bits)
        / staging_basename(cell, run_config_sha256, attempt)
    )


def validate_static_staging_namespace(
    operational: Path, run_config_sha256: str
) -> dict[tuple[int, str], Path]:
    root = operational / "staging" / "static"
    if not path_lexists(root):
        return {}
    require_directory(root)
    precision_names = {path.name for path in root.iterdir()}
    if not precision_names <= {str(bits) for bits in PRECISIONS}:
        raise CorruptGeneration(
            f"static staging precision namespace mismatch: {precision_names}"
        )
    expected_prefix = run_config_sha256[:16]
    active: dict[tuple[int, str], Path] = {}
    for precision_root in root.iterdir():
        require_directory(precision_root)
        precision_bits = int(precision_root.name)
        for stage in precision_root.iterdir():
            match = STAGING_BASENAME.fullmatch(stage.name)
            if match is None:
                raise CorruptGeneration(f"invalid static staging name: {stage.name}")
            slab_id, generation_prefix, _attempt = match.groups()
            if generation_prefix != expected_prefix:
                raise CorruptGeneration(
                    f"foreign-generation static staging name: {stage.name}"
                )
            key = (precision_bits, slab_id)
            if key in active:
                raise CorruptGeneration(
                    f"multiple active static staging owners for {slab_id}"
                )
            active[key] = stage
            require_directory(stage)
    return active


def static_cell_path(output: Path, cell: CellKey) -> Path:
    return output / "static" / "cells" / str(cell.precision_bits) / cell.slab_id


def static_manifest_path(output: Path, cell: CellKey) -> Path:
    return output / "static" / "cell_manifests" / str(cell.precision_bits) / f"{cell.slab_id}.json"


def static_aggregate_summary_path(output: Path) -> Path:
    return output / "static" / "aggregate_summary.json"


def static_aggregate_manifest_path(output: Path) -> Path:
    return output / "static" / "aggregate_manifest.json"


def mock_proof(cell: CellKey, matrix_id: str, run_config_sha256: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_PROOF",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "cell": cell.payload(),
        "matrix_id": matrix_id,
        "run_config_sha256": run_config_sha256,
        "synthetic_trees": ["ANGLE", "SECTION_LOW", "SECTION_HIGH", "SECTION_WINDOW"],
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def mock_record(
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
    proof_sha256: str,
    proof_size_bytes: int,
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_CELL_RECORD",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "cell": cell.payload(),
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "returncode": 0,
        "evaluator_payload": {
            "path": "proof.json",
            "sha256": proof_sha256,
            "size_bytes": proof_size_bytes,
        },
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_mock_cell_directory(
    directory: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    require_directory(directory)
    actual = {path.name for path in directory.iterdir()}
    if actual != {"proof.json", "record.json"}:
        raise CorruptGeneration(f"mock cell file set mismatch: {actual}")
    for child in directory.iterdir():
        require_regular_file(child)
    proof, proof_raw, proof_info = strict_json_image(
        directory / "proof.json", require_canonical=True
    )
    record, record_raw, record_info = strict_json_image(
        directory / "record.json", require_canonical=True
    )
    expected_proof = mock_proof(cell, matrix_id, run_config_sha256)
    if not exact_json_equal(proof, expected_proof):
        raise CorruptGeneration("mock proof content mismatch")
    expected_record = mock_record(
        cell,
        matrix_id,
        run_config_sha256,
        sha256_bytes(proof_raw),
        proof_info.st_size,
    )
    if not exact_json_equal(record, expected_record):
        raise CorruptGeneration("mock record content mismatch")
    return proof, record, {
        "proof.json": {
            "sha256": sha256_bytes(proof_raw),
            "size_bytes": proof_info.st_size,
        },
        "record.json": {
            "sha256": sha256_bytes(record_raw),
            "size_bytes": record_info.st_size,
        },
    }


def derive_static_manifest(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    directory = static_cell_path(output, cell)
    _, _, bindings = validate_mock_cell_directory(
        directory, cell, matrix_id, run_config_sha256
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_CELL_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "cell": cell.payload(),
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "files": bindings,
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_static_manifest(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    return validate_static_manifest_image(
        output, cell, matrix_id, run_config_sha256
    )[0]


def validate_static_manifest_image(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    target = static_manifest_path(output, cell)
    stored, raw, info = strict_json_image(target, require_canonical=True)
    expected = derive_static_manifest(output, cell, matrix_id, run_config_sha256)
    if not exact_json_equal(stored, expected):
        raise CorruptGeneration("static cell manifest mismatch")
    return dict(stored), {
        "sha256": sha256_bytes(raw),
        "size_bytes": info.st_size,
    }


def validate_static_cell_namespace(output: Path) -> None:
    """Require exactly 102 cell directories with exactly two files each."""

    root = output / "static" / "cells"
    require_directory(root)
    precision_names = {path.name for path in root.iterdir()}
    if precision_names != {str(bits) for bits in PRECISIONS}:
        raise CorruptGeneration(
            f"static cell precision namespace mismatch: {precision_names}"
        )
    for bits in PRECISIONS:
        precision_root = root / str(bits)
        require_directory(precision_root)
        expected = set(SLAB_IDS)
        actual = {path.name for path in precision_root.iterdir()}
        if actual != expected:
            raise CorruptGeneration(
                f"static cell namespace mismatch for {bits}: {actual}"
            )
        for slab in SLAB_IDS:
            directory = precision_root / slab
            require_directory(directory)
            names = {path.name for path in directory.iterdir()}
            if names != {"proof.json", "record.json"}:
                raise CorruptGeneration(
                    f"static cell file namespace mismatch for {bits}:{slab}: {names}"
                )
            for path in directory.iterdir():
                require_regular_file(path)


def validate_static_manifest_namespace(output: Path) -> None:
    """Require the full 102-manifest namespace and no aliases or extras."""

    root = output / "static" / "cell_manifests"
    require_directory(root)
    precision_names = {path.name for path in root.iterdir()}
    if precision_names != {str(bits) for bits in PRECISIONS}:
        raise CorruptGeneration(
            f"static manifest precision namespace mismatch: {precision_names}"
        )
    for bits in PRECISIONS:
        precision_root = root / str(bits)
        require_directory(precision_root)
        expected = {f"{slab}.json" for slab in SLAB_IDS}
        actual = {path.name for path in precision_root.iterdir()}
        if actual != expected:
            raise CorruptGeneration(
                f"static manifest namespace mismatch for {bits}: {actual}"
            )
        for path in precision_root.iterdir():
            require_regular_file(path)


def validate_mock_authoritative_namespace(output: Path) -> None:
    """Reject every unexpected authoritative object, including hidden paths."""

    require_directory(output)
    output_names = {path.name for path in output.iterdir()}
    if output_names != {"run_config.json", "static"}:
        raise CorruptGeneration(
            f"mock authoritative root namespace mismatch: {output_names}"
        )
    require_regular_file(run_config_path(output))
    static_root = output / "static"
    require_directory(static_root)
    aggregate_names = {
        path.name
        for path in (
            static_aggregate_summary_path(output),
            static_aggregate_manifest_path(output),
        )
        if path.exists()
    }
    if aggregate_names == {"aggregate_manifest.json"}:
        raise CorruptGeneration("static aggregate manifest exists without summary")
    permitted_aggregate_states = (
        set(),
        {"aggregate_summary.json"},
        {"aggregate_summary.json", "aggregate_manifest.json"},
    )
    if aggregate_names not in permitted_aggregate_states:
        raise CorruptGeneration("invalid static aggregate namespace state")
    expected = {"cells", "cell_manifests"} | aggregate_names
    actual = {path.name for path in static_root.iterdir()}
    if actual != expected:
        raise CorruptGeneration(f"static authoritative namespace mismatch: {actual}")
    validate_static_cell_namespace(output)
    validate_static_manifest_namespace(output)


def ordered_static_manifest_entries(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
) -> list[dict[str, Any]]:
    active_staging = validate_static_staging_namespace(
        operational_root_for(output), run_config_sha256
    )
    if active_staging:
        labels = sorted(f"{bits}:{slab}" for bits, slab in active_staging)
        raise CorruptGeneration(
            "static aggregate cannot coexist with live staging owners: "
            + ",".join(labels)
        )
    validate_mock_authoritative_namespace(output)
    entries: list[dict[str, Any]] = []
    for cell in exact_matrix():
        path = static_manifest_path(output, cell)
        _, binding = validate_static_manifest_image(
            output, cell, matrix_id, run_config_sha256
        )
        entries.append(
            {
                "cell": cell.payload(),
                "path": path.relative_to(output).as_posix(),
                "sha256": binding["sha256"],
                "size_bytes": binding["size_bytes"],
            }
        )
    return entries


def build_static_aggregate_summary(
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
) -> dict[str, Any]:
    if len(entries) != 102:
        raise CorruptGeneration("static aggregate requires exactly 102 cell manifests")
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_AGGREGATE_SUMMARY",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "matrix": matrix_payload(),
        "cell_count": 102,
        "ordered_cell_manifest_root": sha256_bytes(canonical_json_bytes(entries)),
        "status_counts": {"STATIC_CELL_CERTIFIED": 102},
        "scheduler_classification_counts": {"COMMITTED_EVALUATOR_RESULT": 102},
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def build_static_aggregate_manifest(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
    summary: Mapping[str, Any],
) -> dict[str, Any]:
    summary_bytes = canonical_json_bytes(summary)
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_AGGREGATE_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "ordered_cell_manifest_root": sha256_bytes(canonical_json_bytes(entries)),
        "cell_manifests": entries,
        "summary": {
            "path": static_aggregate_summary_path(output).relative_to(output).as_posix(),
            "sha256": sha256_bytes(summary_bytes),
            "size_bytes": len(summary_bytes),
        },
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_static_mock_aggregate(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    summary_path = static_aggregate_summary_path(output)
    manifest_path = static_aggregate_manifest_path(output)
    if not summary_path.exists() or not manifest_path.exists():
        raise CorruptGeneration("static aggregate summary/manifest pair is incomplete")
    entries = ordered_static_manifest_entries(output, matrix_id, run_config_sha256)
    expected_summary = build_static_aggregate_summary(
        matrix_id, run_config_sha256, entries
    )
    stored_summary = strict_json_load(summary_path, require_canonical=True)
    if not exact_json_equal(stored_summary, expected_summary):
        raise CorruptGeneration("static aggregate summary mismatch")
    expected_manifest = build_static_aggregate_manifest(
        output, matrix_id, run_config_sha256, entries, expected_summary
    )
    stored_manifest = strict_json_load(manifest_path, require_canonical=True)
    if not exact_json_equal(stored_manifest, expected_manifest):
        raise CorruptGeneration("static aggregate manifest mismatch")
    return dict(stored_summary), dict(stored_manifest)


def finalize_static_mock_aggregate(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[str, dict[str, Any], dict[str, Any]]:
    """Publish the mock aggregate with the manifest as the commit marker."""

    summary_path = static_aggregate_summary_path(output)
    manifest_path = static_aggregate_manifest_path(output)
    if manifest_path.exists():
        summary, manifest = validate_static_mock_aggregate(
            output, matrix_id, run_config_sha256
        )
        return "RESUMED_COMMITTED", summary, manifest

    entries = ordered_static_manifest_entries(output, matrix_id, run_config_sha256)
    summary = build_static_aggregate_summary(matrix_id, run_config_sha256, entries)
    manifest = build_static_aggregate_manifest(
        output, matrix_id, run_config_sha256, entries, summary
    )
    if summary_path.exists():
        stored_summary = strict_json_load(summary_path, require_canonical=True)
        if not exact_json_equal(stored_summary, summary):
            raise CorruptGeneration("manifest-less aggregate summary mismatch")
        state = "RECOVERED_MANIFEST"
    else:
        exclusive_write_json(summary_path, summary)
        state = "COMMITTED"
    exclusive_write_json(manifest_path, manifest)
    checked_summary, checked_manifest = validate_static_mock_aggregate(
        output, matrix_id, run_config_sha256
    )
    return state, checked_summary, checked_manifest


def publish_manifestless_cell(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    target = static_manifest_path(output, cell)
    if target.exists():
        return validate_static_manifest(output, cell, matrix_id, run_config_sha256)
    manifest = derive_static_manifest(output, cell, matrix_id, run_config_sha256)
    exclusive_write_json(target, manifest)
    return manifest


def write_mock_stage(stage: Path, cell: CellKey, matrix_id: str, run_config_sha256: str) -> None:
    stage.parent.mkdir(parents=True, exist_ok=True)
    if stage.exists():
        raise CorruptGeneration(f"live staging path already exists: {stage}")
    stage.mkdir(mode=0o755)
    fsync_directory(stage.parent)
    proof_payload = canonical_json_bytes(mock_proof(cell, matrix_id, run_config_sha256))
    exclusive_write_bytes(stage / "proof.json", proof_payload)
    record_payload = canonical_json_bytes(
        mock_record(
            cell,
            matrix_id,
            run_config_sha256,
            sha256_bytes(proof_payload),
            len(proof_payload),
        )
    )
    exclusive_write_bytes(stage / "record.json", record_payload)
    fsync_directory(stage)


def commit_mock_static_cell(
    output: Path,
    operational: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
    *,
    fail_after_cell_rename: bool = False,
) -> tuple[str, dict[str, Any]]:
    ensure_same_filesystem(output, operational)
    target = static_cell_path(output, cell)
    manifest_target = static_manifest_path(output, cell)
    stage = staging_path(operational, cell, run_config_sha256)
    active_staging = validate_static_staging_namespace(
        operational, run_config_sha256
    )
    existing_stage = active_staging.get((cell.precision_bits, cell.slab_id))
    if existing_stage is not None and existing_stage != stage:
        raise CorruptGeneration(
            f"noncanonical active staging attempt for {cell.label}: {existing_stage.name}"
        )

    if manifest_target.exists():
        return "RESUMED_COMMITTED", validate_static_manifest(
            output, cell, matrix_id, run_config_sha256
        )
    if target.exists():
        return "RECOVERED_MANIFEST", publish_manifestless_cell(
            output, cell, matrix_id, run_config_sha256
        )
    if stage.exists():
        validate_mock_cell_directory(stage, cell, matrix_id, run_config_sha256)
    else:
        write_mock_stage(stage, cell, matrix_id, run_config_sha256)

    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise CorruptGeneration(f"canonical cell already exists: {target}")
    rename_directory_noreplace(stage, target)
    fsync_directory(stage.parent)
    fsync_directory(target.parent)
    if fail_after_cell_rename:
        raise SyntheticCrash("synthetic crash after canonical cell rename")
    return "COMMITTED", publish_manifestless_cell(
        output, cell, matrix_id, run_config_sha256
    )


def quarantine_paths(output: Path, index: int) -> tuple[Path, Path]:
    operational = operational_root_for(output)
    return (
        output.with_name(f"{output.name}.quarantine-{index:04d}"),
        operational.with_name(f"{operational.name}.quarantine-{index:04d}"),
    )


def quarantine_journal_path(output: Path) -> Path:
    return output.with_name(f"{output.name}.quarantine-transaction.json")


QUARANTINE_FAILURE_POINTS = {
    "AFTER_JOURNAL",
    "AFTER_AUTHORITATIVE_RENAME",
    "AFTER_OPERATIONAL_RENAME",
    "AFTER_RECORD",
}


QUARANTINE_INTENT_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "transaction_index",
    "reason",
    "source_authoritative_root",
    "source_operational_root",
    "destination_authoritative_root",
    "destination_operational_root",
    "operational_present",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def path_lexists(path: Path) -> bool:
    return os.path.lexists(path)


def build_quarantine_intent(
    output: Path,
    reason: str,
    index: int,
    operational_present: bool,
) -> dict[str, Any]:
    output = output.absolute()
    operational = operational_root_for(output)
    q_output, q_operational = quarantine_paths(output, index)
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "QUARANTINE_TRANSACTION_INTENT",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "transaction_index": index,
        "reason": reason,
        "source_authoritative_root": str(output),
        "source_operational_root": str(operational),
        "destination_authoritative_root": str(q_output),
        "destination_operational_root": str(q_operational),
        "operational_present": operational_present,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_quarantine_intent(output: Path, payload: Any) -> dict[str, Any]:
    exact_keys(payload, QUARANTINE_INTENT_KEYS, "quarantine transaction intent")
    if payload["schema_version"] != SCHEMA_VERSION or type(payload["schema_version"]) is not int:
        raise CorruptGeneration("quarantine intent schema mismatch")
    expected_scalars = {
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "QUARANTINE_TRANSACTION_INTENT",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    for key, expected in expected_scalars.items():
        if type(payload[key]) is not type(expected) or payload[key] != expected:
            raise CorruptGeneration(f"quarantine intent {key} mismatch")
    index = exact_int(
        payload["transaction_index"], "quarantine transaction index", minimum=1
    )
    if index >= 10_000:
        raise CorruptGeneration("quarantine transaction index exceeds namespace")
    if type(payload["reason"]) is not str or not payload["reason"]:
        raise CorruptGeneration("quarantine intent reason is invalid")
    if type(payload["operational_present"]) is not bool:
        raise CorruptGeneration("quarantine operational_present must be Boolean")

    output = output.absolute()
    operational = operational_root_for(output)
    q_output, q_operational = quarantine_paths(output, index)
    expected_paths = {
        "source_authoritative_root": output,
        "source_operational_root": operational,
        "destination_authoritative_root": q_output,
        "destination_operational_root": q_operational,
    }
    for key, expected in expected_paths.items():
        actual = safe_absolute_path(payload[key], key.replace("_", " "))
        if actual != expected:
            raise CorruptGeneration(f"quarantine intent {key} is not canonical")
    return dict(payload)


def quarantine_record_payload(
    intent: Mapping[str, Any], journal_sha256: str
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "QUARANTINE_RECORD",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "transaction_index": intent["transaction_index"],
        "transaction_journal_sha256": journal_sha256,
        "reason": intent["reason"],
        "source_authoritative_root": intent["source_authoritative_root"],
        "source_operational_root": intent["source_operational_root"],
        "destination_authoritative_root": intent["destination_authoritative_root"],
        "destination_operational_root": intent["destination_operational_root"],
        "operational_present": intent["operational_present"],
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def _quarantine_move_or_validate(source: Path, destination: Path, label: str) -> bool:
    source_exists = path_lexists(source)
    destination_exists = path_lexists(destination)
    if source_exists and destination_exists:
        raise CorruptGeneration(f"split quarantine has both {label} source and destination")
    if not source_exists and not destination_exists:
        raise CorruptGeneration(f"quarantine lost both {label} source and destination")
    if destination_exists:
        require_directory(destination)
        return False
    require_directory(source)
    rename_directory_noreplace(source, destination)
    fsync_directory(source.parent)
    if destination.parent != source.parent:
        fsync_directory(destination.parent)
    return True


def _complete_quarantine_transaction(
    output: Path,
    *,
    fail_at: str | None = None,
) -> tuple[Path, Path | None]:
    output = output.absolute()
    journal = quarantine_journal_path(output)
    intent = validate_quarantine_intent(
        output, strict_json_load(journal, require_canonical=True)
    )
    journal_digest = sha256(journal)
    source_output = Path(intent["source_authoritative_root"])
    source_operational = Path(intent["source_operational_root"])
    q_output = Path(intent["destination_authoritative_root"])
    q_operational = Path(intent["destination_operational_root"])

    moved_output = _quarantine_move_or_validate(
        source_output, q_output, "authoritative"
    )
    if moved_output and fail_at == "AFTER_AUTHORITATIVE_RENAME":
        raise SyntheticQuarantineCrash("crash after authoritative quarantine rename")

    moved_operational: Path | None = None
    if intent["operational_present"]:
        _quarantine_move_or_validate(
            source_operational, q_operational, "operational"
        )
        moved_operational = q_operational
    elif path_lexists(source_operational) or path_lexists(q_operational):
        raise CorruptGeneration(
            "operational quarantine path exists contrary to frozen transaction intent"
        )
    if fail_at == "AFTER_OPERATIONAL_RENAME":
        raise SyntheticQuarantineCrash("crash after operational quarantine rename")

    record_path = q_output / "QUARANTINE_RECORD.json"
    expected_record = quarantine_record_payload(intent, journal_digest)
    if path_lexists(record_path):
        stored_record = strict_json_load(record_path, require_canonical=True)
        if not exact_json_equal(stored_record, expected_record):
            raise CorruptGeneration("quarantine record mismatch")
    else:
        exclusive_write_json(record_path, expected_record)
    if fail_at == "AFTER_RECORD":
        raise SyntheticQuarantineCrash("crash after quarantine record commit")

    journal.unlink()
    fsync_directory(journal.parent)
    return q_output, moved_operational


def recover_quarantine_transaction(output: Path) -> tuple[Path, Path | None] | None:
    output = output.absolute()
    journal = quarantine_journal_path(output)
    if not path_lexists(journal):
        return None
    return _complete_quarantine_transaction(output)


def quarantine_incompatible_generation(
    output: Path,
    reason: str,
    *,
    fail_at: str | None = None,
) -> tuple[Path, Path | None]:
    output = output.absolute()
    journal = quarantine_journal_path(output)
    if fail_at is not None and fail_at not in QUARANTINE_FAILURE_POINTS:
        raise SchedulerContractError(f"unknown quarantine failure point: {fail_at}")
    if path_lexists(journal):
        intent = validate_quarantine_intent(
            output, strict_json_load(journal, require_canonical=True)
        )
        if intent["reason"] != reason:
            raise CorruptGeneration("active quarantine intent has a different reason")
        return _complete_quarantine_transaction(output, fail_at=fail_at)
    if not path_lexists(output):
        raise PathContractError("authoritative generation does not exist")
    if type(reason) is not str or not reason:
        raise SchedulerContractError("quarantine reason must be nonempty")
    operational = operational_root_for(output)
    require_directory(output)
    operational_present = path_lexists(operational)
    if operational_present:
        require_directory(operational)
        ensure_same_filesystem(output, operational)
    ensure_same_filesystem(output, journal)
    for index in range(1, 10_000):
        q_output, q_operational = quarantine_paths(output, index)
        if not path_lexists(q_output) and not path_lexists(q_operational):
            break
    else:
        raise SchedulerContractError("quarantine namespace exhausted")
    intent = build_quarantine_intent(output, reason, index, operational_present)
    exclusive_write_json(journal, intent)
    if fail_at == "AFTER_JOURNAL":
        raise SyntheticQuarantineCrash("crash after quarantine intent commit")
    return _complete_quarantine_transaction(output, fail_at=fail_at)


def run_mock_static(output: Path, cell_limit: int, *, resume: bool) -> dict[str, Any]:
    ensure_mock_output_allowed(output)
    operational = operational_root_for(output)
    ensure_mock_output_allowed(operational)
    recovered_quarantine = recover_quarantine_transaction(output)
    if recovered_quarantine is not None:
        raise RunBindingMismatch(
            "pending quarantine transaction was completed; the quarantined "
            "generation cannot be resumed"
        )
    exact_int(cell_limit, "mock cell limit", minimum=0)
    if cell_limit > 102:
        raise SchedulerContractError("mock cell limit cannot exceed 102")
    binding = build_mock_binding(output, operational)
    _, config_hash = ensure_run_config(output, binding, resume=resume)
    operational.mkdir(parents=True, exist_ok=True)
    ensure_same_filesystem(output, operational)
    states: list[dict[str, Any]] = []
    for cell in exact_matrix()[:cell_limit]:
        state, manifest = commit_mock_static_cell(
            output,
            operational,
            cell,
            binding["matrix_id"],
            config_hash,
        )
        states.append({"cell": cell.payload(), "state": state, "manifest": manifest})
    aggregate: dict[str, Any] | None = None
    if cell_limit == 102:
        aggregate_state, summary, manifest = finalize_static_mock_aggregate(
            output,
            binding["matrix_id"],
            config_hash,
        )
        aggregate = {
            "state": aggregate_state,
            "ordered_cell_manifest_root": summary["ordered_cell_manifest_root"],
            "summary_sha256": manifest["summary"]["sha256"],
            "manifest_sha256": sha256(static_aggregate_manifest_path(output)),
        }
    return {
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "mock_only": True,
        "production_authorized": False,
        "matrix_id": binding["matrix_id"],
        "requested_cells": cell_limit,
        "completed_cells": len(states),
        "states": states,
        "aggregate_finalized": aggregate is not None,
        "aggregate": aggregate,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=CANONICAL_RESULT)
    parser.add_argument("--initialize-only", action="store_true")
    parser.add_argument("--mock-only", action="store_true")
    parser.add_argument("--mock-static-cells", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--production", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.mock_only:
            if arguments.production:
                raise SchedulerContractError("mock and production modes are exclusive")
            if not arguments.initialize_only and arguments.mock_static_cells == 0:
                raise SchedulerContractError(
                    "mock-only requires --initialize-only or positive --mock-static-cells"
                )
            result = run_mock_static(
                arguments.output.absolute(),
                arguments.mock_static_cells,
                resume=arguments.resume,
            )
            print(json.dumps(result, sort_keys=True))
            return 0

        # Both initialize and production modes require real authority.  This
        # happens before any output directory is inspected or created.
        validate_production_authority()
        raise ProductionAuthorityError("unreachable production authority path")
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
