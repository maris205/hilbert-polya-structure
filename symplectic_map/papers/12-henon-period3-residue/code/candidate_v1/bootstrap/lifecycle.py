"""Durable one-shot claim, result, and terminal transitions."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CLAIM_PATH,
    CLAIM_SCHEMA_PATH,
    DEPLOYMENT_REVIEW_PATH,
    PROOF_SHA256,
    REGISTERED_INDICES,
    RESULT_PATH,
    RUNTIME_ROOT,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
    TERMINAL_FAILURE,
    TERMINAL_PATH,
    TERMINAL_SUCCESS,
)
from .protocol import (
    exact_same,
    fsync_directory,
    load_exact_json,
    mkdir_durable,
    regular_directory,
    regular_file,
    sha256_file,
    validate_canonical_json_file,
    write_json_exclusive,
)


def prepare_runtime_tree(project_root: Path) -> None:
    runtime_parent = project_root / "runtime"
    candidate_root = project_root / RUNTIME_ROOT
    if candidate_root.exists():
        raise RuntimeError("candidate runtime already exists; one-shot lifecycle is closed")
    if runtime_parent.exists():
        if not regular_directory(runtime_parent) or list(runtime_parent.iterdir()):
            raise RuntimeError("runtime parent is not a fresh regular directory")
    else:
        mkdir_durable(runtime_parent)
    mkdir_durable(candidate_root)
    for relative in (
        "official",
        "staging",
        "staging/track_q",
        "staging/track_r",
        "staging/final",
        "review",
    ):
        mkdir_durable(candidate_root / relative)
    fsync_directory(candidate_root)


def build_claim_object(
    manifest: dict[str, Any],
    review_sha256: str,
    code_manifest_sha256: str,
) -> dict[str, Any]:
    return {
        "schema": "HENON_PERIOD3_DURABLE_REGISTERED_CLAIM_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "R100",
        "state": "STARTED",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "proof_sha256": PROOF_SHA256,
        "code_tree_sha256": manifest["code_tree_sha256"],
        "code_manifest_sha256": code_manifest_sha256,
        "preflight_sha256": manifest["preflight_sha256"],
        "deployment_review_sha256": review_sha256,
        "definitions_sha256": manifest["definitions_sha256"],
        "registered_coefficient_indices": list(REGISTERED_INDICES),
        "registered_audit_count": 1,
        "registered_candidate_id_count": 1,
        "rerun_budget_after_start": 0,
        "terminal_failure_rule": TERMINAL_FAILURE,
        "result_path": RESULT_PATH.as_posix(),
        "terminal_path": TERMINAL_PATH.as_posix(),
    }


def _validate_claim_types_schema(project_root: Path, claim: dict[str, Any]) -> None:
    schema = load_exact_json(project_root / CLAIM_SCHEMA_PATH)
    root_keys = {"additionalProperties", "properties", "required", "schema", "type"}
    if type(schema) is not dict or set(schema) != root_keys:
        raise ValueError("durable claim types schema keys")
    if (schema["schema"] != "HENON_PERIOD3_TYPES_ONLY_DURABLE_CLAIM_SCHEMA_V1"
            or schema["type"] != "object"
            or schema["additionalProperties"] is not False
            or type(schema["properties"]) is not dict
            or type(schema["required"]) is not list
            or any(type(key) is not str for key in schema["required"])
            or len(schema["required"]) != len(set(schema["required"]))
            or set(schema["properties"]) != set(claim)
            or set(schema["required"]) != set(claim)):
        raise ValueError("durable claim types schema closure")
    for key, value in claim.items():
        property_schema = schema["properties"][key]
        if type(property_schema) is not dict or "type" not in property_schema:
            raise ValueError("durable claim property schema")
        expected_type = property_schema["type"]
        if expected_type == "string":
            if set(property_schema) not in ({"type"}, {"pattern", "type"}):
                raise ValueError("durable claim string schema keys")
            if type(value) is not str:
                raise ValueError("durable claim string type")
            pattern = property_schema.get("pattern")
            if pattern is not None and (
                pattern != "^[0-9a-f]{64}$"
                or len(value) != 64
                or any(character not in "0123456789abcdef" for character in value)
            ):
                raise ValueError("durable claim digest pattern")
        elif expected_type == "integer":
            if set(property_schema) != {"type"}:
                raise ValueError("durable claim integer schema keys")
            if type(value) is not int:
                raise ValueError("durable claim integer type")
        elif expected_type == "array":
            if (set(property_schema) != {"items", "maxItems", "minItems", "type"}
                    or type(value) is not list
                    or type(property_schema.get("minItems")) is not int
                    or type(property_schema.get("maxItems")) is not int
                    or len(value) != property_schema["minItems"]
                    or len(value) != property_schema["maxItems"]
                    or property_schema.get("items") != {"type": "integer"}
                    or any(type(item) is not int for item in value)):
                raise ValueError("durable claim array type")
        else:
            raise ValueError("durable claim unsupported schema type")


def claim_registered_audit(
    project_root: Path, claim: dict[str, Any]
) -> dict[str, Any]:
    official = project_root / RUNTIME_ROOT / "official"
    if not regular_directory(official) or list(official.iterdir()):
        raise RuntimeError("official namespace is not fresh")
    _validate_claim_types_schema(project_root, claim)
    write_json_exclusive(project_root / CLAIM_PATH, claim)
    return {
        "claim": claim,
        "claim_sha256": sha256_file(project_root / CLAIM_PATH),
    }


def validate_claim(project_root: Path, expected_claim: dict[str, Any]) -> dict[str, Any]:
    if not regular_file(project_root / CLAIM_PATH):
        return {"errors": ["CLAIM_MISSING"], "status": "REJECTED"}
    claim = validate_canonical_json_file(project_root / CLAIM_PATH)
    errors = [] if exact_same(claim, expected_claim) else ["CLAIM_STALE_OR_NONEXACT"]
    return {
        "claim": claim,
        "claim_sha256": sha256_file(project_root / CLAIM_PATH),
        "errors": errors,
        "status": "VALID" if not errors else "REJECTED",
    }


def commit_result(project_root: Path, result: dict[str, Any]) -> str:
    if regular_file(project_root / RESULT_PATH):
        raise RuntimeError("registered result already exists")
    write_json_exclusive(project_root / RESULT_PATH, result)
    return sha256_file(project_root / RESULT_PATH)


def terminalize(
    project_root: Path,
    manifest: dict[str, Any],
    review_sha256: str,
    expected_claim: dict[str, Any],
    *,
    state: str,
    failure_code: str | None,
) -> str:
    if state not in {TERMINAL_SUCCESS, TERMINAL_FAILURE}:
        raise ValueError("terminal state is not frozen")
    claim = validate_claim(project_root, expected_claim)
    if claim["status"] != "VALID":
        raise RuntimeError("cannot terminalize invalid durable claim")
    result_exists = regular_file(project_root / RESULT_PATH)
    if state == TERMINAL_SUCCESS and not result_exists:
        raise RuntimeError("successful terminal requires a durable result")
    if state == TERMINAL_FAILURE and failure_code is None:
        raise RuntimeError("failed terminal requires a failure code")
    terminal = {
        "schema": "HENON_PERIOD3_DURABLE_TERMINAL_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "R100",
        "state": state,
        "claim_sha256": claim["claim_sha256"],
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "code_tree_sha256": manifest["code_tree_sha256"],
        "deployment_review_sha256": review_sha256,
        "result_path": RESULT_PATH.as_posix() if result_exists else None,
        "result_sha256": sha256_file(project_root / RESULT_PATH) if result_exists else None,
        "failure_code": failure_code,
        "registered_audit_count": 1,
        "rerun_permitted": False,
    }
    write_json_exclusive(project_root / TERMINAL_PATH, terminal)
    return sha256_file(project_root / TERMINAL_PATH)


def official_inventory(project_root: Path) -> list[str]:
    official = project_root / RUNTIME_ROOT / "official"
    if not regular_directory(official):
        return []
    entries = sorted(official.iterdir(), key=lambda path: path.name)
    if any(not regular_file(path) for path in entries):
        raise RuntimeError("official namespace contains an unsafe entry")
    return [path.name for path in entries]
