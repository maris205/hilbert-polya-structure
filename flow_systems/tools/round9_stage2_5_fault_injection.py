#!/usr/bin/env python3
"""Isolated fail-closed checks for the Round-9 Stage-2.5 provenance gate.

The test never mutates a registered workspace artifact.  It first validates
the current P24 intake, then applies declaration/alignment mutations in memory
and an artifact-hash mutation in a temporary paper copy.  Success means every
mutation is rejected while the unmodified intake remains accepted.
"""

from __future__ import annotations

import copy
import datetime as dt
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PAPER = "24-bianchi-holonomy-flow"
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does "
    "not judge whether the experiment was correctly designed, run, statistically "
    "adequate, or reproducible by ARS."
)


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("round9_stage2_5_validator_fault", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import validator: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def selected_registry(notes: Path) -> dict[str, dict]:
    registry = load(notes / "stage2_5_claim_registry.json")
    return {
        row["claim_id"]: row
        for row in registry["claims"]
        if row["selection_tier"] != "NOT-SELECTED"
    }


def expect_rejected(label: str, accepted: bool) -> dict[str, str]:
    if accepted:
        raise RuntimeError(f"fault injection was accepted: {label}")
    return {"case": label, "expected": "REJECT", "observed": "REJECT"}


def main() -> int:
    validator = load_module(ROOT / "tools/round9_stage2_5_validate_reports.py")
    base = ROOT / "papers" / PAPER
    notes = base / "notes"
    passport = load(notes / "stage2_5_material_passport.json")
    selected = selected_registry(notes)
    checks: list[dict[str, str]] = []

    if not validator.scholar_intake_is_valid(passport):
        raise RuntimeError("unmodified scholar intake was rejected")
    validator.validate_experiment_transcription(PAPER, base, notes, passport, selected)
    checks.append(
        {
            "case": "unmodified_current_intake_and_transcription",
            "expected": "ACCEPT",
            "observed": "ACCEPT",
        }
    )

    declaration_tamper = copy.deepcopy(passport)
    declaration_tamper["experiment_intake_declaration"]["declared_by"] = "agent"
    checks.append(
        expect_rejected(
            "scholar_declaration_ownership_changed_to_agent",
            validator.scholar_intake_is_valid(declaration_tamper),
        )
    )

    alignment_tamper = copy.deepcopy(passport)
    alignment_tamper["experiment_alignment_results"][0][
        "alignment_verdict"
    ] = "OVERSTATED"
    checks.append(
        expect_rejected(
            "one_claim_alignment_changed_from_ALIGNED_to_OVERSTATED",
            validator.scholar_intake_is_valid(alignment_tamper),
        )
    )

    with tempfile.TemporaryDirectory(prefix="round9-stage2-5-fault-") as temp:
        copied_base = Path(temp) / PAPER
        shutil.copytree(
            base,
            copied_base,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.aux", "*.out", "*.blg"),
        )
        copied_notes = copied_base / "notes"
        source_map_path = copied_notes / "stage2_5_experiment_provenance_source_map.json"
        source_map = load(source_map_path)
        source_map["experiments"][0]["artifacts"][0]["sha256"] = "0" * 64
        source_map_path.write_text(
            json.dumps(source_map, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        try:
            validator.validate_experiment_transcription(
                PAPER,
                copied_base,
                copied_notes,
                load(copied_notes / "stage2_5_material_passport.json"),
                selected_registry(copied_notes),
            )
        except RuntimeError as exc:
            if "stale source artifact" not in str(exc):
                raise
            checks.append(
                {
                    "case": "one_source_map_artifact_sha256_replaced_with_zero_hash",
                    "expected": "REJECT",
                    "observed": f"REJECT: {exc}",
                }
            )
        else:
            raise RuntimeError("source-map hash fault injection was accepted")

    now = (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    print(
        json.dumps(
            {
                "schema": "flow-systems-round9-stage2.5-fault-injection/1.0",
                "generated_at": now,
                "paper": PAPER,
                "status": "PASS",
                "workspace_mutation": "none; mutations were in-memory or temporary-copy only",
                "checks": checks,
                "boundary": BOUNDARY,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
