#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C276."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c276_random_mapping_evidence.json"
CHECKER = ROOT / "code/c276_random_mapping_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    data["payload_sha256"] = hashlib.sha256(raw.encode()).hexdigest()


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(label, change) -> None:
        candidate = copy.deepcopy(original)
        change(candidate)
        rehash(candidate)
        mutations.append((label, candidate))

    add("unknown_key", lambda d: d.__setitem__("unregistered_claim", True))
    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C275"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 1788220801))
    add("scope", lambda d: d.__setitem__("scope_literal", "UNSCOPED"))
    add("evaluator", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FORMAL_HINT"))
    add("verdict", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_PARTIAL"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("maps", lambda d: d["regression"]["enumeration"][0].__setitem__("maps", 2))
    add("joint_count", lambda d: d["regression"]["enumeration"][0]["joint_cells"][0].__setitem__("count", 0))
    add("joint_formula", lambda d: d["regression"]["enumeration"][1]["joint_cells"][0].__setitem__("formula_count", 99))
    add("tail_count", lambda d: d["regression"]["enumeration"][0]["tail_cycle_cells"][0].__setitem__("count", 0))
    add("tail_index", lambda d: d["regression"]["enumeration"][1]["tail_cycle_cells"][0].__setitem__("tail", 1))
    add("cycle_total", lambda d: d["regression"]["enumeration"][0]["cycle_length_cells"][0].__setitem__("aggregate_cycle_count", 0))
    add("cyclic_probability", lambda d: d["regression"]["formula_atlas"][0]["cyclic_point_probabilities"].__setitem__(0, "0/1"))
    add("survival", lambda d: d["regression"]["formula_atlas"][1]["marked_collision_survival"].__setitem__(1, "1/1"))
    add("cycle_mean", lambda d: d["regression"]["formula_atlas"][2]["expected_cycles_by_length"].__setitem__(0, "2/1"))
    add("scaling_mass", lambda d: d["regression"]["cyclic_scaling_receipts"][0].__setitem__("mass", "1/1"))
    add("joint_density", lambda d: d["regression"]["joint_scaling_receipts"][0].__setitem__("joint_density", "0.0"))
    add("count_ledger", lambda d: d["regression"]["counts"].__setitem__("enumerated_maps", 1))
    add("doi", lambda d: d["sources"][0].__setitem__("doi", "10.0000/fake"))
    add("source_year", lambda d: d["sources"][1].__setitem__("year", 1991))

    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c276-mutations-") as directory:
        for index, (label, data) in enumerate(mutations):
            path = Path(directory) / f"{index:02d}-{label}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), str(path)],
                env=environment,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            assert process.returncode != 0, label
            rejected += 1
    print(f"C276 hostile mutations: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
