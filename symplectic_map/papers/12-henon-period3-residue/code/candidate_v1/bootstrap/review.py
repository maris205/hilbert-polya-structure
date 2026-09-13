"""Strict independent-deployment-review authority parser."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CODE_MANIFEST_PATH,
    DEPLOYMENT_REVIEW_PATH,
    JUNIT_PATH,
    PREFLIGHT_PATH,
    PROOF_SHA256,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
)
from .manifest import validate_code_manifest
from .protocol import sha256_file, validate_canonical_json_file


REVIEW_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "reviewer_relation",
        "reviewer_authored_candidate_code",
        "verdict",
        "source_lock_sha256",
        "source_review_sha256",
        "proof_sha256",
        "reviewed_artifacts",
        "reviewed_code_tree_sha256",
        "registered_execution_count_observed",
        "required_checks",
        "blocking_findings",
        "advisories",
    }
)


REQUIRED_CHECKS = (
    "CLOSED_CODE_TREE_AND_AST_DIGESTS",
    "EXACT_IMPORT_DAG_AND_CAPABILITY_CALLSITES",
    "Q_R_SCIENTIFIC_INDEPENDENCE",
    "DEFINITIONS_ONLY_SCHEMA_AND_LEDGER_ISOLATION",
    "QUARTIC_Q_QUOTIENT_AND_R_RESIDUE_COMPLETENESS",
    "REGISTERED_TUPLE_QUARANTINE_AND_NO_EXPECTED_VALUES",
    "P1_P10_WITNESSES_WITHOUT_MACHINE_PROOF_VERDICT",
    "NEGATIVE_CONTROLS_AND_EXTERNAL_PROVENANCE_COUNTERS",
    "DURABLE_ONE_SHOT_FAILURE_CLOSED_LIFECYCLE",
    "STRICT_CANONICAL_JSON_AND_REVIEW_AUTHORITY",
)


def validate_deployment_review(project_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    manifest_validation = validate_code_manifest(project_root)
    if manifest_validation["status"] != "VALID":
        return {"errors": ["CODE_MANIFEST_INVALID"], "status": "REJECTED"}
    manifest = manifest_validation["manifest"]
    review = validate_canonical_json_file(project_root / DEPLOYMENT_REVIEW_PATH)
    if type(review) is not dict or set(review) != REVIEW_KEYS:
        return {"errors": ["DEPLOYMENT_REVIEW_KEYS"], "status": "REJECTED"}
    scalar_expected = {
        "schema": "HENON_PERIOD3_INDEPENDENT_DEPLOYMENT_REVIEW_V1",
        "candidate_id": CANDIDATE_ID,
        "reviewer_relation": "FRESH_INDEPENDENT_NO_BOUND_SOURCE_OR_CODE_AUTHORSHIP",
        "reviewer_authored_candidate_code": False,
        "verdict": "DEPLOYMENT_PASS",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "proof_sha256": PROOF_SHA256,
        "reviewed_code_tree_sha256": manifest["code_tree_sha256"],
        "registered_execution_count_observed": 0,
    }
    for key, expected in scalar_expected.items():
        if type(review[key]) is not type(expected) or review[key] != expected:
            errors.append("DEPLOYMENT_REVIEW_FIELD:" + key)
    artifacts = review["reviewed_artifacts"]
    expected_artifacts = {
        "preexecution/code_manifest.json": sha256_file(project_root / CODE_MANIFEST_PATH),
        "preexecution/junit.xml": sha256_file(project_root / JUNIT_PATH),
        "preexecution/preflight.json": sha256_file(project_root / PREFLIGHT_PATH),
    }
    if type(artifacts) is not dict or artifacts != expected_artifacts:
        errors.append("DEPLOYMENT_REVIEW_ARTIFACT_BINDINGS")
    checks = review["required_checks"]
    if type(checks) is not dict or set(checks) != set(REQUIRED_CHECKS):
        errors.append("DEPLOYMENT_REVIEW_CHECK_SET")
    elif any(checks[key] != "PASS" or type(checks[key]) is not str for key in REQUIRED_CHECKS):
        errors.append("DEPLOYMENT_REVIEW_CHECK_VALUE")
    if type(review["blocking_findings"]) is not list or review["blocking_findings"]:
        errors.append("DEPLOYMENT_REVIEW_BLOCKERS")
    if type(review["advisories"]) is not list:
        errors.append("DEPLOYMENT_REVIEW_ADVISORIES_TYPE")
    return {
        "review": review,
        "review_sha256": sha256_file(project_root / DEPLOYMENT_REVIEW_PATH),
        "code_manifest_sha256": manifest_validation["manifest_sha256"],
        "errors": errors,
        "status": "VALID" if not errors else "REJECTED",
    }
