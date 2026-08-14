from fractions import Fraction
from pathlib import Path

from sdc21_stationary_semiring_sieve_core import (
    determinant_fraction,
    entropy_shuffle_control,
    gf2_irreducible,
    graph_edges,
    polynomial_control,
    recurrent_nodes,
    shuffled_presentation,
    sieve_primes,
    trace_power,
    trial_accepts,
    universal_decider_controls,
)


def test_support_exact_to_512():
    assert [n for n in range(2, 513) if trial_accepts(n)] == sieve_primes(512)


def test_graph_recurrent_core_is_accept_loops():
    nodes, edges, accepted = graph_edges(64)
    assert set(recurrent_nodes(nodes, edges)) == {f"A:{p}" for p in accepted}


def test_power_traces_exact():
    _, edges, accepted = graph_edges(32, s_integer=2)
    for r in range(1, 9):
        assert trace_power(edges, r) == sum((Fraction(1, p ** (2 * r)) for p in accepted), Fraction(0))


def test_finite_determinant_exact():
    nodes, edges, accepted = graph_edges(8, cemetery_depth=2, s_integer=2)
    z = Fraction(1, 3)
    expected = Fraction(1)
    for p in accepted:
        expected *= 1 - z * Fraction(1, p**2)
    assert determinant_fraction(nodes, edges, z) == expected


def test_transported_presentation_invariant():
    assert shuffled_presentation(512, 19021)["accepted_decoded"] == sieve_primes(512)


def test_untransported_entropy_shuffle_breaks_ledger():
    assert not entropy_shuffle_control(512, 19022)["exact_target"]


def test_bounded_trial_depth_fails():
    selected = {n for n in range(2, 513) if trial_accepts(n, max_divisor=3)}
    assert selected - set(sieve_primes(512))


def test_shifted_factor_predicate_fails():
    selected = {n for n in range(2, 513) if trial_accepts(n, shift=1)}
    assert selected != set(sieve_primes(512))


def test_polynomial_irreducibility_examples():
    assert gf2_irreducible(0b11)  # x+1
    assert gf2_irreducible(0b111)  # x^2+x+1
    assert not gf2_irreducible(0b101)  # x^2+1=(x+1)^2


def test_polynomial_control_euler_identity():
    assert polynomial_control(8)["exact"]


def test_universal_decider_wrappers_reproduce_any_support():
    rows = universal_decider_controls(16)
    assert len(rows) == 4
    assert all(row["recurrent_exact"] and row["determinant_exact"] for row in rows)


def test_scientific_source_has_no_factor_existence_helper():
    source = (
        Path(__file__).with_name("sdc21_stationary_semiring_sieve_core.py")
        .read_text(encoding="utf-8")
    )
    for forbidden in ("tensor_divides", "exists_factor", "factor_exists", "has_factor"):
        assert forbidden not in source


def test_explicit_quotient_states_cover_success_reject_and_overshoot():
    nodes, edges, _ = graph_edges(32, cemetery_depth=3, s_integer=2)
    assert any(node.startswith("Q:") for node in nodes)
    q_edges = [edge for edge in edges if edge.source.startswith("Q:")]
    assert any(edge.target.startswith("Q:") for edge in q_edges)
    assert any(edge.target.startswith("R:") for edge in q_edges)
    assert any(edge.target.startswith("T:") for edge in q_edges)
