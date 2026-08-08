#!/usr/bin/env python3
"""Independent checker for the HCS-C19 Frobenius certificate.

The finite-field implementation in this file is self-contained.  In
particular, it does not import the producer or the ``galois`` package.
SymPy is used only for independent characteristic-zero symbolic identities;
all finite-field construction, arithmetic, and point counting below is plain
Python.
"""

from __future__ import annotations

import argparse
from array import array
import hashlib
import itertools
import json
import math
from pathlib import Path
import time
from typing import Any, Iterable

import sympy as sp


PRODUCER_SCHEMA = "HCS-C19-producer-1"
CHECK_SCHEMA = "HCS-C19-independent-check-2"
TARGET_PRIMES = (5, 11, 13)
EXPECTED_BAD_PRIMES = [2, 7, 97]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_type(value: Any, expected: type, path: str) -> None:
    require(type(value) is expected, f"{path}: expected {expected.__name__}, got {type(value).__name__}")


def require_exact_keys(value: Any, expected: Iterable[str], path: str) -> dict[str, Any]:
    require_type(value, dict, path)
    expected_set = set(expected)
    actual_set = set(value)
    missing = sorted(expected_set - actual_set)
    extra = sorted(actual_set - expected_set)
    require(not missing and not extra, f"{path}: missing keys={missing}, extra keys={extra}")
    return value


def require_typed_list(value: Any, item_type: type, length: int, path: str) -> list[Any]:
    require_type(value, list, path)
    require(len(value) == length, f"{path}: expected length {length}, got {len(value)}")
    for index, item in enumerate(value):
        require_type(item, item_type, f"{path}[{index}]")
    return value


