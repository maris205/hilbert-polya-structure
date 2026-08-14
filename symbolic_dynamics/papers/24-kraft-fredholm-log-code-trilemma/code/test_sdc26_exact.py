#!/usr/bin/env python3
"""Exact regression tests for SD-C26."""

from __future__ import annotations

import ast
import math
from fractions import Fraction
from pathlib import Path

import pytest

from sdc26_evaluator import INVENTORY_NAMES, inventories_at_cutoff
from sdc26_kraft_fredholm import (
    ALLOCATORS,
    ENCODERS,
    PREFIX_ENCODERS,
    cyclic_collision_count,
    disjoint_cycle_metrics,
    finite_roof_inventory_rank,
    finite_word_capacity,
    kraft_mass,
    marked_local_word,
    prefix_collision_pairs,
    primitive_necklace_count,
    trie_determinant_identity,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("encoder_name", sorted(ENCODERS))
def test_marked_codes_are_cyclically_separating(encoder_name: str) -> None:
    words = [marked_local_word(atom, encoder_name) for atom in range(2, 2049)]
    assert cyclic_collision_count(words) == 0
    assert all(word.count("#") == 1 for word in words)


@pytest.mark.parametrize("encoder_name", PREFIX_ENCODERS)
def test_self_delimiting_payloads_are_prefix_free(encoder_name: str) -> None:
    words = [ENCODERS[encoder_name](atom) for atom in range(1, 1025)]
    assert prefix_collision_pairs(words)[0] == 0
    assert kraft_mass(words) <= 1


def test_raw_binary_payload_exposes_prefix_collisions() -> None:
    words = [ENCODERS["raw_binary"](atom) for atom in range(1, 65)]
    assert prefix_collision_pairs(words)[0] > 0


def test_elias_gamma_kraft_block_identity() -> None:
    encoder = ENCODERS["elias_gamma"]
    for bit_length in range(1, 11):
        upper = 2**bit_length - 1
        assert kraft_mass(encoder(atom) for atom in range(1, upper + 1)) == (
            1 - Fraction(1, 2**bit_length)
        )


@pytest.mark.parametrize("allocation", sorted(ALLOCATORS))
def test_positive_roof_simplex(allocation: str) -> None:
    for length in range(2, 32):
        shares = ALLOCATORS[allocation](length, 97)
        assert min(shares) > 0
        assert sum(shares, Fraction(0)) == 1


@pytest.mark.parametrize("allocation", sorted(ALLOCATORS))
@pytest.mark.parametrize("sigma", (1, 2))
def test_weighted_cycle_bounds(allocation: str, sigma: int) -> None:
    data = disjoint_cycle_metrics(8191, "elias_gamma", allocation, sigma)
    assert data["max_singular_value"] + 1e-15 >= data[
        "universal_max_sv_lower_bound"
    ]
    assert data["block_s1_norm"] + 1e-14 >= data[
        "amgm_block_s1_lower_bound"
    ]


@pytest.mark.parametrize(
    ("alphabet_size", "length", "expected"),
    ((2, 2, 1), (3, 2, 3), (2, 3, 2), (4, 4, 60)),
)
def test_primitive_necklace_counts(
    alphabet_size: int, length: int, expected: int
) -> None:
    assert primitive_necklace_count(alphabet_size, length) == expected


@pytest.mark.parametrize("encoder_name", sorted(ENCODERS))
def test_trie_renewal_determinant_identity(encoder_name: str) -> None:
    encoder = ENCODERS[encoder_name]
    actual, expected = trie_determinant_identity(
        {atom: encoder(atom) for atom in (2, 3, 5, 7)}, sigma=2
    )
    assert actual == expected


@pytest.mark.parametrize("encoder_name", sorted(ENCODERS))
def test_shared_trie_return_roof_is_positive(encoder_name: str) -> None:
    encoder = ENCODERS[encoder_name]
    for atom in range(2, 4097):
        assert math.log(atom) - len(encoder(atom)) * math.log(2) / 8 > 0


def test_mandatory_inventory_registry() -> None:
    inventories = inventories_at_cutoff(511)
    assert tuple(inventories) == INVENTORY_NAMES
    assert all(inventories[name] for name in INVENTORY_NAMES)


def test_density_matched_controls() -> None:
    for cutoff in (127, 511, 2047, 8191):
        inventories = inventories_at_cutoff(cutoff)
        target = len(inventories["prime_evaluator"])
        assert len(inventories["matched_density_seeded_random"]) == target
        assert len(inventories["matched_density_hash"]) == target


def test_candidate_core_has_no_forbidden_oracle_calls() -> None:
    tree = ast.parse((ROOT / "code" / "sdc26_kraft_fredholm.py").read_text())
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    assert calls.isdisjoint(
        {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
    )


def test_finite_word_capacity_bound() -> None:
    for length in range(1, 10):
        assert finite_word_capacity(3, length) == (3 ** (length + 1) - 3) // 2


def test_finite_roof_inventory_rank() -> None:
    assert finite_roof_inventory_rank([2, 3, 5, 7, 11]) == 5

