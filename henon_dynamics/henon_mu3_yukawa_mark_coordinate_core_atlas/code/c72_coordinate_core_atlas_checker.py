#!/usr/bin/env python3
"""Independent lattice-and-group checker for the C72 coordinate atlas."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from functools import cache
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd, lcm
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c72_coordinate_core_atlas_evidence.json"
SOURCES = {
    "c64": ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json",
    "c64_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json",
    "c71": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/results/c71_complement_geometry_evidence.json",
    "c71_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/C71_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c64": "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212",
    "c64_manifest": "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6",
    "c71": "a7498081bed5a6f8177825e4d556084bd2421da613ed22835c31e537c49579bc",
    "c71_manifest": "d5ec7bf6bc36cc87dcc2f23c838b0ae7ac997b3c442c0640f486b813fb431715",
}
MODULI = (9, 3, 2)
TYPE_ORDER = (
    "1", "Z/2", "Z/3", "Z/6", "(Z/3)^2", "Z/9", "Z/18",
    "Z/3 + Z/6", "Z/3 + Z/9", "Z/3 + Z/18",
)
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def plus(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % modulus for a, b, modulus in zip(left, right, MODULI))


def scale(coefficient: int, value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(coefficient * a % modulus for a, modulus in zip(value, MODULI))


@cache
def order(value: tuple[int, ...]) -> int:
    return lcm(*(modulus // gcd(modulus, a) for a, modulus in zip(value, MODULI)))


@cache
def adjoin(
    subgroup: frozenset[tuple[int, ...]], generator: tuple[int, ...]
) -> frozenset[tuple[int, ...]]:
    return frozenset(
        plus(value, scale(coefficient, generator))
        for value in subgroup for coefficient in range(order(generator))
    )


@cache
def classify(subgroup: frozenset[tuple[int, ...]]) -> str:
    two_part = [value for value in subgroup if order(value) in (1, 2)]
    three_part = [value for value in subgroup if order(value) in (1, 3, 9)]
    assert len(two_part) * len(three_part) == len(subgroup)
    has_two = len(two_part) == 2
    three_size = len(three_part)
    three_exponent = max(order(value) for value in three_part)
    three_rank = 0
    killed_by_three = sum(scale(3, value) == (0, 0, 0) for value in three_part)
    while 3 ** three_rank < killed_by_three:
        three_rank += 1
    three_label = {
        (1, 1, 0): "1",
        (3, 3, 1): "Z/3",
        (9, 3, 2): "(Z/3)^2",
        (9, 9, 1): "Z/9",
        (27, 9, 2): "Z/3 + Z/9",
    }[(three_size, three_exponent, three_rank)]
    if not has_two:
        return three_label
    return {
        "1": "Z/2",
        "Z/3": "Z/6",
        "(Z/3)^2": "Z/3 + Z/6",
        "Z/9": "Z/18",
        "Z/3 + Z/9": "Z/3 + Z/18",
    }[three_label]


def all_subgroups() -> set[frozenset[tuple[int, ...]]]:
    elements = [tuple(value) for value in product(*(range(modulus) for modulus in MODULI))]
    trivial = frozenset({(0, 0, 0)})
    seen = {trivial}
    pending = deque([trivial])
    while pending:
        subgroup = pending.popleft()
        for generator in elements:
            candidate = adjoin(subgroup, generator)
            if candidate not in seen:
                seen.add(candidate)
                pending.append(candidate)
    return seen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    document = json.loads(raw)
    assert raw == canon(document)
    assert document["schema_id"] == "hcs-c72-coordinate-core-atlas-prefreeze-v1"
    assert document["status"] == "PREFREEZE_G3_PASS"
    assert document["scope_literal"] == FIREWALL
    assert {name: digest(path.read_bytes()) for name, path in SOURCES.items()} == HASHES
    assert document["authority"] == HASHES
    c64 = json.loads(SOURCES["c64"].read_text())
    c71 = json.loads(SOURCES["c71"].read_text())

    matrix = sp.Matrix(c64["mark_matrix"])
    core_lattice = hermite_normal_form(matrix.row_join(8 * sp.eye(16)))
    basis_columns = sp.zeros(16, 3)
    for column, row in enumerate((0, 2, 8)):
        basis_columns[row, column] = 8
    basis_lattice = hermite_normal_form(matrix.row_join(basis_columns))
    assert basis_lattice == core_lattice
    assert abs(int(matrix.det())) // abs(int(core_lattice.det())) == 54

    realization = document["coordinate_realization"]
    assert realization["basis"] == ["8[S1]", "8[S3]", "8[S9]"]
    assert realization["basis_moduli"] == list(MODULI)
    assert realization["ambient_model"] == "Z/9 + Z/3 + Z/2"
    coordinates = [tuple(value) for value in realization["coordinates"]]
    assert len(coordinates) == 16
    matrix_inverse = matrix.inv()
    for index, coordinate in enumerate(coordinates):
        difference = sp.zeros(16, 1)
        difference[index, 0] = 8
        for coefficient, basis_index in zip(coordinate, (0, 2, 8)):
            difference[basis_index, 0] -= 8 * coefficient
        solution = matrix_inverse * difference
        assert all(value.q == 1 for value in solution)
    assert realization["coordinates_sha256"] == digest(canon([list(value) for value in coordinates]))
    coordinate_orders = [order(value) for value in coordinates]
    assert realization["orders"] == coordinate_orders
    assert coordinate_orders == c71["named_core_geometry"]["eight_coordinate_orders"]
    assert realization["zero_coordinate_labels"] == ["S5", "S6", "S10", "S13", "S14"]

    trivial = frozenset({(0, 0, 0)})
    subgroups = [trivial] * (1 << 16)
    profile = {size: Counter() for size in range(17)}
    for mask in range(1 << 16):
        if mask:
            highest = mask.bit_length() - 1
            subgroups[mask] = adjoin(subgroups[mask ^ (1 << highest)], coordinates[highest])
        profile[mask.bit_count()][classify(subgroups[mask])] += 1
    reached = set(subgroups)
    complete_lattice = all_subgroups()
    assert reached == complete_lattice and len(reached) == 20
    type_counts = Counter(classify(subgroup) for subgroup in complete_lattice)

    assert document["type_order"] == [f"S{index}" for index in range(1, 17)]
    assert document["core"] == {
        "description": "8C, the C71 universal complement core",
        "invariant_factors": [3, 18],
        "order": 54,
        "abstract_minimum_generator_count": 2,
    }
    atlas = document["subgroup_lattice_atlas"]
    assert atlas["all_subgroup_count"] == atlas["reached_subgroup_count"] == 20
    assert atlas["every_subgroup_reached_by_named_support"] is True
    assert atlas["type_rows"] == [
        {
            "type": name,
            "subgroup_count_in_core": type_counts[name],
            "reached_subgroup_count": sum(classify(group) == name for group in reached),
        }
        for name in TYPE_ORDER
    ]

    support_atlas = document["support_atlas"]
    assert support_atlas["subset_count"] == 65536
    assert support_atlas["type_column_order"] == list(TYPE_ORDER)
    expected_rows = []
    for size in range(17):
        assert sum(profile[size].values()) == comb(16, size)
        expected_rows.append({
            "support_size": size,
            "type_counts": {name: profile[size][name] for name in TYPE_ORDER},
            "total": comb(16, size),
        })
    assert support_atlas["rows"] == expected_rows

    full = frozenset(tuple(value) for value in product(*(range(modulus) for modulus in MODULI)))
    coefficients = {
        str(size): sum(group == full for mask, group in enumerate(subgroups)
                       if mask.bit_count() == size)
        for size in range(17)
    }
    coefficients = {size: count for size, count in coefficients.items() if count}
    minimal = []
    for mask, subgroup in enumerate(subgroups):
        if subgroup != full:
            continue
        if all(subgroups[mask ^ (1 << bit)] != full
               for bit in range(16) if mask & (1 << bit)):
            minimal.append([f"S{bit + 1}" for bit in range(16) if mask & (1 << bit)])
    minimal.sort(key=lambda support: [int(label[1:]) for label in support])
    generation = document["generation_complex"]
    assert generation == {
        "named_minimum_generator_count": 3,
        "generating_support_polynomial_coefficients": coefficients,
        "minimal_generating_support_count": 25,
        "minimal_generating_supports": minimal,
        "every_minimal_support_contains": "S9",
    }
    assert minimal == c71["named_core_geometry"]["generating_triples"]
    assert document["claims"] == {
        "all_65536_named_supports_classified": True,
        "entire_core_subgroup_lattice_reached": True,
        "coordinate_atlas_is_presentation_dependent": True,
        "abstract_generator_rank_three_claimed": False,
        "canonical_smith_coordinates_claimed": False,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "PASS",
        "subset_count": 65536,
        "core_subgroup_count": 20,
        "all_subgroups_reached": True,
        "minimal_generating_support_count": len(minimal),
        "generation_coefficients": coefficients,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
