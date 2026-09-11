"""One fixed tiny author pilot; no arguments, imports, or file writes."""
def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest

def step(a):
    n = len(a)
    q = tuple(min(a[i], a[(i + 1) % n]) for i in range(n))
    return tuple(a[i] - q[i] + q[(i - 1) % n] for i in range(n))

def terminal_prediction(a):
    n = len(a)
    m = min(a)
    r = tuple(x - m for x in a)
    answer = [m] * n
    if not any(r):
        return tuple(answer)
    for i in range(n):
        if r[i] and r[(i + 1) % n] == 0:
            j, mass = i, 0
            while r[j]:
                mass += r[j]
                j = (j - 1) % n
            answer[i] += mass
    return tuple(answer)

def histogram(values):
    out = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return tuple(sorted(out.items()))

total_states = 0
print("FIXED_BOX n=3..5 N=0..6; AUTHOR_PILOT; no automatic enlargement")
for n in (3, 4, 5):
    for mass in range(7):
        states = tuple(compositions(mass, n))
        following = {a: step(a) for a in states}
        fibres = {a: 0 for a in states}
        for a, b in following.items():
            assert b in fibres and sum(b) == mass and min(a) == min(b)
            assert all(b[i] == 0 for i in range(n) if a[i] == 0)
            fibres[b] += 1
        depths, terminals = {}, {}
        for a in states:
            path, b = [], a
            while following[b] != b:
                assert b not in path, ("nonfixed_cycle", n, mass, a, path, b)
                path.append(b)
                b = following[b]
                assert len(path) <= max(0, mass - 1), ("clock_upper", n, mass, a, path)
            depths[a], terminals[a] = len(path), b
            assert b == terminal_prediction(a), ("terminal", a, b)
            r = tuple(x - min(a) for x in a)
            assert (following[a] == a) == all(
                not (r[i] > 0 and r[(i + 1) % n] > 0) for i in range(n))
            if n == 3 and sum(x > 0 for x in r) == 2:
                endpoint = next(i for i in range(n) if r[i] > 0 and r[(i + 1) % n] == 0)
                expected = ((sum(r) - 1) // r[endpoint]).bit_length()
                assert depths[a] == expected, ("three_clock", a, depths[a], expected)
        expected_max = 0 if mass == 0 else ((mass - 1).bit_length() if n == 3 else mass - 1)
        assert max(depths.values()) == expected_max
        print("CARRIER", n, mass, "states", len(states), "image", sum(v > 0 for v in fibres.values()),
              "depth_hist", histogram(depths.values()), "fibre_hist", histogram(fibres.values()),
              "max_fibre_targets", tuple(a for a in states if fibres[a] == max(fibres.values())))
        for a in states:
            print("ROW", a, "->", following[a], "depth", depths[a],
                  "terminal", terminals[a], "fibre", fibres[a])
        total_states += len(states)
assert total_states == 756
print("AUTHOR_FIXED_BOX_CHECKS_COMPLETED states=756 carriers=21; NO_ADMISSION; HOLD_EXTERNAL")

