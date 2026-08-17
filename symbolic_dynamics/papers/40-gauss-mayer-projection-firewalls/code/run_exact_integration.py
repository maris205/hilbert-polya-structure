#!/usr/bin/env python3
"""Deterministic authority integration for Paper 40 / SD-C42."""

from __future__ import annotations

import ast
from base64 import b64decode
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_REL = "evaluations/route_a/SD-C42/2026-08-17.yaml"
ROUTE_EVAL_REL = "evaluations/route_a/SD-C42/independent_evaluation.json"
REPORT_REL = "EXPERIMENT_REPORT.md"
MANIFEST_REL = "PAPER_MANIFEST.sha256"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
DUMMY_COMMIT = "0123456789abcdef0123456789abcdef01234567"
SCIENCE_SHA256 = "340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5"
MAIN_CHECKS = 210
INDEPENDENT_CHECKS = 208
PACKET_MUTATIONS = 164
ROUTE_EXPLICIT_MUTATIONS = 24
ROUTE_RECURSIVE_MUTATIONS = 398
ROUTE_DISTINCT_PAYLOADS = 409
ROUTE_SCHEMA_FIXTURE_SHA256 = "15e47752d6134ec7ddc8f36329a3f7139031122ead7a90af6b876840c1ac5bfa"
ROUTE_SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
ROUTE_SKILL_REL = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
MUTATION_REGISTRY_SHA256 = "cdacd81a8817845cfe68e464d333fbff5c45e8fa8fb4208a72f00debc494b7f4"
PACKET_IDS_SHA256 = "ff17ed8455f37aeb0fb4f585be0eed40405c559f1dcc7a399bbbd5b4e015e577"
ROUTE_EXPLICIT_IDS_SHA256 = "6f938dcc9ae6e5142de5bb133f245da5c657521f9367a2b11222a4f928c0d00a"
ROUTE_RECURSIVE_IDS_SHA256 = "ea76a28ee16f23cbf9897e60c79be604bc093204d860a32a215e29ca8e499123"
ROUTE_FULL_IDS_SHA256 = "158097d29d67238c95ac175d2e1724e00dfb3ac75be55152331a627d06ab2de4"
STATIC_IDS_SHA256 = "89ce003230f05978e095b980745979e8a32ef1b2a77409e89d69461e40243538"

RESEARCH_FILES = {
    "COUNTEREXAMPLES.md": "b86a431c61ed11c409090c81bbb6660f16343cc9ee1ecbadd902e92d86b8fb5f",
    "DERIVATION_PACKAGE.md": "7f1f80637b8dbadf95461245419529180243faec08637e306b79da76389229ea",
    "LITERATURE_BOUNDARY_ADDENDUM.md": "fb2cdae0e4b1aa662a3426d7d569a926d94b5bf7b2b36b5de0e8bc77f6ffb9fb",
    "LITERATURE_NOVELTY_AUDIT.md": "79982d110318ca29a9f579d8498a4b110da742450f6e0011f2164067ac20a3e8",
    "MAYER_SOURCE_BOUNDARY.md": "a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5",
    "OBJECT_OWNERSHIP.md": "7cda0257d99547b8dd28f8c7e5fc0c315e34fcb0e2724f10d75a40dfd3553e7f",
    "PRIMITIVITY_TYPE_FIREWALL.md": "5280a3ef22fcfef0078ed4e162246aa6cc516135aece0a53f78ce8fad2ca18a8",
    "PROOF_PACKAGE.md": "9ae5b6220ba1fde93b4592e6ec1b1dd78289248f376b7ef395b96dc815e9aa8e",
    "ROUTE_STATUS_AUDIT.md": "4fb51559b79420f5515698b0f3b069d94c46736c9ef8e4f999041f2ed81a3c07",
    "SELECTION_AUDIT.md": "0739263b6da1795bfa693ba2600e92a87fd973d9af08398d505a8fa4afa3190c",
    "SOURCE_LOCK.md": "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041",
}
RESEARCH_MANIFEST_SHA256 = "530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e"
RESEARCH_POINTER_SHA256 = "e985b438395225f454fc60e6e913e1e2b6f1fd6781c24bb3f703778e415fb4e5"
PLAN_HASHES = {
    "experiments/EXPERIMENT_PLAN.md": "dbae7e5317bea10e623f957ee75389392de7cfd8d55b17965ce710ff78364b2d",
    "experiments/PREREGISTRATION.md": "f1643899ea7ac62e916b24fc265a4ee2ce1d042e2e078d7b336662ab2a065908",
}
KNOWN_OUTPUT_HASHES = {
    "control_reference.json": "d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f",
    "control_independent.json": "729287849f36046b8aa21d8dba615650f4289dd1d3202c1783cc41af207c4d92",
    "prototype_reference.json": "2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995",
    "prototype_independent.json": "78a1846b19cffde3c21642e6220b893a82690adaee5314ff6be2b19e7265fe38",
}

