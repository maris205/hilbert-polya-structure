#!/usr/bin/env python3
"""Independent standard-library tests for the P28 Round-6 certificate."""

from __future__ import annotations

import importlib.util
import copy
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name(
    "build_round6_bolza_conjugacy_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("p28_round6_conjugacy", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round6_bolza_conjugacy_certificate.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

RESULTS_DIR = Path(__file__).resolve().parents[1] / "results"


class BolzaRound6ConjugacyCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source_package = MODULE.load_source_package(
            RESULTS_DIR / "round5_bolza_marked_cyclic_census.csv",
            RESULTS_DIR / "round5_bolza_magnetic_branch_ledger.csv",
            RESULTS_DIR / "round5_bolza_marked_cyclic_certificate.json",
            RESULTS_DIR / "round5_bolza_marked_cyclic_validation.json",
            RESULTS_DIR / "round5_nonarithmetic_control_contract.json",
        )
        cls.internal_rows = MODULE.build_conjugacy_rows(cls.source_package)
        cls.public_rows = MODULE.public_conjugacy_rows(cls.internal_rows)
        cls.control_gate = MODULE.nonarithmetic_source_package_gate(
            cls.source_package
        )
        cls.validation = MODULE.validate(
            cls.source_package, cls.internal_rows, cls.control_gate
        )

    def test_01_round5_source_package_is_digest_bound(self) -> None:
        self.assertEqual(
            self.source_package["source_digests"], MODULE.EXPECTED_SOURCE_SHA256
        )
        self.assertEqual(self.source_package["certificate"]["status"], "PASS")
        self.assertEqual(self.source_package["validation"]["status"], "PASS")

    def test_02_exact_generators_and_polygon_relator_replay(self) -> None:
        for generator in MODULE.ROUND5.EXACT_GENERATORS:
            self.assertEqual(MODULE.ROUND5.matrix_determinant(generator), MODULE.ROUND5.ONE)
        relator = (1, -2, 3, -4, -1, 2, -3, 4)
        self.assertEqual(
            MODULE.ROUND5.word_matrix(relator), MODULE.ROUND5.matrix_identity()
        )

    def test_03_certificate_resolves_exactly_the_frozen_eight_ids(self) -> None:
        census_rows = self.source_package["census_rows"]
        historical = {
            row["census_id"]
            for row in census_rows
            if row["owner_credit_status"]
            == "WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED"
        }
        resolved = {
            row["historically_withheld_census_id"] for row in self.public_rows
        }
        self.assertEqual(len(historical), 8)
        self.assertEqual(resolved, historical)

    def test_04_frozen_source_target_conjugator_triples_are_exact(self) -> None:
        actual = tuple(
            (
                row["source_census_id"],
                row["historically_withheld_census_id"],
                row["conjugator_word"],
            )
            for row in self.public_rows
        )
        self.assertEqual(actual, MODULE.CONJUGACY_SPECS)

    def test_05_conjugators_are_short_freely_reduced_gamma_words(self) -> None:
        for row in self.public_rows:
            word = MODULE.ROUND5.parse_word_text(row["conjugator_word"])
            self.assertTrue(MODULE.ROUND5.is_freely_reduced(word))
            self.assertEqual(len(word), row["conjugator_marked_length"])
            self.assertLessEqual(len(word), 3)
            self.assertTrue(all(abs(letter) in {1, 2, 3, 4} for letter in word))

    def test_06_all_eight_direct_sl2_conjugacy_equalities_recompute(self) -> None:
        census_index = {
            row["census_id"]: row for row in self.source_package["census_rows"]
        }
        for row in self.public_rows:
            source = census_index[row["source_census_id"]]
            duplicate = census_index[row["historically_withheld_census_id"]]
            source_matrix = MODULE.ROUND5.word_matrix(
                MODULE.ROUND5.parse_word_text(source["canonical_marked_word"])
            )
            duplicate_matrix = MODULE.ROUND5.word_matrix(
                MODULE.ROUND5.parse_word_text(duplicate["canonical_marked_word"])
            )
            conjugator_matrix = MODULE.ROUND5.word_matrix(
                MODULE.ROUND5.parse_word_text(row["conjugator_word"])
            )
            self.assertEqual(
                MODULE.matrix_conjugate(source_matrix, conjugator_matrix),
                duplicate_matrix,
            )
            self.assertEqual(row["exact_sl2_direct_equality"], "true")
            self.assertEqual(row["projective_sign"], "+")

    def test_07_no_inverse_or_orientation_fallback_is_used(self) -> None:
        for internal, public in zip(self.internal_rows, self.public_rows):
            self.assertFalse(internal["_inverse_equal_internal"])
            self.assertEqual(public["inverse_fallback_used"], "false")
            self.assertEqual(public["conjugacy_convention"], "x^-1*g*x=h")

    def test_08_each_peer_pair_is_literal_element_distinct_before_conjugacy(self) -> None:
        self.assertEqual(
            {
                row["source_target_literal_projective_distinct"]
                for row in self.public_rows
            },
            {"true"},
        )
        self.assertEqual(
            self.validation["literal_source_target_distinct_count"], 8
        )

    def test_09_each_pair_shares_frozen_primitivity_homology_trace_and_length(self) -> None:
        for row in self.internal_rows:
            source = row["_source_row_internal"]
            duplicate = row["_duplicate_row_internal"]
            self.assertEqual(
                source["gamma_primitivity_status"],
                "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE",
            )
            self.assertEqual(
                duplicate["gamma_primitivity_status"],
                "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE",
            )
            for field in (
                "inverse_paired_homology_axis_key",
                "exact_trace",
                "exact_trace_squared",
                "geodesic_length_decimal",
            ):
                self.assertEqual(source[field], duplicate[field])

    def test_10_every_resolution_is_duplicate_only_and_mints_zero_owners(self) -> None:
        for row in self.public_rows:
            self.assertEqual(
                row["round6_owner_resolution"],
                "CERTIFIED_CONJUGATE_DUPLICATE_NO_NEW_OWNER",
            )
            self.assertEqual(row["owner_count_delta"], 0)
            self.assertTrue(row["primitive_axis_owner_id"])
        self.assertEqual(self.validation["new_owner_credit_count"], 0)
        self.assertEqual(self.validation["unresolved_count_within_frozen_eight"], 0)

    def test_11_owner_and_branch_ledgers_are_unchanged(self) -> None:
        self.assertEqual(self.validation["primitive_axis_owner_count_per_field"], 36)
        self.assertEqual(self.validation["field_axis_owner_pair_count"], 72)
        self.assertEqual(self.validation["branch_row_count"], 576)
        self.assertTrue(self.validation["round5_branch_ledger_reused_byte_for_byte"])
        self.assertEqual(
            self.validation["round5_branch_ledger_sha256"],
            MODULE.EXPECTED_SOURCE_SHA256["round5_branch_ledger"],
        )

    def test_12_the_44_proved_records_resolve_to_36_owners_plus_8_duplicates(self) -> None:
        self.assertEqual(self.validation["gamma_primitivity_proved_record_count"], 44)
        self.assertEqual(
            self.validation["primitive_axis_owner_count_per_field"]
            + self.validation["certified_conjugate_duplicate_count"],
            44,
        )

    def test_13_open_primitivity_and_marked_power_populations_do_not_move(self) -> None:
        self.assertEqual(self.validation["gamma_primitivity_open_count"], 322)
        self.assertEqual(self.validation["marked_power_count"], 24)
        self.assertEqual(
            self.validation["full_gamma_conjugacy_completeness"],
            "NOT_ESTABLISHED_OUTSIDE_FROZEN_EIGHT",
        )

    def test_14_nonarithmetic_control_source_gate_fails_closed(self) -> None:
        self.assertEqual(self.control_gate["status"], "FAIL_CLOSED_NOT_READY")
        self.assertEqual(self.control_gate["requirements_satisfied"], 0)
        self.assertEqual(self.control_gate["requirements_total"], 6)
        for field in MODULE.CONTROL_GATE_EXECUTION_FIELDS:
            self.assertIs(self.control_gate[field], False, field)

    def test_15_each_control_execution_flag_is_individually_fail_closed(self) -> None:
        for field in MODULE.CONTROL_GATE_EXECUTION_FIELDS:
            mutated = copy.deepcopy(self.control_gate)
            mutated[field] = True
            validation = MODULE.validate(
                self.source_package, self.internal_rows, mutated
            )
            self.assertEqual(validation["status"], "FAIL", field)
            self.assertTrue(
                any(field in error for error in validation["errors"]), field
            )

    def test_16_target_data_arithmetic_and_route_firewalls_remain_closed(self) -> None:
        self.assertEqual(self.validation["target_data_rows"], 0)
        self.assertEqual(self.validation["arithmetic_label_rows"], 0)
        self.assertEqual(self.validation["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.validation["a2_evaluation"], "NOT_RUN")
        self.assertEqual(self.validation["a4_credit"], "NONE")
        self.assertEqual(self.validation["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(self.validation["route_b_invocation_allowed"])
        for row in self.public_rows:
            self.assertEqual(row["target_data_used"], "false")
            self.assertEqual(row["arithmetic_label"], "NONE")
            self.assertEqual(row["formal_route_a_tuple"], "UNASSIGNED")
            self.assertEqual(row["route_b_invocation_allowed"], "false")

    def test_17_validation_passes_without_errors(self) -> None:
        self.assertEqual(self.validation["status"], "PASS")
        self.assertEqual(self.validation["errors"], [])
        self.assertEqual(self.validation["exact_direct_sl2_conjugacy_count"], 8)
        self.assertEqual(self.validation["inverse_fallback_count"], 0)


if __name__ == "__main__":
    unittest.main()
