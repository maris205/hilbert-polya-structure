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
    "pipe_close_grace_seconds": 1.0,
    "record_bytes": 4 * 1024 * 1024,
    "stderr_bytes": 1 * 1024 * 1024,
    "stdout_bytes": 16 * 1024 * 1024,
    "term_grace_seconds": 2.0,
    "timeout_seconds": 600.0,
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
        raise StrictJSONError(f"noncanonical JSON payload: {error}") from error


def branch_transaction_json_bytes(payload: Any) -> bytes:
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
                raise PathContractError(f"input changed during release build: {path}")
    finally:
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
