#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C273."""
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
EVIDENCE = ROOT / "results/c273_sparre_andersen_evidence.json"
CHECKER = ROOT / "code/c273_sparre_andersen_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    data["payload_sha256"] = hashlib.sha256(raw.encode()).hexdigest()


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(label, change):
        candidate = copy.deepcopy(original)
        change(candidate)
        rehash(candidate)
        mutations.append((label, candidate))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C272"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 1788134401))
    add("scope", lambda d: d.__setitem__("scope_literal", "UNSCOPED"))
    add("evaluator", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FAIL"))
    add("verdict", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_PARTIAL"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("q_2", lambda d: d["regression"]["q_rows"][2].__setitem__("q_n", "1/2"))
    add("first_3", lambda d: d["regression"]["q_rows"][3].__setitem__("first_strict_descent_n", "1/8"))
    add("conv_4", lambda d: d["regression"]["q_rows"][4].__setitem__("arcsine_convolution", "0/1"))
    add("arc_cell", lambda d: d["regression"]["arcsine_rows"][6]["cells"].__setitem__(2, "1/7"))
    add("arc_length", lambda d: d["regression"]["arcsine_rows"][5]["cells"].pop())
    add("control_history", lambda d: d["regression"]["permutation_controls"][3].__setitem__("histories", 1))
    add("control_tie", lambda d: d["regression"]["permutation_controls"][2].__setitem__("ties", 1))
    add("control_positive", lambda d: d["regression"]["permutation_controls"][4]["positive_count_histogram"].__setitem__(2, 0))
    add("control_maximum", lambda d: d["regression"]["permutation_controls"][5]["maximum_time_histogram"].__setitem__(3, 0))
    add("atomic_weak", lambda d: d["regression"]["atomic_controls"][1].__setitem__("nonnegative_survival_count", 3))
    add("atomic_ties", lambda d: d["regression"]["atomic_controls"][3].__setitem__("tied_maximum_histories", 0))
    add("scaling_mass", lambda d: d["regression"]["scaling_receipts"][0].__setitem__("mass", "1/1"))
    add("count", lambda d: d["regression"]["counts"].__setitem__("arcsine_cells", 1))
    add("doi", lambda d: d["source"].__setitem__("doi", "10.0000/fake"))
    add("year", lambda d: d["source"].__setitem__("year", 1954))

    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    accepted = 0
    with tempfile.TemporaryDirectory(prefix="c273-mutations-") as directory:
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
            accepted += 1
    print(f"C273 hostile mutations: PASS {accepted}/{len(mutations)}")


if __name__ == "__main__":
    main()
