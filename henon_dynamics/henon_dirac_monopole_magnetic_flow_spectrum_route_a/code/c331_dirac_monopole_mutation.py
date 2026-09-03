#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C331."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C331 mutation lane refuses optimized Python")

root = Path(__file__).resolve().parents[1]
evidence_path = root / "results/c331_dirac_monopole_evidence.json"
evaluation_path = root / "evaluations/route_a/HCS-C331/2026-09-03.yaml"
checker = root / "code/c331_dirac_monopole_checker.py"
source = json.loads(evidence_path.read_text())


def repair(data):
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


mutators = [
    lambda d: d.__setitem__("candidate_id", "HCS-C330"),
    lambda d: d.__setitem__("source_commit", "0"*40),
    lambda d: d.__setitem__("evaluation_date", "2026-09-02"),
    lambda d: d["evaluator"].__setitem__("authority", "wrong.md"),
    lambda d: d["evaluation_lock"].__setitem__("semantic_sha256", "0"*64),
    lambda d: d["scope_flags"].__setitem__("claims_target_zero_match", True),
    lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
    lambda d: d["model"].__setitem__("extra", "unowned"),
    lambda d: d["model"].__setitem__("quantum_operator", "unspecified extension"),
    lambda d: d["theorem_contract"].__setitem__("period", "wrong"),
    lambda d: d["theorem_contract"].__setitem__("bundle_connection_bridge", "same curvature is assumed to imply equality"),
    lambda d: d["theorem_contract"].pop("operator_realization"),
    lambda d: d["classical_rows"][0].__setitem__("q", -5),
    lambda d: d["classical_rows"][1].__setitem__("speed", "2/4"),
    lambda d: d["classical_rows"][2].__setitem__("period", "nan"),
    lambda d: d["classical_rows"][3]["quarter_positions"][1].__setitem__("x", "nan"),
    lambda d: d["classical_rows"][4]["quarter_positions"].pop(),
    lambda d: d["classical_rows"][5].__setitem__("extra", 1),
    lambda d: d["spectral_rows"][0].__setitem__("multiplicity", 99),
    lambda d: d["spectral_rows"][17].__setitem__("eigenvalue", "0"),
    lambda d: d["spectral_rows"].__setitem__(20, copy.deepcopy(d["spectral_rows"][19])),
    lambda d: d["heat_rows"][0].__setitem__("partial_heat_trace", "nan"),
    lambda d: d["heat_rows"][1].__setitem__("cutoff", 79),
    lambda d: d["chern_rows"][0].__setitem__("charge", "-24/2"),
    lambda d: d["chern_rows"][1].__setitem__("flux_over_two_pi", -10),
    lambda d: d["time_reversal_rows"][0].__setitem__("paired_tangent_x", "1/2"),
    lambda d: d["boundary_atlas"].pop(),
    lambda d: d["boundary_atlas"][-2].__setitem__("status", "fixed curvature leaves unaudited holonomy"),
    lambda d: d["references"][0].__setitem__("doi", "10.0000/fake"),
    lambda d: d["enumeration"].__setitem__("extra", 1),
]

attempts = 0
with tempfile.TemporaryDirectory(prefix="c331-mutations-") as directory:
    directory = Path(directory)
    for index, mutate in enumerate(mutators):
        for repaired in (False, True):
            data = copy.deepcopy(source); mutate(data)
            if repaired:
                repair(data)
            path = directory / f"evidence-{index}-{int(repaired)}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
            run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode == 0:
                raise AssertionError(f"evidence mutation survived: {index}/{repaired}")
            attempts += 1
    raw_json = evidence_path.read_text()
    for index, changed in enumerate((
        raw_json.replace('"candidate_id": "HCS-C331",', '"candidate_id": "HCS-C331",\n  "candidate_id": "duplicate",', 1),
        raw_json.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1),
    )):
        path = directory / f"parser-{index}.json"; path.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0:
            raise AssertionError(f"JSON parser mutation survived: {index}")
        attempts += 1
    raw_yaml = evaluation_path.read_text()
    yaml_attacks = (
        raw_yaml.replace("HCS-C331", "HCS-C330", 1),
        raw_yaml.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1),
        raw_yaml.replace("A0_WEAK_ARITHMETIC_RELATION", "A0_FAIL", 1),
        raw_yaml.replace("A1_WEAK", "A1_PASS_ANALYTIC", 1),
        raw_yaml.replace("A4_NATURAL_QUANTIZATION", "A4_FAIL", 1),
        raw_yaml.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1),
        raw_yaml.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "BAD_SCOPE", 1),
        raw_yaml.replace("  - THEOREM_PACKAGE.md", "  - WRONG.md", 1),
        raw_yaml.replace("artifact_paths:\n  - results", "artifact_paths: results", 1),
        raw_yaml + "candidate_id: duplicate\n",
        "base: &base\n  verdict: A0_FAIL\ncopy: *base\n" + raw_yaml,
        raw_yaml.replace("a0:\n", "a0:\n  <<: {verdict: A0_FAIL}\n", 1),
        raw_yaml.replace("candidate_id: HCS-C331", "1: HCS-C331", 1),
        raw_yaml.replace("theorem_status: PROVABLE_AS_STATED", "unknown_field: x\ntheorem_status: PROVABLE_AS_STATED", 1),
        raw_yaml.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong.md", 1),
        raw_yaml.replace("  evidence_status: PROVED\n", "", 1),
        raw_yaml.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1),
        raw_yaml.replace("  - 10.1103/PhysRevD.16.1018", "  - 10.0000/fake", 1),
    )
    for index, changed in enumerate(yaml_attacks):
        path = directory / f"evaluation-{index}.yaml"; path.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evaluation", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0:
            raise AssertionError(f"YAML mutation survived: {index}")
        attempts += 1

print(f"C331 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
