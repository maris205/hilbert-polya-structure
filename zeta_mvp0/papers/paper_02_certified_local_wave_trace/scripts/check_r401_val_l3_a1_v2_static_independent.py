#!/usr/bin/env python3
"""Independent formal-only V2 static checker and role-54 verifier.

This source deliberately carries its own V2 role map, schemas, path checks,
Arb proof replay and write-once publication code.  It imports no scheduler,
evaluator, checker, adapter, or release builder and never invokes an
evaluator.  The retained attempt-1 helpers are unreachable from the V2 CLI;
they remain only as locally duplicated arithmetic used by formal replay.
"""

from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
import ctypes
import csv
from datetime import datetime, timezone
from decimal import Decimal
import errno
import fcntl
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
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterable, Iterator, Mapping, Sequence

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve()
EVALUATOR = ROOT / "scripts/evaluate_r401_val_l3_a1_static_cell.py"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_RELEASE_CHAIN = (
    L1_RELEASE,
    L1_SUMMARY,
    L1_MANIFEST,
    L1_CHECKER,
    L1_POSTCHECK,
)
L1_SUMMARY_KEYS = {
    "bridge_job_count", "claim_boundary", "cross_precision_gates", "environment",
    "final_status", "hash_gates", "job_count_per_precision", "milestone_status",
    "plan_gates", "precision_gates", "primary_job_count", "protocol_id",
    "records", "requested_precisions",
}
L1_MANIFEST_KEYS = {"capd_commit", "files", "final_status", "milestone_status", "protocol_id"}
L1_CHECKER_KEYS = {
    "aggregate_check_count", "arithmetic_replay_count", "checker_status",
    "final_status", "frozen_hash_gates", "global_gates", "job_failures",
    "manifest_file_count", "manifest_hash_failures", "milestone_status",
    "plan_gates", "protocol_id", "scope",
}
L1_POSTCHECK_KEYS = {"checker_status", "files", "final_status", "milestone_status", "protocol_id"}
L1_RELEASE_KEYS = {"files", "final_status", "protocol_id", "release_status", "scope"}
L1_POSTCHECK_FILES = {
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/summary.json",
    "scripts/check_r401_val_l1_independent.py",
}
L1_RELEASE_FILES = {
    "research/route_a_wave_trace/A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md",
    "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    "research/route_a_wave_trace/R401_VAL_L1_PROTOCOL_V2.md",
    "research/route_a_wave_trace/R401_VAL_L1_V2_FREEZE.md",
    "results/R401_VAL_INVALIDATION_REGISTRY.json",
    "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/summary.json",
    "scripts/check_r401_val_l1_independent.py",
    "scripts/run_r401_val_l1_branch.py",
    "validated/capd_r401_local_slab_grid_mp.cpp",
}
L1_SUMMARY_BOUNDARY = (
    "one primitive full-return branch, unique only inside the frozen local primary "
    "boxes and bridge hulls, for every epsilon in [0,0.101]; no root-complement, "
    "global phase-space cover, delta_tr, Hilbert-Polya, or RH claim"
)

SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-A1"
CELL_ROLE = "STATIC_CELL_PROOF"
CHECKER_ROLE = "STATIC_INDEPENDENT_CHECKER"
PASS_STATUS = "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
CELL_PASS_STATUS = "STATIC_CELL_CERTIFIED"
SLABS = tuple(f"S{index:03d}" for index in range(51))
PRECISIONS = (128, 256)
ANGLE_COORDINATES = ("qminus", "qplus", "pminus", "pplus")
SECTION_COORDINATES = ("qminus", "qplus", "pminus")

