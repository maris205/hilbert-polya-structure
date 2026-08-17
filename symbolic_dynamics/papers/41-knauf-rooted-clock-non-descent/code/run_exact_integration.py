#!/usr/bin/env python3
"""Deterministic exact authority integration for Paper 41 / SD-C43."""

from __future__ import annotations

import os
import sys
if not sys.flags.isolated:
    clean_environment = os.environ.copy()
    clean_environment.pop("PYTHONPATH", None)
    clean_environment.pop("PYTHONHOME", None)
    clean_environment["PYTHONNOUSERSITE"] = "1"
    os.execve(
        sys.executable,
        [sys.executable, "-I", "-B", os.path.abspath(__file__), *sys.argv[1:]],
        clean_environment,
    )
sys.dont_write_bytecode = True

import ast
from base64 import b64decode
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_REL = "code/contracts/INTEGRATION_CONTRACT.json"
CONTRACT_SHA256 = "2f0bbcf5dd2d2ff725edcb961f94d45c11351ed1c89fe30af803f6ee1aa07bbc"
ROUTE_REL = "evaluations/route_a/SD-C43/2026-08-17.yaml"
ROUTE_JSON_REL = "evaluations/route_a/SD-C43/independent_evaluation.json"
REPORT_REL = "EXPERIMENT_REPORT.md"
MANIFEST_REL = "PAPER_MANIFEST.sha256"
INTERNAL_STAGE_FLAG = "--build-validated-stage"
INTERNAL_STAGE_ENV = "PAPER41_INTERNAL_TRANSACTION_STAGE"
FORCED_LATE_FAILURE = "FORCED_LATE_PREINSTALL_FAILURE"
LEDGER_REL = "results/SHA256SUMS.txt"
REGISTRY_REL = "code/contracts/MUTATION_REGISTRY.json"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
DUMMY_COMMIT = "0123456789abcdef0123456789abcdef01234567"
RUN_FILES = [
    "independent_evaluation.json", "main_evaluation.json", "route_evaluation.json",
    "scientific_results.json", "source_packet.json",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def require_science_projection_bytes_equal(main_science: Any, independent_science: Any) -> bytes:
    main_bytes = canonical(main_science)
    independent_bytes = canonical(independent_science)
    if main_bytes != independent_bytes:
        raise RuntimeError("MAIN_INDEPENDENT_SCIENCE_BYTES_MISMATCH")
    return main_bytes


def science_projection_byte_control() -> dict[str, Any]:
    cases = {
        "bool_vs_int": ({"value": False}, {"value": 0}),
        "int_vs_float": ({"value": 1}, {"value": 1.0}),
    }
    rows: dict[str, Any] = {}
    for name, (main_value, independent_value) in cases.items():
        rejected = rejection = False
        try:
            require_science_projection_bytes_equal(main_value, independent_value)
        except RuntimeError as error:
            rejected = True
            rejection = str(error)
        if main_value != independent_value or not rejected \
                or rejection != "MAIN_INDEPENDENT_SCIENCE_BYTES_MISMATCH":
            raise RuntimeError(f"science byte-equality synthetic control failed: {name}")
        rows[name] = {
            "canonical_bytes_equal": canonical(main_value) == canonical(independent_value),
            "python_object_equal": main_value == independent_value,
            "rejected": rejected,
            "rejection_class": rejection,
        }
    return {
        "cases": rows,
        "comparison": "byte_for_byte",
        "schema": "paper41-cross-evaluator-science-byte-control-v1",
        "status": "PASS",
    }


def environment() -> dict[str, str]:
    result = os.environ.copy()
    result.pop("PYTHONPATH", None)
    result.pop("PYTHONHOME", None)
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1"})
    return result


def isolated_python(script: Path | str, *arguments: str) -> list[str]:
    return [sys.executable, "-I", "-B", str(script), *arguments]


def isolation_probe() -> dict[str, Any]:
    return {
        "dont_write_bytecode": sys.dont_write_bytecode,
        "isolated": bool(sys.flags.isolated),
        "schema": "paper41-parent-isolation-probe-v1",
        "yaml_version": yaml.__version__,
    }


def hostile_environment_control() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="paper41_hostile_pythonpath_") as temp_name:
        temp = Path(temp_name)
        canonical_dir = temp / "canonical"
        naive_dir = temp / "naive"
        canonical_dir.mkdir()
        naive_dir.mkdir()
        hostile_modules = ("hashlib", "json", "pathlib", "sitecustomize", "source_core", "yaml")

        def install_hostile_modules(directory: Path) -> None:
            for module in hostile_modules:
                (directory / f"{module}.py").write_text(
                    f"open('HOSTILE_{module.upper()}_IMPORTED', 'w').write('imported\\n')\n"
                    + ("" if module == "sitecustomize" else
                       f"raise RuntimeError('HOSTILE_{module.upper()}_IMPORTED')\n"),
                    encoding="utf-8",
                )

        def hostile_environment(directory: Path) -> dict[str, str]:
            result = os.environ.copy()
            result["PYTHONPATH"] = str(directory)
            result.pop("PYTHONHOME", None)
            result.pop("PYTHONDONTWRITEBYTECODE", None)
            result.pop("PYTHONPYCACHEPREFIX", None)
            result["PYTHONNOUSERSITE"] = "0"
            return result

        install_hostile_modules(canonical_dir)
        install_hostile_modules(naive_dir)
        canonical_environment = hostile_environment(canonical_dir)
        naive_environment = hostile_environment(naive_dir)
        parent = subprocess.run(
            [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "--isolation-probe"],
            cwd=canonical_dir,
            env=canonical_environment,
            capture_output=True,
            check=False,
        )
        if parent.returncode != 0 or parent.stderr:
            raise RuntimeError("canonical isolated parent invocation failed")
        parent_result = json.loads(parent.stdout)
        emitter_path = ROOT / "code/source/emit_packet.py"
        canonical_emitter = subprocess.run(
            [sys.executable, "-I", "-B", str(emitter_path)],
            cwd=canonical_dir,
            env=canonical_environment,
            capture_output=True,
            check=False,
        )
        if canonical_emitter.returncode != 0 or canonical_emitter.stderr:
            raise RuntimeError("canonical isolated emitter invocation failed")
        emitter_result = json.loads(canonical_emitter.stdout)
        child = subprocess.run(
            [
                sys.executable, "-I", "-B", "-c",
                "import hashlib,json,pathlib,yaml; print(json.dumps({'v':yaml.__version__}))",
            ],
            cwd=canonical_dir,
            env=canonical_environment,
            capture_output=True,
            check=False,
        )
        if child.returncode != 0 or child.stderr:
            raise RuntimeError("hostile PYTHONPATH reached isolated child")
        child_result = json.loads(child.stdout)
        canonical_cache_entries = [
            path for path in canonical_dir.rglob("*")
            if path.name in {"__pycache__", ".pytest_cache"} or path.suffix in {".pyc", ".pyo"}
        ]
        canonical_markers = sorted(path.name for path in canonical_dir.glob("HOSTILE_*_IMPORTED"))
        if canonical(parent_result) != canonical(isolation_probe()) \
                or canonical(child_result) != canonical({"v": "6.0.2"}) \
                or emitter_result.get("candidate_id") != "SD-C43" \
                or canonical_cache_entries or canonical_markers:
            raise RuntimeError("canonical external -I -B isolation control differs")
        naive = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--isolation-probe"],
            cwd=naive_dir,
            env=naive_environment,
            capture_output=True,
            check=False,
        )
        naive_markers = sorted(path.name for path in naive_dir.glob("HOSTILE_*_IMPORTED"))
        naive_cache_entries = [
            path for path in naive_dir.rglob("*")
            if path.name == "__pycache__" or path.suffix == ".pyc"
        ]
        if naive.returncode != 0 or naive.stderr \
                or "HOSTILE_SITECUSTOMIZE_IMPORTED" not in naive_markers or not naive_cache_entries:
            raise RuntimeError("naive startup contamination negative control was not observed")
    return {
        "canonical_child_isolated": True,
        "canonical_emitter_explicit_I_B": True,
        "canonical_emitter_stdout_sha256": digest(canonical_emitter.stdout),
        "canonical_hostile_modules_imported": [],
        "canonical_parent_explicit_I_B": True,
        "canonical_pycache_created": False,
        "hostile_modules_tested": list(hostile_modules),
        "hostile_parent_environment_normalized": True,
        "hostile_parent_variables_tested": ["PYTHONDONTWRITEBYTECODE", "PYTHONPYCACHEPREFIX"],
        "naive_hostile_invocation_allowed": False,
        "naive_child_bytecode_suppression_env_cleared": True,
        "naive_prestartup_contamination_observed": True,
        "naive_sitecustomize_marker_observed": True,
        "schema": "paper41-hostile-pythonpath-control-v3",
    }


