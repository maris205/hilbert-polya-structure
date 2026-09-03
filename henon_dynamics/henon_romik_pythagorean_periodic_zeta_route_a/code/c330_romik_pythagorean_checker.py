#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C330."""
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
DEFAULT = ROOT / "results/c330_romik_pythagorean_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C330/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "782f6c46fcb826ec1c09dcf057aeada212cecd14965414027924cb5b6e804eec"
YAML_SEMANTIC = "c88269bb217580be8d912f23fb85237f4f0534701ac5d4d237f0d0786e41162f"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DEPTH = 8
INVERSE = {"1": (1, 0, 2, 1), "2": (0, 1, 1, 2), "3": (0, 1, -1, 2)}
TRIPLE = {
    "1": (-1, 2, 2, -2, 1, 2, -2, 2, 3),
    "2": (1, 2, 2, 2, 1, 2, 2, 2, 3),
    "3": (1, -2, 2, 2, -1, 2, 2, -2, 3),
}
FLAGS = {"claims_target_arithmetic_local_data": False,
         "claims_target_euler_factors": False, "claims_root_number": False,
         "claims_automorphy": False, "claims_target_divisor_or_counting_law": False,
         "claims_target_functional_equation": False, "claims_target_zero_match": False,
         "claims_hilbert_polya_operator": False, "invokes_route_b": False}


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors or aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def mul2(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h,
            c * e + d * g, c * f + d * h)


def mul3(left, right):
    return tuple(sum(left[3 * i + k] * right[3 * k + j] for k in range(3))
                 for i in range(3) for j in range(3))


def act3(matrix, vector):
    return tuple(sum(matrix[3 * i + j] * vector[j] for j in range(3)) for i in range(3))


def apply(matrix, value):
    a, b, c, d = matrix
    return Fraction(a * value.numerator + b * value.denominator,
                    c * value.numerator + d * value.denominator)


