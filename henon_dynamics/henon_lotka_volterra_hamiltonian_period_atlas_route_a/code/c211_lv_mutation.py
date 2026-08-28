#!/usr/bin/env python3
"""Hostile semantic and hash attacks against the C211 evidence ledger."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c211_lv_evidence.json"
CHECKER = ROOT / "code/c211_lv_checker.py"


def reseal(data: dict) -> None:
    data.pop("payload_sha256", None)
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = hashlib.sha256(raw).hexdigest()


def altered(base: dict, path: list[object], value: object) -> dict:
    data = copy.deepcopy(base)
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    return data


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks = [
        ("period", ["regression", "parameter_cases", 0, "levels", 0, "period"], "1.0"),
        ("area", ["regression", "parameter_cases", 1, "levels", 1, "area"], "0.0"),
        ("branch", ["regression", "parameter_cases", 2, "levels", 0, "u_minus"], "0.0"),
        ("action", ["regression", "parameter_cases", 3, "levels", 2, "action"], "99.0"),
        ("route", ["route_a", "overall"], "PASS"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope", ["scope_literal"], "TARGET_LOCAL_FACTORS"),
        ("flag", ["scope_flags", "claims_euler_factors"], True),
        ("parameter", ["regression", "parameter_cases", 0, "a"], "2"),
        ("unknown", ["unexpected_key"], 1),
        ("stale", ["payload_sha256"], "0" * 64),
        ("source", ["source_commit"], "0" * 40),
    ]
    repaired = attacks[:-1]
    caught = []
    with tempfile.TemporaryDirectory(prefix="c211-mut-") as directory:
        for index, (name, path, value) in enumerate(attacks):
            data = altered(base, path, value)
            if name != "stale":
                reseal(data)
            target = Path(directory) / f"mutation-{index}.json"
            target.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(target)],
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert result.returncode != 0, name
            caught.append(name)
    print(f"C211 hostile mutations: PASS {len(caught)}/{len(attacks)}")
    print(f"repaired_hash={len(repaired)} stale_hash=1; caught={','.join(caught)}")


if __name__ == "__main__":
    main()
