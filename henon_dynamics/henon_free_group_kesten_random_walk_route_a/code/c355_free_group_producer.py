#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C355."""
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
DEFAULT_OUTPUT = ROOT / "results/c355_free_group_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C355/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "9410dad95b7cec2aae089b70e213a37703296130e17e9c4432efd58e6ddf4423"
YAML_SEMANTIC = "746e6f059b48f299231c2566577c208e67d6839d135083ab3f6d431e4845f0e3"
D_PANEL = (4, 6, 8, 10)
N_MAX = 64
DP_TIME_MAX = 32


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
            raise ValueError("merge key")
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


def catalan(n):
    return math.comb(2 * n, n) // (n + 1)


def dyck_by_excursions(n, k):
    if n == 0 and k == 0:
        return 1
    if not 1 <= k <= n:
        return 0
    numerator = k * math.comb(2 * n - k, n)
    value, remainder = divmod(numerator, 2 * n - k)
    if remainder:
        raise AssertionError("nonintegral Dyck count")
    return value


def closed_formula(D, n):
    if n == 0:
        return 1
    return sum(dyck_by_excursions(n, k) * D ** k * (D - 1) ** (n - k)
               for k in range(1, n + 1))


def radial_dp(D, time_max):
    rows = []
    current = {0: 1}
    for time in range(time_max + 1):
        for radius in range(time + 1):
            if (time - radius) % 2 == 0:
                rows.append({"D": D, "time": time, "radius": radius,
                             "word_count": current.get(radius, 0)})
        if time == time_max:
            break
        following = {}
        for radius, count in current.items():
            if radius == 0:
                following[1] = following.get(1, 0) + D * count
            else:
                following[radius - 1] = following.get(radius - 1, 0) + count
                following[radius + 1] = following.get(radius + 1, 0) + (D - 1) * count
        current = following
    return rows


def return_rows():
    rows = []
    for D in D_PANEL:
        for n in range(N_MAX + 1):
            count = closed_formula(D, n)
            probability = Fraction(count, D ** (2 * n))
            rows.append({"D": D, "rank": D // 2, "half_time": n, "time": 2 * n,
                         "closed_word_count": count, "probability": fstr(probability)})
    return rows


def first_return_rows():
    rows = []
    for D in D_PANEL:
        for k in range(1, N_MAX + 1):
            count = D * catalan(k - 1) * (D - 1) ** (k - 1)
            rows.append({"D": D, "half_time": k, "time": 2 * k,
                         "catalan": catalan(k - 1), "first_return_word_count": count,
                         "probability": fstr(Fraction(count, D ** (2 * k)))})
    return rows


def renewal_rows(returns, firsts):
    u = {(row["D"], row["half_time"]): row["closed_word_count"] for row in returns}
    f = {(row["D"], row["half_time"]): row["first_return_word_count"] for row in firsts}
    rows = []
    for D in D_PANEL:
        for n in range(1, N_MAX + 1):
            terms = [f[D, k] * u[D, n - k] for k in range(1, n + 1)]
            rows.append({"D": D, "half_time": n, "return_word_count": u[D, n],
                         "renewal_convolution": sum(terms), "summands": len(terms)})
    return rows


def parameter_rows():
    rows = []
    for D in D_PANEL:
        rows.append({"D": D, "rank": D // 2,
            "spectral_radius_squared": fstr(Fraction(4 * (D - 1), D * D)),
            "escape_speed": fstr(Fraction(D - 2, D)),
            "clt_variance": fstr(Fraction(4 * (D - 1), D * D)),
            "eventual_return_probability": fstr(Fraction(1, D - 1)),
            "escape_probability": fstr(Fraction(D - 2, D - 1))})
    return rows


