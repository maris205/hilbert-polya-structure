import cmath
import math

import numpy as np

from sdc15_character_holonomy_experiment import (
    CHARACTER_COUNT,
    POSITIVE_CHARGE_SEEDS,
    charged_path_census,
    coefficient_energy,
    continuant_polynomial,
    dense_determinant,
    dft_coefficient_residual,
    euler_constant_coefficient,
    evaluate_polynomial,
    first_composites,
    first_primes,
    frozen_positive_charge_rows,
    forward_dag_determinant_polynomial,
    gauge_residual,
    inventory,
    inverse_charges,
    masses,
    positive_charge_field,
    primary_charges,
    roof_shift_residual,
    trace_log_reconstruction,
    summary,
)


def test_frozen_inventory_algorithms():
    assert first_primes(5) == (2, 3, 5, 7, 11)
    assert first_composites(6) == (4, 6, 8, 9, 10, 12)
    assert len(inventory("shuffled_primes", 128)) == 128
    assert set(inventory("shuffled_primes", 128)) == set(first_primes(128))
    random_values = inventory("random_increasing", 32)
    assert random_values == tuple(sorted(random_values))
    assert len(set(random_values)) == 32
    assert min(random_values) >= 2 and max(random_values) < 16 * 32 + 2


def test_two_atom_primary_formula():
    x, y, z = 0.25, 0.125, 0.35
    a = (x + y) / 2
    poly = continuant_polynomial((x, y), z, *primary_charges(2))
    assert set(poly) == {0, 2}
    assert abs(poly[0] - (1 - z * x) * (1 - z * y)) < 1e-15
    assert abs(poly[2] + z * z * a * a) < 1e-15


def test_continuant_matches_dense_determinant():
    values = inventory("primes", 8)
    xs = masses(values, 1.5 + 0.75j)
    charges = primary_charges(8)
    poly = continuant_polynomial(xs, 0.6, *charges)
    for index in (0, 1, 127, 255, 511, 777):
        w = cmath.exp(2j * math.pi * index / CHARACTER_COUNT)
        expected = dense_determinant(xs, 0.6, w, *charges)
        actual = evaluate_polynomial(poly, w)
        assert abs(actual - expected) < 2e-13


def test_trace_log_dft_and_high_precision_audits_are_small():
    result = summary()["selected_determinant_audit"]
    assert result["dense_residual"] < 2e-13
    assert result["trace_power_64_residual"] < 2e-13
    assert result["high_precision_80_digit_residual"] < 2e-13
    assert result["dft_coefficient_residual"] < 2e-13


def test_primary_d0_is_exact_euler_and_energy_nonzero():
    for kind in ("primes", "composites", "shuffled_primes", "random_increasing"):
        xs = masses(inventory(kind, 32), 1.5 + 0j)
        poly = continuant_polynomial(xs, 0.35, *primary_charges(32))
        assert abs(poly[0] - euler_constant_coefficient(xs, 0.35)) < 1e-15
        assert coefficient_energy(poly) > 1e-8


def test_random_positive_charges_preserve_d0_but_have_nonzero_energy():
    xs = masses(inventory("primes", 32), 1.5 + 0j)
    for seed in POSITIVE_CHARGE_SEEDS:
        charges = positive_charge_field(32, seed)
        assert all(charge in (1, 2, 3) for side in charges for charge in side)
        poly = continuant_polynomial(xs, 0.35, *charges)
        assert abs(poly[0] - euler_constant_coefficient(xs, 0.35)) < 1e-15
        assert coefficient_energy(poly) > 1e-8


def test_full_positive_charge_control_matrix_is_frozen_and_nonzero():
    rows = frozen_positive_charge_rows()
    assert len(rows) == 8 * 4 * 3 * 32
    assert all(row["d0_residual"] == 0 for row in rows)
    assert all(row["E"] > 0 for row in rows)
    assert max(row["degree"] for row in rows) < CHARACTER_COUNT


def test_inverse_charge_moves_two_cycle_into_degree_zero():
    xs = masses(first_primes(2), 2 + 0j)
    primary = continuant_polynomial(xs, 0.35, *primary_charges(2))
    inverse = continuant_polynomial(xs, 0.35, *inverse_charges(2))
    assert set(primary) == {0, 2}
    assert set(inverse) == {0}
    assert abs(inverse[0] - euler_constant_coefficient(xs, 0.35)) > 1e-8


def test_forward_dag_collapses_exactly():
    xs = masses(first_primes(32), 1.5 + 0j)
    poly = forward_dag_determinant_polynomial(xs, 0.35)
    assert set(poly) == {0}
    assert coefficient_energy(poly) == 0


def test_exact_path_census_positive_and_inverse():
    for count in (2, 3, 4, 5):
        values = first_primes(count)
        positive = charged_path_census(values, 12, *primary_charges(count))
        inverse = charged_path_census(values, 12, *inverse_charges(count))
        assert not any(not row["pure"] and row["charge"] == 0 for row in positive)
        inverse_zero_mixed = [
            row for row in inverse if not row["pure"] and row["charge"] == 0
        ]
        assert min(row["r"] for row in inverse_zero_mixed) == 2


def test_rank_entropy_gauge_and_roof_shift_controls():
    values = first_primes(8)
    for kind in ("rank", "entropy"):
        assert gauge_residual(values, 1.5 + 0.75j, 0.713, kind) < 2e-15
    assert max(roof_shift_residual(value, 1.5 + 0.75j, 0.713) for value in values) < 2e-15


def test_frozen_summary_forces_specificity_stop():
    result = summary()
    assert result["zero_data_used"] is False
    assert result["decision"] == {
        "GO_CHARACTER_RESOLUTION": True,
        "GO_ARITHMETIC_SELECTIVITY": False,
        "STOP_ARITHMETIC_SELECTIVITY": True,
        "STOP_TIME_REVERSAL": True,
        "PROVES_TOO_MUCH": True,
    }
    assert all(item["E"] > 1e-8 for item in result["selectivity"].values())
    assert all(item["E"] > 1e-8 for item in result["positive_charge_controls"])
