#!/usr/bin/env python3
"""Adversarial repaired-hash and stale-hash mutations for HCS-C176."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c176_sandpile_evidence.json"
CHECKER = ROOT / "code/c176_sandpile_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c176-mutation-") as tmp:
        path = Path(tmp) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, mutate) -> None:
        item = deepcopy(base)
        mutate(item)
        rehash(item)
        mutations.append((name, item))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("source_commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("clock", lambda d: d["source_lock"].__setitem__("clock", "topple without addition"))
    add("graph_code", lambda d: d["finite_replay"]["graph_rows"][5].__setitem__("canonical_upper_triangle_code", "BROKEN"))
    add("determinant", lambda d: d["finite_replay"]["sink_rows"][20].__setitem__("determinant_D", 999))
    add("recurrent_count", lambda d: d["finite_replay"]["sink_rows"][30].__setitem__("recurrent_state_count", 999))
    add("order", lambda d: d["finite_replay"]["translation_rows"][100].__setitem__("order_L", 999))
    add("adjugate", lambda d: d["finite_replay"]["translation_rows"][200]["adjugate_times_b"].__setitem__(0, 999))
    add("fixed", lambda d: d["finite_replay"]["translation_rows"][300]["fixed_counts"][0].__setitem__("fixed_count_formula", 999))
    add("full_injective", lambda d: d["finite_replay"]["translation_rows"][400].__setitem__("full_stable_injective", not d["finite_replay"]["translation_rows"][400]["full_stable_injective"]))
    add("A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("A1", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("A4", lambda d: d["route_a"].__setitem__("A4_qualification", "POST_HOC"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("target_flag", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))

    repaired_rejections = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired_rejections += 1

    stale = deepcopy(base)
    stale["finite_replay"]["translation_rows"][0]["order_L"] = 123
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({
        "status": "C176_MUTATION_PASS",
        "repaired_hash_rejections": repaired_rejections,
        "stale_hash_rejections": 1,
        "total_rejections": repaired_rejections + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
