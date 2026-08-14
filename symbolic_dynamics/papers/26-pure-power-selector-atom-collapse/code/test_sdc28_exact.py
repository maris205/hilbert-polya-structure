#!/usr/bin/env python3
"""Exact regression tests for SD-C28."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as sp

from sdc28_evaluator import INVENTORY_NAMES, inventories_at_cutoff
from sdc28_pure_power_selector import (
    affine_pullback_one,
    affine_pullback_zero,
    color_algebra_certificate,
    de_rham_local_certificate,
    graded_extension_matrices,
    gamma_length,
    hankel_rank,
    matrix_product,
    monochromatic_selector,
    projector_matrices,
    radical_matrices,
    reversal_adversary_matrices,
    support_exterior_certificate,
    words,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("color_count", range(1, 8))
def test_projector_selector(color_count: int) -> None:
    matrices = projector_matrices(color_count)
    for word in words(color_count, 4):
        assert sp.trace(matrix_product(matrices, word)) == monochromatic_selector(word)


@pytest.mark.parametrize("color_count", range(1, 7))
def test_radical_selector(color_count: int) -> None:
    matrices = radical_matrices(color_count)
    for word in words(color_count, 4):
        assert sp.trace(matrix_product(matrices, word)) == monochromatic_selector(word)


@pytest.mark.parametrize("color_count", range(1, 6))
def test_graded_selector(color_count: int) -> None:
    even, odd = graded_extension_matrices(color_count)
    for word in words(color_count, 4):
        actual = sp.trace(matrix_product(even, word)) - sp.trace(
            matrix_product(odd, word)
        )
        assert actual == monochromatic_selector(word)


@pytest.mark.parametrize("color_count", range(1, 8))
def test_hankel_ranks(color_count: int) -> None:
    assert hankel_rank(color_count, 2, color_count)[0] == color_count
    assert hankel_rank(color_count, 2, 0)[0] == color_count + 1


def test_aggregate_adversary() -> None:
    even, odd = reversal_adversary_matrices()
    for weights in ((1, 2, 3), (-2, 5, 7), (0, 3, -4), (11, -1, 2)):
        even_pencil = sum(
            (weights[i] * even[i] for i in range(3)), sp.zeros(6)
        )
        odd_pencil = sum(
            (weights[i] * odd[i] for i in range(3)), sp.zeros(3)
        )
        for power in range(1, 9):
            assert sp.trace(even_pencil**power) - sp.trace(odd_pencil**power) == sum(
                weight**power for weight in weights
            )
    assert sp.trace(matrix_product(even, (0, 1, 2))) - sp.trace(
        matrix_product(odd, (0, 1, 2))
    ) == 1
    assert sp.trace(matrix_product(even, (2, 1, 0))) - sp.trace(
        matrix_product(odd, (2, 1, 0))
    ) == -1


@pytest.mark.parametrize("support_size", range(1, 10))
def test_support_exterior(support_size: int) -> None:
    certificate = support_exterior_certificate(support_size)
    assert certificate["exact"]


@pytest.mark.parametrize("color_count", range(1, 9))
def test_color_algebra(color_count: int) -> None:
    certificate = color_algebra_certificate(color_count)
    assert certificate["multiplication_failures"] == 0
    assert certificate["separability_centrality_failures"] == 0
    assert certificate["separability_multiplication_is_identity"]


@pytest.mark.parametrize("degree", (2, 3, 4, 5))
@pytest.mark.parametrize("label", (2, 3, 5))
def test_de_rham_local(label: int, degree: int) -> None:
    certificate = de_rham_local_certificate(
        degree,
        Fraction(label - 1, 4 * label),
        Fraction(1, 2 ** gamma_length(label)),
        Fraction(1, label * label),
        6,
    )
    assert certificate["chain_exact"]
    assert certificate["quotient_exact"]
    assert all(row["exact"] for row in certificate["power_rows"])


def test_de_rham_mixed_projector_zero() -> None:
    degree = 4
    projectors = projector_matrices(3)
    zero = []
    one = []
    for index, label in enumerate((2, 3, 5)):
        a = Fraction(label - 1, 4 * label)
        q = Fraction(1, 2 ** gamma_length(label))
        w = Fraction(1, label * label)
        zero.append(sp.kronecker_product(projectors[index], affine_pullback_zero(degree, a, q, w)))
        one.append(sp.kronecker_product(projectors[index], affine_pullback_one(degree, a, q, w)))
    for word in words(3, 4):
        actual = sp.trace(matrix_product(zero, word)) - sp.trace(matrix_product(one, word))
        expected = 0 if len(set(word)) > 1 else Fraction(1, (2, 3, 5)[word[0]] ** (2 * len(word)))
        assert actual == expected


def test_inventory_registry_and_density() -> None:
    inventories = inventories_at_cutoff(127)
    assert tuple(inventories) == INVENTORY_NAMES
    target = len(inventories["prime_evaluator"])
    assert len(inventories["matched_density_seeded_random"]) == target
    assert len(inventories["matched_density_hash"]) == target


def test_candidate_core_has_no_forbidden_oracle_calls() -> None:
    tree = ast.parse(
        (ROOT / "code" / "sdc28_pure_power_selector.py").read_text(encoding="utf-8")
    )
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    assert calls.isdisjoint(
        {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
    )
