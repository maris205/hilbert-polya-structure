import numpy as np

import sdc12_relative_determinant_experiment as experiment


def test_internal_tensor_atoms():
    assert experiment.internal_multiplicative_atoms(8) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_exact_relative_log_coefficients():
    audit = experiment.exact_prefix_audit(pair_count=2, repetition_cutoff=8)
    assert audit["all_exact"]
    assert audit["log_series_exact"]
    assert "a0" in audit["relative_product"]
    assert "b0" in audit["relative_product"]


def test_trace_norm_and_rigorous_tail_bound():
    pair_count = 128
    values = np.asarray(
        experiment.internal_multiplicative_atoms(2 * pair_count + 1), dtype=float
    )
    pairs = experiment.adjacent_pairs(pair_count)
    s = 0.25 + 7j
    got = experiment.paired_trace_norm(values[:-1], pairs, s)
    bound = abs(s) / s.real * 2 ** (-s.real)
    assert got <= bound + 1e-12
    assert experiment.trace_tail_bound(s, values[-1]) > 0


def test_reflection_and_positive_motion_curvature():
    audit = experiment.reflection_audit(max_pairs=256)
    assert all(row["strict_motion"] for row in audit["rows"])
    assert min(row["log_H_second_derivative_t0"] for row in audit["rows"]) > 0
    assert max(row["reflection_residual"] for row in audit["symmetry_rows"]) < 1e-12


def test_primary_zero_free_strip():
    audit = experiment.zero_free_audit()
    assert audit["primary_z1_zero_free"]
    row = next(row for row in audit["rows"] if row["abs_z"] == 1.0)
    assert row["H_certified_strip_lower_sigma"] == 0.0
    assert row["H_certified_strip_upper_sigma"] == 1.0
    assert row["H_strip_nonempty"]


def test_shifted_and_random_pairing_controls():
    audit = experiment.pairing_inventory_controls(pair_count=128)
    assert audit["random_pairing_pass_count"] == 32
    assert audit["random_pairing_motion_count"] == 32
    offsets = [
        row for row in audit["rows"] if row["control_type"] == "offset_pairing"
    ]
    assert [row["name"] for row in offsets] == ["offset_1", "offset_2", "offset_3"]


def test_zero_sum_vs_positive_constraint():
    audit = experiment.block_weight_audit(max_blocks=128)
    rows = audit["rows"]
    assert all(
        row["zero_sum_condition"]
        for row in rows
        if "zero_sum" in row["pattern"] or row["pattern"] == "second_difference"
    )
    assert all(
        not row["zero_sum_condition"]
        for row in rows
        if row["all_positive"]
    )


def test_fixed_parity_is_not_repetition_phase():
    audit = experiment.parity_phase_audit(8)
    assert audit["coincide_only_at_odd_repetitions"]
    assert next(row for row in audit["rows"] if row["repetition"] == 1)["same"]
    assert not next(row for row in audit["rows"] if row["repetition"] == 2)["same"]


def test_relative_product_numeric_orientation():
    values = np.asarray([2.0, 3.0, 5.0, 7.0])
    pairs = experiment.adjacent_pairs(2)
    s, z = 0.4 + 1.2j, 0.3 + 0.1j
    direct = np.prod(
        [
            (1 - z * values[left] ** (-s)) / (1 - z * values[right] ** (-s))
            for left, right in pairs
        ]
    )
    assert abs(np.exp(experiment.log_relative(values, pairs, s, z)) - direct) < 1e-12
