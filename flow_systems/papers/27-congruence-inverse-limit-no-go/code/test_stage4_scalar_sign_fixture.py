#!/usr/bin/env python3
"""Stage-4 direct regression fixtures for the shared projective-sign kernel."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round2_reduction_orders.py")
SPEC = importlib.util.spec_from_file_location("p27_round2_stage4", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Stage4ScalarSignFixtureTests(unittest.TestCase):
    def test_direct_minus_identity_fixture_at_every_registered_modulus(self) -> None:
        for _, modulus in MODULE.LEVELS:
            minus_identity = (((-1) % modulus, 0), (0, (-1) % modulus))
            self.assertEqual(MODULE.scalar_sign(minus_identity, modulus), -1)
            self.assertEqual(
                MODULE.psl_order_sequential(minus_identity, modulus), (1, -1)
            )
            self.assertEqual(
                MODULE.psl_order_from_group_bound(minus_identity, modulus), (1, -1)
            )

    def test_positive_and_negative_scalar_branches_are_distinct(self) -> None:
        for _, modulus in MODULE.LEVELS:
            identity = ((1 % modulus, 0), (0, 1 % modulus))
            minus_identity = (((-1) % modulus, 0), (0, (-1) % modulus))
            nonscalar = ((1 % modulus, 1 % modulus), (0, 1 % modulus))
            self.assertEqual(MODULE.scalar_sign(identity, modulus), 1)
            self.assertEqual(MODULE.scalar_sign(minus_identity, modulus), -1)
            self.assertIsNone(MODULE.scalar_sign(nonscalar, modulus))

    def test_shared_kernel_limitation_is_machine_visible(self) -> None:
        sequential_globals = MODULE.psl_order_sequential.__globals__
        bound_globals = MODULE.psl_order_from_group_bound.__globals__
        self.assertIs(sequential_globals["scalar_sign"], MODULE.scalar_sign)
        self.assertIs(bound_globals["scalar_sign"], MODULE.scalar_sign)
        self.assertIs(sequential_globals["matrix_mul"], MODULE.matrix_mul)
        self.assertIs(MODULE.matrix_pow.__globals__["matrix_mul"], MODULE.matrix_mul)


if __name__ == "__main__":
    unittest.main()
