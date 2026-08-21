#!/usr/bin/env python3
"""Independent bitset reconstruction and semantic checker for C94."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
EVIDENCE = PROJECT / "results/c94_first_passage_hazard_residual_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
TARGETS = 20
GRID = tuple(range(N + 1))
TOTAL = factorial(N)
AUTHORITY = {
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def q(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def fq(value: dict[str, int]) -> Fraction:
    return Fraction(value["numerator"], value["denominator"])


def source() -> dict[str, Any]:
    evidence_path = C88 / "results/c88_subgroup_first_passage_atlas_evidence.json"
    manifest_path = C88 / "C88_PREFREEZE_MANIFEST.json"
    evidence_raw = evidence_path.read_bytes()
    manifest_raw = manifest_path.read_bytes()
    assert digest(evidence_raw) == AUTHORITY["c88"]
    assert digest(manifest_raw) == AUTHORITY["c88_manifest"]
    c88 = json.loads(evidence_raw)
    manifest = json.loads(manifest_raw)
    assert evidence_raw == canonical(c88)
    assert c88["status"] == "PREFREEZE_G3_PASS"
    assert c88["scope_literal"] == FIREWALL
    assert manifest["scope_literal"] == FIREWALL
    assert manifest["files"]["results/c88_subgroup_first_passage_atlas_evidence.json"] == AUTHORITY["c88"]
    return c88


def counts_from_source(source_row: dict[str, Any]) -> list[int]:
    packed = bytes.fromhex(source_row["subset_hit_bitset_hex"])
    assert len(packed) == (1 << N) // 8
    hit = [bool(packed[s // 8] & (1 << (s % 8))) for s in range(1 << N)]
    counts = [0] * (N + 1)
    counts[0] = TOTAL if hit[0] else 0
    # A pivotal k-support is the last prefix at which the target is first hit.
    for k in range(1, N + 1):
        edges = sum(
            1
            for support, is_hit in enumerate(hit)
            if is_hit
            and support.bit_count() == k
            for label in range(N)
            if support & (1 << label) and not hit[support ^ (1 << label)]
        )
        counts[k] = edges * factorial(k - 1) * factorial(N - k)
    assert sum(counts) == TOTAL
    return counts


def tails(counts: list[int]) -> list[int]:
    return [sum(counts[k + 1 :]) for k in GRID]


def hazard_block(counts: list[int], survival: list[int]) -> dict[str, Any]:
    risk = {str(k): TOTAL if k == 0 else survival[k - 1] for k in GRID}
    hazard: dict[str, dict[str, int] | None] = {}
    transition: dict[str, dict[str, int] | None] = {}
    for k in GRID:
        if risk[str(k)] == 0:
            hazard[str(k)] = None
            transition[str(k)] = None
        else:
            h = Fraction(counts[k], risk[str(k)])
            hazard[str(k)] = q(h)
            transition[str(k)] = q(1 - h)
            assert counts[k] + survival[k] == risk[str(k)]
    return {
        "at_risk_permutation_count_before_step": risk,
        "first_passage_permutation_count_at_step": {str(k): counts[k] for k in GRID},
        "hazard_probability": hazard,
        "survival_transition_probability": transition,
    }


def residual_block(counts: list[int], survival: list[int]) -> list[dict[str, Any]]:
    result = []
    for k in GRID:
        denominator = survival[k]
        survival_grid: dict[str, dict[str, int] | None] = {}
        pmf_grid: dict[str, dict[str, int] | None] = {}
        for r in GRID:
            if denominator == 0 or r > N - k:
                survival_grid[str(r)] = None
                pmf_grid[str(r)] = None
            else:
                survival_grid[str(r)] = q(Fraction(survival[k + r], denominator))
                pmf_grid[str(r)] = q(Fraction(0 if r == 0 else counts[k + r], denominator))
        if denominator == 0:
            mean = second = variance = None
            ids: dict[str, bool | None] = {
                "conditioning_event_nonempty": False,
                "pmf_normalized": None,
                "tail_pmf_difference": None,
                "mean_equals_tail_sum": None,
                "second_moment_equals_weighted_tail_sum": None,
                "variance_nonnegative": None,
            }
        else:
            mean_value = Fraction(sum((t - k) * counts[t] for t in range(k + 1, N + 1)), denominator)
            second_value = Fraction(sum((t - k) ** 2 * counts[t] for t in range(k + 1, N + 1)), denominator)
            variance_value = second_value - mean_value * mean_value
            tail_mean = sum(Fraction(survival[k + r], denominator) for r in range(N - k))
            tail_second = sum((2 * r + 1) * Fraction(survival[k + r], denominator) for r in range(N - k))
            pmf_total = sum(Fraction(counts[k + r], denominator) for r in range(1, N - k + 1))
            tail_difference = all(
                fq(survival_grid[str(r - 1)]) - fq(survival_grid[str(r)]) == fq(pmf_grid[str(r)])
                for r in range(1, N - k + 1)
            )
            mean, second, variance = q(mean_value), q(second_value), q(variance_value)
            ids = {
                "conditioning_event_nonempty": True,
                "pmf_normalized": pmf_total == 1,
                "tail_pmf_difference": tail_difference,
                "mean_equals_tail_sum": mean_value == tail_mean,
                "second_moment_equals_weighted_tail_sum": second_value == tail_second,
                "variance_nonnegative": variance_value >= 0,
            }
            assert all(value is True for value in ids.values())
        result.append({
            "conditioning_step_k": k,
            "conditioning_event": "T>k",
            "conditioning_survival_permutation_count": denominator,
            "residual_variable": "R_k=T-k | T>k",
            "residual_support": list(range(1, N - k + 1)) if denominator else [],
            "conditional_residual_survival_probability_by_r": survival_grid,
            "conditional_residual_probability_mass_by_r": pmf_grid,
            "mean_residual_life": mean,
            "second_residual_moment": second,
            "variance_residual_life": variance,
            "identity_checks": ids,
        })
    return result


def build_expected() -> dict[str, Any]:
    c88 = source()
    rows = []
    for index, source_row in enumerate(c88["first_passage_atlas"]["target_rows"]):
        counts = counts_from_source(source_row)
        source_counts = [int(source_row["permutation_count_by_first_passage_time"][str(k)]) for k in GRID]
        assert counts == source_counts
        survival = tails(counts)
        hazard = hazard_block(counts, survival)
        residual = residual_block(counts, survival)
        identities = {
            "distribution_normalized": sum(counts) == TOTAL,
            "source_c88_distribution_match": counts == source_counts,
            "hazard_risk_recurrence": all(
                hazard["at_risk_permutation_count_before_step"][str(k)] == (TOTAL if k == 0 else survival[k - 1])
                for k in GRID
            ),
            "hazard_survival_recurrence": all(
                hazard["hazard_probability"][str(k)] is None
                or fq(hazard["hazard_probability"][str(k)]) + fq(hazard["survival_transition_probability"][str(k)]) == 1
                for k in GRID
            ),
            "all_residual_rows_bound": all(
                entry["conditioning_survival_permutation_count"] == survival[entry["conditioning_step_k"]]
                for entry in residual
            ),
            "all_defined_residual_identities": all(
                all(value is True for value in entry["identity_checks"].values() if value is not None)
                for entry in residual
                if entry["conditioning_survival_permutation_count"]
            ),
        }
        assert all(identities.values())
        rows.append({
            "target_subgroup_index": index,
            "target_subgroup_order": source_row["target_subgroup_order"],
            "source_c88_row_sha256": digest(canonical(source_row)),
            "permutation_count_by_first_passage_time": {str(k): counts[k] for k in GRID},
            "probability_by_first_passage_time": {str(k): q(Fraction(counts[k], TOTAL)) for k in GRID},
            "survival_permutation_count_after_time": {str(k): survival[k] for k in GRID},
            "hazard_atlas": hazard,
            "residual_life_atlas": residual,
            "identity_checks": identities,
        })
    return {
        "schema_id": "hcs-c94-first-passage-hazard-residual-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "first_passage_time": "T=min{k:H<=Phi(A_k)} for a uniform permutation of the sixteen labels",
            "at_risk_count": "A_k=#{pi:T(pi)>=k}; A_0=16!, A_k=S_{k-1} for k>=1",
            "discrete_hazard": "h_k=P(T=k|T>=k)=N_k/A_k, with undefined hazard when A_k=0",
            "survival_transition": "1-h_k=P(T>k|T>=k)=S_k/A_k",
            "residual_condition": "R_k=T-k conditioned on S_k={T>k}",
            "residual_survival": "P(R_k>r|T>k)=P(T>k+r)/P(T>k)=S_{k+r}/S_k",
            "residual_pmf": "P(R_k=r|T>k)=N_{k+r}/S_k for 1<=r<=16-k",
            "residual_mean": "m_k=sum_{r>=0}P(R_k>r|T>k)",
            "residual_second_moment": "q_k=sum_{r>=0}(2r+1)P(R_k>r|T>k)",
            "residual_variance": "v_k=q_k-m_k^2",
            "undefined_conditioning": "A null grid is emitted when S_k=0; no conditional probability is asserted.",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": N,
            "target_subgroup_count": TARGETS,
            "support_count": 1 << N,
            "total_permutations": TOTAL,
            "hazard_step_grid": list(GRID),
            "residual_k_grid": list(GRID),
            "residual_r_grid": list(GRID),
            "source_c88_evidence_sha256": AUTHORITY["c88"],
        },
        "hazard_residual_atlas": {"target_rows": rows},
        "checks": {
            "all_20_targets": True,
            "all_340_hazard_steps": True,
            "all_5780_residual_survival_grid_cells": True,
            "all_5780_residual_pmf_grid_cells": True,
            "all_defined_mean_variance_rows": True,
            "all_hazard_risk_and_survival_recursions": True,
            "all_residual_tail_identities": True,
            "all_c88_distributions_recovered": True,
        },
        "claims": {
            "exact_finite_hazard_and_residual_laws": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }


def main() -> None:
    expected = build_expected()
    observed_raw = EVIDENCE.read_bytes()
    observed = json.loads(observed_raw)
    assert observed_raw == canonical(observed)
    assert observed == expected
    print(json.dumps({
        "status": "C94_INDEPENDENT_CHECK_PASS",
        "target_count": TARGETS,
        "hazard_steps": TARGETS * (N + 1),
        "residual_grid_cells": TARGETS * (N + 1) ** 2,
        "evidence_sha256": digest(observed_raw),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
