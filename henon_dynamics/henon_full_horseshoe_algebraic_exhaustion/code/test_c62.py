#!/usr/bin/env python3
"""Unit tests for HCS-P62."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERT = json.loads((PROJECT / "results" / "c62_certificate.json").read_text())
INDEPENDENT = json.loads((PROJECT / "results" / "c62_independent_check.json").read_text())


class AlgebraicExhaustionTests(unittest.TestCase):
    def test_candidate(self) -> None:
        self.assertTrue(CERT["check"])
        self.assertEqual(CERT["candidate_id"], "HCS-P62")

    def test_parameter_conjugacy(self) -> None:
        parameter = CERT["parameter_conjugacy"]
        self.assertTrue(parameter["six_inside_plateau"])
        self.assertTrue(parameter["path_from_6_to_10_inside_plateau"])

    def test_all_period_exhaustion(self) -> None:
        status = CERT["claim_status"]
        self.assertEqual(status["all_complex_periodic_points_real_and_simple"], "PROVED")
        self.assertEqual(status["ambient_all_period_transversality"], "PROVED")
        self.assertEqual(status["formal_dynatomic_effectivity"], "PROVED")

    def test_full_shift_counts(self) -> None:
        rows = CERT["all_period_fixed_point_rows"]
        self.assertEqual([row["fixed_points_of_nth_iterate"] for row in rows], [2**n for n in range(1, 14)])

    def test_finite_degrees(self) -> None:
        self.assertEqual(
            [row["primitive_degree"] for row in CERT["finite_exact_rows"]],
            [2, 2, 6, 14, 28, 62, 126],
        )

    def test_finite_total_reality(self) -> None:
        self.assertTrue(all(row["all_primitive_roots_real"] for row in CERT["finite_exact_rows"]))
        self.assertTrue(all(row["all_primitive_roots_simple"] for row in CERT["finite_exact_rows"]))

    def test_half_words(self) -> None:
        exact = CERT["finite_exact_rows"][:-1]
        self.assertTrue(all(row["unique_half_sign_words"] == row["primitive_degree"] for row in exact))
        self.assertEqual(CERT["finite_exact_rows"][-1]["half_word_certificate"], "NOT_RUN_THEOREM_INDEPENDENT")

    def test_mutations(self) -> None:
        self.assertEqual(CERT["mutation_audit"]["attempted"], 26)
        self.assertTrue(CERT["mutation_audit"]["all_rejected"])

    def test_independent(self) -> None:
        self.assertTrue(INDEPENDENT["check"])
        self.assertTrue(INDEPENDENT["all_checks_match"])

    def test_scope(self) -> None:
        self.assertEqual(CERT["claim_status"]["arithmetic_advance"], "NO")
        self.assertFalse(CERT["route_a_status"]["full_arithmetic_candidate_pass"])
        self.assertFalse(CERT["route_b_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
