from __future__ import annotations

import csv
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from sdc20_incidence_transition_holonomy_core import (  # noqa: E402
    all_groups,
    exact_group_audit,
    explicit_s3_certificate,
    gauge_power_tables,
    incidence_orbit_rows,
    incidence_orbit_summary,
    inventory_control_rows,
    primitive_holonomy_rows,
    q8_group,
    s3_group,
    trace_class_gate_rows,
    transition_control_rows,
)


class IncidenceGrammarTests(unittest.TestCase):
    def test_01_group_orders_and_representation_dimensions(self) -> None:
        groups = {group.name: group for group in all_groups()}
        self.assertEqual({name: group.order for name, group in groups.items()}, {"S3": 6, "D4": 8, "Q8": 8})
        self.assertEqual(groups["S3"].representation("standard").dimension, 2)
        self.assertEqual(groups["D4"].representation("geometric2d").dimension, 2)
        self.assertEqual(groups["Q8"].representation("left_quaternion4d").dimension, 4)

    def test_02_incidence_orbit_counts(self) -> None:
        rows = incidence_orbit_summary()
        self.assertEqual([row["orbit_count"] for row in rows], [1, 5, 13, 26])
        self.assertEqual([row["new_type_count"] for row in rows], [1, 4, 8, 13])
        self.assertTrue(all(row["exact_match"] for row in rows))

    def test_03_incidence_orbits_partition_all_pairs(self) -> None:
        details = incidence_orbit_rows()
        for n_atoms in range(1, 5):
            selected = [row for row in details if row["n_atoms"] == n_atoms]
            self.assertEqual(sum(row["ordered_pair_orbit_size"] for row in selected), ((1 << n_atoms) - 1) ** 2)
            self.assertTrue(
                all(
                    row["ordered_pair_orbit_size"] * row["stabilizer_size"]
                    == __import__("math").factorial(n_atoms)
                    for row in selected
                )
            )


class ExplicitS3Tests(unittest.TestCase):
    def test_04_standard_determinant_formula(self) -> None:
        certificate = explicit_s3_certificate()
        self.assertTrue(certificate["standard_formula_exact"])
        self.assertIn("6*x**3*y**3", certificate["standard_formula"])

    def test_05_trivial_and_sign_blocks(self) -> None:
        certificate = explicit_s3_certificate()
        self.assertTrue(certificate["trivial_exact"])
        self.assertTrue(certificate["sign_exact"])
        self.assertEqual(certificate["trivial_determinant"], "(1-x)*(1-y)")
        self.assertEqual(certificate["sign_determinant"], "(1-x)*(1-y)")

    def test_06_trace_log_leakage_coefficients(self) -> None:
        certificate = explicit_s3_certificate()
        self.assertTrue(certificate["trace_log_methods_exact"])
        self.assertEqual(certificate["trace_log_coefficients"]["x^2y^1"], "-3")
        self.assertEqual(certificate["trace_log_coefficients"]["x^1y^2"], "-3")
        self.assertEqual(certificate["trace_log_coefficients"]["x^2y^2"], "-6")
        self.assertEqual(certificate["trace_log_coefficients"]["x^3y^3"], "-9")

    def test_07_cycle_separated_commutator(self) -> None:
        certificate = explicit_s3_certificate()
        self.assertTrue(certificate["four_cycle_holonomy_nonidentity"])
        self.assertTrue(certificate["four_cycle_primitive"])
        self.assertEqual(certificate["four_cycle_character_gap"], 3)
        self.assertEqual(certificate["four_cycle_unique_connected_cyclic_traversals"], 1)
        self.assertFalse(certificate["unmarked_x3y3_isolated_commutator"])

    def test_08_primitive_holonomy_ledger(self) -> None:
        rows = primitive_holonomy_rows()
        self.assertEqual(len(rows), 3)
        square = next(row for row in rows if row["length"] == 4)
        self.assertEqual((square["x_degree"], square["y_degree"], square["scalar_sign"]), (3, 3, 1))
        self.assertEqual(square["character_gap"], 3)
        self.assertTrue(all(row["rotation_only_quotient"] and not row["reflection_quotiented"] for row in rows))


class ExhaustiveRigidityTests(unittest.TestCase):
    def test_09_s3_exhaustive_counts(self) -> None:
        audit = exact_group_audit("S3")
        self.assertEqual((audit["tables"], audit["one_dimensional_clean"]), (7776, 972))
        self.assertEqual((audit["all_irrep_clean"], audit["gauge_power_clean"], audit["nongauge_clean"]), (36, 36, 0))
        self.assertTrue(audit["exact_certification"]["crt_bound_strict"])

    def test_10_d4_exhaustive_counts(self) -> None:
        audit = exact_group_audit("D4")
        self.assertEqual(audit["tables"], 32768)
        self.assertEqual((audit["all_irrep_clean"], audit["gauge_power_clean"], audit["nongauge_clean"]), (64, 64, 0))
        self.assertEqual(len(gauge_power_tables(next(group for group in all_groups() if group.name == "D4"))), 64)

    def test_11_q8_one_dimensional_audit_is_insufficient(self) -> None:
        audit = exact_group_audit("Q8")
        self.assertEqual(audit["tables"], 32768)
        self.assertEqual(audit["one_dimensional_clean"], 512)
        self.assertEqual((audit["all_irrep_clean"], audit["gauge_power_clean"], audit["nongauge_clean"]), (64, 64, 0))
        self.assertEqual(len(gauge_power_tables(q8_group())), 64)


class BoundaryAndControlTests(unittest.TestCase):
    def test_12_transition_controls_separate_gauge_and_candidate(self) -> None:
        rows = {row["control"]: row for row in transition_control_rows()}
        self.assertTrue(rows["identity_cocycle"]["in_counting_gauge_class"])
        self.assertTrue(rows["gauge_generated_noncommuting"]["in_counting_gauge_class"])
        candidate = rows["refinement_coarsening_candidate"]
        self.assertFalse(candidate["in_counting_gauge_class"])
        self.assertTrue(candidate["one_dimensional_clean"])
        self.assertTrue(candidate["four_cycle_nonidentity"])

    def test_13_inventory_controls_prove_too_much(self) -> None:
        rows = inventory_control_rows()
        self.assertEqual(len(rows), 30)
        self.assertEqual(len({row["inventory"] for row in rows}), 6)
        self.assertTrue(all(row["trivial_euler_ledger_exact"] for row in rows))
        self.assertTrue(all(row["standard_leakage_persists"] for row in rows))
        self.assertTrue(all(row["inventory_blind_symbolic_rule"] for row in rows))
        self.assertTrue(all(row["target_zero_data_used"] is False for row in rows))

    def test_14_trace_class_thresholds_and_artifact_smoke(self) -> None:
        rows = {row["block"]: row for row in trace_class_gate_rows()}
        self.assertEqual(rows["trivial_rank_one_arrival"]["threshold"], 1)
        self.assertEqual(rows["nontrivial_symmetric_incidence"]["threshold"], 2)
        self.assertTrue(all(row["boundary_or_below_claimed"] is False for row in rows.values()))
        artifact = ROOT / "results" / "group_enumeration_summary.csv"
        if artifact.exists():
            with artifact.open(newline="", encoding="utf-8") as handle:
                self.assertEqual(len(list(csv.DictReader(handle))), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