def validate_certificate_schema(certificate: Any) -> dict[int, dict[str, Any]]:
    """Validate every producer field before trusting any stored value."""
    top = require_exact_keys(
        certificate,
        {"schema_version", "candidate_id", "object", "symbolic", "frobenius", "route_scope"},
        "$",
    )
    for key in ("schema_version", "candidate_id", "object"):
        require_type(top[key], str, f"$.{key}")
    require(top["schema_version"] == PRODUCER_SCHEMA, "unexpected producer schema version")
    require(top["candidate_id"] == "HCS-C19", "unexpected candidate id")
    require(
        top["object"]
        == "genus-three scalar quotient control of the generically certified period-seven Henon carrier",
        "unexpected certified object",
    )

    route = require_exact_keys(
        top["route_scope"],
        {
            "arithmetic_structure",
            "chronological_time_character",
            "hilbert_polya_operator_claimed",
            "riemann_divisor_claimed",
        },
        "$.route_scope",
    )
    require_type(route["arithmetic_structure"], str, "$.route_scope.arithmetic_structure")
    require_type(route["chronological_time_character"], str, "$.route_scope.chronological_time_character")
    require_type(route["hilbert_polya_operator_claimed"], bool, "$.route_scope.hilbert_polya_operator_claimed")
    require_type(route["riemann_divisor_claimed"], bool, "$.route_scope.riemann_divisor_claimed")
    require(not route["hilbert_polya_operator_claimed"], "certificate overclaims a Hilbert-Polya operator")
    require(not route["riemann_divisor_claimed"], "certificate overclaims the Riemann divisor")
    require(
        route["arithmetic_structure"]
        == "positive genus-three curve with point-count-derived candidate Frobenius factors",
        "unexpected arithmetic-structure scope",
    )
    require(
        route["chronological_time_character"]
        == "constructed on companion ordered-edge cover; absent on scalar quotient",
        "certificate overstates chronological scope",
    )

    symbolic = require_exact_keys(
        top["symbolic"],
        {
            "branch_polynomial_discriminant",
            "branch_polynomial_q6",
            "degree_over_sigma_line",
            "discriminant_x",
            "finite_node",
            "generic_irreducibility",
            "infinity",
            "orbit_polynomial",
            "orientation_boundary",
            "parameter_relation",
            "q6_irreducible",
            "q6_ramification",
            "riemann_hurwitz",
            "source_correction",
            "plane_genus_cross_check",
        },
        "$.symbolic",
    )
    for key in (
        "branch_polynomial_discriminant",
        "branch_polynomial_q6",
        "discriminant_x",
        "orbit_polynomial",
        "parameter_relation",
    ):
        require_type(symbolic[key], str, f"$.symbolic.{key}")
    require_type(symbolic["degree_over_sigma_line"], int, "$.symbolic.degree_over_sigma_line")
    require_type(symbolic["q6_irreducible"], bool, "$.symbolic.q6_irreducible")
    require(symbolic["parameter_relation"] == "a = sigma^2 - 2*sigma", "stored parameter relation mismatch")
    require(symbolic["q6_irreducible"], "certificate denies Q6 irreducibility")

    correction = require_exact_keys(
        symbolic["source_correction"],
        {
            "status",
            "printed_equation_literal_constant",
            "adopted_dynamical_constant",
            "printed_discriminant_degree_in_sigma",
            "exact_witness",
            "journal_erratum_claimed",
        },
        "$.symbolic.source_correction",
    )
    for key in ("status", "printed_equation_literal_constant", "adopted_dynamical_constant"):
        require_type(correction[key], str, f"$.symbolic.source_correction.{key}")
    require_type(
        correction["printed_discriminant_degree_in_sigma"],
        int,
        "$.symbolic.source_correction.printed_discriminant_degree_in_sigma",
    )
    require_type(correction["journal_erratum_claimed"], bool, "$.symbolic.source_correction.journal_erratum_claimed")
    witness = require_exact_keys(
        correction["exact_witness"],
        {
            "field",
            "a",
            "sigma",
            "cycles",
            "corrected_coordinate_roots",
            "literal_printed_roots",
            "cycles_are_reversal_pair",
        },
        "$.symbolic.source_correction.exact_witness",
    )
    require_type(witness["field"], str, "$.symbolic.source_correction.exact_witness.field")
    require_type(witness["a"], int, "$.symbolic.source_correction.exact_witness.a")
    require_type(witness["sigma"], int, "$.symbolic.source_correction.exact_witness.sigma")
    require_type(witness["cycles_are_reversal_pair"], bool, "$.symbolic.source_correction.exact_witness.cycles_are_reversal_pair")
    require_typed_list(
        witness["corrected_coordinate_roots"], int, 7, "$.symbolic.source_correction.exact_witness.corrected_coordinate_roots"
    )
    require_type(witness["literal_printed_roots"], list, "$.symbolic.source_correction.exact_witness.literal_printed_roots")
    for index, root in enumerate(witness["literal_printed_roots"]):
        require_type(root, int, f"$.symbolic.source_correction.exact_witness.literal_printed_roots[{index}]")
    require_typed_list(witness["cycles"], list, 2, "$.symbolic.source_correction.exact_witness.cycles")
    for cycle_index, cycle in enumerate(witness["cycles"]):
        require_typed_list(cycle, list, 7, f"$.symbolic.source_correction.exact_witness.cycles[{cycle_index}]")
        for state_index, state in enumerate(cycle):
            require_typed_list(
                state,
                int,
                2,
                f"$.symbolic.source_correction.exact_witness.cycles[{cycle_index}][{state_index}]",
            )

    generic = require_exact_keys(
        symbolic["generic_irreducibility"],
        {"status", "specialization_sigma", "modulus", "polynomial", "irreducible"},
        "$.symbolic.generic_irreducibility",
    )
    require_type(generic["status"], str, "$.symbolic.generic_irreducibility.status")
    require_type(generic["specialization_sigma"], int, "$.symbolic.generic_irreducibility.specialization_sigma")
    require_type(generic["modulus"], int, "$.symbolic.generic_irreducibility.modulus")
    require_type(generic["polynomial"], str, "$.symbolic.generic_irreducibility.polynomial")
    require_type(generic["irreducible"], bool, "$.symbolic.generic_irreducibility.irreducible")
    require(
        generic
        == {
            "status": "PROVED",
            "specialization_sigma": -3,
            "modulus": 2,
            "polynomial": "x**7 + x**6 + x**5 + x**4 + 1",
            "irreducible": True,
        },
        "generic polynomial irreducibility witness changed",
    )

    node = require_exact_keys(
        symbolic["finite_node"],
        {"sigma", "x", "tangent_cone", "tangent_discriminant", "type", "ramification_after_normalization"},
        "$.symbolic.finite_node",
    )
    for key in ("sigma", "x", "tangent_cone", "tangent_discriminant", "type"):
        require_type(node[key], str, f"$.symbolic.finite_node.{key}")
    require_type(node["ramification_after_normalization"], int, "$.symbolic.finite_node.ramification_after_normalization")

    infinity = require_exact_keys(
        symbolic["infinity"],
        {
            "special_fibre",
            "formal_branch_count",
            "rational_branches",
            "ramification",
            "discriminant_order",
            "total_delta_invariant",
            "initial_forms",
        },
        "$.symbolic.infinity",
    )
    require_type(infinity["special_fibre"], str, "$.symbolic.infinity.special_fibre")
    require_type(infinity["formal_branch_count"], int, "$.symbolic.infinity.formal_branch_count")
    require_type(infinity["rational_branches"], bool, "$.symbolic.infinity.rational_branches")
    require_type(infinity["ramification"], int, "$.symbolic.infinity.ramification")
    require_type(infinity["discriminant_order"], int, "$.symbolic.infinity.discriminant_order")
    require_type(infinity["total_delta_invariant"], int, "$.symbolic.infinity.total_delta_invariant")
    require(infinity["ramification"] == 0, "infinity ramification must be zero")
    initial_forms = require_exact_keys(
        infinity["initial_forms"], {"minus", "minus_double", "plus", "plus_double"}, "$.symbolic.infinity.initial_forms"
    )
    for key, value in initial_forms.items():
        require_type(value, str, f"$.symbolic.infinity.initial_forms.{key}")

    ramification = require_exact_keys(
        symbolic["q6_ramification"],
        {"branch_values", "ramification_points_per_value", "ramification_index", "smoothness", "subresultant_last_nonzero_degree"},
        "$.symbolic.q6_ramification",
    )
    for key in ("branch_values", "ramification_points_per_value", "ramification_index", "subresultant_last_nonzero_degree"):
        require_type(ramification[key], int, f"$.symbolic.q6_ramification.{key}")
    require_type(ramification["smoothness"], str, "$.symbolic.q6_ramification.smoothness")
    require(
        ramification
        == {
            "branch_values": 6,
            "ramification_points_per_value": 3,
            "ramification_index": 2,
            "smoothness": "P_sigma is nonzero at the repeated roots",
            "subresultant_last_nonzero_degree": 3,
        },
        "stored Q6 ramification ledger mismatch",
    )

    rh = require_exact_keys(
        symbolic["riemann_hurwitz"],
        {"degree", "total_ramification", "twice_genus_minus_two", "genus"},
        "$.symbolic.riemann_hurwitz",
    )
    for key in rh:
        require_type(rh[key], int, f"$.symbolic.riemann_hurwitz.{key}")

    plane_genus = require_exact_keys(
        symbolic["plane_genus_cross_check"],
        {"arithmetic_genus", "finite_node_delta", "infinity_delta", "geometric_genus"},
        "$.symbolic.plane_genus_cross_check",
    )
    for key in plane_genus:
        require_type(plane_genus[key], int, f"$.symbolic.plane_genus_cross_check.{key}")

    orientation = require_exact_keys(
        symbolic["orientation_boundary"], {"full_chronology_claimed", "reason"}, "$.symbolic.orientation_boundary"
    )
    require_type(orientation["full_chronology_claimed"], bool, "$.symbolic.orientation_boundary.full_chronology_claimed")
    require_type(orientation["reason"], str, "$.symbolic.orientation_boundary.reason")
    require(
        orientation
        == {
            "full_chronology_claimed": False,
            "reason": "Henon time is constructed on the companion ordered-edge cover but does not act on this scalar quotient",
        },
        "orientation-boundary scope changed",
    )

    require_type(top["frobenius"], list, "$.frobenius")
    require(len(top["frobenius"]) > 0, "$.frobenius must not be empty")
    rows: dict[int, dict[str, Any]] = {}
    row_keys = {
        "affine_counts_r1_r3",
        "frobenius_power_sums_r1_r3",
        "frozen_model_screen",
        "irreducible_over_q",
        "l_polynomial",
        "l_polynomial_coefficients_ascending",
        "maximum_reciprocal_root_modulus_error",
        "node_splits_r1_r3",
        "normalization_counts_r1_r3",
        "predicted_normalization_counts_r1_r6",
        "prime",
    }
    for index, raw_row in enumerate(top["frobenius"]):
        path = f"$.frobenius[{index}]"
        row = require_exact_keys(raw_row, row_keys, path)
        require_type(row["prime"], int, f"{path}.prime")
        prime = row["prime"]
        require(prime not in rows, f"duplicate Frobenius row for p={prime}")
        require_typed_list(row["affine_counts_r1_r3"], int, 3, f"{path}.affine_counts_r1_r3")
        require_typed_list(row["frobenius_power_sums_r1_r3"], int, 3, f"{path}.frobenius_power_sums_r1_r3")
        require_typed_list(row["node_splits_r1_r3"], bool, 3, f"{path}.node_splits_r1_r3")
        require_typed_list(row["normalization_counts_r1_r3"], int, 3, f"{path}.normalization_counts_r1_r3")
        require_typed_list(
            row["predicted_normalization_counts_r1_r6"],
            int,
            6,
            f"{path}.predicted_normalization_counts_r1_r6",
        )
        require_typed_list(row["l_polynomial_coefficients_ascending"], int, 7, f"{path}.l_polynomial_coefficients_ascending")
        require_type(row["l_polynomial"], str, f"{path}.l_polynomial")
        require_type(row["irreducible_over_q"], bool, f"{path}.irreducible_over_q")
        require_type(row["maximum_reciprocal_root_modulus_error"], float, f"{path}.maximum_reciprocal_root_modulus_error")
        require(math.isfinite(row["maximum_reciprocal_root_modulus_error"]), f"{path}: non-finite Weil error")
        require(
            0.0 <= row["maximum_reciprocal_root_modulus_error"] <= 1e-10,
            f"{path}: stored Weil residual is outside [0, 1e-10]",
        )
        coefficients = row["l_polynomial_coefficients_ascending"]
        t_symbol = sp.symbols("T")
        canonical_l = str(sp.Poly(sum(c * t_symbol**i for i, c in enumerate(coefficients)), t_symbol, domain=sp.ZZ).as_expr())
        require(row["l_polynomial"] == canonical_l, f"{path}: L-polynomial string/coefficients mismatch")
        require(row["irreducible_over_q"], f"{path}: irreducible-over-Q flag is false")
        screen = require_exact_keys(
            row["frozen_model_screen"],
            {
                "complete_good_reduction_theorem_claimed",
                "exceptional_primes_visible_in_branch_data",
                "node_disjoint_from_q6",
                "q6_squarefree_mod_p",
                "only_expected_affine_node",
                "infinity_blowup_coefficients_are_units",
            },
            f"{path}.frozen_model_screen",
        )
        require_type(
            screen["complete_good_reduction_theorem_claimed"],
            bool,
            f"{path}.frozen_model_screen.complete_good_reduction_theorem_claimed",
        )
        require(
            not screen["complete_good_reduction_theorem_claimed"],
            f"{path}: frozen model screen must not claim a complete good-reduction theorem",
        )
        require_typed_list(
            screen["exceptional_primes_visible_in_branch_data"],
            int,
            3,
            f"{path}.frozen_model_screen.exceptional_primes_visible_in_branch_data",
        )
        require_type(screen["node_disjoint_from_q6"], bool, f"{path}.frozen_model_screen.node_disjoint_from_q6")
        require_type(screen["q6_squarefree_mod_p"], bool, f"{path}.frozen_model_screen.q6_squarefree_mod_p")
        require_type(screen["only_expected_affine_node"], bool, f"{path}.frozen_model_screen.only_expected_affine_node")
        require_type(
            screen["infinity_blowup_coefficients_are_units"],
            bool,
            f"{path}.frozen_model_screen.infinity_blowup_coefficients_are_units",
        )
        require(screen["exceptional_primes_visible_in_branch_data"] == EXPECTED_BAD_PRIMES, f"{path}: bad-prime ledger changed")
        require(screen["q6_squarefree_mod_p"], f"{path}: Q6 squarefree screen is false")
        require(screen["node_disjoint_from_q6"], f"{path}: node/Q6 disjointness screen is false")
        require(screen["only_expected_affine_node"], f"{path}: unexpected affine singularity screen is false")
        require(screen["infinity_blowup_coefficients_are_units"], f"{path}: infinity-unit screen is false")
        rows[prime] = row

    require(set(rows) == set(TARGET_PRIMES), f"expected exactly final primes {list(TARGET_PRIMES)}, got {sorted(rows)}")
    return rows


