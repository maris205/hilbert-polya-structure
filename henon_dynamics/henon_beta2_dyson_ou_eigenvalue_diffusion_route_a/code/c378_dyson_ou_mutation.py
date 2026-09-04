#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C378."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c378 mutation suite refuses optimized Python")

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c378_dyson_ou_checker.py"
EVIDENCE = ROOT / "results/c378_dyson_ou_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C378/2026-09-04.yaml"
TEX = ROOT / "paper/main.tex"
SECTIONS = ("dimension_rows", "level_rows", "partition_rows", "kernel_rows")
ROUND_TITLES = (
    "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion: Matrix Radialization and Ordered GUE Equilibrium",
    "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion: Exact Chamber Kernel and Noncollision",
    "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion: Exact Chamber Kernel and Complete Partition Spectrum",
)
ROUND_TITLE_SUFFIXES = (
    "Matrix Radialization and Ordered GUE Equilibrium",
    "Exact Chamber Kernel and Noncollision",
    "Exact Chamber Kernel and Complete Partition Spectrum",
)


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def encode(value):
    for section in SECTIONS:
        value["section_sha256"][section] = hashlib.sha256(canonical(value[section])).hexdigest()
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n"


def run(evidence_blob=None, yaml_blob=None):
    with tempfile.TemporaryDirectory(prefix="c378-mutation-") as directory:
        evidence_path = Path(directory) / "evidence.json"
        yaml_path = Path(directory) / "evaluation.yaml"
        evidence_path.write_bytes(EVIDENCE.read_bytes() if evidence_blob is None else evidence_blob)
        yaml_path.write_bytes(EVALUATION.read_bytes() if yaml_blob is None else yaml_blob)
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--input", str(evidence_path), "--evaluation", str(yaml_path)],
            capture_output=True, text=True,
        ).returncode


def round_title_contract(flat_text: str, round_index: int) -> bool:
    return (
        ROUND_TITLES[round_index] in flat_text
        and all(
            suffix not in flat_text
            for other_index, suffix in enumerate(ROUND_TITLE_SUFFIXES)
            if other_index != round_index
        )
    )