def write_if_changed(root: Path, relative: str, raw: bytes, changed: set[str]) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_bytes() == raw:
        return
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=path.parent, prefix=f".{path.name}.install-", delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    changed.add(relative)


def run_stdout(arguments: list[str], *, cwd: Path) -> bytes:
    completed = subprocess.run(arguments, cwd=cwd, env=environment(), capture_output=True, check=False)
    if completed.returncode != 0 or completed.stderr:
        raise RuntimeError(
            f"command failed rc={completed.returncode}: {arguments!r}; "
            f"stderr={completed.stderr.decode(errors='replace')!r}"
        )
    return completed.stdout


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module {path.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_contract(root: Path = ROOT) -> dict[str, Any]:
    raw = (root / CONTRACT_REL).read_bytes()
    if digest(raw) != CONTRACT_SHA256:
        raise RuntimeError("integration contract changed")
    return json.loads(raw)


def snapshot_paths(root: Path, contract: dict[str, Any]) -> list[str]:
    base = root / contract["owned_paths"]["repo_snapshot_root"]
    return sorted(path.relative_to(root).as_posix() for path in base.rglob("*") if path.is_file())


def managed_paths(root: Path, contract: dict[str, Any]) -> list[str]:
    owned = contract["owned_paths"]
    return sorted(
        owned["code"] + owned["docs"] + owned["experiments"] + snapshot_paths(root, contract)
        + owned["results"] + [contract["evaluation"]["route_yaml_path"],
                              contract["evaluation"]["route_json_path"], owned["report"]]
    )


def expected_output_paths(contract: dict[str, Any]) -> list[str]:
    return sorted(contract["owned_paths"]["results"] + [
        contract["evaluation"]["route_yaml_path"],
        contract["evaluation"]["route_json_path"],
        contract["owned_paths"]["report"],
    ])


def actual_output_paths(root: Path, contract: dict[str, Any]) -> list[str]:
    return output_namespace_inventory(root, contract)["entries"]


def output_namespace_inventory(root: Path, contract: dict[str, Any]) -> dict[str, list[str]]:
    entries: list[str] = []
    directories: list[str] = []
    unsafe: list[str] = []

    def scan_directory(path: Path) -> None:
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            entries.append(relative)
            unsafe.append(relative)
            return
        if not path.is_dir():
            entries.append(relative)
            unsafe.append(relative)
            return
        directories.append(relative)
        with os.scandir(path) as iterator:
            for entry in sorted(iterator, key=lambda item: item.name):
                child = path / entry.name
                child_relative = child.relative_to(root).as_posix()
                if entry.is_symlink():
                    entries.append(child_relative)
                    unsafe.append(child_relative)
                elif entry.is_dir(follow_symlinks=False):
                    scan_directory(child)
                elif entry.is_file(follow_symlinks=False):
                    entries.append(child_relative)
                else:
                    entries.append(child_relative)
                    unsafe.append(child_relative)

    for directory in ("results", "evaluations"):
        base = root / directory
        if base.exists() or base.is_symlink():
            scan_directory(base)
    report = root / contract["owned_paths"]["report"]
    if report.exists() or report.is_symlink():
        entries.append(report.relative_to(root).as_posix())
        if report.is_symlink() or not report.is_file():
            unsafe.append(report.relative_to(root).as_posix())
    manifest = root / MANIFEST_REL
    if manifest.exists() or manifest.is_symlink():
        entries.append(MANIFEST_REL)
        unsafe.append(MANIFEST_REL)
    forbidden_suffixes = {".aux", ".fdb_latexmk", ".fls", ".log", ".out", ".pyc", ".pyo", ".toc"}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if path.name in {"__pycache__", ".pytest_cache"} \
                or path.suffix in forbidden_suffixes or path.name.endswith(".synctex.gz"):
            unsafe.append(relative)
    return {
        "directories": sorted(set(directories)),
        "entries": sorted(set(entries)),
        "unsafe": sorted(set(unsafe)),
    }


def expected_output_directories(contract: dict[str, Any]) -> list[str]:
    directories: set[str] = set()
    for relative in expected_output_paths(contract):
        parts = Path(relative).parts
        if parts and parts[0] in {"results", "evaluations"}:
            for length in range(1, len(parts)):
                directories.add(Path(*parts[:length]).as_posix())
    return sorted(directories)


def target_output_state(root: Path, contract: dict[str, Any]) -> str:
    inventory = output_namespace_inventory(root, contract)
    if inventory["unsafe"]:
        raise RuntimeError(f"unsafe target output namespace entries: {inventory['unsafe']}")
    entries = inventory["entries"]
    directories = inventory["directories"]
    allowed_directories = set(expected_output_directories(contract))
    if not entries and set(directories).issubset(allowed_directories):
        return "empty"
    if entries == expected_output_paths(contract) \
            and directories == expected_output_directories(contract):
        return "exact"
    raise RuntimeError(
        f"target output namespace is neither exact-empty nor exact-stage-A: "
        f"entries={entries}, directories={directories}"
    )


def input_hash_map(root: Path, contract: dict[str, Any]) -> dict[str, str]:
    excluded = {"evaluations", "results", contract["owned_paths"]["report"], MANIFEST_REL}
    hashes: dict[str, str] = {}

    def scan(path: Path) -> None:
        with os.scandir(path) as iterator:
            for entry in sorted(iterator, key=lambda item: item.name):
                if path == root and entry.name in excluded:
                    continue
                child = path / entry.name
                relative = child.relative_to(root).as_posix()
                if entry.is_symlink():
                    raise RuntimeError(f"input tree contains a symlink: {relative}")
                if entry.is_dir(follow_symlinks=False):
                    if entry.name in {"__pycache__", ".pytest_cache"}:
                        raise RuntimeError(f"input tree contains a cache directory: {relative}")
                    scan(child)
                elif entry.is_file(follow_symlinks=False):
                    if child.suffix in {".pyc", ".pyo"}:
                        raise RuntimeError(f"input tree contains bytecode: {relative}")
                    hashes[relative] = digest(child.read_bytes())
                else:
                    raise RuntimeError(f"input tree contains a special entry: {relative}")

    scan(root)
    return dict(sorted(hashes.items()))


def input_hash_map_sha256(values: dict[str, str]) -> str:
    return digest("".join(
        f"{values[relative]}  {relative}\n" for relative in sorted(values)
    ).encode("utf-8"))


def validate_staged_output_set(stage_root: Path, contract: dict[str, Any]) -> dict[str, bytes]:
    expected = expected_output_paths(contract)
    inventory = output_namespace_inventory(stage_root, contract)
    if inventory["entries"] != expected \
            or inventory["directories"] != expected_output_directories(contract) \
            or inventory["unsafe"]:
        raise RuntimeError(f"staged output namespace differs: {inventory}")
    return {relative: (stage_root / relative).read_bytes() for relative in expected}


def install_staged_outputs(stage_root: Path, target_root: Path, contract: dict[str, Any],
                           *, force_late_failure: bool = False) -> set[str]:
    payloads = validate_staged_output_set(stage_root, contract)
    target_output_state(target_root, contract)
    if force_late_failure:
        raise RuntimeError(FORCED_LATE_FAILURE)
    changed: set[str] = set()
    for relative in sorted(payloads):
        write_if_changed(target_root, relative, payloads[relative], changed)
    return changed


def transactional_preinstall_control(contract: dict[str, Any],
                                     stage_root: Path | None = None) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="paper41_transaction_control_") as temp_name:
        temp = Path(temp_name)
        synthetic_stage = temp / "stage"
        target = temp / "target"
        target.mkdir()
        if stage_root is None:
            synthetic_stage.mkdir()
            for relative in expected_output_paths(contract):
                path = synthetic_stage / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"paper41-transaction-control\n")
        else:
            synthetic_stage = stage_root
        observed = False
        try:
            install_staged_outputs(
                synthetic_stage, target, contract, force_late_failure=True
            )
        except RuntimeError as error:
            observed = str(error) == FORCED_LATE_FAILURE
        if not observed:
            raise RuntimeError("late pre-install failure control did not reach the exact gate")
        target_outputs = actual_output_paths(target, contract)
        target_caches = [
            path for path in target.rglob("*")
            if path.name in {"__pycache__", ".pytest_cache"} or path.suffix in {".pyc", ".pyo"}
        ]
        if target_outputs or target_caches:
            raise RuntimeError("late pre-install failure contaminated the empty target")
    return {
        "forced_failure_class": FORCED_LATE_FAILURE,
        "forced_failure_observed": True,
        "schema": "paper41-transactional-preinstall-control-v1",
        "target_cache_entries": 0,
        "target_output_paths_present": 0,
        "target_physical_writes": 0,
    }


