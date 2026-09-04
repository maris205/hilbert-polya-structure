"""Small independent smoke tests for the frozen HCS-C376 evidence."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C376Smoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = json.loads((ROOT / "results/c376_flat_magnetic_torus_evidence.json").read_text())

    def test_counts(self):
        self.assertEqual(len(self.value["classical_rows"]), 256)
        self.assertEqual(len(self.value["landau_rows"]), 16512)
        self.assertEqual(len(self.value["translation_rows"]), 4160)

    def test_extreme_multiplicity_and_determinant(self):
        self.assertEqual(self.value["landau_rows"][0]["multiplicity"], 64)
        self.assertEqual(self.value["landau_rows"][-1]["multiplicity"], 64)
        self.assertEqual(self.value["determinant_rows"][-1]["determinant_exponent"], {"numerator": 32, "denominator": 1})

    def test_firewall_and_revival(self):
        self.assertTrue(all(flag is False for flag in self.value["scope_flags"].values()))
        self.assertEqual(self.value["route_a"]["overall"], "ROUTE_A_REJECTED")
        self.assertEqual(self.value["revival_rows"][128]["phase_at_classical_period"], "-1")
        self.assertEqual(self.value["revival_rows"][128]["phase_at_double_period"], "+1")
        self.assertEqual(self.value["route_a"]["tuple"][0], "A0_FAIL")
        signs = {row["flux_sign"] for row in self.value["translation_rows"]}
        self.assertEqual(signs, {-1, 1})


if __name__ == "__main__":
    unittest.main()
