#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C326."""
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
OUTPUT = ROOT / "results/c326_two_site_inclusion_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C326/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "c85056e422437e7d31135550a458b4095e0a9e33bcbf4c5018f7a46007fe2e79"
YAML_SEMANTIC = "d37c8ed9bedff936bdfa64c5caa85312101ae2531cd043be53985c352761ccb9"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600

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


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rising(a: Fraction, k: int) -> Fraction:
    value = Fraction(1)
    for index in range(k):
        value *= a + index
    return value


def hahn_value(n: int, alpha: Fraction, degree: int, x: int) -> Fraction:
    """Terminating 3F2(-j,j+2a-1,-x; a,-N;1)."""
    total = Fraction(0)
    for k in range(degree + 1):
        numerator = rising(Fraction(-degree), k) * rising(Fraction(degree) + 2 * alpha - 1, k)
        numerator *= rising(Fraction(-x), k)
        denominator = rising(alpha, k) * rising(Fraction(-n), k) * math.factorial(k)
        total += numerator / denominator
    return total


def parameter_row(n: int, alpha: Fraction):
    weights = [rising(alpha, x) * rising(alpha, n - x) /
               (math.factorial(x) * math.factorial(n - x)) for x in range(n + 1)]
    normalizer = rising(2 * alpha, n) / math.factorial(n)
    stationary = [weight / normalizer for weight in weights]
    rates = []
    for x in range(n + 1):
        rates.append({"x": x,
                      "upward": q(Fraction(n - x) * (alpha + x)),
                      "downward": q(Fraction(x) * (alpha + n - x))})
    spectral = []
    for degree in range(n + 1):
        values = [hahn_value(n, alpha, degree, x) for x in range(n + 1)]
        norm = sum(stationary[x] * values[x] ** 2 for x in range(n + 1))
        spectral.append({"degree": degree,
                         "eigenvalue": q(Fraction(degree) * (degree - 1 + 2 * alpha)),
                         "hahn_values": [q(value) for value in values],
                         "squared_norm": q(norm)})
    return {"N": n, "alpha": q(alpha),
            "stationary": [{"x": x, "probability": q(stationary[x])} for x in range(n + 1)],
            "rate_rows": rates, "spectral_rows": spectral}


def boundary_row(n: int):
    rates = [{"x": x, "upward": str((n - x) * x), "downward": str(x * (n - x))}
             for x in range(n + 1)]
    if n == 0:
        absorption = ["1"]
        limit = ["1"]
    else:
        absorption = [q(Fraction(x, n)) for x in range(n + 1)]
        limit = ["1/2"] + ["0"] * (n - 1) + ["1/2"]
    family = "delta_0" if n == 0 else "c delta_0+(1-c) delta_N for 0<=c<=1"
    return {"N": n, "rate_rows": rates,
            "absorption_probability_at_N": [{"x": x, "probability": value}
                                             for x, value in enumerate(absorption)],
            "stationary_weak_limit": [{"x": x, "probability": value}
                                      for x, value in enumerate(limit)],
            "stationary_law_family": family}


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def produce():
    evaluation = strict_yaml(EVALUATION)
    alphas = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    rows = [parameter_row(n, alpha) for alpha in alphas for n in range(9)]
    data = {
        "schema": "hcs-c326-two-site-inclusion-v1",
        "candidate_id": "HCS-C326",
        "obstruction_id": "HEN-O310",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR,
                      "authority": "flow_systems/skills/route-a-evaluator.md"},
        "model": {
            "state_space": "x in {0,...,N}, recording site-one occupancy",
            "parameter_domain": "integer N>=0 and real alpha>0",
            "upward_rate": "(N-x)(alpha+x)",
            "downward_rate": "x(alpha+N-x)",
            "clock": "continuous time with the displayed unscaled generator",
        },
        "theorem_contract": {
            "stationary_law": "unique beta-binomial(alpha,alpha) law when alpha>0",
            "spectrum": "simple eigenvalues j(j-1+2alpha), j=0,...,N",
            "eigenfunctions": "terminating Hahn 3F2 polynomials with exact orthogonality",
            "semigroup": "full finite spectral kernel and sharp L2 decay at gap 2alpha",
            "alpha_zero_face": "absorbing endpoints, coordinate martingale, hit-N probability x/N, all stationary mixtures c delta_0+(1-c) delta_N, and stationary weak limit half endpoints",
        },
        "finite_grid": {"N_min": 0, "N_max": 8,
                        "alpha_values": [q(alpha) for alpha in alphas],
                        "arithmetic": "exact rational"},
        "parameter_rows": rows,
        "alpha_zero_rows": [boundary_row(n) for n in range(9)],
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C326/2026-09-03.yaml",
            "raw_sha256": hashlib.sha256(EVALUATION.read_bytes()).hexdigest(),
            "semantic_sha256": hashlib.sha256(json.dumps(
                evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(),
        },
        "collision_boundary": {
            "C253": "Moran fixation owns a killed population chain, not reversible inclusion or Hahn diagonalization",
            "C263": "Polya urn reinforcement is discrete-time growth, not fixed-mass continuous-time exchange",
            "C285": "Gordon--Newell owns multisite product form and bottlenecks, not this full two-site spectrum",
            "C322": "Kac sphere collisions use spherical harmonics, not a conservative occupancy chain",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "Finite rational diagonalizations audit but do not prove the all-parameter theorem.",
            "No multisite, open-boundary, or condensation-scaling theorem is asserted.",
            "No literature-priority claim is made.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [
            {"authors": "Cristian Giardina, Frank Redig, and Kiamars Vafayi",
             "title": "Correlation inequalities for interacting particle systems with duality",
             "identifier": "10.1007/s10955-010-0055-0; arXiv:0906.4664"},
            {"authors": "NIST Digital Library of Mathematical Functions",
             "title": "Hahn class definitions, explicit representation, and difference equations",
             "identifier": "DLMF:18.19; DLMF:18.20.5; DLMF:18.22(ii)"},
        ],
    }
    counted = dict(data)
    data["enumeration"] = {
        "parameter_rows": len(rows),
        "state_rows": sum(row["N"] + 1 for row in rows),
        "spectral_rows": sum(row["N"] + 1 for row in rows),
        "alpha_zero_rows": 9,
        "audited_leaf_count": leaves(counted),
    }
    body = dict(data)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C326 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = produce()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C326_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['state_rows']} states")


if __name__ == "__main__":
    main()
