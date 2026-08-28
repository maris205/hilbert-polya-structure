#!/usr/bin/env python3
import json
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction

import round8_roof_nontransfer as roof


class RoofNontransferRound8Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = roof.load_freeze()
        cls.witnesses, cls.replay, cls.summary = roof.build_payload()

    def test_01_freeze_is_pinned_and_target_free(self) -> None:
        self.assertEqual(roof.sha256(self.freeze_raw), roof.FREEZE_SHA256)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))
        self.assertEqual(
            self.freeze["objects"]["physical_clock"],
            "EUCLIDEAN_FLIGHT_LENGTH",
        )

    def test_02_locked_input_is_pinned(self) -> None:
        payload = (roof.PROJECT_ROOT / roof.INPUT_PATH).read_bytes()
        self.assertEqual(roof.sha256(payload), roof.INPUT_SHA256)
        self.assertEqual(len(roof.read_locked_ledger()), 2241)

    def test_03_exact_periodic_average_gap_is_positive(self) -> None:
        exact = roof.exact_geometry(Fraction(6))
        with localcontext() as context:
            context.prec = 80
            self.assertEqual(
                exact["period_three_mean"] - exact["period_two_mean"],
                exact["gap"],
            )
        self.assertGreater(exact["gap"], Decimal(0))
        self.assertLess(exact["gap"], Decimal(1))

    def test_04_exact_length_formulas_hold_for_all_frozen_geometries(self) -> None:
        for distance in (Fraction(29, 5), Fraction(6), Fraction(31, 5)):
            exact = roof.exact_geometry(distance)
            with localcontext() as context:
                context.prec = 80
                self.assertEqual(exact["period_two_total"], 2 * exact["period_two_mean"])
                self.assertEqual(exact["period_three_total"], 3 * exact["period_three_mean"])
                self.assertEqual(exact["gap"], Decimal(2) - exact["sqrt_three"])

    def test_05_minimax_bound_is_half_the_witness_gap(self) -> None:
        exact = roof.exact_geometry(Fraction(6))
        with localcontext() as context:
            context.prec = 80
            self.assertEqual(exact["minimax_lower_bound"] * 2, exact["gap"])
            midpoint = (exact["period_two_mean"] + exact["period_three_mean"]) / 2
            errors = (
                abs(midpoint - exact["period_two_mean"]),
                abs(midpoint - exact["period_three_mean"]),
            )
            self.assertEqual(max(errors), exact["minimax_lower_bound"])

    def test_06_six_exact_witness_rows_pass_locked_replay(self) -> None:
        self.assertEqual(len(self.witnesses), 6)
        self.assertTrue(all(row["locked_ledger_formula_check"] == "PASS" for row in self.witnesses))
        self.assertEqual(
            {row["orbit_family"] for row in self.witnesses},
            {"TWO_DISK_BOUNCE", "THREE_DISK_EQUILATERAL_TRIANGLE"},
        )

    def test_07_full_replay_keeps_every_frozen_owner(self) -> None:
        self.assertEqual(len(self.replay), 2241)
        grouped = {}
        for row in self.replay:
            grouped.setdefault(row["d_over_a_exact"], []).append(row)
        self.assertEqual(set(grouped), {"29/5", "6", "31/5"})
        self.assertTrue(all(len(rows) == 747 for rows in grouped.values()))

    def test_08_only_three_period_two_owners_match_the_scalar_per_geometry(self) -> None:
        for metrics in self.summary["geometry_summaries"].values():
            self.assertEqual(metrics["rows_agreeing_with_period_two_scalar_clock"], 3)
            self.assertEqual(metrics["rows_disagreeing_with_period_two_scalar_clock"], 744)

    def test_09_cohomology_and_transfer_claim_boundaries_are_explicit(self) -> None:
        self.assertIn("PERIOD_TWO_AND_THREE_AVERAGES_DIFFER", self.summary["cohomology_argument"])
        self.assertEqual(
            self.summary["global_scalar_substitution"],
            "REFUTED_FOR_OWNER_AND_REPETITION_PRESERVING_TRANSFER",
        )
        self.assertEqual(
            self.summary["physical_weighted_transfer_operator"],
            "NOT_REFUTED_MAY_REQUIRE_NONCONSTANT_ROOF",
        )

    def test_10_route_tuple_and_owner_firewall_are_intact(self) -> None:
        self.assertEqual(list(roof.FORMAL_TUPLE), self.summary["formal_route_a_tuple"])
        self.assertEqual(self.summary["tuple_owner"], "UNIT_ROOF_SYMBOLIC_CALIBRATOR_ONLY")
        self.assertEqual(self.summary["physical_three_disk_route_tuple"], "UNASSIGNED")
        self.assertEqual(self.summary["overall_verdict"], "ROUTE_A_REJECTED")
        self.assertFalse(self.summary["route_b_invocation_allowed"])
        self.assertFalse(self.summary["prime_or_zero_tables_used"])

    def test_11_render_is_byte_deterministic_and_source_bound(self) -> None:
        first = roof.rendered_outputs()
        second = roof.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[roof.RECEIPT_PATH])
        for relative, binding in receipt["source_bindings"].items():
            payload = (roof.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], roof.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))

    def test_12_receipt_binds_core_outputs_and_validation(self) -> None:
        rendered = roof.rendered_outputs()
        core = {path: rendered[path] for path in roof.RESULT_PATHS.values()}
        receipt = json.loads(rendered[roof.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], roof.combined_hash(core))
        for path, payload in core.items():
            self.assertEqual(receipt["files"][path.as_posix()]["sha256"], roof.sha256(payload))
            self.assertEqual(receipt["files"][path.as_posix()]["bytes"], len(payload))
        validation = rendered[roof.VALIDATION_PATH]
        self.assertEqual(receipt["validation_binding"]["sha256"], roof.sha256(validation))
        self.assertEqual(receipt["validation_binding"]["bytes"], len(validation))


if __name__ == "__main__":
    unittest.main()
