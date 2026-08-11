#!/usr/bin/env python3
"""Independently verify and publish the formal L3-A1 V2 release DAG.

This module is deliberately self contained.  It imports no scheduler,
evaluator, checker, adapter, or earlier release builder, and it never starts
a subprocess.  ``--verify-main-freeze`` and ``--verify-only`` are read-only.
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
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterator, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PROTOCOL_ID = "R401-VAL-L3-A1"
SCHEMA_VERSION = 1
RELEASE_CONTRACT = "write_once_exact_hash_dag_v1"
RELEASE_STATUS = "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"
CHECKER_STATUS = "PASS_INDEPENDENT_CHECKER"
POSTCHECK_STATUS = "PASS_WRITE_ONCE_POSTCHECK"
STATIC_COMPONENT_STATUS = "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
BRANCH_COMPONENT_STATUS = "PASS_BRANCH_TUBE_ALL_SLABS"
COMPOSITE_STATUS = "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"
RELEASE_NAME = "RELEASE_PROVENANCE.json"
RESULT_RELATIVE = PurePosixPath("results/r401_val_l3_a1_v2_all_slabs")
REPORT_NAME = "R401_VAL_L3_A1_REPORT.md"
REPORT_RELATIVE = RESULT_RELATIVE / REPORT_NAME
MAIN_FREEZE_RELATIVE = PurePosixPath(
    "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json"
)
OPERATIONAL_SUFFIX = ".operational"
QUARANTINE_JOURNAL_SUFFIX = ".quarantine-transaction.json"
PREFREEZE_ACCEPT_RAW = b"Verdict: ACCEPT_FOR_FREEZE\n"
# Publication remains an explicit future operator action.  These immutable
# purpose-separated literals avoid any later source edit/self-hash cycle;
# merely possessing the implementation never supplies either authorization.
EXPECTED_MAIN_PUBLICATION_AUTHORITY = "ROLE24_MAIN_FREEZE_PUBLICATION_ONLY"
EXPECTED_REPORT_PUBLICATION_AUTHORITY = "ROLE24_REPORT_PUBLICATION_ONLY"
EXPECTED_RELEASE_PUBLICATION_AUTHORITY = "ROLE24_RELEASE_PROVENANCE_PUBLICATION_ONLY"
PUBLICATION_METHOD = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
HEX_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
SLABS = tuple(f"S{index:03d}" for index in range(51))
PRECISIONS = (128, 256)
MAIN_CHECKER_RECEIPT_ROLES = ("static", "branch", "composite")
MAIN_CHECKER_RECEIPT_KEYS = {
    "verification_status", "authority", "candidate_sha256",
    "input_map_sha256", "size_bytes", "promotion_authorized",
    "artifacts_written",
}
REPORT_VERIFY_RECEIPT_KEYS = {
    "verification_status", "authority", "candidate_sha256",
    "ordered_upstream_roles_sha256", "size_bytes", "promotion_authorized",
    "artifacts_written",
}
PUBLICATION_RECEIPT_COMMON_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "candidate", "canonical", "publication_method",
    "independent_postpublication_verification_performed",
    "scientific_licensing_enabled", "production_authorized",
    "scientific_dispatch_performed", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
MAIN_PUBLICATION_RECEIPT_KEYS = PUBLICATION_RECEIPT_COMMON_KEYS | {
    "input_role_count", "ordered_input_roles_sha256",
    "checker_receipt_sha256",
}
REPORT_PUBLICATION_RECEIPT_KEYS = PUBLICATION_RECEIPT_COMMON_KEYS | {
    "upstream_role_count", "ordered_upstream_roles_sha256",
    "archive_generation_sha256",
}
RELEASE_PUBLICATION_RECEIPT_KEYS = PUBLICATION_RECEIPT_COMMON_KEYS | {
    "role_count", "ordered_roles_sha256", "main_freeze_sha256",
    "archive_generation_sha256",
}
PUBLICATION_FILE_BINDING_KEYS = {
    "path", "sha256", "size_bytes", "mode", "nlink", "fingerprint",
}
PUBLICATION_FINGERPRINT_KEYS = {
    "device_id", "inode", "size_bytes", "mtime_ns", "ctime_ns", "mode",
    "nlink",
}
MAIN_PUBLICATION_CLAIM_BOUNDARY = (
    "role-24 write-once transport evidence for the exact role-54 main freeze "
    "only; no independent postpublication verification, scientific licensing, "
    "production authorization, promotion, or dispatch authority"
)
REPORT_PUBLICATION_CLAIM_BOUNDARY = (
    "role-24 write-once transport evidence for the exact role-68 five-line "
    "report only; no independent postpublication verification, scientific "
    "licensing, production authorization, promotion, or dispatch authority"
)
RELEASE_PUBLICATION_CLAIM_BOUNDARY = (
    "role-24 write-once transport evidence for the exact 68-role release "
    "provenance only; no independent postpublication verification, scientific "
    "licensing, production authorization, promotion, or dispatch authority"
)

MAIN_FREEZE_CLAIM_BOUNDARY = (
    "exact control-plane and ordered 53-role pre-freeze authority only; no "
    "evaluator result, component status, theorem, Hilbert-Polya, zeta-zero, or RH claim"
)
RUN_CONFIG_CLAIM_BOUNDARY = (
    "write-once formal run binding only; the artifact never self-authorizes "
    "scientific dispatch or any component, theorem, Hilbert-Polya, zeta-zero, or RH claim"
)
AGGREGATE_CLAIM_BOUNDARY = (
    "complete 102-cell producer archive only; independent component replay "
    "remains required and no component, theorem, Hilbert-Polya, zeta-zero, or RH status is assigned"
)
STATIC_CELL_CLAIM_BOUNDARY = (
    "producer-only static phase-anchor cell conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no component, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
BRANCH_CELL_CLAIM_BOUNDARY = (
    "accepted-branch complete-period tube cell only; no arbitrary-candidate "
    "tube routing, global uniqueness, trace, Hilbert--Polya, zeta, or RH claim"
)
RELEASE_CLAIM_BOUNDARY = (
    "complete-period local-tube candidate uniqueness modulo time translation "
    "and distinguished-branch tube membership only; no global routing, "
    "trace-formula, Hilbert-Polya, zeta-zero, or RH promotion"
)
STATIC_CHECKER_CLAIM_BOUNDARY = (
    "all-slab static phase-anchor component only, conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no branch-tube, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
BRANCH_CHECKER_CLAIM_BOUNDARY = (
    "all-slab distinguished-branch complete-period tube component only; no "
    "static phase-anchor, composite, global-orbit, trace-formula, "
    "Hilbert--Polya, zeta-zero, or RH authority"
)
STATIC_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the formal 102-cell static checker chain only; "
    "no authority beyond PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
)
BRANCH_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the formal 102-cell branch checker chain only; "
    "no authority beyond PASS_BRANCH_TUBE_ALL_SLABS"
)
COMPOSITE_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the formal composite checker chain only; no "
    "authority beyond PASS_LOCAL_PHASE_TUBE_ALL_SLABS"
)
REPORT_EXACT_RAW = (
    f"Status: {COMPOSITE_STATUS}\n"
    f"milestone_status = {COMPOSITE_STATUS}\n"
    f"theorem_status = {COMPOSITE_STATUS}\n"
    "final_status = null\n"
    f"Claim boundary: {RELEASE_CLAIM_BOUNDARY}\n"
).encode("ascii")

ROLE5_CLAIM_BOUNDARY = (
    "independent withdrawal of control attempt 1 and acceptance of the reviewed "
    "V2 control implementation only; no machine, main freeze, result, theorem, "
    "release, initialization, promotion, or dispatch acceptance"
)
PREFREEZE_TEST_CLAIM_BOUNDARY = (
    "pre-freeze engineering test evidence only; no held-out or all-slab L3 result "
    "was read and no scientific evaluator was dispatched; no L3-A1 component, "
    "milestone, theorem, final, global tube-routing, trace-formula, Hilbert-Polya, "
    "zeta-zero, RH, or implication-toward-RH claim"
)
S0_COMPATIBILITY_CLAIM_BOUNDARY = (
    "read-only compatibility replay of the sealed representative 3x2 S0 archive "
    "only; non-licensing and no evaluator dispatch; no all-slab result, theorem "
    "promotion, global orbit exclusion, trace formula, Hilbert-Polya construction, "
    "zeta-zero result, or RH claim"
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
    ("static_checker_source", "scripts/check_r401_val_l3_a1_v2_static_independent.py"),
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
REPORT_UPSTREAM_ROLES: tuple[tuple[str, str], ...] = (
    ("main_freeze", MAIN_FREEZE_RELATIVE.as_posix()),
    *DOWNSTREAM_ROLES[:-1],
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
RELEASE_KEYS = {
    "schema_version", "protocol_id", "release_contract", "release_status",
    "authority", "scientific_licensing_enabled", "matrix_id",
    "main_freeze_sha256", "machine_freeze_sha256", "run_config_sha256",
    "archive_generation_sha256", "ordered_static_manifest_root",
    "ordered_branch_manifest_root", "roles", "component_chains",
    "composite_chain", "upstream_chains", "s0_compatibility",
    "claim_boundary", "milestone_status", "theorem_status", "final_status",
}


class ReleaseError(RuntimeError):
    """Base class for a fail-closed provenance rejection."""


class StrictJSONError(ReleaseError):
    pass


class PathContractError(ReleaseError):
    pass


@dataclass(frozen=True)
class Snapshot:
    path: Path
    raw: bytes
    fingerprint: tuple[int, ...]
    namespace: tuple[tuple[str, int, int, int], ...]


@dataclass(frozen=True)
class AuthoritySnapshot:
    project_root: Path
    input_roles: tuple[dict[str, str], ...]
    role_images: Mapping[str, bytes]
    main: Mapping[str, Any]
    main_raw: bytes
    main_path: Path


@dataclass(frozen=True)
class PublicationTransient:
    """The one invocation-owned same-parent inode allowed before rename."""

    parent: Path
    name: str
    device_id: int
    inode: int
    mode: int
    nlink: int
    raw: bytes


@dataclass(frozen=True)
class PublicationOutcome:
    """Terminal evidence returned only after the canonical inode replays."""

    canonical_path: Path
    canonical_sha256: str
    size_bytes: int
    fingerprint: tuple[int, ...]
    publication_method: str


@dataclass(frozen=True)
class MainCheckerReceiptSnapshot:
    """Pinned private role-20/21/22 verify-only receipt image."""

    path: Path
    raw: bytes
    fingerprint: tuple[int, ...]
    parent_identity: tuple[int, int, int, int]
    namespace: tuple[tuple[str, int, int, int], ...]
    payload: Mapping[str, Any]


_ACTIVE_SNAPSHOTS: dict[Path, Snapshot] | None = None
_ACTIVE_ABSENCES: dict[
    Path, tuple[str, tuple[tuple[str, int, int, int], ...]]
] | None = None
_ACTIVE_MACHINE_PATHS: dict[Path, tuple[tuple[int, ...], Path]] | None = None
_ACTIVE_MACHINE_MANIFEST_FILES: dict[Path, tuple[bytes, tuple[int, ...]]] | None = None
_ACTIVE_MACHINE_CAPD_NAMESPACES: dict[
    Path, tuple[frozenset[str], tuple[tuple[str, str, tuple[int, ...]], ...]]
] | None = None
_ACTIVE_MACHINE_CONDA_META_NAMESPACES: dict[Path, tuple[str, ...]] | None = None


def _fingerprint(info: os.stat_result) -> tuple[int, ...]:
    return (
        info.st_dev, info.st_ino, info.st_mode, info.st_nlink, info.st_size,
        info.st_mtime_ns, info.st_ctime_ns,
    )


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def exact_json_equal(left: Any, right: Any) -> bool:
    """JSON equality which does not admit Boolean/integer/float aliases."""

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


def require_sha256(value: Any, context: str) -> str:
    if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
        raise ReleaseError(f"{context} must be lowercase SHA-256")
    return value


def exact_int(value: Any, context: str, *, expected: int | None = None, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise StrictJSONError(f"{context} must be an exact integer >= {minimum}")
    if expected is not None and value != expected:
        raise StrictJSONError(f"{context} must equal {expected}")
    return value


def exact_keys(value: Any, expected: set[str], context: str) -> Mapping[str, Any]:
    if type(value) is not dict or set(value) != expected:
        actual = sorted(value) if type(value) is dict else type(value).__name__
        raise StrictJSONError(f"{context} key set mismatch: {actual}")
    return value


def _plain_json(value: Any, context: str = "$", active: set[int] | None = None) -> None:
    if value is None or type(value) in (str, bool, int):
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise StrictJSONError(f"nonfinite number at {context}")
        return
    if type(value) not in (dict, list):
        raise StrictJSONError(f"non-plain JSON value at {context}")
    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise StrictJSONError(f"cyclic JSON value at {context}")
    seen.add(identity)
    try:
        if type(value) is dict:
            for key, child in value.items():
                if type(key) is not str:
                    raise StrictJSONError(f"non-string JSON key at {context}")
                _plain_json(child, f"{context}.{key}", seen)
        else:
            for index, child in enumerate(value):
                _plain_json(child, f"{context}[{index}]", seen)
    finally:
        seen.remove(identity)


def canonical_json_bytes(value: Any) -> bytes:
    _plain_json(value)
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
        + "\n"
    ).encode("utf-8")


def pretty_json_bytes(value: Any) -> bytes:
    _plain_json(value)
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False)
        + "\n"
    ).encode("utf-8")


def branch_transaction_json_bytes(value: Any) -> bytes:
    return pretty_json_bytes(value)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJSONError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(raw: bytes, *, canonical: str | None = None) -> Any:
    try:
        text = raw.decode("utf-8")
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=lambda token: (_ for _ in ()).throw(
                StrictJSONError(f"nonfinite JSON token: {token}")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise StrictJSONError(f"malformed strict JSON: {error}") from error
    _plain_json(value)
    expected = canonical_json_bytes(value) if canonical == "compact" else (
        pretty_json_bytes(value) if canonical == "pretty" else None
    )
    if expected is not None and raw != expected:
        raise StrictJSONError(f"JSON is not {canonical} canonical")
    return value


def _sha1(raw: bytes) -> str:
    return hashlib.sha1(raw, usedforsecurity=False).hexdigest()


def _git_roots(project_root: Path) -> tuple[Path, Path, PurePosixPath]:
    """Find the enclosing ordinary Git directory without invoking Git."""

    root = lexical_absolute(project_root)
    candidate = root
    while True:
        marker = candidate / ".git"
        try:
            info = os.stat(marker, follow_symlinks=False)
        except FileNotFoundError:
            if candidate.parent == candidate:
                raise ReleaseError("authority root is not inside an ordinary Git repository")
            candidate = candidate.parent
            continue
        if not stat.S_ISDIR(info.st_mode):
            raise ReleaseError("Git indirection files and symlinked Git directories are rejected")
        relative = root.relative_to(candidate)
        prefix = PurePosixPath(relative.as_posix()) if relative.parts else PurePosixPath()
        return candidate, marker, prefix


def _inflate_git_stream(raw: bytes, context: str, *, cap: int = 1024 * 1024 * 1024) -> bytes:
    inflater = zlib.decompressobj()
    try:
        value = inflater.decompress(raw, cap + 1)
    except zlib.error as error:
        raise ReleaseError(f"{context}: malformed zlib stream") from error
    if not inflater.eof or inflater.unconsumed_tail or len(value) > cap:
        raise ReleaseError(f"{context}: incomplete or oversize zlib stream")
    return value


def _git_parse_framed(framed: bytes, oid: str, context: str) -> tuple[str, bytes]:
    if _sha1(framed) != oid:
        raise ReleaseError(f"{context}: Git object ID mismatch")
    try:
        header, payload = framed.split(b"\x00", 1)
        kind_raw, size_raw = header.split(b" ", 1)
        kind = kind_raw.decode("ascii")
        size = int(size_raw.decode("ascii"))
    except (ValueError, UnicodeError) as error:
        raise ReleaseError(f"{context}: malformed Git loose-object frame") from error
    if kind not in {"commit", "tree", "blob", "tag"} or str(size).encode() != size_raw or size != len(payload):
        raise ReleaseError(f"{context}: Git object kind/size mismatch")
    return kind, payload


def _git_pack_index(index_raw: bytes, context: str) -> tuple[dict[str, int], bytes]:
    if (
        len(index_raw) < 8 + 256 * 4 + 40
        or index_raw[:4] != b"\xfftOc"
        or struct.unpack_from(">I", index_raw, 4)[0] != 2
        or hashlib.sha1(index_raw[:-20], usedforsecurity=False).digest() != index_raw[-20:]
    ):
        raise ReleaseError(f"{context}: invalid v2 pack index/checksum")
    fanout = struct.unpack_from(">256I", index_raw, 8)
    if any(left > right for left, right in zip(fanout, fanout[1:])):
        raise ReleaseError(f"{context}: unordered pack fanout")
    count = fanout[-1]
    names_offset = 8 + 256 * 4
    crc_offset = names_offset + count * 20
    offsets_offset = crc_offset + count * 4
    large_offset = offsets_offset + count * 4
    if large_offset + 40 > len(index_raw):
        raise ReleaseError(f"{context}: truncated pack index")
    result: dict[str, int] = {}
    previous: bytes | None = None
    for index in range(count):
        raw_oid = index_raw[names_offset + 20 * index:names_offset + 20 * (index + 1)]
        if len(raw_oid) != 20 or (previous is not None and raw_oid <= previous):
            raise ReleaseError(f"{context}: unordered/duplicate object IDs")
        previous = raw_oid
        offset = struct.unpack_from(">I", index_raw, offsets_offset + 4 * index)[0]
        if offset & 0x80000000:
            location = large_offset + 8 * (offset & 0x7fffffff)
            if location + 8 > len(index_raw) - 40:
                raise ReleaseError(f"{context}: malformed large pack offset")
            offset = struct.unpack_from(">Q", index_raw, location)[0]
        result[raw_oid.hex()] = offset
    return result, index_raw[-40:-20]


def _git_delta_varint(raw: bytes, cursor: int, context: str) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        if cursor >= len(raw) or shift > 63:
            raise ReleaseError(f"{context}: malformed delta varint")
        current = raw[cursor]
        cursor += 1
        value |= (current & 0x7f) << shift
        if not current & 0x80:
            return value, cursor
        shift += 7


def _git_apply_delta(base: bytes, delta: bytes, context: str) -> bytes:
    base_size, cursor = _git_delta_varint(delta, 0, context)
    output_size, cursor = _git_delta_varint(delta, cursor, context)
    if base_size != len(base) or output_size > 1024 * 1024 * 1024:
        raise ReleaseError(f"{context}: delta base/output size mismatch")
    output = bytearray()
    while cursor < len(delta):
        opcode = delta[cursor]
        cursor += 1
        if opcode & 0x80:
            offset = 0
            size = 0
            for bit, shift in ((0x01, 0), (0x02, 8), (0x04, 16), (0x08, 24)):
                if opcode & bit:
                    if cursor >= len(delta):
                        raise ReleaseError(f"{context}: truncated delta copy offset")
                    offset |= delta[cursor] << shift
                    cursor += 1
            for bit, shift in ((0x10, 0), (0x20, 8), (0x40, 16)):
                if opcode & bit:
                    if cursor >= len(delta):
                        raise ReleaseError(f"{context}: truncated delta copy size")
                    size |= delta[cursor] << shift
                    cursor += 1
            if size == 0:
                size = 0x10000
            if offset + size > len(base) or len(output) + size > output_size:
                raise ReleaseError(f"{context}: delta copy exceeds bounds")
            output.extend(base[offset:offset + size])
        else:
            if opcode == 0 or cursor + opcode > len(delta) or len(output) + opcode > output_size:
                raise ReleaseError(f"{context}: malformed delta literal")
            output.extend(delta[cursor:cursor + opcode])
            cursor += opcode
    if len(output) != output_size:
        raise ReleaseError(f"{context}: reconstructed delta size mismatch")
    return bytes(output)


def _git_unpack_at(
    pack_raw: bytes,
    offset: int,
    *,
    load_oid: Any,
    memo: dict[int, tuple[str, bytes]],
    active: set[int],
    context: str,
) -> tuple[str, bytes]:
    cached = memo.get(offset)
    if cached is not None:
        return cached
    if offset in active or not (12 <= offset < len(pack_raw) - 20):
        raise ReleaseError(f"{context}: cyclic/out-of-range packed object")
    active.add(offset)
    try:
        cursor = offset
        current = pack_raw[cursor]
        cursor += 1
        object_type = (current >> 4) & 7
        declared_size = current & 0x0f
        shift = 4
        while current & 0x80:
            if cursor >= len(pack_raw) - 20 or shift > 60:
                raise ReleaseError(f"{context}: malformed packed-object header")
            current = pack_raw[cursor]
            cursor += 1
            declared_size |= (current & 0x7f) << shift
            shift += 7
        if object_type in (1, 2, 3, 4):
            data = _inflate_git_stream(pack_raw[cursor:-20], context)
            if len(data) != declared_size:
                raise ReleaseError(f"{context}: packed-object size mismatch")
            kind = {1: "commit", 2: "tree", 3: "blob", 4: "tag"}[object_type]
            result = (kind, data)
        elif object_type == 6:
            if cursor >= len(pack_raw) - 20:
                raise ReleaseError(f"{context}: truncated OFS delta")
            current = pack_raw[cursor]
            cursor += 1
            distance = current & 0x7f
            while current & 0x80:
                if cursor >= len(pack_raw) - 20:
                    raise ReleaseError(f"{context}: truncated OFS delta base")
                current = pack_raw[cursor]
                cursor += 1
                distance = ((distance + 1) << 7) | (current & 0x7f)
            base_offset = offset - distance
            base_kind, base_data = _git_unpack_at(
                pack_raw, base_offset, load_oid=load_oid, memo=memo, active=active,
                context=context,
            )
            delta = _inflate_git_stream(pack_raw[cursor:-20], context)
            if len(delta) != declared_size:
                raise ReleaseError(f"{context}: OFS delta instruction size mismatch")
            result = (base_kind, _git_apply_delta(base_data, delta, context))
        elif object_type == 7:
            if cursor + 20 > len(pack_raw) - 20:
                raise ReleaseError(f"{context}: truncated REF delta")
            base_oid = pack_raw[cursor:cursor + 20].hex()
            cursor += 20
            base_kind, base_data = load_oid(base_oid)
            delta = _inflate_git_stream(pack_raw[cursor:-20], context)
            if len(delta) != declared_size:
                raise ReleaseError(f"{context}: REF delta instruction size mismatch")
            result = (base_kind, _git_apply_delta(base_data, delta, context))
        else:
            raise ReleaseError(f"{context}: reserved packed-object type")
        memo[offset] = result
        return result
    finally:
        active.remove(offset)


def _git_read_object(project_root: Path, oid: str) -> tuple[str, bytes]:
    if type(oid) is not str or re.fullmatch(r"[0-9a-f]{40}", oid) is None:
        raise ReleaseError("Git object ID must be lowercase SHA-1")
    _repository_root, git_dir, _prefix = _git_roots(project_root)
    matches: list[tuple[str, bytes]] = []
    loose = git_dir / "objects" / oid[:2] / oid[2:]
    try:
        loose_raw, _ = read_snapshot(loose, maximum_bytes=1024 * 1024 * 1024)
    except FileNotFoundError:
        pass
    else:
        framed = _inflate_git_stream(loose_raw, f"loose Git object {oid}")
        matches.append(_git_parse_framed(framed, oid, f"loose Git object {oid}"))
    pack_dir = git_dir / "objects" / "pack"
    try:
        first_names = tuple(sorted(
            entry.name for entry in os.scandir(pack_dir)
            if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name)
        ))
    except FileNotFoundError:
        first_names = ()
    for index_name in first_names:
        index_raw, _ = read_snapshot(pack_dir / index_name, maximum_bytes=128 * 1024 * 1024)
        offsets, pack_checksum = _git_pack_index(index_raw, f"Git pack index {index_name}")
        if oid not in offsets:
            continue
        pack_path = pack_dir / f"{index_name[:-4]}.pack"
        pack_raw, _ = read_snapshot(pack_path, maximum_bytes=1024 * 1024 * 1024)
        if (
            len(pack_raw) < 32 or pack_raw[:4] != b"PACK"
            or struct.unpack_from(">I", pack_raw, 4)[0] not in (2, 3)
            or hashlib.sha1(pack_raw[:-20], usedforsecurity=False).digest() != pack_raw[-20:]
            or pack_raw[-20:] != pack_checksum
        ):
            raise ReleaseError(f"Git pack {pack_path.name}: header/checksum mismatch")
        memo: dict[int, tuple[str, bytes]] = {}

        def load_base(base_oid: str) -> tuple[str, bytes]:
            if base_oid in offsets:
                return _git_unpack_at(
                    pack_raw, offsets[base_oid], load_oid=load_base, memo=memo,
                    active=set(), context=f"Git pack {pack_path.name}",
                )
            return _git_read_object(project_root, base_oid)

        kind, data = _git_unpack_at(
            pack_raw, offsets[oid], load_oid=load_base, memo=memo, active=set(),
            context=f"Git pack {pack_path.name}",
        )
        framed = kind.encode() + b" " + str(len(data)).encode() + b"\x00" + data
        if _sha1(framed) != oid:
            raise ReleaseError(f"Git packed object {oid}: reconstructed ID mismatch")
        matches.append((kind, data))
    try:
        second_names = tuple(sorted(
            entry.name for entry in os.scandir(pack_dir)
            if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name)
        ))
    except FileNotFoundError:
        second_names = ()
    if second_names != first_names or not matches:
        raise ReleaseError(f"Git object {oid} is missing, ambiguous, or pack namespace changed")
    if any(match != matches[0] for match in matches[1:]):
        raise ReleaseError(f"Git object {oid} has conflicting loose/pack images")
    return matches[0]


def _git_commit_metadata(
    project_root: Path, commit_oid: str
) -> tuple[str, tuple[str, ...]]:
    """Parse one ordinary commit's closed header grammar from object bytes."""

    kind, payload = _git_read_object(project_root, commit_oid)
    if kind != "commit":
        raise ReleaseError("reviewed Git OID is not a commit")
    separator = payload.find(b"\n\n")
    if separator < 0:
        raise ReleaseError("reviewed Git commit header is unterminated")
    header_raw = payload[:separator]
    if b"\x00" in header_raw or b"\r" in header_raw:
        raise ReleaseError("reviewed Git commit header has control syntax")
    headers = header_raw.split(b"\n")
    if any(not header or header.startswith(b" ") for header in headers):
        raise ReleaseError("reviewed Git commit has empty/continued header syntax")
    tree_match = re.fullmatch(rb"tree ([0-9a-f]{40})", headers[0])
    if tree_match is None:
        raise ReleaseError("reviewed Git commit lacks canonical tree header")
    cursor = 1
    parents: list[str] = []
    while cursor < len(headers):
        parent = re.fullmatch(rb"parent ([0-9a-f]{40})", headers[cursor])
        if parent is None:
            break
        oid = parent.group(1).decode("ascii")
        if oid in parents:
            raise ReleaseError("reviewed Git commit repeats a parent")
        parents.append(oid)
        cursor += 1

    def require_identity(header: bytes, label: bytes) -> None:
        match = re.fullmatch(
            label
            + rb" ([^<>\x00-\x1f\x7f]+) <([^<>\x00-\x20\x7f]+)> "
            + rb"(0|[1-9][0-9]*) ([+-])((?:0[0-9])|(?:1[0-4]))([0-5][0-9])",
            header,
        )
        if match is None or match.group(1) != match.group(1).strip():
            raise ReleaseError(
                f"reviewed Git commit has malformed {label.decode()} header"
            )
        if match.group(5) == b"14" and match.group(6) != b"00":
            raise ReleaseError(
                f"reviewed Git commit has malformed {label.decode()} timezone"
            )

    if len(headers) != cursor + 2:
        raise ReleaseError(
            "reviewed Git commit has missing, duplicate, or unknown headers"
        )
    require_identity(headers[cursor], b"author")
    require_identity(headers[cursor + 1], b"committer")
    return tree_match.group(1).decode("ascii"), tuple(parents)


def _git_commit_tree(project_root: Path, commit_oid: str) -> str:
    return _git_commit_metadata(project_root, commit_oid)[0]


def _git_commit_parents(project_root: Path, commit_oid: str) -> tuple[str, ...]:
    return _git_commit_metadata(project_root, commit_oid)[1]


def _git_tree_entry_optional(
    project_root: Path, tree_oid: str, name: str
) -> tuple[int, str] | None:
    kind, payload = _git_read_object(project_root, tree_oid)
    if kind != "tree":
        raise ReleaseError("Git path traversal encountered a non-tree object")
    wanted = name.encode("utf-8")
    cursor = 0
    matches: list[tuple[int, str]] = []
    previous: bytes | None = None
    while cursor < len(payload):
        space = payload.find(b" ", cursor)
        nul = payload.find(b"\x00", space + 1)
        if space <= cursor or nul < 0 or nul + 21 > len(payload):
            raise ReleaseError("malformed Git tree object")
        mode_raw = payload[cursor:space]
        entry_name = payload[space + 1:nul]
        if previous is not None and entry_name <= previous:
            # Git sorts directory names as if suffixed with '/', but duplicate
            # byte names remain impossible; only enforce uniqueness here.
            if entry_name == previous:
                raise ReleaseError("duplicate Git tree entry")
        previous = entry_name
        try:
            mode = int(mode_raw, 8)
        except ValueError as error:
            raise ReleaseError("malformed Git tree mode") from error
        oid = payload[nul + 1:nul + 21].hex()
        if entry_name == wanted:
            matches.append((mode, oid))
        cursor = nul + 21
    if len(matches) > 1:
        raise ReleaseError(f"Git tree path component {name!r} is ambiguous")
    if not matches:
        return None
    return matches[0]


def _git_tree_entry(project_root: Path, tree_oid: str, name: str) -> tuple[int, str]:
    entry = _git_tree_entry_optional(project_root, tree_oid, name)
    if entry is None:
        raise ReleaseError(f"Git tree path component {name!r} is missing")
    return entry


