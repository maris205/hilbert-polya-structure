from __future__ import annotations

import json
import math
import unittest
from pathlib import Path

import c43_entropy_bridge as C43


class EntropyBridgeTests(unittest.TestCase):
    def test_characteristic_trace_sequence(self) -> None:
        self.assertEqual([C43.marked_count(n) for n in range(1, 9)], [1, 1, 4, 9, 11, 16, 29, 49])

    def test_mobius_exact_period_ledger(self) -> None:
        expected = [1, 0, 3, 8, 10, 12, 28, 40]
        self.assertEqual([C43.exact_period_count(n) for n in range(1, 9)], expected)
        for period in range(1, 25):
            self.assertEqual(C43.exact_period_count(period) % period, 0)

    def test_certificate_boundary(self) -> None:
        certificate = C43.build_certificate(20)
        gate = certificate["finite_gate"]
        self.assertTrue(gate["mobius_integrality"])
        self.assertTrue(gate["positive_exact_counts"])
        self.assertLess(abs(float(gate["last_exact_over_theta"]) - 1.0), 0.01)
        self.assertNotEqual(certificate["claim_boundary"], "orbit-prime bijection")

    def test_committed_certificate(self) -> None:
        path = Path(__file__).resolve().parents[1] / "results" / "c43_certificate.json"
        committed = json.loads(path.read_text(encoding="utf-8"))
        rebuilt = C43.build_certificate(int(committed["max_period"]))
        self.assertEqual(committed, rebuilt)
        self.assertAlmostEqual(float(committed["finite_gate"]["target_primitive_ratio"]), math.log((1 + math.sqrt(5)) / 2))


if __name__ == "__main__":
    unittest.main()
