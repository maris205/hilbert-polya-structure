#!/usr/bin/env python3
r"""Produce the exact C91 race/tie atlas from the frozen C88 receipt.

For an unordered incomparable pair (i,j), a boundary edge S\{x}->S of
cardinality k contributes to the race when the corresponding first-passage
indicator changes on that edge.  The edge represents
(k-1)!(16-k)! permutations, so all reported values are exact counts.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c91_first_passage_race_atlas_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABEL_COUNT = 16
SUPPORT_COUNT = 1 << LABEL_COUNT
TOTAL_PERMUTATIONS = factorial(LABEL_COUNT)
FULL_LABEL_MASK = SUPPORT_COUNT - 1

SOURCE_DIRS = {
    "c75": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift",
    "c83": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time",
    "c85": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_threshold_vector_poset_rigidity",
    "c88": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas",
}
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c83": "033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28",
    "c83_manifest": "981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85",
    "c85": "22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152",
    "c85_manifest": "d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261",
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def source_paths() -> dict[str, Path]:
    return {
        "c75": SOURCE_DIRS["c75"] / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": SOURCE_DIRS["c75"] / "C75_PREFREEZE_MANIFEST.json",
        "c83": SOURCE_DIRS["c83"] / "results/c83_random_order_stopping_time_evidence.json",
        "c83_manifest": SOURCE_DIRS["c83"] / "C83_PREFREEZE_MANIFEST.json",
        "c85": SOURCE_DIRS["c85"] / "results/c85_threshold_vector_poset_rigidity_evidence.json",
        "c85_manifest": SOURCE_DIRS["c85"] / "C85_PREFREEZE_MANIFEST.json",
        "c88": SOURCE_DIRS["c88"] / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": SOURCE_DIRS["c88"] / "C88_PREFREEZE_MANIFEST.json",
    }


def parse_hit_bitset(raw_hex: str) -> list[bool]:
    raw = bytes.fromhex(raw_hex)
    assert len(raw) == SUPPORT_COUNT // 8
    return [bool(raw[mask // 8] & (1 << (mask % 8))) for mask in range(SUPPORT_COUNT)]


def main() -> None:
    paths = source_paths()
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c75, c83, c85, c88 = (json.loads(raw[name]) for name in ("c75", "c83", "c85", "c88"))
    assert c75["status"] == c83["status"] == c85["status"] == c88["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == c83["scope_literal"] == c85["scope_literal"] == c88["scope_literal"] == FIREWALL
    assert c88["authority"]["c75"] == AUTHORITY["c75"]
    assert c88["authority"]["c83"] == AUTHORITY["c83"]
    assert c88["authority"]["c85"] == AUTHORITY["c85"]
    assert raw["c75"] == canonical(c75)
    assert raw["c83"] == canonical(c83)
    assert raw["c85"] == canonical(c85)
    assert raw["c88"] == canonical(c88)

    rows = c88["first_passage_atlas"]["target_rows"]
    assert len(rows) == 20
    hit = [parse_hit_bitset(row["subset_hit_bitset_hex"]) for row in rows]
    # A rise mask stores all labels x that are pivotal on S\{x}->S.
    rise: list[list[int]] = []
    for target in range(20):
        target_rise = [0] * SUPPORT_COUNT
        for support in range(1, SUPPORT_COUNT):
            labels = 0
            value = hit[target][support]
            if value:
                remaining = support
                while remaining:
                    bit = remaining & -remaining
                    remaining ^= bit
                    if not hit[target][support ^ bit]:
                        labels |= bit
            target_rise[support] = labels
        rise.append(target_rise)

    inclusion = c88["target_poset"]["inclusion_matrix"]
    pairs = [
        (left, right)
        for left in range(20)
        for right in range(left + 1, 20)
        if not inclusion[left][right] and not inclusion[right][left]
    ]
    assert len(pairs) == 108

    pair_rows: list[dict[str, Any]] = []
    for left, right in pairs:
        # outcome order: left_first, tie, right_first
        outcome = [0, 0, 0]
        outcome_by_time = [[0, 0, 0] for _ in range(LABEL_COUNT + 1)]
        edge_by_time = [[0, 0, 0] for _ in range(LABEL_COUNT + 1)]
        for support in range(1, SUPPORT_COUNT):
            k = support.bit_count()
            left_rise = rise[left][support]
            right_rise = rise[right][support]
            left_first_edges = left_rise.bit_count() if not hit[right][support] else 0
            right_first_edges = right_rise.bit_count() if not hit[left][support] else 0
            tie_edges = (left_rise & right_rise).bit_count()
            edge_counts = [left_first_edges, tie_edges, right_first_edges]
            weight = factorial(k - 1) * factorial(LABEL_COUNT - k)
            for index, count in enumerate(edge_counts):
                edge_by_time[k][index] += count
                outcome_by_time[k][index] += count * weight
                outcome[index] += count * weight
        assert sum(outcome) == TOTAL_PERMUTATIONS
        assert all(sum(cell) == TOTAL_PERMUTATIONS for cell in outcome_by_time) is False
        assert sum(sum(cell) for cell in outcome_by_time) == TOTAL_PERMUTATIONS
        assert all(sum(cell) <= TOTAL_PERMUTATIONS for cell in outcome_by_time)
        probabilities = [rational(Fraction(value, TOTAL_PERMUTATIONS)) for value in outcome]
        outcome_by_time_dict = {
            str(time): {
                "left_first": outcome_by_time[time][0],
                "tie": outcome_by_time[time][1],
                "right_first": outcome_by_time[time][2],
            }
            for time in range(LABEL_COUNT + 1)
        }
        edge_by_time_dict = {
            str(time): {
                "left_first": edge_by_time[time][0],
                "tie": edge_by_time[time][1],
                "right_first": edge_by_time[time][2],
            }
            for time in range(LABEL_COUNT + 1)
        }
        pair_rows.append({
            "left_target_index": left,
            "right_target_index": right,
            "left_target_order": rows[left]["target_subgroup_order"],
            "right_target_order": rows[right]["target_subgroup_order"],
            "incomparable": True,
            "outcome_order": ["left_first", "tie", "right_first"],
            "outcome_permutation_count": {
                "left_first": outcome[0],
                "tie": outcome[1],
                "right_first": outcome[2],
            },
            "outcome_probability": {
                "left_first": probabilities[0],
                "tie": probabilities[1],
                "right_first": probabilities[2],
            },
            "outcome_permutation_count_by_first_passage_time": outcome_by_time_dict,
            "boundary_edge_count_by_first_passage_time": edge_by_time_dict,
            "winner_count_identity": {
                "left_first_plus_tie_plus_right_first": sum(outcome),
                "total_permutations": TOTAL_PERMUTATIONS,
            },
            "tie_nonzero": outcome[1] > 0,
        })

    tie_nonzero = sum(row["tie_nonzero"] for row in pair_rows)
    left_wins = sum(row["outcome_permutation_count"]["left_first"] for row in pair_rows)
    right_wins = sum(row["outcome_permutation_count"]["right_first"] for row in pair_rows)
    ties = sum(row["outcome_permutation_count"]["tie"] for row in pair_rows)
    result: dict[str, Any] = {
        "schema_id": "hcs-c91-first-passage-race-atlas-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_object": "uniform permutation of the sixteen C75 named labels",
            "target_times": "T_i=min{k:H_i<=Phi(A_k)} from the frozen C88 hit bitsets",
            "pair_scope": "all unordered pairs of distinct C88 targets incomparable in the C88 subgroup poset",
            "left_first": "T_left<T_right",
            "right_first": "T_right<T_left",
            "tie": "T_left=T_right",
            "boundary_edge": "S\\{x}->S with |S|=k and x the final label",
            "edge_weight": "(k-1)!(16-k)!",
            "race_formula": "left_first edges are left pivots with right not hit on S; right_first symmetrically; tie edges are simultaneous pivots",
            "time_convention": "time zero is included as an explicit zero cell for every incomparable pair",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": LABEL_COUNT,
            "support_count": SUPPORT_COUNT,
            "subgroup_count": 20,
            "total_permutations": TOTAL_PERMUTATIONS,
            "incomparable_pair_count": len(pair_rows),
            "coordinate_sha256": c88["source_model"]["coordinate_sha256"],
            "target_subgroup_orders": c88["source_model"]["target_subgroup_orders"],
        },
        "race_atlas": {
            "pair_rows": pair_rows,
            "aggregate_outcome_permutation_count": {
                "left_first": left_wins,
                "tie": ties,
                "right_first": right_wins,
            },
            "pairs_with_nonzero_ties": tie_nonzero,
        },
        "checks": {
            "all_65536_supports_decoded_for_each_target": True,
            "all_108_unordered_incomparable_pairs_enumerated": True,
            "all_pair_outcomes_partition_16_factorial_permutations": True,
            "all_time_rows_use_boundary_factorial_weights": True,
            "all_probability_rows_normalized": True,
            "all_tie_rows_are_simultaneous_first_hits": True,
            "c88_authority_chain_rebound": True,
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
        "pair_count": len(pair_rows),
        "pairs_with_nonzero_ties": tie_nonzero,
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
