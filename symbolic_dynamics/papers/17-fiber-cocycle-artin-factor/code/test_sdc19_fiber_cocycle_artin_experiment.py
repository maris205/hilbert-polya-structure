from __future__ import annotations

import csv
from pathlib import Path
import sys
import unittest

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))

from sdc19_fiber_cocycle_artin_core import (  # noqa: E402
    brute_primitive_necklace_degree_counts,
    c2_transitivity_certificate,
    cm_character_certificate,
    coboundary_control_rows,
    enumerate_natural_tables,
    formal_c2_certificate,
    inventory_control_rows,
    primitive_census_row,
    primitive_necklace_degree_counts,
    regular_local_cyclotomic_certificate,
    repetition_ledger,
    transition_countercontrol_rows,
)


class FormalFactorizationTests(unittest.TestCase):
    def test_c2_formal_factorization_through_ten_atoms(self) -> None:
        for n_atoms in range(1, 11):
            row = formal_c2_certificate(n_atoms)
            self.assertEqual(row["d_plus_mismatch_terms"], 0)
            self.assertEqual(row["d_minus_mismatch_terms"], 0)
            self.assertEqual(row["d_regular_mismatch_terms"], 0)
            self.assertEqual(row["same_object_block_mismatch_terms"], 0)

    def test_two_atom_term_counts(self) -> None:
        row = formal_c2_certificate(2)
        self.assertEqual(row["d_plus_terms"], 4)
        self.assertEqual(row["d_minus_terms"], 4)
        self.assertEqual(row["d_regular_terms"], 4)

    def test_trace_repetitions(self) -> None:
        for n_atoms in range(1, 11):
            rows = repetition_ledger(n_atoms, max_degree=10)
            self.assertEqual(len(rows), 30)
            self.assertTrue(all(row["exact_match"] for row in rows))


class DynamicsAndPrimitiveTests(unittest.TestCase):
    def test_c2_transitivity_and_mixing_boundary(self) -> None:
        one = c2_transitivity_certificate(1)
        self.assertTrue(one["topologically_transitive"])
        self.assertFalse(one["mixing"])
        self.assertEqual(one["period"], 2)
        for n_atoms in range(2, 11):
            row = c2_transitivity_certificate(n_atoms)
            self.assertTrue(row["topologically_transitive"])
            self.assertTrue(row["mixing"])
            self.assertEqual(row["period"], 1)

    def test_formula_matches_small_bruteforce(self) -> None:
        for n_atoms in (1, 2):
            for word_length in range(1, 6):
                self.assertEqual(
                    primitive_necklace_degree_counts(n_atoms, word_length),
                    brute_primitive_necklace_degree_counts(n_atoms, word_length),
                )

    def test_frozen_pilot_counts(self) -> None:
        n2_expected = [
            (3, 1, 1),
            (3, 1, 1),
            (8, 4, 4),
            (18, 8, 8),
            (48, 24, 24),
            (116, 56, 56),
            (312, 156, 156),
            (810, 400, 400),
        ]
        n3_expected = [
            (7, 3, 3),
            (21, 9, 9),
            (112, 56, 56),
            (588, 288, 288),
            (3360, 1680, 1680),
            (19544, 9744, 9744),
        ]
        for word_length, expected in enumerate(n2_expected, start=1):
            row = primitive_census_row(2, word_length, 2)
            actual = (
                row["base_primitive_necklaces"],
                row["base_necklaces_closing_after_one_traversal"],
                row["mixed_members_closing_after_one_traversal"],
            )
            self.assertEqual(actual, expected)
        for word_length, expected in enumerate(n3_expected, start=1):
            row = primitive_census_row(3, word_length, 2)
            actual = (
                row["base_primitive_necklaces"],
                row["base_necklaces_closing_after_one_traversal"],
                row["mixed_members_closing_after_one_traversal"],
            )
            self.assertEqual(actual, expected)

    def test_base_vs_lifted_cycle_count(self) -> None:
        row = primitive_census_row(2, 1, 2)
        self.assertEqual(row["base_primitive_necklaces"], 3)
        self.assertEqual(row["base_necklaces_closing_after_one_traversal"], 1)
        self.assertEqual(row["mixed_members_closing_after_one_traversal"], 1)
        self.assertEqual(row["lifted_primitive_cycles_total"], 4)


