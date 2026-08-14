#!/usr/bin/env python3
"""Targeted fail-closed mutation and transaction tests for HCS-C53."""

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

import c53_atomic_promote as atomic_promote
import c53_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = Path(
    os.environ.get("C53_CERTIFICATE", str(PROJECT / "results/c53_certificate.json"))
)
CHECKER = PROJECT / "code/c53_checker.py"
SEMANTIC_GATES = {
    "passport",
    "source_lock",
    "all_n_exact_descent",
    "all_n_contract",
    "all_n_theorem_scope",
    "n4_explicit_model",
    "twisted_group_scheme",
    "nonconstant_outer_twist",
    "descended_Chow_projectors",
    "compatible_raw_local_factors",
    "reciprocity_pairing",
    "split_half_root_rank255",
    "inert_base_change_dictionary",
    "Artin_base_change",
    "p7_reconnaissance_regression_anchor",
    "scope_firewall",
}


def rehash(certificate: dict) -> dict:
    value = copy.deepcopy(certificate)
    value["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(value["payload"]).encode()
    ).hexdigest()
    return value


def checker_result(certificate: dict) -> tuple[subprocess.CompletedProcess, dict]:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        source = root / "certificate.json"
        output = root / "check.json"
        source.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
        process = subprocess.run(
            [sys.executable, str(CHECKER), str(source), "--output", str(output)],
            text=True,
            capture_output=True,
            check=False,
        )
        return process, json.loads(output.read_text())


def checker_result_raw(raw: str) -> tuple[subprocess.CompletedProcess, dict]:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        source = root / "certificate.json"
        output = root / "check.json"
        source.write_text(raw)
        process = subprocess.run(
            [sys.executable, str(CHECKER), str(source), "--output", str(output)],
            text=True,
            capture_output=True,
            check=False,
        )
        return process, json.loads(output.read_text())


