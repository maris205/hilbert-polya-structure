"""Independent smoke tests for HCS-C377 evidence."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class C377Smoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x = json.loads((ROOT / "results/c377_periodic_clm_evidence.json").read_text())

    def test_counts_and_convention(self):
        self.assertEqual(len(self.x["tricomi_rows"]), 1024)
        self.assertEqual(len(self.x["nonzero_mean_rows"]), 2048)
        self.assertEqual(self.x["multiplier_rows"][-1]["multiplier"]["im"], {"numerator": -1, "denominator": 1})

    def test_tangent_boundary_is_not_simple(self):
        tangent = [row for row in self.x["one_mode_rows"] if row["regime"] == "tangent_zero"]
        self.assertTrue(tangent)
        self.assertIn("no unconditional self-similar rate at tangent or higher-order zeros", self.x["nonclaims"])

    def test_firewall_and_profile(self):
        self.assertTrue(all(value is False for value in self.x["scope_flags"].values()))
        self.assertEqual(self.x["route_a"]["tuple"], ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
        self.assertTrue(all(row["transverse"] for row in self.x["zero_profile_rows"]))


if __name__ == "__main__":
    unittest.main()
