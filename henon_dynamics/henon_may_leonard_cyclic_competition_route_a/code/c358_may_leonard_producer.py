#!/usr/bin/env python3
"""Canonical exact finite-evidence producer for HCS-C358."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c358_may_leonard_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C358/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "305315cd4f2be502ab71d6002b22756aaa59b685a40cd5a00f49a1298798bd41"
YAML_SEMANTIC = "84e064e947cbc912bb42bc8f3dc925cb509aafef099abf52743de846134aa932"

PARAMETERS = tuple(map(lambda pair: tuple(map(Fraction, pair)), (
    ("1/4", "3/2"), ("1/2", "5/4"), ("1/2", "3/2"),
    ("1/4", "7/4"), ("1/2", "7/4"), ("1/4", "2"),
    ("3/2", "1/4"), ("5/4", "1/2"), ("3/2", "1/2"),
    ("7/4", "1/4"), ("7/4", "1/2"), ("2", "1/4"))))
STATES = tuple(map(lambda row: tuple(map(Fraction, row)), (
    ("1/5", "2/5", "3/5"), ("1/2", "3/4", "5/4"),
    ("2/3", "5/6", "7/6"), ("1", "2", "4"),
    ("3/2", "1/3", "5/4"), ("7/8", "9/8", "11/8"))))
SIMPLEX_STATES = tuple(map(lambda row: tuple(map(Fraction, row)), (
    ("1/6", "1/3", "1/2"), ("1/5", "3/10", "1/2"),
    ("1/4", "1/3", "5/12"), ("2/9", "1/3", "4/9"),
    ("3/10", "1/5", "1/2"), ("5/12", "1/4", "1/3"))))


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


def strict_yaml(path: Path):
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


def fstr(value):
    value = Fraction(value)
    return (str(value.numerator) if value.denominator == 1
            else f"{value.numerator}/{value.denominator}")


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def phase(a, b):
    total = a + b
    return "coexistence" if total < 2 else ("critical_periodic" if total == 2 else "heteroclinic")


def orientation(a, b):
    if a < 1 < b:
        return "E1_to_E3_to_E2_to_E1"
    if b < 1 < a:
        return "E1_to_E2_to_E3_to_E1"
    raise ValueError("outside frozen cyclic chamber")


def parameter_rows():
    rows = []
    for a, b in PARAMETERS:
        total = a + b
        rows.append({
            "a": fstr(a), "b": fstr(b), "sum": fstr(total),
            "orientation": orientation(a, b), "phase": phase(a, b),
            "coexistence_coordinate": fstr(Fraction(1, 1) / (1 + total)),
            "radial_eigenvalue": "-1",
            "tangent_real_part": fstr((total - 2) / (2 * (1 + total))),
            "tangent_imaginary_squared": fstr(3 * (b - a) ** 2 / (4 * (1 + total) ** 2)),
            "log_R_sign": "positive" if total < 2 else ("zero" if total == 2 else "negative"),
        })
    return rows


def vector_field(a, b, x, y, z):
    return (x * (1 - x - a * y - b * z),
            y * (1 - b * x - y - a * z),
            z * (1 - a * x - b * y - z))


def invariant_rows():
    rows = []
    for a, b in PARAMETERS:
        for x, y, z in STATES:
            fx, fy, fz = vector_field(a, b, x, y, z)
            total = x + y + z
            pair = x * y + y * z + z * x
            spread = total * total - 3 * pair
            dtotal = fx + fy + fz
            dlog_product = fx / x + fy / y + fz / z
            dlog_ratio = dlog_product - 3 * dtotal / total
            rows.append({
                "a": fstr(a), "b": fstr(b),
                "state": [fstr(x), fstr(y), fstr(z)],
                "vector_field": [fstr(fx), fstr(fy), fstr(fz)],
                "S": fstr(total), "Q": fstr(pair), "spread": fstr(spread),
                "dS": fstr(dtotal),
                "dS_formula": fstr(total - total * total + (2 - a - b) * pair),
                "dlog_product": fstr(dlog_product),
                "dlog_product_formula": fstr(3 - (1 + a + b) * total),
                "dlog_R": fstr(dlog_ratio),
                "dlog_R_formula": fstr((2 - a - b) * spread / total),
            })
    return rows


def critical_rows():
    rows = []
    critical = [(a, b) for a, b in PARAMETERS if a + b == 2]
    for a, b in critical:
        delta = 1 - a
        for u, v, w in SIMPLEX_STATES:
            h = u * v * w
            du = delta * u * (v - w)
            dv = delta * v * (w - u)
            dw = delta * w * (u - v)
            rows.append({
                "a": fstr(a), "b": fstr(b), "delta": fstr(delta),
                "simplex_state": [fstr(u), fstr(v), fstr(w)],
                "h": fstr(h), "normalized_field": [fstr(du), fstr(dv), fstr(dw)],
                "sum_derivative": fstr(du + dv + dw),
                "product_derivative": fstr(du * v * w + u * dv * w + u * v * dw),
                "u_square_velocity": fstr(du * du),
                "quartic_formula": fstr(delta * delta * u * (u * (1 - u) ** 2 - 4 * h)),
            })
    return rows


def logistic_rows():
    rows = []
    for initial in map(Fraction, ("1/5", "1/2", "1", "3/2", "4")):
        for exponential in map(Fraction, ("1/4", "1/2", "1", "2", "5")):
            denominator = 1 + initial * (exponential - 1)
            if denominator <= 0:
                continue
            value = initial * exponential / denominator
            q_derivative = initial / (denominator * denominator)
            rows.append({"S0": fstr(initial), "q_exp_t": fstr(exponential),
                         "S": fstr(value), "dS_dt_from_q": fstr(exponential * q_derivative),
                         "logistic_rhs": fstr(value * (1 - value))})
    return rows


def edge_rows():
    rows = []
    for a, b in ((Fraction(1, 2), Fraction(3, 2)),
                 (Fraction(3, 2), Fraction(1, 2))):
        if a < 1 < b:
            edges = (("y=0", "E1", "E3"), ("x=0", "E3", "E2"),
                     ("z=0", "E2", "E1"))
            low, high = a, b
        else:
            edges = (("z=0", "E1", "E2"), ("x=0", "E2", "E3"),
                     ("y=0", "E3", "E1"))
            low, high = b, a
        for plane, source, target in edges:
            rows.append({"a": fstr(a), "b": fstr(b), "plane": plane,
                         "source": source, "target": target,
                         "source_unstable_rate": fstr(1 - low),
                         "target_transverse_stable_rate": fstr(1 - high),
                         "orientation": orientation(a, b)})
    return rows


def boundary_rows():
    return [
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


def build(evaluation: Path):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    parameters = parameter_rows()
    invariants = invariant_rows()
    critical = critical_rows()
    logistic = logistic_rows()
    edges = edge_rows()
    boundaries = boundary_rows()
    body = {
        "schema": "hcs-c358-may-leonard-evidence-v1",
        "candidate_id": "HCS-C358", "obstruction_id": "HEN-O342",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C358/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "equations": ["x'=x(1-x-a*y-b*z)", "y'=y(1-b*x-y-a*z)",
                          "z'=z(1-a*x-b*y-z)"],
            "parameter_chamber": "a,b>=0 and exactly one of a,b is below 1 and the other above 1",
            "interior": "x,y,z>0", "critical_normalization": "S=x+y+z; (u,v,w)=(x,y,z)/S; d tau=S dt",
        },
        "theorem_contract": {
            "global_flow": "positive octant invariant, interior preserved, every solution forward complete and bounded",
            "source_identity": "d log(x*y*z/S^3)/dt=(2-a-b)*(S^2-3*(xy+yz+zx))/S",
            "subcritical": "if a+b<2 every interior orbit converges to (1,1,1)/(1+a+b)",
            "critical": "if a+b=2, normalized noncentral leaves uvw=h are periodic and every original orbit approaches one with an exact phase",
            "supercritical": "if a+b>2 the diagonal is the stable manifold of coexistence and every other interior orbit approaches the full oriented boundary heteroclinic cycle",
            "period": "T_h=2/|1-a| integral_[r_-(h)]^[r_+(h)] du/sqrt(u*(u*(1-u)^2-4h))",
            "boundaries": "coordinate faces, origin, axial equilibria, orientation reversal, a=b=1, and dominance walls are explicit",
        },
        "collision_boundary": {
            "C211": "two-species Hamiltonian Lotka-Volterra annulus, not three-species cyclic competition",
            "C254": "chemostat extinction threshold, not a periodic-to-heteroclinic transition",
            "C271": "network SIS threshold, not competitive three-dimensional flow",
            "C347": "mean-field stochastic phase PDE, not a polynomial cyclic population ODE",
        },
        "nonclaims": [
            "no classification of the founder-control chamber a>1 and b>1",
            "no finite-time extinction for deterministic interior solutions",
            "no stochastic population or demographic-noise theorem",
            "no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route B",
        ],
        "references": [
            {"identifier": "DOI:10.1137/0129022", "role": "original May-Leonard cyclic competition model"},
            {"identifier": "DOI:10.1016/j.nonrwa.2012.06.004", "role": "integrability and global-dynamics source context"},
        ],
        "parameter_rows": parameters, "invariant_rows": invariants,
        "critical_rows": critical, "logistic_rows": logistic,
        "edge_rows": edges, "boundary_rows": boundaries,
        "section_hashes": {"parameter_rows": digest(parameters),
                           "invariant_rows": digest(invariants),
                           "critical_rows": digest(critical),
                           "logistic_rows": digest(logistic),
                           "edge_rows": digest(edges),
                           "boundary_rows": digest(boundaries)},
        "enumeration": {"parameter_rows": len(parameters),
                        "invariant_rows": len(invariants),
                        "critical_rows": len(critical),
                        "logistic_rows": len(logistic),
                        "edge_rows": len(edges),
                        "boundary_rows": len(boundaries),
                        "finite_evidence_proves_global_theorem": False},
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {"claims_target_arithmetic_local_data": False,
                        "claims_target_euler_factors": False,
                        "claims_root_number": False, "claims_automorphy": False,
                        "claims_target_divisor_or_counting_law": False,
                        "claims_target_functional_equation": False,
                        "claims_target_zero_match": False,
                        "claims_hilbert_polya_operator": False,
                        "invokes_route_b": False},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C358 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2,
                                     ensure_ascii=False) + "\n")
    print(f"C358_PRODUCER_PASS {data['payload_sha256']} "+
          f"{len(data['invariant_rows'])} invariant rows")


if __name__ == "__main__":
    main()
