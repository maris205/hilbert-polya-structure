#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C306."""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c306_walkers_checker.py"
EVIDENCE = ROOT / "results/c306_walkers_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C306/2026-09-03.yaml"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def canonical(data: dict, repair: bool = True) -> bytes:
    if repair:
        data["payload_sha256"] = payload_hash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def run(evidence: Path, evaluation: Path, optimized: bool = False):
    command = [sys.executable]
    if optimized:
        command.append("-O")
    command += [str(CHECKER), "--evidence", str(evidence), "--yaml", str(evaluation), "--skip-heavy"]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def main() -> None:
    baseline = run(EVIDENCE, EVALUATION)
    if baseline.returncode:
        raise AssertionError("baseline failed:\n" + baseline.stdout)
    optimized = run(EVIDENCE, EVALUATION, optimized=True)
    if optimized.returncode == 0 or "refuses python -O" not in optimized.stdout:
        raise AssertionError("checker did not explicitly reject python -O")
    checker_text = CHECKER.read_text(encoding="utf-8")
    if "import c306_walkers_producer" in checker_text or "from c306_walkers_producer" in checker_text:
        raise AssertionError("checker imports producer")

    original = json.loads(EVIDENCE.read_text())
    raw = EVIDENCE.read_bytes()
    yaml_raw = EVALUATION.read_bytes()
    killed: list[str] = []
    survived: list[tuple[str, str]] = []
    semantic = [
        ("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C305")),
        ("obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O000")),
        ("source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)),
        ("epoch-float", lambda d: d.__setitem__("fixed_epoch", 1788393600.0)),
        ("scope", lambda d: d.__setitem__("scope_literal", "OPEN")),
        ("model-killing", lambda d: d["model"].__setitem__("many_particle_killing", "reflect")),
        ("model-diagonal", lambda d: d["model"].__setitem__("generator", "diagonal -degree")),
        ("kernel-theorem", lambda d: d["theorem"].__setitem__("karlin_mcgregor", "permanent")),
        ("qsd-theorem", lambda d: d["theorem"].__setitem__("qsd", "uniform")),
        ("gap-theorem", lambda d: d["theorem"].__setitem__("gap", "epsilon_k")),
        ("proof-switch", lambda d: d["proof_certificates"].__setitem__("path_switching", "assumed")),
        ("case-L-bool", lambda d: d["finite_spectral_atlas"]["cases"][0].__setitem__("L", True)),
        ("case-k-float", lambda d: d["finite_spectral_atlas"]["cases"][4].__setitem__("k", 2.0)),
        ("dimension-bool", lambda d: d["finite_spectral_atlas"]["cases"][10].__setitem__("dimension", True)),
        ("mode-count-float", lambda d: d["finite_spectral_atlas"]["cases"][12].__setitem__("mode_count", 15.0)),
        ("state-coordinate-bool", lambda d: d["finite_spectral_atlas"]["cases"][6]["states"][0].__setitem__(0, False)),
        ("state-extra", lambda d: d["finite_spectral_atlas"]["cases"][8]["states"].append([99])),
        ("edge-count", lambda d: d["finite_spectral_atlas"]["cases"][20].__setitem__("legal_directed_edges", -1)),
        ("killing-count", lambda d: d["finite_spectral_atlas"]["cases"][21].__setitem__("total_killing_rate", 0)),
        ("trace", lambda d: d["finite_spectral_atlas"]["cases"][22].__setitem__("negative_generator_trace", 1)),
        ("ground-mode", lambda d: d["finite_spectral_atlas"]["cases"][13]["ground_mode"].__setitem__(0, 2)),
        ("ground-energy", lambda d: d["finite_spectral_atlas"]["cases"][14].__setitem__("ground_energy_decimal_15", "0.000000000000000")),
        ("ground-min", lambda d: d["finite_spectral_atlas"]["cases"][15].__setitem__("ground_h_min_decimal_15", "-1.000000000000000")),
        ("ground-norm", lambda d: d["finite_spectral_atlas"]["cases"][16].__setitem__("ground_h_l2_squared_decimal_15", "2.000000000000000")),
        ("gap-value", lambda d: d["finite_spectral_atlas"]["cases"][17].__setitem__("spectral_gap_decimal_15", "1.000000000000000")),
        ("singleton-gap", lambda d: d["finite_spectral_atlas"]["cases"][35].__setitem__("spectral_gap_decimal_15", "0.000000000000000")),
        ("residual", lambda d: d["finite_spectral_atlas"]["cases"][18].__setitem__("max_eigen_residual_decimal_12", "1.000000000000e+00")),
        ("probe-count-bool", lambda d: d["finite_spectral_atlas"]["cases"][19].__setitem__("probe_count", True)),
        ("probe-index-bool", lambda d: d["finite_spectral_atlas"]["cases"][5]["probes"][0].__setitem__("state_index", False)),
        ("probe-time", lambda d: d["finite_spectral_atlas"]["cases"][5]["probes"][1].__setitem__("time", "0.4")),
        ("probe-survival", lambda d: d["finite_spectral_atlas"]["cases"][5]["probes"][2].__setitem__("survival_decimal_15", "0.000000000000000")),
        ("probe-extra", lambda d: d["finite_spectral_atlas"]["cases"][5]["probes"].append(copy.deepcopy(d["finite_spectral_atlas"]["cases"][5]["probes"][-1]))),
        ("atlas-case-count-float", lambda d: d["finite_spectral_atlas"].__setitem__("case_count", 36.0)),
        ("atlas-state-rows", lambda d: d["finite_spectral_atlas"].__setitem__("state_rows", 0)),
        ("atlas-extra-case", lambda d: d["finite_spectral_atlas"]["cases"].append(copy.deepcopy(d["finite_spectral_atlas"]["cases"][-1]))),
        ("route-tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FAIL")),
        ("route-verdict", lambda d: d["route_a"].__setitem__("overall_verdict", "ROUTE_A_ACCEPTED")),
        ("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True)),
        ("scope-flag", lambda d: d["scope_flags"].__setitem__("claims_root_number", True)),
        ("boundary", lambda d: d["boundaries"].__setitem__(0, "exclusion")),
        ("source-token", lambda d: d["source_owner_tokens"].__setitem__(0, "fake")),
        ("summary-bool", lambda d: d["regression_summary"].__setitem__("case_count", True)),
        ("unknown-key", lambda d: d.__setitem__("unknown", 1)),
        ("drop-key", lambda d: d.pop("proof_certificates")),
    ]
    json_parser = [
        ("json-duplicate", lambda b: b.replace(b'{\n  "boundaries"', b'{\n  "candidate_id": "HCS-C306",\n  "boundaries"', 1)),
        ("json-trailing", lambda b: b + b"{}\n"),
        ("json-compact", lambda b: json.dumps(json.loads(b)).encode()),
        ("json-nan", lambda b: b.replace(b'"fixed_epoch": 1788393600', b'"fixed_epoch": NaN', 1)),
        ("json-invalid-utf8", lambda b: b + b"\xff"),
        ("json-top-list", lambda b: b"[]\n"),
    ]
    yaml_semantic = [
        ("yaml-candidate", lambda d: d.__setitem__("candidate_id", "HCS-C305")),
        ("yaml-source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("yaml-epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)),
        ("yaml-obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O000")),
        ("yaml-a0", lambda d: d["a0"].__setitem__("verdict", "A0_PASS")),
        ("yaml-a4", lambda d: d["a4"].__setitem__("verdict", "A4_FAIL")),
        ("yaml-tuple", lambda d: d["tuple"].__setitem__(4, "A4_FAIL")),
        ("yaml-route-b", lambda d: d.__setitem__("route_b_invocation_allowed", True)),
        ("yaml-flag", lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True)),
        ("yaml-artifact-extra", lambda d: d["artifact_paths"].append("extra")),
        ("yaml-source-token", lambda d: d["source_owner_tokens"].__setitem__(1, "fake")),
        ("yaml-unknown", lambda d: d.__setitem__("unknown", "x")),
    ]
    yaml_parser = [
        ("yaml-duplicate", lambda b: b + b"candidate_id: HCS-C306\n"),
        ("yaml-anchor", lambda b: b"a: &x y\nb: *x\n" + b),
        ("yaml-merge", lambda b: b"a: &x {v: 1}\nb: {<<: *x}\n" + b),
        ("yaml-nonstring", lambda b: b"1: bad\n" + b),
    ]

    with tempfile.TemporaryDirectory(prefix="c306-mutation-") as folder_name:
        folder = Path(folder_name)
        for name, mutate in semantic:
            data = copy.deepcopy(original)
            mutate(data)
            path = folder / (name + ".json")
            path.write_bytes(canonical(data, repair=True))
            result = run(path, EVALUATION)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))
        stale = copy.deepcopy(original)
        stale["candidate_id"] = "HCS-C305"
        stale_path = folder / "stale-hash.json"
        stale_path.write_bytes(canonical(stale, repair=False))
        result = run(stale_path, EVALUATION)
        (killed if result.returncode else survived).append("stale-hash" if result.returncode else ("stale-hash", result.stdout))
        for name, mutate in json_parser:
            path = folder / (name + ".json")
            path.write_bytes(mutate(raw))
            result = run(path, EVALUATION)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))
        base = yaml.safe_load(EVALUATION.read_text())
        for name, mutate in yaml_semantic:
            data = copy.deepcopy(base)
            mutate(data)
            path = folder / (name + ".yaml")
            path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
            result = run(EVIDENCE, path)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))
        for name, mutate in yaml_parser:
            path = folder / (name + ".yaml")
            path.write_bytes(mutate(yaml_raw))
            result = run(EVIDENCE, path)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))

    if survived:
        raise AssertionError(f"surviving mutations: {survived}")
    expected = len(semantic) + 1 + len(json_parser) + len(yaml_semantic) + len(yaml_parser)
    if len(killed) != expected:
        raise AssertionError("mutation accounting")
    print(f"C306 mutation suite PASS ({len(killed)}/{expected} repaired semantic/parser/stale-hash mutations killed)")
    print("classes=model,spectrum,coordinates,type-traps,probes,QSD,gap,route,scope,JSON,YAML,python-O")


if __name__ == "__main__":
    main()
