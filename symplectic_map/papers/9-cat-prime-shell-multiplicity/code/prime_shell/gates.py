"""Non-candidate pre-execution gates and exact source/upstream validators."""

from __future__ import annotations

import hashlib
import xml.etree.ElementTree as element_tree
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CAT_MATRIX,
    CLAIM_PATH,
    LOCAL_BINDINGS,
    LOCKED_PRIMES,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
    RESULT_PATH,
    REPEATS,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
    TERMINAL_PATH,
    UPSTREAM_BINDINGS,
)
from .proof_contract import proof_only_contract, validate_proof_only_contract
from .protocol import (
    code_tree_sha256,
    executable_isolation_scan,
    lexical_absolute,
    load_exact_json,
    regular_file,
    sha256_file,
    stable_file_bytes,
    write_json,
)
from .review import validate_deployment_authority


REQUIRED_TESTS = frozenset(
    {
        "test_all_locked_rows_match_dual_engines_and_expected_ledger",
        "test_raw_and_label_ledgers_remain_distinct_at_ramified_five",
        "test_equal_weight_repetition_and_fractional_identity",
        "test_symbolic_composite_control_never_selects_q",
        "test_forbidden_modulus_rejected",
        "test_registered_lifecycle_requires_review_and_is_one_shot",
        "test_duplicate_authority_and_duplicate_json_fail_closed",
        "test_manifest_rejects_extra_result_file",
        "test_result_validator_rejects_round1_structural_bypass",
        "test_scanner_rejects_alias_container_dynamic_import_and_loader_attacks",
        "test_scanner_rejects_exact_import_dunder_bypasses_and_counts_float",
        "test_scanner_rejects_unreviewed_os_family_and_low_level_read_sites",
        "test_official_gate_records_must_match_live_recomputation",
        "test_writers_fsync_file_then_parent_directory",
    }
)


