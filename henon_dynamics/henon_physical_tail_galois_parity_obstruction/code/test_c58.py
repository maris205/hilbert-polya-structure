#!/usr/bin/env python3
"""Schema and claim-firewall tests for the HCS-P58 certificate."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


CERTIFICATE = Path(__file__).resolve().parents[1] / "results" / "c58_certificate.json"


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_candidate(self) -> None:
        self.assertEqual(self.certificate["candidate_id"], "HCS-P58")

    def test_trace_degrees(self) -> None:
        algebra = self.certificate["reflection_algebra"]
        self.assertEqual(algebra["A8_vertex_vertex"]["trace_degree"], 12)
        self.assertEqual(algebra["B8_edge_edge"]["trace_degree"], 6)
        self.assertEqual(algebra["A9_B9_vertex_edge"]["trace_degree"], 28)

    def test_total_reality(self) -> None:
        self.assertTrue(all(
            row["all_trace_roots_real_by_sturm"]
            for row in self.certificate["reflection_algebra"].values()
        ))

    def test_physical_embeddings(self) -> None:
        p9 = self.certificate["reflection_algebra"]["A9_B9_vertex_edge"]
        self.assertEqual(set(p9["physical_embeddings"]), {"A9", "B9"})
        self.assertEqual(p9["physical_embeddings"]["A9"]["trace_index"], 0)
        self.assertEqual(p9["physical_embeddings"]["B9"]["trace_index"], 27)

    def test_parity_signs(self) -> None:
        parity = self.certificate["parity_falsifier"]
        self.assertEqual(parity["Delta_6_exact_sign"], "negative")
        self.assertEqual(parity["Delta_7_exact_sign"], "positive")
        self.assertGreater(parity["Delta_6_integer_margin"], 0)
        self.assertGreater(parity["Delta_7_integer_margin"], 0)

    def test_physical_tail_scope(self) -> None:
        tail = self.certificate["fixed_point_tail"]
        self.assertTrue(tail["stable_eigenvalue_positive"])
        self.assertIn("not the sum", tail["scope"])

    def test_claim_firewall(self) -> None:
        self.assertFalse(self.certificate["route_a_status"]["full_galois_A2_pass"])
        self.assertFalse(self.certificate["route_b_authorized"])
        self.assertEqual(self.certificate["arithmetic_advance"], "NO")

    def test_mutations(self) -> None:
        audit = self.certificate["mutation_audit"]
        self.assertEqual(audit["attempted"], 21)
        self.assertEqual(audit["rejected"], 21)
        self.assertTrue(audit["all_rejected"])


if __name__ == "__main__":
    unittest.main()
