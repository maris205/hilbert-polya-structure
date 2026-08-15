"""Read-only source, upstream, code-isolation, and test-evidence gates."""

from __future__ import annotations

import xml.etree.ElementTree as element_tree
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CAT_MATRIX,
    LOCAL_BINDINGS,
    LOCKED_COMPOSITES,
    LOCKED_MODULI,
    LOCKED_PRIMES,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
    TERMINAL_CLASSIFICATION,
    UPSTREAM_BINDINGS,
)
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
        "test_forbidden_modulus_rejected",
        "test_prime_reversing_groups_are_exact_and_never_mix_strata",
        "test_strict_json_and_closed_inventory",
        "test_scanner_rejects_dynamic_alias_loader_process_network_and_float_bypasses",
        "test_scanner_rejects_unreviewed_tree_and_hidden_modulus_literal",
        "test_source_design_and_upstream_bindings_pass",
        "test_deployment_authority_is_hash_bound_and_duplicate_safe",
        "test_registered_lifecycle_requires_review_and_is_one_shot",
        "test_registered_candidate_contract_has_zero_forbidden_counters",
        "test_result_validator_rejects_structural_and_counter_bypasses",
        "test_manifest_rejects_extra_result_file",
    }
)


def validate_source_and_design(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    path = root / "experiments" / "source_lock.json"
    errors: list[str] = []
    try:
        payload = load_exact_json(path)
        observed = sha256_file(path)
    except (OSError, RuntimeError, UnicodeDecodeError, ValueError):
        return {"stage": "P0_SOURCE_DESIGN", "errors": ["SOURCE_LOCK_INVALID"], "pass": False}
    if observed != SOURCE_LOCK_SHA256:
        errors.append("SOURCE_LOCK_SHA256_MISMATCH")
    if type(payload) is not dict:
        return {"stage": "P0_SOURCE_DESIGN", "errors": errors + ["SOURCE_LOCK_NOT_OBJECT"], "pass": False}
    frozen = payload.get("frozen_object", {})
    audit = payload.get("frozen_audit", {})
    implementation = payload.get("implementation_gate", {})
    checks = {
        "candidate_exact": payload.get("candidate_id") == CANDIDATE_ID,
        "matrix_exact": frozen.get("matrix") == [list(row) for row in CAT_MATRIX],
        "moduli_exact": audit.get("ordered_moduli") == list(LOCKED_MODULI),
        "primes_exact": audit.get("inherited_prime_controls") == list(LOCKED_PRIMES),
        "composites_exact": audit.get("predeclared_composite_controls") == list(LOCKED_COMPOSITES),
        "new_modulus_scan_forbidden": audit.get("new_modulus_scan_allowed") is False,
        "new_prime_scan_forbidden": audit.get("new_prime_scan_allowed") is False,
        "network_forbidden": audit.get("network_allowed") is False,
        "randomness_forbidden": audit.get("randomness_allowed") is False,
        "numeric_s_forbidden": audit.get("numeric_s_allowed") is False,
        "numeric_log_forbidden": audit.get("numeric_log_allowed") is False,
        "code_absent_at_lock": implementation.get("code_exists_at_lock") is False,
        "execution_unauthorized_at_lock": implementation.get("execution_authorized") is False,
        "terminal_exact": payload.get("terminal_certificate") == TERMINAL_CLASSIFICATION,
    }
    errors.extend(key.upper() for key, passed in checks.items() if passed is not True)
    local_records = []
    locked_local = payload.get("local_design_bindings", {})
    for binding, (relative, expected) in LOCAL_BINDINGS.items():
        file_path = root / relative
        current = sha256_file(file_path) if regular_file(file_path) else None
        passed = current == expected == locked_local.get(binding)
        local_records.append({"binding": binding, "path": relative, "expected": expected, "observed": current, "pass": passed})
        if not passed:
            errors.append("LOCAL_BINDING_MISMATCH:" + binding)
    review_path = root / "notes" / "INDEPENDENT_SOURCE_LOCK_REVIEW.md"
    review_sha = sha256_file(review_path) if regular_file(review_path) else None
    review_text = stable_file_bytes(review_path).decode("utf-8") if regular_file(review_path) else ""
    if review_sha != SOURCE_REVIEW_SHA256:
        errors.append("SOURCE_REVIEW_SHA256_MISMATCH")
    if "## Verdict\n\n**PASS**" not in review_text:
        errors.append("SOURCE_REVIEW_PASS_MISSING")
    if SOURCE_LOCK_SHA256 not in review_text:
        errors.append("SOURCE_REVIEW_NOT_LOCK_BOUND")
    return {
        "stage": "P0_SOURCE_DESIGN",
        "source_lock_sha256": observed,
        "source_review_sha256": review_sha,
        "checks": checks,
        "local_binding_records": local_records,
        "errors": errors,
        "pass": not errors,
    }


def validate_upstream(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    payload = load_exact_json(root / "experiments" / "source_lock.json")
    locked = payload.get("upstream_paper9_bindings", {})
    records = []
    errors: list[str] = []
    for binding, (relative, expected) in UPSTREAM_BINDINGS.items():
        path = root / relative
        current = sha256_file(path) if regular_file(path) else None
        passed = current == expected == locked.get(binding)
        records.append({"binding": binding, "path": relative, "expected": expected, "observed": current, "pass": passed})
        if not passed:
            errors.append("UPSTREAM_BINDING_MISMATCH:" + binding)
    if locked.get("upstream_terminal_status") != "COMPLETE_LOCAL_FINAL_REVIEW_PASS":
        errors.append("UPSTREAM_TERMINAL_STATUS_MISMATCH")
    return {"stage": "P1_UPSTREAM", "records": records, "errors": errors, "pass": not errors}


def parse_junit(path: Path) -> dict[str, Any]:
    if not regular_file(path):
        return {"stage": "P3_TEST_EVIDENCE", "errors": ["JUNIT_MISSING"], "pass": False}
    raw = stable_file_bytes(path)
    errors: list[str] = []
    names: set[str] = set()
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    try:
        root = element_tree.fromstring(raw)
    except element_tree.ParseError:
        errors.append("JUNIT_MALFORMED")
    else:
        suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
        if not suites:
            errors.append("JUNIT_NO_TESTSUITE")
        for suite in suites:
            for key in totals:
                try:
                    totals[key] += int(suite.attrib.get(key, "0"))
                except ValueError:
                    errors.append("JUNIT_NONINTEGER:" + key)
            for case in suite.iter("testcase"):
                if case.attrib.get("name"):
                    names.add(case.attrib["name"])
    if any(totals[key] != 0 for key in ("failures", "errors", "skipped")):
        errors.append("JUNIT_NOT_ALL_PASSING")
    if REQUIRED_TESTS.difference(names):
        errors.append("JUNIT_REQUIRED_TESTS_MISSING")
    return {
        "stage": "P3_TEST_EVIDENCE",
        "path": PREEXECUTION_TEST_PATH,
        "sha256": sha256_file(path),
        "totals": totals,
        "required_tests": sorted(REQUIRED_TESTS),
        "observed_required_tests": sorted(REQUIRED_TESTS.intersection(names)),
        "errors": errors,
        "pass": not errors,
    }


def source_schema_contract(project_root: Path) -> dict[str, Any]:
    payload = load_exact_json(project_root / "experiments" / "source_lock.json")
    quotient = payload.get("quotient_dynamics_lock", {})
    symplectic = payload.get("symplectic_norm_lock", {})
    route = payload.get("route_evaluation_lock", {})
    outside = payload.get("outside_scope_live_clues", {})
    checks = {
        "full_quotient_one": quotient.get("full_coarse_quotient_cardinality") == 1,
        "full_action_identity": quotient.get("induced_A_map_on_full_quotient") == "IDENTITY",
        "symplectic_action_identity": quotient.get("induced_A_map_on_symplectic_quotient") == "IDENTITY",
        "external_specialization": quotient.get("specialization_status") == "EXTERNAL_MODULUS_SPECIALIZATION_NOT_NATIVE_RETURN_CLOCK",
        "prime_selector_absent": quotient.get("intrinsic_prime_selector") is False,
        "sp_not_full_gl": symplectic.get("full_GL_centralizer_is_generally_symplectic") is False,
        "route_b_closed": route.get("route_b_invocation_allowed") is False,
        "stacky_outside": outside.get("equivariant_burnside_zeta") == "OUTSIDE_SCOPE_PAPER11",
    }
    return {"stage": "P2_SOURCE_SCHEMA", "checks": checks, "errors": [] if all(checks.values()) else ["SOURCE_SCHEMA_CONTRACT_FAILED"], "pass": all(checks.values())}


def collect_safe_preflight(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    gates = {
        "source_and_design": validate_source_and_design(root),
        "upstream": validate_upstream(root),
        "source_schema": source_schema_contract(root),
        "executable_isolation": executable_isolation_scan(root / "code"),
        "test_evidence": parse_junit(root / PREEXECUTION_TEST_PATH),
    }
    safe = all(record.get("pass") is True for record in gates.values())
    review = validate_deployment_authority(root)
    status = "AUTHORIZED_FOR_REGISTERED_EXECUTION" if safe and review.get("pass") is True else (
        "READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW" if safe else "SAFE_PREFLIGHT_FAILED"
    )
    return {
        "schema": "CENTRALIZER_QUOTIENT_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_tree_sha256(root),
        "gates": gates,
        "independent_review": review,
        "locked_moduli": list(LOCKED_MODULI),
        "registered_exact_audits": 0,
        "registered_moduli_executed": [],
        "candidate_numerical_runs": 0,
        "network_accesses": 0,
        "external_data_loads": 0,
        "generated_prime_or_modulus_targets": 0,
        "numeric_s_or_log_evaluations": 0,
        "status": status,
        "pass": safe and review.get("pass") is True,
    }


def write_safe_preflight(project_root: Path) -> Path:
    root = lexical_absolute(project_root)
    output = root / PREEXECUTION_AUDIT_PATH
    write_json(output, collect_safe_preflight(root))
    return output
