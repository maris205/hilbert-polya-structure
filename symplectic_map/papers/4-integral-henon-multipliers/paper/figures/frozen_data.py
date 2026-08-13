"""Read-only adapter for source-locked exact-audit outputs.

Figure generators import all scientific values through this module.  The
module rejects a partial, failed, or wrong-candidate result package before a
plot can be written.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


FIGURE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = FIGURE_DIR.parents[1]
RESULTS_DIR = PROJECT_DIR / "results"
EXPERIMENTS_DIR = PROJECT_DIR / "experiments"


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_frozen_package() -> dict[str, Any]:
    paths = {
        "source_lock": EXPERIMENTS_DIR / "source_lock.json",
        "source_lock_validation": RESULTS_DIR / "source_lock_validation.json",
        "proof": RESULTS_DIR / "proof_audit.json",
        "control": RESULTS_DIR / "control_audit.json",
        "candidate": RESULTS_DIR / "candidate_multiplier_audit.json",
        "periods": RESULTS_DIR / "exact_period_ledger.json",
        "scope": RESULTS_DIR / "scope_audit.json",
        "negative": RESULTS_DIR / "negative_result_ledger.json",
        "summary": RESULTS_DIR / "run_summary.json",
    }
    data = {key: _load(path) for key, path in paths.items()}

    summary = data["summary"]
    candidate = data["candidate"]
    validation = data["source_lock_validation"]
    candidate_id = data["source_lock"]["candidate_id"]
    if summary.get("status") != "PASS" or not summary.get("candidate_executed"):
        raise RuntimeError("refusing to plot an incomplete official run")
    if summary.get("must_run_failed") != 0:
        raise RuntimeError("refusing to plot a run with failed registered checks")
    if candidate.get("candidate_id") != candidate_id:
        raise RuntimeError("candidate audit does not match source lock")
    if validation.get("sha256") != _sha256(paths["source_lock"]):
        raise RuntimeError("source-lock hash changed after the official audit")
    if validation.get("pass") is not True:
        raise RuntimeError("source-lock validation did not pass")

    data["paths"] = {key: str(path.relative_to(PROJECT_DIR)) for key, path in paths.items()}
    data["hashes"] = {key: _sha256(path) for key, path in paths.items()}
    return data


def audited_period_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for record in data["periods"]["records"]:
        determinant_pass = (
            record.get("determinant") == "1"
            or record.get("determinant_remainder") == "0"
            or (
                isinstance(record.get("determinant_remainders"), list)
                and all(value == "0" for value in record["determinant_remainders"])
            )
        )
        rows.append(
            {
                "period": record["period"],
                "points": record["exact_point_count"],
                "cycles": record["exact_cycle_count"],
                "determinant_pass": determinant_pass,
                "trace": record["trace_elimination"]["expression"],
                "multiplier": record["multiplier_polynomial"]["expression"],
                "rational_roots": len(record["rational_multiplier_audit"]["exact_rational_roots"]),
                "unit_pass": bool(record["unit_certificate"]["monic"])
                and bool(record["unit_certificate"]["reciprocal_polynomial"]),
                "pass": bool(record["pass"]),
            }
        )
    return rows


def cycle_class_counts(data: dict[str, Any]) -> dict[str, int]:
    cycles = data["candidate"]["exact_modulus_audit"]["cycles"]
    counts = {"rational unit": 0, "irrational algebraic unit": 0}
    for cycle in cycles:
        classifications = {
            record["rational_modulus_classification"]
            for record in cycle["multiplier_modulus_squared_records"]
        }
        if "RATIONAL_MODULUS_UNIT" in classifications:
            counts["rational unit"] += 1
        else:
            counts["irrational algebraic unit"] += 1
    return counts
