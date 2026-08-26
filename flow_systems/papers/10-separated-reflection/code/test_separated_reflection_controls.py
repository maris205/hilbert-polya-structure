#!/usr/bin/env python3
"""Unit and reproduction tests for Paper 10 deterministic controls."""

from __future__ import annotations

import ast
import json
import os
import shutil
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from separated_reflection_controls import (
    ARTIFACT_FILENAMES,
    CHARACTER_TARGET_ORDERS,
    COMPONENT_COUNTS,
    ELL1_PREFIX_LENGTHS,
    EXPECTED_ACTIVE_TUPLE_HASHES,
    IMPLEMENTATION_RELATIVE_PATHS,
    LOG_EXPONENT_LEVELS,
    MEASURABLE_TARGET_SIZES,
    SOURCE_SIZES,
    _component_mass_rows,
    _continuous_map_rows,
    _coproduct_rows,
    _dirac_rows,
    _ell1_rows,
    _external_log_rows,
    _group_character_rows,
    _label_neutrality_rows,
    _measurable_map_rows,
    _proxy_direction_rows,
    copied_coproduct,
    discrete_topology,
    generated_sigma_algebra,
    indiscrete_topology,
    is_continuous,
    is_measurable,
    is_prime,
    is_t0,
    next_prime_greater_than,
    powerset,
    run,
    sha256,
    sierpinski_topology,
    verify,
)


class FiniteTopologyTests(unittest.TestCase):
    def test_target_separation_and_source_sizes(self) -> None:
        self.assertEqual(SOURCE_SIZES, (1, 2, 3, 5))
        self.assertTrue(is_t0(2, discrete_topology(2)))
        self.assertTrue(is_t0(2, sierpinski_topology()))
        self.assertFalse(is_t0(2, indiscrete_topology(2)))

    def test_exhaustive_topological_map_rows(self) -> None:
        rows = _continuous_map_rows()
        self.assertEqual(len(rows), 3 * sum(2**size for size in SOURCE_SIZES))
        self.assertEqual(len(rows), 138)
        self.assertEqual({row["expectation_match"] for row in rows}, {"true"})
        nonconstant_t0 = [
            row
            for row in rows
            if row["target_t0"] == "true"
            and row["continuous"] == "true"
            and row["constant"] == "false"
        ]
        self.assertEqual(nonconstant_t0, [])
        nonconstant_negative = [
            row
            for row in rows
            if row["target"] == "indiscrete_2_negative"
            and row["continuous"] == "true"
            and row["constant"] == "false"
        ]
        self.assertEqual(len(nonconstant_negative), 38)

    def test_continuity_checker_detects_direction(self) -> None:
        identity = (0, 1, 2)
        self.assertFalse(
            is_continuous(identity, indiscrete_topology(3), discrete_topology(3))
        )
        self.assertTrue(
            is_continuous(identity, discrete_topology(3), indiscrete_topology(3))
        )


class BorelMeasurableDiracTests(unittest.TestCase):
    def test_trivial_borel_sigma_algebra(self) -> None:
        for size in SOURCE_SIZES:
            borel = generated_sigma_algebra(size, indiscrete_topology(size))
            self.assertEqual(borel, indiscrete_topology(size))

    def test_exhaustive_measurable_map_rows(self) -> None:
        rows = _measurable_map_rows()
        expected = sum(
            target_size**source_size
            for source_size in SOURCE_SIZES
            for target_size in MEASURABLE_TARGET_SIZES
        )
        self.assertEqual(len(rows), expected)
        self.assertEqual(len(rows), 328)
        self.assertEqual({row["collapse_match"] for row in rows}, {"true"})
        self.assertFalse(
            any(
                row["measurable"] == "true" and row["constant"] == "false"
                for row in rows
            )
        )

    def test_measurability_checker_accepts_only_constants_for_trivial_source(self) -> None:
        source_sigma = indiscrete_topology(3)
        target_sigma = powerset((0, 1))
        self.assertTrue(is_measurable((1, 1, 1), source_sigma, target_sigma))
        self.assertFalse(is_measurable((0, 1, 0), source_sigma, target_sigma))

    def test_dirac_rows_are_equal_on_the_measurable_ledger(self) -> None:
        rows = _dirac_rows()
        self.assertEqual(len(rows), 2 * sum(size * size for size in SOURCE_SIZES))
        self.assertEqual(len(rows), 78)
        self.assertEqual({row["equal_on_event"] for row in rows}, {"true"})
        self.assertEqual(
            {row["equal_on_entire_borel_ledger"] for row in rows}, {"true"}
        )
        nontrivial = [row for row in rows if int(row["source_size"]) > 1]
        self.assertEqual(
            {row["proper_singleton_measurable"] for row in nontrivial}, {"false"}
        )
        self.assertEqual({row["dirac_domain"] for row in rows}, {"measurable_events_only"})


