#!/usr/bin/env python3
"""Derive the local transverse monodromy gap from frozen L1-V2 transcripts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ACCEPTED = ROOT / "results/r401_val_l1_branch"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L1_MONODROMY_GAP_PROTOCOL.md"
ANALYZER = Path(__file__).resolve()
EXPECTED_ACCEPTED_HASHES = {
    ACCEPTED / "summary.json": "e9a71dfd61d26396d05b62a848f49577fdabdf3722101432455435d32bb7503c",
    ACCEPTED / "manifest.json": "3c653e50042050e69a8928dd1fc7dac3464b6ae8e7ea8d47c70a03e970ece860",
    ACCEPTED / "independent_checker.json": "a6c0db0fc2190013c221d0ecdd71ac6f86895fbaecad735e1f2814ea232280c2",
    ACCEPTED / "POSTCHECK_STATUS.json": "83726312ea975ad9741bf2c802bb03fd0898c76646587c2012eb24401537aaf6",
}

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
DISPLAY_DECIMAL_PLACES = 18


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_field(raw: str, key: str) -> str:
    prefix = f"{key}="
    lines = raw.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith(prefix):
            continue
        value = line[len(prefix) :]
        balance = value.count("{") - value.count("}")
        cursor = index + 1
        while balance > 0 and cursor < len(lines):
            value += "\n" + lines[cursor]
            balance += lines[cursor].count("{") - lines[cursor].count("}")
            cursor += 1
        if balance != 0:
            raise ValueError(f"unbalanced field {key}")
        return value
    raise ValueError(f"missing field {key}")


def parse_intervals(value: str, expected: int) -> list[tuple[Fraction, Fraction]]:
    parsed = [
        (Fraction(lower), Fraction(upper))
        for lower, upper in INTERVAL_PATTERN.findall(value)
    ]
    if len(parsed) != expected:
        raise ValueError(f"expected {expected} intervals, found {len(parsed)}")
    return parsed


def fixed_decimal(scaled_integer: int, decimal_places: int) -> str:
    """Format an integer multiple of 10^-decimal_places without rounding."""

    scale = 10**decimal_places
    sign = "-" if scaled_integer < 0 else ""
    whole, fractional = divmod(abs(scaled_integer), scale)
    return f"{sign}{whole}.{fractional:0{decimal_places}d}"


def directed_decimal_enclosure(
    value: Fraction, decimal_places: int = DISPLAY_DECIMAL_PLACES
) -> tuple[str, str]:
    """Return exact decimal-grid floor/ceil strings enclosing ``value``."""

    scale = 10**decimal_places
    scaled_numerator = value.numerator * scale
    floor_integer = scaled_numerator // value.denominator
    ceil_integer = -((-scaled_numerator) // value.denominator)
    return (
        fixed_decimal(floor_integer, decimal_places),
        fixed_decimal(ceil_integer, decimal_places),
    )


def fraction_payload(value: Fraction) -> dict[str, str | int]:
    decimal_floor, decimal_ceil = directed_decimal_enclosure(value)
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal_places": DISPLAY_DECIMAL_PLACES,
        "decimal_floor": decimal_floor,
        "decimal_ceil": decimal_ceil,
    }


def overlap(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def resolve_manifest_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_l1_monodromy_gap",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite result directory: {output}")
    output.mkdir(parents=True)

    accepted_hash_gates = {
        str(path): sha256(path) == expected
        for path, expected in EXPECTED_ACCEPTED_HASHES.items()
    }
    if not all(accepted_hash_gates.values()):
        raise RuntimeError(f"accepted archive hash mismatch: {accepted_hash_gates}")

    accepted_summary = json.loads(
        (ACCEPTED / "summary.json").read_text(encoding="utf-8")
    )
    accepted_manifest = json.loads(
        (ACCEPTED / "manifest.json").read_text(encoding="utf-8")
    )
    accepted_checker = json.loads(
        (ACCEPTED / "independent_checker.json").read_text(encoding="utf-8")
    )
    accepted_postcheck = json.loads(
        (ACCEPTED / "POSTCHECK_STATUS.json").read_text(encoding="utf-8")
    )
    status_gate = (
        accepted_summary["milestone_status"] == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and accepted_summary["final_status"] is None
        and accepted_checker["checker_status"] == "PASS"
        and accepted_postcheck["checker_status"] == "PASS"
    )
    if not status_gate:
        raise RuntimeError("accepted L1-V2 status gate failed")

    manifest_hash_gates = {
        name: resolve_manifest_path(name).is_file()
        and sha256(resolve_manifest_path(name)) == digest
        for name, digest in accepted_manifest["files"].items()
    }
    if not all(manifest_hash_gates.values()):
        raise RuntimeError("accepted transcript manifest hash failure")

    records: list[dict[str, Any]] = []
    exact_intervals: dict[tuple[int, str], tuple[Fraction, Fraction]] = {}
    exact_phase_slopes: dict[tuple[int, str], tuple[Fraction, Fraction]] = {}
    for accepted_record in accepted_summary["records"]:
        raw_path = ACCEPTED / accepted_record["raw_file"]
        raw = raw_path.read_text(encoding="utf-8")
        monodromy = parse_intervals(extract_field(raw, "monodromy_box"), 36)
        phase_slope = parse_intervals(
            extract_field(raw, "phase_gradient_qplus"), 1
        )[0]
        diagonal = [monodromy[index] for index in (0, 7, 14, 21)]
        trace_lower = sum(value[0] for value in diagonal)
        trace_upper = sum(value[1] for value in diagonal)
        determinant_interval = (Fraction(4) - trace_upper, Fraction(4) - trace_lower)
        bits = int(accepted_record["precision_bits"])
        job_id = str(accepted_record["job_id"])
        exact_intervals[(bits, job_id)] = determinant_interval
        exact_phase_slopes[(bits, job_id)] = phase_slope
        records.append(
            {
                "precision_bits": bits,
                "job_id": job_id,
                "job_type": accepted_record["job_type"],
                "raw_file": str(raw_path.relative_to(ROOT)),
                "d_m_lower": fraction_payload(determinant_interval[0]),
                "d_m_upper": fraction_payload(determinant_interval[1]),
                "strictly_above_3": determinant_interval[0] > 3,
                "phase_slope_lower": fraction_payload(phase_slope[0]),
                "phase_slope_upper": fraction_payload(phase_slope[1]),
                "pplus_section_transverse": phase_slope[0] > 0,
            }
        )

    expected_keys = {
        (bits, f"S{index:03d}") for bits in (128, 256) for index in range(51)
    } | {
        (bits, f"B{index:03d}") for bits in (128, 256) for index in range(50)
    }
    exact_job_gate = set(exact_intervals) == expected_keys
    exact_phase_job_gate = set(exact_phase_slopes) == expected_keys
    gap_gate = all(interval[0] > 3 for interval in exact_intervals.values())
    phase_section_regularity_gate = all(
        interval[0] > 0 for interval in exact_phase_slopes.values()
    )
    cross_precision_gate = all(
        overlap(exact_intervals[(128, job_id)], exact_intervals[(256, job_id)])
        for _bits, job_id in expected_keys
        if _bits == 128
    )
    overall = (
        exact_job_gate
        and exact_phase_job_gate
        and gap_gate
        and phase_section_regularity_gate
        and cross_precision_gate
    )

    minimum_phase_key, minimum_phase_interval = min(
        exact_phase_slopes.items(), key=lambda item: item[1][0]
    )

    per_precision: dict[str, Any] = {}
    for bits in (128, 256):
        items = [
            (key, value)
            for key, value in exact_intervals.items()
            if key[0] == bits
        ]
        minimum_key, minimum_interval = min(items, key=lambda item: item[1][0])
        widest_key, widest_interval = max(
            items, key=lambda item: item[1][1] - item[1][0]
        )
        per_precision[str(bits)] = {
            "job_count": len(items),
            "minimum_lower_job": minimum_key[1],
            "minimum_lower": fraction_payload(minimum_interval[0]),
            "minimum_interval_upper": fraction_payload(minimum_interval[1]),
            "widest_job": widest_key[1],
            "maximum_width": fraction_payload(widest_interval[1] - widest_interval[0]),
        }

    summary = {
        "protocol_id": "R401-VAL-L1-MG-V2",
        "milestone_status": "PASS_LOCAL_MONODROMY_GAP" if overall else "FAIL",
        "final_status": None,
        "claim_boundary": (
            "det(I-DPi)=4-tr(M)>3 only on the already certified local fast "
            "branch; no independent event-projected determinant, Taylor-model "
            "identity residual, root complement, global cover, delta_tr, or arithmetic claim"
        ),
        "accepted_archive_hash_gates": accepted_hash_gates,
        "accepted_manifest_hash_count": len(manifest_hash_gates),
        "accepted_manifest_hash_gate": all(manifest_hash_gates.values()),
        "accepted_status_gate": status_gate,
        "exact_job_gate": exact_job_gate,
        "exact_phase_job_gate": exact_phase_job_gate,
        "strict_gap_gate": gap_gate,
        "phase_section_regularity_gate": phase_section_regularity_gate,
        "phase_section_regularity": {
            "section": "P_plus=0 on K_epsilon=1",
            "hamilton_equation": "dot(P_plus)=-partial(K_epsilon)/partial(Q_plus)",
            "minimum_phase_slope_job": minimum_phase_key[1],
            "minimum_phase_slope_precision_bits": minimum_phase_key[0],
            "minimum_phase_slope_lower": fraction_payload(
                minimum_phase_interval[0]
            ),
        },
        "cross_precision_overlap_gate": cross_precision_gate,
        "decimal_display_policy": {
            "decimal_places": DISPLAY_DECIMAL_PLACES,
            "lower_bound_display": "floor(exact_value * 10^places) / 10^places",
            "upper_bound_display": "ceil(exact_value * 10^places) / 10^places",
            "exact_rational_retained": True,
            "binary_float_conversion_forbidden": True,
        },
        "per_precision": per_precision,
        "records": sorted(
            records, key=lambda record: (record["precision_bits"], record["job_id"])
        ),
    }
    summary_path = output / "summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    report = f"""# R401-VAL-L1-MG-V2 local monodromy gap

