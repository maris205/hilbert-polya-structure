#!/usr/bin/env python3
"""Regression tests for the exact HCS-C15 certificates."""

from __future__ import annotations

import cmath
from fractions import Fraction
import unittest

import sympy as sp

from independent_check import (
    cyclic_bigrams as independent_cyclic_bigrams,
    cyclically_reduced as independently_cyclically_reduced,
    dihedrally_equivalent as independently_dihedrally_equivalent,
    inverse as independent_group_inverse,
    primitive_word as independently_primitive_word,
    word_value as independent_word_value,
)
from voltage_zeta import (
    d4_certificates,
    dihedrally_equivalent,
    heisenberg_certificates,
    heisenberg_holonomy,
    heisenberg_tower_certificates,
    positive_unit_roof_zero_count,
    rational_schrodinger_certificate_q243,
)


class VoltageZetaTests(unittest.TestCase):
    def test_d4_factorization(self) -> None:
        result = d4_certificates()
        self.assertTrue(result["factorization_exact"])
        self.assertEqual(result["unit_roof_degree"], 8)

    def test_heisenberg_chronology(self) -> None:
        result = heisenberg_certificates(7)
        self.assertEqual(result["directed_parikh"], {"x": 3, "X": 3, "y": 2, "Y": 2})
        self.assertEqual(result["holonomies"], [[0, 0, 3], [0, 0, 2]])
        self.assertEqual(sum(result["cyclic_directed_bigram_counts"].values()), 10)
        self.assertFalse(result["dihedrally_equivalent"])
        self.assertTrue(result["aggregated_factors_equal"])
        self.assertTrue(result["resolved_sectors_distinguish"])

    def test_general_prime_at_least_seven_witness(self) -> None:
        for prime in (7, 11, 13):
            self.assertEqual(heisenberg_holonomy("XXXyxxyxYY", prime), (0, 0, prime - 4))
            self.assertEqual(heisenberg_holonomy("XXXyxyxxYY", prime), (0, 0, prime - 5))
        self.assertFalse(dihedrally_equivalent("XXXyxxyxYY", "XXXyxyxxYY"))

    def test_independent_h7_word_certificate(self) -> None:
        left_word = "XXXyxxyxYY"
        right_word = "XXXyxyxxYY"
        self.assertTrue(independently_cyclically_reduced(left_word))
        self.assertTrue(independently_cyclically_reduced(right_word))
        self.assertTrue(independently_primitive_word(left_word))
        self.assertTrue(independently_primitive_word(right_word))
        self.assertFalse(independently_dihedrally_equivalent(left_word, right_word))
        self.assertEqual(
            independent_cyclic_bigrams(left_word), independent_cyclic_bigrams(right_word)
        )
        left = independent_word_value(left_word, 7)
        right = independent_word_value(right_word, 7)
        self.assertNotEqual(left, independent_group_inverse(right, 7))

    def test_conductor_new_branch_return(self) -> None:
        result = heisenberg_tower_certificates(3, 5)
        rows = result["rows"]
        self.assertFalse(rows[0]["violates_ramanujan_bound"])
        self.assertTrue(all(row["violates_ramanujan_bound"] for row in rows[1:]))
        self.assertGreater(rows[-1]["adjacency_eigenvalue"], rows[-2]["adjacency_eigenvalue"])
        self.assertTrue(rows[-1]["schrodinger_bound_violates_ramanujan"])
        self.assertGreater(rows[-1]["schrodinger_rayleigh_lower_bound"], 3.7)
        self.assertIn("abelian_bass_roots", rows[-1])
        self.assertNotIn("bass_roots", rows[-1])

    def test_q243_exact_rational_rayleigh_certificate(self) -> None:
        certificate = rational_schrodinger_certificate_q243()
        lower_bound = Fraction(certificate["rayleigh_lower_bound_fraction"])
        excess = Fraction(certificate["excess_over_7_over_2_fraction"])
        self.assertEqual(lower_bound, Fraction(769442, 203391))
        self.assertEqual(excess, Fraction(115147, 406782))
        self.assertGreater(lower_bound, Fraction(7, 2))
        self.assertGreater(Fraction(7, 2) ** 2, 12)
        tower = heisenberg_tower_certificates(3, 5)
        self.assertEqual(tower["rational_schrodinger_certificate_q243"], certificate)

    def test_q9_schrodinger_representation_and_scalar_commutant(self) -> None:
        q = 9
        omega = cmath.exp(-2j * cmath.pi / q)
        tolerance = 2e-12

        def matrix_multiply(
            left: tuple[tuple[complex, ...], ...],
            right: tuple[tuple[complex, ...], ...],
        ) -> tuple[tuple[complex, ...], ...]:
            result = [[0j for _ in range(q)] for _ in range(q)]
            for row in range(q):
                for middle in range(q):
                    coefficient = left[row][middle]
                    if abs(coefficient) <= tolerance:
                        continue
                    for column in range(q):
                        result[row][column] += coefficient * right[middle][column]
            return tuple(tuple(row) for row in result)

        def matrix_max_error(
            left: tuple[tuple[complex, ...], ...],
            right: tuple[tuple[complex, ...], ...],
        ) -> float:
            return max(
                abs(left[row][column] - right[row][column])
                for row in range(q)
                for column in range(q)
            )

        # U e_j=e_{j+1} and V e_j=omega^{-j}e_j, so UV=omega VU.
        shift = tuple(
            tuple(1 + 0j if row == (column + 1) % q else 0j for column in range(q))
            for row in range(q)
        )
        phase_eigenvalues = tuple(omega ** (-index) for index in range(q))
        phase = tuple(
            tuple(
                phase_eigenvalues[row] if row == column else 0j
                for column in range(q)
            )
            for row in range(q)
        )
        shift_phase = matrix_multiply(shift, phase)
        omega_phase_shift = tuple(
            tuple(omega * value for value in row)
            for row in matrix_multiply(phase, shift)
        )
        self.assertLess(matrix_max_error(shift_phase, omega_phase_shift), tolerance)

        def rho(a: int, b: int, c: int) -> tuple[tuple[complex, ...], ...]:
            # rho(a,b,c)=omega^c V^b U^a for
            # (a,b,c)(a',b',c')=(a+a',b+b',c+c'+a*b').
            matrix = [[0j for _ in range(q)] for _ in range(q)]
            for column in range(q):
                row = (column + a) % q
                matrix[row][column] = omega ** ((c - b * row) % q)
            return tuple(tuple(row) for row in matrix)

        def group_multiply(
            left: tuple[int, int, int], right: tuple[int, int, int]
        ) -> tuple[int, int, int]:
            a, b, c = left
            aa, bb, cc = right
            return ((a + aa) % q, (b + bb) % q, (c + cc + a * bb) % q)

        elements = [
            (a, b, c) for a in range(q) for b in range(q) for c in range(q)
        ]
        representation = {element: rho(*element) for element in elements}
        generators = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        for element in elements:
            for generator in generators:
                product = matrix_multiply(
                    representation[element], representation[generator]
                )
                expected = representation[group_multiply(element, generator)]
                self.assertLess(matrix_max_error(product, expected), tolerance)

        representatives = (
            (0, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (8, 0, 0),
            (0, 8, 0),
            (2, 3, 4),
            (5, 7, 8),
        )
        for left in representatives:
            for right in representatives:
                product = matrix_multiply(representation[left], representation[right])
                expected = representation[group_multiply(left, right)]
                self.assertLess(matrix_max_error(product, expected), tolerance)

        # Explicit scalar-commutant criterion: V has simple spectrum, so a
        # commuting matrix is diagonal; U is one q-cycle, so all of those
        # diagonal entries must be equal.
        for left_index in range(q):
            for right_index in range(left_index + 1, q):
                self.assertGreater(
                    abs(phase_eigenvalues[left_index] - phase_eigenvalues[right_index]),
                    tolerance,
                )
        shift_orbit = []
        current = 0
        while current not in shift_orbit:
            shift_orbit.append(current)
            current = (current + 1) % q
        self.assertEqual(shift_orbit, list(range(q)))
        self.assertEqual(current, 0)
        commutant_dimension = 1  # one diagonal value on the unique shift orbit
        self.assertEqual(commutant_dimension, 1)

    def test_unit_roof_count_is_linear(self) -> None:
        result = d4_certificates()
        angles = result["unit_roof_root_arguments"]
        count_one = positive_unit_roof_zero_count(angles, 10_000.0)
        count_two = positive_unit_roof_zero_count(angles, 20_000.0)
        self.assertLessEqual(abs(count_two - 2 * count_one), 16)

    def test_bivariate_determinant_constant_term(self) -> None:
        x, y = sp.symbols("x y")
        result = d4_certificates()
        polynomial = sp.sympify(result["two_dimensional_weighted_determinant"])
        self.assertEqual(sp.expand(polynomial).subs({x: 0, y: 0}), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