ANGLE_ROOT: dict[str, tuple[Fraction, Fraction]] = {
    "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
    "qplus": (Fraction(-18, 100), Fraction(18, 100)),
    "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    "pplus": (Fraction(-1415, 1000), Fraction(1415, 1000)),
}
SECTION_ROOTS: dict[str, dict[str, tuple[Fraction, Fraction]]] = {
    "SECTION_LOW": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(0), Fraction(12, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
    "SECTION_HIGH": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(17, 100), Fraction(18, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
    "SECTION_WINDOW": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(12, 100), Fraction(17, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
}

ENERGY_LEVEL = Fraction(1)
TUBE_RADIUS_SQUARED = Fraction(36, 10_000)
ANGLE_CEILING = Fraction(18)
EPSILON_CAP = Fraction(101, 1000)
PERIOD_MAX = Fraction(69, 100)
EXPECTED_DERIVATION = {
    "qminus": "r_minus<=0.06 implies |Q_minus|<=0.06/omega_minus",
    "qplus": "K=1 and exprel(s)>=1 imply |W|<=1/(sqrt(2)pi); triangle inequality for A Q=W+(a epsilon q1^2,0) and the fast singular direction gives the displayed bound",
    "pplus": "K=1 with nonnegative potential implies |P_plus|<=sqrt(2)",
    "winding": "theta_dot<18 and T<=0.69 imply Delta theta<4pi",
}

CLAIM_BOUNDARY = (
    "all-slab static phase-anchor component only, conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no branch-tube, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
CELL_CLAIM_BOUNDARY = (
    "producer-only static phase-anchor cell conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no component, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)

# The mock chain is deliberately a separate engineering namespace.  These
# values cannot be confused with the future scientific component pass in the
# checker contract.
MOCK_ARTIFACT_STATUS = "MOCK_ONLY_NON_LICENSING"
MOCK_CHECKER_STATUS = "PASS_MOCK_INDEPENDENT_REPLAY"
MOCK_POSTCHECK_STATUS = "PASS_MOCK_WRITE_ONCE_POSTCHECK"
MOCK_CLAIM_BOUNDARY = (
    "deterministic 102-cell static archive and hash-DAG engineering replay "
    "only; synthetic proofs receive no static component, local theorem, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
MOCK_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the non-licensing 102-cell static mock "
    "checker chain only; no scientific component or programme authority"
)
MOCK_PRODUCER_CLAIM_BOUNDARY = (
    "synthetic static/branch scheduler transaction only; no Arb/CAPD "
    "scientific evaluation, no component or local theorem, no global "
    "routing, trace, Hilbert-Polya, zeta-zero, or RH claim"
)

V2_RESULT_RELATIVE = "results/r401_val_l3_a1_v2_all_slabs"
V2_MAIN_RELATIVE = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json"
V2_REVIEW_RELATIVE = "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md"
V2_CHECKER_RELATIVE = "scripts/check_r401_val_l3_a1_v2_static_independent.py"
V2_CHECKER_OUTPUT = "independent_static_checker.json"
V2_POSTCHECK_OUTPUT = "STATIC_POSTCHECK_STATUS.json"
FORMAL_CHECKER_STATUS = "PASS_INDEPENDENT_CHECKER"
FORMAL_POSTCHECK_STATUS = "PASS_WRITE_ONCE_POSTCHECK"
FORMAL_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the formal 102-cell static checker chain only; "
    "no authority beyond PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
)
MAIN_VERIFY_RECEIPT_KEYS = {
    "verification_status", "authority", "candidate_sha256",
    "input_map_sha256", "size_bytes", "promotion_authorized",
    "artifacts_written",
}
PREFREEZE_ACCEPT_RAW = b"Verdict: ACCEPT_FOR_FREEZE\n"
HEX_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
MAIN_FREEZE_CLAIM_BOUNDARY = (
    "exact control-plane and ordered 53-role pre-freeze authority only; no "
    "evaluator result, component status, theorem, Hilbert-Polya, zeta-zero, or RH claim"
)

INPUT_ROLES: tuple[tuple[str, str], ...] = (
    ("a416_derivation", "research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md"),
    ("s0_protocol", "research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md"),
    ("s0_report", "research/route_a_wave_trace/A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md"),
    ("prefreeze_design", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_DESIGN.md"),
    ("implementation_design_review", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"),
    ("formal_protocol", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PROTOCOL.md"),
    ("scheduler_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_SCHEDULER_CONTRACT.md"),
    ("checker_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_CHECKER_CONTRACT.md"),
    ("release_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_RELEASE_PROVENANCE_CONTRACT.md"),
    ("machine_freeze", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"),
    ("prefreeze_tests", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json"),
    ("prefreeze_review", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md"),
    ("s0_compatibility", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"),
    ("capd_dependency", "validated/CAPD_DEPENDENCY.md"),
    ("static_evaluator", "scripts/evaluate_r401_val_l3_a1_static_cell.py"),
    ("branch_evaluator_source", "validated/capd_r401_phase_branch_tube_mp_a1.cpp"),
    ("branch_evaluator_binary", "validated/bin/capd_r401_phase_branch_tube_mp_a1"),
    ("branch_runtime", "scripts/r401_val_l3_a1_branch_runtime.py"),
    ("scheduler", "scripts/run_r401_val_l3_a1_v2_all_slabs.py"),
    ("static_checker_source", V2_CHECKER_RELATIVE),
    ("branch_checker_source", "scripts/check_r401_val_l3_a1_v2_branch_independent.py"),
    ("composite_checker_source", "scripts/check_r401_val_l3_a1_v2_composite_independent.py"),
    ("s0_adapter", "scripts/replay_r401_val_l3_s0_through_a1_v2_checkers.py"),
    ("release_builder", "scripts/build_r401_val_l3_a1_v2_release_provenance.py"),
    ("test_static_evaluator", "tests/test_r401_val_l3_a1_static_cell.py"),
    ("test_static_scheduler", "tests/test_r401_val_l3_a1_v2_static_scheduler.py"),
    ("test_static_checker", "tests/test_r401_val_l3_a1_v2_static_checker.py"),
    ("test_branch_scheduler", "tests/test_r401_val_l3_a1_v2_branch_scheduler.py"),
    ("test_branch_checker", "tests/test_r401_val_l3_a1_v2_branch_checker.py"),
    ("test_s0_compatibility", "tests/test_r401_val_l3_a1_v2_s0_compatibility.py"),
    ("test_composite", "tests/test_r401_val_l3_a1_v2_composite_contract.py"),
    ("test_adversarial", "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py"),
    ("test_release", "tests/test_r401_val_l3_a1_v2_release_provenance.py"),
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

MAIN_FREEZE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "matrix", "matrix_id", "input_roles",
    "machine_freeze_sha256", "prefreeze_review", "serializers", "scheduler",
    "limits", "status_tables", "evaluators", "checkers", "archive_layout",
    "machine_requirements", "failure_policy", "execution_policy",
    "claim_boundary", "component_status", "milestone_status", "theorem_status",
    "final_status",
}
FORMAL_CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_aggregate_summary_sha256", "component_aggregate_manifest_sha256",
    "replay_counts", "cross_precision", "diagnostics", "failures",
    "source_bindings", "claim_boundary", "milestone_status", "theorem_status",
    "final_status",
}
FORMAL_POSTCHECK_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "postcheck_status", "passed", "checker_path", "checker_sha256",
    "main_freeze_sha256", "run_config_sha256", "bound_artifacts",
    "replay_counts", "failures", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status", "theorem_status",
    "final_status",
}

SCHEDULER_SOURCE = ROOT / "scripts/run_r401_val_l3_a1_v2_all_slabs.py"
BRANCH_RUNTIME_SOURCE = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
MOCK_BRANCH_EVALUATOR_SOURCE = (
    ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"
)
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PROTOCOL.md"
SCHEDULER_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_SCHEDULER_CONTRACT.md"
)
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_RELEASE_PROVENANCE_CONTRACT.md"
)
MOCK_SOURCE_PATHS = (
    SCHEDULER_SOURCE,
    BRANCH_RUNTIME_SOURCE,
    MOCK_BRANCH_EVALUATOR_SOURCE,
    PLAN,
    PROTOCOL,
    SCHEDULER_CONTRACT,
    CHECKER_CONTRACT,
    RELEASE_CONTRACT,
)


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def exact_keys(
    payload: dict[str, Any], expected: set[str], context: str
) -> Mapping[str, Any]:
    require(type(payload) is dict, f"{context}: object required")
    actual = set(payload)
    require(
        actual == expected,
        f"{context}: keys differ; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}",
    )
    return payload


def require_exact_int(
    value: Any,
    context: str,
    *,
    expected: int | None = None,
    minimum: int | None = None,
) -> int:
    require(type(value) is int, f"{context}: expected an exact JSON integer")
    if expected is not None:
        require(value == expected, f"{context}: expected {expected}, found {value}")
    if minimum is not None:
        require(value >= minimum, f"{context}: integer below {minimum}")
    return value


def json_exact_equal(actual: Any, expected: Any) -> bool:
    """Recursive equality that never identifies bool, int, and float."""

    if type(actual) is not type(expected):
        return False
    if isinstance(expected, dict):
        return set(actual) == set(expected) and all(
            json_exact_equal(actual[key], expected[key]) for key in expected
        )
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(
            json_exact_equal(left, right)
            for left, right in zip(actual, expected, strict=True)
        )
    return bool(actual == expected)


def require_json_exact(actual: Any, expected: Any, context: str) -> None:
    require(json_exact_equal(actual, expected), f"{context}: exact JSON value mismatch")


def _require_exact_json_value(value: Any, context: str = "$") -> None:
    """Restrict ``CJ_COMPACT_V1`` to exact JSON data-model values."""

    if value is None or type(value) in (bool, str, int):
        return
    if type(value) is float:
        require(math.isfinite(value), f"{context}: non-finite JSON number")
        return
    if type(value) is list:
        for index, item in enumerate(value):
            _require_exact_json_value(item, f"{context}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            require(type(key) is str, f"{context}: JSON object key is not an exact string")
            _require_exact_json_value(item, f"{context}.{key}")
        return
    raise CheckError(
        f"{context}: unsupported exact JSON value type {type(value).__name__}"
    )


def canonical_json_bytes(payload: Any) -> bytes:
    """Serialize the frozen ``CJ_COMPACT_V1`` byte image."""

    _require_exact_json_value(payload)
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
    )


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(read_pinned_regular_bytes(path))


def require_canonical_absolute_path(value: str | os.PathLike[str], context: str) -> Path:
    text = os.fspath(value)
    require(text.startswith("/") and not text.startswith("//"), f"{context}: one POSIX root slash required")
    require(
        "\x00" not in text
        and "\\" not in text
        and "//" not in text[1:]
        and not text.endswith("/"),
        f"{context}: non-canonical path spelling",
    )
    require(
        all(component not in ("", ".", "..") for component in text[1:].split("/")),
        f"{context}: dot or empty path component",
    )
    path = Path(text)
    require(path.is_absolute() and os.path.abspath(text) == text, f"{context}: normalized path alias")
    return path


def canonical_absolute_argument(value: str) -> Path:
    try:
        return require_canonical_absolute_path(value, "checker CLI path")
    except CheckError as error:
        raise argparse.ArgumentTypeError(str(error)) from error


_ParentChainIdentity = tuple[tuple[str, int, int, int, int, int, int], ...]


def _stable_stat_identity(
    info: os.stat_result,
) -> tuple[int, int, int, int, int, int, int, int, int]:
    """Metadata which must remain stable across one pinned-file transaction.

    Access time is deliberately excluded because a read may update it.  All
    identity, ownership, layout, length, and content-change fields supplied by
    fstat are included.
    """

    return (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_uid,
        info.st_gid,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )


def _directory_stat_identity(
    info: os.stat_result,
) -> tuple[int, int, int, int, int, int]:
    return (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_uid,
        info.st_gid,
    )


def _open_directory_fd_with_chain(path: Path) -> tuple[int, _ParentChainIdentity]:
    path = require_canonical_absolute_path(path, "checker directory path")
    flags = os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    root_info = os.fstat(descriptor)
    require(stat.S_ISDIR(root_info.st_mode), "checker filesystem root is not a directory")
    chain: list[tuple[str, int, int, int, int, int, int]] = [
        ("/", *_directory_stat_identity(root_info))
    ]
    current = Path("/")
    try:
        for component in path.parts[1:]:
            next_fd = os.open(
                component, flags | nofollow, dir_fd=descriptor
            )
            try:
                next_info = os.fstat(next_fd)
                require(
                    stat.S_ISDIR(next_info.st_mode),
                    f"checker path component is not a directory: {current / component}",
                )
            except Exception:
                os.close(next_fd)
                raise
            os.close(descriptor)
            descriptor = next_fd
            current /= component
            chain.append((str(current), *_directory_stat_identity(next_info)))
        return descriptor, tuple(chain)
    except Exception:
        os.close(descriptor)
        raise


def _open_directory_fd(path: Path) -> int:
    descriptor, _chain = _open_directory_fd_with_chain(path)
    return descriptor


@dataclass(frozen=True)
class PinnedRegularSnapshot:
    raw: bytes
    info: os.stat_result
    parent_chain: _ParentChainIdentity


def _pinned_reader_hook(_point: str, _path: Path) -> None:
    """Tests replace this no-op to inject a same-byte inode substitution."""


def _read_pinned_regular_snapshot(
    path: Path,
    *,
    maximum_bytes: int = 512 * 1024 * 1024,
    context: str = "checker input",
) -> PinnedRegularSnapshot:
    path = require_canonical_absolute_path(path, "checker input path")
    require(
        type(maximum_bytes) is int and 0 <= maximum_bytes <= 512 * 1024 * 1024,
        f"{context}: invalid safety cap",
    )
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        directory_fd, parent_chain = _open_directory_fd_with_chain(path.parent)
    except OSError as error:
        raise CheckError(f"{path}: cannot open pinned parent: {error}") from error
    descriptor: int | None = None
    try:
        before = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        require(stat.S_ISREG(before.st_mode), f"{path}: not a regular file")
        require(before.st_nlink == 1, f"{path}: hard-link alias rejected")
        require(
            0 <= before.st_size <= maximum_bytes,
            f"{path}: input exceeds {context} safety cap",
        )
        descriptor = os.open(
            path.name,
            os.O_RDONLY | os.O_NONBLOCK | nofollow,
            dir_fd=directory_fd,
        )
    except OSError as error:
        os.close(directory_fd)
        raise CheckError(f"{path}: cannot open pinned regular file: {error}") from error
    except Exception:
        os.close(directory_fd)
        raise
    try:
        opened = os.fstat(descriptor)
        require(
            stat.S_ISREG(opened.st_mode)
            and _stable_stat_identity(opened) == _stable_stat_identity(before),
            f"{path}: path/inode race before open",
        )
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(
                descriptor,
                min(1024 * 1024, maximum_bytes + 1 - total),
            )
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            require(
                total <= maximum_bytes,
                f"{path}: input grew beyond safety cap during read",
            )
        _pinned_reader_hook("AFTER_READ", path)
        after = os.fstat(descriptor)
        require(
            stat.S_ISREG(after.st_mode)
            and _stable_stat_identity(before) == _stable_stat_identity(after),
            f"{path}: file changed during pinned read",
        )
        raw = b"".join(chunks)
        require(len(raw) == before.st_size, f"{path}: pinned read size mismatch")
        directory_entry = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        require(
            _stable_stat_identity(directory_entry) == _stable_stat_identity(before),
            f"{path}: directory entry changed during pinned read",
        )
        try:
            replay_parent_fd, replay_parent_chain = _open_directory_fd_with_chain(path.parent)
        except OSError as error:
            raise CheckError(f"{path}: lexical parent changed during pinned read: {error}") from error
        try:
            lexical_entry = os.stat(
                path.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
        except OSError as error:
            raise CheckError(f"{path}: lexical path changed during pinned read: {error}") from error
        finally:
            os.close(replay_parent_fd)
        require(
            _stable_stat_identity(lexical_entry) == _stable_stat_identity(before)
            and replay_parent_chain == parent_chain,
            f"{path}: lexical path no longer names pinned inode",
        )
        return PinnedRegularSnapshot(raw=raw, info=after, parent_chain=parent_chain)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_fd)


def read_pinned_regular_bytes(path: Path) -> bytes:
    return _read_pinned_regular_snapshot(path).raw


def write_once(path: Path, payload: bytes) -> None:
    path = require_canonical_absolute_path(path, "checker output path")
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        directory_fd = _open_directory_fd(path.parent)
    except OSError as error:
        raise CheckError(f"checker output parent failed: {error}") from error
    parent_before = os.fstat(directory_fd)
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | nofollow,
            0o644,
            dir_fd=directory_fd,
        )
        view = memoryview(payload)
        while view:
            written = os.write(descriptor, view)
            require(written > 0, "checker short write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        require(
            stat.S_ISREG(info.st_mode)
            and info.st_nlink == 1
            and info.st_size == len(payload),
            "checker output publication mismatch",
        )
        entry = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        require(
            (entry.st_dev, entry.st_ino) == (info.st_dev, info.st_ino),
            "checker output directory entry mismatch",
        )
        try:
            replay_parent_fd = _open_directory_fd(path.parent)
        except OSError as error:
            raise CheckError(f"checker output parent changed: {error}") from error
        try:
            replay_parent = os.fstat(replay_parent_fd)
            replay_entry = os.stat(
                path.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
            require(
                (replay_parent.st_dev, replay_parent.st_ino)
                == (parent_before.st_dev, parent_before.st_ino)
                and (replay_entry.st_dev, replay_entry.st_ino)
                == (info.st_dev, info.st_ino),
                "checker output lexical replay mismatch",
            )
            os.fsync(replay_parent_fd)
        finally:
            os.close(replay_parent_fd)
        os.fsync(directory_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_fd)


def strict_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise CheckError(f"forbidden non-finite JSON number {value}")
    return parsed


def load_canonical_json_with_raw(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = read_pinned_regular_bytes(path)

    def reject_constant(value: str) -> None:
        raise CheckError(f"{path.name}: forbidden non-finite JSON constant {value}")

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        answer: dict[str, Any] = {}
        for key, value in pairs:
            if key in answer:
                raise CheckError(f"{path.name}: duplicate JSON key {key!r}")
            answer[key] = value
        return answer

    try:
        payload = json.loads(
            raw,
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
            parse_float=strict_float,
        )
    except CheckError:
        raise
    except Exception as error:
        raise CheckError(f"{path.name}: invalid JSON: {error}") from error
    require(isinstance(payload, dict), f"{path.name}: JSON root is not an object")
    require(raw == canonical_json_bytes(payload), f"{path.name}: JSON is not canonical")
    return payload, raw


def load_canonical_json(path: Path) -> dict[str, Any]:
    return load_canonical_json_with_raw(path)[0]


def parse_fraction_record(payload: Any, context: str) -> Fraction:
    require(isinstance(payload, dict), f"{context}: fraction is not an object")
    exact_keys(payload, {"numerator", "denominator"}, context)
    numerator_text = payload["numerator"]
    denominator_text = payload["denominator"]
    require(
        isinstance(numerator_text, str) and isinstance(denominator_text, str),
        f"{context}: numerator/denominator must be strings",
    )
    require(
        numerator_text == str(int(numerator_text)),
        f"{context}: numerator is not canonical",
    )
    require(
        denominator_text == str(int(denominator_text)),
        f"{context}: denominator is not canonical",
    )
    numerator = int(numerator_text)
    denominator = int(denominator_text)
    require(denominator > 0, f"{context}: denominator is not positive")
    require(math.gcd(numerator, denominator) == 1, f"{context}: fraction is not reduced")
    return Fraction(numerator, denominator)


def parse_interval_record(payload: Any, context: str) -> tuple[Fraction, Fraction]:
    require(isinstance(payload, list) and len(payload) == 2, f"{context}: interval shape")
    lower = parse_fraction_record(payload[0], f"{context}.lower")
    upper = parse_fraction_record(payload[1], f"{context}.upper")
    require(lower <= upper, f"{context}: reversed interval")
    return lower, upper


def parse_box_record(
    payload: Any,
    coordinates: tuple[str, ...],
    context: str,
) -> dict[str, tuple[Fraction, Fraction]]:
    require(isinstance(payload, dict), f"{context}: box is not an object")
    exact_keys(payload, set(coordinates), context)
    return {
        coordinate: parse_interval_record(payload[coordinate], f"{context}.{coordinate}")
        for coordinate in coordinates
    }


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def point_ball(value: Fraction | int) -> arb:
    return arb(as_fmpq(Fraction(value)))


def interval_ball(interval: tuple[Fraction, Fraction]) -> arb:
    lower, upper = interval
    return arb(as_fmpq((lower + upper) / 2), as_fmpq((upper - lower) / 2))


def square_enclosure(value: arb) -> arb:
    lower = value.lower()
    upper = value.upper()
    zero = arb(0)
    if lower >= zero:
        return arb.union(lower * lower, upper * upper).nonnegative_part()
    if upper <= zero:
        return arb.union(upper * upper, lower * lower).nonnegative_part()
    maximum = max(abs(lower).upper(), abs(upper).upper())
    return arb.union(zero, maximum * maximum).nonnegative_part()


def exprel_enclosure(value: arb) -> arb:
    require(value.lower() >= arb(0), "replay exprel input is not nonnegative")
    order = 16
    result = arb(1)
    summand = arb(1)
    for index in range(1, order + 1):
        summand = summand * value / (index + 1)
        result += summand
    radius = abs(value).upper()
    factorial = math.factorial(order + 2)
    error = radius ** (order + 1) * radius.exp() / factorial
    return result + arb(0, error.upper())


@dataclass(frozen=True)
class IndependentModel:
    a: arb
    c: arb
    pi: arb
    lambda_slow: arb
    lambda_fast: arb
    omega_slow: arb
    omega_fast: arb
    slow_basis: tuple[arb, arb]
    fast_basis: tuple[arb, arb]


def independent_model() -> IndependentModel:
    a = point_ball(Fraction(51, 50))
    pi_value = arb.pi()
    c = 2 * ((1 + a).sqrt() - 1)
    discriminant = c * (c * c + 4).sqrt()
    lambda_slow = (c * c + 2 - discriminant) / 2
    lambda_fast = (c * c + 2 + discriminant) / 2
    slow_raw = (1 - lambda_slow, -c)
    fast_raw = (lambda_fast - 1, c)
    slow_length = (
        square_enclosure(slow_raw[0]) + square_enclosure(slow_raw[1])
    ).sqrt()
    fast_length = (
        square_enclosure(fast_raw[0]) + square_enclosure(fast_raw[1])
    ).sqrt()
    return IndependentModel(
        a=a,
        c=c,
        pi=pi_value,
        lambda_slow=lambda_slow,
        lambda_fast=lambda_fast,
        omega_slow=2 * pi_value * lambda_slow.sqrt(),
        omega_fast=2 * pi_value * lambda_fast.sqrt(),
        slow_basis=(slow_raw[0] / slow_length, slow_raw[1] / slow_length),
        fast_basis=(fast_raw[0] / fast_length, fast_raw[1] / fast_length),
    )


@dataclass(frozen=True)
class ReplayMetrics:
    energy: arb
    tube_squared: arb
    denominator: arb | None
    N_plus: arb | None
    numerator: arb | None
    angular_velocity: arb | None


def recompute_metrics(
    model: IndependentModel,
    epsilon_interval: tuple[Fraction, Fraction],
    box: dict[str, tuple[Fraction, Fraction]],
    *,
    section: bool,
) -> ReplayMetrics:
    epsilon = interval_ball(epsilon_interval)
    qm = interval_ball(box["qminus"])
    qp = interval_ball(box["qplus"])
    pm = interval_ball(box["pminus"])
    pp = arb(0) if section else interval_ball(box["pplus"])

    q1 = model.slow_basis[0] * qm + model.fast_basis[0] * qp
    q2 = model.slow_basis[1] * qm + model.fast_basis[1] * qp
    w1 = -model.c * q1 - q2 - model.a * epsilon * square_enclosure(q1)
    w2 = q1
    w_norm_squared = square_enclosure(w1) + square_enclosure(w2)
    # Positivity is an exact structural fact; remove only the artificial
    # negative sliver introduced by midpoint-radius dependency loss.
    s = (
        model.pi * square_enclosure(epsilon) * w_norm_squared
    ).nonnegative_part()
    potential = (
        2 * model.pi * model.pi * w_norm_squared * exprel_enclosure(s)
    )
    energy = (square_enclosure(pm) + square_enclosure(pp)) / 2 + potential
    tube_squared = square_enclosure(model.omega_slow * qm) + square_enclosure(pm)
    if section:
        return ReplayMetrics(energy, tube_squared, None, None, None, None)

    dw1_dq1 = -model.c - 2 * model.a * epsilon * q1
    radial_factor = 4 * model.pi * model.pi * s.exp()
    grad_q1 = radial_factor * (dw1_dq1 * w1 + w2)
    grad_q2 = -radial_factor * w1
    grad_fast = model.fast_basis[0] * grad_q1 + model.fast_basis[1] * grad_q2
    denominator = square_enclosure(model.omega_fast * qp) + square_enclosure(pp)
    N_plus = square_enclosure(pp) + qp * grad_fast
    # Numerator of theta_dot: omega_fast * N_plus.
    numerator = model.omega_fast * N_plus
    angular_velocity = numerator / denominator
    return ReplayMetrics(
        energy,
        tube_squared,
        denominator,
        N_plus,
        numerator,
        angular_velocity,
    )


def expected_terminal(
    metrics: ReplayMetrics,
    box: dict[str, tuple[Fraction, Fraction]],
    goal: str,
) -> str | None:
    if metrics.tube_squared.lower() > point_ball(TUBE_RADIUS_SQUARED):
        return "TUBE_EXCLUDED"
    if metrics.energy.upper() < point_ball(1) or metrics.energy.lower() > point_ball(1):
        return "ENERGY_EXCLUDED"
    if goal == "ANGLE_COVER":
        assert metrics.denominator is not None
        assert metrics.N_plus is not None
        assert metrics.numerator is not None
        assert metrics.angular_velocity is not None
        if (
            metrics.denominator.lower() > arb(0)
            and metrics.N_plus.lower() > arb(0)
            and metrics.numerator.lower() > arb(0)
            and metrics.angular_velocity.upper() < point_ball(ANGLE_CEILING)
        ):
            return "ANGLE_CERTIFIED"
        return None
    if goal == "SECTION_WINDOW_COVER":
        lower, upper = box["qplus"]
        if lower >= Fraction(12, 100) and upper <= Fraction(17, 100):
            return "LANDING_CLOSED_WINDOW"
    return None


def independently_selected_coordinate(
    box: dict[str, tuple[Fraction, Fraction]],
    root_box: dict[str, tuple[Fraction, Fraction]],
    coordinates: tuple[str, ...],
) -> str:
    best = coordinates[0]
    best_width = Fraction(-1)
    for coordinate in coordinates:
        width = (box[coordinate][1] - box[coordinate][0]) / (
            root_box[coordinate][1] - root_box[coordinate][0]
        )
        if width > best_width:
            best = coordinate
            best_width = width
    return best


def split_exactly(
    box: dict[str, tuple[Fraction, Fraction]], coordinate: str
) -> tuple[Fraction, dict[str, tuple[Fraction, Fraction]], dict[str, tuple[Fraction, Fraction]]]:
    lower, upper = box[coordinate]
    midpoint = (lower + upper) / 2
    left = dict(box)
    right = dict(box)
    left[coordinate] = (lower, midpoint)
    right[coordinate] = (midpoint, upper)
    return midpoint, left, right


def decisive_values(metrics: ReplayMetrics, classification: str) -> dict[str, arb]:
    if classification == "TUBE_EXCLUDED":
        return {"tube_squared": metrics.tube_squared}
    if classification == "ENERGY_EXCLUDED":
        return {"energy": metrics.energy}
    if classification == "ANGLE_CERTIFIED":
        assert metrics.denominator is not None
        assert metrics.N_plus is not None
        assert metrics.numerator is not None
        assert metrics.angular_velocity is not None
        return {
            "D_plus": metrics.denominator,
            "N_plus": metrics.N_plus,
            "theta_numerator": metrics.numerator,
            "theta_dot": metrics.angular_velocity,
        }
    if classification == "LANDING_CLOSED_WINDOW":
        return {}
    raise CheckError(f"unknown terminal class {classification}")


def verify_printed_intervals(
    stored: Any,
    recomputed: dict[str, arb],
    context: str,
) -> int:
    require(isinstance(stored, dict), f"{context}: decisive_intervals not object")
    exact_keys(stored, set(recomputed), context)
    checks = 0
    for key, value in recomputed.items():
        text = stored[key]
        require(isinstance(text, str), f"{context}.{key}: not text")
        try:
            printed = arb(text)
        except Exception as error:
            raise CheckError(f"{context}.{key}: invalid Arb text: {error}") from error
        require(
            printed.contains(value),
            f"{context}.{key}: printed interval does not contain recomputation",
        )
        checks += 1
    return checks


def replay_tree(
    payload: Any,
    epsilon: tuple[Fraction, Fraction],
    model: IndependentModel,
    expected_tree_id: str,
    expected_root: dict[str, tuple[Fraction, Fraction]],
) -> dict[str, Any]:
    require(isinstance(payload, dict), f"{expected_tree_id}: tree not object")
    exact_keys(
        payload,
        {
            "tree_id",
            "goal",
            "coordinates",
            "root_box",
            "split_rule",
            "node_count",
            "internal_count",
            "terminal_count",
            "unresolved_count",
            "maximum_depth",
            "terminal_counts",
            "angle_extrema",
            "complete",
            "nodes",
            "content_hash_definition",
            "content_sha256",
        },
        expected_tree_id,
    )
    require(
        payload["content_hash_definition"]
        == "sha256(canonical_json(tree_without_content_sha256))",
        f"{expected_tree_id}: content-hash definition",
    )
    content_sha256 = payload["content_sha256"]
    require(
        isinstance(content_sha256, str)
        and len(content_sha256) == 64
        and all(character in "0123456789abcdef" for character in content_sha256),
        f"{expected_tree_id}: malformed content hash",
    )
    without_content_hash = dict(payload)
    del without_content_hash["content_sha256"]
    require(
        content_sha256 == sha256_bytes(canonical_json_bytes(without_content_hash)),
        f"{expected_tree_id}: content hash mismatch",
    )
    require(payload["tree_id"] == expected_tree_id, f"{expected_tree_id}: id mismatch")
    goal = payload["goal"]
    require(goal in {"ANGLE_COVER", "SECTION_WINDOW_COVER"}, f"{expected_tree_id}: goal")
    coordinates = ANGLE_COORDINATES if goal == "ANGLE_COVER" else SECTION_COORDINATES
    require(payload["coordinates"] == list(coordinates), f"{expected_tree_id}: coordinates")
    require(
        payload["split_rule"]
        == "largest_normalized_width_then_coordinate_order_exact_midpoint",
        f"{expected_tree_id}: split rule",
    )
    root = parse_box_record(payload["root_box"], coordinates, f"{expected_tree_id}.root")
    require(root == expected_root, f"{expected_tree_id}: unexpected root geometry")
    nodes = payload["nodes"]
    require(isinstance(nodes, list) and nodes, f"{expected_tree_id}: empty nodes")
    require_exact_int(
        payload["node_count"],
        f"{expected_tree_id}.node_count",
        expected=len(nodes),
    )
    require_exact_int(
        payload["maximum_depth"],
        f"{expected_tree_id}.maximum_depth",
        minimum=0,
    )
    require_exact_int(payload["internal_count"], f"{expected_tree_id}.internal_count", minimum=0)
    require_exact_int(payload["terminal_count"], f"{expected_tree_id}.terminal_count", minimum=1)
    require_exact_int(
        payload["unresolved_count"],
        f"{expected_tree_id}.unresolved_count",
        expected=0,
    )
    require(isinstance(payload["terminal_counts"], dict), f"{expected_tree_id}: terminal counts object")
    for terminal_name, count in payload["terminal_counts"].items():
        require(isinstance(terminal_name, str), f"{expected_tree_id}: terminal name type")
        require_exact_int(count, f"{expected_tree_id}.terminal_counts.{terminal_name}", minimum=0)
    require(payload["complete"] is True, f"{expected_tree_id}: incomplete")
    index = 0
    terminal_counts: dict[str, int] = {}
    internal_count = 0
    maximum_depth = 0
    interval_checks = 0
    minimum_D_lower: arb | None = None
    minimum_N_lower: arb | None = None
    minimum_theta_numerator_lower: arb | None = None
    maximum_theta_dot_upper: arb | None = None

    def replay(
        node_id: str,
        parent_id: str | None,
        depth: int,
        box: dict[str, tuple[Fraction, Fraction]],
    ) -> None:
        nonlocal index, maximum_depth, interval_checks, internal_count
        nonlocal minimum_D_lower, minimum_N_lower
        nonlocal minimum_theta_numerator_lower, maximum_theta_dot_upper
        require(index < len(nodes), f"{expected_tree_id}: missing node {node_id}")
        node = nodes[index]
        index += 1
        require(isinstance(node, dict), f"{node_id}: node is not object")
        maximum_depth = max(maximum_depth, depth)
        require(node.get("node_id") == node_id, f"{node_id}: node id mismatch")
        require(node.get("parent_id") == parent_id, f"{node_id}: parent mismatch")
        require_exact_int(node.get("depth"), f"{node_id}.depth", expected=depth)
        metrics = recompute_metrics(
            model,
            epsilon,
            box,
            section=goal != "ANGLE_COVER",
        )
        terminal = expected_terminal(metrics, box, goal)
        if terminal is not None:
            exact_keys(
                node,
                {"node_id", "parent_id", "depth", "classification", "decisive_intervals"},
                node_id,
            )
            require(node["classification"] == terminal, f"{node_id}: terminal class mismatch")
            interval_checks += verify_printed_intervals(
                node["decisive_intervals"],
                decisive_values(metrics, terminal),
                f"{node_id}.decisive_intervals",
            )
            if terminal == "ANGLE_CERTIFIED":
                assert metrics.denominator is not None
                assert metrics.N_plus is not None
                assert metrics.numerator is not None
                assert metrics.angular_velocity is not None
                D_lower = metrics.denominator.lower()
                N_lower = metrics.N_plus.lower()
                numerator_lower = metrics.numerator.lower()
                theta_upper = metrics.angular_velocity.upper()
                minimum_D_lower = (
                    D_lower if minimum_D_lower is None else min(minimum_D_lower, D_lower)
                )
                minimum_N_lower = (
                    N_lower if minimum_N_lower is None else min(minimum_N_lower, N_lower)
                )
                minimum_theta_numerator_lower = (
                    numerator_lower
                    if minimum_theta_numerator_lower is None
                    else min(minimum_theta_numerator_lower, numerator_lower)
                )
                maximum_theta_dot_upper = (
                    theta_upper
                    if maximum_theta_dot_upper is None
                    else max(maximum_theta_dot_upper, theta_upper)
                )
            terminal_counts[terminal] = terminal_counts.get(terminal, 0) + 1
            return

        exact_keys(
            node,
            {"node_id", "parent_id", "depth", "classification", "split_coordinate", "split_point"},
            node_id,
        )
        require(node["classification"] == "SPLIT", f"{node_id}: expected split")
        internal_count += 1
        coordinate = independently_selected_coordinate(box, root, coordinates)
        require(node["split_coordinate"] == coordinate, f"{node_id}: split coordinate")
        midpoint, left, right = split_exactly(box, coordinate)
        recorded_midpoint = parse_fraction_record(node["split_point"], f"{node_id}.split_point")
        require(recorded_midpoint == midpoint, f"{node_id}: non-dyadic split geometry")
        replay(node_id + "0", node_id, depth + 1, left)
        replay(node_id + "1", node_id, depth + 1, right)

    replay(expected_tree_id, None, 0, root)
    require(index == len(nodes), f"{expected_tree_id}: unreachable trailing nodes")
    require_exact_int(
        payload["maximum_depth"],
        f"{expected_tree_id}.maximum_depth",
        expected=maximum_depth,
    )
    require_json_exact(
        payload["terminal_counts"],
        dict(sorted(terminal_counts.items())),
        f"{expected_tree_id}.terminal_counts",
    )
    terminal_count = sum(terminal_counts.values())
    require_exact_int(
        payload["internal_count"],
        f"{expected_tree_id}.internal_count",
        expected=internal_count,
    )
    require_exact_int(
        payload["terminal_count"],
        f"{expected_tree_id}.terminal_count",
        expected=terminal_count,
    )
    require(len(nodes) == internal_count + terminal_count, f"{expected_tree_id}: node accounting")
    if goal == "ANGLE_COVER":
        require(
            all(
                value is not None
                for value in (
                    minimum_D_lower,
                    minimum_N_lower,
                    minimum_theta_numerator_lower,
                    maximum_theta_dot_upper,
                )
            ),
            f"{expected_tree_id}: missing recomputed angle extrema",
        )
        stored_extrema = payload["angle_extrema"]
        require(isinstance(stored_extrema, dict), f"{expected_tree_id}: extrema object")
        exact_keys(
            stored_extrema,
            {
                "minimum_D_plus_lower",
                "minimum_N_plus_lower",
                "minimum_theta_numerator_lower",
                "maximum_theta_dot_upper",
                "theta_numerator_definition",
            },
            f"{expected_tree_id}.angle_extrema",
        )
        require(
            stored_extrema["theta_numerator_definition"] == "omega_fast_times_N_plus",
            f"{expected_tree_id}: theta numerator definition",
        )
        interval_checks += verify_printed_intervals(
            {
                key: value
                for key, value in stored_extrema.items()
                if key != "theta_numerator_definition"
            },
            {
                "minimum_D_plus_lower": minimum_D_lower,
                "minimum_N_plus_lower": minimum_N_lower,
                "minimum_theta_numerator_lower": minimum_theta_numerator_lower,
                "maximum_theta_dot_upper": maximum_theta_dot_upper,
            },
            f"{expected_tree_id}.angle_extrema",
        )
    else:
        require(payload["angle_extrema"] is None, f"{expected_tree_id}: unexpected angle extrema")
    return {
        "tree_id": expected_tree_id,
        "node_count": len(nodes),
        "internal_count": internal_count,
        "terminal_count": terminal_count,
        "unresolved_count": 0,
        "terminal_counts": terminal_counts,
        "interval_checks": interval_checks,
        "maximum_depth": maximum_depth,
        "content_sha256": content_sha256,
        "angle_extrema": payload["angle_extrema"],
    }


def verify_outer_containment(
    payload: Any,
    model: IndependentModel,
    bits: int,
    context: str,
) -> int:
    require(isinstance(payload, dict), f"{context}: outer containment not object")
    exact_keys(payload, {"derivation", "values", "gates", "all_pass"}, context)
    require(payload["derivation"] == EXPECTED_DERIVATION, f"{context}: derivation text")
    sqrt_two = point_ball(2).sqrt()
    w_bound = 1 / (sqrt_two * model.pi)
    qplus_bound = (
        w_bound + model.a * point_ball(EPSILON_CAP) * square_enclosure(w_bound)
    ) / model.lambda_fast.sqrt()
    qminus_bound = point_ball(Fraction(6, 100)) / model.omega_slow
    winding_bound = 4 * model.pi / point_ball(PERIOD_MAX)
    values = {
        "qminus_bound": qminus_bound,
        "qplus_bound": qplus_bound,
        "pplus_bound": sqrt_two,
        "four_pi_over_period_max": winding_bound,
    }
    expected_gates = {
        "qminus_bound_lt_0.015": qminus_bound.upper() < point_ball(Fraction(15, 1000)),
        "qplus_bound_lt_0.18": qplus_bound.upper() < point_ball(Fraction(18, 100)),
        "pplus_bound_lt_1.415": sqrt_two.upper() < point_ball(Fraction(1415, 1000)),
        "theta_ceiling_18_lt_four_pi_over_0.69": point_ball(18) < winding_bound.lower(),
    }
    require_json_exact(payload["gates"], expected_gates, f"{context}.gates")
    require(payload["all_pass"] is True and all(expected_gates.values()), f"{context}: gate failure")
    return verify_printed_intervals(payload["values"], values, f"{context}.values")


def load_strict_json_object_from_bytes(raw: bytes, path: Path) -> dict[str, Any]:
    """Parse one already-pinned byte image as a strict JSON object."""

    def reject_constant(value: str) -> None:
        raise CheckError(f"{path.name}: forbidden non-finite JSON constant {value}")

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        answer: dict[str, Any] = {}
        for key, value in pairs:
            if key in answer:
                raise CheckError(f"{path.name}: duplicate JSON key {key!r}")
            answer[key] = value
        return answer

    try:
        payload = json.loads(
            raw,
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
            parse_float=strict_float,
        )
    except CheckError:
        raise
    except Exception as error:
        raise CheckError(f"{path.name}: invalid JSON: {error}") from error
    require(isinstance(payload, dict), f"{path.name}: root is not an object")
    return payload


def load_strict_json_object(path: Path) -> dict[str, Any]:
    return load_strict_json_object_with_raw(path)[0]


def load_strict_json_object_with_raw(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = read_pinned_regular_bytes(path)
    return load_strict_json_object_from_bytes(raw, path), raw


def project_relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def project_bound_path(value: Any, context: str) -> Path:
    require(type(value) is str and value and not value.startswith("/"), f"{context}: project-relative path")
    require(
        "\x00" not in value
        and "\\" not in value
        and "//" not in value
        and not value.endswith("/")
        and all(component not in ("", ".", "..") for component in value.split("/")),
        f"{context}: unsafe project path",
    )
    return require_canonical_absolute_path(ROOT / value, context)


def validate_bound_hash_map(
    payload: Any,
    expected_paths: set[str],
    context: str,
    captured_hashes: dict[str, str] | None = None,
) -> None:
    require(isinstance(payload, dict), f"{context}: hash map is not object")
    exact_keys(payload, expected_paths, context)
    for relative in sorted(expected_paths):
        expected_hash = payload[relative]
        require(
            type(expected_hash) is str
            and len(expected_hash) == 64
            and all(character in "0123456789abcdef" for character in expected_hash),
            f"{context}: invalid SHA-256 for {relative}",
        )
        actual_hash = (
            captured_hashes[relative]
            if captured_hashes is not None and relative in captured_hashes
            else sha256_file(project_bound_path(relative, context))
        )
        require(
            actual_hash == expected_hash,
            f"{context}: byte hash mismatch for {relative}",
        )


def independently_validate_l1_bundle() -> tuple[dict[str, str], dict[str, Any], str]:
    """Replay the accepted L1 chain and return its captured PLAN image.

    The parsed slab semantics and the PLAN digest deliberately come from the
    same pinned byte snapshot.  Callers must propagate the returned bindings
    rather than reopen PLAN during the same proof verification.
    """

    images = {
        path: load_strict_json_object_with_raw(path)
        for path in L1_RELEASE_CHAIN
    }
    summary, _ = images[L1_SUMMARY]
    manifest, _ = images[L1_MANIFEST]
    checker, _ = images[L1_CHECKER]
    postcheck, _ = images[L1_POSTCHECK]
    release, _ = images[L1_RELEASE]
    plan_raw = read_pinned_regular_bytes(PLAN)
    plan_payload = load_strict_json_object_from_bytes(plan_raw, PLAN)
    captured_hashes = {
        project_relative(path): sha256_bytes(raw)
        for path, (_, raw) in images.items()
    }
    captured_hashes[project_relative(PLAN)] = sha256_bytes(plan_raw)
    exact_keys(summary, L1_SUMMARY_KEYS, "accepted L1 summary")
    exact_keys(manifest, L1_MANIFEST_KEYS, "accepted L1 manifest")
    exact_keys(checker, L1_CHECKER_KEYS, "accepted L1 checker")
    exact_keys(postcheck, L1_POSTCHECK_KEYS, "accepted L1 postcheck")
    exact_keys(release, L1_RELEASE_KEYS, "accepted L1 release")
    require(
        summary.get("protocol_id") == "R401-VAL-L1-V2"
        and summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and summary.get("final_status") is None
        and summary.get("claim_boundary") == L1_SUMMARY_BOUNDARY,
        "accepted L1 summary status gate",
    )
    require(
        manifest.get("protocol_id") == "R401-VAL-L1-V2"
        and manifest.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and manifest.get("final_status") is None
        and manifest.get("capd_commit") == "731079217a9254ea2948d742df2b170895effe7f",
        "accepted L1 manifest status gate",
    )
    require(
        checker.get("protocol_id") == "R401-VAL-L1-V2"
        and checker.get("checker_status") == "PASS"
        and checker.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and checker.get("final_status") is None
        and checker.get("job_failures") == []
        and checker.get("manifest_hash_failures") == []
        and checker.get("scope")
        == "independent exact-rational replay of archived Krawczyk arithmetic, plan coverage, bridge gluing, phase gates, and hashes; not an independent ODE integration",
        "accepted L1 checker status gate",
    )
    require(
        postcheck.get("protocol_id") == "R401-VAL-L1-V2"
        and postcheck.get("checker_status") == "PASS"
        and postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and postcheck.get("final_status") is None,
        "accepted L1 postcheck status gate",
    )
    require(
        release.get("protocol_id") == "R401-VAL-L1-V2"
        and release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and release.get("final_status") is None
        and release.get("scope")
        == "Post-production provenance binding; uniqueness is only inside the frozen local primary boxes and guarded bridge hulls.",
        "accepted L1 release status gate",
    )
    manifest_files = manifest.get("files")
    require(
        isinstance(manifest_files, dict) and len(manifest_files) == 417,
        "accepted L1 manifest exact file count",
    )
    require(
        manifest_files.get(project_relative(PLAN))
        == captured_hashes[project_relative(PLAN)],
        "accepted L1 manifest final-plan binding",
    )
    validate_bound_hash_map(
        postcheck.get("files"),
        L1_POSTCHECK_FILES,
        "accepted L1 postcheck files",
        captured_hashes,
    )
    validate_bound_hash_map(
        release.get("files"),
        L1_RELEASE_FILES,
        "accepted L1 release files",
        captured_hashes,
    )
    hashes = {
        project_relative(path): captured_hashes[project_relative(path)]
        for path in L1_RELEASE_CHAIN
    }
    return hashes, plan_payload, captured_hashes[project_relative(PLAN)]


def independently_validate_l1_release_chain() -> dict[str, str]:
    return independently_validate_l1_bundle()[0]


class ValidatedPlanRecord(dict[str, Any]):
    validated_source_bindings: dict[str, Any]


def expected_source_bindings(
    plan_record: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if isinstance(plan_record, ValidatedPlanRecord):
        bindings = plan_record.validated_source_bindings
        return {
            **bindings,
            "l1_release_chain_sha256": dict(bindings["l1_release_chain_sha256"]),
        }
    hashes, plan_payload, plan_hash = independently_validate_l1_bundle()
    del plan_payload
    return {
        "evaluator_sha256": sha256_file(EVALUATOR),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": plan_hash,
        "l1_release_chain_sha256": hashes,
    }


def verify_source_bindings(
    payload: Any,
    context: str,
    plan_record: Mapping[str, Any] | None = None,
) -> None:
    require(isinstance(payload, dict), f"{context}: bindings not object")
    exact_keys(
        payload,
        {
            "evaluator_sha256",
            "checker_sha256",
            "l1_final_plan_sha256",
            "l1_release_chain_sha256",
        },
        context,
    )
    expected = expected_source_bindings(plan_record)
    require_json_exact(payload, expected, f"{context}: source binding mismatch")


def load_plan() -> dict[str, dict[str, Any]]:
    hashes, payload, plan_hash = independently_validate_l1_bundle()
    require(isinstance(payload.get("slabs"), list), "L1 plan slab list")
    bindings = {
        "evaluator_sha256": sha256_file(EVALUATOR),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": plan_hash,
        "l1_release_chain_sha256": hashes,
    }
    records: dict[str, dict[str, Any]] = {}
    for record in payload["slabs"]:
        require(isinstance(record, dict), "L1 plan slab record")
        slab_id = record.get("slab_id")
        require(type(slab_id) is str and slab_id in SLABS, "L1 plan slab id")
        require(slab_id not in records, "duplicate L1 plan slab")
        captured = ValidatedPlanRecord(record)
        captured.validated_source_bindings = bindings
        records[slab_id] = captured
    require(list(records) == list(SLABS), "L1 plan exact ordered 51 slabs")
    return records


def plan_epsilon(plan: dict[str, dict[str, Any]], slab_id: str) -> tuple[Fraction, Fraction]:
    record = plan[slab_id]
    return Fraction(str(record["epsilon_lower"])), Fraction(str(record["epsilon_upper"]))


def plan_record_sha256(record: dict[str, Any]) -> str:
    # The validated wrapper has provenance state outside the JSON data model.
    return sha256_bytes(canonical_json_bytes(dict(record)))


@dataclass(frozen=True)
class FormalStaticContext:
    matrix_id: str
    freeze_sha256: str
    run_config_sha256: str
    max_depth: int
    max_nodes_per_tree: int
    max_nodes_per_cell: int


def validate_formal_context(context: FormalStaticContext) -> None:
    for label in ("matrix_id", "freeze_sha256", "run_config_sha256"):
        value = getattr(context, label)
        require(
            type(value) is str
            and len(value) == 64
            and all(character in "0123456789abcdef" for character in value),
            f"context.{label}: lowercase SHA-256 required",
        )
    for label in ("max_depth", "max_nodes_per_tree", "max_nodes_per_cell"):
        value = getattr(context, label)
        require(
            type(value) is int and value > 0,
            f"context.{label}: positive exact integer required",
        )
    require(
        context.max_nodes_per_cell >= context.max_nodes_per_tree,
        "context: cell node cap below tree node cap",
    )


def verify_proof(
    path: Path,
    *,
    expected_bits: int,
    expected_slab: str,
    plan: dict[str, dict[str, Any]],
    context: FormalStaticContext,
) -> dict[str, Any]:
    validate_formal_context(context)
    payload, proof_raw = load_canonical_json_with_raw(path)
    exact_keys(
        payload,
        {
            "schema_version",
            "protocol_id",
            "artifact_role",
            "authority",
            "scientific_licensing_enabled",
            "matrix_id",
            "freeze_sha256",
            "run_config_sha256",
            "component_status",
            "milestone_status",
            "theorem_status",
            "final_status",
            "evaluator_status",
            "slab_id",
            "precision_bits",
            "epsilon",
            "period_window",
            "input_echo",
            "claim_boundary",
            "proof_complete",
            "outer_containment",
            "trees",
            "counts",
            "source_bindings",
            "proof_content_hash_definition",
            "proof_content_sha256",
        },
        path.name,
    )
    require_exact_int(payload["schema_version"], f"{path.name}.schema_version", expected=SCHEMA_VERSION)
    require(payload["protocol_id"] == PROTOCOL_ID, f"{path.name}: protocol")
    require(payload["artifact_role"] == CELL_ROLE, f"{path.name}: artifact role")
    require(payload["authority"] == "PRODUCER_ONLY", f"{path.name}: authority")
    require(payload["scientific_licensing_enabled"] is False, f"{path.name}: licensing flag")
    require(payload["matrix_id"] == context.matrix_id, f"{path.name}: matrix id")
    require(payload["freeze_sha256"] == context.freeze_sha256, f"{path.name}: freeze")
    require(payload["run_config_sha256"] == context.run_config_sha256, f"{path.name}: run config")
    require(payload["component_status"] is None, f"{path.name}: producer component status")
    require(payload["milestone_status"] is None, f"{path.name}: milestone status")
    require(payload["theorem_status"] is None, f"{path.name}: theorem status")
    require(payload["final_status"] is None, f"{path.name}: final status")
    require(payload["evaluator_status"] == CELL_PASS_STATUS, f"{path.name}: evaluator status")
    require(payload["proof_complete"] is True, f"{path.name}: proof completeness")
    require(payload["slab_id"] == expected_slab, f"{path.name}: slab")
    require_exact_int(payload["precision_bits"], f"{path.name}.precision_bits", expected=expected_bits)
    require(payload["claim_boundary"] == CELL_CLAIM_BOUNDARY, f"{path.name}: claim boundary")
    epsilon = parse_interval_record(payload["epsilon"], f"{path.name}.epsilon")
    require(epsilon == plan_epsilon(plan, expected_slab), f"{path.name}: plan epsilon")
    require(
        parse_interval_record(payload["period_window"], f"{path.name}.period_window")
        == (Fraction(64, 100), PERIOD_MAX),
        f"{path.name}: period window",
    )
    record = plan[expected_slab]
    require_json_exact(
        payload["input_echo"],
        {
            "slab_id": expected_slab,
            "precision_bits": expected_bits,
            "epsilon_lower": record["epsilon_lower"],
            "epsilon_upper": record["epsilon_upper"],
            "matrix_id": context.matrix_id,
            "freeze_sha256": context.freeze_sha256,
            "run_config_sha256": context.run_config_sha256,
            "plan_record_sha256": plan_record_sha256(record),
            "max_depth": context.max_depth,
            "max_nodes_per_tree": context.max_nodes_per_tree,
            "max_nodes_per_cell": context.max_nodes_per_cell,
        },
        f"{path.name}.input_echo",
    )
    verify_source_bindings(
        payload["source_bindings"],
        f"{path.name}.source_bindings",
        record,
    )
    require(
        payload["proof_content_hash_definition"]
        == "sha256(canonical_json(proof_without_proof_content_sha256))",
        f"{path.name}: proof hash definition",
    )
    without_hash = dict(payload)
    stored_content_hash = without_hash.pop("proof_content_sha256")
    require(
        stored_content_hash == sha256_bytes(canonical_json_bytes(without_hash)),
        f"{path.name}: proof content hash",
    )

    previous_precision = ctx.prec
    ctx.prec = expected_bits
    try:
        model = independent_model()
        interval_checks = verify_outer_containment(
            payload["outer_containment"], model, expected_bits, f"{path.name}.outer"
        )
        trees = payload["trees"]
        require(isinstance(trees, list) and len(trees) == 4, f"{path.name}: tree matrix")
        expected = [
            ("ANGLE", ANGLE_ROOT),
            *[(tree_id, SECTION_ROOTS[tree_id]) for tree_id in SECTION_ROOTS],
        ]
        results = [
            replay_tree(tree, epsilon, model, tree_id, root)
            for tree, (tree_id, root) in zip(trees, expected, strict=True)
        ]
        interval_checks += sum(item["interval_checks"] for item in results)
    finally:
        ctx.prec = previous_precision

    result_by_id = {item["tree_id"]: item for item in results}
    for result in results:
        require(
            result["node_count"] <= context.max_nodes_per_tree,
            f"{path.name}: tree node count exceeds frozen per-tree cap",
        )
        require(
            result["maximum_depth"] <= context.max_depth,
            f"{path.name}: tree depth exceeds frozen cap",
        )
    require(
        sum(item["node_count"] for item in results) <= context.max_nodes_per_cell,
        f"{path.name}: cell node count exceeds frozen cap",
    )
    require(result_by_id["ANGLE"]["terminal_counts"].get("ANGLE_CERTIFIED", 0) > 0, f"{path.name}: no angle leaves")
    for tree_id in ("SECTION_LOW", "SECTION_HIGH"):
        require(
            set(result_by_id[tree_id]["terminal_counts"])
            <= {"ENERGY_EXCLUDED", "TUBE_EXCLUDED"},
            f"{path.name}: {tree_id} retained a section candidate",
        )
    require_json_exact(
        result_by_id["SECTION_WINDOW"]["terminal_counts"],
        {"LANDING_CLOSED_WINDOW": 1},
        f"{path.name}: middle section window contract",
    )
    counts = payload["counts"]
    require(isinstance(counts, dict), f"{path.name}: counts object")
    exact_keys(
        counts,
        {
            "tree_count",
            "node_count",
            "internal_count",
            "terminal_count",
            "unresolved_count",
            "maximum_depth",
        },
        f"{path.name}.counts",
    )
    require_exact_int(counts["tree_count"], f"{path.name}.counts.tree_count", expected=4)
    require_exact_int(
        counts["node_count"],
        f"{path.name}.counts.node_count",
        expected=sum(item["node_count"] for item in results),
    )
    require_exact_int(
        counts["internal_count"],
        f"{path.name}.counts.internal_count",
        expected=sum(item["internal_count"] for item in results),
    )
    require_exact_int(
        counts["terminal_count"],
        f"{path.name}.counts.terminal_count",
        expected=sum(item["terminal_count"] for item in results),
    )
    require_exact_int(
        counts["unresolved_count"],
        f"{path.name}.counts.unresolved_count",
        expected=0,
    )
    require_exact_int(
        counts["maximum_depth"],
        f"{path.name}.counts.maximum_depth",
        expected=max(item["maximum_depth"] for item in results),
    )
    return {
        "path": path.name,
        "precision_bits": expected_bits,
        "slab_id": expected_slab,
        "node_count": counts["node_count"],
        "internal_count": counts["internal_count"],
        "terminal_count": counts["terminal_count"],
        "unresolved_count": counts["unresolved_count"],
        "maximum_depth": counts["maximum_depth"],
        "interval_checks": interval_checks,
        "sha256": sha256_bytes(proof_raw),
        "tree_content_sha256": {
            item["tree_id"]: item["content_sha256"] for item in results
        },
        "angle_extrema": result_by_id["ANGLE"]["angle_extrema"],
    }


def exact_sha256(value: Any, context: str) -> str:
    require(
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value),
        f"{context}: lower-case SHA-256 required",
    )
    return value


def exact_bool(value: Any, context: str, expected: bool) -> None:
    require(type(value) is bool and value is expected, f"{context}: expected {expected}")


def directory_names(path: Path, context: str) -> set[str]:
    """List one directory through a no-follow descriptor and pin its identity."""

    path = require_canonical_absolute_path(path, context)
    try:
        descriptor = _open_directory_fd(path)
    except OSError as error:
        raise CheckError(f"{context}: cannot open directory: {error}") from error
    try:
        before = os.fstat(descriptor)
        require(stat.S_ISDIR(before.st_mode), f"{context}: not a directory")
        names = os.listdir(descriptor)
        after = os.fstat(descriptor)
        require(
            (
                before.st_dev,
                before.st_ino,
                before.st_mode,
                before.st_mtime_ns,
                before.st_ctime_ns,
            )
            == (
                after.st_dev,
                after.st_ino,
                after.st_mode,
                after.st_mtime_ns,
                after.st_ctime_ns,
            ),
            f"{context}: directory changed during scan",
        )
        require(len(names) == len(set(names)), f"{context}: duplicate directory entry")
        for name in names:
            require(
                name not in ("", ".", "..")
                and "/" not in name
                and "\\" not in name
                and "\x00" not in name,
                f"{context}: unsafe directory entry",
            )
        return set(names)
    finally:
        os.close(descriptor)


def require_exact_directory_names(path: Path, expected: set[str], context: str) -> None:
    actual = directory_names(path, context)
    require(
        actual == expected,
        f"{context}: namespace differs; missing={sorted(expected-actual)}, "
        f"extra={sorted(actual-expected)}",
    )


def project_relative_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError as error:
        raise CheckError(f"{path}: path is outside project root") from error


def mock_matrix_payload() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": slab_id}
        for bits in PRECISIONS
        for slab_id in SLABS
    ]


def mock_matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(mock_matrix_payload()))


def mock_candidate_limits() -> dict[str, Any]:
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


MOCK_RUN_CONFIG_KEYS = {
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


def validate_mock_source_bindings(payload: Any, context: str) -> dict[str, str]:
    require(isinstance(payload, dict), f"{context}: not an object")
    expected_paths = {project_relative_path(path) for path in MOCK_SOURCE_PATHS}
    exact_keys(payload, expected_paths, context)
    answer: dict[str, str] = {}
    for path in MOCK_SOURCE_PATHS:
        relative = project_relative_path(path)
        expected = exact_sha256(payload[relative], f"{context}.{relative}")
        actual = sha256_file(path)
        require(actual == expected, f"{context}.{relative}: live source hash mismatch")
        answer[relative] = actual
    return answer


def validate_quiescent_mock_operational(path: Path) -> None:
    """Reject retained task owners while allowing the two empty stage trees."""

    if not os.path.lexists(path):
        return
    require_exact_directory_names(path, {"staging"}, "mock operational root")
    staging = path / "staging"
    components = directory_names(staging, "mock operational staging")
    require(
        components <= {"static", "branch"} and "static" in components,
        "mock operational staging: unexpected component namespace",
    )
    for component in sorted(components):
        component_root = staging / component
        require_exact_directory_names(
            component_root,
            {str(bits) for bits in PRECISIONS},
            f"mock {component} staging root",
        )
        for bits in PRECISIONS:
            require_exact_directory_names(
                component_root / str(bits),
                set(),
                f"mock {component} staging {bits}",
            )


def validate_mock_run_config(
    input_dir: Path,
) -> tuple[dict[str, Any], bytes, str, dict[str, str]]:
    payload, raw = load_canonical_json_with_raw(input_dir / "run_config.json")
    exact_keys(payload, MOCK_RUN_CONFIG_KEYS, "mock run config")
    require_exact_int(payload["schema_version"], "mock run config.schema_version", expected=1)
    require(payload["protocol_id"] == PROTOCOL_ID, "mock run config: protocol")
    require(payload["artifact_role"] == "RUN_CONFIG", "mock run config: role")
    require(payload["artifact_status"] == MOCK_ARTIFACT_STATUS, "mock run config: status")
    require(payload["authority"] == "PRODUCER_ONLY", "mock run config: authority")
    exact_bool(payload["mock_only"], "mock run config.mock_only", True)
    exact_bool(payload["production_authorized"], "mock run config.production_authorized", False)
    exact_bool(
        payload["scientific_licensing_enabled"],
        "mock run config.scientific_licensing_enabled",
        False,
    )
    require_json_exact(payload["matrix"], mock_matrix_payload(), "mock run config.matrix")
    matrix_id = mock_matrix_id()
    require(payload["matrix_id"] == matrix_id, "mock run config: matrix digest")
    require(
        payload["scheduler_policy"] == "deterministic_component_barrier_batches_v1",
        "mock run config: scheduler policy",
    )
    require_json_exact(payload["limits"], mock_candidate_limits(), "mock run config.limits")
    require_json_exact(
        payload["main_freeze"],
        {"path": None, "sha256": None},
        "mock run config.main_freeze",
    )
    require_json_exact(
        payload["machine_freeze"],
        {"path": None, "sha256": None},
        "mock run config.machine_freeze",
    )
    require_json_exact(
        payload["prefreeze_review"],
        {"path": None, "sha256": None, "accepted": False},
        "mock run config.prefreeze_review",
    )
    require(payload["claim_boundary"] == MOCK_PRODUCER_CLAIM_BOUNDARY, "mock run config: claim boundary")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[key] is None, f"mock run config: unauthorized {key}")
    paths = payload["paths"]
    require(isinstance(paths, dict), "mock run config.paths: not an object")
    exact_keys(paths, {"authoritative_root", "operational_root"}, "mock run config.paths")
    authoritative = require_canonical_absolute_path(
        paths["authoritative_root"], "mock run config authoritative root"
    )
    operational = require_canonical_absolute_path(
        paths["operational_root"], "mock run config operational root"
    )
    require(authoritative == input_dir, "mock run config: authoritative root mismatch")
    require(
        operational == input_dir.with_name(input_dir.name + ".operational"),
        "mock run config: operational sibling mismatch",
    )
    bindings = validate_mock_source_bindings(
        payload["source_bindings"], "mock run config.source_bindings"
    )
    validate_quiescent_mock_operational(operational)
    return payload, raw, sha256_bytes(raw), bindings


def validate_cell_identity(payload: Any, bits: int, slab_id: str, context: str) -> None:
    require(isinstance(payload, dict), f"{context}: not an object")
    exact_keys(payload, {"precision_bits", "slab_id"}, context)
    require_exact_int(payload["precision_bits"], f"{context}.precision_bits", expected=bits)
    require(payload["slab_id"] == slab_id, f"{context}: slab id")


FORMAL_STATIC_RECORD_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "authority",
    "scientific_licensing_enabled",
    "matrix_id",
    "freeze_sha256",
    "main_freeze_sha256",
    "run_config_sha256",
    "cell",
    "task",
    "semantic_invocation",
    "scheduler_result",
    "evaluator_result",
    "files",
    "limits",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}
FORMAL_STATIC_MANIFEST_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "authority",
    "scientific_licensing_enabled",
    "matrix_id",
    "freeze_sha256",
    "main_freeze_sha256",
    "run_config_sha256",
    "cell",
    "semantic_invocation_sha256",
    "scheduler_classification",
    "evaluator_status",
    "record",
    "files",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}
STATIC_PROOF_SENTINEL_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "authority",
    "scientific_licensing_enabled",
    "matrix_id",
    "freeze_sha256",
    "main_freeze_sha256",
    "run_config_sha256",
    "cell",
    "scheduler_classification",
    "evaluator_status",
    "reason_code",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}
FORMAL_STATIC_TASK_KEYS = {
    "epsilon_lower",
    "epsilon_upper",
    "plan_record_sha256",
}
FORMAL_STATIC_INVOCATION_KEYS = {
    "argv",
    "argv_sha256",
    "exact_string_count",
    "output_token",
}
FORMAL_STATIC_SCHEDULER_RESULT_KEYS = {
    "classification",
    "evaluator_status",
    "return_code",
    "proof_kind",
    "reason_code",
}
FORMAL_STATIC_EVALUATOR_RESULT_KEYS = {
    "status",
    "return_code",
    "status_line_count",
}
FORMAL_STATIC_FILE_BINDING_KEYS = {
    "path",
    "sha256",
    "size_bytes",
    "serializer",
    "truncated",
}
FORMAL_STATIC_LIMIT_KEYS = {
    "max_depth_per_tree",
    "max_nodes_per_tree",
    "max_nodes_per_cell",
    "timeout_ms",
    "total_cell_bytes",
}
FORMAL_STATIC_FILE_NAMES = {
    "proof.json",
    "stdout.txt",
    "stderr.txt",
    "record.json",
}
FORMAL_STATIC_PROOF_KINDS = {
    "EVALUATOR_PROOF",
    "INVALID_EVALUATOR_PROOF",
    "SCHEDULER_NO_PROOF_SENTINEL",
}
FORMAL_STATIC_STATUS_CODES = {
    "STATIC_CELL_CERTIFIED": 0,
    "STATIC_UNRESOLVED_DEPTH": 2,
    "STATIC_UNRESOLVED_NODE_BUDGET": 2,
    "STATIC_INTERVAL_FAIL": 3,
    "INVALID_STATIC_PROOF_CONTRACT": 5,
}
FORMAL_STATIC_CLASSIFICATIONS = {
    "COMMITTED_EVALUATOR_RESULT",
    "CELL_TIMEOUT",
    "CELL_SIGNAL",
    "CELL_OUTPUT_BUDGET_EXHAUSTED",
    "MALFORMED_EVALUATOR_OUTPUT",
    "PROVENANCE_INVALID",
}
FORMAL_STATIC_SENTINEL_REASONS = {
    "CELL_TIMEOUT": "TIMEOUT",
    "CELL_SIGNAL": "SIGNAL",
    "CELL_OUTPUT_BUDGET_EXHAUSTED": "OUTPUT_BUDGET",
    "PROVENANCE_INVALID": "PROVENANCE",
    "MALFORMED_EVALUATOR_OUTPUT": "NO_EVALUATOR_PROOF",
}
FORMAL_STATIC_NONPASS_PROOF_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "authority",
    "scientific_licensing_enabled",
    "matrix_id",
    "freeze_sha256",
    "run_config_sha256",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
    "evaluator_status",
    "slab_id",
    "precision_bits",
    "epsilon",
    "period_window",
    "input_echo",
    "claim_boundary",
    "proof_complete",
    "failure",
    "trees",
    "counts",
    "proof_content_hash_definition",
    "proof_content_sha256",
}


def _require_formal_static_null_authority(
    payload: Mapping[str, Any], context: str
) -> None:
    require(payload["authority"] == "PRODUCER_ONLY", f"{context}: authority")
    exact_bool(
        payload["scientific_licensing_enabled"],
        f"{context}.scientific_licensing_enabled",
        False,
    )
    require(payload["claim_boundary"] == CELL_CLAIM_BOUNDARY, f"{context}: claim boundary")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[key] is None, f"{context}: unauthorized {key}")


def _canonical_object_from_image(raw: bytes, path: Path) -> dict[str, Any]:
    payload = load_strict_json_object_from_bytes(raw, path)
    require(raw == canonical_json_bytes(payload), f"{path.name}: JSON is not CJ_COMPACT_V1")
    return payload


def _validate_formal_static_binding(
    payload: Any,
    raw: bytes,
    *,
    expected_path: str,
    expected_serializer: str,
    context: str,
    expected_truncated: bool | None = None,
) -> dict[str, Any]:
    require(type(payload) is dict, f"{context}: not an object")
    exact_keys(payload, FORMAL_STATIC_FILE_BINDING_KEYS, context)
    require(payload["path"] == expected_path, f"{context}: path")
    require(
        exact_sha256(payload["sha256"], f"{context}.sha256") == sha256_bytes(raw),
        f"{context}: byte hash mismatch",
    )
    require_exact_int(payload["size_bytes"], f"{context}.size_bytes", expected=len(raw))
    require(payload["serializer"] == expected_serializer, f"{context}: serializer")
    require(type(payload["truncated"]) is bool, f"{context}.truncated: exact Boolean required")
    if expected_truncated is not None:
        require(
            payload["truncated"] is expected_truncated,
            f"{context}.truncated: expected {expected_truncated}",
        )
    return dict(payload)


def _validate_static_proof_identity(
    payload: Mapping[str, Any],
    *,
    expected_bits: int,
    expected_slab: str,
    plan: dict[str, dict[str, Any]],
    context: FormalStaticContext,
    expected_status: str,
    proof_context: str,
) -> None:
    require_exact_int(payload["schema_version"], f"{proof_context}.schema_version", expected=1)
    require(payload["protocol_id"] == PROTOCOL_ID, f"{proof_context}: protocol")
    require(payload["artifact_role"] == CELL_ROLE, f"{proof_context}: role")
    _require_formal_static_null_authority(payload, proof_context)
    require(payload["matrix_id"] == context.matrix_id, f"{proof_context}: matrix")
    require(payload["freeze_sha256"] == context.freeze_sha256, f"{proof_context}: freeze")
    require(payload["run_config_sha256"] == context.run_config_sha256, f"{proof_context}: run config")
    require(payload["evaluator_status"] == expected_status, f"{proof_context}: evaluator status")
    require(payload["slab_id"] == expected_slab, f"{proof_context}: slab")
    require_exact_int(payload["precision_bits"], f"{proof_context}.precision_bits", expected=expected_bits)
    record = plan[expected_slab]
    require(
        parse_interval_record(payload["epsilon"], f"{proof_context}.epsilon")
        == plan_epsilon(plan, expected_slab),
        f"{proof_context}: epsilon",
    )
    require(
        parse_interval_record(payload["period_window"], f"{proof_context}.period_window")
        == (Fraction(64, 100), PERIOD_MAX),
        f"{proof_context}: period window",
    )
    require_json_exact(
        payload["input_echo"],
        {
            "slab_id": expected_slab,
            "precision_bits": expected_bits,
            "epsilon_lower": record["epsilon_lower"],
            "epsilon_upper": record["epsilon_upper"],
            "matrix_id": context.matrix_id,
            "freeze_sha256": context.freeze_sha256,
            "run_config_sha256": context.run_config_sha256,
            "plan_record_sha256": plan_record_sha256(record),
            "max_depth": context.max_depth,
            "max_nodes_per_tree": context.max_nodes_per_tree,
            "max_nodes_per_cell": context.max_nodes_per_cell,
        },
        f"{proof_context}.input_echo",
    )


def _validate_formal_nonpass_proof(
    payload: dict[str, Any],
    *,
    expected_bits: int,
    expected_slab: str,
    plan: dict[str, dict[str, Any]],
    context: FormalStaticContext,
    expected_status: str,
) -> None:
    proof_context = f"formal proof {expected_bits}:{expected_slab}"
    exact_keys(payload, FORMAL_STATIC_NONPASS_PROOF_KEYS, proof_context)
    _validate_static_proof_identity(
        payload,
        expected_bits=expected_bits,
        expected_slab=expected_slab,
        plan=plan,
        context=context,
        expected_status=expected_status,
        proof_context=proof_context,
    )
    require(payload["proof_complete"] is False, f"{proof_context}: nonpass completeness")
    require_json_exact(payload["trees"], [], f"{proof_context}.trees")
    require_json_exact(
        payload["counts"],
        {
            "tree_count": 0,
            "node_count": 0,
            "internal_count": 0,
            "terminal_count": 0,
            "unresolved_count": 1,
            "maximum_depth": None,
        },
        f"{proof_context}.counts",
    )
    failure = payload["failure"]
    require(type(failure) is dict, f"{proof_context}.failure: not an exact object")
    if expected_status == "STATIC_UNRESOLVED_NODE_BUDGET":
        exact_keys(
            failure,
            {"scope", "tree_id", "limit", "consumed_before_node"},
            f"{proof_context}.failure",
        )
        require(
            type(failure["scope"]) is str and failure["scope"] in {"tree", "cell"},
            f"{proof_context}: failure scope",
        )
        require(type(failure["tree_id"]) is str, f"{proof_context}: failure tree")
        require_exact_int(failure["limit"], f"{proof_context}.failure.limit", minimum=1)
        require_exact_int(
            failure["consumed_before_node"],
            f"{proof_context}.failure.consumed_before_node",
            minimum=0,
        )
    elif expected_status == "STATIC_UNRESOLVED_DEPTH":
        require(
            set(failure) in (
                {"tree_id", "limit", "unresolved_depth"},
                {"tree_id", "limit", "unresolved_depth", "node_id"},
            ),
            f"{proof_context}.failure: depth schema",
        )
        require(type(failure["tree_id"]) is str, f"{proof_context}: failure tree")
        if "node_id" in failure:
            require(type(failure["node_id"]) is str, f"{proof_context}: failure node")
        require_exact_int(failure["limit"], f"{proof_context}.failure.limit", minimum=1)
        require_exact_int(
            failure["unresolved_depth"],
            f"{proof_context}.failure.unresolved_depth",
            minimum=0,
        )
    elif expected_status == "INVALID_STATIC_PROOF_CONTRACT":
        exact_keys(failure, {"reason"}, f"{proof_context}.failure")
        require(type(failure["reason"]) is str, f"{proof_context}: failure reason")
    elif expected_status == "STATIC_INTERVAL_FAIL":
        exact_keys(failure, {"error_type", "reason"}, f"{proof_context}.failure")
        require(
            type(failure["error_type"]) is str and type(failure["reason"]) is str,
            f"{proof_context}: interval failure strings",
        )
    else:
        raise CheckError(f"{proof_context}: unsupported nonpass status")
    require(
        payload["proof_content_hash_definition"]
        == "sha256(canonical_json(proof_without_proof_content_sha256))",
        f"{proof_context}: content-hash definition",
    )
    without_hash = dict(payload)
    stored_hash = without_hash.pop("proof_content_sha256")
    require(
        exact_sha256(stored_hash, f"{proof_context}.proof_content_sha256")
        == sha256_bytes(canonical_json_bytes(without_hash)),
        f"{proof_context}: content hash",
    )


def _validate_static_absent_sentinel(
    payload: dict[str, Any],
    *,
    expected_bits: int,
    expected_slab: str,
    context: FormalStaticContext,
    classification: str,
    reason_code: str,
) -> None:
    sentinel_context = f"STATIC_PROOF_ABSENT {expected_bits}:{expected_slab}"
    exact_keys(payload, STATIC_PROOF_SENTINEL_KEYS, sentinel_context)
    require_exact_int(payload["schema_version"], f"{sentinel_context}.schema_version", expected=1)
    require(payload["protocol_id"] == PROTOCOL_ID, f"{sentinel_context}: protocol")
    require(payload["artifact_role"] == "STATIC_PROOF_ABSENT", f"{sentinel_context}: role")
    _require_formal_static_null_authority(payload, sentinel_context)
    require(payload["matrix_id"] == context.matrix_id, f"{sentinel_context}: matrix")
    require(payload["freeze_sha256"] == context.freeze_sha256, f"{sentinel_context}: freeze")
    require(payload["main_freeze_sha256"] == context.freeze_sha256, f"{sentinel_context}: main freeze")
    require(payload["run_config_sha256"] == context.run_config_sha256, f"{sentinel_context}: run config")
    validate_cell_identity(payload["cell"], expected_bits, expected_slab, f"{sentinel_context}.cell")
    require(payload["scheduler_classification"] == classification, f"{sentinel_context}: classification")
    require(payload["evaluator_status"] is None, f"{sentinel_context}: evaluator status")
    require(payload["reason_code"] == reason_code, f"{sentinel_context}: reason")


def validate_formal_static_cell(
    cell_dir: Path,
    manifest_path: Path,
    *,
    expected_bits: int,
    expected_slab: str,
    plan: dict[str, dict[str, Any]],
    context: FormalStaticContext,
    expected_semantic_argv: list[str] | tuple[str, ...],
    expected_limits: Mapping[str, Any],
) -> dict[str, Any]:
    """Validate one formal four-file static transaction without promoting it.

    This leaf API deliberately returns only a structural/scientific
    eligibility Boolean.  It does not implement a formal aggregate or checker
    publication entry point, and it never dispatches an evaluator.
    """

    validate_formal_context(context)
    require(expected_bits in PRECISIONS, "formal static cell: unsupported precision")
    require(expected_slab in SLABS, "formal static cell: unsupported slab")
    cell_dir = require_canonical_absolute_path(cell_dir, "formal static cell directory")
    manifest_path = require_canonical_absolute_path(
        manifest_path, "formal static cell manifest"
    )
    require(
        cell_dir.name == expected_slab
        and cell_dir.parent.name == str(expected_bits)
        and cell_dir.parent.parent.name == "cells"
        and cell_dir.parent.parent.parent.name == "static",
        "formal static cell: canonical hierarchy mismatch",
    )
    require(
        manifest_path.name == f"{expected_slab}.json"
        and manifest_path.parent.name == str(expected_bits)
        and manifest_path.parent.parent.name == "cell_manifests"
        and manifest_path.parent.parent.parent == cell_dir.parent.parent.parent,
        "formal static manifest: canonical hierarchy mismatch",
    )
    require_exact_directory_names(
        cell_dir, FORMAL_STATIC_FILE_NAMES, f"formal static cell {expected_bits}:{expected_slab}"
    )
    paths = {name: cell_dir / name for name in sorted(FORMAL_STATIC_FILE_NAMES)}
    images = {name: read_pinned_regular_bytes(path) for name, path in paths.items()}
    record = _canonical_object_from_image(images["record.json"], paths["record.json"])
    manifest_raw = read_pinned_regular_bytes(manifest_path)
    manifest = _canonical_object_from_image(manifest_raw, manifest_path)

    record_context = f"formal static record {expected_bits}:{expected_slab}"
    exact_keys(record, FORMAL_STATIC_RECORD_KEYS, record_context)
    require_exact_int(record["schema_version"], f"{record_context}.schema_version", expected=1)
    require(record["protocol_id"] == PROTOCOL_ID, f"{record_context}: protocol")
    require(record["artifact_role"] == "STATIC_CELL_RECORD", f"{record_context}: role")
    _require_formal_static_null_authority(record, record_context)
    require(record["matrix_id"] == context.matrix_id, f"{record_context}: matrix")
    require(record["freeze_sha256"] == context.freeze_sha256, f"{record_context}: freeze")
    require(record["main_freeze_sha256"] == context.freeze_sha256, f"{record_context}: main freeze")
    require(record["run_config_sha256"] == context.run_config_sha256, f"{record_context}: run config")
    validate_cell_identity(record["cell"], expected_bits, expected_slab, f"{record_context}.cell")

    plan_record = plan[expected_slab]
    require(type(record["task"]) is dict, f"{record_context}.task: not an object")
    exact_keys(record["task"], FORMAL_STATIC_TASK_KEYS, f"{record_context}.task")
    require_json_exact(
        record["task"],
        {
            "epsilon_lower": plan_record["epsilon_lower"],
            "epsilon_upper": plan_record["epsilon_upper"],
            "plan_record_sha256": plan_record_sha256(plan_record),
        },
        f"{record_context}.task",
    )

    require(type(expected_semantic_argv) in (list, tuple), "expected semantic argv type")
    expected_argv = list(expected_semantic_argv)
    require(
        len(expected_argv) == 26 and all(type(item) is str for item in expected_argv),
        "expected semantic argv must be exactly 26 strings",
    )
    require(expected_argv[-1] == "<STAGING_PROOF_PATH>", "expected semantic output token")
    invocation = record["semantic_invocation"]
    require(type(invocation) is dict, f"{record_context}.semantic_invocation: not an object")
    exact_keys(invocation, FORMAL_STATIC_INVOCATION_KEYS, f"{record_context}.semantic_invocation")
    require_json_exact(invocation["argv"], expected_argv, f"{record_context}.semantic_invocation.argv")
    invocation_sha256 = sha256_bytes(canonical_json_bytes(expected_argv))
    require(
        exact_sha256(invocation["argv_sha256"], f"{record_context}.semantic_invocation.argv_sha256")
        == invocation_sha256,
        f"{record_context}: invocation hash",
    )
    require_exact_int(
        invocation["exact_string_count"],
        f"{record_context}.semantic_invocation.exact_string_count",
        expected=26,
    )
    require(
        invocation["output_token"] == "<STAGING_PROOF_PATH>",
        f"{record_context}: output token",
    )

    require(type(expected_limits) is dict, "expected formal static limits must be exact object")
    exact_keys(dict(expected_limits), FORMAL_STATIC_LIMIT_KEYS, "expected formal static limits")
    for key, value in expected_limits.items():
        require_exact_int(value, f"expected formal static limits.{key}", minimum=1)
    require_json_exact(record["limits"], dict(expected_limits), f"{record_context}.limits")
    require_exact_int(
        expected_limits["max_depth_per_tree"],
        "formal static limits.max_depth_per_tree",
        expected=context.max_depth,
    )
    require_exact_int(
        expected_limits["max_nodes_per_tree"],
        "formal static limits.max_nodes_per_tree",
        expected=context.max_nodes_per_tree,
    )
    require_exact_int(
        expected_limits["max_nodes_per_cell"],
        "formal static limits.max_nodes_per_cell",
        expected=context.max_nodes_per_cell,
    )

    scheduler_result = record["scheduler_result"]
    evaluator_result = record["evaluator_result"]
    require(type(scheduler_result) is dict, f"{record_context}.scheduler_result: not an object")
    require(type(evaluator_result) is dict, f"{record_context}.evaluator_result: not an object")
    exact_keys(
        scheduler_result,
        FORMAL_STATIC_SCHEDULER_RESULT_KEYS,
        f"{record_context}.scheduler_result",
    )
    exact_keys(
        evaluator_result,
        FORMAL_STATIC_EVALUATOR_RESULT_KEYS,
        f"{record_context}.evaluator_result",
    )
    classification = scheduler_result["classification"]
    evaluator_status = scheduler_result["evaluator_status"]
    return_code = scheduler_result["return_code"]
    proof_kind = scheduler_result["proof_kind"]
    reason_code = scheduler_result["reason_code"]
    require(
        type(classification) is str and classification in FORMAL_STATIC_CLASSIFICATIONS,
        f"{record_context}: classification",
    )
    require(
        type(proof_kind) is str and proof_kind in FORMAL_STATIC_PROOF_KINDS,
        f"{record_context}: proof kind",
    )
    require(return_code is None or type(return_code) is int, f"{record_context}: return-code type")
    require(type(evaluator_result["status_line_count"]) is int, f"{record_context}: status-line count type")

    file_bindings = record["files"]
    require(type(file_bindings) is dict, f"{record_context}.files: not an object")
    exact_keys(file_bindings, {"proof.json", "stdout.txt", "stderr.txt"}, f"{record_context}.files")
    proof_serializer = "CJ_COMPACT_V1" if proof_kind != "INVALID_EVALUATOR_PROOF" else "RAW_BYTES"
    validated_bindings = {
        "proof.json": _validate_formal_static_binding(
            file_bindings["proof.json"],
            images["proof.json"],
            expected_path="proof.json",
            expected_serializer=proof_serializer,
            context=f"{record_context}.files.proof.json",
        ),
        "stdout.txt": _validate_formal_static_binding(
            file_bindings["stdout.txt"],
            images["stdout.txt"],
            expected_path="stdout.txt",
            expected_serializer="RAW_BYTES",
            context=f"{record_context}.files.stdout.txt",
        ),
        "stderr.txt": _validate_formal_static_binding(
            file_bindings["stderr.txt"],
            images["stderr.txt"],
            expected_path="stderr.txt",
            expected_serializer="RAW_BYTES",
            context=f"{record_context}.files.stderr.txt",
        ),
    }
    require(
        sum(len(images[name]) for name in FORMAL_STATIC_FILE_NAMES)
        <= expected_limits["total_cell_bytes"],
        f"{record_context}: total byte cap exceeded",
    )

    manifest_context = f"formal static manifest {expected_bits}:{expected_slab}"
    exact_keys(manifest, FORMAL_STATIC_MANIFEST_KEYS, manifest_context)
    require_exact_int(manifest["schema_version"], f"{manifest_context}.schema_version", expected=1)
    require(manifest["protocol_id"] == PROTOCOL_ID, f"{manifest_context}: protocol")
    require(manifest["artifact_role"] == "STATIC_CELL_MANIFEST", f"{manifest_context}: role")
    _require_formal_static_null_authority(manifest, manifest_context)
    require(manifest["matrix_id"] == context.matrix_id, f"{manifest_context}: matrix")
    require(manifest["freeze_sha256"] == context.freeze_sha256, f"{manifest_context}: freeze")
    require(manifest["main_freeze_sha256"] == context.freeze_sha256, f"{manifest_context}: main freeze")
    require(manifest["run_config_sha256"] == context.run_config_sha256, f"{manifest_context}: run config")
    validate_cell_identity(manifest["cell"], expected_bits, expected_slab, f"{manifest_context}.cell")
    require(manifest["semantic_invocation_sha256"] == invocation_sha256, f"{manifest_context}: invocation")
    require(manifest["scheduler_classification"] == classification, f"{manifest_context}: classification")
    require_json_exact(manifest["evaluator_status"], evaluator_status, f"{manifest_context}.evaluator_status")
    manifest_files = manifest["files"]
    require(type(manifest_files) is dict, f"{manifest_context}.files: not an object")
    exact_keys(manifest_files, FORMAL_STATIC_FILE_NAMES, f"{manifest_context}.files")
    for name in ("proof.json", "stdout.txt", "stderr.txt"):
        require_json_exact(
            manifest_files[name], validated_bindings[name], f"{manifest_context}.files.{name}"
        )
    record_binding = _validate_formal_static_binding(
        manifest_files["record.json"],
        images["record.json"],
        expected_path="record.json",
        expected_serializer="CJ_COMPACT_V1",
        expected_truncated=False,
        context=f"{manifest_context}.files.record.json",
    )
    require_json_exact(manifest["record"], record_binding, f"{manifest_context}.record")

    component_eligible = False
    proof_replay: dict[str, Any] | None = None
    if classification == "COMMITTED_EVALUATOR_RESULT":
        require(proof_kind == "EVALUATOR_PROOF", f"{record_context}: committed proof kind")
        require(evaluator_status in FORMAL_STATIC_STATUS_CODES, f"{record_context}: evaluator status")
        expected_code = FORMAL_STATIC_STATUS_CODES[evaluator_status]
        require_exact_int(return_code, f"{record_context}.return_code", expected=expected_code)
        require(reason_code is None, f"{record_context}: committed reason must be null")
        require_json_exact(
            evaluator_result,
            {"status": evaluator_status, "return_code": expected_code, "status_line_count": 1},
            f"{record_context}.evaluator_result",
        )
        require(
            images["stdout.txt"] == f"evaluator_status={evaluator_status}\n".encode("ascii"),
            f"{record_context}: exact evaluator stdout",
        )
        require(images["stderr.txt"] == b"", f"{record_context}: committed stderr is nonempty")
        require(
            all(not binding["truncated"] for binding in validated_bindings.values()),
            f"{record_context}: committed file is truncated",
        )
        proof_payload = _canonical_object_from_image(images["proof.json"], paths["proof.json"])
        if evaluator_status == CELL_PASS_STATUS:
            proof_replay = verify_proof(
                paths["proof.json"],
                expected_bits=expected_bits,
                expected_slab=expected_slab,
                plan=plan,
                context=context,
            )
            require(
                proof_replay["sha256"] == sha256_bytes(images["proof.json"]),
                f"{record_context}: proof changed before scientific replay",
            )
            component_eligible = True
        else:
            _validate_formal_nonpass_proof(
                proof_payload,
                expected_bits=expected_bits,
                expected_slab=expected_slab,
                plan=plan,
                context=context,
                expected_status=evaluator_status,
            )
    else:
        require(evaluator_status is None, f"{record_context}: noncommitted evaluator status")
        require_json_exact(
            evaluator_result,
            {"status": None, "return_code": None, "status_line_count": 0},
            f"{record_context}.evaluator_result",
        )
        if proof_kind == "SCHEDULER_NO_PROOF_SENTINEL":
            expected_reason = FORMAL_STATIC_SENTINEL_REASONS.get(classification)
            require(expected_reason is not None, f"{record_context}: sentinel classification")
            require(reason_code == expected_reason, f"{record_context}: sentinel reason")
            require(return_code is None, f"{record_context}: sentinel return code")
            require(
                validated_bindings["proof.json"]["truncated"] is False,
                f"{record_context}: sentinel cannot be truncated",
            )
            sentinel = _canonical_object_from_image(images["proof.json"], paths["proof.json"])
            _validate_static_absent_sentinel(
                sentinel,
                expected_bits=expected_bits,
                expected_slab=expected_slab,
                context=context,
                classification=classification,
                reason_code=reason_code,
            )
            if classification == "CELL_OUTPUT_BUDGET_EXHAUSTED":
                require(
                    any(binding["truncated"] for binding in validated_bindings.values()),
                    f"{record_context}: budget exhaustion without truncation",
                )
        elif proof_kind == "INVALID_EVALUATOR_PROOF":
            require(
                classification
                in {"MALFORMED_EVALUATOR_OUTPUT", "CELL_OUTPUT_BUDGET_EXHAUSTED"},
                f"{record_context}: invalid proof classification",
            )
            expected_reason = (
                "MALFORMED_OR_NONCANONICAL_PROOF"
                if classification == "MALFORMED_EVALUATOR_OUTPUT"
                else "OUTPUT_BUDGET"
            )
            require(reason_code == expected_reason, f"{record_context}: invalid proof reason")
            require(len(images["proof.json"]) > 0, f"{record_context}: absent proof requires sentinel")
            if classification == "CELL_OUTPUT_BUDGET_EXHAUSTED":
                require(
                    any(binding["truncated"] for binding in validated_bindings.values()),
                    f"{record_context}: budget exhaustion without truncation",
                )
        else:
            require(
                classification == "MALFORMED_EVALUATOR_OUTPUT"
                and reason_code == "STATUS_OR_RETURN_CODE_MISMATCH",
                f"{record_context}: canonical noncommitted proof reason",
            )
            proof_payload = _canonical_object_from_image(
                images["proof.json"], paths["proof.json"]
            )
            proof_status = proof_payload.get("evaluator_status")
            require(
                type(proof_status) is str
                and proof_status in FORMAL_STATIC_STATUS_CODES,
                f"{record_context}: canonical proof has no closed evaluator status",
            )
            if proof_status == CELL_PASS_STATUS:
                rejected_replay = verify_proof(
                    paths["proof.json"],
                    expected_bits=expected_bits,
                    expected_slab=expected_slab,
                    plan=plan,
                    context=context,
                )
                require(
                    rejected_replay["sha256"] == sha256_bytes(images["proof.json"]),
                    f"{record_context}: malformed-status proof changed during replay",
                )
            else:
                _validate_formal_nonpass_proof(
                    proof_payload,
                    expected_bits=expected_bits,
                    expected_slab=expected_slab,
                    plan=plan,
                    context=context,
                    expected_status=proof_status,
                )

    require(
        manifest["evaluator_status"] == (evaluator_status if classification == "COMMITTED_EVALUATOR_RESULT" else None),
        f"{manifest_context}: evaluator status authority",
    )
    # Detect cross-file replacement after all semantic checks.  The manifest
    # itself is immutable evidence but does not make mutable lexical paths safe.
    require_exact_directory_names(
        cell_dir, FORMAL_STATIC_FILE_NAMES, f"formal static cell {expected_bits}:{expected_slab} final scan"
    )
    for name, raw in images.items():
        require(
            read_pinned_regular_bytes(paths[name]) == raw,
            f"formal static cell {expected_bits}:{expected_slab}: {name} changed during replay",
        )
    require(
        read_pinned_regular_bytes(manifest_path) == manifest_raw,
        f"formal static manifest {expected_bits}:{expected_slab}: changed during replay",
    )
    return {
        "cell": {"precision_bits": expected_bits, "slab_id": expected_slab},
        "manifest_path": manifest_path.name,
        "manifest_sha256": sha256_bytes(manifest_raw),
        "manifest_size_bytes": len(manifest_raw),
        "scheduler_classification": classification,
        "evaluator_status": evaluator_status,
        "proof_kind": proof_kind,
        "component_eligible": component_eligible,
        "proof_replay": proof_replay,
    }


def require_mock_null_authority(payload: Mapping[str, Any], context: str) -> None:
    require(payload["artifact_status"] == MOCK_ARTIFACT_STATUS, f"{context}: artifact status")
    require(payload["authority"] == "PRODUCER_ONLY", f"{context}: authority")
    exact_bool(payload["mock_only"], f"{context}.mock_only", True)
    exact_bool(
        payload["scientific_licensing_enabled"],
        f"{context}.scientific_licensing_enabled",
        False,
    )
    require(payload["claim_boundary"] == MOCK_PRODUCER_CLAIM_BOUNDARY, f"{context}: claim boundary")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[key] is None, f"{context}: unauthorized {key}")


MOCK_PROOF_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "cell",
    "matrix_id",
    "run_config_sha256",
    "synthetic_trees",
    "evaluator_status",
    "scientific_licensing_enabled",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}
