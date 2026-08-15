#!/usr/bin/env python3
"""Hostile schema, rebound, source-lock, and rollback tests for HCS-C56."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
CHECKER_PATH = CODE / "c56_checker.py"
PRODUCER_PATH = CODE / "c56_producer.py"
ATOMIC_PATH = CODE / "c56_atomic_promote.py"
MANIFEST_PATH = CODE / "c56_hash_manifest.py"
RUNNER_PATH = CODE / "run_all.sh"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise AssertionError("module loader unavailable")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


checker = load_module("c56_checker_for_tests", CHECKER_PATH)
producer = load_module("c56_producer_for_tests", PRODUCER_PATH)
atomic = load_module("c56_atomic_for_tests", ATOMIC_PATH)
manifest = load_module("c56_manifest_for_tests", MANIFEST_PATH)


def canonical_json(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def assign_path(root, path: tuple, value) -> None:
    target = root
    for component in path[:-1]:
        target = target[component]
    target[path[-1]] = value


def rebound_bytes(certificate: dict) -> bytes:
    certificate["payload_sha256"] = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
    certificate["schema_sha256"] = hashlib.sha256(canonical_json(certificate["schema"])).hexdigest()
    return json.dumps(certificate, sort_keys=True, indent=2, ensure_ascii=False).encode("utf-8") + b"\n"


class C56Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate_path = Path(os.environ.get("C56_CERTIFICATE", PROJECT / "results/c56_certificate.json"))
        cls.schema_path = Path(os.environ.get("C56_SCHEMA", PROJECT / "results/c56_schema.json"))
        cls.check_path = Path(os.environ.get("C56_CHECK_REPORT", PROJECT / "results/c56_check_report.json"))
        cls.raw = cls.certificate_path.read_bytes()
        cls.certificate = checker.strict_load(cls.raw)
        cls.schema_raw = cls.schema_path.read_bytes()
        cls.schema = checker.strict_load(cls.schema_raw, maximum=100_000)
        cls.report = checker.strict_load(cls.check_path.read_bytes(), maximum=100_000)

    def test_000_baseline_schema_envelope_and_all_leaf_report(self):
        expected_schema = checker.expected_schema(self.certificate["payload"])
        checker.deep_exact(self.certificate["schema"], expected_schema, ("certificate_schema",))
        checker.deep_exact(self.schema, expected_schema, ("standalone_schema",))
        self.assertEqual(
            self.certificate["payload_sha256"],
            hashlib.sha256(canonical_json(self.certificate["payload"])).hexdigest(),
        )
        self.assertEqual(
            self.certificate["schema_sha256"],
            hashlib.sha256(canonical_json(self.certificate["schema"])).hexdigest(),
        )
        rebound = self.report["scalar_leaf_rebound"]
        self.assertEqual(self.report["result"], "PASS_PREFREEZE_CODE_RESULTS")
        self.assertEqual(self.report["semantic_gate_count"], 10)
        self.assertEqual(rebound["payload_scalar_leaves"], checker.scalar_leaf_count(self.certificate["payload"]))
        self.assertEqual(rebound["schema_scalar_leaves"], checker.scalar_leaf_count(self.certificate["schema"]))
        self.assertEqual(rebound["envelope_digest_leaves"], 2)
        self.assertEqual(
            rebound["rebound_mutations_rejected"],
            rebound["payload_scalar_leaves"] + rebound["schema_scalar_leaves"] + 2,
        )

    def test_001_strict_json_malformed_inputs(self):
        duplicate = self.raw.replace(b'  "payload":', b'  "payload": {},\n  "payload":', 1)
        with self.assertRaises(AssertionError):
            checker.strict_load(duplicate)
        for malformed in (b'{"x":1.0}', b'{"x":NaN}', b'{"x":-0}', b'\xef\xbb\xbf{}', b'\xff'):
            with self.subTest(malformed=malformed[:20]), self.assertRaises((AssertionError, UnicodeDecodeError, json.JSONDecodeError)):
                checker.strict_load(malformed)
        with self.assertRaises(AssertionError):
            checker.strict_load(b" " * (checker.MAX_CERTIFICATE_BYTES + 1))

    def test_002_preflight_rejects_boolean_integer_and_unknown_schema(self):
        payload = copy.deepcopy(self.certificate["payload"])
        payload["grassmann_main_chart"]["dp_basis_size"] = True
        with self.assertRaises(AssertionError):
            checker.semantic_preflight(payload)
        malformed_schema = copy.deepcopy(self.schema)
        malformed_schema["unexpected"] = True
        with self.assertRaises(AssertionError):
            checker.deep_exact(malformed_schema, checker.expected_schema(self.certificate["payload"]))

    def test_003_complete_standard_box_and_hilbert_counts(self):
        main = self.certificate["payload"]["grassmann_main_chart"]
        leading = [tuple(row["leading_monomial_abcd"]) for row in main["dp_basis_rows"]]
        standards, counts = checker.standard_monomials(leading)
        self.assertEqual(standards, main["standard_monomials_abcd"])
        self.assertEqual(counts, [1, 4, 10, 12, 0])
        self.assertEqual(main["standard_monomial_degree_counts_0_to_4"], counts)

    def test_004_targeted_all_leaf_inventory_coverage(self):
        paths = set(checker.scalar_paths(self.certificate["payload"]))
        for row in range(20):
            self.assertIn(("surface", "primitive_coefficients", row, "coefficient"), paths)
            for exponent in range(4):
                self.assertIn(("surface", "primitive_coefficients", row, "exponents_u0_to_u3", exponent), paths)
        for chart in range(5):
            self.assertIn(("grassmann_complement", "charts", chart, "chart"), paths)
            self.assertIn(("grassmann_complement", "charts", chart, "p01_zero_equation"), paths)
        for shape, length in enumerate((28, 27, 27, 27)):
            for coefficient in range(length):
                self.assertIn(("grassmann_main_chart", "lex_shape", shape, "tail_coefficients_d_0_up", coefficient), paths)
        for prime in checker.WITNESS_PATTERNS:
            base = ("irreducibility", "modular_witnesses", str(prime))
            for leaf in ("prime", "factorization_unit_mod_p", "derivative_gcd_degree", "surface_good_reduction"):
                self.assertIn(base + (leaf,), paths)
            for factor_index, factor in enumerate(self.certificate["payload"]["irreducibility"]["modular_witnesses"][str(prime)]["factors"]):
                self.assertIn(base + ("factors", factor_index, "multiplicity"), paths)
                for coefficient in range(len(factor["coefficients_mod_p_0_up"])):
                    self.assertIn(base + ("factors", factor_index, "coefficients_mod_p_0_up", coefficient), paths)
        for subtree in ("c55_source_lock", "surface", "grassmann_main_chart", "grassmann_complement", "irreducibility", "we6", "theorem_gates", "material_passport"):
            self.assertTrue(any(path and path[0] == subtree for path in paths))
        self.assertIn(("we6", "simple_roots", 0, 0), paths)
        self.assertIn(("we6", "line_classes", 0, 0), paths)
        self.assertIn(("we6", "simple_reflection_line_permutations", 0, 0), paths)

    def test_005_cold_rebound_mutation_in_every_semantic_subtree(self):
        mutations = {
            "material_passport": (("material_passport", "artifact_status"), "PREFREEZE_FORGED"),
            "c55_source_lock": (("c55_source_lock", "implementation_commit"), "0" * 40),
            "surface": (("surface", "primitive_coefficients", 0, "coefficient"), self.certificate["payload"]["surface"]["primitive_coefficients"][0]["coefficient"] + 1),
            "grassmann_main_chart": (("grassmann_main_chart", "dp_basis_size"), 22),
            "grassmann_complement": (("grassmann_complement", "charts", 0, "chart"), "U99"),
            "irreducibility": (("irreducibility", "eliminant_degree"), 28),
            "we6": (("we6", "group_order"), 51841),
            "theorem_gates": (("theorem_gates", "finite_L_line_field_degree_divisible_by_27"), False),
        }
        with tempfile.TemporaryDirectory(prefix="c56-cold-mutations-") as temporary:
            root = Path(temporary)
            for name, (path, value) in mutations.items():
                with self.subTest(subtree=name):
                    mutant = copy.deepcopy(self.certificate)
                    assign_path(mutant["payload"], path, value)
                    source = root / f"{name}.json"
                    output = root / f"{name}.check.json"
                    source.write_bytes(rebound_bytes(mutant))
                    output.write_text('{"result":"STALE_PASS"}\n', encoding="utf-8")
                    completed = subprocess.run(
                        [sys.executable, str(CHECKER_PATH), str(source), "--output", str(output)],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        check=False,
                    )
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertFalse(output.exists())

    def test_006_p37_and_group_semantic_firewalls(self):
        payload = self.certificate["payload"]
        gates = payload["theorem_gates"]
        for key in (
            "p37_surface_good_reduction_gate",
            "p37_eliminant_leading_coefficient_nonzero_and_squarefree_unramified_gate",
            "p37_complete_factor_multiply_back_cycle_type_gate",
            "p37_target_class_outside_index_two_Coxeter_kernel_gate",
        ):
            self.assertIs(gates[key], True)
        witness = payload["irreducibility"]["modular_witnesses"]["37"]
        self.assertIs(witness["surface_good_reduction"], True)
        self.assertNotEqual(witness["leading_coefficient_mod_p"], 0)
        self.assertIs(witness["squarefree"], True)
        self.assertIs(witness["factor_multiplication_rebound"], True)
        self.assertEqual(witness["factor_degrees"], [2, 5, 5, 5, 10])
        we6 = payload["we6"]
        self.assertEqual((we6["group_order"], we6["index_two_kernel_order"]), (51840, 25920))
        self.assertEqual((we6["target_in_index_two_kernel_count"], we6["target_outside_index_two_kernel_count"]), (0, 5184))
        self.assertEqual(we6["S27_odd_element_count"], 0)
        self.assertIn("not_S27_sign", we6["index_two_kernel_definition"])
        self.assertEqual(self.report["picard_fixed_rank"], 1)
        self.assertIs(self.report["written_Hochschild_Serre_rank_bridge_required"], True)
        self.assertEqual(self.report["derived_rational_picard_rank"], 1)

    def test_007_finite_L_and_external_bridge_scope(self):
        gates = self.certificate["payload"]["theorem_gates"]
        self.assertIs(gates["E_is_Galois_claimed"], False)
        self.assertIs(gates["finite_L_line_defines_injective_conjugate_E_embedding"], True)
        self.assertIs(gates["finite_L_line_field_degree_divisible_by_27"], True)
        self.assertIn("Cayley-Salmon", gates["classical_total_27_lines_external_input"])
        self.assertIn("Theorem_2", gates["line_section_rank_external_input"])
        self.assertIn("Corollary_53", gates["simple_zero_external_input"])
        self.assertIn("Corollary_54", gates["separability_external_input"])
        self.assertIs(gates["rational_picard_rank_uses_Hochschild_Serre_torsion_rank_bridge"], True)

    def test_008_singular_diagnostic_and_missing_marker_fail_closed(self):
        original = producer.run
        try:
            producer.run = lambda *args, **kwargs: subprocess.CompletedProcess([], 0, "? error: forged backend\n", "")
            with self.assertRaises(AssertionError):
                producer.run_singular_script("quit;")
            producer.run = lambda *args, **kwargs: subprocess.CompletedProcess([], 0, "ordinary output\n", "")
            with self.assertRaises(AssertionError):
                producer.run_singular_script("quit;")
        finally:
            producer.run = original

    def test_009_optimized_python_removes_stale_producer_and_checker_outputs(self):
        environment = dict(os.environ)
        environment["PYTHONOPTIMIZE"] = "1"
        with tempfile.TemporaryDirectory(prefix="c56-optimize-") as temporary:
            root = Path(temporary)
            certificate = root / "certificate.json"
            schema = root / "schema.json"
            certificate.write_text('{"result":"STALE_PASS"}\n', encoding="utf-8")
            schema.write_text('{"result":"STALE_PASS"}\n', encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(PRODUCER_PATH), "--output", str(certificate), "--schema-output", str(schema)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertFalse(certificate.exists())
            self.assertFalse(schema.exists())
            source = root / "input.json"
            output = root / "check.json"
            source.write_bytes(self.raw)
            output.write_text('{"result":"STALE_PASS"}\n', encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(CHECKER_PATH), str(source), "--output", str(output)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertFalse(output.exists())

    def test_010_rollback_atomic_four_file_group(self):
        for initially_existing in (False, True):
            for failure_move in range(1, 5):
                with self.subTest(existing=initially_existing, move=failure_move), tempfile.TemporaryDirectory(prefix="c56-rollback-") as temporary:
                    root = Path(temporary)
                    stage = root / "stage"
                    results = root / "results"
                    stage.mkdir(); results.mkdir()
                    sources = [stage / name for name in atomic.EXPECTED_TARGET_NAMES]
                    targets = [results / name for name in atomic.EXPECTED_TARGET_NAMES]
                    for index, source in enumerate(sources):
                        source.write_bytes(f"new-{index}".encode("ascii"))
                        source.chmod(0o640 + index)
                    original_modes = []
                    if initially_existing:
                        for index, target in enumerate(targets):
                            target.write_bytes(f"old-{index}".encode("ascii"))
                            target.chmod(0o600 + index)
                            original_modes.append(stat.S_IMODE(target.stat().st_mode))
                    self.assertFalse(atomic.promote(list(zip(sources, targets)), failure_move, result_dir=results))
                    if initially_existing:
                        self.assertEqual([target.read_bytes() for target in targets], [f"old-{index}".encode("ascii") for index in range(4)])
                        self.assertEqual([stat.S_IMODE(target.stat().st_mode) for target in targets], original_modes)
                    else:
                        self.assertTrue(all(not target.exists() for target in targets))
                    self.assertFalse(any(path.name.startswith(".c56-") for path in results.iterdir()))

        with tempfile.TemporaryDirectory(prefix="c56-promote-") as temporary:
            root = Path(temporary); stage = root / "stage"; results = root / "results"
            stage.mkdir(); results.mkdir()
            sources = [stage / name for name in atomic.EXPECTED_TARGET_NAMES]
            targets = [results / name for name in atomic.EXPECTED_TARGET_NAMES]
            for index, source in enumerate(sources):
                source.write_bytes(f"new-{index}".encode("ascii")); source.chmod(0o640 + index)
            self.assertTrue(atomic.promote(list(zip(sources, targets)), result_dir=results))
            self.assertEqual([target.read_bytes() for target in targets], [f"new-{index}".encode("ascii") for index in range(4)])
            self.assertEqual([stat.S_IMODE(target.stat().st_mode) for target in targets], [0o640 + index for index in range(4)])
            self.assertFalse(any(path.name.startswith(".c56-") for path in results.iterdir()))

    def test_011_atomic_hostile_scope_lock_symlink_and_source_nonmutation(self):
        with tempfile.TemporaryDirectory(prefix="c56-atomic-hostile-") as temporary:
            root = Path(temporary); stage = root / "stage"; results = root / "results"
            stage.mkdir(); results.mkdir()
            sources = [stage / name for name in atomic.EXPECTED_TARGET_NAMES]
            targets = [results / name for name in atomic.EXPECTED_TARGET_NAMES]
            for index, source in enumerate(sources):
                source.write_bytes(f"source-{index}".encode("ascii"))
            source_preimages = [(source.read_bytes(), stat.S_IMODE(source.stat().st_mode)) for source in sources]
            swapped = list(targets); swapped[0], swapped[1] = swapped[1], swapped[0]
            with self.assertRaises(atomic.PromotionValidationError):
                atomic.promote(list(zip(sources, swapped)), result_dir=results)
            outside = root / "outside.json"
            malformed = list(targets); malformed[-1] = outside
            with self.assertRaises(atomic.PromotionValidationError):
                atomic.promote(list(zip(sources, malformed)), result_dir=results)
            real_source = sources[0]
            symlink_source = stage / "symlink.json"
            symlink_source.symlink_to(real_source)
            hostile_sources = list(sources); hostile_sources[0] = symlink_source
            with self.assertRaises(atomic.PromotionValidationError):
                atomic.promote(list(zip(hostile_sources, targets)), result_dir=results)
            lock = results / ".c56-atomic-promote.lock"
            lock.write_bytes(b"FOREIGN_LOCK\n")
            with self.assertRaises(atomic.PromotionValidationError):
                atomic.promote(list(zip(sources, targets)), result_dir=results)
            self.assertEqual(lock.read_bytes(), b"FOREIGN_LOCK\n")
            lock.unlink()
            self.assertEqual(
                [(source.read_bytes(), stat.S_IMODE(source.stat().st_mode)) for source in sources],
                source_preimages,
            )
            self.assertFalse(any(path.name.startswith(".c56-") for path in results.iterdir()))

    def test_012_scoped_manifest_exact_inventory_path_safety_and_self_exclusion(self):
        overrides = {
            manifest.CERTIFICATE_RELATIVE: self.certificate_path,
            manifest.SCHEMA_RELATIVE: self.schema_path,
            manifest.CHECK_RELATIVE: self.check_path,
        }
        value = manifest.manifest_object(overrides)
        self.assertEqual(value["entry_count"], len(manifest.SCOPED_REQUIRED))
        paths = [entry["path"] for entry in value["entries"]]
        self.assertEqual(paths, sorted(manifest.SCOPED_REQUIRED))
        self.assertNotIn(manifest.MANIFEST_RELATIVE, paths)
        self.assertIs(value["manifest_self_included"], False)
        for path in paths:
            self.assertTrue(manifest.safe_relative(path))
        for unsafe in ("/absolute", "../escape", "code/../escape", "code\\escape", "./code/file"):
            self.assertFalse(manifest.safe_relative(unsafe))
        original_inventory = manifest.live_inventory
        try:
            manifest.live_inventory = lambda *, ignore_private_stage: original_inventory(ignore_private_stage=ignore_private_stage) | {"code/UNEXPECTED_C56_DEBRIS"}
            with self.assertRaises(AssertionError):
                manifest.manifest_object(overrides)
        finally:
            manifest.live_inventory = original_inventory
        with tempfile.TemporaryDirectory(prefix="c56-manifest-symlink-") as temporary:
            real = Path(temporary) / "real.json"; real.write_bytes(self.raw)
            symlink = Path(temporary) / "symlink.json"; symlink.symlink_to(real)
            hostile = dict(overrides); hostile[manifest.CERTIFICATE_RELATIVE] = symlink
            with self.assertRaises(AssertionError):
                manifest.manifest_object(hostile)

    def test_013_live_and_dangling_output_symlinks_fail_closed(self):
        environment = dict(os.environ)
        environment.pop("PYTHONOPTIMIZE", None)
        with tempfile.TemporaryDirectory(prefix="c56-output-symlink-") as temporary:
            root = Path(temporary)
            external = root / "external.json"
            external.write_bytes(b"EXTERNAL_SENTINEL")
            missing_external = root / "must-not-be-created.json"
            for executable, arguments in (
                (PRODUCER_PATH, lambda output: ["--output", str(output)]),
                (CHECKER_PATH, lambda output: [str(self.certificate_path), "--output", str(output)]),
            ):
                for name, target in (("live", external), ("dangling", missing_external)):
                    with self.subTest(executable=executable.name, symlink=name):
                        output = root / f"{executable.stem}-{name}.json"
                        output.symlink_to(target)
                        completed = subprocess.run(
                            [sys.executable, str(executable), *arguments(output)],
                            env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False,
                        )
                        self.assertNotEqual(completed.returncode, 0)
                        self.assertTrue(output.is_symlink())
                        self.assertEqual(external.read_bytes(), b"EXTERNAL_SENTINEL")
                        self.assertFalse(missing_external.exists())

    def test_014_no_tmp_reconnaissance_digest_or_producer_import_in_checker(self):
        checker_source = CHECKER_PATH.read_text(encoding="utf-8")
        self.assertNotIn("import c56_producer", checker_source)
        self.assertNotIn("from c56_producer", checker_source)
        serialized_payload = canonical_json(self.certificate["payload"])
        self.assertNotIn(b"/tmp/", serialized_payload)
        self.assertIs(self.certificate["payload"]["material_passport"]["tmp_reconnaissance_is_theorem_evidence"], False)


if __name__ == "__main__":
    if sys.flags.optimize or os.environ.get("PYTHONOPTIMIZE") not in (None, "", "0"):
        raise SystemExit("optimized Python is forbidden")
    unittest.main()
