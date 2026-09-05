#!/usr/bin/env python3
"""Direct input enumeration control for the supplementary cyclic gap formula.

No imports from the earlier author verifier. Finite checks are not the proof.
"""
from collections import Counter
from itertools import product


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def gap_value(target):
    w = tuple(x for x in target if x)
    r = len(w)
    if not r:
        return 3
    if len(set(w)) == 1:
        return 0
    start = next(i for i in range(r) if w[i] != w[(i-1) % r])
    runs = []
    length = 0
    last = None
    for k in range(r):
        x = w[(start+k) % r]
        if x != last:
            if length:
                runs.append(length)
            length = 1
            last = x
        else:
            length += 1
    runs.append(length)
    if max(runs) > 2:
        return 0
    doubles = [i for i, size in enumerate(runs) if size == 2]
    if not doubles:
        return fib(r-1) + fib(r+1)
    answer = 1
    for a, b in zip(doubles, doubles[1:] + [doubles[0]+len(runs)]):
        answer *= fib(b-a)
    return answer


def main():
    assertions = 0
    for n in range(1, 11):
        fibres = Counter()
        for x in product((-1, 0, 1), repeat=n):
            y = tuple((x[(i+1) % n] > x[i]) - (x[(i+1) % n] < x[i])
                      for i in range(n))
            fibres[y] += 1
        for y in product((-1, 0, 1), repeat=n):
            assert gap_value(y) == fibres[y], (n, y, gap_value(y), fibres[y])
            assertions += 1
        assert sum(fibres.values()) == 3**n
        assertions += 1
        print(f'n={n} inputs={3**n} image={len(fibres)} max_fibre={max(fibres.values())}')
    print(f'assertions={assertions} status=PASS finite_scope_n1_through_10')


if __name__ == '__main__':
    main()
