"""Regression and fail-closed tests for HCS-C22 T4/orbitwise-scalar T5."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from copy import deepcopy
from fractions import Fraction
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CODE_DIR.parent


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, CODE_DIR / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


producer = load_module("c22_t4_producer_test_module", "c22_t4_producer.py")
checker = load_module("c22_t4_checker_test_module", "c22_t4_independent_check.py")


def released_certificate() -> dict[str, object]:
    return json.loads(
        (PROJECT_ROOT / "results" / "c22_t4_certificate.json").read_text(encoding="utf-8")
    )


def test_multiplier_bounds_and_explicit_domain() -> None:
    result = producer.t4_certificate(7, 16)
    bounds = result["multiplier_bounds"]
    convergence = result["normal_convergence"]
    assert result["pass"] is True
    assert bounds["lower_base_squared"]["fraction"] == "129299641/14112000"
    assert bounds["upper_frobenius_base_squared"]["fraction"] == "11420060341/189778176"
    assert convergence["radius_landmarks"][2]["guaranteed_radius_decimal"].startswith(
        "0.3090169943749474241"
    )
    assert convergence["radius_landmarks"][3]["guaranteed_radius_decimal"].startswith(
        "0.9353771139241039095"
    )
    assert convergence["z_equals_one_requires_real_s_above"].startswith(
        "1.0603180797198193452"
    )


def test_exact_joint_primitive_repetition_audit() -> None:
    result = producer.t4_certificate(7, 10)
    rows = result["fixed_log_identity"]["formal_exact_regression"]["rows"]
    assert [row["fixed_joint_words"] for row in rows] == [2, 4, 32, 144, 352, 1024, 3712]
    assert [row["primitive_orbits_at_period"] for row in rows] == [2, 1, 10, 35, 70, 165, 530]
    assert all(row["exact_equality"] for row in rows)
    assert all(
        row["direct_trace_sha256"] == row["primitive_repetition_trace_sha256"]
        for row in rows
    )


def test_common_complex_domain_exact_margins() -> None:
    result = producer.common_complex_domain_certificate()
    assert result["common_two_letter_domain_pass"] is True
    assert result["X_strictly_inside_Y_margin"]["fraction"] == "1/128"
    assert result["minimum_radicand_modulus"]["fraction"] == "55/488"
    assert result["minimum_squared_boundary_gap"]["fraction"] == "7/4392"
    assert result["minimum_coordinate_clearance"]["fraction"] == "7/5490"
    assert result["derivative_squared_upper"]["fraction"] == "40/649"
    assert result["two_variable_sup_lipschitz_squared_upper"]["fraction"] == "160/649"
    assert result["two_variable_contraction"] is True
    assert len(result["rows"]) == 6


def test_orbitwise_scalar_double_repeat_obstruction_is_scoped() -> None:
    result = producer.orbitwise_scalar_trace_obstruction_certificate()
    assert result["obstruction_pass"] is True
    assert result["orbitwise_scalar_denominator_cancellation_pass"] is False
    assert result["matching_mode"] == "orbitwise_fixed_point_summands"
    assert result["independent_formal_orbit_markers"] is True
    assert result["aggregate_nonexistence_claimed"] is False
    assert result["signed_multiplicativity_mismatch"] == "-2*t*(t - 2)"
    assert result["positive_trace_absolute_gap"] == "4*(t - 2)"
    assert result["negative_trace_absolute_gap"] == "-4*(t - 2)"
    assert result["lifted_positive_multiplier_gap"] == "2*(2*x**2 - x + 1)"
    assert result["lifted_negative_multiplier_gap"] == "2*(2*x**2 + x + 1)"
    assert result["lifted_scalar_double_repeat_contradiction"] is True
    assert result["aggregate_scalar_fredholm_realization_excluded"] is False
    assert result["graded_exterior_algebra_superdeterminant_excluded"] is False
    assert result["arbitrary_nonlocal_operator_excluded"] is False


def test_common_projective_log_domain() -> None:
    result = producer.projective_lift_domain_certificate()
    assert result["common_projective_log_domain_pass"] is True
    assert result["minimum_log_sector_clearance"]["fraction"] == "11371/3360"
    assert result["maximum_projective_image_modulus"]["fraction"] == "125440/466211"
    assert result["slope_disk_image_clearance"]["fraction"] == "215331/932422"
    assert result["maximum_projective_derivative"]["fraction"] == "11289600/129299641"
    assert result["periodic_lift_multiplicity"] == 1
    assert result["stable_projective_fixed_point_in_domain"] is False


def test_released_artifacts_are_hash_bound_and_pass() -> None:
    certificate_path = PROJECT_ROOT / "results" / "c22_t4_certificate.json"
    check_path = PROJECT_ROOT / "results" / "c22_t4_independent_check.json"
    certificate_hash = hashlib.sha256(certificate_path.read_bytes()).hexdigest()
    check = json.loads(check_path.read_text(encoding="utf-8"))
    assert check["producer_sha256"] == certificate_hash
    assert check["pass"] is True
    assert released_certificate()["decision"]["all_certificate_checks_pass"] is True


def test_mutated_lower_multiplier_bound_fails() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["t4_intrinsic_instability_determinant"]["multiplier_bounds"][
        "lower_base_squared"
    ]["fraction"] = "1"
    checks = checker.check_t4(mutated)
    assert checks["multiplier_lower_exact"] is False


def test_deleted_complex_domain_row_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["t5_common_complex_domain"]["rows"].pop()
    checks = checker.check_complex_domain(mutated)
    assert checks["row_coverage"] is False
    assert checks["row_values"] is False


def test_formal_trace_tamper_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    rows = mutated["t4_intrinsic_instability_determinant"]["fixed_log_identity"][
        "formal_exact_regression"
    ]["rows"]
    rows[3]["direct_trace_sha256"] = "0" * 64
    checks = checker.check_t4(mutated)
    assert checks["formal_trace_values"] is False


def test_obstruction_scope_tamper_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["t5_orbitwise_scalar_trace_obstruction"][
        "graded_exterior_algebra_superdeterminant_excluded"
    ] = True
    checks = checker.check_obstruction(mutated)
    assert checks["scoped_claim"] is False


def test_orbitwise_matching_mode_tamper_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["t5_orbitwise_scalar_trace_obstruction"]["matching_mode"] = (
        "aggregate_period_trace"
    )
    checks = checker.check_obstruction(mutated)
    assert checks["structured_scope"] is False


def test_global_scalar_closure_tamper_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["decision"]["c22_positive_operator_claim"] = (
        "ALL_SCALAR_FREDHOLM_REALIZATIONS_CLOSED"
    )
    checks = checker.check_decision(mutated)
    assert checks["operator_claim_scoped"] is False


def test_aggregate_nonexistence_scope_tamper_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["scope"]["not_certified"].remove(
        "nonexistence of every aggregate scalar Fredholm representation"
    )
    mutated["scope"]["certified"].append(
        "nonexistence of every aggregate scalar Fredholm representation"
    )
    checks = checker.check_declared_scope(mutated)
    assert checks["exact_certified_scope"] is False
    assert checks["exact_not_certified_scope"] is False


def test_projective_log_scope_tamper_fails_closed() -> None:
    certificate = released_certificate()
    mutated = deepcopy(certificate)
    mutated["t5_projective_lift_domain"]["periodic_lift_multiplicity"] = 2
    checks = checker.check_projective_domain(mutated)
    assert checks["unique_unstable_lift"] is False


def test_exact_derivative_bound_is_strict() -> None:
    assert Fraction(40, 649) < Fraction(1, 16)
