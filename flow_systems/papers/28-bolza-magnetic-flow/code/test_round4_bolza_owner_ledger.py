#!/usr/bin/env python3
"""Independent tests for the P28 Round-4 Bolza owner ledger."""

from __future__ import annotations

from decimal import Decimal, localcontext
import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("build_round4_bolza_owner_ledger.py")
SPEC = importlib.util.spec_from_file_location("p28_round4_owner", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round4_bolza_owner_ledger.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BolzaOwnerLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.certificate = MODULE.group_certificate()
        self.rows = MODULE.build_rows()
        self.indexed = MODULE.rows_by_id(self.rows)

    def test_01_source_locked_group_certificate_passes(self) -> None:
        self.assertEqual(self.certificate["status"], "PASS")
        self.assertEqual(self.certificate["generator_count"], 4)
        self.assertIn("10.20382/jocg.v13i1a5", self.certificate["primary_source"]["article_url"])

    def test_02_determinants_traces_and_relator_are_replayed(self) -> None:
        self.assertLess(
            Decimal(self.certificate["maximum_determinant_residual"]),
            Decimal("1e-100"),
        )
        self.assertLess(
            Decimal(self.certificate["maximum_trace_residual"]), Decimal("1e-100")
        )
        self.assertLess(
            Decimal(self.certificate["polygon_relator_residual"]), Decimal("1e-100")
        )

    def test_03_systole_norm_identity_is_frozen(self) -> None:
        constants = MODULE.bolza_constants()
        with localcontext() as context:
            context.prec = MODULE.DECIMAL_PRECISION
            self.assertLess(
                abs(constants["norm"].ln() - constants["log_norm"]),
                Decimal("1e-100"),
            )
        self.assertIn("SYSTOLE", self.certificate["primitive_owner_certificate"])

    def test_04_grid_and_classification_are_complete_for_declared_scope(self) -> None:
        self.assertEqual(len(self.rows), 48)
        primitive_branches = [
            row
            for row in self.rows
            if row["source_k_class"] == "SIGNED_K_PRIMITIVE_BRANCH"
        ]
        repetition_branches = [
            row
            for row in self.rows
            if row["source_k_class"] == "SIGNED_K_REPETITION_BRANCH"
        ]
        self.assertEqual(len(primitive_branches), 16)
        self.assertEqual(len(repetition_branches), 32)
        self.assertEqual({row["source_k"] for row in self.rows}, {-3, -2, -1, 1, 2, 3})
        for field_b in ("+1/2", "-1/2"):
            field_rows = [row for row in self.rows if row["field_b"] == field_b]
            self.assertEqual(len(field_rows), 24)
            self.assertEqual(
                len({row["primitive_axis_owner_id"] for row in field_rows}), 4
            )
            self.assertEqual(
                sum(abs(row["source_k"]) == 1 for row in field_rows), 8
            )

    def test_05_inverse_pair_is_one_owner_and_signed_k_mints_no_owner_credit(self) -> None:
        for field_b in ("+1/2", "-1/2"):
            for side_index in MODULE.SIDE_PAIRING_INDICES:
                axis_rows = [
                    row
                    for row in self.rows
                    if row["field_b"] == field_b
                    and row["side_pairing_index"] == side_index
                ]
                self.assertEqual(len(axis_rows), 6)
                self.assertEqual(
                    {row["primitive_axis_owner_id"] for row in axis_rows},
                    {f"BOLZA_AXIS_INVERSE_PAIR_{side_index}"},
                )
                self.assertEqual(
                    {row["canonical_primitive_word"] for row in axis_rows},
                    {f"f{side_index}"},
                )
                self.assertEqual(
                    {row["branch_primitive_word"] for row in axis_rows},
                    {f"f{side_index}", f"f{side_index}^-1"},
                )
        for row in self.rows:
            self.assertEqual(row["primitive_root_status"], "PROVED_SYSTOLIC_SIDE_PAIRING")
            self.assertFalse(
                any(
                    key.startswith("oriented_") and key.endswith("_owner_id")
                    for key in row
                )
            )
            self.assertNotIn("orientation" + "_sign", row)
        self.assertIn("cannot be conjugate", self.certificate["inverse_nonconjugacy_certificate"])
        self.assertIn("no oriented-owner credit", self.certificate["inverse_pair_counting_boundary"])

    def test_06_signed_k_partner_is_an_involution_on_the_same_axis_owner(self) -> None:
        for row in self.rows:
            partner = self.indexed[row["signed_k_partner_row_id"]]
            self.assertEqual(partner["signed_k_partner_row_id"], row["row_id"])
            self.assertEqual(partner["field_b"], row["field_b"])
            self.assertEqual(partner["source_k"], -row["source_k"])
            self.assertEqual(
                partner["primitive_axis_owner_id"], row["primitive_axis_owner_id"]
            )
            self.assertEqual(
                partner["absolute_repetition_index"],
                row["absolute_repetition_index"],
            )

    def test_07_field_sign_partner_maps_b_k_to_minus_b_minus_k(self) -> None:
        with localcontext() as context:
            context.prec = MODULE.DECIMAL_PRECISION
            for row in self.rows:
                partner = self.indexed[row["field_sign_partner_row_id"]]
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

    def test_08_period_and_action_repetition_laws_hold(self) -> None:
        constants = MODULE.bolza_constants()
        with localcontext() as context:
            context.prec = MODULE.DECIMAL_PRECISION
            trace_unit = constants["sqrt5_over_3"] * constants["log_norm"]
            physical_unit = Decimal(2) / constants["sqrt3"] * constants["log_norm"]
            action_unit = constants["sqrt3"] / Decimal(2) * constants["log_norm"]
            tolerance = Decimal("1e-65")
            for row in self.rows:
                source_k = Decimal(row["source_k"])
                repetition = abs(source_k)
                self.assertLess(
                    abs(
                        Decimal(row["absolute_total_trace_clock_period_decimal"])
                        - repetition * trace_unit
                    ),
                    tolerance,
                )
                self.assertLess(
                    abs(
                        Decimal(row["signed_trace_time_decimal"])
                        - source_k * trace_unit
                    ),
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
                    abs(
                        Decimal(row["project_action_per_N_decimal"])
                        - source_k * action_unit
                    ),
                    tolerance,
                )

    def test_09_signed_k_stability_and_maslov_contract_holds(self) -> None:
        constants = MODULE.bolza_constants()
        norm = constants["norm"]
        tolerance = Decimal("1e-65")
        with localcontext() as context:
            context.prec = MODULE.DECIMAL_PRECISION
            for row in self.rows:
                source_k = row["source_k"]
                multiplier_k = Decimal(row["poincare_multiplier_N_to_k_decimal"])
                multiplier_minus_k = Decimal(
                    row["poincare_multiplier_N_to_minus_k_decimal"]
                )
                signed_denominator = Decimal(
                    row["signed_trace_stability_denominator_decimal"]
                )
                absolute_denominator = Decimal(
                    row["stability_determinant_sqrt_abs_decimal"]
                )
                expected_k = (
                    norm**source_k
                    if source_k > 0
                    else Decimal(1) / norm ** abs(source_k)
                )
                expected_minus_k = Decimal(1) / expected_k
                expected_signed = expected_k.sqrt() - expected_minus_k.sqrt()
                self.assertLess(abs(multiplier_k - expected_k), tolerance)
                self.assertLess(
                    abs(multiplier_minus_k - expected_minus_k), tolerance
                )
                self.assertLess(
                    abs(multiplier_k * multiplier_minus_k - Decimal(1)), tolerance
                )
                self.assertLess(abs(signed_denominator - expected_signed), tolerance)
                self.assertLess(
                    abs(absolute_denominator - abs(expected_signed)), tolerance
                )
                self.assertEqual(row["maslov_index"], 0)

    def test_10_same_owner_even_subtype_and_open_regimes_stay_separate(self) -> None:
        for row in self.rows:
            self.assertEqual(
                row["trace_owner_status"],
                "PROVED_SOURCE_COMPATIBLE_INVERSE_PAIRED_AXIS_SIGNED_K_EVEN_SUBTYPE",
            )
            self.assertEqual(row["zero_field_status"], "OPEN_NOT_IN_LEDGER")
            self.assertEqual(row["odd_N_status"], "OPEN_NOT_ESTABLISHED")
            self.assertEqual(row["full_all_N_status"], "OPEN_NOT_ESTABLISHED")
            self.assertIn("NO_CREDIT_TRANSFER", row["fixed_operator_status"])

    def test_11_route_and_completeness_firewalls_hold(self) -> None:
        for row in self.rows:
            self.assertIn("NOT_COMPLETE", row["enumeration_completeness"])
            self.assertEqual(row["formal_route_a_tuple"], "UNASSIGNED")
            self.assertEqual(row["route_b_invocation_allowed"], "false")
            self.assertEqual(row["arithmetic_label"], "NONE")
            self.assertEqual(row["target_data_used"], "false")

    def test_12_validation_passes_and_target_tables_are_absent(self) -> None:
        validation = MODULE.validate_rows(self.rows, self.certificate)
        self.assertEqual(validation["status"], "PASS")
        self.assertEqual(validation["explicit_inverse_paired_axis_owners_per_field"], 4)
        self.assertEqual(validation["field_axis_owner_pairs"], 8)
        self.assertEqual(validation["signed_trace_branches_per_field"], 24)
        self.assertEqual(validation["signed_k_primitive_branches_per_field"], 8)
        self.assertEqual(validation["signed_k_primitive_branch_rows"], 16)
        self.assertEqual(validation["oriented_owner_credit_rows"], 0)
        self.assertEqual(validation["field_partner_checks"], 48)
        self.assertEqual(validation["signed_k_partner_checks"], 48)
        self.assertEqual(validation["target_data_rows"], 0)
        serialized = repr(self.rows).lower()
        for forbidden in ("riemann_zero", "zero_table", "prime_table", "von_mangoldt"):
            self.assertNotIn(forbidden, serialized)


if __name__ == "__main__":
    unittest.main(verbosity=2)