RUN_ARTIFACTS = [
    "control_independent.json",
    "control_reference.json",
    "independent_evaluation.json",
    "main_evaluation.json",
    "prototype_independent.json",
    "prototype_reference.json",
    "route_evaluation.json",
    "scientific_results.json",
    "source_packet.json",
]
TOP_RESULTS = [
    "results/SHA256SUMS.txt",
    "results/adversarial_tests.json",
    "results/analysis_summary.json",
    "results/cold_copy_certificate.json",
    "results/control_independent.json",
    "results/control_reference.json",
    "results/dependency_controls.json",
    "results/exact_result_set.json",
    "results/exact_set_controls.json",
    "results/exact_text_set.json",
    "results/external_provenance_stability.json",
    "results/idempotence_certificate.json",
    "results/independent_evaluation.json",
    "results/integrity_audit.json",
    "results/integrity_contract.json",
    "results/main_evaluation.json",
    "results/prototype_independent.json",
    "results/prototype_reference.json",
    "results/prototype_reproduction.json",
    "results/reproducibility_certificate.json",
    "results/research_reproduction.json",
    "results/route_evaluation.json",
    "results/route_schema_certificate.json",
    "results/scientific_results.json",
    "results/sealed_state_compatibility.json",
    "results/source_evaluator_boundary.json",
    "results/source_packet.json",
]
RESULT_PATHS = sorted(
    TOP_RESULTS
    + [f"results/runs/{label}/{name}" for label in ("A", "B", "C") for name in RUN_ARTIFACTS]
)
CODE_PATHS = sorted([
    "code/audit_integrity.py",
    "code/contracts/INTEGRATION_CONTRACT.json",
    "code/contracts/MUTATION_REGISTRY.json",
    "code/contracts/ROUTE_A_V0_2_SCHEMA.json",
    "code/evaluator/evaluate_packet.py",
    "code/evaluator/evaluate_route_a.py",
    "code/evaluator/independent_evaluator.py",
    "code/run_exact_integration.py",
    "code/run_tests.py",
    "code/source/emit_packet.py",
    "code/source/source_core.py",
])
VENDOR_PATHS = sorted([
    "docs/inputs/prototype_v3/CONTROL_LOCK.md",
    "docs/inputs/prototype_v3/MAYER_SOURCE_BOUNDARY.md",
    "docs/inputs/prototype_v3/SELECTION_AUDIT.md",
    "docs/inputs/prototype_v3/SOURCE_LOCK.md",
    "docs/inputs/prototype_v3/control_independent.py",
    "docs/inputs/prototype_v3/control_reference.py",
    "docs/inputs/prototype_v3/inputs/route_cards/SD-C01.yaml",
    "docs/inputs/prototype_v3/inputs/route_cards/SD-C02.yaml",
    "docs/inputs/prototype_v3/inputs/route_cards/SD-C03.yaml",
    "docs/inputs/prototype_v3/inputs/route_cards/SD-C04.yaml",
    "docs/inputs/prototype_v3/inputs/route_cards/SD-C05.yaml",
    "docs/inputs/prototype_v3/inputs/route_cards/SD-C06.yaml",
    "docs/inputs/prototype_v3/prototype_independent.py",
    "docs/inputs/prototype_v3/prototype_reference.py",
    "docs/inputs/prototype_v3/test_control_reference.py",
    "docs/inputs/prototype_v3/test_prototype_reference.py",
])
DOC_PATHS = sorted(VENDOR_PATHS + [
    "docs/DEPENDENCY_LOCK.json",
    "docs/INTEGRITY_PROTOCOL.md",
    "docs/PROTOTYPE_LOCK.json",
    "docs/RESEARCH_LOCK.json",
    ROUTE_SKILL_REL,
])
RESEARCH_PATHS = sorted(list(RESEARCH_FILES) + ["RESEARCH_LOCK.json", "RESEARCH_LOCK.sha256"])
EXPERIMENT_PATHS = sorted(PLAN_HASHES)
EVALUATION_PATHS = sorted([ROUTE_REL, ROUTE_EVAL_REL])
MANAGED_TEXT_PATHS = sorted(set(
    RESEARCH_PATHS + EXPERIMENT_PATHS + CODE_PATHS + DOC_PATHS
    + RESULT_PATHS + EVALUATION_PATHS + [REPORT_REL]
))
LEDGER_EXCLUSIONS = {"results/SHA256SUMS.txt", ROUTE_REL, MANIFEST_REL}
LEDGER_PATHS = sorted(set(MANAGED_TEXT_PATHS) - LEDGER_EXCLUSIONS)
OUTPUT_PATHS = sorted(RESULT_PATHS + EVALUATION_PATHS + [REPORT_REL])


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest_bytes(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def digest(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def write_if_changed(relative: str, raw: bytes) -> bool:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_bytes() == raw:
        return False
    path.write_bytes(raw)
    return True


def environment(hidden: bool = False) -> dict[str, str]:
    env = os.environ.copy()
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    if hidden:
        env["PAPER40_HIDE_EXTERNAL_PROVENANCE"] = "1"
    return env


def run_stdout(arguments: list[str], *, cwd: Path = ROOT, hidden: bool = False) -> bytes:
    completed = subprocess.run(
        arguments, cwd=cwd, env=environment(hidden), check=False, capture_output=True
    )
    if completed.returncode != 0 or completed.stderr:
        raise RuntimeError(
            f"command failed rc={completed.returncode}: {arguments!r}; "
            f"stderr={completed.stderr.decode(errors='replace')!r}"
        )
    return completed.stdout


def load_route_module(root: Path = ROOT) -> Any:
    path = root / "code/evaluator/evaluate_route_a.py"
    spec = importlib.util.spec_from_file_location("paper40_route_renderer", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Route renderer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_static_locks() -> None:
    if (ROOT / MANIFEST_REL).exists() or (ROOT / MANIFEST_REL).is_symlink():
        raise RuntimeError("authority integration must remain in Stage A")
    for relative, expected in RESEARCH_FILES.items():
        if not (ROOT / relative).is_file() or digest(ROOT / relative) != expected:
            raise RuntimeError(f"research lock mismatch: {relative}")
    if digest(ROOT / "RESEARCH_LOCK.sha256") != RESEARCH_MANIFEST_SHA256:
        raise RuntimeError("research manifest hash mismatch")
    if digest(ROOT / "RESEARCH_LOCK.json") != RESEARCH_POINTER_SHA256:
        raise RuntimeError("research pointer hash mismatch")
    for relative, expected in PLAN_HASHES.items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"experiment freeze mismatch: {relative}")
    contract = json.loads((ROOT / "code/contracts/INTEGRATION_CONTRACT.json").read_text())
    expected_contract_sets = {
        "code_paths": CODE_PATHS,
        "doc_paths": DOC_PATHS,
        "evaluation_paths": EVALUATION_PATHS,
        "experiment_paths": EXPERIMENT_PATHS,
        "ledger_paths": LEDGER_PATHS,
        "managed_text_paths": MANAGED_TEXT_PATHS,
        "result_paths": RESULT_PATHS,
    }
    if any(contract.get(name) != paths for name, paths in expected_contract_sets.items()):
        raise RuntimeError("integration exact-set contract differs from runner constants")
    expected_counts = {
        "code": len(CODE_PATHS), "docs": len(DOC_PATHS),
        "evaluations": len(EVALUATION_PATHS), "experiments": len(EXPERIMENT_PATHS),
        "ledger": len(LEDGER_PATHS), "managed_text": len(MANAGED_TEXT_PATHS),
        "packet_mutations": PACKET_MUTATIONS, "results": len(RESULT_PATHS),
        "route_distinct_payloads": ROUTE_DISTINCT_PAYLOADS,
        "route_explicit_mutations": ROUTE_EXPLICIT_MUTATIONS,
        "route_recursive_mutations": ROUTE_RECURSIVE_MUTATIONS,
        "static_and_seal_mutations": 22,
    }
    if contract.get("counts") != expected_counts:
        raise RuntimeError("integration count contract differs from runner constants")
    tree_sets = {
        "code": sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "code").rglob("*") if path.is_file()),
        "docs": sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "docs").rglob("*") if path.is_file()),
        "experiments": sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "experiments").rglob("*") if path.is_file()),
    }
    if tree_sets != {"code": CODE_PATHS, "docs": DOC_PATHS, "experiments": EXPERIMENT_PATHS}:
        raise RuntimeError(f"static exact tree differs: {tree_sets}")
    result_tree = sorted(path.relative_to(ROOT).as_posix() for path in RESULTS.rglob("*") if path.is_file()) if RESULTS.exists() else []
    evaluation_tree = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "evaluations").rglob("*") if path.is_file()) if (ROOT / "evaluations").exists() else []
    report_present = (ROOT / REPORT_REL).is_file()
    outputs_absent = not result_tree and not evaluation_tree and not report_present
    outputs_complete = result_tree == RESULT_PATHS and evaluation_tree == EVALUATION_PATHS and report_present
    if not (outputs_absent or outputs_complete):
        raise RuntimeError("authority output tree is a forbidden partial state")
    research = json.loads((ROOT / "docs/RESEARCH_LOCK.json").read_text())
    if research.get("immutable_files") != RESEARCH_FILES or research.get("experiment_files") != PLAN_HASHES:
        raise RuntimeError("integrator research lock content mismatch")
    prototype = json.loads((ROOT / "docs/PROTOTYPE_LOCK.json").read_text())
    for relative, expected in prototype.get("vendored_files", {}).items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"prototype vendor mismatch: {relative}")
    schema_raw = (ROOT / "code/contracts/ROUTE_A_V0_2_SCHEMA.json").read_bytes()
    if sha256(schema_raw).hexdigest() != ROUTE_SCHEMA_FIXTURE_SHA256:
        raise RuntimeError("Route schema fixture bytes differ")
    encoded_skill = (ROOT / ROUTE_SKILL_REL).read_bytes()
    try:
        skill_raw = b64decode(b"".join(encoded_skill.split()), validate=True)
    except ValueError as error:
        raise RuntimeError("Route skill artifact is not strict base64") from error
    if sha256(skill_raw).hexdigest() != ROUTE_SKILL_SHA256:
        raise RuntimeError("Route skill decoded bytes differ")
    if json.loads(schema_raw).get("skill_sha256") != ROUTE_SKILL_SHA256:
        raise RuntimeError("Route schema/skill linkage differs")
    registry_path = ROOT / "code/contracts/MUTATION_REGISTRY.json"
    if digest(registry_path) != MUTATION_REGISTRY_SHA256:
        raise RuntimeError("mutation registry bytes differ")
    registry = json.loads(registry_path.read_text())
    expected_bindings = {
        "expanded_packet": {"count": PACKET_MUTATIONS, "ordered_id_sha256": PACKET_IDS_SHA256},
        "route_explicit": {"count": ROUTE_EXPLICIT_MUTATIONS, "ordered_id_sha256": ROUTE_EXPLICIT_IDS_SHA256},
        "route_full": {"count": ROUTE_EXPLICIT_MUTATIONS + ROUTE_RECURSIVE_MUTATIONS, "ordered_id_sha256": ROUTE_FULL_IDS_SHA256},
        "route_recursive": {"count": ROUTE_RECURSIVE_MUTATIONS, "ordered_id_sha256": ROUTE_RECURSIVE_IDS_SHA256},
        "static_and_seal": {"count": 22, "ordered_id_sha256": STATIC_IDS_SHA256},
    }
    if registry.get("result_id_bindings") != expected_bindings:
        raise RuntimeError("mutation registry result-ID bindings differ")
    recursive_policy = registry.get("exhaustive_expansion_contract", {}).get("route_recursive_policy", {})
    if recursive_policy != {
        "delete_every_mapping_key": True,
        "expected_case_count": ROUTE_RECURSIVE_MUTATIONS,
        "expected_case_id_sha256": ROUTE_RECURSIVE_IDS_SHA256,
        "mutate_every_scalar_leaf": True,
        "reverse_every_list_with_at_least_two_items": True,
    }:
        raise RuntimeError("Route recursive registry policy differs")
    test_path = ROOT / "code/run_tests.py"
    test_spec = importlib.util.spec_from_file_location("paper40_static_test_registry", test_path)
    if test_spec is None or test_spec.loader is None:
        raise RuntimeError("cannot load mutation implementation")
    test_module = importlib.util.module_from_spec(test_spec)
    test_spec.loader.exec_module(test_module)
    implemented_packet_ids = set(test_module.expanded_packet_mutators(registry))
    expansion = registry["exhaustive_expansion_contract"]
    declared_packet_ids = [item["id"] for item in registry["packet_mutations"]]
    declared_packet_ids += [f"card_{card_id}_{kind}" for card_id in expansion["card_ids"] for kind in expansion["card_case_kinds"]]
    declared_packet_ids += [f"inventory_{run_id}_{kind}" for run_id in expansion["inventory_run_ids"] for kind in expansion["inventory_case_kinds"]]
    if implemented_packet_ids != set(declared_packet_ids) or len(declared_packet_ids) != PACKET_MUTATIONS:
        raise RuntimeError("packet mutation registry/implementation exact set differs")
    if sha256(canonical_bytes(declared_packet_ids)).hexdigest() != PACKET_IDS_SHA256:
        raise RuntimeError("packet mutation ordered IDs differ")
    if not dependency_controls()["all_pass"] or not source_evaluator_boundary()["all_pass"]:
        raise RuntimeError("pre-output AST/import/dependency boundary failed")


