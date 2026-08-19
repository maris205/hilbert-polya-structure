#!/usr/bin/env python3
"""Independent checker for the C75 lifted closure-incidence certificate."""

from __future__ import annotations

import argparse
from collections import defaultdict, deque, Counter
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
SOURCES = {
    "c72": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/results/c72_coordinate_core_atlas_evidence.json",
    "c72_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/C72_PREFREEZE_MANIFEST.json",
    "c74": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/results/c74_named_core_affine_rigidity_evidence.json",
    "c74_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/C74_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c72": "8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51",
    "c72_manifest": "5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b",
    "c74": "9d5b65a6cee8f8a9e0a5debc544b44b587e1db33dae004c5f448760d5e905c5d",
    "c74_manifest": "356b0f631ae2e221ca7119968091b7670aae4ed2687d796830690ff56ed4093d",
}
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
LABELS = tuple(f"S{i}" for i in range(1, 17))


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left, right):
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient, value):
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def element_order(value):
    for order in range(1, 55):
        if multiple(order, value) == (0, 0, 0):
            return order
    raise AssertionError


def cyclic_subgroup(value):
    return frozenset(multiple(k, value) for k in range(element_order(value)))


def subgroup_key(subgroup):
    return len(subgroup), tuple(sorted(subgroup))


def close(subgroup, cyclic):
    return frozenset(add(left, right) for left in subgroup for right in cyclic)


def all_subgroups(points):
    zero = frozenset({(0, 0, 0)})
    seen = {zero}
    queue = deque([zero])
    while queue:
        current = queue.popleft()
        for point in points:
            candidate = close(current, cyclic_subgroup(point))
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return sorted(seen, key=subgroup_key)


def matrix_image(matrix, point):
    a, b, c, d = matrix
    x, y, z = point
    return ((a * x + 3 * b * y) % 9, (c * x + d * y) % 3, z)


