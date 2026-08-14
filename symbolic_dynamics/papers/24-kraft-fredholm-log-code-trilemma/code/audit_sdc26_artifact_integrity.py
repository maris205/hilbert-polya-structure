#!/usr/bin/env python3
"""Audit SD-C26 exact artifacts, Route schema, source policy, and hygiene."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C26" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc26_kraft_fredholm.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_CSV_ROWS = {
    "arbitrary_inventory_controls.csv": 84,
    "diagonal_escape_controls.csv": 28,
    "disjoint_cycle_witnesses.csv": 672,
    "factorization_renewal_controls.csv": 4,
    "finite_code_counting.csv": 112,
    "finite_prefix_stationarization.csv": 140,
    "finite_roof_inventory.csv": 5,
    "marker_firewall.csv": 20,
    "mixed_primitive_ledger.csv": 112,
    "route_gate_summary.csv": 5,
    "shared_prime_pair_firewall.csv": 28,
    "shared_trie_closure.csv": 28,
}

REQUIRED_ROUTE_KEYS = {
    "skill",
    "skill_version",
    "candidate_id",
    "source_commit",
    "code_commit",
    "evaluation_date",
    "artifact_path_base",
    "freeze_note",
    "source_lock",
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "adversarial_controls",
    "route_tuple",
    "overall_verdict",
    "claim_boundary",
    "blocking_conditions",
    "next_smallest_test",
    "round2_clues",
    "route_b_invocation_allowed",
}

EXPECTED_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]


def csv_rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def true(row: dict[str, str], field: str) -> bool:
    return row.get(field) == "True"


def false(row: dict[str, str], field: str) -> bool:
    return row.get(field) == "False"


def is_git_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    )


def forbidden_metadata_keys(value: object, path: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            if str(key).lower() in {
                "timestamp",
                "elapsed",
                "elapsed_seconds",
                "wall_time",
                "wall_time_seconds",
                "hostname",
                "cwd",
            }:
                found.append(child_path)
            found.extend(forbidden_metadata_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(forbidden_metadata_keys(child, f"{path}[{index}]"))
    return found


def text_control_characters() -> dict[str, list[int]]:
    suffixes = {".bib", ".csv", ".json", ".md", ".py", ".tex", ".txt", ".yaml", ".yml"}
    bad: dict[str, list[int]] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        positions = [
            index
            for index, byte in enumerate(path.read_bytes())
            if byte < 32 and byte not in {9, 10}
        ]
        if positions:
            bad[path.relative_to(ROOT).as_posix()] = positions[:20]
    return bad


def main() -> int:
    row_counts: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_CSV_ROWS.items():
        raw = (RESULTS / name).read_bytes()
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        data = csv_rows(name)
        row_counts[name] = len(data)
        if len(data) != expected:
            raise AssertionError(f"{name}: {len(data)} rows, expected {expected}")

    json_names = sorted(path.name for path in RESULTS.glob("*.json") if path != OUTPUT)
    json_parse: dict[str, bool] = {}
    forbidden_metadata: dict[str, list[str]] = {}
    for name in json_names:
        payload = json.loads((RESULTS / name).read_text(encoding="utf-8"))
        json_parse[name] = True
        forbidden = forbidden_metadata_keys(payload)
        if forbidden:
            forbidden_metadata[name] = forbidden

    route = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))
    route_missing = sorted(REQUIRED_ROUTE_KEYS - set(route))
    metrics = route.get("a2", {}).get("metrics", {})
    target_fields = (
        "zero_error_train",
        "zero_error_validation",
        "zero_error_test",
        "extra_zero_count",
        "missing_zero_count",
        "root_count_discrepancy",
    )
    artifact_paths = route.get("source_lock", {}).get("artifact_paths", [])
    future_artifacts = {"results/integrity_audit.json", "results/SHA256SUMS.txt"}
    missing_artifacts = [
        relative
        for relative in artifact_paths
        if relative not in future_artifacts and not (ROOT / relative).is_file()
    ]
    source_commit = route.get("source_commit")
    code_commit = route.get("code_commit")
    lock_commit = route.get("source_lock", {}).get("code_commit")
    paired_pending = source_commit == code_commit == lock_commit == PENDING
    paired_sealed = (
        source_commit == code_commit == lock_commit and is_git_hash(source_commit)
    )
    route_checks = {
        "yaml_parse": isinstance(route, dict),
        "required_top_level_keys": not route_missing,
        "candidate_id": route.get("candidate_id") == "SD-C26",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "route_tuple": route.get("route_tuple") == EXPECTED_TUPLE,
        "layer_verdicts": [
            route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")
        ]
        == EXPECTED_TUPLE,
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_pending or paired_sealed,
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "artifact_paths_exist": not missing_artifacts,
        "target_zero_root_fields_na": all(
            isinstance(metrics.get(field), str)
            and metrics[field].startswith("not_applicable;")
            for field in target_fields
        ),
        "target_zero_data_false": metrics.get("target_zero_data_used") is False,
        "proves_too_much": route.get("adversarial_controls", {}).get(
            "proves_too_much_risk"
        )
        is True,
        "a4_scoped": "this candidate"
        in route.get("a4", {}).get("strongest_failure", "").lower(),
    }

    source_tree = ast.parse(CORE.read_text(encoding="utf-8"))
    call_names = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    oracle = json.loads((RESULTS / "source_oracle_certificate.json").read_text())
    source_checks = {
        "candidate_evaluator_separation": oracle.get("candidate_evaluator_separated")
        is True,
        "no_forbidden_candidate_calls": oracle.get("forbidden_candidate_calls") == [],
        "static_call_audit": call_names.isdisjoint(
            {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
        ),
        "prime_table_false": oracle.get("prime_table_used_in_candidate") is False,
        "factorization_oracle_false": oracle.get(
            "factorization_oracle_used_in_candidate"
        )
        is False,
        "target_feedback_false": oracle.get("target_feedback_used_in_candidate")
        is False,
        "zero_data_false": oracle.get("riemann_zero_data_used") is False,
        "fixed_three_symbol_alphabet": oracle.get("finite_local_alphabet")
        == ["0", "1", "#"],
        "cutoff_independent_encoder": oracle.get("cutoff_dependent_encoder")
        is False,
    }

    finite_code = csv_rows("finite_code_counting.csv")
    disjoint = csv_rows("disjoint_cycle_witnesses.csv")
    trie = csv_rows("shared_trie_closure.csv")
    mixed = csv_rows("mixed_primitive_ledger.csv")
    pairs = csv_rows("shared_prime_pair_firewall.csv")
    determinants = json.loads(
        (RESULTS / "finite_trie_determinant_checks.json").read_text()
    )
    diagonal = csv_rows("diagonal_escape_controls.csv")
    marker = csv_rows("marker_firewall.csv")
    arbitrary = csv_rows("arbitrary_inventory_controls.csv")
    factorization = csv_rows("factorization_renewal_controls.csv")
    stationarization = csv_rows("finite_prefix_stationarization.csv")
    roofs = csv_rows("finite_roof_inventory.csv")
    route_rows = csv_rows("route_gate_summary.csv")
    tests = json.loads((RESULTS / "test_summary.json").read_text())
    double_run = json.loads((RESULTS / "double_run_certificate.json").read_text())
    summary = json.loads((RESULTS / "summary.json").read_text())

    scientific_checks = {
        "finite_code_separating": all(
            row["return_marker"] == "#"
            and row["finite_local_alphabet_size"] == "3"
            and row["cyclic_collision_count"] == "0"
            and true(row, "prime_orbit_separating_visible_code")
            and true(row, "capacity_bound_pass")
            and row["encoder_target_calls"] == "0"
            for row in finite_code
        ),
        "positive_roof_bounds": all(
            true(row, "max_sv_bound_pass")
            and true(row, "s1_bound_pass")
            and false(row, "finite_row_is_infinite_proof")
            for row in disjoint
        ),
        "shared_trie_noncompact": all(
            true(row, "all_return_roofs_positive")
            and false(row, "whole_tree_compact")
            and false(row, "shared_hub_prime_only_ledger")
            for row in trie
        ),
        "mixed_primitive_flood": all(
            int(row["mixed_primitive_necklaces"]) > 0
            and false(row, "connected_disconnected_match")
            and row["ledger_gate"] == "CYCLE_FLOOD"
            for row in mixed
        ),
        "prime_pair_ufa_firewall": all(
            true(row, "distinct_primes")
            and false(row, "perfect_prime_power")
            and true(row, "unique_factorization_contradiction")
            and false(row, "prime_only_connected_ledger_survives")
            for row in pairs
        ),
        "finite_trie_determinants": len(determinants) == 4
        and all(value["exact_match"] and not value["disconnected_euler_product"] for value in determinants.values()),
        "diagonal_proves_too_much": all(
            true(row, "whole_operator_s1_sigma2")
            and true(row, "proves_too_much")
            and false(row, "visible_finite_alphabet")
            for row in diagonal
        ),
        "marker_firewall": all(
            (
                true(row, "marked_germ_match")
                and row["architecture"] == "countable_atom_diagonal"
                and row["gate"] == "MARKER_PASS_BUT_SELECTOR_TAUTOLOGICAL"
            )
            or (
                false(row, "marked_germ_match")
                and true(row, "induction_required_to_degree_one")
                and false(row, "same_object_after_induction")
            )
            for row in marker
        ),
        "arbitrary_inventory_controls": all(
            true(row, "support_loaded_post_freeze")
            and false(row, "selectivity_credit")
            and true(row, "proves_too_much")
            for row in arbitrary
        ),
        "matched_density_controls": all(
            any(
                row["cutoff"] == cutoff
                and row["inventory"] == inventory
                and true(row, "prime_density_matched")
                for row in arbitrary
            )
            for cutoff in {row["cutoff"] for row in arbitrary}
            for inventory in (
                "matched_density_seeded_random",
                "matched_density_hash",
            )
        ),
        "factorization_connected_disconnected": all(
            true(row, "commutative_word_order_collision")
            and false(row, "prime_only_primitive_ledger")
            for row in factorization
        ),
        "stationarization_firewall": all(
            true(row, "finite_prefix_operator_compact")
            and false(row, "single_stationary_union_compact")
            and true(row, "shared_level_states_create_mixed_cycles")
            and false(row, "acyclic_level_has_primitive_orbits")
            for row in stationarization
        ),
        "finite_roof_rank": all(
            int(row["formal_Q_rank_of_log_primes"]) == int(row["prime_count"])
            and int(row["finite_roof_inventory_size"]) < int(row["prime_count"])
            and false(row, "all_prime_clocks_in_span")
            for row in roofs
        ),
        "route_rows": [row["verdict"] for row in route_rows] == EXPECTED_TUPLE,
        "summary_tuple": summary.get("route_tuple") == EXPECTED_TUPLE,
        "summary_rejected": summary.get("overall_verdict") == "ROUTE_A_REJECTED",
        "test_suite_35": tests.get("status") == "PASS"
        and tests.get("passed") == tests.get("collected") == 35,
        "double_run_byte_identical": double_run.get("status") == "PASS"
        and double_run.get("byte_identical") is True
        and double_run.get("mismatched_paths") == [],
    }

    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for pattern in ("__pycache__", ".pytest_cache")
        for path in ROOT.rglob(pattern)
    )
    control_characters = text_control_characters()
    result = {
        "candidate_id": "SD-C26",
        "cache_clean": not cache_paths,
        "cache_paths": cache_paths,
        "control_character_clean": not control_characters,
        "control_character_paths": control_characters,
        "csv_lf_only": csv_lf_only,
        "csv_row_counts": row_counts,
        "json_parse": json_parse,
        "forbidden_runtime_metadata": forbidden_metadata,
        "missing_artifact_paths": missing_artifacts,
        "provenance_mode": "pending_first_artifact_commit"
        if paired_pending
        else "sealed_git_commit",
        "route_a_missing_keys": route_missing,
        "route_a_schema": route_checks,
        "scientific_artifacts": scientific_checks,
        "source_policy": source_checks,
        "scope": {
            "primary_family": "Symbolic Dynamics",
            "theorem_class": "positive scalar finite-local-code counting-space adjacency",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
            "a4_claim": "this candidate constructs no Route-B mechanism",
        },
        "target_zero_data_used": False,
    }
    passed = (
        all(csv_lf_only.values())
        and not cache_paths
        and not control_characters
        and not forbidden_metadata
        and not missing_artifacts
        and not route_missing
        and all(route_checks.values())
        and all(source_checks.values())
        and all(scientific_checks.values())
    )
    result["integrity_pass"] = passed
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise AssertionError("artifact integrity gate failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

