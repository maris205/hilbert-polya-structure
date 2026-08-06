#!/usr/bin/env python3
"""Run the frozen R057S1 centered-even a/eta mechanism supplement."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_mutual_separation_r057 import (  # noqa: E402
    Configuration,
    fraction_text,
    summarize_configuration,
)


PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057S1_EVEN_PARAMETER_STRESS_PROTOCOL.json"
)
PROTOCOL_SHA256 = "de3f3d33865898191163d33df0444a40bf8fa1d89e080cef6343192a7db91a76"
OUTPUT_JSON = PROJECT_ROOT / "results" / "even_parameter_stress_r057s1.json"
OUTPUT_CSV = PROJECT_ROOT / "results" / "even_parameter_stress_r057s1.csv"
OUTPUT_MD = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057S1_EVEN_PARAMETER_STRESS_ANALYSIS.md"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--output", type=Path, default=OUTPUT_JSON)
    parser.add_argument("--csv-output", type=Path, default=OUTPUT_CSV)
    parser.add_argument("--markdown-output", type=Path, default=OUTPUT_MD)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def slug(value: Fraction) -> str:
    sign = "m" if value < 0 else "p" if value > 0 else "z"
    magnitude = abs(value)
    return f"{sign}{magnitude.numerator}_{magnitude.denominator}"


def load_protocol() -> dict[str, object]:
    if sha256_file(PROTOCOL) != PROTOCOL_SHA256:
        raise SystemExit("R057S1 protocol SHA-256 mismatch")
    payload = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    checks = {
        "run_id": payload.get("run_id") == "R057S1_EVEN_PARAMETER_STRESS",
        "status": payload.get("status")
        == "FROZEN_BEFORE_SUPPLEMENT_PRODUCTION",
        "grid_count": len(payload.get("grids", [])) == 14,
        "panel_count": len(payload.get("panels", [])) == 2,
    }
    if not all(checks.values()):
        raise SystemExit(f"R057S1 code/protocol mismatch: {checks}")
    return payload


def expand_configurations(payload: dict[str, object]) -> list[Configuration]:
    constants = payload["constants"]
    grids = [int(value) for value in payload["grids"]]
    jobs: list[Configuration] = []
    for panel in payload["panels"]:
        panel_id = str(panel["panel_id"])
        if panel_id == "eta_even_stress":
            a_values = [Fraction(str(panel["fixed_a"]))]
            eta_values = [Fraction(str(value)) for value in panel["eta_values"]]
        elif panel_id == "a_even_stress":
            a_values = [Fraction(str(value)) for value in panel["a_values"]]
            eta_values = [Fraction(str(panel["fixed_eta"]))]
        else:
            raise AssertionError(f"unknown R057S1 panel: {panel_id}")
        for grid in grids:
            for a_value in a_values:
                for eta in eta_values:
                    jobs.append(
                        Configuration(
                            panel_id=panel_id,
                            configuration_id=(
                                f"{panel_id}_n{grid}_a{slug(a_value)}_e{slug(eta)}"
                            ),
                            role="post_primary_even_parameter_mechanism",
                            grid=grid,
                            grid_offset=Fraction(str(constants["grid_offset"])),
                            a=a_value,
                            c=Fraction(str(constants["c"])),
                            radius=Fraction(str(constants["radius"])),
                            eta=eta,
                            fresh_discovery_eligible=False,
                        )
                    )
    if len(jobs) != 266 or len({item.configuration_id for item in jobs}) != 266:
        raise AssertionError("R057S1 frozen configuration expansion mismatch")
    return jobs


def run_configuration(
    configuration: Configuration,
) -> tuple[dict[str, object], dict[str, object]]:
    summary, boundary_rows = summarize_configuration(configuration)
    center_rows = [row for row in boundary_rows if row["boundary_fraction"] == "0"]
    if len(center_rows) != 1:
        raise AssertionError("centered even grid must have one p=0 boundary")
    center = center_rows[0]
    if int(center["boundary_index"]) != configuration.grid // 2:
        raise AssertionError("unexpected center-boundary index")
    record = {
        "panel_id": configuration.panel_id,
        "configuration_id": configuration.configuration_id,
        "grid": configuration.grid,
        "a_fraction": fraction_text(configuration.a),
        "eta_fraction": fraction_text(configuration.eta),
        "uncapped_k_max": summary["uncapped_k_max"],
        "cap_active_count": summary["cap_active_count"],
        "k_gate_pass": summary["k_gate_pass"],
        "certificate_pass": summary["certificate_pass"],
        "failure_boundary_count": summary["failure_boundary_count"],
        "all_failure_witnesses_replay_pass": summary[
            "all_failure_witnesses_replay_pass"
        ],
        "first_failure_witness": summary["first_failure_witness"],
        "center_boundary_index": center["boundary_index"],
        "center_left_k": center["left_k"],
        "center_right_k": center["right_k"],
        "center_omega_plus_fraction": center["omega_plus_fraction"],
        "center_delta_plus_fraction": center["delta_plus_fraction"],
        "center_margin_plus_fraction": center["margin_plus_fraction"],
        "center_headroom_plus_fraction": center["headroom_plus"],
        "center_headroom_plus": (
            None
            if center["headroom_plus"] == "inf"
            else float(Fraction(str(center["headroom_plus"])))
        ),
        "center_plus_pass": center["plus_pass"],
        "center_omega_minus_fraction": center["omega_minus_fraction"],
        "center_delta_minus_fraction": center["delta_minus_fraction"],
        "center_margin_minus_fraction": center["margin_minus_fraction"],
        "center_minus_pass": center["minus_pass"],
        "all_failures_at_center": (
            int(summary["failure_boundary_count"])
            == int(not bool(center["boundary_pass"]))
        ),
    }
    return record, center


def transition_count(statuses: Sequence[bool]) -> int:
    return sum(left != right for left, right in zip(statuses, statuses[1:]))


def panel_sequences(
    records: Sequence[dict[str, object]],
    *,
    panel_id: str,
    grids: Sequence[int],
    parameter_order: Sequence[Fraction],
    parameter_key: str,
) -> list[dict[str, object]]:
    output = []
    for grid in grids:
        selected = [
            record
            for record in records
            if record["panel_id"] == panel_id and int(record["grid"]) == grid
        ]
        by_parameter = {
            Fraction(str(record[parameter_key])): record for record in selected
        }
        ordered = [by_parameter[value] for value in parameter_order]
        statuses = [bool(record["certificate_pass"]) for record in ordered]
        transitions = transition_count(statuses)
        output.append(
            {
                "grid": grid,
                "parameter_values": [fraction_text(value) for value in parameter_order],
                "pass_sequence": statuses,
                "k_sequence": [int(record["center_left_k"]) for record in ordered],
                "headroom_sequence": [record["center_headroom_plus"] for record in ordered],
                "transition_count": transitions,
                "nonmonotone_pass_fail_sequence": transitions > 1,
                "pass_count": sum(statuses),
                "fail_count": len(statuses) - sum(statuses),
            }
        )
    return output


def analyze(
    records: Sequence[dict[str, object]], payload: dict[str, object]
) -> dict[str, object]:
    grids = [int(value) for value in payload["grids"]]
    eta_panel = next(
        panel for panel in payload["panels"] if panel["panel_id"] == "eta_even_stress"
    )
    a_panel = next(
        panel for panel in payload["panels"] if panel["panel_id"] == "a_even_stress"
    )
    eta_order = [Fraction(str(value)) for value in eta_panel["eta_values"]]
    a_order = [Fraction(str(value)) for value in a_panel["a_values"]]
    eta_sequences = panel_sequences(
        records,
        panel_id="eta_even_stress",
        grids=grids,
        parameter_order=eta_order,
        parameter_key="eta_fraction",
    )
    a_sequences = panel_sequences(
        records,
        panel_id="a_even_stress",
        grids=grids,
        parameter_order=a_order,
        parameter_key="a_fraction",
    )
    cap_active = [record for record in records if not record["k_gate_pass"]]
    failures = [record for record in records if not record["certificate_pass"]]
    baseline_pairs = {}
    for record in records:
        if record["a_fraction"] == "6" and record["eta_fraction"] == "1/4":
            baseline_pairs.setdefault(int(record["grid"]), []).append(record)
    baseline_duplicate_pass = all(
        len(items) == 2
        and items[0]["certificate_pass"] == items[1]["certificate_pass"]
        and items[0]["center_margin_plus_fraction"]
        == items[1]["center_margin_plus_fraction"]
        for items in baseline_pairs.values()
    )
    return {
        "configuration_count": len(records),
        "pass_count": len(records) - len(failures),
        "fail_count": len(failures),
        "grid_with_any_failure_count": len(
            {int(record["grid"]) for record in failures}
        ),
        "cap_active_configuration_count": len(cap_active),
        "cap_active_configuration_ids": [
            record["configuration_id"] for record in cap_active
        ],
        "all_witnesses_pass": all(
            record["all_failure_witnesses_replay_pass"] for record in failures
        ),
        "all_failures_at_center": all(record["all_failures_at_center"] for record in failures),
        "baseline_duplicate_consistency_pass": baseline_duplicate_pass,
        "strict_all_gates_pass": (
            len(records) == 266
            and not cap_active
            and all(record["all_failure_witnesses_replay_pass"] for record in failures)
            and all(record["all_failures_at_center"] for record in failures)
            and baseline_duplicate_pass
        ),
        "eta_sequences": eta_sequences,
        "a_sequences": a_sequences,
        "eta_nonmonotone_grid_count": sum(
            item["nonmonotone_pass_fail_sequence"] for item in eta_sequences
        ),
        "a_nonmonotone_grid_count": sum(
            item["nonmonotone_pass_fail_sequence"] for item in a_sequences
        ),
        "failure_configuration_ids": [
            record["configuration_id"] for record in failures
        ],
    }


CSV_FIELDS = [
    "panel_id",
    "configuration_id",
    "grid",
    "a_fraction",
    "eta_fraction",
    "uncapped_k_max",
    "cap_active_count",
    "k_gate_pass",
    "certificate_pass",
    "failure_boundary_count",
    "center_left_k",
    "center_right_k",
    "center_omega_plus_fraction",
    "center_delta_plus_fraction",
    "center_margin_plus_fraction",
    "center_headroom_plus_fraction",
    "center_headroom_plus",
    "center_plus_pass",
    "center_omega_minus_fraction",
    "center_delta_minus_fraction",
    "center_margin_minus_fraction",
    "center_minus_pass",
    "all_failures_at_center",
]


def render_markdown(analysis: dict[str, object]) -> str:
    lines = [
        "# R057S1 Even-Grid Parameter-Stress Analysis",
        "",
        "**Completed:** 2026-08-02  ",
        f"**Frozen protocol:** `{PROTOCOL_SHA256}`  ",
        f"**Decision:** {'ALL GATES PASS' if analysis['strict_all_gates_pass'] else 'STRICT GATE FAILURE'}",
        "",
        "## 1. Outcome",
        "",
        (
            f"The post-primary supplement evaluates {analysis['configuration_count']} "
            f"centered-even parameter configurations. "
            f"{analysis['pass_count']} pass the exact mutual=true certificate and "
            f"{analysis['fail_count']} fail. Failures occur on "
            f"{analysis['grid_with_any_failure_count']} of the 14 selected grids."
        ),
        "",
        (
            f"All failures are localized at the shared center boundary $p=0$: "
            f"**{analysis['all_failures_at_center']}**. The uncapped-K gate has "
            f"{analysis['cap_active_configuration_count']} violations."
        ),
        "",
        "## 2. Eta staircase at fixed $a=6$",
        "",
        "Parameter order: $1/8,1/6,1/5,1/4,1/3,1/2,3/4,1,3/2,2$.",
        "",
        "| N | Pass sequence | Center K sequence | Transitions | Nonmonotone |",
        "|---:|---|---|---:|---|",
    ]
    for item in analysis["eta_sequences"]:
        status = "".join("P" if value else "F" for value in item["pass_sequence"])
        lines.append(
            f"| {item['grid']} | `{status}` | "
            f"`{','.join(map(str, item['k_sequence']))}` | "
            f"{item['transition_count']} | "
            f"{'yes' if item['nonmonotone_pass_fail_sequence'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## 3. Quadratic-strength staircase at fixed $\\eta=1/4$",
            "",
            "Parameter order: $1,2,3,4,5,6,8,10,12$.",
            "",
            "| N | Pass sequence | Center K sequence | Transitions | Nonmonotone |",
            "|---:|---|---|---:|---|",
        ]
    )
    for item in analysis["a_sequences"]:
        status = "".join("P" if value else "F" for value in item["pass_sequence"])
        lines.append(
            f"| {item['grid']} | `{status}` | "
            f"`{','.join(map(str, item['k_sequence']))}` | "
            f"{item['transition_count']} | "
            f"{'yes' if item['nonmonotone_pass_fail_sequence'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## 4. Interpretation",
            "",
            (
                "The pass/fail boundary is a discrete arithmetic staircase, not "
                "a smooth convergence law. At $p=0$, the common overshoot is "
                "$a(h/K)^2$ while $K=\\lceil2ah/\\eta\\rceil$; changing $a$ or "
                "$\\eta$ moves both the numerator and the integer subdivision, "
                "producing a sawtooth in $a$ and a one-direction staircase in "
                "$\\eta$."
            ),
            "",
            (
                f"Eta sequences with more than one pass/fail transition: "
                f"{analysis['eta_nonmonotone_grid_count']}. A sequences with "
                f"more than one transition: {analysis['a_nonmonotone_grid_count']}."
            ),
            "",
            "This supplement was selected after R057 and is a mechanism map, not "
            "held-out confirmation. It does not alter the invariant/covering/"
            "operator scope boundary.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    if args.workers <= 0:
        raise SystemExit("--workers must be positive")
    payload = load_protocol()
    jobs = expand_configurations(payload)
    if args.workers == 1:
        outputs = [run_configuration(item) for item in jobs]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as executor:
            outputs = list(executor.map(run_configuration, jobs))
    records = [record for record, _ in outputs]
    analysis = analyze(records, payload)
    result = {
        "run_id": "R057S1_EVEN_PARAMETER_STRESS",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_sha256": PROTOCOL_SHA256,
        "analysis": analysis,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.csv_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with args.csv_output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    args.markdown_output.write_text(render_markdown(analysis), encoding="utf-8")
    print(
        json.dumps(
            {
                "json": str(args.output),
                "csv": str(args.csv_output),
                "analysis": str(args.markdown_output),
                "configuration_count": analysis["configuration_count"],
                "pass_count": analysis["pass_count"],
                "fail_count": analysis["fail_count"],
                "strict_all_gates_pass": analysis["strict_all_gates_pass"],
                "eta_nonmonotone_grid_count": analysis[
                    "eta_nonmonotone_grid_count"
                ],
                "a_nonmonotone_grid_count": analysis[
                    "a_nonmonotone_grid_count"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
