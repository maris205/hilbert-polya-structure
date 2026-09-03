#!/usr/bin/env python3
"""Producer-independent strict exact checker for HCS-C336."""
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
EVIDENCE = ROOT / "results/c336_crow_kimura_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C336/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVALUATION_RAW_SHA256 = "0c48ad05b07c835172f55442d812a1492ca9ef5e320b817916246d62b16d5f56"
EVALUATION_SEMANTIC_SHA256 = "43b56588a42292014f578318aa99d7ab6db99fcdac162e7669f73a1598a73ae3"
FIXTURES = [
    (Fraction(1), Fraction(1)),
    (Fraction(3, 2), Fraction(5, 3)),
    (Fraction(2, 3), Fraction(7, 4)),
]
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
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority_sha256", "evaluation", "model", "theorem",
    "spectral_rows", "walsh_rows", "flow_rows", "boundary_rows", "counts", "references",
    "collisions", "nonclaims", "route_tuple", "overall_verdict", "scope_flags",
    "payload_sha256",
}
ROW_KEYS = {
    "L", "U", "s", "dimension", "poles", "weights", "retained",
    "retained_multiplicity_total", "secular_coefficients_ascending",
    "full_characteristic_coefficients_ascending", "full_degree", "trace",
    "interlacing_intervals", "root_count", "no_root_below",
}
REFERENCES = [
    {"identifier": "10.1017/S0016672301005110", "role": "continuous-time symmetric mutation-selection source owner"},
    {"identifier": "arXiv:1306.0111", "role": "permutation-invariant Crow-Kimura linear-algebra owner"},
    {"identifier": "arXiv:1408.4417", "role": "Crow-Kimura equilibrium and single-peak context"},
]
COLLISIONS = {
    "C171": "mutation-only Ehrenfest hypercube without selection spike",
    "C200": "Wright-Fisher diffusion rather than finite sequence-space flow",
    "C253": "finite-population Moran fixation rather than deterministic quasispecies",
    "C271": "network SIS threshold rather than mutation-selection rank-one spectrum",
}
NONCLAIMS = [
    "No singular infinite-genome error-threshold theorem is claimed from finite-L analyticity.",
    "The secular and characteristic polynomials are source linear algebra, not target Euler factors or divisors.",
    "No target arithmetic data, root number, automorphy, target zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
MODEL = {
    "phase_space": "probability simplex on {0,1}^L",
    "mutation": "M_L=(U/L) sum_i(F_i-I)",
    "selection": "s times the projector onto the all-zero genotype",
    "normalization": "subtract s*p_0*p",
    "parameter_domain": "L>=1 integer and U,s>0; zero faces separated",
}
THEOREM = {
    "projectivization": "p(t)=exp(tA)p(0)/(1^T exp(tA)p(0))",
    "retained": "d_k=-2Uk/L with multiplicity binom(L,k)-1",
    "secular": "1=(s/2^L) sum_k binom(L,k)/(lambda+2Uk/L)",
    "interlacing": "one simple root above zero and one in each adjacent mutation gap",
    "gap": "top secular root minus second secular root is the exact generic projective exponent",
    "boundaries": "s=0, U=0, and L=1 are explicit; no finite-L singular error threshold claim",
}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
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


def duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    value = json.loads(
        path.read_text(), object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
    if type(value) is not dict:
        raise TypeError("JSON root must be object")
    return value


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be object")
    return value


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def semantic_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def q(value) -> Fraction:
    if type(value) is not str:
        raise TypeError("rational encoding must be string")
    return Fraction(value)


def convolve(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i in range(len(result)):
        result[i] = sum(
            a[j] * b[i - j]
            for j in range(max(0, i - len(b) + 1), min(len(a) - 1, i) + 1)
        )
    return result


def add_polys(a, b):
    return [
        (a[i] if i < len(a) else Fraction(0)) +
        (b[i] if i < len(b) else Fraction(0))
        for i in range(max(len(a), len(b)))
    ]


def factor_product(poles, omit=None):
    answer = [Fraction(1)]
    for index, value in enumerate(poles):
        if index != omit:
            answer = convolve(answer, [-value, Fraction(1)])
    return answer


def power_factor(pole, exponent):
    answer = [Fraction(1)]
    for _ in range(exponent):
        answer = convolve(answer, [-pole, Fraction(1)])
    return answer


def mutation_image(length, mutation, vector):
    result = []
    for x in range(2**length):
        neighbor_sum = sum(vector[x ^ (1 << bit)] for bit in range(length))
        result.append(mutation * (neighbor_sum / length - vector[x]))
    return result


def operator_image(length, mutation, selection, vector):
    result = mutation_image(length, mutation, vector)
    result[0] += selection * vector[0]
    return result


def expected_spectral(length, mutation, selection):
    poles = [Fraction(-2 * mutation * k, length) for k in range(length + 1)]
    weights = [Fraction(math.comb(length, k), 2**length) for k in range(length + 1)]
    secular = factor_product(poles)
    for k, weight in enumerate(weights):
        term = [-selection * weight * coefficient for coefficient in factor_product(poles, k)]
        secular = add_polys(secular, term)
    retained = [{
        "k": k,
        "eigenvalue": str(poles[k].numerator) if poles[k].denominator == 1 else f"{poles[k].numerator}/{poles[k].denominator}",
        "multiplicity": math.comb(length, k) - 1,
    } for k in range(length + 1)]
    full = None
    if length <= 6:
        extra = [Fraction(1)]
        for k, pole in enumerate(poles):
            extra = convolve(extra, power_factor(pole, math.comb(length, k) - 1))
        full = convolve(secular, extra)
    return poles, weights, secular, retained, full


def formatted(values):
    return [str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}" for v in values]


def need(condition: bool, message: str, counter: list[int]):
    counter[0] += 1
    if not condition:
        raise AssertionError(message)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C336 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    count = [0]

    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    need(set(data) == TOP_KEYS, "evidence top-level field lock", count)
    need(data["schema"] == "hcs-c336-crow-kimura-evidence-v1", "schema", count)
    need(data["candidate_id"] == "HCS-C336", "candidate", count)
    need(data["obstruction_id"] == "HEN-O320", "obstruction", count)
    need(data["source_commit"] == SOURCE, "source", count)
    need(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH, "epoch", count)
    need(data["scope_literal"] == SCOPE, "scope", count)
    need(data["evaluator_authority_sha256"] == EVALUATOR, "evaluator", count)
    need(payload_hash(data) == data["payload_sha256"], "payload hash", count)

    raw_yaml = args.evaluation.read_bytes()
    need(sha(raw_yaml) == EVALUATION_RAW_SHA256, "YAML raw hash", count)
    need(semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA256, "YAML semantic hash", count)
    need(data["evaluation"] == {
        "path": "evaluations/route_a/HCS-C336/2026-09-03.yaml",
        "raw_sha256": EVALUATION_RAW_SHA256,
        "semantic_sha256": EVALUATION_SEMANTIC_SHA256,
    }, "evidence evaluation lock", count)
    need(evaluation["candidate_id"] == "HCS-C336" and evaluation["obstruction_id"] == "HEN-O320", "YAML IDs", count)
    need(evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == EPOCH, "YAML baseline", count)
    need(evaluation["scope_literal"] == SCOPE, "YAML scope", count)
    need(evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML authority", count)
    need(evaluation["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "YAML tuple", count)
    need(evaluation["scope_flags"] == FLAGS, "YAML flags", count)
    need(evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict", count)
    need(evaluation["route_b_invocation_allowed"] is False, "YAML Route B", count)
    need(type(evaluation["evaluation_date"]) is str, "YAML date type", count)
    for gate, verdict, status in [
        ("a0", "A0_FAIL", "PROVED"), ("a1", "A1_FAIL", "PROVED"),
        ("a2", "A2_FAIL", "STOP_SCOPED"), ("a3", "A3_FAIL", "STOP_SCOPED"),
        ("a4", "A4_FORMAL_HINT", "PROVED"),
    ]:
        need(evaluation[gate]["verdict"] == verdict, f"YAML {gate} verdict", count)
        need(evaluation[gate]["evidence_status"] == status, f"YAML {gate} status", count)

    rows = data["spectral_rows"]
    need(type(rows) is list and len(rows) == 30, "spectral row count", count)
    cursor = 0
    stored_cells = 0
    secular_cells = 0
    retained_cells = 0
    for length in range(1, 11):
        for mutation, selection in FIXTURES:
            row = rows[cursor]
            cursor += 1
            need(type(row) is dict and set(row) == ROW_KEYS, "spectral row fields", count)
            need((row["L"], q(row["U"]), q(row["s"])) == (length, mutation, selection), "fixture order", count)
            poles, weights, secular, retained, full = expected_spectral(length, mutation, selection)
            need(row["dimension"] == 2**length and row["full_degree"] == 2**length, "dimension", count)
            need(row["poles"] == formatted(poles), "poles", count)
            need(row["weights"] == formatted(weights) and sum(q(x) for x in row["weights"]) == 1, "weights", count)
            need(row["retained"] == retained, "retained ledger", count)
            total = sum(item["multiplicity"] for item in retained)
            need(row["retained_multiplicity_total"] == total == 2**length-(length+1), "multiplicity total", count)
            need(row["secular_coefficients_ascending"] == formatted(secular), "secular polynomial", count)
            need(q(row["secular_coefficients_ascending"][-1]) == 1, "secular monic", count)
            expected_full = None if full is None else formatted(full)
            need(row["full_characteristic_coefficients_ascending"] == expected_full, "full factor", count)
            need(q(row["trace"]) == selection-mutation*2**length, "trace", count)
            need(row["root_count"] == length+1 and q(row["no_root_below"]) == poles[-1], "root ledger", count)
            intervals = [{"root_index": 0, "left": "0", "right": "+infinity"}]
            intervals += [{"root_index": k, "left": formatted([poles[k]])[0], "right": formatted([poles[k-1]])[0]} for k in range(1, length+1)]
            need(row["interlacing_intervals"] == intervals, "interlacing interval ledger", count)
            secular_cells += len(secular)
            stored_cells += len(full or [])
            retained_cells += len(retained)

    walsh = data["walsh_rows"]
    walsh_cursor = 0
    mutation, selection = FIXTURES[1]
    for length in range(2, 9):
        for weight in range(1, length):
            if math.comb(length, weight) < 2:
                continue
            row = walsh[walsh_cursor]
            walsh_cursor += 1
            first = (1 << weight)-1
            second = first ^ 1 ^ (1 << weight)
            vector = []
            for x in range(2**length):
                one = -1 if (x & first).bit_count() & 1 else 1
                two = -1 if (x & second).bit_count() & 1 else 1
                vector.append(Fraction(one-two))
            eigenvalue = Fraction(-2*mutation*weight, length)
            image = operator_image(length, mutation, selection, vector)
            residual = sum(abs(image[i]-eigenvalue*vector[i]) for i in range(2**length))
            need(row["L"] == length and row["k"] == weight, "Walsh indices", count)
            need(row["walsh_masks"] == [first, second], "Walsh masks", count)
            need(q(row["U"]) == mutation and q(row["s"]) == selection, "Walsh fixture", count)
            need(q(row["eigenvalue"]) == eigenvalue, "Walsh eigenvalue", count)
            need(row["support_size"] == sum(v != 0 for v in vector), "Walsh support", count)
            need(q(row["selection_coordinate"]) == 0 and q(row["residual_l1"]) == residual == 0, "Walsh residual", count)
    need(walsh_cursor == len(walsh), "Walsh row count", count)

    flow = data["flow_rows"]
    need(len(flow) == 7, "flow row count", count)
    flow_cells = 0
    for length, row in enumerate(flow, 1):
        mutation, selection = FIXTURES[(length-1) % 3]
        probability = [Fraction(x+1) for x in range(2**length)]
        total = sum(probability)
        probability = [v/total for v in probability]
        linear = operator_image(length, mutation, selection, probability)
        mean = sum(linear)
        derivative = [linear[i]-mean*probability[i] for i in range(2**length)]
        need((row["L"], q(row["U"]), q(row["s"])) == (length, mutation, selection), "flow fixture", count)
        need([q(v) for v in row["initial"]] == probability, "flow initial", count)
        need(q(row["mean_fitness"]) == mean == selection*probability[0], "flow mean", count)
        need([q(v) for v in row["quotient_derivative"]] == derivative, "quotient derivative", count)
        need([q(v) for v in row["nonlinear_derivative"]] == derivative, "nonlinear derivative", count)
        need(q(row["derivative_mass"]) == sum(derivative) == 0, "flow tangent", count)
        flow_cells += len(probability)

    boundaries = []
    for length in range(1, 9):
        multiplicities = [math.comb(length, k) for k in range(length+1)]
        boundaries.append({"boundary": "s=0", "L": length, "eigenvalue_multiplicities": multiplicities, "multiplicity_total": 2**length, "stationary_law": "uniform"})
    boundaries += [
        {"boundary": "U=0", "master_mass_positive": False, "conclusion": "master_free_face_stationary", "scalar_equation": "a'=s*a*(1-a)"},
        {"boundary": "U=0", "master_mass_positive": True, "conclusion": "converges_to_master", "scalar_equation": "a'=s*a*(1-a)"},
        {"boundary": "L=1", "characteristic_polynomial": "lambda^2-(s-2U)lambda-sU", "eigenvalues": "(s-2U +/- sqrt(s^2+4U^2))/2", "retained_multiplicity_total": 0},
    ]
    need(data["boundary_rows"] == boundaries, "boundary ledger", count)

    expected_counts = {
        "spectral_rows": 30,
        "secular_coefficient_cells": secular_cells,
        "stored_full_coefficient_cells": stored_cells,
        "retained_cells": retained_cells,
        "walsh_rows": len(walsh),
        "flow_rows": 7,
        "flow_coordinate_cells": flow_cells,
        "boundary_rows": len(boundaries),
    }
    need(data["counts"] == expected_counts, "count ledger", count)
    need(data["references"] == REFERENCES, "reference lock", count)
    need(data["collisions"] == COLLISIONS, "collision lock", count)
    need(data["nonclaims"] == NONCLAIMS, "nonclaim lock", count)
    need(data["route_tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple", count)
    need(data["overall_verdict"] == "ROUTE_A_REJECTED", "overall verdict", count)
    need(data["scope_flags"] == FLAGS, "scope flags", count)
    need(data["model"] == MODEL, "model lock", count)
    need(data["theorem"] == THEOREM, "theorem lock", count)
    print(f"C336 independent Crow-Kimura checker: PASS assertions={count[0]}")


if __name__ == "__main__":
    main()
