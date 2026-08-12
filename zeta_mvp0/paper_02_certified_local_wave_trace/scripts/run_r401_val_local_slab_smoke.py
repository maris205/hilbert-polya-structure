#!/usr/bin/env python3
"""Build and run the R401-VAL-V2 CAPD endpoint-slab smoke."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import shlex
import subprocess
import sys
import time
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_local_slab_mp.cpp"
BASE_PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md"
AMENDMENT = ROOT / "research/route_a_wave_trace/R401_VAL_PROTOCOL_AMENDMENT_V2.md"
RADIAL_PROOF = ROOT / "research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md"
WARPED_PROOF = ROOT / "research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md"
FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_PROTOCOL_V2_FREEZE.md"
EXPECTED_COMPONENT_HASHES = {
    BASE_PROTOCOL: "d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82",
    AMENDMENT: "a163be8800ecc1677ccaf2f6342becfe834d55d80ad59dcc24180e3f0f5e62aa",
    RADIAL_PROOF: "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    WARPED_PROOF: "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8",
}
EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command_output(command: list[str]) -> str:
    return subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


def parse_intervals(text: str) -> list[tuple[str, str]]:
    return [(match.group(1), match.group(2)) for match in INTERVAL_PATTERN.finditer(text)]


def parse_raw(raw: str) -> dict[str, object]:
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if "=" in line and not line.startswith("{"):
            key, value = line.split("=", 1)
            values[key] = value
    required = {
        "status",
        "precision_bits",
        "epsilon",
        "X",
        "K",
        "left_margin",
        "right_margin",
        "subset_interior",
    }
    missing = sorted(required - values.keys())
    if missing:
        raise ValueError(f"missing CAPD output fields: {missing}")
    x_box = parse_intervals(values["X"])
    k_box = parse_intervals(values["K"])
    left = parse_intervals(values["left_margin"])
    right = parse_intervals(values["right_margin"])
    if not all(len(items) == 4 for items in (x_box, k_box, left, right)):
        raise ValueError("failed to parse four-dimensional Krawczyk data")
    recomputed: list[tuple[str, str]] = []
    for x_interval, k_interval in zip(x_box, k_box, strict=True):
        left_value = Decimal(k_interval[0]) - Decimal(x_interval[0])
        right_value = Decimal(x_interval[1]) - Decimal(k_interval[1])
        recomputed.append((str(left_value), str(right_value)))
    minimum = min(
        Decimal(value)
        for pair in recomputed
        for value in pair
    )
    return {
        "status": values["status"],
        "precision_bits": int(values["precision_bits"]),
        "epsilon": parse_intervals(values["epsilon"]),
        "root_box": x_box,
        "krawczyk_image": k_box,
        "reported_left_margin": left,
        "reported_right_margin": right,
        "recomputed_component_margins": recomputed,
        "minimum_recomputed_margin": str(minimum),
        "subset_interior": values["subset_interior"] == "1",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--capd-build",
        type=Path,
        default=Path("/tmp/capd_probe.W9FsjR/build_mp2"),
        help="multiprecision CAPD build directory",
    )
    parser.add_argument(
        "--capd-source",
        type=Path,
        default=Path("/tmp/capd_probe.W9FsjR"),
        help="pinned CAPD source checkout",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_local_slab_smoke",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing result: {output}")
    output.mkdir(parents=True)

    actual_component_hashes = {str(path): sha256(path) for path in EXPECTED_COMPONENT_HASHES}
    component_hash_gates = {
        str(path): actual_component_hashes[str(path)] == expected
        for path, expected in EXPECTED_COMPONENT_HASHES.items()
    }
    if not all(component_hash_gates.values()):
        raise RuntimeError("R401-VAL-V2 protocol component hash mismatch")

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
        raise RuntimeError(f"CAPD multiprecision flags missing: {required_flags - set(flags)}")

    binary = output / "capd_r401_local_slab_mp"
    compile_command = ["g++", str(SOURCE), *flags, "-o", str(binary)]
    compilation = subprocess.run(
        compile_command,
        check=True,
        text=True,
        capture_output=True,
    )
    (output / "compile_stdout.txt").write_text(compilation.stdout, encoding="utf-8")
    (output / "compile_stderr.txt").write_text(compilation.stderr, encoding="utf-8")

    runs: list[dict[str, object]] = []
    for bits in (128, 256):
        started = time.monotonic()
        process = subprocess.run(
            [str(binary), str(bits)],
            text=True,
            capture_output=True,
        )
        elapsed = time.monotonic() - started
        raw_path = output / f"capd_{bits}.txt"
        raw_path.write_text(process.stdout, encoding="utf-8")
        (output / f"capd_{bits}.stderr.txt").write_text(
            process.stderr,
            encoding="utf-8",
        )
        parsed = parse_raw(process.stdout)
        parsed["returncode"] = process.returncode
        parsed["wall_seconds"] = elapsed
        parsed["raw_file"] = raw_path.name
        runs.append(parsed)

    run_gates = {
        str(run["precision_bits"]): (
            run["returncode"] == 0
            and run["status"] == "PASS_LOCAL_SLAB_SMOKE"
            and run["subset_interior"] is True
            and Decimal(str(run["minimum_recomputed_margin"])) > 0
        )
        for run in runs
    }
    overall = all(run_gates.values())
    environment = {
        "python": sys.version,
        "platform": platform.platform(),
        "compiler": command_output(["g++", "--version"]).splitlines()[0],
        "capd_commit": capd_commit,
        "capd_config_flags": flags,
        "mpfr": command_output(["pkg-config", "--modversion", "mpfr"]),
        "gmp": command_output(["pkg-config", "--modversion", "gmp"]),
    }
    summary = {
        "protocol_id": "R401-VAL-V2",
        "milestone_status": "PASS_LOCAL_SLAB_SMOKE" if overall else "FAIL",
        "final_status": None,
        "claim_boundary": (
            "strict local branch existence/uniqueness on epsilon in [0.099,0.101] only; "
            "no root-complement, phase-cover, global-cover, or delta_tr claim"
        ),
        "precision_runs": runs,
        "run_gates": run_gates,
        "component_hash_gates": component_hash_gates,
        "component_hashes": actual_component_hashes,
        "environment": environment,
    }
    summary_path = output / "summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    margins = {
        int(run["precision_bits"]): run["minimum_recomputed_margin"] for run in runs
    }
    report = fr"""# R401-VAL-V2 Local Endpoint-Slab Smoke

