#!/usr/bin/env python3
"""Deterministic boundary audit for Round-10 Stage-1 Phase-5 review.

The script is read-only.  It verifies the frozen inputs, citation/reference/
source-ledger closure, manifest reference closure, and (with --phase full) the
presence and input binding of the four review surfaces plus synthesis and
checkpoint.  It does not judge scientific or editorial merit.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "BATCH_ROUND10_STAGE1_PHASE5_INPUT_FREEZE.json"
ROLES = (
    "editorial_review",
    "ethics_review",
    "citation_integrity_review",
    "devils_advocate",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def reference_ids(report: str) -> list[str]:
    match = re.search(r"(?ms)^## References\s*$\n(.*?)(?=^## |\Z)", report)
    if not match:
        return []
    return re.findall(r"(?m)^- \[([^\]]+)\] ", match.group(1))


def source_ids(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return [row["source_id"] for row in csv.DictReader(handle, delimiter="\t")]


def audit_paper(row: dict, phase: str) -> tuple[dict, list[str]]:
    paper = row["paper"]
    base = ROOT / "papers" / row["slug"] / "notes"
    report_path = base / "stage1_phase4_research_report.md"
    manifest_path = base / "stage1_phase4_claim_intent_manifest.json"
    checkpoint_path = base / "stage1_phase4_checkpoint.md"
    verification_md_path = base / "stage1_phase2_source_verification.md"
    verification_tsv_path = base / "stage1_phase2_source_verification.tsv"
    failures: list[str] = []

    expected = {
        report_path: row["report_sha256"],
        manifest_path: row["manifest_sha256"],
        checkpoint_path: row["checkpoint_sha256"],
        verification_md_path: row["source_verification_md_sha256"],
        verification_tsv_path: row["source_verification_tsv_sha256"],
    }
    for path, sha in expected.items():
        if not path.is_file():
            fail(failures, f"{paper}: missing frozen input {path.relative_to(ROOT)}")
        elif digest(path) != sha:
            fail(failures, f"{paper}: frozen hash mismatch {path.relative_to(ROOT)}")

    report = report_path.read_text(encoding="utf-8")
    pair_re = re.compile(r"<!--ref:([^>]+)--><!--anchor:([^:>]+):([^>]*)-->")
    pairs = pair_re.findall(report)
    raw_ref_markers = re.findall(r"<!--ref:([^>]+)-->", report)
    refs = reference_ids(report)
    sources = source_ids(verification_tsv_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    planned = [ref for claim in manifest["claims"] for ref in claim.get("planned_refs", [])]
    claim_constraints = sum(len(c.get("negative_constraints", [])) for c in manifest["claims"])
    manifest_constraints = len(manifest.get("manifest_negative_constraints", []))

    if len(raw_ref_markers) != len(pairs):
        fail(failures, f"{paper}: unpaired citation marker(s)")
    if set(raw_ref_markers) != set(refs):
        fail(failures, f"{paper}: citation/reference ID set mismatch")
    if set(refs) != set(sources):
        fail(failures, f"{paper}: reference/source-verification ID set mismatch")
    if len(refs) != len(set(refs)):
        fail(failures, f"{paper}: duplicate reference-list ID")
    if any(ref not in set(sources) for ref in planned):
        fail(failures, f"{paper}: manifest planned_refs contains unknown source ID")
    if any(kind != "none" or value != "" for _, kind, value in pairs):
        fail(failures, f"{paper}: unexpected non-none locator in frozen report")
    if "formal Route-A tuple" not in report and "FORMAL_ROUTE_A" not in report:
        fail(failures, f"{paper}: missing visible formal Route-A boundary")

    role_hashes: dict[str, str] = {}
    if phase == "full":
        for role in ROLES:
            path = base / f"stage1_phase5_{role}.md"
            if not path.is_file():
                fail(failures, f"{paper}: missing Phase-5 role output {path.name}")
                continue
            text = path.read_text(encoding="utf-8")
            if row["report_sha256"] not in text:
                fail(failures, f"{paper}: {path.name} lacks exact report binding")
            role_hashes[role] = digest(path)
        for name in ("stage1_phase5_review_synthesis.md", "stage1_phase5_checkpoint.md"):
            path = base / name
            if not path.is_file():
                fail(failures, f"{paper}: missing Phase-5 output {name}")
            else:
                text = path.read_text(encoding="utf-8")
                if row["report_sha256"] not in text:
                    fail(failures, f"{paper}: {name} lacks exact report binding")
                role_hashes[name] = digest(path)

    result = {
        "paper": paper,
        "report_sha256": digest(report_path),
        "citation_pairs": len(pairs),
        "unique_citation_ids": len(set(raw_ref_markers)),
        "reference_ids": len(refs),
        "source_verification_rows": len(sources),
        "anchor_none_pairs": sum(kind == "none" and value == "" for _, kind, value in pairs),
        "claim_intents": len(manifest["claims"]),
        "planned_ref_occurrences": len(planned),
        "claim_negative_constraints": claim_constraints,
        "manifest_negative_constraints": manifest_constraints,
        "phase5_output_sha256": role_hashes,
        "checks": 13 + (12 if phase == "full" else 0),
        "failures": failures,
    }
    return result, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("inputs", "full"), default="inputs")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    all_failures: list[str] = []
    results = []
    for row in freeze["papers"]:
        result, failures = audit_paper(row, args.phase)
        results.append(result)
        all_failures.extend(failures)

    route_a = digest(ROOT / "skills" / "route-a-evaluator.md")
    route_b = digest(ROOT / "skills" / "route-b-evaluator.md")
    if route_a != freeze["roadmaps"]["route_a_sha256"]:
        all_failures.append("Route-A roadmap hash mismatch")
    if route_b != freeze["roadmaps"]["route_b_sha256"]:
        all_failures.append("Route-B roadmap hash mismatch")

    payload = {
        "schema": "round10-stage1-phase5-deterministic-audit/1.0",
        "phase": args.phase,
        "verdict": "PASS" if not all_failures else "FAIL",
        "papers": results,
        "totals": {
            "papers": len(results),
            "citation_pairs": sum(r["citation_pairs"] for r in results),
            "unique_citation_ids": sum(r["unique_citation_ids"] for r in results),
            "reference_ids": sum(r["reference_ids"] for r in results),
            "source_verification_rows": sum(r["source_verification_rows"] for r in results),
            "anchor_none_pairs": sum(r["anchor_none_pairs"] for r in results),
            "claim_intents": sum(r["claim_intents"] for r in results),
            "checks": sum(r["checks"] for r in results) + 2,
            "failures": len(all_failures),
        },
        "failures": all_failures,
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        totals = payload["totals"]
        print(
            f"{payload['verdict']} phase={args.phase} papers={totals['papers']} "
            f"checks={totals['checks']} failures={totals['failures']} "
            f"citation_pairs={totals['citation_pairs']} "
            f"anchor_none={totals['anchor_none_pairs']}"
        )
        for message in all_failures:
            print(f"FAILURE {message}")
    return 0 if not all_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
