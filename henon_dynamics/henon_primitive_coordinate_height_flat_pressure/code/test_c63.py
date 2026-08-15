#!/usr/bin/env python3

from __future__ import annotations

import json
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERT = json.loads((PROJECT / "results" / "c63_certificate.json").read_text(encoding="utf-8"))
INDEPENDENT = json.loads((PROJECT / "results" / "c63_independent_check.json").read_text(encoding="utf-8"))


class HeightFlatPressureTests(unittest.TestCase):
    def test_identity(self) -> None:
        self.assertTrue(CERT["check"])
        self.assertEqual(CERT["candidate_id"], "HCS-P63")

    def test_all_period_status(self) -> None:
        self.assertEqual(CERT["claim_status"]["uniform_coordinate_height"], "PROVED")
        self.assertEqual(CERT["claim_status"]["flat_coordinate_height_pressure"], "PROVED")

    def test_finite_integrality(self) -> None:
        self.assertTrue(all(row["scaled_polynomial_monic_integral"] for row in CERT["finite_exact_and_numeric_rows"]))

    def test_degrees(self) -> None:
        self.assertEqual(
            [row["primitive_degree"] for row in CERT["finite_exact_and_numeric_rows"]],
            [2, 2, 6, 14, 28, 62],
        )

    def test_sentinels(self) -> None:
        self.assertEqual(CERT["exact_sentinels"]["n1_height"], "(1/2)log(6)")
        self.assertEqual(CERT["exact_sentinels"]["n3_height"], "log(2)")

    def test_mutations(self) -> None:
        self.assertEqual(CERT["mutation_audit"]["attempted"], 25)
        self.assertTrue(CERT["mutation_audit"]["all_rejected"])

    def test_independent(self) -> None:
        self.assertTrue(INDEPENDENT["check"])
        self.assertTrue(INDEPENDENT["all_checks_match"])

    def test_claim_boundary(self) -> None:
        self.assertEqual(CERT["claim_status"]["arithmetic_advance"], "NO")
        self.assertFalse(CERT["route_a_status"]["full_arithmetic_candidate_pass"])
        self.assertFalse(CERT["route_b_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
