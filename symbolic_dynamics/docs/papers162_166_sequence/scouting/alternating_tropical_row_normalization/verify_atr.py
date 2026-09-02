#!/usr/bin/env python3
"""Exact verifier for alternating tropical row-normalization dynamics.

The literal state is an n by n matrix over {0,...,q-1}.  One update
subtracts the minimum of each row and then transposes.  This verifier does
not import any author-side implementation.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import comb


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


A = Audit()


def transpose(x: tuple[int, ...], n: int) -> tuple[int, ...]:
    return tuple(x[j * n + i] for i in range(n) for j in range(n))


def row_reduce(x: tuple[int, ...], n: int) -> tuple[int, ...]:
    out: list[int] = []
    for i in range(n):
        row = x[i * n : (i + 1) * n]
        m = min(row)
        out.extend(v - m for v in row)
    return tuple(out)


def step(x: tuple[int, ...], n: int) -> tuple[int, ...]:
    return transpose(row_reduce(x, n), n)


def column_reduced(x: tuple[int, ...], n: int) -> bool:
    return all(min(x[i * n + j] for i in range(n)) == 0 for j in range(n))


def core(x: tuple[int, ...], n: int) -> bool:
    return column_reduced(x, n) and all(
        min(x[i * n : (i + 1) * n]) == 0 for i in range(n)
    )


def symmetric(x: tuple[int, ...], n: int) -> bool:
    return x == transpose(x, n)


def poly_mul(p: Counter[int], r: Counter[int]) -> Counter[int]:
    ans: Counter[int] = Counter()
    for i, a in p.items():
        for j, b in r.items():
            ans[i + j] += a * b
    return ans


def one_step_fibre_poly(y: tuple[int, ...], n: int, q: int) -> Counter[int]:
    if not column_reduced(y, n):
        return Counter()
    ans: Counter[int] = Counter({sum(y): 1})
    for i in range(n):
        ceiling = q - 1 - max(y[j * n + i] for j in range(n))
        factor = Counter({n * r: 1 for r in range(ceiling + 1)})
        ans = poly_mul(ans, factor)
    return ans


def two_step_fibre_poly(c: tuple[int, ...], n: int, q: int) -> Counter[int]:
    if not core(c, n):
        return Counter()
    ceilings = [
        q - 1 - max(c[i * n + j] for i in range(n)) for j in range(n)
    ]
    ans: Counter[int] = Counter()
    for s in product(*(range(h + 1) for h in ceilings)):
        # B=C+column-potential must still be row reduced.
        if any(
            not any(c[i * n + j] == 0 and s[j] == 0 for j in range(n))
            for i in range(n)
        ):
            continue
        term: Counter[int] = Counter({sum(c) + n * sum(s): 1})
        for i in range(n):
            ceiling = q - 1 - max(c[i * n + j] + s[j] for j in range(n))
            term = poly_mul(
                term, Counter({n * r: 1 for r in range(ceiling + 1)})
            )
        ans.update(term)
    return ans


def recurrent_formula(n: int, q: int) -> int:
    return sum(
        (-1) ** (i + j)
        * comb(n, i)
        * comb(n, j)
        * (q - 1) ** (n * (i + j) - i * j)
        * q ** ((n - i) * (n - j))
        for i in range(n + 1)
        for j in range(n + 1)
    )


def fixed_formula(n: int, q: int) -> int:
    N = n * (n + 1) // 2
    return sum(
        (-1) ** i
        * comb(n, i)
        * (q - 1) ** (N - (n - i) * (n - i + 1) // 2)
        * q ** ((n - i) * (n - i + 1) // 2)
        for i in range(n + 1)
    )


def image_one_formula(n: int, q: int) -> int:
    return (q**n - (q - 1) ** n) ** n


def exhaustive_box(n: int, q: int, weighted: bool) -> tuple[int, ...]:
    states = list(product(range(q), repeat=n * n))
    image1: set[tuple[int, ...]] = set()
    image2: set[tuple[int, ...]] = set()
    fibres1: dict[tuple[int, ...], int] = defaultdict(int)
    fibres2: dict[tuple[int, ...], int] = defaultdict(int)
    weighted1: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    weighted2: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    depth = Counter()

    for x in states:
        x1 = step(x, n)
        x2 = step(x1, n)
        x3 = step(x2, n)
        x4 = step(x3, n)
        image1.add(x1)
        image2.add(x2)
        fibres1[x1] += 1
        fibres2[x2] += 1
        if weighted:
            weighted1[x1][sum(x)] += 1
            weighted2[x2][sum(x)] += 1

        A.check(column_reduced(x1, n), (n, q, x, "first image"))
        A.check(core(x2, n), (n, q, x, "second image"))
        A.check(x3 == transpose(x2, n), (n, q, x, "third iterate"))
        A.check(x4 == x2, (n, q, x, "T4=T2"))
        A.check((step(x2, n) == x2) == symmetric(x2, n), (n, q, x, "fixed core"))

        d = 0 if core(x, n) else 1 if core(x1, n) else 2
        depth[d] += 1
        A.check(core((x, x1, x2)[d], n), (n, q, x, "depth landing", d))
        if d:
            A.check(not core((x, x1)[d - 1], n), (n, q, x, "depth minimal", d))

    recurrent = sum(core(x, n) for x in states)
    fixed = sum(core(x, n) and symmetric(x, n) for x in states)
    depth_le_one = sum(one_step_fibre_poly(y, n, q).total() for y in states if core(y, n))

    A.check(len(image1) == image_one_formula(n, q), (n, q, "image one count"))
    A.check(len(image2) == recurrent_formula(n, q), (n, q, "image two count"))
    A.check(recurrent == recurrent_formula(n, q), (n, q, "recurrent IE"))
    A.check(fixed == fixed_formula(n, q), (n, q, "fixed IE"))
    A.check(depth[0] == recurrent, (n, q, "depth zero"))
    A.check(depth[0] + depth[1] == depth_le_one, (n, q, "depth <=1"))
    A.check(depth[2] == q ** (n * n) - depth_le_one, (n, q, "depth two"))
    A.check((recurrent - fixed) % 2 == 0, (n, q, "two-cycle parity"))

    for y in states:
        predicted1 = one_step_fibre_poly(y, n, q)
        predicted2 = two_step_fibre_poly(y, n, q)
        A.check(predicted1.total() == fibres1[y], (n, q, y, "one fibre"))
        A.check(predicted2.total() == fibres2[y], (n, q, y, "two fibre"))
        A.check(bool(predicted1) == column_reduced(y, n), (n, q, y, "one support"))
        A.check(bool(predicted2) == core(y, n), (n, q, y, "two support"))
        if weighted:
            A.check(predicted1 == weighted1[y], (n, q, y, "one weighted"))
            A.check(predicted2 == weighted2[y], (n, q, y, "two weighted"))

    A.check(sum(fibres1.values()) == q ** (n * n), (n, q, "one mass"))
    A.check(sum(fibres2.values()) == q ** (n * n), (n, q, "two mass"))
    A.check(max(depth) == 2, (n, q, "sharp height"))
    return (
        len(states),
        len(image1),
        recurrent,
        fixed,
        depth[0],
        depth[1],
        depth[2],
    )


def structural_checks() -> None:
    # Inclusion--exclusion formulas remain integral and respect the orbit ledger.
    for n in range(2, 11):
        for q in range(2, 11):
            r = recurrent_formula(n, q)
            f = fixed_formula(n, q)
            i1 = image_one_formula(n, q)
            A.check(0 < f <= r <= i1 <= q ** (n * n), (n, q, "count order"))
            A.check((r - f) % 2 == 0, (n, q, "orbit integrality"))
            A.check(i1 == (q**n - (q - 1) ** n) ** n, (n, q, "image factor"))

    # Boundary sentinels: each excluded lower bound destroys sharp height two.
    for q in range(2, 8):
        x = (q - 1,)
        A.check(step(x, 1) == (0,), (q, "n=1 collapse"))
    for n in range(1, 8):
        x = (0,) * (n * n)
        A.check(step(x, n) == x, (n, "q=1 singleton"))

    # Explicit sharp witness in every theorem box.
    for n in range(2, 11):
        for q in range(2, 11):
            x = tuple(0 if j == 0 else 1 for _i in range(n) for j in range(n))
            A.check(not core(x, n), (n, q, "witness noncore"))
            A.check(not core(step(x, n), n), (n, q, "witness depth >1"))
            A.check(core(step(step(x, n), n), n), (n, q, "witness depth 2"))


def main() -> None:
    boxes = [(2, 2, True), (2, 3, True), (2, 4, True),
             (3, 2, True), (3, 3, False), (4, 2, False)]
    print("ALTERNATING_TROPICAL_ROW_NORMALIZATION_SCOUT_V1")
    for n, q, weighted in boxes:
        stats = exhaustive_box(n, q, weighted)
        print(
            "box",
            f"n={n}",
            f"q={q}",
            f"states={stats[0]}",
            f"image1={stats[1]}",
            f"recurrent={stats[2]}",
            f"fixed={stats[3]}",
            f"depths={stats[4]},{stats[5]},{stats[6]}",
            f"weighted={int(weighted)}",
        )
    structural_checks()
    print(f"assertions={A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
