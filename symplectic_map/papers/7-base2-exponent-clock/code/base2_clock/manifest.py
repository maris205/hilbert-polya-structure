"""Strict pre-execution and post-run evidence closure."""

from __future__ import annotations

import stat
import xml.etree.ElementTree as ET
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import candidate_field, parameter_polynomial
from .controls import run_all_controls
from .lifecycle import (
    CLAIM_KEYS,
    CLAIM_RELATIVE,
    TERMINAL_KEYS,
    TERMINAL_RELATIVE,
    validate_registered_claim,
)
from .proof_contract import audit_proof_contract
from .protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    _raw_absolute,
    canonical_json_bytes,
    executable_isolation_scan,
    load_exact_json,
    regular_directory,
    regular_file,
    safe_directory_entries,
    sha256_file,
    stable_file_bytes,
    validate_source_lock,
    validate_upstream_bindings,
    write_json,
)
from .review_gate import reviewed_code_tree_sha256, validate_review_authority


GATE_KEYS = {
    "source_lock",
    "upstream_bindings",
    "executable_isolation",
    "proof_contract",
    "controls",
}
GATE_STAGES = {
    "source_lock": "P0_SOURCE_LOCK",
    "upstream_bindings": "P0_UPSTREAM_BINDINGS",
    "executable_isolation": "P0_EXECUTABLE_ISOLATION",
    "proof_contract": "P1_PROOF_CONTRACT",
    "controls": "P2_CONTROLS_ONLY",
}
PRE_EXECUTION_KEYS = {
    "schema",
    "candidate_id",
    "source_lock_sha256",
    "reviewed_code_sha256",
    "gates",
    "independent_review",
    "registered_candidate_runs",
    "registered_candidate_periods_executed",
    "external_prime_tables_accessed",
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
    "registered_periods_frozen",
    "periods_executed",
    "new_blind_periods",
    "development_seen_periods",
    "period_records",
    "stopped_on_target_hit",
    "completed_frozen_cutoff",
    "candidate_numerical_runs",
    "external_prime_tables_accessed",
    "riemann_zero_data_accessed",
    "approximate_matching_used",
    "classification",
    "all_period_equality_status",
    "route_a",
    "route_b",
    "pass",
    "pre_execution_gates",
    "independent_review_gate",
}
PERIOD_KEYS = {
    "period",
    "iterate_equation_degree",
    "iterate_radical_degree",
    "iterate_scheme_repeated_degree",
    "formal_dynatomic_degree",
    "formal_radical_degree",
    "formal_scheme_repeated_degree",
    "lower_overlap_degree",
    "exact_set_degree",
    "exact_cycle_count",
    "formal_radical_equals_exact_set",
    "exact_set_squarefree",
    "exact_degree_divisible_by_period",
    "normalized_product_invariant",
    "targets",
    "status",
    "iterate_equation",
    "iterate_radical",
    "formal_dynatomic",
    "formal_radical",
    "lower_overlap",
    "exact_set_component",
    "normalized_cycle_product",
    "run_id",
    "evidentiary_role",
    "wall_time_nanoseconds",
    "optional_q3_diagnostic",
}
TARGET_KEYS = {
    "target",
    "gcd_degree",
    "hit",
    "target_resultant",
    "rational_field_norm",
    "field_norm_nonzero",
    "gcd_resultant_norm_agree",
    "gcd_polynomial",
}
POLYNOMIAL_KEYS = {
    "variable",
    "domain",
    "degree",
    "coefficients_descending",
    "coefficient_basis",
    "coefficients_basis_descending",
}
ELEMENT_KEYS = {"domain", "basis", "coefficients_ascending", "expression"}
POST_RESULT_FILES = {
    "AUTHOR_REPAIR_NOT_INDEPENDENT.md",
    "AUTHOR_ROUND2_REPAIR_NOT_INDEPENDENT.md",
    "AUTHOR_ROUND3_REPAIR_NOT_INDEPENDENT.md",
    "CODE_REVIEW.md",
    "EXPERIMENT_RESULTS.json",
    "PRE_EXECUTION_AUDIT.json",
    "pytest.xml",
    "registered_run.claim.json",
    "registered_run.json",
}
POST_RUN_REQUIRED_FILES = (
    "experiments/source_lock.json",
    "experiments/EXPERIMENT_PLAN.md",
    "notes/PROOF_PACKAGE.md",
    "results/AUTHOR_REPAIR_NOT_INDEPENDENT.md",
    "results/AUTHOR_ROUND2_REPAIR_NOT_INDEPENDENT.md",
    "results/AUTHOR_ROUND3_REPAIR_NOT_INDEPENDENT.md",
    "results/CODE_REVIEW.md",
    "results/PRE_EXECUTION_AUDIT.json",
    "results/EXPERIMENT_RESULTS.json",
    CLAIM_RELATIVE,
    TERMINAL_RELATIVE,
    "results/pytest.xml",
)
REQUIRED_JUNIT_TESTS = {
    "test_scanner_blocks_round1_alias_and_path_bypasses",
    "test_field_target_hit_and_miss_agree",
    "test_lifecycle_claim_is_one_shot_and_target_halt_is_terminal",
    "test_manifest_rejects_forged_nested_evidence",
    "test_scanner_blocks_named_container_callable_laundering_in_closed_tree",
    "test_scanner_blocks_ifexp_lambda_and_default_callable_flow_in_closed_tree",
}


