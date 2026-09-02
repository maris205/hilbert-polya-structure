#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C291.

The core oracle directly enumerates every edge order through the greedy
matched-vertex bitmask.  No producer module or producer recurrence is imported.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C291_EVIDENCE", ROOT / "results/c291_dimer_rsa_evidence.json"))
YAML_PATH = Path(os.environ.get("C291_YAML", ROOT / "evaluations/route_a/HCS-C291/2026-09-02.yaml"))
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
checks = 0

TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "headline", "model_contract", "theorem_contract",
    "proof_contract", "enumeration_contract", "path_rows", "cycle_rows",
    "factorial_moment_rows", "asymptotic_rows", "boundary_rows", "references",
    "collision_snapshot", "nonclaims", "route_a", "scope_flags", "payload_sha256",
}
MODEL_KEYS = {"path", "cycle", "sampling", "acceptance_rule", "output_semantics", "clock"}
THEOREM_KEYS = {
    "path_pgf", "riccati_ogf", "factorial_moments", "exact_mean", "variance",
    "path_support", "cycle_identity", "cycle_support", "cycle_mean_boundary", "occupancy",
}
PROOF_KEYS = {"status", "dependencies", "finite_evidence_boundary", "ownership_boundary"}
ENUM_KEYS = {"path_min_n", "path_max_n", "cycle_min_n", "cycle_max_n", "factorial_max_n", "factorial_max_order", "asymptotic_n"}
PATH_KEYS = {"n", "edge_count", "order_count", "distribution", "support_min", "support_max", "mean", "factorial_second", "variance", "closed_mean"}
CYCLE_KEYS = {"n", "edge_count", "order_count", "distribution", "support_min", "support_max", "mean", "factorial_second", "variance", "path_identity_index"}
DIST_KEYS = {"matching_size", "order_count", "probability"}
FM_KEYS = {"n", "moments"}
ASYM_KEYS = {"n", "mean", "variance", "mean_density", "variance_density", "variance_centered"}
BOUNDARY_KEYS = {"face", "condition", "status"}
REFERENCE_KEYS = {"authors", "title", "venue", "identifier", "role"}
COLLISION_KEYS = {"token", "registry_bytes_required", "closest", "direct_owner_risk", "obstruction_id"}
CLOSEST_KEYS = {"candidate", "distinction"}
ROUTE_KEYS = {"tuple", "overall", "route_b_invocation_allowed"}
FLAG_KEYS = {"arithmetic_local_data", "euler_factors", "root_numbers", "automorphy", "target_divisor_or_counting_law", "target_functional_equation", "target_zero_match", "hilbert_polya_operator", "route_b_authorization"}
YAML_TOP_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "candidate_definition", "family", "phase_space",
    "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock",
    "normalization", "determinant_convention", "orbit_cutoff", "precision",
    "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3",
    "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "scope_flags",
    "obstruction_id",
}
YAML_GATE_KEYS = {"verdict", "evidence_status", "strongest_failure"}