def _git_tree_path_absent(
    project_root: Path, tree_oid: str, relative: str
) -> bool:
    safe_relative(relative)
    _repository_root, _git_dir, prefix = _git_roots(project_root)
    parts = (*prefix.parts, *PurePosixPath(relative).parts)
    current = tree_oid
    for index, part in enumerate(parts):
        entry = _git_tree_entry_optional(project_root, current, part)
        if entry is None:
            return True
        mode, child = entry
        if index == len(parts) - 1:
            return False
        if mode != 0o40000:
            raise ReleaseError(
                "Git introduction parent has a non-directory path prefix"
            )
        current = child
    raise ReleaseError("empty Git introduction path")


def _git_commit_blob(project_root: Path, commit_oid: str, relative: str) -> tuple[int, bytes, str]:
    safe_relative(relative)
    _repository_root, _git_dir, prefix = _git_roots(project_root)
    parts = (*prefix.parts, *PurePosixPath(relative).parts)
    oid = _git_commit_tree(project_root, commit_oid)
    mode = 0
    for index, part in enumerate(parts):
        mode, child = _git_tree_entry(project_root, oid, part)
        if index != len(parts) - 1:
            if mode != 0o40000:
                raise ReleaseError("Git reviewed path crosses a non-directory")
            oid = child
        else:
            if mode not in (0o100644, 0o100755):
                raise ReleaseError("Git reviewed artifact is not a regular tracked blob")
            kind, raw = _git_read_object(project_root, child)
            if kind != "blob":
                raise ReleaseError("Git reviewed path does not resolve to a blob")
            return mode, raw, child
    raise ReleaseError("empty Git reviewed path")


def _git_verify_commit_bindings(
    project_root: Path,
    commit_oid: str,
    bindings: Sequence[Mapping[str, Any]],
) -> str:
    tree_oid = _git_commit_tree(project_root, commit_oid)
    for index, binding in enumerate(bindings):
        git_mode, raw, blob_oid = _git_commit_blob(
            project_root, commit_oid, binding["path"]
        )
        if sha256_bytes(raw) != binding["sha256"]:
            raise ReleaseError(f"Git reviewed binding {index} bytes/hash mismatch")
        if "mode" in binding:
            recorded_mode = _mode_text(
                binding["mode"], f"Git reviewed binding {index} mode"
            )
            expected_git_mode = (
                0o100755 if int(recorded_mode, 8) & 0o111 else 0o100644
            )
            if git_mode != expected_git_mode:
                raise ReleaseError(
                    f"Git reviewed binding {index} tracked mode mismatch"
                )
        framed = b"blob " + str(len(raw)).encode() + b"\x00" + raw
        if _sha1(framed) != blob_oid:
            raise ReleaseError(f"Git reviewed binding {index} blob ID mismatch")
    return tree_oid


def _git_verify_introduction_binding(
    project_root: Path,
    commit_oid: str,
    binding: Mapping[str, Any],
    *,
    descendant_oid: str | None = None,
) -> None:
    """Prove a fixed artifact was introduced at one unambiguous commit edge."""

    parents = _git_commit_parents(project_root, commit_oid)
    if len(parents) != 1:
        raise ReleaseError(
            "publication introduction commit must have exactly one parent"
        )
    _git_verify_commit_bindings(project_root, commit_oid, [binding])
    current_older = parents[0]
    older_visited: set[str] = set()
    for _depth in range(100_000):
        if current_older in older_visited:
            raise ReleaseError("Git introduction history contains a cycle")
        older_visited.add(current_older)
        older_tree = _git_commit_tree(project_root, current_older)
        if not _git_tree_path_absent(
            project_root, older_tree, binding["path"]
        ):
            raise ReleaseError(
                "publication commit is a deletion/re-add, not the first introduction"
            )
        older_parents = _git_commit_parents(project_root, current_older)
        if not older_parents:
            break
        current_older = older_parents[0]
    else:
        raise ReleaseError("Git introduction history exceeds the closed depth bound")
    if descendant_oid is not None:
        current = descendant_oid
        visited: set[str] = set()
        lineage: list[str] = []
        for _depth in range(100_000):
            if current in visited:
                raise ReleaseError("Git first-parent history contains a cycle")
            visited.add(current)
            lineage.append(current)
            if current == commit_oid:
                for lineage_commit in lineage:
                    _git_verify_commit_bindings(
                        project_root, lineage_commit, [binding]
                    )
                return
            current_parents = _git_commit_parents(project_root, current)
            if not current_parents:
                break
            current = current_parents[0]
        raise ReleaseError(
            "publication introduction is unreachable on the fixed first-parent history"
        )


def _git_require_first_parent_ancestor(
    project_root: Path, ancestor_oid: str, descendant_oid: str
) -> None:
    current = descendant_oid
    visited: set[str] = set()
    for _depth in range(100_000):
        if current == ancestor_oid:
            return
        if current in visited:
            raise ReleaseError("Git first-parent history contains a cycle")
        visited.add(current)
        parents = _git_commit_parents(project_root, current)
        if not parents:
            break
        current = parents[0]
    raise ReleaseError("required Git commit is not a first-parent ancestor")


def _git_read_ref(project_root: Path, relative: str) -> str:
    _repository_root, git_dir, _prefix = _git_roots(project_root)
    path = git_dir / Path(PurePosixPath(relative))
    try:
        raw, _ = read_snapshot(path, maximum_bytes=1024 * 1024)
    except FileNotFoundError:
        packed_raw, _ = read_snapshot(git_dir / "packed-refs", maximum_bytes=16 * 1024 * 1024)
        text = packed_raw.decode("ascii", errors="strict")
        found = [
            line[:40] for line in text.splitlines()
            if re.fullmatch(rf"[0-9a-f]{{40}} {re.escape(relative)}", line)
        ]
        if len(found) != 1:
            raise ReleaseError(f"Git ref {relative} is missing/ambiguous")
        return found[0]
    text = raw.decode("ascii", errors="strict")
    if re.fullmatch(r"[0-9a-f]{40}\n", text) is None:
        raise ReleaseError(f"Git ref {relative} is malformed")
    return text[:-1]


def _git_index_records(project_root: Path) -> list[tuple[str, int, str]]:
    _repository_root, git_dir, _prefix = _git_roots(project_root)
    raw, _ = read_snapshot(git_dir / "index", maximum_bytes=128 * 1024 * 1024)
    if len(raw) < 32 or raw[:4] != b"DIRC":
        raise ReleaseError("Git index header is malformed")
    version, count = struct.unpack_from(">II", raw, 4)
    if version != 2 or count <= 0:
        raise ReleaseError("Git index must be nonempty version 2")
    body, checksum = raw[:-20], raw[-20:]
    if hashlib.sha1(body, usedforsecurity=False).digest() != checksum:
        raise ReleaseError("Git index checksum mismatch")
    cursor = 12
    fixed_format = ">LLLLLLLLLL20sH"
    fixed_size = struct.calcsize(fixed_format)
    records: list[tuple[str, int, str]] = []
    for index in range(count):
        start = cursor
        if cursor + fixed_size > len(body):
            raise ReleaseError(f"Git index entry {index} is truncated")
        fields = struct.unpack_from(fixed_format, body, cursor)
        mode, oid, flags = fields[6], fields[10].hex(), fields[11]
        cursor += fixed_size
        if flags & 0xf000:
            raise ReleaseError("Git index contains staged/extended entries")
        try:
            end = body.index(b"\x00", cursor)
        except ValueError as error:
            raise ReleaseError("Git index path is unterminated") from error
        try:
            relative = body[cursor:end].decode("utf-8", errors="strict")
        except UnicodeError as error:
            raise ReleaseError("Git index path is not UTF-8") from error
        _machine_safe_relative(relative, "Git index path")
        if (flags & 0x0fff) != min(end - cursor, 0x0fff):
            raise ReleaseError("Git index path-length flag mismatch")
        if mode not in (0o100644, 0o100755, 0o120000):
            raise ReleaseError("Git index contains unsupported mode")
        cursor = end + 1
        while (cursor - start) % 8:
            if cursor >= len(body) or body[cursor] != 0:
                raise ReleaseError("Git index padding is malformed")
            cursor += 1
        records.append((relative, mode, oid))
    while cursor < len(body):
        if cursor + 8 > len(body):
            raise ReleaseError("Git index extension is truncated")
        signature = body[cursor:cursor + 4]
        size = struct.unpack_from(">I", body, cursor + 4)[0]
        cursor += 8
        if re.fullmatch(rb"[A-Z]{4}", signature) is None or size > len(body) - cursor:
            raise ReleaseError("Git index extension is malformed/required")
        cursor += size
    if (
        records != sorted(records, key=lambda row: row[0].encode("utf-8"))
        or len({row[0] for row in records}) != len(records)
    ):
        raise ReleaseError("Git index paths are unordered/duplicated")
    return records


def _git_index_tree_oid(records: Sequence[tuple[str, int, str]]) -> str:
    def node() -> dict[str, Any]:
        return {"files": {}, "directories": {}}

    root = node()
    for relative, mode, oid in records:
        current = root
        parts = PurePosixPath(relative).parts
        for part in parts[:-1]:
            if part in current["files"]:
                raise ReleaseError("Git index file/directory prefix collision")
            current = current["directories"].setdefault(part, node())
        name = parts[-1]
        if name in current["files"] or name in current["directories"]:
            raise ReleaseError("Git index duplicate tree entry")
        current["files"][name] = (mode, oid)

    def digest(current: Mapping[str, Any]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, (mode, oid) in current["files"].items():
            encoded = name.encode("utf-8")
            entries.append((
                encoded,
                f"{mode:o}".encode() + b" " + encoded + b"\x00" + bytes.fromhex(oid),
            ))
        for name, child in current["directories"].items():
            encoded = name.encode("utf-8")
            entries.append((
                encoded + b"/",
                b"40000 " + encoded + b"\x00" + bytes.fromhex(digest(child)),
            ))
        content = b"".join(payload for _key, payload in sorted(entries))
        return _sha1(b"tree " + str(len(content)).encode() + b"\x00" + content)

    return digest(root)


def _validate_current_git_snapshot(
    project_root: Path,
    repository: Mapping[str, Any],
    required_bindings: Sequence[Mapping[str, Any]],
) -> None:
    repository_root, git_dir, prefix = _git_roots(project_root)
    head_raw, _ = read_snapshot(git_dir / "HEAD", maximum_bytes=4096)
    if head_raw != b"ref: refs/heads/main\n":
        raise ReleaseError("current Git HEAD is not exact main symbolic ref")
    commit = repository["capture_commit_oid"]
    if (
        _git_read_ref(project_root, "refs/heads/main") != commit
        or _git_read_ref(project_root, "refs/remotes/origin/main")
        != repository["origin_main_oid"]
    ):
        raise ReleaseError("current Git refs differ from role11 repository snapshot")
    records = _git_index_records(project_root)
    if _git_index_tree_oid(records) != repository["capture_tree_oid"]:
        raise ReleaseError("current Git index tree differs from role11 capture tree")
    record_map = {relative: (mode, oid) for relative, mode, oid in records}
    for index, (relative, mode, oid) in enumerate(records):
        target = repository_root / Path(PurePosixPath(relative))
        if mode == 0o120000:
            before = os.lstat(target)
            if not stat.S_ISLNK(before.st_mode) or before.st_nlink != 1:
                raise PathContractError("tracked Git symlink contract mismatch")
            raw = os.readlink(target).encode("utf-8", errors="strict")
            after = os.lstat(target)
            if _fingerprint(before) != _fingerprint(after) or len(raw) != before.st_size:
                raise PathContractError("tracked Git symlink changed during replay")
        else:
            raw, info = read_snapshot(target)
            if bool(stat.S_IMODE(info.st_mode) & 0o111) is not (mode == 0o100755):
                raise ReleaseError(f"tracked Git mode mismatch at index entry {index}")
        if _sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw) != oid:
            raise ReleaseError(f"tracked Git bytes differ from index at entry {index}")
    for index, binding in enumerate(required_bindings):
        git_relative = PurePosixPath(*prefix.parts, *PurePosixPath(binding["path"]).parts).as_posix()
        record = record_map.get(git_relative)
        if record is None:
            raise ReleaseError(f"role11 required Git binding {index} is not tracked")
        expected_mode = 0o100755 if int(binding["mode"], 8) & 0o111 else 0o100644
        expected_blob = _sha1(
            b"blob " + str(binding["size_bytes"]).encode() + b"\x00"
            + read_snapshot(project_file(project_root, binding["path"]))[0]
        )
        if record != (expected_mode, expected_blob):
            raise ReleaseError(f"role11 required Git binding {index} index mismatch")


def safe_relative(value: Any) -> PurePosixPath:
    if type(value) is not str or not value or "\x00" in value or "\\" in value:
        raise PathContractError("unsafe relative path")
    relative = PurePosixPath(value)
    if (
        relative.is_absolute()
        or relative.as_posix() != value
        or any(part in ("", ".", "..") or part.startswith(".") for part in relative.parts)
    ):
        raise PathContractError(f"noncanonical relative path: {value!r}")
    return relative


def lexical_absolute(path: Path | str) -> Path:
    value = os.fspath(path)
    if (
        type(value) is not str
        or not value.startswith("/")
        or value.startswith("//")
        or "//" in value
        or "\\" in value
        or "\x00" in value
        or (value != "/" and value.endswith("/"))
        or any(part in ("", ".", "..") for part in value.split("/")[1:])
        or os.path.normpath(value) != value
    ):
        raise PathContractError(f"path is not lexical absolute: {value!r}")
    return Path(value)


def project_file(project_root: Path, relative: str | PurePosixPath) -> Path:
    root = lexical_absolute(project_root)
    rel = safe_relative(relative.as_posix() if isinstance(relative, PurePosixPath) else relative)
    return root.joinpath(*rel.parts)


def _assert_absent_namespace(path: Path, context: str) -> None:
    candidate = lexical_absolute(path)
    _reject_symlink_components(candidate.parent)
    parent_signature = _namespace_signature(candidate.parent)
    try:
        os.stat(candidate, follow_symlinks=False)
    except FileNotFoundError:
        pass
    else:
        raise ReleaseError(f"{context} must be absent")
    if _namespace_signature(candidate.parent) != parent_signature:
        raise PathContractError(f"{context} parent namespace changed")
    try:
        os.stat(candidate, follow_symlinks=False)
    except FileNotFoundError:
        if _ACTIVE_ABSENCES is not None:
            previous = _ACTIVE_ABSENCES.get(candidate)
            evidence = (context, parent_signature)
            if previous is not None and previous[1] != parent_signature:
                raise PathContractError(f"{context} absence generation changed")
            _ACTIVE_ABSENCES[candidate] = evidence
        return
    raise ReleaseError(f"{context} appeared during absence replay")


def _terminal_replay_absence(
    path: Path,
    context: str,
    parent_signature: tuple[tuple[str, int, int, int], ...],
) -> None:
    _reject_symlink_components(path.parent)
    if _namespace_signature(path.parent) != parent_signature:
        raise PathContractError(f"{context} parent namespace changed")
    try:
        os.stat(path, follow_symlinks=False)
    except FileNotFoundError:
        pass
    else:
        raise ReleaseError(f"{context} appeared before terminal replay")
    if _namespace_signature(path.parent) != parent_signature:
        raise PathContractError(f"{context} parent changed during terminal replay")


def _reject_symlink_components(path: Path) -> None:
    candidate = Path(path.anchor)
    for part in path.parts[1:]:
        candidate /= part
        try:
            info = os.lstat(candidate)
        except FileNotFoundError:
            return
        if stat.S_ISLNK(info.st_mode):
            raise PathContractError(f"symlink component: {candidate}")
        if candidate != path and not stat.S_ISDIR(info.st_mode):
            raise PathContractError(f"nondirectory ancestor: {candidate}")


def _namespace_signature(path: Path) -> tuple[tuple[str, int, int, int], ...]:
    """Bind every lexical directory inode leading to ``path``.

    Directory timestamps and link counts are intentionally excluded: sibling
    activity is not authority.  Device/inode/type/mode still detects every
    ancestor substitution or alias of the lexical route used for the read.
    """

    rows: list[tuple[str, int, int, int]] = []
    candidate = Path(path.anchor)
    for part in path.parts[1:]:
        candidate /= part
        info = os.lstat(candidate)
        rows.append((str(candidate), info.st_dev, info.st_ino, info.st_mode))
    return tuple(rows)


def read_snapshot(path: Path, *, maximum_bytes: int = 1024 * 1024 * 1024) -> tuple[bytes, os.stat_result]:
    canonical = lexical_absolute(path)
    _reject_symlink_components(canonical)
    cached = _ACTIVE_SNAPSHOTS.get(canonical) if _ACTIVE_SNAPSHOTS is not None else None
    if cached is not None:
        current = os.stat(canonical, follow_symlinks=False)
        if (
            _fingerprint(current) != cached.fingerprint
            or _namespace_signature(canonical) != cached.namespace
        ):
            raise PathContractError(f"input changed after snapshot: {canonical}")
        return cached.raw, current
    before = os.stat(canonical, follow_symlinks=False)
    namespace = _namespace_signature(canonical)
    if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
        raise PathContractError(f"input is not one unaliased regular inode: {canonical}")
    if before.st_size < 0 or before.st_size > maximum_bytes:
        raise PathContractError(f"input exceeds bounded read: {canonical}")
    descriptor = os.open(
        canonical,
        os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
    )
    try:
        opened = os.fstat(descriptor)
        if _fingerprint(opened) != _fingerprint(before):
            raise PathContractError(f"path/inode race: {canonical}")
        chunks: list[bytes] = []
        offset = 0
        while True:
            chunk = os.pread(descriptor, 1024 * 1024, offset)
            if not chunk:
                break
            chunks.append(chunk)
            offset += len(chunk)
            if offset > maximum_bytes:
                raise PathContractError(f"input exceeds bounded read: {canonical}")
        raw = b"".join(chunks)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    lexical_after = os.stat(canonical, follow_symlinks=False)
    if (
        len(raw) != before.st_size
        or _fingerprint(after) != _fingerprint(before)
        or _fingerprint(lexical_after) != _fingerprint(before)
        or _namespace_signature(canonical) != namespace
    ):
        raise PathContractError(f"input changed during snapshot: {canonical}")
    if _ACTIVE_SNAPSHOTS is not None:
        _ACTIVE_SNAPSHOTS[canonical] = Snapshot(
            canonical, raw, _fingerprint(before), namespace
        )
    return raw, before


def _terminal_replay(snapshot: Snapshot) -> None:
    _reject_symlink_components(snapshot.path)
    raw, info = _read_snapshot_uncached(snapshot.path, len(snapshot.raw) + 1)
    if (
        raw != snapshot.raw
        or _fingerprint(info) != snapshot.fingerprint
        or _namespace_signature(snapshot.path) != snapshot.namespace
    ):
        raise PathContractError(f"input changed before terminal replay: {snapshot.path}")


def _read_snapshot_uncached(path: Path, maximum_bytes: int) -> tuple[bytes, os.stat_result]:
    active = globals()["_ACTIVE_SNAPSHOTS"]
    globals()["_ACTIVE_SNAPSHOTS"] = None
    try:
        return read_snapshot(path, maximum_bytes=maximum_bytes)
    finally:
        globals()["_ACTIVE_SNAPSHOTS"] = active


def _open_directory(path: Path) -> int:
    canonical = lexical_absolute(path)
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for part in canonical.parts[1:]:
            child = os.open(part, flags | nofollow, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def _read_machine_manifest_uncached(
    path: Path, *, maximum_bytes: int = 1024 * 1024 * 1024
) -> tuple[bytes, os.stat_result]:
    """Read a package-managed regular file while allowing legitimate hard links."""

    canonical = lexical_absolute(path)
    _reject_symlink_components(canonical)
    namespace = _namespace_signature(canonical)
    before = os.stat(canonical, follow_symlinks=False)
    if not stat.S_ISREG(before.st_mode) or before.st_size < 0 or before.st_size > maximum_bytes:
        raise PathContractError(f"machine manifest file contract mismatch: {canonical}")
    descriptor = os.open(
        canonical,
        os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
    )
    try:
        opened = os.fstat(descriptor)
        if _fingerprint(opened) != _fingerprint(before):
            raise PathContractError(f"machine manifest path/inode race: {canonical}")
        chunks: list[bytes] = []
        offset = 0
        while True:
            chunk = os.pread(descriptor, 1024 * 1024, offset)
            if not chunk:
                break
            chunks.append(chunk)
            offset += len(chunk)
            if offset > maximum_bytes:
                raise PathContractError(f"machine manifest exceeds bound: {canonical}")
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    replay = os.stat(canonical, follow_symlinks=False)
    raw = b"".join(chunks)
    if (
        len(raw) != before.st_size
        or _fingerprint(after) != _fingerprint(before)
        or _fingerprint(replay) != _fingerprint(before)
        or _namespace_signature(canonical) != namespace
    ):
        raise PathContractError(f"machine manifest changed during read: {canonical}")
    return raw, before


@contextmanager
def capture_input_generation() -> Iterator[None]:
    global _ACTIVE_MACHINE_CAPD_NAMESPACES, _ACTIVE_MACHINE_CONDA_META_NAMESPACES
    global _ACTIVE_MACHINE_MANIFEST_FILES, _ACTIVE_MACHINE_PATHS, _ACTIVE_SNAPSHOTS
    global _ACTIVE_ABSENCES
    if _ACTIVE_SNAPSHOTS is not None:
        yield
        return
    _ACTIVE_SNAPSHOTS = {}
    _ACTIVE_ABSENCES = {}
    _ACTIVE_MACHINE_PATHS = {}
    _ACTIVE_MACHINE_MANIFEST_FILES = {}
    _ACTIVE_MACHINE_CAPD_NAMESPACES = {}
    _ACTIVE_MACHINE_CONDA_META_NAMESPACES = {}
    try:
        yield
        snapshots = tuple(_ACTIVE_SNAPSHOTS.values())
        for snapshot in snapshots:
            _terminal_replay(snapshot)
        for path, (context, parent_signature) in (_ACTIVE_ABSENCES or {}).items():
            _terminal_replay_absence(path, context, parent_signature)
        for lexical, (expected_fingerprint, expected_resolved) in (
            _ACTIVE_MACHINE_PATHS or {}
        ).items():
            if (
                _fingerprint(os.lstat(lexical)) != expected_fingerprint
                or lexical.resolve(strict=True) != expected_resolved
            ):
                raise PathContractError(f"external machine path changed: {lexical}")
        for path, (expected_raw, expected_fingerprint) in (
            _ACTIVE_MACHINE_MANIFEST_FILES or {}
        ).items():
            raw, info = _read_machine_manifest_uncached(path)
            if raw != expected_raw or _fingerprint(info) != expected_fingerprint:
                raise PathContractError(f"machine manifest changed: {path}")
        for checkout, (tracked, expected_signature) in (
            _ACTIVE_MACHINE_CAPD_NAMESPACES or {}
        ).items():
            if _machine_capd_namespace_signature(checkout, tracked) != expected_signature:
                raise PathContractError(f"CAPD namespace changed: {checkout}")
        for meta_dir, expected_names in (
            _ACTIVE_MACHINE_CONDA_META_NAMESPACES or {}
        ).items():
            current_names = tuple(sorted(
                (entry.name for entry in os.scandir(meta_dir)),
                key=lambda name: name.encode("utf-8"),
            ))
            if current_names != expected_names:
                raise PathContractError(f"Conda metadata namespace changed: {meta_dir}")
    finally:
        _ACTIVE_MACHINE_CONDA_META_NAMESPACES = None
        _ACTIVE_MACHINE_CAPD_NAMESPACES = None
        _ACTIVE_MACHINE_MANIFEST_FILES = None
        _ACTIVE_MACHINE_PATHS = None
        _ACTIVE_ABSENCES = None
        _ACTIVE_SNAPSHOTS = None


def _terminal_replay_generation() -> None:
    """Force the complete active input generation replay at a commit boundary."""

    if _ACTIVE_SNAPSHOTS is None:
        raise PathContractError("terminal generation replay requires an active capture")
    for snapshot in tuple(_ACTIVE_SNAPSHOTS.values()):
        _terminal_replay(snapshot)
    for path, (context, parent_signature) in (_ACTIVE_ABSENCES or {}).items():
        _terminal_replay_absence(path, context, parent_signature)
    for lexical, (expected_fingerprint, expected_resolved) in (
        _ACTIVE_MACHINE_PATHS or {}
    ).items():
        if (
            _fingerprint(os.lstat(lexical)) != expected_fingerprint
            or lexical.resolve(strict=True) != expected_resolved
        ):
            raise PathContractError(f"external machine path changed: {lexical}")
    for path, (expected_raw, expected_fingerprint) in (
        _ACTIVE_MACHINE_MANIFEST_FILES or {}
    ).items():
        raw, info = _read_machine_manifest_uncached(path)
        if raw != expected_raw or _fingerprint(info) != expected_fingerprint:
            raise PathContractError(f"machine manifest changed: {path}")
    for checkout, (tracked, expected_signature) in (
        _ACTIVE_MACHINE_CAPD_NAMESPACES or {}
    ).items():
        if _machine_capd_namespace_signature(checkout, tracked) != expected_signature:
            raise PathContractError(f"CAPD namespace changed: {checkout}")
    for meta_dir, expected_names in (
        _ACTIVE_MACHINE_CONDA_META_NAMESPACES or {}
    ).items():
        current_names = tuple(sorted(
            (entry.name for entry in os.scandir(meta_dir)),
            key=lambda name: name.encode("utf-8"),
        ))
        if current_names != expected_names:
            raise PathContractError(f"Conda metadata namespace changed: {meta_dir}")


def strict_json_image(path: Path, *, canonical: str | None = None) -> tuple[Mapping[str, Any], bytes]:
    raw, _ = read_snapshot(path)
    value = strict_json_loads(raw, canonical=canonical)
    if type(value) is not dict:
        raise StrictJSONError(f"JSON image is not an object: {path}")
    return value, raw


def matrix_payload() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": slab}
        for bits in PRECISIONS
        for slab in SLABS
    ]


def matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(matrix_payload()))


def formal_serializers() -> dict[str, Any]:
    return {
        "compact_json": {
            "id": "CJ_COMPACT_V1", "sort_keys": True, "ensure_ascii": False,
            "allow_nan": False, "indent": None, "separators": [",", ":"], "trailing_lf": True,
        },
        "branch_pretty_json": {
            "id": "CJ_PRETTY_2_V1", "sort_keys": True, "ensure_ascii": False,
            "allow_nan": False, "indent": 2, "separators": None, "trailing_lf": True,
        },
        "artifact_bindings": {
            "main_freeze": "CJ_COMPACT_V1", "run_config": "CJ_COMPACT_V1",
            "static_proof": "CJ_COMPACT_V1", "static_record": "CJ_COMPACT_V1",
            "static_manifest": "CJ_COMPACT_V1", "branch_task_hash": "CJ_PRETTY_2_V1",
            "branch_argv_hash": "CJ_PRETTY_2_V1", "branch_record": "CJ_PRETTY_2_V1",
            "branch_manifest": "CJ_PRETTY_2_V1", "aggregates": "CJ_COMPACT_V1",
        },
    }


def formal_scheduler_policy() -> dict[str, Any]:
    return {
        "policy": "deterministic_component_barrier_batches_v1",
        "component_order": ["STATIC", "BRANCH"],
        "static_workers": 8, "branch_workers": 6,
        "static_barrier_size": 8, "branch_barrier_size": 6,
        "max_inflight_per_cell": 1, "global_scientific_budget": None,
    }


