#!/usr/bin/env python3
"""Unit and reproduction tests for Paper 11 deterministic controls."""

from __future__ import annotations

import ast
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

from indiscrete_convolution_controls import (
    ACTION_MODELS,
    ARTIFACT_FILENAMES,
    EXPECTED_ACTIVE_LOCK_HASHES,
    EXPECTED_PHASE_GATE_HASHES,
    FACTORIZATION_MODELS,
    IMPLEMENTATION_RELATIVE_PATHS,
    LABEL_PERIODS,
    MANIFEST_FILENAME,
    SCHEMA,
    TOPOLOGY_MODELS,
    _action_blind_rows,
    _arrow_topology_rows,
    _convention_negative_rows,
    _convolution_rows,
    _hopen_zero_rows,
    _involution_rows,
    _label_period_rows,
    _measurable_factorization_rows,
    _proxy_strictness_rows,
    _support_projection_rows,
    _t0_factorization_rows,
    _unit_regular_rows,
    actual_global_convolution,
    arrow_points,
    arrow_source,
    arrow_topology_indices,
    factors_through_time,
    gaussian_profile,
    group_convolution,
    group_involution,
    inverse_arrow,
    is_continuous_mapping,
    is_hausdorff_subspace,
    is_prime,
    is_t0_space,
    multiply_arrows,
    powerset,
    regular_matrix_actual,
    regular_matrix_group,
    run,
    sha256,
    source_fibre_arrow,
    verify,
)


def copy_hash_bound_paper(source_paper: Path, destination: Path) -> None:
    """Copy only the files needed to exercise lock/implementation drift."""

    for relative in (
        *EXPECTED_ACTIVE_LOCK_HASHES,
        *EXPECTED_PHASE_GATE_HASHES,
        *IMPLEMENTATION_RELATIVE_PATHS,
    ):
        source = source_paper / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


class FiniteActionTests(unittest.TestCase):
    def test_action_models_cover_trivial_transitive_nontransitive(self) -> None:
        self.assertEqual(
            {action.name for action in ACTION_MODELS},
            {"trivial", "transitive", "nontransitive"},
        )

    def test_action_law_holds_exhaustively(self) -> None:
        for action in ACTION_MODELS:
            for x in range(action.unit_size):
                for left in range(action.period):
                    for right in range(action.period):
                        self.assertEqual(
                            action.act(action.act(x, left), right),
                            action.act(x, left + right),
                        )

    def test_action_orbit_counts_are_genuinely_distinct(self) -> None:
        self.assertEqual(
            {action.name: len(action.orbit_partition()) for action in ACTION_MODELS},
            {"trivial": 4, "transitive": 1, "nontransitive": 2},
        )

    def test_action_stabilizer_sizes_differ(self) -> None:
        stabilizers = {
            action.name: set(action.stabilizer_sizes()) for action in ACTION_MODELS
        }
        self.assertEqual(stabilizers["trivial"], {4})
        self.assertEqual(stabilizers["transitive"], {1})
        self.assertEqual(stabilizers["nontransitive"], {2})


class ArrowTopologyTests(unittest.TestCase):
    def test_product_topology_has_two_to_period_opens(self) -> None:
        for unit_size, period in TOPOLOGY_MODELS:
            topology = arrow_topology_indices(unit_size, period)
            self.assertEqual(len(topology), 2**period)

    def test_each_open_is_x_times_a_time_subset(self) -> None:
        for unit_size, period in TOPOLOGY_MODELS:
            for opened in arrow_topology_indices(unit_size, period):
                for time in range(period):
                    fibre = {
                        time * unit_size + unit for unit in range(unit_size)
                    }
                    self.assertIn(len(opened.intersection(fibre)), {0, unit_size})

    def test_nontrivial_arrow_models_are_not_t0(self) -> None:
        for unit_size, period in TOPOLOGY_MODELS:
            self.assertGreater(unit_size, 1)
            self.assertFalse(
                is_t0_space(
                    unit_size * period,
                    arrow_topology_indices(unit_size, period),
                )
            )

    def test_only_empty_open_subspace_is_hausdorff(self) -> None:
        for unit_size, period in TOPOLOGY_MODELS:
            topology = arrow_topology_indices(unit_size, period)
            for opened in topology:
                self.assertEqual(
                    is_hausdorff_subspace(opened, topology),
                    not opened,
                )

    def test_arrow_topology_rows_close_all_expectations(self) -> None:
        rows = _arrow_topology_rows()
        self.assertEqual(len(rows), 72)
        self.assertEqual({row["expectation_match"] for row in rows}, {"true"})
        self.assertFalse(
            any(
                row["nonempty"] == "true"
                and row["hausdorff_subspace"] == "true"
                for row in rows
            )
        )


