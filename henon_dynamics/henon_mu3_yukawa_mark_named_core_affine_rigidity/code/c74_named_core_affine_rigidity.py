#!/usr/bin/env python3
"""Produce the C74 named-core affine-rigidity certificate."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from itertools import product
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C72 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
OUT = PROJECT / "results/c74_named_core_affine_rigidity_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{i}" for i in range(1, 17))
MODULI = (9, 3, 2)
AUTHORITY = {
    "c72": "8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51",
    "c72_manifest": "5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b",
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def apply_matrix(matrix: tuple[int, int, int, int], point: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c, d = matrix
    x, y, z = point
    return ((a * x + 3 * b * y) % 9, (c * x + d * y) % 3, z)


def apply_affine(matrix: tuple[int, int, int, int], translation: tuple[int, int, int], point: tuple[int, int, int]) -> tuple[int, int, int]:
    image = apply_matrix(matrix, point)
    return tuple((value + shift) % modulus for value, shift, modulus in zip(image, translation, MODULI))


def is_bijection(matrix: tuple[int, int, int, int]) -> bool:
    points = list(product(range(9), range(3), range(2)))
    return len({apply_matrix(matrix, point) for point in points}) == len(points)


def overlap_multiset(source: Counter[tuple[int, int, int]], image: list[tuple[int, int, int]]) -> int:
    return sum((source & Counter(image)).values())


def main() -> None:
    paths = {
        "c72": C72 / "results/c72_coordinate_core_atlas_evidence.json",
        "c72_manifest": C72 / "C72_PREFREEZE_MANIFEST.json",
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c73_manifest": C73 / "C73_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c72 = json.loads(raw["c72"])
    c73 = json.loads(raw["c73"])
    assert c72["status"] == c73["status"] == "PREFREEZE_G3_PASS"
    assert c72["scope_literal"] == c73["scope_literal"] == FIREWALL
    assert c72["core"]["invariant_factors"] == [3, 18]
    coordinates = [tuple(row) for row in c72["coordinate_realization"]["coordinates"]]
    assert len(coordinates) == 16
    source = Counter(coordinates)
    support = set(coordinates)
    assert len(source) == 10
    assert sorted(source.values(), reverse=True) == [5, 2, 2, 1, 1, 1, 1, 1, 1, 1]

    # Every homomorphism of Z/9 + Z/3 has matrix [[a,3b],[c,d]].
    matrices = [
        (a, b, c, d)
        for a in range(9)
        for b, c, d in product(range(3), repeat=3)
        if is_bijection((a, b, c, d))
    ]
    assert len(matrices) == 108
    assert all(a % 3 != 0 and d % 3 != 0 for a, b, c, d in matrices)
    assert sum(
        1 for a in range(9) for b, c, d in product(range(3), repeat=3)
        if a % 3 != 0 and d % 3 != 0
    ) == 108
    translations = list(product(range(9), range(3), range(2)))
    affine_maps = [(matrix, translation) for matrix in matrices for translation in translations]
    assert len(affine_maps) == 5832

    multiset_stabilizers = []
    set_stabilizers = []
    linear_multiset_stabilizers = []
    linear_set_stabilizers = []
    multiset_distribution: Counter[int] = Counter()
    set_distribution: Counter[int] = Counter()
    nonidentity_witnesses = []
    identity = ((1, 0, 0, 1), (0, 0, 0))
    for matrix, translation in affine_maps:
        image = [apply_affine(matrix, translation, point) for point in coordinates]
        multiset_overlap = overlap_multiset(source, image)
        set_overlap = len(support & set(image))
        multiset_distribution[multiset_overlap] += 1
        set_distribution[set_overlap] += 1
        if Counter(image) == source:
            multiset_stabilizers.append((matrix, translation))
        if set(image) == support:
            set_stabilizers.append((matrix, translation))
        if translation == (0, 0, 0) and Counter(image) == source:
            linear_multiset_stabilizers.append(matrix)
        if translation == (0, 0, 0) and set(image) == support:
            linear_set_stabilizers.append(matrix)
        if (matrix, translation) != identity and multiset_overlap >= 14:
            nonidentity_witnesses.append({
                "matrix": list(matrix),
                "translation": list(translation),
                "multiset_overlap": multiset_overlap,
                "set_overlap": set_overlap,
            })
    assert multiset_stabilizers == [identity]
    assert set_stabilizers == [identity]
    assert linear_multiset_stabilizers == [(1, 0, 0, 1)]
    assert linear_set_stabilizers == [(1, 0, 0, 1)]
    assert max(multiset_distribution) == 16
    assert sum(count for overlap, count in multiset_distribution.items() if overlap < 16) == 5831
    assert max(overlap for overlap in multiset_distribution if overlap < 16) == 14
    assert multiset_distribution[14] == 2
    assert sorted(nonidentity_witnesses, key=lambda row: row["matrix"]) == [
        {"matrix": [4, 0, 2, 1], "translation": [0, 0, 0], "multiset_overlap": 14, "set_overlap": 8},
        {"matrix": [7, 0, 1, 1], "translation": [0, 0, 0], "multiset_overlap": 14, "set_overlap": 8},
    ]

    def distribution(counter: Counter[int]) -> dict[str, int]:
        return {str(key): counter[key] for key in sorted(counter)}

    result: dict[str, Any] = {
        "schema_id": "hcs-c74-named-core-affine-rigidity-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "type_order": list(LABELS),
        "core_model": {
            "ambient_group": "Z/9 + Z/3 + Z/2",
            "core_order": 54,
            "named_label_count": 16,
            "distinct_named_point_count": 10,
            "multiplicity_profile": [5, 2, 2, 1, 1, 1, 1, 1, 1, 1],
            "named_coordinate_sum": [3, 2, 1],
            "distinct_point_sum": [0, 0, 1],
        },
        "automorphism_model": {
            "odd_matrix_form": "(x,y) -> (a*x+3*b*y mod 9, c*x+d*y mod 3)",
            "parameter_ranges": "a in Z/9, b,c,d in Z/3",
            "automorphism_condition": "a mod 3 != 0 and d mod 3 != 0",
            "odd_endomorphism_matrix_count": 243,
            "full_core_endomorphism_count": 486,
            "automorphism_count": len(matrices),
            "affine_count": len(affine_maps),
            "bijection_enumeration": True,
        },
        "stabilizers": {
            "affine_multiset_stabilizer_count": len(multiset_stabilizers),
            "affine_set_stabilizer_count": len(set_stabilizers),
            "linear_multiset_stabilizer_count": len(linear_multiset_stabilizers),
            "linear_set_stabilizer_count": len(linear_set_stabilizers),
            "affine_multiset_stabilizer": [{"matrix": list(m), "translation": list(t)} for m, t in multiset_stabilizers],
            "affine_set_stabilizer": [{"matrix": list(m), "translation": list(t)} for m, t in set_stabilizers],
        },
        "overlap_distributions": {
            "multiset_overlap": distribution(multiset_distribution),
            "underlying_set_overlap": distribution(set_distribution),
        },
        "rigidity_margin": {
            "maximum_nonidentity_multiset_overlap": 14,
            "number_at_maximum": 2,
            "witnesses": nonidentity_witnesses,
            "maximum_nonidentity_underlying_set_overlap": 8,
            "named_multiset_orbit_size": len(affine_maps),
            "named_set_orbit_size": len(affine_maps),
            "linear_multiset_orbit_size": len(matrices),
            "linear_set_orbit_size": len(matrices),
        },
        "symmetry_boundary": {
            "c73_hypergraph_automorphism_order": c73["hypergraph_symmetry"]["abstract_hypergraph_automorphism_order"],
            "core_automorphism_order": len(matrices),
            "affine_group_order": len(affine_maps),
            "induced_named_affine_symmetry_order": 1,
            "identified_as_same_group": False,
            "label_fiber_permutation_order": 480,
            "label_fiber_note": "5! * 2! * 2! permutes duplicate labels after the point map is fixed; it is not an affine symmetry",
        },
        "claims": {
            "named_multiset_rigidity_proved": True,
            "underlying_set_rigidity_proved": True,
            "hypergraph_automorphisms_are_affine_core_automorphisms_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    result["overlap_distributions"]["multiset_overlap"] = distribution(multiset_distribution)
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "automorphism_count": len(matrices),
        "affine_count": len(affine_maps),
        "multiset_stabilizer": len(multiset_stabilizers),
        "set_stabilizer": len(set_stabilizers),
        "max_nonidentity_overlap": 14,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