MOCK_RECORD_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "cell",
    "matrix_id",
    "main_freeze_sha256",
    "run_config_sha256",
    "scheduler_classification",
    "evaluator_status",
    "returncode",
    "evaluator_payload",
    "scientific_licensing_enabled",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}
MOCK_CELL_MANIFEST_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "cell",
    "matrix_id",
    "main_freeze_sha256",
    "run_config_sha256",
    "scheduler_classification",
    "evaluator_status",
    "files",
    "scientific_licensing_enabled",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def validate_file_binding(
    payload: Any,
    raw: bytes,
    context: str,
) -> None:
    require(isinstance(payload, dict), f"{context}: not an object")
    exact_keys(payload, {"sha256", "size_bytes"}, context)
    require(exact_sha256(payload["sha256"], f"{context}.sha256") == sha256_bytes(raw), f"{context}: hash mismatch")
    require_exact_int(payload["size_bytes"], f"{context}.size_bytes", expected=len(raw))


def validate_mock_static_cell(
    input_dir: Path,
    bits: int,
    slab_id: str,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    cell_dir = input_dir / "static" / "cells" / str(bits) / slab_id
    require_exact_directory_names(
        cell_dir, {"proof.json", "record.json"}, f"static cell {bits}:{slab_id}"
    )
    proof, proof_raw = load_canonical_json_with_raw(cell_dir / "proof.json")
    record, record_raw = load_canonical_json_with_raw(cell_dir / "record.json")
    exact_keys(proof, MOCK_PROOF_KEYS, f"proof {bits}:{slab_id}")
    require_exact_int(proof["schema_version"], f"proof {bits}:{slab_id}.schema_version", expected=1)
    require(proof["protocol_id"] == PROTOCOL_ID, f"proof {bits}:{slab_id}: protocol")
    require(proof["artifact_role"] == "MOCK_STATIC_PROOF", f"proof {bits}:{slab_id}: role")
    require_mock_null_authority(proof, f"proof {bits}:{slab_id}")
    validate_cell_identity(proof["cell"], bits, slab_id, f"proof {bits}:{slab_id}.cell")
    require(proof["matrix_id"] == matrix_id, f"proof {bits}:{slab_id}: matrix")
    require(proof["run_config_sha256"] == run_config_sha256, f"proof {bits}:{slab_id}: run config")
    require_json_exact(
        proof["synthetic_trees"],
        ["ANGLE", "SECTION_LOW", "SECTION_HIGH", "SECTION_WINDOW"],
        f"proof {bits}:{slab_id}.synthetic_trees",
    )
    require(proof["evaluator_status"] == CELL_PASS_STATUS, f"proof {bits}:{slab_id}: evaluator status")

    exact_keys(record, MOCK_RECORD_KEYS, f"record {bits}:{slab_id}")
    require_exact_int(record["schema_version"], f"record {bits}:{slab_id}.schema_version", expected=1)
    require(record["protocol_id"] == PROTOCOL_ID, f"record {bits}:{slab_id}: protocol")
    require(record["artifact_role"] == "MOCK_STATIC_CELL_RECORD", f"record {bits}:{slab_id}: role")
    require_mock_null_authority(record, f"record {bits}:{slab_id}")
    validate_cell_identity(record["cell"], bits, slab_id, f"record {bits}:{slab_id}.cell")
    require(record["matrix_id"] == matrix_id, f"record {bits}:{slab_id}: matrix")
    require(record["main_freeze_sha256"] is None, f"record {bits}:{slab_id}: main freeze")
    require(record["run_config_sha256"] == run_config_sha256, f"record {bits}:{slab_id}: run config")
    require(record["scheduler_classification"] == "COMMITTED_EVALUATOR_RESULT", f"record {bits}:{slab_id}: classification")
    require(record["evaluator_status"] == CELL_PASS_STATUS, f"record {bits}:{slab_id}: evaluator status")
    require_exact_int(record["returncode"], f"record {bits}:{slab_id}.returncode", expected=0)
    evaluator_payload = record["evaluator_payload"]
    require(isinstance(evaluator_payload, dict), f"record {bits}:{slab_id}.evaluator_payload")
    exact_keys(evaluator_payload, {"path", "sha256", "size_bytes"}, f"record {bits}:{slab_id}.evaluator_payload")
    require(evaluator_payload["path"] == "proof.json", f"record {bits}:{slab_id}: proof path")
    validate_file_binding(
        {"sha256": evaluator_payload["sha256"], "size_bytes": evaluator_payload["size_bytes"]},
        proof_raw,
        f"record {bits}:{slab_id}.evaluator_payload",
    )

    manifest_path = input_dir / "static" / "cell_manifests" / str(bits) / f"{slab_id}.json"
    manifest, manifest_raw = load_canonical_json_with_raw(manifest_path)
    exact_keys(manifest, MOCK_CELL_MANIFEST_KEYS, f"manifest {bits}:{slab_id}")
    require_exact_int(manifest["schema_version"], f"manifest {bits}:{slab_id}.schema_version", expected=1)
    require(manifest["protocol_id"] == PROTOCOL_ID, f"manifest {bits}:{slab_id}: protocol")
    require(manifest["artifact_role"] == "MOCK_STATIC_CELL_MANIFEST", f"manifest {bits}:{slab_id}: role")
    require_mock_null_authority(manifest, f"manifest {bits}:{slab_id}")
    validate_cell_identity(manifest["cell"], bits, slab_id, f"manifest {bits}:{slab_id}.cell")
    require(manifest["matrix_id"] == matrix_id, f"manifest {bits}:{slab_id}: matrix")
    require(manifest["main_freeze_sha256"] is None, f"manifest {bits}:{slab_id}: main freeze")
    require(manifest["run_config_sha256"] == run_config_sha256, f"manifest {bits}:{slab_id}: run config")
    require(manifest["scheduler_classification"] == "COMMITTED_EVALUATOR_RESULT", f"manifest {bits}:{slab_id}: classification")
    require(manifest["evaluator_status"] == CELL_PASS_STATUS, f"manifest {bits}:{slab_id}: evaluator status")
    files = manifest["files"]
    require(isinstance(files, dict), f"manifest {bits}:{slab_id}.files")
    exact_keys(files, {"proof.json", "record.json"}, f"manifest {bits}:{slab_id}.files")
    validate_file_binding(files["proof.json"], proof_raw, f"manifest {bits}:{slab_id}.files.proof")
    validate_file_binding(files["record.json"], record_raw, f"manifest {bits}:{slab_id}.files.record")
    return {
        "cell": {"precision_bits": bits, "slab_id": slab_id},
        "path": f"static/cell_manifests/{bits}/{slab_id}.json",
        "sha256": sha256_bytes(manifest_raw),
        "size_bytes": len(manifest_raw),
        "evaluator_status": proof["evaluator_status"],
    }


MOCK_AGGREGATE_SUMMARY_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "matrix_id",
    "main_freeze_sha256",
    "run_config_sha256",
    "matrix",
    "cell_count",
    "ordered_cell_manifest_root",
    "status_counts",
    "scheduler_classification_counts",
    "scientific_licensing_enabled",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}
MOCK_AGGREGATE_MANIFEST_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "matrix_id",
    "main_freeze_sha256",
    "run_config_sha256",
    "ordered_cell_manifest_root",
    "cell_manifests",
    "summary",
    "scientific_licensing_enabled",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def validate_static_namespace(input_dir: Path, *, allow_checker: bool) -> None:
    root_names = directory_names(input_dir, "mock authoritative root")
    required = {"run_config.json", "static"}
    permitted = required | {"branch"}
    if allow_checker:
        required.add("independent_static_checker.json")
        permitted.add("independent_static_checker.json")
    require(required <= root_names, "mock authoritative root: required static objects missing")
    require(root_names <= permitted, f"mock authoritative root: extra paths {sorted(root_names-permitted)}")
    if "branch" in root_names:
        directory_names(input_dir / "branch", "mock branch sibling")
    static_root = input_dir / "static"
    require_exact_directory_names(
        static_root,
        {"cells", "cell_manifests", "aggregate_summary.json", "aggregate_manifest.json"},
        "mock static root",
    )
    for namespace, suffix in (("cells", ""), ("cell_manifests", ".json")):
        component_root = static_root / namespace
        require_exact_directory_names(
            component_root, {str(bits) for bits in PRECISIONS}, f"mock static {namespace}"
        )
        for bits in PRECISIONS:
            expected = {slab_id + suffix for slab_id in SLABS}
            require_exact_directory_names(
                component_root / str(bits), expected, f"mock static {namespace} {bits}"
            )


def validate_mock_static_aggregate(
    input_dir: Path,
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
) -> tuple[dict[str, Any], bytes, dict[str, Any], bytes]:
    summary, summary_raw = load_canonical_json_with_raw(
        input_dir / "static" / "aggregate_summary.json"
    )
    manifest, manifest_raw = load_canonical_json_with_raw(
        input_dir / "static" / "aggregate_manifest.json"
    )
    exact_keys(summary, MOCK_AGGREGATE_SUMMARY_KEYS, "mock static aggregate summary")
    require_exact_int(summary["schema_version"], "mock static aggregate summary.schema_version", expected=1)
    require(summary["protocol_id"] == PROTOCOL_ID, "mock static aggregate summary: protocol")
    require(summary["artifact_role"] == "MOCK_STATIC_AGGREGATE_SUMMARY", "mock static aggregate summary: role")
    require_mock_null_authority(summary, "mock static aggregate summary")
    require(summary["matrix_id"] == matrix_id, "mock static aggregate summary: matrix")
    require(summary["main_freeze_sha256"] is None, "mock static aggregate summary: main freeze")
    require(summary["run_config_sha256"] == run_config_sha256, "mock static aggregate summary: run config")
    require_json_exact(summary["matrix"], mock_matrix_payload(), "mock static aggregate summary.matrix")
    require_exact_int(summary["cell_count"], "mock static aggregate summary.cell_count", expected=102)
    root = sha256_bytes(canonical_json_bytes([
        {key: entry[key] for key in ("cell", "path", "sha256", "size_bytes")}
        for entry in entries
    ]))
    require(summary["ordered_cell_manifest_root"] == root, "mock static aggregate summary: ordered root")
    require_json_exact(summary["status_counts"], {CELL_PASS_STATUS: 102}, "mock static aggregate summary.status_counts")
    require_json_exact(
        summary["scheduler_classification_counts"],
        {"COMMITTED_EVALUATOR_RESULT": 102},
        "mock static aggregate summary.scheduler_classification_counts",
    )

    exact_keys(manifest, MOCK_AGGREGATE_MANIFEST_KEYS, "mock static aggregate manifest")
    require_exact_int(manifest["schema_version"], "mock static aggregate manifest.schema_version", expected=1)
    require(manifest["protocol_id"] == PROTOCOL_ID, "mock static aggregate manifest: protocol")
    require(manifest["artifact_role"] == "MOCK_STATIC_AGGREGATE_MANIFEST", "mock static aggregate manifest: role")
    require_mock_null_authority(manifest, "mock static aggregate manifest")
    require(manifest["matrix_id"] == matrix_id, "mock static aggregate manifest: matrix")
    require(manifest["main_freeze_sha256"] is None, "mock static aggregate manifest: main freeze")
    require(manifest["run_config_sha256"] == run_config_sha256, "mock static aggregate manifest: run config")
    require(manifest["ordered_cell_manifest_root"] == root, "mock static aggregate manifest: ordered root")
    expected_entries = [
        {key: entry[key] for key in ("cell", "path", "sha256", "size_bytes")}
        for entry in entries
    ]
    require_json_exact(manifest["cell_manifests"], expected_entries, "mock static aggregate manifest.cell_manifests")
    require(isinstance(manifest["summary"], dict), "mock static aggregate manifest.summary")
    exact_keys(manifest["summary"], {"path", "sha256", "size_bytes"}, "mock static aggregate manifest.summary")
    require(manifest["summary"]["path"] == "static/aggregate_summary.json", "mock static aggregate manifest: summary path")
    validate_file_binding(
        {"sha256": manifest["summary"]["sha256"], "size_bytes": manifest["summary"]["size_bytes"]},
        summary_raw,
        "mock static aggregate manifest.summary",
    )
    return summary, summary_raw, manifest, manifest_raw


def replay_mock_static_archive(input_dir: Path, *, allow_checker: bool) -> dict[str, Any]:
    input_dir = require_canonical_absolute_path(input_dir, "static checker input directory")
    validate_static_namespace(input_dir, allow_checker=allow_checker)
    run_config, run_config_raw, run_config_sha256, producer_bindings = validate_mock_run_config(input_dir)
    entries: list[dict[str, Any]] = []
    status_pairs: dict[str, dict[int, str]] = {slab_id: {} for slab_id in SLABS}
    for bits in PRECISIONS:
        for slab_id in SLABS:
            entry = validate_mock_static_cell(
                input_dir, bits, slab_id, run_config["matrix_id"], run_config_sha256
            )
            entries.append(entry)
            status_pairs[slab_id][bits] = entry["evaluator_status"]
    summary, summary_raw, manifest, manifest_raw = validate_mock_static_aggregate(
        input_dir, run_config["matrix_id"], run_config_sha256, entries
    )
    agreement = sum(
        1
        for slab_id in SLABS
        if status_pairs[slab_id] == {128: CELL_PASS_STATUS, 256: CELL_PASS_STATUS}
    )
    require(agreement == 51, "mock static cross-precision status disagreement")
    return {
        "run_config_sha256": run_config_sha256,
        "matrix_id": run_config["matrix_id"],
        "aggregate_summary_sha256": sha256_bytes(summary_raw),
        "aggregate_manifest_sha256": sha256_bytes(manifest_raw),
        "ordered_cell_manifest_root": manifest["ordered_cell_manifest_root"],
        "producer_source_bindings": producer_bindings,
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
            "status_pairs_agree": agreement,
        },
        "summary": summary,
    }


def build_mock_checker_result(replay: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": CHECKER_ROLE,
        "authority": "INDEPENDENT_CHECKER",
        "checker_status": MOCK_CHECKER_STATUS,
        "component_status": None,
        "scientific_licensing_enabled": False,
        "passed": True,
        "matrix_id": replay["matrix_id"],
        "main_freeze_sha256": None,
        "run_config_sha256": replay["run_config_sha256"],
        "component_aggregate_summary_sha256": replay["aggregate_summary_sha256"],
        "component_aggregate_manifest_sha256": replay["aggregate_manifest_sha256"],
        "replay_counts": replay["replay_counts"],
        "cross_precision": replay["cross_precision"],
        "diagnostics": {
            "artifact_status": MOCK_ARTIFACT_STATUS,
            "mock_only": True,
            "ordered_cell_manifest_root": replay["ordered_cell_manifest_root"],
            "production_dispatch_observed": False,
            "scientific_proof_replay_performed": False,
        },
        "failures": [],
        "source_bindings": {
            "checker_sha256": sha256_file(CHECKER),
            "producer_source_bindings": replay["producer_source_bindings"],
        },
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def run_checker(input_dir: Path) -> dict[str, Any]:
    """Independently close the full mock static archive, without authority.

    A future production run config is intentionally rejected here.  Formal
    proof replay remains available through :func:`verify_proof`, but a
    scientific 102-cell aggregate cannot be promoted before a main freeze.
    """

    replay = replay_mock_static_archive(input_dir, allow_checker=False)
    return build_mock_checker_result(replay)


def run_postcheck(input_dir: Path) -> dict[str, Any]:
    input_dir = require_canonical_absolute_path(input_dir, "static postcheck input directory")
    checker_path = input_dir / "independent_static_checker.json"
    replay = replay_mock_static_archive(input_dir, allow_checker=True)
    expected_checker = build_mock_checker_result(replay)
    checker_payload, checker_raw = load_canonical_json_with_raw(checker_path)
    require_json_exact(checker_payload, expected_checker, "published mock static checker")
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "STATIC_POSTCHECK",
        "authority": "POSTCHECK_ONLY",
        "postcheck_status": MOCK_POSTCHECK_STATUS,
        "passed": True,
        "checker_path": "independent_static_checker.json",
        "checker_sha256": sha256_bytes(checker_raw),
        "main_freeze_sha256": None,
        "run_config_sha256": replay["run_config_sha256"],
        "bound_artifacts": {
            "aggregate_manifest": {
                "path": "static/aggregate_manifest.json",
                "sha256": replay["aggregate_manifest_sha256"],
            },
            "aggregate_summary": {
                "path": "static/aggregate_summary.json",
                "sha256": replay["aggregate_summary_sha256"],
            },
            "checker_source": {
                "path": project_relative_path(CHECKER),
                "sha256": sha256_file(CHECKER),
            },
        },
        "replay_counts": replay["replay_counts"],
        "failures": [],
        "claim_boundary": MOCK_POSTCHECK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


# ---------------------------------------------------------------------------
# V2 formal authority path.  Everything below is independently literal: no
# scheduler, evaluator, release builder, or sibling checker is imported or
# executed.  The attempt-1 mock entry points above are intentionally not
# reachable from the V2 command line defined at the end of this file.

ROLE5_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "production_authorized", "legacy_attempt",
    "reviewed_v2_inputs", "review", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
ROLE5_REVIEWED_ROLES = (
    "prefreeze_design", "formal_protocol", "scheduler_contract",
    "checker_contract", "release_contract", "scheduler",
    "static_checker_source", "branch_checker_source",
    "composite_checker_source", "s0_adapter", "release_builder",
    "test_static_scheduler", "test_static_checker", "test_branch_scheduler",
    "test_branch_checker", "test_s0_compatibility", "test_composite",
    "test_adversarial", "test_release",
)
ROLE5_LEGACY_ARTIFACTS = (
    {"role": 10, "path": "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json", "sha256": "0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e", "publication_commit": "5086e33c7c66f33785338e90b340347e086d9941"},
    {"role": 11, "path": "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json", "sha256": "08ffeb5e7f5d681567bd7a81335585d1b8697040a28d91584b09fdc4304a379a", "publication_commit": "201758031a7784a68ab66d37094c25135de52646"},
    {"role": 12, "path": "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md", "sha256": "af38e899f9dad9abacadbdaa27f12833d5ea423a9896ee089fb8a4d90b55477c", "publication_commit": "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0"},
    {"role": 13, "path": "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json", "sha256": "d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30", "publication_commit": "be2a732625d9cab97879539873a756e1eabd366d"},
)
ROLE5_LEGACY_DEFECTS = (
    {
        "severity": "P1",
        "code": "ROLE24_MOCK_ONLY_NO_FORMAL_54_OR_68_VALIDATION",
        "finding": "legacy role 24 implements mock release and machine verification only; it does not implement formal role-54 validation or publication or formal 68-role release validation or publication",
    },
    {
        "severity": "P1",
        "code": "ROLES20_22_NO_FORMAL_THREE_CHECKER_THREE_POSTCHECK_CHAIN",
        "finding": "legacy roles 20 through 22 do not implement the required formal static, branch, and composite checker plus postcheck publication chain",
    },
)
ROLE5_SUPERSESSION_RULE = (
    "legacy attempt-1 bytes remain immutable audit evidence, are not V2 inputs, "
    "and confer no freeze, initialization, scientific licensing, promotion, or dispatch authority"
)
ROLE5_CLAIM_BOUNDARY = (
    "independent withdrawal of control attempt 1 and acceptance of the reviewed "
    "V2 control implementation only; no machine, main freeze, result, theorem, "
    "release, initialization, promotion, or dispatch acceptance"
)


def _safe_relative(value: Any, context: str = "relative path") -> PurePosixPath:
    require(type(value) is str and value != "", f"{context}: nonempty string required")
    require("\x00" not in value and "\\" not in value, f"{context}: unsafe spelling")
    relative = PurePosixPath(value)
    require(
        not relative.is_absolute()
        and relative.as_posix() == value
        and all(part not in ("", ".", "..") and not part.startswith(".") for part in relative.parts),
        f"{context}: canonical visible relative path required",
    )
    return relative


def _project_file(project_root: Path, relative: str) -> Path:
    root = require_canonical_absolute_path(project_root, "V2 project root")
    return root.joinpath(*_safe_relative(relative).parts)


def _formal_matrix() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": slab}
        for bits in PRECISIONS
        for slab in SLABS
    ]


