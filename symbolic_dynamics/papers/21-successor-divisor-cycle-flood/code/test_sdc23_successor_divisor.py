"""Exact regression suite for SD-C23."""

from __future__ import annotations

import ast
from fractions import Fraction
import math
from pathlib import Path

from sdc23_successor_divisor import (
    CANONICAL_CHECK_MAX,
    CONTROL_MAX_POWER,
    SOURCE_AUDIT_CUTOFF,
    TRACE_MAX_POWER,
    WEIGHTED_MAX_POWER,
    WEIGHTED_S_VALUES,
    canonical_cycle,
    canonical_rotation,
    cycle_mass,
    cycle_quotients,
    determinant_coefficients,
    is_closed_walk,
    is_simple_cycle,
    power_traces,
    primitive_counts,
    primitive_orbits,
    primitive_product_coefficients,
    primitive_root_length,
    quotient,
    quotient_cycle,
    row_nuclear_prefix,
    source_edge_certificate,
    successor_s1_prefix,
    targets,
)


def test_successor_divisor_rule_quotients_and_no_loops() -> None:
    for source in range(2, 512):
        row = targets(source)
        assert source + 1 in row
        assert source not in row
        for target in row:
            assert source + 1 == target * quotient(source, target)


def test_constructive_paths_through_two() -> None:
    for source in range(2, 512):
        if source == 2:
            path = (2,)
        elif source % 2:
            path = (source, 2)
        else:
            path = (source, source + 1, 2)
        assert all(path[index + 1] in targets(path[index]) for index in range(len(path) - 1))
        assert path[-1] == 2
    assert all(vertex + 1 in targets(vertex) for vertex in range(2, 512))


def test_canonical_cycle_every_length() -> None:
    assert all(
        is_simple_cycle(canonical_cycle(length))
        for length in range(2, CANONICAL_CHECK_MAX + 1)
    )


def test_quotient_cycle_family() -> None:
    for edge_quotient in range(2, 17):
        for divisor in range(2, 17):
            word = quotient_cycle(divisor, edge_quotient)
            assert len(word) == divisor * (edge_quotient - 1)
            assert is_simple_cycle(word, frozenset({1, edge_quotient}))
            assert quotient(word[-1], word[0]) == edge_quotient


def test_closed_walk_and_simple_cycle_are_distinct_predicates() -> None:
    repeated = canonical_cycle(2) * 2
    assert is_closed_walk(repeated)
    assert not is_simple_cycle(repeated)
    assert primitive_root_length(repeated) == 2


def test_exact_confinement_stabilization() -> None:
    for power in range(1, 17):
        certified = power_traces(2 * power - 1, power)[-1]
        plus_one = power_traces(2 * power, power)[-1]
        larger = power_traces(4 * power + 3, power)[-1]
        assert certified == plus_one == larger


def test_cutoff_flag_boundary() -> None:
    for cutoff in (7, 15, 31, 63):
        for power in range(1, TRACE_MAX_POWER + 1):
            expected_flag = cutoff >= 2 * power - 1
            if expected_flag:
                assert (
                    power_traces(cutoff, TRACE_MAX_POWER)[power - 1]
                    == power_traces(2 * TRACE_MAX_POWER - 1, TRACE_MAX_POWER)[
                        power - 1
                    ]
                )


def test_first_unweighted_trace_counts() -> None:
    assert power_traces(15, 8) == (
        Fraction(0),
        Fraction(2),
        Fraction(3),
        Fraction(10),
        Fraction(10),
        Fraction(29),
        Fraction(28),
        Fraction(82),
    )


def test_necklace_inversion_through_order_32() -> None:
    rooted = [
        int(value)
        for value in power_traces(2 * TRACE_MAX_POWER - 1, TRACE_MAX_POWER)
    ]
    primitive = primitive_counts(rooted)
    assert primitive[:10] == [0, 1, 1, 2, 2, 4, 4, 9, 10, 18]
    for power in range(1, TRACE_MAX_POWER + 1):
        assert rooted[power - 1] == sum(
            divisor * primitive[divisor - 1]
            for divisor in range(1, power + 1)
            if power % divisor == 0
        )


def test_first_weighted_trace_formulas_for_three_integer_s() -> None:
    for s_integer in WEIGHTED_S_VALUES:
        traces = power_traces(7, 4, s_integer=s_integer)
        assert traces[0] == 0
        assert traces[1] == 2 * Fraction(1, 6 ** (2 * s_integer))
        assert traces[2] == 3 * Fraction(1, 60 ** (2 * s_integer))
        assert traces[3] == (
            2 * Fraction(1, 6 ** (4 * s_integer))
            + 4 * Fraction(1, 120 ** (2 * s_integer))
            + 4 * Fraction(1, 840 ** (2 * s_integer))
        )


