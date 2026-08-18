#!/usr/bin/env python3
"""Build the canonical typed P46 source packet from the sole frozen input."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


PREAUTH_MANIFEST_SHA256 = "fc132644764bb93927dbcd5cbf63917e48e2c512d72adc375ef7590210226bab"
RAW_CASE_SHA256 = "b07dd9541612ea31dc23c0137aac49acf8d2ce07d0df2cdce17721d273f61172"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def safe(root: Path, relative: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    base = root.resolve(strict=True)
    cursor = root
    for component in relative.split("/"):
        if component in {"", ".", ".."}:
            raise ValueError("unsafe path")
        cursor /= component
        if cursor.is_symlink():
            raise ValueError("symlink forbidden")
    result = cursor.resolve(strict=True)
    if base not in result.parents or not result.is_file():
        raise ValueError("path containment")
    return result


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verified_manifest(root: Path) -> list[dict[str, str]]:
    manifest = safe(root, "preauthority/SHA256SUMS.txt")
    raw = manifest.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PREAUTH_MANIFEST_SHA256:
        raise ValueError("preauthority seal")
    rows: list[dict[str, str]] = []
    names: list[str] = []
    for line in raw.decode("ascii").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if not match:
            raise ValueError("manifest row")
        expected, name = match.groups()
        if name == "SHA256SUMS.txt":
            raise ValueError("manifest must self-exclude")
        path = safe(root, "preauthority/" + name)
        observed = digest(path)
        if observed != expected:
            raise ValueError("frozen input drift")
        names.append(name)
        rows.append({"path": "preauthority/" + name, "sha256": observed})
    if len(rows) != 15 or names != sorted(names) or len(names) != len(set(names)):
        raise ValueError("manifest exact set/order")
    actual = sorted(path.name for path in (root / "preauthority").iterdir()
                    if path.is_file() and path.name != "SHA256SUMS.txt")
    if actual != names:
        raise ValueError("preauthority extra/missing file")
    return rows


def provenance(state: str, commit: str | None) -> dict[str, str]:
    if state == "A":
        if commit is not None:
            raise ValueError("State A forbids commit argument")
        value = PENDING
    else:
        if commit is None or not re.fullmatch(r"[0-9a-f]{40}", commit) or commit == "0" * 40:
            raise ValueError("State B commit")
        value = commit
    return {"code_commit": value, "source_commit": value, "source_lock_code_commit": value}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--state", choices=["A", "B"], required=True)
    parser.add_argument("--commit")
    args = parser.parse_args()
    root = Path(args.root)
    rows = verified_manifest(root)
    raw_case = safe(root, "contracts/RAW_CASE_CONTRACT.json")
    if digest(raw_case) != RAW_CASE_SHA256:
        raise ValueError("raw case contract drift")
    packet = {
        "payload": {
            "candidate_id": "SD-C48",
            "case_contract_sha256": RAW_CASE_SHA256,
            "clock": "ONE_EDGE",
            "determinant_domains": {
                "det2": "Re(s)>1/2",
                "ordinary": "Re(s)>1",
            },
            "edge_label_type": "DERIVED_DYADIC_CONSTRAINT",
            "frozen_input_rows": rows,
            "loops": "RETAINED",
            "marker": "z_PER_EDGE",
            "operator": "H_s_ON_ell2_POSITIVE_INTEGERS",
            "ownership": {
                "fournier_wagner_novelty_credit": 0,
                "fournier_wagner_owns": [
                    "alternating_lacunary_representation",
                    "reflection_and_folding_relations",
                    "Schur_lacunary_boundedness_machinery"
                ],
                "paper46_residue": [
                    "complete_positive_odd_even_cycle_closure",
                    "exact_weighted_v2_direct_sum",
                    "legal_trace_and_det2_ledger"
                ]
            },
            "preauthority_manifest_sha256": PREAUTH_MANIFEST_SHA256,
            "primitive_type": "LEAST_PERIOD_CLOSED_VERTEX_CYCLE",
            "provenance": provenance(args.state, args.commit),
            "state": args.state,
            "support": "m+n=2^a_FOR_INTEGER_a>=1",
            "valuation_weight": "2^(-k*r*s)",
        },
        "schema": "paper46-source-packet-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
