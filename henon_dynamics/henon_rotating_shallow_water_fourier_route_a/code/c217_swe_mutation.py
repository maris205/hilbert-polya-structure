#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for C217."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c217_swe_evidence.json"
CHECKER = ROOT / "code/c217_swe_checker.py"


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
        ("omega", ["regression", "cases", 0, "modes", 1, "omega"], "99.0"),
        ("rho", ["regression", "cases", 1, "modes", 2, "rho"], 999),
        ("projector", ["regression", "cases", 2, "modes", 3, "projector_residual"], "99.0"),
        ("shell", ["regression", "cases", 0, "shell_counts", 4, "formula"], 99),
        ("route", ["route_a", "overall"], "PASS"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope", ["scope_literal"], "TARGET_LOCAL_FACTORS"),
        ("flag", ["scope_flags", "claims_euler_factors"], True),
        ("unknown", ["unexpected_key"], 1),
        ("stale", ["payload_sha256"], "0"*64),
        ("source", ["source_commit"], "0"*40),
    ]
    caught = []
    with tempfile.TemporaryDirectory(prefix="c217-mut-") as directory:
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
    print(f"C217 hostile mutations: PASS {len(caught)}/{len(attacks)}")
    print(f"repaired_hash={len(attacks)-2} stale_hash=1; caught={','.join(caught)}")


if __name__ == "__main__":
    main()
