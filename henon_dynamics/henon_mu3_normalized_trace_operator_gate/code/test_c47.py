#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

import c47_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c47_certificate.json"


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C47MutationTests(unittest.TestCase):
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
            "mutation rejected only by full-payload fallback",
        )

    def test_01_base_passes(self):
        gates, passed = checker.audit_certificate(self.certificate, PROJECT)
        self.assertTrue(passed)
        self.assertEqual(len(gates), 12)

    def test_02_replay_matches(self):
        self.assertEqual(self.certificate["payload"], checker.expected_payload(PROJECT))

    def test_03_bad_digest_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload_sha256"] = "0" * 64
        _, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)

    def test_04_bool_prime_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_block_controls"][0].update({"prime": True})
        )

    def test_05_incomplete_prime_ledger_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"]["control_primes"].pop()
        )

    def test_06_bound_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"].update(
                {"control_bound_inclusive": 487}
            )
        )

    def test_07_even_dimension_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_block_controls"][2].update(
                {"total_even_dimension": 0}
            )
        )

    def test_08_odd_dimension_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_block_controls"][3].update(
                {"total_odd_dimension": 0}
            )
        )

    def test_09_identity_trace_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_block_controls"][4][
                "positive_normalized_trace_of_identity"
            ]["numerator"] += 1

        self.assert_rejected(mutate)

    def test_10_first_supertrace_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_block_controls"][5][
                "first_signed_supertrace_moment"
            ]["denominator"] += 1

        self.assert_rejected(mutate)

    def test_11_positive_signed_trace_conflation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_operator_algebra"].update(
                {"positive_trace_warning": "tau=str"}
            )
        )

    def test_12_supertrace_identity_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_operator_algebra"].update(
                {"moment_identity": "averaged moments"}
            )
        )

    def test_13_FK_phase_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_operator_algebra"].update(
                {"fuglede_kadison_warning": "FK equals complex G"}
            )
        )

    def test_14_moment_prime_ledger_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"]["moment_control_primes"].pop()
        )

    def test_15_n3_zero_count_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_chronological_moment_controls"][0][
                "chronological_zero_counts_n1_n2_n3"
            ][2] += 1

        self.assert_rejected(mutate)

    def test_16_C2_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_chronological_moment_controls"][3][
                "galois_traced_moments_C1_C2_C3"
            ][1]["numerator"] += 1

        self.assert_rejected(mutate)

    def test_17_fractional_C3_rounding_rejected(self):
        def mutate(c):
            c["payload"]["exact_chronological_moment_controls"][0][
                "galois_traced_moments_C1_C2_C3"
            ][2] = {"numerator": 1, "denominator": 1}

        self.assert_rejected(mutate)

    def test_18_normalized_C3_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_chronological_moment_controls"][5][
                "normalized_signed_supertrace_moments_c1_c2_c3"
            ][2]["denominator"] += 1

        self.assert_rejected(mutate)

    def test_19_Lq_identity_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"exact_Lq_identity": "signed cancellation"}
            )
        )

    def test_20_L1_threshold_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"tau_L1_threshold": "L1(M,tau) iff Re(s)>1/2"}
            )
        )

    def test_21_L2_threshold_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"tau_L2_threshold": "L2(M,tau) iff Re(s)>1/2"}
            )
        )

    def test_22_L3_threshold_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"tau_L3_threshold": "L3(M,tau) iff Re(s)>1/2"}
            )
        )

    def test_23_L4_threshold_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"tau_L4_threshold": "L4(M,tau) iff Re(s)>0"}
            )
        )

    def test_24_grading_absolute_value_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"grading_cannot_improve_positive_tau_L1": "cancels"}
            )
        )

    def test_25_det4_order_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["regularized_graded_determinant"].update(
                {"minimal_fixed_schatten_order_on_full_domain": 3}
            )
        )

    def test_26_det4_domain_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["regularized_graded_determinant"].update(
                {"domain": "all s"}
            )
        )

    def test_27_factorization_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["regularized_graded_determinant"].update(
                {"exact_factorization": "G=det4"}
            )
        )

    def test_28_fitted_counterterm_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["regularized_graded_determinant"].update(
                {"counterterm_status": "fitted"}
            )
        )

    def test_29_operator_upgrade_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"finite_local_normalized_trace_model": "OPEN"}
            )
        )

    def test_30_L1_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"ordinary_global_semifinite_trace_class_on_critical_half_plane": "PROVED"}
            )
        )

    def test_31_route_a_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"A3": "A3_EXACT_DIVISOR_CANDIDATE"}
            )
        )

    def test_32_route_b_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"route_b_invocation_allowed": True}
            )
        )

    def test_33_scope_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].update(
                {"hilbert_polya_self_adjoint_operator_constructed": True}
            )
        )

    def test_34_source_hash_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"][1].update({"sha256": "f" * 64})
        )

    def test_35_unknown_top_key_rejected(self):
        certificate = rehash(self.certificate)
        certificate["unknown"] = 1
        gates, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)
        self.assertTrue(any(row["gate"] == "G01_SCHEMA_AND_TYPES" and row["status"] == "FAIL" for row in gates))

    def test_36_unexpected_replay_crash_is_error(self):
        original = checker.expected_payload
        try:
            def explode(_project):
                raise RuntimeError("synthetic crash")

            checker.expected_payload = explode
            gates, passed = checker.audit_certificate(self.certificate, PROJECT)
        finally:
            checker.expected_payload = original
        self.assertFalse(passed)
        self.assertTrue(any(row["status"] == "ERROR" for row in gates))

    def test_37_classical_Schatten_conflation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["global_operator_algebra"].update(
                {"classical_Schatten_criterion": "X_s in S^q iff q*Re(s)>2"}
            )
        )

    def test_38_unregularized_tau_domain_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["regularized_graded_determinant"].update(
                {"unregularized_tau_determinant_domain": "Re(s)>1/2"}
            )
        )

    def test_39_classical_Fredholm_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["regularized_graded_determinant"].update(
                {"determinant_category": "ordinary Fredholm determinant"}
            )
        )


if __name__ == "__main__":
    unittest.main()
