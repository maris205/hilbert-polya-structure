#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C375."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import sys
from pathlib import Path

import yaml

if sys.flags.optimize:
    raise RuntimeError("C375 mutation suite refuses optimized Python")

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c375_lps_nonbacktracking_evidence.json"
YAML = ROOT / "evaluations/route_a/HCS-C375/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
TUPLE = ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
A1_SCOPE = "the exact primitive ledger is source-local and does not transfer q or primality to individual primitive-orbit labels"
A1_MISSING = [
    "no prime-to-orbit or prime-power repetition correspondence",
    "no intrinsic log(p) or von Mangoldt orbit weights",
    "no orbit phases or monodromy and stability multipliers",
    "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are absent",
]


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_loads(raw: str):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def mobius(n: int) -> int:
    factors = 0
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            factors += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        factors += 1
    return -1 if factors % 2 else 1


def validate(value):
    payload = dict(value)
    claimed = payload.pop("payload_sha256")
    assert hashlib.sha256(canonical(payload)).hexdigest() == claimed
    assert value["schema"] == "hcs-c375-lps-nonbacktracking-v1"
    assert value["candidate_id"] == "HCS-C375" and value["obstruction_id"] == "HEN-O359"
    assert value["source_commit"] == SOURCE
    assert value["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    construction = value["construction"]
    assert construction["quaternion_prime"] == 5 and construction["valency"] == 6
    assert len(construction["quaternion_generators"]) == 6
    assert all(sum(x * x for x in row) == 5 for row in construction["quaternion_generators"])
    assert construction["psl_residues_mod_20"] == [1, 9]
    assert construction["pgl_residues_mod_20"] == [13, 17]
    boundary = value["source_theorem_boundary"]
    assert boundary["lps_input"].startswith("LPS supplies connectedness")
    assert boundary["bass_hashimoto_input"].startswith("Bass and Hashimoto")
    assert boundary["pnt_ap_input"].startswith("The prime number theorem for arithmetic progressions")
    assert "HCS-C329 owns" in boundary["nearest_workspace_owner"]
    constants = value["theorem_constants"]
    assert constants == {
        "degree": 6, "tree_branching": 5,
        "ramanujan_adjacency_bound": "2*sqrt(5)",
        "hashimoto_circle_radius": "sqrt(5)",
        "bass_formula": "det(I-uH)=(1-u^2)^(2|V|)det(I-uA+5u^2 I)",
    }
    assert [row["q"] for row in value["panels"]] == [13, 17, 29, 37, 41]
    total_vertices = 0
    for panel in value["panels"]:
        q = panel["q"]
        residue = q % 20
        symbol = 1 if residue in (1, 9) else -1
        chamber = "PSL2_NONBIPARTITE" if symbol == 1 else "PGL2_BIPARTITE"
        size = q * (q * q - 1) // (2 if symbol == 1 else 1)
        assert panel["q_mod_20"] == residue and panel["legendre_5_over_q"] == symbol
        assert panel["chamber"] == chamber and panel["vertices"] == size
        assert panel["undirected_edges"] == 3 * size and panel["oriented_edges"] == 6 * size
        assert panel["bass_exponent"] == 2 * size
        expected_classes = ({"square": size, "nonsquare": 0} if symbol == 1
                            else {"square": size // 2, "nonsquare": size // 2})
        assert panel["determinant_square_classes"] == expected_classes
        assert len(panel["generators"]) == 6 and len({tuple(row) for row in panel["generators"]}) == 6
        assert panel["inverse_generator_indices"] == [1, 0, 3, 2, 5, 4]
        assert len(panel["vertex_digest"]) == 64
        rows = panel["iterate_ledger"]
        assert len(rows) == 12 and [row["iterate"] for row in rows] == list(range(1, 13))
        traces = [0] + [row["hashimoto_trace"] for row in rows]
        assert panel["certified_girth"] == next(n for n in range(1, 13) if traces[n] > 0)
        for n, row in enumerate(rows, 1):
            assert row["adjacency_trace"] == size * row["adjacency_return_words_per_vertex"]
            assert row["hashimoto_trace"] >= 0
            exact = sum(mobius(d) * traces[n // d] for d in range(1, n + 1) if n % d == 0)
            assert exact == n * row["primitive_oriented_cycles"]
        if symbol == -1:
            assert all(traces[n] == 0 for n in range(1, 13, 2))
        if q == 13:
            assert panel["direct_cyclic_words_through_8"] == [traces[n] // size for n in range(1, 9)]
        total_vertices += size
    assert value["panel_count"] == 5
    assert value["total_vertices"] == total_vertices
    assert value["total_oriented_edges"] == 6 * total_vertices
    assert value["total_prime_iterate_cells"] == 60
    ledger = value["prime_chamber_ledger"]
    counts = ledger["residue_counts_mod_20"]
    assert set(counts) == {"1", "9", "13", "17"}
    assert sum(counts.values()) == ledger["eligible_prime_count"] == 1124
    assert ledger["finite_chamber_counts"] == {
        "PSL2_NONBIPARTITE": counts["1"] + counts["9"],
        "PGL2_BIPARTITE": counts["13"] + counts["17"],
    }
    assert len(ledger["ledger_sha256"]) == 64 and ledger["prime_bound"] == 20_000
    assert ledger["asymptotic_statement"].startswith(
        "The prime number theorem for arithmetic progressions"
    )
    controls = value["arithmetic_controls"]
    assert controls["wrong_residue_gate"] and controls["composite_gate"]
    assert controls["shuffled_chamber_label_rule"] == (
        "cyclic shift by one on the sorted eligible-prime ledger"
    )
    assert controls["shuffled_chamber_label_trials"] == 1124
    assert 0 < controls["shuffled_chamber_label_mismatches"] <= 1124
    assert controls["shuffled_chamber_labels_rejected"]
    assert controls["duplicate_generator_mutation_rejected"]
    assert controls["wrong_quaternion_norm_mutation_rejected"]
    assert value["route_a"] == {
        "tuple": TUPLE, "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
        "a1_scope": A1_SCOPE, "a1_missing_requirements": A1_MISSING,
    }
    assert not any(value["scope_flags"].values())
    assert "no workspace ownership of the generic Bass-Ihara-Hashimoto identity already owned by HCS-C329" in value["nonclaims"]


def repair(value):
    value["payload_sha256"] = ""
    payload = dict(value)
    payload.pop("payload_sha256")
    value["payload_sha256"] = hashlib.sha256(canonical(payload)).hexdigest()


def mutate_and_expect_rejection(original, mutation):
    candidate = copy.deepcopy(original)
    mutation(candidate)
    repair(candidate)
    try:
        validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError, StopIteration):
        return
    raise AssertionError("semantic mutation survived validation")


def strict_yaml(raw: str):
    class Loader(yaml.SafeLoader):
        pass
    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError("duplicate YAML key")
            result[key] = loader.construct_object(value_node, deep=deep)
        return result
    Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    if "&" in raw or "*" in raw:
        raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if not isinstance(value, dict):
        raise ValueError("YAML root must be mapping")
    return value


def validate_evaluator(value):
    assert value["schema"] == "route-a-evaluation-v0.2.0"
    assert value["skill"] == "route-a-evaluator" and value["skill_version"] == "0.2.0"
    assert value["candidate_id"] == "HCS-C375" and value["source_commit"] == SOURCE
    assert value["code_commit"] == SOURCE
    assert set(value["source_lock"]) == {
        "object", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }
    assert len(value["a0"]["arithmetic_controls"]) >= 3
    assert all(row["status"] == "EXECUTED_EXACT" for row in value["a0"]["arithmetic_controls"])
    assert value["a1"]["verdict"] == "A1_WEAK"
    assert value["a1"]["metrics"]["mandatory_a1_controls_completed"] == 0
    assert value["tuple"] == TUPLE and value["overall_verdict"] == "ROUTE_A_EXPLORATORY"
    assert value["adversarial_controls"]["verdict"] == "PASS_SCOPE_LIMIT_RETAINED"
    assert value["claim_boundary"] and len(value["blocking_conditions"]) >= 4
    assert value["next_smallest_test"] and len(value["round2_clues"]) >= 2
    assert value["route_b_invocation_allowed"] is False
    assert not any(value["scope_flags"].values())


def main():
    original = strict_loads(EVIDENCE.read_text())
    validate(original)
    mutations = [
        lambda x: x.__setitem__("schema", "wrong"),
        lambda x: x.__setitem__("candidate_id", "HCS-C329"),
        lambda x: x.__setitem__("obstruction_id", "HEN-O1"),
        lambda x: x.__setitem__("source_commit", "0" * 40),
        lambda x: x.__setitem__("scope_literal", "OPEN"),
        lambda x: x["construction"].__setitem__("quaternion_prime", 7),
        lambda x: x["construction"].__setitem__("valency", 5),
        lambda x: x["construction"]["quaternion_generators"][0].__setitem__(0, 2),
        lambda x: x["construction"].__setitem__("psl_residues_mod_20", [1, 13]),
        lambda x: x["construction"].__setitem__("pgl_residues_mod_20", [9, 17]),
        lambda x: x["source_theorem_boundary"].__setitem__("lps_input", "package proof"),
        lambda x: x["source_theorem_boundary"].__setitem__("bass_hashimoto_input", "new"),
        lambda x: x["source_theorem_boundary"].__setitem__("pnt_ap_input", "finite data"),
        lambda x: x["source_theorem_boundary"].__setitem__("nearest_workspace_owner", "none"),
        lambda x: x["theorem_constants"].__setitem__("degree", 5),
        lambda x: x["theorem_constants"].__setitem__("tree_branching", 6),
        lambda x: x["theorem_constants"].__setitem__("ramanujan_adjacency_bound", "sqrt(5)"),
        lambda x: x["theorem_constants"].__setitem__("hashimoto_circle_radius", "5"),
        lambda x: x["theorem_constants"].__setitem__("bass_formula", "mutated"),
        lambda x: x["panels"].pop(),
        lambda x: x["panels"].reverse(),
        lambda x: x["panels"][0].__setitem__("q", 17),
        lambda x: x["panels"][0].__setitem__("q_mod_20", 1),
        lambda x: x["panels"][0].__setitem__("legendre_5_over_q", 1),
        lambda x: x["panels"][0].__setitem__("chamber", "PSL2_NONBIPARTITE"),
        lambda x: x["panels"][0].__setitem__("vertices", x["panels"][0]["vertices"] + 1),
        lambda x: x["panels"][0].__setitem__("undirected_edges", 0),
        lambda x: x["panels"][0].__setitem__("oriented_edges", 0),
        lambda x: x["panels"][0].__setitem__("bass_exponent", 0),
        lambda x: x["panels"][0]["determinant_square_classes"].__setitem__("square", 1),
        lambda x: x["panels"][0]["generators"].__setitem__(1, x["panels"][0]["generators"][0]),
        lambda x: x["panels"][0].__setitem__("inverse_generator_indices", [0, 1, 2, 3, 4, 5]),
        lambda x: x["panels"][0].__setitem__("vertex_digest", "0"),
        lambda x: x["panels"][0].__setitem__("certified_girth", 7),
        lambda x: x["panels"][0]["iterate_ledger"].pop(),
        lambda x: x["panels"][0]["iterate_ledger"][7].__setitem__("hashimoto_trace", 1),
        lambda x: x["panels"][0]["iterate_ledger"][7].__setitem__("primitive_oriented_cycles", 1),
        lambda x: x["panels"][0]["iterate_ledger"][5].__setitem__("adjacency_trace", 1),
        lambda x: x["panels"][0].__setitem__("direct_cyclic_words_through_8", [1] * 8),
        lambda x: x.__setitem__("panel_count", 4),
        lambda x: x.__setitem__("total_vertices", 1),
        lambda x: x.__setitem__("total_oriented_edges", 1),
        lambda x: x.__setitem__("total_prime_iterate_cells", 59),
        lambda x: x["prime_chamber_ledger"].__setitem__("prime_bound", 10_000),
        lambda x: x["prime_chamber_ledger"].__setitem__("eligible_prime_count", 1),
        lambda x: x["prime_chamber_ledger"]["residue_counts_mod_20"].__setitem__("1", 0),
        lambda x: x["prime_chamber_ledger"]["finite_chamber_counts"].__setitem__("PSL2_NONBIPARTITE", 0),
        lambda x: x["prime_chamber_ledger"].__setitem__("ledger_sha256", "0"),
        lambda x: x["prime_chamber_ledger"].__setitem__("asymptotic_statement", "finite estimate"),
        lambda x: x["arithmetic_controls"].__setitem__("wrong_residue_gate", False),
        lambda x: x["arithmetic_controls"].__setitem__("composite_gate", False),
        lambda x: x["arithmetic_controls"].__setitem__("shuffled_chamber_label_rule", "none"),
        lambda x: x["arithmetic_controls"].__setitem__("shuffled_chamber_label_trials", 0),
        lambda x: x["arithmetic_controls"].__setitem__("shuffled_chamber_label_mismatches", 0),
        lambda x: x["arithmetic_controls"].__setitem__("shuffled_chamber_labels_rejected", False),
        lambda x: x["arithmetic_controls"].__setitem__("duplicate_generator_mutation_rejected", False),
        lambda x: x["arithmetic_controls"].__setitem__("wrong_quaternion_norm_mutation_rejected", False),
        lambda x: x["route_a"].__setitem__("tuple", ["A0_FAIL"] * 5),
        lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda x: x["route_a"].__setitem__("a1_scope", "A1 passed"),
        lambda x: x["route_a"].__setitem__("a1_missing_requirements", []),
        lambda x: x["scope_flags"].__setitem__("claims_target_zero_match", True),
        lambda x: x["scope_flags"].__setitem__("claims_target_euler_factor", True),
        lambda x: x.__setitem__("nonclaims", []),
    ]
    for mutation in mutations:
        mutate_and_expect_rejection(original, mutation)
    attacks = len(mutations)

    invalid_json = [
        '{"a":1,"a":2}', '{"x":NaN}', '{"x":Infinity}', '[]',
    ]
    for raw in invalid_json:
        try:
            value = strict_loads(raw)
            if not isinstance(value, dict):
                raise ValueError("root")
        except ValueError:
            attacks += 1
        else:
            raise AssertionError("invalid JSON accepted")

    if YAML.exists():
        raw = YAML.read_text()
        parsed = strict_yaml(raw)
        validate_evaluator(parsed)
        evaluator_mutations = [
            lambda x: x.__setitem__("skill_version", "0.1.0"),
            lambda x: x.__setitem__("code_commit", "0" * 40),
            lambda x: x["source_lock"].pop("clock"),
            lambda x: x["a0"].__setitem__("arithmetic_controls", []),
            lambda x: x["a1"].__setitem__("verdict", "A1_PASS_ANALYTIC"),
            lambda x: x["a1"]["metrics"].__setitem__("mandatory_a1_controls_completed", 6),
            lambda x: x.__setitem__("overall_verdict", "ROUTE_A_ARITHMETIC_CANDIDATE"),
            lambda x: x["adversarial_controls"].__setitem__("verdict", "PASS"),
            lambda x: x.__setitem__("blocking_conditions", []),
            lambda x: x.__setitem__("next_smallest_test", ""),
            lambda x: x.__setitem__("route_b_invocation_allowed", True),
        ]
        for mutation in evaluator_mutations:
            candidate = copy.deepcopy(parsed)
            mutation(candidate)
            try:
                validate_evaluator(candidate)
            except (AssertionError, KeyError, TypeError, ValueError):
                attacks += 1
            else:
                raise AssertionError("evaluator mutation survived validation")
        bad_yaml = [raw + "\ncandidate_id: duplicate\n", "base: &b {x: 1}\ncopy: *b\n", "- a\n- b\n"]
        for bad in bad_yaml:
            try:
                strict_yaml(bad)
            except ValueError:
                attacks += 1
            else:
                raise AssertionError("invalid YAML accepted")
    print(f"C375 hostile mutation suite: PASS ({attacks} attacks)")


if __name__ == "__main__":
    main()