Milestone status: **{summary['milestone_status']}**.

Exact-rational parsing of all 202 frozen CAPD monodromy enclosures proves
`D_M = 4 - tr(M) > 3` throughout the accepted local fast branch.

Every displayed decimal below has exactly {DISPLAY_DECIMAL_PLACES} places and
is generated directly from the exact fraction.  Lower bounds are rounded
downward and upper bounds are rounded upward; no binary floating-point
conversion is used.

- 128-bit minimum lower bound (downward):
  `{per_precision['128']['minimum_lower']['decimal_floor']}` at
  `{per_precision['128']['minimum_lower_job']}`; exact
  `{per_precision['128']['minimum_lower']['numerator']}/{per_precision['128']['minimum_lower']['denominator']}`;
- 256-bit minimum lower bound (downward):
  `{per_precision['256']['minimum_lower']['decimal_floor']}` at
  `{per_precision['256']['minimum_lower_job']}`; exact
  `{per_precision['256']['minimum_lower']['numerator']}/{per_precision['256']['minimum_lower']['denominator']}`;
- 128-bit maximum interval width (upward):
  `{per_precision['128']['maximum_width']['decimal_ceil']}`; exact
  `{per_precision['128']['maximum_width']['numerator']}/{per_precision['128']['maximum_width']['denominator']}`;