def render(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def word_period(word):
    return next(d for d in range(1, len(word) + 1)
                if len(word) % d == 0 and word == word[:d] * (len(word) // d))


def mu(n):
    count, rest, prime = 0, n, 2
    while prime * prime <= rest:
        if rest % prime == 0:
            rest //= prime
            if rest % prime == 0:
                return 0
            count += 1
            while rest % prime == 0:
                rest //= prime
        prime += 1
    if rest > 1:
        count += 1
    return -1 if count % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def forward(value):
    if value == Fraction(1, 2):
        return None
    if value == Fraction(1, 3):
        return None
    if 0 < value < Fraction(1, 3):
        return value / (1 - 2 * value)
    if Fraction(1, 3) < value < Fraction(1, 2):
        return 1 / value - 2
    if Fraction(1, 2) < value < 1:
        return 2 - 1 / value
    raise AssertionError("forward domain")


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C330 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    root_keys = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                 "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                 "finite_grid", "word_rows", "period_count_rows", "route_a_yaml", "collision_boundary",
                 "route_a", "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    exact_keys(data, root_keys, "root")
    required = {"schema": "hcs-c330-romik-pythagorean-v1", "candidate_id": "HCS-C330",
                "obstruction_id": "HEN-O314", "evaluation_date": "2026-09-03",
                "fixed_epoch": 1788393600, "source_commit": SOURCE, "scope_literal": SCOPE}
    for key, expected in required.items():
        need(data[key] == expected, key)
    need(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR,
                               "authority": "flow_systems/skills/route-a-evaluator.md"}, "evaluator")
    body = dict(data)
    payload = body.pop("payload_sha256")
    need(payload == hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(), "payload")
    expected_model = {
        "coordinate": "D(t)=((1-t^2)/(1+t^2),2t/(1+t^2)) on 0<t<1",
        "primary_orientation": "a odd, b even, t=n/m with coprime m>n of opposite parity, root t=1/2 and triple (3,4,5)",
        "mirror_orientation": "a even, b odd is obtained by leg swap and terminates at t=1/3",
        "irrational_phase_space": "X=(0,1) minus the rational numbers",
        "forward_branches": ["t/(1-2t) on (0,1/3)", "1/t-2 on (1/3,1/2)", "2-1/t on (1/2,1)"],
        "inverse_branches": ["t/(1+2t)", "1/(2+t)", "1/(2-t)"],
        "endpoint_convention": "branch images are open; 1/2 is the primary terminal and 1/3 the mirror terminal, never periodic points of X"}
    need(data["model"] == expected_model, "model")
    need(data["theorem_contract"] == {
        "tree": "the primary Barning matrices generate every odd-even primitive Pythagorean triple exactly once from a possibly empty word, with the empty word owning (3,4,5)",
        "termination": "primary rational states terminate at 1/2 while irrational states never terminate",
        "periodic": "every length-n word except pure 1 and pure 3 has one quadratic-irrational fixed point",
        "counts": "Fix(T^n on X)=3^n-2 with exact-period and primitive counts by Mobius inversion",
        "zeta": "source Artin-Mazur zeta equals (1-z)^2/(1-3z)",
        "monodromy": "every periodic word has exact Mobius matrix, determinant orientation, and expanding multiplier"}, "contract")
    need(data["finite_grid"] == {"max_word_depth": 8, "max_count_power": 12,
                                  "arithmetic": "exact integers, rationals, and quadratic minimal polynomials"}, "grid")
    # Cheap ownership locks precede the 9,840-row algebraic audit so hostile
    # YAML and repaired-hash metadata attacks fail without paying for the full
    # word traversal.  The detailed semantic checks are repeated below.
    early_evaluation = strict_yaml(args.evaluation)
    early_raw = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    early_semantic = hashlib.sha256(json.dumps(
        early_evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(early_raw == YAML_RAW and early_semantic == YAML_SEMANTIC, "early YAML lock")
    need(data["collision_boundary"] == {
        "C132_C137": "generic Mobius Bergman transfer owners, not the parity-normalized Pythagorean tree",
        "C147_C152_C157": "rational square-billiard direction families, not ternary terminating and periodic coding",
        "C193": "Markoff Vieta descent on a different Diophantine surface",
        "C241": "Luroth countable-branch atlas, not the three-branch Gamma(2) factor"}, "early collisions")
    need(data["nonclaims"] == [
        "Finite word rows audit but do not prove the infinite symbolic theorem.",
        "Terminating primitive Pythagorean triples are not identified with periodic prime orbits.",
        "The source Artin-Mazur zeta and Gamma(2) factor statement are not target Euler factors, automorphy, or target RH claims.",
        "No literature-priority, target local datum, root number, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted."], "early nonclaims")
    need(data["references"] == [{"authors": "Dan Romik", "title": "The dynamics of Pythagorean triples",
          "identifier": "DOI:10.1090/S0002-9947-08-04467-X; arXiv:math/0406512"}], "early references")
    need(data["route_a"] == {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
         "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_EXPLORATORY",
         "route_b_invocation_allowed": False}, "early route")
    need(data["scope_flags"] == FLAGS, "early scope")
    need(data["enumeration"]["word_rows"] == 9840, "early enumeration")
    words = ["".join(word) for length in range(1, DEPTH + 1)
             for word in itertools.product("123", repeat=length)]
    need(len(data["word_rows"]) == len(words), "word rows length")
    identity2 = (1, 0, 0, 1)
    identity3 = (1, 0, 0, 0, 1, 0, 0, 0, 1)
    seen_triples = set()
    checks = 40
    for row, word in zip(data["word_rows"], words):
        exact_keys(row, {"word", "length", "pythagorean_triple", "mobius_matrix_row_major",
                         "determinant", "trace", "discriminant", "cylinder_endpoints",
                         "fixed_polynomial_low_to_high", "fixed_point_class", "least_word_period",
                         "expanding_multiplier"}, "word row")
        mobius_matrix, triple_matrix = identity2, identity3
        for digit in word:
            mobius_matrix = mul2(mobius_matrix, INVERSE[digit])
            triple_matrix = mul3(triple_matrix, TRIPLE[digit])
        triple = act3(triple_matrix, (3, 4, 5))
        need(row["word"] == word and row["length"] == len(word), "word coordinate")
        need(row["mobius_matrix_row_major"] == list(mobius_matrix), "Mobius matrix")
        need(row["pythagorean_triple"] == list(triple), "triple matrix")
        a_leg, b_leg, hyp = triple
        need(a_leg > 0 and b_leg > 0 and a_leg * a_leg + b_leg * b_leg == hyp * hyp,
             "Pythagorean identity")
        need(math.gcd(a_leg, b_leg) == 1 and a_leg % 2 == 1 and b_leg % 2 == 0,
             "primitive parity orientation")
        need(triple not in seen_triples, "unique tree node")
        seen_triples.add(triple)
        t = Fraction(b_leg, a_leg + hyp)
        expected_t = Fraction(1, 2)
        for digit in reversed(word):
            expected_t = apply(INVERSE[digit], expected_t)
        need(t == expected_t, "Euclid coordinate")
        parent = t
        for _ in range(len(word)):
            before_denominator = parent.denominator
            parent = forward(parent)
            need(parent is not None and parent.denominator < before_denominator, "strict rational descent")
        need(parent == Fraction(1, 2), "primary terminal")
        a, b, c, d = mobius_matrix
        determinant, trace = a * d - b * c, a + d
        discriminant = trace * trace - 4 * determinant
        endpoints = sorted((apply(mobius_matrix, Fraction(0)), apply(mobius_matrix, Fraction(1))))
        need(row["determinant"] == determinant and determinant == (-1) ** word.count("2"), "determinant")
        need(row["trace"] == trace and row["discriminant"] == discriminant, "trace discriminant")
        need(row["cylinder_endpoints"] == [render(x) for x in endpoints], "cylinder")
        polynomial = [-b, d - a, c]
        need(row["fixed_polynomial_low_to_high"] == polynomial, "fixed polynomial")
        parabolic = word == "1" * len(word) or word == "3" * len(word)
        classification = "parabolic_boundary" if parabolic else "quadratic_irrational_interior"
        need(row["fixed_point_class"] == classification, "classification")
        need(row["least_word_period"] == word_period(word), "word period")
        if parabolic:
            need(discriminant == 0 and row["expanding_multiplier"] == "boundary", "parabolic boundary")
        else:
            need(discriminant > 0 and math.isqrt(discriminant) ** 2 != discriminant, "quadratic irrational")
            evaluate = lambda x: polynomial[0] + polynomial[1] * x + polynomial[2] * x * x
            need(evaluate(endpoints[0]) * evaluate(endpoints[1]) < 0, "unique interior root bracket")
            need(row["expanding_multiplier"] == f"(({trace}+sqrt({discriminant}))/2)^2", "multiplier")
        checks += 22 + len(word)
    need(len(data["period_count_rows"]) == 12, "period count length")
    for n, row in enumerate(data["period_count_rows"], 1):
        exact_keys(row, {"n", "fixed_points", "exact_period_points", "primitive_oriented_cycles"}, "period count")
        fixed = 3 ** n - 2
        exact = sum(mu(d) * (3 ** (n // d) - 2) for d in divisors(n))
        need(exact % n == 0 and row == {"n": n, "fixed_points": fixed,
             "exact_period_points": exact, "primitive_oriented_cycles": exact // n}, "period values")
        checks += len(divisors(n)) + 3
    need(data["collision_boundary"] == {
        "C132_C137": "generic Mobius Bergman transfer owners, not the parity-normalized Pythagorean tree",
        "C147_C152_C157": "rational square-billiard direction families, not ternary terminating and periodic coding",
        "C193": "Markoff Vieta descent on a different Diophantine surface",
        "C241": "Luroth countable-branch atlas, not the three-branch Gamma(2) factor"}, "collisions")
    need(data["nonclaims"] == [
        "Finite word rows audit but do not prove the infinite symbolic theorem.",
        "Terminating primitive Pythagorean triples are not identified with periodic prime orbits.",
        "The source Artin-Mazur zeta and Gamma(2) factor statement are not target Euler factors, automorphy, or target RH claims.",
        "No literature-priority, target local datum, root number, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted."], "nonclaims")
    need(data["references"] == [{"authors": "Dan Romik", "title": "The dynamics of Pythagorean triples",
          "identifier": "DOI:10.1090/S0002-9947-08-04467-X; arXiv:math/0406512"}], "references")
    evaluation = strict_yaml(args.evaluation)
    yaml_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
                 "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
                 "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
                 "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                 "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
                 "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                 "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    exact_keys(evaluation, yaml_keys, "evaluation")
    lock = data["route_a_yaml"]
    exact_keys(lock, {"relative_path", "raw_sha256", "semantic_sha256"}, "YAML lock")
    need(lock["relative_path"] == "evaluations/route_a/HCS-C330/2026-09-03.yaml", "YAML path")
    raw = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(raw == lock["raw_sha256"] == YAML_RAW and semantic == lock["semantic_sha256"] == YAML_SEMANTIC, "YAML hashes")
    route = {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
             "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}
    need(data["route_a"] == route and evaluation["tuple"] == route["tuple"] and
         evaluation["overall_verdict"] == route["overall"] and evaluation["route_b_invocation_allowed"] is False, "route")
    for branch in ("a0", "a1", "a2", "a3", "a4"):
        exact_keys(evaluation[branch], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, branch)
    need([evaluation[x]["verdict"] for x in ("a0", "a1", "a2", "a3", "a4")] == route["tuple"], "gate verdicts")
    need([evaluation[x]["evidence_status"] for x in ("a0", "a1", "a2", "a3", "a4")] ==
         ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"], "gate statuses")
    need(evaluation["schema"] == "route-a-evaluation-v0.2.0" and evaluation["candidate_id"] == "HCS-C330" and
         evaluation["obstruction_id"] == "HEN-O314" and evaluation["evaluation_date"] == "2026-09-03" and
         evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == 1788393600 and
         evaluation["scope_literal"] == SCOPE, "YAML identity")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and
         evaluation["evaluator_version"] == "0.2.0" and evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(evaluation["artifact_paths"] == ["results/c330_romik_pythagorean_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "artifacts")
    need(evaluation["scope_flags"] == FLAGS and data["scope_flags"] == FLAGS, "scope flags")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED" and
         evaluation["finite_evidence_role"] == "exact finite-word regression audit only, never proof by finite extrapolation" and
         evaluation["route_b_lock_reason"] == "exploratory Route A status does not authorize Route B under the scope firewall" and
         evaluation["source_owner_tokens"] == ["DOI:10.1090/S0002-9947-08-04467-X", "arXiv:math/0406512"], "YAML semantics")
    exact_keys(data["enumeration"], {"word_rows", "tree_nodes_including_root", "hyperbolic_word_rows",
               "parabolic_boundary_rows", "period_count_rows", "audited_leaf_count"}, "enumeration")
    counted = dict(data)
    counted.pop("payload_sha256")
    enumeration = counted.pop("enumeration")
    need(enumeration == {"word_rows": 9840, "tree_nodes_including_root": 9841,
                         "hyperbolic_word_rows": 9824, "parabolic_boundary_rows": 16,
                         "period_count_rows": 12, "audited_leaf_count": leaves(counted)}, "enumeration values")
    print(f"C330 independent checker: PASS ({checks} exact checks, 9840 words, 12 count rows)")


if __name__ == "__main__":
    main()
