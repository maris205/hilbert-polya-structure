#!/usr/bin/env python3
"""Paper-26 Stage-4 support for REV-04 and REV-08.

This module has two deliberately bounded jobs:

1. bind the complete transitive project-source closure used by the frozen
   Round-8 rebuild and fail closed if any bound byte or dynamic-import edge
   drifts; and
2. derive two target-blind rational cohomology controls from the frozen
   Schreier definitions and compare their exact degree-moment failures with
   the already frozen real-newform coordinate k=2y+z.

It never writes the canonical Round-8 result files.  Its only result files are
new ``stage4_*`` support artifacts written to an explicitly supplied output
directory.  No A2 computation, determinant construction, target-prime lookup,
zero matching, Route-B invocation, or cross-instance owner deduplication is
performed.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
import csv
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Iterable, Sequence


DATE = "2026-08-30"
SCHEMA_MANIFEST = "p26-stage4-round8-dependency-manifest/1.0"
SCHEMA_SUMMARY = "p26-stage4-matched-exact-control-summary/1.0"
SCHEMA_RECEIPT = "p26-stage4-round8-support-receipt/1.0"
FORMAL_TUPLE = "(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)"

PROJECT_DIR = Path(__file__).resolve().parents[1]
CODE_DIR = PROJECT_DIR / "code"

MANIFEST_RELATIVE_PATH = "notes/stage4_round8_dependency_manifest.json"
ROUND8_ENTRYPOINT = "code/round8_exact_taxonomy.py"
SUPPORT_ENTRYPOINT = "code/stage4_round8_support.py"

LOCKED_INPUT_PATHS = (
    "results/round4_hecke_cycle_ledger.csv",
    "results/round6_quadratic_degree_moment_ledger.csv",
)
CANONICAL_RESULT_PATHS = (
    "results/round8_artifact_manifest.json",
    "results/round8_exact_group_moment_taxonomy_ledger.csv",
    "results/round8_exact_instance_taxonomy_ledger.csv",
    "results/round8_summary.json",
)
LEGACY_RECEIPT_PATHS = (
    "experiments/round8_reproducibility_receipt.json",
)
LEGACY_SUPPORT_PATHS = (
    "code/test_round8_exact_taxonomy.py",
    "experiments/reproduce_round8.sh",
    "notes/round8_taxonomy_freeze.md",
    "notes/round8_exact_taxonomy_theorem.md",
)
STAGE4_VERIFICATION_PATHS = (
    "code/test_stage4_round8_support.py",
    "experiments/reproduce_stage4_round8_support.sh",
)

RESULT_LEDGER_NAME = "stage4_matched_exact_control_decomposition.csv"
RESULT_SUMMARY_NAME = "stage4_matched_exact_control_summary.json"
RECEIPT_NAME = "stage4_round8_support_receipt.json"

STUDIED_FUNCTIONAL = (2, 1)
CONTROL_COUNT = 2
SCALAR_LAWS = ("a_p", "a_p_squared", "a_p_squared_minus_p")


class SupportError(RuntimeError):
    """Fail-closed Stage-4 support error."""


def canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def safe_project_path(relative_path: str) -> Path:
    candidate = Path(relative_path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise SupportError(f"unsafe project-relative path: {relative_path!r}")
    path = PROJECT_DIR / candidate
    if not path.is_file() or path.is_symlink():
        raise SupportError(f"missing regular no-symlink file: {relative_path}")
    resolved_root = PROJECT_DIR.resolve()
    resolved = path.resolve()
    if not resolved.is_relative_to(resolved_root):
        raise SupportError(f"path escapes project root: {relative_path}")
    return path


def binding(relative_path: str) -> dict[str, object]:
    path = safe_project_path(relative_path)
    return {
        "path": relative_path,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


class _DynamicDependencyVisitor(ast.NodeVisitor):
    """Find only executable local-Python loader references.

    Round 7/8 call ``_load_module(<filename.py>, ...)`` directly.  Round 4
    constructs its local source path with ``Path(__file__).with_name`` inside
    a ``_load_*`` function.  Test-file names mentioned by output-binding code
    are intentionally not dependencies and are therefore excluded.
    """

    def __init__(self) -> None:
        self.function_stack: list[str] = []
        self.filenames: set[str] = set()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.function_stack.append(node.name)
        self.generic_visit(node)
        self.function_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.function_stack.append(node.name)
        self.generic_visit(node)
        self.function_stack.pop()

    @staticmethod
    def _constant_python_name(node: ast.AST) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if node.value.endswith(".py"):
                return node.value
        return None

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Name) and node.func.id == "_load_module":
            if node.args:
                name = self._constant_python_name(node.args[0])
                if name is not None:
                    self.filenames.add(name)
        elif (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "with_name"
            and self.function_stack
            and self.function_stack[-1].startswith("_load_")
            and node.args
        ):
            name = self._constant_python_name(node.args[0])
            if name is not None:
                self.filenames.add(name)
        self.generic_visit(node)


def local_python_dependencies(relative_path: str) -> tuple[str, ...]:
    path = safe_project_path(relative_path)
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeDecodeError) as exc:
        raise SupportError(f"cannot parse dependency source {relative_path}: {exc}")
    visitor = _DynamicDependencyVisitor()
    visitor.visit(tree)
    dependencies = []
    for filename in sorted(visitor.filenames):
        target = f"code/{filename}"
        safe_project_path(target)
        dependencies.append(target)
    return tuple(dependencies)


def discover_round8_graph() -> tuple[list[dict[str, str]], tuple[str, ...]]:
    pending = [ROUND8_ENTRYPOINT]
    seen: set[str] = set()
    edges: set[tuple[str, str]] = set()
    while pending:
        source = pending.pop()
        if source in seen:
            continue
        seen.add(source)
        for target in local_python_dependencies(source):
            edges.add((source, target))
            if target not in seen:
                pending.append(target)
    edge_rows = [
        {"from": source, "to": target, "mechanism": "local_dynamic_import"}
        for source, target in sorted(edges)
    ]
    return edge_rows, tuple(sorted(seen))


def _binding_list(paths: Iterable[str]) -> list[dict[str, object]]:
    return [binding(path) for path in sorted(set(paths))]


def build_manifest_data() -> dict[str, object]:
    edges, round8_closure = discover_round8_graph()
    support_closure = tuple(sorted({SUPPORT_ENTRYPOINT, *round8_closure}))
    closure_projection = {
        "dependency_edges": edges,
        "round8_rebuild_project_source_closure": _binding_list(round8_closure),
        "stage4_support_project_source_closure": _binding_list(support_closure),
    }
    return {
        "schema": SCHEMA_MANIFEST,
        "date": DATE,
        "paper_number": 26,
        "roadmap_items": ["REV-04", "REV-08"],
        "round8_rebuild_entrypoint": ROUND8_ENTRYPOINT,
        "stage4_support_entrypoint": SUPPORT_ENTRYPOINT,
        "closure_detection_rule": (
            "recursive AST detection of executable local _load_module calls and "
            "Path.with_name calls inside _load_* functions; exact closure equality"
        ),
        **closure_projection,
        "closure_sha256": sha256_bytes(canonical_json_bytes(closure_projection)),
        "locked_inputs": _binding_list(LOCKED_INPUT_PATHS),
        "canonical_round8_results": _binding_list(CANONICAL_RESULT_PATHS),
        "legacy_round8_receipts": _binding_list(LEGACY_RECEIPT_PATHS),
        "legacy_round8_support": _binding_list(LEGACY_SUPPORT_PATHS),
        "stage4_verification_sources": _binding_list(STAGE4_VERIFICATION_PATHS),
        "write_boundary": {
            "canonical_round8_result_bytes_may_change": False,
            "stage3_revision_base_may_change": False,
            "paper_manuscript_may_change": False,
            "new_stage4_support_artifacts_only": True,
        },
        "route_boundary": {
            "formal_route_a_tuple": FORMAL_TUPLE,
            "a2_dynamical_zeta_evaluation_run": False,
            "route_b_invocation_allowed": False,
            "target_data_used": False,
            "cross_instance_owner_deduplication_run": False,
        },
    }


def _require_exact_keys(value: dict[str, object], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        raise SupportError(
            f"{label} keys differ: missing={sorted(expected-actual)}, "
            f"extra={sorted(actual-expected)}"
        )


def _verify_bindings(rows: object, label: str) -> None:
    if not isinstance(rows, list):
        raise SupportError(f"{label} must be a list")
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise SupportError(f"{label}[{index}] must be an object")
        _require_exact_keys(row, {"path", "bytes", "sha256"}, f"{label}[{index}]")
        path_text = row["path"]
        if not isinstance(path_text, str) or path_text in seen:
            raise SupportError(f"{label}[{index}] has invalid or duplicate path")
        seen.add(path_text)
        actual = binding(path_text)
        if row != actual:
            raise SupportError(
                f"{label}[{index}] binding drift for {path_text}: "
                f"expected={row}, actual={actual}"
            )


def verify_manifest_data(manifest: dict[str, object]) -> dict[str, object]:
    expected_keys = {
        "schema",
        "date",
        "paper_number",
        "roadmap_items",
        "round8_rebuild_entrypoint",
        "stage4_support_entrypoint",
        "closure_detection_rule",
        "dependency_edges",
        "round8_rebuild_project_source_closure",
        "stage4_support_project_source_closure",
        "closure_sha256",
        "locked_inputs",
        "canonical_round8_results",
        "legacy_round8_receipts",
        "legacy_round8_support",
        "stage4_verification_sources",
        "write_boundary",
        "route_boundary",
    }
    _require_exact_keys(manifest, expected_keys, "dependency manifest")
    if manifest["schema"] != SCHEMA_MANIFEST:
        raise SupportError("unexpected dependency-manifest schema")
    if manifest["paper_number"] != 26 or manifest["roadmap_items"] != ["REV-04", "REV-08"]:
        raise SupportError("dependency manifest is not bound to P26 REV-04/REV-08")
    if manifest["round8_rebuild_entrypoint"] != ROUND8_ENTRYPOINT:
        raise SupportError("round8 rebuild entrypoint drift")
    if manifest["stage4_support_entrypoint"] != SUPPORT_ENTRYPOINT:
        raise SupportError("stage4 support entrypoint drift")

    edges, round8_closure = discover_round8_graph()
    support_closure = tuple(sorted({SUPPORT_ENTRYPOINT, *round8_closure}))
    expected_round8 = _binding_list(round8_closure)
    expected_support = _binding_list(support_closure)
    if manifest["dependency_edges"] != edges:
        raise SupportError("transitive local dependency-edge set drifted")
    if manifest["round8_rebuild_project_source_closure"] != expected_round8:
        raise SupportError("Round-8 project-source closure is incomplete or stale")
    if manifest["stage4_support_project_source_closure"] != expected_support:
        raise SupportError("Stage-4 support source closure is incomplete or stale")
    projection = {
        "dependency_edges": edges,
        "round8_rebuild_project_source_closure": expected_round8,
        "stage4_support_project_source_closure": expected_support,
    }
    actual_closure_hash = sha256_bytes(canonical_json_bytes(projection))
    if manifest["closure_sha256"] != actual_closure_hash:
        raise SupportError("closure_sha256 mismatch")

    for label in (
        "locked_inputs",
        "canonical_round8_results",
        "legacy_round8_receipts",
        "legacy_round8_support",
        "stage4_verification_sources",
    ):
        _verify_bindings(manifest[label], label)

    expected_write_boundary = {
        "canonical_round8_result_bytes_may_change": False,
        "stage3_revision_base_may_change": False,
        "paper_manuscript_may_change": False,
        "new_stage4_support_artifacts_only": True,
    }
    if manifest["write_boundary"] != expected_write_boundary:
        raise SupportError("write boundary is not fail-closed")
    expected_route_boundary = {
        "formal_route_a_tuple": FORMAL_TUPLE,
        "a2_dynamical_zeta_evaluation_run": False,
        "route_b_invocation_allowed": False,
        "target_data_used": False,
        "cross_instance_owner_deduplication_run": False,
    }
    if manifest["route_boundary"] != expected_route_boundary:
        raise SupportError("Route-A boundary drift")
    return {
        "closure_sha256": actual_closure_hash,
        "round8_project_source_count": len(round8_closure),
        "stage4_project_source_count": len(support_closure),
    }


def load_manifest(path: Path) -> tuple[dict[str, object], bytes]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SupportError(f"cannot load dependency manifest {path}: {exc}")
    if not isinstance(value, dict):
        raise SupportError("dependency manifest root must be an object")
    verify_manifest_data(value)
    return value, raw


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def load_round8_module():
    path = safe_project_path(ROUND8_ENTRYPOINT)
    name = "p26_round8_for_stage4_support"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SupportError("could not load frozen Round-8 module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_coordinates(text: str) -> tuple[Fraction, ...]:
    return tuple(Fraction(part) for part in text.split("|"))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def degree_map_text(values: dict[int, Fraction]) -> str:
    return "|".join(
        f"{degree}:{fraction_text(values[degree])}" for degree in sorted(values)
    )


def primitive_functional_candidates() -> Iterable[tuple[int, int]]:
    """Increasing L1 complexity; canonical sign; no observed-output input."""

    norm = 1
    while True:
        candidates: set[tuple[int, int]] = set()
        for coefficient_y in range(0, norm + 1):
            for coefficient_z in range(-norm, norm + 1):
                if abs(coefficient_y) + abs(coefficient_z) != norm:
                    continue
                if coefficient_y == 0 and coefficient_z <= 0:
                    continue
                if math.gcd(coefficient_y, abs(coefficient_z)) != 1:
                    continue
                candidates.add((coefficient_y, coefficient_z))
        yield from sorted(candidates)
        norm += 1


def select_target_blind_controls(
    source_coordinates: dict[str, tuple[Fraction, ...]],
) -> tuple[tuple[int, int], ...]:
    selected: list[tuple[int, int]] = []
    for candidate in primitive_functional_candidates():
        if candidate == STUDIED_FUNCTIONAL:
            continue
        a, b = candidate
        if any(a * values[1] + b * values[2] == 0 for values in source_coordinates.values()):
            continue
        if any(a * d - b * c == 0 for c, d in selected):
            continue
        selected.append(candidate)
        if len(selected) == CONTROL_COUNT:
            break
    if len(selected) != CONTROL_COUNT:
        raise SupportError("could not select two denominator-safe independent controls")
    return tuple(selected)


def failure_mechanism(degree_one_zero: bool, nonunit_zero: bool) -> str:
    if degree_one_zero and nonunit_zero:
        return "PASS"
    if not degree_one_zero and not nonunit_zero:
        return "DEGREE_ONE_AND_NONUNIT"
    if not degree_one_zero:
        return "DEGREE_ONE_ONLY"
    return "NONUNIT_ONLY"


def control_evaluation(
    coefficient: tuple[int, int],
    source: tuple[Fraction, ...],
    instances: Sequence[tuple[int, tuple[Fraction, ...]]],
    scalar: int,
) -> dict[str, object]:
    a, b = coefficient
    source_value = a * source[1] + b * source[2]
    if source_value == 0:
        raise SupportError("selected matched control has a zero source denominator")
    degrees = sorted({1, *(degree for degree, _ in instances)})
    moments = {
        degree: sum(
            (
                ((a * coordinates[1] + b * coordinates[2]) / source_value) ** 2
                for owner_degree, coordinates in instances
                if owner_degree == degree
            ),
            Fraction(0),
        )
        for degree in degrees
    }
    required = {
        degree: Fraction(scalar if degree == 1 else 0) for degree in degrees
    }
    residuals = {degree: moments[degree] - required[degree] for degree in degrees}
    degree_one_zero = residuals[1] == 0
    nonunit_zero = all(moments[degree] == 0 for degree in degrees if degree > 1)
    return {
        "source_value": source_value,
        "moments": moments,
        "required": required,
        "residuals": residuals,
        "degree_one_zero": degree_one_zero,
        "nonunit_zero": nonunit_zero,
        "pass": degree_one_zero and nonunit_zero,
        "failure_mechanism": failure_mechanism(degree_one_zero, nonunit_zero),
    }


LEDGER_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "scalar_law",
    "scalar_lambda_p_exact",
    "cycle_degree_profile",
    "degree_one_owner_present",
    "degree_support_forces_degree_one_failure",
    "scalar_sign_forces_degree_one_failure",
    "studied_functional",
    "studied_k_exact_pass",
    "studied_k_failure_mechanism",
    "control_1_functional",
    "control_1_source_coordinate",
    "control_1_moments_by_degree_exact",
    "control_1_signed_residuals_by_degree_exact",
    "control_1_exact_pass",
    "control_1_failure_mechanism",
    "control_2_functional",
    "control_2_source_coordinate",
    "control_2_moments_by_degree_exact",
    "control_2_signed_residuals_by_degree_exact",
    "control_2_exact_pass",
    "control_2_failure_mechanism",
    "matched_control_overlap_class",
    "newform_specific_residue_supported_in_two_control_panel",
    "target_data_used",
    "formal_a2_evaluation_run",
    "route_b_invocation_allowed",
    "formal_route_a_tuple",
)


def functional_text(coefficient: tuple[int, int]) -> str:
    a, b = coefficient
    if b < 0:
        return f"{a}*y-{abs(b)}*z"
    return f"{a}*y+{b}*z"


def build_decomposition() -> tuple[list[dict[str, object]], dict[str, object]]:
    round8 = load_round8_module()
    cycle_rows = round8.read_csv(PROJECT_DIR / LOCKED_INPUT_PATHS[0])
    moment_rows = round8.read_csv(PROJECT_DIR / LOCKED_INPUT_PATHS[1])
    instance_rows, group_rows, homology_model = round8.build_taxonomy(
        cycle_rows, moment_rows
    )
    validation_errors = round8.validate_outputs(
        instance_rows, group_rows, homology_model
    )
    if validation_errors:
        raise SupportError(
            "frozen Round-8 rebuild failed: " + "; ".join(validation_errors)
        )
    if len(instance_rows) != 138:
        raise SupportError("frozen instance population changed")

    arcs, relations = round8.ROUND7.relation_matrix()
    dual_basis = round8.ROUND7.nullspace_basis(relations)
    words = sorted({str(row["word"]) for row in instance_rows})
    source_coordinates = {
        word: round8.ROUND7.homology_coordinates(
            round8.ROUND2.matrix_from_word(word), arcs, dual_basis
        )
        for word in words
    }
    controls = select_target_blind_controls(source_coordinates)

    grouped_instances: dict[
        tuple[str, int], list[tuple[int, tuple[Fraction, ...]]]
    ] = defaultdict(list)
    a_p_by_group: dict[tuple[str, int], int] = {}
    for row in instance_rows:
        key = (str(row["word"]), int(row["hecke_prime"]))
        grouped_instances[key].append(
            (
                int(row["cycle_degree"]),
                parse_coordinates(str(row["homology_coordinates_y0_11"])),
            )
        )
        a_p_by_group[key] = int(row["a_p"])
    if len(grouped_instances) != 55:
        raise SupportError("frozen group population changed")

    studied_rows = {
        (str(row["word"]), int(row["hecke_prime"]), str(row["scalar_law"])): row
        for row in group_rows
    }
    if len(studied_rows) != 165:
        raise SupportError("frozen group/law population changed")

    output: list[dict[str, object]] = []
    for (word, prime), instances in sorted(grouped_instances.items()):
        eigenvalue = a_p_by_group[(word, prime)]
        degree_profile = "|".join(str(degree) for degree, _ in instances)
        degree_one_present = any(degree == 1 for degree, _ in instances)
        for law in SCALAR_LAWS:
            scalar = round8.scalar_value(law, eigenvalue, prime)
            studied = studied_rows[(word, prime, law)]
            studied_pass = str(studied["all_degree_moment_residuals_zero_exact"]) == "true"
            studied_degree_one_zero = str(studied["degree_one_residual_zero_exact"]) == "true"
            studied_nonunit_zero = str(studied["all_nonunit_degree_moments_zero_exact"]) == "true"
            studied_mechanism = failure_mechanism(
                studied_degree_one_zero, studied_nonunit_zero
            )
            evaluations = [
                control_evaluation(
                    coefficient,
                    source_coordinates[word],
                    instances,
                    scalar,
                )
                for coefficient in controls
            ]
            control_passes = [bool(value["pass"]) for value in evaluations]
            if studied_pass:
                overlap = "STUDIED_K_PASS"
            elif control_passes == [False, False]:
                overlap = "STUDIED_K_FAIL_SHARED_BOTH_MATCHED_CONTROLS"
            elif control_passes == [True, True]:
                overlap = "STUDIED_K_FAIL_MATCHED_CONTROLS_PASS_POSSIBLE_RESIDUE"
            else:
                overlap = "STUDIED_K_FAIL_SHARED_ONE_MATCHED_CONTROL"
            residue = not studied_pass and all(control_passes)
            row: dict[str, object] = {
                "word": word,
                "hecke_prime": prime,
                "a_p": eigenvalue,
                "scalar_law": law,
                "scalar_lambda_p_exact": scalar,
                "cycle_degree_profile": degree_profile,
                "degree_one_owner_present": str(degree_one_present).lower(),
                "degree_support_forces_degree_one_failure": str(
                    (not degree_one_present) and scalar != 0
                ).lower(),
                "scalar_sign_forces_degree_one_failure": str(scalar < 0).lower(),
                "studied_functional": functional_text(STUDIED_FUNCTIONAL),
                "studied_k_exact_pass": str(studied_pass).lower(),
                "studied_k_failure_mechanism": studied_mechanism,
                "matched_control_overlap_class": overlap,
                "newform_specific_residue_supported_in_two_control_panel": str(
                    residue
                ).lower(),
                "target_data_used": "false",
                "formal_a2_evaluation_run": "false",
                "route_b_invocation_allowed": "false",
                "formal_route_a_tuple": FORMAL_TUPLE,
            }
            for index, (coefficient, evaluation) in enumerate(
                zip(controls, evaluations), start=1
            ):
                row[f"control_{index}_functional"] = functional_text(coefficient)
                row[f"control_{index}_source_coordinate"] = fraction_text(
                    Fraction(evaluation["source_value"])
                )
                row[f"control_{index}_moments_by_degree_exact"] = degree_map_text(
                    evaluation["moments"]  # type: ignore[arg-type]
                )
                row[f"control_{index}_signed_residuals_by_degree_exact"] = degree_map_text(
                    evaluation["residuals"]  # type: ignore[arg-type]
                )
                row[f"control_{index}_exact_pass"] = str(
                    bool(evaluation["pass"])
                ).lower()
                row[f"control_{index}_failure_mechanism"] = evaluation[
                    "failure_mechanism"
                ]
            output.append(row)

    summary: dict[str, object] = {
        "schema": SCHEMA_SUMMARY,
        "date": DATE,
        "status": "PASS",
        "selection": {
            "studied_functional": functional_text(STUDIED_FUNCTIONAL),
            "matched_controls": [functional_text(value) for value in controls],
            "algorithm": (
                "enumerate primitive integer (y,z) coefficient pairs by increasing "
                "L1 norm and lexicographic order; canonicalize sign; exclude the "
                "studied 2*y+z direction; retain the first two independent pairs "
                "nonzero on all eleven frozen source classes"
            ),
            "selection_inputs": (
                "frozen source words and exact Schreier source coordinates only; "
                "no output classification, scalar-law verdict, target data, A2, "
                "determinant, or Route-B input"
            ),
            "source_denominators": {
                functional_text(coefficient): {
                    word: fraction_text(
                        coefficient[0] * coordinates[1]
                        + coefficient[1] * coordinates[2]
                    )
                    for word, coordinates in sorted(source_coordinates.items())
                }
                for coefficient in controls
            },
        },
        "population": {
            "instance_total": len(instance_rows),
            "word_prime_groups": len(grouped_instances),
            "group_law_rows": len(output),
        },
        "per_law": {},
        "finding": {
            "newform_specific_residue_supported_in_two_control_panel": False,
            "interpretation": (
                "Within this predeclared two-control exact audit, no studied-k "
                "failure is accompanied by passes for both matched controls. "
                "This is a bounded generic-obstruction result, not a universal "
                "statement over every closed one-form or a newform uniqueness proof."
            ),
        },
        "claim_boundary": {
            "formal_route_a_tuple": FORMAL_TUPLE,
            "instance_multiset_changed": False,
            "group_multiset_changed": False,
            "canonical_round8_result_bytes_changed": False,
            "target_data_used": False,
            "formal_a2_evaluation_run": False,
            "dynamical_determinant_constructed": False,
            "cross_instance_owner_deduplication_run": False,
            "route_b_invocation_allowed": False,
        },
    }

    per_law: dict[str, object] = {}
    for law in SCALAR_LAWS:
        rows = [row for row in output if row["scalar_law"] == law]
        studied_failures = [row for row in rows if row["studied_k_exact_pass"] == "false"]
        mechanisms = {
            "studied_k": dict(
                sorted(Counter(str(row["studied_k_failure_mechanism"]) for row in rows).items())
            )
        }
        for index in (1, 2):
            mechanisms[f"control_{index}"] = dict(
                sorted(
                    Counter(
                        str(row[f"control_{index}_failure_mechanism"]) for row in rows
                    ).items()
                )
            )
        overlap_counts = Counter(
            str(row["matched_control_overlap_class"]) for row in studied_failures
        )
        per_law[law] = {
            "studied_k_failures": len(studied_failures),
            "failure_mechanism_counts": mechanisms,
            "studied_failure_overlap": {
                "both_matched_controls_fail": overlap_counts[
                    "STUDIED_K_FAIL_SHARED_BOTH_MATCHED_CONTROLS"
                ],
                "exactly_one_matched_control_fails": overlap_counts[
                    "STUDIED_K_FAIL_SHARED_ONE_MATCHED_CONTROL"
                ],
                "both_matched_controls_pass_possible_residue": overlap_counts[
                    "STUDIED_K_FAIL_MATCHED_CONTROLS_PASS_POSSIBLE_RESIDUE"
                ],
                "degree_one_absent_with_nonzero_scalar": sum(
                    row["degree_support_forces_degree_one_failure"] == "true"
                    for row in studied_failures
                ),
                "negative_scalar": sum(
                    row["scalar_sign_forces_degree_one_failure"] == "true"
                    for row in studied_failures
                ),
            },
        }
    summary["per_law"] = per_law
    if any(
        row["newform_specific_residue_supported_in_two_control_panel"] == "true"
        for row in output
    ):
        summary["finding"][  # type: ignore[index]
            "newform_specific_residue_supported_in_two_control_panel"
        ] = True
    return output, summary


def write_results(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows, summary = build_decomposition()
    ledger_path = output_dir / RESULT_LEDGER_NAME
    with ledger_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=LEDGER_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    write_json(output_dir / RESULT_SUMMARY_NAME, summary)


def result_tree_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for name in (RESULT_LEDGER_NAME, RESULT_SUMMARY_NAME):
        path = directory / name
        if not path.is_file() or path.is_symlink():
            raise SupportError(f"missing support result: {path}")
        digest.update(f"{sha256_file(path)}  {name}\n".encode("utf-8"))
    return digest.hexdigest()


def build_receipt(
    manifest_path: Path,
    run1_dir: Path,
    run2_dir: Path,
    legacy_tests_passed: int,
    support_tests_passed: int,
) -> dict[str, object]:
    manifest, manifest_raw = load_manifest(manifest_path)
    run1_hash = result_tree_hash(run1_dir)
    run2_hash = result_tree_hash(run2_dir)
    if run1_hash != run2_hash:
        raise SupportError("two isolated Stage-4 result trees differ")
    for name in (RESULT_LEDGER_NAME, RESULT_SUMMARY_NAME):
        if (run1_dir / name).read_bytes() != (run2_dir / name).read_bytes():
            raise SupportError(f"isolated Stage-4 output differs: {name}")
    summary = json.loads((run1_dir / RESULT_SUMMARY_NAME).read_text(encoding="utf-8"))
    if summary.get("status") != "PASS":
        raise SupportError("Stage-4 matched-control summary is not PASS")
    if summary.get("claim_boundary", {}).get("formal_route_a_tuple") != FORMAL_TUPLE:
        raise SupportError("Stage-4 result changed the formal Route-A tuple")
    if summary.get("population") != {
        "instance_total": 138,
        "word_prime_groups": 55,
        "group_law_rows": 165,
    }:
        raise SupportError("Stage-4 result changed the frozen population")
    result_bindings = [
        {
            "path": name,
            "bytes": (run1_dir / name).stat().st_size,
            "sha256": sha256_file(run1_dir / name),
        }
        for name in (RESULT_LEDGER_NAME, RESULT_SUMMARY_NAME)
    ]
    return {
        "schema": SCHEMA_RECEIPT,
        "date": DATE,
        "paper_number": 26,
        "roadmap_items": ["REV-04", "REV-08"],
        "verdict": "REPRODUCIBLE",
        "dependency_manifest": {
            "path": MANIFEST_RELATIVE_PATH,
            "sha256": sha256_bytes(manifest_raw),
            "closure_sha256": manifest["closure_sha256"],
            "round8_project_source_count": len(
                manifest["round8_rebuild_project_source_closure"]  # type: ignore[arg-type]
            ),
        },
        "tests": {
            "legacy_round8_passed": legacy_tests_passed,
            "stage4_support_passed": support_tests_passed,
            "failed": 0,
        },
        "execution": {
            "isolated_runs": 2,
            "byte_identical": True,
            "run1_tree_sha256": run1_hash,
            "run2_tree_sha256": run2_hash,
            "command": "bash experiments/reproduce_stage4_round8_support.sh",
        },
        "support_results": result_bindings,
        "canonical_round8_results": manifest["canonical_round8_results"],
        "legacy_round8_receipts": manifest["legacy_round8_receipts"],
        "registered_results": {
            "instance_total": 138,
            "word_prime_groups": 55,
            "group_law_rows": 165,
            "studied_k_failures": {
                law: summary["per_law"][law]["studied_k_failures"]
                for law in SCALAR_LAWS
            },
            "studied_failure_overlap": {
                law: summary["per_law"][law]["studied_failure_overlap"]
                for law in SCALAR_LAWS
            },
            "newform_specific_residue_supported_in_two_control_panel": summary[
                "finding"
            ]["newform_specific_residue_supported_in_two_control_panel"],
        },
        "scope": summary["claim_boundary"],
        "canonical_result_bytes_unchanged": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_manifest = subparsers.add_parser("build-manifest")
    build_manifest.add_argument("--output", type=Path, required=True)

    verify_manifest = subparsers.add_parser("verify-manifest")
    verify_manifest.add_argument("--manifest", type=Path, required=True)

    build_results = subparsers.add_parser("build-results")
    build_results.add_argument("--manifest", type=Path, required=True)
    build_results.add_argument("--output-dir", type=Path, required=True)

    build_receipt_parser = subparsers.add_parser("build-receipt")
    build_receipt_parser.add_argument("--manifest", type=Path, required=True)
    build_receipt_parser.add_argument("--run1-dir", type=Path, required=True)
    build_receipt_parser.add_argument("--run2-dir", type=Path, required=True)
    build_receipt_parser.add_argument("--legacy-tests-passed", type=int, required=True)
    build_receipt_parser.add_argument("--support-tests-passed", type=int, required=True)
    build_receipt_parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "build-manifest":
            write_json(args.output, build_manifest_data())
            print(f"wrote dependency manifest: {args.output}")
        elif args.command == "verify-manifest":
            _, raw = load_manifest(args.manifest)
            print(f"dependency manifest PASS: {sha256_bytes(raw)}")
        elif args.command == "build-results":
            load_manifest(args.manifest)
            write_results(args.output_dir)
            # Re-read the manifest after computation so any concurrent drift is
            # detected before a result can be accepted.
            load_manifest(args.manifest)
            print(f"Stage-4 support results PASS: {result_tree_hash(args.output_dir)}")
        elif args.command == "build-receipt":
            receipt = build_receipt(
                args.manifest,
                args.run1_dir,
                args.run2_dir,
                args.legacy_tests_passed,
                args.support_tests_passed,
            )
            write_json(args.output, receipt)
            print(f"wrote Stage-4 support receipt: {args.output}")
        else:  # pragma: no cover
            raise SupportError(f"unknown command: {args.command}")
    except SupportError as exc:
        print(f"Stage-4 support FAIL: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
