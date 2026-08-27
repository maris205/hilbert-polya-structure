#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash adversarial tests for C192."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c192_hyperplane_evidence.json"
CHECKER = ROOT / "code/c192_hyperplane_checker.py"
TEMP = ROOT / "results/.c192_mutation.tmp.json"


def repair(document: dict) -> None:
    payload = dict(document)
    payload.pop("payload_sha256", None)
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    document["payload_sha256"] = sha256(canonical).hexdigest()


def rejected(document: dict, repaired: bool) -> bool:
    if repaired:
        repair(document)
    TEMP.write_text(json.dumps(document, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    result = subprocess.run([sys.executable, str(CHECKER), str(TEMP)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode != 0


def set_path(path: tuple, value):
    def mutate(document: dict) -> None:
        cursor = document
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
    return mutate


def append_path(path: tuple, suffix: str):
    def mutate(document: dict) -> None:
        cursor = document
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] += suffix
    return mutate


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, object]] = [
        ("candidate", set_path(("candidate_id",), "HCS-C191")),
        ("date", set_path(("evaluation_date",), "2026-08-26")),
        ("commit", set_path(("source_commit",), "0" * 40)),
        ("evaluator-version", set_path(("evaluator", "version"), "0.2.1")),
        ("evaluator-path", append_path(("evaluator", "path"), ".bak")),
        ("evaluator-hash", set_path(("evaluator", "sha256"), "f" * 64)),
        ("scope", append_path(("scope_literal",), "_RELAXED")),
        ("source-doi", append_path(("source_lock", "primary", "doi"), "x")),
        ("source-authors", append_path(("source_lock", "primary", "authors"), " et al.")),
        ("source-title", append_path(("source_lock", "primary", "title"), " revised")),
        ("source-journal", append_path(("source_lock", "primary", "journal"), " online")),
        ("source-locators", set_path(("source_lock", "primary", "theorem_locators"), ["Theorem 1"])),
        ("om-overclaim", append_path(("source_lock", "oriented_matroid_ceiling"), " All affine extensions follow.")),
        ("strict-sst-overclaim", set_path(("source_lock", "strict_sst_boundary"), "The chamber and stopping time are independent.")),
        ("domain", append_path(("theorem_lock", "domain"), " Including infinite arrangements.")),
        ("spectrum", append_path(("theorem_lock", "spectrum"), " It is self-adjoint.")),
        ("operator", append_path(("theorem_lock", "operator_corollaries"), " This is a target determinant.")),
        ("stationarity", append_path(("theorem_lock", "stationarity"), " Reversibility follows.")),
        ("sampler", append_path(("theorem_lock", "sampler"), " It is a strict SST.")),
        ("mixing", append_path(("theorem_lock", "mixing"), " The bound is always sharp.")),
        ("nonseparating", append_path(("theorem_lock", "nonseparating"), " The chain is irreducible.")),
        ("attribution-status", set_path(("attribution", "status"), "NEW_THEOREM_CLAIMED")),
        ("owner", set_path(("attribution", "all_family_proof_owner"), "HCS-C192")),
        ("code-role", set_path(("attribution", "code_role"), "all-family proof")),
        ("novelty", set_path(("attribution", "novelty_claimed"), True)),
        ("external-review", set_path(("attribution", "external_review_claimed"), True)),
        ("route-tuple", set_path(("route_a", "tuple", 0), "A0_PASS")),
        ("route-A0", append_path(("route_a", "qualifications", "A0"), " Prime clock assigned.")),
        ("route-A1", append_path(("route_a", "qualifications", "A1"), " Arithmetic recovered.")),
        ("route-A2", append_path(("route_a", "qualifications", "A2"), " Functional equation found.")),
        ("route-A3", append_path(("route_a", "qualifications", "A3"), " Counting law found.")),
        ("route-A4", append_path(("route_a", "qualifications", "A4"), " Target operator identified.")),
        ("route-overall", set_path(("route_a", "overall"), "ROUTE_A_ACCEPTED")),
        ("route-b", set_path(("route_a", "route_b_invocation_allowed"), True)),
    ]
    for key in sorted(base["forbidden_claims"]):
        attacks.append((f"forbidden-{key}", set_path(("forbidden_claims", key), True)))
    for key, value in sorted(base["finite_regression"].items()):
        attacks.append((f"aggregate-{key}", set_path(("finite_regression", key), value + 1)))
    attacks.extend([
        ("case-name", append_path(("cases", 0, "name"), "_new")),
        ("case-family", set_path(("cases", 0, "family"), "braid")),
        ("case-parameter", set_path(("cases", 0, "parameter"), 9)),
        ("case-tags", set_path(("cases", 0, "tags"), ["separating"])),
        ("hyperplane-label", append_path(("cases", 0, "hyperplanes", 0), "x")),
        ("face-sign", set_path(("cases", 0, "faces", 0, 0), 2)),
        ("chamber-zero", set_path(("cases", 0, "chambers", 0, 0), 0)),
        ("weight", set_path(("cases", 0, "positive_weights", 0, "weight"), "1")),
        ("separating", set_path(("cases", 0, "separating"), False)),
        ("A0", set_path(("cases", 0, "nonseparating_hyperplane_indices"), [0])),
        ("component", set_path(("cases", 0, "stationary_simplex_vertex_count"), 2)),
        ("flat-lambda", set_path(("cases", 0, "flats", 0, "lambda"), "0")),
        ("flat-mobius", set_path(("cases", 0, "flats", 1, "mobius_to_ambient"), 7)),
        ("flat-multiplicity", set_path(("cases", 0, "flats", 1, "multiplicity"), 7)),
        ("transition", set_path(("cases", 0, "transition_matrix", 0, 0), "1")),
        ("charpoly", set_path(("cases", 0, "charpoly_ascending", 0), "9")),
        ("determinant", set_path(("cases", 0, "det_I_minus_zK_ascending", 0), "9")),
        ("trace", set_path(("cases", 0, "power_traces", 0, "direct"), "0")),
        ("sampler-probability", set_path(("cases", 0, "without_replacement_stationary", 0, "probability"), "1")),
        ("mixing-tv", set_path(("cases", 0, "mixing", 0, "worst_total_variation"), "1")),
        ("mixing-failure", set_path(("cases", 0, "mixing", 0, "exact_failure_probability"), "9")),
        ("nonsep-sampler", set_path(("cases", 4, "without_replacement_stationary"), [{"chamber": [1, 1, 1], "probability": "1"}])),
    ])

    repaired_rejections = 0
    try:
        for name, mutate in attacks:
            document = deepcopy(base)
            mutate(document)
            if not rejected(document, repaired=True):
                raise AssertionError(f"repaired-hash mutation accepted: {name}")
            repaired_rejections += 1
        stale = deepcopy(base)
        stale["route_a"]["overall"] = "ROUTE_A_ACCEPTED"
        assert rejected(stale, repaired=False), "stale-hash mutation accepted"
    finally:
        TEMP.unlink(missing_ok=True)
    print(json.dumps({
        "status": "C192_MUTATION_PASS",
        "repaired_hash_rejections": repaired_rejections,
        "stale_hash_rejections": 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
