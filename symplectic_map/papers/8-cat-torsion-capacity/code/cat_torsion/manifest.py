"""Strict safe-preflight, registered-result, JUnit, and post-run closure."""

from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from .algebra import LOCKED_LEDGER, LOCKED_SUPPORT, frozen_ledger_records
from .controls import run_all_controls
from .finite_field import EXPECTED_PERIOD_PROFILES
from .lifecycle import (
    CLAIM_KEYS,
    CLAIM_RELATIVE,
    REGISTERED_PERIODS,
    TERMINAL_KEYS,
    TERMINAL_RELATIVE,
)
from .proof_contract import audit_proof_contract
from .protocol import (
    CANDIDATE_ID,
    EXPECTED_EXECUTION_TREE_SHA256,
    EXPECTED_LOCK_SHA256,
    _raw_absolute,
    canonical_json_bytes,
    executable_isolation_scan,
    load_exact_json,
    regular_file,
    safe_directory_entries,
    sha256_file,
    stable_file_bytes,
    strict_json_loads,
    validate_source_lock,
    validate_upstream_bindings,
    write_json,
)
from .review_gate import (
    reviewed_code_tree_sha256,
    validate_execution_review_authority,
    validate_postrun_analyzer_authority,
    validate_review_authority,
)


REQUIRED_JUNIT_TESTS = {
    "test_scanner_blocks_alias_named_container_and_path_laundering",
    "test_scanner_rejects_symlink_hardlink_and_extra_file",
    "test_review_authority_is_exact_canonical_and_stale_closed",
    "test_registered_claim_is_one_shot",
    "test_manifest_rejects_nested_forgery",
    "test_fixed_cli_has_no_scientific_overrides",
}
REQUIRED_ANALYZER_JUNIT_TESTS = REQUIRED_JUNIT_TESTS | {
    "test_dual_tree_junit_roles_allow_hash_change_but_not_malformed_evidence",
    "test_existing_postrun_manifest_rejects_changed_missing_extra_symlink_and_json_tampering",
    "test_execution_chain_rejects_malformed_preflight_and_claim",
    "test_postrun_analyzer_authority_is_stale_closed",
    "test_postrun_manifest_write_is_one_shot_and_finally_closed",
    "test_postrun_official_preflight_is_immutable",
}
EXPECTED_RAW_HASHES = {
    "code_review_sha256": "0fe0a5ba625cbbb88bd6ed6a8ff61389a916fd300127a244981fa4643ffa25a6",
    "pre_execution_audit_sha256": "850cb7cd8eb3ca63dd4e54757e569a66e01f190db0980c8d9682f4931d711883",
    "registered_claim_sha256": "14b06403bd5a23b533138ccec4962d74910e6e0242abfcf7ac5fe6b3a947a0ee",
    "experiment_results_sha256": "0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0",
    "registered_terminal_sha256": "b3a40e9db554ffdc9fe14b654d84f8e918f26fdb47025eb301337b3ecd5fa192",
    "execution_postrun_junit_sha256": "2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc",
}
EXPECTED_PRE_EXECUTION_JUNIT_SHA256 = (
    "81ffc571c773cfa9a69f157559fdaa3611f55c748908c20183e4eae3f3420aa1"
)
GATE_KEYS = {
    "source_lock",
    "upstream_bindings",
    "executable_isolation",
    "proof_contract",
    "controls",
    "test_evidence",
}
GATE_STAGES = {
    "source_lock": "P0_SOURCE_LOCK",
    "upstream_bindings": "P0_UPSTREAM_BINDINGS",
    "executable_isolation": "P0_EXECUTABLE_ISOLATION",
    "proof_contract": "P1_PROOF_CONTRACT",
    "controls": "P2_CONTROLS_ONLY",
    "test_evidence": "P2_TEST_EVIDENCE",
}
PRE_EXECUTION_KEYS = {
    "schema",
    "candidate_id",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "gates",
    "independent_review",
    "registered_exact_audits",
    "registered_periods_executed",
    "candidate_numerical_runs",
    "external_prime_tables_accessed",
    "generated_prime_target_arrays",
    "riemann_zero_data_accessed",
    "floating_or_approximate_matching_used",
    "status",
    "pass",
}
RESULT_KEYS = {
    "schema",
    "candidate_id",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "registered_claim_sha256",
    "registered_periods",
    "ledger_records",
    "finite_field_records",
    "boundary_summary",
    "general_theorem_contract",
    "clock_specificity",
    "registered_run_count",
    "registered_exact_audits",
    "candidate_numerical_runs",
    "external_prime_tables_accessed",
    "generated_prime_target_arrays",
    "riemann_zero_data_accessed",
    "floating_or_approximate_matching_used",
    "periods_above_twelve_computed",
    "classification",
    "route_a",
    "route_b",
    "pass",
    "pre_execution_gates",
    "independent_review_gate",
}


