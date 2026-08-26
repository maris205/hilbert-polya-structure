#!/usr/bin/env python3
"""Build exact-byte Stage-2.5 claim registries from audited semantic selections.

The semantic selections below were made from the citation-preserving Markdown
audit views.  The mechanically detected citation/quantitative candidate
sentences are then joined so that the bounded E1.1 coverage checker can replay
the exact spans.  A clean E1.1 report does not establish semantic completeness.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPERS = {
    "P67": (
        "67-multiplicative-plaquette-matroid-complexity",
        [23, 24, 26, 27, 29, 30, 32, 33, 37, 39, 40, 42, 44, 46, 262, 272],
    ),
    "P68": (
        "68-complete-bipartite-homshift-conjugacies",
        [11, 13, 15, 17, 30, 36, 38, 50, 61, 63, 65, 67, 89, 91, 93, 95, 111, 113, 114, 115, 139],
    ),
    "P69": (
        "69-orientation-sensitive-surface-flat-sft",
        [8, 25, 36, 38, 39, 40, 44, 45, 46, 47, 48, 113, 135, 137, 185, 219, 221, 292, 293, 295],
    ),
    "P70": (
        "70-weighted-heisenberg-congruence-nullities",
        [10, 14, 16, 18, 29, 34, 46, 49, 50, 52, 68, 85, 104, 111, 119, 123, 128, 144, 148, 150, 178, 202],
    ),
    "P71": (
        "71-zip-shift-degree-pressure",
        [9, 10, 12, 14, 16, 18, 20, 32, 46, 64, 65, 71, 86, 97, 112, 119, 121, 123, 125, 127, 129, 173, 197, 227, 229, 235],
    ),
}

CITE_KEY = re.compile(r"@([A-Za-z0-9_.:-]+)")


def byte_offset(text: str, char_offset: int) -> int:
    return len(text[:char_offset].encode("utf-8"))


def section_at(lines: list[str], line_no: int) -> str | None:
    section = None
    for idx in range(min(line_no, len(lines))):
        if lines[idx].startswith("# "):
            section = lines[idx][2:].strip()
    return section


def add_or_upgrade(claims: list[dict], claim: dict) -> None:
    span = (claim["draft_span"]["start_byte"], claim["draft_span"]["end_byte"])
    for existing in claims:
        old = (existing["draft_span"]["start_byte"], existing["draft_span"]["end_byte"])
        if old != span:
            continue
        if claim["selection_tier"] == "HIGH-IMPACT":
            existing["selection_tier"] = "HIGH-IMPACT"
            existing["high_impact_basis"] = claim["high_impact_basis"]
        existing["claim_kinds"] = sorted(set(existing["claim_kinds"] + claim["claim_kinds"]))
        existing["ref_slugs"] = sorted(set(existing["ref_slugs"] + claim["ref_slugs"]))
        existing["writer_anchors"] = sorted(set(existing["writer_anchors"] + claim["writer_anchors"]))
        return
    claims.append(claim)


def main() -> int:
    for paper_id, (directory, semantic_lines) in PAPERS.items():
        stage = ROOT / "papers" / directory / "stage2_5"
        draft_path = stage / "draft_for_claim_registry.md"
        probe_path = stage / "claim_registry_candidate_probe.json"
        draft_raw = draft_path.read_bytes()
        draft = draft_raw.decode("utf-8")
        lines = draft.splitlines(keepends=True)
        probe = json.loads(probe_path.read_text(encoding="utf-8"))
        claims: list[dict] = []

        for idx, candidate in enumerate(probe["candidates"], start=1):
            quantitative = "quantitative_sentence" in candidate["candidate_kinds"]
            add_or_upgrade(
                claims,
                {
                    "claim_id": f"{paper_id}-CAND-{idx:03d}",
                    "claim_text": candidate["text"],
                    "draft_span": {
                        "start_byte": candidate["start_byte"],
                        "end_byte": candidate["end_byte"],
                    },
                    "claim_kinds": ["quantitative" if quantitative else "other_factual"],
                    "ref_slugs": sorted(set(CITE_KEY.findall(candidate["text"]))),
                    "writer_anchors": [candidate["candidate_id"], f"line:{candidate['line']}"],
                    "paper_section": section_at(lines, candidate["line"]),
                    "selection_tier": "HIGH-IMPACT" if quantitative else "NOT-SELECTED",
                    **(
                        {"high_impact_basis": ["numerical"]}
                        if quantitative
                        else {}
                    ),
                },
            )

        char_cursor = 0
        line_spans: dict[int, tuple[int, int, str]] = {}
        for line_no, raw_line in enumerate(lines, start=1):
            content = raw_line.rstrip("\r\n")
            leading = len(content) - len(content.lstrip())
            trailing = len(content.rstrip())
            if trailing > leading:
                start_char = char_cursor + leading
                end_char = char_cursor + trailing
                line_spans[line_no] = (
                    byte_offset(draft, start_char),
                    byte_offset(draft, end_char),
                    draft[start_char:end_char],
                )
            char_cursor += len(raw_line)

        for idx, line_no in enumerate(semantic_lines, start=1):
            if line_no not in line_spans:
                raise ValueError(f"{paper_id}: semantic line {line_no} is blank or absent")
            start_byte, end_byte, claim_text = line_spans[line_no]
            # Display equations can be split by Pandoc into operator-only lines.
            # Those fragments are not independently meaningful claims and fail
            # the registry's minimum-text schema constraint.
            if len(claim_text.strip()) < 3:
                continue
            add_or_upgrade(
                claims,
                {
                    "claim_id": f"{paper_id}-SEM-{idx:03d}",
                    "claim_text": claim_text,
                    "draft_span": {"start_byte": start_byte, "end_byte": end_byte},
                    "claim_kinds": ["other_factual"],
                    "ref_slugs": sorted(set(CITE_KEY.findall(claim_text))),
                    "writer_anchors": [f"semantic-selection:line:{line_no}"],
                    "paper_section": section_at(lines, line_no),
                    "selection_tier": "HIGH-IMPACT",
                    "high_impact_basis": ["headline_conclusion", "methods_critical"],
                },
            )

        remainder = [claim for claim in claims if claim["selection_tier"] == "NOT-SELECTED"]
        if remainder:
            random_count = len(remainder) if len(remainder) < 3 else min(10, max(3, math.ceil(0.10 * len(remainder))))
            rng = random.Random(f"{paper_id}:stage2.5:2026-08-26")
            for claim in rng.sample(remainder, random_count):
                claim["selection_tier"] = "RANDOM"

        selected = [claim for claim in claims if claim["selection_tier"] != "NOT-SELECTED"]
        floor = min(10, len(claims))
        if len(selected) < floor:
            available = [claim for claim in claims if claim["selection_tier"] == "NOT-SELECTED"]
            rng = random.Random(f"{paper_id}:stage2.5:top-up:2026-08-26")
            for claim in rng.sample(available, floor - len(selected)):
                claim["selection_tier"] = "TOP-UP"

        claims.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"]))
        registry = {
            "schema_version": "claim-registry/1.0",
            "draft_raw_sha256": hashlib.sha256(draft_raw).hexdigest(),
            "claims": claims,
        }
        (stage / "claim_registry.json").write_text(
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
