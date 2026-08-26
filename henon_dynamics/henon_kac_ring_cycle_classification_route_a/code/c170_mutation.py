#!/usr/bin/env python3
"""Adversarial repaired-hash and stale-hash mutations for HCS-C170."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c170_kac_ring_evidence.json"
CHECKER = ROOT / "code/c170_kac_ring_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c170-mutation-") as tmp:
        path = Path(tmp) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        return subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True).returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name: str, mutate) -> None:
        item = deepcopy(base)
        mutate(item)
        rehash(item)
        mutations.append((name, item))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("family", lambda d: d["source_lock"].__setitem__("family", "N=2 only"))
    add("N-step", lambda d: d["classification_theorem"].__setitem__("N_step_law", "false"))
    add("cycle_length", lambda d: d["finite_replay"]["class_rows"][4].__setitem__("cycle_length_L", 99))
    add("cycle_count", lambda d: d["finite_replay"]["class_rows"][7].__setitem__("cycle_count_c", 99))
    add("fixed", lambda d: d["finite_replay"]["class_rows"][10]["fixed_rows"][0].__setitem__("fixed_points", 99))
    add("zeta", lambda d: d["finite_replay"]["class_rows"][20].__setitem__("zeta", "1"))
    add("digest", lambda d: d["finite_replay"]["brute_rows"][5].__setitem__("configuration_signature_sha256", "0" * 64))
    add("brute_count", lambda d: d["finite_replay"]["brute_rows"][2].__setitem__("marker_configurations", 0))
    add("reversor", lambda d: d["gauge_and_reversal_theorem"].__setitem__("reversor", "false"))
    add("A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("A1", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("A4", lambda d: d["route_a"].__setitem__("A4_qualification", "POST_HOC"))
    add("RouteB", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("target", lambda d: d["scope_flags"].__setitem__("used_target_zero_table", True))

    count = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        count += 1
    stale = deepcopy(base)
    stale["finite_replay"]["class_rows"][0]["cycle_length_L"] = 7
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({"status": "C170_MUTATION_PASS", "repaired_hash_rejections": count, "stale_hash_rejections": 1, "total_rejections": count + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
