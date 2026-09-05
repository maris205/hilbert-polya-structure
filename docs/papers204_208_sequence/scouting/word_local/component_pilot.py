#!/usr/bin/env python3
"""Six bounded fourth root probes. Literal maps, no extrapolated theorem."""
from itertools import product
import json
from pilot import profile


def superlevel_components(w):
    n = len(w)
    result = []
    for a in w:
        high = [b >= a for b in w]
        result.append(max(1, sum(high[i] and not high[(i-1) % n]
                                 for i in range(n))))
    return tuple(result)


def equal_component_size(w):
    n = len(w)
    if len(set(w)) == 1:
        return (n,) * n
    result = []
    for i, a in enumerate(w):
        left = right = 0
        while left < n - 1 and w[(i-left-1) % n] == a:
            left += 1
        while right < n - 1 and w[(i+right+1) % n] == a:
            right += 1
        result.append(left + right + 1)
    return tuple(result)


def weak_increasing_run(w):
    n = len(w)
    answer = []
    for i in range(n):
        length = 1
        while length < n and w[(i+length-1) % n] <= w[(i+length) % n]:
            length += 1
        answer.append(length)
    return tuple(answer)


def balanced_equal_gap(w):
    n = len(w)
    return tuple(max(len(set(w[(i+k) % n] for k in range(d)))
                     for d in range(1, n+1)
                     if w[(i+d) % n] == w[i]) for i in range(n))


def local_upper_basin(w):
    n = len(w)
    result = []
    for i, a in enumerate(w):
        seen = {i}
        for direction in (-1, 1):
            for d in range(1, n):
                j = (i+direction*d) % n
                if w[j] < a:
                    break
                seen.add(j)
        result.append(len(seen))
    return tuple(result)


def strict_prefix_rank(w):
    return tuple(1 + sum(b < a for b in w[:i]) for i, a in enumerate(w))


def main():
    candidates = [('SLC', superlevel_components),
                  ('ECS', equal_component_size),
                  ('WIR', weak_increasing_run),
                  ('BEG', balanced_equal_gap),
                  ('LUB', local_upper_basin),
                  ('SPR', strict_prefix_rank)]
    for name, step in candidates:
        for n in range(1, 7):
            print(json.dumps(dict(candidate=name, n=n,
                                  **profile(product(range(1, n+1), repeat=n), step)),
                             sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
