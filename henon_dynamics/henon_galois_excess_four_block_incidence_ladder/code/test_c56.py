#!/usr/bin/env python3
"""Unit tests for HCS-P56."""

from __future__ import annotations

import unittest

import sympy as sp

import c56_incidence_ladder as c56


class TestP56(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = c56.run_check()

    def test_cycle_counts(self) -> None:
        self.assertEqual(self.result["cycle_counts"], {"1": 1, "2": 0, "3": 1, "4": 2, "5": 2, "6": 2})

    def test_family_words(self) -> None:
        self.assertEqual(c56.family_a(6), (0, 0, 0, 0, 2, 1))
        self.assertEqual(c56.family_b(6), (0, 0, 0, 2, 3, 1))

    def test_ladder_range(self) -> None:
        self.assertEqual(self.result["incidence_ladder"]["finite_verification_range"], [3, 64])

    def test_ladder_direct(self) -> None:
        for m in range(3, 20):
            self.assertFalse(c56.signed_sum(((1, c56.family_a(m)), (1, c56.family_b(m + 2)), (-1, c56.family_a(m + 1)), (-1, c56.family_b(m + 1))), m))

    def test_period_six_residuals(self) -> None:
        self.assertEqual(self.result["period_6_B"]["recurrence_residuals"], ["0"] * 6)

    def test_period_six_trace(self) -> None:
        self.assertEqual(self.result["period_6_B"]["trace"], "5352*sqrt(7) + 18062")

    def test_period_six_multiplier(self) -> None:
        self.assertEqual(self.result["period_6_B"]["multiplier_minpoly_coefficients"], [1, -36124, 125728518, -36124, 1])
        self.assertEqual(self.result["period_6_B"]["multiplier_mod_13_gcd_degrees"], [0, 0])

    def test_period_six_interval(self) -> None:
        self.assertEqual(self.result["period_6_B"]["square_margins"], [13729, 432])

    def test_obstruction(self) -> None:
        self.assertTrue(self.result["four_block_obstruction"]["width_at_most_4_obstruction"])
        self.assertLess(sp.Float(self.result["four_block_obstruction"]["delta_4_decimal_50"]), 0)

    def test_integer_margin(self) -> None:
        self.assertEqual(self.result["four_block_obstruction"]["integer_comparison"]["margin"], 96873)

    def test_width_four_rank(self) -> None:
        self.assertEqual(self.result["finite_sharpness"]["width_4_four_row_rank"], 3)

    def test_width_five_unimodular(self) -> None:
        self.assertEqual(self.result["finite_sharpness"]["width_5_determinant"], 1)

    def test_holder_firewall(self) -> None:
        self.assertEqual(self.result["holder_gate"]["status"], "OPEN_ASYMPTOTICS")

    def test_route_firewall(self) -> None:
        self.assertFalse(self.result["arithmetic_advance"])
        self.assertEqual(self.result["route_b"], "NOT_AUTHORIZED")

    def test_mutations(self) -> None:
        self.assertEqual(self.result["mutation_audit"]["count"], 20)
        self.assertEqual(len(set(self.result["mutation_audit"]["labels"])), 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
