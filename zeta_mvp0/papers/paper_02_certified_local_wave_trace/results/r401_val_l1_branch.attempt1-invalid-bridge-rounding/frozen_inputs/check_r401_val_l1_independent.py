#!/usr/bin/env python3
"""Independent arithmetic and archive checker for R401-VAL-L1.

This checker deliberately does not import the production runner.  It treats
the validated CAPD flow enclosures as inputs, rebuilds every Krawczyk operator
with exact rational arithmetic from printed decimal endpoints, and verifies
the full slab/bridge gluing logic.  It is not a second ODE integrator.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_local_slab_grid_mp.cpp"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN.json"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L1_PROTOCOL.md"
RUNNER = ROOT / "scripts/run_r401_val_l1_branch.py"
V2_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_PROTOCOL_V2_FREEZE.md"
RADIAL_PROOF = ROOT / "research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md"
WARPED_PROOF = ROOT / "research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md"
CHECKER = Path(__file__).resolve()

EXPECTED_HASHES = {
    SOURCE: "9fb83e31937f8006e25cecbea818d74d90c107570f9369c9a03f7577894b1179",
    PLAN: "3d9698bd15f2d6f0d8632c364c9f2d26180b59f731da17d90fbd1d618227ca50",
    PROTOCOL: "3942d7ebcfbf4cb1b91962785869d11476745d2777c3169b1bca048218a8ff18",
    RUNNER: "f2bdddb6ce8c66e19e819c6fb7d4f8d9413a16f9fc27c17db2a295c7a34a3d93",
    V2_FREEZE: "f6f99e7c4bdd86da332848badf439eb3ed5882b8c3fd355b28b2289cf5e049a0",
    RADIAL_PROOF: "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    WARPED_PROOF: "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8",
}

NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
COORDINATES = ("q_slow", "q_fast", "p_slow", "period")
Interval = tuple[Fraction, Fraction]
Vector = list[Interval]
Matrix = list[list[Interval]]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iv(lower: Fraction | int, upper: Fraction | int | None = None) -> Interval:
    low = Fraction(lower)
    high = low if upper is None else Fraction(upper)
    if low > high:
        raise ValueError("invalid interval")
    return low, high


def add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def neg(value: Interval) -> Interval:
    return -value[1], -value[0]


def sub(left: Interval, right: Interval) -> Interval:
    return add(left, neg(right))


def mul(left: Interval, right: Interval) -> Interval:
    products = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(products), max(products)


def abs_upper(value: Interval) -> Fraction:
    return max(abs(value[0]), abs(value[1]))


def subset(left: Interval, right: Interval) -> bool:
    return right[0] <= left[0] and left[1] <= right[1]


def subset_interior(left: Interval, right: Interval) -> bool:
    return right[0] < left[0] and left[1] < right[1]


def overlap(left: Interval, right: Interval) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    result: Vector = []
    for row in matrix:
        total = iv(0)
        for coefficient, value in zip(row, vector, strict=True):
            total = add(total, mul(coefficient, value))
        result.append(total)
    return result


def matrix_matrix(left: Matrix, right: Matrix) -> Matrix:
    columns = list(zip(*right, strict=True))
    result: Matrix = []
    for row in left:
        output_row: list[Interval] = []
        for column in columns:
            total = iv(0)
            for lvalue, rvalue in zip(row, column, strict=True):
                total = add(total, mul(lvalue, rvalue))
            output_row.append(total)
        result.append(output_row)
    return result


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sub(lvalue, rvalue) for lvalue, rvalue in zip(lrow, rrow, strict=True)]
        for lrow, rrow in zip(left, right, strict=True)
    ]


def vector_add(left: Vector, right: Vector) -> Vector:
    return [add(a, b) for a, b in zip(left, right, strict=True)]


def vector_sub(left: Vector, right: Vector) -> Vector:
    return [sub(a, b) for a, b in zip(left, right, strict=True)]


def identity(dimension: int) -> Matrix:
    return [
        [iv(1 if row == column else 0) for column in range(dimension)]
        for row in range(dimension)
    ]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    value = Fraction(1)
    for pivot_column in range(len(work)):
        pivot = next(
            (row for row in range(pivot_column, len(work)) if work[row][pivot_column]),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != pivot_column:
            work[pivot_column], work[pivot] = work[pivot], work[pivot_column]
            value = -value
        pivot_value = work[pivot_column][pivot_column]
        value *= pivot_value
        for column in range(pivot_column, len(work)):
            work[pivot_column][column] /= pivot_value
        for row in range(pivot_column + 1, len(work)):
            factor = work[row][pivot_column]
            for column in range(pivot_column, len(work)):
                work[row][column] -= factor * work[pivot_column][column]
    return value


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


def intervals(value: str, expected: int) -> Vector:
    parsed = [iv(Fraction(low), Fraction(high)) for low, high in INTERVAL_PATTERN.findall(value)]
    if len(parsed) != expected:
        raise ValueError(f"expected {expected} intervals, found {len(parsed)}")
    return parsed


def parse_bool(raw: str, key: str) -> bool:
    value = extract_field(raw, key).strip()
    if value not in {"0", "1"}:
        raise ValueError(f"invalid Boolean {key}")
    return value == "1"


def as_matrix(values: Vector, rows: int, columns: int) -> Matrix:
    if len(values) != rows * columns:
        raise ValueError("matrix shape mismatch")
    return [values[row * columns : (row + 1) * columns] for row in range(rows)]


def point_midpoint_matrix(matrix: Matrix) -> tuple[Matrix, list[list[Fraction]]]:
    rational = [
        [(value[0] + value[1]) / 2 for value in row]
        for row in matrix
    ]
    return [[iv(value) for value in row] for row in rational], rational


def parse_certificate(raw: str) -> dict[str, Any]:
    x_box = intervals(extract_field(raw, "X"), 4)
    x_bar = intervals(extract_field(raw, "x_bar"), 4)
    f_center = intervals(extract_field(raw, "F_center"), 4)
    jacobian = as_matrix(intervals(extract_field(raw, "J"), 16), 4, 4)
    c_printed = as_matrix(intervals(extract_field(raw, "C"), 16), 4, 4)
    c_point, c_rational = point_midpoint_matrix(c_printed)
    defect = matrix_sub(identity(4), matrix_matrix(c_point, jacobian))
    delta = vector_sub(x_box, x_bar)
    krawczyk = vector_add(
        vector_sub(x_bar, matrix_vector(c_point, f_center)),
        matrix_vector(defect, delta),
    )
    printed_k = intervals(extract_field(raw, "K"), 4)
    row_sums = [sum(abs_upper(value) for value in row) for row in defect]
    phase_interval = intervals(extract_field(raw, "phase_interval"), 1)[0]
    initial_qplus = intervals(extract_field(raw, "initial_qplus"), 1)[0]
    terminal_qplus = intervals(extract_field(raw, "terminal_qplus"), 1)[0]
    phase_slope = intervals(extract_field(raw, "phase_gradient_qplus"), 1)[0]
    return {
        "status": extract_field(raw, "status").strip(),
        "precision_bits": int(extract_field(raw, "precision_bits").strip()),
        "epsilon": intervals(extract_field(raw, "epsilon"), 1)[0],
        "x_box": x_box,
        "x_bar": x_bar,
        "f_center": f_center,
        "jacobian": jacobian,
        "c_point": c_point,
        "c_determinant": determinant(c_rational),
        "defect": defect,
        "row_sums": row_sums,
        "krawczyk": krawczyk,
        "printed_k": printed_k,
        "phase_interval": phase_interval,
        "initial_qplus": initial_qplus,
        "terminal_qplus": terminal_qplus,
        "phase_slope": phase_slope,
        "reported_subset": parse_bool(raw, "subset_interior"),
        "reported_point_preconditioner": parse_bool(raw, "preconditioner_point"),
        "reported_contraction": parse_bool(raw, "contraction"),
        "reported_phase": parse_bool(raw, "phase_gate"),
    }


def exact_box(record: dict[str, Any], key: str) -> Interval:
    center = Fraction(str(record["center"][key]))
    radius = Fraction(str(record["root_radii"][key]))
    return center - radius, center + radius


def plan_audit(plan: dict[str, Any]) -> tuple[dict[str, bool], dict[str, dict[str, Any]]]:
    slabs = plan["slabs"]
    bridges = plan["bridges"]
    records: dict[str, dict[str, Any]] = {
        str(record["slab_id"]): record for record in slabs
    }
    records.update({str(record["bridge_id"]): record for record in bridges})
    gates = {
        "counts": len(slabs) == 51 and len(bridges) == 50,
        "coverage": (
            Fraction(str(slabs[0]["epsilon_lower"])) == 0
            and Fraction(str(slabs[-1]["epsilon_upper"])) == Fraction(101, 1000)
        ),
        "positive_radii": all(
            Fraction(str(record["root_radii"][key])) > 0
            for record in records.values()
            for key in COORDINATES
        ),
    }
    overlaps: list[Fraction] = []
    exact_bridges = True
    for index, (left, right) in enumerate(zip(slabs, slabs[1:])):
        overlap_lower = max(
            Fraction(str(left["epsilon_lower"])),
            Fraction(str(right["epsilon_lower"])),
        )
        overlap_upper = min(
            Fraction(str(left["epsilon_upper"])),
            Fraction(str(right["epsilon_upper"])),
        )
        overlaps.append(overlap_upper - overlap_lower)
        bridge = bridges[index]
        exact_bridges = exact_bridges and (
            bridge["bridge_id"] == f"B{index:03d}"
            and bridge["left_slab_id"] == left["slab_id"]
            and bridge["right_slab_id"] == right["slab_id"]
            and Fraction(str(bridge["epsilon_lower"])) == overlap_lower
            and Fraction(str(bridge["epsilon_upper"])) == overlap_upper
        )
        for key in COORDINATES:
            expected = (
                min(exact_box(left, key)[0], exact_box(right, key)[0]),
                max(exact_box(left, key)[1], exact_box(right, key)[1]),
            )
            exact_bridges = exact_bridges and exact_box(bridge, key) == expected
    gates["strict_overlaps"] = all(width > 0 for width in overlaps)
    gates["minimum_overlap_exactly_1_over_5000"] = min(overlaps) == Fraction(1, 5000)
    gates["exact_bridge_intersections_and_hulls"] = exact_bridges
    gates["period_boxes"] = all(
        Fraction(66, 100) < exact_box(record, "period")[0]
        and exact_box(record, "period")[1] < Fraction(67, 100)
        and 2 * exact_box(record, "period")[0] > Fraction(3, 4)
        for record in records.values()
    )

    old_precision = ctx.prec
    try:
        ctx.prec = 256
        a = arb(51) / 50
        c = 2 * ((1 + a).sqrt() - 1)
        lambda_fast = (c * c + 2 + c * (c * c + 4).sqrt()) / 2
        anchor = (
            arb(0),
            arb(2).sqrt() / (2 * arb.pi() * lambda_fast.sqrt()),
            arb(0),
            1 / lambda_fast.sqrt(),
        )
        anchor_inside = True
        for key, value in zip(COORDINATES, anchor, strict=True):
            lower, upper = exact_box(slabs[0], key)
            lower_arb = arb(lower.numerator) / lower.denominator
            upper_arb = arb(upper.numerator) / upper.denominator
            anchor_inside = anchor_inside and value > lower_arb
            anchor_inside = anchor_inside and value < upper_arb
    finally:
        ctx.prec = old_precision
    gates["analytic_fast_anchor_inside_S000"] = anchor_inside
    return gates, records


def resolve_manifest_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--result",
        type=Path,
        default=ROOT / "results/r401_val_l1_branch",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = args.result.resolve()
    summary_path = result / "summary.json"
    manifest_path = result / "manifest.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    plan = json.loads(PLAN.read_text(encoding="utf-8"))

    frozen_hash_gates = {
        str(path): sha256(path) == expected for path, expected in EXPECTED_HASHES.items()
    }
    manifest_hash_gates = {
        name: resolve_manifest_path(name).is_file()
        and sha256(resolve_manifest_path(name)) == digest
        for name, digest in manifest["files"].items()
    }
    plan_gates, plan_records = plan_audit(plan)

    records = summary["records"]
    certificate_by_key: dict[tuple[int, str], dict[str, Any]] = {}
    job_failures: list[dict[str, Any]] = []
    arithmetic_replays = 0
    for record in records:
        bits = int(record["precision_bits"])
        job_id = str(record["job_id"])
        raw_path = result / str(record["raw_file"])
        try:
            certificate = parse_certificate(raw_path.read_text(encoding="utf-8"))
            certificate_by_key[(bits, job_id)] = certificate
            planned = plan_records[job_id]
            requested_epsilon = (
                Fraction(str(planned["epsilon_lower"])),
                Fraction(str(planned["epsilon_upper"])),
            )
            requested_box = [exact_box(planned, key) for key in COORDINATES]
            conditions = {
                "status": certificate["status"] == "PASS_LOCAL_SLAB",
                "precision": certificate["precision_bits"] == bits,
                "epsilon_contains_request": subset(requested_epsilon, certificate["epsilon"]),
                "actual_box_contains_request": all(
                    subset(wanted, actual)
                    for wanted, actual in zip(requested_box, certificate["x_box"], strict=True)
                ),
                "preconditioner_nonsingular": certificate["c_determinant"] != 0,
                "reported_point_preconditioner": certificate["reported_point_preconditioner"],
                "energy_momentum_derivative": subset(
                    certificate["x_box"][2], certificate["jacobian"][0][2]
                ),
                "exact_krawczyk_replay": all(
                    subset_interior(image, domain)
                    for image, domain in zip(
                        certificate["krawczyk"], certificate["x_box"], strict=True
                    )
                ),
                "printed_krawczyk_strict": all(
                    subset_interior(image, domain)
                    for image, domain in zip(
                        certificate["printed_k"], certificate["x_box"], strict=True
                    )
                ),
                "exact_contraction_replay": max(certificate["row_sums"]) < 1,
                "phase_interval": (
                    certificate["phase_interval"][0] <= Fraction(1, 10)
                    and certificate["phase_interval"][1] >= Fraction(18, 100)
                ),
                "initial_phase": subset(
                    certificate["initial_qplus"], certificate["phase_interval"]
                ),
                "terminal_phase": subset(
                    certificate["terminal_qplus"], certificate["phase_interval"]
                ),
                "positive_phase_slope": certificate["phase_slope"][0] > 0,
                "period_window": (
                    certificate["x_box"][3][0] > Fraction(66, 100)
                    and certificate["x_box"][3][1] < Fraction(67, 100)
                    and 2 * certificate["x_box"][3][0] > Fraction(3, 4)
                ),
                "reported_gates": (
                    certificate["reported_subset"]
                    and certificate["reported_contraction"]
                    and certificate["reported_phase"]
                ),
            }
            arithmetic_replays += 1
            if not all(conditions.values()):
                job_failures.append(
                    {
                        "precision_bits": bits,
                        "job_id": job_id,
                        "failed_conditions": [
                            name for name, passed in conditions.items() if not passed
                        ],
                    }
                )
        except Exception as error:
            job_failures.append(
                {
                    "precision_bits": bits,
                    "job_id": job_id,
                    "exception": f"{type(error).__name__}: {error}",
                }
            )

    expected_keys = {(bits, f"S{index:03d}") for bits in (128, 256) for index in range(51)}
    expected_keys |= {(bits, f"B{index:03d}") for bits in (128, 256) for index in range(50)}
    key_gate = set(certificate_by_key) == expected_keys

    bridge_containment = True
    precision_overlap = True
    if key_gate:
        for bits in (128, 256):
            for index in range(50):
                left = certificate_by_key[(bits, f"S{index:03d}")]
                right = certificate_by_key[(bits, f"S{index + 1:03d}")]
                bridge = certificate_by_key[(bits, f"B{index:03d}")]
                bridge_containment = bridge_containment and all(
                    subset(primary_box, bridge_box)
                    for primary in (left, right)
                    for primary_box, bridge_box in zip(
                        primary["x_box"], bridge["x_box"], strict=True
                    )
                )
        for job_id in sorted({job_id for _bits, job_id in expected_keys}):
            low = certificate_by_key[(128, job_id)]
            high = certificate_by_key[(256, job_id)]
            precision_overlap = precision_overlap and all(
                overlap(a, b)
                for a, b in zip(low["x_box"], high["x_box"], strict=True)
            )
            precision_overlap = precision_overlap and all(
                overlap(a, b)
                for a, b in zip(low["printed_k"], high["printed_k"], strict=True)
            )
    else:
        bridge_containment = False
        precision_overlap = False

    global_gates = {
        "frozen_hashes": all(frozen_hash_gates.values()),
        "manifest_hashes": all(manifest_hash_gates.values()),
        "plan": all(plan_gates.values()),
        "protocol_and_status": (
            summary.get("protocol_id") == "R401-VAL-L1"
            and summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
            and summary.get("final_status") is None
            and manifest.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
            and manifest.get("final_status") is None
        ),
        "exact_job_set": key_gate,
        "all_202_arithmetic_replays": arithmetic_replays == 202 and not job_failures,
        "actual_bridge_hulls_contain_adjacent_primary_boxes": bridge_containment,
        "cross_precision_overlap": precision_overlap,
    }
    overall = all(global_gates.values())
    result_payload = {
        "protocol_id": "R401-VAL-L1",
        "checker_status": "PASS" if overall else "FAIL",
        "milestone_status": "PASS_CONTIGUOUS_LOCAL_BRANCH" if overall else None,
        "final_status": None,
        "scope": (
            "independent exact-rational replay of archived Krawczyk arithmetic, "
            "plan coverage, bridge gluing, phase gates, and hashes; not an "
            "independent ODE integration"
        ),
        "global_gates": global_gates,
        "plan_gates": plan_gates,
        "frozen_hash_gates": frozen_hash_gates,
        "manifest_file_count": len(manifest_hash_gates),
        "manifest_hash_failures": [
            name for name, passed in manifest_hash_gates.items() if not passed
        ],
        "arithmetic_replay_count": arithmetic_replays,
        "job_failures": job_failures,
        "aggregate_check_count": (
            len(frozen_hash_gates)
            + len(manifest_hash_gates)
            + len(plan_gates)
            + 7
            + 202 * 16
            + 100
            + 202
        ),
    }
    checker_path = result / "independent_checker.json"
    checker_path.write_text(
        json.dumps(result_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    postcheck = {
        "protocol_id": "R401-VAL-L1",
        "checker_status": result_payload["checker_status"],
        "milestone_status": result_payload["milestone_status"],
        "final_status": None,
        "files": {
            str(CHECKER.relative_to(ROOT)): sha256(CHECKER),
            str(summary_path.relative_to(ROOT) if summary_path.is_relative_to(ROOT) else summary_path): sha256(summary_path),
            str(manifest_path.relative_to(ROOT) if manifest_path.is_relative_to(ROOT) else manifest_path): sha256(manifest_path),
            str(checker_path.relative_to(ROOT) if checker_path.is_relative_to(ROOT) else checker_path): sha256(checker_path),
        },
    }
    (result / "POSTCHECK_STATUS.json").write_text(
        json.dumps(postcheck, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": result_payload["checker_status"],
                "arithmetic_replays": arithmetic_replays,
                "job_failures": len(job_failures),
                "aggregate_checks": result_payload["aggregate_check_count"],
            },
            indent=2,
        )
    )
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
