#!/usr/bin/env python3
"""Independent checker for the C83 random-order stopping-time receipt."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from itertools import product
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c83_random_order_stopping_time_evidence.json"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
C81 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
ALL = (1 << 16) - 1
HASHES = {
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
    "c81": "c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f",
    "c81_manifest": "110d8119169515bf38ca00906ab0cb51264a100f961bfa00142886b326fa6141",
}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def add(a, b):
    return tuple((x + y) % m for x, y, m in zip(a, b, (9, 3, 2)))


def multiple(k, a):
    return tuple(k * x % m for x, m in zip(a, (9, 3, 2)))


def cyclic(a):
    for k in range(1, 55):
        if multiple(k, a) == (0, 0, 0):
            return frozenset(multiple(j, a) for j in range(k))
    raise AssertionError(a)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c83-random-order-prefix-stopping-time-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    paths = {
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
        "c81": C81 / "results/c81_effective_orbit_repair_profile_evidence.json",
        "c81_manifest": C81 / "C81_PREFREEZE_MANIFEST.json",
    }
    observed = {name: digest(path.read_bytes()) if path.exists() else digest(b"")
                for name, path in paths.items()}
    for name, expected in HASHES.items():
        if not expected.startswith("PENDING"):
            assert observed[name] == expected
    assert evidence["authority"] == HASHES
    c76 = json.loads(paths["c76"].read_text())
    c78 = json.loads(paths["c78"].read_text())
    assert c76["status"] == c78["status"] == "PREFREEZE_G3_PASS"
    assert c76["scope_literal"] == c78["scope_literal"] == FIREWALL
    assert c76["full_core_minimality"]["support_count"] == 25

    c75 = json.loads((C75 / "results/c75_closure_incidence_lift_evidence.json").read_text())
    points = list(product(range(9), range(3), range(2)))
    point_index = {p: i for i, p in enumerate(points)}
    rows = c75["closure_incidence"]["all_subgroups"]
    subgroup_masks = [sum(1 << point_index[tuple(p)] for p in row["subgroup_points"])
                      for row in rows]
    subgroup_index = {mask: i for i, mask in enumerate(subgroup_masks)}
    coords = [tuple(p) for p in c75["named_coordinate_source"]["coordinates"]]
    cyclic_masks = [sum(1 << point_index[p] for p in cyclic(point)) for point in coords]

    def extend(left, right):
        result = 0
        for i, a in enumerate(points):
            if left & (1 << i):
                for j, b in enumerate(points):
                    if right & (1 << j):
                        result |= 1 << point_index[add(a, b)]
        return result

    transition = [[subgroup_index[extend(H, C)] for C in cyclic_masks]
                  for H in subgroup_masks]
    zero = subgroup_index[1 << point_index[(0, 0, 0)]]
    full = subgroup_index[subgroup_masks[-1]]
    closure = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        closure[mask] = transition[closure[mask ^ low]][low.bit_length() - 1]
    assert closure[ALL] == full

    full_by_size = Counter()
    pivotal_by_size = Counter()
    pattern = Counter()
    for support in range(1 << 16):
        if closure[support] != full:
            continue
        size = support.bit_count()
        pivotal = sum(closure[support ^ (1 << bit)] != full
                      for bit in range(16) if support & (1 << bit))
        full_by_size[size] += 1
        pivotal_by_size[size] += pivotal
        pattern[(size, pivotal)] += 1

    atlas = evidence["assembly_atlas"]
    assert atlas["full_support_count_by_cardinality"] == {
        str(k): full_by_size[k] for k in sorted(full_by_size)
    }
    assert atlas["pivotal_support_count_by_cardinality"] == {
        str(k): pivotal_by_size[k] for k in sorted(pivotal_by_size)
    }
    assert atlas["pivotal_pattern_counts"] == {
        f"{k},{p}": value for (k, p), value in sorted(pattern.items())
    }
    stopping = {
        str(k): (pivotal_by_size[k] * factorial(k - 1) * factorial(16 - k) if k else 0)
        for k in range(17)
    }
    assert atlas["permutation_count_by_stopping_time"] == stopping
    total = factorial(16)
    assert atlas["total_permutations"] == total
    assert sum(stopping.values()) == total
    expected_probabilities = {}
    for k, count in stopping.items():
        f = Fraction(count, total)
        expected_probabilities[k] = {"numerator": f.numerator, "denominator": f.denominator}
    assert atlas["probability_by_stopping_time"] == expected_probabilities
    survival = {str(k): sum(v for time, v in stopping.items() if int(time) > k)
                for k in range(17)}
    assert atlas["survival_permutation_counts"] == survival
    expected_time = Fraction(sum(int(k) * v for k, v in stopping.items()), total)
    assert atlas["expected_stopping_time"] == {
        "numerator": expected_time.numerator, "denominator": expected_time.denominator
    }
    assert evidence["definition"] == {
        "random_object": "uniform permutation of the sixteen named labels",
        "prefix_support": "first k labels of the permutation",
        "stopping_time": "T=min{k: Phi(prefix_k)=Q}",
        "time_range": [3, 16],
        "pivotal_formula": "N_k=sum_{|S|=k, Phi(S)=Q} p(S)*(k-1)!*(16-k)!, p(S)=#{ell in S: Phi(S\\{ell}) != Q}",
    }
    assert evidence["claims"] == {
        "all_full_supports_enumerated": True,
        "exact_uniform_permutation_distribution": True,
        "pivotal_prefix_formula_verified": True,
        "arithmetic_local_claimed": False,
        "full_burnside_ring_claimed": False,
    }
    print(json.dumps({"status": "C83_INDEPENDENT_CHECK_PASS",
                      "total_permutations": total,
                      "stopping_distribution": stopping,
                      "expected_stopping_time": atlas["expected_stopping_time"]}, sort_keys=True))


if __name__ == "__main__":
    main()
