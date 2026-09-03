#!/usr/bin/env python3
"""Canonical exact finite-evidence producer for HCS-C353."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c353_ewens_crp_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C353/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "1222ce92be15cc96a7f3cf867e7b14d9e302dd8681eace54fc65a70f17f30ce3"
YAML_SEMANTIC = "a25cba8c895eed584d2563bb10d0f6f1e3453a4708c616b223bb264b6005375e"
THETA_PANEL = tuple(map(Fraction, ("1/2", "1", "3/2", "2", "5")))
MOMENT_THETA_PANEL = tuple(map(Fraction, ("1/2", "1", "2", "3")))


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


def rising(theta, n):
    value = Fraction(1)
    for i in range(n):
        value *= theta + i
    return value


def falling(n, s):
    return math.factorial(n) // math.factorial(n - s)


def stirling_table(n_max=32):
    table = [[0] * (n_max + 1) for _ in range(n_max + 1)]
    table[0][0] = 1
    for n in range(1, n_max + 1):
        for k in range(1, n + 1):
            table[n][k] = table[n - 1][k - 1] + (n - 1) * table[n - 1][k]
    return table


def partition_parts(n):
    answer = []

    def visit(remaining, minimum, parts):
        if remaining == 0:
            answer.append(tuple(parts))
            return
        for size in range(minimum, remaining + 1):
            visit(remaining - size, size, parts + [size])

    visit(n, 1, [])
    return answer


def cycle_multiplicity(n, counts):
    denominator = 1
    for j, count in enumerate(counts, 1):
        denominator *= (j ** count) * math.factorial(count)
    value, remainder = divmod(math.factorial(n), denominator)
    if remainder:
        raise AssertionError("nonintegral cycle multiplicity")
    return value


def count_vector_rows():
    rows = []
    for n in range(1, 17):
        for parts in partition_parts(n):
            counter = Counter(parts)
            counts = [counter.get(j, 0) for j in range(1, n + 1)]
            rows.append({"n": n, "counts": counts, "block_count": len(parts),
                         "cycle_multiplicity": cycle_multiplicity(n, counts)})
    return rows


def stirling_rows(table):
    return [{"n": n, "k": k, "unsigned_stirling_first_kind": table[n][k]}
            for n in range(1, 33) for k in range(1, n + 1)]


def k_distribution_rows(table):
    rows = []
    for theta in THETA_PANEL:
        for n in range(1, 33):
            denominator = rising(theta, n)
            for k in range(1, n + 1):
                rows.append({"theta": fstr(theta), "n": n, "k": k,
                             "probability": fstr(Fraction(table[n][k]) * theta ** k / denominator)})
    return rows


def bernoulli_rows():
    rows = []
    for theta in THETA_PANEL:
        for i in range(1, 65):
            p = theta / (theta + i - 1)
            rows.append({"theta": fstr(theta), "customer": i,
                         "new_block_probability": fstr(p),
                         "old_block_probability": fstr(1 - p),
                         "variance_contribution": fstr(p * (1 - p))})
    return rows


def moment_patterns():
    raw = []
    for j in range(1, 7):
        for order in range(1, 4):
            if j * order <= 12:
                raw.append(((j, order),))
    for j in range(1, 7):
        for ell in range(j + 1, 7):
            if j + ell <= 12:
                raw.append(((j, 1), (ell, 1)))
    raw.extend([((1, 2), (2, 1)), ((1, 1), (2, 2)), ((1, 1), (2, 1), (3, 1)),
                ((2, 2), (3, 1)), ((1, 3), (3, 1)), ((1, 2), (2, 1), (4, 1))])
    return tuple(dict.fromkeys(raw))


def factorial_moment_rows():
    rows = []
    for pattern in moment_patterns():
        occupied = sum(j * order for j, order in pattern)
        marked = sum(order for _, order in pattern)
        for theta in MOMENT_THETA_PANEL:
            poisson = Fraction(1)
            for j, order in pattern:
                poisson *= (theta / j) ** order
            for n in sorted({occupied, occupied + 1, occupied + 5, max(24, 2 * occupied), 48}):
                correction = Fraction(falling(n, occupied)) * rising(theta, n - occupied) / rising(theta, n)
                rows.append({
                    "pattern": [{"block_size": j, "falling_order": order} for j, order in pattern],
                    "occupied_labels": occupied, "marked_blocks": marked,
                    "theta": fstr(theta), "n": n,
                    "finite_correction": fstr(correction),
                    "factorial_moment": fstr(poisson * correction),
                    "independent_poisson_limit_moment": fstr(poisson)})
    return rows


def normalization_rows(counts):
    by_n = {n: [] for n in range(1, 17)}
    for row in counts:
        by_n[row["n"]].append(row)
    rows = []
    for n, group in by_n.items():
        permutation_sum = sum(row["cycle_multiplicity"] for row in group)
        for theta in THETA_PANEL:
            weighted = sum(Fraction(row["cycle_multiplicity"]) * theta ** row["block_count"]
                           for row in group)
            rows.append({"n": n, "theta": fstr(theta),
                         "partition_count_vectors": len(group),
                         "permutation_multiplicity_sum": permutation_sum,
                         "weighted_cycle_sum": fstr(weighted),
                         "rising_factorial": fstr(rising(theta, n)),
                         "normalized_probability_sum": fstr(weighted / rising(theta, n))})
    return rows


def boundary_rows():
    rows = []
    for n in range(1, 17):
        rows.append({"n": n,
            "single_block_numerator_without_denominator": f"theta*{math.factorial(n - 1)}",
            "all_singletons_numerator_without_denominator": f"theta^{n}",
            "theta_one_single_block_probability": fstr(Fraction(1, n)),
            "theta_one_all_singletons_probability": fstr(Fraction(1, math.factorial(n)))})
    return rows


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    table = stirling_table()
    counts = count_vector_rows()
    stirling = stirling_rows(table)
    distributions = k_distribution_rows(table)
    bernoulli = bernoulli_rows()
    moments = factorial_moment_rows()
    normalizations = normalization_rows(counts)
    boundaries = boundary_rows()
    body = {
        "schema": "hcs-c353-ewens-crp-evidence-v1",
        "candidate_id": "HCS-C353", "obstruction_id": "HEN-O337",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C353/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {"parameter": "theta>0", "initial_partition": "{{1}}",
                  "new_block_probability": "theta/(theta+n)",
                  "join_block_probability": "block_size/(theta+n)",
                  "state_at_time_n": "set partition of [n]"},
        "theorem_contract": {
            "exchangeability": "partition probability depends only on block sizes",
            "eppf": "theta^k/(theta rising n) times product (block_size-1)!",
            "occupancy": "n!/(theta rising n) times product (theta/j)^c_j/c_j!",
            "block_count": "sum of independent Bernoulli(theta/(theta+i-1)) innovations",
            "laws": "K_n/log n tends almost surely to theta and its variance-standardized law is normal",
            "poisson": "every fixed finite vector (C_1,...,C_m) tends to independent Poisson(theta/j)"},
        "finite_grid": {"count_vector_n_max": 16, "count_vector_rows": len(counts),
                        "stirling_n_max": 32, "stirling_rows": len(stirling),
                        "theta_values": len(THETA_PANEL),
                        "k_distribution_rows": len(distributions),
                        "bernoulli_customer_max": 64, "bernoulli_rows": len(bernoulli),
                        "factorial_moment_patterns": len(moment_patterns()),
                        "factorial_moment_rows": len(moments),
                        "normalization_rows": len(normalizations), "boundary_rows": len(boundaries)},
        "collision_boundary": {
            "C215": "Kingman coalescent merges a fixed population backward in time, not CRP insertion growth",
            "C331": "Moran and Wright-Fisher allele-frequency diffusions, not exchangeable set-partition insertion",
            "C342": "discrete WKB birth-death chains on a fixed line, not a growing combinatorial state space"},
        "nonclaims": [
            "no Poisson-Dirichlet ranked-frequency convergence theorem",
            "no functional central limit theorem, moderate deviations, or process-level coupling rate",
            "no claim that finite block counts are independent before the limit",
            "no target arithmetic local data, Euler factors, root number, automorphy, target functional equation, target-zero match, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "Warren J. Ewens", "year": 1972,
             "identifier": "DOI:10.1016/0040-5809(72)90035-4",
             "url": "https://doi.org/10.1016/0040-5809(72)90035-4",
             "role": "primary sampling-formula source"},
            {"authors": "Fred M. Hoppe", "year": 1984,
             "identifier": "DOI:10.1007/BF00275863",
             "url": "https://doi.org/10.1007/BF00275863",
             "role": "Polya-like urn construction and Ewens-formula lineage"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
            "claims_root_number": False, "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False, "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "count_vector_rows": counts, "stirling_rows": stirling,
        "k_distribution_rows": distributions, "bernoulli_rows": bernoulli,
        "factorial_moment_rows": moments, "normalization_rows": normalizations,
        "boundary_rows": boundaries,
        "enumeration": {"all_arithmetic_exact": True, "floating_point_used": False,
                        "finite_evidence_proves_asymptotic_theorem": False,
                        "count_vector_sha256": digest(counts), "stirling_sha256": digest(stirling),
                        "k_distribution_sha256": digest(distributions),
                        "bernoulli_sha256": digest(bernoulli),
                        "factorial_moment_sha256": digest(moments),
                        "normalization_sha256": digest(normalizations),
                        "boundary_sha256": digest(boundaries)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C353 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C353_PRODUCER_PASS {data['finite_grid']['count_vector_rows']} count vectors "
          f"{data['finite_grid']['factorial_moment_rows']} factorial moments {data['payload_sha256']}")


if __name__ == "__main__":
    main()
