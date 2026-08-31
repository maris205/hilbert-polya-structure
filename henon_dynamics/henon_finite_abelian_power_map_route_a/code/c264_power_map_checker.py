#!/usr/bin/env python3
"""Independent direct-enumeration checker for HCS-C264 (imports no producer)."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c264_power_map_evidence.json"
SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]


def payload_hash(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def elems(ns):
    return list(itertools.product(*(range(n) for n in ns))) if ns else [()]


def step(x, ns, d):
    return tuple(d * v % n for v, n in zip(x, ns))


def iterate(x, ns, d, j):
    for _ in range(j): x = step(x, ns, d)
    return x


def sig(x, ns, d):
    seen, path = {}, []
    while x not in seen:
        seen[x] = len(path); path.append(x); x = step(x, ns, d)
    return seen[x], len(path) - seen[x]


def quick(data):
    a = 0
    assert data["schema"] == "hcs-c264-finite-abelian-power-map-v1"; a += 1
    assert data["candidate_id"] == "HCS-C264"; a += 1
    assert data["source_commit"] == SOURCE and data["fixed_epoch"] == 1788048000; a += 2
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"; a += 1
    assert data["evaluator"]["sha256"] == EVAL; a += 1
    assert data["route_a"]["tuple"] == TUPLE; a += 1
    assert data["route_a"]["overall"] == "ROUTE_A_PARTIAL"; a += 1
    assert data["route_a"]["route_b_invocation_allowed"] is False; a += 1
    assert all(v is False for v in data["scope_flags"].values()); a += len(data["scope_flags"])
    assert data["payload_sha256"] == payload_hash(data); a += 1
    cases = data["regression"]["cases"]
    counts = data["regression"]["counts"]
    assert len(cases) == 646 == counts["cases"]; a += 2
    assert counts["group_types"] == 34 and counts["d_values"] == 19; a += 2
    assert sorted(set(c["d"] for c in cases)) == list(range(19)); a += 1
    assert len({(tuple(c["group"]), c["d"]) for c in cases}) == len(cases); a += 1
    for c in cases:
        ns, d = c["group"], c["d"]
        assert c["order"] == math.prod(ns); a += 1
        assert all(n >= 2 for n in ns); a += 1
        assert all(ns[i + 1] % ns[i] == 0 for i in range(len(ns) - 1)); a += 1
        assert len(c["a_factors"]) == len(ns) == len(c["b_factors"]); a += 1
        assert all(x * y == n for x, y, n in zip(c["a_factors"], c["b_factors"], ns)); a += 1
        ledger = c["koopman_characteristic_ledger"]
        assert ledger["zero_multiplicity"] == c["order"] - c["periodic_points"]; a += 1
        assert ledger["cycle_factors"] == c["cycle_counts"]; a += 1
        assert sum(int(m) * z for m, z in c["zero_jordan_blocks"].items()) == ledger["zero_multiplicity"]; a += 1
        assert sum(int(m) * z for m, z in c["cycle_counts"].items()) == c["periodic_points"]; a += 1
        if d == 0:
            assert c["boundary"] == "constant_identity_map"; a += 1
            assert c["cycle_counts"] == {"1": 1}; a += 1
            assert c["image_ranks"] == [c["order"], 1, 1]; a += 1
            assert c["zero_jordan_blocks"] == ({"1": c["order"] - 1} if c["order"] > 1 else {}); a += 1
        else:
            assert all(math.gcd(x, d) == 1 for x in c["a_factors"]); a += 1
            assert all(y == 1 or all(p in set(_prime_divisors(d)) for p in _prime_divisors(y)) for y in c["b_factors"]); a += 1
            assert c["periodic_points"] == math.prod(c["a_factors"]); a += 1
            ranks = c["image_ranks"]
            assert ranks[-1] == ranks[-2] == c["periodic_points"]; a += 1
            for j, z in c["zero_jordan_blocks"].items():
                j = int(j); assert z == ranks[j - 1] - 2 * ranks[j] + ranks[j + 1]; a += 1
    return a


def _prime_divisors(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        p += 1
    if n > 1: out.append(n)
    return out


def full(data):
    assertions = quick(data)
    total_elements = 0
    for c in data["regression"]["cases"]:
        ns, d = c["group"], c["d"]
        xs = elems(ns); total_elements += len(xs)
        signatures = [sig(x, ns, d) for x in xs]
        observed = {}
        for tail, period in signatures:
            observed[f"{tail}:{period}"] = observed.get(f"{tail}:{period}", 0) + 1
        assert observed == c["observed_tail_period_counts"]; assertions += len(xs)
        raw = ";".join(",".join(map(str, x)) + ">" + ",".join(map(str, step(x, ns, d))) for x in xs)
        assert hashlib.sha256(raw.encode()).hexdigest() == c["map_sha256"]; assertions += 1
        periodic = sum(t == 0 for t, _ in signatures)
        assert periodic == c["periodic_points"]; assertions += 1
        direct_cycles = {}
        for m in sorted({period for tail, period in signatures if tail == 0}):
            direct_cycles[str(m)] = sum(tail == 0 and period == m for tail, period in signatures) // m
        assert direct_cycles == c["cycle_counts"]; assertions += periodic
        for m, fixed in c["fixed_counts"].items():
            direct = sum(iterate(x, ns, d, int(m)) == x for x in xs)
            assert direct == fixed; assertions += len(xs)
        for j, layer in c["tail_layers_per_cycle_vertex"].items():
            direct = sum(t == int(j) for t, _ in signatures)
            assert direct == periodic * layer; assertions += len(xs)
        for j, rank in enumerate(c["image_ranks"]):
            direct = len({iterate(x, ns, d, j) for x in xs})
            assert direct == rank; assertions += len(xs)
        if d == 0:
            assert all(step(x, ns, d) == tuple(0 for _ in ns) for x in xs); assertions += len(xs)
        else:
            for n, aa, bb in zip(ns, c["a_factors"], c["b_factors"]):
                assert aa * bb == n and math.gcd(aa, d) == 1; assertions += 2
                assert math.gcd(aa, bb) == 1; assertions += 1
    counts = data["regression"]["counts"]
    assert counts["enumerated_group_elements"] == total_elements; assertions += 1
    assert counts["constant_boundary_cases"] == 34 and counts["identity_cases"] == 34; assertions += 2
    return assertions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    n = quick(data) if args.quick else full(data)
    print(f"C264 independent checker: PASS ({n} assertions; mode={'quick' if args.quick else 'full'})")


if __name__ == "__main__":
    main()
