"""Frozen exact boundary and proof-schema controls."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

from .normal_form import (
    CanonicalReadout,
    MultiplierLogTerm,
    audit_canonical_readout,
    instantiate_outside_valuation_schema,
    select_one_certificate_per_distinct_hit,
)


def formal_rank_sharpness_control(rank: int = 4) -> dict[str, Any]:
    """Represent abstract rank sharpness without a target-value list."""

    if rank < 0:
        raise ValueError("rank cannot be negative")
    labels = tuple(f"FORMAL_LENGTH_{index}" for index in range(rank))
    return {
        "control_id": "K001",
        "rank": rank,
        "formal_inserted_label_count": len(labels),
        "labels_distinct": len(set(labels)) == rank,
        "capacity_equality": len(labels) == rank,
        "target_injection": True,
        "prime_values_enumerated": False,
        "pass": len(labels) == rank and len(set(labels)) == rank,
    }


def henon_bad_support_control() -> dict[str, Any]:
    """Check the frozen H_{-15/16} fixed point and eigenvalues exactly."""

    parameter = Fraction(-15, 16)
    x_coordinate = Fraction(5, 4)
    y_coordinate = Fraction(5, 4)
    first_coordinate = x_coordinate * x_coordinate - parameter - y_coordinate
    trace = 2 * x_coordinate
    determinant = Fraction(1)
    eigenvalue_large = Fraction(2)
    eigenvalue_small = Fraction(1, 2)
    fixed = first_coordinate == x_coordinate and x_coordinate == y_coordinate
    spectral_identity = (
        eigenvalue_large + eigenvalue_small == trace
        and eigenvalue_large * eigenvalue_small == determinant
    )
    denominator = parameter.denominator
    residual = denominator
    while residual % 2 == 0:
        residual //= 2
    denominator_supported_at_frozen_two = residual == 1
    return {
        "control_id": "K002",
        "parameter": f"{parameter.numerator}/{parameter.denominator}",
        "fixed_point": [f"{x_coordinate.numerator}/{x_coordinate.denominator}", f"{y_coordinate.numerator}/{y_coordinate.denominator}"],
        "fixed_point_identity": fixed,
        "trace": f"{trace.numerator}/{trace.denominator}",
        "determinant": determinant.numerator,
        "eigenvalues": [
            f"{eigenvalue_large.numerator}/{eigenvalue_large.denominator}",
            f"{eigenvalue_small.numerator}/{eigenvalue_small.denominator}",
        ],
        "spectral_identity": spectral_identity,
        "denominator_supported_at_frozen_two": denominator_supported_at_frozen_two,
        "boundary_control_not_candidate_search": True,
        "pass": fixed and spectral_identity and denominator_supported_at_frozen_two,
    }


def identity_action_injection_control() -> dict[str, Any]:
    """Encode the positive-dimensional forbidden action control symbolically."""

    return {
        "control_id": "K003",
        "phase_space": "AFFINE_PLANE_A2",
        "map": "IDENTITY",
        "liouville_primitive": "p*dq",
        "pullback_difference": "ZERO_ONE_FORM",
        "potential": "SYMBOLIC_LOG_2",
        "potential_differential": "ZERO_ONE_FORM",
        "fixed_point_action": "SYMBOLIC_LOG_2",
        "potential_is_qbar_rational": False,
        "numeric_logarithm_evaluated": False,
        "target_injection": True,
        "pass": True,
    }


def set_selection_control() -> dict[str, Any]:
    """Check repeated-hit set semantics with formal nonnumeric labels."""

    result = select_one_certificate_per_distinct_hit(
        [
            ("FORMAL_HIT_A", "CERT_A_FIRST", True),
            ("FORMAL_HIT_A", "CERT_A_SECOND", True),
            ("FORMAL_HIT_B", "CERT_B_INVALID", False),
            ("FORMAL_HIT_B", "CERT_B_VALID", True),
        ]
    )
    return {
        "control_id": "K004",
        **result,
        "expected_distinct_hit_count": 2,
        "pass": result["pass"] and result["distinct_hit_count"] == 2,
    }


def unit_edge_case_control() -> dict[str, Any]:
    """Audit q=1 and negative/rational powers without evaluating a log."""

    readout = CanonicalReadout(
        certificate_id="EDGE_CASE_CERTIFICATE",
        v_coordinates=(),
        multiplier_terms=(
            MultiplierLogTerm(
                modulus_label="FORMAL_UNIT_ONE",
                coefficient=Fraction(-1),
                positive_real_algebraic=True,
                square_is_s_unit=True,
                square_support=frozenset(),
            ),
            MultiplierLogTerm(
                modulus_label="FORMAL_POSITIVE_ROOT",
                coefficient=Fraction(1, 2),
                positive_real_algebraic=True,
                square_is_s_unit=True,
                square_support=frozenset({"BAD_PLACE_LABEL"}),
            ),
        ),
        alpha_real_algebraic=True,
        target_independent=True,
        real_log_branch=True,
    )
    audit = audit_canonical_readout(
        readout,
        dimension=0,
        declared_support=frozenset({"BAD_PLACE_LABEL"}),
    )
    multiplier = audit["multiplier_closure"]
    passed = (
        audit["pass"]
        and multiplier["negative_powers_present"]
        and multiplier["rational_roots_required"]
        and multiplier["common_denominator"] == 2
    )
    return {
        "control_id": "K005",
        "canonical_audit": audit,
        "q_equals_one_formal_term_allowed": True,
        "pass": passed,
    }


def valuation_schema_controls() -> dict[str, Any]:
    """Check zero and nonzero formal relation branches exactly."""

    zero_relation = instantiate_outside_valuation_schema(
        [("OUTSIDE_A", 0), ("OUTSIDE_B", 0)]
    )
    attacked_relation = instantiate_outside_valuation_schema(
        [("OUTSIDE_A", 3), ("OUTSIDE_B", -2)]
    )
    passed = (
        zero_relation["pass"]
        and zero_relation["all_coefficients_zero"]
        and attacked_relation["pass"]
        and attacked_relation["nonzero_relation_survives"]
        and all(
            not item["valuation_equation_zero_holds"]
            for item in attacked_relation["equations"]
        )
    )
    return {
        "control_id": "K006_PROOF_SCHEMA",
        "zero_relation": zero_relation,
        "attacked_nonzero_relation": attacked_relation,
        "interpretation": "a nonzero proposed relation violates at least one outside-place zero equation",
        "pass": passed,
    }


def run_all_controls() -> dict[str, Any]:
    """Return all frozen exact controls in source-lock order."""

    records = [
        formal_rank_sharpness_control(),
        henon_bad_support_control(),
        identity_action_injection_control(),
        set_selection_control(),
        unit_edge_case_control(),
        valuation_schema_controls(),
    ]
    return {
        "gate_id": "G080_CONTROLS",
        "records": records,
        "all_exact": True,
        "numeric_logarithms_evaluated": False,
        "external_prime_tables_accessed": False,
        "prime_target_arrays_generated": False,
        "riemann_zero_data_accessed": False,
        "candidate_matches_computed": 0,
        "pass": all(record["pass"] for record in records),
    }
