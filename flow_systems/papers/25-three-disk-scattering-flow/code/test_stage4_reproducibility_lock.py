#!/usr/bin/env python3
"""Direct fail-closed tests for the Paper-25 Stage-4 lock."""

from __future__ import annotations

import copy
import unittest

import stage4_reproducibility_lock as stage4


class Stage4ReproducibilityLockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lock = stage4.load_lock()

    def assert_rejected(self, modified: dict) -> None:
        with self.assertRaises(stage4.LockValidationError):
            stage4.validate_lock_payload(modified, check_environment=False)

    def test_01_canonical_closed_inventory_and_environment_pass(self) -> None:
        result = stage4.validate_lock_payload(self.lock, check_environment=True)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(
            result["inventory_files_checked"],
            self.lock["inventory_contract"]["expected_path_count"],
        )

    def test_02_round8_replay_is_byte_identical_and_validation_only(self) -> None:
        result = stage4.validate_lock_payload(
            self.lock, check_environment=True, replay_round8=True
        )
        replay = result["round8_replay"]
        self.assertEqual(replay["physical_replay_rows"], 2241)
        self.assertTrue(replay["byte_identical"])
        self.assertTrue(replay["canonical_match"])
        self.assertEqual(
            replay["evidentiary_role"],
            "SOLVER_AND_REPRODUCIBILITY_VALIDATION_ONLY",
        )

    def test_03_changed_artifact_hash_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["artifact_inventory"][0]["sha256"] = "0" * 64
        self.assert_rejected(modified)

    def test_04_missing_inventory_entry_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["artifact_inventory"].pop()
        self.assert_rejected(modified)

    def test_05_duplicate_inventory_entry_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["artifact_inventory"].append(
            copy.deepcopy(modified["artifact_inventory"][0])
        )
        self.assert_rejected(modified)

    def test_06_path_traversal_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["artifact_inventory"][0]["path"] = "../outside"
        self.assert_rejected(modified)

    def test_07_reproduction_command_drift_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["commands"][0]["command"] += " --refresh"
        self.assert_rejected(modified)

    def test_08_route_or_evidence_promotion_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["scientific_boundaries"]["physical_three_disk_route_tuple"] = [
            "A0_PASS"
        ]
        self.assert_rejected(modified)

    def test_09_environment_drift_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["environment"]["runtime"]["packages"]["numpy"] = "0.0.0"
        with self.assertRaises(stage4.LockValidationError):
            stage4.validate_lock_payload(modified, check_environment=True)

    def test_10_replay_fact_drift_fails_closed(self) -> None:
        modified = copy.deepcopy(self.lock)
        modified["round8_replay_contract"]["physical_replay_rows"] = 2242
        self.assert_rejected(modified)


if __name__ == "__main__":
    unittest.main()
