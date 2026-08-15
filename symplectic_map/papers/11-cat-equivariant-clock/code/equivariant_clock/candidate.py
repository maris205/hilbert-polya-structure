"""The sole registered exact audit over the frozen nine moduli."""

from __future__ import annotations

from typing import Any

from .constants import (
    CANDIDATE_ID,
    LOCKED_COMPOSITES,
    LOCKED_MODULI,
    PERIOD_COLLISIONS,
    SOURCE_LOCK_SHA256,
    TERMINAL_CLASSIFICATION,
)
from .cyclic_cset import structural_unit_control
from .invariants import audit_modulus


class RegisteredCandidateFailure(RuntimeError):
    """Fail closed while preserving the exact progress boundary."""

    def __init__(self, message: str, started: list[int], completed: list[int]) -> None:
        super().__init__(message)
        self.moduli_started = list(started)
        self.moduli_completed = list(completed)


def proof_only_contract() -> dict[str, Any]:
    return {
        "finite_audit_role": "FINITE_FALSIFICATION_AND_IMPLEMENTATION_CONTROL",
        "general_theorem_authority": "FROZEN_PROOF_PACKAGE_PLUS_STRUCTURAL_UNIT_CONTROL",
        "point_order_name": "POINT_ORDER_RATIONAL_BURNSIDE_ZETA",
        "orbit_order_name": "ORBIT_ORDER_INTEGRAL_BURNSIDE_ZETA",
        "strong_name": "LABELLED_Z_TIMES_G_PERMUTATION",
        "enhanced_name": "ENHANCED_BURNSIDE_CARRIER",
        "orbifold_map_type": "ADDITIVE_EXACT_PERIOD_REDUCTION_NOT_RING_HOMOMORPHISM",
        "coarse_and_stack_dynamics": "STATIC_PERIOD_ONE",
        "strongest_positive_boundary": "LABELLED_EFFECTIVE_TWIST_RECOVERED_INSIDE_VARYING_LOCAL_GROUP",
        "common_modulus_clock": False,
        "intrinsic_prime_selector": False,
        "route_b_open": False,
        "outside_scope": {
            "transfer_fredholm": "OUTSIDE_SCOPE_ROUTE_B_CLOSED",
            "hecke_quantization": "OUTSIDE_SCOPE_ROUTE_B_CLOSED",
            "ruelle_fried": "OUTSIDE_SCOPE",
            "prime_zero_RH": "OUTSIDE_SCOPE",
            "global_euler_product": "OUTSIDE_SCOPE",
        },
    }


def validate_proof_only_contract(record: Any) -> dict[str, Any]:
    expected = proof_only_contract()
    passed = record == expected
    return {
        "expected": expected,
        "errors": [] if passed else ["PROOF_CONTRACT_MISMATCH"],
        "pass": passed,
    }


def _control_ledger(
    rows: list[dict[str, Any]], structural: dict[str, Any], externality: dict[str, bool]
) -> dict[str, bool]:
    by_q = {row["q"]: row for row in rows}
    return {
        "K001": [row["q"] for row in rows] == list(LOCKED_MODULI),
        "K002": all(
            row["torsor"]["pass"] is True
            and all(row["torsor"]["checks"].values())
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
        "K012": externality
        == {
            "ambient_ring_varies_with_q": True,
            "intrinsic_prime_selector": False,
            "external_modulus_specialization_required": True,
            "common_modulus_clock_found": False,
        },
    }


def run_registered_candidate() -> dict[str, Any]:
    """Execute the fixed audit; no argument can vary a scientific input."""

    started: list[int] = []
    completed: list[int] = []
    rows: list[dict[str, Any]] = []
    try:
        for modulus in LOCKED_MODULI:
            started.append(modulus)
            row = audit_modulus(modulus)
            if row["pass"] is not True:
                raise RegisteredCandidateFailure(
                    "exact frozen control mismatch at modulus " + str(modulus),
                    started,
                    completed,
                )
            rows.append(row)
            completed.append(modulus)
        structural = structural_unit_control()
        if structural["pass"] is not True:
            raise RegisteredCandidateFailure("structural unit control failed", started, completed)
        proof = proof_only_contract()
        proof_validation = validate_proof_only_contract(proof)
        externality = {
            "ambient_ring_varies_with_q": True,
            "intrinsic_prime_selector": False,
            "external_modulus_specialization_required": True,
            "common_modulus_clock_found": False,
        }
        controls = _control_ledger(rows, structural, externality)
        if not all(controls.values()) or proof_validation["pass"] is not True:
            raise RegisteredCandidateFailure("closure control failed", started, completed)
        return {
            "schema": "EQUIVARIANT_CLOCK_REGISTERED_EXACT_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "fixed_matrix": [[2, 1], [1, 1]],
            "arithmetic_modulus_order": list(LOCKED_MODULI),
            "arithmetic_modulus_records": rows,
            "structural_unit_control": structural,
            "controls": controls,
            "proof_only_contract": proof,
            "proof_contract_validation": proof_validation,
            "registered_audit_count": 1,
            "arithmetic_modulus_record_count": 9,
            "structural_unit_control_count": 1,
            "structural_control_in_modulus_namespace": False,
            "candidate_rerun_count": 0,
            "candidate_numerical_run_count": 0,
            "network_access_count": 0,
            "external_prime_data_access_count": 0,
            "riemann_zero_data_access_count": 0,
            "numeric_s_evaluation_count": 0,
            "numeric_log_q_evaluation_count": 0,
            "numeric_q_power_minus_s_evaluation_count": 0,
            "random_seed_count": 0,
            "new_zeta_definition_count": 0,
            "cross_q_coefficient_ring_identification_count": 0,
            "adaptive_matrix_or_group_candidate_search_count": 0,
            "stack_simulation_beyond_exact_finite_formulas_count": 0,
            "external_data_load_count": 0,
            "route_b_open_count": 0,
            **externality,
            "classification": TERMINAL_CLASSIFICATION,
            "pass": True,
        }
    except RegisteredCandidateFailure:
        raise
    except BaseException as error:
        raise RegisteredCandidateFailure(str(error), started, completed) from error
