"""Regression coverage for the independent R056 checker."""

from __future__ import annotations

import ast
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest

from scripts.analyze_true_image_refinement_r056 import (
    CENTERED_SCALING_ORDER,
    analyze_payload,
    loglog_fit,
)
from scripts.audit_true_image_refinement_r056 import (
    build_configuration,
    lift_nodes as producer_lift_nodes,
    load_and_validate_protocol,
    project_pairs as producer_project_pairs,
)
from scripts.check_true_image_refinement_r056 import (
    EDGE_ARRAY_KEYS,
    EdgeArtifact,
    _cell_intervals,
    _maps_to_arrays,
    adaptive_count,
    brute_force_source,
    check_fixed_sources,
    check_refinement_projections,
    compare_artifacts,
    constants_from_protocol,
    fixed_source_ids,
    load_edge_artifact,
    load_protocol,
    make_edges,
    recompute_edge_decisions,
    run_microgrid_sweep,
    run_nested_projection_toy_checks,
    run_predicate_toy_checks,
    run_scc_toy_checks,
    sha256_file,
    validate_persisted_payload,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = PROJECT_ROOT / "scripts" / "check_true_image_refinement_r056.py"
PRODUCTION_CHECK = (
    PROJECT_ROOT
    / "results"
    / "true_image_refinement_independent_check_r056.json"
)


def test_r056_checker_has_no_producer_helper_imports():
    tree = ast.parse(CHECKER_PATH.read_text(encoding="utf-8"))
    imported_modules: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.append(node.module)
    assert not any(module.startswith("scripts.") for module in imported_modules)
    assert not any("audit_true_image" in module for module in imported_modules)


def test_r056_exact_predicate_scc_and_nested_partition_toys_pass():
    assert run_predicate_toy_checks()["pass"]
    assert run_scc_toy_checks()["pass"]
    assert run_nested_projection_toy_checks()["pass"]


def test_r056_frozen_producer_protocol_is_loadable_before_production():
    protocol = load_and_validate_protocol()
    assert protocol["status"] == "FROZEN_BEFORE_HELDOUT_PRODUCTION"
    assert len(protocol["development_anchors"]) == 4
    assert len(protocol["heldout_configurations"]) == 6
    assert len(protocol["nested_refinements"]) == 3


def test_r056_producer_toy_configuration_persists_canonical_arrays(tmp_path: Path):
    artifact_path = tmp_path / "toy_n4_d0.npz"
    record = build_configuration(
        {
            "configuration": "toy_n4_d0",
            "grid": 4,
            "offset": Fraction(0),
            "evidence_role": "unit_test",
            "protocol_role": "unit_test",
            "pre_freeze_uncapped_k_max": None,
            "edge_path": artifact_path,
        }
    )
    assert record["candidate_hull_contains_true_pass"]
    assert record["slab_active_equals_analytic_hull_active_pass"]
    assert record["true_closed_equals_mutual_outer_forward_pass"]
    assert record["true_closed_equals_mutual_outer_backward_pass"]
    assert record["true_positive_equals_outer_positive_forward_pass"]
    assert record["true_positive_equals_outer_positive_backward_pass"]
    artifact = load_edge_artifact(artifact_path, 4)
    decisions = recompute_edge_decisions(artifact.arrays)
    assert decisions["all_decision_set_differences_zero"]


def test_r056_producer_projection_and_lift_match_checker_toy_semantics():
    child_pairs = np.asarray([[0, 10], [1, 11], [12, 3]], dtype=np.int64)
    projected = producer_project_pairs(child_pairs, child_grid=4, parent_grid=2)
    assert {tuple(map(int, row)) for row in projected} == {(0, 3), (2, 1)}
    lifted = producer_lift_nodes({0, 3}, parent_grid=2, child_grid=4)
    assert lifted == {0, 1, 4, 5, 10, 11, 14, 15}


def test_r056_independent_checker_rejects_incomplete_refinement_npz(
    tmp_path: Path,
):
    parent_forward = np.asarray([[0, 3, 1], [2, 1, 0]], dtype=np.int64)
    parent_backward = np.asarray([[1, 2, 0], [3, 0, 1]], dtype=np.int64)
    child_forward = np.asarray(
        [[0, 10, 0], [1, 11, 1], [12, 3, 0]], dtype=np.int64
    )
    child_backward = np.asarray(
        [[3, 12, 0], [10, 0, 0], [11, 1, 1]], dtype=np.int64
    )
    parent_active = np.arange(4, dtype=np.int64)
    child_active = np.arange(16, dtype=np.int64)
    parent_arrays = {
        "true_forward_edges": parent_forward,
        "true_backward_edges": parent_backward,
        "outer_forward_edges": parent_forward.copy(),
        "outer_backward_edges": parent_backward.copy(),
        "active_node_ids": parent_active,
        "analytic_active_node_ids": parent_active.copy(),
        "k_values": np.ones(2, dtype=np.int64),
    }
    child_arrays = {
        "true_forward_edges": child_forward,
        "true_backward_edges": child_backward,
        "outer_forward_edges": child_forward.copy(),
        "outer_backward_edges": child_backward.copy(),
        "active_node_ids": child_active,
        "analytic_active_node_ids": child_active.copy(),
        "k_values": np.ones(4, dtype=np.int64),
    }
    projected_closed_forward = np.asarray([[0, 3], [2, 1]], dtype=np.int64)
    projected_closed_backward = np.asarray([[1, 2], [3, 0]], dtype=np.int64)
    projected_positive_forward = np.asarray([[0, 3]], dtype=np.int64)
    projected_positive_backward = np.asarray([[3, 0]], dtype=np.int64)
    refinement_path = tmp_path / "refinement.npz"
    np.savez_compressed(
        refinement_path,
        lift_parent_active_node_ids=child_active,
        active_lift_missing_child_node_ids=np.empty(0, dtype=np.int64),
        true_closed_complete_projected_edges=projected_closed_forward,
        true_closed_complete_projected_backward_edges=projected_closed_backward,
        true_closed_matched_support_projected_edges=projected_closed_forward,
        true_closed_matched_support_projected_backward_edges=projected_closed_backward,
        true_closed_parent_active_induced_edges=projected_closed_forward,
        true_closed_parent_active_induced_backward_edges=projected_closed_backward,
        true_positive_complete_projected_edges=projected_positive_forward,
        true_positive_complete_projected_backward_edges=projected_positive_backward,
        true_positive_matched_support_projected_edges=projected_positive_forward,
        true_positive_matched_support_projected_backward_edges=projected_positive_backward,
        true_positive_parent_active_induced_edges=projected_positive_forward,
        true_positive_parent_active_induced_backward_edges=projected_positive_backward,
    )
    passing_metrics = {
        "complete_projection_equals_parent_pass": True,
        "complete_backward_projection_equals_parent_pass": True,
        "matched_support_projection_equals_parent_active_graph_pass": True,
        "matched_support_backward_projection_equals_parent_active_graph_pass": True,
    }
    payload = {
        "refinements": [
            {
                "parent_configuration": "p",
                "child_configuration": "c",
                "exact_nested_edge_vectors_pass": True,
                "lift_parent_active_subset_child_active_pass": True,
                "active_lift_missing_child_node_count": 0,
                "refinement_array_path": str(refinement_path),
                "refinement_array_sha256": sha256_file(refinement_path),
                "true_closed": dict(passing_metrics),
                "true_positive": dict(passing_metrics),
            }
        ]
    }
    protocol = {
        "constants": {
            "a": "6",
            "radius": "0.6380064794363034",
            "eta": "1/4",
            "maximum_subdivisions": 64,
        },
        "development_anchors": [
            {"configuration_id": "p", "grid": 2, "grid_offset": "0"}
        ],
        "heldout_configurations": [
            {"configuration_id": "c", "grid": 4, "grid_offset": "0"}
        ],
        "nested_refinements": [
            {"parent_configuration_id": "p", "child_configuration_id": "c"}
        ],
    }
    artifacts = {
        "p": EdgeArtifact(tmp_path / "parent.npz", parent_arrays),
        "c": EdgeArtifact(tmp_path / "child.npz", child_arrays),
    }
    result = check_refinement_projections(payload, protocol, artifacts)
    assert result["refinement_count"] == 1
    pair = result["pairs"][0]
    assert pair["variants"]["true_closed"]["directions"]["forward"][
        "complete_labelled_projection_equals_parent_pass"
    ]
    assert not pair["refinement_artifact_schema"]["pass"]
    assert pair["refinement_artifact_schema"]["missing_array_keys"]
    assert not result["all_refinement_projection_checks_pass"]
    assert not result["pass"]


def test_r056_descriptive_loglog_fit_has_no_decision_threshold():
    records = {}
    for name in CENTERED_SCALING_ORDER:
        grid = int(name.split("_")[0][1:])
        records[name] = {
            "grid": grid,
            "true_closed_graph": {"largest_scc_size": max(2, round(grid**1.1))},
        }
    fit = loglog_fit(records, "true_closed_graph")
    assert fit["fit_available"]
    assert fit["r_squared"] > 0.999
    assert "threshold" not in fit
    assert "dimension" in fit["interpretation"]


def test_r056_protocol_fixed_source_schedule_is_deterministic_and_unique():
    protocol = load_protocol()
    for item in protocol["heldout_configurations"]:
        grid = int(item["grid"])
        first = fixed_source_ids(grid)
        second = fixed_source_ids(grid)
        assert first == second
        assert len(first) == len(set(first)) == 64
        assert all(0 <= node < grid * grid for node in first)
        middle = grid // 2
        mandatory = {
            0,
            grid - 1,
            (grid - 1) * grid,
            grid * grid - 1,
            middle,
            (grid - 1) * grid + middle,
            middle * grid,
            middle * grid + grid - 1,
            middle * grid + middle,
            middle * grid + middle - 1,
            (middle - 1) * grid + middle,
            (middle - 1) * grid + middle - 1,
        }
        assert mandatory <= set(first)


@pytest.mark.parametrize(
    ("grid", "offset", "expected_true", "expected_outer"),
    [
        (7, Fraction(0), 221, 231),
        (8, Fraction(1, 3), 310, 319),
    ],
)
def test_r056_required_full_n4_microgrid_sweeps(
    grid: int,
    offset: Fraction,
    expected_true: int,
    expected_outer: int,
):
    constants = constants_from_protocol(load_protocol())
    result = run_microgrid_sweep(grid, offset, constants)
    assert result["source_target_pair_count"] == grid**4
    assert result["edge_counts"]["true_forward_edges"] == expected_true
    assert result["edge_counts"]["true_backward_edges"] == expected_true
    assert result["edge_counts"]["outer_forward_edges"] == expected_outer
    assert result["edge_counts"]["outer_backward_edges"] == expected_outer
    assert result["all_decision_set_differences_zero"]
    assert result["pass"]


def _write_micro_npz(path: Path, *, use_uncapped_alias: bool = False):
    base_protocol = load_protocol()
    constants = constants_from_protocol(base_protocol)
    grid = 8
    offset = Fraction(1, 3)
    edges = make_edges(constants.radius, grid, offset)
    per_source = [
        brute_force_source(edges, source, constants)
        for source in range(grid * grid)
    ]
    arrays = _maps_to_arrays(per_source)
    cells = _cell_intervals(edges)
    minimum_width = min(upper - lower for lower, upper in cells)
    k_values = np.asarray(
        [adaptive_count(lower, upper, minimum_width, constants) for lower, upper in cells],
        dtype=np.int64,
    )
    node_ids = np.asarray([0, 1, 8, 9], dtype=np.int64)
    payload = {
        **arrays,
        "active_node_ids": node_ids,
        "analytic_active_node_ids": node_ids.copy(),
        ("uncapped_k_values" if use_uncapped_alias else "k_values"): k_values,
    }
    np.savez_compressed(path, **payload)
    return arrays, k_values, node_ids


@pytest.mark.parametrize("use_uncapped_alias", [False, True])
def test_r056_npz_schema_loads_without_pickle_and_recomputes_decisions(
    tmp_path: Path, use_uncapped_alias: bool
):
    path = tmp_path / "micro.npz"
    arrays, k_values, node_ids = _write_micro_npz(
        path, use_uncapped_alias=use_uncapped_alias
    )
    artifact = load_edge_artifact(path, 8)
    for key in EDGE_ARRAY_KEYS:
        assert np.array_equal(artifact.arrays[key], arrays[key])
    assert np.array_equal(artifact.arrays["k_values"], k_values)
    assert np.array_equal(artifact.arrays["active_node_ids"], node_ids)
    assert recompute_edge_decisions(artifact.arrays)[
        "all_decision_set_differences_zero"
    ]


def test_r056_npz_schema_rejects_object_arrays(tmp_path: Path):
    path = tmp_path / "object.npz"
    arrays, k_values, node_ids = _write_micro_npz(path)
    arrays["true_forward_edges"] = np.asarray([{"not": "numeric"}], dtype=object)
    np.savez_compressed(
        path,
        **arrays,
        active_node_ids=node_ids,
        analytic_active_node_ids=node_ids,
        k_values=k_values,
    )
    with pytest.raises(ValueError, match="Object arrays cannot be loaded"):
        load_edge_artifact(path, 8)


def test_r056_synthetic_persisted_schema_fixed_sources_and_replay(tmp_path: Path):
    artifact_path = tmp_path / "n8_dp1_3.npz"
    arrays, _, node_ids = _write_micro_npz(artifact_path)
    sha256 = sha256_file(artifact_path)
    heldouts = [
        {
            "configuration_id": f"toy_{index}",
            "grid": 8,
            "grid_offset": "1/3",
        }
        for index in range(6)
    ]
    protocol = {
        "constants": {
            "a": "6",
            "radius": "0.6380064794363034",
            "eta": "1/4",
            "maximum_subdivisions": 64,
        },
        "development_anchors": [],
        "heldout_configurations": heldouts,
    }
    records = []
    for configuration in heldouts:
        records.append(
            {
                "configuration": configuration["configuration_id"],
                "grid": 8,
                "grid_offset_fraction": "1/3",
                "edge_array_path": str(artifact_path),
                "edge_array_sha256": sha256,
                "edge_array_schema": {
                    "edge_columns": ["source_id", "target_id", "positive_flag"],
                    "edge_dtype": "int64",
                    "node_dtype": "int64",
                    "allow_pickle": False,
                },
                "active_node_count": len(node_ids),
                "true_forward_closed_edge_count": len(arrays["true_forward_edges"]),
                "true_backward_closed_edge_count": len(arrays["true_backward_edges"]),
                "outer_forward_closed_edge_count": len(arrays["outer_forward_edges"]),
                "outer_backward_closed_edge_count": len(arrays["outer_backward_edges"]),
                "true_edge_subset_outer_pass": True,
                "true_positive_subset_outer_positive_pass": True,
                "true_forward_inverse_labelled_transpose_pass": True,
                "true_closed_equals_mutual_outer_forward_pass": True,
                "true_closed_equals_mutual_outer_backward_pass": True,
                "true_positive_equals_outer_positive_forward_pass": True,
                "true_positive_equals_outer_positive_backward_pass": True,
                "true_closed_mutual_outer_forward_symmetric_difference_count": 0,
                "true_closed_mutual_outer_backward_symmetric_difference_count": 0,
                "true_positive_outer_positive_forward_symmetric_difference_count": 0,
                "true_positive_outer_positive_backward_symmetric_difference_count": 0,
            }
        )
    payload = {"run_id": "R056_TRUE_IMAGE_REFINEMENT", "records": records}
    artifacts, schema = validate_persisted_payload(payload, protocol)
    assert schema["configuration_record_count"] == 6
    assert schema["all_persisted_decision_set_differences_zero"]
    assert schema["pass"]
    fixed = check_fixed_sources(protocol, artifacts, workers=2)
    assert fixed["workers"] == 2
    assert fixed["all_fixed_source_checks_pass"]
    assert fixed["pass"]
    comparison = compare_artifacts(artifacts["toy_0"], artifacts["toy_1"])
    assert comparison["pass"]

    bad_payload = json.loads(json.dumps(payload))
    bad_payload["records"][0][
        "true_closed_mutual_outer_forward_symmetric_difference_count"
    ] = 1
    with pytest.raises(AssertionError, match="reported decision fields"):
        validate_persisted_payload(bad_payload, protocol)


@pytest.fixture(scope="module")
def first_production_refinement_case():
    protocol = load_protocol()
    payload = json.loads(
        (PROJECT_ROOT / "results" / "true_image_refinement_r056.json").read_text(
            encoding="utf-8"
        )
    )
    specification = protocol["nested_refinements"][0]
    parent_name = str(specification["parent_configuration_id"])
    child_name = str(specification["child_configuration_id"])
    configurations = {
        str(item["configuration_id"]): item
        for block in ("development_anchors", "heldout_configurations")
        for item in protocol[block]
    }
    records = {str(item["configuration"]): item for item in payload["records"]}
    reduced_protocol = {
        "constants": protocol["constants"],
        "development_anchors": [configurations[parent_name]],
        "heldout_configurations": [configurations[child_name]],
        "nested_refinements": [specification],
    }
    refinement_record = next(
        item
        for item in payload["refinements"]
        if item["parent_configuration"] == parent_name
        and item["child_configuration"] == child_name
    )
    reduced_payload = {
        "refinements": [json.loads(json.dumps(refinement_record))]
    }
    artifacts = {}
    for name in (parent_name, child_name):
        path = Path(records[name]["edge_array_path"])
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        artifacts[name] = load_edge_artifact(path, int(configurations[name]["grid"]))
    return reduced_payload, reduced_protocol, artifacts


def test_r056_checker_independently_recomputes_persisted_refinement_decisions(
    first_production_refinement_case,
):
    payload, protocol, artifacts = first_production_refinement_case
    result = check_refinement_projections(payload, protocol, artifacts)
    assert result["refinement_count"] == 1
    assert result["all_refinement_projection_checks_pass"]
    assert result["pass"]
    pair = result["pairs"][0]
    assert pair["refinement_artifact_sha256_pass"]
    assert pair["refinement_artifact_schema"]["pass"]
    assert all(pair["persisted_decision_array_equality"].values())
    assert all(pair["reported_refinement_field_checks"].values())
    assert pair["active_lift"]["lift_parent_active_subset_child_active_pass"]
    for variant in ("true_closed", "true_positive"):
        for direction in ("forward", "backward"):
            decision = pair["variants"][variant]["directions"][direction]
            assert decision["positive_if_any_projection_rule_applied"]
            assert decision["complete_labelled_projection_equals_parent_pass"]
            assert decision[
                "matched_support_labelled_projection_equals_parent_active_graph_pass"
            ]
        assert pair["variants"][variant]["matched_support_descendant"]["pass"]


def test_r056_checker_rejects_tampered_refinement_decision_array_even_with_new_hash(
    tmp_path: Path,
    first_production_refinement_case,
):
    payload, protocol, artifacts = first_production_refinement_case
    bad_payload = json.loads(json.dumps(payload))
    original = Path(bad_payload["refinements"][0]["refinement_array_path"])
    if not original.is_absolute():
        original = PROJECT_ROOT / original
    with np.load(original, allow_pickle=False) as archive:
        arrays = {key: np.array(archive[key], copy=True) for key in archive.files}
    key = "true_closed_complete_projected_edges"
    arrays[key] = arrays[key][:-1]
    tampered = tmp_path / "tampered_refinement.npz"
    np.savez_compressed(tampered, **arrays)
    bad_payload["refinements"][0]["refinement_array_path"] = str(tampered)
    bad_payload["refinements"][0]["refinement_array_sha256"] = sha256_file(
        tampered
    )

    result = check_refinement_projections(bad_payload, protocol, artifacts)
    pair = result["pairs"][0]
    assert pair["refinement_artifact_sha256_pass"]
    assert pair["refinement_artifact_schema"]["pass"]
    assert not pair["persisted_decision_array_equality"][key]
    assert not pair["pass"]
    assert not result["pass"]


def test_r056_checker_rejects_tampered_nontrivial_descendant_decision(
    first_production_refinement_case,
):
    payload, protocol, artifacts = first_production_refinement_case
    bad_payload = json.loads(json.dumps(payload))
    bad_payload["refinements"][0]["true_closed"][
        "nontrivial_descendant_exists_pass"
    ] = False
    result = check_refinement_projections(bad_payload, protocol, artifacts)
    pair = result["pairs"][0]
    descendant = pair["variants"]["true_closed"][
        "matched_support_descendant"
    ]
    assert descendant["nontrivial_descendant_exists_pass"]
    assert not descendant["reported_metric_checks"][
        "nontrivial_descendant_exists_pass"
    ]
    assert not descendant["pass"]
    assert not pair["pass"]
    assert not result["pass"]


def test_r056_analyzer_rejects_stale_checker_without_refinement_section():
    producer = json.loads(
        (PROJECT_ROOT / "results" / "true_image_refinement_r056.json").read_text(
            encoding="utf-8"
        )
    )
    independent = {
        "run_id": "R056_TRUE_IMAGE_REFINEMENT_INDEPENDENT_CHECK",
        "checker_imports_producer_geometry_or_scc_helpers": False,
        "all_checks_pass": True,
        "persisted_refinement_projections": {"pass": True},
    }
    protocol = json.loads(
        (
            PROJECT_ROOT
            / "research"
            / "refine-logs"
            / "R056_TRUE_IMAGE_REFINEMENT_PROTOCOL.json"
        ).read_text(encoding="utf-8")
    )
    decisions, _ = analyze_payload(producer, independent, protocol)
    assert decisions["independent_checker_pass"]

    stale = json.loads(json.dumps(independent))
    stale.pop("persisted_refinement_projections")
    assert stale["all_checks_pass"]
    stale_decisions, _ = analyze_payload(producer, stale, protocol)
    assert not stale_decisions["independent_checker_pass"]
    assert not stale_decisions["g0_anchor_and_integrity_pass"]
    assert stale_decisions["interpretation"] == "INVALID_AUDIT_INTEGRITY_FAILURE"


@pytest.mark.skipif(
    not PRODUCTION_CHECK.exists(),
    reason="R056 production checker artifact is unavailable in this checkout",
)
def test_r056_persisted_independent_checker_artifact_passes():
    payload = json.loads(PRODUCTION_CHECK.read_text(encoding="utf-8"))
    assert payload["run_id"] == "R056_TRUE_IMAGE_REFINEMENT_INDEPENDENT_CHECK"
    assert not payload["checker_imports_producer_geometry_or_scc_helpers"]
    assert len(payload["microgrid_full_sweeps"]) == 2
    assert payload["fixed_source_full_target_sweeps"][
        "all_fixed_source_checks_pass"
    ]
    assert payload["all_checks_pass"]
