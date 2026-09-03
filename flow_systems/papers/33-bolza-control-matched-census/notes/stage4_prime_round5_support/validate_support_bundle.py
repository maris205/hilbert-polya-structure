#!/usr/bin/env python3
"""Mechanical validation of the P33 Stage-4-prime notes-side support bundle."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def art(path: Path, root: Path) -> dict:
    return {"path": str(path.relative_to(root)), "sha256": sha(path), "bytes": len(path.read_bytes())}


def canonical(obj: object) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def main() -> int:
    support = Path(__file__).resolve().parent
    notes = support.parent
    root = Path(__file__).resolve().parents[4]
    checks = []

    def check(check_id: str, condition: bool, detail: object) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})

    fixed = {
        "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json": "ff160416cd8316326d2ef15b806f41479e63e299e0523899dbe93dc2e0da1650",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json": "7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf",
        "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json": "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff",
        "papers/33-bolza-control-matched-census/notes/stage4_revision_round1.tex": "8a4ea5ff994db83b91c2f14ca5a8425e6e2f954cbc7c87faf7edf27ec98b99d4",
        "papers/33-bolza-control-matched-census/notes/stage4_prime_round5_base.block-manifest.json": "69006ab2614eb3171527b19c7880e58eee198aa5c7576e91210b28d81e9a8262",
        "papers/33-bolza-control-matched-census/paper/references.bib": "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
        "papers/33-bolza-control-matched-census/paper/manuscript.tex": "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
        "papers/33-bolza-control-matched-census/paper/paper.pdf": "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031",
        "papers/33-bolza-control-matched-census/notes/stage1_prestart_brief.md": "b530d2f53f118d57c5281aff8eb3c367a48f85ae8ef2acdb1e73790b69139ea6",
        "papers/33-bolza-control-matched-census/notes/stage4_route_crosswalk.md": "0434982b38bf658bfd808469671431f089140850ceb2c01875539ef997f942cf",
    }
    for rel, expected in fixed.items():
        path = root / rel
        check(f"frozen_sha256:{rel}", path.exists() and sha(path) == expected, {"expected": expected, "actual": sha(path) if path.exists() else None})

    inv_path = notes / "stage4_prime_round5_artifact_inventory_final.json"
    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    check("artifact_inventory_status", inv["status"] == "PASS_EXACT_43_OF_43_AT_PINNED_COMMIT", inv["status"])
    check("artifact_inventory_rows", len(inv["artifacts"]) == 43, len(inv["artifacts"]))
    for row in inv["artifacts"]:
        local = root / row["path"]
        ok = (
            row["pinned_commit_membership_state"] == "EXACT_MATCH_AT_PINNED_COMMIT"
            and local.exists() and sha(local) == row["sha256"] == row["pinned_commit_sha256"]
            and len(local.read_bytes()) == row["bytes"] == row["pinned_commit_bytes"]
        )
        check(f"artifact_row:{row['path']}", ok, row["pinned_commit_membership_state"])

    source_path = notes / "stage4_prime_round5_source_use_locator_final.json"
    matrix = json.loads(source_path.read_text(encoding="utf-8"))
    rows = matrix["source_use_rows"]
    check("source_use_rows", len(rows) == 48, len(rows))
    check("source_use_ids_exact", [r["use_id"] for r in rows] == [f"P33-U{i:02d}" for i in range(1, 49)], [r["use_id"] for r in rows])
    check("source_count", len({r["source_id"] for r in rows}) == 20, len({r["source_id"] for r in rows}))
    check("explicit_bounded_unavailability", all(r["locator_disposition"] == "EXPLICIT_BOUNDED_UNAVAILABLE" for r in rows), sum(r["locator_disposition"] == "EXPLICIT_BOUNDED_UNAVAILABLE" for r in rows))
    check("passage_inconclusive", all(r["claim_to_passage"] == "INCONCLUSIVE" and r["anchor"] == "none" for r in rows), sum(r["claim_to_passage"] == "INCONCLUSIVE" for r in rows))
    check("five_dual_correction_bindings", sum(len(r["citation_keys_required"]) == 2 for r in rows) == 5, sum(len(r["citation_keys_required"]) == 2 for r in rows))

    oracle = json.loads((support / "fixture_oracle_manifest.json").read_text(encoding="utf-8"))
    receipt = json.loads((support / "serialized_fixture_validation_receipt.json").read_text(encoding="utf-8"))
    valid = sorted((support / "fixtures/valid").glob("*.json"))
    invalid = sorted((support / "fixtures/invalid").glob("*.json"))
    check("fixture_count_2_valid", len(valid) == 2, len(valid))
    check("fixture_count_12_invalid", len(invalid) == 12, len(invalid))
    check("fixture_bytes_canonical", all(p.read_bytes() == canonical(json.loads(p.read_bytes().decode("utf-8"))) for p in valid + invalid), len(valid) + len(invalid))
    check("fixture_receipt", receipt["status"] == "PASS_SYNTHETIC_CONFORMANCE_ONLY" and receipt["counts"] == {"valid_fixture_files": 2, "invalid_fixture_files": 12, "outcomes_matching_oracle": 14, "failures": 0}, receipt["counts"])
    check("oracle_independence_not_overclaimed", oracle["independence_state"] == "PROCEDURALLY_SEPARATE_FROM_ANY_PRODUCER_OUTPUT_BUT_NOT_INDEPENDENTLY_AUTHORED_BY_A_SECOND_HUMAN_OR_RUNTIME", oracle["independence_state"])

    provenance = json.loads((support / "component_build_provenance.json").read_text(encoding="utf-8"))
    check("production_components_unavailable", all(r["availability"] == "UNAVAILABLE_COMPONENT_NOT_IMPLEMENTED" and r["source_tree_sha256"] is None and r["build_environment_sha256"] is None and r["build_sha256"] is None for r in provenance["production_components"]), provenance["status"])
    for tool in provenance["synthetic_support_tools"]:
        p = root / tool["path"]
        check(f"support_tool_hash:{tool['path']}", p.exists() and sha(p) == tool["sha256"] and len(p.read_bytes()) == tool["bytes"], tool)
    exclusion = json.loads((support / "producer_code_exclusion_audit.json").read_text(encoding="utf-8"))
    check("independence_not_established", exclusion["independence_established"] is False, exclusion["status"])

    contract_receipt = json.loads((support / "producer_contract_validation_receipt.json").read_text(encoding="utf-8"))
    check("producer_contracts", contract_receipt["status"] == "PASS_CONTRACTS_ONLY_NO_PRODUCER_RUN" and all(contract_receipt["checks"].values()), contract_receipt["checks"])

    forbidden = [
        notes / "stage4_prime_revision_patch_round2.json",
        notes / "stage4_prime_revision_round2.tex",
        notes / "stage4_prime_revision_round2.tex.apply-report.json",
        notes / "stage4_prime_revision_round2.pdf",
        notes / "stage4_prime_revision_round2.build.log",
    ]
    check("scope_stop_no_patch_apply_build", all(not p.exists() for p in forbidden), [str(p.relative_to(root)) for p in forbidden if p.exists()])
    correction_prospect = json.loads((notes / "stage4_prime_round5_correction_bibliography_prospective.json").read_text(encoding="utf-8"))
    bib = (root / "papers/33-bolza-control-matched-census/paper/references.bib").read_text(encoding="utf-8")
    check("correction_entries_not_appended_at_scope_stop", all(f"{{{entry['key']}," not in bib for entry in correction_prospect["prospective_entries"]), [entry["key"] for entry in correction_prospect["prospective_entries"]])

    failures = [c for c in checks if c["status"] != "PASS"]
    artifacts = [
        inv_path,
        notes / "stage4_prime_round5_artifact_inventory_receipt.json",
        notes / "stage4_prime_round5_source_identity_replay_receipt.json",
        source_path,
        notes / "stage4_prime_round5_source_use_locator_receipt.json",
        support / "trust_graph.json",
        support / "fixture_oracle_manifest.json",
        support / "component_build_provenance.json",
        support / "producer_code_exclusion_audit.json",
        support / "synthetic_proof_registry_snapshot.json",
        support / "serialized_fixture_validation_receipt.json",
        support / "bp_enumeration_contract.json",
        support / "bp_coverage_ledger.schema.json",
        support / "cp_enumeration_contract.json",
        support / "cp_coverage_ledger.schema.json",
        support / "producer_contract_validation_receipt.json",
        notes / "stage4_prime_round5_scope_stop_incident.md",
    ] + valid + invalid
    output = {
        "schema_version": "p33-stage4-prime-round5-support-validation/1.0",
        "workflow_date": "2026-09-04",
        "paper_id": "P33",
        "status": "PASS_SUPPORT_COMPLETE_SCOPE_STOPPED_REQUEST_REISSUE_REQUIRED" if not failures else "FAIL_CLOSED",
        "checks_run": len(checks),
        "failure_count": len(failures),
        "checks": checks,
        "artifacts": [art(p, root) for p in artifacts],
        "counts": {
            "artifact_inventory_rows": 43,
            "source_use_rows": 48,
            "distinct_sources": 20,
            "passage_locators_verified": 0,
            "explicit_bounded_unavailability": 48,
            "valid_fixtures": 2,
            "invalid_fixtures": 12,
            "fixture_outcomes_matching": 14,
            "producer_contract_or_schema_files": 4,
            "production_components_available": 0,
        },
        "scope_stop": {"additional_targets_required": ["B0041/replace_block", "B0124/replace_block"], "patch_or_bib_or_build_performed": False},
    }
    out = notes / "stage4_prime_round5_support_validation.json"
    out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
