from __future__ import annotations

import itertools

import numpy as np

from knauf import (
    analytic_liouville,
    analytic_unsigned,
    arithmetic_sieves,
    coefficient_histogram,
    complete_totient_prefix,
    h_value_matrix,
    h_value_recursive,
    h_values,
    splitmix64_state_signs,
)


def test_published_h3_ledger() -> None:
    expected = np.array([1, 4, 3, 5, 2, 5, 3, 4], dtype=np.int64)
    np.testing.assert_array_equal(h_values(3), expected)


def test_vector_recursion_against_two_scalar_implementations() -> None:
    for k in range(0, 9):
        vector = h_values(k)
        words = itertools.product((0, 1), repeat=k)
        for index, word in enumerate(words):
            recursive = h_value_recursive(word)
            matrix = h_value_matrix(word)
            assert recursive == matrix == int(vector[index])


def test_histogram_is_bounded_by_totient_and_has_expected_k3_prefix() -> None:
    hist = coefficient_histogram(h_values(3))
    phi, _, _ = arithmetic_sieves(int(h_values(3).max()))
    assert np.all(hist <= phi)
    assert complete_totient_prefix(hist, phi) == 4
    np.testing.assert_array_equal(hist[1:6], np.array([1, 1, 2, 2, 2]))


def test_linear_sieve_known_small_values() -> None:
    phi, liouville, mobius = arithmetic_sieves(12)
    np.testing.assert_array_equal(
        phi[1:13], np.array([1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4])
    )
    np.testing.assert_array_equal(
        liouville[1:13], np.array([1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1])
    )
    np.testing.assert_array_equal(
        mobius[1:13], np.array([1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0])
    )


def test_random_sign_control_is_reproducible_and_seeded() -> None:
    first = splitmix64_state_signs(4096, 2026081201, 12)
    repeat = splitmix64_state_signs(4096, 2026081201, 12)
    other_seed = splitmix64_state_signs(4096, 2026081202, 12)
    other_level = splitmix64_state_signs(4096, 2026081201, 13)
    np.testing.assert_array_equal(first, repeat)
    assert not np.array_equal(first, other_seed)
    assert not np.array_equal(first, other_level)
    assert set(np.unique(first)) == {-1, 1}


def test_weighted_histogram_preserves_exact_integer_mass() -> None:
    values = h_values(12)
    signs = splitmix64_state_signs(values.size, 2026081201, 12)
    hist = coefficient_histogram(values, signs)
    assert int(hist.sum()) == int(signs.sum())


def test_analytic_ratios_at_safe_real_point() -> None:
    unsigned = analytic_unsigned(3.0 + 0.0j)
    liouville = analytic_liouville(3.0 + 0.0j)
    assert unsigned is not None and abs(unsigned.imag) < 1e-15
    assert liouville is not None and abs(liouville.imag) < 1e-15
    assert 1.0 < unsigned.real < 2.0
    assert 0.0 < liouville.real < 1.0
    assert analytic_liouville(2.0 + 0.0j) == 0.0 + 0.0j
