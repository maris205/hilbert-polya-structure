"""Closed, semantically checked selection for the final result manifest."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Callable


EXPECTED_LOCK_SHA256 = "d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7"

REQUIRED_RESULT_JSON = (
    "source_lock_validation.json",
    "target_isolation_audit.json",
    "proof_audit.json",
    "control_audit.json",
    "henon_static_audit.json",
    "command_environment_manifest.json",
    "run_summary.json",
)
REQUIRED_RESULT_REPORTS = (
    "CODE_REVIEW.md",
    "VALIDATION_REPORT.md",
    "EXPERIMENT_RESULTS.md",
    "pytest.xml",
)
REQUIRED_PROJECT_FILES = (
    "experiments/source_lock.json",
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "notes/PROOF_PACKAGE.md",
    "notes/INDEPENDENT_COUNTEREXAMPLE_REVIEW.md",
)
FINAL_RESULT_MANIFEST = "final_result_manifest.json"
REQUIRED_RESULT_PATHS = {
    f"results/{name}" for name in REQUIRED_RESULT_JSON + REQUIRED_RESULT_REPORTS
}
ALLOWED_RESULT_PATHS = REQUIRED_RESULT_PATHS | {
    f"results/{FINAL_RESULT_MANIFEST}"
}


def _is_within(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
    except ValueError:
        return False
    return True


def _result_schema_audit(project_root: Path) -> dict[str, Any]:
    """Require a flat, exact, regular-file result schema.

    The final manifest itself is an optional output and is never an input.
    Every other discovered result must be one of the eleven declared inputs.
    Symlinks are forbidden even when they resolve inside the project.
    """

    root = project_root.resolve()
    results = root / "results"
    if not results.exists():
        return {
            "discovered_result_paths": [],
            "missing_required_result_paths": sorted(REQUIRED_RESULT_PATHS),
            "unknown_result_paths": [],
            "nested_result_paths": [],
            "duplicate_basenames": [],
            "symlink_paths": [],
            "outside_root_paths": [],
            "pass": False,
        }

    root_symlink = results.is_symlink()
    discovered_entries = [] if root_symlink else sorted(results.rglob("*"))
    discovered_files: list[Path] = []
    nested: list[str] = []
    symlinks: list[str] = ["results"] if root_symlink else []
    outside: list[str] = []

    for path in discovered_entries:
        relative = path.relative_to(root)
        relative_text = str(relative)
        if path.is_symlink():
            symlinks.append(relative_text)
        resolved = path.resolve(strict=False)
        if not _is_within(root, resolved):
            outside.append(relative_text)
        result_relative = path.relative_to(results)
        if path.is_dir() or len(result_relative.parts) != 1:
            nested.append(relative_text)
        if path.is_file() or path.is_symlink():
            discovered_files.append(path)

    discovered_paths = {str(path.relative_to(root)) for path in discovered_files}
    unknown = sorted(discovered_paths - ALLOWED_RESULT_PATHS)
    missing = sorted(REQUIRED_RESULT_PATHS - discovered_paths)
    basename_counts = Counter(path.name for path in discovered_files)
    duplicate_basenames = sorted(
        basename for basename, count in basename_counts.items() if count > 1
    )
    passed = not any(
        (
            missing,
            unknown,
            nested,
            duplicate_basenames,
            symlinks,
            outside,
        )
    )
    return {
        "discovered_result_paths": sorted(discovered_paths),
        "missing_required_result_paths": missing,
        "unknown_result_paths": unknown,
        "nested_result_paths": sorted(set(nested)),
        "duplicate_basenames": duplicate_basenames,
        "symlink_paths": sorted(set(symlinks)),
        "outside_root_paths": sorted(set(outside)),
        "pass": passed,
    }


def _validate_selected_path(root: Path, path: Path) -> None:
    if path.is_symlink():
        raise ValueError(f"manifest input may not be a symlink: {path}")
    if not path.is_file():
        raise ValueError(f"manifest input must be a regular file: {path}")
    if not _is_within(root, path.resolve(strict=True)):
        raise ValueError(f"manifest input resolves outside project root: {path}")


def collect_manifest_inputs(project_root: Path) -> list[Path]:
    """Collect the exact result schema plus frozen source and Python code."""

    root = project_root.resolve()
    schema = _result_schema_audit(root)
    if not schema["pass"]:
        raise ValueError(
            "result schema is not exact and closed: "
            + json.dumps(schema, sort_keys=True)
        )
    selected = [root / relative for relative in sorted(REQUIRED_RESULT_PATHS)]
    selected.extend(root / relative for relative in REQUIRED_PROJECT_FILES)
    selected.extend(sorted((root / "code").rglob("*.py")))
    unique = sorted(set(selected))
    for path in unique:
        _validate_selected_path(root, path)
    return unique


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return value


def _validate_source_lock(record: dict[str, Any]) -> bool:
    return (
        record.get("pass") is True
        and record.get("lock_version") == 3
        and record.get("sha256") == EXPECTED_LOCK_SHA256
        and record.get("prelock_execution_clean") is True
    )


def _validate_target_isolation(record: dict[str, Any]) -> bool:
    return record.get("pass") is True and record.get("findings") == []


def _validate_proof(record: dict[str, Any]) -> bool:
    return (
        record.get("pass") is True
        and record.get("proof_contract_version") == 3
        and all(record.get("dependency_checks", {}).values())
    )


def _validate_controls(record: dict[str, Any]) -> bool:
    return (
        record.get("pass") is True
        and record.get("controls_executed_before_henon_static_audit") is True
        and record.get("candidate_parameter_substituted") is False
        and record.get("candidate_periodic_point_computed") is False
        and record.get("candidate_action_computed") is False
    )


def _validate_henon(record: dict[str, Any]) -> bool:
    required = {
        "henon_identity",
        "recurrence_multiplicity",
        "projective_infinity",
        "s_integral_denominator",
    }
    return required.issubset(record) and all(record[key].get("pass") is True for key in required)


def _validate_environment(record: dict[str, Any]) -> bool:
    try:
        date.fromisoformat(str(record.get("execution_date_utc")))
    except ValueError:
        return False
    return (
        str(record.get("execution_timestamp_utc", "")).endswith("Z")
        and record.get("network_access_by_executable") is False
        and record.get("external_prime_tables_accessed") is False
        and record.get("riemann_zero_data_accessed") is False
        and record.get("candidate_parameter_substituted") is False
        and record.get("candidate_periodic_points_computed") is False
        and record.get("candidate_actions_computed") is False
    )


def _validate_summary(record: dict[str, Any]) -> bool:
    return (
        record.get("status") == "PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION"
        and record.get("candidate_execution_gate") == "CLOSED"
        and record.get("candidate_parameter_substituted") is False
        and record.get("candidate_periodic_points_computed") is False
        and record.get("candidate_actions_computed") is False
    )


JSON_VALIDATORS: dict[str, Callable[[dict[str, Any]], bool]] = {
    "source_lock_validation.json": _validate_source_lock,
    "target_isolation_audit.json": _validate_target_isolation,
    "proof_audit.json": _validate_proof,
    "control_audit.json": _validate_controls,
    "henon_static_audit.json": _validate_henon,
    "command_environment_manifest.json": _validate_environment,
    "run_summary.json": _validate_summary,
}


def _validate_code_review(text: str) -> bool:
    verdicts = re.findall(r"^Verdict:\s*([A-Z_]+)\s*$", text, flags=re.MULTILINE)
    return bool(verdicts) and verdicts[-1] in {"PASS", "PASS_WITH_MINORS", "DEPLOYMENT_PASS"}


def _validate_validation_report(text: str) -> bool:
    return (
        text.lstrip().startswith("# Validation Report")
        and EXPECTED_LOCK_SHA256 in text
        and "PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION" in text
    )


def _validate_experiment_results(text: str) -> bool:
    return (
        text.lstrip().startswith("# Experiment Results")
        and "ALGEBRAIC_NORMALIZED_ACTION_CLOCK_REJECTED_BY_ALL_PERIOD_THEOREM" in text
        and "Candidate periodic points computed: **no**" in text
    )


def _validate_pytest_xml(path: Path) -> bool:
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
    return bool(suites) and all(
        int(suite.attrib.get("failures", "0")) == 0
        and int(suite.attrib.get("errors", "0")) == 0
        for suite in suites
    )


def validate_required_artifacts(project_root: Path) -> dict[str, Any]:
    """Validate existence and semantic closure before hashing artifacts."""

    root = project_root.resolve()
    existence: dict[str, bool] = {}
    semantics: dict[str, bool] = {}
    schema = _result_schema_audit(root)

    for name in REQUIRED_RESULT_JSON:
        path = root / "results" / name
        safe_file = path.is_file() and not path.is_symlink()
        existence[f"results/{name}"] = safe_file
        try:
            semantics[f"results/{name}"] = (
                JSON_VALIDATORS[name](_load_json(path)) if safe_file else False
            )
        except (OSError, ValueError, json.JSONDecodeError):
            semantics[f"results/{name}"] = False

    for name in REQUIRED_RESULT_REPORTS:
        path = root / "results" / name
        safe_file = path.is_file() and not path.is_symlink()
        existence[f"results/{name}"] = safe_file
        if not safe_file:
            semantics[f"results/{name}"] = False
        else:
            try:
                if name == "CODE_REVIEW.md":
                    semantics[f"results/{name}"] = _validate_code_review(path.read_text(encoding="utf-8"))
                elif name == "VALIDATION_REPORT.md":
                    semantics[f"results/{name}"] = _validate_validation_report(path.read_text(encoding="utf-8"))
                elif name == "EXPERIMENT_RESULTS.md":
                    semantics[f"results/{name}"] = _validate_experiment_results(path.read_text(encoding="utf-8"))
                else:
                    semantics[f"results/{name}"] = _validate_pytest_xml(path)
            except (OSError, ValueError, ET.ParseError):
                semantics[f"results/{name}"] = False

    for relative in REQUIRED_PROJECT_FILES:
        path = root / relative
        existence[relative] = path.is_file() and not path.is_symlink()

    selected_relative: set[str] = set()
    collection_error: str | None = None
    if schema["pass"] and all(existence.values()):
        try:
            selected = collect_manifest_inputs(root)
            selected_relative = {str(path.relative_to(root)) for path in selected}
        except (OSError, ValueError) as exc:
            collection_error = str(exc)
    required_in_manifest = REQUIRED_RESULT_PATHS | set(REQUIRED_PROJECT_FILES)
    closure = required_in_manifest.issubset(selected_relative)
    passed = (
        all(existence.values())
        and all(semantics.values())
        and schema["pass"]
        and closure
        and collection_error is None
    )
    return {
        "required_existence": existence,
        "semantic_checks": semantics,
        "exact_result_schema": schema,
        "required_paths_in_manifest_selection": closure,
        "manifest_collection_error": collection_error,
        "selected_file_count": len(selected_relative),
        "pass": passed,
    }
