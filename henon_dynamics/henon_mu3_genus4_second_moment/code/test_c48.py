#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

import c48_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c48_certificate.json"


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C48MutationTests(unittest.TestCase):
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
                row["status"] == "FAIL" and row["gate"] != "G15_FULL_PAYLOAD_REPLAY"
                for row in gates
            ),
            "mutation rejected only by full-payload fallback",
        )

    def test_01_base_passes(self):
        gates, passed = checker.audit_certificate(self.certificate, PROJECT)
        self.assertTrue(passed)
        self.assertEqual(len(gates), 15)

    def test_02_independent_replay_matches(self):
        self.assertEqual(self.certificate["payload"], checker.expected_payload(PROJECT))

    def test_03_bad_digest_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload_sha256"] = "0" * 64
        _, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)

    def test_04_bool_prime_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][0].update({"prime": True})
        )

    def test_05_incomplete_prime_ledger_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"]["control_primes"].pop()
        )

    def test_06_control_bound_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"].update(
                {"control_bound_inclusive": 193}
            )
        )

    def test_07_rho_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][2].update({"rho_order_3": 1})
        )

    def test_08_chronological_zero_count_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][4].update(
                {"chronological_zero_count_Z_p": 0}
            )
        )

    def test_09_averaging_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["finite_field_model"].update(
                {"averaged_transition_matrix_used": True}
            )
        )

    def test_10_wrong_norm_clock_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["finite_field_model"].update(
                {"norm_clock": "z=exp(-s)"}
            )
        )

    def test_10b_chronological_DP_replaced_by_average_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["finite_field_model"].update(
                {"chronological_control_algorithm": "averaged transition matrix"}
            )
        )

    def test_11_curve_count_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][3]["projective_counts"]["curve_X"] += 1

        self.assert_rejected(mutate)

    def test_12_direction_count_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][6].update(
                {"direction_formula_zero_count": 1}
            )
        )

    def test_13_surface_count_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][1]["projective_counts"][
                "split_Fermat_cubic_surface_S"
            ] += 1

        self.assert_rejected(mutate)

    def test_14_direction_theorem_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["projective_direction_theorem"].update(
                {"exact_count": "averaged count"}
            )
        )

    def test_15_direct_P3_count_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_direct_P3_intersection_controls"][2][
                "direct_S_intersection_R_count_in_P3"
            ] += 1

        self.assert_rejected(mutate)

    def test_16_direct_P3_prime_ledger_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_direct_P3_intersection_controls"].pop()
        )

    def test_17_curve_equation_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["genus4_curve_theorem"].update(
                {"curve_equation": "F=0"}
            )
        )

    def test_18_bidegree_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["genus4_curve_theorem"].update(
                {"bidegree": [3, 2]}
            )
        )

    def test_19_characteristic_scope_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["genus4_curve_theorem"].update(
                {"excluded_characteristics": [3]}
            )
        )

    def test_20_finite_controls_promoted_to_proof_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["genus4_curve_theorem"].update(
                {"smoothness_status": "INFERRED_FROM_CONTROLS"}
            )
        )

    def test_21_smoothness_case_mutation_rejected(self):
        def mutate(c):
            c["payload"]["genus4_curve_theorem"]["smoothness_cases"][0] = "assume smooth"

        self.assert_rejected(mutate)

    def test_22_chart_polynomial_mutation_rejected(self):
        def mutate(c):
            c["payload"]["genus4_curve_theorem"]["four_affine_chart_polynomials"][1] = "0"

        self.assert_rejected(mutate)

    def test_23_genus_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["genus4_curve_theorem"].update(
                {"genus_by_adjunction": 3}
            )
        )

    def test_24_boundary_multiple_root_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][0]["smoothness_finite_control"][
                "B_multiple_roots"
            ] = [[1, 0]]

        self.assert_rejected(mutate)

    def test_25_chart_singularity_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][5][
                "four_affine_chart_singular_counts_over_F_p"
            ][2] = 1

        self.assert_rejected(mutate)

    def test_26_frobenius_trace_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][8].update(
                {"frobenius_trace_a_p": 0}
            )
        )

    def test_27_traced_moment_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][10].update(
                {"galois_traced_second_moment_C_p_2": 0}
            )
        )

    def test_28_normalized_fraction_mutation_rejected(self):
        def mutate(c):
            c["payload"]["exact_controls"][11][
                "normalized_second_moment_c_p_2"
            ]["denominator"] += 1

        self.assert_rejected(mutate)

    def test_29_integer_Weil_gate_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_controls"][12]["integer_Weil_gate"].update(
                {"passes": False}
            )
        )

    def test_30_moment_theorem_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["second_moment_theorem"].update(
                {"exact_traced_identity": "C=0"}
            )
        )

    def test_31_n2_abscissa_mutation_rejected(self):
        def mutate(c):
            c["payload"]["analytic_upgrade"]["absolute_convergence_abscissae"][
                "n_equals_2"
            ] = {"numerator": 1, "denominator": 2}

        self.assert_rejected(mutate)

    def test_32_combined_abscissa_mutation_rejected(self):
        def mutate(c):
            c["payload"]["analytic_upgrade"]["absolute_convergence_abscissae"][
                "combined_log_Euler_germ"
            ] = {"numerator": 0, "denominator": 1}

        self.assert_rejected(mutate)

    def test_33_continuation_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["analytic_upgrade"].update(
                {"continuation_through_one_third": "PROVED"}
            )
        )

    def test_34_L6_domain_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"tau_L6_domain": "Re(s)>0"}
            )
        )

    def test_35_L5_obstruction_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"tau_L5_domain": "Re(s)>1/3"}
            )
        )

    def test_36_minimal_order_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"minimal_fixed_tau_Lq_order_on_full_domain": 5}
            )
        )

    def test_37_factorization_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"exact_factorization": "G=det6"}
            )
        )

    def test_38_fitted_counterterm_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"counterterm_status": "five fitted prefactors"}
            )
        )

    def test_39_decision_upgrade_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].update(
                {"ordinary_trace_class_determinant_on_that_domain": "PROVED"}
            )
        )

    def test_40_route_a_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"A3": "A3_EXACT_DIVISOR_CANDIDATE"}
            )
        )

    def test_41_route_b_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].update(
                {"route_b_invocation_allowed": True}
            )
        )

    def test_42_scope_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].update(
                {"global_meromorphic_continuation_claimed": True}
            )
        )

    def test_43_source_hash_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"][1].update(
                {"sha256": "f" * 64}
            )
        )

    def test_44_aggregate_false_flag_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["aggregate_control"].update(
                {"all_integer_Weil_gates_pass": False}
            )
        )

    def test_45_unknown_top_key_rejected(self):
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

    def test_46_unexpected_replay_crash_is_error(self):
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

    def test_47_tau_and_classical_ideal_conflation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"classical_Schatten_criterion": "X_s in S^q iff q*Re(s)>2"}
            )
        )

    def test_48_classical_trace_class_domain_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"classical_trace_class_domain": "Re(s)>2"}
            )
        )

    def test_49_unregularized_tau_domain_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"unregularized_tau_trace_class_domain": "Re(s)>1/3"}
            )
        )

    def test_50_classical_Fredholm_upgrade_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["sixth_order_regularized_determinant"].update(
                {"determinant_category": "classical Fredholm determinant"}
            )
        )


if __name__ == "__main__":
    unittest.main()
