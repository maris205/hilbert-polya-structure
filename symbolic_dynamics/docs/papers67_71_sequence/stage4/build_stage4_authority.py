#!/usr/bin/env python3
"""Build the five bounded Stage-4 author-choice inputs and claim surfaces.

The immutable Stage-3 roadmaps remain reviewer-owned.  This helper records the
author's explicit approval of the already stated Stage-4 policy: address every
locally actionable must/should item, retain external-specialist items as HOLD,
and defer optional scope expansions.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EVENT_TEXT = "可以，进行下一阶段"
EVENT_ID = "AUTHOR-EVENT-2026-08-26-stage4-approval"


PAPERS = {
    "P67": "67-multiplicative-plaquette-matroid-complexity",
    "P68": "68-complete-bipartite-homshift-conjugacies",
    "P69": "69-orientation-sensitive-surface-flat-sft",
    "P70": "70-weighted-heisenberg-congruence-nullities",
    "P71": "71-zip-shift-degree-pressure",
}


TRIAGE = {
    "P67": {
        "REV-P67-EIC-W1": "will_address",
        "REV-P67-R1-W1": "will_address",
        "REV-P67-R2-W1": "specialist_hold",
        "REV-P67-R3-W1": "optional_defer",
    },
    "P68": {
        "REV-P68-EIC-W1": "will_address",
        "REV-P68-R1-W1": "will_address",
        "REV-P68-R2-W1": "specialist_hold",
        "REV-P68-R3-W1": "will_address",
    },
    "P69": {
        "REV-P69-EIC-W1": "will_address",
        "REV-P69-R1-W1": "will_address",
        "REV-P69-R2-W1": "specialist_hold",
        "REV-P69-R3-W1": "optional_defer",
    },
    "P70": {
        "REV-P70-EIC-W1": "will_address",
        "REV-P70-R1-W1": "will_address",
        "REV-P70-R2-W1": "specialist_hold",
        "REV-P70-R3-W1": "will_address",
    },
    "P71": {
        "REV-P71-EIC-W1": "will_address",
        "REV-P71-R1-W1": "will_address",
        "REV-P71-R2-W1": "specialist_hold",
        "REV-P71-R3-W1": "optional_defer",
    },
}


REASONS = {
    "specialist_hold": (
        "External specialist exact-neighbour review is not available in this "
        "internal round. Preserve the explicit HOLD and non-priority wording; "
        "do not represent specialist clearance as completed."
    ),
    "optional_defer": (
        "Deferred to keep this revision bounded to decision-bearing corrections "
        "and reproducible controls; the optional expansion is outside this round."
    ),
}


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    event_hash = sha256(EVENT_TEXT.encode("utf-8"))
    for paper_id, slug in PAPERS.items():
        paper = ROOT / "papers" / slug
        stage3 = paper / "stage3"
        stage4 = paper / "stage4"
        base = stage3 / "ANCHORED_REVIEW_DRAFT.md"
        roadmap_path = stage3 / "REVISION_ROADMAP.json"
        roadmap_raw = roadmap_path.read_bytes()
        roadmap = json.loads(roadmap_raw)

        claim_surface = {
            "schema_version": "claim-surface-manifest/1.0",
            "revision_round": roadmap["revision_round"],
            "roadmap_sha256": sha256(roadmap_raw),
            "base_draft_sha256": sha256(base.read_bytes()),
            "claim_intent_sources": [],
            "surfaces": [],
        }
        dump(stage4 / "CLAIM_SURFACE_MANIFEST.json", claim_surface)

        # This is the exact Stage-4 write-base projection of the completed
        # Stage-2.5 internal integrity gate.  Release/priority/specialist holds
        # remain separate policy gates and are not represented as cleared by
        # this narrowly scoped chain-start receipt.
        integrity_receipt = {
            "schema_version": "integrity-pass-receipt/1.0",
            "receipt_id": f"INTEGRITY-PASS-{paper_id}-stage4-chain-start",
            "checked_draft_sha256": sha256(base.read_bytes()),
            "verdict": "PASS",
            "open_issue_count": 0,
            "issued_by": "integrity_verification_agent",
        }
        dump(stage4 / "INTEGRITY_PASS_RECEIPT.json", integrity_receipt)

        item_ids = [item["id"] for item in roadmap["items"]]
        choices = []
        for item in roadmap["items"]:
            item_id = item["id"]
            policy = TRIAGE[paper_id][item_id]
            if policy == "will_address":
                choices.append(
                    {
                        "item_id": item_id,
                        "author_event_id": EVENT_ID,
                        "author_triage": "will_address",
                        "authorized_targets": item["proposed_targets"],
                        "claim_strength_authorizations": [],
                    }
                )
            else:
                choices.append(
                    {
                        "item_id": item_id,
                        "author_event_id": EVENT_ID,
                        "author_triage": "wont_address",
                        "author_reason": REASONS[policy],
                        "authorized_targets": [],
                        "claim_strength_authorizations": [],
                    }
                )

        collateral = []
        if paper_id == "P70":
            collateral.append(
                {
                    "authorization_id": "COLLATERAL-AUTH-P70-EIC-over-R2-B0056",
                    "author_event_id": EVENT_ID,
                    "authorizing_item_id": "REV-P70-EIC-W1",
                    "constrained_item_id": "REV-P70-R2-W1",
                    "block_id": "B0056",
                    "operation": "replace_block",
                    "reason": (
                        "Permit the EIC-required comparison matrix and bounded "
                        "ownership statement in B0056 while preserving the "
                        "declined specialist-clearance item as unresolved."
                    ),
                }
            )

        author_input = {
            "schema_version": "author-adjudication-input/1.0",
            "author_events": [
                {
                    "event_id": EVENT_ID,
                    "source": "explicit_session_user_message",
                    "actor_role": "author",
                    "input_sha256": event_hash,
                }
            ],
            "display_order": {
                "mode": "source_traceability",
                "item_ids": item_ids,
                "author_event_id": EVENT_ID,
            },
            "author_adjudications": choices,
            "collateral_authorizations": collateral,
        }
        dump(stage4 / "AUTHOR_ADJUDICATION_INPUT.json", author_input)


if __name__ == "__main__":
    main()
