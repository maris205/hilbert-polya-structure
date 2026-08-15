"""Read-only audit of the immutable execution chain and repaired K005 boundary."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .constants import (
    ANALYZER_JUNIT_PATH,
    CANDIDATE_ID,
    CONTROL_KEYS,
    EXECUTION_TREE_SHA256,
    EXPECTED_LEDGER,
    FIRST_MANIFEST_ATTEMPT,
    IMMUTABLE_ARTIFACTS,
    LOCKED_MODULI,
    SOURCE_LOCK_SHA256,
    TERMINAL_CLASSIFICATION,
)
from .protocol import (
    analyzer_executable_isolation,
    analyzer_tree_sha256,
    canonical_json_bytes,
    execution_tree_sha256,
    load_exact_json,
    parse_analyzer_junit,
    regular_file,
    sha256_file,
)
from .review import validate_analyzer_authority, validate_execution_authorities


OUTER_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "reviewed_code_sha256",
        "registered_claim_sha256",
        "pre_execution_gates",
        "independent_review_gate",
        "audit",
        "registered_audit_count",
        "candidate_numerical_run_count",
        "pass",
    }
)
AUDIT_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "fixed_matrix",
        "arithmetic_modulus_order",
        "arithmetic_modulus_records",
        "structural_unit_control",
        "controls",
        "proof_only_contract",
        "proof_contract_validation",
        "registered_audit_count",
        "arithmetic_modulus_record_count",
        "structural_unit_control_count",
        "structural_control_in_modulus_namespace",
        "candidate_rerun_count",
        "candidate_numerical_run_count",
        "network_access_count",
        "external_prime_data_access_count",
        "riemann_zero_data_access_count",
        "numeric_s_evaluation_count",
        "numeric_log_q_evaluation_count",
        "numeric_q_power_minus_s_evaluation_count",
        "random_seed_count",
        "new_zeta_definition_count",
        "cross_q_coefficient_ring_identification_count",
        "adaptive_matrix_or_group_candidate_search_count",
        "stack_simulation_beyond_exact_finite_formulas_count",
        "external_data_load_count",
        "route_b_open_count",
        "common_modulus_clock_found",
        "ambient_ring_varies_with_q",
        "intrinsic_prime_selector",
        "external_modulus_specialization_required",
        "classification",
        "pass",
    }
)
ROW_KEYS = frozenset(
    {
        "q",
        "expected",
        "torsor",
        "enumeration_engine",
        "formula_engine",
        "engine_pair_validation",
        "checks",
        "pass",
    }
)
CLAIM_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "run_id",
        "state",
        "source_lock_sha256",
        "reviewed_code_sha256",
        "review_file_sha256",
        "pre_execution_audit_path",
        "pre_execution_audit_sha256",
        "registered_moduli",
        "structural_control_count",
        "structural_control_in_modulus_namespace",
        "result_path",
        "terminal_path",
        "registered_audit_count",
        "candidate_numerical_run_count",
    }
)
TERMINAL_KEYS = frozenset(
    {
        "schema",
        "candidate_id",
        "run_id",
        "state",
        "source_lock_sha256",
        "reviewed_code_sha256",
        "claim_sha256",
        "result_path",
        "result_sha256",
        "moduli_started",
        "moduli_completed",
        "structural_control_completed",
        "registered_audit_count",
        "candidate_numerical_run_count",
        "failure_code",
    }
)
ZERO_COUNTERS = (
    "candidate_rerun_count",
    "candidate_numerical_run_count",
    "network_access_count",
    "external_prime_data_access_count",
    "riemann_zero_data_access_count",
    "numeric_s_evaluation_count",
    "numeric_log_q_evaluation_count",
    "numeric_q_power_minus_s_evaluation_count",
    "random_seed_count",
    "new_zeta_definition_count",
    "cross_q_coefficient_ring_identification_count",
    "adaptive_matrix_or_group_candidate_search_count",
    "stack_simulation_beyond_exact_finite_formulas_count",
    "external_data_load_count",
    "route_b_open_count",
)


def validate_immutable_artifacts(project_root: Path) -> dict[str, Any]:
    root = Path(project_root).absolute()
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for relative, (expected_hash, expected_size) in sorted(IMMUTABLE_ARTIFACTS.items()):
        path = root / relative
        observed_hash = sha256_file(path) if regular_file(path) else None
        observed_size = path.stat().st_size if regular_file(path) else None
        passed = observed_hash == expected_hash and observed_size == expected_size
        records.append(
            {
                "path": relative,
                "expected_sha256": expected_hash,
                "observed_sha256": observed_hash,
                "expected_size": expected_size,
                "observed_size": observed_size,
                "pass": passed,
            }
        )
        if not passed:
            errors.append("IMMUTABLE_ARTIFACT_MISMATCH:" + relative)
    return {
        "stage": "R115_IMMUTABLE_ARTIFACTS",
        "records": records,
        "errors": errors,
        "pass": not errors,
    }


def validate_immutable_execution_tree(project_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    try:
        observed = execution_tree_sha256(project_root)
    except (OSError, RuntimeError, ValueError):
        observed = None
        errors.append("EXECUTION_TREE_UNSAFE_OR_UNHASHABLE")
    if observed != EXECUTION_TREE_SHA256:
        errors.append("EXECUTION_TREE_HASH_MISMATCH")
    return {
        "stage": "R116_IMMUTABLE_EXECUTION_TREE",
        "expected_sha256": EXECUTION_TREE_SHA256,
        "observed_sha256": observed,
        "errors": errors,
        "pass": not errors,
    }


def _twist_records(row: dict[str, Any], engine_name: str) -> Any:
    try:
        return row[engine_name]["g_permutation"]["unique_fixing_translation_by_iterate"]
    except (KeyError, TypeError):
        return None


def reproduce_legacy_k005(rows: Any) -> bool:
    """Reproduce the historical bug exactly; JSON lists never equal tuples."""

    if type(rows) is not list:
        return False
    try:
        return all(
            record["fixing_group_elements"] == (record["expected_a_inverse_power"],)
            for row in rows
            for record in _twist_records(row, "enumeration_engine")
        )
    except (KeyError, TypeError):
        return False


def validate_corrected_k005(rows: Any) -> dict[str, Any]:
    errors: list[str] = []
    record_count = 0
    if type(rows) is not list or len(rows) != len(LOCKED_MODULI):
        errors.append("K005_ROWS_NOT_EXACT")
    else:
        for row in rows:
            q = row.get("q") if type(row) is dict else None
            for engine_name in ("enumeration_engine", "formula_engine"):
                records = _twist_records(row, engine_name) if type(row) is dict else None
                if type(records) is not list or not records:
                    errors.append(f"K005_Q{q}_{engine_name.upper()}_RECORDS_INVALID")
                    continue
                for record in records:
                    record_count += 1
                    if type(record) is not dict:
                        errors.append(f"K005_Q{q}_RECORD_NOT_OBJECT")
                        continue
                    expected = record.get("expected_a_inverse_power")
                    fixing = record.get("fixing_group_elements")
                    expected_is_matrix = (
                        type(expected) is list
                        and len(expected) == 2
                        and all(
                            type(matrix_row) is list
                            and len(matrix_row) == 2
                            and all(type(value) is int for value in matrix_row)
                            for matrix_row in expected
                        )
                    )
                    if not expected_is_matrix:
                        errors.append(f"K005_Q{q}_EXPECTED_FIXER_NOT_2X2_INT_MATRIX")
                    if type(fixing) is not list:
                        errors.append(f"K005_Q{q}_FIXING_GROUP_NOT_JSON_LIST")
                    elif len(fixing) != 1 or fixing[0] != expected:
                        errors.append(f"K005_Q{q}_FIXING_GROUP_NOT_EXPECTED_SINGLETON")
    return {
        "stage": "R117_K005_JSON_BOUNDARY",
        "record_count": record_count,
        "legacy_list_tuple_comparison": reproduce_legacy_k005(rows),
        "correct_json_list_comparison": not errors,
        "errors": errors,
        "pass": not errors and reproduce_legacy_k005(rows) is False,
    }


def _recompute_controls(
    rows: list[dict[str, Any]], structural: dict[str, Any], audit: dict[str, Any]
) -> dict[str, bool]:
    by_q = {row["q"]: row for row in rows}
    return {
        "K001": [row["q"] for row in rows] == list(LOCKED_MODULI),
        "K002": all(
            row["torsor"]["pass"] is True and all(row["torsor"]["checks"].values())
            for row in rows
        ),
        "K003": all(
            row["engine_pair_validation"]["pass"] is True
            and {key: value for key, value in row["enumeration_engine"].items() if key != "engine"}
            == {key: value for key, value in row["formula_engine"].items() if key != "engine"}
            for row in rows
        ),
        "K004": all(
            row["enumeration_engine"]["point_burnside"]["exact_period_classes"][0]["support"]
            == row["torsor"]["r"]
            and row["enumeration_engine"]["orbit_burnside"]["exact_period_classes"][0]["support"]
            == 1
            for row in rows
        ),
        "K005": validate_corrected_k005(rows)["pass"] is True,
        "K006": all(
            row["enumeration_engine"]["orbifold"]["nonempty_sector_count"] == 1
            and row["enumeration_engine"]["orbifold"]["nonidentity_nonempty_sector_count"] == 0
            and row["enumeration_engine"]["action_groupoid"]["induced_period"] == 1
            for row in rows
        ),
        "K007": all(
            row["enumeration_engine"]["generator_ambiguity"]["same_point_fixed_signature"] is True
            and row["enumeration_engine"]["generator_ambiguity"]["labelled_twists_distinct"] is True
            for row in rows
        ),
        "K008": structural["pass"] is True and structural["is_arithmetic_modulus_row"] is False,
        "K009": (
            by_q[2]["torsor"]["r"] == by_q[4]["torsor"]["r"] == 3
            and by_q[6]["torsor"]["r"] == by_q[9]["torsor"]["r"] == 12
        ),
        "K010": all(
            by_q[q]["pass"] is True
            and by_q[q]["enumeration_engine"]["action_groupoid"]["induced_period"] == 1
            for q in (4, 6, 9, 10)
        ),
        "K011": not all(
            row["enumeration_engine"]["orbifold"]["point_cardinality_factors"][0]["exponent"]
            == {"numerator": 1, "denominator": 1}
            for row in rows
        )
        and all(
            row["enumeration_engine"]["orbifold"]["point_orbifold_factors"][0]["exponent"]
            != {"numerator": 1, "denominator": 1}
            for row in rows
        )
        and all(
            row["enumeration_engine"]["orbifold"]["orbit_cardinality_factors"][0]["support"]
            != row["torsor"]["r"]
            and row["enumeration_engine"]["orbifold"]["orbit_orbifold_factors"][0]["support"]
            != row["torsor"]["r"]
            for row in rows
        ),
        "K012": {
            "ambient_ring_varies_with_q": audit["ambient_ring_varies_with_q"],
            "intrinsic_prime_selector": audit["intrinsic_prime_selector"],
            "external_modulus_specialization_required": audit[
                "external_modulus_specialization_required"
            ],
            "common_modulus_clock_found": audit["common_modulus_clock_found"],
        }
        == {
            "ambient_ring_varies_with_q": True,
            "intrinsic_prime_selector": False,
            "external_modulus_specialization_required": True,
            "common_modulus_clock_found": False,
        },
    }


def validate_result_payload(payload: Any, preflight: Any, claim: Any) -> dict[str, Any]:
    errors: list[str] = []
    if type(payload) is not dict or set(payload) != OUTER_KEYS:
        return {"stage": "R119_STORED_RESULT_SEMANTICS", "errors": ["OUTER_KEYS_NOT_EXACT"], "pass": False}
    exact_outer = {
        "schema": "EQUIVARIANT_CLOCK_OFFICIAL_RESULT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": EXECUTION_TREE_SHA256,
        "registered_claim_sha256": IMMUTABLE_ARTIFACTS[
            "results/registered_run.claim.json"
        ][0],
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
        "pass": True,
    }
    for key, expected in exact_outer.items():
        if payload.get(key) != expected or type(payload.get(key)) is not type(expected):
            errors.append("OUTER_" + key.upper() + "_MISMATCH")
    if type(preflight) is not dict or type(claim) is not dict:
        errors.append("CHAIN_INPUT_NOT_OBJECT")
    else:
        if canonical_json_bytes(payload.get("pre_execution_gates")) != canonical_json_bytes(
            preflight.get("gates")
        ):
            errors.append("RESULT_PREFLIGHT_GATES_LINK_MISMATCH")
        if canonical_json_bytes(payload.get("independent_review_gate")) != canonical_json_bytes(
            preflight.get("independent_review")
        ):
            errors.append("RESULT_DEPLOYMENT_REVIEW_LINK_MISMATCH")
    audit = payload.get("audit")
    if type(audit) is not dict or set(audit) != AUDIT_KEYS:
        errors.append("AUDIT_KEYS_NOT_EXACT")
        return {"stage": "R119_STORED_RESULT_SEMANTICS", "errors": errors, "pass": False}
    exact_audit = {
        "schema": "EQUIVARIANT_CLOCK_REGISTERED_EXACT_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "fixed_matrix": [[2, 1], [1, 1]],
        "arithmetic_modulus_order": list(LOCKED_MODULI),
        "registered_audit_count": 1,
        "arithmetic_modulus_record_count": 9,
        "structural_unit_control_count": 1,
        "structural_control_in_modulus_namespace": False,
        "common_modulus_clock_found": False,
        "ambient_ring_varies_with_q": True,
        "intrinsic_prime_selector": False,
        "external_modulus_specialization_required": True,
        "classification": TERMINAL_CLASSIFICATION,
        "pass": True,
    }
    for key, expected in exact_audit.items():
        if audit.get(key) != expected or type(audit.get(key)) is not type(expected):
            errors.append("AUDIT_" + key.upper() + "_MISMATCH")
    for key in ZERO_COUNTERS:
        if audit.get(key) != 0 or type(audit.get(key)) is not int:
            errors.append("AUDIT_ZERO_COUNTER_MISMATCH:" + key)
    rows = audit.get("arithmetic_modulus_records")
    if type(rows) is not list or len(rows) != len(LOCKED_MODULI):
        errors.append("ROWS_NOT_EXACT")
    else:
        for row, q in zip(rows, LOCKED_MODULI, strict=True):
            if type(row) is not dict or set(row) != ROW_KEYS:
                errors.append(f"Q{q}_ROW_KEYS_NOT_EXACT")
                continue
            n, r, m = EXPECTED_LEDGER[q]
            if row.get("q") != q or row.get("expected") != {"n": n, "r": r, "m": m}:
                errors.append(f"Q{q}_LEDGER_MISMATCH")
            if row.get("pass") is not True:
                errors.append(f"Q{q}_PASS_NOT_TRUE")
            if row.get("engine_pair_validation", {}).get("pass") is not True:
                errors.append(f"Q{q}_ENGINE_PAIR_NOT_PASSING")
            enumeration = row.get("enumeration_engine")
            formula = row.get("formula_engine")
            if type(enumeration) is not dict or type(formula) is not dict:
                errors.append(f"Q{q}_ENGINE_NOT_OBJECT")
            elif (
                {key: value for key, value in enumeration.items() if key != "engine"}
                != {key: value for key, value in formula.items() if key != "engine"}
            ):
                errors.append(f"Q{q}_ENGINE_CROSSWIRE_MISMATCH")
        k005 = validate_corrected_k005(rows)
        if k005["pass"] is not True:
            errors.extend(k005["errors"])
    structural = audit.get("structural_unit_control")
    if (
        type(structural) is not dict
        or structural.get("pass") is not True
        or structural.get("is_arithmetic_modulus_row") is not False
        or "q" in structural
    ):
        errors.append("STRUCTURAL_CONTROL_NAMESPACE_INVALID")
    controls = audit.get("controls")
    if type(controls) is not dict or set(controls) != CONTROL_KEYS:
        errors.append("CONTROL_KEYS_NOT_EXACT")
    elif type(rows) is list and type(structural) is dict:
        try:
            recomputed = _recompute_controls(rows, structural, audit)
        except (KeyError, TypeError, IndexError):
            recomputed = {}
            errors.append("CONTROLS_RECOMPUTATION_FAILED")
        if recomputed != controls or any(value is not True for value in recomputed.values()):
            errors.append("CONTROLS_NOT_EXACT_RECOMPUTED_TRUE")
    proof = audit.get("proof_only_contract")
    expected_proof_validation = {"expected": proof, "errors": [], "pass": True}
    if type(proof) is not dict or audit.get("proof_contract_validation") != expected_proof_validation:
        errors.append("PROOF_CONTRACT_VALIDATION_MISMATCH")
    return {
        "stage": "R119_STORED_RESULT_SEMANTICS",
        "corrected_k005": validate_corrected_k005(rows),
        "errors": errors,
        "pass": not errors,
    }


def validate_execution_chain(project_root: Path) -> dict[str, Any]:
    root = Path(project_root).absolute()
    errors: list[str] = []
    try:
        preflight = load_exact_json(root / "results/PRE_EXECUTION_AUDIT.json")
        claim = load_exact_json(root / "results/registered_run.claim.json")
        result = load_exact_json(root / "results/EXPERIMENT_RESULTS.json")
        terminal = load_exact_json(root / "results/registered_run.json")
    except (OSError, RuntimeError, ValueError, TypeError):
        return {
            "stage": "R119_IMMUTABLE_EXECUTION_CHAIN",
            "errors": ["EXECUTION_CHAIN_STRICT_LOAD_FAILED"],
            "pass": False,
        }
    if type(claim) is not dict or set(claim) != CLAIM_KEYS:
        errors.append("CLAIM_KEYS_NOT_EXACT")
    else:
        claim_expected = {
            "schema": "EQUIVARIANT_CLOCK_REGISTERED_RUN_CLAIM_V1",
            "candidate_id": CANDIDATE_ID,
            "run_id": "REGISTERED_RUN_0001",
            "state": "STARTED",
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "reviewed_code_sha256": EXECUTION_TREE_SHA256,
            "review_file_sha256": IMMUTABLE_ARTIFACTS["results/CODE_REVIEW.md"][0],
            "pre_execution_audit_path": "results/PRE_EXECUTION_AUDIT.json",
            "pre_execution_audit_sha256": IMMUTABLE_ARTIFACTS[
                "results/PRE_EXECUTION_AUDIT.json"
            ][0],
            "registered_moduli": list(LOCKED_MODULI),
            "structural_control_count": 1,
            "structural_control_in_modulus_namespace": False,
            "result_path": "results/EXPERIMENT_RESULTS.json",
            "terminal_path": "results/registered_run.json",
            "registered_audit_count": 1,
            "candidate_numerical_run_count": 0,
        }
        for key, expected in claim_expected.items():
            if claim.get(key) != expected or type(claim.get(key)) is not type(expected):
                errors.append("CLAIM_" + key.upper() + "_MISMATCH")
    if type(terminal) is not dict or set(terminal) != TERMINAL_KEYS:
        errors.append("TERMINAL_KEYS_NOT_EXACT")
    else:
        terminal_expected = {
            "schema": "EQUIVARIANT_CLOCK_REGISTERED_RUN_TERMINAL_V1",
            "candidate_id": CANDIDATE_ID,
            "run_id": "REGISTERED_RUN_0001",
            "state": "COMPLETED_CERTIFIED",
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "reviewed_code_sha256": EXECUTION_TREE_SHA256,
            "claim_sha256": IMMUTABLE_ARTIFACTS["results/registered_run.claim.json"][0],
            "result_path": "results/EXPERIMENT_RESULTS.json",
            "result_sha256": IMMUTABLE_ARTIFACTS["results/EXPERIMENT_RESULTS.json"][0],
            "moduli_started": list(LOCKED_MODULI),
            "moduli_completed": list(LOCKED_MODULI),
            "structural_control_completed": True,
            "registered_audit_count": 1,
            "candidate_numerical_run_count": 0,
            "failure_code": None,
        }
        for key, expected in terminal_expected.items():
            if terminal.get(key) != expected or type(terminal.get(key)) is not type(expected):
                errors.append("TERMINAL_" + key.upper() + "_MISMATCH")
    if type(preflight) is not dict:
        errors.append("PREFLIGHT_NOT_OBJECT")
    else:
        preflight_expected = {
            "schema": "EQUIVARIANT_CLOCK_PRE_EXECUTION_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "reviewed_code_sha256": EXECUTION_TREE_SHA256,
            "registered_audit_count": 0,
            "registered_moduli_executed": [],
            "candidate_numerical_run_count": 0,
            "network_access_count": 0,
            "external_data_load_count": 0,
            "numeric_s_or_log_evaluation_count": 0,
            "arithmetic_modulus_order": list(LOCKED_MODULI),
            "structural_unit_control_count": 1,
            "structural_control_in_modulus_namespace": False,
            "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
            "pass": True,
        }
        for key, expected in preflight_expected.items():
            if preflight.get(key) != expected or type(preflight.get(key)) is not type(expected):
                errors.append("PREFLIGHT_" + key.upper() + "_MISMATCH")
    # Test-only project-root injection is kept outside the immutable payload.
    semantic_claim = dict(claim) if type(claim) is dict else {}
    result_semantics = validate_result_payload(result, preflight, semantic_claim)
    if result_semantics.get("pass") is not True:
        errors.extend(result_semantics.get("errors", []))
    return {
        "stage": "R119_IMMUTABLE_EXECUTION_CHAIN",
        "result_semantics": result_semantics,
        "errors": errors,
        "pass": not errors,
    }


def first_attempt_reproduction(project_root: Path) -> dict[str, Any]:
    root = Path(project_root).absolute()
    try:
        payload = load_exact_json(root / "results/EXPERIMENT_RESULTS.json")
        rows = payload["audit"]["arithmetic_modulus_records"]
    except (OSError, RuntimeError, ValueError, KeyError, TypeError):
        rows = None
    legacy = reproduce_legacy_k005(rows)
    corrected = validate_corrected_k005(rows)
    errors: list[str] = []
    if legacy is not False:
        errors.append("LEGACY_K005_FAILURE_NOT_REPRODUCED")
    if corrected.get("pass") is not True:
        errors.append("CORRECTED_K005_NOT_PASSING")
    return {
        "stage": "R114_FIRST_MANIFEST_ATTEMPT_REPRODUCTION",
        "historical_attempt": FIRST_MANIFEST_ATTEMPT,
        "legacy_k005_value": legacy,
        "corrected_k005": corrected,
        "errors": errors,
        "pass": not errors,
    }


def collect_analyzer_audit(project_root: Path) -> dict[str, Any]:
    root = Path(project_root).absolute()
    try:
        analyzer_sha = analyzer_tree_sha256(root)
    except (OSError, RuntimeError, ValueError):
        analyzer_sha = None
    base_gates = {
        "first_attempt_reproduction": first_attempt_reproduction(root),
        "immutable_artifacts": validate_immutable_artifacts(root),
        "immutable_execution_tree": validate_immutable_execution_tree(root),
        "immutable_authorities": validate_execution_authorities(root),
        "immutable_execution_chain": validate_execution_chain(root),
        "analyzer_executable_isolation": analyzer_executable_isolation(root),
        "analyzer_junit": parse_analyzer_junit(root / ANALYZER_JUNIT_PATH),
    }
    base_pass = (
        analyzer_sha is not None
        and analyzer_sha != EXECUTION_TREE_SHA256
        and all(gate.get("pass") is True for gate in base_gates.values())
    )
    analyzer_review = validate_analyzer_authority(root)
    status = (
        "AUTHORIZED_FOR_POSTRUN_MANIFEST_V2"
        if base_pass and analyzer_review.get("pass") is True
        else "READY_FOR_INDEPENDENT_POSTRUN_ANALYZER_REVIEW"
        if base_pass
        else "POSTRUN_ANALYZER_AUDIT_FAILED"
    )
    return {
        "schema": "EQUIVARIANT_CLOCK_POSTRUN_ANALYZER_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "execution_tree_sha256": EXECUTION_TREE_SHA256,
        "analyzer_tree_sha256": analyzer_sha,
        "dual_tree_contract": {
            "execution_tree_role": "IMMUTABLE_REGISTERED_CANDIDATE_EXECUTION",
            "analyzer_tree_role": "POSTRUN_VALIDATOR_ONLY_NO_CANDIDATE_AUTHORITY",
            "trees_are_distinct": analyzer_sha is not None and analyzer_sha != EXECUTION_TREE_SHA256,
            "candidate_rerun_forbidden": True,
            "registered_audit_count": 1,
            "candidate_numerical_run_count": 0,
            "raw_execution_artifacts_mutable": False,
        },
        "base_gates": base_gates,
        "independent_analyzer_review": analyzer_review,
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
        "candidate_rerun_performed": False,
        "status": status,
        "pass": base_pass,
    }
