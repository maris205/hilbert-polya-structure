#!/usr/bin/env python3
"""Independent strict checker for the HCS-C301 evidence and Route-A YAML."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c301_fragmentation_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C301/2026-09-02.yaml"
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
    "state_space": "labelled set partitions of [n]",
    "initial_state": "the one-block partition",
    "update": "each label independently receives a fresh fair bit; every block is refined by its two bit fibres and empty fibres are deleted",
    "one_step_kernel": "K_n(pi,sigma)=2^(|pi|-n) exactly when sigma refines pi and each pi-block contains at most two sigma-blocks; otherwise 0",
    "t_step_kernel": "K_n^t(pi,sigma)=1_{sigma refines pi} product_{B in pi} (2^t)_{r_B}/(2^t)^{|B|}",
    "encoding": "canonical restricted-growth strings on labels 1,...,n",
}
THEOREM = {
    "partition_law": "P(Pi_t=sigma)=(2^t)_{|sigma|}/(2^t)^n",
    "block_count_law": "P(K_t=k)=S(n,k)(2^t)_k/(2^t)^n",
    "expected_blocks": "E[K_t]=2^t[1-(1-2^{-t})^n]",
    "absorption_cdf": "P(T_n<=t)=(2^t)_n/(2^t)^n",
    "absorption_mass": "P(T_n=t)=P(T_n<=t)-P(T_n<=t-1), with the t=-1 CDF set to 0",
    "mean_absorption_time": "E[T_n]=sum_{t>=0}[1-(2^t)_n/(2^t)^n]",
    "characteristic_polynomial": "chi_n(x)=product_{k=1}^n (x-2^{k-n})^{S(n,k)}",
    "spectral_determinant": "det(I-zK_n)=product_{k=1}^n (1-z 2^{k-n})^{S(n,k)}",
    "trace": "tr(K_n^t)=sum_{k=1}^n S(n,k)2^{t(k-n)}",
    "diagonalizability": "product_{k=1}^n(K_n-2^{k-n}I)=0, hence K_n is diagonalizable over Q",
    "critical_limit": "if n_j tends to infinity and n_j^2/2^{t_j} tends to lambda in (0,infinity), then P(T_{n_j}<=t_j) tends to exp(-lambda/2)",
    "lattice_boundary": "a phase-free continuous limit for T_n-2 log_2 n is not asserted because integer t and dyadic scaling retain subsequence phase",
}
PROOF_CERTIFICATES = {
    "semigroup_word": "after t rounds, each label carries an independent uniform word in {0,1}^t; blocks are equal-word fibres inside starting blocks",
    "kernel_count": "for r target fibres in a source block, injective word assignments number (2^t)_r",
    "spectrum_guard": "rank ordering makes K block upper triangular with scalar diagonal 2^{k-n}I on rank k; recursive block elimination gives the squarefree annihilator, not diagonal entries alone",
    "birthday_limit": "log product_{j=0}^{n-1}(1-j/q)=-n(n-1)/(2q)+O(n^3/q^2) when n^2/q is bounded",
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted.",
    "The finite-state Markov determinant is source-local and is not identified with an arithmetic zeta or L-function.",
    "No literature-priority claim is made for fragmentation chains, occupancy laws, birthday asymptotics, or Hopf-algebraic Markov chains.",
]
COLLISION = {
    "C194": "C194 owns Holte carries and the base/riffle semigroup; C301 refines labelled set partitions by independent bit words and studies absorption at label separation.",
    "C215": "C215 owns continuous-time Kingman coalescence; C301 moves in the reverse refinement direction with synchronous discrete updates.",
    "C276": "C276 owns one marked orbit in a uniform random mapping; C301 separates all labels and has a logarithmic last-collision threshold.",
    "integer_partition_warning": "quotienting to unlabelled block-size partitions changes state multiplicities and is outside the theorem.",
}

EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C301",
    "title": "Parallel binary refinement of labelled set partitions",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": 1788307200,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O285",
    "candidate_definition": "A synchronous discrete-time Markov chain on labelled set partitions: every label draws a fresh fair bit and each block is refined by its two nonempty bit fibres.",
    "family": "parallel fragmentation and occupancy dynamics",
    "phase_space": "the Bell-number state space of labelled set partitions of [n]",
    "dynamics": "monotone refinement by independent fresh binary marks",
    "parameters": "all integers n>=1 and discrete times t>=0",
    "parameter_provenance": "the theorem is uniform in n and t; n<=9 exact tables are regression evidence only",
    "arithmetic_origin": "none; all labels, bits, and eigenvalues are finite stochastic-combinatorial data",
    "clock": "ordinary integer update time t",
    "normalization": "empty bit fibres are deleted and partitions retain element labels",
    "determinant_convention": "the determinant is that of the finite Bell(n)-state transition matrix",
    "orbit_cutoff": "global theorem; finite state tables stop at n=6 and time-law tables at n=9,t=8",
    "precision": "exact integers and reduced rationals; decimal critical-window rows are diagnostics only",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": [
        "results/c301_fragmentation_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf",
    ],
    "a0": {
        "verdict": "A0_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "all transition probabilities and spectral multiplicities are exact finite combinatorics",
        "strongest_failure": "no arithmetic local datum or target Euler factor is constructed",
        "artifacts": ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    },
    "a1": {
        "verdict": "A1_FAIL",
        "evidence_status": "absorbing-refinement obstruction",
        "strongest_evidence": "the full finite-state transition determinant is explicit",
        "strongest_failure": "monotone refinement has no nonconstant recurrent primitive cycles or repetition law",
        "artifacts": ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    },
    "a2": {
        "verdict": "A2_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "integer time creates the occupancy scale q=2^t",
        "strongest_failure": "q=2^t is not a rational-prime norm and time is not an arithmetic logarithmic clock",
        "artifacts": ["THEOREM_PACKAGE.md"],
    },
    "a3": {
        "verdict": "A3_FAIL",
        "evidence_status": "exact negative classification",
        "strongest_evidence": "det(I-zK_n) has a complete finite factorization",
        "strongest_failure": "the source-local polynomial is not a target completed determinant and supplies no target functional equation",
        "artifacts": ["THEOREM_PACKAGE.md", "results/c301_fragmentation_evidence.json"],
    },
    "a4": {
        "verdict": "A4_FAIL",
        "evidence_status": "no certified lift",
        "strongest_evidence": "K_n is diagonalizable over Q with real eigenvalues",
        "strongest_failure": "a stochastic refinement matrix is not a self-adjoint target-zero operator and no natural arithmetic quantization is constructed",
        "artifacts": ["SOURCE_AUDIT.md", "paper/main.pdf"],
    },
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; word coupling, spectral flag argument, absorption law, and critical limit are global",
    "source_owner_tokens": ["arXiv:1206.3620", "doi:10.1007/s10801-013-0456-7"],
}


class Count:
    value = 0


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    Count.value += 1


def reject_duplicate_keys(pairs):
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
    if len(raw) > 32_000_000:
        raise ValueError("JSON exceeds size budget")
    text = raw.decode("utf-8", errors="strict")
    value = json.loads(text, object_pairs_hook=reject_duplicate_keys, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON top level must be an object")
    canonical = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if text != canonical:
        raise ValueError("JSON is not canonical pretty serialization")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
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
        return len(actual) == len(expected) and all(exact_tree(a, e) for a, e in zip(actual, expected))
    return actual == expected


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def parse_rat(text: str) -> Fraction:
    check(type(text) is str and re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text) is not None,
          "noncanonical rational")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    check(canonical == text, "unreduced rational")
    return value


def falling(q: int, k: int) -> int:
    if k > q:
        return 0
    product = 1
    for value in range(q - k + 1, q + 1):
        product *= value
    return product


def stirling(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return sum((-1) ** (k - j) * math.comb(k, j) * j**n for j in range(k + 1)) // math.factorial(k)


def independent_partitions(n: int) -> list[tuple[int, ...]]:
    partitions: list[tuple[tuple[int, ...], ...]] = [((0,),)]
    for label in range(1, n):
        new = []
        for partition in partitions:
            for block_index in range(len(partition)):
                blocks = list(partition)
                blocks[block_index] = blocks[block_index] + (label,)
                new.append(tuple(blocks))
            new.append(partition + ((label,),))
        partitions = new
    encodings = []
    for partition in partitions:
        labels = [0] * n
        for block_index, block in enumerate(partition):
            for label in block:
                labels[label] = block_index
        encodings.append(tuple(labels))
    return sorted(encodings)


def refines(source: tuple[int, ...], target: tuple[int, ...]) -> bool:
    owners = {}
    for s, t in zip(source, target):
        if t in owners and owners[t] != s:
            return False
        owners[t] = s
    children = {}
    for s, t in zip(source, target):
        children.setdefault(s, set()).add(t)
    return all(len(values) <= 2 for values in children.values())


def expected_transitions(source: tuple[int, ...], states: list[tuple[int, ...]]) -> list[dict]:
    probability = Fraction(2 ** (1 + max(source) - len(source)))
    return [
        {
            "target_rgs": "".join(map(str, target)),
            "numerator": probability.numerator,
            "denominator": probability.denominator,
        }
        for target in states if refines(source, target)
    ]


def check_evidence(data: dict) -> None:
    expected_top = {
        "schema", "candidate_id", "obstruction_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority_sha256", "model", "theorem",
        "proof_certificates", "stirling_table", "transition_regression", "time_regression",
        "absorption_mass_regression", "critical_window_diagnostics", "route_a", "scope_flags",
        "nonclaims", "collision_boundary", "regression_summary", "payload_sha256",
    }
    check(set(data) == expected_top, "top-level evidence schema")
    check(data["schema"] == "hcs-c301-parallel-binary-fragmentation-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C301", "candidate")
    check(data["obstruction_id"] == "HEN-O285", "obstruction")
    check(data["title"] == "Parallel binary refinement of labelled set partitions", "title")
    check(data["evaluation_date"] == "2026-09-02", "date")
    check(data["source_commit"] == SOURCE, "source")
    check(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == 1788307200, "epoch")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator_authority_sha256"] == EVALUATOR, "evaluator")
    check(exact_tree(data["model"], MODEL), "model semantics")
    check(exact_tree(data["theorem"], THEOREM), "theorem semantics")
    check(exact_tree(data["proof_certificates"], PROOF_CERTIFICATES), "proof certificates")
    check(exact_tree(data["scope_flags"], FLAGS), "scope flags")
    check(exact_tree(data["nonclaims"], NONCLAIMS), "nonclaims")
    check(exact_tree(data["collision_boundary"], COLLISION), "collision boundary")
    route = data["route_a"]
    check(set(route) == {"tuple", "overall_verdict", "route_b_invocation_allowed", "obstruction"}, "route keys")
    check(exact_tree(route["tuple"], TUPLE), "route tuple")
    check(route["overall_verdict"] == "ROUTE_A_REJECTED", "route verdict")
    check(type(route["route_b_invocation_allowed"]) is bool and not route["route_b_invocation_allowed"], "route B lock")
    check(route["obstruction"] == "absorbing refinement has no nonconstant recurrent primitive cycles, and its finite Markov determinant supplies no arithmetic local datum, logarithmic prime clock, target completed determinant, divisor law, or self-adjoint target-zero lift", "route obstruction")
    check(data["payload_sha256"] == payload_hash(data), "payload digest")

    table = data["stirling_table"]
    check(type(table) is list and len(table) == 13, "Stirling row count")
    for n, row in enumerate(table):
        check(set(row) == {"n", "S_n_k_k_0_to_n"}, "Stirling row keys")
        check(type(row["n"]) is int and row["n"] == n, "Stirling n")
        expected = [stirling(n, k) for k in range(n + 1)]
        check(row["S_n_k_k_0_to_n"] == expected, "Stirling values")

    transition = data["transition_regression"]
    check(set(transition) == {"n_max", "matrix_cells_including_zeros", "listed_nonzero_probability_cells", "groups"}, "transition keys")
    check(transition["n_max"] == 6, "transition cutoff")
    groups = transition["groups"]
    check(type(groups) is list and len(groups) == 6, "transition group count")
    state_rows = zero_cells = nonzero_cells = 0
    for n, group in enumerate(groups, 1):
        states = independent_partitions(n)
        check(set(group) == {"n", "bell_number", "rows"}, "transition group keys")
        check(group["n"] == n and group["bell_number"] == len(states), "Bell count")
        check(type(group["rows"]) is list and len(group["rows"]) == len(states), "state rows")
        for state, row in zip(states, group["rows"]):
            check(set(row) == {"state_rgs", "rank", "transitions"}, "state row keys")
            check(row["state_rgs"] == "".join(map(str, state)), "state encoding")
            check(row["rank"] == 1 + max(state), "state rank")
            expected = expected_transitions(state, states)
            check(exact_tree(row["transitions"], expected), "independent kernel reconstruction")
            check(sum(Fraction(item["numerator"], item["denominator"]) for item in row["transitions"]) == 1, "row stochasticity")
            state_rows += 1
            zero_cells += len(states)
            nonzero_cells += len(expected)
    check(transition["matrix_cells_including_zeros"] == zero_cells, "matrix cell count")
    check(transition["listed_nonzero_probability_cells"] == nonzero_cells, "nonzero cell count")

    time = data["time_regression"]
    check(set(time) == {"n_max", "t_max", "row_count", "block_count_coefficient_cells", "rows"}, "time keys")
    check(time["n_max"] == 9 and time["t_max"] == 8, "time cutoffs")
    check(time["row_count"] == 81 and len(time["rows"]) == 81, "time row count")
    coefficient_cells = 0
    for index, row in enumerate(time["rows"]):
        n, t = index // 9 + 1, index % 9
        q = 2**t
        expected_keys = {"n", "t", "q", "block_count_k_1_to_n_numerators", "common_denominator", "mass_sum_numerator", "expected_blocks", "absorption_cdf", "trace_K_power_t", "eigenvalue_multiplicities_by_rank"}
        check(set(row) == expected_keys, "time row keys")
        check(row["n"] == n and row["t"] == t and row["q"] == q, "time coordinates")
        numerators = [stirling(n, k) * falling(q, k) for k in range(1, n + 1)]
        check(row["block_count_k_1_to_n_numerators"] == numerators, "block law coefficients")
        check(row["common_denominator"] == q**n, "block law denominator")
        check(row["mass_sum_numerator"] == sum(numerators) == q**n, "occupancy normalization")
        expectation = Fraction(q**n - (q - 1) ** n, q ** (n - 1))
        check(parse_rat(row["expected_blocks"]) == expectation, "expected blocks")
        check(parse_rat(row["absorption_cdf"]) == Fraction(falling(q, n), q**n), "absorption CDF")
        trace = sum(Fraction(stirling(n, k), 2 ** (t * (n - k))) for k in range(1, n + 1))
        check(parse_rat(row["trace_K_power_t"]) == trace, "trace formula")
        check(row["eigenvalue_multiplicities_by_rank"] == [stirling(n, k) for k in range(1, n + 1)], "spectral multiplicities")
        coefficient_cells += n
    check(time["block_count_coefficient_cells"] == coefficient_cells == 405, "coefficient cell count")

    mass_rows = data["absorption_mass_regression"]
    check(type(mass_rows) is list and len(mass_rows) == 104, "absorption mass rows")
    for index, row in enumerate(mass_rows):
        n, t = index // 13 + 1, index % 13
        check(set(row) == {"n", "t", "cdf", "mass"}, "mass row keys")
        current = Fraction(falling(2**t, n), 2 ** (t * n))
        previous = Fraction(0) if t == 0 else Fraction(falling(2 ** (t - 1), n), 2 ** ((t - 1) * n))
        check(row["n"] == n and row["t"] == t, "mass row coordinates")
        check(parse_rat(row["cdf"]) == current, "mass CDF")
        check(parse_rat(row["mass"]) == current - previous, "absorption mass")

    diagnostics = data["critical_window_diagnostics"]
    check(type(diagnostics) is list and len(diagnostics) == 5, "diagnostic rows")
    for row, n in zip(diagnostics, (32, 64, 128, 256, 512)):
        t = 2 * int(math.log2(n)); q = 2**t
        cdf = Fraction(falling(q, n), q**n)
        check(set(row) == {"n", "t", "n_squared_over_q", "exact_cdf_decimal_12", "limit_exp_minus_half_decimal_12", "absolute_error_decimal_12"}, "diagnostic keys")
        check(row["n"] == n and row["t"] == t, "diagnostic coordinates")
        check(parse_rat(row["n_squared_over_q"]) == Fraction(n*n, q), "diagnostic scaling")
        check(row["exact_cdf_decimal_12"] == f"{float(cdf):.12f}", "diagnostic CDF")
        check(row["limit_exp_minus_half_decimal_12"] == f"{math.exp(-0.5):.12f}", "diagnostic limit")
        check(row["absolute_error_decimal_12"] == f"{abs(float(cdf)-math.exp(-0.5)):.12f}", "diagnostic error")

    expected_summary = {
        "transition_state_rows": state_rows,
        "transition_nonzero_probability_cells": nonzero_cells,
        "time_rows": 81,
        "block_count_coefficient_cells": 405,
        "absorption_mass_rows": 104,
        "all_exact_probability_rows_normalized": True,
    }
    check(exact_tree(data["regression_summary"], expected_summary), "regression summary")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--yaml", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    evidence = strict_json(args.evidence)
    evaluation = strict_yaml(args.yaml)
    check_evidence(evidence)
    check(exact_tree(evaluation, EXPECTED_EVALUATION), "exact Route-A YAML tree")
    print(f"C301 independent checker PASS ({Count.value} assertions)")
    print(f"payload_sha256={evidence['payload_sha256']}")
    print("route_tuple=" + ",".join(evaluation["tuple"]))


if __name__ == "__main__":
    main()
