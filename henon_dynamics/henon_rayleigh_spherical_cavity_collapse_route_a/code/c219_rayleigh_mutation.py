#!/usr/bin/env python3
"""Hostile semantic and hash mutations against the C219 receipt."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c219_rayleigh_evidence.json"
CHECKER = ROOT / "code/c219_rayleigh_checker.py"


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
        ("beta_constant", ["theorem", "collapse_constant"], "0.0"),
        ("pressure", ["regression", "cases", 0, "pressure"], "2"),
        ("clock", ["regression", "cases", 0, "collapse_time"], "99.0"),
        ("terminal", ["regression", "cases", 1, "terminal_coefficient"], "0.0"),
        ("beta", ["regression", "cases", 2, "beta_clock"], "1.0"),
        ("regime", ["regression", "cases", 5, "regime"], "collapse"),
        ("boundary", ["regression", "cases", 10, "regime"], "collapse"),
        ("route", ["route_a", "overall"], "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope", ["scope_literal"], "TARGET_LOCAL_FACTORS"),
        ("flag", ["scope_flags", "claims_euler_factors"], True),
        ("source", ["source_commit"], "0" * 40),
        ("unknown_nested", ["theorem", "unexpected_key"], 1),
        ("unknown", ["unexpected_key"], 1),
        ("stale", ["payload_sha256"], "0" * 64),
    ]
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c219-mut-") as directory:
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
    print(f"C219 hostile mutations: PASS {len(caught)}/{len(attacks)}")
    print(f"repaired_hash={len(attacks)-1} stale_hash=1; caught={','.join(caught)}")


if __name__ == "__main__":
    main()
