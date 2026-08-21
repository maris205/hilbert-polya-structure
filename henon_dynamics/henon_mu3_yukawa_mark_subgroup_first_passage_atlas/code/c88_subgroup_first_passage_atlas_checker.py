#!/usr/bin/env python3
"""Independent antichain reconstruction and semantic checker for C88."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C83 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time"
C85 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_threshold_vector_poset_rigidity"
EVIDENCE = PROJECT / "results/c88_subgroup_first_passage_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABEL_COUNT = 16
SUPPORT_COUNT = 1 << LABEL_COUNT
TOTAL = factorial(LABEL_COUNT)
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c83": "033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28",
    "c83_manifest": "981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85",
    "c85": "22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152",
    "c85_manifest": "d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return ((left[0] + right[0]) % 9, (left[1] + right[1]) % 3, (left[2] + right[2]) % 2)


def generate(values: list[tuple[int, int, int]]) -> frozenset[tuple[int, int, int]]:
    generated = {(0, 0, 0)}
    changed = True
    while changed:
        changed = False
        for left in tuple(generated):
            for right in values:
                value = add(left, right)
                if value not in generated:
                    generated.add(value)
                    changed = True
    return frozenset(generated)


def enumerate_subgroups() -> list[frozenset[tuple[int, int, int]]]:
    points = list(product(range(9), range(3), range(2)))
    cyclics = sorted({generate([point]) for point in points}, key=lambda group: (len(group), tuple(sorted(group))))
    zero = frozenset({(0, 0, 0)})
    found = {zero}
    queue = deque([zero])
    while queue:
        subgroup = queue.popleft()
        for cyclic in cyclics:
            enlarged = frozenset(add(left, right) for left in subgroup for right in cyclic)
            if enlarged not in found:
                found.add(enlarged)
                queue.append(enlarged)
    return sorted(found, key=lambda group: (len(group), tuple(sorted(group))))


def bitset_hex(hit: list[bool]) -> str:
    raw = bytearray(SUPPORT_COUNT // 8)
    for support, value in enumerate(hit):
        if value:
            raw[support // 8] |= 1 << (support % 8)
    return bytes(raw).hex()


def source_raw() -> dict[str, bytes]:
    paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c83": C83 / "results/c83_random_order_stopping_time_evidence.json",
        "c83_manifest": C83 / "C83_PREFREEZE_MANIFEST.json",
        "c85": C85 / "results/c85_threshold_vector_poset_rigidity_evidence.json",
        "c85_manifest": C85 / "C85_PREFREEZE_MANIFEST.json",
    }
    return {name: path.read_bytes() for name, path in paths.items()}


def build_expected() -> tuple[dict[str, Any], dict[str, Any]]:
    raw = source_raw()
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c75, c83, c85 = (json.loads(raw[name]) for name in ("c75", "c83", "c85"))
    assert all(raw[name] == canonical(value) for name, value in zip(
        ("c75", "c83", "c85"), (c75, c83, c85)
    ))
    assert c75["scope_literal"] == c83["scope_literal"] == c85["scope_literal"] == FIREWALL

    coordinates = [tuple(point) for point in c75["named_coordinate_source"]["coordinates"]]
    subgroup_rows = c75["closure_incidence"]["all_subgroups"]
    source_subgroups = [frozenset(tuple(point) for point in row["subgroup_points"]) for row in subgroup_rows]
    subgroups = enumerate_subgroups()
    assert len(subgroups) == 20
    assert subgroups == source_subgroups
    inclusion = [[int(left <= right) for right in subgroups] for left in subgroups]
    assert inclusion == c85["poset"]["inclusion_matrix"]
    cyclics = [generate([coordinate]) for coordinate in coordinates]
    generated_by_support = [frozenset({(0, 0, 0)})] * SUPPORT_COUNT
    for support in range(1, SUPPORT_COUNT):
        low = support & -support
        previous = generated_by_support[support ^ low]
        cyclic = cyclics[low.bit_length() - 1]
        generated_by_support[support] = frozenset(
            add(left, right) for left in previous for right in cyclic
        )

    target_rows = []
    hit_tables = []
    expectations = []
    for target_index, target in enumerate(subgroups):
        minimal: list[int] = []
        for size in range(LABEL_COUNT + 1):
            for labels in combinations(range(LABEL_COUNT), size):
                support = sum(1 << label for label in labels)
                if any(support & previous == previous for previous in minimal):
                    continue
                if target <= generated_by_support[support]:
                    minimal.append(support)
        minimal.sort()
        hit = [any(support & minimum == minimum for minimum in minimal) for support in range(SUPPORT_COUNT)]
        hit_tables.append(hit)
        hit_counts = {
            str(size): sum(value and support.bit_count() == size for support, value in enumerate(hit))
            for size in range(LABEL_COUNT + 1)
        }
        nonhit_counts = {
            str(size): comb(LABEL_COUNT, size) - hit_counts[str(size)]
            for size in range(LABEL_COUNT + 1)
        }
        pivotal_edges = {}
        pivotal_patterns: dict[str, int] = {}
        for size in range(LABEL_COUNT + 1):
            edge_total = 0
            for support, value in enumerate(hit):
                if not value or support.bit_count() != size:
                    continue
                pivotal = sum(
                    not hit[support ^ (1 << label)]
                    for label in range(LABEL_COUNT)
                    if support & (1 << label)
                )
                edge_total += pivotal
                key = f"{size},{pivotal}"
                pivotal_patterns[key] = pivotal_patterns.get(key, 0) + 1
            pivotal_edges[str(size)] = edge_total

        counts = {}
        probabilities = {}
        previous = Fraction(0)
        for time in range(LABEL_COUNT + 1):
            cdf = Fraction(hit_counts[str(time)], comb(LABEL_COUNT, time))
            count = int((cdf - previous) * TOTAL)
            if time:
                assert count == pivotal_edges[str(time)] * factorial(time - 1) * factorial(LABEL_COUNT - time)
            counts[str(time)] = count
            probabilities[str(time)] = rational(Fraction(count, TOTAL))
            previous = cdf
        expectation = sum(
            (Fraction(nonhit_counts[str(time)], comb(LABEL_COUNT, time)) for time in range(LABEL_COUNT)),
            Fraction(0),
        )
        expectations.append(expectation)
        nonzero = [int(time) for time, count in counts.items() if count]
        minimal_counts = {
            str(size): sum(mask.bit_count() == size for mask in minimal)
            for size in sorted({mask.bit_count() for mask in minimal})
        }
        hit_hex = bitset_hex(hit)
        target_rows.append({
            "target_subgroup_index": target_index,
            "target_subgroup_order": len(target),
            "minimum_first_passage_time": min(nonzero),
            "maximum_first_passage_time": max(nonzero),
            "minimal_hitting_support_masks": minimal,
            "minimal_hitting_support_count_by_cardinality": minimal_counts,
            "subset_hit_bitset_hex": hit_hex,
            "subset_hit_bitset_sha256": digest(bytes.fromhex(hit_hex)),
            "subset_hit_count_by_cardinality": hit_counts,
            "subset_nonhit_count_by_cardinality": nonhit_counts,
            "subset_hit_probability_by_cardinality": {
                str(time): rational(Fraction(hit_counts[str(time)], comb(LABEL_COUNT, time)))
                for time in range(LABEL_COUNT + 1)
            },
            "subset_survival_probability_by_cardinality": {
                str(time): rational(Fraction(nonhit_counts[str(time)], comb(LABEL_COUNT, time)))
                for time in range(LABEL_COUNT + 1)
            },
            "pivotal_edge_count_by_cardinality": pivotal_edges,
            "pivotal_pattern_counts": dict(sorted(pivotal_patterns.items(), key=lambda item: tuple(map(int, item[0].split(","))))),
            "permutation_count_by_first_passage_time": counts,
            "probability_by_first_passage_time": probabilities,
            "survival_permutation_count_after_time": {
                str(time): nonhit_counts[str(time)] * factorial(time) * factorial(LABEL_COUNT - time)
                for time in range(LABEL_COUNT + 1)
            },
            "expected_first_passage_time": rational(expectation),
        })

    covers = [
        [lower, upper]
        for lower in range(20)
        for upper in range(20)
        if lower != upper and inclusion[lower][upper]
        and not any(
            middle not in (lower, upper)
            and inclusion[lower][middle] and inclusion[middle][upper]
            for middle in range(20)
        )
    ]
    pairs = []
    for lower in range(20):
        for upper in range(20):
            if inclusion[lower][upper]:
                assert all(not hit_tables[upper][support] or hit_tables[lower][support] for support in range(SUPPORT_COUNT))
                assert expectations[lower] <= expectations[upper]
                pairs.append({
                    "lower_subgroup_index": lower,
                    "upper_subgroup_index": upper,
                    "subsetwise_first_passage_order": True,
                    "cdf_order_all_times": True,
                    "survival_order_all_times": True,
                    "expectation_order": True,
                })
    assert len(pairs) == 102

    top = target_rows[19]
    reference = c83["assembly_atlas"]
    top_checks = {
        "subset_hit_counts": {key: value for key, value in top["subset_hit_count_by_cardinality"].items() if value}
        == reference["full_support_count_by_cardinality"],
        "pivotal_edge_counts": {key: value for key, value in top["pivotal_edge_count_by_cardinality"].items() if value}
        == reference["pivotal_support_count_by_cardinality"],
        "pivotal_patterns": top["pivotal_pattern_counts"] == reference["pivotal_pattern_counts"],
        "permutation_counts": top["permutation_count_by_first_passage_time"] == reference["permutation_count_by_stopping_time"],
        "probabilities": top["probability_by_first_passage_time"] == reference["probability_by_stopping_time"],
        "survival_counts": top["survival_permutation_count_after_time"] == reference["survival_permutation_counts"],
        "expectation": top["expected_first_passage_time"] == reference["expected_stopping_time"],
        "total_permutations": TOTAL == reference["total_permutations"],
    }
    assert all(top_checks.values())
    expected = {
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
            "subgroup_count": 20,
            "total_permutations": TOTAL,
            "target_subgroup_indices": list(range(20)),
            "target_subgroup_orders": [len(subgroup) for subgroup in subgroups],
            "coordinate_sha256": c75["named_coordinate_source"]["coordinate_sha256"],
        },
        "first_passage_atlas": {"target_rows": target_rows},
        "target_poset": {
            "inclusion_matrix": inclusion,
            "cover_relations": covers,
            "comparable_ordered_pair_count_including_reflexive": len(pairs),
            "monotonicity_pairs": pairs,
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
    return expected, {"minimal_support_counts": [len(row["minimal_hitting_support_masks"]) for row in target_rows]}


def validate_evidence_path(path: Path, expected: dict[str, Any]) -> None:
    raw = path.read_bytes()
    observed = json.loads(raw)
    assert raw == canonical(observed)
    assert observed == expected


def main() -> None:
    expected, diagnostics = build_expected()
    validate_evidence_path(EVIDENCE, expected)
    print(json.dumps({
        "status": "C88_INDEPENDENT_CHECK_PASS",
        "target_count": len(expected["first_passage_atlas"]["target_rows"]),
        "minimal_support_counts": diagnostics["minimal_support_counts"],
        "evidence_sha256": digest(EVIDENCE.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
