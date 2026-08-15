"""Dual-tree one-shot manifest build and strict read-only final closure."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .audit import collect_analyzer_audit
from .constants import (
    ANALYZER_JUNIT_PATH,
    ANALYZER_REVIEW_PATH,
    CANDIDATE_ID,
    EXECUTION_TREE_SHA256,
    FINAL_RESULT_FILES,
    FIRST_MANIFEST_ATTEMPT,
    IMMUTABLE_ARTIFACTS,
    MANIFEST_RECORD_PATHS,
    PREWRITE_RESULT_FILES,
    RESULT_MANIFEST_PATH,
    SOURCE_LOCK_SHA256,
    TERMINAL_CLASSIFICATION,
)
from .protocol import (
    canonical_json_bytes,
    load_exact_json,
    pretty_json_bytes,
    regular_file,
    result_inventory,
    sha256_file,
    stable_file_bytes,
    write_pretty_json_exclusive,
)


MANIFEST_SCHEMA = "EQUIVARIANT_CLOCK_RESULT_MANIFEST_V2_DUAL_TREE"
MANIFEST_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "classification",
        "execution_tree",
        "analyzer_tree",
        "immutable_execution_hashes",
        "junit_provenance",
        "first_manifest_attempt",
        "postrun_analyzer_audit",
        "result_inventory",
        "files",
        "registered_audit_count",
        "candidate_numerical_run_count",
        "candidate_rerun_performed",
        "errors",
        "pass",
    }
)


def _manifest_file_records(project_root: Path) -> tuple[list[dict[str, str]], list[str]]:
    root = Path(project_root).absolute()
    records: list[dict[str, str]] = []
    errors: list[str] = []
    for relative in MANIFEST_RECORD_PATHS:
        path = root / relative
        if not regular_file(path):
            errors.append("MANIFEST_INPUT_MISSING_OR_UNSAFE:" + relative)
        else:
            records.append({"path": relative, "sha256": sha256_file(path)})
    return records, errors


def _compose_manifest(
    project_root: Path, *, expected_result_files: frozenset[str]
) -> dict[str, Any]:
    root = Path(project_root).absolute()
    audit = collect_analyzer_audit(root)
    inventory_gate = result_inventory(root, expected_result_files)
    files, file_errors = _manifest_file_records(root)
    errors = list(file_errors)
    if audit.get("pass") is not True:
        errors.append("POSTRUN_ANALYZER_BASE_GATES_FAILED")
    if audit.get("status") != "AUTHORIZED_FOR_POSTRUN_MANIFEST_V2":
        errors.append("INDEPENDENT_POSTRUN_ANALYZER_REVIEW_MISSING_OR_STALE")
    if audit.get("independent_analyzer_review", {}).get("pass") is not True:
        errors.append("INDEPENDENT_POSTRUN_ANALYZER_REVIEW_NOT_PASSING")
    errors.extend(inventory_gate["errors"])
    analyzer_review = audit.get("independent_analyzer_review", {})
    analyzer_junit = audit.get("base_gates", {}).get("analyzer_junit", {})
    return {
        "schema": MANIFEST_SCHEMA,
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "classification": TERMINAL_CLASSIFICATION,
        "execution_tree": {
            "sha256": EXECUTION_TREE_SHA256,
            "role": "IMMUTABLE_REGISTERED_CANDIDATE_EXECUTION",
            "deployment_authority_path": "results/CODE_REVIEW.md",
            "deployment_authority_sha256": IMMUTABLE_ARTIFACTS[
                "results/CODE_REVIEW.md"
            ][0],
            "result_authority_path": "results/INDEPENDENT_RESULT_INTEGRITY.md",
            "result_authority_sha256": IMMUTABLE_ARTIFACTS[
                "results/INDEPENDENT_RESULT_INTEGRITY.md"
            ][0],
        },
        "analyzer_tree": {
            "sha256": audit.get("analyzer_tree_sha256"),
            "role": "POSTRUN_VALIDATOR_ONLY_NO_CANDIDATE_AUTHORITY",
            "authority_path": ANALYZER_REVIEW_PATH,
            "authority_sha256": analyzer_review.get("review_file_sha256"),
            "junit_path": ANALYZER_JUNIT_PATH,
            "junit_sha256": analyzer_junit.get("sha256"),
        },
        "immutable_execution_hashes": {
            relative: digest for relative, (digest, _) in sorted(IMMUTABLE_ARTIFACTS.items())
        },
        "junit_provenance": {
            "execution_authorization": {
                "path": "results/PRE_EXECUTION_TESTS.xml",
                "sha256": IMMUTABLE_ARTIFACTS["results/PRE_EXECUTION_TESTS.xml"][0],
                "role": "DEPLOYMENT_AUTHORIZATION_EVIDENCE",
            },
            "execution_postrun": {
                "path": "results/POSTRUN_TESTS.xml",
                "sha256": IMMUTABLE_ARTIFACTS["results/POSTRUN_TESTS.xml"][0],
                "role": "IMMUTABLE_POSTRUN_EXECUTION_EVIDENCE",
            },
            "postrun_analyzer": {
                "path": ANALYZER_JUNIT_PATH,
                "sha256": analyzer_junit.get("sha256"),
                "role": "SEPARATE_ANALYZER_TREE_EVIDENCE",
            },
        },
        "first_manifest_attempt": FIRST_MANIFEST_ATTEMPT,
        "postrun_analyzer_audit": audit,
        "result_inventory": {
            "prewrite_files": sorted(PREWRITE_RESULT_FILES),
            "final_files": sorted(FINAL_RESULT_FILES),
            "manifest_path": RESULT_MANIFEST_PATH,
            "manifest_in_final_inventory": True,
            "manifest_self_hash_recorded": False,
            "nonself_hash_records": list(MANIFEST_RECORD_PATHS),
        },
        "files": files,
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
        "candidate_rerun_performed": False,
        "errors": sorted(set(errors)),
        "pass": not errors,
    }


def build_manifest(project_root: Path) -> dict[str, Any]:
    """Compose only against the exact authorized pre-write inventory."""

    return _compose_manifest(
        Path(project_root).absolute(), expected_result_files=PREWRITE_RESULT_FILES
    )


def validate_existing_manifest(project_root: Path) -> dict[str, Any]:
    """Read-only validation of exact final inventory and stored V2 semantics."""

    root = Path(project_root).absolute()
    manifest_path = root / RESULT_MANIFEST_PATH
    inventory_gate = result_inventory(root, FINAL_RESULT_FILES)
    errors = list(inventory_gate["errors"])
    raw: bytes | None = None
    stored: Any = None
    if not regular_file(manifest_path):
        errors.append("RESULT_MANIFEST_MISSING_OR_UNSAFE")
    else:
        try:
            first = stable_file_bytes(manifest_path)
            parsed = load_exact_json(manifest_path)
            second = stable_file_bytes(manifest_path)
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError, TypeError):
            errors.append("RESULT_MANIFEST_STRICT_JSON_INVALID")
        else:
            raw = first
            stored = parsed
            if first != second:
                errors.append("RESULT_MANIFEST_BYTES_UNSTABLE")
            if first != pretty_json_bytes(parsed):
                errors.append("RESULT_MANIFEST_BYTES_NOT_CANONICAL")
    if type(stored) is not dict:
        errors.append("RESULT_MANIFEST_NOT_OBJECT")
    elif set(stored) != MANIFEST_KEYS:
        errors.append("RESULT_MANIFEST_KEYS_NOT_EXACT")
    else:
        records = stored.get("files")
        paths: list[str] = []
        if type(records) is not list:
            errors.append("RESULT_MANIFEST_FILES_NOT_LIST")
        else:
            for record in records:
                if (
                    type(record) is not dict
                    or set(record) != {"path", "sha256"}
                    or type(record.get("path")) is not str
                    or type(record.get("sha256")) is not str
                ):
                    errors.append("RESULT_MANIFEST_FILE_RECORD_INVALID")
                else:
                    paths.append(record["path"])
            if len(paths) != len(set(paths)):
                errors.append("RESULT_MANIFEST_FILE_PATH_DUPLICATE")
            if RESULT_MANIFEST_PATH in paths:
                errors.append("RESULT_MANIFEST_SELF_HASH_FORBIDDEN")
            if set(paths) != set(MANIFEST_RECORD_PATHS) or len(paths) != len(
                MANIFEST_RECORD_PATHS
            ):
                errors.append("RESULT_MANIFEST_NONSELF_PATHS_NOT_EXACT")
        expected_inventory_contract = {
            "prewrite_files": sorted(PREWRITE_RESULT_FILES),
            "final_files": sorted(FINAL_RESULT_FILES),
            "manifest_path": RESULT_MANIFEST_PATH,
            "manifest_in_final_inventory": True,
            "manifest_self_hash_recorded": False,
            "nonself_hash_records": list(MANIFEST_RECORD_PATHS),
        }
        if canonical_json_bytes(stored.get("result_inventory")) != canonical_json_bytes(
            expected_inventory_contract
        ):
            errors.append("RESULT_MANIFEST_INVENTORY_CONTRACT_NOT_EXACT")
        try:
            recomputed = _compose_manifest(
                root, expected_result_files=FINAL_RESULT_FILES
            )
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError, TypeError, KeyError):
            recomputed = None
            errors.append("RESULT_MANIFEST_LIVE_RECOMPUTATION_FAILED")
        if type(recomputed) is not dict or recomputed.get("pass") is not True:
            errors.append("RESULT_MANIFEST_LIVE_CLOSURE_NOT_PASSING")
        elif canonical_json_bytes(stored) != canonical_json_bytes(recomputed):
            errors.append("RESULT_MANIFEST_STORED_SEMANTICS_STALE_OR_TAMPERED")
    return {
        "stage": "R130_FINAL_RESULT_MANIFEST_CLOSURE",
        "manifest_path": RESULT_MANIFEST_PATH,
        "manifest_sha256": hashlib.sha256(raw).hexdigest() if raw is not None else None,
        "observed_result_files": inventory_gate["observed"],
        "errors": sorted(set(errors)),
        "pass": not errors,
    }


def write_manifest(project_root: Path) -> Path:
    root = Path(project_root).absolute()
    output = root / RESULT_MANIFEST_PATH
    if output.exists():
        raise FileExistsError("result manifest V2 is one-shot and already exists")
    payload = build_manifest(root)
    if payload.get("pass") is not True:
        raise RuntimeError("strict dual-tree post-run manifest gates failed")
    write_pretty_json_exclusive(output, payload)
    closure = validate_existing_manifest(root)
    if closure.get("pass") is not True:
        raise RuntimeError("written result manifest failed strict final closure")
    return output
