#!/usr/bin/env python3
"""Independent tests for the P28 Round-7 non-arithmetic source package."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import sys
import unittest

import mpmath as mp


MODULE_PATH = Path(__file__).with_name("build_round7_nonarithmetic_control_gate.py")
SPEC = importlib.util.spec_from_file_location("p28_round7_control", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round7_nonarithmetic_control_gate.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class NonArithmeticControlSourcePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = MODULE.source_rows()
        cls.preflight = MODULE.source_package_preflight(cls.sources)
        cls.geometry = MODULE.build_geometry()
        cls.matrices = MODULE.matrices_artifact(cls.geometry, cls.preflight)
        cls.gate = MODULE.gate_artifact(cls.geometry, cls.preflight)
        cls.validation = MODULE.validate(
            cls.sources, cls.geometry, cls.matrices, cls.gate
        )

    def test_01_freeze_is_digest_bound(self) -> None:
        self.assertEqual(
            MODULE.sha256_file(MODULE.FREEZE_PATH),
            MODULE.EXPECTED_FREEZE_SHA256,
        )

    def test_02_source_matrix_has_four_unique_included_sources(self) -> None:
        self.assertEqual(len(self.sources), 4)
        self.assertEqual(len({row["source_id"] for row in self.sources}), 4)
        self.assertEqual(
            {row["access_date"] for row in self.sources}, {"2026-08-28"}
        )
        self.assertTrue(
            all(row["inclusion"].startswith("INCLUDED") for row in self.sources)
        )

    def test_03_nazarenko_primary_source_is_version_and_hash_locked(self) -> None:
        source = self.sources[0]
        self.assertEqual(source["source_id"], "S1-NAZARENKO-2013")
        self.assertEqual(source["doi_or_identifier"], "arXiv:1301.5446v1")
        self.assertEqual(
            source["content_sha256"],
            MODULE.REMOTE_SOURCE_SHA256["nazarenko_arxiv_source_tar_v1"],
        )
        self.assertIn("Equations (10)-(16)", source["claim_support"])
        self.assertIn("Does not classify", source["claim_boundary"])

    def test_04_peer_reviewed_family_source_is_metadata_bounded(self) -> None:
        source = self.sources[1]
        self.assertEqual(source["doi_or_identifier"], "10.1063/1.1850177")
        self.assertEqual(source["peer_review_status"], "REVIEWED_EPFL_METADATA")
        self.assertEqual(source["original_content_accessed"], "NO_METADATA_ONLY")
        self.assertIn("sourced to S1", source["claim_boundary"])

    def test_05_takeuchi_source_and_theorem_are_publisher_locked(self) -> None:
        source = self.sources[2]
        self.assertEqual(source["doi_or_identifier"], "10.2969/jmsj/02740600")
        self.assertEqual(
            source["content_sha256"],
            MODULE.REMOTE_SOURCE_SHA256["takeuchi_jstage_pdf"],
        )
        self.assertIn("Theorem 1", source["claim_support"])

    def test_06_lindemann_weierstrass_input_is_published_and_source_locked(self) -> None:
        source = self.sources[3]
        self.assertEqual(source["source_id"], "S4-POPESCU-2024")
        self.assertEqual(
            source["doi_or_identifier"], "10.1007/978-3-031-51959-8_16"
        )
        self.assertEqual(
            source["content_sha256"],
            MODULE.REMOTE_SOURCE_SHA256["popescu_arxiv_source_gzip_v2"],
        )
        self.assertEqual(
            source["peer_review_status"],
            "REVIEW_STATUS_NOT_INDEPENDENTLY_CONFIRMED",
        )
        self.assertIn("Corollary 3.2", source["claim_support"])

    def test_07_no_source_has_predatory_or_hidden_conflict_clearances(self) -> None:
        for source in self.sources:
            self.assertTrue(source["predatory_venue_alert"].startswith("NONE"))
            self.assertNotEqual(source["conflict_of_interest_assessment"], "NOT_CHECKED")

    def test_08_exact_parameter_specialization_is_admissible(self) -> None:
        self.assertGreater(self.geometry["a"], 1 / mp.sqrt(2))
        self.assertLess(self.geometry["a"], 1)
        self.assertGreater(self.geometry["b"], 0)
        self.assertLess(self.geometry["b"], 1)
        self.assertEqual(self.geometry["alpha_tilde"], 0)
        self.assertEqual(self.matrices["definition"]["parameter_a"], "exp(-1/10)")

    def test_09_all_four_matrices_have_determinant_one(self) -> None:
        self.assertEqual(len(self.geometry["generators"]), 4)
        for generator in self.geometry["generators"]:
            self.assertLess(abs(mp.det(generator) - 1), mp.mpf("1e-120"))

    def test_10_all_four_matrices_replay_su11_structure(self) -> None:
        for residual in self.geometry["su11_residuals"]:
            self.assertLess(residual, mp.mpf("1e-120"))

    def test_11_all_four_source_generators_are_hyperbolic(self) -> None:
        for generator in self.geometry["generators"]:
            self.assertGreater(abs(generator[0, 0] + generator[1, 1]), 2)
        self.assertTrue(
            self.matrices["replay"]["all_generators_hyperbolic"]
        )

    def test_12_published_polygon_relator_replays(self) -> None:
        self.assertLess(self.geometry["relation_residual"], mp.mpf("1e-120"))
        self.assertLess(
            mp.mpf(self.matrices["replay"]["relator_max_entry_residual"]),
            mp.mpf("1e-120"),
        )

    def test_13_octagon_angle_sum_is_exactly_two_pi_by_formula(self) -> None:
        self.assertEqual(
            4 * self.geometry["beta"]
            + 4 * (mp.pi / 2 - self.geometry["beta"]),
            2 * mp.pi,
        )
        self.assertLess(
            abs(self.geometry["angle_sum"] - 2 * mp.pi), mp.mpf("1e-130")
        )

    def test_14_trace_square_identity_replays(self) -> None:
        self.assertLess(
            abs(
                self.geometry["common_trace"] ** 2
                - self.geometry["trace_square_formula"]
            ),
            mp.mpf("1e-130"),
        )

    def test_15_nonarithmetic_witness_is_exactly_the_frozen_one(self) -> None:
        witness = self.gate["requirements"][
            "independent_nonarithmeticity_certificate"
        ]["witness"]
        self.assertEqual(witness["x"], "exp(-1/5)")
        self.assertEqual(
            witness["trace_square"], "4x/((1-x)(2x-1))"
        )
        self.assertEqual(
            witness["square_subgroup_trace"], "tr(g0^2)=trace_square-2"
        )
        self.assertEqual(
            witness["contradiction_polynomial"],
            "-2*t2*x^2+(3*t2-4)*x-t2",
        )
        self.assertEqual(
            witness["takeuchi_application_owner"],
            "FINITE_COVOLUME_GAMMA_SQUARE_SUBGROUP",
        )
        self.assertIn(
            "finitely generated elementary abelian 2-group",
            witness["square_subgroup_finite_index_reason"],
        )
        self.assertIn("commensurability", witness["arithmeticity_transfer"])
        self.assertEqual(
            witness["real_model_bridge"],
            "Cayley-conjugate SU(1,1) to SL(2,R)",
        )
        self.assertIn("Takeuchi", self.gate["requirements"][
            "independent_nonarithmeticity_certificate"
        ]["evidence"])
        self.assertIn("square subgroup", self.gate["requirements"][
            "independent_nonarithmeticity_certificate"
        ]["evidence"])

    def test_16_four_generators_have_primitive_abelianization_classes(self) -> None:
        requirement = self.gate["requirements"][
            "rigorous_systole_or_per_owner_primitivity_certificate"
        ]
        owners = requirement["owners"]
        self.assertEqual(len(owners), 4)
        vectors = []
        for index, owner in enumerate(owners):
            expected = [1 if component == index else 0 for component in range(4)]
            self.assertEqual(owner["abelianization"], expected)
            vectors.append(owner["abelianization"])
            self.assertEqual(
                owner["certificate"],
                "NOT_A_PROPER_POWER_BY_PRIMITIVE_Z4_CLASS",
            )
        for left_index, left in enumerate(vectors):
            for right in vectors[left_index + 1:]:
                self.assertNotEqual(left, right)
                self.assertNotEqual(left, [-entry for entry in right])
        self.assertTrue(requirement["pairwise_unoriented_owner_distinct"])
        self.assertEqual(
            requirement["owner_distinctness_certificate"],
            "E_I_NOT_EQUAL_TO_PLUS_OR_MINUS_E_J_IN_Z4_FOR_I_NOT_EQUAL_J",
        )
        self.assertFalse(requirement["systole_claimed"])

    def test_17_every_source_package_requirement_passes(self) -> None:
        self.assertEqual(tuple(self.gate["requirements"]), MODULE.REQUIREMENT_NAMES)
        self.assertEqual(
            {row["status"] for row in self.gate["requirements"].values()},
            {"PASS"},
        )
        self.assertEqual(self.gate["requirements_satisfied"], 6)
        self.assertEqual(self.gate["requirements_total"], 6)
        self.assertEqual(self.gate["status"], "PASS_READY_6_OF_6")

    def test_18_geometry_is_selected_only_after_six_of_six(self) -> None:
        self.assertEqual(self.preflight["status"], "PASS_READY_6_OF_6")
        self.assertEqual(self.preflight["requirements_satisfied"], 6)
        self.assertTrue(self.preflight["pre_geometry_authorization"])
        self.assertFalse(self.preflight["geometry_selected"])
        self.assertFalse(self.preflight["matrices_loaded"])
        failed_preflight = MODULE.source_package_preflight([])
        self.assertEqual(failed_preflight["status"], "FAIL_CLOSED_NOT_READY")
        self.assertFalse(failed_preflight["pre_geometry_authorization"])
        self.assertEqual(self.gate["requirements_satisfied"], 6)
        for field in (
            "source_package_supplied",
            "geometry_selected",
            "matrices_loaded",
            "nonarithmeticity_verified",
            "per_owner_primitivity_verified",
            "control_instantiation_authorized",
        ):
            self.assertIs(self.gate[field], True, field)

    def test_19_no_systole_cutoff_census_or_comparison_is_claimed(self) -> None:
        self.assertFalse(self.gate["systole_verified"])
        for field in MODULE.FORBIDDEN_TRUE_FIELDS:
            self.assertIs(self.gate["execution"][field], False, field)

    def test_20_route_and_target_firewalls_remain_closed(self) -> None:
        self.assertEqual(
            self.gate["formal_full_candidate_route_a_tuple"], "UNASSIGNED"
        )
        self.assertEqual(self.gate["bounded_proxy_overall"], "ROUTE_A_EXPLORATORY")
        self.assertFalse(self.validation["target_data_used"])
        self.assertFalse(self.validation["arithmetic_labels_assigned"])
        self.assertEqual(self.validation["a2_evaluation"], "NOT_RUN")
        self.assertEqual(self.validation["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(self.validation["route_b_invocation_allowed"])

    def test_21_mutated_failed_requirement_fails_validation(self) -> None:
        for requirement_name in MODULE.REQUIREMENT_NAMES:
            mutated = copy.deepcopy(self.gate)
            mutated["requirements"][requirement_name]["status"] = "FAIL"
            mutated["requirements_satisfied"] = 5
            mutated["status"] = "FAIL_CLOSED_NOT_READY"
            validation = MODULE.validate(
                self.sources, self.geometry, self.matrices, mutated
            )
            self.assertEqual(validation["status"], "FAIL", requirement_name)
            self.assertTrue(validation["errors"], requirement_name)

    def test_22_validation_passes_without_errors(self) -> None:
        self.assertEqual(self.validation["status"], "PASS")
        self.assertEqual(self.validation["errors"], [])
        self.assertEqual(self.validation["source_package_gate"], "PASS_READY_6_OF_6")
        self.assertEqual(self.validation["primitive_owner_count"], 4)
        self.assertFalse(self.validation["comparison_run"])


if __name__ == "__main__":
    unittest.main()
