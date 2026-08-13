import numpy as np

import sdc13_unitary_fiber_experiment as experiment


def test_intrinsic_atoms():
    assert experiment.internal_multiplicative_atoms(8) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_cycle_moment_formula_m2_to_m8():
    audit = experiment.moment_family_audit(32)
    assert audit["cycle_exact_max_residual"] < 1e-12
    for size in range(2, 9):
        rows = [
            row
            for row in audit["rows"]
            if row["name"] == f"cycle_m{size}"
        ]
        assert next(row for row in rows if row["repetition"] == size)["tau_real"] == 1
        assert abs(next(row for row in rows if row["repetition"] == 1)["tau_real"]) < 1e-12


def test_normalized_positive_rigidity_identity():
    audit = experiment.rigidity_audit(seed_count=4)
    assert audit["max_rigidity_formula_residual"] < 1e-12
    assert all(
        not row["tau_equals_one"]
        for row in audit["random_positive_rows"]
        if row["nontrivial"]
    )


def test_ordinary_newton_rigidity():
    rows = experiment.rigidity_audit(seed_count=1)["ordinary_rows"]
    assert rows[0]["compatible"]
    assert all(not row["compatible"] for row in rows[1:])
    assert all(row["forced_determinant"] == "0" for row in rows[1:])


def test_nonfaithful_and_graded_controls():
    audit = experiment.hidden_and_graded_audit(16)
    assert max(row["state_moment_max_error"] for row in audit["rows"]) < 1e-12
    assert max(row["graded_supertrace_max_error"] for row in audit["rows"]) < 1e-12
    assert max(row["graded_berezinian_residual"] for row in audit["rows"]) < 1e-12
    assert max(row["ordinary_even_det_motion_visible"] for row in audit["rows"]) > 1e-3


def test_triangle_roots_of_unity_only_delay():
    audit = experiment.recurrence_audit(32)
    for size in range(2, 9):
        rows = [
            row
            for row in audit["triangle_rows"]
            if row["fiber_cycle_size"] == size
        ]
        first = next(row for row in rows if row["survives"])
        assert first["primitive_repetition"] == size
        assert first["transfer_power"] == 3 * size


def test_parallel_independent_variables_do_not_cancel():
    audit = experiment.recurrence_audit(8)
    assert all(row["independent_nonzero"] for row in audit["parallel_rows"])
    assert not next(
        row for row in audit["parallel_rows"] if row["repetition"] == 1
    )["equal_path_survives"]
    assert next(
        row for row in audit["parallel_rows"] if row["repetition"] == 2
    )["equal_path_survives"]


def test_entropy_and_matched_clock_controls():
    audit = experiment.entropy_clock_controls(atom_count=16, seed_count=4)
    assert audit["motion_pass_count_by_inventory"] == {
        "tensor_primes": 12,
        "composites": 12,
        "random_increasing": 12,
    }
    assert all(not row["ledger_exact_all_r_to_32"] for row in audit["rows"])


def test_cycle_determinant_formula():
    z = 0.31 + 0.12j
    for size in range(2, 9):
        theta = 0.73
        unitary = experiment.cycle_unitary(size, theta)
        got = np.linalg.det(np.eye(size) - z * unitary)
        expected = 1 - np.exp(1j * theta) * z**size
        assert abs(got - expected) < 1e-12