def validate_source_and_design(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    lock_path = root / "experiments" / "source_lock.json"
    errors: list[str] = []
    try:
        payload = load_exact_json(lock_path)
        observed_lock = sha256_file(lock_path)
    except (OSError, RuntimeError, UnicodeDecodeError, ValueError):
        return {"stage": "P0_SOURCE_AND_DESIGN_BINDINGS", "errors": ["SOURCE_LOCK_INVALID"], "pass": False}
    if observed_lock != SOURCE_LOCK_SHA256:
        errors.append("SOURCE_LOCK_SHA256_MISMATCH")
    if type(payload) is not dict:
        errors.append("SOURCE_LOCK_NOT_OBJECT")
        return {"stage": "P0_SOURCE_AND_DESIGN_BINDINGS", "errors": errors, "pass": False}
    frozen = payload.get("frozen_object", {})
    audit = payload.get("registered_exact_audit_lock", {})
    execution = payload.get("execution_state_at_lock", {})
    permissions = payload.get("preexecution_permissions", {})
    checks = {
        "candidate_id": payload.get("candidate_id") == CANDIDATE_ID,
        "lock_version_v2": payload.get("lock_version") == 2
        and type(payload.get("lock_version")) is int,
        "matrix_exact": frozen.get("matrix") == [list(row) for row in CAT_MATRIX],
        "prime_tuple_exact": audit.get("prime_set") == list(LOCKED_PRIMES),
        "new_prime_scan_forbidden": audit.get("new_prime_scan_allowed") is False,
        "numeric_s_forbidden": audit.get("numeric_s_allowed") is False,
        "numeric_log_forbidden": audit.get("numeric_log_allowed") is False,
        "composite_enumeration_forbidden": audit.get("composite_enumeration_allowed") is False,
        "registered_count_zero_at_lock": execution.get("registered_exact_audits") == 0
        and type(execution.get("registered_exact_audits")) is int,
        "generated_prime_arrays_zero": execution.get("generated_prime_target_arrays") == 0
        and type(execution.get("generated_prime_target_arrays")) is int,
        "external_prime_tables_unaccessed": execution.get("external_prime_target_tables_accessed") is False,
        "riemann_zeros_unaccessed": execution.get("riemann_zero_data_accessed") is False,
        "registered_permission_locked": permissions.get("registered_exact_audit") is False,
        "numeric_permission_locked": permissions.get("candidate_numerical_execution") is False,
        "centralizer_permission_locked": permissions.get("centralizer_quotient_work") is False,
    }
    errors.extend(key.upper() for key, value in checks.items() if value is not True)
    local_locked = payload.get("local_design_bindings", {})
    records = []
    for binding_id, (relative, expected_sha) in LOCAL_BINDINGS.items():
        path = root / relative
        observed = sha256_file(path) if regular_file(path) else None
        locked_sha = local_locked.get(binding_id)
        passed = observed == expected_sha == locked_sha
        records.append(
            {
                "binding_id": binding_id,
                "path": relative,
                "locked_sha256": locked_sha,
                "expected_sha256": expected_sha,
                "observed_sha256": observed,
                "pass": passed,
            }
        )
        if not passed:
            errors.append("LOCAL_BINDING_MISMATCH:" + binding_id)
    review_path = root / "notes" / "INDEPENDENT_SOURCE_LOCK_REVIEW.md"
    review_sha = sha256_file(review_path) if regular_file(review_path) else None
    review_text = stable_file_bytes(review_path).decode("utf-8") if regular_file(review_path) else ""
    if review_sha != SOURCE_REVIEW_SHA256:
        errors.append("SOURCE_REVIEW_SHA256_MISMATCH")
    if "Verdict: **SOURCE_LOCK_PASS**." not in review_text:
        errors.append("SOURCE_REVIEW_VERDICT_MISSING")
    if SOURCE_LOCK_SHA256 not in review_text:
        errors.append("SOURCE_REVIEW_NOT_BOUND_TO_LOCK")
    return {
        "stage": "P0_SOURCE_AND_DESIGN_BINDINGS",
        "source_lock_sha256": observed_lock,
        "source_review_sha256": review_sha,
        "checks": checks,
        "local_binding_records": records,
        "errors": errors,
        "pass": not errors,
    }


def validate_upstream(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    payload = load_exact_json(root / "experiments" / "source_lock.json")
    locked = payload.get("upstream_paper8_bindings", {})
    errors: list[str] = []
    records = []
    for binding_id, (relative, expected_sha) in UPSTREAM_BINDINGS.items():
        path = root / relative
        observed = sha256_file(path) if regular_file(path) else None
        locked_sha = locked.get(binding_id)
        passed = observed == expected_sha == locked_sha
        records.append(
            {
                "binding_id": binding_id,
                "path": relative,
                "locked_sha256": locked_sha,
                "expected_sha256": expected_sha,
                "observed_sha256": observed,
                "pass": passed,
            }
        )
        if not passed:
            errors.append("UPSTREAM_BINDING_MISMATCH:" + binding_id)
    if locked.get("use_boundary") != (
        "only the five inherited p-shell profiles at p in {2,3,5,7,11} may be reused; "
        "the broader Paper-8 prime ledger is forbidden"
    ):
        errors.append("UPSTREAM_USE_BOUNDARY_MISMATCH")
    return {"stage": "P1_UPSTREAM_BINDINGS", "records": records, "errors": errors, "pass": not errors}


def parse_junit(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    names: set[str] = set()
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    if not regular_file(path):
        return {"stage": "P3_PREEXECUTION_TEST_EVIDENCE", "errors": ["JUNIT_MISSING_OR_UNSAFE"], "pass": False}
    raw = stable_file_bytes(path)
    try:
        root = element_tree.fromstring(raw)
    except element_tree.ParseError:
        errors.append("JUNIT_XML_MALFORMED")
    else:
        suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
        if not suites:
            errors.append("JUNIT_NO_TESTSUITE")
        for suite in suites:
            for key in totals:
                raw_value = suite.attrib.get(key, "0")
                try:
                    totals[key] += int(raw_value)
                except ValueError:
                    errors.append("JUNIT_NONINTEGER_TOTAL:" + key)
            for case in suite.iter("testcase"):
                name = case.attrib.get("name")
                if name:
                    names.add(name)
        if totals["tests"] < len(REQUIRED_TESTS):
            errors.append("JUNIT_TOO_FEW_TESTS")
        if any(totals[key] != 0 for key in ("failures", "errors", "skipped")):
            errors.append("JUNIT_NOT_ALL_PASSING")
        missing = sorted(REQUIRED_TESTS.difference(names))
        if missing:
            errors.append("JUNIT_REQUIRED_TESTS_MISSING")
    return {
        "stage": "P3_PREEXECUTION_TEST_EVIDENCE",
        "path": PREEXECUTION_TEST_PATH,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "totals": totals,
        "required_tests": sorted(REQUIRED_TESTS),
        "observed_required_tests": sorted(REQUIRED_TESTS.intersection(names)),
        "errors": errors,
        "pass": not errors,
    }


def source_schema_contract(project_root: Path) -> dict[str, Any]:
    payload = load_exact_json(project_root / "experiments" / "source_lock.json")
    product = payload.get("product_semantics_lock", {})
    scalar = payload.get("scalar_weight_obstruction", {})
    analytic = payload.get("global_analytic_scope", {})
    centralizer = payload.get("centralizer_escape_boundary", {})
    checks = {
        "products_not_identified": product.get("products_may_not_be_identified") is True,
        "repeat_coefficient_exact": product.get("orbit_label", {}).get("repeat_coefficient") == "m_p/r",
        "nonzero_scalar_scope": scalar.get("nonzero_assumption") == "w_gamma is nonzero for every gamma",
        "matrix_weights_excluded": "matrix-valued factors" in scalar.get("excluded_from_theorem", []),
        "analytic_gap_unclaimed": analytic.get("gap_status") == "NO_CLAIM_FOR_2_LT_RE_S_LE_3",
        "centralizer_reserved": centralizer.get("status") == "REAL_OUTSIDE_THEOREM_ESCAPE_RESERVED_FOR_PAPER10",
        "repeat_tuple_exact": REPEATS == (1, 2, 3),
    }
    return {
        "stage": "P2_SOURCE_SCHEMA_PROOF_CONTRACT",
        "checks": checks,
        "embedded_proof_only_contract": proof_only_contract(),
        "proof_contract_validation": validate_proof_only_contract(proof_only_contract()),
        "pass": all(checks.values()),
    }


def collect_safe_preflight(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    gates = {
        "source_and_design": validate_source_and_design(root),
        "upstream": validate_upstream(root),
        "executable_isolation": executable_isolation_scan(root / "code"),
        "source_schema_contract": source_schema_contract(root),
        "test_evidence": parse_junit(root / PREEXECUTION_TEST_PATH),
    }
    safe_pass = all(record.get("pass") is True for record in gates.values())
    review = validate_deployment_authority(root)
    status = (
        "AUTHORIZED_FOR_REGISTERED_EXECUTION"
        if safe_pass and review.get("pass") is True
        else "READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW"
        if safe_pass
        else "SAFE_PREFLIGHT_FAILED"
    )
    return {
        "schema": "PRIME_SHELL_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_tree_sha256(root),
        "gates": gates,
        "independent_review": review,
        "locked_primes": list(LOCKED_PRIMES),
        "formal_repeats": list(REPEATS),
        "registered_exact_audits": 0,
        "registered_primes_executed": [],
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "numeric_s_or_log_evaluations": 0,
        "centralizer_computations_run": 0,
        "status": status,
        "pass": safe_pass,
    }


def write_safe_preflight(project_root: Path) -> Path:
    root = lexical_absolute(project_root)
    if any(regular_file(root / relative) for relative in (CLAIM_PATH, RESULT_PATH, TERMINAL_PATH)):
        raise RuntimeError("official pre-execution evidence is immutable after lifecycle claim")
    output = root / PREEXECUTION_AUDIT_PATH
    write_json(output, collect_safe_preflight(root))
    return output