class C53MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def reject(self, mutation, expected_gate: str) -> None:
        changed = copy.deepcopy(self.certificate)
        mutation(changed)
        process, result = checker_result(rehash(changed))
        self.assertNotEqual(process.returncode, 0, process.stdout + process.stderr)
        self.assertFalse(result["all_pass"], result)
        self.assertFalse(any(row["status"] == "ERROR" for row in result["gates"]), result)
        statuses = {row["name"]: row["status"] for row in result["gates"]}
        self.assertEqual(statuses.get(expected_gate), "FAIL", result)
        self.assertEqual(statuses.get("frozen_expected_payload"), "FAIL", result)
        if expected_gate in SEMANTIC_GATES:
            failed = {gate for gate in SEMANTIC_GATES if statuses.get(gate) == "FAIL"}
            self.assertEqual(failed, {expected_gate}, result)

    def test_01_base_certificate(self) -> None:
        process, result = checker_result(self.certificate)
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.assertTrue(result["all_pass"])

    def test_02_self_digest(self) -> None:
        changed = copy.deepcopy(self.certificate)
        changed["payload_sha256"] = "0" * 64
        process, result = checker_result(changed)
        self.assertNotEqual(process.returncode, 0)
        statuses = {row["name"]: row["status"] for row in result["gates"]}
        self.assertEqual(statuses["payload_hash"], "FAIL")

    def test_03_passport_status_regression(self) -> None:
        self.reject(lambda c: c["payload"]["material_passport"].update({"artifact_status": "PAPER_PENDING"}), "passport")

    def test_04_source_lock(self) -> None:
        self.reject(lambda c: c["payload"]["source_lock"]["certificates"][1].update({"sha256": "0" * 64}), "source_lock")

    def test_05_closing_edge(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["source_equations"].update({"chronological_closing_edge_preserved": False}), "all_n_contract")

    def test_06_phase_rule(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["descent_data"].update({"phase_rule": "all phases zero"}), "all_n_contract")

    def test_07_rational_terminal(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["rational_forms"].update({"terminal_even_n": "u_(n-1)u_n"}), "all_n_contract")

    def test_08_determinant_formula(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["fixed_basis"].update({"determinant_closed_formula": "det(B_n)=1"}), "all_n_theorem_scope")

    def test_09_all_n_smoothness_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["scope"].update({"source_ordered_smoothness_all_n_claimed": True}), "all_n_theorem_scope")

    def test_10_control_phase(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["exact_controls_n2_to_n10"][0]["M_phase_exponents"].__setitem__(2, 0), "all_n_exact_descent")

    def test_11_control_bool_type(self) -> None:
        self.reject(lambda c: c["payload"]["B0_all_n_algebraic_descent"]["exact_controls_n2_to_n10"][3].update({"det_B_closed_formula_matches": 1}), "all_n_exact_descent")

    def test_12_n4_M_phase(self) -> None:
        self.reject(lambda c: c["payload"]["B1_explicit_n4_Q_model"]["descent_M"]["rho_phase_exponents"].__setitem__(2, 0), "n4_explicit_model")

    def test_13_n4_basis(self) -> None:
        self.reject(lambda c: c["payload"]["B1_explicit_n4_Q_model"]["Q_model"]["x_equals_Bu"].__setitem__(6, "u2-theta*v2"), "n4_explicit_model")

    def test_14_n4_K_model(self) -> None:
        self.reject(lambda c: c["payload"]["B1_explicit_n4_Q_model"]["K_model"].update({"rho": "rho=1"}), "n4_explicit_model")

    def test_15_alpha_r(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["group_scheme"].update({"alpha_r": "r"}), "twisted_group_scheme")

    def test_16_alpha_s_normal_form(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["group_scheme"].update({"alpha_s_equivalent_normal_form": "s*r"}), "twisted_group_scheme")

    def test_17_orbit_duplicate(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["group_scheme"]["Galois_orbits"][0].append(0), "twisted_group_scheme")

    def test_18_constant_group_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["group_scheme"].update({"constant_group_scheme": True}), "nonconstant_outer_twist")

    def test_19_fixed_elements(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["group_scheme"]["Q_rational_geometric_element_ids"].append(1), "nonconstant_outer_twist")

    def test_20_reynolds_denominator(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["projectors"].update({"Reynolds_denominator": 2}), "descended_Chow_projectors")

    def test_21_transfer_denominator(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["projectors"].update({"quadratic_descent_transfer_denominator": 24}), "descended_Chow_projectors")

    def test_22_raw_eG_middle(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["projectors"].update({"raw_eG_called_middle_rank10": True}), "descended_Chow_projectors")

    def test_23_core_twist_label(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["motives_over_Q"].update({"CY_type_core": "M0(2), weight 1"}), "descended_Chow_projectors")

    def test_24_core_Hodge_type(self) -> None:
        self.reject(lambda c: c["payload"]["B2_twisted_dihedral_Chow_descent"]["motives_over_Q"]["raw_M0_Hodge"][0].update({"p": 1.0}), "descended_Chow_projectors")

    def test_25_raw_weight(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"].update({"weight": 1}), "compatible_raw_local_factors")

    def test_26_Q_coefficient_step(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"].update({"Q_coefficient_step": "assumed"}), "compatible_raw_local_factors")

    def test_27_integrality_step(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"].update({"Z_integrality_step": "Newton alone"}), "compatible_raw_local_factors")

    def test_28_normalized_integrality_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["normalized_core"].update({"coefficients": "Z[T]"}), "compatible_raw_local_factors")

    def test_29_W4_rank(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["Q_packets"].update({"W4_rank": 254}), "split_half_root_rank255")

    def test_30_global_branch_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["split_prime"].update({"branch_scope": "global square root"}), "split_half_root_rank255")

    def test_31_fractional_n3_cleared(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["all_n_split_exponent"].update({"n3": "1 clears"}), "split_half_root_rank255")

    def test_32_n5_unconditional_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["all_n_split_exponent"].update({"n_ge_5": "PROVED"}), "split_half_root_rank255")

    def test_33_inert_clock(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["inert_prime"].update({"norm_clock": "N(mathfrakp)=p"}), "inert_base_change_dictionary")

    def test_34_inert_half_root(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["inert_prime"].update({"Q_factor_recovered_as_half_root": True}), "inert_base_change_dictionary")

    def test_35_p7_trace(self) -> None:
        self.reject(lambda c: c["payload"]["finite_p7_control"].update({"raw_core_trace": -468}), "p7_reconnaissance_regression_anchor")

    def test_36_p7_uncertified_status(self) -> None:
        self.reject(lambda c: c["payload"]["finite_p7_control"].update({"status": "CERTIFIED"}), "p7_reconnaissance_regression_anchor")

    def test_37_FE_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["scope"].update({"functional_equation_claimed": True}), "scope_firewall")

    def test_38_rank2_overclaim(self) -> None:
        self.reject(lambda c: c["payload"]["decisions"].update({"rank2_projector_beyond_group_algebra": "PROVED"}), "scope_firewall")

    def test_39_unknown_top_key(self) -> None:
        self.reject(lambda c: c["payload"].update({"unknown": 0}), "recursive_schema")

    def test_40_missing_container(self) -> None:
        self.reject(lambda c: c["payload"].pop("B3_compatible_local_factors"), "recursive_schema")

    def test_41_container_type(self) -> None:
        self.reject(lambda c: c["payload"].update({"B2_twisted_dihedral_Chow_descent": []}), "recursive_schema")

    def assert_promotion_rollback(self, failure_after: int) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pairs = []
            old_bytes = {}
            for index in range(3):
                source = root / f"source_{index}"
                target = root / f"target_{index}"
                source.write_bytes(f"new-{index}".encode())
                target.write_bytes(f"old-{index}".encode())
                old_bytes[target] = target.read_bytes()
                pairs.append((source, target))
            self.assertFalse(atomic_promote.promote(pairs, failure_after))
            self.assertEqual({target: target.read_bytes() for _, target in pairs}, old_bytes)
            self.assertFalse(list(root.glob(".*.new")))
            self.assertFalse(list(root.glob(".*.bak")))

    def test_42_second_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(2)

    def test_43_third_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(3)

    def test_44_geometric_frobenius_convention(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"].update({"frobenius_convention": "arithmetic Frobenius"}), "compatible_raw_local_factors")

    def test_45_characteristic_polynomial_monic_type(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"].update({"characteristic_polynomial_monic": 1}), "compatible_raw_local_factors")

    def test_46_local_polynomial_not_called_monic(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"].update({"good_local_polynomial_called_monic": True}), "compatible_raw_local_factors")

    def test_47_normalized_motive(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["normalized_core"].update({"motive": "M0(1)"}), "compatible_raw_local_factors")

    def test_48_normalized_Frobenius(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["normalized_core"].update({"Frobenius_on_twist2": "F_C4=F_M0*p^2"}), "compatible_raw_local_factors")

    def test_49_normalized_local_polynomial(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["normalized_core"].update({"local_polynomial": "P_p_raw(p^2*T)"}), "compatible_raw_local_factors")

    def test_50_reciprocity_self_transpose(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"]["reciprocity_mechanism"].update({"projector_self_transpose": False}), "reciprocity_pairing")

    def test_51_reciprocity_multiplier(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"]["reciprocity_mechanism"].update({"Frobenius_similitude_multiplier": "p"}), "reciprocity_pairing")

    def test_52_split_condition(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["split_prime"].update({"condition": "p split"}), "split_half_root_rank255")

    def test_53_split_identity(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["split_prime"].update({"identity": "global square root"}), "split_half_root_rank255")

    def test_54_inert_raw_identity(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["inert_prime"].update({"raw_identity": "P_K=P_Q"}), "inert_base_change_dictionary")

    def test_55_Artin_identity(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"].update({"Artin_base_change": "L_K=L_Q"}), "Artin_base_change")

    def test_56_duplicate_JSON_key(self) -> None:
        raw=json.dumps(self.certificate,indent=2,sort_keys=True)+"\n"
        needle='  "schema": "hcs-c53-certificate-v1"'
        self.assertIn(needle,raw)
        process,result=checker_result_raw(raw.replace(needle,needle+',\n'+needle,1))
        self.assertNotEqual(process.returncode,0)
        self.assertEqual(result["gates"],[{"detail":"duplicate JSON key: schema","name":"strict_json_parse","status":"FAIL"}])

    def test_57_unknown_envelope_key(self) -> None:
        changed=copy.deepcopy(self.certificate);changed["unknown_envelope"]=0
        process,result=checker_result(changed)
        self.assertNotEqual(process.returncode,0)
        statuses={row["name"]:row["status"] for row in result["gates"]}
        self.assertEqual(statuses["schema"],"FAIL")
        self.assertEqual(statuses["frozen_expected_payload"],"PASS")

    def test_58_first_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(1)

    def test_59_missing_initial_target_rolls_back(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);pairs=[];old={}
            for index in range(3):
                source=root/f"source_{index}";target=root/f"target_{index}"
                source.write_bytes(f"new-{index}".encode())
                if index!=1:
                    target.write_bytes(f"old-{index}".encode());old[target]=target.read_bytes()
                pairs.append((source,target))
            self.assertFalse(atomic_promote.promote(pairs,2))
            self.assertEqual({target:target.read_bytes() for target in old},old)
            self.assertFalse(pairs[1][1].exists())
            self.assertFalse(list(root.glob(".*.new")))
            self.assertFalse(list(root.glob(".*.bak")))

    def test_60_reciprocity_orthogonal_kernel(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"]["reciprocity_mechanism"].update({"kernel_equals_image_orthogonal": False}), "reciprocity_pairing")

    def test_61_reciprocity_nondegenerate(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"]["reciprocity_mechanism"].update({"restricted_pairing_nondegenerate": False}), "reciprocity_pairing")

    def test_62_reciprocity_Frobenius_commutation(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"]["reciprocity_mechanism"].update({"Frobenius_commutes_with_projector": False}), "reciprocity_pairing")

    def test_63_reciprocity_eigenvalue_pairing(self) -> None:
        self.reject(lambda c: c["payload"]["B3_compatible_local_factors"]["raw_core"]["reciprocity_mechanism"].update({"eigenvalue_pairing": "alpha <-> p/alpha"}), "reciprocity_pairing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
