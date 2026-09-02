#!/usr/bin/env python3
"""Hostile semantic, structural, raw-JSON, and stale-hash audit for C288."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c288_delta_evidence.json"
CHECKER = ROOT / "code/c288_delta_checker.py"


def phash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, dict]] = []

    def add(label, mutation) -> None:
        item = copy.deepcopy(original)
        mutation(item)
        item["payload_sha256"] = phash(item)
        attacks.append((label, item))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C287"))
    add("schema", lambda d: d.__setitem__("schema", "hcs-c288-delta-point-interaction-v2"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 0))
    add("scope", lambda d: d.__setitem__("scope_literal", "OPEN"))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS_ANALYTIC"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_VALIDATED"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("flag", lambda d: d["scope_flags"].__setitem__("root_numbers", True))
    add("interface", lambda d: d["model"].__setitem__("interface", "wrong sign"))
    add("theorem_resolvent", lambda d: d["theorem_contract"].__setitem__("resolvent", "unverified resolvent"))
    add("theorem_heat", lambda d: d["theorem_contract"].__setitem__("heat", "unverified heat formula"))
    add("proof_completeness", lambda d: d["proof_contract"].__setitem__("completeness", "singular continuum omitted"))
    add("regular_value", lambda d: d["resolvent_cells"][0].__setitem__("image_coefficient", "0"))
    add("pole", lambda d: d["pole_cells"][0].__setitem__("pole", False))
    add("scatter", lambda d: d["scattering_cells"][0].__setitem__("reflection_probability", "0"))
    add("bound", lambda d: d["bound_state_cells"][0].__setitem__("energy", "0"))
    add("heat_kernel", lambda d: d["heat_cells"][0].__setitem__("kernel", "0"))
    add("heat_trace", lambda d: d["heat_cells"][0].__setitem__("relative_trace", "0"))
    add("reference", lambda d: d["references"][0].__setitem__("identifier", "ghost"))

    def duplicate_resolvent(d: dict) -> None:
        d["resolvent_cells"][-1] = copy.deepcopy(d["resolvent_cells"][0])

    def drop_resolvent(d: dict) -> None:
        d["resolvent_cells"].pop()

    def duplicate_heat(d: dict) -> None:
        d["heat_cells"][-1] = copy.deepcopy(d["heat_cells"][0])

    def drop_heat(d: dict) -> None:
        d["heat_cells"].pop()

    add("duplicate_resolvent", duplicate_resolvent)
    add("drop_resolvent", drop_resolvent)
    add("duplicate_heat", duplicate_heat)
    add("drop_heat", drop_heat)
    add("unknown_top_key", lambda d: d.__setitem__("unexpected_field", "forbidden"))
    add("missing_top_key", lambda d: d.pop("nonclaims"))
    add("type_confusion", lambda d: d.__setitem__("fixed_epoch", "1788307200"))
    add("unknown_row_key", lambda d: d["heat_cells"][0].__setitem__("copied_formula", True))

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TZ"] = "UTC"
    passed = 0
    with tempfile.TemporaryDirectory(prefix="c288_mutation_") as tmp:
        directory = Path(tmp)
        for label, data in attacks:
            path = directory / f"{label}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run(
                [sys.executable, "-B", str(CHECKER), str(path)],
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            assert result.returncode != 0, label
            passed += 1

        # Python's ordinary JSON loader silently keeps the last duplicate;
        # the strict checker must reject the raw document before hashing.
        raw = EVIDENCE.read_text()
        marker = '  "candidate_id": "HCS-C288",\n'
        assert raw.count(marker) == 1
        duplicate_raw = raw.replace(marker, marker + marker, 1)
        raw_path = directory / "raw_duplicate_key.json"
        raw_path.write_text(duplicate_raw)
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(raw_path)],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        assert result.returncode != 0, "raw duplicate key"
        passed += 1

        stale = copy.deepcopy(original)
        stale["candidate_id"] = "HCS-C000"
        stale_path = directory / "stale_hash.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(stale_path)],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        assert result.returncode != 0, "stale hash"
        passed += 1

    total = len(attacks) + 2
    print(
        f"C288 hostile mutation audit: PASS {passed}/{total} "
        "(repaired-hash semantic/structural, raw duplicate-key, and stale-hash attacks)"
    )


if __name__ == "__main__":
    main()
