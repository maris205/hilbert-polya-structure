#!/usr/bin/env python3
"""GAP cross-check for the faithful lifted C75 group representation."""

from __future__ import annotations

from collections import defaultdict
from itertools import product
import json
from pathlib import Path
import subprocess

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c75_closure_incidence_lift_evidence.json"
C72 = PROJECT.parent / "henon_mu3_yukawa_mark_coordinate_core_atlas/results/c72_coordinate_core_atlas_evidence.json"
MODULI = (9, 3, 2)


def multiple(coefficient, value):
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def order(value):
    for candidate in range(1, 55):
        if multiple(candidate, value) == (0, 0, 0):
            return candidate
    raise AssertionError


def cyclic(value):
    return frozenset(multiple(k, value) for k in range(order(value)))


def image(matrix, point):
    a, b, c, d = matrix
    x, y, z = point
    return ((a * x + 3 * b * y) % 9, (c * x + d * y) % 3, z)


def label_permutation(cycles):
    result = list(range(16))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            result[source] = target
    return tuple(result)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    coordinates = [tuple(row) for row in json.loads(C72.read_text())["coordinate_realization"]["coordinates"]]
    points = list(product(range(9), range(3), range(2)))
    point_index = {point: index for index, point in enumerate(points)}

    fibers_by_subgroup = defaultdict(list)
    for label, coordinate in enumerate(coordinates):
        fibers_by_subgroup[cyclic(coordinate)].append(label)
    selected = sorted(fibers_by_subgroup, key=lambda subgroup: (len(subgroup), tuple(sorted(subgroup))))
    fibers = [sorted(fibers_by_subgroup[subgroup]) for subgroup in selected]
    fiber_index = {subgroup: index for index, subgroup in enumerate(selected)}

    def rank_lift(matrix):
        result = [None] * 16
        for source_index, subgroup in enumerate(selected):
            target = frozenset(image(matrix, point) for point in subgroup)
            assert target in fiber_index
            for source, target_label in zip(fibers[source_index], fibers[fiber_index[target]]):
                result[source] = target_label
        return tuple(value for value in result if value is not None)

    identity = (1, 0, 0, 1)
    generators = [
        (identity, label_permutation([[4, 5, 9, 12, 13]])),
        (identity, label_permutation([[4, 5]])),
        (identity, label_permutation([[2, 10]])),
        (identity, label_permutation([[6, 14]])),
        ((2, 0, 0, 2), rank_lift((2, 0, 0, 2))),
        ((2, 1, 2, 1), rank_lift((2, 1, 2, 1))),
    ]

    def full_permutation(matrix, labels):
        ambient = [point_index[image(matrix, point)] + 1 for point in points]
        label_layer = [54 + target + 1 for target in labels]
        return ambient + label_layer

    gap_lines = []
    for index, (matrix, labels) in enumerate(generators):
        gap_lines.append(f"g{index}:=PermList({full_permutation(matrix, labels)});;")
    gap_lines.extend([
        "G:=Group(g0,g1,g2,g3,g4,g5);;",
        'Print("SIZE=",Size(G),"\\n");;',
        'Print("DESC=",StructureDescription(G),"\\n");;',
        'Print("AB=",AbelianInvariants(G),"\\n");;',
    ])
    run = subprocess.run(["gap", "-q"], input="\n".join(gap_lines) + "\n",
                         text=True, capture_output=True, check=True)
    lines = [line.strip() for line in run.stdout.splitlines() if line.strip()]
    assert "SIZE=11520" in lines
    assert "DESC=C2 x C6 x S5 x D8" in lines
    assert "AB=[ 2, 2, 2, 2, 2, 3 ]" in lines
    assert evidence["lifted_symmetry"]["lifted_group_order"] == 11520
    assert evidence["lifted_symmetry"]["abstract_group_candidate"] == "S5 x C2 x D8 x C6"
    print(json.dumps({
        "status": "GROUP_CROSSCHECK_PASS",
        "faithful_representation_degree": 70,
        "gap_order": 11520,
        "gap_structure": "C2 x C6 x S5 x D8",
        "gap_abelian_invariants": [2, 2, 2, 2, 2, 3],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
