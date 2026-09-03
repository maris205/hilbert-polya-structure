#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C330."""
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
EVIDENCE = ROOT / "results/c330_romik_pythagorean_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C330/2026-09-03.yaml"
CHECKER = ROOT / "code/c330_romik_pythagorean_checker.py"
PRODUCER = ROOT / "code/c330_romik_pythagorean_producer.py"


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence, evaluation):
    with tempfile.TemporaryDirectory(prefix="c330-mutation-") as directory:
        root = Path(directory)
        ep, yp = root / "evidence.json", root / "evaluation.yaml"
        ep.write_bytes(evidence)
        yp.write_bytes(evaluation)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        result = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep),
                                 "--evaluation", str(yp)], env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        return result.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C330 mutation lane refuses optimized Python")
    original = json.loads(EVIDENCE.read_text())
    yaml_bytes = EVALUATION.read_bytes()
    cases = []

    def add(name, edit):
        value = copy.deepcopy(original)
        edit(value)
        repair(value)
        rendered = (json.dumps(value, sort_keys=True, separators=(",", ":"),
                               ensure_ascii=False) + "\n").encode()
        cases.append((name, rendered, yaml_bytes))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C329"))
    add("obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O313"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("date", lambda d: d.__setitem__("evaluation_date", "2026-09-04"))
    add("root-extra", lambda d: d.__setitem__("extra", 1))
    add("coordinate", lambda d: d["model"].__setitem__("coordinate", "different"))
    add("primary-orientation", lambda d: d["model"].__setitem__("primary_orientation", "both leg orders"))
    add("mirror", lambda d: d["model"].__setitem__("mirror_orientation", "merged"))
    add("phase-space", lambda d: d["model"].__setitem__("irrational_phase_space", "all reals"))
    add("forward", lambda d: d["model"]["forward_branches"].__setitem__(0, "wrong"))
    add("inverse", lambda d: d["model"]["inverse_branches"].__setitem__(1, "wrong"))
    add("endpoint", lambda d: d["model"].__setitem__("endpoint_convention", "endpoints periodic"))
    add("tree-contract", lambda d: d["theorem_contract"].__setitem__("tree", "numerical"))
    add("periodic-contract", lambda d: d["theorem_contract"].__setitem__("periodic", "all words"))
    add("count-contract", lambda d: d["theorem_contract"].__setitem__("counts", "3^n"))
    add("zeta-contract", lambda d: d["theorem_contract"].__setitem__("zeta", "target zeta"))
    add("grid-depth", lambda d: d["finite_grid"].__setitem__("max_word_depth", 7))
    add("word-drop", lambda d: d["word_rows"].pop())
    add("word-duplicate", lambda d: d["word_rows"].append(copy.deepcopy(d["word_rows"][-1])))
    add("word-extra", lambda d: d["word_rows"][0].__setitem__("extra", 1))
    add("word-coordinate", lambda d: d["word_rows"][1].__setitem__("word", "1"))
    add("triple", lambda d: d["word_rows"][5]["pythagorean_triple"].__setitem__(0, 1))
    add("matrix", lambda d: d["word_rows"][10]["mobius_matrix_row_major"].__setitem__(0, 99))
    add("determinant", lambda d: d["word_rows"][20].__setitem__("determinant", 0))
    add("trace", lambda d: d["word_rows"][30].__setitem__("trace", 0))
    add("discriminant", lambda d: d["word_rows"][40].__setitem__("discriminant", 0))
    add("cylinder-truncate", lambda d: d["word_rows"][50]["cylinder_endpoints"].pop())
    add("polynomial", lambda d: d["word_rows"][60]["fixed_polynomial_low_to_high"].__setitem__(0, 0))
    add("classification", lambda d: d["word_rows"][100].__setitem__("fixed_point_class", "rational"))
    add("least-period", lambda d: d["word_rows"][200].__setitem__("least_word_period", 99))
    add("multiplier", lambda d: d["word_rows"][500].__setitem__("expanding_multiplier", "1"))
    add("late-triple", lambda d: d["word_rows"][-1]["pythagorean_triple"].__setitem__(2, 1))
    add("period-drop", lambda d: d["period_count_rows"].pop())
    add("period-extra", lambda d: d["period_count_rows"][0].__setitem__("extra", 1))
    add("fixed-count", lambda d: d["period_count_rows"][5].__setitem__("fixed_points", 729))
    add("primitive-count", lambda d: d["period_count_rows"][7].__setitem__("primitive_oriented_cycles", 1))
    add("collision", lambda d: d["collision_boundary"].__setitem__("C193", "same"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "PPTs are prime orbits"))
    add("reference", lambda d: d["references"][0].__setitem__("identifier", "wrong"))
    add("route", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_STRUCTURAL_ARITHMETIC_RELATION"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope", lambda d: d["scope_flags"].__setitem__("claims_target_zero_match", True))
    add("yaml-path", lambda d: d["route_a_yaml"].__setitem__("relative_path", "wrong.yaml"))
    add("yaml-semantic", lambda d: d["route_a_yaml"].__setitem__("semantic_sha256", "0" * 64))
    add("enumeration", lambda d: d["enumeration"].__setitem__("word_rows", 1))
    raw = EVIDENCE.read_text()
    cases.extend([
        ("json-duplicate", raw.replace('"candidate_id": "HCS-C330",', '"candidate_id": "HCS-C330",\n  "candidate_id": "HCS-C330",', 1).encode(), yaml_bytes),
        ("json-nonfinite", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1).encode(), yaml_bytes),
        ("json-root", b"[]\n", yaml_bytes),
    ])
    text = EVALUATION.read_text()
    yaml_cases = [
        ("yaml-duplicate", text + "candidate_id: HCS-C330\n"),
        ("yaml-alias", "probe: &p 1\ncopy: *p\n" + text),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + text),
        ("yaml-nonstring", "1: bad\n" + text),
        ("yaml-root", "- bad\n"),
        ("yaml-timestamp", text.replace('evaluation_date: "2026-09-03"', "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown", text + "unknown: bad\n"),
        ("yaml-missing", text.replace("training_data: none\n", "", 1)),
        ("yaml-epoch-type", text.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-route-type", text.replace("route_b_invocation_allowed: false", 'route_b_invocation_allowed: "false"', 1)),
        ("yaml-authority", text.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong", 1)),
        ("yaml-status", text.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-verdict", text.replace("overall_verdict: ROUTE_A_EXPLORATORY", "overall_verdict: ROUTE_A_ACCEPTED", 1)),
        ("yaml-theorem", text.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NUMERICAL_ONLY", 1)),
        ("yaml-schema", text.replace("schema: route-a-evaluation-v0.2.0", "schema: wrong", 1)),
        ("yaml-artifact", text.replace("  - THEOREM_PACKAGE.md", "  - WRONG.md", 1)),
        ("yaml-a1", text.replace("  verdict: A1_PASS_ANALYTIC", "  verdict: A1_WEAK", 1)),
        ("yaml-finite-role", text.replace("exact finite-word regression audit only, never proof by finite extrapolation", "finite grid proves theorem", 1)),
        ("yaml-route-reason", text.replace("exploratory Route A status does not authorize Route B under the scope firewall", "Route B authorized", 1)),
        ("yaml-normalization", text.replace("primary tree has odd first leg and even second leg; leg swap is a separate mirror orientation", "both orientations merged", 1)),
        ("yaml-source-token", text.replace("  - arXiv:math/0406512", "  - arXiv:wrong", 1)),
        ("yaml-candidate", text.replace("Romik three-branch interval map with the odd-first even-second primitive Pythagorean tree rooted at (3,4,5) and its irrational periodic subsystem", "different map", 1)),
        ("yaml-scope", text.replace("  claims_automorphy: false", "  claims_automorphy: true", 1)),
    ]
    cases.extend((name, EVIDENCE.read_bytes(), mutated.encode()) for name, mutated in yaml_cases)
    survived = [name for name, evidence, evaluation in cases if not rejected(evidence, evaluation)]
    if survived:
        raise AssertionError(f"mutations survived: {survived}")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for script in (PRODUCER, CHECKER):
        if subprocess.run([sys.executable, "-O", str(script)], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            raise AssertionError("optimized mode survived")
    print(f"C330 hostile mutation suite: PASS ({len(cases)}/{len(cases)} rejected; optimized mode rejected)")


if __name__ == "__main__":
    main()
