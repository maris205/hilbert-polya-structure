#!/usr/bin/env python3
"""Produce the C87 label influence and pair-interaction atlas."""

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
OUT = PROJECT / "results/c87_label_influence_interaction_atlas_evidence.json"
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

Permutation = tuple[int, ...]
Pair = tuple[int, int]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def label_index(label: str) -> int:
    return int(label[1:]) - 1


def labels_for_pair(pair: Pair) -> list[str]:
    return [LABELS[pair[0]], LABELS[pair[1]]]


def mask_for_labels(labels: list[str]) -> int:
    return sum(1 << label_index(label) for label in labels)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(16))


def permutation_from_cycles(cycles: list[list[str]]) -> Permutation:
    permutation = list(range(16))
    for cycle_labels in cycles:
        cycle = [label_index(label) for label in cycle_labels]
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            permutation[source] = target
    return tuple(permutation)


def close_group(generators: list[Permutation]) -> list[Permutation]:
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


def load_sources() -> dict[str, Any]:
    raw = {name: path.read_bytes() for name, path in SOURCE_PATHS.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    sources = {name: json.loads(value) for name, value in raw.items()}
    for name in ("c73", "c76", "c78", "c81", "c82"):
        assert sources[name]["status"] == "PREFREEZE_G3_PASS"
        assert sources[name]["scope_literal"] == FIREWALL
    for name in ("c73_manifest", "c76_manifest", "c78_manifest", "c81_manifest", "c82_manifest"):
        assert sources[name]["status"] == "PREFREEZE_COMPLETE_NOT_RELEASED"
        assert sources[name]["scope_literal"] == FIREWALL
    return sources


def first_order_rows(truth: list[int]) -> list[dict[str, Any]]:
    rows = []
    for index, label in enumerate(LABELS):
        bit = 1 << index
        by_size = [0] * 16
        for coalition in range(1 << 16):
            if coalition & bit:
                continue
            delta = truth[coalition | bit] - truth[coalition]
            assert delta in (0, 1)
            by_size[coalition.bit_count()] += delta
        swing_count = sum(by_size)
        shapley = sum(
            Fraction(count * factorial(size) * factorial(15 - size), factorial(16))
            for size, count in enumerate(by_size)
        )
        rows.append({
            "label": label,
            "coalition_size_swing_counts": by_size,
            "swing_count": swing_count,
            "uniform_banzhaf_influence": fraction_text(Fraction(swing_count, 2 ** 15)),
            "shapley_shubik_value": fraction_text(shapley),
        })
    return rows


def second_order_rows(truth: list[int]) -> tuple[list[dict[str, Any]], dict[Pair, dict[str, Any]]]:
    rows = []
    by_pair: dict[Pair, dict[str, Any]] = {}
    for first, second in combinations(range(16), 2):
        first_bit = 1 << first
        second_bit = 1 << second
        forbidden = first_bit | second_bit
        positive_by_size = [0] * 15
        negative_by_size = [0] * 15
        for coalition in range(1 << 16):
            if coalition & forbidden:
                continue
            delta = (
                truth[coalition | forbidden]
                - truth[coalition | first_bit]
                - truth[coalition | second_bit]
                + truth[coalition]
            )
            assert delta in (-1, 0, 1)
            size = coalition.bit_count()
            if delta == 1:
                positive_by_size[size] += 1
            elif delta == -1:
                negative_by_size[size] += 1
        signed_by_size = [
            positive_by_size[size] - negative_by_size[size]
            for size in range(15)
        ]
        positive_count = sum(positive_by_size)
        negative_count = sum(negative_by_size)
        signed_sum = positive_count - negative_count
        shapley = sum(
            Fraction(count * factorial(size) * factorial(14 - size), factorial(15))
            for size, count in enumerate(signed_by_size)
        )
        row = {
            "pair": labels_for_pair((first, second)),
            "positive_delta_by_coalition_size": positive_by_size,
            "negative_delta_by_coalition_size": negative_by_size,
            "signed_delta_by_coalition_size": signed_by_size,
            "positive_delta_count": positive_count,
            "negative_delta_count": negative_count,
            "zero_delta_count": 2 ** 14 - positive_count - negative_count,
            "signed_delta_sum": signed_sum,
            "uniform_banzhaf_interaction": fraction_text(Fraction(signed_sum, 2 ** 14)),
            "shapley_pair_interaction": fraction_text(shapley),
        }
        rows.append(row)
        by_pair[(first, second)] = row
    return rows, by_pair


def pair_signature(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        tuple(row["positive_delta_by_coalition_size"]),
        tuple(row["negative_delta_by_coalition_size"]),
        tuple(row["signed_delta_by_coalition_size"]),
        row["positive_delta_count"],
        row["negative_delta_count"],
        row["zero_delta_count"],
        row["signed_delta_sum"],
        row["uniform_banzhaf_interaction"],
        row["shapley_pair_interaction"],
    )


def build_orbits(
    group: list[Permutation],
    first_rows: list[dict[str, Any]],
    pair_rows: list[dict[str, Any]],
    pair_by_index: dict[Pair, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[Pair, str]]:
    label_orbits = []
    unseen_labels = set(range(16))
    while unseen_labels:
        representative = min(unseen_labels)
        orbit = sorted({permutation[representative] for permutation in group})
        unseen_labels.difference_update(orbit)
        signature = {
            key: first_rows[representative][key]
            for key in (
                "coalition_size_swing_counts",
                "swing_count",
                "uniform_banzhaf_influence",
                "shapley_shubik_value",
            )
        }
        for member in orbit:
            assert all(first_rows[member][key] == value for key, value in signature.items())
        label_orbits.append({
            "orbit_id": f"L{len(label_orbits) + 1:02d}",
            "representative": LABELS[representative],
            "labels": [LABELS[index] for index in orbit],
            "orbit_size": len(orbit),
            "first_order_signature": signature,
        })

    pair_orbits = []
    pair_to_orbit: dict[Pair, str] = {}
    unseen_pairs = set(combinations(range(16), 2))
    while unseen_pairs:
        representative = min(unseen_pairs)
        orbit = sorted({
            tuple(sorted((permutation[representative[0]], permutation[representative[1]])))
            for permutation in group
        })
        assert set(orbit) <= unseen_pairs
        unseen_pairs.difference_update(orbit)
        signature = pair_signature(pair_by_index[representative])
        assert all(pair_signature(pair_by_index[pair]) == signature for pair in orbit)
        orbit_id = f"P{len(pair_orbits) + 1:02d}"
        for pair in orbit:
            pair_to_orbit[pair] = orbit_id
        source = pair_by_index[representative]
        pair_orbits.append({
            "orbit_id": orbit_id,
            "representative_pair": labels_for_pair(representative),
            "member_pairs": [labels_for_pair(pair) for pair in orbit],
            "orbit_size": len(orbit),
            "positive_delta_count": source["positive_delta_count"],
            "negative_delta_count": source["negative_delta_count"],
            "uniform_banzhaf_interaction": source["uniform_banzhaf_interaction"],
            "shapley_pair_interaction": source["shapley_pair_interaction"],
        })
    assert len(pair_rows) == len(pair_to_orbit) == 120
    return label_orbits, pair_orbits, pair_to_orbit


def numerical_classes(
    pair_rows: list[dict[str, Any]], pair_to_orbit: dict[Pair, str]
) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], list[Pair]] = {}
    for row in pair_rows:
        pair = tuple(label_index(label) for label in row["pair"])
        signature = (
            row["positive_delta_count"],
            row["negative_delta_count"],
            row["uniform_banzhaf_interaction"],
            row["shapley_pair_interaction"],
        )
        grouped.setdefault(signature, []).append(pair)
    rows = []
    for signature, members in grouped.items():
        positive, negative, banzhaf, shapley = signature
        rows.append({
            "class_id": f"K{len(rows) + 1:02d}",
            "representative_pair": labels_for_pair(members[0]),
            "member_pairs": [labels_for_pair(pair) for pair in members],
            "pair_count": len(members),
            "pair_orbit_ids": sorted({pair_to_orbit[pair] for pair in members}),
            "pair_orbit_count": len({pair_to_orbit[pair] for pair in members}),
            "positive_delta_count_per_pair": positive,
            "negative_delta_count_per_pair": negative,
            "uniform_banzhaf_interaction": banzhaf,
            "shapley_pair_interaction": shapley,
        })
    return rows


