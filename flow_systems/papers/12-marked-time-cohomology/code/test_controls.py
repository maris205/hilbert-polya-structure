#!/usr/bin/env python3
"""Unit and fail-closed tests for Paper 12 deterministic controls."""

from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import generate_controls as controls


PAPER_DIR = Path(__file__).resolve().parents[1]

LEGACY_ARTIFACT_SHA256 = {
    "control_summary.csv": "61fc4f8cb46f15710886a8f4f4bd6e65559ebd78367fc50cd3653b98f5ea6370",
    "degree1_cohomology_controls.csv": "ebd3bb8062e1c4acec70f5b28d3dca90fc9aabdb92fd90592c0f2bb0dafb6b51",
    "factorization_controls.csv": "888b2a95f23a80ef9eb06ef008ee9f81344612a01bce19e0ff1f88993213fce0",
    "label_boundary_controls.csv": "b3f82c3af8382b1d890cd25e1d496cc2b93be90104c036c15d6159ae2af91e90",
    "morphism_controls.csv": "00dbe2ff0e918682cfc75db6e5893631537d77111fcf60c9eff6d21c915a6d2d",
    "negative_controls.csv": "0a3a5c2333a0d5d2620b0f54c22e1dfeba9a8eacc336a61d6de45d9ca2736493",
    "nerve_face_controls.csv": "c50500cc4775abf20c96de55caf6c62330abfa79177bc7dec6eee76b20c52672",
    "packet_period_controls.csv": "3f13dbbbe464522d92e3e33c5b55528be6fd55e92d26b295d74c87ab83c9932e",
    "period_controls.csv": "b7f2450441514b87bd15f9da3598d5c05f4f11cb948679536c0af05433de5d33",
    "quotient_topology_controls.csv": "0bc8338ca42a3a617638c25d3a89309c0388c376fd7208cb592d020bcd9ff5df",
}


