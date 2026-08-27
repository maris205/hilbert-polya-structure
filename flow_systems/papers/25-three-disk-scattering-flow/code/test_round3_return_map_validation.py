#!/usr/bin/env python3
import inspect
import math
import unittest

import mpmath as mp

import round3_return_map_validation as round3


class ThreeDiskRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mp.mp.dps = round3.MP_DPS
        cls.project_root = __import__("pathlib").Path(__file__).resolve().parents[1]
        _path, cls.source_rows = round3.read_source_rows(cls.project_root)

    def direct_check(self, row_index: int) -> tuple[dict[str, str], dict[str, str]]:
        source = self.source_rows[row_index]
        result = round3.validate_row(source)
        self.assertEqual(result["validation_status"], "NUMERICALLY_CERTIFIED")
        return source, result

    def test_round2_source_contract_is_frozen(self) -> None:
        self.assertEqual(len(self.source_rows), 2241)
        self.assertEqual(
            sum(row["finite_difference_validation_status"] == "NUMERICALLY_CERTIFIED" for row in self.source_rows),
            9,
        )

    def test_two_disk_direct_trace_is_positive_98(self) -> None:
        source, result = self.direct_check(747)  # d/a=6.0, word 01
        self.assertEqual(source["cyclic_word"], "01")
        self.assertAlmostEqual(float(result["direct_trace_h1e_36"]), 98.0, places=10)
        self.assertLess(float(result["determinant_residual_h1e_36"]), 1e-30)

    def test_odd_word_has_physical_orientation_sign(self) -> None:
        odd_index = next(
            index for index, row in enumerate(self.source_rows)
            if len(row["cyclic_word"]) == 5
        )
        source, result = self.direct_check(odd_index)
        direct_trace = float(result["direct_trace_h1e_36"])
        self.assertLess(direct_trace, 0.0)
        self.assertAlmostEqual(
            abs(direct_trace) / float(source["monodromy_trace"]), 1.0, places=12
        )

    def test_long_word_closes_binary64_conditioning_gap(self) -> None:
        source, result = self.direct_check(len(self.source_rows) - 1)
        self.assertEqual(len(source["cyclic_word"]), 12)
        self.assertGreater(abs(float(result["direct_trace_h1e_36"])), 1e12)
        self.assertLess(float(result["multiscale_trace_relative_span"]), 1e-18)
        self.assertLess(float(result["determinant_residual_h1e_36"]), 1e-18)
        self.assertLess(float(result["half_density_relative_residual"]), 2e-12)

    def test_condition_aware_stationarity_fallback_stays_independent(self) -> None:
        row_index = next(
            index
            for index, row in enumerate(self.source_rows)
            if row["row_id"] == "Dcb691d445461acef"
        )
        _source, result = self.direct_check(row_index)
        self.assertEqual(result["refinement_method"], "SPECULAR_STATIONARITY_FALLBACK")
        self.assertLess(float(result["fallback_stationarity_residual"]), 1e-70)
        self.assertLess(float(result["post_refinement_return_residual"]), 1e-60)

    def test_direct_jacobian_api_has_no_analytic_trace_input(self) -> None:
        parameters = inspect.signature(round3.central_difference_jacobian).parameters
        self.assertEqual(list(parameters), ["state", "word", "distance_ratio", "step"])
        source = inspect.getsource(round3.central_difference_jacobian)
        self.assertNotIn("paraxial", source.lower())
        self.assertNotIn("analytic_trace", source)

    def test_no_target_data_dependency_or_route_promotion(self) -> None:
        source = inspect.getsource(round3)
        input_reader = inspect.getsource(round3.read_source_rows)
        self.assertIn("three_disk_primitive_ledger_round2.csv", input_reader)
        self.assertNotIn("controls", input_reader)
        self.assertNotIn("prime", input_reader.lower())
        self.assertNotIn("zero", input_reader.lower())
        self.assertIn('"formal_a0_a4_tuple": "UNASSIGNED"', source)
        self.assertIn('"route_b_invocation_allowed": False', source)
        self.assertTrue(math.isclose(float(round3.PARITY_TRACE_RELATIVE_RESIDUAL_LIMIT), 2e-12))


if __name__ == "__main__":
    unittest.main()
