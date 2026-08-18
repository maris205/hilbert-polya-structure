#!/usr/bin/env python3
"""Frozen-source, literature ownership, and provenance auditor S."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

EXPECTED_SEAL = "4053f398c8318d09a821907ce421cb34a2adbe88efa2ac4dbfdc059e54d1e849"


class SourceReject(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


SOURCE_ATTACKS = [
    (("provenance", "phase2_manifest_sha256"), "0" * 64, "PARENT_SEAL_MISMATCH"),
    (("sources", "Luan_Khoi", "doi"), "10.0000/wrong", "SOURCE_DOI_MISMATCH"),
    (("ownership", "weighted_composition"), "novel", "GENERIC_METHOD_NOVELTY"),
    (("ownership", "h_free_part"), "novel", "H_FREE_OBJECT_NOVELTY"),
    (("ownership", "internal_predecessors"), "P27_P29", "INTERNAL_SUBTRACTION_OMITTED"),
    (("ownership", "framing"), "completes_unfilled_P27_adjoint_task", "FALSE_OPEN_OBLIGATION"),
    (("ownership", "priority"), True, "PRIORITY_FROM_SEARCH_ABSENCE"),
    (("ownership", "external_sources"), "omitted", "ABANIN_MANNANIKOV_OMITTED"),
    (("controls", "free_UFD"), "positive_prime_evidence", "FREE_UFD_POSITIVE_PRIME_EVIDENCE"),
    (("scope", "all_h"), False, "H2_SINGLETON_PAPER_ADMISSION"),
]


def source_semantic_code(contract):
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "SOURCE_CONTRACT_SHAPE"
    for path, attacked, code in SOURCE_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "SOURCE_CONTRACT_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(root: Path):
    src = root / "inputs" / "preauthority"
    # Semantic ownership checks precede the physical seal check so a concrete
    # mutated claim receives its fixed diagnostic rather than a generic hash
    # failure.  The seal is still mandatory immediately afterwards.
    contract = json.loads((src / "EXPERIMENT_CONTRACT.json").read_text())
    semantic_code = source_semantic_code(contract)
    if semantic_code:
        raise SourceReject(semantic_code)
    manifest = src / "SHA256SUMS.txt"
    if sha(manifest) != EXPECTED_SEAL:
        raise ValueError("seal")
    lines = manifest.read_text(encoding="utf-8").splitlines()
    if len(lines) != 16 or lines != sorted(lines, key=lambda line: line.split("  ", 1)[1]) or len(set(lines)) != 16:
        raise ValueError("manifest shape")
    names = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if not match:
            raise ValueError("manifest syntax")
        checksum, name = match.groups()
        path = src / name
        if path.is_symlink() or not path.is_file() or sha(path) != checksum:
            raise ValueError("manifest member")
        names.append(name)
    actual = sorted(p.name for p in src.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt")
    if names != actual or len(list(src.iterdir())) != 17:
        raise ValueError("manifest coverage")
    source = (src / "SOURCE_LOCK.md").read_text(encoding="utf-8")
    lit = (src / "LITERATURE_NOVELTY_AUDIT.md").read_text(encoding="utf-8")
    selection = (src / "SELECTION_AND_PROVENANCE.md").read_text(encoding="utf-8")
    required = [
        "10.1090/conm/645/12907",
        "A. V. Abanin and R. S. Mannanikov",
        "10.46698/x5057-2500-3053-t",
        "Papers 27--30",
        "Paper 43",
        "free-UFD",
    ]
    corpus = source + "\n" + lit + "\n" + selection
    if not all(token in corpus for token in required):
        raise ValueError("source ownership")
    baseline = contract["mutation_baseline"]
    if baseline["ownership"] != {
        "external_sources": "includes_Abanin_Mannanikov_2023",
        "framing": "new_pairwise_arithmetic_classification",
        "h_free_part": "zero_credit",
        "internal_predecessors": "P27_P28_P29_P30_P43",
        "priority": False,
        "weighted_composition": "zero_credit",
    }:
        raise ValueError("ownership baseline")
    if baseline["controls"]["free_UFD"] != "negative_control" or baseline["scope"]["all_h"] is not True:
        raise ValueError("firewall")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, required=True)
    ns = p.parse_args()
    try:
        audit(ns.root)
        print('{"consumer":"S","verdict":"PASS"}')
        return 0
    except SourceReject as exc:
        print(json.dumps({"consumer_key": "S", "outcome": "REJECT", "exit_code": 2,
                          "rejection_code": exc.code,
                          "result_digest": hashlib.sha256(("S\n" + exc.code + "\n").encode()).hexdigest()},
                         sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:
        print('{"error":{"code":"SOURCE_AUDIT_ERROR","detail":"redacted","stage":"S"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
