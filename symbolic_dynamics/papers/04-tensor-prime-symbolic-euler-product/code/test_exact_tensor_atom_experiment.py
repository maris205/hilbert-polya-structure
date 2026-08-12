#!/usr/bin/env python3
"""Regression tests for the exact tensor-atom experiment."""

from __future__ import annotations

import math
import unittest

from exact_tensor_atom_experiment import (
    RegistrySpec,
    build_public_registry,
    euler_coefficients,
    free_word_coefficients,
    free_word_log_derivative_coefficients,
    inverse_euler_coefficients,
    is_prime_for_scoring_only,
    log_derivative_coefficients,
    mobius_for_scoring_only,
    recover_from_registered_data,
    von_mangoldt_for_scoring_only,
)


class TensorAtomExperimentTest(unittest.TestCase):
    def recover_tensor_atoms(self, cutoff: int) -> list[int]:
        spec = RegistrySpec(
            name=f"test_tensor_N{cutoff}",
            labels=tuple(range(1, cutoff + 1)),
            unit_label=1,
            operation=lambda a, b: a * b,
        )
        public, _ = build_public_registry(spec)
        recovered = recover_from_registered_data(public)
        self.assertEqual(recovered["unique_factorization_fraction"], 1.0)
        self.assertEqual(recovered["operation_weight_multiplicativity_fraction"], 1.0)
        self.assertEqual(recovered["fixed_point_tensor_identity_fraction"], 1.0)
        return recovered["atom_weights"]

    def test_opaque_tensor_atoms_equal_primes(self) -> None:
        atoms = self.recover_tensor_atoms(128)
        expected = [n for n in range(2, 129) if is_prime_for_scoring_only(n)]
        self.assertEqual(atoms, expected)

    def test_exact_euler_mobius_and_von_mangoldt_prefix(self) -> None:
        cutoff = 128
        atoms = self.recover_tensor_atoms(cutoff)
        zeta = euler_coefficients(atoms, cutoff)
        determinant = inverse_euler_coefficients(atoms, cutoff)
        logderivative = log_derivative_coefficients(atoms, cutoff)
        self.assertEqual(zeta[1:], [1] * cutoff)
        self.assertEqual(
            determinant[1:], [mobius_for_scoring_only(n) for n in range(1, cutoff + 1)]
        )
        for n in range(1, cutoff + 1):
            self.assertAlmostEqual(
                logderivative[n], von_mangoldt_for_scoring_only(n), places=13
            )

    def test_no_mixing_positive_control(self) -> None:
        for p, q in [(2, 3), (2, 5), (3, 7), (5, 11)]:
            cutoff = p * q
            diagonal_zeta = euler_coefficients([p, q], cutoff)
            diagonal_logderivative = log_derivative_coefficients([p, q], cutoff)
            free_zeta = free_word_coefficients([p, q], cutoff)
            free_logderivative = free_word_log_derivative_coefficients([p, q], cutoff)
            self.assertEqual(diagonal_zeta[p * q], 1)
            self.assertEqual(diagonal_logderivative[p * q], 0.0)
            self.assertEqual(free_zeta[p * q], 2)
            self.assertAlmostEqual(free_logderivative[p * q], math.log(p * q), places=13)

    def test_shifted_law_breaks_intrinsic_full_shift_invariants(self) -> None:
        cutoff = 64
        spec = RegistrySpec(
            name="test_shifted",
            labels=tuple(range(2, cutoff + 1)),
            unit_label=2,
            operation=lambda a, b: (a - 1) * (b - 1) + 1,
        )
        public, _ = build_public_registry(spec)
        recovered = recover_from_registered_data(public)
        self.assertEqual(recovered["unique_factorization_fraction"], 1.0)
        self.assertEqual(recovered["operation_weight_multiplicativity_fraction"], 0.0)
        self.assertGreater(recovered["max_operation_entropy_additivity_error"], 0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
