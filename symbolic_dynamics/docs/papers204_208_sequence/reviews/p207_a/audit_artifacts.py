#!/usr/bin/env python3
"""Read-only frozen author/output audit; NOT the independent math producer.

Reads complete JSON/bytes and checks recorded artefacts, without executing
or importing any author/gate/old verifier. Its derived report is exclusively
written inside this review. Historical snapshots use their preserved bases.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import ast
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN = ROOT / "papers/207-upper-neighbor-rank-dynamics/frozen_round0"
CHECKS = 0


def check(value, context):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(context)


def digest(data):
    return sha256(data).hexdigest()


def manifest(path, base):
    checked = []
    for line in path.read_text().splitlines():
        expected, name = line.split("  ", 1)
        check(digest((base / name).read_bytes()) == expected, ("manifest", path, name))
        checked.append(name)
    check(len(checked) == len(set(checked)), ("unique manifest paths", path))
    return {"path": str(path.relative_to(FROZEN)), "entries": len(checked), "sha256": digest(path.read_bytes())}


def step(row):
    return tuple((row[i - 1] > row[i]) + (row[i + 1] > row[i]) for i in range(1, len(row) - 1))


def cone(row):
    rows = [tuple(row)]
    for _ in range(4):
        rows.append(step(rows[-1]))
    return rows


def extremes(row):
    return {i - len(row) // 2 for i in range(1, len(row) - 1)
            if row[i] < min(row[i - 1], row[i + 1]) or row[i] > max(row[i - 1], row[i + 1])}


def json_leaves(value):
    if isinstance(value, dict):
        return sum(json_leaves(v) for v in value.values())
    if isinstance(value, list):
        return sum(json_leaves(v) for v in value)
    return 1


def main():
    files = sorted(p for p in FROZEN.rglob("*") if p.is_file())
    check(len(files) == 106, "105 frozen artefacts plus freeze manifest")
    by_digest, json_inventory, source_inventory = defaultdict(list), [], []
    for path in files:
        data = path.read_bytes()
        by_digest[digest(data)].append(str(path.relative_to(FROZEN)))
        if path.suffix == ".json":
            parsed = json.loads(data)
            json_inventory.append({"path": str(path.relative_to(FROZEN)), "bytes": len(data),
                "sha256": digest(data), "all_scalar_values_traversed": json_leaves(parsed),
                "top_level_keys": sorted(parsed) if isinstance(parsed, dict) else None})
        if path.suffix == ".py":
            tree = ast.parse(data)
            imports = sorted({node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)} |
                             {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names})
            source_inventory.append({"path": str(path.relative_to(FROZEN)), "sha256": digest(data),
                                     "lines": len(data.splitlines()), "imports": imports})
    seals = [manifest(FROZEN / "SHA256SUMS", FROZEN),
             manifest(FROZEN / "author_replay/OWNED_MANIFEST.sha256", FROZEN)]
    author = json.loads((FROZEN / "CANONICAL.json").read_bytes())
    own = json.loads((HERE / "CANONICAL.json").read_bytes())
    check(author["status"] == "PASS" and author["assertions"] == 1384012, "complete author canonical census")
    check(sum(author["assertions_by_section"].values()) == author["assertions"], "author section assertion sum")
    receipts = []
    for attempt in ("initial_01", "pair_01", "export_pair_01"):
        base = FROZEN / "author_replay" / attempt
        seals.append(manifest(base / "MANIFEST.sha256", base))
        receipt = json.loads((base / "RECEIPT.json").read_bytes())
        check(receipt["status"] == "PASS", ("author receipt status", attempt))
        for command in receipt["commands"]:
            check(command["exit_code"] == 0, ("recorded exit", attempt, command["argv"]))
            for stream in ("stdout", "stderr"):
                item = command[stream]
                if isinstance(item, dict):
                    data = (base / item["path"]).read_bytes()
                    check(len(data) == item["bytes"] and digest(data) == item["sha256"], ("recorded full stream", attempt, item["path"]))
                else:
                    check((base / item).read_bytes() == b"", ("empty export comparison stream", item))
        if attempt != "export_pair_01":
            check(receipt["inputs_unchanged"], ("author stable snapshot", attempt))
            before = (base / "INPUT_PINS.before.sha256").read_bytes()
            check(before == (base / "INPUT_PINS.after.sha256").read_bytes(), ("raw before/after", attempt))
            check(len(before.decode().splitlines()) == 17, ("all 17 preserved input copies", attempt))
            manifest(base / "INPUT_PINS.before.sha256", base / "source_inputs")
            check((base / "verify.py").read_bytes() == (FROZEN / "verify.py").read_bytes(), ("author standalone source identity", attempt))
        else:
            check(receipt["new_numerical_runs"] == 0, "aliases are not new executions")
        receipts.append({"attempt": attempt, "commands": len(receipt["commands"]),
                         "mathematical_runs": len(receipt.get("numerical_outputs", [])),
                         "status": receipt["status"], "sha256": digest((base / "RECEIPT.json").read_bytes())})
    for name in ("author_replay/initial_01/run0.stdout", "author_replay/pair_01/run1.stdout",
                 "author_replay/pair_01/run2.stdout", "author_replay/run1.stdout", "author_replay/run2.stdout"):
        check((FROZEN / name).read_bytes() == (FROZEN / "CANONICAL.json").read_bytes(), ("actual complete output equality", name))
    certificate = author["local_growth_certificate"]
    exceptions = certificate["complete_inner_exception_and_extension_certificate"]
    check(len(exceptions) == 204, "all stored exceptional inner words")
    claimed = {tuple(item["inner_word"]): item for item in exceptions}
    check(len(claimed) == 204, "exceptional words unique")
    census = Counter()
    for word in product(range(3), repeat=11):
        rows = cone(word)
        if rows[2][3] == rows[4][1]:
            census["center_equal"] += 1
        elif any(extremes(rows[t]) - extremes(word) for t in range(1, 5)):
            census["inner_witness"] += 1
        else:
            census["needs_outer_letters"] += 1
            check(word in claimed, ("every real exception appears in author canonical", word))
    check(dict(census) == certificate["inner_case_counts"], "entire author's inner partition independently recomputed")
    for word, item in claimed.items():
        all_nine = item["all_nine_extensions_left_right_time_site"]
        check({tuple(v[:2]) for v in all_nine} == set(product(range(3), repeat=2)) and len(all_nine) == 9,
              ("all nine unique outer pairs", word))
        for left, right, time, site in all_nine:
            full = (left,) + word + (right,)
            rows = cone(full)
            check(1 <= time <= 4 and abs(site) <= 5 - time, ("author witness domain", full, time, site))
            check(rows[2][4] != rows[4][2], ("author witness premise", full))
            check(site in extremes(rows[time]) - extremes(full), ("every actual stored witness", full, time, site))
    for row in author["core_certificate"]["traces_n1_to_60"]:
        check(row["all_core_points"] == own["independent_overlap_core_graph"]["trace_exponents_1_to_81"][row["n"] - 1],
              ("eight-role author trace versus 81-height independent trace", row["n"]))
        check(2 * row["two_cycles"] + 1 == row["all_core_points"], ("paired core census", row["n"]))
    for original, independent in zip(author["complete_cyclic_source_target_boxes"], own["complete_cyclic_boxes"], strict=True):
        for key, other in (("n", "n"), ("image_points", "image_points"), ("core_points", "core_points"),
                           ("maximum_fibre", "maximum_fibre"), ("depth_histogram", "exact_depth_histogram"),
                           ("all_labelled_maximizers", "all_labelled_maximizers"),
                           ("target_fibre_histogram_including_empty", "fibre_size_histogram_including_empty"),
                           ("successor_index_vector_sha256", "successor_vector_sha256")):
            check(original[key] == independent[other], ("all reported box values", original["n"], key))
    for box in author["mixed_kernel_checks"]["matrix_word_boxes"]:
        rows = box["by_B_count_J_count_equality"]
        check(sum(row[-1] for row in rows) == 3 ** box["length"], ("all mixed word histogram entries", box["length"]))
        check(sum(row[-1] for row in rows if row[2]) == box["length"] + 1, ("mixed equality histogram", box["length"]))
        check(all(bool(row[2]) == (row[0] <= 1 and row[1] == 0) for row in rows), ("all mixed histogram classifications", box["length"]))
    for original, independent in zip(author["single_seed_only_checks"], own["seed_only_n4_to_64"], strict=True):
        check((original["n"], original["single_seed_hitting_time"], original["one_hole_source_hitting_time"]) ==
              (independent["n"], independent["seed_entrance"], independent["source_entrance"]), ("all seed record outputs", original["n"]))
    result = {"status": "PASS", "kind": "frozen artefact and canonical audit, separate from independent producer runs",
              "checks": CHECKS, "all_physical_frozen_files": len(files), "unique_byte_contents": len(by_digest),
              "duplicate_identity_groups": [{"sha256": key, "paths": paths} for key, paths in sorted(by_digest.items()) if len(paths) > 1],
              "complete_json_inventory": json_inventory, "complete_python_ast_inventory": source_inventory,
              "validated_nested_manifests": seals, "author_receipts": receipts,
              "all_177147_inner_words_recomputed": dict(census), "stored_outer_witnesses_actually_recomputed": 1836,
              "all_60_role_traces_crosschecked": True, "all_8_full_box_summaries_crosschecked": True,
              "author_programs_executed_or_imported": False,
              "historical_live_contract_equality_not_required": "preserved snapshot copies are the provenance inputs; mutable future indexes are not producer runtime data"}
    destination = HERE / "AUTHOR_ARTIFACT_AUDIT.json"
    with destination.open("x") as output:
        json.dump(result, output, sort_keys=True, indent=2)
        output.write("\n")
    print(json.dumps({"status": "PASS", "checks": CHECKS, "files": len(files), "unique_contents": len(by_digest),
                      "output": str(destination), "sha256": digest(destination.read_bytes())}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
