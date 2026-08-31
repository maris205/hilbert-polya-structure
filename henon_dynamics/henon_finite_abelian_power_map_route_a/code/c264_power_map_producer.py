#!/usr/bin/env python3
"""Produce the exact HCS-C264 finite-abelian power-map certificate."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c264_power_map_evidence.json"
SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788048000
GROUPS = [
    (), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (12,),
    (16,), (18,), (25,), (27,), (32,), (2, 2), (2, 4), (2, 6),
    (2, 8), (2, 10), (3, 3), (3, 6), (3, 9), (4, 4), (4, 8),
    (5, 10), (6, 12), (2, 2, 2), (2, 2, 4), (2, 2, 6),
    (3, 3, 3), (2, 4, 8), (4, 8, 16),
]
DS = list(range(19))


def sha_payload(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def prime_divisors(n):
    out, p = set(), 2
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.add(n)
    return out


def split_factor(n, d):
    b = 1
    for p in prime_divisors(d):
        while n % p == 0:
            b *= p
            n //= p
    return n, b


def elements(group):
    return list(itertools.product(*(range(n) for n in group))) if group else [()]


def image(x, group, d):
    return tuple((d * x[i]) % group[i] for i in range(len(group)))


def orbit_signature(x, group, d):
    seen, path, y = {}, [], x
    while y not in seen:
        seen[y] = len(path)
        path.append(y)
        y = image(y, group, d)
    return seen[y], len(path) - seen[y]


def mobius(n):
    ps = prime_divisors(n)
    for p in ps:
        if n % (p * p) == 0:
            return 0
    return -1 if len(ps) % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def lcm(a, b):
    return a // math.gcd(a, b) * b


def multiplicative_order(d, modulus):
    if modulus == 1:
        return 1
    assert math.gcd(d, modulus) == 1
    x = d % modulus
    k = 1
    while x != 1:
        x = (x * d) % modulus
        k += 1
        assert k <= modulus
    return k


def case(group, d):
    xs = elements(group)
    order = len(xs)
    exponent = 1
    for n in group:
        exponent = lcm(exponent, n)
    signatures = [orbit_signature(x, group, d) for x in xs]
    observed = {}
    for tail, period in signatures:
        observed[f"{tail}:{period}"] = observed.get(f"{tail}:{period}", 0) + 1
    mapping_raw = ";".join(
        ",".join(map(str, x)) + ">" + ",".join(map(str, image(x, group, d))) for x in xs
    )
    if d == 0:
        return {
            "group": list(group), "d": 0, "order": order, "exponent": exponent,
            "boundary": "constant_identity_map", "a_factors": [1] * len(group),
            "b_factors": list(group), "periodic_points": 1,
            "cycle_counts": {"1": 1}, "fixed_counts": {"1": 1},
            "tail_layers_per_cycle_vertex": {"0": 1, "1": order - 1},
            "image_ranks": [order, 1, 1], "zero_jordan_blocks": ({"1": order - 1} if order > 1 else {}),
            "koopman_characteristic_ledger": {"zero_multiplicity": order - 1, "cycle_factors": {"1": 1}},
            "observed_tail_period_counts": observed,
            "map_sha256": hashlib.sha256(mapping_raw.encode()).hexdigest(),
        }
    split = [split_factor(n, d) for n in group]
    aa = [a for a, _ in split]
    bb = [b for _, b in split]
    periodic = math.prod(aa)
    exp_a = 1
    for a in aa:
        exp_a = lcm(exp_a, a)
    cycle_order = multiplicative_order(d, exp_a)
    fixed = {}
    cycles = {}
    for m in range(1, cycle_order + 1):
        fm = math.prod(math.gcd(pow(d, m) - 1, a) for a in aa)
        fixed[str(m)] = fm
        primitive = sum(mobius(m // e) * fixed[str(e)] for e in divisors(m))
        if primitive:
            assert primitive % m == 0
            cycles[str(m)] = primitive // m
    k = [1]
    while k[-1] != math.prod(bb):
        j = len(k)
        k.append(math.prod(math.gcd(pow(d, j), b) for b in bb))
    height = len(k) - 1
    tail_layers = {str(j): (k[j] - (k[j - 1] if j else 0)) for j in range(height + 1)}
    ranks = [order]
    for j in range(1, height + 2):
        ranks.append(periodic * math.prod(b // math.gcd(pow(d, j), b) for b in bb))
    zero_blocks = {}
    for j in range(1, height + 1):
        z = ranks[j - 1] - 2 * ranks[j] + ranks[j + 1]
        if z:
            zero_blocks[str(j)] = z
    assert sum(int(j) * z for j, z in zero_blocks.items()) == order - periodic
    return {
        "group": list(group), "d": d, "order": order, "exponent": exponent,
        "boundary": "d_equals_one_identity" if d == 1 else "main_d_positive",
        "a_factors": aa, "b_factors": bb, "periodic_points": periodic,
        "cycle_order": cycle_order, "cycle_counts": cycles, "fixed_counts": fixed,
        "tail_height": height, "kernel_sizes": k,
        "tail_layers_per_cycle_vertex": tail_layers, "image_ranks": ranks,
        "zero_jordan_blocks": zero_blocks,
        "koopman_characteristic_ledger": {"zero_multiplicity": order - periodic, "cycle_factors": cycles},
        "observed_tail_period_counts": observed,
        "map_sha256": hashlib.sha256(mapping_raw.encode()).hexdigest(),
    }


def build():
    cases = [case(group, d) for group in GROUPS for d in DS]
    counts = {
        "group_types": len(GROUPS), "d_values": len(DS), "cases": len(cases),
        "enumerated_group_elements": sum(c["order"] for c in cases),
        "constant_boundary_cases": sum(c["d"] == 0 for c in cases),
        "identity_cases": sum(c["d"] == 1 for c in cases),
        "fixed_point_cells": sum(len(c["fixed_counts"]) for c in cases),
        "cycle_factor_cells": sum(len(c["cycle_counts"]) for c in cases),
        "tail_layer_cells": sum(len(c["tail_layers_per_cycle_vertex"]) for c in cases),
        "zero_jordan_cells": sum(len(c["zero_jordan_blocks"]) for c in cases),
    }
    data = {
        "schema": "hcs-c264-finite-abelian-power-map-v1",
        "candidate_id": "HCS-C264", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Finite abelian power maps split into a periodic automorphism and a uniform nilpotent tree, with complete zeta and Koopman Jordan atlases.",
        "theorem_contract": {
            "domain": "every finite abelian group G and every integer d>=1; d=0 is a separate constant-map boundary",
            "decomposition": "G=A_d direct-product B_d, [d]|A_d automorphic and [d]|B_d nilpotent",
            "periodic_points": "A_d cross {0}",
            "fixed_formula": "Fix([d]^n)=product_i gcd(d^n-1,a_i)",
            "primitive_formula": "P_m=sum_{e|m} mu(m/e) Fix_e and C_m=P_m/m",
            "zeta_formula": "zeta(t)=product_m (1-t^m)^(-C_m)",
            "tail_formula": "K_j=product_i gcd(d^j,b_i); exact height-j layer K_j-K_{j-1}",
            "koopman_formula": "rank(U^j)=R_j=|A| product_i b_i/gcd(d^j,b_i); Z_j=R_{j-1}-2R_j+R_{j+1}",
            "characteristic_formula": "det(lambda I-U)=lambda^(|G|-|A|) product_m(lambda^m-1)^C_m",
            "d_zero_boundary": "one fixed point, tail-one star, zeta=(1-t)^-1, diagonalizable Koopman spectrum 1 plus |G|-1 zeros",
        },
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_PARTIAL", "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data_claimed": False, "bad_euler_factor_claimed": False,
            "root_number_claimed": False, "automorphy_claimed": False,
            "target_divisor_claimed": False, "functional_equation_claimed": False,
            "hilbert_polya_operator_claimed": False, "literature_priority_claimed": False,
        },
        "nonclaims": [
            "No Euler factor, root number, automorphy, target divisor, functional equation, or Hilbert--Polya operator is claimed.",
            "The Koopman matrix is a finite source composition operator and is generally nonnormal.",
            "Ownership is only of this workspace certificate; no literature-priority claim is made.",
        ],
        "regression": {"corpus": "34 invariant-factor group types x d=0,...,18", "counts": counts, "cases": cases},
    }
    data["payload_sha256"] = sha_payload(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    c = data["regression"]["counts"]
    print(f"C264_PRODUCER_PASS cases={c['cases']} elements={c['enumerated_group_elements']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
