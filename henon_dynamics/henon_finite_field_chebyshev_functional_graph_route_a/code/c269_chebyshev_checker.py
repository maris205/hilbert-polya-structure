#!/usr/bin/env python3
"""Independent field-enumeration checker for HCS-C269; imports no producer."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c269_chebyshev_evidence.json"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]


def payload_hash(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def unpack(a, p, r):
    out = []
    for _ in range(r): out.append(a % p); a //= p
    return out


def pack(cs, p, r):
    out, place = 0, 1
    for c in cs[:r]: out += (c % p) * place; place *= p
    return out


def is_prime(p):
    if not isinstance(p, int) or p < 2:
        return False
    return all(p % divisor for divisor in range(2, math.isqrt(p) + 1))


def polynomial_remainder(dividend, divisor, p):
    """Constant-first remainder in GF(p)[X]; divisor is monic."""
    remainder = [coefficient % p for coefficient in dividend]
    while remainder and remainder[-1] == 0:
        remainder.pop()
    degree = len(divisor) - 1
    while len(remainder) - 1 >= degree:
        lead = remainder[-1]
        shift = len(remainder) - len(divisor)
        for index, coefficient in enumerate(divisor):
            remainder[shift + index] = (remainder[shift + index] - lead * coefficient) % p
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return remainder


def is_monic_irreducible(modulus, p):
    """Brute-force irreducibility, independent of the producer and CAS."""
    degree = len(modulus) - 1
    if degree < 1 or modulus[-1] != 1:
        return False
    for divisor_degree in range(1, degree // 2 + 1):
        for lower in itertools.product(range(p), repeat=divisor_degree):
            divisor = list(lower) + [1]
            if not polynomial_remainder(modulus, divisor, p):
                return False
    return True


def add(a, b, p, r):
    return pack([(x + y) % p for x, y in zip(unpack(a, p, r), unpack(b, p, r))], p, r)


def neg(a, p, r): return pack([(-x) % p for x in unpack(a, p, r)], p, r)


def mul(a, b, p, modulus):
    r = len(modulus) - 1
    aa, bb = unpack(a, p, r), unpack(b, p, r)
    cc = [0] * (2 * r - 1)
    for i, x in enumerate(aa):
        for j, y in enumerate(bb): cc[i + j] = (cc[i + j] + x * y) % p
    for k in range(len(cc) - 1, r - 1, -1):
        lead = cc[k] % p
        for j in range(r): cc[k - r + j] = (cc[k - r + j] - lead * modulus[j]) % p
    return pack(cc, p, r)


def cheb(x, d, p, modulus):
    r = len(modulus) - 1
    if d == 0: return 2 % p
    if d == 1: return x
    old, cur = 2 % p, x
    for _ in range(2, d + 1):
        old, cur = cur, add(mul(x, cur, p, modulus), neg(old, p, r), p, r)
    return cur


def iterate(mapping, x, n):
    for _ in range(n): x = mapping[x]
    return x


def signature(mapping, x):
    seen, path = {}, []
    while x not in seen:
        seen[x] = len(path); path.append(x); x = mapping[x]
    return seen[x], len(path) - seen[x]


def quotient_count(q, a, b):
    return (a + math.gcd(2, a)) // 2 + (b + math.gcd(2, b)) // 2 - 1 - int(q % 2 == 1 and a % 2 == 0 and b % 2 == 0)


def fixed_closed(q, D):
    pieces = []
    for n in (q - 1, q + 1):
        u, v = math.gcd(D - 1, n), math.gcd(D + 1, n)
        w = math.gcd(math.gcd(D - 1, D + 1), n)
        s = u + v - w
        inv = 1 + int(n % 2 == 0 and D % 2 == 1)
        pieces.append((s + inv) // 2)
    branch = 1 + int(q % 2 == 1 and D % 2 == 1)
    return sum(pieces) - branch, branch


def quick(data):
    checks = 0
    assert data["schema"] == "hcs-c269-finite-field-chebyshev-v1"; checks += 1
    assert data["candidate_id"] == "HCS-C269" and data["source_commit"] == SOURCE; checks += 2
    assert data["fixed_epoch"] == 1788134400 and data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"; checks += 2
    assert data["evaluator"]["sha256"] == EVAL and data["payload_sha256"] == payload_hash(data); checks += 2
    assert data["route_a"]["tuple"] == TUPLE and data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY"; checks += 2
    assert data["route_a"]["route_b_invocation_allowed"] is False; checks += 1
    assert all(v is False for v in data["scope_flags"].values()); checks += len(data["scope_flags"])
    cases, counts = data["regression"]["cases"], data["regression"]["counts"]
    assert len(cases) == counts["cases"] == 121; checks += 2
    assert counts["field_models"] == counts["degree_values"] == 11; checks += 2
    assert len({(c["q"], c["d"]) for c in cases}) == 121; checks += 1
    models = {}
    for c in cases:
        q, d = c["q"], c["d"]
        p, extension_degree, modulus = c["p"], c["extension_degree"], c["modulus"]
        assert is_prime(p); checks += 1
        assert p ** extension_degree == q; checks += 1
        assert len(modulus) == extension_degree + 1 and modulus[-1] == 1; checks += 2
        assert all(isinstance(coefficient, int) and 0 <= coefficient < p for coefficient in modulus); checks += 1
        assert is_monic_irreducible(modulus, p); checks += 1
        model = (p, extension_degree, tuple(modulus))
        if q in models:
            assert models[q] == model; checks += 1
        else:
            models[q] = model
        assert c["cover_orders"] == [q - 1, q + 1]; checks += 1
        assert c["intersection_order"] == math.gcd(2, q - 1); checks += 1
        assert c["branch_value_count"] == (1 if q % 2 == 0 else 2); checks += 1
        assert sum(int(m) * n for m, n in c["cycle_counts"].items()) == c["periodic_points"]; checks += 1
        ledger = c["koopman_characteristic_ledger"]
        assert ledger["cycle_factors"] == c["cycle_counts"]; checks += 1
        assert ledger["zero_multiplicity"] == q - c["periodic_points"]; checks += 1
        assert sum(int(j) * n for j, n in c["zero_jordan_blocks"].items()) == ledger["zero_multiplicity"]; checks += 1
        assert c["image_ranks"][0] == q and c["image_ranks"][-1] == c["image_ranks"][-2] == c["periodic_points"]; checks += 2
        assert sum(c["tail_layers"]) == q and c["tail_layers"][0] == c["periodic_points"]; checks += 2
        if d == 0:
            assert c["fixed_counts"] == {"1": 1} and c["image_ranks"] == [q, 1, 1]; checks += 2
        else:
            a0, a1 = c["prime_to_d_orders"]; b0, b1 = c["d_primary_orders"]
            assert a0 * b0 == q - 1 and a1 * b1 == q + 1; checks += 2
            assert math.gcd(a0, d) == math.gcd(a1, d) == 1; checks += 1
            assert c["periodic_points"] == quotient_count(q, a0, a1); checks += 1
            for n, value in c["fixed_counts"].items():
                formula, branch = fixed_closed(q, pow(d, int(n)))
                assert value == formula and c["fixed_branch_subtractions"][n] == branch; checks += 2
            ranks = c["image_ranks"]
            for j, number in c["zero_jordan_blocks"].items():
                j = int(j); assert number == ranks[j - 1] - 2 * ranks[j] + ranks[j + 1]; checks += 1
    assert len(models) == counts["field_models"]; checks += 1
    for q in models:
        assert {c["d"] for c in cases if c["q"] == q} == set(range(11)); checks += 1
    return checks


def full(data):
    checks = quick(data)
    total = 0
    for c in data["regression"]["cases"]:
        q, p, modulus, d = c["q"], c["p"], c["modulus"], c["d"]
        mapping = [cheb(x, d, p, modulus) for x in range(q)]
        total += q
        raw = ";".join(f"{x}>{y}" for x, y in enumerate(mapping))
        assert hashlib.sha256(raw.encode()).hexdigest() == c["map_sha256"]; checks += q
        sigs = [signature(mapping, x) for x in range(q)]
        observed = {}
        for tail, period in sigs: observed[f"{tail}:{period}"] = observed.get(f"{tail}:{period}", 0) + 1
        assert observed == c["observed_tail_period_counts"]; checks += q
        assert sum(t == 0 for t, _ in sigs) == c["periodic_points"]; checks += q
        direct_cycles = {}
        for m in sorted({period for tail, period in sigs if tail == 0}):
            direct_cycles[str(m)] = sum(t == 0 and per == m for t, per in sigs) // m
        assert direct_cycles == c["cycle_counts"]; checks += c["periodic_points"]
        for n, expected in c["fixed_counts"].items():
            assert sum(iterate(mapping, x, int(n)) == x for x in range(q)) == expected; checks += q
        for j, expected in enumerate(c["image_ranks"]):
            assert len({iterate(mapping, x, j) for x in range(q)}) == expected; checks += q
        layers = [sum(t == j for t, _ in sigs) for j in range(c["tail_height"] + 1)]
        assert layers == c["tail_layers"]; checks += q
        cumulative = []
        running = 0
        for value in layers: running += value; cumulative.append(running)
        assert cumulative == c["tail_cumulative"]; checks += q
    assert total == data["regression"]["counts"]["direct_field_vertices"]; checks += 1
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    count = quick(data) if args.quick else full(data)
    print(f"C269 independent checker: PASS ({count} assertions; mode={'quick' if args.quick else 'full'})")


if __name__ == "__main__":
    main()
