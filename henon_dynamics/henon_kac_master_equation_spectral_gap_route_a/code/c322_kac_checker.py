#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C322."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c322_kac_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C322/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVALUATION_RAW = "d0f97756644e925ab6c59efeca4f4e4665838405742758c3d602398893b15a72"
EVALUATION_SEMANTIC = "8d127621e319cf76ed9b1cf126b260ca066b49f4448653cf8a60634572b74c2e"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

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


def duplicate_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root must be an object")
    return value


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, expected, label):
    need(type(value) is dict and set(value) == set(expected), f"{label} keys")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fr(value) -> Fraction:
    if type(value) is not str:
        raise TypeError("rational receipt must be string")
    result = Fraction(value)
    if q(result) != value:
        raise ValueError("noncanonical rational")
    return result


def dfact(power: int) -> int:
    result = 1
    cursor = power
    while cursor > 0:
        result *= cursor
        cursor -= 2
    return result


def spherical(exponents: tuple[int, ...]) -> Fraction:
    if any(exponent & 1 for exponent in exponents):
        return Fraction(0)
    n = len(exponents)
    half = tuple(exponent // 2 for exponent in exponents)
    total = sum(half)
    top = n ** total * math.prod(dfact(2 * power - 1) for power in half)
    bottom = math.prod(n + 2 * offset for offset in range(total))
    return Fraction(top, bottom) if total else Fraction(1)


def circle(cosine: int, sine: int) -> Fraction:
    if cosine & 1 or sine & 1:
        return Fraction(0)
    c, s = cosine // 2, sine // 2
    return Fraction(dfact(2 * c - 1) * dfact(2 * s - 1),
                    math.prod(2 * j for j in range(1, c + s + 1))) if c + s else Fraction(1)


def rotated_pair(left_power: int, right_power: int):
    answer = {}
    # First factor chooses b copies of v sin(theta); second chooses a copies of -u sin(theta).
    for b in range(left_power + 1):
        for a in range(right_power + 1):
            trig = circle(left_power - b + right_power - a, b + a)
            if trig == 0:
                continue
            old_u = left_power - b + a
            old_v = b + right_power - a
            coefficient = Fraction(math.comb(left_power, b) * math.comb(right_power, a) * (-1) ** a) * trig
            answer[(old_u, old_v)] = answer.get((old_u, old_v), Fraction(0)) + coefficient
    return {key: value for key, value in answer.items() if value}


def apply_q(monomial: tuple[int, ...]):
    n = len(monomial)
    answer = {}
    scale = Fraction(1, math.comb(n, 2))
    for i, j in itertools.combinations(range(n), 2):
        for (a, b), coefficient in rotated_pair(monomial[i], monomial[j]).items():
            term = list(monomial)
            term[i], term[j] = a, b
            term = tuple(term)
            answer[term] = answer.get(term, Fraction(0)) + scale * coefficient
    return {key: value for key, value in answer.items() if value}


def bracket(left, polynomial):
    answer = Fraction(0)
    for right, coefficient in polynomial.items():
        answer += coefficient * spherical(tuple(a + b for a, b in zip(left, right)))
    return answer


def expected_basis(n: int):
    width = min(n, 3)
    reduced = [item for item in itertools.product(range(5), repeat=width) if sum(item) <= 4]
    reduced = sorted(reduced, key=lambda item: (sum(item), item))
    return [tuple(2 * value for value in item) + (0,) * (n - width) for item in reduced]


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C322 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = 0
    exact_keys(data, {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                      "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                      "finite_grid", "conditional_operator_rows", "gap_rows", "polynomial_form_rows",
                      "quartic_ambient_action", "route_a_yaml", "collision_boundary", "route_a",
                      "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}, "root")
    required = {"schema": "hcs-c322-kac-spectral-gap-v1", "candidate_id": "HCS-C322",
                "obstruction_id": "HEN-O306", "evaluation_date": "2026-09-03",
                "fixed_epoch": 1788393600, "source_commit": SOURCE, "scope_literal": SCOPE}
    for key, value in required.items():
        need(data[key] == value, key)
        checks += 1
    need(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR,
                                "authority": "flow_systems/skills/route-a-evaluator.md"}, "evaluator")
    body = dict(data)
    payload = body.pop("payload_sha256")
    semantic = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False).encode()).hexdigest()
    need(payload == semantic, "payload")
    counted = dict(data)
    counted.pop("payload_sha256")
    need(data["enumeration"]["audited_leaf_count"] == leaves(counted), "leaf accounting")
    checks += 3

    expected_model = {
        "state_space": "S^{N-1}(sqrt(N)) with normalized surface measure",
        "pair_sampling": "uniform over unordered pairs i<j",
        "angle_measure": "dtheta/(2pi) on [-pi,pi]",
        "positive_generator": "L_N=N(I-Q_N)",
        "semigroup": "G_t=exp(-t L_N)",
        "positive_energy_scaling": "all E>0 are unitarily conjugate",
        "zero_energy_boundary": "E=0 is one point with zero mean-zero sector",
    }
    expected_theorem = {
        "gap": "Delta_N=(N+2)/(2(N-1)) for N>=2 under L_N=N(I-Q_N)",
        "slow_mode": "sum_i v_i^4-3N^2/(N+2)",
        "multiplicity": "one for N>=3; every mean-zero mode at N=2",
        "lower_bound": "full conditional-projection induction with kappa_N=3/(N^2-1)",
        "projection_transfer": "P=TT*/N; nonzero spectrum transfers to T*T/N with trivial and standard index branches",
        "decay": "sharp mean-zero L2 norm bound exp(-Delta_N t)",
        "evidence_boundary": "finite polynomial matrices audit algebra and do not prove the infinite-dimensional gap",
    }
    need(data["model"] == expected_model, "model")
    need(data["theorem_contract"] == expected_theorem, "theorem")
    need(data["finite_grid"] == {"conditional_N_min": 3, "conditional_N_max": 12,
                                  "form_N_min": 2, "form_N_max": 7, "ordinary_degree_max": 8,
                                  "basis_support_max": 3}, "grid")
    need(data["quartic_ambient_action"] == {
        "coefficient_sum_v4": "1-(N+2)/(2N(N-1))",
        "coefficient_sum_v2_squared": "3/(2N(N-1))",
        "sphere_relation": "sum_i v_i^2=N"}, "quartic action")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                              "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route")
    need(data["scope_flags"] == FLAGS, "flags")
    need(data["collision_boundary"] == {
        "C170": "the Kac ring is a deterministic scatterer toy model; C322 is a continuous-sphere random binary-collision master equation",
        "C183": "random transpositions act on a finite permutation group; Kac collisions average continuous coordinate-plane rotations",
        "C313": "sphere geodesics are deterministic variational curves; Kac dynamics is a stochastic projection average on functions",
    }, "collisions")
    need(data["nonclaims"] == [
        "Finite polynomial forms are not a proof of the infinite-dimensional spectral lower bound.",
        "No full spectrum, entropy production, nonlinear Boltzmann convergence, or nonuniform-angle theorem is asserted.",
        "No uniqueness claim is made for the N=2 slow eigenspace and no positive gap is assigned at E=0.",
        "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        "No literature-priority claim is made.",
    ], "nonclaims")
    checks += 6

    evaluation = strict_yaml(args.evaluation)
    yaml_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
                 "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
                 "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
                 "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                 "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
                 "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                 "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
                 "source_owner_tokens"}
    exact_keys(evaluation, yaml_keys, "evaluation")
    for branch in ("a0", "a1", "a2", "a3", "a4"):
        exact_keys(evaluation[branch], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, branch)
    exact_keys(evaluation["scope_flags"], FLAGS, "evaluation flags")
    lock = data["route_a_yaml"]
    exact_keys(lock, {"relative_path", "raw_sha256", "semantic_sha256"}, "YAML lock")
    need(lock["relative_path"] == "evaluations/route_a/HCS-C322/2026-09-03.yaml", "YAML relative path")
    raw_hash = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    semantic_hash = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"),
                                                ensure_ascii=False).encode()).hexdigest()
    need(raw_hash == lock["raw_sha256"] == EVALUATION_RAW, "YAML raw")
    need(semantic_hash == lock["semantic_sha256"] == EVALUATION_SEMANTIC, "YAML semantic")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "authority")
    need(evaluation["candidate_id"] == "HCS-C322" and evaluation["source_commit"] == SOURCE, "YAML identity")
    need(evaluation["tuple"] == data["route_a"]["tuple"], "YAML tuple")
    need([evaluation[name]["verdict"] for name in ("a0", "a1", "a2", "a3", "a4")] == data["route_a"]["tuple"], "YAML branch verdicts")
    need(evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    need(evaluation["route_b_invocation_allowed"] is False and type(evaluation["fixed_epoch"]) is int, "YAML types")
    need(evaluation["training_data"] == "none" and evaluation["scope_flags"] == FLAGS, "YAML scope")
    need([evaluation[name]["evidence_status"] for name in ("a0", "a1", "a2", "a3", "a4")] ==
         ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "STOP_SCOPED"], "YAML evidence status")
    need(evaluation["source_owner_tokens"] == ["UC_BERKELEY_RECORD_112857", "10.1007/BF02392695",
                                                "arXiv:math-ph/0109003"], "source tokens")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED", "theorem status")
    need(evaluation["evaluator_version"] == "0.2.0" and evaluation["evaluator_authority_sha256"] == EVALUATOR,
         "YAML evaluator version")
    checks += 11

    rows = data["conditional_operator_rows"]
    need(type(rows) is list and len(rows) == 10 and [row["N"] for row in rows] == list(range(3, 13)), "conditional coordinates")
    for row in rows:
        exact_keys(row, {"N", "cells", "kappa", "beta", "mu", "top_mode"}, "conditional row")
        n = row["N"]
        need(type(row["cells"]) is list and len(row["cells"]) == 5, "conditional cells")
        need([cell["even_degree"] for cell in row["cells"]] == [0, 2, 4, 6, 8], "conditional degrees")
        for r, cell in enumerate(row["cells"]):
            exact_keys(cell, {"even_degree", "monomial_image_coefficients_x2_ascending", "eigenvalue"}, "conditional cell")
            denominator = math.prod(n - 1 + 2 * offset for offset in range(r))
            c = Fraction(dfact(2 * r - 1), denominator) if r else Fraction(1)
            coefficients = [c * math.comb(r, j) * n ** (r - j) * (-1) ** j for j in range(r + 1)]
            need([fr(value) for value in cell["monomial_image_coefficients_x2_ascending"]] == coefficients, "K coefficients")
            need(fr(cell["eigenvalue"]) == coefficients[-1], "K eigenvalue")
            checks += len(coefficients) + 1
        need(fr(row["kappa"]) == Fraction(3, n * n - 1), "kappa")
        need(fr(row["beta"]) == Fraction(1, (n - 1) ** 2), "beta")
        need(fr(row["mu"]) == Fraction(n + 4, n * (n + 1)), "mu")
        need(row["top_mode"] == "unique degree-four coordinate polynomial sum", "top mode")
        checks += 4

    gap_rows = data["gap_rows"]
    need(type(gap_rows) is list and len(gap_rows) == 11 and [row["N"] for row in gap_rows] == list(range(2, 13)), "gap coordinates")
    product = Fraction(1)
    for row in gap_rows:
        exact_keys(row, {"N", "kappa", "induction_factor", "telescoped_product", "gap_L",
                         "quartic_Q_eigenvalue", "quartic_center", "slow_multiplicity"}, "gap row")
        n = row["N"]
        if n == 2:
            need(row["kappa"] == row["induction_factor"] == "not_applicable", "N2 induction")
        else:
            kappa = Fraction(3, n * n - 1)
            factor = 1 - kappa
            product *= factor
            need(fr(row["kappa"]) == kappa and fr(row["induction_factor"]) == factor, "gap factor")
        gap = Fraction(n + 2, 2 * (n - 1))
        need(fr(row["telescoped_product"]) == product, "product")
        need(fr(row["gap_L"]) == gap and fr(row["quartic_Q_eigenvalue"]) == 1 - gap / n, "gap/eigen")
        need(fr(row["quartic_center"]) == Fraction(3 * n * n, n + 2), "center")
        need(row["slow_multiplicity"] == ("all mean-zero modes" if n == 2 else "one"), "multiplicity")
        checks += 6

    form_rows = data["polynomial_form_rows"]
    need(type(form_rows) is list and len(form_rows) == 6 and [row["N"] for row in form_rows] == list(range(2, 8)), "form coordinates")
    total_vectors = total_cells = 0
    for row in form_rows:
        exact_keys(row, {"N", "basis", "gram_upper", "q_form_upper", "self_adjoint_cells", "constant_column_pass"}, "form row")
        n = row["N"]
        basis = expected_basis(n)
        need(row["basis"] == [list(item) for item in basis], "basis")
        actions = [apply_q(item) for item in basis]
        coordinates = [(i, j) for i in range(len(basis)) for j in range(i, len(basis))]
        need(len(row["gram_upper"]) == len(coordinates) and len(row["q_form_upper"]) == len(coordinates), "form cell count")
        need([(cell["i"], cell["j"]) for cell in row["gram_upper"]] == coordinates, "Gram coordinates")
        need([(cell["i"], cell["j"]) for cell in row["q_form_upper"]] == coordinates, "Q coordinates")
        for kind in ("gram_upper", "q_form_upper"):
            for cell in row[kind]:
                exact_keys(cell, {"i", "j", "value"}, f"{kind} cell")
        for (i, j), gram_cell, q_cell in zip(coordinates, row["gram_upper"], row["q_form_upper"]):
            gram = spherical(tuple(a + b for a, b in zip(basis[i], basis[j])))
            qvalue = bracket(basis[i], actions[j])
            need(fr(gram_cell["value"]) == gram, "Gram value")
            need(fr(q_cell["value"]) == qvalue, "Q value")
            need(qvalue == bracket(basis[j], actions[i]), "self-adjoint")
            checks += 3
        need(row["self_adjoint_cells"] == len(coordinates) and row["constant_column_pass"] is True, "form metadata")
        total_vectors += len(basis)
        total_cells += 2 * len(coordinates)
        checks += 2

    enumeration = data["enumeration"]
    exact_keys(enumeration, {"conditional_rows", "gap_rows", "form_rows", "basis_vectors", "upper_form_cells",
                             "audited_leaf_count"}, "enumeration")
    need(enumeration["conditional_rows"] == 10 and enumeration["gap_rows"] == 11 and enumeration["form_rows"] == 6, "enum rows")
    need(enumeration["basis_vectors"] == total_vectors and enumeration["upper_form_cells"] == total_cells, "enum cells")
    need(data["references"] == [
        {"identifier": "UC_BERKELEY_RECORD_112857", "role": "Kac collision model and kinetic-theory lineage"},
        {"identifier": "10.1007/BF02392695", "role": "exact spectral-gap and geometric-induction source"},
        {"identifier": "arXiv:math-ph/0109003", "role": "accessible primary preprint"}], "references")
    checks += 6
    print(f"C322 independent checker: PASS ({checks} checks, {total_cells} exact form cells)")


if __name__ == "__main__":
    main()