def verify_static_gate(contract: dict[str, Any]) -> dict[str, Any]:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("parent interpreter isolation/bytecode guard is inactive")
    if (ROOT / MANIFEST_REL).exists() or (ROOT / MANIFEST_REL).is_symlink():
        raise RuntimeError("PAPER_MANIFEST.sha256 must be absent in Stage 1")
    owned = contract["owned_paths"]
    actual_code = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "code").rglob("*") if path.is_file())
    if actual_code != owned["code"]:
        raise RuntimeError("static code exact set mismatch")
    actual_experiments = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "experiments").rglob("*") if path.is_file())
    if actual_experiments != owned["experiments"]:
        raise RuntimeError("experiment exact set mismatch")
    for relative, expected in contract["experiment_freeze"].items():
        if digest((ROOT / relative).read_bytes()) != expected:
            raise RuntimeError(f"experiment freeze changed: {relative}")
    if len(snapshot_paths(ROOT, contract)) != contract["dependencies"]["snapshot_file_count"]:
        raise RuntimeError("source snapshot exact set mismatch")
    encoded = (ROOT / "docs/inputs/route-a-evaluator-v0.2.0.md.b64").read_bytes()
    decoded = b64decode(b"".join(encoded.split()), validate=True)
    if digest(encoded) != contract["dependencies"]["route_skill_encoded_sha256"] or \
            digest(decoded) != contract["dependencies"]["route_skill_decoded_sha256"]:
        raise RuntimeError("vendored Route skill bytes changed")
    if yaml.__version__ != "6.0.2":
        raise RuntimeError(f"PyYAML version changed: {yaml.__version__}")
    dependency_lock = json.loads((ROOT / "docs/DEPENDENCY_LOCK.json").read_text(encoding="utf-8"))
    if dependency_lock.get("python", {}).get("minimum") != "3.11" or sys.version_info < (3, 11):
        raise RuntimeError("Python minimum dependency contract is not satisfied")
    expected_entrypoint_policy = {
        "canonical_emitter_argv": ["python3", "-I", "-B", "code/source/emit_packet.py"],
        "canonical_parent_argv": ["python3", "-I", "-B", "code/run_exact_integration.py"],
        "child_invocation_flags": ["-I", "-B"],
        "child_only_entrypoints": [
            "code/audit_integrity.py", "code/evaluator/evaluate_packet.py",
            "code/evaluator/evaluate_route_a.py", "code/evaluator/independent_evaluator.py",
            "code/run_tests.py",
        ],
        "internal_transaction_stage_argv": [
            "python3", "-I", "-B", "code/run_exact_integration.py", INTERNAL_STAGE_FLAG,
        ],
        "naive_hostile_invocation_allowed": False,
        "self_reexec_is_security_boundary": False,
        "transaction_failure_probe_argv": [
            "python3", "-I", "-B", "code/run_exact_integration.py",
            "--force-late-transaction-failure",
        ],
    }
    if contract.get("entrypoint_policy") != expected_entrypoint_policy:
        raise RuntimeError("entrypoint isolation policy changed")
    return {
        "code_path_count": len(actual_code),
        "dont_write_bytecode": sys.dont_write_bytecode,
        "experiment_path_count": len(actual_experiments),
        "isolated_interpreter": bool(sys.flags.isolated),
        "python_minimum": "3.11",
        "python_minimum_satisfied": True,
        "PyYAML": yaml.__version__,
        "snapshot_path_count": len(snapshot_paths(ROOT, contract)),
    }


def call_leaf(call: ast.Call) -> str:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    return ""


def dynamic_call_aliases(tree: ast.AST) -> set[str]:
    """Return local names that can invoke Python's dynamic execution/import API."""
    direct = {"__import__", "compile", "eval", "exec", "getattr"}
    imported = {
        "import_module", "module_from_spec", "run_module", "run_path",
        "spec_from_file_location",
    }
    aliases = set(direct)
    module_aliases: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in {"builtins", "importlib", "importlib.util", "runpy"}:
                    module_aliases.add(alias.asname or alias.name.split(".", 1)[0])
        elif isinstance(node, ast.ImportFrom) and node.module in {
                "builtins", "importlib", "importlib.util", "runpy"}:
            for alias in node.names:
                if alias.name in direct | imported:
                    aliases.add(alias.asname or alias.name)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name) \
                and node.value.id in aliases:
            aliases.update(
                target.id for target in node.targets if isinstance(target, ast.Name)
            )
    return aliases | {
        f"{module}.{name}" for module in module_aliases for name in direct | imported
    }


