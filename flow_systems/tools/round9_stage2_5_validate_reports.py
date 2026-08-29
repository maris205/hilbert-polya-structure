#!/usr/bin/env python3
"""Read-only validation for Round-9 Stage-2.5 audit artifacts."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent.parent


def resolve_ars() -> Path:
    override = os.environ.get("ARS_CODEX_ROOT")
    if override:
        path = Path(override).expanduser().resolve()
        if (path / "scripts" / "evidence_rows.py").is_file():
            return path
        raise RuntimeError(f"ARS_CODEX_ROOT is not an ARS resource root: {path}")
    search_roots = [ROOT.parent / ".codex", Path.home() / ".codex"]
    candidates = []
    for codex_root in search_roots:
        candidates.extend(
            (codex_root / "plugins" / "cache" / "ars-codex" / "ars-codex").glob(
                "*/skills/academic-research-suite/ars"
            )
        )
    candidates = sorted(set(candidates))
    if not candidates:
        raise RuntimeError("ARS-Codex academic-research-suite resources not found")
    return candidates[-1]


ARS = resolve_ars()
PAPERS = [
    "24-bianchi-holonomy-flow",
    "25-three-disk-scattering-flow",
    "26-level11-newform-time-change",
    "27-congruence-inverse-limit-no-go",
    "28-bolza-magnetic-flow",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def scholar_intake_is_valid(passport: dict) -> bool:
    declaration = passport.get("experiment_intake_declaration")
    if not isinstance(declaration, dict):
        return False
    confirmation = (
        declaration.get("confirmation_time")
        or declaration.get("confirmed_at")
        or declaration.get("declared_at")
    )
    basic = (
        declaration.get("status") == "experiments_declared"
        and declaration.get("declared_by") == "scholar"
        and isinstance(confirmation, str)
        and bool(confirmation.strip())
        and isinstance(passport.get("experiment_provenance"), list)
        and bool(passport["experiment_provenance"])
        and isinstance(passport.get("experiment_alignment_results"), list)
        and bool(passport["experiment_alignment_results"])
        and isinstance(passport.get("claim_intent_manifests"), list)
        and bool(passport["claim_intent_manifests"])
    )
    if not basic:
        return False
    contracts = ARS / "shared" / "contracts" / "passport"
    provenance_schema = load(contracts / "experiment_provenance_entry.schema.json")
    alignment_schema = load(contracts / "experiment_alignment_result.schema.json")
    manifest_schema = load(contracts / "claim_intent_manifest.schema.json")
    try:
        for entry in passport["experiment_provenance"]:
            jsonschema.Draft202012Validator(provenance_schema).validate(entry)
        for entry in passport["experiment_alignment_results"]:
            jsonschema.Draft202012Validator(
                alignment_schema, format_checker=jsonschema.FormatChecker()
            ).validate(entry)
        for entry in passport["claim_intent_manifests"]:
            jsonschema.Draft202012Validator(
                manifest_schema, format_checker=jsonschema.FormatChecker()
            ).validate(entry)
    except jsonschema.ValidationError:
        return False
    experiment_ids = [entry["experiment_id"] for entry in passport["experiment_provenance"]]
    if len(experiment_ids) != len(set(experiment_ids)):
        return False
    experiment_id_set = set(experiment_ids)
    manifest_claims = {}
    for manifest in passport["claim_intent_manifests"]:
        for claim in manifest["claims"]:
            key = (manifest["manifest_id"], claim["claim_id"])
            if key in manifest_claims:
                return False
            manifest_claims[key] = claim
            planned = claim.get("planned_experiment_ids", [])
            if any(exp_id not in experiment_id_set for exp_id in planned):
                return False
            if planned and claim["intended_evidence_kind"] != "empirical":
                return False
    alignment_pairs = []
    finding_ids = []
    for row in passport["experiment_alignment_results"]:
        key = (row["scoped_manifest_id"], row["claim_id"])
        claim = manifest_claims.get(key)
        if (
            claim is None
            or row["experiment_id"] not in claim.get("planned_experiment_ids", [])
            or row["alignment_verdict"] != "ALIGNED"
        ):
            return False
        alignment_pairs.append((key, row["experiment_id"]))
        finding_ids.append(row["finding_id"])
    expected_pairs = {
        (key, exp_id)
        for key, claim in manifest_claims.items()
        for exp_id in claim.get("planned_experiment_ids", [])
    }
    if (
        len(finding_ids) != len(set(finding_ids))
        or len(alignment_pairs) != len(set(alignment_pairs))
        or set(alignment_pairs) != expected_pairs
    ):
        return False
    if any(
        not any(unit["executed"] for unit in entry["planned_vs_executed"])
        for entry in passport["experiment_provenance"]
    ):
        return False
    return True


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    freeze = load(ROOT / "BATCH_ROUND9_STAGE2_5_INPUT_FREEZE.json")
    frozen = {row["paper"]: row for row in freeze["papers"]}
    claim_schema = load(ARS / "shared/contracts/evidence/claim_registry.schema.json")
    drift_schema = load(
        ARS / "shared/contracts/revision/claim_strength_drift_findings.schema.json"
    )
    compliance_schema = load(ARS / "shared/compliance_report.schema.json")
    evidence = load_module(ARS / "scripts/evidence_rows.py", "round9_validate_evidence_rows")
    coverage_script = ARS / "scripts/claim_registry_coverage.py"

    aggregate = {
        "papers": 0,
        "frozen_files": 0,
        "registered": 0,
        "selected": 0,
        "tuples": 0,
        "anchorless": 0,
        "semantic_files": 0,
    }
    results = []
    report_passes = 0
    paper_pass_state = {}
    for paper in PAPERS:
        base = ROOT / "papers" / paper
        notes = base / "notes"
        fr = frozen[paper]
        actual_freeze = {
            "manuscript_sha256": sha(base / "paper/manuscript.tex"),
            "bibliography_sha256": sha(base / "paper/references.bib"),
            "pdf_sha256": sha(base / "paper/paper.pdf"),
        }
        for key, value in actual_freeze.items():
            if value != fr[key]:
                raise RuntimeError(f"{paper}: frozen {key} mismatch")
        aggregate["frozen_files"] += 3

        registry_path = notes / "stage2_5_claim_registry.json"
        coverage_path = notes / "stage2_5_claim_registry_coverage.json"
        rows_path = notes / "stage2_5_evidence_rows.json"
        drift_path = notes / "stage2_5_claim_strength_drift_findings.json"
        report_path = notes / "stage2_5_integrity_report.json"
        passport_path = notes / "stage2_5_material_passport.json"
        compliance_path = notes / "stage2_5_compliance_report.json"
        semantic_path = notes / "stage2_5_phase_e_semantic_audit.md"
        semantic_receipt_path = notes / "stage2_5_phase_e_semantic_verdicts.json"

        registry = load(registry_path)
        jsonschema.Draft202012Validator(claim_schema).validate(registry)
        selected = [c for c in registry["claims"] if c["selection_tier"] != "NOT-SELECTED"]
        expected = {
            (c["claim_id"], ref)
            for c in selected
            for ref in (c["ref_slugs"] or [None])
        }
        rows = load(rows_path)
        validated_rows = [evidence.validate(row) for row in rows]
        actual_projection = [
            (row["claim"]["claim_id"], row["source"]["ref_slug"])
            for row in validated_rows
        ]
        if len(actual_projection) != len(expected) or set(actual_projection) != expected:
            raise RuntimeError(f"{paper}: evidence tuple set mismatch")
        if any(row["excerpt"]["state"] != "anchorless" for row in validated_rows):
            raise RuntimeError(f"{paper}: unexpected non-anchorless row")
        selected_by_id = {claim["claim_id"]: claim for claim in selected}
        for row in validated_rows:
            claim = selected_by_id[row["claim"]["claim_id"]]
            expected_claim_object = {
                "claim_id": claim["claim_id"],
                "paper_locator": claim["writer_anchors"][0],
                "selection_tier": claim["selection_tier"],
                "text": claim["claim_text"],
            }
            if row["claim"] != expected_claim_object:
                raise RuntimeError(f"{paper}: evidence claim-object mismatch")

        subprocess.run(
            [
                sys.executable,
                str(coverage_script),
                "--draft",
                str(base / "paper/manuscript.tex"),
                "--registry",
                str(registry_path),
                "--validate-report",
                str(coverage_path),
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        coverage = load(coverage_path)
        if coverage["candidate_unregistered_count"] != 0:
            raise RuntimeError(f"{paper}: unresolved coverage candidate")

        drift = load(drift_path)
        jsonschema.Draft202012Validator(drift_schema).validate(drift)
        if drift["status"] != "skipped_no_revision_evidence" or drift["findings"]:
            raise RuntimeError(f"{paper}: invalid first-pass drift state")

        semantic_receipt = load(semantic_receipt_path)
        if semantic_receipt.get("schema") != (
            "flow-systems-stage2.5-semantic-verdict-receipt/1.0"
        ):
            raise RuntimeError(f"{paper}: semantic receipt schema mismatch")
        if semantic_receipt.get("decision") != "PASS_SELECTED_POPULATION":
            raise RuntimeError(f"{paper}: semantic receipt is not PASS")
        expected_semantic_bindings = {
            "manuscript_sha256": sha(base / "paper/manuscript.tex"),
            "claim_registry_sha256": sha(registry_path),
            "evidence_rows_sha256": sha(rows_path),
            "semantic_audit_sha256": sha(semantic_path),
        }
        if semantic_receipt.get("bindings") != expected_semantic_bindings:
            raise RuntimeError(f"{paper}: stale semantic receipt bindings")
        claim_verdicts = semantic_receipt.get("claim_verdicts", [])
        verdict_by_id = {row.get("claim_id"): row for row in claim_verdicts}
        if (
            len(verdict_by_id) != len(claim_verdicts)
            or set(verdict_by_id) != set(selected_by_id)
        ):
            raise RuntimeError(f"{paper}: semantic claim population mismatch")
        grouped_rows = {}
        for row in validated_rows:
            grouped_rows.setdefault(row["claim"]["claim_id"], []).append(row)
        for claim_id, verdict in verdict_by_id.items():
            claim_rows = grouped_rows[claim_id]
            if verdict.get("verdict") != "VERIFIED":
                raise RuntimeError(f"{paper}: non-VERIFIED semantic verdict")
            if any(row["verdict"] != verdict["verdict"] for row in claim_rows):
                raise RuntimeError(f"{paper}: tuple verdict inconsistency for {claim_id}")
            if verdict.get("tuple_count") != len(claim_rows):
                raise RuntimeError(f"{paper}: semantic tuple count mismatch for {claim_id}")
            if verdict.get("row_ids") != [row["row_id"] for row in claim_rows]:
                raise RuntimeError(f"{paper}: semantic row-id mismatch for {claim_id}")
            if verdict.get("row_sha256s") != [row["row_sha256"] for row in claim_rows]:
                raise RuntimeError(f"{paper}: semantic row-hash mismatch for {claim_id}")
            if verdict.get("claim_object_sha256") != canonical_sha(claim_rows[0]["claim"]):
                raise RuntimeError(f"{paper}: semantic claim-object hash mismatch")
        if semantic_receipt.get("verdict_counts") != {
            "VERIFIED": len(selected),
            "MINOR_DISTORTION": 0,
            "MAJOR_DISTORTION": 0,
            "UNVERIFIABLE": 0,
            "UNVERIFIABLE_ACCESS": 0,
        }:
            raise RuntimeError(f"{paper}: semantic verdict totals mismatch")

        report = load(report_path)
        for key in (
            "verdict",
            "mode",
            "phases",
            "overall_issues",
            "citation_integrity_score",
            "fabrication_risk_score",
            "timestamp",
        ):
            if key not in report:
                raise RuntimeError(f"{paper}: report missing {key}")
        if report["verdict"] not in {"PASS", "FAIL"} or report["mode"] != "pre-review":
            raise RuntimeError(f"{paper}: wrong report gate")
        phase_e = report["phases"]["E_claims"]
        if phase_e["checked"] != len(selected) or phase_e["verified"] != len(selected):
            raise RuntimeError(f"{paper}: report distinct-claim count mismatch")
        if phase_e["evidence_rows"] != rows:
            raise RuntimeError(f"{paper}: embedded evidence rows differ from sidecar")
        semantic_pointer = phase_e.get("semantic_verdict_receipt", {})
        if semantic_pointer.get("artifact_sha256") != sha(semantic_receipt_path):
            raise RuntimeError(f"{paper}: stale semantic receipt pointer")
        if semantic_pointer.get("semantic_audit_sha256") != sha(semantic_path):
            raise RuntimeError(f"{paper}: stale semantic audit pointer")
        if phase_e["claim_registry_coverage"]["report_sha256"] != sha(coverage_path):
            raise RuntimeError(f"{paper}: stale coverage report pointer")
        if phase_e["claim_registry_coverage"]["registry_raw_sha256"] != sha(registry_path):
            raise RuntimeError(f"{paper}: stale registry pointer")
        if phase_e["claim_strength_drift_findings"]["artifact_sha256"] != sha(drift_path):
            raise RuntimeError(f"{paper}: stale drift pointer")
        if report["extensions"]["input_freeze"] != actual_freeze:
            raise RuntimeError(f"{paper}: report freeze extension mismatch")

        compliance = load(compliance_path)
        jsonschema.Draft202012Validator(
            compliance_schema,
            format_checker=jsonschema.FormatChecker(),
        ).validate(compliance)
        passport = load(passport_path)
        intake_valid = scholar_intake_is_valid(passport)
        partial_intake = (
            "experiment_intake_declaration" in passport
            or bool(passport.get("experiment_provenance"))
            or bool(passport.get("experiment_alignment_results"))
            or bool(passport.get("claim_intent_manifests"))
        )
        if partial_intake and not intake_valid:
            raise RuntimeError(f"{paper}: partial or invalid scholar intake state")
        c4 = report["phases"].get("C4_experiment_intake", {})
        if c4.get("claims_checked") != 1 or c4.get("verified") != int(intake_valid):
            raise RuntimeError(f"{paper}: C4/passport intake mismatch")
        should_pass = (
            report["overall_issues"].get("SERIOUS") == 0
            and report["overall_issues"].get("MEDIUM") == 0
            and report["phases"]["A_references"]["failed"] == 0
            and intake_valid
        )
        if (report["verdict"] == "PASS") != should_pass:
            raise RuntimeError(f"{paper}: report verdict disagrees with active blockers")
        expected_passport_status = "VERIFIED" if should_pass else "UNVERIFIED"
        if passport["verification_status"] != expected_passport_status:
            raise RuntimeError(f"{paper}: passport/report verification mismatch")
        if not intake_valid and (
            passport.get("experiment_provenance") != []
            or passport.get("experiment_alignment_results") != []
        ):
            raise RuntimeError(f"{paper}: provenance present before valid intake")
        if not semantic_path.is_file() or semantic_path.stat().st_size == 0:
            raise RuntimeError(f"{paper}: semantic audit missing")
        report_passes += int(should_pass)
        paper_pass_state[paper] = should_pass

        aggregate["papers"] += 1
        aggregate["registered"] += len(registry["claims"])
        aggregate["selected"] += len(selected)
        aggregate["tuples"] += len(rows)
        aggregate["anchorless"] += len(rows)
        aggregate["semantic_files"] += 1
        results.append(
            {
                "paper": paper,
                "registered": len(registry["claims"]),
                "selected": len(selected),
                "tuples": len(rows),
                "frozen": True,
                "coverage_replay": "PASS",
                "report": "PASS_AT_CHECKPOINT" if should_pass else "FAIL-CLOSED",
            }
        )

    expected_aggregate = {
        "papers": 5,
        "frozen_files": 15,
        "registered": 382,
        "selected": 331,
        "tuples": 340,
        "anchorless": 340,
        "semantic_files": 5,
    }
    if aggregate != expected_aggregate:
        raise RuntimeError(f"aggregate mismatch: {aggregate} != {expected_aggregate}")

    batch = load(ROOT / "BATCH_ROUND9_STAGE2_5_INTEGRITY_SUMMARY.json")
    expected_batch_verdict = "PASS" if report_passes == len(PAPERS) else "FAIL-CLOSED"
    if batch["batch_verdict"] != expected_batch_verdict or batch["stage3_authorized"]:
        raise RuntimeError("batch gate mismatch")
    if batch.get("route_a_sha256") != sha(ROOT / "skills/route-a-evaluator.md"):
        raise RuntimeError("batch Route-A hash mismatch")
    if batch.get("route_b_sha256") != sha(ROOT / "skills/route-b-evaluator.md"):
        raise RuntimeError("batch Route-B hash mismatch")
    if len(batch.get("papers", [])) != len(PAPERS):
        raise RuntimeError("batch paper population mismatch")
    serious_total = 0
    references_verified = 0
    for row in batch["papers"]:
        paper = row["paper"]
        base = ROOT / "papers" / paper
        notes = base / "notes"
        report = load(notes / "stage2_5_integrity_report.json")
        if row["verdict"] != report["verdict"]:
            raise RuntimeError(f"{paper}: batch/report verdict mismatch")
        if row["active_issues"] != report["extensions"]["active_issue_ids"]:
            raise RuntimeError(f"{paper}: batch/report issue mismatch")
        if row["integrity_report_sha256"] != sha(notes / "stage2_5_integrity_report.json"):
            raise RuntimeError(f"{paper}: batch integrity hash mismatch")
        if row["material_passport_sha256"] != sha(notes / "stage2_5_material_passport.json"):
            raise RuntimeError(f"{paper}: batch passport hash mismatch")
        if row["compliance_report_sha256"] != sha(notes / "stage2_5_compliance_report.json"):
            raise RuntimeError(f"{paper}: batch compliance hash mismatch")
        serious_total += report["overall_issues"]["SERIOUS"]
        references_verified += report["phases"]["A_references"]["passed"]
    expected_batch_aggregate = {
        "papers": 5,
        "papers_passed": report_passes,
        "registered_claims": aggregate["registered"],
        "selected_claims": aggregate["selected"],
        "evidence_tuples": aggregate["tuples"],
        "references_verified": references_verified,
        "references_total": 31,
        "serious_issues": serious_total,
        "positive_arithmetic_A2": 0,
        "route_b_invocations": 0,
    }
    for key, value in expected_batch_aggregate.items():
        if batch["aggregate"].get(key) != value:
            raise RuntimeError(f"batch aggregate mismatch for {key}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    root_phrases = [
        "Stage 2.5 完整审计已执行",
        "382 registered / 331 selected / 340 tuples",
        "skills/route-a-evaluator.md",
        "skills/route-b-evaluator.md",
        "anchorless",
    ]
    root_phrases.append("严格 FAIL-CLOSED" if expected_batch_verdict == "FAIL-CLOSED" else "Stage 2.5")
    for phrase in root_phrases:
        if phrase not in readme:
            raise RuntimeError(f"README missing status phrase: {phrase}")
    for paper in PAPERS:
        paper_readme = (ROOT / "papers" / paper / "README.md").read_text(encoding="utf-8")
        for phrase in ("Stage 2.5", "anchorless"):
            if phrase not in paper_readme:
                raise RuntimeError(f"{paper}: README missing current integrity phrase {phrase}")
        current_header = "\n".join(paper_readme.splitlines()[:45])
        if paper_pass_state[paper]:
            if "FAIL-CLOSED" in current_header or "PASS" not in current_header:
                raise RuntimeError(f"{paper}: README current header does not show Stage-2.5 PASS")
        elif "FAIL-CLOSED" not in current_header:
            raise RuntimeError(f"{paper}: README current header omits FAIL-CLOSED")

    batch_md = (ROOT / "BATCH_ROUND9_STAGE2_5_INTEGRITY_REPORT.md").read_text(
        encoding="utf-8"
    )
    for phrase in (
        expected_batch_verdict,
        "382 claims",
        "331 distinct claims",
        "340/340 exact evidence tuples",
        sha(ROOT / "skills/route-a-evaluator.md"),
        sha(ROOT / "skills/route-b-evaluator.md"),
    ):
        if phrase not in batch_md:
            raise RuntimeError(f"batch Markdown report missing {phrase}")
    for paper, passed in paper_pass_state.items():
        number = paper.split("-", 1)[0]
        verdict = "PASS" if passed else "FAIL"
        if f"| P{number} |" not in batch_md or verdict not in batch_md:
            raise RuntimeError(f"{paper}: batch Markdown paper row missing")

    print(
        json.dumps(
            {"status": "PASS", "aggregate": aggregate, "papers": results},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
