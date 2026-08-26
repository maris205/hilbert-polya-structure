#!/usr/bin/env python3
"""Adversarial repaired-hash and stale-hash mutations for HCS-C175."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c175_rule184_evidence.json"
CHECKER = ROOT / "code/c175_rule184_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c175-mutation-") as tmp:
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
    add("clock", lambda d: d["source_lock"].__setitem__("clock", "asynchronous update"))
    add("core_count", lambda d: d["finite_replay"]["sector_rows"][30].__setitem__("periodic_core_count", 999))
    add("entry_bound", lambda d: d["finite_replay"]["sector_rows"][40].__setitem__("proved_entry_bound_m_squared", 0))
    add("bijection", lambda d: d["finite_replay"]["sector_rows"][50].__setitem__("full_sector_bijective", True))
    add("fixed_formula", lambda d: d["finite_replay"]["fixed_rows"][300].__setitem__("fixed_count_formula", 999))
    add("fixed_enumerated", lambda d: d["finite_replay"]["fixed_rows"][500].__setitem__("fixed_count_enumerated", 999))
    add("primitive", lambda d: d["finite_replay"]["primitive_rows"][100].__setitem__("primitive_cycles", 999))
    add("A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("A1", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("A4", lambda d: d["route_a"].__setitem__("A4_qualification", "FULL_SECTOR_UNITARY"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("target_flag", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))
    add("nonclaim", lambda d: d.__setitem__("nonclaims", []))

    repaired_rejections = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired_rejections += 1

    stale = deepcopy(base)
    stale["finite_replay"]["fixed_rows"][0]["fixed_count_formula"] = 123
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({
        "status": "C175_MUTATION_PASS",
        "repaired_hash_rejections": repaired_rejections,
        "stale_hash_rejections": 1,
        "total_rejections": repaired_rejections + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
