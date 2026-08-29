#!/usr/bin/env python3
"""Materialize hash-locked Phase-E semantic verdict receipts for Papers 24--28.

This is deliberately not a generic "mark everything verified" generator.  It
will emit receipts only for the exact manuscript, registry, evidence-row, and
human-readable semantic-audit bytes independently reviewed on 2026-08-29.
Any change to one of those inputs fails closed and requires a new semantic
review before the constants below may be updated.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent

# These bindings are the independent reviewers' completed Phase-E population,
# not convenient current-file hashes.  The P24--P27 semantic-audit hashes below
# include the reviewed post-authorization status addenda; those addenda close
# the provenance gate without altering any claim-level semantic adjudication.
# Updating one remains a semantic-audit act.
AUDITED_INPUTS: dict[str, dict[str, Any]] = {
    "24-bianchi-holonomy-flow": {
        "manuscript": "e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11",
        "registry": "6a6fc0ebc3f76814638e49e378f2d64b086d06658cf54f1ccb877c0a8eedcdd4",
        "rows": "fe1a8634f6e0a09f0be623b23dd248257a1844a5ed54ce9ce86cfdd0ea7f9890",
        "semantic_audit": "b77151becfc2166ad66031418b552fc306fc9ae167f9127bbe031c5fbb2f5633",
        "selected": 64,
        "tuples": 66,
    },
    "25-three-disk-scattering-flow": {
        "manuscript": "283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb",
        "registry": "57063b60063a873d909506e6fcf8c3bd938c4fed57de06cb58beee0daca76956",
        "rows": "26e7fd2a6f628e463c5fb8f224f17851d55bd65fb67d726aa4dcd0b72e27eb89",
        "semantic_audit": "19e8953e453bce8b5be30e27c9b71dd4285aa7e958b9c57419a3409012909320",
        "selected": 48,
        "tuples": 49,
    },
    "26-level11-newform-time-change": {
        "manuscript": "00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe",
        "registry": "1d27b238ae1fd5485192c7044f135e530d68aba6c997041fd441d7db4ded9cf2",
        "rows": "7cdc6095fae6ef317059ce46104bfaeee4a7707f51fb4dcd78005e1bf8f0a842",
        "semantic_audit": "062a348437ac3fe72b2c26b3832399c3b7949d6496a0fa5409b34368b20eb596",
        "selected": 68,
        "tuples": 70,
    },
    "27-congruence-inverse-limit-no-go": {
        "manuscript": "c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9",
        "registry": "05455f35794381fc5f472baaa56cdd2fedaf3d3cbdb99f58f344364c26893452",
        "rows": "2f47adea1276a72469fddd8c1ee666796e2b73dcd388acc986c9088756be0496",
        "semantic_audit": "ba1b801d7aef1f601a172338d55a26ceb86742eada0c23c22e4162e6fc738fb5",
        "selected": 70,
        "tuples": 71,
    },
    "28-bolza-magnetic-flow": {
        "manuscript": "864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7",
        "registry": "031e04aae854667ba03e4b39d8df28fa61391264ab7f8c1fee55d6d6a3514f07",
        "rows": "58ca03d5c726ec6a6fd018766c35e810e982067fe84fbe8d264dd0acc18879c4",
        "semantic_audit": "e1ca743684bc783d498955f4335e512158917c0d2898802ef0bd5dc989d6a850",
        "selected": 81,
        "tuples": 84,
        "verdict_overrides": {"P28-E1-072": "MINOR_DISTORTION"},
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def utc_now() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def atomic_json(path: Path, value: Any) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def build_one(paper: str, expected: dict[str, Any], generated_at: str) -> dict[str, Any]:
    base = ROOT / "papers" / paper
    notes = base / "notes"
    manuscript_path = base / "paper" / "manuscript.tex"
    registry_path = notes / "stage2_5_claim_registry.json"
    rows_path = notes / "stage2_5_evidence_rows.json"
    semantic_path = notes / "stage2_5_phase_e_semantic_audit.md"
    actual_hashes = {
        "manuscript": sha(manuscript_path),
        "registry": sha(registry_path),
        "rows": sha(rows_path),
        "semantic_audit": sha(semantic_path),
    }
    expected_hashes = {key: expected[key] for key in actual_hashes}
    if actual_hashes != expected_hashes:
        raise RuntimeError(
            f"{paper}: audited input drift; a fresh semantic review is required: "
            f"{actual_hashes} != {expected_hashes}"
        )

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    rows = json.loads(rows_path.read_text(encoding="utf-8"))
    selected = {
        claim["claim_id"]: claim
        for claim in registry["claims"]
        if claim["selection_tier"] != "NOT-SELECTED"
    }
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row["claim"]["claim_id"]].append(row)

    if len(selected) != expected["selected"] or len(rows) != expected["tuples"]:
        raise RuntimeError(f"{paper}: audited denominator mismatch")
    if set(grouped) != set(selected):
        raise RuntimeError(f"{paper}: selected/evidence claim population mismatch")

    verdicts = []
    for claim_id, claim in selected.items():
        claim_rows = grouped[claim_id]
        expected_claim_object = {
            "claim_id": claim_id,
            "paper_locator": claim["writer_anchors"][0],
            "selection_tier": claim["selection_tier"],
            "text": claim["claim_text"],
        }
        if any(row["claim"] != expected_claim_object for row in claim_rows):
            raise RuntimeError(f"{paper}: inconsistent claim object for {claim_id}")
        expected_verdict = expected.get("verdict_overrides", {}).get(
            claim_id, "VERIFIED"
        )
        if any(row["verdict"] != expected_verdict for row in claim_rows):
            raise RuntimeError(
                f"{paper}: evidence verdict mismatch for {claim_id}; "
                f"expected {expected_verdict}"
            )
        expected_refs = set(claim["ref_slugs"] or [None])
        actual_refs = {row["source"]["ref_slug"] for row in claim_rows}
        if actual_refs != expected_refs or len(claim_rows) != len(expected_refs):
            raise RuntimeError(f"{paper}: source-tuple mismatch for {claim_id}")
        verdicts.append(
            {
                "claim_id": claim_id,
                "selection_tier": claim["selection_tier"],
                "verdict": expected_verdict,
                "tuple_count": len(claim_rows),
                "row_ids": [row["row_id"] for row in claim_rows],
                "row_sha256s": [row["row_sha256"] for row in claim_rows],
                "claim_object_sha256": canonical_sha(expected_claim_object),
            }
        )

    verdict_counts = {
        key: sum(row["verdict"] == key for row in verdicts)
        for key in (
            "VERIFIED",
            "MINOR_DISTORTION",
            "MAJOR_DISTORTION",
            "UNVERIFIABLE",
            "UNVERIFIABLE_ACCESS",
        )
    }
    if verdict_counts["MAJOR_DISTORTION"] or verdict_counts["UNVERIFIABLE"] or verdict_counts["UNVERIFIABLE_ACCESS"]:
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
            "manuscript_sha256": actual_hashes["manuscript"],
            "claim_registry_sha256": actual_hashes["registry"],
            "evidence_rows_sha256": actual_hashes["rows"],
            "semantic_audit_sha256": actual_hashes["semantic_audit"],
        },
        "selected_distinct_claims": len(selected),
        "evidence_tuples": len(rows),
        "verdict_counts": verdict_counts,
        "semantic_extraction_coverage": "not_machine_detectable",
        "evidence_state_boundary": (
            "All tuple carriers remain anchorless; this receipt binds the "
            "separate semantic review and does not add source excerpts."
        ),
        "claim_verdicts": verdicts,
    }
    out = notes / "stage2_5_phase_e_semantic_verdicts.json"
    atomic_json(out, receipt)
    return {
        "paper": paper,
        "selected": len(selected),
        "tuples": len(rows),
        "receipt_sha256": sha(out),
    }


def main() -> int:
    generated_at = utc_now()
    result = [
        build_one(paper, expected, generated_at)
        for paper, expected in AUDITED_INPUTS.items()
    ]
    print(json.dumps({"status": "PASS", "papers": result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
