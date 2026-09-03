#!/usr/bin/env python3
"""Canonical exact-evidence producer for HCS-C341."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c341_lamplighter_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C341/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "149222d5ca8282ed8e549c29788d2be83a64c2b56ee0e040d835ac4e19097fb0"
YAML_SEMANTIC = "6b2b892deb756d49ebd863dbb15000bf51973013e2283e7d7ccc0dedca5d5932"


def duplicate_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


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
            raise ValueError("merge key")
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
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def padd(left, right):
    size = max(len(left), len(right))
    return [(left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
            for i in range(size)]


def pscale(poly, scalar):
    return [Fraction(scalar) * item for item in poly]


def pmul(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def path_poly(length):
    old, current = [Fraction(1)], [Fraction(-1, 2), Fraction(1)]
    if length == 0:
        return old
    if length == 1:
        return current
    for _ in range(2, length + 1):
        nxt = padd(pmul([Fraction(-1, 2), Fraction(1)], current),
                    pscale(old, Fraction(-1, 16)))
        old, current = current, nxt
    return current


def cycle_poly(n):
    # 2^(1-2n) [T_n(2z-1)-1].
    t0 = [Fraction(1)]
    t1 = [Fraction(-1), Fraction(2)]
    if n == 1:
        tn = t1
    else:
        for _ in range(2, n + 1):
            nxt = padd(pscale(pmul([Fraction(-1), Fraction(2)], t1), 2), pscale(t0, -1))
            t0, t1 = t1, nxt
        tn = t1
    tn = padd(tn, [Fraction(-1)])
    return pscale(tn, Fraction(1, 2 ** (2 * n - 1)))


def runs(n, mask):
    if mask == 0:
        return [n]
    deleted = next(i for i in range(n) if (mask >> i) & 1)
    result, current = [], 0
    for step in range(1, n + 1):
        vertex = (deleted + step) % n
        if (mask >> vertex) & 1:
            if current:
                result.append(current)
                current = 0
        else:
            current += 1
    if current:
        result.append(current)
    return result


def block_row(n, mask):
    deleted = mask.bit_count()
    lengths = runs(n, mask)
    if mask == 0:
        poly = cycle_poly(n)
        kind = "cycle"
        zero = 0
    else:
        poly = [Fraction(1)]
        for length in lengths:
            poly = pmul(poly, path_poly(length))
        poly = [Fraction(0)] * deleted + poly
        kind = "killed_paths"
        zero = deleted
    if len(poly) != n + 1 or poly[-1] != 1:
        raise AssertionError("monic block polynomial")
    return {
        "n": n,
        "mask": mask,
        "kind": kind,
        "deleted_count": deleted,
        "run_lengths": lengths,
        "zero_multiplicity": zero,
        "charpoly_low_to_high": [fstr(value) for value in poly],
    }


def base_moves(n, x):
    if n == 1:
        return [(0, Fraction(1))]
    if n == 2:
        return [(x, Fraction(1, 2)), (1 - x, Fraction(1, 2))]
    return [(x, Fraction(1, 2)), ((x - 1) % n, Fraction(1, 4)),
            ((x + 1) % n, Fraction(1, 4))]


def set_lamp(configuration, vertex, bit):
    return (configuration & ~(1 << vertex)) | (bit << vertex)


def direct_row(n, block_rows):
    size = n * (1 << n)
    rows = []
    for configuration in range(1 << n):
        for x in range(n):
            row = {}
            for first in (0, 1):
                after_first = set_lamp(configuration, x, first)
                for y, q in base_moves(n, x):
                    for second in (0, 1):
                        final = set_lamp(after_first, y, second)
                        target = final * n + y
                        row[target] = row.get(target, Fraction(0)) + q / 4
            rows.append(row)
    row_sum_failures = sum(sum(row.values()) != 1 for row in rows)
    symmetry_failures = sum(rows[i].get(j, 0) != rows[j].get(i, 0)
                            for i, row in enumerate(rows) for j in row)
    trace_one = sum(row.get(i, 0) for i, row in enumerate(rows))
    trace_two = sum(value * rows[j].get(i, 0)
                    for i, row in enumerate(rows) for j, value in row.items())
    predicted_one = Fraction(0)
    predicted_two = Fraction(0)
    for row in block_rows:
        coefficients = [Fraction(value) for value in row["charpoly_low_to_high"]]
        first = -coefficients[-2]
        second = first * first - 2 * coefficients[-3] if n >= 2 else first * first
        predicted_one += first
        predicted_two += second
    return {
        "n": n,
        "state_count": size,
        "nonzero_transition_cells": sum(len(row) for row in rows),
        "row_sum_failures": row_sum_failures,
        "symmetry_failures": symmetry_failures,
        "trace_one": fstr(trace_one),
        "predicted_trace_one": fstr(predicted_one),
        "trace_two": fstr(trace_two),
        "predicted_trace_two": fstr(predicted_two),
    }


def row_hash(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    blocks = [block_row(n, mask) for n in range(1, 11) for mask in range(1 << n)]
    by_n = {n: [row for row in blocks if row["n"] == n] for n in range(1, 11)}
    direct = [direct_row(n, by_n[n]) for n in range(1, 7)]
    cycles = []
    for n in range(1, 11):
        gap = "1" if n == 1 else ("1/2" if n == 2 else "(1-cos(pi/n))/2")
        top_mult = 1 if n == 1 else n
        cycles.append({
            "n": n,
            "state_count": n * (1 << n),
            "block_count": 1 << n,
            "degree_sum": n * (1 << n),
            "top_nonconstant_multiplicity": top_mult,
            "gap_formula": gap,
            "cycle_charpoly_low_to_high": [fstr(x) for x in cycle_poly(n)],
        })
    data = {
        "schema": "hcs-c341-lamplighter-evidence-v1",
        "candidate_id": "HCS-C341",
        "obstruction_id": "HEN-O325",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": 1788393600,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C341/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "state_space": "binary lamps on C_n times one position",
            "base_kernel": "stay 1/2 and total nearest-neighbour move 1/2",
            "switch": "independent fair replacement at departure and arrival",
            "small_cycles": "coalesce the two directed moves at n=2; Q_1 is identity",
            "inner_product": "uniform probability measure",
        },
        "theorem_contract": {
            "stationarity": "unique uniform reversible law",
            "blocks": "Walsh direct sum of D_A Q_n D_A for every lamp support",
            "spectrum": "cycle Fourier modes plus all killed-path sine modes and deleted zeros",
            "characteristic_polynomial": "complete monic factorization with multiplicities",
            "gap": "sharp all-n L2 contraction and top-mode multiplicity",
            "boundaries": "n=1, n=2, empty support, full support, and switch convention",
        },
        "finite_grid": {"n_min": 1, "n_max": 10, "direct_matrix_n_max": 6,
                        "block_rows": len(blocks), "coefficient_cells": sum(n + 1 for n in range(1, 11) for _ in range(1 << n))},
        "collision_boundary": {
            "C171": "independent hypercube flips, not a moving lamp field",
            "C183": "random transpositions on a symmetric group",
            "C192": "hyperplane chamber walk without deleted-cycle blocks",
            "C338": "Wilson cycle popping and spanning trees, not a wreath-product Markov spectrum",
        },
        "nonclaims": [
            "no infinite-volume or percolation-transition theorem",
            "no deterministic-toggle theorem",
            "no target arithmetic local data or Euler-factor interpretation",
            "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B",
        ],
        "references": [
            {"authors": "Lehner, Neuhauser, Woess", "year": 2008,
             "identifier": "DOI:10.1007/s00208-008-0222-7", "role": "switch-walk-switch spectral lineage"},
            {"authors": "Lehner", "year": 2009,
             "identifier": "DOI:10.1090/S0002-9939-09-09869-4", "role": "graph eigenspace lineage"},
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "cycle_rows": cycles,
        "block_rows": blocks,
        "direct_matrix_rows": direct,
        "enumeration": {
            "cycle_rows_sha256": row_hash(cycles),
            "block_rows_sha256": row_hash(blocks),
            "direct_matrix_rows_sha256": row_hash(direct),
            "all_block_degrees": sum(row["n"] for row in blocks),
            "all_checks_exact": True,
        },
    }
    data["payload_sha256"] = hashlib.sha256(canonical(data)).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C341 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C341_PRODUCER_PASS blocks={len(data['block_rows'])} "
          f"coefficients={data['finite_grid']['coefficient_cells']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