EXPECTED_MODEL = {
    "path": "P_n has vertices 1,...,n and edges {i,i+1}; n>=0",
    "cycle": "C_n is the simple labeled cycle; n>=3",
    "sampling": "a uniformly random permutation of all labeled edges, equivalently iid continuous priorities",
    "acceptance_rule": "scan once and accept an edge exactly when both endpoints are currently unmatched",
    "output_semantics": "the terminal set is a jammed maximal matching, not generally a maximum matching",
    "clock": "one finite edge-order scan; there is no physical-time periodic flow",
}
EXPECTED_THEOREM = {
    "path_pgf": "F_0=F_1=1 and (n-1)F_n(z)=z*sum_{a+b=n-2}F_a(z)F_b(z) for n>=2",
    "riccati_ogf": "F_x=(F-1)/x+z*x*F^2, F(0,z)=1, [x]F=1",
    "factorial_moments": "H_r=partial_z^r F|_{z=1} obeys the displayed all-r triangular linear ODE with H_0=(1-x)^(-1)",
    "exact_mean": "E[M_n]=sum_{j=1}^{n-1}(n-j)(-1)^(j+1)2^(j-1)/j!",
    "variance": "Var(M_n)=exp(-4)*n+2*exp(-4)+o(1), hence exp(-4)*n+O(1)",
    "path_support": "{0} for n=0,1; every integer ceil((n-1)/3),...,floor(n/2) for n>=2",
    "cycle_identity": "G_n(z)=z*F_{n-2}(z) for every simple cycle n>=3",
    "cycle_support": "every integer ceil(n/3),...,floor(n/2) for n>=3",
    "cycle_mean_boundary": "E[C_n]=1+E[M_{n-2}]=((1-exp(-2))/2)n+o(1), and E[C_n]-E[M_n] tends to exp(-2)",
    "occupancy": "2E[M_n]/n and 2E[C_n]/n tend to 1-exp(-2)",
}
EXPECTED_PROOF = {
    "status": "PROVABLE AS STATED",
    "dependencies": [
        "condition on the unique first edge in the continuous-priority order",
        "independence and uniform relative orders on the two residual path components",
        "differentiate the Riccati OGF at z=1 for the all-order factorial hierarchy",
        "solve the first two linear ODEs and extract the pole parts at x=1",
        "use maximal-matching domination bounds plus explicit path and cycle constructions",
    ],
    "finite_evidence_boundary": "edge-order enumeration is a regression oracle only and is not an all-n proof",
    "ownership_boundary": "the RSA model and one-dimensional jamming law are classical; this package is a reproducible reconstruction, not a literature-priority claim",
}
EXPECTED_BOUNDARIES = [
    {"face": "empty_path", "condition": "n=0", "status": "no vertices, no edges, M_0=0 and F_0=1"},
    {"face": "singleton_path", "condition": "n=1", "status": "one vertex, no edges, M_1=0 and F_1=1"},
    {"face": "first_nontrivial_path", "condition": "n=2", "status": "one edge is accepted with certainty, so F_2=z"},
    {"face": "cycle_domain", "condition": "n>=3", "status": "only simple cycles are covered; loops and parallel edges are excluded"},
    {"face": "priority_ties", "condition": "iid continuous priorities", "status": "ties have probability zero; discrete priorities require an extra tie-breaking rule"},
    {"face": "jamming_semantics", "condition": "all edges scanned", "status": "the result is maximal under edge addition but need not have maximum cardinality"},
    {"face": "path_lower_support", "condition": "n>=2", "status": "maximality forces at least ceil((n-1)/3) dimers and constructions attain every size through floor(n/2)"},
    {"face": "cycle_lower_support", "condition": "n>=3", "status": "maximality forces at least ceil(n/3) dimers and first-edge reduction transfers all attainable sizes"},
    {"face": "finite_oracle", "condition": "enumerated n only", "status": "finite order tables test implementations and do not prove any all-n identity"},
]
EXPECTED_REFS = [
    ("10.1021/ja01875a053", "Paul J. Flory"),
    ("10.1103/RevModPhys.65.1281", "J. W. Evans"),
    ("10.1007/s002200100387", "Mathew D. Penrose"),
    ("10.1002/rsa.3240020104", "Martin Dyer and Alan Frieze"),
]
EXPECTED_NONCLAIMS = [
    "A jammed matching is called maximal, never maximum unless its cardinality happens to attain floor(n/2).",
    "Finite edge-order enumeration is not used as proof of the all-n recurrence, support, or asymptotics.",
    "No literature originality or priority is claimed for dimer RSA, random greedy matching, or the Flory jamming constant.",
    "No rational-prime carrier, prime-power repetition law, logarithmic prime clock, target divisor, or target functional equation is obtained.",
    "No source-native self-adjoint Hilbert-Polya operator or Route-B authorization is claimed.",
]
EXPECTED_CLOSEST = [
    {"candidate": "HCS-C208", "distinction": "continuous-time linear birth-death branching PGFs, not greedy adsorption on finite graphs"},
    {"candidate": "HCS-C243", "distinction": "Bose-Josephson Hamiltonian dimer, not an adsorbing graph matching"},
    {"candidate": "HCS-C285", "distinction": "closed queueing-network product form and condensation, not a random edge-order jamming law"},
]
EXPECTED_YAML_SCALARS = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C291",
    "title": "finite path and cycle dimer random sequential adsorption",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "scope_literal": SCOPE,
    "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "candidate_definition": "uniform labeled-edge order scanned greedily on P_n or simple C_n",
    "family": "stochastic combinatorial dynamics / dimer RSA / random greedy matching",
    "phase_space": "finite matched-vertex bitmasks together with remaining ordered edges",
    "dynamics": "accept an edge iff both endpoints are unmatched, then continue the one-pass scan",
    "parameters": "path n>=0; simple cycle n>=3",
    "parameter_provenance": "finite graph and uniform edge-order law fixed before evidence",
    "arithmetic_origin": "none",
    "clock": "one finite edge-order scan",
    "normalization": "F_n(z)=E[z^M_n] and G_n(z)=E[z^K_n]",
    "determinant_convention": "no dynamical or target determinant is defined",
    "orbit_cutoff": "not applicable; this is not a periodic-orbit census",
    "precision": "exact Fraction arithmetic plus 90-digit Decimal asymptotic controls",
    "training_data": "none",
    "forbidden_data": "Riemann zeros, prime labels, target Euler factors, root numbers",
    "overall_verdict": "ROUTE_A_REJECTED",
    "obstruction_id": "HEN-O275",
}
EXPECTED_YAML_GATES = {
    "a0": {
        "verdict": "A0_FAIL",
        "evidence_status": "PROVED",
        "strongest_failure": "graph edges and sizes have no rational-prime carrier or arithmetic weight",
    },
    "a1": {
        "verdict": "A1_FAIL",
        "evidence_status": "PROVED",
        "strongest_failure": "a terminating random scan has no isolated deterministic primitive-periodic ledger or repetition law",
    },
    "a2": {
        "verdict": "A2_FAIL",
        "evidence_status": "PROVED",
        "strongest_failure": "the probability generating functions are stochastic source data, not a target determinant",
    },
    "a3": {
        "verdict": "A3_FAIL",
        "evidence_status": "PROVED",
        "strongest_failure": "no target divisor, functional equation, explicit-formula bridge, or zero match exists",
    },
    "a4": {
        "verdict": "A4_FAIL",
        "evidence_status": "PROVED",
        "strongest_failure": "no source-native same-clock self-adjoint quantization is defined",
    },
}
EXPECTED_YAML_ARTIFACTS = [
    "THEOREM_PACKAGE.md",
    "results/c291_dimer_rsa_evidence.json",
    "paper/main.pdf",
]
EXPECTED_YAML_TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
YAML_SEMANTIC_SHA = "53928a4f4a14928d254ae0a5093d3dfbc622a2d0d7811d7bce517b36771cc1f6"


