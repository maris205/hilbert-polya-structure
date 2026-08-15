#!/usr/bin/env python3
import sys
import unittest
from fractions import Fraction
from pathlib import Path
PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c70_orbit_euler as c70  # noqa: E402


class OrbitEulerTests(unittest.TestCase):
    def test_primitive_polynomial(self):
        self.assertEqual(c70.primitive_poly(5), [0, 2, 0, 4])

    def test_log_coefficient(self):
        for m in range(1, 20):
            poly = c70.log_derivative_polynomial(m)
            for q in (Fraction(1, 2), Fraction(1), Fraction(2)):
                self.assertEqual(c70.poly_eval(poly, q), c70.direct_log_derivative_value(m, q))

    def test_q1_specialization(self):
        self.assertEqual([c70.poly_eval(c70.log_derivative_polynomial(m), Fraction(1)) for m in range(1, 7)], [2, 2, 8, 2, 32, 8])

    def test_radius(self):
        core = c70.core_payload()
        self.assertEqual(core["positive_q_radius"], "R(q)=(1+q^2)^(-1/2)")

    def test_boundary(self):
        self.assertIn("ESSENTIAL", c70.core_payload()["boundary_type"])

    def test_strict_shift(self):
        for row in c70.core_payload()["boundary_samples"]:
            if row["q"] != 1:
                self.assertLess(row["orbit_radius"], row["mean_field_radius"])

    def test_status(self):
        status = c70.core_payload()["claim_status"]
        self.assertEqual(status["arithmetic_advance"], "NO")
        self.assertFalse(status["route_b_authorized"])

    def test_mutations(self):
        audit = c70.mutation_audit(c70.core_payload())
        self.assertEqual(audit["attempted"], 24)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
