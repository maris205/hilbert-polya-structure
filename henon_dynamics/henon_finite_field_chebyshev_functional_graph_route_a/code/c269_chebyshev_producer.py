#!/usr/bin/env python3
"""Produce the exact HCS-C269 finite-field Chebyshev certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c269_chebyshev_evidence.json"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788134400

# Coefficients are constant-first monic irreducible polynomials over F_p.
FIELDS = [
    (4, 2, (1, 1, 1)), (5, 5, (0, 1)), (7, 7, (0, 1)),
    (8, 2, (1, 1, 0, 1)), (9, 3, (1, 0, 1)), (11, 11, (0, 1)),
    (13, 13, (0, 1)), (16, 2, (1, 1, 0, 0, 1)),
    (25, 5, (2, 0, 1)), (27, 3, (1, 2, 0, 1)),
    (49, 7, (1, 0, 1)),
]
DEGREES = list(range(11))


def canonical_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


class GF:
    def __init__(self, q, p, modulus):
        self.q, self.p, self.modulus = q, p, tuple(modulus)
        self.r = len(modulus) - 1
        assert p ** self.r == q and modulus[-1] == 1

    def digits(self, a):
        out = []
        for _ in range(self.r):
            out.append(a % self.p)
            a //= self.p
        return out

    def pack(self, cs):
        out, place = 0, 1
        for c in cs[: self.r]:
            out += (c % self.p) * place
            place *= self.p
        return out

    def add(self, a, b):
        aa, bb = self.digits(a), self.digits(b)
        return self.pack([(x + y) % self.p for x, y in zip(aa, bb)])

    def neg(self, a):
        return self.pack([(-x) % self.p for x in self.digits(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        aa, bb = self.digits(a), self.digits(b)
        cc = [0] * (2 * self.r - 1)
        for i, x in enumerate(aa):
            for j, y in enumerate(bb):
                cc[i + j] = (cc[i + j] + x * y) % self.p
        for k in range(len(cc) - 1, self.r - 1, -1):
            lead = cc[k] % self.p
            if lead:
                for j in range(self.r):
                    cc[k - self.r + j] = (cc[k - self.r + j] - lead * self.modulus[j]) % self.p
        return self.pack(cc)

    def integer(self, n):
        return n % self.p


def chebyshev_value(field, d, x):
    if d == 0:
        return field.integer(2)
    if d == 1:
        return x
    before, current = field.integer(2), x
    for _ in range(2, d + 1):
        before, current = current, field.sub(field.mul(x, current), before)
    return current


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_divisors(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def mobius(n):
    ps = prime_divisors(n)
    if any(n % (p * p) == 0 for p in ps):
        return 0
    return -1 if len(ps) % 2 else 1


def split_factor(n, d):
    b = 1
    for p in prime_divisors(d):
        while n % p == 0:
            b *= p
            n //= p
    return n, b


def multiplicative_order(d, n):
    if n == 1:
        return 1
    assert math.gcd(d, n) == 1
    x, k = d % n, 1
    while x != 1:
        x = x * d % n
        k += 1
        assert k <= n
    return k


def quotient_union_count(q, left_order, right_order):
    """Inversion quotients of two cyclic subgroups, glued at ramified branches."""
    left = (left_order + math.gcd(2, left_order)) // 2
    right = (right_order + math.gcd(2, right_order)) // 2
    overlap = 1 + int(q % 2 == 1 and left_order % 2 == 0 and right_order % 2 == 0)
    return left + right - overlap


def cover_fixed_data(n, D):
    minus = math.gcd(D - 1, n)
    plus = math.gcd(D + 1, n)
    meet = math.gcd(math.gcd(D - 1, D + 1), n)
    union = minus + plus - meet
    inversion_fixed = 1 + int(n % 2 == 0 and D % 2 == 1)
    assert (union + inversion_fixed) % 2 == 0
    return {
        "minus_kernel": minus, "plus_kernel": plus, "kernel_intersection": meet,
        "cover_union": union, "inversion_fixed": inversion_fixed,
        "quotient_fixed": (union + inversion_fixed) // 2,
    }


def fixed_formula(q, d, n):
    D = pow(d, n)
    left = cover_fixed_data(q - 1, D)
    right = cover_fixed_data(q + 1, D)
    branch = 1 + int(q % 2 == 1 and D % 2 == 1)
    return left["quotient_fixed"] + right["quotient_fixed"] - branch, left, right, branch


def iterate_map(mapping, x, n):
    for _ in range(n):
        x = mapping[x]
    return x


def orbit_signature(mapping, x):
    seen, path = {}, []
    while x not in seen:
        seen[x] = len(path)
        path.append(x)
        x = mapping[x]
    return seen[x], len(path) - seen[x]


def case(q, p, modulus, d):
    field = GF(q, p, modulus)
    mapping = [chebyshev_value(field, d, x) for x in range(q)]
    raw = ";".join(f"{x}>{y}" for x, y in enumerate(mapping))
    signatures = [orbit_signature(mapping, x) for x in range(q)]
    observed = {}
    for tail, period in signatures:
        observed[f"{tail}:{period}"] = observed.get(f"{tail}:{period}", 0) + 1
    if d == 0:
        return {
            "q": q, "p": p, "extension_degree": field.r, "modulus": list(modulus), "d": d,
            "boundary": "degree_zero_constant_two", "cover_orders": [q - 1, q + 1],
            "intersection_order": math.gcd(2, q - 1), "branch_value_count": 1 if q % 2 == 0 else 2,
            "periodic_points": 1, "cycle_horizon": 1, "fixed_counts": {"1": 1},
            "cycle_counts": {"1": 1}, "fixed_branch_subtractions": {"1": 1 if q % 2 == 0 else 2},
            "tail_height": 1, "tail_cumulative": [1, q], "tail_layers": [1, q - 1],
            "image_ranks": [q, 1, 1], "zero_jordan_blocks": ({"1": q - 1} if q > 1 else {}),
            "koopman_characteristic_ledger": {"zero_multiplicity": q - 1, "cycle_factors": {"1": 1}},
            "observed_tail_period_counts": observed,
            "map_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        }

    a0, b0 = split_factor(q - 1, d)
    a1, b1 = split_factor(q + 1, d)
    periodic = quotient_union_count(q, a0, a1)
    horizon = math.lcm(multiplicative_order(d, a0), multiplicative_order(d, a1))
    fixed, branch_subtractions = {}, {}
    for n in range(1, horizon + 1):
        value, _, _, branch = fixed_formula(q, d, n)
        fixed[str(n)] = value
        branch_subtractions[str(n)] = branch
    cycles = {}
    for m in range(1, horizon + 1):
        primitive = sum(mobius(m // e) * fixed[str(e)] for e in divisors(m))
        assert primitive >= 0 and primitive % m == 0
        if primitive:
            cycles[str(m)] = primitive // m
    assert sum(int(m) * c for m, c in cycles.items()) == periodic

    height = 0
    while math.gcd(pow(d, height), b0) != b0 or math.gcd(pow(d, height), b1) != b1:
        height += 1
        assert height <= max(q - 1, q + 1)
    cumulative = []
    for j in range(height + 1):
        h0 = a0 * math.gcd(pow(d, j), b0)
        h1 = a1 * math.gcd(pow(d, j), b1)
        cumulative.append(quotient_union_count(q, h0, h1))
    assert cumulative[0] == periodic and cumulative[-1] == q
    layers = [cumulative[0]] + [cumulative[j] - cumulative[j - 1] for j in range(1, len(cumulative))]
    ranks = []
    for j in range(height + 2):
        D = pow(d, j)
        m0 = (q - 1) // math.gcd(D, q - 1)
        m1 = (q + 1) // math.gcd(D, q + 1)
        ranks.append(quotient_union_count(q, m0, m1))
    assert ranks[-1] == ranks[-2] == periodic
    zero = {}
    for j in range(1, height + 1):
        number = ranks[j - 1] - 2 * ranks[j] + ranks[j + 1]
        assert number >= 0
        if number:
            zero[str(j)] = number
    assert sum(int(j) * z for j, z in zero.items()) == q - periodic
    return {
        "q": q, "p": p, "extension_degree": field.r, "modulus": list(modulus), "d": d,
        "boundary": "degree_one_identity" if d == 1 else "main_degree_positive",
        "cover_orders": [q - 1, q + 1], "prime_to_d_orders": [a0, a1],
        "d_primary_orders": [b0, b1], "intersection_order": math.gcd(2, q - 1),
        "branch_value_count": 1 if q % 2 == 0 else 2, "periodic_points": periodic,
        "cycle_horizon": horizon, "fixed_counts": fixed, "cycle_counts": cycles,
        "fixed_branch_subtractions": branch_subtractions, "tail_height": height,
        "tail_cumulative": cumulative, "tail_layers": layers, "image_ranks": ranks,
        "zero_jordan_blocks": zero,
        "koopman_characteristic_ledger": {"zero_multiplicity": q - periodic, "cycle_factors": cycles},
        "observed_tail_period_counts": observed,
        "map_sha256": hashlib.sha256(raw.encode()).hexdigest(),
    }


def build():
    cases = [case(q, p, modulus, d) for q, p, modulus in FIELDS for d in DEGREES]
    counts = {
        "field_models": len(FIELDS), "degree_values": len(DEGREES), "cases": len(cases),
        "direct_field_vertices": sum(c["q"] for c in cases),
        "nonprime_field_cases": sum(c["extension_degree"] > 1 for c in cases),
        "characteristic_two_cases": sum(c["p"] == 2 for c in cases),
        "fixed_cells": sum(len(c["fixed_counts"]) for c in cases),
        "cycle_cells": sum(len(c["cycle_counts"]) for c in cases),
        "tail_cells": sum(len(c["tail_layers"]) for c in cases),
        "image_rank_cells": sum(len(c["image_ranks"]) for c in cases),
        "zero_jordan_cells": sum(len(c["zero_jordan_blocks"]) for c in cases),
    }
    data = {
        "schema": "hcs-c269-finite-field-chebyshev-v1", "candidate_id": "HCS-C269",
        "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every finite-field Chebyshev map is the inversion quotient of two cyclic power maps with exact ramified gluing, cycles, tails, zeta, and Koopman Jordan data.",
        "theorem_contract": {
            "domain": "every prime power q and every integer degree d>=1; d=0 is a separate constant-T_0 boundary",
            "semiconjugacy": "eta(z)=z+z^-1 and eta(z^d)=T_d(eta(z)) on F_q^* union ker Norm(F_q2^*/F_q^*)",
            "quotient": "identify z with z^-1 in each cyclic cover and glue the two copies of their order-gcd(2,q-1) intersection",
            "fixed_formula": "two signed power kernels, inversion Burnside, then subtraction of one or two ramified branch values",
            "tail_formula": "d-primary cover components die; cumulative tail populations are the glued inversion-quotient counts of subgroup orders a_sigma gcd(d^j,b_sigma)",
            "image_formula": "rank U^j equals the glued quotient count of cover image orders (q+sigma)/gcd(d^j,q+sigma)",
            "zeta_formula": "Mobius fixed-to-cycle inversion and product_m(1-t^m)^(-C_m)",
            "koopman_formula": "Z_j=R_(j-1)-2R_j+R_(j+1) and det(lambda I-U)=lambda^(q-P) product_m(lambda^m-1)^C_m",
        },
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data_claimed": False, "bad_euler_factor_claimed": False,
            "root_number_claimed": False, "automorphy_claimed": False,
            "target_divisor_claimed": False, "functional_equation_claimed": False,
            "hilbert_polya_operator_claimed": False, "literature_priority_claimed": False,
        },
        "nonclaims": [
            "Finite-field provenance is not a rational-prime primitive-orbit dictionary or a logarithmic prime clock.",
            "The finite source zeta and Koopman matrix are not target Euler data or a Hilbert--Polya operator.",
            "Workspace ownership does not assert literature priority.",
        ],
        "regression": {"corpus": "11 exact field models x degrees 0,...,10", "counts": counts, "cases": cases},
    }
    data["payload_sha256"] = canonical_hash(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    c = data["regression"]["counts"]
    print(f"C269_PRODUCER_PASS cases={c['cases']} vertices={c['direct_field_vertices']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
