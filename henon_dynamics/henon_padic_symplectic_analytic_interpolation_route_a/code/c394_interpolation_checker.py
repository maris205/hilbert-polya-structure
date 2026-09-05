#!/usr/bin/env python3
"""Independent full reconstruction: direct residue permutations, not producer formulas."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c394 checker refuses optimized Python")
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from math import factorial
from functools import lru_cache
from pathlib import Path
import sympy as sp
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT/"evaluations/route_a/HCS-C394/2026-09-05.yaml"
EVALUATION_RAW_SHA = "3d4d871d9868869617bd8caae8f666f32738ee7f556365240b13df07b77500d6"
EVALUATION_SEMANTIC_SHA = "fe7a577749a18741385c74b7746c336b824f7cc5fb8dce1504d47e041ba4bd4f"
FLAGS = ("claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number", "claims_automorphy", "claims_target_divisor_or_counting_law", "claims_target_functional_equation", "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b")
CHECKS = 0

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out

def read(path):
    return json.loads(path.read_text(), object_pairs_hook=unique, parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))

def same(got, want, path="root"):
    global CHECKS
    CHECKS += 1
    assert type(got) is type(want), "type at "+path
    if type(want) is dict:
        assert set(got) == set(want), "keys at "+path
        for key in want:
            same(got[key], want[key], path+"."+key)
    elif type(want) is list:
        assert len(got) == len(want), "length at "+path
        for k, (a, b) in enumerate(zip(got, want)):
            same(a, b, path+"["+str(k)+"]")
    else:
        assert got == want, "value at "+path

def admissible_tree(x):
    if type(x) is dict:
        assert all(type(k) is str for k in x), "nonstring key"
        for value in x.values():
            admissible_tree(value)
    elif type(x) is list:
        for value in x:
            admissible_tree(value)
    else:
        assert type(x) in (str, int, bool), "unsupported scalar type"

class LockedLoader(yaml.SafeLoader):
    pass

def mapping(loader, node, deep=False):
    out = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if type(key) is not str or key in out or key == "<<":
            raise ValueError("invalid YAML mapping")
        out[key] = loader.construct_object(v, deep=deep)
    return out

LockedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

def evaluation(path):
    raw = path.read_bytes()
    # Parse independently as well as freezing bytes: both are mandatory on write.
    for token in yaml.scan(raw.decode()):
        assert not isinstance(token, (yaml.tokens.AliasToken, yaml.tokens.AnchorToken, yaml.tokens.TagToken)), "YAML alias, anchor or tag"
    data = yaml.load(raw, Loader=LockedLoader)
    admissible_tree(data)
    assert data["route_b_invocation_allowed"] is False
    assert set(data["scope_flags"]) == set(FLAGS)
    assert all(v is False for v in data["scope_flags"].values())
    assert hashlib.sha256(canonical(data)).hexdigest() == EVALUATION_SEMANTIC_SHA, "YAML semantic lock"
    assert hashlib.sha256(raw).hexdigest() == EVALUATION_RAW_SHA, "YAML raw lock"
    return data

def vp(n, p):
    assert n
    return next(k for k in range(abs(n).bit_length()+1) if n % p**(k+1))

def configs():
    answer = []
    for p in (2, 3, 5, 7):
        low, high = (2 if p == 2 else 1), {2: 5, 3: 4, 5: 3, 7: 2}[p]
        for c in range(low, low+2):
            for unit in (1, 3 if p == 2 else 2):
                answer.append((p, unit*p**c, c, high))
    return answer

def step(u, a, modulus):
    x, y = u
    # Expanded evaluation, independently different from sequential shear code.
    return [(x+a*y*y) % modulus, (y+a*x*x+2*a*a*x*y*y+a**3*y**4) % modulus]

def reconstruct_levels():
    rows = []
    for p, a, c, high in configs():
        for N in range(1, high+1):
            mod = p**N
            nxt = []
            for y in range(mod):
                for x in range(mod):
                    xx, yy = step((x, y), a, mod)
                    nxt.append(xx+mod*yy)
            assert len(set(nxt)) == mod*mod
            unseen = set(range(mod*mod))
            lengths = [0]*(mod*mod)
            hist = Counter()
            while unseen:
                start = min(unseen)
                cycle = [start]
                v = nxt[start]
                while v != start:
                    assert v not in cycle
                    cycle.append(v)
                    v = nxt[v]
                for v in cycle:
                    unseen.remove(v)
                    lengths[v] = len(cycle)
                hist[len(cycle)] += 1
            by_radius = defaultdict(list)
            for value in range(1, mod*mod):
                x, y = value % mod, value//mod
                r = min(vp(x, p) if x else N, vp(y, p) if y else N)
                by_radius[r].append(lengths[value])
            shells = []
            for r in range(N):
                L = set(by_radius[r])
                assert len(L) == 1
                length = L.pop()
                shells.append({"r": r, "points": len(by_radius[r]), "period": length, "cycles": len(by_radius[r])//length})
            fixed = [{"n": n, "points": sum(L*num for L, num in hist.items() if n % L == 0)} for n in range(1, 25)]
            rows.append({"p": p, "a": a, "c": c, "N": N, "points": len(nxt), "shells": shells, "cycle_histogram": [[L, num] for L, num in sorted(hist.items())], "fixed_iterates": fixed})
    return rows

def reconstruct_displacements():
    rows = []
    for p, a, c, _ in configs():
        for r in range(4):
            for x, y in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1)):
                seed = [p**r*x, p**r*y]
                for s in range(3):
                    for t in (3, p+3, p*p+3):
                        expected = c+2*r+vp(t-s, p)
                        precision = expected+3
                        modulus = p**precision
                        orbit = [seed]
                        for _ in range(t):
                            orbit.append(step(orbit[-1], a, modulus))
                        difference = [(orbit[t][j]-orbit[s][j]) % modulus for j in range(2)]
                        observed = min(vp(v, p) if v else precision for v in difference)
                        assert observed == expected
                        rows.append({"p": p, "a": a, "c": c, "r": r, "seed": seed, "s": s, "t": t, "precision": precision, "difference": difference, "expected_valuation": expected, "observed_valuation": observed})
    return rows

def reconstruct_polynomials():
    a, x, y = sp.symbols("a x y")
    fx, fy = x+a*y*y, y+a*(x+a*y*y)**2
    current = [x, y]
    rows = []
    for m in range(4):
        polys = [sp.Poly(h, a, x, y) for h in current]
        rows.append({"m": m, "coordinates": [[[int(i) for i in e]+[int(z)] for e, z in sorted(poly.terms())] for poly in polys]})
        if m < 3:
            current = [sp.expand(h.subs({x: fx, y: fy}, simultaneous=True)-h) for h in current]
    return rows

def expected_metadata():
    return {"schema": "hcs-exact-evidence-v1", "candidate_id": "HCS-C394", "source_commit": "697518b6db90458f86f7916fbf397b8ad5ef2372", "fixed_epoch": 1788566400, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "scope_flags": {name: False for name in FLAGS}, "route_a": {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall_verdict": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}, "evidence_role": "finite exact regression; not a proof of the infinite theorem or a target match"}

@lru_cache(maxsize=1)
def reconstruct():
    data = expected_metadata()
    data["finite_levels"] = reconstruct_levels()
    data["displacements"] = reconstruct_displacements()
    data["polynomial_differences"] = reconstruct_polynomials()
    data["tails"] = [{"p": p, "a": a, "c": c, "m": m, "factorial_valuation": vp(factorial(m), p), "gauss_valuation_lower_bound": c*m-vp(factorial(m), p), "strict_margins": [(c+r)*(m-1)-vp(m, p) for r in range(4)] if m > 1 else []} for p, a, c, _ in configs() for m in range(1, 65)]
    data["controls"] = {"zero_parameter": {"modulus": 16, "points": 256, "fixed": sum(step((x, y), 0, 16) == [x, y] for x in range(16) for y in range(16))}, "dyadic_threshold_counterexample": {"modulus": 16, "orbit": [(-1)**n % 16 for n in range(3)], "coefficient_congruence_valuation": vp(-2, 2)}, "pointwise_not_coefficientwise": [{"p": p, "residue_values": [x**p % p for x in range(p)], "coefficient_minimum_valuation": 0} for p in (2, 3, 5, 7)], "genuine_periodic_points": [[0, 0]], "genuine_fixed_counts": [1 for _ in range(24)], "origin_derivative": [[1, 0], [0, 1]], "clock_boundary": ["integer iteration interpolated into Z_p without a roof", "finite quotient cycles are not genuine periodic points", "ordinary tail is not a new certificate algorithm", "local prime p is not an orbit label for rational primes"]}
    return data

def check(path, evaluation_path=EVAL):
    global CHECKS
    CHECKS = 0
    got = read(path)
    admissible_tree(got)
    digest = got.pop("payload_sha256")
    assert type(digest) is str and hashlib.sha256(canonical(got)).hexdigest() == digest, "payload hash"
    want = reconstruct()
    same(got, want)
    evaluation(evaluation_path)
    return {"assertions": CHECKS, "finite_levels": len(want["finite_levels"]), "residue_points": sum(r["points"] for r in want["finite_levels"]), "displacements": len(want["displacements"]), "payload": digest}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=ROOT/"results/c394_interpolation_evidence.json")
    parser.add_argument("--evaluation", type=Path, default=EVAL)
    args = parser.parse_args()
    print("C394 independent checker PASS: "+json.dumps(check(args.evidence, args.evaluation), sort_keys=True))

if __name__ == "__main__":
    main()