class FactorizationTests(unittest.TestCase):
    def test_factors_through_time_reconstructs_time_major_mapping(self) -> None:
        mapping = (0, 0, 1, 1, 0, 0)
        factors, values = factors_through_time(mapping, 2, 3)
        self.assertTrue(factors)
        self.assertEqual(values, (0, 1, 0))

    def test_nonfactor_mapping_is_detected(self) -> None:
        factors, values = factors_through_time((0, 1, 0, 0), 2, 2)
        self.assertFalse(factors)
        self.assertEqual(values, ())

    def test_all_continuous_maps_to_t0_targets_factor(self) -> None:
        rows = _t0_factorization_rows()
        violating = [
            row
            for row in rows
            if row["target_t0"] == "true"
            and row["continuous"] == "true"
            and row["factors_through_time"] == "false"
        ]
        self.assertEqual(violating, [])
        self.assertEqual(
            {row["t0_implication_match"] for row in rows}, {"true"}
        )

    def test_factorized_t0_rows_reconstruct_exactly(self) -> None:
        rows = _t0_factorization_rows()
        factorized = [row for row in rows if row["factors_through_time"] == "true"]
        self.assertTrue(factorized)
        self.assertEqual(
            {row["reconstruction_match"] for row in factorized}, {"true"}
        )

    def test_non_t0_target_is_a_real_negative_control(self) -> None:
        negatives = [
            row
            for row in _t0_factorization_rows()
            if row["negative_nonfactor_continuous"] == "true"
        ]
        self.assertEqual(len(negatives), 68)

    def test_discrete_time_factor_is_continuous(self) -> None:
        for unit_size, period in FACTORIZATION_MODELS:
            mapping = tuple(
                time % 2 for time in range(period) for _ in range(unit_size)
            )
            self.assertTrue(
                is_continuous_mapping(
                    mapping,
                    arrow_topology_indices(unit_size, period),
                    powerset((0, 1)),
                )
            )


class MeasurableFactorizationTests(unittest.TestCase):
    def test_source_borel_sigma_is_the_time_projection_ledger(self) -> None:
        for unit_size, period in FACTORIZATION_MODELS:
            source_sigma = arrow_topology_indices(unit_size, period)
            self.assertEqual(len(source_sigma), 2**period)

    def test_all_measurable_maps_to_separated_targets_factor(self) -> None:
        rows = _measurable_factorization_rows()
        violating = [
            row
            for row in rows
            if row["target_countably_separated"] == "true"
            and row["measurable"] == "true"
            and row["factors_through_time"] == "false"
        ]
        self.assertEqual(violating, [])
        self.assertEqual(
            {row["separated_implication_match"] for row in rows}, {"true"}
        )

    def test_nonseparated_sigma_target_is_a_real_negative(self) -> None:
        negatives = [
            row
            for row in _measurable_factorization_rows()
            if row["negative_nonfactor_measurable"] == "true"
        ]
        self.assertEqual(len(negatives), 68)


class SupportTests(unittest.TestCase):
    def test_support_is_x_times_group_support(self) -> None:
        rows = _support_projection_rows()
        self.assertEqual(len(rows), 15)
        self.assertEqual(
            {row["support_equals_x_times_projection"] for row in rows}, {"true"}
        )

    def test_support_projection_matches_nonzero_time_projection(self) -> None:
        rows = _support_projection_rows()
        self.assertEqual(
            {row["projection_matches_group_support"] for row in rows}, {"true"}
        )
        empty_rows = [row for row in rows if row["profile"] == "empty"]
        self.assertTrue(empty_rows)
        self.assertEqual({row["ambient_support"] for row in empty_rows}, {"{}"})


