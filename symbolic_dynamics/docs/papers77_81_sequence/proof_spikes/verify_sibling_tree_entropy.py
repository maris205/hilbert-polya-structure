#!/usr/bin/env python3
"""Exact controls for the sibling-synchronized golden-mean tree shifts.

The independent system X allows 000,001,010,011,100 at every parent and
the sibling-synchronized system Y allows 000,011,100.  Bits in a triple are
(parent,left child,right child).  We compare literal finite-tree enumeration,
root-conditioned recurrences, the all-height square identity, and certified
entropy-series brackets.
"""

import math
from decimal import Decimal, getcontext


INDEPENDENT = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0)}
SYNCHRONIZED = {(0, 0, 0), (0, 1, 1), (1, 0, 0)}


def literal_counts(height, allowed):
    """Enumerate all labels on a heap-indexed complete tree of given height."""

    vertices = 2**height - 1
    root_counts = [0, 0]
    for state in range(1 << vertices):
        legal = True
        for parent in range(2 ** (height - 1) - 1):
            triple = (
                (state >> parent) & 1,
                (state >> (2 * parent + 1)) & 1,
                (state >> (2 * parent + 2)) & 1,
            )
            if triple not in allowed:
                legal = False
                break
        if legal:
            root_counts[state & 1] += 1
    return tuple(root_counts)


def recurrence_rows(max_height=14):
    # Height one consists only of the root.
    xa = xb = ya = yb = 1
    rows = []
    for height in range(1, max_height + 1):
        assert xa == ya**2 and xb == yb**2
        x_total = xa + xb
        y_total = ya + yb
        discrepancy = math.log(x_total) - 2 * math.log(y_total)
        assert -math.log(2) <= discrepancy <= 1e-12
        rows.append((height, xa, xb, ya, yb, x_total, y_total))
        xa, xb = (xa + xb) ** 2, xa**2
        ya, yb = ya**2 + yb**2, ya**2
    return rows


def entropy_bracket(terms=60):
    """Bracket h(Y) using 3/4 <= g(r_n) <= 1 for the series tail."""

    getcontext().prec = 80
    ratio = Decimal(1) / Decimal(2)
    partial = Decimal(1) / Decimal(2) * Decimal(2).ln()
    for index in range(1, terms + 1):
        assert Decimal(1) / Decimal(2) <= ratio <= Decimal(2) / Decimal(3)
        factor = 1 - 2 * ratio + 3 * ratio * ratio
        assert Decimal(3) / Decimal(4) <= factor <= Decimal(1)
        partial += factor.ln() / (Decimal(2) ** (index + 1))
        ratio = (1 - 2 * ratio + 2 * ratio * ratio) / factor

    remaining_weight = Decimal(1) / (Decimal(2) ** (terms + 1))
    lower = partial + (Decimal(3) / Decimal(4)).ln() * remaining_weight
    upper = partial
    return lower, upper


def check_branch_language():
    # Both local rule sets induce exactly 0->0, 0->1, 1->0 on either child.
    golden_edges = {(0, 0), (0, 1), (1, 0)}
    for allowed in (INDEPENDENT, SYNCHRONIZED):
        left_edges = {(parent, left) for parent, left, _ in allowed}
        right_edges = {(parent, right) for parent, _, right in allowed}
        assert left_edges == golden_edges
        assert right_edges == golden_edges


def main():
    check_branch_language()
    rows = recurrence_rows()
    literal_checks = 0
    for height in range(1, 5):
        assert literal_counts(height, INDEPENDENT) == rows[height - 1][1:3]
        assert literal_counts(height, SYNCHRONIZED) == rows[height - 1][3:5]
        literal_checks += 2
    lower, upper = entropy_bracket()
    assert upper - lower < Decimal("1e-18")
    print("PASS identical left/right golden-mean branch transitions")
    print(f"PASS literal finite-tree/recurrence equalities: {literal_checks}")
    print(f"PASS all-height square identities through height {len(rows)}")
    print("initial totals (height, |X_n|, |Y_n|):")
    for row in rows[:6]:
        print((row[0], row[5], row[6]))
    print(f"certified decimal bracket h(Y): [{lower:.20f}, {upper:.20f}]")
    print(f"corresponding h(X)=2h(Y): [{2*lower:.20f}, {2*upper:.20f}]")


if __name__ == "__main__":
    main()
