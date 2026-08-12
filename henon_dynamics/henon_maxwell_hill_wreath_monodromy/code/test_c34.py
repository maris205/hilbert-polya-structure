#!/usr/bin/env python3
"""Regression and adversarial mutation tests for HCS-C34."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
sys.path.insert(0, str(CODE))
import c34_checker as checker  # noqa: E402


CERTIFICATE = Path(
    os.environ.get("C34_TEST_CERTIFICATE", PROJECT / "results/c34_certificate.json")
)


def load_certificate() -> dict:
    return json.loads(CERTIFICATE.read_text(encoding="utf-8"))


def rehash(certificate: dict) -> None:
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_bytes(certificate["payload"])
    ).hexdigest()


def all_pass(certificate: dict) -> bool:
    gates = checker.audit_certificate(certificate)
    return bool(gates) and all(row["status"] == "PASS" for row in gates)


class C34Tests(unittest.TestCase):
    def test_01_released_certificate_passes(self) -> None:
        cert = load_certificate()
        self.assertTrue(all_pass(cert))
        self.assertEqual(cert["payload"]["relation_elimination_gate"]["kummer_rank"], 9)
        self.assertEqual(cert["payload"]["wreath_monodromy_gate"]["group_order"], 185794560)

    def test_02_producer_is_byte_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "one.json"
            second = Path(tmp) / "two.json"
            command = [sys.executable, str(CODE / "c34_producer.py"), "--output"]
            subprocess.run(command + [str(first)], check=True, capture_output=True, text=True)
            subprocess.run(command + [str(second)], check=True, capture_output=True, text=True)
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_03_c33_explicitly_left_wreath_gate_open(self) -> None:
        source = json.loads((checker.REPO / checker.C33_REL).read_text(encoding="utf-8"))
        self.assertTrue(source["payload"]["scope"]["no_full_wreath_claim"])

    def test_04_exact_theorem_fingerprints(self) -> None:
        payload = load_certificate()["payload"]
        self.assertEqual(
            payload["permutation_relation_module_gate"]["orbit_span_rank_census_over_all_512_vectors"],
            {"0": 1, "1": 1, "8": 255, "9": 255},
        )
        self.assertEqual(
            payload["rational_squareclass_gate"]["norm_over_discriminant_squarefree_class"], 3
        )
        self.assertEqual(
            payload["local_newton_gate"]["local_valuations_normalized_on_K"][
                "v_P(beta/Norm_K_QQ_beta)"
            ],
            -5,
        )

    def test_05_mutations_are_rejected(self) -> None:
        mutations = []

        def add(label, fn, refresh=True):
            mutations.append((label, fn, refresh))

        add("stale payload hash", lambda c: c["payload"].__setitem__("scope", {}), False)
        add("unknown top key", lambda c: c.__setitem__("extra", 1), False)
        add("unknown payload key", lambda c: c["payload"].__setitem__("extra", 1))
        add(
            "bool integer confusion",
            lambda c: c["payload"]["material_passport"].__setitem__("ai_assistance_disclosed", 1),
        )
        add(
            "source digest",
            lambda c: c["payload"]["source_lock"].__setitem__(str(checker.C33_REL), "0" * 64),
        )
        add(
            "P9 coefficient",
            lambda c: c["payload"]["inherited_object"]["P9_coefficients_high_to_low"].__setitem__(0, 1),
        )
        add(
            "F18 coefficient",
            lambda c: c["payload"]["degree_eighteen_polynomial_gate"]["coefficients_high_to_low"].__setitem__(2, 1),
        )
        add(
            "modular prime float",
            lambda c: c["payload"]["degree_eighteen_polynomial_gate"]["modular_irreducibility"].__setitem__("prime", 7.0),
        )
        add(
            "Rabin result",
            lambda c: c["payload"]["degree_eighteen_polynomial_gate"]["modular_irreducibility"].__setitem__("frobenius_final_remainder_zero", False),
        )
        add(
            "discriminant factor",
            lambda c: c["payload"]["rational_squareclass_gate"]["P9_discriminant_factorization"].__setitem__("19", 4),
        )
        add(
            "norm squareclass",
            lambda c: c["payload"]["rational_squareclass_gate"].__setitem__("norm_squarefree_class", 1),
        )
        add(
            "Newton shift",
            lambda c: c["payload"]["local_newton_gate"].__setitem__("shift_integer", 1803),
        )
        add(
            "Newton valuation vector",
            lambda c: c["payload"]["local_newton_gate"]["P9_shifted_coefficient_valuations_low_to_high"].__setitem__(0, 4),
        )
        add(
            "Newton slope",
            lambda c: c["payload"]["local_newton_gate"]["newton_cluster_segment"].__setitem__("slope", "-2"),
        )
        add(
            "residue factor coefficient",
            lambda c: c["payload"]["local_newton_gate"]["residue_factorization_ledger"]["P9_mod_19"]["factors"][0]["monic_coefficients_high_to_low"].__setitem__(1, 4),
        )
        add(
            "local splitting ramification index",
            lambda c: c["payload"]["local_newton_gate"]["local_splitting_field_gate"].__setitem__("local_splitting_field_ramification_index", 1),
        )
        add(
            "odd local valuation",
            lambda c: c["payload"]["local_newton_gate"]["local_valuations_normalized_on_K"].__setitem__("v_P(beta/Norm_K_QQ_beta)", -4),
        )
        add(
            "module census",
            lambda c: c["payload"]["permutation_relation_module_gate"]["orbit_span_rank_census_over_all_512_vectors"].__setitem__("8", 254),
        )
        add(
            "module list",
            lambda c: c["payload"]["permutation_relation_module_gate"]["invariant_submodules"].append("fake"),
        )
        add(
            "relation module",
            lambda c: c["payload"]["relation_elimination_gate"].__setitem__("relation_module", "W"),
        )
        add(
            "Kummer rank",
            lambda c: c["payload"]["relation_elimination_gate"].__setitem__("kummer_rank", 8),
        )
        add(
            "group order",
            lambda c: c["payload"]["wreath_monodromy_gate"].__setitem__("group_order", 9),
        )
        add(
            "group name",
            lambda c: c["payload"]["wreath_monodromy_gate"].__setitem__("galois_group", "S9"),
        )
        add(
            "Route A upgrade",
            lambda c: c["payload"]["route_a_evaluation"]["tuple"].__setitem__(1, "A2_ANALYTIC_DETERMINANT"),
        )
        add(
            "Route B",
            lambda c: c["payload"]["route_a_evaluation"].__setitem__("route_b_invocation_allowed", True),
        )
        add(
            "individual branch overclaim",
            lambda c: c["payload"]["scope"].__setitem__("not_eighteen_individual_branch_Hill_classes", False),
        )
        add(
            "standard theorem novelty overclaim",
            lambda c: c["payload"]["decisions"].__setitem__("standard_kummer_or_wreath_embedding_is_novel", True),
        )

        baseline = load_certificate()
        for label, mutation, refresh in mutations:
            with self.subTest(label=label):
                candidate = copy.deepcopy(baseline)
                mutation(candidate)
                if refresh:
                    rehash(candidate)
                self.assertFalse(all_pass(candidate))

    def test_06_checker_cli_distinguishes_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cert = load_certificate()
            cert["payload"]["wreath_monodromy_gate"]["group_order"] = 1
            rehash(cert)
            mutated = Path(tmp) / "bad.json"
            report = Path(tmp) / "report.json"
            mutated.write_text(json.dumps(cert), encoding="utf-8")
            process = subprocess.run(
                [sys.executable, str(CODE / "c34_checker.py"), "--certificate", str(mutated), "--output", str(report)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(process.returncode, 0)
            statuses = {row["status"] for row in json.loads(report.read_text())["gates"]}
            self.assertIn("FAIL", statuses)
            self.assertNotIn("ERROR", statuses)


if __name__ == "__main__":
    unittest.main()
