#!/usr/bin/env python3

from __future__ import annotations

import json
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERT = json.loads((PROJECT / "results" / "c64_certificate.json").read_text(encoding="utf-8"))
INDEPENDENT = json.loads((PROJECT / "results" / "c64_independent_check.json").read_text(encoding="utf-8"))


class ReflectionPacketPressureTests(unittest.TestCase):
    def test_identity(self) -> None:
        self.assertTrue(CERT["check"])
        self.assertEqual(CERT["candidate_id"], "HCS-P64")

    def test_degree_vector(self) -> None:
        self.assertEqual(
            [row["primitive_half_words"] for row in CERT["symbolic_rows"][:6]],
            [2, 2, 6, 14, 28, 62],
        )

    def test_reflection_event(self) -> None:
        self.assertTrue(all(row["axis_event_s_minus1_equals_s_plus1"] == "1" for row in CERT["symbolic_rows"]))

    def test_two_limits_are_typed(self) -> None:
        self.assertIn("not shift invariant", CERT["axis_limit_measure"])
        self.assertIn("maximal-entropy", CERT["orbit_averaged_limit_measure"])

    def test_extensive_pressure(self) -> None:
        self.assertEqual(CERT["claim_status"]["packet_mahler_pressure"], "PROVED")
        self.assertIn("-s kappa_J", CERT["axis_packet_pressure"])

    def test_numerics_are_not_promoted(self) -> None:
        self.assertEqual(CERT["claim_status"]["numerical_slope_separation"], "NUMERICAL_OBSERVATION")

    def test_mutations(self) -> None:
        self.assertEqual(CERT["mutation_audit"]["attempted"], 26)
        self.assertTrue(CERT["mutation_audit"]["all_rejected"])

    def test_independent(self) -> None:
        self.assertTrue(INDEPENDENT["check"])
        self.assertTrue(INDEPENDENT["all_checks_match"])

    def test_firewall(self) -> None:
        self.assertEqual(CERT["claim_status"]["arithmetic_advance"], "NO")
        self.assertFalse(CERT["claim_status"]["route_b_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