def collect_safe_preflight(project_root: Path) -> dict[str, Any]:
    """Run only P0--P3 authorization checks and never touch the candidate."""

    project_root = _raw_absolute(project_root)
    gates = {
        "source_lock": validate_source_lock(project_root),
        "upstream_bindings": validate_upstream_bindings(project_root),
        "executable_isolation": executable_isolation_scan(project_root / "code"),
        "proof_contract": audit_proof_contract(project_root),
        "controls": run_all_controls(project_root),
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
        "schema": "BASE2_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_tree_sha256(project_root),
        "gates": gates,
        "independent_review": review,
        "registered_candidate_runs": 0,
        "registered_candidate_periods_executed": [],
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "status": status,
        "pass": safe_pass,
    }


def write_safe_preflight(project_root: Path, output_root: Path | None = None) -> Path:
    """Write a deterministic safe audit; this never invokes P4."""

    project_root = _raw_absolute(project_root)
    output = _raw_absolute(output_root or project_root / "results")
    path = output / "PRE_EXECUTION_AUDIT.json"
    write_json(path, collect_safe_preflight(project_root))
    return path


def _exact_int(value: Any, expected: int) -> bool:
    return type(value) is int and value == expected


def _fraction(value: Any) -> Fraction | None:
    if type(value) is not str:
        return None
    try:
        parsed = Fraction(value)
    except (ValueError, ZeroDivisionError):
        return None
    return parsed if str(parsed) == value else None


@lru_cache(maxsize=1)
def _serialization_field():
    return candidate_field()


def _canonical_basis_expression(coefficients: list[Fraction]) -> str:
    field = _serialization_field()
    u = field.generator
    expression = sum(
        sp.Rational(item.numerator, item.denominator) * u**index
        for index, item in enumerate(coefficients)
    )
    converted = field.domain.from_sympy(expression)
    return sp.sstr(field.domain.to_sympy(converted))


def _validate_field_element(value: Any) -> tuple[list[str], Fraction | None]:
    errors: list[str] = []
    if type(value) is not dict or set(value) != ELEMENT_KEYS:
        return ["FIELD_ELEMENT_KEYS_NOT_EXACT"], None
    if value["domain"] != "QQ<u>" or value["basis"] != "1,u,u^2":
        errors.append("FIELD_ELEMENT_DOMAIN_OR_BASIS_MISMATCH")
    coefficients = value["coefficients_ascending"]
    fractions = [_fraction(item) for item in coefficients] if type(coefficients) is list else []
    if type(coefficients) is not list or len(coefficients) != 3 or any(item is None for item in fractions):
        errors.append("FIELD_ELEMENT_COEFFICIENTS_INVALID")
        return errors, None
    U = parameter_polynomial().gens[0]
    representative = sp.Poly(
        sum(
            sp.Rational(item.numerator, item.denominator) * U**index
            for index, item in enumerate(fractions)
        ),
        U,
        domain=sp.QQ,
    )
    exact_norm = sp.Rational(parameter_polynomial().resultant(representative))
    norm = Fraction(int(exact_norm.p), int(exact_norm.q))
    if value["expression"] != _canonical_basis_expression(fractions):
        errors.append("FIELD_ELEMENT_EXPRESSION_BASIS_MISMATCH")
    return errors, norm


