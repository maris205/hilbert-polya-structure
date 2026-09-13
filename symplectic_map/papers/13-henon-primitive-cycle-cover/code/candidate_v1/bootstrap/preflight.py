"""Collect the immutable safe-only preflight record."""

from pathlib import Path

from .canonical import read_regular_bytes, sha256_bytes
from .constants import (
    CANDIDATE_ID,
    CLAIM_RELATIVE,
    RAW_RESULT_RELATIVE,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
    TERMINAL_RELATIVE,
    RUNTIME_RELATIVE,
)
from .launcher import SAFE_PROBE_EXPECTED_COUNTS, launch_safe_probe
from .static_audit import collect_static_audit


def collect_preflight(project_root: Path):
    static = collect_static_audit(project_root)
    q_probe = launch_safe_probe(project_root, "Q")
    r_probe = launch_safe_probe(project_root, "R")
    runtime_paths = (
        project_root / RUNTIME_RELATIVE,
        project_root / CLAIM_RELATIVE,
        project_root / TERMINAL_RELATIVE,
        project_root / RAW_RESULT_RELATIVE,
    )
    if any(path.exists() or path.is_symlink() for path in runtime_paths):
        raise RuntimeError("safe preflight found a runtime artifact")
    for probe in (q_probe, r_probe):
        if probe["response"]["access_counters"] != SAFE_PROBE_EXPECTED_COUNTS:
            raise RuntimeError("safe probe counter drift")
        diagnostic = probe["diagnostic"]
        if diagnostic["returncode"] != 0 or diagnostic["timed_out"]:
            raise RuntimeError("safe probe process disposition")
    return {
        "candidate_id": CANDIDATE_ID,
        "development_execution_boundary": {
            "development_helper_module_imported_by_unit_tests": True,
            "fixed_helper_unit_tests_are_nonofficial": True,
            "official_result_file_count": 0,
            "registered_audit_count": 0,
            "scientific_child_engine_load_count": 0,
            "top_level_run_science_call_count": 0,
        },
        "external_data_access_count": 0,
        "gpu_hour_count": 0,
        "network_access_count": 0,
        "random_seed_count": 0,
        "registered_audit_count": 0,
        "safe_runtime_probes": {
            "Q": q_probe,
            "R": r_probe,
        },
        "schema": "P13_SAFE_PREFLIGHT_V1",
        "source_bindings": {
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "source_review_sha256": SOURCE_REVIEW_SHA256,
        },
        "static_audit": static,
        "status": "SAFE_PREFLIGHT_FROZEN_FOR_INDEPENDENT_REVIEW",
    }
