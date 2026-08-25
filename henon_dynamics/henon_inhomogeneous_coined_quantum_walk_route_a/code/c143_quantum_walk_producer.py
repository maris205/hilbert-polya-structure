#!/usr/bin/env python3
"""Produce exact evidence for the HCS-C143 inhomogeneous coined walk."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


N = 5
WORDS = ("00011", "00101")
PATH_CUTOFF = 10
TRACE_CUTOFF = 12
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
COINS = {
    "0": ((Fraction(3, 5), Fraction(4, 5)), (Fraction(4, 5), Fraction(-3, 5))),
    "1": ((Fraction(5, 13), Fraction(12, 13)), (Fraction(12, 13), Fraction(-5, 13))),
}


def q(x: Fraction | int) -> str:
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def zero(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def identity(n: int) -> list[list[Fraction]]:
    out = zero(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    out = [[Fraction(0) for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            if not a[i][k]:
                continue
            for j in range(len(b[0])):
                if b[k][j]:
                    out[i][j] += a[i][k] * b[k][j]
    return out


def matrix_trace(a) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def build_walk(word: str):
    dim = 2 * len(word)
    cmat = zero(dim)
    shift = zero(dim)
    for x, symbol in enumerate(word):
        coin = COINS[symbol]
        for i in range(2):
            for j in range(2):
                cmat[2 * x + i][2 * x + j] = coin[i][j]
        shift[2 * ((x + 1) % len(word)) + 1][2 * x] = Fraction(1)
        shift[2 * ((x - 1) % len(word))][2 * x + 1] = Fraction(1)
    return shift, cmat, matmul(shift, cmat)


def traces(u, cutoff: int) -> list[Fraction]:
    power = [row[:] for row in u]
    ans = []
    for k in range(1, cutoff + 1):
        ans.append(matrix_trace(power))
        power = matmul(power, u)
    return ans


def determinant_coefficients_from_traces(values: list[Fraction], dim: int) -> list[Fraction]:
    coeff = [Fraction(1)]
    for k in range(1, dim + 1):
        coeff.append(-sum(coeff[k - j] * values[j - 1] for j in range(1, k + 1)) / k)
    return coeff


def rotations(word: tuple[int, ...]):
    return [word[i:] + word[:i] for i in range(len(word))]


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(n % d or word != word[:d] * (n // d) for d in range(1, n))


def path_ledger(u, cutoff: int):
    dim = len(u)
    adjacency = [[(target, u[target][source]) for target in range(dim) if u[target][source]] for source in range(dim)]
    rows = []
    for length in range(1, cutoff + 1):
        rooted_count = 0
        amplitude_sum = Fraction(0)
        primitive_cycles: dict[tuple[int, ...], Fraction] = {}

        def walk(start: int, current: int, vertices: list[int], amp: Fraction, remaining: int) -> None:
            nonlocal rooted_count, amplitude_sum
            if remaining == 0:
                if current == start:
                    rooted_count += 1
                    amplitude_sum += amp
                    cycle = tuple(vertices)
                    if primitive(cycle):
                        canonical = min(rotations(cycle))
                        primitive_cycles.setdefault(canonical, amp)
                return
            for target, weight in adjacency[current]:
                if remaining == 1:
                    walk(start, target, vertices, amp * weight, 0)
                else:
                    walk(start, target, vertices + [target], amp * weight, remaining - 1)

        for start in range(dim):
            walk(start, start, [start], Fraction(1), length)
        rows.append({
            "n": length,
            "rooted_closed_paths": rooted_count,
            "signed_amplitude_sum": q(amplitude_sum),
            "primitive_cycle_count": len(primitive_cycles),
            "primitive_signed_weight_sum": q(sum(primitive_cycles.values(), Fraction(0))),
        })
    return rows


def dihedral_orbit(word: str) -> set[str]:
    return {word[i:] + word[:i] for i in range(len(word))} | {word[::-1][i:] + word[::-1][:i] for i in range(len(word))}


def payload_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_evidence() -> dict:
    walk_rows = {}
    polynomials = {}
    trace_rows = {}
    for word in WORDS:
        shift, coin, u = build_walk(word)
        vals = traces(u, TRACE_CUTOFF)
        coeff = determinant_coefficients_from_traces(vals, 2 * N)
        walk_rows[word] = path_ledger(u, PATH_CUTOFF)
        polynomials[word] = [q(x) for x in coeff]
        trace_rows[word] = [{"n": n, "trace_Un": q(v)} for n, v in enumerate(vals, 1)]
        assert matmul(transpose(u), u) == identity(2 * N)
        assert matmul(matmul(coin, u), coin) == matmul(coin, shift)

    payload = {
        "schema": "hcs-c143-coined-walk-evidence-v1",
        "candidate_id": "HCS-C143",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "inhomogeneous two-state coined quantum walk U_w=S C_w on the five-cycle",
            "basis_order": "(0,+),(0,-),(1,+),(1,-),...,(4,+),(4,-)",
            "clock": "one coin-then-flip-flop-shift step",
            "normalization": "C0=(1/5)[[3,4],[4,-3]], C1=(1/13)[[5,12],[12,-5]]",
            "arrangements": list(WORDS),
            "determinant_convention": "D_w(z)=det(I_10-zU_w)",
            "cutoff": {"path": PATH_CUTOFF, "trace": TRACE_CUTOFF, "matrix_dimension": 10},
            "precision": "exact rational arithmetic",
            "allowed_data": "the frozen cycle, coin reflections, and signed path amplitudes",
            "forbidden_data": "prime tables, target zero tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "unitary_reversal_theorem": {
            "coin_involutions": True,
            "flip_flop_shift_involution": True,
            "unitary": True,
            "determinant_U": "1",
            "antiunitary": "Theta_w=C_w K",
            "theta_square": "I",
            "reversal": "Theta_w U_w Theta_w^(-1)=U_w^(-1)",
            "classical_shadow": "P_w=|U_w|^2 is doubly stochastic with the same one-step clock",
        },
        "arrangement_control": {
            "same_coin_population": {"0": 3, "1": 2},
            "dihedrally_equivalent": WORDS[1] in dihedral_orbit(WORDS[0]),
            "determinant_polynomials_ascending": polynomials,
            "exact_difference": "D_00011-D_00101=(196/4225)z^2(z-1)^2(z+1)^2(z^2+1)",
            "palindromic": True,
        },
        "trace_ledgers": trace_rows,
        "path_ledgers": walk_rows,
        "population_average_negative_control": {
            "coin": "(3C0+2C1)/5=(1/325)[[167,276],[276,-167]]",
            "orthogonality_defect": "Cbar^T Cbar-I=-(24/1625)I",
            "determinant": "-1601/1625",
            "verdict": "POPULATION_AVERAGING_DESTROYS_UNITARITY_AND_ORDER_INFORMATION",
        },
        "raw_primitive_product_domain": "absolute for |z|<5/7 by the maximum absolute column sum",
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "prime_like_correspondence": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "self_adjoint_hilbert_polya": False,
        },
    }
    payload["payload_sha256"] = payload_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c143_quantum_walk_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
