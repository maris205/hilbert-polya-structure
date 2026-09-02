#!/usr/bin/env python3
"""Independent strict checker for HCS-C302 evidence and Route-A YAML."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c302_quicksort_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C302/2026-09-02.yaml"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
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
MODEL = {
    "input": "uniform random permutation of n distinct keys",
    "pivot": "first key, equivalently a pivot rule independent of values with uniform rank",
    "partition_cost": "exactly n-1 key comparisons",
    "total_cost": "key comparisons only",
    "base_cases": "X_0=X_1=0",
    "distributional_recurrence": "X_n =d X_{I_n}+X'_{n-1-I_n}+n-1 with I_n uniform on {0,...,n-1}",
}
THEOREM = {
    "pgf": "G_n(z)=z^{n-1}/n sum_{j=0}^{n-1}G_j(z)G_{n-1-j}(z), G_0=G_1=1",
    "mean": "mu_n=2(n+1)H_n-4n",
    "variance": "v_n=7n^2-4(n+1)^2H_n^(2)-2(n+1)H_n+13n",
    "normalization": "Y_n=(X_n-mu_n)/(n+1)",
    "fixed_point": "Y =d UY_1+(1-U)Y_2+C(U)",
    "toll": "C(u)=1+2u log u+2(1-u)log(1-u), with 0 log 0=0",
    "convergence": "Y_n converges in quadratic Wasserstein distance, and under a recursive coupling in L^2, to the unique centered finite-variance fixed law",
    "limit_variance": "E[Y^2]=7-2*pi^2/3",
    "limit_third_moment": "E[Y^3]=16*zeta(3)-19>0",
    "non_gaussian": "the centered limit is nondegenerate and non-Gaussian",
}
PROOF = {
    "recursive_independence": "conditional on pivot rank, the two relative subarray orders are independent uniform permutations",
    "variance_lane": "law of total variance plus the exact mean gives the all-n variance formula",
    "contraction": "E[U^2+(1-U)^2]=2/3, so the centered transform contracts squared d_2 by 2/3",
    "endogenous_l2": "orthogonal binary-tree toll levels satisfy E[Delta_r^2]=E[C(U)^2](2/3)^r, so their series realizes the unique fixed law in L2",
    "mixed_subproblem_closure": "on one iid-uniform binary tree, e_n<=sqrt(Q_n)+delta_n with Q_n=(2/n)sum_j((j+1)/(n+1))^2e_j^2, delta_n->0, and the cutoff limsup gives D<=sqrt(2/3)D",
    "third_moment_license": "the binary-tree toll series converges in L3 by conditional Rosenthal bounds using level sums (2/3)^r and (1/2)^r",
    "third_moment": "m3=(1/2)m3+3m2 integral C(u)(u^2+(1-u)^2)du+integral C(u)^3du",
    "positivity": "zeta(3)>sum_{k=1}^6 k^{-3}=28567/24000 gives 16*zeta(3)-19>67/1500>0",
}
INTEGRALS = {
    "integral_C": "0",
    "integral_C_squared": "7/3-2*pi^2/9",
    "integral_C_times_branch_square": "1/18",
    "integral_C_cubed": "-32/3+pi^2/9+8*zeta(3)",
    "branch_square_integral": "2/3",
    "fixed_point_variance": "7-2*pi^2/3",
    "fixed_point_third_moment": "16*zeta(3)-19",
    "strict_positive_lower_bound": "67/1500",
}
NONCLAIMS = [
    "No priority is claimed for Quicksort, its comparison recurrence, limiting law, or contraction method.",
    "Finite PGFs are source probability polynomials, not target arithmetic determinants.",
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted.",
]
COLLISION = {
    "C291": "C291 owns random greedy dimer adsorption; C302 owns recursive permutation splitting and a non-Gaussian contraction fixed point.",
    "cost_warning": "swaps, assignments, recursion depth, wall-clock time, repeated keys, three-way partitioning, and sampled pivots are different models",
    "normalization_warning": "division by n has the same limit for n>=1 but is not the frozen finite recurrence, which divides by n+1",
}
SOURCES = [
    "doi:10.1093/comjnl/5.1.10",
    "NUMDAM:ITA_1989__23_3_335_0",
    "NUMDAM:ITA_1991__25_1_85_0",
]

EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C302",
    "title": "Exact Quicksort comparison costs and contraction limit",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": 1788307200,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O286",
    "candidate_definition": "Classical single-pivot Quicksort on a uniform random permutation of n distinct keys, with first-key pivot and key comparisons as the only cost.",
    "family": "recursive divide-and-conquer cost dynamics and distributional contraction",
    "phase_space": "comparison-count laws indexed by input size n",
    "dynamics": "uniform pivot-rank split into two conditionally independent recursive subproblems",
    "parameters": "all integers n>=0; limit along n tending to infinity",
    "parameter_provenance": "all finite n are analytic; exact PGF regression stops at n=12",
    "arithmetic_origin": "none; ranks, permutations, costs, harmonic sums, and zeta(3) moment constants are source probability data",
    "clock": "input size n is an external recursion parameter, not intrinsic dynamical time",
    "normalization": "Y_n=(X_n-mu_n)/(n+1)",
    "determinant_convention": "none; G_n is a probability-generating polynomial and is not promoted to a determinant",
    "orbit_cutoff": "global recurrence and contraction theorem; finite coefficient tables stop at n=12",
    "precision": "exact rational coefficients and symbolic pi^2/zeta(3) integrals; decimal variance rows are diagnostics only",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c302_quicksort_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": {
        "verdict": "A0_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "all finite cost laws are exact rational PGFs",
        "strongest_failure": "no arithmetic local datum or target Euler factor is constructed",
        "artifacts": ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    },
    "a1": {
        "verdict": "A1_FAIL",
        "evidence_status": "recursive-tree obstruction",
        "strongest_evidence": "the cost has a complete recursive split law",
        "strongest_failure": "the recursion tree is not a primitive periodic-orbit ledger with repetition weights",
        "artifacts": ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    },
    "a2": {
        "verdict": "A2_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "input size controls the normalization and harmonic mean",
        "strongest_failure": "n is an external size parameter, not an intrinsic arithmetic logarithmic clock",
        "artifacts": ["THEOREM_PACKAGE.md"],
    },
    "a3": {
        "verdict": "A3_FAIL",
        "evidence_status": "type-separation obstruction",
        "strongest_evidence": "every finite PGF is explicitly computable",
        "strongest_failure": "a probability polynomial is not a target completed determinant and supplies no target functional equation",
        "artifacts": ["THEOREM_PACKAGE.md", "results/c302_quicksort_evidence.json"],
    },
    "a4": {
        "verdict": "A4_FAIL",
        "evidence_status": "no certified lift",
        "strongest_evidence": "the limiting law is the unique fixed point of a Wasserstein contraction",
        "strongest_failure": "the distributional transform is not a same-clock self-adjoint target-zero operator",
        "artifacts": ["SOURCE_AUDIT.md", "paper/main.pdf"],
    },
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; the all-n PGF recurrence, moment formulas, and limiting contraction theorem are analytic",
    "source_owner_tokens": SOURCES,
}


class CounterAssertions:
    value = 0


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    CounterAssertions.value += 1


def check_int(value, expected: int, message: str) -> None:
    """Reject bool/float aliases at every integer count or coordinate."""
    check(type(value) is int and value == expected, message)


def duplicate_guard(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) > 24_000_000:
        raise ValueError("JSON size budget exceeded")
    text = raw.decode("utf-8", errors="strict")
    value = json.loads(text, object_pairs_hook=duplicate_guard, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON top level must be an object")
    if text != json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n":
        raise ValueError("JSON is not canonical pretty serialization")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise TypeError("YAML keys must be strings")
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return value


def exact_tree(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree(actual[k], expected[k]) for k in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree(a, b) for a, b in zip(actual, expected))
    return actual == expected


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def parse_rat(text: str) -> Fraction:
    check(type(text) is str and re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text) is not None,
          "rational syntax")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    check(text == canonical, "rational reduction")
    return value


def harmonic(n: int, power: int = 1) -> Fraction:
    return sum((Fraction(1, k**power) for k in range(1, n+1)), Fraction())


def mean(n: int) -> Fraction:
    return 2*(n+1)*harmonic(n)-4*n


def variance(n: int) -> Fraction:
    return 7*n*n-4*(n+1)**2*harmonic(n, 2)-2*(n+1)*harmonic(n)+13*n


def quicksort_cost(permutation: tuple[int, ...]) -> int:
    if len(permutation) < 2:
        return 0
    pivot = permutation[0]
    left = tuple(value for value in permutation[1:] if value < pivot)
    right = tuple(value for value in permutation[1:] if value > pivot)
    return len(permutation)-1+quicksort_cost(left)+quicksort_cost(right)


def exhaustive_counts(n: int) -> Counter[int]:
    if n == 0:
        return Counter({0: 1})
    return Counter(quicksort_cost(p) for p in itertools.permutations(range(n)))


def integer_recurrence(n_max: int) -> list[Counter[int]]:
    laws = [Counter({0: 1}), Counter({0: 1})]
    for n in range(2, n_max+1):
        row: Counter[int] = Counter()
        for j in range(n):
            interleavings = math.comb(n-1, j)
            for left_cost, left_count in laws[j].items():
                for right_cost, right_count in laws[n-1-j].items():
                    row[n-1+left_cost+right_cost] += interleavings*left_count*right_count
        check(sum(row.values()) == math.factorial(n), "integer recurrence normalization")
        laws.append(row)
    return laws[:n_max+1]


def check_evidence(data: dict, exhaustive: bool = True) -> None:
    top = {
        "schema", "candidate_id", "obstruction_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority_sha256", "model", "theorem",
        "proof_certificates", "finite_pgf_regression", "centered_recursion_regression",
        "limit_integrals", "variance_limit_diagnostics", "route_a", "scope_flags", "nonclaims",
        "collision_boundary", "source_owner_tokens", "regression_summary", "payload_sha256",
    }
    check(set(data) == top, "top-level schema")
    check(data["schema"] == "hcs-c302-quicksort-comparison-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C302", "candidate")
    check(data["obstruction_id"] == "HEN-O286", "obstruction")
    check(data["title"] == "Exact Quicksort comparison costs and contraction limit", "title")
    check(data["evaluation_date"] == "2026-09-02", "date")
    check(data["source_commit"] == SOURCE, "source")
    check_int(data["fixed_epoch"], 1788307200, "epoch type")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator_authority_sha256"] == EVALUATOR, "evaluator")
    check(exact_tree(data["model"], MODEL), "model")
    check(exact_tree(data["theorem"], THEOREM), "theorem")
    check(exact_tree(data["proof_certificates"], PROOF), "proof certificates")
    check(exact_tree(data["limit_integrals"], INTEGRALS), "integral receipt")
    check(exact_tree(data["scope_flags"], FLAGS), "flags")
    check(exact_tree(data["nonclaims"], NONCLAIMS), "nonclaims")
    check(exact_tree(data["collision_boundary"], COLLISION), "collision")
    check(data["source_owner_tokens"] == SOURCES, "sources")
    route = data["route_a"]
    check(set(route) == {"tuple", "overall_verdict", "route_b_invocation_allowed", "obstruction"}, "route keys")
    check(route["tuple"] == TUPLE, "route tuple")
    check(route["overall_verdict"] == "ROUTE_A_REJECTED", "route verdict")
    check(type(route["route_b_invocation_allowed"]) is bool and route["route_b_invocation_allowed"] is False, "route B")
    check(route["obstruction"] == "recursive comparison-cost distributions have no arithmetic local carrier, primitive orbit ledger, intrinsic logarithmic prime clock, target determinant, divisor law, or same-clock self-adjoint zero lift", "route obstruction")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")

    recurrence = integer_recurrence(12)
    finite = data["finite_pgf_regression"]
    check(type(finite) is dict and set(finite) == {"n_max", "row_count", "coefficient_cells", "rows"}, "finite keys")
    check_int(finite["n_max"], 12, "finite n_max")
    check_int(finite["row_count"], 13, "finite row_count")
    check(type(finite["rows"]) is list and len(finite["rows"]) == 13, "finite rows length")
    coefficient_cells = 0
    for n, row in enumerate(finite["rows"]):
        keys = {"n", "coefficient_count", "support_min", "support_max", "coefficients", "probability_sum", "permutation_count_sum", "raw_moment_1", "raw_moment_2", "raw_moment_3", "variance_from_coefficients", "third_centered_moment", "mean_formula", "variance_formula", "normalized_variance_n_plus_1", "normalized_third_centered_n_plus_1"}
        check(type(row) is dict and set(row) == keys, "finite row schema")
        check_int(row["n"], n, "finite row coordinate")
        counts = recurrence[n]
        expected_entries = []
        for cost, count in sorted(counts.items()):
            probability = Fraction(count, math.factorial(n))
            expected_entries.append({"comparisons": cost, "numerator": probability.numerator,
                                     "denominator": probability.denominator, "permutation_count": count})
        check(exact_tree(row["coefficients"], expected_entries), "integer recurrence coefficients")
        if exhaustive and n <= 9:
            check(exhaustive_counts(n) == counts, "full permutation enumeration")
        check_int(row["coefficient_count"], len(counts), "coefficient count")
        check_int(row["support_min"], min(counts), "support minimum")
        check_int(row["support_max"], max(counts), "support maximum")
        check(parse_rat(row["probability_sum"]) == 1, "probability sum")
        check_int(row["permutation_count_sum"], math.factorial(n), "permutation count sum")
        law = {cost: Fraction(count, math.factorial(n)) for cost, count in counts.items()}
        raw = [sum((Fraction(cost**r)*p for cost,p in law.items()), Fraction()) for r in (1,2,3)]
        var = raw[1]-raw[0]**2
        third_centered = raw[2]-3*raw[0]*raw[1]+2*raw[0]**3
        check(parse_rat(row["raw_moment_1"]) == raw[0], "raw mean")
        check(parse_rat(row["raw_moment_2"]) == raw[1], "raw second")
        check(parse_rat(row["raw_moment_3"]) == raw[2], "raw third")
        check(parse_rat(row["variance_from_coefficients"]) == var == variance(n), "variance")
        check(parse_rat(row["third_centered_moment"]) == third_centered, "third centered")
        check(parse_rat(row["mean_formula"]) == raw[0] == mean(n), "mean formula")
        check(parse_rat(row["variance_formula"]) == var, "variance formula")
        check(parse_rat(row["normalized_variance_n_plus_1"]) == var/(n+1)**2, "n+1 variance")
        check(parse_rat(row["normalized_third_centered_n_plus_1"]) == third_centered/(n+1)**3, "n+1 third")
        coefficient_cells += len(counts)
    check_int(finite["coefficient_cells"], coefficient_cells, "total coefficient cell type/count")
    check(coefficient_cells == 173, "total coefficient cell recomputation")

    centered = data["centered_recursion_regression"]
    check(type(centered) is dict and set(centered) == {"n_min", "n_max", "group_count", "pivot_rows", "groups"}, "centered keys")
    check_int(centered["n_min"], 2, "centered n_min")
    check_int(centered["n_max"], 32, "centered n_max")
    check_int(centered["group_count"], 31, "centered group_count")
    check(type(centered["groups"]) is list and len(centered["groups"]) == 31, "centered groups length")
    pivot_rows = 0
    for offset, n in enumerate(range(2,33)):
        group = centered["groups"][offset]
        check(type(group) is dict and set(group) == {"n", "pivot_count", "mean_centered_toll", "coefficient_square_average", "toll_square_average", "rows"}, "center group keys")
        check_int(group["n"], n, "center group coordinate")
        check_int(group["pivot_count"], n, "center group pivot_count")
        check(type(group["rows"]) is list and len(group["rows"]) == n, "center group row length")
        tolls=[]; square=Fraction(); toll_square=Fraction()
        for j, row in enumerate(group["rows"]):
            check(type(row) is dict and set(row) == {"pivot_left_size", "left_coefficient", "right_coefficient", "coefficient_sum", "centered_toll"}, "pivot row keys")
            a=Fraction(j+1,n+1); b=Fraction(n-j,n+1)
            c=(Fraction(n-1)+mean(j)+mean(n-1-j)-mean(n))/(n+1)
            check_int(row["pivot_left_size"], j, "pivot size")
            check(parse_rat(row["left_coefficient"]) == a, "left coefficient")
            check(parse_rat(row["right_coefficient"]) == b, "right coefficient")
            check(parse_rat(row["coefficient_sum"]) == a+b == 1, "coefficient sum")
            check(parse_rat(row["centered_toll"]) == c, "finite centered toll")
            tolls.append(c); square += a*a+b*b; toll_square += c*c
            pivot_rows += 1
        check(sum(tolls)/n == parse_rat(group["mean_centered_toll"]) == 0, "centered toll mean")
        check(square/n == parse_rat(group["coefficient_square_average"]), "branch square average")
        check(toll_square/n == parse_rat(group["toll_square_average"]), "toll square average")
    check_int(centered["pivot_rows"], pivot_rows, "pivot row type/count")
    check(pivot_rows == 527, "pivot row recomputation")

    diagnostics = data["variance_limit_diagnostics"]
    check(type(diagnostics) is list and len(diagnostics) == 6, "diagnostics")
    limit = 7-2*math.pi**2/3
    for row,n in zip(diagnostics,(8,16,32,64,128,256)):
        exact=variance(n)/(n+1)**2
        check(type(row) is dict and set(row) == {"n", "normalized_variance_exact", "normalized_variance_decimal_12", "limit_variance_decimal_12", "absolute_error_decimal_12"}, "diagnostic keys")
        check_int(row["n"], n, "diagnostic coordinate")
        check(parse_rat(row["normalized_variance_exact"]) == exact, "diagnostic exact")
        check(row["normalized_variance_decimal_12"] == f"{float(exact):.12f}", "diagnostic decimal")
        check(row["limit_variance_decimal_12"] == f"{limit:.12f}", "diagnostic limit")
        check(row["absolute_error_decimal_12"] == f"{abs(float(exact)-limit):.12f}", "diagnostic error")

    partial = sum((Fraction(1,k**3) for k in range(1,7)), Fraction())
    check(partial == Fraction(28567,24000), "zeta partial sum")
    check(16*partial-19 == Fraction(67,1500) > 0, "third moment lower bound")
    summary = {
        "finite_pgf_rows": 13,
        "pgf_coefficient_cells": 173,
        "centered_pivot_rows": 527,
        "variance_diagnostic_rows": 6,
        "all_probability_rows_normalized": True,
        "normalization_denominator": "n+1",
    }
    check(exact_tree(data["regression_summary"], summary), "summary")
    for key in ("finite_pgf_rows", "pgf_coefficient_cells", "centered_pivot_rows", "variance_diagnostic_rows"):
        check_int(data["regression_summary"][key], summary[key], f"summary integer {key}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--yaml", type=Path, default=DEFAULT_YAML)
    parser.add_argument("--skip-exhaustive", action="store_true",
                        help="internal mutation-harness mode; release validation never uses it")
    args = parser.parse_args()
    evidence = strict_json(args.evidence)
    evaluation = strict_yaml(args.yaml)
    check_evidence(evidence, exhaustive=not args.skip_exhaustive)
    check(exact_tree(evaluation, EXPECTED_EVALUATION), "exact Route-A YAML tree")
    print(f"C302 independent checker PASS ({CounterAssertions.value} assertions)")
    print(f"payload_sha256={evidence['payload_sha256']}")
    print("route_tuple="+",".join(evaluation["tuple"]))


if __name__ == "__main__":
    main()
