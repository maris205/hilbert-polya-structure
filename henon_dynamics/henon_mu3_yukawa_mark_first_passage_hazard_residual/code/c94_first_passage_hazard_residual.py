#!/usr/bin/env python3
"""Produce exact first-passage hazards and conditional residual-life laws for C94.

The only scientific input is the frozen C88 receipt and its prefreeze manifest.
All arithmetic in the derived atlas is integer or ``Fraction`` arithmetic.
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
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
OUT = PROJECT / "results/c94_first_passage_hazard_residual_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABEL_COUNT = 16
TARGET_COUNT = 20
GRID = tuple(range(LABEL_COUNT + 1))
TOTAL = factorial(LABEL_COUNT)
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


def source_paths() -> dict[str, Path]:
    return {
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
    }


def load_c88() -> tuple[dict[str, Any], dict[str, bytes]]:
    paths = source_paths()
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(data) for name, data in raw.items()} == AUTHORITY
    c88 = json.loads(raw["c88"])
    assert raw["c88"] == canonical(c88)
    manifest = json.loads(raw["c88_manifest"])
    assert c88["status"] == "PREFREEZE_G3_PASS"
    assert c88["scope_literal"] == FIREWALL
    assert manifest["status"] == "PREFREEZE_COMPLETE_NOT_RELEASED"
    assert manifest["scope_literal"] == FIREWALL
    assert manifest["files"]["results/c88_subgroup_first_passage_atlas_evidence.json"] == AUTHORITY["c88"]
    assert c88["source_model"]["label_count"] == LABEL_COUNT
    assert c88["source_model"]["subgroup_count"] == TARGET_COUNT
    return c88, raw


def unpack_hit(source: dict[str, Any]) -> list[bool]:
    packed = bytes.fromhex(source["subset_hit_bitset_hex"])
    assert len(packed) == (1 << LABEL_COUNT) // 8
    return [bool(packed[support // 8] & (1 << (support % 8))) for support in range(1 << LABEL_COUNT)]


def counts_from_hit(hit: list[bool]) -> list[int]:
    """Recover permutation counts from the C88 monotone hit bitset."""
    counts = [0] * (LABEL_COUNT + 1)
    counts[0] = TOTAL if hit[0] else 0
    for time in range(1, LABEL_COUNT + 1):
        pivotal_edges = 0
        for support, value in enumerate(hit):
            if not value or support.bit_count() != time:
                continue
            for label in range(LABEL_COUNT):
                if support & (1 << label) and not hit[support ^ (1 << label)]:
                    pivotal_edges += 1
        counts[time] = pivotal_edges * factorial(time - 1) * factorial(LABEL_COUNT - time)
    assert sum(counts) == TOTAL
    return counts


def survival_counts(counts: list[int]) -> list[int]:
    return [sum(counts[time + 1 :]) for time in GRID]


def make_hazard(counts: list[int], survival: list[int]) -> dict[str, Any]:
    at_risk: dict[str, int] = {}
    first_passage: dict[str, int] = {}
    hazard: dict[str, dict[str, int] | None] = {}
    complement: dict[str, dict[str, int] | None] = {}
    for step in GRID:
        risk = TOTAL if step == 0 else survival[step - 1]
        at_risk[str(step)] = risk
        first_passage[str(step)] = counts[step]
        if risk == 0:
            hazard[str(step)] = None
            complement[str(step)] = None
        else:
            value = Fraction(counts[step], risk)
            hazard[str(step)] = rational(value)
            complement[str(step)] = rational(Fraction(1) - value)
            assert counts[step] + survival[step] == risk
    return {
        "at_risk_permutation_count_before_step": at_risk,
        "first_passage_permutation_count_at_step": first_passage,
        "hazard_probability": hazard,
        "survival_transition_probability": complement,
    }


def make_residual(counts: list[int], survival: list[int]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for k in GRID:
        denominator = survival[k]
        survival_grid: dict[str, dict[str, int] | None] = {}
        pmf_grid: dict[str, dict[str, int] | None] = {}
        for residual in GRID:
            valid = residual <= LABEL_COUNT - k
            if denominator == 0 or not valid:
                survival_grid[str(residual)] = None
                pmf_grid[str(residual)] = None
                continue
            # R_k=T-k conditioned on T>k.  Thus P(R_k>r)=S_{k+r}/S_k.
            survival_grid[str(residual)] = rational(Fraction(survival[k + residual], denominator))
            mass = 0 if residual == 0 else counts[k + residual]
            pmf_grid[str(residual)] = rational(Fraction(mass, denominator))

        if denominator == 0:
            mean = second = variance = None
            identities = {
                "conditioning_event_nonempty": False,
                "pmf_normalized": None,
                "tail_pmf_difference": None,
                "mean_equals_tail_sum": None,
                "second_moment_equals_weighted_tail_sum": None,
                "variance_nonnegative": None,
            }
        else:
            mean_value = Fraction(sum((time - k) * counts[time] for time in range(k + 1, LABEL_COUNT + 1)), denominator)
            second_value = Fraction(sum((time - k) ** 2 * counts[time] for time in range(k + 1, LABEL_COUNT + 1)), denominator)
            variance_value = second_value - mean_value * mean_value
            tail_mean = sum(
                Fraction(survival[k + residual], denominator)
                for residual in range(LABEL_COUNT - k)
            )
            tail_second = sum(
                (2 * residual + 1) * Fraction(survival[k + residual], denominator)
                for residual in range(LABEL_COUNT - k)
            )
            pmf_total = sum(
                Fraction(counts[k + residual], denominator)
                for residual in range(1, LABEL_COUNT - k + 1)
            )
            tail_difference = all(
                survival_grid[str(residual - 1)]
                and survival_grid[str(residual)]
                and Fraction(
                    survival_grid[str(residual - 1)]["numerator"],
                    survival_grid[str(residual - 1)]["denominator"],
                ) - Fraction(
                    survival_grid[str(residual)]["numerator"],
                    survival_grid[str(residual)]["denominator"],
                ) == Fraction(
                    pmf_grid[str(residual)]["numerator"],
                    pmf_grid[str(residual)]["denominator"],
                )
                for residual in range(1, LABEL_COUNT - k + 1)
            )
            mean = rational(mean_value)
            second = rational(second_value)
            variance = rational(variance_value)
            identities = {
                "conditioning_event_nonempty": True,
                "pmf_normalized": pmf_total == 1,
                "tail_pmf_difference": tail_difference,
                "mean_equals_tail_sum": mean_value == tail_mean,
                "second_moment_equals_weighted_tail_sum": second_value == tail_second,
                "variance_nonnegative": variance_value >= 0,
            }
            assert all(identities.values())
        rows.append({
            "conditioning_step_k": k,
            "conditioning_event": "T>k",
            "conditioning_survival_permutation_count": denominator,
            "residual_variable": "R_k=T-k | T>k",
            "residual_support": list(range(1, LABEL_COUNT - k + 1)) if denominator else [],
            "conditional_residual_survival_probability_by_r": survival_grid,
            "conditional_residual_probability_mass_by_r": pmf_grid,
            "mean_residual_life": mean,
            "second_residual_moment": second,
            "variance_residual_life": variance,
            "identity_checks": identities,
        })
    return rows


def build_result(c88: dict[str, Any], raw: dict[str, bytes]) -> dict[str, Any]:
    target_rows: list[dict[str, Any]] = []
    for index, source in enumerate(c88["first_passage_atlas"]["target_rows"]):
        assert source["target_subgroup_index"] == index
        hit = unpack_hit(source)
        counts = counts_from_hit(hit)
        source_counts = [int(source["permutation_count_by_first_passage_time"][str(time)]) for time in GRID]
        assert counts == source_counts
        survival = survival_counts(counts)
        hazard = make_hazard(counts, survival)
        residual = make_residual(counts, survival)
        row = {
            "target_subgroup_index": index,
            "target_subgroup_order": source["target_subgroup_order"],
            "source_c88_row_sha256": digest(canonical(source)),
            "permutation_count_by_first_passage_time": {str(time): counts[time] for time in GRID},
            "probability_by_first_passage_time": {str(time): rational(Fraction(counts[time], TOTAL)) for time in GRID},
            "survival_permutation_count_after_time": {str(time): survival[time] for time in GRID},
            "hazard_atlas": hazard,
            "residual_life_atlas": residual,
        }
        hazard_ok = all(
            hazard["at_risk_permutation_count_before_step"][str(step)]
            == (TOTAL if step == 0 else survival[step - 1])
            for step in GRID
        )
        residual_ok = all(
            (entry["conditioning_survival_permutation_count"] == survival[entry["conditioning_step_k"]])
            for entry in residual
        )
        row["identity_checks"] = {
            "distribution_normalized": sum(counts) == TOTAL,
            "source_c88_distribution_match": counts == source_counts,
            "hazard_risk_recurrence": hazard_ok,
            "hazard_survival_recurrence": all(
                hazard["hazard_probability"][str(step)] is None
                or Fraction(
                    hazard["hazard_probability"][str(step)]["numerator"],
                    hazard["hazard_probability"][str(step)]["denominator"],
                )
                + Fraction(
                    hazard["survival_transition_probability"][str(step)]["numerator"],
                    hazard["survival_transition_probability"][str(step)]["denominator"],
                )
                == 1
                for step in GRID
            ),
            "all_residual_rows_bound": residual_ok,
            "all_defined_residual_identities": all(
                all(value is True for value in entry["identity_checks"].values() if value is not None)
                for entry in residual
                if entry["conditioning_survival_permutation_count"]
            ),
        }
        assert all(row["identity_checks"].values())
        target_rows.append(row)

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
            "label_count": LABEL_COUNT,
            "target_subgroup_count": TARGET_COUNT,
            "support_count": 1 << LABEL_COUNT,
            "total_permutations": TOTAL,
            "hazard_step_grid": list(GRID),
            "residual_k_grid": list(GRID),
            "residual_r_grid": list(GRID),
            "source_c88_evidence_sha256": AUTHORITY["c88"],
        },
        "hazard_residual_atlas": {"target_rows": target_rows},
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
    c88, raw = load_c88()
    result = build_result(c88, raw)
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "target_count": TARGET_COUNT,
        "hazard_steps": TARGET_COUNT * (LABEL_COUNT + 1),
        "residual_grid_cells": TARGET_COUNT * (LABEL_COUNT + 1) ** 2,
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
