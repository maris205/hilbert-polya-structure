#!/usr/bin/env python3
"""Hostile repaired-hash JSON and strict-YAML attacks for HCS-C295."""
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
EVIDENCE = ROOT / "results/c295_isochrone_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C295/2026-09-02.yaml"
CHECKER = ROOT / "code/c295_isochrone_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def encoded(data: dict, repair: bool = True) -> bytes:
    if repair:
        data["payload_sha256"] = payload_hash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def rejected_json(raw: bytes) -> bool:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c295-json-mut-") as temporary:
        path = Path(temporary) / "attack.json"
        path.write_bytes(raw)
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(path), "--yaml", str(EVALUATION)],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return result.returncode != 0


def rejected_yaml(raw: bytes) -> bool:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    with tempfile.TemporaryDirectory(prefix="c295-yaml-mut-") as temporary:
        path = Path(temporary) / "attack.yaml"
        path.write_bytes(raw)
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--yaml", str(path)],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    json_attacks: list[tuple[str, bytes]] = []

    def add(name: str, mutator, repair: bool = True) -> None:
        value = copy.deepcopy(base)
        mutator(value)
        json_attacks.append((name, encoded(value, repair)))

    add("stale-payload-hash", lambda d: d["model"].__setitem__("clock", "tampered"), False)
    add("unknown-top-key", lambda d: d.__setitem__("alien", 1))
    add("missing-top-key", lambda d: d.pop("proof_contract"))
    add("schema-value", lambda d: d.__setitem__("schema", "hcs-c295-v0"))
    add("candidate-value", lambda d: d.__setitem__("candidate_id", "HCS-C294"))
    add("source-commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True))
    add("epoch-string", lambda d: d.__setitem__("fixed_epoch", "1788307200"))
    add("scope-literal", lambda d: d.__setitem__("scope_literal", "ROUTE_B_ALLOWED"))
    add("evaluator-version-type", lambda d: d["evaluator"].__setitem__("version", 0.2))
    add("evaluator-sha", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("model-hamiltonian", lambda d: d["model"].__setitem__("hamiltonian", "free"))
    add("model-unknown", lambda d: d["model"].__setitem__("alien", "x"))
    add("theorem-energy-domain", lambda d: d["theorem_contract"].__setitem__("energy_domain", "all E"))
    add("theorem-period-type", lambda d: d["theorem_contract"].__setitem__("period", True))
    add("proof-apsidal", lambda d: d["proof_contract"].__setitem__("apsidal_integral", "handwave"))
    add("proof-missing", lambda d: d["proof_contract"].pop("closure_logic"))
    add("route-tuple-value", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS"))
    add("route-tuple-bool", lambda d: d["route_a"]["tuple"].__setitem__(0, False))
    add("route-b-int", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("scope-flag-true", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("scope-flag-int", lambda d: d["scope_flags"].__setitem__("root_numbers", 0))
    add("enumeration-mu-bool", lambda d: d["enumeration"]["mu_values"].__setitem__(0, True))
    add("enumeration-grid-value", lambda d: d["enumeration"]["ell_values"].__setitem__(3, 4))
    add("enumeration-count-bool", lambda d: d["enumeration"].__setitem__("orbit_cells", True))
    add("enumeration-closure-count", lambda d: d["enumeration"]["closure_counts"].__setitem__("closed_resonant", 15))
    add("orbit-drop", lambda d: d["orbit_cells"].pop())
    add("orbit-duplicate", lambda d: d["orbit_cells"].append(copy.deepcopy(d["orbit_cells"][0])))
    add("orbit-row-unknown", lambda d: d["orbit_cells"][0].__setitem__("alien", 1))
    add("orbit-row-missing", lambda d: d["orbit_cells"][0].pop("omega_r"))
    add("orbit-mu-bool", lambda d: d["orbit_cells"][0].__setitem__("mu", True))
    add("orbit-radicand", lambda d: d["orbit_cells"][0].__setitem__("radicand", 99))
    add("orbit-square-int", lambda d: d["orbit_cells"][0].__setitem__("radicand_square", 1))
    add("orbit-decimal-type", lambda d: d["orbit_cells"][0].__setitem__("sqrt_radicand_decimal", 2.0))
    add("quad-missing-key", lambda d: d["orbit_cells"][0]["energy"].pop("c"))
    add("quad-unknown-key", lambda d: d["orbit_cells"][0]["energy"].__setitem__("alien", "0"))
    add("quad-d-bool", lambda d: d["orbit_cells"][0]["energy"].__setitem__("d", True))
    add("fraction-noncanonical", lambda d: d["orbit_cells"][1]["radial_action"].__setitem__("a", "0/2"))
    add("energy-value", lambda d: d["orbit_cells"][1]["energy"].__setitem__("a", "0"))
    add("action-value", lambda d: d["orbit_cells"][1]["radial_action"].__setitem__("c", "99"))
    add("turning-root-value", lambda d: d["orbit_cells"][1].__setitem__("x_apo_decimal", "999"))
    add("closure-class", lambda d: d["orbit_cells"][1].__setitem__("closure_class", "closed_resonant"))
    add("primitive-cycles-bool", lambda d: d["orbit_cells"][1].__setitem__("primitive_radial_cycles", True))
    add("boundary-drop", lambda d: d["boundary_cells"].pop())
    add("boundary-face", lambda d: d["boundary_cells"][0].__setitem__("face", "invented"))
    add("boundary-text", lambda d: d["boundary_cells"][0].__setitem__("statement", "forged boundary claim"))
    add("boundary-unknown", lambda d: d["boundary_cells"][0].__setitem__("alien", "x"))
    add("reference-id", lambda d: d["references"][0].__setitem__("id", "ForgedOwner"))
    add("reference-authors", lambda d: d["references"][0].__setitem__("authors", "Forged Owner"))
    add("reference-title", lambda d: d["references"][0].__setitem__("title", "Forged title"))
    add("reference-venue", lambda d: d["references"][0].__setitem__("venue", "Forged venue"))
    add("reference-identifier", lambda d: d["references"][2].__setitem__("identifier", "wrong"))
    add("reference-url-value", lambda d: d["references"][0].__setitem__("url", "https://example.invalid/forged"))
    add("reference-ownership", lambda d: d["references"][0].__setitem__("ownership", "forged ownership"))
    add("reference-type", lambda d: d["references"][0].__setitem__("url", 1))
    add("nonclaim-scope-escalation", lambda d: d["nonclaims"].__setitem__(0, "we claim a target Euler factor and root number"))
    add("nonclaim-type", lambda d: d["nonclaims"].__setitem__(0, False))
    add("payload-type", lambda d: d.__setitem__("payload_sha256", 1), False)

    text = EVIDENCE.read_text()
    json_attacks.extend([
        ("raw-duplicate-top", text.replace('  "candidate_id": "HCS-C295",', '  "candidate_id": "HCS-C295",\n  "candidate_id": "HCS-C295",', 1).encode()),
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

    yreplace("yaml-duplicate-top", "route_b_invocation_allowed: false", "route_b_invocation_allowed: false\nroute_b_invocation_allowed: true")
    yreplace("yaml-duplicate-nested", "  euler_factors: false", "  euler_factors: false\n  euler_factors: true")
    yaml_attacks.append(("yaml-unknown-top", (yaml_text + "alien: 1\n").encode()))
    yreplace("yaml-missing-top", "theorem_status: PROVABLE_AS_STATED\n", "")
    yreplace("yaml-epoch-bool", "fixed_epoch: 1788307200", "fixed_epoch: true")
    yreplace("yaml-epoch-string", "fixed_epoch: 1788307200", 'fixed_epoch: "1788307200"')
    yreplace("yaml-source", "source_commit: f8d3ad9a8940b54e82854b2924be353575ed8fcb", "source_commit: 0000000000000000000000000000000000000000")
    yreplace("yaml-evaluator", "evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "evaluator_authority_sha256: " + "0" * 64)
    yreplace("yaml-artifact", "  - paper/main.pdf", "  - paper/missing.pdf")
    yreplace("yaml-tuple-value", "tuple: [A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION]", "tuple: [A0_FAIL, A1_PASS, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION]")
    yreplace("yaml-tuple-bool", "tuple: [A0_FAIL", "tuple: [true")
    yreplace("yaml-overall", "overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_PASS")
    yreplace("yaml-route-b-true", "route_b_invocation_allowed: false", "route_b_invocation_allowed: true")
    yreplace("yaml-route-b-int", "route_b_invocation_allowed: false", "route_b_invocation_allowed: 0")
    yreplace("yaml-scope", "scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: ROUTE_B_ALLOWED")
    yreplace("yaml-flag-true", "  euler_factors: false", "  euler_factors: true")
    yreplace("yaml-flag-int", "  root_numbers: false", "  root_numbers: 0")
    yreplace("yaml-axis-verdict", "  verdict: A0_FAIL", "  verdict: A0_PASS")
    yreplace("yaml-axis-type", "a0:\n  verdict: A0_FAIL\n  evidence_status: PROVED", "a0:\n  verdict: A0_FAIL\n  evidence_status: true")
    yreplace("yaml-theorem-status", "theorem_status: PROVABLE_AS_STATED", "theorem_status: NOT_PROVED")
    yreplace("yaml-owner-token", "  - 10.1063/5.0056957", "  - invented")
    yaml_attacks.append(("yaml-anchor", (yaml_text + "anchored: &blocked value\n").encode()))
    yaml_attacks.append(("yaml-alias", (yaml_text + "anchored: &blocked value\nalias: *blocked\n").encode()))
    yaml_attacks.append(("yaml-merge", (yaml_text + "base: &base {x: 1}\nmerged: {<<: *base}\n").encode()))
    yaml_attacks.append(("yaml-top-array", b"[]\n"))

    passed: list[str] = []
    for name, raw in json_attacks:
        if not rejected_json(raw):
            raise AssertionError(f"JSON mutation escaped: {name}")
        passed.append(name)
    for name, raw in yaml_attacks:
        if not rejected_yaml(raw):
            raise AssertionError(f"YAML mutation escaped: {name}")
        passed.append(name)
    print(f"C295_MUTATION_PASS {len(passed)}/{len(passed)}: " + ", ".join(passed))


if __name__ == "__main__":
    main()
