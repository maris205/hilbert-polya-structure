from __future__ import annotations

import json
import unittest
from pathlib import Path

import c44_amplitude_gate as C44


class AmplitudeGateTests(unittest.TestCase):
    def test_critical_line_is_inside_absolute_domain(self) -> None:
        data = C44.build_certificate(10_000)
        self.assertTrue(data["critical_line_inside_absolute_domain"])
        self.assertLess(float(data["critical_line_ratio"]), 1.0)

    def test_local_prime_atoms_match_exactly(self) -> None:
        data = C44.build_certificate(10_000)
        self.assertTrue(all(float(row["difference"]) == 0.0 for row in data["local_rows"]))

    def test_prime_absolute_mass_grows(self) -> None:
        data = C44.build_certificate(100_000)
        masses = [float(row["partial_prime_mass"]) for row in data["prime_mass_checkpoints"]]
        self.assertLess(masses[0], masses[1])
        self.assertEqual(masses[1], masses[2])

    def test_committed_certificate_rebuilds(self) -> None:
        path = Path(__file__).resolve().parents[1] / "results" / "c44_certificate.json"
        committed = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(committed, C44.build_certificate(int(committed["prime_mass_checkpoints"][-1]["limit"])))


if __name__ == "__main__":
    unittest.main()
