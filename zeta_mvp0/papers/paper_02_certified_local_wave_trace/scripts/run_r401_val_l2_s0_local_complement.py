#!/usr/bin/env python3
"""Run the R401-VAL-L2-S0 representative local-complement trees."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 100
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_local_complement_mp.cpp"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
PROTOCOL = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L2_S0_LOCAL_COMPLEMENT_PROTOCOL.md"
)
FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L2_S0_FREEZE.md"
DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"
RUNNER = Path(__file__).resolve()
CHECKER = ROOT / "scripts/check_r401_val_l2_s0_local_complement_independent.py"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER_RESULT = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"

EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
COORDINATES = ("q_slow", "q_fast", "p_slow", "period")
BIG_BOX = {
    "q_slow": (Decimal("-0.02"), Decimal("0.02")),
    "q_fast": (Decimal("0.12"), Decimal("0.17")),
    "p_slow": (Decimal("-0.08"), Decimal("0.08")),
    "period": (Decimal("0.64"), Decimal("0.69")),
}
FULL_WIDTHS = {
    key: upper - lower for key, (lower, upper) in BIG_BOX.items()
}
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decimal_text(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text if text not in {"", "-0"} else "0"


def interval_text(interval: tuple[Decimal, Decimal]) -> list[str]:
    return [decimal_text(interval[0]), decimal_text(interval[1])]


def extract_scalar(raw: str, key: str) -> str | None:
    prefix = f"{key}="
    values = [line[len(prefix) :].strip() for line in raw.splitlines() if line.startswith(prefix)]
    return values[-1] if values else None


def extract_intervals(raw: str, key: str, expected: int | None = None) -> list[list[str]]:
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
        intervals = [list(match.groups()) for match in INTERVAL_PATTERN.finditer(value)]
        if expected is not None and len(intervals) != expected:
            raise ValueError(f"{key}: expected {expected} intervals, found {len(intervals)}")
        return intervals
    raise ValueError(f"missing field {key}")


def root_box(record: dict[str, Any]) -> dict[str, tuple[Decimal, Decimal]]:
    answer: dict[str, tuple[Decimal, Decimal]] = {}
    for key in COORDINATES:
        center = Decimal(str(record["center"][key]))
        radius = Decimal(str(record["root_radii"][key]))
        answer[key] = (center - radius, center + radius)
    return answer


def parsed_decimal_box(values: list[list[str]] | list[tuple[str, str]]) -> list[tuple[Decimal, Decimal]]:
    return [(Decimal(pair[0]), Decimal(pair[1])) for pair in values]


def validate_l1_protected_boxes(
    selected_ids: tuple[str, ...],
    plan_records: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    release = json.loads(L1_RELEASE.read_text(encoding="utf-8"))
    summary = json.loads(L1_SUMMARY.read_text(encoding="utf-8"))
    checker = json.loads(L1_CHECKER_RESULT.read_text(encoding="utf-8"))
    postcheck = json.loads(L1_POSTCHECK.read_text(encoding="utf-8"))
    release_hash_gates = {
        key: (ROOT / key).is_file() and sha256(ROOT / key) == expected
        for key, expected in release["files"].items()
    }
    records = {
        (int(record["precision_bits"]), str(record["job_id"])): record
        for record in summary["records"]
        if record["job_type"] == "primary"
    }
    box_gates: dict[str, dict[str, Any]] = {}
    for slab_id in selected_ids:
        planned_box = root_box(plan_records[slab_id])
        for bits in (128, 256):
            record = records[(bits, slab_id)]
            actual = parsed_decimal_box(record["root_box"])
            image = parsed_decimal_box(record["krawczyk_image"])
            requested_inside_actual = all(
                actual[index][0] <= planned_box[key][0]
                and planned_box[key][1] <= actual[index][1]
                for index, key in enumerate(COORDINATES)
            )
            image_strict_inside_requested = all(
                planned_box[key][0] < image[index][0]
                <= image[index][1] < planned_box[key][1]
                for index, key in enumerate(COORDINATES)
            )
            margins = [
                min(
                    image[index][0] - planned_box[key][0],
                    planned_box[key][1] - image[index][1],
                )
                for index, key in enumerate(COORDINATES)
            ]
            box_gates[f"{bits}:{slab_id}"] = {
                "record_passed": bool(record["passed"]),
                "requested_plan_box_inside_actual_validated_X": requested_inside_actual,
                "krawczyk_image_strict_inside_requested_plan_box": image_strict_inside_requested,
                "minimum_plan_box_image_margin": decimal_text(min(margins)),
            }
    status_gates = {
        "release_status": release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH",
        "release_final_status_null": release.get("final_status") is None,
        "summary_status": summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH",
        "independent_checker_status": checker.get("checker_status") == "PASS",
        "postcheck_checker_status": postcheck.get("checker_status") == "PASS",
        "postcheck_status": postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH",
        "release_hash_chain": all(release_hash_gates.values()),
        "selected_box_gates": all(
            all(value for key, value in gate.items() if key != "minimum_plan_box_image_margin")
            for gate in box_gates.values()
        ),
    }
    return {
        "status_gates": status_gates,
        "release_hash_gates": release_hash_gates,
        "box_gates": box_gates,
        "all_pass": all(status_gates.values()),
    }


def strict_inside(
    inner: dict[str, tuple[Decimal, Decimal]],
    outer: dict[str, tuple[Decimal, Decimal]],
) -> bool:
    return all(
        outer[key][0] < inner[key][0] < inner[key][1] < outer[key][1]
        for key in COORDINATES
    )


def complement_shells(
    outer: dict[str, tuple[Decimal, Decimal]],
    protected: dict[str, tuple[Decimal, Decimal]],
) -> list[tuple[str, dict[str, tuple[Decimal, Decimal]]]]:
    """Exact 2d coordinate-shell decomposition of outer minus protected."""

    shells: list[tuple[str, dict[str, tuple[Decimal, Decimal]]]] = []
    prefix = dict(outer)
    for index, key in enumerate(COORDINATES):
        lower = dict(prefix)
        lower[key] = (outer[key][0], protected[key][0])
        upper = dict(prefix)
        upper[key] = (protected[key][1], outer[key][1])
        shells.append((f"C{index}L", lower))
        shells.append((f"C{index}U", upper))
        prefix[key] = protected[key]
    return shells


@dataclass(frozen=True)
class Node:
    node_id: str
    parent_id: str | None
    depth: int
    box: dict[str, tuple[Decimal, Decimal]]

    def arguments(self, binary: Path, bits: int, epsilon: tuple[str, str]) -> list[str]:
        values: list[str] = []
        for key in COORDINATES:
            values.extend(interval_text(self.box[key]))
        return [str(binary), str(bits), *epsilon, *values]


def split_node(node: Node) -> tuple[str, Decimal, Node, Node]:
    coordinate = max(
        COORDINATES,
        key=lambda key: (node.box[key][1] - node.box[key][0]) / FULL_WIDTHS[key],
    )
    lower, upper = node.box[coordinate]
    midpoint = (lower + upper) / 2
    if not lower < midpoint < upper:
        raise ArithmeticError(f"non-strict midpoint for {node.node_id}")
    left_box = dict(node.box)
    right_box = dict(node.box)
    left_box[coordinate] = (lower, midpoint)
    right_box[coordinate] = (midpoint, upper)
    return (
        coordinate,
        midpoint,
        Node(node.node_id + "0", node.node_id, node.depth + 1, left_box),
        Node(node.node_id + "1", node.node_id, node.depth + 1, right_box),
    )


def evaluate_node(
    binary: Path,
    raw_directory: Path,
    bits: int,
    slab_id: str,
    epsilon: tuple[str, str],
    node: Node,
) -> dict[str, Any]:
    raw_path = raw_directory / f"{node.node_id}.txt"
    stderr_path = raw_directory / f"{node.node_id}.stderr.txt"
    command = node.arguments(binary, bits, epsilon)
    started = time.monotonic()
    process = subprocess.run(command, text=True, capture_output=True)
    elapsed = time.monotonic() - started
    raw_path.write_text(process.stdout, encoding="utf-8")
    stderr_path.write_text(process.stderr, encoding="utf-8")
    result_root = raw_directory.parents[2]
    status = extract_scalar(process.stdout, "status") or "NO_STATUS"
    record: dict[str, Any] = {
        "node_id": node.node_id,
        "parent_id": node.parent_id,
        "depth": node.depth,
        "box": {key: interval_text(node.box[key]) for key in COORDINATES},
        "precision_bits": bits,
        "slab_id": slab_id,
        "epsilon": list(epsilon),
        "returncode": process.returncode,
        "evaluator_status": status,
        "raw_file": str(raw_path.relative_to(result_root)),
        "stderr_file": str(stderr_path.relative_to(result_root)),
        "wall_seconds": elapsed,
    }
    try:
        record["qplus_input"] = extract_intervals(process.stdout, "qplus_input", 1)[0]
        record["energy_qplus"] = extract_intervals(process.stdout, "energy_qplus", 1)[0]
    except ValueError:
        pass
    if status == "RETURN_EXCLUDED":
        record["direct_component"] = int(extract_scalar(process.stdout, "direct_component") or -1)
        record["mean_component"] = int(extract_scalar(process.stdout, "mean_component") or -1)
        record["preconditioned_component"] = int(
            extract_scalar(process.stdout, "preconditioned_component") or -1
        )
    return record


def run_tree(
    *,
    binary: Path,
    output: Path,
    bits: int,
    slab: dict[str, Any],
    workers: int,
    max_depth: int,
    max_nodes: int,
) -> dict[str, Any]:
    slab_id = str(slab["slab_id"])
    epsilon = (str(slab["epsilon_lower"]), str(slab["epsilon_upper"]))
    protected = root_box(slab)
    if not strict_inside(protected, BIG_BOX):
        raise ValueError(f"protected root box is not strict inside B_loc: {slab_id}")
    shells = complement_shells(BIG_BOX, protected)
    raw_directory = output / "raw" / str(bits) / slab_id
    raw_directory.mkdir(parents=True, exist_ok=True)
    queue = [Node(shell_id, None, 0, box) for shell_id, box in shells]
    records: list[dict[str, Any]] = []
    terminal_counts = {
        "ENERGY_EXCLUDED": 0,
        "RETURN_EXCLUDED": 0,
        "ROOT_CANDIDATE": 0,
        "INVALID": 0,
        "UNRESOLVED": 0,
    }
    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        while queue and len(records) < max_nodes:
            capacity = max_nodes - len(records)
            batch = queue[: min(workers, capacity)]
            del queue[: len(batch)]
            futures = {
                executor.submit(
                    evaluate_node,
                    binary,
                    raw_directory,
                    bits,
                    slab_id,
                    epsilon,
                    node,
                ): node
                for node in batch
            }
            completed: list[tuple[Node, dict[str, Any]]] = []
            for future in as_completed(futures):
                completed.append((futures[future], future.result()))
            completed.sort(key=lambda pair: pair[0].node_id)
            for node, record in completed:
                status = str(record["evaluator_status"])
                if status in {"ENERGY_EXCLUDED", "RETURN_EXCLUDED"} and record["returncode"] == 0:
                    record["tree_classification"] = status
                    terminal_counts[status] += 1
                elif status == "ROOT_CANDIDATE" or record["returncode"] == 4:
                    record["tree_classification"] = "ROOT_CANDIDATE"
                    terminal_counts["ROOT_CANDIDATE"] += 1
                elif status.startswith("INVALID_") or record["returncode"] == 5:
                    record["tree_classification"] = "INVALID"
                    terminal_counts["INVALID"] += 1
                elif node.depth >= max_depth:
                    record["tree_classification"] = "UNRESOLVED"
                    record["unresolved_reason"] = "MAX_DEPTH"
                    terminal_counts["UNRESOLVED"] += 1
                else:
                    coordinate, midpoint, left, right = split_node(node)
                    record["tree_classification"] = "SPLIT"
                    record["split_coordinate"] = coordinate
                    record["split_midpoint"] = decimal_text(midpoint)
                    record["children"] = [left.node_id, right.node_id]
                    queue.extend((left, right))
                records.append(record)

    if queue:
        terminal_counts["UNRESOLVED"] += len(queue)
        for node in queue:
            records.append(
                {
                    "node_id": node.node_id,
                    "parent_id": node.parent_id,
                    "depth": node.depth,
                    "box": {key: interval_text(node.box[key]) for key in COORDINATES},
                    "precision_bits": bits,
                    "slab_id": slab_id,
                    "epsilon": list(epsilon),
                    "tree_classification": "UNRESOLVED",
                    "unresolved_reason": "NODE_BUDGET",
                }
            )
    records.sort(key=lambda item: (int(item["depth"]), str(item["node_id"])))
    complete = (
        terminal_counts["ROOT_CANDIDATE"] == 0
        and terminal_counts["INVALID"] == 0
        and terminal_counts["UNRESOLVED"] == 0
        and not queue
    )
    tree = {
        "protocol_id": "R401-VAL-L2-S0",
        "precision_bits": bits,
        "slab_id": slab_id,
        "epsilon": list(epsilon),
        "big_box": {key: interval_text(BIG_BOX[key]) for key in COORDINATES},
        "protected_l1_box": {
            key: interval_text(protected[key]) for key in COORDINATES
        },
        "initial_shell_ids": [shell_id for shell_id, _box in shells],
        "protected_route": "A4.12 / R401-VAL-L1-V2",
        "max_depth": max_depth,
        "max_nodes": max_nodes,
        "evaluated_node_count": sum("evaluator_status" in record for record in records),
        "stored_node_count": len(records),
        "terminal_counts": terminal_counts,
        "complete": complete,
        "wall_seconds": time.monotonic() - started,
        "nodes": records,
    }
    tree_path = output / "trees" / str(bits) / f"{slab_id}.json"
    tree_path.parent.mkdir(parents=True, exist_ok=True)
    tree_path.write_text(json.dumps(tree, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tree["tree_file"] = str(tree_path.relative_to(output))
    return tree


def command_output(command: list[str]) -> str:
    return subprocess.run(command, check=True, text=True, capture_output=True).stdout.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capd-build", type=Path, default=Path("/tmp/capd_probe.W9FsjR/build_mp2"))
    parser.add_argument("--capd-source", type=Path, default=Path("/tmp/capd_probe.W9FsjR"))
    parser.add_argument("--output", type=Path, default=ROOT / "results/r401_val_l2_s0_local_complement")
    parser.add_argument("--workers", type=int, default=min(24, os.cpu_count() or 1))
    parser.add_argument("--max-depth", type=int, default=40)
    parser.add_argument("--max-nodes", type=int, default=20_000)
    parser.add_argument("--precisions", type=int, nargs="+", choices=(128, 256), default=(128, 256))
    parser.add_argument("--slabs", nargs="+", choices=REPRESENTATIVE_SLABS, default=REPRESENTATIVE_SLABS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    output.mkdir(parents=True)

    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    selected_ids = tuple(dict.fromkeys(args.slabs))
    selected = [record for record in plan["slabs"] if record["slab_id"] in selected_ids]
    if {record["slab_id"] for record in selected} != set(selected_ids):
        raise ValueError("not every requested representative slab is present")
    selected_plan_records = {str(record["slab_id"]): record for record in selected}
    l1_protected_gates = validate_l1_protected_boxes(selected_ids, selected_plan_records)
    if not l1_protected_gates["all_pass"]:
        raise RuntimeError(f"accepted L1 protected-box gates failed: {l1_protected_gates}")

    capd_commit = command_output(["git", "-C", str(args.capd_source.resolve()), "rev-parse", "HEAD"])
    if capd_commit != EXPECTED_CAPD_COMMIT:
        raise RuntimeError(f"unexpected CAPD commit {capd_commit}")
    capd_config = args.capd_build.resolve() / "bin/capd-config"
    flags = shlex.split(command_output([str(capd_config), "--cflags", "--libs"]))
    required = {"-D__HAVE_MPFR__", "-lmpfr", "-lgmp", "-frounding-math"}
    if not required.issubset(flags):
        raise RuntimeError(f"missing CAPD flags {required - set(flags)}")
    binary = output / "capd_r401_local_complement_mp"
    compile_command = ["g++", "-O2", str(SOURCE), *flags, "-o", str(binary)]
    compilation = subprocess.run(compile_command, text=True, capture_output=True)
    (output / "compile_stdout.txt").write_text(compilation.stdout, encoding="utf-8")
    (output / "compile_stderr.txt").write_text(compilation.stderr, encoding="utf-8")
    if compilation.returncode != 0:
        raise RuntimeError("CAPD complement evaluator compilation failed")

    requested_precisions = tuple(dict.fromkeys(args.precisions))
    trees: list[dict[str, Any]] = []
    started = time.monotonic()
    for bits in requested_precisions:
        for slab in selected:
            tree = run_tree(
                binary=binary,
                output=output,
                bits=bits,
                slab=slab,
                workers=args.workers,
                max_depth=args.max_depth,
                max_nodes=args.max_nodes,
            )
            trees.append({key: value for key, value in tree.items() if key != "nodes"})
            print(
                json.dumps(
                    {
                        "bits": bits,
                        "slab": slab["slab_id"],
                        "complete": tree["complete"],
                        "nodes": tree["evaluated_node_count"],
                        "terminal_counts": tree["terminal_counts"],
                    },
                    sort_keys=True,
                ),
                flush=True,
            )

    production_matrix = (
        set(requested_precisions) == {128, 256}
        and set(selected_ids) == set(REPRESENTATIVE_SLABS)
        and args.max_depth == 40
        and args.max_nodes == 20_000
    )
    all_complete = all(bool(tree["complete"]) for tree in trees)
    overall = production_matrix and all_complete and l1_protected_gates["all_pass"]
    summary = {
        "protocol_id": "R401-VAL-L2-S0",
        "producer_status": "PASS_S0_PRODUCER" if overall else "INCONCLUSIVE_S0_PRODUCER",
        "milestone_status": None,
        "final_status": None,
        "claim_boundary": (
            "validated complement-tree implementation on S000/S025/S050 only; "
            "not an all-slab local complement, phase cover, global cover, delta_tr, "
            "prime-trace, Hilbert-Polya, zeta-zero, or RH result"
        ),
        "representative_slabs": list(selected_ids),
        "precisions": list(requested_precisions),
        "production_matrix": production_matrix,
        "all_trees_complete": all_complete,
        "l1_protected_box_gates": l1_protected_gates,
        "tree_summaries": trees,
        "environment": {
            "python": sys.version,
            "capd_commit": capd_commit,
            "capd_flags": flags,
            "compiler": command_output(["g++", "--version"]).splitlines()[0],
            "workers": args.workers,
            "wall_seconds": time.monotonic() - started,
        },
        "input_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                SOURCE,
                PLAN,
                PROTOCOL,
                FREEZE,
                DEPENDENCY,
                RUNNER,
                CHECKER,
                L1_RELEASE,
                L1_SUMMARY,
                L1_MANIFEST,
                L1_CHECKER_RESULT,
                L1_POSTCHECK,
            )
        },
    }
    summary_path = output / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# R401-VAL-L2-S0 representative local complement",
        "",
        f"Producer status: **{summary['producer_status']}**.",
        "",
        "The validated tree was run on the beginning, middle, and endpoint L1",
        "parameter slabs at 128 and 256 MPFR bits.",
        "",
        "| Bits | Slab | Evaluated nodes | Energy excluded | Return excluded | Unresolved | Complete |",
        "|---:|:---:|---:|---:|---:|---:|:---:|",
    ]
    for tree in trees:
        counts = tree["terminal_counts"]
        lines.append(
            f"| {tree['precision_bits']} | {tree['slab_id']} | "
            f"{tree['evaluated_node_count']} | {counts['ENERGY_EXCLUDED']} | "
            f"{counts['RETURN_EXCLUDED']} | {counts['UNRESOLVED']} | "
            f"{'PASS' if tree['complete'] else 'FAIL'} |"
        )
    lines.extend(
        [
            "",
            "A pass licenses only the complement-engine implementation on these",
            "three representative slabs.  The other 48 slabs, the local phase-cover",
            "tree, the global shell cover, the final determinant cross-check, and all",
            "arithmetic/Hilbert--Polya claims remain open.",
            "",
        ]
    )
    report_path = output / "R401_VAL_L2_S0_REPORT.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    manifest_targets = [
        SOURCE,
        PLAN,
        PROTOCOL,
        FREEZE,
        DEPENDENCY,
        RUNNER,
        CHECKER,
        L1_RELEASE,
        L1_SUMMARY,
        L1_MANIFEST,
        L1_CHECKER_RESULT,
        L1_POSTCHECK,
        binary,
        summary_path,
        report_path,
        output / "compile_stdout.txt",
        output / "compile_stderr.txt",
    ]
    manifest_targets.extend(sorted((output / "trees").rglob("*.json")))
    manifest_targets.extend(sorted((output / "raw").rglob("*.txt")))
    manifest = {
        "protocol_id": "R401-VAL-L2-S0",
        "producer_status": summary["producer_status"],
        "milestone_status": None,
        "final_status": None,
        "capd_commit": capd_commit,
        "files": {
            str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path): sha256(path)
            for path in manifest_targets
        },
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": summary["producer_status"], "output": str(output)}, indent=2))
    return 0 if overall else 2


if __name__ == "__main__":
    raise SystemExit(main())
