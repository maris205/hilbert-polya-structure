#!/usr/bin/env python3
"""Read-only S0-to-A1 schema compatibility replay for R401-VAL-L3.

This adapter validates sealed representative S0 bytes against the prospective
L3-A1 control boundary.  It never imports or invokes an evaluator, packager,
or component checker.  Capture writes one validated temporary candidate under
``/tmp``.  Publication is a separate, fixed-destination, write-once
``renameat2(RENAME_NOREPLACE)`` transaction.  Neither mode authorizes a
scientific dispatch or a main freeze.
"""

from __future__ import annotations

import argparse
import ctypes
from dataclasses import dataclass
import errno
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import stat
import sys
from typing import Any


ROOT = Path(__file__).absolute().parents[1]
ADAPTER = Path(__file__).absolute()
DESIGN = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md"
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/"
    "R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
)
CANONICAL_OUTPUT = (
    ROOT
    / "research/route_a_wave_trace/"
    "R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
)
ROLE13_RELATIVE_PATH = Path(
    "research/route_a_wave_trace/"
    "R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
)
STATIC_DIR = ROOT / "results/r401_val_l3_phase_tube_smoke"
BRANCH_DIR = ROOT / "results/r401_val_l3_branch_tube_smoke"
COMPOSITE_DIR = ROOT / "results/r401_val_l3_s0_composite"

SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY"
STATIC_PROTOCOL = "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT"
BRANCH_PROTOCOL = "R401-VAL-L3-BT-S0"
COMPOSITE_PROTOCOL = "R401-VAL-L3-S0-COMPOSITE-DRAFT"
ARTIFACT_STATUS = "DRAFT_NON_LICENSING"
STATIC_IMPLEMENTATION = "PASS_STATIC_COMPONENT_SMOKE"
BRANCH_IMPLEMENTATION = "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
COMPOSITE_IMPLEMENTATION = "PASS_IMPLEMENTATION_SMOKE"
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
PRECISIONS = (128, 256)
EXPECTED_PAIRS = tuple(
    (precision, slab)
    for precision in PRECISIONS
    for slab in REPRESENTATIVE_SLABS
)
TREE_IDS = ("ANGLE", "SECTION_LOW", "SECTION_WINDOW", "SECTION_HIGH")

CONTROL_PATHS = {
    "static_summary": STATIC_DIR / "summary.json",
    "static_manifest": STATIC_DIR / "manifest.json",
    "static_checker": STATIC_DIR / "independent_checker.json",
    "branch_summary": BRANCH_DIR / "summary.json",
    "branch_manifest": BRANCH_DIR / "manifest.json",
    "branch_checker": BRANCH_DIR / "independent_checker.json",
    "composite_summary": COMPOSITE_DIR / "summary.json",
    "composite_manifest": COMPOSITE_DIR / "manifest.json",
    "composite_checker": COMPOSITE_DIR / "independent_checker.json",
}
CONTROL_HASHES = {
    "static_summary": "e55c5280dcda615dcc672e58694a5639177fd0777595ff03eca163014c1bc225",
    "static_manifest": "f37b11967aab879e369080d3440d932c706bfe662734065077a51cfb1f5bb2ce",
    "static_checker": "4be68b9369714cba1979b03bcb08bc9dd40a4de8a02732b90fb87b39b422a262",
    "branch_summary": "a8853e4eb308cd44ad8413cbbd45da29240c113df15ea4ff3472bc740d3b089a",
    "branch_manifest": "edfa8a2a8e82e14e95828173da3b30c6a8820ef9950d5f31125bddc9c76231bc",
    "branch_checker": "162ebcc992054945deb48c84fa9b47bff970e9865cb629633049b986e3986753",
    "composite_summary": "ab0d7921623a5d4ba61d148ce833d22e14da75c77385897c328b20e41d64257f",
    "composite_manifest": "75c1533196c6c4df96bf21c09ecae3230423924323709652c259cbcd1d67cb05",
    "composite_checker": "197a087ecc75c95f186764f5365d3fc6769cb4cfe99793bfc1abc61afc037470",
}
PUBLIC_FACTS = {
    "static_proof_count": 6,
    "static_nodes": 84172,
    "static_internal_nodes": 42074,
    "static_terminal_nodes": 42098,
    "static_unresolved_nodes": 0,
    "static_independent_checks": 122300,
    "static_maximum_depth": 14,
    "branch_raw_replay_count": 6,
    "branch_manifest_file_count": 26,
    "composite_cell_count": 6,
    "composite_binding_count": 18,
    "composite_failures": 0,
}
STATIC_FACTS = {
    "proof_count": 6,
    "node_count": 84172,
    "internal_count": 42074,
    "terminal_count": 42098,
    "unresolved_count": 0,
    "independent_interval_checks": 122300,
    "maximum_depth": 14,
}
BRANCH_FACTS = {
    "raw_replay_count": 6,
    "manifest_file_count": 26,
}
COMPOSITE_FACTS = {
    "cell_replay_count": 6,
    "manifest_binding_count": 18,
    "failure_count": 0,
}
COMPATIBILITY_OUTPUT_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "source_protocols", "matrix", "static_facts", "branch_facts",
    "composite_facts", "control_hashes", "role_sets", "source_bindings",
    "replay_status", "failures", "claim_boundary", "milestone_status",
    "theorem_status", "final_status",
}

STATIC_SUMMARY_KEYS = {
    "artifact_status", "claim_boundary", "component_scope",
    "composite_s0_passed", "final_status", "implementation_status",
    "matrix", "proofs", "protocol_id", "schema_version",
    "scientific_licensing_enabled", "source_bindings", "totals",
}
STATIC_MANIFEST_KEYS = {
    "artifact_status", "component_scope", "composite_s0_passed", "files",
    "final_status", "implementation_status", "protocol_id", "schema_version",
    "scientific_licensing_enabled",
}
STATIC_CHECKER_KEYS = {
    "artifact_status", "checker_sha256", "claim_boundary", "component_scope",
    "composite_s0_passed", "final_status", "implementation_status",
    "independent_interval_checks", "internal_count", "node_count", "passed",
    "proof_count", "proof_results", "protocol_id", "schema_version",
    "scientific_licensing_enabled", "terminal_count", "unresolved_count",
}
STATIC_ENTRY_KEYS = {
    "internal_count", "node_count", "path", "precision_bits", "sha256",
    "size_bytes", "slab_id", "terminal_count", "tree_content_sha256",
    "unresolved_count",
}
STATIC_REPLAY_KEYS = (STATIC_ENTRY_KEYS - {"size_bytes"}) | {
    "angle_extrema", "interval_checks",
}
STATIC_PROOF_KEYS = {
    "artifact_status", "claim_boundary", "component_scope",
    "composite_s0_passed", "counts", "epsilon", "final_status",
    "implementation_status", "outer_containment", "period_window",
    "precision_bits", "protocol_id", "schema_version",
    "scientific_licensing_enabled", "slab_id", "source_bindings", "trees",
    "wall_seconds",
}
TREE_KEYS = {
    "angle_extrema", "complete", "content_hash_definition", "content_sha256",
    "coordinates", "goal", "internal_count", "maximum_depth", "node_count",
    "nodes", "root_box", "split_rule", "terminal_count", "terminal_counts",
    "tree_id", "unresolved_count",
}

BRANCH_SUMMARY_KEYS = {
    "claim_boundary", "elapsed_seconds", "environment", "final_status",
    "input_hashes", "licensing", "milestone_status", "pair_gate", "phase_grid",
    "precisions", "protocol_id", "prototype_status", "records",
    "representative_slabs", "theorem_status", "tube_radius", "tube_radius_sq",
}
BRANCH_MANIFEST_KEYS = {
    "files", "final_status", "licensing", "milestone_status", "protocol_id",
    "prototype_status", "theorem_status",
}
BRANCH_CHECKER_KEYS = {
    "checker_status", "failures", "final_status", "licensing",
    "manifest_file_count", "maximum_rslow_sq_upper", "milestone_status",
    "minimum_margin_sq_lower", "protocol_id", "prototype_status",
    "raw_replay_count", "theorem_status",
}
BRANCH_RECORD_KEYS = {
    "all_segments_inside", "argv", "epsilon", "input_echo_gate",
    "maximum_rslow_sq_upper", "maximum_segment_rslow_sq_upper",
    "minimum_margin_sq_lower", "omega_slow", "passed", "phase_cover_complete",
    "precision_bits", "raw_file", "returncode", "root_box", "slab_id",
    "solution_piece_count", "status", "stderr_file", "taylor_order",
    "terminal_state_box", "tolerance", "wall_seconds",
}

COMPOSITE_COMMON_KEYS = {
    "schema_version", "protocol_id", "artifact_status",
    "scientific_licensing_enabled", "component_scope", "composite_s0_passed",
    "implementation_status", "milestone_status", "theorem_status", "final_status",
}
COMPOSITE_SUMMARY_KEYS = COMPOSITE_COMMON_KEYS | {
    "claim_boundary", "matrix", "components", "cells", "source_bindings",
}
COMPOSITE_MANIFEST_KEYS = COMPOSITE_COMMON_KEYS | {"files", "component_files"}
COMPOSITE_CHECKER_KEYS = {
    "artifact_status", "cell_replay_count", "checker_sha256", "checker_status",
    "claim_boundary", "component_scope", "composite_s0_passed", "failures",
    "final_status", "implementation_status", "manifest_binding_count",
    "milestone_status", "protocol_id", "schema_version",
    "scientific_licensing_enabled", "theorem_status",
}
COMPONENT_DESCRIPTOR_KEYS = {
    "checker_passed", "component_scope", "component_status",
    "composite_s0_passed", "control_files", "final_status", "milestone_status",
    "protocol_id", "scientific_licensing_enabled", "theorem_status",
}

