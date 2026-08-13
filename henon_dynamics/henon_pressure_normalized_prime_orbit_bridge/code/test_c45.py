from __future__ import annotations

import json
import unittest
from pathlib import Path

import c45_pressure_clock as C45


class PressureClockTests(unittest.TestCase):
    def test_dependency_hashes(self) -> None:
        self.assertEqual(len(C45.dependency_locks()), 3)

    def test_mixing_and_entropy_normalization(self) -> None:
        data = C45.build_certificate()
        self.assertTrue(data["mixing_gate"])
        self.assertEqual(data["normalized_entropy"], 1)
        self.assertEqual(data["prime_orbit_law"], "Pi_hat(T)~exp(T)/T")

    def test_arithmetic_claim_firewall(self) -> None:
        data = C45.build_certificate()
        self.assertFalse(data["fixture"]["label_is_asserted_prime"])
        self.assertIn("positive reals", data["claim_boundary"])

    def test_committed_certificate(self) -> None:
        path = Path(__file__).resolve().parents[1] / "results" / "c45_certificate.json"
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), C45.build_certificate())


if __name__ == "__main__":
    unittest.main()