def _formal_matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(_formal_matrix()))


def _formal_serializers() -> dict[str, Any]:
    return {
        "compact_json": {"id": "CJ_COMPACT_V1", "sort_keys": True, "ensure_ascii": False, "allow_nan": False, "indent": None, "separators": [",", ":"], "trailing_lf": True},
        "branch_pretty_json": {"id": "CJ_PRETTY_2_V1", "sort_keys": True, "ensure_ascii": False, "allow_nan": False, "indent": 2, "separators": None, "trailing_lf": True},
        "artifact_bindings": {
            "main_freeze": "CJ_COMPACT_V1", "run_config": "CJ_COMPACT_V1",
            "static_proof": "CJ_COMPACT_V1", "static_record": "CJ_COMPACT_V1",
            "static_manifest": "CJ_COMPACT_V1", "branch_task_hash": "CJ_PRETTY_2_V1",
            "branch_argv_hash": "CJ_PRETTY_2_V1", "branch_record": "CJ_PRETTY_2_V1",
            "branch_manifest": "CJ_PRETTY_2_V1", "aggregates": "CJ_COMPACT_V1",
        },
    }


def _formal_scheduler_policy() -> dict[str, Any]:
    return {
        "policy": "deterministic_component_barrier_batches_v1",
        "component_order": ["STATIC", "BRANCH"], "static_workers": 8,
        "branch_workers": 6, "static_barrier_size": 8, "branch_barrier_size": 6,
        "max_inflight_per_cell": 1, "global_scientific_budget": None,
    }


def _formal_limits() -> dict[str, Any]:
    return {
        "static": {
            "max_depth_per_tree": 24, "max_nodes_per_tree": 250000,
            "max_nodes_per_cell": 1000000, "timeout_ms": 1800000,
            "total_cell_bytes": 512 * 1024 * 1024,
        },
        "branch": {
            "timeout_ms": 600000, "term_grace_ms": 2000,
            "pipe_close_grace_ms": 1000, "stdout_bytes": 16 * 1024 * 1024,
            "stderr_bytes": 1024 * 1024, "record_bytes": 4 * 1024 * 1024,
            "total_cell_bytes": 32 * 1024 * 1024, "phase_cells": 64,
            "taylor_order": 24, "tolerance_128": "1e-30", "tolerance_256": "1e-60",
        },
        "admission": {
            "memory_pause_bytes": 48 * 1024**3, "launch_free_bytes": 200 * 1024**3,
            "warning_free_bytes": 180 * 1024**3, "pause_free_bytes": 150 * 1024**3,
            "recovery_only_free_bytes": 120 * 1024**3,
        },
    }


def _formal_status_tables() -> dict[str, Any]:
    return {
        "static_evaluator": [
            {"status": "STATIC_CELL_CERTIFIED", "return_code": 0, "promotion": "ELIGIBLE"},
            {"status": "STATIC_UNRESOLVED_DEPTH", "return_code": 2, "promotion": "BLOCKED"},
            {"status": "STATIC_UNRESOLVED_NODE_BUDGET", "return_code": 2, "promotion": "BLOCKED"},
            {"status": "STATIC_INTERVAL_FAIL", "return_code": 3, "promotion": "BLOCKED"},
            {"status": "INVALID_STATIC_PROOF_CONTRACT", "return_code": 5, "promotion": "BLOCKED"},
        ],
        "branch_evaluator": [
            {"status": "BRANCH_CELL_CERTIFIED", "return_code": 0, "promotion": "ELIGIBLE"},
            {"status": "BRANCH_TUBE_UNRESOLVED", "return_code": 2, "promotion": "BLOCKED"},
            {"status": "BRANCH_FLOW_FAIL", "return_code": 3, "promotion": "BLOCKED"},
            {"status": "BRANCH_TUBE_VIOLATION", "return_code": 4, "promotion": "SCIENTIFIC_STOP"},
            {"status": "INVALID_BRANCH_PROOF_CONTRACT", "return_code": 5, "promotion": "BLOCKED"},
        ],
        "scheduler": [
            {
                "classification": name,
                "evaluator_status_required": name == "COMMITTED_EVALUATOR_RESULT",
                "promotion": "CONDITIONAL" if name == "COMMITTED_EVALUATOR_RESULT" else "BLOCKED",
            }
            for name in (
                "COMMITTED_EVALUATOR_RESULT", "CELL_TIMEOUT", "CELL_SIGNAL",
                "CELL_OUTPUT_BUDGET_EXHAUSTED", "MALFORMED_EVALUATOR_OUTPUT",
                "PROVENANCE_INVALID",
            )
        ],
    }


def _formal_machine_requirements() -> dict[str, int]:
    return {
        "logical_cpu_count": 32, "memory_limit_bytes": 60 * 1024**3,
        "static_workers": 8, "branch_workers": 6,
        "memory_admission_limit_bytes": 48 * 1024**3,
        "reserve_bytes": 8 * 1024**3, "launch_free_bytes": 200 * 1024**3,
        "warning_free_bytes": 180 * 1024**3, "pause_free_bytes": 150 * 1024**3,
        "recovery_only_free_bytes": 120 * 1024**3,
    }


def _formal_archive_layout() -> dict[str, Any]:
    return {
        "authoritative_relative": V2_RESULT_RELATIVE,
        "operational_suffix": ".operational",
        "static_cell_files": ["proof.json", "stdout.txt", "stderr.txt", "record.json"],
        "branch_cell_files": ["stdout.txt", "stderr.txt", "record.json"],
        "static_serializer": "CJ_COMPACT_V1", "branch_serializer": "CJ_PRETTY_2_V1",
        "aggregate_serializer": "CJ_COMPACT_V1",
    }


def _formal_failure_policy() -> dict[str, Any]:
    return {
        "stop_after_current_barrier": True, "retry_same_generation": False,
        "aggregate_requires_certified_cells": 102,
        "quarantine_on_corrupt_recovery": True,
    }


def _formal_execution_policy() -> dict[str, Any]:
    return {
        "initialize_only_writes_run_config": True,
        "execute_requires_existing_config": True, "execute_requires_resume": True,
        "explicit_execution_flags": ["--production", "--execute-scientific-dispatch", "--resume"],
        "config_self_authorizes": False,
        "branch_millisecond_migration_complete": True,
    }


def _require_null_program_statuses(value: Mapping[str, Any], context: str) -> None:
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(value.get(key) is None, f"{context}: unauthorized {key}")


def _git_object_frame(kind: bytes, payload: bytes) -> bytes:
    return kind + b" " + str(len(payload)).encode("ascii") + b"\x00" + payload


def _git_context(project_root: Path) -> tuple[Path, PurePosixPath]:
    root = require_canonical_absolute_path(project_root, "V2 Git project root")
    cursor = root
    while True:
        candidate = cursor / ".git"
        try:
            info = os.lstat(candidate)
        except FileNotFoundError:
            pass
        else:
            require(stat.S_ISDIR(info.st_mode), "V2 Git directory indirection is forbidden")
            prefix = PurePosixPath(root.relative_to(cursor).as_posix())
            if prefix == PurePosixPath("."):
                prefix = PurePosixPath()
            return candidate, prefix
        require(cursor.parent != cursor, "V2 authority root is outside a Git checkout")
        cursor = cursor.parent


def _git_inflate(raw: bytes, context: str, cap: int = 64 * 1024 * 1024) -> tuple[bytes, int]:
    inflater = zlib.decompressobj()
    try:
        payload = inflater.decompress(raw, cap + 1)
        payload += inflater.flush()
    except zlib.error as error:
        raise CheckError(f"{context}: malformed zlib stream") from error
    require(inflater.eof and len(payload) <= cap, f"{context}: incomplete or oversize zlib stream")
    return payload, len(raw) - len(inflater.unused_data)


def _git_parse_framed(framed: bytes, oid: str, context: str) -> tuple[bytes, bytes]:
    require(re.fullmatch(r"[0-9a-f]{40}", oid) is not None, f"{context}: malformed object id")
    require(hashlib.sha1(framed, usedforsecurity=False).hexdigest() == oid, f"{context}: object id mismatch")
    try:
        header, payload = framed.split(b"\x00", 1)
        kind, size_raw = header.split(b" ", 1)
        size = int(size_raw.decode("ascii"))
    except (ValueError, UnicodeError) as error:
        raise CheckError(f"{context}: malformed object header") from error
    require(kind in {b"commit", b"tree", b"blob", b"tag"}, f"{context}: unsupported object kind")
    require(str(size).encode("ascii") == size_raw and size == len(payload), f"{context}: noncanonical size")
    return kind, payload


def _git_apply_delta(base: bytes, delta: bytes, context: str) -> bytes:
    def varint(offset: int) -> tuple[int, int]:
        value = 0
        shift = 0
        while True:
            require(offset < len(delta) and shift <= 63, f"{context}: truncated delta varint")
            byte = delta[offset]
            offset += 1
            value |= (byte & 0x7f) << shift
            if not byte & 0x80:
                return value, offset
            shift += 7

    base_size, cursor = varint(0)
    result_size, cursor = varint(cursor)
    require(base_size == len(base) and result_size <= 64 * 1024 * 1024, f"{context}: delta size mismatch")
    output = bytearray()
    while cursor < len(delta):
        opcode = delta[cursor]
        cursor += 1
        require(opcode != 0, f"{context}: reserved zero delta opcode")
        if opcode & 0x80:
            offset = 0
            size = 0
            for bit, shift in ((0x01, 0), (0x02, 8), (0x04, 16), (0x08, 24)):
                if opcode & bit:
                    require(cursor < len(delta), f"{context}: truncated copy offset")
                    offset |= delta[cursor] << shift
                    cursor += 1
            for bit, shift in ((0x10, 0), (0x20, 8), (0x40, 16)):
                if opcode & bit:
                    require(cursor < len(delta), f"{context}: truncated copy size")
                    size |= delta[cursor] << shift
                    cursor += 1
            if size == 0:
                size = 0x10000
            require(offset + size <= len(base), f"{context}: copy escapes base")
            output.extend(base[offset:offset + size])
        else:
            require(cursor + opcode <= len(delta), f"{context}: insert exceeds delta")
            output.extend(delta[cursor:cursor + opcode])
            cursor += opcode
        require(len(output) <= result_size, f"{context}: delta result overflow")
    require(len(output) == result_size, f"{context}: delta result size mismatch")
    return bytes(output)


@dataclass(frozen=True)
class _GitPack:
    raw: bytes
    oid_by_offset: Mapping[int, str]


def _git_pack_catalog(git_dir: Path) -> tuple[dict[str, tuple[_GitPack, int]], dict[tuple[int, int], tuple[_GitPack, str]]]:
    by_oid: dict[str, tuple[_GitPack, int]] = {}
    by_offset: dict[tuple[int, int], tuple[_GitPack, str]] = {}
    pack_dir = git_dir / "objects" / "pack"
    try:
        names = sorted(entry.name for entry in os.scandir(pack_dir) if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name))
    except FileNotFoundError:
        return by_oid, by_offset
    for name in names:
        index_raw = read_pinned_regular_bytes(pack_dir / name)
        require(len(index_raw) >= 8 + 256 * 4 + 40 and index_raw[:4] == b"\xfftOc", f"Git index {name}: invalid header")
        require(struct.unpack_from(">I", index_raw, 4)[0] == 2, f"Git index {name}: version 2 required")
        require(hashlib.sha1(index_raw[:-20], usedforsecurity=False).digest() == index_raw[-20:], f"Git index {name}: checksum")
        fanout = struct.unpack_from(">256I", index_raw, 8)
        require(all(a <= b for a, b in zip(fanout, fanout[1:])), f"Git index {name}: fanout order")
        count = fanout[-1]
        names_at = 8 + 256 * 4
        crc_at = names_at + count * 20
        offsets_at = crc_at + count * 4
        large_at = offsets_at + count * 4
        require(large_at + 40 <= len(index_raw), f"Git index {name}: truncated tables")
        large_count = (len(index_raw) - 40 - large_at) // 8
        require(large_at + large_count * 8 + 40 == len(index_raw), f"Git index {name}: malformed large table")
        rows: list[tuple[str, int]] = []
        for index in range(count):
            oid = index_raw[names_at + index * 20:names_at + (index + 1) * 20].hex()
            offset = struct.unpack_from(">I", index_raw, offsets_at + index * 4)[0]
            if offset & 0x80000000:
                large_index = offset & 0x7fffffff
                require(large_index < large_count, f"Git index {name}: large offset range")
                offset = struct.unpack_from(">Q", index_raw, large_at + large_index * 8)[0]
            rows.append((oid, offset))
        require([oid for oid, _ in rows] == sorted(oid for oid, _ in rows), f"Git index {name}: oid order")
        require(len({oid for oid, _ in rows}) == count and len({offset for _, offset in rows}) == count, f"Git index {name}: aliases")
        pack_raw = read_pinned_regular_bytes(pack_dir / (name[:-4] + ".pack"))
        require(len(pack_raw) >= 32 and pack_raw[:4] == b"PACK", f"Git pack {name}: header")
        require(struct.unpack_from(">I", pack_raw, 4)[0] in (2, 3), f"Git pack {name}: version")
        require(struct.unpack_from(">I", pack_raw, 8)[0] == count, f"Git pack {name}: count")
        require(hashlib.sha1(pack_raw[:-20], usedforsecurity=False).digest() == pack_raw[-20:], f"Git pack {name}: checksum")
        require(index_raw[-40:-20] == pack_raw[-20:], f"Git pack {name}: index binding")
        pack = _GitPack(pack_raw, {offset: oid for oid, offset in rows})
        for oid, offset in rows:
            # Repacking may leave the same content-addressed object in more
            # than one checksum-verified pack.  Selecting the first stable
            # pack is safe because the framed SHA-1 is rechecked after delta
            # reconstruction; a different byte image cannot share this key.
            by_oid.setdefault(oid, (pack, offset))
            by_offset[(id(pack.raw), offset)] = (pack, oid)
    return by_oid, by_offset


def _git_pack_entry(pack: _GitPack, offset: int, catalog: Mapping[str, tuple[_GitPack, int]], active: set[tuple[int, int]]) -> tuple[bytes, bytes]:
    key = (id(pack.raw), offset)
    require(key not in active, "Git delta cycle")
    active.add(key)
    try:
        raw = pack.raw
        require(12 <= offset < len(raw) - 20, "Git packed offset out of range")
        cursor = offset
        first = raw[cursor]
        cursor += 1
        kind_code = (first >> 4) & 7
        declared = first & 0x0f
        shift = 4
        current = first
        while current & 0x80:
            require(cursor < len(raw) - 20 and shift <= 63, "Git packed header truncated")
            current = raw[cursor]
            cursor += 1
            declared |= (current & 0x7f) << shift
            shift += 7
        base_offset: int | None = None
        base_oid: str | None = None
        if kind_code == 6:
            require(cursor < len(raw) - 20, "Git ofs-delta base truncated")
            byte = raw[cursor]
            cursor += 1
            distance = byte & 0x7f
            while byte & 0x80:
                require(cursor < len(raw) - 20, "Git ofs-delta distance truncated")
                byte = raw[cursor]
                cursor += 1
                distance = ((distance + 1) << 7) | (byte & 0x7f)
            base_offset = offset - distance
            require(base_offset in pack.oid_by_offset, "Git ofs-delta base missing")
        elif kind_code == 7:
            require(cursor + 20 <= len(raw) - 20, "Git ref-delta base truncated")
            base_oid = raw[cursor:cursor + 20].hex()
            cursor += 20
        payload, _consumed = _git_inflate(raw[cursor:-20], "Git packed object")
        if kind_code in (1, 2, 3, 4):
            kinds = {1: b"commit", 2: b"tree", 3: b"blob", 4: b"tag"}
            require(len(payload) == declared, "Git packed object size mismatch")
            return kinds[kind_code], payload
        require(kind_code in (6, 7), "Git packed object type unsupported")
        require(
            len(payload) == declared,
            "Git packed delta instruction size mismatch",
        )
        if base_offset is not None:
            base_kind, base = _git_pack_entry(pack, base_offset, catalog, active)
        else:
            assert base_oid is not None
            base_kind, base = _git_read_object_from_catalog(base_oid, catalog, active)
        result = _git_apply_delta(base, payload, "Git packed delta")
        return base_kind, result
    finally:
        active.remove(key)


def _git_read_object_from_catalog(oid: str, catalog: Mapping[str, tuple[_GitPack, int]], active: set[tuple[int, int]]) -> tuple[bytes, bytes]:
    require(oid in catalog, f"Git packed object unavailable: {oid}")
    pack, offset = catalog[oid]
    kind, payload = _git_pack_entry(pack, offset, catalog, active)
    require(hashlib.sha1(_git_object_frame(kind, payload), usedforsecurity=False).hexdigest() == oid, f"Git packed object id mismatch: {oid}")
    return kind, payload


def _git_read_object(git_dir: Path, oid: str, catalog: Mapping[str, tuple[_GitPack, int]]) -> tuple[bytes, bytes]:
    require(re.fullmatch(r"[0-9a-f]{40}", oid) is not None, "Git object id malformed")
    loose = git_dir / "objects" / oid[:2] / oid[2:]
    try:
        loose_before = os.lstat(loose)
    except FileNotFoundError:
        loose_before = None
    if loose_before is not None:
        require(stat.S_ISREG(loose_before.st_mode), f"Git loose object is not regular: {oid}")
        compressed = read_pinned_regular_bytes(loose)
        framed, _ = _git_inflate(compressed, f"Git loose object {oid}")
        return _git_parse_framed(framed, oid, f"Git loose object {oid}")
    result = _git_read_object_from_catalog(oid, catalog, set())
    try:
        os.lstat(loose)
    except FileNotFoundError:
        return result
    raise CheckError(f"Git loose/packed namespace changed during replay: {oid}")


def _git_tree_entries(payload: bytes, context: str) -> dict[bytes, tuple[str, str]]:
    cursor = 0
    entries: dict[bytes, tuple[str, str]] = {}
    order: list[bytes] = []
    while cursor < len(payload):
        space = payload.find(b" ", cursor)
        nul = payload.find(b"\x00", space + 1)
        require(space > cursor and nul > space and nul + 21 <= len(payload), f"{context}: malformed entry")
        mode_raw = payload[cursor:space]
        name = payload[space + 1:nul]
        oid = payload[nul + 1:nul + 21].hex()
        require(mode_raw in {b"100644", b"100755", b"120000", b"40000"}, f"{context}: mode")
        require(name and b"/" not in name and name not in {b".", b".."} and name not in entries, f"{context}: name")
        entries[name] = (mode_raw.decode("ascii"), oid)
        order.append(name + (b"/" if mode_raw == b"40000" else b""))
        cursor = nul + 21
    require(order == sorted(order), f"{context}: noncanonical tree order")
    return entries


def _git_blob_from_catalog(
    git_dir: Path,
    prefix: PurePosixPath,
    catalog: Mapping[str, tuple[_GitPack, int]],
    commit_oid: str,
    relative: str,
) -> tuple[bytes, str]:
    kind, commit = _git_read_object(git_dir, commit_oid, catalog)
    require(kind == b"commit", "Git review object is not a commit")
    match = re.match(rb"tree ([0-9a-f]{40})\n", commit)
    require(match is not None, "Git commit lacks canonical tree header")
    oid = match.group(1).decode("ascii")
    parts = (*prefix.parts, *_safe_relative(relative, "Git reviewed path").parts)
    mode = ""
    for index, part in enumerate(parts):
        kind, tree = _git_read_object(git_dir, oid, catalog)
        require(kind == b"tree", f"Git path ancestor is not a tree: {part}")
        entries = _git_tree_entries(tree, f"Git tree for {relative}")
        name = part.encode("utf-8", errors="strict")
        require(name in entries, f"Git reviewed path missing: {relative}")
        mode, oid = entries[name]
        require((index < len(parts) - 1) is (mode == "40000"), f"Git reviewed path kind mismatch: {relative}")
    kind, blob = _git_read_object(git_dir, oid, catalog)
    require(kind == b"blob" and mode in {"100644", "100755"}, f"Git reviewed terminal is not a regular blob: {relative}")
    return blob, mode


def _git_blob_batch(
    project_root: Path,
    queries: Sequence[tuple[str, str]],
) -> list[tuple[bytes, str]]:
    git_dir, prefix = _git_context(project_root)
    catalog, _ = _git_pack_catalog(git_dir)
    return [
        _git_blob_from_catalog(git_dir, prefix, catalog, commit, relative)
        for commit, relative in queries
    ]


def _git_blob_at(project_root: Path, commit_oid: str, relative: str) -> tuple[bytes, str]:
    return _git_blob_batch(project_root, [(commit_oid, relative)])[0]


def _git_commit_tree(project_root: Path, commit_oid: str) -> str:
    git_dir, _prefix = _git_context(project_root)
    catalog, _ = _git_pack_catalog(git_dir)
    kind, commit = _git_read_object(git_dir, commit_oid, catalog)
    require(kind == b"commit", "Git snapshot object is not a commit")
    match = re.match(rb"tree ([0-9a-f]{40})\n", commit)
    require(match is not None, "Git snapshot commit lacks canonical tree")
    return match.group(1).decode("ascii")


def _live_role_binding(
    project_root: Path, role: str, relative: str
) -> tuple[
    dict[str, Any],
    bytes,
    tuple[tuple[int, int, int, int, int, int, int, int, int], _ParentChainIdentity],
]:
    path = _project_file(project_root, relative)
    pinned = _read_pinned_regular_snapshot(path)
    raw, info = pinned.raw, pinned.info
    require(info.st_nlink == 1, f"V2 role {role}: hard link")
    if relative.endswith(".json"):
        payload, canonical = load_strict_json_object_from_bytes(raw, path), None
        del payload, canonical
    return {
        "role": role, "path": relative, "sha256": sha256_bytes(raw),
        "size_bytes": len(raw), "mode": f"{stat.S_IMODE(info.st_mode):04o}",
        "nlink": info.st_nlink,
    }, raw, (_stable_stat_identity(info), pinned.parent_chain)


def _capture_formal_roles(project_root: Path) -> tuple[
    list[dict[str, str]],
    dict[str, bytes],
    dict[str, dict[str, Any]],
    dict[str, tuple[tuple[int, int, int, int, int, int, int, int, int], _ParentChainIdentity]],
]:
    require(
        len(INPUT_ROLES) == 53
        and len({role for role, _ in INPUT_ROLES}) == 53
        and len({path for _, path in INPUT_ROLES}) == 53,
        "V2 literal role map is not exact unique 53",
    )
    rows: list[dict[str, str]] = []
    images: dict[str, bytes] = {}
    metadata: dict[str, dict[str, Any]] = {}
    generations: dict[
        str,
        tuple[tuple[int, int, int, int, int, int, int, int, int], _ParentChainIdentity],
    ] = {}
    for role, relative in INPUT_ROLES:
        binding, raw, generation = _live_role_binding(project_root, role, relative)
        if role == "prefreeze_review":
            require(raw == PREFREEZE_ACCEPT_RAW, "V2 role12 must be exact 27-byte ACCEPT verdict")
        rows.append({key: binding[key] for key in ("role", "path", "sha256")})
        images[role] = raw
        metadata[role] = binding
        generations[role] = generation
    return rows, images, metadata, generations


def _validate_role5(
    project_root: Path,
    payload: Any,
    role_rows: Sequence[Mapping[str, str]],
    role_images: Mapping[str, bytes],
) -> None:
    require(type(payload) is dict, "V2 role5: object required")
    exact_keys(payload, ROLE5_KEYS, "V2 role5")
    require_exact_int(payload["schema_version"], "V2 role5.schema_version", expected=1)
    require_json_exact(
        {key: payload[key] for key in (
            "protocol_id", "artifact_role", "status", "authority",
            "scientific_licensing_enabled", "production_authorized", "claim_boundary",
            "component_status", "milestone_status", "theorem_status", "final_status",
        )},
        {
            "protocol_id": PROTOCOL_ID,
            "artifact_role": "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL",
            "status": "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1",
            "authority": "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY",
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "claim_boundary": ROLE5_CLAIM_BOUNDARY,
            "component_status": None, "milestone_status": None,
            "theorem_status": None, "final_status": None,
        },
        "V2 role5 literal envelope",
    )
    expected_legacy = {
        "attempt_id": "A416_L3_A1_CONTROL_ATTEMPT_1",
        "status": "WITHDRAWN_NON_LICENSING",
        "terminal_commit": "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0",
        "published_artifacts": list(ROLE5_LEGACY_ARTIFACTS),
        "defects": list(ROLE5_LEGACY_DEFECTS),
        "supersession_rule": ROLE5_SUPERSESSION_RULE,
    }
    require_json_exact(payload["legacy_attempt"], expected_legacy, "V2 role5 legacy attempt")
    role_by_name = {row["role"]: row for row in role_rows}
    expected_reviewed = [dict(role_by_name[role]) for role in ROLE5_REVIEWED_ROLES]
    require_json_exact(payload["reviewed_v2_inputs"], expected_reviewed, "V2 role5 reviewed inputs")
    review = payload["review"]
    require(type(review) is dict, "V2 role5.review: object required")
    exact_keys(
        review,
        {"reviewer_independent_of_attempt1_author", "verdict", "p0_count", "p1_count", "p2_count", "reviewed_commit", "map_matches_contract", "legacy_bytes_unchanged", "scientific_protocol_unchanged"},
        "V2 role5.review",
    )
    require(
        review["reviewer_independent_of_attempt1_author"] is True
        and review["verdict"] == "ACCEPT_CONTROL_PLANE_V2_DESIGN"
        and all(type(review[key]) is int and review[key] == 0 for key in ("p0_count", "p1_count", "p2_count"))
        and type(review["reviewed_commit"]) is str
        and re.fullmatch(r"[0-9a-f]{40}", review["reviewed_commit"]) is not None
        and review["map_matches_contract"] is True
        and review["legacy_bytes_unchanged"] is True
        and review["scientific_protocol_unchanged"] is True,
        "V2 role5 independent review gate mismatch",
    )

    # The review's claims are meaningful only when proved against immutable
    # Git objects.  Resolve commit -> tree -> exact path -> regular blob using
    # the in-process object parser above; no Git command or subprocess exists.
    legacy_queries = [
        (item["publication_commit"], item["path"])
        for item in ROLE5_LEGACY_ARTIFACTS
    ]
    reviewed_queries = [
        (review["reviewed_commit"], role_by_name[role]["path"])
        for role in ROLE5_REVIEWED_ROLES
    ]
    committed_images = _git_blob_batch(project_root, [*legacy_queries, *reviewed_queries])
    legacy_committed = committed_images[:len(legacy_queries)]
    reviewed_committed = committed_images[len(legacy_queries):]
    for item, (committed, mode) in zip(ROLE5_LEGACY_ARTIFACTS, legacy_committed, strict=True):
        live = read_pinned_regular_bytes(_project_file(project_root, item["path"]))
        require(sha256_bytes(live) == item["sha256"], "V2 role5 legacy live bytes changed")
        require(mode == "100644", "V2 role5 legacy Git mode mismatch")
        require(committed == live and sha256_bytes(committed) == item["sha256"], "V2 role5 legacy publication blob mismatch")
    for role, (committed, mode) in zip(ROLE5_REVIEWED_ROLES, reviewed_committed, strict=True):
        row = role_by_name[role]
        require(mode == "100644", f"V2 role5 reviewed Git mode mismatch: {role}")
        require(committed == role_images[role] and sha256_bytes(committed) == row["sha256"], f"V2 role5 reviewed Git blob mismatch: {role}")


MACHINE_FREEZE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "production_authorized", "capture",
    "machine_requirements", "machine_observations", "python_arb", "capd",
    "compiler", "branch_binary", "runtime_libraries", "resource_evidence",
    "resource_admission", "filesystem", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
MACHINE_CAPTURE_KEYS = {"captured_at_utc", "capture_tool_path", "capture_tool_sha256", "boot_id_sha256"}
MACHINE_OBSERVATION_KEYS = {
    "logical_cpu_count", "memory_limit_bytes", "result_parent_free_bytes",
    "idle_baseline_rss_bytes", "representative_static_peak_rss_bytes",
    "representative_branch_peak_rss_bytes",
}
MACHINE_PYTHON_KEYS = {
    "executable_path", "executable_sha256", "python_version", "implementation",
    "python_flint_version", "flint_version", "arb_version",
    "conda_manifest_algorithm", "conda_manifest_file_count",
    "conda_installed_manifest_root_sha256", "python_flint_record_sha256",
    "python_flint_installed_manifest_root_sha256", "arb_extension",
    "fmpq_extension", "bundled_libraries",
}
MACHINE_CAPD_KEYS = {
    "checkout_path", "commit", "tree_algorithm", "tree_sha256", "clean",
    "cmake_cache_path", "cmake_cache_sha256", "config_path", "config_sha256",
    "raw_flags", "raw_flags_sha256", "libcapd", "libfilib",
}
MACHINE_COMPILER_KEYS = {
    "executable_path", "executable_sha256", "version", "build_recipe",
    "fresh_rebuild_receipt", "transfer_evidence",
}
MACHINE_BUILD_RECIPE_KEYS = {"cwd", "environment", "umask", "staging_output_token", "argv_template", "argv_template_sha256"}
MACHINE_REBUILD_KEYS = {
    "cwd", "environment", "umask", "staging_directory", "staging_output_path",
    "argv", "argv_sha256", "stdout", "stderr", "stdout_sha256", "stderr_sha256",
    "return_code", "output_sha256", "output_size_bytes", "output_mode",
    "output_build_id", "output_dt_needed", "output_dt_needed_sha256",
    "output_soname", "shell_used",
}
MACHINE_TRANSFER_KEYS = {
    "staging_output_sha256", "staging_output_size_bytes", "staging_output_mode",
    "branch_calibration_binary_sha256", "persistent_before_sha256",
    "persistent_before_size_bytes", "persistent_before_mode",
    "persistent_before_device_id", "persistent_before_inode",
    "persistent_after_sha256", "persistent_after_size_bytes",
    "persistent_after_mode", "persistent_after_device_id", "persistent_after_inode",
    "byte_for_byte_equal", "persistent_identity_unchanged",
    "persistent_overwrite_performed",
}
MACHINE_BRANCH_BINARY_KEYS = {
    "path", "sha256", "size_bytes", "executable_mode", "build_id", "source_path",
    "source_sha256", "elf_sha256", "dt_needed", "dt_needed_sha256",
    "runtime_libraries_sha256",
}
MACHINE_RUNTIME_ROW_KEYS = {"soname", "path", "mode", "size_bytes", "sha256", "build_id"}
MACHINE_FILE_BINDING_KEYS = {"path", "mode", "size_bytes", "sha256", "build_id"}
MACHINE_RESOURCE_KEYS = {"static_payload_raw_utf8", "static_payload_sha256", "branch_payload_raw_utf8", "branch_payload_sha256", "persistent_binary_sha256"}
MACHINE_ADMISSION_KEYS = {"static_required_bytes", "branch_required_bytes", "admitted_required_bytes", "admission_limit_bytes", "static_inequality_passed", "branch_inequality_passed", "storage_launch_passed"}
MACHINE_FILESYSTEM_KEYS = {"project_root", "result_parent", "operational_parent", "project_device_id", "result_device_id", "operational_device_id", "same_filesystem"}
MACHINE_CLAIM_BOUNDARY = (
    "machine, toolchain, persistent-binary, filesystem, and representative "
    "resource admission only; no evaluator dispatch, component status, local "
    "theorem, global routing, Hilbert-Polya, zeta-zero, or RH claim"
)
MACHINE_PYTHON_VERSION = (
    "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) "
    "[GCC 11.2.0]"
)
MACHINE_COMPILER_VERSION = "g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
MACHINE_EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
MACHINE_PYTHON_BUNDLED_SONAMES = (
    "libflint-6839011d.so.24.0.0",
    "libgmp-e0c82b6b.so.10.5.0",
    "libmpfr-be332c05.so.6.2.2",
)
MACHINE_CAPD_SYSTEM_SONAMES = (
    "ld-linux-x86-64.so.2", "libc.so.6", "libgcc_s.so.1",
    "libgmp.so.10", "libm.so.6", "libmpfr.so.6", "libstdc++.so.6",
)
MACHINE_DT_NEEDED = [
    "libc.so.6", "libgcc_s.so.1", "libm.so.6", "libmpfr.so.6",
    "libstdc++.so.6",
]
MACHINE_BUILD_ENVIRONMENT = {
    "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
    "TZ": "UTC", "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
    "PYTHONDONTWRITEBYTECODE": "1",
}
MACHINE_CONDA_ALGORITHM = "CONDA_META_LIVE_FILES_CJ_COMPACT_V1"
MACHINE_FLINT_RECORD_SHA256 = (
    "a140c3cb2ba819edc913c2adae2dc0a60d49f7f3be547f139b7beb8be9c0d3da"
)
MACHINE_FLINT_MANIFEST_SHA256 = (
    "32a2b16585f81fe5cd4a4c3b7d0d70e0f867f1a032db4b9c3b0f414cf991c870"
)
MACHINE_CAPD_TREE_ALGORITHM = "GIT_INDEX_LIVE_TREE_CJ_COMPACT_V1"
MACHINE_STAGING_TOKEN = "@STAGING_BINARY@"
MACHINE_BUILD_ID = re.compile(r"[0-9a-f]{40}\Z")
MACHINE_TIMESTAMP = re.compile(
    r"(?:19|20)[0-9]{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
    r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z\Z"
)
STATIC_RESOURCE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "scope",
    "production_authorized", "scientific_licensing_enabled", "claim_boundary",
    "project_root", "temporary_root", "execution_environment", "bindings",
    "measurement", "sequential_runs", "concurrent_schedule", "concurrent_runs",
    "admission", "component_status", "milestone_status", "theorem_status",
    "final_status",
}
STATIC_RESOURCE_BINDING_KEYS = {
    "evaluator", "interpreter", "python_flint", "plan", "calibration_binding",
}
STATIC_RESOURCE_EVALUATOR_KEYS = {"path", "sha256", "size_bytes", "mode"}
STATIC_RESOURCE_INTERPRETER_KEYS = {
    "invocation_path", "resolved_path", "sha256", "size_bytes", "version",
}
STATIC_RESOURCE_FLINT_KEYS = {
    "version", "flint_version", "module_path", "record_path", "record_sha256",
    "installed_record_file_count", "installed_manifest_sha256",
    "arb_extension_path", "arb_extension_sha256",
}
STATIC_RESOURCE_PLAN_KEYS = {"path", "sha256", "public_slab_ids"}
STATIC_RESOURCE_CALIBRATION_KEYS = {
    "matrix_id", "nonfreeze_sha256", "nonrunconfig_sha256",
}
STATIC_RESOURCE_ENV_KEYS = {
    "LANG", "LC_ALL", "TZ", "PYTHONHASHSEED", "PYTHONNOUSERSITE",
    "PYTHONDONTWRITEBYTECODE", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
}
STATIC_RESOURCE_MEASUREMENT_KEYS = {
    "method", "ru_maxrss_unit", "bytes_per_kib", "cgroup_usage_path",
    "cgroup_limit_path", "cgroup_limit_bytes", "baseline_samples_bytes",
    "baseline_conservative_bytes", "concurrent_samples_bytes",
    "concurrent_peak_bytes", "sample_interval_seconds",
}
STATIC_RESOURCE_RUN_KEYS = {
    "label", "precision_bits", "slab_id", "replica", "argv", "returncode",
    "elapsed_seconds", "peak_rss_kib", "user_cpu_seconds", "system_cpu_seconds",
    "output", "output_bytes", "output_sha256", "stdout", "stdout_bytes",
    "stdout_sha256", "stdout_exact_status_line", "stderr", "stderr_bytes",
    "stderr_sha256", "stderr_empty", "evaluator_status", "scientific_status",
    "component_status", "milestone_status", "theorem_status", "final_status",
}
STATIC_RESOURCE_SCHEDULE_KEYS = {"precision_bits", "slab_id"}
STATIC_RESOURCE_ADMISSION_KEYS = {
    "workers", "representative_peak_rss_bytes", "idle_baseline_bytes",
    "reserve_bytes", "admission_limit_bytes", "lhs_bytes", "headroom_bytes",
    "formula", "passes",
}
BRANCH_RESOURCE_KEYS = {
    "scope", "binary", "binary_sha256", "cgroup_limit_bytes",
    "baseline_samples_bytes", "baseline_conservative_bytes", "post_samples_bytes",
    "results", "task_count", "per_process_peak_rss_max_kib",
    "sampled_concurrent_peak_bytes", "sampled_concurrent_increment_bytes",
    "admission", "scientific_status", "milestone_status", "theorem_status",
    "final_status",
}
BRANCH_RESOURCE_RUN_KEYS = {
    "precision_bits", "slab_id", "argv", "argv_count", "returncode",
    "elapsed_seconds", "peak_rss_kib", "user_cpu_seconds", "system_cpu_seconds",
    "stdout_bytes", "stdout_sha256", "stderr_bytes", "stderr_sha256",
    "abi_verified", "terminal_abi_value",
}
BRANCH_RESOURCE_ADMISSION_KEYS = {
    "baseline_bytes", "peak_rss_bytes", "workers", "reserve_bytes",
    "limit_bytes", "lhs_bytes", "headroom_bytes", "formula", "passes",
}


def _exact_sha(value: Any, context: str) -> str:
    require(type(value) is str and HEX_SHA256.fullmatch(value) is not None, f"{context}: lowercase SHA-256 required")
    return value


def _machine_identity(info: os.stat_result) -> tuple[int, int, int, int, int, int, int]:
    return (
        info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
        info.st_size, info.st_mtime_ns, info.st_ctime_ns,
    )


