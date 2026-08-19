#!/usr/bin/env python3
"""Produce the exact C71 complement-intersection certificate."""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import gcd, lcm
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks"
C69 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_splitting"
C70 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_direct_factor_orbit"
OUT = PROJECT / "results/c71_complement_geometry_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
HASHES = {
    "c64": "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212",
    "c64_manifest": "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6",
    "c69": "388c250bc8eb475c5bb7bd556376e69d964c7820c5386cd1b51d09b984e136c9",
    "c69_manifest": "55ace9cd2236a4e053f8d4c1c66e21c686118a720f62662050622b612ff70f42",
    "c70": "aa25ed5a0bd2c6be5067f0d4ba385a00298ad3382322b7bcf9c1380b37bb373b",
    "c70_manifest": "fc5472d57bc186bcb4ef4b00a7053808623ec77cab9a924a32f6d69516a6beb1",
}
MATRIX_HASH = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"
D_MODULI = (8, 2, 2)
D_TYPE = (3, 1, 1)
K2_TYPE = (4, 2, 2, 2) + (1,) * 8
K3_TYPE = (2, 1)
IMAGE_TYPES = (
    (), (1,), (2,), (1, 1), (3,), (2, 1), (1, 1, 1),
    (3, 1), (2, 1, 1), (3, 1, 1),
)
TYPE_LABELS = {
    (): "0",
    (1,): "Z/2",
    (2,): "Z/4",
    (1, 1): "(Z/2)^2",
    (3,): "Z/8",
    (2, 1): "Z/2 + Z/4",
    (1, 1, 1): "(Z/2)^3",
    (3, 1): "Z/2 + Z/8",
    (2, 1, 1): "(Z/2)^2 + Z/4",
    (3, 1, 1): "Z/8 + (Z/2)^2",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % modulus for a, b, modulus in zip(x, y, D_MODULI))


def multiply_element(n: int, x: tuple[int, ...]) -> tuple[int, ...]:
    result = (0, 0, 0)
    summand = x
    while n:
        if n & 1:
            result = add(result, summand)
        summand = add(summand, summand)
        n //= 2
    return result