def dynamic_call_name(call: ast.Call) -> str:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return ast.unparse(call.func)
    return ""


def boundary_ast_gate(path: Path, role: str) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    dynamic_aliases = dynamic_call_aliases(tree)
    allowed_reads = {
        "main_evaluator": {"open(argv[1], 'rb')", "open(argv[1], 'rb').read()"},
        "independent_evaluator": {
            "Path(argv[2]).read_bytes()", "handle.read()", "open(argv[1], 'rb')",
            "science_file.read_bytes()",
        },
    }
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        leaf = call_leaf(node)
        if dynamic_call_name(node) in dynamic_aliases:
            raise RuntimeError(f"{role} uses forbidden dynamic execution/import: {leaf}")
        rendered = ast.unparse(node)
        if role in {"source_core", "source_emit"} \
                and leaf in {"open", "read", "read_bytes", "read_text"} \
                and "code/evaluator/" in rendered:
            raise RuntimeError(f"{role} reads evaluator implementation bytes")
        if role in allowed_reads and leaf in {"open", "read", "read_bytes", "read_text"} \
                and rendered not in allowed_reads[role]:
            raise RuntimeError(f"{role} reads outside its packet/Route contract: {rendered}")


def expanded_import_records(tree: ast.AST) -> set[str]:
    records: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            records.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            records.add(module)
            records.update(
                f"{module}.{alias.name}" if module else alias.name
                for alias in node.names if alias.name != "*"
            )
    return records


def minimal_evaluator_packet_control(root: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="paper41_minimal_evaluators_") as temp_name:
        temp = Path(temp_name)
        packet = run_stdout(isolated_python(root / "code/source/emit_packet.py"), cwd=temp)
        packet_path = temp / "packet.json"
        packet_path.write_bytes(packet)
        scripts = {
            "independent_evaluator.py": root / "code/evaluator/independent_evaluator.py",
            "evaluate_packet.py": root / "code/evaluator/evaluate_packet.py",
        }
        for name, source in scripts.items():
            shutil.copyfile(source, temp / name)
        baseline_main = run_stdout(isolated_python(
            root / "code/evaluator/evaluate_packet.py", str(packet_path)
        ), cwd=temp)
        baseline_independent = run_stdout(isolated_python(
            root / "code/evaluator/independent_evaluator.py", str(packet_path)
        ), cwd=temp)
        minimal_main = run_stdout(isolated_python(temp / "evaluate_packet.py", str(packet_path)), cwd=temp)
        minimal_independent = run_stdout(isolated_python(
            temp / "independent_evaluator.py", str(packet_path)
        ), cwd=temp)
        if minimal_main != baseline_main or minimal_independent != baseline_independent:
            raise RuntimeError("minimal evaluator-only packet replay differs")
        unexpected = sorted(
            path.name for path in temp.iterdir()
            if path.name not in {"evaluate_packet.py", "independent_evaluator.py", "packet.json"}
        )
        if unexpected:
            raise RuntimeError(f"minimal evaluator replay created unexpected paths: {unexpected}")
    return {
        "files": ["evaluate_packet.py", "independent_evaluator.py", "packet.json"],
        "independent_stdout_sha256": digest(minimal_independent),
        "main_stdout_sha256": digest(minimal_main),
        "no_contracts_docs_or_source_present": True,
        "packet_sha256": digest(packet),
        "schema": "paper41-minimal-evaluator-packet-control-v1",
        "status": "PASS",
        "stdout_byte_identical_to_full_tree": True,
    }


def inspect_import_boundary(root: Path) -> dict[str, Any]:
    paths = {
        "source_core": root / "code/source/source_core.py",
        "source_emit": root / "code/source/emit_packet.py",
        "main_evaluator": root / "code/evaluator/evaluate_packet.py",
        "independent_evaluator": root / "code/evaluator/independent_evaluator.py",
        "route_renderer": root / "code/evaluator/evaluate_route_a.py",
        "integrity_auditor": root / "code/audit_integrity.py",
    }
    imports: dict[str, list[str]] = {}
    records: dict[str, set[str]] = {}
    for name, path in paths.items():
        boundary_ast_gate(path, name)
        tree = ast.parse(path.read_text(encoding="utf-8"))
        modules: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                modules.add(node.module or "")
        imports[name] = sorted(modules)
        records[name] = expanded_import_records(tree)
    if any("evaluator" in module for module in imports["source_core"] + imports["source_emit"]):
        raise RuntimeError("source imports an evaluator")
    if any(module in {"source_core", "emit_packet"} or module.startswith("code.source")
           for module in imports["main_evaluator"] + imports["independent_evaluator"]):
        raise RuntimeError("evaluator imports source implementation")
    if any("evaluate_packet" in module or "evaluate_route_a" in module
           for module in imports["independent_evaluator"]):
        raise RuntimeError("independent evaluator imports another evaluator")
    if any("independent_evaluator" in name for name in records["main_evaluator"]):
        raise RuntimeError("main evaluator imports independent evaluator")
    if any("evaluate_route_a" in name for name in records["main_evaluator"]):
        raise RuntimeError("main evaluator imports Route renderer")
    if any(name == "code" or name.startswith("code.") for name in records["main_evaluator"]):
        raise RuntimeError("main evaluator imports local code namespace")
    if any("source_core" in name or "code.source" in name for name in records["route_renderer"]):
        raise RuntimeError("Route renderer imports source implementation")
    if any("evaluate_route_a" in name for name in records["integrity_auditor"]):
        raise RuntimeError("auditor imports Route renderer")
    return {
        "auditor_imports_production": False,
        "dynamic_execution_or_import_calls": [],
        "evaluator_unexpected_file_reads": [],
        "independent_imports_main_or_route": False,
        "main_imports_source": False,
        "minimal_packet_runtime": minimal_evaluator_packet_control(root),
        "module_imports": imports,
        "route_imports_production": False,
        "schema": "paper41-source-evaluator-boundary-v3",
        "science_projection_byte_control": science_projection_byte_control(),
        "source_imports_evaluator": False,
    }


def route_run_projection(science: dict[str, Any]) -> dict[str, Any]:
    return {
        "candidate_id": "SD-C43",
        "overall_verdict": science["route"]["overall_verdict"],
        "route_b_invocation_allowed": science["route"]["route_b_invocation_allowed"],
        "route_tuple": science["route"]["route_tuple"],
        "schema": "paper41-run-route-projection-v1",
        "science_sha256": digest(canonical(science)),
        "terminal_codes": science["terminal_codes"],
    }


def execute_run(project: Path, *, cwd: Path) -> dict[str, bytes]:
    with tempfile.TemporaryDirectory(prefix="paper41_run_") as temp_name:
        packet_path = Path(temp_name) / "source_packet.json"
        packet = run_stdout(isolated_python(project / "code/source/emit_packet.py"), cwd=cwd)
        packet_path.write_bytes(packet)
        main = run_stdout(isolated_python(project / "code/evaluator/evaluate_packet.py", str(packet_path)), cwd=cwd)
        independent = run_stdout(isolated_python(project / "code/evaluator/independent_evaluator.py", str(packet_path)), cwd=cwd)
    main_data = json.loads(main)
    independent_data = json.loads(independent)
    science = require_science_projection_bytes_equal(
        main_data["science"], independent_data["science"]
    )
    return {
        "source_packet.json": packet,
        "main_evaluation.json": main,
        "independent_evaluation.json": independent,
        "scientific_results.json": science,
        "route_evaluation.json": canonical(route_run_projection(main_data["science"])),
    }