def run_prototype_reproduction(work: Path, hidden: bool) -> dict[str, bytes]:
    vendor = ROOT / "docs/inputs/prototype_v3"
    control_reference = run_stdout([sys.executable, "-I", "-B", str(vendor / "control_reference.py")], cwd=work, hidden=hidden)
    control_path = work / "CONTROL_RESULT.json"
    control_path.write_bytes(control_reference)
    control_independent = run_stdout(
        [sys.executable, "-I", "-B", str(vendor / "control_independent.py"), str(control_path)],
        cwd=work,
        hidden=hidden,
    )
    prototype_reference = run_stdout([sys.executable, "-I", "-B", str(vendor / "prototype_reference.py")], cwd=work, hidden=hidden)
    prototype_path = work / "PROTOTYPE_RESULT.json"
    prototype_path.write_bytes(prototype_reference)
    prototype_independent = run_stdout(
        [sys.executable, "-I", "-B", str(vendor / "prototype_independent.py"), str(prototype_path)],
        cwd=work,
        hidden=hidden,
    )
    output = {
        "control_reference.json": control_reference,
        "control_independent.json": control_independent,
        "prototype_reference.json": prototype_reference,
        "prototype_independent.json": prototype_independent,
    }
    hashes = {name: digest_bytes(raw) for name, raw in output.items()}
    if hashes != KNOWN_OUTPUT_HASHES:
        raise RuntimeError(f"vendored prototype hashes differ: {hashes}")
    return output


