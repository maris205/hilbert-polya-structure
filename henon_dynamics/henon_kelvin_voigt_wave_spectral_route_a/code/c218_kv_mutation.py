#!/usr/bin/env python3
"""Hostile semantic and hash mutations against C218 evidence."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c218_kv_evidence.json"
CHECKER = ROOT / "code/c218_kv_checker.py"


def reseal(data: dict) -> None:
    data.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(
        json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


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
        ("root", ["regression", "cases", 0, "modes", 0, "lambda_plus", "re"], "99.0"),
        ("regime", ["regression", "cases", 3, "modes", 0, "regime"], "underdamped"),
        ("gap", ["regression", "cases", 1, "spectral_gap"], "99.0"),
        ("asymptotic", ["regression", "cases", 4, "asymptotics", 0, "slow_minus_limit"], "0.0"),
        ("route", ["route_a", "overall"], "PASS"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope", ["scope_literal"], "TARGET_LOCAL_FACTORS"),
        ("flag", ["scope_flags", "claims_euler_factors"], True),
        ("unknown", ["unexpected_key"], 1),
        ("stale", ["payload_sha256"], "0"*64),
        ("source", ["source_commit"], "0"*40),
    ]
    caught = []
    with tempfile.TemporaryDirectory(prefix="c218-mut-") as directory:
        for idx, (name, path, value) in enumerate(attacks):
            data = altered(base, path, value)
            if name != "stale":
                reseal(data)
            target = Path(directory) / f"mutation-{idx}.json"
            target.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(target)],
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert result.returncode != 0, name
            caught.append(name)
    print(f"C218 hostile mutations: PASS {len(caught)}/{len(attacks)}")
    print(f"repaired_hash={len(attacks)-2} stale_hash=1; caught={','.join(caught)}")


if __name__ == "__main__":
    main()
