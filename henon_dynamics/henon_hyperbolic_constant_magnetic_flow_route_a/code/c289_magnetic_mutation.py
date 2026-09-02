#!/usr/bin/env python3
"""Repaired-hash, structural, duplicate-key, and stale-hash attacks for C289."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c289_magnetic_evidence.json"
CHECKER = ROOT / "code/c289_magnetic_checker.py"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C289/2026-09-02.yaml"


def phash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, dict]] = []
    def add(label, edit):
        item = copy.deepcopy(original); edit(item); item["payload_sha256"] = phash(item); attacks.append((label, item))
    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("schema", lambda d: d.__setitem__("schema", "hcs-c289-v2"))
    add("source", lambda d: d.__setitem__("source_commit", "0"*40))
    add("date", lambda d: d.__setitem__("evaluation_date", "2026-09-03"))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 0))
    add("scope", lambda d: d.__setitem__("scope_literal", "OPEN"))
    add("evaluator", lambda d: d["evaluator"].__setitem__("version", "9"))
    add("model", lambda d: d["model"].__setitem__("equation", "wrong sign"))
    add("theorem_circle", lambda d: d["theorem_contract"].__setitem__("circle", "wrong period"))
    add("theorem_critical", lambda d: d["theorem_contract"].__setitem__("critical", "stable closed orbit"))
    add("proof_period", lambda d: d["proof_contract"].__setitem__("period", "asserted"))
    add("smaller_base_return", lambda d: d["proof_contract"].__setitem__("circle_primitivity", "the full frame returns but a smaller basepoint return is not excluded"))
    add("critical_closed", lambda d: d["proof_contract"].__setitem__("critical_basepoint", "the frame is nonidentity but the base point may close"))
    add("proof_finite", lambda d: d["proof_contract"].__setitem__("finite_role", "finite cells prove all parameters"))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("a4_upgrade", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_VALIDATED"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("route_b_integer", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("flag", lambda d: d["scope_flags"].__setitem__("root_numbers", True))
    add("classification", lambda d: d["orbit_cells"][0].__setitem__("orbit_type", "horocycle"))
    add("delta", lambda d: d["orbit_cells"][0].__setitem__("discriminant", "0"))
    add("period", lambda d: d["orbit_cells"][0].__setitem__("period_over_2pi_squared", "1"))
    add("orientation", lambda d: d["orbit_cells"][0].__setitem__("orientation", 0))
    add("shape", lambda d: d["orbit_cells"][0].__setitem__("shape_tanh", "1"))
    add("duplicate_row", lambda d: d["orbit_cells"].__setitem__(-1, copy.deepcopy(d["orbit_cells"][0])))
    add("drop_row", lambda d: d["orbit_cells"].pop())
    add("boundary", lambda d: d["boundary_cells"][0].__setitem__("conclusion", "moving"))
    add("reference", lambda d: d["references"][0].__setitem__("identifier", "ghost"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(0, "original theorem"))
    add("unknown_top", lambda d: d.__setitem__("extra", 1))
    add("missing_top", lambda d: d.pop("proof_contract"))
    add("unknown_row", lambda d: d["orbit_cells"][0].__setitem__("extra", 1))
    add("wrong_type", lambda d: d.__setitem__("fixed_epoch", "1788307200"))

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    passed = 0
    with tempfile.TemporaryDirectory(prefix="c289-mutation-") as tmp:
        for label, item in attacks:
            p = Path(tmp)/f"{label}.json"; p.write_text(json.dumps(item, sort_keys=True, indent=2)+"\n")
            r = subprocess.run([sys.executable, "-B", str(CHECKER), str(p)], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert r.returncode != 0, label; passed += 1
        raw = EVIDENCE.read_text(); marker = '  "candidate_id": "HCS-C289",\n'; assert raw.count(marker) == 1
        p = Path(tmp)/"raw-duplicate.json"; p.write_text(raw.replace(marker, marker+marker, 1))
        assert subprocess.run([sys.executable, "-B", str(CHECKER), str(p)], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0; passed += 1
        stale = copy.deepcopy(original); stale["candidate_id"] = "HCS-C000"
        p = Path(tmp)/"stale.json"; p.write_text(json.dumps(stale, sort_keys=True, indent=2)+"\n")
        assert subprocess.run([sys.executable, "-B", str(CHECKER), str(p)], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0; passed += 1

        yaml_original = yaml.safe_load(YAML_PATH.read_text())
        yaml_attacks: list[tuple[str, dict]] = []
        def yadd(label, edit):
            item = copy.deepcopy(yaml_original); edit(item); yaml_attacks.append((label, item))
        yadd("yaml_schema", lambda d: d.__setitem__("schema", "route-a-evaluation-v9"))
        yadd("yaml_unknown", lambda d: d.__setitem__("unexpected", True))
        yadd("yaml_missing", lambda d: d.pop("a2"))
        yadd("yaml_tuple", lambda d: d["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION"))
        yadd("yaml_route_b", lambda d: d.__setitem__("route_b_invocation_allowed", True))
        yadd("yaml_cutoff", lambda d: d.__setitem__("orbit_cutoff", 1000))
        for label, item in yaml_attacks:
            path = Path(tmp)/f"{label}.yaml"
            path.write_text(yaml.safe_dump(item, sort_keys=False))
            result = subprocess.run([sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--yaml", str(path)], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert result.returncode != 0, label
            passed += 1
        yaml_raw = YAML_PATH.read_text(); yaml_marker = "candidate_id: HCS-C289\n"; assert yaml_raw.count(yaml_marker) == 1
        yaml_path = Path(tmp)/"yaml_raw_duplicate.yaml"; yaml_path.write_text(yaml_raw.replace(yaml_marker, yaml_marker+yaml_marker, 1))
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--yaml", str(yaml_path)], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        assert result.returncode != 0, "yaml raw duplicate"
        passed += 1
    total = len(attacks)+2+len(yaml_attacks)+1
    print(f"C289 hostile mutation audit: PASS {passed}/{total} (repaired-hash semantic/structural, critical/base-return, exact YAML, raw duplicate-key, stale-hash)")


if __name__ == "__main__":
    main()