def boundary_rows():
    rows = []
    D = 2
    for n in range(N_MAX + 1):
        count = math.comb(2 * n, n)
        first = 0 if n == 0 else 2 * catalan(n - 1)
        rows.append({"rank": 1, "D": D, "half_time": n,
                     "return_word_count": count,
                     "return_probability": fstr(Fraction(count, D ** (2 * n))),
                     "first_return_word_count": first,
                     "first_return_probability": fstr(Fraction(first, D ** (2 * n)))})
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
    radial = [row for D in D_PANEL for row in radial_dp(D, DP_TIME_MAX)]
    returns = return_rows()
    firsts = first_return_rows()
    renewals = renewal_rows(returns, firsts)
    parameters = parameter_rows()
    boundaries = boundary_rows()
    body = {
        "schema": "hcs-c355-free-group-evidence-v1",
        "candidate_id": "HCS-C355", "obstruction_id": "HEN-O339",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C355/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {"group": "free group F_d", "rank_range": "integer d>=2",
                  "degree": "D=2d", "step_law": "uniform on generators and inverses",
                  "operator": "P=A/D on the D-regular Cayley tree", "start": "identity"},
        "theorem_contract": {
            "spectrum": "P is purely absolutely continuous with spectrum [-2sqrt(D-1)/D,2sqrt(D-1)/D]",
            "root_density": "sqrt(4(D-1)-D^2*x^2)/(2*pi*(1-x^2)) on the spectral interval",
            "returns": "u_2n=D^(-2n) sum_k k/(2n-k) binom(2n-k,n) D^k (D-1)^(n-k)",
            "first_return": "f_2k=Catalan_(k-1)(D-1)^(k-1)/D^(2k-1), with total 1/(D-1)",
            "escape": "distance/n tends almost surely to (D-2)/D and obeys a centered CLT with variance 4(D-1)/D^2",
            "rank_one_boundary": "for d=1 the spectrum is arcsine, return is recurrent, speed is zero, and distance/sqrt(n) tends to |N(0,1)|"},
        "finite_grid": {"D_values": list(D_PANEL), "n_max": N_MAX,
                        "dp_time_max": DP_TIME_MAX, "radial_rows": len(radial),
                        "return_rows": len(returns), "first_return_rows": len(firsts),
                        "renewal_rows": len(renewals), "parameter_rows": len(parameters),
                        "rank_one_boundary_rows": len(boundaries)},
        "collision_boundary": {
            "C306": "killed multi-walker path avoidance, not a homogeneous Cayley-tree group walk",
            "C333": "finite-graph randomized gossip consensus, not an infinite-tree spectral walk",
            "C341": "lamplighter walk on a finite cycle has a wreath-product lamp state and finite spectrum, not free-group escape"},
        "nonclaims": [
            "no local limit theorem or sharp asymptotic prefactor beyond the stated exact return law",
            "no nonuniform generator law, free-product extension, boundary harmonic measure, or entropy theorem",
            "no interpretation of closed words as primitive arithmetic orbits and no dynamical zeta or determinant",
            "no target arithmetic local data, Euler factors, root number, automorphy, target functional equation, target-zero match, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "Harry Kesten", "year": 1959,
             "identifier": "DOI:10.1090/S0002-9947-1959-0109367-6; JSTOR DOI:10.2307/1993160",
             "url": "https://doi.org/10.1090/S0002-9947-1959-0109367-6",
             "role": "primary source for symmetric group walks and the free-group spectral-radius theorem; the two DOI strings identify the same article"},
            {"authors": "Wolfgang Woess", "year": 2000,
             "identifier": "DOI:10.1017/CBO9780511470967",
             "url": "https://doi.org/10.1017/CBO9780511470967",
             "role": "authoritative monograph lineage for random walks on infinite graphs and groups"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
            "claims_root_number": False, "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False, "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "radial_dp_rows": radial, "return_rows": returns, "first_return_rows": firsts,
        "renewal_rows": renewals, "parameter_rows": parameters,
        "rank_one_boundary_rows": boundaries,
        "enumeration": {"all_arithmetic_exact": True, "floating_point_used": False,
                        "finite_evidence_proves_infinite_tree_theorems": False,
                        "radial_dp_sha256": digest(radial), "return_sha256": digest(returns),
                        "first_return_sha256": digest(firsts), "renewal_sha256": digest(renewals),
                        "parameter_sha256": digest(parameters), "boundary_sha256": digest(boundaries)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C355 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C355_PRODUCER_PASS {data['finite_grid']['radial_rows']} radial rows "
          f"{data['finite_grid']['return_rows']} returns {data['payload_sha256']}")


if __name__ == "__main__":
    main()
