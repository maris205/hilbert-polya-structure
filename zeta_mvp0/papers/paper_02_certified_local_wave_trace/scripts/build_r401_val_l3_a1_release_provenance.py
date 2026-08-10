#!/usr/bin/env python3
"""Build or verify the L3-A1 release-provenance envelope.

Only the mock/non-licensing path is enabled in this implementation increment.
It closes the exact 53-input plus 15-publication-object DAG without invoking
an evaluator or assigning a scientific status.  Formal production remains
fail-closed until the machine/main freezes and independent pre-freeze review
are implemented and accepted.
"""

from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
import csv
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import io
import json
import math
import os
import re
import secrets
import shlex
import stat
import struct
import sys
import zlib
from pathlib import Path, PurePosixPath
from typing import Any, Iterator, Mapping


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PROTOCOL_ID = "R401-VAL-L3-A1"
SCHEMA_VERSION = 1
RELEASE_CONTRACT = "write_once_exact_hash_dag_v1_candidate"
MOCK_RELEASE_STATUS = "PASS_MOCK_PROVENANCE_REPLAY"
MOCK_CHECKER_STATUS = "PASS_MOCK_INDEPENDENT_REPLAY"
MOCK_POSTCHECK_STATUS = "PASS_MOCK_WRITE_ONCE_POSTCHECK"
MOCK_CLAIM_BOUNDARY = (
    "mock 102-static plus 102-branch release DAG replay only; no scientific "
    "licensing, local theorem, global routing, trace-formula, Hilbert-Polya, "
    "zeta-zero, or RH promotion"
)
COMPOSITE_MOCK_CLAIM_BOUNDARY = (
    "mock 102-static plus 102-branch archive replay only; no scientific "
    "licensing, local theorem, global routing, trace-formula, Hilbert-Polya, "
    "zeta-zero, or RH promotion"
)
SCHEDULER_MOCK_CLAIM_BOUNDARY = (
    "synthetic static/branch scheduler transaction only; no Arb/CAPD "
    "scientific evaluation, no component or local theorem, no global "
    "routing, trace, Hilbert-Polya, zeta-zero, or RH claim"
)
BRANCH_CELL_CLAIM_BOUNDARY = (
    "accepted-branch complete-period tube cell only; no arbitrary-candidate "
    "tube routing, global uniqueness, trace, Hilbert--Polya, zeta, or RH claim"
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
BRANCH_CELL_BUDGETS = {
    "pipe_close_grace_ms": 1000,
    "record_bytes": 4 * 1024 * 1024,
    "stderr_bytes": 1 * 1024 * 1024,
    "stdout_bytes": 16 * 1024 * 1024,
    "term_grace_ms": 2000,
    "timeout_ms": 600000,
    "total_cell_bytes": 32 * 1024 * 1024,
}
RESULT_RELATIVE = PurePosixPath("results/r401_val_l3_all_slabs")
MAIN_FREEZE_RELATIVE = PurePosixPath(
    "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
)
RELEASE_NAME = "RELEASE_PROVENANCE.json"
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
SLABS = tuple(f"S{index:03d}" for index in range(51))
PRECISIONS = (128, 256)
RESERVED_NESTED_AUTHORITY_KEYS = {
    "authority", "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status", "release_status", "checker_status",
    "postcheck_status", "promotion_authorized", "scientific_licensing_enabled",
}


INPUT_ROLES: tuple[tuple[str, str], ...] = (
    ("a416_derivation", "research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md"),
    ("s0_protocol", "research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md"),
    ("s0_report", "research/route_a_wave_trace/A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md"),
    ("prefreeze_design", "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md"),
    ("implementation_design_review", "research/route_a_wave_trace/R401_VAL_L3_A1_DESIGN_REVIEW.md"),
    ("formal_protocol", "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"),
    ("scheduler_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"),
    ("checker_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"),
    ("release_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"),
    ("machine_freeze", "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"),
    ("prefreeze_tests", "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json"),
    ("prefreeze_review", "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md"),
    ("s0_compatibility", "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"),
    ("capd_dependency", "validated/CAPD_DEPENDENCY.md"),
    ("static_evaluator", "scripts/evaluate_r401_val_l3_a1_static_cell.py"),
    ("branch_evaluator_source", "validated/capd_r401_phase_branch_tube_mp_a1.cpp"),
    ("branch_evaluator_binary", "validated/bin/capd_r401_phase_branch_tube_mp_a1"),
    ("branch_runtime", "scripts/r401_val_l3_a1_branch_runtime.py"),
    ("scheduler", "scripts/run_r401_val_l3_a1_all_slabs.py"),
    ("static_checker_source", "scripts/check_r401_val_l3_a1_static_independent.py"),
    ("branch_checker_source", "scripts/check_r401_val_l3_a1_branch_independent.py"),
    ("composite_checker_source", "scripts/check_r401_val_l3_a1_composite_independent.py"),
    ("s0_adapter", "scripts/replay_r401_val_l3_s0_through_a1_checkers.py"),
    ("release_builder", "scripts/build_r401_val_l3_a1_release_provenance.py"),
    ("test_static_evaluator", "tests/test_r401_val_l3_a1_static_cell.py"),
    ("test_static_scheduler", "tests/test_r401_val_l3_a1_static_scheduler.py"),
    ("test_static_checker", "tests/test_r401_val_l3_a1_static_checker.py"),
    ("test_branch_scheduler", "tests/test_r401_val_l3_a1_branch_scheduler.py"),
    ("test_branch_checker", "tests/test_r401_val_l3_a1_branch_checker.py"),
    ("test_s0_compatibility", "tests/test_r401_val_l3_a1_s0_compatibility.py"),
    ("test_composite", "tests/test_r401_val_l3_a1_composite_contract.py"),
    ("test_adversarial", "tests/test_r401_val_l3_a1_adversarial_e2e.py"),
    ("test_release", "tests/test_r401_val_l3_a1_release_provenance.py"),
    ("l1_final_plan", "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"),
    ("l1_summary", "results/r401_val_l1_branch/summary.json"),
    ("l1_manifest", "results/r401_val_l1_branch/manifest.json"),
    ("l1_checker", "results/r401_val_l1_branch/independent_checker.json"),
    ("l1_postcheck", "results/r401_val_l1_branch/POSTCHECK_STATUS.json"),
    ("l1_release", "results/r401_val_l1_branch/RELEASE_PROVENANCE.json"),
    ("a415_summary", "results/r401_val_l2_all_slabs/aggregate_summary.json"),
    ("a415_manifest", "results/r401_val_l2_all_slabs/aggregate_manifest.json"),
    ("a415_checker", "results/r401_val_l2_all_slabs/independent_checker.json"),
    ("a415_postcheck", "results/r401_val_l2_all_slabs/POSTCHECK_STATUS.json"),
    ("a415_release", "results/r401_val_l2_all_slabs/RELEASE_PROVENANCE.json"),
    ("s0_static_summary", "results/r401_val_l3_phase_tube_smoke/summary.json"),
    ("s0_static_manifest", "results/r401_val_l3_phase_tube_smoke/manifest.json"),
    ("s0_static_checker", "results/r401_val_l3_phase_tube_smoke/independent_checker.json"),
    ("s0_branch_summary", "results/r401_val_l3_branch_tube_smoke/summary.json"),
    ("s0_branch_manifest", "results/r401_val_l3_branch_tube_smoke/manifest.json"),
    ("s0_branch_checker", "results/r401_val_l3_branch_tube_smoke/independent_checker.json"),
    ("s0_composite_summary", "results/r401_val_l3_s0_composite/summary.json"),
    ("s0_composite_manifest", "results/r401_val_l3_s0_composite/manifest.json"),
    ("s0_composite_checker", "results/r401_val_l3_s0_composite/independent_checker.json"),
)

DOWNSTREAM_ROLES: tuple[tuple[str, str], ...] = (
    ("run_config", f"{RESULT_RELATIVE}/run_config.json"),
    ("static_aggregate_summary", f"{RESULT_RELATIVE}/static/aggregate_summary.json"),
    ("static_aggregate_manifest", f"{RESULT_RELATIVE}/static/aggregate_manifest.json"),
    ("static_checker_result", f"{RESULT_RELATIVE}/independent_static_checker.json"),
    ("static_postcheck", f"{RESULT_RELATIVE}/STATIC_POSTCHECK_STATUS.json"),
    ("branch_aggregate_summary", f"{RESULT_RELATIVE}/branch/aggregate_summary.json"),
    ("branch_aggregate_manifest", f"{RESULT_RELATIVE}/branch/aggregate_manifest.json"),
    ("branch_checker_result", f"{RESULT_RELATIVE}/independent_branch_checker.json"),
    ("branch_postcheck", f"{RESULT_RELATIVE}/BRANCH_POSTCHECK_STATUS.json"),
    ("composite_summary", f"{RESULT_RELATIVE}/composite_summary.json"),
    ("composite_manifest", f"{RESULT_RELATIVE}/composite_manifest.json"),
    ("composite_checker_result", f"{RESULT_RELATIVE}/independent_checker.json"),
    ("composite_postcheck", f"{RESULT_RELATIVE}/POSTCHECK_STATUS.json"),
    ("production_report", f"{RESULT_RELATIVE}/R401_VAL_L3_A1_REPORT.md"),
)

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
COMPOSITE_CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "static_chain", "branch_chain", "upstream_chains", "s0_compatibility",
    "replay_counts", "cross_precision", "diagnostics", "failures",
    "source_bindings", "claim_boundary", "milestone_status",
    "theorem_status", "final_status",
}


class ReleaseError(RuntimeError):
    pass


class StrictJSONError(ReleaseError):
    pass


class PathContractError(ReleaseError):
    pass


_ACTIVE_SNAPSHOTS: dict[Path, tuple[bytes, tuple[int, int, int, int, int]]] | None = None
_ACTIVE_MACHINE_PATHS: dict[
    Path, tuple[tuple[int, int, int, int, int], Path]
] | None = None
_ACTIVE_MACHINE_MANIFEST_FILES: dict[
    Path, tuple[bytes, tuple[int, int, int, int, int]]
] | None = None
_ACTIVE_MACHINE_CAPD_NAMESPACES: dict[
    Path,
    tuple[
        frozenset[str],
        tuple[tuple[str, str, tuple[int, int, int, int, int]], ...],
    ],
] | None = None
_ACTIVE_MACHINE_CONDA_META_NAMESPACES: dict[Path, tuple[str, ...]] | None = None


def _require_plain_json(
    value: Any,
    context: str = "$",
    ancestors: set[int] | None = None,
) -> None:
    """Reject Python aliases that JSON would silently coerce on serialization."""

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


def strict_json_loads(raw: bytes, *, require_canonical: bool = False) -> Any:
    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_float=_finite_float,
            parse_constant=lambda value: (_ for _ in ()).throw(
                StrictJSONError(f"nonfinite JSON constant: {value}")
            ),
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


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def require_sha256(value: Any, context: str) -> str:
    if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
        raise StrictJSONError(f"{context} must be a lowercase SHA-256")
    return value


def exact_int(value: Any, context: str, *, expected: int | None = None) -> int:
    if type(value) is not int or value < 0:
        raise StrictJSONError(f"{context} must be an exact nonnegative integer")
    if expected is not None and value != expected:
        raise StrictJSONError(f"{context} must equal {expected}")
    return value


def exact_keys(payload: Any, expected: set[str], context: str) -> Mapping[str, Any]:
    if type(payload) is not dict or set(payload) != expected:
        actual = set(payload) if type(payload) is dict else type(payload).__name__
        raise StrictJSONError(f"{context} key set mismatch: {actual}")
    return payload


def safe_relative(value: Any) -> PurePosixPath:
    if type(value) is not str or not value or value.startswith("/"):
        raise PathContractError(f"unsafe relative path: {value}")
    if "\\" in value or "//" in value or value.endswith("/"):
        raise PathContractError(f"unsafe relative path: {value}")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise PathContractError(f"unsafe relative path: {value}")
    if pure.as_posix() != value:
        raise PathContractError(f"noncanonical relative path: {value}")
    return pure


def lexical_absolute(path: Path) -> Path:
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
    canonical = lexical_absolute(path)
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


def _read_snapshot_uncached(
    path: Path, *, reject_hardlink: bool = True
) -> tuple[bytes, os.stat_result]:
    canonical = lexical_absolute(path)
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
        fields = lambda item: (
            item.st_dev,
            item.st_ino,
            item.st_size,
            item.st_mtime_ns,
            item.st_ctime_ns,
        )
        if fields(before) != fields(after):
            raise PathContractError(f"file changed during read: {canonical}")
        replay_fd = _open_directory(canonical.parent)
        try:
            replay_parent = os.fstat(replay_fd)
            entry = os.stat(canonical.name, dir_fd=replay_fd, follow_symlinks=False)
        finally:
            os.close(replay_fd)
        if (parent_info.st_dev, parent_info.st_ino) != (
            replay_parent.st_dev,
            replay_parent.st_ino,
        ) or (before.st_dev, before.st_ino) != (entry.st_dev, entry.st_ino):
            raise PathContractError(f"path changed during read: {canonical}")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise PathContractError(f"short read: {canonical}")
        return raw, before
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def _fingerprint(info: os.stat_result) -> tuple[int, int, int, int, int]:
    return (
        info.st_dev,
        info.st_ino,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )


def read_snapshot(path: Path, *, reject_hardlink: bool = True) -> tuple[bytes, os.stat_result]:
    canonical = lexical_absolute(path)
    if _ACTIVE_SNAPSHOTS is not None and canonical in _ACTIVE_SNAPSHOTS:
        raw, expected_fingerprint = _ACTIVE_SNAPSHOTS[canonical]
        info = canonical.stat()
        if _fingerprint(info) != expected_fingerprint:
            raise PathContractError(f"captured input changed: {canonical}")
        return raw, info
    raw, info = _read_snapshot_uncached(canonical, reject_hardlink=reject_hardlink)
    if _ACTIVE_SNAPSHOTS is not None:
        _ACTIVE_SNAPSHOTS[canonical] = (raw, _fingerprint(info))
    return raw, info


@contextmanager
def capture_input_generation() -> Iterator[None]:
    global _ACTIVE_MACHINE_CAPD_NAMESPACES
    global _ACTIVE_MACHINE_CONDA_META_NAMESPACES
    global _ACTIVE_MACHINE_MANIFEST_FILES, _ACTIVE_MACHINE_PATHS, _ACTIVE_SNAPSHOTS
    if _ACTIVE_SNAPSHOTS is not None:
        yield
        return
    captured: dict[Path, tuple[bytes, tuple[int, int, int, int, int]]] = {}
    _ACTIVE_SNAPSHOTS = captured
    _ACTIVE_MACHINE_PATHS = {}
    _ACTIVE_MACHINE_MANIFEST_FILES = {}
    _ACTIVE_MACHINE_CAPD_NAMESPACES = {}
    _ACTIVE_MACHINE_CONDA_META_NAMESPACES = {}
    try:
        yield
        for path, (expected_raw, expected_fingerprint) in captured.items():
            raw, info = _read_snapshot_uncached(path)
            if raw != expected_raw or _fingerprint(info) != expected_fingerprint:
                raise PathContractError(f"input changed during release build: {path}")
        for lexical, (expected_fingerprint, expected_resolved) in (
            _ACTIVE_MACHINE_PATHS or {}
        ).items():
            info = os.lstat(lexical)
            if (
                _fingerprint(info) != expected_fingerprint
                or lexical.resolve(strict=True) != expected_resolved
            ):
                raise PathContractError(
                    f"external machine path changed during validation: {lexical}"
                )
        for path, (expected_raw, expected_fingerprint) in (
            _ACTIVE_MACHINE_MANIFEST_FILES or {}
        ).items():
            raw, info = _read_snapshot_uncached(path, reject_hardlink=False)
            if raw != expected_raw or _fingerprint(info) != expected_fingerprint:
                raise PathContractError(
                    f"machine manifest file changed during validation: {path}"
                )
        for checkout, (tracked, expected_signature) in (
            _ACTIVE_MACHINE_CAPD_NAMESPACES or {}
        ).items():
            if _machine_capd_namespace_signature(checkout, tracked) != expected_signature:
                raise PathContractError(
                    f"CAPD namespace changed during validation: {checkout}"
                )
        for meta_dir, expected_names in (
            _ACTIVE_MACHINE_CONDA_META_NAMESPACES or {}
        ).items():
            try:
                current_names = tuple(sorted(
                    (entry.name for entry in os.scandir(meta_dir)),
                    key=lambda name: name.encode("utf-8"),
                ))
            except UnicodeError as error:
                raise PathContractError(
                    f"Conda metadata namespace is not UTF-8: {meta_dir}"
                ) from error
            if current_names != expected_names:
                raise PathContractError(
                    f"Conda metadata namespace changed during validation: {meta_dir}"
                )
    finally:
        _ACTIVE_MACHINE_CONDA_META_NAMESPACES = None
        _ACTIVE_MACHINE_CAPD_NAMESPACES = None
        _ACTIVE_MACHINE_MANIFEST_FILES = None
        _ACTIVE_MACHINE_PATHS = None
        _ACTIVE_SNAPSHOTS = None


def project_file(project_root: Path, relative: str | PurePosixPath) -> Path:
    pure = safe_relative(str(relative))
    return lexical_absolute(project_root / Path(pure))


def strict_json_image(path: Path, *, canonical: bool = False) -> tuple[Mapping[str, Any], bytes]:
    raw, _ = read_snapshot(path)
    value = strict_json_loads(raw, require_canonical=canonical)
    if type(value) is not dict:
        raise StrictJSONError(f"top-level object required: {path}")
    return value, raw


def role_binding(project_root: Path, role: str, relative: str) -> dict[str, Any]:
    path = project_file(project_root, relative)
    raw, _ = read_snapshot(path)
    if relative.endswith(".json"):
        # Frozen input roles retain their original exact bytes.  They must be
        # strict JSON, but several accepted upstream producers use an
        # indented canonical representation rather than this builder's compact
        # representation.  The main-freeze hash binds either representation.
        strict_json_loads(raw, require_canonical=False)
    return {"role": role, "path": relative, "sha256": sha256_bytes(raw)}


def matrix_payload() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": slab}
        for bits in PRECISIONS
        for slab in SLABS
    ]


def matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(matrix_payload()))


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


def _current_hash(relative: str) -> str:
    raw, _ = read_snapshot(ROOT / Path(safe_relative(relative)))
    return sha256_bytes(raw)


def expected_scheduler_sources() -> dict[str, str]:
    relatives = (
        "scripts/run_r401_val_l3_a1_all_slabs.py",
        "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
        "scripts/r401_val_l3_a1_branch_runtime.py",
        "scripts/mock_r401_val_l3_a1_branch_evaluator.py",
        "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md",
        "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md",
        "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md",
        "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md",
    )
    return {relative: _current_hash(relative) for relative in relatives}


