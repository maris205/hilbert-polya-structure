#!/usr/bin/env python3
"""Adversarial tests for both SD-C42 corrective control implementations."""

from __future__ import annotations

from contextlib import redirect_stdout
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import control_independent as independent
import control_reference as reference


HERE = Path(__file__).resolve().parent


class CorrectiveControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = reference.pair_rows()

    def test_selection_rule_reads_all_six_cards_and_c02_survives(self) -> None:
        selection = reference.parse_selection_cards()
        self.assertTrue(selection["six_cards_valid"])
        self.assertEqual(selection["survivors"], ["SD-C01", "SD-C02", "SD-C04"])
        self.assertEqual(selection["winner"], "SD-C04")
        self.assertTrue(all(reference.selection_mutations().values()))

    def test_pair_orientation_and_sigma_squared_splitting(self) -> None:
        self.assertEqual(len(self.rows), 30)
        self.assertTrue(reference.orientation_metadata_valid(self.rows))
        broken = deepcopy(self.rows)
        broken[0].pop("reverse_orientation_id")
        self.assertFalse(reference.orientation_metadata_valid(broken))
        census = reference.splitting_census()
        self.assertEqual(census["pair_primitive_counts_1_to_3"], {1: 4, 2: 6, 3: 20})
        self.assertTrue(census["trace4_phase_relation_verified"])
        self.assertTrue(census["flattened_22_pair_primitive_sigma_imprimitive"])
        self.assertTrue(census["odd_even_swapped_mutation_rejected"])
        self.assertTrue(census["pass"])
        typing = reference.return_map_typing_certificate()
        self.assertTrue(typing["rho_iota_equals_iota_sigma_squared"])
        self.assertTrue(typing["wrong_sigma_squared_on_pair_space_rejected"])
        self.assertTrue(typing["global_reversal_descends_to_cyclic_pair_classes"])
        self.assertTrue(typing["global_raw_index_reversal_equals_pair_reverse"])
        self.assertTrue(typing["unreversed_block_order_mutation_rejected"])
        self.assertTrue(typing["pass"])

    def test_typed_eigenvalue_norm_and_derivative_algebra(self) -> None:
        row = next(item for item in self.rows if item["trace"] == 4)
        self.assertEqual(row["expanding_eigenvalue_minpoly"], [1, -4, 1])
        self.assertEqual(row["geodesic_norm_minpoly"], [1, -14, 1])
        self.assertEqual(row["derivative_multiplier_minpoly"], [1, -14, 1])
        self.assertEqual(row["norm_root_selector"], "greater_than_one")
        self.assertEqual(row["derivative_root_selector"], "between_zero_and_one")
        self.assertTrue(independent.exact_root_algebra_valid(self.rows))

        wrong_polynomial = deepcopy(self.rows)
        wrong_polynomial[0]["derivative_multiplier_minpoly"] = wrong_polynomial[0][
            "expanding_eigenvalue_minpoly"
        ]
        self.assertFalse(reference.orientation_metadata_valid(wrong_polynomial))
        wrong_root = deepcopy(self.rows)
        wrong_root[0]["derivative_root_selector"] = "greater_than_one"
        self.assertFalse(reference.orientation_metadata_valid(wrong_root))
        wrong_exact_value = deepcopy(self.rows)
        wrong_exact_value[0]["derivative_qsqrt_coefficients"] = wrong_exact_value[0][
            "norm_qsqrt_coefficients"
        ]
        self.assertFalse(reference.orientation_metadata_valid(wrong_exact_value))

    def test_branch_matrix_and_raw_operator_order(self) -> None:
        bridge = reference.build_branch_bridge()
        self.assertEqual(bridge["matrix_A"], [148, 31, 105, 22])
        self.assertEqual(bridge["matrix_B"], [22, 105, 31, 148])
        self.assertEqual(bridge["stored_branch_value"], [442, 623])
        self.assertEqual(bridge["stored_weight_s1"], [16, 388129])
        self.assertEqual(bridge["same_index_wrong_value"], [146, 697])
        self.assertEqual(bridge["same_index_wrong_weight"], [16, 485809])
        self.assertTrue(bridge["order_mutation_rejected"])
        self.assertTrue(bridge["weight_mutation_rejected"])
        self.assertTrue(bridge["pass"])

    def test_literal_a0_a1_controls_and_mutations(self) -> None:
        a0 = reference.build_a0_controls(self.rows)
        a1 = reference.build_a1_controls(self.rows)
        self.assertEqual(len(a0["predicates"]), 7)
        self.assertEqual(len(a1["predicates"]), 6)
        self.assertTrue(all(a0["predicates"].values()))
        self.assertTrue(all(a1["predicates"].values()))
        self.assertTrue(all(a0["negative_mutations"].values()))
        self.assertTrue(all(a1["negative_mutations"].values()))
        self.assertTrue(a0["pass"])
        self.assertTrue(a1["pass"])

    def test_projector_owner_and_scalar_inventory_are_computed(self) -> None:
        ownership = reference.build_ownership_controls()
        self.assertTrue(
            ownership["positive_reducing_owner"]["evaluation"]["declared_owner"]
        )
        self.assertTrue(ownership["full_ledger_owner"]["evaluation"]["declared_owner"])
        self.assertTrue(all(ownership["owner_mutations"].values()))
        selector = ownership["scalar_selector"]
        self.assertEqual(selector["record"]["full_inventory"], [3, 4])
        self.assertEqual(selector["record"]["filtered_inventory"], [3])
        self.assertEqual(selector["record"]["removed_inventory"], [4])
        self.assertIsNone(selector["record"]["declared_projector"])
        self.assertTrue(all(ownership["selector_inventory_mutations"].values()))
        self.assertTrue(ownership["pass"])

    def test_collision_records_bind_matrices_reversal_and_lengths(self) -> None:
        witnesses = reference.collision_witnesses()
        self.assertEqual(
            witnesses["trace4_reversal_one_pair"]["left_matrix"], [3, 1, 2, 1]
        )
        self.assertTrue(
            witnesses["trace4_reversal_one_pair"]["digit_reversal_related"]
        )
        self.assertFalse(
            witnesses["trace6_nonreversal_one_pair"]["digit_reversal_related"]
        )
        self.assertTrue(
            witnesses["trace10_nonreversal_cross_pair_length"]["cross_pair_length"]
        )
        self.assertTrue(all(witnesses["negative_mutations"].values()))
        self.assertTrue(witnesses["all_pass"])

    def test_projection_go_is_derived_and_norm_passes_clock_power(self) -> None:
        ownership = reference.build_ownership_controls()
        a0 = reference.build_a0_controls(self.rows)
        projection = reference.build_projection_go(
            reference.collision_witnesses(),
            self.rows,
            a0,
            ownership,
            reference.build_branch_bridge(),
        )
        norm = projection["criteria"]["geodesic_norm"]
        self.assertFalse(norm["integer_valued"])
        self.assertTrue(norm["clock"])
        self.assertTrue(norm["repetition"])
        self.assertFalse(projection["existential_go"])
        self.assertFalse(projection["rational_integer_clock_repetition_conjunction"])
        self.assertTrue(projection["synthetic_all_true_projection_yields_go"])
        self.assertTrue(all(projection["coverage_mutations"].values()))
        self.assertTrue(all(projection["truth_matrix_mutations"].values()))
        self.assertTrue(all(projection["certificate_mutations"].values()))
        self.assertTrue(projection["pass"])

    def test_all_declared_countermodels_are_executable(self) -> None:
        countermodels = reference.build_countermodels(
            reference.build_ownership_controls(), reference.collision_witnesses()
        )
        self.assertEqual(len(countermodels["predicates"]), 8)
        self.assertTrue(all(countermodels["predicates"].values()))
        self.assertTrue(all(countermodels["negative_mutations"].values()))
        self.assertEqual(countermodels["finite_cycle"]["determinant_polynomial"], [1, 0, 0, -1])
        self.assertTrue(countermodels["pass"])

    def test_aggregate_is_conjunction_and_terminal_is_narrow(self) -> None:
        result = reference.build_result()
        self.assertEqual(result["gate_failure_count"], 0)
        self.assertEqual(result["all_controls_sharp"], all(result["gates"].values()))
        self.assertNotIn("STOP_CLOCK_REPETITION_COMPATIBILITY", result["terminal_codes"])
        self.assertIn(
            "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
            result["terminal_codes"],
        )
        self.assertTrue(result["terminal_semantics"]["old_overbroad_code_rejected"])

    def test_main_exits_nonzero_if_source_hash_is_corrupted(self) -> None:
        original = reference.SOURCE_LOCK_SHA256
        try:
            reference.SOURCE_LOCK_SHA256 = "0" * 64
            with redirect_stdout(StringIO()):
                with self.assertRaises(SystemExit) as raised:
                    reference.main()
            self.assertEqual(raised.exception.code, 1)
        finally:
            reference.SOURCE_LOCK_SHA256 = original

    def test_independent_replay_of_canonical_result(self) -> None:
        result_path = HERE / "CONTROL_RESULT.json"
        self.assertTrue(result_path.is_file())
        replay = independent.replay(result_path)
        self.assertTrue(replay["no_reference_import"])
        self.assertEqual(replay["failure_count"], 0)
        self.assertTrue(replay["all_pass"])

    def test_independent_replay_rejects_payload_tampering(self) -> None:
        canonical = json.loads((HERE / "CONTROL_RESULT.json").read_text())

        def changed(path: tuple[str, ...], value: object) -> dict[str, object]:
            packet = deepcopy(canonical)
            cursor = packet
            for key in path[:-1]:
                cursor = cursor[key]
            cursor[path[-1]] = value
            return packet

        mutations = {
            "aggregate": changed(("all_controls_sharp",), False),
            "candidate": changed(("candidate_id",), "SD-CXX"),
            "chronology": changed(("chronology",), "prospective"),
            "route_b": changed(("route_b_invocation_allowed",), True),
            "gate_count": changed(("gate_count",), 999),
            "selection_path": changed(
                ("selection", "rows", 0, "path"), "ABSOLUTE_PATH_LEAK/SD-C01.yaml"
            ),
            "source_boundary_detail": changed(
                ("source_boundary", "mayer_required_tokens"), False
            ),
            "control_lock_detail": changed(
                ("control_lock", "all_file_hashes_bound"), False
            ),
            "mayer_hash_field": changed(("mayer_boundary_sha256",), "0" * 64),
            "base_hash": changed(
                ("bounded_base", "rows_sha256"), "0" * 64
            ),
            "a0_raw_inventory": changed(
                (
                    "a0_controls",
                    "controls",
                    "shuffled_primes",
                    "inventory",
                    0,
                ),
                4,
            ),
            "a1_raw_phase": changed(
                (
                    "a1_controls",
                    "controls",
                    "random_phases",
                    "assignments",
                    0,
                    1,
                ),
                0,
            ),
            "raw_branch_weight": changed(
                ("branch_matrix_operator_order_bridge", "raw_nested_weight_s1"),
                [1, 1],
            ),
            "splitting_count": changed(
                ("primitivity_splitting", "pair_primitive_counts_1_to_3", "2"),
                7,
            ),
            "return_map_type": changed(
                ("return_map_typing", "rho_iota_equals_iota_sigma_squared"),
                False,
            ),
            "collision_matrix": changed(
                (
                    "collision_witnesses",
                    "trace6_nonreversal_one_pair",
                    "left_matrix",
                ),
                [0, 0, 0, 0],
            ),
            "projection_certificate": changed(
                (
                    "projection_go_evaluation",
                    "derived_certificates",
                    "trace_integral",
                ),
                False,
            ),
            "projection_coverage": changed(
                ("projection_go_evaluation", "coverage_schema_valid"), False
            ),
            "projection_truth_mutation": changed(
                (
                    "projection_go_evaluation",
                    "truth_matrix_mutations",
                    "trace:clock:wrong_value_rejected",
                ),
                False,
            ),
            "projection_synthetic": changed(
                (
                    "projection_go_evaluation",
                    "synthetic_all_true_projection_yields_go",
                ),
                False,
            ),
            "owner_evaluation": changed(
                (
                    "ownership_controls",
                    "positive_reducing_owner",
                    "evaluation",
                    "declared_owner",
                ),
                False,
            ),
            "owner_interpretation": changed(
                ("ownership_controls", "scalar_selector", "interpretation"),
                "universal nonexistence",
            ),
            "countermodel_baseline": changed(
                ("scope_countermodels", "baseline_contract", "clock"),
                "log_trace",
            ),
            "terminal_detail": changed(
                (
                    "terminal_semantics",
                    "STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION",
                ),
                "all projections fail clock",
            ),
            "route_tuple": changed(
                ("route_status_recomputed", "A1"), "A1_FAIL"
            ),
        }
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "CONTROL_RESULT.json"
            for name, packet in mutations.items():
                with self.subTest(name=name):
                    path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
                    replay = independent.replay(path)
                    self.assertFalse(replay["all_pass"])
                    self.assertGreater(replay["failure_count"], 0)

    def test_relocated_package_produces_byte_identical_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            relocated = Path(temporary) / "relocated-package"
            shutil.copytree(
                HERE,
                relocated,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
            reference_run = subprocess.run(
                [sys.executable, str(relocated / "control_reference.py")],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(
                reference_run.stdout, (HERE / "CONTROL_RESULT.json").read_bytes()
            )
            (relocated / "CONTROL_RESULT.json").write_bytes(reference_run.stdout)
            independent_run = subprocess.run(
                [
                    sys.executable,
                    str(relocated / "control_independent.py"),
                    str(relocated / "CONTROL_RESULT.json"),
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(
                independent_run.stdout,
                (HERE / "CONTROL_INDEPENDENT_RESULT.json").read_bytes(),
            )

    def test_control_lock_rejects_an_extra_manifest_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            relocated = Path(temporary) / "extra-scope-package"
            shutil.copytree(
                HERE,
                relocated,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
            lock_path = relocated / "CONTROL_LOCK.md"
            lock_path.write_text(
                lock_path.read_text()
                + "\n"
                + "0" * 64
                + "  POST_RUN_REPORT_MUST_NOT_BE_PRELOCKED.md\n"
            )
            run = subprocess.run(
                [sys.executable, str(relocated / "control_reference.py")],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(run.returncode, 1)
            payload = json.loads(run.stdout)
            self.assertFalse(payload["control_lock"]["exact_file_set"])
            self.assertFalse(payload["control_lock"]["pass"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
