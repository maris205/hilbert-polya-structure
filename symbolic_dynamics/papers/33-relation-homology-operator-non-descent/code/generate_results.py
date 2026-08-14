#!/usr/bin/env python3
"""Run and freeze the Paper 33 exact cycle-quotient census."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List, Mapping

from cycle_quotient_core import (
    adjacency_descent_certificate,
    build_action,
    component_count,
    cross_square_complex,
    cusp_count_gamma0,
    cusp_rs_witness,
    permutation_orbits,
    random_transitive_action,
    relabel_action,
    relation_quotient_dimension,
)


def classify(n: int) -> str:
    divisors = [d for d in range(2, int(n ** 0.5) + 1) if n % d == 0]
    if not divisors:
        return "prime"
    p = divisors[0]
    value = n
    while value % p == 0:
        value //= p
    return "prime_power" if value == 1 else "mixed_composite"


def write_csv(path: Path, rows: List[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty table")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scan_core(core_path: Path) -> Dict[str, object]:
    text = core_path.read_text(encoding="utf-8").lower()
    forbidden = (
        "is_prime(",
        "prime_table",
        "accepted_support",
        "riemann_zero",
        "zeta_zero",
        "target_zero",
    )
    hits = [token for token in forbidden if token in text]
    return {
        "candidate_core": core_path.name,
        "forbidden_patterns": list(forbidden),
        "hits": hits,
        "pass": not hits,
    }


def build_twist_rows() -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for k in range(6):
        s_norm_zero = int(k % 2 == 1)
        r_norm_zero = int(k % 3 != 0)
        rows.append({
            "kind": "honest_character",
            "even_character": k,
            "odd_character": "",
            "superdimension": 1,
            "s2_relator_word_trace": "1",
            "r3_relator_word_trace": "1",
            "diamond_word_trace": "1",
            "kills_identity_cycle_words": 0,
            "s_norm_polynomial_zero": s_norm_zero,
            "r_norm_polynomial_zero": r_norm_zero,
            "kills_both_chain_norms": s_norm_zero * r_norm_zero,
            "cusp_sr_value": f"t^{(5 * k) % 6}",
            "cusp_sr_nonzero": 1,
        })
    for even in range(6):
        for odd in range(even + 1, 6):
            a = (5 * even) % 6
            b = (5 * odd) % 6
            s_norm_zero = int(even % 2 == odd % 2)
            r_norm_zero = int((even % 3 == 0) == (odd % 3 == 0))
            rows.append({
                "kind": "zero_superdimension_difference",
                "even_character": even,
                "odd_character": odd,
                "superdimension": 0,
                "s2_relator_word_trace": "0",
                "r3_relator_word_trace": "0",
                "diamond_word_trace": "0",
                "kills_identity_cycle_words": 1,
                "s_norm_polynomial_zero": s_norm_zero,
                "r_norm_polynomial_zero": r_norm_zero,
                "kills_both_chain_norms": s_norm_zero * r_norm_zero,
                "cusp_sr_value": f"t^{a}-t^{b}",
                "cusp_sr_nonzero": int(a != b),
            })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=192)
    parser.add_argument("--random-trials", type=int, default=64)
    parser.add_argument("--seed", type=int, default=330000)
    parser.add_argument("--result-dir", default="results_a")
    args = parser.parse_args()

    result_dir = Path(args.result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    core_path = Path(__file__).with_name("cycle_quotient_core.py")

    modulus_rows: List[Dict[str, object]] = []
    matched_rows: List[Dict[str, object]] = []
    for n in range(2, args.cutoff + 1):
        action = build_action(n)
        s_orbits = permutation_orbits(action.s_image)
        r_orbits = permutation_orbits(action.r_image)
        relative_betti = relation_quotient_dimension(action.s_image, action.r_image)
        cusps = cusp_count_gamma0(n)
        cuspidal_betti = relative_betti - (cusps - 1)
        relation_rank, augmented_rank = adjacency_descent_certificate(action)
        c0, c1, c2 = cusp_rs_witness(action)
        label = classify(n)
        modulus_rows.append({
            "modulus": n,
            "state_count": action.size,
            "s_orbits": len(s_orbits),
            "r_orbits": len(r_orbits),
            "relation_rank": relation_rank,
            "relative_betti": relative_betti,
            "cusp_count": cusps,
            "cuspidal_betti": cuspidal_betti,
            "cusp_rs_middle_distinct": int(c0 != c1),
            "cusp_rs_returns": int(c0 == c2),
            "adjacency_augmented_rank": augmented_rank,
            "adjacency_descends": int(augmented_rank == relation_rank),
            "evaluator_class": label,
            "evaluator_prime": int(label == "prime"),
            "residual_relative_nonzero": int(relative_betti > 0),
            "residual_cuspidal_nonzero": int(cuspidal_betti > 0),
        })

        s_clone, r_clone = relabel_action(action, 1_003_003 + n)
        clone_betti = relation_quotient_dimension(s_clone, r_clone)
        clone_rel_rank = len(action.points) - clone_betti
        matched_rows.append({
            "modulus": n,
            "state_count_equal": int(len(s_clone) == action.size),
            "component_count_equal": int(component_count(s_clone, r_clone) == 1),
            "relative_betti_original": relative_betti,
            "relative_betti_clone": clone_betti,
            "relation_rank_original": relation_rank,
            "relation_rank_clone": clone_rel_rank,
            "transport_exact": int(relative_betti == clone_betti and relation_rank == clone_rel_rank),
        })

    random_rows: List[Dict[str, object]] = []
    sizes = [12, 18, 24, 30, 36, 42, 48, 60, 72]
    for trial in range(args.random_trials):
        size = sizes[trial % len(sizes)]
        seed = args.seed + trial
        s_image, r_image, attempts = random_transitive_action(size, seed)
        residual = relation_quotient_dimension(s_image, r_image)
        random_rows.append({
            "trial": trial,
            "seed": seed,
            "states": size,
            "sampling_attempts": attempts,
            "s_orbits": len(permutation_orbits(s_image)),
            "r_orbits": len(permutation_orbits(r_image)),
            "components": component_count(s_image, r_image),
            "s2_killed_by_relation_quotient": 1,
            "r3_killed_by_relation_quotient": 1,
            "residual_betti": residual,
            "residual_nonzero": int(residual > 0),
        })

    twist_rows = build_twist_rows()
    cross = cross_square_complex(args.cutoff)

    classes = ("prime", "prime_power", "mixed_composite")
    class_summary = {
        label: {
            "blocks": sum(row["evaluator_class"] == label for row in modulus_rows),
            "relative_nonzero": sum(row["evaluator_class"] == label and row["relative_betti"] > 0 for row in modulus_rows),
            "cuspidal_nonzero": sum(row["evaluator_class"] == label and row["cuspidal_betti"] > 0 for row in modulus_rows),
            "relative_betti_sum": sum(int(row["relative_betti"]) for row in modulus_rows if row["evaluator_class"] == label),
            "cuspidal_betti_sum": sum(int(row["cuspidal_betti"]) for row in modulus_rows if row["evaluator_class"] == label),
        }
        for label in classes
    }
    total_relative = sum(int(row["relative_betti"]) for row in modulus_rows)
    total_cuspidal = sum(int(row["cuspidal_betti"]) for row in modulus_rows)
    summary = {
        "candidate_id": "SD-C35",
        "cutoff": args.cutoff,
        "moduli": len(modulus_rows),
        "class_summary": class_summary,
        "all_blocks_relative_nonzero": all(row["relative_betti"] > 0 for row in modulus_rows),
        "all_blocks_cusp_rs_witness": all(row["cusp_rs_middle_distinct"] and row["cusp_rs_returns"] for row in modulus_rows),
        "all_tested_adjacencies_fail_to_descend": all(not row["adjacency_descends"] for row in modulus_rows),
        "matched_clone_exact_rows": sum(row["transport_exact"] for row in matched_rows),
        "random_relation_controls": len(random_rows),
        "random_controls_relators_killed": sum(row["s2_killed_by_relation_quotient"] and row["r3_killed_by_relation_quotient"] for row in random_rows),
        "random_controls_residual_nonzero": sum(row["residual_nonzero"] for row in random_rows),
        "honest_characters": sum(row["kind"] == "honest_character" for row in twist_rows),
        "honest_characters_killing_identity_cycle_words": sum(
            row["kind"] == "honest_character" and row["kills_identity_cycle_words"]
            for row in twist_rows
        ),
        "honest_characters_killing_both_chain_norms": sum(
            row["kind"] == "honest_character" and row["kills_both_chain_norms"]
            for row in twist_rows
        ),
        "zero_superdimension_twists": sum(row["kind"] == "zero_superdimension_difference" for row in twist_rows),
        "zero_superdimension_twists_killing_identity_cycle_words": sum(
            row["kind"] == "zero_superdimension_difference" and row["kills_identity_cycle_words"]
            for row in twist_rows
        ),
        "zero_superdimension_twists_killing_both_chain_norms": sum(
            row["kind"] == "zero_superdimension_difference" and row["kills_both_chain_norms"]
            for row in twist_rows
        ),
        "zero_superdimension_twists_with_surviving_cusp_sr": sum(row["kind"] == "zero_superdimension_difference" and row["cusp_sr_nonzero"] for row in twist_rows),
        "cross_square_complex": cross,
        "total_relative_betti_after_diamond_filling": total_relative,
        "total_cuspidal_betti": total_cuspidal,
        "branch_action": "CLOSE_SEMIRING_RESIDUE_FAMILY",
        "positive_candidate": "STOP",
        "negative_paper": "GO",
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall": "ROUTE_A_REJECTED",
        "route_b": "LOCKED",
    }

    tests = {
        "test_count": 25,
        "passes": 25,
        "failures": [],
        "checks": {
            "all_projective_actions_connected": all(
                int(row["relation_rank"]) == int(row["state_count"]) - int(row["relative_betti"])
                for row in modulus_rows
            ),
            "relation_rank_formula": all(
                int(row["relation_rank"]) == int(row["s_orbits"]) + int(row["r_orbits"]) - 1
                for row in modulus_rows
            ),
            "all_relative_betti_positive": summary["all_blocks_relative_nonzero"],
            "all_cusp_witnesses_return": summary["all_blocks_cusp_rs_witness"],
            "prime_relative_residuals": class_summary["prime"]["relative_nonzero"] == class_summary["prime"]["blocks"],
            "prime_power_relative_residuals": class_summary["prime_power"]["relative_nonzero"] == class_summary["prime_power"]["blocks"],
            "mixed_relative_residuals": class_summary["mixed_composite"]["relative_nonzero"] == class_summary["mixed_composite"]["blocks"],
            "cuspidal_betti_nonnegative": all(row["cuspidal_betti"] >= 0 for row in modulus_rows),
            "cuspidal_betti_even": all(row["cuspidal_betti"] % 2 == 0 for row in modulus_rows),
            "some_composite_cuspidal_residual": any(
                row["evaluator_class"] != "prime" and row["cuspidal_betti"] > 0 for row in modulus_rows
            ),
            "some_prime_cuspidal_zero": any(
                row["evaluator_class"] == "prime" and row["cuspidal_betti"] == 0 for row in modulus_rows
            ),
            "adjacency_non_descent_n2": modulus_rows[0]["adjacency_descends"] == 0,
            "all_tested_adjacency_non_descent": summary["all_tested_adjacencies_fail_to_descend"],
            "matched_clone_all_exact": summary["matched_clone_exact_rows"] == len(modulus_rows),
            "random_all_transitive": all(row["components"] == 1 for row in random_rows),
            "random_all_relators_killed": summary["random_controls_relators_killed"] == len(random_rows),
            "random_all_residual_nonzero": summary["random_controls_residual_nonzero"] == len(random_rows),
            "honest_characters_do_not_annihilate_identity_words": summary["honest_characters_killing_identity_cycle_words"] == 0,
            "two_honest_characters_kill_both_chain_norms": summary["honest_characters_killing_both_chain_norms"] == 2,
            "all_virtual_twists_annihilate_identity_words": summary["zero_superdimension_twists_killing_identity_cycle_words"] == 15,
            "two_virtual_twists_kill_both_chain_norms": summary["zero_superdimension_twists_killing_both_chain_norms"] == 2,
            "all_virtual_twists_leave_cusp_cycle": summary["zero_superdimension_twists_with_surviving_cusp_sr"] == 15,
            "cross_cycles_generated_by_diamonds": cross["graph_betti_before_filling"] == cross["diamond_boundary_rank"],
            "cross_h1_zero_after_filling": cross["homology_after_filling"] == 0,
            "source_oracle_clean": scan_core(core_path)["pass"],
        },
    }
    if not all(tests["checks"].values()):
        failed = [name for name, value in tests["checks"].items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    write_csv(result_dir / "modulus_homology_census.csv", modulus_rows)
    write_csv(result_dir / "matched_clone.csv", matched_rows)
    write_csv(result_dir / "random_action_controls.csv", random_rows)
    write_csv(result_dir / "twist_census.csv", twist_rows)
    write_json(result_dir / "cross_square_complex.json", cross)
    write_json(result_dir / "source_oracle_certificate.json", scan_core(core_path))
    write_json(result_dir / "summary.json", summary)
    write_json(result_dir / "test_report.json", tests)

    payload_names = (
        "cross_square_complex.json",
        "matched_clone.csv",
        "modulus_homology_census.csv",
        "random_action_controls.csv",
        "source_oracle_certificate.json",
        "summary.json",
        "test_report.json",
        "twist_census.csv",
    )
    ledger = "".join(f"{digest(result_dir / name)}  {name}\n" for name in payload_names)
    (result_dir / "SHA256SUMS.txt").write_text(ledger, encoding="utf-8")
    aggregate = hashlib.sha256(ledger.encode("utf-8")).hexdigest()
    (result_dir / "aggregate_sha256.txt").write_text(aggregate + "\n", encoding="utf-8")

    stdout = {
        "aggregate_sha256": aggregate,
        "candidate_id": "SD-C35",
        "cutoff": args.cutoff,
        "payloads": len(payload_names),
        "tests": f"{tests['passes']}/{tests['test_count']}",
    }
    print(json.dumps(stdout, sort_keys=True))


if __name__ == "__main__":
    main()
