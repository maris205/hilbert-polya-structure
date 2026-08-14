#!/usr/bin/env python3
"""Exact regression tests for SD-C29."""

from __future__ import annotations

import ast
from fractions import Fraction
from itertools import product
from pathlib import Path

import mpmath as mp
import pytest
import sympy as sp

from sdc29_evaluator import (
    arithmetic_mobius,
    deterministic_permutation,
    evaluator_atoms,
    expected_incidence_entry,
)
from sdc29_incidence_atom_compiler import (
    affine_one_form,
    affine_zero_form,
    atom_actions,
    compiled_idempotents,
    covers_bottom,
    de_rham_tensor_transfers,
    derivative_matrix,
    divisibility_relation,
    finite_transfer,
    gamma_affine_branch,
    gamma_code,
    gamma_length,
    incidence_inverse,
    marked_weight,
    mutate_six_to_cover,
    necklace_representatives,
    permute_matrix,
    selector_value,
    word_trace_via_pair_relations,
    zeta_matrix,
)


@pytest.mark.parametrize("cutoff", [6, 12, 18, 30])
def test_incidence_inverse(cutoff: int) -> None:
    relation = divisibility_relation(cutoff)
    zeta = zeta_matrix(relation)
    mobius = incidence_inverse(relation)
    assert zeta * mobius == sp.eye(cutoff)
    assert mobius * zeta == sp.eye(cutoff)


def test_complete_primitive_system() -> None:
    cutoff = 18
    relation = divisibility_relation(cutoff)
    _, _, compiled = compiled_idempotents(relation)
    zero = sp.zeros(cutoff)
    assert sum(compiled, zero) == sp.eye(cutoff)
    for left in range(cutoff):
        assert compiled[left].rank() == 1
        assert sp.trace(compiled[left]) == 1
        for right in range(cutoff):
            assert compiled[left] * compiled[right] == (
                compiled[left] if left == right else zero
            )


@pytest.mark.parametrize("source_label", range(1, 13))
def test_compiled_entry_formula(source_label: int) -> None:
    cutoff = 18
    relation = divisibility_relation(cutoff)
    _, _, compiled = compiled_idempotents(relation)
    matrix = compiled[source_label - 1]
    for left in range(1, cutoff + 1):
        for right in range(1, cutoff + 1):
            assert matrix[left - 1, right - 1] == expected_incidence_entry(
                left, source_label, right
            )


@pytest.mark.parametrize("cutoff", [30, 64, 128])
def test_cover_atoms_against_postfreeze_evaluator(cutoff: int) -> None:
    derived = [
        index + 1 for index in covers_bottom(divisibility_relation(cutoff))
    ]
    assert derived == evaluator_atoms(cutoff)


@pytest.mark.parametrize("length", range(1, 7))
def test_necklace_selector_by_length(length: int) -> None:
    relation = divisibility_relation(30)
    actions, atoms = atom_actions(relation)
    alphabet = tuple(atoms[:4])
    representatives = [
        word
        for word in necklace_representatives(alphabet, length)
        if len(word) == length
    ]
    selected = 0
    for word in representatives:
        actual = word_trace_via_pair_relations(word, actions)
        expected = selector_value(word, atoms)
        assert actual == expected
        selected += int(actual)
    assert selected == 4


def test_composite_letter_and_all_words_control() -> None:
    relation = divisibility_relation(18)
    actions, atoms = atom_actions(relation)
    alphabet = (1, 2, 3, 4)  # labels 2,3,4,5
    for length in range(1, 6):
        for word in product(alphabet, repeat=length):
            assert sp.trace(
                sp.prod(actions[letter] for letter in word)
            ) == selector_value(word, atoms)


