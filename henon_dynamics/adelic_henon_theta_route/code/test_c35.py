from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


producer = load("c35_producer", CODE / "c35_adelic_theta_producer.py")
checker = load("c35_checker", CODE / "c35_adelic_theta_checker.py")


def rehash(certificate):
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()


class C35Tests(unittest.TestCase):
    def setUp(self):
        self.certificate = producer.build_certificate()

    def assert_rejected(self, mutate):
        candidate = copy.deepcopy(self.certificate)
        mutate(candidate)
        rehash(candidate)
        statuses = [row["status"] for row in checker.audit(candidate)]
        self.assertIn("FAIL", statuses)

    def test_01_base_certificate_passes(self):
        self.assertTrue(all(row["status"] == "PASS" for row in checker.audit(self.certificate)))

    def test_02_producer_is_deterministic(self):
        self.assertEqual(
            json.dumps(self.certificate, sort_keys=True),
            json.dumps(producer.build_certificate(), sort_keys=True),
        )

    def test_03_fractional_part_examples(self):
        self.assertEqual(producer.padic_fractional_part(producer.Fraction(1, 6), 2), producer.Fraction(1, 2))
        self.assertEqual(producer.padic_fractional_part(producer.Fraction(1, 6), 3), producer.Fraction(2, 3))
        self.assertEqual(producer.global_character_exponent(producer.Fraction(1, 6)), 1)

    def test_04_henon_map_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["object"].__setitem__("jacobian_determinant", -1))

    def test_04b_source_hash_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"]["area_preserving_henon_model"].__setitem__(
                "sha256", "0" * 64
            )
        )

    def test_05_phase_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["exact_additive_character_gate"]["records"][11].__setitem__("phase_value", "0")
        )

    def test_06_bool_integer_confusion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["object"].__setitem__("jacobian_determinant", True))

    def test_07_gauge_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["constant_gauge_gate"].__setitem__("verdict", "LOCAL_PHASE_ROTATES")
        )

    def test_08_vacuum_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["finite_spherical_vacuum_gate"]["rows"][3].__setitem__("vacuum_verdict", "UNKNOWN")
        )

    def test_09_theta_mutation_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["theta_gate"].__setitem__("status", "HEURISTIC"))

    def test_10_range_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["boundary_space_gate"].__setitem__("range_identity", "E_x U_H(SH) subset E_x(S0)")
        )

    def test_11_zero_accumulation_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["raw_finite_quantum_product_kill"]["rows"][0].__setitem__("guaranteed_nearby_zero_count", 1)
        )

    def test_12_route_b_promotion_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["route_a"].__setitem__("route_b_invocation_allowed", True))

    def test_13_henon_essentiality_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].__setitem__("henon_vacuum_essentiality", "PROVED")
        )

    def test_14_unknown_scope_false_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].__setitem__("no_rh_proof", False))

    def test_15_cubic_sum_recurrence_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_dilation_tower_gate"]["rows"][9].__setitem__(
                "exponential_sum", 0
            )
        )

    def test_16_noncompactness_witness_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_dilation_tower_gate"]["rows"][-1].__setitem__(
                "defect_norm_squared", "0"
            )
        )

    def test_17_finite_channel_rank_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["fixed_domain_relative_range_gate"].__setitem__(
                "conditional_projection_difference_rank_bound", 3
            )
        )

    def test_18_route_a_coordinatewise_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].__setitem__(
                "overall", "ROUTE_A_SUCCESS"
            )
        )

    def test_19_unknown_payload_key_rejected(self):
        self.assert_rejected(lambda c: c["payload"].__setitem__("unverified_claim", True))

    def test_20_direct_cyclotomic_control_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_dilation_tower_gate"][
                "direct_cyclotomic_controls"
            ][0].__setitem__("target_integer", 1)
        )

    def test_21_scope_unknown_key_rejected(self):
        self.assert_rejected(lambda c: c["payload"]["scope"].__setitem__("rh_proved", True))

    def test_22_decision_unknown_key_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].__setitem__("route_a_success", "PROVED")
        )

    def test_23_composite_vacuum_prime_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["finite_spherical_vacuum_gate"]["rows"][4].__setitem__(
                "prime", 49
            )
        )

    def test_24_raw_bound_text_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["raw_finite_quantum_product_kill"]["rows"][0].__setitem__(
                "distance_bound", "nonsense"
            )
        )

    def test_25_tower_unknown_key_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["local_dilation_tower_gate"]["rows"][0].__setitem__(
                "rh_proved", True
            )
        )

    def test_26_scaling_site_erasure_rejected(self):
        self.assert_rejected(lambda c: c["payload"].__setitem__("scaling_site_gate", {}))

    def test_27_boundary_standard_mutation_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["boundary_space_gate"].__setitem__("standard", "anything")
        )

    def test_28_dynamic_two_channel_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scaling_covariance_gate"].__setitem__(
                "static_rank_two_implies_dynamic_two_channel", True
            )
        )

    def test_29_poisson_defect_determinant_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["poisson_boundary_defect_gate"].__setitem__(
                "determinant_class", "PROVED"
            )
        )

    def test_30_poisson_boundary_mode_operator_overclaim_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["poisson_boundary_defect_gate"].__setitem__(
                "bounded_finite_rank_operator", "PROVED"
            )
        )


if __name__ == "__main__":
    unittest.main()
