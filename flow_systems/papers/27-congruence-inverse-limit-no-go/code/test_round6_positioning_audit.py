#!/usr/bin/env python3
"""Independent standard-library tests for P27 Round 6."""

from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


MODULE_PATH = Path(__file__).with_name("round6_positioning_audit.py")
SPEC = importlib.util.spec_from_file_location("p27_round6", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round6_positioning_audit.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PositioningAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = [dict(row) for row in MODULE.CLAIM_ROWS]

    def test_frozen_claim_matrix_has_thirteen_unique_rows(self) -> None:
        self.assertEqual(len(self.rows), 13)
        self.assertEqual(len({row["claim_id"] for row in self.rows}), 13)
        self.assertEqual(MODULE.validate_rows(self.rows), [])

    def test_external_claims_have_primary_urls_locators_and_access_date(self) -> None:
        external = [
            row
            for row in self.rows
            if row["source_id"] in {"S1", "S2", "S3", "S4", "S5"}
        ]
        self.assertEqual(len(external), 9)
        self.assertTrue(all(row["primary_url"].startswith("https://") for row in external))
        self.assertTrue(all(row["exact_locator"] for row in external))
        self.assertTrue(
            all(
                any(
                    marker in row["exact_locator"]
                    for marker in ("p.", "pp.", "Definition", "Section")
                )
                for row in external
            )
        )
        self.assertEqual({row["access_date"] for row in external}, {"2026-08-28"})
        self.assertEqual(
            {row["verification_status"] for row in external},
            {"PRIMARY_SOURCE_WEB_VERIFIED"},
        )

    def test_malcev_exposition_has_page_exact_theorem_locator(self) -> None:
        s5 = next(row for row in self.rows if row["claim_id"] == "P27-S5-MALCEV")
        self.assertEqual(s5["support_class"], "PRIMARY_EXPOSITORY_SOURCE")
        self.assertIn("p.1, Introduction", s5["exact_locator"])
        self.assertIn("Theorem (Malcev 1940)", s5["exact_locator"])

    def test_human_read_status_is_pending_never_attested(self) -> None:
        external = [
            row
            for row in self.rows
            if row["source_id"] in {"S1", "S2", "S3", "S4", "S5"}
        ]
        self.assertEqual(
            {row["human_confirmation_status"] for row in external},
            {MODULE.HUMAN_PENDING},
        )
        self.assertFalse(
            any("USER_ATTESTED_READ" in value for row in self.rows for value in row.values())
        )

    def test_broad_aperiodicity_and_structural_mechanism_are_prior(self) -> None:
        by_id = {row["claim_id"]: row for row in self.rows}
        self.assertEqual(
            by_id["P27-S1-APERIODIC"]["novelty_consequence"],
            "BROAD_APERIODICITY_NOVELTY_REJECTED",
        )
        self.assertEqual(
            by_id["P27-S1-UNIVERSAL"]["novelty_consequence"],
            "SIMPLY_CONNECTED_LEAF_MECHANISM_IS_PRIOR",
        )
        self.assertEqual(
            by_id["P27-S2-PUNCTURED"]["novelty_consequence"],
            "NONCOMPACT_MODULAR_SOLENOID_STRUCTURE_IS_PRIOR",
        )

    def test_s4_compact_domain_caveat_is_explicit(self) -> None:
        s4 = next(row for row in self.rows if row["claim_id"] == "P27-S4-KERNEL")
        self.assertIn("closed compact base", s4["domain_caveat"])
        self.assertIn("not a substitute", s4["domain_caveat"])

    def test_local_compact_cusped_claims_keep_distinct_computation_boundaries(self) -> None:
        by_id = {row["claim_id"]: row for row in self.rows}
        self.assertIn(
            "whole-g closing times",
            by_id["P27-LOCAL-CUSPED"]["domain_caveat"],
        )
        self.assertIn(
            "Full residual-core quotient orders are not computed",
            by_id["P27-LOCAL-CLOSED"]["domain_caveat"],
        )
        self.assertEqual(by_id["P27-LOCAL-COMMON"]["evidence_token"], "PROVED")

    def test_three_way_decision_is_frozen(self) -> None:
        decision = next(
            row for row in self.rows if row["claim_id"] == "P27-DECISION-THREE-WAY"
        )
        self.assertEqual(
            decision["novelty_consequence"], "GO_SHORT_NOTE_NO_GENERAL_NOVELTY_NO_A2"
        )
        self.assertIn("short compact-versus-cusped", decision["claim_text"])

    def test_generated_summary_rejects_same_owner_route_a(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p27-round6-scope-") as directory:
            output = Path(directory)
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "--output-dir", str(output)],
                check=True,
                capture_output=True,
            )
            summary = json.loads(
                (output / "round6_positioning_summary.json").read_text(encoding="utf-8")
            )
        self.assertEqual(
            summary["three_way_go_no_go"],
            {
                "short_comparative_owner_audit": "GO",
                "standalone_new_aperiodicity_theorem": "NO_GO",
                "same_owner_route_a_a2": "NO_GO",
            },
        )
        boundary = summary["claim_boundary"]
        self.assertEqual(boundary["formal_a1_verdict"], "A1_FAIL")
        self.assertEqual(boundary["a2_a4"], "FAIL_NOT_TESTABLE")
        self.assertEqual(boundary["overall_route_a_status"], "ROUTE_A_REJECTED")
        self.assertFalse(boundary["route_b_invocation_allowed"])
        self.assertEqual(
            boundary["finite_level_to_inverse_limit_orbit_credit"], "FORBIDDEN"
        )

    def test_generated_csv_preserves_every_frozen_field(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p27-round6-csv-") as directory:
            output = Path(directory)
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "--output-dir", str(output)],
                check=True,
                capture_output=True,
            )
            with (output / "round6_claim_source_matrix.csv").open(
                newline="", encoding="utf-8"
            ) as handle:
                generated = list(csv.DictReader(handle))
        self.assertEqual(generated, self.rows)

    def test_two_generated_trees_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p27-round6-replay-") as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            prefix = [sys.executable, str(MODULE_PATH), "--output-dir"]
            subprocess.run(prefix + [str(first)], check=True, capture_output=True)
            subprocess.run(prefix + [str(second)], check=True, capture_output=True)
            names = sorted(path.name for path in first.iterdir())
            self.assertEqual(names, sorted(path.name for path in second.iterdir()))
            for name in names:
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())


if __name__ == "__main__":
    unittest.main(verbosity=2)
