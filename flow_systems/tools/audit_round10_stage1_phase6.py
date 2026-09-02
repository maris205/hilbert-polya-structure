#!/usr/bin/env python3
"""Deterministic boundary audit for Round-10 Stage-1 Phase-6 revision.

The audit is deliberately non-scientific.  It verifies immutable inputs,
pre-prose ClaimIntent manifests, canonical-manuscript guards, closed citations,
revision-finding accounting, required disclosure/boundary language, and (in
``full`` mode) independent rechecks and per-paper checkpoints.  It cannot
judge mathematical truth, novelty, passage-level source support, or whether a
prospective proof/certificate architecture will work.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PHASE6_FREEZE = ROOT / "BATCH_ROUND10_STAGE1_PHASE6_INPUT_FREEZE.json"
PHASE5_FREEZE = ROOT / "BATCH_ROUND10_STAGE1_PHASE5_INPUT_FREEZE.json"
CANONICAL_GUARD = ROOT / "BATCH_ROUND10_STAGE1_PHASE6_CANONICAL_GUARD.json"

PHASE6_BINDINGS = {
    "BATCH_ROUND10_STAGE1_PHASE6_AUTHORIZATION_20260902.txt":
        "b516a3f1c0b362a77ba7b5963375492d7bab73c746cb458086feb48638739a85",
    "BATCH_ROUND10_STAGE1_PHASE6_REVISION_CONTRACT.md":
        "9c5ca5807b174a9aae8d473ca265324312acd13c4e4312dcb3d0bd0dd379ba12",
    "BATCH_ROUND10_STAGE1_PHASE6_INPUT_FREEZE.json":
        "d0d10db04cd8fe00b2ec35da2c8b87da6a1c8529378b24b1e8b1f12e72d0e2f8",
    "BATCH_ROUND10_STAGE1_PHASE6_START.md":
        "8dcec94b9616665c6d01f303819d61a506ef9580aa708b36cd8c40712aba4372",
    "BATCH_ROUND10_STAGE1_PHASE6_MANIFEST_FREEZE.md":
        "6d64f0bdfcb9d991e77ac21464d4cfdc73327671118632ae34cadacb9c1f3039",
    "BATCH_ROUND10_STAGE1_PHASE6_CANONICAL_GUARD.json":
        "47f8bec93a5743d73d8208c46de655e4ca10e08e694385086362d9edcba88c06",
    "BATCH_ROUND10_STAGE1_PHASE5_INPUT_FREEZE.json":
        "1abaa50df0b81282092641b2609d278dd4de406895bb45c7e7831dd09550f04c",
}

MANIFEST_SHA256 = {
    "P29": "63596d7c9cb8a1f9f381d7649eb073a2cc9726fd526e092137b6e2cbdf3b1335",
    "P30": "57f330272bb234f1610828f98d855675009dc90f8437ffebdffb0f6e021e8fba",
    "P31": "b9a61badd7e6d05c31ae0ce4f81adfa6ea1c40269afe37de9a620c763597aa38",
    "P32": "8986b9d38f5d561e1eb7fe9aeca51e110bee21de66f4b455307d40909ba9a815",
    "P33": "83500193f234eb5c2681ffd4c6bb3948f107adede9714fc1d1bc75ead2106191",
}

EXPECTED_CITATION_PAIRS = {"P29": 22, "P30": 26, "P31": 22, "P32": 26, "P33": 48}
ROLE_FILES = {
    "phase5_editorial_sha256": "stage1_phase5_editorial_review.md",
    "phase5_ethics_sha256": "stage1_phase5_ethics_review.md",
    "phase5_citation_sha256": "stage1_phase5_citation_integrity_review.md",
    "phase5_da_sha256": "stage1_phase5_devils_advocate.md",
    "phase5_synthesis_sha256": "stage1_phase5_review_synthesis.md",
    "phase5_checkpoint_sha256": "stage1_phase5_checkpoint.md",
}
PAIR_RE = re.compile(r"<!--ref:([^>]+)--><!--anchor:([^:>]+):([^>]*)-->")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_failure(failures: list[str], message: str) -> None:
    failures.append(message)


def check_hash(path: Path, expected: str, failures: list[str], label: str) -> None:
    if not path.is_file():
        add_failure(failures, f"{label}: missing {path.relative_to(ROOT)}")
    elif digest(path) != expected:
        add_failure(failures, f"{label}: SHA-256 mismatch {path.relative_to(ROOT)}")


def reference_body(text: str) -> str | None:
    match = re.search(r"(?ms)^## References\s*$\n(.*?)(?=^## |\Z)", text)
    return match.group(1).strip() if match else None


def reference_ids(text: str) -> list[str]:
    body = reference_body(text)
    if body is None:
        return []
    return re.findall(r"(?m)^- \[([^\]]+)\] ", body)


def source_ids(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return [row["source_id"] for row in csv.DictReader(handle, delimiter="\t")]


def stable_finding_ids(paper: str, role_texts: list[str]) -> set[str]:
    pattern = re.compile(rf"\b{re.escape(paper)}-(?:EIC|ETH|CIT|DA)-\d{{3}}\b")
    return set().union(*(set(pattern.findall(text)) for text in role_texts))


def word_count(text: str) -> int:
    # Markdown/control comments do not need journal-precise tokenization here;
    # this is only a coarse completeness guard.
    return len(re.findall(r"\b[\w][\w'\-’]*\b", text, flags=re.UNICODE))


def audit_inputs(row6: dict, row5: dict, guard: dict) -> tuple[dict, list[str]]:
    paper = row6["paper"]
    base = ROOT / "papers" / row6["slug"]
    notes = base / "notes"
    failures: list[str] = []

    frozen_paths = {
        notes / "stage1_phase4_research_report.md": row6["phase4_report_sha256"],
        notes / "stage1_phase4_claim_intent_manifest.json": row6["phase4_manifest_sha256"],
        notes / "stage1_phase2_source_verification.md": row5["source_verification_md_sha256"],
        notes / "stage1_phase2_source_verification.tsv": row5["source_verification_tsv_sha256"],
    }
    for key, filename in ROLE_FILES.items():
        frozen_paths[notes / filename] = row6[key]
    for path, expected in frozen_paths.items():
        check_hash(path, expected, failures, paper)

    manifest_path = notes / "stage1_phase6_claim_intent_manifest.json"
    check_hash(manifest_path, MANIFEST_SHA256[paper], failures, paper)
    manifest: dict = {}
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            add_failure(failures, f"{paper}: invalid Phase-6 manifest: {exc}")
    claims = manifest.get("claims", [])
    constraints = manifest.get("manifest_negative_constraints", [])
    claim_ids = [claim.get("claim_id") for claim in claims]
    if len(claims) != 8 or len(set(claim_ids)) != 8:
        add_failure(failures, f"{paper}: Phase-6 manifest must contain 8 unique claim IDs")
    if len(constraints) != 6:
        add_failure(failures, f"{paper}: Phase-6 manifest must contain 6 manifest constraints")
    if manifest.get("phase") != "stage1_phase6_revision":
        add_failure(failures, f"{paper}: wrong Phase-6 manifest phase")
    if manifest.get("predecessor_manifest_sha256") != row6["phase4_manifest_sha256"]:
        add_failure(failures, f"{paper}: manifest predecessor hash mismatch")

    verification_path = notes / "stage1_phase2_source_verification.tsv"
    sources = source_ids(verification_path) if verification_path.is_file() else []
    planned = [ref for claim in claims for ref in claim.get("planned_refs", [])]
    if any(ref not in set(sources) for ref in planned):
        add_failure(failures, f"{paper}: Phase-6 planned_refs contains unknown source ID")

    phase4_path = notes / "stage1_phase4_research_report.md"
    phase4_text = phase4_path.read_text(encoding="utf-8") if phase4_path.is_file() else ""
    phase4_pairs = PAIR_RE.findall(phase4_text)
    if len(phase4_pairs) != EXPECTED_CITATION_PAIRS[paper]:
        add_failure(failures, f"{paper}: frozen Phase-4 citation-pair count drift")
    if any(kind != "none" or locator != "" for _, kind, locator in phase4_pairs):
        add_failure(failures, f"{paper}: frozen Phase-4 report has a non-none locator")
    if set(reference_ids(phase4_text)) != set(sources):
        add_failure(failures, f"{paper}: frozen Phase-4 reference/source closure failed")

    for field, expected_field in (
        ("manuscript_path", "manuscript_sha256"),
        ("bibliography_path", "bibliography_sha256"),
    ):
        path = ROOT / guard[field]
        check_hash(path, guard[expected_field], failures, paper)

    role_texts = []
    for filename in ROLE_FILES.values():
        if "review_synthesis" in filename or "checkpoint" in filename:
            continue
        path = notes / filename
        if path.is_file():
            role_texts.append(path.read_text(encoding="utf-8"))
    finding_ids = stable_finding_ids(paper, role_texts)

    result = {
        "paper": paper,
        "claim_intents": len(claims),
        "manifest_constraints": len(constraints),
        "planned_ref_occurrences": len(planned),
        "frozen_source_ids": len(set(sources)),
        "phase4_citation_pairs": len(phase4_pairs),
        "stable_finding_ids": len(finding_ids),
        "input_checks": 24,
        "input_failures": len(failures),
    }
    return result, failures


def check_disclosure(paper: str, report: str, failures: list[str]) -> None:
    required = (
        "OpenAI Codex",
        "GPT-5 model family",
        "2026-09-02 UTC",
        "exact backend snapshot/build was not exposed",
        "Liang Wang",
        "responsible human author",
        "AI-assisted",
    )
    lowered = report.lower()
    for phrase in required:
        if phrase.lower() not in lowered:
            add_failure(failures, f"{paper}: missing disclosure phrase `{phrase}`")
    if "full-text" not in lowered or not re.search(
        r"(?:did not|does not|not|no)\b[^.\n]{0,100}\bfull-text", lowered
    ):
        add_failure(failures, f"{paper}: missing explicit negative human full-text boundary")


def check_revision_dispositions(
    paper: str, text: str, expected_ids: set[str], failures: list[str], label: str
) -> None:
    present = stable_finding_ids(paper, [text])
    missing = sorted(expected_ids - present)
    extra = sorted(present - expected_ids)
    if missing:
        add_failure(failures, f"{paper}: {label} missing finding IDs: {', '.join(missing)}")
    if extra:
        add_failure(failures, f"{paper}: {label} has unknown finding IDs: {', '.join(extra)}")
    allowed = (
        "resolved",
        "partially addressed",
        "acknowledged limitation",
        "retained pass",
        "no action",
        "confirmed",
    )
    lines = text.splitlines()
    for finding in sorted(expected_ids):
        matching = [line.lower() for line in lines if finding in line]
        if not any(any(term in line for term in allowed) for line in matching):
            add_failure(failures, f"{paper}: {label} lacks categorical disposition on line for {finding}")


def audit_revision(row6: dict) -> tuple[dict, list[str]]:
    paper = row6["paper"]
    notes = ROOT / "papers" / row6["slug"] / "notes"
    failures: list[str] = []
    report_path = notes / "stage1_phase6_final_report.md"
    log_path = notes / "stage1_phase6_revision_log.md"
    if not report_path.is_file():
        add_failure(failures, f"{paper}: missing Phase-6 final report")
    if not log_path.is_file():
        add_failure(failures, f"{paper}: missing Phase-6 revision log")
    if failures:
        return {
            "paper": paper,
            "report_words": 0,
            "citation_pairs": 0,
            "finding_ids_in_log": 0,
            "revision_checks": 2,
            "revision_failures": len(failures),
        }, failures

    report = report_path.read_text(encoding="utf-8")
    log = log_path.read_text(encoding="utf-8")
    phase4 = (notes / "stage1_phase4_research_report.md").read_text(encoding="utf-8")
    pairs = PAIR_RE.findall(report)
    raw_markers = re.findall(r"<!--ref:([^>]+)-->", report)
    refs = reference_ids(report)
    source_set = set(source_ids(notes / "stage1_phase2_source_verification.tsv"))
    words = word_count(report)

    if not 3000 <= words <= 8000:
        add_failure(failures, f"{paper}: report word count {words} outside 3000–8000")
    if len(raw_markers) != len(pairs):
        add_failure(failures, f"{paper}: unpaired Phase-6 citation marker")
    if len(pairs) != EXPECTED_CITATION_PAIRS[paper]:
        add_failure(
            failures,
            f"{paper}: citation pairs {len(pairs)} != inherited {EXPECTED_CITATION_PAIRS[paper]}",
        )
    if any(kind != "none" or locator != "" for _, kind, locator in pairs):
        add_failure(failures, f"{paper}: Phase-6 report contains a non-none locator")
    if set(raw_markers) != source_set:
        add_failure(failures, f"{paper}: Phase-6 prose citation/source ID closure failed")
    if set(refs) != source_set or len(refs) != len(set(refs)):
        add_failure(failures, f"{paper}: Phase-6 References/source closure failed")
    if reference_body(report) != reference_body(phase4):
        add_failure(failures, f"{paper}: References block differs from frozen Phase-4 block")

    required_headings = (
        "Abstract",
        "Introduction",
        "Method",
        "Limitation",
        "Conclusion",
        "AI Disclosure",
        "References",
        "Declaration",
    )
    headings = "\n".join(re.findall(r"(?m)^#{1,4}\s+(.+)$", report)).lower()
    for heading in required_headings:
        if heading.lower() not in headings:
            add_failure(failures, f"{paper}: missing report heading containing `{heading}`")
    check_disclosure(paper, report, failures)

    lowered = report.lower()
    for phrase in ("claim-to-passage", "inconclusive", "unassigned", "route b"):
        if phrase not in lowered:
            add_failure(failures, f"{paper}: missing boundary phrase `{phrase}`")
    if "a2" not in lowered or "0/1" not in lowered:
        add_failure(failures, f"{paper}: missing explicit arithmetic A2 0/1 boundary")
    if not re.search(r"(?:no|not|none|without)\b[^.\n]{0,100}\b(?:new retrieval|scientific execution|experiment)", lowered):
        add_failure(failures, f"{paper}: missing negative retrieval/scientific-execution statement")

    role_texts = []
    for filename in ROLE_FILES.values():
        if "review_synthesis" in filename or "checkpoint" in filename:
            continue
        role_texts.append((notes / filename).read_text(encoding="utf-8"))
    expected_ids = stable_finding_ids(paper, role_texts)
    check_revision_dispositions(paper, log, expected_ids, failures, "revision log")
    if MANIFEST_SHA256[paper] not in log:
        add_failure(failures, f"{paper}: revision log lacks exact Phase-6 manifest binding")
    if row6["phase4_report_sha256"] not in log:
        add_failure(failures, f"{paper}: revision log lacks frozen Phase-4 report binding")

    result = {
        "paper": paper,
        "report_words": words,
        "report_sha256": digest(report_path),
        "revision_log_sha256": digest(log_path),
        "citation_pairs": len(pairs),
        "unique_citation_ids": len(set(raw_markers)),
        "anchor_none_pairs": sum(kind == "none" and locator == "" for _, kind, locator in pairs),
        "finding_ids_expected": len(expected_ids),
        "finding_ids_in_log": len(stable_finding_ids(paper, [log])),
        "revision_checks": 24 + len(expected_ids),
        "revision_failures": len(failures),
    }
    return result, failures


def audit_full(row6: dict, revision: dict) -> tuple[dict, list[str]]:
    paper = row6["paper"]
    notes = ROOT / "papers" / row6["slug"] / "notes"
    failures: list[str] = []
    recheck_path = notes / "stage1_phase6_recheck.md"
    checkpoint_path = notes / "stage1_phase6_checkpoint.md"
    if not recheck_path.is_file():
        add_failure(failures, f"{paper}: missing independent Phase-6 recheck")
    if not checkpoint_path.is_file():
        add_failure(failures, f"{paper}: missing Phase-6 checkpoint")
    if failures:
        return {"paper": paper, "full_checks": 2, "full_failures": len(failures)}, failures

    recheck = recheck_path.read_text(encoding="utf-8")
    checkpoint = checkpoint_path.read_text(encoding="utf-8")
    role_texts = []
    for filename in ROLE_FILES.values():
        if "review_synthesis" in filename or "checkpoint" in filename:
            continue
        role_texts.append((notes / filename).read_text(encoding="utf-8"))
    expected_ids = stable_finding_ids(paper, role_texts)
    check_revision_dispositions(paper, recheck, expected_ids, failures, "independent recheck")

    expected_hashes = {
        "manifest": MANIFEST_SHA256[paper],
        "report": revision.get("report_sha256", ""),
        "revision log": revision.get("revision_log_sha256", ""),
        "recheck": digest(recheck_path),
    }
    for label, expected in expected_hashes.items():
        if not expected or expected not in checkpoint:
            add_failure(failures, f"{paper}: checkpoint lacks exact {label} hash")
    for label in ("report", "revision log"):
        expected = expected_hashes[label]
        if not expected or expected not in recheck:
            add_failure(failures, f"{paper}: recheck lacks exact {label} hash")
    if "PASS" not in recheck:
        add_failure(failures, f"{paper}: independent recheck has no PASS verdict")

    result = {
        "paper": paper,
        "recheck_sha256": digest(recheck_path),
        "checkpoint_sha256": digest(checkpoint_path),
        "finding_ids_in_recheck": len(stable_finding_ids(paper, [recheck])),
        "full_checks": 8 + len(expected_ids),
        "full_failures": len(failures),
    }
    return result, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("inputs", "revision", "full"), default="inputs")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    for rel, expected in PHASE6_BINDINGS.items():
        check_hash(ROOT / rel, expected, failures, "batch")

    freeze6 = json.loads(PHASE6_FREEZE.read_text(encoding="utf-8"))
    freeze5 = json.loads(PHASE5_FREEZE.read_text(encoding="utf-8"))
    canonical = json.loads(CANONICAL_GUARD.read_text(encoding="utf-8"))
    rows5 = {row["paper"]: row for row in freeze5["papers"]}
    guards = {row["paper"]: row for row in canonical["papers"]}

    phase5_batch_paths = {
        "BATCH_ROUND10_STAGE1_PHASE5_CHECKPOINT.md": freeze6["phase5_batch"]["checkpoint_sha256"],
        "BATCH_ROUND10_STAGE1_PHASE5_AUDIT_RECEIPT.json": freeze6["phase5_batch"]["audit_receipt_sha256"],
        "BATCH_ROUND10_STAGE1_PHASE5_INDEPENDENT_AUDIT.md": freeze6["phase5_batch"]["independent_audit_sha256"],
    }
    for rel, expected in phase5_batch_paths.items():
        check_hash(ROOT / rel, expected, failures, "Phase-5 batch")

    if digest(ROOT / "skills/route-a-evaluator.md") != freeze6["roadmaps"]["route_a_sha256"]:
        add_failure(failures, "Route-A roadmap SHA-256 mismatch")
    if digest(ROOT / "skills/route-b-evaluator.md") != freeze6["roadmaps"]["route_b_sha256"]:
        add_failure(failures, "Route-B roadmap SHA-256 mismatch")

    input_results = []
    revision_results = []
    full_results = []
    for row6 in freeze6["papers"]:
        paper = row6["paper"]
        input_result, paper_failures = audit_inputs(row6, rows5[paper], guards[paper])
        input_results.append(input_result)
        failures.extend(paper_failures)
        if args.phase in ("revision", "full"):
            revision_result, paper_failures = audit_revision(row6)
            revision_results.append(revision_result)
            failures.extend(paper_failures)
            if args.phase == "full":
                full_result, paper_failures = audit_full(row6, revision_result)
                full_results.append(full_result)
                failures.extend(paper_failures)

    if sum(item["stable_finding_ids"] for item in input_results) != 82:
        add_failure(failures, "batch stable finding count is not 82")
    if sum(item["phase4_citation_pairs"] for item in input_results) != 144:
        add_failure(failures, "batch frozen citation-pair count is not 144")
    if sum(item["claim_intents"] for item in input_results) != 40:
        add_failure(failures, "batch Phase-6 ClaimIntent count is not 40")

    checks = len(PHASE6_BINDINGS) + len(phase5_batch_paths) + 2
    checks += sum(item["input_checks"] for item in input_results) + 3
    checks += sum(item.get("revision_checks", 0) for item in revision_results)
    checks += sum(item.get("full_checks", 0) for item in full_results)
    payload = {
        "schema": "round10-stage1-phase6-deterministic-audit/1.0",
        "phase": args.phase,
        "verdict": "PASS" if not failures else "FAIL",
        "inputs": input_results,
        "revision": revision_results,
        "full": full_results,
        "totals": {
            "papers": len(input_results),
            "checks": checks,
            "failures": len(failures),
            "claim_intents": sum(item["claim_intents"] for item in input_results),
            "stable_finding_ids": sum(item["stable_finding_ids"] for item in input_results),
            "citation_pairs": sum(item.get("citation_pairs", 0) for item in revision_results),
            "anchor_none_pairs": sum(item.get("anchor_none_pairs", 0) for item in revision_results),
            "report_words": sum(item.get("report_words", 0) for item in revision_results),
        },
        "failures": failures,
        "non_scientific_scope": (
            "PASS verifies structure and immutable boundaries only; it is not mathematical, "
            "novelty, passage-faithfulness, Route, or publication acceptance evidence."
        ),
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        totals = payload["totals"]
        print(
            f"{payload['verdict']} phase={args.phase} papers={totals['papers']} "
            f"checks={totals['checks']} failures={totals['failures']} "
            f"claim_intents={totals['claim_intents']} findings={totals['stable_finding_ids']} "
            f"citation_pairs={totals['citation_pairs']} words={totals['report_words']}"
        )
        for message in failures:
            print(f"FAILURE {message}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
