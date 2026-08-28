#!/usr/bin/env python3
"""Tests for the P26 Round-8 complete exact finite taxonomy."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).with_name("round8_exact_taxonomy.py")
SPEC = importlib.util.spec_from_file_location("p26_round8_under_test", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load round8_exact_taxonomy.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def parse_degree_map(text: str) -> dict[int, Fraction]:
    return {
        int(degree): Fraction(value)
        for degree, value in (term.split(":", 1) for term in text.split("|"))
    }


class Round8ExactTaxonomyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cycle_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER)
        cls.moment_rows = MODULE.read_csv(MODULE.DEFAULT_ROUND6_MOMENT_LEDGER)
        cls.instances, cls.groups, cls.model = MODULE.build_taxonomy(
            cls.cycle_rows, cls.moment_rows
        )

    def test_locked_source_hashes(self) -> None:
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND4_CYCLE_LEDGER),
            MODULE.EXPECTED_ROUND4_CYCLE_SHA256,
        )
        self.assertEqual(
            MODULE.sha256(MODULE.DEFAULT_ROUND6_MOMENT_LEDGER),
            MODULE.EXPECTED_ROUND6_MOMENT_SHA256,
        )

    def test_complete_frozen_population_counts(self) -> None:
        self.assertEqual(len(self.cycle_rows), 138)
        self.assertEqual(len(self.instances), 138)
        self.assertEqual(len({(r["word"], r["hecke_prime"]) for r in self.instances}), 55)
        self.assertEqual(len(self.groups), 165)

    def test_exact_schreier_and_real_structure_model(self) -> None:
        self.assertEqual(self.model["homology_dimension_y0_11_over_q"], 3)
        self.assertEqual(self.model["compact_homology_dimension_x0_11_over_q"], 2)
        self.assertEqual(self.model["compact_plus_eigenspace_dimension"], 1)
        self.assertEqual(
            self.model["real_involution_matrix"],
            [[-1, 0, 0], [0, 1, 1], [0, 0, -1]],
        )

    def test_real_involution_formula_on_all_owners(self) -> None:
        arcs, relations = MODULE.ROUND7.relation_matrix()
        dual = MODULE.ROUND7.nullspace_basis(relations)
        for source_row in self.cycle_rows:
            owner = MODULE.ROUND7.parse_matrix(source_row["cycle_owner_matrix"])
            x, y, z = MODULE.ROUND7.homology_coordinates(owner, arcs, dual)
            observed = MODULE.ROUND7.homology_coordinates(
                MODULE.ROUND7.conjugate_owner(owner), arcs, dual
            )
            self.assertEqual(observed, (-x, y + z, -z))

    def test_every_owner_is_rebuilt_and_primitive_exactly(self) -> None:
        self.assertTrue(
            all(row["owner_recomputed_equal_exact"] == "true" for row in self.instances)
        )
        self.assertTrue(
            all(
                row["primitive_in_gamma0_11_exact_recomputed"] == "true"
                for row in self.instances
            )
        )
        self.assertTrue(all(row["owner_determinant"] == 1 for row in self.instances))
        self.assertTrue(all(row["owner_c_mod_11"] == 0 for row in self.instances))

    def test_instance_taxonomy_is_exhaustive_and_mutually_exclusive(self) -> None:
        counts = Counter(row["exact_instance_classification"] for row in self.instances)
        self.assertEqual(
            counts,
            Counter(
                {
                    MODULE.FULL_KERNEL: 2,
                    MODULE.PROJECTION_ONLY_KERNEL: 2,
                    MODULE.TRUE_NONKERNEL: 134,
                }
            ),
        )
        self.assertEqual(counts[MODULE.DEGENERATE_INSTANCE], 0)

    def test_instance_taxonomy_by_prime(self) -> None:
        expected = {
            2: Counter({MODULE.TRUE_NONKERNEL: 18}),
            3: Counter({MODULE.TRUE_NONKERNEL: 22}),
            5: Counter(
                {
                    MODULE.TRUE_NONKERNEL: 26,
                    MODULE.FULL_KERNEL: 2,
                    MODULE.PROJECTION_ONLY_KERNEL: 2,
                }
            ),
            7: Counter({MODULE.TRUE_NONKERNEL: 30}),
            13: Counter({MODULE.TRUE_NONKERNEL: 38}),
        }
        for prime, wanted in expected.items():
            observed = Counter(
                row["exact_instance_classification"]
                for row in self.instances
                if row["hecke_prime"] == prime
            )
            self.assertEqual(observed, wanted)

    def test_four_kernels_match_round7_words_and_split(self) -> None:
        full = {
            row["word"]
            for row in self.instances
            if row["exact_instance_classification"] == MODULE.FULL_KERNEL
        }
        projection = {
            row["word"]
            for row in self.instances
            if row["exact_instance_classification"]
            == MODULE.PROJECTION_ONLY_KERNEL
        }
        self.assertEqual(full, {"LRRLRRR", "LLRLLRLR"})
        self.assertEqual(projection, {"LLLRLLRLR", "LLLRLRLLR"})
        self.assertTrue(
            all(
                row["hecke_prime"] == 5 and row["cycle_degree"] == 5
                for row in self.instances
                if row["real_projection_zero_exact"] == "true"
            )
        )

    def test_real_kernel_is_equivalent_to_zero_exact_ratio(self) -> None:
        for row in self.instances:
            is_kernel = row["real_projection_zero_exact"] == "true"
            self.assertEqual(
                is_kernel,
                parse_fraction(str(row["normalized_real_period_ratio_exact"])) == 0,
            )

    def test_quadratic_moments_are_exact_rational_square_sums(self) -> None:
        grouped: dict[tuple[str, int], list[dict[str, object]]] = {}
        for row in self.instances:
            grouped.setdefault((str(row["word"]), int(row["hecke_prime"])), []).append(
                row
            )
        for row in self.groups:
            moments = parse_degree_map(
                str(row["normalized_quadratic_moments_by_degree_exact"])
            )
            instances = grouped[(str(row["word"]), int(row["hecke_prime"]))]
            for degree, moment in moments.items():
                expected = sum(
                    (
                        parse_fraction(
                            str(instance["normalized_real_period_ratio_exact"])
                        )
                        ** 2
                        for instance in instances
                        if int(instance["cycle_degree"]) == degree
                    ),
                    Fraction(0),
                )
                self.assertEqual(moment, expected)

    def test_sum_of_squares_kernel_equivalence_for_nonunit_degrees(self) -> None:
        for row in self.groups:
            moments = parse_degree_map(
                str(row["normalized_quadratic_moments_by_degree_exact"])
            )
            nonunit_zero = all(value == 0 for degree, value in moments.items() if degree > 1)
            self.assertEqual(
                nonunit_zero,
                row["all_nonunit_degree_moments_zero_exact"] == "true",
            )
            self.assertEqual(
                nonunit_zero,
                int(row["nonunit_true_nonkernel_instances"]) == 0,
            )

    def test_primary_laws_have_exact_four_of_fifty_five_survivors(self) -> None:
        for law in MODULE.PRIMARY_LAWS:
            rows = [row for row in self.groups if row["scalar_law"] == law]
            self.assertEqual(
                Counter(row["exact_group_classification"] for row in rows),
                Counter(
                    {
                        MODULE.FULL_GROUP_SURVIVOR: 2,
                        MODULE.PROJECTION_GROUP_SURVIVOR: 2,
                        MODULE.TRUE_GROUP_FAILURE: 51,
                    }
                ),
            )
            survivor_keys = {
                (str(row["word"]), int(row["hecke_prime"]))
                for row in rows
                if row["all_degree_moment_residuals_zero_exact"] == "true"
            }
            self.assertEqual(survivor_keys, MODULE.FROZEN_SURVIVOR_GROUPS)

    def test_secondary_control_fails_all_fifty_five_groups(self) -> None:
        rows = [
            row
            for row in self.groups
            if row["scalar_law"] == MODULE.SECONDARY_CONTROL_LAW
        ]
        self.assertEqual(len(rows), 55)
        self.assertTrue(
            all(row["exact_group_classification"] == MODULE.TRUE_GROUP_FAILURE for row in rows)
        )

    def test_failure_mechanisms_explain_all_primary_failures(self) -> None:
        a_rows = [
            row
            for row in self.groups
            if row["scalar_law"] == "a_p"
            and row["exact_group_classification"] == MODULE.TRUE_GROUP_FAILURE
        ]
        self.assertEqual(len(a_rows), 51)
        self.assertTrue(
            all(
                row["degree_one_residual_zero_exact"] == "false"
                and row["all_nonunit_degree_moments_zero_exact"] == "false"
                for row in a_rows
            )
        )
        squared = [
            row
            for row in self.groups
            if row["scalar_law"] == "a_p_squared"
            and row["exact_group_classification"] == MODULE.TRUE_GROUP_FAILURE
        ]
        both = sum(
            row["degree_one_residual_zero_exact"] == "false"
            and row["all_nonunit_degree_moments_zero_exact"] == "false"
            for row in squared
        )
        nonunit_only = sum(
            row["degree_one_residual_zero_exact"] == "true"
            and row["all_nonunit_degree_moments_zero_exact"] == "false"
            for row in squared
        )
        self.assertEqual((both, nonunit_only), (47, 4))

    def test_exact_verdicts_match_all_round6_numerical_crosschecks(self) -> None:
        self.assertTrue(
            all(
                row["exact_and_round6_numerical_verdict_agree"] == "true"
                for row in self.groups
            )
        )
        self.assertLessEqual(
            max(
                float(row["max_round6_normalized_moment_crosscheck_residual"])
                for row in self.groups
            ),
            MODULE.NUMERICAL_CROSSCHECK_TOLERANCE,
        )

    def test_fail_closed_validator_rejects_tampering(self) -> None:
        tampered = [dict(row) for row in self.instances]
        tampered[0]["exact_instance_classification"] = MODULE.DEGENERATE_INSTANCE
        self.assertTrue(MODULE.validate_outputs(tampered, self.groups, self.model))

    def test_target_and_route_boundaries_are_preserved(self) -> None:
        self.assertTrue(all(row["target_data_used"] == "false" for row in self.instances))
        self.assertTrue(all(row["target_data_used"] == "false" for row in self.groups))
        self.assertTrue(
            all(row["formal_a2_evaluation_run"] == "false" for row in self.groups)
        )
        self.assertTrue(
            all(row["route_b_invocation_allowed"] == "false" for row in self.groups)
        )

    def test_builder_is_deterministic_in_memory(self) -> None:
        instances, groups, model = MODULE.build_taxonomy(
            self.cycle_rows, self.moment_rows
        )
        self.assertEqual(instances, self.instances)
        self.assertEqual(groups, self.groups)
        self.assertEqual(model, self.model)


if __name__ == "__main__":
    unittest.main()
