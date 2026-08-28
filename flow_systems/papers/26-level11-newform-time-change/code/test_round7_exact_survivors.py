#!/usr/bin/env python3
"""Tests for the P26 Round-7 exact survivor classifier."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round7_exact_survivors.py")
SPEC = importlib.util.spec_from_file_location("p26_round7_under_test", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round7_exact_survivors.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Round7ExactSurvivorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cycle_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER)
        cls.moment_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND6_MOMENT_LEDGER)
        cls.rows, cls.model = MODULE.build_classification_rows(
            cls.cycle_rows, cls.moment_rows
        )

    def test_locked_source_hashes(self) -> None:
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER),
            MODULE.EXPECTED_ROUND4_CYCLE_SHA256,
        )
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND6_MOMENT_LEDGER),
            MODULE.EXPECTED_ROUND6_MOMENT_SHA256,
        )

    def test_coset_and_schreier_counts(self) -> None:
        transversal, tree_arcs = MODULE.schreier_transversal()
        self.assertEqual(len(transversal), 12)
        self.assertEqual(len(tree_arcs), 11)
        self.assertEqual(set(transversal), {(0, 1), *((1, j) for j in range(11))})

    def test_relation_rank_and_nullity(self) -> None:
        arcs, relations = MODULE.relation_matrix()
        _, pivots = MODULE.rref(relations)
        dual = MODULE.nullspace_basis(relations)
        self.assertEqual((len(arcs), len(relations), len(pivots), len(dual)), (24, 35, 21, 3))
        for relation in relations:
            for vector in dual:
                self.assertEqual(sum(a * b for a, b in zip(relation, vector)), 0)

    def test_euclidean_decomposition_round_trip(self) -> None:
        matrices = [
            MODULE.IDENTITY,
            MODULE.T_MATRIX,
            MODULE.power(MODULE.T_MATRIX, -7),
            MODULE.multiply(
                MODULE.S_MATRIX,
                MODULE.multiply(MODULE.power(MODULE.T_MATRIX, 11), MODULE.S_MATRIX),
            ),
        ]
        matrices.extend(
            MODULE.exact_degree_five_cycle(word)[1] for word in MODULE.FROZEN_WORDS
        )
        for matrix in matrices:
            product = MODULE.word_product(MODULE.decompose_sl2(matrix))
            self.assertIn(product, (matrix, tuple(-entry for entry in matrix)))

    def test_cusp_direction_and_other_cusp_relation(self) -> None:
        arcs, relations = MODULE.relation_matrix()
        dual = MODULE.nullspace_basis(relations)
        infinity = MODULE.homology_coordinates(MODULE.T_MATRIX, arcs, dual)
        other_matrix = MODULE.multiply(
            MODULE.S_MATRIX,
            MODULE.multiply(MODULE.power(MODULE.T_MATRIX, 11), MODULE.S_MATRIX),
        )
        other = MODULE.homology_coordinates(other_matrix, arcs, dual)
        self.assertNotEqual(infinity, (Fraction(0),) * 3)
        self.assertTrue(MODULE.in_rational_span(other, infinity))
        self.assertTrue(
            MODULE.in_rational_span(MODULE.add_coordinates(other, infinity), infinity)
        )

    def test_four_exact_cycle_owners_match_locked_round4_rows(self) -> None:
        locked, _ = MODULE.source_maps(self.cycle_rows, self.moment_rows)
        for word in MODULE.FROZEN_WORDS:
            cycle, owner = MODULE.exact_degree_five_cycle(word)
            self.assertEqual(len(cycle), 5)
            self.assertEqual(
                MODULE.parse_matrix(locked[word]["cycle_owner_matrix"]), owner
            )
            self.assertEqual(MODULE.determinant(owner), 1)
            self.assertEqual(owner[2] % 11, 0)

    def test_all_four_are_exact_real_projection_kernels(self) -> None:
        self.assertEqual(tuple(row["word"] for row in self.rows), MODULE.FROZEN_WORDS)
        self.assertTrue(all(row["real_projection_zero_exact"] == "true" for row in self.rows))
        self.assertEqual(MODULE.validate_rows(self.rows), [])

    def test_degree_one_real_period_identity_is_exact(self) -> None:
        self.assertTrue(
            all(
                row["degree_one_real_projection_equal_exact"] == "true"
                for row in self.rows
            )
        )
        self.assertTrue(
            all(
                row["exact_lambda_a_p_squared_group_moment_survivor"] == "true"
                for row in self.rows
            )
        )

    def test_two_full_source_kernels(self) -> None:
        kernels = {
            row["word"]
            for row in self.rows
            if row["exact_classification"] == "EXACT_SOURCE_KERNEL"
        }
        self.assertEqual(kernels, {"LRRLRRR", "LLRLLRLR"})
        self.assertTrue(
            all(
                row["full_complex_period_zero_exact"] == "true"
                for row in self.rows
                if row["word"] in kernels
            )
        )

    def test_two_nonzero_purely_imaginary_periods(self) -> None:
        projection_only = {
            row["word"]
            for row in self.rows
            if row["exact_classification"]
            == "EXACT_REAL_PROJECTION_KERNEL_NONZERO_FULL_PERIOD"
        }
        self.assertEqual(projection_only, {"LLLRLLRLR", "LLLRLRLLR"})
        self.assertTrue(
            all(
                row["exact_period_character"] == "PURELY_IMAGINARY_AND_NONZERO"
                for row in self.rows
                if row["word"] in projection_only
            )
        )

    def test_numerical_values_are_cross_checks_only(self) -> None:
        self.assertTrue(all(row["round6_numerical_survivor"] == "true" for row in self.rows))
        self.assertTrue(all(row["proof_evidence_token"] == "PROVED" for row in self.rows))
        self.assertTrue(
            all(row["quadrature_evidence_token"] == "NUMERICAL_OBSERVATION" for row in self.rows)
        )

    def test_fail_closed_validator_rejects_uncertified_row(self) -> None:
        tampered = [dict(row) for row in self.rows]
        tampered[0]["real_projection_zero_exact"] = "false"
        self.assertTrue(MODULE.validate_rows(tampered))

    def test_route_boundary_and_target_data_prohibition(self) -> None:
        self.assertTrue(all(row["target_data_used"] == "false" for row in self.rows))
        self.assertTrue(all(row["formal_a2_evaluation_run"] == "false" for row in self.rows))
        self.assertTrue(all(row["route_b_invocation_allowed"] == "false" for row in self.rows))
        self.assertEqual(self.model["homology_dimension_y0_11_over_q"], 3)
        self.assertEqual(self.model["compact_homology_dimension_x0_11_over_q"], 2)


if __name__ == "__main__":
    unittest.main()