class GroupCharacterTests(unittest.TestCase):
    def test_indiscrete_group_operations_are_continuous_in_rows(self) -> None:
        rows = _group_character_rows()
        self.assertEqual(len(rows), 62)
        self.assertEqual({row["group_operations_continuous"] for row in rows}, {"true"})
        self.assertEqual(
            {int(row["target_order"]) for row in rows}, set(CHARACTER_TARGET_ORDERS)
        )

    def test_only_trivial_finite_characters_are_continuous(self) -> None:
        rows = _group_character_rows()
        continuous = [row for row in rows if row["continuous_actual_topology"] == "true"]
        self.assertTrue(continuous)
        self.assertEqual({row["nontrivial"] for row in continuous}, {"false"})
        negative = [
            row
            for row in rows
            if row["control_type"]
            == "algebraic_character_noncontinuous_negative"
        ]
        self.assertEqual(len(negative), 22)
        self.assertEqual({row["algebraic_homomorphism"] for row in negative}, {"true"})
        self.assertEqual({row["continuous_actual_topology"] for row in negative}, {"false"})

    def test_circle_mesh_is_explicitly_a_proxy(self) -> None:
        mesh = [
            row
            for row in _group_character_rows()
            if row["target_kind"] == "finite_circle_mesh_discrete_proxy"
        ]
        self.assertTrue(mesh)
        self.assertTrue(all("not a classification of the full circle" in row["scope"] for row in mesh))


class ProxyAndCoproductTests(unittest.TestCase):
    def test_proxy_directions_are_not_swapped(self) -> None:
        rows = _proxy_direction_rows()
        self.assertEqual(len(rows), 2 * len(SOURCE_SIZES))
        for row in rows:
            expected = (
                int(row["set_size"]) == 1
                or row["direction"]
                == "standard_discrete_proxy_to_actual_indiscrete"
            )
            self.assertEqual(row["continuous"], "true" if expected else "false")
            self.assertEqual(row["continuous"], row["expected_continuity"])

    def test_coproduct_open_borel_and_k0_counts(self) -> None:
        rows = _coproduct_rows()
        self.assertEqual(len(rows), len(COMPONENT_COUNTS))
        for row in rows:
            count = int(row["component_count"])
            self.assertEqual(int(row["topology_open_count"]), 2**count)
            self.assertEqual(int(row["borel_event_count"]), 2**count)
            self.assertEqual(int(row["k0_class_count"]), count)
            self.assertEqual(row["within_component_points_erased"], "true")
            self.assertEqual(row["distinct_labels_separated"], "true")

    def test_coproduct_classes_are_exact_components(self) -> None:
        for count in COMPONENT_COUNTS:
            model = copied_coproduct(count)
            expected_sizes = tuple(model["component_sizes"])
            class_sizes = tuple(len(group) for group in model["classes"])
            self.assertEqual(class_sizes, expected_sizes)
            self.assertEqual(len(model["borel"]), len(model["opens"]))


