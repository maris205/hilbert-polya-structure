#!/usr/bin/env python3
import json
import unittest

import round6_nielsen_sensitivity as nielsen
import round5_matched_marked_word as round5


class NielsenSensitivityRound6Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = nielsen.load_freeze()
        cls.panel = nielsen.panel_markings()
        cls.rows, cls.metrics = nielsen.build_payload()

    def test_01_freeze_is_hash_pinned_target_free_and_pilot_disclosed(self) -> None:
        self.assertEqual(nielsen.sha256(self.freeze_raw), nielsen.FREEZE_SHA256)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))
        self.assertEqual(
            self.freeze["pilot_disclosure"]["status"],
            "DISCLOSED_NON_EVIDENTIARY_FEASIBILITY_PILOT",
        )
        self.assertFalse(self.metrics["pilot_values_used_as_evidence"])

    def test_02_panel_is_identity_plus_all_24_elementary_right_moves(self) -> None:
        self.assertEqual(len(self.panel), 25)
        self.assertEqual(self.panel[0]["marking_id"], "ID")
        moves = {
            (row["target"], row["source"], row["exponent"])
            for row in self.panel[1:]
        }
        expected = {
            (target, source, exponent)
            for target in range(4)
            for source in range(4)
            if target != source
            for exponent in (1, -1)
        }
        self.assertEqual(moves, expected)

    def test_03_each_elementary_move_has_an_explicit_inverse(self) -> None:
        base = nielsen.base_marking()
        for row in self.panel[1:]:
            moved = row["marking"]
            restored = nielsen.apply_elementary_move(
                moved, row["target"], row["source"], -row["exponent"]
            )
            self.assertEqual(restored, base)

    def test_04_rank_four_symbolic_owner_census_is_fixed(self) -> None:
        owners = round5.enumerate_marked_owners(4)
        self.assertEqual(len(owners), 2074)
        self.assertEqual(sum(owner["multiplicity"] for owner in owners), 19624)
        self.assertEqual(sum(owner["exponent"] == 1 for owner in owners), 2046)

    def test_05_both_systems_have_all_25_summary_rows_under_same_count(self) -> None:
        self.assertEqual(len(self.rows), 50)
        by_system = {}
        for row in self.rows:
            by_system.setdefault(row["system_id"], []).append(row)
            self.assertEqual(row["positive_generator_count"], "4")
            self.assertEqual(row["alphabet_size"], "8")
            self.assertEqual(row["marked_owner_rows"], "2074")
            self.assertEqual(row["raw_cyclically_reduced_linear_words"], "19624")
        self.assertEqual({key: len(value) for key, value in by_system.items()}, {
            "BIANCHI_LEVEL3_NIELSEN_PANEL": 25,
            "FIVE_TWO_STABILIZED_NIELSEN_PANEL": 25,
        })
        self.assertEqual(
            {row["marking_id"] for row in by_system["BIANCHI_LEVEL3_NIELSEN_PANEL"]},
            {row["marking_id"] for row in by_system["FIVE_TWO_STABILIZED_NIELSEN_PANEL"]},
        )

    def test_06_candidate_exact_matrix_and_level_contract_passes(self) -> None:
        self.assertTrue(self.metrics["candidate_all_exact_determinants_one"])
        self.assertTrue(self.metrics["candidate_all_level3_membership"])
        candidate = [row for row in self.rows if row["system_id"].startswith("BIANCHI")]
        self.assertTrue(all(float(row["maximum_matrix_determinant_residual"]) == 0 for row in candidate))
        self.assertTrue(all(row["all_candidate_level3_membership"] == "true" for row in candidate))

    def test_07_control_presentation_precision_and_redundant_marking_are_explicit(self) -> None:
        self.assertEqual(self.metrics["control_snappy_version"], "3.3.2")
        self.assertEqual(self.metrics["control_precision_bits"], 212)
        self.assertEqual(self.metrics["control_base_four_marking"], ["a", "b", "ab", "aB"])
        self.assertEqual(self.metrics["control_four_marking_status"], "TIETZE_REDUNDANT_NOT_PRESENTATION_MATCHED")
        self.assertLess(self.metrics["control_maximum_determinant_residual"], 1e-55)
        self.assertAlmostEqual(
            self.metrics["control_maximum_determinant_residual"],
            6.32823398779997454e-58,
            delta=1e-72,
        )

    def test_08_phase_panel_is_complete_numeric_and_digest_bound(self) -> None:
        self.assertEqual(self.metrics["markings_per_system"], 25)
        self.assertEqual(self.metrics["summary_rows"], 50)
        for row in self.rows:
            self.assertEqual(len(row["evaluation_digest"]), 64)
            self.assertGreater(int(row["primitive_loxodromic_phase_rows"]), 0)
            self.assertTrue(float(row["null_sample_sd_abs_q"]) > 0)

    def test_09_frozen_decision_rule_is_applied_without_authorizing_metric_work(self) -> None:
        criteria = self.metrics["robustness_criteria"]
        self.assertEqual(self.metrics["marking_robustness_pass"], all(criteria.values()))
        expected = (
            self.freeze["comparison"]["decision_if_all_conditions_pass"]
            if all(criteria.values())
            else self.freeze["comparison"]["decision_otherwise"]
        )
        self.assertEqual(self.metrics["paper_decision"], expected)
        self.assertFalse(self.metrics["metric_bianchi_prefix_authorized"])

    def test_10_route_and_claim_boundaries_fail_closed(self) -> None:
        self.assertEqual(
            self.metrics["formal_route_a_tuple"],
            [
                "A0_WEAK_ARITHMETIC_RELATION",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FAIL",
            ],
        )
        self.assertEqual(self.metrics["overall_verdict"], "ROUTE_A_EXPLORATORY")
        self.assertEqual(self.metrics["route_tuple_owner"], "P24-BIANCHI-MARKED-WORD-PROXY")
        self.assertEqual(self.metrics["full_bianchi_flow_route_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["orbit_to_gaussian_prime_ideal_map"], "OPEN")
        self.assertEqual(self.metrics["full_group_conjugacy_or_primitive_completeness"], "NOT_CLAIMED")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["prime_or_zero_target_data_used"])

    def test_11_render_is_byte_deterministic_and_source_bound(self) -> None:
        first = nielsen.rendered_outputs()
        second = nielsen.rendered_outputs()
        self.assertEqual(first, second)
        core = {
            path: data
            for path, data in first.items()
            if path not in {nielsen.RECEIPT_PATH, nielsen.VALIDATION_PATH}
        }
        receipt = json.loads(first[nielsen.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], nielsen.combined_hash(core))
        for relative, binding in receipt["source_bindings"].items():
            payload = (nielsen.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], nielsen.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))


if __name__ == "__main__":
    unittest.main()
