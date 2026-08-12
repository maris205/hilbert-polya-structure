#!/usr/bin/env python3
"""Build the compact NON_LICENSING R401-VAL-L3 S0 composite archive.

This packager does not evaluate either mathematical component.  It accepts
only the independently checked static phase component and CAPD branch-tube
component, binds their control files byte-for-byte, and constructs the exact
six-cell cross-component matrix.  Only this composite layer may emit the
implementation-smoke token; it has no theorem or final-program authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGER = Path(__file__).resolve()
COMPOSITE_CHECKER = ROOT / "scripts/check_r401_val_l3_s0_composite_independent.py"
STATIC_DIR_DEFAULT = ROOT / "results/r401_val_l3_phase_tube_smoke"
BRANCH_DIR_DEFAULT = ROOT / "results/r401_val_l3_branch_tube_smoke"

STATIC_RUNNER = ROOT / "scripts/run_r401_val_l3_phase_tube_smoke.py"
STATIC_CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_phase_tube_independent.py"
BRANCH_CPP = ROOT / "validated/capd_r401_phase_branch_tube_mp.cpp"
BRANCH_RUNNER = ROOT / "scripts/run_r401_val_l3_branch_tube_smoke.py"
BRANCH_CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_branch_tube_smoke_independent.py"
BRANCH_DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"
L1_DIR = ROOT / "results/r401_val_l1_branch"
L1_CONTROL_FILES = (
    L1_DIR / "summary.json",
    L1_DIR / "manifest.json",
    L1_DIR / "independent_checker.json",
    L1_DIR / "POSTCHECK_STATUS.json",
    L1_DIR / "RELEASE_PROVENANCE.json",
)
DRAFT_DOCS = (
    ROOT / "research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md",
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md",
    ROOT / "research/route_a_wave_trace/refine-logs/A416_EXPERIMENT_PLAN.md",
)
SOURCE_FILES = (
    PACKAGER,
    COMPOSITE_CHECKER,
    STATIC_RUNNER,
    STATIC_CHECKER_SOURCE,
    BRANCH_CPP,
    BRANCH_RUNNER,
    BRANCH_CHECKER_SOURCE,
    *DRAFT_DOCS,
)

SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-S0-COMPOSITE-DRAFT"
ARTIFACT_STATUS = "DRAFT_NON_LICENSING"
IMPLEMENTATION_STATUS = "PASS_IMPLEMENTATION_SMOKE"
COMPONENT_SCOPE = "COMPOSITE_S0"
STATIC_PROTOCOL = "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT"
STATIC_STATUS = "PASS_STATIC_COMPONENT_SMOKE"
BRANCH_PROTOCOL = "R401-VAL-L3-BT-S0"
BRANCH_STATUS = "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
PRECISIONS = (128, 256)
EXPECTED_PAIRS = tuple(
    (bits, slab) for bits in PRECISIONS for slab in REPRESENTATIVE_SLABS
)
CONTROL_NAMES = ("summary.json", "manifest.json", "independent_checker.json")
HASH_PATTERN = re.compile(r"[0-9a-f]{64}")

STATIC_SUMMARY_KEYS = {
    "artifact_status",
    "claim_boundary",
    "component_scope",
    "composite_s0_passed",
    "final_status",
    "implementation_status",
    "matrix",
    "proofs",
    "protocol_id",
    "schema_version",
    "scientific_licensing_enabled",
    "source_bindings",
    "totals",
}
STATIC_MANIFEST_KEYS = {
    "artifact_status",
    "component_scope",
    "composite_s0_passed",
    "files",
    "final_status",
    "implementation_status",
    "protocol_id",
    "schema_version",
    "scientific_licensing_enabled",
}
STATIC_CHECKER_KEYS = {
    "artifact_status",
    "checker_sha256",
    "claim_boundary",
    "component_scope",
    "composite_s0_passed",
    "final_status",
    "implementation_status",
    "independent_interval_checks",
    "internal_count",
    "node_count",
    "passed",
    "proof_count",
    "proof_results",
    "protocol_id",
    "schema_version",
    "scientific_licensing_enabled",
    "terminal_count",
    "unresolved_count",
}
STATIC_PROOF_ENTRY_KEYS = {
    "internal_count",
    "node_count",
    "path",
    "precision_bits",
    "sha256",
    "size_bytes",
    "slab_id",
    "terminal_count",
    "tree_content_sha256",
    "unresolved_count",
}
STATIC_CHECKER_PROOF_KEYS = (STATIC_PROOF_ENTRY_KEYS - {"size_bytes"}) | {
    "angle_extrema",
    "interval_checks",
}

BRANCH_SUMMARY_KEYS = {
    "claim_boundary",
    "elapsed_seconds",
    "environment",
    "final_status",
    "input_hashes",
    "licensing",
    "milestone_status",
    "pair_gate",
    "phase_grid",
    "precisions",
    "protocol_id",
    "prototype_status",
    "records",
    "representative_slabs",
    "theorem_status",
    "tube_radius",
    "tube_radius_sq",
}
BRANCH_MANIFEST_KEYS = {
    "files",
    "final_status",
    "licensing",
    "milestone_status",
    "protocol_id",
    "prototype_status",
    "theorem_status",
}
BRANCH_CHECKER_KEYS = {
    "checker_status",
    "failures",
    "final_status",
    "licensing",
    "manifest_file_count",
    "maximum_rslow_sq_upper",
    "milestone_status",
    "minimum_margin_sq_lower",
    "protocol_id",
    "prototype_status",
    "raw_replay_count",
    "theorem_status",
}
BRANCH_RECORD_KEYS = {
    "all_segments_inside",
    "argv",
    "epsilon",
    "input_echo_gate",
    "maximum_rslow_sq_upper",
    "maximum_segment_rslow_sq_upper",
    "minimum_margin_sq_lower",
    "omega_slow",
    "passed",
    "phase_cover_complete",
    "precision_bits",
    "raw_file",
    "returncode",
    "root_box",
    "slab_id",
    "solution_piece_count",
    "status",
    "stderr_file",
    "taylor_order",
    "terminal_state_box",
    "tolerance",
    "wall_seconds",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def finite_json_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError(f"non-finite JSON float: {value}")
    return parsed


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    for key, value in pairs:
        if key in payload:
            raise ValueError(f"duplicate JSON key: {key}")
        payload[key] = value
    return payload


def strict_json(path: Path) -> dict[str, Any]:
    reject_symlink(path, "JSON control file")
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_object,
        parse_constant=reject_constant,
        parse_float=finite_json_float,
    )
    if type(value) is not dict:
        raise TypeError(f"top-level JSON object required: {path}")
    return value


def exact_keys(payload: dict[str, Any], expected: set[str], context: str) -> None:
    actual = set(payload)
    if actual != expected:
        raise ValueError(
            f"{context} keys: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def exact_json_equal(left: Any, right: Any) -> bool:
    """Compare JSON values with recursive type identity."""
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            exact_json_equal(left[key], right[key]) for key in left
        )
    if type(left) is list:
        return len(left) == len(right) and all(
            exact_json_equal(lvalue, rvalue)
            for lvalue, rvalue in zip(left, right, strict=True)
        )
    return left == right


def require_exact_json(left: Any, right: Any, context: str) -> None:
    if not exact_json_equal(left, right):
        raise ValueError(f"{context} is not exact JSON")


def exact_int(value: Any, context: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise TypeError(f"{context} must be an integer >= {minimum}")
    return value


def finite_number(value: Any, context: str) -> float | int:
    if type(value) not in (int, float) or not math.isfinite(value):
        raise TypeError(f"{context} must be a finite JSON number")
    return value


def hash_string(value: Any, context: str) -> str:
    if type(value) is not str or HASH_PATTERN.fullmatch(value) is None:
        raise TypeError(f"{context} must be a lowercase SHA-256")
    return value


def reject_symlink(path: Path, context: str) -> None:
    if path.is_symlink():
        raise ValueError(f"{context} must not be a symlink: {path}")


def secure_file(path: Path, context: str) -> None:
    reject_symlink(path, context)
    if not path.is_file():
        raise FileNotFoundError(f"{context} missing: {path}")


def secure_component_file(directory: Path, relative: str, context: str) -> Path:
    if Path(relative).is_absolute() or Path(relative).parts != (relative,):
        raise ValueError(f"{context} is not a canonical component basename: {relative}")
    reject_symlink(directory, context)
    path = directory / relative
    reject_symlink(path, context)
    if path.parent.resolve() != directory.resolve() or not path.is_file():
        raise ValueError(f"{context} escapes or is missing: {relative}")
    return path


def require_non_authoritative(payload: dict[str, Any], context: str) -> None:
    if payload.get("final_status", object()) is not None:
        raise ValueError(f"{context} final_status is not null")
    for key in ("milestone_status", "theorem_status"):
        if key in payload and payload[key] is not None:
            raise ValueError(f"{context} assigned {key}")


def require_static_common(payload: dict[str, Any], context: str) -> None:
    if not exact_json_equal(payload.get("schema_version"), SCHEMA_VERSION):
        raise ValueError(f"{context} schema version")
    if not exact_json_equal(payload.get("protocol_id"), STATIC_PROTOCOL):
        raise ValueError(f"{context} protocol")
    if not exact_json_equal(payload.get("artifact_status"), ARTIFACT_STATUS):
        raise ValueError(f"{context} artifact status")
    if not exact_json_equal(payload.get("implementation_status"), STATIC_STATUS):
        raise ValueError(f"{context} implementation status")
    if not exact_json_equal(payload.get("component_scope"), "STATIC_ONLY"):
        raise ValueError(f"{context} component scope")
    if payload.get("composite_s0_passed") is not False:
        raise ValueError(f"{context} composite flag")
    if payload.get("scientific_licensing_enabled") is not False:
        raise ValueError(f"{context} scientific licensing")
    require_non_authoritative(payload, context)


def tree_hashes(value: Any, context: str) -> dict[str, str]:
    if type(value) is not dict or set(value) != {
        "ANGLE",
        "SECTION_LOW",
        "SECTION_WINDOW",
        "SECTION_HIGH",
    }:
        raise TypeError(f"{context} has the wrong tree hash set")
    return {key: hash_string(item, f"{context}.{key}") for key, item in value.items()}


def validate_static_component(directory: Path) -> tuple[dict[str, Any], dict[tuple[int, str], dict[str, Any]]]:
    summary_path = secure_component_file(directory, "summary.json", "static summary")
    manifest_path = secure_component_file(directory, "manifest.json", "static manifest")
    checker_path = secure_component_file(
        directory, "independent_checker.json", "static checker result"
    )
    summary = strict_json(summary_path)
    manifest = strict_json(manifest_path)
    checker = strict_json(checker_path)
    exact_keys(summary, STATIC_SUMMARY_KEYS, "static summary")
    exact_keys(manifest, STATIC_MANIFEST_KEYS, "static manifest")
    exact_keys(checker, STATIC_CHECKER_KEYS, "static checker")
    for payload, context in (
        (summary, "static summary"),
        (manifest, "static manifest"),
        (checker, "static checker"),
    ):
        require_static_common(payload, context)

    matrix = summary["matrix"]
    require_exact_json(matrix, {
        "precisions": list(PRECISIONS),
        "proof_count": 6,
        "slabs": list(REPRESENTATIVE_SLABS),
    }, "static 3x2 matrix")
    proofs = summary["proofs"]
    if type(proofs) is not list or len(proofs) != 6:
        raise TypeError("static proof list must contain six entries")
    proof_by_pair: dict[tuple[int, str], dict[str, Any]] = {}
    expected_paths = {f"proof_{bits}_{slab}.json" for bits, slab in EXPECTED_PAIRS}
    for entry in proofs:
        if type(entry) is not dict:
            raise TypeError("static proof entry must be an object")
        exact_keys(entry, STATIC_PROOF_ENTRY_KEYS, "static proof entry")
        bits = exact_int(entry["precision_bits"], "static precision", minimum=1)
        slab = entry["slab_id"]
        if type(slab) is not str:
            raise TypeError("static slab must be a string")
        pair = (bits, slab)
        if pair not in EXPECTED_PAIRS or pair in proof_by_pair:
            raise ValueError(f"static unexpected or duplicate pair: {pair}")
        expected_path = f"proof_{bits}_{slab}.json"
        if entry["path"] != expected_path:
            raise ValueError(f"static proof path mismatch: {pair}")
        target = secure_component_file(directory, expected_path, "static proof")
        if hash_string(entry["sha256"], "static proof hash") != sha256(target):
            raise ValueError(f"static proof hash mismatch: {pair}")
        if exact_int(entry["size_bytes"], "static proof size") != target.stat().st_size:
            raise ValueError(f"static proof size mismatch: {pair}")
        node_count = exact_int(entry["node_count"], "static nodes", minimum=1)
        internal = exact_int(entry["internal_count"], "static internal")
        terminal = exact_int(entry["terminal_count"], "static terminal", minimum=1)
        if node_count != internal + terminal:
            raise ValueError(f"static node accounting mismatch: {pair}")
        if exact_int(entry["unresolved_count"], "static unresolved") != 0:
            raise ValueError(f"static unresolved cells: {pair}")
        tree_hashes(entry["tree_content_sha256"], "static tree hashes")
        proof_by_pair[pair] = entry
    if set(proof_by_pair) != set(EXPECTED_PAIRS):
        raise ValueError("static proof matrix is incomplete")

    totals = summary["totals"]
    if type(totals) is not dict or set(totals) != {
        "node_count",
        "internal_count",
        "terminal_count",
        "unresolved_count",
        "wall_seconds",
    }:
        raise TypeError("static totals schema")
    expected_totals = {
        "node_count": sum(entry["node_count"] for entry in proofs),
        "internal_count": sum(entry["internal_count"] for entry in proofs),
        "terminal_count": sum(entry["terminal_count"] for entry in proofs),
        "unresolved_count": 0,
    }
    for key, expected in expected_totals.items():
        if exact_int(totals[key], f"static totals.{key}") != expected:
            raise ValueError(f"static total mismatch: {key}")
    if finite_number(totals["wall_seconds"], "static wall seconds") < 0:
        raise ValueError("static wall seconds is negative")

    bindings = summary["source_bindings"]
    if type(bindings) is not dict or set(bindings) != {
        "runner_sha256",
        "checker_sha256",
        "l1_final_plan_sha256",
        "l1_release_chain_sha256",
    }:
        raise TypeError("static source bindings schema")
    if bindings["runner_sha256"] != sha256(STATIC_RUNNER):
        raise ValueError("static runner source binding")
    if bindings["checker_sha256"] != sha256(STATIC_CHECKER_SOURCE):
        raise ValueError("static checker source binding")
    hash_string(bindings["l1_final_plan_sha256"], "static L1 plan hash")
    chain = bindings["l1_release_chain_sha256"]
    if type(chain) is not dict or len(chain) != 5:
        raise TypeError("static L1 release-chain binding")
    for name, digest in chain.items():
        if type(name) is not str or not name.startswith("results/r401_val_l1_branch/"):
            raise ValueError("static L1 release-chain path")
        target = ROOT / name
        secure_file(target, "static L1 release-chain file")
        if hash_string(digest, "static L1 release-chain hash") != sha256(target):
            raise ValueError(f"static L1 release-chain mismatch: {name}")

    manifest_files = manifest["files"]
    if type(manifest_files) is not list or len(manifest_files) != 7:
        raise TypeError("static manifest must have seven entries")
    if {item.get("path") for item in manifest_files if type(item) is dict} != expected_paths | {"summary.json"}:
        raise ValueError("static manifest file set")
    for item in manifest_files:
        if type(item) is not dict:
            raise TypeError("static manifest entry")
        relative = item.get("path")
        target = secure_component_file(directory, relative, "static manifest payload")
        if hash_string(item.get("sha256"), "static manifest hash") != sha256(target):
            raise ValueError(f"static manifest hash mismatch: {relative}")
        if exact_int(item.get("size_bytes"), "static manifest size") != target.stat().st_size:
            raise ValueError(f"static manifest size mismatch: {relative}")

    if checker["passed"] is not True or exact_int(checker["proof_count"], "static checker proof count") != 6:
        raise ValueError("static checker did not pass six proofs")
    if checker["checker_sha256"] != sha256(STATIC_CHECKER_SOURCE):
        raise ValueError("static checker self hash")
    for key in ("node_count", "internal_count", "terminal_count", "unresolved_count"):
        if exact_int(checker[key], f"static checker.{key}") != expected_totals[key]:
            raise ValueError(f"static checker total mismatch: {key}")
    if exact_int(checker["independent_interval_checks"], "static interval checks", minimum=1) <= 0:
        raise ValueError("static checker made no interval checks")
    checker_results = checker["proof_results"]
    if type(checker_results) is not list or len(checker_results) != 6:
        raise TypeError("static checker proof results")
    checker_pairs: set[tuple[int, str]] = set()
    for item in checker_results:
        if type(item) is not dict:
            raise TypeError("static checker proof result")
        exact_keys(item, STATIC_CHECKER_PROOF_KEYS, "static checker proof result")
        replay_bits = exact_int(
            item["precision_bits"], "static checker precision", minimum=1
        )
        if type(item["slab_id"]) is not str:
            raise TypeError("static checker slab")
        pair = (replay_bits, item["slab_id"])
        if pair not in EXPECTED_PAIRS or pair in checker_pairs:
            raise ValueError(f"static checker pair: {pair}")
        checker_pairs.add(pair)
        proof = proof_by_pair[pair]
        for key in (
            "path",
            "sha256",
            "node_count",
            "internal_count",
            "terminal_count",
            "unresolved_count",
            "tree_content_sha256",
        ):
            if not exact_json_equal(item[key], proof[key]):
                raise ValueError(f"static checker/proof mismatch {pair}: {key}")
        exact_int(item["interval_checks"], "static checker interval checks", minimum=1)
        if type(item["angle_extrema"]) is not dict:
            raise TypeError("static angle extrema")

    component = {
        "protocol_id": STATIC_PROTOCOL,
        "component_scope": "STATIC_ONLY",
        "component_status": STATIC_STATUS,
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "checker_passed": True,
        "control_files": control_records("static", directory),
    }
    return component, proof_by_pair


def require_branch_common(payload: dict[str, Any], context: str) -> None:
    if not exact_json_equal(payload.get("protocol_id"), BRANCH_PROTOCOL):
        raise ValueError(f"{context} protocol")
    if not exact_json_equal(payload.get("licensing"), "NON_LICENSING"):
        raise ValueError(f"{context} licensing")
    if not exact_json_equal(payload.get("prototype_status"), BRANCH_STATUS):
        raise ValueError(f"{context} component status")
    require_non_authoritative(payload, context)


def expected_branch_manifest_paths(directory: Path) -> set[Path]:
    paths = {
        BRANCH_CPP.resolve(),
        BRANCH_RUNNER.resolve(),
        BRANCH_CHECKER_SOURCE.resolve(),
        BRANCH_DEPENDENCY.resolve(),
        *(path.resolve() for path in L1_CONTROL_FILES),
        (directory / "summary.json").resolve(),
        (directory / "R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md").resolve(),
        (directory / "capd_r401_phase_branch_tube_mp").resolve(),
        (directory / "compile_stdout.txt").resolve(),
        (directory / "compile_stderr.txt").resolve(),
    }
    for bits, slab in EXPECTED_PAIRS:
        paths.add((directory / f"raw/{bits}/{slab}.txt").resolve())
        paths.add((directory / f"raw/{bits}/{slab}.stderr.txt").resolve())
    return paths


def validate_branch_component(directory: Path) -> tuple[dict[str, Any], dict[tuple[int, str], dict[str, Any]], dict[Path, str]]:
    summary_path = secure_component_file(directory, "summary.json", "branch summary")
    manifest_path = secure_component_file(directory, "manifest.json", "branch manifest")
    checker_path = secure_component_file(
        directory, "independent_checker.json", "branch checker result"
    )
    summary = strict_json(summary_path)
    manifest = strict_json(manifest_path)
    checker = strict_json(checker_path)
    exact_keys(summary, BRANCH_SUMMARY_KEYS, "branch summary")
    exact_keys(manifest, BRANCH_MANIFEST_KEYS, "branch manifest")
    exact_keys(checker, BRANCH_CHECKER_KEYS, "branch checker")
    for payload, context in (
        (summary, "branch summary"),
        (manifest, "branch manifest"),
        (checker, "branch checker"),
    ):
        require_branch_common(payload, context)
    require_exact_json(
        summary["representative_slabs"],
        list(REPRESENTATIVE_SLABS),
        "branch slab matrix",
    )
    require_exact_json(summary["precisions"], list(PRECISIONS), "branch precision matrix")
    if (
        summary["pair_gate"] is not True
        or exact_int(summary["phase_grid"], "branch phase grid") != 64
    ):
        raise ValueError("branch pair or phase-grid gate")
    if summary["tube_radius"] != "0.04" or summary["tube_radius_sq"] != "0.0016":
        raise ValueError("branch tube radius")
    if finite_number(summary["elapsed_seconds"], "branch elapsed seconds") < 0:
        raise ValueError("branch elapsed seconds is negative")

    records = summary["records"]
    if type(records) is not list or len(records) != 6:
        raise TypeError("branch record list")
    record_by_pair: dict[tuple[int, str], dict[str, Any]] = {}
    for record in records:
        if type(record) is not dict:
            raise TypeError("branch record")
        exact_keys(record, BRANCH_RECORD_KEYS, "branch record")
        bits = exact_int(record["precision_bits"], "branch precision", minimum=1)
        slab = record["slab_id"]
        if type(slab) is not str:
            raise TypeError("branch slab")
        pair = (bits, slab)
        if pair not in EXPECTED_PAIRS or pair in record_by_pair:
            raise ValueError(f"branch unexpected or duplicate pair: {pair}")
        if (
            record["status"] != BRANCH_STATUS
            or record["passed"] is not True
            or record["input_echo_gate"] is not True
            or record["all_segments_inside"] is not True
            or record["phase_cover_complete"] is not True
            or exact_int(record["returncode"], "branch return code") != 0
            or exact_int(record["taylor_order"], "branch Taylor order") != 24
        ):
            raise ValueError(f"branch record did not pass: {pair}")
        if record["tolerance"] != ("1e-30" if bits == 128 else "1e-60"):
            raise ValueError(f"branch tolerance: {pair}")
        if exact_int(record["solution_piece_count"], "branch SolutionCurve pieces", minimum=1) <= 0:
            raise ValueError(f"branch empty SolutionCurve: {pair}")
        if finite_number(record["wall_seconds"], "branch wall seconds") < 0:
            raise ValueError(f"branch negative wall seconds: {pair}")
        for key in (
            "maximum_rslow_sq_upper",
            "maximum_segment_rslow_sq_upper",
            "minimum_margin_sq_lower",
        ):
            if type(record[key]) is not str:
                raise TypeError(f"branch {key}: {pair}")
        record_by_pair[pair] = record
    if set(record_by_pair) != set(EXPECTED_PAIRS):
        raise ValueError("branch matrix incomplete")

    input_hashes = summary["input_hashes"]
    if type(input_hashes) is not dict:
        raise TypeError("branch input hashes")
    for source in (BRANCH_CPP, BRANCH_RUNNER, BRANCH_CHECKER_SOURCE):
        relative = str(source.relative_to(ROOT))
        if input_hashes.get(relative) != sha256(source):
            raise ValueError(f"branch source binding: {relative}")

    manifest_files = manifest["files"]
    if type(manifest_files) is not dict or not manifest_files:
        raise TypeError("branch manifest files")
    resolved_hashes: dict[Path, str] = {}
    for name, digest in manifest_files.items():
        if type(name) is not str or not Path(name).is_absolute():
            raise ValueError("branch manifest path must be absolute")
        path = Path(name)
        try:
            path.resolve().relative_to(ROOT)
        except ValueError as error:
            raise ValueError(f"branch manifest path escapes Paper02 root: {path}") from error
        secure_file(path, "branch manifest payload")
        expected = hash_string(digest, "branch manifest hash")
        if sha256(path) != expected:
            raise ValueError(f"branch manifest hash mismatch: {path}")
        if path.resolve() in resolved_hashes:
            raise ValueError(f"branch duplicate resolved manifest path: {path}")
        resolved_hashes[path.resolve()] = expected
    expected_manifest_paths = expected_branch_manifest_paths(directory)
    if set(resolved_hashes) != expected_manifest_paths or len(resolved_hashes) != 26:
        raise ValueError("branch manifest is not the exact frozen 26-file set")

    if (
        not exact_json_equal(checker["checker_status"], "PASS")
        or not exact_json_equal(checker["failures"], [])
        or exact_int(checker["raw_replay_count"], "branch raw replay count") != 6
        or exact_int(checker["manifest_file_count"], "branch manifest file count")
        != len(manifest_files)
    ):
        raise ValueError("branch independent checker did not pass")
    for key in ("maximum_rslow_sq_upper", "minimum_margin_sq_lower"):
        if type(checker[key]) is not str:
            raise TypeError(f"branch checker {key}")

    component = {
        "protocol_id": BRANCH_PROTOCOL,
        "component_scope": "BRANCH_TUBE_ONLY",
        "component_status": BRANCH_STATUS,
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "checker_passed": True,
        "control_files": control_records("branch", directory),
    }
    return component, record_by_pair, resolved_hashes


def control_records(component: str, directory: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for name in CONTROL_NAMES:
        path = secure_component_file(directory, name, f"{component} control file")
        records.append(
            {
                "component": component,
                "path": name,
                "sha256": sha256(path),
                "size_bytes": path.stat().st_size,
            }
        )
    return records


def root_relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def source_bindings() -> dict[str, str]:
    bindings: dict[str, str] = {}
    for path in SOURCE_FILES:
        secure_file(path, "composite source binding")
        relative = root_relative(path)
        if relative in bindings:
            raise ValueError(f"duplicate source binding: {relative}")
        bindings[relative] = sha256(path)
    return bindings


def local_manifest_record(path: Path, *, scope: str, display_path: str) -> dict[str, Any]:
    secure_file(path, "composite manifest payload")
    return {
        "scope": scope,
        "path": display_path,
        "sha256": sha256(path),
        "size_bytes": path.stat().st_size,
    }


def build_cells(
    static_proofs: dict[tuple[int, str], dict[str, Any]],
    branch_records: dict[tuple[int, str], dict[str, Any]],
    branch_manifest: dict[Path, str],
    branch_dir: Path,
) -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []
    for bits, slab in EXPECTED_PAIRS:
        static = static_proofs[(bits, slab)]
        branch = branch_records[(bits, slab)]
        raw_path = (branch_dir / branch["raw_file"]).resolve()
        stderr_path = (branch_dir / branch["stderr_file"]).resolve()
        if raw_path not in branch_manifest or stderr_path not in branch_manifest:
            raise ValueError(f"branch raw files are not manifest-bound: {(bits, slab)}")
        cells.append(
            {
                "precision_bits": bits,
                "slab_id": slab,
                "cell_passed": True,
                "static": {
                    "proof_path": static["path"],
                    "proof_sha256": static["sha256"],
                    "node_count": static["node_count"],
                    "internal_count": static["internal_count"],
                    "terminal_count": static["terminal_count"],
                    "unresolved_count": static["unresolved_count"],
                    "tree_content_sha256": static["tree_content_sha256"],
                },
                "branch": {
                    "raw_file": branch["raw_file"],
                    "raw_sha256": branch_manifest[raw_path],
                    "stderr_file": branch["stderr_file"],
                    "stderr_sha256": branch_manifest[stderr_path],
                    "solution_piece_count": branch["solution_piece_count"],
                    "maximum_rslow_sq_upper": branch["maximum_rslow_sq_upper"],
                    "minimum_margin_sq_lower": branch["minimum_margin_sq_lower"],
                },
            }
        )
    return cells


def common_fields() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_status": ARTIFACT_STATUS,
        "scientific_licensing_enabled": False,
        "component_scope": COMPONENT_SCOPE,
        "composite_s0_passed": True,
        "implementation_status": IMPLEMENTATION_STATUS,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def exclusive_write(path: Path, payload: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(payload)


def build_composite(static_dir: Path, branch_dir: Path, output_dir: Path) -> dict[str, Any]:
    reject_symlink(static_dir, "static result directory")
    reject_symlink(branch_dir, "branch result directory")
    if not static_dir.is_dir() or not branch_dir.is_dir():
        raise FileNotFoundError("both component result directories must exist")
    if output_dir.exists() or output_dir.is_symlink():
        raise FileExistsError(f"refusing to reuse composite output: {output_dir}")

    static_component, static_proofs = validate_static_component(static_dir)
    branch_component, branch_records, branch_manifest = validate_branch_component(
        branch_dir
    )
    cells = build_cells(static_proofs, branch_records, branch_manifest, branch_dir)
    if [(cell["precision_bits"], cell["slab_id"]) for cell in cells] != list(EXPECTED_PAIRS):
        raise ValueError("composite cells are not the canonical 3x2 order")
    bindings = source_bindings()
    summary = {
        **common_fields(),
        "claim_boundary": (
            "representative 3x2 A4.16 implementation composite only; not an "
            "all-slab result, theorem, global orbit exclusion, trace formula, "
            "Hilbert-Polya construction, zeta-zero result, or RH claim"
        ),
        "matrix": {
            "precisions": list(PRECISIONS),
            "slabs": list(REPRESENTATIVE_SLABS),
            "cell_count": 6,
        },
        "components": {
            "static": static_component,
            "branch": branch_component,
        },
        "cells": cells,
        "source_bindings": bindings,
    }
    summary_payload = canonical_bytes(summary)
    report = f"""# R401-VAL-L3 S0 composite implementation smoke