class MassAndEll1Tests(unittest.TestCase):
    def test_mass_vectors_include_zeros_and_same_total_distinct_ledgers(self) -> None:
        rows = _component_mass_rows()
        self.assertEqual(len(rows), len(COMPONENT_COUNTS) * 5)
        self.assertEqual({row["nonnegative"] for row in rows}, {"true"})
        self.assertEqual({row["finite_total"] for row in rows}, {"true"})
        self.assertEqual({row["topology_selects_weights"] for row in rows}, {"false"})
        for count in COMPONENT_COUNTS:
            selected = {
                row["profile"]: row
                for row in rows
                if int(row["component_count"]) == count
            }
            first = selected["unit_first"]
            last = selected["unit_last_same_total"]
            self.assertEqual(first["total_mass_exact"], last["total_mass_exact"])
            self.assertNotEqual(first["weights_exact"], last["weights_exact"])
            self.assertGreater(int(selected["all_zero"]["zero_component_count"]), 0)

    def test_ell1_prefixes_are_nonnegative_exact_and_nondecisive(self) -> None:
        rows = _ell1_rows()
        self.assertEqual(len(rows), 4 * len(ELL1_PREFIX_LENGTHS))
        self.assertEqual({row["all_terms_nonnegative"] for row in rows}, {"true"})
        self.assertEqual(
            {row["finite_prefix_decides_infinite_gate"] for row in rows}, {"false"}
        )
        geometric = {
            int(row["prefix_length"]): Fraction(row["prefix_sum_exact"])
            for row in rows
            if row["profile"] == "geometric_half"
        }
        for length, total in geometric.items():
            self.assertEqual(total, Fraction(1) - Fraction(1, 2**length))
        finite_support = [
            row
            for row in rows
            if row["profile"] == "finite_support_with_zeros"
            and int(row["prefix_length"]) >= 4
        ]
        self.assertEqual(
            {Fraction(row["prefix_sum_exact"]) for row in finite_support},
            {Fraction(7, 3)},
        )


class LabelAndLogTests(unittest.TestCase):
    def test_prime_composite_and_arbitrary_labels_are_structurally_neutral(self) -> None:
        rows = _label_neutrality_rows()
        self.assertEqual(len(rows), len(COMPONENT_COUNTS) * 3)
        self.assertEqual(
            {row["label_family"] for row in rows}, {"prime", "composite", "arbitrary"}
        )
        self.assertEqual(
            {row["abstract_mechanism_detects_primality"] for row in rows}, {"false"}
        )
        for count in COMPONENT_COUNTS:
            selected = [row for row in rows if int(row["component_count"]) == count]
            self.assertEqual(len({row["abstract_signature"] for row in selected}), 1)

    def test_external_log_witnesses_use_exact_integer_bounds(self) -> None:
        rows = _external_log_rows()
        self.assertEqual(len(rows), len(LOG_EXPONENT_LEVELS))
        previous_prime = 0
        for row in rows:
            bound = int(row["integer_bound_2_power_k"])
            prime = int(row["selected_prime_label"])
            self.assertTrue(is_prime(prime))
            self.assertEqual(prime, next_prime_greater_than(bound))
            self.assertGreater(prime, bound)
            self.assertGreater(prime, previous_prime)
            previous_prime = prime
            self.assertEqual(row["topology_selects_log_label"], "false")
            self.assertEqual(row["mass_ledger_selects_log_label"], "false")
            self.assertEqual(row["actual_source_observable_credit"], "false")