def claim(value: bool) -> None:
    global checks
    assert value
    checks += 1


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if type(key) is not str or key in result:
            raise ValueError(f"duplicate or non-string JSON key: {key!r}")
        result[key] = value
    return result


def reject_constant(token: str) -> None:
    raise ValueError(f"nonstandard JSON constant: {token}")


def load_strict(path: Path) -> dict:
    data = json.loads(path.read_text(), object_pairs_hook=unique_object, parse_constant=reject_constant)
    if type(data) is not dict:
        raise ValueError("top-level JSON must be an object")
    return data


def exact_keys(value: object, keys: set[str]) -> None:
    claim(type(value) is dict)
    claim(set(value) == keys)  # type: ignore[arg-type]


def exact_int(value: object) -> None:
    claim(type(value) is int)


def exact_str(value: object) -> None:
    claim(type(value) is str)


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe recursive loader which rejects duplicate mapping keys."""


def construct_unique_mapping(
    loader: UniqueYAMLLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError(f"duplicate or non-string YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def validate_route_yaml(path: Path) -> None:
    value = yaml.load(path.read_text(), Loader=UniqueYAMLLoader)
    exact_keys(value, YAML_TOP_KEYS)
    for key, expected in EXPECTED_YAML_SCALARS.items():
        exact_str(value[key])
        claim(value[key] == expected)
    exact_int(value["fixed_epoch"])
    claim(value["fixed_epoch"] == EPOCH)
    claim(type(value["route_b_invocation_allowed"]) is bool)
    claim(value["route_b_invocation_allowed"] is False)
    claim(type(value["artifact_paths"]) is list)
    claim(all(type(item) is str for item in value["artifact_paths"]))
    claim(value["artifact_paths"] == EXPECTED_YAML_ARTIFACTS)
    claim(type(value["tuple"]) is list)
    claim(all(type(item) is str for item in value["tuple"]))
    claim(value["tuple"] == EXPECTED_YAML_TUPLE)
    for gate, expected in EXPECTED_YAML_GATES.items():
        exact_keys(value[gate], YAML_GATE_KEYS)
        claim(all(type(item) is str for item in value[gate].values()))
        claim(value[gate] == expected)
    exact_keys(value["scope_flags"], FLAG_KEYS)
    claim(all(type(item) is bool and item is False for item in value["scope_flags"].values()))
    semantic = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    claim(hashlib.sha256(semantic.encode()).hexdigest() == YAML_SEMANTIC_SHA)


def parse_q(value: object) -> Fraction:
    exact_str(value)
    parts = value.split("/")  # type: ignore[union-attr]
    claim(len(parts) == 2)
    claim(parts[0] == "0" or not parts[0].startswith("0"))
    claim(not parts[1].startswith("0"))
    answer = Fraction(int(parts[0]), int(parts[1]))
    claim(str(answer.numerator) == parts[0])
    claim(str(answer.denominator) == parts[1])
    return answer


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


ORDER_CACHE: dict[tuple[int, tuple[tuple[int, int], ...]], Counter] = {}


def exhaustive(vertices: int, edges: list[tuple[int, int]]) -> Counter:
    """Count every labeled edge order by subset/vertex-bitmask dynamic enumeration.

    A state weight is the number of order prefixes producing that exact
    processed-edge and matched-vertex mask.  Extending by every unprocessed
    edge enumerates all permutations without using the first-edge convolution.
    """
    cache_key = (vertices, tuple(edges))
    if cache_key in ORDER_CACHE:
        return Counter(ORDER_CACHE[cache_key])
    edge_count = len(edges)
    states = {(0, 0): 1}
    for depth in range(edge_count):
        next_states: dict[tuple[int, int], int] = {}
        for (processed, matched), weight in states.items():
            claim(processed.bit_count() == depth)
            claim(matched >> vertices == 0)
            claim(matched.bit_count() % 2 == 0)
            for index, (u, v) in enumerate(edges):
                if processed & (1 << index):
                    continue
                bits = (1 << u) | (1 << v)
                new_matched = matched if matched & bits else matched | bits
                key = (processed | (1 << index), new_matched)
                next_states[key] = next_states.get(key, 0) + weight
        states = next_states
    counts = Counter()
    for (processed, matched), weight in states.items():
        claim(processed == (1 << edge_count) - 1)
        claim(matched.bit_count() % 2 == 0)
        counts[matched.bit_count() // 2] += weight
    if not edges:
        counts[0] = 1
    claim(sum(counts.values()) == math.factorial(edge_count))
    ORDER_CACHE[cache_key] = Counter(counts)
    return counts


def moment_from_counts(counts: Counter, order: int) -> Fraction:
    denominator = sum(counts.values())
    numerator = 0
    for k, count in counts.items():
        falling = 1
        for j in range(order):
            falling *= k - j
        numerator += count * falling
    return Fraction(numerator, denominator)


def closed_mean(n: int) -> Fraction:
    if n < 2:
        return Fraction(0)
    return sum(Fraction((n-j)*((-1)**(j+1))*2**(j-1), math.factorial(j)) for j in range(1, n))


def recurrence_moments(limit: int) -> tuple[list[Fraction], list[Fraction]]:
    means = [Fraction(0)] * (limit + 1)
    seconds = [Fraction(0)] * (limit + 1)
    for n in range(2, limit + 1):
        means[n] = sum(1 + means[a] + means[n-2-a] for a in range(n-1)) / (n-1)
        seconds[n] = sum(
            seconds[a] + seconds[n-2-a]
            + 2*means[a]*means[n-2-a] + 2*means[a] + 2*means[n-2-a]
            for a in range(n-1)
        ) / (n-1)
    return means, seconds


def check_distribution(row: dict, counts: Counter) -> None:
    items = row["distribution"]
    claim(type(items) is list)
    claim(len(items) == len(counts))
    prior = -1
    total_probability = Fraction(0)
    total_count = 0
    for item, (size, count) in zip(items, sorted(counts.items())):
        exact_keys(item, DIST_KEYS)
        exact_int(item["matching_size"])
        exact_int(item["order_count"])
        claim(item["matching_size"] == size)
        claim(item["matching_size"] > prior)
        prior = item["matching_size"]
        claim(item["order_count"] == count)
        probability = parse_q(item["probability"])
        claim(probability == Fraction(count, row["order_count"]))
        claim(probability > 0)
        total_probability += probability
        total_count += count
    claim(total_probability == 1)
    claim(total_count == row["order_count"])
    claim(row["support_min"] == min(counts))
    claim(row["support_max"] == max(counts))


def main() -> None:
    data = load_strict(EVIDENCE)
    exact_keys(data, TOP_KEYS)
    claim(data["schema"] == "hcs-c291-dimer-rsa-path-cycle-v1")
    claim(data["candidate_id"] == "HCS-C291")
    claim(data["evaluation_date"] == "2026-09-02")
    claim(data["source_commit"] == SOURCE)
    exact_int(data["fixed_epoch"])
    claim(data["fixed_epoch"] == EPOCH)
    claim(data["scope_literal"] == SCOPE)
    exact_keys(data["evaluator"], {"version", "sha256"})
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR})
    exact_str(data["headline"])
    claim("factorial-moment triangle" in data["headline"])
    claim(data["payload_sha256"] == payload_hash(data))

    exact_keys(data["model_contract"], MODEL_KEYS)
    claim(data["model_contract"] == EXPECTED_MODEL)
    exact_keys(data["theorem_contract"], THEOREM_KEYS)
    claim(data["theorem_contract"] == EXPECTED_THEOREM)
    exact_keys(data["proof_contract"], PROOF_KEYS)
    claim(data["proof_contract"] == EXPECTED_PROOF)
    exact_keys(data["enumeration_contract"], ENUM_KEYS)
    enum = data["enumeration_contract"]
    for key in ENUM_KEYS - {"asymptotic_n"}:
        exact_int(enum[key])
    claim(type(enum["asymptotic_n"]) is list)
    claim(all(type(n) is int for n in enum["asymptotic_n"]))
    claim(enum == {"path_min_n": 0, "path_max_n": 10, "cycle_min_n": 3, "cycle_max_n": 9, "factorial_max_n": 20, "factorial_max_order": 5, "asymptotic_n": [20, 50, 100, 200]})

    path_rows = data["path_rows"]
    claim(type(path_rows) is list)
    claim(len(path_rows) == 11)
    path_moments = {}
    for expected_n, row in enumerate(path_rows):
        exact_keys(row, PATH_KEYS)
        for key in ("n", "edge_count", "order_count", "support_min", "support_max"):
            exact_int(row[key])
        claim(row["n"] == expected_n)
        claim(row["edge_count"] == max(0, expected_n - 1))
        claim(row["order_count"] == math.factorial(row["edge_count"]))
        edges = [(i, i + 1) for i in range(expected_n - 1)]
        counts = exhaustive(expected_n, edges)
        check_distribution(row, counts)
        mean = moment_from_counts(counts, 1)
        second = moment_from_counts(counts, 2)
        variance = second + mean - mean * mean
        claim(parse_q(row["mean"]) == mean)
        claim(parse_q(row["factorial_second"]) == second)
        claim(parse_q(row["variance"]) == variance)
        claim(parse_q(row["closed_mean"]) == closed_mean(expected_n))
        if expected_n < 2:
            claim(list(counts) == [0])
        else:
            claim(min(counts) == (expected_n + 1) // 3)
            claim(max(counts) == expected_n // 2)
            claim(sorted(counts) == list(range(min(counts), max(counts) + 1)))
        path_moments[expected_n] = (mean, second, variance, counts)

    cycle_rows = data["cycle_rows"]
    claim(type(cycle_rows) is list)
    claim(len(cycle_rows) == 7)
    for expected_n, row in zip(range(3, 10), cycle_rows):
        exact_keys(row, CYCLE_KEYS)
        for key in ("n", "edge_count", "order_count", "support_min", "support_max", "path_identity_index"):
            exact_int(row[key])
        claim(row["n"] == expected_n)
        claim(row["edge_count"] == expected_n)
        claim(row["order_count"] == math.factorial(expected_n))
        claim(row["path_identity_index"] == expected_n - 2)
        edges = [(i, (i + 1) % expected_n) for i in range(expected_n)]
        counts = exhaustive(expected_n, edges)
        check_distribution(row, counts)
        mean = moment_from_counts(counts, 1)
        second = moment_from_counts(counts, 2)
        variance = second + mean - mean * mean
        claim(parse_q(row["mean"]) == mean)
        claim(parse_q(row["factorial_second"]) == second)
        claim(parse_q(row["variance"]) == variance)
        claim(min(counts) == (expected_n + 2) // 3)
        claim(max(counts) == expected_n // 2)
        claim(sorted(counts) == list(range(min(counts), max(counts) + 1)))
        path_counts = path_moments[expected_n - 2][3]
        path_total = sum(path_counts.values())
        cycle_total = sum(counts.values())
        claim(all(Fraction(counts[k], cycle_total) == Fraction(path_counts[k-1], path_total) for k in counts))
        claim(mean == 1 + path_moments[expected_n - 2][0])
        claim(variance == path_moments[expected_n - 2][2])

    means, seconds = recurrence_moments(200)
    for n in range(201):
        claim(means[n] == closed_mean(n))
    fm_rows = data["factorial_moment_rows"]
    claim(type(fm_rows) is list)
    claim(len(fm_rows) == 21)
    triangle: list[list[Fraction]] = []
    for expected_n, row in enumerate(fm_rows):
        exact_keys(row, FM_KEYS)
        exact_int(row["n"])
        claim(row["n"] == expected_n)
        claim(type(row["moments"]) is list)
        claim(len(row["moments"]) == 6)
        counts = exhaustive(expected_n, [(i, i+1) for i in range(expected_n-1)]) if expected_n <= 10 else None
        parsed = [parse_q(value) for value in row["moments"]]
        claim(parsed[0] == 1)
        claim(parsed[1] == means[expected_n])
        claim(parsed[2] == seconds[expected_n])
        if expected_n < 2:
            expected_triangle = [Fraction(1)] + [Fraction(0)] * 5
        else:
            expected_triangle = [Fraction(1)]
            for order in range(1, 6):
                total = Fraction(0)
                for left in range(expected_n - 1):
                    right = expected_n - 2 - left
                    total += sum(
                        Fraction(math.comb(order, split))
                        * triangle[left][split]
                        * triangle[right][order - split]
                        for split in range(order + 1)
                    )
                    total += order * sum(
                        Fraction(math.comb(order - 1, split))
                        * triangle[left][split]
                        * triangle[right][order - 1 - split]
                        for split in range(order)
                    )
                expected_triangle.append(total / (expected_n - 1))
        claim(parsed == expected_triangle)
        triangle.append(parsed)
        if counts is not None:
            for order in range(6):
                claim(parsed[order] == moment_from_counts(counts, order))

    asym = data["asymptotic_rows"]
    claim(type(asym) is list)
    claim(len(asym) == 4)
    getcontext().prec = 90
    e4 = Decimal(-4).exp()
    for expected_n, row in zip((20, 50, 100, 200), asym):
        exact_keys(row, ASYM_KEYS)
        exact_int(row["n"])
        claim(row["n"] == expected_n)
        mean = means[expected_n]
        variance = seconds[expected_n] + mean - mean * mean
        claim(parse_q(row["mean"]) == mean)
        claim(parse_q(row["variance"]) == variance)
        md = Decimal(mean.numerator) / Decimal(mean.denominator)
        vd = Decimal(variance.numerator) / Decimal(variance.denominator)
        claim(row["mean_density"] == format(md / Decimal(expected_n), ".36E"))
        claim(row["variance_density"] == format(vd / Decimal(expected_n), ".36E"))
        claim(row["variance_centered"] == format(vd - e4 * Decimal(expected_n + 2), ".36E"))
    claim(abs(Decimal(asym[-1]["variance_density"]) - e4) < Decimal("0.001"))
    claim(abs(Decimal(asym[-1]["variance_centered"])) < Decimal("1e-60"))

    boundaries = data["boundary_rows"]
    claim(type(boundaries) is list)
    claim(len(boundaries) == len(EXPECTED_BOUNDARIES))
    claim(boundaries == EXPECTED_BOUNDARIES)
    for row in boundaries:
        exact_keys(row, BOUNDARY_KEYS)
        for value in row.values():
            exact_str(value)

    refs = data["references"]
    claim(type(refs) is list)
    claim(len(refs) == 4)
    for row, (doi, authors) in zip(refs, EXPECTED_REFS):
        exact_keys(row, REFERENCE_KEYS)
        for value in row.values():
            exact_str(value)
        claim(row["identifier"] == doi)
        claim(row["authors"] == authors)
    claim(len({row["identifier"] for row in refs}) == len(refs))

    collision = data["collision_snapshot"]
    exact_keys(collision, COLLISION_KEYS)
    claim(collision["token"] == "C291_READ_ONLY_COLLISION_SNAPSHOT_AT_7fbe9db3")
    claim(type(collision["registry_bytes_required"]) is bool)
    claim(collision["registry_bytes_required"] is False)
    claim(collision["obstruction_id"] == "HEN-O275")
    claim(type(collision["closest"]) is list)
    claim(len(collision["closest"]) == 3)
    claim(collision["closest"] == EXPECTED_CLOSEST)
    for row in collision["closest"]:
        exact_keys(row, CLOSEST_KEYS)
        exact_str(row["candidate"])
        exact_str(row["distinction"])
    exact_str(collision["direct_owner_risk"])

    claim(data["nonclaims"] == EXPECTED_NONCLAIMS)
    claim(type(data["nonclaims"]) is list)
    claim(all(type(value) is str for value in data["nonclaims"]))
    exact_keys(data["route_a"], ROUTE_KEYS)
    claim(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    claim(type(data["route_a"]["route_b_invocation_allowed"]) is bool)
    exact_keys(data["scope_flags"], FLAG_KEYS)
    claim(all(type(value) is bool and value is False for value in data["scope_flags"].values()))
    validate_route_yaml(YAML_PATH)

    print(f"C291 independent bitmask/order checker: PASS ({checks} assertions; strict duplicate-rejecting JSON/YAML schema)")


if __name__ == "__main__":
    main()