BRANCH_ROLE_PATHS = (
    "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
    "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/summary.json",
    "results/r401_val_l3_branch_tube_smoke/R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md",
    "results/r401_val_l3_branch_tube_smoke/capd_r401_phase_branch_tube_mp",
    "results/r401_val_l3_branch_tube_smoke/compile_stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/compile_stdout.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/128/S000.stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/128/S000.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/128/S025.stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/128/S025.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/128/S050.stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/128/S050.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/256/S000.stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/256/S000.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/256/S025.stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/256/S025.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/256/S050.stderr.txt",
    "results/r401_val_l3_branch_tube_smoke/raw/256/S050.txt",
    "results/r401_val_l3_branch_tube_smoke/summary.json",
    "scripts/check_r401_val_l3_branch_tube_smoke_independent.py",
    "scripts/run_r401_val_l3_branch_tube_smoke.py",
    "validated/CAPD_DEPENDENCY.md",
    "validated/capd_r401_phase_branch_tube_mp.cpp",
)
BRANCH_INPUT_ROLES = (
    "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
    "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/summary.json",
    "scripts/check_r401_val_l3_branch_tube_smoke_independent.py",
    "scripts/run_r401_val_l3_branch_tube_smoke.py",
    "validated/CAPD_DEPENDENCY.md",
    "validated/capd_r401_phase_branch_tube_mp.cpp",
)
COMPOSITE_FILE_ROLES = (
    ("OUTPUT", "summary.json"),
    ("OUTPUT", "R401_VAL_L3_S0_COMPOSITE_REPORT.md"),
    ("ROOT", "scripts/build_r401_val_l3_s0_composite.py"),
    ("ROOT", "scripts/check_r401_val_l3_s0_composite_independent.py"),
    ("ROOT", "scripts/run_r401_val_l3_phase_tube_smoke.py"),
    ("ROOT", "scripts/check_r401_val_l3_phase_tube_independent.py"),
    ("ROOT", "validated/capd_r401_phase_branch_tube_mp.cpp"),
    ("ROOT", "scripts/run_r401_val_l3_branch_tube_smoke.py"),
    ("ROOT", "scripts/check_r401_val_l3_branch_tube_smoke_independent.py"),
    ("ROOT", "research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md"),
    ("ROOT", "research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md"),
    ("ROOT", "research/route_a_wave_trace/refine-logs/A416_EXPERIMENT_PLAN.md"),
)
COMPOSITE_COMPONENT_ROLES = tuple(
    (component, name)
    for component in ("static", "branch")
    for name in ("summary.json", "manifest.json", "independent_checker.json")
)
COMPATIBILITY_SOURCE_ROLES = (
    "scripts/replay_r401_val_l3_s0_through_a1_checkers.py",
    "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md",
    "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md",
    "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md",
)
COMPATIBILITY_CLAIM_BOUNDARY = (
    "read-only compatibility replay of the sealed representative 3x2 S0 "
    "archive only; non-licensing and no evaluator dispatch; no all-slab "
    "result, theorem promotion, global orbit exclusion, trace formula, "
    "Hilbert-Polya construction, zeta-zero result, or RH claim"
)


class CompatibilityError(RuntimeError):
    """A fail-closed compatibility or provenance violation."""


MAX_INPUT_BYTES = 64 * 1024 * 1024
PUBLICATION_MAX_CANDIDATE_BYTES = 1024 * 1024
PUBLICATION_STAGE_PREFIX = (
    ".R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json.stage."
)
PUBLICATION_METHOD = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
PUBLICATION_HOOK_PHASES = frozenset(
    {
        "AFTER_STAGE_WRITE",
        "AFTER_STAGE_FILE_FSYNC",
        "AFTER_STAGING_PARENT_FSYNC",
        "BEFORE_TERMINAL_REPLAY",
        "BEFORE_RENAME",
        "AFTER_RENAME",
        "AFTER_DESTINATION_FSYNC",
        "AFTER_PUBLICATION_PARENT_FSYNC",
        "AFTER_POSTPUBLICATION_REPLAY",
    }
)


class SyntheticCompatibilityPublicationCrash(RuntimeError):
    """Test-only crash marker; production never raises this on its own."""


@dataclass(frozen=True)
class FileImage:
    path: Path
    data: bytes
    metadata: tuple[int, ...]

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest()

    @property
    def size(self) -> int:
        return len(self.data)


def _metadata(info: os.stat_result) -> tuple[int, ...]:
    return (
        info.st_dev, info.st_ino, info.st_mode, info.st_nlink, info.st_size,
        info.st_mtime_ns, info.st_ctime_ns,
    )


def _canonical_absolute(path: Path, context: str) -> Path:
    if not path.is_absolute():
        raise CompatibilityError(f"{context}: absolute path required")
    text = os.fspath(path)
    if (
        "\x00" in text
        or "\\" in text
        or text.startswith("//")
        or "//" in text[1:]
        or text.endswith("/")
    ):
        raise CompatibilityError(f"{context}: non-canonical path spelling")
    if any(part in ("", ".", "..") for part in path.parts[1:]):
        raise CompatibilityError(f"{context}: dot or empty path component")
    if Path(os.path.abspath(text)) != path:
        raise CompatibilityError(f"{context}: normalized path alias")
    return path


def canonical_relative(value: Any, context: str, *, hidden_ok: bool = False) -> str:
    if type(value) is not str or not value:
        raise CompatibilityError(f"{context}: nonempty string required")
    if "\x00" in value or "\\" in value or value.startswith("/"):
        raise CompatibilityError(f"{context}: unsafe relative path")
    if "//" in value or value.endswith("/"):
        raise CompatibilityError(f"{context}: non-canonical relative path")
    pure = PurePosixPath(value)
    if str(pure) != value or any(part in ("", ".", "..") for part in pure.parts):
        raise CompatibilityError(f"{context}: normalized or traversal alias")
    if not hidden_ok and any(part.startswith(".") for part in pure.parts):
        raise CompatibilityError(f"{context}: hidden path component")
    return value


