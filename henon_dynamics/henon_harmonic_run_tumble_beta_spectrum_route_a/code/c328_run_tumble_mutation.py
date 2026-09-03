#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C328."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C328 mutation lane refuses optimized Python")

root = Path(__file__).resolve().parents[1]
evidence_path = root / "results/c328_run_tumble_evidence.json"
evaluation_path = root / "evaluations/route_a/HCS-C328/2026-09-03.yaml"
checker = root / "code/c328_run_tumble_checker.py"
source = json.loads(evidence_path.read_text())


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def swap_resonance_class(data):
    data["parameter_rows"][0]["resonance_class"] = "even_integer_semisimple"


mutators = [
    lambda d: d.__setitem__("candidate_id", "HCS-C327"),
    lambda d: d.__setitem__("source_commit", "0"*40),
    lambda d: d.__setitem__("evaluation_date", "2026-09-02"),
    lambda d: d["evaluation_lock"].__setitem__("semantic_sha256", "0"*64),
    lambda d: d["evaluator"].__setitem__("authority", "wrong/authority.md"),
    lambda d: d["scope_flags"].__setitem__("claims_target_euler_factors", True),
    lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
    lambda d: d["model"].__setitem__("extra", "unowned"),
    lambda d: d["theorem_contract"].__setitem__("full_L2_spectrum", "claimed"),
    lambda d: d["theorem_contract"].__setitem__("correlation", "R(t)=exp(A*t)*Sigma for every real t"),
    lambda d: d["parameter_rows"][0].__setitem__("alpha_lambda_over_mu", "2/4"),
    lambda d: d["parameter_rows"][1].__setitem__("beta_normalization_y", "nan"),
    lambda d: d["parameter_rows"][2].__setitem__("extra", 1),
    lambda d: d["parameter_rows"][3]["moments"].__setitem__(1, copy.deepcopy(d["parameter_rows"][3]["moments"][0])),
    lambda d: d["parameter_rows"][4]["moments"].pop(),
    lambda d: d["parameter_rows"][4]["moments"][2].__setitem__("sigma_even_position_moment", "1"),
    lambda d: d["parameter_rows"][5]["correlations"][1].__setitem__("xx", "nan"),
    lambda d: d["parameter_rows"][0]["resonances"][0].__setitem__("geometric_multiplicity", 2),
    lambda d: d["parameter_rows"][1]["resonances"][0].__setitem__("geometric_multiplicity", 1),
    swap_resonance_class,
    lambda d: d["parameter_rows"].__setitem__(7, copy.deepcopy(d["parameter_rows"][6])),
    lambda d: d["enumeration"].__setitem__("extra", 1),
    lambda d: d["boundary_atlas"].pop(),
    lambda d: d["references"][0].__setitem__("doi", "10.0000/fake"),
]

attempts = 0
with tempfile.TemporaryDirectory(prefix="c328-mutations-") as directory:
    directory = Path(directory)
    for index, mutate in enumerate(mutators):
        for repaired in (False, True):
            data = copy.deepcopy(source)
            mutate(data)
            if repaired:
                repair(data)
            path = directory / f"evidence-{index}-{int(repaired)}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
            run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)],
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode == 0:
                raise AssertionError(f"evidence mutation survived: {index}/{repaired}")
            attempts += 1

    raw_json = evidence_path.read_text()
    parser_attacks = (
        raw_json.replace('"candidate_id": "HCS-C328",', '"candidate_id": "HCS-C328",\n  "candidate_id": "duplicate",', 1),
        raw_json.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1),
    )
    for index, changed in enumerate(parser_attacks):
        path = directory / f"parser-{index}.json"
        path.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)],
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0:
            raise AssertionError(f"JSON parser mutation survived: {index}")
        attempts += 1

    raw_yaml = evaluation_path.read_text()
    yaml_attacks = (
        raw_yaml.replace("HCS-C328", "HCS-C327", 1),
        raw_yaml.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1),
        raw_yaml.replace("A0_FAIL", "A0_ANALYTIC_ARITHMETIC_ORIGIN", 1),
        raw_yaml.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1),
        raw_yaml.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "BAD_SCOPE", 1),
        raw_yaml.replace("  - THEOREM_PACKAGE.md", "  - WRONG.md", 1),
        raw_yaml.replace("artifact_paths:\n  - results", "artifact_paths: results", 1),
        raw_yaml + "candidate_id: duplicate\n",
        "base: &base\n  verdict: A0_FAIL\ncopy: *base\n" + raw_yaml,
        raw_yaml.replace("a0:\n", "a0:\n  <<: {verdict: A0_FAIL}\n", 1),
        raw_yaml.replace("candidate_id: HCS-C328", "1: HCS-C328", 1),
        raw_yaml.replace("theorem_status: PROVABLE_AS_STATED", "unknown_field: x\ntheorem_status: PROVABLE_AS_STATED", 1),
        raw_yaml.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong/authority.md", 1),
        raw_yaml.replace("  evidence_status: PROVED\n", "", 1),
        raw_yaml.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1),
        raw_yaml.replace("  - 10.1088/1742-5468/ac014d", "  - 10.0000/fake", 1),
    )
    for index, changed in enumerate(yaml_attacks):
        path = directory / f"evaluation-{index}.yaml"
        path.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evaluation", str(path)],
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0:
            raise AssertionError(f"YAML mutation survived: {index}")
        attempts += 1

print(f"C328 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
