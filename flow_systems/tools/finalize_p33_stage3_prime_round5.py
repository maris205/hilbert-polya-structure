#!/usr/bin/env python3
"""Validate and close P33 Stage 3-prime Round 5 after Phase 2B."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "papers/33-bolza-control-matched-census"
NOTES = PAPER / "notes"
ARS = Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
CHECKER = ARS / "scripts/check_re_review_synthesis.py"
CHECKER_SHA = "8347ec3766857366cc0c6ffd30021afcebf8d0528a83927fabfce9ecb66a59ab"
ROUND_ID = "p33-stage3-prime-round5-2026-09-04"
SAME_FAMILY_DISCLOSURE = "This verification round ran on the same model family that drove the revisions; procedural role separation does not establish error independence, and over-optimization to the shared judge's latent biases remains possible."


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(f"P33_ROUND5_FINALIZE_FAIL: {message}")


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"object required: {path}")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def jcs_sha(value: object) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def binding(path: Path, *, jcs: bool = False) -> dict:
    row: dict[str, object] = {"path": rel(path), "sha256": sha(path), "bytes": path.stat().st_size}
    if jcs:
        row["jcs_sha256"] = jcs_sha(load(path))
    return row


def write_json_new(path: Path, value: object) -> None:
    require(not path.exists(), f"refusing to overwrite {path}")
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def verify_frozen(node: object, checks: list[str], prefix: str) -> None:
    if isinstance(node, dict):
        if set(node) == {"path", "sha256", "bytes"}:
            path = ROOT / str(node["path"])
            require(path.is_file() and not path.is_symlink(), f"{prefix}: missing/symlink {path}")
            require(path.stat().st_size == node["bytes"], f"{prefix}: byte drift {path}")
            require(sha(path) == node["sha256"], f"{prefix}: hash drift {path}")
            checks.append(f"{prefix}:{node['path']}")
        else:
            for key, child in node.items():
                verify_frozen(child, checks, f"{prefix}.{key}")
    elif isinstance(node, list):
        for index, child in enumerate(node):
            verify_frozen(child, checks, f"{prefix}[{index}]")


def main() -> None:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    paths = {
        "freeze": NOTES / "stage3_prime_round5_input_freeze.json",
        "manifest": NOTES / "stage3_prime_round5_input_manifest.json",
        "manifest_receipt": NOTES / "stage3_prime_round5_input_manifest_receipt.json",
        "precommitment": NOTES / "stage3_prime_round5_precommitment.json",
        "phase1_validation": NOTES / "stage3_prime_round5_phase1_validation.json",
        "verdict": NOTES / "stage3_prime_round5_verdict_record.json",
        "phase2a_validation": NOTES / "stage3_prime_round5_phase2a_validation.json",
        "phase2a_semantic": NOTES / "stage3_prime_round5_phase2a_semantic_audit.json",
        "phase2a_receipt": NOTES / "stage3_prime_round5_phase2a_receipt.md",
        "integration": NOTES / "stage3_prime_round5_phase2b_integration.json",
        "phase2b_receipt": NOTES / "stage3_prime_round5_phase2b_receipt.md",
        "trace": NOTES / "stage3_prime_round5_traceability.json",
        "roadmap": NOTES / "stage3_revision_roadmap.json",
        "author": NOTES / "stage4_author_adjudication.json",
        "response": NOTES / "stage4_response_to_reviewers_round1.json",
        "bundle": NOTES / "stage4_revision_evidence_bundle.json",
        "letter": NOTES / "stage3_editorial_synthesis.md",
        "apply_report": NOTES / "stage4_revision_round1.tex.apply-report.json",
        "revised": NOTES / "stage4_revision_round1.tex",
    }
    for label, path in paths.items():
        require(path.is_file() and not path.is_symlink(), f"missing/symlink {label}: {path}")
    require(sha(CHECKER) == CHECKER_SHA, "checker hash drift")

    freeze = load(paths["freeze"])
    manifest = load(paths["manifest"])
    manifest_receipt = load(paths["manifest_receipt"])
    pre = load(paths["precommitment"])
    phase1 = load(paths["phase1_validation"])
    verdict = load(paths["verdict"])
    phase2a = load(paths["phase2a_validation"])
    semantic = load(paths["phase2a_semantic"])
    integration = load(paths["integration"])
    trace = load(paths["trace"])
    roadmap = load(paths["roadmap"])
    response = load(paths["response"])
    checks: list[str] = []

    require(manifest["round_id"] == ROUND_ID and pre["round_id"] == ROUND_ID, "round identity")
    require(phase1["status"] == "PASS" and phase2a["status"] == "PASS" and semantic["status"] == "PASS", "earlier gate status")
    require(manifest_receipt["input_manifest"]["sha256"] == sha(paths["manifest"]), "manifest raw binding")
    require(manifest_receipt["input_manifest"]["jcs_sha256"] == jcs_sha(manifest), "manifest JCS binding")
    require(verdict["precommitment_hash"] == jcs_sha(pre), "verdict/precommitment binding")
    require(integration["verdict_record_hash"] == jcs_sha(verdict), "integration/verdict binding")
    require(trace["verdict_record_hash"] == jcs_sha(verdict), "trace/verdict binding")
    checks += ["round_identity", "earlier_gates", "manifest_raw_binding", "manifest_jcs_binding", "verdict_precommitment_binding", "integration_verdict_binding", "trace_verdict_binding"]
    verify_frozen(freeze["round4_preservation"], checks, "round4_preservation")
    verify_frozen(freeze["immutable_boundaries"], checks, "immutable_boundaries")

    trace_schema = load(ARS / "shared/contracts/re_review/traceability.schema.json")
    schema_errors = sorted(Draft202012Validator(trace_schema).iter_errors(trace), key=lambda error: (list(error.absolute_path), error.message))
    require(not schema_errors, "traceability schema: " + "; ".join(error.message for error in schema_errors))
    checks.append("official_traceability_schema")

    roadmap_rows = roadmap["items"]
    response_rows = response["items"]
    verdict_rows = verdict["items"]
    integration_rows = integration["rows"]
    trace_rows = trace["rows"]
    expected_ids = [row["id"] for row in roadmap_rows]
    require(expected_ids == [row["roadmap_item_id"] for row in response_rows], "response order")
    require(expected_ids == [row["item_id"] for row in verdict_rows], "verdict order")
    require(expected_ids == [row["item_id"] for row in integration_rows], "integration order")
    require(expected_ids == [row["item_id"] for row in trace_rows], "trace order")
    response_by_id = {row["roadmap_item_id"]: row for row in response_rows}
    roadmap_by_id = {row["id"]: row for row in roadmap_rows}
    verdict_by_id = {row["item_id"]: row for row in verdict_rows}
    for row in integration_rows:
        item_id = row["item_id"]
        source = response_by_id[item_id]
        expected_claim = "The authors state: " + source["author_response"]
        if "decline_justification" in source:
            expected_claim += " Decline justification: " + source["decline_justification"]
        require(row["original_comment"] == roadmap_by_id[item_id]["description"], f"{item_id}: original comment copy")
        require(row["authors_claim"] == expected_claim, f"{item_id}: author field copy")
        require(row["revision_location"] == source["change_location"], f"{item_id}: revision location copy")
        require(row["phase2a_verdict"] == verdict_by_id[item_id]["verdict"], f"{item_id}: Phase 2A copy")
        require(row["final_verdict"] == verdict_by_id[item_id]["verdict"], f"{item_id}: untyped verdict change")
        require(str(row["quality_assessment"]).strip(), f"{item_id}: quality assessment")
        checks += [f"{item_id}:author_copy", f"{item_id}:verdict_freeze", f"{item_id}:assessment"]

    require(integration["adjustments"] == [] and trace["adjustments"] == [], "unexpected adjustment")
    require(verdict["new_issues"] == [] and trace["new_issues"] == [], "new-issue set drift")
    require(len(integration["post_letter_observations"]) == 1, "post-letter observation count")
    require(trace["post_letter_observations"] == integration["post_letter_observations"], "post-letter observation drift")
    require(trace["decision_state"] == "Major Revision", "decision state")
    require(trace["decision_inputs"]["apply_chain_witness"] == "pass", "apply-chain witness")
    require(trace["decision_inputs"]["reject_recommended"] is False, "reject recommendation")
    require(trace["decision_inputs"]["should_fix_addressed_rate"] == {"numerator": 6, "denominator": 6}, "should-fix rate")
    residuals = [row for row in verdict_rows if row["verdict"] == "PARTIALLY_ADDRESSED" and row["residual_gap"]["residual_obligation_class"] == "must_fix"]
    require(len(residuals) == 6, "B4 residual count")
    checks += ["zero_adjustments", "new_issue_set_frozen", "post_letter_observation", "decision_major_revision", "apply_chain_pass", "reject_false", "should_fix_rate", "b4_six_must_residuals"]

    phase2b_receipt = paths["phase2b_receipt"].read_text(encoding="utf-8")
    require(next(line.strip() for line in reversed(phase2b_receipt.splitlines()) if line.strip()) == "[MATRIX-COMMITTED]", "matrix marker")
    for marker in ("integration attempt `1/1`", "retries `0`", "post-exposure repairs `0`", "Adjustment count: `0`", "Commitment-axis outcome: `NOT_APPLICABLE_NO_COMMITMENT_FIELDS`"):
        require(marker in phase2b_receipt, f"receipt marker absent: {marker}")
        checks.append(f"receipt:{marker}")
    require("[EVIDENCE-COMMITTED]" in paths["phase2a_receipt"].read_text(encoding="utf-8"), "evidence marker")
    checks.append("evidence_marker")

    phase2b_validation_path = NOTES / "stage3_prime_round5_phase2b_validation.json"
    write_json_new(phase2b_validation_path, {
        "schema_version": "p33-stage3-prime-round5-phase2b-validation/1.0",
        "generated_at": generated_at,
        "paper_id": "P33",
        "round_id": ROUND_ID,
        "phase": "phase2b_claim_matching_and_matrix_integration",
        "status": "PASS",
        "bindings": {
            "integration": binding(paths["integration"], jcs=True),
            "phase2b_receipt": binding(paths["phase2b_receipt"]),
            "traceability": binding(paths["trace"], jcs=True),
            "verdict": binding(paths["verdict"], jcs=True),
        },
        "counts": {
            "rows": len(integration_rows),
            "adjustments": len(integration["adjustments"]),
            "post_letter_observations": len(integration["post_letter_observations"]),
            "commitments_verified": 0,
            "validation_checks": len(checks),
        },
        "protocol": {
            "single_integration_attempt": True,
            "retries": 0,
            "post_exposure_repairs": 0,
            "phase2a_new_issue_set_preserved": True,
            "phase2a_verdicts_preserved": True,
            "same_family_error_independence_claimed": False,
        },
        "checks": checks,
    })

    command = [
        "python3", str(CHECKER),
        "--manifest", str(paths["manifest"]),
        "--precommitment", str(paths["precommitment"]),
        "--verdict-record", str(paths["verdict"]),
        "--traceability", str(paths["trace"]),
        "--roadmap", str(paths["roadmap"]),
        "--author-adjudication", str(paths["author"]),
        "--revision-evidence-bundle", str(paths["bundle"]),
        "--revision-evidence-root", str(PAPER),
        "--letter", str(paths["letter"]),
        "--apply-report", str(paths["apply_report"]),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    require(completed.returncode == 0, f"official checker: {completed.stderr}{completed.stdout}")
    require("decision_state 'Major Revision'" in completed.stdout, "checker decision mismatch")

    checker_receipt_path = NOTES / "stage3_prime_round5_checker_receipt.json"
    verdict_counts = Counter(row["final_verdict"] for row in trace_rows)
    write_json_new(checker_receipt_path, {
        "schema_version": "p33-stage3-prime-round5-checker-receipt/1.0",
        "paper_id": "P33",
        "round_id": ROUND_ID,
        "checked_at": generated_at,
        "checker": "ARS-Codex 0.1.26 scripts/check_re_review_synthesis.py",
        "checker_sha256": CHECKER_SHA,
        "checker_status": "PASS",
        "checker_exit_code": completed.returncode,
        "checker_stdout": completed.stdout,
        "checker_stderr": completed.stderr,
        "decision_state": "Major Revision",
        "decision_rule": "B4",
        "reject_recommended": False,
        "apply_chain_witness": "pass",
        "verdict_counts": dict(sorted(verdict_counts.items())),
        "adjustments": 0,
        "new_issues": 0,
        "dissents": 0,
        "escalation_exceptions": 0,
        "post_letter_observations": 1,
        "artifacts": {
            "manifest": binding(paths["manifest"], jcs=True),
            "precommitment": binding(paths["precommitment"], jcs=True),
            "verdict": binding(paths["verdict"], jcs=True),
            "integration": binding(paths["integration"], jcs=True),
            "traceability": binding(paths["trace"], jcs=True),
            "phase2b_validation": binding(phase2b_validation_path),
            "roadmap": binding(paths["roadmap"], jcs=True),
            "author_adjudication": binding(paths["author"], jcs=True),
            "revision_evidence_bundle": binding(paths["bundle"], jcs=True),
            "editorial_decision_letter": binding(paths["letter"]),
            "apply_report": binding(paths["apply_report"], jcs=True),
        },
        "same_family_disclosure": SAME_FAMILY_DISCLOSURE,
        "boundaries": {
            "canonical_files_changed": False,
            "science_or_results_changed": False,
            "initial_dynamical_system_changed": False,
            "route_credit_changed": False,
            "route_b_invoked": False,
            "successor_stage_authorized": False,
        },
    })

    report_path = NOTES / "stage3_prime_round5_verification_report.md"
    require(not report_path.exists(), f"refusing to overwrite {report_path}")
    report_path.write_text(f"""# P33 Stage 3′ Round 5 verification report

