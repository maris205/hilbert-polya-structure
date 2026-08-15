"""Exact result semantics and strict post-run manifest closure."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CLAIM_PATH,
    CODE_REVIEW_PATH,
    LOCKED_MODULI,
    LOCKED_COMPOSITES,
    OFFICIAL_REPORT_PATHS,
    PERIOD_COLLISIONS,
    POSTRUN_TEST_PATH,
    PREEXECUTION_AUDIT_PATH,
    PREEXECUTION_TEST_PATH,
    RESULT_MANIFEST_PATH,
    RESULT_PATH,
    RESULT_REVIEW_PATH,
    SOURCE_LOCK_SHA256,
    TERMINAL_CLASSIFICATION,
    TERMINAL_PATH,
)
from .gates import collect_safe_preflight, parse_junit, validate_source_and_design, validate_upstream
from .lifecycle import validate_claim
from .protocol import (
    canonical_json_bytes,
    code_tree_sha256,
    lexical_absolute,
    load_exact_json,
    pretty_json_bytes,
    regular_file,
    sha256_file,
    stable_file_bytes,
    strict_json_loads,
    write_json,
)
from .review import validate_deployment_authority, validate_result_authority


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
CONTROL_KEYS = frozenset(
    {"K001", "K002", "K003", "K004", "K005", "K006", "K007", "K008", "K009", "K010", "K011", "K012"}
)
REQUIRED_NAMESPACES = frozenset(
    {
        "source_dynamics",
        "point_burnside",
        "orbit_burnside",
        "g_permutation",
        "enhanced",
        "orbifold",
        "action_groupoid",
        "generator_ambiguity",
        "shortening_gluing",
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


def _exact_same(value: Any, expected: Any) -> bool:
    if type(value) is not type(expected):
        return False
    if type(expected) is dict:
        return set(value) == set(expected) and all(
            _exact_same(value[key], expected[key]) for key in expected
        )
    if type(expected) is list:
        return len(value) == len(expected) and all(
            _exact_same(left, right) for left, right in zip(value, expected, strict=True)
        )
    return value == expected


def _validate_row(row: Any, q: int, errors: list[str]) -> None:
    from .invariants import audit_modulus

    label = "Q" + str(q) + "_"
    if type(row) is not dict or set(row) != ROW_KEYS:
        errors.append(label + "ROW_KEYS_NOT_EXACT")
        return
    if row.get("q") != q or type(row.get("q")) is not int:
        errors.append(label + "Q_MISMATCH")
    fresh = audit_modulus(q)
    if canonical_json_bytes(row) != canonical_json_bytes(fresh):
        errors.append(label + "ROW_NOT_FRESH_ENGINE_EXACT")
    if row.get("pass") is not True:
        errors.append(label + "ROW_PASS_NOT_TRUE")
    checks = row.get("checks")
    if type(checks) is not dict or not checks or any(value is not True for value in checks.values()):
        errors.append(label + "CHECKS_NOT_ALL_TRUE")
    for engine_key, expected_engine in (
        ("enumeration_engine", "EXPLICIT_FIXED_SET_AND_GROUPOID_ENUMERATION"),
        ("formula_engine", "REGULAR_TORSOR_THEOREM_FORMULAS"),
    ):
        engine = row.get(engine_key)
        if type(engine) is not dict or engine.get("engine") != expected_engine:
            errors.append(label + engine_key.upper() + "_INVALID")
            continue
        if set(engine).difference({"engine"}) != REQUIRED_NAMESPACES:
            errors.append(label + engine_key.upper() + "_NAMESPACES_NOT_EXACT")
    torsor = row.get("torsor")
    if type(torsor) is not dict or torsor.get("pass") is not True:
        errors.append(label + "TORSOR_NOT_PASSING")
    elif (
        len(torsor.get("direct_group", [])) != row.get("expected", {}).get("n")
        or len(torsor.get("direct_cyclic_locus", [])) != row.get("expected", {}).get("n")
        or torsor.get("r") != row.get("expected", {}).get("r")
        or torsor.get("m") != row.get("expected", {}).get("m")
    ):
        errors.append(label + "TORSOR_EMBEDDED_COUNT_MISMATCH")


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
        "K005": all(
            all(
                record["fixing_group_elements"] == (record["expected_a_inverse_power"],)
                for record in row["enumeration_engine"]["g_permutation"]["unique_fixing_translation_by_iterate"]
            )
            for row in rows
        ),
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
        "K008": structural["pass"] is True
        and structural["is_arithmetic_modulus_row"] is False,
        "K009": all(
            by_q[left]["torsor"]["r"] == shared
            and by_q[right]["torsor"]["r"] == shared
            for (left, right), shared in PERIOD_COLLISIONS
        ),
        "K010": all(
            by_q[q]["pass"]
            and by_q[q]["enumeration_engine"]["action_groupoid"]["induced_period"] == 1
            for q in LOCKED_COMPOSITES
        ),
        "K011": not all(
            row["enumeration_engine"]["orbifold"]["point_cardinality_factors"][0]["exponent"]
            == {"numerator": 1, "denominator": 1}
            for row in rows
        ) and all(
            row["enumeration_engine"]["orbifold"]["point_orbifold_factors"][0]["exponent"]
            != {"numerator": 1, "denominator": 1}
            for row in rows
        ) and all(
            row["enumeration_engine"]["orbifold"]["orbit_cardinality_factors"][0]["support"]
            != row["torsor"]["r"]
            and row["enumeration_engine"]["orbifold"]["orbit_orbifold_factors"][0]["support"]
            != row["torsor"]["r"]
            for row in rows
        ),
        "K012": {
            "ambient_ring_varies_with_q": audit["ambient_ring_varies_with_q"],
            "intrinsic_prime_selector": audit["intrinsic_prime_selector"],
            "external_modulus_specialization_required": audit["external_modulus_specialization_required"],
            "common_modulus_clock_found": audit["common_modulus_clock_found"],
        }
        == {
            "ambient_ring_varies_with_q": True,
            "intrinsic_prime_selector": False,
            "external_modulus_specialization_required": True,
            "common_modulus_clock_found": False,
        },
    }


def _validate_audit(audit: Any, errors: list[str]) -> None:
    from .candidate import proof_only_contract
    from .cyclic_cset import structural_unit_control

    if type(audit) is not dict or set(audit) != AUDIT_KEYS:
        errors.append("AUDIT_KEYS_NOT_EXACT")
        return
    scalar_expected = {
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
    for key, value in scalar_expected.items():
        if audit.get(key) != value or type(audit.get(key)) is not type(value):
            errors.append("AUDIT_" + key.upper() + "_MISMATCH")
    for key in ZERO_COUNTERS:
        if audit.get(key) != 0 or type(audit.get(key)) is not int:
            errors.append("AUDIT_ZERO_COUNTER_MISMATCH:" + key)
    rows = audit.get("arithmetic_modulus_records")
    rows_valid = type(rows) is list and len(rows) == len(LOCKED_MODULI)
    if not rows_valid:
        errors.append("ROWS_NOT_EXACT_LIST")
    else:
        observed_order = [row.get("q") if type(row) is dict else None for row in rows]
        if observed_order != list(LOCKED_MODULI):
            errors.append("ROW_ORDER_MISMATCH")
        for row, q in zip(rows, LOCKED_MODULI, strict=True):
            _validate_row(row, q, errors)
    structural = audit.get("structural_unit_control")
    fresh_structural = structural_unit_control()
    structural_valid = canonical_json_bytes(structural) == canonical_json_bytes(fresh_structural)
    if not structural_valid:
        errors.append("STRUCTURAL_CONTROL_NOT_FRESH_EXACT")
    elif type(structural) is not dict or structural.get("is_arithmetic_modulus_row") is not False or "q" in structural:
        errors.append("STRUCTURAL_CONTROL_NAMESPACE_VIOLATION")
    controls = audit.get("controls")
    if type(controls) is not dict or set(controls) != CONTROL_KEYS:
        errors.append("CONTROL_KEYS_NOT_EXACT")
    elif not rows_valid or not structural_valid:
        errors.append("CONTROLS_CANNOT_BE_RECOMPUTED")
    else:
        recomputed = _recompute_controls(rows, structural, audit)
        if not _exact_same(controls, recomputed) or any(value is not True for value in controls.values()):
            errors.append("CONTROLS_NOT_EXACT_RECOMPUTED_TRUE")
    proof = audit.get("proof_only_contract")
    expected_proof = proof_only_contract()
    if not _exact_same(proof, expected_proof):
        errors.append("PROOF_CONTRACT_MISMATCH")
    expected_validation = {"expected": expected_proof, "errors": [], "pass": True}
    if not _exact_same(audit.get("proof_contract_validation"), expected_validation):
        errors.append("PROOF_CONTRACT_NOT_PASSING")


def validate_registered_result(payload: Any, project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    errors: list[str] = []
    if type(payload) is not dict or set(payload) != OUTER_KEYS:
        return {"stage": "R100_RESULT_SEMANTICS", "errors": ["OUTER_KEYS_NOT_EXACT"], "pass": False}
    code_sha = code_tree_sha256(root)
    claim = validate_claim(root, code_sha)
    expected_outer = {
        "schema": "EQUIVARIANT_CLOCK_OFFICIAL_RESULT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_sha,
        "registered_claim_sha256": claim.get("claim_sha256"),
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
        "pass": True,
    }
    for key, value in expected_outer.items():
        if payload.get(key) != value or type(payload.get(key)) is not type(value):
            errors.append("OUTER_" + key.upper() + "_MISMATCH")
    _validate_audit(payload.get("audit"), errors)
    live = collect_safe_preflight(root)
    official = load_exact_json(root / PREEXECUTION_AUDIT_PATH) if regular_file(root / PREEXECUTION_AUDIT_PATH) else None
    if live.get("pass") is not True or live.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        errors.append("LIVE_PREFLIGHT_NOT_AUTHORIZED")
    if canonical_json_bytes(official) != canonical_json_bytes(live):
        errors.append("PREFLIGHT_NOT_LIVE_EXACT")
    if canonical_json_bytes(payload.get("pre_execution_gates")) != canonical_json_bytes(live.get("gates")):
        errors.append("EMBEDDED_GATES_NOT_EXACT")
    if canonical_json_bytes(payload.get("independent_review_gate")) != canonical_json_bytes(live.get("independent_review")):
        errors.append("EMBEDDED_REVIEW_NOT_EXACT")
    return {"stage": "R100_RESULT_SEMANTICS", "errors": errors, "pass": not errors}


def _result_inventory(
    project_root: Path, expected: frozenset[str], *, ignore_manifest: bool = False
) -> dict[str, Any]:
    root = lexical_absolute(project_root) / "results"
    manifest_name = Path(RESULT_MANIFEST_PATH).name
    first = sorted(
        entry.name for entry in root.iterdir() if not (ignore_manifest and entry.name == manifest_name)
    )
    second = sorted(
        entry.name for entry in root.iterdir() if not (ignore_manifest and entry.name == manifest_name)
    )
    errors: list[str] = []
    if first != second:
        errors.append("RESULT_INVENTORY_UNSTABLE")
    if set(first) != set(expected) or len(first) != len(expected):
        errors.append("RESULT_INVENTORY_NOT_EXACT")
    for name in expected:
        if not regular_file(root / name):
            errors.append("RESULT_FILE_MISSING_OR_UNSAFE:" + name)
    return {"observed": first, "expected": sorted(expected), "errors": errors, "pass": not errors}


def collect_postrun_audit(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    code_sha = code_tree_sha256(root)
    inventory = _result_inventory(root, PREMANIFEST_RESULT_FILES, ignore_manifest=True)
    claim = validate_claim(root, code_sha)
    payload = load_exact_json(root / RESULT_PATH) if regular_file(root / RESULT_PATH) else None
    semantics = validate_registered_result(payload, root)
    terminal = load_exact_json(root / TERMINAL_PATH) if regular_file(root / TERMINAL_PATH) else None
    terminal_errors: list[str] = []
    if type(terminal) is not dict:
        terminal_errors.append("TERMINAL_MISSING")
    else:
        if terminal.get("state") != "COMPLETED_CERTIFIED":
            terminal_errors.append("TERMINAL_NOT_CERTIFIED")
        if terminal.get("reviewed_code_sha256") != code_sha:
            terminal_errors.append("TERMINAL_CODE_MISMATCH")
        if terminal.get("claim_sha256") != claim.get("claim_sha256"):
            terminal_errors.append("TERMINAL_CLAIM_MISMATCH")
        if terminal.get("result_sha256") != sha256_file(root / RESULT_PATH):
            terminal_errors.append("TERMINAL_RESULT_MISMATCH")
        if terminal.get("moduli_started") != list(LOCKED_MODULI) or terminal.get("moduli_completed") != list(LOCKED_MODULI):
            terminal_errors.append("TERMINAL_MODULI_MISMATCH")
        if terminal.get("structural_control_completed") is not True:
            terminal_errors.append("TERMINAL_STRUCTURAL_CONTROL_MISSING")
    post_tests = parse_junit(root / POSTRUN_TEST_PATH)
    post_tests["stage"] = "R111_POSTRUN_TEST_EVIDENCE"
    reports = [
        {
            "path": relative,
            "sha256": sha256_file(root / relative) if regular_file(root / relative) else None,
            "pass": regular_file(root / relative),
        }
        for relative in OFFICIAL_REPORT_PATHS
    ]
    gates = {
        "inventory": inventory,
        "source": validate_source_and_design(root),
        "upstream": validate_upstream(root),
        "deployment_review": validate_deployment_authority(root),
        "claim": claim,
        "result_semantics": semantics,
        "terminal": {"errors": terminal_errors, "pass": not terminal_errors},
        "postrun_tests": post_tests,
        "official_reports": {"records": reports, "pass": all(record["pass"] for record in reports)},
        "independent_result_review": validate_result_authority(root, code_sha),
    }
    return {
        "schema": "EQUIVARIANT_CLOCK_POSTRUN_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "execution_code_sha256": code_sha,
        "gates": gates,
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
        "candidate_rerun_performed": False,
        "pass": all(record.get("pass") is True for record in gates.values()),
    }


def _manifest_payload(project_root: Path, expected_inventory: frozenset[str]) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    audit = collect_postrun_audit(root)
    errors = [] if audit["pass"] is True else ["POSTRUN_AUDIT_NOT_PASSING"]
    inventory = _result_inventory(
        root,
        expected_inventory,
        ignore_manifest=expected_inventory == PREMANIFEST_RESULT_FILES,
    )
    errors.extend(inventory["errors"])
    paths = sorted({"results/" + name for name in PREMANIFEST_RESULT_FILES}.union(OFFICIAL_REPORT_PATHS))
    files = []
    for relative in paths:
        if not regular_file(root / relative):
            errors.append("MANIFEST_INPUT_MISSING:" + relative)
        else:
            files.append({"path": relative, "sha256": sha256_file(root / relative)})
    return {
        "schema": "EQUIVARIANT_CLOCK_RESULT_MANIFEST_V1",
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
        "registered_audit_count": 1,
        "candidate_numerical_run_count": 0,
        "candidate_rerun_performed": False,
        "errors": errors,
        "pass": not errors,
    }


def write_result_manifest(project_root: Path) -> Path:
    root = lexical_absolute(project_root)
    output = root / RESULT_MANIFEST_PATH
    if output.exists():
        raise FileExistsError("result manifest is one-shot")
    payload = _manifest_payload(root, PREMANIFEST_RESULT_FILES)
    if payload["pass"] is not True:
        raise RuntimeError("strict postrun manifest gates failed")
    write_json(output, payload, exclusive=True)
    if validate_existing_manifest(root)["pass"] is not True:
        raise RuntimeError("written manifest failed live closure")
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
        errors.append("MANIFEST_MISSING")
    else:
        try:
            raw = stable_file_bytes(path)
            stored = strict_json_loads(raw.decode("utf-8"))
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError):
            errors.append("MANIFEST_INVALID")
    if type(stored) is not dict:
        errors.append("MANIFEST_NOT_OBJECT")
    else:
        if raw != pretty_json_bytes(stored):
            errors.append("MANIFEST_BYTES_NOT_CANONICAL")
        recomputed = _manifest_payload(root, FINAL_RESULT_FILES)
        if recomputed["pass"] is not True:
            errors.append("LIVE_MANIFEST_CLOSURE_FAILED")
        elif canonical_json_bytes(stored) != canonical_json_bytes(recomputed):
            errors.append("MANIFEST_STALE_OR_TAMPERED")
    return {
        "stage": "R119_FINAL_MANIFEST_CLOSURE",
        "manifest_sha256": hashlib.sha256(raw).hexdigest() if raw is not None else None,
        "errors": errors,
        "pass": not errors,
    }
