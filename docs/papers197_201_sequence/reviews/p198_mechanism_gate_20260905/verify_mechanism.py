#!/usr/bin/env python3
"""Bounded P198 mechanism gate. Independent literals; no author imports."""
from collections import Counter

checks = 0


def check(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError((label, checks))


def path_matchings(n):
    def rec(i, occupied):
        if i >= n-1:
            yield occupied
        else:
            yield from rec(i+1, occupied)
            yield from rec(i+2, occupied | (1 << i))
    return list(rec(0, 0))


def cycle_matchings(n):
    a = path_matchings(n)
    wrap = 1 << (n-1)
    b = [wrap | (p << 1) for p in path_matchings(n-2)]
    return a+b


def monomers(n, edges, cyclic=True):
    covered = edges | (edges << 1)
    if cyclic:
        covered |= edges >> (n-1)
    return ((1 << n)-1) & ~covered


def labels(bits):
    out = []
    while bits:
        bit = bits & -bits
        out.append(bit.bit_length()-1)
        bits ^= bit
    return out


def reconstruct(n, points):
    ans = 0
    for a,b in zip(points, points[1:]+[points[0]+n]):
        for j in range(a+1,b-1,2):
            ans |= 1 << (j % n)
    return ans


def cmm(n, edges):
    holes = labels(monomers(n,edges))
    if len(holes) == 1:
        a = holes[0]
        return edges ^ (1 << a) ^ (1 << ((a+1) % n))
    a,b = holes[:2]
    return edges ^ (((1 << (b-a))-1) << a)


def lap(n, edges):
    holes = labels(monomers(n,edges,False))
    if len(holes) == 1:
        return edges
    a,b = holes[:2]
    return edges ^ (((1 << (b-a))-1) << a)


def union_lap(n, edges):
    wrap = 1 << (n-1)
    if edges & wrap:
        return wrap | (lap(n-2, (edges ^ wrap) >> 1) << 1)
    return lap(n, edges)


def erase2(bits):
    first = bits & (bits-1)
    return first & (first-1)


def subset_step(n,bits,rewire):
    if bits.bit_count() > 1:
        return erase2(bits)
    if not rewire:
        return bits
    i = bits.bit_length()-1
    return 1 << ((i+2) % n)


def main():
    total = 0
    for n in range(3,26,2):
        states = cycle_matchings(n)
        state_set = set(states)
        images, forest_images = Counter(), Counter()
        codes = set()
        for x in states:
            s = monomers(n,x)
            points = labels(s)
            check(len(points) % 2 == 1, 'odd monomer size')
            check(all((b-a) % 2 == 1 for a,b in zip(points,points[1:]+[points[0]+n])), 'odd gaps')
            check(reconstruct(n,points) == x, 'monomer bijection inverse')
            check(s not in codes, 'injective monomer encoding')
            codes.add(s)
            y = cmm(n,x)
            f = union_lap(n,x)
            check(y in state_set and f in state_set, 'closure')
            check(monomers(n,y) == subset_step(n,s,True), 'full subset conjugacy')
            check(monomers(n,f) == subset_step(n,s,False), 'stopped P100 squared restriction')
            check(y == f if len(points) > 1 else f == x, 'only root arrows rewired')
            if len(points) > 1:
                check((x >> (n-1)) == (y >> (n-1)), 'wrap bit transient invariant')
            images[y] += 1
            forest_images[f] += 1
        check(images == forest_images, 'every labelled fibre preserved by root rewiring')
        check(len(codes) == len(states), 'full monomer code cardinality')
        for y in states:
            s = monomers(n,y)
            u = (s & -s).bit_length()-1
            r, epsilon = divmod(u,2)
            inverse = []
            for i in range(r):
                for j in range(i,r):
                    a,b = 2*i+epsilon,2*j+1+epsilon
                    candidate = s | (1 << a) | (1 << b)
                    check(candidate in codes and erase2(candidate) == s, 'parity-filtered HF1 predecessor')
                    inverse.append(candidate)
            check(len(inverse) == r*(r+1)//2, 'parity insertion triangular count')
            check(images[y] == len(inverse)+(s.bit_count()==1), 'full inherited target formula')
        maximum = 1+(n//2)*(n//2+1)//2
        check(max(images.values()) == maximum, 'inherited maximum')
        check([y for y in states if images[y] == maximum] == [reconstruct(n,[n-1])], 'unique inherited maximizer')
        root_codes = [1 << i for i in range(n)]
        check({subset_step(n,s,True) for s in root_codes} == set(root_codes), 'root permutation')
        print(f'n={n} sources={len(states)} image={len(images)} roots={n} max_tail={n//2} max_fibre={maximum} full_fibres_unchanged=YES')
        total += len(states)
    print(f'full_sources={total}')
    print(f'assertions={checks}')
    print('status=PASS_EXACT_DECOMPOSITION')
    print('disposition=KILL_CONTRIBUTION_ROOT_REWIRED_LAP_ERASURE')
    print('external_status=HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
