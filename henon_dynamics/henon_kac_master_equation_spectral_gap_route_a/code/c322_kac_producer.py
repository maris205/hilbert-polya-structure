#!/usr/bin/env python3
"""Deterministic exact polynomial evidence producer for HCS-C322."""
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
OUTPUT = ROOT / "results/c322_kac_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C322/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVALUATION_RAW = "d0f97756644e925ab6c59efeca4f4e4665838405742758c3d602398893b15a72"
EVALUATION_SEMANTIC = "8d127621e319cf76ed9b1cf126b260ca066b49f4448653cf8a60634572b74c2e"
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
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root must be a mapping")
    return value


def fs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def odd_double_factorial(order: int) -> int:
    answer = 1
    for value in range(1, order + 1, 2):
        answer *= value
    return answer


def sphere_moment(exponents: tuple[int, ...]) -> Fraction:
    if any(exponent % 2 for exponent in exponents):
        return Fraction(0)
    n = len(exponents)
    half = [exponent // 2 for exponent in exponents]
    total = sum(half)
    numerator = n ** total
    for power in half:
        numerator *= odd_double_factorial(2 * power - 1)
    denominator = 1
    for offset in range(total):
        denominator *= n + 2 * offset
    return Fraction(numerator, denominator) if total else Fraction(1)


def trig_average(cosine_power: int, sine_power: int) -> Fraction:
    if cosine_power % 2 or sine_power % 2:
        return Fraction(0)
    a, b = cosine_power // 2, sine_power // 2
    return Fraction(math.factorial(2 * a) * math.factorial(2 * b),
                    4 ** (a + b) * math.factorial(a) * math.factorial(b) * math.factorial(a + b))


def pair_action(a: int, b: int) -> dict[tuple[int, int], Fraction]:
    """Uniform-angle action on u^a v^b, independently expanded."""
    result: dict[tuple[int, int], Fraction] = {}
    for x in range(a + 1):
        for y in range(b + 1):
            cosine = a - x + b - y
            sine = x + y
            average = trig_average(cosine, sine)
            if not average:
                continue
            coefficient = Fraction(math.comb(a, x) * math.comb(b, y) * ((-1) ** y)) * average
            powers = (a - x + y, x + b - y)
            result[powers] = result.get(powers, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def q_action(exponents: tuple[int, ...]) -> dict[tuple[int, ...], Fraction]:
    n = len(exponents)
    pairs = math.comb(n, 2)
    result: dict[tuple[int, ...], Fraction] = {}
    for i in range(n):
        for j in range(i + 1, n):
            for (pi, pj), coefficient in pair_action(exponents[i], exponents[j]).items():
                target = list(exponents)
                target[i], target[j] = pi, pj
                key = tuple(target)
                result[key] = result.get(key, Fraction(0)) + coefficient / pairs
    return {key: value for key, value in result.items() if value}


def inner(left: tuple[int, ...], polynomial: dict[tuple[int, ...], Fraction]) -> Fraction:
    return sum((coefficient * sphere_moment(tuple(a + b for a, b in zip(left, right)))
                for right, coefficient in polynomial.items()), Fraction(0))


def basis(n: int) -> list[tuple[int, ...]]:
    width = min(n, 3)
    raw = [powers for powers in itertools.product(range(5), repeat=width) if sum(powers) <= 4]
    raw.sort(key=lambda powers: (sum(powers), powers))
    return [tuple(2 * power for power in powers) + (0,) * (n - width) for powers in raw]


def form_row(n: int) -> dict:
    vectors = basis(n)
    actions = [q_action(vector) for vector in vectors]
    gram, qform = [], []
    for i, left in enumerate(vectors):
        for j in range(i, len(vectors)):
            gram_value = sphere_moment(tuple(a + b for a, b in zip(left, vectors[j])))
            q_value = inner(left, actions[j])
            reverse = inner(vectors[j], actions[i])
            assert q_value == reverse
            gram.append({"i": i, "j": j, "value": fs(gram_value)})
            qform.append({"i": i, "j": j, "value": fs(q_value)})
    constant = vectors.index((0,) * n)
    for i, left in enumerate(vectors):
        assert inner(left, actions[constant]) == sphere_moment(left)
    return {"N": n, "basis": [list(vector) for vector in vectors],
            "gram_upper": gram, "q_form_upper": qform,
            "self_adjoint_cells": len(qform), "constant_column_pass": True}


def conditional_rows() -> list[dict]:
    rows = []
    for n in range(3, 13):
        cells = []
        for r in range(5):
            denominator = 1
            for offset in range(r):
                denominator *= n - 1 + 2 * offset
            c = Fraction(odd_double_factorial(2 * r - 1), denominator) if r else Fraction(1)
            coefficients = [c * math.comb(r, j) * n ** (r - j) * ((-1) ** j)
                            for j in range(r + 1)]
            alpha = coefficients[-1]
            cells.append({"even_degree": 2 * r, "monomial_image_coefficients_x2_ascending": [fs(x) for x in coefficients],
                          "eigenvalue": fs(alpha)})
        kappa = Fraction(3, n * n - 1)
        beta = Fraction(1, (n - 1) ** 2)
        mu = Fraction(n + 4, n * (n + 1))
        rows.append({"N": n, "cells": cells, "kappa": fs(kappa), "beta": fs(beta),
                     "mu": fs(mu), "top_mode": "unique degree-four coordinate polynomial sum"})
    return rows


def gap_rows() -> list[dict]:
    rows = []
    product = Fraction(1)
    for n in range(2, 13):
        if n == 2:
            kappa = "not_applicable"
            induction = "not_applicable"
            product = Fraction(1)
        else:
            kap = Fraction(3, n * n - 1)
            factor = 1 - kap
            product *= factor
            kappa = fs(kap)
            induction = fs(factor)
        gap = Fraction(n + 2, 2 * (n - 1))
        q_eigen = 1 - gap / n
        center = Fraction(3 * n * n, n + 2)
        expected_product = Fraction(n + 2, 4 * (n - 1)) if n >= 3 else Fraction(1)
        assert product == expected_product
        rows.append({"N": n, "kappa": kappa, "induction_factor": induction,
                     "telescoped_product": fs(product), "gap_L": fs(gap),
                     "quartic_Q_eigenvalue": fs(q_eigen), "quartic_center": fs(center),
                     "slow_multiplicity": "all mean-zero modes" if n == 2 else "one"})
    return rows


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C322 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    evaluation = strict_yaml(EVALUATION)
    raw = hashlib.sha256(EVALUATION.read_bytes()).hexdigest()
    semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False).encode()).hexdigest()
    if raw != EVALUATION_RAW or semantic != EVALUATION_SEMANTIC:
        raise AssertionError("frozen evaluation changed")
    forms = [form_row(n) for n in range(2, 8)]
    data = {
        "schema": "hcs-c322-kac-spectral-gap-v1",
        "candidate_id": "HCS-C322", "obstruction_id": "HEN-O306",
        "evaluation_date": "2026-09-03", "fixed_epoch": EPOCH,
        "source_commit": SOURCE, "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR,
                      "authority": "flow_systems/skills/route-a-evaluator.md"},
        "model": {
            "state_space": "S^{N-1}(sqrt(N)) with normalized surface measure",
            "pair_sampling": "uniform over unordered pairs i<j",
            "angle_measure": "dtheta/(2pi) on [-pi,pi]",
            "positive_generator": "L_N=N(I-Q_N)",
            "semigroup": "G_t=exp(-t L_N)",
            "positive_energy_scaling": "all E>0 are unitarily conjugate",
            "zero_energy_boundary": "E=0 is one point with zero mean-zero sector",
        },
        "theorem_contract": {
            "gap": "Delta_N=(N+2)/(2(N-1)) for N>=2 under L_N=N(I-Q_N)",
            "slow_mode": "sum_i v_i^4-3N^2/(N+2)",
            "multiplicity": "one for N>=3; every mean-zero mode at N=2",
        "lower_bound": "full conditional-projection induction with kappa_N=3/(N^2-1)",
        "projection_transfer": "P=TT*/N; nonzero spectrum transfers to T*T/N with trivial and standard index branches",
            "decay": "sharp mean-zero L2 norm bound exp(-Delta_N t)",
            "evidence_boundary": "finite polynomial matrices audit algebra and do not prove the infinite-dimensional gap",
        },
        "finite_grid": {"conditional_N_min": 3, "conditional_N_max": 12,
                        "form_N_min": 2, "form_N_max": 7, "ordinary_degree_max": 8,
                        "basis_support_max": 3},
        "conditional_operator_rows": conditional_rows(),
        "gap_rows": gap_rows(),
        "polynomial_form_rows": forms,
        "quartic_ambient_action": {
            "coefficient_sum_v4": "1-(N+2)/(2N(N-1))",
            "coefficient_sum_v2_squared": "3/(2N(N-1))",
            "sphere_relation": "sum_i v_i^2=N",
        },
        "route_a_yaml": {"relative_path": str(EVALUATION.relative_to(ROOT)),
                         "raw_sha256": raw, "semantic_sha256": semantic},
        "collision_boundary": {
            "C170": "the Kac ring is a deterministic scatterer toy model; C322 is a continuous-sphere random binary-collision master equation",
            "C183": "random transpositions act on a finite permutation group; Kac collisions average continuous coordinate-plane rotations",
            "C313": "sphere geodesics are deterministic variational curves; Kac dynamics is a stochastic projection average on functions",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "Finite polynomial forms are not a proof of the infinite-dimensional spectral lower bound.",
            "No full spectrum, entropy production, nonlinear Boltzmann convergence, or nonuniform-angle theorem is asserted.",
            "No uniqueness claim is made for the N=2 slow eigenspace and no positive gap is assigned at E=0.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
            "No literature-priority claim is made.",
        ],
        "references": [
            {"identifier": "UC_BERKELEY_RECORD_112857", "role": "Kac collision model and kinetic-theory lineage"},
            {"identifier": "10.1007/BF02392695", "role": "exact spectral-gap and geometric-induction source"},
            {"identifier": "arXiv:math-ph/0109003", "role": "accessible primary preprint"},
        ],
    }
    data["enumeration"] = {
        "conditional_rows": len(data["conditional_operator_rows"]),
        "gap_rows": len(data["gap_rows"]),
        "form_rows": len(forms),
        "basis_vectors": sum(len(row["basis"]) for row in forms),
        "upper_form_cells": sum(len(row["gram_upper"]) + len(row["q_form_upper"]) for row in forms),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C322_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
