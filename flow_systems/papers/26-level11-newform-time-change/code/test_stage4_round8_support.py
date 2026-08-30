#!/usr/bin/env python3
"""Regression tests for the bounded Paper-26 Stage-4 support layer."""

from __future__ import annotations

import copy
import csv
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


MODULE_PATH = Path(__file__).with_name("stage4_round8_support.py")
SPEC = importlib.util.spec_from_file_location("p26_stage4_support_tests", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError("could not load stage4_round8_support.py")
SUPPORT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SUPPORT
SPEC.loader.exec_module(SUPPORT)

MANIFEST_PATH = SUPPORT.PROJECT_DIR / SUPPORT.MANIFEST_RELATIVE_PATH


class Stage4Round8SupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest, cls.manifest_raw = SUPPORT.load_manifest(MANIFEST_PATH)
        cls.rows, cls.summary = SUPPORT.build_decomposition()

    def test_transitive_round8_project_source_closure_is_exact(self) -> None:
        edges, closure = SUPPORT.discover_round8_graph()
        self.assertEqual(
            closure,
            (
                "code/round2_experiment.py",
                "code/round4_hecke_correspondence.py",
                "code/round7_exact_survivors.py",
                "code/round8_exact_taxonomy.py",
            ),
        )
        self.assertEqual(
            {(row["from"], row["to"]) for row in edges},
            {
                ("code/round4_hecke_correspondence.py", "code/round2_experiment.py"),
                ("code/round7_exact_survivors.py", "code/round2_experiment.py"),
                (
                    "code/round7_exact_survivors.py",
                    "code/round4_hecke_correspondence.py",
                ),
                ("code/round8_exact_taxonomy.py", "code/round7_exact_survivors.py"),
            },
        )

    def test_dependency_hash_drift_fails_closed(self) -> None:
        altered = copy.deepcopy(self.manifest)
        altered["locked_inputs"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(SUPPORT.SupportError, "binding drift"):
            SUPPORT.verify_manifest_data(altered)

    def test_omitted_transitive_source_fails_closed(self) -> None:
        altered = copy.deepcopy(self.manifest)
        altered["round8_rebuild_project_source_closure"] = altered[
            "round8_rebuild_project_source_closure"
        ][1:]
        with self.assertRaisesRegex(SUPPORT.SupportError, "closure is incomplete"):
            SUPPORT.verify_manifest_data(altered)

    def test_target_blind_control_selection_is_deterministic(self) -> None:
        selection = self.summary["selection"]
        self.assertEqual(selection["studied_functional"], "2*y+1*z")
        self.assertEqual(selection["matched_controls"], ["1*y-1*z", "1*y-2*z"])
        self.assertIn("source coordinates only", selection["selection_inputs"])
        for denominators in selection["source_denominators"].values():
            self.assertEqual(len(denominators), 11)
            self.assertNotIn("0", denominators.values())

    def test_frozen_population_and_route_boundary_are_unchanged(self) -> None:
        self.assertEqual(
            self.summary["population"],
            {"instance_total": 138, "word_prime_groups": 55, "group_law_rows": 165},
        )
        boundary = self.summary["claim_boundary"]
        self.assertEqual(boundary["formal_route_a_tuple"], SUPPORT.FORMAL_TUPLE)
        self.assertFalse(boundary["instance_multiset_changed"])
        self.assertFalse(boundary["group_multiset_changed"])
        self.assertFalse(boundary["canonical_round8_result_bytes_changed"])
        self.assertFalse(boundary["target_data_used"])
        self.assertFalse(boundary["formal_a2_evaluation_run"])
        self.assertFalse(boundary["dynamical_determinant_constructed"])
        self.assertFalse(boundary["route_b_invocation_allowed"])

    def test_registered_round8_scientific_values_are_preserved(self) -> None:
        per_law = self.summary["per_law"]
        self.assertEqual(per_law["a_p"]["studied_k_failures"], 51)
        self.assertEqual(per_law["a_p_squared"]["studied_k_failures"], 51)
        self.assertEqual(per_law["a_p_squared_minus_p"]["studied_k_failures"], 55)
        mechanisms = per_law["a_p_squared"]["failure_mechanism_counts"][
            "studied_k"
        ]
        self.assertEqual(
            mechanisms,
            {"DEGREE_ONE_AND_NONUNIT": 47, "NONUNIT_ONLY": 4, "PASS": 4},
        )

    def test_matched_control_decomposition_has_no_supported_residue(self) -> None:
        expected = {
            "a_p": {
                "both_matched_controls_fail": 51,
                "exactly_one_matched_control_fails": 0,
                "both_matched_controls_pass_possible_residue": 0,
                "degree_one_absent_with_nonzero_scalar": 17,
                "negative_scalar": 33,
            },
            "a_p_squared": {
                "both_matched_controls_fail": 44,
                "exactly_one_matched_control_fails": 7,
                "both_matched_controls_pass_possible_residue": 0,
                "degree_one_absent_with_nonzero_scalar": 17,
                "negative_scalar": 0,
            },
            "a_p_squared_minus_p": {
                "both_matched_controls_fail": 55,
                "exactly_one_matched_control_fails": 0,
                "both_matched_controls_pass_possible_residue": 0,
                "degree_one_absent_with_nonzero_scalar": 17,
                "negative_scalar": 33,
            },
        }
        for law, counts in expected.items():
            self.assertEqual(
                self.summary["per_law"][law]["studied_failure_overlap"], counts
            )
        self.assertFalse(
            self.summary["finding"][
                "newform_specific_residue_supported_in_two_control_panel"
            ]
        )
        self.assertFalse(
            any(
                row["newform_specific_residue_supported_in_two_control_panel"]
                == "true"
                for row in self.rows
            )
        )

    def test_support_result_serialization_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_path = Path(first)
            second_path = Path(second)
            SUPPORT.write_results(first_path)
            SUPPORT.write_results(second_path)
            self.assertEqual(
                SUPPORT.result_tree_hash(first_path), SUPPORT.result_tree_hash(second_path)
            )
            for name in (SUPPORT.RESULT_LEDGER_NAME, SUPPORT.RESULT_SUMMARY_NAME):
                self.assertEqual(
                    (first_path / name).read_bytes(), (second_path / name).read_bytes()
                )
            with (first_path / SUPPORT.RESULT_LEDGER_NAME).open(
                newline="", encoding="utf-8"
            ) as handle:
                self.assertEqual(len(list(csv.DictReader(handle))), 165)

    def test_manifest_binds_all_canonical_round8_bytes(self) -> None:
        bound = {row["path"]: row["sha256"] for row in self.manifest["canonical_round8_results"]}
        self.assertEqual(set(bound), set(SUPPORT.CANONICAL_RESULT_PATHS))
        for relative_path, expected_hash in bound.items():
            self.assertEqual(
                SUPPORT.sha256_file(SUPPORT.PROJECT_DIR / relative_path), expected_hash
            )
        receipt = self.manifest["legacy_round8_receipts"][0]
        self.assertEqual(
            SUPPORT.sha256_file(SUPPORT.PROJECT_DIR / receipt["path"]),
            receipt["sha256"],
        )

    def test_summary_json_round_trip_is_schema_stable(self) -> None:
        encoded = json.dumps(self.summary, sort_keys=True)
        decoded = json.loads(encoded)
        self.assertEqual(decoded["schema"], SUPPORT.SCHEMA_SUMMARY)
        self.assertEqual(decoded["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
