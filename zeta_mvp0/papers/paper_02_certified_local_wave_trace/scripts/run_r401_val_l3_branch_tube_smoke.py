#!/usr/bin/env python3
"""Run the isolated NON_LICENSING A4.16b branch-tube prototype.

The six jobs are the accepted A4.12 primary boxes S000/S025/S050 at 128
and 256 MPFR bits.  This runner deliberately has no authority to assign a
milestone, theorem, or final status.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shlex
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_phase_branch_tube_mp.cpp"
CHECKER = ROOT / "scripts/check_r401_val_l3_branch_tube_smoke_independent.py"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"
RUNNER = Path(__file__).resolve()

EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
PRECISIONS = (128, 256)
PHASE_GRID = 64
TUBE_RADIUS_SQ = Decimal(1) / Decimal(625)

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
SCALAR_PATTERN = re.compile(rf"\s*({NUMBER})\s*")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command_output(command: list[str]) -> str:
    return subprocess.run(
        command, check=True, text=True, capture_output=True
    ).stdout.strip()


def extract_unique_field(raw: str, key: str) -> str:
    prefix = f"{key}="
    values = [line[len(prefix) :] for line in raw.splitlines() if line.startswith(prefix)]
    if len(values) != 1:
        raise ValueError(f"expected one {key} field, found {len(values)}")
    return values[0]


def parse_interval(value: str) -> tuple[Decimal, Decimal]:
    matches = INTERVAL_PATTERN.findall(value)
    if len(matches) != 1:
        raise ValueError(f"expected one interval, found {len(matches)}")
    lower, upper = (Decimal(item) for item in matches[0])
    if lower > upper:
        raise ValueError("reversed interval")
    return lower, upper


def parse_intervals(value: str, expected: int) -> list[tuple[Decimal, Decimal]]:
    matches = INTERVAL_PATTERN.findall(value)
    if len(matches) != expected:
        raise ValueError(f"expected {expected} intervals, found {len(matches)}")
    parsed = [(Decimal(lower), Decimal(upper)) for lower, upper in matches]
    if any(lower > upper for lower, upper in parsed):
        raise ValueError("reversed interval")
    return parsed


def parse_scalar(value: str) -> Decimal:
    """Parse CAPD scalar output (SolutionCurve domains are not intervals)."""
    match = SCALAR_PATTERN.fullmatch(value)
    if match is None:
        raise ValueError("expected one CAPD scalar")
    return Decimal(match.group(1))


def json_interval(value: tuple[Decimal, Decimal]) -> list[str]:
    return [str(value[0]), str(value[1])]


def json_intervals(
    values: list[tuple[Decimal, Decimal]],
) -> list[list[str]]:
    return [json_interval(value) for value in values]


def parse_transcript(raw: str) -> dict[str, Any]:
    if extract_unique_field(raw, "licensing") != "NON_LICENSING":
        raise ValueError("prototype licensing field is not NON_LICENSING")
    if extract_unique_field(raw, "protocol_id") != "R401-VAL-L3-BT-S0":
        raise ValueError("unexpected prototype protocol")
    for key in ("milestone_status", "theorem_status", "final_status"):
        if extract_unique_field(raw, key) != "null":
            raise ValueError(f"producer assigned {key}")
    precision_bits = int(extract_unique_field(raw, "precision_bits"))
    if precision_bits not in PRECISIONS:
        raise ValueError("precision mismatch")
    if int(extract_unique_field(raw, "taylor_order")) != 24:
        raise ValueError("Taylor order mismatch")
    expected_tolerance = "1e-30" if precision_bits == 128 else "1e-60"
    if extract_unique_field(raw, "tolerance") != expected_tolerance:
        raise ValueError("tolerance mismatch")
    if int(extract_unique_field(raw, "phase_grid")) != PHASE_GRID:
        raise ValueError("phase grid mismatch")
    omega_slow = parse_interval(extract_unique_field(raw, "omega_slow"))
    if omega_slow[0] <= 0:
        raise ValueError("printed slow frequency is not positive")
    tube_radius_sq = parse_interval(extract_unique_field(raw, "tube_radius_sq"))
    if not (tube_radius_sq[0] <= TUBE_RADIUS_SQ <= tube_radius_sq[1]):
        raise ValueError("printed tube radius does not enclose 0.04^2")

    phases: list[tuple[Decimal, Decimal]] = []
    maximum_segment_upper = Decimal(0)
    minimum_margin_lower: Decimal | None = None
    for index in range(PHASE_GRID):
        prefix = f"segment_{index:03d}"
        phase = parse_interval(extract_unique_field(raw, f"{prefix}_phase"))
        parse_intervals(extract_unique_field(raw, f"{prefix}_state"), 6)
        rslow_sq = parse_interval(extract_unique_field(raw, f"{prefix}_rslow_sq"))
        margin_sq = parse_interval(extract_unique_field(raw, f"{prefix}_margin_sq"))
        inside = extract_unique_field(raw, f"{prefix}_inside")
        if inside != "1" or margin_sq[0] <= 0 or rslow_sq[1] >= TUBE_RADIUS_SQ:
            raise ValueError(f"uncertified tube segment {index}")
        expected_phase = (
            Decimal(index) / Decimal(PHASE_GRID),
            Decimal(index + 1) / Decimal(PHASE_GRID),
        )
        if phase != expected_phase:
            raise ValueError(f"phase cell {index} is not the fixed dyadic cell")
        phases.append(phase)
        maximum_segment_upper = max(maximum_segment_upper, rslow_sq[1])
        minimum_margin_lower = (
            margin_sq[0]
            if minimum_margin_lower is None
            else min(minimum_margin_lower, margin_sq[0])
        )

    if phases[0][0] > 0 or phases[-1][1] < 1:
        raise ValueError("phase grid misses an endpoint")
    if any(left[1] < right[0] for left, right in zip(phases, phases[1:], strict=False)):
        raise ValueError("phase grid has a coverage gap")

    reported_maximum = parse_interval(
        extract_unique_field(raw, "maximum_rslow_sq_upper")
    )
    if not (reported_maximum[0] <= maximum_segment_upper <= reported_maximum[1]):
        raise ValueError("reported maximum does not enclose the replayed maximum")
    left_domain = parse_scalar(extract_unique_field(raw, "solution_left_domain"))
    right_domain = parse_scalar(extract_unique_field(raw, "solution_right_domain"))
    if left_domain != 0:
        raise ValueError("SolutionCurve left domain is not zero")
    if right_domain != 1:
        raise ValueError("SolutionCurve right domain is not one")
    if extract_unique_field(raw, "all_segments_inside") != "1":
        raise ValueError("aggregate tube gate is false")
    solution_piece_count = int(extract_unique_field(raw, "solution_piece_count"))
    if solution_piece_count <= 0:
        raise ValueError("SolutionCurve contains no pieces")
    status = extract_unique_field(raw, "status")
    return {
        "status": status,
        "precision_bits": precision_bits,
        "taylor_order": 24,
        "tolerance": expected_tolerance,
        "omega_slow": json_interval(omega_slow),
        "epsilon": json_interval(
            parse_interval(extract_unique_field(raw, "epsilon"))
        ),
        "root_box": json_intervals(
            parse_intervals(extract_unique_field(raw, "root_box"), 4)
        ),
        "terminal_state_box": json_intervals(
            parse_intervals(extract_unique_field(raw, "terminal_state_box"), 6)
        ),
        "solution_piece_count": solution_piece_count,
        "maximum_rslow_sq_upper": str(reported_maximum[1]),
        "maximum_segment_rslow_sq_upper": str(maximum_segment_upper),
        "minimum_margin_sq_lower": str(minimum_margin_lower),
        "all_segments_inside": extract_unique_field(raw, "all_segments_inside") == "1",
        "phase_cover_complete": True,
    }


def validate_upstream() -> tuple[dict[str, Any], dict[str, str]]:
    required = (L1_SUMMARY, L1_MANIFEST, L1_CHECKER, L1_POSTCHECK, L1_RELEASE)
    if any(not path.is_file() for path in required):
        raise FileNotFoundError("accepted A4.12 release chain is incomplete")
    summary = json.loads(L1_SUMMARY.read_text(encoding="utf-8"))
    manifest = json.loads(L1_MANIFEST.read_text(encoding="utf-8"))
    checker = json.loads(L1_CHECKER.read_text(encoding="utf-8"))
    postcheck = json.loads(L1_POSTCHECK.read_text(encoding="utf-8"))
    release = json.loads(L1_RELEASE.read_text(encoding="utf-8"))
    gates = {
        "summary_status": summary.get("milestone_status")
        == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and summary.get("final_status") is None,
        "manifest_status": manifest.get("milestone_status")
        == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and manifest.get("final_status") is None,
        "checker_status": checker.get("checker_status") == "PASS"
        and checker.get("final_status") is None,
        "postcheck_status": postcheck.get("checker_status") == "PASS"
        and postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and postcheck.get("final_status") is None,
        "release_status": release.get("release_status")
        == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and release.get("final_status") is None,
    }
    if not all(gates.values()):
        raise RuntimeError(f"accepted A4.12 status gate failed: {gates}")
    hashes = {str(path.relative_to(ROOT)): sha256(path) for path in required}
    return summary, hashes


def selected_records(summary: dict[str, Any]) -> dict[tuple[int, str], dict[str, Any]]:
    selected: dict[tuple[int, str], dict[str, Any]] = {}
    for record in summary.get("records", []):
        key = (record.get("precision_bits"), record.get("job_id"))
        if (
            record.get("job_type") == "primary"
            and key[0] in PRECISIONS
            and key[1] in REPRESENTATIVE_SLABS
        ):
            if key in selected:
                raise RuntimeError(f"duplicate A4.12 primary record: {key}")
            if not record.get("passed") or record.get("status") != "PASS_LOCAL_SLAB":
                raise RuntimeError(f"unaccepted A4.12 primary record: {key}")
            selected[key] = record
    expected = {(bits, slab) for bits in PRECISIONS for slab in REPRESENTATIVE_SLABS}
    if set(selected) != expected:
        raise RuntimeError(f"wrong representative matrix: {set(selected)}")
    return selected


def job_arguments(binary: Path, record: dict[str, Any]) -> list[str]:
    arguments = [
        str(binary),
        str(record["precision_bits"]),
        *record["epsilon"][0],
    ]
    for interval in record["root_box"]:
        arguments.extend(interval)
    if len(arguments) != 12:
        raise AssertionError("branch-tube evaluator argv is not canonical")
    return arguments


def run_job(
    binary: Path,
    output: Path,
    bits: int,
    slab: str,
    record: dict[str, Any],
) -> dict[str, Any]:
    raw_dir = output / "raw" / str(bits)
    raw_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = raw_dir / f"{slab}.txt"
    stderr_path = raw_dir / f"{slab}.stderr.txt"
    command = job_arguments(binary, record)
    started = time.monotonic()
    process = subprocess.run(command, text=True, capture_output=True, timeout=600)
    wall_seconds = time.monotonic() - started
    stdout_path.write_text(process.stdout, encoding="utf-8")
    stderr_path.write_text(process.stderr, encoding="utf-8")
    result: dict[str, Any] = {
        "precision_bits": bits,
        "slab_id": slab,
        "returncode": process.returncode,
        "wall_seconds": wall_seconds,
        "raw_file": str(stdout_path.relative_to(output)),
        "stderr_file": str(stderr_path.relative_to(output)),
        "argv": command,
    }
    try:
        result.update(parse_transcript(process.stdout))
        expected_epsilon = tuple(Decimal(value) for value in record["epsilon"][0])
        expected_root_box = [
            tuple(Decimal(value) for value in interval)
            for interval in record["root_box"]
        ]
        printed_epsilon = tuple(Decimal(value) for value in result["epsilon"])
        printed_root_box = [
            tuple(Decimal(value) for value in interval)
            for interval in result["root_box"]
        ]
        result["input_echo_gate"] = (
            printed_epsilon[0] <= expected_epsilon[0] <= printed_epsilon[1]
            and printed_epsilon[0] <= expected_epsilon[1] <= printed_epsilon[1]
            and all(
                printed[0] <= expected[0] <= printed[1]
                and printed[0] <= expected[1] <= printed[1]
                for printed, expected in zip(
                    printed_root_box, expected_root_box, strict=True
                )
            )
        )
    except Exception as error:  # fail closed and retain the raw transcript
        result["parse_error"] = f"{type(error).__name__}: {error}"
    result["passed"] = (
        process.returncode == 0
        and result.get("status") == "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
        and result.get("precision_bits") == bits
        and result.get("all_segments_inside") is True
        and result.get("phase_cover_complete") is True
        and result.get("input_echo_gate") is True
        and not process.stderr
    )
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--capd-source",
        type=Path,
        default=Path("/root/autodl-tmp/zeta/dependencies/capd-r401-a1"),
    )
    parser.add_argument(
        "--capd-build",
        type=Path,
        default=Path("/root/autodl-tmp/zeta/dependencies/capd-r401-a1/build-mp"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_l3_branch_tube_smoke",
    )
    parser.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 1))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite result directory: {output}")
    output.mkdir(parents=True)

    l1_summary, upstream_hashes = validate_upstream()
    records = selected_records(l1_summary)
    capd_source = args.capd_source.resolve()
    capd_build = args.capd_build.resolve()
    capd_config = capd_build / "bin/capd-config"
    if not capd_config.is_file():
        raise FileNotFoundError(f"CAPD config not found: {capd_config}")
    commit = command_output(["git", "-C", str(capd_source), "rev-parse", "HEAD"])
    if commit != EXPECTED_CAPD_COMMIT:
        raise RuntimeError(f"unexpected CAPD commit: {commit}")
    flags = shlex.split(command_output([str(capd_config), "--cflags", "--libs"]))
    required_flags = {"-D__HAVE_MPFR__", "-lmpfr", "-lgmp", "-frounding-math"}
    if not required_flags.issubset(flags):
        raise RuntimeError(f"missing CAPD flags: {required_flags - set(flags)}")

    binary = output / "capd_r401_phase_branch_tube_mp"
    compile_command = ["g++", "-O2", str(SOURCE), *flags, "-o", str(binary)]
    compilation = subprocess.run(compile_command, text=True, capture_output=True)
    (output / "compile_stdout.txt").write_text(compilation.stdout, encoding="utf-8")
    (output / "compile_stderr.txt").write_text(compilation.stderr, encoding="utf-8")
    if compilation.returncode != 0:
        raise RuntimeError("branch-tube prototype compilation failed")

    started = time.monotonic()
    outcomes: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(run_job, binary, output, bits, slab, records[(bits, slab)]): (
                bits,
                slab,
            )
            for bits in PRECISIONS
            for slab in REPRESENTATIVE_SLABS
        }
        for future in as_completed(futures):
            outcomes.append(future.result())
    elapsed = time.monotonic() - started
    outcomes.sort(key=lambda item: (item["precision_bits"], item["slab_id"]))
    all_pass = len(outcomes) == 6 and all(item["passed"] for item in outcomes)
    pair_gate = all(
        sum(item["slab_id"] == slab for item in outcomes) == 2
        and all(
            item["passed"]
            for item in outcomes
            if item["slab_id"] == slab
        )
        for slab in REPRESENTATIVE_SLABS
    )
    prototype_status = (
        "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
        if all_pass and pair_gate
        else "INCONCLUSIVE_NON_LICENSING_BRANCH_TUBE_SMOKE"
    )
    summary = {
        "protocol_id": "R401-VAL-L3-BT-S0",
        "licensing": "NON_LICENSING",
        "prototype_status": prototype_status,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "claim_boundary": (
            "representative A4.12 branch-box full-period tube implementation "
            "smoke only; not phase completeness for arbitrary candidates, not "
            "a global shell cover, and no delta_tr, trace, arithmetic, zeta, or RH claim"
        ),
        "representative_slabs": list(REPRESENTATIVE_SLABS),
        "precisions": list(PRECISIONS),
        "phase_grid": PHASE_GRID,
        "tube_radius": "0.04",
        "tube_radius_sq": str(TUBE_RADIUS_SQ),
        "pair_gate": pair_gate,
        "records": outcomes,
        "elapsed_seconds": elapsed,
        "environment": {
            "platform": platform.platform(),
            "python": platform.python_version(),
            "capd_commit": commit,
            "capd_config_flags": flags,
            "compile_command": compile_command,
        },
        "input_hashes": {
            str(SOURCE.relative_to(ROOT)): sha256(SOURCE),
            str(RUNNER.relative_to(ROOT)): sha256(RUNNER),
            str(CHECKER.relative_to(ROOT)): sha256(CHECKER),
            str(DEPENDENCY.relative_to(ROOT)): sha256(DEPENDENCY),
            **upstream_hashes,
        },
    }
    summary_path = output / "summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    maximum_values = [
        Decimal(item["maximum_rslow_sq_upper"])
        for item in outcomes
        if "maximum_rslow_sq_upper" in item
    ]
    margin_values = [
        Decimal(item["minimum_margin_sq_lower"])
        for item in outcomes
        if "minimum_margin_sq_lower" in item
    ]
    maximum = max(maximum_values) if maximum_values else None
    minimum_margin = min(margin_values) if margin_values else None
    maximum_text = str(maximum) if maximum is not None else "null"
    minimum_margin_text = (
        str(minimum_margin) if minimum_margin is not None else "null"
    )
    report = f"""# R401-VAL-L3-BT-S0 branch-tube implementation smoke