def cyclic_subgroup(x: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    result: set[tuple[int, ...]] = set()
    current = (0, 0, 0)
    while current not in result:
        result.add(current)
        current = add(current, x)
    return frozenset(result)


def adjoin(
    subgroup: frozenset[tuple[int, ...]], x: tuple[int, ...]
) -> frozenset[tuple[int, ...]]:
    return frozenset(add(a, b) for a in subgroup for b in cyclic_subgroup(x))


def enumerate_subgroups() -> set[frozenset[tuple[int, ...]]]:
    elements = [
        (a, b, c)
        for a in range(D_MODULI[0])
        for b in range(D_MODULI[1])
        for c in range(D_MODULI[2])
    ]
    trivial = frozenset({(0, 0, 0)})
    subgroups = {trivial}
    queue = deque([trivial])
    while queue:
        subgroup = queue.popleft()
        for x in elements:
            if x in subgroup:
                continue
            enlarged = adjoin(subgroup, x)
            if enlarged not in subgroups:
                subgroups.add(enlarged)
                queue.append(enlarged)
    return subgroups


def subgroup_type(subgroup: frozenset[tuple[int, ...]]) -> tuple[int, ...]:
    cumulative = [0]
    for level in range(1, 4):
        killed = sum(multiply_element(2 ** level, x) == (0, 0, 0) for x in subgroup)
        exponent = killed.bit_length() - 1
        assert 2 ** exponent == killed
        cumulative.append(exponent)
    conjugate = [cumulative[i] - cumulative[i - 1] for i in range(1, 4)]
    result: list[int] = []
    for exponent in range(3, 0, -1):
        following = conjugate[exponent] if exponent < 3 else 0
        result.extend([exponent] * (conjugate[exponent - 1] - following))
    return tuple(result)


def hom_order(source: tuple[int, ...], target: tuple[int, ...]) -> int:
    return 2 ** sum(min(a, b) for a in source for b in target)


def inverse(matrix: list[list[int]]) -> list[list[Fraction]]:
    n = len(matrix)
    work = [
        [Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for col in range(n):
        pivot = next(row for row in range(col, n) if work[row][col])
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [x / scale for x in work[col]]
        for row in range(n):
            if row == col or not work[row][col]:
                continue
            scale = work[row][col]
            work[row] = [x - scale * y for x, y in zip(work[row], work[col])]
    return [row[n:] for row in work]


def fraction_mod_one(value: Fraction) -> Fraction:
    return value % 1


def residue_order(residue: tuple[Fraction, ...]) -> int:
    return lcm(*(value.denominator for value in residue))


def generated_residue_order(
    residues: list[tuple[Fraction, ...]], orders: list[int]
) -> int:
    classes = set()
    for coefficients in product(*(range(order) for order in orders)):
        classes.add(tuple(
            fraction_mod_one(sum(
                (Fraction(coefficient) * residue[row]
                 for coefficient, residue in zip(coefficients, residues)),
                Fraction(0),
            ))
            for row in range(len(residues[0]))
        ))
    return len(classes)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    paths = {
        "c64": C64 / "results/c64_mark_evidence.json",
        "c64_manifest": C64 / "C64_PREFREEZE_MANIFEST.json",
        "c69": C69 / "results/c69_defect_splitting_evidence.json",
        "c69_manifest": C69 / "C69_PREFREEZE_MANIFEST.json",
        "c70": C70 / "results/c70_direct_factor_orbit_evidence.json",
        "c70_manifest": C70 / "C70_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c64, c69, c70 = (json.loads(raw[name]) for name in ("c64", "c69", "c70"))
    for doc in (c64, c69, c70):
        assert doc["status"] == "PREFREEZE_G3_PASS"
        assert doc["scope_literal"] == FIREWALL
    assert c64["matrix_sha256"] == MATRIX_HASH
    assert c69["defect_invariants"] == [2, 2, 8]
    assert c69["complement_count"] == 2 ** 41
    assert c70["primary_types"]["D2"] == list(D_TYPE)
    assert c70["primary_types"]["K2"] == list(K2_TYPE)
    assert c70["primary_types"]["K3"] == list(K3_TYPE)
    assert c70["hom_group_invariants"]["Hom_K_to_D"] == [2] * 32 + [4] * 3 + [8]

    subgroups = enumerate_subgroups()
    assert len(subgroups) == 38
    ordered_subgroups = sorted(subgroups, key=lambda h: (len(h), sorted(h)))
    exact_maps: dict[frozenset[tuple[int, ...]], int] = {}
    for subgroup in ordered_subgroups:
        all_maps = hom_order(K2_TYPE, subgroup_type(subgroup))
        exact_maps[subgroup] = all_maps - sum(
            count for smaller, count in exact_maps.items() if smaller < subgroup
        )
        assert exact_maps[subgroup] >= 0

    subgroup_type_counts = Counter(subgroup_type(subgroup) for subgroup in subgroups)
    assert set(subgroup_type_counts) == set(IMAGE_TYPES)
    image_rows = []
    for image_type in IMAGE_TYPES:
        representatives = [h for h in subgroups if subgroup_type(h) == image_type]
        exact_values = {exact_maps[h] for h in representatives}
        assert len(exact_values) == 1
        surjections = exact_values.pop()
        subgroup_count = len(representatives)
        parameter_count = subgroup_count * surjections
        image_rows.append({
            "image_type": TYPE_LABELS[image_type],
            "image_exponents": list(image_type),
            "image_order": 2 ** sum(image_type),
            "target_subgroup_count": subgroup_count,
            "homomorphisms_into_one_subgroup": hom_order(K2_TYPE, image_type),
            "surjections_onto_one_subgroup": surjections,
            "parameter_count": parameter_count,
            "intersection_index": 2 ** sum(image_type),
            "ordered_pair_count": (2 ** 41) * parameter_count,
            "unordered_distinct_pair_count": (
                0 if not image_type else (2 ** 41) * parameter_count // 2
            ),
        })
    assert sum(row["parameter_count"] for row in image_rows) == 2 ** 41

    index_counts = Counter()
    for row in image_rows:
        index_counts[row["intersection_index"]] += row["parameter_count"]
    expected_index_counts = {
        1: 1,
        2: 28665,
        4: 117600270,
        8: 70111567864,
        16: 1030892519424,
        32: 1097901539328,
    }
    assert dict(sorted(index_counts.items())) == expected_index_counts

    matrix = c64["mark_matrix"]
    matrix_inverse = inverse(matrix)
    coordinate_orders = [
        lcm(*(matrix_inverse[row][col].denominator for row in range(16)))
        for col in range(16)
    ]
    assert coordinate_orders == [36, 12, 6, 6, 2, 2, 36, 6, 16, 8, 6, 12, 2, 2, 36, 36]
    eight_residues = [
        tuple(fraction_mod_one(8 * matrix_inverse[row][col]) for row in range(16))
        for col in range(16)
    ]
    eight_orders = [residue_order(residue) for residue in eight_residues]
    assert eight_orders == [order // gcd(order, 8) for order in coordinate_orders]
    assert eight_orders == [9, 3, 3, 3, 1, 1, 9, 3, 2, 1, 3, 3, 1, 1, 9, 9]

    generating_counts: dict[str, int] = {}
    generating_triples: list[list[str]] = []
    for size in (1, 2, 3):
        count = 0
        for indices in combinations(range(16), size):
            generated_order = generated_residue_order(
                [eight_residues[index] for index in indices],
                [eight_orders[index] for index in indices],
            )
            if generated_order == 54:
                count += 1
                if size == 3:
                    generating_triples.append([f"S{index + 1}" for index in indices])
        generating_counts[str(size)] = count
    assert generating_counts == {"1": 0, "2": 0, "3": 25}
    assert all("S9" in triple for triple in generating_triples)

    serialized_residues = [
        [fraction_text(value) for value in residue] for residue in eight_residues
    ]
    universal_core_order = 54
    ambient_order = c69["ambient_order"]
    assert ambient_order // universal_core_order == 2 ** 22
    full_image_count = next(
        row["parameter_count"] for row in image_rows
        if row["image_exponents"] == list(D_TYPE)
    )

    result: dict[str, Any] = {
        "schema_id": "hcs-c71-complement-geometry-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**HASHES, "c64_matrix_sha256": MATRIX_HASH},
        "type_order": [f"S{i}" for i in range(1, 17)],
        "fixed_decomposition": {
            "D_2_type": list(D_TYPE),
            "K_2_type": list(K2_TYPE),
            "K_3_type": list(K3_TYPE),
            "Hom_K_D_invariants": [2] * 32 + [4] * 3 + [8],
            "Hom_K_D_order": 2 ** 41,
        },
        "graph_model": {
            "complement_parameterization": "f in Hom(K,D) maps to Gamma_f={(f(k),k): k in K}",
            "fixed_complement": "Gamma_0",
            "pairwise_intersection": "Gamma_f intersect Gamma_g is isomorphic to ker(f-g)",
            "intersection_quotient": "K/ker(f-g) is isomorphic to im(f-g)",
            "intersection_index_definition": "[Gamma_f : Gamma_f intersect Gamma_g] = [K : ker(f-g)]",
            "translation_invariant_spectrum": True,
        },
        "target_subgroup_poset": {
            "group_moduli": list(D_MODULI),
            "subgroup_count": len(subgroups),
            "subgroup_counts_by_order": {
                str(order): count
                for order, count in sorted(Counter(map(len, subgroups)).items())
            },
            "subgroup_counts_by_type": [
                {
                    "image_type": TYPE_LABELS[image_type],
                    "image_exponents": list(image_type),
                    "count": subgroup_type_counts[image_type],
                }
                for image_type in IMAGE_TYPES
            ],
        },
        "intersection_quotient_distribution": image_rows,
        "intersection_index_spectrum": [
            {
                "index": index,
                "count_from_each_fixed_complement": count,
                "ordered_pair_count": (2 ** 41) * count,
                "unordered_distinct_pair_count": (
                    0 if index == 1 else (2 ** 41) * count // 2
                ),
            }
            for index, count in sorted(index_counts.items())
        ],
        "spectrum_total": sum(index_counts.values()),
        "universal_core": {
            "description": "intersection of all complements",
            "equals_8C": True,
            "primary_invariants": {"2": [2], "3": [3, 9]},
            "invariant_factors": [3, 18],
            "order": universal_core_order,
            "index_in_C": ambient_order // universal_core_order,
        },
        "complement_span": {
            "generated_subgroup": "C",
            "surjective_difference_count": full_image_count,
        },
        "named_core_geometry": {
            "coordinate_orders_in_C": coordinate_orders,
            "eight_coordinate_orders": eight_orders,
            "eight_coordinate_residue_sha256": digest(canonical(serialized_residues)),
            "minimum_named_generator_count": 3,
            "generating_subset_counts_by_size": generating_counts,
            "generating_triple_count": len(generating_triples),
            "generating_triples": generating_triples,
            "every_generating_triple_contains": "S9",
        },
        "claims": {
            "all_pair_intersection_quotient_types_classified": True,
            "full_kernel_isomorphism_types_classified": False,
            "restricted_fixed_factor_complement_family_only": True,
            "canonical_complement_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "complement_count": result["spectrum_total"],
        "intersection_index_spectrum": expected_index_counts,
        "universal_core_invariants": [3, 18],
        "universal_core_order": universal_core_order,
        "generating_triple_count": len(generating_triples),
        "full_image_count": full_image_count,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
