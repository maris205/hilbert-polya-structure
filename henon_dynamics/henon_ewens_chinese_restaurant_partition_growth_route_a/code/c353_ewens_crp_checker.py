#!/usr/bin/env python3
"""Producer-independent exact and semantic checker for HCS-C353."""
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
DEFAULT = ROOT / "results/c353_ewens_crp_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C353/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "1222ce92be15cc96a7f3cf867e7b14d9e302dd8681eace54fc65a70f17f30ce3"
YAML_SEMANTIC = "a25cba8c895eed584d2563bb10d0f6f1e3453a4708c616b223bb264b6005375e"
THETAS = tuple(map(Fraction, ("1/2", "1", "3/2", "2", "5")))
MOMENT_THETAS = tuple(map(Fraction, ("1/2", "1", "2", "3")))
FLAGS = {"claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False, "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False}


def duplicate_pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


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
    answer = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in answer:
            raise ValueError("duplicate/non-string YAML key")
        answer[key] = loader.construct_object(value_node, deep=deep)
    return answer


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors forbidden")
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


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rising(theta, n):
    value = Fraction(1)
    for offset in range(n):
        value *= theta + offset
    return value


def falling(n, s):
    return math.factorial(n) // math.factorial(n - s)


def independent_stirling():
    rows = {(0, 0): 1}
    for n in range(1, 33):
        for k in range(1, n + 1):
            rows[n, k] = rows.get((n - 1, k - 1), 0) + (n - 1) * rows.get((n - 1, k), 0)
    return rows


def partitions(remaining, minimum=1):
    if remaining == 0:
        yield ()
    for first in range(minimum, remaining + 1):
        for tail in partitions(remaining - first, first):
            yield (first,) + tail