class HelpersTests(unittest.TestCase):
    def test_bool_text_true(self) -> None:
        self.assertEqual(controls.bool_text(True), "true")

    def test_bool_text_false(self) -> None:
        self.assertEqual(controls.bool_text(False), "false")

    def test_float_print_format_is_frozen(self) -> None:
        self.assertEqual(controls.FLOAT_PRINT_FORMAT, ".15g")

    def test_float_tolerance_is_exactly_frozen(self) -> None:
        self.assertEqual(controls.FLOAT_ABS_TOLERANCE, 1e-12)

    def test_float_close_boundary(self) -> None:
        self.assertTrue(controls.float_close(0.0, 1e-12))
        self.assertFalse(controls.float_close(0.0, 1.0001e-12))

    def test_powerset_cardinality(self) -> None:
        self.assertEqual(len(controls.powerset((0, 1, 2))), 8)

    def test_sha256_bytes_known_vector(self) -> None:
        self.assertEqual(
            controls.sha256_bytes(b"abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )


class OrbitwiseExactAlgebraTests(unittest.TestCase):
    def test_exact_rank_empty_matrix_is_zero(self) -> None:
        self.assertEqual(controls.exact_matrix_rank(()), 0)

    def test_exact_rank_rejects_ragged_matrix(self) -> None:
        with self.assertRaises(ValueError):
            controls.exact_matrix_rank(((1, 0), (1,)))

    def test_cycle_incidence_rank_is_m_times_n_minus_one(self) -> None:
        for n in controls.ORBITWISE_STANDARDIZATION_N:
            for m in controls.ORBITWISE_STANDARDIZATION_M:
                self.assertEqual(
                    controls.exact_matrix_rank(controls.cycle_incidence_matrix(n, m)),
                    m * (n - 1),
                )

    def test_cycle_sum_map_has_rank_m(self) -> None:
        for n in controls.ORBITWISE_STANDARDIZATION_N:
            for m in controls.ORBITWISE_STANDARDIZATION_M:
                self.assertEqual(
                    controls.exact_matrix_rank(controls.cycle_sum_matrix(n, m)),
                    m,
                )

    def test_diagonal_rank_is_one_for_nonempty_q(self) -> None:
        for m in controls.ORBITWISE_STANDARDIZATION_M:
            self.assertEqual(controls.exact_matrix_rank(controls.diagonal_matrix(m)), 1)

    def test_diagonal_rejects_empty_q(self) -> None:
        with self.assertRaises(ValueError):
            controls.diagonal_matrix(0)

    def test_full_symmetric_invariant_dimension_is_one(self) -> None:
        for m in controls.ORBITWISE_STANDARDIZATION_M:
            rank = controls.exact_matrix_rank(controls.invariant_constraint_matrix(m))
            self.assertEqual(m - rank, 1)

    def test_nonzero_coboundary_has_zero_cycle_sums(self) -> None:
        n, m = 5, 3
        potential = tuple(
            (orbit + 1) * position
            for orbit in range(m)
            for position in range(n)
        )
        edges = controls.coboundary_from_potential(n, m, potential)
        self.assertTrue(any(edges))
        self.assertEqual(controls.cycle_sums(n, m, edges), (0, 0, 0))

    def test_zero_isotropy_potential_is_recovered_exactly(self) -> None:
        n, m = 7, 2
        edges = tuple(
            orbit + 1 if position == 0 else -(orbit + 1) if position == 1 else 0
            for orbit in range(m)
            for position in range(n)
        )
        potential = controls.recover_zero_isotropy_potential(n, m, edges)
        self.assertEqual(controls.coboundary_from_potential(n, m, potential), edges)
        self.assertEqual((potential[0], potential[n]), (0, 0))

    def test_nonzero_isotropy_sum_rejects_potential_recovery(self) -> None:
        with self.assertRaises(ValueError):
            controls.recover_zero_isotropy_potential(3, 1, (1, 0, 0))

    def test_automorphism_enumeration_matches_n_power_m_m_factorial(self) -> None:
        for n in controls.ORBITWISE_STANDARDIZATION_N:
            for m in controls.ORBITWISE_STANDARDIZATION_M:
                self.assertEqual(
                    len(controls.cycle_automorphisms(n, m)),
                    n**m * controls.math.factorial(m),
                )

    def test_automorphism_order_is_permutation_then_translation_lexicographic(self) -> None:
        automorphisms = controls.cycle_automorphisms(3, 2)
        self.assertEqual(automorphisms[0], ((0, 1), (0, 0)))
        self.assertEqual(automorphisms[8], ((0, 1), (2, 2)))
        self.assertEqual(automorphisms[9], ((1, 0), (0, 0)))

    def test_every_frozen_automorphism_is_equivariant_and_invertible(self) -> None:
        for n in controls.ORBITWISE_STANDARDIZATION_N:
            for m in controls.ORBITWISE_STANDARDIZATION_M:
                metrics = controls.orbitwise_model_metrics(n, m)
                self.assertTrue(metrics.lift_descend_ok)
                self.assertTrue(metrics.group_inverse_ok)

    def test_basepoint_transport_is_exhaustive(self) -> None:
        for n in controls.ORBITWISE_STANDARDIZATION_N:
            for m in controls.ORBITWISE_STANDARDIZATION_M:
                self.assertTrue(
                    all(
                        controls.basepoint_transport_ok(n, m, orbit, basepoint)
                        for orbit in range(m)
                        for basepoint in range(n)
                    )
                )

    def test_common_lengths_accepted_and_mixed_lengths_rejected(self) -> None:
        self.assertTrue(controls.common_cycle_length_accepted((5, 5, 5)))
        self.assertFalse(controls.common_cycle_length_accepted((3, 5)))

    def test_wrong_j_direction_is_detected(self) -> None:
        self.assertTrue(controls.wrong_j_direction_detected(3, 2))

    def test_orbitwise_schema_has_exactly_twenty_six_columns(self) -> None:
        self.assertEqual(len(controls.ORBITWISE_STANDARDIZATION_FIELDS), 26)
        self.assertEqual(
            controls.ORBITWISE_STANDARDIZATION_FIELDS,
            (
                "record_type", "n", "m", "orbit", "basepoint", "permutation",
                "translation_vector", "open_count_actual", "open_count_standard",
                "h1_dim_actual", "h1_dim_standard", "j_rank", "aut_expected",
                "aut_enumerated", "basepoint_independent", "joint_action_ok",
                "lift_descend_ok", "group_inverse_ok", "diagonal_ok",
                "nonzero_coboundary_ok", "zero_isotropy_potential_ok",
                "invariant_dim", "mixed_length_rejected", "packet_schematic_only",
                "replaces_source_proof", "status",
            ),
        )

    def test_orbitwise_row_blocks_have_frozen_counts_and_order(self) -> None:
        rows = controls.orbitwise_standardization_rows()
        self.assertEqual(len(rows), 3252)
        self.assertEqual([row["record_type"] for row in rows[:9]], ["MODEL"] * 9)
        self.assertEqual(
            [row["record_type"] for row in rows[9:99]],
            ["BASEPOINT"] * 90,
        )
        self.assertEqual(
            [row["record_type"] for row in rows[99:3250]],
            ["AUT"] * 3151,
        )
        self.assertEqual(
            [row["record_type"] for row in rows[3250:]],
            ["NEGATIVE", "NEGATIVE"],
        )

    def test_model_rows_have_exact_h1_and_open_counts(self) -> None:
        models = [
            row
            for row in controls.orbitwise_standardization_rows()
            if row["record_type"] == "MODEL"
        ]
        self.assertEqual(len(models), 9)
        for row in models:
            n, m = int(row["n"]), int(row["m"])
            self.assertEqual(row["open_count_actual"], "2")
            self.assertEqual(int(row["open_count_standard"]), 2 ** (n * m))
            self.assertEqual(row["h1_dim_actual"], "1")
            self.assertEqual(int(row["h1_dim_standard"]), m)

    def test_model_rows_have_rank_one_diagonal_and_invariants(self) -> None:
        models = controls.orbitwise_standardization_rows()[:9]
        self.assertTrue(
            all(
                row["j_rank"] == "1"
                and row["diagonal_ok"] == "true"
                and row["invariant_dim"] == "1"
                for row in models
            )
        )

    def test_model_rows_verify_coboundaries_and_potentials(self) -> None:
        models = controls.orbitwise_standardization_rows()[:9]
        self.assertTrue(
            all(
                row["nonzero_coboundary_ok"] == "true"
                and row["zero_isotropy_potential_ok"] == "true"
                for row in models
            )
        )

    def test_q_one_rows_recover_the_transitive_dimensions_and_automorphisms(self) -> None:
        models = [row for row in controls.orbitwise_standardization_rows()[:9] if row["m"] == "1"]
        self.assertEqual(len(models), 3)
        for row in models:
            self.assertEqual(row["h1_dim_actual"], row["h1_dim_standard"])
            self.assertEqual(row["aut_expected"], row["n"])
            self.assertEqual(row["j_rank"], row["invariant_dim"])

    def test_negative_rows_are_mixed_length_then_wrong_j_direction(self) -> None:
        negatives = controls.orbitwise_standardization_rows()[-2:]
        self.assertEqual(
            [row["permutation"] for row in negatives],
            ["MIXED_LENGTHS", "WRONG_J_DIRECTION"],
        )
        self.assertEqual(negatives[0]["mixed_length_rejected"], "true")
        self.assertEqual(negatives[1]["lift_descend_ok"], "true")

    def test_all_orbitwise_rows_are_schematic_not_source_proof(self) -> None:
        rows = controls.orbitwise_standardization_rows()
        self.assertTrue(
            all(
                row["packet_schematic_only"] == "true"
                and row["replaces_source_proof"] == "false"
                and row["status"] == "PASS"
                for row in rows
            )
        )

    def test_legacy_artifact_bytes_are_frozen(self) -> None:
        payloads = controls.expected_artifact_bytes()
        self.assertEqual(
            {
                filename: controls.sha256_bytes(payloads[filename])
                for filename in LEGACY_ARTIFACT_SHA256
            },
            LEGACY_ARTIFACT_SHA256,
        )


class FiniteActionTests(unittest.TestCase):
    def test_invalid_generator_rejected(self) -> None:
        with self.assertRaises(ValueError):
            controls.FiniteAction("bad", 2, (0, 0))

    def test_invalid_modulus_closure_rejected(self) -> None:
        with self.assertRaises(ValueError):
            controls.FiniteAction("bad", 2, (1, 2, 0))

    def test_free_c3_action_closes(self) -> None:
        action = controls.NERVE_ACTIONS[1]
        self.assertEqual(action.act(0, 3), 0)

    def test_trivial_stabilizer_is_all_time(self) -> None:
        action = controls.NERVE_ACTIONS[0]
        self.assertEqual(action.stabilizer(0), (0, 1))

    def test_free_c3_stabilizer_is_identity_only(self) -> None:
        action = controls.NERVE_ACTIONS[1]
        self.assertEqual(action.stabilizer(0), (0,))

    def test_period_c2_time_c4_stabilizer(self) -> None:
        action = controls.NERVE_ACTIONS[2]
        self.assertEqual(action.stabilizer(0), (0, 2))

    def test_nontransitive_stabilizers_differ(self) -> None:
        action = controls.NERVE_ACTIONS[3]
        self.assertNotEqual(action.stabilizer(0), action.stabilizer(2))


class NerveAndDifferentialTests(unittest.TestCase):
    def test_simplex_coordinate_count(self) -> None:
        action = controls.NERVE_ACTIONS[2]
        self.assertEqual(len(controls.simplices(action, 3)), 2 * 4**3)

    def test_psi_tuple_is_composable(self) -> None:
        action = controls.NERVE_ACTIONS[3]
        for coordinate in controls.simplices(action, 3):
            self.assertTrue(controls.is_composable(action, controls.psi(action, coordinate)))

    def test_composable_count_matches_coordinates(self) -> None:
        action = controls.NERVE_ACTIONS[1]
        for degree in (1, 2, 3):
            self.assertEqual(
                len(controls.composable_tuples(action, degree)),
                len(controls.simplices(action, degree)),
            )

    def test_face_zero_moves_unit(self) -> None:
        action = controls.NERVE_ACTIONS[1]
        self.assertEqual(controls.face(action, (0, 1, 2), 0), (1, 2))

    def test_face_middle_adds_time(self) -> None:
        action = controls.NERVE_ACTIONS[2]
        self.assertEqual(controls.face(action, (0, 1, 3), 1), (0, 0))

    def test_face_last_drops_time(self) -> None:
        action = controls.NERVE_ACTIONS[1]
        self.assertEqual(controls.face(action, (0, 1, 2), 2), (0, 1))

    def test_face_bad_index_rejected(self) -> None:
        with self.assertRaises(ValueError):
            controls.face(controls.NERVE_ACTIONS[0], (0, 1), 2)

    def test_face_identities_exhaustive(self) -> None:
        for action in controls.NERVE_ACTIONS:
            checked, failures = controls.face_identity_failures(action, 4)
            self.assertGreater(checked, 0)
            self.assertEqual(failures, 0)

    def test_d2_exhaustive_coefficients_zero(self) -> None:
        for action in controls.NERVE_ACTIONS:
            for degree in (0, 1, 2):
                for output in controls.simplices(action, degree + 2):
                    self.assertTrue(
                        all(
                            value == 0
                            for value in controls.d2_coefficients(action, output, degree).values()
                        )
                    )

    def test_d2_wrong_sign_negative_detected(self) -> None:
        self.assertTrue(controls._wrong_sign_d2_detected())

    def test_nerve_ledger_has_twelve_rows(self) -> None:
        self.assertEqual(len(controls.nerve_face_rows()), 12)

    def test_nerve_ledger_all_bijective(self) -> None:
        self.assertTrue(all(row["psi_bijective"] == "true" for row in controls.nerve_face_rows()))

    def test_nerve_ledger_all_d2_zero(self) -> None:
        self.assertTrue(all(row["d2_zero"] == "true" for row in controls.nerve_face_rows()))


class FactorizationTests(unittest.TestCase):
    def test_factorization_ledger_has_six_rows(self) -> None:
        self.assertEqual(len(controls.factorization_rows()), 6)

    def test_t0_has_no_continuous_nonfactor_map(self) -> None:
        rows = [row for row in controls.factorization_rows() if row["target_t0"] == "true"]
        self.assertTrue(all(int(row["continuous_nonfactor_count"]) == 0 for row in rows))

    def test_nont0_has_continuous_nonfactor_maps(self) -> None:
        rows = [row for row in controls.factorization_rows() if row["target_t0"] == "false"]
        self.assertTrue(all(int(row["continuous_nonfactor_count"]) > 0 for row in rows))

    def test_nont0_degree_zero_witness_is_nonconstant(self) -> None:
        row = next(
            row
            for row in controls.factorization_rows()
            if row["target_t0"] == "false" and row["degree"] == "0"
        )
        self.assertIn(row["first_nonfactor_witness"], {"01", "10"})

    def test_degree_two_map_count_is_256(self) -> None:
        rows = [row for row in controls.factorization_rows() if row["degree"] == "2"]
        self.assertTrue(all(row["maps_checked"] == "256" for row in rows))

    def test_all_factorization_expectations_match(self) -> None:
        self.assertTrue(
            all(row["expected_boundary_match"] == "true" for row in controls.factorization_rows())
        )


class DegreeOneTests(unittest.TestCase):
    def test_linear_profile_has_zero_defect(self) -> None:
        self.assertEqual(controls.polynomial_defect(3, 0, 0, -2, 1), 0)

    def test_quadratic_profile_has_nonzero_defect(self) -> None:
        self.assertNotEqual(controls.polynomial_defect(0, 1, 0, 1, 1), 0)

    def test_nonzero_constant_profile_has_nonzero_defect(self) -> None:
        self.assertNotEqual(controls.polynomial_defect(0, 0, 1, 0, 0), 0)

    def test_degree_one_ledger_has_125_profiles(self) -> None:
        self.assertEqual(len(controls.degree1_rows()), 125)

    def test_degree_one_ledger_accepts_exactly_five_linear_profiles(self) -> None:
        self.assertEqual(
            sum(row["is_cocycle_on_probe"] == "true" for row in controls.degree1_rows()),
            5,
        )

    def test_degree_one_classification_matches_every_row(self) -> None:
        self.assertTrue(all(row["classification_match"] == "true" for row in controls.degree1_rows()))

    def test_b1_probe_is_zero_everywhere(self) -> None:
        self.assertTrue(all(row["b1_probe_zero"] == "true" for row in controls.degree1_rows()))


class PeriodAndMorphismTests(unittest.TestCase):
    def test_four_frozen_periods(self) -> None:
        self.assertEqual(len(controls.PERIODS), 4)

    def test_log_four_is_twice_log_two_with_frozen_float_boundary(self) -> None:
        self.assertTrue(controls.float_close(controls.PERIODS[1].value, 2 * controls.PERIODS[0].value))

    def test_period_ledger_contains_all_required_boundary_types(self) -> None:
        ids = {row["control_id"] for row in controls.period_rows()}
        self.assertTrue({"TRIV-2", "FREE-R", "PER-L", "DENSE-Q", "NONTRANS-1-2"} <= ids)

    def test_trivial_free_dense_are_not_lattices(self) -> None:
        rows = [
            row
            for row in controls.period_rows()
            if row["control_id"] in {"TRIV-2", "FREE-R", "DENSE-Q"}
        ]
        self.assertTrue(all(row["rank_one_lattice"] == "false" for row in rows))

    def test_nontransitive_periods_differ(self) -> None:
        expressions = {
            row["period_expression"]
            for row in controls.period_rows()
            if row["control_id"] == "NONTRANS-1-2"
        }
        self.assertEqual(expressions, {"Z", "2*Z"})

    def test_morphism_ledger_has_twenty_rows(self) -> None:
        self.assertEqual(len(controls.morphism_rows()), 20)

    def test_twelve_ordered_unequal_scaled_pairs(self) -> None:
        self.assertEqual(
            sum(row["control_id"] == "SCALE-LM" for row in controls.morphism_rows()),
            12,
        )

    def test_all_scaled_pairs_are_well_defined_and_covariant(self) -> None:
        rows = [row for row in controls.morphism_rows() if row["control_id"] == "SCALE-LM"]
        self.assertTrue(
            all(
                row["well_defined"] == "true"
                and row["inverse_verified"] == "true"
                and row["period_covariance"] == "true"
                for row in rows
            )
        )

    def test_all_wrong_scale_directions_are_detected(self) -> None:
        rows = [row for row in controls.morphism_rows() if row["control_id"] == "SCALE-LM"]
        self.assertTrue(
            all(
                row["wrong_identity_scale_detected"] == "true"
                and row["wrong_reciprocal_scale_detected"] == "true"
                for row in rows
            )
        )

    def test_orientation_reverse_is_unmarked_not_scaled(self) -> None:
        rows = [row for row in controls.morphism_rows() if row["control_id"] == "REVERSE-L"]
        self.assertTrue(
            all(
                row["unmarked_isomorphism"] == "true"
                and row["scaled_marked"] == "false"
                and row["orientation_nonconverse"] == "true"
                for row in rows
            )
        )


class QuotientPacketLabelTests(unittest.TestCase):
    def test_quotient_direction_is_one_sided(self) -> None:
        self.assertTrue(
            all(row["one_sided_topology_direction"] == "true" for row in controls.quotient_rows())
        )

    def test_quotient_theta_is_equivariant(self) -> None:
        self.assertTrue(all(row["theta_right_equivariant"] == "true" for row in controls.quotient_rows()))

    def test_scaled_dilation_is_not_strict_target_map(self) -> None:
        self.assertTrue(
            all(
                row["scaled_dilation_semilinear"] == "true"
                and row["scaled_dilation_strict_equivariant_when_unequal"] == "false"
                for row in controls.quotient_rows()
            )
        )

    def test_packet_ledger_has_twelve_rows(self) -> None:
        self.assertEqual(len(controls.packet_rows()), 12)

    def test_packet_ledger_binds_phase2_gate(self) -> None:
        self.assertTrue(
            all(
                row["source_gate_sha256"] == controls.PHASE2_FINAL_GATE_SHA256
                and row["source_gate_status"] == "PACKET_COROLLARY_ELIGIBLE"
                for row in controls.packet_rows()
            )
        )

    def test_packet_schema_does_not_claim_source_proof(self) -> None:
        self.assertTrue(all(row["replaces_source_proof"] == "false" for row in controls.packet_rows()))

    def test_label_ledger_has_all_twenty_four_permutations(self) -> None:
        self.assertEqual(len(controls.label_rows()), 24)

    def test_label_ledger_has_one_generic_signature(self) -> None:
        self.assertEqual(
            len({row["generic_theorem_signature_sha256"] for row in controls.label_rows()}),
            1,
        )

    def test_label_ledger_marks_proves_too_much(self) -> None:
        self.assertTrue(all(row["proves_too_much"] == "true" for row in controls.label_rows()))

    def test_negative_ledger_has_twelve_cases(self) -> None:
        self.assertEqual(len(controls.negative_rows()), 12)

    def test_all_negative_cases_detected(self) -> None:
        self.assertTrue(all(row["negative_detected"] == "true" for row in controls.negative_rows()))

    def test_summary_has_exact_frozen_control_ids(self) -> None:
        self.assertEqual(
            {row["control_id"] for row in controls.control_summary_rows()},
            {
                "TRIV-2", "FREE-R", "PER-L", "DENSE-Q", "NONTRANS-1-2",
                "NON-T0-A2", "SCALE-LM", "REVERSE-L", "LABEL-SWAP",
            },
        )


class ArtifactFactoryTests(unittest.TestCase):
    def test_artifact_factory_has_exact_names(self) -> None:
        self.assertEqual(set(controls.artifact_rows()), set(controls.ARTIFACT_FILENAMES))

    def test_artifact_schema_has_exact_names(self) -> None:
        self.assertEqual(set(controls.ARTIFACT_FIELDS), set(controls.ARTIFACT_FILENAMES))

    def test_csv_renderer_uses_lf_and_terminal_newline(self) -> None:
        payload = controls.render_csv(("a",), ({"a": "b"},))
        self.assertEqual(payload, b"a\nb\n")

    def test_artifact_bytes_are_deterministic(self) -> None:
        self.assertEqual(controls.expected_artifact_bytes(), controls.expected_artifact_bytes())

    def test_reserved_seed_is_unused(self) -> None:
        self.assertEqual(controls.RESERVED_UNUSED_SEED, 120012)

    def test_complete_artifact_package_is_eleven_csvs_and_3486_rows(self) -> None:
        rows = controls.artifact_rows()
        self.assertEqual(len(rows), 11)
        self.assertEqual(sum(len(artifact) for artifact in rows.values()), 3486)

    def test_orbitwise_csv_header_and_terminal_newline_are_canonical(self) -> None:
        payload = controls.expected_artifact_bytes()[
            "orbitwise_standardization_h1_controls.csv"
        ]
        self.assertTrue(payload.endswith(b"\n"))
        self.assertEqual(
            payload.splitlines()[0].decode("utf-8"),
            ",".join(controls.ORBITWISE_STANDARDIZATION_FIELDS),
        )


class StrictVerificationTests(unittest.TestCase):
    def _make_mirror(self, root: Path) -> Path:
        mirror = root / "paper"
        relatives = set(controls.EXPECTED_ACTIVE_LOCK_HASHES)
        relatives.update(controls.EXPECTED_PHASE_GATE_HASHES)
        relatives.update(controls.IMPLEMENTATION_RELATIVE_PATHS)
        for relative in sorted(relatives):
            source = PAPER_DIR / relative
            target = mirror / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        return mirror

    def _generated_fixture(self, root: Path) -> tuple[Path, Path]:
        mirror = self._make_mirror(root)
        output = root / "output"
        controls.run(output, mirror)
        return mirror, output

    def test_clean_temporary_generation_verifies(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            manifest = controls.verify(output, mirror)
            self.assertEqual(manifest["regression_status"], "PASS")

    def test_two_independent_generations_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mirror = self._make_mirror(root)
            first = root / "first"
            second = root / "second"
            controls.run(first, mirror)
            controls.run(second, mirror)
            for filename in (*controls.ARTIFACT_FILENAMES, controls.MANIFEST_FILENAME):
                self.assertEqual((first / filename).read_bytes(), (second / filename).read_bytes())

    def test_verify_only_does_not_write(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            before = {
                path.name: (controls.sha256_path(path), path.stat().st_mtime_ns)
                for path in output.iterdir()
            }
            controls.verify(output, mirror)
            after = {
                path.name: (controls.sha256_path(path), path.stat().st_mtime_ns)
                for path in output.iterdir()
            }
            self.assertEqual(before, after)

    def test_content_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / controls.ARTIFACT_FILENAMES[0]
            path.write_bytes(path.read_bytes() + b"tamper\n")
            with self.assertRaisesRegex(ValueError, "content/schema/row drift"):
                controls.verify(output, mirror)

    def test_orbitwise_artifact_tamper_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / "orbitwise_standardization_h1_controls.csv"
            payload = path.read_bytes()
            path.write_bytes(payload.replace(b",PASS\n", b",FAIL\n", 1))
            with self.assertRaisesRegex(ValueError, "content/schema/row drift"):
                controls.verify(output, mirror)

    def test_row_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / "control_summary.csv"
            lines = path.read_text(encoding="utf-8").splitlines()
            path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                controls.verify(output, mirror)

    def test_schema_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / "negative_controls.csv"
            lines = path.read_text(encoding="utf-8").splitlines()
            lines[0] = lines[0].replace("witness", "renamed")
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                controls.verify(output, mirror)

    def test_extra_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            (output / "extra.csv").write_text("x\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "extra"):
                controls.verify(output, mirror)

    def test_extra_directory_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            (output / "extra-dir").mkdir()
            with self.assertRaises(ValueError):
                controls.verify(output, mirror)

    def test_missing_artifact_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            (output / controls.ARTIFACT_FILENAMES[0]).unlink()
            with self.assertRaisesRegex(ValueError, "missing"):
                controls.verify(output, mirror)

    def test_missing_orbitwise_artifact_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            (output / "orbitwise_standardization_h1_controls.csv").unlink()
            with self.assertRaisesRegex(ValueError, "missing"):
                controls.verify(output, mirror)

    def test_missing_output_directory_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mirror = self._make_mirror(root)
            with self.assertRaises(FileNotFoundError):
                controls.verify(root / "absent", mirror)

    def test_lock_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = mirror / "notes/candidate_lock.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "active lock SHA-256 drift"):
                controls.verify(output, mirror)

    def test_gate_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = mirror / "notes/phase2_final_gate.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "phase gate/status SHA-256 drift"):
                controls.verify(output, mirror)

    def test_v4_final_gate_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = mirror / "notes/phase3_v4_final_gate.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "phase gate/status SHA-256 drift"):
                controls.verify(output, mirror)

    def test_v4_status_relock_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = mirror / "notes/phase3_v4_status_relock.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "phase gate/status SHA-256 drift"):
                controls.verify(output, mirror)

    def test_v4_amendment_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = mirror / "notes/phase3_standalone_amendment_v4.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "active lock SHA-256 drift"):
                controls.verify(output, mirror)

    def test_implementation_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = mirror / "code/README.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "manifest/hash/lock/gate/implementation drift"):
                controls.verify(output, mirror)

    def test_missing_implementation_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror = self._make_mirror(Path(temporary))
            (mirror / "code/README.md").unlink()
            with self.assertRaises(FileNotFoundError):
                controls.run(Path(temporary) / "output", mirror)

    def test_manifest_metric_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / controls.MANIFEST_FILENAME
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["metrics"]["negative_control_count"] = 999
            path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "manifest/hash"):
                controls.verify(output, mirror)

    def test_manifest_schema_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / controls.MANIFEST_FILENAME
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["schema"] = "wrong"
            path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                controls.verify(output, mirror)

    def test_manifest_artifact_hash_drift_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            path = output / controls.MANIFEST_FILENAME
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["artifacts"][controls.ARTIFACT_FILENAMES[0]]["sha256"] = "0" * 64
            path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                controls.verify(output, mirror)

    def test_invalid_manifest_json_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mirror, output = self._generated_fixture(Path(temporary))
            (output / controls.MANIFEST_FILENAME).write_text("{", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "canonical valid JSON"):
                controls.verify(output, mirror)

    def test_run_rejects_preexisting_extra_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mirror = self._make_mirror(root)
            output = root / "output"
            output.mkdir()
            (output / "extra").write_text("x", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "extra"):
                controls.run(output, mirror)

    def test_checked_in_results_verify(self) -> None:
        manifest = controls.verify(PAPER_DIR / "results", PAPER_DIR)
        self.assertEqual(manifest["schema"], controls.SCHEMA)

    def test_manifest_binds_v4_tuple_gate_status_and_omits_concurrent_proof(self) -> None:
        manifest = controls.verify(PAPER_DIR / "results", PAPER_DIR)
        self.assertEqual(
            set(manifest["active_lock_files"]),
            set(controls.EXPECTED_ACTIVE_LOCK_HASHES),
        )
        self.assertIn("notes/phase3_v4_final_gate.md", manifest["phase_gate_files"])
        self.assertIn("notes/phase3_v4_status_relock.md", manifest["phase_gate_files"])
        self.assertFalse(manifest["proof_binding"]["concurrent_v4_proof_hash_included"])

    def test_recursive_reproduction_entry_fails_before_work(self) -> None:
        script = PAPER_DIR / "experiments/reproduce.sh"
        environment = dict(os.environ)
        environment["PAPER12_REPRO_ACTIVE"] = "1"
        result = subprocess.run(
            ["bash", str(script)],
            cwd=PAPER_DIR,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("recursive Paper-12 reproduction entry detected", result.stderr)

    def test_checked_in_csv_headers_match_manifest_columns(self) -> None:
        manifest = json.loads((PAPER_DIR / "results/manifest.json").read_text(encoding="utf-8"))
        for filename in controls.ARTIFACT_FILENAMES:
            with (PAPER_DIR / "results" / filename).open(
                "r", encoding="utf-8", newline=""
            ) as handle:
                header = next(csv.reader(handle))
            self.assertEqual(header, manifest["artifacts"][filename]["columns"])


if __name__ == "__main__":
    unittest.main()
