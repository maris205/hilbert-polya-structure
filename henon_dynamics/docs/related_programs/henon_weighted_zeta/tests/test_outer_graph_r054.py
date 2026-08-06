"""Regression tests for the exploratory R054 outer-cover graph audit."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.audit_outer_graph_r054 import (
    GRAPH_VARIANTS,
    LARGEST_SCC_SELECTION_RULE,
    SCC_NODE_ID_SCHEMA,
    graph_stats,
    node_hash,
    strongly_connected_components,
)
from scripts.analyze_outer_graph_r054 import analyze_payload


PROJECT_ROOT = Path(__file__).resolve().parents[1]
R054_RESULT = PROJECT_ROOT / "results" / "outer_graph_r054.json"
R053_RESULT = PROJECT_ROOT / "results" / "exact_closed_cover_r053.json"
R054_ANALYSIS = PROJECT_ROOT / "results" / "outer_graph_analysis_r054.json"


def test_kosaraju_finds_nontrivial_and_singleton_components():
    adjacency = [{1}, {0, 2}, {1}, set()]
    components = strongly_connected_components(adjacency)
    sizes = sorted((len(component) for component in components), reverse=True)
    assert sizes == [3, 1]


def test_kosaraju_finish_order_is_correct_for_branching_cross_edges():
    # This graph exposed the former mark-on-push finish-order bug.
    adjacency = [{1, 2}, set(), {1, 2}]
    components = strongly_connected_components(adjacency)
    assert sorted(sorted(component) for component in components) == [[0], [1], [2]]


def test_graph_stats_restricts_to_active_nodes_before_scc_counting():
    adjacency = [{1}, {0}, {3}, {2}]
    stats = graph_stats(adjacency, {0, 1})
    assert stats["active_node_count"] == 2
    assert stats["induced_edge_count"] == 2
    assert stats["scc_count"] == 1
    assert stats["largest_scc_size"] == 2
    assert stats["recurrent_node_count"] == 2


def test_graph_stats_largest_scc_ids_length_hash_and_schema_are_consistent():
    adjacency = [{1}, {0, 2}, {1}, set()]
    stats = graph_stats(adjacency, {0, 1, 2, 3})
    node_ids = stats["largest_scc_node_ids"]
    assert node_ids == [0, 1, 2]
    assert len(node_ids) == stats["largest_scc_size"]
    assert stats["largest_scc_node_id_count"] == len(node_ids)
    assert stats["largest_scc_node_ids_sha256"] == node_hash(node_ids)
    assert stats["largest_scc_selection_rule"] == LARGEST_SCC_SELECTION_RULE
    assert stats["largest_scc_node_id_schema"] == SCC_NODE_ID_SCHEMA


def _sets_with_insertion_order(rows: list[list[int]]) -> list[set[int]]:
    adjacency: list[set[int]] = []
    for row in rows:
        targets: set[int] = set()
        for target in row:
            targets.add(target)
        adjacency.append(targets)
    return adjacency


def test_graph_stats_is_independent_of_target_set_insertion_order():
    rows = [[1, 2], [0, 2], [0, 1], [4], [3]]
    forward = _sets_with_insertion_order(rows)
    reverse = _sets_with_insertion_order([list(reversed(row)) for row in rows])
    assert graph_stats(forward, {0, 1, 2, 3, 4}) == graph_stats(
        reverse, {4, 3, 2, 1, 0}
    )


def test_graph_stats_tied_largest_scc_uses_lexicographically_smallest_ids():
    # Two SCCs have size two: [0, 2] and [1, 3]. The documented tie-break
    # must select [0, 2], regardless of SCC discovery order.
    adjacency = [{2}, {3}, {0}, {1}]
    stats = graph_stats(adjacency, {3, 2, 1, 0})
    assert stats["largest_scc_size"] == 2
    assert stats["largest_scc_tie_count"] == 2
    assert stats["largest_scc_node_ids"] == [0, 2]
    assert stats["largest_scc_node_ids_sha256"] == node_hash([0, 2])


def test_r054_reproduces_r053_adjacency_hashes_and_counts():
    r054 = json.loads(R054_RESULT.read_text(encoding="utf-8"))
    r053 = json.loads(R053_RESULT.read_text(encoding="utf-8"))
    r053_by_name = {record["configuration"]: record for record in r053["records"]}
    assert len(r054["records"]) == 4
    for record in r054["records"]:
        parent = r053_by_name[record["configuration"]]
        assert record["forward_closed_edge_hash"] == parent["forward_closed_adjacency_sha256"]
        assert record["backward_closed_edge_hash"] == parent["backward_closed_adjacency_sha256"]
        assert record["forward_closed_edge_count"] == parent["forward_closed_adjacency_count"]
        assert record["forward_positive_edge_count"] == parent["forward_positive_area_adjacency_count"]
        assert record["backward_closed_edge_count"] == parent["backward_closed_adjacency_count"]
        assert record["backward_positive_edge_count"] == parent["backward_positive_area_adjacency_count"]
        assert all(
            record[variant]["active_node_count"]
            == record["two_sided_in_box_node_count"]
            for variant in GRAPH_VARIANTS
        )
        assert record["closed_contains_positive"]
        assert record["mutual_subset_closed"]


def test_r054_analysis_frozen_decisions_pass():
    payload = json.loads(R054_RESULT.read_text(encoding="utf-8"))
    parent = json.loads(R053_RESULT.read_text(encoding="utf-8"))
    decisions, records = analyze_payload(payload, parent)
    assert decisions["all_frozen_checks_pass"]
    assert decisions["parent_r053_alignment_pass"]
    assert len(records) == 4


def test_r054_analysis_artifact_is_persisted():
    analysis = json.loads(R054_ANALYSIS.read_text(encoding="utf-8"))
    assert analysis["run_id"] == "R054_OUTER_GRAPH_ANALYSIS"
    assert analysis["decisions"]["all_frozen_checks_pass"]
    assert len(analysis["records"]) == 4
