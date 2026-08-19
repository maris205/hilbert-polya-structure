#!/usr/bin/env python3
"""Independent exact checker for the C77 subgroup reliability certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
EVIDENCE = PROJECT / "results/c77_subgroup_mobius_reliability_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
HASHES = {
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
}


def canon(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def add(left, right):
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient, value):
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def point_order(value):
    for candidate in range(1, 55):
        if multiple(candidate, value) == (0, 0, 0):
            return candidate
    raise AssertionError


def cyclic(value):
    return frozenset(multiple(k, value) for k in range(point_order(value)))


def add_poly(poly, power, coefficient):
    poly[power] = poly.get(power, 0) + coefficient
    if poly[power] == 0:
        del poly[power]


def terms(poly):
    return {str(power): coefficient for power, coefficient in sorted(poly.items()) if coefficient}


def evaluate(poly, q):
    return sum(coefficient * q ** power for power, coefficient in poly.items())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    evidence_raw = args.evidence.read_bytes()
    evidence = json.loads(evidence_raw)
    assert evidence_raw == canon(evidence)
    assert evidence["schema_id"] == "hcs-c77-subgroup-mobius-reliability-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL

    source_paths = {
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c73_manifest": C73 / "C73_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in source_paths.items()} == HASHES
    assert evidence["authority"] == HASHES
    c76 = json.loads(source_paths["c76"].read_text())
    c75 = json.loads(source_paths["c75"].read_text())
    c73 = json.loads(source_paths["c73"].read_text())
    assert c76["status"] == c75["status"] == c73["status"] == "PREFREEZE_G3_PASS"
    assert c76["scope_literal"] == c75["scope_literal"] == c73["scope_literal"] == FIREWALL
    assert c76["support_orbit_atlas"]["support_count"] == 65536
    assert c76["closure_atlas"]["subgroup_count"] == 20
    expected_top = {"0": 1, "1": -1, "4": -1, "5": 1, "7": -1, "8": -1, "9": 5, "10": -3}
    assert c73["exact_reliability"]["homogeneous_expanded_coefficients"] == expected_top

    rows = c75["closure_incidence"]["all_subgroups"]
    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    subgroups = [frozenset(tuple(point) for point in row["subgroup_points"]) for row in rows]
    assert len(subgroups) == 20 and len(set(subgroups)) == 20
    subgroup_index = {subgroup: index for index, subgroup in enumerate(subgroups)}
    n_values = [sum(point in subgroup for point in coordinates) for subgroup in subgroups]
    assert n_values == [5, 6, 7, 6, 7, 6, 8, 7, 8, 7, 11, 7, 7, 8, 12, 8, 8, 9, 15, 16]
    lower = [[index for index, subgroup in enumerate(subgroups) if subgroup <= subgroups[upper]]
             for upper in range(20)]
    mobius = [[0] * 20 for _ in range(20)]
    for upper in range(20):
        for lower_index in sorted(lower[upper], key=lambda index: (len(subgroups[index]), index)):
            if lower_index == upper:
                mobius[lower_index][upper] = 1
            else:
                mobius[lower_index][upper] = -sum(
                    mobius[lower_index][middle]
                    for middle in lower[upper]
                    if middle != upper and subgroups[lower_index] <= subgroups[middle]
                    and subgroups[middle] < subgroups[upper]
                )
    assert evidence["subgroup_poset"]["n_H_vector"] == n_values
    assert evidence["subgroup_poset"]["inclusion_matrix"] == [
        [int(subgroups[left] <= subgroups[right]) for right in range(20)] for left in range(20)
    ]
    assert evidence["mobius_matrix"] == mobius

    cyclics = [cyclic(point) for point in coordinates]
    def extend(left, right):
        return frozenset(add(a, b) for a in left for b in right)
    extension = [[subgroup_index[extend(subgroup, cyclics[label])] for label in range(16)]
                 for subgroup in subgroups]
    zero = subgroup_index[frozenset({(0, 0, 0)})]
    closure = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        closure[mask] = extension[closure[mask ^ low]][low.bit_length() - 1]
    counts = [0] * 20
    by_size = [Counter() for _ in range(20)]
    for mask, index in enumerate(closure):
        counts[index] += 1
        by_size[index][mask.bit_count()] += 1
    assert sum(counts) == 65536
    assert evidence["direct_enumeration"]["support_count"] == 65536
    assert evidence["direct_enumeration"]["generated_support_count_by_subgroup"] == {
        str(index): count for index, count in enumerate(counts)
    }
    assert evidence["direct_enumeration"]["retained_cardinality_total"] == [
        sum(counter[size] for counter in by_size) for size in range(17)
    ]

    expected_rows = []
    exact_polys = []
    from math import comb
    for upper, subgroup in enumerate(subgroups):
        exact = {}
        for lower_index in lower[upper]:
            add_poly(exact, 16 - n_values[lower_index], mobius[lower_index][upper])
        direct = {}
        for retained, count in by_size[upper].items():
            for deleted in range(retained + 1):
                add_poly(direct, 16 - retained + deleted,
                         count * comb(retained, deleted) * ((-1) ** deleted))
        assert direct == exact
        exact_polys.append(exact)
        expected_rows.append({
            "subgroup_index": upper,
            "subgroup_order": len(subgroup),
            "subgroup_points": [list(point) for point in sorted(subgroup)],
            "n_H": n_values[upper],
            "P_leq_polynomial": {str(16 - n_values[upper]): 1},
            "P_eq_polynomial": terms(exact),
            "direct_support_count": counts[upper],
            "direct_by_retained_cardinality": {
                str(size): by_size[upper][size] for size in sorted(by_size[upper])
            },
        })
    assert evidence["subgroup_poset"]["rows"] == expected_rows
    summed = {}
    for poly in exact_polys:
        for power, coefficient in poly.items(): add_poly(summed, power, coefficient)
    assert summed == {0: 1}
    assert evidence["reliability"]["sum_exact_polynomial"] == {"0": 1}
    assert exact_polys[-1] == {0: 1, 1: -1, 4: -1, 5: 1, 7: -1, 8: -1, 9: 5, 10: -3}
    reliability = evidence["reliability"]
    assert reliability["top_subgroup_index"] == 19
    assert reliability["top_polynomial"] == expected_top
    assert reliability["top_matches_c73"] is True
    assert reliability["nonnegative_on_rational_grid"] is True
    grid = [Fraction(index, reliability["rational_grid_denominator"]) for index in range(21)]
    assert reliability["rational_grid_points"] == [str(q) for q in grid]
    assert all(evaluate(poly, q) >= 0 for poly in exact_polys for q in grid)
    assert evidence["claims"] == {
        "all_20_actual_subgroups_enumerated": True,
        "exact_mobius_inversion": True,
        "direct_65536_support_semantics": True,
        "top_polynomial_matches_c73": True,
        "full_burnside_ring_claimed": False,
        "full_table_of_marks_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "PASS",
        "subgroup_count": 20,
        "support_count": 65536,
        "top_polynomial_matches_c73": True,
        "sum_polynomial": {"0": 1},
        "nonnegative_on_rational_grid": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
