#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

import c45_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c45_certificate.json"


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C45MutationTests(unittest.TestCase):
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
            "mutation was rejected only by the full-payload fallback",
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
            lambda c: c["payload"]["exact_trace_controls"][0].update({"prime": True})
        )

    def test_05_float_prime_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_trace_controls"][0].update({"prime": 7.0})
        )

    def test_06_incomplete_trace_prime_ledger_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"]["trace_control_primes"].pop()
        )

    def test_07_trace_bound_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"].update(
                {"trace_control_bound_inclusive": 487}
            )
        )

    def test_08_n1_zero_count_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_trace_controls"][4].update(
                {"chronological_n1_zero_count": 0}
            )
        )

    def test_09_first_trace_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_trace_controls"][5].update(
                {"ordinary_norm_first_log_moment_C_p_1": 6}
            )
        )

    def test_10_normalized_first_moment_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_trace_controls"][6][
                "normalized_first_log_moment_c_p_1"
            ]["numerator"] += 1

        self.assert_rejected(mutate)

    def test_11_norm_virtual_degree_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_trace_controls"][7].update(
                {"ordinary_norm_virtual_degree": 4}
            )
        )

    def test_12_prefactor_triangle_bound_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_trace_controls"][8]["prefactor_lower_bounds"][3][
                "triangle_inequality_rhs"
            ] += 1

        self.assert_rejected(mutate)

    def test_13_incomplete_n2_ledger_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"]["n2_control_primes"].pop()
        )

    def test_14_n2_phase_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_chronological_n2_controls"][0].update(
                {"chronological_phase": "averaged transition"}
            )
        )

    def test_15_n2_zero_count_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_chronological_n2_controls"][3].update(
                {"chronological_n2_zero_count": 0}
            )
        )

    def test_16_second_trace_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_chronological_n2_controls"][5].update(
                {"ordinary_norm_second_log_moment_C_p_2": -6}
            )
        )

    def test_17_normalized_second_moment_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_chronological_n2_controls"][6][
                "normalized_second_log_moment_c_p_2"
            ]["denominator"] += 1

        self.assert_rejected(mutate)

    def test_18_fake_full_tate_cancellation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"one_minus_z_power_6_tate_cancellation": "PROVED_ALL_ORDERS"}
            )
        )

    def test_19_normalized_bound_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["all_prime_theorems"].update(
                {"normalized_higher_moment_bound": "abs(c_p,n)<=1"}
            )
        )

    def test_20_normalized_half_plane_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["all_prime_theorems"].update(
                {"normalized_euler_germ": "entire"}
            )
        )

    def test_21_ordinary_norm_rank_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"ordinary_galois_norm_rational_descent": "FIXED_RANK"}
            )
        )

    def test_22_normalized_root_rational_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"normalized_log_norm_as_rational_fredholm_determinant": "PROVED"}
            )
        )

    def test_23_route_a_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"A3": "A3_EXACT_DIVISOR_CANDIDATE"}
            )
        )

    def test_24_route_b_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"route_b_invocation_allowed": True}
            )
        )

    def test_25_scope_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].update(
                {"normalized_root_claimed_fredholm_determinant": True}
            )
        )

    def test_26_source_hash_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"][1].update({"sha256": "f" * 64})
        )

    def test_27_unknown_top_level_key_rejected(self):
        certificate = rehash(self.certificate)
        certificate["unknown"] = 1
        gates, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)
        self.assertTrue(
            any(
                row["gate"] == "G01_SCHEMA_AND_TYPES" and row["status"] == "FAIL"
                for row in gates
            )
        )

    def test_28_unexpected_replay_crash_is_error(self):
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
