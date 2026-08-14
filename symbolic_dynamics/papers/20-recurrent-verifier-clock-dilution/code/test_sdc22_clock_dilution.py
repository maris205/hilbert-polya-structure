from fractions import Fraction
import ast
import math
from pathlib import Path

from sdc22_clock_dilution import (
    cycle_power_trace,
    determinant_at_return_section,
    direct_sum_determinant,
    expanded_cycle_length,
    harmonic_lower_bound,
    marked_determinant_at_return_section,
    optimal_max_edge_weight,
    padded_decider_controls,
    sieve_primes,
    simulated_cycle_length,
    source_roof_total,
    verifier_forward_path,
)


def test_closed_form_matches_independent_simulation():
    for p in sieve_primes(1024):
        assert expanded_cycle_length(p) == simulated_cycle_length(p)


def test_explicit_q_states_and_contracted_acceptance_boundary():
    accepted, states = verifier_forward_path(101)
    assert accepted
    assert states[0] == states[-1] == "I:101"
    assert any(state.startswith("Q:101:") for state in states)
    assert len(states) - 1 == expanded_cycle_length(101) == 202

    accepted_composite, composite_states = verifier_forward_path(91)
    assert not accepted_composite
    assert composite_states[-1] == "R:91:1"
    assert composite_states[0] not in composite_states[1:]


def test_transition_source_has_no_hidden_oracle_macro():
    source_path = Path(__file__).with_name("sdc22_clock_dilution.py")
    source = source_path.read_text(encoding="utf-8")
    forbidden = ("tensor_divides", "exists_factor", "factor_exists", "has_factor")
    assert all(token not in source for token in forbidden)
    tree = ast.parse(source)
    verifier = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "verifier_forward_path"
    )
    calls = {
        node.func.id
        for node in ast.walk(verifier)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert calls.isdisjoint({"any", "all", "sieve_primes"})


def test_harmonic_lower_bound():
    for p in sieve_primes(1024):
        assert expanded_cycle_length(p) >= harmonic_lower_bound(p)


def test_length_to_clock_ratio_grows_on_frozen_witnesses():
    witnesses = [31, 127, 509, 2039, 4093]
    ratios = [expanded_cycle_length(p) / math.log(p) for p in witnesses]
    assert ratios == sorted(ratios)
    assert ratios[-1] > 1800


def test_optimal_edge_weight_approaches_one():
    witnesses = [31, 127, 509, 2039, 4093]
    weights = [optimal_max_edge_weight(p, 2.0) for p in witnesses]
    assert weights == sorted(weights)
    assert weights[-1] > 0.998


def test_concentrated_clock_has_unit_edges():
    # If the entire log(p) clock sits on one edge, every other edge has roof
    # zero. All witnesses beyond p=3 have at least one such edge.
    assert all(expanded_cycle_length(p) > 1 for p in sieve_primes(512))


def test_z_one_determinant_collapses_to_prime_loop_product():
    primes = sieve_primes(31)
    assert direct_sum_determinant(primes, 2, Fraction(1)) == determinant_at_return_section(primes, 2)


def test_step_variable_retains_long_periods():
    primes = sieve_primes(31)
    z = Fraction(1, 3)
    assert direct_sum_determinant(primes, 2, z) != marked_determinant_at_return_section(
        primes, 2, z
    )


def test_exact_power_trace_repetitions():
    for p in sieve_primes(31):
        length = expanded_cycle_length(p)
        assert cycle_power_trace(p, 2, length - 1) == 0
        assert cycle_power_trace(p, 2, length) == length * Fraction(1, p * p)
        assert cycle_power_trace(p, 2, 2 * length) == length * Fraction(1, p**4)


def test_trace_class_source_roofs_destroy_euler_clock():
    for p in sieve_primes(128):
        assert source_roof_total(p) > math.log(p)


def test_padded_deciders_reproduce_obstruction():
    rows = padded_decider_controls(1024, 2.0)
    assert len(rows) == 4
    assert all(row["all_cycle_products_exact_by_construction"] for row in rows)
    assert all(row["max_optimal_edge_weight"] is not None for row in rows)
