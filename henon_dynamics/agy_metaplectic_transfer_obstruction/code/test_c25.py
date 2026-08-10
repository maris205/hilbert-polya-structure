#!/usr/bin/env python3
"""Regression and mutation tests for the HCS-C25 exact release."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c25_certificate.json"
INDEPENDENT = PROJECT / "results" / "c25_independent_check.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


producer = load_module("c25_release_producer", PROJECT / "code" / "c25_producer.py")
checker = load_module("c25_release_checker", PROJECT / "code" / "c25_independent_check.py")


class C25Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        cls.states, cls.edges = producer.build_graph()

    def test_literal_graph_and_AGY_source_word(self) -> None:
        self.assertEqual(len(self.states), 7)
        self.assertEqual(len(self.edges), 14)
        witness = self.data["agy_section_witness"]
        gamma = witness["gamma_star"]
        self.assertEqual(witness["base_state"], 4)
        self.assertEqual(gamma["word"], "t" * 64 + "tbttbtbb" * 8)
        self.assertEqual(gamma["length"], 128)
        self.assertTrue(gamma["closed"])

    def test_initial_run_is_scanned_not_read_from_compressed_exponent(self) -> None:
        word = self.data["agy_section_witness"]["gamma_star"]["word"]
        neat = self.data["agy_section_witness"]["gamma_star"]["neatness"]
        self.assertEqual(producer.initial_constant_run_length(word), 65)
        self.assertEqual(checker.initial_run(word), 65)
        self.assertEqual(neat["initial_constant_run_length"], 65)
        self.assertTrue(neat["at_least_half_of_word"])

    def test_eight_complete_threshold_and_border_certificate(self) -> None:
        gamma = self.data["agy_section_witness"]["gamma_star"]
        self.assertEqual(gamma["complete_block_count"], 8)
        self.assertTrue(all(block["complete"] for block in gamma["complete_blocks"]))
        self.assertEqual(gamma["strong_positivity_criterion"]["threshold_3d_minus_4"], 8)
        self.assertEqual(gamma["neatness"]["proper_border_lengths"], [])
        bordered_mutation = gamma["word"] + gamma["word"][0]
        self.assertIn(1, producer.proper_border_lengths(bordered_mutation))
        self.assertFalse(7 >= producer.STRONG_POSITIVITY_THRESHOLD)

    def test_later_left_matrix_and_decoder_trace(self) -> None:
        end, matrix, _ = producer.follow_word(4, producer.GAMMA_STAR, self.edges)
        self.assertEqual(end, 4)
        released = self.data["agy_section_witness"]["gamma_star"]
        self.assertEqual(producer.matrix_json(matrix), released["chronological_matrix_B"])
        decoded = producer.decode_length_matrix(4, producer.transpose(matrix), self.edges, include_matrices=True)
        self.assertEqual(decoded, released["decoder"])
        self.assertEqual(decoded["decoded_word"], producer.GAMMA_STAR)
        self.assertTrue(all(row["strict_drop"] == row["loser_row_sum"] > 0 for row in decoded["trace"]))

    def test_right_multiplied_chronology_mutation_is_rejected(self) -> None:
        _, correct, tokens = producer.follow_word(4, producer.GAMMA_STAR, self.edges)
        wrong = producer.IDENTITY
        for token in tokens:
            edge = self.edges[(int(token["source"]), str(token["type"]))]
            wrong = producer.matmul(wrong, edge["matrix"])
        self.assertNotEqual(wrong, correct)
        omega = producer.omega(self.states[4])
        self.assertNotEqual(producer.as_sympy(wrong) * omega * producer.as_sympy(wrong).T, omega)
        with self.assertRaises(ValueError):
            producer.decode_length_matrix(4, producer.transpose(wrong), self.edges, include_matrices=False)

    def test_transposed_edge_and_length_homology_mutations_are_rejected(self) -> None:
        source = 4
        edge = self.edges[(source, "t")]
        target = int(edge["target"])
        correct = producer.as_sympy(edge["matrix"])
        wrong = correct.T
        self.assertEqual(correct * producer.omega(self.states[source]) * correct.T, producer.omega(self.states[target]))
        self.assertNotEqual(wrong * producer.omega(self.states[source]) * wrong.T, producer.omega(self.states[target]))
        _, gamma_matrix, _ = producer.follow_word(4, producer.GAMMA_STAR, self.edges)
        with self.assertRaises(ValueError):
            producer.decode_length_matrix(4, gamma_matrix, self.edges, include_matrices=False)

    def test_state_cannot_be_replaced_by_move_word(self) -> None:
        top_self_loops = []
        for state in range(7):
            edge = self.edges[(state, "t")]
            if edge["target"] == state:
                top_self_loops.append((state, edge["matrix"]))
        self.assertGreaterEqual(len(top_self_loops), 2)
        self.assertGreater(len({matrix for _, matrix in top_self_loops}), 1)
        for state, matrix in top_self_loops:
            decoded = producer.decode_length_matrix(state, producer.transpose(matrix), self.edges, include_matrices=False)
            self.assertEqual(decoded["decoded_word"], "t")
            self.assertEqual(decoded["end_state"], state)

    def test_projective_jacobian_exponent_three_mutation_is_rejected(self) -> None:
        gamma = self.data["agy_section_witness"]["gamma_star"]
        branch = self.data["agy_section_witness"]["projective_inverse_branch"]
        length_matrix = sp.Matrix(gamma["length_matrix_R_equals_B_transpose"])
        x0 = checker.vector_from_json(branch["x0"])
        scale = checker.rational_from_json(branch["roof"]["exp_r_at_x0"])
        actual = checker.jacobian_at(length_matrix, x0)
        self.assertEqual(actual, scale ** (-4))
        self.assertNotEqual(actual, scale ** (-3))

    def test_full_rank_projection_scope_is_explicit(self) -> None:
        theorem = self.data["all_length_decoder_theorem"]
        self.assertTrue(all(producer.omega(state).det() == 1 for state in self.states))
        self.assertIn("full four-by-four", theorem["projection_scope"]["full_matrix_theorem"])
        self.assertIn("relative-homology kernel", theorem["projection_scope"]["general_warning"])
        self.assertIn("does not follow", theorem["projection_scope"]["general_warning"])

    def test_statewise_integer_symplectic_trivialization(self) -> None:
        released = self.data["statewise_symplectic_trivialization"]
        base_form, frames, parents, fixed_edges = checker.independent_fixed_fiber_trivialization(
            self.states, self.edges
        )
        self.assertEqual(released["base_state"], 4)
        self.assertEqual(released["base_form_J0"], producer.matrix_json(base_form))
        self.assertEqual(released["counts"], {
            "state_frames": 7,
            "fixed_fiber_edges": 14,
            "identity_fixed_edges": 6,
            "nonidentity_fixed_edges": 8,
        })
        for state, frame in frames.items():
            self.assertEqual(frame.det(), 1)
            self.assertTrue(all(sp.denom(entry) == 1 for entry in frame))
            self.assertEqual(frame.T * producer.omega(self.states[state]).inv() * frame, base_form)
            if parents[state] is not None:
                source, move_type = parents[state]
                edge = self.edges[(source, move_type)]
                self.assertEqual(frame, sp.Matrix(edge["matrix"]) * frames[source])
        self.assertTrue(all(edge["symplectic"] and edge["integral"] for edge in fixed_edges))

    def test_wrong_frame_direction_and_edge_trivialization_are_rejected(self) -> None:
        base_form, frames, _, _ = checker.independent_fixed_fiber_trivialization(self.states, self.edges)

        tree_edge = self.edges[(4, "b")]
        target = int(tree_edge["target"])
        matrix = sp.Matrix(tree_edge["matrix"])
        correct_frame = matrix * frames[4]
        wrong_direction_frame = matrix.T * frames[4]
        self.assertEqual(correct_frame.T * producer.omega(self.states[target]).inv() * correct_frame, base_form)
        self.assertNotEqual(
            wrong_direction_frame.T * producer.omega(self.states[target]).inv() * wrong_direction_frame,
            base_form,
        )

        source, move_type = 0, "t"
        edge = self.edges[(source, move_type)]
        target = int(edge["target"])
        matrix = sp.Matrix(edge["matrix"])
        correct_fixed = frames[target].inv() * matrix * frames[source]
        wrong_fixed = frames[source].inv() * matrix * frames[target]
        self.assertEqual(correct_fixed.T * base_form * correct_fixed, base_form)
        self.assertNotEqual(wrong_fixed, correct_fixed)
        self.assertNotEqual(wrong_fixed.T * base_form * wrong_fixed, base_form)

    def test_ttt_is_not_promoted_to_the_AGY_section(self) -> None:
        toy = self.data["central_return_toy"]
        self.assertFalse(toy["canonical_AGY_application_claimed"])
        self.assertTrue(toy["scope"].startswith("TOY_CENTRAL_RETURN_SANITY_CHECK"))
        self.assertNotEqual(toy["word"], self.data["agy_section_witness"]["gamma_star"]["word"])

    def test_stress_window_is_not_the_proof_or_an_n13_ledger(self) -> None:
        stress = self.data["finite_stress_test"]
        self.assertEqual(stress["max_elementary_length"], 22)
        self.assertEqual(stress["total_first_returns"], 35420)
        self.assertEqual(stress["distinct_forward_matrices"], 35420)
        self.assertEqual(stress["collision_count"], 0)
        self.assertEqual(stress["role"], "NON_PROOF_DIAGNOSTIC_AND_MUTATION_SENTINEL")
        self.assertFalse(self.data["all_length_decoder_theorem"]["finite_enumeration_is_proof_basis"])
        self.assertFalse(self.data["decisions"]["finite_length_13_ledger_used"])

    def test_checker_is_independent_and_release_passes(self) -> None:
        source = (PROJECT / "code" / "c25_independent_check.py").read_text(encoding="utf-8")
        self.assertNotIn("import c25_producer", source)
        self.assertNotIn("from c25_producer", source)
        self.assertNotIn("importlib", source)
        checked = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
        self.assertTrue(checked["passed"])
        self.assertEqual(checked["material_passport"]["verification_status"], "VERIFIED")
        self.assertTrue(all(checked["checks"].values()))


if __name__ == "__main__":
    unittest.main()
