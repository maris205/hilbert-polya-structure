"""Independent P213 A source. SOURCE ONLY; execution needs root acceptance.

No imports, external data, environment, arguments, random numbers or files.
Fixed box n=1..6, N=0..4. No author or candidate checker is imported.
"""


def box(n, cap):
    for code in range((cap + 1) ** n):
        x = code
        digits = []
        for i in range(n):
            digits.append(x % (cap + 1))
            x //= cap + 1
        yield tuple(digits)


def update(a):
    n = len(a)
    return tuple(max(a[i] - a[(i + 1) % n], 0)
                 + min(a[(i - 1) % n], a[i]) for i in range(n))


def inverse(y, mass):
    # Enumerate currents, not source compositions or comparison chambers.
    n = len(y)
    result = []
    for c in box(n, mass):
        a = tuple(y[i] + c[i] - c[(i - 1) % n] for i in range(n))
        if min(a) < 0:
            continue
        for i in range(n):
            u = a[i] - c[i]
            v = a[(i + 1) % n] - c[i]
            if u < 0 or v < 0 or u * v != 0:
                break
        else:
            assert sum(a) == mass, ("current telescoping", y, c)
            result.append(a)
    assert len(result) == len(set(result)), ("current uniqueness", y)
    return sorted(result)


def terminal_by_cut(a):
    m = min(a)
    n = len(a)
    cut = a.index(m)
    answer = [m] * n
    accumulated = 0
    for offset in range(1, n + 1):
        i = (cut + offset) % n
        if a[i] == m:
            answer[(i - 1) % n] += accumulated
            accumulated = 0
        else:
            accumulated += a[i] - m
    assert accumulated == 0
    return tuple(answer)


def product(y):
    m = min(y)
    spikes = [i for i in range(len(y)) if y[i] > m]
    value = 1
    for j, e in enumerate(spikes):
        previous = spikes[j - 1]
        distance = (e - previous) % len(y) or len(y)
        if distance >= 3:
            value *= (y[e] - m) // 2 + 1
    return value


def text(a):
    return ",".join(str(v) for v in a)


def main():
    lines = ["P213_A_CURRENT_FOREST_V1", "PARAM n=1..6 N=0..4"]
    total = 0
    carriers = 0
    for n in range(1, 7):
        for mass in range(5):
            states = sorted(a for a in box(n, mass) if sum(a) == mass)
            count = 1
            for j in range(1, n):
                count = count * (mass + j) // j
            assert len(states) == count
            successors = {a: update(a) for a in states}
            pred = {a: [] for a in states}
            for a in states:
                b = successors[a]
                assert b in pred and min(b) == min(a)
                assert all(a[i] != min(a) or b[i] == min(a) for i in range(n))
                pred[b].append(a)
            degree = {a: len(pred[a]) for a in states}
            queue = [a for a in states if degree[a] == 0]
            cursor = 0
            while cursor < len(queue):
                a = queue[cursor]
                cursor += 1
                b = successors[a]
                degree[b] -= 1
                if degree[b] == 0:
                    queue.append(b)
            recurrent = [a for a in states if degree[a] > 0]
            assert all(successors[a] == a for a in recurrent)
            depth = {a: 0 for a in recurrent}
            terminal = {a: a for a in recurrent}
            for a in reversed(queue):
                b = successors[a]
                depth[a] = depth[b] + 1
                terminal[a] = terminal[b]
            assert len(depth) == len(states)
            for y in states:
                fixed = all((y[i] - min(y)) * (y[(i + 1) % n] - min(y)) == 0
                            for i in range(n))
                assert (successors[y] == y) == fixed
                assert terminal[y] == terminal_by_cut(y)
                sources = inverse(y, mass)
                assert sources == pred[y], ("complete inverse", y)
                if fixed:
                    assert len(sources) == product(y)
                if n <= 2:
                    assert sources == [y] and depth[y] == 0
                if n == 3:
                    r = [v - min(y) for v in y]
                    if sum(v > 0 for v in r) == 2:
                        head = next(i for i in range(3) if r[i] and not r[(i-1) % 3])
                        receiver = (head + 1) % 3
                        b = y
                        for t in range(depth[y] + 2):
                            assert b[receiver] - min(y) == min((2 ** t) * r[receiver], sum(r))
                            assert b[head] - min(y) == max(sum(r) - (2 ** t) * r[receiver], 0)
                            b = successors[b]
                lines.append("STATE n=" + str(n) + " N=" + str(mass) + " a=" + text(y)
                             + " next=" + text(successors[y]) + " tau=" + str(depth[y])
                             + " terminal=" + text(terminal[y]) + " sources="
                             + (";".join(text(a) for a in sources) or "-"))
            h = max(depth.values())
            expected = 0 if n <= 2 or mass == 0 else ((mass - 1).bit_length() if n == 3 else mass - 1)
            assert h == expected
            maximum = max(len(pred[a]) for a in states)
            if n >= 3:
                k = n // 3
                assert maximum <= ((2 ** n) - 1) * (mass + 1) ** k
                if mass >= 2 * k:
                    witness = [0] * n
                    q = mass // (2 * k)
                    for j in range(k):
                        witness[3 * j] = 2 * q
                    witness[0] += mass - 2 * k * q
                    assert len(pred[tuple(witness)]) >= (q + 1) ** k
                    assert maximum * (2 * k) ** k >= mass ** k
            lines.append("CARRIER n=" + str(n) + " N=" + str(mass) + " states=" + str(count)
                         + " height=" + str(h) + " maximum=" + str(maximum)
                         + " recurrent=" + str(len(recurrent)))
            carriers += 1
            total += count
    assert carriers == 30 and total == 461
    lines.append("TOTAL carriers=" + str(carriers) + " states=" + str(total))
    lines.append("PASS")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
