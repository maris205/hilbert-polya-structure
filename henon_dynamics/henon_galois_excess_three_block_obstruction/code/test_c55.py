#!/usr/bin/env python3
"""Regression tests for HCS-P55."""

from __future__ import annotations

import json
import unittest

import sympy as sp

import c55_galois_blocks as c55
import independent_check


class C55Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = c55.build_certificate()

    def test_dependency_locks(self) -> None:
        self.assertEqual(len(self.certificate["dependency_locks"]), 8)

    def test_primitive_cycle_counts(self) -> None:
        self.assertEqual(
            self.certificate["symbolic_cycle_certificate"]["primitive_cycle_counts_through_5"],
            {"1": 1, "2": 0, "3": 1, "4": 2, "5": 2},
        )

    def test_one_and_two_block_relation(self) -> None:
        rows = self.certificate["symbolic_cycle_certificate"]["incidence_relations"]
        self.assertIn("gamma_4a", rows["width_1"]["relation"])
        self.assertEqual(rows["width_1"]["relation"], rows["width_2"]["relation"])

    def test_three_block_relation(self) -> None:
        relation = self.certificate["symbolic_cycle_certificate"]["incidence_relations"]["width_3"]
        self.assertEqual(relation["row_order"], ["gamma_3", "gamma_4a", "gamma_4b", "gamma_5"])
        self.assertEqual(relation["relation"], "N(gamma_3)+N(gamma_5)=N(gamma_4a)+N(gamma_4b)")

    def test_width_four_finite_sharpness(self) -> None:
        row = self.certificate["symbolic_cycle_certificate"]["width_4_finite_interpolation"]
        self.assertEqual(row["matrix_rank"], 5)
        self.assertEqual(row["selected_determinant"], -1)
        self.assertIn("five exact witnesses", row["scope"])

    def test_period_four_exact_trace(self) -> None:
        row = self.certificate["exact_orbit_algebra"]["period_4a"]
        self.assertEqual(sp.sympify(row["trace"]), -574 - 192 * sp.sqrt(6))
        self.assertEqual(row["galois_excess_formula"], "acosh(287-96*sqrt(6))")

    def test_period_five_trace_field(self) -> None:
        row = self.certificate["exact_orbit_algebra"]["period_5"]
        self.assertEqual(row["trace_root_counts"], [1] * 6)
        self.assertEqual(sp.Poly(sp.sympify(row["trace_polynomial"]), c55.T).degree(), 6)
        self.assertEqual(sp.Poly(sp.sympify(row["multiplier_minimal_polynomial"]), c55.Z).degree(), 12)

    def test_period_five_physical_embedding(self) -> None:
        row = self.certificate["exact_orbit_algebra"]["period_5"]
        self.assertEqual(row["physical_coordinate_root_count"], 1)
        self.assertEqual(
            row["physical_embedding_certificate"]["derivative_root_counts"],
            {"b": 0, "c": 0, "trace": 0},
        )
        self.assertEqual(
            row["physical_embedding_certificate"]["derivative_midpoint_signs"],
            {"b": 1, "c": 1, "trace": -1},
        )
        self.assertEqual(
            row["physical_embedding_certificate"]["coordinate_signs"],
            ["negative", "negative", "positive", "positive", "negative"],
        )

    def test_strict_excess_obstruction(self) -> None:
        row = self.certificate["three_block_obstruction"]
        self.assertEqual(row["status"], "PROVED")
        self.assertIn("E_3+E_5>E_4a+E_4b", row["actual_strict_inequality"])

    def test_no_holder_promotion(self) -> None:
        self.assertIn("does not refute general Holder", self.certificate["livsic_scope_firewall"]["finite_holder_interpolation"])
        self.assertFalse(self.certificate["route_b_authorized"])

    def test_mutations_all_rejected(self) -> None:
        audit = self.certificate["mutation_audit"]
        self.assertTrue(audit["all_rejected"])
        self.assertEqual(audit["attempted"], 17)
        self.assertEqual(len(set(audit["labels"])), 17)

    def test_canonical_hash_stable(self) -> None:
        core = c55.core_payload()
        self.assertEqual(self.certificate["core_sha256"], c55.canonical_sha(core))

    def test_independent_reconstruction(self) -> None:
        reconstructed = independent_check.reconstruct()
        self.assertTrue(reconstructed["strict_obstruction"])
        self.assertEqual(reconstructed["width_4_interpolation_determinant"], -1)

    def test_certificate_json_round_trip(self) -> None:
        encoded = json.dumps(self.certificate, sort_keys=True)
        self.assertEqual(json.loads(encoded)["candidate_id"], "HCS-P55")


if __name__ == "__main__":
    unittest.main()