def expected_l1_bindings() -> dict[str, str]:
    relatives = (
        "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
        "results/r401_val_l1_branch/summary.json",
        "results/r401_val_l1_branch/manifest.json",
        "results/r401_val_l1_branch/independent_checker.json",
        "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
        "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    )
    return {relative: _current_hash(relative) for relative in relatives}


def expected_component_semantics(
    name: str, ordered_root: str, mock_evaluator: Mapping[str, Any] | None
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
                "checker_sha256": _current_hash(
                    "scripts/check_r401_val_l3_a1_static_independent.py"
                ),
                "producer_source_bindings": expected_scheduler_sources(),
            },
            "claim_boundary": STATIC_CHECKER_CLAIM_BOUNDARY,
            "postcheck_claim_boundary": STATIC_POSTCHECK_CLAIM_BOUNDARY,
        }
    if mock_evaluator is None:
        raise ReleaseError("branch mock evaluator binding missing")
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
            "checker_sha256": _current_hash(
                "scripts/check_r401_val_l3_a1_branch_independent.py"
            ),
            "mock_evaluator": dict(mock_evaluator),
            "producer_source_bindings": expected_scheduler_sources(),
        },
        "claim_boundary": BRANCH_CHECKER_CLAIM_BOUNDARY,
        "postcheck_claim_boundary": BRANCH_POSTCHECK_CLAIM_BOUNDARY,
    }


MOCK_FREEZE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "scientific_licensing_enabled", "matrix",
    "matrix_id", "machine_freeze_sha256", "input_roles", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}

# This is an independent copy of the prospective formal machine contract.  It
# must not import the scheduler: release replay is valuable only if a scheduler
# defect cannot silently redefine the environment that it is supposed to bind.
FORMAL_MACHINE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "production_authorized", "capture",
    "machine_requirements", "machine_observations", "python_arb", "capd",
    "compiler", "branch_binary", "runtime_libraries", "resource_evidence",
    "resource_admission", "filesystem", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
FORMAL_MACHINE_CAPTURE_KEYS = {
    "captured_at_utc", "capture_tool_path", "capture_tool_sha256",
    "boot_id_sha256",
}
FORMAL_MACHINE_REQUIREMENT_KEYS = {
    "logical_cpu_count", "memory_limit_bytes", "static_workers",
    "branch_workers", "memory_admission_limit_bytes", "reserve_bytes",
    "launch_free_bytes", "warning_free_bytes", "pause_free_bytes",
    "recovery_only_free_bytes",
}
FORMAL_MACHINE_OBSERVATION_KEYS = {
    "logical_cpu_count", "memory_limit_bytes", "result_parent_free_bytes",
    "idle_baseline_rss_bytes", "representative_static_peak_rss_bytes",
    "representative_branch_peak_rss_bytes",
}
FORMAL_MACHINE_PYTHON_ARB_KEYS = {
    "executable_path", "executable_sha256", "python_version",
    "implementation", "python_flint_version", "flint_version", "arb_version",
    "conda_manifest_algorithm", "conda_manifest_file_count",
    "conda_installed_manifest_root_sha256", "python_flint_record_sha256",
    "python_flint_installed_manifest_root_sha256",
    "arb_extension", "fmpq_extension", "bundled_libraries",
}
FORMAL_MACHINE_CAPD_KEYS = {
    "checkout_path", "commit", "tree_algorithm", "tree_sha256", "clean", "cmake_cache_path",
    "cmake_cache_sha256", "config_path", "config_sha256", "raw_flags",
    "raw_flags_sha256", "libcapd", "libfilib",
}
FORMAL_MACHINE_COMPILER_KEYS = {
    "executable_path", "executable_sha256", "version", "build_record",
}
FORMAL_MACHINE_BUILD_RECORD_KEYS = {
    "cwd", "environment", "umask", "argv", "argv_sha256", "stdout_sha256",
    "stderr_sha256", "stdout", "stderr", "return_code",
}
FORMAL_MACHINE_BRANCH_BINARY_KEYS = {
    "path", "sha256", "size_bytes", "executable_mode", "build_id", "source_path",
    "source_sha256", "elf_sha256", "dt_needed", "dt_needed_sha256",
    "runtime_libraries_sha256",
}
FORMAL_MACHINE_RUNTIME_KEYS = {"python_bundled", "capd_system"}
FORMAL_MACHINE_RUNTIME_ROW_KEYS = {
    "soname", "path", "mode", "size_bytes", "sha256", "build_id",
}
FORMAL_MACHINE_FILE_BINDING_KEYS = {
    "path", "mode", "size_bytes", "sha256", "build_id",
}
FORMAL_MACHINE_RESOURCE_EVIDENCE_KEYS = {
    "static_payload_raw_utf8", "static_payload_sha256",
    "branch_payload_raw_utf8", "branch_payload_sha256",
    "persistent_binary_sha256",
}
FORMAL_MACHINE_ADMISSION_KEYS = {
    "static_required_bytes", "branch_required_bytes", "admitted_required_bytes",
    "admission_limit_bytes", "static_inequality_passed",
    "branch_inequality_passed", "storage_launch_passed",
}
FORMAL_MACHINE_FILESYSTEM_KEYS = {
    "project_root", "result_parent", "operational_parent", "project_device_id",
    "result_device_id", "operational_device_id", "same_filesystem",
}

FORMAL_MACHINE_REQUIREMENTS = {
    "logical_cpu_count": 32,
    "memory_limit_bytes": 60 * 1024**3,
    "static_workers": 8,
    "branch_workers": 6,
    "memory_admission_limit_bytes": 48 * 1024**3,
    "reserve_bytes": 8 * 1024**3,
    "launch_free_bytes": 200 * 1024**3,
    "warning_free_bytes": 180 * 1024**3,
    "pause_free_bytes": 150 * 1024**3,
    "recovery_only_free_bytes": 120 * 1024**3,
}
FORMAL_MACHINE_PUBLIC_SLABS = ("S000", "S025", "S050")
FORMAL_MACHINE_STATIC_ARGV_COUNT = 26
FORMAL_MACHINE_BRANCH_ARGV_COUNT = 12
FORMAL_MACHINE_EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
FORMAL_MACHINE_CAPTURE_TOOL = (
    "scripts/run_r401_val_l3_a1_all_slabs.py"
)
FORMAL_MACHINE_BRANCH_SOURCE = "validated/capd_r401_phase_branch_tube_mp_a1.cpp"
FORMAL_MACHINE_BRANCH_BINARY = "validated/bin/capd_r401_phase_branch_tube_mp_a1"
FORMAL_MACHINE_STATIC_EVALUATOR = "scripts/evaluate_r401_val_l3_a1_static_cell.py"
FORMAL_MACHINE_DT_NEEDED = [
    "libc.so.6", "libgcc_s.so.1", "libm.so.6", "libmpfr.so.6",
    "libstdc++.so.6",
]
FORMAL_MACHINE_PYTHON_BUNDLED_SONAMES = (
    "libflint-6839011d.so.24.0.0",
    "libgmp-e0c82b6b.so.10.5.0",
    "libmpfr-be332c05.so.6.2.2",
)
FORMAL_MACHINE_CAPD_SYSTEM_SONAMES = (
    "ld-linux-x86-64.so.2", "libc.so.6", "libgcc_s.so.1", "libgmp.so.10",
    "libm.so.6", "libmpfr.so.6", "libstdc++.so.6",
)
FORMAL_MACHINE_TIMESTAMP = re.compile(
    r"(?:19|20)[0-9]{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
    r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z\Z"
)
FORMAL_MACHINE_BUILD_ID = re.compile(r"[0-9a-f]{40}\Z")
FORMAL_MACHINE_GIT_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
FORMAL_MACHINE_CLAIM_BOUNDARY = (
    "machine, toolchain, persistent-binary, filesystem, and representative "
    "resource admission only; no evaluator dispatch, component status, local "
    "theorem, global routing, Hilbert-Polya, zeta-zero, or RH claim"
)
FORMAL_MACHINE_RESOURCE_CLAIM_BOUNDARY = (
    "representative public-cell resource calibration only; recorded paths are "
    "inert evidence and no held-out scientific result or production authority "
    "is claimed"
)
FORMAL_MACHINE_CONDA_MANIFEST_ALGORITHM = "CONDA_META_LIVE_FILES_CJ_COMPACT_V1"
FORMAL_MACHINE_PYTHON_FLINT_RECORD_SHA256 = (
    "a140c3cb2ba819edc913c2adae2dc0a60d49f7f3be547f139b7beb8be9c0d3da"
)
FORMAL_MACHINE_PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256 = (
    "32a2b16585f81fe5cd4a4c3b7d0d70e0f867f1a032db4b9c3b0f414cf991c870"
)
FORMAL_MACHINE_CAPD_TREE_ALGORITHM = "GIT_INDEX_LIVE_TREE_CJ_COMPACT_V1"
FORMAL_MACHINE_PYTHON_VERSION = (
    "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) "
    "[GCC 11.2.0]"
)
FORMAL_MACHINE_COMPILER_VERSION = (
    "g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
)
FORMAL_STATIC_RESOURCE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "scope",
    "production_authorized", "scientific_licensing_enabled", "claim_boundary",
    "project_root", "temporary_root", "execution_environment", "bindings",
    "measurement", "sequential_runs", "concurrent_schedule", "concurrent_runs",
    "admission", "component_status", "milestone_status", "theorem_status",
    "final_status",
}
FORMAL_STATIC_RESOURCE_BINDING_KEYS = {
    "evaluator", "interpreter", "python_flint", "plan", "calibration_binding",
}
FORMAL_STATIC_RESOURCE_EVALUATOR_KEYS = {"path", "sha256", "size_bytes", "mode"}
FORMAL_STATIC_RESOURCE_INTERPRETER_KEYS = {
    "invocation_path", "resolved_path", "sha256", "size_bytes", "version",
}
FORMAL_STATIC_RESOURCE_FLINT_KEYS = {
    "version", "flint_version", "module_path", "record_path", "record_sha256",
    "installed_record_file_count", "installed_manifest_sha256",
    "arb_extension_path", "arb_extension_sha256",
}
FORMAL_STATIC_RESOURCE_PLAN_KEYS = {"path", "sha256", "public_slab_ids"}
FORMAL_STATIC_RESOURCE_CALIBRATION_KEYS = {
    "matrix_id", "nonfreeze_sha256", "nonrunconfig_sha256",
}
FORMAL_STATIC_RESOURCE_ENV_KEYS = {
    "LANG", "LC_ALL", "TZ", "PYTHONHASHSEED", "PYTHONNOUSERSITE",
    "PYTHONDONTWRITEBYTECODE", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
}
FORMAL_STATIC_RESOURCE_MEASUREMENT_KEYS = {
    "method", "ru_maxrss_unit", "bytes_per_kib", "cgroup_usage_path",
    "cgroup_limit_path", "cgroup_limit_bytes", "baseline_samples_bytes",
    "baseline_conservative_bytes", "concurrent_samples_bytes",
    "concurrent_peak_bytes", "sample_interval_seconds",
}
FORMAL_STATIC_RESOURCE_RUN_KEYS = {
    "label", "precision_bits", "slab_id", "replica", "argv", "returncode",
    "elapsed_seconds", "peak_rss_kib", "user_cpu_seconds", "system_cpu_seconds",
    "output", "output_bytes", "output_sha256", "stdout", "stdout_bytes",
    "stdout_sha256", "stdout_exact_status_line", "stderr", "stderr_bytes",
    "stderr_sha256", "stderr_empty", "evaluator_status", "scientific_status",
    "component_status", "milestone_status", "theorem_status", "final_status",
}
FORMAL_STATIC_RESOURCE_SCHEDULE_KEYS = {"precision_bits", "slab_id"}
FORMAL_STATIC_RESOURCE_ADMISSION_KEYS = {
    "workers", "representative_peak_rss_bytes", "idle_baseline_bytes",
    "reserve_bytes", "admission_limit_bytes", "lhs_bytes", "headroom_bytes",
    "formula", "passes",
}
FORMAL_BRANCH_RESOURCE_KEYS = {
    "scope", "binary", "binary_sha256", "cgroup_limit_bytes",
    "baseline_samples_bytes", "baseline_conservative_bytes", "post_samples_bytes",
    "results", "task_count", "per_process_peak_rss_max_kib",
    "sampled_concurrent_peak_bytes", "sampled_concurrent_increment_bytes",
    "admission", "scientific_status", "milestone_status", "theorem_status",
    "final_status",
}
FORMAL_BRANCH_RESOURCE_RUN_KEYS = {
    "precision_bits", "slab_id", "argv", "argv_count", "returncode",
    "elapsed_seconds", "peak_rss_kib", "user_cpu_seconds", "system_cpu_seconds",
    "stdout_bytes", "stdout_sha256", "stderr_bytes", "stderr_sha256",
    "abi_verified", "terminal_abi_value",
}
FORMAL_BRANCH_RESOURCE_ADMISSION_KEYS = {
    "baseline_bytes", "peak_rss_bytes", "workers", "reserve_bytes",
    "limit_bytes", "lhs_bytes", "headroom_bytes", "formula", "passes",
}


def _machine_positive_int(value: Any, context: str) -> int:
    if type(value) is not int or value <= 0:
        raise ReleaseError(f"{context} must be a positive exact integer")
    return value


def _machine_nonnegative_int(value: Any, context: str) -> int:
    if type(value) is not int or value < 0:
        raise ReleaseError(f"{context} must be a nonnegative exact integer")
    return value


def _machine_nonnegative_float(value: Any, context: str) -> float:
    if type(value) is not float or not math.isfinite(value) or value < 0.0:
        raise ReleaseError(f"{context} must be a finite nonnegative JSON float")
    return value


def _machine_nonempty_string(value: Any, context: str) -> str:
    if type(value) is not str or not value or "\x00" in value:
        raise ReleaseError(f"{context} must be a nonempty exact string")
    return value


def _machine_project_path(project_root: Path, value: Any, context: str) -> Path:
    try:
        relative = safe_relative(value)
    except Exception as error:
        raise PathContractError(f"{context} is not a canonical project path") from error
    return project_file(project_root, relative)


def _machine_external_snapshot(value: Any, context: str) -> tuple[bytes, os.stat_result, Path]:
    """Read an absolute external tool/library path and pin a final symlink.

    Repository-owned inputs are never allowed to be links.  The machine's
    Python and compiler invocation paths are distribution-managed symlinks,
    however, so their target bytes are bound while the lexical link identity
    is replayed on both sides of the read.
    """

    if type(value) is not str:
        raise PathContractError(f"{context} path must be an exact string")
    lexical = lexical_absolute(Path(value))
    before = os.lstat(lexical)
    resolved = lexical.resolve(strict=True)
    raw, info = read_snapshot(resolved)
    after = os.lstat(lexical)
    if _fingerprint(before) != _fingerprint(after) or lexical.resolve(strict=True) != resolved:
        raise PathContractError(f"{context} path changed during validation")
    if _ACTIVE_MACHINE_PATHS is not None:
        captured = (_fingerprint(after), resolved)
        previous = _ACTIVE_MACHINE_PATHS.setdefault(lexical, captured)
        if previous != captured:
            raise PathContractError(f"{context} external path identity changed")
    return raw, info, resolved


def _machine_manifest_file_snapshot(
    path: Path, context: str
) -> tuple[bytes, os.stat_result]:
    """Capture a package-managed regular file, allowing conda hard links."""

    canonical = lexical_absolute(path)
    raw, info = _read_snapshot_uncached(canonical, reject_hardlink=False)
    if _ACTIVE_MACHINE_MANIFEST_FILES is not None:
        captured = (raw, _fingerprint(info))
        previous = _ACTIVE_MACHINE_MANIFEST_FILES.setdefault(canonical, captured)
        if previous != captured:
            raise PathContractError(f"{context} changed between manifest reads")
    return raw, info


def _machine_manifest_symlink_snapshot(
    path: Path, context: str
) -> tuple[bytes, os.stat_result]:
    """Capture the exact target text and identity of a package symlink."""

    lexical = lexical_absolute(path)
    before = os.lstat(lexical)
    if not stat.S_ISLNK(before.st_mode):
        raise PathContractError(f"{context} is not a symlink")
    target = os.readlink(lexical)
    try:
        raw = target.encode("utf-8")
    except UnicodeError as error:
        raise PathContractError(f"{context} target is not strict UTF-8") from error
    after = os.lstat(lexical)
    resolved = lexical.resolve(strict=True)
    if _fingerprint(before) != _fingerprint(after) or len(raw) != before.st_size:
        raise PathContractError(f"{context} changed during symlink read")
    if _ACTIVE_MACHINE_PATHS is not None:
        captured = (_fingerprint(after), resolved)
        previous = _ACTIVE_MACHINE_PATHS.setdefault(lexical, captured)
        if previous != captured:
            raise PathContractError(f"{context} symlink identity changed")
    return raw, before


def _machine_boot_id_bytes() -> bytes:
    """Read the procfs boot identifier without applying regular-file size rules."""

    path = Path("/proc/sys/kernel/random/boot_id")
    before = os.stat(path, follow_symlinks=False)
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        raw = os.read(descriptor, 256)
        if os.read(descriptor, 1):
            raise PathContractError("boot ID exceeded its bounded ABI")
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    replay = os.stat(path, follow_symlinks=False)
    if (
        (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino)
        or (before.st_dev, before.st_ino) != (replay.st_dev, replay.st_ino)
        or re.fullmatch(
            rb"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\n",
            raw,
        )
        is None
    ):
        raise PathContractError("boot ID changed or is malformed")
    return raw


def _machine_project_snapshot(
    project_root: Path, value: Any, context: str
) -> tuple[bytes, os.stat_result, Path]:
    path = _machine_project_path(project_root, value, context)
    raw, info = read_snapshot(path)
    return raw, info, path


def _machine_require_live_hash(
    raw: bytes, expected: Any, context: str
) -> str:
    digest = require_sha256(expected, context)
    if sha256_bytes(raw) != digest:
        raise ReleaseError(f"{context} does not match live bytes")
    return digest


def _machine_require_mode(value: Any, info: os.stat_result, context: str) -> int:
    if type(value) is not int or value < 0 or value > 0o7777:
        raise ReleaseError(f"{context} mode must be an exact permission integer")
    actual = stat.S_IMODE(info.st_mode)
    if value != actual:
        raise ReleaseError(f"{context} mode does not match live bytes")
    return value


def _machine_require_static_evidence_mode(
    value: Any, info: os.stat_result, context: str
) -> str:
    """Validate the historical string-mode field in the raw static receipt."""

    if type(value) is not str or re.fullmatch(r"0[0-7]{3}", value) is None:
        raise ReleaseError(f"{context} evidence mode is malformed")
    if value != f"{stat.S_IMODE(info.st_mode):04o}":
        raise ReleaseError(f"{context} evidence mode does not match live bytes")
    return value


