#!/usr/bin/env python3
"""Strict registry-to-source-tuple replay for P67--P71 Round-1 Phase E.

This validator closes the gap that standalone evidence-row schema validation
cannot see: exact tuple coverage against the selected Claim Registry entries.
It requires positive, source-bound excerpts for cited-source tuples and an
explicit anchorless empty row for selected claims with no cited source.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_MODULE = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.27/skills/"
    "academic-research-suite/ars/scripts/evidence_rows.py"
)
PAPERS = {
    "P67": "67-multiplicative-plaquette-matroid-complexity",
    "P68": "68-complete-bipartite-homshift-conjugacies",
    "P69": "69-orientation-sensitive-surface-flat-sft",
    "P70": "70-weighted-heisenberg-congruence-nullities",
    "P71": "71-zip-shift-degree-pressure",
}
POSITIVE_STATES = {"verified_exact_match", "agent_extracted"}


def load_runtime():
    spec = importlib.util.spec_from_file_location("ars_evidence_rows", EVIDENCE_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {EVIDENCE_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_tuples(registry: dict) -> list[tuple[str, str | None]]:
    tuples: list[tuple[str, str | None]] = []
    for claim in registry["claims"]:
        if claim["selection_tier"] == "NOT-SELECTED":
            continue
        refs = claim.get("ref_slugs", [])
        if refs:
            tuples.extend((claim["claim_id"], ref) for ref in refs)
        else:
            tuples.append((claim["claim_id"], None))
    return tuples


def validate_paper(runtime, paper_id: str, directory: str) -> dict[str, int]:
    stage = ROOT / "papers" / directory / "stage2_5"
    registry = json.loads((stage / "claim_registry_round1.json").read_text(encoding="utf-8"))
    rows = json.loads((stage / "evidence_rows_round1.json").read_text(encoding="utf-8"))
    sources = json.loads((stage / "evidence_source_map_round1.json").read_text(encoding="utf-8"))
    expected = expected_tuples(registry)
    actual = [(row["claim"]["claim_id"], row["source"]["ref_slug"]) for row in rows]
    if actual != expected:
        raise ValueError(f"{paper_id}: tuple sequence mismatch\nexpected={expected}\nactual={actual}")

    selected = {
        claim["claim_id"]: claim
        for claim in registry["claims"]
        if claim["selection_tier"] != "NOT-SELECTED"
    }
    external = 0
    anchorless = 0
    row_ids: set[str] = set()
    for row in rows:
        row_id = row["row_id"]
        if row_id in row_ids:
            raise ValueError(f"{paper_id}: duplicate row_id {row_id}")
        row_ids.add(row_id)
        claim = selected[row["claim"]["claim_id"]]
        if row["claim"]["text"] != claim["claim_text"]:
            raise ValueError(f"{paper_id} {row_id}: claim text drift")
        if row["claim"]["selection_tier"] != claim["selection_tier"]:
            raise ValueError(f"{paper_id} {row_id}: selection tier drift")
        if row["verdict"] != "VERIFIED":
            raise ValueError(
                f"{paper_id} {row_id}: non-clean Phase-E verdict {row['verdict']}"
            )
        ref_slug = row["source"]["ref_slug"]
        if ref_slug is None:
            if row["anchor"]["kind"] != "none" or row["excerpt"]["state"] != "anchorless":
                raise ValueError(f"{paper_id} {row_id}: no-ref tuple is not explicit anchorless")
            runtime.validate(row, None)
            anchorless += 1
        else:
            if ref_slug not in sources:
                raise ValueError(f"{paper_id} {row_id}: missing held source {ref_slug}")
            if row["excerpt"]["state"] not in POSITIVE_STATES or not row["excerpt"]["text"]:
                raise ValueError(f"{paper_id} {row_id}: cited-source tuple lacks positive excerpt")
            runtime.validate(row, sources[ref_slug])
            external += 1

    if len({row["claim"]["claim_id"] for row in rows}) != len(selected):
        raise ValueError(f"{paper_id}: selected distinct-claim coverage mismatch")
    return {
        "claims": len(selected),
        "rows": len(rows),
        "external": external,
        "anchorless": anchorless,
    }


def main() -> int:
    runtime = load_runtime()
    totals = {"claims": 0, "rows": 0, "external": 0, "anchorless": 0}
    for paper_id, directory in PAPERS.items():
        result = validate_paper(runtime, paper_id, directory)
        for key in totals:
            totals[key] += result[key]
        print(
            f"{paper_id}: PASS claims={result['claims']} rows={result['rows']} "
            f"external={result['external']} anchorless={result['anchorless']}"
        )
    print(
        "TOTAL: PASS "
        f"claims={totals['claims']} rows={totals['rows']} "
        f"external={totals['external']} anchorless={totals['anchorless']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
