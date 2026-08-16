#!/usr/bin/env python3
import sys
import unittest
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c72_essential_ladder as c72  # noqa: E402


class EssentialLadderTests(unittest.TestCase):
    def test_euler_coefficient_identity(self):
        for m in range(1, 101):
            self.assertEqual(c72.c_divisor(m), c72.c_euler(m))

    def test_nonzero_channels(self):
        self.assertTrue(all(c72.c_euler(m) for m in range(1, 101)))

    def test_formal_regrouping(self):
        for degree in range(1, 101):
            self.assertEqual(
                c72.direct_log_coefficient(degree),
                c72.regrouped_log_coefficient(degree),
            )

    def test_first_channels(self):
        self.assertEqual(c72.c_euler(1), Fraction(1))
        self.assertEqual(c72.c_euler(2), Fraction(1, 2))
        self.assertEqual(c72.c_euler(3), Fraction(-2, 3))
        self.assertEqual(c72.c_euler(6), Fraction(-1, 3))

    def test_principal_multiplier(self):
        row = c72.ladder_row(3)
        self.assertEqual(row["log_Crel_principal_multiplier_of_1_over_sqrt2"], "2/9")

    def test_ladder(self):
        rhos = [float(c72.ladder_row(m)["rho_m"]) for m in range(2, 40)]
        self.assertTrue(all(a < b for a, b in zip(rhos, rhos[1:])))
        self.assertLess(rhos[-1], 1)

    def test_status_firewall(self):
        status = c72.core_payload()["claim_status"]
        self.assertEqual(status["unit_disk_meromorphic_determinant"], "REFUTED_FOR_THIS_RELATIVE_GERM")
        self.assertEqual(status["punctured_operator_model"], "OPEN")
        self.assertFalse(status["route_b_authorized"])

    def test_mutations(self):
        audit = c72.mutation_audit(c72.core_payload())
        self.assertEqual(audit["attempted"], 25)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
