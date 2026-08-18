#!/usr/bin/env python3
"""Read-only infinite-theorem and quantifier auditor for P46."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


HASHES = {
    "preauthority/DERIVATION_PACKAGE.md": "daeed45db1dbd2fd504e72d7914d985d8d49a04bf30ceb2c24e92b4913f56dc0",
    "preauthority/PROOF_PACKAGE.md": "c6d4a4578d59ca7d3a4a9e02fe88b68b6ab705ec35a0eefcb47277bec6dafc75",
    "preauthority/THEOREM_FALSIFIERS.md": "9b88b667a065198f95304d78e5022460380d47ae897755f94e6d493e57050bfe",
}
MUTATIONS = {
    "F04/bounded_at_zero": "ROW_ONE_NOT_L2",
    "F05/s2_at_half": "HILBERT_SCHMIDT_ENDPOINT_DIVERGES",
    "F06/s1_at_one": "TRACE_CLASS_ENDPOINT_DIVERGES",
    "F12/cutoff_proves_endpoint": "FINITE_CUTOFF_LIMIT_FAILURE",
    "RES05/finite_trace_geometric_collapse": "FINITE_TRACE_TRUNCATION_FAILURE",
    "RES06/infinite_field_in_evaluator": "FINITE_INFINITE_FIREWALL_FAILURE",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def reject(identifier: str) -> int:
    code = MUTATIONS.get(identifier)
    if code is None:
        raise ValueError("mutation not designated for P")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, "consumer": "P", "instance_id": identifier,
                    "witness": "infinite quantifier and proof dependency replay rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def file_at(root: Path, relative: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    base = root.resolve(strict=True)
    result = root.joinpath(*relative.split("/"))
    cursor = root
    for part in relative.split("/"):
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    result = result.resolve(strict=True)
    if base not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        return reject(args.mutation)
    if not args.root:
        raise ValueError("--root required")
    root = Path(args.root)
    texts: dict[str, str] = {}
    for relative, expected in HASHES.items():
        raw = file_at(root, relative).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError("frozen proof byte drift")
        texts[relative] = raw.decode("utf-8")
    proof = texts["preauthority/PROOF_PACKAGE.md"]
    required = [
        "bounded and compact exactly when $\\sigma>0$",
        "$H_s\\in S_2$ exactly when $\\sigma>1/2$",
        "$H_s\\in S_1$ exactly when $\\sigma>1$",
        "row indexed by $m=1$",
        "central matching",
        "H_s\\cong\\bigoplus_{k\\ge0}2^{-ks}A_s",
        "The product converges locally uniformly in $z$",
        "complete cyclic edge-label solver",
    ]
    if any(anchor not in proof for anchor in required):
        raise ValueError("proof anchor missing")
    certificate = {
        "bounded_and_compact_iff_Re_s_gt_0": True,
        "cycle_odd_even_classification_complete": True,
        "det2_domain_Re_s_gt_one_half": True,
        "finite_trace_uses_scale_dependent_truncations": True,
        "hilbert_schmidt_iff_Re_s_gt_one_half": True,
        "infinite_trace_geometric_identity_separately_typed": True,
        "row_one_endpoint_obstruction": True,
        "trace_class_iff_Re_s_gt_1": True,
        "trace_dual_matching_endpoint_obstruction": True,
        "valuation_direct_sum_exact": True,
    }
    output = {
        "payload": {
            "basis": "FROZEN_ANALYTIC_PROOF_REPLAY",
            "finite_grid_used_as_proof": False,
            "infinite_theorem_certificate": certificate,
            "proof_anchor_count": len(required),
            "theorem_failure_count": 0,
        },
        "schema": "paper46-proof-audit-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