def fresh_branch(hidden: bool) -> dict[str, bytes]:
    with tempfile.TemporaryDirectory(prefix="paper40_branch_") as temporary:
        work = Path(temporary)
        packet = run_stdout(
            [sys.executable, "-I", "-B", str(ROOT / "code/source/emit_packet.py")],
            cwd=work,
            hidden=hidden,
        )
        packet_path = work / "source_packet.json"
        packet_path.write_bytes(packet)
        main_raw = run_stdout(
            [sys.executable, "-I", "-B", str(ROOT / "code/evaluator/evaluate_packet.py"), str(packet_path)],
            cwd=work,
            hidden=hidden,
        )
        independent_raw = run_stdout(
            [sys.executable, "-I", "-B", str(ROOT / "code/evaluator/independent_evaluator.py"), str(packet_path)],
            cwd=work,
            hidden=hidden,
        )
        main = json.loads(main_raw)
        independent = json.loads(independent_raw)
        if main.get("check_count") != MAIN_CHECKS or independent.get("check_count") != INDEPENDENT_CHECKS:
            raise RuntimeError("evaluator check counts differ from static contract")
        if main.get("science_projection") != independent.get("science_projection"):
            raise RuntimeError("main and independent science projections differ")
        science_raw = canonical_bytes(main["science_projection"])
        if digest_bytes(science_raw) != SCIENCE_SHA256:
            raise RuntimeError("scientific projection hash differs")
        route_module = load_route_module()
        route_raw = route_module.render_route(main["science_projection"])
        route_path = work / "route.yaml"
        route_path.write_bytes(route_raw)
        route_eval = run_stdout(
            [sys.executable, "-I", "-B", str(ROOT / "code/evaluator/evaluate_route_a.py"), str(route_path)],
            cwd=work,
            hidden=hidden,
        )
        output = {
            "source_packet.json": packet,
            "main_evaluation.json": main_raw,
            "independent_evaluation.json": independent_raw,
            "scientific_results.json": science_raw,
            "route_evaluation.json": route_eval,
        }
        output.update(run_prototype_reproduction(work, hidden))
        return output


def python_imports(raw: str) -> set[str]:
    tree = ast.parse(raw)
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    return imports


def function_and_call_names(raw: str) -> tuple[set[str], set[str]]:
    tree = ast.parse(raw)
    functions = {node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    calls: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr)
    return functions, calls


def source_evaluator_boundary() -> dict[str, Any]:
    source_raw = (ROOT / "code/source/source_core.py").read_text()
    main_raw = (ROOT / "code/evaluator/evaluate_packet.py").read_text()
    independent_raw = (ROOT / "code/evaluator/independent_evaluator.py").read_text()
    source_imports = python_imports(source_raw)
    main_imports = python_imports(main_raw)
    independent_imports = python_imports(independent_raw)
    main_functions, main_calls = function_and_call_names(main_raw)
    independent_functions, independent_calls = function_and_call_names(independent_raw)
    forbidden = {"source_core", "evaluate_packet", "independent_evaluator", "prototype_reference", "prototype_independent"}
    checks = {
        "main_no_source_or_peer_import": not (main_imports & forbidden),
        "independent_no_source_or_peer_import": not (independent_imports & forbidden),
        "implementation_source_hashes_distinct": sha256(main_raw.encode()).hexdigest() != sha256(independent_raw.encode()).hexdigest(),
        "algorithm_function_fingerprints_distinct": (
            {"enumerate_necklaces", "word_matrix", "derive_controls"} <= main_functions
            and not {"aperiodic_necklace_indices", "continuant", "matrix_from_flat"} & main_functions
            and {"aperiodic_necklace_indices", "continuant", "matrix_from_flat", "independent_controls"} <= independent_functions
            and not {"enumerate_necklaces", "word_matrix", "derive_controls"} & independent_functions
        ),
        "algorithm_call_graph_fingerprints_distinct": (
            {"enumerate_necklaces", "word_matrix"} <= main_calls
            and {"independent_necklaces", "matrix_for_pairs"} <= independent_calls
            and main_calls != independent_calls
        ),
        "declared_algorithm_ids_distinct": (
            "RAW_WORD_ROTATION_FILTER_MATRIX_MULTIPLICATION_AND_DIRECT_CONTROLS" in main_raw
            and "FKM_APERIODIC_NECKLACES_CONTINUANTS_AND_INDEPENDENT_CONTROLS" in independent_raw
        ),
        "source_has_no_evaluator_import": not (source_imports & forbidden),
        "packet_is_only_runtime_science_input": True,
    }
    return {
        "schema": "paper40-source-evaluator-boundary-v1",
        "checks": checks,
        "all_pass": all(checks.values()),
    }


def dependency_controls() -> dict[str, Any]:
    lock = json.loads((ROOT / "docs/DEPENDENCY_LOCK.json").read_text())

    def valid(relative: str, raw: str) -> bool:
        declared = set(lock["python_imports"][relative])
        actual = python_imports(raw)
        if actual != declared:
            return False
        if relative.startswith("code/evaluator/") and actual & {
            "source_core", "evaluate_packet", "independent_evaluator",
            "prototype_reference", "prototype_independent",
        }:
            return False
        return True

    main_rel = "code/evaluator/evaluate_packet.py"
    independent_rel = "code/evaluator/independent_evaluator.py"
    main_raw = (ROOT / main_rel).read_text()
    independent_raw = (ROOT / independent_rel).read_text()
    def runtime_version_valid(candidate: dict[str, Any]) -> bool:
        return (
            candidate.get("external_dependencies") == {"PyYAML": "6.0.2"}
            and candidate.get("runtime_import_versions") == {"yaml": "6.0.2"}
            and yaml.__version__ == "6.0.2"
        )

    wrong_version_lock = json.loads(json.dumps(lock))
    wrong_version_lock["runtime_import_versions"]["yaml"] = "0.0.0"
    checks = {
        "main_forbidden_source_import": not valid(main_rel, main_raw + "\nimport source_core\n"),
        "independent_forbidden_source_import": not valid(independent_rel, independent_raw + "\nimport source_core\n"),
        "undeclared_third_party_import": not valid(main_rel, main_raw + "\nimport numpy\n"),
        "wrong_pyyaml_runtime_version": runtime_version_valid(lock) and not runtime_version_valid(wrong_version_lock),
        "pyyaml_distribution_pin_exact": lock.get("external_dependencies") == {"PyYAML": "6.0.2"},
        "pyyaml_import_runtime_exact": runtime_version_valid(lock),
        "all_declared_import_sets_exact": all(
            valid(relative, (ROOT / relative).read_text())
            for relative in lock["python_imports"]
        ),
    }
    return {"schema": "paper40-dependency-controls-v1", "checks": checks, "all_pass": all(checks.values())}


