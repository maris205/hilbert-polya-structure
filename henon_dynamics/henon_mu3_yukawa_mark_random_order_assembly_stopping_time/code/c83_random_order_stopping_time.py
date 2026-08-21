#!/usr/bin/env python3
"""Produce the exact random-order prefix assembly stopping-time certificate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from itertools import product
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
C81 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile"
OUT = PROJECT / "results/c83_random_order_stopping_time_evidence.json"
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


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(a, b, moduli=(9, 3, 2)):
    return tuple((x + y) % m for x, y, m in zip(a, b, moduli))


def multiple(k, a, moduli=(9, 3, 2)):
    return tuple(k * x % m for x, m in zip(a, moduli))


def cyclic(a):
    for order in range(1, 55):
        if multiple(order, a) == (0, 0, 0):
            return frozenset(multiple(k, a) for k in range(order))
    raise AssertionError(a)


def main() -> None:
    paths = {
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
        "c81": C81 / "results/c81_effective_orbit_repair_profile_evidence.json",
        "c81_manifest": C81 / "C81_PREFREEZE_MANIFEST.json",
    }
    raw = {name: (path.read_bytes() if path.exists() else b"") for name, path in paths.items()}
    observed = {name: digest(value) for name, value in raw.items()}
    for name, expected in HASHES.items():
        if not expected.startswith("PENDING"):
            assert observed[name] == expected, (name, observed[name], expected)
    c76 = json.loads(raw["c76"])
    c78 = json.loads(raw["c78"])
    assert c76["status"] == c78["status"] == "PREFREEZE_G3_PASS"
    assert c76["scope_literal"] == c78["scope_literal"] == FIREWALL
    assert c76["source_model"]["support_count"] == 65536
    assert c76["full_core_minimality"]["support_count"] == 25

    points = list(product(range(9), range(3), range(2)))
    point_index = {point: i for i, point in enumerate(points)}
    rows = json.loads((C75 / "results/c75_closure_incidence_lift_evidence.json").read_text())[
        "closure_incidence"]["all_subgroups"]
    subgroup_masks = [sum(1 << point_index[tuple(p)] for p in row["subgroup_points"])
                      for row in rows]
    subgroup_index = {mask: i for i, mask in enumerate(subgroup_masks)}
    coordinates = [tuple(p) for p in json.loads(
        (C75 / "results/c75_closure_incidence_lift_evidence.json").read_text()
    )["named_coordinate_source"]["coordinates"]]
    cyclic_masks = [sum(1 << point_index[p] for p in cyclic(point)) for point in coordinates]

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
    for support in range(1, 1 << 16):
        low = support & -support
        closure[support] = transition[closure[support ^ low]][low.bit_length() - 1]
    assert closure[ALL] == full

    full_support_count_by_size = Counter()
    pivotal_count_by_size = Counter()
    pivotal_pattern = Counter()
    for support in range(1 << 16):
        if closure[support] != full:
            continue
        size = support.bit_count()
        pivotal = sum(closure[support ^ (1 << bit)] != full
                      for bit in range(16) if support & (1 << bit))
        assert pivotal >= 1
        full_support_count_by_size[size] += 1
        pivotal_count_by_size[size] += pivotal
        pivotal_pattern[(size, pivotal)] += 1
    assert dict(full_support_count_by_size) == {
        3: 25, 4: 224, 5: 940, 6: 2461, 7: 4504, 8: 6095,
        9: 6269, 10: 4950, 11: 2992, 12: 1364, 13: 455,
        14: 105, 15: 15, 16: 1,
    }

    permutation_count_by_time = {}
    for k in range(17):
        pivotal_total = pivotal_count_by_size[k]
        permutation_count_by_time[str(k)] = (
            pivotal_total * factorial(k - 1) * factorial(16 - k) if k else 0
        )
    total_permutations = factorial(16)
    assert sum(permutation_count_by_time.values()) == total_permutations
    probabilities = {}
    for k, count in permutation_count_by_time.items():
        probabilities[k] = {"numerator": Fraction(count, total_permutations).numerator,
                            "denominator": Fraction(count, total_permutations).denominator}
    expected_time = Fraction(sum(int(k) * value for k, value in permutation_count_by_time.items()),
                             total_permutations)
    survival = {
        str(k): sum(value for time, value in permutation_count_by_time.items() if int(time) > k)
        for k in range(17)
    }
    result: dict[str, Any] = {
        "schema_id": "hcs-c83-random-order-prefix-stopping-time-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "definition": {
            "random_object": "uniform permutation of the sixteen named labels",
            "prefix_support": "first k labels of the permutation",
            "stopping_time": "T=min{k: Phi(prefix_k)=Q}",
            "time_range": [3, 16],
            "pivotal_formula": "N_k=sum_{|S|=k, Phi(S)=Q} p(S)*(k-1)!*(16-k)!, p(S)=#{ell in S: Phi(S\\{ell}) != Q}",
        },
        "assembly_atlas": {
            "full_support_count_by_cardinality": {str(k): full_support_count_by_size[k]
                                                   for k in sorted(full_support_count_by_size)},
            "pivotal_support_count_by_cardinality": {str(k): pivotal_count_by_size[k]
                                                      for k in sorted(pivotal_count_by_size)},
            "pivotal_pattern_counts": {f"{k},{p}": value
                                        for (k, p), value in sorted(pivotal_pattern.items())},
            "permutation_count_by_stopping_time": permutation_count_by_time,
            "probability_by_stopping_time": probabilities,
            "survival_permutation_counts": survival,
            "total_permutations": total_permutations,
            "expected_stopping_time": {"numerator": expected_time.numerator,
                                        "denominator": expected_time.denominator},
        },
        "claims": {
            "all_full_supports_enumerated": True,
            "exact_uniform_permutation_distribution": True,
            "pivotal_prefix_formula_verified": True,
            "arithmetic_local_claimed": False,
            "full_burnside_ring_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "total_permutations": total_permutations,
                      "stopping_distribution": permutation_count_by_time,
                      "expected_stopping_time": result["assembly_atlas"]["expected_stopping_time"],
                      "evidence_sha256": digest(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