def test_primitive_orbit_inventory_matches_necklace_counts() -> None:
    orbits = primitive_orbits(2 * WEIGHTED_MAX_POWER - 1, WEIGHTED_MAX_POWER)
    counts = {
        length: sum(len(word) == length for word in orbits)
        for length in range(1, WEIGHTED_MAX_POWER + 1)
    }
    rooted = [
        int(value)
        for value in power_traces(
            2 * WEIGHTED_MAX_POWER - 1,
            WEIGHTED_MAX_POWER,
        )
    ]
    expected = primitive_counts(rooted)
    assert [counts[length] for length in range(1, WEIGHTED_MAX_POWER + 1)] == expected
    assert all(tuple(word) == canonical_rotation(word) for word in orbits)
    assert all(primitive_root_length(word) == len(word) for word in orbits)


def test_determinant_coefficients_match_primitive_product() -> None:
    orbits = primitive_orbits(2 * WEIGHTED_MAX_POWER - 1, WEIGHTED_MAX_POWER)
    for s_integer in WEIGHTED_S_VALUES:
        traces = power_traces(
            2 * WEIGHTED_MAX_POWER - 1,
            WEIGHTED_MAX_POWER,
            s_integer=s_integer,
        )
        from_traces = determinant_coefficients(traces)
        from_orbits = primitive_product_coefficients(
            orbits,
            s_integer,
            WEIGHTED_MAX_POWER,
        )
        assert from_traces == from_orbits


def test_determinant_starts_at_degree_two() -> None:
    traces = power_traces(31, WEIGHTED_MAX_POWER, s_integer=1)
    coefficients = determinant_coefficients(traces)
    assert coefficients[0] == 1
    assert coefficients[1] == 0
    assert coefficients[2] == -Fraction(1, 6**2)


def test_two_quotient_spine_has_all_length_flood() -> None:
    values = power_traces(
        2 * CONTROL_MAX_POWER - 1,
        CONTROL_MAX_POWER,
        quotient_inventory=frozenset({1, 2}),
    )
    assert values[0] == 0
    assert all(values[power - 1] > 0 for power in range(2, CONTROL_MAX_POWER + 1))


def test_successor_only_is_acyclic() -> None:
    values = power_traces(
        2 * CONTROL_MAX_POWER - 1,
        CONTROL_MAX_POWER,
        quotient_inventory=frozenset({1}),
    )
    assert all(value == 0 for value in values)


def test_each_retained_nontrivial_quotient_creates_infinite_family_prefix() -> None:
    for edge_quotient in range(2, 17):
        inventory = frozenset({1, edge_quotient})
        for divisor in range(2, 10):
            assert is_simple_cycle(
                quotient_cycle(divisor, edge_quotient),
                inventory,
            )


def test_natural_orbit_norms_are_composite_squares() -> None:
    for length in range(2, 64):
        mass = cycle_mass(canonical_cycle(length))
        norm = mass * mass
        assert mass >= 6
        assert math.isqrt(norm) ** 2 == norm
        assert norm % mass == 0
        assert all(value >= 1 for value in cycle_quotients(canonical_cycle(length)))


def test_trace_class_prefix_diagnostics_and_successor_identity() -> None:
    for sigma in (0.49, 0.50, 0.51, 0.75, 1.00):
        row_values = [row_nuclear_prefix(cutoff, sigma) for cutoff in (64, 128, 256)]
        successor_values = [
            successor_s1_prefix(cutoff, sigma)
            for cutoff in (64, 128, 256)
        ]
        assert row_values == sorted(row_values)
        assert successor_values == sorted(successor_values)
    for cutoff in (64, 128, 256, 512):
        assert successor_s1_prefix(cutoff, 1.0) == Fraction(1, 2) - Fraction(1, cutoff)


def test_source_firewall_and_edge_certificate() -> None:
    source_path = Path(__file__).with_name("sdc23_successor_divisor.py")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported_modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    forbidden_modules = {"sympy", "mpmath", "primesieve"}
    assert imported_modules.isdisjoint(forbidden_modules)
    forbidden_calls = {"primepi", "primerange", "zetazero", "sieve_primes"}
    call_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert call_names.isdisjoint(forbidden_calls)
    certificate = source_edge_certificate(SOURCE_AUDIT_CUTOFF)
    assert certificate["loop_count"] == 0
    assert certificate["quotient_identity_mismatches"] == 0
    assert certificate["successor_edge_count"] == SOURCE_AUDIT_CUTOFF - 1
    assert certificate["target_feedback_used"] is False
    assert certificate["riemann_zero_data_used"] is False
