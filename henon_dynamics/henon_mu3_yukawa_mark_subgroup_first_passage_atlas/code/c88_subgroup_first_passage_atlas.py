#!/usr/bin/env python3
"""Produce the exact C88 subgroup first-passage atlas."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C83 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time"
C85 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_threshold_vector_poset_rigidity"
OUT = PROJECT / "results/c88_subgroup_first_passage_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
LABEL_COUNT = 16
SUPPORT_COUNT = 1 << LABEL_COUNT
TOTAL_PERMUTATIONS = factorial(LABEL_COUNT)
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c83": "033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28",
    "c83_manifest": "981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85",
    "c85": "22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152",
    "c85_manifest": "d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261",
}

Point = tuple[int, int, int]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def add(left: Point, right: Point) -> Point:
    return tuple(
        (left_value + right_value) % modulus
        for left_value, right_value, modulus in zip(left, right, MODULI)
    )  # type: ignore[return-value]


def multiple(coefficient: int, value: Point) -> Point:
    return tuple(
        coefficient * coordinate % modulus
        for coordinate, modulus in zip(value, MODULI)
    )  # type: ignore[return-value]


def cyclic_subgroup(value: Point) -> frozenset[Point]:
    for order in range(1, 55):
        if multiple(order, value) == (0, 0, 0):
            return frozenset(multiple(coefficient, value) for coefficient in range(order))
    raise AssertionError("finite-order search failed")


def point_mask(values: frozenset[Point], point_index: dict[Point, int]) -> int:
    return sum(1 << point_index[value] for value in values)


def source_paths() -> dict[str, Path]:
    return {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c83": C83 / "results/c83_random_order_stopping_time_evidence.json",
        "c83_manifest": C83 / "C83_PREFREEZE_MANIFEST.json",
        "c85": C85 / "results/c85_threshold_vector_poset_rigidity_evidence.json",
        "c85_manifest": C85 / "C85_PREFREEZE_MANIFEST.json",
    }


def hit_bitset(hit: list[bool]) -> str:
    raw = bytearray(SUPPORT_COUNT // 8)
    for support, value in enumerate(hit):
        if value:
            raw[support // 8] |= 1 << (support % 8)
    return bytes(raw).hex()


def nonzero_string_map(values: dict[str, int]) -> dict[str, int]:
    return {key: value for key, value in values.items() if value}


def main() -> None:
    paths = source_paths()
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c75, c83, c85 = (json.loads(raw[name]) for name in ("c75", "c83", "c85"))
    assert raw["c75"] == canonical(c75)
    assert raw["c83"] == canonical(c83)
    assert raw["c85"] == canonical(c85)
    assert c75["status"] == c83["status"] == c85["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == c83["scope_literal"] == c85["scope_literal"] == FIREWALL

    points = list(product(range(9), range(3), range(2)))
    point_index = {point: index for index, point in enumerate(points)}
    subgroup_rows = c75["closure_incidence"]["all_subgroups"]
    assert len(subgroup_rows) == 20
    subgroup_masks = [
        point_mask(frozenset(tuple(point) for point in row["subgroup_points"]), point_index)
        for row in subgroup_rows
    ]
    subgroup_index = {mask: index for index, mask in enumerate(subgroup_masks)}
    assert len(subgroup_index) == 20
    subgroup_members = [
        [index for index in range(len(points)) if mask & (1 << index)]
        for mask in subgroup_masks
    ]

    coordinates = [tuple(point) for point in c75["named_coordinate_source"]["coordinates"]]
    assert len(coordinates) == LABEL_COUNT
    cyclic_masks = [point_mask(cyclic_subgroup(point), point_index) for point in coordinates]

    def extension(left_index: int, right_mask: int) -> int:
        right_members = [index for index in range(len(points)) if right_mask & (1 << index)]
        result = 0
        for left_point in subgroup_members[left_index]:
            for right_point in right_members:
                result |= 1 << point_index[add(points[left_point], points[right_point])]
        return subgroup_index[result]

    transition = [
        [extension(subgroup, cyclic_mask) for cyclic_mask in cyclic_masks]
        for subgroup in range(len(subgroup_masks))
    ]
    zero_mask = point_mask(frozenset({(0, 0, 0)}), point_index)
    zero_index = subgroup_index[zero_mask]
    closure = [zero_index] * SUPPORT_COUNT
    for support in range(1, SUPPORT_COUNT):
        low = support & -support
        closure[support] = transition[closure[support ^ low]][low.bit_length() - 1]
    assert closure[(1 << LABEL_COUNT) - 1] == 19

    inclusion = [
        [int(left_mask & ~right_mask == 0) for right_mask in subgroup_masks]
        for left_mask in subgroup_masks
    ]
    assert inclusion == c85["poset"]["inclusion_matrix"]
    covers = [
        [lower, upper]
        for lower in range(20)
        for upper in range(20)
        if lower != upper
        and inclusion[lower][upper]
        and not any(
            middle not in (lower, upper)
            and inclusion[lower][middle]
            and inclusion[middle][upper]
            for middle in range(20)
        )
    ]

    target_rows: list[dict[str, Any]] = []
    hit_tables: list[list[bool]] = []
    expectations: list[Fraction] = []
    for target in range(20):
        hit = [bool(inclusion[target][closed]) for closed in closure]
        hit_tables.append(hit)
        hit_counts = Counter()
        nonhit_counts = Counter()
        pivotal_edges = Counter()
        pivotal_patterns = Counter()
        minimal_supports: list[int] = []
        for support, is_hit in enumerate(hit):
            cardinality = support.bit_count()
            if not is_hit:
                nonhit_counts[cardinality] += 1
                continue
            hit_counts[cardinality] += 1
            pivotal = sum(
                not hit[support ^ (1 << label)]
                for label in range(LABEL_COUNT)
                if support & (1 << label)
            )
            pivotal_edges[cardinality] += pivotal
            pivotal_patterns[(cardinality, pivotal)] += 1
            if support == 0 or pivotal == cardinality:
                minimal_supports.append(support)

        assert all(
            hit_counts[cardinality] + nonhit_counts[cardinality] == comb(LABEL_COUNT, cardinality)
            for cardinality in range(LABEL_COUNT + 1)
        )
        assert all(
            hit[support]
            == any(support & minimal == minimal for minimal in minimal_supports)
            for support in range(SUPPORT_COUNT)
        )

        permutation_counts: dict[str, int] = {}
        probability_by_time: dict[str, dict[str, int]] = {}
        previous_cdf = Fraction(0)
        for time in range(LABEL_COUNT + 1):
            cdf = Fraction(hit_counts[time], comb(LABEL_COUNT, time))
            count = int((cdf - previous_cdf) * TOTAL_PERMUTATIONS)
            assert count >= 0
            if time == 0:
                assert count == (TOTAL_PERMUTATIONS if hit[0] else 0)
            else:
                pivotal_count = pivotal_edges[time] * factorial(time - 1) * factorial(LABEL_COUNT - time)
                assert count == pivotal_count
            permutation_counts[str(time)] = count
            probability_by_time[str(time)] = rational(Fraction(count, TOTAL_PERMUTATIONS))
            previous_cdf = cdf
        assert sum(permutation_counts.values()) == TOTAL_PERMUTATIONS

        survival_counts = {
            str(time): nonhit_counts[time] * factorial(time) * factorial(LABEL_COUNT - time)
            for time in range(LABEL_COUNT + 1)
        }
        survival_probability = {
            str(time): rational(Fraction(nonhit_counts[time], comb(LABEL_COUNT, time)))
            for time in range(LABEL_COUNT + 1)
        }
        hit_probability = {
            str(time): rational(Fraction(hit_counts[time], comb(LABEL_COUNT, time)))
            for time in range(LABEL_COUNT + 1)
        }
        expected_from_survival = sum(
            (Fraction(nonhit_counts[time], comb(LABEL_COUNT, time)) for time in range(LABEL_COUNT)),
            Fraction(0),
        )
        expected_from_distribution = Fraction(
            sum(int(time) * count for time, count in permutation_counts.items()),
            TOTAL_PERMUTATIONS,
        )
        assert expected_from_survival == expected_from_distribution
        expectations.append(expected_from_survival)
        support_bitset = hit_bitset(hit)
        nonzero_times = [int(time) for time, count in permutation_counts.items() if count]
        minimal_by_cardinality = Counter(mask.bit_count() for mask in minimal_supports)

        target_rows.append({
            "target_subgroup_index": target,
            "target_subgroup_order": subgroup_rows[target]["subgroup_order"],
            "minimum_first_passage_time": min(nonzero_times),
            "maximum_first_passage_time": max(nonzero_times),
            "minimal_hitting_support_masks": minimal_supports,
            "minimal_hitting_support_count_by_cardinality": {
                str(cardinality): minimal_by_cardinality[cardinality]
                for cardinality in sorted(minimal_by_cardinality)
            },
            "subset_hit_bitset_hex": support_bitset,
            "subset_hit_bitset_sha256": digest(bytes.fromhex(support_bitset)),
            "subset_hit_count_by_cardinality": {
                str(cardinality): hit_counts[cardinality]
                for cardinality in range(LABEL_COUNT + 1)
            },
            "subset_nonhit_count_by_cardinality": {
                str(cardinality): nonhit_counts[cardinality]
                for cardinality in range(LABEL_COUNT + 1)
            },
            "subset_hit_probability_by_cardinality": hit_probability,
            "subset_survival_probability_by_cardinality": survival_probability,
            "pivotal_edge_count_by_cardinality": {
                str(cardinality): pivotal_edges[cardinality]
                for cardinality in range(LABEL_COUNT + 1)
            },
            "pivotal_pattern_counts": {
                f"{cardinality},{pivotal}": count
                for (cardinality, pivotal), count in sorted(pivotal_patterns.items())
            },
            "permutation_count_by_first_passage_time": permutation_counts,
            "probability_by_first_passage_time": probability_by_time,
            "survival_permutation_count_after_time": survival_counts,
            "expected_first_passage_time": rational(expected_from_survival),
        })

    monotonicity_pairs: list[dict[str, Any]] = []
    for lower in range(20):
        for upper in range(20):
            if not inclusion[lower][upper]:
                continue
            assert all(
                not hit_tables[upper][support] or hit_tables[lower][support]
                for support in range(SUPPORT_COUNT)
            )
            lower_row = target_rows[lower]
            upper_row = target_rows[upper]
            assert all(
                lower_row["subset_hit_count_by_cardinality"][str(time)]
                >= upper_row["subset_hit_count_by_cardinality"][str(time)]
                for time in range(LABEL_COUNT + 1)
            )
            assert all(
                lower_row["survival_permutation_count_after_time"][str(time)]
                <= upper_row["survival_permutation_count_after_time"][str(time)]
                for time in range(LABEL_COUNT + 1)
            )
            assert expectations[lower] <= expectations[upper]
            monotonicity_pairs.append({
                "lower_subgroup_index": lower,
                "upper_subgroup_index": upper,
                "subsetwise_first_passage_order": True,
                "cdf_order_all_times": True,
                "survival_order_all_times": True,
                "expectation_order": True,
            })
    assert len(monotonicity_pairs) == 102

    top = target_rows[19]
    reference = c83["assembly_atlas"]
    top_checks = {
        "subset_hit_counts": nonzero_string_map(top["subset_hit_count_by_cardinality"])
        == reference["full_support_count_by_cardinality"],
        "pivotal_edge_counts": nonzero_string_map(top["pivotal_edge_count_by_cardinality"])
        == reference["pivotal_support_count_by_cardinality"],
        "pivotal_patterns": top["pivotal_pattern_counts"] == reference["pivotal_pattern_counts"],
        "permutation_counts": top["permutation_count_by_first_passage_time"]
        == reference["permutation_count_by_stopping_time"],
        "probabilities": top["probability_by_first_passage_time"]
        == reference["probability_by_stopping_time"],
        "survival_counts": top["survival_permutation_count_after_time"]
        == reference["survival_permutation_counts"],
        "expectation": top["expected_first_passage_time"] == reference["expected_stopping_time"],
        "total_permutations": TOTAL_PERMUTATIONS == reference["total_permutations"],
    }
    assert all(top_checks.values())

    result: dict[str, Any] = {
        "schema_id": "hcs-c88-subgroup-first-passage-atlas-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_object": "uniform permutation of the sixteen C75 named labels",
            "prefix_support": "A_k is the set of the first k labels, with A_0 empty",
            "target_first_passage_time": "T_H=min{k:H<=Phi(A_k)}",
            "subset_hit_count": "F_H(k)=#{A:|A|=k and H<=Phi(A)}",
            "cdf_formula": "P(T_H<=k)=F_H(k)/binom(16,k)",
            "pivotal_formula": "N_H(k)=sum_{|S|=k,H<=Phi(S)}p_H(S)(k-1)!(16-k)! for k>=1",
            "survival_formula": "P(T_H>k)=1-F_H(k)/binom(16,k)",
            "expectation_formula": "E[T_H]=sum_{k=0}^{15}P(T_H>k)",
            "trivial_target_convention": "T_{H_0}=0 for every permutation",
            "relation_convention": "H_i<=H_j implies T_{H_i}<=T_{H_j} pointwise",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": LABEL_COUNT,
            "support_count": SUPPORT_COUNT,
            "subgroup_count": len(subgroup_rows),
            "total_permutations": TOTAL_PERMUTATIONS,
            "target_subgroup_indices": list(range(20)),
            "target_subgroup_orders": [row["subgroup_order"] for row in subgroup_rows],
            "coordinate_sha256": c75["named_coordinate_source"]["coordinate_sha256"],
        },
        "first_passage_atlas": {
            "target_rows": target_rows,
        },
        "target_poset": {
            "inclusion_matrix": inclusion,
            "cover_relations": covers,
            "comparable_ordered_pair_count_including_reflexive": len(monotonicity_pairs),
            "monotonicity_pairs": monotonicity_pairs,
        },
        "c83_top_target_identity": {
            "target_subgroup_index": 19,
            "c83_assembly_atlas_sha256": digest(canonical(reference)),
            "field_checks": top_checks,
            "all_fields_match": True,
        },
        "checks": {
            "all_65536_supports_enumerated": True,
            "all_20_targets_enumerated": True,
            "all_minimal_support_antichains_reconstructed": True,
            "all_probability_rows_normalized": True,
            "all_pivotal_identities_verified": True,
            "all_survival_expectation_identities_verified": True,
            "all_102_inclusion_pairs_monotone": True,
            "c85_inclusion_matrix_matches_point_containment": True,
            "c83_top_target_row_matches_exactly": True,
        },
        "claims": {
            "exact_finite_uniform_permutation_law": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "target_count": len(target_rows),
        "comparable_pair_count": len(monotonicity_pairs),
        "top_expected_first_passage_time": top["expected_first_passage_time"],
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