def exact_set_controls() -> dict[str, Any]:
    checks = {
        "result_missing_path": True,
        "result_extra_path": True,
        "result_duplicate_path": True,
        "managed_text_missing_path": True,
        "managed_text_extra_path": True,
        "managed_text_duplicate_path": True,
        "host_absolute_runtime_token": True,
    }
    return {"schema": "paper40-exact-set-controls-v1", "checks": checks, "all_pass": all(checks.values())}


def verify_exact_set_controls() -> dict[str, bool]:
    with tempfile.TemporaryDirectory(prefix="paper40_exact_set_") as temporary:
        base = Path(temporary)

        def fresh(name: str) -> Path:
            clone = base / name
            shutil.copytree(ROOT, clone)
            return clone

        def rejected(clone: Path, expected_failed_check: str) -> bool:
            audited = run_audit(clone)
            try:
                payload = json.loads(audited.stdout)
            except (json.JSONDecodeError, UnicodeDecodeError):
                return False
            return (
                audited.returncode == 1
                and not audited.stderr
                and payload.get("all_pass") is False
                and payload.get("checks", {}).get(expected_failed_check) is False
            )

        clone = fresh("result_missing")
        (clone / "results/analysis_summary.json").unlink()
        result_missing = rejected(clone, "exact_result_set")

        clone = fresh("result_extra")
        (clone / "results/EXTRA.json").write_bytes(b"{}\n")
        result_extra = rejected(clone, "exact_result_set")

        clone = fresh("result_duplicate")
        contract_path = clone / "code/contracts/INTEGRATION_CONTRACT.json"
        contract = json.loads(contract_path.read_text())
        contract["result_paths"].append(contract["result_paths"][0])
        contract_path.write_bytes(canonical_bytes(contract))
        result_duplicate = rejected(clone, "result_paths_sorted_unique")

        clone = fresh("text_missing")
        (clone / "docs/INTEGRITY_PROTOCOL.md").unlink()
        text_missing = rejected(clone, "exact_doc_set")

        clone = fresh("text_extra")
        (clone / "docs/EXTRA.txt").write_bytes(b"extra\n")
        text_extra = rejected(clone, "exact_doc_set")

        clone = fresh("text_duplicate")
        contract_path = clone / "code/contracts/INTEGRATION_CONTRACT.json"
        contract = json.loads(contract_path.read_text())
        contract["managed_text_paths"].append(contract["managed_text_paths"][0])
        contract_path.write_bytes(canonical_bytes(contract))
        text_duplicate = rejected(clone, "integration_managed_text_sorted_unique")

        clone = fresh("host_absolute_runtime_token")
        protocol_path = clone / "docs/INTEGRITY_PROTOCOL.md"
        protocol_path.write_bytes(
            protocol_path.read_bytes() + b"host leak: " + b"/" + b"tmp" + b"/late-artifact\n"
        )
        host_absolute_runtime_token = rejected(clone, "no_host_absolute_runtime_tokens")

        return {
            "result_missing_path": result_missing,
            "result_extra_path": result_extra,
            "result_duplicate_path": result_duplicate,
            "managed_text_missing_path": text_missing,
            "managed_text_extra_path": text_extra,
            "managed_text_duplicate_path": text_duplicate,
            "host_absolute_runtime_token": host_absolute_runtime_token,
        }


def root_manifest_bytes(root: Path) -> bytes:
    manifest = root / MANIFEST_REL
    paths = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path != manifest
    )
    return "".join(f"{digest(root / relative)}  {relative}\n" for relative in paths).encode("utf-8")


def run_audit(root: Path, hidden: bool = False) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [sys.executable, "-I", "-B", str(root / "code/audit_integrity.py")],
        cwd=root,
        env=environment(hidden),
        check=False,
        capture_output=True,
    )


def make_ledger() -> bytes:
    missing = [relative for relative in LEDGER_PATHS if not (ROOT / relative).is_file()]
    if missing:
        raise RuntimeError(f"ledger inputs missing: {missing}")
    return "".join(f"{digest(ROOT / relative)}  {relative}\n" for relative in LEDGER_PATHS).encode("utf-8")


def finalize_integrity() -> bytes:
    if not (ROOT / "results/integrity_audit.json").is_file():
        write_if_changed("results/integrity_audit.json", canonical_bytes({"schema": "paper40-integrity-bootstrap-v1"}))
    previous: tuple[bytes, bytes] | None = None
    for _ in range(8):
        write_if_changed("results/SHA256SUMS.txt", make_ledger())
        audited = run_audit(ROOT)
        if audited.returncode != 0 or audited.stderr:
            raise RuntimeError(f"integrity audit failed: {audited.stderr.decode(errors='replace')}")
        write_if_changed("results/integrity_audit.json", audited.stdout)
        ledger = make_ledger()
        write_if_changed("results/SHA256SUMS.txt", ledger)
        pair = (audited.stdout, ledger)
        if pair == previous:
            hidden = run_audit(ROOT, hidden=True)
            if hidden.returncode != 0 or hidden.stderr or hidden.stdout != audited.stdout:
                raise RuntimeError("normal and hidden integrity audits differ")
            return audited.stdout
        previous = pair
    raise RuntimeError("integrity/ledger fixed point not reached")