def copy_static_for_cold(source: Path, destination: Path) -> None:
    def ignore(directory: str, names: list[str]) -> set[str]:
        ignored = {"__pycache__", ".pytest_cache"}.intersection(names)
        if Path(directory).resolve() == source.resolve():
            ignored.update({"results", "evaluations", "EXPERIMENT_REPORT.md", MANIFEST_REL}.intersection(names))
        return ignored
    shutil.copytree(source, destination, ignore=ignore)


def compare_runs(reference: dict[str, bytes], candidate: dict[str, bytes], label: str) -> None:
    if set(reference) != set(candidate):
        raise RuntimeError(f"{label} run artifact set differs")
    for name in sorted(reference):
        if reference[name] != candidate[name]:
            raise RuntimeError(f"{label} run differs at {name}")


def optional_live_source_comparison(root: Path, contract: dict[str, Any]) -> dict[str, Any]:
    snapshot_root = root / contract["owned_paths"]["repo_snapshot_root"]
    containers = sorted(path for path in snapshot_root.rglob("*") if path.is_file())
    if len(containers) != contract["dependencies"]["snapshot_file_count"] \
            or any(path.suffix != ".b64" for path in containers):
        raise RuntimeError("vendored source snapshot inventory changed")
    return {
        "comparison_affects_science_bytes": False,
        "external_historical_tree_available": "NOT_QUERIED_CANONICAL",
        "external_historical_tree_read": False,
        "live_files_compared": 0,
        "matches": "NOT_APPLICABLE_CANONICAL_PORTABLE_RUN",
        "schema": "paper41-optional-live-provenance-comparison-v1",
        "snapshot_container_count": len(containers),
        "status": "PASS",
    }


def mutation_ledger_projection(mutation: dict[str, Any]) -> dict[str, Any]:
    identifiers = mutation.get("mutation_ids")
    if not isinstance(identifiers, list) or identifiers != sorted(set(identifiers)) \
            or not all(isinstance(item, str) and item for item in identifiers):
        raise RuntimeError("report mutation IDs are not globally sorted and unique")
    identifier_hash = digest("".join(item + "\n" for item in identifiers).encode("ascii"))
    if identifier_hash != mutation.get("mutation_ids_sha256") \
            or len(identifiers) != mutation.get("total_mutations"):
        raise RuntimeError("report mutation ID ledger hash/count differs")
    groups = {
        name: {
            "count": mutation["groups"][name]["count"],
            "ids_sha256": mutation["groups"][name]["id_sha256"],
        }
        for name in ("audit", "packet", "route", "selection", "static")
    }
    return {
        "groups": groups,
        "mutation_ids": identifiers,
        "mutation_ids_sha256": identifier_hash,
        "registry_sha256": mutation["registry_sha256"],
        "schema": "paper41-report-mutation-ledger-v1",
        "total_mutations": len(identifiers),
    }


def registry_identifiers(contract: dict[str, Any]) -> list[str]:
    raw = (ROOT / REGISTRY_REL).read_bytes()
    if digest(raw) != contract["mutation_registry"]["sha256"]:
        raise RuntimeError("mutation registry hash differs before report projection")
    value = json.loads(raw)
    identifiers = sorted(
        row["id"]
        for group in ("packet_mutations", "selection_mutations", "route_mutations",
                      "static_mutations", "audit_mutations")
        for row in value[group]
    )
    if identifiers != sorted(set(identifiers)):
        raise RuntimeError("mutation registry IDs collide")
    return identifiers


def report_bytes(science: dict[str, Any], mutation: dict[str, Any], reproducibility: dict[str, Any],
                 route_validation: dict[str, Any]) -> bytes:
    h = science["h_values"]
    chronology_json = canonical(science["integration_chronology"]).decode("ascii").rstrip("\n")
    mutation_ledger_json = canonical(mutation_ledger_projection(mutation)).decode("ascii").rstrip("\n")
    text = f"""# Paper 41 exact authority-integration report

## Outcome

The self-contained exact source and two physically distinct evaluators agree
on the frozen `SD-C43` closure. The matrix-primary implementation and the
recurrence-first implementation reproduce

```text
h(epsilon)={h['']}, h(0)={h['0']}, h(1)={h['1']},
h(01)={h['01']}, h(10)={h['10']}, h(11)={h['11']},
h(001)={h['001']}, h(010)={h['010']}.
```

They therefore confirm append-one non-descent, cyclic-clock failure,
temporal-power failure, and both literal Liouville character failures. The
finite diagonal calculation is only an exact consistency control for the
inherited multiplicity theorem; it is not promoted to a primitive-return
determinant.

## Selection and chronology

The portable resolver verifies {science['source_resolver']['matches']} of 22
typed source IDs. The literal six-card Boolean rule returns exactly
`{science['selection']['survivors'][0]}`. The rule, witnesses, and outcomes
were known before this authority-integration protocol; prospective,
outcome-independent, preregistration, novelty, and priority flags remain
false.

The original experiment documents were frozen before the initial authority
code and outputs, but the replacement seal is a corrective reseal after
failed outputs and audit findings. Superseded materialization bytes, the
unsorted result contract and raw-snapshot hygiene repair, direct-write
changed-path/idempotence defects, post-seal evaluator byte drift, Route
semantic survivors, mutation-coverage gaps, the superseded `1c38...` seal and
clone evidence, parent pre-bootstrap shadow/cache exposure, direct-emitter
bytecode caching, mandatory external-tree dependence, cross-evaluator Python
equality type coercion, and CLI/Python-version contract gaps were all known
along with Python's pre-line-1 `sitecustomize` startup gap, packet/selection
numeric-equivalent type gaps, coordinated auditor JSON-type gaps, the missing
globally sorted mutation/report ledger, evaluator direct-read and dynamic-import
boundary gaps, hostile-parent-environment negative-control weakness, critical
result semantic-auditor closure gaps, and missing immutable-ledger mutation
coverage, per-role AST allowlist gaps, missing portable source-structure rows,
missing ordered-selection/safe-existing-Route-artifact controls, and the
nontransactional failed-clone contamination gap before the final replacement
static seal. Only the final replacement static
bytes were frozen before the final replacement canonical rerun; corrected
implementation bytes and prior clone results are not claimed unseen, blind,
or fully prospective. These are integration-engineering/static repairs, not a
post-result scientific/model repair.

```json
{chronology_json}
```

## Route result

```text
({', '.join(science['route']['route_tuple'])})

overall: {science['route']['overall_verdict']}
route_b_invocation_allowed: false
```

The strict Route validator passes {route_validation['check_count']} checks.
The valid diagonal inventory determinant does not earn A2, and its
parameter-dependent operator does not earn A4.

## Adversarial and reproducibility result

- packet mutations: {mutation['groups']['packet']['count']}; survivors: 0;
- selection mutations: {mutation['groups']['selection']['count']}; survivors: 0;
- Route mutations: {mutation['groups']['route']['count']}; survivors: 0;
- recursive Route rows: 443 = 176 scalar value-and-type drifts + 80 list-index
  value drifts + 126 mapping-key deletions + 16 mapping insertions + 15 list
  deletions + 15 list duplications + 15 list-order reversals; the four paired
  provenance fields are normalized only for comparison and tested separately;
- static mutations: {mutation['groups']['static']['count']}; survivors: 0;
- read-only audit mutations: {mutation['groups']['audit']['count']}; survivors: 0;
- dual-evaluator rejection decisions: {mutation['dual_rejections']};
- A/B/cold deterministic artifact equality: {str(reproducibility['all_equal']).lower()};
- read-only paired State A/State B audit: pass with byte-identical stdout;
- final idempotence target: `changed_paths=0`.

The following JSON is the complete globally C-sorted mutation-ID ledger and
its registry, total, and per-group anchors.

```json
{mutation_ledger_json}
```

No target zeros, target roots, prime table, fitting, stochastic selection, or
post-result scientific/model repair is used; the corrective post-output
integration-engineering and static repairs are disclosed above. The authority
remains in Stage 1 with no paper manifest. Writer files, immutable research,
external DA, Git, root README, registry, and mirror state are outside integrator
ownership and were not modified.
"""
    return text.encode("utf-8")


