#!/usr/bin/env python3
"""Hostile repaired-hash JSON and strict-YAML attacks for HCS-C297."""
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
EVIDENCE = ROOT / "results/c297_pt_dimer_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C297/2026-09-02.yaml"
CHECKER = ROOT / "code/c297_pt_dimer_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def encode(data: dict, repair: bool = True) -> bytes:
    if repair:
        data["payload_sha256"] = payload_hash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def rejected_json(raw: bytes) -> bool:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c297-json-mut-") as temporary:
        path = Path(temporary) / "attack.json"; path.write_bytes(raw)
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.returncode != 0


def rejected_yaml(raw: bytes) -> bool:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c297-yaml-mut-") as temporary:
        path = Path(temporary) / "attack.yaml"; path.write_bytes(raw)
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--evaluation", str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, bytes]] = []

    def add(name, mutator, repair=True):
        data = copy.deepcopy(base); mutator(data); attacks.append((name, encode(data, repair)))

    add("stale-hash-control", lambda d: d["phase_cells"][0].__setitem__("delta", 999), False)
    add("unknown-top", lambda d: d.__setitem__("alien", 1))
    add("missing-top", lambda d: d.pop("model"))
    add("obstruction-id", lambda d: d.__setitem__("obstruction_id", "HEN-O999"))
    add("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True))
    add("source-change", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("model-equation", lambda d: d["model"].__setitem__("equation", "tampered"))
    add("theorem-chamber", lambda d: d["theorem_contract"].__setitem__("exceptional", "diagonalizable"))
    add("proof-period", lambda d: d["proof_contract"].__setitem__("period", "handwave"))
    add("route-tuple", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("route-b-int", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("flag-true", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("flag-int", lambda d: d["scope_flags"].__setitem__("root_numbers", 0))
    add("drop-cell", lambda d: d["phase_cells"].pop())
    add("duplicate-cell", lambda d: d["phase_cells"].append(copy.deepcopy(d["phase_cells"][0])))
    add("delta-value", lambda d: d["phase_cells"][0].__setitem__("delta", 99))
    add("phase-value", lambda d: d["phase_cells"][0].__setitem__("phase", "exceptional"))
    add("kappa-bool", lambda d: d["phase_cells"][0].__setitem__("kappa", True))
    add("metric-signature", lambda d: d["phase_cells"][0].__setitem__("eta_signature", "positive"))
    add("period-type", lambda d: d["phase_cells"][50].__setitem__("projective_period_over_pi_squared", 1))
    add("boundary-drop", lambda d: d["boundary_cells"].pop())
    add("boundary-name", lambda d: d["boundary_cells"][1].__setitem__("id", "ordinary"))
    add("boundary-text", lambda d: d["boundary_cells"][0].__setitem__("result", "FORGED"))
    add("reference-url", lambda d: d["references"][0].__setitem__("url", "http://example.invalid"))
    add("reference-title-int", lambda d: d["references"][0].__setitem__("title", 0))
    add("reference-ownership-list", lambda d: d["references"][1].__setitem__("ownership", []))
    add("reference-identifier-fake-doi", lambda d: d["references"][1].__setitem__("identifier", "doi:10.0000/fake"))
    add("reference-url-fake-doi", lambda d: d["references"][2].__setitem__("url", "https://doi.org/10.0000/fake"))
    add("nonclaim-type", lambda d: d["nonclaims"].__setitem__(0, False))
    add("nonclaim-scope-escalation", lambda d: d["nonclaims"].__setitem__(3, "target Euler factors and root numbers are constructed"))
    add("payload-type", lambda d: d.__setitem__("payload_sha256", 1), False)
    text = EVIDENCE.read_text()
    attacks.extend([
        ("raw-duplicate-top", text.replace('  "candidate_id": "HCS-C297",', '  "candidate_id": "HCS-C297",\n  "candidate_id": "HCS-C297",', 1).encode()),
        ("raw-duplicate-nested", text.replace('    "version": "0.2.0"', '    "version": "0.2.0",\n    "version": "0.2.0"', 1).encode()),
        ("raw-nan", text.replace("1788307200", "NaN", 1).encode()),
        ("raw-array", b"[]\n"),
    ])

    yaml_text = EVALUATION.read_text()
    yaml_attacks: list[tuple[str, bytes]] = []

    def replace(name, old, new):
        if yaml_text.count(old) != 1:
            raise AssertionError(f"nonunique YAML mutation anchor: {name}")
        yaml_attacks.append((name, yaml_text.replace(old, new, 1).encode()))

    replace("yaml-duplicate-top", "route_b_invocation_allowed: false", "route_b_invocation_allowed: false\nroute_b_invocation_allowed: true")
    replace("yaml-duplicate-nested", "  euler_factors: false", "  euler_factors: false\n  euler_factors: true")
    yaml_attacks.append(("yaml-unknown-top", (yaml_text + "alien: 1\n").encode()))
    replace("yaml-missing-top", "theorem_status: PROVABLE AS STATED\n", "")
    replace("yaml-epoch-bool", "fixed_epoch: 1788307200", "fixed_epoch: true")
    replace("yaml-obstruction-id", "obstruction_id: HEN-O281", "obstruction_id: HEN-O999")
    replace("yaml-route-b", "route_b_invocation_allowed: false", "route_b_invocation_allowed: true")
    replace("yaml-scope", "scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: ROUTE_B_ALLOWED")
    replace("yaml-tuple", "A1_WEAK", "A1_PASS_ANALYTIC")
    replace("yaml-axis", "  A1: exact clean projective periodic family only", "  A1: isolated arithmetic UPO bridge")
    replace("yaml-flag-int", "  root_numbers: false", "  root_numbers: 0")
    replace("yaml-nonstring-key", "schema: route-a-evaluation-v0.2.0", "1: route-a-evaluation-v0.2.0")
    yaml_attacks.append(("yaml-anchor", ("defaults: &x 1\n" + yaml_text).encode()))
    yaml_attacks.append(("yaml-alias", (yaml_text + "alias_test: *x\n").encode()))
    yaml_attacks.append(("yaml-merge", ("base: &base {x: 1}\nmerge: {<<: *base}\n" + yaml_text).encode()))
    yaml_attacks.append(("yaml-array", b"[]\n"))

    passed = []
    for name, raw in attacks:
        if not rejected_json(raw):
            raise AssertionError(f"JSON mutation escaped: {name}")
        passed.append(name)
    for name, raw in yaml_attacks:
        if not rejected_yaml(raw):
            raise AssertionError(f"YAML mutation escaped: {name}")
        passed.append(name)
    print(json.dumps({"status": "C297_MUTATION_PASS", "total_rejections": len(passed), "json_rejections": len(attacks), "yaml_rejections": len(yaml_attacks), "attacks": passed}, sort_keys=True))


if __name__ == "__main__":
    main()
