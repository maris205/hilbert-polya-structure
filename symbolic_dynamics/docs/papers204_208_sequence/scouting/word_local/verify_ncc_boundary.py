#!/usr/bin/env python3
"""Author-level NCC boundary check, original full boxes only; no imports."""
from collections import Counter
from itertools import product
from math import comb, factorial
import json


def update(x):
    return tuple(sum(abs(a-b) <= 1 for b in x) for a in x)


def choose(a, b):
    return comb(a, b) if a >= b >= 0 else 0


def constant_fibre(n, q):
    if n % q:
        return 0
    k = n // q
    return factorial(n) // factorial(q)**k * sum(
        comb(k,r)*choose(n-k-r+1,k)*(2**q-2)**r for r in range(k+1))


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in compositions(total-a, length-1):
                yield (a,) + tail


def main():
    checks = 0
    records = []
    for n in range(1,7):
        fibres = Counter()
        fixed = []
        for x in product(range(1,n+1),repeat=n):
            y = update(x)
            assert all(1 <= a <= n for a in y)
            fibres[y] += 1
            c = Counter(x)
            predicted_fixed = all(c[a] == a and c[a-1] == c[a+1] == 0 for a in c)
            assert (x == y) == predicted_fixed
            checks += 2
            if x == y:
                fixed.append(x)
        constant_counts = []
        for q in range(1,n+1):
            value = constant_fibre(n,q)
            assert fibres[(q,)*n] == value
            checks += 1
            constant_counts.append(value)
        predicted = Counter()
        for m in compositions(n,n):
            d = tuple(sum(m[max(0,a-1):min(n,a+2)]) for a in range(n))
            e = [0]*n
            for a in range(n):
                if m[a]:
                    e[d[a]-1] += m[a]
            numerator = 1
            denominator = 1
            for value in e:
                numerator *= factorial(value)
            for value in m:
                denominator *= factorial(value)
            assert numerator % denominator == 0
            checks += 1
            predicted[tuple(e)] += numerator // denominator
        actual = {}
        for y, value in fibres.items():
            e = tuple(y.count(a) for a in range(1,n+1))
            if e in actual:
                assert actual[e] == value
            actual[e] = value
            assert value == predicted[e]
            checks += 1
        assert dict(predicted) == actual
        checks += 1
        records.append({'n':n,'states':n**n,'fixed_count':len(fixed),
                        'image':len(fibres),'constant_fibres_q_1_to_n':constant_counts,
                        'maximum':max(fibres.values()),
                        'all_maximum_targets':[list(y) for y,v in sorted(fibres.items()) if v == max(fibres.values())]})
    a=(4,4,5,5,3); b=(5,5,4,4,3)
    for x,y in ((a,b),(a+(1,),b+(1,))):
        assert x != y and update(x)==y and update(y)==x
        checks += 1
    print(json.dumps({'kind':'AUTHOR_PARTIAL_BOUNDARY_NOT_INDEPENDENT_GATE',
                      'checks':checks,'records':records},sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
