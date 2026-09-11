"""Independent P214 Review A verifier. SOURCE ONLY until separately granted.

The checker does not import the author verifier or canonical output. It builds
the literal state graph backwards and computes multiplication images/kernels
by finite-field Gaussian elimination. Fixed box: q in {2,3,4}, m in {2,3,4}.
"""


def add(a, b, q):
    if q < 4:
        return (a + b) % q
    return a ^ b


def sub(a, b, q):
    if q < 4:
        return (a - b) % q
    return a ^ b


def mul(a, b, q):
    if q < 4:
        return (a * b) % q
    # F_4 = F_2[z]/(z^2+z+1), with 2=z.
    value = 0
    for i in range(2):
        if (b >> i) & 1:
            value ^= a << i
    if value & 4:
        value ^= 7
    return value


def inv(a, q):
    assert a
    for b in range(1, q):
        if mul(a, b, q) == 1:
            return b
    raise AssertionError(("no inverse", a, q))


def vectors(q, n):
    for code in range(q ** n):
        out = []
        for _ in range(n):
            out.append(code % q)
            code //= q
        yield tuple(out)


def radd(a, b, q):
    return tuple(add(x, y, q) for x, y in zip(a, b))


def rmul(a, b, q):
    m = len(a)
    out = [0] * m
    for i in range(m):
        for j in range(m - i):
            out[i + j] = add(out[i + j], mul(a[i], b[j], q), q)
    return tuple(out)


def valuation(a):
    for i, x in enumerate(a):
        if x:
            return i
    return len(a)


def rank(matrix, q):
    a = [list(row) for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot = 0
    for col in range(cols):
        found = next((r for r in range(pivot, rows) if a[r][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        scale = inv(a[pivot][col], q)
        a[pivot] = [mul(scale, x, q) for x in a[pivot]]
        for r in range(rows):
            if r != pivot and a[r][col]:
                factor = a[r][col]
                a[r] = [sub(a[r][c], mul(factor, a[pivot][c], q), q)
                        for c in range(cols)]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def main():
    lines = ["P214_A_REVERSE_GAUSSIAN_V1", "PARAM q=2,3,4 m=2,3,4"]
    assertions = 0
    total_states = 0
    for q in (2, 3, 4):
        for m in (2, 3, 4):
            zero = (0,) * m
            t = (0, 1) + (0,) * (m - 2)
            ideal = [(0,) + a for a in vectors(q, m - 1)]
            states = [(x, y) for x in ideal for y in ideal]
            successor = {}
            pred = {s: [] for s in states}
            for x, y in states:
                z = (y, rmul(x, radd(t, y, q), q))
                successor[(x, y)] = z
                pred[z].append((x, y))
            assertions += len(states)

            # Reverse breadth layers from zero determine all depths without
            # following author recurrence formulas.
            depth = {(zero, zero): 0}
            frontier = [(zero, zero)]
            while frontier:
                next_frontier = []
                for target in frontier:
                    for source in pred[target]:
                        if source not in depth:
                            depth[source] = depth[target] + 1
                            next_frontier.append(source)
                frontier = next_frontier
            assert len(depth) == len(states)
            assertions += len(states)

            census = [0] * (2 * m - 1)
            for x, y in states:
                expected = max(2 * (m - valuation(y)),
                               2 * (m - valuation(x)) - 1)
                assert depth[(x, y)] == expected
                assert successor[(x, y)] in states
                census[expected] += 1
                assertions += 2
            assert max(depth.values()) == 2 * m - 2
            assert all(sum(census[:h + 1]) == q ** h
                       for h in range(2 * m - 1))
            recurrent = [s for s in states if successor[s] == s]
            assert recurrent == [(zero, zero)]
            assertions += 3 + len(census)

            fibre_counts = {}
            image_size = 0
            for u in ideal:
                a = radd(t, u, q)
                # Matrix of x -> a*x on I in coefficient bases. Columns are
                # products with t,t^2,...; rank-nullity gives the fibre size.
                columns = []
                for j in range(1, m):
                    basis = tuple(1 if i == j else 0 for i in range(m))
                    columns.append(rmul(a, basis, q)[1:])
                matrix = [[columns[c][r] for c in range(m - 1)]
                          for r in range(m - 1)]
                r = rank(matrix, q)
                kernel_size = q ** (m - 1 - r)
                actual_nonempty = 0
                for w in ideal:
                    size = len(pred[(u, w)])
                    if size:
                        assert size == kernel_size
                        actual_nonempty += 1
                        fibre_counts[size] = fibre_counts.get(size, 0) + 1
                    assertions += 1
                assert actual_nonempty == q ** r
                assertions += 1
                image_size += actual_nonempty
            expected_image = q + (q - 1) * sum(q ** (2 * j)
                                               for j in range(1, m - 1))
            assert image_size == expected_image
            assert fibre_counts[q ** (m - 1)] == q
            for d in range(1, m - 1):
                assert fibre_counts[q ** d] == (q - 1) * q ** (2 * (m - d - 1))
            assertions += m

            if m == 2:
                assert all(successor[(x, y)] == (y, rmul(t, x, q))
                           for x, y in states)
            else:
                assert len(fibre_counts) >= 2
            assertions += 1
            total_states += len(states)
            lines.append("CARRIER q=%d m=%d states=%d height=%d image=%d fibres=%s" %
                         (q, m, len(states), max(depth.values()), image_size,
                          ",".join("%d:%d" % item for item in sorted(fibre_counts.items()))))
    assert total_states == 5271
    lines.append("TOTAL carriers=9 states=%d assertions=%d" % (total_states, assertions))
    lines.append("PASS")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