def _validate_polynomial(
    value: Any,
    *,
    expected_degree: int | None = None,
    require_constant_one: bool = False,
) -> list[str]:
    if type(value) is not dict or set(value) != POLYNOMIAL_KEYS:
        return ["POLYNOMIAL_KEYS_NOT_EXACT"]
    errors: list[str] = []
    degree = value["degree"]
    if type(degree) is not int or degree < 0:
        errors.append("POLYNOMIAL_DEGREE_INVALID")
    elif expected_degree is not None and degree != expected_degree:
        errors.append("POLYNOMIAL_DEGREE_MISMATCH")
    coefficients = value["coefficients_descending"]
    basis_coefficients = value["coefficients_basis_descending"]
    if (
        type(coefficients) is not list
        or type(degree) is not int
        or len(coefficients) != degree + 1
        or any(type(item) is not str for item in coefficients)
    ):
        errors.append("POLYNOMIAL_COEFFICIENT_COUNT_INVALID")
    parsed_rows: list[list[Fraction]] = []
    if (
        type(basis_coefficients) is not list
        or type(degree) is not int
        or len(basis_coefficients) != degree + 1
        or any(
            type(row) is not list
            or len(row) != 3
            or any(_fraction(item) is None for item in row)
            for row in basis_coefficients
        )
    ):
        errors.append("POLYNOMIAL_BASIS_COEFFICIENTS_INVALID")
    else:
        parsed_rows = [
            [_fraction(item) for item in row]  # type: ignore[list-item]
            for row in basis_coefficients
        ]
        canonical_coefficients = [
            _canonical_basis_expression(row) for row in parsed_rows
        ]
        if coefficients != canonical_coefficients:
            errors.append("POLYNOMIAL_EXPRESSION_BASIS_MISMATCH")
        if not parsed_rows or all(item == 0 for item in parsed_rows[0]):
            errors.append("POLYNOMIAL_LEADING_COEFFICIENT_ZERO")
        elif parsed_rows[0] != [Fraction(1), Fraction(0), Fraction(0)]:
            errors.append("POLYNOMIAL_NOT_MONIC")
        if require_constant_one and (
            degree != 0
            or parsed_rows != [[Fraction(1), Fraction(0), Fraction(0)]]
        ):
            errors.append("POLYNOMIAL_NOT_CONSTANT_ONE")
    if value["domain"] != "QQ<u>" or value["coefficient_basis"] != "1,u,u^2":
        errors.append("POLYNOMIAL_DOMAIN_OR_BASIS_MISMATCH")
    if value["variable"] != "z":
        errors.append("POLYNOMIAL_VARIABLE_NOT_Z")
    return errors


def validate_period_records(records: Any) -> list[str]:
    """Validate all six nonempty records and both exact target certificates."""

    if type(records) is not list or len(records) != 6:
        return ["PERIOD_RECORDS_NOT_EXACTLY_SIX"]
    errors: list[str] = []
    formal_degrees = {2: 2, 3: 6, 4: 12, 5: 30, 6: 54, 7: 126}
    exact_degrees = formal_degrees
    for period, record in zip(range(2, 8), records, strict=True):
        prefix = f"N{period}:"
        if type(record) is not dict or set(record) != PERIOD_KEYS:
            errors.append(prefix + "PERIOD_KEYS_NOT_EXACT")
            continue
        exact_degree = exact_degrees[period]
        expected_scalars = {
            "period": period,
            "iterate_equation_degree": 2**period,
            "iterate_radical_degree": 2**period,
            "iterate_scheme_repeated_degree": 0,
            "formal_dynatomic_degree": formal_degrees[period],
            "formal_radical_degree": formal_degrees[period],
            "formal_scheme_repeated_degree": 0,
            "lower_overlap_degree": 2**period - exact_degree,
            "exact_set_degree": exact_degree,
            "exact_cycle_count": exact_degree // period,
            "formal_radical_equals_exact_set": True,
            "exact_set_squarefree": True,
            "exact_degree_divisible_by_period": True,
            "normalized_product_invariant": True,
            "status": "PASS",
            "run_id": f"R04{period}",
            "evidentiary_role": "DEVELOPMENT_SEEN_REPRODUCTION",
            "optional_q3_diagnostic": "NOT_REQUESTED",
        }
        for key, expected in expected_scalars.items():
            if record[key] != expected or type(record[key]) is not type(expected):
                errors.append(prefix + key.upper() + "_MISMATCH")
        if type(record["wall_time_nanoseconds"]) is not int or record[
            "wall_time_nanoseconds"
        ] < 0:
            errors.append(prefix + "WALL_TIME_INVALID")
        polynomial_degrees = {
            "iterate_equation": 2**period,
            "iterate_radical": 2**period,
            "formal_dynatomic": formal_degrees[period],
            "formal_radical": formal_degrees[period],
            "lower_overlap": 2**period - exact_degree,
            "exact_set_component": exact_degree,
            "normalized_cycle_product": 2**period - 1,
        }
        for key, expected_degree in polynomial_degrees.items():
            errors.extend(prefix + item for item in _validate_polynomial(record[key], expected_degree=expected_degree))
        targets = record["targets"]
        if type(targets) is not list or len(targets) != 2:
            errors.append(prefix + "TARGETS_NOT_EXACTLY_TWO")
            continue
        if [item.get("target") if type(item) is dict else None for item in targets] != ["1", "-1"]:
            errors.append(prefix + "TARGET_ORDER_OR_SET_MISMATCH")
        for target in targets:
            if type(target) is not dict or set(target) != TARGET_KEYS:
                errors.append(prefix + "TARGET_KEYS_NOT_EXACT")
                continue
            if not _exact_int(target["gcd_degree"], 0):
                errors.append(prefix + "TARGET_GCD_DEGREE_NOT_ZERO")
            if target["hit"] is not False:
                errors.append(prefix + "TARGET_HIT_NOT_FALSE")
            if target["field_norm_nonzero"] is not True:
                errors.append(prefix + "TARGET_NORM_NONZERO_FLAG_FAIL")
            if target["gcd_resultant_norm_agree"] is not True:
                errors.append(prefix + "TARGET_ENGINE_AGREEMENT_FAIL")
            element_errors, computed_norm = _validate_field_element(target["target_resultant"])
            errors.extend(prefix + item for item in element_errors)
            serialized_norm = _fraction(target["rational_field_norm"])
            if serialized_norm is None or serialized_norm == 0 or serialized_norm != computed_norm:
                errors.append(prefix + "TARGET_FIELD_NORM_INVALID")
            errors.extend(
                prefix + item
                for item in _validate_polynomial(
                    target["gcd_polynomial"],
                    expected_degree=0,
                    require_constant_one=True,
                )
            )
    return errors


