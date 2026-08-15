"""Dual exact engines for finite cyclic-group C-set decompositions."""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Any

from .constants import STRUCTURAL_CONTROL


OrbitTypes = tuple[tuple[int, int], ...]


def rational_record(numerator: int, denominator: int) -> dict[str, int]:
    value = Fraction(numerator, denominator)
    return {"numerator": value.numerator, "denominator": value.denominator}


def _validate_input(order: int, orbit_types: OrbitTypes, element: int) -> None:
    if type(order) is not int or order < 1:
        raise ValueError("cyclic group order must be positive")
    if type(element) is not int or not 0 <= element < order:
        raise ValueError("distinguished element must be a canonical residue")
    if type(orbit_types) is not tuple or not orbit_types:
        raise ValueError("at least one orbit type is required")
    seen: set[int] = set()
    for subgroup_order, multiplicity in orbit_types:
        if (
            type(subgroup_order) is not int
            or type(multiplicity) is not int
            or subgroup_order < 1
            or order % subgroup_order
            or multiplicity < 1
            or subgroup_order in seen
        ):
            raise ValueError("orbit types must be unique positive subgroup divisors")
        seen.add(subgroup_order)


def _subgroup_elements(order: int, subgroup_order: int) -> tuple[int, ...]:
    step = order // subgroup_order
    return tuple(index * step for index in range(subgroup_order))


def _aggregate_integer(records: list[tuple[int, int]]) -> tuple[dict[str, int], ...]:
    totals: dict[int, int] = {}
    for support, exponent in records:
        totals[support] = totals.get(support, 0) + exponent
    return tuple(
        {"support": support, "exponent": totals[support]} for support in sorted(totals)
    )


def _aggregate_rational(
    records: list[tuple[int, Fraction]],
) -> tuple[dict[str, Any], ...]:
    totals: dict[int, Fraction] = {}
    for support, exponent in records:
        totals[support] = totals.get(support, Fraction(0, 1)) + exponent
    return tuple(
        {"support": support, "exponent": rational_record(totals[support].numerator, totals[support].denominator)}
        for support in sorted(totals)
    )


def _invert_basis_sequence(
    sequence: tuple[dict[int, int], ...]
) -> tuple[dict[int, int], ...]:
    exact: list[dict[int, int]] = []
    for index, current in enumerate(sequence, start=1):
        value = dict(current)
        for divisor in range(1, index):
            if index % divisor == 0:
                for key, coefficient in exact[divisor - 1].items():
                    value[key] = value.get(key, 0) - coefficient
        exact.append({key: coefficient for key, coefficient in value.items() if coefficient})
    return tuple(exact)


