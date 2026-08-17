#!/usr/bin/env python3
"""Adversarial tests for both exact SD-C42 prototype implementations."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import prototype_independent as independent
import prototype_reference as p


HERE = Path(__file__).resolve().parent


class ExactPrototypeTests(unittest.TestCase):
    def test_frozen_matrix_order_and_witnesses(self) -> None:
        self.assertEqual(p.monodromy(((2, 4),)), (9, 2, 4, 1))
        self.assertEqual(p.monodromy(((1, 1), (1, 2))), (8, 3, 5, 2))
        self.assertEqual(p.trace(p.monodromy(((2, 4),))), 10)
        self.assertEqual(p.trace(p.monodromy(((1, 1), (1, 2)))), 10)

    def test_boundary_and_composite_witnesses(self) -> None:
        boundary = p.monodromy(((1, 1),))
        self.assertEqual((p.trace(boundary), p.determinant(boundary)), (3, 1))
        self.assertEqual(p.trace(boundary) ** 2 - 4, 5)
        composite = p.monodromy(((1, 2),))
        self.assertEqual(p.trace(composite), 4)

    def test_all_three_collision_classes_and_orientation(self) -> None:
        trace4 = p.collision_record(((1, 2),), ((2, 1),))
        trace6 = p.collision_record(((1, 4),), ((2, 2),))
        trace10 = p.collision_record(((2, 4),), ((1, 1), (1, 2)))
        self.assertTrue(trace4["exact"])
        self.assertTrue(trace4["digit_reversal_related"])
        self.assertTrue(trace6["exact"])
        self.assertFalse(trace6["digit_reversal_related"])
        self.assertTrue(trace10["exact"])
        self.assertFalse(trace10["digit_reversal_related"])
        self.assertTrue(trace10["cross_pair_length"])

    def test_splitting_and_nonpalindromic_raw_operator_order(self) -> None:
        splitting = p.splitting_record()
        self.assertEqual(splitting["pair_counts_1_to_3"], {"1": 4, "2": 6, "3": 20})
        self.assertTrue(splitting["trace4_two_rho_phases"])
        self.assertTrue(splitting["flattened_22_pair_primitive_sigma_imprimitive"])
        self.assertTrue(splitting["pass"])
        typing = p.return_map_record()
        self.assertTrue(typing["rho_iota_equals_iota_sigma_squared"])
        self.assertTrue(typing["wrong_sigma_squared_on_pair_space_rejected"])
        self.assertTrue(typing["global_reversal_descends_to_cyclic_pair_classes"])
        self.assertTrue(typing["global_raw_index_reversal_equals_pair_reverse"])
        self.assertTrue(typing["unreversed_block_order_mutation_rejected"])
        self.assertTrue(typing["pass"])
        branch = p.branch_order_record()
        self.assertEqual(branch["branch_value"], [442, 623])
        self.assertEqual(branch["weight_s1"], [16, 388129])
        self.assertEqual(branch["same_index_wrong_value"], [146, 697])
        self.assertEqual(branch["same_index_wrong_weight"], [16, 485809])
        self.assertTrue(branch["pass"])

    def test_pair_primitivity(self) -> None:
        self.assertTrue(p.is_primitive(((1, 1),)))
        self.assertTrue(p.is_primitive(((1, 1), (1, 2))))
        self.assertFalse(p.is_primitive(((1, 2), (1, 2))))

    def test_cayley_hamilton_trace_recurrence(self) -> None:
        matrix = p.monodromy(((1, 3), (2, 4)))
        tr = p.trace(matrix)
        q_prev, q_now = 2, tr
        for exponent in range(2, 7):
            q_next = tr * q_now - q_prev
            self.assertEqual(p.trace(p.matpow(matrix, exponent)), q_next)
            q_prev, q_now = q_now, q_next

    def test_small_registered_grid(self) -> None:
        audit = p.audit_alphabet((1, 2), "unit")
        self.assertEqual(audit["theorem_failures"], {})
        self.assertEqual(audit["order_discriminant_prime_nonboundary_count"], 0)
        self.assertGreater(audit["trace_composite_orbit_count"], 0)

    def test_odd_parity_is_outside_domain(self) -> None:
        matrix = p.digit_matrix(3)
        self.assertEqual(p.determinant(matrix), -1)
        self.assertEqual(p.trace(matrix) ** 2 + 4, 13)

    def test_independent_full_replay_of_canonical_result(self) -> None:
        replay = independent.replay(HERE / "PROTOTYPE_RESULT.json")
        self.assertFalse(replay["shared_reference_helpers"])
        self.assertEqual(replay["failure_count"], 0)
        self.assertTrue(replay["all_pass"])

    def test_independent_rejects_each_prototype_payload_tamper(self) -> None:
        canonical = json.loads((HERE / "PROTOTYPE_RESULT.json").read_text())
        mutations = (
            (("source_lock_hash_matches",), False),
            (("source_lock_sha256",), "0" * 64),
            (("control_lock", "all_inputs_bound"), False),
            (("chronology",), "prospective"),
            (("arithmetic",), "floating_point"),
            (("canonical_runs", 0, "theorem_failures"), {"forged": 1}),
            (("canonical_runs", 0, "scientific_rows_sha256"), "0" * 64),
            (
                (
                    "witnesses",
                    "trace6_nonreversal_collision",
                    "left",
                    "matrix",
                ),
                [0, 0, 0, 0],
            ),
            (("witnesses", "odd_parity_boundary", "determinant"), 1),
            (("primitivity_splitting", "pair_counts_1_to_3", "2"), 7),
            (("return_map_typing", "rho_iota_equals_iota_sigma_squared"), False),
            (("branch_operator_order", "weight_s1"), [1, 1]),
            (("aggregate", "hard_status"), "FAIL"),
            (("claim_boundary",), "unbounded universal no-go"),
        )

        def locate(packet: object, path: tuple[object, ...]) -> tuple[object, object]:
            cursor = packet
            for key in path[:-1]:
                cursor = cursor[key]
            return cursor, path[-1]

        with tempfile.TemporaryDirectory() as temporary:
            result_path = Path(temporary) / "PROTOTYPE_RESULT.json"
            for path, replacement in mutations:
                with self.subTest(path=path):
                    parent, key = locate(canonical, path)
                    original = parent[key]
                    parent[key] = replacement
                    try:
                        result_path.write_text(
                            json.dumps(canonical, indent=2, sort_keys=True) + "\n"
                        )
                        replay = independent.replay(result_path)
                        self.assertFalse(replay["all_pass"])
                        self.assertGreater(replay["failure_count"], 0)
                    finally:
                        parent[key] = original

    def test_relocated_prototype_outputs_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            relocated = Path(temporary) / "relocated-package"
            shutil.copytree(
                HERE,
                relocated,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
            reference_run = subprocess.run(
                [sys.executable, str(relocated / "prototype_reference.py")],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(
                reference_run.stdout, (HERE / "PROTOTYPE_RESULT.json").read_bytes()
            )
            (relocated / "PROTOTYPE_RESULT.json").write_bytes(reference_run.stdout)
            independent_run = subprocess.run(
                [
                    sys.executable,
                    str(relocated / "prototype_independent.py"),
                    str(relocated / "PROTOTYPE_RESULT.json"),
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(
                independent_run.stdout,
                (HERE / "INDEPENDENT_RESULT.json").read_bytes(),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
