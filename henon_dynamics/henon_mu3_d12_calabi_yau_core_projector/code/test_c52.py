#!/usr/bin/env python3
"""Targeted mutation and transaction tests for HCS-C52."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import c52_atomic_promote as atomic_promote
import c52_checker as checker


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = Path(
    os.environ.get("C52_CERTIFICATE", str(PROJECT / "results/c52_certificate.json"))
)
REPOSITORY = Path(__file__).resolve().parents[3]
SEMANTIC_GATES = {
    "passport_and_sources",
    "frozen_model",
    "D12_enumeration",
    "middle_Chow_Kuenneth",
    "Cayley_Jacobian_structure",
    "residue_orientation_and_scalar_lift",
    "quotient_action_well_defined",
    "independent_character_replay",
    "middle_realization_split",
    "Q_group_algebra_no_go",
    "decisions",
    "C53_future_firewall",
    "scope_firewall",
}


def rehash(certificate: dict) -> dict:
    certificate = copy.deepcopy(certificate)
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()
    return certificate


class C52MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        # Warm the independent Q(rho) expected payload once for all mutations.
        checker.expected_payload(REPOSITORY)

    def reject(self, mutation, expected_gate: str) -> None:
        changed = copy.deepcopy(self.certificate)
        mutation(changed)
        gates, passed = checker.audit_certificate(rehash(changed), REPOSITORY)
        self.assertFalse(passed, gates)
        self.assertFalse(any(row["status"] == "ERROR" for row in gates), gates)
        statuses = {row["gate"]: row["status"] for row in gates}
        self.assertEqual(statuses.get(expected_gate), "FAIL", gates)
        self.assertEqual(statuses.get("frozen_full_payload"), "FAIL", gates)
        if expected_gate in SEMANTIC_GATES:
            failed = {gate for gate in SEMANTIC_GATES if statuses.get(gate) == "FAIL"}
            self.assertEqual(failed, {expected_gate}, gates)

    def test_01_base_certificate(self) -> None:
        self.assertTrue(checker.audit_certificate(self.certificate, REPOSITORY)[1])

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
            lambda c: c["payload"]["source_lock"][4].update({"sha256": "0" * 64}),
            "passport_and_sources",
        )

    def test_04_artifact_status_type(self) -> None:
        self.reject(
            lambda c: c["payload"]["material_passport"].update({"artifact_status": 1}),
            "passport_and_sources",
        )

    def test_05_closing_edge(self) -> None:
        self.reject(
            lambda c: c["payload"]["frozen_model"].update({"quadric_Q": "sum_(i=0)^6 x_i*x_(i+1)"}),
            "frozen_model",
        )

    def test_06_averaged_chronology(self) -> None:
        self.reject(
            lambda c: c["payload"]["frozen_model"].update({"chronological_averaging_used": True}),
            "frozen_model",
        )

    def test_07_group_order_type_smuggle(self) -> None:
        self.reject(
            lambda c: c["payload"]["projective_monomial_group"].update({"order": 24.0}),
            "D12_enumeration",
        )

    def test_08_group_phase(self) -> None:
        self.reject(
            lambda c: c["payload"]["projective_monomial_group"]["elements"][3]["rho_phase_exponents"].__setitem__(1, 2),
            "D12_enumeration",
        )

    def test_09_group_table(self) -> None:
        self.reject(
            lambda c: c["payload"]["projective_monomial_group"]["multiplication_table_by_id"][1].__setitem__(2, 1),
            "D12_enumeration",
        )

    def test_10_D12_order_convention(self) -> None:
        self.reject(
            lambda c: c["payload"]["projective_monomial_group"].update({"order_convention": "group of order 12"}),
            "D12_enumeration",
        )

    def test_11_CK_degree(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_chow_kuenneth"].update({"degree_integral_h5": 5}),
            "middle_Chow_Kuenneth",
        )

    def test_12_CK_fraction_type(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_chow_kuenneth"]["Lefschetz_projectors"][0]["coefficient"].update({"denominator": 6.0}),
            "middle_Chow_Kuenneth",
        )

    def test_13_CK_composition(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_chow_kuenneth"]["composition_matrix"][1].__setitem__(1, 0),
            "middle_Chow_Kuenneth",
        )

    def test_14_raw_reynolds_rank_claim(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_chow_kuenneth"].update({"raw_e_G_assigned_middle_rank10": True}),
            "middle_Chow_Kuenneth",
        )

    def test_15_reynolds_pair_count(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_chow_kuenneth"]["independent_correspondence_algebra_controls"]["Reynolds_product_pairs_per_output_group_element"].__setitem__(0, 23),
            "middle_Chow_Kuenneth",
        )

    def test_16_relation_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["relation_construction"].update({"exact_Qrho_relation_rank": 80}),
            "Cayley_Jacobian_structure",
        )

    def test_17_bigrading(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["bigrading"].update({"deg_y": [1, -2]}),
            "Cayley_Jacobian_structure",
        )

    def test_18_delete_orientation_twist(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["residue_action"]["general_scalar_lift_firewall"].update({"net_t_exponent_with_orientation_multiplier": -3}),
            "residue_orientation_and_scalar_lift",
        )

    def test_19_invert_orientation_twist(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["residue_action"]["general_scalar_lift_firewall"].update({"net_t_exponent_if_orientation_inverted": 0}),
            "residue_orientation_and_scalar_lift",
        )

    def test_20_orientation_formula(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["residue_action"].update({"orientation_multiplier": "1"}),
            "residue_orientation_and_scalar_lift",
        )

    def test_21_relation_subspace_invariance(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["quotient_action_certificate"].update({"all_relation_images_reduce_to_zero": False}),
            "quotient_action_well_defined",
        )

    def test_22_representation_law(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["quotient_action_certificate"].update({"ambient_group_law_tests": 94463}),
            "quotient_action_well_defined",
        )

    def test_23_H41_character(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["H41_character"].update({"representation": "sign"}),
            "independent_character_replay",
        )

    def test_24_rotation_trace(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["H32_character"]["rotation_traces_k0_to_k11"].__setitem__(1, 0),
            "independent_character_replay",
        )

    def test_25_trivial_multiplicity(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["H32_character"].update({"trivial_multiplicity": 3}),
            "independent_character_replay",
        )

    def test_26_two_dimensional_multiplicity(self) -> None:
        self.reject(
            lambda c: c["payload"]["cayley_jacobian_representation"]["H32_character"]["two_dimensional_multiplicities"][2].update({"multiplicity": 7}),
            "independent_character_replay",
        )

    def test_27_core_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_realization_decomposition"]["core"].update({"rank": 2}),
            "middle_realization_split",
        )

    def test_28_core_Hodge(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_realization_decomposition"]["core"]["Hodge_summary_high_to_low"].__setitem__(1, 0),
            "middle_realization_split",
        )

    def test_29_level_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_realization_decomposition"]["level_one_complement"].update({"rank": 166}),
            "middle_realization_split",
        )

    def test_30_primewise_projector(self) -> None:
        self.reject(
            lambda c: c["payload"]["middle_realization_decomposition"]["realizations"].update({"primewise_fitted_projector_used": True}),
            "middle_realization_split",
        )

    def test_31_QG_scope(self) -> None:
        self.reject(
            lambda c: c["payload"]["group_algebra_no_go"].update({"algebra": "all Chow correspondences"}),
            "Q_group_algebra_no_go",
        )

    def test_32_QG_minimum_rank(self) -> None:
        self.reject(
            lambda c: c["payload"]["group_algebra_no_go"].update({"minimum_rational_Hodge_rank_containing_extreme_pair_in_QG": 2}),
            "Q_group_algebra_no_go",
        )

    def test_33_all_correspondence_overclaim(self) -> None:
        self.reject(
            lambda c: c["payload"]["group_algebra_no_go"].update({"all_K_rational_algebraic_correspondences": "REFUTED"}),
            "Q_group_algebra_no_go",
        )

    def test_34_decision_rank2(self) -> None:
        self.reject(
            lambda c: c["payload"]["decisions"].update({"rank2_projector_in_full_Chow_ring": "REFUTED"}),
            "decisions",
        )

    def test_35_future_B3(self) -> None:
        self.reject(
            lambda c: c["payload"]["future_gates_C53"].update({"B3_rank10_Frobenius_polynomial": "PROVED"}),
            "C53_future_firewall",
        )

    def test_36_future_local_factor(self) -> None:
        self.reject(
            lambda c: c["payload"]["future_gates_C53"].update({"local_L_polynomial_factorization_claimed": True}),
            "C53_future_firewall",
        )

    def test_37_full_automorphism_overclaim(self) -> None:
        self.reject(
            lambda c: c["payload"]["scope"].update({"full_projective_automorphism_group_classified": True}),
            "scope_firewall",
        )

    def test_38_QG_promoted_to_all(self) -> None:
        self.reject(
            lambda c: c["payload"]["scope"].update({"Q_group_algebra_no_go_promoted_to_all_correspondences": True}),
            "scope_firewall",
        )

    def test_39_RH_overclaim(self) -> None:
        self.reject(
            lambda c: c["payload"]["scope"].update({"Riemann_hypothesis_claimed": True}),
            "scope_firewall",
        )

    def test_40_unknown_top_key(self) -> None:
        self.reject(
            lambda c: c["payload"].update({"unknown": 0}),
            "recursive_exact_schema",
        )

    def test_41_missing_container(self) -> None:
        self.reject(
            lambda c: c["payload"].pop("future_gates_C53"),
            "recursive_exact_schema",
        )

    def test_42_container_type_smuggle(self) -> None:
        self.reject(
            lambda c: c["payload"].update({"middle_chow_kuenneth": []}),
            "recursive_exact_schema",
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

    def test_43_second_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(2)

    def test_44_third_move_failure_rolls_back(self) -> None:
        self.assert_promotion_rollback(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
