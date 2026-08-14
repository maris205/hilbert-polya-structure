#!/usr/bin/env python3
"""Independent serialized-artifact evaluator for SD-C32.

This module imports neither coherence_core nor generate_results.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


def read(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def rational(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def gamma_length(value: int) -> int:
    return 2 * (value.bit_length() - 1) + 1


class Audit:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        self.rows.append({"name": name, "pass": bool(condition), "detail": detail})

    def result(self) -> dict[str, object]:
        failures = [row for row in self.rows if not row["pass"]]
        return {
            "schema_version": "SD-C32-independent-evaluation-v1",
            "candidate_id": "SD-C32",
            "independent_of_candidate_core": True,
            "check_count": len(self.rows),
            "pass_count": len(self.rows) - len(failures),
            "failure_count": len(failures),
            "all_pass": not failures,
            "failures": failures,
            "checks": self.rows,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        }


def evaluate(results: Path) -> dict[str, object]:
    audit = Audit()
    sanity = read(results / "sanity.json")
    baseline = read(results / "baseline.json")
    finite = read(results / "finite_controls.json")
    free = read(results / "free_monoid_controls.json")
    clone = read(results / "clone_certificate.json")
    masks = read(results / "predicate_masks.json")
    analytic = read(results / "analytic_ownership.json")
    summary = read(results / "summary.json")

    payloads = {
        "sanity": sanity,
        "baseline": baseline,
        "finite": finite,
        "free": free,
        "clone": clone,
        "masks": masks,
        "analytic": analytic,
        "summary": summary,
    }
    for name, payload in payloads.items():
        audit.check(f"{name}:schema", payload["schema_version"] == "SD-C32-exact-v1")
        audit.check(f"{name}:candidate", payload["candidate_id"] == "SD-C32")
        audit.check(f"{name}:no_target_zeros", payload["target_zero_data_used"] is False)
        audit.check(f"{name}:route_b_false", payload["route_b_invocation_allowed"] is False)

    expected = {
        12: ([2, 3, 5, 7, 11], 10, 10),
        18: ([2, 3, 5, 7, 11, 13, 17], 21, 35),
        30: ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 45, 120),
    }
    previous_weights: set[int] = set()
    for cutoff, record in zip((12, 18, 30), baseline["records"]):
        weights = [int(value) for value in record["atom_weights"]]
        expected_weights, pair_count, triple_count = expected[cutoff]
        audit.check(f"baseline:{cutoff}:weights", weights == expected_weights)
        audit.check(f"baseline:{cutoff}:nested", previous_weights.issubset(weights))
        audit.check(f"baseline:{cutoff}:pair_count", len(record["pair_rows"]) == pair_count)
        audit.check(f"baseline:{cutoff}:triple_count", len(record["triple_rows"]) == triple_count)
        audit.check(f"baseline:{cutoff}:qualified_pairs", record["qualified_pairs"] == pair_count)
        audit.check(f"baseline:{cutoff}:qualified_triples", record["qualified_triples"] == triple_count)
        gram: dict[tuple[int, int], Fraction] = {}
        e2 = Fraction(0)
        for row in record["pair_rows"]:
            p, q = map(int, row["atom_weights"])
            g = Fraction(1, (p**4 + 1) * (q**4 + 1))
            gram[(p, q)] = g
            audit.check(f"baseline:{cutoff}:pair:{p}:{q}:full", row["coherence"]["full"] is True)
            audit.check(
                f"baseline:{cutoff}:pair:{p}:{q}:predicates",
                all(row["coherence"]["predicates"].values()),
            )
            audit.check(f"baseline:{cutoff}:pair:{p}:{q}:gram", rational(row["gram"]) == g)
            expected_h2 = g * g / (p * q)
            e2 -= expected_h2
            audit.check(f"baseline:{cutoff}:pair:{p}:{q}:H2", rational(row["H_squared"]) == expected_h2)
            audit.check(
                f"baseline:{cutoff}:pair:{p}:{q}:marker",
                int(row["marker_exponent"]) == gamma_length(p) + gamma_length(q),
            )
        theta = Fraction(0)
        e3 = Fraction(0)
        for row in record["triple_rows"]:
            p, q, r = map(int, row["atom_weights"])
            expected_coefficient = 2 * gram[(p, q)] * gram[(p, r)] * gram[(q, r)] / (p * q * r)
            theta += expected_coefficient
            e3 += expected_coefficient
            audit.check(f"baseline:{cutoff}:triple:{p}:{q}:{r}:full", row["coherence"]["full"] is True)
            audit.check(
                f"baseline:{cutoff}:triple:{p}:{q}:{r}:connected",
                rational(row["connected_coefficient"]) == expected_coefficient,
            )
            audit.check(
                f"baseline:{cutoff}:triple:{p}:{q}:{r}:e3",
                rational(row["auxiliary_e3_coefficient"]) == expected_coefficient,
            )
            audit.check(
                f"baseline:{cutoff}:triple:{p}:{q}:{r}:marker",
                int(row["marker_exponent"])
                == 2 * (gamma_length(p) + gamma_length(q) + gamma_length(r)),
            )
        audit.check(f"baseline:{cutoff}:e2", rational(record["auxiliary_det_e2"]) == e2)
        audit.check(f"baseline:{cutoff}:theta", rational(record["theta3"]) == theta)
        audit.check(f"baseline:{cutoff}:e3", rational(record["auxiliary_det_e3"]) == e3)
        previous_weights = set(weights)
    audit.check("baseline:relabels", all(baseline["relabel_canonical_equal"]))
    audit.check(
        "baseline:prefix",
        all(row["canonical_prefix_equal"] for row in baseline["active_cutoff_prefix_checks"]),
    )

    expected_control_counts = {
        "mutated_cover_promote_6": (3, 0),
        "composite_only": (0, 0),
        "seeded_generic_dag_29031": (0, 0),
        "seeded_random_inventory_29032": (0, 0),
    }
    for record in finite["records"]:
        pair_expected, triple_expected = expected_control_counts[record["source"]]
        audit.check(
            f"control:{record['source']}:pairs",
            int(record["qualified_pairs"]) == pair_expected,
        )
        audit.check(
            f"control:{record['source']}:triples",
            int(record["qualified_triples"]) == triple_expected,
        )
    audit.check(
        "control:minimal_survivors",
        finite["minimal_pair_counterexample"]["surviving_pairs"]
        == [[2, 5], [2, 7], [3, 5]],
    )
    audit.check("control:pair_gate_fails", finite["all_four_pair_zero"] is False)
    audit.check("control:triple_gate_passes", finite["all_four_triple_zero"] is True)
    audit.check("control:compiler_sanity", finite["all_compilers_pass"] is True)
    audit.check("control:relabel", finite["generic_relabel_canonical_equal"] is True)

    audit.check("clone:all_equal", clone["all_clone_ledgers_equal"] is True)
    for index in range(3):
        audit.check(
            f"clone:free:{index}",
            clone["baseline_canonical"][index] == clone["clone_canonical"][index],
        )
        audit.check(
            f"clone:UFD:{index}",
            clone["baseline_canonical"][index]
            == clone["polynomial_UFD_canonical"][index],
        )
    audit.check(
        "clone:minimal_pair",
        clone["minimal_pair_clone"]["integer_atoms"] == [2, 3]
        and clone["minimal_pair_clone"]["mobius"] == 1
        and clone["minimal_pair_clone"]["roof"] == 6,
    )
    audit.check(
        "clone:minimal_triple",
        clone["minimal_triple_clone"]["integer_atoms"] == [2, 3, 5]
        and clone["minimal_triple_clone"]["mobius"] == -1
        and clone["minimal_triple_clone"]["roof"] == 30,
    )
    audit.check(
        "clone:theorem_status",
        clone["theorem_certificate"]["status"] == "PROVES_TOO_MUCH",
    )

    audit.check("free:row_count", len(free["rows"]) == 45)
    aliases = set()
    for row in free["rows"]:
        rank = int(row["rank"])
        cap = int(row["exponent_cap"])
        aliases.add(row["alias"])
        audit.check(
            f"free:{row['name']}:elements",
            int(row["element_count"]) == (cap + 1) ** rank,
        )
        audit.check(
            f"free:{row['name']}:pairs",
            int(row["pair_count"]) == math.comb(rank, 2),
        )
        audit.check(
            f"free:{row['name']}:triples",
            int(row["triple_count"]) == math.comb(rank, 3),
        )
        audit.check(f"free:{row['name']}:pair_coherence", row["all_pairs_fully_coherent"] is True)
        audit.check(f"free:{row['name']}:triple_coherence", row["all_triples_fully_coherent"] is True)
        audit.check(f"free:{row['name']}:cap_compatibility", row["cap_independent_local_intervals"] is True)
    audit.check(
        "free:aliases",
        aliases
        == {
            "free_commutative",
            "polynomial_UFD_monomials",
            "generic_weight_free_commutative",
        },
    )

    audit.check("masks:row_count", len(masks["rows"]) == 186)
    audit.check("masks:no_pair_separator", masks["pair_separator_exists"] is False)
    audit.check("masks:triple_separator", masks["triple_separator_exists"] is True)
    audit.check("masks:clone_copy", masks["every_mask_copied_by_transported_clone"] is True)
    for mask in range(1, 32):
        base = next(
            row
            for row in masks["rows"]
            if row["mask"] == mask and row["source"] == "integer_divisibility_active_30"
        )
        copied = next(
            row
            for row in masks["rows"]
            if row["mask"] == mask and row["source"] == "transported_free_commutative_clone_30"
        )
        audit.check(
            f"masks:{mask}:exact_clone",
            base["qualified_pairs"] == copied["qualified_pairs"]
            and base["qualified_triples"] == copied["qualified_triples"],
        )

    audit.check("analytic:strip", analytic["C2_holomorphic_strip"] == "-3 < Re(s) < 4")
    audit.check("analytic:reflection", analytic["C2_reflection"] == "C2(1-s)=C2(s)")
    for row in analytic["tail_certificates"]:
        cutoff = int(row["cutoff"])
        audit.check(
            f"analytic:{cutoff}:pair_tail",
            rational(row["C2_absolute_tail_bound_over_C_eta"])
            == Fraction(5, 36 * cutoff**3),
        )
        audit.check(
            f"analytic:{cutoff}:triangle_tail",
            rational(row["triangle_absolute_tail_bound_over_C_eta_cubed"])
            == Fraction(25, 16_777_216 * cutoff**8),
        )
    audit.check("analytic:H_trace_class", analytic["auxiliary_H"]["trace_class"] is True)
    audit.check(
        "analytic:H_ownership",
        "not the original" in analytic["auxiliary_H"]["ownership"],
    )
    audit.check(
        "analytic:theta_ownership",
        "not the full" in analytic["connected_theta3"]["ownership"],
    )
    audit.check(
        "analytic:chiral_unchanged",
        analytic["chiral_det3"]["ownership_changed_by_filter"] is False,
    )
    audit.check("analytic:marker_count", analytic["marker_row_count"] == 165)
    for index, row in enumerate(analytic["marker_rows"]):
        weights = [int(value) for value in row["atom_weights"]]
        expected_marker = (
            sum(gamma_length(value) for value in weights)
            if row["kind"] == "pair"
            else 2 * sum(gamma_length(value) for value in weights)
        )
        audit.check(
            f"marker:{index}",
            int(row["marker_exponent"]) == expected_marker and row["theorem_u"] == 1,
        )

    audit.check("summary:pair_fail", summary["finite_pair_separator"] is False)
    audit.check("summary:triple_finite_go", summary["finite_triple_separator"] is True)
    audit.check("summary:UFD_not_zero", summary["all_UFD_controls_zero"] is False)
    audit.check("summary:clone_stop", summary["clone_proves_too_much"] is True)
    audit.check(
        "summary:route",
        summary["route_tuple"]
        == [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
    )
    audit.check("summary:rejected", summary["overall_status"] == "REJECTED_AS_RH_COMPLETION")
    audit.check("sanity:all", sanity["all_pass"] is True)
    return audit.result()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    payload = evaluate(args.results)
    (args.results / "evaluation.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not payload["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
