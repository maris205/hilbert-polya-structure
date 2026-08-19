#!/usr/bin/env python3
"""GAP/SymPy cross-check for the C71 group and lattice calculations."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
from math import prod
from pathlib import Path
import subprocess

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C64 = ROOT / "henon_dynamics/henon_mu3_yukawa_burnside_marks/results/c64_mark_evidence.json"
EVIDENCE = PROJECT / "results/c71_complement_geometry_evidence.json"
D_TYPE = (3, 1, 1)
K2_TYPE = (4, 2, 2, 2) + (1,) * 8
TYPE_TO_GAP = {
    (): "1", (1,): "C2", (2,): "C4", (1, 1): "C2 x C2",
    (3,): "C8", (2, 1): "C4 x C2", (1, 1, 1): "C2 x C2 x C2",
    (3, 1): "C8 x C2", (2, 1, 1): "C4 x C2 x C2",
    (3, 1, 1): "C8 x C2 x C2",
}


def conjugate(exponents: tuple[int, ...]) -> list[int]:
    return [sum(value >= level for value in exponents)
            for level in range(1, max(exponents, default=0) + 1)]


def q_binomial(n: int, k: int) -> int:
    if k == 0:
        return 1
    return prod(2 ** (n - i) - 1 for i in range(k)) // prod(
        2 ** (k - i) - 1 for i in range(k)
    )


def subgroup_count(ambient: tuple[int, ...], subgroup: tuple[int, ...]) -> int:
    lam = conjugate(ambient)
    mu = conjugate(subgroup) + [0] * (len(lam) - len(conjugate(subgroup)) + 1)
    exponent = sum(mu[i + 1] * (lam[i] - mu[i]) for i in range(len(lam)))
    return 2 ** exponent * prod(
        q_binomial(lam[i] - mu[i + 1], mu[i] - mu[i + 1])
        for i in range(len(lam))
    )


def aut_order(exponents: tuple[int, ...]) -> int:
    if not exponents:
        return 1
    lam = conjugate(exponents)
    value = Fraction(2 ** sum(item * item for item in lam), 1)
    for multiplicity in Counter(exponents).values():
        for index in range(1, multiplicity + 1):
            value *= Fraction(2 ** index - 1, 2 ** index)
    assert value.denominator == 1
    return value.numerator


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    source = json.loads(C64.read_text())
    matrix = sp.Matrix(source["mark_matrix"])
    dimension = matrix.rows

    gap = subprocess.run(
        ["gap", "-q"],
        input=(
            'D:=AbelianGroup([8,2,2]);; '
            'for H in AllSubgroups(D) do Print(StructureDescription(H),"\\n"); od; '
            'QUIT;\n'
        ),
        capture_output=True,
        text=True,
        check=True,
    )
    gap_types = Counter(line.strip() for line in gap.stdout.splitlines() if line.strip())
    expected_gap = {
        TYPE_TO_GAP[tuple(row["image_exponents"])]: row["count"]
        for row in evidence["target_subgroup_poset"]["subgroup_counts_by_type"]
    }
    assert gap_types == Counter(expected_gap)
    assert sum(gap_types.values()) == 38

    for row in evidence["intersection_quotient_distribution"]:
        image_type = tuple(row["image_exponents"])
        target_subgroups = gap_types[TYPE_TO_GAP[image_type]]
        epimorphisms = subgroup_count(K2_TYPE, image_type) * aut_order(image_type)
        assert target_subgroups * epimorphisms == row["parameter_count"]

    smith = smith_normal_form(matrix, domain=ZZ)
    ambient_invariants = [abs(int(smith[i, i])) for i in range(dimension)]
    eight_image_invariants = [
        int(invariant // sp.gcd(invariant, 8))
        for invariant in ambient_invariants
        if invariant // sp.gcd(invariant, 8) > 1
    ]
    assert eight_image_invariants == evidence["universal_core"]["invariant_factors"] == [3, 18]

    eight_lattice = hermite_normal_form(matrix.row_join(8 * sp.eye(dimension)))
    assert abs(int(eight_lattice.det())) == evidence["universal_core"]["index_in_C"] == 2 ** 22
    assert abs(int(matrix.det())) // abs(int(eight_lattice.det())) == 54

    named_orders = []
    for index in range(dimension):
        column = sp.zeros(dimension, 1)
        column[index, 0] = 8
        enlarged = hermite_normal_form(matrix.row_join(column))
        named_orders.append(abs(int(matrix.det())) // abs(int(enlarged.det())))
    assert named_orders == evidence["named_core_geometry"]["eight_coordinate_orders"]

    generating_counts = {}
    triples = []
    for size in (1, 2, 3):
        generating = []
        for indices in combinations(range(dimension), size):
            generators = sp.zeros(dimension, size)
            for column, index in enumerate(indices):
                generators[index, column] = 8
            generated_lattice = hermite_normal_form(matrix.row_join(generators))
            if generated_lattice == eight_lattice:
                generating.append([f"S{index + 1}" for index in indices])
        generating_counts[str(size)] = len(generating)
        if size == 3:
            triples = generating
    assert generating_counts == evidence["named_core_geometry"]["generating_subset_counts_by_size"]
    assert triples == evidence["named_core_geometry"]["generating_triples"]
    assert all("S9" in triple for triple in triples)
    print(json.dumps({
        "status": "GROUP_LATTICE_CROSSCHECK_PASS",
        "gap_subgroup_count": len(gap.stdout.splitlines()),
        "gap_type_count": len(gap_types),
        "eight_C_invariants": eight_image_invariants,
        "eight_C_order": 54,
        "eight_C_index": 2 ** 22,
        "named_generating_triples": len(triples),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