def validate_official_preflight(payload: Any, live: dict[str, Any]) -> list[str]:
    """Require exact nonvacuous P0--P3 authority and canonical live equality."""

    if type(payload) is not dict or set(payload) != PRE_EXECUTION_KEYS:
        return ["PREFLIGHT_KEYS_NOT_EXACT"]
    errors: list[str] = []
    gates = payload["gates"]
    if type(gates) is not dict or set(gates) != GATE_KEYS:
        errors.append("PREFLIGHT_GATE_KEYS_NOT_EXACT")
    else:
        for key in GATE_KEYS:
            record = gates[key]
            if (
                type(record) is not dict
                or record.get("stage") != GATE_STAGES[key]
                or record.get("pass") is not True
            ):
                errors.append(f"PREFLIGHT_GATE_{key.upper()}_FAIL")
    scalar_checks = {
        "schema": "BASE2_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": live["reviewed_code_sha256"],
        "registered_candidate_runs": 0,
        "registered_candidate_periods_executed": [],
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
        "pass": True,
    }
    for key, expected in scalar_checks.items():
        if payload[key] != expected or type(payload[key]) is not type(expected):
            errors.append(f"PREFLIGHT_{key.upper()}_MISMATCH")
    if type(payload["independent_review"]) is not dict or payload[
        "independent_review"
    ].get("pass") is not True:
        errors.append("PREFLIGHT_REVIEW_GATE_FAIL")
    if canonical_json_bytes(payload) != canonical_json_bytes(live):
        errors.append("PREFLIGHT_NOT_CANONICALLY_EQUAL_TO_LIVE_GATES")
    return errors


