#!/usr/bin/env python3
"""Small exact, deterministic scouting boxes; no conjectures are asserted."""
from collections import Counter
from itertools import product
import json


def prev_distance(w):
    last = {}
    out = []
    for i, a in enumerate(w):
        out.append(i - last[a] if a in last else 0)
        last[a] = i
    return tuple(out)


def distinct_suffix(w):
    out = []
    for i in range(len(w)):
        j = i
        while j and w[j-1] not in w[j:i+1]:
            j -= 1
        out.append(i-j)
    return tuple(out)


def palindrome_suffix(w):
    return tuple(max(k for k in range(1, i+2)
                     if w[i-k+1:i+1] == w[i-k+1:i+1][::-1])-1
                 for i in range(len(w)))


def border_count(w):
    return tuple(sum(w[:k] == w[i-k+1:i+1] for k in range(1, i+1))
                 for i in range(len(w)))


def equal_run(w):
    out = []
    for i, a in enumerate(w):
        out.append(out[-1]+1 if i and a == w[i-1] else 0)
    return tuple(out)


def mex(values):
    return next(k for k in range(len(values)+1) if k not in values)


def mex_open_cycle(w):
    return tuple(mex({w[(i-1) % len(w)], w[(i+1) % len(w)]})
                 for i in range(len(w)))


def mex_forward_closed(w):
    return tuple(mex({w[i], w[(i+1) % len(w)]})
                 for i in range(len(w)))


def z_array(w):
    ans = [0]
    for i in range(1, len(w)):
        j = 0
        while i+j < len(w) and w[j] == w[i+j]:
            j += 1
        ans.append(j)
    return tuple(ans)


def profile(states, step):
    states = list(states)
    arrows = {x: step(x) for x in states}
    assert set(arrows.values()) <= set(arrows)
    data = {}
    cycle_counts = Counter()
    witness = None
    for start in states:
        if start in data:
            continue
        path, pos = [], {}
        x = start
        while x not in pos and x not in data:
            pos[x] = len(path)
            path.append(x)
            x = arrows[x]
        if x in pos:
            cut = pos[x]
            period = len(path)-cut
            cycle_counts[period] += 1
            for y in path[cut:]:
                data[y] = (0, period)
            tail = path[:cut]
        else:
            tail = path
        for y in reversed(tail):
            depth, period = data[arrows[y]]
            data[y] = (depth+1, period)
    height = max(d for d, p in data.values())
    witness = next(x for x in states if data[x][0] == height)
    return dict(states=len(states), image=len(set(arrows.values())),
                height=height, max_fibre=max(Counter(arrows.values()).values()),
                cycles=dict(sorted(cycle_counts.items())), witness=witness)


def main():
    for name, step in [('PD', prev_distance), ('DS', distinct_suffix),
                       ('PS', palindrome_suffix), ('BC', border_count),
                       ('ER', equal_run)]:
        for n in range(1, 9):
            states = product(*(range(i+1) for i in range(n)))
            print(json.dumps(dict(candidate=name, n=n, **profile(states, step)),
                             sort_keys=True))
    for n in range(1, 9):
        states = product([0], *(range(n-i+1) for i in range(1, n)))
        print(json.dumps(dict(candidate='ZA', n=n, **profile(states, z_array)),
                         sort_keys=True))
    for name, step in [('MO', mex_open_cycle), ('MC', mex_forward_closed)]:
        for n in range(1, 9):
            print(json.dumps(dict(candidate=name, n=n,
                                  **profile(product(range(3), repeat=n), step)),
                             sort_keys=True))


if __name__ == '__main__':
    main()
