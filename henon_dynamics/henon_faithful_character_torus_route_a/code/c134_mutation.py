#!/usr/bin/env python3
"""Repaired-hash plus stale-hash mutation suite for C134."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c134_character_evidence.json"
CHECKER = ROOT / "code/c134_character_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main():
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C134-forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("scope", ("scope_literal",), "ALLOW_FORBIDDEN_DATA"),
        ("A_lock", ("source_lock", "linear_part_A", 0, 0), "1/4"),
        ("family_lock", ("source_lock", "scaled_family"), "k=1 only"),
        ("clock_lock", ("source_lock", "clock"), "one primitive cycle per iterate"),
        ("normalization_lock", ("source_lock", "normalization"), "chi_u(m)=u^(2m)"),
        ("determinant_lock", ("source_lock", "determinant_convention"), "det(I+zL)"),
        ("precision_lock", ("source_lock", "precision"), "floating-point samples"),
        ("cutoff_lock", ("source_lock", "cutoff"), "theorem valid only through period 8"),
        ("q_anchor", ("frozen_family", "faithful_anchor_q", "real"), "0"),
        ("q_inverse", ("frozen_family", "q_inverse", "imag"), "4/5"),
        ("faithfulness", ("frozen_family", "faithfulness_certificate"), "q is a fifth root"),
        ("operator", ("frozen_family", "operator"), "FORGED_OPERATOR"),
        ("geometry", ("frozen_family", "geometry_theorem"), "FORGED_GEOMETRY"),
        ("k1_translation", ("frozen_family", "examples", "1", "translations", 0), "-3"),
        ("k6_radius", ("frozen_family", "examples", "6", "domain_radius"), "17"),
        ("symbolic_delta", ("frozen_family", "examples", "1", "symbolic_delta_z0_to_z3", 1, "-2"), "-1/3"),
        ("q_delta", ("frozen_family", "examples", "1", "q_delta_z0_to_z3", 1, "real"), "0"),
        ("hardy_trace", ("frozen_family", "examples", "1", "universal_hardy_traces_n1_to_8", "1", "-2"), "1"),
        ("fredholm", ("frozen_family", "examples", "1", "universal_fredholm_coefficients_z0_to_z8", 1, "-2"), "0"),
        ("trace_formula", ("all_order_operator", "trace_formula"), "FORGED_TRACE"),
        ("lattice_product", ("all_order_operator", "lattice_product"), "FORGED_PRODUCT"),
        ("primitive_product", ("all_order_operator", "primitive_product"), "FORGED_PRIMITIVE"),
        ("delta_general", ("universal_recovery", "symbolic_delta_general"), "FORGED_DELTA"),
        ("normalized_jet", ("universal_recovery", "normalized_log_jet"), "FORGED_JET"),
        ("newton_E1", ("universal_recovery", "newton_E1"), "E1=P1/2"),
        ("newton_E2", ("universal_recovery", "newton_E2"), "E2=(P1^2+P2)/2"),
        ("newton_E3", ("universal_recovery", "newton_E3"), "E3=(P1^3-3*P1*P2-2*P3)/6"),
        ("monomial_recovery", ("universal_recovery", "monomial_recovery", 0), "2*E1=1"),
        ("decode", ("universal_recovery", "decode"), "FORGED_DECODE"),
        ("recovery_theorem", ("universal_recovery", "strongest_theorem"), "complete arbitrary geometry recovery"),
        ("permutation_receipt", ("universal_recovery", "permutation_receipts", 0, "decoded_translations", 0), "99"),
        ("z5_alias", ("controls", "k1_vs_k6_z5_alias"), False),
        ("alias_reason", ("controls", "alias_reason"), "FORGED_ALIAS"),
        ("q_separation", ("controls", "k1_vs_k6_q_separated"), False),
        ("q_witness", ("controls", "q_separation_witness"), "FORGED_WITNESS"),
        ("labelled_boundary", ("controls", "labelled_parameter_boundary"), "UNLABELLED_PARAMETER_ORIENTATION_IS_RECOVERED"),
        ("precision_boundary", ("controls", "finite_precision_boundary"), "stable floating inversion"),
        ("geometry_boundary", ("controls", "geometry_boundary"), "arbitrary geometry recovered"),
        ("rooted_count", ("replay_prefix", "rooted_counts_n1_to_8", "8"), 999),
        ("progress", ("progress_and_boundary", "progress_over_C129"), "FORGED_PROGRESS"),
        ("A4_promotion", ("route_a", "tuple", 3), "A4_ROUTE_B_READY"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("scope_flag", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 0), "stable numeric recovery"),
        ("extra_key", ("frozen_family", "forged_headline"), "FORGED"),
    ]
    cases = [(name, path, value, True) for name, path, value in repaired]
    cases.append(("stale_payload_hash", ("payload_sha256",), "0" * 64, False))
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c134-mutations-") as tmp:
        for name, path, value, repair in cases:
            data = deepcopy(source)
            set_path(data, path, value)
            if repair:
                data["payload_sha256"] = payload_hash(data)
            candidate = Path(tmp) / f"{name}.json"
            candidate.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            completed = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
            if completed.returncode == 0:
                raise AssertionError(f"checker accepted mutation: {name}")
            rejected.append(name)
    print(json.dumps({"status": "C134_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(cases), "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
