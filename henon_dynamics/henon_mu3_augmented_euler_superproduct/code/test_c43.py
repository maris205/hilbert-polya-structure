#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import c43_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c43_certificate.json"


def rehash(cert: dict) -> dict:
    cert = copy.deepcopy(cert)
    cert["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(cert["payload"])
    ).hexdigest()
    return cert


class C43Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def assert_rejected(self, mutation) -> None:
        cert = rehash(self.cert)
        mutation(cert)
        cert = rehash(cert)
        gates, passed = checker.audit_certificate(cert, PROJECT)
        self.assertFalse(passed)
        self.assertTrue(any(row["status"] == "FAIL" for row in gates))
        self.assertTrue(
            any(
                row["status"] == "FAIL"
                and row["gate"] != "G11_FULL_PAYLOAD"
                for row in gates
            ),
            "mutation was rejected only by the full-payload fallback gate",
        )
        self.assertFalse(any(row["status"] == "ERROR" for row in gates))

    def test_01_base_certificate_passes(self):
        gates, passed = checker.audit_certificate(self.cert, PROJECT)
        self.assertTrue(passed)
        self.assertEqual(len(gates), 12)

    def test_02_replay_is_deterministic(self):
        self.assertEqual(self.cert["payload"], checker.expected_payload(PROJECT))

    def test_03_bad_payload_digest_rejected(self):
        cert = copy.deepcopy(self.cert)
        cert["payload_sha256"] = "0" * 64
        _, passed = checker.audit_certificate(cert, PROJECT)
        self.assertFalse(passed)

    def test_04_extra_scope_key_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].update({"rh": True}))

    def test_05_bool_integer_confusion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][0].update({"prime": True}))

    def test_06_float_integer_confusion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][0].update({"prime": 7.0}))

    def test_07_prime_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][0].update({"prime": 13}))

    def test_08_auxiliary_prime_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][0].update({"auxiliary_prime": 49}))

    def test_09_charpoly_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_modular_controls"][1]["sector_charpoly_coefficients_low_to_high"][0][0] += 1
        self.assert_rejected(mutate)

    def test_10_fake_gcd_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][2].update({"gcd_sector_0_sector_1_degree": 1}))

    def test_11_sector_equality_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][3].update({"sector_1_equals_sector_2": False}))

    def test_12_dimension_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][4].update({"sector_dimensions": [12, 12, 12]}))

    def test_13_histogram_mutation_rejected(self):
        def mutate(c):
            c["payload"]["p7_conjugation_obstruction"]["residue_histogram_0_through_6"][2] -= 1
        self.assert_rejected(mutate)

    def test_14_conjugation_verdict_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["p7_conjugation_obstruction"].update({"A_7_1_is_real": True}))

    def test_15_route_a_upgrade_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["route_a"].update({"A3": "A3_EXACT_DIVISOR_CANDIDATE"}))

    def test_16_route_b_upgrade_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["route_a"].update({"route_b_invocation_allowed": True}))

    def test_17_global_continuation_upgrade_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].update({"global_meromorphic_continuation_claimed": True}))

    def test_18_source_hash_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["source_lock"][0].update({"sha256": "f" * 64}))

    def test_19_chronology_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["conventions"].update({"chronological_time": "T_p=U_p"}))

    def test_20_augmentation_weight_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["conventions"].update({"augmentation_weights": [1, 1, 1]}))

    def test_21_unknown_top_level_key_rejected(self):
        cert = rehash(self.cert)
        cert["unknown"] = 1
        gates, passed = checker.audit_certificate(cert, PROJECT)
        self.assertFalse(passed)

    def test_22_unexpected_checker_error_is_error_not_fail(self):
        original = checker.expected_payload
        try:
            def explode(_project):
                raise RuntimeError("synthetic checker crash")
            checker.expected_payload = explode
            gates, passed = checker.audit_certificate(self.cert, PROJECT)
        finally:
            checker.expected_payload = original
        self.assertFalse(passed)
        self.assertTrue(any(row["status"] == "ERROR" for row in gates))

    def test_23_determinant_sign_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_modular_controls"][0]["sector_determinants_mod_auxiliary"][0] = 2
        self.assert_rejected(mutate)

    def test_24_sector_eigenbasis_gate_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_modular_controls"][0]["exact_matrix_gates"]["R_basis_k_equals_omega_power_k_basis_k"] = False
        self.assert_rejected(mutate)

    def test_25_canonical_variable_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["conventions"].update({"local_variable": "z=p^(1/2-s) only"}))

    def test_26_paired_sector_polynomial_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_modular_controls"][0]["sector_charpoly_coefficients_low_to_high"][2][0] += 1
        self.assert_rejected(mutate)

    def test_27_gcd_coefficients_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][0].update({"gcd_sector_0_sector_1_coefficients_low_to_high": [2]}))

    def test_28_reduced_degree_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_modular_controls"][0].update({"reduced_augmentation_numerator_degree": 2}))

    def test_29_p7_difference_vector_mutation_rejected(self):
        def mutate(c):
            c["payload"]["p7_conjugation_obstruction"]["conjugation_difference_coefficients_0_through_6"][1] = 0
        self.assert_rejected(mutate)


if __name__ == "__main__":
    unittest.main()
