#!/usr/bin/env python3
import json
import unittest

import round2_bianchi_ledger as bianchi
import round7_trace_discriminant as trace_disc


class TraceDiscriminantRound7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = trace_disc.load_freeze()
        cls.records = trace_disc.ordered_records()
        cls.rows, cls.metrics = trace_disc.build_payload()

    def test_01_freeze_is_hash_pinned_and_target_free(self) -> None:
        self.assertEqual(trace_disc.sha256(self.freeze_raw), trace_disc.FREEZE_SHA256)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))
        self.assertEqual(
            self.freeze["invariant"]["status"],
            "SOURCE_DERIVED_NECESSARY_INVARIANT_NOT_OWNER_MAP",
        )

    def test_02_exact_matrix_census_and_order_are_frozen(self) -> None:
        self.assertEqual(len(self.records), 11481)
        self.assertEqual(len(self.rows), 11481)
        self.assertEqual(self.rows[0]["representative_word"], "e")
        order_keys = [
            (
                len(record["representative"]),
                record["representative"],
                bianchi.mat_flat(matrix),
            )
            for matrix, record in self.records
        ]
        self.assertEqual(order_keys, sorted(order_keys))

    def test_03_every_frozen_matrix_is_exact_level3_sl2(self) -> None:
        self.assertTrue(self.metrics["all_determinants_one"])
        self.assertTrue(self.metrics["all_level3_membership"])
        self.assertTrue(all(bianchi.mat_det(matrix) == bianchi.ONE for matrix, _ in self.records))
        self.assertTrue(all(bianchi.in_level_three(matrix) for matrix, _ in self.records))

    def test_04_determinant_expansion_proves_trace_divisibility(self) -> None:
        for matrix, _record in self.records:
            a = trace_disc.matrix_a(matrix)
            trace = bianchi.mat_trace(matrix)
            quotient = trace_disc.g_exact_divide(trace_disc.g_sub(trace, (2, 0)), 9)
            self.assertEqual(quotient, bianchi.g_neg(bianchi.mat_det(a)))
        self.assertTrue(self.metrics["all_integrality_identities_pass"])

    def test_05_d9_is_an_exact_gaussian_integer_on_every_row(self) -> None:
        for (matrix, _record), row in zip(self.records, self.rows, strict=True):
            invariant = (int(row["d9_re"]), int(row["d9_im"]))
            numerator = trace_disc.g_sub(
                bianchi.g_square(bianchi.mat_trace(matrix)), (4, 0)
            )
            self.assertEqual(bianchi.g_mul((9, 0), invariant), numerator)

    def test_06_conjugacy_witness_is_exact_for_every_matrix(self) -> None:
        conjugator = bianchi.GENERATORS["U1"]
        for matrix, _record in self.records:
            conjugate = bianchi.mat_mul(
                bianchi.mat_mul(conjugator, matrix), bianchi.mat_inv(conjugator)
            )
            self.assertEqual(trace_disc.d9(conjugate), trace_disc.d9(matrix))
        self.assertTrue(self.metrics["all_conjugacy_witnesses_pass"])

    def test_07_inversion_witness_is_exact_for_every_matrix(self) -> None:
        for matrix, _record in self.records:
            self.assertEqual(trace_disc.d9(bianchi.mat_inv(matrix)), trace_disc.d9(matrix))
        self.assertTrue(self.metrics["all_inversion_witnesses_pass"])

    def test_08_integer_recurrence_matches_declared_initial_values(self) -> None:
        trace = (5, -2)
        values = trace_disc.s_values(trace, 4)
        self.assertEqual(values[0], bianchi.ONE)
        self.assertEqual(values[1], trace)
        for index in range(2, 5):
            self.assertEqual(
                values[index],
                trace_disc.g_sub(bianchi.g_mul(trace, values[index - 1]), values[index - 2]),
            )

    def test_09_repetition_identity_passes_for_r1_through_r5(self) -> None:
        for matrix, _record in self.records:
            invariant = trace_disc.d9(matrix)
            recurrence = trace_disc.s_values(bianchi.mat_trace(matrix), 4)
            for exponent in range(1, 6):
                self.assertEqual(
                    trace_disc.d9(bianchi.mat_pow(matrix, exponent)),
                    bianchi.g_mul(invariant, bianchi.g_square(recurrence[exponent - 1])),
                )
        self.assertTrue(self.metrics["all_repetition_witnesses_r1_to_r5_pass"])

    def test_10_class_counts_and_collision_boundary_are_pinned(self) -> None:
        self.assertEqual(self.metrics["matrix_class_counts"], {
            "IDENTITY": 1,
            "LOXODROMIC": 10976,
            "PARABOLIC": 504,
        })
        self.assertEqual(self.metrics["distinct_d9_values"], 145)
        self.assertEqual(self.metrics["d9_collision_rows_beyond_first"], 11336)
        witness = self.metrics["owner_separation_witness"]
        self.assertEqual(
            witness["status"],
            "PROVED_DISTINCT_UNORIENTED_GAMMA3_OWNERS_WITH_EQUAL_D9",
        )
        self.assertEqual(trace_disc.d9(trace_disc.OWNER_WITNESS_GAMMA_1), (13, 0))
        self.assertEqual(trace_disc.d9(trace_disc.OWNER_WITNESS_GAMMA_2), (13, 0))
        residue_1 = trace_disc.a_residue_mod3(trace_disc.OWNER_WITNESS_GAMMA_1)
        residue_2 = trace_disc.a_residue_mod3(trace_disc.OWNER_WITNESS_GAMMA_2)
        self.assertNotEqual(residue_1, residue_2)
        self.assertNotEqual(trace_disc.negate_residue_mod3(residue_1), residue_2)
        for conjugator, _record in self.records:
            conjugate = bianchi.mat_mul(
                bianchi.mat_mul(conjugator, trace_disc.OWNER_WITNESS_GAMMA_1),
                bianchi.mat_inv(conjugator),
            )
            self.assertEqual(trace_disc.a_residue_mod3(conjugate), residue_1)
        self.assertEqual(
            trace_disc.a_residue_mod3(bianchi.mat_inv(trace_disc.OWNER_WITNESS_GAMMA_1)),
            trace_disc.negate_residue_mod3(residue_1),
        )
        self.assertTrue(self.metrics["d9_noninjective_on_unoriented_gamma3_owners"])
        self.assertTrue(all(row["evidence_status"] == "NUMERICALLY_CERTIFIED" for row in self.rows))
        self.assertTrue(all(row["arithmetic_mode"] == "EXACT_GAUSSIAN_INTEGER" for row in self.rows))
        self.assertEqual(
            self.metrics["completeness_boundary"],
            bianchi.COMPLETENESS_BOUNDARY,
        )

    def test_11_route_and_claim_firewalls_fail_closed(self) -> None:
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

    def test_12_render_is_deterministic_and_receipt_binds_sources_and_outputs(self) -> None:
        first = trace_disc.rendered_outputs()
        second = trace_disc.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[trace_disc.RECEIPT_PATH])
        material = {
            path: data for path, data in first.items() if path != trace_disc.RECEIPT_PATH
        }
        self.assertEqual(receipt["material_sha256"], trace_disc.combined_hash(material))
        for relative, binding in receipt["output_bindings"].items():
            data = first[trace_disc.Path(relative)]
            self.assertEqual(binding["sha256"], trace_disc.sha256(data))
            self.assertEqual(binding["bytes"], len(data))
        for relative, binding in receipt["source_bindings"].items():
            data = (trace_disc.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], trace_disc.sha256(data))
            self.assertEqual(binding["bytes"], len(data))


if __name__ == "__main__":
    unittest.main()
