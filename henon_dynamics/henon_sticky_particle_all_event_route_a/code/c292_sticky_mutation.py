#!/usr/bin/env python3
"""Hostile repaired-hash and raw-JSON attacks against the C292 checker."""
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
EVIDENCE = ROOT / "results/c292_sticky_evidence.json"
CHECKER = ROOT / "code/c292_sticky_checker.py"
EVALUATION = ROOT / "evaluations/route_a/HCS-C292/2026-09-02.yaml"


def phash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def rejected(raw: bytes) -> bool:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c292-mut-") as temporary:
        path = Path(temporary) / "attack.json"; path.write_bytes(raw)
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.returncode != 0


def yaml_rejected(raw: bytes) -> bool:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c292-yaml-mut-") as temporary:
        path = Path(temporary) / "evaluation.yaml"; path.write_bytes(raw)
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--evaluation", str(path)],
            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        return result.returncode != 0


def encoded(data: dict, repair: bool = True) -> bytes:
    if repair:
        data["payload_sha256"] = phash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, bytes]] = []
    def add(name: str, fn, repair: bool = True) -> None:
        data = copy.deepcopy(base); fn(data); attacks.append((name, encoded(data, repair)))

    add("stale-hash-control", lambda d: d["theorem_contract"].__setitem__("projection", "tampered"), False)
    add("unknown-top-key", lambda d: d.__setitem__("alien", 1))
    add("missing-top-key", lambda d: d.pop("model"))
    add("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True))
    add("epoch-string", lambda d: d.__setitem__("fixed_epoch", "1788307200"))
    add("evaluator-type", lambda d: d["evaluator"].__setitem__("version", 2))
    add("model-type", lambda d: d["model"].__setitem__("clock", False))
    add("theorem-repaired-hash", lambda d: d["theorem_contract"].__setitem__("weak_pde", "false theorem"))
    add("theorem-type", lambda d: d["theorem_contract"].__setitem__("events", True))
    add("proof-repaired-hash", lambda d: d["proof_contract"].__setitem__("weak_form", "handwave"))
    add("proof-type", lambda d: d["proof_contract"].__setitem__("hull", 1))
    add("route-tuple-bool", lambda d: d["route_a"]["tuple"].__setitem__(0, True))
    add("route-b-int", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("scope-true", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("scope-int", lambda d: d["scope_flags"].__setitem__("root_numbers", 0))
    add("enum-bool", lambda d: d["enumeration"].__setitem__("scenario_count", True))
    add("enum-string", lambda d: d["enumeration"].__setitem__("projection_cells", str(d["enumeration"]["projection_cells"])))
    add("scenario-duplicate", lambda d: d["scenarios"].append(copy.deepcopy(d["scenarios"][0])))
    add("scenario-drop", lambda d: d["scenarios"].pop())
    add("mass-noncanonical", lambda d: d["scenarios"][0]["raw_masses"].__setitem__(0, "1/1"))
    add("mass-int", lambda d: d["scenarios"][0]["raw_masses"].__setitem__(0, 1))
    add("raw-count-bool", lambda d: d["scenarios"][0].__setitem__("raw_particle_count", True))
    add("query-duplicate", lambda d: d["scenarios"][0]["query_times"].append(d["scenarios"][0]["query_times"][-1]))
    add("premerge-duplicate", lambda d: d["premerge_cells"].append(copy.deepcopy(d["premerge_cells"][0])))
    add("premerge-drop", lambda d: d["premerge_cells"].pop())
    add("raw-member-bool", lambda d: d["premerge_cells"][0]["raw_members"].__setitem__(0, True))
    add("event-drop", lambda d: d["event_cells"].pop())
    add("event-duplicate", lambda d: d["event_cells"].append(copy.deepcopy(d["event_cells"][0])))
    add("incoming-count-bool", lambda d: d["event_cells"][0]["groups"][0].__setitem__("incoming_cluster_count", True))
    add("energy-repaired-hash", lambda d: d["event_cells"][0]["groups"][0].__setitem__("energy_loss", "0"))
    add("projection-drop", lambda d: d["projection_cells"].pop())
    add("projection-duplicate", lambda d: d["projection_cells"].append(copy.deepcopy(d["projection_cells"][0])))
    add("projection-index-bool", lambda d: d["projection_cells"][0].__setitem__("canonical_index", False))
    add("cluster-member-bool", lambda d: d["projection_cells"][0]["cluster_members"].__setitem__(0, False))
    add("conservation-type", lambda d: d["conservation_cells"][0].__setitem__("merger_count", True))
    add("weak-drop", lambda d: d["weak_balance_cells"].pop())
    add("weak-duplicate", lambda d: d["weak_balance_cells"].append(copy.deepcopy(d["weak_balance_cells"][0])))
    add("weak-type", lambda d: d["weak_balance_cells"][0].__setitem__("group_index", False))
    add("reference-type", lambda d: d["references"][0].__setitem__("identifier", 9024373))
    add("nonclaim-type", lambda d: d["nonclaims"].__setitem__(0, False))
    add("hash-type", lambda d: d.__setitem__("payload_sha256", 1), False)

    text = EVIDENCE.read_text()
    attacks.extend([
        ("raw-duplicate-top", text.replace('  "candidate_id": "HCS-C292",', '  "candidate_id": "HCS-C292",\n  "candidate_id": "HCS-C292",', 1).encode()),
        ("raw-duplicate-nested", text.replace('    "version": "0.2.0"', '    "version": "0.2.0",\n    "version": "0.2.0"', 1).encode()),
        ("raw-nan", text.replace("1788307200", "NaN", 1).encode()),
        ("raw-top-array", b"[]\n"),
    ])

    yaml_text = EVALUATION.read_text()
    yaml_attacks: list[tuple[str, bytes]] = []

    def yreplace(name: str, old: str, new: str) -> None:
        if yaml_text.count(old) != 1:
            raise AssertionError(f"YAML attack anchor is not unique: {name}")
        yaml_attacks.append((name, yaml_text.replace(old, new, 1).encode()))

    yreplace("yaml-duplicate-top-route-b", "route_b_invocation_allowed: false", "route_b_invocation_allowed: false\nroute_b_invocation_allowed: true")
    yreplace("yaml-duplicate-nested-scope", "  euler_factors: false", "  euler_factors: false\n  euler_factors: true")
    yaml_attacks.append(("yaml-unknown-top", (yaml_text + "alien: 1\n").encode()))
    yreplace("yaml-missing-top", "theorem_status: PROVABLE AS STATED\n", "")
    yreplace("yaml-fixed-epoch-bool", "fixed_epoch: 1788307200", "fixed_epoch: true")
    yreplace("yaml-source-commit", "source_commit: 7fbe9db30cc460a82883533d7cfb2edd988c5b65", "source_commit: 0000000000000000000000000000000000000000")
    yreplace("yaml-evaluator-hash", "evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "evaluator_authority_sha256: 0000000000000000000000000000000000000000000000000000000000000000")
    yreplace("yaml-tuple-value", "A2_FAIL", "A2_TRAIN_ONLY")
    yreplace("yaml-tuple-bool", "tuple: [A0_FAIL", "tuple: [true")
    yreplace("yaml-overall", "overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_EXPLORATORY")
    yreplace("yaml-route-b-true", "route_b_invocation_allowed: false", "route_b_invocation_allowed: true")
    yreplace("yaml-route-b-int", "route_b_invocation_allowed: false", "route_b_invocation_allowed: 0")
    yreplace("yaml-scope-literal", "scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: ROUTE_B_ALLOWED")
    yreplace("yaml-scope-flag-true", "  euler_factors: false", "  euler_factors: true")
    yreplace("yaml-scope-flag-int", "  root_numbers: false", "  root_numbers: 0")
    yaml_attacks.append(("yaml-scope-unknown", (yaml_text + "  alien_scope_flag: false\n").encode()))
    yreplace("yaml-scope-missing", "  root_numbers: false\n", "")
    yreplace("yaml-axis-value", "  A1: no primitive-orbit repetition bridge", "  A1: primitive orbit bridge certified")
    yreplace("yaml-axis-unknown", "  A4: no relevant target quantization", "  A4: no relevant target quantization\n  A5: invented axis")
    yreplace("yaml-theorem-status", "theorem_status: PROVABLE AS STATED", "theorem_status: NOT_CURRENTLY_JUSTIFIED")
    yaml_attacks.append(("yaml-top-array", b"[]\n"))

    passed = []
    for name, raw in attacks:
        if not rejected(raw):
            raise AssertionError(f"mutation escaped: {name}")
        passed.append(name)
    for name, raw in yaml_attacks:
        if not yaml_rejected(raw):
            raise AssertionError(f"mutation escaped: {name}")
        passed.append(name)
    print(f"C292_MUTATION_PASS {len(passed)}/{len(passed)}: " + ", ".join(passed))


if __name__ == "__main__":
    main()
