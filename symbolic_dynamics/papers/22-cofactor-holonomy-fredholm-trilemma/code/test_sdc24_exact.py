#!/usr/bin/env python3
"""Regression and theorem-audit tests for SD-C24 exact artifacts."""

from __future__ import annotations

import ast
import csv
import inspect
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

import pytest

import sdc24_cofactor_holonomy as core


PROJECT = Path(__file__).resolve().parents[1]
RESULTS = PROJECT / "results"


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def truth(value: str) -> bool:
    assert value in {"True", "False"}
    return value == "True"


def test_01_source_edge_certificate() -> None:
    data = json.loads((RESULTS / "source_oracle_certificate.json").read_text())
    assert data["cutoff"] == 4096
    assert data["edge_count"] == 30626
    assert data["successor_edge_count"] == 4095
    assert data["quotient_identity_mismatches"] == 0
    assert data["loop_count"] == 0
    assert data["prime_table_used"] is False
    assert data["target_feedback_used"] is False
    assert data["riemann_zero_data_used"] is False


def test_02_graph_constructor_static_no_oracle() -> None:
    constructor_source = "\n".join(
        inspect.getsource(function)
        for function in (core.positive_divisors, core.edge_quotient, core.edges_from)
    ).lower()
    forbidden_calls = {"prime", "isprime", "primerange", "zeta", "zero", "mangoldt"}
    tree = ast.parse(constructor_source)
    called = {
        node.func.id.lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert called.isdisjoint(forbidden_calls)
    assert "(source + 1) // target" in constructor_source
    assert "(source + 1) % target" in constructor_source


def test_03_simple_cycle_regression_counts() -> None:
    data = rows("simple_cycle_holonomy.csv")
    counts = Counter(int(row["cutoff"]) for row in data)
    assert counts == Counter({12: 12, 20: 29, 30: 52})


def test_04_exact_cycle_holonomy_identity() -> None:
    data = rows("simple_cycle_holonomy.csv")
    assert all(Fraction(row["telescoped"]) == int(row["holonomy"]) for row in data)
    assert all(int(row["holonomy"]) >= 2 for row in data)
    assert all(truth(row["integer_ge_two"]) for row in data)


def test_05_q2_if_and_only_if_canonical_family() -> None:
    data = rows("simple_cycle_holonomy.csv")
    counts = Counter(
        int(row["cutoff"]) for row in data if int(row["holonomy"]) == 2
    )
    lengths: dict[int, set[int]] = defaultdict(set)
    for row in data:
        if int(row["holonomy"]) == 2:
            assert truth(row["q2_canonical"])
            lengths[int(row["cutoff"])].add(int(row["length"]))
    assert counts == Counter({12: 5, 20: 9, 30: 14})
    assert lengths == {12: set(range(2, 7)), 20: set(range(2, 11)), 30: set(range(2, 16))}


def test_06_atomic_classification_enumerated_direction() -> None:
    data = [row for row in rows("atomic_holonomy_witnesses.csv") if row["kind"] == "enumerated"]
    assert data
    assert all(truth(row["classification_match"]) for row in data)
    assert all(truth(row["predicted_in_cutoff"]) for row in data)


def test_07_atomic_classification_predicted_direction() -> None:
    data = [row for row in rows("atomic_holonomy_witnesses.csv") if row["kind"] == "predicted"]
    assert data
    assert all(truth(row["classification_match"]) for row in data)
    assert all(int(row["atom"]) in {2, 3, 5, 7} for row in data)


def test_08_rooted_cycle_regression_counts() -> None:
    data = rows("rooted_cycle_ledger.csv")
    counts = Counter(int(row["power"]) for row in data)
    assert counts == Counter({2: 2, 3: 3, 4: 10, 5: 10, 6: 29, 7: 28, 8: 82})
    assert len(data) == 164


def test_09_rooted_cycles_have_unique_rotation_repetition_ledger() -> None:
    data = rows("rooted_cycle_ledger.csv")
    assert all(truth(row["rotation_repetition_match"]) for row in data)
    grouped: Counter[tuple[str, str, str]] = Counter(
        (row["power"], row["primitive_root"], row["repetition"]) for row in data
    )
    for row in data:
        key = (row["power"], row["primitive_root"], row["repetition"])
        assert grouped[key] == int(row["primitive_period"])


def test_10_group_trace_has_no_neutral_support() -> None:
    data = rows("group_trace_coefficients.csv")
    assert all(int(row["holonomy"]) != 1 for row in data)
    assert all(not truth(row["neutral"]) for row in data)


def test_11_atomic_group_trace_formula() -> None:
    data = rows("atomic_trace_coefficients.csv")
    assert len(data) == 80
    assert all(truth(row["match"]) for row in data)
    assert all(Fraction(row["observed"]) == Fraction(row["expected"]) for row in data)


def test_12_atomic_trace_has_no_repetition_contamination() -> None:
    data = rows("atomic_trace_coefficients.csv")
    assert all(not truth(row["repetition_contamination"]) for row in data)
    for row in data:
        atom, power = int(row["atom"]), int(row["power"])
        if Fraction(row["observed"]):
            assert power % (atom - 1) == 0 and power // (atom - 1) >= 2


def test_13_neutral_group_trace_determinant_is_one() -> None:
    data = rows("neutral_determinant.csv")
    assert len(data) == 42
    assert all(truth(row["match"]) for row in data)
    coefficients = [row for row in data if row["determinant_coefficient"]]
    assert all(
        Fraction(row["determinant_coefficient"]) == (1 if int(row["degree"]) == 0 else 0)
        for row in coefficients
    )


def test_14_alias_free_fourier_reconstruction() -> None:
    data = rows("fourier_reconstruction.csv")
    assert len(data) == 12
    assert all(truth(row["alias_free"]) for row in data)
    assert max(float(row["absolute_error"]) for row in data) < 2e-15


def test_15_exact_integer_gauge_identity() -> None:
    data = rows("gauge_identity.csv")
    assert len(data) == 15
    assert all(truth(row["exact_match"]) for row in data)
    assert all(int(row["mismatches"]) == 0 for row in data)
    assert all(not truth(row["infinite_nonunitary_similarity_claimed"]) for row in data)


def test_16_unitary_gauge_and_finite_determinants() -> None:
    data = rows("unitary_gauge.csv")
    assert len(data) == 12
    assert all(truth(row["unitary_similarity_match"]) for row in data)
    assert max(float(row["entry_error"]) for row in data) < 1e-12
    assert max(float(row["determinant_error"]) for row in data) < 1e-11


def test_17_sharp_trace_class_phase_labels() -> None:
    data = rows("trace_class_diagnostics.csv")
    assert len(data) == 56
    assert all(truth(row["classification_match"]) for row in data)
    by_point: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in data:
        by_point[int(row["point"])].append(row)
    assert all(len(value) == 7 for value in by_point.values())
    assert {truth(value[0]["trace_class_iff"]) for key, value in by_point.items() if key in {0, 1, 4}} == {True}
    assert {truth(value[0]["trace_class_iff"]) for key, value in by_point.items() if key in {2, 3, 5, 6, 7}} == {False}


def test_18_trace_class_boundary_criterion_directly() -> None:
    assert core.trace_class_membership(0.6, 0.0)
    assert core.trace_class_membership(0.75, -0.2)
    assert not core.trace_class_membership(0.5, 100.0)
    assert not core.trace_class_membership(0.75, -0.25)
    assert core.trace_class_failure_mode(0.6, -0.2) == "unbounded_fixed_row"
    assert core.trace_class_failure_mode(0.49, 0.2) == "not_trace_class_successor"


def test_19_pure_cofactor_spine_noncompactness_certificate() -> None:
    data = rows("pure_cofactor_spine.csv")
    assert len(data) == 28
    assert all(int(row["successor_weight"]) == 1 for row in data)
    assert all(not truth(row["compact_if_bounded"]) for row in data)
    assert all(not truth(row["trace_class"]) for row in data)
    bounded = [row for row in data if float(row["a"]) > 1]
    assert bounded and all(truth(row["bounded_extension_proved"]) for row in bounded)


def test_20_exact_finite_determinant_trace_ledger() -> None:
    data = rows("finite_determinant_checks.csv")
    assert len(data) == 4
    assert all(truth(row["match"]) for row in data)
    assert all(Fraction(row["trace_expansion"]) == Fraction(row["direct_determinant"]) for row in data)


def test_21_pure_cofactor_closed_form_and_divergence() -> None:
    data = rows("pure_cofactor_series.csv")
    assert len(data) == 9
    for row in data:
        if truth(row["convergent"]):
            assert row["infinite_closed_form"] != "diverges"
        else:
            assert row["z"] == "1" and truth(row["at_z1_nondecaying_term"])


def test_22_induced_return_and_factorial_damping() -> None:
    returns = rows("induced_return_exact.csv")
    assert len(returns) == 124
    assert all(
        truth(row["pure_at_z1_constant"])
        for row in returns
        if int(row["s_integer"]) == 0 and row["z"] == "1"
    )
    damping = rows("factorial_damping.csv")
    assert len(damping) == 63
    assert all(truth(row["strictly_decreasing"]) for row in damping)


def test_23_unitary_phase_never_selects_spine() -> None:
    data = rows("unitary_phase_spine.csv")
    assert len(data) == 124
    assert all(not truth(row["selected_out"]) for row in data)
    assert all(abs(float(row["absolute_value"]) - 1.0) < 2e-15 for row in data)
    by_t: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for row in data:
        by_t[row["t"]].add((row["phase_real"], row["phase_imag"]))
    assert all(len(phases) == 1 for phases in by_t.values())


def test_24_positive_inventories_preserve_all_length_support() -> None:
    data = rows("inventory_controls.csv")
    assert len(data) == 186
    assert all(int(row["holonomy"]) == 2 for row in data)
    assert all(truth(row["support_present"]) and truth(row["positive_weight"]) for row in data)
    inventories = {row["inventory"] for row in data}
    assert inventories == set(core.INVENTORY_NAMES)
    for inventory in inventories:
        lengths = {int(row["k"]) for row in data if row["inventory"] == inventory}
        assert lengths == set(range(2, 33))
        assert any(truth(row["composite_length_witness"]) for row in data if row["inventory"] == inventory)


def test_25_transported_presentation_preserves_holonomy() -> None:
    data = rows("presentation_transport.csv")
    assert len(data) == 31
    assert all(truth(row["transported_successor_and_tensor_together"]) for row in data)
    assert all(truth(row["match"]) for row in data)
    assert all(int(row["source_holonomy"]) == int(row["transported_holonomy"]) == 2 for row in data)


def test_26_summary_target_metrics_are_explicitly_not_applicable() -> None:
    data = json.loads((RESULTS / "summary.json").read_text())
    assert data["candidate_id"] == "SD-C24"
    assert data["target_zero_evaluation"] == "not_applicable; no_target_zero_evaluation"
    assert data["target_root_metrics"] == "not_applicable; no_target_zero_evaluation"
    assert data["cartesian_cycle_enumeration"] is False
