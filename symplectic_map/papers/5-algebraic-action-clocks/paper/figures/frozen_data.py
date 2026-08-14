"""Read-only adapter for the source-locked Paper 4 static outputs.

Every scientific status shown in a figure passes through this module.  It
rejects an incomplete package, a changed source lock, or any indication that
the forbidden candidate-execution gate opened.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


FIGURE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = FIGURE_DIR.parents[1]
RESULTS_DIR = PROJECT_DIR / "results"
EXPERIMENTS_DIR = PROJECT_DIR / "experiments"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def load_frozen_package() -> dict[str, Any]:
    paths = {
        "source_lock": EXPERIMENTS_DIR / "source_lock.json",
        "source_lock_validation": RESULTS_DIR / "source_lock_validation.json",
        "proof": RESULTS_DIR / "proof_audit.json",
        "control": RESULTS_DIR / "control_audit.json",
        "henon": RESULTS_DIR / "henon_static_audit.json",
        "summary": RESULTS_DIR / "run_summary.json",
        "environment": RESULTS_DIR / "command_environment_manifest.json",
        "isolation": RESULTS_DIR / "target_isolation_audit.json",
    }
    data = {key: _load(path) for key, path in paths.items()}
    summary = data["summary"]
    validation = data["source_lock_validation"]
    zero_execution = (
        summary.get("candidate_execution_gate") == "CLOSED"
        and summary.get("candidate_parameter_substituted") is False
        and summary.get("candidate_periodic_points_computed") is False
        and summary.get("candidate_actions_computed") is False
    )
    if summary.get("status") != "PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION":
        raise RuntimeError("refusing to plot an incomplete official static audit")
    if not zero_execution:
        raise RuntimeError("refusing to plot after forbidden candidate execution")
    if summary.get("external_prime_tables_accessed") is not False:
        raise RuntimeError("external prime-table isolation changed")
    if summary.get("riemann_zero_data_accessed") is not False:
        raise RuntimeError("zero-data isolation changed")
    if summary.get("controls_executed_before_henon_static_audit") is not True:
        raise RuntimeError("controls-first order changed")
    if data["proof"].get("pass") is not True or data["control"].get("pass") is not True:
        raise RuntimeError("proof or control audit is not PASS")
    if validation.get("sha256") != sha256(paths["source_lock"]):
        raise RuntimeError("source-lock hash changed after the official audit")
    if validation.get("pass") is not True or data["isolation"].get("pass") is not True:
        raise RuntimeError("source-lock or isolation audit is not PASS")
    registry = summary.get("run_registry", [])
    if len(registry) != 8 or any(item.get("status") != "PASS" for item in registry):
        raise RuntimeError("official eight-stage registry is not closed")

    data["paths"] = {
        key: str(path.relative_to(PROJECT_DIR)) for key, path in paths.items()
    }
    data["hashes"] = {key: sha256(path) for key, path in paths.items()}
    return data
