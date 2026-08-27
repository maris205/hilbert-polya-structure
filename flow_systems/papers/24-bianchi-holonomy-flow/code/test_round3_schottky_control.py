#!/usr/bin/env python3
import unittest

import round3_schottky_control as control


class SchottkyRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ping_pong = control.exact_ping_pong_checks()
        cls.reduced_words = control.enumerate_reduced_words()
        cls.domains, cls.rows, cls.controls, cls.metrics = control.build_payload()

    def test_multiplier_and_boundary_scale_are_exact(self) -> None:
        self.assertNotEqual(control.MU[1], 0)
        self.assertEqual(control.g_norm_squared(control.MU), control.MU_ABS_SQUARED)
        self.assertEqual(
            control.MU_ABS_SQUARED * control.RADIUS_RATIO**2,
            control.DELTA**2,
        )
        self.assertTrue(self.ping_pong["boundary_modulus_identity"])

    def test_all_eight_closed_round_disks_are_strictly_disjoint(self) -> None:
        self.assertEqual(len(self.ping_pong["domains"]), 8)
        self.assertEqual(len(self.ping_pong["pairwise_squared_gaps"]), 28)
        self.assertTrue(self.ping_pong["all_closed_disks_pairwise_disjoint"])
        self.assertGreater(self.ping_pong["minimum_pairwise_squared_gap"], 0)

    def test_exact_conjugacy_and_inverse_boundary_maps(self) -> None:
        self.assertEqual(self.ping_pong["exact_conjugacy_identities_checked"], 8)
        for positive, repelling, attracting in control.FIXED_POINT_SPECS:
            h = control.h_matrix(repelling, attracting)
            forward = control.GENERATORS[positive]
            backward = control.GENERATORS[positive + "m"]
            self.assertEqual(
                control.mat_mul(h, forward),
                control.mat_mul(control.diagonal_matrix(control.MU), h),
            )
            self.assertEqual(
                control.mat_mul(h, backward),
                control.mat_mul(control.mat_inv(control.diagonal_matrix(control.MU)), h),
            )

    def test_frozen_reduced_word_count_and_exact_injectivity(self) -> None:
        self.assertEqual(len(self.reduced_words), 22409)
        keys = [control.projective_key(matrix) for _word, matrix in self.reduced_words]
        self.assertEqual(len(set(keys)), 22409)

    def test_cyclic_classes_have_exact_roots_repetitions_and_orientation_pairs(self) -> None:
        rows_by_word = {row["oriented_cyclic_word"]: row for row in self.rows}
        self.assertTrue(rows_by_word)
        for row in self.rows:
            word = tuple(row["oriented_cyclic_word"].split("."))
            root = tuple(row["symbolic_root"].split("."))
            exponent = int(row["repetition_exponent"])
            self.assertEqual(root * exponent, word)
            inverse_class = control.canonical_rotation(control.inverse_word(word))
            self.assertIn(control.word_text(inverse_class), rows_by_word)
            if exponent == 1:
                self.assertEqual(
                    row["primitive_status"],
                    "PRIMITIVE_CONJUGACY_CLASS_IN_FREE_GROUP",
                )
            else:
                self.assertEqual(row["primitive_status"], "REPETITION_IN_FREE_GROUP")

    def test_every_class_is_certified_loxodromic_with_stability(self) -> None:
        self.assertTrue(self.rows)
        for row in self.rows:
            self.assertEqual(row["loxodromic_status"], "LOXODROMIC_BY_CLASSICAL_SCHOTTKY_THEOREM")
            self.assertGreater(float(row["complex_length_re"]), 0.0)
            self.assertLess(float(row["stable_multiplier_abs"]), 1.0)
            self.assertGreater(float(row["unstable_multiplier_abs"]), 1.0)
            self.assertLess(float(row["invariant_reconstruction_relative_residual"]), 1e-10)

    def test_intrinsic_shuffle_is_target_free_and_preserves_lengths(self) -> None:
        rows_by_id = {row["row_id"]: row for row in self.rows}
        self.assertTrue(self.controls)
        for row in self.controls:
            source = rows_by_id[row["row_id"]]
            self.assertEqual(row["complex_length_fixed"], source["complex_length_re"])
            self.assertEqual(row["repetition_exponent_fixed"], "1")
            self.assertEqual(row["target_data_used"], "false")
            self.assertEqual(row["arithmetic_owner"], "NONE_BY_CONSTRUCTION")

    def test_route_and_claim_boundaries_are_not_promoted(self) -> None:
        self.assertEqual(self.metrics["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["a2_a4_evaluation"], "NOT_EVALUATED")
        self.assertEqual(self.metrics["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["forbidden_target_data_used"])
        self.assertIn("NOT_FINITE_VOLUME_MATCHED", self.metrics["completeness_boundary"])
        self.assertEqual(self.metrics["ambient_thin_arithmetic_containment"], "OPEN")

    def test_core_render_is_byte_deterministic(self) -> None:
        first, first_metrics = control.core_outputs()
        second, second_metrics = control.core_outputs()
        self.assertEqual(first, second)
        self.assertEqual(first_metrics, second_metrics)
        self.assertEqual(control.combined_hash(first), control.combined_hash(second))


if __name__ == "__main__":
    unittest.main()
