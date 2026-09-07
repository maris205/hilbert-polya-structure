"""Exact finite-coefficient diagnostic; not a universal classification proof."""

import argparse
import json


def cycles_for(a, b, c):
    # A periodic coordinate of maximal absolute value M satisfies
    # M^3 <= |b| M^2 + (|c|+2) M + |a|.  The ratio of the RHS to M^3
    # is decreasing for positive M, so the first failure is an escape bound.
    radius = 1
    while radius**3 <= abs(b)*radius**2+(abs(c)+2)*radius+abs(a):
        radius += 1
    radius -= 1
    alphabet = range(-radius, radius+1)
    seen = set()
    cycles = []
    for x in alphabet:
        for y in alphabet:
            if (x, y) in seen:
                continue
            path = []
            positions = {}
            point = (x, y)
            while max(map(abs, point)) <= radius and point not in seen:
                if point in positions:
                    cycle = path[positions[point]:]
                    word = tuple(p[0] for p in cycle)
                    word = min(word[i:]+word[:i] for i in range(len(word)))
                    cycles.append(word)
                    break
                positions[point] = len(path)
                path.append(point)
                xx, yy = point
                point = (yy, yy**3+b*yy**2+c*yy+a-xx)
            seen.update(path)
    return sorted(cycles, key=lambda w: (len(w), w))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a-max', type=int, default=60)
    parser.add_argument('--c-min', type=int, default=-80)
    parser.add_argument('--c-max', type=int, default=8)
    args = parser.parse_args()
    periods = {}
    maximum = 0
    maximizers = []
    exceptional_alphabets = []
    maps = 0
    for b in (-1, 0, 1):
        for c in range(args.c_min, args.c_max+1):
            for a in range(-args.a_max, args.a_max+1):
                maps += 1
                cycles = cycles_for(a, b, c)
                size = sum(map(len, cycles))
                if size > maximum:
                    maximum, maximizers = size, []
                if size == maximum:
                    maximizers.append([a, b, c, cycles])
                for word in cycles:
                    periods.setdefault(len(word), [a, b, c, word])
                    if len(set(word)) >= 4:
                        exceptional_alphabets.append([a, b, c, word])
    print(json.dumps({
        'scope': vars(args), 'b_values': [-1, 0, 1], 'maps': maps,
        'period_examples': periods, 'max_points_in_scan': maximum,
        'maximizers': maximizers,
        'cycles_with_at_least_four_symbols': exceptional_alphabets,
        'warning': 'Only the displayed finite coefficient scope is certified.'
    }, indent=2))


if __name__ == '__main__':
    main()