Artifact status: `{ARTIFACT_STATUS}`  
Scientific licensing enabled: `false`  
Component scope: `{COMPONENT_SCOPE}`  
Composite S0 passed: `true`  
Implementation status: `{IMPLEMENTATION_STATUS}`  
Milestone status: `null`  
Theorem status: `null`  
Final status: `null`

The independently checked static phase component and independently checked
continuous branch-tube component cover the same exact matrix
`S000/S025/S050 x 128/256`.  All six composite cells are bound by exact
control-file, proof, raw-transcript, source, and draft-document hashes.

This is a representative implementation smoke only.  It is not an all-slab
A4.16 result, a theorem, a global orbit exclusion, a trace formula, a
Hilbert--Polya operator construction, a zeta-zero result, or an RH claim.
""".encode("utf-8")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    if output_dir.exists() or output_dir.is_symlink():
        raise FileExistsError(f"refusing to reuse composite output: {output_dir}")
    output_dir.mkdir()
    summary_path = output_dir / "summary.json"
    report_path = output_dir / "R401_VAL_L3_S0_COMPOSITE_REPORT.md"
    exclusive_write(summary_path, summary_payload)
    exclusive_write(report_path, report)

    manifest_files = [
        local_manifest_record(
            summary_path, scope="OUTPUT", display_path="summary.json"
        ),
        local_manifest_record(
            report_path,
            scope="OUTPUT",
            display_path="R401_VAL_L3_S0_COMPOSITE_REPORT.md",
        ),
        *[
            local_manifest_record(
                path, scope="ROOT", display_path=root_relative(path)
            )
            for path in SOURCE_FILES
        ],
    ]
    component_files = [
        *static_component["control_files"],
        *branch_component["control_files"],
    ]
    manifest = {
        **common_fields(),
        "files": manifest_files,
        "component_files": component_files,
    }
    exclusive_write(output_dir / "manifest.json", canonical_bytes(manifest))
    return summary


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--static-dir", type=Path, default=STATIC_DIR_DEFAULT)
    parser.add_argument("--branch-dir", type=Path, default=BRANCH_DIR_DEFAULT)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        summary = build_composite(
            arguments.static_dir.absolute(),
            arguments.branch_dir.absolute(),
            arguments.output_dir.absolute(),
        )
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"component_scope={summary['component_scope']} "
        f"composite_s0_passed=true "
        f"implementation_status={summary['implementation_status']} "
        f"cells={summary['matrix']['cell_count']} final_status=null"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
