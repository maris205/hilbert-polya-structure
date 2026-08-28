#!/usr/bin/env python3
import json
import unittest
from collections import Counter

import round6_symbolic_zeta_calibrator as symbolic


class SymbolicZetaRound6Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = symbolic.load_freeze()
        cls.owners = symbolic.load_frozen_owners()
        cls.counts, cls.prefix, cls.metrics = symbolic.build_payload()

    def test_01_freeze_and_input_hashes_are_pinned_and_target_free(self) -> None:
        self.assertEqual(symbolic.sha256(self.freeze_raw), symbolic.FREEZE_SHA256)
        ledger = (symbolic.PROJECT_ROOT / symbolic.LEDGER_PATH).read_bytes()
        self.assertEqual(symbolic.sha256(ledger), symbolic.LEDGER_SHA256)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))
        self.assertEqual(self.freeze["object"]["roof"], 1)

    def test_02_adjacency_determinants_are_exact(self) -> None:
        self.assertEqual(symbolic.determinant_denominator(1), [1, 0, -3, -2])
        self.assertEqual(symbolic.determinant_denominator(-1), [1, 0, -3, 2])
        self.assertEqual(self.metrics["unweighted_denominator_coefficients"], [1, 0, -3, -2])
        self.assertEqual(self.metrics["phase_denominator_coefficients"], [1, 0, -3, 2])

    def test_03_trace_formula_matches_direct_matrix_powers(self) -> None:
        matrix = ((0, 1, 1), (1, 0, 1), (1, 1, 0))
        power = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

        def multiply(left, right):
            return tuple(
                tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
                for i in range(3)
            )

        for exponent in range(1, symbolic.MAX_DEGREE + 1):
            power = multiply(power, matrix)
            self.assertEqual(sum(power[i][i] for i in range(3)), symbolic.adjacency_trace(exponent))

    def test_04_mobius_counts_match_all_747_frozen_owners(self) -> None:
        observed = Counter(map(len, self.owners))
        self.assertEqual(len(self.owners), 747)
        for length in range(1, symbolic.MAX_DEGREE + 1):
            self.assertEqual(observed[length], symbolic.primitive_cycle_count(length))
        self.assertEqual(
            observed,
            Counter({2: 3, 3: 2, 4: 3, 5: 6, 6: 9, 7: 18, 8: 30, 9: 56, 10: 99, 11: 186, 12: 335}),
        )

    def test_05_owner_orientation_rotation_and_primitivity_semantics(self) -> None:
        self.assertIn((0, 1, 2), self.owners)
        self.assertIn((0, 2, 1), self.owners)
        for word in self.owners:
            self.assertEqual(word, symbolic.canonical_rotation(word))
            self.assertTrue(symbolic.is_primitive(word))
            self.assertTrue(all(word[index] != word[(index + 1) % len(word)] for index in range(len(word))))

    def test_06_unweighted_euler_trace_and_determinant_prefixes_match(self) -> None:
        for row in self.prefix:
            self.assertEqual(row["unweighted_euler_coefficient"], row["unweighted_trace_exponential_coefficient"])
            self.assertEqual(row["unweighted_euler_coefficient"], row["unweighted_determinant_coefficient"])

    def test_07_collision_phase_is_exact_z_to_minus_z_substitution(self) -> None:
        for row in self.prefix:
            self.assertEqual(row["phase_euler_coefficient"], row["phase_trace_exponential_coefficient"])
            self.assertEqual(row["phase_euler_coefficient"], row["phase_determinant_coefficient"])
            self.assertEqual(row["phase_euler_coefficient"], row["phase_substitution_coefficient"])

    def test_08_three_independent_exact_implementations_have_zero_mismatches(self) -> None:
        self.assertTrue(self.metrics["three_exact_implementations_match"])
        self.assertEqual(self.metrics["coefficient_mismatch_count"], 0)
        self.assertTrue(self.metrics["all_mobius_counts_match_frozen_ledger"])
        self.assertTrue(all(row["all_exactly_equal"] == "true" for row in self.prefix))

    def test_09_route_tuple_is_typed_and_physical_claims_are_firewalled(self) -> None:
        self.assertEqual(
            self.metrics["formal_route_a_tuple"],
            ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"],
        )
        self.assertEqual(self.metrics["overall_verdict"], "ROUTE_A_REJECTED")
        self.assertEqual(self.metrics["physical_three_disk_route_tuple"], "UNASSIGNED")
        self.assertIn("NOT_PHYSICAL_FLIGHT_LENGTH", self.metrics["a2_claim_boundary"])
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["prime_or_zero_tables_used"])

    def test_10_render_is_byte_deterministic_and_source_bound(self) -> None:
        first = symbolic.rendered_outputs()
        second = symbolic.rendered_outputs()
        self.assertEqual(first, second)
        core = {
            path: data
            for path, data in first.items()
            if path not in {symbolic.RECEIPT_PATH, symbolic.VALIDATION_PATH}
        }
        receipt = json.loads(first[symbolic.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], symbolic.combined_hash(core))
        for relative, binding in receipt["source_bindings"].items():
            payload = (symbolic.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], symbolic.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))


if __name__ == "__main__":
    unittest.main()