def formal_limits() -> dict[str, Any]:
    return {
        "static": {
            "max_depth_per_tree": 24, "max_nodes_per_tree": 250_000,
            "max_nodes_per_cell": 1_000_000, "timeout_ms": 1_800_000,
            "total_cell_bytes": 512 * 1024 * 1024,
        },
        "branch": {
            "timeout_ms": 600_000, "term_grace_ms": 2_000,
            "pipe_close_grace_ms": 1_000, "stdout_bytes": 16 * 1024 * 1024,
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


def formal_status_tables() -> dict[str, Any]:
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


def formal_machine_requirements() -> dict[str, int]:
    return {
        "logical_cpu_count": 32, "memory_limit_bytes": 60 * 1024**3,
        "static_workers": 8, "branch_workers": 6,
        "memory_admission_limit_bytes": 48 * 1024**3, "reserve_bytes": 8 * 1024**3,
        "launch_free_bytes": 200 * 1024**3, "warning_free_bytes": 180 * 1024**3,
        "pause_free_bytes": 150 * 1024**3, "recovery_only_free_bytes": 120 * 1024**3,
    }


def formal_archive_layout() -> dict[str, Any]:
    return {
        "authoritative_relative": RESULT_RELATIVE.as_posix(),
        "operational_suffix": OPERATIONAL_SUFFIX,
        "static_cell_files": ["proof.json", "stdout.txt", "stderr.txt", "record.json"],
        "branch_cell_files": ["stdout.txt", "stderr.txt", "record.json"],
        "static_serializer": "CJ_COMPACT_V1", "branch_serializer": "CJ_PRETTY_2_V1",
        "aggregate_serializer": "CJ_COMPACT_V1",
    }


def formal_failure_policy() -> dict[str, Any]:
    return {
        "stop_after_current_barrier": True, "retry_same_generation": False,
        "aggregate_requires_certified_cells": 102, "quarantine_on_corrupt_recovery": True,
    }


def formal_execution_policy() -> dict[str, Any]:
    return {
        "initialize_only_writes_run_config": True,
        "execute_requires_existing_config": True,
        "execute_requires_resume": True,
        "explicit_execution_flags": ["--production", "--execute-scientific-dispatch", "--resume"],
        "config_self_authorizes": False,
        "branch_millisecond_migration_complete": True,
    }


def _require_null_statuses(payload: Mapping[str, Any], context: str) -> None:
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload.get(key) is not None:
            raise ReleaseError(f"unauthorised {context} status: {key}")


def _capture_input_roles(project_root: Path) -> tuple[tuple[dict[str, str], ...], dict[str, bytes]]:
    if (
        len(INPUT_ROLES) != 53
        or len({role for role, _ in INPUT_ROLES}) != 53
        or len({path for _, path in INPUT_ROLES}) != 53
    ):
        raise ReleaseError("V2 input role table is not exactly 53 unique roles/paths")
    records: list[dict[str, str]] = []
    images: dict[str, bytes] = {}
    for role, relative in INPUT_ROLES:
        raw, _ = read_snapshot(project_file(project_root, relative))
        if relative.endswith(".json"):
            strict_json_loads(raw)
        if role == "prefreeze_review" and raw != PREFREEZE_ACCEPT_RAW:
            raise ReleaseError("pre-freeze review is not the sole exact ASCII ACCEPT verdict")
        records.append({"role": role, "path": relative, "sha256": sha256_bytes(raw)})
        images[role] = raw
    return tuple(records), images


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
ROLE5_LEGACY_TERMINAL_COMMIT = "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0"
ROLE5_LEGACY_ARTIFACTS = (
    {
        "role": 10,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json",
        "sha256": "0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e",
        "publication_commit": "5086e33c7c66f33785338e90b340347e086d9941",
    },
    {
        "role": 11,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json",
        "sha256": "08ffeb5e7f5d681567bd7a81335585d1b8697040a28d91584b09fdc4304a379a",
        "publication_commit": "201758031a7784a68ab66d37094c25135de52646",
    },
    {
        "role": 12,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md",
        "sha256": "af38e899f9dad9abacadbdaa27f12833d5ea423a9896ee089fb8a4d90b55477c",
        "publication_commit": "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0",
    },
    {
        "role": 13,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json",
        "sha256": "d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30",
        "publication_commit": "be2a732625d9cab97879539873a756e1eabd366d",
    },
)
ROLE5_LEGACY_DEFECTS = (
    {
        "severity": "P1",
        "code": "ROLE24_MOCK_ONLY_NO_FORMAL_54_OR_68_VALIDATION",
        "finding": (
            "legacy role 24 implements mock release and machine verification only; "
            "it does not implement formal role-54 validation or publication or "
            "formal 68-role release validation or publication"
        ),
    },
    {
        "severity": "P1",
        "code": "ROLES20_22_NO_FORMAL_THREE_CHECKER_THREE_POSTCHECK_CHAIN",
        "finding": (
            "legacy roles 20 through 22 do not implement the required formal "
            "static, branch, and composite checker plus postcheck publication chain"
        ),
    },
)
ROLE5_SUPERSESSION_RULE = (
    "legacy attempt-1 bytes remain immutable audit evidence, are not V2 inputs, "
    "and confer no freeze, initialization, scientific licensing, promotion, or "
    "dispatch authority"
)


def _validate_role5(
    project_root: Path,
    payload: Any,
    records: Sequence[Mapping[str, str]],
) -> None:
    """Independently replay the exact role-5 withdrawal/design-review object."""

    exact_keys(payload, ROLE5_KEYS, "V2 role5 design review")
    exact_int(payload["schema_version"], "V2 role5 schema", expected=1)
    if (
        payload["protocol_id"] != PROTOCOL_ID
        or payload["artifact_role"] != "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL"
        or payload["status"] != "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1"
        or payload["authority"] != "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY"
        or payload["scientific_licensing_enabled"] is not False
        or payload["production_authorized"] is not False
        or payload["claim_boundary"] != ROLE5_CLAIM_BOUNDARY
    ):
        raise ReleaseError("V2 role5 identity/authority mismatch")
    _require_null_statuses(payload, "V2 role5")

    legacy = exact_keys(
        payload["legacy_attempt"],
        {"attempt_id", "status", "terminal_commit", "published_artifacts",
         "defects", "supersession_rule"},
        "V2 role5 legacy attempt",
    )
    expected_legacy = {
        "attempt_id": "A416_L3_A1_CONTROL_ATTEMPT_1",
        "status": "WITHDRAWN_NON_LICENSING",
        "terminal_commit": ROLE5_LEGACY_TERMINAL_COMMIT,
        "published_artifacts": list(ROLE5_LEGACY_ARTIFACTS),
        "defects": list(ROLE5_LEGACY_DEFECTS),
        "supersession_rule": ROLE5_SUPERSESSION_RULE,
    }
    if not exact_json_equal(legacy, expected_legacy):
        raise ReleaseError("V2 role5 legacy withdrawal literals mismatch")
    for index, row in enumerate(legacy["published_artifacts"]):
        exact_keys(row, {"role", "path", "sha256", "publication_commit"},
                   f"V2 role5 legacy artifact {index}")
        exact_int(row["role"], f"V2 role5 legacy artifact {index} role",
                  expected=10 + index)
        safe_relative(row["path"])
        require_sha256(row["sha256"], f"V2 role5 legacy artifact {index} hash")
        if type(row["publication_commit"]) is not str or re.fullmatch(
            r"[0-9a-f]{40}", row["publication_commit"]
        ) is None:
            raise ReleaseError("V2 role5 legacy publication commit mismatch")

    roles = {row["role"]: row for row in records}
    reviewed = payload["reviewed_v2_inputs"]
    if type(reviewed) is not list or len(reviewed) != 19:
        raise ReleaseError("V2 role5 must bind exactly 19 reviewed inputs")
    expected_reviewed = [
        {key: roles[role][key] for key in ("role", "path", "sha256")}
        for role in ROLE5_REVIEWED_ROLES
    ]
    if not exact_json_equal(reviewed, expected_reviewed):
        raise ReleaseError("V2 role5 reviewed live byte map mismatch")
    for index, row in enumerate(reviewed):
        exact_keys(row, {"role", "path", "sha256"}, f"V2 role5 review row {index}")
        safe_relative(row["path"])
        require_sha256(row["sha256"], f"V2 role5 review row {index} hash")

    review = exact_keys(
        payload["review"],
        {"reviewer_independent_of_attempt1_author", "verdict", "p0_count",
         "p1_count", "p2_count", "reviewed_commit", "map_matches_contract",
         "legacy_bytes_unchanged", "scientific_protocol_unchanged"},
        "V2 role5 review",
    )
    if (
        review["reviewer_independent_of_attempt1_author"] is not True
        or review["verdict"] != "ACCEPT_CONTROL_PLANE_V2_DESIGN"
        or review["map_matches_contract"] is not True
        or review["legacy_bytes_unchanged"] is not True
        or review["scientific_protocol_unchanged"] is not True
        or type(review["reviewed_commit"]) is not str
        or re.fullmatch(r"[0-9a-f]{40}", review["reviewed_commit"]) is None
    ):
        raise ReleaseError("V2 role5 independent review gates mismatch")
    for name in ("p0_count", "p1_count", "p2_count"):
        exact_int(review[name], f"V2 role5 {name}", expected=0)
    _git_verify_commit_bindings(
        project_root, review["reviewed_commit"], reviewed
    )
    for index, row in enumerate(reviewed):
        live_raw, live_info = read_snapshot(project_file(project_root, row["path"]))
        git_mode, git_raw, _blob_oid = _git_commit_blob(
            project_root, review["reviewed_commit"], row["path"]
        )
        expected_git_mode = (
            0o100755 if stat.S_IMODE(live_info.st_mode) & 0o111 else 0o100644
        )
        if (
            live_raw != git_raw
            or sha256_bytes(live_raw) != row["sha256"]
            or git_mode != expected_git_mode
        ):
            raise ReleaseError(
                f"V2 role5 reviewed live/blob/mode mismatch at row {index}"
            )
    terminal_commit = legacy["terminal_commit"]
    _git_require_first_parent_ancestor(
        project_root, terminal_commit, review["reviewed_commit"]
    )
    legacy_live_bindings: list[dict[str, Any]] = []
    for artifact in legacy["published_artifacts"]:
        legacy_raw, legacy_info = read_snapshot(
            project_file(project_root, artifact["path"])
        )
        if sha256_bytes(legacy_raw) != artifact["sha256"]:
            raise ReleaseError("V2 role5 legacy live byte image differs from withdrawal record")
        live_binding = {
            **artifact,
            "mode": f"{stat.S_IMODE(legacy_info.st_mode):04o}",
        }
        legacy_live_bindings.append(live_binding)
        _git_verify_introduction_binding(
            project_root,
            artifact["publication_commit"],
            live_binding,
            descendant_oid=review["reviewed_commit"],
        )
    _git_verify_commit_bindings(
        project_root, terminal_commit, legacy_live_bindings
    )


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
PREFREEZE_PREREQUISITE_KEYS = {
    "machine_role10", "s0_compatibility_role13",
    "second_fresh_rebuild_replay", "canonical_absence",
}
PREFREEZE_MACHINE_BINDING_KEYS = PREFREEZE_ROLE_ENTRY_KEYS | {
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verifier_path", "verifier_sha256", "verify_receipt",
    "promotion_authorized",
}
PREFREEZE_S0_BINDING_KEYS = PREFREEZE_ROLE_ENTRY_KEYS | {
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verify_receipt", "promotion_authorized",
}
PREFREEZE_VERIFY_RECEIPT_KEYS = {
    "verification_status", "authority", "candidate_sha256", "size_bytes",
    "promotion_authorized",
}
PREFREEZE_SECOND_REBUILD_KEYS = {
    "command_result_name", "command_result_sha256", "semantic_receipt",
}
PREFREEZE_SECOND_RECEIPT_KEYS = {
    "verification_status", "authority", "source_path", "source_sha256",
    "persistent_binary_path", "persistent_before_sha256",
    "persistent_after_sha256", "persistent_before_device_id",
    "persistent_before_inode", "persistent_after_device_id",
    "persistent_after_inode", "persistent_identity_unchanged",
    "persistent_overwrite_performed", "staging_output_sha256",
    "staging_output_size_bytes", "staging_output_mode",
    "staging_output_removed", "byte_for_byte_equal",
    "scientific_evaluator_dispatched",
}
PREFREEZE_COMMAND_KEYS = {
    "name", "kind", "argv", "cwd", "environment", "return_code",
    "started_at_utc", "wall_duration_ms", "stdout_utf8", "stdout_sha256",
    "stdout_size_bytes", "stderr_utf8", "stderr_sha256", "stderr_size_bytes",
    "pytest_counts", "semantic_receipt",
}
PREFREEZE_PYTEST_COUNT_KEYS = {"passed", "failed", "skipped", "xfailed", "xpassed"}
PREFREEZE_TEST_TOTAL_KEYS = PREFREEZE_PYTEST_COUNT_KEYS | {"wall_duration_ms"}
PREFREEZE_TEST_TOTAL_NAMES = {"prefreeze_focused", "l3_a1_modules", "paper02_full"}
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
    "producer": "scheduler",
    "independent_checker": "release_builder",
    "focused_test": "test_adversarial",
}
PREFREEZE_INPUT_ROLES = tuple(
    item for item in INPUT_ROLES if item[0] not in {"prefreeze_tests", "prefreeze_review"}
)
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
# This registry is mechanically locked to the three final pre-freeze suites.
# A role-11 candidate is rejected before any authority can consume it if the
# registry is later unset or malformed.
EXPECTED_PREFREEZE_TEST_PASSED: dict[str, int] | None = {
    "prefreeze_focused": 23,
    "l3_a1_modules": 972,
    "paper02_full": 1951,
}


def _utc_timestamp(value: Any, context: str) -> datetime:
    if type(value) is not str or re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", value
    ) is None:
        raise ReleaseError(f"{context} must be canonical whole-second UTC")
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError as error:
        raise ReleaseError(f"{context} is not a valid UTC timestamp") from error
    if parsed.strftime("%Y-%m-%dT%H:%M:%SZ") != value:
        raise ReleaseError(f"{context} is not canonical UTC")
    return parsed


def _mode_text(value: Any, context: str, *, expected: str | None = None) -> str:
    if type(value) is not str or re.fullmatch(r"0[0-7]{3}", value) is None:
        raise ReleaseError(f"{context} must be four-character octal mode")
    if expected is not None and value != expected:
        raise ReleaseError(f"{context} differs from expected mode")
    return value


def _live_prefreeze_binding(project_root: Path, relative: str) -> dict[str, Any]:
    raw, info = read_snapshot(project_file(project_root, relative), maximum_bytes=64 * 1024 * 1024)
    return {
        "path": relative,
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "mode": f"{stat.S_IMODE(info.st_mode):04o}",
        "nlink": info.st_nlink,
    }


def _role11_registry() -> Mapping[str, int]:
    counts = EXPECTED_PREFREEZE_TEST_PASSED
    if (
        type(counts) is not dict
        or set(counts) != PREFREEZE_TEST_TOTAL_NAMES
        or any(type(counts[name]) is not int or counts[name] <= 0 for name in counts)
    ):
        raise ReleaseError("V2 role11 final expected passed-count registry is unset")
    return counts


