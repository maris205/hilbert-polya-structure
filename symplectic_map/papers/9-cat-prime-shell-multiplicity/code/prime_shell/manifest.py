"""Registered-result semantics and strict post-run manifest closure."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .constants import (
    CAT_MATRIX,
    CANDIDATE_ID,
    CLAIM_PATH,
    CODE_REVIEW_PATH,
    EXPECTED_LEDGER,
    EXPECTED_RAW_FACTORS,
    LOCKED_PRIMES,
    OFFICIAL_REPORT_PATHS,
    POSTRUN_TEST_PATH,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
    RESULT_MANIFEST_PATH,
    RESULT_PATH,
    RESULT_REVIEW_PATH,
    SOURCE_LOCK_SHA256,
    TERMINAL_LABELS,
    TERMINAL_PATH,
)
from .mechanisms import mechanism_audit, symbolic_composite_control
from .gates import (
    collect_safe_preflight,
    parse_junit,
    validate_source_and_design,
    validate_upstream,
)
from .lifecycle import validate_claim
from .proof_contract import proof_only_contract, validate_proof_only_contract
from .protocol import (
    canonical_json_bytes,
    code_tree_sha256,
    lexical_absolute,
    load_exact_json,
    regular_file,
    sha256_file,
    stable_file_bytes,
    strict_json_loads,
    pretty_json_bytes,
    write_json,
)
from .review import validate_deployment_authority, validate_result_authority
from .symbolic import symbolic_product_audit


PREMANIFEST_RESULT_FILES = frozenset(
    {
        Path(CODE_REVIEW_PATH).name,
        Path(PREEXECUTION_TEST_PATH).name,
        Path(PREEXECUTION_AUDIT_PATH).name,
        Path(CLAIM_PATH).name,
        Path(RESULT_PATH).name,
        Path(TERMINAL_PATH).name,
        Path(POSTRUN_TEST_PATH).name,
        Path(RESULT_REVIEW_PATH).name,
    }
)
FINAL_RESULT_FILES = PREMANIFEST_RESULT_FILES | {Path(RESULT_MANIFEST_PATH).name}

PREEXECUTION_GATE_KEYS = frozenset(
    {"source_and_design", "upstream", "executable_isolation", "source_schema_contract", "test_evidence"}
)
PREEXECUTION_AUDIT_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "reviewed_code_sha256",
        "gates",
        "independent_review",
        "locked_primes",
        "formal_repeats",
        "registered_exact_audits",
        "registered_primes_executed",
        "candidate_numerical_runs",
        "external_prime_tables_accessed",
        "generated_prime_target_arrays",
        "riemann_zero_data_accessed",
        "numeric_s_or_log_evaluations",
        "centralizer_computations_run",
        "status",
        "pass",
    }
)
AUDIT_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "fixed_matrix",
        "locked_primes",
        "development_seen_controls",
        "rows",
        "controls",
        "symbolic_composite_control",
        "proof_only_contract",
        "proof_contract_validation",
        "terminal_labels",
        "registered_exact_audits",
        "candidate_numerical_runs",
        "external_prime_tables_accessed",
        "generated_prime_target_arrays",
        "riemann_zero_data_accessed",
        "numeric_s_or_log_evaluations",
        "composite_shells_enumerated",
        "centralizer_computations_run",
        "parameter_or_matrix_searches",
        "normalization_or_selector_searches",
        "all_prime_inference_from_finite_audit",
        "global_convergence_inference_from_finite_audit",
        "classification",
        "pass",
    }
)
ROW_KEYS = frozenset(
    {
        "prime",
        "case",
        "shell_cardinality",
        "point_period_profile",
        "cycle_profile",
        "m_p",
        "eigenline_cycles",
        "off_eigenline_cycles",
        "analytic_engine",
        "direct_engine",
        "dual_engine_match",
        "frozen_expected_match",
        "raw_factor",
        "raw_factor_frozen_match",
        "product_audit",
        "mechanism_audit",
        "evidence_role",
        "pass",
    }
)
DIRECT_ENGINE_KEYS = frozenset(
    {
        "engine",
        "prime",
        "shell_cardinality",
        "point_period_profile",
        "cycle_profile",
        "m_p",
        "eigenline_cycles",
        "off_eigenline_cycles",
        "canonical_cycles",
        "partition_exact",
    }
)
ANALYTIC_COMMON_KEYS = frozenset(
    {
        "engine",
        "prime",
        "shell_cardinality",
        "eigenline_cycles",
        "off_eigenline_cycles",
        "case",
        "tau_p",
        "tau_divides",
        "divisibility_pass",
        "point_period_profile",
        "cycle_profile",
        "m_p",
        "case_checks",
    }
)
CONTROL_KEYS = frozenset(
    {
        "K001_shell_partition",
        "K002_binary_exception",
        "K003_ramified_mixture",
        "K004_odd_bound",
        "K005_split_strata",
        "K006_product_separation",
        "K007_repetition",
        "K008_equal_weight_failure",
        "K009_fractional_identity",
        "K010_selector_cost",
        "K011_analytic_boundary",
        "K012_escape_boundary",
    }
)


def _exact_integer(value: Any, expected: int) -> bool:
    return type(value) is int and value == expected


def _exact_value(value: Any, expected: Any) -> bool:
    if type(value) is not type(expected):
        return False
    if type(expected) in {list, dict}:
        return canonical_json_bytes(value) == canonical_json_bytes(expected)
    return value == expected


def _normalize_profile(value: Any) -> dict[int, int] | None:
    if type(value) is not dict:
        return None
    result: dict[int, int] = {}
    for key, count in value.items():
        if type(key) is int:
            period = key
        elif type(key) is str and key.isdigit() and str(int(key)) == key:
            period = int(key)
        else:
            return None
        if type(count) is not int or count < 1 or period < 1 or period in result:
            return None
        result[period] = count
    return dict(sorted(result.items()))


def _validate_direct_engine(value: Any, prime: int, errors: list[str]) -> dict[str, Any] | None:
    label = f"P{prime}_DIRECT_"
    if type(value) is not dict or set(value) != DIRECT_ENGINE_KEYS:
        errors.append(label + "KEYS_NOT_EXACT")
        return None
    expected = EXPECTED_LEDGER[prime]
    point_profile = _normalize_profile(value["point_period_profile"])
    cycle_profile = _normalize_profile(value["cycle_profile"])
    scalar_expected = {
        "engine": "DIRECT_POINT_PERMUTATION",
        "prime": prime,
        "shell_cardinality": prime * prime - 1,
        "m_p": expected["m_p"],
        "eigenline_cycles": expected["eigenline_cycles"],
        "off_eigenline_cycles": expected["off_eigenline_cycles"],
        "partition_exact": True,
    }
    for key, target in scalar_expected.items():
        current = value.get(key)
        if not _exact_value(current, target):
            errors.append(label + key.upper() + "_MISMATCH")
    if point_profile != expected["point_period_profile"]:
        errors.append(label + "POINT_PROFILE_MISMATCH")
    if cycle_profile != expected["cycle_profile"]:
        errors.append(label + "CYCLE_PROFILE_MISMATCH")
    cycles = value.get("canonical_cycles")
    flattened: list[tuple[int, int]] = []
    observed_cycle_profile: dict[int, int] = {}
    if type(cycles) is not list or len(cycles) != expected["m_p"]:
        errors.append(label + "CYCLES_NOT_EXACT_LIST")
    else:
        normalized_cycles: list[tuple[tuple[int, int], ...]] = []
        for cycle in cycles:
            if type(cycle) is not list or not cycle:
                errors.append(label + "CYCLE_INVALID")
                continue
            normalized: list[tuple[int, int]] = []
            for point in cycle:
                if (
                    type(point) is not list
                    or len(point) != 2
                    or any(type(coordinate) is not int for coordinate in point)
                ):
                    errors.append(label + "POINT_INVALID")
                    normalized = []
                    break
                vector = (point[0], point[1])
                if not (0 <= vector[0] < prime and 0 <= vector[1] < prime) or vector == (0, 0):
                    errors.append(label + "POINT_OUTSIDE_SHELL")
                normalized.append(vector)
            if not normalized:
                continue
            normalized_tuple = tuple(normalized)
            if normalized_tuple[0] != min(normalized_tuple):
                errors.append(label + "CYCLE_NOT_CANONICAL")
            for index, vector in enumerate(normalized_tuple):
                following = normalized_tuple[(index + 1) % len(normalized_tuple)]
                image = (
                    (CAT_MATRIX[0][0] * vector[0] + CAT_MATRIX[0][1] * vector[1]) % prime,
                    (CAT_MATRIX[1][0] * vector[0] + CAT_MATRIX[1][1] * vector[1]) % prime,
                )
                if image != following:
                    errors.append(label + "CYCLE_ACTION_MISMATCH")
                    break
            normalized_cycles.append(normalized_tuple)
            flattened.extend(normalized_tuple)
            observed_cycle_profile[len(normalized_tuple)] = (
                observed_cycle_profile.get(len(normalized_tuple), 0) + 1
            )
        if normalized_cycles != sorted(normalized_cycles):
            errors.append(label + "CYCLE_LIST_NOT_SORTED")
    expected_points = {
        (first, second)
        for first in range(prime)
        for second in range(prime)
        if (first, second) != (0, 0)
    }
    if len(flattened) != len(set(flattened)) or set(flattened) != expected_points:
        errors.append(label + "PARTITION_NOT_EXACT")
    if dict(sorted(observed_cycle_profile.items())) != expected["cycle_profile"]:
        errors.append(label + "OBSERVED_CYCLE_PROFILE_MISMATCH")
    if point_profile is None or cycle_profile is None:
        return None
    normalized_value = dict(value)
    normalized_value["point_period_profile"] = point_profile
    normalized_value["cycle_profile"] = cycle_profile
    return normalized_value


def _validate_analytic_engine(value: Any, prime: int, errors: list[str]) -> dict[str, Any] | None:
    label = f"P{prime}_ANALYTIC_"
    extra = {"nilpotent"} if prime == 5 else {"legendre_five", "h_p"} if prime not in {2, 5} else set()
    if type(value) is not dict or set(value) != set(ANALYTIC_COMMON_KEYS) | extra:
        errors.append(label + "KEYS_NOT_EXACT")
        return None
    expected = EXPECTED_LEDGER[prime]
    point_profile = _normalize_profile(value["point_period_profile"])
    cycle_profile = _normalize_profile(value["cycle_profile"])
    tau = {2: 3, 3: 4, 5: None, 7: 8, 11: 5}[prime]
    divisor = {2: "p+1", 3: "p+1", 5: None, 7: "p+1", 11: "p-1"}[prime]
    divisibility = None if prime == 5 else True
    scalar_expected = {
        "engine": "ANALYTIC_CASE_CLASSIFICATION",
        "prime": prime,
        "shell_cardinality": prime * prime - 1,
        "case": expected["case"],
        "tau_p": tau,
        "tau_divides": divisor,
        "divisibility_pass": divisibility,
        "m_p": expected["m_p"],
        "eigenline_cycles": expected["eigenline_cycles"],
        "off_eigenline_cycles": expected["off_eigenline_cycles"],
    }
    for key, target in scalar_expected.items():
        current = value.get(key)
        if not _exact_value(current, target):
            errors.append(label + key.upper() + "_MISMATCH")
    if point_profile != expected["point_period_profile"]:
        errors.append(label + "POINT_PROFILE_MISMATCH")
    if cycle_profile != expected["cycle_profile"]:
        errors.append(label + "CYCLE_PROFILE_MISMATCH")
    checks = value.get("case_checks")
    expected_check_keys = (
        {"cayley_hamilton_order_three"}
        if prime == 2
        else {
            "A_equals_minus_I_plus_N",
            "N_square_zero",
            "N_rank_one",
            "kernel_size_five",
        }
        if prime == 5
        else {"uniform_period_formula", "odd_lower_bound"}
    )
    if (
        type(checks) is not dict
        or set(checks) != expected_check_keys
        or any(type(item) is not bool or item is not True for item in checks.values())
    ):
        errors.append(label + "CASE_CHECKS_NOT_EXACT_TRUE_MAP")
    if prime == 5 and not _exact_value(value.get("nilpotent"), [[3, 1], [1, 2]]):
        errors.append(label + "NILPOTENT_MISMATCH")
    if prime in {3, 7, 11}:
        legendre = -1 if prime in {3, 7} else 1
        h_p = 1 if prime in {3, 7} else 2
        if not _exact_integer(value.get("legendre_five"), legendre):
            errors.append(label + "LEGENDRE_MISMATCH")
        if not _exact_integer(value.get("h_p"), h_p):
            errors.append(label + "H_P_MISMATCH")
    if point_profile is None or cycle_profile is None:
        return None
    normalized_value = dict(value)
    normalized_value["point_period_profile"] = point_profile
    normalized_value["cycle_profile"] = cycle_profile
    return normalized_value


def _validate_audit_payload(audit: Any) -> list[str]:
    errors: list[str] = []
    if type(audit) is not dict or set(audit) != AUDIT_KEYS:
        return ["AUDIT_KEYS_NOT_EXACT"]
    scalar_expected = {
        "schema": "PRIME_SHELL_REGISTERED_EXACT_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "fixed_matrix": [[2, 1], [1, 1]],
        "locked_primes": list(LOCKED_PRIMES),
        "development_seen_controls": True,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "all_prime_inference_from_finite_audit": False,
        "global_convergence_inference_from_finite_audit": False,
        "classification": (
            "PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED / "
            "A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED"
        ),
        "pass": True,
    }
    for key, target in scalar_expected.items():
        current = audit.get(key)
        if not _exact_value(current, target):
            errors.append("AUDIT_" + key.upper() + "_MISMATCH")
    integer_expected = {
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "generated_prime_target_arrays": 0,
        "numeric_s_or_log_evaluations": 0,
        "composite_shells_enumerated": 0,
        "centralizer_computations_run": 0,
        "parameter_or_matrix_searches": 0,
        "normalization_or_selector_searches": 0,
    }
    for key, target in integer_expected.items():
        if not _exact_integer(audit.get(key), target):
            errors.append("AUDIT_" + key.upper() + "_NOT_EXACT_INT")
    rows = audit.get("rows")
    if type(rows) is not list or len(rows) != len(LOCKED_PRIMES):
        errors.append("AUDIT_ROWS_NOT_FIVE_ELEMENT_LIST")
    else:
        observed_primes = [row.get("prime") if type(row) is dict else None for row in rows]
        if observed_primes != list(LOCKED_PRIMES) or any(type(value) is not int for value in observed_primes):
            errors.append("AUDIT_ROW_PRIME_ORDER_NOT_EXACT")
        for prime, row in zip(LOCKED_PRIMES, rows, strict=True):
            label = f"P{prime}_ROW_"
            if type(row) is not dict or set(row) != ROW_KEYS:
                errors.append(label + "KEYS_NOT_EXACT")
                continue
            expected = EXPECTED_LEDGER[prime]
            point_profile = _normalize_profile(row["point_period_profile"])
            cycle_profile = _normalize_profile(row["cycle_profile"])
            row_scalars = {
                "prime": prime,
                "case": expected["case"],
                "shell_cardinality": prime * prime - 1,
                "m_p": expected["m_p"],
                "eigenline_cycles": expected["eigenline_cycles"],
                "off_eigenline_cycles": expected["off_eigenline_cycles"],
                "dual_engine_match": True,
                "frozen_expected_match": True,
                "raw_factor": EXPECTED_RAW_FACTORS[prime],
                "raw_factor_frozen_match": True,
                "evidence_role": "FINITE_FALSIFICATION_CONTROL",
                "pass": True,
            }
            for key, target in row_scalars.items():
                current = row.get(key)
                if not _exact_value(current, target):
                    errors.append(label + key.upper() + "_MISMATCH")
            if point_profile != expected["point_period_profile"]:
                errors.append(label + "POINT_PROFILE_MISMATCH")
            if cycle_profile != expected["cycle_profile"]:
                errors.append(label + "CYCLE_PROFILE_MISMATCH")
            direct = _validate_direct_engine(row["direct_engine"], prime, errors)
            analytic = _validate_analytic_engine(row["analytic_engine"], prime, errors)
            if direct is not None:
                if canonical_json_bytes(row["product_audit"]) != canonical_json_bytes(
                    symbolic_product_audit(direct)
                ):
                    errors.append(label + "PRODUCT_AUDIT_NOT_EXACT")
                if canonical_json_bytes(row["mechanism_audit"]) != canonical_json_bytes(
                    mechanism_audit(direct)
                ):
                    errors.append(label + "MECHANISM_AUDIT_NOT_EXACT")
            if direct is not None and analytic is not None:
                projection_keys = (
                    "prime",
                    "shell_cardinality",
                    "point_period_profile",
                    "cycle_profile",
                    "m_p",
                    "eigenline_cycles",
                    "off_eigenline_cycles",
                )
                if {key: direct[key] for key in projection_keys} != {
                    key: analytic[key] for key in projection_keys
                }:
                    errors.append(label + "DUAL_ENGINE_PROJECTION_MISMATCH")
    controls = audit.get("controls")
    if (
        type(controls) is not dict
        or set(controls) != CONTROL_KEYS
        or any(type(value) is not bool or value is not True for value in controls.values())
    ):
        errors.append("AUDIT_CONTROLS_NOT_EXACT_TRUE_MAP")
    if canonical_json_bytes(audit.get("symbolic_composite_control")) != canonical_json_bytes(
        symbolic_composite_control()
    ):
        errors.append("AUDIT_SYMBOLIC_COMPOSITE_CONTROL_NOT_EXACT")
    expected_proof = proof_only_contract()
    if canonical_json_bytes(audit.get("proof_only_contract")) != canonical_json_bytes(expected_proof):
        errors.append("AUDIT_PROOF_ONLY_CONTRACT_NOT_EXACT")
    expected_proof_validation = validate_proof_only_contract(expected_proof)
    if canonical_json_bytes(audit.get("proof_contract_validation")) != canonical_json_bytes(
        expected_proof_validation
    ):
        errors.append("AUDIT_PROOF_VALIDATION_NOT_EXACT")
    if audit.get("terminal_labels") != list(TERMINAL_LABELS) or any(
        type(value) is not str for value in audit.get("terminal_labels", [])
    ):
        errors.append("AUDIT_TERMINAL_LABELS_NOT_EXACT")
    return errors


def validate_registered_result(payload: Any, project_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    if type(payload) is not dict:
        return {"stage": "R090_REGISTERED_RESULT_SEMANTICS", "errors": ["RESULT_NOT_OBJECT"], "pass": False}
    required = {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "reviewed_code_sha256",
        "registered_claim_sha256",
        "pre_execution_gates",
        "independent_review_gate",
        "audit",
        "registered_exact_audits",
        "candidate_numerical_runs",
        "pass",
    }
    if set(payload) != required:
        errors.append("RESULT_KEYS_NOT_EXACT")
        return {"stage": "R090_REGISTERED_RESULT_SEMANTICS", "errors": errors, "pass": False}
    root = lexical_absolute(project_root)
    code_sha = code_tree_sha256(root)
    claim = validate_claim(root, code_sha)
    if claim.get("pass") is not True:
        errors.append("REGISTERED_CLAIM_NOT_PASSING")
    expected_scalars = {
        "schema": "PRIME_SHELL_OFFICIAL_RESULT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_sha,
        "registered_claim_sha256": claim.get("claim_sha256"),
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "pass": True,
    }
    for key, value in expected_scalars.items():
        if not _exact_value(payload.get(key), value):
            errors.append("RESULT_" + key.upper() + "_MISMATCH")
    errors.extend(_validate_audit_payload(payload.get("audit")))
    official_path = root / PREEXECUTION_AUDIT_PATH
    official = load_exact_json(official_path) if regular_file(official_path) else None
    if type(official) is not dict:
        errors.append("OFFICIAL_PREFLIGHT_MISSING_OR_INVALID")
    else:
        if set(official) != PREEXECUTION_AUDIT_KEYS:
            errors.append("OFFICIAL_PREFLIGHT_KEYS_NOT_EXACT")
        live_preflight = collect_safe_preflight(root)
        if live_preflight.get("pass") is not True or live_preflight.get("status") != (
            "AUTHORIZED_FOR_REGISTERED_EXECUTION"
        ):
            errors.append("LIVE_PREFLIGHT_NOT_AUTHORIZED")
        if canonical_json_bytes(official) != canonical_json_bytes(live_preflight):
            errors.append("OFFICIAL_PREFLIGHT_NOT_LIVE_EXACT_RECOMPUTATION")
        official_checks = {
            "schema": "PRIME_SHELL_PRE_EXECUTION_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "reviewed_code_sha256": code_sha,
            "locked_primes": list(LOCKED_PRIMES),
            "formal_repeats": [1, 2, 3],
            "registered_exact_audits": 0,
            "registered_primes_executed": [],
            "candidate_numerical_runs": 0,
            "external_prime_tables_accessed": False,
            "generated_prime_target_arrays": 0,
            "riemann_zero_data_accessed": False,
            "numeric_s_or_log_evaluations": 0,
            "centralizer_computations_run": 0,
            "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
            "pass": True,
        }
        for key, target in official_checks.items():
            current = official.get(key)
            if not _exact_value(current, target):
                errors.append("OFFICIAL_PREFLIGHT_" + key.upper() + "_MISMATCH")
        official_gates = official.get("gates")
        if (
            type(official_gates) is not dict
            or set(official_gates) != PREEXECUTION_GATE_KEYS
            or any(
                type(record) is not dict or record.get("pass") is not True
                for record in official_gates.values()
            )
        ):
            errors.append("OFFICIAL_PREFLIGHT_GATES_NOT_EXACT_PASSING_SET")
        if canonical_json_bytes(payload.get("pre_execution_gates")) != canonical_json_bytes(
            official_gates
        ):
            errors.append("EMBEDDED_PREFLIGHT_GATES_NOT_OFFICIAL_EXACT")
        live_review = validate_deployment_authority(root)
        if live_review.get("pass") is not True:
            errors.append("LIVE_DEPLOYMENT_REVIEW_NOT_PASSING")
        if canonical_json_bytes(official.get("independent_review")) != canonical_json_bytes(
            live_review
        ):
            errors.append("OFFICIAL_DEPLOYMENT_REVIEW_NOT_LIVE_EXACT")
        if canonical_json_bytes(payload.get("independent_review_gate")) != canonical_json_bytes(
            live_review
        ):
            errors.append("EMBEDDED_DEPLOYMENT_REVIEW_NOT_LIVE_EXACT")
    return {"stage": "R090_REGISTERED_RESULT_SEMANTICS", "errors": errors, "pass": not errors}


def _result_inventory(project_root: Path, expected: frozenset[str]) -> dict[str, Any]:
    root = lexical_absolute(project_root) / "results"
    first = sorted(entry.name for entry in root.iterdir())
    second = sorted(entry.name for entry in root.iterdir())
    errors: list[str] = []
    if first != second:
        errors.append("RESULT_INVENTORY_UNSTABLE")
    if set(first) != set(expected) or len(first) != len(expected):
        errors.append("RESULT_INVENTORY_NOT_EXACT")
    for name in expected:
        if not regular_file(root / name):
            errors.append("RESULT_FILE_UNSAFE_OR_MISSING:" + name)
    return {"observed": first, "expected": sorted(expected), "errors": errors, "pass": not errors}


def _evidence_inventory(project_root: Path) -> dict[str, Any]:
    """Validate immutable evidence while ignoring only the manifest's own path."""

    root = lexical_absolute(project_root) / "results"
    manifest_name = Path(RESULT_MANIFEST_PATH).name
    first = sorted(entry.name for entry in root.iterdir() if entry.name != manifest_name)
    second = sorted(entry.name for entry in root.iterdir() if entry.name != manifest_name)
    errors: list[str] = []
    if first != second:
        errors.append("EVIDENCE_INVENTORY_UNSTABLE")
    if set(first) != set(PREMANIFEST_RESULT_FILES) or len(first) != len(PREMANIFEST_RESULT_FILES):
        errors.append("EVIDENCE_INVENTORY_NOT_EXACT")
    for name in PREMANIFEST_RESULT_FILES:
        if not regular_file(root / name):
            errors.append("EVIDENCE_FILE_UNSAFE_OR_MISSING:" + name)
    return {
        "observed": first,
        "expected": sorted(PREMANIFEST_RESULT_FILES),
        "manifest_excluded_from_evidence_inventory": True,
        "errors": errors,
        "pass": not errors,
    }