class GeneralCyclicAndRigidityTests(unittest.TestCase):
    def test_all_cm_characters(self) -> None:
        for n_atoms in range(1, 11):
            for group_order in range(2, 9):
                for character in range(group_order):
                    row = cm_character_certificate(n_atoms, group_order, character)
                    self.assertEqual(row["coefficient_phase_mismatches"], 0)
                    self.assertTrue(row["atom_local_factorization_exact"])

    def test_regular_local_cyclotomic_identity(self) -> None:
        for group_order in range(2, 9):
            self.assertTrue(regular_local_cyclotomic_certificate(group_order)["exact_match"])

    def test_naturality_unique_power_table(self) -> None:
        for max_degree in range(2, 7):
            for group_order in range(2, 9):
                details, summary = enumerate_natural_tables(max_degree, group_order)
                self.assertEqual(len(details), group_order ** (max_degree - 1))
                self.assertTrue(summary["unique_power_table_confirmed"])
                clean = [
                    row for row in details if row["operator_coefficient_clean"]
                ]
                self.assertEqual(len(clean), 1)
                expected = ":".join(
                    str(degree % group_order)
                    for degree in range(1, max_degree + 1)
                )
                self.assertEqual(clean[0]["table"], expected)


class ControlTests(unittest.TestCase):
    def test_coboundary_controls_and_periodic_negative_controls(self) -> None:
        rows = coboundary_control_rows(max_cycle_length=4)
        positives = [row for row in rows if row["control_kind"] == "vertex_coboundary"]
        negatives = [
            row for row in rows if row["control_kind"] == "noncoboundary_negative_control"
        ]
        self.assertTrue(
            all(
                row["nonidentity_periodic_holonomies"] == 0
                and row["gauge_edge_mismatches"] == 0
                for row in positives
            )
        )
        self.assertTrue(
            all(row["nonidentity_periodic_holonomies"] > 0 for row in negatives)
        )
        c2_positives = [row for row in positives if row["group_order"] == 2]
        self.assertTrue(all(row["c2_exact_determinant_gauge_match"] for row in c2_positives))

    def test_transition_countercontrols(self) -> None:
        rows = {row["control"]: row for row in transition_countercontrol_rows()}
        coboundary = rows["vertex_coboundary_degree"]
        self.assertTrue(coboundary["is_vertex_coboundary"])
        self.assertTrue(coboundary["equals_trivial_atom_local_factor"])
        for name in (
            "diagonal_return",
            "incidence_intersection_parity",
            "strict_symbol_change",
        ):
            self.assertFalse(rows[name]["is_vertex_coboundary"])
            self.assertTrue(rows[name]["first_nontrivial_periodic_holonomy"])
        x, y = sp.symbols("x y")
        self.assertEqual(
            sp.expand(sp.sympify(rows["diagonal_return"]["sign_block_determinant"])),
            4 * x**2 * y**2 - x * y + x + y + 1,
        )
        self.assertEqual(
            sp.expand(sp.sympify(rows["strict_symbol_change"]["sign_block_determinant"])),
            -4 * x**2 * y**2 + x * y - x - y + 1,
        )

    def test_all_inventory_controls_replicate(self) -> None:
        rows = inventory_control_rows(n_atoms=8, seeds=range(17000, 17016))
        self.assertEqual(len(rows), 64)
        for row in rows:
            self.assertTrue(row["d_plus_exact"])
            self.assertTrue(row["d_minus_exact"])
            self.assertTrue(row["d_regular_exact"])
            self.assertTrue(row["same_object_exact"])


class ArtifactSmokeTests(unittest.TestCase):
    def test_result_csvs_if_present(self) -> None:
        result_dir = PROJECT / "results"
        path = result_dir / "formal_c2_factorization.csv"
        if not path.exists():
            self.skipTest("full result suite has not been run yet")
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 10)
        self.assertTrue(all(row["same_object_block_mismatch_terms"] == "0" for row in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
