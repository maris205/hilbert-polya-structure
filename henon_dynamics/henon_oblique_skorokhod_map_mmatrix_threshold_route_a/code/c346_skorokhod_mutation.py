#!/usr/bin/env python3
"""Repaired-hash hostile mutations for HCS-C346."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C346 mutation lane refuses optimized Python")
root = Path(__file__).resolve().parents[1]
evidence_path = root / "results/c346_skorokhod_evidence.json"
evaluation_path = root / "evaluations/route_a/HCS-C346/2026-09-03.yaml"
checker = root / "code/c346_skorokhod_checker.py"
source = json.loads(evidence_path.read_text())


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


mutators = [
    lambda d: d.__setitem__("candidate_id", "HCS-C345"),
    lambda d: d.__setitem__("obstruction_id", "HEN-O329"),
    lambda d: d.__setitem__("source_commit", "0" * 40),
    lambda d: d.__setitem__("evaluation_date", "2026-09-02"),
    lambda d: d["evaluator"].__setitem__("authority", "wrong.md"),
    lambda d: d["evaluation_lock"].__setitem__("raw_sha256", "0" * 64),
    lambda d: d["scope_flags"].__setitem__("claims_target_euler_factors", True),
    lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_STRONG_CANDIDATE"),
    lambda d: d["theorem_contract"].__setitem__("sharp_threshold", "rho sigma <= 1"),
    lambda d: d["theorem_contract"].__setitem__("fixed_point", "fixed point with unconstrained initial regulator"),
    lambda d: d["references"][0].__setitem__("doi", "10.0000/fake"),
    lambda d: d["case_rows"][0].__setitem__("rho", "2/8"),
    lambda d: d["case_rows"][0].__setitem__("determinant", "1"),
    lambda d: d["case_rows"][1]["event_rows"][2].__setitem__("state", ["99", "0"]),
    lambda d: d["case_rows"][1]["event_rows"][3].__setitem__("regulator", ["99", "99"]),
    lambda d: d["case_rows"][2]["event_rows"][4].__setitem__("active_axes", []),
    lambda d: d["case_rows"][2]["event_rows"][5].__setitem__("nonnegative_and_complementary", False),
    lambda d: d["case_rows"][3].__setitem__("well_posed", False),
    lambda d: d["case_rows"][3].__setitem__("stretched_event_count", 11),
    lambda d: d["case_rows"][4].__setitem__("fixed_point_check", False),
    lambda d: d["case_rows"][0]["picard_rows"][2].__setitem__("successive_norm", "999"),
    lambda d: d["case_rows"][1]["picard_rows"][3].__setitem__("contraction_check", False),
    lambda d: d["threshold_rows"]["critical_nonuniqueness"][1].__setitem__("state", [["1", "0"]] * 3),
    lambda d: d["threshold_rows"]["negative_jump_nonexistence"][0].__setitem__("lcp_candidate_count", 1),
    lambda d: d["enumeration"].__setitem__("event_rows", 35),
    lambda d: d["case_rows"][5]["event_rows"].pop(),
]

attempts = 0
with tempfile.TemporaryDirectory(prefix="c346-mutations-") as directory:
    directory = Path(directory)
    for index, mutate in enumerate(mutators):
        for repaired in (False, True):
            data = copy.deepcopy(source)
            mutate(data)
            if repaired:
                repair(data)
            path = directory / f"evidence-{index}-{int(repaired)}.json"
            path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode == 0:
                raise AssertionError(f"evidence mutation survived: {index}/{repaired}")
            attempts += 1
    raw = evidence_path.read_text()
    parser_attacks = (
        raw.replace('"candidate_id": "HCS-C346",', '"candidate_id": "HCS-C346",\n  "candidate_id": "duplicate",', 1),
        raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1),
    )
    for index, changed in enumerate(parser_attacks):
        path = directory / f"parser-{index}.json"
        path.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evidence", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0:
            raise AssertionError(f"JSON parser mutation survived: {index}")
        attempts += 1
    raw = evaluation_path.read_text()
    yaml_attacks = (
        raw.replace("HCS-C346", "HCS-C345", 1),
        raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1),
        raw.replace("A0_FAIL", "A0_WEAK_ARITHMETIC_RELATION", 1),
        raw.replace("A4_FAIL", "A4_FORMAL_HINT", 1),
        raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1),
        raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "BAD_SCOPE", 1),
        raw.replace("  - THEOREM_PACKAGE.md", "  - WRONG.md", 1),
        raw.replace("artifact_paths:\n  - results", "artifact_paths: results", 1),
        raw + "candidate_id: duplicate\n",
        "base: &base\n  verdict: A0_FAIL\ncopy: *base\n" + raw,
        raw.replace("a0:\n", "a0:\n  <<: {verdict: A0_FAIL}\n", 1),
        raw.replace("candidate_id: HCS-C346", "1: HCS-C346", 1),
        raw.replace("theorem_status: PROVABLE_AS_STATED", "unknown_field: x\ntheorem_status: PROVABLE_AS_STATED", 1),
        raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong.md", 1),
        raw.replace("  evidence_status: PROVED\n", "", 1),
        raw.replace("  - 10.1080/17442509108833688", "  - 10.0000/fake", 1),
    )
    for index, changed in enumerate(yaml_attacks):
        path = directory / f"evaluation-{index}.yaml"
        path.write_text(changed)
        run = subprocess.run([sys.executable, "-B", str(checker), "--evaluation", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0:
            raise AssertionError(f"YAML mutation survived: {index}")
        attempts += 1
print(f"C346 hostile mutation suite: PASS ({attempts}/{attempts} rejected)")
