"""Regression checks for the independent R057 G3 checker."""

from __future__ import annotations

import ast
import json
from fractions import Fraction
from pathlib import Path

from scripts.check_mutual_separation_r057 import (
    PROTOCOL_SHA256,
    certificate_rows,
    expand_configurations,
    load_protocol,
    n60_configuration,
    quadratic_range,
    run_microgrid_checks,
    run_n60_check,
    sha256_file,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHECKER = PROJECT_ROOT / "scripts" / "check_mutual_separation_r057.py"
PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057_MUTUAL_SEPARATION_PROTOCOL.json"
)
CHECK_RESULT = (
    PROJECT_ROOT
    / "results"
    / "mutual_separation_independent_check_r057.json"
)


def test_r057_checker_does_not_import_producer_helpers():
    tree = ast.parse(CHECKER.read_text(encoding="utf-8"))
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    assert not any(module.startswith("scripts.") for module in imported)
    assert not any("audit_mutual_separation" in module for module in imported)


def test_r057_frozen_protocol_hash_and_independent_panel_expansion():
    protocol = load_protocol()
    assert sha256_file(PROTOCOL) == PROTOCOL_SHA256
    configurations = expand_configurations(protocol)
    assert len(configurations) == 517
    assert len({item.configuration_id for item in configurations}) == 517


def test_r057_quadratic_range_includes_cross_zero_critical_point():
    assert quadratic_range(Fraction(-2), Fraction(1), Fraction(6)) == (
        Fraction(0),
        Fraction(24),
    )


def test_r057_full_graph_microgrids_match_certificate_and_positive_identity():
    results = run_microgrid_checks(load_protocol())
    assert len(results) == 4
    assert [item["edge_counts"]["true_closed"] for item in results] == [
        119,
        174,
        231,
        296,
    ]
    assert all(item["true_closed_subset_mutual_outer_pass"] for item in results)
    assert all(item["certificate_iff_complete_graph_equality_pass"] for item in results)
    assert all(
        item["outer_forward_positive_equals_true_positive_pass"]
        and item["outer_reverse_positive_equals_true_positive_pass"]
        for item in results
    )
    assert all(item["pass"] for item in results)
    assert results[-1]["uncapped_k_max"] == 123
    assert results[-1]["capped_k_max"] == 64
    assert results[-1]["cap_active_count"] == 2


def test_r057_n60_constructive_witness_and_strict_equality_failure():
    protocol = load_protocol()
    result = run_n60_check(protocol)
    witness = result["recomputed_witness"]
    assert result["pass"]
    assert witness["source_id"] == 2789
    assert witness["target_id"] == 1859
    assert not witness["true_closed_present"]
    assert witness["mutual_outer_present"]
    rows = certificate_rows(n60_configuration(protocol))
    boundary = rows[29]
    assert boundary["boundary_index"] == 30
    assert boundary["margin_plus"] < 0
    assert not boundary["plus_pass"]


def test_r057_persisted_independent_audit_reports_g3_pass_and_cap_conflict():
    payload = json.loads(CHECK_RESULT.read_text(encoding="utf-8"))
    assert payload["run_id"] == "R057_MUTUAL_SEPARATION_INDEPENDENT_CHECK"
    assert not payload["checker_imports_producer_certificate_or_incidence_helpers"]
    assert payload["g3_independent_checker_pass"]
    assert not payload["producer_integrity_gates_pass"]
    assert not payload["strict_all_frozen_gates_pass"]
    assert payload["all_checks_pass"]
    assert payload["persisted_result_audit"]["boundary_csv"]["row_count"] == 102494
    assert payload["persisted_result_audit"]["witness_replay"]["witness_count"] == 11
    assert payload["persisted_result_audit"]["cap_gate_failure_count"] == 16
    assert len(payload["issues"]) == 2