def _machine_elf_metadata(raw: bytes, context: str) -> tuple[str, list[str], str | None]:
    """Parse GNU build-id, DT_NEEDED, and DT_SONAME without external tools.

    The formal machine is pinned to 64-bit little-endian x86-64 ELF objects.
    Reading section tables directly avoids trusting an unbound ``readelf``
    executable during the independent release replay.
    """

    header_format = "<16sHHIQQQIHHHHHH"
    section_format = "<IIQQQQIIQQ"
    dynamic_format = "<qQ"
    header_size = struct.calcsize(header_format)
    section_size = struct.calcsize(section_format)
    if len(raw) < header_size:
        raise ReleaseError(f"{context} is a truncated ELF image")
    header = struct.unpack_from(header_format, raw, 0)
    ident = header[0]
    if (
        ident[:4] != b"\x7fELF"
        or ident[4] != 2  # ELFCLASS64
        or ident[5] != 1  # ELFDATA2LSB
        or ident[6] != 1  # EV_CURRENT
        or header[2] != 62  # EM_X86_64
        or header[3] != 1
        or header[8] != header_size
        or header[11] != section_size
    ):
        raise ReleaseError(f"{context} ELF identity/header mismatch")
    section_offset = header[6]
    section_count = header[12]
    section_name_index = header[13]
    if (
        type(section_offset) is not int
        or type(section_count) is not int
        or section_offset <= 0
        or section_count <= 0
        or section_name_index >= section_count
        or section_offset + section_count * section_size > len(raw)
    ):
        raise ReleaseError(f"{context} ELF section table is malformed")
    sections = [
        struct.unpack_from(section_format, raw, section_offset + index * section_size)
        for index in range(section_count)
    ]

    def section_bytes(index: int, label: str) -> bytes:
        if type(index) is not int or index < 0 or index >= len(sections):
            raise ReleaseError(f"{context} ELF {label} section index is invalid")
        section = sections[index]
        offset, size = section[4], section[5]
        if offset > len(raw) or size > len(raw) - offset:
            raise ReleaseError(f"{context} ELF {label} section is out of bounds")
        return raw[offset : offset + size]

    # Validate the section-name table even though metadata extraction only
    # needs section types and dynamic-string links.
    if sections[section_name_index][1] != 3:  # SHT_STRTAB
        raise ReleaseError(f"{context} ELF section-name table is malformed")
    section_bytes(section_name_index, "section-name")

    build_ids: list[str] = []
    needed: list[str] = []
    sonames: list[str] = []
    for index, section in enumerate(sections):
        section_type = section[1]
        if section_type == 7:  # SHT_NOTE
            note = section_bytes(index, "note")
            cursor = 0
            while cursor < len(note):
                if len(note) - cursor < 12:
                    raise ReleaseError(f"{context} ELF note header is truncated")
                name_size, description_size, note_type = struct.unpack_from(
                    "<III", note, cursor
                )
                cursor += 12
                name_end = cursor + name_size
                description_start = (name_end + 3) & ~3
                description_end = description_start + description_size
                next_cursor = (description_end + 3) & ~3
                if (
                    name_end > len(note)
                    or description_end > len(note)
                    or next_cursor > len(note)
                ):
                    raise ReleaseError(f"{context} ELF note payload is truncated")
                name = note[cursor:name_end]
                description = note[description_start:description_end]
                if name == b"GNU\x00" and note_type == 3:  # NT_GNU_BUILD_ID
                    if len(description) != 20:
                        raise ReleaseError(f"{context} GNU build-id is not 20 bytes")
                    build_ids.append(description.hex())
                cursor = next_cursor
        elif section_type == 6:  # SHT_DYNAMIC
            dynamic = section_bytes(index, "dynamic")
            entry_size = section[9]
            string_index = section[6]
            if (
                entry_size != struct.calcsize(dynamic_format)
                or len(dynamic) % entry_size != 0
                or string_index >= len(sections)
                or sections[string_index][1] != 3
            ):
                raise ReleaseError(f"{context} ELF dynamic table is malformed")
            strings = section_bytes(string_index, "dynamic-string")

            def dynamic_string(offset: int) -> str:
                if offset <= 0 or offset >= len(strings):
                    raise ReleaseError(f"{context} ELF dynamic string offset is invalid")
                end = strings.find(b"\x00", offset)
                if end < 0:
                    raise ReleaseError(f"{context} ELF dynamic string is unterminated")
                try:
                    value = strings[offset:end].decode("ascii")
                except UnicodeDecodeError as error:
                    raise ReleaseError(
                        f"{context} ELF dynamic string is not ASCII"
                    ) from error
                if not value or "/" in value or "\x00" in value:
                    raise ReleaseError(f"{context} ELF dynamic string is unsafe")
                return value

            for cursor in range(0, len(dynamic), entry_size):
                tag, value = struct.unpack_from(dynamic_format, dynamic, cursor)
                if tag == 0:  # DT_NULL
                    break
                if tag == 1:  # DT_NEEDED
                    needed.append(dynamic_string(value))
                elif tag == 14:  # DT_SONAME
                    sonames.append(dynamic_string(value))
    if len(build_ids) != 1 or FORMAL_MACHINE_BUILD_ID.fullmatch(build_ids[0]) is None:
        raise ReleaseError(f"{context} must contain one exact GNU build-id")
    if len(needed) != len(set(needed)):
        raise ReleaseError(f"{context} repeats a DT_NEEDED entry")
    if len(sonames) > 1:
        raise ReleaseError(f"{context} repeats DT_SONAME")
    return build_ids[0], sorted(needed), sonames[0] if sonames else None


def _machine_validate_file_binding(
    binding: Any,
    context: str,
    *,
    allow_null_build_id: bool = False,
) -> tuple[bytes, os.stat_result]:
    exact_keys(binding, FORMAL_MACHINE_FILE_BINDING_KEYS, context)
    raw, info, _ = _machine_external_snapshot(binding["path"], context)
    _machine_require_mode(binding["mode"], info, context)
    if _machine_positive_int(binding["size_bytes"], f"{context}.size_bytes") != len(raw):
        raise ReleaseError(f"{context} size does not match live bytes")
    _machine_require_live_hash(raw, binding["sha256"], f"{context}.sha256")
    build_id = binding["build_id"]
    if build_id is None and allow_null_build_id:
        return raw, info
    if type(build_id) is not str or FORMAL_MACHINE_BUILD_ID.fullmatch(build_id) is None:
        raise ReleaseError(f"{context}.build_id is malformed")
    live_build_id, _, _ = _machine_elf_metadata(raw, context)
    if build_id != live_build_id:
        raise ReleaseError(f"{context}.build_id does not match live ELF bytes")
    return raw, info


def _machine_plan_records(project_root: Path) -> tuple[dict[str, Mapping[str, Any]], str]:
    path = project_file(
        project_root, "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
    )
    payload, raw = strict_json_image(path, canonical=False)
    slabs = payload.get("slabs")
    if type(slabs) is not list:
        raise ReleaseError("L1 plan has no exact slab array")
    records: dict[str, Mapping[str, Any]] = {}
    for record in slabs:
        if type(record) is not dict or type(record.get("slab_id")) is not str:
            raise ReleaseError("L1 plan slab is malformed")
        if record["slab_id"] in records:
            raise ReleaseError("L1 plan contains a duplicate slab identity")
        records[record["slab_id"]] = record
    if any(slab not in records for slab in FORMAL_MACHINE_PUBLIC_SLABS):
        raise ReleaseError("L1 plan is missing a public calibration slab")
    return records, sha256_bytes(raw)


def _machine_static_argv(
    row: Mapping[str, Any],
    bindings: Mapping[str, Any],
    plan_record: Mapping[str, Any],
) -> list[str]:
    return [
        bindings["interpreter"]["invocation_path"],
        bindings["evaluator"]["path"],
        "--slab-id", row["slab_id"],
        "--precision-bits", str(row["precision_bits"]),
        "--epsilon-lower", plan_record["epsilon_lower"],
        "--epsilon-upper", plan_record["epsilon_upper"],
        "--matrix-id", bindings["calibration_binding"]["matrix_id"],
        "--freeze-sha256", bindings["calibration_binding"]["nonfreeze_sha256"],
        "--run-config-sha256", bindings["calibration_binding"]["nonrunconfig_sha256"],
        "--plan-record-sha256", sha256_bytes(canonical_json_bytes(plan_record)),
        "--max-depth", "24",
        "--max-nodes-per-tree", "250000",
        "--max-nodes-per-cell", "1000000",
        "--output", row["output"],
    ]


def _machine_validate_static_run(
    row: Any,
    *,
    context: str,
    identity: tuple[int, str, int],
    bindings: Mapping[str, Any],
    plan_records: Mapping[str, Mapping[str, Any]],
    temporary_root: Path,
    expected_label: str,
) -> int:
    exact_keys(row, FORMAL_STATIC_RESOURCE_RUN_KEYS, context)
    bits, slab, replica = identity
    if (row["precision_bits"], row["slab_id"], row["replica"]) != identity:
        raise ReleaseError(f"{context} public identity/order mismatch")
    if row["label"] != expected_label:
        raise ReleaseError(f"{context} label mismatch")
    for key in ("precision_bits", "replica", "returncode", "peak_rss_kib", "output_bytes", "stdout_bytes", "stderr_bytes"):
        _machine_nonnegative_int(row[key], f"{context}.{key}")
    for key in ("elapsed_seconds", "user_cpu_seconds", "system_cpu_seconds"):
        _machine_nonnegative_float(row[key], f"{context}.{key}")
    if bits not in PRECISIONS or slab not in FORMAL_MACHINE_PUBLIC_SLABS:
        raise ReleaseError(f"{context} is not a public calibration cell")
    if row["returncode"] != 0 or row["peak_rss_kib"] <= 0 or row["output_bytes"] <= 0:
        raise ReleaseError(f"{context} did not complete a usable resource run")
    if row["stdout_exact_status_line"] != "evaluator_status=STATIC_CELL_CERTIFIED":
        raise ReleaseError(f"{context} status-line ABI mismatch")
    if row["evaluator_status"] != "STATIC_CELL_CERTIFIED":
        raise ReleaseError(f"{context} evaluator ABI mismatch")
    if row["stderr_empty"] is not True or row["stderr_bytes"] != 0:
        raise ReleaseError(f"{context} has nonempty stderr")
    for key in ("output_sha256", "stdout_sha256", "stderr_sha256"):
        require_sha256(row[key], f"{context}.{key}")
    if row["stderr_sha256"] != FORMAL_MACHINE_EMPTY_SHA256:
        raise ReleaseError(f"{context} empty stderr hash mismatch")
    expected_stdout = b"evaluator_status=STATIC_CELL_CERTIFIED\n"
    if (
        row["stdout_bytes"] != len(expected_stdout)
        or row["stdout_sha256"] != sha256_bytes(expected_stdout)
    ):
        raise ReleaseError(f"{context} stdout ABI receipt mismatch")
    for key in ("scientific_status", "component_status", "milestone_status", "theorem_status", "final_status"):
        if row[key] is not None:
            raise ReleaseError(f"{context} overclaims {key}")
    for key in ("output", "stdout", "stderr"):
        path = lexical_absolute(Path(_machine_nonempty_string(row[key], f"{context}.{key}")))
        try:
            path.relative_to(temporary_root)
        except ValueError as error:
            raise PathContractError(f"{context}.{key} escaped temporary evidence") from error
    if row["argv"] != _machine_static_argv(row, bindings, plan_records[slab]):
        raise ReleaseError(f"{context} exact argv mismatch")
    return row["peak_rss_kib"] * 1024