def compose_matrix(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return ((a * e + 3 * b * g) % 9, (a * f + b * h) % 3,
            (c * e + d * g) % 3, (d * h) % 3)


def matrix_order(matrix):
    identity = (1, 0, 0, 1)
    power = identity
    for order in range(1, 109):
        power = compose_matrix(matrix, power)
        if power == identity:
            return order
    raise AssertionError


def permutation_compose(left, right):
    return tuple(left[right[index]] for index in range(16))


def permutation_inverse(permutation):
    inverse = [0] * 16
    for source, target in enumerate(permutation):
        inverse[target] = source
    return tuple(inverse)


def compose_pair(left, right):
    return compose_matrix(left[0], right[0]), permutation_compose(left[1], right[1])


def pair_order(pair):
    identity = ((1, 0, 0, 1), tuple(range(16)))
    power = identity
    for order in range(1, 1001):
        power = compose_pair(pair, power)
        if power == identity:
            return order
    raise AssertionError


def permutation_from_cycles(cycles):
    result = list(range(16))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            result[source] = target
    return tuple(result)


def permutation_from_cycles(cycles):
    result = list(range(16))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            result[source] = target
    return tuple(result)


def cycle_labels(permutation):
    seen = set()
    result = []
    for source in range(16):
        if source in seen or permutation[source] == source:
            continue
        cycle = []
        current = source
        while current not in seen:
            seen.add(current)
            cycle.append(LABELS[current])
            current = permutation[current]
        result.append(cycle)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=PROJECT / "results/c75_closure_incidence_lift_evidence.json")
    args = parser.parse_args()
    evidence_raw = args.evidence.read_bytes()
    evidence = json.loads(evidence_raw)
    assert evidence_raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c75-lifted-closure-incidence-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    assert {name: digest(path.read_bytes()) for name, path in SOURCES.items()} == HASHES
    assert evidence["authority"] == HASHES

    c72 = json.loads(SOURCES["c72"].read_text())
    c74 = json.loads(SOURCES["c74"].read_text())
    coordinates = [tuple(row) for row in c72["coordinate_realization"]["coordinates"]]
    assert len(coordinates) == 16
    assert c74["automorphism_model"]["automorphism_count"] == 108
    points = list(product(range(9), range(3), range(2)))
    matrices = [
        (a, b, c, d)
        for a in range(9)
        for b, c, d in product(range(3), repeat=3)
        if len({matrix_image((a, b, c, d), point) for point in points}) == 54
    ]
    assert len(matrices) == 108
    subgroups = all_subgroups(points)
    assert len(subgroups) == 20
    subgroup_index = {subgroup: index for index, subgroup in enumerate(subgroups)}

    def image_subgroup(matrix, subgroup):
        return frozenset(matrix_image(matrix, point) for point in subgroup)

    fibers_by_subgroup = defaultdict(list)
    for index, coordinate in enumerate(coordinates):
        fibers_by_subgroup[cyclic_subgroup(coordinate)].append(index)
    selected = sorted(fibers_by_subgroup, key=subgroup_key)
    fibers = [sorted(fibers_by_subgroup[subgroup]) for subgroup in selected]
    selected_index = {subgroup: index for index, subgroup in enumerate(selected)}
    weights = {subgroup: len(fibers_by_subgroup.get(subgroup, [])) for subgroup in subgroups}
    assert len(selected) == 9
    assert sorted(len(fiber) for fiber in fibers) == [1, 1, 1, 1, 1, 2, 2, 2, 5]
    fiber_order = 1
    for fiber in fibers:
        for value in range(2, len(fiber) + 1):
            fiber_order *= value
    assert fiber_order == 960
    point_json = lambda point: list(point)
    expected_closure_rows = [
        {
            "closure_id": f"F{index}",
            "subgroup_order": len(subgroup),
            "subgroup_points": [point_json(point) for point in sorted(subgroup)],
            "labels": [LABELS[label] for label in fiber],
            "weight": len(fiber),
        }
        for index, (subgroup, fiber) in enumerate(zip(selected, fibers), start=1)
    ]
    expected_subgroup_rows = [
        {
            "subgroup_index": index,
            "subgroup_order": len(subgroup),
            "subgroup_points": [point_json(point) for point in sorted(subgroup)],
            "closure_weight": weights[subgroup],
        }
        for index, subgroup in enumerate(subgroups)
    ]
    expected_coordinates = [point_json(point) for point in coordinates]
    assert evidence["ambient_model"] == {
        "group": "Z/9 + Z/3 + Z/2",
        "order": 54,
        "automorphism_order": 108,
        "matrix_form": "(x,y,z) -> (a*x+3*b*y mod 9, c*x+d*y mod 3, z)",
        "automorphism_condition": "a mod 3 != 0 and d mod 3 != 0",
        "all_subgroup_count": 20,
    }
    assert evidence["named_coordinate_source"] == {
        "label_count": 16,
        "coordinates": expected_coordinates,
        "coordinate_sha256": digest(canonical(expected_coordinates)),
    }
    stabilizer = [
        matrix for matrix in matrices
        if all(weights[image_subgroup(matrix, subgroup)] == weights[subgroup] for subgroup in subgroups)
    ]
    assert len(stabilizer) == 12
    assert all(image_subgroup(matrix, subgroup) in selected_index for matrix in stabilizer for subgroup in selected)
    fiber_actions = {
        str(matrix): [selected_index[image_subgroup(matrix, subgroup)] for subgroup in selected]
        for matrix in stabilizer
    }
    assert evidence["closure_incidence"] == {
        "definition": "I(i,C)=1 iff C=<x_i>; a lifted pair (alpha,pi) preserves I iff <x_{pi(i)}> = alpha(<x_i>) for every i",
        "selected_cyclic_closure_count": 9,
        "selected_fibers": expected_closure_rows,
        "all_subgroups": expected_subgroup_rows,
        "weighted_stabilizer_definition": "K={alpha in Aut(Q): w(alpha C)=w(C) for every subgroup C}, w(C)=# {i:<x_i>=C}",
        "weighted_stabilizer_order": 12,
        "weighted_stabilizer_matrices": [list(matrix) for matrix in stabilizer],
        "weighted_stabilizer_fiber_actions": fiber_actions,
        "generators": [[2, 0, 0, 2], [2, 1, 2, 1]],
        "generator_orders": {"r": 6, "s": 2},
        "commuting_generators": True,
        "abstract_stabilizer_candidate": "C6 x C2",
    }

    r = (2, 0, 0, 2)
    s = (2, 1, 2, 1)
    assert matrix_order(r) == 6 and matrix_order(s) == 2
    assert compose_matrix(r, s) == compose_matrix(s, r)
    generated = { (1, 0, 0, 1) }
    queue = deque([(1, 0, 0, 1)])
    while queue:
        current = queue.popleft()
        for generator in (r, s):
            candidate = compose_matrix(generator, current)
            if candidate not in generated:
                generated.add(candidate)
                queue.append(candidate)
    assert generated == set(stabilizer)

    def rank_lift(matrix):
        result = [None] * 16
        for source_index, subgroup in enumerate(selected):
            target = image_subgroup(matrix, subgroup)
            for source, target_label in zip(fibers[source_index], fibers[selected_index[target]]):
                result[source] = target_label
        assert all(value is not None for value in result)
        return tuple(value for value in result if value is not None)

    generators = [
        ((1, 0, 0, 1), permutation_from_cycles([[4, 5, 9, 12, 13]])),
        ((1, 0, 0, 1), permutation_from_cycles([[4, 5]])),
        ((1, 0, 0, 1), permutation_from_cycles([[2, 10]])),
        ((1, 0, 0, 1), permutation_from_cycles([[6, 14]])),
        (r, rank_lift(r)),
        (s, rank_lift(s)),
    ]
    expected_generator_rows = [
        {
            "name": name,
            "matrix": list(matrix),
            "matrix_order": matrix_order(matrix),
            "label_cycles": cycle_labels(permutation),
            "label_permutation": list(permutation),
        }
        for name, (matrix, permutation) in zip(
            ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition", "fiber_F9_transposition", "ambient_r", "ambient_s"),
            generators,
        )
    ]

    # Independent direct product enumeration of the compatible label lifts.
    lifts = []
    for matrix in stabilizer:
        choices = []
        for subgroup in selected:
            target = image_subgroup(matrix, subgroup)
            choices.append(list(permutations(fibers[selected_index[target]])))
        for block_choices in product(*choices):
            permutation = [None] * 16
            for source_index, ordering in enumerate(block_choices):
                for source_label, target_label in zip(fibers[source_index], ordering):
                    permutation[source_label] = target_label
            assert all(value is not None for value in permutation)
            lifts.append((matrix, tuple(value for value in permutation if value is not None)))
    assert len(lifts) == 11520
    assert len(set(lifts)) == 11520
    for matrix, permutation in lifts:
        for label_index in range(16):
            source = cyclic_subgroup(coordinates[label_index])
            target = cyclic_subgroup(coordinates[permutation[label_index]])
            assert target == image_subgroup(matrix, source)
    distribution = Counter(pair_order(pair) for pair in lifts)
    expected_distribution = {
        "1": 1, "2": 623, "3": 62, "4": 1168, "5": 24, "6": 4066,
        "10": 552, "12": 3296, "15": 48, "20": 192, "30": 1104, "60": 384,
    }
    assert {str(order): distribution[order] for order in sorted(distribution)} == expected_distribution
    assert sum(matrix == (1, 0, 0, 1) for matrix, _ in lifts) == 960
    assert evidence["lifted_symmetry"] == {
        "definition": "G~={(alpha,pi): alpha in K, pi in Sym(16), <x_{pi(i)}> = alpha(<x_i>) for all i}",
        "direct_compatible_pair_count": 11520,
        "unique_pair_count": 11520,
        "label_fiber_order": 960,
        "fiber_factorization": "5! * 2! * 2! * 2!",
        "projection_kernel_order": 960,
        "projection_kernel_candidate": "S5 x C2 x C2 x C2",
        "lifted_group_order": 11520,
        "order_distribution": expected_distribution,
        "center_order": 24,
        "generators": expected_generator_rows,
        "generated_group_order": 11520,
        "abstract_group_candidate": "S5 x C2 x D8 x C6",
        "abstract_group_order_check": 11520,
    }

    lattice_actions = {
        tuple(subgroup_index[image_subgroup(matrix, subgroup)] for subgroup in subgroups)
        for matrix in matrices
    }
    lattice_kernel = sum(
        all(image_subgroup(matrix, subgroup) == subgroup for subgroup in subgroups)
        for matrix in matrices
    )
    assert len(lattice_actions) == 18
    assert lattice_kernel == 6
    assert evidence["nonfaithful_lattice_diagnostic"] == {
        "twenty_subgroup_lattice_action_image_order": 18,
        "twenty_subgroup_lattice_action_kernel_order": 6,
        "warning": "The pure subgroup-lattice action is not the lifted symmetry group; alpha is retained and label fibers are lifted.",
    }
    assert evidence["claims"]["pure_lattice_action_not_substituted"] is True
    assert evidence["claims"] == {
        "source_bound_to_c72_and_c74": True,
        "weighted_stabilizer_order_12": True,
        "label_fiber_order_960": True,
        "lifted_order_11520": True,
        "direct_pair_enumeration": True,
        "lifted_group_generated_independently": True,
        "pure_lattice_action_not_substituted": True,
        "abstract_group_structure_claimed_as_candidate": True,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "PASS",
        "automorphism_order": 108,
        "weighted_stabilizer_order": 12,
        "label_fiber_order": 960,
        "lifted_order": 11520,
        "lattice_image_order": 18,
        "lattice_kernel_order": 6,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