Date: **2026-09-04**

## Decision

**Major Revision — rule B4.** The official ARS synthesis checker passed and independently reproduced `decision_state='Major Revision'` with an intact apply-chain witness.

The fresh three-gate run reviewed all 13 roadmap items. Phase 2A committed 6 `FULLY_ADDRESSED` and 7 `PARTIALLY_ADDRESSED`; Phase 2B found no admissible adjustment basis, so those verdicts remain unchanged. Six partial items retain `must_fix` residuals, which mechanically triggers B4. The 6/6 `should_fix` items count as addressed; there are no negative verdicts, regressions, new issues, dissents, escalation exceptions, or reject recommendation.

## Concrete progress

The revised paper now has fully addressed closest-work/originality positioning, field-facing methods narration, exact control-object binding, self-reciprocal owner serialization, synthetic cross-producer conformance traces, and schema migration rules. Remaining must-fix work is specific: complete artifact locators, implemented independent fixture/oracle/build provenance, concrete valid/invalid serialized fixtures, unambiguous per-producer enumeration/coverage accounting, exact passage anchors for all 48 source uses, and manuscript-wide conditional typing of the target/control asymmetry. The standalone correction bibliography work remains a `should_fix` residual.

## Integrity and boundaries

- Phase 1: PASS, 13/13 revision-blind precommitments.
- Phase 2A: PASS, one evidence emission, no retry, 131 outer validation checks.
- Phase 2B: PASS, 13/13 rows, zero adjustments, one decision-inert pointer observation, no retry.
- Official checker SHA-256: `{CHECKER_SHA}`; result: PASS.
- Same-family role separation was used; error independence is not claimed.
- Canonical manuscript/PDF/bibliography, science/results, the initial dynamical-system restriction, Route A coordinates, and Route B state remain unchanged.

