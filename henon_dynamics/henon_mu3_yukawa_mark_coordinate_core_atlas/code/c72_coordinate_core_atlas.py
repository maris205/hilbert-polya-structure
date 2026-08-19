#!/usr/bin/env python3
"""Produce the exhaustive C72 named-coordinate atlas of the C71 core."""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from functools import cache
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd, lcm
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks"
C71 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry"
OUT = PROJECT / "results/c72_coordinate_core_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
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


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def inverse(matrix: list[list[int]]) -> list[list[Fraction]]:
    size = len(matrix)
    work = [
        [Fraction(value) for value in row]
        + [Fraction(i == j) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        scale = work[column][column]
        work[column] = [value / scale for value in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [x - scale * y for x, y in zip(work[row], work[column])]
    return [row[size:] for row in work]


def mod_one(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient: int, value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


@cache
def element_order(value: tuple[int, ...]) -> int:
    orders = [modulus // gcd(modulus, x) for x, modulus in zip(value, MODULI)]
    return lcm(*orders)


@cache
def cyclic_subgroup(value: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    return frozenset(multiple(coefficient, value) for coefficient in range(element_order(value)))


@cache
def extend(
    subgroup: frozenset[tuple[int, ...]], cyclic: frozenset[tuple[int, ...]]
) -> frozenset[tuple[int, ...]]:
    return frozenset(add(left, right) for left in subgroup for right in cyclic)


@cache
def subgroup_type(subgroup: frozenset[tuple[int, ...]]) -> str:
    order = len(subgroup)
    exponent = max(element_order(value) for value in subgroup)
    lookup = {
        (1, 1): "1",
        (2, 2): "Z/2",
        (3, 3): "Z/3",
        (6, 6): "Z/6",
        (9, 3): "(Z/3)^2",
        (9, 9): "Z/9",
        (18, 18): "Z/18",
        (18, 6): "Z/3 + Z/6",
        (27, 9): "Z/3 + Z/9",
        (54, 18): "Z/3 + Z/18",
    }
    assert (order, exponent) in lookup
    return lookup[(order, exponent)]


def enumerate_all_subgroups() -> set[frozenset[tuple[int, ...]]]:
    elements = [tuple(value) for value in product(*(range(modulus) for modulus in MODULI))]
    cyclics = {value: cyclic_subgroup(value) for value in elements}
    zero = frozenset({(0, 0, 0)})
    found = {zero}
    queue = deque([zero])
    while queue:
        subgroup = queue.popleft()
        for value in elements:
            enlarged = extend(subgroup, cyclics[value])
            if enlarged not in found:
                found.add(enlarged)
                queue.append(enlarged)
    return found


def find_coordinates(
    residues: list[tuple[Fraction, ...]], basis_indices: tuple[int, int, int]
) -> list[tuple[int, int, int]]:
    basis = [residues[index] for index in basis_indices]
    coordinates = []
    for target in residues:
        matches = []
        for coefficients in product(*(range(modulus) for modulus in MODULI)):
            candidate = tuple(
                mod_one(sum((Fraction(c) * basis[j][row]
                             for j, c in enumerate(coefficients)), Fraction(0)))
                for row in range(len(target))
            )
            if candidate == target:
                matches.append(tuple(coefficients))
        assert len(matches) == 1
        coordinates.append(matches[0])
    return coordinates


def main() -> None:
    paths = {
        "c64": C64 / "results/c64_mark_evidence.json",
        "c64_manifest": C64 / "C64_PREFREEZE_MANIFEST.json",
        "c71": C71 / "results/c71_complement_geometry_evidence.json",
        "c71_manifest": C71 / "C71_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c64 = json.loads(raw["c64"])
    c71 = json.loads(raw["c71"])
    assert c64["status"] == c71["status"] == "PREFREEZE_G3_PASS"
    assert c64["scope_literal"] == c71["scope_literal"] == FIREWALL
    assert c71["universal_core"] == {
        "description": "intersection of all complements",
        "equals_8C": True,
        "primary_invariants": {"2": [2], "3": [3, 9]},
        "invariant_factors": [3, 18],
        "order": 54,
        "index_in_C": 2 ** 22,
    }

    matrix = c64["mark_matrix"]
    matrix_inverse = inverse(matrix)
    residues = [
        tuple(mod_one(8 * matrix_inverse[row][column]) for row in range(16))
        for column in range(16)
    ]
    coordinates = find_coordinates(residues, (0, 2, 8))
    expected_coordinates = [
        (1, 0, 0), (6, 0, 0), (0, 1, 0), (3, 1, 0),
        (0, 0, 0), (0, 0, 0), (4, 2, 0), (3, 2, 0),
        (0, 0, 1), (0, 0, 0), (0, 1, 0), (3, 1, 0),
        (0, 0, 0), (0, 0, 0), (2, 1, 0), (8, 2, 0),
    ]
    assert coordinates == expected_coordinates
    orders = [element_order(value) for value in coordinates]
    assert orders == c71["named_core_geometry"]["eight_coordinate_orders"]

    cyclics = [cyclic_subgroup(value) for value in coordinates]
    zero = frozenset({(0, 0, 0)})
    support_subgroups: list[frozenset[tuple[int, ...]]] = [zero] * (1 << 16)
    profile = {size: Counter() for size in range(17)}
    for mask in range(1 << 16):
        if mask:
            bit = (mask & -mask).bit_length() - 1
            support_subgroups[mask] = extend(
                support_subgroups[mask ^ (1 << bit)], cyclics[bit]
            )
        profile[mask.bit_count()][subgroup_type(support_subgroups[mask])] += 1

    reached = set(support_subgroups)
    all_subgroups = enumerate_all_subgroups()
    assert reached == all_subgroups
    assert len(all_subgroups) == 20
    subgroup_type_counts = Counter(subgroup_type(group) for group in all_subgroups)
    assert subgroup_type_counts == Counter({
        "1": 1, "Z/2": 1, "Z/3": 4, "Z/6": 4,
        "(Z/3)^2": 1, "Z/9": 3, "Z/18": 3,
        "Z/3 + Z/6": 1, "Z/3 + Z/9": 1, "Z/3 + Z/18": 1,
    })
    for size in range(17):
        assert sum(profile[size].values()) == comb(16, size)

    full = "Z/3 + Z/18"
    generation_coefficients = {
        str(size): profile[size][full]
        for size in range(17) if profile[size][full]
    }
    assert generation_coefficients == {
        "3": 25, "4": 224, "5": 940, "6": 2461, "7": 4504,
        "8": 6095, "9": 6269, "10": 4950, "11": 2992,
        "12": 1364, "13": 455, "14": 105, "15": 15, "16": 1,
    }
    minimal_generating_supports = []
    for mask, subgroup in enumerate(support_subgroups):
        if len(subgroup) != 54:
            continue
        if all(
            len(support_subgroups[mask ^ (1 << bit)]) < 54
            for bit in range(16) if mask & (1 << bit)
        ):
            minimal_generating_supports.append(
                [f"S{bit + 1}" for bit in range(16) if mask & (1 << bit)]
            )
    minimal_generating_supports.sort(key=lambda support: [int(label[1:]) for label in support])
    assert minimal_generating_supports == c71["named_core_geometry"]["generating_triples"]

    result: dict[str, Any] = {
        "schema_id": "hcs-c72-coordinate-core-atlas-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "type_order": [f"S{index}" for index in range(1, 17)],
        "core": {
            "description": "8C, the C71 universal complement core",
            "invariant_factors": [3, 18],
            "order": 54,
            "abstract_minimum_generator_count": 2,
        },
        "coordinate_realization": {
            "basis": ["8[S1]", "8[S3]", "8[S9]"],
            "basis_moduli": list(MODULI),
            "ambient_model": "Z/9 + Z/3 + Z/2",
            "coordinates": [list(value) for value in coordinates],
            "coordinates_sha256": digest(canonical([list(value) for value in coordinates])),
            "orders": orders,
            "zero_coordinate_labels": ["S5", "S6", "S10", "S13", "S14"],
        },
        "subgroup_lattice_atlas": {
            "all_subgroup_count": len(all_subgroups),
            "reached_subgroup_count": len(reached),
            "every_subgroup_reached_by_named_support": reached == all_subgroups,
            "type_rows": [
                {
                    "type": type_name,
                    "subgroup_count_in_core": subgroup_type_counts[type_name],
                    "reached_subgroup_count": sum(
                        subgroup_type(group) == type_name for group in reached
                    ),
                }
                for type_name in TYPE_ORDER
            ],
        },
        "support_atlas": {
            "subset_count": 1 << 16,
            "type_column_order": list(TYPE_ORDER),
            "rows": [
                {
                    "support_size": size,
                    "type_counts": {
                        type_name: profile[size][type_name] for type_name in TYPE_ORDER
                    },
                    "total": comb(16, size),
                }
                for size in range(17)
            ],
        },
        "generation_complex": {
            "named_minimum_generator_count": 3,
            "generating_support_polynomial_coefficients": generation_coefficients,
            "minimal_generating_support_count": len(minimal_generating_supports),
            "minimal_generating_supports": minimal_generating_supports,
            "every_minimal_support_contains": "S9",
        },
        "claims": {
            "all_65536_named_supports_classified": True,
            "entire_core_subgroup_lattice_reached": True,
            "coordinate_atlas_is_presentation_dependent": True,
            "abstract_generator_rank_three_claimed": False,
            "canonical_smith_coordinates_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "subset_count": 1 << 16,
        "core_subgroup_count": len(all_subgroups),
        "all_subgroups_reached": reached == all_subgroups,
        "minimal_generating_support_count": len(minimal_generating_supports),
        "generating_support_coefficients": generation_coefficients,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
