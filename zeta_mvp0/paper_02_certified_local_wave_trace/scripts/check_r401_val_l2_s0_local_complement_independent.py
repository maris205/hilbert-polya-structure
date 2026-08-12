#!/usr/bin/env python3
"""Independent exact-decimal checker for R401-VAL-L2-S0 trees.

This checker intentionally does not import the production driver or run an
ODE solver.  It verifies the rectangular cover, every binary split, every
stored interval-Newton contraction decision, and every displayed return
separation from the archived decimal proof objects.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L2_S0_LOCAL_COMPLEMENT_PROTOCOL.md"
FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L2_S0_FREEZE.md"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_CHECKER_RESULT = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"
REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
COORDINATES = ("q_slow", "q_fast", "p_slow", "period")
BIG_BOX = {
    "q_slow": (Fraction(-1, 50), Fraction(1, 50)),
    "q_fast": (Fraction(3, 25), Fraction(17, 100)),
    "p_slow": (Fraction(-2, 25), Fraction(2, 25)),
    "period": (Fraction(16, 25), Fraction(69, 100)),
}
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")
Interval = tuple[Fraction, Fraction]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interval(values: list[str] | tuple[str, str]) -> Interval:
    result = (Fraction(values[0]), Fraction(values[1]))
    if result[0] > result[1]:
        raise ValueError(f"reversed interval {values}")
    return result


def extract_scalar(raw: str, key: str) -> str:
    prefix = f"{key}="
    values = [line[len(prefix) :].strip() for line in raw.splitlines() if line.startswith(prefix)]
    if not values:
        raise ValueError(f"missing field {key}")
    return values[-1]


def extract_intervals(raw: str, key: str, expected: int | None = None) -> list[Interval]:
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
        parsed = [(Fraction(a), Fraction(b)) for a, b in INTERVAL_PATTERN.findall(value)]
        if expected is not None and len(parsed) != expected:
            raise ValueError(f"{key}: expected {expected}, got {len(parsed)}")
        if any(a > b for a, b in parsed):
            raise ValueError(f"{key}: reversed interval")
        return parsed
    raise ValueError(f"missing field {key}")


def intersection(left: Interval, right: Interval) -> Interval | None:
    lower = max(left[0], right[0])
    upper = min(left[1], right[1])
    return None if lower > upper else (lower, upper)


def subset(inner: Interval, outer: Interval) -> bool:
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def interval_subtract(left: Interval, right: Interval) -> Interval:
    return left[0] - right[1], left[1] - right[0]


def interval_divide(numerator: Interval, denominator: Interval) -> Interval:
    if denominator[0] <= 0 <= denominator[1]:
        raise ZeroDivisionError("interval denominator contains zero")
    candidates = (
        numerator[0] / denominator[0],
        numerator[0] / denominator[1],
        numerator[1] / denominator[0],
        numerator[1] / denominator[1],
    )
    return min(candidates), max(candidates)


def interval_gap(left: Interval, right: Interval) -> Fraction:
    if left[1] < right[0]:
        return right[0] - left[1]
    if right[1] < left[0]:
        return left[0] - right[1]
    return Fraction(0)


def omits_zero_with_margin(value: Interval, margin: Fraction) -> bool:
    return value[1] < -margin or value[0] > margin


def box_from_json(payload: dict[str, list[str]]) -> dict[str, Interval]:
    return {key: interval(payload[key]) for key in COORDINATES}


def plan_root_box(record: dict[str, Any]) -> dict[str, Interval]:
    answer: dict[str, Interval] = {}
    for key in COORDINATES:
        center = Fraction(str(record["center"][key]))
        radius = Fraction(str(record["root_radii"][key]))
        answer[key] = (center - radius, center + radius)
    return answer


def expected_shells(protected: dict[str, Interval]) -> dict[str, dict[str, Interval]]:
    shells: dict[str, dict[str, Interval]] = {}
    prefix = dict(BIG_BOX)
    for index, key in enumerate(COORDINATES):
        lower = dict(prefix)
        upper = dict(prefix)
        lower[key] = (BIG_BOX[key][0], protected[key][0])
        upper[key] = (protected[key][1], BIG_BOX[key][1])
        shells[f"C{index}L"] = lower
        shells[f"C{index}U"] = upper
        prefix[key] = protected[key]
    return shells


def verify_l1_protected_boxes(
    planned: dict[str, dict[str, Any]],
) -> tuple[bool, int, list[str], dict[str, Any]]:
    failures: list[str] = []
    checks = 0
    release = json.loads(L1_RELEASE.read_text(encoding="utf-8"))
    summary = json.loads(L1_SUMMARY.read_text(encoding="utf-8"))
    checker = json.loads(L1_CHECKER_RESULT.read_text(encoding="utf-8"))
    postcheck = json.loads(L1_POSTCHECK.read_text(encoding="utf-8"))
    status_values = (
        release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH",
        release.get("final_status") is None,
        summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH",
        checker.get("checker_status") == "PASS",
        postcheck.get("checker_status") == "PASS",
        postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH",
    )
    checks += len(status_values)
    if not all(status_values):
        failures.append("accepted L1 status chain failed")
    for key, expected in release["files"].items():
        path = ROOT / key
        checks += 1
        if not path.is_file() or sha256(path) != expected:
            failures.append(f"L1 release hash mismatch: {key}")

    records = {
        (int(record["precision_bits"]), str(record["job_id"])): record
        for record in summary["records"]
        if record["job_type"] == "primary"
    }
    minimum_margin: Fraction | None = None
    for slab_id in REPRESENTATIVE_SLABS:
        requested = plan_root_box(planned[slab_id])
        for bits in (128, 256):
            checks += 4
            record = records.get((bits, slab_id))
            if record is None or not record.get("passed"):
                failures.append(f"L1 passing record missing: {bits}:{slab_id}")
                continue
            actual = [interval(pair) for pair in record["root_box"]]
            image = [interval(pair) for pair in record["krawczyk_image"]]
            requested_inside_actual = all(
                subset(requested[key], actual[index])
                for index, key in enumerate(COORDINATES)
            )
            image_inside_requested = all(
                requested[key][0] < image[index][0]
                <= image[index][1] < requested[key][1]
                for index, key in enumerate(COORDINATES)
            )
            if not requested_inside_actual:
                failures.append(f"L1 plan box not enclosed by actual X: {bits}:{slab_id}")
            if not image_inside_requested:
                failures.append(f"L1 Krawczyk image not strict in plan box: {bits}:{slab_id}")
            margins = [
                min(
                    image[index][0] - requested[key][0],
                    requested[key][1] - image[index][1],
                )
                for index, key in enumerate(COORDINATES)
            ]
            cell_margin = min(margins)
            minimum_margin = cell_margin if minimum_margin is None else min(minimum_margin, cell_margin)
    result = {
        "release_sha256": sha256(L1_RELEASE),
        "minimum_krawczyk_to_plan_boundary_margin": (
            None
            if minimum_margin is None
            else {"numerator": minimum_margin.numerator, "denominator": minimum_margin.denominator}
        ),
    }
    return not failures, checks, failures, result


def verify_energy_steps(raw: str, status: str) -> tuple[bool, int, list[str]]:
    failures: list[str] = []
    step_ids = sorted({int(value) for value in re.findall(r"^energy_step_(\d+)_before=", raw, re.MULTILINE)})
    if not step_ids or step_ids != list(range(len(step_ids))):
        return False, 1, ["energy step indices are missing or non-contiguous"]
    qplus_input = extract_intervals(raw, "qplus_input", 1)[0]
    bits = int(extract_scalar(raw, "precision_bits"))
    expected_margin = Fraction(1, 10**30) if bits == 128 else Fraction(1, 10**60)
    expected_guard = Fraction(1, 10**40) if bits == 128 else Fraction(1, 10**75)
    margin_interval = extract_intervals(raw, "logical_margin", 1)[0]
    guard_interval = extract_intervals(raw, "newton_guard", 1)[0]
    if margin_interval[0] < expected_margin:
        failures.append("represented logical margin is below the frozen precision gate")
    if not subset((-expected_guard, expected_guard), guard_interval):
        failures.append("printed Newton guard does not enclose the frozen guard")
    current = qplus_input
    checks = 3
    final_after: Interval | None = None
    empty_seen = False
    for step_id in step_ids:
        prefix = f"energy_step_{step_id}"
        before = extract_intervals(raw, prefix + "_before", 1)[0]
        midpoint = extract_intervals(raw, prefix + "_midpoint", 1)[0]
        residual = extract_intervals(raw, prefix + "_residual", 1)[0]
        derivative = extract_intervals(raw, prefix + "_derivative", 1)[0]
        checks += 5
        if before != current:
            failures.append(f"{prefix}: before does not equal previous contraction")
        if not subset(midpoint, before):
            failures.append(f"{prefix}: midpoint enclosure is not inside before")
        if derivative[0] <= 0:
            failures.append(f"{prefix}: derivative is not strictly positive")
        if residual[0] > residual[1]:
            failures.append(f"{prefix}: residual reversed")
        intersects = extract_scalar(raw, prefix + "_intersects")
        newton_raw = extract_intervals(raw, prefix + "_newton_raw", 1)[0]
        newton = extract_intervals(raw, prefix + "_newton", 1)[0]
        recomputed_newton = interval_subtract(midpoint, interval_divide(residual, derivative))
        printed_intersection = intersection(before, newton)
        checks += 5
        if not subset(recomputed_newton, newton):
            failures.append(f"{prefix}: guarded Newton does not enclose recomputed m-F/D")
        if not subset(newton_raw, newton):
            failures.append(f"{prefix}: guarded Newton does not enclose printed raw Newton")
        if intersects == "0":
            empty_seen = True
            gap = extract_intervals(raw, prefix + "_gap", 1)[0]
            recomputed_gap = interval_gap(before, newton)
            checks += 2
            if printed_intersection is not None:
                failures.append(f"{prefix}: claimed empty but printed intervals intersect")
            if recomputed_gap <= expected_margin:
                failures.append(f"{prefix}: recomputed printed-interval gap lacks frozen margin")
            if gap[0] <= expected_margin:
                failures.append(f"{prefix}: empty-intersection gap lacks frozen margin")
            if step_id != step_ids[-1]:
                failures.append(f"{prefix}: steps continue after empty intersection")
        elif intersects == "1":
            after = extract_intervals(raw, prefix + "_after", 1)[0]
            recomputed_intersection = intersection(before, recomputed_newton)
            checks += 3
            if recomputed_intersection is None or not subset(recomputed_intersection, after):
                failures.append(f"{prefix}: after does not enclose recomputed safe intersection")
            if not subset(after, before) or not subset(after, newton):
                failures.append(f"{prefix}: after is not a contraction of before and guarded Newton")
            current = after
            final_after = after
        else:
            failures.append(f"{prefix}: invalid intersects flag {intersects}")
    if status == "ENERGY_EXCLUDED":
        checks += 1
        if not empty_seen:
            failures.append("ENERGY_EXCLUDED without an empty Newton intersection")
    else:
        reported = extract_intervals(raw, "energy_qplus", 1)[0]
        checks += 1
        if final_after is None or reported != final_after:
            failures.append("reported energy_qplus does not equal final contraction")
    return not failures, checks, failures


def verify_return_exclusion(raw: str) -> tuple[bool, int, list[str]]:
    failures: list[str] = []
    fields = (
        ("direct_component", "F_direct"),
        ("mean_component", "F_mean"),
        ("preconditioned_component", "F_preconditioned"),
    )
    licensed = 0
    checks = 0
    bits = int(extract_scalar(raw, "precision_bits"))
    margin = Fraction(1, 10**30) if bits == 128 else Fraction(1, 10**60)
    for component_field, interval_field in fields:
        component = int(extract_scalar(raw, component_field))
        values = extract_intervals(raw, interval_field, 4)
        checks += 2
        if component >= 0:
            if component > 3:
                failures.append(f"{component_field}: invalid index {component}")
            elif not omits_zero_with_margin(values[component], margin):
                failures.append(f"{component_field}: selected interval lacks frozen zero margin")
            else:
                licensed += 1
    checks += 1
    if licensed == 0:
        failures.append("RETURN_EXCLUDED has no displayed separating component")
    return not failures, checks, failures


def verify_tree(
    output: Path,
    tree_path: Path,
    planned: dict[str, Any],
) -> tuple[bool, int, list[str], dict[str, Any]]:
    tree = json.loads(tree_path.read_text(encoding="utf-8"))
    failures: list[str] = []
    checks = 0
    protected = plan_root_box(planned)
    expected_epsilon = (
        Fraction(str(planned["epsilon_lower"])),
        Fraction(str(planned["epsilon_upper"])),
    )
    expected_slab_id = str(planned["slab_id"])
    expected_bits = int(tree_path.parent.name)
    checks += 9
    if tree.get("protocol_id") != "R401-VAL-L2-S0":
        failures.append("tree protocol ID mismatch")
    if str(tree.get("slab_id")) != expected_slab_id or tree_path.stem != expected_slab_id:
        failures.append("tree slab/path binding mismatch")
    if int(tree.get("precision_bits", -1)) != expected_bits:
        failures.append("tree precision/path binding mismatch")
    if interval(tree["epsilon"]) != expected_epsilon:
        failures.append("tree epsilon differs from frozen L1 slab")
    if box_from_json(tree["big_box"]) != BIG_BOX:
        failures.append("big_box differs from frozen B_loc")
    if box_from_json(tree["protected_l1_box"]) != protected:
        failures.append("protected box differs from L1 plan")
    if not all(BIG_BOX[key][0] < protected[key][0] < protected[key][1] < BIG_BOX[key][1] for key in COORDINATES):
        failures.append("protected box is not strict inside B_loc")
    shells = expected_shells(protected)
    if tree["initial_shell_ids"] != list(shells):
        failures.append("initial shell IDs/order differs from exact decomposition")

    nodes = tree["nodes"]
    by_id = {str(node["node_id"]): node for node in nodes}
    root_ids = set(shells)
    referenced_children: set[str] = set()
    if len(by_id) != len(nodes):
        failures.append("duplicate node IDs")
    for shell_id, shell_box in shells.items():
        checks += 2
        node = by_id.get(shell_id)
        if node is None or node.get("parent_id") is not None or int(node.get("depth", -1)) != 0:
            failures.append(f"missing/malformed root shell {shell_id}")
        elif box_from_json(node["box"]) != shell_box:
            failures.append(f"root shell box mismatch {shell_id}")

    terminal = 0
    computed_terminal_counts = {
        "ENERGY_EXCLUDED": 0,
        "RETURN_EXCLUDED": 0,
        "ROOT_CANDIDATE": 0,
        "INVALID": 0,
        "UNRESOLVED": 0,
    }
    for node_id, node in by_id.items():
        classification = str(node["tree_classification"])
        node_box = box_from_json(node["box"])
        checks += 3
        if str(node.get("slab_id")) != expected_slab_id:
            failures.append(f"{node_id}: node slab mismatch")
        if int(node.get("precision_bits", -1)) != expected_bits:
            failures.append(f"{node_id}: node precision mismatch")
        if interval(node["epsilon"]) != expected_epsilon:
            failures.append(f"{node_id}: node epsilon differs from frozen slab")
        if classification == "SPLIT":
            children = node.get("children", [])
            checks += 5
            if len(children) != 2 or any(child not in by_id for child in children):
                failures.append(f"{node_id}: missing children")
                continue
            left = by_id[children[0]]
            right = by_id[children[1]]
            coordinate = str(node["split_coordinate"])
            midpoint = Fraction(str(node["split_midpoint"]))
            if coordinate not in COORDINATES:
                failures.append(f"{node_id}: invalid split coordinate")
                continue
            left_box = box_from_json(left["box"])
            right_box = box_from_json(right["box"])
            if left.get("parent_id") != node_id or right.get("parent_id") != node_id:
                failures.append(f"{node_id}: child parent mismatch")
            if int(left["depth"]) != int(node["depth"]) + 1 or int(right["depth"]) != int(node["depth"]) + 1:
                failures.append(f"{node_id}: child depth mismatch")
            exact_midpoint = (node_box[coordinate][0] + node_box[coordinate][1]) / 2
            expected_coordinate = max(
                COORDINATES,
                key=lambda key: (node_box[key][1] - node_box[key][0])
                / (BIG_BOX[key][1] - BIG_BOX[key][0]),
            )
            if midpoint != exact_midpoint:
                failures.append(f"{node_id}: split is not the exact midpoint")
            if coordinate != expected_coordinate:
                failures.append(f"{node_id}: split coordinate violates frozen width rule")
            referenced_children.update(str(child) for child in children)
            for key in COORDINATES:
                if key == coordinate:
                    expected_left = (node_box[key][0], midpoint)
                    expected_right = (midpoint, node_box[key][1])
                else:
                    expected_left = expected_right = node_box[key]
                if left_box[key] != expected_left or right_box[key] != expected_right:
                    failures.append(f"{node_id}: child union mismatch in {key}")
        elif classification in {"ENERGY_EXCLUDED", "RETURN_EXCLUDED"}:
            terminal += 1
            computed_terminal_counts[classification] += 1
            raw_path = output / str(node["raw_file"])
            checks += 3
            if not raw_path.is_file():
                failures.append(f"{node_id}: raw transcript missing")
                continue
            raw = raw_path.read_text(encoding="utf-8")
            status = extract_scalar(raw, "status")
            raw_bits = int(extract_scalar(raw, "precision_bits"))
            if status != classification or int(node.get("returncode", -1)) != 0:
                failures.append(f"{node_id}: status/returncode mismatch")
            if raw_bits != int(tree["precision_bits"]) or raw_bits != int(node["precision_bits"]):
                failures.append(f"{node_id}: raw/tree/node precision mismatch")
            raw_qplus = extract_intervals(raw, "qplus_input", 1)[0]
            raw_epsilon = extract_intervals(raw, "epsilon", 1)[0]
            raw_reduced = extract_intervals(raw, "reduced_box", 3)
            requested_epsilon = interval(node["epsilon"])
            checks += 4
            if not subset(node_box["q_fast"], raw_qplus):
                failures.append(f"{node_id}: printed qplus does not enclose requested tree box")
            if not subset(requested_epsilon, raw_epsilon):
                failures.append(f"{node_id}: printed epsilon does not enclose requested slab")
            for key, printed in zip(("q_slow", "p_slow", "period"), raw_reduced, strict=True):
                if not subset(node_box[key], printed):
                    failures.append(f"{node_id}: printed {key} does not enclose requested tree box")
            energy_ok, energy_checks, energy_failures = verify_energy_steps(raw, status)
            checks += energy_checks
            failures.extend(f"{node_id}: {message}" for message in energy_failures)
            if not energy_ok:
                failures.append(f"{node_id}: energy proof replay failed")
            if classification == "RETURN_EXCLUDED":
                return_ok, return_checks, return_failures = verify_return_exclusion(raw)
                checks += return_checks
                failures.extend(f"{node_id}: {message}" for message in return_failures)
                if not return_ok:
                    failures.append(f"{node_id}: return proof replay failed")
        else:
            if classification in computed_terminal_counts:
                computed_terminal_counts[classification] += 1
            failures.append(f"{node_id}: non-licensing terminal {classification}")

    checks += 4
    checks += 5
    nonroots = set(by_id) - root_ids
    if referenced_children != nonroots:
        failures.append("tree has orphan, duplicate-root, or unreachable nodes")
    if int(tree.get("max_depth", -1)) != 40 or int(tree.get("max_nodes", -1)) != 20_000:
        failures.append("tree resource limits differ from frozen production limits")
    if max(int(node["depth"]) for node in nodes) > 40:
        failures.append("tree exceeds frozen depth")
    evaluated_count = sum("evaluator_status" in node for node in nodes)
    if (
        evaluated_count != int(tree["evaluated_node_count"])
        or evaluated_count != len(nodes)
        or evaluated_count > 20_000
    ):
        failures.append("evaluated-node accounting/budget mismatch")
    if int(tree["stored_node_count"]) != len(nodes):
        failures.append("stored-node count mismatch")
    if terminal != sum(int(tree["terminal_counts"][key]) for key in ("ENERGY_EXCLUDED", "RETURN_EXCLUDED")):
        failures.append("terminal counts disagree with nodes")
    for key, value in computed_terminal_counts.items():
        checks += 1
        if int(tree["terminal_counts"].get(key, -1)) != value:
            failures.append(f"terminal count mismatch for {key}")
    if tree["terminal_counts"]["ROOT_CANDIDATE"] != 0:
        failures.append("root candidate present")
    if tree["terminal_counts"]["INVALID"] != 0 or tree["terminal_counts"]["UNRESOLVED"] != 0:
        failures.append("invalid/unresolved leaf present")
    if not tree["complete"]:
        failures.append("tree does not claim complete")
    stats = {
        "precision_bits": tree["precision_bits"],
        "slab_id": tree["slab_id"],
        "node_count": len(nodes),
        "terminal_count": terminal,
        "terminal_counts": computed_terminal_counts,
        "checks": checks,
        "failures": len(failures),
    }
    return not failures, checks, failures, stats


def resolve_manifest_path(output: Path, key: str) -> Path:
    candidate = Path(key)
    if candidate.is_absolute():
        return candidate
    root_candidate = ROOT / candidate
    if root_candidate.exists():
        return root_candidate
    return output / candidate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=ROOT / "results/r401_val_l2_s0_local_complement")
    args = parser.parse_args()
    output = args.input.resolve()
    summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    planned = {record["slab_id"]: record for record in plan["slabs"]}

    failures: list[str] = []
    checks = 0
    stats: list[dict[str, Any]] = []
    l1_ok, l1_checks, l1_failures, l1_result = verify_l1_protected_boxes(planned)
    checks += l1_checks
    failures.extend(l1_failures)
    if not l1_ok:
        failures.append("accepted L1 protected-box replay failed")
    expected_pairs = {(bits, slab) for bits in (128, 256) for slab in REPRESENTATIVE_SLABS}
    actual_pairs: set[tuple[int, str]] = set()
    tree_paths = sorted((output / "trees").glob("*/*.json"))
    pair_counts: dict[tuple[int, str], int] = {}
    for tree_path in tree_paths:
        tree_payload = json.loads(tree_path.read_text(encoding="utf-8"))
        pair = (int(tree_payload["precision_bits"]), str(tree_payload["slab_id"]))
        actual_pairs.add(pair)
        pair_counts[pair] = pair_counts.get(pair, 0) + 1
        ok, tree_checks, tree_failures, tree_stats = verify_tree(
            output, tree_path, planned[pair[1]]
        )
        checks += tree_checks
        stats.append(tree_stats)
        failures.extend(f"{pair}: {message}" for message in tree_failures)
        if not ok:
            failures.append(f"{pair}: tree replay failed")
    checks += 12
    if len(tree_paths) != 6 or any(count != 1 for count in pair_counts.values()):
        failures.append("expected exactly one tree file for each of six pairs")
    if actual_pairs != expected_pairs:
        failures.append(f"tree matrix mismatch: {actual_pairs}")
    if summary.get("protocol_id") != "R401-VAL-L2-S0" or manifest.get("protocol_id") != "R401-VAL-L2-S0":
        failures.append("summary/manifest protocol ID mismatch")
    if set(summary.get("representative_slabs", [])) != set(REPRESENTATIVE_SLABS):
        failures.append("summary representative slab set mismatch")
    if set(summary.get("precisions", [])) != {128, 256}:
        failures.append("summary precision set mismatch")
    if not summary.get("production_matrix") or not summary.get("all_trees_complete"):
        failures.append("summary production/completeness gates failed")
    summary_pairs = {
        (int(item["precision_bits"]), str(item["slab_id"]))
        for item in summary.get("tree_summaries", [])
    }
    if len(summary.get("tree_summaries", [])) != 6 or summary_pairs != expected_pairs:
        failures.append("summary tree matrix mismatch")
    verified_stats = {
        (int(item["precision_bits"]), str(item["slab_id"])): item for item in stats
    }
    for item in summary.get("tree_summaries", []):
        pair = (int(item["precision_bits"]), str(item["slab_id"]))
        checks += 2
        verified = verified_stats.get(pair)
        if verified is None:
            continue
        if int(item["evaluated_node_count"]) != int(verified["node_count"]):
            failures.append(f"summary evaluated-node mismatch: {pair}")
        if item["terminal_counts"] != verified["terminal_counts"] or not item.get("complete"):
            failures.append(f"summary terminal/completeness mismatch: {pair}")
    if summary.get("producer_status") != "PASS_S0_PRODUCER":
        failures.append("producer status is not PASS_S0_PRODUCER")
    if summary.get("milestone_status") is not None:
        failures.append("producer must not assign the final milestone status")
    if summary.get("final_status") is not None:
        failures.append("final_status must remain null")
    if manifest.get("producer_status") != "PASS_S0_PRODUCER" or manifest.get("milestone_status") is not None:
        failures.append("manifest producer/milestone status mismatch")

    for key, expected_hash in manifest["files"].items():
        path = resolve_manifest_path(output, key)
        checks += 1
        if not path.is_file() or sha256(path) != expected_hash:
            failures.append(f"manifest mismatch: {key}")
    for key, expected_hash in summary["input_hashes"].items():
        path = ROOT / key
        checks += 1
        if not path.is_file() or sha256(path) != expected_hash:
            failures.append(f"input hash mismatch: {key}")

    passed = not failures
    payload = {
        "protocol_id": "R401-VAL-L2-S0",
        "status": "PASS_INDEPENDENT_CHECKER" if passed else "FAIL_INDEPENDENT_CHECKER",
        "milestone_status": "PASS_IMPLEMENTATION_SMOKE" if passed else None,
        "final_status": None,
        "checker_scope": (
            "exact-decimal tree/energy-contraction/separation replay; no second ODE integration"
        ),
        "aggregate_checks": checks,
        "failure_count": len(failures),
        "failures": failures,
        "tree_stats": stats,
        "l1_protected_box_replay": l1_result,
        "checker_source_sha256": sha256(Path(__file__).resolve()),
    }
    checker_path = output / "independent_checker.json"
    checker_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report = [
        "# R401-VAL-L2-S0 independent checker",
        "",
        f"Status: **{payload['status']}**.",
        "",
        f"- exact-decimal checks: `{checks}`;",
        f"- failures: `{len(failures)}`;",
        f"- trees replayed: `{len(stats)}`;",
        "- this checker did not rerun the CAPD ODE integration.",
        "",
        "A pass confirms only the representative implementation smoke and does",
        "not turn the three slabs into an all-parameter complement theorem.",
        "",
    ]
    (output / "INDEPENDENT_CHECKER_REPORT.md").write_text("\n".join(report), encoding="utf-8")
    postcheck = {
        "protocol_id": "R401-VAL-L2-S0",
        "producer_status": summary.get("producer_status"),
        "checker_status": payload["status"],
        "milestone_status": payload["milestone_status"],
        "final_status": None,
        "claim_boundary": (
            "representative local-complement implementation smoke on S000/S025/S050 only"
        ),
        "files": {
            str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path): sha256(path)
            for path in (
                output / "summary.json",
                output / "manifest.json",
                checker_path,
                output / "INDEPENDENT_CHECKER_REPORT.md",
                Path(__file__).resolve(),
                PROTOCOL,
                FREEZE,
            )
        },
    }
    (output / "POSTCHECK_STATUS.json").write_text(
        json.dumps(postcheck, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({"status": payload["status"], "checks": checks, "failures": len(failures)}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
