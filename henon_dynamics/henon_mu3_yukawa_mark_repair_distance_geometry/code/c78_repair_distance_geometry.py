#!/usr/bin/env python3
r"""Produce the C78 exact repair-distance geometry certificate.

For a deletion set D, the retained support is A=L\D.  The repair distance
rho(D) is the least number of labels from D that must be restored so that
A union R generates the full named core.  The C73 generation criterion says
that S9 must be present and at least two of four projective direction blocks
must be hit.  Consequently rho(D)=1_{S9 in D}+max(0,t(D)-2), where t(D) is
the number of direction blocks completely deleted.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from math import comb
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C77 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_mobius_reliability"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
OUT = PROJECT / "results/c78_repair_distance_geometry_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{i}" for i in range(1, 17))
ALL_MASK = (1 << 16) - 1
EXPECTED = {
    "c77": "f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634",
    "c77_manifest": "bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc",
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def mask_for(labels: list[str]) -> int:
    result = 0
    for label in labels:
        result |= 1 << (int(label[1:]) - 1)
    return result


def coefficient_map_add(target: dict[tuple[int, int], int], key: tuple[int, int], value: int) -> None:
    target[key] = target.get(key, 0) + value
    if target[key] == 0:
        del target[key]


def main() -> None:
    paths = {
        "c77": C77 / "results/c77_subgroup_mobius_reliability_evidence.json",
        "c77_manifest": C77 / "C77_PREFREEZE_MANIFEST.json",
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c73_manifest": C73 / "C73_PREFREEZE_MANIFEST.json",
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == EXPECTED
    c77 = json.loads(raw["c77"])
    c73 = json.loads(raw["c73"])
    c75 = json.loads(raw["c75"])
    c76 = json.loads(raw["c76"])
    assert c77["status"] == c73["status"] == c75["status"] == c76["status"] == "PREFREEZE_G3_PASS"
    assert c77["scope_literal"] == c73["scope_literal"] == c75["scope_literal"] == c76["scope_literal"] == FIREWALL
    assert c77["authority"]["c73"] == EXPECTED["c73"]
    assert c77["authority"]["c73_manifest"] == EXPECTED["c73_manifest"]
    assert c77["authority"]["c75"] == EXPECTED["c75"]
    assert c77["authority"]["c75_manifest"] == EXPECTED["c75_manifest"]
    assert c77["authority"]["c76"] == EXPECTED["c76"]
    assert c77["authority"]["c76_manifest"] == EXPECTED["c76_manifest"]
    assert c76["authority"]["c75"] == EXPECTED["c75"]
    assert c76["authority"]["c75_manifest"] == EXPECTED["c75_manifest"]
    assert c76["source_model"]["support_count"] == 65536
    assert c76["full_core_minimality"]["support_count"] == 25
    assert c77["subgroup_poset"]["subgroup_count"] == 20
    assert c73["generation_structure"]["criterion"] == (
        "a support generates 8C iff it contains S9 and meets at least two direction blocks"
    )

    blocks = [row["labels"] for row in c73["generation_structure"]["projective_direction_blocks"]]
    block_sizes = [len(block) for block in blocks]
    assert block_sizes == [1, 1, 2, 5]
    block_masks = [mask_for(block) for block in blocks]
    pivot_label = c73["generation_structure"]["pivot"]
    pivot_bit = mask_for([pivot_label])
    dummy_labels = c73["generation_structure"]["dummy_labels"]
    assert len(dummy_labels) == 6
    assert pivot_label == "S9"
    assert pivot_bit & sum(block_masks) == 0

    def generates(retained_mask: int) -> bool:
        if not retained_mask & pivot_bit:
            return False
        hit = sum(bool(retained_mask & mask) for mask in block_masks)
        return hit >= 2

    def repair_distance(deleted_mask: int) -> int:
        pivot_missing = int(bool(deleted_mask & pivot_bit))
        fully_deleted = sum((deleted_mask & block_mask) == block_mask for block_mask in block_masks)
        return pivot_missing + max(0, fully_deleted - 2)

    # Enumerate every deletion set and retain both marginal tables.
    distribution = Counter()
    by_deleted = [Counter() for _ in range(17)]
    by_retained = [Counter() for _ in range(17)]
    distance_masks: dict[int, list[int]] = {0: [], 1: [], 2: [], 3: []}
    coefficient_table: Counter[tuple[int, int]] = Counter()
    for deleted_mask in range(1 << 16):
        distance = repair_distance(deleted_mask)
        assert 0 <= distance <= 3
        retained_mask = ALL_MASK ^ deleted_mask
        assert (distance == 0) == generates(retained_mask)
        deleted_count = deleted_mask.bit_count()
        retained_count = retained_mask.bit_count()
        distribution[distance] += 1
        by_deleted[deleted_count][distance] += 1
        by_retained[retained_count][distance] += 1
        distance_masks[distance].append(deleted_mask)
        coefficient_table[(deleted_count, distance)] += 1

    assert dict(sorted(distribution.items())) == {0: 30400, 1: 32704, 2: 2368, 3: 64}
    assert sum(distribution.values()) == 1 << 16
    assert max(distribution) == 3

    # Combinatorial bivariate generating function. x marks deletions and z
    # marks completely deleted direction blocks before z^r -> y^max(0,r-2).
    h_xz: Counter[tuple[int, int]] = Counter({(0, 0): 1})
    for size in block_sizes:
        factor: Counter[tuple[int, int]] = Counter()
        for deleted in range(size):
            factor[(deleted, 0)] += comb(size, deleted)
        factor[(size, 1)] += 1
        product_table: Counter[tuple[int, int]] = Counter()
        for (left_degree, left_full), left_coeff in h_xz.items():
            for (right_degree, right_full), right_coeff in factor.items():
                product_table[(left_degree + right_degree, left_full + right_full)] += left_coeff * right_coeff
        h_xz = product_table
    transformed: Counter[tuple[int, int]] = Counter()
    for (degree, full_blocks), coefficient in h_xz.items():
        transformed[(degree, max(0, full_blocks - 2))] += coefficient
    # Six dummy labels contribute (1+x), and deleted pivot contributes xy.
    with_dummy_pivot: Counter[tuple[int, int]] = Counter()
    for (degree, distance), coefficient in transformed.items():
        for dummy_deleted in range(7):
            # six dummies plus pivot: pivot not deleted (distance 0) or deleted (distance +1)
            for pivot_deleted in (0, 1):
                coefficient_factor = comb(6, dummy_deleted)
                with_dummy_pivot[(degree + dummy_deleted + pivot_deleted,
                                  distance + pivot_deleted)] += coefficient * coefficient_factor
    assert dict(with_dummy_pivot) == dict(coefficient_table)

    def map_terms(table: Counter[tuple[int, int]]) -> dict[str, int]:
        return {f"{x},{y}": table[(x, y)] for x, y in sorted(table) if table[(x, y)]}

    p_x1 = {degree: sum(value for (x, y), value in coefficient_table.items() if x == degree)
            for degree in range(17)}
    p_1y = {distance: sum(value for (x, y), value in coefficient_table.items() if y == distance)
            for distance in range(4)}
    assert p_x1 == {degree: comb(16, degree) for degree in range(17)}
    assert p_1y == {0: 30400, 1: 32704, 2: 2368, 3: 64}

    result: dict[str, Any] = {
        "schema_id": "hcs-c78-repair-distance-geometry-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": EXPECTED,
        "definition": {
            "deleted_set": "D",
            "retained_set": "A=L\\D",
            "repair_distance": "rho(D)=min{|R|: R subset D and Phi((L\\D) union R)=Q}",
            "pivot": pivot_label,
            "direction_blocks": blocks,
            "direction_block_sizes": block_sizes,
            "dummy_labels": dummy_labels,
            "formula": "rho(D)=1_{S9 in D}+max(0,t(D)-2), t(D)=number of fully deleted direction blocks",
            "maximum_distance": 3,
        },
        "repair_distance_atlas": {
            "deletion_count_distribution": {str(distance): distribution[distance] for distance in range(4)},
            "by_deleted_cardinality": [
                {"deleted_count": size, "distance_counts": {str(distance): by_deleted[size][distance] for distance in range(4)}}
                for size in range(17)
            ],
            "by_retained_cardinality": [
                {"retained_count": size, "distance_counts": {str(distance): by_retained[size][distance] for distance in range(4)}}
                for size in range(17)
            ],
            "distance_three_masks": sorted(distance_masks[3]),
        },
        "bivariate_generating_function": {
            "x_convention": "x marks deleted labels",
            "y_convention": "y marks repair distance",
            "H_formula": "H(x,z)=product_s(sum_{d=0}^{s-1} binom(s,d)x^d+z*x^s), s in {1,1,2,5}",
            "P_formula": "P(x,y)=(1+x)^6(1+x*y)*Transform_z_to_y(H), z^r -> y^max(0,r-2)",
            "coefficient_table": map_terms(coefficient_table),
            "P_x_at_y1": {str(degree): p_x1[degree] for degree in range(17)},
            "P_1_at_y": {str(distance): p_1y[distance] for distance in range(4)},
        },
        "claims": {
            "all_65536_deletion_sets_enumerated": True,
            "exact_minimum_repair_distance": True,
            "bivariate_formula_verified": True,
            "rho_at_most_three": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "support_count": 1 << 16,
        "distance_distribution": result["repair_distance_atlas"]["deletion_count_distribution"],
        "P_x_at_y1": result["bivariate_generating_function"]["P_x_at_y1"],
        "P_1_at_y": result["bivariate_generating_function"]["P_1_at_y"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
