#!/usr/bin/env python3
"""Targeted mutation tests for HCS-C51 fail-closed gates."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import c51_checker as checker
import c51_atomic_promote as atomic_promote


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = Path(
    os.environ.get("C51_CERTIFICATE", str(PROJECT / "results/c51_certificate.json"))
)
REPOSITORY = Path(__file__).resolve().parents[3]


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C51MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def reject(self, mutation, expected_gate: str) -> None:
        changed = copy.deepcopy(self.certificate)
        mutation(changed)
        gates, passed = checker.audit_certificate(rehash(changed), REPOSITORY)
        self.assertFalse(passed, gates)
        self.assertFalse(any(row["status"] == "ERROR" for row in gates), gates)
        statuses = {row["gate"]: row["status"] for row in gates}
        self.assertEqual(statuses.get(expected_gate), "FAIL", gates)
        self.assertEqual(statuses.get("frozen_full_payload"), "FAIL", gates)
        semantic_gates = {
            "passport_and_sources", "normalization_and_components",
            "exact_moment_replay", "rank_Chern_generating", "center_tower",
            "Tate_and_half_weight", "K_exponent_firewall",
            "ordinary_compatible_system", "cleared_odd_skeleton",
            "Hodge_Gamma", "n4_Hodge", "decisions_and_scope",
        }
        if expected_gate in semantic_gates:
            failed_semantic = {
                gate for gate in semantic_gates if statuses.get(gate) == "FAIL"
            }
            self.assertEqual(failed_semantic, {expected_gate}, gates)

    def test_01_base_certificate(self) -> None:
        self.assertTrue(
            checker.audit_certificate(self.certificate, REPOSITORY)[1]
        )

    def test_02_self_digest(self) -> None:
        changed = copy.deepcopy(self.certificate)
        changed["payload_sha256"] = "0" * 64
        gates, passed = checker.audit_certificate(changed, REPOSITORY)
        self.assertFalse(passed)
        self.assertEqual(
            {row["gate"]: row["status"] for row in gates}["certificate_envelope"],
            "FAIL",
        )

    def test_03_source_lock(self) -> None:
        self.reject(
            lambda c: c["payload"]["source_lock"][0].update({"sha256": "0" * 64}),
            "passport_and_sources",
        )

    def test_04_artifact_status_type(self) -> None:
        self.reject(
            lambda c: c["payload"]["material_passport"].update({"artifact_status": 1}),
            "passport_and_sources",
        )

    def test_05_clock(self) -> None:
        self.reject(
            lambda c: c["payload"]["normalization_convention"].update({"norm_clock": "z=exp(-s)"}),
            "normalization_and_components",
        )

    def test_06_average_transition(self) -> None:
        self.reject(
            lambda c: c["payload"]["normalization_convention"].update({"averaged_transition_matrix_used": True}),
            "normalization_and_components",
        )

    def test_07_raw_weight(self) -> None:
        self.reject(
            lambda c: c["payload"]["trace_components"][3].update({"raw_weight_W": 3}),
            "normalization_and_components",
        )

    def test_08_source_division(self) -> None:
        self.reject(
            lambda c: c["payload"]["trace_components"][6].update({"source_p_division_t": 2}),
            "normalization_and_components",
        )

    def test_09_uniform_trace_formula(self) -> None:
        self.reject(
            lambda c: c["payload"]["exact_moment_theorem"].update({"uniform_form": "C=e+o"}),
            "exact_moment_replay",
        )

    def test_10_n2_control(self) -> None:
        self.reject(
            lambda c: c["payload"]["exact_prime_controls"][0]["moments"]["n2"]["C_p_n"].update({"numerator": -5}),
            "exact_moment_replay",
        )

    def test_11_n3_even_trace(self) -> None:
        self.reject(
            lambda c: c["payload"]["exact_prime_controls"][3]["moments"]["n3"]["even_trace_e_p_n"].update({"denominator": 1}),
            "exact_moment_replay",
        )

    def test_12_n4_fraction_type(self) -> None:
        self.reject(
            lambda c: c["payload"]["exact_prime_controls"][1]["moments"]["n4"]["c_p_n"].update({"numerator": -57.0}),
            "exact_moment_replay",
        )

    def test_13_rank_formula(self) -> None:
        self.reject(
            lambda c: c["payload"]["rank_theorem"].update({"cubic_primitive_rank_formula": "4^n"}),
            "rank_Chern_generating",
        )

    def test_14_rank_chern_coefficient(self) -> None:
        self.reject(
            lambda c: c["payload"]["rank_controls_n2_to_n20"][2].update({"cubic_top_chern_coefficient": 30}),
            "rank_Chern_generating",
        )

    def test_15_rank_row_truncation(self) -> None:
        self.reject(
            lambda c: c["payload"]["rank_controls_n2_to_n20"].pop(),
            "rank_Chern_generating",
        )

    def test_16_tower_variable(self) -> None:
        self.reject(
            lambda c: c["payload"]["center_bifurcation_theorem"].update({"normalized_variable": "u=n*s+1"}),
            "center_tower",
        )

    def test_17_center_value(self) -> None:
        self.reject(
            lambda c: c["payload"]["center_tower_controls_j1_to_j4"][0]["mapped_s_center"].update({"numerator": 0}),
            "center_tower",
        )

    def test_18_odd_alignment_promotion(self) -> None:
        self.reject(
            lambda c: c["payload"]["center_bifurcation_theorem"].update({"odd_weight_alignment_holds_for_full_tower": True}),
            "center_tower",
        )

    def test_19_minimal_witness(self) -> None:
        self.reject(
            lambda c: c["payload"]["center_bifurcation_theorem"]["minimal_exact_witness"]["factor_1_center"].update({"numerator": 0}),
            "center_tower",
        )

    def test_20_integral_tate_center(self) -> None:
        self.reject(
            lambda c: c["payload"]["tate_relabel_controls"][0]["integral_twists"][0].update({"center_invariant": False}),
            "Tate_and_half_weight",
        )

    def test_21_half_weight_physical_mutation(self) -> None:
        self.reject(
            lambda c: c["payload"]["tate_relabel_controls"][0]["formal_half_twist"].update({"fixed_clock_preserves_source_moment": True}),
            "Tate_and_half_weight",
        )

    def test_22_K_exponent(self) -> None:
        self.reject(
            lambda c: c["payload"]["coefficient_field_exponents"]["controls"][1]["candidate_K_L_exponent_per_trace"].update({"numerator": 1}),
            "K_exponent_firewall",
        )

    def test_23_fractional_power_promotion(self) -> None:
        self.reject(
            lambda c: c["payload"]["coefficient_field_exponents"]["controls"][2].update({"ordinary_single_valued_meromorphic_L_power_certified": True}),
            "K_exponent_firewall",
        )

    def test_24_chi_y(self) -> None:
        self.reject(
            lambda c: c["payload"]["n4_Hodge_ledger"]["complete_intersection_X4"]["chi_y_coefficients_low_to_high"].__setitem__(2, -81),
            "n4_Hodge",
        )

    def test_25_twisted_Hodge_type(self) -> None:
        self.reject(
            lambda c: c["payload"]["n4_Hodge_ledger"]["complete_intersection_X4"]["after_Tate_twist_2"][0].update({"p": 0}),
            "n4_Hodge",
        )

    def test_26_full_FE_promotion(self) -> None:
        self.reject(
            lambda c: c["payload"]["scope"].update({"full_Henon_functional_equation_claimed": True}),
            "decisions_and_scope",
        )

    def test_27_half_Tate_adjoined(self) -> None:
        self.reject(
            lambda c: c["payload"]["scope"].update({"half_Tate_object_adjoined": True}),
            "decisions_and_scope",
        )

    def test_28_unknown_nested_key(self) -> None:
        self.reject(
            lambda c: c["payload"]["n4_Hodge_ledger"].update({"unknown": 0}),
            "recursive_exact_schema",
        )

    def test_29_missing_container(self) -> None:
        self.reject(
            lambda c: c["payload"].pop("coefficient_field_exponents"),
            "recursive_exact_schema",
        )

    def test_30_container_type_smuggle(self) -> None:
        self.reject(
            lambda c: c["payload"].update({"center_bifurcation_theorem": []}),
            "recursive_exact_schema",
        )

    def test_31_component_base_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["trace_components"][2].update({"base_motive_rank": 21}),
            "normalization_and_components",
        )

    def test_32_component_contribution_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["trace_components"][3].update({"contribution_rank": 22}),
            "normalization_and_components",
        )

    def test_33_conditional_rank_scope_row(self) -> None:
        self.reject(
            lambda c: c["payload"]["rank_controls_n2_to_n20"][3].update({"source_geometry_status": "HENON_CHAR0_GEOMETRY_LOCKED"}),
            "rank_Chern_generating",
        )

    def test_34_smoothness_overclaim(self) -> None:
        self.reject(
            lambda c: c["payload"]["scope"].update({"Henon_Xn_smoothness_claimed_for_n_greater_than_4": True}),
            "decisions_and_scope",
        )

    def test_35_ordinary_n3_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["ordinary_compatible_system_obstruction"]["controls"][1]["required_even_rank"].update({"numerator": 45}),
            "ordinary_compatible_system",
        )

    def test_36_n4_restriction_overclaim(self) -> None:
        self.reject(
            lambda c: c["payload"]["ordinary_compatible_system_obstruction"].update({"n4_after_Res_K_to_Q_rank_realization": "REFUTED"}),
            "ordinary_compatible_system",
        )

    def test_36b_direct_K_assumption_scope(self) -> None:
        self.reject(
            lambda c: c["payload"]["ordinary_compatible_system_obstruction"].update({"assumptions": "all ordinary compatible systems over Q or K"}),
            "ordinary_compatible_system",
        )

    def test_37_cleared_odd_exponent(self) -> None:
        self.reject(
            lambda c: c["payload"]["denominator_cleared_odd_skeleton"]["controls"][1]["denominator_cleared_K_exponent"].update({"numerator": 3}),
            "cleared_odd_skeleton",
        )

    def test_38_cleared_FE_promotion(self) -> None:
        self.reject(
            lambda c: c["payload"]["denominator_cleared_odd_skeleton"]["controls"][2].update({"functional_equation_status": "PROVED"}),
            "cleared_odd_skeleton",
        )

    def test_39_Gamma_factor(self) -> None:
        self.reject(
            lambda c: c["payload"]["Hodge_Gamma_sector_ledger"]["sector_controls"][2].update({"expected_Gamma_C_factor": "Gamma_C(u)^23"}),
            "Hodge_Gamma",
        )

    def test_40_Gamma_Hodge_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["Hodge_Gamma_sector_ledger"]["sector_controls"][5]["normalized_Hodge_types"][1].update({"multiplicity": 82}),
            "Hodge_Gamma",
        )

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
            self.assertEqual(
                {target: target.read_bytes() for _, target in pairs}, old_bytes
            )
            self.assertFalse(list(root.glob(".*.new")))
            self.assertFalse(list(root.glob(".*.bak")))

    def test_41_second_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(2)

    def test_42_third_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
