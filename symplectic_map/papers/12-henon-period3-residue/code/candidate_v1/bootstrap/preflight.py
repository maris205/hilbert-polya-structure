"""Fresh science-free pre-execution evidence collection."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CLAIM_PATH,
    JUNIT_PATH,
    RESULT_MANIFEST_PATH,
    RESULT_PATH,
    RUNTIME_ROOT,
    TERMINAL_PATH,
)
from .contracts import collect_contract_witnesses
from .controls import run_negative_controls
from .manifest import code_tree_sha256, parse_junit, static_code_audit, validate_source_package
from .protocol import regular_file


def collect_preflight(project_root: Path) -> dict[str, Any]:
    source = validate_source_package(project_root)
    code_audit = static_code_audit(project_root / "code")
    junit = parse_junit(project_root / JUNIT_PATH)
    negative_controls = run_negative_controls()
    code_paths = set(code_audit["code_inventory"]["files"])
    contracts = collect_contract_witnesses(project_root, code_paths)
    official_paths = (CLAIM_PATH, RESULT_PATH, TERMINAL_PATH, RESULT_MANIFEST_PATH)
    official_present = [relative.as_posix() for relative in official_paths if regular_file(project_root / relative)]
    runtime_exists = (project_root / RUNTIME_ROOT).exists()
    errors: list[str] = []
    if source["status"] != "VALID":
        errors.append("SOURCE_PACKAGE")
    if code_audit["status"] != "CLEAN":
        errors.append("STATIC_CODE_AUDIT")
    if junit["status"] != "VALID":
        errors.append("JUNIT")
    if len(negative_controls) != 8 or any(
        record["outcome"] != "REJECTED_BEFORE_SCIENTIFIC_DISPATCH"
        for record in negative_controls
    ):
        errors.append("NEGATIVE_CONTROLS")
    if len(contracts) != 10:
        errors.append("CONTRACT_WITNESSES")
    if official_present or runtime_exists:
        errors.append("RUNTIME_OR_OFFICIAL_STATE_PRESENT")
    status = "PREEXECUTION_PASS_REGISTERED_COUNT_ZERO" if not errors else "PREEXECUTION_REJECTED"
    return {
        "schema": "HENON_PERIOD3_PREEXECUTION_PREFLIGHT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_validation": source,
        "code_tree_sha256": code_tree_sha256(project_root / "code"),
        "static_code_audit": code_audit,
        "junit": junit,
        "contract_witnesses": contracts,
        "negative_controls": negative_controls,
        "registered_audit_count": 0,
        "registered_coefficient_evaluation_count": 0,
        "historical_m2_m7_result_access_count": 0,
        "historical_source_stage_diagnostic_used_as_evidence_count": 0,
        "machine_source_proof_verdict_count": 0,
        "network_access_count": code_audit["science_capability_category_counts"]["network"],
        "floating_field_count": code_audit["science_capability_category_counts"]["floating"],
        "runtime_root_present": runtime_exists,
        "official_artifacts_present": official_present,
        "disclosed_source_stage_diagnostic": {
            "indices": [2, 3, 4, 5, 6, 7],
            "registered": False,
            "evidentiary": False,
            "values_retained": False,
            "candidate_runtime_access": False,
        },
        "errors": errors,
        "status": status,
    }
