#!/usr/bin/env python3
"""Regression and mutation tests for the HCS-C26 exact release."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c26_certificate.json"
INDEPENDENT = PROJECT / "results" / "c26_independent_check.json"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(specification)
    assert specification.loader is not None
    specification.loader.exec_module(module)
    return module


producer = load_module("c26_release_producer", PROJECT / "code" / "c26_producer.py")
checker = load_module("c26_release_checker", PROJECT / "code" / "c26_independent_check.py")


def fraction_from_record(record: dict[str, str]) -> Fraction:
    result = Fraction(int(record["numerator"]), int(record["denominator"]))
    expected = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
    if record["exact"] != expected:
        raise AssertionError("invalid rational record")
    return result


class C26Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        cls.states, cls.edges = producer.build_graph()
        cls.branch = cls.data["source_locked_branch"]
        cls.point = cls.data["projective_point_witness"]
        cls.theorem = cls.data["point_evaluation_slice_theorem"]
        _, cls.b_matrix, cls.tokens = producer.follow_word(4, producer.GAMMA_STAR, cls.edges)
        cls.r_matrix = producer.transpose(cls.b_matrix)
        cls.x0 = tuple(fraction_from_record(value) for value in cls.point["x0"])
        cls.scale = fraction_from_record(cls.point["S_gamma_star_at_x0"])

    def test_literal_graph_state_and_source_word(self) -> None:
        self.assertEqual(len(self.states), 7)
        self.assertEqual(len(self.edges), 14)
        self.assertEqual(self.states.index(producer.INITIAL), 2)
        self.assertEqual(self.states.index(producer.AGY_BASE), 4)
        self.assertEqual(self.branch["base_state"], 4)
        self.assertEqual(self.branch["gamma_star_word"], "t" * 64 + "tbttbtbb" * 8)
        self.assertEqual(self.branch["gamma_star_length"], 128)
        self.assertTrue(self.branch["closed"])

    def test_later_left_chronology_mutation_is_rejected(self) -> None:
        wrong = producer.IDENTITY
        for token in self.tokens:
            edge = self.edges[(int(token["source"]), str(token["type"]))]
            wrong = producer.matmul(wrong, edge["matrix"])
        self.assertNotEqual(wrong, self.b_matrix)
        self.assertNotEqual(producer.matrix_json(wrong), self.branch["chronological_matrix_B"])
        with self.assertRaises(ValueError):
            producer.decode_finite_witness(4, producer.transpose(wrong), self.edges)

    def test_B_and_R_transpose_mutation_changes_projective_data(self) -> None:
        self.assertNotEqual(self.b_matrix, self.r_matrix)
        self.assertEqual(producer.matrix_json(self.r_matrix), self.branch["length_matrix_R_equals_B_transpose"])
        wrong_scale = producer.normalizer(self.b_matrix, self.x0)
        self.assertNotEqual(wrong_scale, self.scale)

    def test_dimension_four_jacobian_exponent_is_not_mutable(self) -> None:
        jacobian = fraction_from_record(self.point["J_gamma_star_at_x0"])
        self.assertEqual(jacobian, self.scale ** -4)
        self.assertEqual(jacobian, producer.direct_projective_jacobian(self.r_matrix, self.x0))
        self.assertNotEqual(jacobian, self.scale ** -3)
        self.assertNotEqual(jacobian, self.scale ** -5)

    def test_word_and_base_mutations_do_not_reproduce_the_witness(self) -> None:
        mutated_word = "b" + producer.GAMMA_STAR[1:]
        mutated_end, mutated_matrix, _ = producer.follow_word(4, mutated_word, self.edges)
        self.assertTrue(mutated_end != 4 or mutated_matrix != self.b_matrix)
        wrong_base_end, wrong_base_matrix, _ = producer.follow_word(2, producer.GAMMA_STAR, self.edges)
        self.assertTrue(wrong_base_end != 2 or wrong_base_matrix != self.b_matrix)
        self.assertNotEqual(producer.ETA, producer.GAMMA_STAR)

    def test_x0_and_normalizer_are_not_barycenter_substitutions(self) -> None:
        raw = tuple(sum(self.r_matrix[row]) for row in range(4))
        expected_x0, expected_normalization = producer.normalize_integer_vector(raw)
        self.assertEqual(self.x0, expected_x0)
        self.assertEqual(self.point["x0_normalization"], expected_normalization)
        self.assertEqual(producer.normalizer(self.r_matrix, self.x0), self.scale)
        barycenter = (Fraction(1, 4),) * 4
        self.assertNotEqual(barycenter, self.x0)
        self.assertNotEqual(producer.normalizer(self.r_matrix, barycenter), self.scale)
        wrong_coefficients = [sum(self.r_matrix[row]) for row in range(4)]
        self.assertNotEqual(wrong_coefficients, self.point["normalizer_coefficients"])

    def test_sigma_zero_and_one_exact_single_branch_floors(self) -> None:
        sigma_zero = fraction_from_record(self.theorem["exact_registered_sigmas"]["0"]["coefficient_magnitude"])
        sigma_one = fraction_from_record(self.theorem["exact_registered_sigmas"]["1"]["coefficient_magnitude"])
        self.assertEqual(sigma_zero, self.scale ** -4)
        self.assertEqual(sigma_one, self.scale ** -5)
        self.assertEqual(sigma_one, sigma_zero / self.scale)
        self.assertGreater(sigma_zero, 0)
        self.assertGreater(sigma_one, 0)
        self.assertTrue(self.theorem["parameter_domain"]["magnitude_independent_of_t"])

    def test_positive_prefix_complex_cone_quantities_are_exact(self) -> None:
        gate = self.data["common_complex_domain_gate"]
        self.assertEqual(gate["fixed_positive_prefix"]["matrix_P"], producer.matrix_json(self.r_matrix))
        self.assertTrue(gate["fixed_positive_prefix"]["entrywise_strictly_positive"])
        delta = fraction_from_record(gate["normalized_column_hull_K"]["coordinate_margin_delta"])
        theta = fraction_from_record(gate["birkhoff_projective_contraction"]["theta"])
        self.assertEqual(delta, Fraction(14783, 1642663))
        self.assertEqual(theta, Fraction(12206150825, 12121793906))
        self.assertEqual(gate["complex_projective_metadata"]["normalized_complex_projective_dimension"], 3)
        self.assertEqual(gate["complex_projective_metadata"]["projective_jacobian_exponent"], 4)
        self.assertFalse(gate["theorem_basis"]["numerical_sampling_used_as_proof"])
        self.assertFalse(gate["theorem_basis"]["finite_branch_cutoff_used_as_proof"])

    def test_positive_prefix_transpose_and_zero_entry_mutations_are_rejected(self) -> None:
        correct_gate = self.data["common_complex_domain_gate"]
        correct_ok, _ = checker.independent_complex_cone_gate(self.r_matrix, correct_gate)
        self.assertTrue(correct_ok)
        transpose_mutation = copy.deepcopy(correct_gate)
        transpose_mutation["fixed_positive_prefix"]["matrix_P"] = producer.matrix_json(self.b_matrix)
        mutated_ok, _ = checker.independent_complex_cone_gate(self.r_matrix, transpose_mutation)
        self.assertFalse(mutated_ok)
        zero_prefix = [list(row) for row in self.r_matrix]
        zero_prefix[0][0] = 0
        with self.assertRaises(ValueError):
            producer.positive_prefix_complex_cone_gate(tuple(tuple(row) for row in zero_prefix))

    def test_complex_dimension_and_principal_log_mutations_are_rejected(self) -> None:
        gate = self.data["common_complex_domain_gate"]
        dimension_mutation = copy.deepcopy(gate)
        dimension_mutation["complex_projective_metadata"]["normalized_complex_projective_dimension"] = 4
        dimension_ok, _ = checker.independent_complex_cone_gate(self.r_matrix, dimension_mutation)
        self.assertFalse(dimension_ok)
        exponent_mutation = copy.deepcopy(gate)
        exponent_mutation["complex_projective_metadata"]["projective_jacobian_exponent"] = 3
        exponent_ok, _ = checker.independent_complex_cone_gate(self.r_matrix, exponent_mutation)
        self.assertFalse(exponent_ok)
        log_mutation = copy.deepcopy(gate)
        log_mutation["principal_log_metadata"]["log_branch"] = "branchwise fitted logarithm"
        log_ok, _ = checker.independent_complex_cone_gate(self.r_matrix, log_mutation)
        self.assertFalse(log_ok)
        sampling_scope = copy.deepcopy(self.data["scope_firewall"])
        sampling_scope["flags"]["common_complex_domain_claimed_from_numerical_sampling"] = True
        self.assertFalse(producer.scope_firewall_valid(sampling_scope))

    def test_scalar_periodic_trace_characteristic_simplification(self) -> None:
        gate = self.data["scalar_periodic_trace_gate"]
        theorem = gate["theorem_basis"]
        self.assertEqual(theorem["weight_telescope"], "product of branch weights around the periodic word = lambda^(-(4+s))")
        self.assertEqual(theorem["projective_denominator"], "det_C(I-Dp_A)=chi_A'(lambda)/lambda^3")
        self.assertEqual(
            theorem["trace_atom_simplification"],
            "lambda^(-(4+s))/(chi_A'(lambda)/lambda^3)=lambda^(-(s+1))/chi_A'(lambda)",
        )
        self.assertFalse(theorem["general_identity_inferred_from_finite_examples"])
        examples = gate["examples"]
        self.assertEqual([row["return_count"] for row in examples], [1, 2, 3])
        self.assertEqual(examples[0]["characteristic_polynomial_coefficients_descending"], [1, -1675423, 463448097, -1675423, 1])
        self.assertEqual(examples[1]["elementary_length"], 391)
        self.assertEqual(examples[2]["elementary_length"], 650)
        self.assertTrue(
            gate["chronological_two_return_witness"]["characteristic_polynomial_is_cyclically_invariant"]
        )
        spectral = gate["three_return_spectral_chronology_witness"]
        self.assertTrue(spectral["noncyclic_reversal_changes_characteristic_polynomial"])
        self.assertNotEqual(
            spectral["forward_characteristic_polynomial_coefficients_descending"],
            spectral["reversed_characteristic_polynomial_coefficients_descending"],
        )

    def test_genuine_two_return_order_mutation_is_rejected(self) -> None:
        gate = self.data["scalar_periodic_trace_gate"]
        valid, _ = checker.independent_periodic_trace_gate(4, self.b_matrix, self.edges, gate)
        self.assertTrue(valid)
        mutated = copy.deepcopy(gate)
        witness = mutated["chronological_two_return_witness"]
        witness["two_return_chronological_matrix_B"] = witness["reversed_order_matrix_B"]
        mutated_ok, _ = checker.independent_periodic_trace_gate(4, self.b_matrix, self.edges, mutated)
        self.assertFalse(mutated_ok)

    def test_three_return_spectral_chronology_mutation_is_rejected(self) -> None:
        gate = copy.deepcopy(self.data["scalar_periodic_trace_gate"])
        spectral = gate["three_return_spectral_chronology_witness"]
        spectral["reversed_characteristic_polynomial_coefficients_descending"] = spectral[
            "forward_characteristic_polynomial_coefficients_descending"
        ]
        valid, _ = checker.independent_periodic_trace_gate(4, self.b_matrix, self.edges, gate)
        self.assertFalse(valid)

    def test_uncancelled_s_plus_four_trace_atom_mutation_is_rejected(self) -> None:
        gate = copy.deepcopy(self.data["scalar_periodic_trace_gate"])
        gate["theorem_basis"]["trace_atom_simplification"] = "lambda^(-(s+4))/chi_A'(lambda)"
        valid, _ = checker.independent_periodic_trace_gate(4, self.b_matrix, self.edges, gate)
        self.assertFalse(valid)

    def test_constant_embedding_assumption_cannot_be_dropped(self) -> None:
        self.assertTrue(producer.slice_schema_valid(self.theorem))
        mutated = copy.deepcopy(self.theorem)
        mutated["hypotheses"] = [row for row in mutated["hypotheses"] if row["id"] != "H2_BOUNDED_CONSTANT_EMBEDDING"]
        self.assertFalse(producer.slice_schema_valid(mutated))
        mutated = copy.deepcopy(self.theorem)
        for row in mutated["hypotheses"]:
            if row["id"] == "H2_BOUNDED_CONSTANT_EMBEDDING":
                row["required"] = False
        self.assertFalse(producer.slice_schema_valid(mutated))

    def test_point_evaluation_assumption_cannot_be_dropped(self) -> None:
        mutated = copy.deepcopy(self.theorem)
        mutated["hypotheses"] = [row for row in mutated["hypotheses"] if row["id"] != "H3_BOUNDED_POINT_EVALUATION"]
        self.assertFalse(producer.slice_schema_valid(mutated))
        mutated = copy.deepcopy(self.theorem)
        for row in mutated["hypotheses"]:
            if row["id"] == "H3_BOUNDED_POINT_EVALUATION":
                row["status"] = "VERIFIED_HERE"
        self.assertFalse(producer.slice_schema_valid(mutated))

    def test_external_C24_and_C25_dependencies_are_not_reproved(self) -> None:
        by_id = {row["id"]: row for row in self.theorem["hypotheses"]}
        self.assertEqual(by_id["H5_PROJECTED_BRANCH_INJECTIVITY"]["status"], "EXTERNAL_C25_THEOREM_NOT_REPROVED")
        self.assertEqual(by_id["H7_DISCRETE_ATOM_ESSENTIAL_NORM"]["status"], "EXTERNAL_C24_THEOREM_NOT_REPROVED")
        self.assertFalse(self.theorem["external_theorems_reproved_here"])
        flags = self.data["scope_firewall"]["flags"]
        self.assertFalse(flags["c24_atomic_theorem_reproved"])
        self.assertFalse(flags["c25_all_length_decoder_reproved"])

    def test_finite_cutoff_cannot_be_promoted_to_proof(self) -> None:
        sentinel = self.data["finite_decoder_sentinel"]
        self.assertEqual(sentinel["max_elementary_length"], 20)
        self.assertEqual(sentinel["total_first_returns"], 13528)
        self.assertEqual(sentinel["distinct_chronological_matrices"], 13528)
        self.assertEqual(sentinel["collision_count"], 0)
        self.assertFalse(sentinel["finite_enumeration_is_proof"])
        self.assertFalse(sentinel["finite_enumeration_is_branch_completeness_claim"])
        self.assertFalse(sentinel["all_length_decoder_dependency_replaced"])
        mutated_scope = copy.deepcopy(self.data["scope_firewall"])
        mutated_scope["flags"]["finite_sentinel_is_proof"] = True
        self.assertFalse(producer.scope_firewall_valid(mutated_scope))

    def test_matrix_collision_requires_signed_aggregation(self) -> None:
        coefficient = fraction_from_record(self.theorem["exact_registered_sigmas"]["0"]["coefficient_magnitude"])
        cancelling = producer.signed_aggregate(((1, coefficient), (-1, coefficient)))
        self.assertEqual(cancelling, 0)
        self.assertGreater(2 * coefficient**2, 0)
        by_id = {row["id"]: row for row in self.theorem["hypotheses"]}
        self.assertTrue(by_id["H5_PROJECTED_BRANCH_INJECTIVITY"]["required"])

    def test_central_sign_and_chronology_averaging_mutations_are_rejected(self) -> None:
        self.assertTrue(producer.scope_firewall_valid(self.data["scope_firewall"]))
        central_mutation = copy.deepcopy(self.data["scope_firewall"])
        central_mutation["flags"]["central_signs_averaged"] = True
        self.assertFalse(producer.scope_firewall_valid(central_mutation))
        collision_mutation = copy.deepcopy(self.data["scope_firewall"])
        collision_mutation["flags"]["projected_matrix_collisions_ignored"] = True
        self.assertFalse(producer.scope_firewall_valid(collision_mutation))
        chronology_mutation = copy.deepcopy(self.data["scope_firewall"])
        chronology_mutation["flags"]["branch_chronology_averaged"] = True
        self.assertFalse(producer.scope_firewall_valid(chronology_mutation))

    def test_checker_is_independent_and_release_passes(self) -> None:
        checker_source = (PROJECT / "code" / "c26_independent_check.py").read_text(encoding="utf-8")
        self.assertNotIn("import c26_producer", checker_source)
        self.assertNotIn("from c26_producer", checker_source)
        self.assertNotIn("importlib", checker_source)
        checked = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
        self.assertTrue(checked["passed"])
        self.assertFalse(checked["producer_imported"])
        self.assertFalse(checked["external_theorems_reproved"])
        self.assertTrue(all(checked["checks"].values()))


if __name__ == "__main__":
    unittest.main()
