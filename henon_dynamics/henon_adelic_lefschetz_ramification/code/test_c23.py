#!/usr/bin/env python3
"""Structural mutation tests for the HCS-C23 first gate."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
CERTIFICATE = PROJECT / "results" / "c23_first_gate_certificate.json"
CHECKER = HERE / "c23_independent_check.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c23_checker", CHECKER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class C23MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.checker = load_checker()
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def reject(self, mutated: dict[str, object], key: str) -> None:
        checks = self.checker.structural_audit(mutated)
        self.assertFalse(checks[key])
        self.assertFalse(all(checks.values()))

    def test_clean_structure(self) -> None:
        checks = self.checker.structural_audit(self.certificate)
        self.assertTrue(all(checks.values()), checks)

    def test_reject_averaged_chronology(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["clock_and_chronology"]["averaging_used"] = True
        self.reject(mutated, "chronology_frozen")

    def test_reject_reversal_quotient(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["clock_and_chronology"]["reversal"] = "quotiented"
        self.reject(mutated, "chronology_frozen")

    def test_reject_wrong_word_pair(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["chronology_pair_controls"][0]["words"][1] = "0001010"
        self.reject(mutated, "pair_controls")

    def test_reject_dihedral_pair_conflation(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["chronology_pair_controls"][0]["non_dihedral_pair"] = False
        self.reject(mutated, "pair_controls")

    def test_reject_deleted_packet_event(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["decisive_packet_norm_rows"][0]["evaluations"][0][
            "r1_multiplication_kernel_dimension"
        ] = 0
        self.reject(mutated, "decisive_rows")

    def test_reject_premature_zsigmondy_claim(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["decisions"]["strong_divisibility_zsigmondy_tower_pass"] = True
        mutated["decisions"]["euler_product_authorized"] = True
        self.reject(mutated, "decision_scope")

    def test_reject_deleted_cyclic_resultant_baseline(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["decisions"]["fixed_word_cyclic_resultant_baseline"] = False
        self.reject(mutated, "decision_scope")

    def test_reject_premature_large_ledger(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["decisions"]["next_gate"] = "RUN_UNFOCUSED_FULL_LEDGER"
        self.reject(mutated, "decision_scope")

    def test_reject_missing_cyclic_resultant_claim_boundary(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["claim_boundary"] = [
            text
            for text in mutated["claim_boundary"]
            if "cyclic-resultant sequence" not in text
        ]
        self.reject(mutated, "cyclic_resultant_novelty_boundary")

    def test_reject_norm_valuation_conflation(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        mutated["claim_boundary"] = [
            text
            for text in mutated["claim_boundary"]
            if "ell-adic valuation" not in text
        ]
        self.reject(mutated, "no_valuation_overclaim")


if __name__ == "__main__":
    unittest.main()
