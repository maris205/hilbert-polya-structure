#!/usr/bin/env python3
"""Produce the C81 effective-1920 orbit quotient of repair profiles.

The C75 ambient lift has order 11520, but its label action has a six-element
kernel.  C81 uses the effective 1920-element label permutation group from C76
and quotients the C79/C80 finite repair observables by that action.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
C79 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity"
C80 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas"
OUT = PROJECT / "results/c81_effective_orbit_repair_profile_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
ALL = (1 << 16) - 1
LABELS = tuple(f"S{i}" for i in range(1, 17))

EXPECTED = {
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
    "c79": "147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879",
    "c79_manifest": "982cce509de371d59c4b87cda75af057d994c6fc36146daddc3b983c9c63246c",
    "c80": "8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5",
    "c80_manifest": "a674116ab6f8f9478130219cc525478525f10f2e42f515e71418a3066e2b229c",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(16))


def generate_group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
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


def apply_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    while mask:
        low = mask & -mask
        result |= 1 << permutation[low.bit_length() - 1]
        mask ^= low
    return result


def permutation_order(permutation: tuple[int, ...]) -> int:
    identity = tuple(range(16))
    power = identity
    for order in range(1, 1001):
        power = compose(permutation, power)
        if power == identity:
            return order
    raise AssertionError("permutation order overflow")


def cycle_count(permutation: tuple[int, ...]) -> int:
    seen: set[int] = set()
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


def labels_for_mask(mask: int) -> list[str]:
    return [LABELS[i] for i in range(16) if mask & (1 << i)]


def profile_key(profile: dict[str, Any]) -> str:
    return json.dumps(profile, sort_keys=True, separators=(",", ":"))


def main() -> None:
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
    raw = {name: (path.read_bytes() if path.exists() else b"") for name, path in paths.items()}
    observed = {name: digest(value) for name, value in raw.items()}
    for name, expected in EXPECTED.items():
        if not expected.startswith("PENDING"):
            assert observed[name] == expected, (name, observed[name], expected)
    source = {name: json.loads(raw[name]) for name in ("c76", "c78", "c79", "c80")}
    assert all(doc["status"] == "PREFREEZE_G3_PASS" for doc in source.values())
    assert all(doc["scope_literal"] == FIREWALL for doc in source.values())
    assert source["c76"]["source_model"]["effective_label_group_order"] == 1920
    assert source["c76"]["source_model"]["c75_lifted_group_order"] == 11520
    assert source["c76"]["source_model"]["c75_ambient_c6_kernel_order"] == 6
    assert source["c79"]["witness_multiplicity_atlas"]["support_count"] == 65536
    assert len(source["c80"]["target_atlas"]["profile_rows"]) == 65536

    c75 = json.loads((C75 / "results/c75_closure_incidence_lift_evidence.json").read_text())
    generator_rows = {row["name"]: row for row in c75["lifted_symmetry"]["generators"]}
    generator_names = ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition",
                       "fiber_F9_transposition", "ambient_s")
    generators = [tuple(generator_rows[name]["label_permutation"]) for name in generator_names]
    group = generate_group(generators)
    assert len(group) == 1920
    assert digest((C75 / "results/c75_closure_incidence_lift_evidence.json").read_bytes()) == \
        "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98"

    # Rebuild closure indices to attach a presentation-independent subgroup
    # order to each retained support.
    from itertools import product
    MODULI = (9, 3, 2)
    points = list(product(range(9), range(3), range(2)))
    point_index = {point: i for i, point in enumerate(points)}

    def add(left, right):
        return tuple((x + y) % m for x, y, m in zip(left, right, MODULI))

    def multiple(k, value):
        return tuple(k * x % m for x, m in zip(value, MODULI))

    def cyclic(value):
        for order in range(1, 55):
            if multiple(order, value) == (0, 0, 0):
                return frozenset(multiple(k, value) for k in range(order))
        raise AssertionError(value)

    rows = c75["closure_incidence"]["all_subgroups"]
    subgroup_masks = [sum(1 << point_index[tuple(point)] for point in row["subgroup_points"])
                      for row in rows]
    subgroup_index = {mask: index for index, mask in enumerate(subgroup_masks)}
    cyclic_masks = [sum(1 << point_index[p] for p in cyclic(tuple(point)))
                    for point in c75["named_coordinate_source"]["coordinates"]]

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
    closure = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        closure[mask] = transition[closure[mask ^ low]][low.bit_length() - 1]

    # The invariant repair profile consists of rho, W, generated subgroup
    # order, and threshold counts grouped by target subgroup order.  Group
    # elements may permute rows inside an order class, so the histogram rather
    # than the raw row vector is the canonical quotient datum.
    target_orders = [row["subgroup_order"] for row in rows]
    distinct_orders = sorted(set(target_orders))
    c80_profiles = source["c80"]["target_atlas"]["profile_rows"]
    blocks = [[int(label[1:]) - 1 for label in block]
              for block in source["c79"]["definition"]["direction_blocks"]]
    block_masks = [sum(1 << i for i in block) for block in blocks]
    pivot = int(source["c79"]["definition"]["pivot"][1:]) - 1

    def repair_values(deleted: int) -> tuple[int, int]:
        flags = [(deleted & block) == block for block in block_masks]
        full_sizes = [len(block) for block, flag in zip(blocks, flags) if flag]
        rho = int(bool(deleted & (1 << pivot))) + max(0, len(full_sizes) - 2)
        if len(full_sizes) <= 2:
            witness = 1
        elif len(full_sizes) == 3:
            witness = sum(full_sizes)
        else:
            witness = sum(a * b for i, a in enumerate(full_sizes)
                          for b in full_sizes[i + 1:])
        return rho, witness

    profiles: list[dict[str, Any]] = []
    for retained in range(1 << 16):
        deleted = ALL ^ retained
        rho, witness = repair_values(deleted)
        thresholds = c80_profiles[retained]["thresholds"]
        histogram = []
        for order in distinct_orders:
            counts = Counter(thresholds[i] for i, target_order in enumerate(target_orders)
                             if target_order == order)
            histogram.append({"order": order,
                              "counts": [counts[t] for t in range(4)]})
        profiles.append({
            "rho": rho,
            "witness_multiplicity": witness,
            "closure_order": target_orders[closure[retained]],
            "threshold_order_histogram": histogram,
        })

    # Partition the 65536 masks into effective-group orbits.
    unseen = set(range(1 << 16))
    orbit_rows: list[dict[str, Any]] = []
    profile_classes: dict[str, dict[str, Any]] = {}
    orbit_size_spectrum: Counter[int] = Counter()
    orbit_count_by_cardinality: Counter[int] = Counter()
    orbit_count_by_rho_witness: Counter[tuple[int, int]] = Counter()
    mask_count_by_rho_witness: Counter[tuple[int, int]] = Counter()
    while unseen:
        representative = min(unseen)
        orbit = {apply_mask(representative, permutation) for permutation in group}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        profile = profiles[representative]
        for member in orbit:
            assert profiles[member] == profile
        key = profile_key(profile)
        orbit_id = len(orbit_rows)
        orbit_size = len(orbit)
        orbit_size_spectrum[orbit_size] += 1
        orbit_count_by_cardinality[representative.bit_count()] += 1
        orbit_count_by_rho_witness[(profile["rho"], profile["witness_multiplicity"])] += 1
        mask_count_by_rho_witness[(profile["rho"], profile["witness_multiplicity"])] += orbit_size
        row = {
            "orbit_id": orbit_id,
            "representative_mask": representative,
            "representative_labels": labels_for_mask(representative),
            "support_size": representative.bit_count(),
            "orbit_size": orbit_size,
            "stabilizer_order": 1920 // orbit_size,
            "profile_key": key,
            "profile": profile,
        }
        orbit_rows.append(row)
        if key not in profile_classes:
            profile_classes[key] = {
                "profile_id": len(profile_classes),
                "profile_key": key,
                "profile": profile,
                "orbit_ids": [],
                "representative_masks": [],
                "orbit_count": 0,
                "mask_count": 0,
                "orbit_size_spectrum": Counter(),
            }
        cls = profile_classes[key]
        cls["orbit_ids"].append(orbit_id)
        cls["representative_masks"].append(representative)
        cls["orbit_count"] += 1
        cls["mask_count"] += orbit_size
        cls["orbit_size_spectrum"][orbit_size] += 1

    orbit_rows.sort(key=lambda row: row["representative_mask"])
    # Reassign IDs after sorting, and rebuild class references deterministically.
    id_by_rep = {row["representative_mask"]: i for i, row in enumerate(orbit_rows)}
    for row in orbit_rows:
        row["orbit_id"] = id_by_rep[row["representative_mask"]]
    class_rows = []
    for cls in sorted(profile_classes.values(), key=lambda row: row["profile_key"]):
        cls = dict(cls)
        cls["profile_id"] = len(class_rows)
        cls["orbit_ids"] = sorted(id_by_rep[m] for m in cls["representative_masks"])
        cls["representative_masks"] = sorted(cls["representative_masks"])
        cls["orbit_size_spectrum"] = {str(k): v for k, v in sorted(cls["orbit_size_spectrum"].items())}
        class_rows.append(cls)
    class_id = {row["profile_key"]: row["profile_id"] for row in class_rows}
    for row in orbit_rows:
        row["profile_id"] = class_id[row["profile_key"]]

    fixed_spectrum = Counter(1 << cycle_count(permutation) for permutation in group)
    assert len(orbit_rows) == 3024
    assert sum(row["orbit_size"] for row in orbit_rows) == 65536
    assert sum(fixed_spectrum.values()) == 1920
    assert sum(fixed * count for fixed, count in fixed_spectrum.items()) // 1920 == 3024
    assert dict(sorted(orbit_size_spectrum.items())) == {
        1: 128, 2: 256, 4: 416, 5: 128, 8: 192, 10: 384,
        16: 16, 20: 672, 40: 608, 80: 208, 160: 16,
    }
    assert [orbit_count_by_cardinality[k] for k in range(17)] == [
        1, 7, 27, 73, 151, 252, 352, 424, 450,
        424, 352, 252, 151, 73, 27, 7, 1,
    ]
    assert dict(mask_count_by_rho_witness) == {
        (0, 1): 30400, (1, 1): 30400, (1, 4): 1984,
        (1, 7): 192, (1, 8): 128, (2, 4): 1984,
        (2, 7): 192, (2, 8): 128, (2, 25): 64, (3, 25): 64,
    }

    # JSON cannot serialize Counter values; normalize class rows.
    result_classes = []
    for row in class_rows:
        row = dict(row)
        row["orbit_size_spectrum"] = dict(row["orbit_size_spectrum"])
        result_classes.append(row)
    result: dict[str, Any] = {
        "schema_id": "hcs-c81-effective-1920-repair-profile-orbit-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": EXPECTED,
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": 16,
            "support_count": 65536,
            "c75_ambient_lift_order": 11520,
            "c75_lift_kernel_order": 6,
            "effective_label_group_order": 1920,
            "effective_group_candidate": "S5 x C2 x D8",
            "generator_names": list(generator_names),
            "element_order_distribution": {
                str(order): count for order, count in sorted(
                    Counter(permutation_order(p) for p in group).items())
            },
        },
        "profile_definition": {
            "profile": "(rho(D), W(D), |Phi(L\\D)|, threshold histograms by target subgroup order)",
            "threshold_histogram_orders": distinct_orders,
            "threshold_bins": [0, 1, 2, 3],
            "invariant_reason": "effective label automorphisms preserve closure order and permute targets within each subgroup-order class",
        },
        "orbit_quotient": {
            "orbit_count": len(orbit_rows),
            "orbit_size_spectrum": {str(k): v for k, v in sorted(orbit_size_spectrum.items())},
            "orbit_count_by_cardinality": [orbit_count_by_cardinality[k] for k in range(17)],
            "rows": orbit_rows,
            "profile_class_count": len(result_classes),
            "profile_classes": result_classes,
            "fixed_support_count_spectrum": {str(k): v for k, v in sorted(fixed_spectrum.items())},
            "burnside_orbit_identity": "sum_g 2^(number of label cycles of g) / 1920 = 3024",
        },
        "repair_profile_marginals": {
            "orbit_count_by_rho_witness": {
                f"{rho},{witness}": orbit_count_by_rho_witness[(rho, witness)]
                for rho, witness in sorted(orbit_count_by_rho_witness)
            },
            "mask_count_by_rho_witness": {
                f"{rho},{witness}": mask_count_by_rho_witness[(rho, witness)]
                for rho, witness in sorted(mask_count_by_rho_witness)
            },
        },
        "claims": {
            "effective_1920_label_orbit_quotient": True,
            "repair_profile_invariance_verified": True,
            "all_65536_masks_partitioned": True,
            "burnside_orbit_count_identity": True,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"], "effective_group_order": 1920,
        "orbit_count": len(orbit_rows), "profile_class_count": len(result_classes),
        "support_count": 65536, "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
