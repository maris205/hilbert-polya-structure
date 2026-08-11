#!/usr/bin/env python3
"""Regression and adversarial mutation tests for HCS-C31."""

from __future__ import annotations

import ast
import decimal
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CODE = PROJECT / "code"
PRODUCER = CODE / "c31_producer.py"
CHECKER = CODE / "c31_independent_check.py"
MANIFEST_TOOL = CODE / "c31_hash_manifest.py"


def load_checker():
    name = "c31_checker_for_tests"
    spec = importlib.util.spec_from_file_location(name, CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load C31 checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CHECK = load_checker()


def load_manifest_tool():
    name = "c31_manifest_for_tests"
    spec = importlib.util.spec_from_file_location(name, MANIFEST_TOOL)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load C31 manifest tool")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


MANIFEST = load_manifest_tool()


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


class C31Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary = tempfile.TemporaryDirectory(prefix="c31-tests-")
        cls.root = Path(cls.temporary.name)
        cls.certificate_path = cls.root / "certificate.json"
        supplied = os.environ.get("C31_TEST_CERTIFICATE")
        released = Path(supplied) if supplied else PROJECT / "results" / "c31_certificate.json"
        if released.is_file():
            cls.certificate_path.write_bytes(released.read_bytes())
        else:
            subprocess.run(
                [sys.executable, str(PRODUCER), "--output", str(cls.certificate_path)],
                check=True,
                capture_output=True,
                text=True,
            )
        cls.base_bytes = cls.certificate_path.read_bytes()
        cls.base = json.loads(cls.base_bytes)
        cls.base_report = CHECK.Audit(cls.base).run()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary.cleanup()

    def changed(self, action, *, rehash: bool = True) -> dict[str, object]:
        certificate = json.loads(json.dumps(self.base))
        action(certificate)
        if rehash:
            certificate["payload_sha256"] = canonical_hash(certificate["payload"])
        return certificate

    def assert_rejected(self, action, gate: str, *, rehash: bool = True) -> None:
        report = CHECK.Audit(self.changed(action, rehash=rehash)).run()
        self.assertFalse(report["all_pass"])
        row = next(item for item in report["gates"] if item["gate"] == gate)
        self.assertEqual(row["status"], "FAIL")
        self.assertTrue(row["detail"])

    @property
    def payload(self) -> dict[str, object]:
        return self.base["payload"]

    def test_01_base_certificate_passes_six_independent_gates(self) -> None:
        self.assertTrue(self.base_report["all_pass"])
        self.assertEqual((self.base_report["passed"], self.base_report["total"]), (6, 6))
        self.assertEqual(self.base["schema"], "hcs-c31-bowen-pressure-certificate-v2")

    def test_02_graph_census_and_chronology_are_exact(self) -> None:
        graph = self.payload["higher_block_graph"]
        self.assertEqual((graph["node_count"], graph["edge_count"]), (714, 1156))
        self.assertEqual(graph["nodes"][graph["edges"][0]["source"]], graph["edges"][0]["word"][:-1])
        self.assertEqual(graph["nodes"][graph["edges"][0]["target"]], graph["edges"][0]["word"][1:])
        # Closed non-palindromic chronology sentinel; its first edge is killed by A^T.
        sentinel = (0, 2, 3, 1)
        self.assertTrue(all(CHECK.GRAPH[sentinel[i]][sentinel[(i + 1) % 4]] for i in range(4)))
        self.assertFalse(CHECK.GRAPH[sentinel[1]][sentinel[0]])

    def test_03_every_direct_interval_is_positive_and_expanding(self) -> None:
        graph = self.payload["higher_block_graph"]
        lower_bound = Fraction(773, 224)
        for edge in graph["edges"]:
            low = Fraction(edge["j_lower"])
            high = Fraction(edge["j_upper"])
            self.assertLessEqual(lower_bound, low)
            self.assertLessEqual(low, high)
            self.assertLessEqual(edge["jacobi_rounds"], 100)

    def test_04_root_bracket_and_collatz_margins_are_strict(self) -> None:
        pressure = self.payload["pressure_certificate"]
        self.assertEqual(pressure["decimal_bracket"], ["0.277980", "0.277987"])
        self.assertGreater(Fraction(pressure["lower_endpoint"]["strict_margin"]), 0)
        self.assertGreater(Fraction(pressure["upper_endpoint"]["strict_margin"]), 0)
        target = Fraction(277982981676189, 10**15)
        self.assertLess(Fraction(pressure["certified_root_bracket"][0]), target)
        self.assertLess(target, Fraction(pressure["certified_root_bracket"][1]))

    def test_05_rational_sqrt_enclosure_control(self) -> None:
        lower, upper = CHECK.rational_sqrt_box(Fraction(2))
        self.assertLessEqual(lower * lower, 2)
        self.assertGreaterEqual(upper * upper, 2)
        self.assertLessEqual(upper - lower, Fraction(1, 10**50))

    def test_06_rational_log_and_exp_enclosures_are_ordered(self) -> None:
        log_box = CHECK.rational_log(Fraction(5))
        self.assertLess(log_box[0], log_box[1])
        exponent = Fraction(2, 5)
        exp_box = CHECK.rational_exp_minus(exponent)
        self.assertTrue(Fraction(0) < exp_box[0] < exp_box[1] < 1)
        with decimal.localcontext() as context:
            context.prec = 90
            truth = (-decimal.Decimal(2) / decimal.Decimal(5)).exp()
            observed_lower = decimal.Decimal(exp_box[0].numerator) / decimal.Decimal(exp_box[0].denominator)
            observed_upper = decimal.Decimal(exp_box[1].numerator) / decimal.Decimal(exp_box[1].denominator)
            self.assertLess(observed_lower, truth)
            self.assertGreater(observed_upper, truth)

    def test_07_checker_does_not_import_or_execute_producer(self) -> None:
        tree = ast.parse(CHECKER.read_text(encoding="utf-8"))
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.append(node.module)
        self.assertFalse(any("c31_producer" in name for name in imports))
        self.assertFalse(any(name in {"numpy", "scipy", "mpmath"} for name in imports))

    def test_08_proof_path_has_no_scipy_numpy_or_mpmath(self) -> None:
        source = PRODUCER.read_text(encoding="utf-8")
        self.assertNotIn("import scipy", source)
        self.assertNotIn("import numpy", source)
        self.assertNotIn("import mpmath", source)
        self.assertIn("floating Perron", source)

    def test_09_stale_payload_hash_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["claims"].__setitem__("bowen_pressure_root_exists_uniquely_in_bracket", False),
            "G0_ENVELOPE_AND_HASH",
            rehash=False,
        )

    def test_10_unknown_nested_key_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["protocol"].__setitem__("silent_extra", 1),
            "G2_TYPE_STRICT_PROTOCOL",
        )

    def test_11_source_hash_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"]["instability_root_ledger"].__setitem__("sha256", "0" * 64),
            "G1_SOURCE_LOCK",
        )

    def test_12_bool_for_integer_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["protocol"].__setitem__("window_state_length", True),
            "G2_TYPE_STRICT_PROTOCOL",
        )

    def test_13_transposed_adjacency_mutation_is_rejected(self) -> None:
        def mutate(c):
            matrix = c["payload"]["protocol"]["adjacency_source_rows_target_columns"]
            c["payload"]["protocol"]["adjacency_source_rows_target_columns"] = [list(row) for row in zip(*matrix)]

        self.assert_rejected(mutate, "G2_TYPE_STRICT_PROTOCOL")

    def test_14_removed_edge_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["higher_block_graph"]["edges"].pop(),
            "G3_ALL_CYLINDER_GRAPH",
        )

    def test_15_edge_orientation_mutation_is_rejected(self) -> None:
        def mutate(c):
            edge = c["payload"]["higher_block_graph"]["edges"][1]
            edge["source"], edge["target"] = edge["target"], edge["source"]

        self.assert_rejected(mutate, "G3_ALL_CYLINDER_GRAPH")

    def test_16_sign_chronology_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["higher_block_graph"]["edges"][10].__setitem__("signs", "+" * 14),
            "G3_ALL_CYLINDER_GRAPH",
        )

    def test_17_illicit_interval_narrowing_mutation_is_rejected(self) -> None:
        def mutate(c):
            edge = c["payload"]["higher_block_graph"]["edges"][20]
            edge["j_lower"] = str(Fraction(edge["j_lower"]) + Fraction(1, 10**50))

        self.assert_rejected(mutate, "G3_ALL_CYLINDER_GRAPH")

    def test_18_jacobi_round_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["higher_block_graph"]["edges"][0].__setitem__("jacobi_rounds", 0),
            "G3_ALL_CYLINDER_GRAPH",
        )

    def test_19_rounding_grid_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["protocol"].__setitem__("sqrt_grid_denominator", 10**49),
            "G2_TYPE_STRICT_PROTOCOL",
        )

    def test_20_endpoint_swap_mutation_is_rejected(self) -> None:
        def mutate(c):
            pressure = c["payload"]["pressure_certificate"]
            pressure["lower_endpoint"]["s"], pressure["upper_endpoint"]["s"] = (
                pressure["upper_endpoint"]["s"],
                pressure["lower_endpoint"]["s"],
            )

        self.assert_rejected(mutate, "G4_RATIONAL_COLLATZ_BRACKET")

    def test_21_bool_in_perron_vector_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["pressure_certificate"]["lower_endpoint"]["vector"].__setitem__(0, True),
            "G4_RATIONAL_COLLATZ_BRACKET",
        )

    def test_22_perron_vector_mutation_is_rejected(self) -> None:
        def mutate(c):
            vector = c["payload"]["pressure_certificate"]["upper_endpoint"]["vector"]
            vector[0] = 1

        self.assert_rejected(mutate, "G4_RATIONAL_COLLATZ_BRACKET")

    def test_23_collatz_margin_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["pressure_certificate"]["lower_endpoint"].__setitem__("strict_margin", "1/2"),
            "G4_RATIONAL_COLLATZ_BRACKET",
        )

    def test_24_bracket_width_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["pressure_certificate"].__setitem__("width", "1/1000000"),
            "G4_RATIONAL_COLLATZ_BRACKET",
        )

    def test_25_legacy_target_grafting_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["pressure_certificate"].__setitem__(
                "legacy_period20_high_precision_root", "0.277980000000000"
            ),
            "G4_RATIONAL_COLLATZ_BRACKET",
        )

    def test_26_hilbert_polya_promotion_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["claims"].__setitem__("this_is_not_a_fredholm_or_hilbert_polya_certificate", False),
            "G5_SCOPE_AND_ROUTE_A",
        )

    def test_27_route_a_A2_promotion_mutation_is_rejected(self) -> None:
        self.assert_rejected(
            lambda c: c["payload"]["claims"]["route_a_tuple"].__setitem__(1, "A2_PASS"),
            "G5_SCOPE_AND_ROUTE_A",
        )

    def test_28_unexpected_checker_exception_is_reported_as_error(self) -> None:
        audit = CHECK.Audit(self.base)
        audit.gate("ERROR_SENTINEL", lambda: 1 / 0)
        self.assertEqual(audit.rows[0]["status"], "ERROR")
        self.assertIn("ZeroDivisionError", audit.rows[0]["detail"])

    def test_29_malformed_json_is_rejected_by_isolated_cli(self) -> None:
        malformed = self.root / "malformed.json"
        malformed.write_text("{not-json", encoding="utf-8")
        output = self.root / "malformed-report.json"
        process = subprocess.run(
            [sys.executable, str(CHECKER), "--certificate", str(malformed), "--output", str(output)],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(process.returncode, 0)
        self.assertFalse(output.exists())

    def test_30_manifest_requires_every_authored_release_file(self) -> None:
        expected = {
            "README.md", "REPOSITORY_UPDATE.md", "RESEARCH_QUESTION.md",
            "METHODOLOGY_BLUEPRINT.md", "DEVILS_ADVOCATE.md", "PAPER_PLAN.md",
            "NARRATIVE_REPORT.md", "THEOREM_PACKAGE.md", "DERIVATION_PACKAGE.md",
            "SOURCE_AUDIT.md", "route_a_evaluation.yaml",
            "evaluations/route_a/HCS-C31/20260811T123751Z.yaml",
            "code/README.md", "code/c31_producer.py",
            "code/c31_independent_check.py", "code/test_c31.py",
            "code/c31_hash_manifest.py", "code/run_c31.sh",
            "results/README.md", "results/RESULTS.md",
            "results/VALIDATION_REPORT.md", "results/TEST_REPORT.md",
            "results/c31_certificate.json", "results/c31_independent_check.json",
            "paper/README.md", "paper/COMPILATION_REPORT.md", "paper/main.tex",
            "paper/math_commands.tex", "paper/references.bib", "paper/main.pdf",
            "paper/sections/0_abstract.tex", "paper/sections/1_introduction.tex",
            "paper/sections/2_context.tex", "paper/sections/3_survivor.tex",
            "paper/sections/4_roof.tex", "paper/sections/5_pressure_certificate.tex",
            "paper/sections/6_zeta_dimension.tex",
            "paper/sections/7_route_a_conclusion.tex",
            "paper/sections/A_interval_arithmetic.tex",
            "paper/sections/B_reproducibility.tex",
        }
        self.assertEqual(MANIFEST.REQUIRED, expected)
        with tempfile.TemporaryDirectory(prefix="c31-manifest-") as folder:
            fixture = Path(folder)
            for relative in expected:
                path = fixture / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(relative + "\n", encoding="utf-8")
            original_project = MANIFEST.PROJECT
            try:
                MANIFEST.PROJECT = fixture
                self.assertEqual(len(MANIFEST.render().splitlines()), 40)
                for relative in sorted(expected):
                    path = fixture / relative
                    original = path.read_bytes()
                    path.unlink()
                    with self.assertRaisesRegex(SystemExit, "required C31 artifacts missing"):
                        MANIFEST.render()
                    path.write_bytes(original)
            finally:
                MANIFEST.PROJECT = original_project


if __name__ == "__main__":
    unittest.main()
