#!/usr/bin/env python3
import copy
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c76_natural_boundary as c76  # noqa: E402


class WeightedNaturalBoundaryTests(unittest.TestCase):
    def test_coefficient_identity_and_nonvanishing(self):
        for m in range(1, 121):
            self.assertEqual(c76.c_divisor(m), c76.c_euler(m))
            self.assertNotEqual(c76.c_euler(m), Fraction(0))

    def test_first_coefficients(self):
        self.assertEqual(c76.c_euler(1), Fraction(1))
        self.assertEqual(c76.c_euler(2), Fraction(1, 2))
        self.assertEqual(c76.c_euler(3), Fraction(-2, 3))
        self.assertEqual(c76.c_euler(10), Fraction(-2, 5))

    def test_strict_radius_ladders(self):
        for q in (0.25, 0.5, 1.0, 2.0, 4.0):
            values = [c76.radius_decimal(m, q) for m in range(1, 80)]
            self.assertTrue(all(a < b for a, b in zip(values, values[1:])))
            self.assertLess(values[-1], c76.radius_decimal(10000, q))

    def test_radius_limit(self):
        for q in (0.5, 1.0, 2.0):
            self.assertLess(
                abs(c76.radius(500, q) - c76.limiting_radius(q)), 8e-4
            )

    def test_all_declared_roots(self):
        for q in (0.5, 1.0, 2.0):
            for m in range(1, 14):
                for k in range(2 * m):
                    self.assertLess(abs(c76.denominator(c76.root(m, k, q), m, q)), 2e-11)

    def test_distinct_channel_moduli(self):
        for q in (0.5, 1.0, 2.0):
            radii = {c76.radius_decimal(m, q) for m in range(1, 40)}
            self.assertEqual(len(radii), 39)

    def test_nonzero_principal_parts(self):
        for q in (0.5, 1.0, 2.0):
            for m in range(1, 30):
                self.assertNotEqual(c76.principal_coefficient(m, 0, q), 0)
                self.assertAlmostEqual(
                    c76.principal_coefficient(m, 1, q),
                    -c76.principal_coefficient(m, 0, q),
                )

    def test_angular_mesh(self):
        gaps = [math.pi / m for m in (5, 10, 20, 40)]
        self.assertTrue(all(a > b for a, b in zip(gaps, gaps[1:])))

    def test_status_firewall(self):
        status = c76.core_payload()["claim_status"]
        self.assertEqual(status["natural_boundary_for_unrenormalized_continuation"], "PROVED")
        self.assertEqual(status["renormalized_natural_boundary"], "NOT_CLAIMED")
        self.assertEqual(status["source_native_operator"], "OPEN")
        self.assertFalse(status["route_b_authorized"])

    def test_mutations(self):
        audit = c76.mutation_audit(c76.core_payload())
        self.assertEqual(audit["attempted"], 24)
        self.assertTrue(audit["all_rejected"])

    def test_validator_rejects_protected_scalar_forgery(self):
        protected = [
            "weighted_channel", "coefficient", "fiber_roots", "fiber_radius",
            "radius_monotonicity", "accumulation_circle", "principal_part",
            "angular_density", "natural_boundary", "strongest_positive_result",
            "strongest_obstruction", "open_theorem", "reusable_structure",
            "round2_clue",
        ]
        for key in protected:
            trial = copy.deepcopy(c76.core_payload())
            trial[key] = "FORGED"
            with self.assertRaises(ValueError, msg=key):
                c76.validate(trial)


if __name__ == "__main__":
    unittest.main()
