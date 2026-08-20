#!/usr/bin/env python3
"""Independent checker for the C78 repair-distance geometry certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
C77 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_mobius_reliability"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
EVIDENCE = PROJECT / "results/c78_repair_distance_geometry_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
ALL_MASK = (1 << 16) - 1
HASHES = {
    "c77": "f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634",
    "c77_manifest": "bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc",
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def add(left, right):
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient, value):
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def order(value):
    for candidate in range(1, 55):
        if multiple(candidate, value) == (0, 0, 0):
            return candidate
    raise AssertionError


def cyclic(value):
    return frozenset(multiple(k, value) for k in range(order(value)))


def mask_for(labels):
    return sum(1 << (int(label[1:]) - 1) for label in labels)


def coefficient_table_from_evidence(value):
    return {(int(key.split(",")[0]), int(key.split(",")[1])): int(number)
            for key, number in value.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    evidence_raw = args.evidence.read_bytes()
    evidence = json.loads(evidence_raw)
    assert evidence_raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c78-repair-distance-geometry-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL

    source_paths = {
        "c77": C77 / "results/c77_subgroup_mobius_reliability_evidence.json",
        "c77_manifest": C77 / "C77_PREFREEZE_MANIFEST.json",
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c73_manifest": C73 / "C73_PREFREEZE_MANIFEST.json",
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in source_paths.items()} == HASHES
    assert evidence["authority"] == HASHES
    c77 = json.loads(source_paths["c77"].read_text())
    c73 = json.loads(source_paths["c73"].read_text())
    c75 = json.loads(source_paths["c75"].read_text())
    c76 = json.loads(source_paths["c76"].read_text())
    assert c77["status"] == c73["status"] == c75["status"] == c76["status"] == "PREFREEZE_G3_PASS"
    assert c77["scope_literal"] == c73["scope_literal"] == c75["scope_literal"] == c76["scope_literal"] == FIREWALL
    assert c77["authority"]["c76"] == HASHES["c76"]
    assert c77["authority"]["c76_manifest"] == HASHES["c76_manifest"]
    assert c76["authority"]["c75"] == HASHES["c75"]
    assert c76["authority"]["c75_manifest"] == HASHES["c75_manifest"]
    assert c76["source_model"]["support_count"] == 65536
    assert c76["full_core_minimality"]["support_count"] == 25

    rows = c75["closure_incidence"]["all_subgroups"]
    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    subgroups = [frozenset(tuple(point) for point in row["subgroup_points"]) for row in rows]
    index = {subgroup: i for i, subgroup in enumerate(subgroups)}
    cyclics = [cyclic(point) for point in coordinates]
    def extend(left, right):
        return frozenset(add(a, b) for a in left for b in right)
    extension = [[index[extend(subgroup, cyclics[label])] for label in range(16)]
                 for subgroup in subgroups]
    zero = index[frozenset({(0, 0, 0)})]
    full = index[frozenset(product(range(9), range(3), range(2)))]
    closure = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        closure[mask] = extension[closure[mask ^ low]][low.bit_length() - 1]
    full_minimal = [
        mask for mask in range(1 << 16)
        if closure[mask] == full and all(
            closure[mask ^ (1 << bit)] != full
            for bit in range(16) if mask & (1 << bit)
        )
    ]
    assert len(full_minimal) == 25

    # Derive the four projective blocks from the named coordinates, rather
    # than accepting the structural decomposition as an axiom.
    pivot = 8
    assert coordinates[pivot] == (0, 0, 1)
    direction_map = {}
    for label, point in enumerate(coordinates):
        if label == pivot or point[2] != 0:
            continue
        a, b = point[0] % 3, point[1] % 3
        if (a, b) == (0, 0):
            continue
        if a:
            direction = (1, b * (1 if a == 1 else 2) % 3)
        else:
            direction = (0, 1)
        direction_map.setdefault(direction, []).append(label)
    directions = ((1, 0), (1, 1), (1, 2), (0, 1))
    block_labels = [[f"S{label + 1}" for label in direction_map[d]] for d in directions]
    block_masks = [sum(1 << label for label in direction_map[d]) for d in directions]
    assert [len(block) for block in block_labels] == [1, 1, 2, 5]
    pivot_bit = 1 << pivot

    def rho_from_minimal(deleted):
        return min((mask & deleted).bit_count() for mask in full_minimal)

    def rho_structural(deleted):
        return int(bool(deleted & pivot_bit)) + max(
            0, sum((deleted & block) == block for block in block_masks) - 2
        )

    table = Counter()
    by_deleted = [Counter() for _ in range(17)]
    by_retained = [Counter() for _ in range(17)]
    for deleted in range(1 << 16):
        rho = rho_from_minimal(deleted)
        assert rho == rho_structural(deleted)
        retained = ALL_MASK ^ deleted
        assert (rho == 0) == (closure[retained] == full)
        table[(deleted.bit_count(), rho)] += 1
        by_deleted[deleted.bit_count()][rho] += 1
        by_retained[retained.bit_count()][rho] += 1
    distribution = {str(rho): sum(value for (size, distance), value in table.items() if distance == rho)
                    for rho in range(4)}
    assert distribution == {"0": 30400, "1": 32704, "2": 2368, "3": 64}
    expected_deleted_rows = [
        {"deleted_count": size, "distance_counts": {str(distance): by_deleted[size][distance] for distance in range(4)} }
        for size in range(17)
    ]
    expected_retained_rows = [
        {"retained_count": size, "distance_counts": {str(distance): by_retained[size][distance] for distance in range(4)} }
        for size in range(17)
    ]
    atlas = evidence["repair_distance_atlas"]
    assert atlas["by_deleted_cardinality"] == expected_deleted_rows
    assert atlas["by_retained_cardinality"] == expected_retained_rows
    assert atlas["distance_three_masks"] == sorted(
        deleted for deleted in range(1 << 16) if rho_structural(deleted) == 3
    )

    # Rebuild H and its z->y transformation symbolically.
    x, y, z = sp.symbols("x y z")
    H = 1
    for size in (1, 1, 2, 5):
        H *= sum(comb(size, d) * x ** d for d in range(size)) + z * x ** size
    transformed = 0
    for (degree, full_blocks), coefficient in sp.Poly(sp.expand(H), x, z).terms():
        transformed += coefficient * x ** degree * y ** max(0, full_blocks - 2)
    predicted = sp.expand((1 + x) ** 6 * (1 + x * y) * transformed)
    actual = sp.expand(sum(value * x ** size * y ** distance
                           for (size, distance), value in table.items()))
    assert predicted == actual
    coefficient_table = coefficient_table_from_evidence(
        evidence["bivariate_generating_function"]["coefficient_table"]
    )
    assert coefficient_table == dict(table)
    assert sp.expand(predicted.subs(y, 1)) == sp.expand((1 + x) ** 16)
    assert sp.expand(predicted.subs(x, 1)) == 30400 + 32704 * y + 2368 * y ** 2 + 64 * y ** 3

    definition = evidence["definition"]
    assert definition["deleted_set"] == "D"
    assert definition["retained_set"] == "A=L\\D"
    assert definition["repair_distance"] == "rho(D)=min{|R|: R subset D and Phi((L\\D) union R)=Q}"
    assert definition["direction_blocks"] == block_labels
    assert definition["direction_block_sizes"] == [1, 1, 2, 5]
    assert definition["dummy_labels"] == ["S2", "S5", "S6", "S10", "S13", "S14"]
    assert definition["pivot"] == "S9"
    assert definition["formula"] == "rho(D)=1_{S9 in D}+max(0,t(D)-2), t(D)=number of fully deleted direction blocks"
    assert definition["maximum_distance"] == 3
    assert atlas["deletion_count_distribution"] == distribution
    assert evidence["bivariate_generating_function"]["P_x_at_y1"] == {
        str(i): comb(16, i) for i in range(17)
    }
    assert evidence["bivariate_generating_function"]["P_1_at_y"] == distribution
    assert evidence["bivariate_generating_function"]["x_convention"] == "x marks deleted labels"
    assert evidence["bivariate_generating_function"]["y_convention"] == "y marks repair distance"
    assert evidence["bivariate_generating_function"]["H_formula"] == (
        "H(x,z)=product_s(sum_{d=0}^{s-1} binom(s,d)x^d+z*x^s), s in {1,1,2,5}"
    )
    assert evidence["bivariate_generating_function"]["P_formula"] == (
        "P(x,y)=(1+x)^6(1+x*y)*Transform_z_to_y(H), z^r -> y^max(0,r-2)"
    )
    assert evidence["claims"] == {
        "all_65536_deletion_sets_enumerated": True,
        "exact_minimum_repair_distance": True,
        "bivariate_formula_verified": True,
        "rho_at_most_three": True,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "SYMPY_CROSSCHECK_PASS",
        "support_count": 65536,
        "full_minimal_support_count": 25,
        "distance_distribution": distribution,
        "P_x_at_y1": "(1+x)^16",
        "P_1_at_y": "30400+32704y+2368y^2+64y^3",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
