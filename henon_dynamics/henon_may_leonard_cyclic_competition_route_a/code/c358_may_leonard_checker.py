#!/usr/bin/env python3
"""Independent exact checker for HCS-C358; imports no producer code."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c358_may_leonard_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C358/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "305315cd4f2be502ab71d6002b22756aaa59b685a40cd5a00f49a1298798bd41"
YAML_SEMANTIC = "84e064e947cbc912bb42bc8f3dc925cb509aafef099abf52743de846134aa932"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAIRS = [("1/4", "3/2"), ("1/2", "5/4"), ("1/2", "3/2"),
         ("1/4", "7/4"), ("1/2", "7/4"), ("1/4", "2"),
         ("3/2", "1/4"), ("5/4", "1/2"), ("3/2", "1/2"),
         ("7/4", "1/4"), ("7/4", "1/2"), ("2", "1/4")]
POINTS = [("1/5", "2/5", "3/5"), ("1/2", "3/4", "5/4"),
          ("2/3", "5/6", "7/6"), ("1", "2", "4"),
          ("3/2", "1/3", "5/4"), ("7/8", "9/8", "11/8")]
SIMPLEX = [("1/6", "1/3", "1/2"), ("1/5", "3/10", "1/2"),
           ("1/4", "1/3", "5/12"), ("2/9", "1/3", "4/9"),
           ("3/10", "1/5", "1/2"), ("5/12", "1/4", "1/3")]
TOP_KEYS = {"schema", "candidate_id", "obstruction_id", "evaluation_date",
            "source_commit", "fixed_epoch", "scope_literal", "evaluator",
            "route_a_yaml", "model", "theorem_contract", "collision_boundary",
            "nonclaims", "references", "parameter_rows", "invariant_rows",
            "critical_rows", "logistic_rows", "edge_rows", "boundary_rows",
            "section_hashes", "enumeration", "route_a", "scope_flags",
            "payload_sha256"}
YAML_KEYS = {"schema", "candidate_id", "title", "evaluation_date", "source_commit",
             "fixed_epoch", "scope_literal", "evaluator_authority",
             "evaluator_version", "evaluator_authority_sha256", "obstruction_id",
             "candidate_definition", "family", "phase_space", "dynamics",
             "parameters", "parameter_provenance", "arithmetic_origin", "clock",
             "normalization", "determinant_convention", "orbit_cutoff", "precision",
             "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2",
             "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
             "route_b_lock_reason", "scope_flags", "theorem_status",
             "finite_evidence_role", "source_owner_tokens"}
FALSE_FLAGS = {"claims_target_arithmetic_local_data", "claims_target_euler_factors",
               "claims_root_number", "claims_automorphy",
               "claims_target_divisor_or_counting_law",
               "claims_target_functional_equation", "claims_target_zero_match",
               "claims_hilbert_polya_operator", "invokes_route_b"}
MODEL = {
    "equations": ["x'=x(1-x-a*y-b*z)", "y'=y(1-b*x-y-a*z)",
                  "z'=z(1-a*x-b*y-z)"],
    "parameter_chamber": "a,b>=0 and exactly one of a,b is below 1 and the other above 1",
    "interior": "x,y,z>0",
    "critical_normalization": "S=x+y+z; (u,v,w)=(x,y,z)/S; d tau=S dt",
}
THEOREM = {
    "global_flow": "positive octant invariant, interior preserved, every solution forward complete and bounded",
    "source_identity": "d log(x*y*z/S^3)/dt=(2-a-b)*(S^2-3*(xy+yz+zx))/S",
    "subcritical": "if a+b<2 every interior orbit converges to (1,1,1)/(1+a+b)",
    "critical": "if a+b=2, normalized noncentral leaves uvw=h are periodic and every original orbit approaches one with an exact phase",
    "supercritical": "if a+b>2 the diagonal is the stable manifold of coexistence and every other interior orbit approaches the full oriented boundary heteroclinic cycle",
    "period": "T_h=2/|1-a| integral_[r_-(h)]^[r_+(h)] du/sqrt(u*(u*(1-u)^2-4h))",
    "boundaries": "coordinate faces, origin, axial equilibria, orientation reversal, a=b=1, and dominance walls are explicit",
}
COLLISIONS = {
    "C211": "two-species Hamiltonian Lotka-Volterra annulus, not three-species cyclic competition",
    "C254": "chemostat extinction threshold, not a periodic-to-heteroclinic transition",
    "C271": "network SIS threshold, not competitive three-dimensional flow",
    "C347": "mean-field stochastic phase PDE, not a polynomial cyclic population ODE",
}
NONCLAIMS = [
    "no classification of the founder-control chamber a>1 and b>1",
    "no finite-time extinction for deterministic interior solutions",
    "no stochastic population or demographic-noise theorem",
    "no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route B",
]


def pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values
          if tag != "tag:yaml.org,2002:timestamp"]
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


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                             strict_mapping)


def load_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode()


def s(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def orient(a, b):
    return ("E1_to_E3_to_E2_to_E1" if a < 1 < b
            else "E1_to_E2_to_E3_to_E1")


def regime(total):
    if total < 2:
        return "coexistence"
    return "critical_periodic" if total == 2 else "heteroclinic"


def expected_parameters():
    out = []
    for aa, bb in PAIRS:
        a, b = F(aa), F(bb)
        total = a + b
        out.append({"a": s(a), "b": s(b), "sum": s(total),
                    "orientation": orient(a, b), "phase": regime(total),
                    "coexistence_coordinate": s(1 / (1 + total)),
                    "radial_eigenvalue": "-1",
                    "tangent_real_part": s((total - 2) / (2 * (1 + total))),
                    "tangent_imaginary_squared": s(3 * (b - a) ** 2 / (4 * (1 + total) ** 2)),
                    "log_R_sign": "positive" if total < 2 else ("zero" if total == 2 else "negative")})
    return out


def expected_invariants():
    out = []
    for aa, bb in PAIRS:
        a, b = F(aa), F(bb)
        for raw_point in POINTS:
            x, y, z = map(F, raw_point)
            field = (x * (1 - x - a * y - b * z),
                     y * (1 - b * x - y - a * z),
                     z * (1 - a * x - b * y - z))
            total = x + y + z
            pair_sum = x * y + y * z + z * x
            spread = total ** 2 - 3 * pair_sum
            dtotal = sum(field)
            dproduct = field[0] / x + field[1] / y + field[2] / z
            ratio = dproduct - 3 * dtotal / total
            out.append({"a": s(a), "b": s(b), "state": list(map(s, (x, y, z))),
                        "vector_field": list(map(s, field)), "S": s(total),
                        "Q": s(pair_sum), "spread": s(spread), "dS": s(dtotal),
                        "dS_formula": s(total - total ** 2 + (2 - a - b) * pair_sum),
                        "dlog_product": s(dproduct),
                        "dlog_product_formula": s(3 - (1 + a + b) * total),
                        "dlog_R": s(ratio),
                        "dlog_R_formula": s((2 - a - b) * spread / total)})
    return out


def expected_critical():
    out = []
    for aa, bb in PAIRS:
        a, b = F(aa), F(bb)
        if a + b != 2:
            continue
        delta = 1 - a
        for raw_point in SIMPLEX:
            u, v, w = map(F, raw_point)
            h = u * v * w
            du, dv, dw = (delta * u * (v - w), delta * v * (w - u),
                          delta * w * (u - v))
            out.append({"a": s(a), "b": s(b), "delta": s(delta),
                        "simplex_state": list(map(s, (u, v, w))), "h": s(h),
                        "normalized_field": list(map(s, (du, dv, dw))),
                        "sum_derivative": s(du + dv + dw),
                        "product_derivative": s(du * v * w + u * dv * w + u * v * dw),
                        "u_square_velocity": s(du ** 2),
                        "quartic_formula": s(delta ** 2 * u * (u * (1 - u) ** 2 - 4 * h))})
    return out


def expected_logistic():
    out = []
    for initial in map(F, ("1/5", "1/2", "1", "3/2", "4")):
        for q in map(F, ("1/4", "1/2", "1", "2", "5")):
            denominator = 1 + initial * (q - 1)
            if denominator <= 0:
                continue
            value = initial * q / denominator
            out.append({"S0": s(initial), "q_exp_t": s(q), "S": s(value),
                        "dS_dt_from_q": s(q * initial / denominator ** 2),
                        "logistic_rhs": s(value * (1 - value))})
    return out


def expected_edges():
    out = []
    for a, b in ((F(1, 2), F(3, 2)), (F(3, 2), F(1, 2))):
        if a < b:
            triples = (("y=0", "E1", "E3"), ("x=0", "E3", "E2"), ("z=0", "E2", "E1"))
        else:
            triples = (("z=0", "E1", "E2"), ("x=0", "E2", "E3"), ("y=0", "E3", "E1"))
        low, high = min(a, b), max(a, b)
        for plane, source, target in triples:
            out.append({"a": s(a), "b": s(b), "plane": plane, "source": source,
                        "target": target, "source_unstable_rate": s(1 - low),
                        "target_transverse_stable_rate": s(1 - high),
                        "orientation": orient(a, b)})
    return out


BOUNDARIES = [
    {"boundary": "origin", "classification": "repelling equilibrium in the positive octant"},
    {"boundary": "positive diagonal", "equation": "r'=r(1-(1+a+b)r)",
     "classification": "global one-dimensional stable set of coexistence when a+b>2 inside the cyclic chamber"},
    {"boundary": "a=b=1", "equation": "x_i'=x_i(1-S)",
     "classification": "ratios are fixed and the entire simplex S=1 is equilibria"},
    {"boundary": "a=1 or b=1 away from a=b=1",
     "classification": "nonhyperbolic dominance wall excluded from the strict cyclic-chamber global theorem"},
    {"boundary": "coordinate planes",
     "classification": "two-species competitive faces form the three directed heteroclinic connections"},
]


def check(path, evaluation):
    count = 0
    data = json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(data) is not dict or set(data) != TOP_KEYS:
        raise AssertionError("evidence top-level schema")
    claimed = data["payload_sha256"]
    body = dict(data)
    del body["payload_sha256"]
    if claimed != hashlib.sha256(canonical(body)).hexdigest():
        raise AssertionError("payload hash")
    count += 1
    if (data["schema"], data["candidate_id"], data["obstruction_id"],
            data["evaluation_date"], data["source_commit"], data["fixed_epoch"],
            data["scope_literal"]) != (
            "hcs-c358-may-leonard-evidence-v1", "HCS-C358", "HEN-O342",
            "2026-09-03", SOURCE, 1788393600, SCOPE):
        raise AssertionError("identity")
    count += 7
    if data["evaluator"] != {"authority": "flow_systems/skills/route-a-evaluator.md",
                             "version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    if data["route_a_yaml"] != {"relative_path": "evaluations/route_a/HCS-C358/2026-09-03.yaml",
                                "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}:
        raise AssertionError("YAML ledger")
    if data["model"] != MODEL or data["theorem_contract"] != THEOREM:
        raise AssertionError("model/theorem contract")
    if data["collision_boundary"] != COLLISIONS or data["nonclaims"] != NONCLAIMS:
        raise AssertionError("collision/nonclaim contract")
    count += 2
    raw = evaluation.read_bytes()
    semantic = load_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW or hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation hash")
    if set(semantic) != YAML_KEYS:
        raise AssertionError("evaluation unknown/missing key")
    if (semantic["candidate_id"], semantic["obstruction_id"], semantic["source_commit"],
            semantic["evaluation_date"], semantic["fixed_epoch"], semantic["scope_literal"]) != (
            "HCS-C358", "HEN-O342", SOURCE, "2026-09-03", 1788393600, SCOPE):
        raise AssertionError("evaluation identity")
    if semantic["tuple"] != ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]:
        raise AssertionError("evaluation tuple")
    if semantic["overall_verdict"] != "ROUTE_A_REJECTED" or semantic["route_b_invocation_allowed"] is not False:
        raise AssertionError("evaluation decision")
    if set(semantic["scope_flags"]) != FALSE_FLAGS or any(type(value) is not bool or value for value in semantic["scope_flags"].values()):
        raise AssertionError("evaluation scope flags")
    count += 12
    expected = {"parameter_rows": expected_parameters(), "invariant_rows": expected_invariants(),
                "critical_rows": expected_critical(), "logistic_rows": expected_logistic(),
                "edge_rows": expected_edges(), "boundary_rows": BOUNDARIES}
    for section, rows in expected.items():
        if data[section] != rows:
            raise AssertionError(f"{section} exact reconstruction")
        if data["section_hashes"][section] != hashlib.sha256(canonical(rows)).hexdigest():
            raise AssertionError(f"{section} digest")
        if data["enumeration"][section] != len(rows):
            raise AssertionError(f"{section} count")
        count += 3 * len(rows) + 2
    if set(data["section_hashes"]) != set(expected):
        raise AssertionError("section hash schema")
    if set(data["enumeration"]) != set(expected) | {"finite_evidence_proves_global_theorem"}:
        raise AssertionError("enumeration schema")
    if data["enumeration"]["finite_evidence_proves_global_theorem"] is not False:
        raise AssertionError("finite evidence overclaim")
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                           "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("route-a result")
    if set(data["scope_flags"]) != FALSE_FLAGS or any(type(value) is not bool or value for value in data["scope_flags"].values()):
        raise AssertionError("evidence scope flags")
    if data["references"] != [
        {"identifier": "DOI:10.1137/0129022", "role": "original May-Leonard cyclic competition model"},
        {"identifier": "DOI:10.1016/j.nonrwa.2012.06.004", "role": "integrability and global-dynamics source context"}]:
        raise AssertionError("references")
    count += 8
    return count


def main():
    if sys.flags.optimize:
        raise RuntimeError("C358 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    count = check(args.evidence, args.evaluation)
    print(f"C358 independent May-Leonard checker: PASS {count} exact assertions")


if __name__ == "__main__":
    main()
