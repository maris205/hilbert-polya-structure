#!/usr/bin/env python3
import math
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c69_cumulant_pressure as c69  # noqa: E402


class CumulantPressureTests(unittest.TestCase):
    def test_all_polynomial(self):
        self.assertEqual(c69.all_palindrome_polynomial(5), [0, 2, 0, 4, 0, 2])

    def test_primitive_enumeration(self):
        for n in range(1, 18, 2):
            self.assertEqual(c69.primitive_polynomial(n), c69.enumerated_primitive_polynomial(n))

    def test_counts(self):
        self.assertEqual([sum(c69.primitive_polynomial(n)) for n in range(1, 12, 2)], [2, 2, 6, 14, 28, 62])

    def test_strict_variance(self):
        for n in range(5, 32, 2):
            self.assertGreater(c69.moments(c69.primitive_polynomial(n))["variance_numerator"], 0)

    def test_pressure_gap(self):
        for s in (-2.0, -0.5, 0.0, 0.7, 2.0):
            orbit = 0.5 * math.log1p(math.exp(-2 * s))
            mean = 0.5 * math.log(2) - 0.5 * s
            self.assertAlmostEqual(orbit - mean, 0.5 * math.log(math.cosh(s)), 14)

    def test_gap_strictness(self):
        self.assertEqual(0.5 * math.log(math.cosh(0.0)), 0.0)
        self.assertGreater(0.5 * math.log(math.cosh(0.1)), 0.0)

    def test_status(self):
        status = c69.core_payload()["claim_status"]
        self.assertEqual(status["arithmetic_advance"], "NO")
        self.assertFalse(status["route_b_authorized"])

    def test_mutations(self):
        audit = c69.mutation_audit(c69.core_payload())
        self.assertEqual(audit["attempted"], 25)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