def parse_passing_junit(
    path: Path,
    *,
    required_tests: set[str] | None = None,
    stage: str = "P2_TEST_EVIDENCE",
    display_path: str = "results/pytest.xml",
) -> dict[str, Any]:
    selected_tests = REQUIRED_JUNIT_TESTS if required_tests is None else required_tests
    if not regular_file(path):
        return {
            "stage": stage,
            "path": display_path,
            "errors": ["JUNIT_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    raw = stable_file_bytes(path)
    errors: list[str] = []
    lowered = raw.lower()
    if b"<!doctype" in lowered or b"<!entity" in lowered:
        errors.append("JUNIT_DTD_OR_ENTITY_FORBIDDEN")
    names: list[str] = []
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    if not errors:
        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            errors.append("JUNIT_XML_MALFORMED")
        else:
            suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
            if not suites:
                errors.append("JUNIT_NO_TESTSUITE")
            for suite in suites:
                for key in totals:
                    raw_count = suite.attrib.get(key, "0")
                    if not raw_count.isdecimal():
                        errors.append("JUNIT_NONINTEGER_COUNT")
                        continue
                    totals[key] += int(raw_count)
                for case in suite.iter("testcase"):
                    name = case.attrib.get("name")
                    if type(name) is str:
                        names.append(name)
            if totals["tests"] != len(names):
                errors.append("JUNIT_DECLARED_TEST_COUNT_MISMATCH")
            if totals["tests"] <= 0:
                errors.append("JUNIT_EMPTY")
            if any(totals[key] != 0 for key in ("failures", "errors", "skipped")):
                errors.append("JUNIT_NOT_ALL_PASSING")
            missing = sorted(selected_tests.difference(names))
            if missing:
                errors.append("JUNIT_REQUIRED_SECURITY_TESTS_MISSING")
    return {
        "stage": stage,
        "path": display_path,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "totals": totals,
        "required_tests": sorted(selected_tests),
        "observed_required_tests": sorted(selected_tests.intersection(names)),
        "errors": errors,
        "pass": not errors,
    }


def collect_safe_preflight(project_root: Path) -> dict[str, Any]:
    """Collect only safe P0--P3 gates; never import the candidate module."""

    project_root = _raw_absolute(project_root)
    gates = {
        "source_lock": validate_source_lock(project_root),
        "upstream_bindings": validate_upstream_bindings(project_root),
        "executable_isolation": executable_isolation_scan(project_root / "code"),
        "proof_contract": audit_proof_contract(project_root),
        "controls": run_all_controls(project_root),
        "test_evidence": parse_passing_junit(project_root / "results" / "pytest.xml"),
    }
    safe_pass = (
        set(gates) == GATE_KEYS
        and all(
            type(gates[key]) is dict
            and gates[key].get("stage") == GATE_STAGES[key]
            and gates[key].get("pass") is True
            for key in GATE_KEYS
        )
    )
    review = validate_review_authority(project_root)
    status = (
        "AUTHORIZED_FOR_REGISTERED_EXECUTION"
        if safe_pass and review.get("pass") is True
        else "READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW"
        if safe_pass
        else "SAFE_PREFLIGHT_FAILED"
    )
    return {
        "schema": "CAT_TORSION_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_tree_sha256(project_root),
        "gates": gates,
        "independent_review": review,
        "registered_exact_audits": 0,
        "registered_periods_executed": [],
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "status": status,
        "pass": safe_pass,
    }


def write_safe_preflight(project_root: Path, output_root: Path | None = None) -> Path:
    project_root = _raw_absolute(project_root)
    output = _raw_absolute(output_root or project_root / "results")
    path = output / "PRE_EXECUTION_AUDIT.json"
    if output == project_root / "results" and any(
        regular_file(project_root / relative)
        for relative in (
            CLAIM_RELATIVE,
            "results/EXPERIMENT_RESULTS.json",
            TERMINAL_RELATIVE,
        )
    ):
        raise RuntimeError("claim-bound official preflight is immutable after registered execution")
    write_json(path, collect_safe_preflight(project_root))
    return path


def validate_official_preflight(official: Any, live: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if type(official) is not dict or set(official) != PRE_EXECUTION_KEYS:
        return ["OFFICIAL_PREFLIGHT_KEYS_NOT_EXACT"]
    if canonical_json_bytes(official) != canonical_json_bytes(live):
        errors.append("OFFICIAL_PREFLIGHT_NOT_LIVE_CANONICAL_SNAPSHOT")
    if official.get("pass") is not True:
        errors.append("OFFICIAL_PREFLIGHT_SAFE_GATES_NOT_PASSING")
    if official.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        errors.append("OFFICIAL_PREFLIGHT_NOT_AUTHORIZED")
    if official.get("registered_exact_audits") != 0:
        errors.append("OFFICIAL_PREFLIGHT_RUN_COUNT_NOT_ZERO")
    if official.get("registered_periods_executed") != []:
        errors.append("OFFICIAL_PREFLIGHT_PERIODS_NOT_EMPTY")
    return errors


def validate_embedded_execution_junit_gate(value: Any) -> dict[str, Any]:
    """Validate the pre-run JUnit record embedded in the claim-bound preflight."""

    errors: list[str] = []
    expected_keys = {
        "stage",
        "path",
        "sha256",
        "totals",
        "required_tests",
        "observed_required_tests",
        "errors",
        "pass",
    }
    if type(value) is not dict or set(value) != expected_keys:
        return {"errors": ["EMBEDDED_EXECUTION_JUNIT_KEYS_NOT_EXACT"], "pass": False}
    expected_totals = {"tests": 21, "failures": 0, "errors": 0, "skipped": 0}
    if value["stage"] != "P2_TEST_EVIDENCE" or value["path"] != "results/pytest.xml":
        errors.append("EMBEDDED_EXECUTION_JUNIT_ROLE_MISMATCH")
    if value["sha256"] != EXPECTED_PRE_EXECUTION_JUNIT_SHA256:
        errors.append("EMBEDDED_EXECUTION_JUNIT_HASH_MISMATCH")
    if value["totals"] != expected_totals or any(
        type(item) is not int for item in value["totals"].values()
    ):
        errors.append("EMBEDDED_EXECUTION_JUNIT_TOTALS_MISMATCH")
    if value["required_tests"] != sorted(REQUIRED_JUNIT_TESTS):
        errors.append("EMBEDDED_EXECUTION_JUNIT_REQUIRED_TESTS_MISMATCH")
    if value["observed_required_tests"] != sorted(REQUIRED_JUNIT_TESTS):
        errors.append("EMBEDDED_EXECUTION_JUNIT_OBSERVED_TESTS_MISMATCH")
    if value["errors"] != [] or value["pass"] is not True:
        errors.append("EMBEDDED_EXECUTION_JUNIT_NOT_PASSING")
    return {"errors": errors, "pass": not errors}


def validate_junit_role_separation(
    execution_gate: Any, postrun_report: Any
) -> dict[str, Any]:
    """Keep immutable pre-run and live post-run JUnit evidence in distinct roles."""

    execution = validate_embedded_execution_junit_gate(execution_gate)
    errors = list(execution["errors"])
    if type(postrun_report) is not dict or postrun_report.get("pass") is not True:
        errors.append("POSTRUN_EXECUTION_JUNIT_NOT_PASSING")
    else:
        if postrun_report.get("stage") != "R091_EXECUTION_TREE_POSTRUN_TEST_EVIDENCE":
            errors.append("POSTRUN_EXECUTION_JUNIT_STAGE_MISMATCH")
        if postrun_report.get("path") != "results/pytest.xml":
            errors.append("POSTRUN_EXECUTION_JUNIT_PATH_MISMATCH")
        if postrun_report.get("sha256") != EXPECTED_RAW_HASHES[
            "execution_postrun_junit_sha256"
        ]:
            errors.append("POSTRUN_EXECUTION_JUNIT_HASH_MISMATCH")
        if postrun_report.get("totals") != {
            "tests": 21,
            "failures": 0,
            "errors": 0,
            "skipped": 0,
        }:
            errors.append("POSTRUN_EXECUTION_JUNIT_TOTALS_MISMATCH")
    execution_hash = execution_gate.get("sha256") if type(execution_gate) is dict else None
    postrun_hash = postrun_report.get("sha256") if type(postrun_report) is dict else None
    if execution_hash == postrun_hash:
        errors.append("JUNIT_ROLES_AMBIGUOUS_IDENTICAL_HASH")
    return {
        "execution_authorization_junit": {
            "role": "CLAIM_BOUND_PRE_EXECUTION_GATE_RECORD",
            "sha256": execution_hash,
        },
        "execution_postrun_junit": {
            "role": "LIVE_POST_EXECUTION_TEST_RECORD",
            "sha256": postrun_hash,
        },
        "content_changed_after_execution": execution_hash != postrun_hash,
        "errors": errors,
        "pass": not errors,
    }


def validate_execution_chain_payloads(
    preflight: Any,
    claim: Any,
    result: Any,
    terminal: Any,
    observed_hashes: Any,
) -> dict[str, Any]:
    """Validate immutable execution artifacts without consulting the analyzer tree."""

    errors: list[str] = []
    if type(observed_hashes) is not dict or set(observed_hashes) != set(EXPECTED_RAW_HASHES):
        errors.append("RAW_HASH_KEYS_NOT_EXACT")
    elif observed_hashes != EXPECTED_RAW_HASHES:
        errors.append("IMMUTABLE_RAW_HASH_MISMATCH")
    if type(preflight) is not dict or set(preflight) != PRE_EXECUTION_KEYS:
        errors.append("EXECUTION_PREFLIGHT_KEYS_NOT_EXACT")
    if type(claim) is not dict or set(claim) != CLAIM_KEYS:
        errors.append("EXECUTION_CLAIM_KEYS_NOT_EXACT")
    if type(result) is not dict or set(result) != RESULT_KEYS:
        errors.append("EXECUTION_RESULT_KEYS_NOT_EXACT")
    if type(terminal) is not dict or set(terminal) != TERMINAL_KEYS:
        errors.append("EXECUTION_TERMINAL_KEYS_NOT_EXACT")
    if errors:
        return {"errors": errors, "pass": False}
    expected_preflight = {
        "schema": "CAT_TORSION_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "registered_exact_audits": 0,
        "registered_periods_executed": [],
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
        "pass": True,
    }
    for key, expected in expected_preflight.items():
        if preflight[key] != expected or type(preflight[key]) is not type(expected):
            errors.append("EXECUTION_PREFLIGHT_" + key.upper() + "_MISMATCH")
    gates = preflight["gates"]
    if (
        type(gates) is not dict
        or set(gates) != GATE_KEYS
        or any(
            type(gates.get(key)) is not dict
            or gates[key].get("stage") != GATE_STAGES[key]
            or gates[key].get("pass") is not True
            for key in GATE_KEYS
        )
    ):
        errors.append("EXECUTION_PREFLIGHT_GATES_NOT_EXACT_PASSING_SET")
    else:
        errors.extend(validate_embedded_execution_junit_gate(gates["test_evidence"])["errors"])
    review = preflight["independent_review"]
    authority = review.get("authority") if type(review) is dict else None
    if (
        type(review) is not dict
        or review.get("pass") is not True
        or review.get("reviewed_code_sha256") != EXPECTED_EXECUTION_TREE_SHA256
        or type(authority) is not dict
        or authority.get("reviewed_code_sha256") != EXPECTED_EXECUTION_TREE_SHA256
        or authority.get("source_lock_sha256") != EXPECTED_LOCK_SHA256
        or authority.get("candidate_id") != CANDIDATE_ID
        or authority.get("reviewer_independent") is not True
        or authority.get("verdict") != "DEPLOYMENT_PASS"
    ):
        errors.append("EXECUTION_PREFLIGHT_REVIEW_AUTHORITY_MISMATCH")
    expected_claim = {
        "schema": "CAT_TORSION_REGISTERED_RUN_CLAIM_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "STARTED",
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "review_file_sha256": EXPECTED_RAW_HASHES["code_review_sha256"],
        "pre_execution_audit_path": "results/PRE_EXECUTION_AUDIT.json",
        "pre_execution_audit_sha256": EXPECTED_RAW_HASHES[
            "pre_execution_audit_sha256"
        ],
        "registered_periods": REGISTERED_PERIODS,
        "result_path": "results/EXPERIMENT_RESULTS.json",
        "terminal_path": TERMINAL_RELATIVE,
        "registered_run_count": 1,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
    }
    for key, expected in expected_claim.items():
        if claim[key] != expected or type(claim[key]) is not type(expected):
            errors.append("EXECUTION_CLAIM_" + key.upper() + "_MISMATCH")
    if result["reviewed_code_sha256"] != EXPECTED_EXECUTION_TREE_SHA256:
        errors.append("EXECUTION_RESULT_TREE_SHA256_MISMATCH")
    if result["registered_claim_sha256"] != EXPECTED_RAW_HASHES["registered_claim_sha256"]:
        errors.append("EXECUTION_RESULT_CLAIM_LINK_MISMATCH")
    if canonical_json_bytes(result["pre_execution_gates"]) != canonical_json_bytes(
        preflight["gates"]
    ):
        errors.append("EXECUTION_RESULT_PREFLIGHT_GATE_LINK_MISMATCH")
    if canonical_json_bytes(result["independent_review_gate"]) != canonical_json_bytes(
        preflight["independent_review"]
    ):
        errors.append("EXECUTION_RESULT_REVIEW_GATE_LINK_MISMATCH")
    expected_terminal = {
        "schema": "CAT_TORSION_REGISTERED_RUN_TERMINAL_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "COMPLETED_CERTIFIED",
        "claim_path": CLAIM_RELATIVE,
        "claim_sha256": EXPECTED_RAW_HASHES["registered_claim_sha256"],
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "review_file_sha256": EXPECTED_RAW_HASHES["code_review_sha256"],
        "pre_execution_audit_sha256": EXPECTED_RAW_HASHES[
            "pre_execution_audit_sha256"
        ],
        "registered_periods": REGISTERED_PERIODS,
        "periods_started": REGISTERED_PERIODS,
        "periods_completed": REGISTERED_PERIODS,
        "artifact_path": "results/EXPERIMENT_RESULTS.json",
        "artifact_sha256": EXPECTED_RAW_HASHES["experiment_results_sha256"],
        "classification": "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH",
        "failure_code": None,
        "registered_run_count": 1,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
    }
    for key, expected in expected_terminal.items():
        if terminal[key] != expected or type(terminal[key]) is not type(expected):
            errors.append("EXECUTION_TERMINAL_" + key.upper() + "_MISMATCH")
    return {"errors": errors, "pass": not errors}


def validate_immutable_execution_chain(project_root: Path) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    paths = {
        "code_review_sha256": project_root / "results" / "CODE_REVIEW.md",
        "pre_execution_audit_sha256": project_root / "results" / "PRE_EXECUTION_AUDIT.json",
        "registered_claim_sha256": project_root / CLAIM_RELATIVE,
        "experiment_results_sha256": project_root / "results" / "EXPERIMENT_RESULTS.json",
        "registered_terminal_sha256": project_root / TERMINAL_RELATIVE,
        "execution_postrun_junit_sha256": project_root / "results" / "pytest.xml",
    }
    unsafe = sorted(key for key, path in paths.items() if not regular_file(path))
    if unsafe:
        return {
            "stage": "R090_IMMUTABLE_EXECUTION_CHAIN",
            "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
            "observed_hashes": {},
            "errors": ["IMMUTABLE_EXECUTION_ARTIFACT_MISSING_OR_UNSAFE:" + key for key in unsafe],
            "pass": False,
        }
    observed = {key: sha256_file(path) for key, path in paths.items()}
    preflight = load_exact_json(paths["pre_execution_audit_sha256"])
    claim = load_exact_json(paths["registered_claim_sha256"])
    result = load_exact_json(paths["experiment_results_sha256"])
    terminal = load_exact_json(paths["registered_terminal_sha256"])
    payload_validation = validate_execution_chain_payloads(
        preflight, claim, result, terminal, observed
    )
    execution_review = validate_execution_review_authority(project_root)
    errors = list(payload_validation["errors"])
    if execution_review.get("pass") is not True:
        errors.append("IMMUTABLE_EXECUTION_REVIEW_AUTHORITY_INVALID")
    return {
        "stage": "R090_IMMUTABLE_EXECUTION_CHAIN",
        "execution_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "observed_hashes": observed,
        "payload_validation": payload_validation,
        "execution_review": execution_review,
        "errors": errors,
        "pass": not errors,
    }


def _expected_registered_ledger() -> list[dict[str, Any]]:
    records = frozen_ledger_records()
    for record in records:
        record["evidentiary_role"] = "DEVELOPMENT_SEEN_PRIMARY_LITERATURE_REPRODUCTION"
    return records


def validate_registered_result(payload: Any, project_root: Path) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    errors: list[str] = []
    if type(payload) is not dict or set(payload) != RESULT_KEYS:
        return {"errors": ["RESULT_KEYS_NOT_EXACT"], "pass": False}
    exact_scalars = {
        "schema": "CAT_TORSION_REGISTERED_EXACT_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "registered_periods": REGISTERED_PERIODS,
        "registered_run_count": 1,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "periods_above_twelve_computed": [],
        "classification": "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH",
        "route_a": "A0_FAIL_PROVES_TOO_MUCH_NO_A1_TO_A4",
        "route_b": "NOT_OPENED",
        "pass": True,
    }
    for key, expected in exact_scalars.items():
        if payload[key] != expected or type(payload[key]) is not type(expected):
            errors.append(key.upper() + "_MISMATCH")
    expected_ledger = _expected_registered_ledger()
    if canonical_json_bytes(payload["ledger_records"]) != canonical_json_bytes(expected_ledger):
        errors.append("REGISTERED_LEDGER_SEMANTICS_MISMATCH")
    finite = payload["finite_field_records"]
    if type(finite) is not list or len(finite) != len(LOCKED_SUPPORT):
        errors.append("FINITE_FIELD_RECORD_COUNT_MISMATCH")
    else:
        for prime, record in zip(LOCKED_SUPPORT, finite, strict=True):
            expected_profile = {
                str(key): value for key, value in EXPECTED_PERIOD_PROFILES[prime].items()
            }
            if type(record) is not dict or set(record) != {
                "prime",
                "period_profile",
                "expected_period_profile",
                "nonzero_vector_count",
                "matches_locked_profile",
            }:
                errors.append(f"P{prime}:FINITE_RECORD_KEYS_NOT_EXACT")
            elif not (
                type(record["prime"]) is int
                and record["prime"] == prime
                and record["period_profile"] == expected_profile
                and record["expected_period_profile"] == expected_profile
                and type(record["nonzero_vector_count"]) is int
                and record["nonzero_vector_count"] == prime * prime - 1
                and record["matches_locked_profile"] is True
            ):
                errors.append(f"P{prime}:FINITE_RECORD_SEMANTICS_MISMATCH")
    boundary = payload["boundary_summary"]
    expected_boundary = {
        "profiles": {
            str(prime): {
                str(period): count
                for period, count in EXPECTED_PERIOD_PROFILES[prime].items()
            }
            for prime in LOCKED_SUPPORT
        },
        "jordan_period_ten_points": 20,
        "jordan_period_ten_cycles": 2,
        "period_1_carriers": 0,
        "period_6_carriers": 0,
        "period_10_carriers": 20,
        "period_12_carriers": 0,
        "exception_set": [1, 6, 12],
    }
    if canonical_json_bytes(boundary) != canonical_json_bytes(expected_boundary):
        errors.append("BOUNDARY_CLASSIFICATION_MISMATCH")
    theorem = payload["general_theorem_contract"]
    if (
        type(theorem) is not dict
        or theorem.get("tail_periods_computed") != []
        or theorem.get("tail_evidence")
        != "IMPORTED_THEOREM_PLUS_SEPARATE_PARITY_PROOF_ONLY"
        or any(
            type(theorem.get(key)) is not dict or theorem[key].get("pass") is not True
            for key in ("norm_determinant", "primitive_kernel", "negative_trace_parity")
        )
    ):
        errors.append("GENERAL_THEOREM_CONTRACT_MISMATCH")
    clock = payload["clock_specificity"]
    if (
        type(clock) is not dict
        or clock.get("range") != "ALL_POSITIVE_INTEGERS_PRIME_AND_COMPOSITE"
        or clock.get("regularity")
        != "UNBOUNDED_AND_DISCONTINUOUS_IN_EVERY_TORSION_NEIGHBORHOOD"
        or clock.get("native_monodromy") != "PERIOD_DEPENDENT_TORSION_ORDER_BLIND"
        or type(clock.get("all_order_witnesses")) is not list
        or not clock["all_order_witnesses"]
        or not all(item.get("pass") is True for item in clock["all_order_witnesses"])
        or type(clock.get("discontinuity_witnesses")) is not list
        or not clock["discontinuity_witnesses"]
        or not all(item.get("pass") is True for item in clock["discontinuity_witnesses"])
        or type(clock.get("orbit_sum_monodromy")) is not dict
        or clock["orbit_sum_monodromy"].get("pass") is not True
    ):
        errors.append("CLOCK_SPECIFICITY_CONTRACT_MISMATCH")
    claim_path = project_root / CLAIM_RELATIVE
    if not regular_file(claim_path) or payload["registered_claim_sha256"] != sha256_file(claim_path):
        errors.append("REGISTERED_CLAIM_HASH_MISMATCH")
    preflight_path = project_root / "results" / "PRE_EXECUTION_AUDIT.json"
    if not regular_file(preflight_path):
        errors.append("CLAIM_BOUND_PREFLIGHT_MISSING_OR_UNSAFE")
    else:
        preflight = load_exact_json(preflight_path)
        if type(preflight) is not dict or set(preflight) != PRE_EXECUTION_KEYS:
            errors.append("CLAIM_BOUND_PREFLIGHT_KEYS_NOT_EXACT")
        else:
            if canonical_json_bytes(payload["pre_execution_gates"]) != canonical_json_bytes(
                preflight["gates"]
            ):
                errors.append("RESULT_GATES_NOT_CLAIM_BOUND_PREFLIGHT_GATES")
            if canonical_json_bytes(payload["independent_review_gate"]) != canonical_json_bytes(
                preflight["independent_review"]
            ):
                errors.append("RESULT_REVIEW_NOT_CLAIM_BOUND_PREFLIGHT_REVIEW")
    return {"errors": errors, "pass": not errors}


PREWRITE_RESULT_FILES = {
    "AUTHOR_POSTRUN_REPAIR_NOT_INDEPENDENT.md",
    "AUTHOR_POSTRUN_ROUND1_REPAIR_NOT_INDEPENDENT.md",
    "CODE_REVIEW.md",
    "EXPERIMENT_RESULTS.json",
    "POSTRUN_ANALYZER_PYTEST.xml",
    "POSTRUN_ANALYZER_REVIEW.md",
    "PRE_EXECUTION_AUDIT.json",
    "pytest.xml",
    "registered_run.claim.json",
    "registered_run.json",
}
FINAL_RESULT_FILES = PREWRITE_RESULT_FILES | {"result_manifest.json"}
REQUIRED_POST_PATHS = (
    "experiments/source_lock.json",
    "experiments/EXPERIMENT_PLAN.md",
    "notes/PROOF_PACKAGE.md",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
    "results/AUTHOR_POSTRUN_REPAIR_NOT_INDEPENDENT.md",
    "results/AUTHOR_POSTRUN_ROUND1_REPAIR_NOT_INDEPENDENT.md",
    "results/CODE_REVIEW.md",
    "results/PRE_EXECUTION_AUDIT.json",
    "results/pytest.xml",
    "results/POSTRUN_ANALYZER_PYTEST.xml",
    "results/POSTRUN_ANALYZER_REVIEW.md",
    CLAIM_RELATIVE,
    "results/EXPERIMENT_RESULTS.json",
    TERMINAL_RELATIVE,
)
RESULT_MANIFEST_PATH = "results/result_manifest.json"
RESULT_MANIFEST_SCHEMA = "CAT_TORSION_RESULT_MANIFEST_V2_DUAL_TREE"
RESULT_MANIFEST_KEYS = {
    "schema",
    "candidate_id",
    "source_lock_sha256",
    "execution_tree",
    "analyzer_tree",
    "immutable_execution_hashes",
    "junit_provenance",
    "postrun_analyzer_audit",
    "result_inventory",
    "files",
    "registered_exact_audits",
    "candidate_numerical_runs",
    "candidate_rerun_performed",
    "errors",
    "pass",
}


def _result_inventory_errors(
    project_root: Path, expected_names: set[str]
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    try:
        first = safe_directory_entries(project_root / "results")
        second = safe_directory_entries(project_root / "results")
    except (OSError, RuntimeError, ValueError):
        return ["RESULT_DIRECTORY_UNSAFE"], []
    if first != second:
        errors.append("RESULT_DIRECTORY_INVENTORY_UNSTABLE")
    names = [record["name"] for record in first]
    if set(names) != expected_names or len(names) != len(expected_names):
        errors.append("RESULT_FILE_INVENTORY_NOT_EXACT")
    for name in sorted(expected_names):
        if not regular_file(project_root / "results" / name):
            errors.append("RESULT_FILE_MISSING_OR_UNSAFE:" + name)
    return errors, names


def collect_postrun_analyzer_audit(project_root: Path) -> dict[str, Any]:
    """Validate immutable execution evidence and the current non-executing analyzer."""

    project_root = _raw_absolute(project_root)
    analyzer_tree = reviewed_code_tree_sha256(project_root)
    execution_chain = validate_immutable_execution_chain(project_root)
    result_path = project_root / "results" / "EXPERIMENT_RESULTS.json"
    result = load_exact_json(result_path) if regular_file(result_path) else None
    result_semantics = (
        validate_registered_result(result, project_root)
        if result is not None
        else {"errors": ["RESULT_MISSING_OR_UNSAFE"], "pass": False}
    )
    source_lock = validate_source_lock(project_root)
    upstream = validate_upstream_bindings(project_root)
    analyzer_isolation = executable_isolation_scan(project_root / "code")
    execution_postrun_junit = parse_passing_junit(
        project_root / "results" / "pytest.xml",
        required_tests=REQUIRED_JUNIT_TESTS,
        stage="R091_EXECUTION_TREE_POSTRUN_TEST_EVIDENCE",
        display_path="results/pytest.xml",
    )
    analyzer_junit = parse_passing_junit(
        project_root / "results" / "POSTRUN_ANALYZER_PYTEST.xml",
        required_tests=REQUIRED_ANALYZER_JUNIT_TESTS,
        stage="R092_ANALYZER_TREE_TEST_EVIDENCE",
        display_path="results/POSTRUN_ANALYZER_PYTEST.xml",
    )
    preflight_path = project_root / "results" / "PRE_EXECUTION_AUDIT.json"
    preflight = load_exact_json(preflight_path) if regular_file(preflight_path) else None
    execution_gate = (
        preflight.get("gates", {}).get("test_evidence")
        if type(preflight) is dict
        else None
    )
    junit_roles = validate_junit_role_separation(execution_gate, execution_postrun_junit)
    analyzer_review = validate_postrun_analyzer_authority(project_root)
    dual_tree_contract = {
        "execution_tree_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "execution_tree_role": "IMMUTABLE_REGISTERED_CANDIDATE_EXECUTION",
        "analyzer_tree_sha256": analyzer_tree,
        "analyzer_tree_role": "POSTRUN_VALIDATOR_ONLY_NO_CANDIDATE_AUTHORITY",
        "trees_are_distinct": analyzer_tree != EXPECTED_EXECUTION_TREE_SHA256,
        "candidate_rerun_forbidden": True,
        "raw_execution_artifacts_mutable": False,
        "same_source_lock_sha256": EXPECTED_LOCK_SHA256,
    }
    base_gates = {
        "immutable_execution_chain": execution_chain,
        "registered_result_semantics": result_semantics,
        "live_source_lock": source_lock,
        "live_upstream_bindings": upstream,
        "analyzer_executable_isolation": analyzer_isolation,
        "execution_postrun_junit": execution_postrun_junit,
        "analyzer_junit": analyzer_junit,
        "junit_role_separation": junit_roles,
    }
    base_pass = (
        dual_tree_contract["trees_are_distinct"] is True
        and all(record.get("pass") is True for record in base_gates.values())
    )
    status = (
        "AUTHORIZED_FOR_POSTRUN_MANIFEST"
        if base_pass and analyzer_review.get("pass") is True
        else "READY_FOR_INDEPENDENT_POSTRUN_ANALYZER_REVIEW"
        if base_pass
        else "POSTRUN_ANALYZER_AUDIT_FAILED"
    )
    return {
        "schema": "CAT_TORSION_POSTRUN_ANALYZER_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "execution_tree_sha256": EXPECTED_EXECUTION_TREE_SHA256,
        "analyzer_tree_sha256": analyzer_tree,
        "dual_tree_contract": dual_tree_contract,
        "base_gates": base_gates,
        "independent_analyzer_review": analyzer_review,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "candidate_rerun_performed": False,
        "status": status,
        "pass": base_pass,
    }


def _compose_post_run_manifest(
    project_root: Path, *, expected_result_files: set[str]
) -> dict[str, Any]:
    audit = collect_postrun_analyzer_audit(project_root)
    errors: list[str] = []
    if audit["pass"] is not True:
        errors.append("POSTRUN_ANALYZER_BASE_GATES_FAILED")
    if audit["status"] != "AUTHORIZED_FOR_POSTRUN_MANIFEST":
        errors.append("INDEPENDENT_POSTRUN_ANALYZER_REVIEW_MISSING_OR_STALE")
    if audit["independent_analyzer_review"].get("pass") is not True:
        errors.append("INDEPENDENT_POSTRUN_ANALYZER_REVIEW_NOT_PASSING")
    inventory_errors, _ = _result_inventory_errors(project_root, expected_result_files)
    errors.extend(inventory_errors)
    records = []
    for relative in REQUIRED_POST_PATHS:
        path = project_root / relative
        if not regular_file(path):
            errors.append("MISSING_OR_UNSAFE:" + relative)
        else:
            records.append({"path": relative, "sha256": sha256_file(path)})
    junit_roles = audit["base_gates"]["junit_role_separation"]
    return {
        "schema": RESULT_MANIFEST_SCHEMA,
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "execution_tree": {
            "sha256": EXPECTED_EXECUTION_TREE_SHA256,
            "role": "IMMUTABLE_REGISTERED_CANDIDATE_EXECUTION",
            "authority_path": "results/CODE_REVIEW.md",
            "authority_sha256": EXPECTED_RAW_HASHES["code_review_sha256"],
        },
        "analyzer_tree": {
            "sha256": audit["analyzer_tree_sha256"],
            "role": "POSTRUN_VALIDATOR_ONLY_NO_CANDIDATE_AUTHORITY",
            "authority_path": "results/POSTRUN_ANALYZER_REVIEW.md",
            "authority_sha256": audit["independent_analyzer_review"].get(
                "review_file_sha256"
            ),
        },
        "immutable_execution_hashes": EXPECTED_RAW_HASHES,
        "junit_provenance": junit_roles,
        "postrun_analyzer_audit": audit,
        "result_inventory": {
            "prewrite_files": sorted(PREWRITE_RESULT_FILES),
            "final_files": sorted(FINAL_RESULT_FILES),
            "manifest_path": RESULT_MANIFEST_PATH,
            "manifest_in_final_inventory": True,
            "manifest_self_hash_recorded": False,
            "nonself_hash_records": sorted(REQUIRED_POST_PATHS),
        },
        "files": records,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "candidate_rerun_performed": False,
        "errors": errors,
        "pass": not errors,
    }


def build_post_run_manifest(project_root: Path) -> dict[str, Any]:
    """Build only against the exact pre-write inventory."""

    project_root = _raw_absolute(project_root)
    return _compose_post_run_manifest(
        project_root, expected_result_files=PREWRITE_RESULT_FILES
    )


def validate_existing_post_run_manifest(project_root: Path) -> dict[str, Any]:
    """Strictly validate a written V2 closure without recursive self-hashing."""

    project_root = _raw_absolute(project_root)
    manifest_path = project_root / RESULT_MANIFEST_PATH
    errors, observed_names = _result_inventory_errors(project_root, FINAL_RESULT_FILES)
    raw: bytes | None = None
    stored: Any = None
    if not regular_file(manifest_path):
        errors.append("RESULT_MANIFEST_MISSING_OR_UNSAFE")
    else:
        try:
            first = stable_file_bytes(manifest_path)
            parsed = strict_json_loads(first.decode("utf-8"))
            canonical_json_bytes(parsed)
            second = stable_file_bytes(manifest_path)
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError, TypeError):
            errors.append("RESULT_MANIFEST_STRICT_JSON_INVALID")
        else:
            raw = first
            stored = parsed
            if first != second:
                errors.append("RESULT_MANIFEST_BYTES_UNSTABLE")
            pretty = (json.dumps(parsed, indent=2, sort_keys=True) + "\n").encode(
                "utf-8"
            )
            if first != pretty:
                errors.append("RESULT_MANIFEST_BYTES_NOT_CANONICAL")
    if type(stored) is not dict:
        errors.append("RESULT_MANIFEST_NOT_OBJECT")
    elif set(stored) != RESULT_MANIFEST_KEYS:
        errors.append("RESULT_MANIFEST_KEYS_NOT_EXACT")
    else:
        file_records = stored["files"]
        paths: list[str] = []
        if type(file_records) is not list:
            errors.append("RESULT_MANIFEST_FILES_NOT_LIST")
        else:
            for record in file_records:
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
            if set(paths) != set(REQUIRED_POST_PATHS):
                errors.append("RESULT_MANIFEST_NONSELF_PATHS_NOT_EXACT")
        expected_inventory = {
            "prewrite_files": sorted(PREWRITE_RESULT_FILES),
            "final_files": sorted(FINAL_RESULT_FILES),
            "manifest_path": RESULT_MANIFEST_PATH,
            "manifest_in_final_inventory": True,
            "manifest_self_hash_recorded": False,
            "nonself_hash_records": sorted(REQUIRED_POST_PATHS),
        }
        if canonical_json_bytes(stored["result_inventory"]) != canonical_json_bytes(
            expected_inventory
        ):
            errors.append("RESULT_MANIFEST_INVENTORY_ROLES_NOT_EXACT")
        try:
            recomputed = _compose_post_run_manifest(
                project_root, expected_result_files=FINAL_RESULT_FILES
            )
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError, TypeError, KeyError):
            recomputed = None
            errors.append("RESULT_MANIFEST_RECOMPUTATION_FAILED")
        if type(recomputed) is not dict or recomputed.get("pass") is not True:
            errors.append("RESULT_MANIFEST_LIVE_CLOSURE_NOT_PASSING")
        elif canonical_json_bytes(stored) != canonical_json_bytes(recomputed):
            errors.append("RESULT_MANIFEST_STORED_SEMANTICS_STALE_OR_TAMPERED")
    return {
        "stage": "R100_FINAL_POSTRUN_MANIFEST_CLOSURE",
        "manifest_path": RESULT_MANIFEST_PATH,
        "manifest_sha256": hashlib.sha256(raw).hexdigest() if raw is not None else None,
        "observed_result_files": observed_names,
        "errors": errors,
        "pass": not errors,
    }


def write_post_run_manifest(project_root: Path) -> Path:
    project_root = _raw_absolute(project_root)
    try:
        names = {
            record["name"] for record in safe_directory_entries(project_root / "results")
        }
    except (OSError, RuntimeError, ValueError) as error:
        raise RuntimeError("post-run result directory is unsafe") from error
    if "result_manifest.json" in names:
        raise FileExistsError("post-run result manifest is one-shot and already exists")
    manifest = build_post_run_manifest(project_root)
    if manifest["pass"] is not True:
        raise RuntimeError("post-run result manifest failed strict validation")
    output = project_root / RESULT_MANIFEST_PATH
    write_json(output, manifest, exclusive=True)
    closure = validate_existing_post_run_manifest(project_root)
    if closure["pass"] is not True:
        raise RuntimeError("written post-run result manifest failed final closure")
    return output