def expected_counts():
    rows = []
    for n in range(1, 17):
        for parts in partitions(n):
            counter = Counter(parts)
            counts = [counter.get(j, 0) for j in range(1, n + 1)]
            denominator = math.prod(j ** count * math.factorial(count)
                                    for j, count in enumerate(counts, 1))
            rows.append({"n": n, "counts": counts, "block_count": len(parts),
                         "cycle_multiplicity": math.factorial(n) // denominator})
    return rows


def patterns():
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


def reconstruct():
    stir = independent_stirling()
    counts = expected_counts()
    stirling_rows = [{"n": n, "k": k, "unsigned_stirling_first_kind": stir[n, k]}
                     for n in range(1, 33) for k in range(1, n + 1)]
    distributions = []
    for theta in THETAS:
        for n in range(1, 33):
            for k in range(1, n + 1):
                distributions.append({"theta": fstr(theta), "n": n, "k": k,
                    "probability": fstr(Fraction(stir[n, k]) * theta ** k / rising(theta, n))})
    bernoulli = []
    for theta in THETAS:
        for i in range(1, 65):
            p = theta / (theta + i - 1)
            bernoulli.append({"theta": fstr(theta), "customer": i,
                "new_block_probability": fstr(p), "old_block_probability": fstr(1 - p),
                "variance_contribution": fstr(p * (1 - p))})
    moments = []
    for pattern in patterns():
        occupied = sum(j * order for j, order in pattern)
        marked = sum(order for _, order in pattern)
        for theta in MOMENT_THETAS:
            poisson = math.prod((theta / j) ** order for j, order in pattern)
            for n in sorted({occupied, occupied + 1, occupied + 5, max(24, 2 * occupied), 48}):
                correction = Fraction(falling(n, occupied)) * rising(theta, n - occupied) / rising(theta, n)
                moments.append({"pattern": [{"block_size": j, "falling_order": order}
                                              for j, order in pattern],
                    "occupied_labels": occupied, "marked_blocks": marked,
                    "theta": fstr(theta), "n": n, "finite_correction": fstr(correction),
                    "factorial_moment": fstr(poisson * correction),
                    "independent_poisson_limit_moment": fstr(poisson)})
    grouped = {n: [] for n in range(1, 17)}
    for row in counts:
        grouped[row["n"]].append(row)
    normalizations = []
    for n, group in grouped.items():
        for theta in THETAS:
            weighted = sum(Fraction(row["cycle_multiplicity"]) * theta ** row["block_count"] for row in group)
            normalizations.append({"n": n, "theta": fstr(theta),
                "partition_count_vectors": len(group),
                "permutation_multiplicity_sum": sum(row["cycle_multiplicity"] for row in group),
                "weighted_cycle_sum": fstr(weighted), "rising_factorial": fstr(rising(theta, n)),
                "normalized_probability_sum": fstr(weighted / rising(theta, n))})
    boundaries = [{"n": n,
        "single_block_numerator_without_denominator": f"theta*{math.factorial(n - 1)}",
        "all_singletons_numerator_without_denominator": f"theta^{n}",
        "theta_one_single_block_probability": fstr(Fraction(1, n)),
        "theta_one_all_singletons_probability": fstr(Fraction(1, math.factorial(n)))}
        for n in range(1, 17)]
    return counts, stirling_rows, distributions, bernoulli, moments, normalizations, boundaries


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def check_yaml(value):
    keys = ["schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
        "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
        "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
        "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"]
    exact_keys(value, keys, "YAML top")
    need((value["schema"], value["candidate_id"], value["obstruction_id"], value["evaluation_date"],
          value["source_commit"], value["fixed_epoch"], value["scope_literal"]) ==
         ("route-a-evaluation-v0.2.0", "HCS-C353", "HEN-O337", "2026-09-03", SOURCE, 1788393600, SCOPE), "YAML identity")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and
         value["evaluator_version"] == "0.2.0" and value["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(value["artifact_paths"] == ["results/c353_ewens_crp_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    verdicts = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "STOP_SCOPED"]
    for index, name in enumerate(("a0", "a1", "a2", "a3", "a4")):
        exact_keys(value[name], ["verdict", "evidence_status", "strongest_evidence", "strongest_failure"], f"YAML {name}")
        need(value[name]["verdict"] == verdicts[index] and value[name]["evidence_status"] == statuses[index], f"YAML {name}")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "YAML outcome")
    need(value["route_b_invocation_allowed"] is False and value["scope_flags"] == FLAGS, "YAML firewall")
    need(value["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(value["source_owner_tokens"] == ["10.1016/0040-5809(72)90035-4", "10.1007/BF00275863"], "YAML sources")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C353 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    raw = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(raw).hexdigest() == YAML_RAW, "YAML raw hash")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic hash")
    check_yaml(evaluation)
    top = ["schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator", "route_a_yaml", "model", "theorem_contract", "finite_grid",
        "collision_boundary", "nonclaims", "references", "route_a", "scope_flags", "count_vector_rows",
        "stirling_rows", "k_distribution_rows", "bernoulli_rows", "factorial_moment_rows",
        "normalization_rows", "boundary_rows", "enumeration", "payload_sha256"]
    exact_keys(data, top, "evidence top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need((data["schema"], data["candidate_id"], data["obstruction_id"],
          data["evaluation_date"], data["source_commit"], data["fixed_epoch"],
          data["scope_literal"]) == ("hcs-c353-ewens-crp-evidence-v1", "HCS-C353",
          "HEN-O337", "2026-09-03", SOURCE, 1788393600, SCOPE), "identity")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C353/2026-09-03.yaml", "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {"parameter": "theta>0", "initial_partition": "{{1}}",
        "new_block_probability": "theta/(theta+n)", "join_block_probability": "block_size/(theta+n)",
        "state_at_time_n": "set partition of [n]"}, "model")
    need(data["theorem_contract"] == {"exchangeability": "partition probability depends only on block sizes",
        "eppf": "theta^k/(theta rising n) times product (block_size-1)!",
        "occupancy": "n!/(theta rising n) times product (theta/j)^c_j/c_j!",
        "block_count": "sum of independent Bernoulli(theta/(theta+i-1)) innovations",
        "laws": "K_n/log n tends almost surely to theta and its variance-standardized law is normal",
        "poisson": "every fixed finite vector (C_1,...,C_m) tends to independent Poisson(theta/j)"}, "contract")
    need(data["collision_boundary"] == {"C215": "Kingman coalescent merges a fixed population backward in time, not CRP insertion growth",
        "C331": "Moran and Wright-Fisher allele-frequency diffusions, not exchangeable set-partition insertion",
        "C342": "discrete WKB birth-death chains on a fixed line, not a growing combinatorial state space"}, "collision")
    need(data["nonclaims"] == ["no Poisson-Dirichlet ranked-frequency convergence theorem",
        "no functional central limit theorem, moderate deviations, or process-level coupling rate",
        "no claim that finite block counts are independent before the limit",
        "no target arithmetic local data, Euler factors, root number, automorphy, target functional equation, target-zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [{"authors": "Warren J. Ewens", "year": 1972,
        "identifier": "DOI:10.1016/0040-5809(72)90035-4", "url": "https://doi.org/10.1016/0040-5809(72)90035-4",
        "role": "primary sampling-formula source"}, {"authors": "Fred M. Hoppe", "year": 1984,
        "identifier": "DOI:10.1007/BF00275863", "url": "https://doi.org/10.1007/BF00275863",
        "role": "Polya-like urn construction and Ewens-formula lineage"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "scope flags")
    counts, stirling, distributions, bernoulli, moments, normalizations, boundaries = reconstruct()
    sections = [("count_vector_rows", counts), ("stirling_rows", stirling),
        ("k_distribution_rows", distributions), ("bernoulli_rows", bernoulli),
        ("factorial_moment_rows", moments), ("normalization_rows", normalizations),
        ("boundary_rows", boundaries)]
    for name, expected in sections:
        need(data[name] == expected, name)
    expected_grid = {"count_vector_n_max": 16, "count_vector_rows": len(counts),
        "stirling_n_max": 32, "stirling_rows": len(stirling), "theta_values": 5,
        "k_distribution_rows": len(distributions), "bernoulli_customer_max": 64,
        "bernoulli_rows": len(bernoulli), "factorial_moment_patterns": len(patterns()),
        "factorial_moment_rows": len(moments), "normalization_rows": len(normalizations),
        "boundary_rows": len(boundaries)}
    need(data["finite_grid"] == expected_grid, "finite grid")
    expected_enum = {"all_arithmetic_exact": True, "floating_point_used": False,
        "finite_evidence_proves_asymptotic_theorem": False,
        "count_vector_sha256": digest(counts), "stirling_sha256": digest(stirling),
        "k_distribution_sha256": digest(distributions), "bernoulli_sha256": digest(bernoulli),
        "factorial_moment_sha256": digest(moments), "normalization_sha256": digest(normalizations),
        "boundary_sha256": digest(boundaries)}
    need(data["enumeration"] == expected_enum, "enumeration")
    need(all(row["normalized_probability_sum"] == "1" for row in normalizations), "normalization")
    print(f"C353 independent Ewens-CRP checker: PASS {sum(len(value) for _, value in sections)} exact rows")


if __name__ == "__main__":
    main()