Milestone status: **{summary['milestone_status']}**.

CAPD's validated C1 Taylor/Lohner flow and a parameterized Krawczyk operator
certify a unique zero of the frozen four-equation local return system for

\[
 0.099\le\epsilon\le0.101.
\]

The strict inclusion was independently replicated at 128-bit and 256-bit
MPFR precision.  The smallest componentwise Krawczyk interior margins are
`{margins[128]}` and `{margins[256]}`, respectively.

This is a local branch milestone.  It does not exclude other roots outside
the displayed root box, does not close the phase/global covers, and does not
certify `delta_tr` or any Hilbert--Polya/RH statement.
"""
    report_path = output / "R401_VAL_LOCAL_SLAB_REPORT.md"
    report_path.write_text(report, encoding="utf-8")

    hash_targets = [
        SOURCE,
        BASE_PROTOCOL,
        AMENDMENT,
        RADIAL_PROOF,
        WARPED_PROOF,
        FREEZE,
        summary_path,
        report_path,
        output / "capd_128.txt",
        output / "capd_256.txt",
        binary,
    ]
    manifest = {
        "protocol_id": "R401-VAL-V2",
        "milestone_status": summary["milestone_status"],
        "final_status": None,
        "capd_commit": capd_commit,
        "files": {str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path): sha256(path) for path in hash_targets},
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": summary["milestone_status"], "output": str(output)}, indent=2))
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