class ReproductionTests(unittest.TestCase):
    def test_outputs_manifest_and_two_generations_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as first_tmp, tempfile.TemporaryDirectory() as second_tmp:
            first = Path(first_tmp)
            second = Path(second_tmp)
            first_manifest = run(first)
            second_manifest = run(second)
            self.assertEqual(first_manifest, second_manifest)
            self.assertEqual(first_manifest["regression_status"], "PASS")
            self.assertEqual(set(first_manifest["artifacts"]), set(ARTIFACT_FILENAMES))
            for filename in (*ARTIFACT_FILENAMES, "separated_reflection_controls_manifest.json"):
                self.assertEqual((first / filename).read_bytes(), (second / filename).read_bytes())
            self.assertEqual(verify(first), first_manifest)
            self.assertEqual(verify(second), second_manifest)

    def test_manifest_detects_artifact_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            target = output / ARTIFACT_FILENAMES[0]
            target.write_bytes(target.read_bytes() + b"tamper\n")
            with self.assertRaisesRegex(ValueError, "artifact SHA-256 mismatch"):
                verify(output)

    def test_manifest_detects_implementation_tampering(self) -> None:
        source_paper = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copied_paper = Path(tmp) / "paper10-copy"
            for directory in ("code", "experiments", "results"):
                shutil.copytree(
                    source_paper / directory,
                    copied_paper / directory,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
                )
            (copied_paper / "notes").mkdir()
            for relative in EXPECTED_ACTIVE_TUPLE_HASHES:
                source = source_paper / relative
                destination = copied_paper / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
            output = copied_paper / "results"
            manifest = run(output, paper_dir=copied_paper)
            self.assertEqual(verify(output, paper_dir=copied_paper), manifest)
            readme = copied_paper / "code" / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8") + "\ntampered copy\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "implementation SHA-256 mismatch"):
                verify(output, paper_dir=copied_paper)

    def test_manifest_has_exact_metrics_and_no_hidden_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest = run(Path(tmp))
            metrics = manifest["metrics"]
            self.assertEqual(metrics["total_csv_rows"], 676)
            self.assertTrue(metrics["all_topology_expectations_match"])
            self.assertEqual(metrics["nonconstant_continuous_maps_to_t0"], 0)
            self.assertEqual(
                metrics["nonconstant_continuous_maps_to_indiscrete_negative_target"],
                38,
            )
            self.assertEqual(metrics["nonconstant_measurable_maps_to_discrete_targets"], 0)
            self.assertTrue(metrics["all_dirac_pairs_equal_on_borel"])
            self.assertEqual(metrics["nontrivial_continuous_finite_characters"], 0)
            self.assertEqual(metrics["algebraic_noncontinuous_negative_controls"], 22)
            self.assertTrue(metrics["coproduct_k0_counts_match_labels"])
            self.assertTrue(metrics["all_finite_prefixes_marked_nondecisive"])
            determinism = manifest["determinism"]
            for key in (
                "network",
                "randomness",
                "external_datasets",
                "target_zero_data",
                "fitting",
                "timestamps",
            ):
                self.assertFalse(determinism[key])
            self.assertEqual(determinism["python_dependencies"], "standard_library_only")
            self.assertIn("not mathematical proofs", manifest["interpretation_boundary"])
            serialized = json.dumps(manifest, sort_keys=True).lower()
            self.assertNotIn("riemann zero value", serialized)

    def test_active_tuple_and_implementation_paths_exist(self) -> None:
        paper_dir = Path(__file__).resolve().parents[1]
        for relative, expected in EXPECTED_ACTIVE_TUPLE_HASHES.items():
            self.assertEqual(sha256(paper_dir / relative), expected)
        for relative in IMPLEMENTATION_RELATIVE_PATHS:
            self.assertTrue((paper_dir / relative).is_file(), relative)

    def test_generator_imports_standard_library_only(self) -> None:
        source_path = Path(__file__).with_name("separated_reflection_controls.py")
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
        allowed = {
            "__future__",
            "argparse",
            "csv",
            "hashlib",
            "itertools",
            "json",
            "fractions",
            "pathlib",
            "typing",
        }
        self.assertLessEqual(imports, allowed)

    def test_bytecode_is_disabled_in_reproduction_environment(self) -> None:
        self.assertEqual(os.environ.get("PYTHONDONTWRITEBYTECODE"), "1")


if __name__ == "__main__":
    unittest.main()
