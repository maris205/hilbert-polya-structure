#!/usr/bin/env python3
import json
import math
import unittest

import round8_homology_renormalization as renorm


class HomologyRenormalizationRound8Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = renorm.load_freeze()
        cls.quadrants, cls.coefficients, cls.summary = renorm.build_payload()

    def test_01_freeze_is_pinned_target_free_and_new_owner(self) -> None:
        self.assertEqual(renorm.sha256(self.freeze_raw), renorm.FREEZE_SHA256)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))
        self.assertEqual(
            self.freeze["new_owner_notice"],
            "THIS_IS_NOT_THE_ROUND7_RESIDUAL_INVERSE_LIMIT_OWNER",
        )

    def test_02_locked_inputs_are_pinned(self) -> None:
        for name, (path, digest) in renorm.INPUT_LOCKS.items():
            payload = (renorm.PROJECT_ROOT / path).read_bytes()
            self.assertEqual(renorm.sha256(payload), digest, name)

    def test_03_source_owner_panel_is_exactly_three_primitive_content_one_owners(self) -> None:
        owners = renorm.source_owner_rows()
        self.assertEqual(set(owners), set(renorm.OWNER_IDS))
        self.assertTrue(all(row["homology_content"] == "1" for row in owners.values()))
        self.assertTrue(all(row["base_conjugacy_primitive"] == "true" for row in owners.values()))

    def test_04_deck_degree_order_and_lift_count_identity(self) -> None:
        for modulus in renorm.MODULI:
            self.assertEqual(modulus**4, modulus * modulus**3)
        self.assertTrue(
            all(
                int(row["deck_degree"])
                == int(row["exact_owner_order_in_deck_group"])
                * int(row["primitive_lift_component_count"])
                for row in self.quadrants
            )
        )

    def test_05_series_coefficient_formula_matches_binomial_expansion(self) -> None:
        self.assertEqual(renorm.series_coefficient(3, 8, 1), 0)
        self.assertEqual(renorm.series_coefficient(3, 8, 3), 8)
        self.assertEqual(renorm.series_coefficient(3, 8, 6), math.comb(9, 2))
        self.assertEqual(renorm.series_coefficient(1, 1, 12), 1)

    def test_06_output_row_counts_cover_all_four_quadrants(self) -> None:
        self.assertEqual(len(self.quadrants), 3 * 8 * 4)
        self.assertEqual(len(self.coefficients), 3 * 8 * 4 * 13)
        self.assertEqual(
            {row["quadrant_id"] for row in self.quadrants},
            {quadrant["quadrant_id"] for quadrant in renorm.QUADRANTS},
        )

    def test_07_raw_clock_quadrants_escape_fixed_prefixes(self) -> None:
        raw = [
            row
            for row in self.quadrants
            if row["quadrant_id"]
            in {"Q00_RAW_CLOCK_RAW_MULTIPLICITY", "Q01_RAW_CLOCK_GEOMETRIC_MEAN"}
        ]
        self.assertTrue(
            all(
                row["first_nonconstant_degree"] == row["modulus_N"]
                and row["all_level_or_asymptotic_status"]
                == "COEFFICIENTWISE_TO_1_ON_EVERY_FIXED_PREFIX"
                for row in raw
            )
        )

    def test_08_time_rescaling_alone_has_divergent_first_coefficient(self) -> None:
        rows = [
            row
            for row in self.quadrants
            if row["quadrant_id"] == "Q10_RESCALED_CLOCK_RAW_MULTIPLICITY"
        ]
        self.assertTrue(all(row["first_nonconstant_degree"] == "1" for row in rows))
        self.assertTrue(
            all(
                int(row["coefficient_at_first_nonconstant_degree"])
                == int(row["modulus_N"]) ** 3
                for row in rows
            )
        )

    def test_09_both_interventions_recover_base_factor_exactly(self) -> None:
        rows = [
            row
            for row in self.quadrants
            if row["quadrant_id"] == "Q11_RESCALED_CLOCK_GEOMETRIC_MEAN"
        ]
        self.assertEqual(len(rows), 24)
        self.assertTrue(all(row["first_nonconstant_degree"] == "1" for row in rows))
        self.assertTrue(all(row["coefficient_at_first_nonconstant_degree"] == "1" for row in rows))
        self.assertTrue(all(row["formal_owner_factor"].endswith("^1)^(-1)") for row in rows))
        q11_coefficients = [
            row
            for row in self.coefficients
            if row["quadrant_id"] == "Q11_RESCALED_CLOCK_GEOMETRIC_MEAN"
        ]
        self.assertTrue(all(row["coefficient"] == "1" for row in q11_coefficients))

    def test_10_route_and_full_flow_boundaries_are_intact(self) -> None:
        self.assertEqual(self.summary["formal_route_a_tuple"], list(renorm.FORMAL_TUPLE))
        self.assertEqual(self.summary["overall_verdict"], "ROUTE_A_REJECTED")
        self.assertEqual(
            self.summary["finite_replay_evidence_status"],
            "NUMERICALLY_CERTIFIED",
        )
        self.assertEqual(
            self.summary["finite_replay_arithmetic_mode"],
            "EXACT_INTEGER",
        )
        self.assertEqual(self.summary["same_owner_round7_verdict"], "ROUTE_A_REJECTED_UNCHANGED")
        self.assertEqual(self.summary["full_flow_determinant"], "NOT_DEFINED_FINITE_OWNER_PANEL_ONLY")
        self.assertFalse(self.summary["cover_tower_residual"])
        self.assertFalse(self.summary["route_b_invocation_allowed"])
        self.assertFalse(self.summary["prime_or_zero_tables_used"])

    def test_11_render_is_byte_deterministic_and_source_bound(self) -> None:
        first = renorm.rendered_outputs()
        second = renorm.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[renorm.RECEIPT_PATH])
        for relative, binding in receipt["source_bindings"].items():
            payload = (renorm.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], renorm.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))

    def test_12_receipt_binds_core_outputs_and_validation(self) -> None:
        rendered = renorm.rendered_outputs()
        core = {path: rendered[path] for path in renorm.RESULT_PATHS.values()}
        receipt = json.loads(rendered[renorm.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], renorm.combined_hash(core))
        for path, payload in core.items():
            self.assertEqual(receipt["files"][path.as_posix()]["sha256"], renorm.sha256(payload))
            self.assertEqual(receipt["files"][path.as_posix()]["bytes"], len(payload))
        validation = rendered[renorm.VALIDATION_PATH]
        self.assertEqual(receipt["validation_binding"]["sha256"], renorm.sha256(validation))
        self.assertEqual(receipt["validation_binding"]["bytes"], len(validation))


if __name__ == "__main__":
    unittest.main()
