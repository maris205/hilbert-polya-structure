#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


producer = load("c12a_producer", "c12a_producer.py")
checker = load("c12a_checker", "c12a_checker.py")


class C12ATests(unittest.TestCase):
    def test_legendre(self):
        self.assertEqual(producer.legendre(7, 5), -1)
        self.assertEqual(producer.legendre(3, 11), 1)
        self.assertEqual(producer.legendre(7, 7), 0)

    def test_symbolic_discriminants(self):
        result = producer.symbolic_certificate()
        self.assertTrue(result["D_a_1_pass"])
        self.assertTrue(result["D_a_2_pass"])
        self.assertTrue(result["n1_iterate_cyclic_ideal_pass"])
        self.assertTrue(result["n2_iterate_cyclic_ideal_pass"])
        self.assertTrue(result["generic_crt_comaximal_pass"])

    def test_period_five_collision(self):
        result = producer.period_five_certificate()
        self.assertEqual(result["scaled_x_coefficients"], [1, 2, -16, -22, 85, 60, -151])
        self.assertEqual(result["galois_group_certificate"]["conclusion"], "S6")

    def test_joint_information_loss(self):
        result = producer.joint_action_control()
        self.assertTrue(result["ordinary_collision_pass"])
        self.assertTrue(result["joint_separation_pass"])
        self.assertTrue(result["reversal_symmetry_pass"])
        independent = checker.independent_joint_control()
        self.assertTrue(independent["RHR_equals_H_inverse"])
        self.assertTrue(independent["F_commutes_with_H_and_R"])

    def test_frozen_fields(self):
        for p in (3, 5, 7, 11):
            for degree in range(1, 5):
                with self.subTest(p=p, degree=degree):
                    self.assertTrue(checker.FiniteField(p, degree).verify_field())

    def test_good_counts(self):
        expected = {(5, 1): (0, 0), (5, 2): (2, 0), (11, 1): (0, 0), (11, 2): (2, 0)}
        for (p, r), n1_expected in expected.items():
            with self.subTest(p=p, r=r):
                self.assertEqual(checker.count_n1_n2(checker.FiniteField(p, r), 1), n1_expected)

    def test_ramified_count(self):
        field = checker.FiniteField(7, 2)
        self.assertEqual(checker.count_n1_n2(field, 1), (1, 1))
        self.assertEqual(checker.count_n1_n2(field, 2), (3, 1))

    def test_degree_drop(self):
        for degree in range(1, 5):
            field = checker.FiniteField(3, degree)
            self.assertEqual(checker.count_n1_n2(field, 1), (1, 0))
            self.assertEqual(checker.count_n1_n2(field, 2), (1, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
