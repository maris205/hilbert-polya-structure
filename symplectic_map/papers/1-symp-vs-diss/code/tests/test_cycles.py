import numpy as np

from symplectic_henon.cycles import (
    binary_primitive_orbit_count,
    build_orbit_ledger,
    cyclic_jacobian,
    cyclic_residual,
    numerical_minimal_period,
    primitive_binary_necklaces,
)


def test_binary_primitive_necklace_counts() -> None:
    expected = [2, 1, 2, 3, 6, 9, 18, 30, 56, 99]
    assert [binary_primitive_orbit_count(period) for period in range(1, 11)] == expected
    assert [len(primitive_binary_necklaces(period)) for period in range(1, 11)] == expected


def test_cyclic_jacobian_matches_finite_difference_for_small_period_collisions() -> None:
    for q in (np.array([0.3]), np.array([0.3, -0.4]), np.array([0.3, -0.4, 0.2])):
        a, rho = 1.7, 0.43
        epsilon = 1e-7
        finite_difference = np.column_stack(
            [
                (
                    cyclic_residual(q + epsilon * np.eye(q.size)[axis], a, rho)
                    - cyclic_residual(q - epsilon * np.eye(q.size)[axis], a, rho)
                )
                / (2.0 * epsilon)
                for axis in range(q.size)
            ]
        )
        assert np.allclose(cyclic_jacobian(q, a, rho), finite_difference, atol=2e-9)


def test_numerical_minimal_period() -> None:
    assert numerical_minimal_period([1.0, -1.0, 1.0, -1.0]) == 2
    assert numerical_minimal_period([1.0, -1.0, 0.5, -0.2]) == 4


def test_high_a_positive_control_matches_full_binary_shift_through_period_eight() -> None:
    ledger = build_orbit_ledger(
        a=6.0,
        rho=1.0,
        max_period=8,
        regime="full_shift_positive_control",
    )
    assert ledger["all_binary_counts_match"]
    assert ledger["completeness_status"] == "validated_against_binary_necklace_counts"
    for period_record in ledger["periods"]:
        assert period_record["orbits_found"] == period_record["binary_primitive_necklaces"]
        for orbit in period_record["orbits"]:
            assert orbit["residual_inf"] < 1e-9
            assert orbit["monodromy_determinant"] == 1.0
            # The direct determinant is only a conditioning diagnostic; the
            # exact local-product identity above is the invariant check.
            assert np.isfinite(orbit["monodromy_determinant_direct_absolute_error"])


def test_uc_ledger_is_never_labeled_complete() -> None:
    ledger = build_orbit_ledger(
        a=1.5436890126920763,
        rho=1.0,
        max_period=3,
        regime="exploratory_incomplete",
    )
    assert ledger["completeness_status"] == "incomplete_binary_seed_exploration_no_completeness_claim"
    assert not ledger["external_arithmetic_data_used"]
