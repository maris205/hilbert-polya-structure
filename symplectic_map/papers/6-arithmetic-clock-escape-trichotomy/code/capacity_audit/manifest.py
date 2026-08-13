"""Strict post-run result-manifest construction and lifecycle validation."""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from .controls import run_all_controls
from .ledger import audit_proof_ledger, audit_scope_ledger
from .protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    load_strict_json_file,
    regular_file_within,
    sha256_file,
    static_executable_isolation_scan,
    validate_source_lock,
)
from .review_gate import reviewed_code_tree_sha256, validate_review_authority
from .scope import audit_escape_semantics, audit_output_scope
from .upstream import validate_upstream_bindings


REQUIRED_RESULT_PATHS = (
    "experiments/source_lock.json",
    "experiments/proof_ledger.json",
    "experiments/scope_ledger.json",
    "experiments/upstream_bindings.json",
    "notes/INDEPENDENT_PROOF_NOVELTY_REVIEW.md",
    "results/CODE_REVIEW.md",
    "results/EXPERIMENT_RESULTS.json",
    "results/registered_run.json",
)
ALLOWED_RESULT_FILES_PRE_RUN = {"CODE_REVIEW.md"}
ALLOWED_RESULT_FILES_POST_RUN = {
    "CODE_REVIEW.md",
    "EXPERIMENT_RESULTS.json",
    "registered_run.json",
}

RESULT_KEYS = {
    "schema",
    "candidate_id",
    "registered_at_utc",
    "audit_type",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "gates",
    "external_prime_tables_accessed",
    "prime_target_arrays_generated",
    "riemann_zero_data_accessed",
    "candidate_numerical_runs",
    "target_matches_computed",
    "classification",
    "pass",
}
REGISTRY_KEYS = {
    "schema",
    "candidate_id",
    "registered_at_utc",
    "result_path",
    "result_sha256",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "registered_run_count",
    "candidate_numerical_runs",
}
GATE_KEYS = {
    "source_lock",
    "independent_code_review",
    "proof_ledger",
    "scope_ledger",
    "exact_controls",
    "executable_isolation",
    "upstream_bindings",
    "escape_semantics",
    "output_scope",
}


def _canonical_json(value: Any) -> str:
    """Serialize JSON values so booleans and integers remain distinguishable."""

    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _exact_int(value: Any, expected: int) -> bool:
    """Require a JSON integer, explicitly excluding Python's bool subclass."""

    return type(value) is int and value == expected


def _utc_timestamp(value: Any) -> bool:
    """Require the canonical timezone-aware ISO string emitted by the runner."""

    if type(value) is not str:
        return False
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return False
    return (
        parsed.tzinfo is not None
        and parsed.utcoffset() == timedelta(0)
        and value == parsed.isoformat()
    )


def _expected_gate_records(project_root: Path) -> dict[str, dict[str, Any]]:
    """Recompute every safe gate for exact post-run record comparison."""

    return {
        "source_lock": validate_source_lock(project_root),
        "independent_code_review": validate_review_authority(project_root),
        "proof_ledger": audit_proof_ledger(project_root),
        "scope_ledger": audit_scope_ledger(project_root),
        "exact_controls": run_all_controls(),
        "executable_isolation": static_executable_isolation_scan(project_root / "code"),
        "upstream_bindings": validate_upstream_bindings(project_root),
        "escape_semantics": audit_escape_semantics(
            necessary=True,
            mutually_exclusive=False,
            exhaustive_for_all_dynamics=False,
            sufficient=False,
        ),
        "output_scope": audit_output_scope("CAPACITY_BOUND_CERTIFIED"),
    }


def _result_tree_findings(project_root: Path, *, post_run: bool) -> dict[str, Any]:
    results = project_root / "results"
    allowed = ALLOWED_RESULT_FILES_POST_RUN if post_run else ALLOWED_RESULT_FILES_PRE_RUN
    discovered: set[str] = set()
    symlinks: list[str] = []
    nested: list[str] = []
    if results.exists():
        for path in results.rglob("*"):
            relative = path.relative_to(results).as_posix()
            if path.is_symlink():
                symlinks.append(relative)
            if path.is_file() or path.is_symlink():
                discovered.add(relative)
                if "/" in relative:
                    nested.append(relative)
    unknown = sorted(discovered.difference(allowed))
    missing = sorted(allowed.difference(discovered))
    return {
        "allowed": sorted(allowed),
        "discovered": sorted(discovered),
        "missing": missing,
        "unknown": unknown,
        "nested": sorted(nested),
        "symlinks": sorted(symlinks),
        "pass": not missing and not unknown and not nested and not symlinks,
    }