@pytest.mark.parametrize("label", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
def test_digit_marker_all_repetitions(label: int) -> None:
    assert gamma_length(label) == 2 * (label.bit_length() - 1) + 1
    assert len(gamma_code(label)) == gamma_length(label)
    for repetition in range(1, 9):
        assert repetition * len(gamma_code(label)) == repetition * gamma_length(label)


def test_finite_fredholm_and_power_traces() -> None:
    cutoff = 18
    relation = divisibility_relation(cutoff)
    _, _, compiled = compiled_idempotents(relation)
    atoms = covers_bottom(relation)
    transfer, weights = finite_transfer(compiled, atoms, 2, Fraction(1, 2))
    z = sp.Rational(1, 3)
    assert (sp.eye(cutoff) - z * transfer).det() == sp.prod(
        1 - z * weight for weight in weights.values()
    )
    for repetition in range(1, 9):
        assert sp.trace(transfer**repetition) == sum(
            weight**repetition for weight in weights.values()
        )


@pytest.mark.parametrize("label", [2, 3, 5, 7])
def test_local_de_rham_chain_and_repetitions(label: int) -> None:
    degree = 4
    translation, contraction = gamma_affine_branch(label)
    zero = affine_zero_form(degree, translation, contraction)
    one = affine_one_form(degree, translation, contraction)
    derivative = derivative_matrix(degree)
    assert derivative * zero == one * derivative
    for repetition in range(1, 7):
        assert sp.trace(zero**repetition) - sp.trace(one**repetition) == 1


def test_honest_de_rham_relative_ratio() -> None:
    relation = divisibility_relation(10)
    degree = 3
    zero, one, weights = de_rham_tensor_transfers(
        relation, degree, 2, Fraction(1, 2)
    )
    z = sp.Rational(1, 3)
    zero_det = (sp.eye(zero.rows) - z * zero).det()
    one_det = (sp.eye(one.rows) - z * one).det()
    assert sp.cancel(zero_det / one_det) == sp.prod(
        1 - z * weight for weight in weights.values()
    )


@pytest.mark.parametrize(
    "eta",
    [Fraction(3, 5), Fraction(3, 4), Fraction(1), Fraction(5, 4)],
)
def test_weighted_hilbert_trace_norm_bound(eta: Fraction) -> None:
    mp.mp.dps = 40
    eta_mp = mp.mpf(eta.numerator) / eta.denominator
    c_eta = mp.zeta(2 * eta_mp) / mp.zeta(4 * eta_mp)
    assert eta > Fraction(1, 2)
    for label in [2, 3, 5, 7, 11, 13]:
        norm = mp.sqrt((1 + label ** (-2 * eta_mp)) * c_eta)
        assert norm <= mp.sqrt(2 * c_eta)
        assert norm >= 1


def test_bounded_similarity_finite_certificate() -> None:
    relation = divisibility_relation(18)
    zeta, mobius, compiled = compiled_idempotents(relation)
    assert zeta * mobius == mobius * zeta == sp.eye(18)
    for index in range(18):
        coordinate = sp.zeros(18)
        coordinate[index, index] = 1
        assert compiled[index] == zeta * coordinate * mobius
    for eta in [Fraction(5, 4), Fraction(3, 2), Fraction(2)]:
        assert eta > 1


@pytest.mark.parametrize("label", range(1, 7))
def test_cutoff_stability(label: int) -> None:
    _, _, larger = compiled_idempotents(divisibility_relation(30))
    _, _, smaller = compiled_idempotents(divisibility_relation(18))
    assert larger[label - 1][:18, :18] == smaller[label - 1]


def test_relabeling_equivariance() -> None:
    size = 12
    relation = divisibility_relation(size)
    zeta, _, compiled = compiled_idempotents(relation)
    permutation = deterministic_permutation(size)
    relabeled_zeta = permute_matrix(zeta, permutation)
    relabeled_mobius = relabeled_zeta.inv()
    for new_index, old_index in enumerate(permutation):
        coordinate = sp.zeros(size)
        coordinate[new_index, new_index] = 1
        assert (
            relabeled_zeta * coordinate * relabeled_mobius
            == permute_matrix(compiled[old_index], permutation)
        )


def test_mutated_source_proves_too_much() -> None:
    standard = divisibility_relation(6)
    mutated = mutate_six_to_cover(standard)
    assert [index + 1 for index in covers_bottom(standard)] == [2, 3, 5]
    assert [index + 1 for index in covers_bottom(mutated)] == [2, 3, 5, 6]


@pytest.mark.parametrize(
    ("label", "expected"),
    [(2, -1), (6, 1), (4, 0)],
)
def test_scalar_mobius_ablation(label: int, expected: int) -> None:
    assert arithmetic_mobius(label) == expected
    if label == 2:
        assert expected * expected != expected
    elif label == 6:
        assert expected != 0
    else:
        assert expected == 0


def test_zeta_only_and_unfiltered_ablations() -> None:
    relation = divisibility_relation(12)
    zeta, _, compiled = compiled_idempotents(relation)
    e2 = sp.zeros(12)
    e4 = sp.zeros(12)
    e2[1, 1] = 1
    e4[3, 3] = 1
    assert (zeta * e2) * (zeta * e4) != sp.zeros(12)
    assert sp.trace(compiled[3]) == 1
    assert 3 not in covers_bottom(relation)


def test_candidate_core_has_no_forbidden_oracle_calls() -> None:
    core = Path(__file__).with_name("sdc29_incidence_atom_compiler.py")
    tree = ast.parse(core.read_text(encoding="utf-8"))
    calls = {
        (
            node.func.id
            if isinstance(node.func, ast.Name)
            else node.func.attr
        ).lower()
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
            "mangoldt",
        }
    )
