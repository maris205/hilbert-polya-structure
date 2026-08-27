#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks for C198."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c198_sir_evidence.json"
CHECKER = Path(__file__).with_name("c198_sir_checker.py")


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data, path):
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    result = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)], capture_output=True)
    return result.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        lambda d: d.__setitem__("source_commit", "0"*40),
        lambda d: d.__setitem__("headline", "mutated headline"),
        lambda d: d["evaluator"].__setitem__("sha256", "0"*64),
        lambda d: d["scope_flags"].__setitem__("gives_medical_advice", True),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
        lambda d: d["route_a"].__setitem__("tuple", ["A0_FAIL"]*4+["A4_NATURAL_QUANTIZATION"]),
        lambda d: d["citations"][1].__setitem__("doi", "10.fake/branch"),
        lambda d: d["regression"]["cases"][0].__setitem__("x0", "2"),
        lambda d: d["regression"]["cases"][1].__setitem__("final_x_W0", "0.9"),
        lambda d: d["regression"]["cases"][2].__setitem__("companion_x_Wminus1", "0.5"),
        lambda d: d["regression"]["cases"][3].__setitem__("peak_y", "99"),
        lambda d: d["regression"]["physical_scalings"][0].__setitem__("susceptible_threshold_kappa", "7"),
    ]
    repaired = 0
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mutated.json"
        for mutate in mutations:
            data = deepcopy(original)
            mutate(data)
            repair(data)
            if not rejected(data, path):
                raise AssertionError("semantic mutation survived")
            repaired += 1
        stale = deepcopy(original)
        stale["regression"]["cases"][0]["peak_x"] = "123"
        if not rejected(stale, path):
            raise AssertionError("stale-hash mutation survived")
    print(json.dumps({
        "status": "C198_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
