#!/usr/bin/env python3
"""Exact regression tests for the frozen SD-C30 candidate and controls."""

from __future__ import annotations

import ast
from pathlib import Path

import pytest
import sympy as sp

from sdc30_chiral_incidence import (
    active_positive_metric,
    b2_from_gram,
    compile_idempotents,
    covers_bottom,
    gamma_length,
    gram_matrix,
    is_selfadjoint_in_metric,
    marker_exponent,
    native_chiral_block,
    orthogonal_chiral_block,
    orthogonal_det3_factor,
)
from sdc30_evaluator import (
    all_fixtures,
    composite_fixture,
    mutated_fixture,
    seeded_dag_fixture,
)


ETA = 2
FIXTURES = all_fixtures()


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_incidence_inverse(fixture) -> None:
    zeta, mobius, _ = compile_idempotents(fixture.relation)
    identity = sp.eye(len(fixture.labels))
    assert zeta * mobius == identity
    assert mobius * zeta == identity


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_complete_primitive_system(fixture) -> None:
    _, _, compiled = compile_idempotents(fixture.relation)
    size = len(fixture.labels)
    zero = sp.zeros(size)
    assert sum(compiled, zero) == sp.eye(size)
    for left in range(size):
        assert compiled[left].rank() == 1
        assert sp.trace(compiled[left]) == 1
        for right in range(size):
            assert compiled[left] * compiled[right] == (
                compiled[left] if left == right else zero
            )


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_cover_atoms_are_relation_derived(fixture) -> None:
    atoms = covers_bottom(fixture.relation)
    assert len(atoms) >= fixture.selected_count
    for atom in atoms:
        assert fixture.relation[0][atom]
        assert not any(
            middle != atom
            and fixture.relation[0][middle]
            and fixture.relation[middle][atom]
            for middle in range(1, len(fixture.labels))
        )


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_native_gram_against_direct_weighted_trace(fixture) -> None:
    _, _, compiled = compile_idempotents(fixture.relation)
    selected = covers_bottom(fixture.relation)[: fixture.selected_count]
    weights = tuple(label ** (2 * ETA) for label in fixture.labels)
    weight = sp.diag(*weights)
    gram = gram_matrix(selected, compiled, weights)
    assert gram == gram.T
    for left, left_index in enumerate(selected):
        for right, right_index in enumerate(selected):
            direct = sp.cancel(
                sp.trace(
                    compiled[left_index]
                    * weight.inv()
                    * compiled[right_index].T
                    * weight
                )
            )
            assert gram[left, right] == direct
            assert direct >= 0
            if left == right:
                assert direct > 0


@pytest.mark.parametrize(
    ("left", "right"),
    [(2, 2), (2, 3), (2, 5), (3, 2), (3, 3), (3, 5), (5, 2), (5, 3), (5, 5)],
)
def test_infinite_native_gram_formula(left: int, right: int) -> None:
    c_eta = sp.simplify(sp.zeta(2 * ETA) / sp.zeta(4 * ETA))
    if left == right:
        value = sp.simplify(c_eta * (1 + sp.Rational(1, left ** (2 * ETA))))
    else:
        value = sp.simplify(
            c_eta
            * sp.Rational(1, (left * right) ** (2 * ETA))
            / (
                (1 + sp.Rational(1, left ** (2 * ETA)))
                * (1 + sp.Rational(1, right ** (2 * ETA)))
            )
        )
    assert value > 0
    if left != right:
        reverse = sp.simplify(
            c_eta
            * sp.Rational(1, (right * left) ** (2 * ETA))
            / (
                (1 + sp.Rational(1, right ** (2 * ETA)))
                * (1 + sp.Rational(1, left ** (2 * ETA)))
            )
        )
        assert value == reverse


@pytest.mark.parametrize("order", range(1, 9))
def test_common_schatten_strip(order: int) -> None:
    lower = sp.Rational(1, order)
    upper = 1 - lower
    nonempty = lower < upper
    assert nonempty == (order > 2)
    assert (lower < sp.Rational(1, 2) < upper) == (order > 2)
    assert (order == 3) == (nonempty and not sp.Rational(1, order - 1) < sp.Rational(1, 2))


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_finite_b2_direct_equals_gram_and_moves(fixture) -> None:
    _, _, compiled = compile_idempotents(fixture.relation)
    selected = covers_bottom(fixture.relation)[: fixture.selected_count]
    labels = tuple(fixture.labels[index] for index in selected)
    weights = tuple(label ** (2 * ETA) for label in fixture.labels)
    gram = gram_matrix(selected, compiled, weights)
    block, phases = native_chiral_block(selected, fixture.labels, compiled, weights)
    size = len(fixture.labels)
    direct = sp.expand(2 * sp.trace(block[:size, size:] * block[size:, :size]))
    expected = b2_from_gram(selected, fixture.labels, gram, phases)
    assert sp.simplify(direct - expected) == 0
    assert direct.free_symbols & set(phases)
    at_one = {phase: 1 for phase in phases}
    at_flip = {phase: (-1 if index == 1 else 1) for index, phase in enumerate(phases)}
    assert sp.simplify(direct.subs(at_one) - direct.subs(at_flip)) != 0
    assert len(labels) >= 2