def _machine_manifest_regular(
    path: Path,
    context: str,
    *,
    maximum_bytes: int = 1024 * 1024 * 1024,
) -> tuple[bytes, os.stat_result]:
    """Pinned regular reader for package-managed files (hard links allowed)."""

    path = require_canonical_absolute_path(path, context)
    parent_fd = _open_directory_fd(path.parent)
    descriptor: int | None = None
    try:
        before = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        require(
            stat.S_ISREG(before.st_mode)
            and before.st_nlink >= 1
            and 0 <= before.st_size <= maximum_bytes,
            f"{context}: bounded package regular file required",
        )
        descriptor = os.open(
            path.name,
            os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
        opened = os.fstat(descriptor)
        require(_machine_identity(opened) == _machine_identity(before), f"{context}: open race")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(
                descriptor,
                min(1024 * 1024, maximum_bytes + 1 - total),
            )
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            require(total <= maximum_bytes, f"{context}: byte cap")
        after = os.fstat(descriptor)
        replay = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        raw = b"".join(chunks)
        require(
            _machine_identity(before) == _machine_identity(after)
            == _machine_identity(replay)
            and len(raw) == before.st_size,
            f"{context}: package file changed during read",
        )
        return raw, before
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def _machine_manifest_symlink(path: Path, context: str) -> tuple[bytes, os.stat_result]:
    path = require_canonical_absolute_path(path, context)
    parent_fd = _open_directory_fd(path.parent)
    try:
        before = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        require(stat.S_ISLNK(before.st_mode), f"{context}: symlink required")
        first = os.readlink(path.name, dir_fd=parent_fd)
        after = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        second = os.readlink(path.name, dir_fd=parent_fd)
        require(
            type(first) is str and first == second
            and "\x00" not in first
            and _machine_identity(before) == _machine_identity(after),
            f"{context}: symlink changed",
        )
        return first.encode("utf-8", errors="strict"), before
    finally:
        os.close(parent_fd)


def _machine_external_snapshot(
    value: Any, context: str
) -> tuple[bytes, os.stat_result, Path]:
    require(type(value) is str, f"{context}: exact absolute path required")
    lexical = require_canonical_absolute_path(value, context)
    parent_chain = _directory_chain(lexical.parent)
    before = os.stat(lexical, follow_symlinks=False)
    resolved = require_canonical_absolute_path(lexical.resolve(strict=True), context)
    pinned = _read_pinned_regular_snapshot(resolved, context=context)
    raw, resolved_info = pinned.raw, pinned.info
    after = os.stat(lexical, follow_symlinks=False)
    require(
        _machine_identity(before) == _machine_identity(after)
        and lexical.resolve(strict=True) == resolved
        and _directory_chain(lexical.parent) == parent_chain,
        f"{context}: lexical tool/library path changed",
    )
    return raw, resolved_info, resolved


def _machine_boot_id_bytes() -> bytes:
    path = Path("/proc/sys/kernel/random/boot_id")
    before = os.stat(path, follow_symlinks=False)
    descriptor = os.open(
        path, os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0)
    )
    try:
        raw = os.read(descriptor, 256)
        require(os.read(descriptor, 1) == b"", "V2 role10 boot ID cap")
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    replay = os.stat(path, follow_symlinks=False)
    require(
        (before.st_dev, before.st_ino) == (after.st_dev, after.st_ino)
        == (replay.st_dev, replay.st_ino)
        and re.fullmatch(
            rb"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\n",
            raw,
        ) is not None,
        "V2 role10 boot ID changed/malformed",
    )
    return raw


def _machine_elf_metadata(
    raw: bytes, context: str
) -> tuple[str, list[str], str | None]:
    header_format = "<16sHHIQQQIHHHHHH"
    section_format = "<IIQQQQIIQQ"
    dynamic_format = "<qQ"
    header_size = struct.calcsize(header_format)
    section_size = struct.calcsize(section_format)
    require(len(raw) >= header_size, f"{context}: truncated ELF")
    header = struct.unpack_from(header_format, raw, 0)
    ident = header[0]
    require(
        ident[:4] == b"\x7fELF" and ident[4:7] == bytes((2, 1, 1))
        and header[2] == 62 and header[3] == 1
        and header[8] == header_size and header[11] == section_size,
        f"{context}: ELF identity/header",
    )
    section_offset, section_count, string_index = header[6], header[12], header[13]
    require(
        section_offset > 0 and section_count > 0 and string_index < section_count
        and section_offset + section_count * section_size <= len(raw),
        f"{context}: ELF section table",
    )
    sections = [
        struct.unpack_from(section_format, raw, section_offset + index * section_size)
        for index in range(section_count)
    ]

    def section_bytes(index: int, label: str) -> bytes:
        require(0 <= index < len(sections), f"{context}: ELF {label} index")
        offset, size = sections[index][4], sections[index][5]
        require(offset <= len(raw) and size <= len(raw) - offset, f"{context}: ELF {label} bounds")
        return raw[offset:offset + size]

    require(sections[string_index][1] == 3, f"{context}: ELF section-name table")
    section_bytes(string_index, "section-name")
    build_ids: list[str] = []
    needed: list[str] = []
    sonames: list[str] = []
    for index, section in enumerate(sections):
        if section[1] == 7:
            note = section_bytes(index, "note")
            cursor = 0
            while cursor < len(note):
                require(len(note) - cursor >= 12, f"{context}: ELF note header")
                name_size, description_size, note_type = struct.unpack_from("<III", note, cursor)
                cursor += 12
                name_end = cursor + name_size
                description_start = (name_end + 3) & ~3
                description_end = description_start + description_size
                next_cursor = (description_end + 3) & ~3
                require(next_cursor <= len(note), f"{context}: ELF note bounds")
                if note[cursor:name_end] == b"GNU\x00" and note_type == 3:
                    description = note[description_start:description_end]
                    require(len(description) == 20, f"{context}: GNU build-id length")
                    build_ids.append(description.hex())
                cursor = next_cursor
        elif section[1] == 6:
            dynamic = section_bytes(index, "dynamic")
            entry_size = section[9]
            linked = section[6]
            require(
                entry_size == struct.calcsize(dynamic_format)
                and len(dynamic) % entry_size == 0
                and linked < len(sections) and sections[linked][1] == 3,
                f"{context}: ELF dynamic table",
            )
            strings = section_bytes(linked, "dynamic-string")

            def dynamic_string(offset: int) -> str:
                require(0 < offset < len(strings), f"{context}: ELF string offset")
                end = strings.find(b"\x00", offset)
                require(end >= 0, f"{context}: ELF unterminated string")
                try:
                    value = strings[offset:end].decode("ascii")
                except UnicodeError as error:
                    raise CheckError(f"{context}: ELF non-ASCII string") from error
                require(value != "" and "/" not in value, f"{context}: ELF unsafe string")
                return value

            for cursor in range(0, len(dynamic), entry_size):
                tag, value = struct.unpack_from(dynamic_format, dynamic, cursor)
                if tag == 0:
                    break
                if tag == 1:
                    needed.append(dynamic_string(value))
                elif tag == 14:
                    sonames.append(dynamic_string(value))
    require(len(build_ids) == 1 and MACHINE_BUILD_ID.fullmatch(build_ids[0]), f"{context}: one build-id")
    require(len(needed) == len(set(needed)) and len(sonames) <= 1, f"{context}: duplicate dynamic identity")
    return build_ids[0], sorted(needed), sonames[0] if sonames else None


def _validate_machine_file_binding(value: Any, context: str, *, allow_null_build: bool = False) -> Mapping[str, Any]:
    require(type(value) is dict, f"{context}: object required")
    exact_keys(value, MACHINE_FILE_BINDING_KEYS, context)
    require(type(value["path"]) is str and value["path"].startswith("/"), f"{context}: absolute path required")
    raw, info, _resolved = _machine_external_snapshot(value["path"], context)
    require(value["sha256"] == sha256_bytes(raw), f"{context}: live hash mismatch")
    _exact_sha(value["sha256"], f"{context}.sha256")
    require_exact_int(value["size_bytes"], f"{context}.size_bytes", expected=len(raw))
    require(type(value["mode"]) is int and value["mode"] == stat.S_IMODE(info.st_mode), f"{context}: mode mismatch")
    if allow_null_build:
        require(value["build_id"] is None, f"{context}: static archive build_id must be null")
    else:
        require(type(value["build_id"]) is str and MACHINE_BUILD_ID.fullmatch(value["build_id"]), f"{context}: build_id")
        live_build_id, _needed, _soname = _machine_elf_metadata(raw, context)
        require(value["build_id"] == live_build_id, f"{context}: live ELF build-id")
    return value


def _machine_recompute_conda_manifest(executable_path: str) -> tuple[int, str]:
    executable = require_canonical_absolute_path(executable_path, "V2 role10 conda Python")
    require(executable.name == "python3" and executable.parent.name == "bin", "V2 role10 conda layout")
    prefix = executable.parent.parent
    meta_dir = prefix / "conda-meta"
    meta_fd = _open_directory_fd(meta_dir)
    try:
        names = tuple(sorted(os.listdir(meta_fd), key=lambda value: value.encode("utf-8")))
    finally:
        os.close(meta_fd)
    matches = [
        name for name in names
        if re.fullmatch(r"python-3\.12\.3-[A-Za-z0-9_.-]+\.json", name)
    ]
    require(len(matches) == 1, "V2 role10 unique Python conda metadata")
    meta_path = meta_dir / matches[0]
    meta_raw, _ = _machine_manifest_regular(meta_path, "V2 role10 conda metadata")
    metadata = load_strict_json_object_from_bytes(meta_raw, meta_path)
    require(metadata.get("name") == "python" and metadata.get("version") == "3.12.3", "V2 role10 conda metadata identity")
    files = metadata.get("files")
    paths = metadata.get("paths_data", {}).get("paths")
    require(
        type(files) is list and files
        and all(type(item) is str for item in files)
        and type(paths) is list and len(paths) == len(files),
        "V2 role10 conda manifest schema",
    )
    normalized = [_safe_relative(item, "V2 role10 conda file").as_posix() for item in files]
    require(len(normalized) == len(set(normalized)), "V2 role10 conda duplicate file")
    path_names = [item.get("_path") if type(item) is dict else None for item in paths]
    require(
        all(type(item) is str for item in path_names)
        and len(path_names) == len(set(path_names))
        and set(path_names) == set(normalized),
        "V2 role10 conda files/paths_data mismatch",
    )
    rows: list[dict[str, Any]] = []
    for relative in normalized:
        target = prefix.joinpath(*PurePosixPath(relative).parts)
        info = os.stat(target, follow_symlinks=False)
        if stat.S_ISREG(info.st_mode):
            raw, info = _machine_manifest_regular(target, f"V2 role10 conda file {relative}")
            kind = "REGULAR"
        elif stat.S_ISLNK(info.st_mode):
            raw, info = _machine_manifest_symlink(target, f"V2 role10 conda link {relative}")
            kind = "SYMLINK"
        else:
            raise CheckError(f"V2 role10 conda unsupported file type: {relative}")
        rows.append({
            "kind": kind, "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "path": relative, "sha256": sha256_bytes(raw),
            "size_bytes": len(raw),
        })
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    return len(rows), sha256_bytes(canonical_json_bytes(rows))


def _machine_recompute_flint_manifest(
    record_path: str, record_raw: bytes
) -> tuple[int, str]:
    record = require_canonical_absolute_path(record_path, "V2 role10 python-flint RECORD")
    site_packages = record.parents[1]
    try:
        parsed = list(csv.reader(io.StringIO(record_raw.decode("utf-8"), newline="")))
    except (UnicodeError, csv.Error) as error:
        raise CheckError("V2 role10 python-flint RECORD malformed") from error
    require(parsed, "V2 role10 python-flint RECORD empty")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(parsed):
        require(len(row) == 3, f"V2 role10 python-flint RECORD[{index}]")
        relative_raw, declared_digest, declared_size = row
        relative = _safe_relative(relative_raw, "V2 role10 python-flint RECORD path").as_posix()
        require(relative not in seen, "V2 role10 python-flint duplicate RECORD path")
        seen.add(relative)
        target = site_packages.joinpath(*PurePosixPath(relative).parts)
        raw, info = _machine_manifest_regular(target, f"V2 role10 python-flint file {relative}")
        digest = sha256_bytes(raw)
        if declared_digest:
            require(declared_digest.startswith("sha256="), "V2 role10 python-flint non-SHA256 RECORD")
            encoded = declared_digest.removeprefix("sha256=")
            try:
                decoded = base64.urlsafe_b64decode(encoded + "=" * (-len(encoded) % 4))
            except Exception as error:
                raise CheckError("V2 role10 python-flint RECORD digest") from error
            require(decoded.hex() == digest and declared_size == str(len(raw)), "V2 role10 python-flint installed bytes")
        else:
            require(declared_size == "", "V2 role10 python-flint size without digest")
        rows.append({
            "mode": f"{stat.S_IMODE(info.st_mode):04o}", "path": relative,
            "sha256": digest, "size_bytes": len(raw),
        })
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    return len(rows), sha256_bytes(canonical_json_bytes(rows))


def _machine_git_blob_sha1(raw: bytes) -> str:
    framed = b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw
    return hashlib.sha1(framed, usedforsecurity=False).hexdigest()


def _machine_relative(value: Any, context: str) -> PurePosixPath:
    require(type(value) is str and value and "\x00" not in value and "\\" not in value, f"{context}: relative path spelling")
    relative = PurePosixPath(value)
    require(
        not relative.is_absolute() and relative.as_posix() == value
        and all(part not in {"", ".", ".."} for part in relative.parts),
        f"{context}: canonical relative path",
    )
    return relative


def _machine_read_git_index(checkout: Path) -> list[tuple[str, int, str]]:
    path = checkout / ".git/index"
    raw = read_pinned_regular_bytes(path)
    require(len(raw) >= 32 and raw[:4] == b"DIRC", "V2 role10 CAPD Git index header")
    version, count = struct.unpack_from(">II", raw, 4)
    require(version == 2 and count > 0, "V2 role10 CAPD exact nonempty index v2")
    body, checksum = raw[:-20], raw[-20:]
    require(hashlib.sha1(body, usedforsecurity=False).digest() == checksum, "V2 role10 CAPD Git index checksum")
    cursor = 12
    records: list[tuple[str, int, str]] = []
    fixed_format = ">LLLLLLLLLL20sH"
    fixed_size = struct.calcsize(fixed_format)
    for index in range(count):
        start = cursor
        require(cursor + fixed_size <= len(body), f"V2 role10 CAPD index[{index}] truncated")
        fields = struct.unpack_from(fixed_format, body, cursor)
        mode, oid, flags = fields[6], fields[10].hex(), fields[11]
        cursor += fixed_size
        require(not flags & 0xF000, "V2 role10 CAPD staged/extended index entry")
        end = body.find(b"\x00", cursor)
        require(end >= cursor, "V2 role10 CAPD unterminated index path")
        try:
            relative = body[cursor:end].decode("utf-8")
        except UnicodeError as error:
            raise CheckError("V2 role10 CAPD non-UTF8 index path") from error
        relative = _machine_relative(relative, "V2 role10 CAPD index path").as_posix()
        require((flags & 0x0FFF) == min(len(body[cursor:end]), 0x0FFF), "V2 role10 CAPD index path length")
        require(mode in {0o100644, 0o100755, 0o120000}, "V2 role10 CAPD unsupported Git mode")
        cursor = end + 1
        while (cursor - start) % 8:
            require(cursor < len(body) and body[cursor] == 0, "V2 role10 CAPD index padding")
            cursor += 1
        records.append((relative, mode, oid))
    while cursor < len(body):
        require(cursor + 8 <= len(body), "V2 role10 CAPD index extension header")
        signature = body[cursor:cursor + 4]
        size = struct.unpack_from(">I", body, cursor + 4)[0]
        cursor += 8
        require(re.fullmatch(rb"[A-Z]{4}", signature) and size <= len(body) - cursor, "V2 role10 CAPD required/malformed index extension")
        cursor += size
    require(
        records == sorted(records, key=lambda item: item[0].encode("utf-8"))
        and len({item[0] for item in records}) == len(records),
        "V2 role10 CAPD duplicate/unordered index",
    )
    return records


def _machine_index_tree_oid(records: Sequence[tuple[str, int, str]]) -> str:
    def node() -> dict[str, dict[str, Any]]:
        return {"files": {}, "directories": {}}

    root = node()
    for relative, mode, oid in records:
        current = root
        parts = PurePosixPath(relative).parts
        for part in parts[:-1]:
            require(part not in current["files"], "V2 role10 CAPD file/directory prefix")
            current = current["directories"].setdefault(part, node())
        name = parts[-1]
        require(name not in current["files"] and name not in current["directories"], "V2 role10 CAPD duplicate tree entry")
        current["files"][name] = (mode, oid)

    def digest(current: Mapping[str, Any]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, (mode, oid) in current["files"].items():
            raw_name = name.encode("utf-8")
            entries.append((raw_name, f"{mode:06o}".encode() + b" " + raw_name + b"\x00" + bytes.fromhex(oid)))
        for name, child in current["directories"].items():
            raw_name = name.encode("utf-8")
            entries.append((raw_name + b"/", b"40000 " + raw_name + b"\x00" + bytes.fromhex(digest(child))))
        content = b"".join(payload for _key, payload in sorted(entries))
        framed = b"tree " + str(len(content)).encode() + b"\x00" + content
        return hashlib.sha1(framed, usedforsecurity=False).hexdigest()

    return digest(root)


def _machine_capd_tree(checkout: Path) -> tuple[str, str]:
    checkout = require_canonical_absolute_path(checkout, "V2 role10 CAPD checkout")
    head_raw = read_pinned_regular_bytes(checkout / ".git/HEAD")
    require(re.fullmatch(rb"[0-9a-f]{40}\n", head_raw), "V2 role10 CAPD detached HEAD")
    commit = head_raw[:-1].decode("ascii")
    records = _machine_read_git_index(checkout)
    index_tree = _machine_index_tree_oid(records)
    catalog, _ = _git_pack_catalog(checkout / ".git")
    kind, commit_payload = _git_read_object(checkout / ".git", commit, catalog)
    require(kind == b"commit", "V2 role10 CAPD HEAD is not commit")
    match = re.match(rb"tree ([0-9a-f]{40})\n", commit_payload)
    require(match is not None and match.group(1).decode() == index_tree, "V2 role10 CAPD commit/index tree mismatch")
    tracked = {relative for relative, _mode, _oid in records}
    expected_directories: set[str] = set()
    for relative in tracked:
        parent = PurePosixPath(relative).parent
        while parent != PurePosixPath("."):
            expected_directories.add(parent.as_posix())
            parent = parent.parent
    observed_files: set[str] = set()
    observed_directories: set[str] = set()
    pending = [checkout]
    while pending:
        directory = pending.pop()
        for entry in sorted(os.scandir(directory), key=lambda item: os.fsencode(item.name)):
            relative = Path(entry.path).relative_to(checkout).as_posix()
            if relative in {".git", "build-mp"}:
                continue
            info = entry.stat(follow_symlinks=False)
            if stat.S_ISDIR(info.st_mode):
                observed_directories.add(relative)
                pending.append(Path(entry.path))
            elif stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode):
                observed_files.add(relative)
            else:
                raise CheckError(f"V2 role10 CAPD unsupported namespace: {relative}")
    require(observed_files == tracked and observed_directories == expected_directories, "V2 role10 CAPD tracked/untracked namespace drift")
    rows: list[dict[str, Any]] = []
    for relative, git_mode, oid in records:
        target = checkout.joinpath(*PurePosixPath(relative).parts)
        if git_mode == 0o120000:
            raw, info = _machine_manifest_symlink(target, f"V2 role10 CAPD tracked link {relative}")
        else:
            raw, info = _machine_manifest_regular(target, f"V2 role10 CAPD tracked file {relative}")
            require(bool(stat.S_IMODE(info.st_mode) & 0o111) is (git_mode == 0o100755), "V2 role10 CAPD tracked mode")
        require(_machine_git_blob_sha1(raw) == oid, "V2 role10 CAPD tracked blob mismatch")
        rows.append({
            "git_blob_sha1": oid, "mode": f"{git_mode:06o}",
            "path": relative, "sha256": sha256_bytes(raw),
            "size_bytes": len(raw),
        })
    return commit, sha256_bytes(canonical_json_bytes(rows))


def _machine_nonnegative_float(value: Any, context: str) -> float:
    require(type(value) is float and math.isfinite(value) and value >= 0.0, f"{context}: finite nonnegative float")
    return value


def _machine_plan_records(
    project_root: Path,
) -> tuple[dict[str, Mapping[str, Any]], str]:
    path = _project_file(project_root, "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json")
    raw = read_pinned_regular_bytes(path)
    payload = load_strict_json_object_from_bytes(raw, path)
    slabs = payload.get("slabs")
    require(type(slabs) is list, "V2 role10 L1 plan slabs")
    records: dict[str, Mapping[str, Any]] = {}
    for record in slabs:
        require(type(record) is dict and type(record.get("slab_id")) is str, "V2 role10 L1 plan record")
        require(record["slab_id"] not in records, "V2 role10 duplicate L1 slab")
        records[record["slab_id"]] = record
    require(all(slab in records for slab in ("S000", "S025", "S050")), "V2 role10 public plan slabs")
    return records, sha256_bytes(raw)


def _machine_static_resource_argv(
    row: Mapping[str, Any],
    bindings: Mapping[str, Any],
    plan: Mapping[str, Any],
) -> list[str]:
    return [
        bindings["interpreter"]["invocation_path"], bindings["evaluator"]["path"],
        "--slab-id", row["slab_id"], "--precision-bits", str(row["precision_bits"]),
        "--epsilon-lower", plan["epsilon_lower"], "--epsilon-upper", plan["epsilon_upper"],
        "--matrix-id", bindings["calibration_binding"]["matrix_id"],
        "--freeze-sha256", bindings["calibration_binding"]["nonfreeze_sha256"],
        "--run-config-sha256", bindings["calibration_binding"]["nonrunconfig_sha256"],
        "--plan-record-sha256", sha256_bytes(canonical_json_bytes(plan)),
        "--max-depth", "24", "--max-nodes-per-tree", "250000",
        "--max-nodes-per-cell", "1000000", "--output", row["output"],
    ]


def _machine_validate_static_resource_run(
    row: Any,
    *,
    identity: tuple[int, str, int],
    bindings: Mapping[str, Any],
    plan_records: Mapping[str, Mapping[str, Any]],
    temporary_root: Path,
    label: str,
    context: str,
) -> int:
    exact_keys(row, STATIC_RESOURCE_RUN_KEYS, context)
    bits, slab, replica = identity
    require((row["precision_bits"], row["slab_id"], row["replica"]) == identity and row["label"] == label, f"{context}: identity/order")
    for key in ("precision_bits", "replica", "returncode", "peak_rss_kib", "output_bytes", "stdout_bytes", "stderr_bytes"):
        require_exact_int(row[key], f"{context}.{key}", minimum=0)
    for key in ("elapsed_seconds", "user_cpu_seconds", "system_cpu_seconds"):
        _machine_nonnegative_float(row[key], f"{context}.{key}")
    require(bits in PRECISIONS and slab in {"S000", "S025", "S050"}, f"{context}: public cell")
    require(
        row["returncode"] == 0 and row["peak_rss_kib"] > 0 and row["output_bytes"] > 0
        and row["stdout_exact_status_line"] == "evaluator_status=STATIC_CELL_CERTIFIED"
        and row["evaluator_status"] == "STATIC_CELL_CERTIFIED"
        and row["stderr_empty"] is True and row["stderr_bytes"] == 0,
        f"{context}: successful static calibration ABI",
    )
    for key in ("output_sha256", "stdout_sha256", "stderr_sha256"):
        _exact_sha(row[key], f"{context}.{key}")
    expected_stdout = b"evaluator_status=STATIC_CELL_CERTIFIED\n"
    require(
        row["stdout_bytes"] == len(expected_stdout)
        and row["stdout_sha256"] == sha256_bytes(expected_stdout)
        and row["stderr_sha256"] == MACHINE_EMPTY_SHA256,
        f"{context}: transcript binding",
    )
    for key in ("scientific_status", "component_status", "milestone_status", "theorem_status", "final_status"):
        require(row[key] is None, f"{context}: overclaim {key}")
    for key in ("output", "stdout", "stderr"):
        path = require_canonical_absolute_path(row[key], f"{context}.{key}")
        try:
            path.relative_to(temporary_root)
        except ValueError as error:
            raise CheckError(f"{context}.{key}: escapes inert /tmp evidence") from error
    require(row["argv"] == _machine_static_resource_argv(row, bindings, plan_records[slab]), f"{context}: exact argv")
    return row["peak_rss_kib"] * 1024


def _machine_validate_static_resource(
    project_root: Path,
    raw: bytes,
    machine: Mapping[str, Any],
) -> dict[str, int]:
    pseudo = Path("/V2_STATIC_RESOURCE.json")
    payload = load_strict_json_object_from_bytes(raw, pseudo)
    require(raw == canonical_json_bytes(payload), "V2 role10 static resource CJ_COMPACT_V1")
    exact_keys(payload, STATIC_RESOURCE_KEYS, "V2 role10 static resource")
    require(
        payload["schema_version"] == 1 and type(payload["schema_version"]) is int
        and payload["protocol_id"] == PROTOCOL_ID
        and payload["artifact_role"] == "TEMP_PUBLIC_STATIC_RSS_CALIBRATION"
        and payload["scope"] == "PUBLIC_S0_RESOURCE_CALIBRATION_ONLY"
        and payload["production_authorized"] is False
        and payload["scientific_licensing_enabled"] is False
        and payload["claim_boundary"] == "resource telemetry on already-public S000/S025/S050 at 128/256 only; no held-out/all-slab evaluation, no freeze, no scientific promotion"
        and payload["project_root"] == str(project_root),
        "V2 role10 static resource identity",
    )
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[key] is None, f"V2 role10 static resource overclaim {key}")
    temporary_root = require_canonical_absolute_path(payload["temporary_root"], "V2 role10 static resource temp")
    require(temporary_root.parts[:2] == ("/", "tmp"), "V2 role10 static resource inert /tmp origin")
    expected_env = {
        "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC",
        "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1",
    }
    exact_keys(payload["execution_environment"], STATIC_RESOURCE_ENV_KEYS, "V2 role10 static resource env")
    require_json_exact(payload["execution_environment"], expected_env, "V2 role10 static resource env")
    bindings = exact_keys(payload["bindings"], STATIC_RESOURCE_BINDING_KEYS, "V2 role10 static bindings")
    for value, keys, context in (
        (bindings["evaluator"], STATIC_RESOURCE_EVALUATOR_KEYS, "evaluator"),
        (bindings["interpreter"], STATIC_RESOURCE_INTERPRETER_KEYS, "interpreter"),
        (bindings["python_flint"], STATIC_RESOURCE_FLINT_KEYS, "python-flint"),
        (bindings["plan"], STATIC_RESOURCE_PLAN_KEYS, "plan"),
        (bindings["calibration_binding"], STATIC_RESOURCE_CALIBRATION_KEYS, "calibration"),
    ):
        exact_keys(value, keys, f"V2 role10 static {context}")
    evaluator_path = _project_file(project_root, "scripts/evaluate_r401_val_l3_a1_static_cell.py")
    evaluator_pinned = _read_pinned_regular_snapshot(
        evaluator_path, context="V2 role10 static evaluator"
    )
    evaluator_raw, evaluator_info = evaluator_pinned.raw, evaluator_pinned.info
    require(
        bindings["evaluator"] == {
            "path": str(evaluator_path), "sha256": sha256_bytes(evaluator_raw),
            "size_bytes": len(evaluator_raw),
            "mode": f"{stat.S_IMODE(evaluator_info.st_mode):04o}",
        },
        "V2 role10 static evaluator binding",
    )
    python = machine["python_arb"]
    interpreter_raw, _interpreter_info, resolved = _machine_external_snapshot(bindings["interpreter"]["invocation_path"], "V2 role10 static interpreter")
    require(bindings["interpreter"] == {
        "invocation_path": python["executable_path"], "resolved_path": str(resolved),
        "sha256": python["executable_sha256"], "size_bytes": len(interpreter_raw),
        "version": python["python_version"],
    }, "V2 role10 static interpreter cross-binding")
    flint = bindings["python_flint"]
    module_raw, _module_info, module_path = _machine_external_snapshot(flint["module_path"], "V2 role10 flint module")
    del module_raw
    record_raw, _record_info, record_path = _machine_external_snapshot(flint["record_path"], "V2 role10 flint RECORD")
    site_packages = record_path.parents[1]
    count, root = _machine_recompute_flint_manifest(str(record_path), record_raw)
    require(
        record_path.name == "RECORD" and record_path.parent.name == "python_flint-0.9.0.dist-info"
        and module_path == site_packages / "flint/__init__.py"
        and flint["version"] == python["python_flint_version"]
        and flint["flint_version"] == python["flint_version"]
        and flint["record_sha256"] == sha256_bytes(record_raw) == python["python_flint_record_sha256"]
        and flint["installed_record_file_count"] == count
        and flint["installed_manifest_sha256"] == root == python["python_flint_installed_manifest_root_sha256"]
        and flint["arb_extension_path"] == python["arb_extension"]["path"]
        and flint["arb_extension_sha256"] == python["arb_extension"]["sha256"],
        "V2 role10 static Python-flint cross-binding",
    )
    plans, plan_sha = _machine_plan_records(project_root)
    require(bindings["plan"] == {
        "path": str(_project_file(project_root, "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json")),
        "sha256": plan_sha, "public_slab_ids": ["S000", "S025", "S050"],
    }, "V2 role10 static plan binding")
    for key in STATIC_RESOURCE_CALIBRATION_KEYS:
        _exact_sha(bindings["calibration_binding"][key], f"V2 role10 calibration.{key}")
    require(bindings["calibration_binding"]["matrix_id"] == _formal_matrix_id(), "V2 role10 calibration matrix")
    public = [(bits, slab) for bits in PRECISIONS for slab in ("S000", "S025", "S050")]
    sequential = payload["sequential_runs"]
    require(type(sequential) is list and len(sequential) == 6, "V2 role10 six static sequential runs")
    peaks = [
        _machine_validate_static_resource_run(
            row, identity=(bits, slab, 0), bindings=bindings,
            plan_records=plans, temporary_root=temporary_root,
            label=f"{bits}_{slab}", context=f"V2 role10 static sequential[{index}]",
        )
        for index, (row, (bits, slab)) in enumerate(zip(sequential, public, strict=True))
    ]
    stress = [*public, (256, "S025"), (256, "S050")]
    schedule = payload["concurrent_schedule"]
    require(type(schedule) is list and len(schedule) == 8, "V2 role10 static concurrent schedule")
    for row, (bits, slab) in zip(schedule, stress, strict=True):
        exact_keys(row, STATIC_RESOURCE_SCHEDULE_KEYS, "V2 role10 static schedule row")
        require_json_exact(row, {"precision_bits": bits, "slab_id": slab}, "V2 role10 static schedule row")
    concurrent = payload["concurrent_runs"]
    require(type(concurrent) is list and len(concurrent) == 8, "V2 role10 eight static concurrent runs")
    seen: dict[tuple[int, str], int] = {}
    for index, (row, (bits, slab)) in enumerate(zip(concurrent, stress, strict=True)):
        replica = seen.get((bits, slab), 0)
        seen[(bits, slab)] = replica + 1
        peaks.append(_machine_validate_static_resource_run(
            row, identity=(bits, slab, replica), bindings=bindings,
            plan_records=plans, temporary_root=temporary_root,
            label=f"{index:02d}_{bits}_{slab}_r{replica}",
            context=f"V2 role10 static concurrent[{index}]",
        ))
    measurement = exact_keys(payload["measurement"], STATIC_RESOURCE_MEASUREMENT_KEYS, "V2 role10 static measurement")
    require(
        measurement["method"] == "os.wait4(pid,0/WNOHANG).rusage.ru_maxrss on Linux"
        and measurement["ru_maxrss_unit"] == "KiB"
        and measurement["bytes_per_kib"] == 1024
        and measurement["cgroup_usage_path"] == "/sys/fs/cgroup/memory/memory.usage_in_bytes"
        and measurement["cgroup_limit_path"] == "/sys/fs/cgroup/memory/memory.limit_in_bytes"
        and measurement["cgroup_limit_bytes"] == machine["machine_requirements"]["memory_limit_bytes"]
        and type(measurement["sample_interval_seconds"]) is float
        and measurement["sample_interval_seconds"] == 0.05,
        "V2 role10 static measurement ABI",
    )
    baseline_samples = measurement["baseline_samples_bytes"]
    concurrent_samples = measurement["concurrent_samples_bytes"]
    require(type(baseline_samples) is list and len(baseline_samples) == 21 and type(concurrent_samples) is list and concurrent_samples, "V2 role10 static sample arrays")
    require(all(type(value) is int and value > 0 for value in [*baseline_samples, *concurrent_samples]), "V2 role10 static sample values")
    baseline = max(baseline_samples)
    peak = max(peaks)
    require(measurement["baseline_conservative_bytes"] == baseline and measurement["concurrent_peak_bytes"] == max(concurrent_samples), "V2 role10 static sample aggregation")
    admission = exact_keys(payload["admission"], STATIC_RESOURCE_ADMISSION_KEYS, "V2 role10 static admission")
    lhs = baseline + 8 * peak + machine["machine_requirements"]["reserve_bytes"]
    require(admission == {
        "workers": 8, "representative_peak_rss_bytes": peak,
        "idle_baseline_bytes": baseline,
        "reserve_bytes": machine["machine_requirements"]["reserve_bytes"],
        "admission_limit_bytes": machine["machine_requirements"]["memory_admission_limit_bytes"],
        "lhs_bytes": lhs,
        "headroom_bytes": machine["machine_requirements"]["memory_admission_limit_bytes"] - lhs,
        "formula": "idle_baseline_bytes + workers * representative_peak_rss_bytes + reserve_bytes <= admission_limit_bytes",
        "passes": lhs <= machine["machine_requirements"]["memory_admission_limit_bytes"],
    }, "V2 role10 static admission arithmetic")
    return {"baseline_bytes": baseline, "peak_rss_bytes": peak}


def _machine_branch_resource_argv(
    binary: str, bits: int, plan: Mapping[str, Any]
) -> list[str]:
    center, radii = plan["center"], plan["root_radii"]

    def endpoint(name: str, sign: int) -> str:
        return format(Decimal(center[name]) + sign * Decimal(radii[name]), "f")

    return [
        binary, str(bits), plan["epsilon_lower"], plan["epsilon_upper"],
        endpoint("q_slow", -1), endpoint("q_slow", 1),
        endpoint("q_fast", -1), endpoint("q_fast", 1),
        endpoint("p_slow", -1), endpoint("p_slow", 1),
        endpoint("period", -1), endpoint("period", 1),
    ]


