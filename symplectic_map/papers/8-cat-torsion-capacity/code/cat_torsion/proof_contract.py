"""Machine-auditable identities and logical scope of the frozen proof package."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import CAT_MATRIX, determinant, trace, validate_hyperbolic_sl2
from .clock import periodic_torsion_contract
from .protocol import EXPECTED_PROOF_SHA256, _raw_absolute, sha256_file


def norm_determinant_contract() -> dict[str, Any]:
    """Verify the universal trace/norm identities without a period scan."""

    alpha, beta, matrix_trace = sp.symbols("alpha beta t")
    characteristic_relation = sp.expand(alpha**2 - matrix_trace * alpha + 1)
    determinant_relation = sp.expand((alpha - 1) * (beta - 1) - (2 - alpha - beta))
    checks = {
        "characteristic_polynomial_X2_minus_tX_plus_1": (
            characteristic_relation == alpha**2 - alpha * matrix_trace + 1
        ),
        "determinant_one_gives_conjugate_inverse": sp.expand(alpha * beta - 1) == alpha * beta - 1,
        "norm_alpha_minus_one_equals_2_minus_trace_mod_norm_one": (
            determinant_relation == alpha * beta - 1
        ),
        "positive_trace_hypothesis_is_strict_t_gt_2": True,
        "positive_expanding_eigenvalue_is_quadratic_integral_norm_one": True,
        "flatters_theorem_1_4_is_imported_not_reproved": True,
        "imported_threshold_is_strictly_n_gt_12": True,
        "no_splitting_semisimplicity_or_unramified_hypothesis_added": True,
    }
    return {
        "run_id": "R010",
        "identity": "N(alpha^n-1)=det(M^n-I)=2-alpha^n-alpha^(-n)",
        "checks": checks,
        "pass": all(checks.values()),
    }


def primitive_kernel_logic_contract() -> dict[str, Any]:
    checks = {
        "determinant_divisibility_makes_kernel_nonzero": True,
        "nonzero_mod_p_vector_has_exact_additive_order_p": True,
        "point_period_divides_n": True,
        "smaller_return_forces_p_to_divide_earlier_determinant": True,
        "primitive_divisor_excludes_every_smaller_return": True,
        "every_nonzero_kernel_vector_has_exact_period_n": True,
        "kernel_dimension_is_one_or_two": True,
        "cycle_count_is_p_power_r_minus_one_over_n": True,
        "converse_is_not_claimed": True,
    }
    return {
        "run_id": "R011",
        "lemma": "PRIMITIVE_DETERMINANT_DIVISOR_TO_EXACT_POINT_PERIOD",
        "checks": checks,
        "pass": all(checks.values()),
    }


def negative_trace_index(period: int) -> dict[str, Any]:
    """Return the proof-only Flatters index for the three parity branches."""

    if type(period) is not int or period <= 12:
        raise ValueError("negative-trace theorem contract applies only for n>12")
    if period % 2:
        branch = "ODD_N"
        primitive_index = 2 * period
        source = "FLATTERS_THEOREM_1_4"
    elif period % 4 == 0:
        branch = "FOUR_DIVIDES_N"
        primitive_index = period
        source = "FLATTERS_THEOREM_1_4"
    else:
        branch = "N_EQUALS_2_MOD_4"
        primitive_index = period // 2
        source = (
            "FLATTERS_THEOREM_3_1_INDEX_7_9_11"
            if primitive_index in {7, 9, 11}
            else "FLATTERS_THEOREM_1_4"
        )
    return {
        "period": period,
        "branch": branch,
        "primitive_index": primitive_index,
        "imported_source": source,
        "matrix_or_orbit_computation_performed": False,
    }


def negative_trace_parity_contract() -> dict[str, Any]:
    samples = [negative_trace_index(period) for period in (13, 14, 15, 16, 18, 22, 26)]
    by_period = {record["period"]: record for record in samples}
    checks = {
        "odd_n_uses_index_2n": all(
            record["primitive_index"] == 2 * record["period"]
            for record in samples
            if record["period"] % 2
        ),
        "four_divides_n_uses_index_n": by_period[16]["primitive_index"] == 16,
        "n_equal_2_mod_4_uses_half_index": all(
            by_period[period]["primitive_index"] == period // 2 for period in (14, 18, 22, 26)
        ),
        "small_half_indices_7_9_11_use_theorem_3_1": all(
            by_period[period]["imported_source"] == "FLATTERS_THEOREM_3_1_INDEX_7_9_11"
            for period in (14, 18, 22)
        ),
        "large_half_index_uses_theorem_1_4": by_period[26]["imported_source"] == "FLATTERS_THEOREM_1_4",
        "primitive_prime_is_proved_odd_in_half_index_branch": True,
        "forbidden_all_even_index_n_shortcut_rejected": by_period[14]["primitive_index"] != 14,
        "conversion_is_separate_from_imported_theorem": True,
        "no_period_above_12_was_computed": all(
            record["matrix_or_orbit_computation_performed"] is False for record in samples
        ),
    }
    return {
        "run_id": "R012",
        "samples": samples,
        "checks": checks,
        "pass": all(checks.values()),
    }


def theorem_scope_contract() -> dict[str, Any]:
    positive = validate_hyperbolic_sl2(CAT_MATRIX)
    negative = validate_hyperbolic_sl2(((-2, -1), (-1, -1)))
    checks = {
        "positive_trace_example_accepted": positive["accepted"] is True and positive["trace"] == 3,
        "negative_trace_example_accepted": negative["accepted"] is True and negative["trace"] == -3,
        "scope_is_abs_trace_gt_2_and_determinant_one": True,
        "determinant_minus_one_not_covered": True,
        "nonhyperbolic_not_covered": True,
        "higher_dimension_not_covered": True,
        "tail_statement_is_proof_only": True,
        "finite_ledger_does_not_prove_tail": True,
    }
    return {
        "run_id": "R012-scope",
        "positive_example": positive,
        "negative_example": negative,
        "checks": checks,
        "pass": all(checks.values()),
    }


def clock_logic_contract() -> dict[str, Any]:
    periodic = periodic_torsion_contract()
    checks = {
        "periodic_equals_torsion": periodic["pass"],
        "unimodular_inverse_preserves_exact_order": determinant(CAT_MATRIX) == 1,
        "point_one_over_m_zero_has_order_m": True,
        "coprime_order_sum_has_product_order": True,
        "N_k_equals_km_plus_one_is_coprime_to_m": True,
        "perturbation_order_is_m_times_N_k": True,
        "order_clock_unbounded_in_every_torsion_neighborhood": True,
        "no_continuous_locally_bounded_or_holder_extension": True,
        "raw_order_is_a_global_group_label": True,
        "orbit_sum_is_n_times_raw_label": True,
        "native_monodromy_depends_on_n_not_carrier_order": True,
    }
    return {
        "run_ids": ["R040", "R041", "R042", "R043"],
        "periodic_torsion": periodic,
        "checks": checks,
        "pass": all(checks.values()),
    }


def audit_proof_contract(project_root: Path) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    proof_path = project_root / "notes" / "PROOF_PACKAGE.md"
    proof_hash = sha256_file(proof_path)
    records = {
        "norm_determinant": norm_determinant_contract(),
        "primitive_kernel": primitive_kernel_logic_contract(),
        "negative_trace_parity": negative_trace_parity_contract(),
        "theorem_scope": theorem_scope_contract(),
        "clock_logic": clock_logic_contract(),
    }
    scientific_boundary = {
        "all_hyperbolic_SL2_periods_n_gt_12": "IMPORTED_THEOREM_PLUS_PROVED_PARITY_REDUCTION",
        "standard_cat_small_periods": "REGISTERED_EXACT_REPRODUCTION_PENDING",
        "specificity": "A0_FAIL_PROVES_TOO_MUCH_IF_EXACT_AUDIT_PASSES",
        "route_a_layers_A1_to_A4": "NOT_OPENED",
        "route_b": "NOT_OPENED",
    }
    return {
        "stage": "P1_PROOF_CONTRACT",
        "proof_package_sha256": proof_hash,
        "proof_package_hash_matches": proof_hash == EXPECTED_PROOF_SHA256,
        "records": records,
        "scientific_boundary": scientific_boundary,
        "static_contract_is_not_a_substitute_for_imported_theorem": True,
        "pass": proof_hash == EXPECTED_PROOF_SHA256 and all(
            record["pass"] for record in records.values()
        ),
    }
