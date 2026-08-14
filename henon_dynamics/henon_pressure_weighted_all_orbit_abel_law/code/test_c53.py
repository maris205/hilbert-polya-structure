#!/usr/bin/env python3
"""Unit and adversarial tests for HCS-P53."""

from __future__ import annotations

import copy
import math
import tempfile
import unittest
from pathlib import Path

import c53_all_orbit_abel as c53
import independent_check


class AllOrbitAbelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = c53.build_certificate(max_index=48)

    def test_dependency_locks(self) -> None:
        self.assertEqual(len(self.certificate["dependency_locks"]), 7)

    def test_reciprocal_half_polynomials(self) -> None:
        self.assertEqual(c53.beta_trace_polynomial(3), c53.T + 1)
        self.assertEqual(c53.beta_trace_polynomial(4), c53.T)
        self.assertEqual(c53.beta_trace_polynomial(5), c53.T**2 + c53.T - 1)
        self.assertEqual(c53.beta_trace_polynomial(6), c53.T - 1)

    def test_exact_trace_field_norms(self) -> None:
        sentinels = self.certificate["orbit_sentinels"]
        self.assertEqual(sentinels["period_1"]["packet_rows"][0]["absolute_half_norm"], "19")
        self.assertEqual(sentinels["period_3"]["packet_rows"][0]["absolute_half_norm"], "7451")
        self.assertEqual(sentinels["period_4"]["packet_rows"][0]["absolute_half_norm"], "579")

    def test_spectral_height_not_physical_only(self) -> None:
        row = self.certificate["orbit_sentinels"]["period_1"]
        self.assertGreater(row["spectral_height_log_mahler"], math.log(row["physical_multiplier_modulus"]) + 1)

    def test_unit_circle_branch_is_exercised(self) -> None:
        row = self.certificate["orbit_sentinels"]["abstract_salem_stress"]
        self.assertFalse(row["source_native_h6"])
        self.assertEqual(row["unit_circle_multiplier_conjugates"], 2)
        self.assertLess(max(item["embedding_formula_abs_error"] for item in row["packet_rows"]), 1e-55)

    def test_per_orbit_abel_targets(self) -> None:
        for row in self.certificate["orbit_sentinels"].values():
            final = row["abel_rows"][-1]
            self.assertLess(abs(final["ratio_to_target"] - 1), 0.006)

    def test_pressure_weighted_sample_limit(self) -> None:
        profile = self.certificate["sample_pressure_profile"]
        self.assertAlmostEqual(sum(profile["orbit_limit_weights"].values()), 1.0, places=14)
        self.assertGreater(profile["rows"][-1]["ratio_to_target"], 0.998)

    def test_joint_profile_is_gamma_two(self) -> None:
        final = self.certificate["sample_pressure_profile"]["rows"][-1]
        row = next(item for item in final["scaled_index_laplace"] if item["r"] == 1.0)
        self.assertEqual(row["target_gamma_2_1"], 0.25)
        self.assertNotEqual(row["target_gamma_2_1"], 0.5)
        self.assertLess(abs(row["observed"] - 0.25), 0.002)

    def test_claim_boundary(self) -> None:
        ledger = self.certificate["theorem_ledger"]
        self.assertEqual(
            ledger["pressure_weighted_all_orbit_abel_interchange"],
            "PROVED_IN_P51_SAFE_HALF_PLANE",
        )
        self.assertEqual(
            ledger["tagged_banach_boundary"],
            "REFUTED_NO_NORM_OR_WEAKLY_CONVERGENT_SUBNET",
        )
        self.assertEqual(ledger["continuation_to_pressure_boundary"], "OPEN")
        self.assertEqual(ledger["fredholm_determinant"], "OPEN")

    def test_promoted_claim_mutation_is_detectable(self) -> None:
        promoted = copy.deepcopy(self.certificate)
        promoted["theorem_ledger"]["hilbert_polya_operator"] = "PROVED"
        self.assertNotEqual(
            promoted["theorem_ledger"]["hilbert_polya_operator"],
            self.certificate["theorem_ledger"]["hilbert_polya_operator"],
        )

    def test_independent_checker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "certificate.json"
            c53.write_certificate(path, max_index=48)
            result = independent_check.run_check(path)
            self.assertEqual(result["status"], "PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
