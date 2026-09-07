"""Nonauthor exact reconstruction by domains of iterated partial injections.

No producer import, root-alphabet filtering, escaping-vertex peeling, or
producer cycle traversal. All arithmetic uses Python integers. For a partial
injection on N vertices, dom(T^m) for m >= N consists precisely of cycles:
an acyclic injective component is a chain with fewer than N edges. Repeated
squaring computes that domain. Cycles are then read only on this invariant set.
"""

from itertools import product
import hashlib
import json
import platform


def periodic_words(vertices, transition):
    vertices = tuple(vertices)
    index = {x: i for i, x in enumerate(vertices)}
    step = [index.get(transition(x), -1) for x in vertices]
    finite_images = [x for x in step if x >= 0]
    assert len(set(finite_images)) == len(finite_images)
    jump, length = step[:], 1
    while length < len(vertices):
        jump = [jump[j] if j >= 0 else -1 for j in jump]
        length *= 2
    live = {i for i, j in enumerate(jump) if j >= 0}
    assert {step[i] for i in live} == live
    result = []
    while live:
        first = min(live)
        cursor, word = first, []
        while cursor in live:
            live.remove(cursor)
            word.append(vertices[cursor][0])
            cursor = step[cursor]
        assert cursor == first
        word = tuple(word)
        result.append(min(word[j:]+word[:j] for j in range(len(word))))
    return sorted(result, key=lambda w: (len(w), w))


def small():
    rows, best, winners, cycle_total = [], -1, [], 0
    for D in range(2, 16):
        trials, retained, maximum, alphabet = 0, 0, 0, 0
        periods = set()
        for B in range(-2*D-3, 4-D):
            r = -B-D
            for C in range(D*r-2, D*r+3):
                q = C-D*r
                for A in range(2*D+1):
                    if not 0 <= D**3+B*D**2+C*D+A <= 2*D:
                        continue
                    trials += 1
                    def step(point):
                        x, y = point
                        return y, y**3+B*y*y+C*y+A-x
                    words = periodic_words(product(range(D+1), repeat=2), step)
                    cycle_total += len(words)
                    used = {x for w in words for x in w}
                    if not {0, D} <= used:
                        continue
                    retained += 1
                    n = sum(map(len, words))
                    maximum = max(maximum, n)
                    periods.update(map(len, words))
                    alphabet = max(alphabet, *(len(set(w)) for w in words))
                    if n > best:
                        best, winners = n, []
                    if n == best:
                        winners.append({'D': D, 'r': r, 'A': A, 'q': q,
                                        'cycles': words})
        rows.append([D, trials, retained, maximum, sorted(periods), alphabet])
    return {'rows': rows, 'computed_maximum': best, 'maximizers': winners,
            'all_cycles_before_endpoint_filter': cycle_total}


def large():
    # T_r is derived in the written inequalities; D is represented by its
    # evaluations at 0 and 1. Every polynomial in an edge is affine in D,
    # so simultaneous equality of these evaluations is an identity in Z[D].
    rows, patterns = [], []
    for r, T in [(-1, [0, 1]), (0, [0, 1]), (1, [0, 1, 2]),
                 (2, [0, 1, 2]), (3, [0, 1, 2, 3])]:
        symbols = [(t, t) for t in T]+[(0, 1)]
        sums = {tuple(x+y for x, y in zip(u, v))
                for u, v in product(symbols, repeat=2)}
        trials, retained, maximum, alphabet, error = 0, 0, 0, 0, 0
        periods = set()
        for at_zero, at_one in sorted(sums):
            for q in range(-2, 3):
                if (at_zero, at_one+q) not in sums:
                    continue
                trials += 1
                def value(y):
                    if y == (0, 1):
                        return at_zero, at_one+q
                    t = y[0]
                    return (at_zero+q*t+t*t*(t-r),
                            at_one+q*t+t*(t-1)*(t-r))
                def step(point):
                    x, y = point
                    return y, tuple(a-b for a, b in zip(value(y), x))
                for y, x, z in product(symbols, repeat=3):
                    error = max(error, abs(value(y)[0]-x[0]-z[0]))
                words = periodic_words(product(symbols, repeat=2), step)
                maximum = max(maximum, sum(map(len, words)))
                periods.update(map(len, words))
                if words:
                    alphabet = max(alphabet, *(len(set(w)) for w in words))
                used = {x for w in words for x in w}
                if {(0, 0), (0, 1)} <= used:
                    retained += 1
                    # Convert evaluations back to coefficient/constant labels.
                    translated = [[[x[1]-x[0], x[0]] for x in w] for w in words]
                    patterns.append([r, [at_one-at_zero, at_zero], q, translated])
        assert error < 16
        rows.append([r, trials, retained, maximum, sorted(periods), alphabet, error])
    return {'rows': rows, 'all_endpoint_patterns': patterns}


if __name__ == '__main__':
    with open(__file__, 'rb') as source:
        own_hash = hashlib.sha256(source.read()).hexdigest()
    print(json.dumps({'python': platform.python_version(), 'script_sha256': own_hash,
                      'small': small(), 'large': large()}, indent=2))
