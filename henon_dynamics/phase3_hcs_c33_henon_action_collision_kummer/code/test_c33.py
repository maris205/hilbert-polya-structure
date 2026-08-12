#!/usr/bin/env python3
"""Mutation and regression tests for HCS-C33 Phase 3."""

from __future__ import annotations

import copy
import json
import os
import sys
import unittest
import warnings
from pathlib import Path

from sympy.utilities.exceptions import SymPyDeprecationWarning

warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
sys.path.insert(0, str(CODE))

import c33_kummer_checker as checker  # noqa: E402


CERTIFICATE = Path(
    os.environ.get(
        "C33_TEST_CERTIFICATE",
        str(PROJECT / "results" / "c33_kummer_certificate.json"),
    )
).resolve()


class C33Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        cls.base_report = checker.audit_certificate(copy.deepcopy(cls.base))

    @staticmethod
    def rehash(certificate: dict) -> None:
        certificate["payload_sha256"] = checker.sha256_bytes(
            checker.canonical_json(certificate["payload"]).encode("utf-8")
        )

    def assert_rejected(self, mutation, *, rehash: bool = True) -> None:
        certificate = copy.deepcopy(self.base)
        mutation(certificate)
        if rehash:
            self.rehash(certificate)
        try:
            report = checker.audit_certificate(certificate)
        except checker.GateFailure:
            return
        self.assertNotEqual(report["status"], "ERROR")
        self.assertFalse(report["all_pass"])

    def test_01_base_certificate_passes_all_gates(self) -> None:
        self.assertEqual(self.base_report["status"], "PASS")
        self.assertEqual(self.base_report["gate_count"], 12)
        self.assertEqual(self.base_report["passed_gate_count"], 12)

    def test_02_decisive_exact_values(self) -> None:
        payload = self.base["payload"]
        self.assertEqual(
            payload["derived_polynomials"]["action_discriminant_factor_degrees_and_powers"],
            [[1, 60], [2, 5], [5, 3], [9, 2]],
        )
        self.assertEqual(
            payload["hill_kummer_gate"]["field_norm"],
            {"numerator": 1929715196403899883576140608, "denominator": 243},
        )
        self.assertEqual(
            payload["exact_period_and_nonparabolic_gate"]["conclusion"],
            "GENERIC_P9_BRANCHES_HAVE_EXACT_PERIOD_FIVE_AND_NO_MULTIPLIER_PLUS_OR_MINUS_ONE",
        )

    def test_03_stale_payload_digest_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["scope"].__setitem__("no_zeta_claim", False),
            rehash=False,
        )

    def test_04_bool_integer_type_confusion_rejected(self) -> None:
        self.assert_rejected(lambda cert: cert["payload"]["material_passport"].__setitem__("ai_assistance_disclosed", 1))

    def test_05_source_drift_rejected(self) -> None:
        key = next(iter(self.base["payload"]["source_lock"]))
        self.assert_rejected(lambda cert: cert["payload"]["source_lock"].__setitem__(key, "0" * 64))

    def test_06_marker_mutation_rejected(self) -> None:
        def mutate(cert):
            cert["payload"]["derived_polynomials"]["exact_period_five_marker_G"]["terms"][0]["numerator"] += 1
        self.assert_rejected(mutate)

    def test_07_action_curve_mutation_rejected(self) -> None:
        def mutate(cert):
            cert["payload"]["derived_polynomials"]["action_curve_W"]["terms"][-1]["numerator"] += 1
        self.assert_rejected(mutate)

    def test_08_discriminant_exponent_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["derived_polynomials"].__setitem__(
                "action_discriminant_factor_degrees_and_powers", [[1, 60], [2, 5], [5, 3], [9, 1]]
            )
        )

    def test_09_galois_cycle_type_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["collision_parameter_galois_gate"]["modular_factorizations"][1].__setitem__(
                "factor_degrees", [5, 2, True, True]
            )
        )

    def test_10_collision_value_mutation_rejected(self) -> None:
        def mutate(cert):
            cert["payload"]["node_gate"]["double_action_value_c0"]["numerators_low_to_high"][0] += 1
        self.assert_rejected(mutate)

    def test_09b_duplicate_galois_prime_row_rejected(self) -> None:
        def mutate(cert):
            rows = cert["payload"]["collision_parameter_galois_gate"]["modular_factorizations"]
            rows[1] = copy.deepcopy(rows[0])
        self.assert_rejected(mutate)

    def test_11_branch_pair_mutation_rejected(self) -> None:
        def mutate(cert):
            cert["payload"]["node_gate"]["branch_pair_polynomial"]["coefficients_low_to_high"][1]["numerators_low_to_high"][2] += 1
        self.assert_rejected(mutate)

    def test_12_tangent_certificate_mutation_rejected(self) -> None:
        def mutate(cert):
            cert["payload"]["node_gate"]["tangent_cone_discriminant_WAc_squared_minus_WAA_Wcc"]["numerators_low_to_high"][0] += 1
        self.assert_rejected(mutate)

    def test_13_minus_one_gate_omission_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["exact_period_and_nonparabolic_gate"].__setitem__(
                "P9_coprime_to_multiplier_minus_one_resultant", False
            )
        )

    def test_14_normalization_slope_mutation_rejected(self) -> None:
        def mutate(cert):
            cert["payload"]["node_gate"]["normalization_branch_slope"]["linear_q"]["numerators_low_to_high"][0] += 1
        self.assert_rejected(mutate)

    def test_15_field_norm_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["hill_kummer_gate"]["field_norm"].__setitem__(
                "numerator", 1929715196403899883576140609
            )
        )

    def test_16_finite_nonsquare_control_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["finite_prime_controls"]["rows"][2].__setitem__(
                "hill_product_character", 1
            )
        )

    def test_17_post_hoc_disclosure_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["finite_prime_controls"]["rows"][0].__setitem__(
                "selection_status", "PREDICTION"
            )
        )

    def test_18_route_a_upgrade_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["route_a_evaluation"].__setitem__(
                "overall", "ROUTE_A_STRONG_CANDIDATE"
            )
        )

    def test_19_zeta_scope_firewall_rejected(self) -> None:
        self.assert_rejected(lambda cert: cert["payload"]["scope"].__setitem__("no_zeta_claim", False))

    def test_20_unknown_nested_key_rejected(self) -> None:
        self.assert_rejected(lambda cert: cert["payload"]["scope"].__setitem__("silent_extra", True))

    def test_21_generic_irreducibility_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["derived_polynomials"][
                "generic_irreducibility_certificate"
            ]["rows"][0].__setitem__("factor_degrees", [3, 3])
        )

    def test_22_square_class_descent_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["hill_kummer_gate"].__setitem__(
                "square_class_identity", "[h1/h2]=1"
            )
        )

    def test_23_finite_least_period_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["finite_prime_controls"]["rows"][1][
                "branches"
            ][0].__setitem__("least_state_period", 1)
        )

    def test_24_finite_minus_one_boolean_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["finite_prime_controls"]["rows"][3].__setitem__(
                "multiplier_minus_one_excluded", False
            )
        )

    def test_25_convention_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["conventions"].__setitem__(
                "chronological_recurrence", "averaged transition matrix"
            )
        )

    def test_26_inverse_formula_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["derived_polynomials"][
                "normalization_birational_inverse"
            ].__setitem__("inverse_formula", "q=V/U")
        )

    def test_27_collision_field_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["node_gate"].__setitem__(
                "collision_field", "QQ"
            )
        )

    def test_28_node_nonzero_unknown_key_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["node_gate"]["nonzero_gates"].__setitem__(
                "unchecked", True
            )
        )

    def test_29_chronology_string_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["exact_period_and_nonparabolic_gate"].__setitem__(
                "chronology", "earlier factors on the left"
            )
        )

    def test_30_slope_formula_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["node_gate"][
                "normalization_branch_slope"
            ].__setitem__("formula", "post-hoc slope")
        )

    def test_31_finite_selection_rule_mutation_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["finite_prime_controls"].__setitem__(
                "selection_rule", "chosen after observing desired characters"
            )
        )

    def test_32_irreducibility_float_integer_confusion_rejected(self) -> None:
        self.assert_rejected(
            lambda cert: cert["payload"]["derived_polynomials"][
                "generic_irreducibility_certificate"
            ].__setitem__("parameter_value", 6.0)
        )


if __name__ == "__main__":
    unittest.main()
