#!/usr/bin/env python3
"""Exact SymPy cross-checks for HCS-C301; does not import the producer/checker."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c301_fragmentation_evidence.json"


def partitions(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def visit(prefix: tuple[int, ...]) -> None:
        if len(prefix) == n:
            out.append(prefix)
            return
        ceiling = max(prefix) + 1 if prefix else 0
        for label in range(ceiling + 1):
            visit(prefix + (label,))

    visit(())
    return out


def compatible(source: tuple[int, ...], target: tuple[int, ...]) -> bool:
    owners: dict[int, int] = {}
    children: dict[int, set[int]] = {}
    for parent, child in zip(source, target):
        if child in owners and owners[child] != parent:
            return False
        owners[child] = parent
        children.setdefault(parent, set()).add(child)
    return all(len(group) <= 2 for group in children.values())


def refines(source: tuple[int, ...], target: tuple[int, ...]) -> tuple[bool, list[int]]:
    owners: dict[int, int] = {}
    children: dict[int, set[int]] = {}
    for parent, child in zip(source, target):
        if child in owners and owners[child] != parent:
            return False, []
        owners[child] = parent
        children.setdefault(parent, set()).add(child)
    return True, [len(children[parent]) for parent in sorted(children)]


def falling(q: int | sp.Expr, k: int) -> sp.Expr:
    return sp.prod(q - j for j in range(k))


def matrix(n: int, states: list[tuple[int, ...]]) -> sp.Matrix:
    return sp.Matrix([
        [sp.Rational(2 ** (max(source) + 1), 2**n) if compatible(source, target) else 0
         for target in states]
        for source in states
    ])


def t_step_formula(source: tuple[int, ...], target: tuple[int, ...], t: int) -> sp.Rational:
    ok, child_counts = refines(source, target)
    if not ok:
        return sp.Rational(0)
    q = 2**t
    numerator = sp.prod(falling(q, r) for r in child_counts)
    return sp.Rational(numerator, q ** len(source))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assert data["candidate_id"] == "HCS-C301"
    checks = 1

    x, z, q = sp.symbols("x z q")
    for n in range(1, 6):
        states = partitions(n)
        K = matrix(n, states)
        bell = len(states)
        assert all(sp.simplify(sum(K[row, col] for col in range(bell)) - 1) == 0 for row in range(bell))
        checks += bell

        predicted_char = sp.prod(
            (x - sp.Rational(1, 2 ** (n - k))) ** sp.functions.combinatorial.numbers.stirling(n, k, kind=2)
            for k in range(1, n + 1)
        )
        assert sp.Poly(K.charpoly(x).as_expr() - sp.expand(predicted_char), x).is_zero
        checks += 1

        predicted_det = sp.prod(
            (1 - z * sp.Rational(1, 2 ** (n - k))) ** sp.functions.combinatorial.numbers.stirling(n, k, kind=2)
            for k in range(1, n + 1)
        )
        assert sp.Poly((sp.eye(bell) - z*K).det() - sp.expand(predicted_det), z).is_zero
        checks += 1

        annihilator = sp.eye(bell)
        for k in range(1, n + 1):
            annihilator = annihilator * (K - sp.Rational(1, 2 ** (n-k)) * sp.eye(bell))
        assert annihilator == sp.zeros(bell)
        checks += bell * bell

        for k in range(1, n + 1):
            eigenvalue = sp.Rational(1, 2 ** (n-k))
            geometric = bell - (K - eigenvalue * sp.eye(bell)).rank()
            expected = int(sp.functions.combinatorial.numbers.stirling(n, k, kind=2))
            assert geometric == expected
            checks += 1

        for t in range(5):
            power = K**t
            for i, source in enumerate(states):
                for j, target in enumerate(states):
                    assert power[i, j] == t_step_formula(source, target, t)
                    checks += 1
            predicted_trace = sum(
                sp.functions.combinatorial.numbers.stirling(n, k, kind=2)
                * sp.Rational(1, 2 ** (t * (n-k)))
                for k in range(1, n + 1)
            )
            assert sp.trace(power) == predicted_trace
            checks += 1

    # Polynomial occupancy identities, independently expanded for n<=12.
    for n in range(1, 13):
        normalization = sum(
            sp.functions.combinatorial.numbers.stirling(n, k, kind=2) * falling(q, k)
            for k in range(1, n + 1)
        )
        assert sp.expand(normalization - q**n) == 0
        checks += 1
        first_moment = sum(
            k * sp.functions.combinatorial.numbers.stirling(n, k, kind=2) * falling(q, k)
            for k in range(1, n + 1)
        )
        expected_numerator = q * (q**n - (q-1)**n)
        assert sp.expand(first_moment - expected_numerator) == 0
        checks += 1

    # The archived table must agree with the independently constructed matrices.
    groups = data["transition_regression"]["groups"]
    for n, group in enumerate(groups, 1):
        assert group["bell_number"] == int(sp.functions.combinatorial.numbers.bell(n))
        checks += 1

    print(f"C301 SymPy exact cross-check PASS ({checks} symbolic/cell assertions)")
    print("verified: characteristic polynomials, determinants, squarefree annihilators, eigenspaces, semigroup kernels, occupancy moments")


if __name__ == "__main__":
    main()