def _machine_validate_static_resource(
    project_root: Path,
    raw: bytes,
    machine: Mapping[str, Any],
) -> dict[str, int]:
    payload = strict_json_loads(raw, require_canonical=True)
    exact_keys(payload, FORMAL_STATIC_RESOURCE_KEYS, "static resource evidence")
    if (
        type(payload["schema_version"]) is not int
        or payload["schema_version"] != 1
        or payload["protocol_id"] != PROTOCOL_ID
        or payload["artifact_role"] != "TEMP_PUBLIC_STATIC_RSS_CALIBRATION"
        or payload["scope"] != "PUBLIC_S0_RESOURCE_CALIBRATION_ONLY"
        or payload["production_authorized"] is not False
        or payload["scientific_licensing_enabled"] is not False
    ):
        raise ReleaseError("static resource evidence identity mismatch")
    if payload["claim_boundary"] != (
        "resource telemetry on already-public S000/S025/S050 at 128/256 only; "
        "no held-out/all-slab evaluation, no freeze, no scientific promotion"
    ):
        raise ReleaseError("static resource evidence claim boundary mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload[key] is not None:
            raise ReleaseError(f"static resource evidence overclaims {key}")
    if payload["project_root"] != str(project_root):
        raise ReleaseError("static resource evidence project-root mismatch")
    temporary_root = lexical_absolute(Path(payload["temporary_root"]))
    if temporary_root.parts[:2] != ("/", "tmp"):
        raise PathContractError("static resource origin is not inert /tmp evidence")
    exact_keys(payload["execution_environment"], FORMAL_STATIC_RESOURCE_ENV_KEYS, "static resource environment")
    expected_environment = {
        "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC",
        "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1",
    }
    if not exact_json_equal(payload["execution_environment"], expected_environment):
        raise ReleaseError("static resource execution environment mismatch")
    bindings = exact_keys(payload["bindings"], FORMAL_STATIC_RESOURCE_BINDING_KEYS, "static resource bindings")
    exact_keys(bindings["evaluator"], FORMAL_STATIC_RESOURCE_EVALUATOR_KEYS, "static evaluator binding")
    exact_keys(bindings["interpreter"], FORMAL_STATIC_RESOURCE_INTERPRETER_KEYS, "static interpreter binding")
    exact_keys(bindings["python_flint"], FORMAL_STATIC_RESOURCE_FLINT_KEYS, "static python-flint binding")
    exact_keys(bindings["plan"], FORMAL_STATIC_RESOURCE_PLAN_KEYS, "static plan binding")
    exact_keys(bindings["calibration_binding"], FORMAL_STATIC_RESOURCE_CALIBRATION_KEYS, "static calibration binding")
    evaluator_raw, evaluator_info, evaluator_path = _machine_project_snapshot(
        project_root, FORMAL_MACHINE_STATIC_EVALUATOR, "static evaluator"
    )
    if bindings["evaluator"]["path"] != str(evaluator_path):
        raise ReleaseError("static resource evaluator path mismatch")
    _machine_require_live_hash(evaluator_raw, bindings["evaluator"]["sha256"], "static evaluator")
    if (
        _machine_positive_int(
            bindings["evaluator"]["size_bytes"],
            "static evaluator.size_bytes",
        )
        != len(evaluator_raw)
    ):
        raise ReleaseError("static resource evaluator size mismatch")
    _machine_require_static_evidence_mode(
        bindings["evaluator"]["mode"], evaluator_info, "static evaluator"
    )
    python = machine["python_arb"]
    interpreter_raw, _, interpreter_resolved = _machine_external_snapshot(
        bindings["interpreter"]["invocation_path"],
        "static resource interpreter",
    )
    _machine_positive_int(
        bindings["interpreter"]["size_bytes"],
        "static interpreter.size_bytes",
    )
    if (
        bindings["interpreter"]["invocation_path"] != python["executable_path"]
        or bindings["interpreter"]["resolved_path"] != str(interpreter_resolved)
        or bindings["interpreter"]["sha256"] != python["executable_sha256"]
        or bindings["interpreter"]["sha256"] != sha256_bytes(interpreter_raw)
        or bindings["interpreter"]["size_bytes"] != len(interpreter_raw)
        or bindings["interpreter"]["version"] != python["python_version"]
    ):
        raise ReleaseError("static resource interpreter cross-binding mismatch")
    flint = bindings["python_flint"]
    _, _, module_resolved = _machine_external_snapshot(
        flint["module_path"], "static resource python-flint module"
    )
    record_raw, _, record_resolved = _machine_external_snapshot(
        flint["record_path"], "static resource python-flint RECORD"
    )
    site_packages = record_resolved.parents[1]
    expected_module = site_packages / "flint/__init__.py"
    expected_arb = site_packages / "flint/types/arb.abi3.so"
    expected_fmpq = site_packages / "flint/types/fmpq.abi3.so"
    if (
        record_resolved.name != "RECORD"
        or record_resolved.parent.name != "python_flint-0.9.0.dist-info"
        or module_resolved != expected_module
        or flint["module_path"] != str(expected_module)
        or flint["record_path"] != str(record_resolved)
        or python["arb_extension"]["path"] != str(expected_arb)
        or python["fmpq_extension"]["path"] != str(expected_fmpq)
    ):
        raise PathContractError("static Python-flint installation paths are incoherent")
    installed_count, installed_root = _machine_recompute_python_flint_manifest(
        str(record_resolved), record_raw
    )
    _machine_positive_int(
        flint["installed_record_file_count"],
        "static python-flint installed_record_file_count",
    )
    if (
        flint["version"] != python["python_flint_version"]
        or flint["flint_version"] != python["flint_version"]
        or flint["installed_manifest_sha256"]
        != python["python_flint_installed_manifest_root_sha256"]
        or flint["record_sha256"] != python["python_flint_record_sha256"]
        or flint["record_sha256"] != sha256_bytes(record_raw)
        or flint["installed_record_file_count"] != installed_count
        or flint["installed_manifest_sha256"] != installed_root
        or flint["arb_extension_path"] != python["arb_extension"]["path"]
        or flint["arb_extension_sha256"] != python["arb_extension"]["sha256"]
    ):
        raise ReleaseError("static resource Python-Arb cross-binding mismatch")
    plan_records, plan_sha = _machine_plan_records(project_root)
    if (
        bindings["plan"]["path"] != str(project_file(project_root, "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"))
        or bindings["plan"]["sha256"] != plan_sha
        or bindings["plan"]["public_slab_ids"] != list(FORMAL_MACHINE_PUBLIC_SLABS)
    ):
        raise ReleaseError("static resource plan cross-binding mismatch")
    for key in ("matrix_id", "nonfreeze_sha256", "nonrunconfig_sha256"):
        require_sha256(bindings["calibration_binding"][key], f"static calibration {key}")
    if bindings["calibration_binding"]["matrix_id"] != matrix_id():
        raise ReleaseError("static resource matrix mismatch")
    public = [(bits, slab) for bits in PRECISIONS for slab in FORMAL_MACHINE_PUBLIC_SLABS]
    sequential = payload["sequential_runs"]
    if type(sequential) is not list or len(sequential) != 6:
        raise ReleaseError("static resource must contain six sequential public runs")
    peaks: list[int] = []
    for index, (row, (bits, slab)) in enumerate(zip(sequential, public, strict=True)):
        peaks.append(_machine_validate_static_run(
            row, context=f"static sequential row {index}", identity=(bits, slab, 0),
            bindings=bindings, plan_records=plan_records, temporary_root=temporary_root,
            expected_label=f"{bits}_{slab}",
        ))
    stress = [*public, (256, "S025"), (256, "S050")]
    schedule = payload["concurrent_schedule"]
    if type(schedule) is not list or len(schedule) != 8:
        raise ReleaseError("static resource concurrent schedule mismatch")
    for row, (bits, slab) in zip(schedule, stress, strict=True):
        exact_keys(row, FORMAL_STATIC_RESOURCE_SCHEDULE_KEYS, "static resource schedule row")
        _machine_positive_int(
            row["precision_bits"], "static resource schedule precision_bits"
        )
        if row != {"precision_bits": bits, "slab_id": slab}:
            raise ReleaseError("static resource schedule identity mismatch")
    concurrent = payload["concurrent_runs"]
    if type(concurrent) is not list or len(concurrent) != 8:
        raise ReleaseError("static resource must contain eight concurrent public runs")
    seen: dict[tuple[int, str], int] = {}
    for index, (row, (bits, slab)) in enumerate(zip(concurrent, stress, strict=True)):
        replica = seen.get((bits, slab), 0)
        seen[(bits, slab)] = replica + 1
        peaks.append(_machine_validate_static_run(
            row, context=f"static concurrent row {index}", identity=(bits, slab, replica),
            bindings=bindings, plan_records=plan_records, temporary_root=temporary_root,
            expected_label=f"{index:02d}_{bits}_{slab}_r{replica}",
        ))
    measurement = exact_keys(payload["measurement"], FORMAL_STATIC_RESOURCE_MEASUREMENT_KEYS, "static resource measurement")
    for key in (
        "bytes_per_kib", "cgroup_limit_bytes", "baseline_conservative_bytes",
        "concurrent_peak_bytes",
    ):
        _machine_positive_int(
            measurement[key], f"static resource measurement.{key}"
        )
    if (
        measurement["method"] != "os.wait4(pid,0/WNOHANG).rusage.ru_maxrss on Linux"
        or measurement["ru_maxrss_unit"] != "KiB"
        or measurement["bytes_per_kib"] != 1024
        or measurement["cgroup_usage_path"] != "/sys/fs/cgroup/memory/memory.usage_in_bytes"
        or measurement["cgroup_limit_path"] != "/sys/fs/cgroup/memory/memory.limit_in_bytes"
        or measurement["cgroup_limit_bytes"] != FORMAL_MACHINE_REQUIREMENTS["memory_limit_bytes"]
    ):
        raise ReleaseError("static resource measurement method mismatch")
    baseline_samples = measurement["baseline_samples_bytes"]
    concurrent_samples = measurement["concurrent_samples_bytes"]
    if type(baseline_samples) is not list or len(baseline_samples) != 21 or type(concurrent_samples) is not list or not concurrent_samples:
        raise ReleaseError("static resource cgroup sample shape mismatch")
    for value in [*baseline_samples, *concurrent_samples]:
        _machine_positive_int(value, "static resource cgroup sample")
    if measurement["baseline_conservative_bytes"] != max(baseline_samples):
        raise ReleaseError("static resource baseline aggregation mismatch")
    if measurement["concurrent_peak_bytes"] != max(concurrent_samples):
        raise ReleaseError("static resource concurrent aggregation mismatch")
    if type(measurement["sample_interval_seconds"]) is not float or measurement["sample_interval_seconds"] != 0.05:
        raise ReleaseError("static resource sample interval mismatch")
    admission = exact_keys(payload["admission"], FORMAL_STATIC_RESOURCE_ADMISSION_KEYS, "static resource admission")
    for key in (
        "workers", "representative_peak_rss_bytes", "idle_baseline_bytes",
        "reserve_bytes", "admission_limit_bytes", "lhs_bytes",
    ):
        _machine_positive_int(admission[key], f"static resource admission.{key}")
    _machine_nonnegative_int(
        admission["headroom_bytes"], "static resource admission.headroom_bytes"
    )
    peak = max(peaks)
    baseline = measurement["baseline_conservative_bytes"]
    expected_lhs = baseline + 8 * peak + FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
    if (
        admission["workers"] != 8
        or admission["representative_peak_rss_bytes"] != peak
        or admission["idle_baseline_bytes"] != baseline
        or admission["reserve_bytes"] != FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
        or admission["admission_limit_bytes"] != FORMAL_MACHINE_REQUIREMENTS["memory_admission_limit_bytes"]
        or admission["lhs_bytes"] != expected_lhs
        or admission["headroom_bytes"] != admission["admission_limit_bytes"] - expected_lhs
        or admission["formula"] != "idle_baseline_bytes + workers * representative_peak_rss_bytes + reserve_bytes <= admission_limit_bytes"
        or admission["passes"] is not (expected_lhs <= admission["admission_limit_bytes"])
    ):
        raise ReleaseError("static resource admission arithmetic mismatch")
    return {"baseline_bytes": baseline, "peak_rss_bytes": peak}


def _machine_branch_argv(
    binary_path: str,
    bits: int,
    record: Mapping[str, Any],
) -> list[str]:
    center = record["center"]
    radii = record["root_radii"]

    def endpoint(name: str, sign: int) -> str:
        value = Decimal(center[name]) + sign * Decimal(radii[name])
        return format(value, "f")

    return [
        binary_path,
        str(bits),
        record["epsilon_lower"],
        record["epsilon_upper"],
        endpoint("q_slow", -1),
        endpoint("q_slow", 1),
        endpoint("q_fast", -1),
        endpoint("q_fast", 1),
        endpoint("p_slow", -1),
        endpoint("p_slow", 1),
        endpoint("period", -1),
        endpoint("period", 1),
    ]


def _machine_validate_branch_resource(
    project_root: Path,
    raw: bytes,
    machine: Mapping[str, Any],
) -> dict[str, int]:
    payload = strict_json_loads(raw, require_canonical=False)
    if branch_transaction_json_bytes(payload) != raw:
        raise StrictJSONError("branch resource evidence is not its exact pretty JSON")
    exact_keys(payload, FORMAL_BRANCH_RESOURCE_KEYS, "branch resource evidence")
    if payload["scope"] != "REPRESENTATIVE_S0_CALIBRATION_ONLY":
        raise ReleaseError("branch resource evidence scope mismatch")
    for key in ("scientific_status", "milestone_status", "theorem_status", "final_status"):
        if payload[key] is not None:
            raise ReleaseError(f"branch resource evidence overclaims {key}")
    binary_path = _machine_nonempty_string(payload["binary"], "branch resource binary")
    lexical_absolute(Path(binary_path))
    if payload["binary_sha256"] != machine["branch_binary"]["sha256"]:
        raise ReleaseError("branch resource/persistent binary mismatch")
    require_sha256(payload["binary_sha256"], "branch resource binary hash")
    for key in (
        "cgroup_limit_bytes", "baseline_conservative_bytes", "task_count",
        "per_process_peak_rss_max_kib",
    ):
        _machine_positive_int(payload[key], f"branch resource {key}")
    if payload["cgroup_limit_bytes"] != FORMAL_MACHINE_REQUIREMENTS["memory_limit_bytes"]:
        raise ReleaseError("branch resource cgroup limit mismatch")
    for name in ("baseline_samples_bytes", "post_samples_bytes"):
        values = payload[name]
        if type(values) is not list or len(values) != 21:
            raise ReleaseError(f"branch resource {name} shape mismatch")
        for value in values:
            _machine_positive_int(value, f"branch resource {name} sample")
    baseline = max(payload["baseline_samples_bytes"])
    if payload["baseline_conservative_bytes"] != baseline:
        raise ReleaseError("branch resource baseline aggregation mismatch")
    plan_records, _ = _machine_plan_records(project_root)
    results = payload["results"]
    public = [(bits, slab) for bits in PRECISIONS for slab in FORMAL_MACHINE_PUBLIC_SLABS]
    if type(results) is not list or len(results) != 6 or payload["task_count"] != 6:
        raise ReleaseError("branch resource must contain exactly six public runs")
    peaks: list[int] = []
    for index, (row, (bits, slab)) in enumerate(zip(results, public, strict=True)):
        context = f"branch resource row {index}"
        exact_keys(row, FORMAL_BRANCH_RESOURCE_RUN_KEYS, context)
        if row["precision_bits"] != bits or row["slab_id"] != slab:
            raise ReleaseError(f"{context} identity/order mismatch")
        for key in ("precision_bits", "argv_count", "returncode", "peak_rss_kib", "stdout_bytes", "stderr_bytes"):
            _machine_nonnegative_int(row[key], f"{context}.{key}")
        for key in ("elapsed_seconds", "user_cpu_seconds", "system_cpu_seconds"):
            _machine_nonnegative_float(row[key], f"{context}.{key}")
        if row["argv_count"] != FORMAL_MACHINE_BRANCH_ARGV_COUNT or row["argv"] != _machine_branch_argv(binary_path, bits, plan_records[slab]):
            raise ReleaseError(f"{context} exact 12-string argv mismatch")
        if (
            row["returncode"] != 0
            or row["peak_rss_kib"] <= 0
            or row["stdout_bytes"] <= 0
            or row["stderr_bytes"] != 0
            or row["abi_verified"] is not True
            or row["terminal_abi_value"] != "BRANCH_CELL_CERTIFIED"
        ):
            raise ReleaseError(f"{context} ABI/resource result mismatch")
        for key in ("stdout_sha256", "stderr_sha256"):
            require_sha256(row[key], f"{context}.{key}")
        if row["stderr_sha256"] != FORMAL_MACHINE_EMPTY_SHA256:
            raise ReleaseError(f"{context} empty stderr hash mismatch")
        peaks.append(row["peak_rss_kib"] * 1024)
    peak = max(peaks)
    if payload["per_process_peak_rss_max_kib"] * 1024 != peak:
        raise ReleaseError("branch resource maximum RSS mismatch")
    _machine_positive_int(payload["sampled_concurrent_peak_bytes"], "branch concurrent peak")
    _machine_nonnegative_int(payload["sampled_concurrent_increment_bytes"], "branch concurrent increment")
    if payload["sampled_concurrent_increment_bytes"] != payload["sampled_concurrent_peak_bytes"] - baseline:
        raise ReleaseError("branch concurrent cgroup increment mismatch")
    admission = exact_keys(payload["admission"], FORMAL_BRANCH_RESOURCE_ADMISSION_KEYS, "branch resource admission")
    for key in (
        "baseline_bytes", "peak_rss_bytes", "workers", "reserve_bytes",
        "limit_bytes", "lhs_bytes",
    ):
        _machine_positive_int(admission[key], f"branch resource admission.{key}")
    _machine_nonnegative_int(
        admission["headroom_bytes"], "branch resource admission.headroom_bytes"
    )
    expected_lhs = baseline + 6 * peak + FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
    if (
        admission["baseline_bytes"] != baseline
        or admission["peak_rss_bytes"] != peak
        or admission["workers"] != 6
        or admission["reserve_bytes"] != FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
        or admission["limit_bytes"] != FORMAL_MACHINE_REQUIREMENTS["memory_admission_limit_bytes"]
        or admission["lhs_bytes"] != expected_lhs
        or admission["headroom_bytes"] != admission["limit_bytes"] - expected_lhs
        or admission["formula"] != "baseline + 6*peak_rss + 8GiB <= 48GiB"
        or admission["passes"] is not (expected_lhs <= admission["limit_bytes"])
    ):
        raise ReleaseError("branch resource admission arithmetic mismatch")
    return {"baseline_bytes": baseline, "peak_rss_bytes": peak}


def _machine_validate_runtime_row(
    row: Any,
    *,
    expected_soname: str,
    context: str,
) -> Mapping[str, Any]:
    exact_keys(row, FORMAL_MACHINE_RUNTIME_ROW_KEYS, context)
    if row["soname"] != expected_soname:
        raise ReleaseError(f"{context} SONAME/order mismatch")
    raw, info, _ = _machine_external_snapshot(row["path"], context)
    _machine_require_mode(row["mode"], info, context)
    if _machine_positive_int(row["size_bytes"], f"{context}.size_bytes") != len(raw):
        raise ReleaseError(f"{context} size does not match live bytes")
    _machine_require_live_hash(raw, row["sha256"], f"{context}.sha256")
    if type(row["build_id"]) is not str or FORMAL_MACHINE_BUILD_ID.fullmatch(row["build_id"]) is None:
        raise ReleaseError(f"{context}.build_id is malformed")
    live_build_id, _, live_soname = _machine_elf_metadata(raw, context)
    if row["build_id"] != live_build_id or live_soname != expected_soname:
        raise ReleaseError(f"{context} live ELF build-id/SONAME mismatch")
    return row


def _machine_recompute_conda_manifest(
    executable_path: str,
) -> tuple[int, str]:
    """Recompute the frozen Python conda-package live-file manifest root."""

    executable = lexical_absolute(Path(executable_path))
    if executable.name != "python3" or executable.parent.name != "bin":
        raise PathContractError("machine Python executable is outside a conda bin layout")
    prefix = executable.parent.parent
    meta_dir = prefix / "conda-meta"
    descriptor = _open_directory(meta_dir)
    os.close(descriptor)
    pattern = re.compile(r"python-3\.12\.3-[A-Za-z0-9_.-]+\.json\Z")
    try:
        all_names = tuple(sorted(
            (entry.name for entry in os.scandir(meta_dir)),
            key=lambda name: name.encode("utf-8"),
        ))
    except UnicodeError as error:
        raise PathContractError("machine Python conda metadata namespace is not UTF-8") from error
    candidates = [name for name in all_names if pattern.fullmatch(name) is not None]
    if len(candidates) != 1:
        raise ReleaseError("machine Python conda metadata is not uniquely identified")
    if _ACTIVE_MACHINE_CONDA_META_NAMESPACES is not None:
        captured = all_names
        previous = _ACTIVE_MACHINE_CONDA_META_NAMESPACES.setdefault(meta_dir, captured)
        if previous != captured:
            raise PathContractError("machine Python conda metadata namespace changed")
    meta_path = lexical_absolute(meta_dir / candidates[0])
    meta_raw, _ = _machine_manifest_file_snapshot(
        meta_path, "machine Python conda metadata"
    )
    metadata = strict_json_loads(meta_raw)
    if (
        type(metadata) is not dict
        or metadata.get("name") != "python"
        or metadata.get("version") != "3.12.3"
    ):
        raise ReleaseError("machine Python conda metadata identity mismatch")
    files = metadata.get("files")
    paths = metadata.get("paths_data", {}).get("paths")
    if (
        type(files) is not list
        or not files
        or not all(type(item) is str for item in files)
        or type(paths) is not list
        or len(paths) != len(files)
    ):
        raise ReleaseError("machine Python conda file manifest is malformed")
    normalized: list[str] = []
    for value in files:
        try:
            relative = safe_relative(value)
        except Exception as error:
            raise PathContractError("unsafe path in Python conda manifest") from error
        normalized.append(relative.as_posix())
    if len(set(normalized)) != len(normalized):
        raise ReleaseError("machine Python conda manifest repeats a file")
    path_names: list[str] = []
    for index, item in enumerate(paths):
        if type(item) is not dict or type(item.get("_path")) is not str:
            raise ReleaseError(f"machine Python conda paths_data[{index}] is malformed")
        path_names.append(item["_path"])
    if set(path_names) != set(normalized) or len(set(path_names)) != len(path_names):
        raise ReleaseError("machine Python conda files/paths_data disagreement")
    rows: list[dict[str, Any]] = []
    for relative in normalized:
        target = lexical_absolute(prefix / Path(PurePosixPath(relative)))
        info = os.lstat(target)
        if stat.S_ISREG(info.st_mode):
            raw, info = _machine_manifest_file_snapshot(
                target, f"machine Python conda file {relative}"
            )
            kind = "REGULAR"
        elif stat.S_ISLNK(info.st_mode):
            raw, info = _machine_manifest_symlink_snapshot(
                target, f"machine Python conda link {relative}"
            )
            kind = "SYMLINK"
        else:
            raise PathContractError(
                f"machine Python conda entry is not a file/link: {relative}"
            )
        rows.append({
            "kind": kind,
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "path": relative,
            "sha256": sha256_bytes(raw),
            "size_bytes": len(raw),
        })
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    return len(rows), sha256_bytes(canonical_json_bytes(rows))


def _machine_recompute_python_flint_manifest(
    record_path: str,
    record_raw: bytes,
) -> tuple[int, str]:
    """Replay python-flint's 139-file live RECORD manifest exactly."""

    record = lexical_absolute(Path(record_path))
    site_packages = record.parents[1]
    try:
        parsed = list(csv.reader(io.StringIO(record_raw.decode("utf-8"), newline="")))
    except (UnicodeDecodeError, csv.Error) as error:
        raise ReleaseError("python-flint RECORD is not strict UTF-8 CSV") from error
    if not parsed:
        raise ReleaseError("python-flint RECORD is empty")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, record_row in enumerate(parsed):
        if len(record_row) != 3:
            raise ReleaseError(f"python-flint RECORD row {index} is malformed")
        relative_raw, declared_digest, declared_size = record_row
        try:
            relative = safe_relative(relative_raw)
        except Exception as error:
            raise PathContractError("unsafe python-flint RECORD path") from error
        relative_text = relative.as_posix()
        if relative_text in seen:
            raise ReleaseError("python-flint RECORD repeats a path")
        seen.add(relative_text)
        target = lexical_absolute(site_packages / Path(relative))
        raw, info = _machine_manifest_file_snapshot(
            target, f"python-flint installed file {relative_text}"
        )
        if not stat.S_ISREG(info.st_mode):
            raise PathContractError("python-flint RECORD target is not regular")
        digest = sha256_bytes(raw)
        if declared_digest:
            if not declared_digest.startswith("sha256="):
                raise ReleaseError("python-flint RECORD uses a non-SHA256 digest")
            encoded = declared_digest.removeprefix("sha256=")
            try:
                decoded = base64.urlsafe_b64decode(
                    encoded + "=" * (-len(encoded) % 4)
                )
            except Exception as error:
                raise ReleaseError("python-flint RECORD digest is malformed") from error
            if decoded.hex() != digest or declared_size != str(len(raw)):
                raise ReleaseError("python-flint RECORD differs from installed bytes")
        elif declared_size != "":
            raise ReleaseError("python-flint RECORD has size without digest")
        rows.append({
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "path": relative_text,
            "sha256": digest,
            "size_bytes": len(raw),
        })
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    return len(rows), sha256_bytes(canonical_json_bytes(rows))


def _machine_git_blob_sha1(raw: bytes) -> str:
    framed = b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw
    return hashlib.sha1(framed, usedforsecurity=False).hexdigest()


def _machine_read_git_index(
    checkout: Path,
) -> tuple[list[tuple[str, int, str]], bytes]:
    """Read a v2 Git index and return ordered path/mode/blob bindings."""

    git_dir = checkout / ".git"
    descriptor = _open_directory(git_dir)
    os.close(descriptor)
    index_raw, _ = _machine_manifest_file_snapshot(
        git_dir / "index", "CAPD Git index"
    )
    if len(index_raw) < 32 or index_raw[:4] != b"DIRC":
        raise ReleaseError("CAPD Git index header is malformed")
    version, count = struct.unpack_from(">II", index_raw, 4)
    if version != 2 or count <= 0:
        raise ReleaseError("CAPD Git index is not a nonempty v2 index")
    body, checksum = index_raw[:-20], index_raw[-20:]
    if hashlib.sha1(body, usedforsecurity=False).digest() != checksum:
        raise ReleaseError("CAPD Git index checksum mismatch")
    cursor = 12
    records: list[tuple[str, int, str]] = []
    fixed_format = ">LLLLLLLLLL20sH"
    fixed_size = struct.calcsize(fixed_format)
    for index in range(count):
        entry_start = cursor
        if cursor + fixed_size > len(body):
            raise ReleaseError(f"CAPD Git index entry {index} is truncated")
        fields = struct.unpack_from(fixed_format, body, cursor)
        mode, object_id, flags = fields[6], fields[10].hex(), fields[11]
        cursor += fixed_size
        if flags & 0xF000:
            raise ReleaseError("CAPD Git index uses staged/extended entries")
        try:
            path_end = body.index(b"\x00", cursor)
        except ValueError as error:
            raise ReleaseError("CAPD Git index path is unterminated") from error
        path_raw = body[cursor:path_end]
        try:
            path_text = path_raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ReleaseError("CAPD Git index path is not UTF-8") from error
        relative = safe_relative(path_text).as_posix()
        encoded_length = flags & 0x0FFF
        if encoded_length != min(len(path_raw), 0x0FFF):
            raise ReleaseError("CAPD Git index path-length flag mismatch")
        if mode not in (0o100644, 0o100755, 0o120000):
            raise ReleaseError("CAPD Git index contains an unsupported mode")
        cursor = path_end + 1
        while (cursor - entry_start) % 8:
            if cursor >= len(body) or body[cursor] != 0:
                raise ReleaseError("CAPD Git index entry padding is malformed")
            cursor += 1
        records.append((relative, mode, object_id))
    # Index extensions are checksum-covered.  Only optional all-uppercase
    # signatures are accepted; required lowercase extensions fail closed.
    while cursor < len(body):
        if cursor + 8 > len(body):
            raise ReleaseError("CAPD Git index extension is truncated")
        signature = body[cursor : cursor + 4]
        extension_size = struct.unpack_from(">I", body, cursor + 4)[0]
        cursor += 8
        if (
            re.fullmatch(rb"[A-Z]{4}", signature) is None
            or extension_size > len(body) - cursor
        ):
            raise ReleaseError("CAPD Git index extension is malformed/required")
        cursor += extension_size
    if len({path for path, _, _ in records}) != len(records) or records != sorted(
        records, key=lambda item: item[0].encode("utf-8")
    ):
        raise ReleaseError("CAPD Git index paths are duplicate or unordered")
    return records, index_raw


def _machine_capd_namespace_signature(
    checkout: Path,
    tracked: frozenset[str],
) -> tuple[tuple[str, str, tuple[int, int, int, int, int]], ...]:
    """Snapshot the clean source namespace, excluding only .git/build-mp."""

    expected_directories: set[str] = set()
    for relative in tracked:
        parent = PurePosixPath(relative).parent
        while parent != PurePosixPath("."):
            expected_directories.add(parent.as_posix())
            parent = parent.parent
    observed_files: set[str] = set()
    observed_directories: set[str] = set()
    rows: list[tuple[str, str, tuple[int, int, int, int, int]]] = []
    pending = [checkout]
    while pending:
        directory = pending.pop()
        entries = sorted(os.scandir(directory), key=lambda item: os.fsencode(item.name))
        for entry in entries:
            relative = Path(entry.path).relative_to(checkout).as_posix()
            if relative in {".git", "build-mp"}:
                continue
            info = entry.stat(follow_symlinks=False)
            if stat.S_ISDIR(info.st_mode):
                observed_directories.add(relative)
                rows.append((relative, "DIRECTORY", _fingerprint(info)))
                pending.append(Path(entry.path))
            elif stat.S_ISREG(info.st_mode):
                observed_files.add(relative)
                rows.append((relative, "REGULAR", _fingerprint(info)))
            elif stat.S_ISLNK(info.st_mode):
                observed_files.add(relative)
                rows.append((relative, "SYMLINK", _fingerprint(info)))
            else:
                raise PathContractError(f"unsupported CAPD namespace entry: {relative}")
    if observed_files != set(tracked) or observed_directories != expected_directories:
        raise PathContractError("CAPD checkout has tracked/untracked namespace drift")
    rows.sort(key=lambda row: row[0].encode("utf-8"))
    return tuple(rows)


def _machine_git_index_tree_oid(records: list[tuple[str, int, str]]) -> str:
    """Recursively reproduce Git's tree object from stage-zero index rows."""

    def node() -> dict[str, dict[str, Any]]:
        return {"files": {}, "directories": {}}

    root = node()
    for relative, mode, object_id in records:
        parts = PurePosixPath(relative).parts
        current = root
        for part in parts[:-1]:
            if part in current["files"]:
                raise ReleaseError("CAPD Git index has a file/directory prefix collision")
            current = current["directories"].setdefault(part, node())
        name = parts[-1]
        if name in current["files"] or name in current["directories"]:
            raise ReleaseError("CAPD Git index has a duplicate tree entry")
        current["files"][name] = (mode, object_id)

    def digest_tree(current: dict[str, dict[str, Any]]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, (mode, object_id) in current["files"].items():
            name_raw = name.encode("utf-8")
            payload = (
                f"{mode:06o}".encode("ascii")
                + b" " + name_raw + b"\x00" + bytes.fromhex(object_id)
            )
            entries.append((name_raw, payload))
        for name, child in current["directories"].items():
            name_raw = name.encode("utf-8")
            child_id = digest_tree(child)
            payload = b"40000 " + name_raw + b"\x00" + bytes.fromhex(child_id)
            entries.append((name_raw + b"/", payload))
        content = b"".join(payload for _, payload in sorted(entries))
        framed = b"tree " + str(len(content)).encode("ascii") + b"\x00" + content
        return hashlib.sha1(framed, usedforsecurity=False).hexdigest()

    return digest_tree(root)


def _machine_inflate_git_object(raw: bytes, context: str) -> bytes:
    inflater = zlib.decompressobj()
    try:
        inflated = inflater.decompress(raw, 4 * 1024 * 1024 + 1)
    except zlib.error as error:
        raise ReleaseError(f"{context} zlib stream is malformed") from error
    if (
        not inflater.eof
        or len(inflated) > 4 * 1024 * 1024
        or inflater.unconsumed_tail
    ):
        raise ReleaseError(f"{context} zlib stream exceeds its exact bound")
    return inflated


def _machine_parse_git_object(
    framed: bytes,
    expected_oid: str,
    expected_kind: bytes,
    context: str,
) -> bytes:
    if hashlib.sha1(framed, usedforsecurity=False).hexdigest() != expected_oid:
        raise ReleaseError(f"{context} Git object ID mismatch")
    try:
        header, payload = framed.split(b"\x00", 1)
        kind, size_raw = header.split(b" ", 1)
        size = int(size_raw.decode("ascii"))
    except (ValueError, UnicodeDecodeError) as error:
        raise ReleaseError(f"{context} Git object header is malformed") from error
    if kind != expected_kind or str(size).encode("ascii") != size_raw or size != len(payload):
        raise ReleaseError(f"{context} Git object kind/size mismatch")
    return payload


def _machine_git_packed_object(
    git_dir: Path,
    object_id: str,
) -> bytes | None:
    """Resolve a non-delta object through a checksum-verified pack index v2."""

    pack_dir = git_dir / "objects/pack"
    if not pack_dir.is_dir():
        return None
    index_names = sorted(
        entry.name
        for entry in os.scandir(pack_dir)
        if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name) is not None
    )
    matches: list[bytes] = []
    needle = bytes.fromhex(object_id)
    for index_name in index_names:
        index_raw, _ = _machine_manifest_file_snapshot(
            pack_dir / index_name, f"CAPD Git pack index {index_name}"
        )
        if (
            len(index_raw) < 8 + 256 * 4 + 40
            or index_raw[:4] != b"\xfftOc"
            or struct.unpack_from(">I", index_raw, 4)[0] != 2
            or hashlib.sha1(index_raw[:-20], usedforsecurity=False).digest()
            != index_raw[-20:]
        ):
            raise ReleaseError("CAPD Git pack index identity/checksum mismatch")
        fanout = struct.unpack_from(">256I", index_raw, 8)
        if any(left > right for left, right in zip(fanout, fanout[1:])):
            raise ReleaseError("CAPD Git pack index fanout is unordered")
        count = fanout[-1]
        names_offset = 8 + 256 * 4
        crc_offset = names_offset + count * 20
        offsets_offset = crc_offset + count * 4
        large_offset = offsets_offset + count * 4
        if large_offset + 40 > len(index_raw):
            raise ReleaseError("CAPD Git pack index tables are truncated")
        lower = fanout[needle[0] - 1] if needle[0] else 0
        upper = fanout[needle[0]]
        found_index: int | None = None
        while lower < upper:
            middle = (lower + upper) // 2
            candidate = index_raw[
                names_offset + middle * 20 : names_offset + (middle + 1) * 20
            ]
            if candidate < needle:
                lower = middle + 1
            else:
                upper = middle
        if lower < count and index_raw[
            names_offset + lower * 20 : names_offset + (lower + 1) * 20
        ] == needle:
            found_index = lower
        if found_index is None:
            continue
        packed_offset = struct.unpack_from(">I", index_raw, offsets_offset + found_index * 4)[0]
        if packed_offset & 0x80000000:
            large_index = packed_offset & 0x7FFFFFFF
            location = large_offset + large_index * 8
            if location + 8 > len(index_raw) - 40:
                raise ReleaseError("CAPD Git pack large-offset table is malformed")
            packed_offset = struct.unpack_from(">Q", index_raw, location)[0]
        pack_name = index_name[:-4] + ".pack"
        pack_raw, _ = _machine_manifest_file_snapshot(
            pack_dir / pack_name, f"CAPD Git pack {pack_name}"
        )
        if (
            len(pack_raw) < 32
            or pack_raw[:4] != b"PACK"
            or struct.unpack_from(">I", pack_raw, 4)[0] not in (2, 3)
            or hashlib.sha1(pack_raw[:-20], usedforsecurity=False).digest()
            != pack_raw[-20:]
            or index_raw[-40:-20] != pack_raw[-20:]
            or packed_offset < 12
            or packed_offset >= len(pack_raw) - 20
        ):
            raise ReleaseError("CAPD Git pack identity/checksum mismatch")
        cursor = packed_offset
        first = pack_raw[cursor]
        cursor += 1
        object_type = (first >> 4) & 7
        object_size = first & 0x0F
        shift = 4
        current = first
        while current & 0x80:
            if cursor >= len(pack_raw) - 20 or shift > 60:
                raise ReleaseError("CAPD Git packed-object header is malformed")
            current = pack_raw[cursor]
            cursor += 1
            object_size |= (current & 0x7F) << shift
            shift += 7
        if object_type != 1:  # OBJ_COMMIT; delta commits fail closed.
            raise ReleaseError("CAPD HEAD commit is stored as an unsupported Git delta")
        payload = _machine_inflate_git_object(
            pack_raw[cursor:-20], "CAPD packed HEAD commit"
        )
        if len(payload) != object_size:
            raise ReleaseError("CAPD packed HEAD commit size mismatch")
        framed = b"commit " + str(len(payload)).encode("ascii") + b"\x00" + payload
        matches.append(framed)
    if len(matches) > 1:
        raise ReleaseError("CAPD HEAD object is ambiguously packed")
    return matches[0] if matches else None


def _machine_git_commit_tree(git_dir: Path, commit: str) -> str:
    loose_path = git_dir / "objects" / commit[:2] / commit[2:]
    framed: bytes | None = None
    if loose_path.exists():
        loose_raw, _ = _machine_manifest_file_snapshot(
            loose_path, "CAPD loose HEAD commit"
        )
        inflated = _machine_inflate_git_object(loose_raw, "CAPD loose HEAD commit")
        framed = inflated
    packed = _machine_git_packed_object(git_dir, commit)
    if framed is not None and packed is not None:
        raise ReleaseError("CAPD HEAD object is ambiguously loose and packed")
    framed = framed if framed is not None else packed
    if framed is None:
        raise ReleaseError("CAPD HEAD commit object is unavailable")
    payload = _machine_parse_git_object(
        framed, commit, b"commit", "CAPD HEAD commit"
    )
    match = re.match(rb"tree ([0-9a-f]{40})\n", payload)
    if match is None:
        raise ReleaseError("CAPD HEAD commit has no canonical tree header")
    return match.group(1).decode("ascii")


def _machine_recompute_capd_tree(checkout: Path) -> tuple[str, str]:
    """Replay detached HEAD, the Git index, and every tracked source byte."""

    head_raw, _ = _machine_manifest_file_snapshot(
        checkout / ".git/HEAD", "CAPD detached Git HEAD"
    )
    if re.fullmatch(rb"[0-9a-f]{40}\n", head_raw) is None:
        raise ReleaseError("CAPD Git HEAD is not detached at an exact commit")
    commit = head_raw[:-1].decode("ascii")
    records, _ = _machine_read_git_index(checkout)
    index_tree = _machine_git_index_tree_oid(records)
    head_tree = _machine_git_commit_tree(checkout / ".git", commit)
    if index_tree != head_tree:
        raise ReleaseError("CAPD Git index tree differs from detached HEAD tree")
    rows: list[dict[str, Any]] = []
    for relative, git_mode, object_id in records:
        target = lexical_absolute(checkout / Path(PurePosixPath(relative)))
        info = os.lstat(target)
        if git_mode == 0o120000:
            raw, info = _machine_manifest_symlink_snapshot(
                target, f"CAPD tracked symlink {relative}"
            )
            if not stat.S_ISLNK(info.st_mode):
                raise PathContractError("CAPD index symlink is not live as a symlink")
        else:
            raw, info = _machine_manifest_file_snapshot(
                target, f"CAPD tracked file {relative}"
            )
            expected_executable = git_mode == 0o100755
            if (
                not stat.S_ISREG(info.st_mode)
                or bool(stat.S_IMODE(info.st_mode) & 0o111) is not expected_executable
            ):
                raise PathContractError("CAPD tracked file mode differs from Git index")
        if _machine_git_blob_sha1(raw) != object_id:
            raise ReleaseError("CAPD tracked bytes differ from Git index object ID")
        rows.append({
            "git_blob_sha1": object_id,
            "mode": f"{git_mode:06o}",
            "path": relative,
            "sha256": sha256_bytes(raw),
            "size_bytes": len(raw),
        })
    tracked = frozenset(path for path, _, _ in records)
    namespace = _machine_capd_namespace_signature(checkout, tracked)
    if _ACTIVE_MACHINE_CAPD_NAMESPACES is not None:
        captured = (tracked, namespace)
        previous = _ACTIVE_MACHINE_CAPD_NAMESPACES.setdefault(checkout, captured)
        if previous != captured:
            raise PathContractError("CAPD namespace changed between live replays")
    return commit, sha256_bytes(canonical_json_bytes(rows))


def _machine_validate_python_arb(
    machine: Mapping[str, Any],
) -> None:
    python = exact_keys(machine["python_arb"], FORMAL_MACHINE_PYTHON_ARB_KEYS, "machine python_arb")
    root_keys = (
        "conda_installed_manifest_root_sha256",
        "python_flint_record_sha256",
        "python_flint_installed_manifest_root_sha256",
    )
    roots = [require_sha256(python[key], f"machine python_arb.{key}") for key in root_keys]
    if len(set(roots)) != len(roots):
        raise ReleaseError("machine Python manifest roots must be pairwise distinct")
    executable_raw, _, resolved = _machine_external_snapshot(
        python["executable_path"], "machine Python executable"
    )
    _machine_require_live_hash(
        executable_raw, python["executable_sha256"], "machine Python executable"
    )
    if (
        python["implementation"] != "CPython"
        or python["python_version"] != FORMAL_MACHINE_PYTHON_VERSION
        or python["python_flint_version"] != "0.9.0"
        or python["flint_version"] != "3.6.0"
        or python["arb_version"] != "FLINT-3.6.0"
        or python["conda_manifest_algorithm"]
        != FORMAL_MACHINE_CONDA_MANIFEST_ALGORITHM
        or python["python_flint_record_sha256"]
        != FORMAL_MACHINE_PYTHON_FLINT_RECORD_SHA256
        or python["python_flint_installed_manifest_root_sha256"]
        != FORMAL_MACHINE_PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256
    ):
        raise ReleaseError("machine Python-Arb identity mismatch")
    conda_count, conda_root = _machine_recompute_conda_manifest(
        python["executable_path"]
    )
    if (
        _machine_positive_int(
            python["conda_manifest_file_count"],
            "machine python_arb.conda_manifest_file_count",
        )
        != conda_count
        or require_sha256(
            python["conda_installed_manifest_root_sha256"],
            "machine python_arb.conda_installed_manifest_root_sha256",
        )
        != conda_root
    ):
        raise ReleaseError("machine Python conda manifest live replay mismatch")
    _machine_validate_file_binding(python["arb_extension"], "machine Arb extension")
    _machine_validate_file_binding(python["fmpq_extension"], "machine fmpq extension")
    bundled = python["bundled_libraries"]
    if type(bundled) is not list or len(bundled) != len(FORMAL_MACHINE_PYTHON_BUNDLED_SONAMES):
        raise ReleaseError("machine Python bundled library list mismatch")
    for index, (binding, soname) in enumerate(
        zip(bundled, FORMAL_MACHINE_PYTHON_BUNDLED_SONAMES, strict=True)
    ):
        _machine_validate_runtime_row(
            binding,
            expected_soname=soname,
            context=f"machine Python bundled library {index}",
        )


def _machine_validate_capd(machine: Mapping[str, Any]) -> list[str]:
    capd = exact_keys(machine["capd"], FORMAL_MACHINE_CAPD_KEYS, "machine CAPD")
    checkout = lexical_absolute(Path(_machine_nonempty_string(capd["checkout_path"], "CAPD checkout path")))
    descriptor = _open_directory(checkout)
    os.close(descriptor)
    if type(capd["commit"]) is not str or FORMAL_MACHINE_GIT_COMMIT.fullmatch(capd["commit"]) is None:
        raise ReleaseError("machine CAPD commit is malformed")
    if (
        capd["tree_algorithm"] != FORMAL_MACHINE_CAPD_TREE_ALGORITHM
        or capd["clean"] is not True
    ):
        raise ReleaseError("machine CAPD checkout is not recorded clean")
    live_commit, live_tree = _machine_recompute_capd_tree(checkout)
    if (
        capd["commit"] != live_commit
        or require_sha256(capd["tree_sha256"], "machine CAPD tree evidence")
        != live_tree
    ):
        raise ReleaseError("machine CAPD commit/tree live replay mismatch")
    cache_raw, _, cache_path = _machine_external_snapshot(capd["cmake_cache_path"], "CAPD CMake cache")
    config_raw, _, config_path = _machine_external_snapshot(capd["config_path"], "CAPD config helper")
    if (
        cache_path != checkout / "build-mp/CMakeCache.txt"
        or config_path != checkout / "build-mp/bin/capd-config"
    ):
        raise PathContractError("CAPD cache/config paths do not match the pinned layout")
    _machine_require_live_hash(cache_raw, capd["cmake_cache_sha256"], "CAPD CMake cache")
    _machine_require_live_hash(config_raw, capd["config_sha256"], "CAPD config helper")
    raw_flags = _machine_nonempty_string(capd["raw_flags"], "CAPD raw flags")
    if not raw_flags.endswith("\n") or sha256_bytes(raw_flags.encode("utf-8")) != require_sha256(
        capd["raw_flags_sha256"], "CAPD raw flags hash"
    ):
        raise ReleaseError("machine CAPD raw flags hash/terminator mismatch")
    try:
        tokens = shlex.split(raw_flags)
    except ValueError as error:
        raise ReleaseError("machine CAPD raw flags cannot be tokenized") from error
    expected_tokens = [
        "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
        "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
        "-DFILIB_HAVE_SSE",
        f"-I{checkout}/capdDynSys/include",
        f"-I{checkout}/capdAlg/include",
        f"-I{checkout}/capdAux/include",
        f"-I{checkout}/capdExt/include",
        f"-I{checkout}/capdExt/filibsrc",
        f"-L{checkout}/build-mp",
        f"-L{checkout}/build-mp/capdExt/filibsrc",
        "-lcapd", "-lfilib", "-lmpfr", "-lgmp",
    ]
    if tokens != expected_tokens:
        raise ReleaseError("machine CAPD ordered flag contract mismatch")
    _machine_validate_file_binding(
        capd["libcapd"], "machine libcapd", allow_null_build_id=True
    )
    _machine_validate_file_binding(
        capd["libfilib"], "machine libfilib", allow_null_build_id=True
    )
    if (
        capd["libcapd"]["path"] != str(checkout / "build-mp/libcapd.a")
        or capd["libfilib"]["path"]
        != str(checkout / "build-mp/capdExt/filibsrc/libfilib.a")
    ):
        raise PathContractError("CAPD archive paths do not match the pinned layout")
    if capd["libcapd"]["build_id"] is not None or capd["libfilib"]["build_id"] is not None:
        raise ReleaseError("static CAPD archives must have null build_id")
    return tokens


def _machine_validate_compiler_and_binary(
    project_root: Path,
    machine: Mapping[str, Any],
    capd_tokens: list[str],
) -> tuple[bytes, Mapping[str, Any]]:
    compiler = exact_keys(machine["compiler"], FORMAL_MACHINE_COMPILER_KEYS, "machine compiler")
    compiler_raw, _, _ = _machine_external_snapshot(
        compiler["executable_path"], "machine compiler executable"
    )
    _machine_require_live_hash(
        compiler_raw, compiler["executable_sha256"], "machine compiler executable"
    )
    if (
        _machine_nonempty_string(compiler["version"], "machine compiler version")
        != FORMAL_MACHINE_COMPILER_VERSION
    ):
        raise ReleaseError("machine compiler version mismatch")
    branch = exact_keys(
        machine["branch_binary"], FORMAL_MACHINE_BRANCH_BINARY_KEYS,
        "machine branch binary",
    )
    if branch["path"] != FORMAL_MACHINE_BRANCH_BINARY or branch["source_path"] != FORMAL_MACHINE_BRANCH_SOURCE:
        raise ReleaseError("machine branch source/binary path mismatch")
    binary_raw, binary_info, _ = _machine_project_snapshot(
        project_root, branch["path"], "machine persistent branch binary"
    )
    source_raw, _, _ = _machine_project_snapshot(
        project_root, branch["source_path"], "machine branch source"
    )
    _machine_require_live_hash(binary_raw, branch["sha256"], "machine persistent branch binary")
    _machine_require_live_hash(source_raw, branch["source_sha256"], "machine branch source")
    _machine_positive_int(branch["size_bytes"], "machine branch binary.size_bytes")
    if (
        branch["size_bytes"] != len(binary_raw)
        or type(branch["executable_mode"]) is not int
        or branch["executable_mode"] != 0o755
        or stat.S_IMODE(binary_info.st_mode) != branch["executable_mode"]
        or not binary_raw.startswith(b"\x7fELF")
        or branch["elf_sha256"] != branch["sha256"]
    ):
        raise ReleaseError("machine persistent branch binary metadata mismatch")
    live_build_id, live_needed, live_soname = _machine_elf_metadata(
        binary_raw, "machine persistent branch binary"
    )
    if (
        branch["build_id"] != live_build_id
        or live_soname is not None
        or live_needed != FORMAL_MACHINE_DT_NEEDED
        or branch["dt_needed"] != live_needed
        or sha256_bytes(
        canonical_json_bytes(branch["dt_needed"])
        ) != require_sha256(branch["dt_needed_sha256"], "machine DT_NEEDED hash")
    ):
        raise ReleaseError("machine persistent branch DT_NEEDED mismatch")
    build = exact_keys(
        compiler["build_record"], FORMAL_MACHINE_BUILD_RECORD_KEYS,
        "machine compiler build record",
    )
    if build["cwd"] != str(project_root) or build["umask"] != "0022":
        raise ReleaseError("machine build working-directory/umask mismatch")
    environment = build["environment"]
    expected_environment = {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}
    if not exact_json_equal(environment, expected_environment):
        raise ReleaseError("machine build environment is not exact and pinned")
    argv = build["argv"]
    expected_argv = [
        compiler["executable_path"], "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(project_file(project_root, FORMAL_MACHINE_BRANCH_SOURCE)),
        *capd_tokens, "-o",
        str(project_file(project_root, FORMAL_MACHINE_BRANCH_BINARY)),
    ]
    if argv != expected_argv or sha256_bytes(canonical_json_bytes(argv)) != require_sha256(
        build["argv_sha256"], "machine build argv hash"
    ):
        raise ReleaseError("machine exact build argv mismatch")
    if (
        type(build["return_code"]) is not int
        or build["return_code"] != 0
        or build["stdout"] != ""
        or build["stderr"] != ""
        or build["stdout_sha256"] != FORMAL_MACHINE_EMPTY_SHA256
        or build["stderr_sha256"] != FORMAL_MACHINE_EMPTY_SHA256
    ):
        raise ReleaseError("machine compiler transcript mismatch")
    return binary_raw, branch


def _machine_validate_runtime_libraries(
    machine: Mapping[str, Any],
) -> None:
    runtime = exact_keys(
        machine["runtime_libraries"], FORMAL_MACHINE_RUNTIME_KEYS,
        "machine runtime libraries",
    )
    python_rows = runtime["python_bundled"]
    capd_rows = runtime["capd_system"]
    if type(python_rows) is not list or len(python_rows) != len(FORMAL_MACHINE_PYTHON_BUNDLED_SONAMES):
        raise ReleaseError("machine Python runtime closure mismatch")
    if type(capd_rows) is not list or len(capd_rows) != len(FORMAL_MACHINE_CAPD_SYSTEM_SONAMES):
        raise ReleaseError("machine CAPD runtime closure mismatch")
    for index, (row, soname) in enumerate(zip(python_rows, FORMAL_MACHINE_PYTHON_BUNDLED_SONAMES, strict=True)):
        _machine_validate_runtime_row(
            row, expected_soname=soname, context=f"machine Python runtime {index}"
        )
    for index, (row, soname) in enumerate(zip(capd_rows, FORMAL_MACHINE_CAPD_SYSTEM_SONAMES, strict=True)):
        _machine_validate_runtime_row(
            row, expected_soname=soname, context=f"machine CAPD runtime {index}"
        )
    for domain, rows in (("Python", python_rows), ("CAPD", capd_rows)):
        paths = [row["path"] for row in rows]
        if len(set(paths)) != len(paths):
            raise ReleaseError(f"machine {domain} runtime contains duplicate paths")
    python_bindings = machine["python_arb"]["bundled_libraries"]
    if not exact_json_equal(python_bindings, python_rows):
        raise ReleaseError("machine Python runtime duplicate binding mismatch")
    if machine["branch_binary"]["runtime_libraries_sha256"] != sha256_bytes(
        canonical_json_bytes(runtime)
    ):
        raise ReleaseError("machine branch runtime closure hash mismatch")


def _machine_validate_filesystem(project_root: Path, machine: Mapping[str, Any]) -> None:
    fs = exact_keys(machine["filesystem"], FORMAL_MACHINE_FILESYSTEM_KEYS, "machine filesystem")
    if fs["project_root"] != str(project_root):
        raise ReleaseError("machine filesystem project root mismatch")
    expected_parent = str(project_root / "results")
    if fs["result_parent"] != expected_parent or fs["operational_parent"] != expected_parent:
        raise ReleaseError("machine filesystem parent mismatch")
    observed: list[int] = []
    for key in ("project_root", "result_parent", "operational_parent"):
        path = lexical_absolute(Path(fs[key]))
        descriptor = _open_directory(path)
        try:
            observed.append(os.fstat(descriptor).st_dev)
        finally:
            os.close(descriptor)
    for key in ("project_device_id", "result_device_id", "operational_device_id"):
        _machine_positive_int(fs[key], f"machine filesystem.{key}")
    if (
        fs["same_filesystem"] is not True
        or len(set(observed)) != 1
        or [fs["project_device_id"], fs["result_device_id"], fs["operational_device_id"]] != observed
    ):
        raise ReleaseError("machine filesystem live device mismatch")
    current_free = os.statvfs(project_root / "results").f_bavail * os.statvfs(
        project_root / "results"
    ).f_frsize
    if current_free < FORMAL_MACHINE_REQUIREMENTS["launch_free_bytes"]:
        raise ReleaseError("machine filesystem no longer passes live launch gate")


def _validate_formal_machine_freeze(
    project_root: Path,
    machine: Any,
    *,
    expected_role_hashes: Mapping[str, str] | None,
) -> Mapping[str, Any]:
    exact_keys(machine, FORMAL_MACHINE_KEYS, "formal machine freeze")
    if (
        machine["schema_version"] != 1
        or type(machine["schema_version"]) is not int
        or machine["protocol_id"] != PROTOCOL_ID
        or machine["artifact_role"] != "MACHINE_FREEZE"
        or machine["status"] != "FROZEN_FOR_PRODUCTION"
        or machine["authority"] != "MACHINE_ADMISSION_ONLY"
        or machine["scientific_licensing_enabled"] is not True
        or machine["production_authorized"] is not False
        or machine["claim_boundary"] != FORMAL_MACHINE_CLAIM_BOUNDARY
    ):
        raise ReleaseError("formal machine-freeze identity/authority mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if machine[key] is not None:
            raise ReleaseError(f"formal machine freeze overclaims {key}")
    capture = exact_keys(machine["capture"], FORMAL_MACHINE_CAPTURE_KEYS, "machine capture")
    timestamp = _machine_nonempty_string(capture["captured_at_utc"], "machine capture timestamp")
    if FORMAL_MACHINE_TIMESTAMP.fullmatch(timestamp) is None:
        raise ReleaseError("machine capture timestamp is not exact UTC seconds")
    try:
        capture_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError as error:
        raise ReleaseError("machine capture timestamp is not a calendar time") from error
    try:
        uptime_text = Path("/proc/uptime").read_text(encoding="ascii").split()[0]
        uptime_seconds = Decimal(uptime_text)
    except (OSError, UnicodeError, IndexError, ArithmeticError) as error:
        raise ReleaseError("live boot uptime is unavailable/malformed") from error
    now = datetime.now(timezone.utc)
    # A capture belongs to the live boot and cannot come from the future.  Five
    # minutes allows wall-clock discipline around boot/capture without making a
    # stale record from an earlier boot reusable.
    tolerance_seconds = 300.0
    age_seconds = (now - capture_time).total_seconds()
    if age_seconds < -tolerance_seconds or age_seconds > float(uptime_seconds) + tolerance_seconds:
        raise ReleaseError("machine capture timestamp is outside the live boot window")
    if capture["capture_tool_path"] != FORMAL_MACHINE_CAPTURE_TOOL:
        raise ReleaseError("machine capture tool is not the frozen scheduler role")
    capture_raw, _, _ = _machine_project_snapshot(
        project_root, capture["capture_tool_path"], "machine capture tool"
    )
    _machine_require_live_hash(capture_raw, capture["capture_tool_sha256"], "machine capture tool")
    boot_raw = _machine_boot_id_bytes()
    if sha256_bytes(boot_raw) != require_sha256(capture["boot_id_sha256"], "machine boot ID hash"):
        raise ReleaseError("machine boot ID changed after capture")
    requirements = exact_keys(
        machine["machine_requirements"], FORMAL_MACHINE_REQUIREMENT_KEYS,
        "machine requirements",
    )
    if not exact_json_equal(requirements, FORMAL_MACHINE_REQUIREMENTS):
        raise ReleaseError("formal machine requirements differ from protocol")
    observations = exact_keys(
        machine["machine_observations"], FORMAL_MACHINE_OBSERVATION_KEYS,
        "machine observations",
    )
    for key, value in observations.items():
        _machine_positive_int(value, f"machine observations.{key}")
    if (
        observations["logical_cpu_count"] != requirements["logical_cpu_count"]
        or observations["memory_limit_bytes"] != requirements["memory_limit_bytes"]
        or len(os.sched_getaffinity(0)) != requirements["logical_cpu_count"]
    ):
        raise ReleaseError("machine CPU/memory observation mismatch")
    memory_limit_path = Path("/sys/fs/cgroup/memory/memory.limit_in_bytes")
    if int(memory_limit_path.read_text(encoding="ascii").strip()) != requirements["memory_limit_bytes"]:
        raise ReleaseError("live cgroup memory limit mismatch")
    _machine_validate_python_arb(machine)
    capd_tokens = _machine_validate_capd(machine)
    binary_raw, branch_binding = _machine_validate_compiler_and_binary(
        project_root, machine, capd_tokens
    )
    _machine_validate_runtime_libraries(machine)
    resource = exact_keys(
        machine["resource_evidence"], FORMAL_MACHINE_RESOURCE_EVIDENCE_KEYS,
        "machine resource evidence",
    )
    for key in ("static_payload_raw_utf8", "branch_payload_raw_utf8"):
        if type(resource[key]) is not str or "\x00" in resource[key]:
            raise ReleaseError(f"machine resource evidence {key} must be exact UTF-8 text")
    static_raw = resource["static_payload_raw_utf8"].encode("utf-8")
    branch_raw = resource["branch_payload_raw_utf8"].encode("utf-8")
    if sha256_bytes(static_raw) != require_sha256(
        resource["static_payload_sha256"], "static resource payload hash"
    ):
        raise ReleaseError("static resource raw-byte hash mismatch")
    if sha256_bytes(branch_raw) != require_sha256(
        resource["branch_payload_sha256"], "branch resource payload hash"
    ):
        raise ReleaseError("branch resource raw-byte hash mismatch")
    if resource["persistent_binary_sha256"] != branch_binding["sha256"]:
        raise ReleaseError("resource evidence persistent binary transfer mismatch")
    require_sha256(resource["persistent_binary_sha256"], "resource persistent binary hash")
    static_metrics = _machine_validate_static_resource(project_root, static_raw, machine)
    branch_metrics = _machine_validate_branch_resource(project_root, branch_raw, machine)
    baseline = max(static_metrics["baseline_bytes"], branch_metrics["baseline_bytes"])
    if (
        observations["idle_baseline_rss_bytes"] != baseline
        or observations["representative_static_peak_rss_bytes"] != static_metrics["peak_rss_bytes"]
        or observations["representative_branch_peak_rss_bytes"] != branch_metrics["peak_rss_bytes"]
    ):
        raise ReleaseError("machine observations/resource evidence mismatch")
    admission = exact_keys(
        machine["resource_admission"], FORMAL_MACHINE_ADMISSION_KEYS,
        "machine resource admission",
    )
    for key in (
        "static_required_bytes", "branch_required_bytes", "admitted_required_bytes",
        "admission_limit_bytes",
    ):
        _machine_positive_int(admission[key], f"machine resource admission.{key}")
    for key in (
        "static_inequality_passed", "branch_inequality_passed",
        "storage_launch_passed",
    ):
        if type(admission[key]) is not bool:
            raise ReleaseError(f"machine resource admission.{key} must be exact Boolean")
    static_required = baseline + requirements["static_workers"] * static_metrics[
        "peak_rss_bytes"
    ] + requirements["reserve_bytes"]
    branch_required = baseline + requirements["branch_workers"] * branch_metrics[
        "peak_rss_bytes"
    ] + requirements["reserve_bytes"]
    if (
        admission["static_required_bytes"] != static_required
        or admission["branch_required_bytes"] != branch_required
        or admission["admitted_required_bytes"] != max(static_required, branch_required)
        or admission["admission_limit_bytes"] != requirements["memory_admission_limit_bytes"]
        or admission["static_inequality_passed"] is not (static_required <= admission["admission_limit_bytes"])
        or admission["branch_inequality_passed"] is not (branch_required <= admission["admission_limit_bytes"])
        or admission["storage_launch_passed"] is not (
            observations["result_parent_free_bytes"] >= requirements["launch_free_bytes"]
        )
    ):
        raise ReleaseError("machine admission arithmetic/Boolean mismatch")
    if not (
        admission["static_inequality_passed"]
        and admission["branch_inequality_passed"]
        and admission["storage_launch_passed"]
    ):
        raise ReleaseError("machine freeze records a failed admission gate")
    _machine_validate_filesystem(project_root, machine)
    if expected_role_hashes is None:
        raise ReleaseError("formal machine validation requires frozen role hashes")
    if type(expected_role_hashes) is not dict or not all(
        type(role) is str
        and type(digest) is str
        and HEX_SHA256.fullmatch(digest) is not None
        for role, digest in expected_role_hashes.items()
    ):
        raise ReleaseError("formal machine frozen role-hash map is malformed")
    static_evaluator_raw, _, _ = _machine_project_snapshot(
        project_root, FORMAL_MACHINE_STATIC_EVALUATOR,
        "machine static evaluator role",
    )
    _, plan_hash = _machine_plan_records(project_root)
    required_roles = {
        "scheduler": capture["capture_tool_sha256"],
        "static_evaluator": sha256_bytes(static_evaluator_raw),
        "branch_evaluator_source": branch_binding["source_sha256"],
        "branch_evaluator_binary": branch_binding["sha256"],
        "l1_final_plan": plan_hash,
    }
    for role, digest in required_roles.items():
        if expected_role_hashes.get(role) != digest:
            raise ReleaseError(f"machine freeze/{role} 53-role cross-binding mismatch")
    return machine


def validate_formal_machine_freeze(
    project_root: Path,
    *,
    machine_path: Path | None = None,
    expected_role_hashes: Mapping[str, str] | None = None,
) -> Mapping[str, Any]:
    """Independently validate formal machine bytes without enabling release.

    This helper is intentionally not called by the mock release path.  A later
    formal-release implementation must still pass the separately frozen main
    handshake and independent pre-freeze verdict; a valid machine record alone
    never authorizes dispatch or publication.
    """

    root = lexical_absolute(project_root)
    path = machine_path or project_file(
        root, "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
    )
    with capture_input_generation():
        payload, _ = strict_json_image(lexical_absolute(path), canonical=True)
        return _validate_formal_machine_freeze(
            root, payload, expected_role_hashes=expected_role_hashes
        )


def validate_mock_freeze(project_root: Path) -> tuple[Mapping[str, Any], bytes, list[dict[str, Any]]]:
    path = project_file(project_root, MAIN_FREEZE_RELATIVE)
    freeze, raw = strict_json_image(path, canonical=True)
    if set(freeze) != MOCK_FREEZE_KEYS:
        raise ReleaseError("mock main-freeze key set mismatch")
    exact_int(freeze["schema_version"], "freeze schema", expected=1)
    if freeze["protocol_id"] != PROTOCOL_ID or freeze["artifact_role"] != "MOCK_MAIN_FREEZE":
        raise ReleaseError("mock main-freeze identity mismatch")
    if freeze["artifact_status"] != "MOCK_ONLY_NON_LICENSING" or freeze["authority"] != "ENGINEERING_TEST_ONLY":
        raise ReleaseError("mock main-freeze status mismatch")
    if freeze["mock_only"] is not True or freeze["scientific_licensing_enabled"] is not False:
        raise ReleaseError("formal production release is not implemented")
    if freeze["matrix_id"] != matrix_id() or not exact_json_equal(freeze["matrix"], matrix_payload()):
        raise ReleaseError("mock main-freeze matrix mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if freeze[key] is not None:
            raise ReleaseError(f"unauthorised mock freeze status: {key}")
    expected_roles = [role_binding(project_root, role, relative) for role, relative in INPUT_ROLES]
    if not exact_json_equal(freeze["input_roles"], expected_roles):
        raise ReleaseError("mock main-freeze 53-role map mismatch")
    roles_by_name = {item["role"]: item for item in expected_roles}
    execution_sources = {
        "release_builder": "scripts/build_r401_val_l3_a1_release_provenance.py",
        "composite_checker_source": "scripts/check_r401_val_l3_a1_composite_independent.py",
        "static_checker_source": "scripts/check_r401_val_l3_a1_static_independent.py",
        "branch_checker_source": "scripts/check_r401_val_l3_a1_branch_independent.py",
        "scheduler": "scripts/run_r401_val_l3_a1_all_slabs.py",
        "branch_runtime": "scripts/r401_val_l3_a1_branch_runtime.py",
        "formal_protocol": "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md",
        "scheduler_contract": "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md",
        "checker_contract": "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md",
        "release_contract": "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md",
        "l1_final_plan": "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
        "l1_summary": "results/r401_val_l1_branch/summary.json",
        "l1_manifest": "results/r401_val_l1_branch/manifest.json",
        "l1_checker": "results/r401_val_l1_branch/independent_checker.json",
        "l1_postcheck": "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
        "l1_release": "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    }
    for role, relative in execution_sources.items():
        if roles_by_name[role]["sha256"] != _current_hash(relative):
            raise ReleaseError(f"executing source is not the frozen {role} bytes")
    machine_binding = next(item for item in expected_roles if item["role"] == "machine_freeze")
    if freeze["machine_freeze_sha256"] != machine_binding["sha256"]:
        raise ReleaseError("mock machine-freeze hash mismatch")
    if freeze["claim_boundary"] != MOCK_CLAIM_BOUNDARY:
        raise ReleaseError("mock main-freeze claim boundary mismatch")
    return freeze, raw, expected_roles


def validate_report(path: Path) -> bytes:
    raw, _ = read_snapshot(path)
    expected = (
        "Status: PASS_MOCK_PROVENANCE_REPLAY\n"
        "milestone_status = null\n"
        "theorem_status = null\n"
        "final_status = null\n"
        f"Claim boundary: {MOCK_CLAIM_BOUNDARY}\n"
    ).encode("utf-8")
    if raw != expected:
        raise ReleaseError("mock report authority block mismatch")
    return raw


def _require_null_statuses(payload: Mapping[str, Any], context: str) -> None:
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload.get(key) is not None:
            raise ReleaseError(f"unauthorised {context} status: {key}")


def reject_nested_authority(value: Any, context: str) -> None:
    if type(value) is dict:
        for key, child in value.items():
            if key in RESERVED_NESTED_AUTHORITY_KEYS:
                raise ReleaseError(
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
        raise ReleaseError(f"unexpected {context} authority fields: {sorted(unexpected)}")
    if "authority" in payload and payload["authority"] != "PRODUCER_ONLY":
        raise ReleaseError(f"{context} authority mismatch")
    if "claim_boundary" in payload and payload["claim_boundary"] != expected_claim_boundary:
        raise ReleaseError(f"{context} claim boundary mismatch")
    if (
        "scientific_licensing_enabled" in payload
        and payload["scientific_licensing_enabled"] is not False
    ):
        raise ReleaseError(f"{context} licenses science")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if key in payload and payload[key] is not None:
            raise ReleaseError(f"unauthorised {context} status: {key}")
    for key, value in payload.items():
        if key not in permitted_root_authority:
            reject_nested_authority(value, context)
    return payload


def validate_result_namespace(result: Path, *, allow_release: bool) -> None:
    expected_root = {
        "run_config.json", "static", "branch",
        "independent_static_checker.json", "STATIC_POSTCHECK_STATUS.json",
        "independent_branch_checker.json", "BRANCH_POSTCHECK_STATUS.json",
        "composite_summary.json", "composite_manifest.json",
        "independent_checker.json", "POSTCHECK_STATUS.json",
        "R401_VAL_L3_A1_REPORT.md",
    }
    if allow_release:
        expected_root.add(RELEASE_NAME)
    actual_root = {entry.name for entry in result.iterdir()}
    if actual_root != expected_root:
        raise PathContractError(
            f"authoritative result namespace mismatch: {sorted(actual_root)}"
        )
    for name in expected_root - {"static", "branch"}:
        read_snapshot(result / name)
    for component in ("static", "branch"):
        component_root = result / component
        component_fd = _open_directory(component_root)
        os.close(component_fd)
        names = {entry.name for entry in component_root.iterdir()}
        if names != {"cells", "cell_manifests", "aggregate_summary.json", "aggregate_manifest.json"}:
            raise PathContractError(f"{component} authoritative namespace mismatch")
        for bits in PRECISIONS:
            cell_precision = component_root / "cells" / str(bits)
            manifest_precision = component_root / "cell_manifests" / str(bits)
            cell_fd = _open_directory(cell_precision)
            manifest_fd = _open_directory(manifest_precision)
            os.close(cell_fd)
            os.close(manifest_fd)
            if {entry.name for entry in cell_precision.iterdir()} != set(SLABS):
                raise PathContractError(f"{component} cell slab namespace mismatch")
            if {entry.name for entry in manifest_precision.iterdir()} != {
                f"{slab}.json" for slab in SLABS
            }:
                raise PathContractError(f"{component} manifest slab namespace mismatch")
            expected_files = (
                {"proof.json", "record.json"}
                if component == "static"
                else {"record.json", "stderr.txt", "stdout.txt"}
            )
            for slab in SLABS:
                cell_root = cell_precision / slab
                cell_directory_fd = _open_directory(cell_root)
                os.close(cell_directory_fd)
                if {entry.name for entry in cell_root.iterdir()} != expected_files:
                    raise PathContractError(
                        f"{component} cell payload namespace mismatch: {bits}:{slab}"
                    )
                for filename in expected_files:
                    read_snapshot(cell_root / filename)
                read_snapshot(manifest_precision / f"{slab}.json")


def validate_operational_quiescence(result: Path) -> None:
    journal = result.with_name(f"{result.name}.quarantine-transaction.json")
    if journal.exists() or journal.is_symlink():
        raise PathContractError("live quarantine transaction journal")
    operational = result.with_name(f"{result.name}.operational")
    if not operational.exists():
        return
    descriptor = _open_directory(operational)
    os.close(descriptor)
    expected_directories = {
        "staging", "staging/static", "staging/static/128", "staging/static/256",
        "staging/branch", "staging/branch/128", "staging/branch/256",
        "locks", "locks/branch", "locks/branch/128", "locks/branch/256",
    }
    actual_directories: set[str] = set()
    for path in operational.rglob("*"):
        relative = path.relative_to(operational).as_posix()
        if path.is_symlink() or not path.is_dir():
            raise PathContractError(f"nonquiescent operational object: {relative}")
        directory_fd = _open_directory(path)
        os.close(directory_fd)
        actual_directories.add(relative)
    if actual_directories != expected_directories:
        raise PathContractError(
            f"operational directory layout mismatch: {sorted(actual_directories)}"
        )


def validate_control_chain(project_root: Path) -> dict[str, Any]:
    result = project_file(project_root, RESULT_RELATIVE)
    release_exists = (result / RELEASE_NAME).exists()
    validate_result_namespace(result, allow_release=release_exists)
    validate_operational_quiescence(result)
    run_config, run_raw = strict_json_image(result / "run_config.json", canonical=True)
    exact_keys(run_config, RUN_CONFIG_KEYS, "run config")
    exact_int(run_config["schema_version"], "run-config schema", expected=1)
    if (
        run_config["protocol_id"] != PROTOCOL_ID
        or run_config["artifact_role"] != "RUN_CONFIG"
        or run_config["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or run_config["authority"] != "PRODUCER_ONLY"
        or run_config["mock_only"] is not True
        or run_config["production_authorized"] is not False
        or run_config["scientific_licensing_enabled"] is not False
        or run_config["scheduler_policy"] != "deterministic_component_barrier_batches_v1"
        or run_config["matrix_id"] != matrix_id()
        or not exact_json_equal(run_config["matrix"], matrix_payload())
        or not exact_json_equal(run_config["limits"], candidate_limits())
        or run_config["main_freeze"] != {"path": None, "sha256": None}
        or run_config["machine_freeze"] != {"path": None, "sha256": None}
        or run_config["prefreeze_review"]
        != {"path": None, "sha256": None, "accepted": False}
        or run_config["paths"]
        != {"authoritative_root": str(result), "operational_root": str(result) + ".operational"}
        or not exact_json_equal(run_config["source_bindings"], expected_scheduler_sources())
        or run_config["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
    ):
        raise ReleaseError("run-config semantics mismatch")
    reject_nested_authority(run_config["source_bindings"], "run-config sources")
    _require_null_statuses(run_config, "run config")
    run_hash = sha256_bytes(run_raw)

    component_chains: dict[str, Any] = {}
    for name in ("static", "branch"):
        summary_path = result / name / "aggregate_summary.json"
        manifest_path = result / name / "aggregate_manifest.json"
        checker_path = result / f"independent_{name}_checker.json"
        postcheck_path = result / f"{name.upper()}_POSTCHECK_STATUS.json"
        summary, summary_raw = strict_json_image(summary_path, canonical=True)
        manifest, manifest_raw = strict_json_image(manifest_path, canonical=True)
        checker, checker_raw = strict_json_image(checker_path, canonical=True)
        postcheck, postcheck_raw = strict_json_image(postcheck_path, canonical=True)
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
        exact_keys(checker, COMPONENT_CHECKER_KEYS, f"{name} checker")
        exact_keys(postcheck, POSTCHECK_KEYS, f"{name} postcheck")
        exact_int(summary["schema_version"], f"{name} summary schema", expected=1)
        exact_int(manifest["schema_version"], f"{name} manifest schema", expected=1)
        exact_int(checker["schema_version"], f"{name} checker schema", expected=1)
        exact_int(postcheck["schema_version"], f"{name} postcheck schema", expected=1)
        if (
            summary["protocol_id"] != PROTOCOL_ID
            or manifest["protocol_id"] != PROTOCOL_ID
            or checker["protocol_id"] != PROTOCOL_ID
            or postcheck["protocol_id"] != PROTOCOL_ID
            or summary["artifact_role"] != f"MOCK_{name.upper()}_AGGREGATE_SUMMARY"
            or manifest["artifact_role"] != f"MOCK_{name.upper()}_AGGREGATE_MANIFEST"
            or summary["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
            or manifest["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
            or summary["authority"] != "PRODUCER_ONLY"
            or manifest["authority"] != "PRODUCER_ONLY"
            or summary["mock_only"] is not True
            or manifest["mock_only"] is not True
            or summary["scientific_licensing_enabled"] is not False
            or manifest["scientific_licensing_enabled"] is not False
            or summary["main_freeze_sha256"] is not None
            or manifest["main_freeze_sha256"] is not None
            or summary["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
            or manifest["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
        ):
            raise ReleaseError(f"{name} aggregate identity mismatch")
        if summary.get("run_config_sha256") != run_hash or manifest.get("run_config_sha256") != run_hash:
            raise ReleaseError(f"{name} aggregate run binding mismatch")
        if summary.get("matrix_id") != matrix_id() or manifest.get("matrix_id") != matrix_id():
            raise ReleaseError(f"{name} aggregate matrix mismatch")
        if not exact_json_equal(summary["matrix"], matrix_payload()):
            raise ReleaseError(f"{name} aggregate matrix payload mismatch")
        exact_int(summary["cell_count"], f"{name} cell count", expected=102)
        expected_status = f"{name.upper()}_CELL_CERTIFIED"
        if not exact_json_equal(summary["status_counts"], {expected_status: 102}):
            raise ReleaseError(f"{name} status-count mismatch")
        if not exact_json_equal(
            summary["scheduler_classification_counts"],
            {"COMMITTED_EVALUATOR_RESULT": 102},
        ):
            raise ReleaseError(f"{name} scheduler-classification mismatch")
        summary_binding = exact_keys(
            manifest["summary"], {"path", "sha256", "size_bytes"},
            f"{name} summary binding",
        )
        if (
            summary_binding["path"] != f"{name}/aggregate_summary.json"
            or summary_binding["sha256"] != sha256_bytes(summary_raw)
        ):
            raise ReleaseError(f"{name} aggregate summary edge mismatch")
        exact_int(
            summary_binding["size_bytes"], f"{name} summary size",
            expected=len(summary_raw),
        )
        if name == "branch":
            expected_mock_evaluator = {
                "path": str(ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"),
                "sha256": _current_hash("scripts/mock_r401_val_l3_a1_branch_evaluator.py"),
            }
            if (
                not exact_json_equal(summary["mock_evaluator"], expected_mock_evaluator)
                or not exact_json_equal(manifest["mock_evaluator"], expected_mock_evaluator)
            ):
                raise ReleaseError("branch mock evaluator binding mismatch")
        _require_null_statuses(summary, f"{name} aggregate summary")
        _require_null_statuses(manifest, f"{name} aggregate manifest")
        entries = manifest.get("cell_manifests")
        if type(entries) is not list or len(entries) != 102:
            raise ReleaseError(f"{name} aggregate does not bind 102 manifests")
        expected_root = sha256_bytes(canonical_json_bytes(entries))
        if (
            summary.get("ordered_cell_manifest_root") != expected_root
            or manifest.get("ordered_cell_manifest_root") != expected_root
        ):
            raise ReleaseError(f"{name} aggregate root mismatch")
        for index, (entry, cell) in enumerate(zip(entries, matrix_payload(), strict=True)):
            if type(entry) is not dict or set(entry) != {"cell", "path", "sha256", "size_bytes"}:
                raise ReleaseError(f"{name} manifest entry schema mismatch")
            if not exact_json_equal(entry["cell"], cell):
                raise ReleaseError(f"{name} matrix order mismatch at {index}")
            relative = safe_relative(entry["path"])
            expected = PurePosixPath(name) / "cell_manifests" / str(cell["precision_bits"]) / f"{cell['slab_id']}.json"
            if relative != expected:
                raise ReleaseError(f"{name} cell manifest path mismatch")
            cell_manifest, cell_raw = strict_json_image(
                result / Path(relative), canonical=(name == "static")
            )
            if name == "branch" and branch_transaction_json_bytes(cell_manifest) != cell_raw:
                raise StrictJSONError("branch cell manifest is not runtime-canonical")
            if entry["sha256"] != sha256_bytes(cell_raw):
                raise ReleaseError(f"{name} cell manifest hash mismatch")
            exact_int(entry["size_bytes"], f"{name} cell manifest size", expected=len(cell_raw))
            exact_keys(
                cell_manifest,
                STATIC_CELL_MANIFEST_KEYS if name == "static" else BRANCH_CELL_MANIFEST_KEYS,
                f"{name} cell manifest",
            )
            exact_int(cell_manifest["schema_version"], f"{name} cell schema", expected=1)
            if (
                cell_manifest["protocol_id"] != PROTOCOL_ID
                or cell_manifest["authority"] != "PRODUCER_ONLY"
                or cell_manifest["scientific_licensing_enabled"] is not False
                or cell_manifest["matrix_id"] != matrix_id()
                or cell_manifest["run_config_sha256"] != run_hash
            ):
                raise ReleaseError(f"{name} cell identity/binding mismatch")
            _require_null_statuses(cell_manifest, f"{name} cell manifest")
            files = cell_manifest.get("files")
            if type(files) is not dict:
                raise ReleaseError(f"{name} cell file map is mandatory")
            cell_root = result / name / "cells" / str(cell["precision_bits"]) / cell["slab_id"]
            if name == "static":
                if (
                    cell_manifest["artifact_role"] != "MOCK_STATIC_CELL_MANIFEST"
                    or cell_manifest["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
                    or cell_manifest["mock_only"] is not True
                    or cell_manifest["main_freeze_sha256"] is not None
                    or cell_manifest["scheduler_classification"] != "COMMITTED_EVALUATOR_RESULT"
                    or cell_manifest["evaluator_status"] != "STATIC_CELL_CERTIFIED"
                    or cell_manifest["claim_boundary"] != SCHEDULER_MOCK_CLAIM_BOUNDARY
                    or not exact_json_equal(cell_manifest["cell"], cell)
                ):
                    raise ReleaseError("static cell semantics mismatch")
                if set(files) != {"proof.json", "record.json"}:
                    raise ReleaseError("static cell file map must bind proof and record")
                for filename in ("proof.json", "record.json"):
                    binding = files[filename]
                    if type(binding) is not dict or set(binding) != {"sha256", "size_bytes"}:
                        raise ReleaseError("static cell file binding mismatch")
                    payload_raw, info = read_snapshot(cell_root / filename)
                    if binding["sha256"] != sha256_bytes(payload_raw):
                        raise ReleaseError("static cell payload hash mismatch")
                    exact_int(
                        binding["size_bytes"],
                        "static cell payload size",
                        expected=info.st_size,
                    )
                    validate_json_payload_authority(
                        payload_raw,
                        context=f"static {filename}",
                        branch_transaction=False,
                        expected_claim_boundary=SCHEDULER_MOCK_CLAIM_BOUNDARY,
                    )
            else:
                if (
                    cell_manifest["artifact_role"] != "BRANCH_CELL_MANIFEST"
                    or cell_manifest["claim_boundary"] != BRANCH_CELL_CLAIM_BOUNDARY
                    or not exact_json_equal(cell_manifest["cell_identity"], cell)
                    or not exact_json_equal(cell_manifest["budgets"], BRANCH_CELL_BUDGETS)
                ):
                    raise ReleaseError("branch cell semantics mismatch")
                require_sha256(cell_manifest["freeze_sha256"], "branch cell freeze hash")
                require_sha256(cell_manifest["task_binding_sha256"], "branch task hash")
                expected_files = {
                    (
                        PurePosixPath("branch")
                        / "cells"
                        / str(cell["precision_bits"])
                        / cell["slab_id"]
                        / filename
                    ).as_posix()
                    for filename in ("record.json", "stderr.txt", "stdout.txt")
                }
                if set(files) != expected_files:
                    raise ReleaseError("branch cell file map must bind raw and record bytes")
                for relative_payload, bound_hash in files.items():
                    safe_relative(relative_payload)
                    require_sha256(bound_hash, "branch cell payload hash")
                    payload_raw, _ = read_snapshot(result / relative_payload)
                    if bound_hash != sha256_bytes(payload_raw):
                        raise ReleaseError("branch cell payload hash mismatch")
                    if relative_payload.endswith("/record.json"):
                        validate_json_payload_authority(
                            payload_raw,
                            context="branch record.json",
                            branch_transaction=True,
                            expected_claim_boundary=BRANCH_CELL_CLAIM_BOUNDARY,
                        )
        semantics = expected_component_semantics(
            name,
            expected_root,
            summary.get("mock_evaluator") if name == "branch" else None,
        )
        if (
            checker["artifact_role"] != f"{name.upper()}_INDEPENDENT_CHECKER"
            or checker["authority"] != "INDEPENDENT_CHECKER"
            or checker["checker_status"] != MOCK_CHECKER_STATUS
            or checker["passed"] is not True
            or checker["component_status"] is not None
            or checker["scientific_licensing_enabled"] is not False
            or checker["matrix_id"] != matrix_id()
            or checker["main_freeze_sha256"] is not None
            or checker["run_config_sha256"] != run_hash
            or checker["component_aggregate_summary_sha256"] != sha256_bytes(summary_raw)
            or checker["component_aggregate_manifest_sha256"] != sha256_bytes(manifest_raw)
            or checker["failures"] != []
            or not exact_json_equal(checker["replay_counts"], semantics["replay_counts"])
            or not exact_json_equal(checker["cross_precision"], semantics["cross_precision"])
            or not exact_json_equal(checker["diagnostics"], semantics["diagnostics"])
            or not exact_json_equal(checker["source_bindings"], semantics["source_bindings"])
            or checker["claim_boundary"] != semantics["claim_boundary"]
        ):
            raise ReleaseError(f"{name} checker authority mismatch")
        _require_null_statuses(checker, f"{name} checker")
        for field in ("replay_counts", "cross_precision", "diagnostics", "source_bindings"):
            reject_nested_authority(checker[field], f"{name} checker {field}")
        checker_source_relative = f"scripts/check_r401_val_l3_a1_{name}_independent.py"
        expected_bound_artifacts = {
            "aggregate_manifest": {
                "path": f"{name}/aggregate_manifest.json",
                "sha256": sha256_bytes(manifest_raw),
            },
            "aggregate_summary": {
                "path": f"{name}/aggregate_summary.json",
                "sha256": sha256_bytes(summary_raw),
            },
            "checker_source": {
                "path": checker_source_relative,
                "sha256": _current_hash(checker_source_relative),
            },
        }
        if (
            postcheck["artifact_role"] != f"{name.upper()}_POSTCHECK"
            or postcheck["authority"] != "POSTCHECK_ONLY"
            or postcheck["postcheck_status"] != MOCK_POSTCHECK_STATUS
            or postcheck["passed"] is not True
            or postcheck["checker_path"] != f"independent_{name}_checker.json"
            or postcheck["checker_sha256"] != sha256_bytes(checker_raw)
            or postcheck["run_config_sha256"] != run_hash
            or postcheck["main_freeze_sha256"] is not None
            or postcheck["failures"] != []
            or postcheck["claim_boundary"] != semantics["postcheck_claim_boundary"]
            or not exact_json_equal(postcheck["replay_counts"], semantics["replay_counts"])
            or not exact_json_equal(postcheck["bound_artifacts"], expected_bound_artifacts)
        ):
            raise ReleaseError(f"{name} postcheck authority/binding mismatch")
        _require_null_statuses(postcheck, f"{name} postcheck")
        for field in ("bound_artifacts", "replay_counts"):
            reject_nested_authority(postcheck[field], f"{name} postcheck {field}")
        component_chains[name] = {
            "aggregate_summary_sha256": sha256_bytes(summary_raw),
            "aggregate_manifest_sha256": sha256_bytes(manifest_raw),
            "checker_sha256": sha256_bytes(checker_raw),
            "postcheck_sha256": sha256_bytes(postcheck_raw),
            "ordered_cell_manifest_root": summary["ordered_cell_manifest_root"],
        }

    composite_summary, composite_summary_raw = strict_json_image(result / "composite_summary.json", canonical=True)
    composite_manifest, composite_manifest_raw = strict_json_image(result / "composite_manifest.json", canonical=True)
    composite_checker, composite_checker_raw = strict_json_image(result / "independent_checker.json", canonical=True)
    composite_postcheck, composite_postcheck_raw = strict_json_image(result / "POSTCHECK_STATUS.json", canonical=True)
    exact_keys(composite_summary, COMPOSITE_SUMMARY_KEYS, "composite summary")
    exact_keys(composite_manifest, COMPOSITE_MANIFEST_KEYS, "composite manifest")
    exact_keys(composite_checker, COMPOSITE_CHECKER_KEYS, "composite checker")
    exact_keys(composite_postcheck, POSTCHECK_KEYS, "composite postcheck")
    exact_int(composite_summary["schema_version"], "composite summary schema", expected=1)
    exact_int(composite_manifest["schema_version"], "composite manifest schema", expected=1)
    exact_int(composite_checker["schema_version"], "composite checker schema", expected=1)
    exact_int(composite_postcheck["schema_version"], "composite postcheck schema", expected=1)
    if composite_checker["protocol_id"] != PROTOCOL_ID or composite_postcheck["protocol_id"] != PROTOCOL_ID:
        raise ReleaseError("composite checker/postcheck protocol mismatch")
    expected_verbose_chains = {
        "static": {
            "aggregate_summary": {"path": "static/aggregate_summary.json", "sha256": component_chains["static"]["aggregate_summary_sha256"]},
            "aggregate_manifest": {"path": "static/aggregate_manifest.json", "sha256": component_chains["static"]["aggregate_manifest_sha256"]},
            "checker": {"path": "independent_static_checker.json", "sha256": component_chains["static"]["checker_sha256"]},
            "postcheck": {"path": "STATIC_POSTCHECK_STATUS.json", "sha256": component_chains["static"]["postcheck_sha256"]},
            "ordered_cell_manifest_root": component_chains["static"]["ordered_cell_manifest_root"],
        },
        "branch": {
            "aggregate_summary": {"path": "branch/aggregate_summary.json", "sha256": component_chains["branch"]["aggregate_summary_sha256"]},
            "aggregate_manifest": {"path": "branch/aggregate_manifest.json", "sha256": component_chains["branch"]["aggregate_manifest_sha256"]},
            "checker": {"path": "independent_branch_checker.json", "sha256": component_chains["branch"]["checker_sha256"]},
            "postcheck": {"path": "BRANCH_POSTCHECK_STATUS.json", "sha256": component_chains["branch"]["postcheck_sha256"]},
            "ordered_cell_manifest_root": component_chains["branch"]["ordered_cell_manifest_root"],
        },
    }
    if not exact_json_equal(composite_summary["component_chains"], expected_verbose_chains):
        raise ReleaseError("composite component-chain binding mismatch")
    if not exact_json_equal(composite_manifest["component_chains"], expected_verbose_chains):
        raise ReleaseError("composite manifest component-chain binding mismatch")
    expected_generation = sha256_bytes(canonical_json_bytes(expected_verbose_chains))
    if (
        composite_summary["archive_generation_sha256"] != expected_generation
        or composite_manifest["archive_generation_sha256"] != expected_generation
    ):
        raise ReleaseError("composite archive-generation mismatch")
    if (
        composite_summary["artifact_role"] != "MOCK_COMPOSITE_SUMMARY"
        or composite_manifest["artifact_role"] != "MOCK_COMPOSITE_MANIFEST"
        or composite_summary["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or composite_manifest["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or composite_summary["authority"] != "PRODUCER_ONLY"
        or composite_manifest["authority"] != "PRODUCER_ONLY"
        or composite_summary["mock_only"] is not True
        or composite_manifest["mock_only"] is not True
        or composite_summary["scientific_licensing_enabled"] is not False
        or composite_manifest["scientific_licensing_enabled"] is not False
        or composite_summary["run_config_sha256"] != run_hash
        or composite_manifest["run_config_sha256"] != run_hash
        or composite_summary["matrix_id"] != matrix_id()
        or composite_manifest["matrix_id"] != matrix_id()
        or composite_summary["protocol_id"] != PROTOCOL_ID
        or composite_manifest["protocol_id"] != PROTOCOL_ID
        or composite_summary["main_freeze_sha256"] is not None
        or composite_manifest["main_freeze_sha256"] is not None
        or composite_summary["claim_boundary"] != COMPOSITE_MOCK_CLAIM_BOUNDARY
        or composite_manifest["claim_boundary"] != COMPOSITE_MOCK_CLAIM_BOUNDARY
        or not exact_json_equal(composite_summary["matrix"], matrix_payload())
    ):
        raise ReleaseError("composite producer identity/binding mismatch")
    exact_int(
        composite_summary["cell_count_per_component"],
        "composite cell count per component",
        expected=102,
    )
    _require_null_statuses(composite_summary, "composite summary")
    _require_null_statuses(composite_manifest, "composite manifest")
    reject_nested_authority(composite_summary["component_chains"], "composite summary chains")
    reject_nested_authority(composite_manifest["component_chains"], "composite manifest chains")
    summary_binding = exact_keys(
        composite_manifest["summary"],
        {"path", "sha256", "size_bytes"},
        "composite summary binding",
    )
    if (
        summary_binding["path"] != "composite_summary.json"
        or summary_binding["sha256"] != sha256_bytes(composite_summary_raw)
    ):
        raise ReleaseError("composite manifest summary edge mismatch")
    exact_int(
        summary_binding["size_bytes"],
        "composite summary size",
        expected=len(composite_summary_raw),
    )
    expected_composite_sources = {
        "composite_checker_source": _current_hash(
            "scripts/check_r401_val_l3_a1_composite_independent.py"
        ),
        "checker_contract": _current_hash(
            "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
        ),
        "release_contract": _current_hash(
            "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
        ),
    }
    expected_composite_diagnostics = {
        "mock_only": True,
        "archive_generation_sha256": expected_generation,
        "composite_summary_sha256": sha256_bytes(composite_summary_raw),
        "composite_manifest_sha256": sha256_bytes(composite_manifest_raw),
    }
    if (
        composite_checker["artifact_role"] != "COMPOSITE_INDEPENDENT_CHECKER"
        or composite_checker["authority"] != "INDEPENDENT_CHECKER"
        or composite_checker["checker_status"] != MOCK_CHECKER_STATUS
        or composite_checker["passed"] is not True
        or composite_checker["scientific_licensing_enabled"] is not False
        or composite_checker["matrix_id"] != matrix_id()
        or composite_checker["main_freeze_sha256"] is not None
        or composite_checker["run_config_sha256"] != run_hash
        or not exact_json_equal(composite_checker["static_chain"], expected_verbose_chains["static"])
        or not exact_json_equal(composite_checker["branch_chain"], expected_verbose_chains["branch"])
        or not exact_json_equal(
            composite_checker["upstream_chains"],
            {"mock_only": True, "scientific_replay": False},
        )
        or composite_checker["s0_compatibility"] is not None
        or not exact_json_equal(
            composite_checker["replay_counts"],
            {"static_cells": 102, "branch_cells": 102, "component_chains": 2},
        )
        or not exact_json_equal(
            composite_checker["cross_precision"],
            {"checked_slabs": 51, "matching_mock_verdicts": 51, "passed": True},
        )
        or not exact_json_equal(
            composite_checker["diagnostics"], expected_composite_diagnostics
        )
        or not exact_json_equal(
            composite_checker["source_bindings"], expected_composite_sources
        )
        or composite_checker["claim_boundary"] != COMPOSITE_MOCK_CLAIM_BOUNDARY
        or composite_checker["failures"] != []
    ):
        raise ReleaseError("composite checker authority/binding mismatch")
    if composite_checker.get("diagnostics", {}).get("composite_summary_sha256") != sha256_bytes(composite_summary_raw):
        raise ReleaseError("composite checker summary edge mismatch")
    if composite_checker.get("diagnostics", {}).get("composite_manifest_sha256") != sha256_bytes(composite_manifest_raw):
        raise ReleaseError("composite checker manifest edge mismatch")
    _require_null_statuses(composite_checker, "composite checker")
    for field in (
        "static_chain", "branch_chain", "upstream_chains", "replay_counts",
        "cross_precision", "diagnostics", "source_bindings",
    ):
        reject_nested_authority(composite_checker[field], f"composite checker {field}")
    if composite_postcheck.get("postcheck_status") != MOCK_POSTCHECK_STATUS or composite_postcheck.get("passed") is not True:
        raise ReleaseError("composite postcheck mock status mismatch")
    if composite_postcheck.get("checker_sha256") != sha256_bytes(composite_checker_raw):
        raise ReleaseError("composite postcheck checker edge mismatch")
    if (
        composite_postcheck["artifact_role"] != "COMPOSITE_POSTCHECK"
        or composite_postcheck["authority"] != "POSTCHECK_ONLY"
        or composite_postcheck["checker_path"] != "independent_checker.json"
        or composite_postcheck["run_config_sha256"] != run_hash
        or composite_postcheck["main_freeze_sha256"] is not None
        or composite_postcheck["failures"] != []
    ):
        raise ReleaseError("composite postcheck authority/binding mismatch")
    _require_null_statuses(composite_postcheck, "composite postcheck")
    for field in ("bound_artifacts", "replay_counts"):
        reject_nested_authority(composite_postcheck[field], f"composite postcheck {field}")
    if composite_postcheck["claim_boundary"] != COMPOSITE_MOCK_CLAIM_BOUNDARY:
        raise ReleaseError("composite postcheck claim boundary mismatch")
    if not exact_json_equal(
        composite_postcheck["replay_counts"],
        composite_checker["replay_counts"],
    ):
        raise ReleaseError("composite postcheck replay-count mismatch")
    expected_composite_bound = {
        "archive_generation_sha256": expected_generation,
        "composite_manifest_sha256": sha256_bytes(composite_manifest_raw),
        "composite_summary_sha256": sha256_bytes(composite_summary_raw),
    }
    if not exact_json_equal(
        composite_postcheck["bound_artifacts"], expected_composite_bound
    ):
        raise ReleaseError("composite postcheck artifact bindings mismatch")
    return {
        "run_config_sha256": run_hash,
        "component_chains": component_chains,
        "composite_chain": {
            "summary_sha256": sha256_bytes(composite_summary_raw),
            "manifest_sha256": sha256_bytes(composite_manifest_raw),
            "checker_sha256": sha256_bytes(composite_checker_raw),
            "postcheck_sha256": sha256_bytes(composite_postcheck_raw),
            "archive_generation_sha256": composite_summary["archive_generation_sha256"],
        },
    }


def _build_expected_release(project_root: Path) -> dict[str, Any]:
    project_root = lexical_absolute(project_root)
    freeze, freeze_raw, input_roles = validate_mock_freeze(project_root)
    chain = validate_control_chain(project_root)
    report_path = project_file(project_root, f"{RESULT_RELATIVE}/R401_VAL_L3_A1_REPORT.md")
    validate_report(report_path)
    main_role = {
        "role": "main_freeze",
        "path": MAIN_FREEZE_RELATIVE.as_posix(),
        "sha256": sha256_bytes(freeze_raw),
    }
    downstream = [role_binding(project_root, role, relative) for role, relative in DOWNSTREAM_ROLES]
    roles = [*input_roles, main_role, *downstream]
    if len(roles) != 68 or len({item["role"] for item in roles}) != 68:
        raise ReleaseError("release role map is not exactly 68 unique roles")
    machine_hash = next(item["sha256"] for item in input_roles if item["role"] == "machine_freeze")
    return {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "release_contract": RELEASE_CONTRACT,
        "release_status": MOCK_RELEASE_STATUS,
        "authority": "RELEASE_BINDING_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": matrix_id(),
        "main_freeze_sha256": sha256_bytes(freeze_raw),
        "machine_freeze_sha256": machine_hash,
        "run_config_sha256": chain["run_config_sha256"],
        "archive_generation_sha256": chain["composite_chain"]["archive_generation_sha256"],
        "ordered_static_manifest_root": chain["component_chains"]["static"]["ordered_cell_manifest_root"],
        "ordered_branch_manifest_root": chain["component_chains"]["branch"]["ordered_cell_manifest_root"],
        "roles": roles,
        "component_chains": chain["component_chains"],
        "composite_chain": chain["composite_chain"],
        "upstream_chains": {"mock_hash_binding_only": True, "scientific_replay": False},
        "s0_compatibility": {"mock_hash_binding_only": True, "scientific_replay": False},
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def build_expected_release(project_root: Path) -> dict[str, Any]:
    with capture_input_generation():
        return _build_expected_release(project_root)


def release_path(project_root: Path) -> Path:
    return project_file(project_root, f"{RESULT_RELATIVE}/{RELEASE_NAME}")


def write_once(path: Path, raw: bytes) -> None:
    canonical = lexical_absolute(path)
    parent_fd = _open_directory(canonical.parent)
    descriptor: int | None = None
    temporary_name = f".{canonical.name}.seal-{os.getpid()}-{secrets.token_hex(16)}"
    temporary_unlinked = False
    try:
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o600,
            dir_fd=parent_fd,
        )
        view = memoryview(raw)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short release write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise PathContractError("release staging inode is not a regular file")
        try:
            os.link(
                f"/proc/self/fd/{descriptor}",
                canonical.name,
                dst_dir_fd=parent_fd,
                follow_symlinks=True,
            )
        except FileExistsError:
            raise
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        if (info.st_dev, info.st_ino) != (entry.st_dev, entry.st_ino):
            raise PathContractError("release publication inode mismatch")
        os.unlink(temporary_name, dir_fd=parent_fd)
        temporary_unlinked = True
        published_fd = os.open(
            canonical.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
        try:
            published = os.read(published_fd, len(raw) + 1)
            published_info = os.fstat(published_fd)
            if published != raw or published_info.st_nlink != 1:
                raise PathContractError("release publication byte/link mismatch")
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


def build_release(project_root: Path) -> dict[str, Any]:
    with capture_input_generation():
        expected = _build_expected_release(project_root)
        path = release_path(project_root)
        raw = canonical_json_bytes(expected)
        if path.exists():
            stored, stored_raw = strict_json_image(path, canonical=True)
            if stored_raw != raw or not exact_json_equal(stored, expected):
                raise ReleaseError("different release already exists")
            result = project_file(project_root, RESULT_RELATIVE)
            validate_result_namespace(result, allow_release=True)
            validate_operational_quiescence(result)
            return dict(stored)
        write_once(path, raw)
        stored, stored_raw = strict_json_image(path, canonical=True)
        if stored_raw != raw or not exact_json_equal(stored, expected):
            raise ReleaseError("published release verification failed")
        result = project_file(project_root, RESULT_RELATIVE)
        validate_result_namespace(result, allow_release=True)
        validate_operational_quiescence(result)
        return expected


def verify_release(project_root: Path) -> dict[str, Any]:
    with capture_input_generation():
        expected = _build_expected_release(project_root)
        stored, raw = strict_json_image(release_path(project_root), canonical=True)
        if raw != canonical_json_bytes(expected) or not exact_json_equal(stored, expected):
            raise ReleaseError("release bytes or provenance DAG mismatch")
        result = project_file(project_root, RESULT_RELATIVE)
        validate_result_namespace(result, allow_release=True)
        validate_operational_quiescence(result)
        return dict(stored)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--verify-only", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        root = lexical_absolute(arguments.project_root)
        payload = verify_release(root) if arguments.verify_only else build_release(root)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"release_status={payload['release_status']} roles={len(payload['roles'])} "
        "scientific_licensing_enabled=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
