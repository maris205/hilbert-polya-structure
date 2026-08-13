#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

import c46_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c46_certificate.json"


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C46MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def assert_rejected(self, mutation) -> None:
        certificate = rehash(self.certificate)
        mutation(certificate)
        certificate = rehash(certificate)
        gates, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)
        self.assertFalse(any(row["status"] == "ERROR" for row in gates))
        self.assertTrue(
            any(
                row["status"] == "FAIL" and row["gate"] != "G12_FULL_PAYLOAD_REPLAY"
                for row in gates
            ),
            "mutation was rejected only by full-payload fallback",
        )

    def test_01_base_certificate_passes(self):
        gates, passed = checker.audit_certificate(self.certificate, PROJECT)
        self.assertTrue(passed)
        self.assertEqual(len(gates), 12)

    def test_02_independent_replay_matches(self):
        self.assertEqual(self.certificate["payload"], checker.expected_payload(PROJECT))

    def test_03_bad_digest_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload_sha256"] = "0" * 64
        _, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)

    def test_04_bool_prime_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["p7_conventions"].update({"prime": True})
        )

    def test_05_wrong_rho_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["p7_conventions"].update({"rho_order_3": 4})
        )

    def test_06_field_degree_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["p7_conventions"].update(
                {"real_field_degree_d7": 6}
            )
        )

    def test_07_sector_dimension_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["p7_conventions"].update(
                {"sector_dimensions": [3, 3, 1]}
            )
        )

    def test_08_D0_coefficient_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_sector_polynomials"][
                "D0_numerator_X0_through_X5_by_z_low_to_high"
            ][2][5] += 1

        self.assert_rejected(mutate)

    def test_09_D1_coefficient_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_sector_polynomials"][
                "D1_numerator_X0_through_X5_by_z_low_to_high"
            ][1][1] += 1

        self.assert_rejected(mutate)

    def test_10_sector_pairing_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_sector_polynomials"].update(
                {"D2_equals_D1": False}
            )
        )

    def test_11_theta_minpoly_mutation_rejected(self):
        def mutate(c):
            c["payload"]["resultant_and_norm_control"][
                "theta_minimal_polynomial_high_to_low"
            ][-1] = 1

        self.assert_rejected(mutate)

    def test_12_q0_theta_mutation_rejected(self):
        def mutate(c):
            c["payload"]["resultant_and_norm_control"][
                "q0_numerator_theta2_theta1_theta0_by_z_low_to_high"
            ][3][1] += 1

        self.assert_rejected(mutate)

    def test_13_q1_theta_mutation_rejected(self):
        def mutate(c):
            c["payload"]["resultant_and_norm_control"][
                "q1_numerator_theta2_theta1_theta0_by_z_low_to_high"
            ][2][0] += 1

        self.assert_rejected(mutate)

    def test_14_P18_mutation_rejected(self):
        def mutate(c):
            c["payload"]["resultant_and_norm_control"][
                "P18_coefficients_high_to_low"
            ][9] += 1

        self.assert_rejected(mutate)

    def test_15_P12_mutation_rejected(self):
        def mutate(c):
            c["payload"]["resultant_and_norm_control"][
                "P12_coefficients_high_to_low"
            ][6] += 1

        self.assert_rejected(mutate)

    def test_16_norm_constant_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["resultant_and_norm_control"].update(
                {"ordinary_norm_at_zero": 49}
            )
        )

    def test_17_norm_degree_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["resultant_and_norm_control"].update(
                {"ordinary_norm_numerator_degree": 18}
            )
        )

    def test_18_good_prime_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["good_reduction_control"].update(
                {"modulus": 7}
            )
        )

    def test_19_modular_degree_drop_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["good_reduction_control"].update(
                {"P18_degree_retained": 17}
            )
        )

    def test_20_cross_gcd_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["good_reduction_control"].update(
                {"gcd_P18_P12_coefficients_low_to_high": [1, 1]}
            )
        )

    def test_21_squarefree_gcd_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["good_reduction_control"].update(
                {"gcd_P12_derivative_coefficients_low_to_high": [0, 1]}
            )
        )

    def test_22_root_degree_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["branch_theorem"].update(
                {"normalizing_root_degree": 2}
            )
        )

    def test_23_fractional_order_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["branch_theorem"].update(
                {"normalized_root_local_orders": ["integral"]}
            )
        )

    def test_24_rational_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["branch_theorem"].update(
                {"normalized_root_is_rational": True}
            )
        )

    def test_25_meromorphic_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["branch_theorem"].update(
                {"normalized_root_is_single_valued_meromorphic_across_divisor": True}
            )
        )

    def test_26_discarding_log_germ_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"C45_normalized_euler_germ": "DISCARDED"}
            )
        )

    def test_27_fredholm_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"normalized_root_as_meromorphic_fredholm_determinant": "PROVED"}
            )
        )

    def test_28_route_a_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"A3": "A3_EXACT_DIVISOR_CANDIDATE"}
            )
        )

    def test_29_route_b_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"route_b_invocation_allowed": True}
            )
        )

    def test_30_scope_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].update(
                {"normalized_root_claimed_single_valued_meromorphic": True}
            )
        )

    def test_31_source_hash_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"][2].update({"sha256": "f" * 64})
        )

    def test_32_unknown_top_level_key_rejected(self):
        certificate = rehash(self.certificate)
        certificate["unknown"] = 1
        gates, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)
        self.assertTrue(any(row["gate"] == "G01_SCHEMA_AND_TYPES" and row["status"] == "FAIL" for row in gates))

    def test_33_unexpected_replay_crash_is_error(self):
        original = checker.expected_payload
        try:
            def explode(_project):
                raise RuntimeError("synthetic checker crash")

            checker.expected_payload = explode
            gates, passed = checker.audit_certificate(self.certificate, PROJECT)
        finally:
            checker.expected_payload = original
        self.assertFalse(passed)
        self.assertTrue(any(row["status"] == "ERROR" for row in gates))


if __name__ == "__main__":
    unittest.main()