def orbit_polynomial() -> tuple[sp.Symbol, sp.Symbol, sp.Expr]:
    """Construct P from its defining parameter relation, not stored text."""
    x, sigma = sp.symbols("x sigma")
    a = sigma**2 - 2 * sigma
    polynomial = (
        x**7
        - sigma * x**6
        - (3 * a - 2 * sigma) * x**5
        - (2 * a - (3 * a - 4) * sigma - 4) * x**4
        + (3 * a**2 - 2 * (2 * a - 1) * sigma + 1) * x**3
        + (4 * a**2 - 10 * a - (3 * a**2 - 8 * a + 1) * sigma - 2) * x**2
        - (a - 1) * (a**2 - 2 * a * sigma + a + 2) * x
        - 2 * a**3
        + 6 * a**2
        + 2 * a
        + 3
        + (a**3 - 4 * a**2 + a - 2) * sigma
    )
    return x, sigma, sp.expand(polynomial)


def weighted_initial_form(
    expression: sp.Expr,
    variables: tuple[sp.Symbol, ...],
    weights: tuple[int, ...],
) -> sp.Expr:
    terms = sp.Poly(sp.expand(expression), *variables).terms()
    minimum = min(sum(power * weight for power, weight in zip(exponents, weights)) for exponents, _ in terms)
    return sp.factor(
        sum(
            coefficient * sp.prod(variable**power for variable, power in zip(variables, exponents))
            for exponents, coefficient in terms
            if sum(power * weight for power, weight in zip(exponents, weights)) == minimum
        )
    )


