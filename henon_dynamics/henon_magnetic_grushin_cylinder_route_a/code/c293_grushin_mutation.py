#!/usr/bin/env python3
"""Hostile repaired-hash and raw-JSON attacks for HCS-C293."""
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
EVIDENCE = ROOT/"results/c293_grushin_evidence.json"
CHECKER = ROOT/"code/c293_grushin_checker.py"
EVALUATION = ROOT/"evaluations/route_a/HCS-C293/2026-09-02.yaml"


def phash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def encode(data: dict, repair: bool = True) -> bytes:
    if repair: data["payload_sha256"] = phash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n").encode()


def rejected(raw: bytes) -> bool:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE":"1", "TZ":"UTC"})
    with tempfile.TemporaryDirectory(prefix="c293-mut-") as temporary:
        path = Path(temporary)/"attack.json"; path.write_bytes(raw)
        result = subprocess.run([sys.executable, "-B", str(CHECKER), str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.returncode != 0


def yaml_rejected(raw: bytes) -> bool:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE":"1", "TZ":"UTC"})
    with tempfile.TemporaryDirectory(prefix="c293-yaml-mut-") as temporary:
        path = Path(temporary)/"evaluation.yaml"; path.write_bytes(raw)
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(EVIDENCE), "--evaluation", str(path)],
            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text()); attacks: list[tuple[str,bytes]] = []
    def add(name: str, fn, repair: bool = True) -> None:
        data = copy.deepcopy(base); fn(data); attacks.append((name, encode(data, repair)))
    add("stale-hash-control", lambda d: d["theorem_contract"].__setitem__("integer", "tampered"), False)
    add("unknown-top", lambda d: d.__setitem__("alien", 1)); add("missing-top", lambda d: d.pop("model"))
    add("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)); add("epoch-string", lambda d: d.__setitem__("fixed_epoch", "1788307200"))
    add("evaluator-type", lambda d: d["evaluator"].__setitem__("version", 2)); add("model-type", lambda d: d["model"].__setitem__("form", False))
    add("theorem-integer", lambda d: d["theorem_contract"].__setitem__("integer", "pure point only")); add("theorem-type", lambda d: d["theorem_contract"].__setitem__("noninteger", True))
    add("proof-integer", lambda d: d["proof_contract"].__setitem__("integer_type", "handwave")); add("proof-type", lambda d: d["proof_contract"].__setitem__("form", 1))
    add("route-tuple-type", lambda d: d["route_a"]["tuple"].__setitem__(0, True)); add("route-b-int", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("flag-true", lambda d: d["scope_flags"].__setitem__("euler_factors", True)); add("flag-int", lambda d: d["scope_flags"].__setitem__("root_numbers", 0))
    add("enum-bool", lambda d: d["enumeration"].__setitem__("spectral_cells", True)); add("enum-flux-int", lambda d: d["enumeration"]["noninteger_fluxes"].__setitem__(0, 1))
    add("enum-k-bool", lambda d: d["enumeration"]["k_values"].__setitem__(0, False))
    add("spectral-drop", lambda d: d["spectral_cells"].pop()); add("spectral-duplicate", lambda d: d["spectral_cells"].append(copy.deepcopy(d["spectral_cells"][0])))
    add("spectral-value", lambda d: d["spectral_cells"][0].__setitem__("eigenvalue", "999")); add("spectral-k-bool", lambda d: d["spectral_cells"][0].__setitem__("k", True)); add("spectral-fraction-noncanonical", lambda d: d["spectral_cells"][0].__setitem__("alpha", "2/6"))
    add("heat-drop", lambda d: d["heat_cells"].pop()); add("heat-duplicate", lambda d: d["heat_cells"].append(copy.deepcopy(d["heat_cells"][0])))
    add("heat-value", lambda d: d["heat_cells"][0].__setitem__("trace", "1.0")); add("heat-time-int", lambda d: d["heat_cells"][0].__setitem__("t", 1)); add("heat-cutoff-bool", lambda d: d["heat_cells"][0].__setitem__("k_cutoff", True))
    add("integer-heat-drop", lambda d: d["integer_heat_cells"].pop()); add("integer-heat-value", lambda d: d["integer_heat_cells"][0].__setitem__("nonresonant_trace", "0.0")); add("integer-cutoff-bool", lambda d: d["integer_heat_cells"][0].__setitem__("mode_cutoff", False))
    add("multiplicity-drop", lambda d: d["multiplicity_cells"].pop()); add("multiplicity-duplicate", lambda d: d["multiplicity_cells"].append(copy.deepcopy(d["multiplicity_cells"][0])))
    add("multiplicity-value", lambda d: d["multiplicity_cells"][0].__setitem__("multiplicity", 4)); add("multiplicity-N-bool", lambda d: d["multiplicity_cells"][0].__setitem__("N", True))
    add("count-drop", lambda d: d["counting_cells"].pop()); add("count-value", lambda d: d["counting_cells"][0].__setitem__("exact_count", 25)); add("count-Lambda-bool", lambda d: d["counting_cells"][0].__setitem__("Lambda", True))
    add("zeta-drop", lambda d: d["zeta_cells"].pop()); add("zeta-value", lambda d: d["zeta_cells"][0].__setitem__("value", "1.0")); add("zeta-s-bool", lambda d: d["zeta_cells"][0].__setitem__("s", True))
    add("symmetry-drop", lambda d: d["symmetry_cells"].pop()); add("symmetry-value", lambda d: d["symmetry_cells"][0].__setitem__("fundamental_distance", "1/3")); add("symmetry-bool-int", lambda d: d["symmetry_cells"][0].__setitem__("integer_flux", 0))
    add("integer-spectrum-ac", lambda d: d["integer_spectrum"].__setitem__("absolutely_continuous_spectrum", "empty")); add("integer-spectrum-ac-multiplicity-one", lambda d: d["integer_spectrum"].__setitem__("absolutely_continuous_multiplicity", 1)); add("integer-spectrum-bool-int", lambda d: d["integer_spectrum"].__setitem__("singular_continuous_spectrum_empty", 1))
    add("reference-type", lambda d: d["references"][0].__setitem__("identifier", 14066578)); add("nonclaim-type", lambda d: d["nonclaims"].__setitem__(0, False)); add("hash-type", lambda d: d.__setitem__("payload_sha256", 1), False)
    text = EVIDENCE.read_text()
    attacks.extend([
        ("raw-duplicate-top", text.replace('  "candidate_id": "HCS-C293",', '  "candidate_id": "HCS-C293",\n  "candidate_id": "HCS-C293",', 1).encode()),
        ("raw-duplicate-nested", text.replace('    "version": "0.2.0"', '    "version": "0.2.0",\n    "version": "0.2.0"', 1).encode()),
        ("raw-nan", text.replace("1788307200", "NaN", 1).encode()), ("raw-array", b"[]\n"),
    ])

    yaml_text = EVALUATION.read_text(); yaml_attacks: list[tuple[str,bytes]] = []
    def yreplace(name: str, old: str, new: str) -> None:
        if yaml_text.count(old) != 1: raise AssertionError(f"YAML attack anchor is not unique: {name}")
        yaml_attacks.append((name, yaml_text.replace(old, new, 1).encode()))
    yreplace("yaml-duplicate-top-route-b", "route_b_invocation_allowed: false", "route_b_invocation_allowed: false\nroute_b_invocation_allowed: true")
    yreplace("yaml-duplicate-nested-scope", "  euler_factors: false", "  euler_factors: false\n  euler_factors: true")
    yaml_attacks.append(("yaml-unknown-top", (yaml_text+"alien: 1\n").encode()))
    yreplace("yaml-missing-top", "theorem_status: PROVABLE AS STATED\n", "")
    yreplace("yaml-fixed-epoch-bool", "fixed_epoch: 1788307200", "fixed_epoch: true")
    yreplace("yaml-source-commit", "source_commit: 7fbe9db30cc460a82883533d7cfb2edd988c5b65", "source_commit: 0000000000000000000000000000000000000000")
    yreplace("yaml-evaluator-hash", "evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "evaluator_authority_sha256: 0000000000000000000000000000000000000000000000000000000000000000")
    yreplace("yaml-tuple-value", "A2_FAIL", "A2_TRAIN_ONLY")
    yreplace("yaml-tuple-bool", "tuple: [A0_WEAK_ARITHMETIC_RELATION", "tuple: [true")
    yreplace("yaml-overall", "overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_EXPLORATORY")
    yreplace("yaml-route-b-true", "route_b_invocation_allowed: false", "route_b_invocation_allowed: true")
    yreplace("yaml-route-b-int", "route_b_invocation_allowed: false", "route_b_invocation_allowed: 0")
    yreplace("yaml-scope-literal", "scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: ROUTE_B_ALLOWED")
    yreplace("yaml-scope-flag-true", "  euler_factors: false", "  euler_factors: true")
    yreplace("yaml-scope-flag-int", "  root_numbers: false", "  root_numbers: 0")
    yaml_attacks.append(("yaml-scope-unknown", (yaml_text+"  alien_scope_flag: false\n").encode()))
    yreplace("yaml-scope-missing", "  root_numbers: false\n", "")
    yreplace("yaml-axis-value", "  A1: no primitive-orbit repetition bridge", "  A1: primitive orbit bridge certified")
    yreplace("yaml-axis-unknown", "  A4: natural Friedrichs quantization", "  A4: natural Friedrichs quantization\n  A5: invented axis")
    yreplace("yaml-theorem-status", "theorem_status: PROVABLE AS STATED", "theorem_status: NOT_CURRENTLY_JUSTIFIED")
    yaml_attacks.append(("yaml-top-array", b"[]\n"))

    passed=[]
    for name, raw in attacks:
        if not rejected(raw): raise AssertionError(f"mutation escaped: {name}")
        passed.append(name)
    for name, raw in yaml_attacks:
        if not yaml_rejected(raw): raise AssertionError(f"mutation escaped: {name}")
        passed.append(name)
    print(f"C293_MUTATION_PASS {len(passed)}/{len(passed)}: " + ", ".join(passed))


if __name__ == "__main__": main()