def main():
    argparse.ArgumentParser().parse_args()
    base = json.loads(EVIDENCE.read_text())
    assert run() == 0
    attacks = []

    def add(label, mutation):
        value = copy.deepcopy(base)
        mutation(value)
        attacks.append((label, encode(value)))

    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O000"))
    add("source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BROKEN"))
    add("authority", lambda x: x["evaluator"].__setitem__("authority", "wrong"))
    add("authority-sha", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("yaml-path", lambda x: x["route_a_yaml"].__setitem__("relative_path", "wrong"))
    add("yaml-raw", lambda x: x["route_a_yaml"].__setitem__("raw_sha256", "0" * 64))
    add("matrix-sde", lambda x: x["conventions"].__setitem__("matrix_sde", "wrong covariance"))
    add("eigenvalue-sde", lambda x: x["conventions"].__setitem__("eigenvalue_sde", "wrong drift"))
    add("variance", lambda x: x["conventions"].__setitem__("scalar_ou_contraction", "variance=1-r"))
    add("normalizer", lambda x: x["conventions"].__setitem__("normalizer", "missing factorial"))
    add("doob", lambda x: x["theorem_contract"].__setitem__("doob_kernel", "missing energy shift"))
    add("boundary", lambda x: x["theorem_contract"].__setitem__("boundary", "collisions allowed"))
    add("spectrum", lambda x: x["theorem_contract"].__setitem__("spectrum", "integer spectrum"))
    add("gap", lambda x: x["theorem_contract"].__setitem__("gap", "gap=1"))
    add("collision-owner", lambda x: x["collision_boundary"].__setitem__("C306", "same owner"))
    add("reference", lambda x: x["references"][0].__setitem__("doi", "wrong"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(1, "GUE proves target zeros"))
    add("scope-flag", lambda x: x["scope_flags"].__setitem__("claims_target_zero_match", True))
    add("scope-bool-int", lambda x: x["scope_flags"].__setitem__("claims_root_number", 0))
    add("tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_ANALYTIC_ARITHMETIC_ORIGIN"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("theorem-status", lambda x: x["route_a"].__setitem__("theorem_status", "OPEN"))
    add("finite-role", lambda x: x.__setitem__("finite_evidence_role", "proof by sampling"))
    add("dimension", lambda x: x["dimension_rows"][7].__setitem__("hermitian_real_dimension", 63))
    add("degree-shift", lambda x: x["dimension_rows"][7].__setitem__("vandermonde_degree", 27))
    add("level-count", lambda x: x["level_rows"][64].__setitem__("partition_multiplicity", 0))
    add("level-eigenvalue", lambda x: x["level_rows"][10].__setitem__("generator_eigenvalue", {"numerator": -10, "denominator": 1}))
    add("partition-label", lambda x: x["partition_rows"][20]["partition"].__setitem__(0, 99))
    add("slater-index", lambda x: x["partition_rows"][100]["slater_indices"].__setitem__(0, 99))
    add("partition-norm", lambda x: x["partition_rows"][100].__setitem__("squared_norm", {"numerator": 1, "denominator": 1}))
    add("kernel-q", lambda x: x["kernel_rows"][0].__setitem__("killed_determinant_q_xy_decimal_50", "1.0"))
    add("kernel-k", lambda x: x["kernel_rows"][1].__setitem__("doob_kernel_k_xy_decimal_50", "1.0"))
    add("kernel-balance", lambda x: x["kernel_rows"][2].__setitem__("relative_detailed_balance_residual_decimal_50", "0.1"))
    add("extra-top", lambda x: x.__setitem__("unexpected", 1))
    add("missing-top", lambda x: x.pop("conventions"))

    killed = 0
    for label, blob in attacks:
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    stale = copy.deepcopy(base)
    stale["dimension_rows"][0]["spectral_gap"] = {"numerator": 1, "denominator": 1}
    stale_blob = json.dumps(stale, sort_keys=True, indent=2).encode() + b"\n"
    assert run(evidence_blob=stale_blob) != 0
    killed += 1

    raw = EVIDENCE.read_bytes()
    duplicate = raw.replace(b'{\n  "candidate_id"', b'{\n  "candidate_id": "evil",\n  "candidate_id"', 1)
    nonfinite = raw.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1)
    for label, blob in (("duplicate-json", duplicate), ("nonfinite-json", nonfinite)):
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    yaml_text = EVALUATION.read_text()
    yaml_attacks = [
        ("yaml-duplicate", yaml_text + "candidate_id: duplicate\n"),
        ("yaml-merge", "base: &b {x: 1}\nmerged: {<<: *b}\n" + yaml_text),
        ("yaml-nonstring", "1: bad\n" + yaml_text),
        ("yaml-date-type", yaml_text.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04")),
        ("yaml-unknown", yaml_text + "unknown_field: true\n"),
        ("yaml-epoch-type", yaml_text.replace("fixed_epoch: 1788480000", "fixed_epoch: '1788480000'")),
        ("yaml-tuple", yaml_text.replace("  - A4_FORMAL_HINT", "  - A4_NATURAL_QUANTIZATION")),
        ("yaml-route-b", yaml_text.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true")),
        ("yaml-skill", yaml_text.replace("skill: route-a-evaluator", "skill: wrong-evaluator")),
        ("yaml-skill-version", yaml_text.replace("skill_version: 0.2.0", "skill_version: 9.9.9")),
        ("yaml-code-commit", yaml_text.replace("code_commit: " + "f58422d8f03235329863f946654981ecb5d4dc97", "code_commit: " + "0" * 40)),
        ("yaml-arithmetic-control", yaml_text.replace("    - prime and composite matrix dimensions obey the same partition-spectrum theorem with no prime-specific term\n", "")),
        ("yaml-metric", yaml_text.replace("    target_tables_used: 0", "    target_tables_used: 1", 1)),
        ("yaml-claim-boundary", yaml_text.replace("claim_boundary: exact source-local", "claim_boundary: overclaimed global")),
        ("yaml-round2", yaml_text.replace("round2_clues:\n", "round2_clues: []\n# ", 1)),
        ("yaml-source-token", yaml_text.replace("DOI:10.1063/1.1703862", "DOI:wrong")),
        ("yaml-normalization", yaml_text.replace("minus one half of the matrix", "minus the matrix")),
    ]
    for label, text in yaml_attacks:
        assert run(yaml_blob=text.encode()) != 0, label
        killed += 1

    spacing_pattern = re.compile(r"(?<!\\)\b(?:quad|qquad)\b")
    clean_tex = TEX.read_text()
    assert spacing_pattern.search(clean_tex) is None
    assert spacing_pattern.search("x,quad y") is not None
    assert spacing_pattern.search("x,qquad y") is not None
    killed += 2

    assert round_title_contract(ROUND_TITLES[0], 0)
    generic_title = "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion"
    future_title_leak = ROUND_TITLES[0] + " " + ROUND_TITLE_SUFFIXES[2]
    assert not round_title_contract(generic_title, 0)
    assert not round_title_contract(future_title_leak, 0)
    killed += 2

    expected = len(attacks) + 3 + len(yaml_attacks) + 4
    assert killed == expected
    print(f"C378 mutation PASS: killed={killed}/{expected} repaired_hash_attacks={len(attacks)}")


if __name__ == "__main__":
    main()
