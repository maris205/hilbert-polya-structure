from __future__ import annotations

import json
import math
import shutil
import tempfile
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import independent_check
import s_arithmetic_clock as clock


class Quad3Tests(unittest.TestCase):
    def test_generator_norms_and_inverses(self):
        self.assertEqual(clock.EPSILON.norm(), 1)
        self.assertEqual(clock.PI.norm(), 13)
        self.assertEqual(clock.EPSILON * clock.EPSILON.inverse(), clock.Quad3(1))
        self.assertEqual(clock.PI * clock.PI.inverse(), clock.Quad3(1))

    def test_regular_matrix_representation(self):
        value = clock.Quad3(Fraction(7, 13), Fraction(-5, 13))
        matrix = value.matrix()
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        self.assertEqual(determinant, value.norm())

    def test_hilbert_symbols(self):
        self.assertEqual(clock.hilbert_symbol_two(-1, 3), -1)
        self.assertEqual(clock.hilbert_symbol_odd(-1, 3, 3), -1)
        self.assertEqual(clock.hilbert_symbol_odd(-1, 3, 13), 1)


class ClockTests(unittest.TestCase):
    def test_exact_invariant_length_formula(self):
        for m, n in [(1, 0), (0, 1), (1, -1), (-1, 2), (-6, 17)]:
            row = clock.element_certificate(m, n)
            self.assertTrue(row["norm_matches_13_power"])
            self.assertTrue(row["matrix_determinant_matches_norm"])
            self.assertEqual(row["tree_length_from_trace_norm"], abs(n))

    def test_iteration_and_primitivity(self):
        base = clock.element(2, 3)
        self.assertEqual(base**4, clock.element(8, 12))
        self.assertTrue(clock.canonical_primitive(-2, 3))
        self.assertFalse(clock.canonical_primitive(-4, 6))
        self.assertFalse(clock.canonical_primitive(2, -3))

    def test_rank_two_determinant(self):
        real_unit, _ = clock.clock_constants()
        self.assertGreater(real_unit, 0.0)
        self.assertAlmostEqual(real_unit, 2.633915793849633, places=14)

    def test_near_wall_records(self):
        records = clock.record_near_wall(400)
        lookup = {(row["m"], row["n"]): row for row in records}
        for pair in [(-6, 17), (-19, 54), (-44, 125), (-113, 321)]:
            self.assertIn(pair, lookup)
        selected = [lookup[pair] for pair in [(-6, 17), (-19, 54), (-44, 125), (-113, 321)]]
        self.assertTrue(
            all(selected[i + 1]["real_length"] < selected[i]["real_length"] for i in range(3))
        )
        self.assertTrue(
            all(selected[i + 1]["height"] > selected[i]["height"] for i in range(3))
        )

    def test_box_counts(self):
        self.assertEqual(clock.primitive_box_count(10, 10), 48)
        self.assertEqual(clock.primitive_box_count(40, 40), 742)
        count, margin = clock.primitive_box_count_details(320, 320)
        self.assertEqual(count, 47349)
        self.assertGreater(margin, 0)

    def test_height_counts(self):
        self.assertEqual(clock.primitive_height_count(20), 36)
        self.assertEqual(clock.primitive_height_count(80), 577)
        count, margin = clock.primitive_height_count_details(640)
        self.assertEqual(count, 36857)
        self.assertGreater(margin, 0)

    def test_height_identity_for_model_coordinates(self):
        # Recompute 2h(r) from the primitive integer minimal polynomial of
        # r=alpha/alpha', rather than defining h by the claimed clock formula.
        with localcontext() as context:
            context.prec = 80
            root3 = Decimal(3).sqrt()
            real_unit, split_unit, log_p = clock.decimal_clock_constants()
            for m, n in [(1, 0), (0, 1), (-6, 17), (5, -2)]:
                alpha = clock.element(m, n)
                ratio = alpha * alpha.conjugate().inverse()
                coefficients = [Fraction(1), -2 * ratio.a, Fraction(1)]
                scale = math.lcm(*(value.denominator for value in coefficients))
                integer_coefficients = [int(value * scale) for value in coefficients]
                common = math.gcd(*(abs(value) for value in integer_coefficients))
                integer_coefficients = [value // common for value in integer_coefficients]
                if integer_coefficients[0] < 0:
                    integer_coefficients = [-value for value in integer_coefficients]

                ratio_a = Decimal(ratio.a.numerator) / ratio.a.denominator
                ratio_b = Decimal(ratio.b.numerator) / ratio.b.denominator
                conjugates = (ratio_a + ratio_b * root3, ratio_a - ratio_b * root3)
                twice_height_from_polynomial = Decimal(integer_coefficients[0]).ln()
                for conjugate in conjugates:
                    twice_height_from_polynomial += max(Decimal(0), abs(conjugate).ln())

                clock_height = abs(Decimal(m) * real_unit + Decimal(n) * split_unit)
                clock_height += Decimal(abs(n)) * log_p
                self.assertLess(abs(twice_height_from_polynomial - clock_height), Decimal("1e-70"))


class ReproductionTests(unittest.TestCase):
    @staticmethod
    def rewrite_certificate(results: Path, mutate) -> None:
        path = results / "exact_certificates.json"
        certificate = json.loads(path.read_text(encoding="utf-8"))
        mutate(certificate)
        path.write_text(
            json.dumps(certificate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        manifest_path = results / "artifact_hashes.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest[path.name] = independent_check.digest(path)
        manifest_path.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def test_producer_and_independent_checker(self):
        with self.assertRaises(ValueError):
            independent_check.v13(Fraction(0))
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "baseline"
            clock.produce(results, near_wall_limit=1000)
            report = independent_check.check(results)
            self.assertTrue(report["all_passed"], report["checks"])
            self.assertEqual(report["check_count"], 16)

            mutations = Path(directory) / "mutations"
            mutations.mkdir()

            def case(name: str) -> Path:
                target = mutations / name
                shutil.copytree(results, target)
                return target

            empty_manifest = case("empty_manifest")
            (empty_manifest / "artifact_hashes.json").write_text("{}\n", encoding="utf-8")
            self.assertFalse(independent_check.check(empty_manifest)["all_passed"])

            missing_artifact = case("missing_artifact")
            (missing_artifact / "near_wall.csv").unlink()
            self.assertFalse(independent_check.check(missing_artifact)["all_passed"])

            empty_samples = case("empty_samples")
            self.rewrite_certificate(empty_samples, lambda cert: cert.update(sample_elements=[]))
            self.assertFalse(independent_check.check(empty_samples)["all_passed"])

            empty_near_wall = case("empty_near_wall")
            self.rewrite_certificate(empty_near_wall, lambda cert: cert.update(near_wall_records=[]))
            self.assertFalse(independent_check.check(empty_near_wall)["all_passed"])

            corrupt_generator = case("corrupt_generator")
            self.rewrite_certificate(
                corrupt_generator,
                lambda cert: cert["generators"]["epsilon"].update(a="999"),
            )
            corrupt_report = independent_check.check(corrupt_generator)
            self.assertFalse(corrupt_report["checks"]["generators_rederived"])
            self.assertTrue(corrupt_report["checks"]["artifact_hashes"])

            corrupt_table = case("corrupt_table")
            self.rewrite_certificate(
                corrupt_table,
                lambda cert: cert["primitive_box_counts"][0].update(count_mod_inverse=999),
            )
            table_report = independent_check.check(corrupt_table)
            self.assertFalse(table_report["checks"]["embedded_tables_match_csv"])
            self.assertFalse(table_report["checks"]["independent_box_rows"])

            duplicate_rows = case("duplicate_rows")
            csv_path = duplicate_rows / "primitive_box_counts.csv"
            lines = csv_path.read_text(encoding="utf-8").splitlines()
            csv_path.write_text("\n".join(lines + [lines[-1]]) + "\n", encoding="utf-8")
            duplicate_report = independent_check.check(duplicate_rows)
            self.assertFalse(duplicate_report["all_passed"])
            self.assertFalse(duplicate_report["checks"]["exact_schema"])

if __name__ == "__main__":
    unittest.main()
