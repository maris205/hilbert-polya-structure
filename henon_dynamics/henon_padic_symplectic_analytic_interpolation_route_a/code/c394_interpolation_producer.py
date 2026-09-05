#!/usr/bin/env python3
"""Exact formula producer; finite audits do not prove the infinite theorem."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c394 producer refuses optimized Python")
import argparse
import hashlib
import json
from collections import Counter
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLAGS = ("claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number", "claims_automorphy", "claims_target_divisor_or_counting_law", "claims_target_functional_equation", "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b")

def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def valuation(n, p):
    assert n != 0
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def parameters():
    for p, top in ((2, 5), (3, 4), (5, 3), (7, 2)):
        first = 2 if p == 2 else 1
        for c in (first, first + 1):
            for unit in (1, 3 if p == 2 else 2):
                yield p, unit * p**c, c, top

def metadata():
    return {"schema": "hcs-exact-evidence-v1", "candidate_id": "HCS-C394", "source_commit": "697518b6db90458f86f7916fbf397b8ad5ef2372", "fixed_epoch": 1788566400, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "scope_flags": {k: False for k in FLAGS}, "route_a": {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall_verdict": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}, "evidence_role": "finite exact regression; not a proof of the infinite theorem or a target match"}

def finite_levels():
    rows = []
    for p, a, c, top in parameters():
        for nlevel in range(1, top + 1):
            shells = []
            cycles = Counter({1: 1})
            for r in range(nlevel):
                size = p**(2*(nlevel-r)) - p**(2*(nlevel-r-1))
                period = p**max(0, nlevel-c-2*r)
                assert size % period == 0
                shells.append({"r": r, "points": size, "period": period, "cycles": size//period})
                cycles[period] += size//period
            fixed = []
            for n in range(1, 25):
                rmin = max(0, (nlevel-c-valuation(n, p)+1)//2)
                fixed.append({"n": n, "points": p**(2*(nlevel-rmin))})
            rows.append({"p": p, "a": a, "c": c, "N": nlevel, "points": p**(2*nlevel), "shells": shells, "cycle_histogram": [[k, v] for k, v in sorted(cycles.items())], "fixed_iterates": fixed})
    return rows

def iterate(seed, a, n, modulus):
    x, y = seed
    for _ in range(n):
        x = (x+a*y*y) % modulus
        y = (y+a*x*x) % modulus
    return [x % modulus, y % modulus]

def displacements():
    rows = []
    for p, a, c, _ in parameters():
        seeds = ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1))
        for r in range(4):
            for base in seeds:
                seed = [p**r*x for x in base]
                for s in (0, 1, 2):
                    for t in (3, p+3, p*p+3):
                        expected = c+2*r+valuation(t-s, p)
                        precision = expected+3
                        mod = p**precision
                        us, ut = iterate(seed, a, s, mod), iterate(seed, a, t, mod)
                        diff = [(v-u) % mod for u, v in zip(us, ut)]
                        observed = min(valuation(v, p) if v else precision for v in diff)
                        assert observed == expected < precision
                        rows.append({"p": p, "a": a, "c": c, "r": r, "seed": seed, "s": s, "t": t, "precision": precision, "difference": diff, "expected_valuation": expected, "observed_valuation": observed})
    return rows

# Sparse integer polynomials in a,x,y; no symbolic dependency in the producer.
def add(*polynomials):
    result = Counter()
    for poly in polynomials:
        for e, coefficient in poly.items():
            result[e] += coefficient
    return {e: z for e, z in result.items() if z}

def scale(poly, k):
    return {e: k*z for e, z in poly.items() if k*z}

def mul(left, right):
    result = Counter()
    for e, x in left.items():
        for f, y in right.items():
            result[tuple(a+b for a, b in zip(e, f))] += x*y
    return {e: z for e, z in result.items() if z}

def polynomial_differences():
    ap = {(1, 0, 0): 1}
    orbit = [({(0, 1, 0): 1}, {(0, 0, 1): 1})]
    for _ in range(3):
        x, y = orbit[-1]
        x = add(x, mul(ap, mul(y, y)))
        y = add(y, mul(ap, mul(x, x)))
        orbit.append((x, y))
    result = []
    for m in range(4):
        coordinates = []
        for j in range(2):
            d = add(*(scale(orbit[k][j], (-1)**(m-k)*comb(m, k)) for k in range(m+1)))
            assert all(e[0] >= m for e in d)
            coordinates.append([[*e, z] for e, z in sorted(d.items())])
        result.append({"m": m, "coordinates": coordinates})
    return result

def tails():
    rows = []
    for p, a, c, _ in parameters():
        for m in range(1, 65):
            factorial = sum(m//p**j for j in range(1, m+1))
            rows.append({"p": p, "a": a, "c": c, "m": m, "factorial_valuation": factorial, "gauss_valuation_lower_bound": c*m-factorial, "strict_margins": [(c+r)*(m-1)-valuation(m, p) for r in range(4)] if m >= 2 else []})
    return rows

def controls():
    return {"zero_parameter": {"modulus": 16, "points": 256, "fixed": 256}, "dyadic_threshold_counterexample": {"modulus": 16, "orbit": [1, 15, 1], "coefficient_congruence_valuation": 1}, "pointwise_not_coefficientwise": [{"p": p, "residue_values": [pow(x, p, p) for x in range(p)], "coefficient_minimum_valuation": 0} for p in (2, 3, 5, 7)], "genuine_periodic_points": [[0, 0]], "genuine_fixed_counts": [1]*24, "origin_derivative": [[1, 0], [0, 1]], "clock_boundary": ["integer iteration interpolated into Z_p without a roof", "finite quotient cycles are not genuine periodic points", "ordinary tail is not a new certificate algorithm", "local prime p is not an orbit label for rational primes"]}

def produce():
    data = metadata()
    data.update(finite_levels=finite_levels(), displacements=displacements(), polynomial_differences=polynomial_differences(), tails=tails(), controls=controls())
    data["payload_sha256"] = hashlib.sha256(canonical(data)).hexdigest()
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT/"results/c394_interpolation_evidence.json")
    args = parser.parse_args()
    data = produce()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2)+"\n")
    print("C394 producer PASS: "+json.dumps({"finite_levels": len(data["finite_levels"]), "residue_points": sum(r["points"] for r in data["finite_levels"]), "displacements": len(data["displacements"]), "polynomial_coefficients": sum(len(c) for r in data["polynomial_differences"] for c in r["coordinates"]), "tails": len(data["tails"]), "payload": data["payload_sha256"]}, sort_keys=True))

if __name__ == "__main__":
    main()
