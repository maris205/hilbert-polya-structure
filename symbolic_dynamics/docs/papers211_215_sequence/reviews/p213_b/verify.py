"""P213 B occupation/relation/layer checker. SOURCE ONLY until authorized.

No imports, files, arguments, environment, subprocesses or canonical reads.
The independent oracle is a complete synchronous token forward relation.
Chambers are tested declaratively, not solved by the author's atlas.
"""


def occupations(n, mass):
    # A sorted multiset of particle locations encodes each occupation once.
    words = [()]
    for unused in range(mass):
        words = [w + (site,) for w in words
                 for site in range(w[-1] if w else 0, n)]
    return sorted(tuple(w.count(i) for i in range(n)) for w in words)


def move(a):
    # Label particles temporarily by their height within the old site.
    # Only height <= old receiver population moves; decisions are simultaneous.
    b = [0] * len(a)
    for i, population in enumerate(a):
        receiver = (i + 1) % len(a)
        for height in range(1, population + 1):
            destination = receiver if height <= a[receiver] else i
            b[destination] += 1
    return tuple(b)


def word(a):
    return tuple(int(a[i] <= a[(i + 1) % len(a)]) for i in range(len(a)))


def table(a, s):
    b = []
    for i in range(len(a)):
        prev, nex = (i - 1) % len(a), (i + 1) % len(a)
        pair = (s[prev], s[i])
        if pair == (0, 1):
            value = a[i]
        elif pair == (1, 1):
            value = a[prev]
        elif pair == (0, 0):
            value = 2 * a[i] - a[nex]
        else:
            value = a[i] + a[prev] - a[nex]
        b.append(value)
    return tuple(b)


def endpoint(a):
    # Independently route each residual unit to its next zero's predecessor.
    base = min(a)
    result = [base] * len(a)
    for site, value in enumerate(a):
        if value == base:
            continue
        e = site
        for unused in range(len(a)):
            if a[(e + 1) % len(a)] == base:
                break
            e = (e + 1) % len(a)
        else:
            raise AssertionError("residual has no barrier")
        result[e] += value - base
    return tuple(result)


def fixed_formula(a):
    base = min(a)
    return all(a[i] == base or a[(i + 1) % len(a)] == base
               for i in range(len(a)))


def fixed_product(a):
    base = min(a)
    value = 1
    for e in range(len(a)):
        if a[e] == base:
            continue
        gap = 0
        for distance in range(1, len(a)):
            if a[(e - distance) % len(a)] != base:
                break
            gap += 1
        if gap >= 2:
            value *= (a[e] - base) // 2 + 1
    return value


def prepeaks(s):
    # Free prepeak iff its own and previous edge ascend and next descends.
    return [i for i in range(len(s))
            if s[(i - 1) % len(s)] == s[i] == 1
            and s[(i + 1) % len(s)] == 0]


