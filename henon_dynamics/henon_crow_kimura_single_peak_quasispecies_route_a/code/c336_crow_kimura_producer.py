#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C336."""
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
OUTPUT = ROOT / "results/c336_crow_kimura_evidence.json"
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


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def qlist(values) -> list[str]:
    return [qstr(value) for value in values]


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def poly_scale(c: Fraction, a: list[Fraction]) -> list[Fraction]:
    return [c * value for value in a]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            result[i + j] += u * v
    return result


def poly_pow(a: list[Fraction], exponent: int) -> list[Fraction]:
    result = [Fraction(1)]
    base = list(a)
    while exponent:
        if exponent & 1:
            result = poly_mul(result, base)
        base = poly_mul(base, base)
        exponent //= 2
    return result


def product_without(poles: list[Fraction], skipped: int | None = None) -> list[Fraction]:
    result = [Fraction(1)]
    for index, pole in enumerate(poles):
        if index != skipped:
            result = poly_mul(result, [-pole, Fraction(1)])
    return result


def spectral_data(length: int, mutation: Fraction, selection: Fraction):
    poles = [Fraction(-2 * mutation * k, length) for k in range(length + 1)]
    weights = [Fraction(math.comb(length, k), 2**length) for k in range(length + 1)]
    secular = product_without(poles)
    correction = [Fraction(0)] * len(secular)
    for k, weight in enumerate(weights):
        correction = poly_add(correction, poly_scale(selection * weight, product_without(poles, k)))
    secular = poly_add(secular, poly_scale(Fraction(-1), correction))
    retained = []
    retained_factor = [Fraction(1)]
    for k, pole in enumerate(poles):
        multiplicity = math.comb(length, k) - 1
        retained.append({
            "k": k,
            "eigenvalue": qstr(pole),
            "multiplicity": multiplicity,
        })
        if length <= 6:
            retained_factor = poly_mul(retained_factor, poly_pow([-pole, Fraction(1)], multiplicity))
    full = poly_mul(secular, retained_factor) if length <= 6 else None
    intervals = [{
        "root_index": 0,
        "left": "0",
        "right": "+infinity",
    }]
    for k in range(1, length + 1):
        intervals.append({
            "root_index": k,
            "left": qstr(poles[k]),
            "right": qstr(poles[k - 1]),
        })
    return poles, weights, secular, retained, full, intervals


def mutation_apply(length: int, mutation: Fraction, vector: list[Fraction]) -> list[Fraction]:
    dimension = 2**length
    result = [-mutation * vector[x] for x in range(dimension)]
    rate = mutation / length
    for x in range(dimension):
        for bit in range(length):
            result[x] += rate * vector[x ^ (1 << bit)]
    return result


def operator_apply(length: int, mutation: Fraction, selection: Fraction,
                   vector: list[Fraction]) -> list[Fraction]:
    result = mutation_apply(length, mutation, vector)
    result[0] += selection * vector[0]
    return result


def walsh_difference(length: int, weight: int):
    first = (1 << weight) - 1
    second = first ^ 1 ^ (1 << weight)
    vector = []
    for x in range(2**length):
        a = -1 if (x & first).bit_count() & 1 else 1
        b = -1 if (x & second).bit_count() & 1 else 1
        vector.append(Fraction(a - b))
    return first, second, vector


def spectral_rows():
    rows = []
    for length in range(1, 11):
        for mutation, selection in FIXTURES:
            poles, weights, secular, retained, full, intervals = spectral_data(length, mutation, selection)
            dimension = 2**length
            rows.append({
                "L": length,
                "U": qstr(mutation),
                "s": qstr(selection),
                "dimension": dimension,
                "poles": qlist(poles),
                "weights": qlist(weights),
                "retained": retained,
                "retained_multiplicity_total": sum(row["multiplicity"] for row in retained),
                "secular_coefficients_ascending": qlist(secular),
                "full_characteristic_coefficients_ascending": qlist(full) if full is not None else None,
                "full_degree": dimension,
                "trace": qstr(selection - mutation * dimension),
                "interlacing_intervals": intervals,
                "root_count": length + 1,
                "no_root_below": qstr(poles[-1]),
            })
    return rows


def walsh_rows():
    rows = []
    mutation, selection = FIXTURES[1]
    for length in range(2, 9):
        for weight in range(1, length):
            if math.comb(length, weight) < 2:
                continue
            first, second, vector = walsh_difference(length, weight)
            image = operator_apply(length, mutation, selection, vector)
            eigenvalue = Fraction(-2 * mutation * weight, length)
            residual = [image[i] - eigenvalue * vector[i] for i in range(2**length)]
            rows.append({
                "L": length,
                "k": weight,
                "U": qstr(mutation),
                "s": qstr(selection),
                "walsh_masks": [first, second],
                "eigenvalue": qstr(eigenvalue),
                "support_size": sum(value != 0 for value in vector),
                "selection_coordinate": qstr(vector[0]),
                "residual_l1": qstr(sum(abs(value) for value in residual)),
            })
    return rows