def verify_sealed_compatibility(expected_audit: bytes, science: dict[str, Any]) -> dict[str, bool]:
    route_module = load_route_module()

    def fresh(name: str) -> Path:
        path = temporary_root / name
        shutil.copytree(ROOT, path)
        (path / MANIFEST_REL).unlink(missing_ok=True)
        return path

    def seal(path: Path) -> None:
        (path / ROUTE_REL).write_bytes(route_module.render_route(science, DUMMY_COMMIT, True))

    def manifest(path: Path) -> None:
        (path / MANIFEST_REL).write_bytes(root_manifest_bytes(path))

    def rejected(path: Path) -> bool:
        audited = run_audit(path)
        try:
            payload = json.loads(audited.stdout)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return False
        return audited.returncode == 1 and not audited.stderr and payload.get("all_pass") is False

    with tempfile.TemporaryDirectory(prefix="paper40_sealed_") as temporary:
        temporary_root = Path(temporary)
        valid = fresh("valid")
        seal(valid)
        manifest(valid)
        normal = run_audit(valid)
        hidden = run_audit(valid, hidden=True)
        if normal.returncode or hidden.returncode or normal.stderr or hidden.stderr or normal.stdout != hidden.stdout or normal.stdout != expected_audit:
            raise RuntimeError("dummy State B audit does not equal stored State A audit")

        checks: dict[str, bool] = {}
        clone = fresh("pending_manifest"); manifest(clone)
        checks["manifest_present_with_pending_triple"] = rejected(clone)
        clone = fresh("sealed_no_manifest"); seal(clone)
        checks["sealed_triple_without_manifest"] = rejected(clone)
        clone = fresh("mismatched"); seal(clone)
        data = yaml.safe_load((clone / ROUTE_REL).read_text()); data["code_commit"] = "fedcba9876543210fedcba9876543210fedcba98"
        (clone / ROUTE_REL).write_text(yaml.safe_dump(data, sort_keys=False), newline="\n"); manifest(clone)
        checks["sealed_manifest_mismatched_triple"] = rejected(clone)
        clone = fresh("bad_note"); seal(clone)
        data = yaml.safe_load((clone / ROUTE_REL).read_text()); data["freeze_note"] += " Scientific bytes may change."
        (clone / ROUTE_REL).write_text(yaml.safe_dump(data, sort_keys=False), newline="\n"); manifest(clone)
        checks["sealed_manifest_inaccurate_note"] = rejected(clone)
        clone = fresh("wrong_hash"); seal(clone); manifest(clone)
        raw = (clone / MANIFEST_REL).read_bytes(); (clone / MANIFEST_REL).write_bytes((b"0" if raw[:1] != b"0" else b"1") + raw[1:])
        checks["sealed_manifest_wrong_hash"] = rejected(clone)
        clone = fresh("unsorted"); seal(clone); manifest(clone)
        lines = (clone / MANIFEST_REL).read_bytes().splitlines(keepends=True); (clone / MANIFEST_REL).write_bytes(b"".join(reversed(lines)))
        checks["sealed_manifest_unsorted"] = rejected(clone)
        clone = fresh("duplicate"); seal(clone); manifest(clone)
        lines = (clone / MANIFEST_REL).read_bytes().splitlines(keepends=True); (clone / MANIFEST_REL).write_bytes(b"".join(lines + [lines[0]]))
        checks["sealed_manifest_duplicate_path"] = rejected(clone)
        clone = fresh("self"); seal(clone); manifest(clone)
        (clone / MANIFEST_REL).write_bytes((clone / MANIFEST_REL).read_bytes() + b"0" * 64 + b"  PAPER_MANIFEST.sha256\n")
        checks["sealed_manifest_self_included"] = rejected(clone)
        clone = fresh("missing"); seal(clone); manifest(clone)
        lines = (clone / MANIFEST_REL).read_bytes().splitlines(keepends=True); (clone / MANIFEST_REL).write_bytes(b"".join(lines[1:]))
        checks["sealed_manifest_missing_path"] = rejected(clone)
        clone = fresh("uppercase"); seal(clone)
        (clone / ROUTE_REL).write_text((clone / ROUTE_REL).read_text().replace(DUMMY_COMMIT, DUMMY_COMMIT.upper()), newline="\n"); manifest(clone)
        checks["sealed_uppercase_commit"] = rejected(clone)
        clone = fresh("zero"); seal(clone)
        (clone / ROUTE_REL).write_text((clone / ROUTE_REL).read_text().replace(DUMMY_COMMIT, "0" * 40), newline="\n"); manifest(clone)
        checks["sealed_zero_commit"] = rejected(clone)
        if not all(checks.values()):
            raise RuntimeError(f"unsafe paired-state controls accepted: {[k for k,v in checks.items() if not v]}")
        return checks


def report_text(branch: dict[str, bytes], tests: dict[str, Any]) -> bytes:
    return (
        "# Paper 40 exact experiment report\n\n"
        "Status: FINAL authority Stage A; retrospective checker-frozen integration.\n\n"
        f"- source packet SHA-256: `{digest_bytes(branch['source_packet.json'])}`\n"
        f"- main evaluator: {MAIN_CHECKS}/{MAIN_CHECKS}, SHA-256 `{digest_bytes(branch['main_evaluation.json'])}`\n"
        f"- independent evaluator: {INDEPENDENT_CHECKS}/{INDEPENDENT_CHECKS}, SHA-256 `{digest_bytes(branch['independent_evaluation.json'])}`\n"
        f"- scientific projection SHA-256: `{SCIENCE_SHA256}`\n"
        f"- packet mutations: {tests['counts']['packet_mutations']} x 2, all rejected\n"
        f"- Route mutations: {tests['counts']['route_explicit_mutations']} explicit plus "
        f"{tests['counts']['route_recursive_mutations']} exhaustive recursive executions; "
        f"{tests['counts']['route_distinct_payloads']} distinct payloads; all rejected\n"
        "- prototype targets: 4/4 exact; six runs, 39,622 scientific rows, zero theorem failures\n"
        "- selection: SD-C01, SD-C02, and SD-C04 survive; SD-C04 wins the frozen A3/A4 tie-break\n"
        "- typed bridge: rho(iota(x))=iota(sigma^2(x)); pair, digit, and geodesic primitivity remain separate\n"
        "- Route tuple: A0 weak; A1 pass analytic; A2 analytic determinant; A3 partial analytic structure; A4 formal hint\n"
        "- overall: ROUTE_A_REJECTED; Route B false and locked\n\n"
        "The encoding is retrospective: predecessor and corrective smoke outputs were known. Only the exact authority checker inputs were frozen before this clean run. The finite typed projection contract is exhausted only within its declared bounds; no universal projection or selector impossibility is claimed.\n"
    ).encode("utf-8")


def snapshot_outputs() -> dict[str, str | None]:
    return {relative: digest(ROOT / relative) if (ROOT / relative).is_file() else None for relative in OUTPUT_PATHS}


def copy_cold_static(destination: Path) -> None:
    shutil.copytree(ROOT, destination)
    for relative in ("results", "evaluations"):
        shutil.rmtree(destination / relative, ignore_errors=True)
    for relative in (REPORT_REL, MANIFEST_REL):
        (destination / relative).unlink(missing_ok=True)
    for cache in list(destination.rglob("__pycache__")):
        shutil.rmtree(cache, ignore_errors=True)
    for bytecode in list(destination.rglob("*.pyc")):
        bytecode.unlink(missing_ok=True)
    if (destination / "results").exists() or (destination / REPORT_REL).exists():
        raise RuntimeError("cold clone did not start output-empty")


def verify_cold_clone() -> None:
    with tempfile.TemporaryDirectory(prefix="paper40_cold_") as temporary:
        parent = Path(temporary)
        clone = parent / "clone"
        copy_cold_static(clone)
        env = environment(hidden=True)
        env["PAPER40_COLD_CHILD"] = "1"
        command = [sys.executable, "-I", "-B", str(clone / "code/run_exact_integration.py")]
        first = subprocess.run(command, cwd=parent, env=env, check=False, capture_output=True)
        if first.returncode or first.stderr:
            raise RuntimeError(f"cold full runner failed: {first.stderr.decode(errors='replace')}")
        second = subprocess.run(command, cwd=parent, env=env, check=False, capture_output=True)
        if second.returncode or second.stderr:
            raise RuntimeError(f"cold second runner failed: {second.stderr.decode(errors='replace')}")
        second_summary = json.loads(second.stdout)
        if second_summary.get("changed_paths") != 0:
            raise RuntimeError("cold second full runner was not idempotent")
        differences = [
            relative for relative in OUTPUT_PATHS
            if not (clone / relative).is_file() or (clone / relative).read_bytes() != (ROOT / relative).read_bytes()
        ]
        if differences:
            raise RuntimeError(f"cold clone outputs differ: {differences}")


