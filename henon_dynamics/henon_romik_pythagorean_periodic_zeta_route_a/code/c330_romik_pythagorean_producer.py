#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C330."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c330_romik_pythagorean_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C330/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
MAX_WORD_DEPTH = 8
F = {
    "1": ((1, 0), (2, 1)),
    "2": ((0, 1), (1, 2)),
    "3": ((0, 1), (-1, 2)),
}
M = {
    "1": ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3)),
    "2": ((1, 2, 2), (2, 1, 2), (2, 2, 3)),
    "3": ((1, -2, 2), (2, -1, 2), (2, -2, 3)),
}
FLAGS = {"claims_target_arithmetic_local_data": False,
         "claims_target_euler_factors": False, "claims_root_number": False,
         "claims_automorphy": False, "claims_target_divisor_or_counting_law": False,
         "claims_target_functional_equation": False, "claims_target_zero_match": False,
         "claims_hilbert_polya_operator": False, "invokes_route_b": False}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def matmul(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(middle))
                       for j in range(columns)) for i in range(rows))


def matvec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def frac(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def apply2(matrix, value):
    a, b = matrix[0]
    c, d = matrix[1]
    return Fraction(a * value.numerator + b * value.denominator,
                    c * value.numerator + d * value.denominator)


def least_period(word):
    for d in range(1, len(word) + 1):
        if len(word) % d == 0 and word == word[:d] * (len(word) // d):
            return d
    raise AssertionError("word period")


def mobius(n):
    rest, parity = n, 0
    factor = 2
    while factor * factor <= rest:
        if rest % factor == 0:
            rest //= factor
            if rest % factor == 0:
                return 0
            parity += 1
            while rest % factor == 0:
                rest //= factor
        factor += 1
    if rest > 1:
        parity += 1
    return -1 if parity % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def word_row(word):
    mobius_matrix = ((1, 0), (0, 1))
    triple_matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for digit in word:
        mobius_matrix = matmul(mobius_matrix, F[digit])
        triple_matrix = matmul(triple_matrix, M[digit])
    triple = matvec(triple_matrix, (3, 4, 5))
    a, b = mobius_matrix[0]
    c, d = mobius_matrix[1]
    determinant = a * d - b * c
    trace = a + d
    discriminant = trace * trace - 4 * determinant
    endpoints = sorted((apply2(mobius_matrix, Fraction(0)),
                        apply2(mobius_matrix, Fraction(1))))
    parabolic = word == "1" * len(word) or word == "3" * len(word)
    return {
        "word": word,
        "length": len(word),
        "pythagorean_triple": list(triple),
        "mobius_matrix_row_major": [a, b, c, d],
        "determinant": determinant,
        "trace": trace,
        "discriminant": discriminant,
        "cylinder_endpoints": [frac(value) for value in endpoints],
        "fixed_polynomial_low_to_high": [-b, d - a, c],
        "fixed_point_class": "parabolic_boundary" if parabolic else "quadratic_irrational_interior",
        "least_word_period": least_period(word),
        "expanding_multiplier": ("boundary" if parabolic else
                                  f"(({trace}+sqrt({discriminant}))/2)^2"),
    }


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def produce(evaluation_path):
    evaluation = strict_yaml(evaluation_path)
    rows = [word_row("".join(word)) for length in range(1, MAX_WORD_DEPTH + 1)
            for word in itertools.product("123", repeat=length)]
    period_rows = []
    for n in range(1, 13):
        fixed = 3 ** n - 2
        exact = sum(mobius(d) * (3 ** (n // d) - 2) for d in divisors(n))
        if exact % n:
            raise AssertionError("primitive divisibility")
        period_rows.append({"n": n, "fixed_points": fixed,
                            "exact_period_points": exact, "primitive_oriented_cycles": exact // n})
    data = {
        "schema": "hcs-c330-romik-pythagorean-v1",
        "candidate_id": "HCS-C330", "obstruction_id": "HEN-O314",
        "evaluation_date": "2026-09-03", "fixed_epoch": EPOCH,
        "source_commit": SOURCE, "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR,
                      "authority": "flow_systems/skills/route-a-evaluator.md"},
        "model": {
            "coordinate": "D(t)=((1-t^2)/(1+t^2),2t/(1+t^2)) on 0<t<1",
            "primary_orientation": "a odd, b even, t=n/m with coprime m>n of opposite parity, root t=1/2 and triple (3,4,5)",
            "mirror_orientation": "a even, b odd is obtained by leg swap and terminates at t=1/3",
            "irrational_phase_space": "X=(0,1) minus the rational numbers",
            "forward_branches": ["t/(1-2t) on (0,1/3)", "1/t-2 on (1/3,1/2)", "2-1/t on (1/2,1)"],
            "inverse_branches": ["t/(1+2t)", "1/(2+t)", "1/(2-t)"],
            "endpoint_convention": "branch images are open; 1/2 is the primary terminal and 1/3 the mirror terminal, never periodic points of X",
        },
        "theorem_contract": {
            "tree": "the primary Barning matrices generate every odd-even primitive Pythagorean triple exactly once from a possibly empty word, with the empty word owning (3,4,5)",
            "termination": "primary rational states terminate at 1/2 while irrational states never terminate",
            "periodic": "every length-n word except pure 1 and pure 3 has one quadratic-irrational fixed point",
            "counts": "Fix(T^n on X)=3^n-2 with exact-period and primitive counts by Mobius inversion",
            "zeta": "source Artin-Mazur zeta equals (1-z)^2/(1-3z)",
            "monodromy": "every periodic word has exact Mobius matrix, determinant orientation, and expanding multiplier",
        },
        "finite_grid": {"max_word_depth": MAX_WORD_DEPTH, "max_count_power": 12,
                        "arithmetic": "exact integers, rationals, and quadratic minimal polynomials"},
        "word_rows": rows,
        "period_count_rows": period_rows,
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C330/2026-09-03.yaml",
                         "raw_sha256": hashlib.sha256(evaluation_path.read_bytes()).hexdigest(),
                         "semantic_sha256": hashlib.sha256(json.dumps(
                             evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()},
        "collision_boundary": {
            "C132_C137": "generic Mobius Bergman transfer owners, not the parity-normalized Pythagorean tree",
            "C147_C152_C157": "rational square-billiard direction families, not ternary terminating and periodic coding",
            "C193": "Markoff Vieta descent on a different Diophantine surface",
            "C241": "Luroth countable-branch atlas, not the three-branch Gamma(2) factor",
        },
        "route_a": {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
                               "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "Finite word rows audit but do not prove the infinite symbolic theorem.",
            "Terminating primitive Pythagorean triples are not identified with periodic prime orbits.",
            "The source Artin-Mazur zeta and Gamma(2) factor statement are not target Euler factors, automorphy, or target RH claims.",
            "No literature-priority, target local datum, root number, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [{"authors": "Dan Romik", "title": "The dynamics of Pythagorean triples",
                        "identifier": "DOI:10.1090/S0002-9947-08-04467-X; arXiv:math/0406512"}],
    }
    counted = dict(data)
    data["enumeration"] = {
        "word_rows": len(rows),
        "tree_nodes_including_root": len(rows) + 1,
        "hyperbolic_word_rows": sum(row["fixed_point_class"] == "quadratic_irrational_interior" for row in rows),
        "parabolic_boundary_rows": sum(row["fixed_point_class"] == "parabolic_boundary" for row in rows),
        "period_count_rows": len(period_rows),
        "audited_leaf_count": leaves(counted),
    }
    body = dict(data)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C330 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = produce(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C330_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['word_rows']} words")


if __name__ == "__main__":
    main()
