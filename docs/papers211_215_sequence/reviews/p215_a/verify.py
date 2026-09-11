"""Independent P215 Review A verifier. SOURCE ONLY; do not execute pre-grant.

No imports, files, randomness, author code or author canonical. The temporal
route is reverse BFS on the full graph. Fibres use a left-to-right finite-state
automaton whose state is the current record maximum.
"""


def words(n, q):
    result = [()]
    for _ in range(n):
        result = [prefix + (digit,) for prefix in result
                  for digit in range(q + 1)]
    return result


def update(x):
    peak = 0
    out = []
    for value in x:
        peak = max(peak, value)
        out.append(peak - value)
    return tuple(out)


def run_count(x):
    previous = 0
    last = 0
    count = 0
    for value in x:
        difference = value - previous
        previous = value
        sign = (difference > 0) - (difference < 0)
        if sign and sign != last:
            count += 1
            last = sign
    return count


def choose(n, k):
    if k < 0 or k > n:
        return 0
    answer = 1
    for j in range(1, k + 1):
        answer = answer * (n - j + 1) // j
    return answer


def automaton_sources(y, q):
    # A partial path is (source prefix, record maximum). At the next
    # coordinate choose its new record H and force x_i=H-y_i.
    paths = [((), 0)]
    for target in y:
        following = []
        for prefix, previous_peak in paths:
            for peak in range(previous_peak, q + 1):
                value = peak - target
                if 0 <= value <= q and peak == max(previous_peak, value):
                    following.append((prefix + (value,), peak))
        paths = following
    return sorted(prefix for prefix, _ in paths)


def recurrence_count(y, q):
    if not y:
        return 1
    if y[0] != 0:
        return 0
    zeros = [i for i, value in enumerate(y) if value == 0]
    ends = zeros[1:] + [len(y)]
    block_maxima = [max(y[start:end]) for start, end in zip(zeros, ends)]
    barriers = []
    for value in block_maxima:
        barriers.append(max(barriers[-1] if barriers else 0, value))
    ceilings = [q - value for value in reversed(barriers)]
    counts = [1]
    for m in range(1, len(ceilings) + 1):
        value = choose(ceilings[m - 1] + m, m)
        for i in range(1, m):
            value -= counts[i - 1] * choose(
                ceilings[m - 1] - ceilings[i - 1] + m - i,
                m - i + 1)
        counts.append(value)
    return counts[-1]


def main():
    lines = ["P215_A_REVERSE_AUTOMATON_V1", "PARAM n=0..6 q=0..4"]
    assertions = 0
    total_states = 0
    for n in range(7):
        for q in range(5):
            states = words(n, q)
            zero = (0,) * n
            successor = {x: update(x) for x in states}
            predecessor = {x: [] for x in states}
            for x, y in successor.items():
                predecessor[y].append(x)

            # Reverse graph layers compute depth without following individual
            # orbits and without using the sign-run theorem as a stopping rule.
            depth = {zero: 0}
            frontier = [zero]
            while frontier:
                following = []
                for y in frontier:
                    for x in predecessor[y]:
                        if x not in depth:
                            depth[x] = depth[y] + 1
                            following.append(x)
                frontier = following
            assert len(depth) == len(states)
            assertions += len(states)

            deepest = []
            for x in states:
                expected = run_count(x)
                assert depth[x] == expected
                maximal = (all(x[i] != (x[i - 1] if i else 0)
                               for i in range(n)) and
                           all((x[i] - (x[i - 1] if i else 0)) *
                               (x[i + 1] - x[i]) < 0 for i in range(n - 1)))
                if n == 0 or q == 0:
                    maximal = x == zero
                assert (depth[x] == (n if n and q else 0)) == maximal
                if depth[x] == max(depth.values()):
                    deepest.append(x)
                assertions += 2

            image = []
            largest = -1
            maximizers = []
            for y in states:
                actual = sorted(predecessor[y])
                reconstructed = automaton_sources(y, q)
                assert reconstructed == actual
                assert recurrence_count(y, q) == len(actual)
                expected_image = (not y) or y[0] == 0
                assert bool(actual) == expected_image
                assertions += 3
                if actual:
                    image.append(y)
                if len(actual) > largest:
                    largest = len(actual)
                    maximizers = [y]
                elif len(actual) == largest:
                    maximizers.append(y)

            assert max(depth.values()) == (n if n and q else 0)
            assert len(image) == ((q + 1) ** (n - 1) if n else 1)
            assert largest == choose(q + n, n)
            assert maximizers == [zero]
            assertions += 4
            total_states += len(states)
            lines.append("CARRIER n=%d q=%d states=%d height=%d image=%d max_fibre=%d" %
                         (n, q, len(states), max(depth.values()), len(image), largest))
    assert total_states == 26219
    lines.append("TOTAL carriers=35 states=26219 assertions=%d" % assertions)
    lines.append("PASS")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
