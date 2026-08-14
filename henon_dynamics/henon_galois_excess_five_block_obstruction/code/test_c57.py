#!/usr/bin/env python3
"""Unit tests for the HCS-P57 exact certificate."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("c57_five_block_obstruction.py")
SPEC = importlib.util.spec_from_file_location("c57", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load c57 module")
C57 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C57)


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = C57.build_certificate()

    def test_candidate_id(self) -> None:
        self.assertEqual(self.certificate["candidate_id"], "HCS-P57")

    def test_cycle_count(self) -> None:
        self.assertEqual(self.certificate["symbolic_certificate"]["primitive_cycle_counts_through_7"]["7"], 4)

    def test_family_words(self) -> None:
        self.assertEqual(self.certificate["symbolic_certificate"]["A7"], "0000021")
        self.assertEqual(self.certificate["symbolic_certificate"]["B7"], "0000231")

    def test_a6_coordinate_degree(self) -> None:
        self.assertEqual(self.certificate["A6_exact_algebra"]["coordinate_polynomial_degree"], 6)

    def test_a6_trace_degree(self) -> None:
        self.assertEqual(self.certificate["A6_exact_algebra"]["trace_polynomial_degree"], 3)

    def test_a6_trace_interval(self) -> None:
        self.assertEqual(self.certificate["A6_exact_algebra"]["physical_trace_interval"], [-54575, -54574])

    def test_period7_degree(self) -> None:
        self.assertEqual(self.certificate["period_7_exact_algebra"]["trace_polynomial_degree"], 14)

    def test_period7_total_reality(self) -> None:
        self.assertTrue(self.certificate["period_7_exact_algebra"]["all_trace_roots_real"])

    def test_shared_trace_field(self) -> None:
        self.assertIn("one irreducible degree-14", self.certificate["period_7_exact_algebra"]["shared_field_statement"])

    def test_delta_sign(self) -> None:
        self.assertEqual(self.certificate["five_block_obstruction"]["strict_sign"], "positive")
        self.assertGreater(float(self.certificate["five_block_obstruction"]["Delta_5_decimal_50"]), 139.0)

    def test_integer_margin(self) -> None:
        self.assertEqual(self.certificate["five_block_obstruction"]["integer_margin"], 554187019465548)

    def test_obstruction(self) -> None:
        self.assertTrue(self.certificate["five_block_obstruction"]["width_at_most_5_obstruction"])

    def test_width_six_sharpness(self) -> None:
        self.assertEqual(self.certificate["finite_sharpness"]["width_6_four_row_determinant"], -1)
        self.assertEqual(self.certificate["finite_sharpness"]["width_6_cumulative_determinant"], 1)

    def test_route_firewall(self) -> None:
        self.assertFalse(self.certificate["route_b_authorized"])
        self.assertEqual(self.certificate["arithmetic_advance"], "NO")

    def test_mutations(self) -> None:
        self.assertEqual(self.certificate["mutation_audit"]["attempted"], 22)
        self.assertTrue(self.certificate["mutation_audit"]["all_rejected"])


if __name__ == "__main__":
    unittest.main()