def formula_cyclic_cset(
    order: int, orbit_types: OrbitTypes, element: int
) -> dict[str, Any]:
    """Compute the theorem ledger directly from subgroup-index formulas."""

    _validate_input(order, orbit_types, element)
    h_order = order // gcd(order, element)
    kernel_order = 0
    orbit_records: list[dict[str, Any]] = []
    source_terms: list[tuple[int, int]] = []
    point_orbifold_terms: list[tuple[int, Fraction]] = []
    basis_by_support: dict[int, list[dict[str, int]]] = {}
    point_count = 0
    inertia_count = 0
    for subgroup_order, multiplicity in orbit_types:
        intersection_order = gcd(h_order, subgroup_order)
        period = h_order // intersection_order
        hk_order = h_order * subgroup_order // intersection_order
        cycles_per_orbit = order // hk_order
        point_count += multiplicity * (order // subgroup_order)
        inertia_count += multiplicity * subgroup_order
        kernel_order = subgroup_order if kernel_order == 0 else gcd(kernel_order, subgroup_order)
        source_terms.append((period, multiplicity * cycles_per_orbit))
        point_orbifold_terms.append(
            (period, Fraction(multiplicity * subgroup_order, period))
        )
        basis = {"subgroup_order": subgroup_order, "coefficient": multiplicity}
        basis_by_support.setdefault(period, []).append(basis)
        k_elements = _subgroup_elements(order, subgroup_order)
        orbit_records.append(
            {
                "subgroup_order": subgroup_order,
                "multiplicity": multiplicity,
                "H_intersection_order": intersection_order,
                "period_d_K": period,
                "cycle_count_per_orbit_M_K": cycles_per_orbit,
                "subgroup_elements": k_elements,
                "z1_stabilizer_group_elements": tuple(
                    sorted({(value - element) % order for value in k_elements})
                ),
            }
        )
    kernel_elements = _subgroup_elements(order, kernel_order)
    recovered_coset = tuple(sorted({(element + value) % order for value in kernel_elements}))
    point_classes = tuple(
        {"support": support, "basis": tuple(sorted(basis_by_support[support], key=lambda item: item["subgroup_order"]))}
        for support in sorted(basis_by_support)
    )
    orbit_basis = tuple(
        {"subgroup_order": subgroup_order, "coefficient": multiplicity}
        for subgroup_order, multiplicity in orbit_types
    )
    max_k = 2 * h_order
    point_lefschetz: list[dict[str, Any]] = []
    orbit_lefschetz: list[dict[str, Any]] = []
    for iterate in range(1, max_k + 1):
        point_basis = tuple(
            {"subgroup_order": record["subgroup_order"], "coefficient": record["multiplicity"]}
            for record in orbit_records
            if iterate % record["period_d_K"] == 0
        )
        point_lefschetz.append({"iterate": iterate, "basis": point_basis})
        orbit_lefschetz.append({"iterate": iterate, "basis": orbit_basis})
    return {
        "engine": "CYCLIC_SUBGROUP_INDEX_FORMULAS",
        "ambient_group_order": order,
        "distinguished_element": element,
        "generated_subgroup_order": h_order,
        "orbit_types": orbit_records,
        "point_count": point_count,
        "source_factors": _aggregate_integer(source_terms),
        "coarse_quotient_factors": ({"support": 1, "exponent": sum(item[1] for item in orbit_types)},),
        "point_lefschetz": tuple(point_lefschetz),
        "point_exact_classes": point_classes,
        "orbit_lefschetz": tuple(orbit_lefschetz),
        "orbit_exact_classes": ({"support": 1, "basis": orbit_basis},),
        "point_orbifold_factors": _aggregate_rational(point_orbifold_terms),
        "orbit_orbifold_factors": ({"support": 1, "exponent": inertia_count},),
        "action_kernel_elements": kernel_elements,
        "action_kernel_order": kernel_order,
        "action_effective": kernel_order == 1,
        "g_permutation_recovered_a_coset": recovered_coset,
        "g_permutation_exact_label_recovery": kernel_order == 1,
        "stack_components": tuple(
            {"subgroup_order": subgroup_order, "multiplicity": multiplicity}
            for subgroup_order, multiplicity in orbit_types
        ),
        "static_inertia_sector_count": inertia_count,
        "stack_dynamics_static": True,
        "naturality_equalities_checked": point_count * order,
    }


def enumeration_cyclic_cset(
    order: int, orbit_types: OrbitTypes, element: int
) -> dict[str, Any]:
    """Compute the same ledger by explicit points, actions, cycles, and fixed sets."""

    _validate_input(order, orbit_types, element)
    points: list[tuple[int, int, int]] = []
    points_by_type: dict[int, tuple[tuple[int, int, int], ...]] = {}
    orbit_records: list[dict[str, Any]] = []
    for type_index, (subgroup_order, multiplicity) in enumerate(orbit_types):
        step = order // subgroup_order
        local: list[tuple[int, int, int]] = []
        for copy_index in range(multiplicity):
            for coset in range(step):
                point = (type_index, copy_index, coset)
                points.append(point)
                local.append(point)
        points_by_type[type_index] = tuple(local)

    def act(group_element: int, point: tuple[int, int, int]) -> tuple[int, int, int]:
        type_index, copy_index, coset = point
        subgroup_order = orbit_types[type_index][0]
        step = order // subgroup_order
        return (type_index, copy_index, (coset + group_element) % step)

    unseen = set(points)
    cycles: list[tuple[tuple[int, int, int], ...]] = []
    while unseen:
        start = min(unseen)
        current = start
        cycle: list[tuple[int, int, int]] = []
        while current not in cycle:
            cycle.append(current)
            current = act(element, current)
        if current != start:
            raise RuntimeError("explicit cyclic C-set orbit failed to close")
        cycles.append(tuple(cycle))
        unseen.difference_update(cycle)
    source_terms = _aggregate_integer([(len(cycle), 1) for cycle in cycles])
    kernel_elements = tuple(
        group_element
        for group_element in range(order)
        if all(act(group_element, point) == point for point in points)
    )
    h_order = 1
    current = element % order
    while current:
        h_order += 1
        current = (current + element) % order
    max_k = 2 * h_order
    point_sequence: list[dict[int, int]] = []
    orbit_sequence: list[dict[int, int]] = []
    point_lefschetz: list[dict[str, Any]] = []
    orbit_lefschetz: list[dict[str, Any]] = []
    for iterate in range(1, max_k + 1):
        point_basis: dict[int, int] = {}
        orbit_basis: dict[int, int] = {}
        for type_index, (subgroup_order, multiplicity) in enumerate(orbit_types):
            local = points_by_type[type_index]
            fixed_all = all(act(iterate * element, point) == point for point in local)
            if fixed_all:
                point_basis[subgroup_order] = multiplicity
            orbit_basis[subgroup_order] = multiplicity
        point_sequence.append(point_basis)
        orbit_sequence.append(orbit_basis)
        point_lefschetz.append(
            {
                "iterate": iterate,
                "basis": tuple(
                    {"subgroup_order": key, "coefficient": point_basis[key]}
                    for key in sorted(point_basis)
                ),
            }
        )
        orbit_lefschetz.append(
            {
                "iterate": iterate,
                "basis": tuple(
                    {"subgroup_order": key, "coefficient": orbit_basis[key]}
                    for key in sorted(orbit_basis)
                ),
            }
        )
    point_exact_raw = _invert_basis_sequence(tuple(point_sequence))
    orbit_exact_raw = _invert_basis_sequence(tuple(orbit_sequence))
    point_exact = tuple(
        {
            "support": support,
            "basis": tuple(
                {"subgroup_order": key, "coefficient": values[key]}
                for key in sorted(values)
            ),
        }
        for support, values in enumerate(point_exact_raw, start=1)
        if values
    )
    orbit_exact = tuple(
        {
            "support": support,
            "basis": tuple(
                {"subgroup_order": key, "coefficient": values[key]}
                for key in sorted(values)
            ),
        }
        for support, values in enumerate(orbit_exact_raw, start=1)
        if values
    )
    point_orbifold_terms: list[tuple[int, Fraction]] = []
    for record in point_exact:
        for basis in record["basis"]:
            point_orbifold_terms.append(
                (
                    record["support"],
                    Fraction(
                        basis["coefficient"] * basis["subgroup_order"],
                        record["support"],
                    ),
                )
            )
    representatives = tuple(
        (type_index, copy_index, 0)
        for type_index, (_, multiplicity) in enumerate(orbit_types)
        for copy_index in range(multiplicity)
    )
    inertia_count = sum(
        sum(act(group_element, point) == point for group_element in range(order))
        for point in representatives
    )
    z1_elements = tuple(
        group_element
        for group_element in range(order)
        if all(act((group_element + element) % order, point) == point for point in points)
    )
    recovered_coset = tuple(sorted({(-value) % order for value in z1_elements}))
    naturality = all(
        act(element, act(group_element, point))
        == act(group_element, act(element, point))
        for point in points
        for group_element in range(order)
    )
    for type_index, (subgroup_order, multiplicity) in enumerate(orbit_types):
        local_cycles = [cycle for cycle in cycles if cycle[0][0] == type_index]
        period = len(local_cycles[0])
        cycles_per_orbit = len(local_cycles) // multiplicity
        k_elements = tuple(
            group_element
            for group_element in range(order)
            if act(group_element, points_by_type[type_index][0]) == points_by_type[type_index][0]
        )
        orbit_records.append(
            {
                "subgroup_order": subgroup_order,
                "multiplicity": multiplicity,
                "H_intersection_order": h_order // period,
                "period_d_K": period,
                "cycle_count_per_orbit_M_K": cycles_per_orbit,
                "subgroup_elements": k_elements,
                "z1_stabilizer_group_elements": tuple(
                    group_element
                    for group_element in range(order)
                    if act((group_element + element) % order, points_by_type[type_index][0])
                    == points_by_type[type_index][0]
                ),
            }
        )
    return {
        "engine": "EXPLICIT_CYCLIC_CSET_ENUMERATION",
        "ambient_group_order": order,
        "distinguished_element": element,
        "generated_subgroup_order": h_order,
        "orbit_types": orbit_records,
        "point_count": len(points),
        "source_factors": source_terms,
        "coarse_quotient_factors": ({"support": 1, "exponent": len(representatives)},),
        "point_lefschetz": tuple(point_lefschetz),
        "point_exact_classes": point_exact,
        "orbit_lefschetz": tuple(orbit_lefschetz),
        "orbit_exact_classes": orbit_exact,
        "point_orbifold_factors": _aggregate_rational(point_orbifold_terms),
        "orbit_orbifold_factors": ({"support": 1, "exponent": inertia_count},),
        "action_kernel_elements": kernel_elements,
        "action_kernel_order": len(kernel_elements),
        "action_effective": len(kernel_elements) == 1,
        "g_permutation_recovered_a_coset": recovered_coset,
        "g_permutation_exact_label_recovery": len(kernel_elements) == 1,
        "stack_components": tuple(
            {"subgroup_order": subgroup_order, "multiplicity": multiplicity}
            for subgroup_order, multiplicity in orbit_types
        ),
        "static_inertia_sector_count": inertia_count,
        "stack_dynamics_static": naturality,
        "naturality_equalities_checked": len(points) * order,
    }


def comparable_projection(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if key != "engine"}


def structural_unit_control() -> dict[str, Any]:
    order, orbit_types, element = STRUCTURAL_CONTROL
    formula = formula_cyclic_cset(order, orbit_types, element)
    enumeration = enumeration_cyclic_cset(order, orbit_types, element)
    dual_match = comparable_projection(formula) == comparable_projection(enumeration)
    expected_checks = {
        "dual_engines_match": dual_match,
        "effective_kernel_one": formula["action_kernel_order"] == 1,
        "source_supports_two_three": formula["source_factors"]
        == ({"support": 2, "exponent": 1}, {"support": 3, "exponent": 1}),
        "no_period_six_factor": all(
            record["support"] != 6 for record in formula["source_factors"]
        ),
        "coarse_two_fixed_components": formula["coarse_quotient_factors"]
        == ({"support": 1, "exponent": 2},),
        "point_orbifold_weights_exact": formula["point_orbifold_factors"]
        == (
            {"support": 2, "exponent": {"numerator": 3, "denominator": 2}},
            {"support": 3, "exponent": {"numerator": 2, "denominator": 3}},
        ),
        "orbit_orbifold_inertia_five": formula["orbit_orbifold_factors"]
        == ({"support": 1, "exponent": 5},),
        "static_inertia_five": formula["static_inertia_sector_count"] == 5,
        "labelled_twist_recovered": formula["g_permutation_recovered_a_coset"] == (1,),
    }
    return {
        "namespace": "structural_unit_control",
        "is_arithmetic_modulus_row": False,
        "is_candidate": False,
        "name": "C6/C2_DISJOINT_UNION_C6/C3",
        "formula_engine": formula,
        "enumeration_engine": enumeration,
        "checks": expected_checks,
        "pass": all(expected_checks.values()),
    }
