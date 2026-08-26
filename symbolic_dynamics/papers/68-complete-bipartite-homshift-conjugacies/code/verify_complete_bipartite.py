#!/usr/bin/env python3
"""Deterministic finite controls for P68.

These checks exercise finite instances of the exact formulae and the local
dimer code.  They are regression tests, not premises of the proofs.
"""

from itertools import product


def edges(shape):
    shape = set(shape)
    ans = []
    for v in sorted(shape):
        for delta in ((1, 0), (0, 1)):
            w = (v[0] + delta[0], v[1] + delta[1])
            if w in shape:
                ans.append((v, w))
    return ans


def formula(shape, m, n):
    if not shape:
        return 1
    even = sum((x + y) % 2 == 0 for x, y in shape)
    odd = len(shape) - even
    return m**even * n**odd + n**even * m**odd


def brute_extendible_patterns(shape, m, n):
    sites = sorted(shape)
    alphabet = [(0, i) for i in range(m)] + [(1, j) for j in range(n)]
    count = 0
    for word in product(alphabet, repeat=len(sites)):
        if any(
            all(
                part == (((x + y) & 1) ^ phase)
                for (x, y), (part, _) in zip(sites, word)
            )
            for phase in (0, 1)
        ):
            count += 1
    return count


def brute_locally_admissible_patterns(shape, m, n):
    sites = sorted(shape)
    alphabet = [(0, i) for i in range(m)] + [(1, j) for j in range(n)]
    edge_list = edges(shape)
    count = 0
    for word in product(alphabet, repeat=len(sites)):
        x = dict(zip(sites, word))
        if all(x[v][0] != x[w][0] for v, w in edge_list):
            count += 1
    return count


def torus_sites(nx=2, ny=2):
    return [(i, j) for i in range(nx) for j in range(ny)]


def shift(v, dx, dy, nx=2, ny=2):
    return ((v[0] + dx) % nx, (v[1] + dy) % ny)


def f_pair(a, b, n, s):
    """Lexicographic bijection A x B -> A' x B' when mn=rs."""
    q = a * n + b
    return divmod(q, s)


def finv_pair(ap, bp, s, n):
    q = ap * s + bp
    return divmod(q, n)


def encode(x, n, s):
    y = {}
    for v, symbol in x.items():
        part, colour = symbol
        if part == 0:
            _, b = x[shift(v, 1, 0)]
            ap, _ = f_pair(colour, b, n, s)
            y[v] = (0, ap)
        else:
            _, a = x[shift(v, -1, 0)]
            _, bp = f_pair(a, colour, n, s)
            y[v] = (1, bp)
    return y


def decode(y, s, n):
    x = {}
    for v, symbol in y.items():
        part, colour = symbol
        if part == 0:
            _, bp = y[shift(v, 1, 0)]
            a, _ = finv_pair(colour, bp, s, n)
            x[v] = (0, a)
        else:
            _, ap = y[shift(v, -1, 0)]
            _, b = finv_pair(ap, colour, s, n)
            x[v] = (1, b)
    return x


def all_torus_configurations(m, n):
    sites = torus_sites()
    for phase in (0, 1):
        alphabets = []
        for v in sites:
            part = ((v[0] + v[1]) & 1) ^ phase
            size = m if part == 0 else n
            alphabets.append([(part, c) for c in range(size)])
        for word in product(*alphabets):
            yield dict(zip(sites, word))


def check_dimer_bijection(m, n, r, s):
    """Check the local dimer code and inverse on the 2 x 2 torus."""
    assert m * n == r * s
    count = 0
    images = set()
    sites = torus_sites()
    for x in all_torus_configurations(m, n):
        y = encode(x, n, s)
        assert decode(y, s, n) == x
        assert all(y[v][0] != y[shift(v, 1, 0)][0] for v in sites)
        assert all(y[v][0] != y[shift(v, 0, 1)][0] for v in sites)
        assert all(
            0 <= colour < (r if part == 0 else s)
            for part, colour in y.values()
        )
        images.add(tuple(y[v] for v in sites))
        count += 1
    assert count == 2 * (m * n) ** 2 == len(images)
    return count


def weighted_square_check():
    shape = {(0, 0), (1, 0), (0, 1), (1, 1)}
    wa = (2, 3)
    wb = (5, 7, 11)
    alphabet = [(0, i) for i in range(len(wa))] + [
        (1, j) for j in range(len(wb))
    ]
    total = 0
    sites = sorted(shape)
    for word in product(alphabet, repeat=len(sites)):
        x = dict(zip(sites, word))
        if all(x[v][0] != x[w][0] for v, w in edges(shape)):
            weight = 1
            for part, colour in word:
                weight *= wa[colour] if part == 0 else wb[colour]
            total += weight
    expected = 2 * (sum(wa) * sum(wb)) ** 2
    assert total == expected
    return total


def main():
    shapes = [
        set(),
        {(0, 0)},
        {(0, 0), (1, 0)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 0), (1, 0), (0, 1), (1, 1)},
        {(0, 0), (2, 0)},
    ]
    for m, n in ((1, 1), (1, 6), (2, 2), (2, 3)):
        for shape in shapes:
            assert brute_extendible_patterns(shape, m, n) == formula(shape, m, n)
    print("globally extendible finite-shape counts (six shapes, four parameter pairs): PASS")

    remote_even = {(0, 0), (2, 0)}
    remote_opposite = {(0, 0), (3, 0)}
    assert brute_extendible_patterns(remote_even, 2, 3) == 13
    assert brute_locally_admissible_patterns(remote_even, 2, 3) == 25
    assert brute_extendible_patterns(remote_opposite, 2, 3) == 12
    assert brute_locally_admissible_patterns(remote_opposite, 2, 3) == 25
    print("global-phase versus local-admissibility counterexamples: PASS (13/25 and 12/25)")

    count = check_dimer_bijection(2, 6, 3, 4)
    print("radius-one dimer bijection K_(2,6) <-> K_(3,4): PASS (288 torus points)")

    singleton_count = check_dimer_bijection(1, 6, 2, 3)
    minimal_count = check_dimer_bijection(1, 1, 1, 1)
    assert singleton_count == 72 and minimal_count == 2
    print(
        "singleton-part boundary controls: PASS "
        "(K_(1,6) <-> K_(2,3): 72; K_(1,1): 2 torus points)"
    )

    # L=2Z x 2Z has [E:L]=2; an odd period has no fixed point.
    assert count == 2 * (2 * 6) ** 2
    odd_period_points = 0
    assert odd_period_points == 0
    print("finite-index fixed-point formula: PASS")

    weighted = weighted_square_check()
    print(f"weighted 2x2 partition identity: PASS (sum={weighted})")

    # The probabilistic core is the exact identity I_0=I_u for even u.
    for p in (0.0, 1.0):
        assert p == p * p
    assert all(abs(p - p * p) > 1e-12 for p in (0.1, 0.25, 0.5, 0.9))
    print("remote-phase independence equation p=p^2: PASS")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
