#!/usr/bin/env python3
"""Producer-independent exact and semantic checker for HCS-C355."""
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
DEFAULT = ROOT / "results/c355_free_group_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C355/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "9410dad95b7cec2aae089b70e213a37703296130e17e9c4432efd58e6ddf4423"
YAML_SEMANTIC = "746e6f059b48f299231c2566577c208e67d6839d135083ab3f6d431e4845f0e3"
D_PANEL = (4, 6, 8, 10)
N_MAX = 64
DP_TIME_MAX = 32
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


def catalans(limit):
    values = [1]
    for n in range(limit):
        values.append(values[-1] * 2 * (2 * n + 1) // (n + 2))
    return values


def dyck_compositions(n, k):
    if n == 0 and k == 0:
        return 1
    if not 1 <= k <= n:
        return 0
    return k * math.comb(2 * n - k, n) // (2 * n - k)


def independent_rows():
    cats = catalans(N_MAX)
    radial = []
    return_rows = []
    first_rows = []
    renewal_rows = []
    parameter_rows = []
    for D in D_PANEL:
        levels = {0: 1}
        return_counts = []
        for time in range(2 * N_MAX + 1):
            if time <= DP_TIME_MAX:
                for radius in range(time + 1):
                    if (time - radius) % 2 == 0:
                        radial.append({"D": D, "time": time, "radius": radius,
                                       "word_count": levels.get(radius, 0)})
            if time % 2 == 0:
                return_counts.append(levels.get(0, 0))
            following = {}
            for radius, count in levels.items():
                if radius == 0:
                    following[1] = following.get(1, 0) + D * count
                else:
                    following[radius - 1] = following.get(radius - 1, 0) + count
                    following[radius + 1] = following.get(radius + 1, 0) + (D - 1) * count
            levels = following
        for n, count in enumerate(return_counts):
            formula = 1 if n == 0 else sum(dyck_compositions(n, k) * D ** k *
                (D - 1) ** (n - k) for k in range(1, n + 1))
            need(count == formula, f"independent DP/formula D={D} n={n}")
            return_rows.append({"D": D, "rank": D // 2, "half_time": n,
                "time": 2 * n, "closed_word_count": count,
                "probability": fstr(Fraction(count, D ** (2 * n)))})
        first_counts = [0]
        for k in range(1, N_MAX + 1):
            count = D * cats[k - 1] * (D - 1) ** (k - 1)
            first_counts.append(count)
            first_rows.append({"D": D, "half_time": k, "time": 2 * k,
                "catalan": cats[k - 1], "first_return_word_count": count,
                "probability": fstr(Fraction(count, D ** (2 * k)))})
        for n in range(1, N_MAX + 1):
            total = sum(first_counts[k] * return_counts[n - k] for k in range(1, n + 1))
            renewal_rows.append({"D": D, "half_time": n,
                "return_word_count": return_counts[n], "renewal_convolution": total,
                "summands": n})
        parameter_rows.append({"D": D, "rank": D // 2,
            "spectral_radius_squared": fstr(Fraction(4 * (D - 1), D * D)),
            "escape_speed": fstr(Fraction(D - 2, D)),
            "clt_variance": fstr(Fraction(4 * (D - 1), D * D)),
            "eventual_return_probability": fstr(Fraction(1, D - 1)),
            "escape_probability": fstr(Fraction(D - 2, D - 1))})
    boundaries = []
    for n in range(N_MAX + 1):
        first = 0 if n == 0 else 2 * cats[n - 1]
        count = math.comb(2 * n, n)
        boundaries.append({"rank": 1, "D": 2, "half_time": n,
            "return_word_count": count, "return_probability": fstr(Fraction(count, 2 ** (2 * n))),
            "first_return_word_count": first,
            "first_return_probability": fstr(Fraction(first, 2 ** (2 * n)))})
    return radial, return_rows, first_rows, renewal_rows, parameter_rows, boundaries


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def check_yaml(value):
    top = ["schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
        "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
        "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
        "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
        "source_owner_tokens"]
    exact_keys(value, top, "YAML top")
    need((value["schema"], value["candidate_id"], value["obstruction_id"],
          value["evaluation_date"], value["source_commit"], value["fixed_epoch"],
          value["scope_literal"]) == ("route-a-evaluation-v0.2.0", "HCS-C355", "HEN-O339",
          "2026-09-03", SOURCE, 1788393600, SCOPE), "YAML identity")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and
         value["evaluator_version"] == "0.2.0" and
         value["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(value["artifact_paths"] == ["results/c355_free_group_evidence.json",
         "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    verdicts = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"]
    for index, branch in enumerate(("a0", "a1", "a2", "a3", "a4")):
        exact_keys(value[branch], ["verdict", "evidence_status", "strongest_evidence", "strongest_failure"], branch)
        need(value[branch]["verdict"] == verdicts[index], f"{branch} verdict")
        need(value[branch]["evidence_status"] == statuses[index], f"{branch} status")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    need(value["route_b_invocation_allowed"] is False and value["scope_flags"] == FLAGS,
         "YAML firewall")
    need(value["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem status")
    need(value["source_owner_tokens"] == ["10.1090/S0002-9947-1959-0109367-6",
        "10.2307/1993160", "10.1017/CBO9780511470967"], "YAML sources")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C355 checker refuses optimized Python")
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
        "collision_boundary", "nonclaims", "references", "route_a", "scope_flags", "radial_dp_rows",
        "return_rows", "first_return_rows", "renewal_rows", "parameter_rows", "rank_one_boundary_rows",
        "enumeration", "payload_sha256"]
    exact_keys(data, top, "evidence top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need((data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"],
          data["source_commit"], data["fixed_epoch"], data["scope_literal"]) ==
         ("hcs-c355-free-group-evidence-v1", "HCS-C355", "HEN-O339", "2026-09-03",
          SOURCE, 1788393600, SCOPE), "identity")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md",
         "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C355/2026-09-03.yaml",
         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {"group": "free group F_d", "rank_range": "integer d>=2", "degree": "D=2d",
         "step_law": "uniform on generators and inverses",
         "operator": "P=A/D on the D-regular Cayley tree", "start": "identity"}, "model")
    need(data["theorem_contract"] == {
        "spectrum": "P is purely absolutely continuous with spectrum [-2sqrt(D-1)/D,2sqrt(D-1)/D]",
        "root_density": "sqrt(4(D-1)-D^2*x^2)/(2*pi*(1-x^2)) on the spectral interval",
        "returns": "u_2n=D^(-2n) sum_k k/(2n-k) binom(2n-k,n) D^k (D-1)^(n-k)",
        "first_return": "f_2k=Catalan_(k-1)(D-1)^(k-1)/D^(2k-1), with total 1/(D-1)",
        "escape": "distance/n tends almost surely to (D-2)/D and obeys a centered CLT with variance 4(D-1)/D^2",
        "rank_one_boundary": "for d=1 the spectrum is arcsine, return is recurrent, speed is zero, and distance/sqrt(n) tends to |N(0,1)|"}, "contract")
    need(data["collision_boundary"] == {
        "C306": "killed multi-walker path avoidance, not a homogeneous Cayley-tree group walk",
        "C333": "finite-graph randomized gossip consensus, not an infinite-tree spectral walk",
        "C341": "lamplighter walk on a finite cycle has a wreath-product lamp state and finite spectrum, not free-group escape"}, "collision")
    need(data["nonclaims"] == [
        "no local limit theorem or sharp asymptotic prefactor beyond the stated exact return law",
        "no nonuniform generator law, free-product extension, boundary harmonic measure, or entropy theorem",
        "no interpretation of closed words as primitive arithmetic orbits and no dynamical zeta or determinant",
        "no target arithmetic local data, Euler factors, root number, automorphy, target functional equation, target-zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [
        {"authors": "Harry Kesten", "year": 1959,
         "identifier": "DOI:10.1090/S0002-9947-1959-0109367-6; JSTOR DOI:10.2307/1993160",
         "url": "https://doi.org/10.1090/S0002-9947-1959-0109367-6",
         "role": "primary source for symmetric group walks and the free-group spectral-radius theorem; the two DOI strings identify the same article"},
        {"authors": "Wolfgang Woess", "year": 2000,
         "identifier": "DOI:10.1017/CBO9780511470967",
         "url": "https://doi.org/10.1017/CBO9780511470967",
         "role": "authoritative monograph lineage for random walks on infinite graphs and groups"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
         "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "scope flags")
    radial, returns, firsts, renewals, parameters, boundaries = independent_rows()
    sections = [("radial_dp_rows", radial), ("return_rows", returns),
        ("first_return_rows", firsts), ("renewal_rows", renewals),
        ("parameter_rows", parameters), ("rank_one_boundary_rows", boundaries)]
    for name, expected in sections:
        need(data[name] == expected, name)
    need(data["finite_grid"] == {"D_values": list(D_PANEL), "n_max": N_MAX,
        "dp_time_max": DP_TIME_MAX, "radial_rows": len(radial), "return_rows": len(returns),
        "first_return_rows": len(firsts), "renewal_rows": len(renewals),
        "parameter_rows": len(parameters), "rank_one_boundary_rows": len(boundaries)}, "finite grid")
    need(data["enumeration"] == {"all_arithmetic_exact": True, "floating_point_used": False,
        "finite_evidence_proves_infinite_tree_theorems": False,
        "radial_dp_sha256": digest(radial), "return_sha256": digest(returns),
        "first_return_sha256": digest(firsts), "renewal_sha256": digest(renewals),
        "parameter_sha256": digest(parameters), "boundary_sha256": digest(boundaries)}, "enumeration")
    need(all(row["return_word_count"] == row["renewal_convolution"] for row in renewals), "renewal")
    exact_cells = sum(len(row) for _, rows in sections for row in rows)
    print(f"C355 independent free-group checker: PASS {sum(len(rows) for _, rows in sections)} rows {exact_cells} exact cells")


if __name__ == "__main__":
    main()