def _validate_post_run_semantics(project_root: Path) -> dict[str, Any]:
    result_path = project_root / "results" / "EXPERIMENT_RESULTS.json"
    registry_path = project_root / "results" / "registered_run.json"
    errors: list[str] = []
    try:
        result = load_strict_json_file(project_root, result_path)
        registry = load_strict_json_file(project_root, registry_path)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        return {"errors": [f"STRICT_JSON_LOAD_FAIL:{type(error).__name__}"], "pass": False}
    if type(result) is not dict or set(result) != RESULT_KEYS:
        errors.append("RESULT_SCHEMA_NOT_EXACT")
    if type(registry) is not dict or set(registry) != REGISTRY_KEYS:
        errors.append("REGISTRY_SCHEMA_NOT_EXACT")
    if errors:
        return {"errors": errors, "pass": False}

    code_digest = reviewed_code_tree_sha256(project_root)
    gates = result.get("gates")
    expected_gates = _expected_gate_records(project_root)
    gates_exact = (
        type(gates) is dict
        and set(gates) == GATE_KEYS
        and _canonical_json(gates) == _canonical_json(expected_gates)
    )
    all_gates_pass = gates_exact and all(
        type(record) is dict
        and type(record.get("pass")) is bool
        and record["pass"] is True
        for record in gates.values()
    )
    if not gates_exact:
        errors.append("RESULT_GATE_RECORDS_NOT_EXACT")
    elif not all_gates_pass:
        errors.append("RESULT_GATE_FAILURE")
    result_types_exact = (
        type(result["schema"]) is str
        and type(result["candidate_id"]) is str
        and _utc_timestamp(result["registered_at_utc"])
        and type(result["audit_type"]) is str
        and type(result["source_lock_sha256"]) is str
        and type(result["reviewed_code_sha256"]) is str
        and type(result["gates"]) is dict
        and type(result["external_prime_tables_accessed"]) is bool
        and type(result["prime_target_arrays_generated"]) is bool
        and type(result["riemann_zero_data_accessed"]) is bool
        and type(result["candidate_numerical_runs"]) is int
        and type(result["target_matches_computed"]) is int
        and type(result["classification"]) is str
        and type(result["pass"]) is bool
    )
    if not result_types_exact:
        errors.append("RESULT_TYPES_NOT_EXACT")
    result_valid = (
        result_types_exact
        and
        result["schema"] == "CAPACITY_REGISTERED_AUDIT_V1"
        and result["candidate_id"] == CANDIDATE_ID
        and result["audit_type"] == "EXACT_SYMBOLIC_AND_STATIC_ONLY"
        and result["source_lock_sha256"] == EXPECTED_LOCK_SHA256
        and result["reviewed_code_sha256"] == code_digest
        and result["external_prime_tables_accessed"] is False
        and result["prime_target_arrays_generated"] is False
        and result["riemann_zero_data_accessed"] is False
        and _exact_int(result["candidate_numerical_runs"], 0)
        and _exact_int(result["target_matches_computed"], 0)
        and result["classification"] == "CAPACITY_BOUND_CERTIFIED"
        and result["pass"] is True
        and all_gates_pass
    )
    if not result_valid:
        errors.append("RESULT_SEMANTICS_FAIL")
    result_digest = sha256_file(result_path) if regular_file_within(project_root, result_path) else None
    registry_types_exact = (
        type(registry["schema"]) is str
        and type(registry["candidate_id"]) is str
        and _utc_timestamp(registry["registered_at_utc"])
        and type(registry["result_path"]) is str
        and type(registry["result_sha256"]) is str
        and type(registry["source_lock_sha256"]) is str
        and type(registry["reviewed_code_sha256"]) is str
        and type(registry["registered_run_count"]) is int
        and type(registry["candidate_numerical_runs"]) is int
    )
    if not registry_types_exact:
        errors.append("REGISTRY_TYPES_NOT_EXACT")
    registry_valid = (
        registry_types_exact
        and
        registry["schema"] == "CAPACITY_REGISTERED_RUN_REGISTRY_V1"
        and registry["candidate_id"] == CANDIDATE_ID
        and registry["registered_at_utc"] == result["registered_at_utc"]
        and registry["result_path"] == "results/EXPERIMENT_RESULTS.json"
        and registry["result_sha256"] == result_digest
        and registry["source_lock_sha256"] == EXPECTED_LOCK_SHA256
        and registry["reviewed_code_sha256"] == code_digest
        and _exact_int(registry["registered_run_count"], 1)
        and _exact_int(registry["candidate_numerical_runs"], 0)
    )
    if not registry_valid:
        errors.append("REGISTRY_SEMANTICS_FAIL")
    return {
        "result_sha256": result_digest,
        "reviewed_code_sha256": code_digest,
        "errors": errors,
        "pass": not errors,
    }


def build_result_manifest(project_root: Path) -> dict[str, Any]:
    """Validate exact post-run lifecycle semantics, then hash required files."""

    project_root = project_root.resolve()
    lifecycle = _result_tree_findings(project_root, post_run=True)
    semantics = _validate_post_run_semantics(project_root) if lifecycle["pass"] else {
        "errors": ["RESULT_TREE_NOT_EXACT"],
        "pass": False,
    }
    records: list[dict[str, str]] = []
    missing: list[str] = []
    unsafe: list[str] = []
    for relative in REQUIRED_RESULT_PATHS:
        path = project_root / relative
        if not path.exists():
            missing.append(relative)
        elif not regular_file_within(project_root, path):
            unsafe.append(relative)
        else:
            records.append({"path": relative, "sha256": sha256_file(path)})
    passed = lifecycle["pass"] and semantics["pass"] and not missing and not unsafe
    return {
        "schema": "CAPACITY_RESULT_MANIFEST_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_tree_sha256(project_root),
        "result_tree": lifecycle,
        "semantic_checks": semantics,
        "files": records,
        "missing": missing,
        "unsafe": unsafe,
        "pass": passed,
    }


def write_result_manifest(project_root: Path) -> Path:
    """Write a final manifest atomically and exclusively after validation."""

    project_root = project_root.resolve()
    manifest = build_result_manifest(project_root)
    if not manifest["pass"]:
        raise RuntimeError("result manifest failed strict lifecycle validation")
    output = project_root / "results" / "result_manifest.json"
    with output.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return output
