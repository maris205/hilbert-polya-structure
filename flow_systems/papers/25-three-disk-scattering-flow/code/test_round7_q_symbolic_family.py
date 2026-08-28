#!/usr/bin/env python3
import json
import unittest

import round7_q_symbolic_family as family


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    size = len(work)
    if size == 1:
        return work[0][0]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size) if work[row][pivot_index]),
                None,
            )
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column]
                if numerator % previous:
                    raise AssertionError("Bareiss division lost exactness")
                work[row][column] = numerator // previous
        previous = pivot
    return sign * work[-1][-1]


def evaluate_polynomial(coefficients: list[int], value: int) -> int:
    return sum(coefficient * value**degree for degree, coefficient in enumerate(coefficients))


class QSymbolicFamilyRound7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = family.load_freeze()
        cls.counts, cls.prefix, cls.summary = family.build_payload()

    def test_01_freeze_is_pinned_and_target_free(self) -> None:
        self.assertEqual(family.sha256(self.freeze_raw), family.FREEZE_SHA256)
        self.assertEqual(tuple(self.freeze["finite_replay"]["q_values"]), family.Q_VALUES)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))

    def test_02_closed_traces_match_direct_integer_matrix_powers(self) -> None:
        for q in family.Q_VALUES:
            direct = family.direct_traces(q, family.MAX_DEGREE)
            expected = [family.closed_trace(q, degree) for degree in range(1, family.MAX_DEGREE + 1)]
            self.assertEqual(direct, expected)

    def test_03_mobius_counts_recover_known_q2_and_q3_cases(self) -> None:
        self.assertEqual(
            [family.primitive_count(2, n) for n in range(1, 13)],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )
        self.assertEqual(
            [family.primitive_count(3, n) for n in range(1, 13)],
            [0, 3, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335],
        )

    def test_04_all_finite_replay_primitive_counts_are_nonnegative_integers(self) -> None:
        self.assertEqual(len(self.counts), 7 * 12)
        self.assertTrue(all(row["primitive_count_nonnegative_integer"] == "true" for row in self.counts))
        self.assertTrue(all(row["trace_match"] == "true" for row in self.counts))

    def test_05_q3_denominators_recover_round6(self) -> None:
        self.assertEqual(family.determinant_denominator(3, 1), [1, 0, -3, -2])
        self.assertEqual(family.determinant_denominator(3, -1), [1, 0, -3, 2])

    def test_06_closed_determinants_match_direct_bareiss_evaluations(self) -> None:
        for q in family.Q_VALUES:
            adjacency = family.adjacency_matrix(q)
            for step_weight in (1, -1):
                coefficients = family.determinant_denominator(q, step_weight)
                for z_value in (-2, -1, 0, 1, 2):
                    matrix = [
                        [
                            int(row == column) - step_weight * z_value * adjacency[row][column]
                            for column in range(q)
                        ]
                        for row in range(q)
                    ]
                    self.assertEqual(
                        bareiss_determinant(matrix),
                        evaluate_polynomial(coefficients, z_value),
                    )

    def test_07_euler_trace_and_determinant_prefixes_match(self) -> None:
        self.assertTrue(all(row["all_exactly_equal"] == "true" for row in self.prefix))
        self.assertEqual(self.summary["three_construction_coefficient_mismatch_count"], 0)

    def test_08_collision_phase_is_exact_substitution_for_every_q(self) -> None:
        grouped: dict[tuple[str, str], dict[int, str]] = {}
        for row in self.prefix:
            grouped.setdefault((row["q"], row["step_weight_u"]), {})[int(row["degree"])] = row[
                "reciprocal_determinant_coefficient"
            ]
        for q in map(str, family.Q_VALUES):
            for degree, positive in grouped[(q, "1")].items():
                expected = positive if degree % 2 == 0 else str(-int(positive))
                self.assertEqual(grouped[(q, "-1")][degree], expected)

    def test_09_frozen_replay_row_counts_and_theorem_domain_are_explicit(self) -> None:
        self.assertEqual(self.summary["count_rows"], 84)
        self.assertEqual(self.summary["prefix_rows"], 182)
        self.assertEqual(self.summary["parameter_domain_theorem"], "INTEGER_Q_AT_LEAST_2")
        self.assertEqual(self.summary["finite_replay_q_values"], list(range(2, 9)))
        self.assertEqual(self.summary["finite_replay_evidence_status"], "NUMERICALLY_CERTIFIED")
        self.assertEqual(self.summary["finite_replay_arithmetic_mode"], "EXACT_INTEGER_RATIONAL")

    def test_10_route_tuple_and_physical_flow_firewall_are_intact(self) -> None:
        self.assertEqual(
            self.summary["formal_route_a_tuple"],
            ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"],
        )
        self.assertEqual(self.summary["overall_verdict"], "ROUTE_A_REJECTED")
        self.assertEqual(self.summary["physical_three_disk_route_tuple"], "UNASSIGNED")
        self.assertFalse(self.summary["route_b_invocation_allowed"])
        self.assertFalse(self.summary["prime_or_zero_tables_used"])

    def test_11_render_is_byte_deterministic_and_source_bound(self) -> None:
        first = family.rendered_outputs()
        second = family.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[family.RECEIPT_PATH])
        for relative, binding in receipt["source_bindings"].items():
            payload = (family.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], family.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))

    def test_12_receipt_binds_every_core_output_and_hash(self) -> None:
        rendered = family.rendered_outputs()
        core = {path: rendered[path] for path in family.RESULT_PATHS.values()}
        receipt = json.loads(rendered[family.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], family.combined_hash(core))
        for path, payload in core.items():
            self.assertEqual(receipt["files"][path.as_posix()]["sha256"], family.sha256(payload))
            self.assertEqual(receipt["files"][path.as_posix()]["bytes"], len(payload))
        validation = rendered[family.VALIDATION_PATH]
        self.assertEqual(receipt["validation_binding"]["sha256"], family.sha256(validation))
        self.assertEqual(receipt["validation_binding"]["bytes"], len(validation))


if __name__ == "__main__":
    unittest.main()
