#!/usr/bin/env python3
"""Unit and adversarial tests for HCS-P51."""

from __future__ import annotations

import copy
import math
import unittest

import c51_abel_germ as c51
import independent_check


class AbelGermTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = c51.build_certificate(max_period=32)

    def test_dependency_locks(self) -> None:
        self.assertEqual(len(self.certificate["dependency_locks"]), 8)

    def test_marked_and_primitive_counts(self) -> None:
        self.assertEqual([c51.marked_count(n) for n in range(1, 9)], [1, 1, 4, 9, 11, 16, 29, 49])
        for period in range(1, 33):
            self.assertGreaterEqual(c51.primitive_orbit_count(period), 0)

    def test_reciprocal_packet_polynomials(self) -> None:
        self.assertEqual(c51.beta_trace_polynomial(3), c51.T + 1)
        self.assertEqual(c51.beta_trace_polynomial(4), c51.T)
        self.assertEqual(c51.beta_trace_polynomial(5), c51.T**2 + c51.T - 1)
        self.assertEqual(c51.beta_trace_polynomial(6), c51.T - 1)

    def test_period_four_crosscheck(self) -> None:
        rows = self.certificate["period_four_rows"]
        self.assertTrue(all(row["p50_crosscheck"] for row in rows if row["p50_crosscheck"] is not None))
        self.assertTrue(all(row["beta_absolute"] != "0" for row in rows))

    def test_certified_pressure_ratio(self) -> None:
        constants = self.certificate["constants"]
        threshold = constants["sigma_certified"]
        ratio = 2.0 * constants["golden_ratio"] * math.exp(
            -(threshold + 1e-5) * constants["pressure_lower"] * math.log(constants["J_star"])
        )
        self.assertLess(ratio, 1.0)

    def test_degree_factor_cannot_be_dropped(self) -> None:
        constants = self.certificate["constants"]
        wrong = math.log(constants["golden_ratio"]) / (
            constants["pressure_lower"] * math.log(constants["J_star"])
        )
        true_ratio = 2.0 * constants["golden_ratio"] * math.exp(
            -wrong * constants["pressure_lower"] * math.log(constants["J_star"])
        )
        self.assertGreater(true_ratio, 1.0)

    def test_boundary_radius_is_not_promoted(self) -> None:
        lower = [
            row["flatters_lower_norm"]
            for row in self.certificate["abel_boundary_lower_bounds"]
            if row["u_radius"] == 1.0
        ]
        self.assertEqual(lower, sorted(lower))
        self.assertGreater(lower[-1], 100.0)
        self.assertEqual(
            self.certificate["theorem_ledger"]["ungraded_u_equals_one_series"],
            "REFUTED_DIVERGES",
        )

    def test_pushforward_is_contractive_not_injective(self) -> None:
        spaces = self.certificate["banach_spaces"]
        self.assertEqual(spaces["operator_norm_upper"], 1)
        self.assertTrue(spaces["packetwise_norm_identity"])
        self.assertFalse(spaces["pushforward_injective"])

    def test_claim_boundary_rejects_promotions(self) -> None:
        promoted = copy.deepcopy(self.certificate["theorem_ledger"])
        for key in [
            "analytic_continuation_beyond_certified_domain",
            "boundary_abel_renormalization",
            "von_mangoldt_trace_law",
            "fredholm_determinant",
            "hilbert_polya_operator",
        ]:
            self.assertEqual(promoted[key], "OPEN")

    def test_independent_checker(self) -> None:
        path = c51.DEFAULT_OUTPUT
        c51.write_certificate(path)
        result = independent_check.run_check(path)
        self.assertEqual(result["status"], "PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
