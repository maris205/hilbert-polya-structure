#!/usr/bin/env python3

from __future__ import annotations

import copy
import hashlib
import json
import os
import unittest
from pathlib import Path

import c49_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = Path(
    os.environ.get("C49_CERTIFICATE", str(PROJECT / "results" / "c49_certificate.json"))
)


def rehash(certificate: dict) -> dict:
    answer = copy.deepcopy(certificate)
    answer["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(answer["payload"])
    ).hexdigest()
    return answer


class C49MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def assert_rejected(self, mutation) -> None:
        certificate = copy.deepcopy(self.certificate)
        mutation(certificate)
        certificate = rehash(certificate)
        gates, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)
        self.assertFalse(any(row["status"] == "ERROR" for row in gates), gates)
        self.assertTrue(any(row["status"] == "FAIL" for row in gates), gates)

    def test_01_base_passes(self):
        gates, passed = checker.audit_certificate(self.certificate, PROJECT)
        self.assertTrue(passed)
        self.assertEqual(len(gates), 13)

    def test_02_independent_last_chart_replay_matches(self):
        expected = [checker.rebuild_geometry(row) for row in checker.ROWS]
        self.assertEqual(self.certificate["payload"]["exact_geometry_controls"], expected)

    def test_03_bad_digest_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload_sha256"] = "0" * 64
        _, passed = checker.audit_certificate(certificate, PROJECT)
        self.assertFalse(passed)

    def test_04_unknown_top_key_rejected(self):
        self.assert_rejected(lambda c: c.update({"unknown": 1}))

    def test_05_passport_candidate_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["material_passport"].update({"candidate_id": "HCS-C48"}))

    def test_06_source_hash_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["source_lock"][0].update({"sha256": "f" * 64}))

    def test_07_averaged_transition_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["finite_field_model"].update({"averaged_transition_matrix_used": True}))

    def test_08_wrong_norm_clock_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["finite_field_model"].update({"norm_clock": "z=exp(-s)"}))

    def test_09_phase_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["finite_field_model"].update({"chronological_phase": "averaged phase"}))

    def test_10_direction_formula_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["projective_direction_theorem"].update({"exact_count": "Z=0"}))

    def test_11_split_quadric_formula_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["projective_direction_theorem"].update({"split_Q4_count": "(p+1)^4"}))

    def test_12_geometry_prime_bool_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][0].update({"prime": True}))

    def test_13_rho_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][2].update({"rho_order_3": 1}))

    def test_14_surface_count_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][4]["projective_counts"].update({"Fermat_cubic_fourfold_S": 0}))

    def test_15_intersection_count_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][5]["projective_counts"].update({"complete_intersection_X": 0}))

    def test_16_chart_count_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][6]["first_nonzero_u_chart_counts_for_X"].__setitem__(0, 0))

    def test_17_direction_zero_count_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][7].update({"direction_formula_zero_count_Z_p_3": 0}))

    def test_18_alpha_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][8].update({"alpha_p": 0}))

    def test_19_beta_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][9].update({"beta_p": 0}))

    def test_20_rational_C_denominator_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][10]["galois_traced_third_moment_C_p_3"].update({"denominator": 1}))

    def test_21_normalized_c_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][11]["normalized_third_moment_c_p_3"].update({"numerator": 0}))

    def test_22_integer_Weil_gate_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][12]["integer_Weil_controls"].update({"passes": False}))

    def test_23_Jacobi_divisibility_control_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][13]["arithmetic_divisibility_controls"].update({"alpha_minus_20p2_divisible_by_p": False}))

    def test_24_Chevalley_divisibility_control_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][14]["arithmetic_divisibility_controls"].update({"beta_divisible_by_p": False}))

    def test_25_finer_distribution_promotion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][15]["finite_observation_only"].update({"finer_quotient_distribution_promoted_to_theorem": True}))

    def test_26_finite_singularity_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_geometry_controls"][16].update({"normalized_singularity_candidates_forward_recurrence": 1}))

    def test_27_chronology_zero_count_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_chronology_controls"][4].update({"literal_six_step_DP_zero_count_Z_p_3": 0}))

    def test_28_chronology_ledger_truncation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["exact_chronology_controls"].pop())

    def test_29_generic_smoothness_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"].update({"generic_characteristic_zero_smooth": False}))

    def test_30_b3_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"].update({"middle_betti_number_b3": 4}))

    def test_31_H_coefficient_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"]["finite_characteristic_firewall"]["L_remainder_H_integer_coefficients_descending"].__setitem__(0, 0))

    def test_32_resultant_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"]["finite_characteristic_firewall"].update({"recorded_resultant_Res_R_H": 0}))

    def test_33_denominator_factor_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"]["finite_characteristic_firewall"]["projection_denominator_factorization"][0].update({"exponent": 3}))

    def test_34_split_exception_list_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"]["finite_characteristic_firewall"]["split_projection_denominator_primes"].pop())

    def test_35_modular_Groebner_record_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"]["finite_characteristic_firewall"]["direct_modular_Groebner_records_at_split_denominators"][0].update({"recorded_outcome": "SINGULAR"}))

    def test_36_all_split_smoothness_promotion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["generic_fano_threefold_theorem"].update({"all_split_prime_smoothness_status": "PROVED"}))

    def test_37_moment_identity_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["third_moment_theorem"].update({"exact_identity": "C=0"}))

    def test_38_Jacobi_theorem_downgrade_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["third_moment_theorem"].update({"Fermat_Jacobi_formula_all_split_theorem": False}))

    def test_39_Chevalley_theorem_downgrade_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["third_moment_theorem"].update({"Chevalley_Warning_beta_divisibility_all_good_split_theorem": False}))

    def test_40_refined_identity_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["third_moment_theorem"].update({"refined_identity": "C=-2"}))

    def test_41_n3_abscissa_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["analytic_upgrade"]["absolute_convergence_abscissae"].update({"n_equals_3": {"numerator": 1, "denominator": 3}}))

    def test_42_combined_abscissa_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["analytic_upgrade"]["absolute_convergence_abscissae"].update({"combined_log_Euler_germ": {"numerator": 0, "denominator": 1}}))

    def test_43_continuation_overclaim_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["analytic_upgrade"].update({"continuation_through_one_fourth": "PROVED"}))

    def test_44_tau_L8_domain_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["eighth_order_regularized_determinant"].update({"tau_L8_domain": "Re(s)>0"}))

    def test_45_tau_L7_obstruction_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["eighth_order_regularized_determinant"].update({"tau_L7_domain": "Re(s)>1/4"}))

    def test_46_minimal_order_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["eighth_order_regularized_determinant"].update({"minimal_fixed_tau_Lq_order_on_full_domain": 7}))

    def test_47_factorization_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["eighth_order_regularized_determinant"].update({"exact_factorization": "G=det8"}))

    def test_48_classical_Schatten_confusion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["eighth_order_regularized_determinant"].update({"classical_Schatten_criterion": "q*Re(s)>2"}))

    def test_49_decision_smoothness_overclaim_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["decisions"].update({"all_split_prime_smoothness": "PROVED"}))

    def test_50_route_A_overclaim_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["route_a"].update({"A3": "A3_EXACT_DIVISOR_CANDIDATE"}))

    def test_51_route_B_invocation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["route_a"].update({"route_b_invocation_allowed": True}))

    def test_52_scope_continuation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].update({"global_meromorphic_continuation_claimed": True}))

    def test_53_scope_all_split_smoothness_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].update({"all_split_prime_smoothness_claimed": True}))

    def test_54_scope_Jacobi_contradiction_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].update({"fermat_Jacobi_formula_all_split_theorem": False}))

    def test_55_aggregate_warning_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["aggregate_control"].update({"finite_observation_warning": "all-prime fit"}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