def parse_passing_junit(path: Path) -> dict[str, Any]:
    """Parse, count, and bind a complete passing security-aware JUnit report."""

    errors: list[str] = []
    if not regular_file(path):
        return {"errors": ["JUNIT_MISSING_OR_UNSAFE"], "pass": False}
    data = stable_file_bytes(path)
    upper = data.upper()
    if b"<!DOCTYPE" in upper or b"<!ENTITY" in upper:
        return {"errors": ["JUNIT_DTD_OR_ENTITY_FORBIDDEN"], "pass": False}
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return {"errors": ["JUNIT_XML_MALFORMED"], "pass": False}
    suites = [root] if root.tag == "testsuite" else list(root) if root.tag == "testsuites" else []
    if not suites or any(suite.tag != "testsuite" for suite in suites):
        errors.append("JUNIT_ROOT_OR_SUITE_INVALID")
    testcases = [case for suite in suites for case in suite.findall("testcase")]
    totals = {key: 0 for key in ("tests", "errors", "failures", "skipped")}
    for suite in suites:
        for key in totals:
            raw = suite.attrib.get(key)
            if raw is None or not raw.isdigit():
                errors.append(f"JUNIT_{key.upper()}_COUNT_INVALID")
            else:
                totals[key] += int(raw)
    if totals["tests"] <= 0 or totals["tests"] != len(testcases):
        errors.append("JUNIT_TEST_COUNT_MISMATCH")
    if any(totals[key] != 0 for key in ("errors", "failures", "skipped")):
        errors.append("JUNIT_NONPASSING_COUNTS")
    if any(case.find("failure") is not None or case.find("error") is not None for case in testcases):
        errors.append("JUNIT_FAILURE_OR_ERROR_NODE_PRESENT")
    names = {case.attrib.get("name", "") for case in testcases}
    if not REQUIRED_JUNIT_TESTS.issubset(names):
        errors.append("JUNIT_REQUIRED_SECURITY_TESTS_MISSING")
    return {"counts": totals, "test_names": sorted(names), "errors": errors, "pass": not errors}


def _result_tree_inventory(project_root: Path) -> dict[str, Any]:
    results = project_root / "results"
    if not regular_directory(results):
        return {"files": [], "nested": [], "symlinks": ["<results>"], "extra": [], "missing": sorted(POST_RESULT_FILES), "pass": False}
    files: list[str] = []
    nested: list[str] = []
    symlinks: list[str] = []
    unsupported: list[str] = []
    try:
        entries = safe_directory_entries(results)
    except (OSError, RuntimeError):
        return {
            "files": [],
            "nested": [],
            "symlinks": ["<results-changed-or-unsafe>"],
            "unsupported": [],
            "extra": [],
            "missing": sorted(POST_RESULT_FILES),
            "pass": False,
        }
    for entry in entries:
        mode = entry["mode"]
        if stat.S_ISLNK(mode):
            symlinks.append(entry["name"])
        elif stat.S_ISDIR(mode):
            nested.append(entry["name"])
        elif stat.S_ISREG(mode) and entry["nlink"] == 1:
            files.append(entry["name"])
        else:
            unsupported.append(entry["name"])
    discovered = set(files)
    return {
        "files": sorted(files),
        "nested": sorted(nested),
        "symlinks": sorted(symlinks),
        "unsupported": sorted(unsupported),
        "extra": sorted(discovered.difference(POST_RESULT_FILES)),
        "missing": sorted(POST_RESULT_FILES.difference(discovered)),
        "pass": (
            not nested
            and not symlinks
            and not unsupported
            and discovered == POST_RESULT_FILES
        ),
    }


def _validate_terminal(
    terminal: Any,
    *,
    code_digest: str,
    claim_sha256: str,
    result_sha256: str,
    claim: dict[str, Any],
) -> list[str]:
    if type(terminal) is not dict or set(terminal) != TERMINAL_KEYS:
        return ["TERMINAL_KEYS_NOT_EXACT"]
    expected = {
        "schema": "BASE2_REGISTERED_RUN_TERMINAL_V1",
        "candidate_id": CANDIDATE_ID,
        "run_id": "REGISTERED_RUN_0001",
        "state": "COMPLETED_NO_HIT",
        "claim_path": CLAIM_RELATIVE,
        "claim_sha256": claim_sha256,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": code_digest,
        "review_file_sha256": claim["review_file_sha256"],
        "pre_execution_audit_sha256": claim["pre_execution_audit_sha256"],
        "registered_periods": list(range(2, 8)),
        "target_set": ["1", "-1"],
        "periods_started": list(range(2, 8)),
        "periods_completed": list(range(2, 8)),
        "stopped_period": None,
        "artifact_path": "results/EXPERIMENT_RESULTS.json",
        "artifact_sha256": result_sha256,
        "failure_code": None,
        "registered_run_count": 1,
        "candidate_numerical_runs": 0,
    }
    return [
        f"TERMINAL_{key.upper()}_MISMATCH"
        for key, value in expected.items()
        if terminal[key] != value or type(terminal[key]) is not type(value)
    ]