class ConvolutionAndInvolutionTests(unittest.TestCase):
    def test_group_convolution_is_associative_on_profiles(self) -> None:
        left = gaussian_profile("dense_a", 4)
        middle = gaussian_profile("dense_b", 4)
        right = gaussian_profile("sparse_signed", 4)
        self.assertEqual(
            group_convolution(group_convolution(left, middle), right),
            group_convolution(left, group_convolution(middle, right)),
        )

    def test_involution_is_antimultiplicative(self) -> None:
        left = gaussian_profile("dense_a", 4)
        right = gaussian_profile("dense_b", 4)
        self.assertEqual(
            group_involution(group_convolution(left, right)),
            group_convolution(group_involution(right), group_involution(left)),
        )

    def test_actual_global_convolution_matches_group_for_every_action(self) -> None:
        self.assertEqual(
            {row["all_units_match_group"] for row in _convolution_rows()},
            {"true"},
        )

    def test_actual_global_convolution_erases_unit_coordinate(self) -> None:
        self.assertEqual(
            {row["unit_coordinate_erased"] for row in _convolution_rows()},
            {"true"},
        )

    def test_actual_global_involution_matches_group_for_every_action(self) -> None:
        self.assertEqual(
            {row["all_units_match_group"] for row in _involution_rows()},
            {"true"},
        )

    def test_delta_shift_convolution_has_expected_support(self) -> None:
        action = next(action for action in ACTION_MODELS if action.name == "transitive")
        left = gaussian_profile("delta_shift", 4)
        right = gaussian_profile("delta_zero", 4)
        values = tuple(
            actual_global_convolution(action, left, right, 0, time)
            for time in range(4)
        )
        self.assertEqual(values, left)


class ConventionNegativeTests(unittest.TestCase):
    def test_wrong_time_sign_is_detected_for_every_action(self) -> None:
        rows = [
            row
            for row in _convention_negative_rows()
            if row["negative_kind"] == "wrong_time_sign_t_plus_u"
        ]
        self.assertEqual(len(rows), 3)
        self.assertEqual({row["negative_detected"] for row in rows}, {"true"})
        self.assertTrue(all(int(row["mismatch_count"]) > 0 for row in rows))

    def test_wrong_source_range_is_detected_by_raw_nontrivial_probe(self) -> None:
        rows = [
            row
            for row in _convention_negative_rows()
            if row["negative_kind"] == "wrong_source_range_no_unit_shift"
        ]
        self.assertEqual({row["action"] for row in rows}, {"transitive", "nontransitive"})
        self.assertEqual({row["negative_detected"] for row in rows}, {"true"})
        self.assertEqual(
            {row["probe_domain"] for row in rows},
            {"raw_x_dependent_probe_outside_global_algebra"},
        )


class RegularRepresentationTests(unittest.TestCase):
    def test_source_fibre_parameterization_has_fixed_source(self) -> None:
        for action in ACTION_MODELS:
            for base in range(action.unit_size):
                for time in range(action.period):
                    gamma = source_fibre_arrow(action, base, time)
                    self.assertEqual(arrow_source(action, gamma), base)

    def test_groupoid_inverse_and_product_yield_time_difference(self) -> None:
        for action in ACTION_MODELS:
            base = 0
            for time in range(action.period):
                for u in range(action.period):
                    gamma = source_fibre_arrow(action, base, time)
                    eta = source_fibre_arrow(action, base, u)
                    product = multiply_arrows(action, gamma, inverse_arrow(action, eta))
                    self.assertEqual(product[1], (time - u) % action.period)

    def test_every_actual_regular_matrix_matches_group_matrix(self) -> None:
        self.assertEqual(
            {row["matches_group_matrix"] for row in _unit_regular_rows()},
            {"true"},
        )

    def test_regular_matrices_are_identical_across_units_and_actions(self) -> None:
        rows = _unit_regular_rows()
        for profile in {row["profile"] for row in rows}:
            selected = {
                row["actual_matrix"] for row in rows if row["profile"] == profile
            }
            self.assertEqual(len(selected), 1)

    def test_direct_regular_constructor_matches_group(self) -> None:
        values = gaussian_profile("dense_a", 4)
        expected = regular_matrix_group(values)
        for action in ACTION_MODELS:
            for base in range(action.unit_size):
                self.assertEqual(regular_matrix_actual(action, values, base), expected)