def symbolic_checks(certificate: dict[str, Any]) -> tuple[sp.Expr, sp.Expr, sp.Expr, dict[str, Any]]:
    x, sigma, polynomial = orbit_polynomial()
    a_relation = sigma**2 - 2 * sigma
    correction_block = a_relation**3 - 4 * a_relation**2 + a_relation - 2
    printed_polynomial = sp.expand(polynomial - (3 + correction_block * sigma) + 3 * correction_block * sigma)
    q6 = (
        64 * sigma**6
        - 448 * sigma**5
        + 848 * sigma**4
        + 80 * sigma**3
        - 1048 * sigma**2
        + 152 * sigma
        - 151
    )
    discriminant = sp.factor(sp.discriminant(polynomial, x))
    expected_discriminant = (4 * sigma - 9) ** 2 * q6**3
    require(sp.expand(discriminant - expected_discriminant) == 0, "independent discriminant factorization failed")
    q6_discriminant = sp.factor(sp.discriminant(q6, sigma))
    require(q6_discriminant == 2**63 * 97, "independent Q6 discriminant failed")
    printed_discriminant = sp.factor(sp.discriminant(printed_polynomial, x))
    printed_discriminant_degree = int(sp.degree(printed_discriminant, sigma))
    require(printed_discriminant_degree == 42, "literal printed Eq.16 discriminant degree changed")
    resultant_sigma = sp.factor(sp.resultant(polynomial, sp.diff(polynomial, sigma), x))
    specialization = sp.Poly(polynomial.subs(sigma, -3), x, modulus=2)
    require(specialization.is_irreducible, "independent generic-polynomial irreducibility witness failed")
    require(sp.Poly(q6, sigma, domain=sp.QQ).is_irreducible, "independent Q6 irreducibility check failed")

    q6_poly = sp.Poly(q6, sigma, domain=sp.QQ)
    vanishing_subresultant_degrees: list[int] = []
    last_nonzero_subresultant_degree = None
    for subresultant in sp.subresultants(polynomial, sp.diff(polynomial, x), x):
        reduced_coefficients = [
            sp.Poly(coefficient, sigma, domain=sp.QQ).rem(q6_poly).as_expr()
            for coefficient in sp.Poly(subresultant, x).all_coeffs()
        ]
        if all(coefficient == 0 for coefficient in reduced_coefficients):
            vanishing_subresultant_degrees.append(int(sp.degree(subresultant, x)))
        else:
            last_nonzero_subresultant_degree = int(sp.degree(subresultant, x))
    require(
        last_nonzero_subresultant_degree == 3 and vanishing_subresultant_degrees == [2, 1, 0],
        "independent Q6 subresultant pattern failed",
    )
    singular_projection_gcd = sp.factor(
        sp.gcd(
            sp.Poly(discriminant, sigma, domain=sp.QQ),
            sp.Poly(resultant_sigma, sigma, domain=sp.QQ),
        ).as_expr()
    )
    require(
        sp.expand(16 * singular_projection_gcd - (4 * sigma - 9) ** 2) == 0,
        "independent finite singularity/smooth-ramification projection failed",
    )

    node_sigma = sp.Rational(9, 4)
    node_x = sp.Rational(1, 4)
    node_values = (
        sp.expand(polynomial.subs({sigma: node_sigma, x: node_x})),
        sp.expand(sp.diff(polynomial, sigma).subs({sigma: node_sigma, x: node_x})),
        sp.expand(sp.diff(polynomial, x).subs({sigma: node_sigma, x: node_x})),
    )
    require(node_values == (0, 0, 0), "finite node is not singular at (9/4,1/4)")
    t, y = sp.symbols("t y")
    local = sp.expand(polynomial.subs({sigma: node_sigma + t, x: node_x + y}))
    tangent = weighted_initial_form(local, (t, y), (1, 1))
    expected_tangent = -(137 * t**2 - 10 * t * y + y**2) / 8
    require(sp.expand(tangent - expected_tangent) == 0, "independent node tangent cone failed")
    tangent_discriminant = sp.factor(sp.discriminant(sp.Poly(tangent, y), y))
    require(tangent_discriminant == -7 * t**2, "independent node tangent discriminant failed")
    require(sp.factor(q6.subs(sigma, node_sigma)) != 0, "node collides with Q6 over Q")

    infinity_polynomial = sp.cancel(t**7 * polynomial.subs({sigma: 1 / t, x: y / t}))
    infinity_fibre = sp.factor(infinity_polynomial.subs(t, 0))
    require(infinity_fibre == (y - 1) ** 4 * (y + 1) ** 3, "independent infinity fibre failed")
    z, w = sp.symbols("z w")
    infinity_initials = {
        "plus": weighted_initial_form(infinity_polynomial.subs(y, 1 + z), (t, z), (1, 1)),
        "minus": weighted_initial_form(infinity_polynomial.subs(y, -1 + z), (t, z), (1, 1)),
        "plus_double": weighted_initial_form(infinity_polynomial.subs(y, 1 - t + w), (t, w), (1, 2)),
        "minus_double": weighted_initial_form(infinity_polynomial.subs(y, -1 + t + w), (t, w), (1, 2)),
    }
    expected_initials = {
        "plus": 8 * z * (t + z) ** 2 * (2 * t + z),
        "minus": 16 * (-2 * t + z) * (-t + z) ** 2,
        "plus_double": -4 * t**2 * w * (t**2 + 2 * w),
        "minus_double": -8 * t * (t**2 - 2 * w) * (t**2 - w),
    }
    require(
        all(sp.expand(infinity_initials[key] - expected_initials[key]) == 0 for key in expected_initials),
        "independent infinity blow-up initial forms failed",
    )
    infinity_discriminant = sp.factor(sp.discriminant(infinity_polynomial, y))
    infinity_discriminant_order = int(sp.Poly(infinity_discriminant, t).terms()[-1][0][0])
    require(infinity_discriminant_order == 22, "independent infinity discriminant order failed")
    arithmetic_genus = (7 - 1) * (7 - 2) // 2
    finite_node_delta = 1
    infinity_delta = infinity_discriminant_order // 2
    geometric_genus = arithmetic_genus - finite_node_delta - infinity_delta
    require((arithmetic_genus, finite_node_delta, infinity_delta, geometric_genus) == (15, 1, 11, 3), "plane genus delta check failed")

    modulus = 103
    fixed_a = 6
    fixed_sigma = 26
    require((fixed_sigma**2 - 2 * fixed_sigma) % modulus == fixed_a, "F_103 chiral parameter relation failed")
    corrected_roots = {
        value for value in range(modulus) if int(polynomial.subs({sigma: fixed_sigma, x: value})) % modulus == 0
    }
    literal_printed_roots = {
        value for value in range(modulus) if int(printed_polynomial.subs({sigma: fixed_sigma, x: value})) % modulus == 0
    }
    require(len(corrected_roots) == 7, "adopted polynomial does not have seven distinct F_103 roots")
    require(literal_printed_roots != corrected_roots, "literal printed roots unexpectedly equal adopted roots")

    def henon(state: tuple[int, int]) -> tuple[int, int]:
        coordinate, previous = state
        return ((fixed_a - coordinate * coordinate - previous) % modulus, coordinate)

    canonical_cycles: set[tuple[tuple[int, int], ...]] = set()
    for coordinate in corrected_roots:
        for previous in corrected_roots:
            states: list[tuple[int, int]] = []
            state = (coordinate, previous)
            for _ in range(7):
                states.append(state)
                state = henon(state)
            if state != states[0] or len(set(states)) != 7:
                continue
            if {q for q, _ in states} != corrected_roots or sum(q for q, _ in states) % modulus != fixed_sigma:
                continue
            rotations = [tuple(states[index:] + states[:index]) for index in range(7)]
            canonical_cycles.add(min(rotations))
    cycles = sorted(canonical_cycles)
    require(len(cycles) == 2, f"expected two oriented F_103 cycles, found {len(cycles)}")
    require(set(cycles[1]) == {(previous, coordinate) for coordinate, previous in cycles[0]}, "F_103 cycles are not reversals")

    a_symbol = sp.symbols("a")
    adopted_constant = -2 * a_symbol**3 + 6 * a_symbol**2 + 2 * a_symbol + 3 + (
        a_symbol**3 - 4 * a_symbol**2 + a_symbol - 2
    ) * sigma
    printed_constant = -2 * a_symbol**3 + 6 * a_symbol**2 + 2 * a_symbol + 3 * (
        a_symbol**3 - 4 * a_symbol**2 + a_symbol - 2
    ) * sigma

    stored = certificate["symbolic"]
    locals_map = {"a": a_symbol, "x": x, "sigma": sigma, "t": t, "y": y, "z": z, "w": w}
    require(sp.expand(sp.sympify(stored["orbit_polynomial"], locals=locals_map) - polynomial) == 0, "stored orbit polynomial mismatch")
    require(sp.expand(sp.sympify(stored["branch_polynomial_q6"], locals=locals_map) - q6) == 0, "stored Q6 mismatch")
    require(sp.expand(sp.sympify(stored["discriminant_x"], locals=locals_map) - discriminant) == 0, "stored x-discriminant mismatch")
    require(int(stored["branch_polynomial_discriminant"]) == q6_discriminant, "stored Q6 discriminant mismatch")
    stored_node = stored["finite_node"]
    require(stored_node["sigma"] == "9/4" and stored_node["x"] == "1/4", "stored node coordinates mismatch")
    require(sp.expand(sp.sympify(stored_node["tangent_cone"], locals=locals_map) - tangent) == 0, "stored tangent cone mismatch")
    require(
        sp.expand(sp.sympify(stored_node["tangent_discriminant"], locals=locals_map) - tangent_discriminant) == 0,
        "stored tangent discriminant mismatch",
    )
    require(stored_node["type"] == "ordinary node", "stored node type mismatch")
    require(stored_node["ramification_after_normalization"] == 0, "stored node ramification mismatch")
    require(stored["degree_over_sigma_line"] == 7, "stored cover degree mismatch")
    require(stored["parameter_relation"] == "a = sigma^2 - 2*sigma", "stored parameter relation mismatch")
    require(stored["q6_irreducible"], "stored Q6 irreducibility flag is false")
    require(
        stored["generic_irreducibility"]["polynomial"] == str(specialization.as_expr())
        and stored["generic_irreducibility"]["irreducible"],
        "stored generic-polynomial irreducibility witness mismatch",
    )
    require(stored["q6_ramification"]["subresultant_last_nonzero_degree"] == last_nonzero_subresultant_degree, "stored Q6 subresultant degree mismatch")
    require(stored["infinity"]["formal_branch_count"] == 7, "stored infinity branch count mismatch")
    require(stored["infinity"]["rational_branches"], "stored infinity branches are not rational")
    require(stored["infinity"]["ramification"] == 0, "stored infinity ramification mismatch")
    require(sp.expand(sp.sympify(stored["infinity"]["special_fibre"], locals=locals_map) - infinity_fibre) == 0, "stored infinity fibre mismatch")
    for key, initial in infinity_initials.items():
        require(
            sp.expand(sp.sympify(stored["infinity"]["initial_forms"][key], locals=locals_map) - initial) == 0,
            f"stored infinity initial form mismatch: {key}",
        )
    require(stored["infinity"]["discriminant_order"] == infinity_discriminant_order, "stored infinity discriminant order mismatch")
    require(stored["infinity"]["total_delta_invariant"] == infinity_delta, "stored infinity delta mismatch")
    require(stored["riemann_hurwitz"] == {"degree": 7, "genus": 3, "total_ramification": 18, "twice_genus_minus_two": 4}, "stored genus data mismatch")
    require(
        stored["plane_genus_cross_check"]
        == {"arithmetic_genus": 15, "finite_node_delta": 1, "geometric_genus": 3, "infinity_delta": 11},
        "stored plane genus cross-check mismatch",
    )

    correction = stored["source_correction"]
    require(correction["status"] == "EXACT_SPECIALIZATION_CERTIFIED_APPARENT_PRINT_ERROR", "source-correction status mismatch")
    require(not correction["journal_erratum_claimed"], "certificate improperly claims a journal erratum")
    require(
        sp.expand(sp.sympify(correction["printed_equation_literal_constant"], locals=locals_map) - printed_constant) == 0,
        "stored printed Eq.16 literal constant mismatch",
    )
    require(
        sp.expand(sp.sympify(correction["adopted_dynamical_constant"], locals=locals_map) - adopted_constant) == 0,
        "stored adopted dynamical constant mismatch",
    )
    require(correction["printed_discriminant_degree_in_sigma"] == printed_discriminant_degree, "stored printed discriminant degree mismatch")
    witness = correction["exact_witness"]
    derived_cycles = [[[coordinate, previous] for coordinate, previous in cycle] for cycle in cycles]
    require(witness["field"] == "F_103" and witness["a"] == fixed_a and witness["sigma"] == fixed_sigma, "stored F_103 witness parameters mismatch")
    require(witness["corrected_coordinate_roots"] == sorted(corrected_roots), "stored adopted root set mismatch")
    require(witness["literal_printed_roots"] == sorted(literal_printed_roots), "stored literal printed root set mismatch")
    require(witness["cycles"] == derived_cycles, "stored F_103 cycles mismatch")
    require(witness["cycles_are_reversal_pair"], "stored F_103 reversal assertion is false")

    return q6, discriminant, resultant_sigma, {
        "orbit_polynomial_matches": True,
        "discriminant_identity": str(discriminant),
        "q6_discriminant": int(q6_discriminant),
        "generic_polynomial_irreducibility_witness": {
            "specialization_sigma": -3,
            "modulus": 2,
            "polynomial": str(specialization.as_expr()),
            "irreducible": True,
            "scope": "scalar genus certificate only; generic chronology is certified separately on the ordered-edge cover",
        },
        "q6_irreducible_over_q": True,
        "q6_ramification": {
            "last_nonzero_subresultant_degree": last_nonzero_subresultant_degree,
            "vanishing_subresultant_degrees": vanishing_subresultant_degrees,
            "smooth_projection_check": True,
        },
        "node_coordinates": {"sigma": "9/4", "x": "1/4"},
        "node_value_and_first_derivatives": [int(value) for value in node_values],
        "node_tangent_cone": str(tangent),
        "node_tangent_discriminant": str(tangent_discriminant),
        "node_disjoint_from_q6_over_q": True,
        "source_correction": {
            "status": correction["status"],
            "journal_erratum_claimed": False,
            "field": "F_103",
            "a": fixed_a,
            "sigma": fixed_sigma,
            "adopted_coordinate_roots": sorted(corrected_roots),
            "literal_printed_roots": sorted(literal_printed_roots),
            "literal_roots_differ": True,
            "independently_derived_cycles": derived_cycles,
            "cycles_are_reversal_pair": True,
            "printed_discriminant_degree_in_sigma": printed_discriminant_degree,
        },
        "infinity": {
            "rational_branch_count_used": 7,
            "discriminant_order": infinity_discriminant_order,
            "total_delta_invariant": infinity_delta,
            "initial_forms_match": True,
        },
        "plane_genus_cross_check": {
            "arithmetic_genus": arithmetic_genus,
            "finite_node_delta": finite_node_delta,
            "infinity_delta": infinity_delta,
            "geometric_genus": geometric_genus,
        },
    }


