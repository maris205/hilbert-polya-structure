"""Author-side independent graph implementation, not a nonauthor review.

Build the full (D+1)^2 square, with no secant-symbol filtering. Remove
every vertex whose forward orbit leaves the square by reverse propagation.
For the injective Hénon map the surviving finite set is exactly its cycles.
Compare every cycle with the separate path-traversal certificate and
check the seven exact coefficient templates, not only a maximum count.
"""

from collections import deque
from itertools import product
import json

from certify_cubic import cycle_graph, symbolic_certificate


def canonical(word):
    return min(word[i:]+word[:i] for i in range(len(word)))


def peel_cycles(D, A, q, r):
    def value(t):
        return A+q*t+t*(t-D)*(t-r)

    vertices = set(product(range(D+1), repeat=2))
    queue = deque((x, y) for x, y in vertices if not 0 <= value(y)-x <= D)
    while queue:
        point = queue.popleft()
        if point not in vertices:
            continue
        vertices.remove(point)
        x, y = point
        previous = (value(x)-y, x)
        if previous in vertices:
            queue.append(previous)
    cycles = []
    while vertices:
        start = min(vertices)
        point, word = start, []
        while True:
            assert point in vertices
            vertices.remove(point)
            x, y = point
            word.append(x)
            point = (y, value(y)-x)
            if point == start:
                break
        cycles.append(canonical(tuple(word)))
    return sorted(cycles, key=lambda w: (len(w), w))


def template_matches(word, a, b, c):
    n = len(word)
    symbols = sorted(set(word))
    if n == 1:
        u = word[0]
        return u**3+b*u*u+c*u+a == 2*u
    if len(symbols) == 2 and n in (2, 3, 4):
        u, v = symbols
        if n == 3 and word.count(u) != 2:
            u, v = v, u
        S, P = u+v, u*v
        C = -(u*u+u*v+v*v+b*S)
        if n == 2:
            return c == C-2 and a == 2*S+P*(S+b)
        if n == 3:
            return (canonical(word) == canonical((u, u, v))
                    and c == C-1 and a == 2*u+v+P*(S+b))
        return (canonical(word) == canonical((u, u, v, v))
                and c == C and a == S+P*(S+b))
    if len(symbols) == 3:
        u, h, v = symbols
        if n == 3:
            return b == -(u+h+v) and c == u*h+u*v+h*v-1 and a == u+h+v-u*h*v
        if n in (4, 6) and u+v == 2*h:
            k = v-h
            expected = (u, h, v, h) if n == 4 else (u, u, h, v, v, h)
            shift = 0 if n == 4 else 1
            return (canonical(word) == canonical(expected) and b == -3*h
                    and c == 3*h*h+shift-k*k
                    and a == -h**3+(k*k+2-shift)*h)
    return False


def main():
    cases, cycle_checks, maximum, maximizers = 0, 0, -1, []
    for D in range(2, 16):
        for r, A, q in product(range(-3, D+4), range(2*D+1), range(-2, 3)):
            if not 0 <= A+q*D <= 2*D:
                continue
            cases += 1
            cycles = peel_cycles(D, A, q, r)
            symbols = [t for t in range(D+1) if abs(t*(t-D)*(t-r)) <= 2*D]
            values = {t: A+q*t+t*(t-D)*(t-r) for t in symbols}
            other = cycle_graph(symbols, values)
            assert cycles == other, (D, r, A, q, cycles, other)
            for word in cycles:
                cycle_checks += 1
                assert template_matches(word, A, -(D+r), D*r+q), (D, r, A, q, word)
            used = {x for word in cycles for x in word}
            if 0 in used and D in used:
                count = sum(map(len, cycles))
                if count > maximum:
                    maximum, maximizers = count, []
                if count == maximum:
                    maximizers.append([D, r, A, q])
    large = symbolic_certificate()
    print(json.dumps({'full_square_cases_compared': cases,
                      'individual_cycle_templates_checked': cycle_checks,
                      'computed_maximum': maximum,
                      'all_maximizing_tuples_D_r_A_q': maximizers,
                      'large_symbolic_rows': large['rows'],
                      'review_status': 'author-side second implementation only'}, indent=2))


if __name__ == '__main__':
    main()
