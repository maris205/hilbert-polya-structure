#!/usr/bin/env python3
"""Regression and mutation tests for HCS-C22G."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
PRODUCER = HERE / "c22g_producer.py"
CHECKER = HERE / "c22g_independent_check.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c22g_checker", CHECKER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class C22GTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.checker = load_checker()
        cls.tmp = tempfile.TemporaryDirectory()
        cls.certificate_path = Path(cls.tmp.name) / "certificate.json"
        subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(cls.certificate_path)],
            check=True,
            cwd=PROJECT,
            capture_output=True,
            text=True,
        )
        cls.certificate = json.loads(cls.certificate_path.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def assert_rejected(self, mutated: dict[str, object], key: str) -> None:
        checks = self.checker.audit(mutated)
        self.assertFalse(checks[key])
        self.assertFalse(all(checks.values()))

    def test_clean_certificate(self) -> None:
        checks = self.checker.audit(self.certificate)
        self.assertTrue(all(checks.values()), checks)

    def test_reject_reverse_pinning_convention(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        convention = mutated["g1_lifted_pinning"]["bps_convention"]
        convention["fixed_mixed_data"] = "input unstable and output stable"
        convention["reverse_stable_output_inverse_used"] = True
        self.assert_rejected(mutated, "correct_bps_mixed_data")

    def test_reject_unshifted_supertrace(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        exterior = mutated["g2_g4_residue_and_supertrace"]["exterior"]
        exterior["supertrace_parity"] = "(-1)^k"
        exterior["fredholm_exponents"][0]["exponent"] = 1
        self.assert_rejected(mutated, "raw_sign_and_parity")

    def test_reject_reversed_chronology(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        chronology = mutated["g2_g4_residue_and_supertrace"]["chronology_control"]
        chronology["forward_trace"], chronology["reversed_trace"] = (
            chronology["reversed_trace"],
            chronology["forward_trace"],
        )
        self.assert_rejected(mutated, "chronology_mutation")

    def test_reject_deleted_edge(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        graph = mutated["g1_lifted_pinning"]["graph"]
        graph["edges"].pop()
        graph["state_edges"] = 5
        graph["branch_blocks"] = 10
        self.assert_rejected(mutated, "graph_exact")

    def test_reject_false_entire_scope(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        nuclear = mutated["g3_nuclearity"]
        nuclear["alternating_product_scope"] = "entire scalar determinant"
        self.assert_rejected(mutated, "nuclear_scope")

    def test_reject_false_nuclearity_pass(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        nuclear = mutated["g3_nuclearity"]
        nuclear["nuclear_order"] = 0
        nuclear["nuclearity_pass"] = True
        self.assert_rejected(mutated, "nuclear_scope")

    def test_reject_unproved_all_word_trace(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        raw = mutated["g2_g4_residue_and_supertrace"]["raw_residue"]
        raw["all_word_kernel_trace_proved"] = True
        self.assert_rejected(mutated, "raw_sign_and_parity")

    def test_reject_reversed_contour_orientation(self) -> None:
        mutated = copy.deepcopy(self.certificate)
        raw = mutated["g2_g4_residue_and_supertrace"]["raw_residue"]
        raw["product_contour_order"] = "du*dm*dx"
        raw["product_orientation"] = "du wedge dm wedge dx"
        self.assert_rejected(mutated, "raw_sign_and_parity")


if __name__ == "__main__":
    unittest.main()