The next legal transition is a new, explicitly authorized Stage 4′ residual-remediation round. Stage 4.5, Stage 5, canonical promotion, Route advancement, and new scientific execution are not authorized by this result.
""", encoding="utf-8")

    final_audit_path = NOTES / "stage3_prime_round5_final_integrity_audit.json"
    completion_path = NOTES / "stage3_prime_round5_completion_receipt.json"
    final_inputs = [
        paths["freeze"], paths["manifest"], paths["manifest_receipt"], paths["precommitment"],
        paths["phase1_validation"], paths["verdict"], paths["phase2a_validation"], paths["phase2a_semantic"],
        paths["phase2a_receipt"], paths["integration"], paths["phase2b_receipt"], phase2b_validation_path,
        paths["trace"], checker_receipt_path, report_path,
    ]
    write_json_new(final_audit_path, {
        "schema_version": "p33-stage3-prime-round5-final-integrity-audit/1.0",
        "generated_at": generated_at,
        "paper_id": "P33",
        "round_id": ROUND_ID,
        "status": "PASS",
        "decision": "Major Revision",
        "decision_rule": "B4",
        "artifacts": [binding(path, jcs=path.suffix == ".json") for path in final_inputs],
        "counts": {
            "phase1_items": 13,
            "phase2a_items": 13,
            "phase2b_rows": 13,
            "fully_addressed": 6,
            "partially_addressed": 7,
            "must_fix_residuals": 6,
            "should_fix_residuals": 1,
            "adjustments": 0,
            "post_letter_observations": 1,
        },
        "official_checker": "PASS",
        "frozen_inputs_replayed": len([check for check in checks if check.startswith(("round4_preservation", "immutable_boundaries"))]),
        "boundaries": {
            "no_phase2_retry": True,
            "no_manuscript_edit": True,
            "no_canonical_promotion": True,
            "no_scientific_execution": True,
            "no_route_transition": True,
        },
    })
    write_json_new(completion_path, {
        "schema_version": "p33-stage3-prime-round5-completion-receipt/1.0",
        "generated_at": generated_at,
        "paper_id": "P33",
        "round_id": ROUND_ID,
        "status": "COMPLETE",
        "decision": "Major Revision",
        "decision_rule": "B4",
        "reject_recommended": False,
        "phase_counts": {"FULLY_ADDRESSED": 6, "PARTIALLY_ADDRESSED": 7},
        "residual_counts": {"must_fix": 6, "should_fix": 1},
        "official_checker": binding(checker_receipt_path),
        "verification_report": binding(report_path),
        "final_integrity_audit": binding(final_audit_path),
        "next_gate": "EXPLICIT_AUTHORIZATION_REQUIRED_FOR_NEW_STAGE4_PRIME_RESIDUAL_REMEDIATION",
        "route_state_changed": False,
        "canonical_or_science_state_changed": False,
    })
    print(f"PASS -- P33 Round 5 complete: Major Revision/B4; checker {sha(checker_receipt_path)}")


if __name__ == "__main__":
    main()
