#!/usr/bin/env python3
import json
import unittest

import round5_matched_marked_word as matched


class MatchedMarkedWordRound5Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = matched.load_frozen_contract()
        (
            cls.candidate_rows,
            cls.control_rows,
            cls.comparison,
            cls.metrics,
        ) = matched.build_payload()

    def test_01_pre_result_freeze_is_hash_pinned_and_target_free(self) -> None:
        self.assertEqual(matched.sha256(self.freeze_raw), matched.FREEZE_SHA256)
        self.assertEqual(
            self.freeze["schema"], "p24-round5-matched-marked-word-freeze/1.0"
        )
        self.assertEqual(
            self.freeze["comparison"]["complex_phase_length_moment"],
            "q=corr(length,cos(theta))+i*corr(length,sin(theta))",
        )
        self.assertTrue(
            all(value is False for value in self.freeze["forbidden_inputs"].values())
        )

    def test_02_dihedral_canonicalization_is_rotation_and_inverse_invariant(self) -> None:
        word = (0, 2, 3, 4, 1)
        canonical = matched.canonical_owner(word)
        for rotated in matched.rotations(word):
            self.assertEqual(matched.canonical_owner(rotated), canonical)
        for rotated in matched.rotations(matched.inverse_word(word)):
            self.assertEqual(matched.canonical_owner(rotated), canonical)

    def test_03_symbolic_roots_and_repetitions_are_exact(self) -> None:
        primitive = matched.canonical_owner((0, 2, 1, 3))
        repeated = matched.canonical_owner(primitive * 2)
        root, exponent = matched.symbolic_root(repeated)
        self.assertEqual(root, primitive)
        self.assertEqual(exponent, 2)
        self.assertEqual(matched.symbolic_root(primitive), (primitive, 1))

    def test_04_frozen_owner_and_raw_word_counts(self) -> None:
        candidate = self.metrics["candidate"]
        control = self.metrics["control"]
        self.assertEqual(candidate["raw_cyclically_reduced_linear_words"], 19624)
        self.assertEqual(candidate["marked_owner_rows"], 2074)
        self.assertEqual(candidate["symbolically_primitive_owner_rows"], 2046)
        self.assertEqual(candidate["symbolic_repetition_owner_rows"], 28)
        self.assertEqual(control["raw_cyclically_reduced_linear_words"], 372)
        self.assertEqual(control["marked_owner_rows"], 51)
        self.assertEqual(control["symbolically_primitive_owner_rows"], 41)
        self.assertEqual(control["symbolic_repetition_owner_rows"], 10)

    def test_05_candidate_exact_layer_and_relation_rows(self) -> None:
        self.assertTrue(self.metrics["candidate_all_exact_determinants_one"])
        self.assertTrue(self.metrics["candidate_all_level3_membership"])
        self.assertEqual(self.metrics["candidate"]["identity_owner_rows"], 2)
        self.assertEqual(self.metrics["candidate"]["parabolic_owner_rows"], 132)
        self.assertEqual(self.metrics["candidate"]["loxodromic_owner_rows"], 1940)
        self.assertTrue(
            all(row["matrix_determinant_residual"] == "0" for row in self.candidate_rows)
        )

    def test_06_control_presentation_and_high_precision_contract(self) -> None:
        contract = self.metrics["control_numerical_contract"]
        self.assertEqual(contract["snappy_version"], "3.3.2")
        self.assertEqual(contract["precision_bits"], 212)
        self.assertEqual(contract["generators"], ["a", "b"])
        self.assertEqual(contract["relators"], ["aBBBabbAAbb"])
        self.assertEqual(contract["named_control_isometry_check"], "RIGOROUS_TRUE")
        self.assertLess(contract["maximum_determinant_residual"], 1e-55)
        self.assertLess(
            contract["maximum_parabolic_trace_squared_minus_four_residual"],
            1e-55,
        )
        self.assertGreater(
            contract["minimum_loxodromic_trace_squared_minus_four_gap"], 1.0
        )
        self.assertEqual(self.metrics["control"]["identity_owner_rows"], 0)

    def test_07_contract_is_algorithm_matched_but_not_marking_count_matched(self) -> None:
        self.assertTrue(self.metrics["same_executable_enumeration_contract"])
        self.assertTrue(self.metrics["same_canonicalization"])
        self.assertTrue(self.metrics["same_symbolic_primitivity_rule"])
        self.assertTrue(self.metrics["same_marked_orbit_multiplicity_rule"])
        self.assertEqual(self.metrics["same_marked_word_cutoff"], 5)
        self.assertTrue(self.metrics["same_comparison_precision_contract"])
        self.assertIn(
            "COMMON_BINARY64", self.metrics["comparison_precision_contract"]
        )
        self.assertEqual(self.metrics["candidate_positive_generator_rank"], 4)
        self.assertEqual(self.metrics["control_positive_generator_rank"], 2)
        self.assertIn(
            "MARKED_POSITIVE_GENERATOR_COUNT",
            self.metrics["generator_rank_semantics"],
        )
        self.assertEqual(
            self.metrics["alphabet_size_and_presentation_confound"],
            "RETAINED_AND_EXPLICIT",
        )

    def test_08_frozen_phase_statistic_uses_only_primitive_loxodromics(self) -> None:
        self.assertTrue(self.comparison["statistic_frozen_before_result_execution"])
        self.assertEqual(self.comparison["candidate"]["rows_used"], 1932)
        self.assertEqual(self.comparison["control"]["rows_used"], 39)
        self.assertEqual(self.comparison["candidate"]["null_replicates"], 64)
        self.assertEqual(self.comparison["control"]["null_replicates"], 64)
        self.assertGreaterEqual(
            self.comparison["absolute_permutation_standardized_phase_contrast"], 0
        )
        self.assertFalse(self.comparison["prime_or_zero_target_data_used"])

    def test_09_evidence_and_route_boundaries_are_fail_closed(self) -> None:
        self.assertFalse(self.metrics["forbidden_target_data_used"])
        self.assertEqual(self.metrics["metric_length_spectrum"], "NOT_CLAIMED")
        self.assertEqual(
            self.metrics["full_group_conjugacy_completeness"], "NOT_CLAIMED"
        )
        self.assertEqual(self.metrics["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["a2_a4_evaluation"], "NOT_EVALUATED")
        self.assertEqual(self.metrics["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])

    def test_10_render_is_byte_deterministic(self) -> None:
        first = matched.rendered_outputs()
        second = matched.rendered_outputs()
        self.assertEqual(first, second)
        first_core = {
            path: data
            for path, data in first.items()
            if path not in {matched.RECEIPT_PATH, matched.VALIDATION_PATH}
        }
        receipt = json.loads(first[matched.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], matched.combined_hash(first_core))
        self.assertEqual(
            tuple(receipt["source_bindings"]),
            tuple(path.as_posix() for path in matched.SOURCE_BINDING_PATHS),
        )
        for relative, binding in receipt["source_bindings"].items():
            payload = (matched.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], matched.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))


if __name__ == "__main__":
    unittest.main()