def build_post_run_manifest(project_root: Path) -> dict[str, Any]:
    """Close exact schemas, live gates, JUnit, one-shot state, and file inventory."""

    project_root = _raw_absolute(project_root)
    tree = _result_tree_inventory(project_root)
    errors: list[str] = []
    if not tree["pass"]:
        errors.append("RESULT_TREE_NOT_EXACT")
    files: list[dict[str, str]] = []
    missing: list[str] = []
    unsafe: list[str] = []
    for relative in POST_RUN_REQUIRED_FILES:
        path = project_root / relative
        if not regular_file(path):
            missing.append(relative)
        else:
            files.append({"path": relative, "sha256": sha256_file(path)})
    if missing or unsafe:
        errors.append("REQUIRED_FILE_SET_INCOMPLETE_OR_UNSAFE")
    code_digest = reviewed_code_tree_sha256(project_root)
    if not errors:
        live = collect_safe_preflight(project_root)
        review = validate_review_authority(project_root)
        official_preflight = load_exact_json(
            project_root / "results" / "PRE_EXECUTION_AUDIT.json"
        )
        errors.extend(validate_official_preflight(official_preflight, live))
        if review.get("pass") is not True:
            errors.append("LIVE_REVIEW_GATE_FAIL")
        claim_record = validate_registered_claim(project_root, code_digest)
        if claim_record["pass"] is not True:
            errors.append("REGISTERED_CLAIM_INVALID")
            claim_payload: dict[str, Any] = {}
            claim_sha = ""
        else:
            claim_payload = claim_record["payload"]
            claim_sha = claim_record["claim_sha256"]
        result_path = project_root / "results" / "EXPERIMENT_RESULTS.json"
        result = load_exact_json(result_path)
        if type(result) is not dict or set(result) != RESULT_KEYS:
            errors.append("RESULT_KEYS_NOT_EXACT")
        else:
            top_expected = {
                "schema": "BASE2_REGISTERED_CANDIDATE_AUDIT_V1",
                "candidate_id": CANDIDATE_ID,
                "source_lock_sha256": EXPECTED_LOCK_SHA256,
                "reviewed_code_sha256": code_digest,
                "registered_claim_sha256": claim_sha,
                "registered_periods_frozen": list(range(2, 8)),
                "periods_executed": list(range(2, 8)),
                "new_blind_periods": [],
                "development_seen_periods": list(range(2, 8)),
                "stopped_on_target_hit": False,
                "completed_frozen_cutoff": True,
                "candidate_numerical_runs": 0,
                "external_prime_tables_accessed": False,
                "riemann_zero_data_accessed": False,
                "approximate_matching_used": False,
                "classification": "BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN",
                "all_period_equality_status": "OPEN_FOR_N_GE_4",
                "route_a": "NOT_ADVANCED",
                "route_b": "NOT_OPENED",
                "pass": True,
            }
            for key, expected in top_expected.items():
                if result[key] != expected or type(result[key]) is not type(expected):
                    errors.append(f"RESULT_{key.upper()}_MISMATCH")
            errors.extend(validate_period_records(result["period_records"]))
            if canonical_json_bytes(result["pre_execution_gates"]) != canonical_json_bytes(
                live["gates"]
            ):
                errors.append("RESULT_PREFLIGHT_GATES_NOT_LIVE_EXACT")
            if canonical_json_bytes(result["independent_review_gate"]) != canonical_json_bytes(
                review
            ):
                errors.append("RESULT_REVIEW_GATE_NOT_LIVE_EXACT")
        result_sha = sha256_file(result_path)
        terminal = load_exact_json(project_root / TERMINAL_RELATIVE)
        if claim_payload:
            errors.extend(
                _validate_terminal(
                    terminal,
                    code_digest=code_digest,
                    claim_sha256=claim_sha,
                    result_sha256=result_sha,
                    claim=claim_payload,
                )
            )
        junit = parse_passing_junit(project_root / "results" / "pytest.xml")
        if junit["pass"] is not True:
            errors.extend(junit["errors"])
    return {
        "schema": "BASE2_RESULT_MANIFEST_V2",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": code_digest,
        "result_tree": tree,
        "files": files,
        "missing": missing,
        "unsafe": unsafe,
        "semantic_errors": errors,
        "pass": not errors,
    }


def write_post_run_manifest(project_root: Path) -> Path:
    """Create the final manifest exclusively after strict validation."""

    project_root = _raw_absolute(project_root)
    manifest = build_post_run_manifest(project_root)
    if not manifest["pass"]:
        raise RuntimeError("post-run manifest validation failed")
    path = project_root / "results" / "result_manifest.json"
    write_json(path, manifest, exclusive=True)
    return path
