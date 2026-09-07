"""Two predeclared original literals; no historical science imports."""
import collections
import itertools
import json
import os
import sys

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def increasing_blocks(w):
    if not w:
        return []
    cuts = [0] + [i for i in range(1, len(w)) if w[i - 1] > w[i]] + [len(w)]
    return [w[a:b] for a, b in zip(cuts, cuts[1:])]


def orr(w):
    return tuple(x for block in increasing_blocks(w)
                 for x in (block[::-1] if len(block) % 2 else block))


def orr_positions(w):
    out = list(w)
    start = 0
    while start < len(w):
        end = start + 1
        while end < len(w) and w[end - 1] < w[end]:
            end += 1
        if (end - start) % 2:
            for i in range(start, end):
                out[i] = w[start + end - i - 1]
        start = end
    return tuple(out)


def orr_inverse(y):
    if not y:
        return [()], [()]
    sources, codes = [], []
    n = len(y)
    for mask in range(1 << (n - 1)):
        cuts = [0] + [i for i in range(1, n) if mask >> (i - 1) & 1] + [n]
        blocks = [y[a:b] for a, b in zip(cuts, cuts[1:])]
        valid = True
        for block in blocks:
            if len(block) % 2:
                valid &= all(a > b for a, b in zip(block, block[1:]))
            else:
                valid &= all(a < b for a, b in zip(block, block[1:]))
        if not valid or any(max(a) < min(b) for a, b in zip(blocks, blocks[1:])):
            continue
        sources.append(tuple(v for b in blocks for v in (b[::-1] if len(b) % 2 else b)))
        codes.append(tuple(map(len, blocks)))
    return sorted(sources), sorted(codes)


def inversions(w):
    return sum(w[i] > w[j] for i in range(len(w)) for j in range(i + 1, len(w)))


def family(mask, n):
    return tuple(a for a in range(1, 1 << n) if mask >> (a - 1) & 1)


def hxc(h):
    return tuple(sorted({a ^ next((b for b in h if b != a and a & b), 0) for a in h}))


def hxc_sets(h, n):
    old = {a: frozenset(i for i in range(n) if a >> i & 1) for a in h}
    outputs = set()
    for a in h:
        choices = sorted(b for b in h if b != a and old[a].intersection(old[b]))
        new = old[a] ^ old[choices[0]] if choices else old[a]
        outputs.add(sum(1 << i for i in new))
    return tuple(sorted(outputs))


def disjoint(h):
    return all(not a & b for a, b in itertools.combinations(h, 2))


def orbit(start, transition):
    seen, walk = {}, []
    here = start
    while here not in seen:
        seen[here] = len(walk)
        walk.append(here)
        here = transition[here]
    return seen[here], len(walk) - seen[here], walk


def analyze(rule, n, states, transition):
    index = {x: i for i, x in enumerate(states)}
    fibres = [[] for _ in states]
    for i, j in enumerate(transition):
        fibres[j].append(i)
    rows, depths, periods = [], [], []
    for i, x in enumerate(states):
        depth, period, walk = orbit(i, transition)
        check(period == 1, ('no_nonfixed_cycle', rule, n, x))
        if rule == 'ORR':
            fixed = all(len(b) == 1 or len(b) % 2 == 0 for b in increasing_blocks(x))
            check(depth <= (n * (n - 1) // 2 - inversions(x)) // 3, ('inversion_bound', n, x))
            decoded, codes = orr_inverse(x)
            decoded_ids = sorted(index[y] for y in decoded)
            check(decoded_ids == fibres[i], ('full_target_inverse', n, x))
            check(len(decoded) == len(set(decoded)) == len(codes), ('nonredundant', n, x))
        else:
            fixed = disjoint(x)
            check(depth <= max(0, len(x) - 1), ('cardinality_bound', n, x))
            decoded_ids, codes = None, None
        check(fixed == (depth == 0) == (transition[i] == i), ('fixed_locus', rule, n, x))
        rows.append(dict(state=x, successor_index=transition[i], entrance=depth, period=period,
                         fibre_indices=fibres[i], decoded_indices=decoded_ids, interval_codes=codes))
        depths.append(depth)
        periods.append(period)
    maximum = max(map(len, fibres))
    height = max(depths)
    record = dict(rule=rule, n=n, states=len(states), image=sum(bool(f) for f in fibres),
        recurrent=sum(d == 0 for d in depths), max_entrance=height, max_fibre=maximum,
        max_fibre_targets=[states[i] for i, f in enumerate(fibres) if len(f) == maximum],
        max_entrance_states=[states[i] for i, d in enumerate(depths) if d == height],
        deepest_orbit=[states[i] for i in orbit(depths.index(height), transition)[2]],
        fibre_histogram=sorted(collections.Counter(map(len, fibres)).items()),
        depth_histogram=sorted(collections.Counter(depths).items()), rows=rows, checks_cumulative=CHECKS,
        state_order='lexicographic tuples' if rule == 'ORR' else 'increasing family mask on nonempty edge codes')
    print(json.dumps(record, sort_keys=True, separators=(',', ':')), flush=True)


def main():
    total = 0
    for n in range(8):
        states = list(itertools.permutations(range(1, n + 1)))
        index = {x: i for i, x in enumerate(states)}
        transition = []
        for x in states:
            y = orr(x)
            check(y == orr_positions(x), ('two_literals', 'ORR', n, x))
            check(all(x.index(v) % 2 == y.index(v) % 2 for v in x), ('position_parity', n, x))
            check(y == x or inversions(y) > inversions(x), ('strict_inversions', n, x))
            transition.append(index[y])
        analyze('ORR', n, states, transition)
        total += len(states)
    for n in range(5):
        states = [family(mask, n) for mask in range(1 << ((1 << n) - 1))]
        index = {x: i for i, x in enumerate(states)}
        transition = []
        for x in states:
            y = hxc(x)
            check(y == hxc_sets(x, n), ('two_literals', 'HXC', n, x))
            check(all(y) and bool(x) == bool(y), ('nonempty_edges_and_family', n, x))
            check(disjoint(x) or len(y) < len(x), ('strict_cardinality', n, x))
            transition.append(index[y])
        analyze('HXC', n, states, transition)
        total += len(states)
    check(total == 38821, ('intake_total', total))
    print(json.dumps(dict(status='PASS', rules=2, boxes=13, states=total, checks=CHECKS), sort_keys=True), flush=True)
    modules = {name: dict(origin=getattr(getattr(module, '__spec__', None), 'origin', None),
                         file=getattr(module, '__file__', None)) for name, module in sorted(sys.modules.items())}
    with open('/proc/self/maps', encoding='utf8') as source:
        mapped = sorted({line.split()[-1] for line in source if '/' in line and os.path.isfile(line.split()[-1])})
    print(json.dumps(dict(modules=modules, mapped_files=mapped, executable=sys.executable,
        version=sys.version, flags=repr(sys.flags), path=sys.path, xoptions=sys._xoptions,
        byteorder=sys.byteorder), sort_keys=True), file=sys.stderr)


if __name__ == '__main__':
    main()
