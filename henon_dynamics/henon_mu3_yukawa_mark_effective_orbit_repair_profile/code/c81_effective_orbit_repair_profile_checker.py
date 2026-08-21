#!/usr/bin/env python3
"""Independent checker for the C81 effective-group repair-profile quotient."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from hashlib import sha256
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c81_effective_orbit_repair_profile_evidence.json"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
C79 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity"
C80 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
ALL = (1 << 16) - 1
HASHES = {
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
    "c79": "147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879",
    "c79_manifest": "982cce509de371d59c4b87cda75af057d994c6fc36146daddc3b983c9c63246c",
    "c80": "8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5",
    "c80_manifest": "a674116ab6f8f9478130219cc525478525f10f2e42f515e71418a3066e2b229c",
}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def compose(left, right):
    return tuple(left[right[i]] for i in range(16))


def group_from(generators):
    identity = tuple(range(16))
    found = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in found:
                found.add(candidate)
                queue.append(candidate)
    return sorted(found)


def apply_mask(mask, permutation):
    result = 0
    while mask:
        low = mask & -mask
        result |= 1 << permutation[low.bit_length() - 1]
        mask ^= low
    return result


def cycles(permutation):
    seen = set()
    count = 0
    for start in range(16):
        if start in seen:
            continue
        count += 1
        current = start
        while current not in seen:
            seen.add(current)
            current = permutation[current]
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c81-effective-1920-repair-profile-orbit-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    paths = {
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
        "c79": C79 / "results/c79_repair_witness_multiplicity_evidence.json",
        "c79_manifest": C79 / "C79_PREFREEZE_MANIFEST.json",
        "c80": C80 / "results/c80_threshold_repair_atlas_evidence.json",
        "c80_manifest": C80 / "C80_PREFREEZE_MANIFEST.json",
    }
    observed = {name: digest(path.read_bytes()) if path.exists() else digest(b"")
                for name, path in paths.items()}
    for name, expected in HASHES.items():
        if not expected.startswith("PENDING"):
            assert observed[name] == expected
    assert evidence["authority"] == HASHES
    c75 = json.loads((C75 / "results/c75_closure_incidence_lift_evidence.json").read_text())
    c76, c78, c79, c80 = (json.loads(paths[name].read_text())
                           for name in ("c76", "c78", "c79", "c80"))
    assert all(doc["scope_literal"] == FIREWALL for doc in (c76, c78, c79, c80))
    assert c76["source_model"]["effective_label_group_order"] == 1920
    assert c76["source_model"]["c75_lifted_group_order"] == 11520
    assert c76["source_model"]["c75_ambient_c6_kernel_order"] == 6
    source_model = evidence["source_model"]
    assert source_model["group"] == "Z/9 + Z/3 + Z/2"
    assert source_model["label_count"] == 16
    assert source_model["support_count"] == 65536
    assert source_model["c75_ambient_lift_order"] == 11520
    assert source_model["c75_lift_kernel_order"] == 6
    assert source_model["effective_label_group_order"] == 1920
    assert source_model["effective_group_candidate"] == "S5 x C2 x D8"
    assert source_model["generator_names"] == list(
        ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition",
         "fiber_F9_transposition", "ambient_s"))

    names = ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition",
             "fiber_F9_transposition", "ambient_s")
    rows_by_name = {row["name"]: row for row in c75["lifted_symmetry"]["generators"]}
    group = group_from([tuple(rows_by_name[name]["label_permutation"]) for name in names])
    assert len(group) == 1920
    assert c76["source_model"]["effective_label_group_order"] == 1920

    # Point-set closure reconstruction.
    moduli = (9, 3, 2)
    points = list(product(range(9), range(3), range(2)))
    point_index = {p: i for i, p in enumerate(points)}

    def add(a, b):
        return tuple((x + y) % m for x, y, m in zip(a, b, moduli))

    def mult(k, a):
        return tuple(k * x % m for x, m in zip(a, moduli))

    def cyclic(a):
        for k in range(1, 55):
            if mult(k, a) == (0, 0, 0):
                return frozenset(mult(j, a) for j in range(k))
        raise AssertionError(a)

    subgroups = [sum(1 << point_index[tuple(p)] for p in row["subgroup_points"])
                 for row in c75["closure_incidence"]["all_subgroups"]]
    index = {mask: i for i, mask in enumerate(subgroups)}
    coords = [tuple(p) for p in c75["named_coordinate_source"]["coordinates"]]
    cyclic_masks = [sum(1 << point_index[p] for p in cyclic(p)) for p in coords]

    def extend(left, right):
        result = 0
        for i, a in enumerate(points):
            if left & (1 << i):
                for j, b in enumerate(points):
                    if right & (1 << j):
                        result |= 1 << point_index[add(a, b)]
        return result

    transition = [[index[extend(H, C)] for C in cyclic_masks] for H in subgroups]
    zero = index[1 << point_index[(0, 0, 0)]]
    closure = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        closure[mask] = transition[closure[mask ^ low]][low.bit_length() - 1]

    orders = [row["subgroup_order"] for row in c75["closure_incidence"]["all_subgroups"]]
    distinct_orders = sorted(set(orders))
    rows80 = c80["target_atlas"]["profile_rows"]
    blocks = [[int(label[1:]) - 1 for label in block]
              for block in c79["definition"]["direction_blocks"]]
    block_masks = [sum(1 << i for i in block) for block in blocks]
    pivot = int(c79["definition"]["pivot"][1:]) - 1

    def repair(deleted):
        full_sizes = [len(block) for block, mask in zip(blocks, block_masks)
                      if (deleted & mask) == mask]
        rho = int(bool(deleted & (1 << pivot))) + max(0, len(full_sizes) - 2)
        if len(full_sizes) <= 2:
            witness = 1
        elif len(full_sizes) == 3:
            witness = sum(full_sizes)
        else:
            witness = sum(a * b for i, a in enumerate(full_sizes)
                          for b in full_sizes[i + 1:])
        return rho, witness

    def make_profile(retained):
        rho, witness = repair(ALL ^ retained)
        thresholds = rows80[retained]["thresholds"]
        histogram = []
        for order in distinct_orders:
            count = Counter(thresholds[i] for i, value in enumerate(orders) if value == order)
            histogram.append({"order": order, "counts": [count[k] for k in range(4)]})
        return {"rho": rho, "witness_multiplicity": witness,
                "closure_order": orders[closure[retained]],
                "threshold_order_histogram": histogram}

    profiles = [make_profile(mask) for mask in range(1 << 16)]
    quotient = evidence["orbit_quotient"]
    rows = quotient["rows"]
    assert len(rows) == 3024
    assert quotient["orbit_count"] == 3024
    assert quotient["profile_class_count"] == 14
    expected_rows = []
    unseen = set(range(1 << 16))
    while unseen:
        rep = min(unseen)
        orbit = {apply_mask(rep, p) for p in group}
        unseen -= orbit
        expected_rows.append((rep, len(orbit), profiles[rep]))
        assert all(profiles[m] == profiles[rep] for m in orbit)
    expected_rows.sort()
    actual_rows = sorted((row["representative_mask"], row["orbit_size"], row["profile"]) for row in rows)
    assert actual_rows == expected_rows
    assert all(row["stabilizer_order"] * row["orbit_size"] == 1920 for row in rows)
    assert sum(row["orbit_size"] for row in rows) == 65536
    assert quotient["orbit_size_spectrum"] == {
        "1": 128, "2": 256, "4": 416, "5": 128, "8": 192,
        "10": 384, "16": 16, "20": 672, "40": 608, "80": 208, "160": 16,
    }
    assert quotient["orbit_count_by_cardinality"] == [
        1, 7, 27, 73, 151, 252, 352, 424, 450,
        424, 352, 252, 151, 73, 27, 7, 1,
    ]
    fixed = Counter(1 << cycles(p) for p in group)
    assert quotient["fixed_support_count_spectrum"] == {str(k): v for k, v in sorted(fixed.items())}
    assert sum(k * v for k, v in fixed.items()) == 1920 * 3024

    mask_counts = Counter()
    for row in rows:
        profile = row["profile"]
        mask_counts[(profile["rho"], profile["witness_multiplicity"])] += row["orbit_size"]
    expected_marginal = {
        "0,1": 30400, "1,1": 30400, "1,4": 1984, "1,7": 192,
        "1,8": 128, "2,4": 1984, "2,7": 192, "2,8": 128,
        "2,25": 64, "3,25": 64,
    }
    assert {f"{r},{w}": mask_counts[(r, w)] for r, w in sorted(mask_counts)} == expected_marginal
    assert evidence["repair_profile_marginals"]["mask_count_by_rho_witness"] == expected_marginal
    assert evidence["claims"] == {
        "effective_1920_label_orbit_quotient": True,
        "repair_profile_invariance_verified": True,
        "all_65536_masks_partitioned": True,
        "burnside_orbit_count_identity": True,
        "full_burnside_ring_claimed": False,
        "full_table_of_marks_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({"status": "C81_INDEPENDENT_CHECK_PASS", "group_order": 1920,
                      "orbit_count": len(rows), "profile_class_count": quotient["profile_class_count"],
                      "burnside_identity": True}, sort_keys=True))


if __name__ == "__main__":
    main()
