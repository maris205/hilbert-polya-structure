#!/usr/bin/env python3
"""Separate SymPy reconstruction of C185 identities and finite sentinels."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c185_brockett_evidence.json"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(
        json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def check(condition: bool, message: str, count: list[int]) -> None:
    count[0] += 1
    if not condition:
        raise AssertionError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    payload = json.loads(args.evidence.read_text())
    count = [0]
    check(payload["payload_sha256"] == canonical_hash(payload), "canonical hash", count)

    h11, h22, h33, h12, h13, h23 = sp.symbols("h11 h22 h33 h12 h13 h23", real=True)
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
    h = sp.Matrix([[h11, h12, h13], [h12, h22, h23], [h13, h23, h33]])
    target = sp.diag(n1, n2, n3)
    generator = h * target - target * h
    velocity = h * generator - generator * h
    derivative = sp.trace(velocity * target)
    norm_sq = sum(generator[i, j] ** 2 for i in range(3) for j in range(3))
    check(sp.simplify(derivative - norm_sq) == 0, "symbolic Lyapunov identity", count)
    check(sp.simplify(generator + generator.T) == sp.zeros(3), "symbolic skew generator", count)
    check(sp.simplify(velocity - velocity.T) == sp.zeros(3), "symbolic symmetric velocity", count)
    for power in range(1, 6):
        derivative_trace_power = power * sp.trace((h ** (power - 1)) * velocity)
        check(sp.simplify(derivative_trace_power) == 0, f"isospectral trace power {power}", count)

    d1, d2, d3, e = sp.symbols("d1 d2 d3 e", real=True)
    x12, x13, x23 = sp.symbols("x12 x13 x23", real=True)
    d = sp.diag(d1, d2, d3)
    k = sp.Matrix([[0, x12, x13], [x12, 0, x23], [x13, x23, 0]])
    he = d + e * k
    nonlinear = he * (he * target - target * he) - (he * target - target * he) * he
    linear = nonlinear.diff(e).subs(e, 0)
    expected = d * (k * target - target * k) - (k * target - target * k) * d
    check(sp.simplify(linear - expected) == sp.zeros(3), "full linearization", count)
    for i, j, x in [(0, 1, x12), (0, 2, x13), (1, 2, x23)]:
        rate = (d[i, i] - d[j, j]) * (target[j, j] - target[i, i])
        check(sp.simplify(linear[i, j] - rate * x) == 0, f"pair rate {i},{j}", count)

    rows = payload["permutation_rows"]
    cursor = 0
    mode_count = 0
    for n in range(2, 8):
        source = tuple(range(1, n + 1))
        nu = [sp.Integer(i * i) for i in range(1, n + 1)]
        for perm in permutations(source):
            row = rows[cursor]
            cursor += 1
            inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
            check(row["inversions"] == inv, f"inversion n={n} p={perm}", count)
            check(row["morse_index_of_minus_height"] == inv, f"Morse n={n} p={perm}", count)
            symbolic_height = sum(sp.Integer(perm[i]) * nu[i] for i in range(n))
            check(row["height_Tr_DN"] == int(symbolic_height), f"height n={n} p={perm}", count)
            for actual in row["pair_modes"]:
                i, j, rate, sign = actual
                symbolic_rate = (sp.Integer(perm[i - 1]) - sp.Integer(perm[j - 1])) * (nu[j - 1] - nu[i - 1])
                check(rate == int(symbolic_rate), f"mode rate n={n} p={perm} i={i} j={j}", count)
                check(sign == ("unstable" if symbolic_rate > 0 else "stable"), f"mode sign n={n} p={perm} i={i} j={j}", count)
                mode_count += 1
    check(cursor == 5912, "permutation rows consumed", count)
    check(mode_count == 118004, "pair modes consumed", count)

    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    rotation = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    repeated_target = sp.diag(1, 1, 4)
    rotated_h = rotation * sp.diag(1, 2, 3) * rotation.T
    check(rotated_h[0, 1] != 0, "boundary non-diagonal", count)
    check(rotated_h * repeated_target - repeated_target * rotated_h == sp.zeros(3), "boundary equilibrium", count)
    check(payload["boundary_controls"]["repeated_target_spectrum"]["zero_pair_modes"] == 1, "boundary zero mode", count)
    check(payload["route_a_verdict"]["A0"] == "A0_FAIL", "A0", count)
    check(payload["route_a_verdict"]["A1"] == "A1_FAIL", "A1", count)
    check(payload["route_a_verdict"]["A4"] == "A4_FORMAL_HINT", "A4", count)
    print(json.dumps({"status": "C185_SYMPY_PASS", "checks": count[0], "pair_modes": mode_count, "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