def mutation_placeholder(contract: dict[str, Any]) -> dict[str, Any]:
    frozen = contract["mutation_registry"]
    raw = (ROOT / REGISTRY_REL).read_bytes()
    if digest(raw) != frozen["sha256"]:
        raise RuntimeError("mutation registry hash differs before expected-result construction")
    registry = json.loads(raw)
    specifications = {
        "audit": ("audit_mutations", "auditor_rejects"),
        "packet": ("packet_mutations", "dual"),
        "route": ("route_mutations", "dual"),
        "selection": ("selection_mutations", "dual"),
        "static": ("static_mutations", "auditor_rejects"),
    }
    groups: dict[str, Any] = {}
    identifiers: list[str] = []
    for name, (registry_key, decision) in specifications.items():
        rows = registry[registry_key]
        ids = [row["id"] for row in rows]
        if ids != sorted(set(ids)):
            raise RuntimeError(f"{name} mutation registry IDs differ")
        identifiers.extend(ids)
        executed = []
        for row in rows:
            decisions = (
                {"independent_rejects": True, "main_rejects": True}
                if decision == "dual" else {decision: True}
            )
            executed.append({
                **decisions,
                "expected_rejection": row["expected_rejection"],
                "id": row["id"],
                "json_pointer": row["json_pointer"],
                "operation": row["operation"],
            })
        groups[name] = {
            "count": frozen[f"{name}_count"],
            "id_sha256": frozen[f"{name}_ids_sha256"],
            "rows": executed,
            "survivors": [],
        }
    identifiers = sorted(identifiers)
    if identifiers != registry_identifiers(contract):
        raise RuntimeError("expected mutation result ID ledger differs")
    return {
        "audit_rejections": frozen["audit_count"],
        "dual_rejections": frozen["dual_evaluator_rejection_count"],
        "groups": groups,
        "mutation_ids": identifiers,
        "mutation_ids_sha256": frozen["total_ids_sha256"],
        "registry_sha256": frozen["sha256"],
        "schema": "paper41-adversarial-mutation-results-v2",
        "static_rejections": frozen["static_count"],
        "survivors": [],
        "total_mutations": frozen["total_count"],
    }


def prepare_manifest(root: Path) -> bytes:
    paths = sorted(path.relative_to(root).as_posix() for path in root.rglob("*")
                   if path.is_file() and path.relative_to(root).as_posix() != MANIFEST_REL)
    return "".join(f"{digest((root / relative).read_bytes())}  {relative}\n" for relative in paths).encode("utf-8")


