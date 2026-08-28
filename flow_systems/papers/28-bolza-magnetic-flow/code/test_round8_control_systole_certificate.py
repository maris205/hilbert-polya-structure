#!/usr/bin/env python3
"""Tests for the P28 Round-8 exact control-systole certificate."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import unittest

import build_round8_control_systole_certificate as builder


PROJECT = Path(__file__).resolve().parents[1]
RESULTS = PROJECT / "results"


class Round8ControlSystoleCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (RESULTS / "round8_control_systole_source_matrix.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            cls.sources = list(csv.DictReader(handle))
        cls.certificate_path = RESULTS / "round8_control_finite_ball_certificate.json"
        cls.validation_path = RESULTS / "round8_control_systole_validation.json"
        cls.certificate = json.loads(cls.certificate_path.read_text(encoding="utf-8"))
        cls.validation = json.loads(cls.validation_path.read_text(encoding="utf-8"))

    def test_01_freeze_is_immutable(self) -> None:
        self.assertEqual(
            builder.sha256_file(builder.FREEZE_PATH), builder.EXPECTED_FREEZE_SHA256
        )

    def test_02_round7_upstream_bytes_are_locked(self) -> None:
        for relative_path, expected in builder.UPSTREAM_LOCKS.items():
            self.assertEqual(builder.sha256_file(PROJECT / relative_path), expected)

    def test_03_source_inclusion_and_exclusion_counts(self) -> None:
        self.assertEqual(len(self.sources), 6)
        self.assertEqual(
            sum(row["decision"].startswith("INCLUDE") for row in self.sources), 3
        )
        self.assertEqual(
            sum(row["decision"].startswith("EXCLUDE") for row in self.sources), 3
        )

    def test_04_source_locators_dates_and_claim_boundaries_are_present(self) -> None:
        self.assertEqual({row["access_date"] for row in self.sources}, {"2026-08-28"})
        for row in self.sources:
            self.assertTrue(row["identifier"])
            self.assertTrue(row["claim_support"])
            self.assertTrue(row["claim_boundary"])
            self.assertTrue(row["overall_grade"])

    def test_05_all_exact_generator_inverse_pairs_reduce_to_identity(self) -> None:
        generators = builder.generator_numerators()
        for index in range(4):
            state = builder.multiply_state(builder.IDENTITY, generators[index])
            state = builder.multiply_state(state, generators[index + 4])
            self.assertEqual(state, builder.IDENTITY)

    def test_06_published_relator_reduces_to_exact_identity(self) -> None:
        state = builder.IDENTITY
        generators = builder.generator_numerators()
        for step in (0, 5, 2, 7, 4, 1, 6, 3):
            state = builder.multiply_state(state, generators[step])
        self.assertEqual(state, builder.IDENTITY)

    def test_07_g0_g3_has_identically_zero_systole_difference(self) -> None:
        generators = builder.generator_numerators()
        witness = builder.multiply_state(builder.IDENTITY, generators[0])
        witness = builder.multiply_state(witness, generators[3])
        self.assertNotEqual(witness, builder.IDENTITY)
        self.assertEqual(
            builder.certified_poly_sign(
                builder.systole_difference_polynomial(witness)
            )[0],
            0,
        )

    def test_08_alternating_vertex_is_strictly_inside_outer_radius(self) -> None:
        guard = self.certificate["proof_guards"]["vertex_radius_order"]
        self.assertEqual(guard["status"], "PASS")
        self.assertEqual(guard["equivalent_check"], "u^4>1/2")

    def test_09_fundamental_polygon_radius_guard_passes(self) -> None:
        guard = self.certificate["proof_guards"]["fundamental_polygon_radius"]
        self.assertEqual(guard["status"], "PASS")
        self.assertEqual(guard["claim"], "2*atanh(u)<3")

    def test_10_candidate_is_strictly_below_frozen_cutoff(self) -> None:
        guard = self.certificate["proof_guards"]["candidate_below_cutoff"]
        self.assertEqual(guard["status"], "PASS")
        self.assertIn("<21/10", guard["claim"])

    def test_11_center_radius_guard_passes_exactly(self) -> None:
        guard = self.certificate["proof_guards"]["center_radius_guard"]
        self.assertEqual(guard["status"], "PASS")
        self.assertEqual(guard["claim"], "cosh(111/20)^2<20000")

    def test_12_certificate_has_theorem_level_status(self) -> None:
        self.assertEqual(
            self.certificate["status"],
            "PASS_EXACT_SYSTOLE_AND_FINITE_COMPLETENESS",
        )
        self.assertEqual(self.certificate["evidence_token"], "PROVED")

    def test_13_finite_component_state_count_and_closure(self) -> None:
        finite = self.certificate["finite_completeness"]
        self.assertEqual(finite["included_state_count"], 18533)
        self.assertTrue(finite["component_boundary_closed"])
        self.assertFalse(finite["resource_cap_reached"])

    def test_14_discovery_depth_histogram_is_frozen(self) -> None:
        self.assertEqual(
            self.certificate["finite_completeness"]["discovery_depth_histogram"],
            {
                "0": 1,
                "1": 8,
                "2": 56,
                "3": 392,
                "4": 1632,
                "5": 3976,
                "6": 5104,
                "7": 4168,
                "8": 2260,
                "9": 752,
                "10": 176,
                "11": 8,
            },
        )

    def test_15_exact_included_state_stream_hash_is_frozen(self) -> None:
        self.assertEqual(
            self.certificate["finite_completeness"][
                "included_state_stream_sha256"
            ],
            "814f72badce2cc90e8e26edc2a7db18d52c4c334c0f5dfc5bf7d8e4a90dcf545",
        )

    def test_16_exact_rejected_boundary_is_frozen(self) -> None:
        finite = self.certificate["finite_completeness"]
        self.assertEqual(finite["rejected_boundary_state_count"], 108616)
        self.assertEqual(
            finite["rejected_boundary_stream_sha256"],
            "3017c21285daad5a1173b076c9b5700975f67cdbbdaa8a6218e80d4bc89da6f4",
        )

    def test_17_every_interval_sign_resolved_at_frozen_order(self) -> None:
        finite = self.certificate["finite_completeness"]
        self.assertEqual(finite["inside_sign_taylor_order_histogram"], {"24": 18532})
        self.assertEqual(
            finite["outside_sign_taylor_order_histogram"], {"24": 108616}
        )
        self.assertEqual(
            finite["systole_sign_taylor_order_histogram"],
            {"0": 144, "24": 18388},
        )

    def test_18_exact_systole_formula_and_witness_are_frozen(self) -> None:
        systole = self.certificate["exact_systole"]
        self.assertEqual(
            systole["formula"], "2*acosh(1/(2*exp(-1/5)-1))"
        )
        self.assertEqual(systole["equality_witness"], "g0*g3")
        self.assertTrue(systole["decimal"].startswith("2.043026655880296214455945667"))

    def test_19_all_finite_nonidentity_states_meet_lower_bound(self) -> None:
        systole = self.certificate["exact_systole"]
        self.assertTrue(systole["all_nonidentity_states_at_least_candidate"])
        self.assertEqual(systole["strictly_above_state_count"], 18388)
        self.assertEqual(systole["equality_state_count_in_finite_component"], 144)
        self.assertEqual(18388 + 144, 18533 - 1)

    def test_20_systolic_witness_is_primitive(self) -> None:
        systole = self.certificate["exact_systole"]
        self.assertTrue(systole["witness_primitive"])
        self.assertIn("proper root", systole["primitivity_reason"].lower())

    def test_21_common_cutoff_is_frozen_only_after_certificate(self) -> None:
        execution = self.certificate["execution"]
        self.assertTrue(execution["control_systole_verified"])
        self.assertTrue(execution["finite_word_to_length_completeness_verified"])
        self.assertTrue(execution["common_geometric_cutoff_frozen"])
        self.assertEqual(execution["common_geometric_cutoff"], "21/10")

    def test_22_no_census_or_comparison_was_run(self) -> None:
        execution = self.certificate["execution"]
        for field in (
            "control_census_run",
            "bolza_census_run",
            "comparison_run",
            "target_data_used",
            "arithmetic_labels_assigned",
        ):
            self.assertFalse(execution[field], field)

    def test_23_route_a_and_route_b_firewalls_hold(self) -> None:
        execution = self.certificate["execution"]
        route_a = self.certificate["route_a"]
        self.assertFalse(execution["a2_evaluation_run"])
        self.assertFalse(execution["route_b_invocation_allowed"])
        self.assertEqual(route_a["formal_full_candidate_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(route_a["bounded_proxy_overall"], "ROUTE_A_EXPLORATORY")

    def test_24_validation_hashes_and_evidence_tokens_are_consistent(self) -> None:
        self.assertEqual(self.validation["status"], "PASS")
        self.assertEqual(self.validation["evidence_token"], "PROVED")
        self.assertEqual(self.validation["errors"], [])
        self.assertEqual(
            self.validation["source_matrix_sha256"],
            builder.sha256_file(RESULTS / "round8_control_systole_source_matrix.csv"),
        )
        self.assertEqual(
            self.validation["certificate_payload_sha256"],
            hashlib.sha256(self.certificate_path.read_bytes()).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
