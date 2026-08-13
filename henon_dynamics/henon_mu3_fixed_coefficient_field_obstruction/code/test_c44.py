#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

import c44_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c44_certificate.json"


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C44MutationTests(unittest.TestCase):
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

    def test_02_producer_and_checker_replays_agree(self):
        self.assertEqual(self.certificate["payload"], checker.expected_payload(PROJECT))

    def test_03_bad_digest_is_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload_sha256"] = "0" * 64
        _, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)

    def test_04_bool_prime_is_not_an_integer(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][0].update({"prime": True})
        )

    def test_05_float_prime_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][0].update({"prime": 7.0})
        )

    def test_06_incomplete_prime_ledger_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"]["control_primes"].pop()
        )

    def test_07_control_bound_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"].update({"bound_inclusive": 487})
        )

    def test_08_histogram_mutation_is_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][4]["phase_histogram"][3] += 1

        self.assert_rejected(mutate)

    def test_09_rho_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][2].update({"rho_order_3": 1})
        )

    def test_10_first_moment_formula_mutation_is_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][3]["first_nonzero_power_moment"][
                "closed_formula_mod_p"
            ] += 1

        self.assert_rejected(mutate)

    def test_11_second_moment_formula_mutation_is_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][5]["second_nonzero_power_moment"][
                "direct_mod_p"
            ] += 1

        self.assert_rejected(mutate)

    def test_12_stabilizer_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][6].update(
                {"paired_scaling_stabilizer": [1]}
            )
        )

    def test_13_field_degree_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][7].update(
                {"paired_moment_field_degree": 2}
            )
        )

    def test_14_p7_polynomial_mutation_is_rejected(self):
        def mutate(c):
            c["payload"]["p7_anchor"][
                "paired_moment_primitive_minimal_polynomial_high_to_low"
            ][-1] += 1

        self.assert_rejected(mutate)

    def test_15_p7_irreducibility_verdict_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["p7_anchor"].update({"irreducible_over_Q": False})
        )

    def test_16_zero_fibre_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][8].update(
                {"zero_fibre_count": 0}
            )
        )

    def test_17_field_trace_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][9].update(
                {"paired_moment_field_trace": 6}
            )
        )

    def test_18_fixed_field_upgrade_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["all_prime_theorem"].update(
                {"fixed_coefficient_number_field": "POSSIBLE"}
            )
        )

    def test_19_stop_decision_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"uniform_fixed_rank_compatible_system": "CONTINUE"}
            )
        )

    def test_20_inert_clock_averaging_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["conventions"].update(
                {"inert_prime_clock_if_extended": "p^(-s)"}
            )
        )

    def test_21_route_b_upgrade_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"route_b_invocation_allowed": True}
            )
        )

    def test_22_global_continuation_upgrade_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].update(
                {"global_meromorphic_continuation_claimed": True}
            )
        )

    def test_23_source_hash_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"][0].update({"sha256": "f" * 64})
        )

    def test_24_unknown_top_level_key_is_rejected(self):
        certificate = rehash(self.certificate)
        certificate["unknown"] = 1
        gates, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)
        self.assertTrue(any(row["gate"] == "G01_SCHEMA_AND_TYPES" and row["status"] == "FAIL" for row in gates))

    def test_25_unexpected_replay_crash_is_reported_as_error(self):
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

    def test_26_zero_fibre_theorem_downgrade_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["all_prime_zero_fibre_theorem"].update(
                {"status": "FINITE_CONTROLS_ONLY"}
            )
        )


if __name__ == "__main__":
    unittest.main()
