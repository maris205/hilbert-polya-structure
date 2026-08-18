#!/usr/bin/env python3
"""Hostile semantic mutations that the C63 checker must reject."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c63_kernel_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c63_kernel_checker.py"


def main() -> None:
    original = json.loads(EVIDENCE.read_text())

    def mutation(path, value):
        doc = deepcopy(original)
        node = doc
        for key in path[:-1]:
            node = node[key]
        node[path[-1]] = value
        return doc

    mutations = {
        "scope": mutation(["scope_literal"], "BAD_EULER_ALLOWED"),
        "status": mutation(["status"], "RELEASED"),
        "rank": mutation(["rank_over_Q"], 14),
        "matrix_entry": mutation(["character_matrix", 0, 0], original["character_matrix"][0][0] + 1),
        "basis": mutation(["nullspace_basis", "z2", 1], 0),
        "relation": mutation(["relation_vectors", "q_exterior", 1], 0),
        "full_burnside": mutation(["claims", "full_burnside_ring_kernel_claimed"], True),
        "arithmetic": mutation(["claims", "arithmetic_local_claimed"], True),
        "source_hash": mutation(["authority", "c62_dictionary_evidence_sha256"], "0" * 64),
        "primitive_rank": mutation(["primitive_support", "restricted_rank_over_Q"], 8),
    }

    rejected = []
    with tempfile.TemporaryDirectory(prefix="c63-mutations-") as tmp:
        tmpdir = Path(tmp)
        for name, doc in mutations.items():
            path = tmpdir / f"{name}.json"
            path.write_text(json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n")
            run = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                text=True,
                capture_output=True,
            )
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)

    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected), "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
