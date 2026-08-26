#!/usr/bin/env python3
"""Rebase frozen Stage-2.5 Claim Registries onto corrected manuscripts.

Round-0 artifacts remain immutable.  The corrected draft and empty-registry
coverage probe must already exist under the ``*_round1`` names.  Exact
round-0 HIGH-IMPACT spans are relocated by their full bytes; newly added
owner-subtraction sentences are promoted by disclosed lexical rules; the
remaining mechanical candidates receive a deterministic random sentinel.

This is a bounded registration helper, not a semantic-completeness detector.
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
    "P67": "67-multiplicative-plaquette-matroid-complexity",
    "P68": "68-complete-bipartite-homshift-conjugacies",
    "P69": "69-orientation-sensitive-surface-flat-sft",
    "P70": "70-weighted-heisenberg-congruence-nullities",
    "P71": "71-zip-shift-degree-pressure",
}

OWNER_TERMS = {
    "P67": ("abbe", "spirkl", "affine multiplicative", "kir\\'aly", "király", "graph-symmetric"),
    "P68": (),
    "P69": ("snyder", "liebeck", "representation-zeta", "representation zeta", "ward", "röttger", "roettger"),
    "P70": ("deundyak", "leonov", "grassberger", "hörmann", "hormann"),
    "P71": ("s-expans", "2510.12980", "formalismo termodin", "thermodynamic-formalism project", "thermodynamic formalism project", "ufv"),
}

SUPERSEDED_HIGH_IMPACT = {
    "P71": {"P71-SEM-024", "P71-SEM-025"},
}

CITE_KEY = re.compile(r"@([A-Za-z0-9_.:-]+)")


def section_for_offset(draft: str, byte_offset: int) -> str | None:
    prefix = draft.encode("utf-8")[:byte_offset].decode("utf-8")
    section = None
    for line in prefix.splitlines():
        if line.startswith("# "):
            section = line[2:].strip()
    return section


def add_or_upgrade(claims: list[dict], claim: dict) -> None:
    span = (claim["draft_span"]["start_byte"], claim["draft_span"]["end_byte"])
    for existing in claims:
        old = (existing["draft_span"]["start_byte"], existing["draft_span"]["end_byte"])
        if old != span:
            continue
        if claim["selection_tier"] == "HIGH-IMPACT":
            existing["selection_tier"] = "HIGH-IMPACT"
            existing["high_impact_basis"] = sorted(
                set(existing.get("high_impact_basis", []) + claim.get("high_impact_basis", []))
            )
        existing["claim_kinds"] = sorted(set(existing["claim_kinds"] + claim["claim_kinds"]))
        existing["ref_slugs"] = sorted(set(existing["ref_slugs"] + claim["ref_slugs"]))
        existing["writer_anchors"] = sorted(set(existing["writer_anchors"] + claim["writer_anchors"]))
        return
    claims.append(claim)


def all_byte_offsets(haystack: bytes, needle: bytes) -> list[int]:
    offsets: list[int] = []
    cursor = 0
    while True:
        found = haystack.find(needle, cursor)
        if found < 0:
            return offsets
        offsets.append(found)
        cursor = found + max(1, len(needle))


def main() -> int:
    for paper_id, directory in PAPERS.items():
        stage = ROOT / "papers" / directory / "stage2_5"
        old_registry = json.loads((stage / "claim_registry.json").read_text(encoding="utf-8"))
        draft_path = stage / "draft_for_claim_registry_round1.md"
        draft_raw = draft_path.read_bytes()
        draft = draft_raw.decode("utf-8")
        probe = json.loads((stage / "claim_registry_candidate_probe_round1.json").read_text(encoding="utf-8"))
        claims: list[dict] = []
        rebase_rows: list[dict] = []

        for old in old_registry["claims"]:
            if old["selection_tier"] != "HIGH-IMPACT":
                continue
            needle = old["claim_text"].encode("utf-8")
            offsets = all_byte_offsets(draft_raw, needle)
            selected_offset = offsets[0] if len(offsets) == 1 else None
            status = "REBASED" if selected_offset is not None else "UNMATCHED_OR_AMBIGUOUS"
            if len(offsets) > 1:
                same_section = [
                    offset for offset in offsets
                    if section_for_offset(draft, offset) == old.get("paper_section")
                ]
                if len(same_section) == 1:
                    selected_offset = same_section[0]
                    status = "REBASED_SECTION_DISAMBIGUATED"
            if (
                selected_offset is None
                and old["claim_id"] in SUPERSEDED_HIGH_IMPACT.get(paper_id, set())
            ):
                status = "SUPERSEDED_BY_CORRECTED_OWNER_BOUNDARY"
            row = {
                "round0_claim_id": old["claim_id"],
                "match_count": len(offsets),
                "status": status,
            }
            rebase_rows.append(row)
            if selected_offset is None:
                continue
            start = selected_offset
            end = start + len(needle)
            add_or_upgrade(
                claims,
                {
                    "claim_id": old["claim_id"],
                    "claim_text": old["claim_text"],
                    "draft_span": {"start_byte": start, "end_byte": end},
                    "claim_kinds": old["claim_kinds"],
                    "ref_slugs": sorted(set(CITE_KEY.findall(old["claim_text"])) | set(old["ref_slugs"])),
                    "writer_anchors": sorted(set(old["writer_anchors"] + [f"round1-rebase:{old['claim_id']}"])),
                    "paper_section": section_for_offset(draft, start),
                    "selection_tier": "HIGH-IMPACT",
                    "high_impact_basis": sorted(set(old.get("high_impact_basis", []))),
                },
            )

        owner_terms = tuple(term.casefold() for term in OWNER_TERMS[paper_id])
        for idx, candidate in enumerate(probe["candidates"], start=1):
            quantitative = "quantitative_sentence" in candidate["candidate_kinds"]
            candidate_folded = candidate["text"].casefold()
            owner_boundary = any(term in candidate_folded for term in owner_terms)
            high = quantitative or owner_boundary
            add_or_upgrade(
                claims,
                {
                    "claim_id": f"{paper_id}-R1-CAND-{idx:03d}",
                    "claim_text": candidate["text"],
                    "draft_span": {
                        "start_byte": candidate["start_byte"],
                        "end_byte": candidate["end_byte"],
                    },
                    "claim_kinds": ["quantitative" if quantitative else "other_factual"],
                    "ref_slugs": sorted(set(CITE_KEY.findall(candidate["text"]))),
                    "writer_anchors": [candidate["candidate_id"], f"round1-line:{candidate['line']}"],
                    "paper_section": section_for_offset(draft, candidate["start_byte"]),
                    "selection_tier": "HIGH-IMPACT" if high else "NOT-SELECTED",
                    **(
                        {
                            "high_impact_basis": (
                                ["numerical", "disputed"]
                                if quantitative and owner_boundary
                                else ["numerical"]
                                if quantitative
                                else ["disputed"]
                            )
                        }
                        if high
                        else {}
                    ),
                },
            )

        remainder = [claim for claim in claims if claim["selection_tier"] == "NOT-SELECTED"]
        if remainder:
            random_count = (
                len(remainder)
                if len(remainder) < 3
                else min(10, max(3, math.ceil(0.10 * len(remainder))))
            )
            rng = random.Random(f"{paper_id}:stage2.5:round1:2026-08-26")
            for claim in rng.sample(remainder, random_count):
                claim["selection_tier"] = "RANDOM"

        selected = [claim for claim in claims if claim["selection_tier"] != "NOT-SELECTED"]
        floor = min(10, len(claims))
        if len(selected) < floor:
            available = [claim for claim in claims if claim["selection_tier"] == "NOT-SELECTED"]
            rng = random.Random(f"{paper_id}:stage2.5:round1:top-up:2026-08-26")
            for claim in rng.sample(available, floor - len(selected)):
                claim["selection_tier"] = "TOP-UP"

        claims.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"]))
        registry = {
            "schema_version": "claim-registry/1.0",
            "draft_raw_sha256": hashlib.sha256(draft_raw).hexdigest(),
            "claims": claims,
        }
        (stage / "claim_registry_round1.json").write_text(
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        report = {
            "paper_id": paper_id,
            "round": 1,
            "round0_high_impact_total": sum(
                row["selection_tier"] == "HIGH-IMPACT" for row in old_registry["claims"]
            ),
            "round0_high_impact_rebased": sum(row["status"] == "REBASED" for row in rebase_rows),
            "round0_high_impact_rebased_after_section_disambiguation": sum(
                row["status"].startswith("REBASED") for row in rebase_rows
            ),
            "round0_high_impact_superseded_by_correction": sum(
                row["status"].startswith("SUPERSEDED") for row in rebase_rows
            ),
            "unmatched_or_ambiguous": [
                row for row in rebase_rows if row["status"] == "UNMATCHED_OR_AMBIGUOUS"
            ],
            "round1_registry_claims": len(claims),
            "selection_tiers": {
                tier: sum(row["selection_tier"] == tier for row in claims)
                for tier in ("HIGH-IMPACT", "RANDOM", "TOP-UP", "NOT-SELECTED")
            },
            "semantic_extraction_completeness": "not_machine_detectable",
        }
        (stage / "claim_registry_round1_rebase_report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