def flow_rows():
    rows = []
    for length in range(1, 8):
        mutation, selection = FIXTURES[(length - 1) % len(FIXTURES)]
        dimension = 2**length
        raw = [Fraction(x + 1) for x in range(dimension)]
        total = sum(raw)
        probability = [value / total for value in raw]
        linear = operator_apply(length, mutation, selection, probability)
        mean_fitness = sum(linear)
        quotient_derivative = [value - mean_fitness * probability[i] for i, value in enumerate(linear)]
        nonlinear = [linear[i] - selection * probability[0] * probability[i] for i in range(dimension)]
        rows.append({
            "L": length,
            "U": qstr(mutation),
            "s": qstr(selection),
            "initial": qlist(probability),
            "mean_fitness": qstr(mean_fitness),
            "quotient_derivative": qlist(quotient_derivative),
            "nonlinear_derivative": qlist(nonlinear),
            "derivative_mass": qstr(sum(nonlinear)),
        })
    return rows


def boundary_rows():
    rows = []
    for length in range(1, 9):
        multiplicities = [math.comb(length, k) for k in range(length + 1)]
        rows.append({
            "boundary": "s=0",
            "L": length,
            "eigenvalue_multiplicities": multiplicities,
            "multiplicity_total": sum(multiplicities),
            "stationary_law": "uniform",
        })
    for master_present in (False, True):
        rows.append({
            "boundary": "U=0",
            "master_mass_positive": master_present,
            "conclusion": "converges_to_master" if master_present else "master_free_face_stationary",
            "scalar_equation": "a'=s*a*(1-a)",
        })
    rows.append({
        "boundary": "L=1",
        "characteristic_polynomial": "lambda^2-(s-2U)lambda-sU",
        "eigenvalues": "(s-2U +/- sqrt(s^2+4U^2))/2",
        "retained_multiplicity_total": 0,
    })
    return rows


def build_evidence():
    spectral = spectral_rows()
    walsh = walsh_rows()
    flow = flow_rows()
    boundaries = boundary_rows()
    evaluation_raw = EVALUATION.read_bytes()
    evaluation_value = yaml.safe_load(evaluation_raw)
    data = {
        "schema": "hcs-c336-crow-kimura-evidence-v1",
        "candidate_id": "HCS-C336",
        "obstruction_id": "HEN-O320",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "evaluation": {
            "path": "evaluations/route_a/HCS-C336/2026-09-03.yaml",
            "raw_sha256": sha(evaluation_raw),
            "semantic_sha256": sha(json.dumps(evaluation_value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()),
        },
        "model": {
            "phase_space": "probability simplex on {0,1}^L",
            "mutation": "M_L=(U/L) sum_i(F_i-I)",
            "selection": "s times the projector onto the all-zero genotype",
            "normalization": "subtract s*p_0*p",
            "parameter_domain": "L>=1 integer and U,s>0; zero faces separated",
        },
        "theorem": {
            "projectivization": "p(t)=exp(tA)p(0)/(1^T exp(tA)p(0))",
            "retained": "d_k=-2Uk/L with multiplicity binom(L,k)-1",
            "secular": "1=(s/2^L) sum_k binom(L,k)/(lambda+2Uk/L)",
            "interlacing": "one simple root above zero and one in each adjacent mutation gap",
            "gap": "top secular root minus second secular root is the exact generic projective exponent",
            "boundaries": "s=0, U=0, and L=1 are explicit; no finite-L singular error threshold claim",
        },
        "spectral_rows": spectral,
        "walsh_rows": walsh,
        "flow_rows": flow,
        "boundary_rows": boundaries,
        "counts": {
            "spectral_rows": len(spectral),
            "secular_coefficient_cells": sum(len(row["secular_coefficients_ascending"]) for row in spectral),
            "stored_full_coefficient_cells": sum(len(row["full_characteristic_coefficients_ascending"] or []) for row in spectral),
            "retained_cells": sum(len(row["retained"]) for row in spectral),
            "walsh_rows": len(walsh),
            "flow_rows": len(flow),
            "flow_coordinate_cells": sum(len(row["initial"]) for row in flow),
            "boundary_rows": len(boundaries),
        },
        "references": [
            {"identifier": "10.1017/S0016672301005110", "role": "continuous-time symmetric mutation-selection source owner"},
            {"identifier": "arXiv:1306.0111", "role": "permutation-invariant Crow-Kimura linear-algebra owner"},
            {"identifier": "arXiv:1408.4417", "role": "Crow-Kimura equilibrium and single-peak context"},
        ],
        "collisions": {
            "C171": "mutation-only Ehrenfest hypercube without selection spike",
            "C200": "Wright-Fisher diffusion rather than finite sequence-space flow",
            "C253": "finite-population Moran fixation rather than deterministic quasispecies",
            "C271": "network SIS threshold rather than mutation-selection rank-one spectrum",
        },
        "nonclaims": [
            "No singular infinite-genome error-threshold theorem is claimed from finite-L analyticity.",
            "The secular and characteristic polynomials are source linear algebra, not target Euler factors or divisors.",
            "No target arithmetic data, root number, automorphy, target zero match, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
        "route_tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall_verdict": "ROUTE_A_REJECTED",
        "scope_flags": FLAGS,
    }
    assert data["evaluation"]["raw_sha256"] == EVALUATION_RAW_SHA256
    assert data["evaluation"]["semantic_sha256"] == EVALUATION_SEMANTIC_SHA256
    data["payload_sha256"] = sha(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C336 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C336_PRODUCER_PASS rows={data['counts']['spectral_rows']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
