#!/usr/bin/env python3
"""Author-level theorem-fragment controls, not an independent admission gate.

Literal update and carrier helpers are imported from both pinned lane scripts.
Formula controls are newly implemented here. Bounds never exceed the pilots.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
import json
from pilot_initial import (partitions, predecessor_reverse, zero_pair_reaction,
    balanced_split_transpose, ballistic_annihilation)
from pilot_additional import autocorrelation_zero, missing_language_tools

checks = Counter()


def check(name, condition):
    checks[name] += 1
    assert condition, (name, checks[name])


def occurrences(w, pattern):
    n = len(w)
    return {i for i in range(n)
            if tuple(w[(i+j)%n] for j in range(3)) == pattern}


def normalized_partition(w):
    counts = Counter(w)
    for a, count in tuple(counts.items()):
        if a%2:
            pairs = count//2
            counts[a] %= 2
            if a > 1:
                counts[a-1] += pairs
            counts[a+1] += pairs
    return tuple(a for a,count in sorted(counts.items(),reverse=True)
                 for _ in range(count))


def partition_fibre(target):
    if any(a%2 and c > 1 for a,c in Counter(target).items()):
        return 0
    core = Counter(balanced_split_transpose(target))
    top = max((a//2 for a in core if a%2 == 0),default=0)
    if not top:
        return 1
    @lru_cache(None)
    def count(j, previous):
        if j == top+1:
            return int(previous == 0)
        return sum(count(j+1,k) for k in range(core[2*j]-previous+1))
    return sum(count(1,k) for k in range(core[2]+1))


def main():
    for n in range(1,7):
        for f in product(range(n),repeat=n):
            g = predecessor_reverse(f)
            old = {frozenset((i,j)) for i,j in enumerate(f)}
            new = {frozenset((i,j)) for i,j in enumerate(g)}
            check("PR_edge_descent",new <= old)
    lucas = [2,1]
    for _ in range(2,15):
        lucas.append(sum(lucas[-2:]))
    for n in range(1,15):
        states = list(product((0,1),repeat=n))
        fibres = Counter(zero_pair_reaction(w) for w in states)
        fixed = 0
        for y in states:
            z = zero_pair_reaction(y)
            fixed += (y == z)
            check("ZR_weight_descent",y == z or sum(z) > sum(y))
            if n < 3:
                check("ZR_inverse",fibres[y] == 1)
                continue
            qs = sorted(occurrences(y,(1,1,0)))
            constraints = [set(qs) & {(j-2)%n,(j+2)%n}
                           for j in occurrences(y,(0,0,1))]
            accepted = 0
            for bits in product((0,1),repeat=len(qs)):
                selected = {q for q,b in zip(qs,bits) if b}
                predicted = all(selected & c for c in constraints)
                source = list(y)
                for q in selected:
                    source[q],source[(q+1)%n],source[(q+2)%n] = 0,0,1
                actual = zero_pair_reaction(tuple(source)) == y
                check("ZR_inverse_subset",actual == predicted)
                accepted += predicted
            check("ZR_inverse",accepted == fibres[y])
            check("ZR_maximizers",(fibres[y] == 2**(n//3)) ==
                  (len(qs) == n//3 and not occurrences(y,(0,0,1))))
        check("ZR_fixed_count",fixed == lucas[n]+1)
        check("ZR_maximum",max(fibres.values()) == 2**(n//3))
    for n in range(1,31):
        states = partitions(n)
        fibres = Counter(balanced_split_transpose(w) for w in states)
        for w in states:
            tw = balanced_split_transpose(w)
            ttw = balanced_split_transpose(tw)
            check("BS_normalization",ttw == normalized_partition(w))
            check("BS_cubic",balanced_split_transpose(ttw) == tw)
            check("BS_fibre",partition_fibre(w) == fibres[w])
    for n in range(1,10):
        for w in product((-1,0,1),repeat=n):
            v = w
            for _ in range(n//2):
                v = ballistic_annihilation(v)
            check("BA_clock",not (1 in v and -1 in v))
            if not (1 in w and -1 in w):
                u = w
                for _ in range(n):
                    u = ballistic_annihilation(u)
                check("BA_recurrent_shift",u == w)
        if n > 1:
            v = (1,)+(0,)*(n-2)+(-1,)
            for _ in range(n//2-1):
                v = ballistic_annihilation(v)
            check("BA_sharp_witness",1 in v and -1 in v)
            check("BA_sharp_end",set(ballistic_annihilation(v)) <= {0})
    for n in range(1,13):
        full = (1 << n)-1
        for a in range(1 << n):
            b = autocorrelation_zero(n,a)
            negative_b = sum(1 << ((-i)%n) for i in range(n) if (b >> i)&1)
            check("AZ_symmetry",b == negative_b)
            if a == b:
                sums = 0
                for i in range(n):
                    for j in range(n):
                        if ((a >> i)&1) and ((a >> j)&1):
                            sums |= 1 << ((i+j)%n)
                check("AZ_fixed_sumfree",sums == full^a)
    for n in range(1,5):
        edges, vertices = 1 << n, 1 << (n-1)
        size = 1 << edges
        endpoints = [(1 << (w >> 1)) | (1 << (w & (vertices-1)))
                     for w in range(edges)]
        supports = [0]*size
        reversals = [0]*size
        reverse_word = [int(f"{w:0{n}b}"[::-1],2) for w in range(edges)]
        for language in range(1,size):
            bit = language & -language
            w = bit.bit_length()-1
            supports[language] = supports[language^bit] | endpoints[w]
            reversals[language] = reversals[language^bit] | (1 << reverse_word[w])
        closures = [sum(1 << w for w,ep in enumerate(endpoints) if ep & ~v == 0)
                    for v in range(1 << vertices)]
        u = [closures[supports[a]]^a for a in range(size)]
        update = missing_language_tools(n)
        arrows = [update(a) for a in range(size)]
        fibres = Counter(arrows)
        for a in range(size):
            check("MA_literal",arrows[a] == reversals[u[a]])
            check("MA_square",arrows[arrows[a]] == u[u[a]])
            check("MA_erosion",u[u[a]] & ~a == 0)
            y = reversals[a]
            predicted = sum(y & ~closed == 0 and supports[closed^y] == v
                            for v,closed in enumerate(closures))
            check("MA_fibre",predicted == fibres[a])
    print(json.dumps({"status":"PASS","checks":dict(sorted(checks.items())),
        "assertions":sum(checks.values()),"scope":"author_fragment_controls_only"},
        sort_keys=True,separators=(",",":")))


if __name__ == "__main__":
    main()
