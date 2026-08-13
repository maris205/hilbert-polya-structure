import math

import numpy as np

import sdc10_positive_cone_experiment as experiment


def test_internal_atom_generation():
    assert experiment.internal_multiplicative_atoms(8) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_free_reduction():
    group = experiment.FreeGroup()
    assert group.reduce((1, 2, -2, -1, 3)) == (3,)
    assert group.mul((1, 2), (-2, -1)) == ()
    assert group.inv((1, -2, 3)) == (-3, 2, -1)


def test_exact_candidate_ledger_and_first_backtrack():
    audit = experiment.exact_candidate_audit(base_cutoff=8, chiral_cutoff=4)
    assert audit["all_base_traces_exact"]
    assert audit["all_mixed_closed_paths_tau_killed"]
    assert audit["formal_tau_determinant"]["log_series_exact"]
    first = audit["first_mixed_identity_contribution"]
    assert first["length"] == 2
    assert first["mixed_identity_extra"] == "2*(y01**2 + y10**2 + y12**2 + y21**2)"


def test_inverse_pair_fails_but_positive_abelian_passes():
    controls = experiment.label_controls(cutoff=4, seed_count=2)
    assert controls["inverse_paired_free_labels"]["first_mixed_identity"]["length"] == 2
    assert controls["positive_free_abelian_Z_labels"]["first_mixed_identity"] is None


def test_finite_group_regular_trace_identity():
    audit = experiment.finite_regular_s3_audit()
    assert audit["max_trace_residual"] == 0.0
    assert next(row for row in audit["rows"] if row["length"] == 4)["mixed_identity_count"] == 2


def test_endpoint_gauges_and_midpoint_motion():
    rows = experiment.endpoint_alpha_sweep()["rows"]
    by_alpha = {row["alpha"]: row for row in rows}
    assert not by_alpha[0.0]["motion"]
    assert not by_alpha[1.0]["motion"]
    assert by_alpha[0.5]["motion"]


def test_word_ball_finite_determinant_and_root_moment():
    row = experiment.word_ball_row(2, 2, 0.0, 0.5, 0.25 + 0.0j)
    assert abs(row["finite_logabsdet_error_vs_euler"]) < 1e-12
    d0, d1 = 2 ** -0.5, 3 ** -0.5
    c = (d0 + d1) / 2
    expected_gram_trace = d0**2 + d1**2 + 2 * c**2
    assert abs(row["root_tau_gram"] - expected_gram_trace) < 1e-12
    assert row["ordinary_eigen_max_distance_from_loop_values"] < 1e-12


def test_numeric_chiral_second_moment_formula():
    group = experiment.FreeGroup()
    masses = [2, 3, 5]
    labels = experiment.positive_chain_labels(3)
    height, alpha = 1.7, 0.5
    edges = experiment.numeric_chain_edges(masses, height, alpha, labels, group)
    block = experiment.numeric_chiral_edges(edges, 3, group)
    got = experiment.numeric_tau_trace(block, 6, 2, group).real
    expected = 2 * sum(abs(edge.coefficient) ** 2 for edge in edges)
    assert abs(got - expected) < 1e-12
