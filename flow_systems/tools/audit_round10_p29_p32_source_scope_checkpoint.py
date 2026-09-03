#!/usr/bin/env python3
"""Final audit and receipt for the stopped P29/P32 correction track."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
RECEIPT = ROOT / "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SOURCE_FINALIZATION_SCOPE_CHECKPOINT_RECEIPT.json"

EXPECTED = {
    "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.json": "2b8a1c5d57cc01589ca6c926dc5590be0cbe58cae187a0b70d0b4c6c9a6bf3b3",
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json": "7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf",
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json": "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff",
    "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_ESCALATION_INCIDENT.json": "4f89cacee2d05a4c1d0dd03afdc44e2c26d015dbc4517ffc66a69c73db16c3b9",
    "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json": "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b",
    "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.md": "74045f2b6758333d6dc1792e5e5a40052a559ed9f983a88b6154e37aa3e6f63d",
    "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED_VALIDATION.json": "947e7203cc22109969831aa0bee066dbc2b0fa5415090c6781aa3b33d8f7dd80",
    "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_source_finalization_round3.json": "05997bc748c453d01e9a5674528acfeb496ffdb9b8d7d6ef22c6e8d30c2bffdc",
    "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_claim_passage_matrix_round3.json": "ac253359ce62df4c4f7d8c1143fde92d71918c157c45a68f8a32717d3bc79b71",
    "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_source_finalization_round3_validation.json": "9373e2bd962a9d865a1a3690b5b0cf17fd3d01336578c3fde665692c5bb4b26e",
    "papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_source_finalization_round3.json": "545da2f55c9e8e2318273d81100821978aaec0e4ab799207ed0fc02ac4dc5c26",
    "papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_claim_passage_matrix_round3.json": "18259fa9200782715192325dd882c9d6b32bd7f7f2e335e1bf54c8c39d10ea9a",
    "papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_source_finalization_round3_validation.json": "d05ff4ae861989ec8052371b668e6286bdafcacec0c652603303584d789f4a5e",
}

PAPERS = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "expected_source": {"registered_contexts": 22, "exact_locators_finalized": 13, "prior_bounded_scopes_retained": 0, "explicit_bounded_unavailability": 9, "passage_bounded_total": 13},
        "original": 26,
        "expanded": 31,
        "added": ["B0004", "B0050", "B0054", "B0090", "B0091"],
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "expected_source": {"registered_contexts": 30, "exact_locators_finalized": 18, "prior_bounded_scopes_retained": 4, "explicit_bounded_unavailability": 8, "passage_bounded_total": 22},
        "original": 10,
        "expanded": 15,
        "added": ["B0006", "B0047", "B0109", "B0128", "B0137"],
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(path: Path) -> dict[str, Any]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_blocks(text: str) -> dict[str, str]:
    markers = list(re.finditer(r"(?m)^<!--block:(B\d{4})-->\s*$", text))
    result: dict[str, str] = {}
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        result[marker.group(1)] = text[marker.end():end].strip()
    return result


def target_rows(paper: dict[str, Any]) -> list[dict[str, Any]]:
    return [target for issue in paper["issues"] for target in issue["proposed_targets"]]


def main() -> int:
    checks: list[dict[str, str]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})

    for path_text, expected in EXPECTED.items():
        path = ROOT / path_text
        check(f"H{len(checks) + 1:03d}", path.exists() and sha(path) == expected, f"exact artifact hash: {path_text}")

    old_request_path = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.json"
    expanded_path = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json"
    freeze_path = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json"
    validation_path = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED_VALIDATION.json"
    old_request = load(old_request_path)
    expanded = load(expanded_path)
    freeze = load(freeze_path)
    validation = load(validation_path)
    old_by_id = {paper["paper_id"]: paper for paper in old_request["papers"]}
    expanded_by_id = {paper["paper_id"]: paper for paper in expanded["papers"]}
    freeze_by_id = {paper["paper_id"]: paper for paper in freeze["papers"]}

    source_bindings = []
    readme_bindings = []
    frozen_bindings = []
    prohibited = []
    for paper_id, cfg in PAPERS.items():
        notes = ROOT / "papers" / cfg["slug"] / "notes"
        source_path = notes / "stage4_prime_source_finalization_round3.json"
        matrix_path = notes / "stage4_prime_claim_passage_matrix_round3.json"
        source_validation_path = notes / "stage4_prime_source_finalization_round3_validation.json"
        source = load(source_path)
        source_validation = load(source_validation_path)
        expected_summary = {**cfg["expected_source"], "manuscript_patch_applied": False}
        check(f"S-{paper_id}-01", source["summary"] == expected_summary, f"{paper_id} exact locator/unavailability partition")
        check(f"S-{paper_id}-02", source_validation["verdict"] == "PASS" and source_validation["passed"] == 6 and source_validation["failed"] == 0, f"{paper_id} source validation 6/6")
        check(f"S-{paper_id}-03", len(source["rows"]) == cfg["expected_source"]["registered_contexts"], f"{paper_id} source row denominator")
        check(f"S-{paper_id}-04", all(not row["locator_guessed"] for row in source["rows"]), f"{paper_id} no guessed locator")
        check(f"S-{paper_id}-05", all(not row["manuscript_patch_applied"] for row in source["rows"]), f"{paper_id} no source row claims a patch")
        source_bindings.extend([binding(source_path), binding(matrix_path), binding(source_validation_path)])

        current = freeze_by_id[paper_id]
        rows = [
            current["current_working_draft"],
            current["current_working_bibliography"],
            current["available_block_manifest"],
            *current["canonical_files"],
            *current["science_files"],
            current["initial_system_source"],
            current["route_crosswalk"],
        ]
        check(f"F-{paper_id}-01", all(sha(ROOT / row["path"]) == row["sha256"] for row in rows), f"{paper_id} frozen draft/Bib/manifest/canonical/science/initial/Route hashes")
        frozen_bindings.extend(rows)

        old_targets = target_rows(old_by_id[paper_id])
        new_targets = target_rows(expanded_by_id[paper_id])
        current_blocks = parse_blocks((ROOT / current["current_working_draft"]["path"]).read_text(encoding="utf-8"))
        check(f"T-{paper_id}-01", len(old_targets) == cfg["original"] and len(new_targets) == cfg["expanded"], f"{paper_id} original/expanded target counts")
        check(f"T-{paper_id}-02", [target["block_id"] for target in new_targets[-5:]] == cfg["added"], f"{paper_id} exact additional target order")
        check(f"T-{paper_id}-03", all(target["allowed_operations"] == ["replace_block"] for target in new_targets), f"{paper_id} operation whitelist")
        check(
            f"T-{paper_id}-04",
            all(hashlib.sha256(current_blocks[target["block_id"]].encode("utf-8")).hexdigest() == target["expected_old_hash"] for target in new_targets),
            f"{paper_id} every expanded old hash matches current Round-2 block",
        )

        readme = ROOT / "papers" / cfg["slug"] / "README.md"
        readme_text = readme.read_text(encoding="utf-8")
        check(f"R-{paper_id}-01", EXPECTED[expanded_path.name] in readme_text, f"{paper_id} README records expanded request SHA")
        check(f"R-{paper_id}-02", "No Round-3 manuscript patch, draft, build, or PDF was created" in readme_text, f"{paper_id} README records fail-closed boundary")
        readme_bindings.append(binding(readme))

        prohibited.extend(
            [
                notes / "stage4_prime_revision_patch_round3.json",
                notes / "stage4_prime_revision_round3.tex",
                notes / "stage4_prime_revision_round3.pdf",
                notes / "stage4_prime_revision_round3_build_receipt.json",
                notes / "stage4_prime_revision_evidence_bundle_round3.json",
                notes / "stage4_prime_response_to_reviewers_round3.json",
            ]
        )

    check("A001", validation["verdict"] == "PASS" and validation["passed"] == 20 and validation["failed"] == 0, "expanded request validation 20/20")
    check("A002", expanded["totals"]["block_operation_pairs"] == 46 and expanded["totals"]["unique_target_blocks"] == 46, "46 exact unique replace_block pairs")
    check("A003", expanded["totals"]["passage_bounded_total"] == 35 and expanded["totals"]["explicit_bounded_unavailability"] == 17, "35 passage-bounded plus 17 explicit unavailable contexts")
    check("A004", all(not path.exists() for path in prohibited), "no patch/draft/PDF/build/evidence/response Round-3 output")
    check("A005", expanded["boundaries"]["bibliography_mutation"] is False and expanded["boundaries"]["route_or_initial_system_mutation"] is False, "Bib/Route/initial-system boundaries retained")
    check("A006", expanded["boundaries"]["stage4_5_rerun"] is False and expanded["boundaries"]["patch_application_now"] is False, "no Stage-4.5 rerun or current patch authority")

    incident_paths = [
        ROOT / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_001.json",
        ROOT / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_002.json",
        ROOT / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_003.json",
        ROOT / "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_REQUEST_PREP_INCIDENT_001.json",
        ROOT / "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_ESCALATION_INCIDENT.json",
    ]
    check("A007", all(path.exists() for path in incident_paths), "all fail-closed incidents retained")

    verdict = "PASS" if all(row["status"] == "PASS" for row in checks) else "FAIL"
    receipt = {
        "schema_version": "round10-p29-p32-stage4-prime-source-finalization-scope-checkpoint-receipt/1.0",
        "generated_at_utc": STAMP,
        "status": "READ_ONLY_SOURCE_FINALIZATION_COMPLETE_PATCH_BLOCKED_AWAITING_EXPANDED_AUTHORIZATION",
        "verdict": verdict,
        "authority": [binding(old_request_path), binding(ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json"), binding(freeze_path)],
        "source_finalization_artifacts": source_bindings,
        "scope_checkpoint_artifacts": [
            binding(ROOT / "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_ESCALATION_INCIDENT.json"),
            binding(expanded_path),
            binding(ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.md"),
            binding(validation_path),
        ],
        "retained_fail_closed_incidents": [binding(path) for path in incident_paths],
        "orchestration_tools": [
            binding(ROOT / "tools/build_round10_p29_p32_source_finalization_round3.py"),
            binding(ROOT / "tools/build_round10_p29_p32_scope_escalation_request.py"),
            binding(Path(__file__).resolve()),
        ],
        "per_paper_readmes": readme_bindings,
        "frozen_boundary_bindings": frozen_bindings,
        "counts": {
            "source_contexts": 52,
            "exact_locators_newly_finalized": 31,
            "prior_bounded_scopes_retained": 4,
            "passage_bounded_total": 35,
            "explicit_bounded_unavailability": 17,
            "original_replace_block_pairs": 36,
            "additional_required_pairs": 10,
            "expanded_requested_pairs": 46,
            "applied_pairs": 0,
            "checks_passed": sum(row["status"] == "PASS" for row in checks),
            "checks_failed": sum(row["status"] == "FAIL" for row in checks),
        },
        "build": {
            "status": "NOT_RUN_BY_UNLISTED_TARGET_STOP_CONDITION",
            "papers_built": 0,
            "pdfs_created": 0,
            "pages": None,
        },
        "next_checkpoint": {
            "request": binding(expanded_path),
            "required_event": "explicit author confirmation of the displayed exact request SHA-256",
        },
        "checks": checks,
    }
    dump(RECEIPT, receipt)
    if verdict != "PASS":
        raise RuntimeError("final checkpoint audit failed")
    print(json.dumps({"receipt": binding(RECEIPT), "counts": receipt["counts"], "build": receipt["build"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
