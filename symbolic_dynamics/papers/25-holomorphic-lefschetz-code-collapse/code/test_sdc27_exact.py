#!/usr/bin/env python3
"""Exact regression tests for SD-C27."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path

import sympy as sp
import pytest

from sdc27_evaluator import INVENTORY_NAMES, inventories_at_cutoff
from sdc27_holomorphic_lefschetz import (
    branch_for_integer,
    centered_local_determinants,
    chain_certificate,
    desired_ordinary_fiber_determinant,
    elias_gamma_code,
    gamma_length,
    power_supertrace,
    prefix_collision_pairs,
    primitive_necklaces,
    scalar_rigidity,
    shared_disjoint_polynomials,
    two_by_two_moment_control,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("atom", "expected"),
    ((1, "1"), (2, "010"), (3, "011"), (4, "00100"), (5, "00101"), (8, "0001000")),
)
def test_gamma_examples(atom: int, expected: str) -> None:
    assert elias_gamma_code(atom) == expected


@pytest.mark.parametrize("atom", (2, 3, 7, 31, 4096))
def test_gamma_length_formula(atom: int) -> None:
    assert len(elias_gamma_code(atom)) == gamma_length(atom)


def test_gamma_prefix_free_registry() -> None:
    words = [elias_gamma_code(atom) for atom in range(1, 4097)]
    assert prefix_collision_pairs(words) == 0


@pytest.mark.parametrize("atom", (2, 3, 5, 31, 4096))
def test_affine_branch_derivative_and_containment(atom: int) -> None:
    code, translation, derivative = branch_for_integer(atom)
    assert derivative == Fraction(1, 2 ** len(code))
    assert abs(translation) + derivative <= Fraction(3, 4)


@pytest.mark.parametrize("degree", (2, 3, 4, 5))
@pytest.mark.parametrize("atoms", ((2,), (2, 3, 5)))
def test_de_rham_chain_and_characteristic_quotient(
    degree: int, atoms: tuple[int, ...]
) -> None:
    branches = []
    for atom in atoms:
        _, translation, derivative = branch_for_integer(atom)
        branches.append((Fraction(1, atom * atom), translation, derivative))
    certificate = chain_certificate(branches, degree)
    assert certificate["chain_residual_zero"]
    assert certificate["characteristic_quotient_exact"]
    assert not certificate["ordinary_block_equals_graded_ratio"]


@pytest.mark.parametrize("power", range(1, 7))
def test_all_power_supertrace(power: int) -> None:
    branches = []
    for atom in (2, 3, 5):
        _, translation, derivative = branch_for_integer(atom)
        branches.append((Fraction(1, atom * atom), translation, derivative))
    actual, expected = power_supertrace(branches, 5, power)
    assert sp.expand(actual - expected) == 0


@pytest.mark.parametrize("atom", (2, 3, 5, 31, 257))
def test_scalar_first_fit_second_failure(atom: int) -> None:
    _, _, q = branch_for_integer(atom)
    first, first_residual = scalar_rigidity(q, 1)
    second, second_residual = scalar_rigidity(q, 2)
    assert first == 1 and first_residual == 0
    assert second != 1 and second_residual != 0
    assert second_residual == -2 * q / (1 + q)


@pytest.mark.parametrize("atom", (2, 4, 16, 256, 4096))
def test_ordinary_matrix_entire_pole_firewall(atom: int) -> None:
    _, _, q = branch_for_integer(atom)
    determinant, has_pole = desired_ordinary_fiber_determinant(q)
    control = two_by_two_moment_control(q)
    assert "t" in determinant
    assert has_pole
    assert control["p3_residual"] != 0


@pytest.mark.parametrize("atom", (2, 3, 5, 17, 257))
def test_local_telescoping_and_ordinary_block_firewall(atom: int) -> None:
    _, _, q = branch_for_integer(atom)
    value = centered_local_determinants(Fraction(1, atom * atom), q, 5)
    assert value["quotient_exact"]
    assert not value["ordinary_equals_graded"]


def test_shared_disjoint_difference() -> None:
    value = shared_disjoint_polynomials([Fraction(1, 4), Fraction(1, 9)])
    assert not value["equal"]
    assert value["shared"] != value["disjoint"]


@pytest.mark.parametrize(
    ("alphabet_size", "expected"), ((2, 23), (3, 196), (4, 964))
)
def test_primitive_necklace_census(alphabet_size: int, expected: int) -> None:
    assert len(primitive_necklaces(alphabet_size, 6)) == expected


def test_inventory_registry() -> None:
    inventories = inventories_at_cutoff(127)
    assert tuple(inventories) == INVENTORY_NAMES
    assert all(inventories[name] for name in INVENTORY_NAMES)


def test_matched_density_controls() -> None:
    for cutoff in (31, 127, 511):
        inventories = inventories_at_cutoff(cutoff)
        target = len(inventories["prime_evaluator"])
        assert len(inventories["matched_density_seeded_random"]) == target
        assert len(inventories["matched_density_hash"]) == target


def test_candidate_core_has_no_forbidden_oracle_calls() -> None:
    tree = ast.parse((ROOT / "code" / "sdc27_holomorphic_lefschetz.py").read_text())
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    assert calls.isdisjoint(
        {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
    )