def build_result(sources: dict[str, Any]) -> dict[str, Any]:
    c73 = sources["c73"]
    c76 = sources["c76"]
    c78 = sources["c78"]
    c81 = sources["c81"]
    c82 = sources["c82"]

    assert c73["type_order"] == list(LABELS)
    edges = c73["generation_structure"]["minimal_generating_edges"]
    assert len(edges) == 25
    edge_masks = [mask_for_labels(edge) for edge in edges]
    truth = [int(any(mask & edge == edge for edge in edge_masks)) for mask in range(1 << 16)]
    assert sum(truth) == 30400

    definition = c78["definition"]
    direction_blocks = definition["direction_blocks"]
    dummy_labels = definition["dummy_labels"]
    assert definition["pivot"] == "S9"
    assert direction_blocks == c73["generation_structure"]["projective_direction_blocks"][0:0] + [
        ["S1"], ["S16"], ["S7", "S15"], ["S3", "S4", "S8", "S11", "S12"]
    ]
    assert dummy_labels == ["S2", "S5", "S6", "S10", "S13", "S14"]
    assert c82["predicate"]["one_count"] == sum(truth)
    assert c82["predicate"]["support_count"] == 1 << 16
    c82_distance_one = int(c82["bitflip_noise"]["autocorrelation_by_distance"]["1"])

    source_model = c76["source_model"]
    generator_names = source_model["effective_generator_names"]
    cycles = source_model["effective_generator_cycles"]
    generators = [permutation_from_cycles(cycles[name]) for name in generator_names]
    group = close_group(generators)
    assert source_model["c75_lifted_group_order"] == 11520
    assert source_model["c75_ambient_c6_kernel_order"] == 6
    assert source_model["effective_label_group_order"] == len(group) == 1920
    assert c81["source_model"]["c75_ambient_lift_order"] == 11520
    assert c81["source_model"]["c75_lift_kernel_order"] == 6
    assert c81["source_model"]["effective_label_group_order"] == 1920
    assert all(
        truth[mask] == truth[
            sum(1 << permutation[index] for index in range(16) if mask & (1 << index))
        ]
        for permutation in generators
        for mask in range(1 << 16)
    )

    first_rows = first_order_rows(truth)
    pair_rows, pair_by_index = second_order_rows(truth)
    label_orbits, pair_orbits, pair_to_orbit = build_orbits(
        group, first_rows, pair_rows, pair_by_index
    )
    classes = numerical_classes(pair_rows, pair_to_orbit)

    first_by_label = {row["label"]: row for row in first_rows}
    expected_vectors = {
        "S1": [0, 0, 8, 59, 196, 390, 521, 494, 339, 166, 55, 11, 1, 0, 0, 0],
        "S7": [0, 0, 7, 52, 175, 355, 486, 473, 332, 165, 55, 11, 1, 0, 0, 0],
        "S3": [0, 0, 4, 25, 66, 95, 80, 39, 10, 1, 0, 0, 0, 0, 0, 0],
        "S9": [0, 0, 25, 224, 940, 2461, 4504, 6095, 6269, 4950, 2992, 1364, 455, 105, 15, 1],
    }
    assert all(first_by_label[label]["coalition_size_swing_counts"] == vector for label, vector in expected_vectors.items())
    assert [(row["swing_count"], row["uniform_banzhaf_influence"], row["shapley_shubik_value"]) for row in first_rows] == [
        (2240, "35/512", "61/1260"), (0, "0", "0"), (320, "5/512", "31/2520"),
        (320, "5/512", "31/2520"), (0, "0", "0"), (0, "0", "0"),
        (2112, "33/512", "2/45"), (320, "5/512", "31/2520"),
        (30400, "475/512", "271/360"), (0, "0", "0"),
        (320, "5/512", "31/2520"), (320, "5/512", "31/2520"),
        (0, "0", "0"), (0, "0", "0"), (2112, "33/512", "2/45"),
        (2240, "35/512", "61/1260"),
    ]
    assert sum(row["swing_count"] for row in first_rows) == 40704
    assert sum(row["swing_count"] for row in first_rows) + c82_distance_one == 16 * sum(truth)
    assert sum(Fraction(row["shapley_shubik_value"]) for row in first_rows) == 1
    assert [row["labels"] for row in label_orbits] == [
        ["S1", "S16"], ["S2"], ["S3", "S4", "S11", "S12"],
        ["S5", "S6", "S10", "S13", "S14"], ["S7", "S15"], ["S8"], ["S9"],
    ]

    assert len(pair_rows) == 120
    assert len(pair_orbits) == 27
    assert Counter(row["orbit_size"] for row in pair_orbits) == Counter({
        1: 5, 2: 7, 4: 7, 5: 3, 8: 1, 10: 3, 20: 1,
    })
    class_summary = [
        (
            row["pair_count"], row["positive_delta_count_per_pair"],
            row["negative_delta_count_per_pair"], row["uniform_banzhaf_interaction"],
            row["shapley_pair_interaction"],
        )
        for row in classes
    ]
    assert class_summary == [
        (75, 0, 0, "0", "0"),
        (10, 64, 256, "-3/256", "0"),
        (4, 64, 2048, "-31/256", "-5/84"),
        (2, 2240, 0, "35/256", "31/168"),
        (1, 64, 2176, "-33/256", "-11/168"),
        (10, 0, 320, "-5/256", "-1/56"),
        (10, 64, 128, "-1/256", "1/168"),
        (5, 320, 0, "5/256", "5/84"),
        (2, 2112, 0, "33/256", "1/6"),
        (1, 0, 2112, "-33/256", "-13/168"),
    ]

    pair_shapley_by_label = {}
    pair_banzhaf_by_label = {}
    endpoint_contrast_by_label = {}
    for index, label in enumerate(LABELS):
        incident = [
            row for pair, row in pair_by_index.items() if index in pair
        ]
        pair_shapley_by_label[label] = fraction_text(sum(
            Fraction(row["shapley_pair_interaction"]) for row in incident
        ))
        pair_banzhaf_by_label[label] = fraction_text(sum(
            Fraction(row["uniform_banzhaf_interaction"]) for row in incident
        ))
        without = ((1 << 16) - 1) ^ (1 << index)
        endpoint_contrast_by_label[label] = str(
            (truth[-1] - truth[without]) - (truth[1 << index] - truth[0])
        )
    assert pair_shapley_by_label == endpoint_contrast_by_label
    assert pair_shapley_by_label == {
        label: ("1" if label == "S9" else "0") for label in LABELS
    }
    total_pair_shapley = sum(Fraction(row["shapley_pair_interaction"]) for row in pair_rows)
    total_pair_banzhaf = sum(Fraction(row["uniform_banzhaf_interaction"]) for row in pair_rows)
    assert total_pair_shapley == Fraction(1, 2)

    c73_rows = {row["label"]: row for row in c73["coordinate_importance"]["rows"]}
    for row in first_rows:
        upstream = c73_rows[row["label"]]
        assert row["swing_count"] == upstream["pivotal_coalition_count"]
        assert row["uniform_banzhaf_influence"] == upstream["uniform_banzhaf_influence"]
        assert row["shapley_shubik_value"] == upstream["shapley_value"]

    return {
        "schema_id": "hcs-c87-label-influence-interaction-atlas-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "source_model": {
            "label_order": list(LABELS),
            "label_count": 16,
            "support_count": 1 << 16,
            "one_count": sum(truth),
            "predicate_construction": "edge containment over the 25 C73 minimal generating supports",
            "equivalent_block_criterion": "S9 is present and at least two direction blocks are met",
            "pivot": "S9",
            "direction_blocks": direction_blocks,
            "direction_block_sizes": [len(block) for block in direction_blocks],
            "dummy_labels": dummy_labels,
            "minimal_generation_edge_count": len(edges),
            "ambient_lift_order": 11520,
            "ambient_label_action_kernel_order": 6,
            "faithful_label_group_order": len(group),
            "faithful_label_group_candidate": source_model["effective_label_group_candidate"],
            "faithful_generator_names": generator_names,
            "faithful_generator_cycles": cycles,
        },
        "definitions": {
            "first_difference": "Delta_i F(A)=F(A union {i})-F(A), A subset L\\{i}",
            "first_order_uniform_banzhaf": "2^-15 sum_A Delta_i F(A)",
            "first_order_shapley_shubik": "sum_k c_i(k) k!(15-k)!/16!",
            "second_difference": "Delta_ij F(A)=F(A union {i,j})-F(A union {i})-F(A union {j})+F(A)",
            "second_order_uniform_banzhaf": "2^-14 sum_A Delta_ij F(A)",
            "second_order_shapley_pair": "sum_k d_ij(k) k!(14-k)!/15!",
            "coalition_size_convention": "first-order k ranges 0..15; second-order k ranges 0..14",
        },
        "first_order_atlas": {
            "row_count": len(first_rows),
            "coalition_size_range": list(range(16)),
            "rows": first_rows,
            "total_swing_count": sum(row["swing_count"] for row in first_rows),
            "sum_uniform_banzhaf_influence": fraction_text(Fraction(sum(row["swing_count"] for row in first_rows), 2 ** 15)),
            "sum_shapley_shubik_value": fraction_text(sum(Fraction(row["shapley_shubik_value"]) for row in first_rows)),
            "faithful_label_orbit_count": len(label_orbits),
            "faithful_label_orbits": label_orbits,
        },
        "second_order_atlas": {
            "row_count": len(pair_rows),
            "coalition_size_range": list(range(15)),
            "rows": pair_rows,
            "faithful_pair_orbit_count": len(pair_orbits),
            "faithful_pair_orbit_size_spectrum": {
                str(size): count for size, count in sorted(Counter(row["orbit_size"] for row in pair_orbits).items())
            },
            "faithful_pair_orbits": pair_orbits,
            "numerical_class_count": len(classes),
            "numerical_classes": classes,
        },
        "identities": {
            "first_order_shapley_efficiency": {
                "left_sum": fraction_text(sum(Fraction(row["shapley_shubik_value"]) for row in first_rows)),
                "right_endpoint_difference": str(truth[-1] - truth[0]),
                "verified": True,
            },
            "second_order_shapley_endpoint_identity": {
                "formula": "sum_{j!=i} I^Sh_{ij}=Delta_i F(L\\{i})-Delta_i F(empty)",
                "incident_pair_sum_by_label": pair_shapley_by_label,
                "endpoint_contrast_by_label": endpoint_contrast_by_label,
                "verified_for_all_16_labels": True,
            },
            "second_order_global_sums": {
                "sum_unordered_shapley_pair_interactions": fraction_text(total_pair_shapley),
                "sum_unordered_uniform_banzhaf_interactions": fraction_text(total_pair_banzhaf),
                "incident_uniform_banzhaf_sum_by_label": pair_banzhaf_by_label,
                "banzhaf_efficiency_claimed": False,
            },
            "faithful_group_orbit_constancy": {
                "first_order_label_orbits_checked": len(label_orbits),
                "second_order_pair_orbits_checked": len(pair_orbits),
                "verified": True,
            },
            "c82_distance_one_boundary_identity": {
                "formula": "total_swing_count+C82_autocorrelation_by_distance[1]=16*one_count",
                "total_swing_count": sum(row["swing_count"] for row in first_rows),
                "c82_autocorrelation_by_distance_one": c82_distance_one,
                "dimension_times_one_count": 16 * sum(truth),
                "verified": True,
            },
        },
        "claims": {
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
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    result = build_result(load_sources())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "first_order_rows": result["first_order_atlas"]["row_count"],
        "second_order_rows": result["second_order_atlas"]["row_count"],
        "label_orbits": result["first_order_atlas"]["faithful_label_orbit_count"],
        "pair_orbits": result["second_order_atlas"]["faithful_pair_orbit_count"],
        "numerical_classes": result["second_order_atlas"]["numerical_class_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
