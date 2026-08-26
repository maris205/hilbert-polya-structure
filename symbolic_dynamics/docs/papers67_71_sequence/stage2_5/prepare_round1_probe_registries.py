#!/usr/bin/env python3
"""Create empty, draft-bound Claim Registry probes for correction round 1."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPERS = (
    "67-multiplicative-plaquette-matroid-complexity",
    "68-complete-bipartite-homshift-conjugacies",
    "69-orientation-sensitive-surface-flat-sft",
    "70-weighted-heisenberg-congruence-nullities",
    "71-zip-shift-degree-pressure",
)


def main() -> int:
    for directory in PAPERS:
        stage = ROOT / "papers" / directory / "stage2_5"
        draft_raw = (stage / "draft_for_claim_registry_round1.md").read_bytes()
        probe = {
            "schema_version": "claim-registry/1.0",
            "draft_raw_sha256": hashlib.sha256(draft_raw).hexdigest(),
            "claims": [],
        }
        (stage / "claim_registry_probe_round1.json").write_text(
            json.dumps(probe, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

