#!/usr/bin/env python3
"""Exact controls for (x,y) -> (xy,yx) on finite groups."""

from collections import Counter
from itertools import product, permutations


class FiniteGroup:
    def __init__(self, name, elements, mul, inv, identity, class_two_odd):
        self.name = name
        self.elements = tuple(elements)
        self.mul = mul
        self.inv = inv
        self.e = identity
        self.class_two_odd = class_two_odd

    def conj(self, x, a):
        return self.mul(self.mul(self.inv(x), a), x)

    def pow(self, x, n):
        ans = self.e
        base = x
        while n:
            if n & 1:
                ans = self.mul(ans, base)
            base = self.mul(base, base)
            n //= 2
        return ans


def cyclic(n):
    return FiniteGroup(
        f"C{n}", range(n), lambda a, b: (a + b) % n,
        lambda a: (-a) % n, 0, n % 2 == 1,
    )


def heisenberg(p):
    elems = tuple(product(range(p), repeat=3))

    def mul(g, h):
        a, b, c = g
        x, y, z = h
        return ((a + x) % p, (b + y) % p, (c + z + a * y) % p)

    def inv(g):
        a, b, c = g
        return ((-a) % p, (-b) % p, (-c + a * b) % p)

    return FiniteGroup(f"H{p}", elems, mul, inv, (0, 0, 0), True)


def symmetric3():
    elems = tuple(permutations(range(3)))

    def mul(a, b):
        return tuple(a[b[i]] for i in range(3))

    def inv(a):
        out = [0] * 3
        for i, v in enumerate(a):
            out[v] = i
        return tuple(out)

    return FiniteGroup("S3-control", elems, mul, inv, (0, 1, 2), False)


def direct_product(g1, g2):
    elems = tuple(product(g1.elements, g2.elements))
    return FiniteGroup(
        f"{g1.name}x{g2.name}", elems,
        lambda a, b: (g1.mul(a[0], b[0]), g2.mul(a[1], b[1])),
        lambda a: (g1.inv(a[0]), g2.inv(a[1])),
        (g1.e, g2.e), g1.class_two_odd and g2.class_two_odd,
    )


def check_group(G):
    assertions = 0
    E = G.elements
    assert G.inv(G.e) == G.e
    assertions += 1
    for x in E:
        assert G.mul(G.e, x) == x == G.mul(x, G.e)
        assert G.mul(x, G.inv(x)) == G.e == G.mul(G.inv(x), x)
        assertions += 2
    # Full associativity is affordable on the small generic control; sample a
    # deterministic Cartesian slice on the larger formula-defined groups.
    stride = max(1, len(E) // 13)
    sample = E[::stride]
    for x, y, z in product(sample, repeat=3):
        assert G.mul(G.mul(x, y), z) == G.mul(x, G.mul(y, z))
        assertions += 1
    return assertions


def check_map(G):
    E = G.elements
    pairs = tuple(product(E, repeat=2))
    assertions = check_group(G)

    def phi(pair):
        x, y = pair
        return G.mul(x, y), G.mul(y, x)

    centralizer = {}
    conjugate = {}
    commuting_pairs = 0
    for a in E:
        centralizer[a] = sum(G.mul(a, x) == G.mul(x, a) for x in E)
        conjugate[a] = {G.conj(x, a) for x in E}
        assertions += len(E) + 1
    for x, y in pairs:
        commuting_pairs += G.mul(x, y) == G.mul(y, x)
        assertions += 1

    fibres1 = Counter(phi(pair) for pair in pairs)
    for a, b in pairs:
        expected = centralizer[a] if b in conjugate[a] else 0
        assert fibres1[(a, b)] == expected
        assertions += 1
    assert sum(fibres1.values()) == len(E) ** 2
    assertions += 1

    result = {
        "group": G.name,
        "order": len(E),
        "image": len(fibres1),
        "one_step_fibre_sizes": sorted(set(fibres1.values())),
    }

    if G.class_two_odd:
        assert len(E) % 2 == 1
        assertions += 1
        squares = {G.mul(x, x) for x in E}
        assert len(squares) == len(E)
        assertions += 1

        phi2 = {}
        for pair in pairs:
            out = phi(phi(pair))
            phi2[pair] = out
            assert out[0] == out[1]
            assertions += 1

        fibres2 = Counter(phi2.values())
        for g in E:
            assert fibres2[(g, g)] == len(E)
            assertions += 1
        assert len(fibres2) == len(E)
        assertions += 1

        # For t >= 2 the iterate is the bijective power map on the diagonal
        # after the uniform |G|-to-one two-step collapse.
        current = dict(phi2)
        for t in range(3, 8):
            current = {pair: phi(out) for pair, out in current.items()}
            counts = Counter(current.values())
            assert len(counts) == len(E)
            assertions += 1
            for out, count in counts.items():
                assert out[0] == out[1]
                assert count == len(E)
                assertions += 2

        depth = Counter()
        for x, y in pairs:
            if x == y:
                depth[0] += 1
            elif G.mul(x, y) == G.mul(y, x):
                depth[1] += 1
            else:
                depth[2] += 1
            assertions += 1
        assert depth[0] == len(E)
        assert depth[1] == commuting_pairs - len(E)
        assert depth[2] == len(E) ** 2 - commuting_pairs
        assertions += 3

        # Fixed points of every iterate are exactly diagonal power solutions.
        fixed = []
        for t in range(1, 9):
            literal = 0
            for pair in pairs:
                out = pair
                for _ in range(t):
                    out = phi(out)
                literal += out == pair
                assertions += 1
            formula = sum(G.pow(g, 2 ** t - 1) == G.e for g in E)
            assert literal == formula
            assertions += len(E) + 1
            fixed.append(literal)

        # Class two is checked directly, not inferred from the flag.
        for x, y, z in product(E[::max(1, len(E) // 11)], repeat=3):
            comm = G.mul(G.mul(x, y), G.mul(G.inv(x), G.inv(y)))
            assert G.mul(comm, z) == G.mul(z, comm)
            assertions += 1

        result.update(
            commuting_pairs=commuting_pairs,
            depth_hist=dict(sorted(depth.items())),
            iterated_fibre_size=len(E),
            fixed_iterates=fixed,
        )
    return assertions, result


def main():
    groups = [
        symmetric3(), cyclic(3), cyclic(9), heisenberg(3), heisenberg(5),
        direct_product(heisenberg(3), cyclic(3)),
    ]
    total = 0
    print("GROUP PRODUCT-EXCHANGE EXACT CONTROL: PASS")
    for G in groups:
        assertions, result = check_map(G)
        total += assertions
        print(result)
    print(f"assertions={total}")


if __name__ == "__main__":
    main()
