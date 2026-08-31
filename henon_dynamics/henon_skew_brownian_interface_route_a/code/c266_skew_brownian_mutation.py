#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for HCS-C266."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c266_skew_brownian_evidence.json"
CHECKER = ROOT / "code/c266_skew_brownian_checker.py"


def ph(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def repaired(data):
    data["payload_sha256"] = ph(data)
    return data


def main():
    original = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name, fn, repair=True):
        mutations.append((name, fn, repair))

    add("stale_hash", lambda d: d["regression"]["kernel_rows"][0].__setitem__("density", "0"), False)
    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 0))
    add("scope", lambda d: d.__setitem__("scope_literal", "BAD"))
    add("evaluator", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION"))
    add("verdict", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_PASS"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("local_time", lambda d: d["frozen_model"].__setitem__("local_time", "right local time"))
    add("interface", lambda d: d["frozen_model"].__setitem__("generator_interface", "(1-p)f'(0+)=p f'(0-)"))
    add("measure", lambda d: d["frozen_model"].__setitem__("density_reference_measure", "continuous Lebesgue density"))
    add("kernel", lambda d: d["regression"]["kernel_rows"][7].__setitem__("density", "0"))
    add("exit_side", lambda d: d["regression"]["exit_rows"][17].__setitem__("right_probability", "0/1"))
    add("occupation", lambda d: d["regression"]["occupation_rows"][0].__setitem__("mean", "1/2"))
    passed = 0
    with tempfile.TemporaryDirectory(prefix="c266-mutation-") as tmp:
        for index, (name, fn, repair) in enumerate(mutations):
            data = copy.deepcopy(original)
            fn(data)
            if repair:
                repaired(data)
            path = Path(tmp) / f"{index:02d}-{name}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, "-B", str(CHECKER), str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert result.returncode != 0, name
            passed += 1
    print(f"C266 hostile mutation audit: PASS {passed}/{len(mutations)}")


if __name__ == "__main__":
    main()
