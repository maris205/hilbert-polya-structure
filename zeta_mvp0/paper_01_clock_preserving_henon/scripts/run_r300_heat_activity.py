#!/usr/bin/env python3
"""Run the frozen R300 relative heat-activity carrier pilot."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

from hp_candidate_search.heat_activity import asymptotic_constants, evaluate_record


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "results" / "r300_heat_activity"
PROTOCOL = PROJECT_ROOT / "research" / "route_b_round2" / "PILOT_PROTOCOL.md"
MODULE = PROJECT_ROOT / "src" / "hp_candidate_search" / "heat_activity.py"
TIME_GRID = (1.0e-2, 3.0e-3, 1.0e-3, 3.0e-4, 1.0e-4, 3.0e-5, 1.0e-5)
A = 51.0 / 50.0


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    records = [evaluate_record(t, A) for t in TIME_GRID]
    constants = asymptotic_constants(A)

    max_identity_error = max(record.identity_relative_error for record in records)
    all_positive = all(record.exact_bracket > 0.0 for record in records)
    all_negative = all(record.formal_relative_heat_carrier < 0.0 for record in records)
    tail_ratios = [record.bracket_over_log_squared for record in records[-4:]]
    monotone_tail = all(second < first for first, second in zip(tail_ratios, tail_ratios[1:]))
    gate_a = bool(all_positive and max_identity_error <= 1.0e-9)
    gate_b = bool(all_negative and monotone_tail)

    with (OUTPUT_DIR / "records.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0].to_dict()))
        writer.writeheader()
        writer.writerows(record.to_dict() for record in records)

    summary = {
        "run_id": "R300",
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "status": "PARTIAL_PASS" if gate_a and gate_b else "KILLED_OR_REVISE",
        "scope": "first_gradient_wigner_kirkwood_carrier_only",
        "a_exact": "51/50",
        "a": A,
        "h": "arbitrary_fixed_positive; carrier coefficient is h-independent in d=2",
        "time_grid": list(TIME_GRID),
        "constants": constants,
        "gates": {
            "R300_A_identity": "PASS" if gate_a else "FAIL",
            "R300_B_coefficient": "PASS" if gate_b else "FAIL",
            "R300_C_uniform_heat_remainder": "OPEN",
        },
        "diagnostics": {
            "max_identity_relative_error": max_identity_error,
            "all_exact_brackets_positive": all_positive,
            "all_formal_carriers_negative": all_negative,
            "tail_bracket_over_log_squared": tail_ratios,
            "tail_ratio_monotone_to_one": monotone_tail,
        },
        "allowed_claim": (
            "Exact nonzero first-gradient heat carrier for the fixed Hénon pair; "
            "the full small-t relative heat-trace asymptotic remains conditional "
            "on a uniform noncompact remainder proof."
        ),
        "forbidden_claims": [
            "rational-prime P gate",
            "explicit-formula Z gate",
            "individual zeta-zero prediction",
            "Riemann Hypothesis",
        ],
        "arithmetic_inputs": [],
        "records": [record.to_dict() for record in records],
    }
    (OUTPUT_DIR / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    manifest = {
        "run_id": "R300",
        "protocol_sha256": sha256(PROTOCOL),
        "module_sha256": sha256(MODULE),
        "runner_sha256": sha256(Path(__file__).resolve()),
        "summary_sha256": sha256(OUTPUT_DIR / "summary.json"),
        "records_sha256": sha256(OUTPUT_DIR / "records.csv"),
    }
    (OUTPUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if gate_a and gate_b else 2


if __name__ == "__main__":
    raise SystemExit(main())