def inspect_nonempty(y, s, sources):
    # No backwards dyadic solving: extract invariant coordinates from the
    # independently inverted relation, then test the claimed interval product.
    free = prepeaks(s)
    varying = set(free + [(i + 1) % len(s) for i in free])
    for i in range(len(s)):
        if i not in varying:
            assert len({a[i] for a in sources}) == 1, ("forced", y, s, i)
    rectangle = [()]
    bounds = []
    for i in free:
        p, right = (i + 1) % len(s), (i + 2) % len(s)
        right_values = {a[right] for a in sources}
        assert len(right_values) == 1
        total = y[p] + next(iter(right_values))
        lo, hi = y[i], min(total // 2, y[p] - 1)
        assert lo <= hi
        assert {a[i] for a in sources} == set(range(lo, hi + 1))
        assert all(a[i] + a[p] == total for a in sources)
        rectangle = [r + (t,) for r in rectangle for t in range(lo, hi + 1)]
        bounds.append((i, lo, hi))
    projected = [tuple(a[i] for i in free) for a in sources]
    assert len(projected) == len(set(projected)), ("projection injective", y, s)
    assert set(projected) == set(rectangle), ("full rectangularity", y, s)
    assert len(free) <= len(s) // 3
    return bounds


def encode(a):
    return ",".join(str(v) for v in a)


def main():
    print("P213_B_OCCUPATION_RELATION_LAYERS_V1")
    print("PARAM n=1..6 N=0..4")
    total_states = total_carriers = total_words = 0
    for n in range(1, 7):
        for mass in range(5):
            states = occupations(n, mass)
            expected = 1
            for j in range(1, mass + 1):
                expected = expected * (n + j - 1) // j
            assert len(states) == len(set(states)) == expected
            arrows = {a: move(a) for a in states}
            predecessors = {y: sorted(a for a in states if arrows[a] == y)
                            for y in states}
            assert sum(len(v) for v in predecessors.values()) == len(states)
            reached = {a: (0, a) for a in states if arrows[a] == a}
            layer_sizes = [len(reached)]
            for depth in range(1, len(states) + 1):
                added = {a: (depth, reached[arrows[a]][1]) for a in states
                         if a not in reached and arrows[a] in reached}
                if not added:
                    break
                reached.update(added)
                layer_sizes.append(len(added))
            assert len(reached) == len(states), "nonfixed recurrence or missing layer"
            height = len(layer_sizes) - 1
            bound = (0 if n <= 2 or mass == 0 else
                     (mass - 1).bit_length() if n == 3 else mass - 1)
            assert height == bound, ("sharp height", n, mass)
            words = [tuple((code >> i) & 1 for i in range(n))
                     for code in range(1 << n)]
            by_word = {s: [a for a in states if word(a) == s] for s in words}
            largest = max(len(v) for v in predecessors.values())
            for y in states:
                b = arrows[y]
                assert b in arrows and min(b) == min(y)
                assert all(y[i] != min(y) or b[i] == min(y) for i in range(n))
                assert fixed_formula(y) == (b == y)
                assert reached[y][1] == endpoint(y)
                if b == y:
                    assert len(predecessors[y]) == fixed_product(y)
                print("STATE", n, mass, encode(y), "NEXT", encode(b),
                      "TIME", reached[y][0], "END", encode(reached[y][1]),
                      "PRE", ";".join(encode(a) for a in predecessors[y]) or "-")
                if n >= 3:
                    union = []
                    for s in words:
                        actual = [a for a in predecessors[y] if word(a) == s]
                        declared = [a for a in by_word[s] if table(a, s) == y]
                        assert actual == declared, ("full chamber set", y, s)
                        bounds = inspect_nonempty(y, s, actual) if actual else []
                        if not any(s):
                            assert not actual
                        if all(s):
                            assert actual == ([y] if len(set(y)) == 1 else [])
                        union.extend(declared)
                        print("CHAMBER", n, mass, encode(y), "WORD", encode(s),
                              "PRE", ";".join(encode(a) for a in declared) or "-",
                              "INTERVALS", ";".join(encode(t) for t in bounds) or "-")
                        total_words += 1
                    assert sorted(union) == predecessors[y]
                    assert len(union) == len(set(union))
                    assert bool(union) == bool(predecessors[y])
            if n >= 3:
                k = n // 3
                assert largest <= ((1 << n) - 1) * (mass + 1) ** k
                if mass >= 2 * k:
                    spike = [0] * n
                    q = mass // (2 * k)
                    for i in range(k):
                        spike[3 * i + 2] = 2 * q
                    spike[2] += mass - 2 * k * q
                    assert len(predecessors[tuple(spike)]) >= (q + 1) ** k
                    assert largest * (2 * k) ** k >= mass ** k
                for A in range(1, mass):
                    B = mass - A
                    state = (A, B) + (0,) * (n - 2)
                    for t in range(mass + 1):
                        target = (max(mass - (1 << t) * B, 0),
                                  min((1 << t) * B, mass)) + (0,) * (n - 2)
                        assert state == target, ("two-site", n, mass, A, t)
                        state = arrows[state]
            else:
                assert largest == 1
            print("CARRIER", n, mass, "STATES", len(states), "HEIGHT", height,
                  "LAYERS", encode(layer_sizes), "MAXFIBRE", largest)
            total_carriers += 1
            total_states += len(states)
    assert (total_carriers, total_states) == (30, 461)
    print("PASS", "CARRIERS", total_carriers, "STATES", total_states,
          "CHAMBERS", total_words)


if __name__ == "__main__":
    main()
