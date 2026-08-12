#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import c32_morse_gate_checker as checker
import c32_morse_gate_producer as producer
import c32_hash_manifest as manifest


class C32MorseGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = producer.build_certificate()

    def resign(self, certificate: dict) -> dict:
        certificate["payload_sha256"] = producer.sha256_bytes(
            producer.canonical_bytes(certificate["payload"])
        )
        return certificate

    def assert_semantic_reject(self, certificate: dict) -> None:
        report = checker.run_audit(certificate)
        self.assertFalse(report["all_pass"])
        self.assertGreater(report["failed"], 0)
        self.assertEqual(report["errors"], 0, report)

    def test_01_producer_is_deterministic(self) -> None:
        self.assertEqual(
            producer.canonical_bytes(self.base),
            producer.canonical_bytes(producer.build_certificate()),
        )

    def test_02_base_checker_passes_all_fourteen_gates(self) -> None:
        report = checker.run_audit(copy.deepcopy(self.base))
        self.assertTrue(report["all_pass"], report)
        self.assertEqual((report["passed"], report["failed"], report["errors"]), (14, 0, 0))

    def test_03_independent_scan_has_unique_registered_collision(self) -> None:
        rows, first = checker.independent_scan()
        self.assertEqual(len(rows), 80)
        self.assertEqual((first["n"], first["p"]), (5, 61))
        self.assertEqual(first["action"], 45)
        self.assertEqual(first["quadratic_character"], -1)
        self.assertEqual(first["determinants"], [7, 44])
        self.assertEqual(
            [(row["n"], row["p"]) for row in rows if row["collision_groups"]],
            [(5, 61)],
        )

    def test_04_small_clock_hessian_multiplicities(self) -> None:
        self.assertEqual(producer.hessian_from_action((3,), 61), [[38]])
        self.assertEqual(producer.hessian_from_action((3, 4), 61), [[36, 2], [2, 48]])
        self.assertEqual(checker.hessian((3,), 61), [[38]])
        self.assertEqual(checker.hessian((3, 4), 61), [[36, 2], [2, 48]])

    def test_05_explicit_witness_values(self) -> None:
        witness = self.base["payload"]["witness"]
        self.assertEqual(
            [orbit["q_word"] for orbit in witness["orbit_classes"]],
            [[12, 12, 40, 27, 40], [33, 58, 36, 36, 58]],
        )
        self.assertEqual(
            [orbit["hessian_det"] for orbit in witness["orbit_classes"]],
            [44, 7],
        )
        self.assertEqual(witness["determinant_square_ratio"]["least_square_root"], 25)
        self.assertEqual(witness["quadratic_congruence"]["matrix_det"], 22)

    def test_06_cli_bad_json_is_error_not_semantic_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text("{", encoding="utf-8")
            report = checker.audit_file(path)
        self.assertFalse(report["all_pass"])
        self.assertEqual(report["errors"], 1)
        self.assertEqual(report["failed"], 0)

    def test_07_reversed_chronology_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        word = tuple(mutated["payload"]["witness"]["orbit_classes"][0]["q_word"])
        p = 61
        product = [[1, 0], [0, 1]]
        for value in word:
            product = producer.matmul(product, producer.derivative_factor(value, p), p)
        mutated["payload"]["witness"]["orbit_classes"][0]["monodromy_matrix"] = product
        self.assert_semantic_reject(self.resign(mutated))

    def test_08_orbit_coordinate_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["orbit_classes"][0]["q_word"][2] = 41
        self.assert_semantic_reject(self.resign(mutated))

    def test_09_n2_multiplicity_contract_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["conventions"]["hessian"] = "generic cyclic tridiagonal shortcut"
        self.assert_semantic_reject(self.resign(mutated))

    def test_10_action_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["common_action"] = 46
        self.assert_semantic_reject(self.resign(mutated))

    def test_11_hessian_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["orbit_classes"][0]["hessian_det"] = 45
        self.assert_semantic_reject(self.resign(mutated))

    def test_12_hill_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["orbit_classes"][1]["hill_det"] = 8
        self.assert_semantic_reject(self.resign(mutated))

    def test_13_square_class_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["common_quadratic_character"] = 1
        self.assert_semantic_reject(self.resign(mutated))

    def test_14_singular_congruence_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["quadratic_congruence"]["matrix"][0] = [0] * 5
        mutated["payload"]["witness"]["quadratic_congruence"]["matrix_det"] = 0
        self.assert_semantic_reject(self.resign(mutated))

    def test_15_false_primitive_period_mutation_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["orbit_classes"][0]["primitive_state_period"] = 1
        self.assert_semantic_reject(self.resign(mutated))

    def test_16_global_no_go_promotion_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["decisions"]["global_artin_schreier_cohomology_no_go"] = True
        self.assert_semantic_reject(self.resign(mutated))

    def test_17_post_pilot_suppression_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["material_passport"]["post_pilot_disclosure"] = "preregistered prediction"
        self.assert_semantic_reject(self.resign(mutated))

    def test_18_bool_integer_type_confusion_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["p"] = True
        self.assert_semantic_reject(self.resign(mutated))

    def test_19_unknown_nested_key_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["quadratic_congruence"]["unchecked"] = True
        self.assert_semantic_reject(self.resign(mutated))

    def test_20_stale_payload_digest_rejected(self) -> None:
        mutated = copy.deepcopy(self.base)
        mutated["payload"]["witness"]["common_action"] = 46
        report = checker.run_audit(mutated)
        self.assertFalse(report["all_pass"])
        self.assertTrue(any(gate["gate"] == "G0" and gate["status"] == "FAIL" for gate in report["gates"]))

    def test_21_manifest_required_inventory_is_explicit(self) -> None:
        self.assertIn("THEOREM_PACKAGE.md", manifest.REQUIRED_RELATIVE_PATHS)
        self.assertIn("SOURCE_AUDIT.md", manifest.REQUIRED_RELATIVE_PATHS)
        self.assertIn(
            "results/c32_morse_gate_certificate.json",
            manifest.REQUIRED_RELATIVE_PATHS,
        )
        self.assertIn(
            "results/c32_morse_gate_independent_check.json",
            manifest.REQUIRED_RELATIVE_PATHS,
        )

    def test_22_manifest_rejects_missing_required_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            for relative in manifest.REQUIRED_RELATIVE_PATHS:
                path = project / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("fixture\n", encoding="utf-8")
            (project / "THEOREM_PACKAGE.md").unlink()
            with self.assertRaisesRegex(
                RuntimeError, "required release artifacts missing"
            ):
                manifest.tracked_files(project)


if __name__ == "__main__":
    unittest.main()
