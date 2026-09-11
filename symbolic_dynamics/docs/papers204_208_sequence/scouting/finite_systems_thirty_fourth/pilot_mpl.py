#!/usr/bin/env python3
"""Original complete n=1..6 MPL pilot, no imported scientific code."""
from collections import Counter
from itertools import product
import json

CHECKS = 0
def check(value):
    global CHECKS
    CHECKS += 1
    assert value

def step(x):
    lengths = [0]
    for stop in range(1, len(x) + 1):
        lengths.append(1 + min(lengths[start] for start in range(stop)
                               if x[start:stop] == x[start:stop][::-1]))
    return tuple(k - 1 for k in lengths[1:])

def brute(x):
    out = []
    for stop in range(1, len(x) + 1):
        best = stop
        for mask in range(1 << (stop - 1)):
            cuts = [0] + [i for i in range(1, stop) if mask >> (i-1) & 1] + [stop]
            if all(x[a:b] == x[a:b][::-1] for a, b in zip(cuts, cuts[1:])):
                best = min(best, len(cuts)-1)
        out.append(best-1)
    return tuple(out)

def emit(row):
    print(json.dumps(row, sort_keys=True, separators=(',', ':')))

def main():
    total = 0
    for n in range(1, 7):
        states = list(product(*(range(i+1) for i in range(n))))
        arrows = {x: step(x) for x in states}
        image = set(arrows.values())
        check(image <= set(states))
        fibres = Counter(arrows.values())
        data = {}
        cycle_counts = Counter()
        for start in states:
            if start in data:
                continue
            path, positions, x = [], {}, start
            while x not in positions and x not in data:
                positions[x] = len(path)
                path.append(x)
                x = arrows[x]
            if x in positions:
                cut = positions[x]
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
        monotone_failures = []
        idempotence_failures = []
        for x in states:
            y = arrows[x]
            check(y == brute(x))
            check(all(abs(y[i]-y[i-1]) <= 1 for i in range(1, n)))
            check(data[x][0] == 0 or data[y][0] == data[x][0]-1)
            check(data[x][1] == data[y][1])
            if x in image and not all(a <= b for a, b in zip(x, y)):
                monotone_failures.append([x, y])
            if x in image and y != x:
                idempotence_failures.append([x, y])
            emit(dict(kind='state', n=n, x=x, next=y, depth=data[x][0],
                      period=data[x][1], fibre=fibres[x]))
        height = max(d for d, _ in data.values())
        max_fibre = max(fibres.values())
        check(sum(fibres[x] for x in states) == len(states))
        emit(dict(kind='summary', n=n, states=len(states), image=len(image),
                  recurrent=sum(d == 0 for d, _ in data.values()), height=height,
                  cycles=sorted(cycle_counts.items()), max_fibre=max_fibre,
                  maximal_targets=[x for x in states if fibres[x] == max_fibre],
                  deepest=[x for x in states if data[x][0] == height],
                  image_monotonicity_failures=monotone_failures,
                  image_nonfixed_arrows=idempotence_failures))
        total += len(states)
    emit(dict(kind='total', states=total, assertions=CHECKS,
              claim='complete original boxes only; not an all-size proof'))

if __name__ == '__main__':
    main()
