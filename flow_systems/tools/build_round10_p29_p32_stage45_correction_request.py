#!/usr/bin/env python3
"""Prepare, but do not execute, the exact P29/P32 Stage-4.5 correction request."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_AUTHORIZATION_RECEIPT.json"
AUTH_SHA = "3c2b273f637d0739473c4df06deef9bbcec0773fff2b2af39e5580a2f6d1129c"
FREEZE = ROOT / "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_INPUT_FREEZE.json"
FREEZE_SHA = "3c03bdfd37d6e95dcbc937b30e45ca4759565b189a1c5bd5c619c28e20ceb2cb"
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

CONFIGS: tuple[dict[str, Any], ...] = (
    {
        "paper_id": "P29",
        "paper_slug": "29-bianchi-ideal-owner-refinement",
        "draft_sha": "b8e6526e626d7ff6f343b1bc02ed610b3baedfa55cd1fa734f7e943ab6f6d6e8",
        "bib_sha": "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
        "citation_blocks": [
            "B0020", "B0021", "B0022", "B0023", "B0024", "B0025", "B0026", "B0027",
            "B0028", "B0029", "B0030", "B0033", "B0034", "B0035", "B0036", "B0037",
            "B0038", "B0039", "B0042", "B0043", "B0044", "B0045",
        ],
        "inventory_blocks": ["B0080", "B0107"],
        "status_blocks": ["B0109"],
        "disclosure_blocks": ["B0108"],
        "issues": [
            {
                "issue_id": "P29-S45R1-I01",
                "severity": "SERIOUS",
                "implementation_branch": (
                    "For all 22 registered contexts, retrieve the authoritative/first-party source when accessible and bind an exact theorem, page, section, or paragraph locator plus a hashed support excerpt. If access or support remains unavailable, record that state explicitly and replace only the listed citation block with a narrower metadata-only statement or remove the unsupported transfer; never guess a locator. Bind the resulting 22-row matrix in B0080 and B0107."
                ),
            },
            {
                "issue_id": "P29-S45R1-I02",
                "severity": "MEDIUM",
                "implementation_branch": "Replace B0109's stale pending-Stage-2.5 statement with the exact post-correction locator totals and current Stage-4.5 status; make no scientific or Route promotion.",
            },
            {
                "issue_id": "P29-S45R1-I03",
                "severity": "MEDIUM",
                "implementation_branch": "Extend B0108 to disclose the actual 3--4 September Stage-4/Stage-4-prime and Stage-4.5 assistance, preserving the unavailable backend-build limitation and same-family correlated-error boundary.",
            },
        ],
    },
    {
        "paper_id": "P32",
        "paper_slug": "32-homology-cover-renormalization-uniformity",
        "draft_sha": "e52dabd5b228bc39006574b884b2fba64389a536c7ff2a749e1afa4b82e2b784",
        "bib_sha": "adba0e9dd3e020cce23e3601480fa6aa5fc8f5d8384793eb1d0860af04a1b195",
        "citation_blocks": ["B0024", "B0028", "B0032", "B0033", "B0036", "B0039"],
        "inventory_blocks": ["B0125"],
        "status_blocks": ["B0119"],
        "disclosure_blocks": ["B0127", "B0138"],
        "issues": [
            {
                "issue_id": "P32-S45R1-I01",
                "severity": "SERIOUS",
                "implementation_branch": (
                    "Retain the four already finalized closest-work scopes. For each of the 26 inherited contexts, retrieve the authoritative/first-party source when accessible and bind an exact theorem, page, section, or paragraph locator plus a hashed support excerpt. If access or support remains unavailable, record that state and narrow or remove only the unsupported transfer in one of the six listed citation blocks; never guess. Bind the 30-row matrix in B0125."
                ),
            },
            {
                "issue_id": "P32-S45R1-I02",
                "severity": "MEDIUM",
                "implementation_branch": "Replace B0119's overbroad all-unresolved sentence with the exact split: four bounded closest-work uses finalized and 26 inherited uses resolved or explicitly unavailable according to the new matrix.",
            },
            {
                "issue_id": "P32-S45R1-I03",
                "severity": "MEDIUM",
                "implementation_branch": "Update B0127 and B0138 to disclose the actual 3--4 September Stage-4-prime Round-2 and Stage-4.5 assistance, while retaining the unavailable backend-build and correlated-error limitations.",
            },
        ],
    },
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write(path: Path, value: str) -> None:
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def block_rows(text: str) -> dict[str, dict[str, Any]]:
    marks = list(re.finditer(r"(?m)^<!--block:(B\d{4})-->\s*$", text))
    rows: dict[str, dict[str, Any]] = {}
    for index, marker in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        value = text[marker.end():end].strip()
        rows[marker.group(1)] = {
            "block_id": marker.group(1),
            "expected_old_hash": hashlib.sha256(value.encode("utf-8")).hexdigest(),
            "first_line_excerpt": re.sub(r"\s+", " ", value)[:160],
            "allowed_operations": ["replace_block"],
        }
    return rows


def binding(path: Path) -> dict[str, Any]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size}


def source_proposal(cfg: dict[str, Any], notes: Path) -> tuple[Path, Path]:
    audit_path = notes / "stage4_5_round1_reference_citation_audit.json"
    browser_path = notes / "stage4_5_round1_browser_reference_verification.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    browser = json.loads(browser_path.read_text(encoding="utf-8"))
    by_slug = {row["ref_slug"]: row for row in browser["rows"]}
    rows = []
    for context in audit["phase_b"]["contexts"]:
        source = by_slug[context["ref_slug"]]
        rows.append(
            {
                "context_id": context["context_id"],
                "context_sha256": context["context_sha256"],
                "block_id": context["block_id"],
                "ref_slug": context["ref_slug"],
                "identity_source_url": source["authoritative_or_first_party_url_reviewed"],
                "current_passage_locator": context["passage_locator"],
                "current_verdict": context["verdict"],
                "proposed_later_branch": (
                    "RETAIN_FINALIZED_BOUNDED_SCOPE"
                    if context["verdict"].startswith("VERIFIED")
                    else "EXACT_LOCATOR_OR_EXPLICIT_UNAVAILABILITY_AND_CLAIM_NARROWING"
                ),
                "locator_not_guessed": True,
            }
        )
    proposal = {
        "schema_version": f"{cfg['paper_id'].lower()}-stage4.5-round1-source-finalization-proposal/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "status": "PROPOSAL_ONLY_NOT_EXECUTED",
        "inputs": [binding(audit_path), binding(browser_path)],
        "registered_contexts": len(rows),
        "currently_verified": sum(row["current_verdict"].startswith("VERIFIED") for row in rows),
        "currently_anchorless": sum(row["current_passage_locator"] is None for row in rows),
        "rows": rows,
        "scientific_claim_strengthening_allowed": False,
        "passage_locator_guessing_allowed": False,
        "manuscript_patch_applied": False,
    }
    jp = notes / "stage4_5_round1_source_finalization_proposal.json"
    mp = notes / "stage4_5_round1_source_finalization_proposal.md"
    dump(jp, proposal)
    write(
        mp,
        "\n".join(
            [
                f"# {cfg['paper_id']} — Stage 4.5 Round 1 source-finalization proposal",
                "",
                "Status: **proposal only; no source passage or manuscript correction has been applied.**",
                "",
                f"All {len(rows)} registered citation-context tuples are enumerated. "
                f"{proposal['currently_verified']} retain a bounded finalized scope and "
                f"{proposal['currently_anchorless']} currently have no passage locator.",
                "",
                "A later authorized pass must either bind an exact source passage or preserve explicit unavailability and narrow/remove the unsupported transfer. No locator may be guessed and no claim may be strengthened.",
            ]
        ),
    )
    return jp, mp


def main() -> int:
    if sha(AUTH) != AUTH_SHA or sha(FREEZE) != FREEZE_SHA:
        raise RuntimeError("authorization/input-freeze digest mismatch")
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    if not (auth["authorized_tracks"]["p29_stage4_5_fresh_audit_only"] and auth["authorized_tracks"]["p32_stage4_5_fresh_audit_only"]):
        raise RuntimeError("proposal authority missing")

    papers = []
    for cfg in CONFIGS:
        paper = ROOT / "papers" / cfg["paper_slug"]
        notes = paper / "notes"
        draft = notes / "stage4_prime_revision_round2.tex"
        bib = notes / "stage4_prime_references_round2.bib"
        if sha(draft) != cfg["draft_sha"] or sha(bib) != cfg["bib_sha"]:
            raise RuntimeError(f"{cfg['paper_id']} current Stage-4-prime chain changed")
        source_json, source_md = source_proposal(cfg, notes)
        blocks = block_rows(draft.read_text(encoding="utf-8"))
        issue_targets = []
        for issue in cfg["issues"]:
            if issue["issue_id"].endswith("I01"):
                ids = cfg["citation_blocks"] + cfg["inventory_blocks"]
            elif issue["issue_id"].endswith("I02"):
                ids = cfg["status_blocks"]
            else:
                ids = cfg["disclosure_blocks"]
            issue_targets.append({**issue, "proposed_author_triage": "will_address", "proposed_targets": [blocks[x] for x in ids]})
        all_ids = cfg["citation_blocks"] + cfg["inventory_blocks"] + cfg["status_blocks"] + cfg["disclosure_blocks"]
        if len(all_ids) != len(set(all_ids)):
            raise RuntimeError(f"{cfg['paper_id']} duplicate target")
        integrity = notes / "stage4_5_round1_integrity_report.json"
        receipt = notes / "stage4_5_round1_receipt.json"
        checkpoint = notes / "stage4_5_round1_correction_checkpoint.json"
        if json.loads(integrity.read_text(encoding="utf-8"))["verdict"] != "FAIL":
            raise RuntimeError("request may only follow the recorded FAIL")
        papers.append(
            {
                "paper_id": cfg["paper_id"],
                "paper_slug": cfg["paper_slug"],
                "current_stage4_prime_draft": binding(draft),
                "current_stage4_prime_bibliography": binding(bib),
                "stage4_5_integrity_report": binding(integrity),
                "stage4_5_receipt": binding(receipt),
                "stage4_5_correction_checkpoint": binding(checkpoint),
                "source_finalization_proposal": binding(source_json),
                "source_finalization_human_summary": binding(source_md),
                "blocking_issue_count": len(issue_targets),
                "unique_target_blocks": len(all_ids),
                "block_operation_pairs": len(all_ids),
                "issues": issue_targets,
                "supporting_operations_after_authorization": [
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_source_finalization_round3.json", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_claim_passage_matrix_round3.json", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_revision_patch_round3.json", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_revision_round3.tex", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_revision_evidence_bundle_round3.json", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_response_to_reviewers_round3.json", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_revision_round3.pdf", "operation": "create_file"},
                    {"path": f"papers/{cfg['paper_slug']}/notes/stage4_prime_revision_round3_build_receipt.json", "operation": "create_file"},
                ],
            }
        )

    request = {
        "schema_version": "round10-stage4.5-correction-authorization-request-p29-p32/1.0",
        "generated_at_utc": STAMP,
        "status": "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION",
        "authorization_source": [binding(AUTH), binding(FREEZE)],
        "proposed_display_order": "source_traceability",
        "proposed_author_triage": "will_address",
        "proposed_revision_round": 3,
        "papers": papers,
        "totals": {
            "papers": 2,
            "blocking_issues": sum(p["blocking_issue_count"] for p in papers),
            "unique_target_blocks": sum(p["unique_target_blocks"] for p in papers),
            "block_operation_pairs": sum(p["block_operation_pairs"] for p in papers),
            "registered_citation_contexts": 52,
            "currently_passage_verified": 4,
            "currently_anchorless": 48,
        },
        "boundaries": {
            "request_preparation_only_now": True,
            "patch_application_now": False,
            "bibliography_mutation": False,
            "canonical_or_science_result_mutation": False,
            "stage4_5_rerun": False,
            "stage5_or_stage6": False,
            "route_or_initial_system_mutation": False,
            "registered_claim_strength_replacement": False,
            "citation_style": "plainnat numeric",
        },
        "stop_conditions_for_later_execution": [
            "target block hash mismatch",
            "source passage cannot be verified and the claim cannot be safely narrowed within the listed block",
            "scientific value or canonical result would change",
            "registered claim would require strengthening or replacement",
            "any target or operation outside this request is required",
        ],
    }
    request_json = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.json"
    request_md = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.md"
    dump(request_json, request)
    lines = [
        "# Round 10 P29/P32 — exact Stage 4.5 correction authorization request",
        "",
        "Status: **AWAITING EXPLICIT AUTHOR CONFIRMATION. Nothing in this request has been applied.**",
        "",
        f"Machine request: `{request_json.name}` SHA-256 `{sha(request_json)}`.",
        "",
        "A later short confirmation would authorize only the exact `replace_block` targets below plus the named notes-side support artifacts. Source locators must be exact; unavailable or non-supporting sources require explicit unavailability and claim narrowing/removal, never inference by metadata.",
        "",
    ]
    for paper in papers:
        lines.extend([f"## {paper['paper_id']}", ""])
        for issue in paper["issues"]:
            targets = ", ".join(f"`{row['block_id']}`/{row['allowed_operations'][0]}@`{row['expected_old_hash'][:12]}`" for row in issue["proposed_targets"])
            lines.extend([f"- `{issue['issue_id']}` ({issue['severity']}): {targets}.", f"  Branch: {issue['implementation_branch']}"])
        lines.append("")
    lines.extend(
        [
            "## Frozen boundaries",
            "",
            "No patch, bibliography change, canonical promotion, scientific execution/result refresh, Stage 4.5 rerun, Stage 5/6, Route change, initial-system change, or registered-claim strengthening is authorized by preparing this request.",
        ]
    )
    write(request_md, "\n".join(lines))

    checks = []
    def check(check_id: str, condition: bool, detail: str) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})
    check("V001", sha(AUTH) == AUTH_SHA, "authorization receipt digest")
    check("V002", sha(FREEZE) == FREEZE_SHA, "input-freeze digest")
    check("V003", request["totals"]["registered_citation_contexts"] == 52, "22 P29 + 30 P32 contexts")
    check("V004", request["totals"]["currently_anchorless"] == 48, "22 P29 + 26 P32 anchorless contexts")
    check("V005", request["totals"]["unique_target_blocks"] == 36, "26 P29 + 10 P32 exact target blocks")
    check("V006", request["totals"]["block_operation_pairs"] == 36, "replace_block only")
    check("V007", all(row["allowed_operations"] == ["replace_block"] for p in papers for issue in p["issues"] for row in issue["proposed_targets"]), "no broad operation")
    check("V008", all(sha(ROOT / p["current_stage4_prime_draft"]["path"]) == p["current_stage4_prime_draft"]["sha256"] for p in papers), "draft hashes rebound")
    check("V009", all(sha(ROOT / p["current_stage4_prime_bibliography"]["path"]) == p["current_stage4_prime_bibliography"]["sha256"] for p in papers), "bibliography hashes rebound")
    check("V010", request["boundaries"]["patch_application_now"] is False and request["boundaries"]["stage4_5_rerun"] is False, "request prep remains non-executing")
    validation = {
        "schema_version": "round10-stage4.5-correction-authorization-request-p29-p32-validation/1.0",
        "generated_at_utc": STAMP,
        "request_json": binding(request_json),
        "request_md": binding(request_md),
        "checks": checks,
        "passed": sum(row["status"] == "PASS" for row in checks),
        "failed": sum(row["status"] == "FAIL" for row in checks),
        "verdict": "PASS" if all(row["status"] == "PASS" for row in checks) else "FAIL",
    }
    validation_path = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json"
    dump(validation_path, validation)
    if validation["verdict"] != "PASS":
        raise RuntimeError("request validation failed")
    print(json.dumps({"request": binding(request_json), "human": binding(request_md), "validation": binding(validation_path), "totals": request["totals"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