class HOpenAndProxyTests(unittest.TestCase):
    def test_hopen_diagnostic_is_zero_in_all_models(self) -> None:
        rows = _hopen_zero_rows()
        self.assertEqual(len(rows), len(TOPOLOGY_MODELS))
        self.assertEqual({row["hopen_span_zero"] for row in rows}, {"true"})
        self.assertEqual(
            {int(row["nonempty_hausdorff_open_count"]) for row in rows}, {0}
        )

    def test_proxy_map_directions_are_strict(self) -> None:
        rows = _proxy_strictness_rows()
        self.assertEqual(
            {row["actual_to_proxy_identity_continuous"] for row in rows},
            {"false"},
        )
        self.assertEqual(
            {row["proxy_to_actual_identity_continuous"] for row in rows},
            {"true"},
        )

    def test_proxy_has_explicit_extra_functions(self) -> None:
        rows = _proxy_strictness_rows()
        self.assertEqual(
            {row["strict_extra_proxy_function"] for row in rows}, {"true"}
        )
        self.assertTrue(all(int(row["dimension_gap"]) > 0 for row in rows))


class ActionBlindAndLabelTests(unittest.TestCase):
    def test_action_blind_rows_preserve_distinct_orbit_data(self) -> None:
        rows = _action_blind_rows()
        self.assertEqual(
            {row["action"]: int(row["orbit_count"]) for row in rows},
            {"trivial": 4, "transitive": 1, "nontransitive": 2},
        )

    def test_all_actions_have_one_global_signature(self) -> None:
        rows = _action_blind_rows()
        self.assertEqual(len({row["global_signature"] for row in rows}), 1)
        self.assertEqual(
            {row["action_visible_in_global_signature"] for row in rows},
            {"false"},
        )

    def test_label_controls_cover_prime_composite_arbitrary(self) -> None:
        rows = _label_period_rows()
        self.assertEqual(
            {row["label_family"] for row in rows},
            {"prime", "composite", "arbitrary"},
        )
        prime_labels = {
            int(row["label"])
            for row in rows
            if row["label_family"] == "prime"
        }
        self.assertTrue(all(is_prime(label) for label in prime_labels))

    def test_each_label_is_crossed_with_every_period(self) -> None:
        rows = _label_period_rows()
        for label in {row["label"] for row in rows}:
            self.assertEqual(
                {
                    int(row["period"])
                    for row in rows
                    if row["label"] == label
                },
                set(LABEL_PERIODS),
            )

    def test_period_signatures_do_not_depend_on_label(self) -> None:
        rows = _label_period_rows()
        for period in LABEL_PERIODS:
            signatures = {
                row["period_signature"]
                for row in rows
                if int(row["period"]) == period
            }
            self.assertEqual(len(signatures), 1)


