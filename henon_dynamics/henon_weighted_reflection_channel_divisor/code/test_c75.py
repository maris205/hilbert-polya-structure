#!/usr/bin/env python3
import sys
import unittest
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c75_weighted_divisor as c75  # noqa: E402


class WeightedDivisorTests(unittest.TestCase):
    def test_euler_coefficient_identity(self):
        for m in range(1, 129):
            self.assertEqual(c75.c_divisor(m), c75.c_euler(m))

    def test_nonzero_and_bound(self):
        for m in range(1, 129):
            coefficient = c75.c_euler(m)
            self.assertNotEqual(coefficient, 0)
            self.assertLessEqual(abs(coefficient), 1)

    def test_first_channels(self):
        self.assertEqual(c75.c_euler(1), Fraction(1))
        self.assertEqual(c75.c_euler(2), Fraction(1, 2))
        self.assertEqual(c75.c_euler(3), Fraction(-2, 3))
        self.assertEqual(c75.c_euler(6), Fraction(-1, 3))
        self.assertEqual(c75.c_euler(15), Fraction(8, 15))

    def test_exact_weighted_regrouping(self):
        for degree in range(1, 101):
            self.assertEqual(
                c75.direct_log_polynomial(degree),
                c75.regrouped_log_polynomial(degree),
            )

    def test_positive_fiber_radius_separation(self):
        for q in (Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)):
            self.assertTrue(all(c75.exact_radius_increase(q, m, m + 1) for m in range(1, 41)))

    def test_radius_limit_side(self):
        for q in (0.5, 1.0, 2.0):
            log_radius = c75.log_rho(q, 20)
            log_limit = min(0.0, -math.log(q))
            self.assertLess(log_radius, log_limit)
            self.assertLess(log_limit - log_radius, 0.02)

    def test_all_complex_roots_on_hypersurface(self):
        for q in (0.5, 1.0, 2.0):
            for m in range(1, 17):
                for ell in range(2 * m):
                    self.assertLess(c75.hypersurface_residual(q, m, ell), 2e-12)

    def test_local_finiteness_cutoff(self):
        for rz, rw in (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(3, 4), Fraction(2, 3)),
            (Fraction(9, 10), Fraction(4, 5)),
        ):
            cutoff = c75.local_finiteness_cutoff(rz, rw)
            self.assertLess(rz ** (2 * cutoff) + rw ** (2 * cutoff), 1)
            if cutoff > 1:
                self.assertGreaterEqual(rz ** (2 * (cutoff - 1)) + rw ** (2 * (cutoff - 1)), 1)

    def test_dependency_locks(self):
        self.assertEqual(len(c75.dependency_locks()), 9)

    def test_status_firewall(self):
        status = c75.core_payload()["claim_status"]
        self.assertEqual(status["dense_natural_boundary"], "NOT_CLAIMED_RESERVED_FOR_P76")
        self.assertEqual(status["weighted_lind_source_for_q_not_1"], "NOT_CLAIMED")
        self.assertEqual(status["operator_model"], "OPEN")
        self.assertEqual(status["arithmetic_advance"], "NO")
        self.assertFalse(status["route_b_authorized"])

    def test_schema_validation(self):
        core = c75.core_payload()
        c75.validate(core)
        core["fiber_radius_limit"] = "FORGED"
        with self.assertRaises(ValueError):
            c75.validate(core)

    def test_mutations(self):
        audit = c75.mutation_audit(c75.core_payload())
        self.assertEqual(audit["attempted"], 38)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
