#!/usr/bin/env python3
"""Independent standard-library tests for the P28 Round-5 census."""

from __future__ import annotations

from decimal import Decimal, localcontext
import importlib.util
from itertools import product
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("build_round5_bolza_marked_cyclic_census.py")
SPEC = importlib.util.spec_from_file_location("p28_round5_census", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round5_bolza_marked_cyclic_census.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BolzaMarkedCyclicCensusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.census_rows, cls.raw_counts = MODULE.enumerate_marked_classes()
        cls.branch_rows = MODULE.build_branch_rows(cls.census_rows)
        cls.certificate = MODULE.group_certificate(cls.census_rows, cls.raw_counts)
        cls.control = MODULE.nonarithmetic_control_contract()
        cls.validation = MODULE.validate(
            cls.census_rows, cls.branch_rows, cls.certificate, cls.control
        )
        cls.census_index = MODULE.rows_by_id(cls.census_rows, "census_id")
        cls.branch_index = MODULE.rows_by_id(cls.branch_rows, "row_id")

    def test_01_exact_number_field_replays_generators_and_relator(self) -> None:
        self.assertEqual(self.certificate["status"], "PASS")
        exact = self.certificate["exact_number_field"]
        self.assertTrue(exact["all_generator_determinants_exactly_one"])
        self.assertTrue(exact["polygon_relator_exactly_identity"])
        self.assertEqual(MODULE.matrix_determinant(MODULE.EXACT_GENERATORS[0]), MODULE.ONE)

    def test_02_exhaustive_declared_marked_scope_has_frozen_counts(self) -> None:
        self.assertEqual(self.raw_counts, {1: 8, 2: 56, 3: 344, 4: 2408})
        self.assertEqual(len(self.census_rows), 390)
        counts = {
            length: sum(row["marked_length"] == length for row in self.census_rows)
            for length in range(1, 5)
        }
        self.assertEqual(counts, {1: 4, 2: 16, 3: 60, 4: 310})

    def test_03_canonical_rule_is_rotation_and_inverse_invariant(self) -> None:
        canonical_words = set()
        for row in self.census_rows:
            word = MODULE.parse_word_text(row["canonical_marked_word"])
            canonical_words.add(word)
            self.assertEqual(word, MODULE.canonical_marked_inverse_pair(word))
            for partner in set(MODULE.rotations(word)) | set(
                MODULE.rotations(MODULE.inverse_word(word))
            ):
                self.assertEqual(
                    word, MODULE.canonical_marked_inverse_pair(partner)
                )
        self.assertEqual(len(canonical_words), 390)

    def test_04_marked_power_decomposition_and_exact_matrix_law_hold(self) -> None:
        powers = [row for row in self.census_rows if row["marked_repetition_exponent"] > 1]
        self.assertEqual(len(powers), 24)
        exponent_counts = {
            exponent: sum(row["marked_repetition_exponent"] == exponent for row in powers)
            for exponent in (2, 3, 4)
        }
        self.assertEqual(exponent_counts, {2: 16, 3: 4, 4: 4})
        for row in powers:
            word = MODULE.parse_word_text(row["canonical_marked_word"])
            root, exponent = MODULE.marked_root_decomposition(word)
            self.assertEqual(MODULE.word_text(root), row["marked_root_word"])
            self.assertEqual(
                MODULE.projective_matrix_key(MODULE.word_matrix(word)),
                MODULE.projective_matrix_key(
                    MODULE.matrix_power(MODULE.word_matrix(root), exponent)
                ),
            )

    def test_05_exact_projective_collision_audits_are_clean(self) -> None:
        self.assertEqual(
            self.certificate["exact_projective_matrix_collision_groups"], 0
        )
        self.assertEqual(self.certificate["exact_inverse_pair_collision_groups"], 0)
        self.assertEqual(
            len({row["exact_psl_matrix_key_sha256"] for row in self.census_rows}),
            390,
        )
        self.assertEqual(
            len(
                {
                    row["exact_inverse_paired_psl_key_sha256"]
                    for row in self.census_rows
                }
            ),
            390,
        )
        # Equal trace squared is recorded as an isospectral collision only; it
        # is never silently promoted to Gamma conjugacy.
        self.assertEqual(self.certificate["trace_squared_isospectral_group_count"], 35)
        self.assertGreater(
            self.certificate["trace_squared_isospectral_nontrivial_group_count"], 0
        )

    def test_06_exact_systolic_gate_proves_44_gamma_primitives(self) -> None:
        proved = [
            row
            for row in self.census_rows
            if row["gamma_primitivity_status"]
            == "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE"
        ]
        self.assertEqual(len(proved), 44)
        distribution = {
            length: sum(row["marked_length"] == length for row in proved)
            for length in range(1, 5)
        }
        self.assertEqual(distribution, {1: 4, 2: 12, 3: 16, 4: 12})
        threshold = MODULE.nf_add(MODULE.nf_scale(MODULE.ONE, 10), MODULE.nf_scale(MODULE.S, 8))
        for row in proved:
            word = MODULE.parse_word_text(row["canonical_marked_word"])
            trace = MODULE.matrix_trace(MODULE.word_matrix(word))
            margin = MODULE.nf_sub(threshold, MODULE.nf_abs_real_qsqrt2(trace))
            self.assertGreater(MODULE.q_sqrt2_sign(margin), 0)
            self.assertLess(Decimal(row["bolza_systole_ratio_decimal"]), Decimal(2))

    def test_07_unproved_and_power_records_receive_no_owner_credit(self) -> None:
        open_candidates = [
            row
            for row in self.census_rows
            if row["gamma_primitivity_status"]
            == "NOT_ESTABLISHED_MARKED_PRIMITIVE_ONLY"
        ]
        powers = [row for row in self.census_rows if row["marked_repetition_exponent"] > 1]
        credited = [
            row
            for row in self.census_rows
            if row["owner_credit_status"] == "MINTED_INVERSE_PAIRED_AXIS_OWNER"
        ]
        homology_withheld = [
            row
            for row in self.census_rows
            if row["owner_credit_status"]
            == "WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED"
        ]
        self.assertEqual(len(open_candidates), 322)
        self.assertEqual(len(powers), 24)
        self.assertEqual(len(credited), 36)
        self.assertEqual(len(homology_withheld), 8)
        self.assertEqual(
            len({row["inverse_paired_homology_axis_key"] for row in credited}), 36
        )
        for row in open_candidates + powers + homology_withheld:
            self.assertEqual(row["primitive_axis_owner_id"], "")
            self.assertTrue(str(row["owner_credit_status"]).startswith("WITHHELD"))
        self.assertEqual(
            {row["full_gamma_conjugacy_completeness"] for row in self.census_rows},
            {"NOT_ESTABLISHED"},
        )

    def test_08_signed_k_branch_grid_covers_only_proved_owners(self) -> None:
        self.assertEqual(len(self.branch_rows), 576)
        self.assertEqual({row["source_k"] for row in self.branch_rows}, {-4, -3, -2, -1, 1, 2, 3, 4})
        for field_b in ("+1/2", "-1/2"):
            rows = [row for row in self.branch_rows if row["field_b"] == field_b]
            self.assertEqual(len(rows), 288)
            self.assertEqual(len({row["primitive_axis_owner_id"] for row in rows}), 36)
        self.assertEqual(
            sum(abs(row["source_k"]) == 1 for row in self.branch_rows), 144
        )
        self.assertEqual(
            sum(abs(row["source_k"]) > 1 for row in self.branch_rows), 432
        )

    def test_09_inverse_pair_owner_credit_has_no_orientation_double_count(self) -> None:
        for row in list(self.census_rows) + list(self.branch_rows):
            self.assertNotIn("oriented_primitive_owner_id", row)
            self.assertNotIn("orientation_sign", row)
        for row in self.branch_rows:
            self.assertIn("INVERSE_PAIRED_AXIS", row["owner_counting_convention"])
            self.assertEqual(
                row["owner_credit_status"],
                "MINTED_ONCE_PER_INVERSE_PAIRED_AXIS_PER_FIELD",
            )
            canonical = MODULE.parse_word_text(row["canonical_primitive_word"])
            expected_branch = (
                row["canonical_primitive_word"]
                if row["source_k"] > 0
                else MODULE.word_text(MODULE.inverse_word(canonical))
            )
            self.assertEqual(row["branch_primitive_word"], expected_branch)
            self.assertIn(row["canonical_primitive_word"], row["inverse_pair_definition"])

    def test_10_signed_k_partner_is_an_involution_on_one_owner(self) -> None:
        for row in self.branch_rows:
            partner = self.branch_index[row["signed_k_partner_row_id"]]
            self.assertEqual(partner["signed_k_partner_row_id"], row["row_id"])
            self.assertEqual(partner["field_b"], row["field_b"])
            self.assertEqual(partner["source_k"], -row["source_k"])
            self.assertEqual(
                partner["primitive_axis_owner_id"], row["primitive_axis_owner_id"]
            )

    def test_11_field_partner_maps_b_k_to_minus_b_minus_k(self) -> None:
        with localcontext() as context:
            context.prec = MODULE.DECIMAL_PRECISION
            for row in self.branch_rows:
                partner = self.branch_index[row["field_sign_partner_row_id"]]
                self.assertEqual(partner["field_sign_partner_row_id"], row["row_id"])
                self.assertNotEqual(partner["field_b"], row["field_b"])
                self.assertEqual(partner["source_k"], -row["source_k"])
                self.assertEqual(
                    partner["primitive_axis_owner_id"], row["primitive_axis_owner_id"]
                )
                self.assertEqual(
                    Decimal(partner["project_action_per_N_decimal"]),
                    -Decimal(row["project_action_per_N_decimal"]),
                )

    def test_12_period_action_multiplier_and_stability_laws_hold(self) -> None:
        with localcontext() as context:
            context.prec = MODULE.DECIMAL_PRECISION
            sqrt3 = Decimal(3).sqrt()
            sqrt5_over_3 = (Decimal(5) / Decimal(3)).sqrt()
            for row in self.branch_rows:
                ell = Decimal(row["primitive_geodesic_length_decimal"])
                source_k = Decimal(row["source_k"])
                repetition = abs(source_k)
                trace_unit = sqrt5_over_3 * ell
                physical_unit = Decimal(2) / sqrt3 * ell
                action_unit = sqrt3 / Decimal(2) * ell
                tolerance = Decimal("1e-64")
                self.assertLess(
                    abs(Decimal(row["signed_trace_time_decimal"]) - source_k * trace_unit),
                    tolerance,
                )
                self.assertLess(
                    abs(
                        Decimal(row["absolute_total_physical_period_decimal"])
                        - repetition * physical_unit
                    ),
                    tolerance,
                )
                self.assertLess(
                    abs(Decimal(row["project_action_per_N_decimal"]) - source_k * action_unit),
                    tolerance,
                )
                multiplier = Decimal(row["poincare_multiplier_N_to_k_decimal"])
                reciprocal = Decimal(row["poincare_multiplier_N_to_minus_k_decimal"])
                self.assertLess(abs(multiplier * reciprocal - Decimal(1)), tolerance)
                expected_denominator = multiplier.sqrt() - reciprocal.sqrt()
                actual_denominator = Decimal(
                    row["signed_trace_stability_denominator_decimal"]
                )
                scale = max(abs(actual_denominator), abs(expected_denominator), Decimal(1))
                self.assertLess(abs(actual_denominator - expected_denominator) / scale, tolerance)
                self.assertEqual(row["maslov_index"], 0)

    def test_13_round4_seed_is_recovered_without_owner_id_drift(self) -> None:
        self.assertEqual(self.validation["round4_seed_compatibility_checks"], 48)
        old_rows = MODULE.ROUND4.build_rows()
        for old in old_rows:
            matches = [
                row
                for row in self.branch_rows
                if row["field_b"] == old["field_b"]
                and row["primitive_axis_owner_id"] == old["primitive_axis_owner_id"]
                and row["source_k"] == old["source_k"]
            ]
            self.assertEqual(len(matches), 1)

    def test_14_validation_control_and_route_firewalls_pass(self) -> None:
        self.assertEqual(self.validation["status"], "PASS")
        self.assertEqual(self.validation["errors"], [])
        self.assertEqual(self.control["status"], "DESIGN_ONLY_NOT_INSTANTIATED")
        self.assertFalse(self.control["execution"]["geometry_selected"])
        self.assertFalse(self.control["execution"]["comparison_run"])
        for row in list(self.census_rows) + list(self.branch_rows):
            self.assertEqual(row["target_data_used"], "false")
            self.assertEqual(row["arithmetic_label"], "NONE")
            self.assertEqual(row["formal_route_a_tuple"], "UNASSIGNED")
            self.assertEqual(row["route_b_invocation_allowed"], "false")
        self.assertEqual(self.control["formal_route_a_tuple"], "UNASSIGNED")
        self.assertFalse(self.control["route_b_invocation_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
