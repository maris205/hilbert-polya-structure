#!/usr/bin/env python3
"""Regression and mutation tests for the HCS-C27 exact release."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c27_certificate.json"
INDEPENDENT = PROJECT / "results" / "c27_independent_check.json"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(specification)
    assert specification.loader is not None
    specification.loader.exec_module(module)
    return module


producer = load_module("c27_release_producer", PROJECT / "code" / "c27_producer.py")


class C27Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        cls.c24 = json.loads(producer.C24_PATH.read_text(encoding="utf-8"))
        cls.c26 = json.loads(producer.C26_PATH.read_text(encoding="utf-8"))
        cls.matrices = producer.c26_matrices(cls.c26)

    def test_source_hashes_are_frozen(self) -> None:
        observed = {
            "C24": producer.sha256(producer.C24_PATH),
            "C25": producer.sha256(producer.C25_PATH),
            "C26": producer.sha256(producer.C26_PATH),
        }
        self.assertEqual(observed, producer.EXPECTED_SOURCE_HASHES)

    def test_integral_darboux_basis_and_symplectic_targets(self) -> None:
        self.assertEqual(producer.DARBOUX_T.det(), -1)
        self.assertEqual(producer.DARBOUX_T.T * producer.J_C26 * producer.DARBOUX_T, producer.J_STANDARD)
        for matrix in self.matrices.values():
            self.assertEqual(matrix.T * producer.J_C26 * matrix, producer.J_C26)

    def test_later_on_left_chronology_is_literal(self) -> None:
        forward = self.matrices["third_branch"] * self.matrices["second_branch"] * self.matrices["gamma_star"]
        reverse = self.matrices["gamma_star"] * self.matrices["second_branch"] * self.matrices["third_branch"]
        self.assertEqual(forward, self.matrices["three_forward"])
        self.assertEqual(reverse, self.matrices["three_reverse"])
        self.assertNotEqual(forward, reverse)

    def test_transpose_and_average_mutations_are_not_the_fibre_cocycle(self) -> None:
        forward = self.matrices["three_forward"]
        self.assertNotEqual(forward.T, forward)
        self.assertNotEqual(forward.T.T * producer.J_C26 * forward.T, producer.J_C26)
        average = (forward + self.matrices["three_reverse"]) / 2
        self.assertTrue(any(value.q != 1 for value in average))
        self.assertNotEqual(average.T * producer.J_C26 * average, producer.J_C26)

    def test_character_is_evaluated_after_product_not_branchwise(self) -> None:
        p = 5
        gamma = tuple(Fraction(value) for value in producer.character_key(self.matrices["gamma_star"], producer.J_C26, p))
        second = tuple(Fraction(value) for value in producer.character_key(self.matrices["second_branch"], producer.J_C26, p))
        branchwise_product = producer.pair_multiply(second, gamma, p)
        chronological_character = tuple(
            Fraction(value) for value in producer.character_key(self.matrices["two_forward"], producer.J_C26, p)
        )
        self.assertNotEqual(branchwise_product, chronological_character)

    def test_two_return_is_a_required_trace_cyclicity_null_control(self) -> None:
        control = self.data["c26_chronology_controls"]["two_return_null_control"]
        self.assertTrue(control["integer_matrices_different"])
        self.assertTrue(control["characteristic_polynomials_equal"])
        for p in (3, 5, 7, 11, 43):
            self.assertEqual(
                producer.character_key(self.matrices["two_forward"], producer.J_C26, p),
                producer.character_key(self.matrices["two_reverse"], producer.J_C26, p),
            )

    def test_three_return_small_prime_signal_is_exact(self) -> None:
        expected = {
            "3": ([1, 0], [0, 1]),
            "5": ([-1, 0], [1, 0]),
            "7": ([-1, 0], [0, -1]),
        }
        for prime, (forward, reverse) in expected.items():
            record = self.data["small_prime_exact_characters"][prime]
            self.assertEqual(record["characters"]["three_forward"]["exact_pair_one_gauss"], forward)
            self.assertEqual(record["characters"]["three_reverse"]["exact_pair_one_gauss"], reverse)
            self.assertTrue(record["three_forward_differs_from_reverse"])

    def test_Thomas_absolute_value_identity(self) -> None:
        for p in (3, 5, 7, 11):
            for matrix in self.matrices.values():
                record = producer.thomas_character(matrix, producer.J_C26, p)
                self.assertEqual(record["absolute_value_squared"], p ** record["kernel_dimension"])

    def test_identity_character_and_even_prime_rejection(self) -> None:
        for p in (3, 5, 7):
            self.assertEqual(
                producer.thomas_character(sp.eye(4), producer.J_C26, p)["exact_pair_one_gauss"],
                [p * p, 0],
            )
        with self.assertRaises(ValueError):
            producer.thomas_character(sp.eye(4), producer.J_C26, 2)

    def test_good_prime_formula_and_singular_prime_mutation(self) -> None:
        gamma = self.matrices["gamma_star"]
        discriminant = producer.discriminant_at_one(gamma)
        self.assertNotEqual(discriminant % 13, 0)
        self.assertEqual(
            producer.character_key(gamma, producer.J_C26, 13),
            (producer.legendre(discriminant, 13), 0),
        )
        singular = self.data["c24_controls"]["singular_prime_positive_control"]
        self.assertEqual(singular["common_det_I_minus_g"] % 3, 0)
        self.assertNotEqual(singular["left_character"]["exact_pair_one_gauss"], [0, 0])

    def test_repetition_character_is_not_character_power(self) -> None:
        p = 3
        matrix = producer.matrix_mod(self.matrices["gamma_star"], p)
        theta = tuple(Fraction(value) for value in producer.character_key(matrix, producer.J_C26, p))
        theta_squared = producer.pair_multiply(theta, theta, p)
        theta_of_square = tuple(
            Fraction(value)
            for value in producer.character_key(producer.matmul_mod(matrix, matrix, p), producer.J_C26, p)
        )
        self.assertNotEqual(theta_squared, theta_of_square)

    def test_local_polynomials_have_full_fibre_degree_and_reciprocity(self) -> None:
        for prime in ("3", "5", "7"):
            p = int(prime)
            record = self.data["exact_local_weil_polynomials"][prime]
            for side in ("three_forward", "three_reverse"):
                polynomial = record[side]
                self.assertEqual(polynomial["degree"], p * p)
                self.assertEqual(len(polynomial["coefficients_one_gauss"]), p * p + 1)
                self.assertEqual(polynomial["leading_coefficient"], ["-1", "0"])
                self.assertTrue(polynomial["conjugate_reciprocity_verified"])
            self.assertTrue(record["polynomials_different"])

    def test_p43_is_a_complete_fibre_polynomial_collision_not_a_cutoff_guess(self) -> None:
        collision = self.data["p43_complete_weil_fibre_polynomial_collision"]
        self.assertEqual(collision["left_matrix_order"], 925)
        self.assertEqual(collision["right_matrix_order"], 925)
        self.assertEqual(collision["first_common_identity_power"], 925)
        self.assertTrue(collision["all_power_characters_equal"])
        self.assertTrue(collision["base_characteristic_polynomials_different_mod_p"])
        self.assertTrue(collision["complete_period_proof"])

    def test_short_power_window_cannot_be_promoted_to_universal_separation(self) -> None:
        scan = self.data["c26_power_character_scan"]
        self.assertEqual(scan["different_comparisons"], 328)
        self.assertEqual(scan["equal_comparisons"], 248)
        self.assertEqual(scan["per_prime"]["83"]["first_different_power"], None)
        self.assertLess(scan["maximum_power"], 41)
        late = self.data["c26_post_window_separation_controls"]
        self.assertEqual(late["83"]["first_different_power"], 41)
        self.assertEqual(late["89"]["first_different_power"], 30)
        self.assertTrue(late["83"]["characters_equal_through_short_window"])
        self.assertTrue(late["89"]["characters_equal_through_short_window"])

    def test_integral_symplectic_conjugacy_collapse(self) -> None:
        control = self.data["c24_controls"]["integral_symplectic_conjugacy_collapse"]
        left = sp.Matrix(control["left_matrix"])
        right = sp.Matrix(control["right_matrix"])
        form = sp.Matrix(self.data["c24_controls"]["source_form_J0"])
        conjugator = sp.Matrix(control["conjugator_X"])
        self.assertEqual(conjugator.det(), 1)
        self.assertEqual(conjugator.T * form * conjugator, form)
        self.assertEqual(right * conjugator, conjugator * left)
        mutated = conjugator.copy()
        mutated[0, 0] += 1
        self.assertFalse(mutated.T * form * mutated == form and right * mutated == mutated * left)

    def test_C24_symbolic_cycles_are_distinct_despite_conjugacy(self) -> None:
        control = self.data["c24_controls"]["integral_symplectic_conjugacy_collapse"]
        left_order = control["left_central_first_return_order"]
        right_order = control["right_central_first_return_order"]
        rotations = [left_order[offset:] + left_order[:offset] for offset in range(len(left_order))]
        self.assertTrue(control["same_branch_multiset"])
        self.assertTrue(control["not_cyclic_rotations"])
        self.assertNotIn(right_order, rotations)
        self.assertNotEqual(control["left_central_first_return_order"], control["right_central_first_return_order"])
        self.assertNotEqual(control["left_matrix"], control["right_matrix"])

    def test_singular_prime_refines_a_charpoly_collision(self) -> None:
        witness = self.data["c24_controls"]["singular_prime_positive_control"]
        self.assertEqual(witness["common_characteristic_coefficients"], [1, -9, 19, -9, 1])
        self.assertTrue(witness["characters_different"])
        self.assertEqual(witness["left_character"]["kernel_dimension"], 1)
        self.assertEqual(witness["right_character"]["kernel_dimension"], 1)
        self.assertNotEqual(
            witness["left_character"]["legendre_sigma_discriminant"],
            witness["right_character"]["legendre_sigma_discriminant"],
        )

    def test_arithmetic_scan_is_large_but_finitely_scoped(self) -> None:
        scan = self.data["agy_branch_arithmetic_scan"]
        self.assertEqual(scan["branch_count"], 150)
        self.assertEqual(scan["distinct_discriminants"], 150)
        self.assertEqual(scan["distinct_characteristic_polynomials"], 150)
        self.assertEqual(scan["distinct_legendre_signatures"], 150)
        self.assertTrue(scan["all_150_signatures_distinct"])
        self.assertFalse(scan["scope"]["finite_scan_is_all_length_theorem"])

    def test_fixed_prime_determinant_is_not_an_adelic_operator(self) -> None:
        theorem = self.data["finite_twist_theorem"]
        self.assertEqual(theorem["status"], "PROVED_BY_FINITE_TENSOR_EXTENSION_OF_C26_THEOREM_3_2")
        self.assertIn("p^2", theorem["space"])
        self.assertIn("no adelic Hilbert space", theorem["not_claimed"])
        self.assertEqual(self.data["decisions"]["intrinsic_global_Hilbert_Polya_gate"], "FAIL_MODULUS_P_REMAINS_EXTERNAL")

    def test_scope_firewall_and_independent_replay(self) -> None:
        self.assertFalse(any(self.data["scope_firewall"]["flags"].values()))
        independent = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
        self.assertEqual(independent["status"], "PASS")
        self.assertFalse(independent["independence"]["imports_c27_producer"])
        self.assertTrue(all(independent["checks"].values()))


if __name__ == "__main__":
    unittest.main()
