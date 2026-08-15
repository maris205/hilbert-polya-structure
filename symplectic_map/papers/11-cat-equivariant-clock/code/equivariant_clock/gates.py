"""Read-only source, upstream, closed-world, and test-evidence gates."""

from __future__ import annotations

import xml.etree.ElementTree as element_tree
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CAT_MATRIX,
    CITATION_BINDING,
    LOCAL_BINDINGS,
    LOCKED_COMPOSITES,
    LOCKED_MODULI,
    LOCKED_PRIMES,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_BINDINGS,
    SOURCE_REVIEW_R1_SHA256,
    SOURCE_REVIEW_R2_SHA256,
    TERMINAL_CLASSIFICATION,
    UPSTREAM_PAPER9_BINDINGS,
    UPSTREAM_PAPER10_BINDINGS,
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
        "test_all_locked_rows_reconstruct_regular_torsors",
        "test_definition_separated_invariants_match_dual_engines",
        "test_one_sided_engine_mutations_are_detected",
        "test_general_cyclic_cset_engines_match_structural_control",
        "test_structural_C6_control_is_effective_without_period_six",
        "test_forbidden_modulus_and_structural_namespace_rejected",
        "test_source_design_and_upstream_bindings_pass",
        "test_strict_json_closed_inventory_and_scanner",
        "test_scanner_rejects_capability_float_and_hidden_modulus_attacks",
        "test_deployment_authority_is_hash_bound_and_duplicate_safe",
        "test_registered_lifecycle_requires_review_and_is_one_shot",
        "test_registered_candidate_contract_has_zero_forbidden_counters",
        "test_result_validator_rejects_hollow_rows_and_counter_bypasses",
        "test_externality_and_exact_control_schema_rejects_mutations",
        "test_preclaim_import_graph_stays_science_free",
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
    audit = payload.get("frozen_audit", {})
    specialization = payload.get("paper10_torsor_specialization_lock", {})
    implementation = payload.get("implementation_gate", {})
    checks = {
        "candidate_exact": payload.get("candidate_id") == CANDIDATE_ID,
        "lock_version_two": payload.get("lock_version") == 2,
        "matrix_exact": specialization.get("matrix") == [list(row) for row in CAT_MATRIX],
        "moduli_exact": audit.get("ordered_moduli") == list(LOCKED_MODULI),
        "primes_exact": audit.get("prime_controls") == list(LOCKED_PRIMES),
        "composites_exact": audit.get("composite_controls") == list(LOCKED_COMPOSITES),
        "row_count_nine": audit.get("row_count") == 9,
        "no_other_modulus": audit.get("no_other_modulus") is True,
        "numeric_s_forbidden": audit.get("numeric_s_evaluation_allowed") is False,
        "numeric_log_forbidden": audit.get("numeric_log_q_evaluation_allowed") is False,
        "source_pass_required": implementation.get("required_verdict") == "SOURCE_LOCK_PASS",
        "later_deployment_pass_required": implementation.get("later_deployment_pass_required") is True,
        "terminal_exact": payload.get("intended_terminal_certificate") == TERMINAL_CLASSIFICATION,
    }
    errors.extend(key.upper() for key, passed in checks.items() if passed is not True)
    locked_local = payload.get("local_design_bindings", {})
    local_records = []
    for binding, (relative, expected) in LOCAL_BINDINGS.items():
        file_path = root / relative
        current = sha256_file(file_path) if regular_file(file_path) else None
        passed = current == expected == locked_local.get(binding)
        local_records.append(
            {"binding": binding, "path": relative, "expected": expected, "observed": current, "pass": passed}
        )
        if not passed:
            errors.append("LOCAL_BINDING_MISMATCH:" + binding)
    citation_path, citation_expected = CITATION_BINDING
    citation_current = sha256_file(root / citation_path) if regular_file(root / citation_path) else None
    citation_locked = payload.get("citation_verification_binding", {}).get("sha256")
    citation_pass = citation_current == citation_expected == citation_locked
    if not citation_pass:
        errors.append("CITATION_BINDING_MISMATCH")
    review_records = []
    for relative, expected, verdict in SOURCE_REVIEW_BINDINGS:
        review_path = root / relative
        current = sha256_file(review_path) if regular_file(review_path) else None
        text = stable_file_bytes(review_path).decode("utf-8") if regular_file(review_path) else ""
        passed = current == expected and verdict in text
        review_records.append(
            {"path": relative, "expected": expected, "observed": current, "verdict": verdict, "pass": passed}
        )
        if not passed:
            errors.append("SOURCE_REVIEW_BINDING_MISMATCH:" + relative)
    r2_text = stable_file_bytes(root / SOURCE_REVIEW_BINDINGS[1][0]).decode("utf-8")
    if SOURCE_LOCK_SHA256 not in r2_text or SOURCE_REVIEW_R1_SHA256 not in r2_text:
        errors.append("SOURCE_R2_NOT_BOUND_TO_LOCK_AND_R1")
    if SOURCE_REVIEW_R2_SHA256 != SOURCE_REVIEW_BINDINGS[1][1]:
        errors.append("SOURCE_R2_CONSTANT_MISMATCH")
    return {
        "stage": "P0_SOURCE_DESIGN",
        "source_lock_sha256": observed,
        "checks": checks,
        "local_binding_records": local_records,
        "citation_binding": {
            "path": citation_path,
            "expected": citation_expected,
            "observed": citation_current,
            "pass": citation_pass,
        },
        "source_review_records": review_records,
        "errors": errors,
        "pass": not errors,
    }


