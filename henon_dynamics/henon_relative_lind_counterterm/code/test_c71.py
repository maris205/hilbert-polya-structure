#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path
import sympy as sp
PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c71_relative_lind as c71  # noqa: E402


class RelativeLindTests(unittest.TestCase):
    def test_boundary_coordinate(self):
        self.assertEqual(c71.exact_boundary_ledger()["denominator_in_u"], "u*(2 - u)")

    def test_lind_pole(self):
        self.assertEqual(c71.exact_boundary_ledger()["lind_pole_coefficient"], "sqrt(2)/2 + 3/4")

    def test_packet_coefficient(self):
        self.assertEqual(c71.exact_boundary_ledger()["packet_pole_coefficient"], "sqrt(2)/2")

    def test_relative_pole(self):
        self.assertEqual(c71.exact_boundary_ledger()["relative_pole_coefficient"], "3/4")

    def test_branch(self):
        self.assertEqual(c71.exact_boundary_ledger()["normalized_algebraic_factor"], "1/sqrt(2 - u)")

    def test_analytic_remainder(self):
        u = sp.symbols("u")
        series = c71.exact_boundary_ledger()["analytic_exponent_series_through_u6"]
        self.assertNotIn("1/u", series)

    def test_status(self):
        status = c71.core_payload()["claim_status"]
        self.assertEqual(status["global_relative_determinant"], "OPEN")
        self.assertFalse(status["route_b_authorized"])

    def test_mutations(self):
        audit = c71.mutation_audit(c71.core_payload())
        self.assertEqual(audit["attempted"], 23)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
