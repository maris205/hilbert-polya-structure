#!/usr/bin/env python3
"""Repaired-hash JSON plus strict YAML hostile audit for HCS-C291."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/c291_dimer_rsa_evidence.json"
CHECKER = ROOT / "code/c291_dimer_rsa_checker.py"
YAML_SOURCE = ROOT / "evaluations/route_a/HCS-C291/2026-09-02.yaml"


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def delete_path(data, path) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]
    del target[path[-1]]


def rejected(path: Path, yaml_path: Path = YAML_SOURCE) -> bool:
    env = dict(os.environ)
    env.update({
        "C291_EVIDENCE": str(path),
        "C291_YAML": str(yaml_path),
        "PYTHONDONTWRITEBYTECODE": "1",
        "TZ": "UTC",
    })
    result = subprocess.run([sys.executable, "-B", str(CHECKER)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode != 0


def main() -> None:
    base = json.loads(SOURCE.read_text())
    attacks = [
        ("source", ("source_commit",), "0"*40),
        ("date", ("evaluation_date",), "2026-09-01"),
        ("epoch", ("fixed_epoch",), 1),
        ("scope", ("scope_literal",), "BAD_SCOPE"),
        ("evaluator", ("evaluator", "sha256"), "0"*64),
        ("schema", ("schema",), "wrong-schema"),
        ("candidate", ("candidate_id",), "HCS-C000"),
        ("headline", ("headline",), "maximum matching theorem"),
        ("sampling", ("model_contract", "sampling"), "biased edge order"),
        ("acceptance", ("model_contract", "acceptance_rule"), "accept adjacent edges"),
        ("maximal_semantics", ("model_contract", "output_semantics"), "always a maximum matching"),
        ("clock", ("model_contract", "clock"), "periodic flow"),
        ("path_pgf", ("theorem_contract", "path_pgf"), "F_n=z F_(n-2)"),
        ("riccati", ("theorem_contract", "riccati_ogf"), "F_x=z F^2"),
        ("factorial", ("theorem_contract", "factorial_moments"), "only first moment"),
        ("mean", ("theorem_contract", "exact_mean"), "E[M_n]=n/2"),
        ("variance", ("theorem_contract", "variance"), "Var=0"),
        ("path_support", ("theorem_contract", "path_support"), "only floor(n/2)"),
        ("cycle_identity", ("theorem_contract", "cycle_identity"), "G_n=F_n"),
        ("cycle_support", ("theorem_contract", "cycle_support"), "only maximum"),
        ("cycle_boundary", ("theorem_contract", "cycle_mean_boundary"), "no boundary correction"),
        ("occupancy", ("theorem_contract", "occupancy"), "tends to 1"),
        ("proof_status", ("proof_contract", "status"), "HEURISTIC"),
        ("proof_dependency", ("proof_contract", "dependencies", 1), "assume independence without conditioning"),
        ("finite_boundary", ("proof_contract", "finite_evidence_boundary"), "finite cases prove all n"),
        ("owner_boundary", ("proof_contract", "ownership_boundary"), "newly invented model"),
        ("enum_limit", ("enumeration_contract", "path_max_n"), 9),
        ("enum_bool", ("enumeration_contract", "cycle_max_n"), False),
        ("path_n", ("path_rows", 4, "n"), 5),
        ("path_edge_count", ("path_rows", 6, "edge_count"), 99),
        ("path_order_count", ("path_rows", 8, "order_count"), 1),
        ("path_probability", ("path_rows", 8, "distribution", 0, "probability"), "1/1"),
        ("path_order_cell", ("path_rows", 9, "distribution", 0, "order_count"), 0),
        ("path_mean", ("path_rows", 10, "mean"), "0/1"),
        ("path_variance", ("path_rows", 7, "variance"), "0/1"),
        ("path_support_min", ("path_rows", 10, "support_min"), 0),
        ("cycle_index", ("cycle_rows", 4, "path_identity_index"), 999),
        ("cycle_probability", ("cycle_rows", 6, "distribution", 0, "probability"), "0/1"),
        ("cycle_variance", ("cycle_rows", 5, "variance"), "999/1"),
        ("cycle_support", ("cycle_rows", 3, "support_max"), 0),
        ("factorial_n", ("factorial_moment_rows", 12, "n"), 13),
        ("factorial_value", ("factorial_moment_rows", 20, "moments", 5), "999/1"),
        ("factorial_truncate", ("factorial_moment_rows", 10, "moments"), ["1/1"]),
        ("asym_n", ("asymptotic_rows", 2, "n"), 101),
        ("asym_variance", ("asymptotic_rows", 3, "variance"), "1/1"),
        ("asym_decimal", ("asymptotic_rows", 3, "variance_density"), "9.99E+2"),
        ("boundary_semantic", ("boundary_rows", 5, "status"), "terminal matching is always maximum"),
        ("reference_doi", ("references", 0, "identifier"), "10.invalid"),
        ("reference_author", ("references", 1, "authors"), "anonymous"),
        ("collision_token", ("collision_snapshot", "token"), "mutable registry bytes"),
        ("collision_bool", ("collision_snapshot", "registry_bytes_required"), 0),
        ("collision_distinction", ("collision_snapshot", "closest", 0, "distinction"), "same model"),
        ("obstruction", ("collision_snapshot", "obstruction_id"), "HEN-O000"),
        ("nonclaim", ("nonclaims", 0), "Every jammed matching is maximum."),
        ("route_tuple", ("route_a", "tuple", 0), "A0_PASS"),
        ("route_overall", ("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("scope_flag", ("scope_flags", "root_numbers"), True),
        ("bool_path_n", ("path_rows", 0, "n"), False),
        ("string_edge_count", ("cycle_rows", 0, "edge_count"), "3"),
        ("unknown_top", ("unexpected_top",), True),
        ("unknown_nested", ("model_contract", "unexpected"), True),
        ("unknown_path_row", ("path_rows", 0, "unexpected"), True),
        ("unknown_distribution", ("path_rows", 2, "distribution", 0, "unexpected"), True),
    ]
    drops = [
        ("drop_headline", ("headline",)),
        ("drop_model", ("model_contract", "output_semantics")),
        ("drop_theorem", ("theorem_contract", "variance")),
        ("drop_proof", ("proof_contract", "finite_evidence_boundary")),
        ("drop_dependency", ("proof_contract", "dependencies", 0)),
        ("drop_path_row", ("path_rows", 5)),
        ("drop_path_field", ("path_rows", 0, "closed_mean")),
        ("drop_distribution_field", ("path_rows", 2, "distribution", 0, "probability")),
        ("drop_cycle_field", ("cycle_rows", 0, "path_identity_index")),
        ("drop_factorial_row", ("factorial_moment_rows", 20)),
        ("drop_asym_field", ("asymptotic_rows", 0, "variance_centered")),
        ("drop_boundary", ("boundary_rows", 0)),
        ("drop_reference", ("references", 3)),
        ("drop_closest", ("collision_snapshot", "closest", 1)),
        ("drop_nonclaim", ("nonclaims", 0)),
    ]

    trials = []
    for name, path, value in attacks:
        trial = copy.deepcopy(base)
        set_path(trial, path, value)
        trial["payload_sha256"] = payload_hash(trial)
        trials.append((name, trial))
    for name, path in drops:
        trial = copy.deepcopy(base)
        delete_path(trial, path)
        trial["payload_sha256"] = payload_hash(trial)
        trials.append((name, trial))
    for family in ("path_rows", "cycle_rows", "factorial_moment_rows", "asymptotic_rows", "boundary_rows", "references"):
        trial = copy.deepcopy(base)
        trial[family][-1] = copy.deepcopy(trial[family][0])
        trial["payload_sha256"] = payload_hash(trial)
        trials.append((f"duplicate_replace_{family}", trial))
    trial = copy.deepcopy(base)
    trial["path_rows"][0], trial["path_rows"][1] = trial["path_rows"][1], trial["path_rows"][0]
    trial["payload_sha256"] = payload_hash(trial)
    trials.append(("path_order_swap", trial))

    failures = []
    rejected_count = 0
    with tempfile.TemporaryDirectory(prefix="c291-mutation-") as temporary:
        directory = Path(temporary)
        for index, (name, trial) in enumerate(trials):
            path = directory / f"{index:03d}_{name}.json"
            path.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            if rejected(path):
                rejected_count += 1
            else:
                failures.append(name)

        stale = copy.deepcopy(base)
        stale["headline"] += " stale tamper"
        path = directory / "stale.json"
        path.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        rejected_count += rejected(path)

        raw = SOURCE.read_text()
        needle = '  "candidate_id": "HCS-C291",\n'
        assert needle in raw
        path = directory / "duplicate.json"
        path.write_text(raw.replace(needle, '  "candidate_id": "EVIL-FIRST",\n' + needle, 1))
        rejected_count += rejected(path)

        needle = '  "fixed_epoch": 1788307200,\n'
        assert needle in raw
        path = directory / "nan.json"
        path.write_text(raw.replace(needle, '  "fixed_epoch": NaN,\n', 1))
        rejected_count += rejected(path)

        yaml_base = yaml.safe_load(YAML_SOURCE.read_text())
        yaml_attacks = [
            ("yaml_schema", ("schema",), "route-a-evaluation-v9"),
            ("yaml_source", ("source_commit",), "0"*40),
            ("yaml_unknown_top", ("unexpected_top",), True),
            ("yaml_unknown_nested", ("a1", "unexpected"), "bad"),
            ("yaml_tuple", ("tuple", 0), "A0_PASS"),
            ("yaml_overall", ("overall_verdict",), "ROUTE_A_ACCEPTED"),
            ("yaml_route_b", ("route_b_invocation_allowed",), True),
            ("yaml_route_b_integer", ("route_b_invocation_allowed",), 0),
            ("yaml_scope", ("scope_literal",), "OPEN"),
            ("yaml_scope_flag", ("scope_flags", "root_numbers"), True),
            ("yaml_cutoff", ("orbit_cutoff",), 1000),
            ("yaml_epoch_bool", ("fixed_epoch",), False),
        ]
        yaml_trials = []
        for name, path_keys, value in yaml_attacks:
            trial = copy.deepcopy(yaml_base)
            set_path(trial, path_keys, value)
            yaml_trials.append((name, trial))
        for name, path_keys in (
            ("yaml_missing_top", ("obstruction_id",)),
            ("yaml_missing_nested", ("a2", "strongest_failure")),
        ):
            trial = copy.deepcopy(yaml_base)
            delete_path(trial, path_keys)
            yaml_trials.append((name, trial))
        for index, (name, trial) in enumerate(yaml_trials):
            yaml_path = directory / f"yaml_{index:03d}_{name}.yaml"
            yaml_path.write_text(yaml.safe_dump(trial, sort_keys=False, allow_unicode=True))
            if rejected(SOURCE, yaml_path):
                rejected_count += 1
            else:
                failures.append(name)

        yaml_raw = YAML_SOURCE.read_text()
        needle = "candidate_id: HCS-C291\n"
        assert yaml_raw.count(needle) == 1
        yaml_path = directory / "yaml_duplicate_top.yaml"
        yaml_path.write_text(yaml_raw.replace(needle, needle + needle, 1))
        if rejected(SOURCE, yaml_path):
            rejected_count += 1
        else:
            failures.append("yaml_duplicate_top")

        needle = "  root_numbers: false\n"
        assert yaml_raw.count(needle) == 1
        yaml_path = directory / "yaml_duplicate_nested.yaml"
        yaml_path.write_text(yaml_raw.replace(needle, "  root_numbers: true\n" + needle, 1))
        if rejected(SOURCE, yaml_path):
            rejected_count += 1
        else:
            failures.append("yaml_duplicate_nested")

    total = len(trials) + 3 + len(yaml_trials) + 2
    assert not failures, f"accepted repaired-hash attacks: {failures}"
    assert rejected_count == total
    print(f"C291 hostile mutation audit: PASS {rejected_count}/{total} (repaired-hash JSON attacks plus strict YAML schema/type/value, top/nested duplicate-key, stale-hash, and NaN attacks)")


if __name__ == "__main__":
    main()
