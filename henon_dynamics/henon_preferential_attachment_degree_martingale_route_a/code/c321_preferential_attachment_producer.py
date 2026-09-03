#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C321."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c321_preferential_attachment_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C321/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
NMAX = 9
EVALUATION_RAW = "a8f62dc0ddb1546c7a5174b59e7ecffce201530d3a462e72ecf0ff3644dc9ec5"
EVALUATION_SEMANTIC = "cc1b0fbf9fdc348a592adecbe6682ea789dd1706275ab39916a3fa8731408014"

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


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    text = path.read_text()
    for token in yaml.scan(text):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(text, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root must be a mapping")
    return value


def fs(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def rising(x: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= x + j
    return out


def expected_rising(n: int, s: int, r: int) -> Fraction:
    out = Fraction(math.factorial(r))
    for t in range(s, n):
        out *= Fraction(2 * (t - 1) + r, 2 * (t - 1))
    return out


def step(states: dict[tuple[int, ...], Fraction]) -> dict[tuple[int, ...], Fraction]:
    result: dict[tuple[int, ...], Fraction] = {}
    for degrees, mass in states.items():
        n = len(degrees)
        assert sum(degrees) == 2 * (n - 1)
        for vertex, degree in enumerate(degrees):
            nxt = list(degrees)
            nxt[vertex] += 1
            nxt.append(1)
            key = tuple(nxt)
            result[key] = result.get(key, Fraction(0)) + mass * Fraction(degree, 2 * (n - 1))
    assert sum(result.values(), Fraction(0)) == 1
    return result


def count_degree(degrees: tuple[int, ...], k: int) -> int:
    return sum(value == k for value in degrees)


def time_row(n: int, states: dict[tuple[int, ...], Fraction]) -> dict:
    fixed = []
    for i in range(1, n + 1):
        s = 2 if i <= 2 else i
        for r in range(1, 9):
            observed = sum((mass * rising(degrees[i - 1], r)
                            for degrees, mass in states.items()), Fraction(0))
            predicted = expected_rising(n, s, r)
            assert observed == predicted
            fixed.append({"vertex": i, "birth_time": s, "order": r,
                          "observed": fs(observed), "formula": fs(predicted)})
    populations = []
    drift_cells = 0
    for k in range(1, n):
        mean = sum((mass * count_degree(degrees, k)
                    for degrees, mass in states.items()), Fraction(0))
        second = sum((mass * count_degree(degrees, k) ** 2
                      for degrees, mass in states.items()), Fraction(0))
        for degrees in states:
            nk = count_degree(degrees, k)
            nkm1 = count_degree(degrees, k - 1) if k > 1 else 0
            drift = Fraction(int(k == 1)) + Fraction((k - 1) * nkm1 - k * nk, 2 * (n - 1))
            direct = Fraction(0)
            for vertex, degree in enumerate(degrees):
                before = nk
                after = nk + int(k == 1) + int(degree == k - 1) - int(degree == k)
                direct += Fraction(degree, 2 * (n - 1)) * (after - before)
            assert direct == drift
            drift_cells += 1
        populations.append({"degree": k, "mean": fs(mean), "second_moment": fs(second),
                            "variance": fs(second - mean * mean)})
    return {
        "n": n,
        "state_count": len(states),
        "labeled_parent_history_count": math.factorial(n - 1),
        "total_mass": fs(sum(states.values(), Fraction(0))),
        "vertex_count_identity": n,
        "degree_sum_identity": 2 * (n - 1),
        "conditional_drift_cells_checked": drift_cells,
        "fixed_vertex_moments": fixed,
        "degree_population_moments": populations,
    }


def profile_rows() -> list[dict]:
    rows = []
    previous = Fraction(0)
    cumulative = Fraction(0)
    weighted = Fraction(0)
    for k in range(1, 13):
        p = Fraction(4, k * (k + 1) * (k + 2))
        recurrence_rhs = Fraction(int(k == 1)) + (k - 1) * previous / 2 - k * p / 2
        cumulative += p
        weighted += k * p
        assert p == recurrence_rhs
        assert cumulative == 1 - Fraction(2, (k + 1) * (k + 2))
        assert weighted == 2 - Fraction(4, k + 2)
        rows.append({"degree": k, "p_k": fs(p), "recurrence_rhs": fs(recurrence_rhs),
                     "partial_mass": fs(cumulative), "partial_mean_degree": fs(weighted)})
        previous = p
    return rows


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(v) for v in value.values())
    if type(value) is list:
        return sum(leaf_count(v) for v in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C321 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    evaluation = strict_yaml(EVALUATION)
    semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False).encode()).hexdigest()
    if hashlib.sha256(EVALUATION.read_bytes()).hexdigest() != EVALUATION_RAW or semantic != EVALUATION_SEMANTIC:
        raise AssertionError("frozen evaluation changed")
    states = {(1, 1): Fraction(1)}
    times = []
    for n in range(2, NMAX + 1):
        times.append(time_row(n, states))
        if n < NMAX:
            states = step(states)
    terminal = [{"degrees": list(degrees), "probability": fs(mass)}
                for degrees, mass in sorted(states.items())]
    data = {
        "schema": "hcs-c321-preferential-attachment-v1",
        "candidate_id": "HCS-C321",
        "obstruction_id": "HEN-O305",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "initial_tree": "T_2 is the single edge {1,2}",
            "self_loops": False,
            "multiple_edges": False,
            "update": "vertex n+1 attaches to old v with probability d_v(n)/(2(n-1))",
            "clock": "n equals the number of vertices",
            "fixed_observable": "D_i(n) is the degree of one fixed labeled vertex",
            "population_observable": "N_k(n) counts all degree-k vertices",
        },
        "theorem_contract": {
            "fixed_moments": "all integer rising-factorial orders with the s_i birth-time split",
            "fixed_limit": "D_i(n)/sqrt(n) converges almost surely and in every finite Lp",
            "limit_moments": "r! Gamma(s_i-1)/Gamma(s_i-1+r/2), moment determinate by Carleman",
            "population_limit": "for fixed k, N_k(n)/n converges in L2 to 4/[k(k+1)(k+2)]",
            "excluded": "no maximum-degree, joint-hub, m>1, self-loop, or uniform-in-k theorem",
            "evidence_boundary": "finite exact enumeration is regression evidence only",
        },
        "finite_grid": {"n_min": 2, "n_max": NMAX, "rising_order_max": 8,
                        "terminal_parent_histories": math.factorial(NMAX - 1)},
        "time_rows": times,
        "terminal_degree_vector_distribution": terminal,
        "profile_rows": profile_rows(),
        "route_a_yaml": {
            "relative_path": str(EVALUATION.relative_to(ROOT)),
            "raw_sha256": hashlib.sha256(EVALUATION.read_bytes()).hexdigest(),
            "semantic_sha256": semantic,
        },
        "collision_boundary": {
            "C263": "a fixed-color Polya urn is exchangeable; attachment evolves a labeled tree and a degree population",
            "C276": "a uniform random mapping is sampled at fixed size; preferential attachment is sequential reinforced growth",
            "C307": "Erdos--Renyi connectivity uses independent edges; preferential attachment uses degree-biased dependent edges",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No finite computation is presented as an asymptotic proof.",
            "No theorem about maximum degree or a joint hub law is asserted.",
            "No result for a self-loop seed, the LCD convention, or m greater than one is asserted.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
            "No literature-priority claim is made.",
        ],
        "references": [
            {"identifier": "10.1126/science.286.5439.509", "role": "historical preferential-attachment model"},
            {"identifier": "10.1002/rsa.1009", "role": "rigorous degree-sequence lineage with a distinct convention"},
            {"identifier": "10.1214/ECP.v16-1598", "role": "fixed-vertex degree-limit lineage with convention audit"},
        ],
    }
    data["audited_leaf_count"] = leaf_count(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C321_PRODUCER_PASS {data['payload_sha256']} {data['audited_leaf_count']}")


if __name__ == "__main__":
    main()
