import numpy as np

import sdc14_haar_fiber_experiment as experiment


def test_intrinsic_atoms():
    assert experiment.internal_multiplicative_atoms(8) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_haar_moments_and_normalization():
    for c in [0.25, 1.0, 3.0]:
        assert experiment.haar_moment(c, 0) == 1 + c
        for repetition in range(1, 33):
            assert experiment.haar_moment(c, repetition) == 1
            assert experiment.haar_moment(c, repetition, True) == 1 / (1 + c)


def test_all_cyclic_approximants_first_leak_at_order():
    audit = experiment.cyclic_approximant_audit(64, 128)
    assert audit["all_first_leaks_exact"]
    assert [row["first_leak_repetition"] for row in audit["summary_rows"]] == list(range(2, 65))


def test_cyclic_determinant_formula_direct_roots():
    q, c = 0.61 + 0.12j, 1.0
    for order in [2, 3, 5, 8, 16, 32, 64]:
        roots = np.exp(2j * np.pi * np.arange(order) / order)
        direct = (1 - q) * np.exp(
            (c / order) * np.sum(np.log(1 - q * roots))
        )
        formula = (1 - q) * np.exp((c / order) * np.log1p(-(q**order)))
        assert abs(direct - formula) < 1e-11


def test_haar_analytic_and_fk_formulas():
    audit = experiment.haar_formula_audit()
    assert all(
        abs(complex(row["analytic_D_real"], row["analytic_D_imag"]) - (1 - row["q_abs"] * np.exp(1j * row["q_arg"]))) < 1e-12
        for row in audit["rows"]
    )
    assert max(row["fk_quadrature_residual"] for row in audit["rows"]) < 1e-10


def test_density_first_fourier_leak():
    audit = experiment.density_perturbation_audit(32)
    assert audit["all_first_leaks_exact"]
    assert all(row["density_nonnegative"] for row in audit["rows"])


def test_selfadjoint_square_control():
    audit = experiment.selfadjoint_audit(8)
    assert audit["first_even_leak_power"] == 2
    assert all(row["odd_zero"] for row in audit["rows"] if row["power"] % 2)
    assert all(row["H2_identity"] for row in audit["rows"] if row["power"] == 2)


def test_balanced_inverse_word_survives():
    audit = experiment.balanced_word_audit()
    assert audit["nonzero"]
    assert audit["word"] == "u*u^(-1)=1"


def test_all_inventories_are_analytic_determinant_blind():
    audit = experiment.inventory_controls(32)
    assert audit["all_determinant_blind"]
    assert all(row["analytic_difference"] == 0 for row in audit["rows"])
    assert all(row["phase_log_D_range"] == 0 for row in audit["rows"])