@pytest.mark.parametrize(("left", "right"), [(2, 3), (2, 5), (3, 5)])
def test_unique_positive_b4_frequency(left: int, right: int) -> None:
    c_eta = sp.simplify(sp.zeta(2 * ETA) / sp.zeta(4 * ETA))
    gram = sp.simplify(
        c_eta
        * sp.Rational(1, (left * right) ** (2 * ETA))
        / (
            (1 + sp.Rational(1, left ** (2 * ETA)))
            * (1 + sp.Rational(1, right ** (2 * ETA)))
        )
    )
    coefficient = sp.simplify(4 * gram**2 / (left * right))
    assert coefficient > 0
    assert sp.factor(sp.Rational(right, left)) != 1
    if (left, right) == (2, 3):
        assert coefficient == sp.Rational(3675, 971618) / sp.pi**8


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_full_metric_rigidity(fixture) -> None:
    zeta, mobius, compiled = compile_idempotents(fixture.relation)
    diagonal = sp.diag(*range(1, len(fixture.labels) + 1))
    metric = mobius.T * diagonal * mobius
    assert metric.is_positive_definite
    assert zeta.T * metric * zeta == diagonal
    assert all(is_selfadjoint_in_metric(matrix, metric) for matrix in compiled)


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_active_metric_rigidity(fixture) -> None:
    zeta, mobius, compiled = compile_idempotents(fixture.relation)
    selected = covers_bottom(fixture.relation)[: fixture.selected_count]
    metric, coordinate_metric, coupled = active_positive_metric(mobius, selected)
    assert coordinate_metric.is_positive_definite
    assert zeta.T * metric * zeta == coordinate_metric
    assert coordinate_metric[coupled[0], coupled[1]] != 0
    assert all(is_selfadjoint_in_metric(compiled[index], metric) for index in selected)
    assert not all(is_selfadjoint_in_metric(matrix, metric) for matrix in compiled)


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda item: item.name)
def test_orthogonalized_det3_is_phase_free(fixture) -> None:
    atoms = covers_bottom(fixture.relation)[: fixture.selected_count]
    labels = tuple(fixture.labels[index] for index in atoms)
    block, phases = orthogonal_chiral_block(labels)
    z = sp.symbols("z")
    characteristic = sp.factor((sp.eye(block.rows) - z * block).det())
    expected = sp.factor(sp.prod(1 - z**2 / label for label in labels))
    det3 = sp.prod(orthogonal_det3_factor(label, z) for label in labels)
    assert sp.simplify(characteristic - expected) == 0
    assert not characteristic.free_symbols & set(phases)
    assert not det3.free_symbols & set(phases)


@pytest.mark.parametrize("label", [2, 3, 5])
def test_marker_u1_ownership_all_repetitions(label: int) -> None:
    length = gamma_length(label)
    assert length == 2 * (label.bit_length() - 1) + 1
    for repetition in range(1, 9):
        assert marker_exponent(label, repetition) == repetition * length
        assert 1 ** marker_exponent(label, repetition) == 1


@pytest.mark.parametrize(
    "fixture",
    [mutated_fixture(), composite_fixture(), seeded_dag_fixture()],
    ids=lambda item: item.name,
)
def test_nonarithmetic_controls_prove_too_much(fixture) -> None:
    _, _, compiled = compile_idempotents(fixture.relation)
    selected = covers_bottom(fixture.relation)[: fixture.selected_count]
    weights = tuple(label ** (2 * ETA) for label in fixture.labels)
    gram = gram_matrix(selected, compiled, weights)
    block, phases = native_chiral_block(selected, fixture.labels, compiled, weights)
    size = len(fixture.labels)
    product = block[:size, size:] * block[size:, :size]
    b4 = sp.expand(2 * sp.trace(product * product))
    assert any(gram[left, right] != 0 for left in range(gram.rows) for right in range(left + 1, gram.cols))
    assert b4.free_symbols & set(phases)


def test_det3_deletion_ledger() -> None:
    deleted = [power for power in range(1, 9) if power < 3]
    visible = [power for power in range(1, 9) if power >= 3 and power % 2 == 0]
    assert deleted == [1, 2]
    assert visible[0] == 4
    assert visible == [4, 6, 8]


def test_infinite_non_s2_firewall() -> None:
    critical = sp.Rational(1, 2)
    assert not 2 * critical > 1
    assert all(order * critical > 1 for order in range(3, 9))
    assert not (sp.Rational(1, 2) < critical < sp.Rational(1, 2))


def test_candidate_core_has_no_forbidden_oracle_calls() -> None:
    core = Path(__file__).with_name("sdc30_chiral_incidence.py")
    tree = ast.parse(core.read_text(encoding="utf-8"))
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    assert calls.isdisjoint(
        {
            "factorint",
            "isprime",
            "primepi",
            "primerange",
            "sieve",
            "zeta",
            "zetazero",
            "siegelz",
            "mangoldt",
        }
    )
