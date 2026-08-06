#!/usr/bin/env python3
"""Run the frozen R401-VAL-L1 contiguous local-branch certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shlex
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_local_slab_grid_mp.cpp"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN.json"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L1_PROTOCOL.md"
V2_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_PROTOCOL_V2_FREEZE.md"
RADIAL_PROOF = ROOT / "research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md"
WARPED_PROOF = ROOT / "research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md"
DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"
RUNNER = Path(__file__).resolve()

EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
EXPECTED_HASHES = {
    SOURCE: "9fb83e31937f8006e25cecbea818d74d90c107570f9369c9a03f7577894b1179",
    PLAN: "3d9698bd15f2d6f0d8632c364c9f2d26180b59f731da17d90fbd1d618227ca50",
    PROTOCOL: "3942d7ebcfbf4cb1b91962785869d11476745d2777c3169b1bca048218a8ff18",
    V2_FREEZE: "f6f99e7c4bdd86da332848badf439eb3ed5882b8c3fd355b28b2289cf5e049a0",
    RADIAL_PROOF: "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    WARPED_PROOF: "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8",
}

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
COORDINATES = ("q_slow", "q_fast", "p_slow", "period")


@dataclass(frozen=True)
class Job:
    job_id: str
    job_type: str
    epsilon_lower: str
    epsilon_upper: str
    center: dict[str, str]
    root_radii: dict[str, str]

    def arguments(self, binary: Path, bits: int) -> list[str]:
        return [
            str(binary),
            str(bits),
            self.epsilon_lower,
            self.epsilon_upper,
            *(self.center[key] for key in COORDINATES),
            *(self.root_radii[key] for key in COORDINATES),
        ]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command_output(command: list[str]) -> str:
    return subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


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


def parse_intervals(value: str, expected: int | None = None) -> list[tuple[str, str]]:
    intervals = [match.groups() for match in INTERVAL_PATTERN.finditer(value)]
    if expected is not None and len(intervals) != expected:
        raise ValueError(f"expected {expected} intervals, found {len(intervals)}")
    return intervals


def parse_bool(raw: str, key: str) -> bool:
    value = extract_field(raw, key).strip()
    if value not in {"0", "1"}:
        raise ValueError(f"invalid Boolean {key}={value}")
    return value == "1"


def parse_transcript(raw: str) -> dict[str, Any]:
    root_box = parse_intervals(extract_field(raw, "X"), 4)
    krawczyk = parse_intervals(extract_field(raw, "K"), 4)
    margins: list[tuple[str, str]] = []
    for x_value, k_value in zip(root_box, krawczyk, strict=True):
        margins.append(
            (
                str(Decimal(k_value[0]) - Decimal(x_value[0])),
                str(Decimal(x_value[1]) - Decimal(k_value[1])),
            )
        )
    minimum_margin = min(Decimal(value) for pair in margins for value in pair)
    defect_rows = parse_intervals(extract_field(raw, "defect_row_sums"), 4)
    phase_gradient = parse_intervals(extract_field(raw, "phase_gradient_qplus"), 1)[0]
    parsed = {
        "status": extract_field(raw, "status").strip(),
        "precision_bits": int(extract_field(raw, "precision_bits").strip()),
        "epsilon": parse_intervals(extract_field(raw, "epsilon"), 1),
        "root_box": root_box,
        "x_bar": parse_intervals(extract_field(raw, "x_bar"), 4),
        "f_center_count": len(parse_intervals(extract_field(raw, "F_center"))),
        "jacobian_count": len(parse_intervals(extract_field(raw, "J"))),
        "preconditioner_count": len(parse_intervals(extract_field(raw, "C"))),
        "defect_count": len(parse_intervals(extract_field(raw, "defect"))),
        "krawczyk_image": krawczyk,
        "recomputed_component_margins": margins,
        "minimum_recomputed_margin": str(minimum_margin),
        "maximum_defect_row_sum": str(
            max(Decimal(upper) for _lower, upper in defect_rows)
        ),
        "phase_interval": parse_intervals(extract_field(raw, "phase_interval"), 1),
        "initial_qplus": parse_intervals(extract_field(raw, "initial_qplus"), 1),
        "terminal_qplus": parse_intervals(extract_field(raw, "terminal_qplus"), 1),
        "phase_gradient_qplus": phase_gradient,
        "subset_interior": parse_bool(raw, "subset_interior"),
        "preconditioner_point": parse_bool(raw, "preconditioner_point"),
        "contraction": parse_bool(raw, "contraction"),
        "phase_gate": parse_bool(raw, "phase_gate"),
    }
    if parsed["f_center_count"] != 4:
        raise ValueError("F_center is not four-dimensional")
    if parsed["jacobian_count"] != 16:
        raise ValueError("J is not 4 by 4")
    if parsed["preconditioner_count"] != 16:
        raise ValueError("C is not 4 by 4")
    if parsed["defect_count"] != 16:
        raise ValueError("defect is not 4 by 4")
    return parsed


def decimal_box(record: dict[str, Any], key: str) -> tuple[Decimal, Decimal]:
    center = Decimal(str(record["center"][key]))
    radius = Decimal(str(record["root_radii"][key]))
    return center - radius, center + radius


def validate_plan(plan: dict[str, Any]) -> dict[str, bool]:
    slabs = plan["slabs"]
    bridges = plan["bridges"]
    gates = {
        "slab_count_51": len(slabs) == 51 == int(plan["slab_count"]),
        "bridge_count_50": len(bridges) == 50 == int(plan["bridge_count"]),
        "coverage_endpoints": (
            Decimal(str(slabs[0]["epsilon_lower"])) == Decimal("0")
            and Decimal(str(slabs[-1]["epsilon_upper"])) == Decimal("0.101")
        ),
        "strict_positive_primary_radii": all(
            Decimal(str(record["root_radii"][key])) > 0
            for record in slabs
            for key in COORDINATES
        ),
        "period_window": all(
            decimal_box(record, "period")[0] > Decimal("0.66")
            and decimal_box(record, "period")[1] < Decimal("0.67")
            and decimal_box(record, "period")[1] < Decimal("0.68")
            and 2 * decimal_box(record, "period")[0] > Decimal("0.75")
            for record in [*slabs, *bridges]
        ),
    }
    no_gaps = True
    bridge_exact = True
    for index, (left, right) in enumerate(zip(slabs, slabs[1:])):
        left_upper = Decimal(str(left["epsilon_upper"]))
        right_lower = Decimal(str(right["epsilon_lower"]))
        no_gaps = no_gaps and right_lower < left_upper
        bridge = bridges[index]
        bridge_exact = bridge_exact and (
            bridge["bridge_id"] == f"B{index:03d}"
            and bridge["left_slab_id"] == left["slab_id"]
            and bridge["right_slab_id"] == right["slab_id"]
            and Decimal(str(bridge["epsilon_lower"]))
            == max(Decimal(str(left["epsilon_lower"])), right_lower)
            and Decimal(str(bridge["epsilon_upper"]))
            == min(left_upper, Decimal(str(right["epsilon_upper"])))
        )
        for key in COORDINATES:
            lower = min(decimal_box(left, key)[0], decimal_box(right, key)[0])
            upper = max(decimal_box(left, key)[1], decimal_box(right, key)[1])
            bridge_exact = bridge_exact and decimal_box(bridge, key) == (lower, upper)
    gates["positive_adjacent_overlaps"] = no_gaps
    gates["exact_bridge_intersections_and_hulls"] = bridge_exact
    gates["floating_centers_are_only_accelerators"] = all(
        float(record["floating_residual_inf"]) < 1.0e-9 for record in slabs
    )
    with mp.workdps(100):
        a = mp.mpf(51) / 50
        c = 2 * (mp.sqrt(1 + a) - 1)
        lambda_fast = (c * c + 2 + c * mp.sqrt(c * c + 4)) / 2
        anchor = (
            mp.mpf(0),
            mp.sqrt(2) / (2 * mp.pi * mp.sqrt(lambda_fast)),
            mp.mpf(0),
            1 / mp.sqrt(lambda_fast),
        )
        anchor_inside = all(
            mp.mpf(str(decimal_box(slabs[0], key)[0])) < value
            < mp.mpf(str(decimal_box(slabs[0], key)[1]))
            for key, value in zip(COORDINATES, anchor, strict=True)
        )
    gates["analytic_fast_anchor_inside_S000"] = anchor_inside
    return gates


def make_jobs(plan: dict[str, Any]) -> list[Job]:
    jobs = [
        Job(
            str(record["slab_id"]),
            "primary",
            str(record["epsilon_lower"]),
            str(record["epsilon_upper"]),
            {key: str(record["center"][key]) for key in COORDINATES},
            {key: str(record["root_radii"][key]) for key in COORDINATES},
        )
        for record in plan["slabs"]
    ]
    jobs.extend(
        Job(
            str(record["bridge_id"]),
            "bridge",
            str(record["epsilon_lower"]),
            str(record["epsilon_upper"]),
            {key: str(record["center"][key]) for key in COORDINATES},
            {key: str(record["root_radii"][key]) for key in COORDINATES},
        )
        for record in plan["bridges"]
    )
    return jobs


def run_job(binary: Path, output: Path, bits: int, job: Job) -> dict[str, Any]:
    raw_directory = output / "raw" / str(bits) / job.job_type
    raw_directory.mkdir(parents=True, exist_ok=True)
    raw_path = raw_directory / f"{job.job_id}.txt"
    stderr_path = raw_directory / f"{job.job_id}.stderr.txt"
    started = time.monotonic()
    process = subprocess.run(job.arguments(binary, bits), text=True, capture_output=True)
    elapsed = time.monotonic() - started
    raw_path.write_text(process.stdout, encoding="utf-8")
    stderr_path.write_text(process.stderr, encoding="utf-8")
    record: dict[str, Any] = {
        "job_id": job.job_id,
        "job_type": job.job_type,
        "precision_bits": bits,
        "returncode": process.returncode,
        "wall_seconds": elapsed,
        "raw_file": str(raw_path.relative_to(output)),
        "stderr_file": str(stderr_path.relative_to(output)),
        "command_arguments": job.arguments(Path("capd_r401_local_slab_grid_mp"), bits)[1:],
    }
    try:
        record.update(parse_transcript(process.stdout))
    except Exception as error:  # preserve a complete failed attempt
        record["parse_error"] = f"{type(error).__name__}: {error}"
    record["passed"] = (
        process.returncode == 0
        and record.get("status") == "PASS_LOCAL_SLAB"
        and record.get("precision_bits") == bits
        and record.get("subset_interior") is True
        and record.get("preconditioner_point") is True
        and record.get("contraction") is True
        and record.get("phase_gate") is True
        and Decimal(str(record.get("minimum_recomputed_margin", "-1"))) > 0
        and Decimal(str(record.get("maximum_defect_row_sum", "2"))) < 1
        and Decimal(str(record.get("phase_gradient_qplus", ("-1", "-1"))[0])) > 0
    )
    return record


def interval_overlap(
    left: tuple[str, str], right: tuple[str, str]
) -> bool:
    return max(Decimal(left[0]), Decimal(right[0])) <= min(
        Decimal(left[1]), Decimal(right[1])
    )


def cross_precision_gates(records: list[dict[str, Any]]) -> dict[str, bool]:
    keyed = {(int(record["precision_bits"]), str(record["job_id"])): record for record in records}
    ids = sorted({str(record["job_id"]) for record in records})
    root_overlap = True
    image_overlap = True
    for job_id in ids:
        low = keyed[(128, job_id)]
        high = keyed[(256, job_id)]
        if not low.get("passed") or not high.get("passed"):
            root_overlap = False
            image_overlap = False
            continue
        root_overlap = root_overlap and all(
            interval_overlap(left, right)
            for left, right in zip(low["root_box"], high["root_box"], strict=True)
        )
        image_overlap = image_overlap and all(
            interval_overlap(left, right)
            for left, right in zip(
                low["krawczyk_image"], high["krawczyk_image"], strict=True
            )
        )
    return {
        "all_128_256_root_boxes_overlap": root_overlap,
        "all_128_256_krawczyk_images_overlap": image_overlap,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--capd-build",
        type=Path,
        default=Path("/tmp/capd_probe.W9FsjR/build_mp2"),
    )
    parser.add_argument(
        "--capd-source",
        type=Path,
        default=Path("/tmp/capd_probe.W9FsjR"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_l1_branch",
    )
    parser.add_argument("--workers", type=int, default=min(24, os.cpu_count() or 1))
    parser.add_argument(
        "--precisions",
        type=int,
        nargs="+",
        choices=(128, 256),
        default=(128, 256),
        help="production requires both; a subset is permitted only for an external pilot",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite result directory: {output}")
    output.mkdir(parents=True)

    actual_hashes = {str(path): sha256(path) for path in EXPECTED_HASHES}
    hash_gates = {
        str(path): actual_hashes[str(path)] == expected
        for path, expected in EXPECTED_HASHES.items()
    }
    if not all(hash_gates.values()):
        raise RuntimeError(f"frozen input hash mismatch: {hash_gates}")

    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    plan_gates = validate_plan(plan)
    if not all(plan_gates.values()):
        raise RuntimeError(f"plan validation failed: {plan_gates}")
    jobs = make_jobs(plan)

    capd_config = args.capd_build.resolve() / "bin/capd-config"
    if not capd_config.is_file():
        raise FileNotFoundError(f"CAPD config not found: {capd_config}")
    capd_commit = command_output(
        ["git", "-C", str(args.capd_source.resolve()), "rev-parse", "HEAD"]
    )
    if capd_commit != EXPECTED_CAPD_COMMIT:
        raise RuntimeError(f"unexpected CAPD commit: {capd_commit}")
    flags = shlex.split(command_output([str(capd_config), "--cflags", "--libs"]))
    required_flags = {"-D__HAVE_MPFR__", "-lmpfr", "-lgmp", "-frounding-math"}
    if not required_flags.issubset(flags):
        raise RuntimeError(f"missing CAPD flags: {required_flags - set(flags)}")

    binary = output / "capd_r401_local_slab_grid_mp"
    compile_command = ["g++", "-O2", str(SOURCE), *flags, "-o", str(binary)]
    compilation = subprocess.run(compile_command, text=True, capture_output=True)
    (output / "compile_stdout.txt").write_text(compilation.stdout, encoding="utf-8")
    (output / "compile_stderr.txt").write_text(compilation.stderr, encoding="utf-8")
    if compilation.returncode != 0:
        raise RuntimeError("CAPD producer compilation failed")

    requested_precisions = tuple(dict.fromkeys(args.precisions))
    all_records: list[dict[str, Any]] = []
    started = time.monotonic()
    for bits in requested_precisions:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [executor.submit(run_job, binary, output, bits, job) for job in jobs]
            for future in as_completed(futures):
                all_records.append(future.result())
    elapsed = time.monotonic() - started
    all_records.sort(key=lambda record: (int(record["precision_bits"]), str(record["job_id"])))

    precision_gates = {
        str(bits): (
            sum(record["precision_bits"] == bits for record in all_records) == 101
            and all(
                bool(record["passed"])
                for record in all_records
                if record["precision_bits"] == bits
            )
        )
        for bits in requested_precisions
    }
    production_precision_set = set(requested_precisions) == {128, 256}
    cross_gates = (
        cross_precision_gates(all_records)
        if production_precision_set and all(precision_gates.values())
        else {
            "all_128_256_root_boxes_overlap": False,
            "all_128_256_krawczyk_images_overlap": False,
        }
    )
    overall = (
        production_precision_set
        and all(precision_gates.values())
        and all(cross_gates.values())
    )

    environment = {
        "python": sys.version,
        "platform": platform.platform(),
        "compiler": command_output(["g++", "--version"]).splitlines()[0],
        "capd_commit": capd_commit,
        "capd_config_flags": flags,
        "mpfr": command_output(["pkg-config", "--modversion", "mpfr"]),
        "gmp": command_output(["pkg-config", "--modversion", "gmp"]),
        "workers": args.workers,
        "wall_seconds": elapsed,
    }
    summary = {
        "protocol_id": "R401-VAL-L1",
        "milestone_status": "PASS_CONTIGUOUS_LOCAL_BRANCH" if overall else "FAIL",
        "final_status": None,
        "claim_boundary": (
            "one primitive full-return branch, unique only inside the frozen local "
            "primary boxes and bridge hulls, for every epsilon in [0,0.101]; no "
            "root-complement, global phase-space cover, delta_tr, Hilbert-Polya, or RH claim"
        ),
        "job_count_per_precision": len(jobs),
        "primary_job_count": sum(job.job_type == "primary" for job in jobs),
        "bridge_job_count": sum(job.job_type == "bridge" for job in jobs),
        "requested_precisions": list(requested_precisions),
        "precision_gates": precision_gates,
        "cross_precision_gates": cross_gates,
        "plan_gates": plan_gates,
        "hash_gates": hash_gates,
        "records": all_records,
        "environment": environment,
    }
    summary_path = output / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    passing_records = [record for record in all_records if record.get("passed")]
    if passing_records:
        minimum_margin = min(
            Decimal(str(record["minimum_recomputed_margin"])) for record in passing_records
        )
        maximum_contraction = max(
            Decimal(str(record["maximum_defect_row_sum"])) for record in passing_records
        )
        minimum_phase_slope = min(
            Decimal(str(record["phase_gradient_qplus"][0])) for record in passing_records
        )
    else:
        minimum_margin = Decimal("NaN")
        maximum_contraction = Decimal("NaN")
        minimum_phase_slope = Decimal("NaN")
    report = f"""# R401-VAL-L1 contiguous local branch

