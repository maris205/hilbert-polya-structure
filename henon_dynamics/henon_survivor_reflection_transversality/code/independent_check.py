#!/usr/bin/env python3
"""Independent numerical/symbolic check for HCS-P61."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT / "results" / "c61_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c61_independent_check.json"
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
REVERSAL = (0, 2, 1, 3)
PERIODS = (1, 3, 5, 7, 9, 11)


def sha(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[k:] + word[:k] for k in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def admissible(word: tuple[int, ...]) -> bool:
    return all(ADJACENCY[word[i]][word[(i + 1) % len(word)]] for i in range(len(word)))


def reversible(word: tuple[int, ...]) -> bool:
    reflected = tuple(REVERSAL[word[-i % len(word)]] for i in range(len(word)))
    return any(reflected[k:] + reflected[:k] == word for k in range(len(word)))


def reversible_necklaces(n: int) -> int:
    necklaces = {
        min(rotations(word))
        for word in product(range(4), repeat=n)
        if admissible(word) and primitive(word) and reversible(word)
    }
    return len(necklaces)


def closure_quotients() -> dict[int, sp.Poly]:
    x = sp.symbols("x")
    q = [x, (1 - 6 * x**2) / 2]
    result: dict[int, sp.Poly] = {}
    for n in PERIODS:
        m = (n - 1) // 2
        while len(q) <= m + 1:
            q.append(sp.expand(1 - 6 * q[-1] ** 2 - q[-2]))
        closure = sp.Poly(q[m + 1] - q[m], x, domain=sp.QQ).monic()
        lower = sp.Poly(1, x, domain=sp.QQ)
        for d, quotient in result.items():
            if n % d == 0:
                lower *= quotient
        quotient, remainder = sp.div(closure, lower)
        if not remainder.is_zero:
            raise ArithmeticError("independent quotient reconstruction failed")
        result[n] = quotient.monic()
    return result


def numerical_band_count(poly: sp.Poly, n: int) -> tuple[int, list[str]]:
    lower = (17 / 144) ** 0.5
    upper = (3 / 8) ** 0.5
    roots = sp.nroots(poly.as_expr(), n=50, maxsteps=1000)
    words: list[str] = []
    for root in roots:
        value = complex(root)
        if abs(value.imag) > 1e-35:
            continue
        current = value.real
        previous = (1 - 6 * current**2) / 2
        orbit = [current]
        for _ in range(n - 1):
            following = 1 - 6 * current**2 - previous
            previous, current = current, following
            orbit.append(current)
        if all(lower < abs(coordinate) < upper for coordinate in orbit):
            words.append("".join("+" if coordinate > 0 else "-" for coordinate in orbit))
    return len(words), sorted(words)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    quotients = closure_quotients()
    rows = []
    for certified in certificate["finite_exact_rows"]:
        n = certified["period"]
        symbolic = reversible_necklaces(n)
        numerical, words = numerical_band_count(quotients[n], n)
        if symbolic != certified["physical_simple_roots"] or numerical != symbolic:
            raise ArithmeticError(f"independent physical count mismatch at n={n}")
        if words != certified["physical_sign_words"]:
            raise ArithmeticError(f"independent sign-word mismatch at n={n}")
        rows.append({
            "period": n,
            "symbolic_reversible_necklaces": symbolic,
            "numerical_survivor_roots": numerical,
            "sign_words_sha256": sha(words),
        })
    result_core = {
        "candidate_id": "HCS-P61",
        "independent_method": "Cartesian symbolic necklaces plus high-precision numerical quotient roots",
        "rows": rows,
        "all_counts_and_words_match": True,
        "claim_boundary_preserved": certificate["claim_status"]["ambient_all_period_transversality"] == "OPEN",
    }
    result = {**result_core, "result_sha256": sha(result_core), "check": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": result["candidate_id"],
        "check": result["check"],
        "result_sha256": result["result_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
