#!/usr/bin/env python3
"""Produce the exact C80 all-subgroup containment-threshold atlas."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from itertools import product
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
OUT = PROJECT / "results/c80_threshold_repair_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
ALL_MASK = (1 << 16) - 1
HASHES = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient: int, value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def cyclic(value: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    for order in range(1, 55):
        if multiple(order, value) == (0, 0, 0):
            return frozenset(multiple(k, value) for k in range(order))
    raise AssertionError("finite order search failed")


def mask_for_points(points: frozenset[tuple[int, ...]], index: dict[tuple[int, ...], int]) -> int:
    return sum(1 << index[point] for point in points)


def main() -> None:
    paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c75, c76, c78 = (json.loads(raw[name]) for name in ("c75", "c76", "c78"))
    assert c75["status"] == c76["status"] == c78["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == c76["scope_literal"] == c78["scope_literal"] == FIREWALL
    assert c76["source_model"]["support_count"] == 65536
    assert c76["full_core_minimality"]["support_count"] == 25

    points = list(product(range(9), range(3), range(2)))
    point_index = {point: index for index, point in enumerate(points)}
    rows = c75["closure_incidence"]["all_subgroups"]
    subgroup_masks = [mask_for_points(frozenset(tuple(point) for point in row["subgroup_points"]), point_index)
                      for row in rows]
    subgroup_index = {mask: index for index, mask in enumerate(subgroup_masks)}
    coordinates = [tuple(point) for point in c75["named_coordinate_source"]["coordinates"]]
    cyclic_masks = [mask_for_points(cyclic(point), point_index) for point in coordinates]

    def extension(left: int, right: int) -> int:
        result = 0
        for left_index in range(54):
            if not left & (1 << left_index):
                continue
            for right_index in range(54):
                if right & (1 << right_index):
                    result |= 1 << point_index[add(points[left_index], points[right_index])]
        return result

    transition = [[subgroup_index[extension(subgroup, cyclic)] for cyclic in cyclic_masks]
                  for subgroup in subgroup_masks]
    zero = subgroup_index[mask_for_points(frozenset({(0, 0, 0)}), point_index)]
    closure = [zero] * (1 << 16)
    for support in range(1, 1 << 16):
        low = support & -support
        closure[support] = transition[closure[support ^ low]][low.bit_length() - 1]
    assert closure[ALL_MASK] == 19

    # Target containment is tested on subgroup bitsets, not by subgroup order.
    contains = [[(subgroup_masks[target] & ~subgroup_masks[closed]) == 0
                 for closed in range(20)] for target in range(20)]
    thresholds = [[0] * 20 for _ in range(1 << 16)]
    for target in range(20):
        values = [0] * (1 << 16)
        for support in range(ALL_MASK, -1, -1):
            if contains[target][closure[support]]:
                values[support] = 0
                continue
            best = 17
            deleted = ALL_MASK ^ support
            while deleted:
                low = deleted & -deleted
                best = min(best, values[support | low] + 1)
                deleted ^= low
            values[support] = best
        for support, value in enumerate(values):
            thresholds[support][target] = value

    # C78's exact-core row is the target Q row, with deletion-mask ordering.
    q_distribution = Counter(thresholds[support][19] for support in range(1 << 16))
    assert dict(sorted(q_distribution.items())) == {0: 30400, 1: 32704, 2: 2368, 3: 64}
    assert sum(thresholds[support][19] != 0 for support in range(1 << 16)) == 35136
    block_masks = [
        sum(1 << (int(label[1:]) - 1) for label in block)
        for block in c78["definition"]["direction_blocks"]
    ]
    pivot_bit = 1 << (int(c78["definition"]["pivot"][1:]) - 1)
    for support in range(1 << 16):
        deleted = ALL_MASK ^ support
        c78_rho = int(bool(deleted & pivot_bit)) + max(
            0, sum((deleted & block) == block for block in block_masks) - 2
        )
        assert thresholds[support][19] == c78_rho

    target_distributions = []
    target_tables = []
    for target, row in enumerate(rows):
        distribution = Counter(thresholds[support][target] for support in range(1 << 16))
        table = Counter(((ALL_MASK ^ support).bit_count(), thresholds[support][target])
                        for support in range(1 << 16))
        target_distributions.append({str(distance): distribution[distance] for distance in range(max(distribution) + 1)})
        target_tables.append({f"{deleted},{distance}": value for (deleted, distance), value in sorted(table.items())})

    result: dict[str, Any] = {
        "schema_id": "hcs-c80-subgroup-threshold-repair-atlas-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "definition": {
            "deleted_set": "D",
            "retained_set": "A=L\\D",
            "threshold": "tau_H(D)=min{|R|:R subset D and H subset Phi((L\\D) union R)}",
            "exact_core_boundary": "tau_Q(D)=rho(D)",
            "target_count": 20,
            "target_index_order": list(range(20)),
            "target_subgroup_orders": [row["subgroup_order"] for row in rows],
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": 16,
            "support_count": 1 << 16,
            "subgroup_count": 20,
            "full_target_index": 19,
        },
        "target_atlas": {
            "threshold_distributions": target_distributions,
            "deleted_cardinality_tables": target_tables,
            "profile_rows": [
                {"retained_mask": support, "deletion_mask": ALL_MASK ^ support,
                 "thresholds": thresholds[support]}
                for support in range(1 << 16)
            ],
        },
        "checks": {
            "all_65536_supports_enumerated": True,
            "all_20_targets_present": True,
            "tau_Q_equals_c78_rho": True,
            "threshold_monotone_under_target_inclusion": True,
        },
        "claims": {
            "arithmetic_local_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
        },
    }
    # Verify monotonicity with the subgroup row bitsets before serializing.
    for left in range(20):
        for right in range(20):
            if subgroup_masks[left] & ~subgroup_masks[right] == 0:
                assert all(thresholds[support][left] <= thresholds[support][right]
                           for support in range(1 << 16))
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"], "support_count": 1 << 16,
        "target_count": 20, "q_distribution": dict(sorted(q_distribution.items())),
        "profile_rows": 1 << 16, "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
