"""Exact result semantics and strict post-run manifest closure."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    CLAIM_PATH,
    CODE_REVIEW_PATH,
    EXPECTED_LEDGER,
    LEDGER_FIELDS,
    LOCKED_MODULI,
    OFFICIAL_REPORT_PATHS,
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
from .finite_module import audit_modulus
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
        "schema", "candidate_id", "source_lock_sha256", "reviewed_code_sha256",
        "registered_claim_sha256", "pre_execution_gates", "independent_review_gate",
        "audit", "registered_exact_audits", "candidate_numerical_runs", "pass",
    }
)
AUDIT_KEYS = frozenset(
    {
        "schema", "candidate_id", "source_lock_sha256", "fixed_matrix", "locked_moduli",
        "rows", "controls", "proof_only_contract", "proof_contract_validation",
        "quotient_clock_status", "formal_factor_status", "external_modulus_label_required",
        "intrinsic_prime_selector", "local_pseudo_symmetry_scope", "registered_exact_audits",
        "candidate_reruns", "candidate_numerical_runs", "network_accesses",
        "external_data_loads", "external_prime_tables_accessed",
        "generated_prime_or_modulus_targets", "riemann_zero_data_accessed",
        "numeric_s_evaluations", "numeric_log_evaluations", "numeric_q_to_minus_s_evaluations",
        "random_draws", "matrix_or_parameter_searches",
        "equivariant_stacky_or_twisted_constructions",
        "hecke_transfer_fredholm_or_quantum_constructions", "all_q_inference_from_finite_audit",
        "novelty_inference_from_finite_audit", "route_b_opened", "classification", "pass",
    }
)
ROW_KEYS = frozenset(
    {"q", "expected", "ledger", "frozen_expected_match", "dual_checks", "direct_engine", "algebra_engine", "pass"}
)
LEDGER_KEYS = frozenset(LEDGER_FIELDS) | {
    "retained_fraction", "discarded_fraction", "norm_image_size",
}
DUAL_CHECK_KEYS = frozenset(
    {
        "commutant_equals_algebra_ring", "full_centralizer_equals_algebra_units",
        "symplectic_equals_norm_one", "cyclic_locus_equals_torsor_image",
        "matrix_det_equals_norm", "norm_images_match",
        "delta_fibers_equal_symplectic_orbits", "every_cyclic_vector_has_exact_order_q",
        "torsor_closure", "torsor_free", "torsor_transitive",
        "torsor_base_map_bijective", "full_quotient_action_identity",
        "symplectic_quotient_action_identity", "reversing_group_exact_and_no_mixing",
    }
)
CONTROL_KEYS = frozenset(
    {
        "K001_ordered_moduli_complete", "K002_dual_engines_pass",
        "K003_frozen_ledgers_match", "K004_torsors_exact", "K005_full_quotients_one",
        "K006_symplectic_norm_classes", "K007_quotient_actions_identity",
        "K008_prime_reversing_boundary", "K009_composites_prove_too_much",
        "K010_clock_and_prime_selector_absent",
    }
)
DIRECT_ENGINE_KEYS = frozenset(
    {
        "engine", "q", "commutant", "full_centralizer", "symplectic_centralizer",
        "exact_order_shell", "cyclic_locus", "discarded_shell", "cyclic_additive_orders",
        "A_order", "cyclic_A_orbits", "full_CV_orbits", "symplectic_CV_orbits",
        "full_shell_orbits", "symplectic_shell_orbits", "full_quotient_transition",
        "symplectic_quotient_transition", "delta_fibers", "norm_image_from_determinants",
        "reversing",
    }
)
ALGEBRA_ENGINE_KEYS = frozenset(
    {
        "engine", "q", "algebra_entries", "norm_table", "ring_matrices", "unit_matrices",
        "norm_one_matrices", "torsor_image", "torsor_axioms", "matrix_det_equals_norm",
        "norm_image", "norm_fiber_orbits", "delta_fibers_equal_norm_one_orbits",
    }
)
TRANSITION_KEYS = frozenset({"class_count", "transition", "identity"})
RATIONAL_KEYS = frozenset({"numerator", "denominator", "text"})
NORM_RECORD_KEYS = frozenset({"a", "b", "matrix", "matrix_determinant", "algebra_norm"})
DELTA_FIBER_KEYS = frozenset({"delta", "points"})
TORSOR_KEYS = frozenset({"closure", "free", "transitive", "base_map_bijective"})
REVERSING_KEYS = frozenset(
    {
        "constructed_group", "brute_reversing_group", "constructed_equals_brute",
        "group_closed", "reversor_relation", "shell_orbits", "shell_orbit_count",
        "cyclic_noncyclic_mixing",
    }
)
ZERO_COUNTERS = (
    "candidate_reruns", "candidate_numerical_runs", "network_accesses", "external_data_loads",
    "generated_prime_or_modulus_targets", "numeric_s_evaluations", "numeric_log_evaluations",
    "numeric_q_to_minus_s_evaluations", "random_draws", "matrix_or_parameter_searches",
    "equivariant_stacky_or_twisted_constructions",
    "hecke_transfer_fredholm_or_quantum_constructions",
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


def _expected(q: int) -> dict[str, Any]:
    return dict(zip(LEDGER_FIELDS, EXPECTED_LEDGER[q], strict=True))


def _sequence(value: Any) -> bool:
    return type(value) in {list, tuple}


def _residue(value: Any, q: int) -> bool:
    return type(value) is int and 0 <= value < q


def _vector(value: Any, q: int) -> bool:
    return _sequence(value) and len(value) == 2 and all(_residue(item, q) for item in value)


def _matrix(value: Any, q: int) -> bool:
    return _sequence(value) and len(value) == 2 and all(
        _sequence(row) and len(row) == 2 and all(_residue(item, q) for item in row)
        for row in value
    )


def _unique(value: Any) -> bool:
    return _sequence(value) and len(value) == len({canonical_json_bytes(item) for item in value})


def _validate_matrix_sequence(value: Any, q: int, label: str, errors: list[str]) -> None:
    if not _unique(value) or not all(_matrix(item, q) for item in value):
        errors.append(label + "MATRIX_SEQUENCE_INVALID")


def _validate_vector_sequence(value: Any, q: int, label: str, errors: list[str]) -> None:
    if not _unique(value) or not all(_vector(item, q) for item in value):
        errors.append(label + "VECTOR_SEQUENCE_INVALID")


def _validate_orbits(
    value: Any, q: int, expected_points: Any, label: str, errors: list[str]
) -> None:
    if not _sequence(value) or not _unique(value) or any(
        not _sequence(orbit) or not orbit or not _unique(orbit) or not all(_vector(point, q) for point in orbit)
        for orbit in value
    ):
        errors.append(label + "ORBIT_CONTAINER_INVALID")
        return
    flattened = [point for orbit in value for point in orbit]
    if len(flattened) != len({canonical_json_bytes(point) for point in flattened}):
        errors.append(label + "ORBIT_MULTIPLICITY_INVALID")
    if {canonical_json_bytes(point) for point in flattened} != {
        canonical_json_bytes(point) for point in expected_points
    }:
        errors.append(label + "ORBIT_PARTITION_INVALID")


def _proof_contract_expected() -> dict[str, Any]:
    return {
        "all_q_theorem_authority": "PROOF_PACKAGE_ONLY",
        "finite_audit_role": "FINITE_FALSIFICATION_AND_IMPLEMENTATION_CONTROL",
        "coarse_quotient_clock": "IDENTITY_NO_NATIVE_MODULUS_CLOCK",
        "formal_abstract_factor": "(1-z)^(-1)",
        "riemann_specialization": "EXTERNAL_MODULUS_SPECIALIZATION",
        "local_symmetry_scope": "Q_DEPENDENT_FULL_LOCAL_GL_CENTRALIZER",
        "intrinsic_prime_selector": False,
        "outside_scope": {
            "burnside_equivariant_zeta": "OUTSIDE_SCOPE_PAPER11",
            "orbifold_stacky_groupoid_zeta": "OUTSIDE_SCOPE_PAPER11",
            "twisted_sectors": "OUTSIDE_SCOPE_PAPER11",
            "group_action_zeta": "OUTSIDE_SCOPE_PAPER11",
            "hecke_quantization": "OUTSIDE_SCOPE_ROUTE_B_CLOSED",
            "transfer_fredholm": "OUTSIDE_SCOPE_ROUTE_B_CLOSED",
        },
        "route_b_open": False,
    }


def _validate_row(row: Any, q: int, errors: list[str]) -> None:
    label = "Q" + str(q) + "_"
    if type(row) is not dict or set(row) != ROW_KEYS:
        errors.append(label + "ROW_KEYS_NOT_EXACT")
        return
    if row.get("q") != q or type(row.get("q")) is not int:
        errors.append(label + "Q_MISMATCH")
    fresh = audit_modulus(q)
    if canonical_json_bytes(row) != canonical_json_bytes(fresh):
        errors.append(label + "ROW_NOT_FRESH_ENGINE_EXACT")
    expected = _expected(q)
    if not _exact_same(row.get("expected"), expected):
        errors.append(label + "EXPECTED_RECORD_MISMATCH")
    ledger = row.get("ledger")
    if type(ledger) is not dict or set(ledger) != LEDGER_KEYS:
        errors.append(label + "LEDGER_NOT_OBJECT")
        return
    if not _exact_same({key: ledger.get(key) for key in LEDGER_FIELDS}, expected):
        errors.append(label + "FROZEN_LEDGER_MISMATCH")
    if row.get("frozen_expected_match") is not True or row.get("pass") is not True:
        errors.append(label + "ROW_PASS_NOT_EXACT_TRUE")
    dual = row.get("dual_checks")
    if type(dual) is not dict or set(dual) != DUAL_CHECK_KEYS or any(value is not True for value in dual.values()):
        errors.append(label + "DUAL_CHECKS_NOT_ALL_TRUE")
    direct = row.get("direct_engine")
    algebra = row.get("algebra_engine")
    if type(direct) is not dict or set(direct) != DIRECT_ENGINE_KEYS:
        errors.append(label + "DIRECT_ENGINE_KEYS_NOT_EXACT")
        return
    if type(algebra) is not dict or set(algebra) != ALGEBRA_ENGINE_KEYS:
        errors.append(label + "ALGEBRA_ENGINE_KEYS_NOT_EXACT")
        return
    if type(direct) is not dict or type(algebra) is not dict:
        errors.append(label + "ENGINE_NOT_OBJECT")
        return
    if direct.get("q") != q or algebra.get("q") != q:
        errors.append(label + "ENGINE_Q_MISMATCH")
    exact_relations = {
        "commutant_ring": direct.get("commutant") == algebra.get("ring_matrices"),
        "full_units": direct.get("full_centralizer") == algebra.get("unit_matrices"),
        "symplectic_norm_one": direct.get("symplectic_centralizer") == algebra.get("norm_one_matrices"),
        "cyclic_torsor": direct.get("cyclic_locus") == algebra.get("torsor_image"),
        "norm_image": direct.get("norm_image_from_determinants") == algebra.get("norm_image"),
    }
    if not all(exact_relations.values()):
        errors.append(label + "EMBEDDED_DUAL_RELATION_MISMATCH")
    for key in ("commutant", "full_centralizer", "symplectic_centralizer"):
        _validate_matrix_sequence(direct[key], q, label + "DIRECT_" + key.upper() + "_", errors)
    for key in ("ring_matrices", "unit_matrices", "norm_one_matrices"):
        _validate_matrix_sequence(algebra[key], q, label + "ALGEBRA_" + key.upper() + "_", errors)
    for key in ("exact_order_shell", "cyclic_locus", "discarded_shell"):
        _validate_vector_sequence(direct[key], q, label + "DIRECT_" + key.upper() + "_", errors)
    _validate_vector_sequence(algebra["torsor_image"], q, label + "TORSOR_IMAGE_", errors)
    count_relations = {
        "shell": len(direct.get("exact_order_shell", [])) == expected["exact_shell_size"],
        "cyclic": len(direct.get("cyclic_locus", [])) == expected["cyclic_locus_size"],
        "discard": len(direct.get("discarded_shell", [])) == expected["discard_size"],
        "full": len(direct.get("full_centralizer", [])) == expected["full_centralizer_size"],
        "symplectic": len(direct.get("symplectic_centralizer", [])) == expected["symplectic_centralizer_size"],
        "a_orbits": len(direct.get("cyclic_A_orbits", [])) == expected["cyclic_A_orbit_count"],
        "full_cv_orbits": len(direct.get("full_CV_orbits", [])) == expected["full_CV_quotient_count"],
        "symplectic_cv_orbits": len(direct.get("symplectic_CV_orbits", [])) == expected["symplectic_CV_quotient_count"],
        "full_shell_orbits": len(direct.get("full_shell_orbits", [])) == expected["full_centralizer_shell_orbits"],
        "symplectic_shell_orbits": len(direct.get("symplectic_shell_orbits", [])) == expected["symplectic_centralizer_shell_orbits"],
    }
    if not all(count_relations.values()):
        errors.append(label + "EMBEDDED_COUNT_RELATION_MISMATCH")
    shell = {tuple(point) for point in direct.get("exact_order_shell", [])}
    cyclic = {tuple(point) for point in direct.get("cyclic_locus", [])}
    discard = {tuple(point) for point in direct.get("discarded_shell", [])}
    if cyclic.intersection(discard) or cyclic.union(discard) != shell:
        errors.append(label + "SHELL_PARTITION_MISMATCH")
    _validate_orbits(direct["cyclic_A_orbits"], q, direct["cyclic_locus"], label + "A_", errors)
    _validate_orbits(direct["full_CV_orbits"], q, direct["cyclic_locus"], label + "FULL_CV_", errors)
    _validate_orbits(direct["symplectic_CV_orbits"], q, direct["cyclic_locus"], label + "SP_CV_", errors)
    _validate_orbits(direct["full_shell_orbits"], q, direct["exact_order_shell"], label + "FULL_SHELL_", errors)
    _validate_orbits(direct["symplectic_shell_orbits"], q, direct["exact_order_shell"], label + "SP_SHELL_", errors)
    _validate_orbits(algebra["norm_fiber_orbits"], q, direct["cyclic_locus"], label + "NORM_FIBER_", errors)
    for key in ("full_quotient_transition", "symplectic_quotient_transition"):
        transition = direct.get(key, {})
        if type(transition) is not dict or set(transition) != TRANSITION_KEYS or transition.get("identity") is not True:
            errors.append(label + key.upper() + "_NOT_IDENTITY")
        elif type(transition.get("class_count")) is not int or type(transition.get("transition")) not in {list, tuple} or (
            list(transition.get("transition")) != list(range(transition.get("class_count")))
        ) or any(type(item) is not int for item in transition.get("transition")):
            errors.append(label + key.upper() + "_MAP_MISMATCH")
    reversing = direct.get("reversing")
    expected_reversing = expected["prime_reversing_group_shell_orbits"]
    if expected_reversing is None:
        if reversing is not None:
            errors.append(label + "COMPOSITE_REVERSING_NOT_NULL")
    elif type(reversing) is not dict or set(reversing) != REVERSING_KEYS or (
        reversing.get("shell_orbit_count") != expected_reversing
        or reversing.get("constructed_equals_brute") is not True
        or reversing.get("group_closed") is not True
        or reversing.get("cyclic_noncyclic_mixing") is not False
    ):
        errors.append(label + "REVERSING_RECORD_MISMATCH")
    else:
        _validate_matrix_sequence(reversing["constructed_group"], q, label + "REVERSING_CONSTRUCTED_", errors)
        _validate_matrix_sequence(reversing["brute_reversing_group"], q, label + "REVERSING_BRUTE_", errors)
        _validate_orbits(reversing["shell_orbits"], q, direct["exact_order_shell"], label + "REVERSING_", errors)
    norm_table = algebra.get("norm_table")
    if type(norm_table) not in {list, tuple} or len(norm_table) != q * q or any(
        type(record) is not dict or set(record) != NORM_RECORD_KEYS
        or type(record.get("a")) is not int or type(record.get("b")) is not int
        or not _matrix(record.get("matrix"), q)
        or not _residue(record.get("matrix_determinant"), q)
        or not _residue(record.get("algebra_norm"), q)
        or record.get("matrix_determinant") != record.get("algebra_norm")
        for record in norm_table
    ):
        errors.append(label + "NORM_TABLE_MISMATCH")
    elif not _unique(norm_table):
        errors.append(label + "NORM_TABLE_DUPLICATES")
    torsor = algebra.get("torsor_axioms")
    if type(torsor) is not dict or set(torsor) != TORSOR_KEYS or any(value is not True for value in torsor.values()):
        errors.append(label + "TORSOR_AXIOMS_NOT_EXACT")
    for key in ("retained_fraction", "discarded_fraction"):
        rational = ledger.get(key)
        if type(rational) is not dict or set(rational) != RATIONAL_KEYS or (
            type(rational.get("numerator")) is not int
            or type(rational.get("denominator")) is not int
            or type(rational.get("text")) is not str
            or rational.get("denominator", 0) < 1
        ):
            errors.append(label + key.upper() + "_NOT_EXACT")
    fibers = direct.get("delta_fibers")
    if type(fibers) not in {list, tuple} or not _unique(fibers) or any(
        type(record) is not dict or set(record) != DELTA_FIBER_KEYS
        or not _residue(record.get("delta"), q)
        or not _unique(record.get("points"))
        or not all(_vector(point, q) for point in record.get("points", []))
        for record in fibers
    ):
        errors.append(label + "DELTA_FIBERS_INVALID")


def validate_registered_result(payload: Any, project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    errors: list[str] = []
    if type(payload) is not dict or set(payload) != OUTER_KEYS:
        return {"stage": "R100_RESULT_SEMANTICS", "errors": ["OUTER_KEYS_NOT_EXACT"], "pass": False}
    code_sha = code_tree_sha256(root)
    claim = validate_claim(root, code_sha)
    expected_outer = {
        "schema": "CENTRALIZER_QUOTIENT_OFFICIAL_RESULT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "reviewed_code_sha256": code_sha,
        "registered_claim_sha256": claim.get("claim_sha256"),
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "pass": True,
    }
    for key, value in expected_outer.items():
        if payload.get(key) != value or type(payload.get(key)) is not type(value):
            errors.append("OUTER_" + key.upper() + "_MISMATCH")
    audit = payload.get("audit")
    if type(audit) is not dict or set(audit) != AUDIT_KEYS:
        errors.append("AUDIT_KEYS_NOT_EXACT")
    else:
        scalar_expected = {
            "schema": "CENTRALIZER_QUOTIENT_REGISTERED_EXACT_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "fixed_matrix": [[2, 1], [1, 1]],
            "locked_moduli": list(LOCKED_MODULI),
            "quotient_clock_status": "IDENTITY_NO_NATIVE_MODULUS_CLOCK",
            "formal_factor_status": "EXTERNAL_MODULUS_SPECIALIZATION",
            "external_modulus_label_required": True,
            "intrinsic_prime_selector": False,
            "local_pseudo_symmetry_scope": "Q_DEPENDENT_FULL_LOCAL_GL_CENTRALIZER",
            "registered_exact_audits": 1,
            "external_prime_tables_accessed": False,
            "riemann_zero_data_accessed": False,
            "all_q_inference_from_finite_audit": False,
            "novelty_inference_from_finite_audit": False,
            "route_b_opened": False,
            "classification": TERMINAL_CLASSIFICATION,
            "pass": True,
        }
        for key, value in scalar_expected.items():
            if audit.get(key) != value or type(audit.get(key)) is not type(value):
                errors.append("AUDIT_" + key.upper() + "_MISMATCH")
        for key in ZERO_COUNTERS:
            if audit.get(key) != 0 or type(audit.get(key)) is not int:
                errors.append("AUDIT_ZERO_COUNTER_MISMATCH:" + key)
        rows = audit.get("rows")
        if type(rows) is not list or len(rows) != len(LOCKED_MODULI):
            errors.append("ROWS_NOT_EXACT_LIST")
        else:
            if [row.get("q") if type(row) is dict else None for row in rows] != list(LOCKED_MODULI):
                errors.append("ROW_ORDER_MISMATCH")
            for row, q in zip(rows, LOCKED_MODULI, strict=True):
                _validate_row(row, q, errors)
        controls = audit.get("controls")
        if type(controls) is not dict or set(controls) != CONTROL_KEYS or any(value is not True for value in controls.values()):
            errors.append("CONTROLS_NOT_ALL_TRUE")
        proof = audit.get("proof_only_contract")
        validation = audit.get("proof_contract_validation")
        expected_proof = _proof_contract_expected()
        if not _exact_same(proof, expected_proof):
            errors.append("PROOF_CONTRACT_MISMATCH")
        expected_validation = {"expected": expected_proof, "errors": [], "pass": True}
        if not _exact_same(validation, expected_validation):
            errors.append("PROOF_CONTRACT_NOT_PASSING")
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


def _result_inventory(project_root: Path, expected: frozenset[str], *, ignore_manifest: bool = False) -> dict[str, Any]:
    root = lexical_absolute(project_root) / "results"
    manifest_name = Path(RESULT_MANIFEST_PATH).name
    first = sorted(entry.name for entry in root.iterdir() if not (ignore_manifest and entry.name == manifest_name))
    second = sorted(entry.name for entry in root.iterdir() if not (ignore_manifest and entry.name == manifest_name))
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
    post_tests = parse_junit(root / POSTRUN_TEST_PATH)
    post_tests["stage"] = "R111_POSTRUN_TEST_EVIDENCE"
    reports = [
        {"path": relative, "sha256": sha256_file(root / relative) if regular_file(root / relative) else None, "pass": regular_file(root / relative)}
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
        "schema": "CENTRALIZER_QUOTIENT_POSTRUN_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "execution_code_sha256": code_sha,
        "gates": gates,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "candidate_rerun_performed": False,
        "pass": all(record.get("pass") is True for record in gates.values()),
    }


def _manifest_payload(project_root: Path, expected_inventory: frozenset[str]) -> dict[str, Any]:
    root = lexical_absolute(project_root)
    audit = collect_postrun_audit(root)
    errors = [] if audit["pass"] is True else ["POSTRUN_AUDIT_NOT_PASSING"]
    inventory = _result_inventory(root, expected_inventory, ignore_manifest=expected_inventory == PREMANIFEST_RESULT_FILES)
    errors.extend(inventory["errors"])
    paths = sorted({"results/" + name for name in PREMANIFEST_RESULT_FILES}.union(OFFICIAL_REPORT_PATHS))
    files = []
    for relative in paths:
        if not regular_file(root / relative):
            errors.append("MANIFEST_INPUT_MISSING:" + relative)
        else:
            files.append({"path": relative, "sha256": sha256_file(root / relative)})
    return {
        "schema": "CENTRALIZER_QUOTIENT_RESULT_MANIFEST_V1",
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
