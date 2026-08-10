#!/usr/bin/env python3
"""Regression and mutation tests for HCS-C28."""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


producer = load_module("c28_producer", HERE / "c28_producer.py")
checker = load_module("c28_independent_check", HERE / "c28_independent_check.py")


class C28Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = producer.run()

    def test_schema(self) -> None:
        self.assertEqual(self.report["schema"], "HCS-C28-PRIME-DIRECT-SUM-DETERMINANT-V1")

    def test_gamma_star_discriminant(self) -> None:
        row = self.report["gamma_star_raw_product_control"]
        self.assertEqual(row["det_I_minus_g"], 460097253)
        self.assertEqual(row["squarefree_kernel"], 5680213)
        self.assertEqual(row["negative_class_character"], -1)
        self.assertEqual(row["positive_class_character"], 1)

    def test_normalized_character_limit_scope(self) -> None:
        theorem = self.report["normalized_character_limit_theorem"]
        self.assertIn("regular character", theorem["interpretation"])
        self.assertEqual(theorem["AGY_positive_monoid"]["nonempty_identity_words"], 0)

    def test_sharp_trace_class_threshold(self) -> None:
        theorem = self.report["sharp_schatten_theorem"]
        self.assertEqual(theorem["prime_norm_weight"]["ordinary_trace_class_iff"], "Re(z)>3")
        rows = theorem["prime_norm_weight"]["phase_diagram_controls"]
        observed = {(row["Re_z"], row["Schatten_q"]): row["membership"] for row in rows}
        self.assertFalse(observed[(3, 1)])
        self.assertTrue(observed[(4, 1)])
        self.assertFalse(observed[(2, 1)])
        self.assertTrue(observed[(2, 2)])

    def test_p073_exact_all_prime_obstruction(self) -> None:
        row = self.report["c24_p073_fixed_plane_obstruction"]
        self.assertEqual(row["fixed_dimension_over_Q"], 2)
        self.assertEqual(row["two_by_two_minor_gcd"], 1)
        self.assertEqual(row["three_by_three_minors"], [0])
        self.assertEqual(row["thomas_quotient_determinant"], -4)
        self.assertEqual(row["all_odd_prime_theorem"]["exact_character"], "p")

    def test_c24_census(self) -> None:
        census = self.report["c24_fixed_space_census"]
        self.assertEqual(census["fixed_dimension_counts"], {"0": 125, "1": 20, "2": 1})
        self.assertEqual(census["unique_fixed_dimension_two_id"], "C24-P073")

    def test_mobius_formal_identity(self) -> None:
        series = self.report["quadratic_prime_series"]
        values = series["divisor_mobius_sums"]
        self.assertEqual(values["1"], 1)
        self.assertTrue(all(value == 0 for key, value in values.items() if key != "1"))
        self.assertIn("-chi(2)*2^(-q)", series["identity"])
        self.assertIn("Euler-product logarithm", series["euler_log_branch"])
        self.assertIn("may be imprimitive", series["power_character_scope"])

    def test_independent_replay(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            certificate = Path(temporary) / "certificate.json"
            certificate.write_text(json.dumps(self.report), encoding="utf-8")
            replay = checker.run(certificate)
        self.assertEqual(replay["status"], "PASS")
        self.assertTrue(replay["payload_hash_check"])
        self.assertTrue(all(replay["certificate_checks"].values()))

    def assert_checker_rejects(self, mutated: dict[str, object], *, refresh_payload_hash: bool) -> None:
        if refresh_payload_hash:
            mutated.pop("certificate_payload_sha256", None)
            mutated["certificate_payload_sha256"] = checker.canonical_sha256(mutated)
        with tempfile.TemporaryDirectory() as temporary:
            certificate = Path(temporary) / "certificate.json"
            certificate.write_text(json.dumps(mutated), encoding="utf-8")
            with self.assertRaises(AssertionError):
                checker.run(certificate)

    def test_mutation_stale_payload_hash_is_detected(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["candidate_name"] = "mutated"
        self.assert_checker_rejects(mutated, refresh_payload_hash=False)

    def test_mutation_wrong_threshold_is_detected(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["sharp_schatten_theorem"]["prime_norm_weight"]["ordinary_trace_class_iff"] = "Re(z)>2"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_wrong_p073_character_is_detected(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["c24_p073_fixed_plane_obstruction"]["all_odd_prime_theorem"][
            "exact_character"
        ] = "1"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_unmarked_p073_consequence_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["c24_p073_fixed_plane_obstruction"]["all_odd_prime_theorem"][
            "consequence"
        ] = "FULL_RAUZY_DIMENSION_NORMALIZED_ASSEMBLY_FAILS"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_fractional_power_germ_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["normalized_character_limit_theorem"]["AGY_positive_monoid"][
            "determinant_germ"
        ] = "D_p(s,u)^(1/p^2) -> 1 on one common sufficiently small u-disc"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_real_only_marked_threshold_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["marked_normalization_threshold"]["convergence_iff"] = "alpha>1+k_Q/2"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_full_prime_mobius_formula_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["quadratic_prime_series"]["identity"] = (
            "P_chi(q)=sum_(k>=1) mu(k)/k log L(k*q,chi^k), Re(q)>1"
        )
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_wrong_normalized_limit_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["decisions"]["normalized_trace_AGY_limit"] = "NONTRIVIAL_XI_DETERMINANT"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_wrong_fredholm_gate_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["prime_direct_sum_fredholm_theorem"]["repetition_firewall"] = (
            "Theta_p(g_w^r)=Theta_p(g_w)^r"
        )
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_wrong_unweighted_gate_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["decisions"]["raw_unweighted_prime_direct_sum"] = "PASS_TRACE_CLASS"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_scope_violation_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["scope_firewall"]["flags"]["xi_divisor_or_RH_claimed"] = True
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_mutation_source_lock_is_detected_after_rehash(self) -> None:
        mutated = copy.deepcopy(self.report)
        mutated["source_lock"]["chronology"] = "later edges multiply on the right"
        self.assert_checker_rejects(mutated, refresh_payload_hash=True)

    def test_scope_firewall(self) -> None:
        flags = self.report["scope_firewall"]["flags"]
        self.assertFalse(any(flags.values()))
        self.assertFalse(self.report["decisions"]["route_B_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
