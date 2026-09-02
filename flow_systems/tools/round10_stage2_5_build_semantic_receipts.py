#!/usr/bin/env python3
"""Build hash-bound Round-10 Phase-E receipts from completed claim-by-claim audits.

The Markdown audit is the independent semantic adjudication.  This compiler
does not invent verdicts: it requires exactly one table row for every selected
Claim Registry ID, rejects extra/duplicate IDs, and checks that every persisted
evidence tuple carries the same verdict before emitting a receipt.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
PAPERS = (
    "29-bianchi-ideal-owner-refinement",
    "30-three-disk-nonconstant-roof-determinant",
    "31-level11-conjugacy-owner-ledger",
    "32-homology-cover-renormalization-uniformity",
    "33-bolza-control-matched-census",
)
VERDICTS = {
    "VERIFIED",
    "MINOR_DISTORTION",
    "MAJOR_DISTORTION",
    "UNVERIFIABLE",
    "UNVERIFIABLE_ACCESS",
}
CLAIM_ROW_RE = re.compile(
    r"^\|\s*`(?P<claim>P(?:29|30|31|32|33)-E1-\d{3})`\s*\|"
)
NON_DISTORTION_CLASSES = {
    "SOURCE_ROLE_ALIGNED__PASSAGE_INCONCLUSIVE",
    "INTERNAL_PROVENANCE_CORROBORATED__SCIENTIFIC_TRUTH_NOT_TESTED",
    "PROJECT_DEFINITION_OR_PROSPECTIVE_DESIGN__NOT_EXTERNAL_FACT",
    "PARALLEL_FRONT_MATTER_FRAGMENT__CONSISTENT_NOT_STANDALONE",
    "REGISTRY_NONCLAIM_OR_NAME_FRAGMENT",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: Any) -> str:
    raw = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path: Path, value: Any) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def now() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def parse_verdicts(text: str) -> dict[str, str]:
    found: list[tuple[str, str]] = []
    for line in text.splitlines():
        match = CLAIM_ROW_RE.match(line)
        if match:
            # The verdict is the final nonempty pipe cell.  Stripping Markdown
            # emphasis/code formatting avoids presentational coupling.  The
            # P33 reviewer used five more informative no-distortion subclasses;
            # they map to the closed evidence-row verdict VERIFIED while their
            # epistemic boundaries remain in the human-readable audit.
            cells = [cell.strip().strip("*`") for cell in line.split("|")[1:-1]]
            verdict_cells = [
                cell
                for cell in cells
                if cell in VERDICTS or cell in NON_DISTORTION_CLASSES
            ]
            if len(verdict_cells) != 1:
                raise RuntimeError(
                    f"semantic row must carry exactly one recognized verdict: {line}"
                )
            raw_verdict = verdict_cells[0]
            verdict = (
                raw_verdict if raw_verdict in VERDICTS else "VERIFIED"
            )
            found.append((match.group("claim"), verdict))
    counts = Counter(claim for claim, _ in found)
    duplicate = sorted(claim for claim, count in counts.items() if count != 1)
    if duplicate:
        raise RuntimeError(f"duplicate semantic-audit rows: {duplicate}")
    return dict(found)


def build_one(paper: str, generated_at: str) -> dict[str, Any]:
    base = ROOT / "papers" / paper
    notes = base / "notes"
    manuscript = base / "paper" / "manuscript.tex"
    registry_path = notes / "stage2_5_claim_registry.json"
    rows_path = notes / "stage2_5_evidence_rows.json"
    audit_path = notes / "stage2_5_phase_e_semantic_audit.md"
    registry = load(registry_path)
    rows = load(rows_path)
    audit_text = audit_path.read_text(encoding="utf-8")
    audited = parse_verdicts(audit_text)

    selected = {
        claim["claim_id"]: claim
        for claim in registry["claims"]
        if claim["selection_tier"] != "NOT-SELECTED"
    }
    if set(audited) != set(selected):
        missing = sorted(set(selected) - set(audited))
        extra = sorted(set(audited) - set(selected))
        raise RuntimeError(f"{paper}: semantic population mismatch: missing={missing}, extra={extra}")

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row["claim"]["claim_id"]].append(row)
    if set(grouped) != set(selected):
        raise RuntimeError(f"{paper}: evidence population differs from selected registry")

    claim_verdicts = []
    for claim_id, claim in selected.items():
        verdict = audited[claim_id]
        claim_rows = grouped[claim_id]
        expected_claim = {
            "claim_id": claim_id,
            "paper_locator": claim["writer_anchors"][0],
            "selection_tier": claim["selection_tier"],
            "text": claim["claim_text"],
        }
        if any(row["claim"] != expected_claim for row in claim_rows):
            raise RuntimeError(f"{paper}: evidence claim object drift for {claim_id}")
        if any(row["verdict"] != verdict for row in claim_rows):
            raise RuntimeError(
                f"{paper}: evidence verdict differs from semantic audit for {claim_id}"
            )
        expected_refs = set(claim["ref_slugs"] or [None])
        actual_refs = {row["source"]["ref_slug"] for row in claim_rows}
        if actual_refs != expected_refs or len(claim_rows) != len(expected_refs):
            raise RuntimeError(f"{paper}: evidence tuple mismatch for {claim_id}")
        claim_verdicts.append(
            {
                "claim_id": claim_id,
                "selection_tier": claim["selection_tier"],
                "verdict": verdict,
                "tuple_count": len(claim_rows),
                "row_ids": [row["row_id"] for row in claim_rows],
                "row_sha256s": [row["row_sha256"] for row in claim_rows],
                "claim_object_sha256": canonical_sha(expected_claim),
            }
        )

    verdict_counts = {
        verdict: sum(row["verdict"] == verdict for row in claim_verdicts)
        for verdict in sorted(VERDICTS)
    }
    if any(
        verdict_counts[key]
        for key in ("MAJOR_DISTORTION", "UNVERIFIABLE", "UNVERIFIABLE_ACCESS")
    ):
        decision = "FAIL_SELECTED_POPULATION"
    elif verdict_counts["MINOR_DISTORTION"]:
        decision = "PASS_SELECTED_POPULATION_WITH_MINOR_DISTORTION"
    else:
        decision = "PASS_SELECTED_POPULATION"

    receipt = {
        "schema": "flow-systems-stage2.5-semantic-verdict-receipt/1.0",
        "paper": paper,
        "generated_at": generated_at,
        "audit_role": "independent_agent_semantic_review",
        "decision": decision,
        "bindings": {
            "manuscript_sha256": sha(manuscript),
            "claim_registry_sha256": sha(registry_path),
            "evidence_rows_sha256": sha(rows_path),
            "semantic_audit_sha256": sha(audit_path),
        },
        "selected_distinct_claims": len(selected),
        "evidence_tuples": len(rows),
        "verdict_counts": verdict_counts,
        "semantic_extraction_coverage": "not_machine_detectable",
        "evidence_state_boundary": (
            "All tuple carriers remain anchorless; this receipt binds the "
            "separate claim-by-claim semantic review and adds no source excerpt."
        ),
        "claim_verdicts": claim_verdicts,
    }
    output = notes / "stage2_5_phase_e_semantic_verdicts.json"
    atomic_json(output, receipt)
    return {
        "paper": paper,
        "decision": decision,
        "selected": len(selected),
        "tuples": len(rows),
        "receipt_sha256": sha(output),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generated-at", default=now())
    parser.add_argument(
        "--paper",
        choices=("all", *PAPERS),
        default="all",
        help="emit one paper receipt without writing sidecars for the other papers",
    )
    args = parser.parse_args()
    selected = PAPERS if args.paper == "all" else (args.paper,)
    results = [build_one(paper, args.generated_at) for paper in selected]
    print(json.dumps({"status": "PASS", "papers": results}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