- 256-bit maximum interval width (upward):
  `{per_precision['256']['maximum_width']['decimal_ceil']}`; exact
  `{per_precision['256']['maximum_width']['numerator']}/{per_precision['256']['maximum_width']['denominator']}`;
- inherited all-job phase-slope lower bound (downward):
  `{summary['phase_section_regularity']['minimum_phase_slope_lower']['decimal_floor']}`
  at {summary['phase_section_regularity']['minimum_phase_slope_precision_bits']}-bit
  `{summary['phase_section_regularity']['minimum_phase_slope_job']}`; exact
  `{summary['phase_section_regularity']['minimum_phase_slope_lower']['numerator']}/{summary['phase_section_regularity']['minimum_phase_slope_lower']['denominator']}`;
- every paired 128/256 interval intersects.

The inherited positive phase-slope certificate gives
`dK_epsilon/dQ_plus > 0` at the `P_plus=0` event.  Thus the energy shell is
regular there and `dot(P_plus)=-dK_epsilon/dQ_plus` is nonzero, so the event
section is transverse to the Hamiltonian flow.  Hamiltonian symplecticity
and the invariant flag
`span(X_K) subset ker(dK) subset T_z(R^4)` give
`chi_M(t)=(t-1)^2 chi_DPi(t)` on the quotient, including possible unit
Jordan blocks.  Hence `D_M` is the determinant of the energy-section
transverse Poincare return on the periodic orbit.  This is a local-branch gap
only.  The independent event-projected determinant,
Taylor-model residual, root-complement tree, global cover, and `delta_tr`
promotion remain open.
"""
    report_path = output / "R401_VAL_L1_MONODROMY_GAP_REPORT.md"
    report_path.write_text(report, encoding="utf-8")

    hash_targets = [
        PROTOCOL,
        ANALYZER,
        ACCEPTED / "summary.json",
        ACCEPTED / "manifest.json",
        ACCEPTED / "independent_checker.json",
        ACCEPTED / "POSTCHECK_STATUS.json",
        summary_path,
        report_path,
    ]
    manifest = {
        "protocol_id": "R401-VAL-L1-MG-V2",
        "milestone_status": summary["milestone_status"],
        "final_status": None,
        "files": {
            str(path.relative_to(ROOT)): sha256(path) for path in hash_targets
        },
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": summary["milestone_status"],
                "records": len(records),
                "output": str(output),
            },
            indent=2,
        )
    )
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