def _secure_read(path: Path, context: str) -> FileImage:
    path = _canonical_absolute(path, context)
    directory_flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory_fd = os.open("/", directory_flags)
    file_fd: int | None = None
    try:
        for index, component in enumerate(path.parts[1:]):
            leaf = index == len(path.parts[1:]) - 1
            flags = os.O_RDONLY | nofollow
            if not leaf:
                flags |= getattr(os, "O_DIRECTORY", 0)
            next_fd = os.open(component, flags, dir_fd=directory_fd)
            if leaf:
                file_fd = next_fd
            else:
                os.close(directory_fd)
                directory_fd = next_fd
        if file_fd is None:
            raise CompatibilityError(f"{context}: file path required")
        info_before = os.fstat(file_fd)
        if not stat.S_ISREG(info_before.st_mode):
            raise CompatibilityError(f"{context}: regular file required")
        if info_before.st_nlink != 1:
            raise CompatibilityError(f"{context}: hard-link alias rejected")
        if info_before.st_size > MAX_INPUT_BYTES:
            raise CompatibilityError(f"{context}: frozen input size cap exceeded")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(file_fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        info_after = os.fstat(file_fd)
        if _metadata(info_before) != _metadata(info_after):
            raise CompatibilityError(f"{context}: file changed while read")
        data = b"".join(chunks)
        if len(data) != info_after.st_size:
            raise CompatibilityError(f"{context}: short or unstable read")
        return FileImage(path, data, _metadata(info_after))
    except OSError as error:
        raise CompatibilityError(f"{context}: secure open failed: {error}") from error
    finally:
        if file_fd is not None:
            os.close(file_fd)
        os.close(directory_fd)


class InputSnapshot:
    """Single-read byte snapshots with a final same-path TOCTOU audit."""

    def __init__(self) -> None:
        self._images: dict[Path, FileImage] = {}

    def capture(self, path: Path, context: str) -> FileImage:
        candidate = path if path.is_absolute() else Path.cwd() / path
        absolute = _canonical_absolute(candidate, context)
        image = self._images.get(absolute)
        if image is None:
            image = _secure_read(absolute, context)
            self._images[absolute] = image
        return image

    def json(self, path: Path, context: str) -> dict[str, Any]:
        return strict_json_bytes(self.capture(path, context).data, context)

    def assert_unchanged(self) -> None:
        for path, original in self._images.items():
            current = _secure_read(path, f"TOCTOU recheck {path}")
            if current.metadata != original.metadata or current.data != original.data:
                raise CompatibilityError(f"TOCTOU mutation detected: {path}")

    @property
    def count(self) -> int:
        return len(self._images)


def _reject_constant(value: str) -> None:
    raise CompatibilityError(f"non-finite JSON constant: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise CompatibilityError(f"non-finite JSON float: {value}")
    return parsed


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CompatibilityError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_bytes(data: bytes, context: str) -> dict[str, Any]:
    try:
        text = data.decode("utf-8", errors="strict")
        payload = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except CompatibilityError:
        raise
    except Exception as error:
        raise CompatibilityError(f"{context}: invalid strict JSON: {error}") from error
    if type(payload) is not dict:
        raise CompatibilityError(f"{context}: top-level object required")
    return payload


def canonical_json_bytes(payload: Any) -> bytes:
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


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


def require_exact(actual: Any, expected: Any, context: str) -> None:
    if not exact_json_equal(actual, expected):
        raise CompatibilityError(f"{context}: exact JSON mismatch")


def exact_keys(payload: Any, expected: set[str], context: str) -> dict[str, Any]:
    if type(payload) is not dict:
        raise CompatibilityError(f"{context}: object required")
    if set(payload) != expected:
        raise CompatibilityError(
            f"{context}: missing={sorted(expected - set(payload))}; "
            f"extra={sorted(set(payload) - expected)}"
        )
    return payload


def exact_int(value: Any, context: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise CompatibilityError(f"{context}: exact integer >= {minimum} required")
    return value


def finite_number(value: Any, context: str, *, minimum: float = 0.0) -> int | float:
    if type(value) not in (int, float) or not math.isfinite(value) or value < minimum:
        raise CompatibilityError(f"{context}: finite number >= {minimum} required")
    return value


def hash_string(value: Any, context: str) -> str:
    if (
        type(value) is not str
        or len(value) != 64
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise CompatibilityError(f"{context}: lowercase SHA-256 required")
    return value


def require_null_authority(payload: dict[str, Any], context: str) -> None:
    if payload.get("final_status", object()) is not None:
        raise CompatibilityError(f"{context}: final authority must be null")
    for key in ("milestone_status", "theorem_status"):
        if key in payload and payload[key] is not None:
            raise CompatibilityError(f"{context}: {key} must be null")


def static_common(payload: dict[str, Any], context: str) -> None:
    expected = {
        "schema_version": 1,
        "protocol_id": STATIC_PROTOCOL,
        "artifact_status": ARTIFACT_STATUS,
        "implementation_status": STATIC_IMPLEMENTATION,
        "component_scope": "STATIC_ONLY",
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
    }
    for key, value in expected.items():
        if key not in payload or not exact_json_equal(payload[key], value):
            raise CompatibilityError(f"{context}: {key}")
    require_null_authority(payload, context)


def _tree_hashes(value: Any, context: str) -> dict[str, str]:
    exact_keys(value, set(TREE_IDS), context)
    return {key: hash_string(value[key], f"{context}.{key}") for key in TREE_IDS}


def validate_static_summary_shape(
    summary: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[tuple[int, str], dict[str, Any]]]:
    exact_keys(summary, STATIC_SUMMARY_KEYS, "static summary")
    static_common(summary, "static summary")
    require_exact(
        summary["matrix"],
        {"precisions": [128, 256], "proof_count": 6,
         "slabs": ["S000", "S025", "S050"]},
        "static matrix",
    )
    proofs = summary["proofs"]
    if type(proofs) is not list or len(proofs) != 6:
        raise CompatibilityError("static summary: exactly six proofs required")
    by_pair: dict[tuple[int, str], dict[str, Any]] = {}
    for expected_pair, entry in zip(EXPECTED_PAIRS, proofs, strict=True):
        exact_keys(entry, STATIC_ENTRY_KEYS, "static proof entry")
        pair = (
            exact_int(entry["precision_bits"], "static precision", minimum=1),
            entry["slab_id"],
        )
        if type(pair[1]) is not str or pair != expected_pair:
            raise CompatibilityError(f"static proof order/identity: {pair}")
        expected_name = f"proof_{pair[0]}_{pair[1]}.json"
        if canonical_relative(entry["path"], "static proof path") != expected_name:
            raise CompatibilityError(f"static proof path: {pair}")
        hash_string(entry["sha256"], "static proof hash")
        exact_int(entry["size_bytes"], "static proof size", minimum=1)
        nodes = exact_int(entry["node_count"], "static node count", minimum=1)
        internal = exact_int(entry["internal_count"], "static internal count")
        terminal = exact_int(entry["terminal_count"], "static terminal count", minimum=1)
        unresolved = exact_int(entry["unresolved_count"], "static unresolved count")
        if nodes != internal + terminal or unresolved != 0:
            raise CompatibilityError(f"static proof count identity: {pair}")
        _tree_hashes(entry["tree_content_sha256"], "static tree hashes")
        by_pair[pair] = entry
    totals = exact_keys(
        summary["totals"],
        {"node_count", "internal_count", "terminal_count", "unresolved_count",
         "wall_seconds"},
        "static totals",
    )
    computed = {
        "node_count": sum(item["node_count"] for item in proofs),
        "internal_count": sum(item["internal_count"] for item in proofs),
        "terminal_count": sum(item["terminal_count"] for item in proofs),
        "unresolved_count": sum(item["unresolved_count"] for item in proofs),
    }
    for key, expected in computed.items():
        if exact_int(totals[key], f"static totals.{key}") != expected:
            raise CompatibilityError(f"static total mismatch: {key}")
    finite_number(totals["wall_seconds"], "static total wall time")
    if type(summary["claim_boundary"]) is not str:
        raise CompatibilityError("static summary: claim boundary string required")
    bindings = exact_keys(
        summary["source_bindings"],
        {"checker_sha256", "l1_final_plan_sha256", "l1_release_chain_sha256",
         "runner_sha256"},
        "static source bindings",
    )
    hash_string(bindings["checker_sha256"], "static checker binding")
    hash_string(bindings["runner_sha256"], "static runner binding")
    hash_string(bindings["l1_final_plan_sha256"], "static L1 plan binding")
    release = exact_keys(
        bindings["l1_release_chain_sha256"],
        {
            "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
            "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
            "results/r401_val_l1_branch/independent_checker.json",
            "results/r401_val_l1_branch/manifest.json",
            "results/r401_val_l1_branch/summary.json",
        },
        "static L1 release bindings",
    )
    for role, digest in release.items():
        canonical_relative(role, "static L1 release role")
        hash_string(digest, "static L1 release hash")
    return proofs, by_pair


def validate_static_source_bindings(
    bindings: dict[str, Any], snapshot: InputSnapshot
) -> None:
    direct = {
        "checker_sha256": "scripts/check_r401_val_l3_phase_tube_independent.py",
        "runner_sha256": "scripts/run_r401_val_l3_phase_tube_smoke.py",
        "l1_final_plan_sha256":
            "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    }
    for key, role in direct.items():
        image = snapshot.capture(ROOT / role, f"static source binding {role}")
        require_exact(bindings[key], image.sha256, f"static source hash {role}")
    for role, digest in bindings["l1_release_chain_sha256"].items():
        image = snapshot.capture(ROOT / role, f"static L1 binding {role}")
        require_exact(digest, image.sha256, f"static L1 hash {role}")


def validate_static_manifest_shape(
    manifest: dict[str, Any], proofs: list[dict[str, Any]], summary: FileImage
) -> None:
    exact_keys(manifest, STATIC_MANIFEST_KEYS, "static manifest")
    static_common(manifest, "static manifest")
    files = manifest["files"]
    if type(files) is not list or len(files) != 7:
        raise CompatibilityError("static manifest: exactly seven roles required")
    for expected, actual in zip(proofs, files[:6], strict=True):
        exact_keys(actual, STATIC_ENTRY_KEYS, "static manifest proof role")
        require_exact(actual, expected, "static manifest proof role")
    final = exact_keys(files[6], {"path", "sha256", "size_bytes"}, "static summary role")
    require_exact(final["path"], "summary.json", "static summary role path")
    require_exact(hash_string(final["sha256"], "static summary role hash"), summary.sha256,
                  "static summary role hash")
    if exact_int(final["size_bytes"], "static summary role size", minimum=1) != summary.size:
        raise CompatibilityError("static summary role size mismatch")


def _fraction_record(value: Any, context: str) -> None:
    exact_keys(value, {"numerator", "denominator"}, context)
    if type(value["numerator"]) is not str or type(value["denominator"]) is not str:
        raise CompatibilityError(f"{context}: fraction strings required")


def _validate_tree(tree: dict[str, Any], tree_id: str) -> int:
    exact_keys(tree, TREE_KEYS, f"static tree {tree_id}")
    require_exact(tree["tree_id"], tree_id, f"static tree {tree_id} identity")
    expected_goal = "ANGLE_COVER" if tree_id == "ANGLE" else "SECTION_WINDOW_COVER"
    require_exact(tree["goal"], expected_goal, f"static tree {tree_id} goal")
    expected_coordinates = (
        ["qminus", "qplus", "pminus", "pplus"]
        if tree_id == "ANGLE" else ["qminus", "qplus", "pminus"]
    )
    require_exact(tree["coordinates"], expected_coordinates,
                  f"static tree {tree_id} coordinates")
    require_exact(
        tree["split_rule"],
        "largest_normalized_width_then_coordinate_order_exact_midpoint",
        f"static tree {tree_id} split rule",
    )
    require_exact(
        tree["content_hash_definition"],
        "sha256(canonical_json(tree_without_content_sha256))",
        f"static tree {tree_id} hash definition",
    )
    digest = hash_string(tree["content_sha256"], f"static tree {tree_id} hash")
    without_hash = dict(tree)
    del without_hash["content_sha256"]
    if hashlib.sha256(canonical_json_bytes(without_hash)).hexdigest() != digest:
        raise CompatibilityError(f"static tree {tree_id}: content hash mismatch")
    if tree["complete"] is not True:
        raise CompatibilityError(f"static tree {tree_id}: incomplete")
    nodes = tree["nodes"]
    if type(nodes) is not list or not nodes:
        raise CompatibilityError(f"static tree {tree_id}: nonempty node list required")
    node_count = exact_int(tree["node_count"], f"static tree {tree_id} nodes", minimum=1)
    internal_count = exact_int(tree["internal_count"], f"static tree {tree_id} internal")
    terminal_count = exact_int(tree["terminal_count"], f"static tree {tree_id} terminal", minimum=1)
    unresolved_count = exact_int(tree["unresolved_count"], f"static tree {tree_id} unresolved")
    maximum_depth = exact_int(tree["maximum_depth"], f"static tree {tree_id} depth")
    if node_count != len(nodes) or node_count != internal_count + terminal_count or unresolved_count != 0:
        raise CompatibilityError(f"static tree {tree_id}: count identity")
    expected_terminal_keys = {
        "ANGLE": {"ANGLE_CERTIFIED", "ENERGY_EXCLUDED", "TUBE_EXCLUDED"},
        "SECTION_LOW": {"ENERGY_EXCLUDED"},
        "SECTION_WINDOW": {"LANDING_CLOSED_WINDOW"},
        "SECTION_HIGH": {"ENERGY_EXCLUDED"},
    }[tree_id]
    terminal_counts = exact_keys(
        tree["terminal_counts"], expected_terminal_keys,
        f"static tree {tree_id} terminal classes",
    )
    observed: dict[str, int] = {key: 0 for key in expected_terminal_keys}
    observed_internal = 0
    observed_depth = 0
    for node in nodes:
        if type(node) is not dict:
            raise CompatibilityError(f"static tree {tree_id}: node object required")
        classification = node.get("classification")
        if classification == "SPLIT":
            exact_keys(
                node,
                {"classification", "depth", "node_id", "parent_id",
                 "split_coordinate", "split_point"},
                f"static tree {tree_id} split node",
            )
            if node["split_coordinate"] not in expected_coordinates:
                raise CompatibilityError(f"static tree {tree_id}: split coordinate")
            _fraction_record(node["split_point"], f"static tree {tree_id} split point")
            observed_internal += 1
        else:
            exact_keys(
                node,
                {"classification", "decisive_intervals", "depth", "node_id",
                 "parent_id"},
                f"static tree {tree_id} terminal node",
            )
            if classification not in expected_terminal_keys:
                raise CompatibilityError(f"static tree {tree_id}: terminal class")
            decisive_keys = {
                "ENERGY_EXCLUDED": {"energy"},
                "TUBE_EXCLUDED": {"tube_squared"},
                "ANGLE_CERTIFIED": {"D_plus", "N_plus", "theta_dot",
                                    "theta_numerator"},
                "LANDING_CLOSED_WINDOW": set(),
            }[classification]
            decisive = exact_keys(
                node["decisive_intervals"], decisive_keys,
                f"static tree {tree_id} decisive intervals",
            )
            if any(type(value) is not str for value in decisive.values()):
                raise CompatibilityError(f"static tree {tree_id}: interval strings required")
            observed[classification] += 1
        depth = exact_int(node["depth"], f"static tree {tree_id} node depth")
        observed_depth = max(observed_depth, depth)
        if type(node["node_id"]) is not str:
            raise CompatibilityError(f"static tree {tree_id}: node id string required")
        if node["parent_id"] is not None and type(node["parent_id"]) is not str:
            raise CompatibilityError(f"static tree {tree_id}: parent id")
    if observed_internal != internal_count or sum(observed.values()) != terminal_count:
        raise CompatibilityError(f"static tree {tree_id}: observed count mismatch")
    for key, count in observed.items():
        if exact_int(terminal_counts[key], f"static tree {tree_id} class count") != count:
            raise CompatibilityError(f"static tree {tree_id}: terminal class count")
    if observed_depth != maximum_depth:
        raise CompatibilityError(f"static tree {tree_id}: maximum depth mismatch")
    if tree_id == "ANGLE":
        exact_keys(
            tree["angle_extrema"],
            {"maximum_theta_dot_upper", "minimum_D_plus_lower",
             "minimum_N_plus_lower", "minimum_theta_numerator_lower",
             "theta_numerator_definition"},
            "static angle extrema",
        )
    elif tree["angle_extrema"] is not None:
        raise CompatibilityError(f"static tree {tree_id}: angle extrema must be null")
    return maximum_depth


def validate_static_proof(
    proof: dict[str, Any], entry: dict[str, Any], source_bindings: dict[str, Any]
) -> int:
    pair = (entry["precision_bits"], entry["slab_id"])
    exact_keys(proof, STATIC_PROOF_KEYS, f"static proof {pair}")
    static_common(proof, f"static proof {pair}")
    require_exact(proof["precision_bits"], pair[0], f"static proof {pair} precision")
    require_exact(proof["slab_id"], pair[1], f"static proof {pair} slab")
    require_exact(proof["source_bindings"], source_bindings,
                  f"static proof {pair} source bindings")
    if type(proof["claim_boundary"]) is not str:
        raise CompatibilityError(f"static proof {pair}: claim boundary")
    finite_number(proof["wall_seconds"], f"static proof {pair} wall time")
    for name in ("epsilon", "period_window"):
        value = proof[name]
        if type(value) is not list or len(value) != 2:
            raise CompatibilityError(f"static proof {pair}: {name}")
        for index, fraction in enumerate(value):
            _fraction_record(fraction, f"static proof {pair} {name}[{index}]")
    exact_keys(proof["outer_containment"], {"all_pass", "derivation", "gates", "values"},
               f"static proof {pair} outer containment")
    if proof["outer_containment"]["all_pass"] is not True:
        raise CompatibilityError(f"static proof {pair}: outer containment")
    counts = exact_keys(
        proof["counts"],
        {"internal_count", "node_count", "terminal_count", "tree_count",
         "unresolved_count"},
        f"static proof {pair} counts",
    )
    expected_counts = {
        "internal_count": entry["internal_count"],
        "node_count": entry["node_count"],
        "terminal_count": entry["terminal_count"],
        "tree_count": 4,
        "unresolved_count": entry["unresolved_count"],
    }
    require_exact(counts, expected_counts, f"static proof {pair} counts")
    trees = proof["trees"]
    if type(trees) is not list or len(trees) != 4:
        raise CompatibilityError(f"static proof {pair}: four trees required")
    maxima: list[int] = []
    for tree_id, tree in zip(TREE_IDS, trees, strict=True):
        maxima.append(_validate_tree(tree, tree_id))
        require_exact(
            tree["content_sha256"], entry["tree_content_sha256"][tree_id],
            f"static proof {pair} tree binding {tree_id}",
        )
    for key in ("node_count", "internal_count", "terminal_count", "unresolved_count"):
        if sum(tree[key] for tree in trees) != counts[key]:
            raise CompatibilityError(f"static proof {pair}: aggregate {key}")
    return max(maxima)


def validate_static_checker_shape(
    checker: dict[str, Any], proofs: list[dict[str, Any]], checker_source: FileImage
) -> None:
    exact_keys(checker, STATIC_CHECKER_KEYS, "static checker")
    static_common(checker, "static checker")
    if checker["passed"] is not True:
        raise CompatibilityError("static checker: pass gate")
    require_exact(checker["checker_sha256"], checker_source.sha256,
                  "static checker source hash")
    expected = {
        "proof_count": PUBLIC_FACTS["static_proof_count"],
        "node_count": PUBLIC_FACTS["static_nodes"],
        "internal_count": PUBLIC_FACTS["static_internal_nodes"],
        "terminal_count": PUBLIC_FACTS["static_terminal_nodes"],
        "unresolved_count": PUBLIC_FACTS["static_unresolved_nodes"],
        "independent_interval_checks": PUBLIC_FACTS["static_independent_checks"],
    }
    for key, value in expected.items():
        if exact_int(checker[key], f"static checker {key}") != value:
            raise CompatibilityError(f"static checker fact mismatch: {key}")
    replay = checker["proof_results"]
    if type(replay) is not list or len(replay) != 6:
        raise CompatibilityError("static checker: exactly six replay entries")
    interval_sum = 0
    for expected_pair, proof, item in zip(EXPECTED_PAIRS, proofs, replay, strict=True):
        exact_keys(item, STATIC_REPLAY_KEYS, "static checker proof replay")
        require_exact(
            [item["precision_bits"], item["slab_id"]], list(expected_pair),
            "static checker replay order",
        )
        for key in STATIC_ENTRY_KEYS - {"size_bytes"}:
            require_exact(item[key], proof[key], f"static checker replay {key}")
        interval_sum += exact_int(item["interval_checks"], "static interval checks", minimum=1)
        if type(item["angle_extrema"]) is not dict:
            raise CompatibilityError("static checker: angle extrema object required")
    if interval_sum != PUBLIC_FACTS["static_independent_checks"]:
        raise CompatibilityError("static checker: interval check sum")


def _validate_bound_project_roles(
    bindings: Any, roles: tuple[str, ...], snapshot: InputSnapshot, context: str
) -> None:
    if type(bindings) is not dict or set(bindings) != set(roles):
        raise CompatibilityError(f"{context}: exact role set required")
    for role in roles:
        canonical_relative(role, f"{context} role")
        image = snapshot.capture(ROOT / role, f"{context} payload {role}")
        require_exact(hash_string(bindings[role], f"{context} hash"), image.sha256,
                      f"{context} hash {role}")


def validate_branch_summary_shape(
    summary: dict[str, Any], snapshot: InputSnapshot
) -> tuple[list[dict[str, Any]], dict[tuple[int, str], dict[str, Any]]]:
    exact_keys(summary, BRANCH_SUMMARY_KEYS, "branch summary")
    branch_common(summary, "branch summary")
    require_exact(summary["representative_slabs"], list(REPRESENTATIVE_SLABS),
                  "branch slabs")
    require_exact(summary["precisions"], list(PRECISIONS), "branch precisions")
    if summary["pair_gate"] is not True or exact_int(summary["phase_grid"], "branch grid") != 64:
        raise CompatibilityError("branch summary: matrix gate")
    require_exact(summary["tube_radius"], "0.04", "branch tube radius")
    require_exact(summary["tube_radius_sq"], "0.0016", "branch tube radius square")
    finite_number(summary["elapsed_seconds"], "branch elapsed time")
    if type(summary["claim_boundary"]) is not str or type(summary["environment"]) is not dict:
        raise CompatibilityError("branch summary: boundary/environment schema")
    _validate_bound_project_roles(summary["input_hashes"], BRANCH_INPUT_ROLES,
                                  snapshot, "branch input bindings")
    records = summary["records"]
    if type(records) is not list or len(records) != 6:
        raise CompatibilityError("branch summary: exactly six records required")
    by_pair: dict[tuple[int, str], dict[str, Any]] = {}
    for expected_pair, record in zip(EXPECTED_PAIRS, records, strict=True):
        exact_keys(record, BRANCH_RECORD_KEYS, "branch record")
        pair = (
            exact_int(record["precision_bits"], "branch precision", minimum=1),
            record["slab_id"],
        )
        if type(pair[1]) is not str or pair != expected_pair:
            raise CompatibilityError(f"branch record order/identity: {pair}")
        expected_raw = f"raw/{pair[0]}/{pair[1]}.txt"
        expected_stderr = f"raw/{pair[0]}/{pair[1]}.stderr.txt"
        require_exact(canonical_relative(record["raw_file"], "branch raw path"),
                      expected_raw, "branch raw role")
        require_exact(canonical_relative(record["stderr_file"], "branch stderr path"),
                      expected_stderr, "branch stderr role")
        if not (
            record["status"] == BRANCH_IMPLEMENTATION
            and record["passed"] is True
            and record["input_echo_gate"] is True
            and record["all_segments_inside"] is True
            and record["phase_cover_complete"] is True
            and exact_int(record["returncode"], "branch return code") == 0
            and exact_int(record["taylor_order"], "branch Taylor order") == 24
        ):
            raise CompatibilityError(f"branch record gate: {pair}")
        require_exact(record["tolerance"], "1e-30" if pair[0] == 128 else "1e-60",
                      f"branch tolerance {pair}")
        exact_int(record["solution_piece_count"], "branch solution pieces", minimum=1)
        finite_number(record["wall_seconds"], "branch wall time")
        for name in ("argv", "epsilon", "omega_slow", "root_box", "terminal_state_box"):
            if type(record[name]) is not list:
                raise CompatibilityError(f"branch record {pair}: {name} list required")
        for name in ("maximum_rslow_sq_upper", "maximum_segment_rslow_sq_upper",
                     "minimum_margin_sq_lower"):
            if type(record[name]) is not str:
                raise CompatibilityError(f"branch record {pair}: {name} string required")
        by_pair[pair] = record
    return records, by_pair


def branch_common(payload: dict[str, Any], context: str) -> None:
    expected = {
        "protocol_id": BRANCH_PROTOCOL,
        "licensing": "NON_LICENSING",
        "prototype_status": BRANCH_IMPLEMENTATION,
    }
    for key, value in expected.items():
        if key not in payload or not exact_json_equal(payload[key], value):
            raise CompatibilityError(f"{context}: {key}")
    require_null_authority(payload, context)


def validate_branch_manifest_shape(
    manifest: dict[str, Any], snapshot: InputSnapshot
) -> dict[str, str]:
    exact_keys(manifest, BRANCH_MANIFEST_KEYS, "branch manifest")
    branch_common(manifest, "branch manifest")
    files = manifest["files"]
    if type(files) is not dict or len(files) != 26:
        raise CompatibilityError("branch manifest: exactly 26 roles required")
    expected_absolute = tuple(str(ROOT / role) for role in BRANCH_ROLE_PATHS)
    if set(files) != set(expected_absolute):
        raise CompatibilityError("branch manifest: exact 26-role set required")
    normalized: dict[str, str] = {}
    for role, absolute in zip(BRANCH_ROLE_PATHS, expected_absolute, strict=True):
        if canonical_relative(role, "branch manifest role") != role:
            raise CompatibilityError("branch manifest: role alias")
        image = snapshot.capture(Path(absolute), f"branch manifest payload {role}")
        digest = hash_string(files[absolute], "branch manifest digest")
        require_exact(digest, image.sha256, f"branch manifest digest {role}")
        normalized[role] = digest
    return normalized


def validate_branch_checker_shape(checker: dict[str, Any]) -> None:
    exact_keys(checker, BRANCH_CHECKER_KEYS, "branch checker")
    branch_common(checker, "branch checker")
    require_exact(checker["checker_status"], "PASS", "branch checker result")
    require_exact(checker["failures"], [], "branch checker failures")
    if exact_int(checker["raw_replay_count"], "branch raw replay count") != 6:
        raise CompatibilityError("branch checker: raw replay count")
    if exact_int(checker["manifest_file_count"], "branch manifest role count") != 26:
        raise CompatibilityError("branch checker: manifest role count")
    for name in ("maximum_rslow_sq_upper", "minimum_margin_sq_lower"):
        if type(checker[name]) is not str:
            raise CompatibilityError(f"branch checker: {name} string required")


def composite_common(payload: dict[str, Any], context: str) -> None:
    expected = {
        "schema_version": 1,
        "protocol_id": COMPOSITE_PROTOCOL,
        "artifact_status": ARTIFACT_STATUS,
        "scientific_licensing_enabled": False,
        "component_scope": "COMPOSITE_S0",
        "composite_s0_passed": True,
        "implementation_status": COMPOSITE_IMPLEMENTATION,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    for key, value in expected.items():
        if key not in payload or not exact_json_equal(payload[key], value):
            raise CompatibilityError(f"{context}: {key}")


def _control_descriptor(
    component: str, controls: dict[str, FileImage]
) -> list[dict[str, Any]]:
    names = {
        "summary.json": f"{component}_summary",
        "manifest.json": f"{component}_manifest",
        "independent_checker.json": f"{component}_checker",
    }
    return [
        {
            "component": component,
            "path": name,
            "sha256": controls[names[name]].sha256,
            "size_bytes": controls[names[name]].size,
        }
        for name in ("summary.json", "manifest.json", "independent_checker.json")
    ]


def expected_component_descriptors(controls: dict[str, FileImage]) -> dict[str, Any]:
    return {
        "static": {
            "protocol_id": STATIC_PROTOCOL,
            "component_scope": "STATIC_ONLY",
            "component_status": STATIC_IMPLEMENTATION,
            "composite_s0_passed": False,
            "scientific_licensing_enabled": False,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
            "checker_passed": True,
            "control_files": _control_descriptor("static", controls),
        },
        "branch": {
            "protocol_id": BRANCH_PROTOCOL,
            "component_scope": "BRANCH_TUBE_ONLY",
            "component_status": BRANCH_IMPLEMENTATION,
            "composite_s0_passed": False,
            "scientific_licensing_enabled": False,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
            "checker_passed": True,
            "control_files": _control_descriptor("branch", controls),
        },
    }


def expected_cells(
    static_by_pair: dict[tuple[int, str], dict[str, Any]],
    branch_by_pair: dict[tuple[int, str], dict[str, Any]],
    branch_roles: dict[str, str],
) -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []
    for pair in EXPECTED_PAIRS:
        proof = static_by_pair[pair]
        record = branch_by_pair[pair]
        raw_role = f"results/r401_val_l3_branch_tube_smoke/{record['raw_file']}"
        stderr_role = f"results/r401_val_l3_branch_tube_smoke/{record['stderr_file']}"
        if raw_role not in branch_roles or stderr_role not in branch_roles:
            raise CompatibilityError(f"composite cell: missing raw role {pair}")
        cells.append(
            {
                "precision_bits": pair[0],
                "slab_id": pair[1],
                "cell_passed": True,
                "static": {
                    "proof_path": proof["path"],
                    "proof_sha256": proof["sha256"],
                    "node_count": proof["node_count"],
                    "internal_count": proof["internal_count"],
                    "terminal_count": proof["terminal_count"],
                    "unresolved_count": proof["unresolved_count"],
                    "tree_content_sha256": proof["tree_content_sha256"],
                },
                "branch": {
                    "raw_file": record["raw_file"],
                    "raw_sha256": branch_roles[raw_role],
                    "stderr_file": record["stderr_file"],
                    "stderr_sha256": branch_roles[stderr_role],
                    "solution_piece_count": record["solution_piece_count"],
                    "maximum_rslow_sq_upper": record["maximum_rslow_sq_upper"],
                    "minimum_margin_sq_lower": record["minimum_margin_sq_lower"],
                },
            }
        )
    return cells


def validate_composite_summary_shape(
    summary: dict[str, Any], controls: dict[str, FileImage],
    static_by_pair: dict[tuple[int, str], dict[str, Any]],
    branch_by_pair: dict[tuple[int, str], dict[str, Any]],
    branch_roles: dict[str, str], snapshot: InputSnapshot,
) -> None:
    exact_keys(summary, COMPOSITE_SUMMARY_KEYS, "composite summary")
    composite_common(summary, "composite summary")
    require_exact(
        summary["matrix"],
        {"cell_count": 6, "precisions": [128, 256],
         "slabs": ["S000", "S025", "S050"]},
        "composite matrix",
    )
    if type(summary["claim_boundary"]) is not str:
        raise CompatibilityError("composite summary: claim boundary string required")
    components = exact_keys(summary["components"], {"static", "branch"},
                            "composite components")
    for component in ("static", "branch"):
        exact_keys(components[component], COMPONENT_DESCRIPTOR_KEYS,
                   f"composite {component} descriptor")
    require_exact(components, expected_component_descriptors(controls),
                  "composite component descriptors")
    require_exact(
        summary["cells"], expected_cells(static_by_pair, branch_by_pair, branch_roles),
        "composite six cells",
    )
    bindings = summary["source_bindings"]
    expected_roles = tuple(role for scope, role in COMPOSITE_FILE_ROLES if scope == "ROOT")
    _validate_bound_project_roles(bindings, expected_roles, snapshot,
                                  "composite source bindings")


def validate_composite_manifest_shape(
    manifest: dict[str, Any], controls: dict[str, FileImage], snapshot: InputSnapshot
) -> None:
    exact_keys(manifest, COMPOSITE_MANIFEST_KEYS, "composite manifest")
    composite_common(manifest, "composite manifest")
    files = manifest["files"]
    if type(files) is not list or len(files) != len(COMPOSITE_FILE_ROLES):
        raise CompatibilityError("composite manifest: exact file-role count")
    for expected_role, item in zip(COMPOSITE_FILE_ROLES, files, strict=True):
        exact_keys(item, {"scope", "path", "sha256", "size_bytes"},
                   "composite manifest file")
        role = (item["scope"], canonical_relative(item["path"], "composite role"))
        if role != expected_role:
            raise CompatibilityError(f"composite manifest role/order: {role}")
        target = COMPOSITE_DIR / role[1] if role[0] == "OUTPUT" else ROOT / role[1]
        image = snapshot.capture(target, f"composite manifest payload {role}")
        require_exact(hash_string(item["sha256"], "composite manifest hash"), image.sha256,
                      f"composite manifest hash {role}")
        if exact_int(item["size_bytes"], "composite manifest size") != image.size:
            raise CompatibilityError(f"composite manifest size {role}")
    component_files = manifest["component_files"]
    expected_controls = (
        expected_component_descriptors(controls)["static"]["control_files"]
        + expected_component_descriptors(controls)["branch"]["control_files"]
    )
    if type(component_files) is not list or len(component_files) != 6:
        raise CompatibilityError("composite manifest: six component roles required")
    for expected_role, item in zip(COMPOSITE_COMPONENT_ROLES, component_files, strict=True):
        exact_keys(item, {"component", "path", "sha256", "size_bytes"},
                   "composite component role")
        role = (item["component"], canonical_relative(item["path"],
                                                       "composite component path"))
        if role != expected_role:
            raise CompatibilityError(f"composite component role/order: {role}")
    require_exact(component_files, expected_controls, "composite component controls")


def validate_composite_checker_shape(
    checker: dict[str, Any], checker_source: FileImage
) -> None:
    exact_keys(checker, COMPOSITE_CHECKER_KEYS, "composite checker")
    composite_common(checker, "composite checker")
    require_exact(checker["checker_status"], "PASS", "composite checker result")
    require_exact(checker["failures"], [], "composite checker failures")
    require_exact(checker["checker_sha256"], checker_source.sha256,
                  "composite checker source hash")
    if exact_int(checker["cell_replay_count"], "composite cell count") != 6:
        raise CompatibilityError("composite checker: cell count")
    if exact_int(checker["manifest_binding_count"], "composite binding count") != 18:
        raise CompatibilityError("composite checker: binding count")


def validate_compatibility_output(payload: dict[str, Any]) -> None:
    """Validate the exact closed §8 compatibility result schema."""
    exact_keys(payload, COMPATIBILITY_OUTPUT_KEYS, "compatibility output")
    expected_scalars = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "S0_TO_A1_COMPATIBILITY_REPLAY",
        "artifact_status": "NON_LICENSING",
        "replay_status": "PASS_S0_COMPATIBILITY_REPLAY",
        "failures": [],
        "claim_boundary": COMPATIBILITY_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    for key, expected in expected_scalars.items():
        require_exact(payload[key], expected, f"compatibility output {key}")
    require_exact(
        payload["source_protocols"],
        {
            "static": STATIC_PROTOCOL,
            "branch": BRANCH_PROTOCOL,
            "composite": COMPOSITE_PROTOCOL,
        },
        "compatibility source protocols",
    )
    require_exact(
        payload["matrix"],
        {"precisions": [128, 256], "slabs": ["S000", "S025", "S050"],
         "cell_count": 6},
        "compatibility matrix",
    )
    require_exact(payload["static_facts"], STATIC_FACTS,
                  "compatibility static facts")
    require_exact(payload["branch_facts"], BRANCH_FACTS,
                  "compatibility branch facts")
    require_exact(payload["composite_facts"], COMPOSITE_FACTS,
                  "compatibility composite facts")
    require_exact(payload["control_hashes"], CONTROL_HASHES,
                  "compatibility control hashes")
    for role, digest in payload["control_hashes"].items():
        if role not in CONTROL_PATHS:
            raise CompatibilityError("compatibility control role")
        hash_string(digest, f"compatibility control hash {role}")

    role_sets = exact_keys(
        payload["role_sets"],
        {"static_proof_entries", "branch_manifest_roles",
         "composite_manifest_roles", "composite_component_roles"},
        "compatibility role sets",
    )
    static_entries = role_sets["static_proof_entries"]
    if type(static_entries) is not list or len(static_entries) != 6:
        raise CompatibilityError("compatibility role sets: six static entries")
    for expected_pair, entry in zip(EXPECTED_PAIRS, static_entries, strict=True):
        exact_keys(entry, STATIC_ENTRY_KEYS, "compatibility static role")
        require_exact([entry["precision_bits"], entry["slab_id"]],
                      list(expected_pair), "compatibility static role identity")
        require_exact(
            canonical_relative(entry["path"], "compatibility static path"),
            f"proof_{expected_pair[0]}_{expected_pair[1]}.json",
            "compatibility static path",
        )
        hash_string(entry["sha256"], "compatibility static hash")
        exact_int(entry["size_bytes"], "compatibility static size", minimum=1)
        nodes = exact_int(entry["node_count"], "compatibility static nodes", minimum=1)
        internal = exact_int(entry["internal_count"], "compatibility static internal")
        terminal = exact_int(entry["terminal_count"], "compatibility static terminal",
                             minimum=1)
        unresolved = exact_int(entry["unresolved_count"],
                               "compatibility static unresolved")
        if nodes != internal + terminal or unresolved != 0:
            raise CompatibilityError("compatibility static role counts")
        _tree_hashes(entry["tree_content_sha256"],
                     "compatibility static tree hashes")
    require_exact(role_sets["branch_manifest_roles"], list(BRANCH_ROLE_PATHS),
                  "compatibility branch roles")
    require_exact(
        role_sets["composite_manifest_roles"],
        [{"scope": scope, "path": path} for scope, path in COMPOSITE_FILE_ROLES],
        "compatibility composite roles",
    )
    require_exact(
        role_sets["composite_component_roles"],
        [{"component": component, "path": path}
         for component, path in COMPOSITE_COMPONENT_ROLES],
        "compatibility component roles",
    )
    bindings = exact_keys(
        payload["source_bindings"], set(COMPATIBILITY_SOURCE_ROLES),
        "compatibility source bindings",
    )
    for role in COMPATIBILITY_SOURCE_ROLES:
        canonical_relative(role, "compatibility source role")
        hash_string(bindings[role], f"compatibility source hash {role}")


def _capture_controls(snapshot: InputSnapshot) -> dict[str, FileImage]:
    controls: dict[str, FileImage] = {}
    if tuple(CONTROL_PATHS) != tuple(CONTROL_HASHES):
        raise CompatibilityError("internal control role mismatch")
    for role, path in CONTROL_PATHS.items():
        image = snapshot.capture(path, f"sealed S0 control {role}")
        require_exact(image.sha256, CONTROL_HASHES[role], f"sealed S0 hash {role}")
        controls[role] = image
    return controls


def build_compatibility_object() -> dict[str, Any]:
    snapshot = InputSnapshot()
    controls = _capture_controls(snapshot)
    static_summary = strict_json_bytes(controls["static_summary"].data, "static summary")
    static_manifest = strict_json_bytes(controls["static_manifest"].data, "static manifest")
    static_checker = strict_json_bytes(controls["static_checker"].data, "static checker")
    branch_summary = strict_json_bytes(controls["branch_summary"].data, "branch summary")
    branch_manifest = strict_json_bytes(controls["branch_manifest"].data, "branch manifest")
    branch_checker = strict_json_bytes(controls["branch_checker"].data, "branch checker")
    composite_summary = strict_json_bytes(controls["composite_summary"].data,
                                          "composite summary")
    composite_manifest = strict_json_bytes(controls["composite_manifest"].data,
                                           "composite manifest")
    composite_checker = strict_json_bytes(controls["composite_checker"].data,
                                          "composite checker")

    proofs, static_by_pair = validate_static_summary_shape(static_summary)
    validate_static_source_bindings(static_summary["source_bindings"], snapshot)
    validate_static_manifest_shape(static_manifest, proofs, controls["static_summary"])
    static_checker_source = snapshot.capture(
        ROOT / "scripts/check_r401_val_l3_phase_tube_independent.py",
        "static checker source",
    )
    maximum_depth = 0
    for entry in proofs:
        image = snapshot.capture(STATIC_DIR / entry["path"],
                                 f"static proof payload {entry['path']}")
        require_exact(image.sha256, entry["sha256"], "static proof byte hash")
        if image.size != entry["size_bytes"]:
            raise CompatibilityError("static proof byte size mismatch")
        proof = strict_json_bytes(image.data, f"static proof {entry['path']}")
        maximum_depth = max(
            maximum_depth,
            validate_static_proof(proof, entry, static_summary["source_bindings"]),
        )
    validate_static_checker_shape(static_checker, proofs, static_checker_source)

    _, branch_by_pair = validate_branch_summary_shape(branch_summary, snapshot)
    branch_roles = validate_branch_manifest_shape(branch_manifest, snapshot)
    validate_branch_checker_shape(branch_checker)
    for record in branch_summary["records"]:
        for key in ("raw_file", "stderr_file"):
            role = f"results/r401_val_l3_branch_tube_smoke/{record[key]}"
            if role not in branch_roles:
                raise CompatibilityError(f"branch record role missing: {role}")

    composite_checker_source = snapshot.capture(
        ROOT / "scripts/check_r401_val_l3_s0_composite_independent.py",
        "composite checker source",
    )
    validate_composite_summary_shape(
        composite_summary, controls, static_by_pair, branch_by_pair,
        branch_roles, snapshot,
    )
    validate_composite_manifest_shape(composite_manifest, controls, snapshot)
    validate_composite_checker_shape(composite_checker, composite_checker_source)

    observed_facts = {
        "static_proof_count": len(proofs),
        "static_nodes": static_summary["totals"]["node_count"],
        "static_internal_nodes": static_summary["totals"]["internal_count"],
        "static_terminal_nodes": static_summary["totals"]["terminal_count"],
        "static_unresolved_nodes": static_summary["totals"]["unresolved_count"],
        "static_independent_checks": static_checker["independent_interval_checks"],
        "static_maximum_depth": maximum_depth,
        "branch_raw_replay_count": branch_checker["raw_replay_count"],
        "branch_manifest_file_count": len(branch_roles),
        "composite_cell_count": composite_checker["cell_replay_count"],
        "composite_binding_count": composite_checker["manifest_binding_count"],
        "composite_failures": len(composite_checker["failures"]),
    }
    require_exact(observed_facts, PUBLIC_FACTS, "exact S0 public facts")

    design_image = snapshot.capture(DESIGN, "A1 prefreeze design")
    checker_contract_image = snapshot.capture(CHECKER_CONTRACT, "A1 checker contract")
    release_contract_image = snapshot.capture(RELEASE_CONTRACT, "A1 release contract")
    adapter_image = snapshot.capture(ADAPTER, "compatibility adapter source")
    snapshot.assert_unchanged()

    payload = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "S0_TO_A1_COMPATIBILITY_REPLAY",
        "artifact_status": "NON_LICENSING",
        "source_protocols": {
            "static": STATIC_PROTOCOL,
            "branch": BRANCH_PROTOCOL,
            "composite": COMPOSITE_PROTOCOL,
        },
        "matrix": {
            "precisions": list(PRECISIONS),
            "slabs": list(REPRESENTATIVE_SLABS),
            "cell_count": 6,
        },
        "static_facts": dict(STATIC_FACTS),
        "branch_facts": dict(BRANCH_FACTS),
        "composite_facts": dict(COMPOSITE_FACTS),
        "control_hashes": dict(CONTROL_HASHES),
        "role_sets": {
            "static_proof_entries": [dict(item) for item in proofs],
            "branch_manifest_roles": list(BRANCH_ROLE_PATHS),
            "composite_manifest_roles": [
                {"scope": scope, "path": path}
                for scope, path in COMPOSITE_FILE_ROLES
            ],
            "composite_component_roles": [
                {"component": component, "path": path}
                for component, path in COMPOSITE_COMPONENT_ROLES
            ],
        },
        "source_bindings": {
            COMPATIBILITY_SOURCE_ROLES[0]: adapter_image.sha256,
            COMPATIBILITY_SOURCE_ROLES[1]: design_image.sha256,
            COMPATIBILITY_SOURCE_ROLES[2]: checker_contract_image.sha256,
            COMPATIBILITY_SOURCE_ROLES[3]: release_contract_image.sha256,
        },
        "replay_status": "PASS_S0_COMPATIBILITY_REPLAY",
        "failures": [],
        "claim_boundary": COMPATIBILITY_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    validate_compatibility_output(payload)
    return payload


def _publication_file_identity(
    info: os.stat_result,
) -> tuple[int, int, int, int, int, int, int]:
    return (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )


def _absolute_argument(value: str, context: str) -> Path:
    if type(value) is not str or not value.startswith("/") or value.startswith("//"):
        raise CompatibilityError(f"{context}: exactly one POSIX root slash required")
    if (
        "\x00" in value
        or "\\" in value
        or "//" in value[1:]
        or value.endswith("/")
        or any(component in ("", ".", "..") for component in value[1:].split("/"))
    ):
        raise CompatibilityError(f"{context}: non-canonical path spelling")
    return _canonical_absolute(Path(value), context)


def _require_tmp_candidate(path: Path, context: str) -> None:
    if path.parts[:2] != ("/", "tmp") or len(path.parts) < 3:
        raise CompatibilityError(f"{context}: exact absolute /tmp file required")


def _open_publication_directory(
    path: Path, context: str,
) -> tuple[int, tuple[tuple[str, int, int, int], ...]]:
    """Open a lexical directory chain with no symlink traversal and pin it."""

    canonical = _canonical_absolute(path, context)
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor: int | None = None
    current = Path("/")
    signatures: list[tuple[str, int, int, int]] = []
    try:
        descriptor = os.open("/", flags)
        root_info = os.fstat(descriptor)
        if not stat.S_ISDIR(root_info.st_mode):
            raise CompatibilityError(f"{context}: filesystem root is not a directory")
        signatures.append(
            ("/", root_info.st_dev, root_info.st_ino, stat.S_IFMT(root_info.st_mode))
        )
        for component in canonical.parts[1:]:
            next_fd = os.open(
                component, flags | nofollow, dir_fd=descriptor
            )
            os.close(descriptor)
            descriptor = next_fd
            current /= component
            info = os.fstat(descriptor)
            if not stat.S_ISDIR(info.st_mode):
                raise CompatibilityError(
                    f"{context}: namespace component is not a directory: {current}"
                )
            signatures.append(
                (
                    os.fspath(current),
                    info.st_dev,
                    info.st_ino,
                    stat.S_IFMT(info.st_mode),
                )
            )
        return descriptor, tuple(signatures)
    except CompatibilityError:
        if descriptor is not None:
            os.close(descriptor)
        raise
    except OSError as error:
        if descriptor is not None:
            os.close(descriptor)
        raise CompatibilityError(
            f"{context}: unsafe directory chain: {canonical}: {error}"
        ) from error


def _publication_directory_chain(
    path: Path, context: str,
) -> tuple[tuple[str, int, int, int], ...]:
    descriptor, signatures = _open_publication_directory(path, context)
    os.close(descriptor)
    return signatures


def _replay_publication_directory(
    path: Path,
    pinned_fd: int,
    expected_chain: tuple[tuple[str, int, int, int], ...],
    context: str,
) -> None:
    pinned = os.fstat(pinned_fd)
    if (
        not stat.S_ISDIR(pinned.st_mode)
        or not expected_chain
        or (pinned.st_dev, pinned.st_ino)
        != (expected_chain[-1][1], expected_chain[-1][2])
        or _publication_directory_chain(path, context) != expected_chain
    ):
        raise CompatibilityError(f"{context}: directory namespace changed")


def _read_publication_file_at(
    parent_fd: int,
    name: str,
    context: str,
    *,
    expected_mode: int,
    fsync_file: bool = False,
) -> tuple[bytes, os.stat_result]:
    """Read one pinned, single-link regular file through an exact parent fd."""

    if type(name) is not str or not name or "/" in name or name in {".", ".."}:
        raise CompatibilityError(f"{context}: malformed basename")
    descriptor: int | None = None
    try:
        entry_before = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if not stat.S_ISREG(entry_before.st_mode):
            raise CompatibilityError(f"{context}: regular file required")
        if stat.S_IMODE(entry_before.st_mode) != expected_mode:
            raise CompatibilityError(
                f"{context}: exact mode {expected_mode:04o} required"
            )
        if entry_before.st_nlink != 1:
            raise CompatibilityError(f"{context}: hard-link alias rejected")
        if (
            entry_before.st_size <= 0
            or entry_before.st_size > PUBLICATION_MAX_CANDIDATE_BYTES
        ):
            raise CompatibilityError(
                f"{context}: size outside 1..{PUBLICATION_MAX_CANDIDATE_BYTES}"
            )
        descriptor = os.open(
            name,
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        before = os.fstat(descriptor)
        if (
            not stat.S_ISREG(before.st_mode)
            or stat.S_IMODE(before.st_mode) != expected_mode
            or before.st_nlink != 1
            or _publication_file_identity(before)
            != _publication_file_identity(entry_before)
        ):
            raise CompatibilityError(f"{context}: changed before pinned open")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(
                descriptor,
                min(1024 * 1024, PUBLICATION_MAX_CANDIDATE_BYTES - total + 1),
            )
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total > PUBLICATION_MAX_CANDIDATE_BYTES:
                raise CompatibilityError(f"{context}: pinned size cap exceeded")
        if fsync_file:
            os.fsync(descriptor)
        after = os.fstat(descriptor)
        entry_after = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        identity = _publication_file_identity(before)
        if (
            identity != _publication_file_identity(after)
            or identity != _publication_file_identity(entry_after)
            or (entry_after.st_dev, entry_after.st_ino)
            != (before.st_dev, before.st_ino)
        ):
            raise CompatibilityError(f"{context}: changed during pinned replay")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise CompatibilityError(f"{context}: short pinned read")
        return raw, before
    except CompatibilityError:
        raise
    except OSError as error:
        raise CompatibilityError(f"{context}: secure replay failed: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _replay_publication_candidate(
    *,
    path: Path,
    parent_fd: int,
    parent_chain: tuple[tuple[str, int, int, int], ...],
    expected_raw: bytes,
    expected_identity: tuple[int, int, int, int, int, int, int],
) -> None:
    _replay_publication_directory(
        path.parent, parent_fd, parent_chain, "compatibility candidate parent"
    )
    raw, info = _read_publication_file_at(
        parent_fd,
        path.name,
        "compatibility publication candidate",
        expected_mode=0o600,
    )
    if raw != expected_raw or _publication_file_identity(info) != expected_identity:
        raise CompatibilityError("compatibility publication candidate changed")


def _write_publication_bytes(descriptor: int, raw: bytes) -> None:
    view = memoryview(raw)
    while view:
        written = os.write(descriptor, view)
        if written <= 0:
            raise OSError("short compatibility publication staging write")
        view = view[written:]


def _publication_stage_basename() -> str:
    name = PUBLICATION_STAGE_PREFIX + os.urandom(16).hex()
    suffix = name.removeprefix(PUBLICATION_STAGE_PREFIX)
    if (
        len(suffix) != 32
        or any(character not in "0123456789abcdef" for character in suffix)
    ):
        raise CompatibilityError("compatibility publication stage name malformed")
    return name


def _publication_fault_hook(phase: str) -> None:
    """No-op production hook; tests use it to model exact crash boundaries."""

    if phase not in PUBLICATION_HOOK_PHASES:
        raise CompatibilityError(f"unknown compatibility publication phase: {phase}")


def _rename_publication_noreplace(
    parent_fd: int, source_name: str, destination_name: str,
) -> None:
    if sys.platform != "linux":
        raise CompatibilityError("Linux renameat2(RENAME_NOREPLACE) is required")
    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = getattr(libc, "renameat2", None)
    if renameat2 is None:
        raise CompatibilityError("renameat2(RENAME_NOREPLACE) is unavailable")
    renameat2.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    ctypes.set_errno(0)
    result = renameat2(
        parent_fd,
        os.fsencode(source_name),
        parent_fd,
        os.fsencode(destination_name),
        1,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in {errno.EEXIST, errno.ENOTEMPTY}:
        raise CompatibilityError(
            "canonical compatibility destination already exists or collided"
        )
    raise CompatibilityError(
        "compatibility renameat2(RENAME_NOREPLACE) failed: "
        f"{os.strerror(error_number)}"
    )


def _cleanup_publication_stage(
    parent_fd: int, name: str, owned_inode: tuple[int, int],
) -> None:
    try:
        entry = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    except OSError as error:
        raise CompatibilityError(
            f"compatibility staging cleanup stat failed: {error}"
        ) from error
    if (entry.st_dev, entry.st_ino) != owned_inode:
        raise CompatibilityError(
            "compatibility publication refused to unlink a replaced staging inode"
        )
    try:
        os.unlink(name, dir_fd=parent_fd)
        os.fsync(parent_fd)
    except OSError as error:
        raise CompatibilityError(
            f"compatibility staging cleanup failed: {error}"
        ) from error


def _canonical_output_for_root(root: Path) -> Path:
    return _canonical_absolute(
        root / ROLE13_RELATIVE_PATH, "canonical compatibility destination"
    )


def _validate_candidate_bytes(raw: bytes) -> dict[str, Any]:
    payload = strict_json_bytes(raw, "compatibility publication candidate")
    if raw != canonical_json_bytes(payload):
        raise CompatibilityError(
            "compatibility publication candidate is not CJ_COMPACT_V1"
        )
    validate_compatibility_output(payload)
    return payload


def _live_compatibility_bytes(root: Path) -> bytes:
    live_root = _canonical_absolute(ROOT, "live Paper02 root")
    if root != live_root:
        raise CompatibilityError(
            "compatibility publication authority root is not live Paper02 root"
        )
    payload = build_compatibility_object()
    validate_compatibility_output(payload)
    encoded = canonical_json_bytes(payload)
    if _validate_candidate_bytes(encoded) != payload:
        raise CompatibilityError("live compatibility object failed exact replay")
    return encoded


def _secure_exclusive_write(path: Path, data: bytes) -> None:
    """Capture exact candidate bytes at a new 0600 /tmp path."""

    path = _canonical_absolute(path, "temporary output")
    _require_tmp_candidate(path, "temporary output")
    if path == _canonical_output_for_root(_canonical_absolute(ROOT, "Paper02 root")):
        raise CompatibilityError("canonical compatibility replay is reserved")
    try:
        path.relative_to(ROOT)
    except ValueError:
        pass
    else:
        raise CompatibilityError("temporary output must be outside the project tree")
    if not data or len(data) > PUBLICATION_MAX_CANDIDATE_BYTES:
        raise CompatibilityError("temporary compatibility candidate size is invalid")

    parent_fd: int | None = None
    output_fd: int | None = None
    output_inode: tuple[int, int] | None = None
    committed = False
    try:
        parent_fd, parent_chain = _open_publication_directory(
            path.parent, "temporary output parent"
        )
        _replay_publication_directory(
            path.parent, parent_fd, parent_chain, "temporary output parent"
        )
        output_fd = os.open(
            path.name,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0),
            0o600,
            dir_fd=parent_fd,
        )
        output_info = os.fstat(output_fd)
        if (
            not stat.S_ISREG(output_info.st_mode)
            or output_info.st_nlink != 1
            or stat.S_IMODE(output_info.st_mode) != 0o600
        ):
            raise CompatibilityError("temporary output inode contract mismatch")
        output_inode = (output_info.st_dev, output_info.st_ino)
        _write_publication_bytes(output_fd, data)
        os.fsync(output_fd)
        captured_raw, captured_info = _read_publication_file_at(
            parent_fd,
            path.name,
            "temporary compatibility candidate",
            expected_mode=0o600,
            fsync_file=True,
        )
        if (
            captured_raw != data
            or (captured_info.st_dev, captured_info.st_ino) != output_inode
        ):
            raise CompatibilityError("temporary output publication mismatch")
        os.fsync(parent_fd)
        _replay_publication_directory(
            path.parent, parent_fd, parent_chain, "temporary output parent"
        )
        committed = True
    except CompatibilityError:
        raise
    except OSError as error:
        raise CompatibilityError(f"exclusive temporary output failed: {error}") from error
    finally:
        cleanup_error: BaseException | None = None
        if (
            parent_fd is not None
            and output_inode is not None
            and not committed
        ):
            try:
                _cleanup_publication_stage(parent_fd, path.name, output_inode)
            except BaseException as error:
                cleanup_error = error
        if output_fd is not None:
            os.close(output_fd)
        if parent_fd is not None:
            os.close(parent_fd)
        if cleanup_error is not None:
            raise cleanup_error


def capture_compatibility_candidate(output_value: str) -> dict[str, Any]:
    output = _absolute_argument(output_value, "temporary output argument")
    _require_tmp_candidate(output, "temporary output argument")
    payload = build_compatibility_object()
    validate_compatibility_output(payload)
    encoded = canonical_json_bytes(payload)
    _validate_candidate_bytes(encoded)
    _secure_exclusive_write(output, encoded)
    captured = _secure_read(output, "captured compatibility candidate")
    if (
        captured.data != encoded
        or stat.S_IMODE(captured.metadata[2]) != 0o600
        or captured.metadata[3] != 1
    ):
        raise CompatibilityError("captured compatibility candidate terminal mismatch")
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "TEMP_S0_COMPATIBILITY_CANDIDATE_RECEIPT",
        "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
        "authority": "NON_AUTHORITATIVE_CAPTURE_ONLY",
        "candidate_path": os.fspath(output),
        "candidate_sha256": hashlib.sha256(encoded).hexdigest(),
        "size_bytes": len(encoded),
        "mode": "0600",
        "nlink": 1,
        "serializer": "CJ_COMPACT_V1",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def publish_compatibility_replay(
    *, candidate_value: str, expected_sha256: str, authority_root_value: str,
) -> dict[str, Any]:
    """Publish canonical role 13 once without evaluator or freeze authority."""

    expected_sha256 = hash_string(
        expected_sha256, "expected compatibility candidate SHA-256"
    )
    root = _absolute_argument(authority_root_value, "publication authority root")
    live_root = _canonical_absolute(ROOT, "live Paper02 root")
    if root != live_root:
        raise CompatibilityError(
            "publication authority root must equal exact live Paper02 root"
        )
    candidate_path = _absolute_argument(
        candidate_value, "compatibility publication candidate"
    )
    _require_tmp_candidate(candidate_path, "compatibility publication candidate")
    destination = _canonical_output_for_root(root)
    if candidate_path == destination:
        raise CompatibilityError("candidate aliases canonical role 13")

    candidate_parent_fd: int | None = None
    root_fd: int | None = None
    publication_parent_fd: int | None = None
    stage_fd: int | None = None
    stage_name: str | None = None
    stage_inode: tuple[int, int] | None = None
    renamed = False
    preserve_crash_residue = False
    try:
        candidate_parent_fd, candidate_parent_chain = _open_publication_directory(
            candidate_path.parent, "compatibility candidate parent"
        )
        candidate_raw, candidate_info = _read_publication_file_at(
            candidate_parent_fd,
            candidate_path.name,
            "compatibility publication candidate",
            expected_mode=0o600,
        )
        candidate_identity = _publication_file_identity(candidate_info)
        if hashlib.sha256(candidate_raw).hexdigest() != expected_sha256:
            raise CompatibilityError(
                "compatibility candidate SHA-256 differs from expected intent"
            )
        _validate_candidate_bytes(candidate_raw)

        root_fd, root_chain = _open_publication_directory(
            root, "publication authority root"
        )
        publication_parent_fd, publication_parent_chain = (
            _open_publication_directory(
                destination.parent, "compatibility publication parent"
            )
        )
        _replay_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "compatibility publication parent",
        )
        try:
            os.stat(
                destination.name,
                dir_fd=publication_parent_fd,
                follow_symlinks=False,
            )
        except FileNotFoundError:
            pass
        else:
            raise CompatibilityError(
                "canonical compatibility destination already exists"
            )

        live_raw = _live_compatibility_bytes(root)
        if candidate_raw != live_raw:
            raise CompatibilityError(
                "compatibility candidate is stale relative to live replay bytes"
            )
        _replay_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )

        for _attempt in range(32):
            proposed_name = _publication_stage_basename()
            suffix = proposed_name.removeprefix(PUBLICATION_STAGE_PREFIX)
            if (
                not proposed_name.startswith(PUBLICATION_STAGE_PREFIX)
                or len(suffix) != 32
                or any(character not in "0123456789abcdef" for character in suffix)
            ):
                raise CompatibilityError(
                    "compatibility publication staging basename violates contract"
                )
            try:
                stage_fd = os.open(
                    proposed_name,
                    os.O_WRONLY
                    | os.O_CREAT
                    | os.O_EXCL
                    | getattr(os, "O_NOFOLLOW", 0),
                    0o600,
                    dir_fd=publication_parent_fd,
                )
            except FileExistsError:
                continue
            except OSError as error:
                raise CompatibilityError(
                    f"compatibility publication staging create failed: {error}"
                ) from error
            stage_name = proposed_name
            initial_stage = os.fstat(stage_fd)
            if not stat.S_ISREG(initial_stage.st_mode) or initial_stage.st_nlink != 1:
                raise CompatibilityError(
                    "compatibility staging inode is not exclusive regular file"
                )
            stage_inode = (initial_stage.st_dev, initial_stage.st_ino)
            break
        else:
            raise CompatibilityError(
                "compatibility publication exhausted collision-safe stage names"
            )
        assert stage_fd is not None and stage_name is not None and stage_inode is not None
        os.fchmod(stage_fd, 0o644)
        _write_publication_bytes(stage_fd, candidate_raw)
        try:
            _publication_fault_hook("AFTER_STAGE_WRITE")
        except SyntheticCompatibilityPublicationCrash:
            preserve_crash_residue = True
            raise
        os.fsync(stage_fd)
        try:
            _publication_fault_hook("AFTER_STAGE_FILE_FSYNC")
        except SyntheticCompatibilityPublicationCrash:
            preserve_crash_residue = True
            raise
        staged_raw, staged_info = _read_publication_file_at(
            publication_parent_fd,
            stage_name,
            "compatibility publication staging file",
            expected_mode=0o644,
            fsync_file=True,
        )
        if (
            staged_raw != candidate_raw
            or (staged_info.st_dev, staged_info.st_ino) != stage_inode
        ):
            raise CompatibilityError("compatibility staging replay mismatch")
        os.fsync(publication_parent_fd)
        try:
            _publication_fault_hook("AFTER_STAGING_PARENT_FSYNC")
        except SyntheticCompatibilityPublicationCrash:
            preserve_crash_residue = True
            raise

        try:
            _publication_fault_hook("BEFORE_TERMINAL_REPLAY")
        except SyntheticCompatibilityPublicationCrash:
            preserve_crash_residue = True
            raise
        _replay_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )
        _replay_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "compatibility publication parent",
        )
        terminal_live_raw = _live_compatibility_bytes(root)
        if terminal_live_raw != candidate_raw or terminal_live_raw != live_raw:
            raise CompatibilityError(
                "live compatibility replay changed before publication"
            )
        staged_raw, staged_info = _read_publication_file_at(
            publication_parent_fd,
            stage_name,
            "compatibility publication staging file",
            expected_mode=0o644,
        )
        if (
            staged_raw != candidate_raw
            or (staged_info.st_dev, staged_info.st_ino) != stage_inode
        ):
            raise CompatibilityError("compatibility staging inode changed")

        try:
            _publication_fault_hook("BEFORE_RENAME")
        except SyntheticCompatibilityPublicationCrash:
            preserve_crash_residue = True
            raise
        _replay_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )
        _replay_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "compatibility publication parent",
        )
        if _live_compatibility_bytes(root) != candidate_raw:
            raise CompatibilityError(
                "live compatibility replay changed at publication boundary"
            )
        staged_raw, staged_info = _read_publication_file_at(
            publication_parent_fd,
            stage_name,
            "compatibility publication staging file",
            expected_mode=0o644,
        )
        if (
            staged_raw != candidate_raw
            or (staged_info.st_dev, staged_info.st_ino) != stage_inode
        ):
            raise CompatibilityError(
                "compatibility staging changed at publication boundary"
            )
        _rename_publication_noreplace(
            publication_parent_fd, stage_name, destination.name
        )
        renamed = True
        _publication_fault_hook("AFTER_RENAME")

        try:
            os.stat(stage_name, dir_fd=publication_parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise CompatibilityError(
                "compatibility rename left staging entry present"
            )
        open_stage = os.fstat(stage_fd)
        if (
            (open_stage.st_dev, open_stage.st_ino) != stage_inode
            or not stat.S_ISREG(open_stage.st_mode)
            or stat.S_IMODE(open_stage.st_mode) != 0o644
            or open_stage.st_nlink != 1
            or open_stage.st_size != len(candidate_raw)
        ):
            raise CompatibilityError(
                "open compatibility staging inode changed after rename"
            )
        published_raw, published_info = _read_publication_file_at(
            publication_parent_fd,
            destination.name,
            "canonical S0 compatibility replay",
            expected_mode=0o644,
            fsync_file=True,
        )
        if (
            published_raw != candidate_raw
            or hashlib.sha256(published_raw).hexdigest() != expected_sha256
            or (published_info.st_dev, published_info.st_ino) != stage_inode
        ):
            raise CompatibilityError(
                "canonical compatibility post-publication replay mismatch"
            )
        _publication_fault_hook("AFTER_DESTINATION_FSYNC")
        os.fsync(publication_parent_fd)
        _publication_fault_hook("AFTER_PUBLICATION_PARENT_FSYNC")

        _replay_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "compatibility publication parent",
        )
        lexical = _secure_read(destination, "canonical compatibility lexical replay")
        if (
            lexical.data != candidate_raw
            or (lexical.metadata[0], lexical.metadata[1]) != stage_inode
            or stat.S_IMODE(lexical.metadata[2]) != 0o644
            or lexical.metadata[3] != 1
        ):
            raise CompatibilityError(
                "canonical compatibility lexical terminal replay mismatch"
            )
        _replay_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )
        if _live_compatibility_bytes(root) != candidate_raw:
            raise CompatibilityError(
                "live compatibility replay changed after publication"
            )
        _publication_fault_hook("AFTER_POSTPUBLICATION_REPLAY")

        receipt = {
            "schema_version": SCHEMA_VERSION,
            "protocol_id": PROTOCOL_ID,
            "artifact_role": "S0_COMPATIBILITY_PUBLICATION_RECEIPT",
            "artifact_status": "PUBLISHED_WRITE_ONCE_NON_LICENSING",
            "authority": "ROLE23_ADAPTER_PUBLICATION_ONLY",
            "candidate_path": os.fspath(candidate_path),
            "canonical_path": os.fspath(destination),
            "compatibility_sha256": expected_sha256,
            "size_bytes": len(candidate_raw),
            "mode": "0644",
            "nlink": 1,
            "serializer": "CJ_COMPACT_V1",
            "publication_method": PUBLICATION_METHOD,
            "independent_verification_performed": False,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        canonical_json_bytes(receipt)
        return receipt
    finally:
        cleanup_error: BaseException | None = None
        if (
            publication_parent_fd is not None
            and stage_name is not None
            and stage_inode is not None
            and not renamed
            and not preserve_crash_residue
        ):
            try:
                _cleanup_publication_stage(
                    publication_parent_fd, stage_name, stage_inode
                )
            except BaseException as error:
                cleanup_error = error
        close_error: OSError | None = None
        for descriptor in (
            stage_fd,
            publication_parent_fd,
            root_fd,
            candidate_parent_fd,
        ):
            if descriptor is None:
                continue
            try:
                os.close(descriptor)
            except OSError as error:
                if close_error is None:
                    close_error = error
        if cleanup_error is not None:
            raise cleanup_error
        if close_error is not None:
            raise CompatibilityError(
                f"compatibility publication descriptor close failed: {close_error}"
            ) from close_error


def _output_argument(value: str) -> Path:
    try:
        path = _absolute_argument(value, "temporary output argument")
        _require_tmp_candidate(path, "temporary output argument")
        return path
    except CompatibilityError as error:
        raise argparse.ArgumentTypeError(str(error)) from error


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-s0-compatibility", action="store_true")
    parser.add_argument("--publish-s0-compatibility", action="store_true")
    parser.add_argument(
        "--output", type=_output_argument, default=None,
        help="new exact 0600 /tmp candidate path (capture only)",
    )
    parser.add_argument("--candidate")
    parser.add_argument("--expected-sha256")
    parser.add_argument("--authority-root")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.capture_s0_compatibility == arguments.publish_s0_compatibility:
            raise CompatibilityError(
                "exactly one of capture or publish compatibility mode is required"
            )
        if arguments.capture_s0_compatibility:
            if (
                arguments.output is None
                or arguments.candidate is not None
                or arguments.expected_sha256 is not None
                or arguments.authority_root is not None
            ):
                raise CompatibilityError(
                    "compatibility capture requires only --output"
                )
            receipt = capture_compatibility_candidate(os.fspath(arguments.output))
        else:
            if (
                arguments.output is not None
                or arguments.candidate is None
                or arguments.expected_sha256 is None
                or arguments.authority_root is None
            ):
                raise CompatibilityError(
                    "compatibility publication requires --candidate, "
                    "--expected-sha256, and --authority-root, without --output"
                )
            receipt = publish_compatibility_replay(
                candidate_value=arguments.candidate,
                expected_sha256=arguments.expected_sha256,
                authority_root_value=arguments.authority_root,
            )
        sys.stdout.buffer.write(canonical_json_bytes(receipt))
        return 0
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