def trim_polynomial(poly: list[int], p: int) -> list[int]:
    result = [coefficient % p for coefficient in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_divmod(left: list[int], right: list[int], p: int) -> tuple[list[int], list[int]]:
    numerator = trim_polynomial(left, p)
    denominator = trim_polynomial(right, p)
    require(denominator != [0], "polynomial division by zero")
    if len(numerator) < len(denominator):
        return [0], numerator
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], p - 2, p)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] * inverse_lead % p
        quotient[shift] = factor
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] = (numerator[index + shift] - factor * coefficient) % p
        numerator = trim_polynomial(numerator, p)
    return trim_polynomial(quotient, p), numerator


def polynomial_gcd(left: list[int], right: list[int], p: int) -> list[int]:
    a = trim_polynomial(left, p)
    b = trim_polynomial(right, p)
    while b != [0]:
        _, remainder = polynomial_divmod(a, b, p)
        a, b = b, remainder
    if a == [0]:
        return a
    inverse = pow(a[-1], p - 2, p)
    return [(coefficient * inverse) % p for coefficient in a]


def polynomial_multiply_mod(left: list[int], right: list[int], modulus: list[int], p: int) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % p
    return polynomial_divmod(product, modulus, p)[1]


def polynomial_power_mod(base: list[int], exponent: int, modulus: list[int], p: int) -> list[int]:
    result = [1]
    value = polynomial_divmod(base, modulus, p)[1]
    while exponent:
        if exponent & 1:
            result = polynomial_multiply_mod(result, value, modulus, p)
        value = polynomial_multiply_mod(value, value, modulus, p)
        exponent >>= 1
    return trim_polynomial(result, p)


