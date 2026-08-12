import unittest

from wheel_dag import (
    certify_levels,
    compare_to_arithmetic_units,
    controlled_levels,
    intrinsic_wheels,
)


class WheelDAGTests(unittest.TestCase):
    def test_intrinsic_recursion_generates_initial_primes(self):
        levels, _, _ = intrinsic_wheels(7)
        self.assertEqual([level.multiplier for level in levels[1:]], [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual([level.modulus for level in levels[1:]], [2, 6, 30, 210, 2310, 30030, 510510])

    def test_arithmetic_lift_is_exact_unit_set(self):
        levels, _, _ = intrinsic_wheels(7)
        for level in levels:
            comparison = compare_to_arithmetic_units(level)
            self.assertEqual(comparison["unit_false_positive_count"], 0)
            self.assertEqual(comparison["unit_false_negative_count"], 0)

    def test_exact_dag_certificate(self):
        levels, edges, _ = intrinsic_wheels(6)
        certificate = certify_levels(levels, edges)
        self.assertTrue(certificate["edge_count_exact"])
        self.assertEqual(certificate["level_step_failures"], 0)
        self.assertEqual(certificate["branch_formula_failures"], 0)
        self.assertTrue(certificate["kahn_processed_all_nodes"])
        self.assertEqual(certificate["directed_cycle_count"], 0)

    def test_controls_are_degree_and_size_matched(self):
        baseline, baseline_edges, _ = intrinsic_wheels(5)
        for control, seed in (("fixed_branch", None), ("cyclic_branch", None), ("random_branch", 1234)):
            levels, edges, _ = controlled_levels(baseline, control, seed)
            self.assertEqual([len(level.residues) for level in levels], [len(level.residues) for level in baseline])
            self.assertEqual(len(edges), len(baseline_edges))
            self.assertTrue(certify_levels(levels, edges)["kahn_processed_all_nodes"])

    def test_nonarithmetic_control_fails_unit_ledger(self):
        baseline, _, _ = intrinsic_wheels(4)
        levels, _, _ = controlled_levels(baseline, "fixed_branch")
        self.assertGreater(compare_to_arithmetic_units(levels[-1])["unit_false_positive_count"], 0)


if __name__ == "__main__":
    unittest.main()
