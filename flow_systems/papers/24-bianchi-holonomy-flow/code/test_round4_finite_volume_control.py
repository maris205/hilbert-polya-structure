#!/usr/bin/env python3
import unittest

import round4_finite_volume_control as control


class FiniteVolumeControlRound4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        (
            cls.invariants,
            cls.length_rows,
            cls.cross_rows,
            cls.metrics,
        ) = control.build_payload()
        cls.contract = cls.invariants["contract"]

    def test_pinned_dependency_and_named_object(self) -> None:
        self.assertEqual(control.snappy.__version__, "3.3.2")
        self.assertEqual(self.contract["link_table_name"], "5_2")
        self.assertEqual(self.contract["census_name"], "m015")
        self.assertTrue(self.contract["isometric_to_census"])

    def test_exact_topological_control_contract(self) -> None:
        self.assertTrue(self.contract["orientable"])
        self.assertEqual(self.contract["cusps"], 1)
        self.assertEqual(self.contract["cusp_topology"], "torus cusp")
        self.assertTrue(self.contract["cusp_complete"])
        self.assertEqual(self.contract["link_components"], 1)
        self.assertEqual(self.contract["diagram_crossings"], 5)
        self.assertEqual(self.contract["homology"], "Z")
        self.assertFalse(self.contract["has_finite_vertices"])

    def test_source_chain_keeps_theorem_and_execution_layers_separate(self) -> None:
        self.assertEqual(len(self.contract["source_chain"]), 3)
        self.assertEqual(
            self.contract["finite_volume_hyperbolic_status"],
            "PROVED_BY_SOURCE_CHAIN",
        )
        self.assertEqual(
            self.contract["nonarithmetic_status"], "PROVED_BY_SOURCE_CHAIN"
        )
        self.assertEqual(
            self.contract["local_interval_verification"],
            "NOT_RUN_SAGEMATH_INTERVAL_BACKEND_UNAVAILABLE",
        )

    def test_high_precision_invariants_remain_numerical(self) -> None:
        numerical = self.invariants["numerical_invariants"]
        self.assertEqual(
            numerical["status"],
            "HIGH_PRECISION_NUMERICAL_OBSERVATION_NOT_INTERVAL_VERIFIED",
        )
        self.assertGreater(float(numerical["volume"]), 0.0)
        self.assertGreater(float(numerical["cusp_shape_im"]), 0.0)
        self.assertEqual(len(numerical["tetrahedron_shapes"]), 3)
        for shape in numerical["tetrahedron_shapes"]:
            self.assertGreater(float(shape["shape_im"]), 0.0)

    def test_frozen_primary_primitive_length_ledger(self) -> None:
        self.assertEqual(len(self.length_rows), 18)
        self.assertEqual(sum(int(row["multiplicity"]) for row in self.length_rows), 31)
        lengths = [float(row["length_re"]) for row in self.length_rows]
        self.assertEqual(lengths, sorted(lengths))
        self.assertTrue(all(0.0 < length < control.PRIMARY_LENGTH_CUTOFF for length in lengths))

    def test_complex_holonomy_and_psl_trace_squared_are_retained(self) -> None:
        self.assertTrue(any(abs(float(row["holonomy_angle"])) > 0.1 for row in self.length_rows))
        for row in self.length_rows:
            self.assertEqual(row["target_data_used"], "false")
            self.assertEqual(row["arithmetic_owner"], "NONE_CONTROL_IS_NONARITHMETIC")
            self.assertTrue(row["psl_trace_squared_re"])
            self.assertTrue(row["psl_trace_squared_im"])
            self.assertIn("NOT_INTERVAL_VERIFIED", row["primitive_status"])

    def test_independent_length_algorithms_agree_on_prefix(self) -> None:
        self.assertEqual(len(self.cross_rows), 9)
        self.assertEqual(self.metrics["crosscheck_groups"], 6)
        self.assertTrue(self.metrics["multiplicity_vector_agrees"])
        self.assertLess(
            self.metrics["maximum_absolute_complex_length_residual"], 1e-25
        )

    def test_route_and_forbidden_data_boundaries_are_preserved(self) -> None:
        self.assertFalse(self.metrics["forbidden_target_data_used"])
        self.assertEqual(self.metrics["formal_route_a_tuple"], "UNASSIGNED")
        self.assertEqual(self.metrics["a2_a4_evaluation"], "NOT_EVALUATED")
        self.assertEqual(self.metrics["route_b_evaluation"], "NOT_RUN")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertEqual(self.metrics["gates_a_e"], "NOT_REACHED")

    def test_render_is_byte_deterministic_within_process(self) -> None:
        first = control.rendered_outputs()
        second = control.rendered_outputs()
        self.assertEqual(first, second)
        first_core = {path: data for path, data in first.items() if path != control.RECEIPT_PATH}
        second_core = {path: data for path, data in second.items() if path != control.RECEIPT_PATH}
        self.assertEqual(control.combined_hash(first_core), control.combined_hash(second_core))


if __name__ == "__main__":
    unittest.main()
