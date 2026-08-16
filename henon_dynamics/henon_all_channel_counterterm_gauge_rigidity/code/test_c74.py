#!/usr/bin/env python3
import copy
import sys
import unittest
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c74_gauge_rigidity as c74  # noqa: E402


class GaugeRigidityTests(unittest.TestCase):
    def test_p72_coefficient_replay(self):
        for m in range(1, 150):
            self.assertEqual(c74.c_divisor(m), c74.c_euler(m))
            self.assertNotEqual(c74.c_euler(m), 0)

    def test_root_filter(self):
        for m in range(1, 30):
            for degree in range(0, 6 * m + 1):
                expected = 2 * m if degree % (2 * m) == m else 0
                self.assertEqual(c74.weighted_root_filter(m, degree), expected)

    def test_channel_first_coefficients(self):
        self.assertEqual(c74.channel_log_coefficient(2, 2), Fraction(1))
        self.assertEqual(c74.channel_log_coefficient(3, 3), Fraction(-4, 3))
        self.assertEqual(c74.channel_log_coefficient(3, 6), 0)
        self.assertEqual(c74.channel_log_coefficient(3, 9), Fraction(-8, 3))

    def test_genus_m_minus_one_annihilates(self):
        for degree in range(1, 180):
            self.assertEqual(
                c74.relative_channel_coefficient(degree)
                + c74.genus_minus_one_multiplier_coefficient(degree),
                0,
            )

    def test_genus_m_preserves_residual_with_negative_sign(self):
        for degree in range(1, 180):
            observed = (
                c74.relative_channel_coefficient(degree)
                + c74.genus_m_multiplier_coefficient(degree)
            )
            expected = Fraction(0) if degree == 1 else -2 * c74.c_euler(degree)
            self.assertEqual(observed, expected)

    def test_product_form(self):
        for degree in range(1, 180):
            expected = Fraction(0) if degree == 1 else -2 * c74.c_euler(degree)
            self.assertEqual(c74.product_residual_log_coefficient(degree), expected)

    def test_source_pair(self):
        self.assertEqual(
            c74.source_residual(Fraction(3, 4), Fraction(1, 2)),
            {"pole_coefficient": "0", "log_coefficient": "0", "constant": "-3/2"},
        )
        self.assertNotEqual(
            c74.source_residual(Fraction(-3, 4), Fraction(1, 2))["pole_coefficient"],
            "0",
        )
        self.assertNotEqual(
            c74.source_residual(Fraction(3, 4), Fraction(-1, 2))["log_coefficient"],
            "0",
        )

    def test_finite_jet_nonuniqueness(self):
        for order in range(0, 20):
            series = c74.finite_jet_example(order, Fraction(7, 3))
            self.assertEqual(series[0], 1)
            self.assertTrue(all(value == 0 for value in series[1:order + 1]))
            self.assertEqual(series[order + 1], Fraction(7, 3))

    def test_core_sign_lock(self):
        core = c74.core_payload()
        self.assertIn("-sum_", core["relative_sign_lock"])
        self.assertEqual(core["source_forced_pair"], {"a": "3/4", "beta": "1/2"})
        self.assertEqual(core["genus_m_minus_1_channel_residual"], "1")
        self.assertEqual(core["genus_m_channel_residual"], "exp(-2sum_(m>=2)c_m t^m)")

    def test_channel_rows_force_positive_d(self):
        for row in c74.core_payload()["channel_ledger"]:
            self.assertEqual(Fraction(row["forced_d_m"]), Fraction(row["c_m"]))

    def test_dependency_locks(self):
        locks = c74.dependency_locks()
        self.assertEqual(set(locks), set(c74.DEPENDENCIES))

    def test_validation_rejects_wrong_sign(self):
        core = c74.core_payload()
        core["channel_ledger"][0]["forced_d_m"] = str(-c74.c_euler(2))
        with self.assertRaises(ValueError):
            c74.validate(core)

    def test_validation_rejects_absolute_canonicity(self):
        core = c74.core_payload()
        core["claim_status"]["absolute_canonical_gauge"] = "PROVED"
        with self.assertRaises(ValueError):
            c74.validate(core)

    def test_mutation_audit(self):
        audit = c74.mutation_audit(c74.core_payload())
        self.assertGreaterEqual(audit["attempted"], 35)
        self.assertTrue(audit["all_rejected"])

    def test_build_is_deterministic(self):
        first = c74.build()
        second = c74.build()
        self.assertEqual(first["core_sha256"], second["core_sha256"])
        self.assertEqual(first, second)

    def test_copy_mutation_does_not_change_core(self):
        core = c74.core_payload()
        trial = copy.deepcopy(core)
        trial["source_forced_pair"]["a"] = "0"
        self.assertEqual(core["source_forced_pair"]["a"], "3/4")


if __name__ == "__main__":
    unittest.main()
