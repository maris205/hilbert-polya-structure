#!/usr/bin/env python3
"""Fail-closed hostile mutations for the C64 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c64_mark_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c64_mark_checker.py"


def changed(source: dict, path: list[object], value: object) -> dict:
    out = deepcopy(source)
    node = out
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return out


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "status": changed(original, ["status"], "RELEASED"),
        "scope": changed(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "source": changed(original, ["authority", "c63"], "0" * 64),
        "matrix": changed(original, ["mark_matrix", 1, 1], 5),
        "matrix_hash": changed(original, ["matrix_sha256"], "0" * 64),
        "determinant": changed(original, ["determinant"], 0),
        "rank": changed(original, ["rank_over_Q"], 15),
        "relation": changed(original, ["r4_vector", 1], 0),
        "mark": changed(original, ["r4_mark_vector", 1], 0),
        "claim_scope": changed(original, ["claims", "full_burnside_ring_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c64-mutations-") as tmp:
        for name, doc in mutations.items():
            path = Path(tmp) / f"{name}.json"
            path.write_bytes((json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)], cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status":"PASS", "mutations_rejected":len(rejected), "names":sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
