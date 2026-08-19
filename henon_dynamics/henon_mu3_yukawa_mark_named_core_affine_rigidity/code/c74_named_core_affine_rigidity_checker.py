#!/usr/bin/env python3
"""Independent finite-group checker for the C74 affine-rigidity certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
SOURCES = {
    "c72": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/results/c72_coordinate_core_atlas_evidence.json",
    "c72_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/C72_PREFREEZE_MANIFEST.json",
    "c73": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/results/c73_generation_blocker_reliability_evidence.json",
    "c73_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/C73_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c72": "8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51",
    "c72_manifest": "5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b",
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
}
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{i}" for i in range(1, 17))
MODULI = (9, 3, 2)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def matrix_image(matrix: tuple[int, int, int, int], point: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c, d = matrix
    x, y, z = point
    return ((a * x + 3 * b * y) % 9, (c * x + d * y) % 3, z)


def affine_image(matrix: tuple[int, int, int, int], translation: tuple[int, int, int], point: tuple[int, int, int]) -> tuple[int, int, int]:
    image = matrix_image(matrix, point)
    return tuple((value + shift) % modulus for value, shift, modulus in zip(image, translation, MODULI))


def enumerate_aut() -> list[tuple[int, int, int, int]]:
    points = list(product(range(9), range(3), range(2)))
    result = []
    # Independent bijectivity test, rather than trusting a determinant formula.
    for a in range(9):
        for b, c, d in product(range(3), repeat=3):
            matrix = (a, b, c, d)
            if len({matrix_image(matrix, point) for point in points}) == len(points):
                result.append(matrix)
    return result


def overlap(source: Counter[tuple[int, int, int]], image: list[tuple[int, int, int]]) -> int:
    return sum((source & Counter(image)).values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=PROJECT / "results/c74_named_core_affine_rigidity_evidence.json")
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    document = json.loads(raw)
    assert raw == canonical(document)
    assert document["schema_id"] == "hcs-c74-named-core-affine-rigidity-prefreeze-v1"
    assert document["status"] == "PREFREEZE_G3_PASS"
    assert document["scope_literal"] == FIREWALL
    assert {name: digest(path.read_bytes()) for name, path in SOURCES.items()} == HASHES
    assert document["authority"] == HASHES
    c72 = json.loads(SOURCES["c72"].read_text())
    c73 = json.loads(SOURCES["c73"].read_text())
    coordinates = [tuple(row) for row in c72["coordinate_realization"]["coordinates"]]
    source = Counter(coordinates)
    support = set(coordinates)
    assert len(coordinates) == 16 and len(source) == 10
    assert document["core_model"] == {
        "ambient_group": "Z/9 + Z/3 + Z/2",
        "core_order": 54,
        "named_label_count": 16,
        "distinct_named_point_count": 10,
        "multiplicity_profile": [5, 2, 2, 1, 1, 1, 1, 1, 1, 1],
        "named_coordinate_sum": [3, 2, 1],
        "distinct_point_sum": [0, 0, 1],
    }
    matrices = enumerate_aut()
    assert len(matrices) == 108
    assert all(a % 3 != 0 and d % 3 != 0 for a, b, c, d in matrices)
    translations = list(product(range(9), range(3), range(2)))
    assert len(translations) == 54
    assert document["automorphism_model"] == {
        "odd_matrix_form": "(x,y) -> (a*x+3*b*y mod 9, c*x+d*y mod 3)",
        "parameter_ranges": "a in Z/9, b,c,d in Z/3",
        "automorphism_condition": "a mod 3 != 0 and d mod 3 != 0",
        "odd_endomorphism_matrix_count": 243,
        "full_core_endomorphism_count": 486,
        "automorphism_count": 108,
        "affine_count": 5832,
        "bijection_enumeration": True,
    }
    multi_dist: Counter[int] = Counter()
    set_dist: Counter[int] = Counter()
    mult_stab = []
    set_stab = []
    near = []
    for matrix in matrices:
        for translation in translations:
            image = [affine_image(matrix, translation, point) for point in coordinates]
            mo = overlap(source, image)
            so = len(support & set(image))
            multi_dist[mo] += 1
            set_dist[so] += 1
            if Counter(image) == source:
                mult_stab.append((matrix, translation))
            if set(image) == support:
                set_stab.append((matrix, translation))
            if (matrix, translation) != ((1, 0, 0, 1), (0, 0, 0)) and mo >= 14:
                near.append({"matrix": list(matrix), "translation": list(translation), "multiset_overlap": mo, "set_overlap": so})
    stringify = lambda counter: {str(k): counter[k] for k in sorted(counter)}
    assert document["overlap_distributions"] == {
        "multiset_overlap": stringify(multi_dist),
        "underlying_set_overlap": stringify(set_dist),
    }
    assert mult_stab == [((1, 0, 0, 1), (0, 0, 0))]
    assert set_stab == [((1, 0, 0, 1), (0, 0, 0))]
    assert document["stabilizers"] == {
        "affine_multiset_stabilizer_count": 1,
        "affine_set_stabilizer_count": 1,
        "linear_multiset_stabilizer_count": 1,
        "linear_set_stabilizer_count": 1,
        "affine_multiset_stabilizer": [{"matrix": [1, 0, 0, 1], "translation": [0, 0, 0]}],
        "affine_set_stabilizer": [{"matrix": [1, 0, 0, 1], "translation": [0, 0, 0]}],
    }
    expected_near = [
        {"matrix": [4, 0, 2, 1], "translation": [0, 0, 0], "multiset_overlap": 14, "set_overlap": 8},
        {"matrix": [7, 0, 1, 1], "translation": [0, 0, 0], "multiset_overlap": 14, "set_overlap": 8},
    ]
    assert sorted(near, key=lambda row: row["matrix"]) == expected_near
    assert document["rigidity_margin"] == {
        "maximum_nonidentity_multiset_overlap": 14,
        "number_at_maximum": 2,
        "witnesses": expected_near,
        "maximum_nonidentity_underlying_set_overlap": 8,
        "named_multiset_orbit_size": 5832,
        "named_set_orbit_size": 5832,
        "linear_multiset_orbit_size": 108,
        "linear_set_orbit_size": 108,
    }
    assert c73["hypergraph_symmetry"]["abstract_hypergraph_automorphism_order"] == 345600
    assert document["symmetry_boundary"] == {
        "c73_hypergraph_automorphism_order": 345600,
        "core_automorphism_order": 108,
        "affine_group_order": 5832,
        "induced_named_affine_symmetry_order": 1,
        "identified_as_same_group": False,
        "label_fiber_permutation_order": 480,
        "label_fiber_note": "5! * 2! * 2! permutes duplicate labels after the point map is fixed; it is not an affine symmetry",
    }
    assert document["claims"] == {
        "named_multiset_rigidity_proved": True,
        "underlying_set_rigidity_proved": True,
        "hypergraph_automorphisms_are_affine_core_automorphisms_claimed": False,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "PASS",
        "automorphism_count": 108,
        "affine_count": 5832,
        "multiset_stabilizer": 1,
        "set_stabilizer": 1,
        "max_nonidentity_overlap": 14,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
