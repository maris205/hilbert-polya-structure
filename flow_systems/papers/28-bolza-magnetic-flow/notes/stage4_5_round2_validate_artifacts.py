#!/usr/bin/env python3
"""Replay-validate the Paper-28 Stage-4.5 Round-2 artifact package.

Official ARS builders/validators remain authoritative for their closed
contracts.  This script adds only paper-local binding and tuple checks.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path

import jsonschema


PAPER = Path(__file__).resolve().parents[1]
ROOT = PAPER.parents[1]
NOTES = PAPER / "notes"
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str):
    return json.loads((NOTES / name).read_text(encoding="utf-8"))


def run(command: list[str]) -> dict[str, object]:
    result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    if result.returncode != 0:
        raise AssertionError(f"official validator failed: {' '.join(command)}\n{result.stdout}")
    return {"command": " ".join(command), "exit_code": result.returncode, "output": result.stdout.strip()}


required = [
    "stage4_5_round2_input_manifest.json",
    "stage4_5_round2_reference_source_snapshot.json",
    "stage4_5_round2_reference_citation_audit.md",
    "stage4_5_round2_phase_c_internal_consistency_audit.md",
    "stage4_5_round2_originality_failure_mode_audit.md",
    "stage4_5_round2_originality_failure_mode_audit.json",
    "stage4_5_round2_claim_registry.json",
    "stage4_5_round2_claim_registry_coverage.json",
    "stage4_5_round2_evidence_source_map.json",
    "stage4_5_round2_evidence_tuple_audit.json",
    "stage4_5_round2_evidence_rows.json",
    "stage4_5_round2_claim_strength_drift_findings.json",
    "stage4_5_round2_e6_semantic_audit.md",
    "stage4_5_round2_compliance_report.json",
    "stage4_5_round2_integrity_report.json",
    "stage4_5_round2_final_integrity_report.md",
    "stage4_5_round2_material_passport.json",
    "stage4_5_round2_preview_build_receipt.json",
]
assert all((NOTES / name).is_file() for name in required)

manifest = load("stage4_5_round2_input_manifest.json")
draft = PAPER / manifest["audit_target"]["path"]
bib = PAPER / manifest["bibliography"]["path"]
assert sha256(draft) == manifest["audit_target"]["sha256"] == "126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e"
assert sha256(bib) == manifest["bibliography"]["sha256"] == "95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e"
assert sha256(ROOT / "BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json") == manifest["batch_input_lock"]["sha256"] == "bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30"
assert sha256(NOTES / "stage4_prime_revision_evidence_bundle.json") == manifest["e6_dispatch_authority"]["sha256"] == "2c3d46b8d4282a2b1ec7b00d6a5dba743cf25e6d3cc2bdb7b1b6ea445ef3570e"
for rel, record in manifest["canonical_frozen"].items():
    assert sha256(PAPER / rel) == record["sha256"]

snapshot = load("stage4_5_round2_reference_source_snapshot.json")
assert snapshot["coverage"] == {"bibliography_entries": 6, "checked": 6, "rate": 1.0}
assert len(snapshot["records"]) == 6
s2_keys = {
    "status", "queried_at", "verification_method", "match_score", "semantic_scholar_id",
    "s2_title", "s2_authors", "s2_year", "s2_venue", "doi_crosscheck",
}
for record in snapshot["records"]:
    assert set(record["semantic_scholar"]) == s2_keys
    assert record["semantic_scholar"]["status"] in {"S2_VERIFIED", "S2_NOT_FOUND", "S2_API_UNAVAILABLE"}
    if record["semantic_scholar"]["status"] == "S2_VERIFIED":
        assert record["semantic_scholar"]["verification_method"] in {"s2_doi_lookup", "s2_title_search"}
    else:
        method = record["semantic_scholar"]["verification_method"]
        assert method is None or "unavailable" in method
    assert record["fresh_query"] and record["query_url"].startswith("https://www.bing.com/search?q=")
    assert record["result"] and record["status"] in {"VERIFIED", "VERIFIED_WITH_UPDATE_NOTE"}
    assert record["post_publication_update_check"]["observation"]

draft_text = draft.read_text(encoding="utf-8")
citations = re.findall(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", draft_text)
assert len(citations) == 9
assert set(x for keys in citations for x in keys.split(",")) == {row["ref_slug"] for row in snapshot["records"]}

phase_c = load("stage4_5_round2_phase_c_internal_consistency_audit.json")
c_cov = phase_c["registered_data_stat_table_experiment_surface_coverage"]
assert c_cov["experiment_claims_checked"] == c_cov["experiment_claims_verified"] == 14
assert c_cov["protected_surfaces_checked"] == c_cov["protected_surfaces_byte_exact_once"] == 14
assert c_cov["coverage_rate"] == 1.0
assert phase_c["experiment_intake"]["boundary"] == "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
assert phase_c["execution_replay"]["unit_tests"] == 108
assert phase_c["execution_replay"]["canonical_results_refreshed"] is False

originality = load("stage4_5_round2_originality_failure_mode_audit.json")
assert originality["denominator"] == 77
assert originality["successful_search_count"] == 44
assert originality["sampling_rate"] >= 0.5
assert originality["changed_total"] == originality["changed_successful"] == 5
assert len(originality["major_sections_represented"]) == 10
assert set(originality["seven_failure_modes"]) == {
    "implementation bug passing AI self-review", "hallucinated citation", "hallucinated experimental result",
    "shortcut reliance", "implementation bug reframed as novel insight", "methodology fabrication",
    "frame-lock at early pipeline stage",
}
assert originality["audit_mode"] == 2 and originality["audit_date"] == "2026-08-31"
for sample in originality["samples"]:
    assert sample["dual_lane_success"] is True
    assert 8 <= sample["word_count"] <= 12
    assert {track["lane"] for track in sample["searches"]} == {"quoted_exact", "unquoted_supplementary"}
    assert all(track["transport_status"] == "success" and track["http_status"] == 200 and track["top_result_summary"] for track in sample["searches"])

registry = load("stage4_5_round2_claim_registry.json")
coverage = load("stage4_5_round2_claim_registry_coverage.json")
draft_raw = draft.read_bytes()
assert registry["draft_raw_sha256"] == sha256(draft)
assert len(registry["claims"]) == 95
assert coverage["registry_claim_count"] == 95 and coverage["candidate_unregistered_count"] == 0
for claim in registry["claims"]:
    assert claim["selection_tier"] == "ALL"
    assert "P28LocalArtifactChain" in claim["ref_slugs"]
    span = claim["draft_span"]
    assert draft_raw[span["start_byte"] : span["end_byte"]].decode("utf-8") == claim["claim_text"]

rows = load("stage4_5_round2_evidence_rows.json")
source_map = load("stage4_5_round2_evidence_source_map.json")
tuple_audit = load("stage4_5_round2_evidence_tuple_audit.json")
assert source_map and all(isinstance(slug, str) and isinstance(source_text, str) and source_text for slug, source_text in source_map.items())
assert set(source_map) == {"P28LocalArtifactChain", "Nazarenko2013", "Takeuchi1975", "AigonDupuyEtAl2005", "Voight2009", "DespreEtAl2023", "Popescu2024"}
assert tuple_audit["tuple_accounting"] == {
    "registry_claims": 95,
    "external_ref_tuples": 9,
    "expected": 104,
    "actual": 104,
    "missing": 0,
    "anchorless": 0,
    "agent_extracted": 104,
}
assert len(rows) == 104
row_by_claim_slug = {(row["claim"]["claim_id"], row["source"]["ref_slug"]): row for row in rows}
assert len(row_by_claim_slug) == len(rows)
for claim in registry["claims"]:
    for slug in claim["ref_slugs"]:
        assert (claim["claim_id"], slug) in row_by_claim_slug
assert all(row["source"]["ref_slug"] is not None for row in rows)
assert all(row["excerpt"]["state"] == "agent_extracted" for row in rows)
assert all(row["anchor"]["kind"] != "none" for row in rows)
assert sum(len(claim["ref_slugs"]) for claim in registry["claims"]) == len(rows) == 104

drift = load("stage4_5_round2_claim_strength_drift_findings.json")
assert drift["status"] == "completed" and drift["findings"] == []
assert drift["final_draft_sha256"] == manifest["audit_target"]["sha256"]
assert drift["revision_evidence_bundle_sha256"] == manifest["e6_dispatch_authority"]["sha256"]

integrity = load("stage4_5_round2_integrity_report.json")
required_top = {"verdict", "mode", "phases", "overall_issues", "citation_integrity_score", "fabrication_risk_score", "timestamp"}
assert required_top <= set(integrity) <= required_top | {"extensions"}
assert integrity["verdict"] in {"PASS", "PASS_WITH_CONDITIONS", "FAIL"} and integrity["verdict"] == "PASS"
assert integrity["mode"] in {"pre-review", "final-check"} and integrity["mode"] == "final-check"
assert integrity["overall_issues"] == {"SERIOUS": 0, "MEDIUM": 0, "MINOR": 0}
assert set(integrity["phases"]) == {"A_references", "B_citation_context", "C_data", "D_originality", "E_claims"}
assert set(integrity["phases"]["A_references"]) == {"checked", "passed", "failed", "issues"}
assert set(integrity["phases"]["B_citation_context"]) == {"sampled", "verified", "issues"}
assert integrity["phases"]["C_data"] == {"claims_checked": 14, "verified": 14, "issues": []}
assert integrity["phases"]["D_originality"] == {"checked": True, "issues": []}
e_claims = integrity["phases"]["E_claims"]
assert set(e_claims) == {"checked", "verified", "distortions", "claim_registry_coverage", "evidence_rows", "claim_strength_drift_findings"}
assert e_claims["checked"] == e_claims["verified"] == 95 and e_claims["distortions"] == []
assert e_claims["evidence_rows"] == rows and len(e_claims["evidence_rows"]) == 104
coverage_pointer = e_claims["claim_registry_coverage"]
assert set(coverage_pointer) == {"status", "registry_schema_version", "report_path", "report_sha256", "draft_raw_sha256", "registry_raw_sha256", "candidate_unregistered_count", "semantic_extraction_coverage"}
assert coverage_pointer["status"] == "completed" and coverage_pointer["registry_schema_version"] == "claim-registry/1.0"
assert coverage_pointer["report_sha256"] == sha256(NOTES / coverage_pointer["report_path"].removeprefix("notes/"))
assert coverage_pointer["draft_raw_sha256"] == sha256(draft)
assert coverage_pointer["registry_raw_sha256"] == sha256(NOTES / "stage4_5_round2_claim_registry.json")
assert coverage_pointer["candidate_unregistered_count"] == 0
assert coverage_pointer["semantic_extraction_coverage"] == "not_machine_detectable"
drift_pointer = e_claims["claim_strength_drift_findings"]
assert set(drift_pointer) == {"schema_version", "artifact_path", "artifact_sha256"}
assert drift_pointer["schema_version"] == "claim-strength-drift-findings/1.0"
assert drift_pointer["artifact_sha256"] == sha256(NOTES / drift_pointer["artifact_path"].removeprefix("notes/"))
assert integrity["extensions"]["audit_mode"] == 2 and integrity["extensions"]["audit_date"] == "2026-08-31"
assert set(integrity["extensions"]["failure_modes"]) == set(originality["seven_failure_modes"])

preview = load("stage4_5_round2_preview_build_receipt.json")
assert preview["status"] == "PASS" and preview["canonical_unchanged"] is True
assert preview["preview"]["pages"] == 14
assert sha256(NOTES / "stage4_5_round2_preview.pdf") == preview["preview"]["sha256"]

final_text = (NOTES / "stage4_5_round2_final_integrity_report.md").read_text(encoding="utf-8")
for phrase in (
    "Stage 5 has not started and is awaiting mandatory author confirmation",
    "A2=0/5",
    "Route B invocations=0/5",
    "19 instances are not independent samples",
    "does not constitute Route promotion",
    "none detected by the recorded semantic review",
):
    assert phrase in final_text

official_commands = [
    run([
        "python3", str(ARS / "scripts/claim_registry_coverage.py"),
        "--draft", str(draft), "--registry", str(NOTES / "stage4_5_round2_claim_registry.json"),
        "--validate-report", str(NOTES / "stage4_5_round2_claim_registry_coverage.json"),
    ]),
    run([
        "python3", str(ARS / "scripts/evidence_rows.py"), "validate",
        str(NOTES / "stage4_5_round2_evidence_rows.json"),
        "--source-map", str(NOTES / "stage4_5_round2_evidence_source_map.json"),
    ]),
    run([
        "python3", str(ARS / "scripts/evidence_rows.py"), "validate",
        str(NOTES / "stage4_5_round2_integrity_report.json"),
        "--source-map", str(NOTES / "stage4_5_round2_evidence_source_map.json"),
    ]),
    run([
        "python3", str(ARS / "scripts/revision_roadmap.py"), "validate-bundle",
        str(NOTES / "stage4_prime_revision_evidence_bundle.json"), "--root", str(PAPER),
    ]),
    run([
        "python3", str(ARS / "scripts/check_compliance_report.py"),
        str(NOTES / "stage4_5_round2_compliance_report.json"),
    ]),
]

for artifact_name, schema_name in (
    ("stage4_5_round2_claim_registry.json", "shared/contracts/evidence/claim_registry.schema.json"),
    ("stage4_5_round2_claim_registry_coverage.json", "shared/contracts/evidence/claim_registry_coverage_report.schema.json"),
    ("stage4_5_round2_claim_strength_drift_findings.json", "shared/contracts/revision/claim_strength_drift_findings.schema.json"),
    ("stage4_5_round2_revision_evidence_bundle.json", "shared/contracts/revision/revision_evidence_bundle.schema.json"),
):
    schema = json.loads((ARS / schema_name).read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(load(artifact_name))

receipt = {
    "schema": "p28-stage4.5-round2-validation-receipt/1.0",
    "validated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    "status": "PASS",
    "official_commands": official_commands,
    "cross_artifact_checks": {
        "input_hashes": "PASS",
        "canonical_unchanged": "PASS",
        "references": "6/6",
        "citation_contexts": "9/9",
        "phase_c": "14/14 claims; 14/14 protected surfaces; 100% registered surface coverage",
        "originality": "44/77 dual-lane; 5/5 changed",
        "claim_registry": "95 ALL; 0 uncovered mechanical candidates",
        "evidence_rows": "104/104; 0 anchorless; 104 agent_extracted",
        "integrity_schema_5": "PASS; closed phase shapes; 104 embedded evidence rows; replayed coverage and drift pointers",
        "e6_findings": "0",
        "preview": "14-page PASS",
        "stage5_started": False,
    },
}
(NOTES / "stage4_5_round2_validation_receipt.json").write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
output_manifest_path = NOTES / "stage4_5_round2_output_manifest.json"
output_manifest = load("stage4_5_round2_output_manifest.json")
output_manifest["artifacts"] = [
    {
        "path": f"notes/{path.name}",
        "sha256": sha256(path),
        "size_bytes": path.stat().st_size,
    }
    for path in sorted(NOTES.glob("stage4_5_round2_*"))
    if path.is_file() and path != output_manifest_path
]
output_manifest["validation_receipt"] = {
    "path": "notes/stage4_5_round2_validation_receipt.json",
    "sha256": sha256(NOTES / "stage4_5_round2_validation_receipt.json"),
}
output_manifest_path.write_text(
    json.dumps(output_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(receipt["cross_artifact_checks"], sort_keys=True))
