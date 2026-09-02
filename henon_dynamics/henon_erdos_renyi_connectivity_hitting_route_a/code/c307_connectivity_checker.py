#!/usr/bin/env python3
"""Independent strict checker for HCS-C307 evidence and Route-A YAML."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import yaml

if sys.flags.optimize:
    raise RuntimeError("HCS-C307 checker refuses python -O: validation must not be disabled")

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c307_connectivity_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C307/2026-09-03.yaml"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
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
    "edges": "a uniformly random permutation of the K=binom(n,2) edges of the complete labeled graph",
    "state": "G_m contains the first m edges and is uniform on G(n,m)",
    "hitting_time": "tau_conn=min{m:G_m is connected}, with tau_conn=0 for n=1",
    "monotonicity": "edges are added without replacement and connectivity is absorbing",
}
THEOREM = {
    "recurrence": "C(n,m)=binom(K,m)-sum_{s=1}^{n-1}binom(n-1,s-1)sum_j C(s,j)binom(binom(n-s,2),m-j)",
    "base": "C(1,0)=1 and out-of-range binomial coefficients are zero",
    "support": "for n>=2, C(n,m)=0 below n-1, C(n,n-1)=n^(n-2), and C(n,K)=1",
    "cdf": "P(tau_conn<=m)=C(n,m)/binom(K,m)",
    "pmf": "P(tau_conn=m)=F_n(m)-F_n(m-1), with F_n(-1)=0",
    "tails": "P(tau_conn>m)=1-C(n,m)/binom(K,m)",
    "moments": "E[tau_conn^r]=sum_{m=0}^{K-1}((m+1)^r-m^r)P(tau_conn>m), r>=1",
    "last_support": "for n>=2, tau_conn<=binom(n-1,2)+1",
    "window": "m_n(c)=floor((n/2)(log n+c))",
    "gumbel": "P(2 tau_conn/n-log n<=c) tends to exp(-exp(-c)) for every real c",
}
PROOF = {
    "component_of_one": "a disconnected graph is uniquely decomposed by the size and internal edges of the component containing vertex 1",
    "uniform_slice": "the first m positions of a uniform edge permutation form a uniform m-edge subset",
    "isolated_factorial": "E[(I_n)_{r↓}]=(n)_{r↓} binom(binom(n-r,2),m)/binom(K,m), where (x)_{r↓}=x(x-1)...(x-r+1)",
    "poisson": "at m_n(c), every fixed factorial moment tends to exp(-rc), so I_n converges to Poisson(exp(-c))",
    "other_components": "a spanning-tree union bound over component sizes 2 through floor(n/2), split at n/log n, is o(1)",
    "rounding": "tau_conn is integer, so {2 tau_conn/n-log n<=c}={tau_conn<=m_n(c)} exactly",
}
BOUNDARIES = [
    "The finite process adds edges without replacement; it is not the independent-edge G(n,p) process.",
    "No pathwise identity with the disappearance time of the last isolated vertex is claimed.",
    "The Gumbel theorem is distributional; convergence of unbounded moments is not claimed.",
    "For fixed c, m_n(c) lies in [0,K] for all sufficiently large n; finite implementations clip only outside that asymptotic regime.",
    "The cases n=1 and n=2 have tau_conn=0 and tau_conn=1 respectively.",
]
COLLISION_BOUNDARY = {
    "C301": "C301 is a parallel fair-bit partition-refinement birthday process; C307 is a without-replacement graph-edge growth process stopped at connectivity.",
    "C291": "C291 is random greedy dimer adsorption on finite paths and cycles; C307 adds unused complete-graph edges and stops at the absorbing connectivity upper set.",
    "C276": "C276 samples a whole uniform random mapping and studies functional-graph components; C307 evolves simple graphs one edge at a time with exact connected-graph counts.",
}
SOURCES = ["primary:https://static.renyi.hu/~p_erdos/1960-10.pdf"]


class Count:
    value = 0


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    Count.value += 1


def check_int(value, expected: int, message: str) -> None:
    check(type(value) is int and value == expected, message)


def exact_tree(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree(actual[key], expected[key]) for key in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree(a, b) for a, b in zip(actual, expected))
    return actual == expected


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def duplicate_guard(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) > 8_000_000:
        raise ValueError("JSON size budget exceeded")
    text = raw.decode("utf-8", errors="strict")
    value = json.loads(text, object_pairs_hook=duplicate_guard, parse_constant=reject_nonfinite)
    check(type(value) is dict, "JSON top-level object")
    check(text == json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n", "canonical JSON")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("non-string or duplicate YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    check(type(value) is dict, "YAML top-level mapping")
    return value


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def parse_rat(text: str) -> Fraction:
    check(type(text) is str and re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text) is not None,
          "rational syntax")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    check(text == canonical, "reduced rational")
    return value


def parse_decimal(text: str) -> float:
    check(type(text) is str and re.fullmatch(r"(?:0|[1-9][0-9]*)\.[0-9]{12}", text) is not None,
          "decimal syntax")
    value = float(text)
    check(math.isfinite(value), "finite decimal")
    return value


def independent_table(n_max: int) -> list[list[int]]:
    # Reconstructed locally from the unique component containing the largest
    # label.  No producer code is imported or executed.
    tables: list[list[int]] = [[], [1]]
    for n in range(2, n_max + 1):
        K = choose(n, 2)
        row = []
        for m in range(K + 1):
            disconnected = 0
            for s in range(1, n):
                outside_edges = choose(n - s, 2)
                ways_inside = sum(count * choose(outside_edges, m - j)
                                  for j, count in enumerate(tables[s]))
                disconnected += choose(n - 1, s - 1) * ways_inside
            row.append(choose(K, m) - disconnected)
        tables.append(row)
    return tables


def exhaustive_counts(n: int) -> tuple[Counter[int], int]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    connected = Counter()
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a != b:
                parent[b] = a

        for bit, (a, b) in enumerate(edges):
            if mask & (1 << bit):
                union(a, b)
        if n <= 1 or all(find(i) == find(0) for i in range(1, n)):
            connected[mask.bit_count()] += 1
    return connected, 1 << len(edges)


ENTRY_KEYS = {"m", "connected_count", "total_graph_count", "cdf", "pmf", "tail"}
ROW_KEYS = {"n", "K", "cell_count", "first_possible_hitting_m", "last_possible_hitting_m",
            "tree_endpoint_count", "complete_endpoint_count", "entries", "moment_count", "moments"}
DIAG_KEYS = {"n", "c", "m", "r", "within_edge_range", "factorial_moment_decimal_12",
             "poisson_target_decimal_12", "absolute_error_decimal_12"}


def isolated_factorial(n: int, m: int, r: int) -> float:
    K = choose(n, 2)
    allowed = choose(n - r, 2)
    log_value = sum(math.log(n - j) for j in range(r))
    removed = K - allowed
    for i in range(m):
        log_value += math.log1p(-removed / (K - i))
    return math.exp(log_value)


def check_evidence(data: dict, exhaustive: bool) -> None:
    top = {"schema", "candidate_id", "obstruction_id", "title", "evaluation_date", "source_commit",
           "fixed_epoch", "scope_literal", "evaluator_authority_sha256", "model", "theorem",
           "proof_certificates", "finite_connected_atlas", "isolated_vertex_diagnostics", "route_a",
           "scope_flags", "boundaries", "collision_boundary", "source_owner_tokens",
           "regression_summary", "payload_sha256"}
    check(set(data) == top, "top-level exact keys")
    check(data["schema"] == "hcs-c307-erdos-renyi-connectivity-hitting-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C307" and data["obstruction_id"] == "HEN-O291", "ids")
    check(data["title"] == "Connectivity hitting in the random graph process: exact finite laws and the Gumbel window", "title")
    check(data["evaluation_date"] == "2026-09-03" and data["source_commit"] == SOURCE, "provenance")
    check_int(data["fixed_epoch"], EPOCH, "epoch")
    check(data["scope_literal"] == SCOPE and data["evaluator_authority_sha256"] == EVALUATOR, "authority")
    check(exact_tree(data["model"], MODEL), "model")
    check(exact_tree(data["theorem"], THEOREM), "theorem")
    check(exact_tree(data["proof_certificates"], PROOF), "proof")
    check(exact_tree(data["scope_flags"], FLAGS), "flags")
    check(exact_tree(data["boundaries"], BOUNDARIES), "boundaries")
    check(exact_tree(data["collision_boundary"], COLLISION_BOUNDARY), "collision boundary")
    check(exact_tree(data["source_owner_tokens"], SOURCES), "sources")
    route = data["route_a"]
    check(type(route) is dict and set(route) == {"tuple", "overall_verdict", "route_b_invocation_allowed", "obstruction"}, "route keys")
    check(exact_tree(route["tuple"], TUPLE), "tuple")
    check(route["overall_verdict"] == "ROUTE_A_REJECTED", "route verdict")
    check(type(route["route_b_invocation_allowed"]) is bool and route["route_b_invocation_allowed"] is False, "route B")
    check(route["obstruction"] == "the edge-addition process and its connected-graph counts provide no target arithmetic local carrier, primitive-orbit Euler ledger, intrinsic prime clock, target determinant, or same-clock self-adjoint zero lift", "obstruction")
    check(data["payload_sha256"] == payload_hash(data), "self hash")

    tables = independent_table(12)
    atlas = data["finite_connected_atlas"]
    check(type(atlas) is dict and set(atlas) == {"n_min", "n_max", "row_count", "coefficient_cells", "rows"}, "atlas keys")
    check_int(atlas["n_min"], 1, "n min")
    check_int(atlas["n_max"], 12, "n max")
    check_int(atlas["row_count"], 12, "row count")
    check(type(atlas["rows"]) is list and len(atlas["rows"]) == 12, "rows list")
    coefficient_cells = 0
    exhaustive_masks = 0
    for n, row in enumerate(atlas["rows"], start=1):
        K = choose(n, 2)
        counts = tables[n]
        check(type(row) is dict and set(row) == ROW_KEYS, "finite row keys")
        check_int(row["n"], n, "n coordinate")
        check_int(row["K"], K, "K")
        check_int(row["cell_count"], K + 1, "cell count")
        check_int(row["first_possible_hitting_m"], 0 if n == 1 else n - 1, "first support")
        check_int(row["last_possible_hitting_m"], 0 if n == 1 else choose(n - 1, 2) + 1, "last support")
        check_int(row["tree_endpoint_count"], 1 if n == 1 else n ** (n - 2), "tree endpoint")
        check_int(row["complete_endpoint_count"], 1, "complete endpoint")
        check(type(row["entries"]) is list and len(row["entries"]) == K + 1, "entries length")
        previous = Fraction(0)
        tails = []
        pmf_sum = Fraction(0)
        for m, entry in enumerate(row["entries"]):
            check(type(entry) is dict and set(entry) == ENTRY_KEYS, "entry keys")
            check_int(entry["m"], m, "m coordinate")
            check_int(entry["connected_count"], counts[m], "connected count")
            total = choose(K, m)
            check_int(entry["total_graph_count"], total, "total graph count")
            cdf = Fraction(counts[m], total)
            pmf = cdf - previous
            tail = 1 - cdf
            check(parse_rat(entry["cdf"]) == cdf, "CDF")
            check(parse_rat(entry["pmf"]) == pmf, "PMF")
            check(parse_rat(entry["tail"]) == tail, "tail")
            check(pmf >= 0 and 0 <= cdf <= 1 and 0 <= tail <= 1, "probability range/monotonicity")
            pmf_sum += pmf
            previous = cdf
            tails.append(tail)
        check(pmf_sum == 1 and previous == 1, "distribution normalization")
        if n >= 2:
            check(all(counts[m] == 0 for m in range(n - 1)), "lower support zero")
            check(counts[n - 1] == n ** (n - 2), "Cayley endpoint")
            check(counts[K] == 1, "complete graph endpoint")
            last = choose(n - 1, 2) + 1
            check(all(counts[m] == choose(K, m) for m in range(last, K + 1)), "guaranteed connectivity edge range")
        check_int(row["moment_count"], 4, "moment count")
        check(type(row["moments"]) is list and len(row["moments"]) == 4, "moment list")
        for order, moment_row in enumerate(row["moments"], start=1):
            check(type(moment_row) is dict and set(moment_row) == {"order", "raw_moment"}, "moment keys")
            check_int(moment_row["order"], order, "moment order")
            expected = sum((Fraction((m + 1) ** order - m ** order) * tails[m] for m in range(K)), Fraction())
            check(parse_rat(moment_row["raw_moment"]) == expected, "tail-sum moment")
        coefficient_cells += K + 1
        if exhaustive and n <= 6:
            enumerated, masks = exhaustive_counts(n)
            exhaustive_masks += masks
            check(all(enumerated[m] == counts[m] for m in range(K + 1)), "exhaustive graph masks")
    check_int(atlas["coefficient_cells"], coefficient_cells, "coefficient cells")

    diagnostics = data["isolated_vertex_diagnostics"]
    check(type(diagnostics) is dict and set(diagnostics) == {"row_count", "n_values", "c_values", "orders", "rows"}, "diagnostic keys")
    check(exact_tree(diagnostics["n_values"], [50, 100, 200, 400, 800]), "diagnostic n values")
    check(exact_tree(diagnostics["c_values"], [-1, 0, 1]), "diagnostic c values")
    check(exact_tree(diagnostics["orders"], [1, 2, 3, 4]), "diagnostic orders")
    check_int(diagnostics["row_count"], 60, "diagnostic row count")
    check(type(diagnostics["rows"]) is list and len(diagnostics["rows"]) == 60, "diagnostic rows")
    cursor = 0
    for n in (50, 100, 200, 400, 800):
        K = choose(n, 2)
        for c in (-1, 0, 1):
            m = math.floor(0.5 * n * (math.log(n) + c))
            for r in range(1, 5):
                row = diagnostics["rows"][cursor]
                cursor += 1
                check(type(row) is dict and set(row) == DIAG_KEYS, "diagnostic row keys")
                check_int(row["n"], n, "diagnostic n")
                check_int(row["c"], c, "diagnostic c")
                check_int(row["m"], m, "diagnostic m")
                check_int(row["r"], r, "diagnostic r")
                check(type(row["within_edge_range"]) is bool and row["within_edge_range"] is True and m <= K, "diagnostic range")
                actual = isolated_factorial(n, m, r)
                target = math.exp(-r * c)
                observed = parse_decimal(row["factorial_moment_decimal_12"])
                wanted = parse_decimal(row["poisson_target_decimal_12"])
                error = parse_decimal(row["absolute_error_decimal_12"])
                check(abs(observed - actual) <= 5.1e-13, "factorial diagnostic")
                check(abs(wanted - target) <= 5.1e-13, "target diagnostic")
                check(abs(error - abs(actual - target)) <= 5.1e-13, "error diagnostic")

    summary = data["regression_summary"]
    expected_summary = {"finite_n_max": 12, "finite_rows": 12, "coefficient_cells": coefficient_cells,
                        "moment_cells": 48, "exhaustive_n_max": 6,
                        "exhaustive_graph_masks": sum(2 ** choose(n, 2) for n in range(1, 7)),
                        "isolated_diagnostic_rows": 60}
    check(exact_tree(summary, expected_summary), "summary exact tree")
    if exhaustive:
        check_int(exhaustive_masks, expected_summary["exhaustive_graph_masks"], "exhaustive accounting")


EVAL_KEYS = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
             "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
             "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
             "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
             "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
             "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
             "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}


def check_evaluation(value: dict) -> None:
    check(set(value) == EVAL_KEYS, "evaluation exact keys")
    check(value["schema"] == "route-a-evaluation-v0.2.0", "evaluation schema")
    check(value["candidate_id"] == "HCS-C307" and value["obstruction_id"] == "HEN-O291", "evaluation ids")
    check(value["title"] == "Connectivity hitting in the random graph process: exact finite laws and the Gumbel window", "evaluation title")
    check(value["evaluation_date"] == "2026-09-03" and value["source_commit"] == SOURCE, "evaluation provenance")
    check_int(value["fixed_epoch"], EPOCH, "evaluation epoch")
    check(value["scope_literal"] == SCOPE and value["evaluator_authority_sha256"] == EVALUATOR, "evaluation authority")
    check(value["evaluator_authority"] == "route-a-evaluator" and value["evaluator_version"] == "0.2.0", "evaluation version")
    check(exact_tree(value["artifact_paths"], ["results/c307_connectivity_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]), "artifacts")
    for index, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        lane = value[key]
        check(type(lane) is dict and set(lane) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"}, key + " keys")
        check(lane["verdict"] == f"A{index}_FAIL", key + " verdict")
        check(type(lane["artifacts"]) is list and len(lane["artifacts"]) >= 1 and all(type(x) is str for x in lane["artifacts"]), key + " artifacts")
        check(all(type(lane[x]) is str and lane[x] for x in ("evidence_status", "strongest_evidence", "strongest_failure")), key + " prose")
    check(exact_tree(value["tuple"], TUPLE), "evaluation tuple")
    check(value["overall_verdict"] == "ROUTE_A_REJECTED", "evaluation verdict")
    check(type(value["route_b_invocation_allowed"]) is bool and value["route_b_invocation_allowed"] is False, "evaluation Route B")
    check(exact_tree(value["scope_flags"], FLAGS), "evaluation flags")
    check(value["theorem_status"] == "PROVABLE_AS_STATED", "theorem status")
    check(exact_tree(value["source_owner_tokens"], SOURCES), "evaluation sources")
    complex_keys = {"fixed_epoch", "route_b_invocation_allowed", "scope_flags", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "source_owner_tokens"}
    for key in EVAL_KEYS - complex_keys:
        check(type(value[key]) is str and bool(value[key]), "evaluation scalar " + key)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--yaml", type=Path, default=DEFAULT_YAML)
    parser.add_argument("--skip-exhaustive", action="store_true")
    args = parser.parse_args()
    evidence = strict_json(args.evidence)
    evaluation = strict_yaml(args.yaml)
    check_evidence(evidence, not args.skip_exhaustive)
    check_evaluation(evaluation)
    print(f"C307 independent checker PASS ({Count.value} explicit checks; producer import forbidden)")
    print(f"finite_rows=12 coefficient_cells=298 exhaustive_masks={0 if args.skip_exhaustive else 33867}")


if __name__ == "__main__":
    main()
