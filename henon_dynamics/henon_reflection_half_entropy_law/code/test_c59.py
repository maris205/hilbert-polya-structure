#!/usr/bin/env python3
"""Certificate tests for HCS-P59."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


CERT = Path(__file__).resolve().parents[1] / "results" / "c59_certificate.json"


class ReflectionCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CERT.read_text(encoding="utf-8"))

    def test_candidate(self) -> None:
        self.assertEqual(self.data["candidate_id"], "HCS-P59")

    def test_reversal(self) -> None:
        self.assertEqual(self.data["time_reversal_involution"], [0, 2, 1, 3])
        self.assertEqual(self.data["reversal_identity"], "A=P*A^T*P")

    def test_known_census(self) -> None:
        rows = {row["period"]: row for row in self.data["formula_rows_1_to_32"]}
        self.assertEqual(rows[8], {"period": 8, "primitive_cycles": 5, "reversible_cycles": 3, "edge_edge_cycles": 2, "vertex_vertex_cycles": 1})
        self.assertEqual(rows[16]["reversible_cycles"], 37)
        self.assertEqual(rows[20]["primitive_cycles"], 750)

    def test_family_types(self) -> None:
        lock = self.data["family_axis_lock"]
        self.assertEqual(lock["A8_type"], "vertex_vertex")
        self.assertEqual(lock["B8_type"], "edge_edge")

    def test_half_entropy(self) -> None:
        theorem = self.data["entropy_theorem"]
        self.assertEqual(theorem["full_primitive_entropy"], "log(phi)")
        self.assertEqual(theorem["reflection_primitive_entropy"], "(1/2)log(phi)")
        self.assertEqual(theorem["status"], "PROVED_EXACT_SYMBOLIC_HALF_ENTROPY_LAW")

    def test_scope(self) -> None:
        self.assertIn("does not count algebraic conjugates", self.data["claim_boundary"])
        self.assertFalse(self.data["route_a_status"]["full_arithmetic_candidate_pass"])
        self.assertFalse(self.data["route_b_authorized"])
        self.assertEqual(self.data["arithmetic_advance"], "NO")

    def test_mutations(self) -> None:
        self.assertEqual(self.data["mutation_audit"]["attempted"], 18)
        self.assertTrue(self.data["mutation_audit"]["all_rejected"])


if __name__ == "__main__":
    unittest.main()
