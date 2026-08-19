#!/usr/bin/env python3
"""Independent checker for the C76 support orbit atlas."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
HASHES = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
}
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
LABELS = tuple(f"S{index}" for index in range(1, 17))


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def compose(left, right):
    return tuple(left[right[index]] for index in range(16))


def apply_mask(mask, permutation):
    result = 0
    while mask:
        low = mask & -mask
        result |= 1 << permutation[low.bit_length() - 1]
        mask ^= low
    return result


def order(permutation):
    identity = tuple(range(16))
    power = identity
    for candidate in range(1, 1001):
        power = compose(permutation, power)
        if power == identity:
            return candidate
    raise AssertionError


def permutation_cycles(permutation):
    seen = set()
    cycles = []
    for source in range(16):
        if source in seen or permutation[source] == source:
            continue
        cycle = []
        current = source
        while current not in seen:
            seen.add(current)
            cycle.append(LABELS[current])
            current = permutation[current]
        cycles.append(cycle)
    return cycles


def labels_for_mask(mask):
    return [LABELS[index] for index in range(16) if mask & (1 << index)]


def generate(generators):
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
    return frozenset(multiple(candidate, value) for candidate in range(point_order(value)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=PROJECT / "results/c76_closure_orbit_atlas_evidence.json")
    args = parser.parse_args()
    evidence_raw = args.evidence.read_bytes()
    evidence = json.loads(evidence_raw)
    assert evidence_raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c76-finite-support-closure-orbit-atlas-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    sources = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in sources.items()} == HASHES
    assert evidence["authority"] == HASHES
    c75 = json.loads(sources["c75"].read_text())
    assert c75["lifted_symmetry"]["lifted_group_order"] == 11520
    assert c75["nonfaithful_lattice_diagnostic"]["twenty_subgroup_lattice_action_kernel_order"] == 6

    generator_rows = {row["name"]: row for row in c75["lifted_symmetry"]["generators"]}
    names = ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition", "fiber_F9_transposition", "ambient_s")
    generators = [tuple(generator_rows[name]["label_permutation"]) for name in names]
    group = generate(generators)
    assert len(group) == 1920
    assert {str(key): value for key, value in sorted(Counter(order(g) for g in group).items())} == {
        "1": 1, "2": 311, "3": 20, "4": 584, "5": 24, "6": 460,
        "10": 264, "12": 160, "20": 96,
    }
    source_model = evidence["source_model"]
    assert source_model == {
        "ambient_group": "Z/9 + Z/3 + Z/2",
        "label_count": 16,
        "support_count": 1 << 16,
        "c75_lifted_group_order": 11520,
        "c75_ambient_c6_kernel_order": 6,
        "effective_label_group_order": 1920,
        "effective_label_group_candidate": "S5 x C2 x D8",
        "effective_generator_names": list(names),
        "effective_generator_cycles": {
            name: permutation_cycles(permutation)
            for name, permutation in zip(names, generators)
        },
        "effective_generator_orders": {
            name: order(permutation)
            for name, permutation in zip(names, generators)
        },
        "effective_group_element_order_distribution": {
            str(key): value
            for key, value in sorted(Counter(order(permutation) for permutation in group).items())
        },
    }
    # Reject headline/statistical metadata mutations before the exhaustive
    # 54-point closure scan.  The same fields are checked again against the
    # independently reconstructed tables below.
    assert evidence["support_orbit_atlas"]["support_count"] == 1 << 16
    assert evidence["support_orbit_atlas"]["orbit_count"] == 3024
    assert evidence["support_orbit_atlas"]["orbit_size_spectrum"] == {
        "1": 128, "2": 256, "4": 416, "5": 128, "8": 192,
        "10": 384, "16": 16, "20": 672, "40": 608, "80": 208, "160": 16,
    }
    assert evidence["support_orbit_atlas"]["orbit_count_by_cardinality"] == [
        1, 7, 27, 73, 151, 252, 352, 424, 450,
        424, 352, 252, 151, 73, 27, 7, 1,
    ]
    assert evidence["closure_minimality"]["support_count"] == 98
    assert evidence["full_core_minimality"]["support_count"] == 25

    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    points = list(product(range(9), range(3), range(2)))
    point_index = {point: index for index, point in enumerate(points)}
    subgroup_rows = c75["closure_incidence"]["all_subgroups"]
    subgroups = [
        frozenset(tuple(point) for point in row["subgroup_points"])
        for row in subgroup_rows
    ]
    subgroup_index = {frozenset(subgroup): index for index, subgroup in enumerate(subgroups)}
    cyclic_bitsets = []
    for coordinate in coordinates:
        bitset = 0
        for point in cyclic(coordinate):
            bitset |= 1 << point_index[point]
        cyclic_bitsets.append(bitset)
    subgroup_bits = []
    for subgroup in subgroups:
        bits = 0
        for point in subgroup:
            bits |= 1 << point_index[point]
        subgroup_bits.append(bits)
    subgroup_bit_index = {bits: index for index, bits in enumerate(subgroup_bits)}
    extension = [[None] * 16 for _ in subgroups]
    for subgroup_index_value, left in enumerate(subgroup_bits):
        left_points = [points[index] for index in range(54) if left & (1 << index)]
        for label_index, right in enumerate(cyclic_bitsets):
            right_points = [points[index] for index in range(54) if right & (1 << index)]
            generated = set()
            for left_point in left_points:
                for right_point in right_points:
                    generated.add(add(left_point, right_point))
            bits = 0
            for point in generated:
                bits |= 1 << point_index[point]
            extension[subgroup_index_value][label_index] = subgroup_bit_index[bits]
    zero = subgroup_bit_index[1 << point_index[(0, 0, 0)]]
    closure_index = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        label_index = low.bit_length() - 1
        closure_index[mask] = extension[closure_index[mask ^ low]][label_index]
    full = subgroup_bit_index[subgroup_bits[-1]]
    closure_minimal = [
        mask for mask in range(1 << 16)
        if mask == 0 or all(
            closure_index[mask ^ (1 << label_index)] != closure_index[mask]
            for label_index in range(16) if mask & (1 << label_index)
        )
    ]
    full_minimal = [
        mask for mask in range(1 << 16)
        if mask and closure_index[mask] == full and all(
            closure_index[mask ^ (1 << label_index)] != closure_index[mask]
            for label_index in range(16) if mask & (1 << label_index)
        )
    ]
    assert len(closure_minimal) == 98
    assert len(full_minimal) == 25
    assert dict(sorted(Counter(mask.bit_count() for mask in closure_minimal).items())) == {0: 1, 1: 11, 2: 48, 3: 38}
    assert all(mask.bit_count() == 3 for mask in full_minimal)
    closure_minimal_set = set(closure_minimal)
    full_minimal_set = set(full_minimal)

    unseen = set(range(1 << 16))
    rows = []
    spectrum = Counter()
    by_cardinality = Counter()
    orbit_by_closure = Counter()
    while unseen:
        representative = min(unseen)
        orbit = {apply_mask(representative, permutation) for permutation in group}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        orbit_size = len(orbit)
        closure = closure_index[representative]
        spectrum[orbit_size] += 1
        by_cardinality[representative.bit_count()] += 1
        orbit_by_closure[closure] += 1
        rows.append({
            "representative_mask": representative,
            "representative_labels": labels_for_mask(representative),
            "support_size": representative.bit_count(),
            "orbit_size": orbit_size,
            "closure_subgroup_index": closure,
            "closure_order": subgroup_rows[closure]["subgroup_order"],
            "closure_minimal": representative in closure_minimal_set,
            "full_core_minimal": representative in full_minimal_set,
        })
    assert len(rows) == 3024
    assert sum(row["orbit_size"] for row in rows) == 65536
    assert dict(sorted(spectrum.items())) == {
        1: 128, 2: 256, 4: 416, 5: 128, 8: 192,
        10: 384, 16: 16, 20: 672, 40: 608, 80: 208, 160: 16,
    }
    assert [by_cardinality[index] for index in range(17)] == [1, 7, 27, 73, 151, 252, 352, 424, 450, 424, 352, 252, 151, 73, 27, 7, 1]

    support_count_by_closure = Counter(closure_index)
    assert evidence["closure_atlas"] == {
        "subgroup_count": 20,
        "closure_index_order": [row["subgroup_order"] for row in subgroup_rows],
        "support_count_by_closure_index": {
            str(index): support_count_by_closure[index]
            for index in range(len(subgroup_rows))
        },
        "orbit_count_by_closure_index": {
            str(index): orbit_by_closure[index]
            for index in range(len(subgroup_rows))
        },
    }

    def restricted_orbits(supports):
        unseen_local = set(supports)
        spectrum_local = Counter()
        reps = []
        while unseen_local:
            representative = min(unseen_local)
            orbit = {apply_mask(representative, permutation) for permutation in group}
            assert orbit <= unseen_local
            unseen_local.difference_update(orbit)
            spectrum_local[len(orbit)] += 1
            reps.append((representative, len(orbit), closure_index[representative]))
        return spectrum_local, sorted(reps)

    minimal_spectrum, minimal_rows = restricted_orbits(closure_minimal)
    full_spectrum, full_rows = restricted_orbits(full_minimal)
    assert len(minimal_rows) == 34
    assert len(full_rows) == 7
    assert dict(sorted(minimal_spectrum.items())) == {1: 10, 2: 8, 4: 14, 8: 2}
    assert dict(sorted(full_spectrum.items())) == {1: 1, 2: 2, 4: 3, 8: 1}

    expected_support_orbit_atlas = {
        "support_count": 1 << 16,
        "orbit_count": 3024,
        "orbit_size_spectrum": {str(k): v for k, v in sorted(spectrum.items())},
        "orbit_count_by_cardinality": [by_cardinality[index] for index in range(17)],
        "rows": sorted(rows, key=lambda row: row["representative_mask"]),
    }
    assert evidence["support_orbit_atlas"] == expected_support_orbit_atlas

    expected_minimal_orbits = [
        {
            "representative_mask": representative,
            "support_size": representative.bit_count(),
            "orbit_size": orbit_size,
            "closure_subgroup_index": closure,
        }
        for representative, orbit_size, closure in minimal_rows
    ]
    assert evidence["closure_minimality"] == {
        "definition": "mask is minimal iff empty or every single-label deletion strictly changes its generated subgroup",
        "including_empty_support": True,
        "support_count": 98,
        "support_count_by_cardinality": {"0": 1, "1": 11, "2": 48, "3": 38},
        "orbit_count": 34,
        "orbit_size_spectrum": {str(k): v for k, v in sorted(minimal_spectrum.items())},
        "orbit_rows": expected_minimal_orbits,
    }

    expected_full_orbits = [
        {
            "representative_mask": representative,
            "support_size": representative.bit_count(),
            "orbit_size": orbit_size,
            "closure_subgroup_index": closure,
        }
        for representative, orbit_size, closure in full_rows
    ]
    assert evidence["full_core_minimality"] == {
        "definition": "single-deletion minimal supports whose closure is the full 54-point core",
        "support_count": 25,
        "all_supports_have_cardinality": 3,
        "orbit_count": 7,
        "orbit_size_spectrum": {str(k): v for k, v in sorted(full_spectrum.items())},
        "orbit_rows": expected_full_orbits,
        "representative_masks": [row["representative_mask"] for row in expected_full_orbits],
    }
    assert evidence["claims"] == {
        "finite_support_orbit_atlas": True,
        "effective_group_used_not_ambient_lift": True,
        "ambient_c6_kernel_recorded": True,
        "all_65536_supports_partitioned": True,
        "exact_closure_minimality_enumerated": True,
        "full_core_minimality_enumerated": True,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "PASS",
        "effective_group_order": 1920,
        "orbit_count": 3024,
        "closure_minimal_support_count": 98,
        "closure_minimal_orbit_count": 34,
        "full_core_minimal_support_count": 25,
        "full_core_minimal_orbit_count": 7,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
