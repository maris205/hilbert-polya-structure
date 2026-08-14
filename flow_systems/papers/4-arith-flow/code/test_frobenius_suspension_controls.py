#!/usr/bin/env python3
import csv
import json
import math
import tempfile
import unittest
from pathlib import Path

from frobenius_suspension_controls import (
    affine_irreducible_count_formula,
    circle_compiler_log_product,
    clock_intersection_solutions,
    continued_zeta_p1,
    fixed_point_count_p1_f2,
    irreducible_polynomials_f2,
    is_irreducible_f2,
    moebius,
    orbit_product_coefficients,
    partial_orbit_log,
    poly_gcd,
    poly_mod,
    poly_multiply,
    poly_power_mod,
    poly_to_string,
    projective_closed_point_count,
    rational_p1_coefficients,
    recovered_fixed_point_count,
    run,
)


class FinitePolynomialArithmeticTest(unittest.TestCase):
    def test_render_and_arithmetic(self) -> None:
        self.assertEqual(poly_to_string(0b1011), "x^3+x+1")
        self.assertEqual(poly_multiply(0b11, 0b11), 0b101)
        self.assertEqual(poly_mod(0b101, 0b11), 0)
        self.assertEqual(poly_gcd(0b101, 0b11), 0b11)
        self.assertEqual(poly_power_mod(0b10, 4, 0b111), 0b10)

    def test_known_irreducibles(self) -> None:
        self.assertTrue(is_irreducible_f2(0b10))
        self.assertTrue(is_irreducible_f2(0b11))
        self.assertTrue(is_irreducible_f2(0b111))
        self.assertTrue(is_irreducible_f2(0b1011))
        self.assertTrue(is_irreducible_f2(0b1101))
        self.assertFalse(is_irreducible_f2(0b101))
        self.assertFalse(is_irreducible_f2(0b1001))

    def test_irreducible_lists_and_counts(self) -> None:
        self.assertEqual(irreducible_polynomials_f2(1), [0b10, 0b11])
        self.assertEqual(irreducible_polynomials_f2(2), [0b111])
        self.assertEqual(
            irreducible_polynomials_f2(3), [0b1011, 0b1101]
        )
        expected = [2, 1, 2, 3, 6, 9, 18, 30]
        observed = [
            len(irreducible_polynomials_f2(degree))
            for degree in range(1, 9)
        ]
        self.assertEqual(observed, expected)
        self.assertEqual(
            observed,
            [affine_irreducible_count_formula(degree) for degree in range(1, 9)],
        )

    def test_moebius(self) -> None:
        self.assertEqual([moebius(n) for n in range(1, 11)], [1, -1, -1, 0, -1, 1, -1, 0, 0, 1])


class FrobeniusLedgerTest(unittest.TestCase):
    @staticmethod
    def closed_counts(max_degree: int) -> dict[int, int]:
        return {
            degree: projective_closed_point_count(
                degree, affine_irreducible_count_formula(degree)
            )
            for degree in range(1, max_degree + 1)
        }

    def test_p1_closed_point_counts(self) -> None:
        counts = self.closed_counts(8)
        self.assertEqual(counts[1], 3)
        self.assertEqual([counts[d] for d in range(2, 9)], [1, 2, 3, 6, 9, 18, 30])

    def test_fixed_points_recovered_from_primitive_cycles(self) -> None:
        counts = self.closed_counts(12)
        for extension_degree in range(1, 13):
            self.assertEqual(
                recovered_fixed_point_count(extension_degree, counts),
                fixed_point_count_p1_f2(extension_degree),
            )

    def test_formal_orbit_product_matches_rational_zeta(self) -> None:
        max_order = 12
        counts = self.closed_counts(max_order)
        self.assertEqual(
            orbit_product_coefficients(max_order, counts),
            rational_p1_coefficients(max_order),
        )

    def test_convergence_regression(self) -> None:
        counts = self.closed_counts(12)
        for sigma in (0.75, 1.0, 1.25, 2.0):
            partials = [
                partial_orbit_log(sigma, cutoff, counts)
                for cutoff in (2, 4, 6, 8, 10, 12)
            ]
            self.assertTrue(all(right > left for left, right in zip(partials, partials[1:])))
        exact_log = -math.log1p(-(2.0 ** -2.0)) - math.log1p(-(2.0 ** -1.0))
        # The omitted primitive-degree tail at cutoff 12 is small but not zero;
        # this is a convergence regression, not a finite exact-identity claim.
        self.assertLess(abs(partial_orbit_log(2.0, 12, counts) - exact_log), 2e-5)

    def test_imaginary_periodicity(self) -> None:
        s_value = complex(1.5, 0.37)
        period = 2.0 * math.pi / math.log(2.0)
        reference = continued_zeta_p1(s_value)
        for multiple in range(-4, 5):
            observed = continued_zeta_p1(s_value + 1j * multiple * period)
            self.assertLess(abs(observed - reference), 2e-13)


