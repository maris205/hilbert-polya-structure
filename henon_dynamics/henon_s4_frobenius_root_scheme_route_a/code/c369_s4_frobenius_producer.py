#!/usr/bin/env python3
"""Canonical exact finite evidence for HCS-C369."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c369_s4_frobenius_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C369/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
RAW = "421a590612cbe66b3ba3dc7af6c8ee6bbca83a465343c9eb19b852e323d2cd13"
SEMANTIC = "36f2d0a42d65a3f1def14c18cf7fd5601c049c02477a7f4c5e89edae0369f731"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MAX_PRIME = 10000
MAX_ITERATE = 12
F = [-1, -1, 0, 0, 1]  # ascending coefficients of x^4-x-1
OWNERSHIP_BOUNDARY = {
    "inherited_workspace_owner": "HCS-C12A owns the universal zero-dimensional Frobenius finite-permutation fixed-point and finite zeta/determinant mechanism",
    "c369_owner": "x^4-x-1 S4 Galois proof, five-class all-good-prime factor/fixed/primitive/density atlas, p=283 non-etale boundary, and convention-locked executable ledger",
    "nonownership": "HCS-C369 does not claim workspace ownership of the universal finite-permutation zeta/determinant mechanism",
}
COLLISION_BOUNDARY = {
    "nearest_C12A": "C12A owns the universal zero-dimensional Frobenius finite-permutation fixed-point and finite zeta/determinant mechanism; C369 owns only the x^4-x-1 S4 all-good-prime factor/fixed/primitive/density atlas, p=283 boundary, and convention-locked executable ledger",
    "nearest_C19": "period-seven Henon ordered-edge curve with a two-axis chronology/Frobenius problem; C369 is the autonomous Frobenius permutation on a quartic zero-dimensional root scheme",
    "nearest_C41": "a cubic CM elliptic Frobenius bridge with cohomological degree-two factors; C369 classifies four-point permutation fibers and primitive cycles",
    "nearest_C56": "a degree-27 finite-etale Fano line scheme with W(E6) normal-closure action and selected Frobenius witnesses; C369 gives the all-good-prime S4 atlas for one quartic root scheme",
    "nearest_C172": "a primitive finite-field multiplier on field elements with a fixed point and a large cycle; C369 instead varies S4 root fibers over rational primes",
    "nearest_C364": "a finite Gauss reduction permutation without rational-prime fibers; C369 has an intrinsic integral root scheme and Chebotarev classes",
}
NONCLAIMS = [
    "no workspace ownership of the universal zero-dimensional finite-permutation zeta/determinant mechanism already owned by C12A",
    "no single autonomous dynamical owner across primes",
    "no cross-prime Fredholm direct sum or trace-class statement",
    "no target Euler product or target arithmetic local factors",
    "no target continuation, functional equation, divisor, or zero fit",
    "no Hilbert-Polya operator; fiber Koopman operators are finite-dimensional permutation unitaries",
    "no priority claim for the classical Dedekind or Chebotarev theorems",
]


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    k: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for k, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases are forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def trim(poly, p):
    out = [int(c) % p for c in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_sub(left, right, p):
    n = max(len(left), len(right))
    return trim([(left[i] if i < len(left) else 0) - (right[i] if i < len(right) else 0) for i in range(n)], p)


def poly_divmod(dividend, divisor, p):
    a = trim(dividend, p)
    b = trim(divisor, p)
    if b == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        coeff = a[-1] * inv % p
        q[shift] = coeff
        for j, value in enumerate(b):
            a[shift + j] = (a[shift + j] - coeff * value) % p
        a = trim(a, p)
    return trim(q, p), a


def poly_mod(poly, modulus, p):
    return poly_divmod(poly, modulus, p)[1]


def poly_mul_mod(left, right, modulus, p):
    raw = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            raw[i + j] = (raw[i + j] + a * b) % p
    return poly_mod(raw, modulus, p)


def poly_pow_mod(base, exponent, modulus, p):
    result = [1]
    power = poly_mod(base, modulus, p)
    n = exponent
    while n:
        if n & 1:
            result = poly_mul_mod(result, power, modulus, p)
        power = poly_mul_mod(power, power, modulus, p)
        n >>= 1
    return result


def poly_gcd(left, right, p):
    a, b = trim(left, p), trim(right, p)
    while b != [0]:
        _, remainder = poly_divmod(a, b, p)
        a, b = b, remainder
    inv = pow(a[-1], -1, p)
    return trim([inv * c for c in a], p)


def factor_degree_partition(p):
    modulus = trim(F, p)
    derivative = trim([-1, 0, 0, 4], p)
    if len(poly_gcd(modulus, derivative, p)) != 1:
        raise ValueError(f"ramified prime passed as good: {p}")
    xp = poly_pow_mod([0, 1], p, modulus, p)
    n1 = len(poly_gcd(modulus, poly_sub(xp, [0, 1], p), p)) - 1
    if n1 == 4:
        return (1, 1, 1, 1)
    if n1 == 2:
        return (1, 1, 2)
    if n1 == 1:
        return (1, 3)
    if n1 != 0:
        raise ArithmeticError(f"impossible degree-one count {n1} at p={p}")
    xp2 = poly_pow_mod(xp, p, modulus, p)
    n2 = len(poly_gcd(modulus, poly_sub(xp2, [0, 1], p), p)) - 1
    if n2 == 4:
        return (2, 2)
    if n2 == 0:
        return (4,)
    raise ArithmeticError(f"impossible degree-two count {n2} at p={p}")


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(limit**0.5) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (((limit - q * q) // q) + 1)
    return [q for q in range(2, limit + 1) if sieve[q]]


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    remaining = n
    prime_factors = 0
    q = 2
    while q * q <= remaining:
        if remaining % q == 0:
            remaining //= q
            prime_factors += 1
            if remaining % q == 0:
                return 0
            while remaining % q == 0:
                remaining //= q
        q += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def fixed_count(partition, r):
    return sum(d for d in partition if r % d == 0)


def primitive_points(partition, n):
    return sum(mobius(d) * fixed_count(partition, n // d) for d in divisors(n))


def multiply_integer_polynomials(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def determinant_denominator(partition):
    out = [1]
    for length in partition:
        factor = [0] * (length + 1)
        factor[0], factor[-1] = 1, -1
        out = multiply_integer_polynomials(out, factor)
    return out


CLASS_DATA = {
    (1, 1, 1, 1): ("1+1+1+1", 1, "1/24", 83, "(x+3)(x+7)(x+14)(x-24)"),
    (1, 1, 2): ("2+1+1", 6, "1/4", 17, "(x+2)(x+5)(x^2-7x+5)"),
    (2, 2): ("2+2", 3, "1/8", 71, "(x^2+15x-20)(x^2-15x+32)"),
    (1, 3): ("3+1", 8, "1/3", 7, "(x-3)(x^3+3x^2+2x-2)"),
    (4,): ("4", 6, "1/4", 2, "x^4+x+1"),
}


def make_row(p):
    partition = factor_degree_partition(p)
    label, class_size, density, _, _ = CLASS_DATA[partition]
    fixed = [fixed_count(partition, r) for r in range(1, MAX_ITERATE + 1)]
    primitive = [primitive_points(partition, r) for r in range(1, MAX_ITERATE + 1)]
    cycles = [primitive[r - 1] // r for r in range(1, MAX_ITERATE + 1)]
    if any(primitive[r - 1] % r for r in range(1, MAX_ITERATE + 1)):
        raise ArithmeticError("primitive point count is not divisible by period")
    return {
        "p": p,
        "factor_degree_partition": list(partition),
        "cycle_type": label,
        "s4_conjugacy_class_size": class_size,
        "chebotarev_density": density,
        "fixed_counts_r1_to_r12": fixed,
        "primitive_point_counts_r1_to_r12": primitive,
        "primitive_cycle_counts_r1_to_r12": cycles,
        "det_I_minus_uP_coefficients": determinant_denominator(partition),
        "koopman_unitary": True,
        "koopman_self_adjoint": max(partition) <= 2,
    }


def build(evaluation=YML):
    y = strict_yaml(evaluation)
    if hashlib.sha256(evaluation.read_bytes()).hexdigest() != RAW:
        raise ValueError("raw evaluator YAML drift")
    if hashlib.sha256(canonical(y)).hexdigest() != SEMANTIC:
        raise ValueError("semantic evaluator YAML drift")
    primes = primes_up_to(MAX_PRIME)
    good = [p for p in primes if p != 283]
    rows = [make_row(p) for p in good]
    counts = {data[0]: 0 for data in CLASS_DATA.values()}
    for row in rows:
        counts[row["cycle_type"]] += 1
    witnesses = []
    for partition, (label, class_size, density, p, factorization) in CLASS_DATA.items():
        if factor_degree_partition(p) != partition:
            raise ArithmeticError(f"bad witness at {p}")
        witnesses.append({
            "cycle_type": label,
            "p": p,
            "factorization_mod_p": factorization,
            "s4_conjugacy_class_size": class_size,
            "chebotarev_density": density,
        })
    flags = {
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
    body = {
        "schema": "hcs-c369-s4-frobenius-root-scheme-evidence-v2",
        "candidate_id": "HCS-C369",
        "obstruction_id": "HEN-O353",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C369/2026-09-04.yaml", "raw_sha256": RAW, "semantic_sha256": SEMANTIC},
        "model": {
            "integral_polynomial": "x^4-x-1",
            "discriminant": -283,
            "good_prime_condition": "p != 283",
            "fiber": "X_p=geometric roots of f mod p",
            "dynamics": "arithmetic Frobenius F_p(alpha)=alpha^p",
            "geometric_frobenius_convention": "geometric Frobenius is F_p inverse and has the same cycle type",
        },
        "galois_proof": {
            "irreducibility_witness": "mod 2 factorization is the irreducible polynomial x^4+x+1",
            "four_cycle_witness": "p=2 has partition 4",
            "three_cycle_witness": "p=7 has partition 3+1",
            "discriminant": "disc(f)=-283 is not a square",
            "conclusion": "the transitive subgroup has order divisible by 12; the 4-cycle or nonsquare discriminant excludes A4, hence Gal(f/Q)=S4",
        },
        "theorem_contract": {
            "factor_orbit_dictionary": "for every p != 283, irreducible factor degrees equal arithmetic-Frobenius cycle lengths on X_p",
            "fixed_points": "#Fix(F_p^r)=sum over cycle lengths d dividing r of d",
            "primitive_points": "E_p(n)=sum over d|n mu(d)#Fix(F_p^(n/d)) and primitive cycles equal E_p(n)/n",
            "determinant": "Z_p(u)=exp(sum_r #Fix(F_p^r)u^r/r)=det(I-uP_p)^(-1)=product over cycle lengths d of (1-u^d)^(-1)",
            "density": "the five classes 1+1+1+1, 2+1+1, 2+2, 3+1, 4 have Chebotarev densities 1/24, 1/4, 1/8, 1/3, 1/4",
            "ramified_boundary": "p=283 has (x-115)(x-93)^2(x+18), so the fiber is not etale and is excluded",
        },
        "ownership_boundary": OWNERSHIP_BOUNDARY,
        "finite_evidence_role": "all 1228 good primes at most 10000 and iterates through 12 are exact regression receipts; the quartic theorem covers all good primes and all iterates",
        "class_witnesses": sorted(witnesses, key=lambda row: row["p"]),
        "ramified_boundary": {
            "p": 283,
            "factorization_mod_p": "(x-115)(x-93)^2(x+18)",
            "repeated_root": 93,
            "gcd_f_fprime_coefficients_mod_p": [190, 1],
            "classification": "non-etale boundary; no four-point Frobenius permutation atlas asserted",
        },
        "class_atlas": [
            {
                "cycle_type": data[0],
                "partition": list(partition),
                "s4_conjugacy_class_size": data[1],
                "chebotarev_density": data[2],
                "det_I_minus_uP_coefficients": determinant_denominator(partition),
                "fixed_counts_r1_to_r12": [fixed_count(partition, r) for r in range(1, 13)],
            }
            for partition, data in CLASS_DATA.items()
        ],
        "prime_rows": rows,
        "enumeration": {
            "prime_bound": MAX_PRIME,
            "all_primes": len(primes),
            "good_primes": len(good),
            "ramified_primes": 1,
            "iterate_bound": MAX_ITERATE,
            "prime_iterate_cells": len(good) * MAX_ITERATE,
            "class_counts": counts,
            "all_five_types_seen": set(counts) == {row["cycle_type"] for row in witnesses} and all(counts.values()),
        },
        "collision_boundary": COLLISION_BOUNDARY,
        "nonclaims": NONCLAIMS,
        "references": [
            "J.-P. Serre, Topics in Galois Theory, second edition",
            "J. Neukirch, Algebraic Number Theory",
            "R. Lidl and H. Niederreiter, Finite Fields",
            "HCS-C12A, internal workspace ownership record for the universal zero-dimensional Frobenius finite-permutation mechanism",
        ],
        "route_a": {
            "tuple": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_ARITHMETIC_CANDIDATE",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": flags,
    }
    body["payload_sha256"] = digest(body)
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C369 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--evaluation", type=Path, default=YML)
    args = parser.parse_args()
    value = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    enum = value["enumeration"]
    print(f'C369_PRODUCER_PASS {value["payload_sha256"]} {enum["good_primes"]} {enum["prime_iterate_cells"]}')


if __name__ == "__main__":
    main()
