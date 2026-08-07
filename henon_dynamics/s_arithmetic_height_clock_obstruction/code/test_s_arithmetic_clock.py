from __future__ import annotations

import math
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import independent_check
import s_arithmetic_clock as clock


class Quad3Tests(unittest.TestCase):
    def test_generator_norms_and_inverses(self):
        self.assertEqual(clock.EPSILON.norm(), 1)
        self.assertEqual(clock.PI.norm(), 13)
        self.assertEqual(clock.EPSILON * clock.EPSILON.inverse(), clock.Quad3(1))
        self.assertEqual(clock.PI * clock.PI.inverse(), clock.Quad3(1))

    def test_regular_matrix_representation(self):
        value = clock.Quad3(Fraction(7, 13), Fraction(-5, 13))
        matrix = value.matrix()
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        self.assertEqual(determinant, value.norm())

    def test_hilbert_symbols(self):
        self.assertEqual(clock.hilbert_symbol_two(-1, 3), -1)
        self.assertEqual(clock.hilbert_symbol_odd(-1, 3, 3), -1)
        self.assertEqual(clock.hilbert_symbol_odd(-1, 3, 13), 1)


class ClockTests(unittest.TestCase):
    def test_exact_invariant_length_formula(self):
        for m, n in [(1, 0), (0, 1), (1, -1), (-1, 2), (-6, 17)]:
            row = clock.element_certificate(m, n)
            self.assertTrue(row["norm_matches_13_power"])
            self.assertTrue(row["matrix_determinant_matches_norm"])
            self.assertEqual(row["tree_length_from_trace_norm"], abs(n))

    def test_iteration_and_primitivity(self):
        base = clock.element(2, 3)
        self.assertEqual(base**4, clock.element(8, 12))
        self.assertTrue(clock.canonical_primitive(-2, 3))
        self.assertFalse(clock.canonical_primitive(-4, 6))
        self.assertFalse(clock.canonical_primitive(2, -3))

    def test_rank_two_determinant(self):
        real_unit, _ = clock.clock_constants()
        self.assertGreater(real_unit, 0.0)
        self.assertAlmostEqual(real_unit, 2.633915793849633, places=14)

    def test_near_wall_records(self):
        records = clock.record_near_wall(400)
        lookup = {(row["m"], row["n"]): row for row in records}
        for pair in [(-6, 17), (-19, 54), (-44, 125), (-113, 321)]:
            self.assertIn(pair, lookup)
        selected = [lookup[pair] for pair in [(-6, 17), (-19, 54), (-44, 125), (-113, 321)]]
        self.assertTrue(
            all(selected[i + 1]["real_length"] < selected[i]["real_length"] for i in range(3))
        )
        self.assertTrue(
            all(selected[i + 1]["height"] > selected[i]["height"] for i in range(3))
        )

    def test_box_counts(self):
        self.assertEqual(clock.primitive_box_count(10, 10), 48)
        self.assertEqual(clock.primitive_box_count(40, 40), 742)

    def test_height_counts(self):
        self.assertEqual(clock.primitive_height_count(20), 36)
        self.assertEqual(clock.primitive_height_count(80), 577)

    def test_height_identity_for_model_coordinates(self):
        real_unit, split_unit = clock.clock_constants()
        for m, n in [(1, 0), (0, 1), (-6, 17), (5, -2)]:
            real_length = abs(m * real_unit + n * split_unit)
            tree_length = abs(n)
            height_twice = real_length + math.log(13.0) * tree_length
            self.assertGreater(height_twice, 0.0)
            self.assertAlmostEqual(height_twice, real_length + math.log(13.0) * abs(n))


class ReproductionTests(unittest.TestCase):
    def test_producer_and_independent_checker(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory)
            clock.produce(results, near_wall_limit=1000)
            report = independent_check.check(results)
            self.assertTrue(report["all_passed"], report["checks"])
            self.assertGreaterEqual(report["check_count"], 10)


if __name__ == "__main__":
    unittest.main()