class AdversarialControlTest(unittest.TestCase):
    def test_clock_grid_has_only_same_characteristic_solutions(self) -> None:
        rows = clock_intersection_solutions()
        self.assertGreater(len(rows), 0)
        for row in rows:
            self.assertEqual(row["characteristic"], row["target_prime"])
            self.assertEqual(
                row["field_exponent"] * row["orbit_degree"],
                row["target_repetition"],
            )

    def test_arbitrary_circle_compiler_identity(self) -> None:
        lengths = [0.5, math.sqrt(2.0), math.pi / 2.0, 2.75]
        for sigma in (0.75, 1.25, 2.0):
            observed = circle_compiler_log_product(lengths, sigma)
            expected = math.log(
                math.prod(
                    (1.0 - math.exp(-sigma * length)) ** -1
                    for length in lengths
                )
            )
            self.assertAlmostEqual(observed, expected, places=14)

    def test_nonpositive_compiler_length_rejected(self) -> None:
        with self.assertRaises(ValueError):
            circle_compiler_log_product([1.0, 0.0], 2.0)


class ArtifactTest(unittest.TestCase):
    def test_run_writes_complete_self_consistent_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output_dir = Path(temporary)
            manifest = run(output_dir, max_degree=8)
            self.assertTrue(manifest["all_moebius_counts_match"])
            self.assertTrue(manifest["all_fixed_point_ledgers_match"])
            self.assertTrue(manifest["all_formal_zeta_coefficients_match"])
            self.assertTrue(manifest["all_clock_solutions_same_characteristic"])
            self.assertEqual(
                manifest["route_a_native"]["overall"],
                "ROUTE_A_SUCCESS_ROUTE_B_NOT_READY",
            )
            self.assertEqual(
                manifest["route_a_riemann_target"]["a1"],
                "A1_PASS_ANALYTIC",
            )
            self.assertEqual(
                manifest["route_a_riemann_target"]["overall"],
                "ROUTE_A_REJECTED",
            )
            self.assertEqual(
                manifest["route_a_tautological_compiler"]["adversarial_verdict"],
                "STOP_SCOPED / PROVES_TOO_MUCH",
            )
            self.assertFalse(manifest["route_b_invocation_allowed"])
            for artifact_name, expected_hash in manifest["artifacts"].items():
                artifact_path = output_dir / artifact_name
                self.assertTrue(artifact_path.is_file())
                self.assertEqual(len(expected_hash), 64)
            stored_manifest = json.loads(
                (output_dir / "frobenius_suspension_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(stored_manifest, manifest)
            with (output_dir / "closed_point_ledger.csv").open(
                newline="", encoding="utf-8"
            ) as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 8)
            self.assertTrue(all(row["count_match"] == "True" for row in rows))
            self.assertTrue(
                all(row["fixed_point_match"] == "True" for row in rows)
            )


if __name__ == "__main__":
    unittest.main()
