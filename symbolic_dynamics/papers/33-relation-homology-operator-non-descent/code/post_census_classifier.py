#!/usr/bin/env python3
"""Append arithmetic labels after Paper 33 source invariants are frozen."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Mapping


PROTOTYPE_CORE_SHA256 = (
    "3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168"
)
PROTOTYPE_RUNNER_SHA256 = (
    "03e840f8941e69220a467fa106a55939529bd1adbe1b2fe2d2e67d2fb1887335"
)
PROTOTYPE_PAYLOAD_AGGREGATE = (
    "c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4"
)
PROTOTYPE_PAYLOADS = (
    "cross_square_complex.json",
    "matched_clone.csv",
    "modulus_homology_census.csv",
    "random_action_controls.csv",
    "source_oracle_certificate.json",
    "summary.json",
    "test_report.json",
    "twist_census.csv",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: List[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty table")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def classify(n: int) -> str:
    divisor = next(
        (d for d in range(2, int(n ** 0.5) + 1) if n % d == 0),
        None,
    )
    if divisor is None:
        return "prime"
    value = n
    while value % divisor == 0:
        value //= divisor
    return "prime_power" if value == 1 else "mixed_composite"


def add_labels(raw_rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    labelled: List[Dict[str, object]] = []
    for raw in raw_rows:
        n = int(raw["modulus"])
        label = classify(n)
        row: Dict[str, object] = dict(raw)
        row.update({
            "evaluator_class": label,
            "evaluator_prime": int(label == "prime"),
            "residual_relative_nonzero": int(
                int(raw["relative_betti"]) > 0
            ),
            "residual_cuspidal_nonzero": int(
                int(raw["cuspidal_betti"]) > 0
            ),
        })
        labelled.append(row)
    return labelled


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default="results")
    args = parser.parse_args()

    result_dir = Path(args.result_dir)
    code_dir = Path(__file__).resolve().parent
    raw_path = result_dir / "modulus_source_census.csv"
    raw_rows = read_csv(raw_path)
    labelled_rows = add_labels(raw_rows)
    write_csv(result_dir / "modulus_homology_census.csv", labelled_rows)

    matched_rows = read_csv(result_dir / "matched_clone.csv")
    random_rows = read_csv(result_dir / "random_action_controls.csv")
    twist_rows = read_csv(result_dir / "twist_census.csv")
    cross = json.loads(
        (result_dir / "cross_square_complex.json").read_text(
            encoding="utf-8"
        )
    )
    source_scan = json.loads(
        (result_dir / "source_oracle_certificate.json").read_text(
            encoding="utf-8"
        )
    )

    classes = ("prime", "prime_power", "mixed_composite")
    class_summary = {
        label: {
            "blocks": sum(
                row["evaluator_class"] == label for row in labelled_rows
            ),
            "relative_nonzero": sum(
                row["evaluator_class"] == label
                and int(row["relative_betti"]) > 0
                for row in labelled_rows
            ),
            "cuspidal_nonzero": sum(
                row["evaluator_class"] == label
                and int(row["cuspidal_betti"]) > 0
                for row in labelled_rows
            ),
            "relative_betti_sum": sum(
                int(row["relative_betti"])
                for row in labelled_rows
                if row["evaluator_class"] == label
            ),
            "cuspidal_betti_sum": sum(
                int(row["cuspidal_betti"])
                for row in labelled_rows
                if row["evaluator_class"] == label
            ),
        }
        for label in classes
    }
    summary = {
        "candidate_id": "SD-C35",
        "cutoff": 192,
        "moduli": len(labelled_rows),
        "class_summary": class_summary,
        "all_blocks_relative_nonzero": all(
            int(row["relative_betti"]) > 0 for row in labelled_rows
        ),
        "all_blocks_cusp_rs_witness": all(
            int(row["cusp_rs_middle_distinct"])
            and int(row["cusp_rs_returns"])
            for row in labelled_rows
        ),
        "all_tested_adjacencies_fail_to_descend": all(
            not int(row["adjacency_descends"])
            for row in labelled_rows
        ),
        "matched_clone_exact_rows": sum(
            int(row["transport_exact"]) for row in matched_rows
        ),
        "random_relation_controls": len(random_rows),
        "random_controls_relators_killed": sum(
            int(row["s2_killed_by_relation_quotient"])
            and int(row["r3_killed_by_relation_quotient"])
            for row in random_rows
        ),
        "random_controls_residual_nonzero": sum(
            int(row["residual_nonzero"]) for row in random_rows
        ),
        "honest_characters": sum(
            row["kind"] == "honest_character" for row in twist_rows
        ),
        "honest_characters_killing_identity_cycle_words": sum(
            row["kind"] == "honest_character"
            and int(row["kills_identity_cycle_words"])
            for row in twist_rows
        ),
        "honest_characters_killing_both_chain_norms": sum(
            row["kind"] == "honest_character"
            and int(row["kills_both_chain_norms"])
            for row in twist_rows
        ),
        "zero_superdimension_twists": sum(
            row["kind"] == "zero_superdimension_difference"
            for row in twist_rows
        ),
        "zero_superdimension_twists_killing_identity_cycle_words": sum(
            row["kind"] == "zero_superdimension_difference"
            and int(row["kills_identity_cycle_words"])
            for row in twist_rows
        ),
        "zero_superdimension_twists_killing_both_chain_norms": sum(
            row["kind"] == "zero_superdimension_difference"
            and int(row["kills_both_chain_norms"])
            for row in twist_rows
        ),
        "zero_superdimension_twists_with_surviving_cusp_sr": sum(
            row["kind"] == "zero_superdimension_difference"
            and int(row["cusp_sr_nonzero"])
            for row in twist_rows
        ),
        "cross_square_complex": cross,
        "total_relative_betti_after_diamond_filling": sum(
            int(row["relative_betti"]) for row in labelled_rows
        ),
        "total_cuspidal_betti": sum(
            int(row["cuspidal_betti"]) for row in labelled_rows
        ),
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
    write_json(result_dir / "summary.json", summary)

    checks = {
        "all_projective_actions_connected": all(
            int(row["relation_rank"])
            == int(row["state_count"]) - int(row["relative_betti"])
            for row in labelled_rows
        ),
        "relation_rank_formula": all(
            int(row["relation_rank"])
            == int(row["s_orbits"]) + int(row["r_orbits"]) - 1
            for row in labelled_rows
        ),
        "all_relative_betti_positive": summary[
            "all_blocks_relative_nonzero"
        ],
        "all_cusp_witnesses_return": summary["all_blocks_cusp_rs_witness"],
        "prime_relative_residuals": class_summary["prime"][
            "relative_nonzero"
        ] == class_summary["prime"]["blocks"],
        "prime_power_relative_residuals": class_summary["prime_power"][
            "relative_nonzero"
        ] == class_summary["prime_power"]["blocks"],
        "mixed_relative_residuals": class_summary["mixed_composite"][
            "relative_nonzero"
        ] == class_summary["mixed_composite"]["blocks"],
        "cuspidal_betti_nonnegative": all(
            int(row["cuspidal_betti"]) >= 0 for row in labelled_rows
        ),
        "cuspidal_betti_even": all(
            int(row["cuspidal_betti"]) % 2 == 0 for row in labelled_rows
        ),
        "some_composite_cuspidal_residual": any(
            row["evaluator_class"] != "prime"
            and int(row["cuspidal_betti"]) > 0
            for row in labelled_rows
        ),
        "some_prime_cuspidal_zero": any(
            row["evaluator_class"] == "prime"
            and int(row["cuspidal_betti"]) == 0
            for row in labelled_rows
        ),
        "adjacency_non_descent_n2": int(
            labelled_rows[0]["adjacency_descends"]
        ) == 0,
        "all_tested_adjacency_non_descent": summary[
            "all_tested_adjacencies_fail_to_descend"
        ],
        "matched_clone_all_exact": summary["matched_clone_exact_rows"]
        == len(labelled_rows),
        "random_all_transitive": all(
            int(row["components"]) == 1 for row in random_rows
        ),
        "random_all_relators_killed": summary[
            "random_controls_relators_killed"
        ] == len(random_rows),
        "random_all_residual_nonzero": summary[
            "random_controls_residual_nonzero"
        ] == len(random_rows),
        "honest_characters_do_not_annihilate_identity_words": summary[
            "honest_characters_killing_identity_cycle_words"
        ] == 0,
        "two_honest_characters_kill_both_chain_norms": summary[
            "honest_characters_killing_both_chain_norms"
        ] == 2,
        "all_virtual_twists_annihilate_identity_words": summary[
            "zero_superdimension_twists_killing_identity_cycle_words"
        ] == 15,
        "two_virtual_twists_kill_both_chain_norms": summary[
            "zero_superdimension_twists_killing_both_chain_norms"
        ] == 2,
        "all_virtual_twists_leave_cusp_cycle": summary[
            "zero_superdimension_twists_with_surviving_cusp_sr"
        ] == 15,
        "cross_cycles_generated_by_diamonds": cross[
            "graph_betti_before_filling"
        ] == cross["diamond_boundary_rank"],
        "cross_h1_zero_after_filling": cross["homology_after_filling"] == 0,
        "source_oracle_clean": source_scan["pass"],
    }
    failures = [name for name, value in checks.items() if not value]
    test_report = {
        "test_count": 25,
        "passes": 25 if not failures else 25 - len(failures),
        "failures": failures,
        "checks": checks,
    }
    if len(checks) != 25:
        raise AssertionError(f"expected 25 checks, got {len(checks)}")
    write_json(result_dir / "test_report.json", test_report)
    if failures:
        raise AssertionError(f"post-census checks failed: {failures}")

    class_counts = {
        label: class_summary[label]["blocks"] for label in classes
    }
    classification_certificate = {
        "candidate_id": "SD-C35",
        "stage": "post_census_arithmetic_labels",
        "classifier": Path(__file__).name,
        "classifier_sha256": digest(Path(__file__).resolve()),
        "raw_census": raw_path.name,
        "raw_census_sha256": digest(raw_path),
        "labelled_census": "modulus_homology_census.csv",
        "labelled_census_sha256": digest(
            result_dir / "modulus_homology_census.csv"
        ),
        "rows": len(labelled_rows),
        "class_counts": class_counts,
        "source_columns_preserved": all(
            all(str(labelled[key]) == value for key, value in raw.items())
            for raw, labelled in zip(raw_rows, labelled_rows)
        ),
        "pass": len(labelled_rows) == 191
        and class_counts
        == {"prime": 43, "prime_power": 14, "mixed_composite": 134},
    }
    write_json(
        result_dir / "classification_certificate.json",
        classification_certificate,
    )
    if not classification_certificate["pass"]:
        raise AssertionError("post-census classification certificate failed")

    ledger = "".join(
        f"{digest(result_dir / name)}  {name}\n"
        for name in PROTOTYPE_PAYLOADS
    )
    aggregate = hashlib.sha256(ledger.encode("utf-8")).hexdigest()
    bridge = {
        "candidate_id": "SD-C35",
        "prototype_core_sha256_expected": PROTOTYPE_CORE_SHA256,
        "prototype_core_sha256_actual": digest(
            code_dir / "cycle_quotient_core.py"
        ),
        "prototype_runner_sha256_expected": PROTOTYPE_RUNNER_SHA256,
        "prototype_runner_sha256_actual": digest(
            code_dir / "generate_results.py"
        ),
        "prototype_payload_aggregate_expected": PROTOTYPE_PAYLOAD_AGGREGATE,
        "prototype_payload_aggregate_actual": aggregate,
        "prototype_test_count": test_report["test_count"],
        "prototype_test_passes": test_report["passes"],
        "payloads": [
            {"path": name, "sha256": digest(result_dir / name)}
            for name in PROTOTYPE_PAYLOADS
        ],
    }
    bridge["pass"] = (
        bridge["prototype_core_sha256_actual"] == PROTOTYPE_CORE_SHA256
        and bridge["prototype_runner_sha256_actual"]
        == PROTOTYPE_RUNNER_SHA256
        and aggregate == PROTOTYPE_PAYLOAD_AGGREGATE
        and test_report["passes"] == test_report["test_count"] == 25
    )
    write_json(result_dir / "prototype_bridge_certificate.json", bridge)
    if not bridge["pass"]:
        raise AssertionError("prototype bridge mismatch")

    print(json.dumps({
        "candidate_id": "SD-C35",
        "classes": class_counts,
        "prototype_bridge": bridge["pass"],
        "tests": f'{test_report["passes"]}/{test_report["test_count"]}',
    }, sort_keys=True))


if __name__ == "__main__":
    main()
