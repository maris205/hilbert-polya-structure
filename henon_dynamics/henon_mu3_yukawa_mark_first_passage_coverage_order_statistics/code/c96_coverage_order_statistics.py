#!/usr/bin/env python3
"""Produce exact target-coverage order statistics from frozen C88 hit bitsets."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
OUT = PROJECT / "results/c96_coverage_order_statistics_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
M = N + 1
TARGETS = 20
SUPPORTS = 1 << N
TOTAL = factorial(N)
AUTHORITY = {
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def load_source() -> dict[str, Any]:
    paths = {
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
    }
    raw = {key: path.read_bytes() for key, path in paths.items()}
    assert {key: digest(value) for key, value in raw.items()} == AUTHORITY
    c88 = json.loads(raw["c88"])
    assert raw["c88"] == canonical(c88)
    assert c88["status"] == "PREFREEZE_G3_PASS"
    assert c88["scope_literal"] == FIREWALL
    return c88


def unpack(raw_hex: str) -> list[bool]:
    raw = bytes.fromhex(raw_hex)
    assert len(raw) == SUPPORTS // 8
    return [bool(raw[s // 8] & (1 << (s % 8))) for s in range(SUPPORTS)]


def main() -> None:
    c88 = load_source()
    rows = c88["first_passage_atlas"]["target_rows"]
    assert len(rows) == TARGETS
    hits = [unpack(row["subset_hit_bitset_hex"]) for row in rows]
    assert all(hits[0])  # the trivial subgroup target is already hit at time zero
    coverage = [sum(hits[target][support] for target in range(TARGETS)) for support in range(SUPPORTS)]
    assert coverage[0] == 1 and coverage[-1] == TARGETS

    exact_histograms: list[dict[str, int]] = []
    exact_arrays: list[list[int]] = []
    for k in range(M):
        counter = Counter(coverage[s] for s in range(SUPPORTS) if s.bit_count() == k)
        assert sum(counter.values()) == comb(N, k)
        exact_arrays.append([counter[value] for value in range(1, TARGETS + 1)])
        exact_histograms.append({str(value): counter[value] for value in range(1, TARGETS + 1)})

    rank_rows: list[dict[str, Any]] = []
    for rank in range(1, TARGETS + 1):
        reached = [sum(exact_arrays[k][rank - 1:]) for k in range(M)]
        assert reached[-1] == 1
        cdf = [Fraction(reached[k], comb(N, k)) for k in range(M)]
        assert all(cdf[k] <= cdf[k + 1] for k in range(N))
        counts: list[int] = []
        previous = Fraction(0)
        for k in range(M):
            value = int((cdf[k] - previous) * TOTAL)
            assert value >= 0
            counts.append(value)
            previous = cdf[k]
        assert sum(counts) == TOTAL
        boundary_edges = [0] * M
        for support in range(1, SUPPORTS):
            if coverage[support] < rank:
                continue
            k = support.bit_count()
            remaining = support
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                boundary_edges[k] += int(coverage[support ^ bit] < rank)
        completion_weights = [TOTAL] + [factorial(k - 1) * factorial(N - k) for k in range(1, M)]
        support_or_edge_counts = [int(coverage[0] >= rank)] + boundary_edges[1:]
        assert all(support_or_edge_counts[k] * completion_weights[k] == counts[k] for k in range(M))
        probabilities = [Fraction(value, TOTAL) for value in counts]
        raw_moments = {
            str(order): rational(sum((Fraction((k ** order) * counts[k], TOTAL) for k in range(M)), Fraction(0)))
            for order in range(1, 5)
        }
        mean = sum((Fraction(k * counts[k], TOTAL) for k in range(M)), Fraction(0))
        second = sum((Fraction(k * k * counts[k], TOTAL) for k in range(M)), Fraction(0))
        support = [k for k, value in enumerate(counts) if value]
        survival_mean = sum((Fraction(1) - cdf[k] for k in range(N)), Fraction(0))
        assert mean == survival_mean
        rank_rows.append({
            "coverage_rank": rank,
            "order_statistic_definition": f"K_{rank}=min{{k:at least {rank} of 20 C88 targets are hit by the prefix support}}",
            "minimum_time": min(support),
            "maximum_time": max(support),
            "subset_count_reaching_rank_by_prefix_size": {str(k): reached[k] for k in range(M)},
            "cdf_by_prefix_size": {str(k): rational(cdf[k]) for k in range(M)},
            "permutation_count_by_first_reach_time": {str(k): counts[k] for k in range(M)},
            "probability_by_first_reach_time": {str(k): rational(probabilities[k]) for k in range(M)},
            "raw_moments_orders_1_to_4": raw_moments,
            "mean": rational(mean),
            "variance": rational(second - mean * mean),
            "first_reach_support_edge_factorial_certificate": {
                str(k): {
                    "count_kind": "initial_empty_support" if k == 0 else "oriented_boundary_edge",
                    "support_or_edge_count": support_or_edge_counts[k],
                    "completion_factorial_weight": completion_weights[k],
                    "permutation_count": counts[k],
                }
                for k in range(M)
            },
        })

    # For each fixed support, increasing the required number of covered targets
    # delays the first passage.  The distributional CDFs therefore decrease in r.
    for rank in range(TARGETS - 1):
        left = rank_rows[rank]["cdf_by_prefix_size"]
        right = rank_rows[rank + 1]["cdf_by_prefix_size"]
        for k in range(M):
            a = Fraction(left[str(k)]["numerator"], left[str(k)]["denominator"])
            b = Fraction(right[str(k)]["numerator"], right[str(k)]["denominator"])
            assert a >= b

    result: dict[str, Any] = {
        "schema_id": "hcs-c96-first-passage-coverage-order-statistics-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_object": "uniform permutation of the sixteen frozen C88 labels",
            "prefix_support": "A_k is the set of the first k labels",
            "coverage_count": "C(A)=#{i in 0,...,19:H_i is hit by support A}",
            "order_statistic": "K_r=min{k:C(A_k)>=r}, r=1,...,20",
            "cdf_formula": "P(K_r<=k)=#{A:|A|=k,C(A)>=r}/binom(16,k)",
            "pmf_formula": "P(K_r=k)=P(K_r<=k)-P(K_r<=k-1)",
            "factorial_weight": "for k>=1, each oriented first-reach boundary edge has weight (k-1)!(16-k)!; at k=0 the empty support has 16! completions",
            "trivial_target_convention": "target 0 is hit by the empty support, so C(empty)=1 and K_1=0 deterministically",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": N,
            "target_subgroup_count_including_trivial": TARGETS,
            "support_count": SUPPORTS,
            "total_permutations": TOTAL,
            "coverage_rank_range": [1, TARGETS],
        },
        "coverage_atlas": {
            "exact_support_count_by_prefix_size_and_coverage": {str(k): exact_histograms[k] for k in range(M)},
            "rank_rows": rank_rows,
        },
        "checks": {
            "all_65536_supports_decoded_across_20_targets": True,
            "all_17_prefix_cardinality_layers_partitioned": True,
            "all_20_coverage_order_statistics": True,
            "all_20_distributions_normalized_to_16_factorial": True,
            "all_20_boundary_edge_factorial_identities": True,
            "all_20_means_match_survival_sums": True,
            "all_19_rank_monotonicity_relations": True,
            "rank_1_is_zero_due_to_trivial_target": True,
        },
        "claims": {
            "exact_finite_coverage_order_statistics": True,
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
    print(json.dumps({"status": result["status"], "rank_count": len(rank_rows), "support_count": SUPPORTS, "evidence_sha256": digest(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