def _machine_validate_branch_resource(
    project_root: Path, raw: bytes, machine: Mapping[str, Any]
) -> dict[str, int]:
    path = Path("/V2_BRANCH_RESOURCE.json")
    payload = load_strict_json_object_from_bytes(raw, path)
    pretty = (json.dumps(payload, sort_keys=True, ensure_ascii=False, allow_nan=False, indent=2) + "\n").encode()
    require(raw == pretty, "V2 role10 branch resource exact pretty JSON")
    exact_keys(payload, BRANCH_RESOURCE_KEYS, "V2 role10 branch resource")
    require(payload["scope"] == "REPRESENTATIVE_S0_CALIBRATION_ONLY", "V2 role10 branch resource scope")
    for key in ("scientific_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[key] is None, f"V2 role10 branch resource overclaim {key}")
    binary = payload["binary"]
    require_canonical_absolute_path(binary, "V2 role10 branch resource binary")
    require(payload["binary_sha256"] == machine["branch_binary"]["sha256"], "V2 role10 branch resource binary binding")
    require_exact_int(payload["cgroup_limit_bytes"], "V2 role10 branch cgroup", expected=machine["machine_requirements"]["memory_limit_bytes"])
    for name in ("baseline_samples_bytes", "post_samples_bytes"):
        values = payload[name]
        require(type(values) is list and len(values) == 21 and all(type(value) is int and value > 0 for value in values), f"V2 role10 branch {name}")
    baseline = max(payload["baseline_samples_bytes"])
    require(payload["baseline_conservative_bytes"] == baseline, "V2 role10 branch baseline aggregation")
    plans, _plan_sha = _machine_plan_records(project_root)
    public = [(bits, slab) for bits in PRECISIONS for slab in ("S000", "S025", "S050")]
    results = payload["results"]
    require(type(results) is list and len(results) == 6 and payload["task_count"] == 6, "V2 role10 branch six public runs")
    peaks: list[int] = []
    for index, (row, (bits, slab)) in enumerate(zip(results, public, strict=True)):
        context = f"V2 role10 branch run[{index}]"
        exact_keys(row, BRANCH_RESOURCE_RUN_KEYS, context)
        require(row["precision_bits"] == bits and row["slab_id"] == slab, f"{context}: identity/order")
        for key in ("precision_bits", "argv_count", "returncode", "peak_rss_kib", "stdout_bytes", "stderr_bytes"):
            require_exact_int(row[key], f"{context}.{key}", minimum=0)
        for key in ("elapsed_seconds", "user_cpu_seconds", "system_cpu_seconds"):
            _machine_nonnegative_float(row[key], f"{context}.{key}")
        require(
            row["argv_count"] == 12
            and row["argv"] == _machine_branch_resource_argv(binary, bits, plans[slab])
            and row["returncode"] == 0 and row["peak_rss_kib"] > 0
            and row["stdout_bytes"] > 0 and row["stderr_bytes"] == 0
            and row["stderr_sha256"] == MACHINE_EMPTY_SHA256
            and row["abi_verified"] is True
            and row["terminal_abi_value"] == "BRANCH_CELL_CERTIFIED",
            f"{context}: ABI/resource result",
        )
        _exact_sha(row["stdout_sha256"], f"{context}.stdout")
        peaks.append(row["peak_rss_kib"] * 1024)
    peak = max(peaks)
    require(payload["per_process_peak_rss_max_kib"] * 1024 == peak, "V2 role10 branch peak aggregation")
    require(
        type(payload["sampled_concurrent_peak_bytes"]) is int
        and payload["sampled_concurrent_peak_bytes"] > 0
        and type(payload["sampled_concurrent_increment_bytes"]) is int
        and payload["sampled_concurrent_increment_bytes"] >= 0
        and payload["sampled_concurrent_increment_bytes"] == payload["sampled_concurrent_peak_bytes"] - baseline,
        "V2 role10 branch concurrent aggregation",
    )
    admission = exact_keys(payload["admission"], BRANCH_RESOURCE_ADMISSION_KEYS, "V2 role10 branch admission")
    lhs = baseline + 6 * peak + machine["machine_requirements"]["reserve_bytes"]
    require(admission == {
        "baseline_bytes": baseline, "peak_rss_bytes": peak, "workers": 6,
        "reserve_bytes": machine["machine_requirements"]["reserve_bytes"],
        "limit_bytes": machine["machine_requirements"]["memory_admission_limit_bytes"],
        "lhs_bytes": lhs,
        "headroom_bytes": machine["machine_requirements"]["memory_admission_limit_bytes"] - lhs,
        "formula": "baseline + 6*peak_rss + 8GiB <= 48GiB",
        "passes": lhs <= machine["machine_requirements"]["memory_admission_limit_bytes"],
    }, "V2 role10 branch admission arithmetic")
    return {"baseline_bytes": baseline, "peak_rss_bytes": peak}


def _validate_machine_freeze(project_root: Path, machine: Any, roles: Mapping[str, Mapping[str, str]]) -> None:
    require(type(machine) is dict, "V2 role10: object required")
    exact_keys(machine, MACHINE_FREEZE_KEYS, "V2 role10")
    require_exact_int(machine["schema_version"], "V2 role10.schema_version", expected=1)
    require(
        machine["protocol_id"] == PROTOCOL_ID
        and machine["artifact_role"] == "MACHINE_FREEZE"
        and machine["status"] == "FROZEN_FOR_PRODUCTION"
        and machine["authority"] == "MACHINE_ADMISSION_ONLY"
        and machine["scientific_licensing_enabled"] is True
        and machine["production_authorized"] is False
        and machine["claim_boundary"] == MACHINE_CLAIM_BOUNDARY,
        "V2 role10 identity/authority mismatch",
    )
    _require_null_program_statuses(machine, "V2 role10")
    capture = machine["capture"]
    exact_keys(capture, MACHINE_CAPTURE_KEYS, "V2 role10.capture")
    timestamp = capture["captured_at_utc"]
    require(type(timestamp) is str and MACHINE_TIMESTAMP.fullmatch(timestamp), "V2 role10 timestamp")
    try:
        captured_at = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        uptime = Decimal(Path("/proc/uptime").read_text(encoding="ascii").split()[0])
    except (ValueError, OSError, UnicodeError, IndexError, ArithmeticError) as error:
        raise CheckError("V2 role10 live boot/timestamp evidence unavailable") from error
    age = (datetime.now(timezone.utc) - captured_at).total_seconds()
    require(-300.0 <= age <= float(uptime) + 300.0, "V2 role10 capture is outside live boot window")
    require(capture["capture_tool_path"] == roles["scheduler"]["path"] and capture["capture_tool_sha256"] == roles["scheduler"]["sha256"], "V2 role10 scheduler binding")
    require(capture["boot_id_sha256"] == sha256_bytes(_machine_boot_id_bytes()), "V2 role10 live boot ID binding")
    require_json_exact(machine["machine_requirements"], _formal_machine_requirements(), "V2 role10 requirements")
    observations = machine["machine_observations"]
    exact_keys(observations, MACHINE_OBSERVATION_KEYS, "V2 role10 observations")
    for key, value in observations.items():
        require_exact_int(value, f"V2 role10 observations.{key}", minimum=1)
    require(
        observations["logical_cpu_count"] == machine["machine_requirements"]["logical_cpu_count"]
        and observations["memory_limit_bytes"] == machine["machine_requirements"]["memory_limit_bytes"]
        and len(os.sched_getaffinity(0)) == machine["machine_requirements"]["logical_cpu_count"],
        "V2 role10 observation/requirement/live CPU mismatch",
    )
    try:
        live_memory_limit = int(Path("/sys/fs/cgroup/memory/memory.limit_in_bytes").read_text(encoding="ascii").strip())
    except (OSError, UnicodeError, ValueError) as error:
        raise CheckError("V2 role10 live cgroup memory limit unavailable") from error
    require(live_memory_limit == machine["machine_requirements"]["memory_limit_bytes"], "V2 role10 live cgroup memory limit")

    python = machine["python_arb"]
    exact_keys(python, MACHINE_PYTHON_KEYS, "V2 role10 python_arb")
    require(
        python["implementation"] == "CPython"
        and python["python_version"] == MACHINE_PYTHON_VERSION
        and python["python_flint_version"] == "0.9.0"
        and python["flint_version"] == "3.6.0"
        and python["arb_version"] == "FLINT-3.6.0"
        and python["conda_manifest_algorithm"] == MACHINE_CONDA_ALGORITHM
        and python["python_flint_record_sha256"] == MACHINE_FLINT_RECORD_SHA256
        and python["python_flint_installed_manifest_root_sha256"] == MACHINE_FLINT_MANIFEST_SHA256,
        "V2 role10 Python-Arb literal identity",
    )
    for key in ("executable_sha256", "conda_installed_manifest_root_sha256", "python_flint_record_sha256", "python_flint_installed_manifest_root_sha256"):
        _exact_sha(python[key], f"V2 role10 python.{key}")
    python_raw, _python_info, _python_resolved = _machine_external_snapshot(python["executable_path"], "V2 role10 Python")
    require(sha256_bytes(python_raw) == python["executable_sha256"], "V2 role10 Python live hash")
    conda_count, conda_root = _machine_recompute_conda_manifest(python["executable_path"])
    require_exact_int(python["conda_manifest_file_count"], "V2 role10 conda count", expected=conda_count, minimum=1)
    require(python["conda_installed_manifest_root_sha256"] == conda_root, "V2 role10 live conda manifest root")
    _validate_machine_file_binding(python["arb_extension"], "V2 role10 Arb extension")
    _validate_machine_file_binding(python["fmpq_extension"], "V2 role10 fmpq extension")
    require(type(python["bundled_libraries"]) is list and len(python["bundled_libraries"]) == 3, "V2 role10 Python exact bundled libraries")

    capd = machine["capd"]
    exact_keys(capd, MACHINE_CAPD_KEYS, "V2 role10 CAPD")
    checkout = require_canonical_absolute_path(capd["checkout_path"], "V2 role10 CAPD checkout")
    require(
        type(capd["commit"]) is str and re.fullmatch(r"[0-9a-f]{40}", capd["commit"])
        and capd["clean"] is True
        and capd["tree_algorithm"] == MACHINE_CAPD_TREE_ALGORITHM,
        "V2 role10 CAPD commit/clean/algorithm",
    )
    for key in ("tree_sha256", "cmake_cache_sha256", "config_sha256", "raw_flags_sha256"):
        _exact_sha(capd[key], f"V2 role10 CAPD.{key}")
    live_commit, live_tree = _machine_capd_tree(checkout)
    require(capd["commit"] == live_commit and capd["tree_sha256"] == live_tree, "V2 role10 live CAPD detached tree")
    require(type(capd["raw_flags"]) is str and capd["raw_flags"].endswith("\n") and sha256_bytes(capd["raw_flags"].encode()) == capd["raw_flags_sha256"], "V2 role10 CAPD flags")
    try:
        capd_tokens = shlex.split(capd["raw_flags"])
    except ValueError as error:
        raise CheckError("V2 role10 CAPD flags cannot be tokenized") from error
    expected_capd_tokens = [
        "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
        "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
        "-DFILIB_HAVE_SSE", f"-I{checkout}/capdDynSys/include",
        f"-I{checkout}/capdAlg/include", f"-I{checkout}/capdAux/include",
        f"-I{checkout}/capdExt/include", f"-I{checkout}/capdExt/filibsrc",
        f"-L{checkout}/build-mp", f"-L{checkout}/build-mp/capdExt/filibsrc",
        "-lcapd", "-lfilib", "-lmpfr", "-lgmp",
    ]
    require(capd_tokens == expected_capd_tokens, "V2 role10 CAPD ordered flags")
    for path_key, hash_key in (("cmake_cache_path", "cmake_cache_sha256"), ("config_path", "config_sha256")):
        raw, _info, resolved = _machine_external_snapshot(capd[path_key], f"V2 role10 {path_key}")
        require(sha256_bytes(raw) == capd[hash_key], f"V2 role10 {path_key} hash")
        expected = checkout / ("build-mp/CMakeCache.txt" if path_key == "cmake_cache_path" else "build-mp/bin/capd-config")
        require(resolved == expected, f"V2 role10 {path_key} layout")
    _validate_machine_file_binding(capd["libcapd"], "V2 role10 libcapd", allow_null_build=True)
    _validate_machine_file_binding(capd["libfilib"], "V2 role10 libfilib", allow_null_build=True)
    require(
        capd["libcapd"]["path"] == str(checkout / "build-mp/libcapd.a")
        and capd["libfilib"]["path"] == str(checkout / "build-mp/capdExt/filibsrc/libfilib.a"),
        "V2 role10 CAPD archive layout",
    )

    branch = machine["branch_binary"]
    exact_keys(branch, MACHINE_BRANCH_BINARY_KEYS, "V2 role10 branch binary")
    require(branch["path"] == roles["branch_evaluator_binary"]["path"] and branch["sha256"] == roles["branch_evaluator_binary"]["sha256"] and branch["source_path"] == roles["branch_evaluator_source"]["path"] and branch["source_sha256"] == roles["branch_evaluator_source"]["sha256"], "V2 role10 branch role binding")
    binary_pinned = _read_pinned_regular_snapshot(
        _project_file(project_root, branch["path"]),
        context="V2 role10 branch binary",
    )
    binary_raw = binary_pinned.raw
    source_raw = read_pinned_regular_bytes(_project_file(project_root, branch["source_path"]))
    require(sha256_bytes(binary_raw) == branch["sha256"] == branch["elf_sha256"] and sha256_bytes(source_raw) == branch["source_sha256"], "V2 role10 branch live bytes")
    require_exact_int(branch["size_bytes"], "V2 role10 branch size", expected=len(binary_raw))
    require(type(branch["executable_mode"]) is int and branch["executable_mode"] == stat.S_IMODE(binary_pinned.info.st_mode), "V2 role10 branch mode")
    live_build_id, live_needed, live_soname = _machine_elf_metadata(binary_raw, "V2 role10 persistent branch binary")
    require(
        branch["build_id"] == live_build_id
        and live_soname is None
        and branch["dt_needed"] == live_needed == MACHINE_DT_NEEDED
        and branch["dt_needed_sha256"] == sha256_bytes(canonical_json_bytes(live_needed)),
        "V2 role10 branch live ELF metadata",
    )

    compiler = machine["compiler"]
    exact_keys(compiler, MACHINE_COMPILER_KEYS, "V2 role10 compiler")
    compiler_raw, _compiler_info, _compiler_resolved = _machine_external_snapshot(compiler["executable_path"], "V2 role10 compiler path")
    require(sha256_bytes(compiler_raw) == compiler["executable_sha256"] and compiler["version"] == MACHINE_COMPILER_VERSION, "V2 role10 compiler identity")
    recipe = compiler["build_recipe"]
    exact_keys(recipe, MACHINE_BUILD_RECIPE_KEYS, "V2 role10 build recipe")
    expected_template = [
        compiler["executable_path"], "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(_project_file(project_root, branch["source_path"])), *capd_tokens,
        "-o", MACHINE_STAGING_TOKEN,
    ]
    require(
        recipe["cwd"] == str(project_root) and recipe["umask"] == "0022"
        and recipe["environment"] == MACHINE_BUILD_ENVIRONMENT
        and recipe["staging_output_token"] == MACHINE_STAGING_TOKEN
        and recipe["argv_template"] == expected_template,
        "V2 role10 build recipe context/argv",
    )
    require(recipe["argv_template_sha256"] == sha256_bytes(canonical_json_bytes(recipe["argv_template"])), "V2 role10 build recipe hash")
    receipt = compiler["fresh_rebuild_receipt"]
    exact_keys(receipt, MACHINE_REBUILD_KEYS, "V2 role10 rebuild receipt")
    staging_dir = require_canonical_absolute_path(receipt["staging_directory"], "V2 role10 staging directory")
    staging_output = require_canonical_absolute_path(receipt["staging_output_path"], "V2 role10 staging output")
    require(
        staging_dir.parent == Path("/tmp")
        and staging_output.parent == staging_dir
        and staging_output.name == Path(branch["path"]).name
        and receipt["cwd"] == recipe["cwd"]
        and receipt["environment"] == recipe["environment"]
        and receipt["umask"] == recipe["umask"]
        and receipt["argv"] == [*expected_template[:-1], str(staging_output)]
        and receipt["return_code"] == 0 and receipt["shell_used"] is False,
        "V2 role10 rebuild context/private argv",
    )
    require(receipt["argv_sha256"] == sha256_bytes(canonical_json_bytes(receipt["argv"])) and receipt["stdout_sha256"] == sha256_bytes(receipt["stdout"].encode()) and receipt["stderr_sha256"] == sha256_bytes(receipt["stderr"].encode()), "V2 role10 rebuild transcript hash")
    require(
        receipt["stdout"] == "" and receipt["stderr"] == ""
        and receipt["stdout_sha256"] == receipt["stderr_sha256"] == MACHINE_EMPTY_SHA256
        and receipt["output_sha256"] == branch["sha256"]
        and receipt["output_size_bytes"] == len(binary_raw)
        and receipt["output_mode"] == branch["executable_mode"] == 0o755
        and receipt["output_build_id"] == live_build_id
        and receipt["output_dt_needed"] == live_needed
        and receipt["output_dt_needed_sha256"] == sha256_bytes(canonical_json_bytes(live_needed))
        and receipt["output_soname"] is None,
        "V2 role10 rebuild output/ELF transcript",
    )
    transfer = compiler["transfer_evidence"]
    exact_keys(transfer, MACHINE_TRANSFER_KEYS, "V2 role10 transfer")
    for key in ("staging_output_sha256", "branch_calibration_binary_sha256", "persistent_before_sha256", "persistent_after_sha256"):
        require(transfer[key] == branch["sha256"], f"V2 role10 transfer.{key}")
    binary_info = binary_pinned.info
    require(
        all(transfer[key] == len(binary_raw) for key in ("staging_output_size_bytes", "persistent_before_size_bytes", "persistent_after_size_bytes"))
        and all(transfer[key] == branch["executable_mode"] for key in ("staging_output_mode", "persistent_before_mode", "persistent_after_mode"))
        and transfer["persistent_before_device_id"] == binary_info.st_dev
        and transfer["persistent_after_device_id"] == binary_info.st_dev
        and transfer["persistent_before_inode"] == binary_info.st_ino
        and transfer["persistent_after_inode"] == binary_info.st_ino
        and transfer["byte_for_byte_equal"] is True
        and transfer["persistent_identity_unchanged"] is True
        and transfer["persistent_overwrite_performed"] is False,
        "V2 role10 no-overwrite transfer/live inode",
    )

    runtime = machine["runtime_libraries"]
    exact_keys(runtime, {"python_bundled", "capd_system"}, "V2 role10 runtime")
    for domain, sonames in (("python_bundled", MACHINE_PYTHON_BUNDLED_SONAMES), ("capd_system", MACHINE_CAPD_SYSTEM_SONAMES)):
        require(type(runtime[domain]) is list and len(runtime[domain]) == len(sonames), f"V2 role10 runtime {domain}")
        paths: list[str] = []
        for index, (row, soname) in enumerate(zip(runtime[domain], sonames, strict=True)):
            exact_keys(row, MACHINE_RUNTIME_ROW_KEYS, f"V2 role10 runtime {domain}[{index}]")
            raw, info, _resolved = _machine_external_snapshot(row["path"], f"V2 role10 runtime {domain}[{index}]")
            build_id, _needed, live_soname = _machine_elf_metadata(raw, f"V2 role10 runtime {domain}[{index}]")
            require(
                row["soname"] == soname == live_soname
                and row["sha256"] == sha256_bytes(raw)
                and row["size_bytes"] == len(raw)
                and row["mode"] == stat.S_IMODE(info.st_mode)
                and row["build_id"] == build_id,
                f"V2 role10 runtime live ELF binding {domain}[{index}]",
            )
            paths.append(row["path"])
        require(len(paths) == len(set(paths)), f"V2 role10 runtime duplicate paths {domain}")
    require_json_exact(python["bundled_libraries"], runtime["python_bundled"], "V2 role10 duplicate Python runtime")
    require(branch["runtime_libraries_sha256"] == sha256_bytes(canonical_json_bytes(runtime)), "V2 role10 runtime root")

    resource = machine["resource_evidence"]
    exact_keys(resource, MACHINE_RESOURCE_KEYS, "V2 role10 resource evidence")
    for stem in ("static", "branch"):
        raw_text = resource[f"{stem}_payload_raw_utf8"]
        require(type(raw_text) is str and "\x00" not in raw_text, f"V2 role10 {stem} resource UTF-8")
        require(resource[f"{stem}_payload_sha256"] == sha256_bytes(raw_text.encode()), f"V2 role10 {stem} resource hash")
        load_strict_json_object_from_bytes(raw_text.encode(), Path(f"/{stem}_resource.json"))
    require(resource["persistent_binary_sha256"] == branch["sha256"], "V2 role10 resource binary")
    static_metrics = _machine_validate_static_resource(project_root, resource["static_payload_raw_utf8"].encode(), machine)
    branch_metrics = _machine_validate_branch_resource(project_root, resource["branch_payload_raw_utf8"].encode(), machine)
    baseline = max(static_metrics["baseline_bytes"], branch_metrics["baseline_bytes"])
    require(
        observations["idle_baseline_rss_bytes"] == baseline
        and observations["representative_static_peak_rss_bytes"] == static_metrics["peak_rss_bytes"]
        and observations["representative_branch_peak_rss_bytes"] == branch_metrics["peak_rss_bytes"],
        "V2 role10 observations/resource replay mismatch",
    )
    admission = machine["resource_admission"]
    exact_keys(admission, MACHINE_ADMISSION_KEYS, "V2 role10 admission")
    requirements = machine["machine_requirements"]
    static_required = baseline + requirements["static_workers"] * static_metrics["peak_rss_bytes"] + requirements["reserve_bytes"]
    branch_required = baseline + requirements["branch_workers"] * branch_metrics["peak_rss_bytes"] + requirements["reserve_bytes"]
    require(admission == {
        "static_required_bytes": static_required, "branch_required_bytes": branch_required,
        "admitted_required_bytes": max(static_required, branch_required),
        "admission_limit_bytes": requirements["memory_admission_limit_bytes"],
        "static_inequality_passed": static_required <= requirements["memory_admission_limit_bytes"],
        "branch_inequality_passed": branch_required <= requirements["memory_admission_limit_bytes"],
        "storage_launch_passed": observations["result_parent_free_bytes"] >= requirements["launch_free_bytes"],
    } and admission["static_inequality_passed"] is True and admission["branch_inequality_passed"] is True and admission["storage_launch_passed"] is True, "V2 role10 admission arithmetic/nonpass")
    filesystem = machine["filesystem"]
    exact_keys(filesystem, MACHINE_FILESYSTEM_KEYS, "V2 role10 filesystem")
    result_parent = project_root / "results"
    require(filesystem["project_root"] == str(project_root) and filesystem["result_parent"] == str(result_parent) and filesystem["operational_parent"] == str(result_parent), "V2 role10 filesystem paths")
    require(filesystem["same_filesystem"] is True and filesystem["project_device_id"] == project_root.stat().st_dev and filesystem["result_device_id"] == result_parent.stat().st_dev and filesystem["operational_device_id"] == result_parent.stat().st_dev, "V2 role10 filesystem device binding")
    free = os.statvfs(result_parent)
    current_free = free.f_bavail * free.f_frsize
    require(current_free >= requirements["launch_free_bytes"], "V2 role10 live storage launch gate")
    static_raw = read_pinned_regular_bytes(
        _project_file(project_root, roles["static_evaluator"]["path"])
    )
    _plans, plan_hash = _machine_plan_records(project_root)
    require(
        roles["static_evaluator"]["sha256"] == sha256_bytes(static_raw)
        and roles["l1_final_plan"]["sha256"] == plan_hash,
        "V2 role10 static evaluator/plan 53-role cross-binding",
    )


S0_COMPATIBILITY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "replay_status", "matrix", "static_facts", "branch_facts",
    "composite_facts", "control_hashes", "role_sets", "source_protocols",
    "source_bindings", "failures", "claim_boundary", "milestone_status",
    "theorem_status", "final_status",
}
S0_CONTROL_ROLE_MAP = {
    "static_summary": "s0_static_summary", "static_manifest": "s0_static_manifest",
    "static_checker": "s0_static_checker", "branch_summary": "s0_branch_summary",
    "branch_manifest": "s0_branch_manifest", "branch_checker": "s0_branch_checker",
    "composite_summary": "s0_composite_summary", "composite_manifest": "s0_composite_manifest",
    "composite_checker": "s0_composite_checker",
}
S0_STATIC_FACTS = {
    "proof_count": 6, "node_count": 84172, "internal_count": 42074,
    "terminal_count": 42098, "unresolved_count": 0,
    "independent_interval_checks": 122300, "maximum_depth": 14,
}
S0_BRANCH_FACTS = {"raw_replay_count": 6, "manifest_file_count": 26}
S0_COMPOSITE_FACTS = {"cell_replay_count": 6, "manifest_binding_count": 18, "failure_count": 0}
S0_SOURCE_PROTOCOLS = {
    "static": "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT",
    "branch": "R401-VAL-L3-BT-S0",
    "composite": "R401-VAL-L3-S0-COMPOSITE-DRAFT",
}
S0_CLAIM_BOUNDARY = (
    "read-only compatibility replay of the sealed representative 3x2 S0 archive "
    "only; non-licensing and no evaluator dispatch; no all-slab result, theorem "
    "promotion, global orbit exclusion, trace formula, Hilbert-Polya construction, "
    "zeta-zero result, or RH claim"
)
S0_STATIC_ENTRY_KEYS = {
    "internal_count", "node_count", "path", "precision_bits", "sha256",
    "size_bytes", "slab_id", "terminal_count", "tree_content_sha256",
    "unresolved_count",
}


def _validate_s0_compatibility(
    project_root: Path,
    payload: Any,
    roles: Mapping[str, Mapping[str, Any]],
) -> None:
    require(type(payload) is dict, "V2 role13: object required")
    exact_keys(payload, S0_COMPATIBILITY_KEYS, "V2 role13")
    require_exact_int(payload["schema_version"], "V2 role13.schema_version", expected=1)
    expected_controls = {name: roles[role]["sha256"] for name, role in S0_CONTROL_ROLE_MAP.items()}
    expected_sources = {
        roles[role]["path"]: roles[role]["sha256"]
        for role in ("s0_adapter", "prefreeze_design", "checker_contract", "release_contract")
    }
    require(
        payload["protocol_id"] == "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY"
        and payload["artifact_role"] == "S0_TO_A1_COMPATIBILITY_REPLAY"
        and payload["artifact_status"] == "NON_LICENSING"
        and payload["replay_status"] == "PASS_S0_COMPATIBILITY_REPLAY"
        and payload["failures"] == []
        and payload["claim_boundary"] == S0_CLAIM_BOUNDARY,
        "V2 role13 identity/authority mismatch",
    )
    _require_null_program_statuses(payload, "V2 role13")
    require_json_exact(payload["matrix"], {"precisions": [128, 256], "slabs": ["S000", "S025", "S050"], "cell_count": 6}, "V2 role13 matrix")
    require_json_exact(payload["source_protocols"], S0_SOURCE_PROTOCOLS, "V2 role13 protocols")
    require_json_exact(payload["static_facts"], S0_STATIC_FACTS, "V2 role13 static facts")
    require_json_exact(payload["branch_facts"], S0_BRANCH_FACTS, "V2 role13 branch facts")
    require_json_exact(payload["composite_facts"], S0_COMPOSITE_FACTS, "V2 role13 composite facts")
    require_json_exact(payload["control_hashes"], expected_controls, "V2 role13 controls")
    require_json_exact(payload["source_bindings"], expected_sources, "V2 role13 sources")
    controls: dict[str, Mapping[str, Any]] = {}
    for name, role in S0_CONTROL_ROLE_MAP.items():
        raw = read_pinned_regular_bytes(_project_file(project_root, roles[role]["path"]))
        require(sha256_bytes(raw) == roles[role]["sha256"], f"V2 role13 live control changed: {name}")
        controls[name] = load_strict_json_object_from_bytes(raw, _project_file(project_root, roles[role]["path"]))
    require(
        controls["static_summary"].get("totals", {}).get("node_count") == 84172
        and controls["static_summary"].get("totals", {}).get("internal_count") == 42074
        and controls["static_summary"].get("totals", {}).get("terminal_count") == 42098
        and controls["static_summary"].get("totals", {}).get("unresolved_count") == 0
        and controls["static_checker"].get("independent_interval_checks") == 122300
        and controls["branch_checker"].get("raw_replay_count") == 6
        and controls["branch_checker"].get("manifest_file_count") == 26
        and controls["composite_checker"].get("cell_replay_count") == 6
        and controls["composite_checker"].get("manifest_binding_count") == 18
        and controls["composite_checker"].get("failures") == [],
        "V2 role13 sealed control facts mismatch",
    )
    role_sets = payload["role_sets"]
    exact_keys(role_sets, {"static_proof_entries", "branch_manifest_roles", "composite_manifest_roles", "composite_component_roles"}, "V2 role13 role sets")
    proofs = controls["static_summary"].get("proofs")
    require(type(proofs) is list and len(proofs) == 6, "V2 role13 proof list")
    require_json_exact(role_sets["static_proof_entries"], proofs, "V2 role13 proof roles")
    pairs = tuple((bits, slab) for bits in PRECISIONS for slab in ("S000", "S025", "S050"))
    for index, (entry, pair) in enumerate(zip(proofs, pairs, strict=True)):
        exact_keys(entry, S0_STATIC_ENTRY_KEYS, f"V2 role13 proof[{index}]")
        require(entry["precision_bits"] == pair[0] and entry["slab_id"] == pair[1] and entry["path"] == f"proof_{pair[0]}_{pair[1]}.json", "V2 role13 proof identity")
        _exact_sha(entry["sha256"], f"V2 role13 proof[{index}]")
        require_exact_int(entry["size_bytes"], f"V2 role13 proof[{index}].size", minimum=1)
        require(entry["node_count"] == entry["internal_count"] + entry["terminal_count"] and entry["unresolved_count"] == 0, "V2 role13 proof count conservation")
        exact_keys(entry["tree_content_sha256"], {"ANGLE", "SECTION_HIGH", "SECTION_LOW", "SECTION_WINDOW"}, f"V2 role13 proof[{index}].trees")
        for digest in entry["tree_content_sha256"].values():
            _exact_sha(digest, f"V2 role13 proof[{index}].tree")
    branch_files = controls["branch_manifest"].get("files")
    require(type(branch_files) is dict, "V2 role13 branch file map")
    prefix = f"{project_root}/"
    branch_roles = []
    for absolute in branch_files:
        require(type(absolute) is str and absolute.startswith(prefix), "V2 role13 absolute branch path")
        relative = absolute[len(prefix):]
        _safe_relative(relative)
        branch_roles.append(relative)
    require_json_exact(role_sets["branch_manifest_roles"], branch_roles, "V2 role13 branch roles")
    composite_files = controls["composite_manifest"].get("files")
    component_files = controls["composite_manifest"].get("component_files")
    require(type(composite_files) is list and type(component_files) is list, "V2 role13 composite role arrays")
    expected_composite = [{"scope": row.get("scope"), "path": row.get("path")} for row in composite_files]
    expected_components = [{"component": row.get("component"), "path": row.get("path")} for row in component_files]
    require_json_exact(role_sets["composite_manifest_roles"], expected_composite, "V2 role13 composite roles")
    require_json_exact(role_sets["composite_component_roles"], expected_components, "V2 role13 component roles")
    for row in expected_composite:
        exact_keys(row, {"scope", "path"}, "V2 role13 composite role")
        require(row["scope"] in {"ROOT", "OUTPUT"}, "V2 role13 composite scope")
        _safe_relative(row["path"])
    for row in expected_components:
        exact_keys(row, {"component", "path"}, "V2 role13 component role")
        require(row["component"] in {"static", "branch"}, "V2 role13 component identity")
        _safe_relative(row["path"])


PREFREEZE_TEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "recorded_at_utc", "repository_snapshot",
    "evidence_tool_bindings", "pre_review_input_roles", "prerequisite_bindings",
    "command_results", "test_totals", "covered_gates", "held_out_policy",
    "scientific_licensing_enabled", "production_authorized",
    "scientific_dispatch_performed", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
PREFREEZE_ROLE_ENTRY_KEYS = {"role", "path", "sha256", "size_bytes", "mode", "nlink"}
PREFREEZE_FILE_BINDING_KEYS = {"path", "sha256", "size_bytes", "mode", "nlink"}
PREFREEZE_REPOSITORY_KEYS = {
    "authority_root", "branch", "capture_commit_oid", "capture_tree_oid",
    "origin_url", "origin_main_oid", "live_remote_main_oid",
    "head_equals_origin_main", "head_equals_live_remote_main", "ahead", "behind",
    "worktree_clean_before", "worktree_clean_after",
}
PREFREEZE_COMMAND_KEYS = {
    "name", "kind", "argv", "cwd", "environment", "return_code",
    "started_at_utc", "wall_duration_ms", "stdout_utf8", "stdout_sha256",
    "stdout_size_bytes", "stderr_utf8", "stderr_sha256", "stderr_size_bytes",
    "pytest_counts", "semantic_receipt",
}
PREFREEZE_PYTEST_COUNT_KEYS = {"passed", "failed", "skipped", "xfailed", "xpassed"}
PREFREEZE_TEST_TOTAL_KEYS = PREFREEZE_PYTEST_COUNT_KEYS | {"wall_duration_ms"}
PREFREEZE_VERIFY_RECEIPT_KEYS = {"verification_status", "authority", "candidate_sha256", "size_bytes", "promotion_authorized"}
PREFREEZE_SECOND_RECEIPT_KEYS = {
    "verification_status", "authority", "source_path", "source_sha256",
    "persistent_binary_path", "persistent_before_sha256", "persistent_after_sha256",
    "persistent_before_device_id", "persistent_before_inode",
    "persistent_after_device_id", "persistent_after_inode",
    "persistent_identity_unchanged", "persistent_overwrite_performed",
    "staging_output_sha256", "staging_output_size_bytes", "staging_output_mode",
    "staging_output_removed", "byte_for_byte_equal", "scientific_evaluator_dispatched",
}
PREFREEZE_COMMAND_SPECS = (
    ("role24_machine_verify", "VERIFY_MACHINE_FREEZE"),
    ("role13_compatibility_verify", "VERIFY_S0_COMPATIBILITY"),
    ("prefreeze_focused_pytest", "PYTEST_FOCUSED"),
    ("l3_a1_modules_pytest", "PYTEST_L3_A1"),
    ("paper02_full_pytest", "PYTEST_PAPER02"),
    ("git_diff_check", "GIT_DIFF_CHECK"),
    ("second_fresh_rebuild", "SECOND_FRESH_REBUILD"),
)
PREFREEZE_TEST_RESULT_TOTAL = {
    "prefreeze_focused_pytest": "prefreeze_focused",
    "l3_a1_modules_pytest": "l3_a1_modules",
    "paper02_full_pytest": "paper02_full",
}
PREFREEZE_TOOL_ROLES = {
    "producer": "scheduler", "independent_checker": "release_builder",
    "focused_test": "test_adversarial",
}
PREFREEZE_INPUT_ROLES = tuple(item for item in INPUT_ROLES if item[0] not in {"prefreeze_tests", "prefreeze_review"})
PREFREEZE_COVERED_GATES = (
    "EXACT_51_ROLE_ORDER_AND_SAME_BYTE_SNAPSHOTS",
    "CANONICAL_ROLE10_AND_ROLE13_REPLAY",
    "SEVEN_FIXED_COMMAND_IDENTITIES",
    "BOUNDED_RAW_UTF8_TRANSCRIPT_REHASH",
    "PYTEST_SUMMARY_REPARSE_AND_ZERO_NONPASS_COUNTS",
    "CLEAN_REPOSITORY_AND_FIXED_ENVIRONMENT",
    "PROCESS_GROUP_TIMEOUT_AND_DESCENDANT_CLEANUP",
    "SECOND_REBUILD_NO_OVERWRITE_BYTE_EQUALITY",
    "STRICT_SCHEMA_TYPES_PATHS_LINKS_AND_TOCTOU_REPLAY",
    "INDEPENDENT_CHECKER_SOURCE_SEPARATION",
    "WRITE_ONCE_FIXED_DESTINATION_NOREPLACE_PUBLICATION",
)
PREFREEZE_CLEAN_ENVIRONMENT = {
    "PATH": "/root/miniconda3/bin:/usr/bin:/bin", "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8", "TZ": "UTC", "PYTHONHASHSEED": "0",
    "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1",
    "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1", "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1", "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
}
PREFREEZE_CLAIM_BOUNDARY = (
    "pre-freeze engineering test evidence only; no held-out or all-slab L3 result "
    "was read and no scientific evaluator was dispatched; no L3-A1 component, "
    "milestone, theorem, final, global tube-routing, trace-formula, Hilbert-Polya, "
    "zeta-zero, RH, or implication-toward-RH claim"
)
# This registry is mechanically copied into each independent validator after
# the final suite because passing counts have no non-cyclic artifact source.
EXPECTED_PREFREEZE_TEST_PASSED: dict[str, int] | None = {
    "prefreeze_focused": 23,
    "l3_a1_modules": 972,
    "paper02_full": 1951,
}


