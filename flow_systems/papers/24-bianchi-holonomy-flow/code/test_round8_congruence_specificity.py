#!/usr/bin/env python3
import json
import unittest

import round2_bianchi_ledger as bianchi
import round7_trace_discriminant as round7
import round8_congruence_specificity as round8


class CongruenceSpecificityRound8Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = round8.load_freeze()
        cls.controls = round8.control_rows()
        cls.profile, cls.collision = round8.collision_payload()
        cls.metrics = round8.build_metrics()
        cls.records = round7.ordered_records()

    def test_01_freeze_is_hash_pinned_and_target_free(self) -> None:
        self.assertEqual(round8.sha256(self.freeze_raw), round8.FREEZE_SHA256)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))
        self.assertEqual(len(self.freeze["arithmetic_controls"]), 4)
        self.assertEqual(
            self.freeze["first_jet_audit"]["owner_claim_boundary"],
            "joint D9/jet descriptors are necessary owner invariants only; residual matrix collisions are not asserted to be distinct conjugacy owners",
        )

    def test_02_quadratic_ring_arithmetic_is_exact(self) -> None:
        self.assertEqual(round8.e_square((0, 1), round8.GAUSSIAN), (-1, 0))
        self.assertEqual(round8.e_square((0, 1), round8.EISENSTEIN), (-1, -1))
        self.assertEqual(
            round8.e_mul((2, 3), (5, -1), round8.GAUSSIAN),
            (13, 13),
        )
        self.assertEqual(
            round8.e_mul((2, 3), (5, -1), round8.EISENSTEIN),
            (13, 16),
        )

    def test_03_universal_formula_passes_every_principal_control_row(self) -> None:
        total = 0
        for ring, level, matrices in round8.principal_control_panels().values():
            for matrix in matrices:
                self.assertEqual(round8.mat_det(matrix, ring), round8.ONE)
                self.assertTrue(round8.in_principal_level(matrix, level))
                self.assertEqual(
                    round8.normalized_discriminant(matrix, level, ring),
                    round8.theorem_formula(matrix, level, ring),
                )
                total += 1
        self.assertEqual(total, 6392)

    def test_04_control_panel_counts_are_pinned(self) -> None:
        self.assertEqual([int(row["matrix_rows"]) for row in self.controls], [4, 485, 1969, 1969, 1969])
        self.assertEqual(
            [int(row["distinct_normalized_discriminants"]) for row in self.controls],
            [1, 21, 29, 49, 69],
        )
        self.assertEqual(self.metrics["finite_control_matrix_rows"], 6396)

    def test_05_ambient_parent_proves_level_hypothesis_is_essential(self) -> None:
        row = self.controls[0]
        self.assertEqual(row["control_id"], "C1-FULL-GAUSSIAN-AMBIENT-PARENT")
        self.assertEqual(row["principal_congruence_rows"], "0")
        self.assertEqual(row["normalized_discriminant_integral_rows"], "1")
        self.assertEqual(row["normalized_discriminant_nonintegral_rows"], "3")
        self.assertEqual(row["exact_result"], "D9_NONINTEGRAL_WITNESSES_PRESENT")

    def test_06_four_families_execute_but_only_two_canonical_types_count(self) -> None:
        gate = self.metrics["a0_control_gate"]
        self.assertEqual(gate["required_minimum"], 3)
        self.assertEqual(gate["executed_distinct_control_families"], 4)
        self.assertEqual(gate["executed_subpanels"], 5)
        self.assertEqual(gate["frozen_control_family_status"], "COMPLETE_4_OF_4")
        self.assertEqual(
            gate["canonical_route_control_types"],
            ["neighboring dynamical parameters", "simpler parent system"],
        )
        self.assertEqual(gate["executed_distinct_canonical_types"], 2)
        self.assertEqual(gate["status"], "INCOMPLETE_2_OF_3_CANONICAL_TYPES")
        self.assertEqual(gate["specificity_verdict"], "REFUTED_D9_IS_NOT_GAUSSIAN_SPECIFIC")

    def test_07_formula_specializes_exactly_to_all_candidate_rows(self) -> None:
        for matrix, _record in self.records:
            a = round7.matrix_a(matrix)
            determinant = bianchi.mat_det(a)
            expected = round7.g_sub(
                bianchi.g_mul((9, 0), bianchi.g_square(determinant)),
                bianchi.g_mul((4, 0), determinant),
            )
            self.assertEqual(round7.d9(matrix), expected)

    def test_08_first_jet_is_invariant_under_gamma3_conjugacy(self) -> None:
        conjugators = [bianchi.GENERATORS[name] for name in ("U1", "Ui", "L1", "Li")]
        for matrix, _record in self.records:
            expected = round8.canonical_first_jet(matrix)
            for conjugator in conjugators:
                conjugate = bianchi.mat_mul(
                    bianchi.mat_mul(conjugator, matrix), bianchi.mat_inv(conjugator)
                )
                self.assertEqual(round8.canonical_first_jet(conjugate), expected)

    def test_09_first_jet_sign_quotient_is_inversion_invariant(self) -> None:
        for matrix, _record in self.records:
            self.assertEqual(
                round8.canonical_first_jet(bianchi.mat_inv(matrix)),
                round8.canonical_first_jet(matrix),
            )

    def test_10_oriented_first_jet_obeys_the_power_law(self) -> None:
        for matrix, _record in self.records:
            for exponent in range(1, 6):
                self.assertEqual(
                    round8.first_jet_power(matrix, exponent),
                    round8.scaled_first_jet(matrix, exponent),
                )

    def test_11_collision_profile_is_exact_and_conservative(self) -> None:
        self.assertEqual(len(self.profile), 145)
        self.assertEqual(sum(int(row["matrix_rows"]) for row in self.profile), 11481)
        self.assertEqual(sum(int(row["distinct_first_jets_up_to_sign"]) for row in self.profile), 517)
        self.assertEqual(
            sum(int(row["joint_descriptor_collisions_beyond_first"]) for row in self.profile),
            10964,
        )
        self.assertTrue(all(
            row["owner_interpretation"] == "NECESSARY_INVARIANT_ONLY_NOT_CONJUGACY_CLASSIFICATION"
            for row in self.profile
        ))

    def test_12_first_jet_strictly_refines_but_does_not_classify(self) -> None:
        audit = self.collision
        self.assertEqual(audit["distinct_d9_values"], 145)
        self.assertEqual(audit["distinct_first_jets_up_to_sign"], 41)
        self.assertEqual(audit["distinct_joint_d9_jet_descriptors"], 517)
        self.assertEqual(audit["collision_rows_separated_by_first_jet"], 372)
        self.assertEqual(audit["collision_reduction_fraction"], "372/11336")
        self.assertEqual(audit["maximum_d9_bucket"], 505)
        self.assertEqual(audit["maximum_joint_descriptor_bucket"], 84)
        self.assertEqual(audit["singleton_joint_descriptor_buckets"], 0)
        self.assertTrue(audit["owner_separation_witness"]["separated_by_first_jet"])

    def test_13_route_and_claim_firewalls_fail_closed(self) -> None:
        self.assertEqual(self.metrics["formal_route_a_tuple"], [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_WEAK",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ])
        self.assertEqual(self.metrics["overall_verdict"], "ROUTE_A_EXPLORATORY")
        self.assertEqual(self.metrics["full_bianchi_flow_route_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["orbit_to_gaussian_prime_ideal_map"], "OPEN")
        self.assertFalse(self.metrics["metric_bianchi_prefix_authorized"])
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["prime_or_zero_target_data_used"])

    def test_14_render_is_deterministic_and_receipt_binds_every_byte(self) -> None:
        first = round8.rendered_outputs()
        second = round8.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[round8.RECEIPT_PATH])
        material = {path: data for path, data in first.items() if path != round8.RECEIPT_PATH}
        self.assertEqual(receipt["material_sha256"], round8.combined_hash(material))
        self.assertEqual(receipt["unit_tests"], {"expected": 14, "failed": 0})
        for relative, binding in receipt["output_bindings"].items():
            data = first[round8.Path(relative)]
            self.assertEqual(binding["sha256"], round8.sha256(data))
            self.assertEqual(binding["bytes"], len(data))
        for relative, binding in receipt["source_bindings"].items():
            data = (round8.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], round8.sha256(data))
            self.assertEqual(binding["bytes"], len(data))


if __name__ == "__main__":
    unittest.main()
