#!/usr/bin/env python3
"""Hostile repaired-hash JSON and raw YAML attacks for HCS-C296."""
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
EVIDENCE = ROOT / "results/c296_hard_rod_evidence.json"
CHECKER = ROOT / "code/c296_hard_rod_checker.py"
EVALUATION = ROOT / "evaluations/route_a/HCS-C296/2026-09-02.yaml"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"


def phash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def encode(data: dict, repair: bool = True) -> bytes:
    if repair:
        data["payload_sha256"] = phash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def rejected(raw: bytes) -> bool:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c296-mut-") as temporary:
        path = Path(temporary) / "attack.json"
        path.write_bytes(raw)
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.returncode != 0


def yaml_rejected(raw: bytes) -> bool:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c296-yaml-mut-") as temporary:
        path = Path(temporary) / "evaluation.yaml"
        path.write_bytes(raw)
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--evaluation", str(path)],
            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, bytes]] = []

    def add(name: str, fn, repair: bool = True) -> None:
        data = copy.deepcopy(base)
        fn(data)
        attacks.append((name, encode(data, repair)))

    add("stale-hash-control", lambda d: d["theorem_contract"].__setitem__("conjugacy", "tampered"), False)
    add("unknown-top", lambda d: d.__setitem__("alien", 1))
    add("missing-top", lambda d: d.pop("model"))
    add("obstruction-id", lambda d: d.__setitem__("obstruction_id", "HEN-O999"))
    add("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True))
    add("epoch-string", lambda d: d.__setitem__("fixed_epoch", "1788307200"))
    add("evaluator-type", lambda d: d["evaluator"].__setitem__("version", 2))
    add("model-value", lambda d: d["model"].__setitem__("shape_quotient", "no rotation quotient"))
    add("model-type", lambda d: d["model"].__setitem__("clock", False))
    add("theorem-conjugacy", lambda d: d["theorem_contract"].__setitem__("conjugacy", "unreduced conjugacy"))
    add("theorem-topology", lambda d: d["theorem_contract"].__setitem__("topology_obstruction", "none"))
    add("theorem-type", lambda d: d["theorem_contract"].__setitem__("events", True))
    add("proof-gap", lambda d: d["proof_contract"].__setitem__("gap_map", "handwave"))
    add("proof-obstruction", lambda d: d["proof_contract"].__setitem__("obstruction_proof", "omitted"))
    add("proof-type", lambda d: d["proof_contract"].__setitem__("flow", 1))
    add("route-tuple-value", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route-tuple-bool", lambda d: d["route_a"]["tuple"].__setitem__(0, True))
    add("route-overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_EXPLORATORY"))
    add("route-b-int", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("flag-true", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("flag-int", lambda d: d["scope_flags"].__setitem__("root_numbers", 0))
    add("enum-bool", lambda d: d["enumeration"].__setitem__("event_time_cells", True))
    add("scenario-drop", lambda d: d["scenarios"].pop())
    add("scenario-duplicate", lambda d: d["scenarios"].append(copy.deepcopy(d["scenarios"][0])))
    add("scenario-ell", lambda d: d["scenarios"][0].__setitem__("ell", "12"))
    add("scenario-N-bool", lambda d: d["scenarios"][0].__setitem__("N", True))
    add("particle-drop", lambda d: d["particle_cells"].pop())
    add("particle-duplicate", lambda d: d["particle_cells"].append(copy.deepcopy(d["particle_cells"][0])))
    add("particle-y", lambda d: d["particle_cells"][0].__setitem__("y", "1"))
    add("particle-index-bool", lambda d: d["particle_cells"][0].__setitem__("index", False))
    add("pair-drop", lambda d: d["pair_crossing_cells"].pop())
    add("pair-duplicate", lambda d: d["pair_crossing_cells"].append(copy.deepcopy(d["pair_crossing_cells"][0])))
    add("pair-time", lambda d: d["pair_crossing_cells"][0].__setitem__("time", "2"))
    add("pair-index-bool", lambda d: d["pair_crossing_cells"][0].__setitem__("i", True))
    add("event-drop", lambda d: d["event_cells"].pop())
    add("event-duplicate", lambda d: d["event_cells"].append(copy.deepcopy(d["event_cells"][0])))
    add("event-time", lambda d: d["event_cells"][0].__setitem__("time", "3/2"))
    add("event-group-count", lambda d: d["event_cells"][0].__setitem__("group_count", 2))
    add("group-outgoing", lambda d: d["event_cells"][0]["groups"][0]["outgoing_spatial_velocities"].reverse())
    add("group-energy", lambda d: d["event_cells"][0]["groups"][0].__setitem__("twice_energy_after", "99"))
    add("shape-drop", lambda d: d["shape_cells"].pop())
    add("shape-duplicate", lambda d: d["shape_cells"].append(copy.deepcopy(d["shape_cells"][0])))
    add("shape-gap", lambda d: d["shape_cells"][0]["gap_signature"].__setitem__(0, "1"))
    add("shape-phase-type", lambda d: d["shape_cells"][0]["phase_signature"].__setitem__(0, False))
    add("stabilizer-drop", lambda d: d["stabilizer_cells"].pop())
    add("stabilizer-duplicate", lambda d: d["stabilizer_cells"].append(copy.deepcopy(d["stabilizer_cells"][0])))
    add("stabilizer-order", lambda d: d["stabilizer_cells"][0].__setitem__("stabilizer_order", 2))
    add("stabilizer-shift", lambda d: d["stabilizer_cells"][0]["stabilizer_shifts"].__setitem__(0, "1"))
    add("return-drop", lambda d: d["return_cells"].pop())
    add("return-duplicate", lambda d: d["return_cells"].append(copy.deepcopy(d["return_cells"][0])))
    add("return-period", lambda d: d["return_cells"][0].__setitem__("minimal_period", "6"))
    add("return-translation", lambda d: d["return_cells"][0].__setitem__("witness_common_translation", "0"))
    add("return-permutation", lambda d: d["return_cells"][0]["witness_permutation"].reverse())
    add("symbolic-verdict", lambda d: d["symbolic_return_cases"][0].__setitem__("verdict", "PERIODIC"))
    add("symbolic-velocity", lambda d: d["symbolic_return_cases"][0]["velocities"].__setitem__(2, "2"))
    add("conservation-drop", lambda d: d["conservation_cells"].pop())
    add("conservation-energy", lambda d: d["conservation_cells"][0].__setitem__("twice_kinetic_energy", "0"))
    add("boundary-drop", lambda d: d["boundary_cells"].pop())
    add("boundary-counterexample", lambda d: d["boundary_cells"][2].__setitem__("status", "unreduced map is valid"))
    add("boundary-text", lambda d: d["boundary_cells"][0].__setitem__("status", "forged boundary claim"))
    add("reference-id", lambda d: d["references"][0].__setitem__("id", "ForgedOwner"))
    add("reference-authors", lambda d: d["references"][0].__setitem__("authors", "Forged Owner"))
    add("reference-title", lambda d: d["references"][0].__setitem__("title", "Forged title"))
    add("reference-venue", lambda d: d["references"][0].__setitem__("venue", "Forged venue"))
    add("reference-identifier", lambda d: d["references"][0].__setitem__("identifier", "unknown"))
    add("reference-url", lambda d: d["references"][0].__setitem__("url", "https://example.invalid/forged"))
    add("reference-ownership", lambda d: d["references"][0].__setitem__("ownership", "forged ownership"))
    add("nonclaim-scope-escalation", lambda d: d["nonclaims"].__setitem__(0, "we claim a target Euler factor and root number"))
    add("nonclaim-reduction", lambda d: d["nonclaims"].__setitem__(1, "complete physical conjugacy"))
    add("hash-type", lambda d: d.__setitem__("payload_sha256", 1), False)

    text = EVIDENCE.read_text()
    attacks.extend([
        ("raw-duplicate-top", text.replace('  "candidate_id": "HCS-C296",', '  "candidate_id": "HCS-C296",\n  "candidate_id": "HCS-C296",', 1).encode()),
        ("raw-duplicate-nested", text.replace('    "version": "0.2.0"', '    "version": "0.2.0",\n    "version": "0.2.0"', 1).encode()),
        ("raw-nan", text.replace("1788307200", "NaN", 1).encode()),
        ("raw-array", b"[]\n"),
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
    yreplace("yaml-missing-top", "theorem_status: PROVABLE AS CORRECTED\n", "")
    yreplace("yaml-fixed-epoch-bool", "fixed_epoch: 1788307200", "fixed_epoch: true")
    yreplace("yaml-source-commit", f"source_commit: {SOURCE}", "source_commit: 0000000000000000000000000000000000000000")
    yreplace("yaml-obstruction-id", "obstruction_id: HEN-O280", "obstruction_id: HEN-O999")
    yreplace("yaml-evaluator-hash", "evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "evaluator_authority_sha256: 0000000000000000000000000000000000000000000000000000000000000000")
    yreplace("yaml-tuple-value", "A1_WEAK", "A1_PASS_ANALYTIC")
    yreplace("yaml-tuple-bool", "tuple: [A0_FAIL", "tuple: [true")
    yreplace("yaml-overall", "overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_EXPLORATORY")
    yreplace("yaml-route-b-true", "route_b_invocation_allowed: false", "route_b_invocation_allowed: true")
    yreplace("yaml-route-b-int", "route_b_invocation_allowed: false", "route_b_invocation_allowed: 0")
    yreplace("yaml-scope-literal", "scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: ROUTE_B_ALLOWED")
    yreplace("yaml-scope-flag-true", "  euler_factors: false", "  euler_factors: true")
    yreplace("yaml-scope-flag-int", "  root_numbers: false", "  root_numbers: 0")
    yaml_attacks.append(("yaml-scope-unknown", (yaml_text + "  alien_scope_flag: false\n").encode()))
    yreplace("yaml-scope-missing", "  root_numbers: false\n", "")
    yreplace("yaml-axis-value", "  A1: exact reduced periodic-return classification but no prime-like orbit bridge", "  A1: prime orbit bridge certified")
    yreplace("yaml-axis-unknown", "  A4: natural hard-core kinetic quantization on the reduced collision chamber", "  A4: natural hard-core kinetic quantization on the reduced collision chamber\n  A5: invented axis")
    yreplace("yaml-theorem-status", "theorem_status: PROVABLE AS CORRECTED", "theorem_status: PROVABLE AS ORIGINALLY STATED")
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
    print(f"C296_MUTATION_PASS {len(passed)}/{len(passed)}: " + ", ".join(passed))


if __name__ == "__main__":
    main()
