#!/usr/bin/env python3
"""Independent exact checks for plane-partition layer stripping.

This file implements the literal map directly.  It imports no verifier from
the paper portfolio or from another scout.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def transitive_closure(n: int, covers: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
    for i, j in covers:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return tuple((i, j) for i in range(n) for j in range(n) if i != j and reach[i][j])


def poset(name: str, n: int, covers: tuple[tuple[int, int], ...]) -> tuple[str, int, tuple[tuple[int, int], ...]]:
    return name, n, transitive_closure(n, covers)


def rectangle_poset(a: int, b: int) -> tuple[str, int, tuple[tuple[int, int], ...]]:
    n = a * b
    strict = []
    for i in range(a):
        for j in range(b):
            x = i * b + j
            for ii in range(i, a):
                for jj in range(j, b):
                    y = ii * b + jj
                    if x != y:
                        strict.append((x, y))
    return f"rect-{a}x{b}", n, tuple(strict)


def is_order_reversing(values: tuple[int, ...], strict: tuple[tuple[int, int], ...]) -> bool:
    return all(values[x] >= values[y] for x, y in strict)


def bounded_maps(n: int, strict: tuple[tuple[int, int], ...], cap: int) -> tuple[tuple[int, ...], ...]:
    if cap < 0:
        return ()
    return tuple(v for v in product(range(cap + 1), repeat=n) if is_order_reversing(v, strict))


def induced_count(
    n: int,
    strict: tuple[tuple[int, int], ...],
    mask: int,
    cap: int,
) -> int:
    elements = tuple(i for i in range(n) if mask >> i & 1)
    if cap < 0:
        return int(not elements)
    index = {x: i for i, x in enumerate(elements)}
    induced = tuple((index[x], index[y]) for x, y in strict if x in index and y in index)
    return len(bounded_maps(len(elements), induced, cap))


def support(values: tuple[int, ...]) -> int:
    return sum((v > 0) << i for i, v in enumerate(values))


def is_ideal(n: int, strict: tuple[tuple[int, int], ...], mask: int) -> bool:
    return all(not (mask >> y & 1) or (mask >> x & 1) for x, y in strict)


def strip(values: tuple[int, ...], t: int = 1) -> tuple[int, ...]:
    return tuple(max(v - t, 0) for v in values)


def macmahon(a: int, b: int, c: int) -> int:
    if c < 0:
        return 0
    ans = Fraction(1)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            ans *= Fraction(i + j + c - 1, i + j - 1)
    check(ans.denominator == 1, f"MacMahon integrality {a},{b},{c}")
    return ans.numerator


def audit_poset(
    name: str,
    n: int,
    strict: tuple[tuple[int, int], ...],
    max_cap: int,
) -> str:
    all_mask = (1 << n) - 1
    state_counts = []
    for c in range(max_cap + 1):
        states = bounded_maps(n, strict, c)
        state_set = set(states)
        state_counts.append(len(states))
        zero = (0,) * n
        check(zero in state_set, f"zero in carrier {name},{c}")

        for f in states:
            d = max(f, default=0)
            check(is_ideal(n, strict, support(f)), f"support ideal {name},{c},{f}")
            check(strip(f, d) == zero, f"depth endpoint {name},{c},{f}")
            if d:
                check(strip(f, d - 1) != zero, f"depth minimality {name},{c},{f}")
            check(strip(f, c) == zero, f"global absorption {name},{c},{f}")
            check(all(strip(strip(f, 1), t) == strip(f, t + 1) for t in range(c + 1)),
                  f"iterate semigroup {name},{c},{f}")

        fixed = [f for f in states if strip(f) == f]
        check(fixed == [zero], f"unique recurrent/fixed zero {name},{c}")
        height = max((max(f, default=0) for f in states), default=0)
        check(height == (c if n else 0), f"sharp height {name},{c}")

        ideals = tuple(mask for mask in range(1 << n) if is_ideal(n, strict, mask))
        for t in range(c + 2):
            fibres: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
            for f in states:
                fibres[strip(f, t)].append(f)

            image_cap = max(c - t, 0)
            expected_image = set(bounded_maps(n, strict, image_cap))
            check(set(fibres) == expected_image, f"image {name},{c},{t}")

            by_support = Counter(support(g) for g in expected_image)
            for g in expected_image:
                s = support(g)
                forced = tuple(g[i] + t if s >> i & 1 else None for i in range(n))
                for f in fibres[g]:
                    check(all(forced[i] is None or f[i] == forced[i] for i in range(n)),
                          f"forced positive part {name},{c},{t},{g},{f}")
                    check(all((s >> i & 1) or f[i] <= min(t, c) for i in range(n)),
                          f"bounded complement {name},{c},{t},{g},{f}")
                predicted = induced_count(n, strict, all_mask ^ s, min(t, c))
                check(len(fibres[g]) == predicted, f"target fibre {name},{c},{t},{g}")

            if t <= c:
                convolution = 0
                for s in ideals:
                    target_multiplicity = induced_count(n, strict, s, c - t - 1)
                    check(by_support[s] == target_multiplicity,
                          f"support multiplicity {name},{c},{t},{s}")
                    fibre_multiplicity = induced_count(n, strict, all_mask ^ s, t)
                    if target_multiplicity:
                        observed = {len(fibres[g]) for g in expected_image if support(g) == s}
                        check(observed == {fibre_multiplicity},
                              f"support-constant fibre {name},{c},{t},{s}")
                    convolution += target_multiplicity * fibre_multiplicity
                check(convolution == len(states), f"order polynomial convolution {name},{c},{t}")

    return f"poset {name} n={n} counts={','.join(map(str, state_counts))}"


def audit_rectangles() -> list[str]:
    rows = []
    for a in range(4):
        for b in range(4):
            name, n, strict = rectangle_poset(a, b)
            row = audit_poset(name, n, strict, 4)
            counts = [len(bounded_maps(n, strict, c)) for c in range(5)]
            for c, count in enumerate(counts):
                check(count == macmahon(a, b, c), f"MacMahon count {a},{b},{c}")
                states = bounded_maps(n, strict, c)
                shells = Counter(max(f, default=0) for f in states)
                for d in range(c + 1):
                    cumulative = sum(v for depth, v in shells.items() if depth <= d)
                    check(cumulative == macmahon(a, b, min(d, c)),
                          f"MacMahon cumulative depth {a},{b},{c},{d}")
            rows.append(row.replace("poset ", "rectangle "))
    return rows


def main() -> None:
    rows = ["plane-partition layer stripping independent exact scout"]
    examples = (
        poset("empty", 0, ()),
        poset("point", 1, ()),
        poset("chain4", 4, ((0, 1), (1, 2), (2, 3))),
        poset("antichain4", 4, ()),
        poset("vee3", 3, ((0, 2), (1, 2))),
        poset("lambda3", 3, ((0, 1), (0, 2))),
        poset("diamond4", 4, ((0, 1), (0, 2), (1, 3), (2, 3))),
        poset("fence4", 4, ((0, 1), (2, 1), (2, 3))),
        poset("two-chains", 4, ((0, 1), (2, 3))),
        poset("n-poset5", 5, ((0, 2), (1, 2), (1, 3), (3, 4))),
    )
    for name, n, strict in examples:
        rows.append(audit_poset(name, n, strict, 4))
    rows.extend(audit_rectangles())

    digest = sha256(("\n".join(rows) + "\n").encode()).hexdigest()
    for row in rows:
        print(row)
    print(f"ASSERTIONS {ASSERTIONS}")
    print(f"ROW_SHA256 {digest}")
    print("GENERAL_POSET_SIGNAL LEFT_SHIFT_OF_ORDER_IDEAL_MULTICHAIN")
    print("DECISION KILL_DEFINITION_LEVEL_AND_INTERNAL_COLLISION")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
