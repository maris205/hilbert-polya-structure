#!/usr/bin/env python3
import sys
import unittest
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c73_full_ladder_counterterm as c73  # noqa: E402


class FullLadderCountertermTests(unittest.TestCase):
    def test_channel_coefficients(self):
        for m in range(1, 101):
            self.assertEqual(c73.c_divisor(m), c73.c_euler(m))
            self.assertNotEqual(c73.c_euler(m), 0)

    def test_complex_root_ledger(self):
        for m in range(2, 30):
            roots = [c73.alpha(m, k) for k in range(2 * m)]
            self.assertEqual(len(roots), 2 * m)
            self.assertTrue(all(abs(1 - 2 * root ** (2 * m)) < 2e-12 for root in roots))

    def test_partial_fraction_coefficients(self):
        for m in range(2, 25):
            for degree in range(0, 6 * m + 1):
                expected = c73.channel_coefficient(m, degree)
                if degree < m:
                    self.assertEqual(expected, 0)
                elif (degree - m) % (2 * m) == 0:
                    ell = (degree - m) // (2 * m)
                    self.assertEqual(expected, c73.c_euler(m) * 2 ** (ell + 1))
                else:
                    self.assertEqual(expected, 0)

    def test_weierstrass_cancellations(self):
        for m in range(2, 80):
            self.assertTrue(all(c73.root_sum_is_zero(m, j) for j in range(m)))
            self.assertFalse(c73.root_sum_is_zero(m, m))

    def test_absolute_normal_majorant(self):
        q = Fraction(4, 5)
        levels = [c73.normalized_level_bound(m, q) for m in range(2, 60)]
        self.assertTrue(all(value > 0 for value in levels))
        self.assertLessEqual(
            sum(levels[23:]),
            c73.normalized_tail_bound(25, q),
        )

    def test_raw_prime_mass_divergence(self):
        primes = [p for p in range(3, 100) if c73.is_prime(p)]
        masses = [abs(c73.c_euler(p)) for p in primes]
        self.assertTrue(all(mass >= Fraction(2, 3) for mass in masses))
        self.assertGreater(sum(masses), 10)

    def test_tail_and_status_firewall(self):
        for degree in range(1, 121):
            self.assertEqual(
                c73.tail_direct_coefficient(degree),
                c73.tail_channel_coefficient(degree),
            )
        core = c73.core_payload()
        self.assertEqual(core["renormalization_identity"], "K_all(t)*C_rel(t)=1 on compatible branches")
        self.assertEqual(core["claim_status"]["transfer_operator_ownership"], "NOT_CLAIMED")
        self.assertEqual(core["claim_status"]["arithmetic_advance"], "NO")
        self.assertFalse(core["claim_status"]["route_b_authorized"])

    def test_dependencies_and_mutations(self):
        self.assertEqual(len(c73.dependency_locks()), 6)
        core = c73.core_payload()
        for key in c73.EXPECTED_STRINGS:
            forged = dict(core)
            forged[key] = "FORGED"
            with self.assertRaises(ValueError):
                c73.validate(forged)
        forged = dict(core)
        forged["claim_status"] = dict(core["claim_status"])
        forged["claim_status"]["transfer_operator_ownership"] = "PROVED"
        with self.assertRaises(ValueError):
            c73.validate(forged)
        audit = c73.mutation_audit(core)
        self.assertEqual(audit["attempted"], 25)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
