#!/usr/bin/env python3
"""No-packager-import checker for the NON_LICENSING L3 S0 composite."""

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
PACKAGER = ROOT / "scripts/build_r401_val_l3_s0_composite.py"
CHECKER = Path(__file__).resolve()
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
    CHECKER,
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
STATIC_PROOF_KEYS = {
    "internal_count", "node_count", "path", "precision_bits", "sha256",
    "size_bytes", "slab_id", "terminal_count", "tree_content_sha256",
    "unresolved_count",
}
STATIC_REPLAY_KEYS = (STATIC_PROOF_KEYS - {"size_bytes"}) | {
    "angle_extrema", "interval_checks",
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
COMMON_KEYS = {
    "schema_version", "protocol_id", "artifact_status",
    "scientific_licensing_enabled", "component_scope", "composite_s0_passed",
    "implementation_status", "milestone_status", "theorem_status", "final_status",
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
    secure_file(path, "JSON file")
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
    if set(payload) != expected:
        raise ValueError(
            f"{context} keys: missing={sorted(expected - set(payload))}, "
            f"extra={sorted(set(payload) - expected)}"
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
        raise TypeError(f"{context} must be a finite number")
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


def component_file(directory: Path, relative: str, context: str) -> Path:
    if type(relative) is not str or Path(relative).parts != (relative,):
        raise ValueError(f"{context} is not a canonical basename: {relative}")
    reject_symlink(directory, context)
    path = directory / relative
    reject_symlink(path, context)
    if path.parent.resolve() != directory.resolve() or not path.is_file():
        raise ValueError(f"{context} escapes or is missing: {relative}")
    return path


def authority_null(payload: dict[str, Any], context: str) -> None:
    if payload.get("final_status", object()) is not None:
        raise ValueError(f"{context} final_status")
    for key in ("milestone_status", "theorem_status"):
        if key in payload and payload[key] is not None:
            raise ValueError(f"{context} assigned {key}")


def static_common(payload: dict[str, Any], context: str) -> None:
    required = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": STATIC_PROTOCOL,
        "artifact_status": ARTIFACT_STATUS,
        "implementation_status": STATIC_STATUS,
        "component_scope": "STATIC_ONLY",
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
    }
    for key, expected in required.items():
        if key not in payload or not exact_json_equal(payload[key], expected):
            raise ValueError(f"{context} {key}")
    authority_null(payload, context)


def tree_hashes(value: Any, context: str) -> dict[str, str]:
    expected = {"ANGLE", "SECTION_LOW", "SECTION_WINDOW", "SECTION_HIGH"}
    if type(value) is not dict or set(value) != expected:
        raise TypeError(f"{context} tree hash set")
    return {key: hash_string(item, f"{context}.{key}") for key, item in value.items()}


def control_records(component: str, directory: Path) -> list[dict[str, Any]]:
    return [
        {
            "component": component,
            "path": name,
            "sha256": sha256(component_file(directory, name, f"{component} control")),
            "size_bytes": component_file(directory, name, f"{component} control").stat().st_size,
        }
        for name in CONTROL_NAMES
    ]


def replay_static(directory: Path) -> tuple[dict[str, Any], dict[tuple[int, str], dict[str, Any]]]:
    summary = strict_json(component_file(directory, "summary.json", "static summary"))
    manifest = strict_json(component_file(directory, "manifest.json", "static manifest"))
    checker = strict_json(component_file(directory, "independent_checker.json", "static checker"))
    exact_keys(summary, STATIC_SUMMARY_KEYS, "static summary")
    exact_keys(manifest, STATIC_MANIFEST_KEYS, "static manifest")
    exact_keys(checker, STATIC_CHECKER_KEYS, "static checker")
    for payload, context in ((summary, "static summary"), (manifest, "static manifest"), (checker, "static checker")):
        static_common(payload, context)
    require_exact_json(summary["matrix"], {
        "precisions": list(PRECISIONS), "proof_count": 6,
        "slabs": list(REPRESENTATIVE_SLABS),
    }, "static 3x2 matrix")
    proofs = summary["proofs"]
    if type(proofs) is not list or len(proofs) != 6:
        raise TypeError("static proof list")
    by_pair: dict[tuple[int, str], dict[str, Any]] = {}
    for proof in proofs:
        if type(proof) is not dict:
            raise TypeError("static proof entry")
        exact_keys(proof, STATIC_PROOF_KEYS, "static proof")
        proof_bits = exact_int(proof["precision_bits"], "static precision", minimum=1)
        if type(proof["slab_id"]) is not str:
            raise TypeError("static slab")
        pair = (proof_bits, proof["slab_id"])
        if pair not in EXPECTED_PAIRS or pair in by_pair:
            raise ValueError(f"static proof pair: {pair}")
        target = component_file(directory, proof["path"], "static proof payload")
        if proof["path"] != f"proof_{pair[0]}_{pair[1]}.json":
            raise ValueError(f"static proof path: {pair}")
        if hash_string(proof["sha256"], "static proof hash") != sha256(target):
            raise ValueError(f"static proof hash: {pair}")
        if exact_int(proof["size_bytes"], "static proof size") != target.stat().st_size:
            raise ValueError(f"static proof size: {pair}")
        nodes = exact_int(proof["node_count"], "static nodes", minimum=1)
        internal = exact_int(proof["internal_count"], "static internal")
        terminal = exact_int(proof["terminal_count"], "static terminal", minimum=1)
        unresolved = exact_int(proof["unresolved_count"], "static unresolved")
        if nodes != internal + terminal or unresolved != 0:
            raise ValueError(f"static counts: {pair}")
        tree_hashes(proof["tree_content_sha256"], "static tree hashes")
        by_pair[pair] = proof
    if tuple(sorted(by_pair, key=lambda pair: (pair[0], REPRESENTATIVE_SLABS.index(pair[1])))) != EXPECTED_PAIRS:
        raise ValueError("static matrix incomplete")

    totals = summary["totals"]
    if type(totals) is not dict or set(totals) != {
        "node_count", "internal_count", "terminal_count", "unresolved_count", "wall_seconds",
    }:
        raise TypeError("static totals")
    computed = {
        "node_count": sum(item["node_count"] for item in proofs),
        "internal_count": sum(item["internal_count"] for item in proofs),
        "terminal_count": sum(item["terminal_count"] for item in proofs),
        "unresolved_count": 0,
    }
    for key, expected in computed.items():
        if exact_int(totals[key], f"static total.{key}") != expected:
            raise ValueError(f"static total: {key}")
    if finite_number(totals["wall_seconds"], "static wall seconds") < 0:
        raise ValueError("static wall seconds")
    bindings = summary["source_bindings"]
    if type(bindings) is not dict or bindings.get("runner_sha256") != sha256(STATIC_RUNNER) or bindings.get("checker_sha256") != sha256(STATIC_CHECKER_SOURCE):
        raise ValueError("static source bindings")

    files = manifest["files"]
    expected_names = {f"proof_{bits}_{slab}.json" for bits, slab in EXPECTED_PAIRS} | {"summary.json"}
    if type(files) is not list or len(files) != 7 or {item.get("path") for item in files if type(item) is dict} != expected_names:
        raise ValueError("static manifest file set")
    for item in files:
        if type(item) is not dict:
            raise TypeError("static manifest entry")
        target = component_file(directory, item.get("path"), "static manifest payload")
        if hash_string(item.get("sha256"), "static manifest hash") != sha256(target):
            raise ValueError("static manifest hash")
        if exact_int(item.get("size_bytes"), "static manifest size") != target.stat().st_size:
            raise ValueError("static manifest size")

    if (
        checker["passed"] is not True
        or exact_int(checker["proof_count"], "static checker proof count") != 6
        or exact_int(checker["unresolved_count"], "static checker unresolved") != 0
    ):
        raise ValueError("static independent checker")
    if checker["checker_sha256"] != sha256(STATIC_CHECKER_SOURCE):
        raise ValueError("static checker self hash")
    for key in ("node_count", "internal_count", "terminal_count", "unresolved_count"):
        if exact_int(checker[key], f"static checker total.{key}") != computed[key]:
            raise ValueError(f"static checker total: {key}")
    exact_int(checker["independent_interval_checks"], "static interval checks", minimum=1)
    replay = checker["proof_results"]
    if type(replay) is not list or len(replay) != 6:
        raise TypeError("static replay list")
    seen: set[tuple[int, str]] = set()
    for item in replay:
        if type(item) is not dict:
            raise TypeError("static replay entry")
        exact_keys(item, STATIC_REPLAY_KEYS, "static replay")
        replay_bits = exact_int(
            item["precision_bits"], "static replay precision", minimum=1
        )
        if type(item["slab_id"]) is not str:
            raise TypeError("static replay slab")
        pair = (replay_bits, item["slab_id"])
        if pair not in by_pair or pair in seen:
            raise ValueError(f"static replay pair: {pair}")
        seen.add(pair)
        proof = by_pair[pair]
        for key in (
            "path", "sha256", "node_count", "internal_count", "terminal_count",
            "unresolved_count", "tree_content_sha256",
        ):
            if not exact_json_equal(item[key], proof[key]):
                raise ValueError(f"static replay mismatch {pair}: {key}")
        exact_int(item["interval_checks"], "static replay interval checks", minimum=1)
        if type(item["angle_extrema"]) is not dict:
            raise TypeError("static angle extrema")
    descriptor = {
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
    return descriptor, by_pair


def branch_common(payload: dict[str, Any], context: str) -> None:
    if not (
        exact_json_equal(payload.get("protocol_id"), BRANCH_PROTOCOL)
        and exact_json_equal(payload.get("licensing"), "NON_LICENSING")
        and exact_json_equal(payload.get("prototype_status"), BRANCH_STATUS)
    ):
        raise ValueError(f"{context} status")
    authority_null(payload, context)


def expected_branch_manifest_paths(directory: Path) -> set[Path]:
    paths = {
        BRANCH_CPP.resolve(), BRANCH_RUNNER.resolve(),
        BRANCH_CHECKER_SOURCE.resolve(), BRANCH_DEPENDENCY.resolve(),
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


def replay_branch(directory: Path) -> tuple[dict[str, Any], dict[tuple[int, str], dict[str, Any]], dict[Path, str]]:
    summary = strict_json(component_file(directory, "summary.json", "branch summary"))
    manifest = strict_json(component_file(directory, "manifest.json", "branch manifest"))
    checker = strict_json(component_file(directory, "independent_checker.json", "branch checker"))
    exact_keys(summary, BRANCH_SUMMARY_KEYS, "branch summary")
    exact_keys(manifest, BRANCH_MANIFEST_KEYS, "branch manifest")
    exact_keys(checker, BRANCH_CHECKER_KEYS, "branch checker")
    for payload, context in ((summary, "branch summary"), (manifest, "branch manifest"), (checker, "branch checker")):
        branch_common(payload, context)
    if (
        not exact_json_equal(summary["representative_slabs"], list(REPRESENTATIVE_SLABS))
        or not exact_json_equal(summary["precisions"], list(PRECISIONS))
        or summary["pair_gate"] is not True
        or exact_int(summary["phase_grid"], "branch phase grid") != 64
    ):
        raise ValueError("branch matrix")
    if summary["tube_radius"] != "0.04" or summary["tube_radius_sq"] != "0.0016":
        raise ValueError("branch radius")
    records = summary["records"]
    if type(records) is not list or len(records) != 6:
        raise TypeError("branch records")
    by_pair: dict[tuple[int, str], dict[str, Any]] = {}
    for record in records:
        if type(record) is not dict:
            raise TypeError("branch record")
        exact_keys(record, BRANCH_RECORD_KEYS, "branch record")
        bits = exact_int(record["precision_bits"], "branch precision", minimum=1)
        pair = (bits, record["slab_id"])
        if pair not in EXPECTED_PAIRS or pair in by_pair:
            raise ValueError(f"branch pair: {pair}")
        if not (
            record["status"] == BRANCH_STATUS and record["passed"] is True
            and record["input_echo_gate"] is True and record["all_segments_inside"] is True
            and record["phase_cover_complete"] is True
            and exact_int(record["returncode"], "branch return code") == 0
            and exact_int(record["taylor_order"], "branch Taylor order") == 24
        ):
            raise ValueError(f"branch record gate: {pair}")
        if record["tolerance"] != ("1e-30" if pair[0] == 128 else "1e-60"):
            raise ValueError(f"branch tolerance: {pair}")
        exact_int(record["solution_piece_count"], "branch pieces", minimum=1)
        if finite_number(record["wall_seconds"], "branch wall seconds") < 0:
            raise ValueError(f"branch wall seconds: {pair}")
        by_pair[pair] = record
    if set(by_pair) != set(EXPECTED_PAIRS):
        raise ValueError("branch matrix incomplete")
    input_hashes = summary["input_hashes"]
    for source in (BRANCH_CPP, BRANCH_RUNNER, BRANCH_CHECKER_SOURCE):
        if input_hashes.get(str(source.relative_to(ROOT))) != sha256(source):
            raise ValueError(f"branch source binding: {source}")

    manifest_files = manifest["files"]
    if type(manifest_files) is not dict or not manifest_files:
        raise TypeError("branch manifest")
    resolved: dict[Path, str] = {}
    for name, digest in manifest_files.items():
        if type(name) is not str or not Path(name).is_absolute():
            raise ValueError("branch manifest path")
        path = Path(name)
        try:
            path.resolve().relative_to(ROOT)
        except ValueError as error:
            raise ValueError("branch manifest escape") from error
        secure_file(path, "branch manifest payload")
        digest = hash_string(digest, "branch manifest hash")
        if sha256(path) != digest or path.resolve() in resolved:
            raise ValueError(f"branch manifest mismatch: {path}")
        resolved[path.resolve()] = digest
    if set(resolved) != expected_branch_manifest_paths(directory) or len(resolved) != 26:
        raise ValueError("branch manifest is not the exact frozen 26-file set")
    if (
        not exact_json_equal(checker["checker_status"], "PASS")
        or not exact_json_equal(checker["failures"], [])
        or exact_int(checker["raw_replay_count"], "branch raw replay count") != 6
        or exact_int(checker["manifest_file_count"], "branch manifest file count")
        != len(manifest_files)
    ):
        raise ValueError("branch independent checker")
    descriptor = {
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
    return descriptor, by_pair, resolved


def expected_cells(
    static: dict[tuple[int, str], dict[str, Any]],
    branch: dict[tuple[int, str], dict[str, Any]],
    branch_manifest: dict[Path, str],
    branch_dir: Path,
) -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []
    for bits, slab in EXPECTED_PAIRS:
        proof = static[(bits, slab)]
        record = branch[(bits, slab)]
        raw = (branch_dir / record["raw_file"]).resolve()
        stderr = (branch_dir / record["stderr_file"]).resolve()
        if raw not in branch_manifest or stderr not in branch_manifest:
            raise ValueError(f"branch raw binding: {(bits, slab)}")
        cells.append(
            {
                "precision_bits": bits,
                "slab_id": slab,
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
                    "raw_sha256": branch_manifest[raw],
                    "stderr_file": record["stderr_file"],
                    "stderr_sha256": branch_manifest[stderr],
                    "solution_piece_count": record["solution_piece_count"],
                    "maximum_rslow_sq_upper": record["maximum_rslow_sq_upper"],
                    "minimum_margin_sq_lower": record["minimum_margin_sq_lower"],
                },
            }
        )
    return cells


def root_relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def expected_source_bindings() -> dict[str, str]:
    bindings: dict[str, str] = {}
    for path in SOURCE_FILES:
        secure_file(path, "source binding")
        bindings[root_relative(path)] = sha256(path)
    return bindings


def common_gate(payload: dict[str, Any], context: str) -> None:
    expected = {
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
    for key, value in expected.items():
        if key not in payload or not exact_json_equal(payload[key], value):
            raise ValueError(f"{context} {key}")


def verify_composite(
    input_dir: Path,
    static_dir: Path,
    branch_dir: Path,
) -> tuple[int, int]:
    reject_symlink(input_dir, "composite directory")
    if not input_dir.is_dir():
        raise FileNotFoundError("composite directory")
    expected_names = {
        "summary.json", "manifest.json", "R401_VAL_L3_S0_COMPOSITE_REPORT.md"
    }
    actual_names = {path.name for path in input_dir.iterdir()}
    if actual_names != expected_names:
        raise ValueError(f"composite directory file set: {sorted(actual_names)}")
    summary_path = input_dir / "summary.json"
    manifest_path = input_dir / "manifest.json"
    report_path = input_dir / "R401_VAL_L3_S0_COMPOSITE_REPORT.md"
    summary = strict_json(summary_path)
    manifest = strict_json(manifest_path)
    secure_file(report_path, "composite report")
    exact_keys(
        summary,
        COMMON_KEYS | {"claim_boundary", "matrix", "components", "cells", "source_bindings"},
        "composite summary",
    )
    exact_keys(
        manifest,
        COMMON_KEYS | {"files", "component_files"},
        "composite manifest",
    )
    common_gate(summary, "composite summary")
    common_gate(manifest, "composite manifest")
    require_exact_json(summary["matrix"], {
        "precisions": list(PRECISIONS), "slabs": list(REPRESENTATIVE_SLABS),
        "cell_count": 6,
    }, "composite matrix")
    if type(summary["claim_boundary"]) is not str or "not an all-slab" not in summary["claim_boundary"]:
        raise ValueError("composite claim boundary")

    static_descriptor, static_proofs = replay_static(static_dir)
    branch_descriptor, branch_records, branch_manifest = replay_branch(branch_dir)
    expected_components = {"static": static_descriptor, "branch": branch_descriptor}
    if not exact_json_equal(summary["components"], expected_components):
        raise ValueError("composite component descriptors")
    cells = expected_cells(static_proofs, branch_records, branch_manifest, branch_dir)
    if not exact_json_equal(summary["cells"], cells):
        raise ValueError("composite cells do not independently reconstruct")
    bindings = expected_source_bindings()
    if not exact_json_equal(summary["source_bindings"], bindings):
        raise ValueError("composite source bindings")

    files = manifest["files"]
    expected_file_pairs = {
        ("OUTPUT", "summary.json"),
        ("OUTPUT", "R401_VAL_L3_S0_COMPOSITE_REPORT.md"),
        *(("ROOT", root_relative(path)) for path in SOURCE_FILES),
    }
    if type(files) is not list or len(files) != len(expected_file_pairs):
        raise TypeError("composite manifest file list")
    seen: set[tuple[str, str]] = set()
    for item in files:
        if type(item) is not dict:
            raise TypeError("composite manifest file")
        exact_keys(item, {"scope", "path", "sha256", "size_bytes"}, "composite manifest file")
        pair = (item["scope"], item["path"])
        if pair not in expected_file_pairs or pair in seen:
            raise ValueError(f"composite manifest file pair: {pair}")
        seen.add(pair)
        target = input_dir / item["path"] if item["scope"] == "OUTPUT" else ROOT / item["path"]
        secure_file(target, "composite manifest payload")
        if hash_string(item["sha256"], "composite manifest hash") != sha256(target):
            raise ValueError(f"composite manifest hash: {pair}")
        if exact_int(item["size_bytes"], "composite manifest size") != target.stat().st_size:
            raise ValueError(f"composite manifest size: {pair}")
    if seen != expected_file_pairs:
        raise ValueError("composite manifest file set incomplete")

    component_files = manifest["component_files"]
    expected_controls = static_descriptor["control_files"] + branch_descriptor["control_files"]
    if not exact_json_equal(component_files, expected_controls):
        raise ValueError("composite component control bindings")
    normalized_report = " ".join(report_path.read_text(encoding="utf-8").split())
    for token in (
        "DRAFT_NON_LICENSING", "Scientific licensing enabled: `false`",
        "Component scope: `COMPOSITE_S0`", "Composite S0 passed: `true`",
        "Implementation status: `PASS_IMPLEMENTATION_SMOKE`",
        "Milestone status: `null`", "Theorem status: `null`",
        "Final status: `null`", "not an all-slab A4.16 result",
    ):
        if token not in normalized_report:
            raise ValueError(f"composite report token: {token}")
    return len(cells), len(files) + len(component_files)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--static-dir", type=Path, default=STATIC_DIR_DEFAULT)
    parser.add_argument("--branch-dir", type=Path, default=BRANCH_DIR_DEFAULT)
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    input_dir = arguments.input_dir.absolute()
    output = arguments.output.absolute() if arguments.output else input_dir / "independent_checker.json"
    if output.parent.resolve() != input_dir.resolve() or output.name != "independent_checker.json":
        print("ERROR: checker output must be INPUT_DIR/independent_checker.json", file=sys.stderr)
        return 1
    if output.exists() or output.is_symlink():
        print(f"ERROR: refusing to overwrite checker result: {output}", file=sys.stderr)
        return 1
    failures: list[str] = []
    cell_count = 0
    manifest_binding_count = 0
    try:
        cell_count, manifest_binding_count = verify_composite(
            input_dir,
            arguments.static_dir.absolute(),
            arguments.branch_dir.absolute(),
        )
    except Exception as error:
        failures.append(f"{type(error).__name__}: {error}")
    passed = not failures
    payload = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_status": ARTIFACT_STATUS,
        "scientific_licensing_enabled": False,
        "component_scope": COMPONENT_SCOPE,
        "composite_s0_passed": passed,
        "implementation_status": IMPLEMENTATION_STATUS if passed else None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "checker_status": "PASS" if passed else "FAIL",
        "cell_replay_count": cell_count,
        "manifest_binding_count": manifest_binding_count,
        "checker_sha256": sha256(CHECKER),
        "failures": failures,
        "claim_boundary": (
            "independent control/hash/matrix replay of the representative S0 "
            "composite only; no theorem, all-slab, global, trace, zeta, or RH claim"
        ),
    }
    try:
        with output.open("xb") as handle:
            handle.write(canonical_bytes(payload))
    except Exception as error:
        print(f"ERROR: cannot write checker result: {error}", file=sys.stderr)
        return 1
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