def collect_postrun_audit(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    code_sha = code_tree_sha256(root)
    inventory = _evidence_inventory(root)
    claim = validate_claim(root, code_sha)
    result = load_exact_json(root / RESULT_PATH) if regular_file(root / RESULT_PATH) else None
    result_semantics = validate_registered_result(result, root)
    terminal_errors: list[str] = []
    terminal = load_exact_json(root / TERMINAL_PATH) if regular_file(root / TERMINAL_PATH) else None
    if type(terminal) is not dict:
        terminal_errors.append("TERMINAL_MISSING_OR_INVALID")
    else:
        if terminal.get("state") != "COMPLETED_CERTIFIED":
            terminal_errors.append("TERMINAL_NOT_CERTIFIED")
        if terminal.get("reviewed_code_sha256") != code_sha:
            terminal_errors.append("TERMINAL_CODE_SHA_MISMATCH")
        if terminal.get("claim_sha256") != claim.get("claim_sha256"):
            terminal_errors.append("TERMINAL_CLAIM_SHA_MISMATCH")
        if terminal.get("result_sha256") != sha256_file(root / RESULT_PATH):
            terminal_errors.append("TERMINAL_RESULT_SHA_MISMATCH")
        if terminal.get("primes_started") != list(LOCKED_PRIMES):
            terminal_errors.append("TERMINAL_STARTED_PRIMES_MISMATCH")
        if terminal.get("primes_completed") != list(LOCKED_PRIMES):
            terminal_errors.append("TERMINAL_COMPLETED_PRIMES_MISMATCH")
    postrun_tests = parse_junit(root / POSTRUN_TEST_PATH)
    postrun_tests["stage"] = "R091_POSTRUN_TEST_EVIDENCE"
    postrun_tests["path"] = POSTRUN_TEST_PATH
    reports = []
    for relative in OFFICIAL_REPORT_PATHS:
        reports.append(
            {
                "path": relative,
                "sha256": sha256_file(root / relative) if regular_file(root / relative) else None,
                "pass": regular_file(root / relative),
            }
        )
    gates = {
        "inventory": inventory,
        "source": validate_source_and_design(root),
        "upstream": validate_upstream(root),
        "deployment_review": validate_deployment_authority(root),
        "claim": claim,
        "result_semantics": result_semantics,
        "terminal": {"errors": terminal_errors, "pass": not terminal_errors},
        "postrun_tests": postrun_tests,
        "official_reports": {"records": reports, "pass": all(item["pass"] for item in reports)},
        "independent_result_review": validate_result_authority(root, code_sha),
    }
    return {
        "schema": "PRIME_SHELL_POSTRUN_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "execution_code_sha256": code_sha,
        "gates": gates,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "candidate_rerun_performed": False,
        "pass": all(item.get("pass") is True for item in gates.values()),
    }


def _manifest_payload(project_root: Path, expected_inventory: frozenset[str]) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    audit = collect_postrun_audit(root)
    errors: list[str] = []
    if audit["pass"] is not True:
        errors.append("POSTRUN_AUDIT_NOT_PASSING")
    inventory = _result_inventory(root, expected_inventory)
    errors.extend(inventory["errors"])
    paths = sorted(
        {f"results/{name}" for name in PREMANIFEST_RESULT_FILES}
        | set(OFFICIAL_REPORT_PATHS)
    )
    files = []
    for relative in paths:
        if not regular_file(root / relative):
            errors.append("MANIFEST_INPUT_MISSING_OR_UNSAFE:" + relative)
        else:
            files.append({"path": relative, "sha256": sha256_file(root / relative)})
    return {
        "schema": "PRIME_SHELL_RESULT_MANIFEST_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "execution_code_sha256": audit["execution_code_sha256"],
        "postrun_audit": audit,
        "result_inventory": {
            "prewrite_files": sorted(PREMANIFEST_RESULT_FILES),
            "final_files": sorted(FINAL_RESULT_FILES),
            "manifest_path": RESULT_MANIFEST_PATH,
            "manifest_self_hash_recorded": False,
        },
        "files": files,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "candidate_rerun_performed": False,
        "errors": errors,
        "pass": not errors,
    }


def write_result_manifest(project_root: Path) -> Path:
    root = lexical_absolute(project_root)
    output = root / RESULT_MANIFEST_PATH
    if output.exists():
        raise FileExistsError("result manifest is one-shot and already exists")
    payload = _manifest_payload(root, PREMANIFEST_RESULT_FILES)
    if payload["pass"] is not True:
        raise RuntimeError("strict post-run manifest gates failed")
    write_json(output, payload, exclusive=True)
    closure = validate_existing_manifest(root)
    if closure["pass"] is not True:
        raise RuntimeError("written result manifest failed live closure")
    return output


def validate_existing_manifest(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    path = root / RESULT_MANIFEST_PATH
    errors: list[str] = []
    inventory = _result_inventory(root, FINAL_RESULT_FILES)
    errors.extend(inventory["errors"])
    raw: bytes | None = None
    stored: Any = None
    if not regular_file(path):
        errors.append("RESULT_MANIFEST_MISSING_OR_UNSAFE")
    else:
        try:
            raw = stable_file_bytes(path)
            stored = strict_json_loads(raw.decode("utf-8"))
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError):
            errors.append("RESULT_MANIFEST_INVALID_JSON")
    if type(stored) is not dict:
        errors.append("RESULT_MANIFEST_NOT_OBJECT")
    else:
        if raw != pretty_json_bytes(stored):
            errors.append("RESULT_MANIFEST_BYTES_NOT_CANONICAL")
        recomputed = _manifest_payload(root, FINAL_RESULT_FILES)
        if recomputed["pass"] is not True:
            errors.append("LIVE_MANIFEST_CLOSURE_NOT_PASSING")
        elif canonical_json_bytes(stored) != canonical_json_bytes(recomputed):
            errors.append("RESULT_MANIFEST_STALE_OR_TAMPERED")
    return {
        "stage": "R100_FINAL_MANIFEST_CLOSURE",
        "manifest_sha256": hashlib.sha256(raw).hexdigest() if raw is not None else None,
        "errors": errors,
        "pass": not errors,
    }
