#!/usr/bin/env python3
"""Independent L3-A1 composite-chain checker.

The currently enabled path is deliberately mock-only and non-licensing.  It
replays two complete 102-cell component control chains without importing a
producer, scheduler, component checker, or S0 helper.  Formal production
authority remains fail-closed until a reviewed main freeze exists.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import math
import os
import re
import secrets
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PROTOCOL_ID = "R401-VAL-L3-A1"
SCHEMA_VERSION = 1
MOCK_CHECKER_STATUS = "PASS_MOCK_INDEPENDENT_REPLAY"
MOCK_POSTCHECK_STATUS = "PASS_MOCK_WRITE_ONCE_POSTCHECK"
MOCK_CLAIM_BOUNDARY = (
    "mock 102-static plus 102-branch archive replay only; no scientific "
    "licensing, local theorem, global routing, trace-formula, Hilbert-Polya, "
    "zeta-zero, or RH promotion"
)
FORMAL_CLAIM_BOUNDARY = (
    "complete-period local-tube candidate uniqueness modulo time translation "
    "and distinguished-branch tube membership only; no global routing, "
    "trace-formula, Hilbert-Polya, zeta-zero, or RH promotion"
)
CHECKER_CONTRACT = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
RELEASE_CONTRACT = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
STATIC_CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
BRANCH_CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_branch_independent.py"
SCHEDULER = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
BRANCH_RUNTIME = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
MOCK_BRANCH_EVALUATOR = ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"
SCHEDULER_CONTRACT = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
SLAB_IDS = tuple(f"S{index:03d}" for index in range(51))
PRECISIONS = (128, 256)
SCHEDULER_POLICY = "deterministic_component_barrier_batches_v1"
SCHEDULER_MOCK_CLAIM_BOUNDARY = (
    "synthetic static/branch scheduler transaction only; no Arb/CAPD "
    "scientific evaluation, no component or local theorem, no global "
    "routing, trace, Hilbert-Polya, zeta-zero, or RH claim"
)
STATIC_CHECKER_CLAIM_BOUNDARY = (
    "deterministic 102-cell static archive and hash-DAG engineering replay "
    "only; synthetic proofs receive no static component, local theorem, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
STATIC_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the non-licensing 102-cell static mock "
    "checker chain only; no scientific component or programme authority"
)
BRANCH_CHECKER_CLAIM_BOUNDARY = (
    "mock-only all-slab branch archive replay for transaction, transcript, "
    "tube-implication, aggregate, and cross-precision engineering; no "
    "component, local theorem, global orbit, trace-formula, Hilbert--Polya, "
    "zeta-zero, or RH authority"
)
BRANCH_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once replay of the mock branch checker and aggregate chain only; "
    "no scientific component, theorem, trace, Hilbert--Polya, zeta, or RH authority"
)
BRANCH_CELL_CLAIM_BOUNDARY = (
    "accepted-branch complete-period tube cell only; no arbitrary-candidate "
    "tube routing, global uniqueness, trace, Hilbert--Polya, zeta, or RH claim"
)
BRANCH_CELL_BUDGETS = {
    "pipe_close_grace_ms": 1_000,
    "record_bytes": 4 * 1024 * 1024,
    "stderr_bytes": 1 * 1024 * 1024,
    "stdout_bytes": 16 * 1024 * 1024,
    "term_grace_ms": 2_000,
    "timeout_ms": 600_000,
    "total_cell_bytes": 32 * 1024 * 1024,
}
L1_CHAIN = (
    ROOT / "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    ROOT / "results/r401_val_l1_branch/summary.json",
    ROOT / "results/r401_val_l1_branch/manifest.json",
    ROOT / "results/r401_val_l1_branch/independent_checker.json",
    ROOT / "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
)
RESERVED_NESTED_AUTHORITY_KEYS = {
    "authority", "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status", "release_status", "checker_status",
    "postcheck_status", "promotion_authorized", "scientific_licensing_enabled",
}
_ACTIVE_SNAPSHOTS: dict[Path, tuple[bytes, tuple[int, int, int, int, int]]] | None = None


class CompositeCheckError(RuntimeError):
    """Closed failure for malformed or unauthorised composite evidence."""


class StrictJSONError(CompositeCheckError):
    pass


class PathContractError(CompositeCheckError):
    pass


def _require_plain_json(
    value: Any,
    context: str = "$",
    ancestors: set[int] | None = None,
) -> None:
    """Reject Python aliases that ``json.dumps`` would silently coerce."""

    if value is None or type(value) in (str, bool, int):
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise StrictJSONError(f"nonfinite JSON number at {context}")
        return
    if type(value) not in (dict, list):
        raise StrictJSONError(
            f"non-plain JSON value at {context}: {type(value).__name__}"
        )
    active = ancestors if ancestors is not None else set()
    identity = id(value)
    if identity in active:
        raise StrictJSONError(f"cyclic JSON container at {context}")
    active.add(identity)
    try:
        if type(value) is dict:
            for key, item in value.items():
                if type(key) is not str:
                    raise StrictJSONError(
                        f"non-string JSON object key at {context}: "
                        f"{type(key).__name__}"
                    )
                _require_plain_json(item, f"{context}.{key}", active)
        else:
            for index, item in enumerate(value):
                _require_plain_json(item, f"{context}[{index}]", active)
    finally:
        active.remove(identity)


def canonical_json_bytes(payload: Any) -> bytes:
    _require_plain_json(payload)
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
        raise StrictJSONError(f"noncanonical JSON payload: {error}") from error


def branch_transaction_json_bytes(payload: Any) -> bytes:
    """Canonical representation frozen by the branch transaction runtime."""
    _require_plain_json(payload)
    try:
        return (
            json.dumps(
                payload,
                indent=2,
                sort_keys=True,
                ensure_ascii=False,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise StrictJSONError(f"noncanonical branch JSON payload: {error}") from error


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJSONError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise StrictJSONError(f"nonfinite JSON number: {value}")
    return parsed


def _reject_constant(value: str) -> None:
    raise StrictJSONError(f"nonfinite JSON constant: {value}")


def strict_json_loads(raw: bytes, *, require_canonical: bool = True) -> Any:
    try:
        text = raw.decode("utf-8")
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_float=_finite_float,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise StrictJSONError(f"invalid strict JSON: {error}") from error
    if require_canonical and canonical_json_bytes(value) != raw:
        raise StrictJSONError("JSON bytes are not canonical")
    return value


def exact_json_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            exact_json_equal(left[key], right[key]) for key in left
        )
    if type(left) is list:
        return len(left) == len(right) and all(
            exact_json_equal(a, b) for a, b in zip(left, right, strict=True)
        )
    return left == right


def exact_keys(payload: Any, expected: set[str], context: str) -> Mapping[str, Any]:
    if type(payload) is not dict or set(payload) != expected:
        actual = set(payload) if type(payload) is dict else type(payload).__name__
        raise StrictJSONError(f"{context} key set mismatch: {actual}")
    return payload


def exact_int(value: Any, context: str, *, expected: int | None = None) -> int:
    if type(value) is not int or value < 0:
        raise StrictJSONError(f"{context} must be an exact nonnegative integer")
    if expected is not None and value != expected:
        raise StrictJSONError(f"{context} must equal {expected}")
    return value


def require_sha256(value: Any, context: str) -> str:
    if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
        raise StrictJSONError(f"{context} must be a lowercase SHA-256")
    return value


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe_relative_path(value: Any) -> PurePosixPath:
    if type(value) is not str or not value:
        raise PathContractError("relative path must be a nonempty string")
    if value.startswith("/") or "\\" in value or "//" in value or value.endswith("/"):
        raise PathContractError(f"unsafe relative path: {value}")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise PathContractError(f"unsafe relative path: {value}")
    if pure.as_posix() != value:
        raise PathContractError(f"noncanonical relative path: {value}")
    return pure


def _absolute_lexical(path: Path) -> Path:
    text = os.fspath(path)
    if not text.startswith("/") or text.startswith("//") or "//" in text[1:]:
        raise PathContractError(f"noncanonical absolute path: {text}")
    if "\\" in text or text.endswith("/"):
        raise PathContractError(f"noncanonical absolute path: {text}")
    pure = PurePosixPath(text)
    if any(part in {"", ".", ".."} for part in pure.parts[1:]) or pure.as_posix() != text:
        raise PathContractError(f"unsafe absolute path: {text}")
    return Path(text)


def _open_directory(path: Path) -> int:
    canonical = _absolute_lexical(path)
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for part in canonical.parts[1:]:
            next_descriptor = os.open(part, flags | nofollow, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def _fingerprint(info: os.stat_result) -> tuple[int, int, int, int, int]:
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def _read_snapshot_uncached(
    path: Path, *, reject_hardlink: bool = True
) -> tuple[bytes, os.stat_result]:
    canonical = _absolute_lexical(path)
    parent_fd = _open_directory(canonical.parent)
    parent_info = os.fstat(parent_fd)
    descriptor: int | None = None
    try:
        descriptor = os.open(
            canonical.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
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
        fingerprint = lambda item: (
            item.st_dev,
            item.st_ino,
            item.st_size,
            item.st_mtime_ns,
            item.st_ctime_ns,
        )
        if fingerprint(before) != fingerprint(after):
            raise PathContractError(f"file changed during read: {canonical}")
        replay_parent_fd = _open_directory(canonical.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            entry = os.stat(canonical.name, dir_fd=replay_parent_fd, follow_symlinks=False)
        finally:
            os.close(replay_parent_fd)
        if (replay_parent.st_dev, replay_parent.st_ino) != (
            parent_info.st_dev,
            parent_info.st_ino,
        ) or (entry.st_dev, entry.st_ino) != (before.st_dev, before.st_ino):
            raise PathContractError(f"path changed during read: {canonical}")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise PathContractError(f"short read: {canonical}")
        return raw, before
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def read_snapshot(path: Path, *, reject_hardlink: bool = True) -> tuple[bytes, os.stat_result]:
    canonical = _absolute_lexical(path)
    if _ACTIVE_SNAPSHOTS is not None and canonical in _ACTIVE_SNAPSHOTS:
        raw, expected = _ACTIVE_SNAPSHOTS[canonical]
        current_raw, current_info = _read_snapshot_uncached(
            canonical, reject_hardlink=reject_hardlink
        )
        if current_raw != raw or _fingerprint(current_info) != expected:
            raise PathContractError(f"input changed during composite replay: {canonical}")
        return raw, current_info
    raw, info = _read_snapshot_uncached(canonical, reject_hardlink=reject_hardlink)
    if _ACTIVE_SNAPSHOTS is not None:
        _ACTIVE_SNAPSHOTS[canonical] = (raw, _fingerprint(info))
    return raw, info


@contextmanager
def capture_input_generation():
    global _ACTIVE_SNAPSHOTS
    if _ACTIVE_SNAPSHOTS is not None:
        yield
        return
    captured: dict[Path, tuple[bytes, tuple[int, int, int, int, int]]] = {}
    _ACTIVE_SNAPSHOTS = captured
    try:
        yield
        for path, (expected_raw, expected_fingerprint) in captured.items():
            raw, info = _read_snapshot_uncached(path)
            if raw != expected_raw or _fingerprint(info) != expected_fingerprint:
                raise PathContractError(f"input changed during composite replay: {path}")
    finally:
        _ACTIVE_SNAPSHOTS = None


def strict_json_image(path: Path) -> tuple[Mapping[str, Any], bytes, os.stat_result]:
    raw, info = read_snapshot(path)
    value = strict_json_loads(raw)
    if type(value) is not dict:
        raise StrictJSONError(f"top-level object required: {path}")
    return value, raw, info


def write_once(path: Path, raw: bytes) -> None:
    canonical = _absolute_lexical(path)
    if not canonical.parent.exists():
        raise PathContractError("write-once parent must already exist")
    parent_fd = _open_directory(canonical.parent)
    descriptor: int | None = None
    temporary_name = f".{canonical.name}.tmp-{secrets.token_hex(16)}"
    temporary_unlinked = False
    try:
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o644,
            dir_fd=parent_fd,
        )
        view = memoryview(raw)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise PathContractError("temporary checker is not a single-link regular file")
        os.link(
            f"/proc/self/fd/{descriptor}", canonical.name,
            dst_dir_fd=parent_fd, follow_symlinks=True,
        )
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        if (entry.st_dev, entry.st_ino) != (info.st_dev, info.st_ino):
            raise PathContractError("published checker inode mismatch")
        os.unlink(temporary_name, dir_fd=parent_fd)
        temporary_unlinked = True
        published_fd = os.open(
            canonical.name, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
        try:
            published = b""
            while True:
                chunk = os.read(published_fd, 1024 * 1024)
                if not chunk:
                    break
                published += chunk
            published_info = os.fstat(published_fd)
            if published != raw or published_info.st_nlink != 1:
                raise PathContractError("published checker byte/link mismatch")
        finally:
            os.close(published_fd)
        os.fsync(parent_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if not temporary_unlinked:
            try:
                os.unlink(temporary_name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        os.close(parent_fd)


def matrix_payload() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": slab}
        for bits in PRECISIONS
        for slab in SLAB_IDS
    ]


def matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(matrix_payload()))


RUN_CONFIG_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "production_authorized",
    "scientific_licensing_enabled", "matrix", "matrix_id",
    "scheduler_policy", "limits", "paths", "main_freeze", "machine_freeze",
    "prefreeze_review", "source_bindings", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}

COMPONENT_CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_aggregate_summary_sha256",
    "component_aggregate_manifest_sha256", "replay_counts",
    "cross_precision", "diagnostics", "failures", "source_bindings",
    "claim_boundary", "milestone_status", "theorem_status", "final_status",
}

POSTCHECK_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "postcheck_status", "passed", "checker_path", "checker_sha256",
    "main_freeze_sha256", "run_config_sha256", "bound_artifacts",
    "replay_counts", "failures", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}

COMPOSITE_SUMMARY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "matrix", "cell_count_per_component",
    "component_chains", "archive_generation_sha256",
    "scientific_licensing_enabled", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}

COMPOSITE_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "component_chains", "archive_generation_sha256",
    "summary", "scientific_licensing_enabled", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}

STATIC_SUMMARY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "matrix", "cell_count",
    "ordered_cell_manifest_root", "status_counts",
    "scheduler_classification_counts", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}

STATIC_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "ordered_cell_manifest_root", "cell_manifests",
    "summary", "scientific_licensing_enabled", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}

BRANCH_SUMMARY_KEYS = STATIC_SUMMARY_KEYS | {"mock_evaluator"}
BRANCH_MANIFEST_KEYS = STATIC_MANIFEST_KEYS | {"mock_evaluator"}

STATIC_CELL_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "cell", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "scheduler_classification", "evaluator_status",
    "files", "scientific_licensing_enabled", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}

BRANCH_CELL_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority", "budgets",
    "cell_identity", "claim_boundary", "component_status", "files",
    "final_status", "freeze_sha256", "matrix_id", "milestone_status",
    "run_config_sha256", "scientific_licensing_enabled",
    "task_binding_sha256", "theorem_status",
}


def _null_statuses(payload: Mapping[str, Any], context: str) -> None:
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload.get(key) is not None:
            raise CompositeCheckError(f"unauthorised {context} status: {key}")


def reject_nested_authority(value: Any, context: str) -> None:
    if type(value) is dict:
        for key, child in value.items():
            if key in RESERVED_NESTED_AUTHORITY_KEYS:
                raise CompositeCheckError(
                    f"unexpected nested authority field in {context}: {key}"
                )
            reject_nested_authority(child, context)
    elif type(value) is list:
        for child in value:
            reject_nested_authority(child, context)


def validate_json_payload_authority(
    raw: bytes,
    *,
    context: str,
    branch_transaction: bool,
    expected_claim_boundary: str,
) -> Mapping[str, Any]:
    payload = strict_json_loads(raw, require_canonical=not branch_transaction)
    if branch_transaction and branch_transaction_json_bytes(payload) != raw:
        raise StrictJSONError(f"{context} is not branch-runtime canonical JSON")
    if type(payload) is not dict:
        raise StrictJSONError(f"{context} must be a JSON object")
    permitted_root_authority = {
        "authority", "claim_boundary", "component_status", "milestone_status",
        "theorem_status", "final_status", "scientific_licensing_enabled",
    }
    unexpected = (set(payload) & RESERVED_NESTED_AUTHORITY_KEYS) - permitted_root_authority
    if unexpected:
        raise CompositeCheckError(f"unexpected {context} authority fields: {sorted(unexpected)}")
    if "authority" in payload and payload["authority"] != "PRODUCER_ONLY":
        raise CompositeCheckError(f"{context} authority mismatch")
    if "claim_boundary" in payload and payload["claim_boundary"] != expected_claim_boundary:
        raise CompositeCheckError(f"{context} claim boundary mismatch")
    if (
        "scientific_licensing_enabled" in payload
        and payload["scientific_licensing_enabled"] is not False
    ):
        raise CompositeCheckError(f"{context} licenses science")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if key in payload and payload[key] is not None:
            raise CompositeCheckError(f"unauthorised {context} status: {key}")
    for key, value in payload.items():
        if key not in permitted_root_authority:
            reject_nested_authority(value, context)
    return payload


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


def expected_scheduler_sources() -> dict[str, str]:
    paths = (
        SCHEDULER,
        PLAN,
        BRANCH_RUNTIME,
        MOCK_BRANCH_EVALUATOR,
        PROTOCOL,
        SCHEDULER_CONTRACT,
        CHECKER_CONTRACT,
        RELEASE_CONTRACT,
    )
    return {
        path.relative_to(ROOT).as_posix(): sha256_bytes(read_snapshot(path)[0])
        for path in paths
    }


def expected_l1_bindings() -> dict[str, str]:
    paths = (*L1_CHAIN, PLAN)
    return {
        path.relative_to(ROOT).as_posix(): sha256_bytes(read_snapshot(path)[0])
        for path in paths
    }


def expected_component_semantics(
    name: str,
    ordered_root: str,
    mock_evaluator: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if name == "static":
        return {
            "replay_counts": {
                "aggregate_objects": 2,
                "cell_directories": 102,
                "cell_manifests": 102,
                "hash_bound_payloads": 306,
                "proof_objects": 102,
                "record_objects": 102,
            },
            "cross_precision": {
                "all_agree": True,
                "mock_only": True,
                "scientific_domain_replay_performed": False,
                "slab_pairs": 51,
                "status_pairs_agree": 51,
            },
            "diagnostics": {
                "artifact_status": "MOCK_ONLY_NON_LICENSING",
                "mock_only": True,
                "ordered_cell_manifest_root": ordered_root,
                "production_dispatch_observed": False,
                "scientific_proof_replay_performed": False,
            },
            "source_bindings": {
                "checker_sha256": sha256_bytes(read_snapshot(STATIC_CHECKER_SOURCE)[0]),
                "producer_source_bindings": expected_scheduler_sources(),
            },
            "claim_boundary": STATIC_CHECKER_CLAIM_BOUNDARY,
            "postcheck_claim_boundary": STATIC_POSTCHECK_CLAIM_BOUNDARY,
        }
    if mock_evaluator is None:
        raise CompositeCheckError("branch mock evaluator binding is missing")
    return {
        "replay_counts": {
            "accepted_l1_chain_objects": 6,
            "aggregate_objects": 2,
            "cell_directories": 102,
            "cell_manifests": 102,
            "cell_records": 102,
            "hash_bound_payloads": 408,
            "phase_records": 6528,
            "raw_stderr_objects": 102,
            "raw_transcripts": 102,
            "tube_implication_checks": 6528,
        },
        "cross_precision": {
            "all_agree": True,
            "input_domains_agree": 51,
            "mock_only": True,
            "scientific_domain_replay_performed": False,
            "slab_pairs": 51,
            "status_pairs_agree": 51,
        },
        "diagnostics": {
            "archive_transcripts_are_synthetic": True,
            "artifact_status": "MOCK_ONLY_NON_LICENSING",
            "maximum_rslow_sq_upper": "0/1",
            "minimum_margin_sq_lower": "1/625",
            "mock_only": True,
            "ordered_cell_manifest_root": ordered_root,
            "production_dispatch_observed": False,
            "scientific_flow_replay_performed": False,
            "synthetic_tube_implication_replay_performed": True,
        },
        "source_bindings": {
            "accepted_l1_chain_bindings": expected_l1_bindings(),
            "checker_sha256": sha256_bytes(read_snapshot(BRANCH_CHECKER_SOURCE)[0]),
            "mock_evaluator": dict(mock_evaluator),
            "producer_source_bindings": expected_scheduler_sources(),
        },
        "claim_boundary": BRANCH_CHECKER_CLAIM_BOUNDARY,
        "postcheck_claim_boundary": BRANCH_POSTCHECK_CLAIM_BOUNDARY,
    }


def validate_mock_run_config(result_dir: Path) -> tuple[Mapping[str, Any], bytes]:
    payload, raw, _ = strict_json_image(result_dir / "run_config.json")
    exact_keys(payload, RUN_CONFIG_KEYS, "run config")
    exact_int(payload["schema_version"], "run config schema", expected=1)
    if payload["protocol_id"] != PROTOCOL_ID or payload["artifact_role"] != "RUN_CONFIG":
        raise CompositeCheckError("run config identity mismatch")
    if payload["artifact_status"] != "MOCK_ONLY_NON_LICENSING" or payload["authority"] != "PRODUCER_ONLY":
        raise CompositeCheckError("run config authority mismatch")
    if payload["mock_only"] is not True or payload["production_authorized"] is not False:
        raise CompositeCheckError("only an explicit mock run config is enabled")
    if payload["scientific_licensing_enabled"] is not False:
        raise CompositeCheckError("mock run config cannot license science")
    if payload["scheduler_policy"] != SCHEDULER_POLICY:
        raise CompositeCheckError("mock scheduler policy mismatch")
    if not exact_json_equal(payload["limits"], candidate_limits()):
        raise CompositeCheckError("mock scheduler limits mismatch")
    if payload["matrix_id"] != matrix_id() or not exact_json_equal(payload["matrix"], matrix_payload()):
        raise CompositeCheckError("run config matrix mismatch")
    if payload["main_freeze"] != {"path": None, "sha256": None}:
        raise CompositeCheckError("mock main-freeze edge mismatch")
    if payload["machine_freeze"] != {"path": None, "sha256": None}:
        raise CompositeCheckError("mock machine-freeze edge mismatch")
    if payload["prefreeze_review"] != {
        "path": None, "sha256": None, "accepted": False
    }:
        raise CompositeCheckError("mock pre-freeze review edge mismatch")
    exact_keys(
        payload["paths"],
        {"authoritative_root", "operational_root"},
        "run config paths",
    )
    expected_authoritative = str(result_dir)
    expected_operational = str(result_dir) + ".operational"
    if payload["paths"] != {
        "authoritative_root": expected_authoritative,
        "operational_root": expected_operational,
    }:
        raise CompositeCheckError("mock archive paths mismatch")
    if not exact_json_equal(payload["source_bindings"], expected_scheduler_sources()):
        raise CompositeCheckError("mock scheduler source bindings mismatch")
    if payload["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY:
        raise CompositeCheckError("mock run-config claim boundary mismatch")
    reject_nested_authority(payload["source_bindings"], "run config source bindings")
    _null_statuses(payload, "run config")
    return payload, raw


def validate_root_namespace(
    result_dir: Path, *, allow_checker: bool, allow_postcheck: bool = False
) -> None:
    expected = {
        "run_config.json", "static", "branch",
        "independent_static_checker.json", "STATIC_POSTCHECK_STATUS.json",
        "independent_branch_checker.json", "BRANCH_POSTCHECK_STATUS.json",
        "composite_summary.json", "composite_manifest.json",
    }
    if allow_checker:
        expected.add("independent_checker.json")
    if allow_postcheck:
        if not allow_checker:
            raise PathContractError("postcheck cannot exist without checker")
        expected.add("POSTCHECK_STATUS.json")
    actual = {entry.name for entry in result_dir.iterdir()}
    if actual != expected:
        raise PathContractError(
            f"composite authoritative namespace mismatch: {sorted(actual)}"
        )
    for name in expected - {"static", "branch"}:
        raw_path = result_dir / name
        _, info = read_snapshot(raw_path)
        if info.st_nlink != 1:
            raise PathContractError(f"authoritative hard-link alias: {name}")
    for name in ("static", "branch"):
        directory = result_dir / name
        descriptor = _open_directory(directory)
        os.close(descriptor)
        expected_component = {
            "cells", "cell_manifests", "aggregate_summary.json",
            "aggregate_manifest.json",
        }
        actual_component = {entry.name for entry in directory.iterdir()}
        if actual_component != expected_component:
            raise PathContractError(
                f"{name} component namespace mismatch: {sorted(actual_component)}"
            )
        cells_root = directory / "cells"
        manifests_root = directory / "cell_manifests"
        for root in (cells_root, manifests_root):
            root_fd = _open_directory(root)
            os.close(root_fd)
            if {entry.name for entry in root.iterdir()} != {"128", "256"}:
                raise PathContractError(f"{name} precision namespace mismatch")
        expected_cell_files = (
            {"proof.json", "record.json"}
            if name == "static"
            else {"record.json", "stderr.txt", "stdout.txt"}
        )
        for bits in PRECISIONS:
            cell_precision = cells_root / str(bits)
            manifest_precision = manifests_root / str(bits)
            if {entry.name for entry in cell_precision.iterdir()} != set(SLAB_IDS):
                raise PathContractError(f"{name} cell slab namespace mismatch")
            if {entry.name for entry in manifest_precision.iterdir()} != {
                f"{slab}.json" for slab in SLAB_IDS
            }:
                raise PathContractError(f"{name} manifest slab namespace mismatch")
            for slab in SLAB_IDS:
                cell_directory = cell_precision / slab
                cell_fd = _open_directory(cell_directory)
                os.close(cell_fd)
                if {entry.name for entry in cell_directory.iterdir()} != expected_cell_files:
                    raise PathContractError(
                        f"{name} cell file namespace mismatch: {bits}:{slab}"
                    )
                for filename in expected_cell_files:
                    read_snapshot(cell_directory / filename)
                read_snapshot(manifest_precision / f"{slab}.json")


def _component_paths(result_dir: Path, name: str) -> dict[str, Path]:
    checker_name = f"independent_{name}_checker.json"
    postcheck_name = f"{name.upper()}_POSTCHECK_STATUS.json"
    return {
        "aggregate_summary": result_dir / name / "aggregate_summary.json",
        "aggregate_manifest": result_dir / name / "aggregate_manifest.json",
        "checker": result_dir / checker_name,
        "postcheck": result_dir / postcheck_name,
    }


def validate_cell_manifest(
    result_dir: Path,
    name: str,
    cell: Mapping[str, Any],
    run_config_sha256: str,
    raw: bytes,
) -> Mapping[str, Any]:
    manifest = strict_json_loads(raw, require_canonical=(name == "static"))
    if type(manifest) is not dict:
        raise StrictJSONError(f"{name} cell manifest must be an object")
    if name == "branch" and branch_transaction_json_bytes(manifest) != raw:
        raise StrictJSONError("branch cell manifest bytes are not runtime-canonical")
    exact_keys(
        manifest,
        STATIC_CELL_MANIFEST_KEYS if name == "static" else BRANCH_CELL_MANIFEST_KEYS,
        f"{name} cell manifest",
    )
    exact_int(manifest["schema_version"], f"{name} cell manifest schema", expected=1)
    if manifest["protocol_id"] != PROTOCOL_ID:
        raise CompositeCheckError(f"{name} cell protocol mismatch")
    if manifest["matrix_id"] != matrix_id() or manifest["run_config_sha256"] != run_config_sha256:
        raise CompositeCheckError(f"{name} cell generation binding mismatch")
    if manifest["authority"] != "PRODUCER_ONLY" or manifest["scientific_licensing_enabled"] is not False:
        raise CompositeCheckError(f"{name} cell authority mismatch")
    _null_statuses(manifest, f"{name} cell manifest")
    cell_root = (
        result_dir / name / "cells" / str(cell["precision_bits"]) / cell["slab_id"]
    )
    if name == "static":
        if (
            manifest["artifact_role"] != "MOCK_STATIC_CELL_MANIFEST"
            or manifest["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
            or manifest["mock_only"] is not True
            or manifest["main_freeze_sha256"] is not None
            or manifest["scheduler_classification"] != "COMMITTED_EVALUATOR_RESULT"
            or manifest["evaluator_status"] != "STATIC_CELL_CERTIFIED"
            or manifest["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
            or not exact_json_equal(manifest["cell"], cell)
        ):
            raise CompositeCheckError("static cell manifest semantics mismatch")
        files = exact_keys(
            manifest["files"], {"proof.json", "record.json"},
            "static cell files",
        )
        for filename in ("proof.json", "record.json"):
            binding = exact_keys(
                files[filename], {"sha256", "size_bytes"},
                f"static {filename} binding",
            )
            payload, info = read_snapshot(cell_root / filename)
            if require_sha256(binding["sha256"], "static payload hash") != sha256_bytes(payload):
                raise CompositeCheckError("static cell payload hash mismatch")
            exact_int(binding["size_bytes"], "static payload size", expected=info.st_size)
            validate_json_payload_authority(
                payload,
                context=f"static {filename}",
                branch_transaction=False,
                expected_claim_boundary=SCHEDULER_MOCK_CLAIM_BOUNDARY,
            )
    else:
        if (
            manifest["artifact_role"] != "BRANCH_CELL_MANIFEST"
            or manifest["claim_boundary"] != BRANCH_CELL_CLAIM_BOUNDARY
            or not exact_json_equal(manifest["cell_identity"], cell)
            or not exact_json_equal(manifest["budgets"], BRANCH_CELL_BUDGETS)
        ):
            raise CompositeCheckError("branch cell manifest semantics mismatch")
        require_sha256(manifest["freeze_sha256"], "branch cell freeze hash")
        require_sha256(manifest["task_binding_sha256"], "branch task binding hash")
        expected_files = {
            (
                PurePosixPath("branch") / "cells" / str(cell["precision_bits"])
                / cell["slab_id"] / filename
            ).as_posix()
            for filename in ("record.json", "stderr.txt", "stdout.txt")
        }
        files = exact_keys(manifest["files"], expected_files, "branch cell files")
        for relative, bound_hash in files.items():
            payload, _ = read_snapshot(result_dir / Path(safe_relative_path(relative)))
            if require_sha256(bound_hash, "branch payload hash") != sha256_bytes(payload):
                raise CompositeCheckError("branch cell payload hash mismatch")
            if relative.endswith("/record.json"):
                validate_json_payload_authority(
                    payload,
                    context="branch record.json",
                    branch_transaction=True,
                    expected_claim_boundary=BRANCH_CELL_CLAIM_BOUNDARY,
                )
    return manifest


def validate_component_chain(
    result_dir: Path,
    name: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], Mapping[str, Any], Mapping[str, Any]]:
    paths = _component_paths(result_dir, name)
    images: dict[str, tuple[Mapping[str, Any], bytes, os.stat_result]] = {
        role: strict_json_image(path) for role, path in paths.items()
    }
    summary, summary_raw, _ = images["aggregate_summary"]
    manifest, manifest_raw, _ = images["aggregate_manifest"]
    checker, checker_raw, _ = images["checker"]
    postcheck, _, _ = images["postcheck"]
    exact_keys(
        summary,
        STATIC_SUMMARY_KEYS if name == "static" else BRANCH_SUMMARY_KEYS,
        f"{name} aggregate summary",
    )
    exact_keys(
        manifest,
        STATIC_MANIFEST_KEYS if name == "static" else BRANCH_MANIFEST_KEYS,
        f"{name} aggregate manifest",
    )
    exact_int(summary["schema_version"], f"{name} summary schema", expected=1)
    exact_int(manifest["schema_version"], f"{name} manifest schema", expected=1)
    if (
        summary["protocol_id"] != PROTOCOL_ID
        or manifest["protocol_id"] != PROTOCOL_ID
        or summary["artifact_role"] != f"MOCK_{name.upper()}_AGGREGATE_SUMMARY"
        or manifest["artifact_role"] != f"MOCK_{name.upper()}_AGGREGATE_MANIFEST"
        or summary["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or manifest["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or summary["authority"] != "PRODUCER_ONLY"
        or manifest["authority"] != "PRODUCER_ONLY"
        or summary["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
        or manifest["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
    ):
        raise CompositeCheckError(f"{name} aggregate identity mismatch")
    if summary["main_freeze_sha256"] is not None or manifest["main_freeze_sha256"] is not None:
        raise CompositeCheckError(f"{name} mock aggregate has a freeze hash")
    if not exact_json_equal(summary["matrix"], matrix_payload()):
        raise CompositeCheckError(f"{name} aggregate matrix payload mismatch")
    expected_status = f"{name.upper()}_CELL_CERTIFIED"
    if not exact_json_equal(summary["status_counts"], {expected_status: 102}):
        raise CompositeCheckError(f"{name} aggregate status counts mismatch")
    if not exact_json_equal(
        summary["scheduler_classification_counts"],
        {"COMMITTED_EVALUATOR_RESULT": 102},
    ):
        raise CompositeCheckError(f"{name} scheduler classification counts mismatch")
    if name == "branch":
        for payload, label in ((summary, "summary"), (manifest, "manifest")):
            mock_evaluator = exact_keys(
                payload["mock_evaluator"], {"path", "sha256"},
                f"branch {label} mock evaluator",
            )
            evaluator_path = _absolute_lexical(Path(mock_evaluator["path"]))
            if evaluator_path != MOCK_BRANCH_EVALUATOR:
                raise CompositeCheckError("branch mock evaluator path mismatch")
            require_sha256(mock_evaluator["sha256"], "branch mock evaluator hash")
            evaluator_raw, _ = read_snapshot(evaluator_path)
            if mock_evaluator["sha256"] != sha256_bytes(evaluator_raw):
                raise CompositeCheckError("branch mock evaluator hash mismatch")
        if not exact_json_equal(summary["mock_evaluator"], manifest["mock_evaluator"]):
            raise CompositeCheckError("branch mock evaluator bindings disagree")
    if summary.get("matrix_id") != matrix_id() or manifest.get("matrix_id") != matrix_id():
        raise CompositeCheckError(f"{name} aggregate matrix mismatch")
    for payload, label in ((summary, "summary"), (manifest, "manifest")):
        if payload.get("run_config_sha256") != run_config_sha256:
            raise CompositeCheckError(f"{name} {label} run-config mismatch")
        if payload.get("mock_only") is not True:
            raise CompositeCheckError(f"{name} {label} is not mock-only")
        if payload.get("scientific_licensing_enabled") is not False:
            raise CompositeCheckError(f"{name} {label} licenses science")
        _null_statuses(payload, f"{name} {label}")
    entries = manifest.get("cell_manifests")
    if type(entries) is not list or len(entries) != 102:
        raise CompositeCheckError(f"{name} aggregate must bind exactly 102 manifests")
    expected_cells = matrix_payload()
    for index, (entry, cell) in enumerate(zip(entries, expected_cells, strict=True)):
        exact_keys(entry, {"cell", "path", "sha256", "size_bytes"}, f"{name} entry {index}")
        if not exact_json_equal(entry["cell"], cell):
            raise CompositeCheckError(f"{name} manifest order mismatch at {index}")
        relative = safe_relative_path(entry["path"])
        expected = PurePosixPath(name) / "cell_manifests" / str(cell["precision_bits"]) / f"{cell['slab_id']}.json"
        if relative != expected:
            raise CompositeCheckError(f"{name} manifest path mismatch at {index}")
        raw, info = read_snapshot(result_dir / Path(relative))
        if require_sha256(entry["sha256"], f"{name} manifest hash") != sha256_bytes(raw):
            raise CompositeCheckError(f"{name} manifest hash mismatch at {index}")
        exact_int(entry["size_bytes"], f"{name} manifest size", expected=info.st_size)
        validate_cell_manifest(result_dir, name, cell, run_config_sha256, raw)
    root = sha256_bytes(canonical_json_bytes(entries))
    if summary.get("ordered_cell_manifest_root") != root or manifest.get("ordered_cell_manifest_root") != root:
        raise CompositeCheckError(f"{name} ordered manifest root mismatch")
    exact_int(summary.get("cell_count"), f"{name} cell count", expected=102)
    summary_binding = manifest.get("summary")
    exact_keys(summary_binding, {"path", "sha256", "size_bytes"}, f"{name} summary binding")
    if safe_relative_path(summary_binding["path"]) != PurePosixPath(name) / "aggregate_summary.json":
        raise CompositeCheckError(f"{name} summary path mismatch")
    if summary_binding["sha256"] != sha256_bytes(summary_raw):
        raise CompositeCheckError(f"{name} summary hash mismatch")
    exact_int(summary_binding["size_bytes"], f"{name} summary size", expected=len(summary_raw))

    exact_keys(checker, COMPONENT_CHECKER_KEYS, f"{name} checker")
    if checker["artifact_role"] != f"{name.upper()}_INDEPENDENT_CHECKER":
        raise CompositeCheckError(f"{name} checker role mismatch")
    exact_int(checker["schema_version"], f"{name} checker schema", expected=1)
    if checker["protocol_id"] != PROTOCOL_ID:
        raise CompositeCheckError(f"{name} checker protocol mismatch")
    if checker["authority"] != "INDEPENDENT_CHECKER":
        raise CompositeCheckError(f"{name} checker authority mismatch")
    if checker["checker_status"] != MOCK_CHECKER_STATUS or checker["passed"] is not True:
        raise CompositeCheckError(f"{name} checker did not pass mock replay")
    if checker["scientific_licensing_enabled"] is not False:
        raise CompositeCheckError(f"{name} checker licenses science")
    if checker["matrix_id"] != matrix_id() or checker["run_config_sha256"] != run_config_sha256:
        raise CompositeCheckError(f"{name} checker run binding mismatch")
    if checker["main_freeze_sha256"] is not None:
        raise CompositeCheckError(f"{name} mock checker has a freeze hash")
    if checker["component_aggregate_summary_sha256"] != sha256_bytes(summary_raw):
        raise CompositeCheckError(f"{name} checker summary hash mismatch")
    if checker["component_aggregate_manifest_sha256"] != sha256_bytes(manifest_raw):
        raise CompositeCheckError(f"{name} checker manifest hash mismatch")
    if checker["failures"] != []:
        raise CompositeCheckError(f"{name} checker contains failures")
    _null_statuses(checker, f"{name} checker")
    semantics = expected_component_semantics(
        name,
        root,
        summary.get("mock_evaluator") if name == "branch" else None,
    )
    for field in ("replay_counts", "cross_precision", "source_bindings"):
        if not exact_json_equal(checker[field], semantics[field]):
            raise CompositeCheckError(f"{name} checker {field} mismatch")
    if checker["claim_boundary"] != semantics["claim_boundary"]:
        raise CompositeCheckError(f"{name} checker claim boundary mismatch")
    if not exact_json_equal(checker["diagnostics"], semantics["diagnostics"]):
        raise CompositeCheckError(f"{name} checker diagnostics mismatch")
    for field in ("replay_counts", "cross_precision", "diagnostics", "source_bindings"):
        reject_nested_authority(checker[field], f"{name} checker {field}")

    exact_keys(postcheck, POSTCHECK_KEYS, f"{name} postcheck")
    if postcheck["artifact_role"] != f"{name.upper()}_POSTCHECK":
        raise CompositeCheckError(f"{name} postcheck role mismatch")
    exact_int(postcheck["schema_version"], f"{name} postcheck schema", expected=1)
    if postcheck["protocol_id"] != PROTOCOL_ID:
        raise CompositeCheckError(f"{name} postcheck protocol mismatch")
    if postcheck["authority"] != "POSTCHECK_ONLY":
        raise CompositeCheckError(f"{name} postcheck authority mismatch")
    if postcheck["postcheck_status"] != MOCK_POSTCHECK_STATUS or postcheck["passed"] is not True:
        raise CompositeCheckError(f"{name} postcheck did not pass mock replay")
    if postcheck["checker_sha256"] != sha256_bytes(checker_raw):
        raise CompositeCheckError(f"{name} postcheck checker hash mismatch")
    if postcheck["checker_path"] != f"independent_{name}_checker.json":
        raise CompositeCheckError(f"{name} postcheck checker path mismatch")
    if postcheck["run_config_sha256"] != run_config_sha256 or postcheck["main_freeze_sha256"] is not None:
        raise CompositeCheckError(f"{name} postcheck run binding mismatch")
    if postcheck["failures"] != []:
        raise CompositeCheckError(f"{name} postcheck contains failures")
    if not exact_json_equal(postcheck["replay_counts"], semantics["replay_counts"]):
        raise CompositeCheckError(f"{name} postcheck replay counts mismatch")
    if postcheck["claim_boundary"] != semantics["postcheck_claim_boundary"]:
        raise CompositeCheckError(f"{name} postcheck claim boundary mismatch")
    for field in ("bound_artifacts", "replay_counts"):
        reject_nested_authority(postcheck[field], f"{name} postcheck {field}")
    checker_source = STATIC_CHECKER_SOURCE if name == "static" else BRANCH_CHECKER_SOURCE
    checker_source_raw, _ = read_snapshot(checker_source)
    expected_bound = {
        "aggregate_manifest": {
            "path": f"{name}/aggregate_manifest.json",
            "sha256": sha256_bytes(manifest_raw),
        },
        "aggregate_summary": {
            "path": f"{name}/aggregate_summary.json",
            "sha256": sha256_bytes(summary_raw),
        },
        "checker_source": {
            "path": checker_source.relative_to(ROOT).as_posix(),
            "sha256": sha256_bytes(checker_source_raw),
        },
    }
    if not exact_json_equal(postcheck["bound_artifacts"], expected_bound):
        raise CompositeCheckError(f"{name} postcheck artifact bindings mismatch")
    _null_statuses(postcheck, f"{name} postcheck")
    bindings = {
        "aggregate_summary": {"path": paths["aggregate_summary"].relative_to(result_dir).as_posix(), "sha256": sha256_bytes(summary_raw)},
        "aggregate_manifest": {"path": paths["aggregate_manifest"].relative_to(result_dir).as_posix(), "sha256": sha256_bytes(manifest_raw)},
        "checker": {"path": paths["checker"].relative_to(result_dir).as_posix(), "sha256": sha256_bytes(checker_raw)},
        "postcheck": {"path": paths["postcheck"].relative_to(result_dir).as_posix(), "sha256": sha256_bytes(images["postcheck"][1])},
        "ordered_cell_manifest_root": root,
    }
    return bindings, checker, postcheck


def expected_composite_controls(
    result_dir: Path,
    run_config_sha256: str,
    static_chain: Mapping[str, Any],
    branch_chain: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    chains = {"static": static_chain, "branch": branch_chain}
    generation = sha256_bytes(canonical_json_bytes(chains))
    summary = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_COMPOSITE_SUMMARY",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "matrix": matrix_payload(),
        "cell_count_per_component": 102,
        "component_chains": chains,
        "archive_generation_sha256": generation,
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    summary_raw = canonical_json_bytes(summary)
    manifest = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_COMPOSITE_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "component_chains": chains,
        "archive_generation_sha256": generation,
        "summary": {"path": "composite_summary.json", "sha256": sha256_bytes(summary_raw), "size_bytes": len(summary_raw)},
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    return summary, manifest


def validate_composite_controls(
    result_dir: Path,
    run_config_sha256: str,
    static_chain: Mapping[str, Any],
    branch_chain: Mapping[str, Any],
) -> tuple[Mapping[str, Any], bytes, Mapping[str, Any], bytes]:
    summary, summary_raw, _ = strict_json_image(result_dir / "composite_summary.json")
    manifest, manifest_raw, _ = strict_json_image(result_dir / "composite_manifest.json")
    exact_keys(summary, COMPOSITE_SUMMARY_KEYS, "composite summary")
    exact_keys(manifest, COMPOSITE_MANIFEST_KEYS, "composite manifest")
    expected_summary, expected_manifest = expected_composite_controls(
        result_dir, run_config_sha256, static_chain, branch_chain
    )
    if not exact_json_equal(summary, expected_summary):
        raise CompositeCheckError("composite summary mismatch")
    if not exact_json_equal(manifest, expected_manifest):
        raise CompositeCheckError("composite manifest mismatch")
    return summary, summary_raw, manifest, manifest_raw


def _run_checker(
    result_dir: Path,
    *,
    allow_checker: bool = False,
    allow_postcheck: bool = False,
) -> dict[str, Any]:
    validate_root_namespace(
        result_dir,
        allow_checker=allow_checker,
        allow_postcheck=allow_postcheck,
    )
    run_config, run_raw = validate_mock_run_config(result_dir)
    run_hash = sha256_bytes(run_raw)
    static_chain, _, _ = validate_component_chain(result_dir, "static", run_hash)
    branch_chain, _, _ = validate_component_chain(result_dir, "branch", run_hash)
    summary, summary_raw, manifest, manifest_raw = validate_composite_controls(
        result_dir, run_hash, static_chain, branch_chain
    )
    source_bindings = {
        "composite_checker_source": sha256_bytes(read_snapshot(SCRIPT)[0]),
        "checker_contract": sha256_bytes(read_snapshot(CHECKER_CONTRACT)[0]),
        "release_contract": sha256_bytes(read_snapshot(RELEASE_CONTRACT)[0]),
    }
    return {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "COMPOSITE_INDEPENDENT_CHECKER",
        "authority": "INDEPENDENT_CHECKER",
        "checker_status": MOCK_CHECKER_STATUS,
        "component_status": None,
        "scientific_licensing_enabled": False,
        "passed": True,
        "matrix_id": matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_hash,
        "static_chain": static_chain,
        "branch_chain": branch_chain,
        "upstream_chains": {"mock_only": True, "scientific_replay": False},
        "s0_compatibility": None,
        "replay_counts": {"static_cells": 102, "branch_cells": 102, "component_chains": 2},
        "cross_precision": {"checked_slabs": 51, "matching_mock_verdicts": 51, "passed": True},
        "diagnostics": {
            "mock_only": True,
            "archive_generation_sha256": summary["archive_generation_sha256"],
            "composite_summary_sha256": sha256_bytes(summary_raw),
            "composite_manifest_sha256": sha256_bytes(manifest_raw),
        },
        "failures": [],
        "source_bindings": source_bindings,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def run_checker(
    result_dir: Path,
    *,
    allow_checker: bool = False,
    allow_postcheck: bool = False,
) -> dict[str, Any]:
    with capture_input_generation():
        return _run_checker(
            result_dir,
            allow_checker=allow_checker,
            allow_postcheck=allow_postcheck,
        )


def _run_postcheck(result_dir: Path) -> dict[str, Any]:
    expected = run_checker(result_dir, allow_checker=True)
    checker_path = result_dir / "independent_checker.json"
    checker, checker_raw, _ = strict_json_image(checker_path)
    exact_keys(checker, set(expected), "published composite checker")
    if not exact_json_equal(checker, expected):
        raise CompositeCheckError("published composite checker is not reproducible")
    return {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "COMPOSITE_POSTCHECK",
        "authority": "POSTCHECK_ONLY",
        "postcheck_status": MOCK_POSTCHECK_STATUS,
        "passed": True,
        "checker_path": "independent_checker.json",
        "checker_sha256": sha256_bytes(checker_raw),
        "main_freeze_sha256": None,
        "run_config_sha256": checker["run_config_sha256"],
        "bound_artifacts": {
            "composite_summary_sha256": checker["diagnostics"]["composite_summary_sha256"],
            "composite_manifest_sha256": checker["diagnostics"]["composite_manifest_sha256"],
            "archive_generation_sha256": checker["diagnostics"]["archive_generation_sha256"],
        },
        "replay_counts": checker["replay_counts"],
        "failures": [],
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def run_postcheck(result_dir: Path) -> dict[str, Any]:
    with capture_input_generation():
        return _run_postcheck(result_dir)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--postcheck", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        input_dir = _absolute_lexical(arguments.input_dir)
        with capture_input_generation():
            if arguments.postcheck:
                payload = run_postcheck(input_dir)
                output = arguments.output or input_dir / "POSTCHECK_STATUS.json"
            else:
                payload = run_checker(input_dir)
                output = arguments.output or input_dir / "independent_checker.json"
            expected_output = input_dir / (
                "POSTCHECK_STATUS.json" if arguments.postcheck else "independent_checker.json"
            )
            if _absolute_lexical(output) != expected_output:
                raise PathContractError("checker output must use the canonical archive path")
            write_once(_absolute_lexical(output), canonical_json_bytes(payload))
            validate_root_namespace(
                input_dir, allow_checker=True, allow_postcheck=arguments.postcheck
            )
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"checker_status={payload.get('checker_status', payload.get('postcheck_status'))} "
        "scientific_licensing_enabled=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
