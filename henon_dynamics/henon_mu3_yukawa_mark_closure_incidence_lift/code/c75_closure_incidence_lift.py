#!/usr/bin/env python3
"""Produce the C75 lifted closure-incidence symmetry certificate.

The object is the incidence map i -> <x_i>, where x_i are the sixteen
source-bound C72 named coordinates.  A lifted symmetry is a pair (alpha, pi)
with alpha in Aut(Q) and pi a permutation of the sixteen labels satisfying
<x_{pi(i)}> = alpha(<x_i>) for every label i.  The ambient automorphism is
retained in the pair; it is not replaced by its generally non-faithful action
on the twenty subgroup lattice points.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import permutations, product
import json
from math import factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C72 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas"
C74 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity"
OUT = PROJECT / "results/c75_closure_incidence_lift_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
LABELS = tuple(f"S{i}" for i in range(1, 17))
AUTHORITY = {
    "c72": "8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51",
    "c72_manifest": "5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b",
    "c74": "9d5b65a6cee8f8a9e0a5debc544b44b587e1db33dae004c5f448760d5e905c5d",
    "c74_manifest": "356b0f631ae2e221ca7119968091b7670aae4ed2687d796830690ff56ed4093d",
}

Point = tuple[int, int, int]
Matrix = tuple[int, int, int, int]
Subgroup = frozenset[Point]
Permutation = tuple[int, ...]
Pair = tuple[Matrix, Permutation]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left: Point, right: Point) -> Point:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))  # type: ignore[return-value]


def multiple(coefficient: int, value: Point) -> Point:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))  # type: ignore[return-value]


def element_order(value: Point) -> int:
    for order in range(1, 55):
        if multiple(order, value) == (0, 0, 0):
            return order
    raise AssertionError("finite-group order search failed")


def cyclic_subgroup(value: Point) -> Subgroup:
    return frozenset(multiple(coefficient, value) for coefficient in range(element_order(value)))


def subgroup_key(subgroup: Subgroup) -> tuple[int, tuple[Point, ...]]:
    return len(subgroup), tuple(sorted(subgroup))


def extend(subgroup: Subgroup, cyclic: Subgroup) -> Subgroup:
    return frozenset(add(left, right) for left in subgroup for right in cyclic)


def enumerate_subgroups(points: list[Point]) -> list[Subgroup]:
    zero = frozenset({(0, 0, 0)})
    found = {zero}
    queue = deque([zero])
    cyclics = [cyclic_subgroup(point) for point in points]
    while queue:
        subgroup = queue.popleft()
        for cyclic in cyclics:
            enlarged = extend(subgroup, cyclic)
            if enlarged not in found:
                found.add(enlarged)
                queue.append(enlarged)
    return sorted(found, key=subgroup_key)


def matrix_image(matrix: Matrix, point: Point) -> Point:
    a, b, c, d = matrix
    x, y, z = point
    return ((a * x + 3 * b * y) % 9, (c * x + d * y) % 3, z)


def enumerate_automorphisms(points: list[Point]) -> list[Matrix]:
    result = []
    for a in range(9):
        for b, c, d in product(range(3), repeat=3):
            matrix = (a, b, c, d)
            if len({matrix_image(matrix, point) for point in points}) == len(points):
                result.append(matrix)
    return result


def compose_matrix(left: Matrix, right: Matrix) -> Matrix:
    """Return left after right in the displayed matrix coordinates."""
    a, b, c, d = left
    e, f, g, h = right
    return (
        (a * e + 3 * b * g) % 9,
        (a * f + b * h) % 3,
        (c * e + d * g) % 3,
        (d * h) % 3,
    )


def matrix_order(matrix: Matrix) -> int:
    identity = (1, 0, 0, 1)
    power = identity
    for order in range(1, 109):
        power = compose_matrix(matrix, power)
        if power == identity:
            return order
    raise AssertionError("matrix order search failed")


def permutation_compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def permutation_inverse(permutation: Permutation) -> Permutation:
    inverse = [0] * len(permutation)
    for source, target in enumerate(permutation):
        inverse[target] = source
    return tuple(inverse)


def compose_pair(left: Pair, right: Pair) -> Pair:
    return compose_matrix(left[0], right[0]), permutation_compose(left[1], right[1])


def pair_order(pair: Pair) -> int:
    identity = ((1, 0, 0, 1), tuple(range(16)))
    power = identity
    for order in range(1, 1001):
        power = compose_pair(pair, power)
        if power == identity:
            return order
    raise AssertionError("lifted-pair order search failed")


def permutation_from_cycles(cycles: list[list[int]]) -> Permutation:
    result = list(range(16))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            result[source] = target
    return tuple(result)


def cycle_labels(permutation: Permutation) -> list[list[str]]:
    seen: set[int] = set()
    cycles: list[list[str]] = []
    for source in range(len(permutation)):
        if source in seen or permutation[source] == source:
            continue
        cycle = []
        current = source
        while current not in seen:
            seen.add(current)
            cycle.append(LABELS[current])
            current = permutation[current]
        cycles.append(cycle)
    return cycles


def canonical_lift(
    matrix: Matrix,
    fibers: list[list[int]],
    fiber_index: dict[Subgroup, int],
    selected: list[Subgroup],
    image_subgroup,
) -> Permutation:
    result = [None] * 16
    for source_index, subgroup in enumerate(selected):
        target = image_subgroup(matrix, subgroup)
        target_index = fiber_index[target]
        for source_label, target_label in zip(fibers[source_index], fibers[target_index]):
            result[source_label] = target_label
    assert all(value is not None for value in result)
    return tuple(value for value in result if value is not None)


def all_compatible_lifts(
    matrix: Matrix,
    fibers: list[list[int]],
    fiber_index: dict[Subgroup, int],
    selected: list[Subgroup],
    image_subgroup,
) -> list[Pair]:
    target_permutations = []
    for subgroup in selected:
        target = image_subgroup(matrix, subgroup)
        target_permutations.append(list(permutations(fibers[fiber_index[target]])))
    result: list[Pair] = []

    def visit(block: int, partial: list[int | None]) -> None:
        if block == len(selected):
            assert all(value is not None for value in partial)
            result.append((matrix, tuple(value for value in partial if value is not None)))
            return
        source = fibers[block]
        for target_ordering in target_permutations[block]:
            next_partial = partial.copy()
            for source_label, target_label in zip(source, target_ordering):
                next_partial[source_label] = target_label
            visit(block + 1, next_partial)

    visit(0, [None] * 16)
    return result


def main() -> None:
    paths = {
        "c72": C72 / "results/c72_coordinate_core_atlas_evidence.json",
        "c72_manifest": C72 / "C72_PREFREEZE_MANIFEST.json",
        "c74": C74 / "results/c74_named_core_affine_rigidity_evidence.json",
        "c74_manifest": C74 / "C74_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c72 = json.loads(raw["c72"])
    c74 = json.loads(raw["c74"])
    assert c72["status"] == c74["status"] == "PREFREEZE_G3_PASS"
    assert c72["scope_literal"] == c74["scope_literal"] == FIREWALL
    assert c74["automorphism_model"]["automorphism_count"] == 108

    points = list(product(range(9), range(3), range(2)))
    coordinates = [tuple(row) for row in c72["coordinate_realization"]["coordinates"]]
    assert len(coordinates) == 16
    matrices = enumerate_automorphisms(points)
    assert len(matrices) == 108
    all_subgroups = enumerate_subgroups(points)
    assert len(all_subgroups) == 20
    all_subgroup_index = {subgroup: index for index, subgroup in enumerate(all_subgroups)}

    fibers_by_subgroup: defaultdict[Subgroup, list[int]] = defaultdict(list)
    for label_index, coordinate in enumerate(coordinates):
        fibers_by_subgroup[cyclic_subgroup(coordinate)].append(label_index)
    selected = sorted(fibers_by_subgroup, key=subgroup_key)
    fibers = [sorted(fibers_by_subgroup[subgroup]) for subgroup in selected]
    fiber_index = {subgroup: index for index, subgroup in enumerate(selected)}
    assert len(selected) == 9
    assert sorted(len(fiber) for fiber in fibers) == [1, 1, 1, 1, 1, 2, 2, 2, 5]
    fiber_factor = 1
    for fiber in fibers:
        fiber_factor *= factorial(len(fiber))
    assert fiber_factor == 960

    def image_subgroup(matrix: Matrix, subgroup: Subgroup) -> Subgroup:
        return frozenset(matrix_image(matrix, point) for point in subgroup)

    weights = {subgroup: len(fibers_by_subgroup.get(subgroup, [])) for subgroup in all_subgroups}
    weighted_stabilizer = [
        matrix
        for matrix in matrices
        if all(weights[image_subgroup(matrix, subgroup)] == weights[subgroup] for subgroup in all_subgroups)
    ]
    assert len(weighted_stabilizer) == 12
    assert all(image_subgroup(matrix, subgroup) in fiber_index for matrix in weighted_stabilizer for subgroup in selected)

    fiber_actions = {
        str(matrix): [fiber_index[image_subgroup(matrix, subgroup)] for subgroup in selected]
        for matrix in weighted_stabilizer
    }
    identity_matrix = (1, 0, 0, 1)
    r = (2, 0, 0, 2)
    s = (2, 1, 2, 1)
    assert r in weighted_stabilizer and s in weighted_stabilizer
    assert matrix_order(r) == 6 and matrix_order(s) == 2
    assert compose_matrix(r, s) == compose_matrix(s, r)
    assert {compose_matrix(r, r) for _ in [0]}  # keep the exact composition path exercised
    generated_stabilizer = {identity_matrix}
    queue = deque([identity_matrix])
    while queue:
        current = queue.popleft()
        for generator in (r, s):
            candidate = compose_matrix(generator, current)
            if candidate not in generated_stabilizer:
                generated_stabilizer.add(candidate)
                queue.append(candidate)
    assert generated_stabilizer == set(weighted_stabilizer)

    lifts: list[Pair] = []
    for matrix in weighted_stabilizer:
        lifts.extend(all_compatible_lifts(matrix, fibers, fiber_index, selected, image_subgroup))
    assert len(lifts) == 12 * fiber_factor
    assert len(set(lifts)) == len(lifts) == 11520
    lift_set = set(lifts)
    identity_pair = (identity_matrix, tuple(range(16)))
    assert identity_pair in lift_set
    for pair in lifts:
        matrix, permutation = pair
        for label_index in range(16):
            source_subgroup = cyclic_subgroup(coordinates[label_index])
            target_subgroup = cyclic_subgroup(coordinates[permutation[label_index]])
            assert target_subgroup == image_subgroup(matrix, source_subgroup)

    # The following six generators use only label permutations within closure
    # fibers plus two ambient matrices.  Their generated group is checked
    # against the direct 11,520-pair enumeration.
    zero = next(index for index, fiber in enumerate(fibers) if len(fiber) == 5)
    _ = zero  # the block is retained in the evidence below by its labels.
    generators: list[Pair] = [
        (identity_matrix, permutation_from_cycles([[4, 5, 9, 12, 13]])),
        (identity_matrix, permutation_from_cycles([[4, 5]])),
        (identity_matrix, permutation_from_cycles([[2, 10]])),
        (identity_matrix, permutation_from_cycles([[6, 14]])),
        (r, canonical_lift(r, fibers, fiber_index, selected, image_subgroup)),
        (s, canonical_lift(s, fibers, fiber_index, selected, image_subgroup)),
    ]
    assert all(generator in lift_set for generator in generators)
    inverse_generators = []
    matrix_inverse = {matrix: next(candidate for candidate in weighted_stabilizer if compose_matrix(matrix, candidate) == identity_matrix) for matrix in weighted_stabilizer}
    for matrix, permutation in generators:
        inverse_generators.append((matrix_inverse.get(matrix, identity_matrix), permutation_inverse(permutation)))
    generated_lifts = {identity_pair}
    queue = deque([identity_pair])
    for generator in generators + inverse_generators:
        if generator not in generated_lifts:
            generated_lifts.add(generator)
            queue.append(generator)
    while queue:
        current = queue.popleft()
        for generator in generators + inverse_generators:
            candidate = compose_pair(generator, current)
            assert candidate in lift_set
            if candidate not in generated_lifts:
                generated_lifts.add(candidate)
                queue.append(candidate)
    assert generated_lifts == lift_set

    order_distribution = Counter(pair_order(pair) for pair in lifts)
    assert order_distribution == Counter({
        1: 1, 2: 623, 3: 62, 4: 1168, 5: 24, 6: 4066,
        10: 552, 12: 3296, 15: 48, 20: 192, 30: 1104, 60: 384,
    })
    center_order = sum(
        all(compose_pair(pair, generator) == compose_pair(generator, pair) for generator in generators)
        for pair in lifts
    )
    assert center_order == 24

    kernel_order = sum(matrix == identity_matrix for matrix, _ in lifts)
    assert kernel_order == fiber_factor
    # The pure subgroup-lattice action is intentionally recorded only as a
    # diagnostic: six ambient automorphisms act trivially on all twenty
    # subgroups, so that action alone cannot represent the lifted group.
    lattice_actions = {
        tuple(all_subgroup_index[image_subgroup(matrix, subgroup)] for subgroup in all_subgroups)
        for matrix in matrices
    }
    lattice_kernel_order = sum(
        all(image_subgroup(matrix, subgroup) == subgroup for subgroup in all_subgroups)
        for matrix in matrices
    )
    assert len(lattice_actions) == 18
    assert lattice_kernel_order == 6

    def matrix_json(matrix: Matrix) -> list[int]:
        return list(matrix)

    def point_json(point: Point) -> list[int]:
        return list(point)

    closure_rows = []
    for index, (subgroup, fiber) in enumerate(zip(selected, fibers), start=1):
        closure_rows.append({
            "closure_id": f"F{index}",
            "subgroup_order": len(subgroup),
            "subgroup_points": [point_json(point) for point in sorted(subgroup)],
            "labels": [LABELS[label] for label in fiber],
            "weight": len(fiber),
        })
    subgroup_rows = [
        {
            "subgroup_index": index,
            "subgroup_order": len(subgroup),
            "subgroup_points": [point_json(point) for point in sorted(subgroup)],
            "closure_weight": weights[subgroup],
        }
        for index, subgroup in enumerate(all_subgroups)
    ]
    generator_rows = [
        {
            "name": name,
            "matrix": matrix_json(matrix),
            "matrix_order": matrix_order(matrix),
            "label_cycles": cycle_labels(permutation),
            "label_permutation": list(permutation),
        }
        for name, (matrix, permutation) in zip(
            ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition", "fiber_F9_transposition", "ambient_r", "ambient_s"),
            generators,
        )
    ]
    result: dict[str, Any] = {
        "schema_id": "hcs-c75-lifted-closure-incidence-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "ambient_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "order": 54,
            "automorphism_order": len(matrices),
            "matrix_form": "(x,y,z) -> (a*x+3*b*y mod 9, c*x+d*y mod 3, z)",
            "automorphism_condition": "a mod 3 != 0 and d mod 3 != 0",
            "all_subgroup_count": len(all_subgroups),
        },
        "named_coordinate_source": {
            "label_count": len(LABELS),
            "coordinates": [point_json(point) for point in coordinates],
            "coordinate_sha256": digest(canonical([point_json(point) for point in coordinates])),
        },
        "closure_incidence": {
            "definition": "I(i,C)=1 iff C=<x_i>; a lifted pair (alpha,pi) preserves I iff <x_{pi(i)}> = alpha(<x_i>) for every i",
            "selected_cyclic_closure_count": len(selected),
            "selected_fibers": closure_rows,
            "all_subgroups": subgroup_rows,
            "weighted_stabilizer_definition": "K={alpha in Aut(Q): w(alpha C)=w(C) for every subgroup C}, w(C)=# {i:<x_i>=C}",
            "weighted_stabilizer_order": len(weighted_stabilizer),
            "weighted_stabilizer_matrices": [matrix_json(matrix) for matrix in weighted_stabilizer],
            "weighted_stabilizer_fiber_actions": fiber_actions,
            "generators": [[2, 0, 0, 2], [2, 1, 2, 1]],
            "generator_orders": {"r": matrix_order(r), "s": matrix_order(s)},
            "commuting_generators": True,
            "abstract_stabilizer_candidate": "C6 x C2",
        },
        "lifted_symmetry": {
            "definition": "G~={(alpha,pi): alpha in K, pi in Sym(16), <x_{pi(i)}> = alpha(<x_i>) for all i}",
            "direct_compatible_pair_count": len(lifts),
            "unique_pair_count": len(set(lifts)),
            "label_fiber_order": fiber_factor,
            "fiber_factorization": "5! * 2! * 2! * 2!",
            "projection_kernel_order": kernel_order,
            "projection_kernel_candidate": "S5 x C2 x C2 x C2",
            "lifted_group_order": len(lift_set),
            "order_distribution": {str(order): order_distribution[order] for order in sorted(order_distribution)},
            "center_order": center_order,
            "generators": generator_rows,
            "generated_group_order": len(generated_lifts),
            "abstract_group_candidate": "S5 x C2 x D8 x C6",
            "abstract_group_order_check": 120 * 2 * 8 * 6,
        },
        "nonfaithful_lattice_diagnostic": {
            "twenty_subgroup_lattice_action_image_order": len(lattice_actions),
            "twenty_subgroup_lattice_action_kernel_order": lattice_kernel_order,
            "warning": "The pure subgroup-lattice action is not the lifted symmetry group; alpha is retained and label fibers are lifted.",
        },
        "claims": {
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
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "ambient_automorphism_order": len(matrices),
        "weighted_stabilizer_order": len(weighted_stabilizer),
        "label_fiber_order": fiber_factor,
        "lifted_order": len(lift_set),
        "lattice_image_order": len(lattice_actions),
        "lattice_kernel_order": lattice_kernel_order,
        "abstract_group_candidate": result["lifted_symmetry"]["abstract_group_candidate"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