def prime_factors(number: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    remaining = number
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


def is_irreducible(modulus: tuple[int, ...], p: int) -> bool:
    degree = len(modulus) - 1
    if degree == 1:
        return modulus[-1] % p != 0
    polynomial = list(modulus)
    x_poly = [0, 1]
    for factor in prime_factors(degree):
        power = polynomial_power_mod(x_poly, p ** (degree // factor), polynomial, p)
        difference = power + [0] * max(0, len(x_poly) - len(power))
        if len(difference) < 2:
            difference += [0] * (2 - len(difference))
        difference[1] = (difference[1] - 1) % p
        if len(polynomial_gcd(difference, polynomial, p)) > 1:
            return False
    final_power = polynomial_power_mod(x_poly, p**degree, polynomial, p)
    difference = final_power + [0] * max(0, 2 - len(final_power))
    difference[1] = (difference[1] - 1) % p
    return trim_polynomial(difference, p) == [0]


def first_irreducible_modulus(p: int, degree: int) -> tuple[int, ...]:
    if degree == 1:
        return (0, 1)
    for coefficients in itertools.product(range(p), repeat=degree):
        if coefficients[0] == 0:
            continue
        candidate = tuple(coefficients) + (1,)
        if is_irreducible(candidate, p):
            return candidate
    raise AssertionError(f"no irreducible polynomial found over F_{p} of degree {degree}")


class FiniteField:
    """Small F_p[t]/(f) with integer-encoded coefficient vectors."""

    def __init__(self, p: int, degree: int) -> None:
        self.p = p
        self.degree = degree
        self.order = p**degree
        self.modulus = first_irreducible_modulus(p, degree)
        self._powers = [p**index for index in range(degree)]
        self._digits = [self._decode(value) for value in range(self.order)]
        self.negatives = [self._encode(tuple((-digit) % p for digit in digits)) for digits in self._digits]
        self.exponents, self.logarithms, self.primitive_element = self._build_log_tables()
        typecode = "H" if self.order <= 65535 else "I"
        self.addition = array(typecode)
        for left_digits in self._digits:
            self.addition.extend(
                self._encode(tuple((a + b) % p for a, b in zip(left_digits, right_digits)))
                for right_digits in self._digits
            )

    def _decode(self, value: int) -> tuple[int, ...]:
        digits = []
        for _ in range(self.degree):
            digits.append(value % self.p)
            value //= self.p
        return tuple(digits)

    def _encode(self, digits: tuple[int, ...]) -> int:
        return sum(digit * power for digit, power in zip(digits, self._powers))

    def _raw_multiply(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        convolution = [0] * (2 * self.degree - 1)
        for i, a in enumerate(self._digits[left]):
            for j, b in enumerate(self._digits[right]):
                convolution[i + j] += a * b
        for power in range(len(convolution) - 1, self.degree - 1, -1):
            leading = convolution[power] % self.p
            if leading:
                shift = power - self.degree
                for j in range(self.degree):
                    convolution[shift + j] -= leading * self.modulus[j]
        return self._encode(tuple(coefficient % self.p for coefficient in convolution[: self.degree]))

    def _raw_power(self, base: int, exponent: int) -> int:
        result = 1
        value = base
        while exponent:
            if exponent & 1:
                result = self._raw_multiply(result, value)
            value = self._raw_multiply(value, value)
            exponent >>= 1
        return result

    def _build_log_tables(self) -> tuple[list[int], list[int], int]:
        group_order = self.order - 1
        factors = prime_factors(group_order)
        primitive = None
        for candidate in range(2, self.order):
            if all(self._raw_power(candidate, group_order // factor) != 1 for factor in factors):
                primitive = candidate
                break
        require(primitive is not None, f"failed to find primitive element in F_{self.order}")
        exponents = [0] * group_order
        logarithms = [-1] * self.order
        value = 1
        for exponent in range(group_order):
            require(logarithms[value] == -1, "primitive-element cycle repeated early")
            exponents[exponent] = value
            logarithms[value] = exponent
            value = self._raw_multiply(value, primitive)
        require(value == 1 and all(logarithms[value] >= 0 for value in range(1, self.order)), "incomplete log table")
        return exponents, logarithms, primitive

    def add(self, left: int, right: int) -> int:
        return self.addition[left * self.order + right]

    def neg(self, value: int) -> int:
        return self.negatives[value]

    def sub(self, left: int, right: int) -> int:
        return self.add(left, self.neg(right))

    def mul(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        exponent = self.logarithms[left] + self.logarithms[right]
        if exponent >= self.order - 1:
            exponent -= self.order - 1
        return self.exponents[exponent]

    def power(self, value: int, exponent: int) -> int:
        if exponent == 0:
            return 1
        if value == 0:
            return 0
        return self.exponents[(self.logarithms[value] * exponent) % (self.order - 1)]


def field_sum(field: FiniteField, *values: int) -> int:
    result = 0
    for value in values:
        result = field.add(result, value)
    return result


def field_coefficients(field: FiniteField, sigma: int) -> tuple[int, ...]:
    """Descending x-coefficients of independently encoded P(sigma,x)."""
    c = lambda integer: integer % field.p
    add, sub, mul, neg = field.add, field.sub, field.mul, field.neg
    sigma2 = mul(sigma, sigma)
    a = sub(sigma2, mul(c(2), sigma))
    a2 = mul(a, a)
    a3 = mul(a2, a)
    coefficient5 = neg(sub(mul(c(3), a), mul(c(2), sigma)))
    coefficient4 = neg(sub(sub(mul(c(2), a), mul(sub(mul(c(3), a), c(4)), sigma)), c(4)))
    coefficient3 = field_sum(
        field,
        mul(c(3), a2),
        neg(mul(c(2), mul(sub(mul(c(2), a), c(1)), sigma))),
        c(1),
    )
    coefficient2 = field_sum(
        field,
        mul(c(4), a2),
        neg(mul(c(10), a)),
        neg(mul(field_sum(field, mul(c(3), a2), neg(mul(c(8), a)), c(1)), sigma)),
        neg(c(2)),
    )
    coefficient1 = neg(
        mul(
            sub(a, c(1)),
            field_sum(field, a2, neg(mul(c(2), mul(a, sigma))), a, c(2)),
        )
    )
    coefficient0 = field_sum(
        field,
        neg(mul(c(2), a3)),
        mul(c(6), a2),
        mul(c(2), a),
        c(3),
        mul(field_sum(field, a3, neg(mul(c(4), a2)), a, neg(c(2))), sigma),
    )
    return (
        c(1),
        neg(sigma),
        coefficient5,
        coefficient4,
        coefficient3,
        coefficient2,
        coefficient1,
        coefficient0,
    )


def affine_count(p: int, degree: int) -> tuple[int, bool, dict[str, Any]]:
    field = FiniteField(p, degree)
    q = field.order
    group_order = q - 1
    exponents = field.exponents
    logarithms = field.logarithms
    addition = field.addition
    x_logs = logarithms
    total = 0
    for sigma in range(q):
        coefficients = field_coefficients(field, sigma)
        values = [1] * q
        for coefficient in coefficients[1:]:
            addition_offset = coefficient * q
            values[0] = coefficient
            for x_value in range(1, q):
                current = values[x_value]
                if current == 0:
                    product = 0
                else:
                    exponent = logarithms[current] + x_logs[x_value]
                    if exponent >= group_order:
                        exponent -= group_order
                    product = exponents[exponent]
                values[x_value] = addition[addition_offset + product]
        total += values.count(0)
    minus_seven = (-7) % p
    splits = field.power(minus_seven, (q - 1) // 2) == 1
    metadata = {
        "field_order": q,
        "modulus_coefficients_ascending": list(field.modulus),
        "primitive_element_encoded": field.primitive_element,
    }
    return total, splits, metadata


def l_polynomial(p: int, normalization_counts: list[int]) -> tuple[list[int], list[int]]:
    power_sums = [p**degree + 1 - normalization_counts[degree - 1] for degree in (1, 2, 3)]
    s1, s2, s3 = power_sums
    e1 = s1
    numerator2 = e1 * s1 - s2
    require(numerator2 % 2 == 0, f"nonintegral second Newton coefficient at p={p}")
    e2 = numerator2 // 2
    numerator3 = s3 - e1 * s2 + e2 * s1
    require(numerator3 % 3 == 0, f"nonintegral third Newton coefficient at p={p}")
    e3 = numerator3 // 3
    coefficients = [1, -e1, e2, -e3, p * e2, p**2 * (-e1), p**3]
    return power_sums, coefficients


def fourth_power_sum(coefficients: list[int], first_three: list[int]) -> int:
    c1, c2, c3, c4 = coefficients[1:5]
    s1, s2, s3 = first_three
    return -(c1 * s3 + c2 * s2 + c3 * s1 + 4 * c4)


def predicted_normalization_counts(p: int, coefficients: list[int]) -> tuple[list[int], list[int]]:
    """Return Frobenius power sums and curve counts through r=6 by Newton."""
    power_sums: list[int] = []
    for degree in range(1, 7):
        convolution = sum(coefficients[index] * power_sums[degree - index - 1] for index in range(1, degree))
        power_sum = -(convolution + degree * coefficients[degree])
        power_sums.append(power_sum)
    counts = [p**degree + 1 - power_sums[degree - 1] for degree in range(1, 7)]
    return power_sums, counts


def frozen_model_checks(
    q6: sp.Expr,
    discriminant: sp.Expr,
    resultant_sigma: sp.Expr,
    p: int,
) -> tuple[bool, bool, bool, bool]:
    sigma = next(iter(q6.free_symbols))
    poly = sp.Poly(q6, sigma, modulus=p)
    squarefree = sp.gcd(poly, sp.diff(poly, sigma)).degree() == 0
    node_sigma = 9 * pow(4, p - 2, p) % p
    node_disjoint = int(poly.eval(node_sigma)) % p != 0
    singular_projection = sp.gcd(
        sp.Poly(discriminant, sigma, modulus=p),
        sp.Poly(resultant_sigma, sigma, modulus=p),
    ).monic()
    expected_node = sp.Poly((4 * sigma - 9) ** 2, sigma, modulus=p).monic()
    only_expected_affine_node = singular_projection == expected_node
    # The frozen blow-up charts use 2 and 3 as nonzero coefficients/units.
    infinity_blowup_coefficients_are_units = all(coefficient % p != 0 for coefficient in (2, 3))
    return squarefree, node_disjoint, only_expected_affine_node, infinity_blowup_coefficients_are_units


def check_target_prime(
    p: int,
    producer_row: dict[str, Any],
    q6: sp.Expr,
    discriminant: sp.Expr,
    resultant_sigma: sp.Expr,
) -> dict[str, Any]:
    affine_counts: list[int] = []
    node_splits: list[bool] = []
    normalization_counts: list[int] = []
    fields: list[dict[str, Any]] = []
    for degree in (1, 2, 3):
        affine, splits, metadata = affine_count(p, degree)
        normalized = affine + 7 + (1 if splits else -1)
        affine_counts.append(affine)
        node_splits.append(splits)
        normalization_counts.append(normalized)
        fields.append({"extension_degree": degree, **metadata})
    power_sums, coefficients = l_polynomial(p, normalization_counts)
    functional_equation = (
        coefficients[4] == p * coefficients[2]
        and coefficients[5] == p**2 * coefficients[1]
        and coefficients[6] == p**3
    )
    require(functional_equation, f"functional equation failed at p={p}")
    squarefree, node_disjoint, only_expected_node, infinity_units = frozen_model_checks(
        q6, discriminant, resultant_sigma, p
    )
    require(
        squarefree and node_disjoint and only_expected_node and infinity_units,
        f"independent frozen-model check failed at p={p}",
    )
    predicted_power_sums, predicted_counts = predicted_normalization_counts(p, coefficients)
    t_symbol = sp.symbols("T")
    l_poly = sp.Poly(sum(c * t_symbol**i for i, c in enumerate(coefficients)), t_symbol, domain=sp.ZZ)
    canonical_l_string = str(l_poly.as_expr())
    irreducible_over_q = bool(l_poly.is_irreducible)
    require(irreducible_over_q, f"independent L-polynomial irreducibility failed at p={p}")
    reciprocal_roots = [complex(root) for root in sp.nroots(l_poly.as_expr(), n=30, maxsteps=200)]
    recomputed_weil_error = max(abs(abs(root) - 1 / math.sqrt(p)) for root in reciprocal_roots)
    stored_weil_error = producer_row["maximum_reciprocal_root_modulus_error"]
    require(
        recomputed_weil_error <= 1e-10 and 0.0 <= stored_weil_error <= 1e-10,
        f"Weil-circle residual failed at p={p}",
    )

    comparisons = {
        "affine_counts_match": affine_counts == producer_row["affine_counts_r1_r3"],
        "node_splitting_matches": node_splits == producer_row["node_splits_r1_r3"],
        "normalization_counts_match": normalization_counts == producer_row["normalization_counts_r1_r3"],
        "power_sums_match": power_sums == producer_row["frobenius_power_sums_r1_r3"],
        "l_polynomial_coefficients_match": coefficients == producer_row["l_polynomial_coefficients_ascending"],
        "l_polynomial_string_matches": canonical_l_string == producer_row["l_polynomial"],
        "irreducible_over_q_matches": producer_row["irreducible_over_q"] is irreducible_over_q,
        "weil_residual_recomputed_and_bounded": recomputed_weil_error <= 1e-10 and stored_weil_error <= 1e-10,
        "predicted_counts_r1_r6_match": predicted_counts == producer_row["predicted_normalization_counts_r1_r6"],
        "exceptional_prime_list_matches": producer_row["frozen_model_screen"]["exceptional_primes_visible_in_branch_data"]
        == EXPECTED_BAD_PRIMES,
        "complete_good_reduction_theorem_not_claimed": not producer_row["frozen_model_screen"][
            "complete_good_reduction_theorem_claimed"
        ],
        "q6_squarefree_matches": producer_row["frozen_model_screen"]["q6_squarefree_mod_p"] == squarefree,
        "node_disjoint_matches": producer_row["frozen_model_screen"]["node_disjoint_from_q6"] == node_disjoint,
        "only_expected_affine_node_matches": producer_row["frozen_model_screen"]["only_expected_affine_node"]
        == only_expected_node,
        "infinity_blowup_units_match": producer_row["frozen_model_screen"]["infinity_blowup_coefficients_are_units"]
        == infinity_units,
    }
    require(all(comparisons.values()), f"producer mismatch at p={p}: {comparisons}")
    return {
        "prime": p,
        "fields": fields,
        "affine_counts_r1_r3": affine_counts,
        "node_splits_r1_r3": node_splits,
        "normalization_counts_r1_r3": normalization_counts,
        "frobenius_power_sums_r1_r3": power_sums,
        "predicted_frobenius_power_sums_r1_r6": predicted_power_sums,
        "predicted_normalization_counts_r1_r6": predicted_counts,
        "l_polynomial_coefficients_ascending": coefficients,
        "l_polynomial": canonical_l_string,
        "irreducible_over_q": irreducible_over_q,
        "stored_maximum_reciprocal_root_modulus_error": stored_weil_error,
        "recomputed_maximum_reciprocal_root_modulus_error": recomputed_weil_error,
        "functional_equation_symmetry": functional_equation,
        "frozen_model_screen": {
            "exceptional_primes_visible_in_branch_data": EXPECTED_BAD_PRIMES,
            "q6_squarefree_mod_p": squarefree,
            "node_disjoint_from_q6": node_disjoint,
            "only_expected_affine_node": only_expected_node,
            "infinity_blowup_coefficients_are_units": infinity_units,
            "complete_good_reduction_theorem_claimed": False,
        },
        "producer_comparisons": comparisons,
    }


def direct_p5_r4_check(p5_result: dict[str, Any]) -> dict[str, Any]:
    p = 5
    affine, splits, field_metadata = affine_count(p, 4)
    normalized = affine + 7 + (1 if splits else -1)
    coefficients = p5_result["l_polynomial_coefficients_ascending"]
    first_three = p5_result["frobenius_power_sums_r1_r3"]
    power_sum4 = fourth_power_sum(coefficients, first_three)
    predicted = p**4 + 1 - power_sum4
    require(normalized == predicted, f"direct p=5,r=4 count {normalized} != L-polynomial prediction {predicted}")
    return {
        "prime": p,
        "extension_degree": 4,
        "field": field_metadata,
        "affine_count": affine,
        "node_splits": splits,
        "normalization_count": normalized,
        "l_polynomial_predicted_power_sum": power_sum4,
        "l_polynomial_predicted_normalization_count": predicted,
        "matches_prediction": True,
    }


def validate_field_metadata(metadata: Any, p: int, degree: int, path: str) -> None:
    field = require_exact_keys(
        metadata,
        {"field_order", "modulus_coefficients_ascending", "primitive_element_encoded"},
        path,
    )
    require_type(field["field_order"], int, f"{path}.field_order")
    require(field["field_order"] == p**degree, f"{path}: field order mismatch")
    modulus = require_typed_list(
        field["modulus_coefficients_ascending"], int, degree + 1, f"{path}.modulus_coefficients_ascending"
    )
    require(modulus[-1] == 1, f"{path}: field modulus is not monic")
    require(is_irreducible(tuple(modulus), p), f"{path}: field modulus is reducible")
    require_type(field["primitive_element_encoded"], int, f"{path}.primitive_element_encoded")
    require(
        1 <= field["primitive_element_encoded"] < p**degree,
        f"{path}: primitive-element encoding out of range",
    )


def validate_independent_report(
    report: Any,
    certificate: dict[str, Any],
    certificate_bytes: bytes,
    expected_symbolic: dict[str, Any] | None = None,
) -> None:
    """Strictly validate the emitted independent artifact and its certificate link."""
    top = require_exact_keys(
        report,
        {
            "schema_version",
            "candidate_id",
            "all_checks_passed",
            "implementation",
            "source_certificate",
            "symbolic_checks",
            "frobenius_recomputations",
            "direct_p5_r4_check",
            "runtime_seconds",
        },
        "$report",
    )
    require_type(top["schema_version"], str, "$report.schema_version")
    require(top["schema_version"] == CHECK_SCHEMA, "independent-report schema version mismatch")
    require_type(top["candidate_id"], str, "$report.candidate_id")
    require(top["candidate_id"] == "HCS-C19", "independent-report candidate mismatch")
    require_type(top["all_checks_passed"], bool, "$report.all_checks_passed")
    require(top["all_checks_passed"], "independent report does not pass")
    require_type(top["runtime_seconds"], float, "$report.runtime_seconds")
    require(math.isfinite(top["runtime_seconds"]) and top["runtime_seconds"] >= 0.0, "invalid report runtime")

    implementation = require_exact_keys(
        top["implementation"],
        {"finite_field", "producer_imported", "galois_imported", "normalization_formula"},
        "$report.implementation",
    )
    require(
        implementation
        == {
            "finite_field": "self-contained Python polynomial-basis fields with independently selected irreducible moduli",
            "producer_imported": False,
            "galois_imported": False,
            "normalization_formula": "affine_count + 7 + (1 if node_splits else -1)",
        },
        "independent-report implementation declaration mismatch",
    )

    source = require_exact_keys(
        top["source_certificate"],
        {"path", "sha256", "schema_version", "schema_and_field_validation", "certificate_primes", "recomputed_primes"},
        "$report.source_certificate",
    )
    require_type(source["path"], str, "$report.source_certificate.path")
    require_type(source["sha256"], str, "$report.source_certificate.sha256")
    require(source["sha256"] == hashlib.sha256(certificate_bytes).hexdigest(), "report/certificate SHA-256 mismatch")
    require(source["schema_version"] == PRODUCER_SCHEMA, "report records wrong producer schema")
    require_type(source["schema_and_field_validation"], bool, "$report.source_certificate.schema_and_field_validation")
    require(source["schema_and_field_validation"], "report denies schema validation")
    require_typed_list(source["certificate_primes"], int, 3, "$report.source_certificate.certificate_primes")
    require_typed_list(source["recomputed_primes"], int, 3, "$report.source_certificate.recomputed_primes")
    require(source["certificate_primes"] == list(TARGET_PRIMES), "report certificate-prime order mismatch")
    require(source["recomputed_primes"] == list(TARGET_PRIMES), "report recomputed-prime mismatch")

    certificate_rows = validate_certificate_schema(certificate)
    if expected_symbolic is None:
        expected_symbolic = symbolic_checks(certificate)[3]
    require(top["symbolic_checks"] == expected_symbolic, "independent symbolic report content mismatch")

    require_typed_list(top["frobenius_recomputations"], dict, 3, "$report.frobenius_recomputations")
    report_rows: dict[int, dict[str, Any]] = {}
    row_keys = {
        "prime",
        "fields",
        "affine_counts_r1_r3",
        "node_splits_r1_r3",
        "normalization_counts_r1_r3",
        "frobenius_power_sums_r1_r3",
        "predicted_frobenius_power_sums_r1_r6",
        "predicted_normalization_counts_r1_r6",
        "l_polynomial_coefficients_ascending",
        "l_polynomial",
        "irreducible_over_q",
        "stored_maximum_reciprocal_root_modulus_error",
        "recomputed_maximum_reciprocal_root_modulus_error",
        "functional_equation_symmetry",
        "frozen_model_screen",
        "producer_comparisons",
    }
    comparison_keys = {
        "affine_counts_match",
        "node_splitting_matches",
        "normalization_counts_match",
        "power_sums_match",
        "l_polynomial_coefficients_match",
        "l_polynomial_string_matches",
        "irreducible_over_q_matches",
        "weil_residual_recomputed_and_bounded",
        "predicted_counts_r1_r6_match",
        "exceptional_prime_list_matches",
        "complete_good_reduction_theorem_not_claimed",
        "q6_squarefree_matches",
        "node_disjoint_matches",
        "only_expected_affine_node_matches",
        "infinity_blowup_units_match",
    }
    for index, raw_row in enumerate(top["frobenius_recomputations"]):
        path = f"$report.frobenius_recomputations[{index}]"
        row = require_exact_keys(raw_row, row_keys, path)
        require_type(row["prime"], int, f"{path}.prime")
        prime = row["prime"]
        require(prime in certificate_rows and prime not in report_rows, f"{path}: unexpected or duplicate prime")
        stored = certificate_rows[prime]
        require(row["affine_counts_r1_r3"] == stored["affine_counts_r1_r3"], f"{path}: affine counts mismatch")
        require(row["node_splits_r1_r3"] == stored["node_splits_r1_r3"], f"{path}: node splitting mismatch")
        require(row["normalization_counts_r1_r3"] == stored["normalization_counts_r1_r3"], f"{path}: normalization counts mismatch")
        require(row["frobenius_power_sums_r1_r3"] == stored["frobenius_power_sums_r1_r3"], f"{path}: power sums mismatch")
        require(row["predicted_normalization_counts_r1_r6"] == stored["predicted_normalization_counts_r1_r6"], f"{path}: predicted counts mismatch")
        coefficients = stored["l_polynomial_coefficients_ascending"]
        predicted_sums, predicted_counts = predicted_normalization_counts(prime, coefficients)
        require(row["predicted_frobenius_power_sums_r1_r6"] == predicted_sums, f"{path}: predicted power sums mismatch")
        require(row["predicted_normalization_counts_r1_r6"] == predicted_counts, f"{path}: Newton count reconstruction mismatch")
        require(row["l_polynomial_coefficients_ascending"] == coefficients, f"{path}: L coefficients mismatch")
        require(row["l_polynomial"] == stored["l_polynomial"], f"{path}: L string mismatch")
        require_type(row["irreducible_over_q"], bool, f"{path}.irreducible_over_q")
        require(row["irreducible_over_q"] and stored["irreducible_over_q"], f"{path}: L irreducibility assertion failed")
        for error_key in (
            "stored_maximum_reciprocal_root_modulus_error",
            "recomputed_maximum_reciprocal_root_modulus_error",
        ):
            require_type(row[error_key], float, f"{path}.{error_key}")
            require(0.0 <= row[error_key] <= 1e-10, f"{path}: invalid Weil residual")
        require(
            row["stored_maximum_reciprocal_root_modulus_error"]
            == stored["maximum_reciprocal_root_modulus_error"],
            f"{path}: stored Weil residual mismatch",
        )
        require_type(row["functional_equation_symmetry"], bool, f"{path}.functional_equation_symmetry")
        require(row["functional_equation_symmetry"], f"{path}: functional equation assertion is false")
        require(row["frozen_model_screen"] == stored["frozen_model_screen"], f"{path}: frozen-model screen mismatch")
        comparisons = require_exact_keys(row["producer_comparisons"], comparison_keys, f"{path}.producer_comparisons")
        require(all(type(value) is bool and value for value in comparisons.values()), f"{path}: producer comparison failed")
        require_typed_list(row["fields"], dict, 3, f"{path}.fields")
        for degree, field_entry in enumerate(row["fields"], start=1):
            entry = require_exact_keys(
                field_entry,
                {"extension_degree", "field_order", "modulus_coefficients_ascending", "primitive_element_encoded"},
                f"{path}.fields[{degree - 1}]",
            )
            require_type(entry["extension_degree"], int, f"{path}.fields[{degree - 1}].extension_degree")
            require(entry["extension_degree"] == degree, f"{path}: extension degree mismatch")
            validate_field_metadata(
                {key: value for key, value in entry.items() if key != "extension_degree"},
                prime,
                degree,
                f"{path}.fields[{degree - 1}]",
            )
        report_rows[prime] = row
    require(set(report_rows) == set(TARGET_PRIMES), "independent report is missing target primes")

    direct = require_exact_keys(
        top["direct_p5_r4_check"],
        {
            "prime",
            "extension_degree",
            "field",
            "affine_count",
            "node_splits",
            "normalization_count",
            "l_polynomial_predicted_power_sum",
            "l_polynomial_predicted_normalization_count",
            "matches_prediction",
        },
        "$report.direct_p5_r4_check",
    )
    expected_direct = {
        "prime": 5,
        "extension_degree": 4,
        "affine_count": 539,
        "node_splits": True,
        "normalization_count": 547,
        "l_polynomial_predicted_power_sum": 79,
        "l_polynomial_predicted_normalization_count": 547,
        "matches_prediction": True,
    }
    for key, value in expected_direct.items():
        require(direct[key] == value and type(direct[key]) is type(value), f"$report.direct_p5_r4_check.{key} mismatch")
    validate_field_metadata(direct["field"], 5, 4, "$report.direct_p5_r4_check.field")


def run(certificate_path: Path, output_path: Path) -> dict[str, Any]:
    started = time.perf_counter()
    raw_bytes = certificate_path.read_bytes()
    certificate = json.loads(raw_bytes)
    rows = validate_certificate_schema(certificate)
    q6, discriminant, resultant_sigma, symbolic = symbolic_checks(certificate)

    target_results = [
        check_target_prime(p, rows[p], q6, discriminant, resultant_sigma) for p in TARGET_PRIMES
    ]
    result_by_prime = {row["prime"]: row for row in target_results}
    direct_r4 = direct_p5_r4_check(result_by_prime[5])
    elapsed = time.perf_counter() - started
    payload = {
        "schema_version": CHECK_SCHEMA,
        "candidate_id": "HCS-C19",
        "all_checks_passed": True,
        "implementation": {
            "finite_field": "self-contained Python polynomial-basis fields with independently selected irreducible moduli",
            "producer_imported": False,
            "galois_imported": False,
            "normalization_formula": "affine_count + 7 + (1 if node_splits else -1)",
        },
        "source_certificate": {
            "path": str(certificate_path.resolve()),
            "sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "schema_version": certificate["schema_version"],
            "schema_and_field_validation": True,
            "certificate_primes": [row["prime"] for row in certificate["frobenius"]],
            "recomputed_primes": list(TARGET_PRIMES),
        },
        "symbolic_checks": symbolic,
        "frobenius_recomputations": target_results,
        "direct_p5_r4_check": direct_r4,
        "runtime_seconds": elapsed,
    }
    validate_independent_report(payload, certificate, raw_bytes, expected_symbolic=symbolic)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    return payload


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=project / "results" / "c19_certificate.json")
    parser.add_argument("--output", type=Path, default=project / "results" / "c19_independent_check.json")
    arguments = parser.parse_args()
    payload = run(arguments.certificate, arguments.output)
    print(json.dumps({"all_checks_passed": True, "output": str(arguments.output), "runtime_seconds": payload["runtime_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
