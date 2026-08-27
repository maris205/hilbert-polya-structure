#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash mutation tests for C195."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c195_burgers_evidence.json"
CHECKER = ROOT / "code/c195_burgers_checker.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c195_mutation_checker", CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def repaired_hash(data: dict) -> None:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def mutations() -> list[tuple[str, callable]]:
    return [
        ("source_commit", lambda d: d["metadata"].__setitem__("source_commit", "0" * 40)),
        ("scope_literal", lambda d: d["metadata"].__setitem__("scope_literal", "UNSAFE_SCOPE")),
        ("evaluator_sha", lambda d: d["metadata"].__setitem__("evaluator_sha256", "0" * 64)),
        ("target_tables", lambda d: d["metadata"].__setitem__("target_tables_used", 1)),
        ("hopf_doi", lambda d: d["metadata"]["primary_sources"][0].__setitem__("doi", "bad-doi")),
        ("phase_regularities", lambda d: d["theorem"].__setitem__("phase_leaf", "all distributions")),
        ("cole_hopf_sign", lambda d: d["theorem"].__setitem__("cole_hopf_map", "Phi=m+2*nu*d_x(log w)")),
        ("snapshot_semantics", lambda d: d["theorem"].__setitem__("algebraic_snapshot_oracle", "every rational row is a physical-time sample")),
        ("recurrence_claim", lambda d: d["theorem"].__setitem__("recurrence", "all points recur")),
        ("route_a4", lambda d: d["route_a"].__setitem__("A4", "A4_PASS")),
        ("overall_route", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED")),
        ("summary_case_count", lambda d: d["summary"].__setitem__("regression_cases", 25)),
        ("viscosity", lambda d: d["regression_rows"][0].__setitem__("nu", "0/1")),
        ("initial_coefficient", lambda d: d["regression_rows"][0]["initial_coefficients"][0].__setitem__("coefficient", ["9/1", "0/1"])),
        ("positive_margin", lambda d: d["regression_rows"][1].__setitem__("strict_positive_l1_margin", "-1/1")),
        ("generator_residual", lambda d: d["regression_rows"][2].__setitem__("generator_residual_coefficients", [{"mode": 0, "coefficient": ["1/1", "0/1"]}])),
        ("snapshot_rho", lambda d: d["regression_rows"][3]["snapshot_parameters"].__setitem__("rho", "2/1")),
        ("snapshot_coefficient", lambda d: d["regression_rows"][4]["snapshot_coefficients"][0].__setitem__("coefficient", ["1/1", "1/1"])),
        ("semigroup_residual", lambda d: d["regression_rows"][5].__setitem__("semigroup_composition_residual_coefficients", [{"mode": 1, "coefficient": ["1/7", "0/1"]}])),
        ("first_mode", lambda d: d["regression_rows"][6].__setitem__("first_active_mode", 8)),
        ("decay_exponent", lambda d: d["regression_rows"][7].__setitem__("exact_decay_exponent", "999/1")),
        ("spectrum", lambda d: d["regression_rows"][8]["linearized_spectrum"][0].__setitem__("eigenvalue", ["0/1", "0/1"])),
    ]


def main() -> None:
    baseline = json.loads(EVIDENCE.read_text())
    checker = load_checker()
    repaired_rejections = 0
    stale_rejections = 0
    with tempfile.TemporaryDirectory(prefix="c195-mutations-") as temp:
        tempdir = Path(temp)
        for index, (name, mutate) in enumerate(mutations()):
            changed = deepcopy(baseline)
            mutate(changed)
            repaired_hash(changed)
            path = tempdir / f"repaired_{index:02d}_{name}.json"
            path.write_text(json.dumps(changed, sort_keys=True, indent=2) + "\n")
            try:
                checker.check(path)
            except (AssertionError, KeyError, TypeError, ValueError, ZeroDivisionError):
                repaired_rejections += 1
            else:
                raise AssertionError(f"repaired-hash mutation survived: {name}")

        stale = deepcopy(baseline)
        stale["metadata"]["candidate_id"] = "HCS-C195-STale"
        stale_path = tempdir / "stale_hash.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        try:
            checker.check(stale_path)
        except AssertionError:
            stale_rejections += 1
        else:
            raise AssertionError("stale-hash mutation survived")

    print(json.dumps({
        "status": "C195_MUTATION_PASS",
        "repaired_hash_mutations_rejected": repaired_rejections,
        "stale_hash_mutations_rejected": stale_rejections,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
