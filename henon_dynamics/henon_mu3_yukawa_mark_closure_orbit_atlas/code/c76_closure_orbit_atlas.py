#!/usr/bin/env python3
"""Produce the C76 finite support orbit atlas.

C75 supplies a 11520-element lifted ambient group whose label action has a
6-element ambient C6 kernel.  C76 works with the effective 16-label image
E = S5 x C2 x D8 of order 1920.  Every support is a 16-bit label subset.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
OUT = PROJECT / "results/c76_closure_orbit_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
LABELS = tuple(f"S{i}" for i in range(1, 17))
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
}

Point = tuple[int, int, int]
Permutation = tuple[int, ...]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left: Point, right: Point) -> Point:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))  # type: ignore[return-value]


def multiple(coefficient: int, value: Point) -> Point:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))  # type: ignore[return-value]


def element_order(value: Point) -> int:
    for order in range(1, 55):
        if multiple(order, value) == (0, 0, 0):
            return order
    raise AssertionError("finite-group order search failed")


def cyclic_subgroup(value: Point) -> frozenset[Point]:
    return frozenset(multiple(coefficient, value) for coefficient in range(element_order(value)))


def subgroup_key(subgroup: frozenset[Point]) -> tuple[int, tuple[Point, ...]]:
    return len(subgroup), tuple(sorted(subgroup))


def point_bitset(subgroup: frozenset[Point], point_index: dict[Point, int]) -> int:
    result = 0
    for point in subgroup:
        result |= 1 << point_index[point]
    return result


def extend_bitsets(left: int, right: int, points: list[Point], point_index: dict[Point, int]) -> int:
    result = 0
    left_indices = [index for index in range(54) if left & (1 << index)]
    right_indices = [index for index in range(54) if right & (1 << index)]
    for left_index in left_indices:
        for right_index in right_indices:
            result |= 1 << point_index[add(points[left_index], points[right_index])]
    return result


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(16))


def permutation_cycles(permutation: Permutation) -> list[list[str]]:
    seen: set[int] = set()
    result: list[list[str]] = []
    for source in range(16):
        if source in seen or permutation[source] == source:
            continue
        cycle: list[str] = []
        current = source
        while current not in seen:
            seen.add(current)
            cycle.append(LABELS[current])
            current = permutation[current]
        result.append(cycle)
    return result


def permutation_order(permutation: Permutation) -> int:
    power = tuple(range(16))
    for order in range(1, 1001):
        power = compose(permutation, power)
        if power == tuple(range(16)):
            return order
    raise AssertionError("permutation order search failed")


def apply_mask(mask: int, permutation: Permutation) -> int:
    result = 0
    while mask:
        low = mask & -mask
        source = low.bit_length() - 1
        result |= 1 << permutation[source]
        mask ^= low
    return result


def generate_group(generators: list[Permutation]) -> list[Permutation]:
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


def labels_for_mask(mask: int) -> list[str]:
    return [LABELS[index] for index in range(16) if mask & (1 << index)]


def main() -> None:
    paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c75 = json.loads(raw["c75"])
    assert c75["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == FIREWALL
    assert c75["lifted_symmetry"]["lifted_group_order"] == 11520
    assert c75["nonfaithful_lattice_diagnostic"]["twenty_subgroup_lattice_action_kernel_order"] == 6

    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    assert len(coordinates) == 16
    generator_rows = {row["name"]: row for row in c75["lifted_symmetry"]["generators"]}
    generator_names = (
        "zero_5_cycle",
        "zero_transposition",
        "fiber_F3_transposition",
        "fiber_F9_transposition",
        "ambient_s",
    )
    generators = [tuple(generator_rows[name]["label_permutation"]) for name in generator_names]
    assert all(len(permutation) == 16 for permutation in generators)
    group = generate_group(generators)
    assert len(group) == 1920
    assert Counter(permutation_order(permutation) for permutation in group) == Counter({
        1: 1, 2: 311, 3: 20, 4: 584, 5: 24, 6: 460,
        10: 264, 12: 160, 20: 96,
    })

    points = list(product(range(9), range(3), range(2)))
    point_index = {point: index for index, point in enumerate(points)}
    subgroup_rows = c75["closure_incidence"]["all_subgroups"]
    subgroup_bitsets = [
        point_bitset(frozenset(tuple(point) for point in row["subgroup_points"]), point_index)
        for row in subgroup_rows
    ]
    subgroup_index = {bitset: index for index, bitset in enumerate(subgroup_bitsets)}
    cyclic_bitsets = [point_bitset(cyclic_subgroup(point), point_index) for point in coordinates]
    extension_table = [
        [subgroup_index[extend_bitsets(subgroup, cyclic, points, point_index)] for cyclic in cyclic_bitsets]
        for subgroup in subgroup_bitsets
    ]
    zero_index = subgroup_index[point_bitset(frozenset({(0, 0, 0)}), point_index)]
    closure_index = [zero_index] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        label_index = low.bit_length() - 1
        closure_index[mask] = extension_table[closure_index[mask ^ low]][label_index]
    assert closure_index[-1] == subgroup_index[subgroup_bitsets[-1]]

    closure_minimal = []
    full_core_minimal = []
    full_core_index = subgroup_index[subgroup_bitsets[-1]]
    for mask in range(1 << 16):
        is_minimal = mask == 0 or all(
            closure_index[mask ^ (1 << label_index)] != closure_index[mask]
            for label_index in range(16) if mask & (1 << label_index)
        )
        if is_minimal:
            closure_minimal.append(mask)
        if mask and closure_index[mask] == full_core_index and all(
            closure_index[mask ^ (1 << label_index)] != closure_index[mask]
            for label_index in range(16) if mask & (1 << label_index)
        ):
            full_core_minimal.append(mask)
    assert len(closure_minimal) == 98
    assert len(full_core_minimal) == 25

    unseen = set(range(1 << 16))
    orbit_rows: list[dict[str, Any]] = []
    orbit_size_spectrum: Counter[int] = Counter()
    orbit_count_by_cardinality: Counter[int] = Counter()
    orbit_count_by_closure: Counter[int] = Counter()
    while unseen:
        representative = min(unseen)
        orbit = {apply_mask(representative, permutation) for permutation in group}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        closure = closure_index[representative]
        support_size = representative.bit_count()
        orbit_size = len(orbit)
        orbit_size_spectrum[orbit_size] += 1
        orbit_count_by_cardinality[support_size] += 1
        orbit_count_by_closure[closure] += 1
        orbit_rows.append({
            "representative_mask": representative,
            "representative_labels": labels_for_mask(representative),
            "support_size": support_size,
            "orbit_size": orbit_size,
            "closure_subgroup_index": closure,
            "closure_order": len(subgroup_bitsets[closure].to_bytes((54 + 7) // 8, "little").rstrip(b"\x00")) if False else subgroup_rows[closure]["subgroup_order"],
            "closure_minimal": representative in closure_minimal,
            "full_core_minimal": representative in full_core_minimal,
        })
    orbit_rows.sort(key=lambda row: row["representative_mask"])
    assert len(orbit_rows) == 3024
    assert sum(row["orbit_size"] for row in orbit_rows) == 65536
    assert dict(sorted(orbit_size_spectrum.items())) == {
        1: 128, 2: 256, 4: 416, 5: 128, 8: 192, 10: 384,
        16: 16, 20: 672, 40: 608, 80: 208, 160: 16,
    }
    assert [orbit_count_by_cardinality[index] for index in range(17)] == [
        1, 7, 27, 73, 151, 252, 352, 424, 450,
        424, 352, 252, 151, 73, 27, 7, 1,
    ]

    def atlas_subset(supports: list[int]) -> tuple[Counter[int], list[dict[str, Any]]]:
        unseen_subset = set(supports)
        spectrum: Counter[int] = Counter()
        rows_subset: list[dict[str, Any]] = []
        while unseen_subset:
            representative = min(unseen_subset)
            orbit = {apply_mask(representative, permutation) for permutation in group}
            orbit.intersection_update(unseen_subset)
            assert orbit == {apply_mask(representative, permutation) for permutation in group}
            unseen_subset.difference_update(orbit)
            spectrum[len(orbit)] += 1
            rows_subset.append({
                "representative_mask": representative,
                "support_size": representative.bit_count(),
                "orbit_size": len(orbit),
                "closure_subgroup_index": closure_index[representative],
            })
        rows_subset.sort(key=lambda row: row["representative_mask"])
        return spectrum, rows_subset

    minimal_spectrum, minimal_orbits = atlas_subset(closure_minimal)
    full_spectrum, full_orbits = atlas_subset(full_core_minimal)
    assert dict(sorted(minimal_spectrum.items())) == {1: 10, 2: 8, 4: 14, 8: 2}
    assert dict(sorted(full_spectrum.items())) == {1: 1, 2: 2, 4: 3, 8: 1}
    assert len(minimal_orbits) == 34
    assert len(full_orbits) == 7
    assert all(row["support_size"] == 3 for row in full_orbits)

    minimal_size_counts = Counter(mask.bit_count() for mask in closure_minimal)
    assert dict(sorted(minimal_size_counts.items())) == {0: 1, 1: 11, 2: 48, 3: 38}
    subgroup_support_counts = Counter(closure_index[mask] for mask in range(1 << 16))
    subgroup_orbit_counts = Counter(row["closure_subgroup_index"] for row in orbit_rows)
    result: dict[str, Any] = {
        "schema_id": "hcs-c76-finite-support-closure-orbit-atlas-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "source_model": {
            "ambient_group": "Z/9 + Z/3 + Z/2",
            "label_count": 16,
            "support_count": 1 << 16,
            "c75_lifted_group_order": 11520,
            "c75_ambient_c6_kernel_order": 6,
            "effective_label_group_order": len(group),
            "effective_label_group_candidate": "S5 x C2 x D8",
            "effective_generator_names": list(generator_names),
            "effective_generator_cycles": {
                name: permutation_cycles(permutation)
                for name, permutation in zip(generator_names, generators)
            },
            "effective_generator_orders": {
                name: permutation_order(permutation)
                for name, permutation in zip(generator_names, generators)
            },
            "effective_group_element_order_distribution": {
                str(order): count
                for order, count in sorted(Counter(permutation_order(permutation) for permutation in group).items())
            },
        },
        "closure_atlas": {
            "subgroup_count": len(subgroup_rows),
            "closure_index_order": [row["subgroup_order"] for row in subgroup_rows],
            "support_count_by_closure_index": {
                str(index): subgroup_support_counts[index]
                for index in range(len(subgroup_rows))
            },
            "orbit_count_by_closure_index": {
                str(index): subgroup_orbit_counts[index]
                for index in range(len(subgroup_rows))
            },
        },
        "support_orbit_atlas": {
            "support_count": 1 << 16,
            "orbit_count": len(orbit_rows),
            "orbit_size_spectrum": {str(size): count for size, count in sorted(orbit_size_spectrum.items())},
            "orbit_count_by_cardinality": [orbit_count_by_cardinality[index] for index in range(17)],
            "rows": orbit_rows,
        },
        "closure_minimality": {
            "definition": "mask is minimal iff empty or every single-label deletion strictly changes its generated subgroup",
            "including_empty_support": True,
            "support_count": len(closure_minimal),
            "support_count_by_cardinality": {str(size): minimal_size_counts[size] for size in sorted(minimal_size_counts)},
            "orbit_count": len(minimal_orbits),
            "orbit_size_spectrum": {str(size): count for size, count in sorted(minimal_spectrum.items())},
            "orbit_rows": minimal_orbits,
        },
        "full_core_minimality": {
            "definition": "single-deletion minimal supports whose closure is the full 54-point core",
            "support_count": len(full_core_minimal),
            "all_supports_have_cardinality": 3,
            "orbit_count": len(full_orbits),
            "orbit_size_spectrum": {str(size): count for size, count in sorted(full_spectrum.items())},
            "orbit_rows": full_orbits,
            "representative_masks": [row["representative_mask"] for row in full_orbits],
        },
        "claims": {
            "finite_support_orbit_atlas": True,
            "effective_group_used_not_ambient_lift": True,
            "ambient_c6_kernel_recorded": True,
            "all_65536_supports_partitioned": True,
            "exact_closure_minimality_enumerated": True,
            "full_core_minimality_enumerated": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "effective_group_order": len(group),
        "support_count": 1 << 16,
        "orbit_count": len(orbit_rows),
        "closure_minimal_support_count": len(closure_minimal),
        "closure_minimal_orbit_count": len(minimal_orbits),
        "full_core_minimal_support_count": len(full_core_minimal),
        "full_core_minimal_orbit_count": len(full_orbits),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