Milestone status: **{summary['milestone_status']}**.

The run evaluated 51 primary parameter slabs and 50 bridge hulls at both
128-bit and 256-bit MPFR precision.  The union of the primary slabs is
`epsilon in [0,0.101]`; the bridge certificates identify all adjacent local
solutions as one branch.

- smallest strict Krawczyk interior margin: `{minimum_margin}`;
- largest certified infinity-norm contraction bound: `{maximum_contraction}`;
- smallest certified `dK/dQ_plus` lower bound on the phase interval:
  `{minimum_phase_slope}`;
- total validated jobs: `{sum(bool(record.get('passed')) for record in all_records)}`
  of `{len(all_records)}`;
- wall time with `{args.workers}` workers: `{elapsed:.3f}` seconds.

The phase gate and exact energy conservation recover the omitted `Q_plus`
return equation, and the existing short-period exclusion makes the certified
returns primitive.  The result proves uniqueness only inside the frozen
local boxes.  It does not exclude other roots, close the global covers,
promote `delta_tr`, or imply any Hilbert--Polya/RH statement.
"""
    report_path = output / "R401_VAL_L1_REPORT.md"
    report_path.write_text(report, encoding="utf-8")

    hash_targets = [
        SOURCE,
        PLAN,
        PROTOCOL,
        V2_FREEZE,
        RADIAL_PROOF,
        WARPED_PROOF,
        DEPENDENCY,
        RUNNER,
        summary_path,
        report_path,
        output / "compile_stdout.txt",
        output / "compile_stderr.txt",
        binary,
    ]
    hash_targets.extend(sorted((output / "raw").rglob("*.txt")))
    manifest = {
        "protocol_id": "R401-VAL-L1",
        "milestone_status": summary["milestone_status"],
        "final_status": None,
        "capd_commit": capd_commit,
        "files": {
            str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path): sha256(path)
            for path in hash_targets
        },
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": summary["milestone_status"],
                "output": str(output),
                "wall_seconds": elapsed,
                "passed_jobs": sum(bool(record.get("passed")) for record in all_records),
                "total_jobs": len(all_records),
            },
            indent=2,
        )
    )
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