class ReproductionTests(unittest.TestCase):
    def test_two_fresh_generations_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as first_tmp, tempfile.TemporaryDirectory() as second_tmp:
            first = Path(first_tmp)
            second = Path(second_tmp)
            first_manifest = run(first)
            second_manifest = run(second)
            self.assertEqual(first_manifest, second_manifest)
            for filename in (*ARTIFACT_FILENAMES, MANIFEST_FILENAME):
                self.assertEqual(
                    (first / filename).read_bytes(),
                    (second / filename).read_bytes(),
                )

    def test_verify_accepts_clean_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = run(output)
            self.assertEqual(verify(output), manifest)

    def test_verify_rejects_artifact_byte_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            target = output / ARTIFACT_FILENAMES[0]
            target.write_bytes(target.read_bytes() + b"tamper\n")
            with self.assertRaisesRegex(ValueError, "artifact SHA-256 mismatch"):
                verify(output)

    def test_verify_rejects_missing_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            (output / ARTIFACT_FILENAMES[0]).unlink()
            with self.assertRaisesRegex(ValueError, "output artifact set mismatch"):
                verify(output)

    def test_verify_rejects_extra_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            (output / "unexpected.csv").write_text("x\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "output artifact set mismatch"):
                verify(output)

    def test_verify_rejects_readme_as_extra_outside_checked_results(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            (output / "README.md").write_text("unexpected\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "output artifact set mismatch"):
                verify(output)

    def test_verify_rejects_manifest_metric_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            run(output)
            manifest_path = output / MANIFEST_FILENAME
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["metrics"]["total_csv_rows"] += 1
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "manifest metric or metadata"):
                verify(output)

    def test_verify_rejects_implementation_drift(self) -> None:
        source_paper = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copied_paper = Path(tmp) / "paper11-copy"
            copy_hash_bound_paper(source_paper, copied_paper)
            output = copied_paper / "results"
            run(output, paper_dir=copied_paper)
            readme = copied_paper / "code" / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8") + "\ndrift\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "implementation SHA-256 mismatch"):
                verify(output, paper_dir=copied_paper)

    def test_verify_rejects_active_lock_drift(self) -> None:
        source_paper = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copied_paper = Path(tmp) / "paper11-copy"
            copy_hash_bound_paper(source_paper, copied_paper)
            output = copied_paper / "results"
            run(output, paper_dir=copied_paper)
            lock = copied_paper / "notes" / "pipeline_state.md"
            lock.write_text(
                lock.read_text(encoding="utf-8") + "\ndrift\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "active lock SHA-256 mismatch"):
                verify(output, paper_dir=copied_paper)

    def test_verify_rejects_phase_gate_drift(self) -> None:
        source_paper = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copied_paper = Path(tmp) / "paper11-copy"
            copy_hash_bound_paper(source_paper, copied_paper)
            output = copied_paper / "results"
            run(output, paper_dir=copied_paper)
            gate = copied_paper / "notes" / "phase2_final_review.md"
            gate.write_text(
                gate.read_text(encoding="utf-8") + "\ndrift\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "Phase-2 gate SHA-256 mismatch"):
                verify(output, paper_dir=copied_paper)

    def test_manifest_binds_all_active_and_implementation_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest = run(Path(tmp))
            self.assertEqual(
                set(manifest["active_lock_files"]), set(EXPECTED_ACTIVE_LOCK_HASHES)
            )
            self.assertEqual(
                set(manifest["phase_gate_files"]), set(EXPECTED_PHASE_GATE_HASHES)
            )
            self.assertEqual(
                set(manifest["implementation_files"]),
                set(IMPLEMENTATION_RELATIVE_PATHS),
            )

    def test_manifest_metrics_are_exact_and_complete(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest = run(Path(tmp))
            metrics = manifest["metrics"]
            self.assertEqual(manifest["schema"], SCHEMA)
            self.assertEqual(metrics["csv_artifact_count"], 12)
            self.assertEqual(metrics["total_csv_rows"], 642)
            self.assertEqual(metrics["nonempty_hausdorff_open_count"], 0)
            self.assertEqual(metrics["t0_continuous_nonfactor_count"], 0)
            self.assertEqual(metrics["nont0_continuous_nonfactor_negative_count"], 68)
            self.assertEqual(metrics["separated_measurable_nonfactor_count"], 0)
            self.assertEqual(
                metrics["nonseparated_measurable_nonfactor_negative_count"], 68
            )
            self.assertEqual(metrics["negative_control_count"], 5)
            self.assertEqual(metrics["distinct_global_action_signatures"], 1)
            self.assertEqual(metrics["label_family_count"], 3)
            self.assertEqual(metrics["label_period_pair_count"], 27)

    def test_manifest_declares_no_hidden_or_stochastic_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest = run(Path(tmp))
            determinism = manifest["determinism"]
            self.assertEqual(
                determinism["python_dependencies"], "standard_library_only"
            )
            for key in (
                "network",
                "randomness",
                "external_datasets",
                "target_zero_data",
                "fitting",
                "timestamps",
            ):
                self.assertFalse(determinism[key])
            self.assertIn("witnesses, not proofs", manifest["interpretation_boundary"])

    def test_generator_imports_standard_library_only(self) -> None:
        source_path = Path(__file__).with_name("indiscrete_convolution_controls.py")
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        imports: set[str] = set()
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
            "dataclasses",
            "pathlib",
            "typing",
        }
        self.assertLessEqual(imports, allowed)

    def test_hash_bound_paths_exist_at_expected_bytes(self) -> None:
        paper_dir = Path(__file__).resolve().parents[1]
        for relative, expected in {
            **EXPECTED_ACTIVE_LOCK_HASHES,
            **EXPECTED_PHASE_GATE_HASHES,
        }.items():
            self.assertEqual(sha256(paper_dir / relative), expected)
        for relative in IMPLEMENTATION_RELATIVE_PATHS:
            self.assertTrue((paper_dir / relative).is_file(), relative)

    def test_reproduction_environment_disables_bytecode(self) -> None:
        self.assertEqual(os.environ.get("PYTHONDONTWRITEBYTECODE"), "1")


if __name__ == "__main__":
    unittest.main()
