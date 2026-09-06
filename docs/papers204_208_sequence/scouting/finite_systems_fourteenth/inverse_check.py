"""New author inverse-proof checks, confined to eight original SNC/RCI boxes.

No scientific-code imports. The original producer output is read only to
compare full mapping digests and finite extrema, not to generate a map.
"""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def index(digits, p):
    result = 0
    for digit in digits:
        result = result * p + digit
    return result


def digest(mapping):
    return hashlib.sha256(json.dumps(mapping, separators=(",", ":")).encode()).hexdigest()


def snc(p):
    c = 3
    sink = p ** (2 * c)
    mapping = []
    for a in product(range(p), repeat=2 * c):
        first, second = a[:c], a[c:]
        u, w = sum(first) % p, sum(second) % p
        out = sink
        if u and w:
            # Clear both row denominators, then normalize the columns.
            upper = tuple(x * w % p for x in first)
            lower = tuple(x * u % p for x in second)
            columns = tuple((x + y) % p for x, y in zip(upper, lower))
            if all(columns):
                normalized = tuple(2 * row[j] * pow(columns[j], -1, p) % p
                                   for row in (upper, lower) for j in range(c))
                out = index(normalized, p)
        mapping.append(out)
    mapping.append(sink)
    actual = Counter(mapping)
    expected = {}
    torus = list(product(range(1, p), repeat=c))
    for upper in product(range(p), repeat=c):
        lower = tuple((2 - a) % p for a in upper)
        solutions = sum(sum(a * b for a, b in zip(upper, v)) % p == c % p
                        and sum(a * b for a, b in zip(lower, v)) % p == c % p
                        for v in torus)
        expected[index(upper + lower, p)] = (p - 1) ** 2 * solutions
    extremum = p ** (2 * c) + 1 - (p - 1) ** 2 * p ** (c - 2) * ((p - 1) ** c - (-1) ** c)
    for y in range(sink):
        check(actual[y] == expected.get(y, 0))
        check(actual[y] <= (p - 1) ** 2 * p ** (c - 1))
    check(actual[sink] == extremum)
    check(sum(expected.values()) + extremum == sink + 1)
    check([y for y, count in actual.items() if count == max(actual.values())] == [sink])
    check(extremum > (p - 1) ** 2 * p ** (c - 1))
    return dict(rule="SNC", params=dict(rows=2, cols=c, p=p), states=len(mapping),
                all_target_formula_checks=len(mapping), maximum_fibre=extremum,
                unique_maximum_target=sink, mapping_sha256=digest(mapping))


def derivative_at(roots, g, p):
    # Direct product rule, without inverses or a logarithmic derivative.
    value = 0
    for excluded in range(len(roots)):
        term = 1
        for j, root in enumerate(roots):
            if j != excluded:
                term = term * (g - root) % p
        value = (value + term) % p
    return value


def rci(p, dim):
    points = list(product(range(p), repeat=dim))
    v = len(points)
    selected = [[j for j in range(v) if mask >> j & 1] for mask in range(1 << v)]
    mapping = []
    for subset in selected:
        cardinal = len(subset)
        if cardinal % p == 0:
            mapping.append(0)
            continue
        g = tuple(sum(points[j][i] for j in subset) * pow(cardinal, -1, p) % p
                  for i in range(dim))
        out = set()
        for j in subset:
            delta = tuple((x - y) % p for x, y in zip(points[j], g))
            q = sum(x * x for x in delta) % p
            check((q == 0) == (points[j] == g))
            if q:
                # Solve q(z-g)=x-g by exhaustive points, not inversion lookup.
                matches = [i for i, z in enumerate(points)
                           if all(q * (a - b) % p == c for a, b, c in zip(z, g, delta))]
                check(len(matches) == 1)
                out.add(matches[0])
        mapping.append(sum(1 << j for j in out))
    actual = Counter(mapping)
    extremum = v + sum(comb(v, k) for k in range(v + 1) if k % p == 0)
    check(actual[0] == extremum)
    for mask, subset in enumerate(selected[1:], 1):
        k = len(subset)
        multiplier = int(k % p != 0) + int((k + 1) % p != 0)
        critical = []
        for g_index, g in enumerate(points):
            if g_index in subset:
                continue
            total = [0] * dim
            for j in subset:
                delta = tuple((x - y) % p for x, y in zip(points[j], g))
                q = sum(x * x for x in delta) % p
                check(q != 0)
                for i in range(dim):
                    total[i] = (total[i] + delta[i] * pow(q, -1, p)) % p
            if not any(total):
                critical.append(g_index)
        check(actual[mask] == multiplier * len(critical))
        check(actual[mask] < extremum)
        if dim == 1:
            roots = [points[j][0] for j in subset]
            derivative_roots = [g for g in range(p) if derivative_at(roots, g, p) == 0]
            check(derivative_roots == critical)
            check(not set(derivative_roots).intersection(roots))
            check(actual[mask] <= p - 1)
        if dim == 2:
            check(actual[mask] <= 2 * (v - 1))
    check([y for y, count in actual.items() if count == max(actual.values())] == [0])
    if dim == 1:
        check(extremum == p + 2)
    if dim == 0:
        check(extremum == 2)
    return dict(rule="RCI", params=dict(p=p, d=dim), states=len(mapping),
                all_target_formula_checks=len(mapping), maximum_fibre=extremum,
                unique_maximum_target=0, mapping_sha256=digest(mapping))


def main():
    old = json.loads((BASE / "execution_pair_v1/run1/producer.stdout").read_bytes())
    rows = [snc(p) for p in (5, 7)]
    rows += [rci(p, d) for p, d in ((3, 0), (3, 1), (3, 2), (5, 1), (7, 1), (11, 1))]
    for row, original in zip(rows, old["boxes"][:8]):
        for key in ("rule", "params", "states", "mapping_sha256", "maximum_fibre"):
            check(row[key] == original[key])
        check(row["unique_maximum_target"] == original["first_maximum_fibre_target"])
        check(original["maximum_fibre_target_count"] == 1)
    check(len(rows) == 8)
    check(sum(row["states"] for row in rows) == 136006)
    print(json.dumps(dict(schema="fourteenth-inverse-author-check-v1", assertions=CHECKS,
                          boxes=rows), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