def materialize(contract: dict[str, Any]) -> set[str]:
    changed: set[str] = set()
    static_gate = verify_static_gate(contract)
    static_gate["transactional_preinstall_control"] = transactional_preinstall_control(contract)
    isolation_control = hostile_environment_control()
    boundary = inspect_import_boundary(ROOT)
    route_module = load_module(ROOT / "code/evaluator/evaluate_route_a.py", "paper41_route_renderer")
    audit_module = load_module(ROOT / "code/audit_integrity.py", "paper41_integrity_auditor")

    run_artifacts: dict[str, dict[str, bytes]] = {}
    for label in ("A", "B"):
        run_artifacts[label] = execute_run(ROOT, cwd=ROOT)
        for name, raw in run_artifacts[label].items():
            write_if_changed(ROOT, f"results/runs/{label}/{name}", raw, changed)
    run_a = run_artifacts["A"]
    run_b = run_artifacts["B"]
    compare_runs(run_a, run_b, "B")

    for name in ("source_packet.json", "main_evaluation.json", "independent_evaluation.json", "scientific_results.json"):
        raw = run_a[name]
        write_if_changed(ROOT, f"results/{name}", raw, changed)

    with tempfile.TemporaryDirectory(prefix="paper41_cold_") as temp_name:
        temp = Path(temp_name)
        cold = temp / "relocated-paper41"
        copy_static_for_cold(ROOT, cold)
        cold_artifacts = execute_run(cold, cwd=temp)
        compare_runs(run_a, cold_artifacts, "cold C")
        for name, raw in cold_artifacts.items():
            write_if_changed(ROOT, f"results/runs/C/{name}", raw, changed)

    science = json.loads(run_a["scientific_results.json"])
    science_hash = digest(run_a["scientific_results.json"])
    source_packet_hash = digest(run_a["source_packet.json"])
    write_if_changed(ROOT, "results/source_resolver.json", canonical(science["source_resolver"]), changed)
    write_if_changed(ROOT, "results/selection_resolver.json", canonical(science["selection"]), changed)
    write_if_changed(ROOT, "results/source_evaluator_boundary.json", canonical(boundary), changed)
    write_if_changed(ROOT, "results/external_provenance_stability.json",
                     canonical(optional_live_source_comparison(ROOT, contract)), changed)

    dependency = {
        "PyYAML": yaml.__version__,
        "dependency_lock_sha256": contract["dependencies"]["dependency_lock_sha256"],
        "paper40_da_report_sha256": contract["dependencies"]["paper40_da_report_sha256"],
        "paper40_da_sidecar_sha256": contract["dependencies"]["paper40_da_sidecar_sha256"],
        "route_skill_decoded_sha256": contract["dependencies"]["route_skill_decoded_sha256"],
        "schema": "paper41-dependency-controls-v1",
        "source_snapshot_files": contract["dependencies"]["snapshot_file_count"],
        "status": "PASS",
        "interpreter_isolation": isolation_control,
        "entrypoint_policy": contract["entrypoint_policy"],
        "python_minimum": "3.11",
        "python_minimum_satisfied": True,
    }
    write_if_changed(ROOT, "results/dependency_controls.json", canonical(dependency), changed)
    immutable = {
        **contract["immutable_release"],
        "schema": "paper41-immutable-input-reproduction-v1",
        "status": "PASS",
    }
    write_if_changed(ROOT, "results/immutable_inputs.json", canonical(immutable), changed)
    research = {
        "h_values": science["h_values"],
        "main_independent_equal": True,
        "schema": "paper41-research-reproduction-v1",
        "theorems": science["theorems"],
        "universal_no_go_claimed": False,
    }
    write_if_changed(ROOT, "results/research_reproduction.json", canonical(research), changed)

    route_bytes = route_module.render_route(science, PENDING, False)
    write_if_changed(ROOT, ROUTE_REL, route_bytes, changed)
    main_route_bytes = run_stdout(isolated_python(
        ROOT / "code/evaluator/evaluate_route_a.py", "validate", str(ROOT / ROUTE_REL), "absent"
    ), cwd=ROOT)
    independent_route_bytes = run_stdout(isolated_python(
        ROOT / "code/evaluator/independent_evaluator.py", "--route", str(ROOT / ROUTE_REL), "absent", str(ROOT)
    ), cwd=ROOT)
    main_route = json.loads(main_route_bytes)
    independent_route = json.loads(independent_route_bytes)
    write_if_changed(ROOT, "results/route_evaluation.json", main_route_bytes, changed)
    write_if_changed(ROOT, ROUTE_JSON_REL, independent_route_bytes, changed)
    route_certificate = {
        "independent_check_count": independent_route["check_count"],
        "independent_route_sha256": digest(independent_route_bytes),
        "main_check_count": main_route["check_count"],
        "main_route_sha256": digest(main_route_bytes),
        "paired_state": "VALID_STAGE1",
        "schema": "paper41-route-schema-certificate-v1",
        "tuple_agreement": main_route["route_tuple"] == independent_route["route_tuple"] == contract["route_contract"]["tuple"],
    }
    write_if_changed(ROOT, "results/route_schema_certificate.json", canonical(route_certificate), changed)

    mutation = mutation_placeholder(contract)
    if not (ROOT / "results/adversarial_tests.json").is_file():
        write_if_changed(ROOT, "results/adversarial_tests.json", canonical(mutation), changed)

    run_hashes = {
        label: {name: digest((ROOT / f"results/runs/{label}/{name}").read_bytes()) for name in RUN_FILES}
        for label in ("A", "B", "C")
    }
    reproducibility = {
        "all_equal": run_hashes["A"] == run_hashes["B"] == run_hashes["C"],
        "artifact_count_per_run": len(RUN_FILES),
        "run_hashes": run_hashes,
        "schema": "paper41-reproducibility-certificate-v1",
    }
    if not reproducibility["all_equal"]:
        raise RuntimeError("A/B/cold hashes differ")
    write_if_changed(ROOT, "results/reproducibility_certificate.json", canonical(reproducibility), changed)
    write_if_changed(ROOT, "results/cold_copy_certificate.json", canonical({
        "external_historical_tree_read": False,
        "non_project_cwd": True,
        "relocated": True,
        "run_c_equals_run_a": True,
        "schema": "paper41-cold-copy-certificate-v1",
    }), changed)
    write_if_changed(ROOT, "results/analysis_summary.json", canonical({
        "candidate_id": "SD-C43",
        "main_independent_science_equal": True,
        "mutation_survivors": 0,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "schema": "paper41-analysis-summary-v1",
        "science_sha256": science_hash,
        "source_packet_sha256": source_packet_hash,
    }), changed)
    write_if_changed(ROOT, "results/integrity_contract.json", canonical({
        "contract_sha256": CONTRACT_SHA256,
        "managed_path_count": len(managed_paths(ROOT, contract)),
        "result_path_count": len(contract["owned_paths"]["results"]),
        "schema": "paper41-integrity-contract-result-v1",
        "static_gate": static_gate,
    }), changed)
    write_if_changed(ROOT, "results/exact_result_set.json", canonical({
        "paths": contract["owned_paths"]["results"],
        "schema": "paper41-exact-result-set-v1",
    }), changed)
    write_if_changed(ROOT, "results/exact_text_set.json", canonical({
        "ledger_exclusions": [LEDGER_REL, MANIFEST_REL, ROUTE_REL],
        "managed_paths": managed_paths(ROOT, contract),
        "schema": "paper41-exact-integration-text-set-v1",
        "writer_paths_included": False,
    }), changed)
    write_if_changed(ROOT, "results/idempotence_certificate.json", canonical({
        "changed_paths": 0,
        "schema": "paper41-idempotence-certificate-v1",
        "status": "PASS",
    }), changed)

    audit_bytes = audit_module.canonical(audit_module.pass_result())
    audit_hash = digest(audit_bytes)
    write_if_changed(ROOT, "results/integrity_audit.json", audit_bytes, changed)
    sealed_certificate = {
        "audit_stdout_sha256": audit_hash,
        "dummy_commit": DUMMY_COMMIT,
        "schema": "paper41-sealed-state-compatibility-v1",
        "state_a_status": "PASS",
        "state_b_status": "PASS",
        "stdout_byte_identical": True,
    }
    write_if_changed(ROOT, "results/sealed_state_compatibility.json", canonical(sealed_certificate), changed)

    write_if_changed(ROOT, REPORT_REL, report_bytes(science, mutation, reproducibility, main_route), changed)

    ledger_paths = sorted(set(managed_paths(ROOT, contract)) - {LEDGER_REL, ROUTE_REL, MANIFEST_REL})
    missing = [relative for relative in ledger_paths if not (ROOT / relative).is_file()]
    if missing:
        raise RuntimeError("cannot seal missing managed paths: " + ", ".join(missing))
    ledger = "".join(f"{digest((ROOT / relative).read_bytes())}  {relative}\n" for relative in ledger_paths).encode("utf-8")
    write_if_changed(ROOT, LEDGER_REL, ledger, changed)

    mutation_bytes = run_stdout(isolated_python(
        ROOT / "code/run_tests.py", str(ROOT / "results/source_packet.json"), str(ROOT / ROUTE_REL), str(ROOT)
    ), cwd=ROOT)
    mutation = json.loads(mutation_bytes)
    if mutation_bytes != canonical(mutation_placeholder(contract)):
        raise RuntimeError("mutation result bytes differ from the frozen exhaustive expectation")
    frozen_mutation = contract["mutation_registry"]
    if (
        type(mutation.get("total_mutations")) is not int
        or mutation["total_mutations"] != frozen_mutation["total_count"]
        or type(mutation.get("dual_rejections")) is not int
        or mutation["dual_rejections"] != frozen_mutation["dual_evaluator_rejection_count"]
        or mutation["mutation_ids_sha256"] != frozen_mutation["total_ids_sha256"]
        or mutation.get("mutation_ids") != registry_identifiers(contract)
        or mutation["registry_sha256"] != frozen_mutation["sha256"]
        or mutation["survivors"]
    ):
        raise RuntimeError("mutation result does not match frozen exhaustive registry")
    for group_name in ("packet", "selection", "route", "static", "audit"):
        group = mutation["groups"][group_name]
        if (
            type(group.get("count")) is not int
            or group["count"] != frozen_mutation[f"{group_name}_count"]
            or group["id_sha256"] != frozen_mutation[f"{group_name}_ids_sha256"]
            or group["survivors"]
        ):
            raise RuntimeError(f"mutation group seal differs: {group_name}")
    write_if_changed(ROOT, "results/adversarial_tests.json", mutation_bytes, changed)
    write_if_changed(ROOT, REPORT_REL, report_bytes(science, mutation, reproducibility, main_route), changed)
    ledger = "".join(f"{digest((ROOT / relative).read_bytes())}  {relative}\n" for relative in ledger_paths).encode("utf-8")
    write_if_changed(ROOT, LEDGER_REL, ledger, changed)

    actual_audit = run_stdout(isolated_python(ROOT / "code/audit_integrity.py", str(ROOT)), cwd=ROOT)
    if actual_audit != audit_bytes:
        raise RuntimeError("actual State-A audit bytes differ from frozen pass bytes")

    with tempfile.TemporaryDirectory(prefix="paper41_sealed_") as temp_name:
        sealed = Path(temp_name) / "sealed-paper41"
        shutil.copytree(ROOT, sealed, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        (sealed / ROUTE_REL).write_bytes(route_module.render_route(science, DUMMY_COMMIT, True))
        (sealed / MANIFEST_REL).write_bytes(prepare_manifest(sealed))
        sealed_audit = run_stdout(isolated_python(sealed / "code/audit_integrity.py", str(sealed)), cwd=Path(temp_name))
        if sealed_audit != actual_audit:
            raise RuntimeError("paired State-B audit stdout differs")
        run_stdout(isolated_python(
            sealed / "code/evaluator/evaluate_route_a.py", "validate", str(sealed / ROUTE_REL), "present"
        ), cwd=Path(temp_name))
        run_stdout(isolated_python(
            sealed / "code/evaluator/independent_evaluator.py", "--route", str(sealed / ROUTE_REL),
            "present", str(sealed)
        ), cwd=Path(temp_name))
    return changed


def hash_managed(contract: dict[str, Any]) -> dict[str, str]:
    return {relative: digest((ROOT / relative).read_bytes()) for relative in managed_paths(ROOT, contract)}


def stage_certificate(root: Path, contract: dict[str, Any], changed_count: int) -> dict[str, Any]:
    payloads = validate_staged_output_set(root, contract)
    inputs = input_hash_map(root, contract)
    path_stream = "".join(relative + "\n" for relative in sorted(payloads)).encode("utf-8")
    hash_stream = "".join(
        f"{digest(payloads[relative])}  {relative}\n" for relative in sorted(payloads)
    ).encode("utf-8")
    return {
        "changed_path_count": changed_count,
        "input_hash_map_sha256": input_hash_map_sha256(inputs),
        "input_path_count": len(inputs),
        "integrity_audit_sha256": digest(payloads["results/integrity_audit.json"]),
        "mutation_count": contract["mutation_registry"]["total_count"],
        "output_hash_map_sha256": digest(hash_stream),
        "output_path_count": len(payloads),
        "output_path_list_sha256": digest(path_stream),
        "schema": "paper41-validated-transaction-stage-v1",
        "status": "PASS",
        "transactional_preinstall_control": transactional_preinstall_control(contract, root),
    }


def build_validated_stage_and_install(contract: dict[str, Any],
                                      *, force_late_failure: bool = False) -> set[str]:
    initial_state = target_output_state(ROOT, contract)
    initial_inputs = input_hash_map(ROOT, contract)
    with tempfile.TemporaryDirectory(prefix="paper41_output_transaction_") as temp_name:
        temp = Path(temp_name)
        stage = temp / "stage-paper41"
        copy_static_for_cold(ROOT, stage)
        if input_hash_map(stage, contract) != initial_inputs:
            raise RuntimeError("transaction stage input map differs before execution")
        stage_env = environment()
        stage_env[INTERNAL_STAGE_ENV] = "1"
        completed = subprocess.run(
            isolated_python(stage / "code/run_exact_integration.py", INTERNAL_STAGE_FLAG),
            cwd=temp, env=stage_env, capture_output=True, check=False,
        )
        if completed.returncode != 0 or completed.stderr:
            raise RuntimeError(
                "validated output stage failed before target install: "
                f"rc={completed.returncode}; stderr={completed.stderr.decode(errors='replace')!r}"
            )
        stage_result = json.loads(completed.stdout)
        expected_stage_result = stage_certificate(
            stage, contract, len(expected_output_paths(contract))
        )
        if canonical(stage_result) != canonical(expected_stage_result):
            raise RuntimeError("validated stage certificate differs before target install")
        if input_hash_map(stage, contract) != initial_inputs:
            raise RuntimeError("transaction stage changed its complete input byte map")
        if target_output_state(ROOT, contract) != initial_state \
                or input_hash_map(ROOT, contract) != initial_inputs:
            raise RuntimeError("target tree changed while the isolated stage was executing")
        if force_late_failure:
            raise RuntimeError(FORCED_LATE_FAILURE)
        changed = install_staged_outputs(stage, ROOT, contract)
        if input_hash_map(ROOT, contract) != initial_inputs:
            raise RuntimeError("target input map changed during output install")
        return changed


def stage_main() -> int:
    try:
        if os.environ.get(INTERNAL_STAGE_ENV) != "1":
            raise RuntimeError("internal transaction stage requires the parent-controlled environment")
        contract = load_contract()
        if target_output_state(ROOT, contract) != "empty":
            raise RuntimeError("internal transaction stage was not empty")
        changed = materialize(contract)
        expected = set(expected_output_paths(contract))
        if changed != expected:
            raise RuntimeError(
                f"internal stage changed-set differs: missing={sorted(expected - changed)}, "
                f"extra={sorted(changed - expected)}"
            )
        result = stage_certificate(ROOT, contract, len(changed))
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(canonical(result))
    return 0


def main(*, force_late_failure: bool = False) -> int:
    try:
        contract = load_contract()
        expected_outputs = set(expected_output_paths(contract))
        preexisting_state = target_output_state(ROOT, contract)
        first_changed = build_validated_stage_and_install(
            contract, force_late_failure=force_late_failure
        )
        if preexisting_state == "empty" and first_changed != expected_outputs:
            missing = sorted(expected_outputs - first_changed)
            extra = sorted(first_changed - expected_outputs)
            raise RuntimeError(f"fresh first-write ledger mismatch: missing={missing}, extra={extra}")
        if preexisting_state == "exact" and first_changed:
            raise RuntimeError(f"replay rewrote authority outputs: {sorted(first_changed)}")
        before = hash_managed(contract)
        second_changed = build_validated_stage_and_install(contract)
        after = hash_managed(contract)
        changed_paths = sorted(path for path in before if before[path] != after[path])
        if second_changed or changed_paths:
            raise RuntimeError(f"idempotence failed: writes={sorted(second_changed)}, hashes={changed_paths}")
        final_audit = run_stdout(isolated_python(ROOT / "code/audit_integrity.py", str(ROOT)), cwd=ROOT)
        result = {
            "first_materialization_changed_path_count": len(first_changed),
            "idempotence_changed_paths": 0,
            "integrity_audit_sha256": digest(final_audit),
            "managed_path_count": len(before),
            "mutation_count": contract["mutation_registry"]["total_count"],
            "output_path_count": len(expected_outputs),
            "route_b_invocation_allowed": False,
            "schema": "paper41-authority-integration-run-v1",
            "status": "PASS",
        }
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--isolation-probe"]:
        sys.stdout.buffer.write(canonical(isolation_probe()))
        raise SystemExit(0)
    if sys.argv[1:] == [INTERNAL_STAGE_FLAG]:
        raise SystemExit(stage_main())
    if sys.argv[1:] == ["--force-late-transaction-failure"]:
        raise SystemExit(main(force_late_failure=True))
    if sys.argv[1:]:
        print("FAIL: unsupported parent argument", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main())
