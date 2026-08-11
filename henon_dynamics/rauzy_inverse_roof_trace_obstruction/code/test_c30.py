#!/usr/bin/env python3
"""Regression, phase-census, mutation, and independence tests for HCS-C30."""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CODE = PROJECT / "code"
PRODUCER = CODE / "c30_producer.py"
CHECKER = CODE / "c30_independent_check.py"
MANIFEST_TOOL = CODE / "c30_hash_manifest.py"


def load_checker_module():
    spec = importlib.util.spec_from_file_location("c30_checker_under_test", CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECK = load_checker_module()


def load_manifest_module():
    spec = importlib.util.spec_from_file_location(
        "c30_hash_manifest_under_test", MANIFEST_TOOL
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load manifest tool")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HASH_MANIFEST = load_manifest_module()


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


class C30Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="c30-tests-")
        cls.root = Path(cls.temp.name)
        cls.base_path = cls.root / "base.json"
        subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(cls.base_path)],
            check=True,
            capture_output=True,
            text=True,
        )
        cls.base = json.loads(cls.base_path.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    @property
    def payload(self) -> dict[str, object]:
        return self.base["payload"]

    def checker_report(self, certificate: dict[str, object]) -> dict[str, object]:
        return CHECK.Audit(certificate).run()

    def mutated(self, mutate, *, rehash: bool = True) -> dict[str, object]:
        certificate = json.loads(json.dumps(self.base))
        mutate(certificate)
        if rehash:
            certificate["payload_sha256"] = canonical_hash(certificate["payload"])
        return certificate

    def assert_rejected(self, mutate, *, rehash: bool = True, gate: str | None = None) -> None:
        report = self.checker_report(self.mutated(mutate, rehash=rehash))
        self.assertFalse(report["all_pass"])
        failures = [row for row in report["gates"] if row["status"] in {"FAIL", "ERROR"}]
        self.assertTrue(failures)
        if gate is not None:
            self.assertTrue(any(row["gate"] == gate for row in failures))

    def test_01_producer_is_byte_deterministic(self) -> None:
        other = self.root / "other.json"
        subprocess.run(
            [sys.executable, str(PRODUCER), "--output", str(other)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(self.base_path.read_bytes(), other.read_bytes())

    def test_02_independent_checker_passes_all_gates(self) -> None:
        report = self.checker_report(self.base)
        self.assertTrue(report["all_pass"])
        self.assertEqual(self.base["schema"], "hcs-c30-certificate-v3")
        self.assertEqual((report["passed"], report["total"]), (13, 13))

    def test_03_raw_homology_controls_are_exact_and_not_mislabelled(self) -> None:
        raw = self.payload["raw_homology_zigzag_control"]
        self.assertIn("not the AGY forward length", raw["classification"])
        controls = raw["C25_positive_controls"]
        self.assertEqual(controls["C1"]["phase_zero_positive_integer_witness"], [1, 2, 1, 1])
        self.assertEqual(controls["C2"]["phase_zero_positive_integer_witness"], [1, 1, 3, 1])
        for record in controls.values():
            self.assertEqual((record["feasible_phase_count"], record["phase_count"]), (6, 6))
            self.assertTrue(record["all_cyclic_phases_feasible"])
            self.assertTrue(
                all(
                    value > 0
                    for phase in record["phase_records"]
                    for state in phase["trajectory"]
                    for value in state
                )
            )

    def test_04_raw_c26_is_infeasible_in_all_24_phases(self) -> None:
        record = self.payload["raw_homology_zigzag_control"]["C26_infeasibility"]
        self.assertEqual((record["infeasible_phase_count"], record["phase_count"]), (24, 24))
        self.assertTrue(record["all_cyclic_phases_infeasible"])
        self.assertEqual(
            [row["linear_form"] for row in record["phase_zero_highlights"]],
            [[1, 0, 0, 0], [-1, 0, 0, 0]],
        )

    def test_05_forward_length_phase_census_is_6_6_24(self) -> None:
        words = self.payload["forward_length_positive_cone_gate"]["words"]
        expected = {"C25_C1": 6, "C25_C2": 6, "C26_W24": 24}
        self.assertEqual(set(words), set(expected))
        for name, count in expected.items():
            self.assertEqual(words[name]["phase_count"], count)
            self.assertEqual(words[name]["infeasible_phase_count"], count)
            self.assertTrue(words[name]["all_cyclic_phases_infeasible"])
            self.assertEqual(len(words[name]["phase_records"]), count)

    def test_06_transfer_branch_phase_census_is_6_6_24(self) -> None:
        gate = self.payload["transfer_inverse_branch_positive_cone_gate"]
        words = gate["words"]
        for name, count in {"C25_C1": 6, "C25_C2": 6, "C26_W24": 24}.items():
            self.assertEqual((words[name]["infeasible_phase_count"], words[name]["phase_count"]), (count, count))
            self.assertTrue(words[name]["all_cyclic_phases_infeasible"])
        self.assertEqual(
            words["C26_W24"]["phase_records"][0]["action_sequence"],
            gate["C26_phase_zero_equivalent_holonomy_word"],
        )

    def test_07_forward_length_representative_rows_are_exact(self) -> None:
        words = self.payload["forward_length_positive_cone_gate"]["words"]
        self.assertEqual(
            [row["linear_form"] for row in words["C25_C1"]["phase_zero_highlights"]],
            [[0, -1, 0, 1], [0, 1, 0, -1]],
        )
        self.assertEqual(
            [row["linear_form"] for row in words["C25_C2"]["phase_zero_highlights"]],
            [[1, 0, 0, 0], [-1, 0, 0, 0]],
        )
        self.assertEqual(
            [row["linear_form"] for row in words["C26_W24"]["phase_zero_highlights"]],
            [[1, 0, 1, -1], [-1, 0, -1, 1]],
        )

    def test_08_transfer_representative_rows_and_fatal_row_are_exact(self) -> None:
        words = self.payload["transfer_inverse_branch_positive_cone_gate"]["words"]
        self.assertEqual(
            [row["linear_form"] for row in words["C25_C1"]["phase_zero_highlights"]],
            [[0, 1, 0, -1], [0, -1, 0, 1]],
        )
        self.assertEqual(
            [row["linear_form"] for row in words["C25_C2"]["phase_zero_highlights"]],
            [[1, 0, 0, 0], [-1, 0, 0, 0]],
        )
        c26 = [row["linear_form"] for row in words["C26_W24"]["phase_zero_highlights"]]
        self.assertEqual(c26[0], [-984333, -498163, -999116, -479060])
        self.assertTrue(all(value < 0 for value in c26[0]))
        self.assertEqual(c26[1:], [[-1, 0, -1, 1], [1, 0, 1, -1]])

    def test_09_transfer_sequence_is_reverse_of_each_raw_rotation(self) -> None:
        words = self.payload["transfer_inverse_branch_positive_cone_gate"]["words"]
        for word in words.values():
            for phase in word["phase_records"]:
                self.assertEqual(phase["action_sequence"], list(reversed(phase["raw_rotation"])))

    def test_10_every_phase_finishes_at_identity(self) -> None:
        identity = [[int(i == j) for j in range(4)] for i in range(4)]
        gates = [
            self.payload["raw_homology_zigzag_control"]["C26_infeasibility"],
            *self.payload["forward_length_positive_cone_gate"]["words"].values(),
            *self.payload["transfer_inverse_branch_positive_cone_gate"]["words"].values(),
        ]
        for word in gates:
            for phase in word["phase_records"]:
                self.assertEqual(phase["final_matrix"], identity)

    def test_11_every_farkas_relation_is_explicit_primitive_and_exact(self) -> None:
        gates = [
            self.payload["raw_homology_zigzag_control"]["C26_infeasibility"],
            *self.payload["forward_length_positive_cone_gate"]["words"].values(),
            *self.payload["transfer_inverse_branch_positive_cone_gate"]["words"].values(),
        ]
        for word in gates:
            for phase in word["phase_records"]:
                cert = phase["farkas_infeasibility_certificate"]
                self.assertEqual(cert["weighted_form_sum"], [0, 0, 0, 0])
                self.assertEqual(cert["support_size"], len(cert["terms"]))
                self.assertLessEqual(cert["support_size"], 5)
                self.assertTrue(cert["coefficients_are_primitive_positive_integers"])
                self.assertTrue(all(type(term["coefficient"]) is int and term["coefficient"] > 0 for term in cert["terms"]))
                self.assertEqual(
                    [(term["step"], term["coordinate"]) for term in cert["terms"]],
                    sorted((term["step"], term["coordinate"]) for term in cert["terms"]),
                )
                if cert["certificate_type"] == "POSITIVE_DEPENDENCE":
                    self.assertEqual(cert["support_size"], 2)

    def test_12_roof_inverse_law_is_zero_sum(self) -> None:
        roof = self.payload["projective_roof_cocycle"]
        self.assertEqual(roof["domain"], "normalized projective simplex ell(x)=1")
        self.assertEqual(roof["inverse_pair_sum"], 0)
        self.assertFalse(roof["strictly_positive_on_both_M_and_M_inverse"])

    def test_13_nuclearity_gate_is_infinite_dimensional_only(self) -> None:
        gate = self.payload["same_space_nuclearity"]
        self.assertFalse(gate["compact_hashimoto_possible"])
        self.assertIn("finite graph/finite-Weil", gate["finite_dimensional_exception"])

    def test_14_flat_trace_denominator_is_zero(self) -> None:
        gate = self.payload["identity_word_flat_trace"]
        self.assertEqual(gate["derivative"], "Dh_W=I")
        self.assertEqual(gate["fixed_point_denominator"], "det(I-Dh_W)=0")

    def test_15_route_a_rejects_dynamical_promotion(self) -> None:
        route = self.payload["route_a"]
        self.assertEqual(route["overall"], "ROUTE_A_REJECTED_FOR_DYNAMICAL_PROMOTION")
        self.assertEqual(route["tuple"][:3], ["A1_FAIL", "A2_FAIL", "A3_FAIL"])

    def test_16_stale_payload_hash_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].__setitem__("route_B_authorized", True),
            rehash=False,
            gate="G0_ENVELOPE_AND_PAYLOAD_HASH",
        )

    def test_17_bool_for_integer_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["projective_roof_cocycle"].__setitem__("inverse_pair_sum", False),
            gate="G6_ROOF_COCYCLE",
        )

    def test_18_unknown_nested_key_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["material_passport"].__setitem__("silent_extra", "x"),
            gate="G1_TYPE_STRICT_CONTRACT",
        )

    def test_19_rehashed_forward_phase_count_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["forward_length_positive_cone_gate"]["words"]["C26_W24"].__setitem__("infeasible_phase_count", 23),
            gate="G4_FORWARD_LENGTH_ALL_PHASES",
        )

    def test_20_rehashed_forward_certificate_row_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["forward_length_positive_cone_gate"]["words"]["C25_C1"]["phase_records"][0]["farkas_infeasibility_certificate"]["terms"][0]["linear_form"].__setitem__(1, 99),
            gate="G4_FORWARD_LENGTH_ALL_PHASES",
        )

    def test_21_rehashed_transfer_phase_sequence_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["transfer_inverse_branch_positive_cone_gate"]["words"]["C25_C2"]["phase_records"][1]["action_sequence"].reverse(),
            gate="G5_TRANSFER_BRANCH_ALL_PHASES",
        )

    def test_22_rehashed_transfer_certificate_coefficient_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["transfer_inverse_branch_positive_cone_gate"]["words"]["C26_W24"]["phase_records"][0]["farkas_infeasibility_certificate"]["terms"][0].__setitem__("coefficient", 2),
            gate="G5_TRANSFER_BRANCH_ALL_PHASES",
        )

    def test_23_rehashed_raw_control_witness_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["raw_homology_zigzag_control"]["C25_positive_controls"]["C1"]["phase_zero_positive_integer_witness"].__setitem__(0, 2),
            gate="G3_RAW_HOMOLOGY_CONTROL",
        )

    def test_24_rehashed_raw_agy_misclassification_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["raw_homology_zigzag_control"].__setitem__("classification", "AGY positive length orbit"),
            gate="G3_RAW_HOMOLOGY_CONTROL",
        )

    def test_25_rehashed_chronology_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["conventions"].__setitem__("forward_length_action", "B(t)^T"),
            gate="G11_CHRONOLOGY_CONVENTIONS",
        )

    def test_26_rehashed_roof_law_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["projective_roof_cocycle"].__setitem__("inverse_law", "positive in both directions"),
            gate="G6_ROOF_COCYCLE",
        )

    def test_27_rehashed_nuclearity_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["same_space_nuclearity"].__setitem__("trace_class_hashimoto_possible", True),
            gate="G7_SAME_SPACE_NUCLEARITY",
        )

    def test_28_rehashed_flat_trace_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["identity_word_flat_trace"].__setitem__("standard_isolated_fixed_point_flat_trace_applies", True),
            gate="G8_IDENTITY_WORD_FLAT_TRACE",
        )

    def test_29_rehashed_decision_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].__setitem__("all_forward_length_cyclic_phases", "PASS"),
            gate="G9_DECISIONS",
        )

    def test_30_rehashed_source_path_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"]["files"]["C29_theorem"].__setitem__("path", "wrong"),
            gate="G2_SOURCE_LOCK",
        )

    def test_31_checker_has_ast_import_firewall(self) -> None:
        tree = ast.parse(CHECKER.read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module)
        self.assertFalse(any(name.endswith("c30_producer") for name in imported))

    def test_32_real_checker_cli_accepts_and_rejects(self) -> None:
        good_report = self.root / "good-report.json"
        good = subprocess.run(
            [sys.executable, str(CHECKER), "--certificate", str(self.base_path), "--output", str(good_report)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(good.returncode, 0)
        bad_cert = self.root / "bad.json"
        bad_report = self.root / "bad-report.json"
        mutated = self.mutated(lambda c: c["payload"]["decisions"].__setitem__("C29_lane", "CONTINUE_SCAN"))
        bad_cert.write_text(json.dumps(mutated), encoding="utf-8")
        bad = subprocess.run(
            [sys.executable, str(CHECKER), "--certificate", str(bad_cert), "--output", str(bad_report)],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(bad.returncode, 0)
        self.assertFalse(json.loads(bad_report.read_text(encoding="utf-8"))["all_pass"])

    def test_33_malformed_json_checker_cli_fails_closed(self) -> None:
        bad_cert = self.root / "malformed.json"
        bad_report = self.root / "malformed-report.json"
        bad_cert.write_text("{not-json", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(CHECKER), "--certificate", str(bad_cert), "--output", str(bad_report)],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        report = json.loads(bad_report.read_text(encoding="utf-8"))
        self.assertFalse(report["all_pass"])
        self.assertEqual(report["gates"][0]["status"], "ERROR")

    def test_34_exact_unimodular_inverse_fuzz(self) -> None:
        rng = random.Random(30030)
        identity = CHECK.ident()
        for _ in range(100):
            matrix = CHECK.ident()
            for _ in range(12):
                i, j = rng.sample(range(4), 2)
                scale = rng.choice([-3, -2, -1, 1, 2, 3])
                elementary = CHECK.ident()
                elementary[i][j] = scale
                matrix = CHECK.mul(elementary, matrix)
            inverse = CHECK.integral_inverse(matrix)
            self.assertEqual(CHECK.mul(matrix, inverse), identity)
            self.assertEqual(CHECK.mul(inverse, matrix), identity)

    def test_35_checker_error_is_not_reported_as_pass(self) -> None:
        certificate = self.mutated(
            lambda c: c["payload"]["forward_length_positive_cone_gate"]["words"]["C26_W24"].__setitem__("phase_count", "24")
        )
        report = self.checker_report(certificate)
        self.assertFalse(report["all_pass"])
        self.assertNotEqual(
            next(row for row in report["gates"] if row["gate"] == "G4_FORWARD_LENGTH_ALL_PHASES")["status"],
            "PASS",
        )

    def test_36_identity_trichotomy_and_signed_abelianization_are_exact(self) -> None:
        semantics = self.payload["identity_and_clock_semantics"]
        trichotomy = semantics["identity_trichotomy"]
        self.assertTrue(trichotomy["matrix_holonomy_identity_for_certified_words"])
        self.assertFalse(trichotomy["matrix_holonomy_identity_is_groupoid_unit"])
        self.assertEqual(
            trichotomy["formal_freely_reduced_lengths"],
            {"C25_C1": 6, "C25_C2": 6, "C26_W24": 24},
        )
        abelian = semantics["signed_abelianization"]
        self.assertEqual(abelian["C25_C1"]["nonzero_generator_counts"], {"1b": 1, "3t": 1})
        self.assertEqual(abelian["C25_C2"]["nonzero_generator_counts"], {"4t": 1, "5b": 1})
        self.assertEqual(abelian["C26_W24"]["generator_counts"], {"A": 0, "B": 0, "C": 0})

    def test_37_normalizer_and_repetition_clock_fork_is_explicit(self) -> None:
        semantics = self.payload["identity_and_clock_semantics"]
        normalizer = semantics["projective_normalizer"]
        self.assertEqual(normalizer["identity_holonomy_period"], 0)
        self.assertIn("all chronological prefixes", normalizer["conditional_domain"])
        symmetric = semantics["symmetric_positive_edge_clock"]
        self.assertTrue(symmetric["valid_new_nonbacktracking_graph_suspension"])
        self.assertFalse(symmetric["is_AGY_time"])
        self.assertFalse(symmetric["compatible_with_groupoid_unit_cancellation_e_e_inverse"])
        fork = semantics["repetition_fork"]
        self.assertIn("conditional", fork["intrinsic_projective_normalizer"]["domain_condition"])
        self.assertFalse(fork["intrinsic_projective_normalizer"]["harmonic_repetition_sum_converges"])
        self.assertEqual(
            fork["combinatorial_unit_edge_clock"]["period_of_w_power"],
            {"C25_C1": "6*m", "C25_C2": "6*m", "C26_W24": "24*m"},
        )
        self.assertEqual(
            self.payload["decisions"]["new_symmetric_hashimoto_suspension"],
            "VALID_BUT_DIFFERENT_SYSTEM",
        )

    def test_38_rehashed_groupoid_unit_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["identity_and_clock_semantics"]["identity_trichotomy"].__setitem__("matrix_holonomy_identity_is_groupoid_unit", True),
            gate="G12_IDENTITY_AND_CLOCK_SEMANTICS",
        )

    def test_39_rehashed_signed_abelianization_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["identity_and_clock_semantics"]["signed_abelianization"]["C25_C1"]["nonzero_generator_counts"].__setitem__("1b", 0),
            gate="G12_IDENTITY_AND_CLOCK_SEMANTICS",
        )

    def test_40_rehashed_symmetric_clock_system_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["identity_and_clock_semantics"]["symmetric_positive_edge_clock"].__setitem__("is_AGY_time", True),
            gate="G12_IDENTITY_AND_CLOCK_SEMANTICS",
        )

    def test_41_rehashed_repetition_period_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["identity_and_clock_semantics"]["repetition_fork"]["combinatorial_unit_edge_clock"]["period_of_w_power"].__setitem__("C26_W24", "0"),
            gate="G12_IDENTITY_AND_CLOCK_SEMANTICS",
        )

    def test_42_c26_certificate_type_and_support_censuses_are_not_conflated(self) -> None:
        for gate_name in (
            "forward_length_positive_cone_gate",
            "transfer_inverse_branch_positive_cone_gate",
        ):
            records = self.payload[gate_name]["words"]["C26_W24"]["phase_records"]
            certificates = [
                record["farkas_infeasibility_certificate"] for record in records
            ]
            type_counts = {
                name: sum(cert["certificate_type"] == name for cert in certificates)
                for name in ("NEG_ROW", "POSITIVE_DEPENDENCE")
            }
            self.assertEqual(
                type_counts,
                {"NEG_ROW": 15, "POSITIVE_DEPENDENCE": 9},
            )
        forward_certificates = [
            record["farkas_infeasibility_certificate"]
            for record in self.payload["forward_length_positive_cone_gate"]
            ["words"]["C26_W24"]["phase_records"]
        ]
        support_counts = {
            size: sum(cert["support_size"] == size for cert in forward_certificates)
            for size in (2, 5)
        }
        self.assertEqual(support_counts, {2: 10, 5: 14})

    def test_43_manifest_refresh_rejects_deleted_authored_sources(self) -> None:
        critical_sources = {
            "evaluations/route_a/hcs_c30/20260811T183000Z.yaml",
            "paper/references.bib",
            "paper/sections/0_abstract.tex",
            "paper/sections/1_introduction.tex",
            "paper/sections/2_setting.tex",
            "paper/sections/3_cone_obstruction.tex",
            "paper/sections/4_roof_and_repetition.tex",
            "paper/sections/5_operator_and_flat_trace.tex",
            "paper/sections/6_group_trace_control.tex",
            "paper/sections/7_route_a_and_pivot.tex",
            "paper/sections/8_conclusion.tex",
            "paper/sections/A_certificate_protocol.tex",
            "paper/sections/B_scope_table.tex",
        }
        self.assertTrue(
            critical_sources <= HASH_MANIFEST.REQUIRED_RELATIVE_PATHS
        )

        fixture = self.root / "manifest-deletion-fixture"
        for relative in HASH_MANIFEST.REQUIRED_RELATIVE_PATHS:
            path = fixture / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"fixture\n")

        original_project = HASH_MANIFEST.PROJECT
        original_manifest = HASH_MANIFEST.MANIFEST
        HASH_MANIFEST.PROJECT = fixture
        HASH_MANIFEST.MANIFEST = fixture / "results" / "ARTIFACT_HASHES.sha256"
        try:
            for relative in sorted(critical_sources):
                with self.subTest(deleted=relative):
                    path = fixture / relative
                    path.unlink()
                    with self.assertRaisesRegex(
                        SystemExit, "required release artifacts missing"
                    ):
                        HASH_MANIFEST.tracked_files()
                    path.write_bytes(b"fixture\n")
        finally:
            HASH_MANIFEST.PROJECT = original_project
            HASH_MANIFEST.MANIFEST = original_manifest


if __name__ == "__main__":
    unittest.main()
