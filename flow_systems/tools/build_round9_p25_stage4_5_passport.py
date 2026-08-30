#!/usr/bin/env python3
"""Build Paper 25's append-only Stage-4.5 Material Passport handoff.

The Stage-2.5 passport remains immutable history.  This producer copies it to a
new handoff, appends the current compliance entry, binds the current revised
draft, and deliberately marks the handoff UNVERIFIED while exact MINOR
bibliography corrections remain unauthorized.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "papers/25-three-disk-scattering-flow"
NOTES = PAPER / "notes"
SOURCE = NOTES / "stage2_5_material_passport.json"
COMPLIANCE = NOTES / "stage4_5_compliance_report.json"
OUTPUT = NOTES / "stage4_5_material_passport.json"
DRAFT = NOTES / "stage4_revision_round1.tex"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    passport = json.loads(SOURCE.read_text(encoding="utf-8"))
    compliance = json.loads(COMPLIANCE.read_text(encoding="utf-8"))

    history = list(passport.get("compliance_history", []))
    key = (compliance["stage"], compliance["generated_at"])
    if not any((row.get("stage"), row.get("generated_at")) == key for row in history):
        history.append(compliance)

    dependencies = list(passport.get("upstream_dependencies", []))
    additions = [
        "round9-stage4-revision-round1",
        "round9-stage3-prime-round2-minor-revision",
        "round9-stage4.5-final-check-round1-four-minor-hold",
    ]
    for item in additions:
        if item not in dependencies:
            dependencies.append(item)

    passport.update(
        {
            "origin_skill": "ars-codex:academic-research-suite",
            "origin_mode": "full",
            "origin_date": "2026-08-30T12:27:09Z",
            "verification_status": "UNVERIFIED",
            "version_label": "p25-round9-stage4.5-round1-four-minor-hold-v1",
            "content_hash": sha(DRAFT),
            "upstream_dependencies": dependencies,
            "compliance_history": history,
            "repro_lock": None,
            "stage4_5_gate": {
                "status": "AUDIT_COMPLETE_HOLD_FOR_EXACT_MINOR_CORRECTIONS",
                "mode": "final-check",
                "audit_target": {
                    "path": "notes/stage4_revision_round1.tex",
                    "sha256": sha(DRAFT),
                },
                "issues": {
                    "SERIOUS": 0,
                    "MEDIUM": 0,
                    "MINOR": 4,
                },
                "correction_list": {
                    "path": "notes/stage4_5_integrity_correction_list.json",
                    "sha256": sha(NOTES / "stage4_5_integrity_correction_list.json"),
                },
                "proposed_patch": {
                    "path": "notes/stage4_5_integrity_patch_round1.json",
                    "sha256": sha(NOTES / "stage4_5_integrity_patch_round1.json"),
                    "applied": False,
                    "authorized": False,
                },
                "stage5_entry": "CLOSED_ZERO_ISSUE_BOUNDARY",
                "canonical_promotion": False,
                "route_gate_credit": "NONE",
            },
        }
    )
    passport.pop("integrity_pass_date", None)

    OUTPUT.write_text(
        json.dumps(passport, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"sha256={sha(OUTPUT)}")


if __name__ == "__main__":
    main()

