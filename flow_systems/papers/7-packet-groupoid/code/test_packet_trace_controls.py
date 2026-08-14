#!/usr/bin/env python3
"""Regression tests for the deterministic Paper 7 control package."""

from __future__ import annotations

import csv
import json
import math
import shutil
import tempfile
import unittest
from pathlib import Path

from packet_trace_controls import (
    DEFAULT_MAX_PRIME,
    POISSON_LENGTHS,
    RIEMANN_LENGTHS,
    _clock_compiler_rows,
    _hilbert_vs_tau_rows,
    _probability_base_rows,
    _zero_time_rows,
    compiled_d_product,
    compiled_z_product,
    determinant_reciprocal_control,
    deterministic_mass,
    log_z_exact,
    log_z_partial,
    poisson_control,
    prime_power_decomposition,
    primes_up_to,
    run,
    tau_log_d_exact,
    trace_norm_riemann_control,
    verify,
    von_mangoldt,
)


class ArithmeticLedgerTests(unittest.TestCase):
    def test_prime_sieve(self) -> None:
        self.assertEqual(primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_prime_power_classification(self) -> None:
        self.assertEqual(prime_power_decomposition(2), (2, 1))
        self.assertEqual(prime_power_decomposition(64), (2, 6))
        self.assertEqual(prime_power_decomposition(81), (3, 4))
        self.assertEqual(prime_power_decomposition(125), (5, 3))
        self.assertIsNone(prime_power_decomposition(1))
        self.assertIsNone(prime_power_decomposition(12))
        self.assertIsNone(prime_power_decomposition(225))

    def test_von_mangoldt_ledger(self) -> None:
        self.assertAlmostEqual(von_mangoldt(8), math.log(2.0))
        self.assertAlmostEqual(von_mangoldt(49), math.log(7.0))
        self.assertEqual(von_mangoldt(12), 0.0)


class FourierConventionTests(unittest.TestCase):
    def test_poisson_convention_at_all_frozen_lengths(self) -> None:
        for length in POISSON_LENGTHS:
            with self.subTest(length=length):
                control = poisson_control(length)
                self.assertLess(float(control["absolute_error"]), 1.0e-12)

    def test_poisson_rejects_nonpositive_length(self) -> None:
        with self.assertRaises(ValueError):
            poisson_control(0.0)

    def test_trace_norm_has_preregistered_scaling(self) -> None:
        controls = [trace_norm_riemann_control(length) for length in RIEMANN_LENGTHS]
        self.assertGreater(float(controls[0]["absolute_error"]), 1.0)
        self.assertLess(float(controls[-1]["absolute_error"]), 1.0e-12)
        self.assertAlmostEqual(
            float(controls[-1]["trace_norm_over_length"]), 1.0, places=12
        )

    def test_trace_norm_is_unscaled_and_grows_with_length(self) -> None:
        at_eight = trace_norm_riemann_control(8.0)
        at_sixteen = trace_norm_riemann_control(16.0)
        self.assertGreater(float(at_sixteen["trace_norm"]), float(at_eight["trace_norm"]))
        self.assertAlmostEqual(float(at_sixteen["trace_norm"]), 16.0, places=12)


class TraceLogTests(unittest.TestCase):
    def test_log_z_tau_log_d_sign_and_d_z_reciprocal(self) -> None:
        lengths = [math.log(prime) for prime in (2, 3, 5, 7)]
        masses = [1.0] * len(lengths)
        quantities = determinant_reciprocal_control(lengths, masses, 2.0)
        self.assertGreater(quantities["log_Z"], 0.0)
        self.assertLess(quantities["tau_Log_D"], 0.0)
        self.assertAlmostEqual(
            quantities["log_Z"], -quantities["tau_Log_D"], places=15
        )
        self.assertAlmostEqual(
            tau_log_d_exact(lengths, masses, 2.0),
            -log_z_exact(lengths, masses, 2.0),
            places=15,
        )
        self.assertAlmostEqual(quantities["D"] * quantities["Z"], 1.0, places=15)
        self.assertAlmostEqual(
            compiled_d_product(lengths, masses, 2.0)
            * compiled_z_product(lengths, masses, 2.0),
            1.0,
            places=15,
        )
        self.assertEqual(quantities["sign_residual"], 0.0)
        self.assertLess(quantities["reciprocal_residual"], 1.0e-15)

    def test_repetition_ledger_increases_to_exact_log_z(self) -> None:
        lengths = [math.log(2.0), math.log(3.0)]
        masses = [1.0, 1.0]
        partials = [
            log_z_partial(lengths, masses, 1.25, cutoff)
            for cutoff in (1, 2, 4, 8, 16, 32)
        ]
        exact = log_z_exact(lengths, masses, 1.25)
        self.assertTrue(all(left < right for left, right in zip(partials, partials[1:])))
        self.assertTrue(all(partial < exact for partial in partials))
        self.assertLess(exact - partials[-1], 1.0e-11)

    def test_positive_mass_perturbation_and_copy_are_linear(self) -> None:
        length = [math.log(5.0)]
        mass = deterministic_mass("clock_decay", 5, 2)
        single = log_z_exact(length, [mass], 2.0)
        copied = log_z_exact(length * 3, [mass] * 3, 2.0)
        self.assertGreater(mass, 0.0)
        self.assertAlmostEqual(copied, 3.0 * single, places=15)

    def test_invalid_clock_or_mass_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            log_z_exact([1.0], [-1.0], 2.0)
        with self.assertRaises(ValueError):
            log_z_exact([0.0], [1.0], 2.0)
        with self.assertRaises(ValueError):
            log_z_exact([1.0], [1.0, 2.0], 2.0)


class FalsificationControlTests(unittest.TestCase):
    def test_probability_base_blindness(self) -> None:
        rows = _probability_base_rows()
        self.assertEqual(len(rows), 4)
        self.assertEqual({row["total_probability_exact"] for row in rows}, {"1"})
        self.assertEqual({row["tau_zero_mode_projection"] for row in rows}, {"1"})
        self.assertEqual({row["difference_from_singleton"] for row in rows}, {"0"})

    def test_arbitrary_and_composite_clocks_compile(self) -> None:
        rows = _clock_compiler_rows()
        self.assertEqual({row["analytic_compiles"] for row in rows}, {"true"})
        for row in rows:
            self.assertLess(float(row["sign_residual"]), 1.0e-14)
            self.assertLess(float(row["reciprocal_residual"]), 1.0e-14)
            self.assertLess(float(row["D_product_residual"]), 1.0e-14)
            self.assertLess(float(row["Z_product_residual"]), 1.0e-14)
        composite = next(row for row in rows if row["clock_system"] == "composite_augmented")
        self.assertEqual(composite["composite_label_count"], 2)
        self.assertIn("provenance fails", str(composite["provenance_status"]))

    def test_ordinary_hilbert_multiplicity_differs_from_finite_tau(self) -> None:
        rows = _hilbert_vs_tau_rows()
        finite = rows[:-1]
        self.assertEqual({row["finite_tau_projection"] for row in rows}, {"1"})
        self.assertEqual(
            [row["ordinary_Hilbert_trace_I_tensor_P0"] for row in finite],
            [1, 2, 4, 16, 256],
        )
        self.assertEqual(rows[-1]["ordinary_Hilbert_trace_I_tensor_P0"], "infinite")

    def test_zero_time_partial_sums_are_strictly_increasing(self) -> None:
        primes = primes_up_to(DEFAULT_MAX_PRIME)
        rows = _zero_time_rows(primes, DEFAULT_MAX_PRIME)
        for model in ("unit", "rank_modulated"):
            model_rows = [row for row in rows if row["mass_model"] == model]
            sums = [float(row["partial_sum_m_p_log_p_f0"]) for row in model_rows]
            self.assertTrue(all(left < right for left, right in zip(sums, sums[1:])))
            self.assertEqual({row["monotone_positive"] for row in model_rows}, {"true"})


class ReproductionTests(unittest.TestCase):
    def test_outputs_manifest_and_byte_reproducibility(self) -> None:
        with tempfile.TemporaryDirectory() as first_tmp, tempfile.TemporaryDirectory() as second_tmp:
            first = Path(first_tmp)
            second = Path(second_tmp)
            first_manifest = run(first, 1_000)
            second_manifest = run(second, 1_000)
            self.assertEqual(first_manifest, second_manifest)
            self.assertEqual(len(first_manifest["artifacts"]), 9)
            self.assertEqual(first_manifest["regression_status"], "PASS")
            self.assertEqual(first_manifest["determinism"]["network"], False)
            self.assertEqual(first_manifest["determinism"]["randomness"], False)
            self.assertIn("finite_prime_d_z_ledger.csv", first_manifest["artifacts"])
            self.assertNotIn("finite_prime_trace_log.csv", first_manifest["artifacts"])
            for filename in (*first_manifest["artifacts"].keys(), "packet_trace_manifest.json"):
                self.assertEqual((first / filename).read_bytes(), (second / filename).read_bytes())
            with (first / "finite_prime_d_z_ledger.csv").open(
                "r", encoding="utf-8", newline=""
            ) as handle:
                fieldnames = csv.DictReader(handle).fieldnames
            self.assertIsNotNone(fieldnames)
            self.assertTrue(
                {
                    "tau_Log_D",
                    "log_Z",
                    "D",
                    "Z",
                    "sign_residual",
                    "reciprocal_residual",
                }.issubset(set(fieldnames or ()))
            )
            self.assertEqual(verify(first), first_manifest)

    def test_manifest_detects_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = run(output, 100)
            filename = next(iter(manifest["artifacts"]))
            path = output / filename
            path.write_bytes(path.read_bytes() + b"tamper\n")
            with self.assertRaises(ValueError):
                verify(output)

    def test_manifest_contains_no_timestamp_or_external_data_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output, 100)
            manifest = json.loads(
                (output / "packet_trace_manifest.json").read_text(encoding="utf-8")
            )
            self.assertFalse(manifest["determinism"]["timestamps"])
            self.assertFalse(manifest["determinism"]["external_datasets"])
            self.assertEqual(
                manifest["determinism"]["python_dependencies"],
                "standard_library_only",
            )

    def test_manifest_rejects_tampered_implementation_in_complete_copy(self) -> None:
        source_paper = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copied_paper = Path(tmp) / "paper7-copy"
            for directory in ("code", "experiments", "results"):
                shutil.copytree(
                    source_paper / directory,
                    copied_paper / directory,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
                )
            output = copied_paper / "results"
            manifest = run(output, 100, paper_dir=copied_paper)
            self.assertEqual(verify(output, paper_dir=copied_paper), manifest)
            copied_readme = copied_paper / "code" / "README.md"
            copied_readme.write_text(
                copied_readme.read_text(encoding="utf-8") + "\ntampered copy\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                ValueError, "implementation SHA-256 mismatch"
            ):
                verify(output, paper_dir=copied_paper)

    def test_manifest_rejects_missing_implementation_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output, 100)
            manifest_path = output / "packet_trace_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["implementation_files"].pop("code/README.md")
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "file set mismatch"):
                verify(output)

    def test_manifest_rejects_extra_implementation_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output, 100)
            manifest_path = output / "packet_trace_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["implementation_files"]["results/packet_trace_manifest.json"] = (
                "0" * 64
            )
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "file set mismatch"):
                verify(output)


if __name__ == "__main__":
    unittest.main()
