#!/usr/bin/env python3
"""Certify that metadata additions leave all SD-C36 science bytes unchanged."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_CARD = ROOT / "evaluations" / "route_a" / "SD-C36" / "2026-08-15.yaml"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]
TARGET_ROOT_FIELDS = (
    "zero_error_train",
    "zero_error_validation",
    "zero_error_test",
    "extra_zero_count",
    "missing_zero_count",
    "root_count_discrepancy",
)
A2_STABILITY_FIELDS = (
    "cutoff_drift",
    "precision_drift",
    "control_margin",
)
RESEARCH_DOCUMENTS = (
    ("preregistration_sha256", "PREREGISTRATION.md"),
    ("source_lock_sha256", "SOURCE_LOCK.md"),
    ("derivation_package_sha256", "DERIVATION_PACKAGE.md"),
    ("proof_package_sha256", "PROOF_PACKAGE.md"),
    ("literature_audit_sha256", "LITERATURE_AUDIT.md"),
    ("experiment_plan_sha256", "experiments/EXPERIMENT_PLAN.md"),
)
REQUIRED_METADATA = (
    "EXPERIMENT_REPORT.md",
    "docs/EXPERIMENT_ARTIFACT_SCHEMA.md",
    "docs/candidate_registry.md",
    "docs/obstruction_registry.md",
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "experiments/IMPLEMENTATION_NOTES.md",
    "evaluations/route_a/SD-C36/2026-08-15.yaml",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    double = json.loads(
        (RESULTS / "double_run_certificate.json").read_text(encoding="utf-8")
    )
    cold = json.loads(
        (RESULTS / "cold_start_certificate.json").read_text(encoding="utf-8")
    )
    research = json.loads(
        (RESULTS / "research_lock.json").read_text(encoding="utf-8")
    )
    environment = json.loads(
        (RESULTS / "environment_lock.json").read_text(encoding="utf-8")
    )
    environment_lock_sha256 = digest(RESULTS / "environment_lock.json")
    environment_checks = {
        "schema_v2": environment.get("schema_version") == "P34-environment-v2",
        "scientific_dependencies_empty": environment.get("scientific_dependencies")
        == [],
        "seal_audit_dependencies_exact": environment.get(
            "seal_audit_dependencies"
        )
        == {"PyYAML": "6.0.2"}
        == {"PyYAML": yaml.__version__},
        "ambiguous_dependency_field_absent": "experiment_dependencies"
        not in environment,
        "PyYAML_role_scoped": environment.get("dependency_roles", {}).get(
            "PyYAML"
        )
        == "Route-A YAML sealing and integrity audit only",
    }
    research_lock_sha256 = digest(RESULTS / "research_lock.json")
    current_research_records = [
        {
            "path": relative,
            "pointer_field": field,
            "sha256": digest(ROOT / relative),
        }
        for field, relative in RESEARCH_DOCUMENTS
    ]
    research_checks = {
        "schema_v2": research.get("schema_version") == "SD-C36-research-lock-v2",
        "six_documents": research.get("research_document_count")
        == len(RESEARCH_DOCUMENTS)
        == 6,
        "document_ledger_exact": research.get("research_documents")
        == current_research_records,
        "named_pointers_match_current_files": all(
            research.get(record["pointer_field"]) == record["sha256"]
            for record in current_research_records
        ),
        "double_certificate_links_lock": double.get("research_lock_sha256")
        == research_lock_sha256,
        "cold_certificate_links_lock": cold.get("research_lock_sha256")
        == research_lock_sha256,
    }
    before = double["first_hashes"]
    after = {name: digest(RESULTS / name) for name in sorted(before)}
    missing_metadata = [name for name in REQUIRED_METADATA if not (ROOT / name).is_file()]
    route = yaml.safe_load(ROUTE_CARD.read_text(encoding="utf-8"))
    provenance = [
        route.get("source_commit"),
        route.get("code_commit"),
        route.get("source_lock", {}).get("code_commit"),
    ]
    a2_metrics = route.get("a2", {}).get("metrics", {})
    a4_metrics = route.get("a4", {}).get("metrics", {})
    target_values = [
        a2_metrics.get(name) for name in TARGET_ROOT_FIELDS
    ] + [
        a4_metrics.get(name) for name in TARGET_ROOT_FIELDS
    ]
    stability_values = [a2_metrics.get(name) for name in A2_STABILITY_FIELDS]
    route_checks = {
        "schema_v0_2": route.get("skill") == "route-a-evaluator"
        and route.get("skill_version") == "0.2.0",
        "candidate": route.get("candidate_id") == "SD-C36",
        "route_tuple": route.get("route_tuple") == ROUTE_TUPLE,
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_pending_provenance": provenance == [PENDING, PENDING, PENDING],
        "two_stage_note": "Two-stage provenance" in route.get("freeze_note", "")
        and PENDING in route.get("freeze_note", ""),
        "target_root_fields_scoped": all(
            isinstance(value, str) and value.startswith("not_applicable;")
            for value in target_values
        ),
        "a2_stability_fields_scoped": all(
            isinstance(value, str) and value.startswith("not_applicable;")
            for value in stability_values
        ),
    }
    metadata_hashes = {
        name: digest(ROOT / name) for name in REQUIRED_METADATA if (ROOT / name).is_file()
    }
    unchanged = before == after
    status = (
        "PASS"
        if unchanged
        and not missing_metadata
        and all(route_checks.values())
        and all(research_checks.values())
        and all(environment_checks.values())
        else "FAIL"
    )
    payload = {
        "schema_version": "SD-C36-metadata-seal-stability-v3",
        "scientific_artifact_count": len(before),
        "scientific_hashes_before_metadata": before,
        "scientific_hashes_after_metadata": after,
        "scientific_payload_byte_identical": unchanged,
        "metadata_paths": list(REQUIRED_METADATA),
        "metadata_hashes": metadata_hashes,
        "missing_metadata": missing_metadata,
        "environment_lock_sha256": environment_lock_sha256,
        "environment_lock_checks": environment_checks,
        "research_lock_sha256": research_lock_sha256,
        "research_lock_checks": research_checks,
        "route_checks": route_checks,
        "route_card_excluded_from_stage1_sha_for_future_paired_provenance_binding": True,
        "status": status,
    }
    write_json(RESULTS / "metadata_seal_stability.json", payload)
    inventory_path = RESULTS / "artifact_inventory.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    inventory["metadata_seal_pending"] = False
    inventory["metadata_seal_status"] = status
    write_json(inventory_path, inventory)
    if status != "PASS":
        raise SystemExit(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
