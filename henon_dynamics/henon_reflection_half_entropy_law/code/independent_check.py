#!/usr/bin/env python3
"""Independent transfer-matrix and brute census for HCS-P59."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT / "results" / "c59_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c59_independent_check.json"

A = sp.Matrix(((1, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 1), (0, 1, 0, 0)))
RHO = (0, 2, 1, 3)


def sha(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def fib(n: int) -> int:
    return int(sp.fibonacci(n))


def luc(n: int) -> int:
    return int(sp.lucas(n))


def ccos(n: int) -> int:
    return (1, 0, -1, 0)[n % 4]


def csin(n: int) -> int:
    return (0, 1, 0, -1)[n % 4]


def odd_fixed(n: int) -> int:
    m = (n - 1) // 2
    left = (0, 3)
    right = (0, 2)
    direct = sum(int((A**m)[i, j]) for i in left for j in right)
    formula = fib(m + 2)
    if direct != formula:
        raise ArithmeticError("independent odd fixed-word formula failed")
    return direct


def even_fixed(n: int, edge_axis: bool) -> int:
    m = n // 2
    if edge_axis:
        direct = sum(int((A**m)[i, j]) for i in (0, 3) for j in (0, 3))
        formula = luc(m)
    else:
        direct = sum(int((A ** (m - 1))[i, j]) for i in (0, 1) for j in (0, 2))
        formula = fib(m) + (2 * luc(m) - 4 * ccos(m) - 2 * csin(m)) // 5
    if direct != formula:
        raise ArithmeticError("independent even fixed-word formula failed")
    return direct


def fixed(n: int, edge_axis: bool) -> int:
    return odd_fixed(n) if n % 2 else even_fixed(n, edge_axis)


def row_formula(n: int) -> dict[str, int]:
    divs = [int(d) for d in sp.divisors(n)]
    closed = lambda d: int(sp.trace(A**d))
    cycle_numerator = sum(int(sp.mobius(n // d)) * closed(d) for d in divs)
    cycles = cycle_numerator // n
    if n % 2:
        reversible = sum(int(sp.mobius(n // d)) * fixed(d, True) for d in divs)
        ee = vv = 0
    else:
        ee_fixed = sum(int(sp.mobius(n // d)) * fixed(d, True) for d in divs)
        vv_fixed = sum(int(sp.mobius(n // d)) * fixed(d, False) for d in divs)
        ee, vv = ee_fixed // 2, vv_fixed // 2
        reversible = ee + vv
    return {
        "period": n,
        "primitive_cycles": cycles,
        "reversible_cycles": reversible,
        "edge_edge_cycles": ee,
        "vertex_vertex_cycles": vv,
    }


def rots(w: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(w[i:] + w[:i] for i in range(len(w)))


def primitive(w: tuple[int, ...]) -> bool:
    n = len(w)
    return all(not (n % d == 0 and w == w[:d] * (n // d)) for d in range(1, n))


def brute(n: int) -> dict[str, int]:
    found: set[tuple[int, ...]] = set()
    for word in itertools.product(range(4), repeat=n):
        if primitive(word) and all(A[word[i], word[(i + 1) % n]] for i in range(n)):
            found.add(min(rots(word)))
    shifts: list[int] = []
    for word in found:
        reflected = tuple(RHO[word[-i % n]] for i in range(n))
        for k in range(n):
            if reflected[k:] + reflected[:k] == word:
                shifts.append(k)
                break
    ee = sum(k % 2 == 0 for k in shifts) if n % 2 == 0 else 0
    vv = sum(k % 2 == 1 for k in shifts) if n % 2 == 0 else 0
    return {
        "period": n,
        "primitive_cycles": len(found),
        "reversible_cycles": len(shifts),
        "edge_edge_cycles": ee,
        "vertex_vertex_cycles": vv,
    }


def reconstruct() -> dict[str, object]:
    z = sp.symbols("z")
    if sp.factor(A.charpoly(z).as_expr()) != (z**2 + 1) * (z**2 - z - 1):
        raise ArithmeticError("independent characteristic polynomial failed")
    formulas = [row_formula(n) for n in range(1, 33)]
    brute_rows = [brute(n) for n in range(1, 13)]
    if brute_rows != formulas[:12]:
        raise ArithmeticError("independent brute census failed")
    return {
        "candidate_id": "HCS-P59",
        "formula_rows_1_to_32": formulas,
        "brute_rows_1_to_12": brute_rows,
        "charpoly": "(z^2+1)(z^2-z-1)",
        "full_entropy": "log(phi)",
        "reflection_entropy": "(1/2)log(phi)",
    }


def compare(result: dict[str, object], certificate: dict[str, object]) -> None:
    expected = {
        "candidate_id": certificate["candidate_id"],
        "formula_rows_1_to_32": certificate["formula_rows_1_to_32"],
        "brute_rows_1_to_12": certificate["brute_rows_1_to_16"][:12],
        "charpoly": certificate["characteristic_polynomial"],
        "full_entropy": certificate["entropy_theorem"]["full_primitive_entropy"],
        "reflection_entropy": certificate["entropy_theorem"]["reflection_primitive_entropy"],
    }
    if result != expected:
        raise ArithmeticError("independent result disagrees with primary certificate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = reconstruct()
    compare(result, certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "HCS-P59", "check": True, "result_sha256": sha(result)}, sort_keys=True))


if __name__ == "__main__":
    main()
