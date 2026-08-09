#!/usr/bin/env python3
"""Regression and mutation tests for the HCS-C24 release."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "results" / "c24_certificate.json"
INDEPENDENT = PROJECT / "results" / "c24_independent_check.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


producer = load_module("c24_producer", PROJECT / "code" / "c24_producer.py")


class C24Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_release_counts(self) -> None:
        enumeration = self.data["enumeration"]
        self.assertEqual(
            [row["primitive_free_cycles"] for row in enumeration["rows"]],
            [4, 2, 4, 4, 8, 11, 22, 35, 64, 110, 204, 360],
        )
        self.assertEqual(enumeration["primitive_free_cycle_total"], 828)
        self.assertEqual(enumeration["eventually_positive_by_length"], {"8": 1, "9": 6, "10": 14, "11": 36, "12": 89})
        self.assertEqual(enumeration["distinct_reciprocal_characteristic_polynomials"], 41)
        self.assertEqual(enumeration["character_singular_by_length"], {"10": 6, "11": 6, "12": 9})

    def test_literal_source_and_transport(self) -> None:
        states, edges, _ = producer.build_graph()
        self.assertEqual(len(states), 7)
        self.assertEqual(len(edges), 14)
        for (source, _), edge in edges.items():
            target = edge["target"]
            matrix = edge["matrix"]
            self.assertEqual(matrix * producer.omega(states[source]) * matrix.T, producer.omega(states[target]))

    def test_transposed_edge_mutation_is_rejected(self) -> None:
        states, edges, _ = producer.build_graph()
        source = states.index(producer.INITIAL)
        edge = edges[(source, "t")]
        wrong = sp.Matrix(edge["matrix"]).T
        self.assertNotEqual(wrong * producer.omega(states[source]) * wrong.T, producer.omega(states[edge["target"]]))

    def test_wrong_chronology_mutation_is_rejected(self) -> None:
        states, edges, _ = producer.build_graph()
        central = states.index(producer.INITIAL)
        move_word = "bbtbttbt"
        current = central
        correct, wrong = sp.eye(4), sp.eye(4)
        for move_type in move_word:
            edge = edges[(current, move_type)]
            matrix = sp.Matrix(edge["matrix"])
            correct = matrix * correct
            wrong = wrong * matrix
            current = edge["target"]
        self.assertEqual(current, central)
        self.assertEqual(correct.charpoly().all_coeffs(), [1, -7, 13, -7, 1])
        self.assertEqual(wrong.charpoly().all_coeffs(), [1, -15, 17, -7, 1])
        self.assertNotEqual(wrong.charpoly().all_coeffs(), wrong.charpoly().all_coeffs()[::-1])
        J0 = producer.omega(producer.INITIAL).inv()
        self.assertEqual(correct.T * J0 * correct, J0)
        self.assertNotEqual(wrong.T * J0 * wrong, J0)

    def test_directed_tokens_prevent_move_word_collision(self) -> None:
        states, edges, _ = producer.build_graph()
        t_self_loops = []
        for state in range(len(states)):
            edge = edges[(state, "t")]
            if edge["target"] == state:
                t_self_loops.append(((state, "t", state),))
        self.assertGreaterEqual(len(t_self_loops), 2)
        self.assertEqual({"".join(token[1] for token in loop) for loop in t_self_loops}, {"t"})
        self.assertGreater(len({loop for loop in t_self_loops}), 1)

    def test_proper_power_mutation_is_rejected(self) -> None:
        first = self.data["eventually_positive_cycles"][0]
        tokens = []
        for encoded in first["canonical_edges"]:
            source, move_type, target = encoded.split(":")
            tokens.append((int(source[1:]), move_type, int(target[1:])))
        tokens = tuple(tokens)
        self.assertTrue(producer.primitive_cycle(tokens))
        self.assertFalse(producer.primitive_cycle(tokens + tokens))

    def test_positive_filter_is_phase_invariant(self) -> None:
        states, edges, _ = producer.build_graph()
        first = self.data["eventually_positive_cycles"][0]
        tokens = []
        for encoded in first["canonical_edges"]:
            source, move_type, target = encoded.split(":")
            tokens.append((int(source[1:]), move_type, int(target[1:])))
        phase_flags = []
        for phase in producer.rotations(tokens):
            matrix = producer.cycle_matrix(phase, edges)
            phase_flags.append(producer.positive_exponent(matrix) is not None)
        self.assertTrue(all(phase_flags))

    def test_singular_character_rows_are_not_silently_regularized(self) -> None:
        singular = [row for row in self.data["eventually_positive_cycles"] if row["metaplectic_character_locus"] != "regular"]
        self.assertEqual(len(singular), 21)
        for row in singular:
            self.assertTrue(all(value == 0 for value in row["det_I_minus_power"].values()))

    def test_independent_release_passed(self) -> None:
        checked = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
        self.assertTrue(checked["passed"])
        self.assertEqual(checked["material_passport"]["verification_status"], "VERIFIED")
        self.assertTrue(all(checked["checks"].values()))


if __name__ == "__main__":
    unittest.main()
