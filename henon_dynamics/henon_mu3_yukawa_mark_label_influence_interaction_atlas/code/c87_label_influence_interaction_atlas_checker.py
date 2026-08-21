#!/usr/bin/env python3
"""Independent block-criterion checker for the C87 atlas."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import factorial
from pathlib import Path
from typing import Any

PROJECT = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = PROJECT / "results/c87_label_influence_interaction_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{index}" for index in range(1, 17))
AUTHORITY = {
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
    "c81": "c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f",
    "c81_manifest": "ff3028fd68817795b08ff24332ef44de4cf520ccba543f053fbd78140ac1b512",
    "c82": "6fc49cad02956f463b1e37d017506f437edce6717414da74770ad94913ccefa1",
    "c82_manifest": "5934de3a933e559e941fc636860db2f9f5ceca181acd9d4915396e9facdc8f8b",
}
SOURCE_PATHS = {
    "c73": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/results/c73_generation_blocker_reliability_evidence.json",
    "c73_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/C73_PREFREEZE_MANIFEST.json",
    "c76": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas/results/c76_closure_orbit_atlas_evidence.json",
    "c76_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas/C76_PREFREEZE_MANIFEST.json",
    "c78": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/results/c78_repair_distance_geometry_evidence.json",
    "c78_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/C78_PREFREEZE_MANIFEST.json",
    "c81": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/results/c81_effective_orbit_repair_profile_evidence.json",
    "c81_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/C81_PREFREEZE_MANIFEST.json",
    "c82": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/results/c82_bitflip_noise_fourier_evidence.json",
    "c82_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/C82_PREFREEZE_MANIFEST.json",
}

Pair = tuple[int, int]
Permutation = tuple[int, ...]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def index_of(label: str) -> int:
    return int(label.removeprefix("S")) - 1


def pair_labels(pair: Pair) -> list[str]:
    return [LABELS[pair[0]], LABELS[pair[1]]]


def cycles_to_map(cycles: list[list[str]]) -> Permutation:
    image = list(range(16))
    for labels in cycles:
        entries = [index_of(label) for label in labels]
        for position, source in enumerate(entries):
            image[source] = entries[(position + 1) % len(entries)]
    return tuple(image)


def enumerate_group(generators: list[Permutation]) -> set[Permutation]:
    identity = tuple(range(16))
    group = {identity}
    pending = [identity]
    while pending:
        current = pending.pop()
        for generator in generators:
            candidate = tuple(generator[current[index]] for index in range(16))
            if candidate not in group:
                group.add(candidate)
                pending.append(candidate)
    return group


def orbit_from_generators(seed: tuple[int, ...], generators: list[Permutation]) -> list[tuple[int, ...]]:
    orbit = {seed}
    queue = deque([seed])
    while queue:
        current = queue.popleft()
        for generator in generators:
            image = tuple(sorted(generator[index] for index in current))
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    return sorted(orbit)


def compute_first_rows(truth: list[int]) -> list[dict[str, Any]]:
    result = []
    for index in range(16):
        bit = 1 << index
        counts = [0] * 16
        for base in range(1 << 15):
            lower = base & (bit - 1)
            upper = base ^ lower
            coalition = lower | (upper << 1)
            difference = truth[coalition | bit] - truth[coalition]
            assert difference in (0, 1)
            counts[coalition.bit_count()] += difference
        swings = sum(counts)
        weighted = Fraction(0)
        for size in range(16):
            weighted += Fraction(counts[size] * factorial(size) * factorial(15 - size), factorial(16))
        result.append({
            "label": LABELS[index],
            "coalition_size_swing_counts": counts,
            "swing_count": swings,
            "uniform_banzhaf_influence": fraction_text(Fraction(swings, 32768)),
            "shapley_shubik_value": fraction_text(weighted),
        })
    return result


def compute_pair_rows(truth: list[int]) -> tuple[list[dict[str, Any]], dict[Pair, dict[str, Any]]]:
    result = []
    lookup = {}
    for pair in combinations(range(16), 2):
        first, second = pair
        positive = [0] * 15
        negative = [0] * 15
        first_bit = 1 << first
        second_bit = 1 << second
        both = first_bit | second_bit
        for coalition in range(1 << 16):
            if coalition & both:
                continue
            hessian = truth[coalition | both] + truth[coalition]
            hessian -= truth[coalition | first_bit] + truth[coalition | second_bit]
            assert hessian in (-1, 0, 1)
            if hessian > 0:
                positive[coalition.bit_count()] += 1
            elif hessian < 0:
                negative[coalition.bit_count()] += 1
        signed = [left - right for left, right in zip(positive, negative)]
        positive_total = sum(positive)
        negative_total = sum(negative)
        signed_total = positive_total - negative_total
        shapley = Fraction(0)
        for size, count in enumerate(signed):
            shapley += Fraction(count * factorial(size) * factorial(14 - size), factorial(15))
        row = {
            "pair": pair_labels(pair),
            "positive_delta_by_coalition_size": positive,
            "negative_delta_by_coalition_size": negative,
            "signed_delta_by_coalition_size": signed,
            "positive_delta_count": positive_total,
            "negative_delta_count": negative_total,
            "zero_delta_count": 16384 - positive_total - negative_total,
            "signed_delta_sum": signed_total,
            "uniform_banzhaf_interaction": fraction_text(Fraction(signed_total, 16384)),
            "shapley_pair_interaction": fraction_text(shapley),
        }
        result.append(row)
        lookup[pair] = row
    return result, lookup


def signature(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        tuple(row["positive_delta_by_coalition_size"]),
        tuple(row["negative_delta_by_coalition_size"]),
        tuple(row["signed_delta_by_coalition_size"]),
        row["positive_delta_count"], row["negative_delta_count"],
        row["zero_delta_count"], row["signed_delta_sum"],
        row["uniform_banzhaf_interaction"], row["shapley_pair_interaction"],
    )


def expected_orbits(
    generators: list[Permutation],
    first_rows: list[dict[str, Any]],
    pair_lookup: dict[Pair, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[Pair, str]]:
    label_rows = []
    remaining_labels = {(index,) for index in range(16)}
    while remaining_labels:
        seed = min(remaining_labels)
        orbit = orbit_from_generators(seed, generators)
        remaining_labels.difference_update(orbit)
        representative = seed[0]
        members = [item[0] for item in orbit]
        first_signature = {
            key: first_rows[representative][key]
            for key in (
                "coalition_size_swing_counts", "swing_count",
                "uniform_banzhaf_influence", "shapley_shubik_value",
            )
        }
        assert all(
            all(first_rows[member][key] == value for key, value in first_signature.items())
            for member in members
        )
        label_rows.append({
            "orbit_id": f"L{len(label_rows) + 1:02d}",
            "representative": LABELS[representative],
            "labels": [LABELS[index] for index in members],
            "orbit_size": len(members),
            "first_order_signature": first_signature,
        })

    pair_rows = []
    pair_to_orbit = {}
    remaining_pairs = set(combinations(range(16), 2))
    while remaining_pairs:
        seed = min(remaining_pairs)
        orbit = [tuple(item) for item in orbit_from_generators(seed, generators)]
        remaining_pairs.difference_update(orbit)
        assert all(signature(pair_lookup[pair]) == signature(pair_lookup[seed]) for pair in orbit)
        orbit_id = f"P{len(pair_rows) + 1:02d}"
        for pair in orbit:
            pair_to_orbit[pair] = orbit_id
        source = pair_lookup[seed]
        pair_rows.append({
            "orbit_id": orbit_id,
            "representative_pair": pair_labels(seed),
            "member_pairs": [pair_labels(pair) for pair in orbit],
            "orbit_size": len(orbit),
            "positive_delta_count": source["positive_delta_count"],
            "negative_delta_count": source["negative_delta_count"],
            "uniform_banzhaf_interaction": source["uniform_banzhaf_interaction"],
            "shapley_pair_interaction": source["shapley_pair_interaction"],
        })
    return label_rows, pair_rows, pair_to_orbit


def expected_classes(pair_rows: list[dict[str, Any]], pair_to_orbit: dict[Pair, str]) -> list[dict[str, Any]]:
    buckets: dict[tuple[Any, ...], list[Pair]] = {}
    for row in pair_rows:
        pair = tuple(index_of(label) for label in row["pair"])
        key = (
            row["positive_delta_count"], row["negative_delta_count"],
            row["uniform_banzhaf_interaction"], row["shapley_pair_interaction"],
        )
        buckets.setdefault(key, []).append(pair)
    result = []
    for key, members in buckets.items():
        orbit_ids = {pair_to_orbit[pair] for pair in members}
        result.append({
            "class_id": f"K{len(result) + 1:02d}",
            "representative_pair": pair_labels(members[0]),
            "member_pairs": [pair_labels(pair) for pair in members],
            "pair_count": len(members),
            "pair_orbit_ids": sorted(orbit_ids),
            "pair_orbit_count": len(orbit_ids),
            "positive_delta_count_per_pair": key[0],
            "negative_delta_count_per_pair": key[1],
            "uniform_banzhaf_interaction": key[2],
            "shapley_pair_interaction": key[3],
        })
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw_evidence = args.evidence.read_bytes()
    evidence = json.loads(raw_evidence)
    assert raw_evidence == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c87-label-influence-interaction-atlas-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    assert evidence["authority"] == AUTHORITY

    source_raw = {name: path.read_bytes() for name, path in SOURCE_PATHS.items()}
    assert {name: digest(value) for name, value in source_raw.items()} == AUTHORITY
    sources = {name: json.loads(value) for name, value in source_raw.items()}
    for name in ("c73", "c76", "c78", "c81", "c82"):
        assert sources[name]["status"] == "PREFREEZE_G3_PASS"
        assert sources[name]["scope_literal"] == FIREWALL

    c73 = sources["c73"]
    c76 = sources["c76"]
    c78 = sources["c78"]
    c81 = sources["c81"]
    c82 = sources["c82"]
    block_labels = c78["definition"]["direction_blocks"]
    block_masks = [sum(1 << index_of(label) for label in block) for block in block_labels]
    pivot = index_of(c78["definition"]["pivot"])
    pivot_bit = 1 << pivot

    def predicate(mask: int) -> int:
        return int(bool(mask & pivot_bit) and sum(bool(mask & block) for block in block_masks) >= 2)

    truth = [predicate(mask) for mask in range(65536)]
    assert sum(truth) == 30400
    edge_masks = [sum(1 << index_of(label) for label in edge)
                  for edge in c73["generation_structure"]["minimal_generating_edges"]]
    assert all(truth[mask] == int(any(mask & edge == edge for edge in edge_masks)) for mask in range(65536))
    assert c82["predicate"]["one_count"] == 30400

    source_group = c76["source_model"]
    names = source_group["effective_generator_names"]
    cycles = source_group["effective_generator_cycles"]
    generators = [cycles_to_map(cycles[name]) for name in names]
    group = enumerate_group(generators)
    assert len(group) == 1920
    assert source_group["c75_lifted_group_order"] == 11520
    assert source_group["c75_ambient_c6_kernel_order"] == 6
    assert c81["source_model"]["effective_label_group_order"] == 1920
    for generator in generators:
        for mask in range(65536):
            image = 0
            for index in range(16):
                if mask & (1 << index):
                    image |= 1 << generator[index]
            assert truth[mask] == truth[image]

    first_rows = compute_first_rows(truth)
    pair_rows, pair_lookup = compute_pair_rows(truth)
    label_orbits, pair_orbits, pair_to_orbit = expected_orbits(
        generators, first_rows, pair_lookup
    )
    classes = expected_classes(pair_rows, pair_to_orbit)

    first_atlas = evidence["first_order_atlas"]
    assert first_atlas["row_count"] == 16
    assert first_atlas["coalition_size_range"] == list(range(16))
    assert first_atlas["rows"] == first_rows
    assert first_atlas["total_swing_count"] == 40704
    assert first_atlas["sum_uniform_banzhaf_influence"] == "159/128"
    assert first_atlas["sum_shapley_shubik_value"] == "1"
    assert sum(Fraction(row["shapley_shubik_value"]) for row in first_rows) == truth[-1] - truth[0] == 1
    assert first_atlas["faithful_label_orbit_count"] == 7
    assert first_atlas["faithful_label_orbits"] == label_orbits

    c73_importance = {row["label"]: row for row in c73["coordinate_importance"]["rows"]}
    for row in first_rows:
        source = c73_importance[row["label"]]
        assert row["swing_count"] == source["pivotal_coalition_count"]
        assert row["uniform_banzhaf_influence"] == source["uniform_banzhaf_influence"]
        assert row["shapley_shubik_value"] == source["shapley_value"]

    dummy_set = set(c78["definition"]["dummy_labels"])
    for row in first_rows:
        assert (row["swing_count"] == 0) == (row["label"] in dummy_set)
    zero_pairs = [row for row in pair_rows if row["positive_delta_count"] == row["negative_delta_count"] == 0]
    assert len(zero_pairs) == 75
    assert all(any(label in dummy_set for label in row["pair"]) for row in zero_pairs)

    second_atlas = evidence["second_order_atlas"]
    assert second_atlas["row_count"] == 120
    assert second_atlas["coalition_size_range"] == list(range(15))
    assert second_atlas["rows"] == pair_rows
    assert second_atlas["faithful_pair_orbit_count"] == 27
    assert second_atlas["faithful_pair_orbit_size_spectrum"] == {
        str(size): count for size, count in sorted(Counter(row["orbit_size"] for row in pair_orbits).items())
    }
    assert second_atlas["faithful_pair_orbits"] == pair_orbits
    assert second_atlas["numerical_class_count"] == 10
    assert second_atlas["numerical_classes"] == classes
    assert sum(row["orbit_size"] for row in pair_orbits) == 120
    assert sum(row["pair_count"] for row in classes) == 120

    incident_shapley = {}
    incident_banzhaf = {}
    endpoint_contrast = {}
    for index, label in enumerate(LABELS):
        incident = [row for pair, row in pair_lookup.items() if index in pair]
        incident_shapley[label] = fraction_text(sum(
            Fraction(row["shapley_pair_interaction"]) for row in incident
        ))
        incident_banzhaf[label] = fraction_text(sum(
            Fraction(row["uniform_banzhaf_interaction"]) for row in incident
        ))
        without = 65535 ^ (1 << index)
        endpoint_contrast[label] = str(
            (truth[65535] - truth[without]) - (truth[1 << index] - truth[0])
        )
    assert incident_shapley == endpoint_contrast
    assert evidence["identities"] == {
        "first_order_shapley_efficiency": {
            "left_sum": "1",
            "right_endpoint_difference": "1",
            "verified": True,
        },
        "second_order_shapley_endpoint_identity": {
            "formula": "sum_{j!=i} I^Sh_{ij}=Delta_i F(L\\{i})-Delta_i F(empty)",
            "incident_pair_sum_by_label": incident_shapley,
            "endpoint_contrast_by_label": endpoint_contrast,
            "verified_for_all_16_labels": True,
        },
        "second_order_global_sums": {
            "sum_unordered_shapley_pair_interactions": fraction_text(sum(
                Fraction(row["shapley_pair_interaction"]) for row in pair_rows
            )),
            "sum_unordered_uniform_banzhaf_interactions": fraction_text(sum(
                Fraction(row["uniform_banzhaf_interaction"]) for row in pair_rows
            )),
            "incident_uniform_banzhaf_sum_by_label": incident_banzhaf,
            "banzhaf_efficiency_claimed": False,
        },
        "faithful_group_orbit_constancy": {
            "first_order_label_orbits_checked": 7,
            "second_order_pair_orbits_checked": 27,
            "verified": True,
        },
        "c82_distance_one_boundary_identity": {
            "formula": "total_swing_count+C82_autocorrelation_by_distance[1]=16*one_count",
            "total_swing_count": 40704,
            "c82_autocorrelation_by_distance_one": int(
                c82["bitflip_noise"]["autocorrelation_by_distance"]["1"]
            ),
            "dimension_times_one_count": 16 * sum(truth),
            "verified": True,
        },
    }
    assert 40704 + int(c82["bitflip_noise"]["autocorrelation_by_distance"]["1"]) == 16 * 30400

    assert evidence["source_model"] == {
        "label_order": list(LABELS),
        "label_count": 16,
        "support_count": 65536,
        "one_count": 30400,
        "predicate_construction": "edge containment over the 25 C73 minimal generating supports",
        "equivalent_block_criterion": "S9 is present and at least two direction blocks are met",
        "pivot": "S9",
        "direction_blocks": block_labels,
        "direction_block_sizes": [1, 1, 2, 5],
        "dummy_labels": c78["definition"]["dummy_labels"],
        "minimal_generation_edge_count": 25,
        "ambient_lift_order": 11520,
        "ambient_label_action_kernel_order": 6,
        "faithful_label_group_order": 1920,
        "faithful_label_group_candidate": source_group["effective_label_group_candidate"],
        "faithful_generator_names": names,
        "faithful_generator_cycles": cycles,
    }
    assert evidence["definitions"] == {
        "first_difference": "Delta_i F(A)=F(A union {i})-F(A), A subset L\\{i}",
        "first_order_uniform_banzhaf": "2^-15 sum_A Delta_i F(A)",
        "first_order_shapley_shubik": "sum_k c_i(k) k!(15-k)!/16!",
        "second_difference": "Delta_ij F(A)=F(A union {i,j})-F(A union {i})-F(A union {j})+F(A)",
        "second_order_uniform_banzhaf": "2^-14 sum_A Delta_ij F(A)",
        "second_order_shapley_pair": "sum_k d_ij(k) k!(14-k)!/15!",
        "coalition_size_convention": "first-order k ranges 0..15; second-order k ranges 0..14",
    }
    assert evidence["claims"] == {
        "all_65536_supports_enumerated": True,
        "all_16_first_order_rows_retained": True,
        "coalition_size_resolved_first_order_atlas": True,
        "all_120_unordered_pair_rows_retained": True,
        "positive_and_negative_second_differences_retained": True,
        "faithful_1920_label_and_pair_orbits_computed": True,
        "ambient_11520_lift_used_as_label_group": False,
        "full_burnside_ring_claimed": False,
        "full_table_of_marks_claimed": False,
        "arithmetic_local_claimed": False,
        "euler_or_root_number_claimed": False,
        "automorphy_claimed": False,
        "hilbert_polya_operator_claimed": False,
    }
    print(json.dumps({
        "status": "C87_INDEPENDENT_CHECK_PASS",
        "support_count": len(truth),
        "first_order_rows": len(first_rows),
        "second_order_rows": len(pair_rows),
        "label_orbits": len(label_orbits),
        "pair_orbits": len(pair_orbits),
        "numerical_classes": len(classes),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
