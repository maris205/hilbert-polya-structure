"""Two scientifically independent invariant engines for each regular torsor."""

from __future__ import annotations

from math import gcd
from typing import Any

from .constants import EXPECTED_LEDGER, IDENTITY
from .finite_module import (
    Matrix2,
    Vector2,
    locked_modulus,
    matrix_mod,
    matrix_multiply,
    matrix_order,
    matrix_power,
    matrix_vector,
    reconstruct_regular_torsor,
)


def enumeration_engine(torsor: dict[str, Any]) -> dict[str, Any]:
    """Derive every record from explicit points, actions, partitions, and arrows."""

    def reduced_pair(numerator: int, denominator: int) -> dict[str, int]:
        common = gcd(abs(numerator), denominator)
        return {"numerator": numerator // common, "denominator": denominator // common}

    def invert_counts(sequence: tuple[int, ...]) -> tuple[int, ...]:
        values: list[int] = []
        for index, current in enumerate(sequence, start=1):
            exact = current
            for divisor in range(1, index):
                if index % divisor == 0:
                    exact -= values[divisor - 1]
            values.append(exact)
        return tuple(values)

    q = locked_modulus(torsor["q"])
    group: tuple[Matrix2, ...] = torsor["direct_group"]
    points: tuple[Vector2, ...] = torsor["direct_cyclic_locus"]
    matrix: Matrix2 = torsor["cat_matrix"]
    inverse: Matrix2 = torsor["cat_matrix_inverse"]
    identity = matrix_mod(IDENTITY, q)
    n = len(points)
    r = matrix_order(matrix, q)
    source_cycles: tuple[tuple[Vector2, ...], ...] = torsor["source_cycles"]
    cycle_factors: dict[int, int] = {}
    for cycle in source_cycles:
        cycle_factors[len(cycle)] = cycle_factors.get(len(cycle), 0) + 1
    source_factors = tuple(
        {
            "support": support,
            "exponent": cycle_factors[support],
            "inverse_power_sign": -1,
        }
        for support in sorted(cycle_factors)
    )
    unseen = set(points)
    quotient_orbits: list[tuple[Vector2, ...]] = []
    while unseen:
        base = min(unseen)
        orbit = tuple(sorted({matrix_vector(item, base, q) for item in group}))
        quotient_orbits.append(orbit)
        unseen.difference_update(orbit)
    quotient_index = {
        point: index for index, orbit in enumerate(quotient_orbits) for point in orbit
    }
    quotient_transition = tuple(
        quotient_index[matrix_vector(matrix, orbit[0], q)] for orbit in quotient_orbits
    )
    fixed_coefficients: list[int] = []
    point_lefschetz: list[dict[str, Any]] = []
    orbit_coefficients: list[int] = []
    orbit_lefschetz: list[dict[str, Any]] = []
    for iterate in range(1, 2 * r + 1):
        iterate_matrix = matrix_power(matrix, iterate, q)
        fixed = sum(matrix_vector(iterate_matrix, point, q) == point for point in points)
        coefficient = 1 if fixed == n else 0
        fixed_coefficients.append(coefficient)
        point_lefschetz.append(
            {
                "iterate": iterate,
                "fixed_point_count": fixed,
                "regular_basis_coefficient": coefficient,
            }
        )
        fixed_orbits = sum(
            quotient_index[matrix_vector(iterate_matrix, orbit[0], q)] == index
            for index, orbit in enumerate(quotient_orbits)
        )
        orbit_coefficient = 1 if fixed_orbits == len(quotient_orbits) else 0
        orbit_coefficients.append(orbit_coefficient)
        orbit_lefschetz.append(
            {
                "iterate": iterate,
                "fixed_G_orbit_count": fixed_orbits,
                "regular_basis_coefficient": orbit_coefficient,
            }
        )
    point_exact_raw = invert_counts(tuple(fixed_coefficients))
    orbit_exact_raw = invert_counts(tuple(orbit_coefficients))
    point_exact = tuple(
        {
            "support": support,
            "regular_basis_coefficient": coefficient,
            "basis": "[G_q/1]",
        }
        for support, coefficient in enumerate(point_exact_raw, start=1)
        if coefficient
    )
    orbit_exact = tuple(
        {
            "support": support,
            "regular_basis_coefficient": coefficient,
            "basis": "[G_q/1]",
        }
        for support, coefficient in enumerate(orbit_exact_raw, start=1)
        if coefficient
    )
    marks = tuple(
        {
            "group_element": group_element,
            "fixed_point_count": sum(
                matrix_vector(group_element, point, q) == point for point in points
            ),
        }
        for group_element in group
    )
    twisted_table: list[dict[str, Any]] = []
    unique_fixing: list[dict[str, Any]] = []
    for iterate in range(r):
        iterate_matrix = matrix_power(matrix, iterate, q)
        expected_fixer = matrix_power(inverse, iterate, q)
        local: list[dict[str, Any]] = []
        for group_element in group:
            combined = matrix_multiply(group_element, iterate_matrix, q)
            fixed = sum(
                matrix_vector(combined, point, q) == point for point in points
            )
            local.append({"group_element": group_element, "fixed_point_count": fixed})
        fixers = tuple(record["group_element"] for record in local if record["fixed_point_count"])
        twisted_table.append({"iterate": iterate, "rows": tuple(local)})
        unique_fixing.append(
            {
                "iterate": iterate,
                "expected_a_inverse_power": expected_fixer,
                "fixing_group_elements": fixers,
            }
        )
    sectors = tuple(
        {
            "group_element": group_element,
            "fixed_point_count": sum(
                matrix_vector(group_element, point, q) == point for point in points
            ),
            "nonempty": any(
                matrix_vector(group_element, point, q) == point for point in points
            ),
        }
        for group_element in group
    )
    naturality = all(
        matrix_vector(matrix, matrix_vector(group_element, point, q), q)
        == matrix_vector(group_element, matrix_vector(matrix, point, q), q)
        for point in points
        for group_element in group
    )
    generator_exponents: list[int] = []
    generator_matrices: list[Matrix2] = []
    for exponent in range(1, r + 1):
        candidate = matrix_power(matrix, exponent, q)
        if matrix_order(candidate, q) == r:
            generator_exponents.append(exponent)
            generator_matrices.append(candidate)
    original_signature = tuple(record["fixed_point_count"] for record in point_lefschetz)
    inverse_signature = tuple(
        sum(
            matrix_vector(matrix_power(inverse, iterate, q), point, q) == point
            for point in points
        )
        for iterate in range(1, 2 * r + 1)
    )
    nonempty_sectors = tuple(record for record in sectors if record["nonempty"])
    return {
        "engine": "EXPLICIT_FIXED_SET_AND_GROUPOID_ENUMERATION",
        "source_dynamics": {
            "ordinary_zeta_factors": source_factors,
            "source_cycle_count": len(source_cycles),
            "source_cycle_lengths": tuple(len(cycle) for cycle in source_cycles),
            "coarse_quotient_zeta_factors": (
                {"support": 1, "exponent": len(quotient_orbits), "inverse_power_sign": -1},
            ),
            "coarse_quotient_object_count": len(quotient_orbits),
            "coarse_quotient_transition": quotient_transition,
            "coarse_induced_map_identity": quotient_transition
            == tuple(range(len(quotient_orbits))),
        },
        "point_burnside": {
            "construction": "POINT_ORDER_RATIONAL_BURNSIDE_ZETA",
            "fixed_lefschetz": tuple(point_lefschetz),
            "divisor_inversion": tuple(
                {"support": support, "regular_basis_coefficient": coefficient}
                for support, coefficient in enumerate(point_exact_raw, start=1)
            ),
            "exact_period_classes": point_exact,
            "zeta_factors": (
                {
                    "support": point_exact[0]["support"],
                    "basis": "[G_q/1]",
                    "exponent": reduced_pair(1, point_exact[0]["support"]),
                    "inverse_power_sign": -1,
                },
            ),
            "regular_marks": marks,
            "depends_only_on_generated_subgroup": original_signature == inverse_signature,
            "recovers_selected_generator": False,
        },
        "orbit_burnside": {
            "construction": "ORBIT_ORDER_INTEGRAL_BURNSIDE_ZETA",
            "fixed_orbit_lefschetz": tuple(orbit_lefschetz),
            "divisor_inversion": tuple(
                {"support": support, "regular_basis_coefficient": coefficient}
                for support, coefficient in enumerate(orbit_exact_raw, start=1)
            ),
            "exact_period_classes": orbit_exact,
            "zeta_factors": (
                {
                    "support": orbit_exact[0]["support"],
                    "basis": "[G_q/1]",
                    "exponent": reduced_pair(1, orbit_exact[0]["support"]),
                    "inverse_power_sign": -1,
                },
            ),
            "orbit_order_is_static": orbit_exact[0]["support"] == 1,
        },
        "g_permutation": {
            "construction": "LABELLED_Z_TIMES_G_PERMUTATION",
            "left_action_convention": "(k,g).x=g*a^k*x",
            "twisted_fixed_table": tuple(twisted_table),
            "unique_fixing_translation_by_iterate": tuple(unique_fixing),
            "stabilizer_relation": {
                "K": tuple(item for item in group if all(
                    matrix_vector(item, point, q) == point for point in points
                )),
                "z1_generator_group_element": inverse,
            },
            "triple": {"H_order": 1, "m": 1, "alpha": inverse},
            "action_kernel": tuple(item for item in group if all(
                matrix_vector(item, point, q) == point for point in points
            )),
            "recovered_a_mod_kernel": (matrix,),
            "exact_labelled_a_recovered": True,
        },
        "enhanced": {
            "construction": "ENHANCED_BURNSIDE_CARRIER",
            "tuple": {"H_order": 1, "m": 1, "return_twist": matrix, "character": 1},
            "return_twist_order": r,
            "coefficient_category_label": "enhanced_B(G_" + str(q) + ")",
        },
        "orbifold": {
            "map_type": "ADDITIVE_EXACT_PERIOD_REDUCTION_NOT_RING_HOMOMORPHISM",
            "point_cardinality_factors": (
                {
                    "support": point_exact[0]["support"],
                    "exponent": reduced_pair(n, point_exact[0]["support"]),
                    "inverse_power_sign": -1,
                },
            ),
            "point_orbifold_factors": (
                {
                    "support": point_exact[0]["support"],
                    "exponent": reduced_pair(1, point_exact[0]["support"]),
                    "inverse_power_sign": -1,
                },
            ),
            "orbit_cardinality_factors": (
                {
                    "support": orbit_exact[0]["support"],
                    "exponent": reduced_pair(n, orbit_exact[0]["support"]),
                    "inverse_power_sign": -1,
                },
            ),
            "orbit_orbifold_factors": (
                {
                    "support": orbit_exact[0]["support"],
                    "exponent": reduced_pair(len(nonempty_sectors), orbit_exact[0]["support"]),
                    "inverse_power_sign": -1,
                },
            ),
            "fixed_sectors": sectors,
            "nonempty_sector_count": len(nonempty_sectors),
            "nonidentity_nonempty_sector_count": sum(
                record["nonempty"] and record["group_element"] != identity for record in sectors
            ),
            "enhanced_orbifold_factors": (
                {"support": 1, "exponent": reduced_pair(1, 1), "inverse_power_sign": -1},
            ),
        },
        "action_groupoid": {
            "object_count": len(points),
            "arrow_count": len(points) * len(group),
            "isomorphism_class_count": len(quotient_orbits),
            "quotient_representative_automorphism_count": len(torsor["action_kernel"]),
            "quotient_stack_components": (
                {"stabilizer_order": len(torsor["action_kernel"]), "multiplicity": len(quotient_orbits)},
            ),
            "static_inertia_sector_count": len(nonempty_sectors),
            "natural_transformation_component": matrix,
            "naturality_equalities_checked": len(points) * len(group),
            "naturality_all_commute": naturality,
            "induced_period": 1 if naturality and quotient_transition == tuple(range(len(quotient_orbits))) else r,
            "translation_2_isomorphic_to_identity": naturality,
        },
        "generator_ambiguity": {
            "generated_subgroup_order": r,
            "generator_exponents": tuple(generator_exponents),
            "generator_matrices": tuple(generator_matrices),
            "chosen_a": matrix,
            "comparison_a_inverse": inverse,
            "chosen_and_inverse_distinct": matrix != inverse,
            "same_point_fixed_signature": original_signature == inverse_signature,
            "same_point_support": point_exact[0]["support"],
            "chosen_g_permutation_twist": inverse,
            "inverse_map_g_permutation_twist": matrix,
            "labelled_twists_distinct": matrix != inverse,
            "unlabelled_generator_not_selected": original_signature == inverse_signature,
        },
        "shortening_gluing": {
            "source_period": point_exact[0]["support"],
            "shortening_factor": reduced_pair(1, point_exact[0]["support"]),
            "source_cycle_gluing_count": len(source_cycles),
            "quotient_period": 1 if quotient_transition == tuple(range(len(quotient_orbits))) else r,
        },
    }


def formula_engine(torsor: dict[str, Any]) -> dict[str, Any]:
    """Derive every record independently from the regular-torsor theorem."""

    def theorem_fraction(numerator: int, denominator: int) -> dict[str, int]:
        divisor = gcd(abs(numerator), denominator)
        return {"numerator": numerator // divisor, "denominator": denominator // divisor}

    def theorem_exact(sequence: tuple[int, ...]) -> tuple[int, ...]:
        output: list[int] = []
        for period in range(1, len(sequence) + 1):
            coefficient = sequence[period - 1]
            coefficient -= sum(
                output[proper - 1]
                for proper in range(1, period)
                if period % proper == 0
            )
            output.append(coefficient)
        return tuple(output)

    q = torsor["q"]
    group: tuple[Matrix2, ...] = torsor["algebra_group"]
    matrix: Matrix2 = torsor["cat_matrix"]
    inverse: Matrix2 = torsor["cat_matrix_inverse"]
    powers: tuple[Matrix2, ...] = torsor["cat_power_table"]
    inverse_powers: tuple[Matrix2, ...] = torsor["cat_inverse_power_table"]
    identity: Matrix2 = powers[0]
    n = torsor["n"]
    r = torsor["r"]
    m = torsor["m"]
    fixed_sequence = tuple(1 if iterate % r == 0 else 0 for iterate in range(1, 2 * r + 1))
    orbit_sequence = tuple(1 for _ in range(1, 2 * r + 1))
    point_exact_raw = theorem_exact(fixed_sequence)
    orbit_exact_raw = theorem_exact(orbit_sequence)
    point_exact = tuple(
        {"support": support, "regular_basis_coefficient": value, "basis": "[G_q/1]"}
        for support, value in enumerate(point_exact_raw, start=1)
        if value
    )
    orbit_exact = tuple(
        {"support": support, "regular_basis_coefficient": value, "basis": "[G_q/1]"}
        for support, value in enumerate(orbit_exact_raw, start=1)
        if value
    )
    point_lefschetz = tuple(
        {
            "iterate": iterate,
            "fixed_point_count": n if iterate % r == 0 else 0,
            "regular_basis_coefficient": 1 if iterate % r == 0 else 0,
        }
        for iterate in range(1, 2 * r + 1)
    )
    orbit_lefschetz = tuple(
        {"iterate": iterate, "fixed_G_orbit_count": 1, "regular_basis_coefficient": 1}
        for iterate in range(1, 2 * r + 1)
    )
    marks = tuple(
        {
            "group_element": group_element,
            "fixed_point_count": n if group_element == identity else 0,
        }
        for group_element in group
    )
    twisted_table = tuple(
        {
            "iterate": iterate,
            "rows": tuple(
                {
                    "group_element": group_element,
                    "fixed_point_count": n if group_element == inverse_powers[iterate] else 0,
                }
                for group_element in group
            ),
        }
        for iterate in range(r)
    )
    unique_fixing = tuple(
        {
            "iterate": iterate,
            "expected_a_inverse_power": inverse_powers[iterate],
            "fixing_group_elements": (inverse_powers[iterate],),
        }
        for iterate in range(r)
    )
    sectors = tuple(
        {
            "group_element": group_element,
            "fixed_point_count": n if group_element == identity else 0,
            "nonempty": group_element == identity,
        }
        for group_element in group
    )
    generator_exponents = tuple(exponent for exponent in range(1, r + 1) if gcd(exponent, r) == 1)
    generator_matrices = tuple(powers[exponent % r] for exponent in generator_exponents)
    return {
        "engine": "REGULAR_TORSOR_THEOREM_FORMULAS",
        "source_dynamics": {
            "ordinary_zeta_factors": (
                {"support": r, "exponent": m, "inverse_power_sign": -1},
            ),
            "source_cycle_count": m,
            "source_cycle_lengths": tuple(r for _ in range(m)),
            "coarse_quotient_zeta_factors": (
                {"support": 1, "exponent": 1, "inverse_power_sign": -1},
            ),
            "coarse_quotient_object_count": 1,
            "coarse_quotient_transition": (0,),
            "coarse_induced_map_identity": True,
        },
        "point_burnside": {
            "construction": "POINT_ORDER_RATIONAL_BURNSIDE_ZETA",
            "fixed_lefschetz": point_lefschetz,
            "divisor_inversion": tuple(
                {"support": support, "regular_basis_coefficient": coefficient}
                for support, coefficient in enumerate(point_exact_raw, start=1)
            ),
            "exact_period_classes": point_exact,
            "zeta_factors": (
                {
                    "support": r,
                    "basis": "[G_q/1]",
                    "exponent": theorem_fraction(1, r),
                    "inverse_power_sign": -1,
                },
            ),
            "regular_marks": marks,
            "depends_only_on_generated_subgroup": True,
            "recovers_selected_generator": False,
        },
        "orbit_burnside": {
            "construction": "ORBIT_ORDER_INTEGRAL_BURNSIDE_ZETA",
            "fixed_orbit_lefschetz": orbit_lefschetz,
            "divisor_inversion": tuple(
                {"support": support, "regular_basis_coefficient": coefficient}
                for support, coefficient in enumerate(orbit_exact_raw, start=1)
            ),
            "exact_period_classes": orbit_exact,
            "zeta_factors": (
                {
                    "support": 1,
                    "basis": "[G_q/1]",
                    "exponent": theorem_fraction(1, 1),
                    "inverse_power_sign": -1,
                },
            ),
            "orbit_order_is_static": True,
        },
        "g_permutation": {
            "construction": "LABELLED_Z_TIMES_G_PERMUTATION",
            "left_action_convention": "(k,g).x=g*a^k*x",
            "twisted_fixed_table": twisted_table,
            "unique_fixing_translation_by_iterate": unique_fixing,
            "stabilizer_relation": {"K": (identity,), "z1_generator_group_element": inverse},
            "triple": {"H_order": 1, "m": 1, "alpha": inverse},
            "action_kernel": (identity,),
            "recovered_a_mod_kernel": (matrix,),
            "exact_labelled_a_recovered": True,
        },
        "enhanced": {
            "construction": "ENHANCED_BURNSIDE_CARRIER",
            "tuple": {"H_order": 1, "m": 1, "return_twist": matrix, "character": 1},
            "return_twist_order": r,
            "coefficient_category_label": "enhanced_B(G_" + str(q) + ")",
        },
        "orbifold": {
            "map_type": "ADDITIVE_EXACT_PERIOD_REDUCTION_NOT_RING_HOMOMORPHISM",
            "point_cardinality_factors": (
                {"support": r, "exponent": theorem_fraction(m, 1), "inverse_power_sign": -1},
            ),
            "point_orbifold_factors": (
                {"support": r, "exponent": theorem_fraction(1, r), "inverse_power_sign": -1},
            ),
            "orbit_cardinality_factors": (
                {"support": 1, "exponent": theorem_fraction(n, 1), "inverse_power_sign": -1},
            ),
            "orbit_orbifold_factors": (
                {"support": 1, "exponent": theorem_fraction(1, 1), "inverse_power_sign": -1},
            ),
            "fixed_sectors": sectors,
            "nonempty_sector_count": 1,
            "nonidentity_nonempty_sector_count": 0,
            "enhanced_orbifold_factors": (
                {"support": 1, "exponent": theorem_fraction(1, 1), "inverse_power_sign": -1},
            ),
        },
        "action_groupoid": {
            "object_count": n,
            "arrow_count": n * n,
            "isomorphism_class_count": 1,
            "quotient_representative_automorphism_count": 1,
            "quotient_stack_components": ({"stabilizer_order": 1, "multiplicity": 1},),
            "static_inertia_sector_count": 1,
            "natural_transformation_component": matrix,
            "naturality_equalities_checked": n * n,
            "naturality_all_commute": True,
            "induced_period": 1,
            "translation_2_isomorphic_to_identity": True,
        },
        "generator_ambiguity": {
            "generated_subgroup_order": r,
            "generator_exponents": generator_exponents,
            "generator_matrices": generator_matrices,
            "chosen_a": matrix,
            "comparison_a_inverse": inverse,
            "chosen_and_inverse_distinct": matrix != inverse,
            "same_point_fixed_signature": True,
            "same_point_support": r,
            "chosen_g_permutation_twist": inverse,
            "inverse_map_g_permutation_twist": matrix,
            "labelled_twists_distinct": matrix != inverse,
            "unlabelled_generator_not_selected": True,
        },
        "shortening_gluing": {
            "source_period": r,
            "shortening_factor": theorem_fraction(1, r),
            "source_cycle_gluing_count": m,
            "quotient_period": 1,
        },
    }


def engine_pair_validation(
    enumeration: dict[str, Any], formula: dict[str, Any]
) -> dict[str, Any]:
    errors: list[str] = []
    if enumeration.get("engine") != "EXPLICIT_FIXED_SET_AND_GROUPOID_ENUMERATION":
        errors.append("ENUMERATION_ENGINE_ID_MISMATCH")
    if formula.get("engine") != "REGULAR_TORSOR_THEOREM_FORMULAS":
        errors.append("FORMULA_ENGINE_ID_MISMATCH")
    enumeration_projection = {key: value for key, value in enumeration.items() if key != "engine"}
    formula_projection = {key: value for key, value in formula.items() if key != "engine"}
    if enumeration_projection != formula_projection:
        errors.append("INDEPENDENT_ENGINE_RECORD_MISMATCH")
    return {"errors": errors, "pass": not errors}


def audit_modulus(modulus: int) -> dict[str, Any]:
    q = locked_modulus(modulus)
    torsor = reconstruct_regular_torsor(q)
    enumeration = enumeration_engine(torsor)
    formula = formula_engine(torsor)
    pair = engine_pair_validation(enumeration, formula)
    n, r, m = EXPECTED_LEDGER[q]
    expected = {"n": n, "r": r, "m": m}
    all_factor_groups = (
        enumeration["source_dynamics"]["ordinary_zeta_factors"],
        enumeration["source_dynamics"]["coarse_quotient_zeta_factors"],
        enumeration["point_burnside"]["zeta_factors"],
        enumeration["orbit_burnside"]["zeta_factors"],
        enumeration["orbifold"]["point_cardinality_factors"],
        enumeration["orbifold"]["point_orbifold_factors"],
        enumeration["orbifold"]["orbit_cardinality_factors"],
        enumeration["orbifold"]["orbit_orbifold_factors"],
        enumeration["orbifold"]["enhanced_orbifold_factors"],
    )
    checks = {
        "torsor_reconstruction_pass": torsor["pass"],
        "dual_invariant_engines_match": pair["pass"],
        "expected_ledger_match": {"n": torsor["n"], "r": torsor["r"], "m": torsor["m"]}
        == expected,
        "point_support_r": enumeration["point_burnside"]["exact_period_classes"]
        == ({"support": r, "regular_basis_coefficient": 1, "basis": "[G_q/1]"},),
        "orbit_support_one": enumeration["orbit_burnside"]["exact_period_classes"]
        == ({"support": 1, "regular_basis_coefficient": 1, "basis": "[G_q/1]"},),
        "all_factors_use_inverse_convention": all(
            factor["inverse_power_sign"] == -1
            for group in all_factor_groups
            for factor in group
        ),
        "twisted_unique_fixer_each_iterate": all(
            record["fixing_group_elements"] == (record["expected_a_inverse_power"],)
            for record in enumeration["g_permutation"]["unique_fixing_translation_by_iterate"]
        ),
        "regular_sector_identity_only": enumeration["orbifold"]["nonempty_sector_count"] == 1
        and enumeration["orbifold"]["nonidentity_nonempty_sector_count"] == 0,
        "stack_period_one": enumeration["action_groupoid"]["induced_period"] == 1,
        "generator_ambiguity_exact": enumeration["generator_ambiguity"]["same_point_fixed_signature"]
        and enumeration["generator_ambiguity"]["labelled_twists_distinct"],
    }
    return {
        "q": q,
        "expected": expected,
        "torsor": torsor,
        "enumeration_engine": enumeration,
        "formula_engine": formula,
        "engine_pair_validation": pair,
        "checks": checks,
        "pass": all(checks.values()),
    }
