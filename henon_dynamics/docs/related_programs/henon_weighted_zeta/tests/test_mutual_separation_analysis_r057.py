"""Producer/result/analysis regression tests for R057."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from scripts.analyze_mutual_separation_r057 import analyze_payload
from scripts.audit_mutual_separation_r057 import (
    Configuration,
    PROTOCOL_SHA256,
    expand_configurations,
    load_and_validate_protocol,
    summarize_configuration,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULT = PROJECT_ROOT / "results" / "mutual_separation_r057.json"
CHECKER = PROJECT_ROOT / "results" / "mutual_separation_independent_check_r057.json"
ANALYSIS = PROJECT_ROOT / "results" / "mutual_separation_analysis_r057.json"


def test_r057_producer_expands_the_frozen_panel_exactly():
    protocol = load_and_validate_protocol()
    configurations = expand_configurations(protocol)
    assert len(configurations) == 517
    assert len({item.configuration_id for item in configurations}) == 517
    assert PROTOCOL_SHA256 == (
        "4eb540372ad29568054cdaa05b7c3f605913dfcf358855c98f45594c78af0a91"
    )


def test_r057_producer_recomputes_n60_and_neighbor_controls():
    common = {
        "panel_id": "test",
        "role": "test",
        "grid_offset": Fraction(0),
        "a": Fraction(6),
        "c": Fraction(1),
        "radius": Fraction("0.6380064794363034"),
        "eta": Fraction(1, 4),
        "fresh_discovery_eligible": False,
    }
    records = {}
    for grid in (58, 60, 62):
        record, rows = summarize_configuration(
            Configuration(
                configuration_id=f"n{grid}",
                grid=grid,
                **common,
            )
        )
        records[grid] = record
        assert len(rows) == grid - 1
    assert records[58]["certificate_pass"]
    assert not records[60]["certificate_pass"]
    assert records[62]["certificate_pass"]
    witness = records[60]["first_failure_witness"]
    assert witness["source_id"] == 2789
    assert witness["target_id"] == 1859
    assert witness["exact_false_mutual_witness_pass"]


def test_r057_persisted_production_preserves_failures_and_cap_gate():
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    decisions = payload["decisions"]
    assert payload["run_id"] == "R057_MUTUAL_SEPARATION"
    assert payload["protocol_sha256"] == PROTOCOL_SHA256
    assert payload["boundary_row_count"] == 102494
    assert decisions["total_pass_count"] == 506
    assert decisions["total_fail_count"] == 11
    assert decisions["fresh_counterexample_count"] == 3
    assert decisions["fresh_counterexample_configuration_ids"] == [
        "phase_n71_dm1_5",
        "phase_n89_dm2_7",
        "phase_n173_dp2_7",
    ]
    assert decisions["g0_protocol_and_exact_arithmetic_pass"]
    assert not decisions["g1_certificate_and_witness_integrity_pass"]
    assert decisions["g1_cap_active_configuration_count"] == 16
    assert decisions["g1_cap_free_configuration_count"] == 501
    assert decisions["g2_all_theory_controls_pass"]


def test_r057_analysis_separates_strict_gate_from_core_theory_audit():
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    checker = json.loads(CHECKER.read_text(encoding="utf-8"))
    recomputed = analyze_payload(result, checker)
    persisted = json.loads(ANALYSIS.read_text(encoding="utf-8"))
    for analysis in (recomputed, persisted):
        assert not analysis["decision"]["strict_all_frozen_gates_pass"]
        assert analysis["decision"]["core_theory_and_counterexample_audit_pass"]
        assert analysis["decision"]["closed_universal_identity_status"] == "REFUTED"
        assert analysis["decision"]["g3_independent_checker_pass"]
        assert analysis["summary"]["fresh_counterexample_count"] == 3
        assert analysis["summary"]["centered_odd_failure_count"] == 0
        assert analysis["centered_failure_grids"] == [
            60,
            106,
            120,
            134,
            194,
            208,
            282,
            342,
        ]


def test_r057_theory_packages_record_corrected_scope():
    derivation = (PROJECT_ROOT / "DERIVATION_PACKAGE.md").read_text(encoding="utf-8")
    proof = (PROJECT_ROOT / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    assert "COHERENT AFTER REFRAMING / EXTRA ASSUMPTION" in derivation
    assert "necessary-and-sufficient criterion" in derivation
    assert "PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION" in proof
    assert "constructive counterexample" in proof.lower()
    assert "invariant set" in derivation
    assert "Riemann" in derivation