def _upstream_records(
    root: Path,
    locked: dict[str, Any],
    expected_bindings: dict[str, tuple[str, str]],
    label: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for binding, (relative, expected) in expected_bindings.items():
        path = root / relative
        current = sha256_file(path) if regular_file(path) else None
        passed = current == expected == locked.get(binding)
        records.append(
            {"binding": binding, "path": relative, "expected": expected, "observed": current, "pass": passed}
        )
        if not passed:
            errors.append(label + "_BINDING_MISMATCH:" + binding)
    if locked.get("upstream_terminal_status") != "COMPLETE_LOCAL_FINAL_REVIEW_PASS":
        errors.append(label + "_TERMINAL_STATUS_MISMATCH")
    return records, errors


def validate_upstream(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    payload = load_exact_json(root / "experiments" / "source_lock.json")
    paper9_records, paper9_errors = _upstream_records(
        root,
        payload.get("upstream_paper9_bindings", {}),
        UPSTREAM_PAPER9_BINDINGS,
        "PAPER9",
    )
    paper10_records, paper10_errors = _upstream_records(
        root,
        payload.get("upstream_paper10_bindings", {}),
        UPSTREAM_PAPER10_BINDINGS,
        "PAPER10",
    )
    errors = paper9_errors + paper10_errors
    return {
        "stage": "P1_UPSTREAM",
        "paper9_records": paper9_records,
        "paper10_records": paper10_records,
        "errors": errors,
        "pass": not errors,
    }


def source_schema_contract(project_root: Path) -> dict[str, Any]:
    payload = load_exact_json(project_root / "experiments" / "source_lock.json")
    conventions = payload.get("formal_convention_lock", {})
    theorem = payload.get("general_finite_abelian_theorem_lock", {})
    structural = payload.get("structural_counterexample_lock", {})
    specialization = payload.get("paper10_torsor_specialization_lock", {})
    clock = payload.get("clock_semantics_lock", {})
    checks = {
        "point_name_exact": conventions.get("point_zeta_name") == "point-order rational Burnside zeta",
        "orbit_name_exact": conventions.get("orbit_zeta_name") == "orbit-order integral Burnside zeta",
        "g_permutation_inverse": conventions.get("g_permutation_twist_convention") == "a^(-1)",
        "enhanced_twist_a": conventions.get("enhanced_return_twist_convention") == "a",
        "orbifold_additive_only": "additive homomorphism" in conventions.get("orbifold_map_type", ""),
        "action_kernel_formula": theorem.get("action_kernel") == "N=intersection of K with n_K>0",
        "stack_static": theorem.get("stack_dynamics")
        == "translation by a is 2-isomorphic to identity; all retained inertia is static",
        "structural_namespace": structural.get("namespace") == "structural_unit_control",
        "structural_not_modulus": structural.get("is_arithmetic_modulus_row") is False,
        "structural_no_period_six": structural.get("period_6_factor_present") is False,
        "regular_effective": specialization.get("action_is_free_transitive_effective") is True,
        "coarse_point": specialization.get("action_groupoid")
        == "G_q action_groupoid X_q is equivalent to one point",
        "period_not_modulus": clock.get("period_determines_modulus") is False,
        "prime_selector_absent": clock.get("intrinsic_prime_selector") is False,
    }
    return {
        "stage": "P2_SOURCE_SCHEMA",
        "checks": checks,
        "errors": [] if all(checks.values()) else ["SOURCE_SCHEMA_CONTRACT_FAILED"],
        "pass": all(checks.values()),
    }


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
    status = (
        "AUTHORIZED_FOR_REGISTERED_EXECUTION"
        if safe and review.get("pass") is True
        else ("READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW" if safe else "SAFE_PREFLIGHT_FAILED")
    )
    return {
        "schema": "EQUIVARIANT_CLOCK_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_tree_sha256(root),
        "gates": gates,
        "independent_review": review,
        "arithmetic_modulus_order": list(LOCKED_MODULI),
        "structural_unit_control_count": 1,
        "structural_control_in_modulus_namespace": False,
        "registered_audit_count": 0,
        "registered_moduli_executed": [],
        "candidate_numerical_run_count": 0,
        "network_access_count": 0,
        "external_data_load_count": 0,
        "numeric_s_or_log_evaluation_count": 0,
        "status": status,
        "pass": safe and review.get("pass") is True,
    }


def write_safe_preflight(project_root: Path) -> Path:
    root = lexical_absolute(project_root)
    output = root / PREEXECUTION_AUDIT_PATH
    write_json(output, collect_safe_preflight(root))
    return output
