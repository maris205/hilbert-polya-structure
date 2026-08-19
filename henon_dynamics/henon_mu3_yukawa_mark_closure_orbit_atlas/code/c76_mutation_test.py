#!/usr/bin/env python3
"""Hostile semantic mutations for the C76 independent checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c76_closure_orbit_atlas_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c76_closure_orbit_atlas_checker.py"


def mutate(document: dict, path: list[object], value: object) -> dict:
    result = deepcopy(document)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c76-unknown-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "c75_authority": mutate(original, ["authority", "c75"], "0" * 64),
        "manifest_authority": mutate(original, ["authority", "c75_manifest"], "1" * 64),
        "ambient_lift_order": mutate(original, ["source_model", "c75_lifted_group_order"], 1920),
        "kernel_order": mutate(original, ["source_model", "c75_ambient_c6_kernel_order"], 1),
        "effective_group_order": mutate(original, ["source_model", "effective_label_group_order"], 11520),
        "group_structure": mutate(original, ["source_model", "effective_label_group_candidate"], "S5 x C2 x C8"),
        "generator_name": mutate(
            original,
            ["source_model", "effective_generator_names", 0],
            "ambient_r",
        ),
        "orbit_count": mutate(original, ["support_orbit_atlas", "orbit_count"], 3025),
        "orbit_spectrum": mutate(
            original,
            ["support_orbit_atlas", "orbit_size_spectrum", "160"],
            17,
        ),
        "cardinality_vector": mutate(
            original,
            ["support_orbit_atlas", "orbit_count_by_cardinality", 8],
            451,
        ),
        "closure_minimal_count": mutate(original, ["closure_minimality", "support_count"], 99),
        "full_core_minimal_count": mutate(original, ["full_core_minimality", "support_count"], 26),
        "firewall_claim": mutate(original, ["claims", "arithmetic_local_claimed"], True),
    }

    rejected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c76-mutations-") as temporary:
        for name, document in mutations.items():
            path = Path(temporary) / f"{name}.json"
            path.write_bytes((json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
            )
            assert run.returncode != 0, f"mutation accepted: {name}\nstdout={run.stdout}\nstderr={run.stderr}"
            rejected.append(name)

    print(json.dumps({
        "status": "MUTATION_TEST_PASS",
        "mutations_rejected": len(rejected),
        "names": sorted(rejected),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
