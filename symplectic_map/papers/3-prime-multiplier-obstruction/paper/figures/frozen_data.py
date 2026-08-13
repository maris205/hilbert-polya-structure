from __future__ import annotations

import json
from pathlib import Path


FIG_DIR = Path(__file__).resolve().parent
PAPER_DIR = FIG_DIR.parent
PROJECT_DIR = PAPER_DIR.parent
RESULTS_DIR = PROJECT_DIR / "results"
EXPERIMENTS_DIR = PROJECT_DIR / "experiments"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def checklist_by_id(checklist: list[dict]) -> dict[str, dict]:
    return {item["id"]: item for item in checklist}


def load_core():
    return {
        "source_lock": load_json(EXPERIMENTS_DIR / "source_lock.json"),
        "proof_audit": load_json(RESULTS_DIR / "proof_audit.json"),
        "negative_ledger": load_json(RESULTS_DIR / "negative_result_ledger.json"),
        "candidate_audit": load_json(RESULTS_DIR / "candidate_multiplier_audit.json"),
        "control_audit": load_json(RESULTS_DIR / "control_audit.json"),
        "conjugacy_audit": load_json(RESULTS_DIR / "conjugacy_audit.json"),
        "bridge_audit": load_json(RESULTS_DIR / "symplectic_bridge_audit.json"),
        "exact_polynomials": load_json(RESULTS_DIR / "exact_polynomials.json"),
    }