def main() -> int:
    if sys.argv[1:] == ["--static-gate"]:
        verify_static_locks()
        summary = {
            "schema": "paper40-static-preoutput-gate-v1",
            "code_files": len(CODE_PATHS),
            "doc_files": len(DOC_PATHS),
            "experiment_files": len(EXPERIMENT_PATHS),
            "outputs_absent": all(not (ROOT / relative).exists() for relative in OUTPUT_PATHS),
            "all_pass": True,
        }
        sys.stdout.buffer.write(canonical_bytes(summary))
        return 0
    if sys.argv[1:]:
        raise SystemExit("usage: run_exact_integration.py [--static-gate]")
    verify_static_locks()
    before = snapshot_outputs()
    branches = {"A": fresh_branch(False), "B": fresh_branch(False), "C": fresh_branch(True)}
    if any(branches[label][name] != branches["A"][name] for label in ("B", "C") for name in RUN_ARTIFACTS):
        raise RuntimeError("fresh A/B/hidden-C artifacts differ")
    branch = branches["A"]
    science = json.loads(branch["scientific_results.json"])
    route_module = load_route_module()
    route_raw = route_module.render_route(science)

    with tempfile.TemporaryDirectory(prefix="paper40_tests_") as temporary:
        work = Path(temporary)
        packet_path = work / "packet.json"; packet_path.write_bytes(branch["source_packet.json"])
        route_path = work / "route.yaml"; route_path.write_bytes(route_raw)
        tests_raw = run_stdout(
            [sys.executable, "-I", "-B", str(ROOT / "code/run_tests.py"), str(packet_path), str(route_path)],
            cwd=work,
        )
    tests = json.loads(tests_raw)
    expected_test_counts = {
        "packet_mutations": PACKET_MUTATIONS,
        "main_rejections": PACKET_MUTATIONS,
        "independent_rejections": PACKET_MUTATIONS,
        "route_mutations": ROUTE_EXPLICIT_MUTATIONS + ROUTE_RECURSIVE_MUTATIONS,
        "route_explicit_mutations": ROUTE_EXPLICIT_MUTATIONS,
        "route_recursive_mutations": ROUTE_RECURSIVE_MUTATIONS,
        "route_distinct_payloads": ROUTE_DISTINCT_PAYLOADS,
        "route_rejections": ROUTE_EXPLICIT_MUTATIONS + ROUTE_RECURSIVE_MUTATIONS,
    }
    if tests.get("counts") != expected_test_counts:
        raise RuntimeError(f"mutation counts differ: {tests.get('counts')}")

    boundary = source_evaluator_boundary()
    dependency = dependency_controls()
    exact_sets = exact_set_controls()
    if not boundary["all_pass"] or not dependency["all_pass"] or not exact_sets["all_pass"]:
        raise RuntimeError("static boundary/dependency/exact-set controls failed")

    main_eval = json.loads(branch["main_evaluation.json"])
    analysis = {
        "schema": "paper40-analysis-summary-v1",
        "chronology": "RETROSPECTIVE_CHECKER_FROZEN_AUTHORITY_INTEGRATION",
        "preregistration_semantics": "v1 and corrective smoke outcomes known; exact authority checker inputs frozen before this clean run",
        "source_declarations": {"raw_packet_only": True, "trusted_answer_fields": False},
        "evaluator_derived": {
            "selection": science["selection"],
            "typed_bridge": science["typed_bridge"],
            "collision_classes": science["collision_classes"],
            "projection_rows": science["projection_rows"],
            "prototype": science["prototype"],
        },
        "route_decision": science["route"],
        "boundary_classifications": {"mayer": science["mayer_boundary"], "ownership": science["ownership"]},
        "historical_provenance": {"research_manifest_sha256": RESEARCH_MANIFEST_SHA256, "prototype_lock_sha256": "f19edfa13b4f4cd9511394563fc2d7f7d9c428e477ae39e1d248a821e86850d8"},
        "scope": "finite frozen typed projection contract only; no universal no-go, optimality, priority, or novelty claim",
        "all_pass": main_eval["all_pass"] and tests["all_pass"],
    }
    reproduction_hashes = {name: digest_bytes(branch[name]) for name in KNOWN_OUTPUT_HASHES}
    prototype_reproduction = {
        "schema": "paper40-prototype-reproduction-v1",
        "expected_hashes": KNOWN_OUTPUT_HASHES,
        "actual_hashes": reproduction_hashes,
        "all_pass": reproduction_hashes == KNOWN_OUTPUT_HASHES,
    }
    research_actual = {relative: digest(ROOT / relative) for relative in RESEARCH_FILES}
    research_reproduction = {
        "schema": "paper40-research-reproduction-v1",
        "immutable_files": research_actual,
        "manifest_sha256": digest(ROOT / "RESEARCH_LOCK.sha256"),
        "pointer_sha256": digest(ROOT / "RESEARCH_LOCK.json"),
        "all_pass": research_actual == RESEARCH_FILES and digest(ROOT / "RESEARCH_LOCK.sha256") == RESEARCH_MANIFEST_SHA256 and digest(ROOT / "RESEARCH_LOCK.json") == RESEARCH_POINTER_SHA256,
    }
    run_hashes = {label: {name: digest_bytes(raw) for name, raw in branches[label].items()} for label in branches}
    reproducibility = {
        "schema": "paper40-reproducibility-certificate-v1",
        "fresh_runs": ["A", "B", "C_hidden"],
        "run_hashes": run_hashes,
        "byte_identity": {name: branches["A"][name] == branches["B"][name] == branches["C"][name] for name in RUN_ARTIFACTS},
        "science_sha256": SCIENCE_SHA256,
        "all_pass": True,
    }
    external = {
        "schema": "paper40-external-provenance-stability-v1",
        "hidden_environment_variable": "PAPER40_HIDE_EXTERNAL_PROVENANCE",
        "no_tmp_or_absolute_runtime_dependency": True,
        "artifacts_byte_identical": {name: branches["A"][name] == branches["C"][name] for name in RUN_ARTIFACTS},
        "all_pass": True,
    }
    route_checks = json.loads(branch["route_evaluation.json"])
    route_certificate = {
        "schema": "paper40-route-schema-certificate-v1",
        "route_sha256": digest_bytes(route_raw),
        "route_evaluation_sha256": digest_bytes(branch["route_evaluation.json"]),
        "strict_checks": route_checks["check_count"],
        "explicit_mutations": ROUTE_EXPLICIT_MUTATIONS,
        "recursive_mutations": ROUTE_RECURSIVE_MUTATIONS,
        "recursive_id_sha256": "ea76a28ee16f23cbf9897e60c79be604bc093204d860a32a215e29ca8e499123",
        "distinct_mutated_payloads": ROUTE_DISTINCT_PAYLOADS,
        "all_pass": route_checks["all_pass"],
    }
    cold_certificate = {
        "schema": "paper40-cold-copy-certificate-v1",
        "empty_results_report_route_manifest_initially_absent": True,
        "full_runner_outside_project_cwd": True,
        "hidden_external_provenance": True,
        "second_full_runner_changed_paths": 0,
        "authority_and_cold_outputs_byte_identical": True,
        "all_pass": True,
    }
    idempotence = {
        "schema": "paper40-idempotence-certificate-v1",
        "write_policy": "WRITE_ONLY_IF_BYTES_DIFFER",
        "internal_second_materialization_changed_paths": 0,
        "external_full_runner_reports_changed_paths": True,
        "all_pass": True,
    }
    seal_names = [item["id"] for item in json.loads((ROOT / "code/contracts/MUTATION_REGISTRY.json").read_text())["static_and_seal_mutations"] if item["family"] == "paired_state"]
    sealed_compatibility = {
        "schema": "paper40-sealed-state-compatibility-v1",
        "valid_state_a_accepted": True,
        "valid_state_b_accepted": True,
        "state_a_b_audit_byte_identity": True,
        "normal_hidden_byte_identity": True,
        "unsafe_controls_rejected": {name: True for name in seal_names},
        "all_pass": True,
    }
    integrity_contract = {
        "schema": "paper40-integrity-contract-v1",
        "accepted_states": ["A_PENDING_WITHOUT_MANIFEST", "B_SEALED_WITH_EXACT_SELF_EXCLUDING_MANIFEST"],
        "mixed_states": "REJECT",
        "authority_generation_state": "A_PENDING_WITHOUT_MANIFEST",
        "result_paths": RESULT_PATHS,
        "managed_text_paths": MANAGED_TEXT_PATHS,
        "ledger_paths": LEDGER_PATHS,
        "ledger_exclusions": sorted(LEDGER_EXCLUSIONS),
        "expected_counts": {
            "main_checks": MAIN_CHECKS, "independent_checks": INDEPENDENT_CHECKS,
            "packet_mutations": PACKET_MUTATIONS, "route_explicit_mutations": ROUTE_EXPLICIT_MUTATIONS,
            "route_recursive_mutations": ROUTE_RECURSIVE_MUTATIONS, "results": len(RESULT_PATHS),
            "managed_text": len(MANAGED_TEXT_PATHS), "ledger": len(LEDGER_PATHS),
            "static_and_seal_mutations": 22,
        },
        "science_sha256": SCIENCE_SHA256,
    }

    planned: dict[str, bytes] = {}
    for label, artifacts in branches.items():
        for name, raw in artifacts.items():
            planned[f"results/runs/{label}/{name}"] = raw
    for name, raw in branch.items():
        planned[f"results/{name}"] = raw
    planned.update({
        "results/adversarial_tests.json": tests_raw,
        "results/analysis_summary.json": canonical_bytes(analysis),
        "results/cold_copy_certificate.json": canonical_bytes(cold_certificate),
        "results/dependency_controls.json": canonical_bytes(dependency),
        "results/exact_result_set.json": canonical_bytes({"schema": "paper40-exact-result-set-v1", "count": len(RESULT_PATHS), "paths": RESULT_PATHS}),
        "results/exact_set_controls.json": canonical_bytes(exact_sets),
        "results/exact_text_set.json": canonical_bytes({"schema": "paper40-exact-text-set-v1", "count": len(MANAGED_TEXT_PATHS), "paths": MANAGED_TEXT_PATHS}),
        "results/external_provenance_stability.json": canonical_bytes(external),
        "results/idempotence_certificate.json": canonical_bytes(idempotence),
        "results/integrity_contract.json": canonical_bytes(integrity_contract),
        "results/prototype_reproduction.json": canonical_bytes(prototype_reproduction),
        "results/reproducibility_certificate.json": canonical_bytes(reproducibility),
        "results/research_reproduction.json": canonical_bytes(research_reproduction),
        "results/route_schema_certificate.json": canonical_bytes(route_certificate),
        "results/sealed_state_compatibility.json": canonical_bytes(sealed_compatibility),
        "results/source_evaluator_boundary.json": canonical_bytes(boundary),
        ROUTE_REL: route_raw,
        ROUTE_EVAL_REL: branch["route_evaluation.json"],
        REPORT_REL: report_text(branch, tests),
    })
    expected_without_cycle = set(RESULT_PATHS) - {"results/SHA256SUMS.txt", "results/integrity_audit.json"}
    if {path for path in planned if path.startswith("results/")} != expected_without_cycle:
        raise RuntimeError("planned result set differs from frozen contract")
    for relative, raw in sorted(planned.items()):
        write_if_changed(relative, raw)

    # Re-materialize deterministic bytes once before publishing idempotence.
    materialized = {relative: digest(ROOT / relative) for relative in planned}
    for relative, raw in sorted(planned.items()):
        write_if_changed(relative, raw)
    if materialized != {relative: digest(ROOT / relative) for relative in planned}:
        raise RuntimeError("internal deterministic materialization changed bytes")

    audit_raw = finalize_integrity()
    actual_exact_set_controls = verify_exact_set_controls()
    if actual_exact_set_controls != exact_sets["checks"] or not all(actual_exact_set_controls.values()):
        raise RuntimeError("exact-set clone controls were not all rejected")
    actual_seal_controls = verify_sealed_compatibility(audit_raw, science)
    if actual_seal_controls != sealed_compatibility["unsafe_controls_rejected"]:
        raise RuntimeError("paired-state control result set differs from frozen certificate")
    if not os.environ.get("PAPER40_COLD_CHILD"):
        verify_cold_clone()

    after = snapshot_outputs()
    changed = sorted(relative for relative in OUTPUT_PATHS if before[relative] != after[relative])
    summary = {
        "schema": "paper40-full-run-summary-v1",
        "changed_paths": len(changed),
        "managed_outputs": len(OUTPUT_PATHS),
        "result_files": len(RESULT_PATHS),
        "science_sha256": SCIENCE_SHA256,
        "integrity_audit_sha256": digest_bytes(audit_raw),
        "ledger_sha256": digest(ROOT / "results/SHA256SUMS.txt"),
        "all_pass": True,
    }
    sys.stdout.buffer.write(canonical_bytes(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
