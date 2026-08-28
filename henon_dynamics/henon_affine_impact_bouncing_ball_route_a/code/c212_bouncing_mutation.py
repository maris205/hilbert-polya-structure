#!/usr/bin/env python3
"""Hostile semantic and hash attacks against the C212 ledger."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c212_bouncing_evidence.json"
CHECKER = ROOT / "code/c212_bouncing_checker.py"


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
        ("iterate", ["cases", 0, "u_sequence_n0_to_n8", 2], "999"),
        ("time", ["cases", 1, "cumulative_time_n0_to_n8", 3], "0"),
        ("roof", ["cases", 2, "flight_roof_n0_to_n7", 0], "0"),
        ("fixed", ["cases", 0, "fixed_speed"], "0"),
        ("zeno", ["cases", 3, "regime"], "sticking_edge"),
        ("r_zero_zeno", ["cases", 5, "regime"], "zeno_contraction"),
        ("zeta_domain", ["cases", 3, "zeta", "physical_event_map_series"], "1/(1-z)"),
        ("closed_series", ["cases", 3, "zeta", "closed_affine_series"], "1"),
        ("multiplier", ["cases", 0, "event_multiplier"], "1"),
        ("route", ["route_a", "overall"], "PASS"),
        ("route_b", ["route_a", "route_b_invocation_allowed"], True),
        ("scope", ["scope_flags", "claims_euler_factors"], True),
        ("unknown", ["unexpected_key"], 1),
        ("stale", ["payload_sha256"], "0" * 64),
    ]
    caught = []
    with tempfile.TemporaryDirectory(prefix="c212-mut-") as directory:
        for index, (name, path, value) in enumerate(attacks):
            data = altered(base, path, value)
            if name != "stale":
                reseal(data)
            target = Path(directory) / ("mutation-" + str(index) + ".json")
            target.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(target)],
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert result.returncode != 0, name
            caught.append(name)
    print("C212 hostile mutations: PASS " + str(len(caught)) + "/" + str(len(attacks)))
    print("repaired_hash=" + str(len(attacks) - 1) + " stale_hash=1; caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