def _role11_fixed_argv(project_root: Path, python_path: str) -> dict[str, list[str]]:
    root = str(project_root)
    pytest_prefix = [python_path, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no"]
    return {
        "role24_machine_verify": [
            python_path,
            f"{root}/scripts/build_r401_val_l3_a1_v2_release_provenance.py",
            "--verify-machine-freeze",
            f"{root}/research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json",
        ],
        "role13_compatibility_verify": [
            python_path,
            f"{root}/scripts/build_r401_val_l3_a1_v2_release_provenance.py",
            "--verify-s0-compatibility",
            f"{root}/research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json",
        ],
        "prefreeze_focused_pytest": [
            *pytest_prefix, "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py",
        ],
        "l3_a1_modules_pytest": [
            *pytest_prefix,
            "tests/test_r401_val_l3_a1_static_cell.py",
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


def _validate_prefreeze_file_binding(
    value: Any,
    expected: Mapping[str, Any],
    context: str,
    *,
    role: str | None = None,
) -> Mapping[str, Any]:
    keys = PREFREEZE_ROLE_ENTRY_KEYS if role is not None else PREFREEZE_FILE_BINDING_KEYS
    binding = exact_keys(value, keys, context)
    if role is not None and binding["role"] != role:
        raise ReleaseError(f"{context} role mismatch")
    if not exact_json_equal(
        {key: binding[key] for key in PREFREEZE_FILE_BINDING_KEYS}, expected
    ):
        raise ReleaseError(f"{context} differs from live unaliased inode")
    safe_relative(binding["path"])
    require_sha256(binding["sha256"], f"{context} hash")
    exact_int(binding["size_bytes"], f"{context} size", minimum=1)
    _mode_text(binding["mode"], f"{context} mode")
    exact_int(binding["nlink"], f"{context} link count", expected=1, minimum=1)
    return binding


def _validate_prefreeze_verify_receipt(
    value: Any,
    *,
    status_value: str,
    binding: Mapping[str, Any],
    context: str,
) -> Mapping[str, Any]:
    receipt = exact_keys(value, PREFREEZE_VERIFY_RECEIPT_KEYS, context)
    if (
        receipt["verification_status"] != status_value
        or receipt["authority"] != "NON_AUTHORITATIVE_VERIFY_ONLY"
        or receipt["candidate_sha256"] != binding["sha256"]
        or receipt["promotion_authorized"] is not False
    ):
        raise ReleaseError(f"{context} verification authority mismatch")
    require_sha256(receipt["candidate_sha256"], f"{context} candidate hash")
    exact_int(
        receipt["size_bytes"], f"{context} candidate size",
        expected=binding["size_bytes"], minimum=1,
    )
    return receipt


def _validate_second_rebuild_receipt(
    project_root: Path,
    value: Any,
    roles: Mapping[str, Mapping[str, Any]],
    context: str,
) -> Mapping[str, Any]:
    receipt = exact_keys(value, PREFREEZE_SECOND_RECEIPT_KEYS, context)
    source = roles["branch_evaluator_source"]
    binary = roles["branch_evaluator_binary"]
    if (
        receipt["verification_status"] != "PASS_SECOND_FRESH_REBUILD"
        or receipt["authority"] != "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY"
        or receipt["source_path"] != source["path"]
        or receipt["source_sha256"] != source["sha256"]
        or receipt["persistent_binary_path"] != binary["path"]
        or receipt["persistent_before_sha256"] != binary["sha256"]
        or receipt["persistent_after_sha256"] != binary["sha256"]
        or receipt["staging_output_sha256"] != binary["sha256"]
        or receipt["staging_output_mode"] != "0755"
        or receipt["persistent_identity_unchanged"] is not True
        or receipt["persistent_overwrite_performed"] is not False
        or receipt["staging_output_removed"] is not True
        or receipt["byte_for_byte_equal"] is not True
        or receipt["scientific_evaluator_dispatched"] is not False
    ):
        raise ReleaseError(f"{context} compiler reproducibility mismatch")
    for name in (
        "source_sha256", "persistent_before_sha256", "persistent_after_sha256",
        "staging_output_sha256",
    ):
        require_sha256(receipt[name], f"{context} {name}")
    for name in (
        "persistent_before_device_id", "persistent_before_inode",
        "persistent_after_device_id", "persistent_after_inode",
    ):
        exact_int(receipt[name], f"{context} {name}", minimum=1)
    _binary_raw, binary_info = read_snapshot(project_file(project_root, binary["path"]))
    if (
        receipt["persistent_before_device_id"] != receipt["persistent_after_device_id"]
        or receipt["persistent_before_inode"] != receipt["persistent_after_inode"]
        or receipt["persistent_before_device_id"] != binary_info.st_dev
        or receipt["persistent_before_inode"] != binary_info.st_ino
    ):
        raise ReleaseError(f"{context} persistent binary inode changed")
    exact_int(
        receipt["staging_output_size_bytes"], f"{context} staging size",
        expected=binary["size_bytes"], minimum=1,
    )
    return receipt


def _parse_prefreeze_pytest_counts(
    stdout: Any,
    context: str,
    *,
    wall_duration_ms: int | None = None,
) -> dict[str, int]:
    if type(stdout) is not str or not stdout.endswith("\n") or "\x00" in stdout:
        raise ReleaseError(f"{context} must end in one pytest summary line")
    try:
        encoded = stdout.encode("utf-8", errors="strict")
    except UnicodeEncodeError as error:
        raise ReleaseError(f"{context} is not valid UTF-8 text") from error
    if len(encoded) > 1024 * 1024:
        raise ReleaseError(f"{context} exceeds the fixed transcript cap")
    if any(
        (ord(character) < 0x20 and character != "\n")
        or 0x7f <= ord(character) <= 0x9f
        or character in "\u2028\u2029"
        for character in stdout
    ):
        raise ReleaseError(f"{context} contains forbidden control output")
    lines = stdout[:-1].split("\n")
    pattern = re.compile(
        r"(?P<counts>[1-9][0-9]{0,3} (?:passed|failed|skipped|xfailed|xpassed)"
        r"(?:, [1-9][0-9]{0,3} (?:passed|failed|skipped|xfailed|xpassed))*) "
        r"in (?P<elapsed>(?:0|[1-9][0-9]{0,2})\.[0-9]{2})s"
        r"(?: \((?P<hours>0):(?P<minutes>[0-5][0-9]):"
        r"(?P<seconds>[0-5][0-9])\))?"
    )
    matches = [pattern.fullmatch(line) for line in lines]
    observed = [item for item in matches if item is not None]
    if len(observed) != 1 or not matches or matches[-1] is None:
        raise ReleaseError(f"{context} lacks exactly one terminal pytest summary")
    if re.search(
        r"(?i)(?<![A-Za-z0-9_])(?:errors?|fail(?:ed|ures?)?|warnings?|"
        r"deselected|skipped|xfail(?:ed)?|xpass(?:ed)?)(?![A-Za-z0-9_])",
        stdout,
    ) is not None:
        raise ReleaseError(f"{context} contains a forbidden nonpass token")
    match = observed[0]
    assert match is not None
    elapsed_whole_text, elapsed_fraction = match.group("elapsed").split(".", 1)
    whole_seconds = int(elapsed_whole_text)
    elapsed_centiseconds = whole_seconds * 100 + int(elapsed_fraction)
    if elapsed_centiseconds > 60000:
        raise ReleaseError(f"{context} pytest duration exceeds 600 seconds")
    elapsed_ms = elapsed_centiseconds * 10
    human_parts = tuple(
        match.group(name) for name in ("hours", "minutes", "seconds")
    )
    if all(part is None for part in human_parts):
        if whole_seconds > 60 or (
            whole_seconds == 60 and elapsed_fraction != "00"
        ):
            raise ReleaseError(f"{context} lacks required long-duration suffix")
    else:
        if any(part is None for part in human_parts):
            raise ReleaseError(f"{context} has a partial duration suffix")
        hours, minutes, seconds = (
            int(part) for part in human_parts if part is not None
        )
        human_seconds = hours * 3600 + minutes * 60 + seconds
        allowed_human_seconds = {whole_seconds}
        # Pytest rounds the decimal to centiseconds but truncates the
        # parenthetic timedelta.  Thus X.995.. may print (X+1).00s and X.
        if elapsed_fraction == "00" and whole_seconds > 60:
            allowed_human_seconds.add(whole_seconds - 1)
        if human_seconds < 60 or human_seconds not in allowed_human_seconds:
            raise ReleaseError(f"{context} has inconsistent duration suffix")
    if wall_duration_ms is not None and elapsed_ms > wall_duration_ms + 5:
        raise ReleaseError(f"{context} pytest duration exceeds outer wall time")
    counts = {name: 0 for name in PREFREEZE_PYTEST_COUNT_KEYS}
    observed_categories: set[str] = set()
    for item in match.group("counts").split(", "):
        count_text, name = item.split(" ", 1)
        if name in observed_categories:
            raise ReleaseError(f"{context} contains duplicate pytest category")
        observed_categories.add(name)
        counts[name] = int(count_text)
    if counts["passed"] <= 0 or any(
        value != 0 for name, value in counts.items() if name != "passed"
    ):
        raise ReleaseError(f"{context} pytest summary is not exact all-pass")
    return counts


def _validate_prefreeze_command(
    value: Any,
    index: int,
    *,
    project_root: Path,
    python_path: str,
    roles: Mapping[str, Mapping[str, Any]],
    locked_counts: Mapping[str, int],
) -> tuple[Mapping[str, Any], dict[str, int] | None]:
    name, kind = PREFREEZE_COMMAND_SPECS[index]
    context = f"V2 role11 command_results[{index}]"
    result = exact_keys(value, PREFREEZE_COMMAND_KEYS, context)
    if result["name"] != name or result["kind"] != kind:
        raise ReleaseError(f"{context} identity/order mismatch")
    argv = result["argv"]
    if type(argv) is not list or not argv or any(
        type(item) is not str or not item or "\x00" in item for item in argv
    ):
        raise ReleaseError(f"{context} argv must be nonempty NUL-free strings")
    fixed = _role11_fixed_argv(project_root, python_path)
    if name == "second_fresh_rebuild":
        prefix = [
            python_path, str(project_root / "scripts/run_r401_val_l3_a1_v2_all_slabs.py"),
            "--second-fresh-rebuild-only", "--output",
        ]
        if argv[:-1] != prefix or re.fullmatch(
            r"/tmp/a416-l3a1-v2-role11-rebuild\.[0-9A-Za-z]{6,}/"
            r"capd_r401_phase_branch_tube_mp_a1",
            argv[-1],
        ) is None:
            raise ReleaseError(f"{context} owned rebuild output mismatch")
    elif not exact_json_equal(argv, fixed[name]):
        raise ReleaseError(f"{context} fixed argv mismatch")
    if (
        result["cwd"] != str(project_root)
        or not exact_json_equal(result["environment"], PREFREEZE_CLEAN_ENVIRONMENT)
    ):
        raise ReleaseError(f"{context} cwd/environment mismatch")
    exact_int(result["return_code"], f"{context} return code", expected=0)
    _utc_timestamp(result["started_at_utc"], f"{context} start time")
    duration = exact_int(result["wall_duration_ms"], f"{context} wall duration", minimum=1)
    if duration > 603000:
        raise ReleaseError(f"{context} exceeded fixed wall envelope")
    for stream in ("stdout", "stderr"):
        text = result[f"{stream}_utf8"]
        if type(text) is not str or "\x00" in text:
            raise ReleaseError(f"{context} {stream} is not NUL-free UTF-8 text")
        raw = text.encode("utf-8", errors="strict")
        if len(raw) > 1024 * 1024:
            raise ReleaseError(f"{context} {stream} exceeds transcript cap")
        require_sha256(result[f"{stream}_sha256"], f"{context} {stream} hash")
        if result[f"{stream}_sha256"] != sha256_bytes(raw):
            raise ReleaseError(f"{context} {stream} hash mismatch")
        exact_int(
            result[f"{stream}_size_bytes"], f"{context} {stream} size",
            expected=len(raw), minimum=0,
        )
    if result["stderr_utf8"] != "":
        raise ReleaseError(f"{context} successful command stderr is nonempty")

    parsed: dict[str, int] | None = None
    if name in PREFREEZE_TEST_RESULT_TOTAL:
        parsed = _parse_prefreeze_pytest_counts(
            result["stdout_utf8"], context, wall_duration_ms=duration
        )
        total_name = PREFREEZE_TEST_RESULT_TOTAL[name]
        if parsed["passed"] != locked_counts[total_name]:
            raise ReleaseError(f"{context} passed count differs from final lock")
        counts = exact_keys(
            result["pytest_counts"], PREFREEZE_PYTEST_COUNT_KEYS,
            f"{context} pytest counts",
        )
        if not exact_json_equal(counts, parsed):
            raise ReleaseError(f"{context} serialized pytest counts mismatch")
        if result["semantic_receipt"] is not None:
            raise ReleaseError(f"{context} pytest semantic receipt must be null")
    else:
        if result["pytest_counts"] is not None:
            raise ReleaseError(f"{context} non-pytest counts must be null")
        if name == "role24_machine_verify":
            receipt = _validate_prefreeze_verify_receipt(
                result["semantic_receipt"],
                status_value="PASS_MACHINE_FREEZE_VERIFY_ONLY",
                binding=roles["machine_freeze"], context=f"{context} receipt",
            )
            expected_stdout = (
                "machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY "
                f"authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256={roles['machine_freeze']['sha256']} "
                f"size_bytes={roles['machine_freeze']['size_bytes']} promotion_authorized=false\n"
            )
            if result["stdout_utf8"] != expected_stdout:
                raise ReleaseError(f"{context} machine transcript mismatch")
        elif name == "role13_compatibility_verify":
            receipt = _validate_prefreeze_verify_receipt(
                result["semantic_receipt"],
                status_value="PASS_S0_COMPATIBILITY_VERIFY_ONLY",
                binding=roles["s0_compatibility"], context=f"{context} receipt",
            )
            expected_stdout = (
                "s0_compatibility_verification=PASS_S0_COMPATIBILITY_VERIFY_ONLY "
                f"authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256={roles['s0_compatibility']['sha256']} "
                f"size_bytes={roles['s0_compatibility']['size_bytes']} promotion_authorized=false\n"
            )
            if result["stdout_utf8"] != expected_stdout:
                raise ReleaseError(f"{context} S0 transcript mismatch")
        elif name == "git_diff_check":
            if result["stdout_utf8"] != "" or result["semantic_receipt"] is not None:
                raise ReleaseError(f"{context} diff-check evidence must be empty/null")
        else:
            receipt = _validate_second_rebuild_receipt(
                project_root, result["semantic_receipt"], roles, f"{context} receipt"
            )
            if result["stdout_utf8"].encode("utf-8") != canonical_json_bytes(receipt):
                raise ReleaseError(f"{context} rebuild transcript/receipt mismatch")
    return result, parsed


def _validate_prefreeze_prerequisites(
    project_root: Path,
    value: Any,
    roles: Mapping[str, Mapping[str, Any]],
    command_results: Sequence[Mapping[str, Any]],
    *,
    capture_commit_oid: str,
) -> None:
    prerequisites = exact_keys(
        value, PREFREEZE_PREREQUISITE_KEYS, "V2 role11 prerequisite bindings"
    )
    machine = exact_keys(
        prerequisites["machine_role10"], PREFREEZE_MACHINE_BINDING_KEYS,
        "V2 role11 machine prerequisite",
    )
    role10 = roles["machine_freeze"]
    if not exact_json_equal(
        {key: machine[key] for key in PREFREEZE_ROLE_ENTRY_KEYS}, role10
    ):
        raise ReleaseError("V2 role11 machine prerequisite/live role mismatch")
    if (
        machine["producer_path"] != roles["scheduler"]["path"]
        or machine["producer_sha256"] != roles["scheduler"]["sha256"]
        or machine["verifier_path"] != roles["release_builder"]["path"]
        or machine["verifier_sha256"] != roles["release_builder"]["sha256"]
        or machine["promotion_authorized"] is not False
        or machine["mode"] != "0644"
    ):
        raise ReleaseError("V2 role11 machine prerequisite tool/authority mismatch")
    if type(machine["publication_commit_oid"]) is not str or re.fullmatch(
        r"[0-9a-f]{40}", machine["publication_commit_oid"]
    ) is None:
        raise ReleaseError("V2 role11 machine publication commit is invalid")
    _git_verify_introduction_binding(
        project_root,
        machine["publication_commit_oid"],
        machine,
        descendant_oid=capture_commit_oid,
    )
    machine_receipt = _validate_prefreeze_verify_receipt(
        machine["verify_receipt"], status_value="PASS_MACHINE_FREEZE_VERIFY_ONLY",
        binding=role10, context="V2 role11 machine prerequisite receipt",
    )
    if not exact_json_equal(machine_receipt, command_results[0]["semantic_receipt"]):
        raise ReleaseError("V2 role11 machine receipt/command mismatch")

    compatibility = exact_keys(
        prerequisites["s0_compatibility_role13"], PREFREEZE_S0_BINDING_KEYS,
        "V2 role11 S0 prerequisite",
    )
    role13 = roles["s0_compatibility"]
    if not exact_json_equal(
        {key: compatibility[key] for key in PREFREEZE_ROLE_ENTRY_KEYS}, role13
    ):
        raise ReleaseError("V2 role11 S0 prerequisite/live role mismatch")
    if (
        compatibility["producer_path"] != roles["s0_adapter"]["path"]
        or compatibility["producer_sha256"] != roles["s0_adapter"]["sha256"]
        or compatibility["promotion_authorized"] is not False
        or compatibility["mode"] != "0644"
    ):
        raise ReleaseError("V2 role11 S0 prerequisite tool/authority mismatch")
    if type(compatibility["publication_commit_oid"]) is not str or re.fullmatch(
        r"[0-9a-f]{40}", compatibility["publication_commit_oid"]
    ) is None:
        raise ReleaseError("V2 role11 S0 publication commit is invalid")
    _git_verify_introduction_binding(
        project_root,
        compatibility["publication_commit_oid"],
        compatibility,
        descendant_oid=capture_commit_oid,
    )
    s0_receipt = _validate_prefreeze_verify_receipt(
        compatibility["verify_receipt"],
        status_value="PASS_S0_COMPATIBILITY_VERIFY_ONLY", binding=role13,
        context="V2 role11 S0 prerequisite receipt",
    )
    if not exact_json_equal(s0_receipt, command_results[1]["semantic_receipt"]):
        raise ReleaseError("V2 role11 S0 receipt/command mismatch")

    absence = exact_keys(
        prerequisites["canonical_absence"],
        {"prefreeze_review_role12_exists", "main_freeze_role54_exists",
         "canonical_result_root_exists", "canonical_operational_root_exists"},
        "V2 role11 canonical absence",
    )
    if any(type(value) is not bool or value is not False for value in absence.values()):
        raise ReleaseError("V2 role11 canonical absence gates must all be false")

    rebuild = exact_keys(
        prerequisites["second_fresh_rebuild_replay"], PREFREEZE_SECOND_REBUILD_KEYS,
        "V2 role11 second rebuild replay",
    )
    if rebuild["command_result_name"] != "second_fresh_rebuild":
        raise ReleaseError("V2 role11 second rebuild command name mismatch")
    expected_command_hash = sha256_bytes(canonical_json_bytes(command_results[6]))
    if rebuild["command_result_sha256"] != expected_command_hash:
        raise ReleaseError("V2 role11 second rebuild command hash mismatch")
    require_sha256(rebuild["command_result_sha256"], "V2 role11 rebuild command hash")
    receipt = _validate_second_rebuild_receipt(
        project_root, rebuild["semantic_receipt"], roles,
        "V2 role11 prerequisite rebuild receipt"
    )
    if not exact_json_equal(receipt, command_results[6]["semantic_receipt"]):
        raise ReleaseError("V2 role11 rebuild receipt/command mismatch")


def _validate_prefreeze_tests_payload(
    project_root: Path,
    payload: Any,
    *,
    require_current: bool = False,
) -> None:
    """Replay one exact role-11 image without starting any child process."""

    locked_counts = _role11_registry()
    exact_keys(payload, PREFREEZE_TEST_KEYS, "V2 role11 prefreeze tests")
    exact_int(payload["schema_version"], "V2 role11 schema", expected=1)
    if (
        payload["protocol_id"] != "R401-VAL-L3-A1-PREFREEZE-TESTS"
        or payload["artifact_role"] != "PREFREEZE_TEST_RECORD"
        or payload["artifact_status"] != "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW"
        or payload["authority"] != "PREFREEZE_TEST_EVIDENCE_ONLY"
        or payload["scientific_licensing_enabled"] is not False
        or payload["production_authorized"] is not False
        or payload["scientific_dispatch_performed"] is not False
        or payload["claim_boundary"] != PREFREEZE_TEST_CLAIM_BOUNDARY
    ):
        raise ReleaseError("V2 role11 identity/authority mismatch")
    _require_null_statuses(payload, "V2 role11")
    recorded_at = _utc_timestamp(payload["recorded_at_utc"], "V2 role11 recorded time")

    held_out = exact_keys(
        payload["held_out_policy"],
        {"held_out_l3_scientific_outputs_read", "held_out_l3_evaluator_dispatched",
         "scientific_evaluator_dispatch_count", "new_archive_scope",
         "s0_archive_access", "canonical_result_created"},
        "V2 role11 held-out policy",
    )
    expected_held_out = {
        "held_out_l3_scientific_outputs_read": False,
        "held_out_l3_evaluator_dispatched": False,
        "scientific_evaluator_dispatch_count": 0,
        "new_archive_scope": "TEMPORARY_MOCK_ONLY",
        "s0_archive_access": "READ_ONLY_SEALED_PUBLIC_SIX_CELL",
        "canonical_result_created": False,
    }
    if not exact_json_equal(held_out, expected_held_out):
        raise ReleaseError("V2 role11 held-out policy mismatch")

    live_roles: dict[str, dict[str, Any]] = {}
    entries = payload["pre_review_input_roles"]
    if type(entries) is not list or len(entries) != 51 or len(PREFREEZE_INPUT_ROLES) != 51:
        raise ReleaseError("V2 role11 must contain exact ordered 51-role snapshot")
    for index, ((role, relative), entry) in enumerate(
        zip(PREFREEZE_INPUT_ROLES, entries, strict=True)
    ):
        live = {"role": role, **_live_prefreeze_binding(project_root, relative)}
        _validate_prefreeze_file_binding(
            entry, {key: live[key] for key in PREFREEZE_FILE_BINDING_KEYS},
            f"V2 role11 input role {index}", role=role,
        )
        live_roles[role] = live
    if len({row["role"] for row in entries}) != 51 or len({row["path"] for row in entries}) != 51:
        raise ReleaseError("V2 role11 input role/path alias")

    role5_payload = strict_json_loads(
        read_snapshot(project_file(
            project_root, dict(INPUT_ROLES)["implementation_design_review"]
        ))[0],
        canonical="compact",
    )
    _validate_role5(project_root, role5_payload, tuple(live_roles.values()))
    role5_anchors = {
        row["role"]: row for row in role5_payload["reviewed_v2_inputs"]
    }

    tools = exact_keys(
        payload["evidence_tool_bindings"], set(PREFREEZE_TOOL_ROLES),
        "V2 role11 evidence tools",
    )
    for name, role in PREFREEZE_TOOL_ROLES.items():
        live = {key: live_roles[role][key] for key in PREFREEZE_FILE_BINDING_KEYS}
        _validate_prefreeze_file_binding(tools[name], live, f"V2 role11 tool {name}")
        if not exact_json_equal(
            role5_anchors.get(role),
            {key: live_roles[role][key] for key in ("role", "path", "sha256")},
        ):
            raise ReleaseError(f"V2 role11 tool {name} differs from role5 stable anchor")
    if len({tools[name]["path"] for name in tools}) != 3:
        raise ReleaseError("V2 role11 evidence tool paths are not unique")

    machine_payload = strict_json_loads(
        read_snapshot(project_file(project_root, dict(INPUT_ROLES)["machine_freeze"]))[0],
        canonical="compact",
    )
    validate_formal_machine_freeze(project_root, machine_payload, live_roles)
    s0_payload = strict_json_loads(
        read_snapshot(project_file(project_root, dict(INPUT_ROLES)["s0_compatibility"]))[0],
        canonical="compact",
    )
    _validate_s0_payload(project_root, s0_payload, live_roles)

    repository = exact_keys(
        payload["repository_snapshot"], PREFREEZE_REPOSITORY_KEYS,
        "V2 role11 repository snapshot",
    )
    root_from_machine = machine_payload["filesystem"]["project_root"]
    if (
        repository["authority_root"] != root_from_machine
        or repository["authority_root"] != str(project_root)
        or repository["branch"] != "main"
        or repository["origin_url"] != "git@github.com:maris205/hilbert-polya-structure.git"
        or repository["capture_commit_oid"] != repository["origin_main_oid"]
        or repository["capture_commit_oid"] != repository["live_remote_main_oid"]
        or repository["head_equals_origin_main"] is not True
        or repository["head_equals_live_remote_main"] is not True
        or repository["worktree_clean_before"] is not True
        or repository["worktree_clean_after"] is not True
    ):
        raise ReleaseError("V2 role11 repository authority snapshot mismatch")
    for name in ("capture_commit_oid", "capture_tree_oid", "origin_main_oid", "live_remote_main_oid"):
        if type(repository[name]) is not str or re.fullmatch(r"[0-9a-f]{40}", repository[name]) is None:
            raise ReleaseError(f"V2 role11 repository {name} is invalid")
    exact_int(repository["ahead"], "V2 role11 repository ahead", expected=0)
    exact_int(repository["behind"], "V2 role11 repository behind", expected=0)
    captured_tree = _git_verify_commit_bindings(project_root, repository["capture_commit_oid"], entries)
    if captured_tree != repository["capture_tree_oid"]:
        raise ReleaseError("V2 role11 repository commit/tree snapshot mismatch")
    def validate_current_state() -> None:
        for relative, label in (
            (dict(INPUT_ROLES)["prefreeze_tests"], "canonical role11"),
            (dict(INPUT_ROLES)["prefreeze_review"], "role12 review"),
            (MAIN_FREEZE_RELATIVE.as_posix(), "role54 main freeze"),
            (RESULT_RELATIVE.as_posix(), "canonical result root"),
            (f"{RESULT_RELATIVE}{OPERATIONAL_SUFFIX}", "canonical operational root"),
        ):
            _assert_absent_namespace(project_file(project_root, relative), label)
        _validate_current_git_snapshot(project_root, repository, entries)

    if require_current:
        validate_current_state()

    results = payload["command_results"]
    if type(results) is not list or len(results) != 7:
        raise ReleaseError("V2 role11 must contain exact ordered seven commands")
    python_path = machine_payload["python_arb"]["executable_path"]
    if type(python_path) is not str or not python_path.startswith("/"):
        raise ReleaseError("V2 role11 machine Python token is invalid")
    validated_results: list[Mapping[str, Any]] = []
    parsed_counts: dict[str, dict[str, int]] = {}
    previous_start: datetime | None = None
    for index, result in enumerate(results):
        validated, counts = _validate_prefreeze_command(
            result, index, project_root=project_root, python_path=python_path,
            roles=live_roles, locked_counts=locked_counts,
        )
        started = _utc_timestamp(validated["started_at_utc"], f"V2 role11 command {index} time")
        if (previous_start is not None and started < previous_start) or started > recorded_at:
            raise ReleaseError("V2 role11 command timestamps are not ordered/bounded")
        previous_start = started
        validated_results.append(validated)
        if counts is not None:
            parsed_counts[validated["name"]] = counts

    _validate_prefreeze_prerequisites(
        project_root,
        payload["prerequisite_bindings"],
        live_roles,
        validated_results,
        capture_commit_oid=repository["capture_commit_oid"],
    )
    totals = exact_keys(
        payload["test_totals"], PREFREEZE_TEST_TOTAL_NAMES, "V2 role11 test totals"
    )
    by_name = {row["name"]: row for row in validated_results}
    for result_name, total_name in PREFREEZE_TEST_RESULT_TOTAL.items():
        total = exact_keys(
            totals[total_name], PREFREEZE_TEST_TOTAL_KEYS,
            f"V2 role11 total {total_name}",
        )
        expected_counts = parsed_counts[result_name]
        for key in PREFREEZE_PYTEST_COUNT_KEYS:
            exact_int(total[key], f"V2 role11 total {total_name} {key}",
                      expected=expected_counts[key])
        exact_int(
            total["wall_duration_ms"], f"V2 role11 total {total_name} duration",
            expected=by_name[result_name]["wall_duration_ms"], minimum=1,
        )
    if not exact_json_equal(payload["covered_gates"], list(PREFREEZE_COVERED_GATES)):
        raise ReleaseError("V2 role11 covered gates mismatch")
    if len(canonical_json_bytes(payload)) > 4 * 1024 * 1024:
        raise ReleaseError("V2 role11 candidate exceeds fixed four-MiB bound")
    if require_current:
        # Absence and repository cleanliness are namespace assertions rather
        # than leaf snapshots, so replay them explicitly at the terminal edge.
        validate_current_state()


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
    "executable_path", "executable_sha256", "version", "build_recipe",
    "fresh_rebuild_receipt", "transfer_evidence",
}
FORMAL_MACHINE_BUILD_RECIPE_KEYS = {
    "cwd", "environment", "umask", "staging_output_token", "argv_template",
    "argv_template_sha256",
}
FORMAL_MACHINE_FRESH_REBUILD_RECEIPT_KEYS = {
    "cwd", "environment", "umask", "staging_directory",
    "staging_output_path", "argv", "argv_sha256", "stdout", "stderr",
    "stdout_sha256", "stderr_sha256", "return_code", "output_sha256",
    "output_size_bytes", "output_mode", "output_build_id", "output_dt_needed",
    "output_dt_needed_sha256", "output_soname", "shell_used",
}
FORMAL_MACHINE_TRANSFER_EVIDENCE_KEYS = {
    "staging_output_sha256", "staging_output_size_bytes",
    "staging_output_mode", "branch_calibration_binary_sha256",
    "persistent_before_sha256",
    "persistent_before_size_bytes", "persistent_before_mode",
    "persistent_before_device_id", "persistent_before_inode",
    "persistent_after_sha256", "persistent_after_size_bytes",
    "persistent_after_mode", "persistent_after_device_id",
    "persistent_after_inode", "byte_for_byte_equal",
    "persistent_identity_unchanged", "persistent_overwrite_performed",
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
    "scripts/run_r401_val_l3_a1_v2_all_slabs.py"
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
FORMAL_MACHINE_BUILD_ENVIRONMENT = {
    "PATH": "/usr/bin:/bin",
    "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8",
    "TZ": "UTC",
    "PYTHONHASHSEED": "0",
    "PYTHONNOUSERSITE": "1",
    "PYTHONDONTWRITEBYTECODE": "1",
}
FORMAL_MACHINE_STAGING_OUTPUT_TOKEN = "@STAGING_BINARY@"
FORMAL_MACHINE_VERIFY_STATUS = "PASS_MACHINE_FREEZE_VERIFY_ONLY"
FORMAL_MACHINE_VERIFY_AUTHORITY = "NON_AUTHORITATIVE_VERIFY_ONLY"
FORMAL_MACHINE_VERIFY_CLAIM_BOUNDARY = (
    "read-only machine-freeze schema and live-binding replay only; no freeze "
    "publication, evaluator dispatch, production authorization, scientific "
    "component, theorem, or release authority"
)
FORMAL_MACHINE_VERIFY_ROLES: tuple[tuple[str, str], ...] = (
    ("scheduler", FORMAL_MACHINE_CAPTURE_TOOL),
    ("static_evaluator", FORMAL_MACHINE_STATIC_EVALUATOR),
    ("branch_evaluator_source", FORMAL_MACHINE_BRANCH_SOURCE),
    ("branch_evaluator_binary", FORMAL_MACHINE_BRANCH_BINARY),
    ("l1_final_plan", "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"),
)
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


def _machine_safe_relative(value: Any, context: str) -> PurePosixPath:
    if type(value) is not str or not value or value.startswith("/"):
        raise PathContractError(f"{context}: unsafe relative path")
    if "\x00" in value or "\\" in value or "//" in value or value.endswith("/"):
        raise PathContractError(f"{context}: unsafe relative path")
    pure = PurePosixPath(value)
    if pure.is_absolute() or pure.as_posix() != value or any(
        part in ("", ".", "..") for part in pure.parts
    ):
        raise PathContractError(f"{context}: noncanonical relative path")
    return pure


def _exact_machine_verify_path(value: Any) -> Path:
    if type(value) is str:
        text = value
    elif isinstance(value, Path):
        text = os.fspath(value)
    else:
        raise PathContractError("machine evidence path must be string/path")
    if (
        not text or "\x00" in text or not text.startswith("/")
        or text.startswith("//") or "//" in text[1:] or "\\" in text
        or text.endswith("/")
    ):
        raise PathContractError("machine evidence path is not canonical absolute")
    pure = PurePosixPath(text)
    if pure.as_posix() != text or any(part in ("", ".", "..") for part in pure.parts[1:]):
        raise PathContractError("machine evidence path contains traversal/alias")
    return lexical_absolute(Path(text))


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
        relative = _machine_safe_relative(value, "Python conda manifest path")
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
    raw, info = _read_machine_manifest_uncached(canonical)
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
    payload, raw = strict_json_image(path)
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
    payload = strict_json_loads(raw, canonical="compact")
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
    payload = strict_json_loads(raw)
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
            relative = _machine_safe_relative(value, "Python conda manifest path")
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
            relative = _machine_safe_relative(relative_raw, "python-flint RECORD path")
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
        relative = _machine_safe_relative(path_text, "CAPD Git index path").as_posix()
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
    recipe = exact_keys(
        compiler["build_recipe"], FORMAL_MACHINE_BUILD_RECIPE_KEYS,
        "machine compiler build recipe",
    )
    if (
        recipe["cwd"] != str(project_root)
        or recipe["umask"] != "0022"
        or not exact_json_equal(
            recipe["environment"], FORMAL_MACHINE_BUILD_ENVIRONMENT
        )
        or recipe["staging_output_token"] != FORMAL_MACHINE_STAGING_OUTPUT_TOKEN
    ):
        raise ReleaseError("machine build recipe environment/identity mismatch")
    expected_template = [
        compiler["executable_path"], "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(project_file(project_root, FORMAL_MACHINE_BRANCH_SOURCE)),
        *capd_tokens, "-o",
        FORMAL_MACHINE_STAGING_OUTPUT_TOKEN,
    ]
    if (
        not exact_json_equal(recipe["argv_template"], expected_template)
        or sha256_bytes(canonical_json_bytes(recipe["argv_template"]))
        != require_sha256(
            recipe["argv_template_sha256"], "machine build template hash"
        )
    ):
        raise ReleaseError("machine semantic build-recipe template mismatch")

    receipt = exact_keys(
        compiler["fresh_rebuild_receipt"],
        FORMAL_MACHINE_FRESH_REBUILD_RECEIPT_KEYS,
        "machine fresh-rebuild receipt",
    )
    if (
        receipt["cwd"] != recipe["cwd"]
        or receipt["umask"] != recipe["umask"]
        or not exact_json_equal(receipt["environment"], recipe["environment"])
    ):
        raise ReleaseError("machine fresh-rebuild execution context mismatch")
    staging_directory = _exact_machine_verify_path(
        _machine_nonempty_string(
            receipt["staging_directory"], "machine fresh staging directory"
        )
    )
    staging_output = _exact_machine_verify_path(
        _machine_nonempty_string(
            receipt["staging_output_path"], "machine fresh staging output"
        )
    )
    persistent_path = project_file(project_root, FORMAL_MACHINE_BRANCH_BINARY)
    if (
        staging_directory.parent != Path("/tmp")
        or staging_directory == project_root
        or staging_output.parent != staging_directory
        or staging_output.name != persistent_path.name
        or staging_output == persistent_path
    ):
        raise PathContractError("machine fresh rebuild is not a private /tmp staging build")
    expected_receipt_argv = [*expected_template[:-1], str(staging_output)]
    if (
        not exact_json_equal(receipt["argv"], expected_receipt_argv)
        or sha256_bytes(canonical_json_bytes(receipt["argv"]))
        != require_sha256(receipt["argv_sha256"], "machine fresh argv hash")
    ):
        raise ReleaseError("machine fresh-rebuild argv/template substitution mismatch")
    if (
        type(receipt["return_code"]) is not int
        or receipt["return_code"] != 0
        or receipt["stdout"] != ""
        or receipt["stderr"] != ""
        or receipt["stdout_sha256"] != FORMAL_MACHINE_EMPTY_SHA256
        or receipt["stderr_sha256"] != FORMAL_MACHINE_EMPTY_SHA256
        or receipt["shell_used"] is not False
        or receipt["output_sha256"] != branch["sha256"]
        or type(receipt["output_size_bytes"]) is not int
        or receipt["output_size_bytes"] != len(binary_raw)
        or type(receipt["output_mode"]) is not int
        or receipt["output_mode"] != 0o755
        or receipt["output_build_id"] != live_build_id
        or not exact_json_equal(receipt["output_dt_needed"], live_needed)
        or sha256_bytes(canonical_json_bytes(receipt["output_dt_needed"]))
        != require_sha256(
            receipt["output_dt_needed_sha256"],
            "machine fresh DT_NEEDED hash",
        )
        or receipt["output_soname"] is not None
    ):
        raise ReleaseError("machine fresh-rebuild transcript/output mismatch")

    transfer = exact_keys(
        compiler["transfer_evidence"], FORMAL_MACHINE_TRANSFER_EVIDENCE_KEYS,
        "machine build transfer evidence",
    )
    hash_keys = (
        "staging_output_sha256", "branch_calibration_binary_sha256",
        "persistent_before_sha256", "persistent_after_sha256",
    )
    for key in hash_keys:
        if require_sha256(transfer[key], f"machine transfer {key}") != branch["sha256"]:
            raise ReleaseError("machine staging/calibration/persistent hash mismatch")
    for key in (
        "staging_output_size_bytes", "persistent_before_size_bytes",
        "persistent_after_size_bytes",
    ):
        if _machine_positive_int(transfer[key], f"machine transfer {key}") != len(binary_raw):
            raise ReleaseError("machine staging/persistent size mismatch")
    for key in (
        "staging_output_mode", "persistent_before_mode", "persistent_after_mode",
    ):
        if type(transfer[key]) is not int or transfer[key] != 0o755:
            raise ReleaseError("machine staging/persistent mode mismatch")
    for key in (
        "persistent_before_device_id", "persistent_before_inode",
        "persistent_after_device_id", "persistent_after_inode",
    ):
        _machine_positive_int(transfer[key], f"machine transfer {key}")
    if (
        transfer["staging_output_sha256"] != receipt["output_sha256"]
        or transfer["staging_output_size_bytes"] != receipt["output_size_bytes"]
        or transfer["staging_output_mode"] != receipt["output_mode"]
        or transfer["persistent_before_device_id"] != binary_info.st_dev
        or transfer["persistent_after_device_id"] != binary_info.st_dev
        or transfer["persistent_before_inode"] != binary_info.st_ino
        or transfer["persistent_after_inode"] != binary_info.st_ino
        or transfer["byte_for_byte_equal"] is not True
        or transfer["persistent_identity_unchanged"] is not True
        or transfer["persistent_overwrite_performed"] is not False
    ):
        raise ReleaseError("machine no-overwrite transfer evidence mismatch")
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

MACHINE_FREEZE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "production_authorized", "capture",
    "machine_requirements", "machine_observations", "python_arb", "capd",
    "compiler", "branch_binary", "runtime_libraries", "resource_evidence",
    "resource_admission", "filesystem", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
MACHINE_NESTED_KEYS = {
    "capture": {"captured_at_utc", "capture_tool_path", "capture_tool_sha256", "boot_id_sha256"},
    "machine_requirements": set(formal_machine_requirements()),
    "machine_observations": {
        "logical_cpu_count", "memory_limit_bytes", "result_parent_free_bytes",
        "idle_baseline_rss_bytes", "representative_static_peak_rss_bytes",
        "representative_branch_peak_rss_bytes",
    },
    "resource_admission": {
        "static_required_bytes", "branch_required_bytes", "admitted_required_bytes",
        "admission_limit_bytes", "static_inequality_passed",
        "branch_inequality_passed", "storage_launch_passed",
    },
    "resource_evidence": {
        "static_payload_raw_utf8", "static_payload_sha256", "branch_payload_raw_utf8",
        "branch_payload_sha256", "persistent_binary_sha256",
    },
    "filesystem": {
        "project_root", "result_parent", "operational_parent", "project_device_id",
        "result_device_id", "operational_device_id", "same_filesystem",
    },
}


def validate_formal_machine_freeze(
    project_root: Path,
    machine: Any,
    roles: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Run the independent full live machine/toolchain/resource replay."""

    root = lexical_absolute(project_root)
    role_hashes = {
        role: row["sha256"]
        for role, row in roles.items()
        if type(role) is str and type(row) is dict and "sha256" in row
    }
    return _validate_formal_machine_freeze(
        root, machine, expected_role_hashes=role_hashes
    )


def _validate_main(
    project_root: Path,
    main: Any,
    records: Sequence[Mapping[str, str]],
    images: Mapping[str, bytes],
) -> Mapping[str, Any]:
    exact_keys(main, MAIN_FREEZE_KEYS, "V2 main freeze")
    exact_int(main["schema_version"], "main schema", expected=1)
    if (
        main["protocol_id"] != PROTOCOL_ID
        or main["artifact_role"] != "MAIN_FREEZE"
        or main["status"] != "FROZEN_FOR_PRODUCTION"
        or main["authority"] != "INDEPENDENT_PREFREEZE_REVIEW"
        or main["scientific_licensing_enabled"] is not True
    ):
        raise ReleaseError("V2 main freeze identity/authority mismatch")
    for forbidden in ("sha256", "freeze_sha256", "main_freeze_sha256"):
        if forbidden in main:
            raise ReleaseError("V2 main freeze contains a forbidden self hash")
    if not exact_json_equal(main["matrix"], matrix_payload()) or main["matrix_id"] != matrix_id():
        raise ReleaseError("V2 main freeze matrix mismatch")
    expected_records = list(records)
    if not exact_json_equal(main["input_roles"], expected_records):
        raise ReleaseError("V2 main freeze ordered 53-role handshake mismatch")
    if len(main["input_roles"]) != 53:
        raise ReleaseError("V2 main freeze does not contain exactly 53 roles")
    for row in main["input_roles"]:
        exact_keys(row, {"role", "path", "sha256"}, "V2 main role row")
        safe_relative(row["path"])
        require_sha256(row["sha256"], "V2 main role hash")
    roles = {row["role"]: row for row in records}
    role5 = strict_json_loads(images["implementation_design_review"], canonical="compact")
    _validate_role5(project_root, role5, records)
    machine = strict_json_loads(images["machine_freeze"], canonical="compact")
    validate_formal_machine_freeze(project_root, machine, roles)
    role11 = strict_json_loads(images["prefreeze_tests"], canonical="compact")
    _validate_prefreeze_tests_payload(project_root, role11)
    if main["machine_freeze_sha256"] != roles["machine_freeze"]["sha256"]:
        raise ReleaseError("V2 main/machine freeze hash mismatch")
    exact_keys(main["prefreeze_review"], {"path", "sha256", "verdict"}, "main review binding")
    if not exact_json_equal(main["prefreeze_review"], {
        "path": roles["prefreeze_review"]["path"],
        "sha256": roles["prefreeze_review"]["sha256"],
        "verdict": "ACCEPT_FOR_FREEZE",
    }):
        raise ReleaseError("V2 main pre-freeze review binding mismatch")
    expected_sections = {
        "serializers": formal_serializers(),
        "scheduler": formal_scheduler_policy(),
        "limits": formal_limits(),
        "status_tables": formal_status_tables(),
        "archive_layout": formal_archive_layout(),
        "machine_requirements": formal_machine_requirements(),
        "failure_policy": formal_failure_policy(),
        "execution_policy": formal_execution_policy(),
    }
    for key, expected in expected_sections.items():
        if not exact_json_equal(main[key], expected):
            raise ReleaseError(f"V2 main exact policy section mismatch: {key}")
    expected_evaluators = {
        "static": {
            "path": roles["static_evaluator"]["path"],
            "sha256": roles["static_evaluator"]["sha256"],
            "abi": "PYTHON_STATIC_ABI_26_STRINGS_V1", "argv_count": 26,
        },
        "branch": {
            "source_path": roles["branch_evaluator_source"]["path"],
            "source_sha256": roles["branch_evaluator_source"]["sha256"],
            "binary_path": roles["branch_evaluator_binary"]["path"],
            "binary_sha256": roles["branch_evaluator_binary"]["sha256"],
            "runtime_path": roles["branch_runtime"]["path"],
            "runtime_sha256": roles["branch_runtime"]["sha256"],
            "abi": "CAPD_BRANCH_ABI_12_STRINGS_V1", "argv_count": 12,
        },
    }
    if not exact_json_equal(main["evaluators"], expected_evaluators):
        raise ReleaseError("V2 main evaluator bindings mismatch")
    expected_checkers = {
        name: {"path": roles[role]["path"], "sha256": roles[role]["sha256"]}
        for name, role in (
            ("static", "static_checker_source"),
            ("branch", "branch_checker_source"),
            ("composite", "composite_checker_source"),
            ("release_builder", "release_builder"),
        )
    }
    if not exact_json_equal(main["checkers"], expected_checkers):
        raise ReleaseError("V2 main checker bindings mismatch")
    if main["claim_boundary"] != MAIN_FREEZE_CLAIM_BOUNDARY:
        raise ReleaseError("V2 main claim boundary mismatch")
    _require_null_statuses(main, "main freeze")
    if roles["release_builder"]["sha256"] != sha256_bytes(SCRIPT.read_bytes()):
        raise ReleaseError("executing V2 release builder differs from frozen role24")
    return main


def validate_formal_main_freeze(
    project_root: Path,
    main_path: Path | None = None,
) -> AuthoritySnapshot:
    root = lexical_absolute(project_root)
    records, images = _capture_input_roles(root)
    path = main_path if main_path is not None else project_file(root, MAIN_FREEZE_RELATIVE)
    path = lexical_absolute(path)
    main, raw = strict_json_image(path, canonical="compact")
    validated = _validate_main(root, main, records, images)
    return AuthoritySnapshot(root, records, images, validated, raw, path)


def _build_expected_main_freeze(project_root: Path) -> dict[str, Any]:
    records, images = _capture_input_roles(project_root)
    roles = {row["role"]: row for row in records}
    payload = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MAIN_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "INDEPENDENT_PREFREEZE_REVIEW",
        "scientific_licensing_enabled": True,
        "matrix": matrix_payload(),
        "matrix_id": matrix_id(),
        "input_roles": list(records),
        "machine_freeze_sha256": roles["machine_freeze"]["sha256"],
        "prefreeze_review": {
            "path": roles["prefreeze_review"]["path"],
            "sha256": roles["prefreeze_review"]["sha256"],
            "verdict": "ACCEPT_FOR_FREEZE",
        },
        "serializers": formal_serializers(),
        "scheduler": formal_scheduler_policy(),
        "limits": formal_limits(),
        "status_tables": formal_status_tables(),
        "evaluators": {
            "static": {
                "path": roles["static_evaluator"]["path"],
                "sha256": roles["static_evaluator"]["sha256"],
                "abi": "PYTHON_STATIC_ABI_26_STRINGS_V1", "argv_count": 26,
            },
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
        "checkers": {
            name: {"path": roles[role]["path"], "sha256": roles[role]["sha256"]}
            for name, role in (
                ("static", "static_checker_source"),
                ("branch", "branch_checker_source"),
                ("composite", "composite_checker_source"),
                ("release_builder", "release_builder"),
            )
        },
        "archive_layout": formal_archive_layout(),
        "machine_requirements": formal_machine_requirements(),
        "failure_policy": formal_failure_policy(),
        "execution_policy": formal_execution_policy(),
        "claim_boundary": MAIN_FREEZE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    _validate_main(project_root, payload, records, images)
    return payload


def build_expected_main_freeze(project_root: Path) -> dict[str, Any]:
    with capture_input_generation():
        return _build_expected_main_freeze(lexical_absolute(project_root))


def verify_formal_main_freeze_path(path: Path | str) -> dict[str, Any]:
    candidate = lexical_absolute(path)
    with capture_input_generation():
        main, raw, _ = _read_candidate_policy(
            candidate, canonical=project_file(ROOT, MAIN_FREEZE_RELATIVE),
            temporary_mode=0o600, maximum_bytes=1024 * 1024,
        )
        records, images = _capture_input_roles(ROOT)
        _validate_main(ROOT, main, records, images)
    return {
        "verification_status": "PASS_MAIN_FREEZE_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "promotion_authorized": False,
    }


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
AGGREGATE_MANIFEST_KEYS = AGGREGATE_COMMON_KEYS | {
    "artifact_role", "cell_manifests", "summary",
}
STATIC_CELL_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "scientific_licensing_enabled", "matrix_id", "freeze_sha256",
    "main_freeze_sha256", "run_config_sha256", "cell",
    "semantic_invocation_sha256", "scheduler_classification", "evaluator_status",
    "record", "files", "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}
BRANCH_CELL_MANIFEST_KEYS = {
    "artifact_role", "authority", "claim_boundary", "component_status",
    "final_status", "freeze_sha256", "matrix_id", "milestone_status",
    "protocol_id", "run_config_sha256", "schema_version",
    "scientific_licensing_enabled", "theorem_status", "budgets",
    "cell_identity", "files", "task_binding_sha256",
}
STATIC_FILE_BINDING_KEYS = {"path", "sha256", "size_bytes", "serializer", "truncated"}
AGGREGATE_ENTRY_KEYS = {
    "cell", "path", "sha256", "size_bytes", "evaluator_status",
    "scheduler_classification",
}
COMPONENT_CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_aggregate_summary_sha256", "component_aggregate_manifest_sha256",
    "replay_counts", "cross_precision", "diagnostics", "failures",
    "source_bindings", "claim_boundary", "milestone_status", "theorem_status",
    "final_status",
}
POSTCHECK_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "postcheck_status", "passed", "checker_path", "checker_sha256",
    "main_freeze_sha256", "run_config_sha256", "bound_artifacts",
    "replay_counts", "failures", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status", "theorem_status",
    "final_status",
}

RESERVED_AUTHORITY_KEYS = {
    "authority", "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status", "release_status", "checker_status",
    "postcheck_status", "promotion_authorized", "scientific_licensing_enabled",
}


def _reject_nested_authority(value: Any, context: str) -> None:
    if type(value) is dict:
        for key, child in value.items():
            if key in RESERVED_AUTHORITY_KEYS:
                raise ReleaseError(f"unexpected nested authority in {context}: {key}")
            _reject_nested_authority(child, context)
    elif type(value) is list:
        for child in value:
            _reject_nested_authority(child, context)


def _validate_root_producer_authority(
    payload: Mapping[str, Any], context: str, claim_boundary: str
) -> None:
    permitted = {
        "authority", "claim_boundary", "component_status", "milestone_status",
        "theorem_status", "final_status", "scientific_licensing_enabled",
    }
    if payload.get("authority") != "PRODUCER_ONLY":
        raise ReleaseError(f"{context} producer authority mismatch")
    if payload.get("claim_boundary") != claim_boundary:
        raise ReleaseError(f"{context} claim boundary mismatch")
    if payload.get("scientific_licensing_enabled") is not False:
        raise ReleaseError(f"{context} unexpectedly licenses science")
    _require_null_statuses(payload, context)
    for key, child in payload.items():
        if key not in permitted:
            _reject_nested_authority(child, context)


def _validate_publication_transient(
    result: Path,
    transient: PublicationTransient,
    *,
    destination_name: str,
) -> None:
    if (
        transient.parent != result
        or re.fullmatch(
            rf"\.{re.escape(destination_name)}\.publish-[0-9a-f]{{32}}",
            transient.name,
        ) is None
        or transient.mode != 0o644
        or transient.nlink != 1
    ):
        raise PathContractError("invalid release publication transient declaration")
    parent_fd = os.open(
        result,
        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0),
    )
    descriptor: int | None = None
    try:
        descriptor = os.open(
            transient.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        raw, info = _read_fd_all(
            descriptor, len(transient.raw), "release publication transient"
        )
        if (
            raw != transient.raw
            or (info.st_dev, info.st_ino)
            != (transient.device_id, transient.inode)
            or not stat.S_ISREG(info.st_mode)
            or stat.S_IMODE(info.st_mode) != transient.mode
            or info.st_nlink != transient.nlink
        ):
            raise PathContractError("release publication transient changed")
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def _validate_result_namespace(
    result: Path,
    *,
    allow_release: bool,
    require_report: bool = True,
    transient: PublicationTransient | None = None,
) -> None:
    expected_root = {
        "run_config.json", "static", "branch", "independent_static_checker.json",
        "STATIC_POSTCHECK_STATUS.json", "independent_branch_checker.json",
        "BRANCH_POSTCHECK_STATUS.json", "composite_summary.json",
        "composite_manifest.json", "independent_checker.json", "POSTCHECK_STATUS.json",
    }
    if require_report:
        expected_root.add(REPORT_NAME)
    if allow_release:
        expected_root.add(RELEASE_NAME)
    if transient is not None:
        if allow_release:
            raise PathContractError("release destination and publication transient coexist")
        _validate_publication_transient(
            result,
            transient,
            destination_name=REPORT_NAME if not require_report else RELEASE_NAME,
        )
        expected_root.add(transient.name)
    try:
        actual_root = {entry.name for entry in result.iterdir()}
    except OSError as error:
        raise PathContractError(f"cannot scan V2 result root: {error}") from error
    if actual_root != expected_root:
        raise PathContractError(f"V2 result root namespace mismatch: {sorted(actual_root)}")
    transient_name = transient.name if transient is not None else None
    for name in expected_root - {"static", "branch", transient_name}:
        read_snapshot(result / name)
    for component in ("static", "branch"):
        root = result / component
        if root.is_symlink() or not root.is_dir():
            raise PathContractError(f"V2 {component} root is not a real directory")
        if {entry.name for entry in root.iterdir()} != {
            "cells", "cell_manifests", "aggregate_summary.json", "aggregate_manifest.json"
        }:
            raise PathContractError(f"V2 {component} root namespace mismatch")
        cells_root = root / "cells"
        manifests_root = root / "cell_manifests"
        precision_names = {str(bits) for bits in PRECISIONS}
        if (
            cells_root.is_symlink()
            or manifests_root.is_symlink()
            or not cells_root.is_dir()
            or not manifests_root.is_dir()
            or {entry.name for entry in cells_root.iterdir()} != precision_names
            or {entry.name for entry in manifests_root.iterdir()} != precision_names
        ):
            raise PathContractError(
                f"V2 {component} precision-root namespace mismatch"
            )
        for bits in PRECISIONS:
            cells = cells_root / str(bits)
            manifests = manifests_root / str(bits)
            if cells.is_symlink() or manifests.is_symlink() or not cells.is_dir() or not manifests.is_dir():
                raise PathContractError(f"V2 {component} precision namespace is aliased")
            if {entry.name for entry in cells.iterdir()} != set(SLABS):
                raise PathContractError(f"V2 {component} cell slab namespace mismatch")
            if {entry.name for entry in manifests.iterdir()} != {f"{slab}.json" for slab in SLABS}:
                raise PathContractError(f"V2 {component} manifest slab namespace mismatch")
            expected_files = (
                {"proof.json", "stdout.txt", "stderr.txt", "record.json"}
                if component == "static"
                else {"stdout.txt", "stderr.txt", "record.json"}
            )
            for slab in SLABS:
                cell = cells / slab
                if cell.is_symlink() or not cell.is_dir() or {entry.name for entry in cell.iterdir()} != expected_files:
                    raise PathContractError(f"V2 {component} cell namespace mismatch: {bits}:{slab}")
                for filename in expected_files:
                    read_snapshot(cell / filename)
                read_snapshot(manifests / f"{slab}.json")


def _validate_operational_absence(result: Path) -> None:
    operational = result.with_name(result.name + OPERATIONAL_SUFFIX)
    journal = result.with_name(result.name + QUARANTINE_JOURNAL_SUFFIX)
    for path, context in ((operational, "operational sibling"), (journal, "quarantine journal")):
        _assert_absent_namespace(path, f"V2 {context} at release capture")


def _expected_run_config(authority: AuthoritySnapshot, result: Path) -> dict[str, Any]:
    roles = {row["role"]: row for row in authority.input_roles}
    main_hash = sha256_bytes(authority.main_raw)
    device = result.parent.stat().st_dev
    return {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "RUN_CONFIG",
        "artifact_status": "SEALED_CONTROL_PLANE_BINDING",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "dispatch_authorized_by_artifact": False,
        "matrix": matrix_payload(),
        "matrix_id": matrix_id(),
        "freeze_sha256": main_hash,
        "main_freeze_sha256": main_hash,
        "main_freeze": {"path": MAIN_FREEZE_RELATIVE.as_posix(), "sha256": main_hash},
        "machine_freeze": {
            "path": roles["machine_freeze"]["path"],
            "sha256": roles["machine_freeze"]["sha256"],
        },
        "prefreeze_review": {
            "path": roles["prefreeze_review"]["path"],
            "sha256": roles["prefreeze_review"]["sha256"],
            "verdict": "ACCEPT_FOR_FREEZE",
        },
        "input_roles": list(authority.input_roles),
        "serializers": authority.main["serializers"],
        "scheduler": authority.main["scheduler"],
        "limits": authority.main["limits"],
        "status_tables": authority.main["status_tables"],
        "evaluators": authority.main["evaluators"],
        "checkers": authority.main["checkers"],
        "archive_layout": authority.main["archive_layout"],
        "machine_requirements": authority.main["machine_requirements"],
        "execution_policy": authority.main["execution_policy"],
        "paths": {
            "authoritative_root": str(result),
            "operational_root": str(result) + OPERATIONAL_SUFFIX,
        },
        "filesystem_identity": {
            "authoritative_parent_device_id": device,
            "operational_parent_device_id": device,
            "same_filesystem": True,
        },
        "claim_boundary": RUN_CONFIG_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def _validate_run_config(authority: AuthoritySnapshot, result: Path) -> tuple[Mapping[str, Any], bytes]:
    run, raw = strict_json_image(result / "run_config.json", canonical="compact")
    exact_keys(run, RUN_CONFIG_KEYS, "V2 run config")
    expected = _expected_run_config(authority, result)
    if not exact_json_equal(run, expected):
        raise ReleaseError("V2 run config differs from role54 authority")
    return run, raw


def _validate_static_manifest(
    result: Path,
    manifest: Mapping[str, Any],
    cell: Mapping[str, Any],
    main_hash: str,
    run_hash: str,
) -> None:
    exact_keys(manifest, STATIC_CELL_MANIFEST_KEYS, "V2 static cell manifest")
    exact_int(manifest["schema_version"], "static manifest schema", expected=1)
    if (
        manifest["protocol_id"] != PROTOCOL_ID
        or manifest["artifact_role"] != "STATIC_CELL_MANIFEST"
        or manifest["authority"] != "PRODUCER_ONLY"
        or manifest["scientific_licensing_enabled"] is not False
        or manifest["matrix_id"] != matrix_id()
        or manifest["freeze_sha256"] != main_hash
        or manifest["main_freeze_sha256"] != main_hash
        or manifest["run_config_sha256"] != run_hash
        or not exact_json_equal(manifest["cell"], cell)
        or manifest["scheduler_classification"] != "COMMITTED_EVALUATOR_RESULT"
        or manifest["evaluator_status"] != "STATIC_CELL_CERTIFIED"
        or manifest["claim_boundary"] != STATIC_CELL_CLAIM_BOUNDARY
    ):
        raise ReleaseError("V2 static cell identity/binding mismatch")
    _require_null_statuses(manifest, "static cell manifest")
    require_sha256(manifest["semantic_invocation_sha256"], "static semantic invocation")
    files = exact_keys(manifest["files"], {"proof.json", "stdout.txt", "stderr.txt", "record.json"}, "static file map")
    cell_root = result / "static" / "cells" / str(cell["precision_bits"]) / cell["slab_id"]
    for filename, binding in files.items():
        exact_keys(binding, STATIC_FILE_BINDING_KEYS, f"static {filename} binding")
        if binding["path"] != filename or type(binding["truncated"]) is not bool:
            raise ReleaseError(f"V2 static {filename} path/truncation mismatch")
        expected_serializer = "CJ_COMPACT_V1" if filename in {"proof.json", "record.json"} else "RAW_BYTES"
        if binding["serializer"] != expected_serializer or binding["truncated"] is not False:
            raise ReleaseError(f"V2 static {filename} serializer mismatch")
        payload_raw, _ = read_snapshot(cell_root / filename)
        if binding["sha256"] != sha256_bytes(payload_raw):
            raise ReleaseError(f"V2 static {filename} hash mismatch")
        exact_int(binding["size_bytes"], f"static {filename} size", expected=len(payload_raw))
        if filename in {"proof.json", "record.json"}:
            payload = strict_json_loads(payload_raw, canonical="compact")
            if type(payload) is not dict:
                raise ReleaseError(f"V2 static {filename} is not an object")
            _validate_root_producer_authority(payload, f"static {filename}", STATIC_CELL_CLAIM_BOUNDARY)
    if not exact_json_equal(manifest["record"], files["record.json"]):
        raise ReleaseError("V2 static record binding is inconsistent")


def _validate_branch_manifest(
    result: Path,
    manifest: Mapping[str, Any],
    cell: Mapping[str, Any],
    main_hash: str,
    run_hash: str,
) -> None:
    exact_keys(manifest, BRANCH_CELL_MANIFEST_KEYS, "V2 branch cell manifest")
    exact_int(manifest["schema_version"], "branch manifest schema", expected=1)
    if (
        manifest["protocol_id"] != PROTOCOL_ID
        or manifest["artifact_role"] != "BRANCH_CELL_MANIFEST"
        or manifest["authority"] != "PRODUCER_ONLY"
        or manifest["scientific_licensing_enabled"] is not False
        or manifest["matrix_id"] != matrix_id()
        or manifest["freeze_sha256"] != main_hash
        or manifest["run_config_sha256"] != run_hash
        or not exact_json_equal(manifest["cell_identity"], cell)
        or not exact_json_equal(manifest["budgets"], _branch_budgets())
        or manifest["claim_boundary"] != BRANCH_CELL_CLAIM_BOUNDARY
    ):
        raise ReleaseError("V2 branch cell identity/binding mismatch")
    _require_null_statuses(manifest, "branch cell manifest")
    require_sha256(manifest["task_binding_sha256"], "branch task binding")
    cell_root_relative = PurePosixPath("branch/cells") / str(cell["precision_bits"]) / cell["slab_id"]
    expected_paths = {(cell_root_relative / name).as_posix() for name in ("stdout.txt", "stderr.txt", "record.json")}
    files = exact_keys(manifest["files"], expected_paths, "branch file map")
    for relative, digest in files.items():
        require_sha256(digest, "branch payload hash")
        raw, _ = read_snapshot(result / Path(safe_relative(relative)))
        if sha256_bytes(raw) != digest:
            raise ReleaseError("V2 branch payload hash mismatch")
        if relative.endswith("/record.json"):
            payload = strict_json_loads(raw, canonical="pretty")
            if type(payload) is not dict:
                raise ReleaseError("V2 branch record is not an object")
            _validate_root_producer_authority(payload, "branch record", BRANCH_CELL_CLAIM_BOUNDARY)


def _branch_budgets() -> dict[str, int]:
    limits = formal_limits()["branch"]
    return {
        key: limits[key]
        for key in (
            "timeout_ms", "term_grace_ms", "pipe_close_grace_ms", "stdout_bytes",
            "stderr_bytes", "record_bytes", "total_cell_bytes",
        )
    }


def _validate_component_archive(
    authority: AuthoritySnapshot,
    result: Path,
    component: str,
    run_hash: str,
) -> tuple[dict[str, Any], dict[str, bytes], Mapping[str, Any], Mapping[str, Any]]:
    if component not in {"static", "branch"}:
        raise ReleaseError("unknown V2 component")
    summary, summary_raw = strict_json_image(result / component / "aggregate_summary.json", canonical="compact")
    manifest, manifest_raw = strict_json_image(result / component / "aggregate_manifest.json", canonical="compact")
    exact_keys(summary, AGGREGATE_SUMMARY_KEYS, f"V2 {component} aggregate summary")
    exact_keys(manifest, AGGREGATE_MANIFEST_KEYS, f"V2 {component} aggregate manifest")
    prefix = component.upper()
    main_hash = sha256_bytes(authority.main_raw)
    roles = {row["role"]: row for row in authority.input_roles}
    expected_evaluator_roles = (
        {"static_evaluator": roles["static_evaluator"]}
        if component == "static"
        else {
            "branch_evaluator_source": roles["branch_evaluator_source"],
            "branch_evaluator_binary": roles["branch_evaluator_binary"],
        }
    )
    for payload, kind in ((summary, "summary"), (manifest, "manifest")):
        exact_int(payload["schema_version"], f"{component} aggregate schema", expected=1)
        if (
            payload["protocol_id"] != PROTOCOL_ID
            or payload["artifact_role"] != f"{prefix}_AGGREGATE_{kind.upper()}"
            or payload["artifact_status"] != "COMPLETE_PRODUCER_ARCHIVE"
            or payload["authority"] != "PRODUCER_ONLY"
            or payload["scientific_licensing_enabled"] is not False
            or payload["matrix_id"] != matrix_id()
            or payload["freeze_sha256"] != main_hash
            or payload["main_freeze_sha256"] != main_hash
            or payload["run_config_sha256"] != run_hash
            or not exact_json_equal(payload["evaluator_roles"], expected_evaluator_roles)
            or payload["claim_boundary"] != AGGREGATE_CLAIM_BOUNDARY
        ):
            raise ReleaseError(f"V2 {component} aggregate identity/binding mismatch")
        _require_null_statuses(payload, f"{component} aggregate {kind}")
    if not exact_json_equal(summary["matrix"], matrix_payload()):
        raise ReleaseError(f"V2 {component} aggregate matrix mismatch")
    exact_int(summary["cell_count"], f"{component} aggregate cell count", expected=102)
    certified = f"{prefix}_CELL_CERTIFIED"
    if not exact_json_equal(summary["status_counts"], {certified: 102}) or not exact_json_equal(
        summary["scheduler_classification_counts"], {"COMMITTED_EVALUATOR_RESULT": 102}
    ):
        raise ReleaseError(f"V2 {component} aggregate status counts mismatch")
    entries = manifest["cell_manifests"]
    if type(entries) is not list or len(entries) != 102:
        raise ReleaseError(f"V2 {component} aggregate must bind exactly 102 manifests")
    expected_root = sha256_bytes(canonical_json_bytes(entries))
    if summary["ordered_cell_manifest_root"] != expected_root or manifest["ordered_cell_manifest_root"] != expected_root:
        raise ReleaseError(f"V2 {component} ordered manifest root mismatch")
    summary_binding = exact_keys(manifest["summary"], {"path", "sha256", "size_bytes"}, f"{component} summary binding")
    if (
        summary_binding["path"] != f"{component}/aggregate_summary.json"
        or summary_binding["sha256"] != sha256_bytes(summary_raw)
    ):
        raise ReleaseError(f"V2 {component} aggregate summary edge mismatch")
    exact_int(summary_binding["size_bytes"], f"{component} summary size", expected=len(summary_raw))
    for index, (entry, cell) in enumerate(zip(entries, matrix_payload(), strict=True)):
        exact_keys(entry, AGGREGATE_ENTRY_KEYS, f"{component} manifest entry {index}")
        expected_path = f"{component}/cell_manifests/{cell['precision_bits']}/{cell['slab_id']}.json"
        if (
            not exact_json_equal(entry["cell"], cell)
            or entry["path"] != expected_path
            or entry["evaluator_status"] != certified
            or entry["scheduler_classification"] != "COMMITTED_EVALUATOR_RESULT"
        ):
            raise ReleaseError(f"V2 {component} manifest entry order/status mismatch")
        cell_manifest, cell_raw = strict_json_image(
            result / Path(safe_relative(expected_path)),
            canonical="compact" if component == "static" else "pretty",
        )
        if entry["sha256"] != sha256_bytes(cell_raw):
            raise ReleaseError(f"V2 {component} cell manifest hash mismatch")
        exact_int(entry["size_bytes"], f"{component} cell manifest size", expected=len(cell_raw))
        if component == "static":
            _validate_static_manifest(result, cell_manifest, cell, main_hash, run_hash)
        else:
            _validate_branch_manifest(result, cell_manifest, cell, main_hash, run_hash)
    chain = {
        "aggregate_summary_sha256": sha256_bytes(summary_raw),
        "aggregate_manifest_sha256": sha256_bytes(manifest_raw),
        "ordered_cell_manifest_root": expected_root,
    }
    return chain, {"summary": summary_raw, "manifest": manifest_raw}, summary, manifest


def _component_replay_counts(component: str) -> dict[str, int]:
    return {
        "cell_manifests": 102,
        "hash_bound_payloads": 408 if component == "static" else 306,
    }


def _component_cross_precision() -> dict[str, Any]:
    return {"slab_pairs": 51, "status_pairs_agree": 51, "passed": True}


def _component_source_bindings(
    roles: Mapping[str, Mapping[str, str]], component: str
) -> dict[str, Any]:
    checker_role = f"{component}_checker_source"
    return {
        "checker_source": {
            "path": roles[checker_role]["path"],
            "sha256": roles[checker_role]["sha256"],
        },
        "producer_source": {
            "path": roles["scheduler"]["path"],
            "sha256": roles["scheduler"]["sha256"],
        },
    }


def _validate_component_controls(
    authority: AuthoritySnapshot,
    result: Path,
    component: str,
    run_hash: str,
    chain: dict[str, Any],
    aggregate_raw: Mapping[str, bytes],
) -> dict[str, Any]:
    checker_path = result / f"independent_{component}_checker.json"
    postcheck_path = result / f"{component.upper()}_POSTCHECK_STATUS.json"
    checker, checker_raw = strict_json_image(checker_path, canonical="compact")
    postcheck, postcheck_raw = strict_json_image(postcheck_path, canonical="compact")
    exact_keys(checker, COMPONENT_CHECKER_KEYS, f"V2 {component} checker")
    exact_keys(postcheck, POSTCHECK_KEYS, f"V2 {component} postcheck")
    roles = {row["role"]: row for row in authority.input_roles}
    main_hash = sha256_bytes(authority.main_raw)
    component_status = STATIC_COMPONENT_STATUS if component == "static" else BRANCH_COMPONENT_STATUS
    checker_claim = (
        STATIC_CHECKER_CLAIM_BOUNDARY
        if component == "static"
        else BRANCH_CHECKER_CLAIM_BOUNDARY
    )
    postcheck_claim = (
        STATIC_POSTCHECK_CLAIM_BOUNDARY
        if component == "static"
        else BRANCH_POSTCHECK_CLAIM_BOUNDARY
    )
    replay_counts = _component_replay_counts(component)
    cross_precision = _component_cross_precision()
    diagnostics = {
        "ordered_cell_manifest_root": chain["ordered_cell_manifest_root"],
        "aggregate_summary_sha256": chain["aggregate_summary_sha256"],
        "aggregate_manifest_sha256": chain["aggregate_manifest_sha256"],
    }
    source_bindings = _component_source_bindings(roles, component)
    exact_int(checker["schema_version"], f"{component} checker schema", expected=1)
    if (
        checker["protocol_id"] != PROTOCOL_ID
        or checker["artifact_role"] != f"{component.upper()}_INDEPENDENT_CHECKER"
        or checker["authority"] != "INDEPENDENT_CHECKER"
        or checker["checker_status"] != CHECKER_STATUS
        or checker["component_status"] != component_status
        or checker["scientific_licensing_enabled"] is not False
        or checker["passed"] is not True
        or checker["matrix_id"] != matrix_id()
        or checker["main_freeze_sha256"] != main_hash
        or checker["run_config_sha256"] != run_hash
        or checker["component_aggregate_summary_sha256"] != chain["aggregate_summary_sha256"]
        or checker["component_aggregate_manifest_sha256"] != chain["aggregate_manifest_sha256"]
        or not exact_json_equal(checker["replay_counts"], replay_counts)
        or not exact_json_equal(checker["cross_precision"], cross_precision)
        or not exact_json_equal(checker["diagnostics"], diagnostics)
        or checker["failures"] != []
        or not exact_json_equal(checker["source_bindings"], source_bindings)
        or checker["claim_boundary"] != checker_claim
        or checker["milestone_status"] is not None
        or checker["theorem_status"] is not None
        or checker["final_status"] is not None
    ):
        raise ReleaseError(f"V2 {component} formal checker mismatch")
    for field in ("replay_counts", "cross_precision", "diagnostics", "source_bindings"):
        _reject_nested_authority(checker[field], f"{component} checker {field}")
    exact_int(postcheck["schema_version"], f"{component} postcheck schema", expected=1)
    expected_bound = {
        "aggregate_summary": {
            "path": f"{component}/aggregate_summary.json",
            "sha256": chain["aggregate_summary_sha256"],
            "size_bytes": len(aggregate_raw["summary"]),
        },
        "aggregate_manifest": {
            "path": f"{component}/aggregate_manifest.json",
            "sha256": chain["aggregate_manifest_sha256"],
            "size_bytes": len(aggregate_raw["manifest"]),
        },
        "ordered_cell_manifest_root": chain["ordered_cell_manifest_root"],
    }
    if (
        postcheck["protocol_id"] != PROTOCOL_ID
        or postcheck["artifact_role"] != f"{component.upper()}_POSTCHECK"
        or postcheck["authority"] != "POSTCHECK_ONLY"
        or postcheck["postcheck_status"] != POSTCHECK_STATUS
        or postcheck["passed"] is not True
        or postcheck["checker_path"] != f"independent_{component}_checker.json"
        or postcheck["checker_sha256"] != sha256_bytes(checker_raw)
        or postcheck["main_freeze_sha256"] != main_hash
        or postcheck["run_config_sha256"] != run_hash
        or not exact_json_equal(postcheck["bound_artifacts"], expected_bound)
        or not exact_json_equal(postcheck["replay_counts"], replay_counts)
        or postcheck["failures"] != []
        or postcheck["scientific_licensing_enabled"] is not False
        or postcheck["claim_boundary"] != postcheck_claim
        or postcheck["component_status"] != component_status
        or postcheck["milestone_status"] is not None
        or postcheck["theorem_status"] is not None
        or postcheck["final_status"] is not None
    ):
        raise ReleaseError(f"V2 {component} formal postcheck mismatch")
    for field in ("bound_artifacts", "replay_counts"):
        _reject_nested_authority(postcheck[field], f"{component} postcheck {field}")
    return {
        **chain,
        "checker_sha256": sha256_bytes(checker_raw),
        "postcheck_sha256": sha256_bytes(postcheck_raw),
    }


COMPOSITE_SUMMARY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "matrix", "cell_count_per_component", "component_chains",
    "archive_generation_sha256", "scientific_licensing_enabled", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}
COMPOSITE_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_chains", "archive_generation_sha256", "summary",
    "scientific_licensing_enabled", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
COMPOSITE_CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "static_chain", "branch_chain", "upstream_chains", "s0_compatibility",
    "replay_counts", "cross_precision", "diagnostics", "failures",
    "source_bindings", "claim_boundary", "milestone_status", "theorem_status",
    "final_status",
}


def _verbose_component_chains(component_chains: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    return {
        name: {
            "aggregate_summary": {
                "path": f"{name}/aggregate_summary.json",
                "sha256": component_chains[name]["aggregate_summary_sha256"],
            },
            "aggregate_manifest": {
                "path": f"{name}/aggregate_manifest.json",
                "sha256": component_chains[name]["aggregate_manifest_sha256"],
            },
            "checker": {
                "path": f"independent_{name}_checker.json",
                "sha256": component_chains[name]["checker_sha256"],
            },
            "postcheck": {
                "path": f"{name.upper()}_POSTCHECK_STATUS.json",
                "sha256": component_chains[name]["postcheck_sha256"],
            },
            "ordered_cell_manifest_root": component_chains[name]["ordered_cell_manifest_root"],
        }
        for name in ("static", "branch")
    }


def _validate_upstream_chains(authority: AuthoritySnapshot) -> dict[str, Any]:
    roles = {row["role"]: row for row in authority.input_roles}
    images = authority.role_images
    payloads = {
        role: strict_json_loads(images[role])
        for role in (
            "l1_summary", "l1_manifest", "l1_checker", "l1_postcheck", "l1_release",
            "a415_summary", "a415_manifest", "a415_checker", "a415_postcheck", "a415_release",
        )
    }
    if any(type(payload) is not dict for payload in payloads.values()):
        raise ReleaseError("upstream chain contains a non-object JSON role")
    l1 = {key: payloads[f"l1_{key}"] for key in ("summary", "manifest", "checker", "postcheck", "release")}
    if (
        any(payload["protocol_id"] != "R401-VAL-L1-V2" for payload in l1.values())
        or l1["checker"].get("checker_status") != "PASS"
        or l1["postcheck"].get("checker_status") != "PASS"
        or l1["release"].get("release_status") != "PASS_CONTIGUOUS_LOCAL_BRANCH"
        or any(payload.get("milestone_status") != "PASS_CONTIGUOUS_LOCAL_BRANCH" for payload in (l1["summary"], l1["manifest"], l1["checker"], l1["postcheck"]))
        or any(payload.get("final_status") is not None for payload in l1.values())
    ):
        raise ReleaseError("L1 upstream chain status mismatch")
    l1_expected = {
        "results/r401_val_l1_branch/summary.json": roles["l1_summary"]["sha256"],
        "results/r401_val_l1_branch/manifest.json": roles["l1_manifest"]["sha256"],
        "results/r401_val_l1_branch/independent_checker.json": roles["l1_checker"]["sha256"],
        "results/r401_val_l1_branch/POSTCHECK_STATUS.json": roles["l1_postcheck"]["sha256"],
    }
    if any(l1["postcheck"].get("files", {}).get(path) != digest for path, digest in list(l1_expected.items())[:3]):
        raise ReleaseError("L1 postcheck five-object edge mismatch")
    if any(l1["release"].get("files", {}).get(path) != digest for path, digest in l1_expected.items()):
        raise ReleaseError("L1 release five-object edge mismatch")
    a415 = {key: payloads[f"a415_{key}"] for key in ("summary", "manifest", "checker", "postcheck", "release")}
    if (
        any(payload["protocol_id"] != "R401-VAL-L2-A1" for payload in a415.values())
        or a415["checker"].get("checker_status") != CHECKER_STATUS
        or a415["postcheck"].get("checker_status") != CHECKER_STATUS
        or a415["release"].get("release_status") != "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
        or a415["checker"].get("milestone_status") != "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
        or a415["checker"].get("theorem_status") != "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
        or a415["postcheck"].get("milestone_status") != "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
        or a415["postcheck"].get("theorem_status") != "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
        or any(payload.get("final_status") is not None for payload in a415.values())
    ):
        raise ReleaseError("A4.15 upstream chain status mismatch")
    if a415["manifest"].get("aggregate_summary_sha256") != roles["a415_summary"]["sha256"]:
        raise ReleaseError("A4.15 manifest summary edge mismatch")
    provenance = a415["checker"].get("provenance_bindings", {})
    if (
        provenance.get("aggregate_summary_sha256") != roles["a415_summary"]["sha256"]
        or provenance.get("aggregate_manifest_sha256") != roles["a415_manifest"]["sha256"]
        or a415["postcheck"].get("checker_sha256") != roles["a415_checker"]["sha256"]
    ):
        raise ReleaseError("A4.15 checker/postcheck edge mismatch")
    a415_files = a415["release"].get("files", {})
    for role, path in (
        ("a415_summary", "results/r401_val_l2_all_slabs/aggregate_summary.json"),
        ("a415_manifest", "results/r401_val_l2_all_slabs/aggregate_manifest.json"),
        ("a415_checker", "results/r401_val_l2_all_slabs/independent_checker.json"),
        ("a415_postcheck", "results/r401_val_l2_all_slabs/POSTCHECK_STATUS.json"),
    ):
        if a415_files.get(path) != roles[role]["sha256"]:
            raise ReleaseError("A4.15 release five-object edge mismatch")
    return {
        "l1": {
            f"{name}_sha256": roles[f"l1_{name}"]["sha256"]
            for name in ("summary", "manifest", "checker", "postcheck", "release")
        },
        "a415": {
            f"{name}_sha256": roles[f"a415_{name}"]["sha256"]
            for name in ("summary", "manifest", "checker", "postcheck", "release")
        },
    }


S0_COMPATIBILITY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "replay_status", "matrix", "static_facts", "branch_facts", "composite_facts",
    "control_hashes", "role_sets", "source_protocols", "source_bindings",
    "failures", "claim_boundary", "milestone_status", "theorem_status", "final_status",
}
S0_CONTROL_ROLE_MAP = {
    "static_summary": "s0_static_summary",
    "static_manifest": "s0_static_manifest",
    "static_checker": "s0_static_checker",
    "branch_summary": "s0_branch_summary",
    "branch_manifest": "s0_branch_manifest",
    "branch_checker": "s0_branch_checker",
    "composite_summary": "s0_composite_summary",
    "composite_manifest": "s0_composite_manifest",
    "composite_checker": "s0_composite_checker",
}

S0_STATIC_FACTS = {
    "proof_count": 6, "node_count": 84172, "internal_count": 42074,
    "terminal_count": 42098, "unresolved_count": 0,
    "independent_interval_checks": 122300, "maximum_depth": 14,
}
S0_BRANCH_FACTS = {"raw_replay_count": 6, "manifest_file_count": 26}
S0_COMPOSITE_FACTS = {
    "cell_replay_count": 6, "manifest_binding_count": 18, "failure_count": 0,
}
S0_SOURCE_PROTOCOLS = {
    "static": "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT",
    "branch": "R401-VAL-L3-BT-S0",
    "composite": "R401-VAL-L3-S0-COMPOSITE-DRAFT",
}
S0_STATIC_ENTRY_KEYS = {
    "internal_count", "node_count", "path", "precision_bits", "sha256",
    "size_bytes", "slab_id", "terminal_count", "tree_content_sha256",
    "unresolved_count",
}


def _validate_s0_payload(
    project_root: Path,
    payload: Any,
    roles: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    """Replay all eighteen closed role-13 fields against the nine sealed controls."""

    exact_keys(payload, S0_COMPATIBILITY_KEYS, "V2 S0 compatibility")
    exact_int(payload["schema_version"], "V2 S0 schema", expected=1)
    expected_controls = {
        name: roles[role]["sha256"] for name, role in S0_CONTROL_ROLE_MAP.items()
    }
    expected_sources = {
        roles[role]["path"]: roles[role]["sha256"]
        for role in ("s0_adapter", "prefreeze_design", "checker_contract", "release_contract")
    }
    if (
        payload["protocol_id"] != "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY"
        or payload["artifact_role"] != "S0_TO_A1_COMPATIBILITY_REPLAY"
        or payload["artifact_status"] != "NON_LICENSING"
        or payload["replay_status"] != "PASS_S0_COMPATIBILITY_REPLAY"
        or payload["failures"] != []
        or payload["claim_boundary"] != S0_COMPATIBILITY_CLAIM_BOUNDARY
        or not exact_json_equal(payload["matrix"], {
            "precisions": [128, 256], "slabs": ["S000", "S025", "S050"],
            "cell_count": 6,
        })
        or not exact_json_equal(payload["source_protocols"], S0_SOURCE_PROTOCOLS)
        or not exact_json_equal(payload["static_facts"], S0_STATIC_FACTS)
        or not exact_json_equal(payload["branch_facts"], S0_BRANCH_FACTS)
        or not exact_json_equal(payload["composite_facts"], S0_COMPOSITE_FACTS)
        or not exact_json_equal(payload["control_hashes"], expected_controls)
        or not exact_json_equal(payload["source_bindings"], expected_sources)
    ):
        raise ReleaseError("V2 S0 exact identity/facts/bindings mismatch")
    _require_null_statuses(payload, "V2 S0 compatibility")
    for name, digest in expected_controls.items():
        require_sha256(digest, f"V2 S0 control {name}")
    for path, digest in expected_sources.items():
        safe_relative(path)
        require_sha256(digest, f"V2 S0 source {path}")

    controls: dict[str, Mapping[str, Any]] = {}
    for name, role in S0_CONTROL_ROLE_MAP.items():
        raw, _ = read_snapshot(project_file(project_root, roles[role]["path"]))
        if sha256_bytes(raw) != roles[role]["sha256"]:
            raise ReleaseError(f"V2 S0 live control changed: {name}")
        controls[name] = strict_json_loads(raw)
    static_summary = controls["static_summary"]
    static_checker = controls["static_checker"]
    branch_manifest = controls["branch_manifest"]
    branch_checker = controls["branch_checker"]
    composite_manifest = controls["composite_manifest"]
    composite_checker = controls["composite_checker"]
    if (
        static_summary.get("totals", {}).get("node_count") != 84172
        or static_summary.get("totals", {}).get("internal_count") != 42074
        or static_summary.get("totals", {}).get("terminal_count") != 42098
        or static_summary.get("totals", {}).get("unresolved_count") != 0
        or static_checker.get("independent_interval_checks") != 122300
        or branch_checker.get("raw_replay_count") != 6
        or branch_checker.get("manifest_file_count") != 26
        or composite_checker.get("cell_replay_count") != 6
        or composite_checker.get("manifest_binding_count") != 18
        or composite_checker.get("failures") != []
    ):
        raise ReleaseError("V2 S0 sealed control facts disagree with role13")

    role_sets = exact_keys(
        payload["role_sets"],
        {"static_proof_entries", "branch_manifest_roles",
         "composite_manifest_roles", "composite_component_roles"},
        "V2 S0 role sets",
    )
    proofs = static_summary.get("proofs")
    if type(proofs) is not list or len(proofs) != 6 or not exact_json_equal(
        role_sets["static_proof_entries"], proofs
    ):
        raise ReleaseError("V2 S0 six static proof roles mismatch")
    expected_pairs = tuple((precision, slab) for precision in (128, 256) for slab in ("S000", "S025", "S050"))
    for index, (entry, pair) in enumerate(zip(proofs, expected_pairs, strict=True)):
        exact_keys(entry, S0_STATIC_ENTRY_KEYS, f"V2 S0 static proof {index}")
        if (
            entry["precision_bits"] != pair[0]
            or entry["slab_id"] != pair[1]
            or entry["path"] != f"proof_{pair[0]}_{pair[1]}.json"
        ):
            raise ReleaseError("V2 S0 static proof identity/order mismatch")
        safe_relative(entry["path"])
        require_sha256(entry["sha256"], f"V2 S0 static proof {index} hash")
        exact_int(entry["size_bytes"], f"V2 S0 static proof {index} size", minimum=1)
        nodes = exact_int(entry["node_count"], f"V2 S0 static proof {index} nodes", minimum=1)
        internal = exact_int(entry["internal_count"], f"V2 S0 static proof {index} internal")
        terminal = exact_int(entry["terminal_count"], f"V2 S0 static proof {index} terminal", minimum=1)
        exact_int(entry["unresolved_count"], f"V2 S0 static proof {index} unresolved", expected=0)
        if nodes != internal + terminal:
            raise ReleaseError("V2 S0 static proof count conservation failed")
        tree_hashes = exact_keys(
            entry["tree_content_sha256"],
            {"ANGLE", "SECTION_HIGH", "SECTION_LOW", "SECTION_WINDOW"},
            f"V2 S0 static proof {index} tree hashes",
        )
        for tree, digest in tree_hashes.items():
            require_sha256(digest, f"V2 S0 proof {index} tree {tree}")

    branch_files = branch_manifest.get("files")
    if type(branch_files) is not dict:
        raise ReleaseError("V2 S0 branch manifest files is not an object")
    prefix = f"{project_root}/"
    branch_roles: list[str] = []
    for absolute in branch_files:
        if type(absolute) is not str or not absolute.startswith(prefix):
            raise ReleaseError("V2 S0 branch manifest path escapes authority root")
        relative = absolute[len(prefix):]
        safe_relative(relative)
        branch_roles.append(relative)
    if not exact_json_equal(role_sets["branch_manifest_roles"], branch_roles):
        raise ReleaseError("V2 S0 ordered branch manifest roles mismatch")

    composite_files = composite_manifest.get("files")
    component_files = composite_manifest.get("component_files")
    if type(composite_files) is not list or type(component_files) is not list:
        raise ReleaseError("V2 S0 composite manifest role arrays missing")
    expected_composite = [
        {"scope": row.get("scope"), "path": row.get("path")} for row in composite_files
    ]
    expected_components = [
        {"component": row.get("component"), "path": row.get("path")}
        for row in component_files
    ]
    if (
        not exact_json_equal(role_sets["composite_manifest_roles"], expected_composite)
        or not exact_json_equal(role_sets["composite_component_roles"], expected_components)
    ):
        raise ReleaseError("V2 S0 composite role sets mismatch")
    for row in expected_composite:
        exact_keys(row, {"scope", "path"}, "V2 S0 composite manifest role")
        if row["scope"] not in ("ROOT", "OUTPUT"):
            raise ReleaseError("V2 S0 composite role scope mismatch")
        safe_relative(row["path"])
    for row in expected_components:
        exact_keys(row, {"component", "path"}, "V2 S0 component role")
        if row["component"] not in ("static", "branch"):
            raise ReleaseError("V2 S0 component role identity mismatch")
        safe_relative(row["path"])
    return {"replay_sha256": roles["s0_compatibility"]["sha256"], "control_hashes": expected_controls}


def _validate_s0_compatibility(authority: AuthoritySnapshot) -> dict[str, Any]:
    roles = {row["role"]: row for row in authority.input_roles}
    payload = strict_json_loads(authority.role_images["s0_compatibility"], canonical="compact")
    return _validate_s0_payload(authority.project_root, payload, roles)


def _composite_source_bindings(roles: Mapping[str, Mapping[str, str]]) -> dict[str, Any]:
    return {
        name: {"path": roles[role]["path"], "sha256": roles[role]["sha256"]}
        for name, role in (
            ("checker_source", "composite_checker_source"),
            ("checker_contract", "checker_contract"),
            ("release_contract", "release_contract"),
        )
    }


def _validate_composite_chain(
    authority: AuthoritySnapshot,
    result: Path,
    run_hash: str,
    component_chains: Mapping[str, Mapping[str, Any]],
    upstream_chains: Mapping[str, Any],
    s0_compatibility: Mapping[str, Any],
) -> dict[str, Any]:
    summary, summary_raw = strict_json_image(result / "composite_summary.json", canonical="compact")
    manifest, manifest_raw = strict_json_image(result / "composite_manifest.json", canonical="compact")
    checker, checker_raw = strict_json_image(result / "independent_checker.json", canonical="compact")
    postcheck, postcheck_raw = strict_json_image(result / "POSTCHECK_STATUS.json", canonical="compact")
    exact_keys(summary, COMPOSITE_SUMMARY_KEYS, "V2 composite summary")
    exact_keys(manifest, COMPOSITE_MANIFEST_KEYS, "V2 composite manifest")
    exact_keys(checker, COMPOSITE_CHECKER_KEYS, "V2 composite checker")
    exact_keys(postcheck, POSTCHECK_KEYS, "V2 composite postcheck")
    verbose = _verbose_component_chains(component_chains)
    generation = sha256_bytes(canonical_json_bytes(verbose))
    main_hash = sha256_bytes(authority.main_raw)
    for payload, role in ((summary, "SUMMARY"), (manifest, "MANIFEST")):
        exact_int(payload["schema_version"], "composite producer schema", expected=1)
        if (
            payload["protocol_id"] != PROTOCOL_ID
            or payload["artifact_role"] != f"COMPOSITE_{role}"
            or payload["artifact_status"] != "COMPLETE_PRODUCER_ARCHIVE"
            or payload["authority"] != "PRODUCER_ONLY"
            or payload["scientific_licensing_enabled"] is not False
            or payload["matrix_id"] != matrix_id()
            or payload["main_freeze_sha256"] != main_hash
            or payload["run_config_sha256"] != run_hash
            or not exact_json_equal(payload["component_chains"], verbose)
            or payload["archive_generation_sha256"] != generation
            or payload["claim_boundary"] != RELEASE_CLAIM_BOUNDARY
        ):
            raise ReleaseError("V2 composite producer identity/binding mismatch")
        _require_null_statuses(payload, "composite producer")
        _reject_nested_authority(payload["component_chains"], "composite producer chains")
    if not exact_json_equal(summary["matrix"], matrix_payload()):
        raise ReleaseError("V2 composite matrix mismatch")
    exact_int(summary["cell_count_per_component"], "composite cell count", expected=102)
    summary_binding = exact_keys(manifest["summary"], {"path", "sha256", "size_bytes"}, "composite summary binding")
    if (
        summary_binding["path"] != "composite_summary.json"
        or summary_binding["sha256"] != sha256_bytes(summary_raw)
    ):
        raise ReleaseError("V2 composite summary edge mismatch")
    exact_int(summary_binding["size_bytes"], "composite summary size", expected=len(summary_raw))
    roles = {row["role"]: row for row in authority.input_roles}
    replay_counts = {
        "static_cells": 102,
        "branch_cells": 102,
        "component_chains": 2,
        "upstream_objects": 10,
        "s0_controls": 9,
    }
    cross_precision = {
        "checked_slabs": 51,
        "matching_component_verdicts": 51,
        "passed": True,
    }
    diagnostics = {
        "archive_generation_sha256": generation,
        "composite_summary_sha256": sha256_bytes(summary_raw),
        "composite_manifest_sha256": sha256_bytes(manifest_raw),
    }
    sources = _composite_source_bindings(roles)
    exact_int(checker["schema_version"], "composite checker schema", expected=1)
    if (
        checker["protocol_id"] != PROTOCOL_ID
        or checker["artifact_role"] != "COMPOSITE_INDEPENDENT_CHECKER"
        or checker["authority"] != "INDEPENDENT_CHECKER"
        or checker["checker_status"] != CHECKER_STATUS
        or checker["component_status"] is not None
        or checker["scientific_licensing_enabled"] is not True
        or checker["passed"] is not True
        or checker["matrix_id"] != matrix_id()
        or checker["main_freeze_sha256"] != main_hash
        or checker["run_config_sha256"] != run_hash
        or not exact_json_equal(checker["static_chain"], verbose["static"])
        or not exact_json_equal(checker["branch_chain"], verbose["branch"])
        or not exact_json_equal(checker["upstream_chains"], upstream_chains)
        or not exact_json_equal(checker["s0_compatibility"], s0_compatibility)
        or not exact_json_equal(checker["replay_counts"], replay_counts)
        or not exact_json_equal(checker["cross_precision"], cross_precision)
        or not exact_json_equal(checker["diagnostics"], diagnostics)
        or checker["failures"] != []
        or not exact_json_equal(checker["source_bindings"], sources)
        or checker["claim_boundary"] != RELEASE_CLAIM_BOUNDARY
        or checker["milestone_status"] != COMPOSITE_STATUS
        or checker["theorem_status"] != COMPOSITE_STATUS
        or checker["final_status"] is not None
    ):
        raise ReleaseError("V2 formal composite checker mismatch")
    for field in (
        "static_chain", "branch_chain", "upstream_chains", "s0_compatibility",
        "replay_counts", "cross_precision", "diagnostics", "source_bindings",
    ):
        _reject_nested_authority(checker[field], f"composite checker {field}")
    expected_bound = {
        "composite_summary": {
            "path": "composite_summary.json",
            "sha256": sha256_bytes(summary_raw),
            "size_bytes": len(summary_raw),
        },
        "composite_manifest": {
            "path": "composite_manifest.json",
            "sha256": sha256_bytes(manifest_raw),
            "size_bytes": len(manifest_raw),
        },
        "archive_generation_sha256": generation,
    }
    exact_int(postcheck["schema_version"], "composite postcheck schema", expected=1)
    if (
        postcheck["protocol_id"] != PROTOCOL_ID
        or postcheck["artifact_role"] != "COMPOSITE_POSTCHECK"
        or postcheck["authority"] != "POSTCHECK_ONLY"
        or postcheck["postcheck_status"] != POSTCHECK_STATUS
        or postcheck["passed"] is not True
        or postcheck["checker_path"] != "independent_checker.json"
        or postcheck["checker_sha256"] != sha256_bytes(checker_raw)
        or postcheck["main_freeze_sha256"] != main_hash
        or postcheck["run_config_sha256"] != run_hash
        or not exact_json_equal(postcheck["bound_artifacts"], expected_bound)
        or not exact_json_equal(postcheck["replay_counts"], replay_counts)
        or postcheck["failures"] != []
        or postcheck["scientific_licensing_enabled"] is not True
        or postcheck["claim_boundary"] != COMPOSITE_POSTCHECK_CLAIM_BOUNDARY
        or postcheck["component_status"] is not None
        or postcheck["milestone_status"] != COMPOSITE_STATUS
        or postcheck["theorem_status"] != COMPOSITE_STATUS
        or postcheck["final_status"] is not None
    ):
        raise ReleaseError("V2 formal composite postcheck mismatch")
    for field in ("bound_artifacts", "replay_counts"):
        _reject_nested_authority(postcheck[field], f"composite postcheck {field}")
    return {
        "summary_sha256": sha256_bytes(summary_raw),
        "manifest_sha256": sha256_bytes(manifest_raw),
        "checker_sha256": sha256_bytes(checker_raw),
        "postcheck_sha256": sha256_bytes(postcheck_raw),
        "archive_generation_sha256": generation,
    }


def _validate_report_raw(raw: bytes) -> bytes:
    if type(raw) is not bytes:
        raise ReleaseError("V2 report image must be bytes")
    try:
        text = raw.decode("ascii")
    except UnicodeError as error:
        raise ReleaseError("V2 production report authority must be ASCII") from error
    if "&" in text or re.search(r"(?i)(?<![A-Za-z0-9_])Verdict(?![A-Za-z0-9_])", text):
        raise ReleaseError("V2 report contains entity/verdict authority syntax")
    if raw == REPORT_EXACT_RAW:
        return raw
    declaration = re.compile(
        r"(?i)(?<![A-Za-z0-9_])(?:"
        r"status|authority|verdict|promotion[\s_-]*authorized|"
        r"production[\s_-]*authorized|scientific[\s_-]*licensing(?:[\s_-]*enabled)?|"
        r"scientific[\s_-]*dispatch(?:[\s_-]*performed)?|"
        r"dispatch[\s_-]*authorized(?:[\s_-]*by[\s_-]*artifact)?|"
        r"component[\s_-]*status|milestone[\s_-]*status|"
        r"theorem[\s_-]*status|final[\s_-]*status|"
        r"claim[\s_-]*boundary"
        r")(?![A-Za-z0-9_])\s*(?:=|:|->)"
    )
    if any(declaration.search(line) is not None for line in text.splitlines()):
        raise ReleaseError(
            "V2 report contains conflicting/decorated authority declarations"
        )
    raise ReleaseError("V2 report is not the exact five-line LF-terminated image")


def _validate_report(path: Path) -> bytes:
    raw, _ = read_snapshot(path, maximum_bytes=4096)
    return _validate_report_raw(raw)


def _validate_control_chain(
    authority: AuthoritySnapshot,
    *,
    transient: PublicationTransient | None = None,
    require_report: bool = True,
    permit_release: bool = True,
) -> dict[str, Any]:
    result = project_file(authority.project_root, RESULT_RELATIVE)
    release = result / RELEASE_NAME
    allow_release = permit_release and release.exists() and not release.is_symlink()
    _validate_result_namespace(
        result,
        allow_release=allow_release,
        require_report=require_report,
        transient=transient,
    )
    _validate_operational_absence(result)
    _run, run_raw = _validate_run_config(authority, result)
    run_hash = sha256_bytes(run_raw)
    component_chains: dict[str, Any] = {}
    for component in ("static", "branch"):
        chain, aggregate_raw, _summary, _manifest = _validate_component_archive(
            authority, result, component, run_hash
        )
        component_chains[component] = _validate_component_controls(
            authority, result, component, run_hash, chain, aggregate_raw
        )
    upstream_chains = _validate_upstream_chains(authority)
    s0_compatibility = _validate_s0_compatibility(authority)
    composite_chain = _validate_composite_chain(
        authority, result, run_hash, component_chains, upstream_chains, s0_compatibility
    )
    if require_report:
        _validate_report(result / REPORT_NAME)
    return {
        "run_config_sha256": run_hash,
        "component_chains": component_chains,
        "composite_chain": composite_chain,
        "upstream_chains": upstream_chains,
        "s0_compatibility": s0_compatibility,
    }


def _role_binding(project_root: Path, role: str, relative: str) -> dict[str, str]:
    raw, _ = read_snapshot(project_file(project_root, relative))
    if relative.endswith(".json"):
        strict_json_loads(raw)
    return {"role": role, "path": relative, "sha256": sha256_bytes(raw)}


def _build_expected_report_state(
    project_root: Path,
    *,
    report_published: bool,
    permit_release: bool = False,
    transient: PublicationTransient | None = None,
) -> dict[str, Any]:
    """Replay roles 54--67 and derive the one fixed role-68 byte image."""

    root = lexical_absolute(project_root)
    if type(report_published) is not bool:
        raise ReleaseError("report publication state must be an exact boolean")
    if type(permit_release) is not bool:
        raise ReleaseError("report release-permission state must be an exact boolean")
    if permit_release and not report_published:
        raise ReleaseError("only a canonical report replay may permit a release image")
    if report_published and transient is not None:
        raise ReleaseError("published report and publication transient cannot coexist")
    authority = validate_formal_main_freeze(root)
    chain = _validate_control_chain(
        authority,
        transient=transient,
        require_report=report_published,
        permit_release=permit_release,
    )
    if (
        len(REPORT_UPSTREAM_ROLES) != 14
        or len({role for role, _path in REPORT_UPSTREAM_ROLES}) != 14
        or len({path for _role, path in REPORT_UPSTREAM_ROLES}) != 14
    ):
        raise ReleaseError("production-report upstream role map is not exact14")
    rows = [
        _role_binding(root, role, relative)
        for role, relative in REPORT_UPSTREAM_ROLES
    ]
    if [(row["role"], row["path"]) for row in rows] != list(
        REPORT_UPSTREAM_ROLES
    ):
        raise ReleaseError("production-report ordered upstream role map changed")
    generation = chain["composite_chain"]["archive_generation_sha256"]
    require_sha256(generation, "production-report archive generation digest")
    _validate_report_raw(REPORT_EXACT_RAW)
    return {
        "raw": REPORT_EXACT_RAW,
        "upstream_roles": rows,
        "ordered_upstream_roles_sha256": sha256_bytes(
            canonical_json_bytes(rows)
        ),
        "archive_generation_sha256": generation,
    }


def _validate_historical_release_for_report(project_root: Path) -> None:
    """If role 68 has already fed a release, replay that release exactly.

    A canonical report remains independently verifiable after the later release
    publication.  Private report candidates never get this historical allowance.
    """

    root = lexical_absolute(project_root)
    destination = project_file(root, f"{RESULT_RELATIVE}/{RELEASE_NAME}")
    try:
        info = os.stat(destination, follow_symlinks=False)
    except FileNotFoundError:
        return
    if not stat.S_ISREG(info.st_mode):
        raise PathContractError("historical release destination is not a regular file")
    expected = _build_expected_release(root)
    stored, raw = strict_json_image(destination, canonical="compact")
    if raw != canonical_json_bytes(expected) or not exact_json_equal(stored, expected):
        raise ReleaseError("historical release does not bind the exact 68-role DAG")


def build_expected_report(project_root: Path) -> bytes:
    with capture_input_generation():
        state = _build_expected_report_state(
            lexical_absolute(project_root), report_published=False
        )
        _terminal_replay_generation()
    return state["raw"]


def report_path(project_root: Path) -> Path:
    return project_file(lexical_absolute(project_root), REPORT_RELATIVE)


def _build_expected_release(
    project_root: Path,
    *,
    transient: PublicationTransient | None = None,
) -> dict[str, Any]:
    authority = validate_formal_main_freeze(project_root)
    chain = _validate_control_chain(authority, transient=transient)
    main_role = {
        "role": "main_freeze",
        "path": MAIN_FREEZE_RELATIVE.as_posix(),
        "sha256": sha256_bytes(authority.main_raw),
    }
    downstream = [
        _role_binding(authority.project_root, role, relative)
        for role, relative in DOWNSTREAM_ROLES
    ]
    roles = [*authority.input_roles, main_role, *downstream]
    if (
        len(roles) != 68
        or len({row["role"] for row in roles}) != 68
        or len({row["path"] for row in roles}) != 68
    ):
        raise ReleaseError("V2 release role map is not exactly 68 unique roles/paths")
    machine_hash = next(
        row["sha256"] for row in authority.input_roles if row["role"] == "machine_freeze"
    )
    payload = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "release_contract": RELEASE_CONTRACT,
        "release_status": RELEASE_STATUS,
        "authority": "RELEASE_BINDING_ONLY",
        "scientific_licensing_enabled": True,
        "matrix_id": matrix_id(),
        "main_freeze_sha256": main_role["sha256"],
        "machine_freeze_sha256": machine_hash,
        "run_config_sha256": chain["run_config_sha256"],
        "archive_generation_sha256": chain["composite_chain"]["archive_generation_sha256"],
        "ordered_static_manifest_root": chain["component_chains"]["static"]["ordered_cell_manifest_root"],
        "ordered_branch_manifest_root": chain["component_chains"]["branch"]["ordered_cell_manifest_root"],
        "roles": roles,
        "component_chains": chain["component_chains"],
        "composite_chain": chain["composite_chain"],
        "upstream_chains": chain["upstream_chains"],
        "s0_compatibility": chain["s0_compatibility"],
        "claim_boundary": RELEASE_CLAIM_BOUNDARY,
        "milestone_status": COMPOSITE_STATUS,
        "theorem_status": COMPOSITE_STATUS,
        "final_status": None,
    }
    exact_keys(payload, RELEASE_KEYS, "V2 release envelope")
    return payload


def build_expected_release(project_root: Path) -> dict[str, Any]:
    with capture_input_generation():
        return _build_expected_release(lexical_absolute(project_root))


def release_path(project_root: Path) -> Path:
    return project_file(lexical_absolute(project_root), f"{RESULT_RELATIVE}/{RELEASE_NAME}")


def _rename_noreplace(parent_fd: int, source_name: str, destination_name: str) -> None:
    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = getattr(libc, "renameat2", None)
    if renameat2 is None:
        raise PathContractError("Linux renameat2(RENAME_NOREPLACE) is unavailable")
    renameat2.argtypes = [
        ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    if renameat2(parent_fd, os.fsencode(source_name), parent_fd, os.fsencode(destination_name), 1) == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in (errno.EEXIST, errno.ENOTEMPTY):
        raise FileExistsError(error_number, os.strerror(error_number), destination_name)
    raise PathContractError(f"renameat2(RENAME_NOREPLACE) failed: errno={error_number}")


def _write_all(descriptor: int, raw: bytes) -> None:
    view = memoryview(raw)
    while view:
        count = os.write(descriptor, view)
        if count <= 0:
            raise OSError("short release staging write")
        view = view[count:]


def _read_fd_all(descriptor: int, maximum_bytes: int, context: str) -> tuple[bytes, os.stat_result]:
    before = os.fstat(descriptor)
    if not stat.S_ISREG(before.st_mode) or before.st_size < 0 or before.st_size > maximum_bytes:
        raise PathContractError(f"{context}: regular bounded inode required")
    chunks: list[bytes] = []
    offset = 0
    while True:
        chunk = os.pread(descriptor, 1024 * 1024, offset)
        if not chunk:
            break
        chunks.append(chunk)
        offset += len(chunk)
        if offset > maximum_bytes:
            raise PathContractError(f"{context}: bounded read exceeded")
    after = os.fstat(descriptor)
    raw = b"".join(chunks)
    if _fingerprint(before) != _fingerprint(after) or len(raw) != before.st_size:
        raise PathContractError(f"{context}: inode changed or short read")
    return raw, after


def _destination_absent(parent_fd: int, name: str, context: str) -> None:
    try:
        os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    raise FileExistsError(errno.EEXIST, f"{context} already exists", name)


def write_once(
    path: Path,
    raw: bytes,
    *,
    revalidate: Callable[[PublicationTransient | None], bytes] | None = None,
    fault_hook: Callable[[str], None] | None = None,
) -> PublicationOutcome:
    """Commit bytes through one same-parent Linux RENAME_NOREPLACE edge."""

    canonical = lexical_absolute(path)
    parent = canonical.parent
    _reject_symlink_components(parent)
    parent_namespace = _namespace_signature(parent)
    parent_before = os.stat(parent, follow_symlinks=False)
    if not stat.S_ISDIR(parent_before.st_mode):
        raise PathContractError("publication parent is not a directory")
    parent_fd = os.open(
        parent,
        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0),
    )
    stage_fd: int | None = None
    stage_name: str | None = None
    stage_identity: tuple[int, int] | None = None
    renamed = False
    primary_error: BaseException | None = None
    cleanup_error: BaseException | None = None
    outcome: PublicationOutcome | None = None

    def phase(name: str) -> None:
        if fault_hook is not None:
            fault_hook(name)

    def transient() -> PublicationTransient:
        if stage_name is None or stage_identity is None:
            raise PathContractError("publication transient is not initialized")
        return PublicationTransient(
            parent=parent,
            name=stage_name,
            device_id=stage_identity[0],
            inode=stage_identity[1],
            mode=0o644,
            nlink=1,
            raw=raw,
        )

    def replay_stage(context: str) -> None:
        if stage_name is None or stage_identity is None:
            raise PathContractError("publication stage is not initialized")
        replay_descriptor = os.open(
            stage_name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        try:
            replay_raw, replay_info = _read_fd_all(
                replay_descriptor, len(raw), context
            )
        finally:
            os.close(replay_descriptor)
        if (
            replay_raw != raw
            or (replay_info.st_dev, replay_info.st_ino) != stage_identity
            or not stat.S_ISREG(replay_info.st_mode)
            or stat.S_IMODE(replay_info.st_mode) != 0o644
            or replay_info.st_nlink != 1
        ):
            raise PathContractError(f"{context}: byte/inode contract mismatch")

    try:
        parent_opened = os.fstat(parent_fd)
        if (
            (parent_opened.st_dev, parent_opened.st_ino, parent_opened.st_mode)
            != (parent_before.st_dev, parent_before.st_ino, parent_before.st_mode)
        ):
            raise PathContractError("publication parent open race")
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ReleaseError("publication parent is locked by another writer") from error
        _destination_absent(parent_fd, canonical.name, "publication destination")
        for _attempt in range(32):
            candidate = f".{canonical.name}.publish-{secrets.token_hex(16)}"
            try:
                opened_fd = os.open(
                    candidate,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
                    0o600,
                    dir_fd=parent_fd,
                )
            except FileExistsError:
                continue
            stage_fd = opened_fd
            stage_name = candidate
            # Record invocation ownership immediately after the successful open.
            opened_info = os.fstat(opened_fd)
            stage_identity = (opened_info.st_dev, opened_info.st_ino)
            if (
                not stat.S_ISREG(opened_info.st_mode)
                or opened_info.st_nlink != 1
                or opened_info.st_size != 0
                or stat.S_IMODE(opened_info.st_mode) != 0o600
            ):
                raise PathContractError("new publication stage inode is not private/empty")
            break
        if stage_fd is None or stage_name is None or stage_identity is None:
            raise PathContractError("publication staging namespace exhausted")
        _write_all(stage_fd, raw)
        phase("AFTER_STAGE_WRITE")
        os.fchmod(stage_fd, 0o644)
        os.fsync(stage_fd)
        phase("AFTER_STAGE_FILE_FSYNC")
        stage_info = os.fstat(stage_fd)
        if (
            (stage_info.st_dev, stage_info.st_ino) != stage_identity
            or not stat.S_ISREG(stage_info.st_mode)
            or stage_info.st_nlink != 1
            or stat.S_IMODE(stage_info.st_mode) != 0o644
            or stage_info.st_size != len(raw)
        ):
            raise PathContractError("publication stage inode contract mismatch")
        replay_stage("publication stage replay")
        os.fsync(parent_fd)
        phase("AFTER_STAGING_PARENT_FSYNC")

        # The entire semantic/live envelope is reconstructed in the final
        # pre-rename window; active snapshots are then force-replayed.
        if revalidate is not None and revalidate(transient()) != raw:
            raise ReleaseError("publication terminal validation changed candidate bytes")
        _terminal_replay_generation()
        phase("AFTER_TERMINAL_REPLAY")
        if _namespace_signature(parent) != parent_namespace:
            raise PathContractError("publication parent lexical namespace changed")
        parent_terminal = os.fstat(parent_fd)
        if (
            parent_terminal.st_dev, parent_terminal.st_ino, parent_terminal.st_mode
        ) != (
            parent_before.st_dev, parent_before.st_ino, parent_before.st_mode
        ):
            raise PathContractError("publication parent inode changed")
        replay_stage("terminal publication stage")
        _destination_absent(parent_fd, canonical.name, "publication destination")
        phase("BEFORE_RENAME")
        # A fault hook, signal handler, or concurrent actor may have changed an
        # input after the first terminal pass.  Rebuild the complete envelope
        # once more in the instruction window immediately preceding rename.
        if revalidate is not None and revalidate(transient()) != raw:
            raise ReleaseError("publication immediate-prerename envelope changed")
        _terminal_replay_generation()
        replay_stage("immediate-prerename publication stage")
        lexical_parent = os.stat(parent, follow_symlinks=False)
        if (
            _namespace_signature(parent) != parent_namespace
            or (
                lexical_parent.st_dev,
                lexical_parent.st_ino,
                lexical_parent.st_mode,
            )
            != (
                parent_before.st_dev,
                parent_before.st_ino,
                parent_before.st_mode,
            )
        ):
            raise PathContractError("publication parent changed immediately before rename")
        _destination_absent(parent_fd, canonical.name, "publication destination")
        _rename_noreplace(parent_fd, stage_name, canonical.name)
        renamed = True
        phase("AFTER_RENAME")

        published_fd = os.open(
            canonical.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        try:
            published, published_info = _read_fd_all(
                published_fd, len(raw), "published authority inode"
            )
            if (
                published != raw
                or (published_info.st_dev, published_info.st_ino) != stage_identity
                or published_info.st_nlink != 1
                or stat.S_IMODE(published_info.st_mode) != 0o644
            ):
                raise PathContractError("published authority inode/byte mismatch")
            lexical_info = os.stat(canonical, follow_symlinks=False)
            if _fingerprint(lexical_info) != _fingerprint(published_info):
                raise PathContractError("published lexical path/inode mismatch")
            os.fsync(published_fd)
        finally:
            os.close(published_fd)
        phase("AFTER_DESTINATION_FSYNC")
        os.fsync(parent_fd)
        phase("AFTER_PUBLICATION_PARENT_FSYNC")
        if _namespace_signature(parent) != parent_namespace:
            raise PathContractError("publication parent namespace changed after rename")
        final_fd = os.open(
            canonical.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        try:
            final_raw, final_info = _read_fd_all(final_fd, len(raw), "postpublication replay")
        finally:
            os.close(final_fd)
        if (
            final_raw != raw
            or (final_info.st_dev, final_info.st_ino) != stage_identity
            or final_info.st_nlink != 1
            or stat.S_IMODE(final_info.st_mode) != 0o644
        ):
            raise PathContractError("postpublication replay mismatch")
        phase("AFTER_POSTPUBLICATION_REPLAY")
        if revalidate is not None and revalidate(None) != raw:
            raise ReleaseError("postpublication authority envelope changed")
        _terminal_replay_generation()
        ultimate_fd = os.open(
            canonical.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        try:
            ultimate_raw, ultimate_info = _read_fd_all(
                ultimate_fd, len(raw), "ultimate post-hook publication replay"
            )
        finally:
            os.close(ultimate_fd)
        ultimate_lexical = os.stat(canonical, follow_symlinks=False)
        if (
            ultimate_raw != raw
            or (ultimate_info.st_dev, ultimate_info.st_ino) != stage_identity
            or _fingerprint(ultimate_lexical) != _fingerprint(ultimate_info)
            or ultimate_info.st_nlink != 1
            or stat.S_IMODE(ultimate_info.st_mode) != 0o644
            or _namespace_signature(parent) != parent_namespace
        ):
            raise PathContractError("ultimate post-hook authority replay mismatch")
        outcome = PublicationOutcome(
            canonical_path=canonical,
            canonical_sha256=sha256_bytes(ultimate_raw),
            size_bytes=len(ultimate_raw),
            fingerprint=_fingerprint(ultimate_info),
            publication_method=PUBLICATION_METHOD,
        )
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
        # No destination operation of any kind occurs after the rename edge.
        if not renamed and stage_name is not None and stage_identity is not None:
            try:
                current = os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
                if (current.st_dev, current.st_ino) == stage_identity:
                    os.unlink(stage_name, dir_fd=parent_fd)
                    os.fsync(parent_fd)
                else:
                    raise PathContractError(
                        "publication stage name was replaced by a foreign inode"
                    )
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
    if outcome is None:
        raise PathContractError("publication completed without a terminal outcome")
    return outcome


def _owned_tmp_candidate_parent(path: Path, *, before_write: bool) -> tuple[int, int, int, int]:
    candidate = lexical_absolute(path)
    if candidate.parent.parent != Path("/tmp") or len(candidate.parts) != 4:
        raise PathContractError("candidate must be exact /tmp/<owned-dir>/<leaf>")
    parent = candidate.parent
    _reject_symlink_components(parent)
    info = os.stat(parent, follow_symlinks=False)
    if (
        not stat.S_ISDIR(info.st_mode)
        or info.st_uid != os.geteuid()
        or stat.S_IMODE(info.st_mode) != 0o700
        or info.st_nlink != 2
    ):
        raise PathContractError("candidate parent must be euid-owned 0700 nlink2")
    entries = tuple(sorted(entry.name for entry in os.scandir(parent)))
    expected = () if before_write else (candidate.name,)
    if entries != expected:
        raise PathContractError("candidate parent is not the required empty/singleton namespace")
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink)


def _read_candidate_policy(
    path: Path,
    *,
    canonical: Path,
    temporary_mode: int,
    maximum_bytes: int,
) -> tuple[Mapping[str, Any], bytes, bool]:
    candidate = lexical_absolute(path)
    is_canonical = candidate == lexical_absolute(canonical)
    parent_identity: tuple[int, int, int, int] | None = None
    if not is_canonical:
        parent_identity = _owned_tmp_candidate_parent(candidate, before_write=False)
    raw, info = read_snapshot(candidate, maximum_bytes=maximum_bytes)
    expected_mode = 0o644 if is_canonical else temporary_mode
    if stat.S_IMODE(info.st_mode) != expected_mode or info.st_nlink != 1:
        raise PathContractError("candidate mode/link contract mismatch")
    if parent_identity is not None:
        replay = os.stat(candidate.parent, follow_symlinks=False)
        if (
            replay.st_dev, replay.st_ino, replay.st_mode, replay.st_nlink
        ) != parent_identity:
            raise PathContractError("candidate parent identity changed")
        if _owned_tmp_candidate_parent(candidate, before_write=False) != parent_identity:
            raise PathContractError("private candidate lexical parent changed")
    payload = strict_json_loads(raw, canonical="compact")
    if type(payload) is not dict:
        raise StrictJSONError("candidate JSON root is not an object")
    return payload, raw, is_canonical


def _read_report_candidate_policy(
    path: Path, *, canonical: Path
) -> tuple[bytes, os.stat_result, bool]:
    candidate = lexical_absolute(path)
    fixed = lexical_absolute(canonical)
    if candidate.name != REPORT_NAME:
        raise PathContractError(
            f"production-report candidate leaf must equal {REPORT_NAME}"
        )
    is_canonical = candidate == fixed
    parent_identity: tuple[int, int, int, int] | None = None
    if not is_canonical:
        parent_identity = _owned_tmp_candidate_parent(
            candidate, before_write=False
        )
    raw, info = read_snapshot(candidate, maximum_bytes=4096)
    expected_mode = 0o644 if is_canonical else 0o600
    if (
        stat.S_IMODE(info.st_mode) != expected_mode
        or info.st_nlink != 1
        or len(raw) > 4096
    ):
        raise PathContractError("production-report candidate mode/link/cap mismatch")
    _validate_report_raw(raw)
    if parent_identity is not None:
        replay = os.stat(candidate.parent, follow_symlinks=False)
        if (
            replay.st_dev,
            replay.st_ino,
            replay.st_mode,
            replay.st_nlink,
        ) != parent_identity:
            raise PathContractError("production-report candidate parent changed")
        if (
            _owned_tmp_candidate_parent(candidate, before_write=False)
            != parent_identity
        ):
            raise PathContractError(
                "production-report private lexical parent changed"
            )
    return raw, info, is_canonical


def _validate_main_checker_receipts(
    receipts: Mapping[str, Mapping[str, Any]],
    *,
    candidate_raw: bytes,
    input_roles: Sequence[Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Validate the three non-authoritative role-20--22 receipts.

    The receipts are only evidence that the three independent programs saw
    this exact candidate/input map.  Their PASS tokens never replace role
    24's own complete semantic reconstruction.
    """

    outer = exact_keys(
        receipts, set(MAIN_CHECKER_RECEIPT_ROLES),
        "role54 checker receipt map",
    )
    candidate_sha256 = sha256_bytes(candidate_raw)
    input_map_sha256 = sha256_bytes(canonical_json_bytes(list(input_roles)))
    validated: dict[str, dict[str, Any]] = {}
    for role in MAIN_CHECKER_RECEIPT_ROLES:
        receipt = exact_keys(
            outer[role], MAIN_CHECKER_RECEIPT_KEYS,
            f"role54 {role} checker receipt",
        )
        if (
            receipt["verification_status"] != "PASS_MAIN_FREEZE_VERIFY_ONLY"
            or receipt["authority"] != "NON_AUTHORITATIVE_VERIFY_ONLY"
            or receipt["candidate_sha256"] != candidate_sha256
            or receipt["input_map_sha256"] != input_map_sha256
            or receipt["promotion_authorized"] is not False
            or receipt["artifacts_written"] is not False
        ):
            raise ReleaseError(f"role54 {role} checker receipt binding mismatch")
        require_sha256(receipt["candidate_sha256"], f"role54 {role} candidate digest")
        require_sha256(receipt["input_map_sha256"], f"role54 {role} input-map digest")
        exact_int(
            receipt["size_bytes"], f"role54 {role} candidate size",
            expected=len(candidate_raw),
        )
        # Make a plain immutable-by-convention copy; subsequent caller-side
        # mutation is detected by the terminal replay below.
        validated[role] = dict(receipt)
    return validated


def _read_main_checker_receipt_path(path: Path) -> MainCheckerReceiptSnapshot:
    candidate = lexical_absolute(path)
    parent_identity = _owned_tmp_candidate_parent(candidate, before_write=False)
    raw, info = read_snapshot(candidate, maximum_bytes=1024 * 1024)
    if stat.S_IMODE(info.st_mode) != 0o600 or info.st_nlink != 1:
        raise PathContractError("main checker receipt must be private 0600 nlink1")
    payload = strict_json_loads(raw, canonical="compact")
    exact_keys(payload, MAIN_CHECKER_RECEIPT_KEYS, "main checker receipt")
    namespace = _namespace_signature(candidate)
    replay_parent = _owned_tmp_candidate_parent(candidate, before_write=False)
    if replay_parent != parent_identity or _namespace_signature(candidate) != namespace:
        raise PathContractError("main checker receipt parent changed")
    return MainCheckerReceiptSnapshot(
        path=candidate,
        raw=raw,
        fingerprint=_fingerprint(info),
        parent_identity=parent_identity,
        namespace=namespace,
        payload=payload,
    )


def _replay_main_checker_receipt(snapshot: MainCheckerReceiptSnapshot) -> None:
    if (
        _namespace_signature(snapshot.path) != snapshot.namespace
        or _owned_tmp_candidate_parent(snapshot.path, before_write=False)
        != snapshot.parent_identity
    ):
        raise PathContractError("main checker receipt parent/namespace changed")
    raw, info = read_snapshot(snapshot.path, maximum_bytes=1024 * 1024)
    if raw != snapshot.raw or _fingerprint(info) != snapshot.fingerprint:
        raise PathContractError("main checker receipt byte/inode generation changed")
    if stat.S_IMODE(info.st_mode) != 0o600 or info.st_nlink != 1:
        raise PathContractError("main checker receipt mode/link changed")
    if (
        _namespace_signature(snapshot.path) != snapshot.namespace
        or _owned_tmp_candidate_parent(snapshot.path, before_write=False)
        != snapshot.parent_identity
    ):
        raise PathContractError("main checker receipt lexical parent changed")


def _read_main_checker_receipt_set(
    paths: Mapping[str, Path],
) -> tuple[dict[str, Mapping[str, Any]], dict[str, MainCheckerReceiptSnapshot]]:
    rows = exact_keys(
        paths, set(MAIN_CHECKER_RECEIPT_ROLES),
        "role54 checker receipt path map",
    )
    snapshots = {
        role: _read_main_checker_receipt_path(rows[role])
        for role in MAIN_CHECKER_RECEIPT_ROLES
    }
    if len({snapshot.path for snapshot in snapshots.values()}) != 3:
        raise PathContractError("role54 checker receipt paths must be distinct")
    if len({snapshot.fingerprint[:2] for snapshot in snapshots.values()}) != 3:
        raise PathContractError("role54 checker receipt inodes must be distinct")
    return (
        {role: snapshots[role].payload for role in MAIN_CHECKER_RECEIPT_ROLES},
        snapshots,
    )


def _write_private_candidate(
    path: Path,
    raw: bytes,
    *,
    mode: int = 0o600,
    revalidate: Callable[[], bytes] | None = None,
    fault_hook: Callable[[str], None] | None = None,
) -> None:
    candidate = lexical_absolute(path)
    parent_identity = _owned_tmp_candidate_parent(candidate, before_write=True)
    parent_fd = os.open(
        candidate.parent,
        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0),
    )
    descriptor: int | None = None
    identity: tuple[int, int] | None = None
    primary: BaseException | None = None
    cleanup: BaseException | None = None

    def phase(name: str) -> None:
        if fault_hook is not None:
            fault_hook(name)

    def replay_candidate(context: str) -> None:
        if identity is None:
            raise PathContractError("private candidate identity is unavailable")
        replay_descriptor = os.open(
            candidate.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        try:
            replay_raw, replay_info = _read_fd_all(
                replay_descriptor, len(raw), context
            )
        finally:
            os.close(replay_descriptor)
        if (
            replay_raw != raw
            or (replay_info.st_dev, replay_info.st_ino) != identity
            or not stat.S_ISREG(replay_info.st_mode)
            or stat.S_IMODE(replay_info.st_mode) != mode
            or replay_info.st_nlink != 1
        ):
            raise PathContractError(f"{context}: byte/inode contract mismatch")
    try:
        parent_info = os.fstat(parent_fd)
        if (
            parent_info.st_dev, parent_info.st_ino, parent_info.st_mode, parent_info.st_nlink
        ) != parent_identity:
            raise PathContractError("candidate parent open race")
        descriptor = os.open(
            candidate.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o600,
            dir_fd=parent_fd,
        )
        opened = os.fstat(descriptor)
        identity = (opened.st_dev, opened.st_ino)
        if (
            not stat.S_ISREG(opened.st_mode) or opened.st_nlink != 1
            or opened.st_size != 0 or stat.S_IMODE(opened.st_mode) != 0o600
        ):
            raise PathContractError("new candidate inode is not private/empty")
        _write_all(descriptor, raw)
        os.fchmod(descriptor, mode)
        os.fsync(descriptor)
        written = os.fstat(descriptor)
        if (
            (written.st_dev, written.st_ino) != identity
            or written.st_nlink != 1 or written.st_size != len(raw)
            or stat.S_IMODE(written.st_mode) != mode
        ):
            raise PathContractError("candidate inode changed during write")
        os.fsync(parent_fd)
        replay_candidate("candidate replay")
        if _owned_tmp_candidate_parent(candidate, before_write=False) != parent_identity:
            raise PathContractError("private candidate lexical parent changed")
        phase("AFTER_CANDIDATE_WRITE")
        if revalidate is not None and revalidate() != raw:
            raise ReleaseError("private candidate authority envelope changed")
        _terminal_replay_generation()
        phase("AFTER_CANDIDATE_TERMINAL_REPLAY")
        # The hook above is deliberately followed by a second full rebuild;
        # success therefore cannot be returned after a late same-byte inode or
        # authority-input substitution.
        if revalidate is not None and revalidate() != raw:
            raise ReleaseError("private candidate final authority envelope changed")
        _terminal_replay_generation()
        replay_candidate("final private candidate replay")
        final_parent = os.fstat(parent_fd)
        if (
            final_parent.st_dev, final_parent.st_ino,
            final_parent.st_mode, final_parent.st_nlink,
        ) != parent_identity:
            raise PathContractError("private candidate parent changed")
        if _owned_tmp_candidate_parent(candidate, before_write=False) != parent_identity:
            raise PathContractError("private candidate lexical parent changed")
    except BaseException as error:
        primary = error
    finally:
        if identity is None and descriptor is not None:
            try:
                info = os.fstat(descriptor)
                identity = (info.st_dev, info.st_ino)
            except BaseException as error:
                cleanup = cleanup or error
        if descriptor is not None:
            try:
                os.close(descriptor)
            except BaseException as error:
                cleanup = cleanup or error
        if primary is not None and identity is not None:
            try:
                current = os.stat(candidate.name, dir_fd=parent_fd, follow_symlinks=False)
                if (current.st_dev, current.st_ino) != identity:
                    raise PathContractError("candidate name replaced by foreign inode")
                os.unlink(candidate.name, dir_fd=parent_fd)
                os.fsync(parent_fd)
            except FileNotFoundError:
                pass
            except BaseException as error:
                cleanup = cleanup or error
        try:
            os.close(parent_fd)
        except BaseException as error:
            cleanup = cleanup or error
    if cleanup is not None:
        if primary is not None:
            raise cleanup from primary
        raise cleanup
    if primary is not None:
        raise primary


def _publication_fingerprint_payload(
    fingerprint: tuple[int, ...], context: str
) -> dict[str, int]:
    if len(fingerprint) != 7 or any(type(value) is not int for value in fingerprint):
        raise PathContractError(f"{context} fingerprint shape is invalid")
    device_id, inode, mode, nlink, size_bytes, mtime_ns, ctime_ns = fingerprint
    if (
        device_id < 0 or inode <= 0 or size_bytes < 0
        or mtime_ns < 0 or ctime_ns < 0 or nlink != 1
        or not stat.S_ISREG(mode)
    ):
        raise PathContractError(f"{context} fingerprint values are invalid")
    return {
        "device_id": device_id,
        "inode": inode,
        "size_bytes": size_bytes,
        "mtime_ns": mtime_ns,
        "ctime_ns": ctime_ns,
        "mode": mode,
        "nlink": nlink,
    }


def _publication_file_binding(
    path: Path,
    raw: bytes,
    fingerprint: tuple[int, ...],
    *,
    expected_mode: int,
    context: str,
) -> dict[str, Any]:
    canonical = lexical_absolute(path)
    nested = _publication_fingerprint_payload(fingerprint, context)
    if (
        nested["size_bytes"] != len(raw)
        or stat.S_IMODE(nested["mode"]) != expected_mode
        or nested["nlink"] != 1
    ):
        raise PathContractError(f"{context} binding/fingerprint mismatch")
    binding = {
        "path": str(canonical),
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "mode": f"{expected_mode:04o}",
        "nlink": 1,
        "fingerprint": nested,
    }
    exact_keys(binding, PUBLICATION_FILE_BINDING_KEYS, context)
    exact_keys(nested, PUBLICATION_FINGERPRINT_KEYS, f"{context} fingerprint")
    return binding


def _publication_receipt_common(
    *,
    artifact_role: str,
    authority: str,
    claim_boundary: str,
    candidate: Mapping[str, Any],
    canonical: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": artifact_role,
        "artifact_status": "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY",
        "authority": authority,
        "candidate": dict(candidate),
        "canonical": dict(canonical),
        "publication_method": PUBLICATION_METHOD,
        "independent_postpublication_verification_performed": False,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "claim_boundary": claim_boundary,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def _validate_publication_receipt_common(
    receipt: Any,
    *,
    expected_keys: set[str],
    artifact_role: str,
    authority: str,
    claim_boundary: str,
) -> Mapping[str, Any]:
    value = exact_keys(receipt, expected_keys, "publication receipt")
    exact_int(value["schema_version"], "publication receipt schema", expected=1)
    if (
        value["protocol_id"] != PROTOCOL_ID
        or value["artifact_role"] != artifact_role
        or value["artifact_status"]
        != "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY"
        or value["authority"] != authority
        or value["publication_method"] != PUBLICATION_METHOD
        or value["claim_boundary"] != claim_boundary
        or value["independent_postpublication_verification_performed"] is not False
        or value["scientific_licensing_enabled"] is not False
        or value["production_authorized"] is not False
        or value["scientific_dispatch_performed"] is not False
    ):
        raise ReleaseError("publication receipt identity/authority mismatch")
    _require_null_statuses(value, "publication receipt")
    bindings: dict[str, Mapping[str, Any]] = {}
    for name, mode in (("candidate", "0600"), ("canonical", "0644")):
        binding = exact_keys(
            value[name], PUBLICATION_FILE_BINDING_KEYS,
            f"publication receipt {name}",
        )
        if type(binding["path"]) is not str:
            raise PathContractError(f"publication receipt {name} path is invalid")
        lexical_absolute(binding["path"])
        require_sha256(binding["sha256"], f"publication receipt {name} digest")
        exact_int(binding["size_bytes"], f"publication receipt {name} size")
        exact_int(binding["nlink"], f"publication receipt {name} nlink", expected=1)
        if binding["mode"] != mode:
            raise PathContractError(f"publication receipt {name} mode mismatch")
        fingerprint = exact_keys(
            binding["fingerprint"], PUBLICATION_FINGERPRINT_KEYS,
            f"publication receipt {name} fingerprint",
        )
        for field in (
            "device_id", "size_bytes", "mtime_ns", "ctime_ns", "mode",
        ):
            exact_int(
                fingerprint[field],
                f"publication receipt {name} fingerprint {field}",
            )
        exact_int(
            fingerprint["inode"],
            f"publication receipt {name} fingerprint inode", minimum=1,
        )
        exact_int(
            fingerprint["nlink"],
            f"publication receipt {name} fingerprint nlink", expected=1,
        )
        if (
            fingerprint["size_bytes"] != binding["size_bytes"]
            or not stat.S_ISREG(fingerprint["mode"])
            or stat.S_IMODE(fingerprint["mode"]) != int(mode, 8)
        ):
            raise PathContractError(
                f"publication receipt {name} fingerprint cross-binding mismatch"
            )
        bindings[name] = binding
    if (
        bindings["candidate"]["path"] == bindings["canonical"]["path"]
        or bindings["candidate"]["sha256"] != bindings["canonical"]["sha256"]
        or bindings["candidate"]["size_bytes"] != bindings["canonical"]["size_bytes"]
    ):
        raise ReleaseError("publication receipt candidate/canonical edge mismatch")
    return value


def _validate_main_publication_receipt(receipt: Any) -> Mapping[str, Any]:
    value = _validate_publication_receipt_common(
        receipt,
        expected_keys=MAIN_PUBLICATION_RECEIPT_KEYS,
        artifact_role="MAIN_FREEZE_PUBLICATION_RECEIPT",
        authority=EXPECTED_MAIN_PUBLICATION_AUTHORITY,
        claim_boundary=MAIN_PUBLICATION_CLAIM_BOUNDARY,
    )
    exact_int(
        value["input_role_count"], "role54 publication input-role count",
        expected=53,
    )
    require_sha256(
        value["ordered_input_roles_sha256"],
        "role54 publication ordered input-role digest",
    )
    checker_hashes = exact_keys(
        value["checker_receipt_sha256"], set(MAIN_CHECKER_RECEIPT_ROLES),
        "role54 checker receipt digest map",
    )
    for role in MAIN_CHECKER_RECEIPT_ROLES:
        require_sha256(checker_hashes[role], f"role54 {role} receipt raw digest")
    return value


def _validate_report_verify_receipt(
    receipt: Any,
    *,
    candidate_raw: bytes,
    ordered_upstream_roles_sha256: str,
) -> Mapping[str, Any]:
    value = exact_keys(
        receipt, REPORT_VERIFY_RECEIPT_KEYS,
        "production-report verify receipt",
    )
    if (
        value["verification_status"]
        != "PASS_PRODUCTION_REPORT_VERIFY_ONLY"
        or value["authority"] != "NON_AUTHORITATIVE_VERIFY_ONLY"
        or value["candidate_sha256"] != sha256_bytes(candidate_raw)
        or value["ordered_upstream_roles_sha256"]
        != ordered_upstream_roles_sha256
        or value["promotion_authorized"] is not False
        or value["artifacts_written"] is not False
    ):
        raise ReleaseError("production-report verify receipt binding mismatch")
    require_sha256(
        value["candidate_sha256"],
        "production-report verify candidate digest",
    )
    require_sha256(
        value["ordered_upstream_roles_sha256"],
        "production-report verify ordered-upstream digest",
    )
    exact_int(
        value["size_bytes"], "production-report verify size",
        expected=len(candidate_raw),
    )
    return value


def _validate_report_publication_receipt(
    receipt: Any,
    *,
    expected_ordered_upstream_roles_sha256: str,
    expected_archive_generation_sha256: str,
) -> Mapping[str, Any]:
    require_sha256(
        expected_ordered_upstream_roles_sha256,
        "expected production-report ordered-upstream digest",
    )
    require_sha256(
        expected_archive_generation_sha256,
        "expected production-report archive-generation digest",
    )
    value = _validate_publication_receipt_common(
        receipt,
        expected_keys=REPORT_PUBLICATION_RECEIPT_KEYS,
        artifact_role="PRODUCTION_REPORT_PUBLICATION_RECEIPT",
        authority=EXPECTED_REPORT_PUBLICATION_AUTHORITY,
        claim_boundary=REPORT_PUBLICATION_CLAIM_BOUNDARY,
    )
    exact_int(
        value["upstream_role_count"],
        "production-report publication upstream-role count",
        expected=14,
    )
    for name in (
        "ordered_upstream_roles_sha256", "archive_generation_sha256",
    ):
        require_sha256(value[name], f"production-report publication {name}")
    if (
        value["ordered_upstream_roles_sha256"]
        != expected_ordered_upstream_roles_sha256
        or value["archive_generation_sha256"]
        != expected_archive_generation_sha256
    ):
        raise ReleaseError(
            "production-report publication upstream/archive binding mismatch"
        )
    return value


def _validate_release_publication_receipt(receipt: Any) -> Mapping[str, Any]:
    value = _validate_publication_receipt_common(
        receipt,
        expected_keys=RELEASE_PUBLICATION_RECEIPT_KEYS,
        artifact_role="RELEASE_PROVENANCE_PUBLICATION_RECEIPT",
        authority=EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
        claim_boundary=RELEASE_PUBLICATION_CLAIM_BOUNDARY,
    )
    exact_int(value["role_count"], "release publication role count", expected=68)
    for name in (
        "ordered_roles_sha256", "main_freeze_sha256",
        "archive_generation_sha256",
    ):
        require_sha256(value[name], f"release publication {name}")
    return value


def build_main_freeze_candidate(
    project_root: Path,
    candidate_path: Path,
    *,
    fault_hook: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    with capture_input_generation():
        payload = _build_expected_main_freeze(root)
        raw = canonical_json_bytes(payload)
        if len(raw) > 1024 * 1024:
            raise ReleaseError("role54 candidate exceeds the 1048576-byte contract")
        _terminal_replay_generation()

        def terminal() -> bytes:
            return canonical_json_bytes(_build_expected_main_freeze(root))

        _write_private_candidate(
            candidate_path, raw, mode=0o600,
            revalidate=terminal, fault_hook=fault_hook,
        )
    return payload


def verify_main_freeze_candidate(project_root: Path, candidate_path: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    with capture_input_generation():
        payload, raw, _ = _read_candidate_policy(
            candidate_path, canonical=project_file(root, MAIN_FREEZE_RELATIVE),
            temporary_mode=0o600, maximum_bytes=1024 * 1024,
        )
        records, images = _capture_input_roles(root)
        _validate_main(root, payload, records, images)
        expected = _build_expected_main_freeze(root)
        if raw != canonical_json_bytes(expected) or not exact_json_equal(payload, expected):
            raise ReleaseError("role54 candidate differs from exact independently rebuilt bytes")
    return dict(payload)


def publish_main_freeze(
    project_root: Path,
    candidate_path: Path,
    *,
    checker_receipts: Mapping[str, Mapping[str, Any]],
    expected_candidate_sha256: str,
    publication_authority: str,
    fault_hook: Callable[[str], None] | None = None,
    _checker_receipt_snapshots: Mapping[str, MainCheckerReceiptSnapshot] | None = None,
) -> dict[str, Any]:
    if publication_authority != EXPECTED_MAIN_PUBLICATION_AUTHORITY:
        raise ReleaseError("role54 canonical publication is not authorized by the current lock")
    require_sha256(expected_candidate_sha256, "role54 expected candidate digest")
    root = lexical_absolute(project_root)
    candidate = lexical_absolute(candidate_path)
    destination = project_file(root, MAIN_FREEZE_RELATIVE)
    with capture_input_generation():
        payload, raw, _ = _read_candidate_policy(
            candidate, canonical=destination, temporary_mode=0o600,
            maximum_bytes=1024 * 1024,
        )
        candidate_replay_raw, candidate_info = read_snapshot(
            candidate, maximum_bytes=1024 * 1024
        )
        if candidate_replay_raw != raw:
            raise PathContractError("role54 candidate changed after policy read")
        candidate_fingerprint = _fingerprint(candidate_info)
        if candidate == destination:
            raise PathContractError("role54 publisher requires a separate private candidate")
        if sha256_bytes(raw) != expected_candidate_sha256:
            raise ReleaseError("role54 explicit expected digest mismatch")
        expected = _build_expected_main_freeze(root)
        if raw != canonical_json_bytes(expected) or not exact_json_equal(payload, expected):
            raise ReleaseError("role54 candidate differs from rebuilt authority envelope")

        validated_receipts = _validate_main_checker_receipts(
            checker_receipts,
            candidate_raw=raw,
            input_roles=expected["input_roles"],
        )
        frozen_receipt_raw = {
            role: canonical_json_bytes(validated_receipts[role])
            for role in MAIN_CHECKER_RECEIPT_ROLES
        }
        snapshots: Mapping[str, MainCheckerReceiptSnapshot] | None = None
        if _checker_receipt_snapshots is not None:
            snapshots = exact_keys(
                _checker_receipt_snapshots, set(MAIN_CHECKER_RECEIPT_ROLES),
                "role54 checker receipt snapshots",
            )
            if len({snapshots[role].path for role in MAIN_CHECKER_RECEIPT_ROLES}) != 3:
                raise PathContractError("role54 checker receipt paths must be distinct")
            if len({snapshots[role].fingerprint[:2] for role in MAIN_CHECKER_RECEIPT_ROLES}) != 3:
                raise PathContractError("role54 checker receipt inodes must be distinct")
            for role in MAIN_CHECKER_RECEIPT_ROLES:
                if (
                    snapshots[role].raw != frozen_receipt_raw[role]
                    or not exact_json_equal(snapshots[role].payload, validated_receipts[role])
                ):
                    raise ReleaseError(f"role54 {role} receipt path/payload mismatch")

        def replay_receipts(input_roles: Sequence[Mapping[str, Any]]) -> None:
            current = _validate_main_checker_receipts(
                checker_receipts,
                candidate_raw=raw,
                input_roles=input_roles,
            )
            for role in MAIN_CHECKER_RECEIPT_ROLES:
                if canonical_json_bytes(current[role]) != frozen_receipt_raw[role]:
                    raise ReleaseError(f"role54 {role} receipt mapping changed")
                if snapshots is not None:
                    _replay_main_checker_receipt(snapshots[role])
                    if snapshots[role].raw != frozen_receipt_raw[role]:
                        raise ReleaseError(f"role54 {role} receipt image changed")

        replay_receipts(expected["input_roles"])

        def terminal(_transient: PublicationTransient | None) -> bytes:
            replay_receipts(expected["input_roles"])
            terminal_payload, terminal_raw, _ = _read_candidate_policy(
                candidate, canonical=destination, temporary_mode=0o600,
                maximum_bytes=1024 * 1024,
            )
            rebuilt = _build_expected_main_freeze(root)
            if (
                terminal_raw != canonical_json_bytes(rebuilt)
                or not exact_json_equal(terminal_payload, rebuilt)
                or sha256_bytes(terminal_raw) != expected_candidate_sha256
            ):
                raise ReleaseError("role54 terminal candidate/envelope mismatch")
            replay_receipts(rebuilt["input_roles"])
            return terminal_raw

        outcome = write_once(
            destination, raw, revalidate=terminal, fault_hook=fault_hook
        )
        stored, stored_raw = strict_json_image(destination, canonical="compact")
        if stored_raw != raw or not exact_json_equal(stored, expected):
            raise ReleaseError("published role54 failed exact postpublication verification")
        terminal_candidate_raw, terminal_candidate_info = read_snapshot(
            candidate, maximum_bytes=1024 * 1024
        )
        terminal_canonical_raw, terminal_canonical_info = read_snapshot(
            destination, maximum_bytes=1024 * 1024
        )
        if (
            terminal_candidate_raw != raw
            or _fingerprint(terminal_candidate_info) != candidate_fingerprint
            or terminal_canonical_raw != raw
            or _fingerprint(terminal_canonical_info) != outcome.fingerprint
            or outcome.canonical_path != destination
            or outcome.canonical_sha256 != expected_candidate_sha256
            or outcome.size_bytes != len(raw)
            or outcome.publication_method != PUBLICATION_METHOD
        ):
            raise PathContractError("role54 terminal publication outcome mismatch")
        candidate_binding = _publication_file_binding(
            candidate, raw, candidate_fingerprint,
            expected_mode=0o600, context="role54 publication candidate",
        )
        canonical_binding = _publication_file_binding(
            destination, raw, outcome.fingerprint,
            expected_mode=0o644, context="role54 publication canonical",
        )
        receipt = _publication_receipt_common(
            artifact_role="MAIN_FREEZE_PUBLICATION_RECEIPT",
            authority=EXPECTED_MAIN_PUBLICATION_AUTHORITY,
            claim_boundary=MAIN_PUBLICATION_CLAIM_BOUNDARY,
            candidate=candidate_binding,
            canonical=canonical_binding,
        )
        input_roles = expected["input_roles"]
        if type(input_roles) is not list:
            raise ReleaseError("role54 publication input-role array is invalid")
        exact_int(
            len(input_roles), "role54 publication input-role count", expected=53
        )
        receipt.update({
            "input_role_count": 53,
            "ordered_input_roles_sha256": sha256_bytes(
                canonical_json_bytes(input_roles)
            ),
            "checker_receipt_sha256": {
                role: sha256_bytes(frozen_receipt_raw[role])
                for role in MAIN_CHECKER_RECEIPT_ROLES
            },
        })
        exact_keys(receipt, MAIN_PUBLICATION_RECEIPT_KEYS, "role54 publication receipt")
        exact_keys(
            receipt["checker_receipt_sha256"],
            set(MAIN_CHECKER_RECEIPT_ROLES),
            "role54 checker receipt digest map",
        )
        for role in MAIN_CHECKER_RECEIPT_ROLES:
            require_sha256(
                receipt["checker_receipt_sha256"][role],
                f"role54 {role} receipt raw digest",
            )
        _validate_main_publication_receipt(receipt)
        canonical_json_bytes(receipt)
    return receipt


def _report_private_candidate_path(path: Path, *, before_write: bool) -> Path:
    candidate = lexical_absolute(path)
    if candidate.name != REPORT_NAME:
        raise PathContractError(
            f"production-report private leaf must equal {REPORT_NAME}"
        )
    _owned_tmp_candidate_parent(candidate, before_write=before_write)
    return candidate


def build_report_candidate(
    project_root: Path,
    candidate_path: Path,
    *,
    fault_hook: Callable[[str], None] | None = None,
) -> bytes:
    root = lexical_absolute(project_root)
    candidate = _report_private_candidate_path(candidate_path, before_write=True)
    with capture_input_generation():
        state = _build_expected_report_state(root, report_published=False)
        raw = state["raw"]
        if len(raw) > 4096:
            raise ReleaseError("production-report candidate exceeds 4096 bytes")
        _terminal_replay_generation()

        def terminal() -> bytes:
            return _build_expected_report_state(
                root, report_published=False
            )["raw"]

        _write_private_candidate(
            candidate, raw, mode=0o600,
            revalidate=terminal, fault_hook=fault_hook,
        )
    return raw


def verify_report_candidate(
    project_root: Path, candidate_path: Path
) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    candidate = lexical_absolute(candidate_path)
    destination = report_path(root)
    with capture_input_generation():
        raw, info, is_canonical = _read_report_candidate_policy(
            candidate, canonical=destination
        )
        fingerprint = _fingerprint(info)
        state = _build_expected_report_state(
            root,
            report_published=is_canonical,
            permit_release=is_canonical,
        )
        if is_canonical:
            _validate_historical_release_for_report(root)
        if raw != state["raw"]:
            raise ReleaseError("production-report candidate differs from exact bytes")
        terminal_state = _build_expected_report_state(
            root,
            report_published=is_canonical,
            permit_release=is_canonical,
        )
        if is_canonical:
            _validate_historical_release_for_report(root)
        terminal_raw, terminal_info, terminal_is_canonical = (
            _read_report_candidate_policy(candidate, canonical=destination)
        )
        if (
            terminal_state != state
            or terminal_raw != raw
            or _fingerprint(terminal_info) != fingerprint
            or terminal_is_canonical is not is_canonical
        ):
            raise PathContractError(
                "production-report candidate/upstream generation changed"
            )
        receipt = {
            "verification_status": "PASS_PRODUCTION_REPORT_VERIFY_ONLY",
            "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
            "candidate_sha256": sha256_bytes(raw),
            "ordered_upstream_roles_sha256": state[
                "ordered_upstream_roles_sha256"
            ],
            "size_bytes": len(raw),
            "promotion_authorized": False,
            "artifacts_written": False,
        }
        _validate_report_verify_receipt(
            receipt,
            candidate_raw=raw,
            ordered_upstream_roles_sha256=state[
                "ordered_upstream_roles_sha256"
            ],
        )
        _terminal_replay_generation()
    return receipt


def publish_report(
    project_root: Path,
    candidate_path: Path,
    *,
    expected_candidate_sha256: str,
    publication_authority: str,
    fault_hook: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    if publication_authority != EXPECTED_REPORT_PUBLICATION_AUTHORITY:
        raise ReleaseError(
            "production-report canonical publication is not authorized by the current lock"
        )
    require_sha256(
        expected_candidate_sha256,
        "production-report expected candidate digest",
    )
    root = lexical_absolute(project_root)
    candidate = _report_private_candidate_path(candidate_path, before_write=False)
    destination = report_path(root)
    with capture_input_generation():
        try:
            os.stat(destination, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise FileExistsError(
                errno.EEXIST,
                "production-report canonical destination already exists",
                destination.name,
            )
        raw, candidate_info, is_canonical = _read_report_candidate_policy(
            candidate, canonical=destination
        )
        if is_canonical or candidate == destination:
            raise PathContractError(
                "production-report publisher requires a separate private candidate"
            )
        candidate_fingerprint = _fingerprint(candidate_info)
        state = _build_expected_report_state(root, report_published=False)
        if (
            raw != state["raw"]
            or sha256_bytes(raw) != expected_candidate_sha256
        ):
            raise ReleaseError(
                "production-report explicit digest/upstream envelope mismatch"
            )

        def terminal(publication_transient: PublicationTransient | None) -> bytes:
            terminal_raw, terminal_info, terminal_is_canonical = (
                _read_report_candidate_policy(candidate, canonical=destination)
            )
            rebuilt = _build_expected_report_state(
                root,
                report_published=publication_transient is None,
                transient=publication_transient,
            )
            if (
                terminal_is_canonical
                or terminal_raw != rebuilt["raw"]
                or sha256_bytes(terminal_raw) != expected_candidate_sha256
                or _fingerprint(terminal_info) != candidate_fingerprint
            ):
                raise ReleaseError(
                    "production-report terminal candidate/upstream mismatch"
                )
            return terminal_raw

        outcome = write_once(
            destination, raw, revalidate=terminal, fault_hook=fault_hook
        )
        stored_raw = _validate_report(destination)
        published_state = _build_expected_report_state(
            root, report_published=True
        )
        if stored_raw != raw or published_state != state:
            raise ReleaseError(
                "published production report failed exact postpublication verification"
            )
        terminal_candidate_raw, terminal_candidate_info, terminal_is_canonical = (
            _read_report_candidate_policy(candidate, canonical=destination)
        )
        terminal_canonical_raw, terminal_canonical_info, canonical_flag = (
            _read_report_candidate_policy(destination, canonical=destination)
        )
        if (
            terminal_is_canonical
            or canonical_flag is not True
            or terminal_candidate_raw != raw
            or _fingerprint(terminal_candidate_info) != candidate_fingerprint
            or terminal_canonical_raw != raw
            or _fingerprint(terminal_canonical_info) != outcome.fingerprint
            or outcome.canonical_path != destination
            or outcome.canonical_sha256 != expected_candidate_sha256
            or outcome.size_bytes != len(raw)
            or outcome.publication_method != PUBLICATION_METHOD
        ):
            raise PathContractError(
                "production-report terminal publication outcome mismatch"
            )
        candidate_binding = _publication_file_binding(
            candidate, raw, candidate_fingerprint,
            expected_mode=0o600,
            context="production-report publication candidate",
        )
        canonical_binding = _publication_file_binding(
            destination, raw, outcome.fingerprint,
            expected_mode=0o644,
            context="production-report publication canonical",
        )
        receipt = _publication_receipt_common(
            artifact_role="PRODUCTION_REPORT_PUBLICATION_RECEIPT",
            authority=EXPECTED_REPORT_PUBLICATION_AUTHORITY,
            claim_boundary=REPORT_PUBLICATION_CLAIM_BOUNDARY,
            candidate=candidate_binding,
            canonical=canonical_binding,
        )
        receipt.update({
            "upstream_role_count": 14,
            "ordered_upstream_roles_sha256": state[
                "ordered_upstream_roles_sha256"
            ],
            "archive_generation_sha256": state[
                "archive_generation_sha256"
            ],
        })
        exact_keys(
            receipt, REPORT_PUBLICATION_RECEIPT_KEYS,
            "production-report publication receipt",
        )
        _validate_report_publication_receipt(
            receipt,
            expected_ordered_upstream_roles_sha256=state[
                "ordered_upstream_roles_sha256"
            ],
            expected_archive_generation_sha256=state[
                "archive_generation_sha256"
            ],
        )
        canonical_json_bytes(receipt)
    return receipt


def build_release(
    project_root: Path,
    candidate_path: Path,
    *,
    fault_hook: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    with capture_input_generation():
        payload = _build_expected_release(root)
        raw = canonical_json_bytes(payload)
        _terminal_replay_generation()

        def terminal() -> bytes:
            return canonical_json_bytes(_build_expected_release(root))

        _write_private_candidate(
            candidate_path, raw, mode=0o600,
            revalidate=terminal, fault_hook=fault_hook,
        )
    return payload


def verify_release_candidate(project_root: Path, candidate_path: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    with capture_input_generation():
        payload, raw, _ = _read_candidate_policy(
            candidate_path, canonical=release_path(root), temporary_mode=0o600,
            maximum_bytes=16 * 1024 * 1024,
        )
        expected = _build_expected_release(root)
        if raw != canonical_json_bytes(expected) or not exact_json_equal(payload, expected):
            raise ReleaseError("V2 release candidate bytes or 68-role DAG mismatch")
    return dict(payload)


def publish_release(
    project_root: Path,
    candidate_path: Path,
    *,
    expected_candidate_sha256: str,
    publication_authority: str,
    fault_hook: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    if publication_authority != EXPECTED_RELEASE_PUBLICATION_AUTHORITY:
        raise ReleaseError("release canonical publication is not authorized by the current lock")
    require_sha256(expected_candidate_sha256, "release expected candidate digest")
    root = lexical_absolute(project_root)
    candidate = lexical_absolute(candidate_path)
    destination = release_path(root)
    with capture_input_generation():
        payload, raw, _ = _read_candidate_policy(
            candidate, canonical=destination, temporary_mode=0o600,
            maximum_bytes=16 * 1024 * 1024,
        )
        candidate_replay_raw, candidate_info = read_snapshot(
            candidate, maximum_bytes=16 * 1024 * 1024
        )
        if candidate_replay_raw != raw:
            raise PathContractError("release candidate changed after policy read")
        candidate_fingerprint = _fingerprint(candidate_info)
        if candidate == destination:
            raise PathContractError("release publisher requires a separate private candidate")
        expected = _build_expected_release(root)
        if (
            sha256_bytes(raw) != expected_candidate_sha256
            or raw != canonical_json_bytes(expected)
            or not exact_json_equal(payload, expected)
        ):
            raise ReleaseError("release explicit digest/68-role envelope mismatch")

        def terminal(publication_transient: PublicationTransient | None) -> bytes:
            terminal_payload, terminal_raw, _ = _read_candidate_policy(
                candidate, canonical=destination, temporary_mode=0o600,
                maximum_bytes=16 * 1024 * 1024,
            )
            rebuilt = _build_expected_release(
                root, transient=publication_transient
            )
            if (
                terminal_raw != canonical_json_bytes(rebuilt)
                or not exact_json_equal(terminal_payload, rebuilt)
                or sha256_bytes(terminal_raw) != expected_candidate_sha256
            ):
                raise ReleaseError("release terminal candidate/envelope mismatch")
            return terminal_raw

        outcome = write_once(
            destination, raw, revalidate=terminal, fault_hook=fault_hook
        )
        stored, stored_raw = strict_json_image(destination, canonical="compact")
        if stored_raw != raw or not exact_json_equal(stored, expected):
            raise ReleaseError("published V2 release failed exact verification")
        terminal_candidate_raw, terminal_candidate_info = read_snapshot(
            candidate, maximum_bytes=16 * 1024 * 1024
        )
        terminal_canonical_raw, terminal_canonical_info = read_snapshot(
            destination, maximum_bytes=16 * 1024 * 1024
        )
        if (
            terminal_candidate_raw != raw
            or _fingerprint(terminal_candidate_info) != candidate_fingerprint
            or terminal_canonical_raw != raw
            or _fingerprint(terminal_canonical_info) != outcome.fingerprint
            or outcome.canonical_path != destination
            or outcome.canonical_sha256 != expected_candidate_sha256
            or outcome.size_bytes != len(raw)
            or outcome.publication_method != PUBLICATION_METHOD
        ):
            raise PathContractError("release terminal publication outcome mismatch")
        candidate_binding = _publication_file_binding(
            candidate, raw, candidate_fingerprint,
            expected_mode=0o600, context="release publication candidate",
        )
        canonical_binding = _publication_file_binding(
            destination, raw, outcome.fingerprint,
            expected_mode=0o644, context="release publication canonical",
        )
        receipt = _publication_receipt_common(
            artifact_role="RELEASE_PROVENANCE_PUBLICATION_RECEIPT",
            authority=EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
            claim_boundary=RELEASE_PUBLICATION_CLAIM_BOUNDARY,
            candidate=candidate_binding,
            canonical=canonical_binding,
        )
        roles = expected["roles"]
        if type(roles) is not list:
            raise ReleaseError("release publication ordered role array is invalid")
        exact_int(len(roles), "release publication role count", expected=68)
        receipt.update({
            "role_count": 68,
            "ordered_roles_sha256": sha256_bytes(canonical_json_bytes(roles)),
            "main_freeze_sha256": expected["main_freeze_sha256"],
            "archive_generation_sha256": expected["archive_generation_sha256"],
        })
        exact_keys(
            receipt, RELEASE_PUBLICATION_RECEIPT_KEYS,
            "release publication receipt",
        )
        for name in (
            "ordered_roles_sha256", "main_freeze_sha256",
            "archive_generation_sha256",
        ):
            require_sha256(receipt[name], f"release publication {name}")
        _validate_release_publication_receipt(receipt)
        canonical_json_bytes(receipt)
    return receipt


def verify_release(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    with capture_input_generation():
        expected = _build_expected_release(root)
        stored, raw = strict_json_image(release_path(root), canonical="compact")
        if raw != canonical_json_bytes(expected) or not exact_json_equal(stored, expected):
            raise ReleaseError("V2 release bytes or 68-role DAG mismatch")
        _terminal_replay_generation()
    return dict(stored)


def _minimal_machine_roles(project_root: Path) -> dict[str, dict[str, str]]:
    table = dict(INPUT_ROLES)
    return {
        role: _role_binding(project_root, role, table[role])
        for role in (
            "scheduler", "static_evaluator", "branch_evaluator_source",
            "branch_evaluator_binary", "l1_final_plan",
        )
    }


def verify_formal_machine_freeze_path(path: Path | str) -> dict[str, Any]:
    candidate = lexical_absolute(path)
    with capture_input_generation():
        machine, raw, _ = _read_candidate_policy(
            candidate,
            canonical=project_file(ROOT, dict(INPUT_ROLES)["machine_freeze"]),
            temporary_mode=0o644, maximum_bytes=64 * 1024 * 1024,
        )
        roles = _minimal_machine_roles(ROOT)
        validate_formal_machine_freeze(ROOT, machine, roles)
    return {
        "verification_status": "PASS_MACHINE_FREEZE_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "promotion_authorized": False,
    }


def verify_s0_compatibility_path(path: Path | str) -> dict[str, Any]:
    candidate = lexical_absolute(path)
    with capture_input_generation():
        payload, raw, _ = _read_candidate_policy(
            candidate,
            canonical=project_file(ROOT, dict(INPUT_ROLES)["s0_compatibility"]),
            temporary_mode=0o600, maximum_bytes=4 * 1024 * 1024,
        )
        table = dict(INPUT_ROLES)
        role_names = (
            "s0_adapter", "prefreeze_design", "checker_contract", "release_contract",
            *S0_CONTROL_ROLE_MAP.values(),
        )
        needed: dict[str, dict[str, Any]] = {
            role: _role_binding(ROOT, role, table[role]) for role in role_names
        }
        needed["s0_compatibility"] = {
            "role": "s0_compatibility", "path": table["s0_compatibility"],
            "sha256": sha256_bytes(raw),
        }
        _validate_s0_payload(ROOT, payload, needed)
    return {
        "verification_status": "PASS_S0_COMPATIBILITY_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "promotion_authorized": False,
    }


def verify_prefreeze_tests_path(path: Path | str) -> dict[str, Any]:
    """Verify a private role-11 candidate with no subprocess and no writes."""

    candidate = lexical_absolute(path)
    with capture_input_generation():
        payload, raw, is_canonical = _read_candidate_policy(
            candidate,
            canonical=project_file(ROOT, dict(INPUT_ROLES)["prefreeze_tests"]),
            temporary_mode=0o600, maximum_bytes=4 * 1024 * 1024,
        )
        _validate_prefreeze_tests_payload(
            ROOT, payload, require_current=not is_canonical
        )
    return {
        "verification_status": "PASS_PREFREEZE_TEST_RECORD_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "promotion_authorized": False,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--verify-only", action="store_true")
    # Keep raw strings until ``lexical_absolute`` has rejected every spelling
    # alias.  ``argparse`` coercion to Path would erase `//`, `.` and `..`.
    modes.add_argument("--build-main-freeze-candidate", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--verify-main-freeze", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--publish-main-freeze", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--build-report-candidate", metavar="ABSOLUTE_MD_PATH")
    modes.add_argument("--verify-report", metavar="ABSOLUTE_MD_PATH")
    modes.add_argument("--publish-report", metavar="ABSOLUTE_MD_PATH")
    modes.add_argument("--build-release-candidate", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--verify-release-candidate", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--publish-release", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--verify-machine-freeze", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--verify-s0-compatibility", metavar="ABSOLUTE_JSON_PATH")
    modes.add_argument("--verify-prefreeze-tests", metavar="ABSOLUTE_JSON_PATH")
    parser.add_argument("--expected-candidate-sha256")
    parser.add_argument("--publication-authority")
    parser.add_argument("--role20-receipt", metavar="ABSOLUTE_JSON_PATH")
    parser.add_argument("--role21-receipt", metavar="ABSOLUTE_JSON_PATH")
    parser.add_argument("--role22-receipt", metavar="ABSOLUTE_JSON_PATH")
    return parser.parse_args(argv)


def _print_verify_receipt(prefix: str, receipt: Mapping[str, Any]) -> None:
    print(
        f"{prefix}={receipt['verification_status']} "
        f"authority={receipt['authority']} "
        f"candidate_sha256={receipt['candidate_sha256']} "
        f"size_bytes={receipt['size_bytes']} promotion_authorized=false"
    )


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        publishing = (
            arguments.publish_main_freeze is not None
            or arguments.publish_report is not None
            or arguments.publish_release is not None
        )
        receipt_arguments = (
            arguments.role20_receipt,
            arguments.role21_receipt,
            arguments.role22_receipt,
        )
        if publishing:
            if arguments.expected_candidate_sha256 is None or arguments.publication_authority is None:
                raise ReleaseError("publication requires explicit expected digest and authority")
            require_sha256(arguments.expected_candidate_sha256, "CLI expected candidate digest")
        elif arguments.expected_candidate_sha256 is not None or arguments.publication_authority is not None:
            raise ReleaseError("publication digest/authority flags are forbidden in nonpublish modes")
        if arguments.publish_main_freeze is not None:
            if any(value is None for value in receipt_arguments):
                raise ReleaseError("role54 publication requires all three checker receipt paths")
        elif any(value is not None for value in receipt_arguments):
            raise ReleaseError("checker receipt paths are allowed only for role54 publication")
        root = lexical_absolute(ROOT)
        if arguments.build_main_freeze_candidate is not None:
            payload = build_main_freeze_candidate(root, lexical_absolute(arguments.build_main_freeze_candidate))
            print(f"main_freeze_candidate_sha256={sha256_bytes(canonical_json_bytes(payload))} roles=53")
            return 0
        if arguments.verify_main_freeze is not None:
            receipt = verify_formal_main_freeze_path(arguments.verify_main_freeze)
            _print_verify_receipt("main_freeze_verification", receipt)
            return 0
        if arguments.publish_main_freeze is not None:
            checker_receipts, checker_receipt_snapshots = _read_main_checker_receipt_set({
                "static": lexical_absolute(arguments.role20_receipt),
                "branch": lexical_absolute(arguments.role21_receipt),
                "composite": lexical_absolute(arguments.role22_receipt),
            })
            receipt = publish_main_freeze(
                root, lexical_absolute(arguments.publish_main_freeze),
                checker_receipts=checker_receipts,
                expected_candidate_sha256=arguments.expected_candidate_sha256,
                publication_authority=arguments.publication_authority,
                _checker_receipt_snapshots=checker_receipt_snapshots,
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0
        if arguments.build_report_candidate is not None:
            raw = build_report_candidate(
                root, lexical_absolute(arguments.build_report_candidate)
            )
            print(
                f"report_candidate_sha256={sha256_bytes(raw)} "
                "upstream_roles=14"
            )
            return 0
        if arguments.verify_report is not None:
            receipt = verify_report_candidate(
                root, lexical_absolute(arguments.verify_report)
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0
        if arguments.publish_report is not None:
            receipt = publish_report(
                root, lexical_absolute(arguments.publish_report),
                expected_candidate_sha256=arguments.expected_candidate_sha256,
                publication_authority=arguments.publication_authority,
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0
        if arguments.build_release_candidate is not None:
            payload = build_release(root, lexical_absolute(arguments.build_release_candidate))
            print(f"release_candidate_sha256={sha256_bytes(canonical_json_bytes(payload))} roles=68")
            return 0
        if arguments.verify_release_candidate is not None:
            payload = verify_release_candidate(root, lexical_absolute(arguments.verify_release_candidate))
            print(f"release_candidate_verification=PASS_RELEASE_VERIFY_ONLY roles={len(payload['roles'])}")
            return 0
        if arguments.publish_release is not None:
            receipt = publish_release(
                root, lexical_absolute(arguments.publish_release),
                expected_candidate_sha256=arguments.expected_candidate_sha256,
                publication_authority=arguments.publication_authority,
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0
        if arguments.verify_machine_freeze is not None:
            receipt = verify_formal_machine_freeze_path(arguments.verify_machine_freeze)
            _print_verify_receipt("machine_freeze_verification", receipt)
            return 0
        if arguments.verify_s0_compatibility is not None:
            receipt = verify_s0_compatibility_path(arguments.verify_s0_compatibility)
            _print_verify_receipt("s0_compatibility_verification", receipt)
            return 0
        if arguments.verify_prefreeze_tests is not None:
            receipt = verify_prefreeze_tests_path(arguments.verify_prefreeze_tests)
            _print_verify_receipt("prefreeze_test_verification", receipt)
            return 0
        if not arguments.verify_only:
            raise ReleaseError("no exact V2 role24 mode selected")
        payload = verify_release(root)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"release_status={payload['release_status']} roles={len(payload['roles'])} "
        "scientific_licensing_enabled=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
