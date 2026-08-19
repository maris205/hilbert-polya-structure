#!/usr/bin/env python3
"""Independent formula-and-lattice checker for the C71 certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import gcd, lcm, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c71_complement_geometry_evidence.json"
SOURCES = {
    "c64": ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json",
    "c64_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/C64_PREFREEZE_MANIFEST.json",
    "c69": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_splitting/results/c69_defect_splitting_evidence.json",
    "c69_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_splitting/C69_PREFREEZE_MANIFEST.json",
    "c70": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_direct_factor_orbit/results/c70_direct_factor_orbit_evidence.json",
    "c70_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_direct_factor_orbit/C70_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c64": "7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212",
    "c64_manifest": "eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6",
    "c69": "388c250bc8eb475c5bb7bd556376e69d964c7820c5386cd1b51d09b984e136c9",
    "c69_manifest": "55ace9cd2236a4e053f8d4c1c66e21c686118a720f62662050622b612ff70f42",
    "c70": "aa25ed5a0bd2c6be5067f0d4ba385a00298ad3382322b7bcf9c1380b37bb373b",
    "c70_manifest": "fc5472d57bc186bcb4ef4b00a7053808623ec77cab9a924a32f6d69516a6beb1",
}
MATRIX_HASH = "4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
D_TYPE = (3, 1, 1)
K2_TYPE = (4, 2, 2, 2) + (1,) * 8
K3_TYPE = (2, 1)
IMAGE_TYPES = (
    (), (1,), (2,), (1, 1), (3,), (2, 1), (1, 1, 1),
    (3, 1), (2, 1, 1), (3, 1, 1),
)
TYPE_LABELS = {
    (): "0", (1,): "Z/2", (2,): "Z/4", (1, 1): "(Z/2)^2",
    (3,): "Z/8", (2, 1): "Z/2 + Z/4", (1, 1, 1): "(Z/2)^3",
    (3, 1): "Z/2 + Z/8", (2, 1, 1): "(Z/2)^2 + Z/4",
    (3, 1, 1): "Z/8 + (Z/2)^2",
}


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def conjugate(exponents: tuple[int, ...]) -> list[int]:
    return [sum(value >= level for value in exponents)
            for level in range(1, max(exponents, default=0) + 1)]


def gaussian_binomial(n: int, k: int, p: int = 2) -> int:
    assert 0 <= k <= n
    if k == 0:
        return 1
    numerator = prod(p ** (n - i) - 1 for i in range(k))
    denominator = prod(p ** (k - i) - 1 for i in range(k))
    assert numerator % denominator == 0
    return numerator // denominator


def subgroup_count(ambient: tuple[int, ...], subgroup: tuple[int, ...]) -> int:
    lam = conjugate(ambient)
    mu = conjugate(subgroup) + [0] * (len(lam) - len(conjugate(subgroup)) + 1)
    exponent = sum(mu[i + 1] * (lam[i] - mu[i]) for i in range(len(lam)))
    factors = [gaussian_binomial(lam[i] - mu[i + 1], mu[i] - mu[i + 1])
               for i in range(len(lam))]
    return 2 ** exponent * prod(factors)


def automorphism_order(exponents: tuple[int, ...]) -> int:
    if not exponents:
        return 1
    blocks = Counter(exponents)
    endomorphism_exponent = sum(min(a, b) for a in exponents for b in exponents)
    diagonal_dimension = sum(multiplicity ** 2 for multiplicity in blocks.values())
    invertible_blocks = prod(
        prod(2 ** multiplicity - 2 ** i for i in range(multiplicity))
        for multiplicity in blocks.values()
    )
    return 2 ** (endomorphism_exponent - diagonal_dimension) * invertible_blocks


def hom_order(source: tuple[int, ...], target: tuple[int, ...]) -> int:
    return 2 ** sum(min(a, b) for a in source for b in target)


def invert(matrix: list[list[int]]) -> list[list[Fraction]]:
    """Gauss-Jordan solve written independently from the producer."""
    dimension = len(matrix)
    augmented = [
        list(map(Fraction, row)) + [Fraction(row_index == column_index)
                                    for column_index in range(dimension)]
        for row_index, row in enumerate(matrix)
    ]
    for column in range(dimension):
        pivot = min(row for row in range(column, dimension)
                    if augmented[row][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        for entry in range(2 * dimension):
            augmented[column][entry] /= pivot_value
        for row in range(dimension):
            if row == column:
                continue
            coefficient = augmented[row][column]
            if coefficient:
                for entry in range(2 * dimension):
                    augmented[row][entry] -= coefficient * augmented[column][entry]
    return [row[dimension:] for row in augmented]


def residue_add(x: tuple[Fraction, ...], y: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple((a + b) % 1 for a, b in zip(x, y))


def residue_scale(n: int, x: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple((n * value) % 1 for value in x)


def generated_size(generators: tuple[tuple[Fraction, ...], ...]) -> int:
    subgroup = {tuple(Fraction(0) for _ in range(16))}
    for generator in generators:
        cyclic = {residue_scale(n, generator)
                  for n in range(lcm(*(entry.denominator for entry in generator)))}
        subgroup = {residue_add(x, y) for x in subgroup for y in cyclic}
    return len(subgroup)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    doc = json.loads(raw)
    assert raw == canon(doc)
    assert doc["schema_id"] == "hcs-c71-complement-geometry-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert doc["type_order"] == [f"S{i}" for i in range(1, 17)]
    assert {name: digest(path.read_bytes()) for name, path in SOURCES.items()} == HASHES
    assert doc["authority"] == {**HASHES, "c64_matrix_sha256": MATRIX_HASH}
    c64, c69, c70 = (json.loads(SOURCES[name].read_text()) for name in ("c64", "c69", "c70"))
    assert c64["matrix_sha256"] == MATRIX_HASH

    total = 2 ** sum(min(a, b) for a in K2_TYPE for b in D_TYPE)
    assert total == c69["complement_count"] == c70["complements_per_direct_factor"] == 2 ** 41
    expected_fixed = {
        "D_2_type": list(D_TYPE),
        "K_2_type": list(K2_TYPE),
        "K_3_type": list(K3_TYPE),
        "Hom_K_D_invariants": [2] * 32 + [4] * 3 + [8],
        "Hom_K_D_order": total,
    }
    assert doc["fixed_decomposition"] == expected_fixed
    assert doc["graph_model"] == {
        "complement_parameterization": "f in Hom(K,D) maps to Gamma_f={(f(k),k): k in K}",
        "fixed_complement": "Gamma_0",
        "intersection_index_definition": "[Gamma_f : Gamma_f intersect Gamma_g] = [K : ker(f-g)]",
        "intersection_quotient": "K/ker(f-g) is isomorphic to im(f-g)",
        "pairwise_intersection": "Gamma_f intersect Gamma_g is isomorphic to ker(f-g)",
        "translation_invariant_spectrum": True,
    }

    rows = []
    order_counts = Counter()
    type_counts = []
    index_counts = Counter()
    for image_type in IMAGE_TYPES:
        targets = subgroup_count(D_TYPE, image_type)
        source_copies = subgroup_count(K2_TYPE, image_type)
        epimorphisms = source_copies * automorphism_order(image_type)
        parameters = targets * epimorphisms
        image_order = 2 ** sum(image_type)
        order_counts[image_order] += targets
        type_counts.append({
            "image_type": TYPE_LABELS[image_type],
            "image_exponents": list(image_type),
            "count": targets,
        })
        row = {
            "image_type": TYPE_LABELS[image_type],
            "image_exponents": list(image_type),
            "image_order": image_order,
            "target_subgroup_count": targets,
            "homomorphisms_into_one_subgroup": hom_order(K2_TYPE, image_type),
            "surjections_onto_one_subgroup": epimorphisms,
            "parameter_count": parameters,
            "intersection_index": image_order,
            "ordered_pair_count": total * parameters,
            "unordered_distinct_pair_count": 0 if not image_type else total * parameters // 2,
        }
        rows.append(row)
        index_counts[image_order] += parameters
    assert doc["target_subgroup_poset"] == {
        "group_moduli": [8, 2, 2],
        "subgroup_count": sum(item["count"] for item in type_counts),
        "subgroup_counts_by_order": {str(order): count for order, count in sorted(order_counts.items())},
        "subgroup_counts_by_type": type_counts,
    }
    assert sum(item["count"] for item in type_counts) == 38
    assert doc["intersection_quotient_distribution"] == rows
    expected_spectrum = [
        {
            "index": index,
            "count_from_each_fixed_complement": count,
            "ordered_pair_count": total * count,
            "unordered_distinct_pair_count": 0 if index == 1 else total * count // 2,
        }
        for index, count in sorted(index_counts.items())
    ]
    assert doc["intersection_index_spectrum"] == expected_spectrum
    assert doc["spectrum_total"] == sum(index_counts.values()) == total

    expected_core = {
        "description": "intersection of all complements",
        "equals_8C": True,
        "primary_invariants": {"2": [2], "3": [3, 9]},
        "invariant_factors": [3, 18],
        "order": 54,
        "index_in_C": 2 ** 22,
    }
    assert doc["universal_core"] == expected_core
    full_image_count = next(row["parameter_count"] for row in rows
                            if row["image_exponents"] == list(D_TYPE))
    assert doc["complement_span"] == {
        "generated_subgroup": "C",
        "surjective_difference_count": full_image_count,
    }

    inverse_matrix = invert(c64["mark_matrix"])
    coordinate_orders = [lcm(*(inverse_matrix[row][column].denominator for row in range(16)))
                         for column in range(16)]
    residues = [tuple((8 * inverse_matrix[row][column]) % 1 for row in range(16))
                for column in range(16)]
    eight_orders = [lcm(*(entry.denominator for entry in residue)) for residue in residues]
    assert eight_orders == [order // gcd(order, 8) for order in coordinate_orders]
    serialized = [[fraction_text(value) for value in residue] for residue in residues]
    triples = []
    counts = {}
    for size in (1, 2, 3):
        generating = []
        for indices in combinations(range(16), size):
            if generated_size(tuple(residues[index] for index in indices)) == 54:
                generating.append([f"S{index + 1}" for index in indices])
        counts[str(size)] = len(generating)
        if size == 3:
            triples = generating
    expected_named = {
        "coordinate_orders_in_C": coordinate_orders,
        "eight_coordinate_orders": eight_orders,
        "eight_coordinate_residue_sha256": digest(canon(serialized)),
        "minimum_named_generator_count": 3,
        "generating_subset_counts_by_size": counts,
        "generating_triple_count": len(triples),
        "generating_triples": triples,
        "every_generating_triple_contains": "S9",
    }
    assert counts == {"1": 0, "2": 0, "3": 25}
    assert all("S9" in triple for triple in triples)
    assert doc["named_core_geometry"] == expected_named
    assert doc["claims"] == {
        "all_pair_intersection_quotient_types_classified": True,
        "arithmetic_local_claimed": False,
        "canonical_complement_claimed": False,
        "full_burnside_ring_claimed": False,
        "full_kernel_isomorphism_types_classified": False,
        "restricted_fixed_factor_complement_family_only": True,
    }
    print(json.dumps({
        "status": "PASS",
        "complement_count": total,
        "subgroup_poset_size": 38,
        "intersection_index_spectrum": dict(sorted(index_counts.items())),
        "universal_core": "Z/3 + Z/18",
        "generating_triple_count": len(triples),
        "full_image_count": full_image_count,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
