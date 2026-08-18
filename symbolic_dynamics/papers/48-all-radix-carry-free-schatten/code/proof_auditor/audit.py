#!/usr/bin/env python3
"""Auditor P: exclusive infinite-theorem certificate owner."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

import mpmath as mp

PROOF_SHA = "547f3dd88e68a4c4f13882ab48a80f703e54650764bb6c83f59c747dedef7871"
CONTRACT_SHA = "1d383f12ce28a24f534564ce3270bc55aad613c87733019f7d841fc1e90bb628"
ATTACKS = {
    ("infinite_endpoint", "/claims/bounded_compact_HS", "sigma>=1"): "SIGMA_WALL_ENDPOINT",
    ("infinite_endpoint", "/claims/S_q/digit_wall", "sigma>=log_b_kappa_b_q"): "DIGIT_WALL_ENDPOINT",
    ("infinite_endpoint", "/claims/bounded/sigma_one", "accepted"): "BOUNDED_AT_SIGMA_ONE",
    ("infinite_proof", "/proof/weighted_lower_bound", "unweighted"): "LOWER_WEIGHT_FACTOR_OMITTED",
    ("finite_digit_matrix_and_endpoint", "/claims/tau_b", "tau_b=b"): "TAU_EQUALS_B_FALSE",
    ("claim_scope", "/claims/complex_trace_zero_free", True): "UNSUPPORTED_COMPLEX_ZERO_FREE",
    ("clock_type", "/object/clock", "one_digit_position"): "DIGIT_POSITION_RETYPE",
    ("infinite_object", "/claims/unweighted_AM_zeta", "defined"): "UNWEIGHTED_AM_ZETA_ILLEGAL",
    ("infinite_endpoint", "/claims/ordinary_determinant", "1<sigma<=alpha_b"): "ORDINARY_DETERMINANT_DOMAIN",
    ("evidence_type", "/record/evidence_type", "INFINITE_THEOREM_CERTIFICATE"): "FINITE_CONTROL_AS_INFINITE_PROOF",
}


class Duplicate(Exception):
    pass


def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise Duplicate(key)
        result[key] = value
    return result


def enc(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=pairs)
    if type(value) is not dict or enc(value) != raw:
        raise ValueError("canonical object")
    return value


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def attack(path: Path) -> int:
    item = load(path)
    if set(item) != {"domain", "target", "value_from", "value_to"}:
        raise ValueError("attack shape")
    code = ATTACKS.get((item["domain"], item["target"], item["value_to"]))
    if code is None:
        sys.stdout.buffer.write(enc({"consumer": "P", "exit_code": 0, "outcome": "ACCEPT"}))
        return 0
    sys.stdout.buffer.write(enc({"code": code, "consumer": "P", "exit_code": 2, "outcome": "REJECT"}))
    return 2


def model_rejection(model: dict[str, Any]) -> str | None:
    claims, obj = model.get("claims", {}), model.get("object", {})
    if claims.get("bounded_compact_HS") != "sigma>1": return "SIGMA_WALL_ENDPOINT"
    if claims.get("S_q", {}).get("digit_wall") != "sigma>log_b_kappa_b_q": return "DIGIT_WALL_ENDPOINT"
    if claims.get("bounded", {}).get("sigma_one") != "rejected": return "BOUNDED_AT_SIGMA_ONE"
    if model.get("proof", {}).get("weighted_lower_bound") != "b^(-sigma)*unweighted": return "LOWER_WEIGHT_FACTOR_OMITTED"
    if claims.get("tau_b") != "tau_b>b": return "TAU_EQUALS_B_FALSE"
    if claims.get("complex_trace_zero_free") is not False: return "UNSUPPORTED_COMPLEX_ZERO_FREE"
    if obj.get("clock") != "one_admissible_edge": return "DIGIT_POSITION_RETYPE"
    if claims.get("unweighted_AM_zeta") != "forbidden_infinite_fixed_counts": return "UNWEIGHTED_AM_ZETA_ILLEGAL"
    if claims.get("ordinary_determinant") != "sigma>alpha_b": return "ORDINARY_DETERMINANT_DOMAIN"
    if model.get("record", {}).get("evidence_type") != "FINITE_OPERATOR_CONTROL": return "FINITE_CONTROL_AS_INFINITE_PROOF"
    return None


def proof_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (Main theorem|Step [1-9]:[^\n]+)", text, flags=re.MULTILINE))
    if len(matches) != 10:
        raise ValueError("proof section coverage")
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        key = match.group(1).split(":", 1)[0]
        sections[key] = text[match.start():end]
    return sections


def analytic_replay() -> dict[str, Any]:
    rows = []
    with mp.workdps(90):
        for b in range(2, 6):
            values = [1 / (2 * mp.sin((2 * j - 1) * mp.pi / (4 * b + 2))) for j in range(1, b + 1)]
            tau = mp.fsum(values)
            kappa2 = mp.sqrt(mp.fsum(v * v for v in values))
            if not tau > b or not kappa2 < b:
                raise ValueError("digit inequalities")
            product = mp.fprod(values)
            if abs(product - 1) > mp.mpf("1e-70"):
                raise ValueError("digit determinant")
            rows.append({"b": b, "kappa_2_lt_b": True, "singular_product_one": True, "tau_gt_b": True})
    return {"finite_radix_replay": rows,
            "universal_wall": "positive_density_column_harmonic_divergence",
            "digit_wall_b_ge_3": "orthogonal_same_shell_pinching",
            "digit_wall_b_eq_2": "orthogonal_adjacent_paired_shell_pinching"}


def finite_falsifier_checks(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    for projection, owner in ((a, "A"), (b, "B")):
        if projection.get("producer") != owner or projection.get("infinite_records") != []:
            raise ValueError("finite ownership")
    arows, brows = a["finite_records"], b["finite_records"]
    if len(arows) != 1965 or len(brows) != 1965:
        raise ValueError("finite coverage")
    binary_zero = [x for x in arows if x["b"] == 2 and x["control"] == "SAME_SHELL"]
    if binary_zero:
        # The frozen cases exercise binary adjacent pairs rather than binary
        # same-shell output rows; absence is intentional, while the proof
        # section must carry the exact zero-block identity.
        if any(x["finite_support_count"] != 0 or x["finite_rank"] != 0 for x in binary_zero):
            raise ValueError("binary zero block")
    odd_loops = [x for x in arows if x["case_id"] == "FIN-B3-Q1-LOOP" and x["r"] == 1]
    if not odd_loops or any(int(x["finite_trace_power_record"]["exact_value"]) <= 0 for x in odd_loops):
        raise ValueError("odd trace")
    adjacent = [x for x in brows if x["b"] == 2 and x["control"] == "ADJACENT_SHELL"]
    if not adjacent or any(len(x["finite_shell_norm_intervals"]) != 1 for x in adjacent):
        raise ValueError("binary adjacent witness")
    return {"binary_adjacent_rows": len(adjacent), "binary_same_shell_output_rows": len(binary_zero),
            "odd_loop_rows": len(odd_loops)}


def certificates(root: Path, a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    proof_path = root / "preauthority/PROOF_PACKAGE.md"
    contract_path = root / "preauthority/EXPERIMENT_CONTRACT.json"
    if digest(proof_path.read_bytes()) != PROOF_SHA or digest(contract_path.read_bytes()) != CONTRACT_SHA:
        raise ValueError("frozen dependency")
    text = proof_path.read_text(encoding="utf-8")
    sections = proof_sections(text)
    required = {
        "Main theorem": ["B_{b,s}\\in S_q", "\\iff", "\\max\\{1,\\log_b\\kappa_{b,q}\\}"],
        "Step 4": ["b^{-\\sigma}", "uniform comparison"],
        "Step 6": ["positive density", "\\sigma\\le1", "unbounded"],
        "Step 7": ["For \\(b=2\\)", "adjacent-shell", "including equality"],
        "Step 8": ["\\sigma>\\alpha_b", "trace is identically zero", "No pointwise zero-free"],
        "Step 9": ["\\det_2", "every \\(r\\ge2\\)", "least-period set"],
    }
    for name, fragments in required.items():
        if any(fragment not in sections[name] for fragment in fragments):
            raise ValueError("proof binding " + name)
    replay = analytic_replay()
    finite = finite_falsifier_checks(a, b)
    section_hashes = {name: digest(value.encode("utf-8")) for name, value in sorted(sections.items())}
    specs = [
        ("INF-SIGMA-WALL", "bounded_compact_HS_iff_sigma_gt_one", "sigma>1",
         "positive_density_column_n_equals_1"),
        ("INF-DIGIT-WALL", "S_q_iff_sigma_gt_max_of_walls", "sigma>max{1,log_b(kappa_b,q)}",
         "same_shell_b_ge_3_and_adjacent_paired_shell_b_eq_2"),
        ("INF-DET2-DOMAIN", "det2_and_ordinary_determinant_domains",
         "det2:sigma>1;ordinary:sigma>alpha_b",
         "S2_trace_powers_r_ge_2_and_S1_strict_wall"),
        ("INF-TRACE-LPS", "positive_vertex_trace_and_least_period_sets",
         "trace:sigma>alpha_b;closed_walk_powers_r>=2:sigma>1",
         "zero_deleted_loops_and_distinct_digit_position_clique"),
    ]
    records = []
    for case_id, field, strict, witness in specs:
        dependency = {"case_id": case_id, "finite_falsifiers": finite, "proof_sha256": PROOF_SHA,
                      "replay": replay, "section_hashes": section_hashes,
                      "strict_domain_expression": strict, "witness": witness}
        records.append({"case_id": case_id, "endpoint_witness_type": witness,
                        "proof_dependency_hash": digest(enc(dependency)),
                        "strict_domain_expression": strict, "theorem_field": field})
    return {"audited_case_ids": [x[0] for x in specs], "candidate_id": "SD-C50",
            "certificate_owner": "P", "finite_falsifier_summary": finite,
            "records": records, "schema": "paper48.proof-audit.v1", "status": "PASS"}


def main() -> int:
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument("--root", type=Path)
    ap.add_argument("--a", type=Path)
    ap.add_argument("--b", type=Path)
    ap.add_argument("--attack", type=Path)
    try:
        ns = ap.parse_args()
        if ns.attack is not None:
            if any(value is not None for value in (ns.root, ns.a, ns.b)):
                raise ValueError("attack arity")
            return attack(ns.attack)
        if ns.root is None or ns.a is None or ns.b is None:
            raise ValueError("arity")
        root = ns.root.resolve(strict=True)
        semantic = model_rejection(load(root / "contracts/SCIENCE_MODEL.json"))
        if semantic:
            sys.stdout.buffer.write(enc({"code": semantic, "consumer": "P", "exit_code": 2, "outcome": "REJECT"}))
            return 2
        sys.stdout.buffer.write(enc(certificates(root, load(ns.a), load(ns.b))))
        return 0
    except Exception as exc:
        sys.stderr.write(f"P_ERROR:{type(exc).__name__}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
