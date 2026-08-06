"""Regression tests for the exact R055 true-image graph audit."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import pytest

from scripts.audit_true_image_graph_r055 import (
    require_outer_reference_matches,
    summarize_configuration,
)
from scripts.analyze_true_image_graph_r055 import analyze_payload
from scripts.check_true_image_graph_r055 import run_toy_checks


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRUE_RESULT = PROJECT_ROOT / "results" / "true_image_graph_r055.json"
OUTER_RESULT = PROJECT_ROOT / "results" / "outer_graph_r054.json"
TRUE_ANALYSIS = PROJECT_ROOT / "results" / "true_image_graph_analysis_r055.json"


def test_r055_toy_predicates_cover_boundary_and_interior_cases():
    run_toy_checks()


def _outer_reference_from_summary(record: dict[str, object]) -> dict[str, object]:
    return {
        "forward_closed_edge_count": record["outer_forward_closed_edge_count"],
        "backward_closed_edge_count": record["outer_backward_closed_edge_count"],
        "two_sided_in_box_node_count": record["two_sided_in_box_node_count"],
        "two_sided_in_box_node_ids_sha256": record[
            "two_sided_in_box_node_ids_sha256"
        ],
        "forward_closed_edge_hash": record["outer_forward_closed_edge_hash"],
        "backward_closed_edge_hash": record["outer_backward_closed_edge_hash"],
    }


def test_r055_summary_allows_missing_outer_reference_for_noncanonical_consumers():
    configuration = ("toy_n4_d0", 4, Fraction(0))
    record = summarize_configuration((configuration, None))
    assert not record["outer_reference_provided"]
    assert record["outer_reconstruction_pass"] is None
    assert record["candidate_hull_contains_true_pass"]
    assert record["true_edge_subset_outer_pass"]


def test_r055_canonical_guard_requires_a_matching_outer_parent():
    configuration = ("toy_n4_d0", 4, Fraction(0))
    without_parent = summarize_configuration((configuration, None))
    reference = _outer_reference_from_summary(without_parent)
    matched = summarize_configuration((configuration, reference))
    assert matched["outer_reference_provided"]
    assert matched["outer_reconstruction_pass"] is True
    require_outer_reference_matches([matched])

    with pytest.raises(AssertionError, match="toy_n4_d0"):
        require_outer_reference_matches([without_parent])

    bad_reference = dict(reference)
    bad_reference["forward_closed_edge_count"] = (
        int(bad_reference["forward_closed_edge_count"]) + 1
    )
    mismatched = summarize_configuration((configuration, bad_reference))
    assert mismatched["outer_reconstruction_pass"] is False
    with pytest.raises(AssertionError, match="toy_n4_d0"):
        require_outer_reference_matches([mismatched])


def test_r055_true_graph_matches_expected_outer_filters():
    payload = json.loads(TRUE_RESULT.read_text(encoding="utf-8"))
    assert payload["run_id"] == "R055_TRUE_IMAGE_GRAPH"
    assert len(payload["records"]) == 4
    for record in payload["records"]:
        assert record["outer_reconstruction_pass"]
        assert record["true_edge_subset_outer_pass"]
        assert record["true_positive_subset_outer_positive_pass"]
        assert record["true_forward_inverse_transpose_pass"]
        assert record["true_equals_outer_mutual_pass"]
        assert record["true_positive_equals_outer_positive_pass"]
        assert record["true_forward_closed_edge_count"] == record["true_mutual_edge_count"]
        assert record["true_forward_positive_edge_count"] <= record["true_forward_closed_edge_count"]


def test_r055_analyzer_all_frozen_checks_pass():
    payload = json.loads(TRUE_RESULT.read_text(encoding="utf-8"))
    outer = json.loads(OUTER_RESULT.read_text(encoding="utf-8"))
    decisions, records = analyze_payload(payload, outer)
    assert decisions["all_frozen_checks_pass"]
    assert decisions["outer_alignment_pass"]
    assert decisions["true_outer_mutual_equivalence_pass"]
    assert decisions["true_outer_mutual_hash_equality_pass"]
    assert decisions["true_outer_positive_hash_equality_pass"]
    assert len(records) == 4


def test_r055_analysis_artifact_is_persisted():
    analysis = json.loads(TRUE_ANALYSIS.read_text(encoding="utf-8"))
    assert analysis["run_id"] == "R055_TRUE_IMAGE_GRAPH_ANALYSIS"
    assert analysis["decisions"]["all_frozen_checks_pass"]
