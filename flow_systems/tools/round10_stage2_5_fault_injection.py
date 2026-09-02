#!/usr/bin/env python3
"""Isolated fail-closed tests for the Round-10 Stage-2.5 validator.

The script validates the current P29 carriers first, then injects four faults
in memory or in disposable copies.  It never mutates a registered workspace
artifact.  A PASS means the clean baseline was accepted and every mutation
was rejected; it is not a scientific-correctness or reproducibility claim.
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
from typing import Callable


ROOT = Path(__file__).resolve().parent.parent
PAPER = "29-bianchi-ideal-owner-refinement"
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does "
    "not judge whether the experiment was correctly designed, run, statistically "
    "adequate, or reproducible by ARS."
)


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("round10_stage2_5_validator_fault", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import validator: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_temp_json(path: Path, value) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def rejected(label: str, action: Callable[[], object]) -> dict[str, str]:
    try:
        action()
    except Exception as exc:  # the tested validators may raise schema or gate errors
        return {
            "case": label,
            "expected": "REJECT",
            "observed": f"REJECT: {type(exc).__name__}: {exc}",
        }
    raise RuntimeError(f"fault injection was accepted: {label}")


def copied_paper() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    temp = tempfile.TemporaryDirectory(prefix="round10-stage2-5-fault-")
    destination = Path(temp.name) / PAPER
    shutil.copytree(
        ROOT / "papers" / PAPER,
        destination,
        ignore=shutil.ignore_patterns(
            "__pycache__", "*.pyc", "*.aux", "*.out", "*.blg", "*.bbl", "paper.pdf"
        ),
    )
    return temp, destination


def main() -> int:
    validator = load_module(ROOT / "tools/round10_stage2_5_validate_reports.py")
    base = ROOT / "papers" / PAPER
    notes = base / "notes"
    cfg = validator.PAPERS[PAPER]
    manuscript = base / "paper/manuscript.tex"
    canonical = {
        "manuscript_sha256": validator.sha(manuscript),
        "bibliography_sha256": validator.sha(base / "paper/references.bib"),
        "pdf_sha256": validator.sha(base / "paper/paper.pdf"),
    }
    checks: list[dict[str, str]] = []

    validator.validate_phase_ab(notes, PAPER, cfg, canonical)
    validator.validate_claim_core(base, PAPER, cfg, manuscript)
    checks.append(
        {
            "case": "unmodified_current_P29_phase_ab_and_claim_core",
            "expected": "ACCEPT",
            "observed": "ACCEPT",
        }
    )

    batch = load(ROOT / "BATCH_ROUND10_STAGE2_5_INTEGRITY_SUMMARY.json")
    stage3_tamper = copy.deepcopy(batch)
    stage3_tamper["stage3_authorized"] = True
    checks.append(
        rejected(
            "batch_stage3_authorized_changed_false_to_true",
            lambda: validator.assert_no_true_key(
                stage3_tamper, "stage3_authorized", "fault-injected batch"
            ),
        )
    )

    temp, copied = copied_paper()
    try:
        phase_ab_path = copied / "notes/stage2_5_phase_ab_final.json"
        phase_ab = load(phase_ab_path)
        phase_ab["bindings"]["manuscript_sha256"] = "0" * 64
        write_temp_json(phase_ab_path, phase_ab)
        checks.append(
            rejected(
                "phase_ab_manuscript_binding_replaced_with_zero_hash",
                lambda: validator.validate_phase_ab(
                    copied / "notes", PAPER, cfg, canonical
                ),
            )
        )
    finally:
        temp.cleanup()

    temp, copied = copied_paper()
    try:
        rows_path = copied / "notes/stage2_5_evidence_rows.json"
        rows = load(rows_path)
        rows[0]["anchor"] = {
            "kind": "url",
            "value_decoded": "https://example.invalid/injected",
            "value_encoded": "https%3A%2F%2Fexample.invalid%2Finjected",
        }
        write_temp_json(rows_path, rows)
        checks.append(
            rejected(
                "one_anchorless_evidence_row_upgraded_to_injected_url",
                lambda: validator.validate_claim_core(
                    copied, PAPER, cfg, copied / "paper/manuscript.tex"
                ),
            )
        )
    finally:
        temp.cleanup()

    temp, copied = copied_paper()
    try:
        drift_path = copied / "notes/stage2_5_claim_strength_drift_findings.json"
        drift = load(drift_path)
        drift["status"] = "completed"
        drift["revision_evidence_bundle_sha256"] = "0" * 64
        write_temp_json(drift_path, drift)
        checks.append(
            rejected(
                "official_E6_skip_falsely_changed_to_completed_with_unresolved_hash",
                lambda: validator.validate_claim_core(
                    copied, PAPER, cfg, copied / "paper/manuscript.tex"
                ),
            )
        )
    finally:
        temp.cleanup()

    generated_at = (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    print(
        json.dumps(
            {
                "schema": "flow-systems-round10-stage2.5-fault-injection/1.0",
                "generated_at": generated_at,
                "paper": PAPER,
                "status": "PASS",
                "workspace_mutation": "none; mutations were in-memory or temporary-copy only",
                "validator_sha256": validator.sha(
                    ROOT / "tools/round10_stage2_5_validate_reports.py"
                ),
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