Prototype status: `{prototype_status}`  
Licensing: `NON_LICENSING`  
Milestone status: `null`  
Theorem status: `null`  
Final status: `null`

The pinned CAPD multiprecision `SolutionCurve` integrated the accepted A4.12
primary boxes S000, S025, and S050 at 128 and 256 bits.  Each complete
normalized period was covered by {PHASE_GRID} closed dyadic phase cells.

- jobs passing: `{sum(item['passed'] for item in outcomes)}/6`;
- largest rigorous upper endpoint of `r_-^2`: `{maximum_text}`;
- smallest rigorous lower endpoint of `0.04^2-r_-^2`: `{minimum_margin_text}`;
- CAPD commit: `{commit}`.

This is an implementation smoke for the distinguished branch only.  It does
not show that an arbitrary return starting with small slow radius remains in
the tube, does not make the Poincare section complete modulo time translation,
and does not close a global shell, `delta_tr`, trace-formula, arithmetic,
zeta-zero, Hilbert--Polya, or RH gate.
"""
    (output / "R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md").write_text(
        report, encoding="utf-8"
    )
    manifest_targets = [
        SOURCE,
        RUNNER,
        CHECKER,
        DEPENDENCY,
        summary_path,
        output / "compile_stdout.txt",
        output / "compile_stderr.txt",
        output / "R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md",
        binary,
        *sorted((output / "raw").rglob("*.txt")),
        L1_SUMMARY,
        L1_MANIFEST,
        L1_CHECKER,
        L1_POSTCHECK,
        L1_RELEASE,
    ]
    manifest = {
        "protocol_id": "R401-VAL-L3-BT-S0",
        "licensing": "NON_LICENSING",
        "prototype_status": prototype_status,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "files": {str(path.resolve()): sha256(path) for path in manifest_targets},
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "prototype_status": prototype_status,
        "jobs": len(outcomes),
        "maximum_rslow_sq_upper": maximum_text,
        "minimum_margin_sq_lower": minimum_margin_text,
        "output": str(output),
    }, indent=2))
    return 0 if prototype_status == "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
