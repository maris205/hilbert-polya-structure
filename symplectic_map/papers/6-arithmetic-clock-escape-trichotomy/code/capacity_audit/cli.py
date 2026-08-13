"""Single registered exact/static audit, closed before independent review."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .controls import run_all_controls
from .ledger import audit_proof_ledger, audit_scope_ledger
from .protocol import (
    CANDIDATE_ID,
    EXPECTED_LOCK_SHA256,
    sha256_file,
    static_executable_isolation_scan,
    validate_source_lock,
)
from .review_gate import validate_review_authority
from .review_gate import reviewed_code_tree_sha256
from .scope import audit_escape_semantics, audit_output_scope
from .upstream import validate_upstream_bindings


def collect_registered_audit(project_root: Path) -> dict[str, Any]:
    """Collect every gate in fail-closed order without writing a result."""

    project_root = project_root.resolve()
    source_lock = validate_source_lock(project_root)
    review = validate_review_authority(project_root)
    proof = audit_proof_ledger(project_root)
    scope_ledger = audit_scope_ledger(project_root)
    controls = run_all_controls()
    isolation = static_executable_isolation_scan(project_root / "code")
    upstream = validate_upstream_bindings(project_root)
    escape = audit_escape_semantics(
        necessary=True,
        mutually_exclusive=False,
        exhaustive_for_all_dynamics=False,
        sufficient=False,
    )
    output_scope = audit_output_scope("CAPACITY_BOUND_CERTIFIED")

    gates = {
        "source_lock": source_lock,
        "independent_code_review": review,
        "proof_ledger": proof,
        "scope_ledger": scope_ledger,
        "exact_controls": controls,
        "executable_isolation": isolation,
        "upstream_bindings": upstream,
        "escape_semantics": escape,
        "output_scope": output_scope,
    }
    all_pass = all(record.get("pass") is True for record in gates.values())
    return {
        "schema": "CAPACITY_REGISTERED_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "registered_at_utc": datetime.now(timezone.utc).isoformat(),
        "audit_type": "EXACT_SYMBOLIC_AND_STATIC_ONLY",
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": reviewed_code_tree_sha256(project_root),
        "gates": gates,
        "external_prime_tables_accessed": False,
        "prime_target_arrays_generated": False,
        "riemann_zero_data_accessed": False,
        "candidate_numerical_runs": 0,
        "target_matches_computed": 0,
        "classification": "CAPACITY_BOUND_CERTIFIED" if all_pass else "REJECTED_OR_REQUIRES_AMENDMENT",
        "pass": all_pass,
    }


def run_registered_audit(project_root: Path) -> tuple[Path, Path]:
    """Run once and write official artifacts only after every gate passes."""

    project_root = project_root.resolve()
    results_directory = project_root / "results"
    output_path = results_directory / "EXPERIMENT_RESULTS.json"
    registry_path = results_directory / "registered_run.json"
    if output_path.exists() or registry_path.exists():
        raise FileExistsError("registered audit output or registry already exists")

    report = collect_registered_audit(project_root)
    if not report["pass"]:
        failed = [name for name, record in report["gates"].items() if record.get("pass") is not True]
        raise RuntimeError(f"registered audit gate failure: {failed}")

    results_directory.mkdir(parents=True, exist_ok=True)
    with output_path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    registry = {
        "schema": "CAPACITY_REGISTERED_RUN_REGISTRY_V1",
        "candidate_id": CANDIDATE_ID,
        "registered_at_utc": report["registered_at_utc"],
        "result_path": "results/EXPERIMENT_RESULTS.json",
        "result_sha256": sha256_file(output_path),
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": report["reviewed_code_sha256"],
        "registered_run_count": 1,
        "candidate_numerical_runs": 0,
    }
    with registry_path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(registry, indent=2, sort_keys=True) + "\n")
    return output_path, registry_path


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    output_path, registry_path = run_registered_audit(project_root)
    print(json.dumps({"result": str(output_path), "registry": str(registry_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
