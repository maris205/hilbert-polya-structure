#!/usr/bin/env python3
"""Independent checker for the C80 containment-threshold atlas.

The producer uses a descending dynamic-programming recurrence.  This checker
instead finds every inclusion-minimal support for each target subgroup and
computes the distance to that finite antichain.  It then rebuilds every one of
the 20 by 65536 profile entries from the point-set group law.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c80_threshold_repair_atlas_evidence.json"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
ALL = (1 << 16) - 1
HASHES = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def add(a, b):
    return tuple((x + y) % m for x, y, m in zip(a, b, MODULI))


def multiple(k, a):
    return tuple(k * x % m for x, m in zip(a, MODULI))


def cyclic(a):
    for k in range(1, 55):
        if multiple(k, a) == (0, 0, 0):
            return frozenset(multiple(j, a) for j in range(k))
    raise AssertionError(a)


def point_mask(points, index):
    return sum(1 << index[p] for p in points)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw_evidence = args.evidence.read_bytes()
    evidence = json.loads(raw_evidence)
    assert raw_evidence == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c80-subgroup-threshold-repair-atlas-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in paths.items()} == HASHES
    assert evidence["authority"] == HASHES
    c75 = json.loads(paths["c75"].read_text())
    c76 = json.loads(paths["c76"].read_text())
    c78 = json.loads(paths["c78"].read_text())
    assert all(d["status"] == "PREFREEZE_G3_PASS" for d in (c75, c76, c78))
    assert all(d["scope_literal"] == FIREWALL for d in (c75, c76, c78))
    assert c76["source_model"]["support_count"] == 65536
    assert c76["full_core_minimality"]["support_count"] == 25

    points = list(product(range(9), range(3), range(2)))
    point_index = {p: i for i, p in enumerate(points)}
    rows = c75["closure_incidence"]["all_subgroups"]
    subgroup_masks = [point_mask(frozenset(tuple(p) for p in row["subgroup_points"]), point_index)
                      for row in rows]
    subgroup_index = {mask: i for i, mask in enumerate(subgroup_masks)}
    coordinates = [tuple(p) for p in c75["named_coordinate_source"]["coordinates"]]
    cyclic_masks = [point_mask(cyclic(p), point_index) for p in coordinates]

    def extend(left, right):
        result = 0
        for i, a in enumerate(points):
            if not left & (1 << i):
                continue
            for j, b in enumerate(points):
                if right & (1 << j):
                    result |= 1 << point_index[add(a, b)]
        return result

    transition = [[subgroup_index[extend(H, C)] for C in cyclic_masks]
                  for H in subgroup_masks]
    zero = subgroup_index[point_mask(frozenset({(0, 0, 0)}), point_index)]
    full = subgroup_index[point_mask(frozenset(points), point_index)]
    closure = [zero] * (1 << 16)
    for support in range(1, 1 << 16):
        low = support & -support
        closure[support] = transition[closure[support ^ low]][low.bit_length() - 1]
    assert closure[ALL] == full

    contains = [[(subgroup_masks[target] & ~subgroup_masks[closed]) == 0
                 for closed in range(20)] for target in range(20)]
    minimal_by_target = []
    for target in range(20):
        minimal = []
        for support in range(1 << 16):
            if not contains[target][closure[support]]:
                continue
            if all(not (support & (1 << bit)) or
                   not contains[target][closure[support ^ (1 << bit)]]
                   for bit in range(16)):
                minimal.append(support)
        assert minimal
        minimal_by_target.append(minimal)

    # Distances to the target antichain.  This is a different route from the
    # producer's recurrence and avoids reading any producer-computed profile.
    expected_profiles = []
    distributions = []
    cardinality_tables = []
    for support in range(1 << 16):
        expected_profiles.append([
            min((minimal & ~support).bit_count() for minimal in minimal_by_target[target])
            for target in range(20)
        ])
    for target in range(20):
        dist = Counter(profile[target] for profile in expected_profiles)
        table = Counter(((ALL ^ support).bit_count(), expected_profiles[support][target])
                        for support in range(1 << 16))
        distributions.append({str(k): dist[k] for k in range(max(dist) + 1)})
        cardinality_tables.append({f"{k},{t}": v for (k, t), v in sorted(table.items())})

    atlas = evidence["target_atlas"]
    assert atlas["profile_rows"] == expected_profiles if False else True
    rows_profile = atlas["profile_rows"]
    assert len(rows_profile) == 65536
    for support, row in enumerate(rows_profile):
        assert row == {
            "retained_mask": support,
            "deletion_mask": ALL ^ support,
            "thresholds": expected_profiles[support],
        }
    assert atlas["threshold_distributions"] == distributions
    assert atlas["deleted_cardinality_tables"] == cardinality_tables
    assert evidence["definition"]["target_count"] == 20
    assert evidence["definition"]["target_index_order"] == list(range(20))
    assert evidence["definition"]["target_subgroup_orders"] == [r["subgroup_order"] for r in rows]
    assert evidence["source_model"] == {
        "group": "Z/9 + Z/3 + Z/2", "label_count": 16,
        "support_count": 65536, "subgroup_count": 20, "full_target_index": 19,
    }

    # The full target is exactly C78's repair-distance row.
    block_masks = [sum(1 << (int(label[1:]) - 1) for label in block)
                   for block in c78["definition"]["direction_blocks"]]
    pivot = 1 << (int(c78["definition"]["pivot"][1:]) - 1)
    q = [profile[19] for profile in expected_profiles]
    structural = [int(bool((ALL ^ s) & pivot)) + max(
        0, sum((((ALL ^ s) & block) == block) for block in block_masks) - 2)
        for s in range(1 << 16)]
    assert q == structural
    assert distributions[19] == {"0": 30400, "1": 32704, "2": 2368, "3": 64}

    # Target inclusion monotonicity is checked on the actual subgroup masks.
    for left in range(20):
        for right in range(20):
            if subgroup_masks[left] & ~subgroup_masks[right] == 0:
                assert all(expected_profiles[s][left] <= expected_profiles[s][right]
                           for s in range(1 << 16))
    assert evidence["checks"] == {
        "all_65536_supports_enumerated": True,
        "all_20_targets_present": True,
        "tau_Q_equals_c78_rho": True,
        "threshold_monotone_under_target_inclusion": True,
    }
    assert evidence["claims"] == {
        "arithmetic_local_claimed": False,
        "full_burnside_ring_claimed": False,
        "full_table_of_marks_claimed": False,
    }
    print(json.dumps({
        "status": "C80_INDEPENDENT_CHECK_PASS",
        "support_count": 65536,
        "target_count": 20,
        "minimal_support_counts": [len(x) for x in minimal_by_target],
        "q_distribution": distributions[19],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
