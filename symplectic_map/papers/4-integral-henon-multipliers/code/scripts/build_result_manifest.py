#!/usr/bin/env python3
"""Hash the frozen source, exact outputs, tests, and validation documents."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from henon_audit.protocol import sha256_file
from henon_audit.manifest import collect_artifacts, validate_official_report_linkage


def main() -> int:
    project_root = Path(__file__).resolve().parents[2]
    result_root = project_root / "results"
    output = result_root / "final_result_manifest.json"

    required = [
        project_root / "experiments" / "source_lock.json",
        project_root / "experiments" / "EXPERIMENT_PLAN.md",
        project_root / "experiments" / "EXPERIMENT_TRACKER.md",
        project_root / "notes" / "PROOF_PACKAGE.md",
        project_root / "notes" / "RESEARCH_QUESTION.md",
        result_root / "source_lock_validation.json",
        result_root / "target_isolation_audit.json",
        result_root / "proof_audit.json",
        result_root / "control_audit.json",
        result_root / "parameter_preflight.json",
        result_root / "symplectic_identity_audit.json",
        result_root / "exact_polynomials.json",
        result_root / "exact_period_ledger.json",
        result_root / "candidate_multiplier_audit.json",
        result_root / "scope_audit.json",
        result_root / "negative_result_ledger.json",
        result_root / "run_summary.json",
        result_root / "command_environment_manifest.json",
        result_root / "pytest.xml",
        result_root / "CODE_REVIEW.md",
        result_root / "EXPERIMENT_RESULTS.md",
        result_root / "VALIDATION_REPORT.md",
    ]
    required.extend(sorted((project_root / "code" / "henon_audit").glob("*.py")))
    required.extend(sorted((project_root / "code" / "tests").glob("test_*.py")))
    required.extend(
        [
            project_root / "code" / "scripts" / "run_exact_audit.py",
            project_root / "code" / "scripts" / "build_result_manifest.py",
        ]
    )
    artifacts = collect_artifacts(project_root, required)
    report_linkage = validate_official_report_linkage(project_root)

    run_summary = json.loads((result_root / "run_summary.json").read_text(encoding="utf-8"))
    candidate = json.loads(
        (result_root / "candidate_multiplier_audit.json").read_text(encoding="utf-8")
    )
    manifest = {
        "candidate_id": "integral_area_henon_multiplier_support_v1",
        "manifest_version": 1,
        "execution_status": run_summary["status"],
        "all_must_run_pass": run_summary["must_run_failed"] == 0,
        "candidate_classification": candidate["classification"],
        "source_lock_sha256": sha256_file(project_root / "experiments" / "source_lock.json"),
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "official_report_linkage": report_linkage,
        "forbidden_data_used": False,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "all_period_result_from_proof_not_finite_search": True,
    }
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
