#!/usr/bin/env python3
"""Exact serialized-artifact regression tests for SD-C33."""

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
    """Use authority results by default; the isolated runner overrides RESULTS."""
    return RESULTS


def rows(name: str) -> list[dict[str, str]]:
    with (path() / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def payload(name: str):
    return json.loads((path() / name).read_text(encoding="utf-8"))


class WilsonArtifactTests(unittest.TestCase):
    def test_wilson_matches_independent_prime_audit(self) -> None:
        self.assertTrue(all(row["accepts"] == row["independent_prime_audit"] for row in rows("wilson_ledger.csv")))

    def test_all_composites_rejected(self) -> None:
        self.assertEqual(len(rows("composite_controls.csv")), 3531)
        self.assertTrue(all(row["wilson_accepts"] == "0" for row in rows("composite_controls.csv")))

    def test_all_base2_pseudoprime_controls_rejected(self) -> None:
        self.assertEqual(len(rows("fermat_pseudoprime_controls.csv")), 13)
        self.assertTrue(all(row["wilson_accepts"] == "0" for row in rows("fermat_pseudoprime_controls.csv")))

    def test_bare_ufd_not_additively_closed(self) -> None:
        self.assertEqual(len(rows("bare_ufd_addition_failure.csv")), 144)
        self.assertTrue(all(row["ordinary_sum_is_required_monic_monomial"] == "0" for row in rows("bare_ufd_addition_failure.csv")))

    def test_explicit_1_plus_1_breaks_bare_clone(self) -> None:
        record = next(row for row in rows("bare_ufd_addition_failure.csv") if row["left"] == row["right"] == "1")
        self.assertEqual(record["required_target"], "x_2")
        self.assertEqual(record["ordinary_polynomial_sum"], "(1)+(1)")

    def test_matched_semiring_clone_operations_copy(self) -> None:
        self.assertEqual(len(rows("matched_semiring_clone.csv")), 169)
        self.assertTrue(all(row["matches"] == "1" for row in rows("matched_semiring_clone.csv")))

    def test_matched_semiring_clone_wilson_copy(self) -> None:
        self.assertIs(payload("summary.json")["matched_clone_wilson_equal"], True)

    def test_source_lock_selects_baseline_and_matched_clone_only(self) -> None:
        selected = [row["name"] for row in payload("semiring_controls.json") if row["passes_source_lock"]]
        self.assertEqual(selected, ["full_shift_positive_integer_semiring", "matched_transported_semiring_clone"])

    def test_random_magma_tables_do_not_accidentally_pass(self) -> None:
        controls = payload("random_operation_controls.json")
        self.assertTrue(all(not row["passes_commutative_semiring_axioms"] for row in controls[:32]))

    def test_random_relabel_Zmod11_is_semiring(self) -> None:
        self.assertIs(payload("random_operation_controls.json")[-1]["passes_commutative_semiring_axioms"], True)

    def test_candidate_call_audit_passes(self) -> None:
        certificate = payload("source_oracle_certificate.json")
        self.assertIs(certificate["passes"], True)
        self.assertEqual(certificate["forbidden_seen"], [])
        # Regression for complete-tree audit idempotence: the production
        # normalizer must treat pre-audit and final inventories identically.
        self.assertEqual(
            inventory_without_self_generated(
                ["summary.json", "integrity_audit.json", "SHA256SUMS.txt"]
            ),
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
            final_audit = json.loads((DEFAULT_RESULTS / "integrity_audit.json").read_text(encoding="utf-8"))
            self.assertEqual(final_audit["status"], "PASS")
            self.assertIs(final_audit["all_pass"], True)

    def test_prime_cycle_length_is_p_minus_1(self) -> None:
        accepted = [row for row in rows("wilson_ledger.csv") if row["accepts"] == "1"]
        self.assertTrue(all(int(row["cycle_length_if_accepted"]) == int(row["n"]) - 1 for row in accepted))

    def test_dilution_lower_bound_exceeds_0_95_at_largest_prime_sigma2(self) -> None:
        record = next(row for row in rows("entropy_budget_dilution.csv") if row["p"] == "4093" and row["sigma"] == "2")
        self.assertGreater(float(record["max_edge_weight_lower_bound"]), 0.95)

    def test_formal_trace_contributions_are_finite(self) -> None:
        self.assertTrue(all(int(row["finite_contribution_count"]) <= int(row["power"]) + 1 for row in rows("formal_trace_ledger.csv")))

    def test_raw_and_induced_products_agree_at_z1(self) -> None:
        self.assertIs(payload("marker_change_certificate.json")[0]["equal"], True)

    def test_raw_and_induced_products_differ_at_z_one_third(self) -> None:
        self.assertIs(payload("marker_change_certificate.json")[1]["equal"], False)

    def test_universal_wrapper_has_five_supports(self) -> None:
        self.assertEqual(len(payload("universal_wrapper_controls.json")), 5)

    def test_all_transient_wrappers_prune(self) -> None:
        self.assertTrue(all(row["transient_prunes_to_diagonal"] for row in payload("universal_wrapper_controls.json")))
