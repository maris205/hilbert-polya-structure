#!/usr/bin/env python3
"""Independently replay the NON_LICENSING branch-tube smoke archive.

This checker intentionally does not import the producer.  It re-parses every
CAPD interval transcript with exact rational arithmetic, binds the six jobs to
the accepted A4.12 primary records, and verifies the manifest byte hashes.  It
can assign only a checker status; all scientific authority fields remain null.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_phase_branch_tube_mp.cpp"
RUNNER = ROOT / "scripts/run_r401_val_l3_branch_tube_smoke.py"
CHECKER = Path(__file__).resolve()
DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
UPSTREAM_FILES = (
    L1_RESULT / "summary.json",
    L1_RESULT / "manifest.json",
    L1_RESULT / "independent_checker.json",
    L1_RESULT / "POSTCHECK_STATUS.json",
    L1_RESULT / "RELEASE_PROVENANCE.json",
)
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
PRECISIONS = (128, 256)
PHASE_GRID = 64
TUBE_RADIUS_SQ = Fraction(1, 625)
PASS_STATUS = "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
SCALAR_PATTERN = re.compile(rf"\s*({NUMBER})\s*")
Interval = tuple[Fraction, Fraction]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_keys(payload: dict[str, Any], expected: set[str], context: str) -> None:
    actual = set(payload)
    if actual != expected:
        raise ValueError(
            f"{context} key mismatch: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def require_string(value: Any, context: str) -> str:
    if type(value) is not str:
        raise TypeError(f"{context} must be a string")
    return value


def reject_symlink(path: Path, context: str) -> None:
    if path.is_symlink():
        raise ValueError(f"{context} must not be a symlink: {path}")


def reject_result_symlink_chain(path: Path, output: Path, context: str) -> None:
    candidate = path
    while True:
        reject_symlink(candidate, context)
        if candidate == output:
            return
        if output not in candidate.parents:
            raise ValueError(f"{context} escapes result directory: {path}")
        candidate = candidate.parent


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_object,
        parse_constant=reject_constant,
    )
    if type(value) is not dict:
        raise TypeError(f"top-level JSON object required: {path}")
    return value


def exact_field(raw: str, key: str) -> str:
    prefix = f"{key}="
    values = [line[len(prefix) :] for line in raw.splitlines() if line.startswith(prefix)]
    if len(values) != 1:
        raise ValueError(f"expected exactly one {key}, found {len(values)}")
    return values[0]


def interval(value: str) -> tuple[Fraction, Fraction]:
    matches = INTERVAL_PATTERN.findall(value)
    if len(matches) != 1:
        raise ValueError(f"expected one interval, found {len(matches)}")
    lower, upper = (Fraction(token) for token in matches[0])
    if lower > upper:
        raise ValueError("reversed interval")
    return lower, upper


def intervals(value: str, count: int) -> list[tuple[Fraction, Fraction]]:
    matches = INTERVAL_PATTERN.findall(value)
    if len(matches) != count:
        raise ValueError(f"expected {count} intervals, found {len(matches)}")
    result = [(Fraction(lower), Fraction(upper)) for lower, upper in matches]
    if any(lower > upper for lower, upper in result):
        raise ValueError("reversed vector interval")
    return result


def scalar(value: str) -> Fraction:
    match = SCALAR_PATTERN.fullmatch(value)
    if match is None:
        raise ValueError("expected one CAPD scalar")
    return Fraction(match.group(1))


def add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def sub(left: Interval, right: Interval) -> Interval:
    return left[0] - right[1], left[1] - right[0]


def mul(left: Interval, right: Interval) -> Interval:
    products = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(products), max(products)


def square(value: Interval) -> Interval:
    lower, upper = value
    if lower >= 0:
        return lower * lower, upper * upper
    if upper <= 0:
        return upper * upper, lower * lower
    return Fraction(0), max(lower * lower, upper * upper)


def overlap(left: Interval, right: Interval) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def arb_endpoint_fraction(value: arb, *, lower: bool) -> Fraction:
    endpoint = value.lower() if lower else value.upper()
    rational = endpoint.fmpq()
    return Fraction(int(rational.p), int(rational.q))


def independent_omega_slow(bits: int) -> Interval:
    previous_precision = ctx.prec
    try:
        ctx.prec = bits
        a = arb(51) / 50
        c = 2 * ((1 + a).sqrt() - 1)
        discriminant = c * (c * c + 4).sqrt()
        lambda_slow = (c * c + 2 - discriminant) / 2
        omega_slow = 2 * arb.pi() * lambda_slow.sqrt()
        return (
            arb_endpoint_fraction(omega_slow, lower=True),
            arb_endpoint_fraction(omega_slow, lower=False),
        )
    finally:
        ctx.prec = previous_precision


def parse_int_field(raw: str, key: str) -> int:
    value = exact_field(raw, key)
    if not re.fullmatch(r"0|[1-9]\d*", value):
        raise ValueError(f"non-canonical nonnegative integer in {key}")
    return int(value)


def replay_transcript(raw: str) -> dict[str, Any]:
    if exact_field(raw, "protocol_id") != "R401-VAL-L3-BT-S0":
        raise ValueError("wrong protocol")
    if exact_field(raw, "licensing") != "NON_LICENSING":
        raise ValueError("licensing promotion")
    for key in ("milestone_status", "theorem_status", "final_status"):
        if exact_field(raw, key) != "null":
            raise ValueError(f"producer assigned {key}")
    bits = parse_int_field(raw, "precision_bits")
    if bits not in PRECISIONS:
        raise ValueError("wrong precision")
    if parse_int_field(raw, "phase_grid") != PHASE_GRID:
        raise ValueError("wrong phase grid")
    if parse_int_field(raw, "taylor_order") != 24:
        raise ValueError("wrong Taylor order")
    expected_tolerance = "1e-30" if bits == 128 else "1e-60"
    if exact_field(raw, "tolerance") != expected_tolerance:
        raise ValueError("wrong solver tolerance")
    radius = interval(exact_field(raw, "tube_radius_sq"))
    if not radius[0] <= TUBE_RADIUS_SQ <= radius[1]:
        raise ValueError("tube radius does not enclose 1/625")
    epsilon = interval(exact_field(raw, "epsilon"))
    root_box = intervals(exact_field(raw, "root_box"), 4)
    printed_omega = interval(exact_field(raw, "omega_slow"))
    omega = independent_omega_slow(bits)
    if not (printed_omega[0] <= omega[0] and omega[1] <= printed_omega[1]):
        raise ValueError("CAPD omega_slow does not contain independent Arb enclosure")

    maximum = Fraction(0)
    minimum_margin: Fraction | None = None
    printed_maximum = Fraction(0)
    printed_minimum_margin: Fraction | None = None
    for index in range(PHASE_GRID):
        stem = f"segment_{index:03d}"
        phase = interval(exact_field(raw, f"{stem}_phase"))
        expected_phase = (Fraction(index, PHASE_GRID), Fraction(index + 1, PHASE_GRID))
        if phase != expected_phase:
            raise ValueError(f"segment {index} is not its frozen dyadic cell")
        state = intervals(exact_field(raw, f"{stem}_state"), 6)
        rslow_sq = interval(exact_field(raw, f"{stem}_rslow_sq"))
        margin_sq = interval(exact_field(raw, f"{stem}_margin_sq"))
        if exact_field(raw, f"{stem}_inside") != "1":
            raise ValueError(f"segment {index} inside flag is false")
        recomputed = add(square(mul(omega, state[0])), square(state[2]))
        recomputed_margin = sub((TUBE_RADIUS_SQ, TUBE_RADIUS_SQ), recomputed)
        if recomputed[1] >= TUBE_RADIUS_SQ or recomputed_margin[0] <= 0:
            raise ValueError(f"segment {index} fails independent rational tube gate")
        # Decimal printing expands the state and frequency endpoints.  The
        # pre-print CAPD radius can therefore be microscopically narrower;
        # overlap is consistency telemetry, while the recomputed gate above
        # is the checker authority and uses no tolerance.
        if not overlap(rslow_sq, recomputed):
            raise ValueError(f"segment {index} printed radius is inconsistent")
        if not overlap(margin_sq, recomputed_margin):
            raise ValueError(f"segment {index} printed margin is inconsistent")
        maximum = max(maximum, recomputed[1])
        minimum_margin = (
            recomputed_margin[0]
            if minimum_margin is None
            else min(minimum_margin, recomputed_margin[0])
        )
        printed_maximum = max(printed_maximum, rslow_sq[1])
        printed_minimum_margin = (
            margin_sq[0]
            if printed_minimum_margin is None
            else min(printed_minimum_margin, margin_sq[0])
        )

    left_domain = scalar(exact_field(raw, "solution_left_domain"))
    right_domain = scalar(exact_field(raw, "solution_right_domain"))
    if left_domain != 0:
        raise ValueError("SolutionCurve left endpoint is not zero")
    if right_domain != 1:
        raise ValueError("SolutionCurve right endpoint is not one")
    piece_count = parse_int_field(raw, "solution_piece_count")
    if piece_count <= 0:
        raise ValueError("SolutionCurve has no pieces")
    terminal_state_box = intervals(exact_field(raw, "terminal_state_box"), 6)
    reported_maximum = interval(exact_field(raw, "maximum_rslow_sq_upper"))
    if not reported_maximum[0] <= printed_maximum <= reported_maximum[1]:
        raise ValueError("aggregate maximum does not contain printed-segment maximum")
    if exact_field(raw, "all_segments_inside") != "1":
        raise ValueError("aggregate inside gate is false")
    if exact_field(raw, "status") != PASS_STATUS:
        raise ValueError("producer status is not the non-licensing pass token")
    return {
        "precision_bits": bits,
        "epsilon": epsilon,
        "root_box": root_box,
        "omega_slow": printed_omega,
        "terminal_state_box": terminal_state_box,
        "reported_maximum_rslow_sq_upper": reported_maximum[1],
        "maximum_printed_segment_upper": printed_maximum,
        "maximum_rslow_sq_upper": maximum,
        "minimum_margin_sq_lower": minimum_margin,
        "minimum_printed_margin_sq_lower": printed_minimum_margin,
        "solution_piece_count": piece_count,
    }


def contains_interval(
    printed: tuple[Fraction, Fraction], expected: tuple[Fraction, Fraction]
) -> bool:
    return printed[0] <= expected[0] <= printed[1] and printed[0] <= expected[1] <= printed[1]


def upstream_primary_records() -> dict[tuple[int, str], dict[str, Any]]:
    summary = strict_json(UPSTREAM_FILES[0])
    if (
        summary.get("protocol_id") != "R401-VAL-L1-V2"
        or summary.get("milestone_status") != "PASS_CONTIGUOUS_LOCAL_BRANCH"
        or summary.get("final_status") is not None
    ):
        raise ValueError("A4.12 upstream summary is not accepted")
    records = summary.get("records")
    if type(records) is not list:
        raise TypeError("A4.12 records must be a list")
    selected: dict[tuple[int, str], dict[str, Any]] = {}
    for record in records:
        if type(record) is not dict:
            raise TypeError("A4.12 record must be an object")
        pair = (record.get("precision_bits"), record.get("job_id"))
        if (
            record.get("job_type") == "primary"
            and pair[0] in PRECISIONS
            and pair[1] in REPRESENTATIVE_SLABS
        ):
            if pair in selected:
                raise ValueError(f"duplicate A4.12 pair: {pair}")
            if record.get("passed") is not True or record.get("status") != "PASS_LOCAL_SLAB":
                raise ValueError(f"unaccepted A4.12 pair: {pair}")
            selected[pair] = record
    expected = {(bits, slab) for bits in PRECISIONS for slab in REPRESENTATIVE_SLABS}
    if set(selected) != expected:
        raise ValueError("A4.12 representative matrix is incomplete")
    return selected


def verify_authority(record: dict[str, Any]) -> None:
    if record.get("protocol_id") != "R401-VAL-L3-BT-S0":
        raise ValueError("wrong archive protocol")
    if record.get("licensing") != "NON_LICENSING":
        raise ValueError("archive licensing is not NON_LICENSING")
    if record.get("prototype_status") != PASS_STATUS:
        raise ValueError("archive prototype status is not the frozen token")
    for key in ("milestone_status", "theorem_status", "final_status"):
        if key not in record or record[key] is not None:
            raise ValueError(f"archive assigned {key}")


def expected_manifest_paths(output: Path) -> set[Path]:
    paths = {
        SOURCE.resolve(),
        RUNNER.resolve(),
        CHECKER.resolve(),
        DEPENDENCY.resolve(),
        (output / "summary.json").resolve(),
        (output / "compile_stdout.txt").resolve(),
        (output / "compile_stderr.txt").resolve(),
        (output / "R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md").resolve(),
        (output / "capd_r401_phase_branch_tube_mp").resolve(),
        *(path.resolve() for path in UPSTREAM_FILES),
    }
    for bits in PRECISIONS:
        for slab in REPRESENTATIVE_SLABS:
            paths.add((output / f"raw/{bits}/{slab}.txt").resolve())
            paths.add((output / f"raw/{bits}/{slab}.stderr.txt").resolve())
    return paths


def verify_manifest(output: Path, manifest: dict[str, Any]) -> int:
    exact_keys(
        manifest,
        {
            "protocol_id",
            "licensing",
            "prototype_status",
            "milestone_status",
            "theorem_status",
            "final_status",
            "files",
        },
        "manifest",
    )
    verify_authority(manifest)
    files = manifest.get("files")
    if type(files) is not dict or not files:
        raise TypeError("manifest files must be a nonempty object")
    actual_paths = {Path(name).resolve() for name in files}
    expected_paths = expected_manifest_paths(output)
    if actual_paths != expected_paths or len(files) != len(actual_paths):
        raise ValueError("manifest file set is not exact")
    for name, expected_hash in files.items():
        if type(name) is not str or type(expected_hash) is not str or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            raise TypeError("malformed manifest entry")
        path = Path(name)
        reject_symlink(path, "manifest payload")
        if not path.is_file() or sha256(path) != expected_hash:
            raise ValueError(f"manifest hash mismatch: {path}")
    return len(files)


def verify_summary(output: Path, summary: dict[str, Any]) -> tuple[int, Fraction, Fraction]:
    exact_keys(
        summary,
        {
            "protocol_id",
            "licensing",
            "prototype_status",
            "milestone_status",
            "theorem_status",
            "final_status",
            "claim_boundary",
            "representative_slabs",
            "precisions",
            "phase_grid",
            "tube_radius",
            "tube_radius_sq",
            "pair_gate",
            "records",
            "elapsed_seconds",
            "environment",
            "input_hashes",
        },
        "summary",
    )
    verify_authority(summary)
    require_string(summary["claim_boundary"], "summary.claim_boundary")
    if "not phase completeness" not in summary["claim_boundary"]:
        raise ValueError("summary claim boundary is too broad")
    if summary.get("representative_slabs") != list(REPRESENTATIVE_SLABS):
        raise ValueError("wrong representative slabs")
    if summary.get("precisions") != list(PRECISIONS):
        raise ValueError("wrong precision matrix")
    if type(summary.get("phase_grid")) is not int or summary["phase_grid"] != PHASE_GRID:
        raise TypeError("wrong phase-grid type or value")
    if summary.get("tube_radius") != "0.04" or summary.get("tube_radius_sq") != "0.0016":
        raise ValueError("wrong tube radius")
    if summary.get("pair_gate") is not True:
        raise ValueError("pair gate is not true")
    if type(summary.get("elapsed_seconds")) not in (int, float) or not math.isfinite(summary["elapsed_seconds"]) or summary["elapsed_seconds"] < 0:
        raise TypeError("elapsed_seconds must be a finite nonnegative JSON number")
    environment = summary.get("environment")
    if type(environment) is not dict:
        raise TypeError("environment must be an object")
    exact_keys(
        environment,
        {"platform", "python", "capd_commit", "capd_config_flags", "compile_command"},
        "summary.environment",
    )
    require_string(environment["platform"], "summary.environment.platform")
    require_string(environment["python"], "summary.environment.python")
    if environment["capd_commit"] != EXPECTED_CAPD_COMMIT:
        raise ValueError("wrong CAPD commit")
    flags = environment["capd_config_flags"]
    command = environment["compile_command"]
    if type(flags) is not list or not flags or any(type(flag) is not str for flag in flags):
        raise TypeError("CAPD flags must be a nonempty string list")
    for required in ("-D__HAVE_MPFR__", "-lmpfr", "-lgmp", "-frounding-math"):
        if required not in flags:
            raise ValueError(f"missing CAPD compile flag: {required}")
    binary = (output / "capd_r401_phase_branch_tube_mp").resolve()
    expected_command = ["g++", "-O2", str(SOURCE), *flags, "-o", str(binary)]
    if command != expected_command:
        raise ValueError("compile command is not exactly bound to source, CAPD flags, and binary")
    records = summary.get("records")
    if type(records) is not list or len(records) != 6:
        raise TypeError("summary must contain exactly six records")
    upstream = upstream_primary_records()
    expected_pairs = {(bits, slab) for bits in PRECISIONS for slab in REPRESENTATIVE_SLABS}
    seen: set[tuple[int, str]] = set()
    global_maximum = Fraction(0)
    global_minimum_margin: Fraction | None = None
    for record in records:
        if type(record) is not dict:
            raise TypeError("summary job record must be an object")
        bits = record.get("precision_bits")
        slab = record.get("slab_id")
        exact_keys(
            record,
            {
                "precision_bits",
                "slab_id",
                "returncode",
                "wall_seconds",
                "raw_file",
                "stderr_file",
                "argv",
                "status",
                "taylor_order",
                "tolerance",
                "omega_slow",
                "epsilon",
                "root_box",
                "terminal_state_box",
                "solution_piece_count",
                "maximum_rslow_sq_upper",
                "maximum_segment_rslow_sq_upper",
                "minimum_margin_sq_lower",
                "all_segments_inside",
                "phase_cover_complete",
                "input_echo_gate",
                "passed",
            },
            f"summary record {bits}/{slab}",
        )
        if type(bits) is not int or type(slab) is not str:
            raise TypeError("noncanonical pair types")
        pair = (bits, slab)
        if pair not in expected_pairs or pair in seen:
            raise ValueError(f"unexpected or duplicate pair: {pair}")
        seen.add(pair)
        if (
            type(record.get("returncode")) is not int
            or record["returncode"] != 0
            or record.get("passed") is not True
            or record.get("input_echo_gate") is not True
            or record.get("status") != PASS_STATUS
            or record.get("all_segments_inside") is not True
            or record.get("phase_cover_complete") is not True
            or "parse_error" in record
        ):
            raise ValueError(f"failed producer gate: {pair}")
        if type(record.get("wall_seconds")) not in (int, float) or record["wall_seconds"] < 0:
            raise TypeError("wall time must be a nonnegative JSON number")
        if not math.isfinite(record["wall_seconds"]):
            raise TypeError("wall time must be finite")
        if record.get("taylor_order") != 24:
            raise ValueError(f"wrong recorded Taylor order: {pair}")
        if record.get("tolerance") != ("1e-30" if bits == 128 else "1e-60"):
            raise ValueError(f"wrong recorded tolerance: {pair}")
        for field, count in (("omega_slow", 2), ("epsilon", 2)):
            value = record.get(field)
            if type(value) is not list or len(value) != count or any(type(token) is not str for token in value):
                raise TypeError(f"malformed {field}: {pair}")
        for field, count in (("root_box", 4), ("terminal_state_box", 6)):
            value = record.get(field)
            if type(value) is not list or len(value) != count or any(
                type(item) is not list or len(item) != 2 or any(type(token) is not str for token in item)
                for item in value
            ):
                raise TypeError(f"malformed {field}: {pair}")
        raw_relative = f"raw/{bits}/{slab}.txt"
        stderr_relative = f"raw/{bits}/{slab}.stderr.txt"
        if record.get("raw_file") != raw_relative or record.get("stderr_file") != stderr_relative:
            raise ValueError(f"wrong transcript paths: {pair}")
        raw_path = output / raw_relative
        stderr_path = output / stderr_relative
        reject_result_symlink_chain(raw_path, output, "raw transcript")
        reject_result_symlink_chain(stderr_path, output, "stderr transcript")
        if stderr_path.read_bytes() != b"":
            raise ValueError(f"nonempty stderr: {pair}")
        replay = replay_transcript(raw_path.read_text(encoding="utf-8"))
        if replay["precision_bits"] != bits:
            raise ValueError(f"transcript precision mismatch: {pair}")
        if tuple(Fraction(token) for token in record["omega_slow"]) != replay["omega_slow"]:
            raise ValueError(f"summary omega mismatch: {pair}")
        if tuple(Fraction(token) for token in record["epsilon"]) != replay["epsilon"]:
            raise ValueError(f"summary epsilon mismatch: {pair}")
        if [tuple(Fraction(token) for token in item) for item in record["root_box"]] != replay["root_box"]:
            raise ValueError(f"summary root-box mismatch: {pair}")
        if [
            tuple(Fraction(token) for token in item)
            for item in record["terminal_state_box"]
        ] != replay["terminal_state_box"]:
            raise ValueError(f"summary terminal-box mismatch: {pair}")

        accepted = upstream[pair]
        expected_epsilon = tuple(Fraction(value) for value in accepted["epsilon"][0])
        expected_root = [
            tuple(Fraction(value) for value in item) for item in accepted["root_box"]
        ]
        if not contains_interval(replay["epsilon"], expected_epsilon):
            raise ValueError(f"epsilon echo does not contain accepted input: {pair}")
        if not all(
            contains_interval(printed, expected)
            for printed, expected in zip(replay["root_box"], expected_root, strict=True)
        ):
            raise ValueError(f"root-box echo does not contain accepted input: {pair}")
        binary = (output / "capd_r401_phase_branch_tube_mp").resolve()
        expected_argv = [
            str(binary),
            str(bits),
            *accepted["epsilon"][0],
            *(token for item in accepted["root_box"] for token in item),
        ]
        if record.get("argv") != expected_argv:
            raise ValueError(f"argv is not bound to accepted A4.12 input: {pair}")
        if Fraction(record["maximum_rslow_sq_upper"]) != replay["reported_maximum_rslow_sq_upper"]:
            raise ValueError(f"summary maximum mismatch: {pair}")
        if Fraction(record["maximum_segment_rslow_sq_upper"]) != replay["maximum_printed_segment_upper"]:
            raise ValueError(f"summary replay maximum mismatch: {pair}")
        if Fraction(record["minimum_margin_sq_lower"]) != replay["minimum_printed_margin_sq_lower"]:
            raise ValueError(f"summary margin mismatch: {pair}")
        if record.get("solution_piece_count") != replay["solution_piece_count"]:
            raise ValueError(f"SolutionCurve piece-count mismatch: {pair}")
        global_maximum = max(global_maximum, replay["maximum_rslow_sq_upper"])
        global_minimum_margin = (
            replay["minimum_margin_sq_lower"]
            if global_minimum_margin is None
            else min(global_minimum_margin, replay["minimum_margin_sq_lower"])
        )
    if seen != expected_pairs or global_minimum_margin is None:
        raise ValueError("six-pair replay is incomplete")

    required_hash_inputs = {SOURCE, RUNNER, CHECKER, DEPENDENCY, *UPSTREAM_FILES}
    input_hashes = summary.get("input_hashes")
    if type(input_hashes) is not dict:
        raise TypeError("input_hashes must be an object")
    expected_names = {str(path.relative_to(ROOT)) for path in required_hash_inputs}
    if set(input_hashes) != expected_names:
        raise ValueError("summary input-hash set is not exact")
    for path in required_hash_inputs:
        relative = str(path.relative_to(ROOT))
        if input_hashes[relative] != sha256(path):
            raise ValueError(f"summary input hash mismatch: {relative}")
    return len(records), global_maximum, global_minimum_margin


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_l3_branch_tube_smoke",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    requested_output = args.output.absolute()
    reject_symlink(requested_output, "result directory")
    output = requested_output.resolve()
    checker_path = output / "independent_checker.json"
    if checker_path.exists():
        raise FileExistsError(f"refusing to overwrite checker: {checker_path}")
    failures: list[str] = []
    replay_count = 0
    manifest_file_count = 0
    maximum: Fraction | None = None
    minimum_margin: Fraction | None = None
    try:
        for path in (
            output / "summary.json",
            output / "manifest.json",
            output / "R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md",
        ):
            reject_result_symlink_chain(path, output, "result control file")
        summary = strict_json(output / "summary.json")
        manifest = strict_json(output / "manifest.json")
        manifest_file_count = verify_manifest(output, manifest)
        replay_count, maximum, minimum_margin = verify_summary(output, summary)
        report = (output / "R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md").read_text(
            encoding="utf-8"
        )
        normalized_report = " ".join(report.split())
        for token in (
            "NON_LICENSING",
            "Milestone status: `null`",
            "Theorem status: `null`",
            "Final status: `null`",
            "does not show that an arbitrary return",
        ):
            if token not in normalized_report:
                raise ValueError(f"report claim boundary is missing: {token}")
    except Exception as error:
        failures.append(f"{type(error).__name__}: {error}")

    checker_status = "PASS" if not failures else "FAIL"
    payload = {
        "protocol_id": "R401-VAL-L3-BT-S0",
        "licensing": "NON_LICENSING",
        "checker_status": checker_status,
        "prototype_status": PASS_STATUS if not failures else None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "raw_replay_count": replay_count,
        "manifest_file_count": manifest_file_count,
        "maximum_rslow_sq_upper": str(maximum) if maximum is not None else None,
        "minimum_margin_sq_lower": (
            str(minimum_margin) if minimum_margin is not None else None
        ),
        "failures": failures,
    }
    output.mkdir(parents=True, exist_ok=True)
    checker_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if checker_status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
