#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C341."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c341_lamplighter_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C341/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "149222d5ca8282ed8e549c29788d2be83a64c2b56ee0e040d835ac4e19097fb0"
YAML_SEMANTIC = "6b2b892deb756d49ebd863dbb15000bf51973013e2283e7d7ccc0dedca5d5932"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


def duplicate_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate/non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def render(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def add_poly(a, b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def scale_poly(a, c):
    return [Fraction(c) * x for x in a]


def multiply_poly(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i + j] += a[i] * b[j]
    return out


def independent_path_det(length):
    determinants = [[Fraction(1)], [Fraction(-1, 2), Fraction(1)]]
    for order in range(2, length + 1):
        determinants.append(add_poly(
            multiply_poly([Fraction(-1, 2), Fraction(1)], determinants[-1]),
            scale_poly(determinants[-2], Fraction(-1, 16))))
    return determinants[length]


def independent_cycle_det(n):
    cheb = [[Fraction(1)], [Fraction(-1), Fraction(2)]]
    for order in range(2, n + 1):
        cheb.append(add_poly(
            scale_poly(multiply_poly([Fraction(-1), Fraction(2)], cheb[-1]), 2),
            scale_poly(cheb[-2], -1)))
    numerator = add_poly(cheb[n], [Fraction(-1)])
    return scale_poly(numerator, Fraction(1, 2 ** (2 * n - 1)))


def independent_runs(n, mask):
    if mask == 0:
        return [n]
    anchor = min(i for i in range(n) if mask & (1 << i))
    word = [not bool(mask & (1 << ((anchor + step) % n))) for step in range(1, n + 1)]
    answer, count = [], 0
    for kept in word:
        if kept:
            count += 1
        elif count:
            answer.append(count)
            count = 0
    if count:
        answer.append(count)
    return answer


def expected_block(n, mask):
    support = mask.bit_count()
    run_lengths = independent_runs(n, mask)
    if mask == 0:
        coefficients = independent_cycle_det(n)
        kind, zeros = "cycle", 0
    else:
        coefficients = [Fraction(1)]
        for length in run_lengths:
            coefficients = multiply_poly(coefficients, independent_path_det(length))
        coefficients = [Fraction(0)] * support + coefficients
        kind, zeros = "killed_paths", support
    return {"n": n, "mask": mask, "kind": kind, "deleted_count": support,
            "run_lengths": run_lengths, "zero_multiplicity": zeros,
            "charpoly_low_to_high": [render(x) for x in coefficients]}


def moves(n, x):
    if n == 1:
        return [(0, Fraction(1))]
    if n == 2:
        return [(x, Fraction(1, 2)), (1 - x, Fraction(1, 2))]
    return [(x, Fraction(1, 2)), ((x - 1) % n, Fraction(1, 4)),
            ((x + 1) % n, Fraction(1, 4))]


def overwrite(bits, vertex, value):
    cleared = bits ^ (bits & (1 << vertex))
    return cleared | (value << vertex)


def expected_direct(n, blocks):
    transition = []
    for bits in range(1 << n):
        for x in range(n):
            row = {}
            for departure_bit in range(2):
                middle = overwrite(bits, x, departure_bit)
                for y, motion in moves(n, x):
                    for arrival_bit in range(2):
                        final = overwrite(middle, y, arrival_bit)
                        column = final * n + y
                        row[column] = row.get(column, Fraction(0)) + motion * Fraction(1, 4)
            transition.append(row)
    one = sum(row.get(i, 0) for i, row in enumerate(transition))
    two = sum(probability * transition[j].get(i, 0)
              for i, row in enumerate(transition) for j, probability in row.items())
    expected_one = Fraction(0)
    expected_two = Fraction(0)
    for block in blocks:
        coefficients = [Fraction(x) for x in block["charpoly_low_to_high"]]
        trace = -coefficients[-2]
        square_trace = trace * trace - 2 * coefficients[-3] if n > 1 else trace * trace
        expected_one += trace
        expected_two += square_trace
    return {
        "n": n, "state_count": n * (1 << n),
        "nonzero_transition_cells": sum(map(len, transition)),
        "row_sum_failures": sum(sum(row.values()) != 1 for row in transition),
        "symmetry_failures": sum(transition[i].get(j, 0) != transition[j].get(i, 0)
                                  for i, row in enumerate(transition) for j in row),
        "trace_one": render(one), "predicted_trace_one": render(expected_one),
        "trace_two": render(two), "predicted_trace_two": render(expected_two),
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C341 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation_raw = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(evaluation_raw).hexdigest() == YAML_RAW, "YAML raw digest")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic digest")
    exact_keys(data, ["schema", "candidate_id", "obstruction_id", "evaluation_date",
        "source_commit", "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml",
        "model", "theorem_contract", "finite_grid", "collision_boundary", "nonclaims",
        "references", "route_a", "scope_flags", "cycle_rows", "block_rows",
        "direct_matrix_rows", "enumeration", "payload_sha256"], "top")
    claimed = data["payload_sha256"]
    body = dict(data)
    body.pop("payload_sha256")
    need(type(claimed) is str and claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need(data["schema"] == "hcs-c341-lamplighter-evidence-v1", "schema")
    need(data["candidate_id"] == "HCS-C341" and data["obstruction_id"] == "HEN-O325", "ids")
    need(data["evaluation_date"] == "2026-09-03", "evaluation date")
    need(data["source_commit"] == SOURCE and data["fixed_epoch"] == 1788393600, "source/epoch")
    need(data["scope_literal"] == SCOPE, "scope")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md",
         "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C341/2026-09-03.yaml",
         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {
        "state_space": "binary lamps on C_n times one position",
        "base_kernel": "stay 1/2 and total nearest-neighbour move 1/2",
        "switch": "independent fair replacement at departure and arrival",
        "small_cycles": "coalesce the two directed moves at n=2; Q_1 is identity",
        "inner_product": "uniform probability measure"}, "model")
    need(data["theorem_contract"] == {
        "stationarity": "unique uniform reversible law",
        "blocks": "Walsh direct sum of D_A Q_n D_A for every lamp support",
        "spectrum": "cycle Fourier modes plus all killed-path sine modes and deleted zeros",
        "characteristic_polynomial": "complete monic factorization with multiplicities",
        "gap": "sharp all-n L2 contraction and top-mode multiplicity",
        "boundaries": "n=1, n=2, empty support, full support, and switch convention"}, "theorem contract")
    need(data["finite_grid"] == {"n_min": 1, "n_max": 10, "direct_matrix_n_max": 6,
         "block_rows": 2046, "coefficient_cells": 20480}, "finite grid")
    need(data["collision_boundary"] == {
        "C171": "independent hypercube flips, not a moving lamp field",
        "C183": "random transpositions on a symmetric group",
        "C192": "hyperplane chamber walk without deleted-cycle blocks",
        "C338": "Wilson cycle popping and spanning trees, not a wreath-product Markov spectrum"}, "collision")
    need(data["nonclaims"] == [
        "no infinite-volume or percolation-transition theorem",
        "no deterministic-toggle theorem",
        "no target arithmetic local data or Euler-factor interpretation",
        "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [
        {"authors": "Lehner, Neuhauser, Woess", "year": 2008,
         "identifier": "DOI:10.1007/s00208-008-0222-7", "role": "switch-walk-switch spectral lineage"},
        {"authors": "Lehner", "year": 2009,
         "identifier": "DOI:10.1090/S0002-9939-09-09869-4", "role": "graph eigenspace lineage"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
         "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route A")
    need(data["scope_flags"] == FLAGS, "scope flags")
    blocks = [expected_block(n, mask) for n in range(1, 11) for mask in range(1 << n)]
    need(data["block_rows"] == blocks, "complete block ledger")
    cycles = []
    for n in range(1, 11):
        cycles.append({"n": n, "state_count": n * (1 << n), "block_count": 1 << n,
            "degree_sum": n * (1 << n), "top_nonconstant_multiplicity": 1 if n == 1 else n,
            "gap_formula": "1" if n == 1 else ("1/2" if n == 2 else "(1-cos(pi/n))/2"),
            "cycle_charpoly_low_to_high": [render(x) for x in independent_cycle_det(n)]})
    need(data["cycle_rows"] == cycles, "cycle rows")
    by_n = {n: [row for row in blocks if row["n"] == n] for n in range(1, 7)}
    direct = [expected_direct(n, by_n[n]) for n in range(1, 7)]
    need(data["direct_matrix_rows"] == direct, "direct matrix rows")
    expected_enumeration = {
        "cycle_rows_sha256": hashlib.sha256(canonical(cycles)).hexdigest(),
        "block_rows_sha256": hashlib.sha256(canonical(blocks)).hexdigest(),
        "direct_matrix_rows_sha256": hashlib.sha256(canonical(direct)).hexdigest(),
        "all_block_degrees": sum(row["n"] for row in blocks),
        "all_checks_exact": True,
    }
    need(data["enumeration"] == expected_enumeration, "enumeration")
    need(data["finite_grid"]["coefficient_cells"] == sum(len(row["charpoly_low_to_high"])
                                                          for row in blocks), "coefficient count")
    need(evaluation["candidate_id"] == "HCS-C341" and evaluation["obstruction_id"] == "HEN-O325", "YAML ids")
    need(evaluation["source_commit"] == SOURCE and evaluation["evaluation_date"] == "2026-09-03", "YAML source/date")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "YAML authority")
    need(evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator hash")
    need(evaluation["scope_literal"] == SCOPE and evaluation["scope_flags"] == FLAGS, "YAML scope")
    need(evaluation["tuple"] == data["route_a"]["tuple"] and evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    need(evaluation["route_b_invocation_allowed"] is False and evaluation["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(evaluation["finite_evidence_role"] == "convention and implementation receipt, not proof", "YAML finite role")
    print(f"C341 independent lamplighter checker: PASS {len(blocks)} blocks "
          f"{sum(len(x['charpoly_low_to_high']) for x in blocks)} coefficients 6 full kernels")


if __name__ == "__main__":
    main()
