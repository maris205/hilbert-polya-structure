#!/usr/bin/env python3
"""Unit tests for HCS-P61."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERT = json.loads((PROJECT / "results" / "c61_certificate.json").read_text())
INDEPENDENT = json.loads((PROJECT / "results" / "c61_independent_check.json").read_text())


class TransversalityTests(unittest.TestCase):
    def test_candidate(self) -> None:
        self.assertTrue(CERT["check"])
        self.assertEqual(CERT["candidate_id"], "HCS-P61")

    def test_all_period_theorem(self) -> None:
        self.assertEqual(CERT["claim_status"]["physical_all_period_transversality"], "PROVED")
        self.assertIn("eigenvalue", CERT["transversality_implication"])

    def test_counts(self) -> None:
        self.assertEqual(
            [row["physical_simple_roots"] for row in CERT["finite_exact_rows"]],
            [1, 1, 2, 4, 6, 12],
        )

    def test_formal_degrees(self) -> None:
        self.assertEqual(
            [row["formal_degree"] for row in CERT["finite_exact_rows"]],
            [2, 2, 6, 14, 28, 62],
        )

    def test_transverse_intervals(self) -> None:
        self.assertTrue(all(row["physical_derivatives_exclude_zero"] for row in CERT["finite_exact_rows"]))

    def test_mutations(self) -> None:
        self.assertEqual(CERT["mutation_audit"]["attempted"], 22)
        self.assertTrue(CERT["mutation_audit"]["all_rejected"])

    def test_independent(self) -> None:
        self.assertTrue(INDEPENDENT["check"])
        self.assertTrue(INDEPENDENT["all_counts_and_words_match"])

    def test_scope(self) -> None:
        self.assertEqual(CERT["claim_status"]["ambient_all_period_transversality"], "OPEN")
        self.assertFalse(CERT["route_b_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
