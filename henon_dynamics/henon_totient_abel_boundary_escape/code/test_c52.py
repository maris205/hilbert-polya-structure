#!/usr/bin/env python3
"""Unit and adversarial tests for HCS-P52."""

from __future__ import annotations

import copy
import math
import unittest

import c52_abel_escape as c52
import independent_check


class TotientAbelEscapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = c52.build_certificate(max_index=72)

    def test_dependency_locks(self) -> None:
        self.assertEqual(len(self.certificate["dependency_locks"]), 4)

    def test_reciprocal_packet_polynomials(self) -> None:
        self.assertEqual(c52.beta_trace_polynomial(3), c52.T + 1)
        self.assertEqual(c52.beta_trace_polynomial(4), c52.T)
        self.assertEqual(c52.beta_trace_polynomial(5), c52.T**2 + c52.T - 1)
        self.assertEqual(c52.beta_trace_polynomial(6), c52.T - 1)

    def test_exact_packet_formula(self) -> None:
        rows = self.certificate["packet_rows"]
        self.assertLess(max(row["formula_abs_error"] for row in rows), 1e-70)
        self.assertTrue(all(row["p51_crosscheck"] for row in rows if row["p51_crosscheck"] is not None))

    def test_uniform_correction_is_tiny(self) -> None:
        constants = self.certificate["constants"]
        self.assertLess(constants["uniform_correction_upper"], 0.001735)
        self.assertGreaterEqual(
            constants["uniform_correction_upper"],
            constants["uniform_correction_partial_32"],
        )

    def test_abel_constant_uses_half_normalization(self) -> None:
        constants = self.certificate["constants"]
        lam = float(constants["L"])
        expected = 3.0 * math.log(lam) / math.pi**2
        wrong = 6.0 * math.log(lam) / math.pi**2
        self.assertAlmostEqual(constants["abel_limit_constant_3logL_over_pi2"], expected, places=14)
        self.assertNotAlmostEqual(expected, wrong, places=8)

    def test_abel_rows_approach_limit(self) -> None:
        ratios = [row["ratio_to_target"] for row in self.certificate["abel_rows"]]
        self.assertEqual(ratios, sorted(ratios))
        self.assertGreater(ratios[-1], 0.999)

    def test_gamma_profile_not_exponential(self) -> None:
        final = self.certificate["abel_rows"][-1]
        row = next(item for item in final["profile_laplace"] if item["s"] == 1.0)
        self.assertAlmostEqual(row["target_gamma_2_1"], 0.25, places=15)
        self.assertNotAlmostEqual(row["target_gamma_2_1"], 0.5, places=6)
        self.assertLess(abs(row["observed"] - 0.25), 4e-4)

    def test_fixed_prefix_mass_escapes(self) -> None:
        fractions = [row["fixed_prefix_3_20_mass_fraction"] for row in self.certificate["abel_rows"]]
        self.assertLess(fractions[-1], fractions[0] / 20)

    def test_vector_limit_is_not_promoted(self) -> None:
        ledger = self.certificate["theorem_ledger"]
        self.assertEqual(
            ledger["tagged_banach_norm_boundary_limit"],
            "REFUTED_NO_CONVERGENT_SUBNET",
        )
        self.assertEqual(ledger["all_orbit_boundary_interchange"], "OPEN")

    def test_wrong_tau_power_rejected(self) -> None:
        rows = self.certificate["abel_rows"]
        wrong = [row["tau_squared_Z"] / row["tau"] for row in rows]
        self.assertGreater(wrong[-1], wrong[0])
        self.assertGreater(wrong[-1], 100.0)

    def test_claim_boundary_rejects_promotions(self) -> None:
        promoted = copy.deepcopy(self.certificate["theorem_ledger"])
        for key in ["all_orbit_boundary_interchange", "von_mangoldt_trace_law", "fredholm_determinant", "hilbert_polya_operator"]:
            self.assertEqual(promoted[key], "OPEN")

    def test_independent_checker(self) -> None:
        c52.write_certificate(c52.DEFAULT_OUTPUT, max_index=72)
        result = independent_check.run_check(c52.DEFAULT_OUTPUT)
        self.assertEqual(result["status"], "PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