def _utc_timestamp(value: Any, context: str) -> datetime:
    require(type(value) is str and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", value) is not None, f"{context}: canonical UTC required")
    parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    require(parsed.strftime("%Y-%m-%dT%H:%M:%SZ") == value, f"{context}: invalid UTC")
    return parsed


def _role11_fixed_argv(project_root: Path, python_path: str) -> dict[str, list[str]]:
    root = str(project_root)
    pytest_prefix = [python_path, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no"]
    return {
        "role24_machine_verify": [python_path, f"{root}/scripts/build_r401_val_l3_a1_v2_release_provenance.py", "--verify-machine-freeze", f"{root}/research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"],
        "role13_compatibility_verify": [python_path, f"{root}/scripts/build_r401_val_l3_a1_v2_release_provenance.py", "--verify-s0-compatibility", f"{root}/research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"],
        "prefreeze_focused_pytest": [*pytest_prefix, "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py"],
        "l3_a1_modules_pytest": [
            *pytest_prefix, "tests/test_r401_val_l3_a1_static_cell.py",
            "tests/test_r401_val_l3_a1_v2_static_scheduler.py",
            "tests/test_r401_val_l3_a1_v2_static_checker.py",
            "tests/test_r401_val_l3_a1_v2_branch_scheduler.py",
            "tests/test_r401_val_l3_a1_v2_branch_checker.py",
            "tests/test_r401_val_l3_a1_v2_s0_compatibility.py",
            "tests/test_r401_val_l3_a1_v2_composite_contract.py",
            "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py",
            "tests/test_r401_val_l3_a1_v2_release_provenance.py",
        ],
        "paper02_full_pytest": list(pytest_prefix),
        "git_diff_check": ["/usr/bin/git", "diff", "--check", "HEAD", "--"],
    }


def _parse_pytest_counts(
    stdout: Any,
    context: str,
    *,
    wall_duration_ms: int | None = None,
) -> dict[str, int]:
    require(type(stdout) is str and stdout.endswith("\n") and "\x00" not in stdout, f"{context}: terminal UTF-8 summary required")
    raw = stdout.encode("utf-8", errors="strict")
    require(len(raw) <= 1024 * 1024, f"{context}: transcript cap")
    require(
        all(
            not ((ord(character) < 0x20 and character != "\n") or 0x7f <= ord(character) <= 0x9f or character in "\u2028\u2029")
            for character in stdout
        ),
        f"{context}: forbidden control character",
    )
    pattern = re.compile(
        r"(?P<counts>[1-9][0-9]{0,3} (?:passed|failed|skipped|xfailed|xpassed)"
        r"(?:, [1-9][0-9]{0,3} (?:passed|failed|skipped|xfailed|xpassed))*) "
        r"in (?P<elapsed>(?:0|[1-9][0-9]{0,2})\.[0-9]{2})s"
        r"(?: \((?P<hours>0):(?P<minutes>[0-5][0-9]):(?P<seconds>[0-5][0-9])\))?"
    )
    matches = [pattern.fullmatch(line) for line in stdout[:-1].split("\n")]
    observed = [match for match in matches if match is not None]
    require(len(observed) == 1 and matches[-1] is not None, f"{context}: one terminal pytest summary")
    require(re.search(r"(?i)(?<![A-Za-z0-9_])(?:errors?|fail(?:ed|ures?)?|warnings?|deselected|skipped|xfail(?:ed)?|xpass(?:ed)?)(?![A-Za-z0-9_])", stdout) is None, f"{context}: nonpass token")
    match = observed[0]
    elapsed_whole_text, elapsed_fraction = match.group("elapsed").split(".", 1)
    whole_seconds = int(elapsed_whole_text)
    elapsed_centiseconds = whole_seconds * 100 + int(elapsed_fraction)
    require(elapsed_centiseconds <= 60000, f"{context}: pytest duration exceeds 600 seconds")
    elapsed_ms = elapsed_centiseconds * 10
    human_parts = tuple(match.group(name) for name in ("hours", "minutes", "seconds"))
    if all(part is None for part in human_parts):
        require(whole_seconds < 60 or (whole_seconds == 60 and elapsed_fraction == "00"), f"{context}: missing long-duration pytest suffix")
    else:
        require(all(part is not None for part in human_parts), f"{context}: malformed long-duration suffix")
        hours, minutes, seconds = (int(part) for part in human_parts if part is not None)
        human_seconds = hours * 3600 + minutes * 60 + seconds
        allowed = {whole_seconds}
        if elapsed_fraction == "00" and whole_seconds > 60:
            allowed.add(whole_seconds - 1)
        require(human_seconds >= 60 and human_seconds in allowed, f"{context}: inconsistent long-duration suffix")
    if wall_duration_ms is not None:
        require(elapsed_ms <= wall_duration_ms + 5, f"{context}: pytest duration exceeds outer wall")
    counts = {key: 0 for key in PREFREEZE_PYTEST_COUNT_KEYS}
    observed_names: set[str] = set()
    for part in match.group("counts").split(", "):
        count_text, name = part.split(" ", 1)
        require(name not in observed_names and name in counts, f"{context}: duplicate pytest category")
        observed_names.add(name)
        counts[name] = int(count_text)
    require(counts["passed"] > 0 and all(value == 0 for key, value in counts.items() if key != "passed"), f"{context}: pytest is not exact all-pass")
    return counts


def _validate_verify_receipt(value: Any, status_value: str, binding: Mapping[str, Any], context: str) -> None:
    exact_keys(value, PREFREEZE_VERIFY_RECEIPT_KEYS, context)
    require(value == {
        "verification_status": status_value,
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": binding["sha256"],
        "size_bytes": binding["size_bytes"],
        "promotion_authorized": False,
    }, f"{context}: exact receipt mismatch")


def _validate_second_receipt(
    value: Any,
    roles: Mapping[str, Mapping[str, Any]],
    context: str,
    *,
    project_root: Path,
) -> None:
    exact_keys(value, PREFREEZE_SECOND_RECEIPT_KEYS, context)
    source = roles["branch_evaluator_source"]
    binary = roles["branch_evaluator_binary"]
    require(
        value["verification_status"] == "PASS_SECOND_FRESH_REBUILD"
        and value["authority"] == "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY"
        and value["source_path"] == source["path"]
        and value["source_sha256"] == source["sha256"]
        and value["persistent_binary_path"] == binary["path"]
        and value["persistent_before_sha256"] == binary["sha256"]
        and value["persistent_after_sha256"] == binary["sha256"]
        and value["staging_output_sha256"] == binary["sha256"]
        and value["staging_output_mode"] == "0755"
        and value["persistent_identity_unchanged"] is True
        and value["persistent_overwrite_performed"] is False
        and value["staging_output_removed"] is True
        and value["byte_for_byte_equal"] is True
        and value["scientific_evaluator_dispatched"] is False,
        f"{context}: reproducibility receipt mismatch",
    )
    for key in ("persistent_before_device_id", "persistent_before_inode", "persistent_after_device_id", "persistent_after_inode"):
        require_exact_int(value[key], f"{context}.{key}", minimum=1)
    require(value["persistent_before_device_id"] == value["persistent_after_device_id"] and value["persistent_before_inode"] == value["persistent_after_inode"], f"{context}: persistent identity")
    binary_pinned = _read_pinned_regular_snapshot(
        _project_file(project_root, binary["path"]),
        context=f"{context}: live role17 binary",
    )
    binary_info = binary_pinned.info
    require(
        sha256_bytes(binary_pinned.raw) == binary["sha256"]
        and len(binary_pinned.raw) == binary["size_bytes"]
        and value["persistent_before_device_id"] == binary_info.st_dev
        and value["persistent_after_device_id"] == binary_info.st_dev
        and value["persistent_before_inode"] == binary_info.st_ino
        and value["persistent_after_inode"] == binary_info.st_ino,
        f"{context}: receipt/live role17 inode mismatch",
    )
    require_exact_int(value["staging_output_size_bytes"], f"{context}.staging size", expected=binary["size_bytes"], minimum=1)


def _validate_role11_command(
    value: Any,
    index: int,
    *,
    project_root: Path,
    python_path: str,
    roles: Mapping[str, Mapping[str, Any]],
    locked_counts: Mapping[str, int],
) -> tuple[Mapping[str, Any], dict[str, int] | None]:
    require(type(value) is dict, f"V2 role11 command[{index}]: object required")
    exact_keys(value, PREFREEZE_COMMAND_KEYS, f"V2 role11 command[{index}]")
    name, kind = PREFREEZE_COMMAND_SPECS[index]
    require(value["name"] == name and value["kind"] == kind, f"V2 role11 command[{index}]: identity/order")
    argv = value["argv"]
    require(type(argv) is list and argv and all(type(item) is str and item and "\x00" not in item for item in argv), f"V2 role11 command[{index}]: argv")
    fixed = _role11_fixed_argv(project_root, python_path)
    if name == "second_fresh_rebuild":
        require(
            argv[:-1] == [python_path, str(project_root / "scripts/run_r401_val_l3_a1_v2_all_slabs.py"), "--second-fresh-rebuild-only", "--output"]
            and re.fullmatch(r"/tmp/a416-l3a1-v2-role11-rebuild\.[0-9A-Za-z]{6,}/capd_r401_phase_branch_tube_mp_a1", argv[-1]) is not None,
            f"V2 role11 command[{index}]: private rebuild argv",
        )
    else:
        require_json_exact(argv, fixed[name], f"V2 role11 command[{index}].argv")
    require(value["cwd"] == str(project_root) and json_exact_equal(value["environment"], PREFREEZE_CLEAN_ENVIRONMENT), f"V2 role11 command[{index}]: cwd/environment")
    require_exact_int(value["return_code"], f"V2 role11 command[{index}].return_code", expected=0)
    _utc_timestamp(value["started_at_utc"], f"V2 role11 command[{index}].started")
    duration = require_exact_int(value["wall_duration_ms"], f"V2 role11 command[{index}].duration", minimum=1)
    require(duration <= 603000, f"V2 role11 command[{index}]: timeout envelope")
    for stream in ("stdout", "stderr"):
        text = value[f"{stream}_utf8"]
        require(type(text) is str and "\x00" not in text, f"V2 role11 command[{index}].{stream}: UTF-8")
        raw = text.encode("utf-8", errors="strict")
        require(len(raw) <= 1024 * 1024, f"V2 role11 command[{index}].{stream}: cap")
        require(value[f"{stream}_sha256"] == sha256_bytes(raw), f"V2 role11 command[{index}].{stream}: hash")
        require_exact_int(value[f"{stream}_size_bytes"], f"V2 role11 command[{index}].{stream}.size", expected=len(raw))
    require(value["stderr_utf8"] == "", f"V2 role11 command[{index}]: successful stderr")
    parsed: dict[str, int] | None = None
    if name in PREFREEZE_TEST_RESULT_TOTAL:
        parsed = _parse_pytest_counts(value["stdout_utf8"], f"V2 role11 command[{index}]", wall_duration_ms=duration)
        total_name = PREFREEZE_TEST_RESULT_TOTAL[name]
        require(parsed["passed"] == locked_counts[total_name], f"V2 role11 command[{index}]: passed-count lock")
        require(type(value["pytest_counts"]) is dict, f"V2 role11 command[{index}].pytest_counts")
        exact_keys(value["pytest_counts"], PREFREEZE_PYTEST_COUNT_KEYS, f"V2 role11 command[{index}].pytest_counts")
        require_json_exact(value["pytest_counts"], parsed, f"V2 role11 command[{index}].pytest_counts")
        require(value["semantic_receipt"] is None, f"V2 role11 command[{index}]: pytest receipt")
    else:
        require(value["pytest_counts"] is None, f"V2 role11 command[{index}]: non-pytest counts")
        if name == "role24_machine_verify":
            _validate_verify_receipt(value["semantic_receipt"], "PASS_MACHINE_FREEZE_VERIFY_ONLY", roles["machine_freeze"], f"V2 role11 command[{index}].receipt")
            expected = f"machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256={roles['machine_freeze']['sha256']} size_bytes={roles['machine_freeze']['size_bytes']} promotion_authorized=false\n"
            require(value["stdout_utf8"] == expected, f"V2 role11 command[{index}]: machine transcript")
        elif name == "role13_compatibility_verify":
            _validate_verify_receipt(value["semantic_receipt"], "PASS_S0_COMPATIBILITY_VERIFY_ONLY", roles["s0_compatibility"], f"V2 role11 command[{index}].receipt")
            expected = f"s0_compatibility_verification=PASS_S0_COMPATIBILITY_VERIFY_ONLY authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256={roles['s0_compatibility']['sha256']} size_bytes={roles['s0_compatibility']['size_bytes']} promotion_authorized=false\n"
            require(value["stdout_utf8"] == expected, f"V2 role11 command[{index}]: S0 transcript")
        elif name == "git_diff_check":
            require(value["stdout_utf8"] == "" and value["semantic_receipt"] is None, f"V2 role11 command[{index}]: diff evidence")
        else:
            _validate_second_receipt(value["semantic_receipt"], roles, f"V2 role11 command[{index}].receipt", project_root=project_root)
            require(value["stdout_utf8"].encode() == canonical_json_bytes(value["semantic_receipt"]), f"V2 role11 command[{index}]: rebuild transcript")
    return value, parsed


def _validate_role11(
    project_root: Path,
    payload: Any,
    metadata: Mapping[str, Mapping[str, Any]],
    role5: Mapping[str, Any],
) -> None:
    require(type(payload) is dict, "V2 role11: object required")
    exact_keys(payload, PREFREEZE_TEST_KEYS, "V2 role11")
    require_exact_int(payload["schema_version"], "V2 role11.schema_version", expected=1)
    require(
        payload["protocol_id"] == "R401-VAL-L3-A1-PREFREEZE-TESTS"
        and payload["artifact_role"] == "PREFREEZE_TEST_RECORD"
        and payload["artifact_status"] == "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW"
        and payload["authority"] == "PREFREEZE_TEST_EVIDENCE_ONLY"
        and payload["scientific_licensing_enabled"] is False
        and payload["production_authorized"] is False
        and payload["scientific_dispatch_performed"] is False
        and payload["claim_boundary"] == PREFREEZE_CLAIM_BOUNDARY,
        "V2 role11 identity/authority",
    )
    _require_null_program_statuses(payload, "V2 role11")
    recorded_at = _utc_timestamp(payload["recorded_at_utc"], "V2 role11.recorded_at_utc")
    expected_held = {
        "held_out_l3_scientific_outputs_read": False,
        "held_out_l3_evaluator_dispatched": False,
        "scientific_evaluator_dispatch_count": 0,
        "new_archive_scope": "TEMPORARY_MOCK_ONLY",
        "s0_archive_access": "READ_ONLY_SEALED_PUBLIC_SIX_CELL",
        "canonical_result_created": False,
    }
    require_json_exact(payload["held_out_policy"], expected_held, "V2 role11 held-out policy")
    counts = EXPECTED_PREFREEZE_TEST_PASSED
    require(
        type(counts) is dict
        and set(counts) == {"prefreeze_focused", "l3_a1_modules", "paper02_full"}
        and all(type(value) is int and value > 0 for value in counts.values()),
        "V2 role11 final passed-count registry is unset",
    )

    entries = payload["pre_review_input_roles"]
    require(type(entries) is list and len(entries) == 51 and len(PREFREEZE_INPUT_ROLES) == 51, "V2 role11 ordered 51 roles")
    live_roles: dict[str, Mapping[str, Any]] = {}
    for index, ((role, relative), entry) in enumerate(zip(PREFREEZE_INPUT_ROLES, entries, strict=True)):
        require(type(entry) is dict, f"V2 role11 role[{index}]: object")
        exact_keys(entry, PREFREEZE_ROLE_ENTRY_KEYS, f"V2 role11 role[{index}]")
        expected = metadata[role]
        require_json_exact(entry, expected, f"V2 role11 role[{index}]")
        require(relative == entry["path"] and entry["nlink"] == 1, f"V2 role11 role[{index}]: path/link")
        live_roles[role] = entry
    require(len({entry["role"] for entry in entries}) == 51 and len({entry["path"] for entry in entries}) == 51, "V2 role11 role aliases")

    reviewed_anchors = {row["role"]: row for row in role5["reviewed_v2_inputs"]}
    tools = payload["evidence_tool_bindings"]
    exact_keys(tools, set(PREFREEZE_TOOL_ROLES), "V2 role11 evidence tools")
    for name, role in PREFREEZE_TOOL_ROLES.items():
        binding = tools[name]
        exact_keys(binding, PREFREEZE_FILE_BINDING_KEYS, f"V2 role11 tool {name}")
        expected = {key: metadata[role][key] for key in PREFREEZE_FILE_BINDING_KEYS}
        require_json_exact(binding, expected, f"V2 role11 tool {name}/live")
        require_json_exact(
            {key: binding[key] for key in ("path", "sha256")},
            {key: reviewed_anchors[role][key] for key in ("path", "sha256")},
            f"V2 role11 tool {name}/role5",
        )
        require_json_exact(binding, {key: live_roles[role][key] for key in PREFREEZE_FILE_BINDING_KEYS}, f"V2 role11 tool {name}/51-role")
    require(len({tools[name]["path"] for name in tools}) == 3, "V2 role11 tool aliases")

    repository = payload["repository_snapshot"]
    exact_keys(repository, PREFREEZE_REPOSITORY_KEYS, "V2 role11 repository")
    for name in ("capture_commit_oid", "capture_tree_oid", "origin_main_oid", "live_remote_main_oid"):
        require(type(repository[name]) is str and re.fullmatch(r"[0-9a-f]{40}", repository[name]), f"V2 role11 repository.{name}")
    require(
        repository["authority_root"] == str(project_root)
        and repository["branch"] == "main"
        and repository["origin_url"] == "git@github.com:maris205/hilbert-polya-structure.git"
        and repository["capture_commit_oid"] == repository["origin_main_oid"] == repository["live_remote_main_oid"]
        and repository["head_equals_origin_main"] is True
        and repository["head_equals_live_remote_main"] is True
        and repository["ahead"] == 0 and type(repository["ahead"]) is int
        and repository["behind"] == 0 and type(repository["behind"]) is int
        and repository["worktree_clean_before"] is True
        and repository["worktree_clean_after"] is True,
        "V2 role11 repository gates",
    )
    require(_git_commit_tree(project_root, repository["capture_commit_oid"]) == repository["capture_tree_oid"], "V2 role11 commit/tree binding")
    committed = _git_blob_batch(project_root, [(repository["capture_commit_oid"], entry["path"]) for entry in entries])
    for entry, (raw, mode) in zip(entries, committed, strict=True):
        expected_mode = "100755" if int(entry["mode"], 8) & 0o111 else "100644"
        require(mode == expected_mode and sha256_bytes(raw) == entry["sha256"] and raw == read_pinned_regular_bytes(_project_file(project_root, entry["path"])), f"V2 role11 commit/live mismatch: {entry['role']}")

    results = payload["command_results"]
    require(type(results) is list and len(results) == 7, "V2 role11 seven commands")
    python_path = load_strict_json_object_from_bytes(read_pinned_regular_bytes(_project_file(project_root, dict(INPUT_ROLES)["machine_freeze"])), _project_file(project_root, dict(INPUT_ROLES)["machine_freeze"]))["python_arb"]["executable_path"]
    validated: list[Mapping[str, Any]] = []
    parsed_counts: dict[str, dict[str, int]] = {}
    previous: datetime | None = None
    assert counts is not None
    for index, result in enumerate(results):
        row, parsed = _validate_role11_command(result, index, project_root=project_root, python_path=python_path, roles=live_roles, locked_counts=counts)
        started = _utc_timestamp(row["started_at_utc"], f"V2 role11 command[{index}].started")
        require((previous is None or started >= previous) and started <= recorded_at, "V2 role11 command timestamp order")
        previous = started
        validated.append(row)
        if parsed is not None:
            parsed_counts[row["name"]] = parsed

    prerequisites = payload["prerequisite_bindings"]
    exact_keys(prerequisites, {"machine_role10", "s0_compatibility_role13", "second_fresh_rebuild_replay", "canonical_absence"}, "V2 role11 prerequisites")
    machine = prerequisites["machine_role10"]
    exact_keys(machine, PREFREEZE_ROLE_ENTRY_KEYS | {"publication_commit_oid", "producer_path", "producer_sha256", "verifier_path", "verifier_sha256", "verify_receipt", "promotion_authorized"}, "V2 role11 machine prerequisite")
    require_json_exact({key: machine[key] for key in PREFREEZE_ROLE_ENTRY_KEYS}, live_roles["machine_freeze"], "V2 role11 machine/live")
    require(machine["producer_path"] == live_roles["scheduler"]["path"] and machine["producer_sha256"] == live_roles["scheduler"]["sha256"] and machine["verifier_path"] == live_roles["release_builder"]["path"] and machine["verifier_sha256"] == live_roles["release_builder"]["sha256"] and machine["promotion_authorized"] is False and machine["mode"] == "0644", "V2 role11 machine tools")
    _validate_verify_receipt(machine["verify_receipt"], "PASS_MACHINE_FREEZE_VERIFY_ONLY", live_roles["machine_freeze"], "V2 role11 machine receipt")
    require_json_exact(machine["verify_receipt"], validated[0]["semantic_receipt"], "V2 role11 machine command receipt")
    compatibility = prerequisites["s0_compatibility_role13"]
    exact_keys(compatibility, PREFREEZE_ROLE_ENTRY_KEYS | {"publication_commit_oid", "producer_path", "producer_sha256", "verify_receipt", "promotion_authorized"}, "V2 role11 S0 prerequisite")
    require_json_exact({key: compatibility[key] for key in PREFREEZE_ROLE_ENTRY_KEYS}, live_roles["s0_compatibility"], "V2 role11 S0/live")
    require(compatibility["producer_path"] == live_roles["s0_adapter"]["path"] and compatibility["producer_sha256"] == live_roles["s0_adapter"]["sha256"] and compatibility["promotion_authorized"] is False and compatibility["mode"] == "0644", "V2 role11 S0 producer")
    _validate_verify_receipt(compatibility["verify_receipt"], "PASS_S0_COMPATIBILITY_VERIFY_ONLY", live_roles["s0_compatibility"], "V2 role11 S0 receipt")
    require_json_exact(compatibility["verify_receipt"], validated[1]["semantic_receipt"], "V2 role11 S0 command receipt")
    for item in (machine, compatibility):
        require(type(item["publication_commit_oid"]) is str and re.fullmatch(r"[0-9a-f]{40}", item["publication_commit_oid"]), "V2 role11 publication commit")
    publication_blobs = _git_blob_batch(project_root, [(machine["publication_commit_oid"], machine["path"]), (compatibility["publication_commit_oid"], compatibility["path"])])
    for item, (raw, mode) in zip((machine, compatibility), publication_blobs, strict=True):
        require(mode == "100644" and sha256_bytes(raw) == item["sha256"] and raw == read_pinned_regular_bytes(_project_file(project_root, item["path"])), "V2 role11 prerequisite publication blob")
    absence = prerequisites["canonical_absence"]
    exact_keys(absence, {"prefreeze_review_role12_exists", "main_freeze_role54_exists", "canonical_result_root_exists", "canonical_operational_root_exists"}, "V2 role11 historical absence")
    require(all(type(value) is bool and value is False for value in absence.values()), "V2 role11 historical absence values")
    rebuild = prerequisites["second_fresh_rebuild_replay"]
    exact_keys(rebuild, {"command_result_name", "command_result_sha256", "semantic_receipt"}, "V2 role11 rebuild replay")
    require(rebuild["command_result_name"] == "second_fresh_rebuild" and rebuild["command_result_sha256"] == sha256_bytes(canonical_json_bytes(validated[6])), "V2 role11 rebuild command binding")
    _validate_second_receipt(rebuild["semantic_receipt"], live_roles, "V2 role11 rebuild prerequisite", project_root=project_root)
    require_json_exact(rebuild["semantic_receipt"], validated[6]["semantic_receipt"], "V2 role11 rebuild receipt binding")

    totals = payload["test_totals"]
    exact_keys(totals, {"prefreeze_focused", "l3_a1_modules", "paper02_full"}, "V2 role11 test totals")
    by_name = {row["name"]: row for row in validated}
    for result_name, total_name in PREFREEZE_TEST_RESULT_TOTAL.items():
        total = totals[total_name]
        exact_keys(total, PREFREEZE_TEST_TOTAL_KEYS, f"V2 role11 total {total_name}")
        for key in PREFREEZE_PYTEST_COUNT_KEYS:
            require_exact_int(total[key], f"V2 role11 total {total_name}.{key}", expected=parsed_counts[result_name][key])
        require_exact_int(total["wall_duration_ms"], f"V2 role11 total {total_name}.duration", expected=by_name[result_name]["wall_duration_ms"], minimum=1)
    require_json_exact(payload["covered_gates"], list(PREFREEZE_COVERED_GATES), "V2 role11 covered gates")
    require(len(canonical_json_bytes(payload)) <= 4 * 1024 * 1024, "V2 role11 byte cap")


def _compact_object(raw: bytes, path: Path, context: str) -> dict[str, Any]:
    payload = load_strict_json_object_from_bytes(raw, path)
    require(raw == canonical_json_bytes(payload), f"{context}: CJ_COMPACT_V1 required")
    return payload


def _validate_main_payload(
    project_root: Path,
    main: Any,
    rows: Sequence[Mapping[str, str]],
    images: Mapping[str, bytes],
    metadata: Mapping[str, Mapping[str, Any]],
) -> None:
    require(type(main) is dict, "V2 main: object required")
    exact_keys(main, MAIN_FREEZE_KEYS, "V2 main")
    require_exact_int(main["schema_version"], "V2 main.schema_version", expected=1)
    require(
        main["protocol_id"] == PROTOCOL_ID
        and main["artifact_role"] == "MAIN_FREEZE"
        and main["status"] == "FROZEN_FOR_PRODUCTION"
        and main["authority"] == "INDEPENDENT_PREFREEZE_REVIEW"
        and main["scientific_licensing_enabled"] is True,
        "V2 main identity/authority",
    )
    require_json_exact(main["matrix"], _formal_matrix(), "V2 main matrix")
    require(main["matrix_id"] == _formal_matrix_id(), "V2 main matrix id")
    require_json_exact(main["input_roles"], list(rows), "V2 main ordered 53 roles")
    require(type(main["input_roles"]) is list and len(main["input_roles"]) == 53, "V2 main role count")
    for index, row in enumerate(main["input_roles"]):
        exact_keys(row, {"role", "path", "sha256"}, f"V2 main role[{index}]")
        _safe_relative(row["path"], f"V2 main role[{index}].path")
        _exact_sha(row["sha256"], f"V2 main role[{index}].sha256")
    roles = {row["role"]: row for row in rows}
    role5 = _compact_object(images["implementation_design_review"], _project_file(project_root, roles["implementation_design_review"]["path"]), "V2 role5")
    _validate_role5(project_root, role5, rows, images)
    machine = _compact_object(images["machine_freeze"], _project_file(project_root, roles["machine_freeze"]["path"]), "V2 role10")
    _validate_machine_freeze(project_root, machine, roles)
    role11 = _compact_object(images["prefreeze_tests"], _project_file(project_root, roles["prefreeze_tests"]["path"]), "V2 role11")
    _validate_role11(project_root, role11, metadata, role5)
    require(images["prefreeze_review"] == PREFREEZE_ACCEPT_RAW and len(images["prefreeze_review"]) == 27, "V2 role12 exact verdict")
    role13 = _compact_object(images["s0_compatibility"], _project_file(project_root, roles["s0_compatibility"]["path"]), "V2 role13")
    _validate_s0_compatibility(project_root, role13, metadata)
    require(main["machine_freeze_sha256"] == roles["machine_freeze"]["sha256"], "V2 main/machine hash")
    exact_keys(main["prefreeze_review"], {"path", "sha256", "verdict"}, "V2 main review binding")
    require_json_exact(
        main["prefreeze_review"],
        {"path": roles["prefreeze_review"]["path"], "sha256": roles["prefreeze_review"]["sha256"], "verdict": "ACCEPT_FOR_FREEZE"},
        "V2 main review binding",
    )
    expected_sections = {
        "serializers": _formal_serializers(), "scheduler": _formal_scheduler_policy(),
        "limits": _formal_limits(), "status_tables": _formal_status_tables(),
        "archive_layout": _formal_archive_layout(),
        "machine_requirements": _formal_machine_requirements(),
        "failure_policy": _formal_failure_policy(),
        "execution_policy": _formal_execution_policy(),
    }
    for key, expected in expected_sections.items():
        require_json_exact(main[key], expected, f"V2 main.{key}")
    require_json_exact(
        main["evaluators"],
        {
            "static": {"path": roles["static_evaluator"]["path"], "sha256": roles["static_evaluator"]["sha256"], "abi": "PYTHON_STATIC_ABI_26_STRINGS_V1", "argv_count": 26},
            "branch": {
                "source_path": roles["branch_evaluator_source"]["path"],
                "source_sha256": roles["branch_evaluator_source"]["sha256"],
                "binary_path": roles["branch_evaluator_binary"]["path"],
                "binary_sha256": roles["branch_evaluator_binary"]["sha256"],
                "runtime_path": roles["branch_runtime"]["path"],
                "runtime_sha256": roles["branch_runtime"]["sha256"],
                "abi": "CAPD_BRANCH_ABI_12_STRINGS_V1", "argv_count": 12,
            },
        },
        "V2 main evaluators",
    )
    require_json_exact(
        main["checkers"],
        {
            "static": {"path": roles["static_checker_source"]["path"], "sha256": roles["static_checker_source"]["sha256"]},
            "branch": {"path": roles["branch_checker_source"]["path"], "sha256": roles["branch_checker_source"]["sha256"]},
            "composite": {"path": roles["composite_checker_source"]["path"], "sha256": roles["composite_checker_source"]["sha256"]},
            "release_builder": {"path": roles["release_builder"]["path"], "sha256": roles["release_builder"]["sha256"]},
        },
        "V2 main checkers",
    )
    require(main["claim_boundary"] == MAIN_FREEZE_CLAIM_BOUNDARY, "V2 main claim boundary")
    _require_null_program_statuses(main, "V2 main")
    require(roles["static_checker_source"]["sha256"] == sha256_file(CHECKER), "executing V2 static checker differs from role20")


def verify_formal_main_freeze_path(
    candidate: Path | str,
    project_root: Path | str = ROOT,
) -> dict[str, Any]:
    """Strict read-only V2 role-54 verification with terminal replay."""

    root = require_canonical_absolute_path(project_root, "V2 project root")
    path = require_canonical_absolute_path(candidate, "V2 main candidate")
    canonical_main = _project_file(root, V2_MAIN_RELATIVE)
    private_parent: tuple[int, int, int, int] | None = None
    if path != canonical_main:
        private_parent = _owned_candidate_parent(
            path,
            expected_leaf=Path(V2_MAIN_RELATIVE).name,
            before_write=False,
        )
    candidate_pinned = _read_pinned_regular_snapshot(
        path,
        maximum_bytes=PUBLICATION_MAX_BYTES,
        context="V2 main candidate",
    )
    require(
        candidate_pinned.info.st_nlink == 1
        and stat.S_IMODE(candidate_pinned.info.st_mode)
        == (0o644 if path == canonical_main else 0o600),
        "V2 main candidate mode/link contract mismatch",
    )
    if private_parent is not None:
        require(
            candidate_pinned.parent_chain[-1][1:5] == private_parent,
            "V2 private main candidate parent changed",
        )
    candidate_raw = candidate_pinned.raw
    main = _compact_object(candidate_raw, path, "V2 main")
    rows, images, metadata, generations = _capture_formal_roles(root)
    _validate_main_payload(root, main, rows, images, metadata)
    # Re-open and repeat every semantic gate at the terminal edge.  Rechecking
    # only hashes here would leave the Git/role10/role11/role13 live bindings
    # outside the final generation boundary.
    terminal_candidate = _read_pinned_regular_snapshot(
        path,
        maximum_bytes=PUBLICATION_MAX_BYTES,
        context="V2 main candidate terminal replay",
    )
    require(
        terminal_candidate.raw == candidate_raw
        and _stable_stat_identity(terminal_candidate.info)
        == _stable_stat_identity(candidate_pinned.info)
        and terminal_candidate.parent_chain == candidate_pinned.parent_chain,
        "V2 main candidate changed before terminal replay",
    )
    if private_parent is not None:
        require(
            _owned_candidate_parent(
                path,
                expected_leaf=Path(V2_MAIN_RELATIVE).name,
                before_write=False,
            )
            == private_parent,
            "V2 private main candidate namespace changed",
        )
    terminal_rows, terminal_images, terminal_metadata, terminal_generations = _capture_formal_roles(root)
    require_json_exact(terminal_rows, rows, "V2 terminal ordered role generation")
    require(terminal_images == images, "V2 terminal role bytes changed")
    require_json_exact(terminal_metadata, metadata, "V2 terminal role metadata changed")
    require(
        terminal_generations == generations,
        "V2 terminal role inode generation changed",
    )
    _validate_main_payload(
        root, main, terminal_rows, terminal_images, terminal_metadata
    )
    receipt = {
        "verification_status": "PASS_MAIN_FREEZE_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(candidate_raw),
        "input_map_sha256": sha256_bytes(canonical_json_bytes(list(rows))),
        "size_bytes": len(candidate_raw),
        "promotion_authorized": False,
        "artifacts_written": False,
    }
    validate_main_verify_receipt(receipt, candidate_raw, rows)
    return receipt


def validate_main_verify_receipt(
    receipt: Any,
    candidate_raw: bytes,
    input_roles: Sequence[Mapping[str, Any]],
) -> None:
    """Close the non-authoritative exact-seven role-54 receipt contract."""

    require(type(receipt) is dict, "V2 main verify receipt: object required")
    exact_keys(receipt, MAIN_VERIFY_RECEIPT_KEYS, "V2 main verify receipt")
    require(
        receipt["verification_status"] == "PASS_MAIN_FREEZE_VERIFY_ONLY"
        and receipt["authority"] == "NON_AUTHORITATIVE_VERIFY_ONLY"
        and receipt["candidate_sha256"] == sha256_bytes(candidate_raw)
        and receipt["input_map_sha256"]
        == sha256_bytes(canonical_json_bytes(list(input_roles)))
        and receipt["promotion_authorized"] is False
        and receipt["artifacts_written"] is False,
        "V2 main verify receipt binding mismatch",
    )
    _exact_sha(receipt["candidate_sha256"], "V2 main receipt candidate hash")
    _exact_sha(receipt["input_map_sha256"], "V2 main receipt input-map hash")
    require_exact_int(
        receipt["size_bytes"],
        "V2 main receipt size_bytes",
        expected=len(candidate_raw),
    )


RUN_CONFIG_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "scientific_licensing_enabled", "dispatch_authorized_by_artifact",
    "matrix", "matrix_id", "freeze_sha256", "main_freeze_sha256",
    "main_freeze", "machine_freeze", "prefreeze_review", "input_roles",
    "serializers", "scheduler", "limits", "status_tables", "evaluators",
    "checkers", "archive_layout", "machine_requirements", "execution_policy",
    "paths", "filesystem_identity", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
AGGREGATE_COMMON_KEYS = {
    "schema_version", "protocol_id", "artifact_status", "authority",
    "scientific_licensing_enabled", "matrix_id", "freeze_sha256",
    "main_freeze_sha256", "run_config_sha256", "ordered_cell_manifest_root",
    "evaluator_roles", "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}
AGGREGATE_SUMMARY_KEYS = AGGREGATE_COMMON_KEYS | {
    "artifact_role", "matrix", "cell_count", "status_counts",
    "scheduler_classification_counts",
}
AGGREGATE_MANIFEST_KEYS = AGGREGATE_COMMON_KEYS | {"artifact_role", "cell_manifests", "summary"}
AGGREGATE_ENTRY_KEYS = {"cell", "path", "sha256", "size_bytes", "evaluator_status", "scheduler_classification"}
RUN_CONFIG_CLAIM_BOUNDARY = (
    "write-once formal run binding only; the artifact never self-authorizes "
    "scientific dispatch or any component, theorem, Hilbert-Polya, zeta-zero, or RH claim"
)
AGGREGATE_CLAIM_BOUNDARY = (
    "complete 102-cell producer archive only; independent component replay "
    "remains required and no component, theorem, Hilbert-Polya, zeta-zero, or RH status is assigned"
)


@dataclass(frozen=True)
class FormalAuthority:
    root: Path
    main: Mapping[str, Any]
    main_raw: bytes
    rows: tuple[Mapping[str, str], ...]
    images: Mapping[str, bytes]
    metadata: Mapping[str, Mapping[str, Any]]
    generations: Mapping[
        str,
        tuple[tuple[int, int, int, int, int, int, int, int, int], _ParentChainIdentity],
    ]


@dataclass(frozen=True)
class PublicationTransient:
    """The one invocation-owned same-parent staging inode.

    Formal archive replay accepts this entry only while the publisher holds
    the parent-directory lock, and only with the exact recorded inode and
    bytes.  No other dotfile or operational residue is tolerated.
    """

    parent: Path
    name: str
    device_id: int
    inode: int
    raw: bytes


def _load_formal_authority(project_root: Path) -> FormalAuthority:
    root = require_canonical_absolute_path(project_root, "V2 project root")
    main_path = _project_file(root, V2_MAIN_RELATIVE)
    main_raw = read_pinned_regular_bytes(main_path)
    main = _compact_object(main_raw, main_path, "V2 canonical main")
    rows, images, metadata, generations = _capture_formal_roles(root)
    _validate_main_payload(root, main, rows, images, metadata)
    return FormalAuthority(
        root, main, main_raw, tuple(rows), images, metadata, generations
    )


def _fixed_result_root(project_root: Path, result_root: Path | str) -> Path:
    result = require_canonical_absolute_path(result_root, "V2 result root")
    expected = _project_file(project_root, V2_RESULT_RELATIVE)
    require(result == expected, "V2 formal checker requires the fixed result root")
    require(result.is_dir() and not result.is_symlink(), "V2 result root must be a real directory")
    return result


def _expected_run_config(authority: FormalAuthority, result: Path) -> dict[str, Any]:
    roles = {row["role"]: row for row in authority.rows}
    main_hash = sha256_bytes(authority.main_raw)
    device = result.parent.stat().st_dev
    return {
        "schema_version": 1, "protocol_id": PROTOCOL_ID,
        "artifact_role": "RUN_CONFIG", "artifact_status": "SEALED_CONTROL_PLANE_BINDING",
        "authority": "PRODUCER_ONLY", "scientific_licensing_enabled": False,
        "dispatch_authorized_by_artifact": False, "matrix": _formal_matrix(),
        "matrix_id": _formal_matrix_id(), "freeze_sha256": main_hash,
        "main_freeze_sha256": main_hash,
        "main_freeze": {"path": V2_MAIN_RELATIVE, "sha256": main_hash},
        "machine_freeze": {"path": roles["machine_freeze"]["path"], "sha256": roles["machine_freeze"]["sha256"]},
        "prefreeze_review": {"path": roles["prefreeze_review"]["path"], "sha256": roles["prefreeze_review"]["sha256"], "verdict": "ACCEPT_FOR_FREEZE"},
        "input_roles": list(authority.rows), "serializers": authority.main["serializers"],
        "scheduler": authority.main["scheduler"], "limits": authority.main["limits"],
        "status_tables": authority.main["status_tables"], "evaluators": authority.main["evaluators"],
        "checkers": authority.main["checkers"], "archive_layout": authority.main["archive_layout"],
        "machine_requirements": authority.main["machine_requirements"],
        "execution_policy": authority.main["execution_policy"],
        "paths": {"authoritative_root": str(result), "operational_root": str(result) + ".operational"},
        "filesystem_identity": {"authoritative_parent_device_id": device, "operational_parent_device_id": device, "same_filesystem": True},
        "claim_boundary": RUN_CONFIG_CLAIM_BOUNDARY,
        "component_status": None, "milestone_status": None,
        "theorem_status": None, "final_status": None,
    }


def _load_run_config(authority: FormalAuthority, result: Path) -> tuple[dict[str, Any], bytes]:
    path = result / "run_config.json"
    raw = read_pinned_regular_bytes(path)
    payload = _compact_object(raw, path, "V2 run config")
    exact_keys(payload, RUN_CONFIG_KEYS, "V2 run config")
    require_json_exact(payload, _expected_run_config(authority, result), "V2 run config/main authority")
    return payload, raw


def _validate_formal_static_namespace(
    result: Path,
    *,
    checker: bool,
    postcheck: bool,
    transient: PublicationTransient | None = None,
) -> None:
    expected_root = {"run_config.json", "static", "branch"}
    if checker:
        expected_root.add(V2_CHECKER_OUTPUT)
    if postcheck:
        expected_root.add(V2_POSTCHECK_OUTPUT)
    if transient is not None:
        require(transient.parent == result, "V2 static transient parent mismatch")
        require(
            re.fullmatch(r"\.(?:independent_static_checker\.json|STATIC_POSTCHECK_STATUS\.json)\.publish-[0-9a-f]{32}", transient.name) is not None,
            "V2 static transient basename mismatch",
        )
        expected_root.add(transient.name)
    require_exact_directory_names(result, expected_root, "V2 static authority root")
    if transient is not None:
        transient_path = result / transient.name
        transient_pinned = _read_pinned_regular_snapshot(
            transient_path,
            maximum_bytes=PUBLICATION_MAX_BYTES,
            context="V2 static owned publication transient",
        )
        transient_raw, transient_info = transient_pinned.raw, transient_pinned.info
        require(
            transient_raw == transient.raw
            and (transient_info.st_dev, transient_info.st_ino)
            == (transient.device_id, transient.inode)
            and stat.S_IMODE(transient_info.st_mode) == 0o644
            and transient_info.st_nlink == 1,
            "V2 static transient inode/byte contract mismatch",
        )
    branch = result / "branch"
    require(branch.is_dir() and not branch.is_symlink(), "V2 branch sibling must be a real directory")
    static_root = result / "static"
    require_exact_directory_names(static_root, {"cells", "cell_manifests", "aggregate_summary.json", "aggregate_manifest.json"}, "V2 static root")
    for namespace, suffix in (("cells", ""), ("cell_manifests", ".json")):
        component_root = static_root / namespace
        require_exact_directory_names(component_root, {"128", "256"}, f"V2 static {namespace}")
        for bits in PRECISIONS:
            require_exact_directory_names(component_root / str(bits), {slab + suffix for slab in SLABS}, f"V2 static {namespace}/{bits}")
    for bits in PRECISIONS:
        for slab in SLABS:
            require_exact_directory_names(static_root / "cells" / str(bits) / slab, FORMAL_STATIC_FILE_NAMES, f"V2 static cell {bits}:{slab}")


def _formal_static_argv(
    authority: FormalAuthority,
    run_hash: str,
    bits: int,
    slab: str,
    plan: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    roles = {row["role"]: row for row in authority.rows}
    machine = _compact_object(authority.images["machine_freeze"], _project_file(authority.root, roles["machine_freeze"]["path"]), "V2 role10 argv")
    record = plan[slab]
    return [
        machine["python_arb"]["executable_path"],
        str(_project_file(authority.root, roles["static_evaluator"]["path"])),
        "--slab-id", slab, "--precision-bits", str(bits),
        "--epsilon-lower", record["epsilon_lower"],
        "--epsilon-upper", record["epsilon_upper"],
        "--matrix-id", _formal_matrix_id(),
        "--freeze-sha256", sha256_bytes(authority.main_raw),
        "--run-config-sha256", run_hash,
        "--plan-record-sha256", plan_record_sha256(record),
        "--max-depth", str(_formal_limits()["static"]["max_depth_per_tree"]),
        "--max-nodes-per-tree", str(_formal_limits()["static"]["max_nodes_per_tree"]),
        "--max-nodes-per-cell", str(_formal_limits()["static"]["max_nodes_per_cell"]),
        "--output", "<STAGING_PROOF_PATH>",
    ]


def replay_formal_static_archive(
    project_root: Path | str,
    result_root: Path | str,
    *,
    checker_present: bool = False,
    postcheck_present: bool = False,
    transient: PublicationTransient | None = None,
) -> dict[str, Any]:
    root = require_canonical_absolute_path(project_root, "V2 project root")
    result = _fixed_result_root(root, result_root)
    _validate_formal_static_namespace(
        result,
        checker=checker_present,
        postcheck=postcheck_present,
        transient=transient,
    )
    authority = _load_formal_authority(root)
    _run, run_raw = _load_run_config(authority, result)
    run_hash = sha256_bytes(run_raw)
    main_hash = sha256_bytes(authority.main_raw)
    roles = {row["role"]: row for row in authority.rows}
    summary_path = result / "static" / "aggregate_summary.json"
    manifest_path = result / "static" / "aggregate_manifest.json"
    summary_raw = read_pinned_regular_bytes(summary_path)
    manifest_raw = read_pinned_regular_bytes(manifest_path)
    summary = _compact_object(summary_raw, summary_path, "V2 static aggregate summary")
    manifest = _compact_object(manifest_raw, manifest_path, "V2 static aggregate manifest")
    exact_keys(summary, AGGREGATE_SUMMARY_KEYS, "V2 static aggregate summary")
    exact_keys(manifest, AGGREGATE_MANIFEST_KEYS, "V2 static aggregate manifest")
    expected_evaluators = {"static_evaluator": roles["static_evaluator"]}
    for payload, kind in ((summary, "SUMMARY"), (manifest, "MANIFEST")):
        require_exact_int(payload["schema_version"], f"V2 static aggregate {kind}.schema_version", expected=1)
        require(
            payload["protocol_id"] == PROTOCOL_ID
            and payload["artifact_role"] == f"STATIC_AGGREGATE_{kind}"
            and payload["artifact_status"] == "COMPLETE_PRODUCER_ARCHIVE"
            and payload["authority"] == "PRODUCER_ONLY"
            and payload["scientific_licensing_enabled"] is False
            and payload["matrix_id"] == _formal_matrix_id()
            and payload["freeze_sha256"] == main_hash
            and payload["main_freeze_sha256"] == main_hash
            and payload["run_config_sha256"] == run_hash
            and json_exact_equal(payload["evaluator_roles"], expected_evaluators)
            and payload["claim_boundary"] == AGGREGATE_CLAIM_BOUNDARY,
            f"V2 static aggregate {kind}: identity/binding",
        )
        _require_null_program_statuses(payload, f"V2 static aggregate {kind}")
    require_json_exact(summary["matrix"], _formal_matrix(), "V2 static aggregate matrix")
    require_exact_int(summary["cell_count"], "V2 static aggregate cell count", expected=102)
    require_json_exact(summary["status_counts"], {CELL_PASS_STATUS: 102}, "V2 static aggregate statuses")
    require_json_exact(summary["scheduler_classification_counts"], {"COMMITTED_EVALUATOR_RESULT": 102}, "V2 static aggregate classifications")
    entries = manifest["cell_manifests"]
    require(type(entries) is list and len(entries) == 102, "V2 static aggregate exact 102 entries")
    ordered_root = sha256_bytes(canonical_json_bytes(entries))
    require(summary["ordered_cell_manifest_root"] == ordered_root and manifest["ordered_cell_manifest_root"] == ordered_root, "V2 static aggregate ordered root")
    exact_keys(manifest["summary"], {"path", "sha256", "size_bytes"}, "V2 static aggregate summary edge")
    require_json_exact(manifest["summary"], {"path": "static/aggregate_summary.json", "sha256": sha256_bytes(summary_raw), "size_bytes": len(summary_raw)}, "V2 static aggregate summary edge")
    plan = load_plan()
    context = FormalStaticContext(
        matrix_id=_formal_matrix_id(), freeze_sha256=main_hash,
        run_config_sha256=run_hash,
        max_depth=_formal_limits()["static"]["max_depth_per_tree"],
        max_nodes_per_tree=_formal_limits()["static"]["max_nodes_per_tree"],
        max_nodes_per_cell=_formal_limits()["static"]["max_nodes_per_cell"],
    )
    eligible = 0
    status_pairs: dict[str, dict[int, str]] = {slab: {} for slab in SLABS}
    manifest_images: list[bytes] = []
    for index, (entry, cell) in enumerate(zip(entries, _formal_matrix(), strict=True)):
        exact_keys(entry, AGGREGATE_ENTRY_KEYS, f"V2 static aggregate entry[{index}]")
        bits, slab = cell["precision_bits"], cell["slab_id"]
        expected_path = f"static/cell_manifests/{bits}/{slab}.json"
        require_json_exact(entry["cell"], cell, f"V2 static aggregate entry[{index}].cell")
        require(entry["path"] == expected_path and entry["evaluator_status"] == CELL_PASS_STATUS and entry["scheduler_classification"] == "COMMITTED_EVALUATOR_RESULT", f"V2 static aggregate entry[{index}]: identity/status")
        cell_manifest_path = result / "static" / "cell_manifests" / str(bits) / f"{slab}.json"
        cell_raw = read_pinned_regular_bytes(cell_manifest_path)
        require(entry["sha256"] == sha256_bytes(cell_raw), f"V2 static aggregate entry[{index}]: hash")
        require_exact_int(entry["size_bytes"], f"V2 static aggregate entry[{index}].size", expected=len(cell_raw))
        leaf = validate_formal_static_cell(
            result / "static" / "cells" / str(bits) / slab,
            cell_manifest_path,
            expected_bits=bits, expected_slab=slab, plan=plan, context=context,
            expected_semantic_argv=_formal_static_argv(authority, run_hash, bits, slab, plan),
            expected_limits=_formal_limits()["static"],
        )
        require(leaf["component_eligible"] is True and leaf["evaluator_status"] == CELL_PASS_STATUS and leaf["scheduler_classification"] == "COMMITTED_EVALUATOR_RESULT", f"V2 static leaf not eligible: {bits}:{slab}")
        eligible += 1
        status_pairs[slab][bits] = leaf["evaluator_status"]
        manifest_images.append(cell_raw)
    require(eligible == 102 and all(pair == {128: CELL_PASS_STATUS, 256: CELL_PASS_STATUS} for pair in status_pairs.values()), "V2 static cross-precision eligibility")
    # Terminal replay for every directly authoritative byte.
    require(read_pinned_regular_bytes(summary_path) == summary_raw and read_pinned_regular_bytes(manifest_path) == manifest_raw, "V2 static aggregate changed before terminal replay")
    for entry, before in zip(entries, manifest_images, strict=True):
        require(read_pinned_regular_bytes(result.joinpath(*_safe_relative(entry["path"]).parts)) == before, "V2 static manifest changed before terminal replay")
    return {
        "authority": authority, "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash, "matrix_id": _formal_matrix_id(),
        "aggregate_summary_sha256": sha256_bytes(summary_raw),
        "aggregate_manifest_sha256": sha256_bytes(manifest_raw),
        "aggregate_summary_size_bytes": len(summary_raw),
        "aggregate_manifest_size_bytes": len(manifest_raw),
        "ordered_cell_manifest_root": ordered_root,
        "replay_counts": {"cell_manifests": 102, "hash_bound_payloads": 408},
        "cross_precision": {"slab_pairs": 51, "status_pairs_agree": 51, "passed": True},
    }


def _checker_payload_from_replay(replay: Mapping[str, Any]) -> dict[str, Any]:
    authority: FormalAuthority = replay["authority"]
    roles = {row["role"]: row for row in authority.rows}
    return {
        "schema_version": 1, "protocol_id": PROTOCOL_ID,
        "artifact_role": "STATIC_INDEPENDENT_CHECKER", "authority": "INDEPENDENT_CHECKER",
        "checker_status": FORMAL_CHECKER_STATUS, "component_status": PASS_STATUS,
        "scientific_licensing_enabled": False, "passed": True,
        "matrix_id": replay["matrix_id"], "main_freeze_sha256": replay["main_freeze_sha256"],
        "run_config_sha256": replay["run_config_sha256"],
        "component_aggregate_summary_sha256": replay["aggregate_summary_sha256"],
        "component_aggregate_manifest_sha256": replay["aggregate_manifest_sha256"],
        "replay_counts": replay["replay_counts"], "cross_precision": replay["cross_precision"],
        "diagnostics": {
            "ordered_cell_manifest_root": replay["ordered_cell_manifest_root"],
            "aggregate_summary_sha256": replay["aggregate_summary_sha256"],
            "aggregate_manifest_sha256": replay["aggregate_manifest_sha256"],
        },
        "failures": [],
        "source_bindings": {
            "checker_source": {"path": roles["static_checker_source"]["path"], "sha256": roles["static_checker_source"]["sha256"]},
            "producer_source": {"path": roles["scheduler"]["path"], "sha256": roles["scheduler"]["sha256"]},
        },
        "claim_boundary": CLAIM_BOUNDARY, "milestone_status": None,
        "theorem_status": None, "final_status": None,
    }


def build_checker_payload(project_root: Path | str, result_root: Path | str) -> dict[str, Any]:
    return _checker_payload_from_replay(
        replay_formal_static_archive(project_root, result_root)
    )


def validate_checker_payload(payload: Any, expected: Mapping[str, Any]) -> None:
    require(type(payload) is dict, "V2 static checker: object required")
    exact_keys(payload, FORMAL_CHECKER_KEYS, "V2 static checker")
    exact_keys(expected, FORMAL_CHECKER_KEYS, "V2 static expected checker")
    require_json_exact(payload, dict(expected), "V2 static checker exact replay")
    require(
        payload["checker_status"] == FORMAL_CHECKER_STATUS
        and payload["component_status"] == PASS_STATUS
        and payload["scientific_licensing_enabled"] is False
        and payload["passed"] is True
        and payload["failures"] == []
        and payload["milestone_status"] is None
        and payload["theorem_status"] is None
        and payload["final_status"] is None,
        "V2 static checker status/authority",
    )


def verify_checker(project_root: Path | str, result_root: Path | str) -> dict[str, Any]:
    replay = replay_formal_static_archive(project_root, result_root, checker_present=True)
    result = _fixed_result_root(require_canonical_absolute_path(project_root, "V2 project root"), result_root)
    path = result / V2_CHECKER_OUTPUT
    raw = read_pinned_regular_bytes(path)
    payload = _compact_object(raw, path, "V2 static checker")
    validate_checker_payload(payload, _checker_payload_from_replay(replay))
    require(read_pinned_regular_bytes(path) == raw, "V2 static checker changed before terminal replay")
    return {
        "verification_status": "PASS_STATIC_CHECKER_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(raw), "size_bytes": len(raw),
        "promotion_authorized": False, "artifacts_written": False,
    }


def _postcheck_payload_from_replay(
    replay: Mapping[str, Any],
    checker_raw: bytes,
) -> dict[str, Any]:
    return {
        "schema_version": 1, "protocol_id": PROTOCOL_ID,
        "artifact_role": "STATIC_POSTCHECK", "authority": "POSTCHECK_ONLY",
        "postcheck_status": FORMAL_POSTCHECK_STATUS, "passed": True,
        "checker_path": V2_CHECKER_OUTPUT, "checker_sha256": sha256_bytes(checker_raw),
        "main_freeze_sha256": replay["main_freeze_sha256"],
        "run_config_sha256": replay["run_config_sha256"],
        "bound_artifacts": {
            "aggregate_summary": {
                "path": "static/aggregate_summary.json",
                "sha256": replay["aggregate_summary_sha256"],
                "size_bytes": replay["aggregate_summary_size_bytes"],
            },
            "aggregate_manifest": {
                "path": "static/aggregate_manifest.json",
                "sha256": replay["aggregate_manifest_sha256"],
                "size_bytes": replay["aggregate_manifest_size_bytes"],
            },
            "ordered_cell_manifest_root": replay["ordered_cell_manifest_root"],
        },
        "replay_counts": replay["replay_counts"], "failures": [],
        "scientific_licensing_enabled": False,
        "claim_boundary": FORMAL_POSTCHECK_CLAIM_BOUNDARY,
        "component_status": PASS_STATUS, "milestone_status": None,
        "theorem_status": None, "final_status": None,
    }


def build_postcheck_payload(project_root: Path | str, result_root: Path | str) -> dict[str, Any]:
    replay = replay_formal_static_archive(project_root, result_root, checker_present=True)
    result = _fixed_result_root(require_canonical_absolute_path(project_root, "V2 project root"), result_root)
    checker_path = result / V2_CHECKER_OUTPUT
    checker_raw = read_pinned_regular_bytes(checker_path)
    checker = _compact_object(checker_raw, checker_path, "V2 static checker")
    validate_checker_payload(checker, _checker_payload_from_replay(replay))
    return _postcheck_payload_from_replay(replay, checker_raw)


def validate_postcheck_payload(payload: Any, expected: Mapping[str, Any]) -> None:
    require(type(payload) is dict, "V2 static postcheck: object required")
    exact_keys(payload, FORMAL_POSTCHECK_KEYS, "V2 static postcheck")
    exact_keys(expected, FORMAL_POSTCHECK_KEYS, "V2 static expected postcheck")
    require_json_exact(payload, dict(expected), "V2 static postcheck exact replay")
    require(
        payload["postcheck_status"] == FORMAL_POSTCHECK_STATUS
        and payload["passed"] is True
        and payload["scientific_licensing_enabled"] is False
        and payload["component_status"] == PASS_STATUS
        and payload["milestone_status"] is None
        and payload["theorem_status"] is None
        and payload["final_status"] is None
        and payload["failures"] == [],
        "V2 static postcheck status/authority",
    )
    exact_keys(payload["bound_artifacts"], {"aggregate_summary", "aggregate_manifest", "ordered_cell_manifest_root"}, "V2 static postcheck bound artifacts")
    for name in ("aggregate_summary", "aggregate_manifest"):
        exact_keys(payload["bound_artifacts"][name], {"path", "sha256", "size_bytes"}, f"V2 static postcheck {name}")


def verify_postcheck(project_root: Path | str, result_root: Path | str) -> dict[str, Any]:
    replay = replay_formal_static_archive(
        project_root, result_root, checker_present=True, postcheck_present=True
    )
    result = _fixed_result_root(require_canonical_absolute_path(project_root, "V2 project root"), result_root)
    checker_path = result / V2_CHECKER_OUTPUT
    checker_raw = read_pinned_regular_bytes(checker_path)
    checker = _compact_object(checker_raw, checker_path, "V2 static checker")
    validate_checker_payload(checker, _checker_payload_from_replay(replay))
    path = result / V2_POSTCHECK_OUTPUT
    raw = read_pinned_regular_bytes(path)
    payload = _compact_object(raw, path, "V2 static postcheck")
    validate_postcheck_payload(payload, _postcheck_payload_from_replay(replay, checker_raw))
    require(read_pinned_regular_bytes(checker_path) == checker_raw and read_pinned_regular_bytes(path) == raw, "V2 static postcheck chain changed before terminal replay")
    return {
        "verification_status": "PASS_STATIC_POSTCHECK_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(raw), "size_bytes": len(raw),
        "promotion_authorized": False, "artifacts_written": False,
    }


PUBLICATION_AUTHORITY = "ROLE20_STATIC_CHECKER_PUBLICATION_ONLY"
PUBLICATION_MAX_BYTES = 1024 * 1024
_RENAME_NOREPLACE = 1


@dataclass(frozen=True)
class CandidateSnapshot:
    path: Path
    raw: bytes
    identity: tuple[int, int, int, int, int, int, int, int, int]
    parent_identity: tuple[int, int, int, int]
    parent_chain: _ParentChainIdentity


def _publication_hook(_point: str) -> None:
    """Tests may replace this no-op to model a bounded crash point."""


def _file_identity(info: os.stat_result) -> tuple[int, int, int, int, int, int, int]:
    return (
        info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
        info.st_size, info.st_mtime_ns, info.st_ctime_ns,
    )


def _directory_chain(path: Path) -> tuple[tuple[str, int, int, int], ...]:
    path = require_canonical_absolute_path(path, "V2 publication directory")
    rows: list[tuple[str, int, int, int]] = []
    current = Path("/")
    for part in path.parts[1:]:
        current /= part
        info = os.stat(current, follow_symlinks=False)
        require(stat.S_ISDIR(info.st_mode), f"V2 publication ancestor is not a directory: {current}")
        rows.append((str(current), info.st_dev, info.st_ino, info.st_mode))
    return tuple(rows)


def _read_fd_exact(
    descriptor: int,
    maximum_bytes: int,
    context: str,
) -> tuple[bytes, os.stat_result]:
    before = os.fstat(descriptor)
    require(
        stat.S_ISREG(before.st_mode)
        and before.st_nlink == 1
        and 0 <= before.st_size <= maximum_bytes,
        f"{context}: bounded unaliased regular inode required",
    )
    chunks: list[bytes] = []
    total = 0
    while True:
        chunk = os.pread(
            descriptor,
            min(1024 * 1024, maximum_bytes + 1 - total),
            total,
        )
        if not chunk:
            break
        chunks.append(chunk)
        total += len(chunk)
        require(total <= maximum_bytes, f"{context}: byte cap exceeded")
    after = os.fstat(descriptor)
    raw = b"".join(chunks)
    require(
        _file_identity(before) == _file_identity(after)
        and len(raw) == before.st_size,
        f"{context}: inode changed or read was short",
    )
    return raw, after


def _write_all(descriptor: int, raw: bytes) -> None:
    view = memoryview(raw)
    while view:
        written = os.write(descriptor, view)
        require(written > 0, "V2 static publication short write")
        view = view[written:]


def _destination_absent(parent_fd: int, name: str) -> None:
    try:
        os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    raise CheckError("V2 static publication destination already exists")


def _rename_noreplace(parent_fd: int, source: str, destination: str) -> None:
    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = getattr(libc, "renameat2", None)
    require(renameat2 is not None, "Linux renameat2(RENAME_NOREPLACE) is unavailable")
    renameat2.argtypes = [
        ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    ctypes.set_errno(0)
    result = renameat2(
        parent_fd, os.fsencode(source), parent_fd, os.fsencode(destination),
        _RENAME_NOREPLACE,
    )
    if result == 0:
        return
    code = ctypes.get_errno()
    if code in {errno.EEXIST, errno.ENOTEMPTY}:
        raise CheckError("V2 static publication destination already exists")
    raise CheckError(f"V2 static renameat2 publication failed: errno={code}")


def _formal_base_identity_signature(
    root: Path,
    result: Path,
    *,
    checker_input: bool,
) -> tuple[tuple[str, tuple[int, int, int, int, int, int, int]], ...]:
    paths = [
        _project_file(root, V2_MAIN_RELATIVE),
        *(_project_file(root, relative) for _role, relative in INPUT_ROLES),
        result / "run_config.json",
        result / "static/aggregate_summary.json",
        result / "static/aggregate_manifest.json",
    ]
    for bits in PRECISIONS:
        for slab in SLABS:
            paths.append(result / "static/cell_manifests" / str(bits) / f"{slab}.json")
            cell = result / "static/cells" / str(bits) / slab
            paths.extend(cell / name for name in sorted(FORMAL_STATIC_FILE_NAMES))
    if checker_input:
        paths.append(result / V2_CHECKER_OUTPUT)
    rows: list[tuple[str, tuple[int, int, int, int, int, int, int]]] = []
    for path in paths:
        info = os.stat(path, follow_symlinks=False)
        require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1, f"V2 authority identity is not one regular inode: {path}")
        rows.append((str(path), _file_identity(info)))
    return tuple(rows)


def _checker_publication_state(
    root: Path,
    result: Path,
    *,
    transient: PublicationTransient | None,
    published: bool,
) -> tuple[bytes, tuple[tuple[str, tuple[int, int, int, int, int, int, int]], ...]]:
    replay = replay_formal_static_archive(
        root, result, checker_present=published, transient=transient
    )
    raw = canonical_json_bytes(_checker_payload_from_replay(replay))
    return raw, _formal_base_identity_signature(root, result, checker_input=False)


def _postcheck_publication_state(
    root: Path,
    result: Path,
    *,
    transient: PublicationTransient | None,
    published: bool,
) -> tuple[bytes, tuple[tuple[str, tuple[int, int, int, int, int, int, int]], ...]]:
    replay = replay_formal_static_archive(
        root, result, checker_present=True,
        postcheck_present=published, transient=transient,
    )
    checker_path = result / V2_CHECKER_OUTPUT
    checker_raw = read_pinned_regular_bytes(checker_path)
    checker_payload = _compact_object(checker_raw, checker_path, "V2 static checker")
    validate_checker_payload(checker_payload, _checker_payload_from_replay(replay))
    raw = canonical_json_bytes(_postcheck_payload_from_replay(replay, checker_raw))
    return raw, _formal_base_identity_signature(root, result, checker_input=True)


def _replay_stage(
    parent_fd: int,
    name: str,
    raw: bytes,
    identity: tuple[int, int],
    context: str,
) -> None:
    descriptor = os.open(
        name,
        os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0),
        dir_fd=parent_fd,
    )
    try:
        observed, info = _read_fd_exact(descriptor, len(raw), context)
    finally:
        os.close(descriptor)
    require(
        observed == raw
        and (info.st_dev, info.st_ino) == identity
        and stat.S_IMODE(info.st_mode) == 0o644
        and info.st_nlink == 1,
        f"{context}: byte/inode/mode contract mismatch",
    )


def _publish_no_replace(
    path: Path,
    raw: bytes,
    *,
    project_root: Path | None = None,
    revalidate: Callable[[PublicationTransient | None], bytes] | None = None,
) -> None:
    """One locked, terminally replayed Linux RENAME_NOREPLACE edge."""

    path = require_canonical_absolute_path(path, "V2 static publication path")
    require(type(raw) is bytes and 0 < len(raw) <= PUBLICATION_MAX_BYTES, "V2 static publication byte cap")
    parent = path.parent
    parent_chain = _directory_chain(parent)
    root_chain = _directory_chain(project_root) if project_root is not None else None
    parent_fd = _open_directory_fd(parent)
    parent_before = os.fstat(parent_fd)
    stage_name: str | None = None
    stage_fd: int | None = None
    stage_identity: tuple[int, int] | None = None
    renamed = False
    primary_error: BaseException | None = None
    cleanup_error: BaseException | None = None

    def transient() -> PublicationTransient:
        require(stage_name is not None and stage_identity is not None, "V2 static transient unavailable")
        return PublicationTransient(
            parent=parent, name=stage_name,
            device_id=stage_identity[0], inode=stage_identity[1], raw=raw,
        )

    def replay_parent(context: str) -> None:
        require(_directory_chain(parent) == parent_chain, f"{context}: lexical parent chain changed")
        opened = os.fstat(parent_fd)
        require(
            (opened.st_dev, opened.st_ino, opened.st_mode)
            == (parent_before.st_dev, parent_before.st_ino, parent_before.st_mode),
            f"{context}: pinned parent inode changed",
        )
        if project_root is not None:
            require(_directory_chain(project_root) == root_chain, f"{context}: authority root chain changed")

    try:
        replay_parent("V2 static publication open")
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise CheckError("V2 static publication parent is locked by another writer") from error
        _destination_absent(parent_fd, path.name)
        for _attempt in range(32):
            proposed = f".{path.name}.publish-{secrets.token_hex(16)}"
            try:
                stage_fd = os.open(
                    proposed,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL
                    | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0),
                    0o600,
                    dir_fd=parent_fd,
                )
            except FileExistsError:
                continue
            stage_name = proposed
            opened = os.fstat(stage_fd)
            stage_identity = (opened.st_dev, opened.st_ino)
            require(
                stat.S_ISREG(opened.st_mode)
                and stat.S_IMODE(opened.st_mode) == 0o600
                and opened.st_nlink == 1 and opened.st_size == 0,
                "V2 static new stage is not private empty regular inode",
            )
            break
        require(stage_fd is not None and stage_name is not None and stage_identity is not None, "V2 static publication staging collision exhaustion")
        _write_all(stage_fd, raw)
        _publication_hook("AFTER_STAGE_WRITE")
        os.fchmod(stage_fd, 0o644)
        os.fsync(stage_fd)
        _publication_hook("AFTER_STAGE_FILE_FSYNC")
        staged = os.fstat(stage_fd)
        require(
            (staged.st_dev, staged.st_ino) == stage_identity
            and stat.S_ISREG(staged.st_mode)
            and stat.S_IMODE(staged.st_mode) == 0o644
            and staged.st_nlink == 1 and staged.st_size == len(raw),
            "V2 static stage inode contract mismatch",
        )
        _replay_stage(parent_fd, stage_name, raw, stage_identity, "V2 static staged replay")
        os.fsync(parent_fd)
        _publication_hook("AFTER_STAGING_PARENT_FSYNC")

        if revalidate is not None:
            require(revalidate(transient()) == raw, "V2 static terminal authority changed candidate")
        replay_parent("V2 static terminal publication")
        _replay_stage(parent_fd, stage_name, raw, stage_identity, "V2 static terminal stage")
        _destination_absent(parent_fd, path.name)
        _publication_hook("BEFORE_RENAME")
        if revalidate is not None:
            require(revalidate(transient()) == raw, "V2 static immediate-prerename authority changed candidate")
        replay_parent("V2 static immediate-prerename publication")
        _replay_stage(parent_fd, stage_name, raw, stage_identity, "V2 static immediate-prerename stage")
        _destination_absent(parent_fd, path.name)
        _rename_noreplace(parent_fd, stage_name, path.name)
        renamed = True
        _publication_hook("AFTER_RENAME")

        published_fd = os.open(
            path.name,
            os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
        try:
            published_raw, published_info = _read_fd_exact(
                published_fd, len(raw), "V2 static published inode"
            )
            lexical = os.stat(path, follow_symlinks=False)
            require(
                published_raw == raw
                and (published_info.st_dev, published_info.st_ino) == stage_identity
                and _file_identity(lexical) == _file_identity(published_info)
                and stat.S_IMODE(published_info.st_mode) == 0o644
                and published_info.st_nlink == 1,
                "V2 static published inode/byte replay mismatch",
            )
            os.fsync(published_fd)
        finally:
            os.close(published_fd)
        _publication_hook("AFTER_DESTINATION_FSYNC")
        os.fsync(parent_fd)
        _publication_hook("AFTER_PUBLICATION_PARENT_FSYNC")
        replay_parent("V2 static postpublication")
        _replay_stage(parent_fd, path.name, raw, stage_identity, "V2 static postpublication replay")
        _publication_hook("AFTER_POSTPUBLICATION_REPLAY")
        if revalidate is not None:
            require(revalidate(None) == raw, "V2 static postpublication authority envelope changed")
        replay_parent("V2 static ultimate publication")
        _replay_stage(parent_fd, path.name, raw, stage_identity, "V2 static ultimate replay")
    except BaseException as error:
        primary_error = error
    finally:
        if stage_identity is None and stage_fd is not None:
            try:
                info = os.fstat(stage_fd)
                stage_identity = (info.st_dev, info.st_ino)
            except BaseException as error:
                cleanup_error = cleanup_error or error
        if stage_fd is not None:
            try:
                os.close(stage_fd)
            except BaseException as error:
                cleanup_error = cleanup_error or error
        if not renamed and stage_name is not None and stage_identity is not None:
            try:
                current = os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
                if (current.st_dev, current.st_ino) != stage_identity:
                    raise CheckError("V2 static refused to unlink replaced foreign stage inode")
                os.unlink(stage_name, dir_fd=parent_fd)
                os.fsync(parent_fd)
            except FileNotFoundError:
                pass
            except BaseException as error:
                cleanup_error = cleanup_error or error
        try:
            os.close(parent_fd)
        except BaseException as error:
            cleanup_error = cleanup_error or error
    if cleanup_error is not None:
        if primary_error is not None:
            raise cleanup_error from primary_error
        raise cleanup_error
    if primary_error is not None:
        raise primary_error


def _owned_candidate_parent(
    candidate: Path,
    *,
    expected_leaf: str,
    before_write: bool,
) -> tuple[int, int, int, int]:
    candidate = require_canonical_absolute_path(candidate, "V2 static candidate")
    require(
        candidate.parent.parent == Path("/tmp")
        and len(candidate.parts) == 4
        and candidate.name == expected_leaf,
        "V2 static candidate must be exact /tmp/<owned-dir>/<fixed-leaf>",
    )
    parent_fd = _open_directory_fd(candidate.parent)
    try:
        info = os.fstat(parent_fd)
        require(
            info.st_uid == os.geteuid()
            and stat.S_IMODE(info.st_mode) == 0o700
            and info.st_nlink == 2,
            "V2 static candidate parent must be euid-owned 0700 nlink2",
        )
        entries = tuple(sorted(os.listdir(parent_fd)))
        expected = () if before_write else (expected_leaf,)
        require(entries == expected, "V2 static candidate parent must be empty/singleton")
        return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink)
    finally:
        os.close(parent_fd)


def _replay_candidate(snapshot: CandidateSnapshot, *, expected_leaf: str) -> None:
    parent = _owned_candidate_parent(
        snapshot.path, expected_leaf=expected_leaf, before_write=False
    )
    require(parent == snapshot.parent_identity, "V2 static candidate parent identity changed")
    pinned = _read_pinned_regular_snapshot(
        snapshot.path,
        maximum_bytes=PUBLICATION_MAX_BYTES,
        context="V2 static candidate",
    )
    require(
        pinned.raw == snapshot.raw
        and _stable_stat_identity(pinned.info) == snapshot.identity
        and pinned.parent_chain == snapshot.parent_chain
        and stat.S_IMODE(pinned.info.st_mode) == 0o600
        and pinned.info.st_nlink == 1,
        "V2 static candidate inode/byte/mode changed",
    )


def _read_candidate(path: Path, *, expected_leaf: str) -> CandidateSnapshot:
    parent = _owned_candidate_parent(path, expected_leaf=expected_leaf, before_write=False)
    pinned = _read_pinned_regular_snapshot(
        path,
        maximum_bytes=PUBLICATION_MAX_BYTES,
        context="V2 static candidate",
    )
    pinned_parent = pinned.parent_chain[-1]
    require(
        pinned_parent[1:5]
        == (parent[0], parent[1], parent[2], parent[3])
        and stat.S_IMODE(pinned.info.st_mode) == 0o600
        and pinned.info.st_nlink == 1,
        "V2 static candidate must be regular 0600 nlink1",
    )
    snapshot = CandidateSnapshot(
        path,
        pinned.raw,
        _stable_stat_identity(pinned.info),
        parent,
        pinned.parent_chain,
    )
    _replay_candidate(snapshot, expected_leaf=expected_leaf)
    return snapshot


def _write_private_candidate(
    path: Path,
    raw: bytes,
    *,
    expected_leaf: str,
    revalidate: Callable[[], bytes],
) -> CandidateSnapshot:
    require(type(raw) is bytes and 0 < len(raw) <= PUBLICATION_MAX_BYTES, "V2 static candidate byte cap")
    parent_identity = _owned_candidate_parent(
        path, expected_leaf=expected_leaf, before_write=True
    )
    parent_fd, parent_chain = _open_directory_fd_with_chain(path.parent)
    descriptor: int | None = None
    identity: tuple[int, int] | None = None
    primary_error: BaseException | None = None
    cleanup_error: BaseException | None = None
    try:
        require(
            (lambda info: (info.st_dev, info.st_ino, info.st_mode, info.st_nlink))(os.fstat(parent_fd))
            == parent_identity,
            "V2 static candidate parent open race",
        )
        descriptor = os.open(
            path.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NONBLOCK
            | getattr(os, "O_NOFOLLOW", 0),
            0o600,
            dir_fd=parent_fd,
        )
        opened = os.fstat(descriptor)
        identity = (opened.st_dev, opened.st_ino)
        require(
            stat.S_ISREG(opened.st_mode)
            and stat.S_IMODE(opened.st_mode) == 0o600
            and opened.st_nlink == 1 and opened.st_size == 0,
            "V2 static candidate creation contract mismatch",
        )
        _write_all(descriptor, raw)
        os.fsync(descriptor)
        os.fsync(parent_fd)
        written = os.fstat(descriptor)
        require(
            (written.st_dev, written.st_ino) == identity
            and stat.S_IMODE(written.st_mode) == 0o600
            and written.st_nlink == 1 and written.st_size == len(raw),
            "V2 static candidate write changed inode",
        )
        snapshot = CandidateSnapshot(
            path,
            raw,
            _stable_stat_identity(written),
            parent_identity,
            parent_chain,
        )
        _replay_candidate(snapshot, expected_leaf=expected_leaf)
        _publication_hook("AFTER_CANDIDATE_WRITE")
        require(revalidate() == raw, "V2 static candidate authority changed after write")
        _publication_hook("AFTER_CANDIDATE_TERMINAL_REPLAY")
        require(revalidate() == raw, "V2 static candidate final authority changed")
        _replay_candidate(snapshot, expected_leaf=expected_leaf)
        return snapshot
    except BaseException as error:
        primary_error = error
    finally:
        if descriptor is not None:
            try:
                os.close(descriptor)
            except BaseException as error:
                cleanup_error = cleanup_error or error
        if primary_error is not None and identity is not None:
            try:
                current = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
                if (current.st_dev, current.st_ino) != identity:
                    raise CheckError("V2 static refused to unlink replaced foreign candidate")
                os.unlink(path.name, dir_fd=parent_fd)
                os.fsync(parent_fd)
            except FileNotFoundError:
                pass
            except BaseException as error:
                cleanup_error = cleanup_error or error
        try:
            os.close(parent_fd)
        except BaseException as error:
            cleanup_error = cleanup_error or error
    if cleanup_error is not None:
        if primary_error is not None:
            raise cleanup_error from primary_error
        raise cleanup_error
    assert primary_error is not None
    raise primary_error


def build_checker_candidate(
    project_root: Path | str,
    result_root: Path | str,
    candidate_path: Path | str,
) -> dict[str, Any]:
    root = require_canonical_absolute_path(project_root, "V2 project root")
    result = _fixed_result_root(root, result_root)
    candidate = require_canonical_absolute_path(candidate_path, "V2 static checker candidate")
    raw, identities = _checker_publication_state(root, result, transient=None, published=False)

    def terminal() -> bytes:
        replay_raw, replay_identities = _checker_publication_state(root, result, transient=None, published=False)
        require(replay_identities == identities, "V2 static input generation inode changed")
        return replay_raw

    snapshot = _write_private_candidate(
        candidate, raw, expected_leaf=V2_CHECKER_OUTPUT, revalidate=terminal
    )
    return {
        "candidate_status": "BUILT_PRIVATE_CHECKER_CANDIDATE",
        "authority": "NON_AUTHORITATIVE_CANDIDATE_ONLY",
        "candidate_path": str(snapshot.path),
        "candidate_sha256": sha256_bytes(snapshot.raw),
        "size_bytes": len(snapshot.raw), "mode": "0600", "nlink": 1,
        "artifacts_written_to_canonical_root": False,
    }


def publish_checker(
    project_root: Path | str,
    result_root: Path | str,
    candidate_path: Path | str,
    *,
    expected_sha256: str,
    authority: str,
) -> dict[str, Any]:
    require(authority == PUBLICATION_AUTHORITY, "V2 static publication authority literal mismatch")
    _exact_sha(expected_sha256, "V2 static expected checker candidate hash")
    root = require_canonical_absolute_path(project_root, "V2 project root")
    result = _fixed_result_root(root, result_root)
    candidate = require_canonical_absolute_path(candidate_path, "V2 static checker candidate")
    snapshot = _read_candidate(candidate, expected_leaf=V2_CHECKER_OUTPUT)
    require(sha256_bytes(snapshot.raw) == expected_sha256, "V2 static candidate intent hash mismatch")
    expected_raw, identities = _checker_publication_state(root, result, transient=None, published=False)
    require(snapshot.raw == expected_raw, "V2 static candidate differs from full authority replay")

    def terminal(transient: PublicationTransient | None) -> bytes:
        _replay_candidate(snapshot, expected_leaf=V2_CHECKER_OUTPUT)
        replay_raw, replay_identities = _checker_publication_state(
            root, result, transient=transient, published=transient is None
        )
        require(replay_identities == identities, "V2 static source/archive inode generation changed")
        return replay_raw

    _publish_no_replace(
        result / V2_CHECKER_OUTPUT, snapshot.raw,
        project_root=root, revalidate=terminal,
    )
    return verify_checker(root, result)


def build_postcheck_candidate(
    project_root: Path | str,
    result_root: Path | str,
    candidate_path: Path | str,
) -> dict[str, Any]:
    root = require_canonical_absolute_path(project_root, "V2 project root")
    result = _fixed_result_root(root, result_root)
    candidate = require_canonical_absolute_path(candidate_path, "V2 static postcheck candidate")
    raw, identities = _postcheck_publication_state(root, result, transient=None, published=False)

    def terminal() -> bytes:
        replay_raw, replay_identities = _postcheck_publication_state(root, result, transient=None, published=False)
        require(replay_identities == identities, "V2 static postcheck input inode generation changed")
        return replay_raw

    snapshot = _write_private_candidate(
        candidate, raw, expected_leaf=V2_POSTCHECK_OUTPUT, revalidate=terminal
    )
    return {
        "candidate_status": "BUILT_PRIVATE_POSTCHECK_CANDIDATE",
        "authority": "NON_AUTHORITATIVE_CANDIDATE_ONLY",
        "candidate_path": str(snapshot.path),
        "candidate_sha256": sha256_bytes(snapshot.raw),
        "size_bytes": len(snapshot.raw), "mode": "0600", "nlink": 1,
        "artifacts_written_to_canonical_root": False,
    }


def publish_postcheck(
    project_root: Path | str,
    result_root: Path | str,
    candidate_path: Path | str,
    *,
    expected_sha256: str,
    authority: str,
) -> dict[str, Any]:
    require(authority == PUBLICATION_AUTHORITY, "V2 static publication authority literal mismatch")
    _exact_sha(expected_sha256, "V2 static expected postcheck candidate hash")
    root = require_canonical_absolute_path(project_root, "V2 project root")
    result = _fixed_result_root(root, result_root)
    candidate = require_canonical_absolute_path(candidate_path, "V2 static postcheck candidate")
    snapshot = _read_candidate(candidate, expected_leaf=V2_POSTCHECK_OUTPUT)
    require(sha256_bytes(snapshot.raw) == expected_sha256, "V2 static postcheck candidate intent hash mismatch")
    expected_raw, identities = _postcheck_publication_state(root, result, transient=None, published=False)
    require(snapshot.raw == expected_raw, "V2 static postcheck candidate differs from full authority replay")

    def terminal(transient: PublicationTransient | None) -> bytes:
        _replay_candidate(snapshot, expected_leaf=V2_POSTCHECK_OUTPUT)
        replay_raw, replay_identities = _postcheck_publication_state(
            root, result, transient=transient, published=transient is None
        )
        require(replay_identities == identities, "V2 static postcheck source/archive inode generation changed")
        return replay_raw

    _publish_no_replace(
        result / V2_POSTCHECK_OUTPUT, snapshot.raw,
        project_root=root, revalidate=terminal,
    )
    return verify_postcheck(root, result)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--verify-main-freeze", type=canonical_absolute_argument)
    modes.add_argument("--build-checker-candidate", type=canonical_absolute_argument)
    modes.add_argument("--publish-checker-candidate", type=canonical_absolute_argument)
    modes.add_argument("--verify-checker", action="store_true", help="read-only role 58 replay")
    modes.add_argument("--build-postcheck-candidate", type=canonical_absolute_argument)
    modes.add_argument("--publish-postcheck-candidate", type=canonical_absolute_argument)
    modes.add_argument("--verify-postcheck", action="store_true", help="read-only role 59 replay")
    parser.add_argument(
        "--project-root", type=canonical_absolute_argument,
        default=require_canonical_absolute_path(ROOT, "default project root"),
    )
    parser.add_argument("--result-root", type=canonical_absolute_argument)
    parser.add_argument("--publication-authority")
    parser.add_argument("--expected-sha256")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        project_root = arguments.project_root
        result_root = arguments.result_root or _project_file(project_root, V2_RESULT_RELATIVE)
        publication_mode = (
            arguments.publish_checker_candidate is not None
            or arguments.publish_postcheck_candidate is not None
        )
        if publication_mode:
            require(arguments.publication_authority == PUBLICATION_AUTHORITY, "explicit fixed publication authority is required")
            require(arguments.expected_sha256 is not None, "publication requires an expected candidate SHA-256")
        else:
            require(arguments.publication_authority is None, "verify-only mode rejects publication authority")
            require(arguments.expected_sha256 is None, "nonpublication mode rejects an expected candidate SHA-256")
        if arguments.verify_main_freeze is not None:
            require(arguments.result_root is None, "main-freeze verify rejects a result-root argument")
            result = verify_formal_main_freeze_path(arguments.verify_main_freeze, project_root)
        elif arguments.build_checker_candidate is not None:
            result = build_checker_candidate(
                project_root, result_root, arguments.build_checker_candidate
            )
        elif arguments.publish_checker_candidate is not None:
            result = publish_checker(
                project_root, result_root, arguments.publish_checker_candidate,
                expected_sha256=arguments.expected_sha256,
                authority=arguments.publication_authority,
            )
        elif arguments.verify_checker:
            result = verify_checker(project_root, result_root)
        elif arguments.build_postcheck_candidate is not None:
            result = build_postcheck_candidate(
                project_root, result_root, arguments.build_postcheck_candidate
            )
        elif arguments.publish_postcheck_candidate is not None:
            result = publish_postcheck(
                project_root, result_root, arguments.publish_postcheck_candidate,
                expected_sha256=arguments.expected_sha256,
                authority=arguments.publication_authority,
            )
        else:
            result = verify_postcheck(project_root, result_root)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(canonical_json_bytes(result).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
