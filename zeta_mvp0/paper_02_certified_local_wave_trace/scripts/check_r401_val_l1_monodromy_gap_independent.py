#!/usr/bin/env python3
"""Independent exact-rational replay of the L1 local monodromy gap."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACCEPTED = ROOT / "results/r401_val_l1_branch"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L1_MONODROMY_GAP_PROTOCOL.md"
ANALYZER = ROOT / "scripts/run_r401_val_l1_monodromy_gap.py"
CHECKER = Path(__file__).resolve()
EXPECTED_HASHES = {
    PROTOCOL: "760fc64f8d240edb352782272b95f0ce2fc4e78faefc643d2e4956aae25b138a",
    ANALYZER: "40b84dd6cc0fa8507b88640e52520e7bb80153d6b89d06d16b578566dbd6f0c0",
    ACCEPTED / "summary.json": "e9a71dfd61d26396d05b62a848f49577fdabdf3722101432455435d32bb7503c",
    ACCEPTED / "manifest.json": "3c653e50042050e69a8928dd1fc7dac3464b6ae8e7ea8d47c70a03e970ece860",
    ACCEPTED / "independent_checker.json": "a6c0db0fc2190013c221d0ecdd71ac6f86895fbaecad735e1f2814ea232280c2",
}

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
DISPLAY_DECIMAL_PLACES = 18
FIXED_DECIMAL_PATTERN = re.compile(r"^-?\d+\.\d{18}$")


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


def monodromy_gap(raw: str) -> tuple[Fraction, Fraction]:
    entries = [
        (Fraction(lower), Fraction(upper))
        for lower, upper in INTERVAL_PATTERN.findall(
            extract_field(raw, "monodromy_box")
        )
    ]
    if len(entries) != 36:
        raise ValueError(f"expected 36 monodromy entries, found {len(entries)}")
    diagonal = [entries[index] for index in (0, 7, 14, 21)]
    return (
        Fraction(4) - sum(value[1] for value in diagonal),
        Fraction(4) - sum(value[0] for value in diagonal),
    )


def phase_slope(raw: str) -> tuple[Fraction, Fraction]:
    entries = [
        (Fraction(lower), Fraction(upper))
        for lower, upper in INTERVAL_PATTERN.findall(
            extract_field(raw, "phase_gradient_qplus")
        )
    ]
    if len(entries) != 1:
        raise ValueError(f"expected one phase-slope interval, found {len(entries)}")
    return entries[0]


def payload_fraction(payload: dict[str, object]) -> Fraction:
    return Fraction(int(payload["numerator"]), int(payload["denominator"]))


def fixed_decimal(scaled_integer: int, decimal_places: int) -> str:
    scale = 10**decimal_places
    sign = "-" if scaled_integer < 0 else ""
    whole, fractional = divmod(abs(scaled_integer), scale)
    return f"{sign}{whole}.{fractional:0{decimal_places}d}"


def directed_decimal_enclosure(value: Fraction) -> tuple[str, str]:
    scale = 10**DISPLAY_DECIMAL_PLACES
    scaled_numerator = value.numerator * scale
    floor_integer = scaled_numerator // value.denominator
    ceil_integer = -((-scaled_numerator) // value.denominator)
    return (
        fixed_decimal(floor_integer, DISPLAY_DECIMAL_PLACES),
        fixed_decimal(ceil_integer, DISPLAY_DECIMAL_PLACES),
    )


def payload_conditions(
    payload: dict[str, object], expected: Fraction
) -> dict[str, bool]:
    expected_floor, expected_ceil = directed_decimal_enclosure(expected)
    stored_floor = str(payload.get("decimal_floor", ""))
    stored_ceil = str(payload.get("decimal_ceil", ""))
    try:
        floor_fraction = Fraction(stored_floor)
        ceil_fraction = Fraction(stored_ceil)
    except (ValueError, ZeroDivisionError):
        floor_fraction = Fraction(1)
        ceil_fraction = Fraction(-1)
    scale = Fraction(1, 10**DISPLAY_DECIMAL_PLACES)
    return {
        "exact_fraction": payload_fraction(payload) == expected,
        "decimal_places": payload.get("decimal_places") == DISPLAY_DECIMAL_PLACES,
        "fixed_floor_format": FIXED_DECIMAL_PATTERN.fullmatch(stored_floor) is not None,
        "fixed_ceil_format": FIXED_DECIMAL_PATTERN.fullmatch(stored_ceil) is not None,
        "exact_floor_string": stored_floor == expected_floor,
        "exact_ceil_string": stored_ceil == expected_ceil,
        "directed_enclosure": floor_fraction <= expected <= ceil_fraction,
        "at_most_one_grid_unit": Fraction(0) <= ceil_fraction - floor_fraction <= scale,
    }


def overlap(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def resolve(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--result",
        type=Path,
        default=ROOT / "results/r401_val_l1_monodromy_gap",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = args.result.resolve()
    summary_path = result / "summary.json"
    manifest_path = result / "manifest.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    accepted_summary = json.loads(
        (ACCEPTED / "summary.json").read_text(encoding="utf-8")
    )
    accepted_manifest = json.loads(
        (ACCEPTED / "manifest.json").read_text(encoding="utf-8")
    )

    frozen_hash_gates = {
        str(path): sha256(path) == expected for path, expected in EXPECTED_HASHES.items()
    }
    result_manifest_gates = {
        name: resolve(name).is_file() and sha256(resolve(name)) == digest
        for name, digest in manifest["files"].items()
    }
    accepted_manifest_gates = {
        name: resolve(name).is_file() and sha256(resolve(name)) == digest
        for name, digest in accepted_manifest["files"].items()
    }

    archived_records = {
        (int(record["precision_bits"]), str(record["job_id"])): record
        for record in summary["records"]
    }
    replayed: dict[tuple[int, str], tuple[Fraction, Fraction]] = {}
    replayed_phase_slopes: dict[tuple[int, str], tuple[Fraction, Fraction]] = {}
    failures: list[dict[str, object]] = []
    atomic_replay_check_count = 0
    directed_decimal_payload_count = 0
    record_failure_count = 0

    def add_payload_checks(
        conditions: dict[str, bool],
        prefix: str,
        stored_payload: dict[str, object],
        expected: Fraction,
    ) -> None:
        nonlocal directed_decimal_payload_count
        directed_decimal_payload_count += 1
        for name, passed in payload_conditions(stored_payload, expected).items():
            conditions[f"{prefix}.{name}"] = passed

    for accepted_record in accepted_summary["records"]:
        key = (
            int(accepted_record["precision_bits"]),
            str(accepted_record["job_id"]),
        )
        try:
            raw = (ACCEPTED / accepted_record["raw_file"]).read_text(
                encoding="utf-8"
            )
            interval = monodromy_gap(raw)
            slope = phase_slope(raw)
            replayed[key] = interval
            replayed_phase_slopes[key] = slope
            stored = archived_records[key]
            conditions = {
                "ordered": interval[0] <= interval[1],
                "strictly_above_3": interval[0] > 3,
                "stored_gate": stored["strictly_above_3"] is True,
                "phase_slope_ordered": slope[0] <= slope[1],
                "positive_phase_slope": slope[0] > 0,
                "stored_section_transversality_gate": (
                    stored["pplus_section_transverse"] is True
                ),
            }
            add_payload_checks(conditions, "d_m_lower", stored["d_m_lower"], interval[0])
            add_payload_checks(conditions, "d_m_upper", stored["d_m_upper"], interval[1])
            add_payload_checks(
                conditions,
                "phase_slope_lower",
                stored["phase_slope_lower"],
                slope[0],
            )
            add_payload_checks(
                conditions,
                "phase_slope_upper",
                stored["phase_slope_upper"],
                slope[1],
            )
            atomic_replay_check_count += len(conditions)
            if not all(conditions.values()):
                record_failure_count += 1
                failures.append(
                    {
                        "scope": "record",
                        "precision_bits": key[0],
                        "job_id": key[1],
                        "failed": [name for name, value in conditions.items() if not value],
                    }
                )
        except Exception as error:
            record_failure_count += 1
            failures.append(
                {
                    "scope": "record",
                    "precision_bits": key[0],
                    "job_id": key[1],
                    "exception": f"{type(error).__name__}: {error}",
                }
            )

    expected_keys = {
        (bits, f"S{index:03d}") for bits in (128, 256) for index in range(51)
    } | {
        (bits, f"B{index:03d}") for bits in (128, 256) for index in range(50)
    }
    exact_job_set = set(replayed) == expected_keys == set(archived_records)
    exact_phase_job_set = set(replayed_phase_slopes) == expected_keys
    precision_overlap = exact_job_set and all(
        overlap(replayed[(128, job_id)], replayed[(256, job_id)])
        for bits, job_id in expected_keys
        if bits == 128
    )

    aggregate_conditions: dict[str, bool] = {}
    for bits in (128, 256):
        items = [(key, value) for key, value in replayed.items() if key[0] == bits]
        minimum_key, minimum_interval = min(items, key=lambda item: item[1][0])
        widest_key, widest_interval = max(
            items, key=lambda item: item[1][1] - item[1][0]
        )
        stored = summary["per_precision"][str(bits)]
        aggregate_conditions.update(
            {
                f"{bits}.job_count": stored["job_count"] == 101,
                f"{bits}.minimum_lower_job": (
                    stored["minimum_lower_job"] == minimum_key[1]
                ),
                f"{bits}.widest_job": stored["widest_job"] == widest_key[1],
            }
        )
        add_payload_checks(
            aggregate_conditions,
            f"{bits}.minimum_lower",
            stored["minimum_lower"],
            minimum_interval[0],
        )
        add_payload_checks(
            aggregate_conditions,
            f"{bits}.minimum_interval_upper",
            stored["minimum_interval_upper"],
            minimum_interval[1],
        )
        add_payload_checks(
            aggregate_conditions,
            f"{bits}.maximum_width",
            stored["maximum_width"],
            widest_interval[1] - widest_interval[0],
        )

    minimum_phase_key, minimum_phase_interval = min(
        replayed_phase_slopes.items(), key=lambda item: item[1][0]
    )
    stored_phase = summary["phase_section_regularity"]
    aggregate_conditions.update(
        {
            "phase.section": stored_phase["section"] == "P_plus=0 on K_epsilon=1",
            "phase.hamilton_equation": (
                stored_phase["hamilton_equation"]
                == "dot(P_plus)=-partial(K_epsilon)/partial(Q_plus)"
            ),
            "phase.minimum_job": (
                stored_phase["minimum_phase_slope_job"] == minimum_phase_key[1]
            ),
            "phase.minimum_precision": (
                stored_phase["minimum_phase_slope_precision_bits"]
                == minimum_phase_key[0]
            ),
        }
    )
    add_payload_checks(
        aggregate_conditions,
        "phase.minimum_lower",
        stored_phase["minimum_phase_slope_lower"],
        minimum_phase_interval[0],
    )

    policy = summary["decimal_display_policy"]
    aggregate_conditions.update(
        {
            "policy.decimal_places": (
                policy["decimal_places"] == DISPLAY_DECIMAL_PLACES
            ),
            "policy.lower_is_floor": policy["lower_bound_display"].startswith("floor("),
            "policy.upper_is_ceil": policy["upper_bound_display"].startswith("ceil("),
            "policy.exact_rational": policy["exact_rational_retained"] is True,
            "policy.binary_float_forbidden": (
                policy["binary_float_conversion_forbidden"] is True
                and "float(" not in ANALYZER.read_text(encoding="utf-8")
            ),
        }
    )

    report = (result / "R401_VAL_L1_MONODROMY_GAP_REPORT.md").read_text(
        encoding="utf-8"
    )
    report_conditions: dict[str, bool] = {
        "states_direction_policy": (
            "Lower bounds are rounded\ndownward and upper bounds are rounded upward"
            in report
        ),
        "states_no_binary_float": "no binary floating-point\nconversion" in report,
    }
    for bits in (128, 256):
        stored = summary["per_precision"][str(bits)]
        lower = stored["minimum_lower"]
        width = stored["maximum_width"]
        report_conditions[f"{bits}.lower_uses_floor"] = (
            f"`{lower['decimal_floor']}`" in report
        )
        report_conditions[f"{bits}.lower_exact_fraction"] = (
            f"`{lower['numerator']}/{lower['denominator']}`" in report
        )
        report_conditions[f"{bits}.width_uses_ceil"] = (
            f"`{width['decimal_ceil']}`" in report
        )
        report_conditions[f"{bits}.width_exact_fraction"] = (
            f"`{width['numerator']}/{width['denominator']}`" in report
        )
    phase_payload = stored_phase["minimum_phase_slope_lower"]
    report_conditions.update(
        {
            "phase.lower_uses_floor": (
                f"`{phase_payload['decimal_floor']}`" in report
            ),
            "phase.exact_fraction": (
                f"`{phase_payload['numerator']}/{phase_payload['denominator']}`"
                in report
            ),
            "phase.section_regularity_explained": (
                "energy shell is\nregular" in report
                and "event\nsection is transverse" in report
            ),
            "invariant_quotient_identity_explained": (
                "invariant flag" in report
                and "`chi_M(t)=(t-1)^2 chi_DPi(t)`" in report
                and "unit\nJordan blocks" in report
            ),
        }
    )
    atomic_replay_check_count += len(aggregate_conditions) + len(report_conditions)
    if not all(aggregate_conditions.values()):
        failures.append(
            {
                "scope": "aggregate",
                "failed": [
                    name for name, value in aggregate_conditions.items() if not value
                ],
            }
        )
    if not all(report_conditions.values()):
        failures.append(
            {
                "scope": "report",
                "failed": [name for name, value in report_conditions.items() if not value],
            }
        )

    global_gates = {
        "frozen_hashes": all(frozen_hash_gates.values()),
        "result_manifest_hashes": all(result_manifest_gates.values()),
        "accepted_manifest_hashes": all(accepted_manifest_gates.values()),
        "status_namespace": (
            summary["protocol_id"] == "R401-VAL-L1-MG-V2"
            and summary["milestone_status"] == "PASS_LOCAL_MONODROMY_GAP"
            and summary["final_status"] is None
            and manifest["protocol_id"] == "R401-VAL-L1-MG-V2"
            and manifest["milestone_status"] == "PASS_LOCAL_MONODROMY_GAP"
            and manifest["final_status"] is None
        ),
        "exact_job_set": exact_job_set,
        "exact_phase_job_set": exact_phase_job_set,
        "all_202_exact_replays": len(replayed) == 202 and record_failure_count == 0,
        "all_202_phase_slope_replays": (
            len(replayed_phase_slopes) == 202
            and all(interval[0] > 0 for interval in replayed_phase_slopes.values())
        ),
        "all_directional_decimal_payloads": (
            directed_decimal_payload_count == 815
            and record_failure_count == 0
            and all(aggregate_conditions.values())
            and all(report_conditions.values())
        ),
        "cross_precision_overlap": precision_overlap,
    }
    overall = all(global_gates.values())
    payload = {
        "protocol_id": "R401-VAL-L1-MG-V2",
        "checker_status": "PASS" if overall else "FAIL",
        "milestone_status": "PASS_LOCAL_MONODROMY_GAP" if overall else None,
        "final_status": None,
        "scope": (
            "independent exact-rational replay of 4-tr(M) from frozen CAPD "
            "monodromy and phase-slope transcripts, including independent "
            "floor/ceil decimal rendering; not a second ODE integration or the "
            "independent event-projected DPi/Taylor-model cross-check"
        ),
        "global_gates": global_gates,
        "replay_count": len(replayed),
        "phase_slope_replay_count": len(replayed_phase_slopes),
        "directed_decimal_payload_count": directed_decimal_payload_count,
        "failures": failures,
        "aggregate_check_count": (
            len(frozen_hash_gates)
            + len(result_manifest_gates)
            + len(accepted_manifest_gates)
            + len(global_gates)
            + atomic_replay_check_count
            + 101
        ),
    }
    checker_path = result / "independent_checker.json"
    checker_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    postcheck = {
        "protocol_id": "R401-VAL-L1-MG-V2",
        "checker_status": payload["checker_status"],
        "milestone_status": payload["milestone_status"],
        "final_status": None,
        "files": {
            str(CHECKER.relative_to(ROOT)): sha256(CHECKER),
            str(summary_path.relative_to(ROOT)): sha256(summary_path),
            str(manifest_path.relative_to(ROOT)): sha256(manifest_path),
            str(checker_path.relative_to(ROOT)): sha256(checker_path),
        },
    }
    (result / "POSTCHECK_STATUS.json").write_text(
        json.dumps(postcheck, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": payload["checker_status"],
                "replays": len(replayed),
                "phase_slope_replays": len(replayed_phase_slopes),
                "directed_decimal_payloads": directed_decimal_payload_count,
                "failures": len(failures),
                "aggregate_checks": payload["aggregate_check_count"],
            },
            indent=2,
        )
    )
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
