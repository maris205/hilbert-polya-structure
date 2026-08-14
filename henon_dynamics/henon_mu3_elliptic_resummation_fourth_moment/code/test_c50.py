#!/usr/bin/env python3
from __future__ import annotations
import copy,hashlib,json,os,unittest
from pathlib import Path
import c50_checker as checker

PROJECT=Path(__file__).resolve().parents[1]
CERT=Path(os.environ.get("C50_CERTIFICATE",str(PROJECT/"results/c50_certificate.json")))

def rehash(c):
    c=copy.deepcopy(c); c["payload_sha256"]=hashlib.sha256(checker.canonical_json(c["payload"])).hexdigest(); return c

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.cert=json.loads(CERT.read_text())
    def reject(self,mutation,expected_gate):
        c=copy.deepcopy(self.cert); mutation(c); gates,passed=checker.audit_certificate(rehash(c),Path(__file__).resolve().parents[3]); self.assertFalse(passed)
        self.assertFalse(any(g["status"]=="ERROR" for g in gates),gates)
        statuses={g["gate"]:g["status"] for g in gates}; self.assertEqual(statuses.get(expected_gate),"FAIL",gates)
        self.assertEqual(statuses.get("frozen_full_payload"),"FAIL",gates)
    def test_01_base(self): self.assertTrue(checker.audit_certificate(self.cert,Path(__file__).resolve().parents[3])[1])
    def test_02_digest(self):
        c=copy.deepcopy(self.cert); c["payload_sha256"]="0"*64; self.assertFalse(checker.audit_certificate(c,Path(__file__).resolve().parents[3])[1])
    def test_03_group(self): self.reject(lambda c:c["payload"]["curve_and_group"]["exact_identities"].update({"T2_squared_identity":False}),"group_and_isogeny")
    def test_04_isogeny(self): self.reject(lambda c:c["payload"]["jacobian_decomposition"].update({"elliptic_idempotent_rank":2}),"group_and_isogeny")
    def test_05_factor(self): self.reject(lambda c:c["payload"]["local_factor_controls"][0].update({"E_minus_trace":3}),"local_factors")
    def test_06_F2(self): self.reject(lambda c:c["payload"]["second_moment_resummation"].update({"H2_holomorphic_nonzero_domain":"Re(s)>-1"}),"resummation")
    def test_07_average(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"].update({"averaged_transition_matrix_used":True}),"n4_geometry")
    def test_08_groebner(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"]["char0_singular_ideal_reduced_basis_dp"].pop(),"n4_geometry")
    def test_09_n4(self): self.reject(lambda c:c["payload"]["exact_fourth_moment_controls"][0].update({"Z_p_4":0}),"n4_exact_ledger")
    def test_10_p181(self): self.reject(lambda c:c["payload"]["bad_reduction_control"]["normalized_singular_points"].pop(),"p181_negative")
    def test_11_domain(self): self.reject(lambda c:c["payload"]["analytic_continuation"].update({"holomorphic_continuation_domain":"Re(s)>0"}),"analytic_and_route")
    def test_12_A3(self): self.reject(lambda c:c["payload"]["route_a"].update({"A3":"A3_CONTROLLED_CONTINUATION"}),"analytic_and_route")
    def test_13_tau(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"minimal_fixed_order_on_full_domain":9}),"tau_Det10")
    def test_14_classical(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"classical_Hilbert_Schatten_criterion":"X_s in S^q iff q*Re(s)>2"}),"tau_Det10")
    def test_15_overclaim(self): self.reject(lambda c:c["payload"]["scope"].update({"global_nonvanishing_claimed":True}),"scope")
    def test_16_unknown_payload_key(self): self.reject(lambda c:c["payload"].update({"unknown":0}),"recursive_exact_schema")
    def test_17_unknown_nested_key(self): self.reject(lambda c:c["payload"]["curve_and_group"].update({"unknown":0}),"recursive_exact_schema")
    def test_18_source_lock(self): self.reject(lambda c:c["payload"]["source_lock"][0].update({"sha256":"0"*64}),"passport_and_sources")
    def test_19_extension_count(self): self.reject(lambda c:c["payload"]["extension_field_Newton_controls"][0]["curve_counts_degrees_1_to_4"].__setitem__(1,0),"extension_Newton")
    def test_20_factor_status(self): self.reject(lambda c:c["payload"]["local_factor_controls"][0].update({"factorization_status":"FINITE_VERIFIED"}),"local_factors")
    def test_21_Prym_promotion(self): self.reject(lambda c:c["payload"]["jacobian_decomposition"].update({"Prym_description_status":"PROVED"}),"group_and_isogeny")
    def test_22_Eminus_Q_overclaim(self): self.reject(lambda c:c["payload"]["jacobian_decomposition"].update({"E_minus_Q_Weierstrass_model_claimed":True}),"group_and_isogeny")
    def test_23_coefficient_ledger(self): self.reject(lambda c:c["payload"]["second_moment_resummation"]["coefficient_ledger"].update({"Dedekind_zeta_exponent":6}),"resummation")
    def test_24_clock(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"].update({"norm_clock":"z=exp(-s)"}),"n4_geometry")
    def test_25_betti(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"].update({"complete_intersection_fivefold_b5":167}),"n4_geometry")
    def test_26_smoothness_overclaim(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"].update({"all_split_prime_smoothness":True}),"n4_geometry")
    def test_27_n4_row_truncation(self): self.reject(lambda c:c["payload"]["exact_fourth_moment_controls"].pop(),"n4_exact_ledger")
    def test_28_n4_fraction(self): self.reject(lambda c:c["payload"]["exact_fourth_moment_controls"][2]["C_p_4"].update({"denominator":1}),"n4_exact_ledger")
    def test_29_bad_scope(self): self.reject(lambda c:c["payload"]["scope"].update({"p181_contaminates_C48_curve":True}),"p181_negative")
    def test_30_full_FE(self): self.reject(lambda c:c["payload"]["analytic_continuation"].update({"full_functional_equation":True}),"analytic_and_route")
    def test_31_elliptic_FE(self): self.reject(lambda c:c["payload"]["analytic_continuation"].update({"elliptic_factor_functional_equation":False}),"analytic_and_route")
    def test_32_tau_L9(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"tau_L9_domain":"Re(s)>1/5"}),"tau_Det10")
    def test_33_continued_identity(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"continued_identity":"G=raw"}),"tau_Det10")
    def test_34_Fredholm_overclaim(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"ordinary_Fredholm_determinant_claimed":True}),"tau_Det10")
    def test_35_FK_overclaim(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"positive_Fuglede_Kadison_equals_complex_G":True}),"tau_Det10")
    def test_36_route_B(self): self.reject(lambda c:c["payload"]["route_a"].update({"route_b_invoked":True}),"analytic_and_route")
    def test_37_idempotent_rank(self): self.reject(lambda c:c["payload"]["idempotent_matrix_control"].update({"primitive_minus_rank":2}),"matrix_idempotents")
    def test_38_idempotent_matrix(self): self.reject(lambda c:c["payload"]["idempotent_matrix_control"]["e_j_matrix"][0][0].update({"numerator":0}),"matrix_idempotents")
    def test_39_chern_coefficient(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"]["Chern_Betti_recomputation"].update({"cubic_top_chern_coefficient":30}),"n4_geometry")
    def test_40_euler(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"]["Chern_Betti_recomputation"].update({"complete_intersection_Euler_characteristic":-161}),"n4_geometry")
    def test_41_Newton_coefficient(self): self.reject(lambda c:c["payload"]["extension_field_Newton_controls"][1]["Newton_polynomial_coefficients_low_to_high"].__setitem__(3,0),"extension_Newton")
    def test_42_reciprocal_coefficient(self): self.reject(lambda c:c["payload"]["extension_field_Newton_controls"][2]["Newton_polynomial_coefficients_low_to_high"].__setitem__(7,0),"extension_Newton")
    def test_43_closing_edge_deleted(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"].update({"chronological_phase":"Phi_4=2*sum x_i^3+sum_i=0^6 x_i*x_(i+1)"}),"n4_geometry")
    def test_44_chronology_permuted(self): self.reject(lambda c:c["payload"]["fourth_moment_geometry"].update({"chronological_phase":"Phi_4 with permuted transitions"}),"n4_geometry")
    def test_45_bad_Q_row(self): self.reject(lambda c:c["payload"]["bad_reduction_control"]["normalized_singular_points"][0].update({"Q_mod_p":1}),"p181_negative")
    def test_46_bad_Q_summary(self): self.reject(lambda c:c["payload"]["bad_reduction_control"].update({"all_points_Q_zero":False}),"p181_negative")
    def test_47_type_smuggle(self): self.reject(lambda c:c["payload"]["jacobian_decomposition"].update({"genus_C":4.0}),"strict_static_leaves")
    def test_48_unread_leaf(self): self.reject(lambda c:c["payload"]["curve_and_group"].update({"base_field":"K=Q"}),"strict_static_leaves")
    def test_49_missing_nested_key(self): self.reject(lambda c:c["payload"]["curve_and_group"].pop("generators"),"recursive_exact_schema")
    def test_50_container_type(self): self.reject(lambda c:c["payload"].update({"curve_and_group":[]}),"recursive_exact_schema")
    def test_51_bad_coordinate_type(self): self.reject(lambda c:c["payload"]["bad_reduction_control"]["normalized_singular_points"][0]["coordinates"].__setitem__(0,9.0),"p181_negative")
    def test_52_bad_recurrence_bool_type(self): self.reject(lambda c:c["payload"]["bad_reduction_control"]["normalized_singular_points"][0].update({"normalized_gradient_recurrence_pass":1}),"p181_negative")
    def test_53_Det10_order_type(self): self.reject(lambda c:c["payload"]["tenth_order_regularized_determinant"].update({"minimal_fixed_order_on_full_domain":10.0}),"tau_Det10")

if __name__=="__main__": unittest.main(verbosity=2)
