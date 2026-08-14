#!/usr/bin/env python3
"""Thirteen frozen exact artifact tests for SD-C34."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

from audit_artifact_integrity import inventory_without_self_generated


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results"
RESULTS: Path = DEFAULT_RESULTS


def path() -> Path:
    return RESULTS


def rows(name: str) -> list[dict[str, str]]:
    with (path() / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def payload(name: str):
    return json.loads((path() / name).read_text(encoding="utf-8"))


class ProjectiveArtifactTests(unittest.TestCase):
    def test_static_defect_equivalence(self) -> None:
        self.assertEqual(len(rows("static_selector_firewall.csv")), 191)
        self.assertTrue(all(row["selector_equivalent_to_prime"] == "1" for row in rows("static_selector_firewall.csv")))
        self.assertTrue(all(row["selector_used_by_candidate"] == "0" for row in rows("static_selector_firewall.csv")))

    def test_all_prime_blocks_recurrent(self) -> None:
        prime_rows = [row for row in rows("modulus_census.csv") if row["evaluator_class"] == "prime"]
        self.assertEqual(len(prime_rows), 43)
        self.assertTrue(all(row["recurrent_support_nonzero"] == "1" for row in prime_rows))

    def test_all_composite_blocks_recurrent(self) -> None:
        composite_rows = [row for row in rows("modulus_census.csv") if row["evaluator_class"] != "prime"]
        self.assertEqual(len(composite_rows), 148)
        self.assertTrue(all(row["recurrent_support_nonzero"] == "1" for row in composite_rows))

    def test_all_actions_transitive(self) -> None:
        self.assertTrue(all(row["forward_component_size"] == row["state_count"] for row in rows("candidate_census.csv")))

    def test_all_states_overlap(self) -> None:
        self.assertTrue(all(row["overlap_state_count"] == row["state_count"] for row in rows("candidate_census.csv")))

    def test_matched_clone_exact(self) -> None:
        clone_rows = rows("matched_clone.csv")
        self.assertEqual(len(clone_rows), 191)
        self.assertTrue(all(row["semiring_transport_exact"] == row["graph_transport_exact"] == row["exact_equal"] == "1" for row in clone_rows))

    def test_random_compiler_controls(self) -> None:
        control_rows = rows("random_relation_controls.csv")
        self.assertEqual(len(control_rows), 48)
        self.assertTrue(all(row["s2_identity"] == row["r3_identity"] == row["universal_recurrence_nonzero"] == "1" for row in control_rows))

    def test_diamond_composite_flood(self) -> None:
        diamonds = payload("cross_modulus_diamonds.json")
        self.assertEqual(len(diamonds), 31)
        self.assertTrue(all(row["top_is_composite_evaluator"] == 1 for row in diamonds))

    def test_diamond_weight_identity(self) -> None:
        self.assertTrue(all(row["weight_base_product"] == row["expected_product"] for row in payload("cross_modulus_diamonds.json")))

    def test_source_oracle_certificate(self) -> None:
        certificate = payload("source_oracle_certificate.json")
        self.assertIs(certificate["pass"], True)
        self.assertEqual(certificate["forbidden_hits"], [])
        self.assertEqual(
            inventory_without_self_generated(["summary.json", "integrity_audit.json", "SHA256SUMS.txt"]),
            ["summary.json"],
        )
        if path().resolve() == DEFAULT_RESULTS.resolve():
            environment = dict(os.environ)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            completed = subprocess.run(
                [sys.executable, "-B", str(ROOT / "code" / "audit_artifact_integrity.py")],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            final_audit = payload("integrity_audit.json")
            self.assertEqual(final_audit["status"], "PASS")
            self.assertIs(final_audit["all_pass"], True)

    def test_no_empty_state_spaces(self) -> None:
        self.assertTrue(all(int(row["state_count"]) > 0 for row in rows("candidate_census.csv")))

    def test_s_cycle_partition(self) -> None:
        self.assertTrue(all(int(row["s_fixed_count"]) + 2 * int(row["s_two_cycle_count"]) == int(row["state_count"]) for row in rows("candidate_census.csv")))

    def test_r_cycle_partition(self) -> None:
        self.assertTrue(all(int(row["r_fixed_count"]) + 3 * int(row["r_three_cycle_count"]) == int(row["state_count"]) for row in rows("candidate_census.csv")))
